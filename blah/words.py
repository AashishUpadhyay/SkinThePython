import sys
from urllib.request import urlopen

# test url:  http://sixty-north.com/c/t.txt


def fetch_words(url):
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

    story.close()
    return story_words


def print_items(story_words):
    for w in story_words:
        print(w)


def main(url):
    print_items(fetch_words(url))


if __name__ == '__main__':
    main(sys.argv[1])  # 0th arg is filename
