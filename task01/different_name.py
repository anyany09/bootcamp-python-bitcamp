#different names with different answers
print("Please choose names starting on: A, T, M or D ")
name = input("Hey, what is your name? ")

match name[0]:
    case "A":
        print("Hello, " + name.title() + "! How are you?")
    case "T":
        print("Hello, " + name.title() + "! you look great")
    case "M":
        print("Hello, " + name.title() + "! you are nice bro")
    case _:
        print("Hello, you are always great " + name.title())

  
