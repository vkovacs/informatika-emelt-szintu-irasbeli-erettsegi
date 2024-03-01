# 1
signals_file = open("veetel.txt")

signals_metadata = []
signals = []

actual_line = 1
for line in signals_file.readlines():
    if actual_line % 2 == 1:
        signals_metadata.append([int(x) for x in line.strip().split(" ")])  # split line and convert to array of ints
    else:
        signals.append(line.strip())

    actual_line = actual_line + 1

print(signals_metadata)
print(signals)

# 2
print(f'First radio amateur id in file: {signals_metadata[0][1]}')
print(f'Last radio amateur id in file: {signals_metadata[-1][1]}')

# 3
for i in range(len(signals)):
    if 'farkas' in signals[i]:
        print(f'farkas word is in {signals_metadata[i]}')

# 4
signal_count_per_day = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for metadata in signals_metadata:
    day = metadata[0]
    day_index = day - 1
    signal_count_per_day[day_index] = signal_count_per_day[day_index] + 1

for day_index in range(len(signal_count_per_day)):
    print(f'On the {day_index + 1} day there were {signal_count_per_day[day_index]} message')

# 5
all_signal_for_a_day = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []}
for i in range(len(signals_metadata)):
    day = signals_metadata[i][0]
    all_signal_for_a_day[day].append(signals[i])


# print(all_signal_for_a_day)

def merged_character(lists, index):
    for list in lists:
        if list[index] != '#':
            return list[index]
    return '#'


merged_signals_for_a_day = dict()

for day in all_signal_for_a_day:  # iterate over the dict day is the key
    signals_for_a_day = all_signal_for_a_day[day]
    merged_signal = ''
    for signal_index in range(len(signals_for_a_day[0])):  # for every character index of a message (all messages has the same legnth for a given day) merge the characters of all the messages prefer not # over #
        merged_signal = merged_signal + merged_character(all_signal_for_a_day[day], signal_index)
    merged_signals_for_a_day[day] = merged_signal

print(merged_signals_for_a_day)


# 6
def szame(szo):
    for i in szo:
        if i < 0 or i > 9:
            return False
    return True


# 7
def radio_amateur_signal_for_a_day(day, radio_amateur_id):
    for i in range(len(signals_metadata)):
        if signals_metadata[i][0] == day and signals_metadata[i][1] == radio_amateur_id:
            return signals[i]


# -1: no entity count description in signal. -2: invalid entity count description. otherwise the number of entities
def determine_entity_count(signal):
    if '/' not in signal:
        return -1

    entity_description = signal.split(" ")[0]

    if '#' in entity_description:
        return -2

    entities_count_string = entity_description.split('/')
    return int(entities_count_string[0]) + int (entities_count_string[1])

def determine_entity_count_message(signal):
    count = determine_entity_count(signal)

    if (count == -1):
        return "Nincs ilyen feljegyzés"
    if (count == -2):
        return "Nincs információ"

    return count

day = 2
radio_amateur_id = 15

print(determine_entity_count_message(radio_amateur_signal_for_a_day(2, 15)))
print(determine_entity_count_message(radio_amateur_signal_for_a_day(6, 19)))
print(determine_entity_count_message(radio_amateur_signal_for_a_day(10, 7)))