
from turtle import *
speed(100)
color('red', 'skyblue')
begin_fill()
while True:
	forward(250)
	left(1)
	right(200)
	if abs(pos()) < 1:
		break

end_fill()

done()