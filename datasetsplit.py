import os
import shutil
from sklearn.model_selection import train_test_split

# Define paths
DATASET_DIR = "C:/Users/Medta/Galerie/Galerie-/combined_dataset"
TRAIN_DIR = "C:/Users/Medta/Galerie/Galerie-/train_dataset"
TEST_DIR = "C:/Users/Medta/Galerie/Galerie-/test_dataset"

# Define the split ratio
TEST_RATIO = 0.2  # 20% for testing

# Create train and test directories
os.makedirs(TRAIN_DIR, exist_ok=True)
os.makedirs(TEST_DIR, exist_ok=True)

# Split dataset
for class_name in os.listdir(DATASET_DIR):
    class_path = os.path.join(DATASET_DIR, class_name)
    if not os.path.isdir(class_path):
        continue

    # Create class directories in train and test folders
    os.makedirs(os.path.join(TRAIN_DIR, class_name), exist_ok=True)
    os.makedirs(os.path.join(TEST_DIR, class_name), exist_ok=True)

    # Get all image paths
    images = [os.path.join(class_path, img) for img in os.listdir(class_path) if img.endswith(('jpg', 'jpeg', 'png'))]
    
    # Split into train and test sets
    train_images, test_images = train_test_split(images, test_size=TEST_RATIO, random_state=42)

    # Move images to respective directories
    for img in train_images:
        shutil.copy(img, os.path.join(TRAIN_DIR, class_name, os.path.basename(img)))

    for img in test_images:
        shutil.copy(img, os.path.join(TEST_DIR, class_name, os.path.basename(img)))

print("Dataset successfully split into train and test folders!")
