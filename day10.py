input_data = '''noop
noop
addx 5
addx 21
addx -16
noop
addx 1
noop
noop
addx 4
addx 1
addx 4
addx 1
noop
addx 4
addx -9
noop
addx 19
addx -5
noop
noop
addx 5
addx 1
addx -38
addx 5
addx -2
addx 2
noop
noop
addx 7
addx 9
addx 20
addx -3
addx -18
addx 2
addx 5
noop
noop
addx -2
noop
noop
addx 7
addx 3
addx -2
addx 2
addx -28
addx -7
addx 5
noop
addx 2
addx 32
addx -27
noop
noop
noop
noop
noop
addx 7
noop
addx 22
addx -19
noop
addx 5
noop
addx -7
addx 17
addx -7
noop
addx -20
addx 27
noop
addx -16
addx -20
addx 1
noop
addx 3
addx 15
addx -8
addx -2
addx -6
addx 14
addx 4
noop
noop
addx -17
addx 22
noop
addx 5
noop
noop
noop
addx 2
noop
addx 3
addx -32
addx -5
noop
addx 4
addx 3
addx -2
addx 34
addx -27
addx 5
addx 16
addx -18
addx 7
noop
addx -2
addx -1
addx 8
addx 14
addx -9
noop
addx -15
addx 16
addx 2
addx -35
noop
noop
noop
noop
addx 3
addx 4
noop
addx 1
addx 4
addx 1
noop
addx 4
addx 2
addx 3
addx -5
addx 19
addx -9
addx 2
addx 4
noop
noop
noop
noop
addx 3
addx 2
noop
noop
noop'''


# input_data = '''addx 15
# addx -11
# addx 6
# addx -3
# addx 5
# addx -1
# addx -8
# addx 13
# addx 4
# noop
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx -35
# addx 1
# addx 24
# addx -19
# addx 1
# addx 16
# addx -11
# noop
# noop
# addx 21
# addx -15
# noop
# noop
# addx -3
# addx 9
# addx 1
# addx -3
# addx 8
# addx 1
# addx 5
# noop
# noop
# noop
# noop
# noop
# addx -36
# noop
# addx 1
# addx 7
# noop
# noop
# noop
# addx 2
# addx 6
# noop
# noop
# noop
# noop
# noop
# addx 1
# noop
# noop
# addx 7
# addx 1
# noop
# addx -13
# addx 13
# addx 7
# noop
# addx 1
# addx -33
# noop
# noop
# noop
# addx 2
# noop
# noop
# noop
# addx 8
# noop
# addx -1
# addx 2
# addx 1
# noop
# addx 17
# addx -9
# addx 1
# addx 1
# addx -3
# addx 11
# noop
# noop
# addx 1
# noop
# addx 1
# noop
# noop
# addx -13
# addx -19
# addx 1
# addx 3
# addx 26
# addx -30
# addx 12
# addx -1
# addx 3
# addx 1
# noop
# noop
# noop
# addx -9
# addx 18
# addx 1
# addx 2
# noop
# noop
# addx 9
# noop
# noop
# noop
# addx -1
# addx 2
# addx -37
# addx 1
# addx 3
# noop
# addx 15
# addx -21
# addx 22
# addx -6
# addx 1
# noop
# addx 2
# addx 1
# noop
# addx -10
# noop
# noop
# addx 20
# addx 1
# addx 2
# addx 2
# addx -6
# addx -11
# noop
# noop
# noop'''

values ={
    'noop': 1,
    'addx': 2
}

# 1
# x = 1
# cycles = 0
# looked_for = {20,60,100,140,180,220}
# suma = 0
# for line in input_data.splitlines():
#     command = line.split(' ')[0]
#     try:
#         data = int(line.split(' ')[1])
#     except IndexError:
#         data = None
#     for cycle in range(values[command]):
#         cycles += 1
#         if cycles in looked_for:
#             suma+=x*cycles
#
#     if data is not None:
#         x+= data
#
# print(suma)


2
screen = ['']
screen_line = 0
x = 1
cycles = 0

for line in input_data.splitlines():
    command = line.split(' ')[0]
    if len(line.split(' ')) == 2:
        data = int(line.split(' ')[1])
    else:
        data = None

    for cycle in range(values[command]):
        cycles += 1

        if cycles-1 == x or cycles-1 == x-1 or cycles-1 == x+1:
            screen[screen_line] += '#'
        else:
            screen[screen_line] += '.'

        if cycles == 40:
            screen_line +=1
            screen.append('')
            cycles = 0

    if data is not None:
        x+= data

for line in screen:
    print("".join(line))
