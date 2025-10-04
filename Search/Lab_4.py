class Hash:
    def __init__(self, size, max_collision, threshold):
        self.table_size = size
        self.max_collision = max_collision
        self.threshold = threshold
        self.table = [None] * self.table_size
        self.data_count = 0
        self.inserted_keys = []
        print("Initial Table :")
        self.print_table()

    def print_table(self):
        for i, item in enumerate(self.table):
            print(f"#{i+1}\t{item}")
        print("----------------------------------------")

    def add(self, data, is_rehashing=False):
        if not is_rehashing:
            print(f"Add : {data}")
        initial_hash = data % self.table_size
        for i in range(self.table_size):
            index = (initial_hash + i**2) % self.table_size
            if self.table[index] is None:
                self.table[index] = data
                self.data_count += 1
                self.inserted_keys.append(data)
                if not is_rehashing:
                    current_load = (self.data_count / self.table_size) * 100
                    if current_load >= self.threshold:
                        print("****** Data over threshold - Rehash !!! ******")
                        self.rehash()
                return
            else:
                collision_count = i + 1
                print(f"collision number {collision_count} at {index}")

                if not is_rehashing and collision_count >= self.max_collision:
                    print("****** Max collision - Rehash !!! ******")
                    self.rehash()
                    self.add(data, is_rehashing=True)
                    return
                
    def rehash(self):
        keys_to_rehash = self.inserted_keys[:]
        new_size = self.find_next_prime(self.table_size * 2)
        self.table_size = new_size
        self.table = [None] * self.table_size
        self.data_count = 0
        self.inserted_keys = []
        for data in keys_to_rehash:
            self.add(data, is_rehashing=True)

    def is_prime(self,n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def find_next_prime(self,n):
        if n <= 1:
            return 2
        prime = n
        found = False
        while not found:
            prime += 1
            if self.is_prime(prime):
                found = True
        return prime

print(" ***** Rehashing *****")
config_part,data_part = input("Enter Input : ").split("/")
table_size, max_col, threshold = map(int, config_part.split())
data_list = list(map(int, data_part.split()))
hash_table = Hash(table_size, max_col, threshold)
for data in data_list:
    hash_table.add(data)
    hash_table.print_table()