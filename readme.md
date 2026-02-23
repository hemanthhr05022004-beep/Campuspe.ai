=====================================================

**Question 1**

 **Student Bio Card Program**

========================================================

\# Variables

name = "Hemanth H R"

age = 22

course = "Python Programming"

college = "Atria Institute of Technology"

email = "hemanthhr12@example.com"



\# Card Width

card\_width = 50



\# Top Border

print("=" \* card\_width)

print("|" + "STUDENT BIO CARD".center(card\_width - 2) + "|")

print("=" \* card\_width)



\# Information Section

print("|" + f" Name    : {name}".ljust(card\_width - 2) + "|")

print("|" + f" Age     : {age} years".ljust(card\_width - 2) + "|")

print("|" + f" Course  : {course}".ljust(card\_width - 2) + "|")

print("|" + f" College : {college}".ljust(card\_width - 2) + "|")

print("|" + f" Email   : {email}".ljust(card\_width - 2) + "|")



\# Bottom Border

print("=" \* card\_width)







Variables                                                                                                      

• name

• age

• course

• college

• email



Formatted Output

• print () : to display text on the screen

• f"" (f-string) : to insert variable values inside the string

• {variable:<25} : (25 characters wide)



Box Design

• ╔ ╗ ╚ ╝ → corners

• ═ → horizontal line

• ║ → vertical border







Output:

|                STUDENT BIO CARD                |

==================================================

| Name    : Hemanth H R                          |

| Age     : 22 years                             |

| Course  : Python Programming                   |

| College : Atria Institute of Technology        |

| Email   : hemanthhr12@example.com              |

==================================================



=================================================================

**Question 2**

**simple calculator**

=================================================================

\# Taking input from user

num1 = float(input("Enter first number: "))

num2 = float(input("Enter second number: "))



\# Performing calculations

addition = num1 + num2

subtraction = num1 - num2

multiplication = num1 \* num2

division = num1 / num2

modulus = num1 % num2

exponentiation = num1 \*\* num2



\# Displaying results

print("\\nResults:")

print(f"{num1} + {num2} = {addition}")

print(f"{num1} - {num2} = {subtraction}")

print(f"{num1} \* {num2} = {multiplication}")

print(f"{num1} / {num2} = {round(division, 2)}")

print(f"{num1} % {num2} = {modulus}")

print(f"{num1} ^ {num2} = {exponentiation}")



Operations

• +: Addition

• -: Subtraction

• \*: Multiplication

• /: Division

• %: Modulus

• \*\*: Exponentiation 



Expected output:

Enter first number: 2

Enter second number: 5



Results:

2.0 + 5.0 = 7.0

2.0 - 5.0 = -3.0

2.0 \* 5.0 = 10.0

2.0 / 5.0 = 0.4

2.0 % 5.0 = 2.0

2.0 ^ 5.0 = 32.0



==============================================

**Question 3**

**string manipulator**

===============================================

\# Taking input from user

sentence = input("Enter a sentence: ")



\# Calculations

original = sentence

characters\_with\_spaces = len(sentence)

characters\_without\_spaces = len(sentence.replace(" ", ""))

words\_list = sentence.split()

total\_words = len(words\_list)

uppercase = sentence.upper()

lowercase = sentence.lower()

title\_case = sentence.title()

first\_word = words\_list\[0] if total\_words > 0 else ""

last\_word = words\_list\[-1] if total\_words > 0 else ""

reversed\_sentence = sentence\[::-1]



\# Display results

print("\\nResults:")

print("Original:", original)

print("Characters (with spaces):", characters\_with\_spaces)

print("Characters (without spaces):", characters\_without\_spaces)

print("Words:", total\_words)

print("UPPERCASE:", uppercase)

print("lowercase:", lowercase)

print("Title Case:", title\_case)

print("First word:", first\_word)

print("Last word:", last\_word)

print("Reversed:", reversed\_sentence)



conditions:

* upper(): Converts to UPPERCASE
* lower(): Converts to lowercase
* title(): Converts to Title Case
* input() takes a full sentence from the user and stores it in the variable sentence.
* len() counts all characters including spaces.
* split() breaks the sentence into a list of words.
* len() counts the number of words.



Expected output:

Enter a sentence: i am python



Results:

Original: i am python

Characters (with spaces): 11

Characters (without spaces): 9

Words: 3

UPPERCASE: I AM PYTHON

lowercase: i am python

Title Case: I Am Python

First word: i

Last word: python

Reversed: nohtyp ma I



==================================================

**Question 4**

**age calculator**

==================================================

\# Age Calculator  



from datetime import datetime



\# Get current year

current\_year = datetime.now().year



\# Taking input

birth\_year = int(input("Enter your birth year: "))



\# Calculations

age = current\_year - birth\_year

months = age \* 12

days = age \* 365

hours = days \* 24

minutes = hours \* 60

years\_to\_100 = 100 - age



\# Display results

print("\\nResults:")

print("Current Age:", age)

print("Age in Months:", months)

print("Age in Days (approx):", days)

print("Age in Hours:", hours)

