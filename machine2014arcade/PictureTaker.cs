using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Threading;

namespace machine2014arcade
{
    public partial class PictureTaker : Form
    {
        Camera _cam = null;
        
        private int _count = 3;
        private Image _photo;

        public Image Photo
        {
            get { return _photo; }
        }

        public PictureBox Screen
        {
            get { return picboxPhoto; }
        }

        public int Count 
        {
            set
            {
                _count = value;
                lblCount.Text = "Picture in : " + Convert.ToString(_count);
            }
            get {return _count;}
        }

        public PictureTaker(Camera cam)
        {
            InitializeComponent();
            Count = 3;
            _cam = cam;

            Rectangle screen = System.Windows.Forms.Screen.PrimaryScreen.WorkingArea;
            this.WindowState = FormWindowState.Normal;
            this.StartPosition = FormStartPosition.CenterScreen;
            this.FormBorderStyle = FormBorderStyle.None;
            this.Size = new Size(_cam.Width + 200, _cam.Height + 125);

            picboxPhoto.Size = new Size(_cam.Width, _cam.Height);
            picboxPhoto.Location = new Point(this.Width / 2 - _cam.Width / 2, this.Height - cam.Height -10);

            lblCount.Location = new Point(this.Width / 2 - lblCount.Width / 2, 15);
            Application.Idle += refreshImage;
        }



        private void refreshImage(Object sender, EventArgs e)
        {
            if (Count != 0)
                picboxPhoto.Image = _cam.ActualFrame;
            else
                picboxPhoto.Image = _photo;
        }

        public Image TakePicture(int delay)
        {
            Count = delay;
            tmrCount.Enabled = true;
            this.ShowDialog();
            return _photo;
        }

        private void tmrCount_Tick(object sender, EventArgs e)
        {
            Count--;
            if (Count == 0)
            {
                tmrCount.Enabled = false;
                _photo = (Image)picboxPhoto.Image.Clone();
                Thread.Sleep(2000);
                this.Close();
            }
        }
    }
}
