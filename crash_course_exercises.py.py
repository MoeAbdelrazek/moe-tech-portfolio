# tasks = []

# while True:

#     print(f"1-  Add a task")
#     print(f"2-  View tasks")
#     print(f"3-  Save tasks to file")
#     print(f"4-  Exit")

#     choice = input("please enter your choice [1 - 4]: ")

#     try:
#         choice  not in ValueError

#         if choice == "1":
#             Task = input(" Please add a new task: ")
#             print(tasks.append(Task))

#         elif choice == 2:
#             for i, task in enumerate(tasks, start = 1):
#                 print(f"{i}. {task}")

#         elif choice == 3:
#             with open("tasks.txt", "w") as file:
#                 file.write(f"{tasks}")

#         elif  choice == 4:
#             print(f"Goodbye")
#             break
           
    
#     except:
#         choice in ValueError
#         print("Please enter a valid option!")



    

#=========================================== Ask the user for their name and age, then print a greeting:

# Example run:

# Enter your name: Alice
# Enter your age: 25
# Hello Alice, you are 25 years old!

# name = input("What's your name? ")
# age = input("How old are you? ")
# print(f"Hello {name}, you are {age} years old")

#  ===================✅ Exercise 2 (Variables + Conditionals + Loops)

# Write a program that asks the user for a number n.

# If n is greater than 10, print "Too big!".

# If n is less than 1, print "Too small!".

# Otherwise, use a for loop to print all numbers from 1 up to n.

# n = int(input("Please enter a number: "))

# if n > 10:
#     print(f"Too big!")

# elif n < 1:
#     print(f"Too small!")

# else:
#     for n in range(1, n+1):
#         print(n)



# ================== Exercise 3 (Functions + Conditionals + Loops):
# Write a function is_even(n) that:

# Returns "Even" if the number is even

# Returns "Odd" if the number is odd

# Then, ask the user for a number m, and use a loop to print whether each number from 1 to m is even or odd.

# def is_even(n):

#     if n % 2 == 0:
#         return "Even"

#     else:
#         return "Odd"
    
# m = int(input("Please enter a number: "))

# for m in range(1, m+1):
#     if m % 2 == 0:
#         print(f"{m} is Even")

#     else:
#         print(f"{m} is Odd")


#==========================       Exercise 4 (Strings + Loops + Conditionals):
#Ask the user for a word. Print each letter on a new line, but if the letter is a vowel (a, e, i, o, u), print it in uppercase.

# word = input("Please enter a word: ")

# for letter in word:
#     if letter in ("ioueaIOEUA"):
#         print(f"{letter.upper()}")

#     else:
#         print(f"{letter}")


#=================    Exercise 5 (Lists + Loops + Conditionals + Functions)
# Write a function filter_positive(numbers) that takes a list of numbers and returns a new list containing only the positive numbers.

# Then:

# Ask the user to enter 5 numbers (store them in a list).

# Call the function to filter positives.

# Print the resulting list.

# def filter_positive(numbers):
#     positive_numbers = []

#     for number in numbers:
#         if number > 0:
            
#             positive_numbers.append(number)

#     return(positive_numbers)

# new_numbers = []

# for n in range(5):

#     user_input = input("Enter 5 numbers: ")
#     number = int(user_input)
#     new_numbers.append(number)

# print(new_numbers)
# print(filter_positive(new_numbers))     
        

# ----======================---Exercise 6 (Dictionaries + Loops + Conditionals): --------------------------
# Create a dictionary of 3 countries and their capitals.

# Ask the user to enter a country name.

# If the country is in the dictionary, print the capital.

# If not, print "Sorry, I don't know that country."


# capitals = {
#     "Egypt": "Cairo",
#     "France": "Paris",
#     "Italy": "Rome",
# }
# country = input("Please enter your country: ")

# capital = capitals.get(country)

# if capital:
        
#         print(f"The capital of {country} is {capital}")

# else:
#         print(f"Sorry, I don't know that country.")
    


# -------------------- Exercise 7 (Lists + Loops + Strings + Conditionals) ----------------
# Ask the user to enter 5 words (store them in a list).

# Then loop through the list and print only the words that are longer than 3 letters, in uppercase.


# words = []

# for i in range (5):
#     user_input = input("Please enter 5 words: ")

#     words.append(user_input)

# for word in words:
#     if len(word) > 3:
#         print(word.upper())


# ----------==== Exercise 8 (Functions + Loops + Lists + Conditionals) =====-----------
# Write a function count_vowels(word) that counts how many vowels (a, e, i, o, u) are in a word.

# Ask the user to enter 3 words.

# For each word, print the word and the number of vowels it contains.



