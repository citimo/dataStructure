# 解决汉诺塔问题
def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)

def moveDisk(fp, tp):
    print("moving disk from %d to %d\n" % (fp, tp))

if __name__ == '__main__':
    moveTower(4, 1, 2, 3)
