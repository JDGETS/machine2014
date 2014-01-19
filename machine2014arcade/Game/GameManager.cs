using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Drawing;
using System.Threading;
using System.IO.Ports;

namespace machine2014arcade.Game
{
    class GameManager
    {
        private const int WIDTH = 0;   // 2d array dimension index
        private const int HEIGHT = 1;  // 2d array dimension index

        private const int SPEEDUP_INTERVAL = 5;
        private const int DRINKING_SIP_INTERVAL = 200;
        private const int DRINKUP_INTERVAL = 10000;
        private const int INITIAL_DRINK_INTERVAL = 5000;

       // private int nextDrinkInterval = INITIAL_DRINK_INTERVAL;

        private MainWindow _win;
        private GameParameters _params;
        private Stacker _stacker;
        private int _blockSize = 0;
        private bool _dead;
        private const int _columnsQty = 14;

        private System.Windows.Forms.Timer _blinkerTimer;
       

        private Cell[,] _cellMatrix;
        private Label[] _lineNoLabel;
        private System.Windows.Forms.Timer _tmrMoveBlocks;
        private Pump _pump1, _pump2;

        private ScreenMessage _speedUpMsg;
        private ScreenMessage _drinkMsg;

        private ScreenMessageQueue _messageQueue;

        private System.Windows.Forms.Timer _tmrPump;    // Turn of the pump

        private int _activeLine = 0;    // Matrix number, always < matrixHeight
        private int _lineNumber=1;      // Line number that user see

        public bool Dead 
        {
            get { return _dead; }
        }

        public int ActiveLineNumer 
        {
            get { return _lineNumber; }
        }

        public GameManager(MainWindow win, Panel drawingZone, GameParameters parameters)
        {
            _params         = parameters;
            _tmrMoveBlocks  = new System.Windows.Forms.Timer();
      //      _tmrDrinkUp     = new System.Windows.Forms.Timer();
      //      _tmrDrink       = new System.Windows.Forms.Timer();
            _blinkerTimer = new System.Windows.Forms.Timer();
            _tmrPump        = new System.Windows.Forms.Timer();
            _tmrPump.Tick   += new EventHandler(stopBlinker);

            _stacker = new Stacker(_params, _columnsQty);
            _win            = win;

            _pump1          = new Pump(Pump.ID.PUMP1);
            _pump2          = new Pump(Pump.ID.PUMP2);

            _messageQueue = new ScreenMessageQueue();

            _speedUpMsg = new ScreenMessage(_win, "Speed Up !", _messageQueue);
            _drinkMsg   = new ScreenMessage(_win, "You Drink !", _messageQueue);

           

            _speedUpMsg.TextColor = Color.Orange;
            _speedUpMsg.TextColor = Color.MediumPurple;

            initDrawingZone(drawingZone);

            _tmrMoveBlocks.Tick += new EventHandler(moveBlocks);
            _tmrPump.Tick       += new EventHandler(turnOffPump);

        }

        public void actionButton()
        {
            int chopped;
            _tmrMoveBlocks.Stop();
            chopped = stack();
            drawActiveLine();

            if (!_stacker.isDead())
            {
                _lineNumber++;
                if (_lineNumber % SPEEDUP_INTERVAL == 0)
                {
                    _messageQueue.Push(_speedUpMsg);

                    _tmrMoveBlocks.Interval -= 20;
                    if (_tmrMoveBlocks.Interval <= 20)
                        _tmrMoveBlocks.Interval = 20;
                }

                if (_activeLine == _cellMatrix.GetLength(HEIGHT) - 1)
                {
                    scrollDown();
                }
                else
                    _activeLine++;

                _stacker.setRandomPosition();
                _stacker.setRandomDirection();
                drawActiveLine();
                _tmrMoveBlocks.Start();
            }

            if (chopped > 0)
                drink(1000 * chopped);

            _dead = _stacker.isDead();
          
        }

        private int stack()
        {
            int chopped = 0;
            if (_activeLine > 0)
            {
                bool finished = false;
                do
                {
                    if (!_cellMatrix[_stacker.Left, _activeLine - 1].Activated)
                    {
                        _stacker.chop(Stacker.Direction.LEFT);
                        chopped++; 
                    }

                    else if (!_cellMatrix[_stacker.Right, _activeLine - 1].Activated)
                    {
                        _stacker.chop(Stacker.Direction.RIGHT);
                        chopped++;
                    }
                    else
                        finished = true;
                } while (!finished && !_stacker.isDead());
            }
            return chopped;
        }

        private void moveBlocks(object sender, EventArgs e)
        {
            if (!_stacker.isDead())
            {
                _stacker.move();
                drawActiveLine();
            }
        }

