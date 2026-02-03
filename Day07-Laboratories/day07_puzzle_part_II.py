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
      output = ""
      for row in self.data:
        output += "\n"
        for cell in row:
          output += " " + str(cell) + " "
      return output

def init_grid(data):
  height = len(data)
  width = len(data[0])
  grid = Grid(width, height)
  for line in data:
    grid.set_row(data.index(line), line.strip())
  return grid

def start_beam(grid:Grid, count_grid:Grid):
  start_idx = -1
  width = grid.get_width()
  for i in range(0,width):
    if grid.get(i, 0) == "S":
      start_idx = i
      break
  grid.set(start_idx, 1, "|")
  count_grid.set(start_idx, 1, 1)

def count_splits(grid:Grid):
  count = 0
  for y in range(0, grid.get_height()):
    for x in range(0, grid.get_width()):
      if grid.get(x, y) == "^" and grid.get(x, y-1) == "|":
        count += 1
  return count

def count_timelines(grid:Grid):
  count = 0
  y = grid.get_height()-1
  for x in range(0, grid.get_width()):
    count += int(grid.get(x,y))
  return count


def init_count_grid(width: int, height: int)->Grid:
  grid = Grid(width, height)
  for y in range(0, height):
    for x in range(0, width):
      grid.set(x, y, int(0))
  return grid


def perform_time_beam(grid:Grid):
  count_grid = init_count_grid(grid.get_width(), grid.get_height())
  start_beam(grid, count_grid)
  y = 1
  while y < grid.get_height()-1:
    x = 0
    while x < grid.get_width():
      # split beam
      if grid.get(x, y) == "|":
        # split beam
        if grid.get(x, y+1) == "^":
          grid.set(x-1, y+1, "|")
          grid.set(x+1, y+1, "|")
          # count timelines
          count_top = int(count_grid.get(x, y))
          count_left = int(count_grid.get(x-1, y+1))
          count_grid.set(x-1, y+1, int(count_left+count_top))
          count_right = int(count_grid.get(x+1, y+1))
          count_grid.set(x+1, y+1, int(count_right+count_top))
        # continue beam
        else:
          grid.set(x, y+1, "|")
          count_top = int(count_grid.get(x, y))
          count_bot = int(count_grid.get(x, y+1))
          count_grid.set(x, y+1, int(count_top+count_bot))
      x += 1
    y += 1
  return count_grid

# Part II
# --- main ---
# read data
file = open("input.data", "r")
# file = open("example.data", "r")
data = file.readlines()

grid = init_grid(data)
time_grid = perform_time_beam(grid)
splits = count_splits(grid)
timelines = count_timelines(time_grid)

print(grid)
print(time_grid)
print("Splits: " + str(splits))
print("Timelines: " + str(timelines))