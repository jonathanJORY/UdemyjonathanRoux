<?php
fscanf(STDIN, "%d %d %d %d", $lightX, $lightY, $thorX, $thorY);

while (TRUE) {
    fscanf(STDIN, "%d", $remainingTurns); // reads remaining turns from standard input

    $dx = $lightX - $thorX <=> 0; // spaceship operator returns -1, 0, or 1
    $dy = $lightY - $thorY <=> 0;

    $thorX += $dx;
    $thorY += $dy;

    echo (($dy > 0 ? 'S' : ($dy < 0 ? 'N' : '')) .
          ($dx > 0 ? 'E' : ($dx < 0 ? 'W' : ''))) . "\n";
}
?>
