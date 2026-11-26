import numpy as np

# 1. Activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# 2. Input dataset (XOR problem) and expected outputs
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([[0], [1], [1], [0]])

# 3. Initialize weights and biases randomly
np.random.seed(42)
input_size = 2
hidden_size = 4
output_size = 1

W1 = np.random.uniform(-1, 1, (input_size, hidden_size))
b1 = np.zeros((1, hidden_size))

W2 = np.random.uniform(-1, 1, (hidden_size, output_size))
b2 = np.zeros((1, output_size))

learning_rate = 0.5
epochs = 10000

# 4. Training loop
for epoch in range(epochs):
    # --- Forward Pass ---
    hidden_input = np.dot(X, W1) + b1
    hidden_output = sigmoid(hidden_input)
    
    final_input = np.dot(hidden_output, W2) + b2
    predicted_output = sigmoid(final_input)
    
    # --- Backpropagation ---
    error = y - predicted_output
    d_output = error * sigmoid_derivative(predicted_output)
    
    error_hidden = d_output.dot(W2.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)
    
    # --- Update Weights and Biases ---
    W2 += hidden_output.T.dot(d_output) * learning_rate
    b2 += np.sum(d_output, axis=0, keepdims=True) * learning_rate
    
    W1 += X.T.dot(d_hidden) * learning_rate
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate

# 5. Test the trained network
print("Predictions after training:")
print(np.round(predicted_output, 3))
