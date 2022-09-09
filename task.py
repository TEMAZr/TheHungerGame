class Task:

    def __init__(self, name, desc, dp, dd, dw, da, cost, target):
        self.name = name
        self.desc = desc
        self.dp = dp
        self.dd = dd
        self.dw = dw
        self.da = da
        self.cost = cost
        self.target = target
        self.progress = 0
    
    def tick(self):
        self.progress += 1
    
    def done(self):
        return self.progress == self.target

    def __str__(self):
        return f'{self.name}, {self.progress}/{self.target}'
    
t = Task("eat food", "chomp the food", 0, 0, 1, 0, 1, 5)
t.tick()
print(t)