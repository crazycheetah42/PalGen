import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
from collections import Counter
import sv_ttk
import platform
import darkdetect
import os
import sys
import traceback

PALETTE_SIZE = 5  # Adjustable number of colors


class PalGenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PalGen - Color Palette Generator")
        self.root.geometry("1000x650")

        self.image_path = ""
        self.image_selected = False
        self.original_image = None
        self.mode = tk.StringVar(value="fast")

        self.setup_icon()
        self.build_ui()
        self.apply_theme()

    def setup_icon(self):
        try:
            if getattr(sys, 'frozen', False):
                icon_path = os.path.join(sys._MEIPASS, "icon.ico")
            else:
                icon_path = "icon.ico"
            if os.path.exists(icon_path):
                self.root.iconbitmap(icon_path)
        except Exception as e:
            print("Icon load error:", e)

    def build_ui(self):
        ttk.Label(self.root, text="PalGen - Color Palette Generator", font=("Segoe UI", 20)).pack(pady=15)

        # Image preview
        self.image_preview = ttk.Label(self.root)
        self.image_preview.pack(pady=10)

        # Import image
        ttk.Button(self.root, text="Import Image", command=self.import_image).pack(pady=5)

        # Mode selection
        mode_frame = ttk.Frame(self.root)
        mode_frame.pack(pady=5)

        ttk.Label(mode_frame, text="Palette Mode: ").pack(side=tk.LEFT, padx=(0, 10))
        ttk.Radiobutton(mode_frame, text="Fast", variable=self.mode, value="fast").pack(side=tk.LEFT)
        ttk.Radiobutton(mode_frame, text="Accurate", variable=self.mode, value="accurate").pack(side=tk.LEFT)

        # Palette display frame
        self.palette_frame = ttk.Frame(self.root)
        self.palette_frame.pack(pady=15)

        # Generate button
        ttk.Button(self.root, text="Generate Palette", command=self.generate_palette).pack(pady=10)

        # Progress label
        self.progress_label = ttk.Label(self.root, text="Import an image to generate a color palette.")
        self.progress_label.pack(pady=5)

    def import_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif"), ("All Files", "*.*")]
        )

        if file_path:
            self.image_path = file_path
            self.image_selected = True
            self.progress_label.config(text="Image imported successfully!")

            try:
                self.original_image = Image.open(self.image_path)
                preview = self.original_image.copy()
                preview.thumbnail((250, 250))
                img_tk = ImageTk.PhotoImage(preview)
                self.image_preview.configure(image=img_tk)
                self.image_preview.image = img_tk
            except Exception:
                print("Error loading image preview:", traceback.format_exc())
                messagebox.showerror("Error", "Failed to load image preview.")

    def copy_to_clipboard(self, text):
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.progress_label.config(text=f"{text} copied to clipboard!")

    def is_near_white(self, pixel, threshold=50):
        # Slightly larger threshold to avoid filtering light purples/blues
        return sum((255 - c) ** 2 for c in pixel) ** 0.5 < threshold

    def generate_palette(self):
        if not self.image_selected or self.original_image is None:
            messagebox.showerror("Error", "Please import an image first.")
            return

        try:
            img = self.original_image.copy().convert("RGB")

            # FAST MODE
            if self.mode.get() == "fast":
                img_small = img.resize((150, 150))
                img_small = img_small.quantize(colors=PALETTE_SIZE * 6).convert("RGB")
                pixels = [p for p in img_small.getdata() if not self.is_near_white(p)]
                color_counts = Counter(pixels)
                dominant_colors = color_counts.most_common(PALETTE_SIZE)

            # ACCURATE MODE (Fast with MiniBatchKMeans)
            else:
                self.progress_label.config(text="Generating Accurate Palette…")
                self.root.update_idletasks()

                import numpy as np
                from sklearn.cluster import MiniBatchKMeans

                img_small = img.resize((200, 200))
                pixels = np.array(img_small.getdata())
                pixels = np.array([p for p in pixels if not self.is_near_white(p)])

                if len(pixels) == 0:
                    messagebox.showerror("Error", "No valid colors found (image too white).")
                    return

                # Random sample ~10k pixels for speed
                if len(pixels) > 10000:
                    idx = np.random.choice(len(pixels), 10000, replace=False)
                    pixels = pixels[idx]

                kmeans = MiniBatchKMeans(
                    n_clusters=PALETTE_SIZE,
                    random_state=0,
                    batch_size=2048,
                    n_init="auto"
                )
                kmeans.fit(pixels)
                centers = kmeans.cluster_centers_.astype(int)

                counts = Counter(kmeans.labels_)
                dominant_colors = [(tuple(centers[i]), counts[i]) for i in counts.keys()]
                dominant_colors.sort(key=lambda x: x[1], reverse=True)

            # Clear old palette
            for widget in self.palette_frame.winfo_children():
                widget.destroy()

            # Display colors
            for idx, (color, _) in enumerate(dominant_colors):
                rgb_tuple = tuple(int(c) for c in color)
                hex_color = '#%02x%02x%02x' % rgb_tuple

                # Color box
                tk.Label(
                    self.palette_frame,
                    bg=hex_color, width=20, height=2, bd=1, relief="solid"
                ).grid(row=0, column=idx, padx=8, pady=5)

                # HEX label (click to copy)
                hex_label = tk.Label(self.palette_frame, text=hex_color, cursor="hand2")
                hex_label.grid(row=1, column=idx)
                hex_label.bind("<Button-1>", lambda e, val=hex_color: self.copy_to_clipboard(val))

                # RGB label (click to copy)
                rgb_str = str(rgb_tuple)
                rgb_label = tk.Label(self.palette_frame, text=rgb_str, fg="gray", cursor="hand2")
                rgb_label.grid(row=2, column=idx)
                rgb_label.bind("<Button-1>", lambda e, val=rgb_str: self.copy_to_clipboard(val))

            self.progress_label.config(text="Palette generated successfully!")

        except Exception:
            print("Error generating palette:", traceback.format_exc())
            messagebox.showerror("Error", "Failed to process image.")

    def apply_theme(self):
        try:
            theme = darkdetect.isDark()
            if theme is True:
                sv_ttk.use_dark_theme()
            elif theme is False:
                sv_ttk.use_light_theme()
        except Exception:
            sv_ttk.use_dark_theme()  # Default


if __name__ == "__main__":
    root = tk.Tk()
    app = PalGenApp(root)
    root.mainloop()
