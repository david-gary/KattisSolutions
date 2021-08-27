import sys
import math
for line in sys.stdin.readlines():
    line = line.rstrip().split(' ')
    radius = float(line[0])
    if radius == 0:
        break
    markedtotal = int(line[1])
    markedinCircle = int(line[2])
    actual = math.pi*(radius**2)
    square_area = (radius*2)*(radius*2)
    ratio = markedinCircle / markedtotal
    estimate = square_area*ratio
    result = str(actual) + ' ' + str(estimate)
    print(result)