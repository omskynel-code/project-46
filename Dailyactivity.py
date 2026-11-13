print("=========================================")
print("MY ACTIVITY PLANNER")
print("=========================================")

homework_minutes = int(input("How many minutes will you spend on homework? "))

if homework_minutes > 60:
    plan = "start homework now"
    print("That is a long homework session.")
else:
    plan = "finish homework quickly"
    print("That is a short homework session.")

free_time = input("Is there free time after homework? (yes/no): ")

if free_time == "yes":
    print("Remember to pick a hobby!")

print("===== DAILY PLAN =====")
print("Homework minutes:", homework_minutes)
print("Plan:", plan)
print("Free time:", free_time)
