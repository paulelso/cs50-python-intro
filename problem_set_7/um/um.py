import re
import sys
import string


def main():
    sentences = [
        "hello, um, world",
        "um, hello, um, world",
        "um...",
        "yum",
        "yummy",
        "um?",
        "album",
        "Um, thanks for the album.",
        "Um, thanks, um...",
        "Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?",
        "Um, thanks, um, regular expressions make sense now."
    ]
    for s in sentences:
        print(count(s))
              


def count(s):
    s = s.lower().strip(string.punctuation) # catches um, um., um..., um?
    found = re.findall(r"\bum\b", s)
    return len(found)
        
        
if __name__ == "__main__":
    main()