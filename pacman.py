import pygame
import sys
from collections import deque
import heapq

# Constants
GRID_SIZE = 20
ROWS = 20
COLS = 20
WIDTH = COLS * GRID_SIZE
HEIGHT = ROWS * GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man A* Autonomous")
clock = pygame.time.Clock()

# Maze grid: 0=empty, 1=wall, 2=food
grid = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,0,0,0,1,0,0,2,0,0,1,0,0,0,1,0,0,2,1],
    [1,0,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,0,0,0,1,2,1,0,0,0,1,0,0,0,1,0,1],
    [1,0,1,0,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,1,2,0,0,0,0,0,0,0,0,2,1,0,0,0,1],
    [1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1],
    [1,2,1,0,0,0,0,0,2,0,0,0,0,1,0,0,0,1,2,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,2,1,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1],
    [1,2,0,0,0,1,0,1,2,0,0,0,0,0,0,1,0,0,2,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,0,2,1,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1],
    [1,0,0,0,1,2,0,0,0,2,0,0,0,0,2,1,0,0,0,1],
    [1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1],
    [1,2,1,0,0,0,0,0,2,0,0,0,0,1,0,0,0,1,2,1],
    [1,0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

# Positions
pacman_pos = [1, 1]
ghost_pos = [18, 18]

def draw_grid():
    for r in range(ROWS):
        for c in range(COLS):
            rect = pygame.Rect(c * GRID_SIZE, r * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            if grid[r][c] == 1:
                pygame.draw.rect(screen, BLUE, rect)
            elif grid[r][c] == 2:
                pygame.draw.circle(screen, WHITE, rect.center, 3)
            pygame.draw.rect(screen, BLACK, rect, 1)

def draw_pacman():
    rect = pygame.Rect(pacman_pos[1] * GRID_SIZE, pacman_pos[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    pygame.draw.circle(screen, YELLOW, rect.center, GRID_SIZE // 2 - 2)

def draw_ghost():
    rect = pygame.Rect(ghost_pos[1] * GRID_SIZE, ghost_pos[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    pygame.draw.circle(screen, RED, rect.center, GRID_SIZE // 2 - 2)

def find_nearest_dot(start):
    visited = set([start])
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if grid[current[0]][current[1]] == 2:
            return current
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            neighbor = (current[0]+dx, current[1]+dy)
            if 0 <= neighbor[0] < ROWS and 0 <= neighbor[1] < COLS:
                if neighbor not in visited and grid[neighbor[0]][neighbor[1]] != 1:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return None

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def a_star_search(start, goal, grid):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))  # (f, g, node, path)

    closed_set = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current == goal:
            # exclude starting pos for movement to next steps
            return path[1:]

        if current in closed_set:
            continue
        closed_set.add(current)

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            neighbor = (current[0]+dx, current[1]+dy)
            if 0 <= neighbor[0] < ROWS and 0 <= neighbor[1] < COLS:
                if grid[neighbor[0]][neighbor[1]] != 1 and neighbor not in closed_set:
                    new_g = g + 1
                    new_f = new_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return []  # no path found

def main():
    global pacman_pos, ghost_pos
    pacman_path = []
    ghost_path = []

    while True:
        screen.fill(BLACK)
        draw_grid()
        draw_pacman()
        draw_ghost()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Pac-Man logic
        if not pacman_path:
            target = find_nearest_dot(tuple(pacman_pos))
            if target:
                if target == tuple(pacman_pos):
                    grid[pacman_pos[0]][pacman_pos[1]] = 0
                    print(f"Pac-Man ate food at {pacman_pos} (no movement needed)")
                else:
                    pacman_path = a_star_search(tuple(pacman_pos), target, grid)
                    print("Pac-Man path:", pacman_path)

        # Pac-Man: move along path
        if pacman_path:
            next_pos = pacman_path.pop(0)
            pacman_pos = list(next_pos)

            if grid[pacman_pos[0]][pacman_pos[1]] == 2:
                grid[pacman_pos[0]][pacman_pos[1]] = 0
                print(f"Pac-Man ate food at {pacman_pos}")

        # Check collision (end game) after Pac-Man moves
        if pacman_pos == ghost_pos:
            print("Ghost caught Pac-Man! Game Over.")
            pygame.quit()
            sys.exit()

        # Ghost logic (chase Pac-Man)
        if not ghost_path:
            ghost_path = a_star_search(tuple(ghost_pos), tuple(pacman_pos), grid)
            print("Ghost path:", ghost_path)

        if ghost_path:
            next_ghost_pos = ghost_path.pop(0)
            ghost_pos = list(next_ghost_pos)

        # Check collision (end game) after both have moved
        if pacman_pos == ghost_pos:
            print("Ghost caught Pac-Man! Game Over.")
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        clock.tick(5)  # Slow down for visibility


print(f"Pac-Man position: {pacman_pos}, Ghost position: {ghost_pos}")

if __name__ == "__main__":
    main()

