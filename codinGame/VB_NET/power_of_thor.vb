Imports System

Module Player
    Sub Main()
        Dim inputs As String() = Console.ReadLine().Split(" ")
        Dim lightX As Integer = Integer.Parse(inputs(0))
        Dim lightY As Integer = Integer.Parse(inputs(1))
        Dim thorX As Integer = Integer.Parse(inputs(2))
        Dim thorY As Integer = Integer.Parse(inputs(3))

        While True
            Dim remainingTurns As Integer = Integer.Parse(Console.ReadLine()) ' Reading remaining turns (not used)

            Dim dx As Integer = Math.Sign(lightX - thorX)
            Dim dy As Integer = Math.Sign(lightY - thorY)

            thorX += dx
            thorY += dy

            Console.WriteLine(
                If(dy > 0, "S", If(dy < 0, "N", "")) +
                If(dx > 0, "E", If(dx < 0, "W", ""))
            )
        End While
    End Sub
End Module
