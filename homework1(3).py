def get_message(hour, firstname):
    if hour >= 7 and hour < 12:
        return f"Good morning, {firstname}."
    elif hour >= 12 and hour < 13:
        return f"Yay, it's afternoon, {firstname}."
    elif hour >= 13 and hour < 17:
        return f"Good afternoon, {firstname}."
    elif hour >= 17 and hour < 21:
        return f"Good evening, {firstname}."
    else:
        return f"Good night, {firstname}."


hour = int(input("What time is it?"))
firstname = input("What is your first name?")

welcome = get_message(hour, firstname)

print(welcome)
