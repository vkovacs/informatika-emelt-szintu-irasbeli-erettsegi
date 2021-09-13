# 1
path = "../resources/Forrasok/4_Tarsalgo/ajto.txt"  # Relative paths are relative to current working directory

entries = []

# read file from local directory
file = open(path)
for line in file.readlines():
    entries.append(line.strip())

file.close()

print(f"Entries: {entries}")  # string interpolation

# 2
# First entry to the room:
first_entry = entries[0]  # first must be an entering entry

# split by white space (default)
entry_tokens = first_entry.split()

first_actor_id = entry_tokens[2]
print(f"First actor id to enter the room: {first_actor_id}")

for entry in reversed(entries):
    entry_tokens = entry.split()
    if entry_tokens[3] == "ki":
        last_actor_id = entry_tokens[2]
        print(f"Last actor id to exit {last_actor_id}")
        break  # break the execution of the loop since the last actor id is already found

# 3
actor_id_door_pass_count_dict = {}

for entry in entries:
    entry_tokens = entry.split()
    actor_id = int(entry_tokens[2])  # actor_id must be casted to int, because by default it would be a string,and the lexicographic order of ints and strings are different

    if actor_id in actor_id_door_pass_count_dict:
        actor_id_door_pass_count_dict[actor_id] = actor_id_door_pass_count_dict[actor_id] + 1
    else:
        actor_id_door_pass_count_dict[actor_id] = 1


output_file_path = "athaladas.txt"
output_file = open(output_file_path, "w") #  by using 'w' flag file will be created if not exists, if exists content will be overwritten

for actor_id in sorted(actor_id_door_pass_count_dict):  # this sorted method call uses to int() cast
    output_file.write(f"{actor_id} {actor_id_door_pass_count_dict[actor_id]}\n")  # "\n" is for breaking the line

output_file.close()

# 4
print("4: Actors still in the room:")
for actor_id in actor_id_door_pass_count_dict:
    if actor_id_door_pass_count_dict[actor_id] % 2 == 1:  # actors in the room are the actors whose door pass count are odd
        print(actor_id)

# 5
max_actor_count_in_room = 0
at = ""
actor_count_in_room = 0
for entry in entries:
    entry_tokens = entry.split()
    hour = entry_tokens[0]
    minute = entry_tokens[1]
    actor_id = entry_tokens[2]
    direction = entry_tokens[3]

    if direction == "be":
        actor_count_in_room += 1

        if actor_count_in_room > max_actor_count_in_room:
            max_actor_count_in_room = actor_count_in_room
            at = hour + ":" + minute
    else:
        actor_count_in_room -= 1

print(f"5: Most actor simultaneously in the room: {max_actor_count_in_room} at: {at}")

# 6
print("6: Please type an existing actor_id:")
input_actor_id = input()  # read input as string by default

# 7
print("Actor's sessions in the room:")

entries_for_actor = filter(lambda entry: entry.split()[2] == input_actor_id, entries)  # use lambda function to filter for entries of an actor

for entry in entries_for_actor:
    entry_tokens = entry.split()
    hour = entry_tokens[0]
    minute = entry_tokens[1]
    actor_id = entry_tokens[2]
    direction = entry_tokens[3]
    if direction == "be":
        print(f"{hour}:{minute}-", end="") # keyword argument "end" is added to prevent print to terminate printing by line ending
    else:
        print(f"{hour}:{minute}")
