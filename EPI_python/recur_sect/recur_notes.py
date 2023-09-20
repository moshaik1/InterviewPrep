
"""
a series of helper function that calls itself. A helper function calls another helper function,
etc, until the last helper function performs standalone logic without calling another
helper function. When the latest helper function is complete, it goes to the previous helper
and completes it. Continues to unravel until the first helper function is complete

need a break condition to stop the loop, or it will be an infinite loop

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

behaves like a recursive call stack:
- initial call is the bottom most frame
- each recursion adds another frame to the stack
- once last frame is reached, the top frame gets popped (base case)
- continues until 1st frame is reached, resulting in empty stack
- call stack: Last In First Out behavior
"""