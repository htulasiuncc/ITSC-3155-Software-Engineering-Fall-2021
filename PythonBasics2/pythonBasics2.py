# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
  # YOUR CODE HERE

  #returns n divided by 3 typecast as int
  #return int(n/3)


  #sets the integer n to a list of string characers
  n = list(str(n))

  #declares the direcotry
  dictionary = {}

  #populates the dictionary with the three multiples of 3 and sets them equal to zero
  dictionary[3] = 0
  dictionary[6] = 0
  dictionary[9] = 0

  #for loop to count the number of multiples of 3
  for i in n:
    number = int(i)
    #if loop to test if the the number in question is divisible by 3, with no remainder, and isn't 0
    if number % 3 == 0 and number != 0:
      #increments the dictionary number to the next digit
      dictionary[number] = dictionary[number] + 1

  #initializes the max value and index to -1
  #-1 indicates the last number in a sequence so this will count from
  #the last value left off on during iteration
  maxValue = -1
  index = -1
  #for loop to test the current and next values in a dictionary to see if the next value is the last value
  for current, next in dictionary.items():
    #if condition to test if the next value is greater than the max value to continue or not
    if next > maxValue:
      #sets the next value to the max value and sets the current value to the index
      maxValue = next
      index = current

  # and returning the number finally
  return index

# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.

def longest_consecutive_repeating_char(s):
  # YOUR CODE HERE

  #declares a variable for stringLength and sets it equal to the length of string s
  #stringLength = len(s)
  #initializes a count variable to be used to count the characters of the string
  #count = 0
  #initializes a maximum variable used to stop the count of a string
  #when a maximum amount of repeating letters is reached
  #maximum = 0
  #initializes a variable as the first, or 0 in the array,
  #character of the string s which is an array of characters
  #character = s[0]
  #a for loop with the parameters of the first character in the string
  #and the last character, denoted by the length of the string -1
  #for i in range(0, stringLength - 1):
    #if statement to compare the current letter of the string to the next letter
    #if s[i] == s[i + 1]:
      #if the condition above is met, the loop will continue counting the consecutive letters
      #count += 1
    #else:
      #if the count of repeating characters exceeds the maximum number of repeating characters
      #the maximum will be set to that count and the character will be set to the one where
      #the repetition ends on the string or i.
      #the count is then set to 1
      #if count > maximum:
        #maximum = count
        #character = s[i]
      #count = 1
  #condition to account for if there is no repeating letters present so count can return to 0
  #and the character can be reset to the last place in the array i
  #if count > maximum:
    #maximum = count
    #character = s[i]
  #return character

  #declaring variables for the string to be read as a list of characters,
  #the string length initialized to the length of string s,
  #and a count variable set to 1,
  #a dictionary to hold letters to be counted
  s = list(s)
  stringLength = len(s)
  count = 1
  dictionary = {}

  #for loop to check check if each letter is the same as last and else the count is reset to 1 for that letter
  for i in range(0, stringLength - 1):
    if (s[i] != s[i + 1]):
      if ((s[i] in dictionary) and dictionary[s[i]] > count):
        continue
      else:
        dictionary[s[i]] = count
        count = 1
    else:
      count = count + 1
  #updates dictionary as the string with the last longest lenght is set to the count
  dictionary[s[stringLength - 1]] = count

  #sets max value to -1 to denote the last number recorded
  maxValue = -1
  #for loop to find the maximum value of how many times a letter was repeated
  for listSoFar, lastValue in dictionary.items():
    if lastValue > maxValue:
      maxValue = lastValue

  #declares a dictionary to store the list of each letter's frequency
  frequencyList = []
  #for loop to keep a count of the max frequency of each letter that has the highest frequency
  # since there are multiple in this test
  for listSoFar, lastValue in dictionary.items():
    if lastValue == maxValue:
      #appends the list with new values added to the list so far
      frequencyList.append(listSoFar)

  return frequencyList

# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  # YOUR CODE HERE

  # intialize the first letter from the left as 0 or the first character
  letterFromLeft = 0
  # initialize the first letter from the right as the length of the string minus 1
  letterFromRight = len(s) - 1

  # while loop where the letter on the left is less than or equal to the one on the right
  # this ensures that the letters don't cross over
  while letterFromLeft <= letterFromRight:
    # if statement setting the letter from the left equal to a blank space to skip
    # then the letter will move one to the right or add one character count
    # this accounts for any spaces between words or letters that shouldn't
    # be considered in a palindrome
    if s[letterFromLeft] == ' ':
      letterFromLeft += 1

    # if statement setting the letter from the right equal to a blank space to skip
    # then the letter will move one to the left or subtract one character count
    # this accounts for any spaces between words or letters that shouldn't
    # be considered in a palindrome
    if s[letterFromRight] == ' ':
      letterFromRight -= 1

    # if statement comparing the letter from the left to the letter from the right
    # if they both aren't equal then the statement would return false
    # the letters are both set to lowercase so that they can be compared
    if s[letterFromLeft].lower() != s[letterFromRight].lower():
      return False

    # calls to keep the letters from the left to be analyzed toward the right
    # or increasing the increment
    letterFromLeft += 1
    # calls to keep the letters from the right to be analyzed toward the left
    # or decreasing the increment
    letterFromRight -= 1

  return True