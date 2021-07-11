def template(template_row):
    return template_row


def change_value(provided_value):
    pass


def check_winner():
    pass


def enter_value(value):
    valid_value = True

    while valid_value:
        value_selected = input("Player " + value + " please select a value: ")
        if 0 < int(value_selected) < 10:
            valid_value = False
            break

    change_value(value_selected)


if __name__ == "__main__":
    row1 = ["1", "2", "3"]
    row2 = ["4", "5", "6"]
    row3 = ["7", "8", "9"]

    is_winner = False

    while not is_winner:
        print(template(row1))
        print(template(row2))
        print(template(row3))

        enter_value("X")
        is_winner = True
