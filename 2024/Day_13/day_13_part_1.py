def parse_input_file(file_path):
    machines = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 4):  
            button_a_line = lines[i].strip()
            x_a = int(button_a_line.split('X+')[1].split(',')[0])
            y_a = int(button_a_line.split('Y+')[1])
            
            button_b_line = lines[i + 1].strip()
            x_b = int(button_b_line.split('X+')[1].split(',')[0])
            y_b = int(button_b_line.split('Y+')[1])
            
            prize_line = lines[i + 2].strip()
            x_prize = int(prize_line.split('X=')[1].split(',')[0])
            y_prize = int(prize_line.split('Y=')[1])
            
            machines.append({
                "button_a": (x_a, y_a),
                "button_b": (x_b, y_b),
                "prize": (x_prize, y_prize)
            })
    return machines


def solve_machine(x_a, y_a, x_b, y_b, x_prize, y_prize):
    min_cost = float('inf')
    
    for a in range(101): 
        x_remaining = x_prize - a * x_a
        y_remaining = y_prize - a * y_a

        if x_remaining % x_b == 0 and y_remaining % y_b == 0:
            b_x = x_remaining // x_b
            b_y = y_remaining // y_b
            if b_x == b_y and b_x >= 0:
                b = b_x
                cost = 3 * a + b
                if cost < min_cost:
                    min_cost = cost

    if min_cost == float('inf'):
        return None
    return min_cost


def solve_all_machines(machines):
    total_cost = 0

    for machine in machines:
        x_a, y_a = machine['button_a']
        x_b, y_b = machine['button_b']
        x_prize, y_prize = machine['prize']

        cost = solve_machine(x_a, y_a, x_b, y_b, x_prize, y_prize)
        if cost is not None:
            total_cost += cost

    return total_cost


if __name__ == "__main__":
    input_file = "input.txt"  
    machines = parse_input_file(input_file)
    total_cost = solve_all_machines(machines)
    print(total_cost)
