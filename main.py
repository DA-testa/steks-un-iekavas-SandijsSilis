# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)

        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[len(opening_brackets_stack) - 1], next):
                return i+1
            else:
                opening_brackets_stack.pop() 
            


def main():
    text = input()
    mismatch = find_mismatch(text)
    while text=="I" or text=="" or text=="\n":
        text = input()
        mismatch = find_mismatch(text)
    if not mismatch:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()