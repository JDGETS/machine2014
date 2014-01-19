using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO.Ports;
using System.Windows.Forms;


namespace machine2014arcade.Game
{
    class Pump
    {
        private static SerialPort _serialPort = null;
        string _onString;
        string _offString;
        private bool _activated = false;
        private static int _instanceNo = 0;

        public bool Activated
        {
            get {return _activated;}
            set 
            {
                if (_serialPort.IsOpen)
                {
                    _activated = value;
                    if (_activated == true)
                        _serialPort.Write(_onString);
                    else
                        _serialPort.Write(_offString);
                }
            }
        }

        public enum ID
        {
            PUMP1,
            PUMP2
        }

        public Pump(ID id)
        {
            _instanceNo++;
            getPort();

            if (id == ID.PUMP1)
            {
                _onString   = "e";
                _offString  = "o";
            }
            else if (id == ID.PUMP2)
            {
                _onString = "f";
                _offString = "p";
            }

            Activated = false;
        }

        public static SerialPort getPort()
        {
            if (_serialPort == null)
                initPort();

            return _serialPort;
        }

        private static void initPort()
        {
            _serialPort = new SerialPort();
            _serialPort.BaudRate = 19200;
            _serialPort.PortName = "COM3";
            _serialPort.Parity = Parity.None;
            _serialPort.StopBits = StopBits.One;
            _serialPort.DataBits = 8;

            try
            {
                _serialPort.Open();
            }
            catch
            {
                MessageBox.Show("Serial port is not accessible");
            }
        }

        public void toggle()
        {
            Activated = !Activated;
        }

        ~Pump()
        {
            if (_serialPort != null)
            {
                if (_serialPort.IsOpen)
                {
                    _serialPort.Close();
                    _serialPort = null;
                }
            } 
        }
    }
}
