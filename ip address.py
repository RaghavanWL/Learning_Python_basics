ip = input("Please enter an IP address : ")
if ip[-1] != '.':
    ip += '.'

segment = 1
segment_length = 0
# character = ""

for i in ip:
    if i == '.':
        print("segment {} contains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1
