'''Chap 7'''

def palindrome(word):
    word = word.lower()
    
    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            return False
    return True

def main():
    user_word = input("Enter a word: ")
    
    if palindrome(user_word):
        print("This Word is a Palindrome!")
    else:
        print("This Word is not a Palindrome.")

if __name__ == "__main__":
    main()