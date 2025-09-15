snack = input("Enter your prefered snack: ").lower()

print(f"user said: {snack}")

if snack == "cookies" or snack == "samosa":
    print(f"great Choice! we'll serve you {snack}")
else:
    print("Sorry, we only serve cookies or samosa with tea")