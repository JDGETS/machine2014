namespace machine2014arcade
{
    partial class PictureTaker
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
            this.components = new System.ComponentModel.Container();
            this.picboxPhoto = new System.Windows.Forms.PictureBox();
            this.lblCount = new System.Windows.Forms.Label();
            this.tmrCount = new System.Windows.Forms.Timer(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.picboxPhoto)).BeginInit();
            this.SuspendLayout();
            // 
            // picboxPhoto
            // 
            this.picboxPhoto.BackColor = System.Drawing.Color.Black;
            this.picboxPhoto.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picboxPhoto.Location = new System.Drawing.Point(137, 95);
            this.picboxPhoto.Name = "picboxPhoto";
            this.picboxPhoto.Size = new System.Drawing.Size(497, 378);
            this.picboxPhoto.TabIndex = 3;
            this.picboxPhoto.TabStop = false;
            // 
            // lblCount
            // 
            this.lblCount.AutoSize = true;
            this.lblCount.Font = new System.Drawing.Font("Pristina", 48F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblCount.ForeColor = System.Drawing.Color.White;
            this.lblCount.Location = new System.Drawing.Point(241, 7);
            this.lblCount.Name = "lblCount";
            this.lblCount.Size = new System.Drawing.Size(288, 85);
            this.lblCount.TabIndex = 4;
            this.lblCount.Text = "Picture in X";
            // 
            // tmrCount
            // 
            this.tmrCount.Interval = 1000;
            this.tmrCount.Tick += new System.EventHandler(this.tmrCount_Tick);
            // 
            // PictureTaker
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.Black;
            this.ClientSize = new System.Drawing.Size(720, 485);
            this.Controls.Add(this.lblCount);
            this.Controls.Add(this.picboxPhoto);
            this.Name = "PictureTaker";
            this.Text = "PictureTaker";
            ((System.ComponentModel.ISupportInitialize)(this.picboxPhoto)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox picboxPhoto;
        private System.Windows.Forms.Label lblCount;
        private System.Windows.Forms.Timer tmrCount;
    }
}