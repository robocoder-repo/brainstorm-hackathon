import tensorflow as tf
import numpy as np

# Generate some sample data
X = np.linspace(-1, 1, 100).reshape(-1, 1)
y = 2 * X + np.random.randn(*X.shape) * 0.1

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(X, y, epochs=100, verbose=0)

# Make predictions
X_test = np.linspace(-1, 1, 10).reshape(-1, 1)
predictions = model.predict(X_test)

print("Sample predictions:")
for x, y in zip(X_test, predictions):
    print(f"Input: {x[0]:.2f}, Predicted: {y[0]:.2f}")
