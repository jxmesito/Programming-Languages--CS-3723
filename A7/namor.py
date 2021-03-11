# this program converts a Roman Numeral to a number
# should accept one or more parameters via sys.argv(1:)
# must use a function to do the conversion
# For namor.py, the function takes a string and returns a number
# Given a Roman Numeral String, parse it and return the number.
# If it does not match a legal number from above (in the range 1 to 3,999), return -1. (20 points)
import sys

thousands = {"MMM": 3000, "MM": 2000, "M": 1000}
hundreds = {"CM": 900, "DCCC": 800, "DCC": 700, "DC": 600, "D": 500, "CD": 400, "CCC": 300, "CC":200, "C": 100, "": 0}
tens = {"XC": 90, "LXXX": 80, "LXX": 70, "LX": 60, "L": 50, "XL": 40, "XXX": 30, "XX": 20, "X": 10, "": 0}
ones = {"IX": 9, "VIII": 8, "VII": 7, "VI": 6, "V": 5, "IV": 4, "III": 3, "II": 2, "I": 1, "": 0}

integers = (thousands, hundreds, tens, ones)

def romanToInt(romanNumeral):  
    # create variable to return
    totalNum = 0
    # loop through integer tuples
    for dict in integers:
    # loop through items within tuples
        for item in dict.items():
    # if the number starts with the current key
            if romanNumeral.startswith(item[0]):
    # add to running total
                totalNum += item[1]
    # remove the added number and exit the loop
                romanNumeral = romanNumeral[len(item[0]):]
                break
    
    # check to see if number is fully trimmed and done looping
    # if not return -1
    if len(romanNumeral) != 0:
        totalNum = -1
    return totalNum 
        
    
arguments = sys.argv[1:]
for x in arguments:
    print(x.upper(), "is", romanToInt(x.upper()))
