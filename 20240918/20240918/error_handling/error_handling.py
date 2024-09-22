try:
    # Code that might raise an exception
    try:
        first=int(input('Enter the no : '))
  
    except Exception as ex:
        print('the error is : ',ex)    
    

    result=first/second
    print(result)
except ZeroDivisionError:
    # Handle the exception
    print("You cannot divide by zero!")
else:
    # Executes if no exception occurs
    print("Division successful.")
finally:
    # Always executes
    print("Execution complete.")


