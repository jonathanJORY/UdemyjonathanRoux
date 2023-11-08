import java.util.*

fun main(args: Array<String>) {
    val input = Scanner(System.`in`)
    val lightX = input.nextInt()
    val lightY = input.nextInt()
    var thorX = input.nextInt()
    var thorY = input.nextInt()

    while (true) {
        input.nextInt() // remaining turns (not used)

        val dx = sign(lightX - thorX)
        val dy = sign(lightY - thorY)

        thorX += dx
        thorY += dy

        print((if (dy > 0) "S" else if (dy < 0) "N" else "") +
              (if (dx > 0) "E" else if (dx < 0) "W" else "") + "\n")
    }
}

fun sign(value: Int): Int = when {
    value > 0 -> 1
    value < 0 -> -1
    else -> 0
}
