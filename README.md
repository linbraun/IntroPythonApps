# Python App Samples
### IT 140 | October 2020
Python projects: ATM, grocery list, pattern search, rental car billing

### ATM
Knowing how and when to use and modify custom functions can really cut down on lines of code and make your program run as efficiently as possible. Having the option to use custom functions gives the programmer the control to make code as personalized to each task as possible, this also allows the opportunity to add new functions and modify current functions without having to make changes to each occurrence in the script. Knowing how and when to use parameters will save on time and space as well. Adding the proper parameters to each function will allow the function to pull information from an existing variable outside of the function. If this value changes, as it often does, putting it in the parameters will make sure it is current. A common use for parameters would be in functions that perform calculations based on previous input, like calculating the tax on an item or collecting a grand total, these tasks will require parameters to communicate outside of the function and retrieve the numbers they will be calculating on. Having functions return the correct output is extremely important, it allows for work done inside the function to be used in the rest of the code, which is often the most important part of a function’s job. Returning the output of a function allows for continued usage with that (now modified) variable. The ATM script uses all three of these features to define a specific function for each task, send the necessary parameters, and return that output to the display. I did not encounter many errors in making this script besides for some regular syntax errors. When fixing syntax errors, I check the line the error occurred on and fix what was missing or out of place. When revising the code for my final project, I added more descriptive comments to guide the viewer through the script and explain the tasks being executed.

### Grocery List
Final Project Script Two exemplified the importance of knowing how and when to use lists, dictionaries, and loop types. Using a dictionary to hold the name, quantity, and cost of an item made for an organized and easy way to store all of an item’s information in one place. Putting these dictionaries in a list made it easy to refer to and calculate a total from. Loops in this script allowed for multiple items to be inputted and the grand total to be calculated. I happened upon a few index errors while writing this script and after many failed attempts at fixing it, I decided to consult a tutor through SNHU. The index error was because I was calling on an index that did not exist. This was fixed by swapping the order of conditions and checking that I was using the correct variables.

### Pattern Search
Knowing how and when to use a search allows for the most proficient usage of regular expressions and the opportunity for more compact and concise coding. Searching using literal characters can help you quickly identify if they can be found in what you are searching, this can help you verify information or return the location where a pattern is matched. Searching for sequences and ranges can help you find a pattern or the number of times a pattern occurs. By using the len() method with the findall regular expression, I was able to find how many misspellings of sit amet were in the lorem_ipsum string and then verify that all occurrences were fixed by searching once again. Searching for special characters and wildcards can help you identify when or where they occur, or do not occur, in a script. In my project, I was able to search for special characters and wildcards by searching for everything but letters and numbers, this returned all non-alphanumeric characters in the string I was searching. I did not encounter many errors in making this script besides for some basic syntax errors. When fixing syntax errors, I checked the line the error had occurred on and fixed what was missing or out of place. 

### Rental Car Billing
Knowing how and when to use and modify variables is a crucial part of programming. Variables give context to what you code, they hold value while the rest of the code instructs what to do with that value. Modifying this value can be very useful as well, you may use it as a counter or a placeholder for current user input. Branches give priority to tasks and make sure the right code is being executed for each particular task. You may only want a line of code to execute when a certain value is reached, putting this line within a branch assures that the program will not hit a dead end and crash if that value was not reached. Branches also allow for blocks of code to be looped in a particular order and once certain arguments are met. I did not encounter any major errors during this assignment. General syntax errors were corrected by reviewing the line the error occurred on. Errors regarding mixed variable types were corrected by using a formatting method like str() or int().

