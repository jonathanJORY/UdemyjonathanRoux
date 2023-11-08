using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Player
{
    static void Main(string[] args)
    {

        // game loop
        while (true)
        {   
            int maxHauteur = 0;
            int ind = 0;
            for (int i = 0; i < 8; i++)
            {
                int mountainH = int.Parse(Console.ReadLine()); // represents the height of one mountain.
                if (maxHauteur <mountainH){
                    maxHauteur = mountainH;
                    ind = i;
                }
            }
            // To debug: Console.Error.WriteLine("Debug messages...");

            Console.WriteLine(ind); // The index of the mountain to fire on.

        }
    }
}