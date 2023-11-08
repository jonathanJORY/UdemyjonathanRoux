local lightX, lightY, thorX, thorY = io.read("*n", "*n", "*n", "*n")

while true do
    io.read()  -- Reads the remaining turns (not used)

    local dx = (lightX > thorX) and 1 or ((lightX < thorX) and -1 or 0)
    local dy = (lightY > thorY) and 1 or ((lightY < thorY) and -1 or 0)

    thorX, thorY = thorX + dx, thorY + dy
    print(((dy > 0) and "S" or ((dy < 0) and "N" or "")) ..
          ((dx > 0) and "E" or ((dx < 0) and "W" or "")))
end
