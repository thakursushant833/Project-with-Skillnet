total_bottles=int(input("Enter total number of water bottles-> "))
bottles_per_day = int(input("Enter bottles you drink per day-> "))
day=1
while total_bottles > 0:
    print("Day", day, end=": ")

    if total_bottles >= bottles_per_day:
        print("Drank", bottles_per_day, "bottles.", end=" ")
        total_bottles = total_bottles - bottles_per_day
    else:
        print("Drank", total_bottles, "bottle.", end=" ")
        total_bottles = 0

    print(total_bottles, "left.")
    day= day+1
print("Refill Bottles!")
