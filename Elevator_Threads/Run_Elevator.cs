using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Principal;
using System.Text;
using System.Collections;
using System.Threading;
using System.Threading.Tasks;

namespace Elevator_Threads
{
    class ElevatorControl
    {
        Hashtable _listOfStopHashtable = null;
        private Elevator thisElevator = null;
        public ElevatorControl(Elevator initElevator)
        {
            _listOfStopHashtable = new Hashtable();
            thisElevator = initElevator;
        }

        private void PrintElevatorState(Elevator thisElevator)
        {
            Console.WriteLine("Elevator State is {0}\t Elevator Door is {1}\t Elevator Floor is {2} Current Direction {3}\n",thisElevator.CurrentElevatorState,
                                thisElevator.DoorState,thisElevator.CurrentFloor,thisElevator.Direction);
        }

        public void Run()
        {
            int i = 0;
            int maxFloor = ElevatorEnums.MaxFloor();
            int minFloor = ElevatorEnums.MinFloor();
            while (true)
            {
                try
                {
                    //If there are not more buttons pressed, just stay
                    var _templist = thisElevator.ButtonList.FindAll(ii => ii.IsPressed == true);
                    if (_listOfStopHashtable.Count !=0 || _templist.Count != 0 )
                    {
                        PrintElevatorState(thisElevator);
                        //if we are stopped
                        //Check if we were moving down
                        //IF we are stopped now, see if we need to move down. 
                        if (thisElevator.CurrentElevatorState == ElevatorEnums.ElevatorState.Stopped)
                        {
                            if ((thisElevator.Direction == ElevatorEnums.ElevatorDirection.Down && thisElevator.CurrentFloor != minFloor)
                                  || thisElevator.Direction == ElevatorEnums.ElevatorDirection.Neutral)
                            {
                                //Check for floors above us that we need to move to

                                for (i = thisElevator.CurrentFloor; i > minFloor; i--)
                                {
                                        if (thisElevator.ButtonList[i].Floor < thisElevator.CurrentFloor &&
                                            thisElevator.ButtonList[i].IsPressed)
                                        {
                                            _listOfStopHashtable[thisElevator.ButtonList[i].Floor] =
                                                thisElevator.ButtonList[i];
                                            thisElevator.CurrentElevatorState = ElevatorEnums.ElevatorState.Running;
                                            thisElevator.DoorState = ElevatorEnums.DoorState.Close;
                                            thisElevator.Direction = ElevatorEnums.ElevatorDirection.Down;
                                        }
                                }
                                
                            }
                            //This is broken logic. You need to fix this
                            if ((thisElevator.Direction == ElevatorEnums.ElevatorDirection.Up &&
                                 thisElevator.CurrentFloor != maxFloor) ||
                                thisElevator.Direction == ElevatorEnums.ElevatorDirection.Neutral)
                            {
                                //Check for floors above us that we need to move to

                                for (i = thisElevator.CurrentFloor; i < maxFloor; i++)
                                {
                                    if (thisElevator.ButtonList[i].Floor > thisElevator.CurrentFloor &&
                                        thisElevator.ButtonList[i].IsPressed)
                                    {
                                        _listOfStopHashtable[thisElevator.ButtonList[i].Floor] =
                                            thisElevator.ButtonList[i];
                                        thisElevator.CurrentElevatorState = ElevatorEnums.ElevatorState.Running;
                                        thisElevator.DoorState = ElevatorEnums.DoorState.Close;
                                        thisElevator.Direction = ElevatorEnums.ElevatorDirection.Up;
                                    }
                                }
                            }

                        }
                        else if (thisElevator.CurrentElevatorState == ElevatorEnums.ElevatorState.Running)
                        {
                            //See if we need to stop
                            if (_listOfStopHashtable.Count != 0)
                            {
                                if (ReachedNextFloor(thisElevator))
                                {
                                    //Stop the Elevator
                                    //Open the door
                                    //Switch of the button
                                    //Remove the button from our list of stops
                                    thisElevator.CurrentElevatorState = ElevatorEnums.ElevatorState.Stopped;
                                    thisElevator.DoorState = ElevatorEnums.DoorState.Open;
                                    thisElevator.ButtonList[thisElevator.CurrentFloor].IsPressed = false;
                                    _listOfStopHashtable.Remove(thisElevator.CurrentFloor);
                                }
                                else
                                {
                                    thisElevator.CurrentFloor++;
                                }
                            }
                        }
                  
                    }
                    else
                    {
                        thisElevator.Direction = ElevatorEnums.ElevatorDirection.Neutral;
                    }
                    Thread.Sleep(1000);
                }
                catch (Exception ex)
                {
                    Console.WriteLine("Caught Exception {0}", ex.Message);
                }
            }
        }

        private bool ReachedNextFloor(Elevator thisElevator)
        {
            return (_listOfStopHashtable.Count != 0 &&
                    _listOfStopHashtable.ContainsKey(thisElevator.CurrentFloor));
        }
    }
}
