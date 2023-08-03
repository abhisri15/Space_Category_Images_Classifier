# Space Image Classifier

This project focuses on building an image classifier to identify different categories of space images using deep learning. It consists of a Jupyter Notebook (`space-image-classifier.ipynb`) for model training and evaluation, and a Flask web application (`app.py`) for making predictions on new images.

## Jupyter Notebook - `space-image-classifier.ipynb`

The Jupyter Notebook contains the code for:

1. Loading and preprocessing the space image dataset.
2. Creating a deep learning model using the DenseNet201 architecture.
3. Compiling and training the model on the dataset.
4. Saving the trained model.

## Flask Web Application - `app.py`

The Flask web application allows users to upload space images and receive predictions for their categories. The application performs the following tasks:

1. Loads the trained classification model.
2. Accepts image uploads from users.
3. Preprocesses the uploaded image and makes a prediction using the trained model.
4. Displays the predicted category along with the uploaded image on the web interface.

## Prerequisites

- TensorFlow and Keras libraries
- Flask library
- OpenCV (cv2) library

Install the required libraries using the following command:

```bash
pip install tensorflow flask opencv-python
```

## Dataset

The space image dataset used for training is stored in the /kaggle/input/space-images-category/space images directory. It contains images categorized into 'stars', 'galaxies', 'planets', 'cosmos', 'constellation', and 'nebula'.
