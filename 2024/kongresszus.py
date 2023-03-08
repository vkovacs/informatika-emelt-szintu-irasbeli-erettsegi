class Talk:
    speaker = "",
    month = 0,
    day = 0,
    ordinal = 0,
    duration = 0,
    title = "",
    tools = []

    def __init__(self, speaker, month, day, ordinal, duration, title, tools):
        self.speaker = speaker
        self.month = int(month) # ha lehagyjuk az int-é konvertálást az első rendezésénél elromlik a sorrend mert string ként próbál majd rendezni
        self.day = int(day)
        self.ordinal = int(ordinal)
        self.duration = int(duration)
        self.title = title
        self.tools = tools

    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4}, {5}, {6}".format(self.speaker, self.month, self.day, self.ordinal,
                                                          self.duration, self.title,
                                                          self.tools)


input_file = open("eloadasok.txt")

# 1. feladat
talks = []

for line in input_file.readlines():
    split_line = line.strip().split(
        "\t")  # strip: used to remove line end character "\n" which would just cause trouble later
    talks.append(
        Talk(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4], split_line[5],
             split_line[6].split(",")))

# 2. feladat

dayTalksDict = {}  # dictionary aminek value-ja az azonos napon tartott előadások listája, key-e pedig az nap
for talk in talks:
    if talk.day in dayTalksDict:
        dayTalksDict[talk.day].append(talk)
    else:
        dayTalksDict[talk.day] = [talk]

sortedDayTalksDict = dict(sorted(dayTalksDict.items()))  # https://realpython.com/sort-python-dictionary/

for key, value in sortedDayTalksDict.items():
    print("november: {0}.:".format(key))
    value.sort(key=lambda talk: talk.ordinal)  # https://www.techiedelight.com/sort-list-of-objects-python/

    i = 1
    for talk in value:
        print(str(i) + "." + talk.speaker)
        i = i + 1
