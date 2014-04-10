using System;
using System.Collections.Generic;
using System.Threading;
using System.Text;


namespace lazy_Read
{
    class Program
    {

        class ReturnInt
        {
            public  int _value = 0xBEEF;
            private bool IsInitialized = false;
            private volatile int _calculate = 0;

            public int GetVal()
            {                
               // if(_value < 0 ) throw new Exception();
               if (!IsInitialized)
               {

                   _calculate = 7 * 6;
                   _calculate = _calculate + 1;
                   _calculate = _calculate - 1;
                   _value = _calculate;
                   _value = _calculate;
                    IsInitialized = true;                  
                    return _value=42;
                }
                return _value;
            }
        }
        static void Main(string[] args)
        {
            
            for (int i = 0; i < 100000; i++)
            {
                ReturnInt myclass = new ReturnInt();

                new Thread(() =>
                {
                    if (myclass.GetVal() != 42)
                    {
                        //Console.WriteLine("Meaning of life is {0:X}!!",j);
                        throw new Exception("Meaning of Life FAIL! ");
                    }
                    else
                        Console.WriteLine("Value in Thread {0}", myclass.GetVal());
                }).Start();
                //new Thread(() =>
                //{
                //    if (myclass.GetVal() != 42)
                //    {
                //        Console.WriteLine("Thread Found incorrect Value FAIL!!");
                //        throw new Exception("Incorrect Data Value in Thread ");
                //    }
                //    else
                //        Console.WriteLine("Value in Thread {0}", myclass.GetVal());
                //}).Start();

                if (myclass.GetVal() != 42)
                {
                    Console.WriteLine("Fail!! Fail! FAIL");
                    throw new Exception("Incorrect Data Value in Thread ");
                }
                else
                {
                    Console.WriteLine("The meaning of life {0}", myclass.GetVal());
                }
            }
            Console.ReadKey();
        }
    }
}
