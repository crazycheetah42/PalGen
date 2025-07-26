# Here is where we import libraries
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
from collections import Counter
import sv_ttk
import platform
import darkdetect

# Variables defined here
image_path = ""
image_selected = False
img_label = None  # So we can update the preview later

# Setup main window
root = tk.Tk()
root.title("Color Palette Generator")
root.geometry("1000x650")
root.configure()

# This makes sure that the icon is present. If it is, great! It sets the icon for the window. Otherwise it throws an error.
# Since it's most likely that there won't be an issue with the installer (unless I mess something up), we'll simply tell the user to redownload the program in case they tried to run the main executable without an icon.
try:
    root.iconbitmap("icon.ico")
except Exception as e:
    print("Icon not found or unsupported:", e)
    messagebox.showwarning("Warning", "The necessary files for this program were not found. Please redownload the program to ensure all required files get included.")

# Heading
heading = ttk.Label(root, text="Color Palette Generator", font=("Segoe UI", 20))
heading.pack(pady=15)

# Image preview placeholder
image_preview = ttk.Label(root)
image_preview.pack(pady=10)

# Import image
def import_image():
    global image_path, image_selected, image_preview

    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    if file_path:
        image_path = file_path
        image_selected = True
        progress_label.config(text="Image imported successfully!")

        # Display thumbnail
        try:
            preview = Image.open(image_path)
            preview.thumbnail((250, 250))
            img_tk = ImageTk.PhotoImage(preview)
            image_preview.configure(image=img_tk)
            image_preview.image = img_tk  # prevent garbage collection
        except Exception as e:
            print("Error loading image preview:", e)

        print(f"Image imported: {image_path}")

# Button to import image
import_button = ttk.Button(root, text="Import Image", command=import_image)
import_button.pack(pady=5)

# Palette frame
palette_frame = tk.Frame(root, )
palette_frame.pack(pady=15)

# Clipboard copy handler
def on_color_click(hex_val):
    root.clipboard_clear()
    root.clipboard_append(hex_val)
    messagebox.showinfo("Copied", f"{hex_val} copied to clipboard!")

# Generate palette function
def generate_palette():
    if not image_selected:
        messagebox.showerror("Error", "Please import an image first.")
        return

    try:
        img = Image.open(image_path).resize((150, 150)).convert("RGB")
        img = img.quantize(colors=32).convert("RGB")
        pixels = list(img.getdata())

        # Filter out near-white pixels
        filtered_pixels = [
            pixel for pixel in pixels
            if not (pixel[0] > 240 and pixel[1] > 240 and pixel[2] > 240)
        ]

        # Count and sort by brightness
        color_counts = Counter(filtered_pixels)
        dominant_colors = color_counts.most_common(5)
        dominant_colors.sort(key=lambda x: sum(x[0]), reverse=True)

        # Clear previous colors
        for widget in palette_frame.winfo_children():
            widget.destroy()

        # Display palette
        for idx, (color, _) in enumerate(dominant_colors):
            hex_color = '#%02x%02x%02x' % color

            # Color box
            color_label = tk.Label(palette_frame, bg=hex_color, width=20, height=2, bd=1, relief="solid")
            color_label.grid(row=0, column=idx, padx=8, pady=5)

            # HEX label (clickable)
            hex_label = tk.Label(palette_frame, text=hex_color, cursor="hand2")
            hex_label.grid(row=1, column=idx)
            hex_label.bind("<Button-1>", lambda e, val=hex_color: on_color_click(val))

            # RGB label
            rgb_label = tk.Label(palette_frame, text=str(color), fg="gray")
            rgb_label.grid(row=2, column=idx)

    except Exception as e:
        print("Error generating palette:", e)
        messagebox.showerror("Error", "Failed to process image.")

# Generate button
palette_button = ttk.Button(root, text="Generate Palette", command=generate_palette)
palette_button.pack(pady=10)

# Progress label
progress_label = ttk.Label(root, text="Import an image to generate a color palette.")
progress_label.pack(pady=5)

if platform.system() == "Windows":
    print("Running on Windows, applying theme based on system theme...")
    if darkdetect.isDark():
        print("Dark mode detected, applying dark theme.")
        sv_ttk.use_dark_theme()
    else:
        print("Light mode detected, applying light theme.")
        sv_ttk.use_light_theme()

# Main loop
if __name__ == "__main__":
    print("Application launched directly.")
    root.mainloop()