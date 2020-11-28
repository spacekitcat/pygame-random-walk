import random
import math
import pygame as pg
from enum import Enum
import numpy as np

WINSIZE = [800, 500]

def is_exit_key(e):
  return e.type == pg.KEYUP and (e.key == pg.K_ESCAPE or e.key == pg.K_q)

class Direction(Enum):
  North = 0,
  East = 1,
  South = 2,
  West = 3

def draw_line(origin, direction, length, color):
  destination = None
  if direction == Direction.North:
    destination = (origin[0], origin[1] + length)
  elif direction == Direction.East:
    destination = (origin[0] + length, origin[1])
  elif direction == Direction.South:
    destination = (origin[0], origin[1] - length)
  elif direction == Direction.West:
    destination = (origin[0] - length, origin[1])

  pg.draw.line(pg.display.get_surface(), color, origin, destination, 1)

  return destination

def choose_random_direction(origin, previous):
  choices = []

  if origin[0] > 0 and not previous == Direction.West:
    choices.append(Direction.West)
  
  if origin[0] < WINSIZE[0] and not previous == Direction.East:
    choices.append(Direction.East)
  
  if origin[1] < WINSIZE[1] and not previous == Direction.North:
    choices.append(Direction.North)
  
  if origin[1] > 0 and not previous == Direction.South:
    choices.append(Direction.South)

  return random.choice(choices)

def choose_random_color():
  return list(np.random.choice(range(256), size=3))

def main():
  random.seed()
  clock = pg.time.Clock()
  pg.init()
  pg.mouse.set_visible(False)
  screen = pg.display.set_mode(WINSIZE, pg.FULLSCREEN)
  pg.display.set_caption("THERE WAS A SPIDER")
  black = 20, 20, 40
  screen.fill(black)

  done = 0
  origin = (WINSIZE[0] / 2, WINSIZE[1] / 2)
  direction = choose_random_direction(origin, None)
  while not done:
    origin = draw_line(origin, direction, 5,  choose_random_color())
    direction = choose_random_direction(origin, direction)
    pg.display.update()
    for e in pg.event.get():
      if e.type == pg.QUIT or is_exit_key(e):
        done = 1
        break
      if e.type == pg.KEYUP and e.key == pg.K_f:
        pg.display.toggle_fullscreen() 

    clock.tick(50)

if __name__ == "__main__":
  main()