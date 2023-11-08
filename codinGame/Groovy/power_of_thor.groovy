Scanner sc = new Scanner(System.in)
int lightX = sc.nextInt(), lightY = sc.nextInt(), thorX = sc.nextInt(), thorY = sc.nextInt()

while (true) {
    sc.nextInt() // Read and ignore the remaining amount of turns Thor can move.
    int dx = lightX <=> thorX, dy = lightY <=> thorY
    thorX += dx
    thorY += dy
    println("${dy < 0 ? 'N' : dy > 0 ? 'S' : ''}${dx > 0 ? 'E' : dx < 0 ? 'W' : ''}")
}
