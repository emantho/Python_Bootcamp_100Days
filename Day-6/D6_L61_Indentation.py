from os import system

system("clear")

sky = ""


def my_function():
    # indentation of function
    if sky == "clear":
        # indentation of if
        print("Blue")
    elif sky == "cloudy":
        # indentation of elif
        print("grey")
    print("Hello")


# indentation at the root
print("World")
