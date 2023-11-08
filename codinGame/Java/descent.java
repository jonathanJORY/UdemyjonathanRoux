import java.util.*;
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        ArrayList<Integer> hauteurs = new ArrayList<>(); // Initialisez la liste

        // game loop
        while (true) {
            hauteurs.clear(); // Videz la liste à chaque itération
            for (int i = 0; i < 8; i++) {
                int mountainH = in.nextInt(); // represents the height of one mountain.
                hauteurs.add(mountainH);
            }

            // Trouver la montagne la plus haute
            int max_index = 0;
            for (int i = 0; i < hauteurs.size(); i++) {
                if (hauteurs.get(i) > hauteurs.get(max_index)) {
                    max_index = i;
                }
            }

            // Imprimer l'index de la montagne la plus haute
            System.out.println(max_index);
        }
    }
}
