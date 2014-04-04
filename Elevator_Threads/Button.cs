using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Elevator_Threads
{
    class Button
    {
        public ElevatorEnums.ButtonType Type { get; private set; }
        public int Floor { get; private set;  }
        
        public bool IsPressed { get; set; }
        public Button(ElevatorEnums.ButtonType t, int floorNum)
        {
            Type = t;
            Floor = floorNum;
        }

      
    }
}
