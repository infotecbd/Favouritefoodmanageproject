from random import choice

favorite_foods=[] #initialize empty foods list


while True:
    print("Favourite Food Manager")

    print ("1. Add Foods")
    print("2. Remove Foods")
    print("3. View favourite all foods")
    print("4. Exit")

    choice = input("choose an option: ") #For take an user input



    if choice == "1":
        food = input("Enter your favourite food name: ")
        favorite_foods.append(food)
        print(f" {food} Food added Successful")

    elif choice == "2":
        food = input("Enter food name that you want to remove: ")
        favorite_foods.remove(food)
        print(f" {food} Food removed Successful")

    elif choice == "3":
        if favorite_foods:
            print("Your favourite foods are: ")
            for index, food in enumerate(favorite_foods, start=1):
                print(f" {index}.{food}")

    elif choice == '4':

        print("Goodbye!")

        break

    else:

        print("Invalid choice.")






