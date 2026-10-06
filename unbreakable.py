def get_number():
    while True:
        text = input("Enter a whole number: ")

        try:
            return int(text)
        except ValueError:
            print("That is not a valid number. Try again.")


number = get_number()
print(f"You entered {number}")