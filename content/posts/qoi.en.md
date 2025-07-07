---
title: QOI file format spec
date: 2025-07-07 00:02:21
draft: false
---


File Structure

A QOI file consists of:

	•	A 14-byte header

	•	Data chunks

	•	An 8-byte end marker

Header Format
qoi_header {
  char magic[4];       // Magic bytes "qoif"
  uint32_t width;      // Image width in pixels (Big Endian)
  uint32_t height;     // Image height in pixels (Big Endian)
  uint8_t channels;    // 3 = RGB, 4 = RGBA
  uint8_t colorspace;  // 0 = sRGB with linear alpha, 1 = all channels linear
}
	•	colorspace and channels are purely informative

	•	Images are encoded row by row, left to right, top to bottom

	•	Decoder/encoder starts with {r:0, g:0, b:0, a:255} as the previous pixel

Pixel Encoding Methods

	•	Run of the previous pixel

	•	Index into a color index array

	•	Difference from the previous pixel

	•	Full RGB or RGBA values

Color Index Array

	•	A running array [64] of previously seen pixels

	•	Index position calculated by:
index_position = (r * 3 + g * 5 + b * 7 + a * 11) % 64
Chunk Structure

	•	Each chunk starts with a 2 or 8-bit tag

	•	All chunks are byte-aligned

	•	8-bit tags take precedence over 2-bit tags

Chunk Types

8-bit Tags

	•	QOI_OP_RGB (Tag: b11111110):

	◦	8-bit red channel

	◦	8-bit green channel

	◦	8-bit blue channel

	◦	Alpha remains unchanged

	•	QOI_OP_RGBA (Tag: b11111111):

	◦	8-bit red channel

	◦	8-bit green channel

	◦	8-bit blue channel

	◦	8-bit alpha channel

2-bit Tags

	•	QOI_OP_INDEX (Tag: b00):

	◦	6-bit index into color array (0-63)

	◦	No consecutive identical indices allowed

	•	QOI_OP_DIFF (Tag: b01):

	◦	2-bit red difference (-2 to 1)

	◦	2-bit green difference (-2 to 1)

	◦	2-bit blue difference (-2 to 1)

	◦	Values stored with bias of 2

	•	QOI_OP_LUMA (Tag: b10):

	◦	6-bit green difference (-32 to 31)

	◦	4-bit red difference minus green difference (-8 to 7)

	◦	4-bit blue difference minus green difference (-8 to 7)

	◦	Green bias: 32, red/blue bias: 8

	•	QOI_OP_RUN (Tag: b11):

	◦	6-bit run-length (1-62)

	◦	Run-length stored with bias of -1

	◦	63 and 64 are invalid

End Marker

	•	7 x 00 bytes followed by 0x01 byte
