---
title: sparkastML 意图识别模型技术总结
date: 2024-09-01T22:44:34+08:00
draft: false
summary: 我花了三天时间，升级了 sparkast 的意图识别模型，并建立了 sparkastML 这个开源深度学习实验室仓库，在未来给我们的产品提供更好的搜索增强功能。
tags:
    - sparkast
    - 机器学习
    - 深度学习
    - 人工智能
    - 开源
    - 前端
---

## 数据处理

本项目初期采用 sparkhome 基于 nlp.js 的数据集，
随后通过 AI 技术生成额外数据，
并由人工进行最终修订。

## 模型架构设计

模型架构包含三层卷积网络，核大小分别为 3, 4, 5，每层后接批归一化处理。
采用 ReLU 作为激活函数，并应用自适应最大池化技术。
特征通过拼接后，引入 dropout 机制增强泛化能力，最终通过全连接层输出结果。

## 核心代码

```python
import torch.nn as nn
import torch.nn.functional as F

class TextCNN(nn.Module):
    def __init__(self, input_dim, num_classes):
        super(TextCNN, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=input_dim, out_channels=DIMENSIONS, kernel_size=3, padding=1)
        self.conv2 = nn.Conv1d(in_channels=DIMENSIONS, out_channels=DIMENSIONS, kernel_size=4, padding=1)
        self.conv3 = nn.Conv1d(in_channels=DIMENSIONS, out_channels=DIMENSIONS, kernel_size=5, padding=2)
        
        self.bn1 = nn.BatchNorm1d(DIMENSIONS)
        self.bn2 = nn.BatchNorm1d(DIMENSIONS)
        self.bn3 = nn.BatchNorm1d(DIMENSIONS)
        
        self.dropout = nn.Dropout(0.5)
        self.fc = nn.Linear(DIMENSIONS * 3, num_classes)

    def forward(self, x):
        x = x.permute(0, 2, 1)  # Change the input shape to (batch_size, embedding_dim, seq_length)
        
        x1 = F.relu(self.bn1(self.conv1(x)))
        x1 = F.adaptive_max_pool1d(x1, output_size=1).squeeze(2)
        
        x2 = F.relu(self.bn2(self.conv2(x)))
        x2 = F.adaptive_max_pool1d(x2, output_size=1).squeeze(2)
        
        x3 = F.relu(self.bn3(self.conv3(x)))
        x3 = F.adaptive_max_pool1d(x3, output_size=1).squeeze(2)
        
        x = torch.cat((x1, x2, x3), dim=1)
        x = self.dropout(x)
        x = self.fc(x)
        return x
```

## 模型特点详述

### 输入处理

模型采用 [`phi3-mini-4k-instruct`](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/) 的 tokenizer 进行词元分割，
并通过嵌入层将分割后的词元编号转换为 128 维的特征向量，作为模型输入。

### 嵌入层优化

从 phi3 模型中提取嵌入层，其原始维度为 3072。
为实现轻量化推理，采用 PCA（主成分分析）技术将其降维至 128 维，
并保存为约 16MB 的二进制文件，以便于 JS 环境下的读写操作。

### 基于能量的模型应用

初始模型在处理“不属于任何一个已知类别”的输入时表现不佳。  
借鉴 LLM 的建议，引入 OSR 开集识别和基于能量的模型(Energy-based Model)概念。

> 参考论文 [Glocal Energy-based Learning for Few-Shot Open-Set Recognition](https://arxiv.org/abs/2304.11855)

我们在现有分类模型中加入了能量计算模块。
具体来说，在训练过程中，通过调整损失函数，使噪声输入（即语义上不属于已知类别的输入）的能量最大化，
而样本输入的能量最小化。  
噪声数据集混合了高斯噪声及人工指定的数据，实际应用中仅使用高斯噪声亦能取得良好效果。  
推理阶段，模型在输出类别的同时计算能量值，并设定阈值，
高于该阈值的输入将被识别为噪声或 unknown 类别，有效解决了开集识别问题。

初期尝试的 OpenMax 方法效果不佳，未能发挥预期作用。

### JS/TS 整合与浏览器端推理实现

本项目最终目标是在 JS/TS 环境中实现模型推理。  
为此，模型被导出为 ONNX 格式，并借助微软的 onnxruntime 库在 JS 环境中运行。  
由于模型输入为嵌入序列，预先将词元到嵌入向量的映射保存为文件供 JS 读取。  
词元分割部分，考虑到某些地区无法访问 huggingface，故从 phi3 模型中提取原始词典，并开发了符合 phi3 行为的分割器。

## 项目开源地址

本项目在 [MIT](https://opensource.org/license/mit) 协议下开源，项目源代码位于 [GitHub](https://github.com/alikia2x/sparkastml).

感谢微软 [phi3](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/) 与 [srcbook](https://github.com/srcbookdev/srcbook) 对本项目的支持。
