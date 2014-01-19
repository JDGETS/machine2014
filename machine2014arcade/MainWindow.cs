using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using machine2014arcade.Game;
using System.IO;

namespace machine2014arcade
{
    public partial class MainWindow : Form
    {

        public const string scoreCardExtension = "score";
        public const string scoreCardFolder = "score/";
        public const string imgFolder = "img/";
        public const int thumbnailHeight = 140;  


        Game.GameManager game = null;
        Game.GameParameters gameParams = null;
        UniversitySelector universitySelector = null;
        PictureTaker pictureTaker = null;

        List<Panel> topScoreDisplay = null;
        Camera _cam = null;

        bool _exitRequested = false;


        public MainWindow()
        {
            InitializeComponent();
            
            gameParams = new Game.GameParameters();
            gameParams.StackerSize = 5;

            System.IO.Directory.CreateDirectory(scoreCardFolder);
            System.IO.Directory.CreateDirectory(imgFolder);
            System.IO.Directory.CreateDirectory(imgFolder+"full/");
            
            initGraphic();

            pictureTaker = new PictureTaker(_cam);
            game = new Game.GameManager(this, pnlGameDrawingZone, gameParams);
            universitySelector= new UniversitySelector();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
            do
            {
                showTopScore( getTopScore(5));

                universitySelector.ShowDialog();
                if (universitySelector.requestedExit())
                    break;
                game.Start();
                while (!game.Dead)
                {
                    Application.DoEvents();
                    if (requestExit())
                        break;
                }
                game.activateBlinker(3);    
                if (!requestExit())
                {
                    ScoreCard score = new ScoreCard();
                    score.Score = (game.ActiveLineNumer - 1);
                    Image photo = pictureTaker.TakePicture(3);
                    Image thumbnail = makeThumbnail(photo);
                    score.Photo = imgFolder + DateTime.Now.ToString("yyyyMMddHHmmssfff") + ".jpg";
                    photo.Save(imgFolder+"full/" + DateTime.Now.ToString("yyyyMMddHHmmssfff") + ".jpg");
                    thumbnail.Save(score.Photo);
                    score.University = universitySelector.Choice;

                    score.save(scoreCardFolder + DateTime.Now.ToString("yyyyMMddHHmmssfff") + "." + scoreCardExtension);
                    
                }
            } while (!requestExit());

            universitySelector.Close();
            _cam.Close();
            this.Close();
        }

        public void Window_KeyPress(object sender, KeyPressEventArgs e)
        {
            if ((Keys)e.KeyChar == Keys.Enter)
            {
                game.actionButton();
            }
            else if ((Keys)e.KeyChar == Keys.Escape)
            {
                _exitRequested = true;
                universitySelector.Close();
                this.Close();
            }
        }

        private void initGraphic()
        {
            topScoreDisplay = new List<Panel>();

            // Let's put the screen to full size
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;

            Rectangle screen = Screen.GetBounds(this);      
            pnlGameDrawingZone.Size = new Size(900, 1080);
            pnlGameDrawingZone.Location = new Point(100, -15);

            pnlTopScore.Size = new Size(600, screen.Height);
            pnlTopScore.Location = new Point(1000, -15);

            lblTopScore.Location = new Point(90, 15);

            _cam = new Camera(768,480);
            
        }

        private bool requestExit()
        {
            return _exitRequested;
        }

        private Image makeThumbnail(Image image)
        {
            var ratio = (double)thumbnailHeight / image.Height;

            var newWidth = (int)(image.Width * ratio);

            var newImage = new Bitmap(newWidth, thumbnailHeight);
            Graphics.FromImage(newImage).DrawImage(image, 0, 0, newWidth, thumbnailHeight);
            return newImage;
        }


        private List<ScoreCard> getTopScore(int qty)
        {
            List<ScoreCard> topScore = new List<ScoreCard>();

            string[] scoreFiles = Directory.GetFiles(scoreCardFolder, "*." + scoreCardExtension);

            foreach (string filename in scoreFiles)
                topScore.Add(ScoreCard.load(filename));
            
            topScore.Sort(
                delegate(ScoreCard a, ScoreCard b)
                {
                    return b.Score.CompareTo(a.Score);  // Descending sort
                }
            );

            if (qty < topScore.Count)
                topScore.RemoveRange(qty, topScore.Count - qty);

            return topScore;
        }

        void showTopScore(List<ScoreCard> scoreCardList)
        {

            pnlTopScore.Controls.Clear();
            pnlTopScore.Controls.Add(lblTopScore);
                
            for (int i=0; i<scoreCardList.Count; i++)
            {

                Panel scorePanel = new Panel();
                scorePanel.Size = new Size(pnlTopScore.Width - 30, 150);
                scorePanel.Location = new Point (15, 175 * i + 120);
                scorePanel.BackColor = Color.LightBlue;
                scorePanel.BorderStyle = BorderStyle.Fixed3D;

                PictureBox picTempPic = new PictureBox();
                picTempPic.Image = Image.FromFile(scoreCardList[i].Photo);
                picTempPic.Location = new Point(5, 5);
                picTempPic.Size = new Size(picTempPic.Image.Width, picTempPic.Image.Height);

                Label lbltempUniveristy = new Label();
                lbltempUniveristy.Text = Convert.ToString(scoreCardList[i].University);
                lbltempUniveristy.Location = new Point(250, 10);
                lbltempUniveristy.Font = new Font("Imprint MT Shadow", 30);
                lbltempUniveristy.AutoSize = true;

                Label lbltempScore = new Label();
                lbltempScore.Text =Convert.ToString(scoreCardList[i].Score) + " pts";
                lbltempScore.Location = new Point(250, 75);
                lbltempScore.Font = new Font("Imprint MT Shadow", 36);
                lbltempScore.AutoSize = true;

                scorePanel.Controls.Add(picTempPic);
                scorePanel.Controls.Add(lbltempScore);
                scorePanel.Controls.Add(lbltempUniveristy);

                pnlTopScore.Controls.Add(scorePanel);
            }
        }
    }
}
