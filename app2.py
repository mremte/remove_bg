import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from rembg import remove
import os


# Function to upload image
def upload_image():
    global img_path
    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if img_path:
        load_image(img_path, original_image_label)


# Function to load and display image
def load_image(image_path, label):
    image = Image.open(image_path)
    image.thumbnail((300, 300))  # Resize to fit in the label
    img = ImageTk.PhotoImage(image)
    label.config(image=img)
    label.image = img  # Keep a reference to avoid garbage collection


# Function to remove background and show the result
def process_image():
    if img_path:
        image = Image.open(img_path)
        result = remove(image)

        # Save the result if you want
        save_path = os.path.join(os.path.dirname(img_path), "processed_image.png")
        result.save(save_path)

        load_image(save_path, processed_image_label)


# Create main window
root = tk.Tk()
root.title("Remove Background")

# Upload button
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

# Original image display
original_image_label = tk.Label(root)
original_image_label.pack(pady=10)

# Process button
process_button = tk.Button(root, text="Remove Background", command=process_image)
process_button.pack(pady=10)

# Processed image display
processed_image_label = tk.Label(root)
processed_image_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
