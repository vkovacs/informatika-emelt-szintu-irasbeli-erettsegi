from FileDeserializer import FileDeserializer


# 1
def deserialize_file(filename):
    deserializer = FileDeserializer(filename)
    return deserializer.deserialize()


for i in deserialize_file("ajto.txt"):
    print(str(i))