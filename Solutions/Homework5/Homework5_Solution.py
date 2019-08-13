"""
Below are the solutions to Homework 5 which deals with objects and classes
"""

# Question 1
class Computer:
    def __init__(self, name, ram_size, cpu_speed, hdd_size, price):
        self.name = name
        self.ram_size = ram_size
        self.cpu_speed = cpu_speed
        self.hdd_size = hdd_size
        self.price = price

    def __repr__(self):
        return("Computer Info \n" + "Name: " + self.name + "\n" + "Ram size: " + str(self.ram_size) + "\n"
              + "CPU speed: " + str(self.cpu_speed) + "\n" + "HDD size: " + str(self.hdd_size) + "\n"
              + "Price: $" + str(self.price))

    def __eq__(self, other_computer):
        return self.price == other_computer.price

    def __lt__(self, other_computer):
        return self.price < other_computer.price

    def print_name(self):
        print(self.name)

    def print_ram_size(self):
        print(self.ram_size)

    def print_cpu_speed(self):
        print(self.cpu_speed)

    def print_hdd_size(self):
        print(self.hdd_size)

    def print_price(self):
        print(self.price)

    def change_price(self, new_price):
        self.price = new_price


# Question 2
x = Computer("x", 1, 2, 3, 1000)
y = Computer("y", 1, 2, 3, 2000)
print(x == y)
print(x < y)


# Question 3
def get_cheaper_computers(main_computer, other_computers):
    cheaper_computers = []
    for computer in other_computers:
        if computer == main_computer or computer < main_computer:
            cheaper_computers.append(computer)
    return cheaper_computers


"""
For the remaining question solutions will not be provided. You need to think.
"""