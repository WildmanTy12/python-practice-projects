bugs = {}
i = 0


while True:
    choice = input(
        "--- BUG TRACKER ---\n"
        "1. Add a new bug\n"
        "2. View all bugs\n"
        "3. Exit\n"
    )

    if choice == "1":
        # 🟡 These go inside the if-block
        title = input("What is the title? ")
        severity = input("What is the Severity? e.g. low/medium/high ")
        desc = input("Please provide a description.")

        # ✅ Build dictionary and append it
        bugs[title] = {
            "severity": severity,
            "description": desc
        }
        i += 1
    elif choice == "2":
        print(bugs)
    elif choice == "3":
        print("Exiting")
        break
    else:
        print("Invalid choice. Try again.")
