import turtle


def draw_tree(t, s, l, angle):
    if s <= 0:
        return

    t.forward(l)
    t.left(angle)
    draw_tree(t, s - 1, l * 0.7, angle)
    t.right(2 * angle)
    draw_tree(t, s - 1, l * 0.7, angle)
    t.left(angle)
    t.backward(l)

def main():
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, -100)
    t.pendown()
    t.setheading(90)

    level = int(input("Введіть рівень рекурсії: "))
    draw_tree(t, level, 100, 45)

if __name__ == "__main__":
    main()