import std.stdio;
import std.conv;
import std.string;

void main() {
    auto inputs = strip(readln()).split();
    int lightX = to!int(inputs[0]);
    int lightY = to!int(inputs[1]);
    int thorX = to!int(inputs[2]);
    int thorY = to!int(inputs[3]);

    while (true) {
        readln(); // Read and ignore the remaining turns input
        string move = "";
        if (thorY > lightY) { move ~= "N"; thorY--; }
        else if (thorY < lightY) { move ~= "S"; thorY++; }
        if (thorX > lightX) { move ~= "W"; thorX--; }
        else if (thorX < lightX) { move ~= "E"; thorX++; }

        writeln(move);
    }
}
