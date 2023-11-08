
-- game loop
while true do
    ind = 0
    maxH = 0
    for i=0,8-1 do
        mountainH = tonumber(io.read()) -- represents the height of one mountain.
        if maxH < mountainH
            then
                ind = i
                maxH = mountainH
            end
        end

    -- To debug: io.stderr:write("Debug message\n")
    
    print(ind) -- The index of the mountain to fire on.
end