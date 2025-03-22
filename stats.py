def get_word_count(text:str)-> None:
  num_words = len(text.split())
  print(f"Found {num_words} total words")

def count_chars(text:str)->dict:
  words = text.split()
  char_map = {}
  for word in words:
    for char in word:
      if char.lower() in char_map:
        char_map[char.lower()] +=1
      else:
        char_map[char.lower()] = 1
  return char_map

def sorted_chars(char_map:dict)-> list:
  char_list = []
  for char,count in  char_map.items():
   char_list.append({"char":char,"count":count})
  
  char_list.sort(reverse=True,key=lambda x :x["count"])
  return char_list