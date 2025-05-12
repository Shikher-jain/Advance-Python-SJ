alpha=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digit=[0,1, 2, 3, 4, 5, 6, 7, 8, 9]


num="Alphanumeric, also referred to as alphameric, is a term that encompasses all of the letters and numerals in a given language set. In layouts designed for English language users, alphanumeric characters are those comprised of the combined set of the 26 alphabetic characters, A to Z, and the 10 Arabic numerals, 0 to 9."

print(num)
for n in range(10):
    num=num.replace(str(digit[n]),alpha[n])
print(num)