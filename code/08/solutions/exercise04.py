import re

def extract_info():
    text = "Contacts are: pyhton@hanam.ai, info@hanam.ai, support@hanam.ai"
    # 1. Extract all emails
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    print("Email found:", emails)
    # 2. Replace domains with ***.com
    masked_text = re.sub(r'@[\w\.-]+', '@***.ai', text)
    print("New text:", masked_text)

if __name__ == "__main__":
    extract_info()