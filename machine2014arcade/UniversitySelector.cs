using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace machine2014arcade
{

    public partial class UniversitySelector : Form
    {
        private bool _requestedExit = false;
        public List<University> UniversityList;
        public String Choice 
        {
            get { return _choice;}
        }


        public struct University
        {
            public Image image;
            public String name;

            public University (Image image, string name)
            {
                this.image  = image;
                this.name   = name;
            }
        }
        private String _choice;
        private int _index = 0;

        public UniversitySelector()
        {
            InitializeComponent();

            UniversityList = new List<University>(new []
            {
                new University(Image.FromFile("img/university/abitibi.png"), "Abitibi"),
                new University(Image.FromFile("img/university/concordia.png"), "Concordia"),
                new University(Image.FromFile("img/university/epm.png"), "EPM"),
                new University(Image.FromFile("img/university/itr.png"), "ITR"),
                new University(Image.FromFile("img/university/laval.png"), "Laval"),
                new University(Image.FromFile("img/university/mcgill.png"), "McGill"),
                new University(Image.FromFile("img/university/rimouski.png"), "Rimouski"),
                new University(Image.FromFile("img/university/sherbrooke.png"), "Sherbrooke"),
                new University(Image.FromFile("img/university/uqac.png"), "UQAC"),
                new University(Image.FromFile("img/university/uqamo.png"), "UQAMO"),
                new University(Image.FromFile("img/university/ets.png"), "ÉTS")
            });
            

            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            this.BackColor = Color.Black;
            Rectangle screen = Screen.GetBounds(this);

            pic_etsStacker.Width = pic_etsStacker.Image.Width;
            pic_etsStacker.Height = pic_etsStacker.Image.Height;

            pic_etsStacker.Location = new Point(screen.Size.Width/2 - pic_etsStacker.Width/2, 100);

            pic_chooseUniversity.Width = pic_chooseUniversity.Image.Width;
            pic_chooseUniversity.Height = pic_chooseUniversity.Image.Height;

            pic_chooseUniversity.Location = new Point(screen.Size.Width / 2 - pic_chooseUniversity.Size.Width / 2, 400);
            
            
            this.Focus();
            update();
        }

        private void next()
        {
            _index++;
            _index %= UniversityList.Count;
            
        }

        private void previous()
        {
            if (_index == 0)
                _index = UniversityList.Count - 1;
            else
            {
                _index--;
                _index %= UniversityList.Count;
            }
        }

        private void update()
        {
            Rectangle screen = Screen.GetBounds(this);
            _choice = UniversityList[_index].name;

            pic_universityName.Image = UniversityList[_index].image;
            pic_universityName.Height = pic_universityName.Image.Height;
            pic_universityName.Width = pic_universityName.Image.Width;
            pic_universityName.Location = new Point(screen.Width / 2 - pic_universityName.Width / 2, 600);

        }

        private void UniversitySelector_KeyDown(object sender, KeyEventArgs e)
        {

            switch ((Keys)e.KeyCode)
            {
                case Keys.Enter:
                    this.Close();
                    break;
                    
                case Keys.Up:
                    next();
                    update();
                    break;

                case Keys.Down:
                    previous();
                    update();
                    break;

                case Keys.Escape:
                    _requestedExit = true;
                    this.Close();
                    break;

                default:
                    break;
            }
        }

        public bool requestedExit()
        {
            return _requestedExit;
        }
    }
}
