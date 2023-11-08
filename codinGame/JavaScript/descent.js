
// game loop
while (true) {
    let maxHauteur = -1;
    let ind = -1;
    for (let i = 0; i < 8; i++) {
        const mountainH = parseInt(readline()); // represents the height of one mountain.
        if (maxHauteur < mountainH){
            maxHauteur = mountainH;
            ind = i;
            console.error('Debug messages...',ind)
        }
    }
    // To debug: console.error('Debug messages...');
    console.log(ind);     // The index of the mountain to fire on.
}