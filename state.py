import random 


class Lizard:
    def __init__(self, row, col):
        self.row = row
        self.col = col
  
        
class State:
    def __init__(self, length, p, lizards=None):
        self.size = length
        self.cost = 0
        self.p = p
        self.lizards = []
        if lizards:
            self.lizards[:0] = lizards

    def assign_random_indexes(self, arr):
        self.lizards = [Lizard(random.randint(0, self.size - 1), random.randint(0, self.size - 1)) 
                        for i in range(self.p)]
        for i in range(self.p):
            row = self.lizards[i].row
            col = self.lizards[i].col
            if arr[row][col] != 2:
                continue
            row, col = get_random_index(arr, self.lizards, self.size, self.p)
            self.lizards[i].row = row
            self.lizards[i].col = col

    def calculate_cost(self, arr):
        self.cost = 0
        for i in range(self.p):
            for j in range(self.p):
                if i == j:
                    continue
                min_col = self.lizards[i].col
                max_col = self.lizards[j].col
                min_row = self.lizards[i].row
                max_row = self.lizards[j].row
                if self.lizards[j].col < self.lizards[i].col:
                    min_col = self.lizards[j].col
                    max_col = self.lizards[i].col
                if self.lizards[j].row < self.lizards[i].row:
                    min_row = self.lizards[j].row
                    max_row = self.lizards[i].row
                if self.lizards[i].row == self.lizards[j].row and self.lizards[i].col == self.lizards[j].col:
                    self.cost += 1
                elif self.lizards[i].row == self.lizards[j].row:
                    col = min_col
                    while col <= max_col:
                        if arr[self.lizards[i].row][col] == 2:
                            break
                        col += 1
                    if col > max_col:
                        self.cost += 1
                elif self.lizards[i].col == self.lizards[j].col:
                    row = min_row
                    while row <= max_row:
                        if arr[row][self.lizards[i].col] == 2:
                            break
                        row += 1
                    if row > max_row:
                        self.cost += 1
                elif (max_row - min_row == max_col - min_col):
                    start_row = max_row
                    end_row = min_row
                    if max_row == self.lizards[i].row:
                        start_col = self.lizards[i].col
                        end_col = self.lizards[j].col
                    else:
                        start_col = self.lizards[j].col
                        end_col = self.lizards[i].col
                    count = 1
                    if end_col < start_col:
                        count = -1
                    while start_row != end_row and start_col != end_col:
                        if arr[start_row][start_col] == 2:
                            break
                        start_row -= 1
                        start_col += count
                        if start_row == end_row and start_col == end_col:
                            self.cost += 1
        self.cost = self.cost / 2
        return self.cost

    def transition(self, arr):
        new_allocation = list()
        for i in range(self.p):
            new_allocation.append(Lizard(self.lizards[i].row, self.lizards[i].col))
        random_index = random.randint(0, self.p - 1)
        lizard = new_allocation[random_index]
        random_row, random_col = get_random_index(arr, self.lizards, self.size, self.p)
        while lizard.row == random_row and lizard.col == random_col:
            random_row, random_col = get_random_index(arr, self.lizards, self.size, self.p)
        lizard.row = random_row
        lizard.col = random_col
        return State(self.size, self.p, new_allocation)
   
    
def write_output(msg, arr, length):
    output_file = open("output.txt", "w")
    output_file.write(msg)
    if not arr:
        return
    output_file.write('\n')
    for i in range(length):
        output_file.write(''.join([str(x) for x in arr[i]]))
        if i != length - 1:
            output_file.write('\n')
    output_file.close()


def get_random_index(arr, lizards, length, p):
    random_row = random.randint(0, length - 1)
    random_col = random.randint(0, length - 1)
    rows = list()
    for row in range(length):
        rows.append(list())
    for i in range(p):
        rows[lizards[i].row].append(lizards[i].col)
    occupied = False
    if len(rows[random_row]) > 0:
        for col in rows[random_row]:
            if col == random_col:
                occupied = True
                break
    while arr[random_row][random_col] == 2 or occupied:
        random_row = random.randint(0, length - 1)
        random_col = random.randint(0, length - 1)
        occupied = False
        if len(rows[random_row]) > 0:
            for col in rows[random_row]:
                if col == random_col:
                    occupied = True

    return random_row, random_col
