import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(html):
    # Break down of pattern:
    # - src=" matches the literal characters "src=" in the HTML code.
    # - https?:// matches the protocol part of the URL, i.e: "http://" & "https://".
    # - (?:www\.)? matches an optional "www." part of the URL.
    # - youtube\.com/embed/ matches the literal characters "youtube.com/embed/" in the URL.
    # - ([^"]+) is a capturing group that matches & captures one or more characters that are not a double quote ("). 
    #   This part captures the YouTube video ID.
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"' 
    match = re.search(pattern, html)
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        return None

if __name__ == "__main__":
    main()