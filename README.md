# Galerie-
# 🌟 Image Organizer & Classifier 🔍

Welcome to the **Image Organizer & Classifier** repository! 🚀  
This project leverages **Deep Learning** to efficiently **classify, organize, and analyze images** for various use cases, including:  
📸 Assisting journalists with image management  
🔥 Identifying fire hazards from images  
🐾 Supporting veterinarians in determining animal breeds  

---

## 🖥️ Features  
✨ **State-of-the-art Models**: Utilizing ResNet-18 and CNN architectures.  
✨ **User-friendly Outputs**: Provides a clean classification system for easy interpretation.  
✨ **Scalable & Adaptive**: Designed to be applicable across industries (journalism, safety, veterinary, etc.).  
✨ **Optimized Performance**: Validated through Cross-Validation (CV=4) to find the best hyperparameters.

---

## 📽️ Demo  

![Demo GIF](https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif)  
_Showcasing the classification and organization in action!_

---

## 🚀 How It Works  

1. **Upload Images**: The model accepts batches of images.  
2. **Feature Extraction**: Automatically identifies patterns using convolutional layers.  
3. **Classification**: Groups images into predefined categories.  
4. **Organized Output**: Generates a structured gallery.  

### 💡 Applications:  
- **Journalism**: Categorize large photo collections for easier reporting.  
- **Safety**: Detect potential fire hazards from drone or surveillance images.  
- **Veterinary**: Assist in identifying animal breeds from photos.  

---

## 📊 Model Architecture  

We leverage a combination of **ResNet-18** and **custom CNN models** to achieve high accuracy and scalability.  
Below is the architecture used:  

![ResNet Architecture](https://miro.medium.com/max/1400/1*wnPmdm7_oAhDv4U40gEOjQ.png)  
_ResNet-18 Backbone_

---

## 🛠️ Installation  

```bash
# Clone the repository
git clone https://github.com/your-repo/Image-Organizer-Classifier.git

# Navigate to the folder
cd Image-Organizer-Classifier

# Install dependencies
pip install -r requirements.txt

# Run the project
python app.py

