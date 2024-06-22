import re

def main():
    html = input("HTML: ")
    print(parse(html))

def parse(s):
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"'

    match = re.search(pattern, s)

    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"

    return None

if __name__ == '__main__':
    main()
