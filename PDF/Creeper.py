from turtle import*

speed(5)
up()
goto(-30,100)
down()

#La tête
begin_fill()
fillcolor("green")
for i in range(4):
    forward(120)
    left(90)
end_fill()
begin_fill()

#Le corps
fillcolor("green")
forward(35)
right(90)
forward(200)
left(90)
forward(50)
left(90)
forward(200)
end_fill()

backward(200)
right(90)
begin_fill()
fillcolor("green")

#Les pieds
for j in range (4):
        forward(60)
        right(90)
backward(50)
right(90)
for f in range (4):
    forward(60)
    right(90)
end_fill()

#Le visage

#Les yeux
up()
goto(-15,190)
down()
begin_fill()
fillcolor("black")
for z in range(2):
    forward(30)
    left(90)
    forward(30)
    left(90)
left(90)
end_fill()
up()
forward(60)
down()
begin_fill()

#Le nez
for u in range (2):
    forward(30)
    right(90)
    forward(30)
    right(90)
end_fill()

begin_fill()
right(90)
forward(30)
for o in range (2):
    forward(20)
    right(90)
    forward(30)
    right(90)
end_fill()

#La "bouche"
begin_fill()
forward(20)
for t in range (2):
    forward(25)
    left(90)
    forward(20)
    left(90)
end_fill()

right(90)
forward(30)
begin_fill()
for w in range (2):
    forward(20)
    left(90)
    forward(25)
    left(90)

end_fill()
ht()

