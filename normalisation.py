import os
import shutil

# Exemple de structure de dossier
categories = ["fashion", "Feu", "documents", "Paysage","Personne", "nourriture", "plante" , "devices", "animal", "vehicule"]
base_dir = "./combined_dataset/"

# Crée les sous-dossiers pour chaque catégorie
for category in categories:
    os.makedirs(os.path.join(base_dir, category), exist_ok=True)
