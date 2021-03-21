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


def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360 / n)


def main():
    tess = turtle.Turtle()
    # tess.pensize(2)

    for i in range(3, 100):
        draw_poly(tess, i, 30)

    turtle.done()


if __name__ == '__main__':
    main()
