def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    word_count = count_total_words(text)
    chars_counts = count_all_chars(text)
    doc_report = present_doc_report(path, word_count, chars_counts)
    return(doc_report) 

def get_text(path):
    with open(path) as f:
        return f.read()

def count_total_words(text):
    words = text.split()
    return len(words)

def count_all_chars(text):
    lowered_text = text.lower()
    char_counts = {}
    for char in lowered_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def present_doc_report(path, word_count, chars_counts):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document \n")
    chars_data = present_chars_counts(chars_counts)
    print("--- End report ---")

def present_chars_counts(chars_counts):
    alpha_chars = {}
    for key, value in chars_counts.items():
        if key.isalpha():
            alpha_chars[key] = value
    alpha_chars_list = list(alpha_chars.items())
    sorted_list = sorted(alpha_chars_list, reverse=True, key=lambda item: item[1])
    for key, value in sorted_list:
        print(f"The '{key}' character was found {value} times")
           
    


main()