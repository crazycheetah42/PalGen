using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PalGen
{
    public partial class Form1 : Form
    {
        private Image _selectedImage;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            _selectedImage = Program.HandleImageSelection();
            if (_selectedImage != null)
            {
                pictureBox1.Image = _selectedImage;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (_selectedImage != null)
            {
                Program.GeneratePalette(this);
            }
            else
            {
                MessageBox.Show("Please select an image first.", "No Image Selected",
                    MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }
    }
}
