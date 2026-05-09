## Bug 1 – bug1.cpp
**Intended Behavior**: The program should concatenate two strings and print "hesablayici isleyir" upon completion.
**Issue Type**: Syntax Error and Type Mismatch.
**Notes**: Missing semicolons and attempting to store string results in an integer variable.

## Bug 2 – bug2.py
**Intended Behavior**: The script should calculate a user's future age and find the average price of items in a list.
**Issue Type**: Runtime Exception.
**Notes**: Crashes due to string/integer concatenation and potential division by zero with empty lists.

## Bug 3 – bug3.js
**Intended Behavior**: The function should find a user by ID in an array and return the user's name.
**Issue Type**: Logical and Reference Error.
**Notes**: Uses assignment instead of comparison in the if-statement and lacks null-checking for the result.

## Bug 4 – bug4.c
**Intended Behavior**: The program should print all elements of a 5-element array and perform a division operation.
**Issue Type**: Buffer Overflow and Division by Zero.
**Notes**: The loop index exceeds array limits and the division operation uses a zero denominator.
