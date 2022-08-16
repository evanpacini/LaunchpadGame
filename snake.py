import time
import random
import sys
import launchpad_py as lpad

# Initialise launchpad
if lpad.LaunchpadMiniMk3().Check(1):
    lp = lpad.LaunchpadMiniMk3()
    if lp.Open(1, "MiniMK3"):
        print("Connected to Launchpad Mini Mk3.")
        lp.Reset()  # Turn all LEDs off
    else:
        print("Couldn't connect to Launchpad Mini Mk3!")
        exit(0)
else:
    print("Did not find any Launchpad Mini Mk3!")
    exit(0)


def lose():
    print("You lose!")
    lp.Reset()  # Turn all LEDs off
    # Codes for LEDs
    LEDcodes = list(range(81, 89)) + list(range(71, 79)) + list(range(61, 69)) + list(range(51, 59)) + \
        list(range(41, 49)) + list(range(31, 39)) + \
        list(range(21, 29)) + list(range(11, 19))
    loseimage = [0, 0, 7, 7, 0, 0, 0, 0, 0, 7, 7, 7, 7, 0, 0, 0, 0, 1, 7, 1, 7, 0, 0, 0, 0, 7, 7, 7, 83, 83, 7, 0,
                 7, 0, 83, 83, 83, 83, 0, 7, 0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 83, 83, 83, 83, 0, 0, 0, 0, 83, 0, 0, 83, 0, 0]
    for i in range(len(LEDcodes)):
        lp.LedCtrlRawByCode(LEDcodes[i], loseimage[i])  # Draw splendid image
    lp.LedCtrlPulseByCode(62, 25)
    lp.LedCtrlPulseByCode(64, 25)
    exit(0)


def resetDirections():
    lp.LedCtrlPulseByCode(91, 0)
    lp.LedCtrlPulseByCode(92, 0)
    lp.LedCtrlPulseByCode(93, 0)
    lp.LedCtrlPulseByCode(94, 0)


def checkButtons(event):
    global v
    if len(event) and event[1]:
        if event[0] == 91 and v[1] != 1:  # UP
            resetDirections()  # Reset diretion
            v[0] = 0
            v[1] = -1  # Set direction
            lp.LedCtrlPulseByCode(91, 54)

        elif event[0] == 92 and v[1] != -1:  # DOWN
            resetDirections()  # Reset diretion
            v[0] = 0
            v[1] = 1  # Set direction
            lp.LedCtrlPulseByCode(92, 54)

        elif event[0] == 93 and v[0] != 1:  # LEFT
            resetDirections()  # Reset diretion
            v[0] = -1  # Set direction
            v[1] = 0
            lp.LedCtrlPulseByCode(93, 54)

        elif event[0] == 94 and v[0] != -1:  # RIGHT
            resetDirections()  # Reset diretion
            v[0] = 1  # Set direction
            v[1] = 0
            lp.LedCtrlPulseByCode(94, 54)

        elif event[0] == 19:  # STOP
            lose()
        lp.ButtonFlush()


# set starting values (values are chosen by preference):
snakeMovementDelay = 0.5
snakeMovementDelayDecrease = -0.02
snake = [[3, 6], [3, 5]]
food = [random.randint(0, 7), random.randint(0, 7)]
v = [0, -1]

# start delay:
time.sleep(2)
print("Score:", len(snake)-2)

# -----------------------------------
#             game loop
# -----------------------------------
while True:
    # check if snake bites itself:
    if snake[0] in snake[1:]:
        lose()

    # check if snake eats food:
    if snake[0] == food:
        snake.append([0, 0])  # grow snake
        sys.stdout.write("\033[F")  # move up cursor one line
        print("\rScore:", len(snake)-2)  # print score
        # generate new food
        while food in snake:
            food = [random.randint(0, 7), random.randint(0, 7)]
        snakeMovementDelay += snakeMovementDelayDecrease

    # check joystick events:
    checkButtons(lp.ButtonStateRaw())

    # remove previous tail
    lp.LedCtrlXYByCode(snake[len(snake)-1][0], snake[len(snake)-1][1]+1, 0)

    # move snake:
    for i in range((len(snake) - 1), 0, -1):
        snake[i][0] = snake[i - 1][0]
        snake[i][1] = snake[i - 1][1]

    snake[0][0] += v[0]
    snake[0][1] += v[1]

    # check game borders:
    if snake[0][0] > 7:
        snake[0][0] -= 8
    elif snake[0][0] < 0:
        snake[0][0] += 8
    if snake[0][1] > 7:
        snake[0][1] -= 8
    elif snake[0][1] < 0:
        snake[0][1] += 8

    # update matrix:
    lp.LedCtrlXYByCode(food[0], food[1]+1, 5)  # draw food
    for i in range(len(snake)):  # draw snake body
        lp.LedCtrlXYByCode(snake[i][0], snake[i][1]+1, 25)
    lp.LedCtrlXYByCode(snake[0][0], snake[0][1]+1, 10)  # draw snake head
    # snake speed (game loop delay):
    time.sleep(snakeMovementDelay)
