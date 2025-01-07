from drawLine import drawLine, drawDiagonalLine, drawSquare, drawFilledSquare
from drawCircle import drawCircle, drawCircleFill

#defaults
color = [0, 0, 0]
drawCircleFill(color, 99, 99, 12)

# drawLine(color, 50, 50, 'd', 10)
# drawLine(color, 50, 50, 'r', 10)
# drawLine(color, 50, 50, 'l', 10)
# drawLine(color, 50, 50, 'u', 10)

drawDiagonalLine(color, 199, 199, 'ul', 200)
drawDiagonalLine(color, 199, 0, 'dl', 200)
drawLine(color, 0, 199, 'r', 80)


# drawCircle(color, 70, 70, 8)
