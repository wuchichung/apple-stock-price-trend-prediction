import re


def transform(link):
    result = ""
    for w in link:
        result += w
    return result


def remove_special_characters(link_string):
    letters = list(link_string)
    for i in range(len(letters)):
        l = letters[i]
        if not (l.isalnum() or l == ">" or l == "<" or l == " "):
            letters[i] = " "
    return "".join(letters)


def get_guardian_time(link_string):
    time_search = re.search(r"/([\d]+)/([\w]+)/+([\d]+)/", link_string)

    if (time_search):
        year = time_search.group(1)
        month = time_search.group(2)
        date = time_search.group(3)
        time = month + " " + date + "," + year
        return time


def get_guardian_words(link_string):
    total_words = []
    titles = re.findall(r">([\w\s]+)<", link_string)
    for title in titles:
        words = re.findall(r"[\w]+", title)
        total_words += words
    return total_words


def get_guardian_time_words(link):
    link_string = transform(link)
    time = get_guardian_time(link_string)
    link_string = remove_special_characters(link_string)
    words = get_guardian_words(link_string)

    return time, words


if __name__ == "__main__":
    test = ""
    get_guardian_time_words(test)