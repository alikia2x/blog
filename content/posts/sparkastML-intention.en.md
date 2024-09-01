---
title: Technical Summary of sparkastML Intent Recognition Model
date: 2024-09-01T22:44:34+08:00
draft: false
summary: I spent three days upgrading the intent recognition model for sparkast and established the sparkastML open-source deep learning lab repository, which will provide better search enhancement features for our products in the future.
tags:
    - sparkast
    - machine learning
    - deep learning
    - artificial intelligence
    - open source
    - frontend
---

## Data Processing

The project initially used a dataset based on nlp.js from sparkhome,
then generated additional data through AI technology,
and finally revised it manually.

## Model Architecture Design

The model architecture includes three layers of convolutional networks with kernel sizes of 3, 4, and 5, each followed by batch normalization.
ReLU is used as the activation function, and adaptive max pooling technology is applied.
Features are concatenated, and a dropout mechanism is introduced to enhance generalization, finally outputting results through a fully connected layer.

## Model Structure

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

## Detailed Model Features

### Input Processing

The model uses the [`phi3-mini-4k-instruct`](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/) tokenizer for word segmentation,
and converts the segmented token IDs into 128-dimensional feature vectors through an embedding layer, as model input.

### Embedding Layer Optimization

The embedding layer is extracted from the phi3 model, with its original dimension being 3072.
To achieve lightweight inference, PCA (Principal Component Analysis) technology is used to reduce it to 128 dimensions,
and saved as a 16MB binary file for easy read and write operations in JS environments.

### Application of Energy-based Models

The initial model performed poorly in handling inputs that "do not belong to any known category."
Inspired by LLM's suggestions, the concepts of OSR (Open Set Recognition) and Energy-based Models are introduced.

> Reference paper [Glocal Energy-based Learning for Few-Shot Open-Set Recognition](https://arxiv.org/abs/2304.11855)

We added an energy calculation module to the existing classification model.

Specifically, during training, by adjusting the loss function, the energy of noisy inputs (i.e., semantically inputs that do not belong to known categories) is maximized,
while the energy of sample inputs is minimized.

The noisy dataset is mixed with Gaussian noise and manually specified data; in practice, using only Gaussian noise can achieve good results.  

During inference, the model calculates the energy value along with the output category and sets a threshold,
inputs above this threshold are identified as noise or unknown categories, effectively solving the open set recognition problem.

The initial attempt with the OpenMax method did not perform well and did not meet expectations.

### JS/TS Integration and Browser-side Inference Implementation

The ultimate goal of this project is to implement model inference in JS/TS environments.

To this end, the model is exported in ONNX format and run in the JS environment using Microsoft's onnxruntime library.

Since the model input is an embedding sequence, the mapping from tokens to embedding vectors is pre-saved as a file for JS to read.

For word segmentation, considering that some regions cannot access huggingface, the original dictionary is extracted from the phi3 model and a segmenter that behaves according to phi3 is developed.

## Open Source

This project is open-sourced under the [MIT](https://opensource.org/license/mit) license, and the source code is located on [GitHub](https://github.com/alikia2x/sparkastml).

Thanks to Microsoft [`phi3`](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/) and [`srcbook`](https://github.com/srcbookdev/srcbook) for their support on this project.
