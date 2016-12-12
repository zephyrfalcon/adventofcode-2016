# day12a.py

registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

def maybe_a_number(s):
    try:
        return int(s)
    except:
        return s

def parse(instruction):
    parts = instruction.split()
    return [maybe_a_number(p) for p in parts]

def run(instructions):
    ip = 0 # current instructions
    while 0 <= ip < len(instructions):
        parts = instructions[ip]
        if parts[0] == 'cpy':
            value, target = parts[1:3]
            if value in registers:
                value = registers[value]
            registers[target] = value
        elif parts[0] == 'jnz':
            value, offset = parts[1:3]
            if value in registers:
                value = registers[value]
            if value != 0:
                ip = ip + offset
                continue
        elif parts[0] == 'inc':
            registers[parts[1]] += 1
        elif parts[0] == 'dec':
            registers[parts[1]] -= 1
        else:
            print("Unknown instruction:", parts)
        ip += 1

with open("input12.txt") as f:
    instructions = f.readlines()
instructions = [parse(ins) for ins in  instructions]

run(instructions)
print(registers)

