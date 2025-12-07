
print("Day 4 - Printing Department")

# Puzzle I:
# Find x-y positions, where only 4 paper rolls are in the neighbour hood.
#
# Idea:
# We do a brute force around each position and count if there are less than 4
# rolls in the neighborhood.

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [["." for x in range(width)] for y in range(height)]

    def set(self, x, y, value):
        self.data[y][x] = value

    def get(self, x, y):
        return self.data[y][x]

    def width(self):
        return self.width

    def height(self):
        return self.height


def create_grid(data)->Grid:
    height = len(data)
    width = len(data[0].strip())
    grid = Grid(width, height)

    for y in range(height):
        row = data[y].strip()
        for x in range(width):
            grid.set(x, y, row[x])
    return grid

def print_grid(grid:Grid):
    print("")
    for y in range(grid.height):
        row = ""
        for x in range(grid.width):
            row += grid.get(x, y)
        print(row)
    print("")


def count_neighbour_rolls(grid, x, y):
    count = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx = x + dx
            ny = y + dy
            if nx >= 0 and nx < grid.width and ny >= 0 and ny < grid.height:
                if grid.get(nx, ny) == "@":
                    count += 1
    return count

def mark_accessable_positions(grid, mark_grid):
  for x in range(grid.width):
      for y in range(grid.height):
          if grid.get(x, y) == "@":
              count = count_neighbour_rolls(grid, x, y)
              if count < 4:
                  mark_grid.set(x, y, "x")

def remove_accessable_positions(grid, mark_grid)->int:
  removed_count = 0
  for x in range(grid.width):
      for y in range(grid.height):
          if mark_grid.get(x, y) == "x":
              grid.set(x, y, ".")
              mark_grid.set(x, y, ".")
              removed_count += 1
  return removed_count

# --- main ---
# read data
file = open("input.data", "r")
# file = open("example.data", "r")
data = file.readlines()
grid = create_grid(data)
grid2 = create_grid(data)

mark_accessable_positions(grid, grid2)
print_grid(grid2)
removed = remove_accessable_positions(grid, grid2)
sum = removed
while removed > 0:
  mark_accessable_positions(grid, grid2)
  print_grid(grid2)
  removed = remove_accessable_positions(grid, grid2)
  sum += removed
  print_grid(grid2)

print("--- result: number of removed rolls ---")
print(sum)