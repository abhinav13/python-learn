using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Elevator_Threads
{
    class ElevatorEnums
    {
        public enum ButtonType
        {
            Floor,
            Stop,
            Start,
            RingBell

        }

        public enum ButtonState
        {
            On,
            Off
        }

        public enum ElevatorState
        {
            Running,
            Stopped
        }

        public enum ElevatorDirection
        {
            Up,
            Down,
            Neutral
        }

        public enum DoorState
        {
            Open,
            Close
        }

        public static int MinFloor()
        {
            return 0;
        }

        public static int MaxFloor()
        {
            return 5;
        }
    }
}
