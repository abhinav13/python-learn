using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Security.Principal;
using System.Text;
using System.Threading.Tasks;


namespace Elevator_Threads
{
    class Elevator
    {
        private Guid _id;
        
        public List<Button> ButtonList = null;

        public ElevatorEnums.ElevatorDirection Direction { get; set; }
        public int CurrentFloor { get;  set; }

        public ElevatorEnums.ElevatorState CurrentElevatorState { get; set; }
        public ElevatorEnums.DoorState DoorState { get; set; }
        //Defensive coding, so you cant make an elvator without floors
        private Elevator()
        {
        }

        public Elevator(int numfloors)
        {
            int i = 0;
            _id = Guid.NewGuid();
            ButtonList = new List<Button>();
            while (i < numfloors)
            {
                Button tempButton = new Button(ElevatorEnums.ButtonType.Floor, i);
                ButtonList.Insert(i++,tempButton);
            }
            CurrentElevatorState = ElevatorEnums.ElevatorState.Stopped;
            DoorState = ElevatorEnums.DoorState.Close;
            Direction = ElevatorEnums.ElevatorDirection.Neutral;
        }

        public Guid ID
        {
            get { return _id; }
        }

        //Define Operations on the Elevator
        //Push button, take a Button Object as input

        public void PushButton(int floor)
        {
           ButtonList[floor].IsPressed = true;

        }

        public int GetNextFloor()
        {
            throw new NotImplementedException();
        }

        public void UpdateStatus()
        {
            throw new NotImplementedException();
        }

    }
}
