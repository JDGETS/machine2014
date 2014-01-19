using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace machine2014arcade.Game
{
    public class Stacker
    {
        public enum Direction
        {LEFT, RIGHT}

        private int _left = 0;
        private int _right = 0;
        private int _columnCount;
        private Direction _dir;
        private GameParameters _params;
        private Random _random;

        public int Size {get;set;}

        public int Left 
        { 
            get{return _left;} 
        }

        public int Right 
        { 
            get{return _right;}
        }

        public Direction Dir
        {
            get { return _dir; }
        }


        public Stacker(GameParameters gameParams, int columnCount)
        {
            _random = new Random();
            _params = gameParams;
            _columnCount = columnCount;

            if (_params.StackerSize < 0)
                Size = 0;
            else if (_params.StackerSize > _columnCount)
                Size = _columnCount;
            else
                Size = _params.StackerSize;

            setRandomPosition();
        }

        public void setRandomPosition()
        {
            _left = _random.Next(0, _columnCount - Size);
            _right = _left + Size-1;
        }

        public void setRandomDirection()
        {
            _dir = (Direction)_random.Next(0, 2);
        }

        public void move()
        {
            if (!isDead() && !(_left == 0 && _right == _columnCount - 1))
            {
                if (_dir == Direction.RIGHT && _right == _columnCount - 1)
                    _dir = Direction.LEFT;
                else if (_dir == Direction.LEFT && _left == 0)
                    _dir = Direction.RIGHT;

                if (_dir == Direction.LEFT)
                {
                    _left--;
                    _right--;
                }
                else if (_dir == Direction.RIGHT)
                {
                    _left++;
                    _right++;
                }
            }
        }
        
        public void chop(Direction side)
        {
            if (!isDead())
            {
                if (side == Direction.RIGHT)
                    _right--;
                else if (side == Direction.LEFT)
                    _left++;

                Size = _right - _left + 1;
            }
        }

        public bool isDead()
        {
            return (Size == 0);
        }
    }
}
