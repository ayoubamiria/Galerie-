import torch
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
import torchvision.transforms as transforms

# Définir ton modèle CNN (qui est déjà le même que celui que tu as utilisé pour entraîner le modèle)
class CNNModel(nn.Module):
    def __init__(self, num_classes):
        super(CNNModel, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = nn.Linear(32 * 32 * 32, 128)  # 32*32*32 après convolution et pooling
        self.fc2 = nn.Linear(128, num_classes)  # Nombre de classes

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 32 * 32 * 32)  # Aplatir pour la couche entièrement connectée
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Vérifier la disponibilité du GPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Charger le modèle déjà entraîné avec les poids sauvegardés
model = CNNModel(num_classes=10)  # Remplace 10 par le nombre réel de classes
model.load_state_dict(torch.load("cnn_model.pth", map_location=device))  # Charger les poids du modèle
model.to(device)
model.eval()  # Passer le modèle en mode évaluation

# Transformation complète pour la prédiction (taille et normalisation cohérentes avec l'entraînement)
transform = transforms.Compose([
    transforms.Resize((128, 128)),  # Redimensionner à 128x128 pixels
    transforms.ToTensor(),          # Convertir en tenseur PyTorch
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normalisation pour ResNet
])

# Fonction de prédiction d'image
def predict_image(image_path, model, class_names):
    # Charger l'image
    image = Image.open(image_path).convert("RGB")

    # Appliquer la transformation
    image_tensor = transform(image).unsqueeze(0).to(device)

    # Prédiction
    with torch.no_grad():
        output = model(image_tensor)
        _, predicted_class = torch.max(output, 1)

    return class_names[predicted_class.item()]

# Liste des classes (celles que tu utilises lors de l'entraînement)
class_names = ["fashion", "Feu", "documents", "Paysage", "Personne", "nourriture", "plante", "devices", "animal", "vehicule"]

# Prédire une image spécifique
image_path = "téléchargement.png"  # Remplace par le chemin de ton image
predicted_class = predict_image(image_path, model, class_names)
print(f"La classe prédite est : {predicted_class}")
