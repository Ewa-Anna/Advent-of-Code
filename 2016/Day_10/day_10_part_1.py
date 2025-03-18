from collections import defaultdict, deque

def parse_instructions(filename):
    bots = defaultdict(list)
    instructions = {}
    
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
    
    return bots, instructions

def process_bots(bots, instructions):
    queue = deque([bot for bot in bots if len(bots[bot]) == 2])
    
    while queue:
        bot = queue.popleft()
        chips = sorted(bots[bot])
        low, high = chips
        
        if low == 17 and high == 61:
            return bot
        
        low_type, low_id, high_type, high_id = instructions[bot]
        
        if low_type == "bot":
            bots[low_id].append(low)
            if len(bots[low_id]) == 2:
                queue.append(low_id)
        
        if high_type == "bot":
            bots[high_id].append(high)
            if len(bots[high_id]) == 2:
                queue.append(high_id)
        
        bots[bot] = [] 
    
    return None

def main():
    bots, instructions = parse_instructions("input.txt")
    result = process_bots(bots, instructions)
    print("Bot responsible for comparing 61 and 17:", result)

if __name__ == "__main__":
    main()
