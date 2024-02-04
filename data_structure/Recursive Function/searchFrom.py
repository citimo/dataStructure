# 迷宫搜索
from turtle import *
from Maze import Maze
PART_OF_PATH = '*'  # 部分路径
TRIED = '.'  # 尝试
OBSTACLE = '+'  # 障碍
DEAD_END = '-'  # 死胡同 非递归不用死胡同
def searchFrom(maze, startRow, startColumn):
    maze.updatePosition(startRow, startColumn)
    # 检查基本情况
    # 1.遇到墙
    if maze[startRow][startColumn] == OBSTACLE:
        return False
    # 2.遇到已经走过的格子
    if maze[startRow][startColumn] == TRIED:
        return False
    # 3.找到出口
    if maze.isExit(startRow, startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startColumn, TRIED)

    # 否则，依次尝试向4个方向移动
    found = searchFrom(maze, startRow - 1, startColumn) or \
    searchFrom(maze, startRow + 1, startColumn) or \
    searchFrom(maze, startRow, startColumn - 1) or \
    searchFrom(maze, startRow, startColumn + 1)
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
        return found

if __name__ == '__main__':
    a = Maze('D:\VSCode\py\data_structure\Recursive Function\MazeFile.txt')
    searchFrom(a, 0, 0)