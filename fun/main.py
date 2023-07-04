import Json_config

user_pass = {}

while True:
    # when you type show first
    username = input("choose a username, or just type 'exit' to exit: ")
    match username:
        case "show":
            for n, i in enumerate(user_pass):
                print(f"{n + 1}-{i}:{user_pass[i]}")
            continue

        case "save":
            Json_config.make(user_pass)
            print(user_pass)
            continue
        case "exit":
            break

    if len(username) < 2 or username.isdigit():
        print("must contains at least 4 characters")
        continue

    while True:
        password = input("choose a password (must be more than 8 characters contains a Maj and nums): ")
        if len(password) < 8:
            print("its short man!")
            continue

        pass_digit = [d for d in password if d.isdigit()]
        pass_alpha = [a for a in password if a.isalpha()]
        pass_upper = [u for u in password if u.isupper()]
        pass_lower = [m for m in password if m.islower()]

        if not bool(pass_lower):
            print("-there's no minicule alphabets.")
        if not bool(pass_alpha):
            print("-There's no Alphabets.")
        if not bool(pass_digit):
            print("-Password does not contain a number.")
        if not bool(pass_upper):
            print("-Password must contain a Maj.")

        if not bool(pass_upper):
            continue
        elif not bool(pass_digit):
            continue
        elif not bool(pass_lower):
            continue
        print("All good man!")
        user_pass[username] = password
        break

    continue
