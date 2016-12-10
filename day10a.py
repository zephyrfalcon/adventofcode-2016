# day10_v2.py

import collections

class Bot:
    def __init__(self):
        self.values = []
        self.has_distributed = False
    def receive(self, value):
        assert len(self.values) < 2
        if value not in self.values:
            self.values.append(value)
        if len(self.values) == 2:
            self.values.sort()
    def is_ready(self):
        return len(self.values) == 2

class OutputBin:
    def __init__(self):
        self.values = []
    def receive(self, value):
        self.values.append(value) # assume a bin can hold any number of values

def give(bot, recv1, recv2):
    """ Give a bot's values to two receivers. Returns True if this was done
        successfully, False if it could not be done (yet). """
    if not bot.has_distributed and bot.is_ready():
        low, high = bot.values
        recv1.receive(low)
        recv2.receive(high)
        bot.has_distributed = True
        return True
    return False

def process_instruction(line):
    parts = line.split()
    if parts[0] == 'value':
        # value V goes to bot B
        value, botno = int(parts[1]), int(parts[5])
        bot = bots[botno]
        bot.receive(value)
    elif parts[0] == 'bot':
        # bot B gives low to RECV1 R1 and high to RECV2 R2
        botno = int(parts[1])
        rectype1, rectype2 = parts[5], parts[10]
        recno1, recno2 = int(parts[6]), int(parts[11])
        recv1 = bots[recno1] if rectype1 == 'bot' else output[recno1]
        recv2 = bots[recno2] if rectype2 == 'bot' else output[recno2]
        return give(bots[botno], recv1, recv2)
    return True

bots = collections.defaultdict(lambda: Bot())
output = collections.defaultdict(lambda: OutputBin())

with open("input10.txt") as f:
    instructions = f.readlines()

# new approach: try instructions; if they cannot be done yet, put at end of
# queue
while instructions:
    ins = instructions.pop(0)
    ok = process_instruction(ins)
    if not ok:
        instructions.append(ins)

total = 1
for i in range(3):
    out = output[i]
    print(i, out.values)
    total = total * out.values[0]
print(total)
