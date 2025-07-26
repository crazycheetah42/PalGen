# Import required libraries/modules
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from PIL import Image
from collections import Counter

# First, we must set up the variables that will be used in the app.
# Below is the variable which stores the image path. It's empty because the user hasn't selected an image yet.
image_path = ""
# Below is a boolean variable to check if an image has been selected or not.
# This will be used later to ensure that the user has selected an image before generating a palette
image_selected = False

# Here we set up the main application window to be able to add elements later
print("Setting up the main application window...")
root = tk.Tk()
root.title("Color Palette Generator")
root.geometry("900x600")
root.iconbitmap("icon.ico")  # Set the icon for the application window

# This is a heading label for the application, which will be displayed at the top
heading = ttk.Label(root, text="Color Palette Generator", font=("Segoe UI", 20))
heading.pack(pady=15)

# This function will be used to import an image from the user's file system.
# It opens a file dialog to let the user choose an image file, and then stores the output path in the global variable image_path.
def import_image():
    global image_path
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    if file_path:
        image_path = file_path
        global image_selected
        image_selected = True
        progress_label.config(text="Image imported successfully!")
        print(f"Image imported: {image_path}")

# This is a button that will be used to import the user's image of choice.
import_button = ttk.Button(root, text="Import Image", command=import_image)
import_button.pack(pady=10)

# This is the function to extract dominant colors from the image
def generate_palette():
    # Failsafe to ensure that an image was selected before generating.
    if not image_selected:
        print("No image selected.")
        messagebox.showerror("Error", "Please import an image first.")

    img = Image.open(image_path)
    img = img.resize((150, 150))
    img = img.convert('RGB')
    # Quantize to group similar colors
    img = img.quantize(colors=32).convert('RGB')
    pixels = list(img.getdata())

    # Filter out near-white pixels
    filtered_pixels = [
        pixel for pixel in pixels
        if not (pixel[0] > 240 and pixel[1] > 240 and pixel[2] > 240)
    ]

    color_counts = Counter(filtered_pixels)
    dominant_colors = color_counts.most_common(5)

    # Remove previous palette if any
    for widget in palette_frame.winfo_children():
        widget.destroy()

    # Display the colors
    for idx, (color, count) in enumerate(dominant_colors):
        hex_color = '#%02x%02x%02x' % color
        color_label = tk.Label(palette_frame, bg=hex_color, width=20, height=2)
        color_label.grid(row=0, column=idx, padx=5, pady=5)
        hex_label = tk.Label(palette_frame, text=hex_color)
        hex_label.grid(row=1, column=idx)

# This is a frame to hold the palette
palette_frame = tk.Frame(root)
palette_frame.pack(pady=10)

# This is a label to show the user information about the program's progress
progress_label = ttk.Label(root, text="Import an image to generate a color palette.")
progress_label.pack(pady=5)

# This is the button to generate the palette
palette_button = ttk.Button(root, text="Generate Palette", command=generate_palette)
palette_button.pack(pady=10)

# This makes sure that the program is being run directly and not imported as a module
if __name__ == "__main__":
    print("Application launched directly.")
    # This starts the loop of the application which makes it run
    print("Starting root.mainloop()...")
    root.mainloop()