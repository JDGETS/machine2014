using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace machine2014arcade.Game
{
    class ScreenMessageQueue
    {
        private Queue<ScreenMessage> _queue;
        bool _messageInProgress = false;

        public ScreenMessageQueue()
        {
            _queue = new Queue<ScreenMessage>();
        }

        public void Push(ScreenMessage msg)
        {
            _queue.Enqueue(msg);
            if (!_messageInProgress)
            {
                _queue.Peek().Go();
                _messageInProgress = true;
            }
        }

        public void Pop()
        {
            if (_queue.Count > 0)
            {
                _queue.Dequeue();
                _messageInProgress = false;
                if (_queue.Count > 0)
                {
                    _messageInProgress = true;
                    _queue.Peek().Go();
                }
            }
        }
    }
}
