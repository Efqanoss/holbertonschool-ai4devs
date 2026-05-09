## Bug 1 – bug1.cpp
**Intended Behavior**: The application is intended to perform basic string operations. It should take two string variables, concatenate them to form a single output, and simulate a result for a multiplication-like logic. The program must compile successfully and conclude by printing a status message ("hesablayici isleyir") to the standard output to confirm the routine completed without interruption.
**Issue Type**: Syntax Error, Type Mismatch, and Undeclared Identifiers.
**Notes**: 
* **Syntax**: Multiple missing semicolons (`;`) after variable declarations (`string a, b`) and arithmetic operations violate C++ grammar rules.
* **Static Typing Violation**: Attempting to assign the result of string concatenation (a `std::string` type) to an integer variable `c` causes a compilation failure.
* **Invalid Operator**: Multiplication (`*`) is not a defined operator for `std::string` objects in the standard library.
* **Undeclared Variable**: The standalone `x` at the end of the `main` function is not declared in the scope and lacks a terminating semicolon.

## Bug 2 – bug2.py
**Intended Behavior**: This script serves as a data processing utility for user profiles. It is designed to calculate a user's age for the upcoming year and compute the arithmetic mean of prices for a list of items. It should be robust enough to handle empty lists by returning a default average and skip over items that have missing (`None`) price values without crashing.
**Issue Type**: Runtime Exception (TypeError, ZeroDivisionError, AttributeError).
**Notes**: 
* **Strong Typing Conflict**: Python does not allow implicit concatenation of `str` and `int`. The expression `"text" + (age + 1)` triggers a `TypeError`.
* **Unhandled Nulls**: Iterating through `my_items` where a price is `None` leads to a crash when trying to add `None` to the `total_price` integer.
* **Mathematical Edge Case**: The script does not check if the `items` list is empty before calling `len(items)`, which leads to a `ZeroDivisionError` during the average calculation.

## Bug 3 – bug3.js
**Intended Behavior**: The function `findUserById` is designed to search through a database-like array of user objects. Its goal is to locate a specific user by their unique ID and return the corresponding name. If the ID is found, the search should stop immediately for efficiency. If the ID does not exist in the array, it should return a null value or an appropriate message without attempting to access properties of an undefined object.
**Issue Type**: Logical Error, Reference Error, and Memory Leak.
**Notes**: 
* **Global Scope Pollution**: The variable `i` in the `for` loop is not declared with `let` or `var`, causing it to be treated as a global variable.
* **Assignment Trap**: The condition `if (user.id = id)` uses the assignment operator instead of the strict equality operator (`===`). This overwrites the user ID with the target ID, making the condition always true.
* **Null Pointer Dereference**: If a search yields no results, `foundUser` remains `null`. Accessing `foundUser.name` outside the loop then triggers a runtime error.
* **Inefficiency**: The lack of a `break` statement ensures the loop continues to run even after the target user is identified.

## Bug 4 – bug4.c
**Intended Behavior**: The program is meant to initialize an integer array of size 5 and safely iterate through it to display each element's value. Afterward, it should perform a division of two predefined integers and exit cleanly. The loop logic must strictly respect the memory boundaries allocated for the array.
**Issue Type**: Buffer Overflow and Floating Point Exception (SIGFPE).
**Notes**: 
* **Memory Corruption (Out-of-Bounds)**: The loop condition `i <= 10` forces the program to read memory far beyond the 5 elements allocated for `numbers[5]`. This is a classic buffer overflow scenario that leads to undefined behavior.
* **Arithmetic Crash**: Dividing an integer by zero (`x / y` where `y = 0`) is undefined in C and causes the operating system to terminate the process with a "Division by zero" or "Floating point exception" error.