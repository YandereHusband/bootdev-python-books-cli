import sys
from stats import count_words, count_characters, report

def get_book_text(flie_path):
  file_contents = ""

  with open(flie_path) as f:
    file_contents = f.read()
  
  return file_contents

def print_report(character_list, word_count):
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")

  for item in character_list:
    if not item["char"].isalpha():
      continue
    print(f"{item["char"]}: {item["num"]}")
  print("============= END ===============")

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  path = sys.argv[1]

  book = get_book_text(path)
  num_words = count_words(book)
  num_characters = count_characters(book)
  dict = report(num_characters)

  print_report(dict, num_words)

main()