
 
data = [] 
 
print("Welcome to the Data Analyzer and Transformer Program") 
 
while True: 
 
    print("\nMain Menu:") 
    print("1. Input Data") 
    print("2. Display Data Summary") 
    print("3. Calculate Factorial") 
    print("4. Filter Data") 
    print("5. Sort Data") 
    print("6. Display Statistics") 
    print("7. Exit Program") 
 
    choice = input("\nPlease enter your choice: ") 
 
    # 1. Input Data 
    if choice == "1": 
 
        values = input("Enter data separated by spaces: ") 
        data = list(map(int, values.split())) 
 
        print("Data has been stored successfully!") 
 
    # 2. Built-in Functions 
    elif choice == "2": 
 
        if len(data) == 0: 
            print("Please enter data first!") 
        else: 
            print("\nData Summary:") 
            print("Total elements:", len(data)) 
            print("Minimum value:", min(data)) 
            print("Maximum value:", max(data)) 
            print("Sum:", sum(data)) 
            print("Average:", sum(data) / len(data)) 
 
    # 3. Recursion - Factorial 
    elif choice == "3": 
 
        n = int(input("Enter a number: ")) 
 
        def factorial(n): 
            if n == 0 or n == 1: 
                return 1 
            return n * factorial(n - 1) 
 
        print("Factorial:", factorial(n)) 
 
    # 4. Lambda Function 
    elif choice == "4": 
 
        if len(data) == 0: 
            print("Please enter data first!") 
        else: 
            number = int(input("Enter threshold: ")) 
 
            result = list(filter(lambda x: x >= number, data)) 
 
            print("Filtered Data:", result) 
 
    # 5. Sorting 
    elif choice == "5": 
 
        if len(data) == 0: 
            print("Please enter data first!") 
        else: 
            print("1. Ascending") 
            print("2. Descending") 
 
            ch = input("Enter choice: ") 
 
            if ch == "1": 
                print("Sorted Data:", sorted(data)) 
 
            elif ch == "2": 
                print("Sorted Data:", sorted(data, reverse=True)) 
 
            else: 
                print("Invalid choice!") 
 
    # 6. Return Multiple Values 
    elif choice == "6": 
 
        if len(data) == 0: 
            print("Please enter data first!") 
        else: 
 
            def statistics(numbers): 
                minimum = min(numbers) 
                maximum = max(numbers) 
                total = sum(numbers) 
                average = total / len(numbers) 
 
                return minimum, maximum, total, average 
 
            a, b, c, d = statistics(data) 
 
            print("\nDataset Statistics:") 
            print("Minimum:", a) 
            print("Maximum:", b) 
            print("Sum:", c) 
            print("Average:", d) 
 
    # 7. Exit 
    elif choice == "7": 
 
        print("Thank you! Goodbye!") 
        break 
 
    else: 
        print("Invalid choice!")