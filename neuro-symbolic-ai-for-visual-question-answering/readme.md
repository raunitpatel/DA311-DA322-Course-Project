# Neuro-Symbolic AI for Visual Question Answering (VQA) on the Sort-of-CLEVR Dataset

This repository implements a **Neuro-Symbolic AI (NSAI)** approach for **Visual Question Answering (VQA)** on the **Sort-of-CLEVR** dataset. By combining deep learning's pattern recognition abilities with symbolic reasoning methods like program synthesis, this approach achieves **over 99% accuracy** on the dataset.

## Overview

The NSAI approach for VQA consists of three key modules:
1. **Perception Module**: Extracts a symbolic representation of the visual scene.
2. **Semantic Parser**: Converts the natural language query into an executable program.
3. **Program Executor**: Executes the program on the symbolic scene to find the answer.

This method allows precise reasoning over images based on natural language queries.

## Key Features
- **State-of-the-Art Accuracy**: Over 99% accuracy on the Sort-of-CLEVR dataset.
- **End-to-End Pipeline**: From training individual modules to full integration, all steps are covered.
- **Interpretability**: Symbolic reasoning allows for better interpretability of the results.

## Requirements

- **PyTorch** (<= 1.7)
- **Torchtext** (<= 0.8.0)
- **Torchvision** (<= 0.8.0)
- **OpenCV**
- **dlib**: Used for object detection and other visual tasks.
- **Scikit Learn**: For various machine learning utilities.
- **Pandas & Numpy**: For data manipulation and processing.

## Installation

To install the necessary dependencies, run the following command:

```bash
pip install torch<=1.7.0 torchtext<=0.8.0 torchvision<=0.8.0 opencv-python dlib scikit-learn pandas numpy
```

## References
- [Neural-Symbolic VQA: Disentangling Reasoning from Vision and Language Understanding](https://arxiv.org/abs/1810.02338)
- [The Neuro-Symbolic Concept Learner: Interpreting Scenes, Words, and Sentences From Natural Supervision](https://arxiv.org/abs/1904.12584)
- [Seq2Seq Transformer](https://github.com/aladdinpersson/Machine-Learning-Collection/blob/master/ML/Pytorch/more_advanced/seq2seq_transformer/seq2seq_transformer.py)
- [Object detection using dlib](https://www.learnopencv.com/training-a-custom-object-detector-with-dlib-making-gesture-controlled-applications/)
