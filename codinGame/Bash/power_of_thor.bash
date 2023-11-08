#!/bin/bash

read -r lx ly tx ty

while true; do
  # Read remaining turns if necessary, just to follow the input format
  read -r remaining_turns
  
  # Calculate the direction in which Thor should move
  dx=$((lx > tx ? 1 : (lx < tx ? -1 : 0)))
  dy=$((ly > ty ? 1 : (ly < ty ? -1 : 0)))

  # Update Thor's position
  ((tx += dx))
  ((ty += dy))

  # Build the move string based on the direction
  move=""
  [[ $dy -gt 0 ]] && move+="S"
  [[ $dy -lt 0 ]] && move+="N"
  [[ $dx -gt 0 ]] && move+="E"
  [[ $dx -lt 0 ]] && move+="W"

  # Output the move
  echo "$move"
done
