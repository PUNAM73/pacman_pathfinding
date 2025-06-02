# # import heapq

# # def heuristic(a, b):
# #     # Manhattan distance
# #     return abs(a[0] - b[0]) + abs(a[1] - b[1])

# # def a_star_search(start, goal, grid):
# #     open_set = []
# #     heapq.heappush(open_set, (0, start))
    
# #     came_from = {}
# #     g_score = {start: 0}
    
# #     while open_set:
# #         _, current = heapq.heappop(open_set)
        
# #         if current == goal:
# #             path = []
# #             while current in came_from:
# #                 path.append(current)
# #                 current = came_from[current]
# #             path.reverse()
# #             return path
        
# #         for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:  # Up, Down, Left, Right
# #             neighbor = (current[0]+dx, current[1]+dy)
# #             if (0 <= neighbor[0] < len(grid) and
# #                 0 <= neighbor[1] < len(grid[0]) and
# #                 grid[neighbor[0]][neighbor[1]] != 1):  # Not a wall
                
# #                 tentative_g_score = g_score[current] + 1
# #                 if tentative_g_score < g_score.get(neighbor, float('inf')):
# #                     came_from[neighbor] = current
# #                     g_score[neighbor] = tentative_g_score
# #                     f_score = tentative_g_score + heuristic(neighbor, goal)
# #                     heapq.heappush(open_set, (f_score, neighbor))
    
# #     return None  # No path found

# # # 3x3 grid: 0 = free cell, 1 = wall
# # grid = [
# #     [0, 0, 0],
# #     [1, 1, 0],
# #     [0, 0, 0]
# # ]

# # start = (0, 0)
# # goal = (2, 2)

# # path = a_star_search(start, goal, grid)
# # print("Path:", path)



# # astar.py

import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(start, goal, grid):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (current[0]+dx, current[1]+dy)
            if (0 <= neighbor[0] < len(grid) and
                0 <= neighbor[1] < len(grid[0]) and
                grid[neighbor[0]][neighbor[1]] != 1):

                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))

    return []

