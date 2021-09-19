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

entries_for_actor = list(filter(lambda entry: entry.split()[2] == input_actor_id, entries))  # use lambda function to filter for entries of an actor and store it in a list for future use (otherwise it would be consumed on the first iteration)

for entry in entries_for_actor:
    entry_tokens = entry.split()
    hour = entry_tokens[0]
    minute = entry_tokens[1]
    direction = entry_tokens[3]
    if direction == "be":
        print(f"{hour}:{minute}-", end="") # keyword argument "end" is added to prevent print to terminate printing by line ending
    else:
        print(f"{hour}:{minute}")

# 8
entry_times = [] # will only contain time typed values for time span calculation
for entry in entries_for_actor:
    entry_tokens = entry.split()
    hour = entry_tokens[0].zfill(2)  # fill it by trailing zeros if necessary because time api needs hours in such format
    minute = entry_tokens[1].zfill(2) # fill it by trailing zeros if necessary because time api needs minutes in such format
    direction = entry_tokens[3]

    from datetime import datetime  # import should be on the top line but it's here to do not confuse anyone while studiing the previous solutions

    entry_time = datetime.strptime(f"{hour}:{minute}", "%H:%M")  # convert string to time
    entry_times.append(entry_time)


# preprocess entry_time to make sure it contains even number of elements
total_seconds_in_room = 0
stayed_in_the_room = (len(entry_times) % 2 == 1)

if stayed_in_the_room:  # if the actor was in the room at the end of the observation add 15:00 as the last time
    entry_times.append(datetime.strptime("15:00", "%H:%M"))

for i in range(1, len(entry_times), 2):
    current_time = entry_times[i]
    last_time = entry_times[i - 1]
    total_seconds_in_room += (current_time - last_time).total_seconds() # in case actor exit the room calculate the length of the session in this room and acumulate it in total_seconds_in_room

print()
print(f"8: Actor by id {input_actor_id} was in the room for {total_seconds_in_room / 60} minutes", end=" ")
if stayed_in_the_room:
    print("and he was in the room in the end of the observation.")

