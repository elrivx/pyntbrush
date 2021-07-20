# Importaciones

from utils import *

# Definiciones

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyntBrush")

def draw(win, grid, buttons):
  win.fill(BG_COLOR)
  draw_grid(win, grid)

  for button in buttons:
    button.draw(win)

  pygame.display.update()


def draw_grid(win, grid):
  for i, row in enumerate(grid):
    for j, pixel in enumerate(row):
      pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

  if DRAW_GRID_LINES:
    for i in range(ROWS + 1):
      pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))

    for i in range(COLS + 1):
      pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))




def init_grid(rows, cols, color):
  grid = []

  for i in range(rows):
    grid.append([])
    for _ in range(cols):
      grid[i].append(color)

  return grid


def get_row_col_pos_from(pos):
  x, y = pos
  row = y // PIXEL_SIZE
  col = x // PIXEL_SIZE

  if row >= ROWS:
    raise IndexError

  return row, col

run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK

buttonY = HEIGHT - TOOLBAR_HEIGHT/2 -25
buttons = [
  Button(10, buttonY, 50, 50, BLACK),
  Button(70, buttonY, 50, 50, RED),
  Button(130, buttonY, 50, 50, GREEN),
  Button(190, buttonY, 50, 50, BLUE),
  Button(250, buttonY, 50, 50, YELLOW),
  Button(310, buttonY, 50, 50, WHITE, "Borrar", BLACK),
  Button(370, buttonY, 50, 50, WHITE, "Limpiar", BLACK)
]

# Aquí ejecutamos

while run:
  clock.tick(FPS)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    

    if pygame.mouse.get_pressed()[0]:
      pos = pygame.mouse.get_pos()

      try:
        row, col = get_row_col_pos_from(pos)
        grid[row][col] = drawing_color
      except IndexError:
        for button in buttons:
          if not button.clicked(pos):
            continue

          drawing_color = button.color

          if button.text == "Limpiar":
            grid = init_grid(ROWS, COLS, BG_COLOR)
            drawing_color = BLACK

          

  draw(WIN, grid, buttons)

pygame.quit()