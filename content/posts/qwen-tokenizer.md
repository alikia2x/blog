---
title: Qwen(千问)系列大模型的tokenizer为什么是乱码？
date: 2024-10-06T23:22:18+08:00
draft: false
summary: Qwen系列大模型的tokenizer的vocabulary（词典）看起来有点奇怪似乎全是乱码？这是因为它对原始Unicode做了一些变换。
---

最近在使用 Qwen 系列模型做一系列 ML 领域的探索，但是当我注意到它的 tokenizer（词元分割器）部分时，却发现有一点奇怪。

具体是怎么个奇怪呢？

我们看一看下面这个例子：

![千问模型 tokenizer 的行为](/img/qwen-tokenizer-behaviour.png)

其中，“你好”对应的词元编号为 108386，而“世界”则为 99489.

但是，当我们查看 `Qwen/Qwen2.5-7B` 的词元映射表文件(`vocab.json`)，却会发现 108386 对应的字符串是 `"ä½łå¥½"`，而 99489 对应的则是 `ä¸ĸçķĮ`.

和原始的输入并不一样，而是变成了乱码。为什么呢？

这是因为，千问系列模型实际上对原始的字节流进行了变换，而这个变换来源于 GPT-2 的词元分割器。

其原始代码如下：

```python
def bytes_to_unicode():
    """
    Returns list of utf-8 byte and a mapping to unicode strings. We specifically avoids mapping to whitespace/control
    characters the bpe code barfs on.

    The reversible bpe codes work on unicode strings. This means you need a large # of unicode characters in your vocab
    if you want to avoid UNKs. When you're at something like a 10B token dataset you end up needing around 5K for
    decent coverage. This is a significant percentage of your normal, say, 32K bpe vocab. To avoid that, we want lookup
    tables between utf-8 bytes and unicode strings.
    """
    bs = (
        list(range(ord("!"), ord("~") + 1)) + list(range(ord("¡"), ord("¬") + 1)) + list(range(ord("®"), ord("ÿ") + 1))
    )
    cs = bs[:]
    n = 0
    for b in range(2**8):
        if b not in bs:
            bs.append(b)
            cs.append(2**8 + n)
            n += 1
    cs = [chr(n) for n in cs]
    return dict(zip(bs, cs))
```

我们也可以得到其 TypeScript 版本：

```typescript
function bytesToUnicode(): { [key: number]: string } {
    const bs: number[] = [
        ...Array.from({ length: 126 - 33 + 1 }, (_, i) => 33 + i), // range(ord("!"), ord("~") + 1)
        ...Array.from({ length: 172 - 161 + 1 }, (_, i) => 161 + i), // range(ord("¡"), ord("¬") + 1)
        ...Array.from({ length: 255 - 174 + 1 }, (_, i) => 174 + i)  // range(ord("®"), ord("ÿ") + 1)
    ];

    const cs: number[] = [...bs];
    let n = 0;

    for (let b = 0; b < 256; b++) {
        if (!bs.includes(b)) {
            bs.push(b);
            cs.push(256 + n);
            n++;
        }
    }

    const csChars: string[] = cs.map(n => String.fromCharCode(n));
    return Object.fromEntries(bs.map((b, i) => [b, csChars[i]]));
}
```

这会生成一个原始字节(0-255 的整数表示)到“乱码”字符（Unicode）的映射表。

例如，一个十进制为 136 (0x88)的字节，其对应的 Unicode 字符为 `Ī`.

有了映射关系，我们在解码时只需要反向查找乱码的字符串，将其换原为原始的字节即可。
