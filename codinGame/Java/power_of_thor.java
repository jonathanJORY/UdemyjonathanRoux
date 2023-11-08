import java.util.*;

class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int lightX = in.nextInt(); // the X position of the light of power
        int lightY = in.nextInt(); // the Y position of the light of power
        int x = in.nextInt(); // Thor's starting X position
        int y = in.nextInt(); // Thor's starting Y position

        // game loop
        while (true) {
            int remainingTurns = in.nextInt(); // The remaining amount of turns Thor can move. Do not remove this line.

            // A single line providing the move to be made){} N NE E SE S SW W or NW
            String res = "";
            if (y < lightY){
                res+="S";
                y += 1;
            }
            else if (y > lightY){
                res+="N";
                y -= 1;
            }
            if (x > lightX){
                res+="W";
                x -= 1;
            }
            else if (x < lightX){
                res+="E";
                x += 1;
            }
            System.out.println(res);
        }
    }
}