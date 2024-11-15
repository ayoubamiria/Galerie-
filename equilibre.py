from torchvision import transforms
from PIL import Image
import random
import os

# Transformations de base pour l’augmentation
augment = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.RandomResizedCrop(32)
])


# Appliquer les transformations et sauvegarder
def augment_data(category_dir):
    for img_name in os.listdir(category_dir):
        img_path = os.path.join(category_dir, img_name)
        img = Image.open(img_path).convert("RGB")

        # Appliquer la transformation et sauvegarder une copie
        augmented_img = augment(img)
        new_name = f"aug_{random.randint(0, 9999)}_{img_name}"
        augmented_img.save(os.path.join(category_dir, new_name))


# Appel de la fonction pour une catégorie
augment_data("./combined_dataset/fashion")