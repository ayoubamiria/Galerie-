import csv
import os

import csv
import os
from PIL import Image  # Pillow pour analyser les images

def create_csv(data_dir, output_csv):
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Ajouter des colonnes pour les nouvelles caractéristiques
        writer.writerow(["filename", "category", "source", "resolution", "format"])

        for category in os.listdir(data_dir):
            category_path = os.path.join(data_dir, category)
            if not os.path.isdir(category_path):
                continue
            for img_name in os.listdir(category_path):
                try:
                    img_path = os.path.join(category_path, img_name)
                    with Image.open(img_path) as img:
                        resolution = f"{img.width}x{img.height}"  # Largeur x Hauteur
                        img_format = img.format  # Format de l'image (e.g., JPEG, PNG)
                    writer.writerow([os.path.join(category, img_name), category, "combined_dataset", resolution, img_format])
                except Exception as e:
                    print(f"Erreur avec le fichier {img_name}: {e}")
    print(f"Fichier CSV généré avec succès à : {output_csv}")

# Appel de la fonction
create_csv(data_dir="./combined_dataset", output_csv="dataset_labels.csv")



# Appel de la fonction
create_csv(data_dir="./combined_dataset", output_csv="dataset_labels.csv")