print("Age in Minutes:", minutes)

print("Years until 100:", years\_to\_100)



Current Date

• current\_date = datetime.now()



Basic Age Formula

• age = current\_year - birth\_year



&nbsp;Time Calculations

• Months : age \* 12

• Days : age \* 365

• Hours : days \* 24

• Minutes : hours \* 60





Expected output:

Enter a sentence: birth year

Enter your birth year: 2005



Results:

Current Age: 21

Age in Months: 252

Age in Days (approx): 7665

Age in Hours: 183960

Age in Minutes: 11037600

Years until 100: 79



========================================================

**Question 5**

**bill splitter**

=========================================================

\# Taking inputs

total\_bill = float(input("Enter total bill: "))

people = int(input("Number of people: "))

tax\_percent = float(input("Tax percentage: "))

tip\_percent = float(input("Tip percentage: "))



\# Calculations

subtotal = total\_bill

tax\_amount = subtotal \* (tax\_percent / 100)

after\_tax = subtotal + tax\_amount

tip\_amount = after\_tax \* (tip\_percent / 100)

final\_total = after\_tax + tip\_amount

per\_person = final\_total / people



\# Displaying formatted output

print("\\n=== BILL BREAKDOWN ===")

print(f"Subtotal:    ₹{subtotal:.2f}")

print(f"Tax ({tax\_percent}%):   ₹{tax\_amount:.2f}")

print(f"After tax:   ₹{after\_tax:.2f}")

print(f"Tip ({tip\_percent}%):   ₹{tip\_amount:.2f}")

print(f"Total:       ₹{final\_total:.2f}")

print(f"Per person:  ₹{per\_person:.2f}")





Taking  Input

* total\_bill = float(input("Enter total bill: "))



Calculating Tax

* tax\_amount = subtotal \* (tax\_percent / 100)



Calculating Tip

* tip\_amount = after\_tax \* (tip\_percent / 100)



Total

* final\_total = after\_tax + tip\_amount



Output

* ₹{amount:2f}





Expected output: 



Enter total bill: 51

Number of people: 2

Tax percentage: 1

Tip percentage: 2.5



=== BILL BREAKDOWN ===

Subtotal:    ₹51.00

Tax (1.0%):   ₹0.51

After tax:   ₹51.51

Tip (2.5%):   ₹1.29

Total:       ₹52.80

Per person:  ₹26.40



==================================================

**Question 6**

**grade calculator**

=====================================================

\# Taking input for 5 subjects

sub1 = float(input("Enter marks for Subject 1: "))

sub2 = float(input("Enter marks for Subject 2: "))

sub3 = float(input("Enter marks for Subject 3: "))

sub4 = float(input("Enter marks for Subject 4: "))

sub5 = float(input("Enter marks for Subject 5: "))



total = sub1 + sub2 + sub3 + sub4 + sub5

percentage = (total / 500) \* 100



\# Grade

if percentage >= 90:

&nbsp;   grade = "A+ (Outstanding)"

elif percentage >= 80:

&nbsp;   grade = "A (Excellent)"

elif percentage >= 70:

&nbsp;   grade = "B (Good)"

elif percentage >= 60:

&nbsp;   grade = "C (Average)"

elif percentage >= 50:

&nbsp;   grade = "D (Pass)"

else:

&nbsp;   grade = "F (Fail)"



\# Pass/Fail condition  

if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and sub4 >= 40 and sub5 >= 40:

&nbsp;   result = "Pass"

else:

&nbsp;   result = "Fail"



\# Displaying Results

print("\\n=== MARKS REPORT ===")

print("Subject 1:", sub1)

print("Subject 2:", sub2)

print("Subject 3:", sub3)

print("Subject 4:", sub4)

print("Subject 5:", sub5)

print("Total Marks (out of 500):", total)

print("Percentage: {:.2f}%".format(percentage))

print("Grade:", grade)

print("Result:", result)



Taking Input

* sub1 = float(input("Enter marks for Subject 1: "))

same as the 5 subjects 



Total calculation

* total = sub1 + sub2 + sub3 + sub4 + sub5



Percentage calculation

percentage = (total / 500) \* 100



Grade Calculation

* 90–100 =  A+
* 80–89 = A
* 70–79 = B
* 60–69 = C
* 50–59 = D
* Below 50 = F





Expected output:

Enter marks for Subject 1: 85

Enter marks for Subject 2: 35

Enter marks for Subject 3: 45

Enter marks for Subject 4: 95

Enter marks for Subject 5: 100



=== MARKS REPORT ===

Subject 1: 85.0

Subject 2: 35.0

Subject 3: 45.0

Subject 4: 95.0

Subject 5: 100.0

Total Marks (out of 500): 360.0

Percentage: 72.00%

Grade: B (Good)

Result: Fail



=================================================

**Question 7**

**temperature converter**

=====================================================

while True:

&nbsp;   print("\\n=== TEMPERATURE CONVERTER ===")

&nbsp;   print("1. Celsius to Fahrenheit")

&nbsp;   print("2. Fahrenheit to Celsius")

