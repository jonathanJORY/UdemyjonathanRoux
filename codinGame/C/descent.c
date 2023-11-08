#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    // game loop
    while (1) {
        int max_height = 0;
        int max_index = 0;
        for (int i = 0; i < 8; i++) {
            // represents the height of one mountain.
            int mountain_h;
            scanf("%d", &mountain_h);
            if (mountain_h > max_height) {
                max_height = mountain_h;
                max_index = i;
            }
        }
        // To debug: fprintf(stderr, "Debug messages...\n");

        printf("%d\n", max_index); // The index of the mountain to fire on.
    }

    return 0;
}
