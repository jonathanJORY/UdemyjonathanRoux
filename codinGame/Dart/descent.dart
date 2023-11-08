import 'dart:io';
import 'dart:math';

String readLineSync() {
  String? s = stdin.readLineSync();
  return s == null ? '' : s;
}


void main() {

    // game loop
    while (true) {
        int maxH = 0;
        int ind = 0;
        for (int i = 0; i < 8; i++) {
            int mountainH = int.parse(readLineSync()); // represents the height of one mountain.
            if (maxH < mountainH){
              ind=i;
              maxH=mountainH;
            }
        }

        // To debug: stderr.writeln('Debug messages...');

        print(ind); // The index of the mountain to fire on.
    }
}