first = int(input())
second = int(input())
third = int(input())
if first == second != third or third == second != first or first == third != second:
    print("2")
elif first != second != third:
    print("0")
elif first == second == third:
    print("3")