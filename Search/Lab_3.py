class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self, table_size, max_collision):
        self.table_size = table_size
        self.max_collision = max_collision
        self.table = [None] * self.table_size

    def _calculate_initial_index(self, key):
        return sum(ord(char) for char in key) % self.table_size

    def insert(self, data):
        initial_index = self._calculate_initial_index(data.key)
        for i in range(self.max_collision):
            current_index = (initial_index + i**2) % self.table_size
            if self.table[current_index] is None:
                self.table[current_index] = data
                return
            print(f"collision number {i + 1} at {current_index}")
        print("Max of collisionChain")

    def print_table(self):
        for i, item in enumerate(self.table):
            print(f"#{i+1}\t{item}")


print(" ***** Fun with hashing *****")
input_str = input("Enter Input : ")
config_part, data_part = input_str.split('/')
table_size, max_collision = map(int, config_part.split())
data_list = data_part.split(',')
h = hash(table_size, max_collision)

for item in data_list:
    if all(slot is not None for slot in h.table):
        print("This table is full !!!!!!")
        break
    key, value = item.split()
    data_to_insert = Data(key, value)
    h.insert(data_to_insert)
    h.print_table()
    print("---------------------------")