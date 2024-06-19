user_file = input("Enter the path to the file: ")
word = input("Enter the word to be replaced: ")
replaceWord = input("Enter the replace word: ")
# Open and read the file
try:
    with open(user_file, 'r') as file:
        content = file.read()
        new_content = content.replace(word, replaceWord)
    with open(user_file, 'w') as file:
        file.write(new_content)
    print("The word has been replaced successfully.")
except FileNotFoundError:
    print("File not found. Please check the path and try again.")
except Exception as e:
    print(f"An error occurred: {e}")
