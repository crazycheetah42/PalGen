using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Windows.Forms;

namespace PalGen
{
    internal static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
        }

        // Add a static field to store the selected file path
        private static string selectedFilePath;

        // This method will be called when button1 is pressed
        // Update HandleImageSelection to set the selectedFilePath field
        // Add a parameter for the PictureBox to update
        public static Image HandleImageSelection()
        {
            using (OpenFileDialog openFileDialog = new OpenFileDialog())
            {
                openFileDialog.Title = "Select an Image";
                openFileDialog.Filter = "Image Files|*.jpg;*.jpeg;*.png;*.bmp;*.gif";
                openFileDialog.RestoreDirectory = true;

                if (openFileDialog.ShowDialog() == DialogResult.OK)
                {
                    selectedFilePath = openFileDialog.FileName;
                    // Use selectedFilePath to load the image
                    return Image.FromFile(selectedFilePath);
                }
            }
            return null;
        }
        public static void GeneratePalette(Form form)
        {
            if (form == null)
            {
                throw new ArgumentNullException(nameof(form));
            }

            if (string.IsNullOrEmpty(selectedFilePath))
            {
                throw new InvalidOperationException("No image has been selected.");
            }

            try
            {
                using (Bitmap image = new Bitmap(selectedFilePath))
                {
                    // Find 5 dominant colors
                    var dominantColors = ImageColorAnalyzer.FindDominantColors(image, 5);

                    // Get reference to Form1
                    var mainForm = form as Form1;
                    if (mainForm == null)
                    {
                        throw new ArgumentException("Form must be of type Form1");
                    }

                    // Get the panels in the desired order
                    var panels = new[]
                    {
                        mainForm.Controls.Find("panel1", true).FirstOrDefault(),
                        mainForm.Controls.Find("panel4", true).FirstOrDefault(),
                        mainForm.Controls.Find("panel3", true).FirstOrDefault(),
                        mainForm.Controls.Find("panel5", true).FirstOrDefault(),
                        mainForm.Controls.Find("panel6", true).FirstOrDefault()
                    };

                    // Update panel colors
                    for (int i = 0; i < Math.Min(dominantColors.Count, panels.Length); i++)
                    {
                        if (panels[i] != null)
                        {
                            panels[i].BackColor = dominantColors[i];
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Error generating palette: {ex.Message}", "Error", 
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
        public static class ImageColorAnalyzer
        {
            private const int SamplingInterval = 5; // Sample every Nth pixel
            private const double DarkThreshold = 0.15; // Colors darker than this are considered too dark
            private const double LightThreshold = 0.85; // Colors lighter than this are considered too light

            /// <summary>
            /// Finds the dominant colors in a given image.
            /// </summary>
            /// <param name="image">The image to analyze.</param>
            /// <param name="colorCount">The number of dominant colors to return.</param>
            /// <returns>A list of dominant colors.</returns>
            public static List<Color> FindDominantColors(Bitmap image, int colorCount = 3)
            {
                var colorDict = new Dictionary<ColorKey, int>();
                
                // Process pixels at intervals for better performance
                for (int y = 0; y < image.Height; y += SamplingInterval)
                {
                    for (int x = 0; x < image.Width; x += SamplingInterval)
                    {
                        Color pixel = image.GetPixel(x, y);
                        
                        // Skip very dark or very light colors
                        double brightness = (pixel.R + pixel.G + pixel.B) / (3.0 * 255);
                        if (brightness < DarkThreshold || brightness > LightThreshold)
                            continue;

                        // Quantize the color
                        var quantizedColor = new ColorKey(
                            QuantizeColorComponent(pixel.R),
                            QuantizeColorComponent(pixel.G),
                            QuantizeColorComponent(pixel.B)
                        );

                        if (colorDict.ContainsKey(quantizedColor))
                            colorDict[quantizedColor]++;
                        else
                            colorDict[quantizedColor] = 1;
                    }
                }

                // Get the most common colors
                return colorDict
                    .OrderByDescending(kvp => kvp.Value)
                    .Take(colorCount)
                    .Select(kvp => Color.FromArgb(
                        DeQuantizeColorComponent(kvp.Key.R),
                        DeQuantizeColorComponent(kvp.Key.G),
                        DeQuantizeColorComponent(kvp.Key.B)))
                    .ToList();
            }

            private const int ColorLevels = 32; // Number of levels per color channel

            private static int QuantizeColorComponent(int value)
            {
                return (value * ColorLevels) / 256;
            }

            private static int DeQuantizeColorComponent(int value)
            {
                return (value * 256) / ColorLevels;
            }

            private struct ColorKey
            {
                public int R, G, B;

                public ColorKey(int r, int g, int b)
                {
                    R = r;
                    G = g;
                    B = b;
                }

                public override bool Equals(object obj)
                {
                    if (!(obj is ColorKey)) return false;
                    var other = (ColorKey)obj;
                    return R == other.R && G == other.G && B == other.B;
                }

                public override int GetHashCode()
                {
                    return (R << 16) | (G << 8) | B;
                }
            }
        }
    }

}
