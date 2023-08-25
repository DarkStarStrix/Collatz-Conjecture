# Code the collatz conjecture in oop style ask for a number and ask again if they want to continue

import sys
import time
import matplotlib.pyplot as plt
import numpy as np


class Collatz:
    def __init__(self, number):
        self.number = number
        self.steps = 0
        self.sequence = []
        self.sequence.append(self.number)

    def calculate(self):
        while self.number != 1:
            if self.number % 2 == 0:
                self.number = self.number / 2
                self.steps += 1
                self.sequence.append(self.number)
            else:
                self.number = (self.number * 3) + 1
                self.steps += 1
                self.sequence.append(self.number)

    def get_steps(self):
        return self.steps

    def get_sequence(self):
        return self.sequence

    def get_number(self):
        return self.number

    def get_all(self):
        return self.number, self.steps, self.sequence

    def __str__(self):
        return f"Number: {self.number}, Steps: {self.steps}, Sequence: {self.sequence}"

    def __repr__(self):
        return f"Number: {self.number}, Steps: {self.steps}, Sequence: {self.sequence}"

    def __add__(self, other):
        return self.steps + other.steps

    def __sub__(self, other):
        return self.steps - other.steps

    def __mul__(self, other):
        return self.steps * other.steps

    def __truediv__(self, other):
        return self.steps / other.steps

    def __floordiv__(self, other):
        return self.steps // other.steps

    def __mod__(self, other):
        return self.steps % other.steps

    def __pow__(self, other):
        return self.steps ** other.steps

    def __and__(self, other):
        return self.steps & other.steps

    def __xor__(self, other):
        return self.steps ^ other.steps

    def __or__(self, other):
        return self.steps | other.steps

    def __lt__(self, other):
        return self.steps < other.steps

    def __le__(self, other):
        return self.steps <= other.steps


def main():
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Please enter a valid number")
            continue
    collatz = Collatz(number)
    collatz.calculate()
    print(collatz)
    print(collatz.get_all())
    print(collatz.get_number())
    print(collatz.get_sequence())
    print(collatz.get_steps())
    print(collatz + collatz)
    print(collatz - collatz)
    print(collatz * collatz)
    print(collatz / collatz)
    print(collatz // collatz)
    print(collatz % collatz)
    print(collatz ** collatz)
    print(collatz & collatz)
    print(collatz ^ collatz)
    print(collatz | collatz)
    print(collatz < collatz)
    print(collatz <= collatz)

    x = np.arange(len(collatz.get_sequence()))
    y = collatz.get_sequence()
    plt.plot(x, y)
    plt.xlabel("Steps")
    plt.ylabel("Sequence")
    plt.title("Collatz Conjecture")
    plt.show()

    while True:
        try:
            answer = input("Do you want to continue? (y/n): ")
            if answer == "y":
                main()
            elif answer == "n":
                sys.exit()
            else:
                print("Please enter y or n")
                continue
        except ValueError:
            print("Please enter y or n")
            continue


if __name__ == "__main__":
    main()
