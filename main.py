from drawLine import drawLine, drawDiagonalLine, drawSquare, drawFilledSquare
from drawCircle import drawCircle, drawCircleFill
from writeLetters import write_string_to_canvas

#write text
color = [0, 0, 0]
write_string_to_canvas(color, 'welkom  bij de\ncodam\npixelcorp\nworkshop', 5, 5, 3)


#draw panda
color = [0, 0, 0]
drawCircleFill(color, 99, 99, 40) # big body
color = [255, 255, 255]
drawCircleFill(color, 99, 54, 20) # head
color = [0, 0, 0]
drawCircle(color, 99, 54, 20)

color = [0, 0, 0]
drawCircleFill(color, 116, 135, 10)
drawCircleFill(color, 82, 135, 10)

drawCircleFill(color, 107, 45, 4)
drawCircleFill(color, 91, 45, 4)

color = [255, 255, 255]
drawCircleFill(color, 99, 110, 16)

color = [200, 0, 0]
drawCircleFill(color, 99, 59, 3)

color = [0, 0, 0]
drawLine(color, 92, 63, 'r', 14)
drawLine(color, 93, 64, 'r', 12)
drawLine(color, 94, 65, 'r', 11)

# drawDiagonalLine(color, 199, 199, 'ul', 200)
# drawDiagonalLine(color, 199, 0, 'dl', 200)
# drawLine(color, 0, 199, 'r', 80)


# drawCircle(color, 70, 70, 8)
