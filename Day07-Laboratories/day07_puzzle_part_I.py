print("Day 7 - Laboratories")

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [["." for x in range(width)] for y in range(height)]

    def set(self, x, y, value):
        self.data[y][x] = value

    def set_row(self, y:int, row:str):
      for x in range(len(row)):
        self.data[y][x] = row[x]

    def get(self, x, y):
        return self.data[y][x]

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def __str__(self):
        return "\n".join(["".join(row) for row in self.data])

def init_grid(data):
  height = len(data)
  width = len(data[0])
  grid = Grid(width, height)
  for line in data:
    grid.set_row(data.index(line), line.strip())
  return grid

def start_beam(grid:Grid):
  start_idx = -1
  width = grid.get_width()
  for i in range(0,width):
    if grid.get(i, 0) == "S":
      start_idx = i
      break
  grid.set(start_idx, 1, "|")

def perform_beam(grid:Grid):
  start_beam(grid)
  y = 2
  while y < grid.get_height():
    x = 0
    while x < grid.get_width():
      # split beam
      if grid.get(x, y) == "^":
        if grid.get(x, y-1) == "|":
          if grid.get(x-1, y) == ".":
            grid.set(x-1, y, "|")
          if grid.get(x+1, y) == ".":
            grid.set(x+1, y, "|")
      # continue beam
      elif grid.get(x, y) == ".":
        if grid.get(x, y-1) == "|":
          grid.set(x, y, "|")
      x += 1
    y += 1

def count_splits(grid:Grid):
  count = 0
  for y in range(0, grid.get_height()):
    for x in range(0, grid.get_width()):
      if grid.get(x, y) == "^" and grid.get(x, y-1) == "|":
        count += 1
  return count

# Part I
# --- main ---
# read data
file = open("input.data", "r")
# file = open("example.data", "r")
data = file.readlines()

grid = init_grid(data)
perform_beam(grid)
splits = count_splits(grid)

print(grid)
print("Splits: " + str(splits))