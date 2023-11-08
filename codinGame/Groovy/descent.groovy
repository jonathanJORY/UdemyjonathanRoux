input = new Scanner(System.in);

// game loop
while (true) {
    maxH = 0
    ind = 0
    for (i = 0; i < 8; ++i) {
        mountainH = input.nextInt() // represents the height of one mountain.
        if (maxH < mountainH){
            maxH = mountainH
            ind = i
        }
    }

    // To debug: System.err << "Debug messages...\n"

    println ind // The index of the mountain to fire on.
}