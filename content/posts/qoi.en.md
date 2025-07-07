---
title: QOI file format spec
date: 2025-07-07 00:02:21
draft: false
---

The Quite OK Image Format (QOI)

Specification Version 1.0 (2022-01-05)
Source: qoiformat.org – Dominic Szablewski

File Structure

A QOI file consists of:
	•	A 14-byte header
	•	Any number of data “chunks”
	•	An 8-byte end marker

Header

qoi_header {
char     magic[4];   // magic bytes “qoif”
uint32_t width;      // image width in pixels (big-endian)
uint32_t height;     // image height in pixels (big-endian)
uint8_t  channels;   // 3 = RGB, 4 = RGBA
uint8_t  colorspace; // 0 = sRGB with linear alpha, 1 = all channels linear
};
	•	Colorspace and channels are informative only, not affecting chunk encoding.

Encoding Overview

Images are encoded:
	•	Row by row, left to right, top to bottom.
	•	Starting with previous pixel value {r:0, g:0, b:0, a:255}.
	•	Encoding stops when width * height pixels are covered.

Pixels can be encoded as:
	•	A run of the previous pixel
	•	An index into a seen pixels array
	•	A difference to the previous pixel value
	•	Full r,g,b or r,g,b,a values

Color channels are un-premultiplied alpha.

Color Index Array

A running array of 64 previously seen pixel values is maintained, initialized to zero.
Each pixel is stored at an index computed by:

index_position = (r * 3 + g * 5 + b * 7 + a * 11) % 64

If a pixel matches the value at its computed index, QOI_OP_INDEX is written.

Chunks

All chunks:
	•	Start with a 2- or 8-bit tag, followed by data bits.
	•	Are byte-aligned.
	•	Encoded MSB-first.

End Marker
	•	7 bytes of 0x00 followed by a single 0x01.

Chunk Types

QOI_OP_RGB

Byte[0]	Byte[1]	Byte[2]	Byte[3]
11111110	red	green	blue

	•	Tag: 8-bit 0xFE
	•	Stores RGB values.
	•	Alpha remains unchanged.

QOI_OP_RGBA

Byte[0]	Byte[1]	Byte[2]	Byte[3]	Byte[4]
11111111	red	green	blue	alpha

	•	Tag: 8-bit 0xFF
	•	Stores full RGBA values.

QOI_OP_INDEX

Byte[0]
00xxxxxx

	•	Tag: 2-bit 00
	•	6-bit index into the color index array (0..63).
	•	No two consecutive chunks to the same index (use QOI_OP_RUN instead).

QOI_OP_DIFF

Byte[0]
01rrggbb

	•	Tag: 2-bit 01
	•	2-bit diffs for r, g, b channels (-2..1).
	•	Stored as unsigned integers with bias +2:
	•	e.g. -2 stored as 0b00, +1 stored as 0b11.
	•	Uses wraparound for underflow/overflow.
	•	Alpha remains unchanged.

QOI_OP_LUMA

Byte[0]	Byte[1]
10gggggg	rrrrbbbb

	•	Tag: 2-bit 10
	•	Green channel difference: 6 bits (-32..31, bias +32)
	•	Red and blue diffs are relative to green difference:
dr_dg = (cur.r - prev.r) - (cur.g - prev.g)
db_dg = (cur.b - prev.b) - (cur.g - prev.g)
	•	dr_dg and db_dg: 4 bits each (-8..7, bias +8).
	•	Wraparound is used.
	•	Alpha remains unchanged.

QOI_OP_RUN

Byte[0]
11xxxxxx

	•	Tag: 2-bit 11
	•	6-bit run-length for repeating previous pixel (1..62, bias -1).
	•	Values 63 and 64 are illegal (reserved for QOI_OP_RGB/RGBA).

Notes
	•	8-bit tags take precedence over 2-bit tags.
	•	Decoder must check for 8-bit tags first.

