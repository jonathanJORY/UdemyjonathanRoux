package main

import "fmt"

func main() {
    for {
        var maxH = 0
        var  ind = 0
        for i := 0; i < 8; i++ {
            // mountainH: represents the height of one mountain.
            var mountainH int
            fmt.Scan(&mountainH)
            if ( maxH < mountainH){
                maxH = mountainH
                ind = i
            }
        }
        
        // fmt.Fprintln(os.Stderr, "Debug messages...")
        fmt.Println(ind) // The index of the mountain to fire on.
    }
}