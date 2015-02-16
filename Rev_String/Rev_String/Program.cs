using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Rev_String
{
    class Program
    {
       
        static string StringReverse(string S)
        {
            char[] sentence = S.ToCharArray();
                      
            for(int i=0; i< S.Length/2; i++)
            {
                int a = sentence[i];
                int b = sentence[S.Length - 1 - i];
              
                a = a ^ b;
                b = a ^ b;
                a = a ^ b;
                                
                sentence[i] = (char)a;
                sentence[S.Length - 1 - i] = (char)b;
               
            }
            string s = new string(sentence);
            return s;
        }

        static void Main(string[] args)
        {
            string name = "My Name is Jed Mao";
            Console.WriteLine("String Before Reversing {0}", name);
            Console.WriteLine("Reversed String {0}", StringReverse(name));
            Console.ReadKey();
        }
    }
}
