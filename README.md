# 🧠 Brain Tumor Detection

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![](https://badgen.net/badge/release/1.2.0/green?icon=github)](https://github.com/giuseppebrb/BrainTumorDetection/releases) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1T8QWGy9V8gpll-veGo_W9fMPVrvZB2dv?usp=sharing)

## Model 
 https://drive.google.com/file/d/11Dswcbv1iZojFeU1-oHyaak9a01qcDtz/view?usp=sharing

## About

This project focuses on building a website that allows users to upload brain MRI images for tumor detection. Using computer vision and deep learning models trained on the yes and no — the system analyzes the images to detect whether a tumor is present or not.


The dataset used in this project has been edited and enlarged starting from this repository on Kaggle: [Brain Tumor Object Detection Dataset](https://www.kaggle.com/datasets/navoneel/brain-mri-images-for-brain-tumor-detection). In total there are ~1.300 images and labels.

## Tech overview

 This will be integrated into a website using the TensorFlow CNC model to enhance tumor identification and provide an accessible, efficient platform for users to upload MRI images and receive predictions directly from the model. The site will feature an intuitive interface, allowing seamless integration between the frontend and the deep learning backend.

A Python environment with [**PyTorch**](https://pytorch.org/get-started/locally/) installed is required to perform both training end/or detection.

## About the repo

You can use the code in this repository in different ways:

1. Train and detect on this **Google Colaboratory** environment [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1T8QWGy9V8gpll-veGo_W9fMPVrvZB2dv?usp=sharing) (TIP: if you select the runtime with GPU, training process will be faster).
2. Train and detect locally by cloning the repository and running this **Jupyter Notebook** file [Brain_Tumor_Detector.ipynb][![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1T8QWGy9V8gpll-veGo_W9fMPVrvZB2dv?usp=sharing) (training time will be determined by your hardware capacity).

## How to use the models


In order to run one of the models please follow these steps:

**1.** Clone the  repository

```
git clone https://github.com/nimradev064/Brain-Tumor-MRI.git
```
```
pip install -r requirements.txt
```

A **label** over the bounding box identifies the **class** of the detection ("tumor" / "not tumor") and besides that is displayed a **confidence score** (**0 minimum** - **1 maximum**).
![output](https://i.imgur.com/sk2Vh1s.jpg)
