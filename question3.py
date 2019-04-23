"""
Question 3
"""

FILEPATH = 'graph.txt'
with open(FILEPATH) as fp:
    LINE = fp.readline()
    CNT = 1
    while LINE:
        print("Line {}: {}".format(CNT, LINE.strip()))
        LINE = fp.readline()
        CNT += 1
