path = "../resources/Forrasok/4_Tarsalgo/ajto.txt"  # Relative paths are relative to current working directory

entries = []

# read file from local directory
file = open(path)
for line in file.readlines():
    entries.append(line.strip())

print(f"Entries: {entries}")  # string interpolation

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
