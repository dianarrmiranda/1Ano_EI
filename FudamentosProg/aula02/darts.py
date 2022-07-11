# You throw a dart that hits coordinates (x, y) on a dartboard.
# Create a program that gives you the score.
# See:
#   https://en.wikipedia.org/wiki/Darts#Dartboard
#   https://www.dimensions.com/element/dartboard

print("Enter the coordinates in mm from the center of the board.")
x = float(input("x? "))
y = float(input("y? "))

# Points of the sectors, clockwise from the top
# Example: the sector right from the center is POINTS[5] == 6.
POINTS = (20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5)

if (x**2+y**2)<(6.35**2):
    score=50
elif (6.35**2)<(x**2+y**2)<(16**2):
    score=25
elif (16**2)<(x**2+y**2)<(170**2):
    import math
    if x!=0:
        angle=math.atan2(y,x)
        if angle>(math.pi/2)+(math.pi/20):
            angle=angle-(math.pi*2)
    elif x==0:
        if y<0:
            angle=math.pi/2
        elif y>0:
            angle=-(math.pi/2)
    posicao=0
    a=(math.pi/2)-(math.pi/20)
    b=(math.pi/2)+(math.pi/20)
    while(posicao<20):
        if angle==a or angle==b:
            score=0
            break
        elif a<angle<b:
            score=POINTS[posicao]
            break
        else:
            a=a-(math.pi/10)
            b=b-(math.pi/10)
            posicao=posicao+1
    if ((107)**2)>(x**2+y**2)>((99)**2):
        score=score*3
    if (x**2+y**2)>((162)**2):
        score=score*2
else:
    score=0

# COMPLETE...

print('Score:',score)
