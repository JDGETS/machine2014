namespace machine2014arcade
{
    partial class MainWindow
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
            this.pnlGameDrawingZone = new System.Windows.Forms.Panel();
            this.pnlTopScore = new System.Windows.Forms.Panel();
            this.lblTopScore = new System.Windows.Forms.Label();
            this.pnlTopScore.SuspendLayout();
            this.SuspendLayout();
            // 
            // pnlGameDrawingZone
            // 
            this.pnlGameDrawingZone.Anchor = System.Windows.Forms.AnchorStyles.None;
            this.pnlGameDrawingZone.BackColor = System.Drawing.Color.Silver;
            this.pnlGameDrawingZone.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pnlGameDrawingZone.Location = new System.Drawing.Point(303, 0);
            this.pnlGameDrawingZone.Margin = new System.Windows.Forms.Padding(0);
            this.pnlGameDrawingZone.Name = "pnlGameDrawingZone";
            this.pnlGameDrawingZone.Size = new System.Drawing.Size(682, 658);
            this.pnlGameDrawingZone.TabIndex = 0;
            // 
            // pnlTopScore
            // 
            this.pnlTopScore.Anchor = System.Windows.Forms.AnchorStyles.None;
            this.pnlTopScore.BackColor = System.Drawing.Color.Black;
            this.pnlTopScore.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pnlTopScore.Controls.Add(this.lblTopScore);
            this.pnlTopScore.Location = new System.Drawing.Point(988, -5);
            this.pnlTopScore.Name = "pnlTopScore";
            this.pnlTopScore.Size = new System.Drawing.Size(313, 658);
            this.pnlTopScore.TabIndex = 1;
            // 
            // lblTopScore
            // 
            this.lblTopScore.AutoSize = true;
            this.lblTopScore.BackColor = System.Drawing.Color.Black;
            this.lblTopScore.Font = new System.Drawing.Font("Old English Text MT", 48F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblTopScore.ForeColor = System.Drawing.SystemColors.ButtonFace;
            this.lblTopScore.Location = new System.Drawing.Point(42, 12);
            this.lblTopScore.Name = "lblTopScore";
            this.lblTopScore.Size = new System.Drawing.Size(311, 77);
            this.lblTopScore.TabIndex = 1;
            this.lblTopScore.Text = "Top Score";
            // 
            // MainWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.Black;
            this.ClientSize = new System.Drawing.Size(1325, 656);
            this.Controls.Add(this.pnlTopScore);
            this.Controls.Add(this.pnlGameDrawingZone);
            this.Name = "MainWindow";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.Window_KeyPress);
            this.pnlTopScore.ResumeLayout(false);
            this.pnlTopScore.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel pnlGameDrawingZone;
        private System.Windows.Forms.Panel pnlTopScore;
        private System.Windows.Forms.Label lblTopScore;
    }
}

