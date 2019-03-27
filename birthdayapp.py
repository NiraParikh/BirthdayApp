dict = {}  # dictionary data type to have key:value pair

while True:
    print("-------B'Day App ---------")
    print("1.Show Birthday ")
    print("2.Add to Birthday List ")
    print("3.Exit ")

    choice = int(input("Enter the choice "))  # int casting as the options are string
    if choice == 1:                          # therefore need to convert input to int in above code
        if len(dict.keys()) == 0:
            print("Nothing to show")
        else:
            name=input("Enter the name to look up the B'Day ")
            birthday=dict.get(name, 'No Data Found')
            print(birthday)
    elif choice ==2:
        name = input("Enter Friend's name ")
        date = input("Enter BirthDate ")
        dict[name]= date
        print("Birthday Added")
    elif choice ==3:
        break
    else:
        print("Choose a valid option")
