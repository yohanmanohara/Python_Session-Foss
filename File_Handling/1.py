def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Content written to '{filename}' successfully.")

# Function to append content to a file
def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)
    print(f"Content appended to '{filename}' successfully.")




filename = 'D:/project_files/Python_Session-Foss/File_Handling/notes.txt'

New_content = "New Content."
write_to_file(filename, New_content)


read_file(filename)

Append_Content = "\nThis is appended content."
append_to_file(filename,Append_Content)

read_file(filename)