&nbsp;   print("3. Celsius to Kelvin")

&nbsp;   print("4. Kelvin to Celsius")

&nbsp;   print("5. Fahrenheit to Kelvin")

&nbsp;   print("6. Kelvin to Fahrenheit")

&nbsp;   print("7. Exit")



&nbsp;   choice = int(input("Enter your choice (1-7): "))



&nbsp;   if choice == 7:

&nbsp;       print("Exiting program... Goodbye!")

&nbsp;       break



&nbsp;   temp = float(input("Enter temperature value: "))



&nbsp;   if choice == 1:

&nbsp;       result = (temp \* 9/5) + 32

&nbsp;       print(f"{temp}°C = {result:.2f}°F")



&nbsp;   elif choice == 2:

&nbsp;       result = (temp - 32) \* 5/9

&nbsp;       print(f"{temp}°F = {result:.2f}°C")



&nbsp;   elif choice == 3:

&nbsp;       result = temp + 273.15

&nbsp;       print(f"{temp}°C = {result:.2f}K")



&nbsp;   elif choice == 4:

&nbsp;       result = temp - 273.15

&nbsp;       print(f"{temp}K = {result:.2f}°C")



&nbsp;   elif choice == 5:

&nbsp;       result = (temp - 32) \* 5/9 + 273.15

&nbsp;       print(f"{temp}°F = {result:.2f}K")



&nbsp;   elif choice == 6:

&nbsp;       result = (temp - 273.15) \* 9/5 + 32

&nbsp;       print(f"{temp}K = {result:.2f}°F")



&nbsp;   else:

&nbsp;       print("Invalid choice! Please select between 1 and 7.")



conditions:

* while True:

&nbsp;	Keeps the program running until the user chooses exit 7.

&nbsp;	break stops the loop.



* Temperature Input

&nbsp;	temp = float(input("Enter temperature value: "))

&nbsp;	float() allows decimal temperature values.

* Conversion Formulas Used

Conversion	Formula Used

C → F	     (C × 9/5) + 32

F → C	     (F - 32) × 5/9

C → K	      C + 273.15

K → C	      K - 273.15

F → K	     (F - 32) × 5/9 + 273.15

K → F	     (K - 273.15) × 9/5 + 32



Expected output:

=== TEMPERATURE CONVERTER ===

1\. Celsius to Fahrenheit

2\. Fahrenheit to Celsius

3\. Celsius to Kelvin

4\. Kelvin to Celsius

5\. Fahrenheit to Kelvin

6\. Kelvin to Fahrenheit

7\. Exit

Enter your choice (1-7): 3

Enter temperature value: 26

26.0°C = 299.15K



=== TEMPERATURE CONVERTER ===

1\. Celsius to Fahrenheit

2\. Fahrenheit to Celsius

3\. Celsius to Kelvin

4\. Kelvin to Celsius

5\. Fahrenheit to Kelvin

6\. Kelvin to Fahrenheit

7\. Exit

Enter your choice (1-7):





==================================================

**Question 8**

**leap year checker**

======================================================



\# Taking input

year = int(input("Enter a year: "))



\# Checking leap year condition

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):

&nbsp;   print(f"\\n{year} is a Leap Year.")

&nbsp;   

&nbsp;   # Explaining reason

&nbsp;   if year % 400 == 0:

&nbsp;       print("Reason: Divisible by 400 (special century rule).")

&nbsp;   elif year % 100 == 0:

&nbsp;       print("Reason: Divisible by 100 but not by 400 (Not leap rule).")

&nbsp;   else:

&nbsp;       print("Reason: Divisible by 4 and not divisible by 100.")

else:

&nbsp;   print(f"\\n{year} is NOT a Leap Year.")

&nbsp;   

&nbsp;   # Explaining reason

&nbsp;   if year % 4 != 0:

&nbsp;       print("Reason: Not divisible by 4.")

&nbsp;   elif year % 100 == 0 and year % 400 != 0:

&nbsp;       print("Reason: Divisible by 100 but not divisible by 400.")



* Taking Input

&nbsp;	year = int(input("Enter a year: "))

&nbsp;       int() : converts input to an integer.



* Leap Year Rule

&nbsp;	Divisible by 4 and not divisible by 100



Expected output:

1.Enter a year: 2029

2029 is NOT a Leap Year.

Reason: Not divisible by 4.



2.Enter a year: 2024

2024 is a Leap Year.

Reason: Divisible by 4 and not divisible by 100.



==========================================================

**Question 9**

**ticket pricing system**

=========================================================

\# pricing system  



\# Taking inputs

age = int(input("Enter age: "))

day = input("Enter day of the week: ").strip().lower()

tickets = int(input("Enter number of tickets: "))



\# Determine base price based on age

if age < 3:

&nbsp;   base\_price = 0

&nbsp;   category = "Free"

elif 3 <= age <= 12:

&nbsp;   base\_price = 150

&nbsp;   category = "Child"

elif 13 <= age <= 59:

&nbsp;   base\_price = 300

&nbsp;   category = "Adult"

