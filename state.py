import task as t

class State:

    global wp, wd, bh, ch, money

    wp = 5
    wd = 1
    bh = 70 #% da
    ch = 80 #% bh
    money = 100 #pesos.

    def __init__(self, old = None):
        global wp, wd
        self.p = 90
        self.d = self.calc_distribution()
        self.w = wp + wd + self.calc_corporate_waste() + self.calc_household_waste()
        self.a = 0
        if old is not None:
            self.p = old.p
            self.d = old.d
            self.w = old.w
            self.a = old.a
        self.calc_hunger()

    def is_doable(self, t):
        global money
        return t.cost <= money
    
    def task_comp(self, t):
        self.p += t.dp
        self.d += t.dd
        self.w += t.dw
        self.a += t.da
        
    # calculates da
    def calc_distribution(self):
        global wp, wd
        return self.p - wp - wd

    def calc_corporate_waste(self):
        global bh
        return self.d - (self.d * bh/100)

    def calc_household_waste(self):
        global bh, ch
        return (self.d * bh/100) - (self.d * bh/100 * ch/100)

    def calc_hunger(self):
        self.h = 100 - (self.p - self.w)
        return self.h

    def __str__(self):
        s = f'Production: {self.p}\nDistribution: {self.d}\nTotal Waste: {self.w}\nDirect Aid: {self.a}\nHunger Rate: {self.hunger}'
        return s

class Operator:

  def init(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)

t = t.Task("eat food", "chomp the food", 0, -1, 0, 0, 1, 5)
phi0 = Operator("steal and eat dennyville food", lambda s: s.is_doable(t), lambda s: s.comp_task(t))

t1 = t.Task("eat food", "CHOMP CHOMP CHOMP", 0, -5, 0, 0, 1, 5)
phi1 = Operator("mega chomp", lambda s: s.is_doable(t1), lambda s: s.comp_task(t1))

t2 = t.Task("buy food and don't eat it", "wallet empty", 0, 0, 100, 0, 2, 5)
phi2 = Operator("wasting everything", lambda s: s.is_doable(t2), lambda s: s.comp_task(t2))

OPERATORS = [phi0, phi1, phi2]

s = State()
print(s)
