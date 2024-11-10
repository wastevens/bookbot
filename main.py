def count_words(source):
    words = source.split()
    return len(words)

def count_unique_characters(source):
    words = source.lower().split()
    character_counts = {}
    for word in words:
        characters = list(word)
        for character in characters:
            if character in character_counts:
                character_counts[character] += 1
            else:
                character_counts[character]= 1
    return character_counts

def list_alpha_character_counts(character_counts):
    alpha_character_counts = []
    for character in character_counts:
        if(character.isalpha()):
            alpha_character_counts.append({"character": character, "count": character_counts[character]})
    return alpha_character_counts

def sort_key(list_character_counts):
    return list_character_counts["count"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path):
    file_contents = get_book_text(book_path)
    word_count = count_words(file_contents)
    character_counts = count_unique_characters(file_contents)
    alpha_character_counts = list_alpha_character_counts(character_counts)
    alpha_character_counts.sort(reverse=True, key=sort_key)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")

    for character_count in alpha_character_counts:
        print(f"The {character_count['character']} character was found {character_count['count']} times")

    print("--- End report ---")

def main():
    print_report("books/frankenstein.txt")
    
main()