else:

&nbsp;   base\_price = 200

&nbsp;   category = "Senior"



\# Calculate subtotal

subtotal = base\_price \* tickets



\# Determine discount

if day in \["friday", "saturday", "sunday"]:

&nbsp;   discount = subtotal \* 0.20   # 20% discount

else:

&nbsp;   discount = 0



\# Final price after discount

final\_amount = subtotal - discount



\# Display results

print("\\n=== MOVIE TICKET BILL ===")

print("Category:", category)

print(f"Base price per ticket: ₹{base\_price:.2f}")

print(f"Subtotal: ₹{subtotal:.2f}")



if discount > 0:

&nbsp;   print(f"Weekend Discount (20%): -₹{discount:.2f}")

else:

&nbsp;   print("No Discount Applied")



print(f"Total Amount: ₹{final\_amount:.2f}")



conditions:

* subtotal = base\_price \* tickets (Multiple ticket price by number of tickets)
* final\_amount = subtotal - discount

Discount

* Friday–Sunday → 20% discount
* Monday–Thursday → No discount





Expected output:

Enter age: 25

Enter day of the week: monday

Enter number of tickets: 5



=== MOVIE TICKET BILL ===

Category: Adult

Base price per ticket: ₹300.00

Subtotal: ₹1500.00

No Discount Applied

Total Amount: ₹1500.00



==============================================================

**Question 10**

**simple ATM simulator**

===========================================================

balance = 10000 # Initial balance

MIN\_BALANCE = 500



while True:

print("\\n=== ATM SIMULATOR ===")

print("1. Check Balance")

print("2. Deposit")

print("3. Withdraw")

print("4. Exit")



choice = int(input("Enter choice: "))



if choice == 1:

print(f"Current Balance: ₹{balance:.2f}")



elif choice == 2:

amount = float(input("Enter amount to deposit: "))

if amount > 0:

balance += amount

print("Deposit successful!")

print(f"New balance: ₹{balance:.2f}")

else:

print("Invalid deposit amount!")



elif choice == 3:

amount = float(input("Enter amount to withdraw: "))

if amount <= 0:

print("Invalid withdrawal amount!")

elif amount > balance:

print("Insufficient balance!")

elif balance - amount < MIN\_BALANCE:

print(f"Minimum balance of ₹{MIN\_BALANCE} must be maintained!")

else:

balance -= amount

print("Withdrawal successful!")

print(f"New balance: ₹{balance:.2f}")



elif choice == 4:

print("Thank you for using the ATM. Goodbye!")

break



else:

print("Invalid choice! Please select 1-4.")



conditions:

* initial balance

&nbsp;    Account starts with ₹10,000.

&nbsp;    ₹500 must always remain in account.

* menu loop

&nbsp;    Keeps ATM running until user chooses Exit.

&nbsp;    break stops the loop.

* deposit money

&nbsp;    Adds money to balance.

&nbsp;    Checks that deposit amount is positive.



Expected output:

=== ATM SIMULATOR ===

1\. Check Balance

2\. Deposit

3\. Withdraw

4\. Exit

Enter choice: 2

Enter amount to deposit: 200

Deposit successful!

New balance: ₹10200.00



=== ATM SIMULATOR ===

1\. Check Balance

2\. Deposit

3\. Withdraw

4\. Exit

Enter choice:



=====================================================

**Question 11**

**number pattern printer**

=======================================================

\# Pattern Printing Program



while True:

&nbsp;   print("\\n=== PATTERN MENU ===")

&nbsp;   print("1. Pattern 1")

&nbsp;   print("2. Pattern 2")

&nbsp;   print("3. Pattern 3")

&nbsp;   print("4. Pattern 4")

&nbsp;   print("5. Exit")



&nbsp;   choice = int(input("Enter your choice: "))



&nbsp;   if choice == 5:

&nbsp;       print("Exiting program...")

&nbsp;       break



&nbsp;   height = int(input("Enter height: "))



&nbsp;   print("\\nOutput:\\n")



&nbsp;   # Pattern 1

&nbsp;   if choice == 1:

&nbsp;       for i in range(1, height + 1):

&nbsp;           for j in range(1, i + 1):

&nbsp;               print(j, end=" ")

&nbsp;           print()



&nbsp;   # Pattern 2

&nbsp;   elif choice == 2:

&nbsp;       for i in range(1, height + 1):

&nbsp;           for j in range(i):

&nbsp;               print(i, end=" ")

&nbsp;           print()



&nbsp;   # Pattern 3

&nbsp;   elif choice == 3:

&nbsp;       for i in range(height, 0, -1):

&nbsp;           for j in range(i, 0, -1):

&nbsp;               print(j, end=" ")

&nbsp;           print()



&nbsp;   # Pattern 4

&nbsp;   elif choice == 4:

&nbsp;       for i in range(1, height + 1):

&nbsp;           # Increasing part

&nbsp;           for j in range(1, i + 1):

&nbsp;               print(j, end="")

&nbsp;           # Decreasing part

&nbsp;           for j in range(i - 1, 0, -1):

