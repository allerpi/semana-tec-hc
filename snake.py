"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.

Modders

- Valeria Pineda (A01023979)
- Luis Fernández (A01023675)

"""
from time import sleep
from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
powerup = vector(1000,0)
snake = [vector(10, 0)]
aim = vector(0, -10)
speed = int(450)
state = {'score': 0, 'powerup': True}

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    global speed
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if state['score'] % 10 == 0 and state['score'] != 0 and state['powerup']:
        state['powerup'] = False
        powerup.x = randrange(-15, 15) * 10
        powerup.y = randrange(-15, 15) * 10

    if state['score'] == 100:
        square(head.x, head.y, 9, '#D4AF37')
        for body in snake:
            square(body.x, body.y, 9, '#D4AF37')
        update()
        print('Congratulations, YOU WON!')
        print('Game over')
        sleep(3)
        bye()
        return

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        print('Game over')
        sleep(3)
        bye()
        return

    snake.append(head)

    if head == food:
        state['score'] += 1
        print('Snake:', state['score'])
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        speed = int(speed*0.8)
    elif head == powerup:
        state['powerup'] = True
        speed = int(speed*2)
        powerup.x = 1000
        powerup.y = 0
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    square(powerup.x, powerup.y, 9, 'blue')
    update()
    ontimer(move, speed)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
