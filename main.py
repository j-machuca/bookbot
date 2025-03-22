import sys
from stats import get_word_count,count_chars,sorted_chars

def get_book_text(file_path)->str:
  with open(file_path) as f:
    file_contents = f.read()
    print("----------- Word Count ----------")
    get_word_count(file_contents)
    print("--------- Character Count -------")
    char_count = count_chars(file_contents)
    sorted_count = sorted_chars(char_count)
    for char in sorted_count:
      if char['char'].isalpha():
        print(f"{char['char']}: {char['count']}")
    
def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  print(f"Analyzing book found at {sys.argv[1]}")
  get_book_text(sys.argv[1])
if __name__ == "__main__":
  print("============ BOOKBOT ============")
  main()