&nbsp;               print(j, end="")

&nbsp;           print()



&nbsp;   else:

&nbsp;       print("Invalid choice! Please select 1-5.")



conditions:



* infinite loop

&nbsp;  Creates an infinite loop

&nbsp;  Keeps showing the menu until user chooses Exit

&nbsp;  Stops only when break is executed



* taking inputs

&nbsp;  input() → Takes input from user

&nbsp;  int() → Converts string input into integer



&nbsp;

Expected output:

=== PATTERN MENU ===

1\. Pattern 1

2\. Pattern 2

3\. Pattern 3

4\. Pattern 4

5\. Exit

Enter your choice: 2

Enter height: 4



Output:



1 

2 2 

3 3 3 

4 4 4 4 



=== PATTERN MENU ===

1\. Pattern 1

2\. Pattern 2

3\. Pattern 3

4\. Pattern 4

5\. Exit

Enter your choice:



=================================================

**Question 12**

**multiplication table generator**

===================================================

\# Multiplication Table Program



\# Taking input from user

number = int(input("Enter number: "))

range\_end = int(input("Enter range (end): "))



print("\\nMultiplication Table of", number)



\# Loop to generate table

for i in range(1, range\_end + 1):

&nbsp;   result = number \* i

&nbsp;   print(number, "x", i, "=", result)



conditions:

* Prints numbers 1 to 10 across the top.
* Outer loop → rows
* Inner loop → columns
* i \* j prints multiplication result.
* Ensures equal spacing (grid alignment).
* Makes table neat and professional.





Expected Output

FULL MULTIPLICATION TABLE (1-10) ===



&nbsp;      1   2   3   4   5   6   7   8   9  10

--------------------------------------------------

&nbsp;1 |   1   2   3   4   5   6   7   8   9  10

&nbsp;2 |   2   4   6   8  10  12  14  16  18  20

&nbsp;3 |   3   6   9  12  15  18  21  24  27  30

&nbsp;4 |   4   8  12  16  20  24  28  32  36  40

&nbsp;5 |   5  10  15  20  25  30  35  40  45  50

&nbsp;6 |   6  12  18  24  30  36  42  48  54  60

&nbsp;7 |   7  14  21  28  35  42  49  56  63  70

&nbsp;8 |   8  16  24  32  40  48  56  64  72  80

&nbsp;9 |   9  18  27  36  45  54  63  72  81  90

10 |  10  20  30  40  50  60  70  80  90 100



=====================================================

**Question 13**

**sum and average calculator**

==========================================================

count = int(input("How many numbers? "))



\# Initialize variables

total = 0

numbers = \[]



\# Loop to take inputs

for i in range(1, count + 1):

&nbsp;   num = int(input(f"Enter number {i}: "))

&nbsp;   numbers.append(num)

&nbsp;   total += num



\# Calculations

average = total / count

maximum = max(numbers)

minimum = min(numbers)



\# Display results

print("\\nResults:")

print("Sum:", total)

print("Average:", average)

print("Maximum:", maximum)

print("Minimum:", minimum)



conditions:



* User decides how many numbers they want to enter.
* total stores the sum of all numbers.
* Starts from 2 because first number is already taken.
* Adds each number to total.
* Compares for maximum and minimum.
* average = total / count





Expected output:

How many numbers? 5

Enter number 1: 2

Enter number 2: 1

Enter number 3: 4

Enter number 4: 0

Enter number 5: 3



Results:

Sum: 10.0

Average: 2.0

Maximum: 4.0

Minimum: 0.0



=======================================================

**Question 14**

**factorial calculator**

=========================================================

num = int(input("Enter a number: "))



\# negative numbers

if num < 0:

print("Factorial is not defined for negative numbers.")



\# Handle 0

elif num == 0:

print("0! = 1")

print("Factorial of 0 is 1")



\# Positive numbers

else:

factorial = 1

steps = ""



for i in range(num, 0, -1):

factorial \*= i

steps += str(i)

if i != 1:

steps += " × "



print(f"\\n{num}! = {steps} = {factorial}")



conditions:

* User enters the number for factorial. 
* Factorial is not defined for negative numbers. 



Loop

* Starts from num
* Goes down to 1
* Multiplies each value
* Builds a step-by-step multiplication string



Expected output:

Enter a number: 10



10! = 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 3628800





=========================================================

**Question 15**

**prime number checker**

===========================================================

\# Prime Number Program

\# **part 1**

num = int(input("Enter a number: "))



if num < 2:

&nbsp;   print(num, "is NOT a prime number")



elif num == 2:

&nbsp;   print("2 is a PRIME number")



else:

&nbsp;   is\_prime = True



&nbsp;   for i in range(2, int(num \*\* 0.5) + 1):

&nbsp;       if num % i == 0:

&nbsp;           is\_prime = False

&nbsp;           break



&nbsp;   if is\_prime:

&nbsp;       print(num, "is a PRIME number")

&nbsp;   else:

&nbsp;       print(num, "is NOT a prime number")





\# **part 2**

num = int(input("Enter a number: "))

