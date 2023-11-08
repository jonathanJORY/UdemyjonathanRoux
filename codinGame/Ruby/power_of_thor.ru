STDOUT.sync = true

light_x, light_y, thor_x, thor_y = gets.split.map(&:to_i)

loop do
  gets  # Read and ignore the remaining turns
  move = ''
  move += 'S' if thor_y < light_y
  move += 'N' if thor_y > light_y
  move += 'E' if thor_x < light_x
  move += 'W' if thor_x > light_x
  thor_x += 1 if thor_x < light_x
  thor_x -= 1 if thor_x > light_x
  thor_y += 1 if thor_y < light_y
  thor_y -= 1 if thor_y > light_y

  puts move
end
