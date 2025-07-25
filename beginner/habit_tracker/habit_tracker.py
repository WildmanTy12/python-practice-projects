from datetime import datetime

habit = input("What habit did you complete today?")
today = datetime.now().strftime("%m-%d-%Y")

with open("habit_t.txt", "a") as file:
    file.write(f"{today} - {habit}\n")

with open("habit_t.txt", "r") as file:
    lines = file.readlines()
    last_7 = lines[-7:]
    print("\nYour last 7 tracked habits:")
    for line in last_7:
        print(line.strip())
