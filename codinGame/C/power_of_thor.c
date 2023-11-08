#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    int light_x, light_y, initial_tx, initial_ty;
    int emplacement_x, emplacement_y;
    scanf("%d%d%d%d", &light_x, &light_y, &initial_tx, &initial_ty);

    emplacement_x = initial_tx;
    emplacement_y = initial_ty;

    while (1) {
        int remaining_turns;
        scanf("%d", &remaining_turns);

        if (emplacement_x < light_x && emplacement_y < light_y) {
            printf("SE\n");
            emplacement_x += 1;
            emplacement_y += 1;
        } else if (emplacement_x < light_x && emplacement_y > light_y) {
            printf("NE\n");
            emplacement_x += 1;
            emplacement_y -= 1;
        } else if (emplacement_x > light_x && emplacement_y > light_y) {
            printf("NW\n");
            emplacement_x -= 1;
            emplacement_y -= 1;
        } else if (emplacement_x > light_x && emplacement_y < light_y) {
            printf("SW\n");
            emplacement_x -= 1;
            emplacement_y += 1;
        } else if (emplacement_x > light_x && emplacement_y == light_y) {
            printf("W\n");
            emplacement_x -= 1;
        } else if (emplacement_x < light_x && emplacement_y == light_y) {
            printf("E\n");
            emplacement_x += 1;
        } else if (emplacement_x == light_x && emplacement_y < light_y) {
            printf("S\n");
            emplacement_y += 1;
        } else if (emplacement_x == light_x && emplacement_y > light_y) {
            printf("N\n");
            emplacement_y -= 1;
        }
    }

    return 0;
}
