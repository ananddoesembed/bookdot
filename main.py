from stats import get_book_text,count_charactor
import sys

def main():
    if len(sys.argv) != 2 :
        sys.exit(1)
    f = get_book_text(sys.argv[1])
    word = list(f)
    count = len(f.split())
    d = count_charactor(word)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}..\n----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for i in d:
        print(f"{i}: {d[i]}")
    print("============= END ===============")

main()