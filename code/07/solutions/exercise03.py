def format_text():
    text = "   Hello, python is a FANTASTIC language!   "
    # 1. Remove whitespaces
    clean_text = text.strip()
    # 2. Replace a word
    replaced_text = clean_text.replace("FANTASTIC", "incredible")
    # 3. Convert lower case
    final_text = replaced_text.lower()
    print(final_text) # Output: hello, python is an incredible language!

if __name__ == "__main__":
    format_text()