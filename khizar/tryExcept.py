x=input("Enter a number ")
try:
    print(int(x))
except ValueError:
    print("input is not a number")