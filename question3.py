"""
Question 3
"""

from collections import defaultdict
import heapq as hq

START = 'A'
END = 'C'

FILEPATH = 'graph.txt'

LIST = []

with open(FILEPATH) as fp:
    LINE = fp.readline()
    while LINE:
        S, E, REL = LINE.strip().split(",")
        # Looks like heapq uses a min heap
        # So just invert it and fix later
        REL = -float(REL)
        CONN = [S, E, REL]
        LIST.append(CONN)
        LINE = fp.readline()

# --- DIJKSTRA'S ALGORITHM ---

GRAPH = defaultdict(list)
for s, e, r in LIST:
    GRAPH[s].append((r, e))

Q, VISITED = [(1, START, ())], set()
while Q:
    (COST, CURR, PATH) = hq.heappop(Q)
    if CURR not in VISITED:
        VISITED.add(CURR)
        PATH = (CURR, PATH)
        if CURR == END:
            FIXED_PATH = []
            TEMP_PATH = PATH
            # Fixing weird formatting
            while TEMP_PATH:
                TEMP = TEMP_PATH[0]
                FIXED_PATH.append(TEMP)
                TEMP_PATH = TEMP_PATH[1]
            FIXED_PATH.reverse()
            print("The path was {}".format(FIXED_PATH))
            COST = -COST
            print("The total reliability was {}".format(COST))
            break

        for OCOST, OTHER in GRAPH.get(CURR, ()):
            nxt = -abs(COST * OCOST)
            hq.heappush(Q, (nxt, OTHER, PATH))
