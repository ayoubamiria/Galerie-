from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
import os
import numpy as np

# Set the path to your dataset
dataset_path = 'C:/Users/Medta/Galerie/Galerie-/combined_dataset'

# Create an ImageDataGenerator instance for data augmentation
datagen = ImageDataGenerator(
    rotation_range=30,      # Random rotation between 0-30 degrees
    width_shift_range=0.2,  # Randomly shift images horizontally
    height_shift_range=0.2, # Randomly shift images vertically
    shear_range=0.2,        # Shear transformation
    zoom_range=0.2,         # Random zoom
    horizontal_flip=True,   # Random horizontal flip
    fill_mode='nearest'     # Fill missing pixels with the nearest value
)

# Function to augment images in a specific class folder
def augment_images_in_class(class_name):
    class_path = os.path.join(dataset_path, class_name)
    save_path = os.path.join(class_path, 'augmented')  # Folder to save augmented images
    os.makedirs(save_path, exist_ok=True)  # Create the folder if it doesn't exist

    # Loop through all images in the class folder
    for img_name in os.listdir(class_path):
        img_path = os.path.join(class_path, img_name)
        
        # Skip directories, we only want image files
        if os.path.isdir(img_path):
            continue
        
        # Load the image
        img = image.load_img(img_path)
        x = image.img_to_array(img)  # Convert image to array
        x = np.expand_dims(x, axis=0)  # Expand dims to make it a batch of 1

        # Augment the image and save it to the augmented folder
        i = 0
        for batch in datagen.flow(x, batch_size=1, save_to_dir=save_path, save_prefix='aug', save_format='jpeg'):
            i += 1
            if i > 1:  # To double the number of images, augment each image once (original + 1 augmented)
                break

# Loop through each class folder and augment the images
for class_name in os.listdir(dataset_path):
    class_folder_path = os.path.join(dataset_path, class_name)
    if os.path.isdir(class_folder_path):  # Only process folders (representing classes)
        augment_images_in_class(class_name)

print("Data augmentation completed!")
