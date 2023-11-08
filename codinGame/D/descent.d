import std;

void main()
{

    // game loop
    while (1) {
        int maxHauteur = 0;
        int ind = 0;
        for (int i = 0; i < 8; i++) {
            int mountainH = readln.chomp.to!int; // represents the height of one mountain.
            if (mountainH > maxHauteur){
                maxHauteur = mountainH;
                ind = i;
            }
        }
        // To debug: stderr.writeln("Debug messages...");

        writeln(ind); // The index of the mountain to fire on.
    }
}