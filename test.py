import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image_dataset_from_directory
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load the saved model
loaded_model = tf.keras.models.load_model('my_model.h5')

# Recompile the model (if necessary)
loaded_model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Path to the test dataset
test_dataset_path = "C:/Users/Medta/Galerie/Galerie-/test_dataset" #changer le path (generaliser)

# Load the test dataset with the correct image size
test_dataset = image_dataset_from_directory(
    test_dataset_path,
    image_size=(256, 256),  # Match this with the input size used during training
    batch_size=32,
    shuffle=False
)

# Evaluate the model
loss, accuracy = loaded_model.evaluate(test_dataset)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

# Get predictions
predictions = np.argmax(loaded_model.predict(test_dataset), axis=-1)

# Get true labels
true_labels = np.concatenate([y.numpy() for _, y in test_dataset], axis=0)

# Class names
class_names = test_dataset.class_names

# Classification report
print("\nClassification Report:")
print(classification_report(true_labels, predictions, target_names=class_names))

# Confusion matrix
conf_matrix = confusion_matrix(true_labels, predictions)

# Plot confusion matrix
plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
plt.title("Confusion Matrix")
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.show()
