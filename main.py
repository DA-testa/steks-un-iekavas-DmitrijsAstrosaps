# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)

        if next in ")]}":
            # Process closing bracket, write your code here
            pers = ")]}".index(next)
            match pers:
                case 0:
                    idiot = "("
                case 1:
                    idiot = "["
                case 2:
                    idiot = "{"
            if (len(opening_brackets_stack)>0) and (opening_brackets_stack[len(opening_brackets_stack)-1]==idiot):
                opening_brackets_stack.pop()
            else:
                return i+1
        if (len(opening_brackets_stack)==0):
            return -45;


def main():
    text = input()
    if ("I" in text):
        text = input()
        mismatch = find_mismatch(text)
        if mismatch == -45:
            print("Success")
        else:
            print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
