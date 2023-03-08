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
        self.month = month
        self.ordinal = ordinal
        self.duration = duration
        self.title = title
        self.tools = tools

    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4}, {5}, {6}".format(self.speaker, self.month, self.day, self.ordinal,
                                                          self.duration, self.title,
                                                          self.tools)


input_file = open("eloadasok.txt")

talks = []

for line in input_file.readlines():
    split_line = line.split("\t")
    talks.append(
        Talk(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4], split_line[5], split_line[6].split(",")))

print(talks[0])
