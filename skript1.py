def split_words_with_letters_and_numbers(text):
    # Initialize an empty list to store the split words
    split_words = []

    # Initialize empty strings to store the letters and numbers
    letters = ""
    numbers = ""

    # Iterate through each character in the text
    for char in text:
        if char.isalpha():
            letters += char
        elif char.isdigit():
            numbers += char
        else:
            # If a non-letter, non-digit character is encountered, add the previous word to the list
            if letters:
                split_words.append((letters, numbers))
                letters = ""
                numbers = ""

    # Add the last word if it exists
    if letters:
        split_words.append((letters, numbers))

    return split_words

# Example usage:
text = "This is a text with words like word123 and another word456."
word_splits = split_words_with_letters_and_numbers(text)

for idx, (letters_part, numbers_part) in enumerate(word_splits, start=1):
    print(f"Word {idx} - Letters Part: {letters_part}, Numbers Part: {numbers_part}")
