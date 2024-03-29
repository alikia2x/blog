---
title: 第四课-变量和数据
tags:
  - 计算机
  - python教程
date: 2022-08-08 18:12:52
---

## 变量

还记得我们在第三课中运行的 HelloWorld 程序吗？  
它长这样:

```python
print("Hello,wolrd!")
```

接下来，我们对它做一些改动，变成这样

```python
message="Hello,world!"
print(message)
```

保存运行，你会得到和之前相同的结果。那么我们究竟作了什么更改呢？可以看到，新代码的第一行为 `message="Hello,world!"`，它表示我们定义了一个叫做 *message* 的 **变量**。编程中的变量与数学中相似，但不完全相同。编程中，变量用于 **保存数据**。每一个变量都存储了一个 **值**，它就是变量存储的数据，而我们还会给它起一个名字，即 **变量名**。在这个例子中，变量名是 *message*，值(存储的数据)为字符串 *Hello, world!*。

### 知识点

- **变量**，可以简单理解为装数据的盒子。这个盒子的名字，叫 **变量名**，而里面放的数据就是 **值**。既然被成为 **变** 量，那么就表明盒子里面的东西（值）是可以改变的，这个我们稍后再提。

- `message="Hello,world!"` 这一行代码更准确地说是在给变量 **赋值**。**赋值**，顾名思义，就是给变量规定一个值，也就是将你要存储的东西放在变量中。因为在某些编程语言中，变量需要先声明，再赋值。而 Python 中，变量第一次赋值时，Python 就会自动“声明”这个变量，并将其保存到内存中。

- Python 中，给变量赋值的语法为 **`变量名=值`**

### 变量的命名

在大多数时候，你可以随意选用你喜欢的变量名。但是有一些规则需要注意。

- 变量名可以是字母、数字、下划线，也可以是中文（由于 Python3 支持了 [Unicode](../binary#unicode) 编码，因此可以用包括中文在内的很多非英文字符作为变量名，但是 *不建议* 这么做）
- 变量 **不能** 包含空格，但是可以使用下划线。因此，如果你需要用多个单词作为变量名，有两种方法。第一种是用下划线分割，如 `greeting_message`，也可以使用驼峰法，也就是除第一个单词之外，其他单词首字母大写，如 `greetingMessage`。
- 不能使用 Python 关键字和函数名作为变量名
- 变量名需要尽可能让人能看出它的作用。如 `name` 要比 `n` 好。

### 避免错误

在编程过程中，我们常常会犯一些错误。我们要学会识别错误，并想办法解决它。请看一个代码实例：

```python
message="Hello,world!"
print(messge)
```

运行代码后，你会得到一个 **Traceback**:

```text
Traceback (most recent call last):
  File "D:/Desktop/hello_world.py", line 2, in <module>
    print(messge)
NameError: name 'messge' is not defined. Did you mean: 'message'?
```

当你遇到 **Traceback** 时，表明你的代码出现了错误。**Traceback** 是一条记录，指出了 Python 解释器 [^1] 在尝试运行代码时，在什么地方遇见了错误。第二行告诉我们出错的代码位于文件 `D:/Desktop/hello_world.py` 的第 2 行，第 3 行则显示了出错的具体代码 `print(messge)` ，而第 4 行显示了出错的具体原因和修改建议。

我们要结合第 2-4 行的信息来分析错误。首先，第 4 行的信息最为详细，它告诉我们，"messge" 这个变量没有定义，并询问我们是否想要使用 "message" 这个变量。那么我们看回 traceback 的第 3 行，发现我们在使用 print 函数时，给它传递的参数是一个叫 "messge" 的变量。而在代码第 1 行，却只给名为 "message" 的变量进行了赋值操作，因此 python 解释器提示出错。

正确的代码如下:

```python
message="Hello,world!"
print(message)
```

[^1]: Python解释器是用于执行Python代码的程序，当你执行代码时，它会逐行解析你的代码并执行。

> 刚刚我们提到，我们在使用 print 函数时，为它提供的参数是一个变量。而在第三课的代码中，我们给 print 提供的参数是一个字符串。实际上，对于 print 函数来说，它们都是一个变量，而 print 函数需要的变量是字符串类型的，因此直接传递字符串和传递一个字符串类型的变量是一样的效果。

## 数据类型

数据类型，顾名思义就是数据的类型(废话）。在 python 中，数据有很多种类型，我们之前提到的 **字符串** 就是其中一种。

除了字符串，python 中常见的数据类型还有整型、浮点型。

整型(int)，和浮点型(float)一样，都属于数字。区别在于，整型变量存储的是 **整数**，而浮点型变量存储的是 **小数**（浮点数）。

让我们来直接看例子吧。

```python
height=1.8
print("My height is",height)
```

运行代码，你会看到一行输出: `My height is 1.8`

这个例子展示了浮点数和字符串同时作为参数给 print 函数的情况。之前的例子中，我们给 print 函数提供的参数是 **字符串**，
