import csv


def write_csv(time_words_dict):
    if not bool(time_words_dict) and len(time_words_dict.keys()) == 0:
        return False

    with open('bloomberg_apple_record.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)

        for time, words in time_words_dict.items():
            row = []
            row.append(time)

            for word in words:
                row.append(word)

            writer.writerow(row)
            return True


if __name__ == "__main__":
    dista = {}
    dista["time"] = ["2016", "2017", "2018"]
    write_csv(dista)