# def count_vowels(word):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for letter in word:
#         if letter in vowels:
#             count += 1
#     return count
# new_words = []
# for i in range(3):
#     user_input = input("please enter 3 words: ")
#     new_words.append(user_input)

# count_vowels(new_words)

# for word in new_words:
#     print(f"{word}: {count_vowels(word)}")




# === ------------------- Exercise 9 (Loops + Conditionals + Numbers + Lists) --------------- ========
# Ask the user to enter 5 numbers.

# Store them in a list.

# Print the largest number and the smallest number from the list.

# numbers = []
# for i in range(5):
#     user_input = int(input("Please enter a number: "))
#     numbers.append(user_input)

# print(f"Largest number: {max(numbers)}")
# print(f"Smallest number: {min(numbers)}")




#  ----------------- ================       Exercise 10 (Functions + Lists + Loops + Conditionals) -------- ============
# Write a function average(numbers) that takes a list of numbers and returns their average.

# Ask the user for 5 numbers.

# Print the list and the average.


# def average(numbers):

#     return sum(numbers) / len(numbers)

# items = []

# for i in range(5):

#         user_input = int((input("Please enter a number: ")))

#         items.append(user_input)

# print("Numbers entered:", items)
# print("Average:" , average(items))




# ==================----------⚡ Exercise 11 (Strings + Conditionals + Loops + Functions) -------*******============

# Write a function is_palindrome(word) that checks if a word is a palindrome (the same forwards and backwards, like madam or level).

# Ask the user for 3 words.

# For each word, print whether it is or is not a palindrome.


# def is_palindrome(word):
#     word = word.lower()
#     return word == word[::-1]

# words = []

# for i in range(3):

#     user_input = input("Please enter a word: ")
#     words.append(user_input)

# for w in words:
#     if is_palindrome(w):
#         print(f"{w} is a palindrome")
#     else:
#         print(f"{w} is not a palindrome")

    

# ------------------=============Exercise 12 (Lists + Dictionaries + Loops)  --------------------********

# Create a dictionary of 3 fruits and their prices (e.g., "apple": 2, "banana": 1, "cherry": 3).

# Ask the user to enter the name of a fruit.

# If it’s in the dictionary, print the price.

# If not, print "Sorry, that fruit is not available." 


# prices = {
#     "apple": 2,
#     "banana": 1,
#     "cherry": 3,
# }

# fruit = input("Enter the name of a fruit: ")
# price = prices.get(fruit)

# if price:

#     print(f"{fruit}: {price}")
# else:
#     print("sorry, that fruit is not available")




# ---- ***** ===========Exercise 13 (Loops + Conditionals + Lists + Strings) --------------- *************** ====

# Ask the user for a sentence.

# Split the sentence into words.

# Print each word on a new line, but if the word is longer than 5 letters, print it in uppercase.


# sentence = input("Enter a sentence: ")

# words = sentence.split()

# for word in words:

#     if len(word) > 5:
#         print(word.upper())

#     else:
#         print(word)



# ---------*************** Exercise 14 (Loops + Lists + Conditionals + Functions) ******** ---------------------

# Write a function only_even(numbers) that takes a list of numbers and returns a new list with only the even ones.

# Ask the user for 6 numbers.

# Print both the original list and the filtered list.


def only_even(numbers):

    even_numbers= []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

        else:
            continue

    return even_numbers

new_numbers = []

for i in range(6):

    user_input = int(input("Enter a number: "))
    new_numbers.append(user_input)

print(new_numbers)
print(only_even(new_numbers))



# --------******** Exercise 15 (Strings + Loops + Conditionals) --------********======= 

# Ask the user for a word.

# Count how many consonants it has (letters that are not vowels).

# Print the result.


# word = input("Enter a word: ")

# vowels = "aeiouAEIOU"
# count = 0

# for letter in word:
#     if letter.isalpha() and letter not in vowels: 
#         count += 1

# print(f"The word '{word}' has {count} consonants.")




#********* --------------------Exercise 16 (Lists + Functions + Logic) ------- ****************==========

# Write a function longest_word(words) that:

# Takes a list of words

# Returns the longest word in that list

# def longest_word(words):
#     longest = ""

#     for word in words:
#         if len(word) > len(longest):
#             longest = word
#     return longest                        # word_list = []
#                                         # result = longest_word(word_list)
#                                         #print(result)




# Function to filter only even numbers from a list
def only_even(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

# Collect 6 numbers from the user
new_numbers = []
for i in range(6):
    user_input = int(input("Enter a number: "))
    new_numbers.append(user_input)

# Display the original list and the filtered even numbers
print("All numbers entered:", new_numbers)
print("Even numbers:", only_even(new_numbers))