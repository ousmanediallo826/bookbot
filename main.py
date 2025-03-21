import sys

def count_words(text):
    """Counts the total number of words in the given text."""
    return len(text.split())

def count_letters(text):
    """Counts the frequency of each letter in the given text."""
    letter_counts = {}
    for char in text.lower():
        if char.isalpha(): 
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts

def print_report(book_path):
    """Reads a file, counts words and letters, and prints a report."""
    try:
        with open(book_path, 'r', encoding='utf-8') as file:
            text = file.read()

        word_count = count_words(text)
        letter_counts = count_letters(text)

        print(f"--- Book Report for {book_path} ---")
        print(f"Total words: {word_count}\n")

   
        sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

    
        for letter, count in sorted_letters:
            print(f"{letter}: {count}") 

    except FileNotFoundError:
        print(f"Error: The file '{book_path}' was not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied for file '{book_path}'.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print_report(book_path)