        public void scrollDown()
        {
            int scrollAmount = 2*_cellMatrix.GetLength(HEIGHT) / 3;
            _activeLine = _cellMatrix.GetLength(HEIGHT) / 3+1;

            for (int i = 0; i < _cellMatrix.GetLength(WIDTH); i++)
            {
                for (int j = 0; j < _cellMatrix.GetLength(HEIGHT); j++)
                {
                    if (j + scrollAmount < _cellMatrix.GetLength(HEIGHT) - 1)   // Copy a line
                    {
                        if (_cellMatrix[i, j + scrollAmount].Activated)
                            _cellMatrix[i, j].activate();
                        else
                            _cellMatrix[i, j].deactivate();
                    }
                    else if(j+scrollAmount == _cellMatrix.GetLength(HEIGHT)-1)  // Last line (active one)
                    {
                        if (i >= _stacker.Left && i <= _stacker.Right)
                            _cellMatrix[i, j].activate();
                        else
                            _cellMatrix[i, j].deactivate();
                    }
                    else   // New space
                        _cellMatrix[i, j].deactivate();
                }
            }

            for (int i = 0; i < _cellMatrix.GetLength(HEIGHT); i++)
            {
                int lineNo = (Convert.ToInt32(_lineNoLabel[i].Text) + scrollAmount);
                _lineNoLabel[i].BackColor = (lineNo % 5 == 0) ? Color.MediumPurple : Color.LightGray;
                _lineNoLabel[i].Text = Convert.ToString(Convert.ToInt32(_lineNoLabel[i].Text) + scrollAmount);
            
            }
                

        }

        private void drawActiveLine()
        {
            for (int i = 0; i < _cellMatrix.GetLength(WIDTH); i++)
            {
                if (i >= _stacker.Left && i <= _stacker.Right)
                    _cellMatrix[i, _activeLine].activate();
                else
                    _cellMatrix[i, _activeLine].deactivate();
            }
        }

        public void Start()
        {
            _dead = false;
            _lineNumber = 1;
            for (int i = 0; i < _cellMatrix.GetLength(WIDTH); i++)
            {
                for (int j = 0; j < _cellMatrix.GetLength(HEIGHT); j++)
                {
                    _cellMatrix[i, j].deactivate();
                }
            }

            for (int i = 0; i < _cellMatrix.GetLength(HEIGHT); i++)
            {
                _lineNoLabel[i].Text = Convert.ToString(i+1);
                _lineNoLabel[i].BackColor = ((i + 1) % 5 == 0) ? Color.MediumPurple : Color.LightGray;

            }

            _activeLine = 0;
            _stacker.Size = _params.StackerSize;
            _stacker.setRandomPosition();
            drawActiveLine();

            _tmrMoveBlocks.Interval = 250;
            _tmrPump.Interval = DRINKING_SIP_INTERVAL;

            _tmrMoveBlocks.Start();
        }

        private void initDrawingZone(Panel drawingZone)
        {
            _blockSize = 60; // 960/10  //(drawingZone.Width / (_params.ColumnsQty+1));
            
            //drawingZone.Width -= (drawingZone.Width % _blockSize);  // Resize the drawing zone to be a multiple of _blockSize
            drawingZone.Height -= 25; // Resize the drawing zone to be a multiple of _blockSize
            //int matrixHeight = drawingZone.Height/_blockSize;

            
            _cellMatrix = new Cell[_columnsQty, 17];
            _lineNoLabel = new Label[_cellMatrix.GetLength(HEIGHT)];

            
            for (int i = 0; i < _cellMatrix.GetLength(WIDTH); i++)
            {
                for (int j = 0; j < _cellMatrix.GetLength(HEIGHT); j++)
                {
                    _cellMatrix[i, j] = new Cell(new Rectangle(
                        (i+1) * _blockSize,
                        drawingZone.Size.Height - _blockSize - j * _blockSize,
                        _blockSize,
                        _blockSize));

                    drawingZone.Controls.Add(_cellMatrix[i, j].Panel);

                }
            }

            for (int i = 0; i < _cellMatrix.GetLength(HEIGHT); i++)
            {

                _lineNoLabel[i] = new Label();
                _lineNoLabel[i].Location = new Point(0, drawingZone.Size.Height - _blockSize - i * _blockSize);
                _lineNoLabel[i].Size = new Size(_blockSize, _blockSize);
                
                
                _lineNoLabel[i].BackColor = ((i+1)%5==0) ? Color.MediumPurple : Color.LightGray;
                
                
                _lineNoLabel[i].ForeColor = Color.Black;
                _lineNoLabel[i].TextAlign = ContentAlignment.MiddleCenter;
                _lineNoLabel[i].Text = Convert.ToString(i + 1);
                _lineNoLabel[i].Font = new Font("Times New Roman", 20);
                _lineNoLabel[i].BorderStyle = BorderStyle.FixedSingle;

                drawingZone.Controls.Add(_lineNoLabel[i]);
            }

            drawActiveLine();
        }
  
        private void drink(int time)
        {
            _messageQueue.Push(_drinkMsg);
            _pump1.Activated = true;
            _tmrPump.Interval = time;
            _tmrPump.Start();
            _tmrPump.Enabled = true;
        }

        public void activateBlinker(int time)
        {
            _blinkerTimer.Stop();
            _blinkerTimer.Interval =time;
            _blinkerTimer.Start();

            _pump2.Activated = true;
        }

        private void stopBlinker(Object myObject, EventArgs myEventArgs)
        {
            _blinkerTimer.Stop();
            _pump2.Activated = false;
        }
       
        private void turnOffPump(object sender, EventArgs e)
        {
            _pump1.Activated = false;
            _tmrPump.Stop();
        }

    };
};
