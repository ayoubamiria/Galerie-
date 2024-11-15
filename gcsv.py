import csv
import os

def create_csv(data_dir, output_csv):
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["filename", "category", "source"])

        for category in os.listdir(data_dir):
            category_path = os.path.join(data_dir, category)
            for img_name in os.listdir(category_path):
                writer.writerow([os.path.join(category, img_name), category, "combined_dataset"])


# Appel de la fonction
create_csv(data_dir="./combined_dataset", output_csv="dataset_labels.csv")
