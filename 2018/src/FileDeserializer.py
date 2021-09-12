from Entry import Entry


class FileDeserializer:
    def __init__(self, path):
        self.path = path

    def __read_file(self):
        with open(self.path) as file:
            return file.readlines()

    def __to_entries(self, lines):
        entries = []

        for line in lines:
            tokens = line.split()
            entries.append(Entry(tokens[0], tokens[1], tokens[2], tokens[3]))

        return entries

    def deserialize(self):
        return self.__to_entries(self.__read_file())
