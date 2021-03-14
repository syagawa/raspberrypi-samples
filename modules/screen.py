import time
import subprocess

from modules import display

info = display.getDisplayInfo()
rows = info["rows"]
columns = info["columns"]
max_rows = rows
use_rows = 0
screens = []

def getUsableRows():
  n = max_rows - use_rows
  if n < 0:
    return 0
  else:
    return n



def show():
  display.drawBlackRect()

  for sc in screens:
    display.showMessages(sc["matrix"], sc["start"])

def add(index, message):
  if index < 0:
    return
  sc = screens[index]
  sc["matrix"].append(message)
  max = sc["length"]
  if len(sc["matrix"]) > max:
    sc["matrix"].pop(0)

def makeScreen(lines=max_rows):
  if lines > getUsableRows():
    return -1
  global use_rows
  start = use_rows + 1
  end = start + lines - 1
  use_rows = use_rows + lines
  matrix = []
  o = { "start": start, "end": end, "matrix": matrix, "length": lines }
  screens.append(o)
  index = len(screens) - 1
  def f(mes):
    add(index, mes)
  return f
