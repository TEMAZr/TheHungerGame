class State:

    def __init__(self, old = None):
        self.p = 90 # production in a percentage of pop. that could be fed given no waste
        self.wp = 14 # waste after production, before distribution - same units
        self.wd = 5 # waste during distribution/transit - same units
        self.bh = 80 # percent of food distributed that people buy from corporations
        self.ch = 70 # percent of food that people buy, that they eat
        self.a = 0 # direct aid
        self.m = 100 # amount of money available - change later
        self.t = 0 # time passed
        if old is not None:
            self.p = old.p
            self.wp = old.wp
            self.wd = old.wp
            self.bh = old.bh
            self.ch = old.ch
            self.a = old.a
            self.m = old.m
            self.t = old.t
        self.d = 0
        self.calc_total_distribution()
        self.w = 0
        self.calc_total_waste()
        self.h = 0
        self.calc_hunger()
    
    def calc_total_distribution(self):
        self.d = self.p - self.wp - self.wd # food that gets off farms and to corps/retailers
        return self.d

    def calc_corporation_waste(self):
        return self.d - (self.d * self.bh/100)

    def calc_household_waste(self):
        return self.calc_corporation_waste() - (self.calc_corporation_waste * self.ch/100)
    
    def calc_total_waste(self):
        self.w = self.wp + self.wd + self.calc_corporation_waste() + self.calc_household_waste()
        return self.w

    def calc_hunger(self):
        self.h = 100 - (self.p - self.w)
        return self.h

    def move(self, dp, dwp, dwd, dbh, dch, da, cost):
        new = State(self)
        new.p += dp
        new.wp += dwp
        new.wd += dwd
        new.bh += dbh
        new.ch += dch
        new.a += da
        new.m -= cost
        return new

    def can_move(self, dp, dwp, dwd, dbh, dch, da, cost):
        if self.wp + self.wd + dwp + dwd > self.p + dp: return False
        if dbh > 100 or dbh < 0 or dch > 100 or dch < 0: return False
        if cost > self.m: return False
        return True

    def __str__(self):
        s = f'Production: {self.p:.2f}\nDistribution: {self.d:.2f}\nTotal Waste: {self.w:.2f}\nDirect Aid: {self.a:.2f}\nHunger Rate: {self.h:.2f}'
        return s

    def describe_state(self):
        return str(self)

    '''SET THE END TIME lATER!! DO NOT FORGET THIS YOU IDIOT!!!!!'''
    def is_goal(self):
        return self.h <= 20

    def __eq__(self, s2):
        if s2 is None: return False
        return str(self) == str(s2)

    def __hash__(self):
        return (str(self)).__hash__()

    def goal_message(self):
        if self.m <= 0: return "lol u broke, it's a skill issue"
        return "Dennyville is ever grateful for your contributions! bye lul"

def copy_state(s):
    return State(old=s)

class Operator:

  def init(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)

INITIAL_STATE = State()

GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)

# (self, dp, dwp, dwd, dbh, dch, da, cost)

phi0 = Operator("eat some food", lambda s: s.can_move(0, 0, 0, 0, 5, 0, 1),\
    lambda s: s.move(0, 0, 0, 0, 5, 0, 1))

phi1 = Operator("BURN SOME FOOD", lambda s: s.can_move(0, 0, 0, 0, -5, 0, 0),\
    lambda s: s.move(0, 0, 0, 0, -5, 0, 0))

phi2 = Operator("Better pesticides! :)", lambda s: s.can_move(10, 0, 0, 0, 0, 0, 10),\
    lambda s: s.move(10, 0, 0, 0, 0, 0, 10))

OPERATORS = [phi0, phi1, phi2]