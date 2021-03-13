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
  return index

def show(index, message):
  if index < 0:
    return
  sc = screens[index]
  sc["matrix"].append(message)
  max = sc["length"]
  if len(sc["matrix"]) > max:
    array_shift(sc["matrix"])

  for n in range(len(sc["matrix"])):
    print(sc["matrix"][n])
    # display.showMessage(sc["matrix"][n], n + 1)
    display.showMessage("aaa", n + 1)

