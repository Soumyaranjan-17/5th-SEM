import tkinter as tk
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Dataset
data = [
    ['Sunny', 'Hot', 'High', False, 'No'],
    ['Sunny', 'Hot', 'High', True, 'No'],
    ['Overcast', 'Hot', 'High', False, 'Yes'],
    ['Rainy', 'Mild', 'High', False, 'Yes'],
    ['Rainy', 'Cool', 'Normal', False, 'Yes'],
    ['Rainy', 'Cool', 'Normal', True, 'No'],
    ['Overcast', 'Cool', 'Normal', True, 'Yes'],
    ['Sunny', 'Mild', 'High', False, 'No'],
    ['Sunny', 'Cool', 'Normal', False, 'Yes'],
    ['Rainy', 'Mild', 'Normal', False, 'Yes'],
    ['Sunny', 'Mild', 'Normal', True, 'Yes'],
    ['Overcast', 'Mild', 'High', True, 'Yes'],
    ['Overcast', 'Hot', 'Normal', False, 'Yes'],
    ['Rainy', 'Mild', 'High', True, 'No'],
]

# Split features and labels
X = [row[:-1] for row in data]
y = [row[-1] for row in data]

# Encode categorical variables
encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X).toarray()

# Train the decision tree model
model = DecisionTreeClassifier()
model.fit(X_encoded, y)

# Create Tkinter GUI
root = tk.Tk()
root.title("Weather Decision Tree - Should You Play?")

# Dropdown options
outlook_options = ['Sunny', 'Overcast', 'Rainy']
temperature_options = ['Hot', 'Mild', 'Cool']
humidity_options = ['High', 'Normal']
windy_options = ['True', 'False']

# Tkinter variable bindings
outlook_var = tk.StringVar(value=outlook_options[0])
temperature_var = tk.StringVar(value=temperature_options[0])
humidity_var = tk.StringVar(value=humidity_options[0])
windy_var = tk.StringVar(value=windy_options[0])

# Layout
tk.Label(root, text="Outlook:").grid(row=0, column=0)
tk.OptionMenu(root, outlook_var, *outlook_options).grid(row=0, column=1)

tk.Label(root, text="Temperature:").grid(row=1, column=0)
tk.OptionMenu(root, temperature_var, *temperature_options).grid(row=1, column=1)

tk.Label(root, text="Humidity:").grid(row=2, column=0)
tk.OptionMenu(root, humidity_var, *humidity_options).grid(row=2, column=1)

tk.Label(root, text="Windy:").grid(row=3, column=0)
tk.OptionMenu(root, windy_var, *windy_options).grid(row=3, column=1)

result_label = tk.Label(root, text="Prediction: ")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Prediction function
def predict():
    input_data = [[
        outlook_var.get(),
        temperature_var.get(),
        humidity_var.get(),
        windy_var.get() == 'True'
    ]]
    
    input_encoded = encoder.transform(input_data).toarray()
    prediction = model.predict(input_encoded)[0]
    
    result_label.config(
        text=f"Prediction: {'✅ Play' if prediction == 'Yes' else '❌ Don’t Play'}"
    )

# Button
tk.Button(root, text="Predict", command=predict).grid(row=4, column=0, columnspan=2, pady=5)

# Run the GUI
root.mainloop()
