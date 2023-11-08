import Foundation

let inputs = readLine()!.split(separator: " ").map { Int($0)! }
let lightX = inputs[0]
let lightY = inputs[1]
var thorX = inputs[2]
var thorY = inputs[3]

while true {
    let _ = readLine()! // Read and ignore the remaining turns (not used)

    let dx = (lightX > thorX) ? 1 : (lightX < thorX) ? -1 : 0
    let dy = (lightY > thorY) ? 1 : (lightY < thorY) ? -1 : 0

    thorX += dx
    thorY += dy

    let moveY = dy > 0 ? "S" : dy < 0 ? "N" : ""
    let moveX = dx > 0 ? "E" : dx < 0 ? "W" : ""

    print(moveY + moveX)
}
