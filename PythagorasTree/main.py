import turtle


def draw_pifagor_tree(branch_length, t, recursion_level):
    if recursion_level == 0:
        return
    else:
        t.forward(branch_length)
        t.left(45)
        draw_pifagor_tree(branch_length * 0.7, t, recursion_level - 1)
        t.right(90)
        draw_pifagor_tree(branch_length * 0.7, t, recursion_level - 1)
        t.left(45)
        t.backward(branch_length)


def main():
    print("Вітаю! Це програма для створення Дерева Піфагора.")
    while True:
        try:
            recursion_level = int(
                input("Введіть рівень рекурсії: ")
            )
            break
        except ValueError:
            print("Будь ласка, введіть ціле число.")

    screen = turtle.Screen()

    t = turtle.Turtle()
    t.speed('fastest')
    t.color("green")
    t.left(90)
    t.penup()
    t.goto(0, -150)
    t.pendown()

    draw_pifagor_tree(200, t, recursion_level)

    screen.exitonclick()


if __name__ == "__main__":
    main()