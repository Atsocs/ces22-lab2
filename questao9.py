import turtle


def get_turtle_state(t):
    """ Return turtle's current heading and position. """
    return t.heading(), t.position(), t.isdown()


def restore_turtle_state(t, state):
    """ Set the turtle's heading and position to the given values. """
    t.up()
    t.setheading(state[0])
    t.setposition(state[1][0], state[1][1])
    f = t.down if state[2] else t.up
    f()


def square(t, lenght, bottom_left=None, center=None):
    if bottom_left is None:
        if center is None:
            return
        bottom_left = ((center[i] - lenght / 2) for i in range(len(center)))

    state = get_turtle_state(t)
    t.up()
    t.goto(bottom_left)
    t.down()
    t.setheading(0)
    for i in range(4):
        t.forward(lenght)
        t.left(90)
    restore_turtle_state(t, state)


def main():
    t = turtle.Turtle()
    # t.right(90)
    # t.forward(100)
    # t.left(90)
    # t.backward(100)

    for i in range(1, 6):
        square(t, 20 * i, center=(0, 0))

    turtle.done()


if __name__ == '__main__':
    main()
