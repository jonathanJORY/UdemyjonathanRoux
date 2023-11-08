#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{

    // game loop
    while (1) {
        int max_hauteur = 0;
        int ind = -1;
        for (int i = 0; i < 8; i++) {
            int mountain_h; // represents the height of one mountain.
            cin >> mountain_h; cin.ignore();
            if (max_hauteur < mountain_h){
                ind=i;
                max_hauteur=mountain_h;
            }
        }

        // To debug: cerr << "Debug messages..." << endl;

        cout << ind << endl; // The index of the mountain to fire on.
    }
}