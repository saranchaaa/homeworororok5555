import colorama

print(colorama.Fore.WHITE)


def uc():
    while True:
        what = int(input(
            """
1 - check all colorama functions;
2 - check if colorama has this attribute;
3 - example of colorama code;
4 - exit.

"""))

        if what == 1:
            for i in dir(colorama):
                print(i)
        elif what == 2:
            w = input("What attribute do you want to check? - ")
            if hasattr(colorama, w):
                print(f"Colorama has {w}.")
            else:
                print(f"Colorama doesn't have {w}.")
        elif what == 3:
            print("print(colorama.Fore.RED + 'string.' + colorama.Fore.WHITE)")
            print("# Line 'colorama.Fore.RED' makes string after this line red. There are other colors. To make string white again, write ' + colorama.Fore.WHITE' in the end of the string, and close it with ')'")
        elif what == 4:
            print("Bye!")
            break
        else:
            print("Incorrect.")


uc()
