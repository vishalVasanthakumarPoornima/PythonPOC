res = input("Please enter your string for validation: ")
val = True
if res[2] != '*':
    print("The 2nd char is not a *")
    val = False
if res[3].isupper() == False:
    print("The 3rd char is not an uppercase char.")
    val = False
if res[(len(res)-1)-5].isalpha() == False:
    print("The 5th character from the end is not an alphabet.") 
    val = False
if len(res) > 14:
    print("The string is too long.")
    val = False
try:
    if type(int(res[(len(res)-1)-3: len(res)])) != int:
        print("The last 4 chars are not numbers.")
        val = False
except ValueError:
    print("The last 4 chars are not numbers.")
    val = False

if val:
    print("Success.")
