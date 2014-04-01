using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Principal;
using System.Text;
using System.Threading.Tasks;


namespace Elevator_Threads
{
    class Elevator
    {
        private Guid _id;
        
        private List<Button> _buttons = null;

        public ElevatorEnums.ElevatorDirection Direction { get; set; }
        public int CurrentFloor { get; private set; }

        //Defensive coding, so you cant make an elvator without floors
        private Elevator()
        {
        }

        public Elevator(int numfloors)
        {
            int i = 0;
            _id = Guid.NewGuid();
            while (i++ < numfloors)
            {
                Button tempButton = new Button(ElevatorEnums.ButtonType.Floor, i);
                _buttons.Add(tempButton);
            }
        }

        public Guid ID
        {
            get { return _id; }
        }

        //Define Operations on the Elevator
        //Push button, take a Button Object as input

        public void PushButton(int floor)
        {
            _buttons[floor].ButtonState = ElevatorEnums.ButtonState.On;
            _buttons[floor].IsPressed = true;

        }

       

    }
}
