package main

import "fmt"

func main() {
    var lx, ly, tx, ty int
    fmt.Scan(&lx, &ly, &tx, &ty)
    for {
        var t int
        fmt.Scan(&t) // This is just to read the turn number, if necessary
        dx, dy := 0, 0
        if lx > tx {
            dx = 1
        } else if lx < tx {
            dx = -1
        }
        if ly > ty {
            dy = 1
        } else if ly < ty {
            dy = -1
        }
        tx += dx
        ty += dy
        move := ""
        if dy > 0 {
            move += "S"
        } else if dy < 0 {
            move += "N"
        }
        if dx > 0 {
            move += "E"
        } else if dx < 0 {
            move += "W"
        }
        fmt.Println(move)
    }
}