start = int(input("\\nEnter start range: "))

end = int(input("Enter end range: "))



print("Prime numbers:", end=" ")



for number in range(start, end + 1):



&nbsp;   if number >= 2:

&nbsp;       prime = True



&nbsp;       for i in range(2, int(number \*\* 0.5) + 1):

&nbsp;           if number % i == 0:

&nbsp;               prime = False

&nbsp;               break



&nbsp;       if prime:

&nbsp;           print(number, end=", ")





used by:

* if-elif-else
* for loop
* range()
* break
* Square root optimization (num \*\* 0.5)
* Proper edge case handling
* prime number is greater than 1 and only two factors 1 and itself.



expected output:

Enter a number: 10

10 is NOT a prime number



Enter a number: 17

17 is a PRIME number



Enter start range: 1

Enter end range: 30

Prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29



=====================================================

**Question 16**

**number guessing game**

========================================================

import random



print("===== NUMBER GUESSING GAME =====")



while True:

&nbsp;   # Computer selects random number

&nbsp;   secret\_number = random.randint(1, 100)

&nbsp;   attempts\_left = 7

&nbsp;   total\_attempts = 7

&nbsp;   guessed = False



&nbsp;   print("\\nI have selected a number between 1 and 100.")

&nbsp;   print("You have 7 attempts to guess the number.")



&nbsp;   # Loop for attempts

&nbsp;   while attempts\_left > 0:

&nbsp;       guess = int(input("\\nEnter your guess: "))



&nbsp;       if guess == secret\_number:

&nbsp;           attempts\_used = total\_attempts - attempts\_left + 1

&nbsp;           print("Congratulations! You guessed the correct number.")

&nbsp;           print("Attempts used:", attempts\_used)

&nbsp;           guessed = True

&nbsp;           break



&nbsp;       elif guess < secret\_number:

&nbsp;           attempts\_left -= 1

&nbsp;           print("Too low!")

&nbsp;           print("Attempts remaining:", attempts\_left)



&nbsp;       else:

&nbsp;           attempts\_left -= 1

&nbsp;           print("Too high!")

&nbsp;           print("Attempts remaining:", attempts\_left)



&nbsp;   # If user fails after 7 attempts

&nbsp;   if not guessed:

&nbsp;       print("\\nYou failed to guess the number.")

&nbsp;       print("The correct number was:", secret\_number)



&nbsp;   # Ask to play again

&nbsp;   choice = input("\\nDo you want to play again? (yes/no): ").lower()



&nbsp;   if choice != "yes":

&nbsp;       print("Thank you for playing!")

&nbsp;       break





used that operations for:

* import random
* random.randint(1, 100)
* while loop for replay
* while loop for attempts
* if-elif-else conditions
* Attempts remaining display
* Attempts used display
* Reveal number if failed
* Play again option





===== NUMBER GUESSING GAME =====



I have selected a number between 1 and 100.

You have 7 attempts to guess the number.



Enter your guess: 20

Too high!

Attempts remaining: 6



Enter your guess: 0

Too low!

Attempts remaining: 5



Enter your guess: 1

Too low!

Attempts remaining: 4



Enter your guess: 5

Too low!

Attempts remaining: 3







==================================================

**Question 17**

**palindrome checker**

====================================================



\# Taking input from user

user\_input = input("Enter word/number: ")



\# Step 1: Store original value

original = user\_input



\# Step 2: Convert to lowercase for case-insensitive comparison

processed = user\_input.lower()



\# Step 3: Reverse the string

reversed\_value = processed\[::-1]



\# Display step-by-step verification

print("\\nOriginal:", original)

print("Reversed:", original\[::-1])   # Showing visual reverse

print("Processed (lowercase):", processed)

print("Reversed (lowercase):", reversed\_value)



\# Step 4: Check palindrome

if processed == reversed\_value:

&nbsp;   print("Result: PALINDROME")

else:

&nbsp;   print("Result: NOT A PALINDROME")





Expected output:

Enter word/number: words



Original: words

Reversed: sdrow

Processed (lowercase): words

Reversed (lowercase): sdrow

Result: NOT A PALINDROME



================================================

**Question 18**

**calculator functions**

=====================================================

\# 1. Addition

def add(a, b):

&nbsp;   return a + b



\# 2. Subtraction

def subtract(a, b):

&nbsp;   return a - b



\# 3. Multiplication

def multiply(a, b):

&nbsp;   return a \* b



\# 4. Division (handle division by zero)

def divide(a, b):

&nbsp;   if b == 0:

&nbsp;       return "Error! Division by zero is not allowed."

&nbsp;   return a / b



\# 5. Modulus

def modulus(a, b):

&nbsp;   return a % b



\# 6. Power

def power(a, b):

&nbsp;   return a \*\* b



\# 7. Main Calculator Function

def calculator():

&nbsp;   while True:

&nbsp;       print("\\n===== CALCULATOR MENU =====")

&nbsp;       print("1. Add")

&nbsp;       print("2. Subtract")

&nbsp;       print("3. Multiply")

