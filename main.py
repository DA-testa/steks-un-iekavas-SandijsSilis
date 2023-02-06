# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            print(next + " appended")
            opening_brackets_stack.append(next)

        if next in ")]}":
            if not opening_brackets_stack or not are_matching(next,opening_brackets_stack[len(opening_brackets_stack) - 1]):
                print("Returning")
                opening_brackets_stack.pop()
                print(opening_brackets_stack[len(opening_brackets_stack) - 1] + " popped")
            return i+1
            


def main():
    text = input()
    mismatch = find_mismatch(text)
    if not mismatch:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()