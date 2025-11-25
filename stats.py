def count_words(book):
  return len(book.split())

def sort_by_word_count(items):
    return items["num"]

def count_characters(book):
  book_array = book.split()
  character_dict = {}
  for word in book_array:
    letters = list(word)
    for letter in letters:
      if letter.lower() not in character_dict:
        character_dict[letter.lower()] = 1
      else:
        character_dict[letter.lower()] += 1
      
  return character_dict

def report(dict):
  new_list = []
  for item in dict:
    new_list.append({ "char": item, "num": dict[item]})
  new_list.sort(reverse=True, key=sort_by_word_count)
  return new_list
