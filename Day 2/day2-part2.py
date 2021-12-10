with open(r"day2-data.txt") as f:
    commands = [i.strip() for i in f.readlines()]
print("Day 2 Challenge Part 2\n")

class Submarine:
    
    def __init__(self, xpos, ypos, aim):
        self.xpos = xpos
        self.ypos = ypos
        self.aim = aim 
        self.dir_count = 0
    
    def updatePos(self, command):
        comm_dir = command.split(" ")
        direction, dist = comm_dir[0], int(comm_dir[1])

        if direction == "forward":
            self.xpos += dist
            self.ypos += self.aim * dist
        if direction == "up":
            self.aim += dist * -1
        if direction == "down":
            self.aim += dist

        self.dir_count += 1
    
    def printPos(self):
        if self.dir_count % 50 == 0:
            print(f"X Position: {self.xpos}, Y Position: {self.ypos}\n")
        
    def finalAnswer(self):
        print(self.xpos * self.ypos)
        
    
sub = Submarine(0, 0, 0)
for com in commands:
    sub.updatePos(com)
    sub.printPos()

sub.finalAnswer()
