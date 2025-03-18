from collections import defaultdict, deque

def parse_instructions(filename):
    bots = defaultdict(list)
    instructions = {}
    outputs = {}
    
    with open(filename) as f:
        for line in f:
            parts = line.strip().split()
            if parts[0] == "value":
                value = int(parts[1])
                bot_id = int(parts[-1])
                bots[bot_id].append(value)
            else:
                bot_id = int(parts[1])
                low_type, low_id = parts[5], int(parts[6])
                high_type, high_id = parts[10], int(parts[11])
                instructions[bot_id] = (low_type, low_id, high_type, high_id)
    
    return bots, instructions, outputs

def process_bots(bots, instructions, outputs):
    queue = deque([bot for bot in bots if len(bots[bot]) == 2])
    
    while queue:
        bot = queue.popleft()
        chips = sorted(bots[bot])
        low, high = chips
        
        if low == 17 and high == 61:
            responsible_bot = bot
        
        low_type, low_id, high_type, high_id = instructions[bot]
        
        if low_type == "bot":
            bots[low_id].append(low)
            if len(bots[low_id]) == 2:
                queue.append(low_id)
        else:
            outputs[low_id] = low
        
        if high_type == "bot":
            bots[high_id].append(high)
            if len(bots[high_id]) == 2:
                queue.append(high_id)
        else:
            outputs[high_id] = high
        
        bots[bot] = [] 
    
    return responsible_bot, outputs

def main():
    bots, instructions, outputs = parse_instructions("input.txt")
    responsible_bot, outputs = process_bots(bots, instructions, outputs)
    print("Bot responsible for comparing 61 and 17:", responsible_bot)
    
    result = outputs[0] * outputs[1] * outputs[2]
    print("Product of outputs 0, 1, and 2:", result)

if __name__ == "__main__":
    main()