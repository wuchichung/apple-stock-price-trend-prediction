import re

def transform(link):
    result = ""
    for w in link:
        result += w
    return result


def get_time(link):
    time_search = re.search(r"/([0-9-]+)/", link)
    time = ""

    if time_search:
        search = re.findall(r"[0-9]+", time_search.group(1))
        time = search[1] + "/" + search[-1] + "/" + search[0]
    return time


def get_words(link):
    total_words = []
    titles = re.findall(r">([\w'?!&%;.\s]+)<", link)
    for title in titles:
        words = re.findall(r"[\w]+", title)
        total_words += words
    return total_words


def get_time_words(time_title_dist):
    if not bool(time_title_dist):
        return None
    else:
        time_words = {}
        for key in time_title_dist.keys():
            title = transform(time_title_dist[key])

            letters = list(title)
            for i in range(len(letters)):
                l = letters[i]
                if not (l.isalnum() or l == ">" or l == "<" or l == " "):
                    letters[i] = " "
            title = "".join(letters)

            words = get_words(title)
            time_words[key] = words
            return time_words