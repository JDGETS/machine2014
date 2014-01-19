namespace machine2014arcade
{
    partial class UniversitySelector
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(UniversitySelector));
            this.backgroundWorker1 = new System.ComponentModel.BackgroundWorker();
            this.pic_etsStacker = new System.Windows.Forms.PictureBox();
            this.pic_chooseUniversity = new System.Windows.Forms.PictureBox();
            this.pic_universityName = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.pic_etsStacker)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pic_chooseUniversity)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pic_universityName)).BeginInit();
            this.SuspendLayout();
            // 
            // pic_etsStacker
            // 
            this.pic_etsStacker.Image = ((System.Drawing.Image)(resources.GetObject("pic_etsStacker.Image")));
            this.pic_etsStacker.Location = new System.Drawing.Point(77, 29);
            this.pic_etsStacker.Name = "pic_etsStacker";
            this.pic_etsStacker.Size = new System.Drawing.Size(1300, 219);
            this.pic_etsStacker.TabIndex = 2;
            this.pic_etsStacker.TabStop = false;
            // 
            // pic_chooseUniversity
            // 
            this.pic_chooseUniversity.Image = ((System.Drawing.Image)(resources.GetObject("pic_chooseUniversity.Image")));
            this.pic_chooseUniversity.Location = new System.Drawing.Point(169, 297);
            this.pic_chooseUniversity.Name = "pic_chooseUniversity";
            this.pic_chooseUniversity.Size = new System.Drawing.Size(734, 119);
            this.pic_chooseUniversity.TabIndex = 3;
            this.pic_chooseUniversity.TabStop = false;
            // 
            // pic_universityName
            // 
            this.pic_universityName.Location = new System.Drawing.Point(213, 444);
            this.pic_universityName.Name = "pic_universityName";
            this.pic_universityName.Size = new System.Drawing.Size(483, 50);
            this.pic_universityName.TabIndex = 4;
            this.pic_universityName.TabStop = false;
            // 
            // UniversitySelector
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1061, 545);
            this.Controls.Add(this.pic_universityName);
            this.Controls.Add(this.pic_chooseUniversity);
            this.Controls.Add(this.pic_etsStacker);
            this.Name = "UniversitySelector";
            this.Text = "UniversitySelector";
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.UniversitySelector_KeyDown);
            ((System.ComponentModel.ISupportInitialize)(this.pic_etsStacker)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pic_chooseUniversity)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pic_universityName)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.ComponentModel.BackgroundWorker backgroundWorker1;
        private System.Windows.Forms.PictureBox pic_etsStacker;
        private System.Windows.Forms.PictureBox pic_chooseUniversity;
        private System.Windows.Forms.PictureBox pic_universityName;
    }
}