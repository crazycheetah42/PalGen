namespace PalGen
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.label1 = new System.Windows.Forms.Label();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.panel1 = new System.Windows.Forms.Panel();
            this.panel2 = new System.Windows.Forms.Panel();
            this.panel4 = new System.Windows.Forms.Panel();
            this.panel3 = new System.Windows.Forms.Panel();
            this.panel5 = new System.Windows.Forms.Panel();
            this.panel6 = new System.Windows.Forms.Panel();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Segoe UI", 24F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(390, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(118, 45);
            this.label1.TabIndex = 0;
            this.label1.Text = "PalGen";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // button1
            // 
            this.button1.Cursor = System.Windows.Forms.Cursors.Hand;
            this.button1.Font = new System.Drawing.Font("Segoe UI", 10F);
            this.button1.Location = new System.Drawing.Point(392, 100);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(109, 32);
            this.button1.TabIndex = 1;
            this.button1.Text = "Select image";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Cursor = System.Windows.Forms.Cursors.Hand;
            this.button2.Font = new System.Drawing.Font("Segoe UI", 10F);
            this.button2.Location = new System.Drawing.Point(385, 296);
            this.button2.Name = "button2";
            this.button2.RightToLeft = System.Windows.Forms.RightToLeft.Yes;
            this.button2.Size = new System.Drawing.Size(122, 32);
            this.button2.TabIndex = 2;
            this.button2.Text = "Generate Palette";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(352, 331);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(190, 13);
            this.label2.TabIndex = 3;
            this.label2.Text = "Choose an image to generate a palette";
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.panel2);
            this.panel1.Location = new System.Drawing.Point(137, 391);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(118, 58);
            this.panel1.TabIndex = 4;
            // 
            // panel2
            // 
            this.panel2.Location = new System.Drawing.Point(156, 20);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(200, 100);
            this.panel2.TabIndex = 5;
            // 
            // panel4
            // 
            this.panel4.Location = new System.Drawing.Point(261, 391);
            this.panel4.Name = "panel4";
            this.panel4.Size = new System.Drawing.Size(118, 58);
            this.panel4.TabIndex = 5;
            // 
            // panel3
            // 
            this.panel3.Location = new System.Drawing.Point(385, 391);
            this.panel3.Name = "panel3";
            this.panel3.Size = new System.Drawing.Size(118, 58);
            this.panel3.TabIndex = 6;
            // 
            // panel5
            // 
            this.panel5.Location = new System.Drawing.Point(509, 391);
            this.panel5.Name = "panel5";
            this.panel5.Size = new System.Drawing.Size(118, 58);
            this.panel5.TabIndex = 7;
            // 
            // panel6
            // 
            this.panel6.Location = new System.Drawing.Point(633, 391);
            this.panel6.Name = "panel6";
            this.panel6.Size = new System.Drawing.Size(118, 58);
            this.panel6.TabIndex = 8;
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(311, 141);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(268, 149);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox1.TabIndex = 9;
            this.pictureBox1.TabStop = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(895, 577);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.panel6);
            this.Controls.Add(this.panel5);
            this.Controls.Add(this.panel3);
            this.Controls.Add(this.panel4);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.label1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "PalGen";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.panel1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.Panel panel4;
        private System.Windows.Forms.Panel panel3;
        private System.Windows.Forms.Panel panel5;
        private System.Windows.Forms.Panel panel6;
        private System.Windows.Forms.PictureBox pictureBox1;
    }
}

