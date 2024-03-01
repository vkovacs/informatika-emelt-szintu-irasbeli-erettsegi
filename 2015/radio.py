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
