# James Hernandez | jwg455 | 11/27/2020

# this program converts a number to a Roman Numeral
# should accept one or more parameters via sys.argv(1:)
# must use a function to do the conversion
# for roman.py, define a function that takes a number and returns the string
# can take any number <= 0 or > 3,999, if it is an invalid number return "Error"
# assume input is a number NOT a string
# roman.py 812 43 ----->  "812 is DCCCXII" and "43 is XLIII"
# roman.py 49 5000 ---->  "49 is XLIX" and "5000 is Error"

     # example: 
            # 3840 // 3000 or thousands[3]
            # quotient = 1, remainder = 840
            # 840 // 800 or hundreds[8]
            # quotient = 1, remainder = 40
            # 40 // 40 or tens[4]
            # quotient = 1, reminder = 0 

import sys

ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
thousands = ["", "M", "MM", "MMM"]
lists = [ones, tens, hundreds, thousands]

def intToRoman(x):
    #converts string argument into integer
    xStr = int(x)
   
    try:
        # finds the ith value in thousands place by using integer divide
        a = thousands[xStr // 1000]
    # gathers the remainder of xStr / 1000 , divides it by 100 and finds the ith value in hundreds
        b = hundreds[(xStr % 1000) // 100]
    # gathers the remainder of xStr / 100, divides it by 10 and finds the ith value in tens
        c = tens[(xStr % 100) // 10]
    # finds the ith value in ones place by using integer divide
        d = ones[xStr % 10]
    # concatenates strings   
        finalStr = (a + b + c + d)
    except IndexError:
        finalStr = 'Error'

    # prints string
    return finalStr



# reads arguments from cmd line
arguments = sys.argv[1:]
# loops through arguments and turns integers into roman numerals
for x in arguments:
    print (x, 'is', intToRoman(x))

    