&nbsp;       print("4. Divide")

&nbsp;       print("5. Modulus")

&nbsp;       print("6. Power")

&nbsp;       print("7. Exit")



&nbsp;       choice = input("Enter your choice (1-7): ")



&nbsp;       if choice == "7":

&nbsp;           print("Exiting Calculator. Thank you!")

&nbsp;           break



&nbsp;       if choice in \["1", "2", "3", "4", "5", "6"]:

&nbsp;           num1 = float(input("Enter first number: "))

&nbsp;           num2 = float(input("Enter second number: "))



&nbsp;           if choice == "1":

&nbsp;               print("Result:", add(num1, num2))



&nbsp;           elif choice == "2":

&nbsp;               print("Result:", subtract(num1, num2))



&nbsp;           elif choice == "3":

&nbsp;               print("Result:", multiply(num1, num2))



&nbsp;           elif choice == "4":

&nbsp;               print("Result:", divide(num1, num2))



&nbsp;           elif choice == "5":

&nbsp;               print("Result:", modulus(num1, num2))



&nbsp;           elif choice == "6":

&nbsp;               print("Result:", power(num1, num2))



&nbsp;       else:

&nbsp;           print("Invalid choice! Please select between 1 and 7.")



\# Run the calculator

calculator()







Expected output:

===== CALCULATOR MENU =====

1\. Add

2\. Subtract

3\. Multiply

4\. Divide

5\. Modulus

6\. Power

7\. Exit

Enter your choice (1-7): 4

Enter first number: 10

Enter second number: 2

Result: 5.0



===== CALCULATOR MENU =====

1\. Add

2\. Subtract

3\. Multiply

4\. Divide

5\. Modulus

6\. Power

7\. Exit

Enter your choice (1-7):



================================================

**Question 19**

**text analysis function**

======================================================

\# 1. Count Words

def count\_words(text):

&nbsp;   words = text.split()

&nbsp;   return len(words)



\# 2. Count Vowels

def count\_vowels(text):

&nbsp;   vowels = "aeiouAEIOU"

&nbsp;   count = 0

&nbsp;   for char in text:

&nbsp;       if char in vowels:

&nbsp;           count += 1

&nbsp;   return count



\# 3. Count Consonants

def count\_consonants(text):

&nbsp;   vowels = "aeiouAEIOU"

&nbsp;   count = 0

&nbsp;   for char in text:

&nbsp;       if char.isalpha() and char not in vowels:

&nbsp;           count += 1

&nbsp;   return count



\# 4. Reverse Text

def reverse\_text(text):

&nbsp;   return text\[::-1]



\# 5. Check Palindrome

def is\_palindrome(text):

&nbsp;   processed = text.replace(" ", "").lower()

&nbsp;   return processed == processed\[::-1]



\# 6. Remove Vowels

def remove\_vowels(text):

&nbsp;   vowels = "aeiouAEIOU"

&nbsp;   result = ""

&nbsp;   for char in text:

&nbsp;       if char not in vowels:

&nbsp;           result += char

&nbsp;   return result



\# 7. Word Frequency

def word\_frequency(text):

&nbsp;   words = text.lower().split()

&nbsp;   frequency = {}

&nbsp;   for word in words:

&nbsp;       frequency\[word] = frequency.get(word, 0) + 1

&nbsp;   return frequency



\# 8. Longest Word

def longest\_word(text):

&nbsp;   words = text.split()

&nbsp;   longest = ""

&nbsp;   for word in words:

&nbsp;       if len(word) > len(longest):

&nbsp;           longest = word

&nbsp;   return longest



\# 9. Analyze Text (Main Function)

def analyze\_text(text):

&nbsp;   print("\\n=== TEXT ANALYSIS ===")

&nbsp;   print("Words:", count\_words(text))

&nbsp;   print("Vowels:", count\_vowels(text))

&nbsp;   print("Consonants:", count\_consonants(text))

&nbsp;   print("Reversed:", reverse\_text(text))

&nbsp;   print("Palindrome:", "Yes" if is\_palindrome(text) else "No")

&nbsp;   print("Without vowels:", remove\_vowels(text))



&nbsp;   longest = longest\_word(text)

&nbsp;   print("Longest word:", longest, f"({len(longest)} letters)")



&nbsp;   freq = word\_frequency(text)

&nbsp;   print("Word Frequency:", end=" ")

&nbsp;   for word, count in freq.items():

&nbsp;       print(f"{word}: {count}", end=", ")

&nbsp;   print()



\# Program Execution

text\_input = input("Enter text: ")

analyze\_text(text\_input)





==========================================================



**Question 20**

**number system function**

=============================================================



\# 1. Factorial

def factorial(n):

&nbsp;   if n < 0:

&nbsp;       return "Factorial not defined for negative numbers"

&nbsp;   result = 1

&nbsp;   for i in range(1, n + 1):

&nbsp;       result \*= i

&nbsp;   return result





\# 2. Check Prime

def is\_prime(n):

&nbsp;   if n < 2:

&nbsp;       return False

