cup_size = input("Select the cup size: ").lower

match cup_size:
    case "small":
        print("price is 10")
    case "medium":
        print("price is 15")
    case "large":
        print("price is 20")
    case _:
        print(f"Unknown cup size")