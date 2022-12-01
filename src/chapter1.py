""" Code for chapter 1.
"""
import random


def guessing_game():
    """Guesing game function."""
    guessing_int = random.randint(1, 100)
    while input_as_int := int(input("guess a number")):
        match input_as_int:
            case input_as_int if input_as_int < guessing_int:
                print("Too low")
            case input_as_int if input_as_int == guessing_int:
                print("Just right")
                break
            case input_as_int if input_as_int > guessing_int:
                print("Too High")
            case _:
                print("Not an acceptible value")


def my_sum(*nums):
    """Sums all numbers."""
    total_ = 0
    for num in nums:
        total_ += num
    return total_


def run_timing():
    """ """
    run_times = []
    while True:
        run_time_input = input("Enter 10 km run time: ")
        if not run_time_input:
            print(
                f"Average of {sum(run_times)/len(run_times):.2f}, over {len(run_times)} runs"
            )
            break
        else:
            try:
                run_time = float(run_time_input)
                run_times.append(run_time)
            except ValueError as e:
                print("That is not a valid number")


def hex_output():
    raw_int_input = input("Enter a hex numbr: ")
    decimal_value = 0
    for exponent, value in enumerate(reversed(raw_int_input)):
        decimal_value += int(value, 16) * 16**exponent
    return decimal_value