&nbsp;   for i in range(2, int(n \*\* 0.5) + 1):

&nbsp;       if n % i == 0:

&nbsp;           return False

&nbsp;   return True





\# 3. Fibonacci (nth term)

def fibonacci(n):

&nbsp;   if n <= 0:

&nbsp;       return "Invalid input"

&nbsp;   elif n == 1:

&nbsp;       return 0

&nbsp;   elif n == 2:

&nbsp;       return 1

&nbsp;   a, b = 0, 1

&nbsp;   for \_ in range(3, n + 1):

&nbsp;       a, b = b, a + b

&nbsp;   return b





\# 4. Sum of Digits

def sum\_of\_digits(n):

&nbsp;   return sum(int(digit) for digit in str(abs(n)))





\# 5. Reverse Number

def reverse\_number(n):

&nbsp;   sign = -1 if n < 0 else 1

&nbsp;   reversed\_num = int(str(abs(n))\[::-1])

&nbsp;   return sign \* reversed\_num





\# 6. Armstrong Number

def is\_armstrong(n):

&nbsp;   num\_str = str(abs(n))

&nbsp;   power = len(num\_str)

&nbsp;   total = sum(int(digit) \*\* power for digit in num\_str)

&nbsp;   return total == abs(n)





\# 7. GCD (Euclidean Algorithm)

def gcd(a, b):

&nbsp;   while b != 0:

&nbsp;       a, b = b, a % b

&nbsp;   return abs(a)





\# 8. LCM

def lcm(a, b):

&nbsp;   return abs(a \* b) // gcd(a, b)





\# 9. Perfect Number

def is\_perfect\_number(n):

&nbsp;   if n <= 0:

&nbsp;       return False

&nbsp;   total = 0

&nbsp;   for i in range(1, n):

&nbsp;       if n % i == 0:

&nbsp;           total += i

&nbsp;   return total == n





\# 10. Menu Function

def math\_menu():

&nbsp;   while True:

&nbsp;       print("\\n===== NUMBER SYSTEM MENU =====")

&nbsp;       print("1. Factorial")

&nbsp;       print("2. Check Prime")

&nbsp;       print("3. Fibonacci")

&nbsp;       print("4. Sum of Digits")

&nbsp;       print("5. Reverse Number")

&nbsp;       print("6. Armstrong Number")

&nbsp;       print("7. GCD")

&nbsp;       print("8. LCM")

&nbsp;       print("9. Perfect Number")

&nbsp;       print("10. Exit")



&nbsp;       choice = input("Enter your choice (1-10): ")



&nbsp;       if choice == "10":

&nbsp;           print("Exiting Program. Thank you!")

&nbsp;           break



&nbsp;       elif choice == "1":

&nbsp;           n = int(input("Enter number: "))

&nbsp;           print("Factorial:", factorial(n))



&nbsp;       elif choice == "2":

&nbsp;           n = int(input("Enter number: "))

&nbsp;           print("Prime:" , "Yes" if is\_prime(n) else "No")



&nbsp;       elif choice == "3":

&nbsp;           n = int(input("Enter position (n): "))

&nbsp;           print("Fibonacci:", fibonacci(n))



&nbsp;       elif choice == "4":

&nbsp;           n = int(input("Enter number: "))

&nbsp;           print("Sum of digits:", sum\_of\_digits(n))



&nbsp;       elif choice == "5":

&nbsp;           n = int(input("Enter number: "))

&nbsp;           print("Reversed number:", reverse\_number(n))



&nbsp;       elif choice == "6":

&nbsp;           n = int(input("Enter number: "))

&nbsp;           print("Armstrong:", "Yes" if is\_armstrong(n) else "No")



&nbsp;       elif choice == "7":

&nbsp;           a = int(input("Enter first number: "))

&nbsp;           b = int(input("Enter second number: "))

&nbsp;           print("GCD:", gcd(a, b))



&nbsp;       elif choice == "8":

&nbsp;           a = int(input("Enter first number: "))

&nbsp;           b = int(input("Enter second number: "))

&nbsp;           print("LCM:", lcm(a, b))



&nbsp;       elif choice == "9":

&nbsp;           n = int(input("Enter number: "))

&nbsp;           print("Perfect Number:", "Yes" if is\_perfect\_number(n) else "No")



&nbsp;       else:

&nbsp;           print("Invalid choice! Please select between 1 and 10.")





\# Run the menu

math\_menu()









==================================================

&nbsp;             README

===================================================

Name: Hemanth HR

Course: Python Basics Assignment – Modules 1 to 6

Total Questions Attempted: 20



Program Description:

This assignment covers basic Python concepts including:

* Variables
* Data types
* Operators
* Conditional statements
* Loops
* Functions



Special Instructions:

All programs were tested with multiple inputs.



Challenges Faced:

* Handling division by zero.
* Managing edge cases in prime number logic.
* Formatting output neatly.
* Avoiding errors like division by zero in LCM and other operations.
* Managing loops properly.
* Implementing multiple functions and calling them correctly.



Declaration:

I confirm that this assignment is my own work.

























































