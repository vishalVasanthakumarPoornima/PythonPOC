def word_count(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        count = text.split()
        return len(count)
    
file_path = input("Please enter the path to the file: ")
print(word_count(file_path))
