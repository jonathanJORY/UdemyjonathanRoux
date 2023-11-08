import 'dart:io';
import 'dart:math';

String readLineSync() {
  String? s = stdin.readLineSync();
  return s == null ? '' : s;
}

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/
void main() {
    List inputs;
    inputs = readLineSync().split(' ');
    int lx = int.parse(inputs[0]); // the X position of the light of power
    int ly = int.parse(inputs[1]); // the Y position of the light of power
    int tx = int.parse(inputs[2]); // Thor's starting X position
    int ty = int.parse(inputs[3]); // Thor's starting Y position

    // game loop
    while (true) {
        int remainingTurns = int.parse(readLineSync()); // The remaining amount of turns Thor can move. Do not remove this line.
        int dx=(lx>tx)?1:((lx<tx)?-1:0);
        int dy=(ly>ty)?1:((ly<ty)?-1:0);
        tx+=dx;
        ty+=dy;

        String move = '';
        move += dy > 0 ? 'S' : (dy < 0 ? 'N' : '');
        move += dx > 0 ? 'E' : (dx < 0 ? 'W' : '');

        print(move);
      }
}