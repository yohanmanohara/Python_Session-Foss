def is_vowel(letter):
    vowels = "aeiouAEIOU"
    return letter in vowels

def check_vowels_in_file(filename):
        with open(filename, 'r') as file:
            content = file.read().strip().split(',')
            result = {letter: is_vowel(letter) for letter in content}
            return result


filename = 'D:/project_files/Python_Session-Foss/File_Handling/letter.txt'
vowel_results = check_vowels_in_file(filename)
for letter, is_vowel_result in vowel_results.items():
    print(f"Letter '{letter}' is a vowel: {is_vowel_result}")
