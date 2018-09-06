my_number = 3
while True:
    print("Enter user_number:")
    user_number = int(input())
    #3 > x <= 2
    if user_number >= my_number:
        print("Repeat number.")
    else:
        print("You win!!!")
        break