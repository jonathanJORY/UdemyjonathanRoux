use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let mut parts = input.split_whitespace().map(|x| x.parse::<i32>().unwrap());
    let (mut lx, mut ly, mut tx, mut ty) = (parts.next().unwrap(), parts.next().unwrap(), parts.next().unwrap(), parts.next().unwrap());

    loop {
        input.clear();
        io::stdin().read_line(&mut input).unwrap(); // read and ignore the remaining turns input
        
        let (dx, dy) = ((lx > tx) as i32 - (lx < tx) as i32, (ly > ty) as i32 - (ly < ty) as i32);
        
        tx += dx;
        ty += dy;
        
        println!("{}{}", if dy > 0 { "S" } else if dy < 0 { "N" } else { "" }, if dx > 0 { "E" } else if dx < 0 { "W" } else { "" });
    }
}
