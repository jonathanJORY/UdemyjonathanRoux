using System;

class Player {
    static void Main(string[] args) {
        string[] inputs = Console.ReadLine().Split(' ');
        int lightX = int.Parse(inputs[0]);
        int lightY = int.Parse(inputs[1]);
        int thorX = int.Parse(inputs[2]);
        int thorY = int.Parse(inputs[3]);

        while (true) {
            int remainingTurns = int.Parse(Console.ReadLine());  // reading remaining turns (not used)

            int dx = Math.Sign(lightX - thorX);
            int dy = Math.Sign(lightY - thorY);

            thorX += dx;
            thorY += dy;

            Console.WriteLine(
                (dy > 0 ? "S" : (dy < 0 ? "N" : "")) +
                (dx > 0 ? "E" : (dx < 0 ? "W" : ""))
            );
        }
    }
}
