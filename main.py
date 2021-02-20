import random
import math
import pygame as pg
from enum import Enum
import numpy as np

WINSIZE = [800, 500]

def is_exit_key(e):
  return e.type == pg.KEYUP and (e.key == pg.K_ESCAPE or e.key == pg.K_q)

def choose_random_color():
  return list(np.random.choice(range(256), size=3))

def generate_random_direction(origin):
  x_choices = [0]
  y_choices = [0]
  
  if origin[0] > 0:
    x_choices.append(-1)
  
  if (origin[0] < WINSIZE[0]):
    x_choices.append(1)
    
  if origin[1] > 0:
    y_choices.append(-1)

  if (origin[1] < WINSIZE[1]):
    y_choices.append(1)
    
  return [np.random.choice(x_choices), np.random.choice(y_choices)]

def draw_direction(origin, direction, length, color):
  destination = np.add(origin, np.multiply(direction, length))
  pg.draw.line(pg.display.get_surface(), color, origin, tuple(destination), 1)
  return destination

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
  origin = [WINSIZE[0] / 2, WINSIZE[1] / 2]
  while not done:
    direction = generate_random_direction(origin)
    origin = draw_direction(origin, direction, 5,  choose_random_color())
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
