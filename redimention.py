import os
from PIL import Image, UnidentifiedImageError

# Dictionnaire de correspondance des noms de catégories (si nécessaire)
category_mapping = {
   'food': 'nourriture',
'vehicle': 'vehicule',
    'documents': 'documents',
    'fashion': 'fashion'
}


def preprocess_images(input_dir, output_dir, size=(128, 128)):
    # Parcourir chaque catégorie dans le dossier d'entrée
    for category in os.listdir(input_dir):
        category_path = os.path.join(input_dir, category)

        # Vérifier si le nom de la catégorie a une correspondance dans le dictionnaire
        output_category = category_mapping.get(category, category)  # Utilise le même nom si pas de correspondance
        output_category_path = os.path.join(output_dir, output_category)
        os.makedirs(output_category_path, exist_ok=True)

        # Parcourir chaque fichier image dans le dossier de la catégorie
        for img_name in os.listdir(category_path):
            img_path = os.path.join(category_path, img_name)

            # Vérifier que le fichier est une image (formats jpg, jpeg, png)
            if not img_name.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue

            try:
                # Charger et redimensionner l'image
                img = Image.open(img_path).convert("RGB")
                img = img.resize(size)

                # Nouveau nom pour éviter les conflits, avec un préfixe de catégorie
                new_img_name = f"{output_category}_{img_name}"

                # Enregistrer l'image redimensionnée avec le nouveau nom
                img.save(os.path.join(output_category_path, new_img_name))
                print(f"Image traitée et enregistrée : {new_img_name}")

            except UnidentifiedImageError:
                print(f"Erreur : Impossible de lire le fichier image : {img_path}")
            except Exception as e:
                print(f"Erreur inattendue avec le fichier {img_path} : {e}")


# Appel de la fonction
preprocess_images(input_dir=r"C:\ds", output_dir="./combined_dataset")
