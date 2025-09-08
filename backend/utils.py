import os
import cv2
import numpy as np
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

IMG_SIZE = 64  # Resize all images to 64x64

def load_dataset(dataset_path):
    X = []
    y = []
    classes = sorted(os.listdir(dataset_path))
    class_map = {cls_name: idx for idx, cls_name in enumerate(classes)}

    for cls in classes:
        cls_path = os.path.join(dataset_path, cls)
        for img_name in os.listdir(cls_path):
            img_path = os.path.join(cls_path, img_name)
            img = cv2.imread(img_path)
            if img is None:
                continue
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            X.append(img)
            y.append(class_map[cls])
    
    X = np.array(X, dtype="float32") / 255.0
    y = to_categorical(y, num_classes=len(classes))
    return train_test_split(X, y, test_size=0.2, random_state=42), class_map
