using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;


namespace CalculatingDevices
{
    public class Calculator
    {
        public int Value { get; private set; }
        public int Add(int a, int b)
        {
            return a + b;
        }

        public int Multiply(int a, int b)
        {
            return a*b;
        }

        public double AddDouble(double a, double b)
        {
            return a + b;
        }

        public string AddString(string a, string b)
        {
            return a + b;
        }

        public int IncreaseRandomAmount(int a)
        {
            var rand = new Random();
            return (a + rand.Next(1, 100));
        }

        public List<string> ButtonList()
        {
            List<string> buttonsList = new List<string>();
            buttonsList.Add("One");
            buttonsList.Add("Two");
            buttonsList.Add("Three");
            buttonsList.Add("Four");
            buttonsList.Add("Five");
            return buttonsList;
        }

        public List<string> EmptyItemsInButtonList()
        {
            List<string> buttonsList = new List<string>();
            buttonsList.Add("One");
            buttonsList.Add("Two");
            buttonsList.Add("Three");
            buttonsList.Add("Four");
            buttonsList.Add("");
            return buttonsList;
        }

        public int DividbyZero(int a, int b)
        {
            return a/b;
        }

        public int DivideByZeroThrowException(int value, int by)
        {
            if (value > 100)
                throw new ArgumentOutOfRangeException("value");
            return value/by;
        }

        public int RememberAdd(int a)
        {
            Value += a;
            return Value;
        }

        public int RememberSubtract(int a)
        {
            Value -= a;
            return Value;
        }

        public int DivideBy(int b)
        {
            return Value/b;
        }

        public int TakesLongTime(int b)
        {
            Thread.Sleep(5000);
            return b;
        }

        public int FailRandomly(int b)
        {
            var rnd = new Random();
            int divisor = rnd.Next(1, b + 1);
            if (b%divisor == 0)
            {
                throw new Exception();
            }
            else
            {
                return b;
            }
        }
    }
}
