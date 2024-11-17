import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from PIL import Image

# Charger le fichier CSV
data = pd.read_csv("dataset_labels.csv")

# Afficher les 5 premières lignes
print(data.head())
# Vérifier les dimensions du dataset
print(f"Nombre de lignes et colonnes : {data.shape}")

# Vérifier les types de données
print(data.info())
# description de dataset
print(data.describe())

#Visualiser les données avec Seaborn

# Compter les occurrences de chaque catégorie
sns.countplot(x="category", data=data)
plt.xticks(rotation=45)  # Faire pivoter les noms des catégories pour lisibilité
plt.title("Distribution des catégories")
plt.show()

import os
from PIL import Image


# Fonction pour afficher des échantillons
def display_images_from_category(category, dataset_dir, num_images=5):
    category_path = os.path.join(dataset_dir, category)
    images = os.listdir(category_path)[:num_images]

    plt.figure(figsize=(10, 5))
    for i, img_name in enumerate(images):
        img_path = os.path.join(category_path, img_name)
        img = Image.open(img_path)
        plt.subplot(1, num_images, i + 1)
        plt.imshow(img)
        plt.axis('off')
        plt.title(category)
    plt.show()


# Appel de la fonction
display_images_from_category("devices", "./combined_dataset", num_images=5)


