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

