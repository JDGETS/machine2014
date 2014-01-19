using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using Emgu.CV;
using Emgu.Util;
using Emgu.CV.CvEnum;
using Emgu.CV.Structure;
using System.Drawing;
using System.Threading;

namespace machine2014arcade
{
    public class Camera
    {
        Capture _capture = null;
        Image _actualFrame = null;
        Thread _camThread = null;

        public int Width = 768;
        public int Height = 480;

        public Image ActualFrame 
        {
            get { return _actualFrame; }
        }

        public Camera(int w, int h)
        {
            Width = w;
            Height = h;

            _camThread = new Thread(new ThreadStart(refreshCam));
            _camThread.Start();

        }


        private void refreshCam()
        {
            while (true)
            {
                if (_capture == null)
                    initCamera();

                if (_capture != null)
                {
                    try
                    {
                        _actualFrame = _capture.QueryFrame().ToBitmap();
                    }
                    catch
                    {
                        _capture.Dispose();
                        _capture = null;
                    }
                }
            }
        }

        private void initCamera()
        {
            try
            {
                _capture = new Capture(0);
                _capture.SetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_WIDTH, Width);
                _capture.SetCaptureProperty(CAP_PROP.CV_CAP_PROP_FRAME_HEIGHT, Height);
            }
            catch
            {
                if (_capture != null)
                    _capture.Dispose();
                _capture = null;
                
            }
        }

        public void Close()
        {
            if (_camThread != null)
            {
                if (_camThread.IsAlive)
                {
                    _camThread.Abort();
                    _camThread.Join();
                }
            } 
        }

         ~Camera()
        {
            if (_capture != null)
                _capture.Dispose();
        }
    }
}
