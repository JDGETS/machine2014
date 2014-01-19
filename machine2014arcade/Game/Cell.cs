using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Drawing;
using System.Windows.Forms;

namespace machine2014arcade.Game
{


    public class Cell
    {
        private static Bitmap _imgActivated = null;
        private static Bitmap _imgDeactivated = null;

        public Color ActivatedColor = Color.LightGreen;
        public Color NormalColor = Color.White;

        private bool _activated;
        private Panel _panel;

        public Panel Panel
        {
            get { return _panel; }
        }

        public int X { get; set; }
        public int Y { get; set; }

        public Cell(Rectangle rect)
        {
            if (_imgActivated == null)
                _imgActivated = new Bitmap("ressources/activated.png");

            if (_imgDeactivated == null)
                _imgDeactivated = new Bitmap("ressources/deactivated.png");

            _panel = new Panel();
            _panel.Location = rect.Location;
            _panel.Size = rect.Size;
            _panel.BorderStyle = BorderStyle.FixedSingle;
        }

        public bool Activated 
        { 
            get{return _activated;} 
        }

        public void activate()
        {
            _activated = true;
            Panel.BackgroundImage = _imgActivated;
        }

        public void deactivate()
        {
            _activated = false;
            Panel.BackgroundImage = _imgDeactivated;
        }
    }
}
