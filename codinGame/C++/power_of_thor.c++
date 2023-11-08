#include <iostream>
#include <string>

int main() {
    int lx, ly, tx, ty;
    std::cin >> lx >> ly >> tx >> ty;

    while (true) {
        // Assuming there's some input to be read here, e.g., remaining turns
        int remaining_turns;
        std::cin >> remaining_turns;

        int dx = (lx > tx) - (lx < tx);
        int dy = (ly > ty) - (ly < ty);

        tx += dx;
        ty += dy;

        std::string move;
        move += dy > 0 ? "S" : (dy < 0 ? "N" : "");
        move += dx > 0 ? "E" : (dx < 0 ? "W" : "");

        std::cout << move << std::endl;
    }

    return 0;
}