data = []
# 1. Input Data
def input_data():
    """
    Take input from the user and store it in a 1D array.
    This function allows the user to enter multiple integer
    values separated by spaces. The input values are converted
    into integers and stored in the global data list.
    The function updates the existing data and displays a
    success message after storing the values.
    Parameters:
        None
    Returns:
        None
    Example:
        Input: 10 20 30 40 50
        Output:
            Data has been stored successfully!
    """
    global data
    values = input("Enter data for a 1D array (separated by spaces): ")
    data = [int(x) for x in values.split()]
    print("Data has been stored successfully!")
#2. Display Summary
def display_summary():
    """
    Display a summary of the stored dataset.
    This function checks whether the data list contains
    any elements. If data is available, it calculates and
    displays the total number of elements, maximum value,
    minimum value, sum of all values and average value.
    If the data list is empty, the function displays a
    message indicating that no data is available.
    Parameters:
        None
    Returns:
        None
    Example:
        Input Data: [10, 20, 30, 40, 50]
        Output:
            Total Elements: 5
            Maximum value: 50
            Minimum value: 10
            Sum of all values: 150
            Average value: 30.0
    """
    if data:
        print(" Data Summary:")
        print("- Total Elements:", len(data))
        print("- Maximum value:", max(data))
        print("- Minimum value:", min(data))
        print("- Sum of all values:", sum(data))
        print("- Average value:", sum(data)/len(data))
    else:
        print("No data available.")
#3.Factorial Calculation (Recursion)
def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    This function calculates the factorial of a non-negative
    integer. Factorial is the product of all positive integers
    from 1 to the given number.
    The function uses recursion, where it calls itself with
    a smaller value until it reaches the base case.
    The base case occurs when n is 0 or 1, because the
    factorial of both values is 1.
    Negative numbers are not supported because their
    factorial is not defined in this context.
    Parameters:
        n (int): The number whose factorial is calculated.
    Returns:
        int: The factorial of the given number.
        str: An error message if the number is negative.
    Examples:
        factorial(5) returns 120
        factorial(0) returns 1
        factorial(1) returns 1
        factorial(-2) returns an error message.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
# 4. Filter Data by Threshold (Lambda Function)
def filter_data():
    """
    Filter dataset values based on a threshold using lambda.
    This function asks the user to enter a threshold value.
    It filters the elements from the data list that are
    greater than the given threshold.
    The filter() function is used with a lambda function
    to check each element in the dataset.
    If the dataset is empty, the function displays a
    message indicating that no data is available.
    Parameters:
        None
    Returns:
        None
    Example:
        Input Data: [10, 20, 30, 40, 50]
        Threshold: 25
        Output:
            Filtered data: [30, 40, 50]
    """
    if data:
        threshold = int(input("Enter a threshold value to Filter out data above this value: "))
        filtered = list(filter(lambda x: x > threshold, data))
        print("Filtered data:", filtered)
    else:
        print("NO data Available!")
#5. sorting data 
def sort_data():
    """
    Sort the dataset in ascending or descending order.
    This function asks the user to select a sorting order.
    The user can choose between ascending order and
    descending order.
    The sorted() function is used to arrange the elements
    of the data list. The reverse=True argument is used
    for descending order.
    The function uses a while loop to repeatedly ask for
    a valid choice if the user enters an invalid option.
    Parameters:
        None
    Returns:
        None
    Examples:
        Input Data: [40, 10, 30, 20]
        Choice: 1
        Output:
            Sorted data in Ascending order: [10, 20, 30, 40]
        Choice: 2
        Output:
            Sorted data in Descending order: [40, 30, 20, 10]
    """
    ch = input("choose sorting order (1/2): ")
    print("1. Ascending")
    print("2. Descending")
    while True:
        if ch == '1':
            sorted_data = sorted(data)
            print("\nSorted data in Ascending order:", sorted_data)
            print(*sorted_data, sep=", ")
            break
        elif ch == '2':
            sorted_data = sorted(data, reverse=True)
            print("\nSorted data in Descending order:", sorted_data)
            print(*sorted_data, sep=", ")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
            ch = input("choose sorting order (1/2): ")
# 6. Dataset Statistics
def dataset_statistics(data):
    """
    Calculate basic statistical values for a dataset.
    This function calculates the minimum value, maximum
    value, total sum and average of the elements in the
    given dataset.
    The built-in Python functions min(), max() and sum()
    are used to calculate the required statistical values.
    The average is calculated by dividing the total sum
    by the number of elements in the dataset.
    Parameters:
        data (list): A list containing numerical values.
    Returns:
        tuple: A tuple containing four values:
            - minimum: The smallest value in the dataset.
            - maximum: The largest value in the dataset.
            - total: The sum of all elements.
            - average: The average of all elements.
    Example:
        Input:
            data = [10, 20, 30, 40, 50]
        Output:
            (10, 50, 150, 30.0)
    """
    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = total / len(data)
    return minimum, maximum, total, average
while True:
    print("\nWelcome to the  data Analyzer  and transformer program")
    print("Main menu:")
    print("1. Input Data")
    print("2. Display Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data")
    print("5. Sort Data")
    print("6. Dataset Statistics")
    print("7. Exit")
    choice = input("Please select an option (1-7):")
    match choice:
        case '1':
            input_data()
        case '2':
            display_summary()
        case '3':
            num = int(input("Enter a number to calculate its factorial: "))
            print("Factorial of", num, "is:", factorial(num))
        case '4':
            filter_data()
        case '5':
            sort_data()
        case '6':
            if data:
                minimum, maximum, total, average = dataset_statistics(data)
                print("\nDataset Statistics:")
                print("- Minimum value:", minimum)
                print("- Maximum value:", maximum)
                print("- Sum of all values:", total)
                print(f"- Average value: {average:.2f}")
            else:
                print("No data available to calculate statistics.")
        case '7':
            print("Thank you for using the data Analyzer and transformer program. Goodbye!")
            break
        case _:
            print("Invalid choice please select a valid option (1-7).")