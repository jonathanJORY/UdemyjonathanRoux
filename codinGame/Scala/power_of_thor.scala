import scala.io.StdIn._

object Player extends App {
  val Array(lightX, lightY, initialTx, initialTy) = readLine.split(" ").map(_.toInt)
  var (thorX, thorY) = (initialTx, initialTy)

  while (true) {
    readLine  // Read and ignore the remaining turns input.

    val dx = math.signum(lightX - thorX).toInt
    val dy = math.signum(lightY - thorY).toInt

    thorX += dx
    thorY += dy

    println((if (dy > 0) "S" else if (dy < 0) "N" else "") +
            (if (dx > 0) "E" else if (dx < 0) "W" else ""))
  }
}
