lx, ly, x, y = [int(i) for i in input().split()]

while True:
    move  = 'N' if y>ly else 'S' if y<ly else ''
    move += 'W' if x>lx else 'E' if x<lx else ''
    
    if 'N' in move: y-=1
    if 'S' in move: y+=1
    if 'W' in move: x-=1
    if 'E' in move: x+=1

    print(move)