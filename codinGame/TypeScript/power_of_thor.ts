import { createInterface } from 'readline';

const rl = createInterface({ input: process.stdin, output: process.stdout });
rl.question('', (i) => {
  const [lx, ly, tx, ty] = i.split(' ').map(Number);
  let x = tx, y = ty;
  rl.on('line', (l) => {
    const [dx, dy] = [lx - x, ly - y];
    [x, y] = [x + (dx ? Math.sign(dx) : 0), y + (dy ? Math.sign(dy) : 0)];
    console.log(`${dy > 0 ? 'S' : dy < 0 ? 'N' : ''}${dx > 0 ? 'E' : dx < 0 ? 'W' : ''}`);
  });
});
