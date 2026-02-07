# Binary Image Classification: Cats vs. Dogs using MobileNetV2 Transfer Learning

## Project Overview
This project implements a Convolutional Neural Network (CNN) for the binary classification of images depicting cats and dogs. The solution leverages Transfer Learning techniques, utilizing the MobileNetV2 architecture pre-trained on the ImageNet dataset as a feature extractor.

The primary objective was to develop a high-accuracy model capable of operating on a limited dataset while minimizing computational costs and overfitting. The final model achieved a test set accuracy of 96.00%, significantly exceeding the 63% benchmark required for the Machine Learning with Python certification by freeCodeCamp.

## Key Performance Metrics
* Test Set Accuracy: 96.00%
* Architecture: MobileNetV2 (Feature Extraction)
* Training Time: 15 Epochs
* Optimizer: Adam (Learning Rate: 0.001)

## Methodology and Technical Implementation

### 1. Data Preprocessing
The implementation utilizes the native preprocessing_function provided by tensorflow.keras.applications.mobilenet_v2.
* Rationale: MobileNetV2 requires input data normalized within the range [-1, 1]. Using the model-specific preprocessing function ensures that the input distribution matches the statistical properties of the data used during the original ImageNet pre-training, thereby maximizing the efficacy of feature extraction.

### 2. Data Augmentation Strategy
To mitigate overfitting inherent to small datasets, a robust data augmentation pipeline was applied during the training phase. The ImageDataGenerator was configured with the following parameters:
* Rotation Range: 40 degrees
* Width/Height Shift: 0.2
* Shear Range: 0.2
* Zoom Range: 0.2
* Horizontal Flip: True

These transformations compel the model to learn invariant structural features rather than memorizing specific pixel arrangements.

### 3. Model Architecture
The model follows a Feature Extraction transfer learning approach:
1. Base Model: MobileNetV2 instantiated with include_top=False and weights='imagenet'. The weights of the base model were frozen (trainable=False).
2. GlobalAveragePooling2D: Applied to reduce the spatial dimensions of the feature maps to a single vector, minimizing the parameter count.
3. Dropout (0.5): A high dropout rate was implemented to introduce regularization, reducing the risk of over-confidence in predictions and further preventing overfitting.
4. Output Layer: A Dense layer with a single unit and Sigmoid activation function for binary classification.

### 4. Training Configuration
* Optimizer: Adam with an initial learning rate of 0.001.
* Loss Function: BinaryCrossentropy.
* Callbacks: EarlyStopping (patience of 6) and ReduceLROnPlateau (factor of 0.2) were utilized to ensure optimal convergence and prevent overfitting.

## Performance Analysis
The model demonstrates high robustness and generalization capabilities. Analysis of the Confusion Matrix reveals that residual errors (approx. 4%) are primarily restricted to ambiguous cases, such as images with extreme low-light conditions or significant occlusion. The training and validation loss curves remain parallel throughout the process, indicating a healthy convergence.

## Dependencies
* Python 3.x
* TensorFlow 2.x
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn