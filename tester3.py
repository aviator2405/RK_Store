import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Create the main application window
root = tk.Tk()
root.title("Image Viewer")

# Create a function to load and display the image
def load_image():
    url = entry.get()
    try:
        response = requests.get(url)
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img = img.resize((300, 300))  # Resize the image as needed
        img = ImageTk.PhotoImage(img)

        label.config(image=img)
        label.image = img  # Keep a reference to prevent garbage collection

    except Exception as e:
        label.config(text="Error: Unable to load image")
        print(e)

# Create an entry widget for entering the image URL
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a button to load the image
load_button = tk.Button(root, text="Load Image", command=load_image)
load_button.pack()

# Create a label to display the image
label = tk.Label(root)
label.pack()

root.mainloop()
