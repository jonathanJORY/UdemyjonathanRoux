let [lightX, lightY, thorX, thorY] = readline().split(' ').map(Number);

while (true) {
  readline(); // read and ignore the remaining turns input

  let dx = Math.sign(lightX - thorX);
  let dy = Math.sign(lightY - thorY);

  thorX += dx;
  thorY += dy;

  console.log((dy > 0 ? 'S' : '') + (dy < 0 ? 'N' : '') + (dx > 0 ? 'E' : '') + (dx < 0 ? 'W' : ''));
}