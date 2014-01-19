using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing;

namespace machine2014arcade.Game
{
    class ScreenMessage : Form
    {
        private Label lblText;
        private Timer tmrMvt;
        private System.ComponentModel.IContainer components;
        private MainWindow _win;
        private ScreenMessageQueue _queueRef;

        public Color TextColor
        {
            get {return lblText.ForeColor;}
            set { lblText.ForeColor = value; }
        }
    
        public ScreenMessage(MainWindow win, String text, ScreenMessageQueue queue)
        {
            InitializeComponent();

            lblText.Text = text;
            _win = win;
            _queueRef = queue;

            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            this.Visible = false;
            this.Show();

        }

        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.lblText = new System.Windows.Forms.Label();
            this.tmrMvt = new System.Windows.Forms.Timer(this.components);
            this.SuspendLayout();
            // 
            // lblText
            // 
            this.lblText.AutoSize = true;
            this.lblText.Font = new System.Drawing.Font("Ravie", 72F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblText.ForeColor = System.Drawing.Color.Orange;
            this.lblText.Location = new System.Drawing.Point(46, 56);
            this.lblText.Name = "lblText";
            this.lblText.Size = new System.Drawing.Size(869, 129);
            this.lblText.TabIndex = 0;
            this.lblText.Text = "Dummy Text";
            // 
            // tmrMvt
            // 
            this.tmrMvt.Interval = 40;
            this.tmrMvt.Tick += new System.EventHandler(this.tmrMvt_Tick);
            // 
            // ScreenMessage
            // 
            this.BackColor = System.Drawing.Color.White;
            this.ClientSize = new System.Drawing.Size(940, 250);
            this.Controls.Add(this.lblText);
            this.Name = "ScreenMessage";
            this.TransparencyKey = System.Drawing.Color.White;
            this.WindowState = System.Windows.Forms.FormWindowState.Maximized;
            this.Load += new System.EventHandler(this.ScreenMessage_Load);
            this.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.ScreenMessage_KeyPress);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        public void Go()
        {
            lblText.Location = new Point(this.Width / 2 - lblText.Width / 2, this.Height - lblText.Height);
            this.BringToFront();
            this.Visible = true;
            tmrMvt.Enabled = true;
            
        }

        private void Done()
        {
            this.Visible = false;
            _queueRef.Pop();
        }

        private void ScreenMessage_Load(object sender, EventArgs e)
        {
            
            
        }

        private void tmrMvt_Tick(object sender, EventArgs e)
        {
            
            lblText.Location = new Point(lblText.Location.X, lblText.Location.Y - 25);
            if (lblText.Location.Y < 300)
               this.Done();
        }

        private void ScreenMessage_KeyPress(object sender, KeyPressEventArgs e)
        {
            _win.Window_KeyPress(sender,e);
        }
    }
}
