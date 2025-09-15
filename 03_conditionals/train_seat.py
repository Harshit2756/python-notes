seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()

match seat_type:
    case "sleeper":
        print("hello1")
    case "ac":
        print("hello2")
    case "general":
        print("hello3")
    case "luxury":
        print("hello4")
    case "general":
        print("hello5")
    case _:
        print("Invalid seat type")