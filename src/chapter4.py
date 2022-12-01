""" Work for chapter 4.
"""

MENU = {"sandwich": 10, "tea": 7}


def restaurant() -> None:
    """Asks for a user to order."""
    total = 0
    while ordering := input("Order: "):
        """
        if ordering.lower() in MENU.keys():
            total += MENU[ordering]
            print(f'{ordering.capitalize()} costs {MENU[ordering]}, total is {total}')
        elif not ordering:
            break
        else:
            print(f'{ordering.capitalize()} is not on the Menu.')
        """
        match ordering:
            case ordering if ordering in MENU.keys():
                total += MENU[ordering]
                print(
                    f"{ordering.capitalize()} costs {MENU[ordering]}, total is {total}"
                )
            case ordering if not ordering:
                break
            case _:
                print(f"{ordering.capitalize()} is not on the Menu.")
    print(f"Your Total is {total}")


def get_rainfall() -> None:
    """Takes a city and rainfall to let you know the total sums for all."""
    rainfall_dict = {}
    while city := input("City name?"):
        rain_amount = input("How much rain?")
        if not city:
            break
        rainfall_dict[city.capitalize()] = rainfall_dict.get(
            city.capitalize(), 0
        ) + int(rain_amount)
    for value in rainfall_dict:
        print(f"{value}: {rainfall_dict[value]}")


def dict_diff(dict_1: dict, dict_2: dict) -> dict:
    """Takes two dicts and returns the difference between the two."""
    if not (unshared_values := set(dict_1.items()) ^ set(dict_2.items())):
        return {}
    dict_diff = {
        pair[0]: [dict_1.get(pair[0]), dict_2.get(pair[0])] for pair in unshared_values
    }
    return dict_diff


def how_many_different_numbers(list_: list) -> int:
    """Takes a list of integers and returns the len of unique ints"""
    return len(set(list_))
