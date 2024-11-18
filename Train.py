import tensorflow as tf

# Set image size and batch size
image_size = (256, 256)
batch_size = 32

# Load the dataset
train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    'C:/Users/Medta/Galerie/Galerie-/combined_dataset',
    image_size=image_size,
    batch_size=batch_size,
    label_mode='int'
)

# Normalize pixel values to [0, 1]
train_dataset = train_dataset.map(lambda x, y: (x / 255.0, y))

# Define the CNN model
model = tf.keras.Sequential([
    tf.keras.layers.Rescaling(1./255, input_shape=(256, 256, 3)),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)  # 10 classes, adjust if needed
])

# Compile the model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Train the model
model.fit(train_dataset, epochs=10)


# Save the trained model
model.save('my_model.h5')
