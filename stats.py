def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    text = text.lower()
    char_count = {}
    
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
    

def sort_char_count(char_count):
    sorted_chars = [
        {"char": char, "count": count}
        for char, count in char_count.items() if char.isalpha()  
    ]
    
    sorted_chars.sort(key=lambda item: item["count"], reverse=True)  
    return sorted_chars