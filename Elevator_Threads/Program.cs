using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace Elevator_Threads
{
    class Program
    {
        static void Main(string[] args)
        {
            
            Elevator newElevator = new Elevator(ElevatorEnums.MaxFloor());
            ElevatorControl newControl = new ElevatorControl(newElevator);
            Thread runThread = new Thread(new ThreadStart(newControl.Run));
            runThread.Start();
            newElevator.PushButton(1);
            newElevator.PushButton(2);
            newElevator.PushButton(3);

        }
    }
}
