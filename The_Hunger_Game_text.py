SOLUZION_VERSION = "0.2"
PROBLEM_NAME = "The Hunger Game"
PROBLEM_VERSION = "the first one"
PROBLEM_AUTHORS = ['S. Mahankali', 'Z. Tu', 'A. Willis', 'D. Khani']
PROBLEM_CREATION_DATE = "9-SEP-2022"
PROBLEM_DESC = "It is bad for people to starve - Michael"

# TODO: add angy/satisfaction meter >:(

class State:

    def __init__(self, old = None):
        self.p = 90 # production in a percentage of pop. that could be fed given no waste
        self.wp = 14 # waste after production, before distribution - same units
        self.wd = 5 # waste during distribution/transit - same units
        self.bh = 80 # percent of food distributed that people buy from corporations
        self.ch = 70 # percent of food that people buy, that they eat
        self.m = 100 # amount of money available - change later
        self.t = 0 # time passed
        if old is not None:
            self.p = old.p
            self.wp = old.wp
            self.wd = old.wp
            self.bh = old.bh
            self.ch = old.ch
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
        return (self.d-self.calc_corporation_waste()) - (self.d-self.calc_corporation_waste()) * self.ch/100
    
    def calc_total_waste(self):
        self.w = self.wp + self.wd + self.calc_corporation_waste() + self.calc_household_waste()
        return self.w

    def calc_hunger(self):
        self.h = 100 - (self.p - self.w)
        return max(0, self.h)

    def move(self, dp, dwp, dwd, dbh, dch, cost):
        new = State(self)
        new.p += dp
        new.wp += dwp
        new.wd += dwd
        new.bh += dbh
        new.ch += dch
        new.m -= cost
        new.d = new.calc_total_distribution()
        new.w = new.calc_total_waste()
        new.h = new.calc_hunger()
        return new

    def can_move(self, dp, dwp, dwd, dbh, dch, cost):
        if self.wp + self.wd + dwp + dwd > self.p + dp: return False
        if self.bh + dbh > 100 or self.bh + dbh < 0: return False
        if self.ch + dch > 100 or self.ch + dch < 0: return False
        if cost > self.m: return False
        return True

    # \u001b[38;5;##m
    # \u001b[0m
    def __str__(self):
        s = f'Money: {self.m:.2f}\n\u001b[38;5;196m=\u001b[38;5;203m=\u001b[38;5;208m=\u001b[38;5;214m=\u001b[38;5;220m=\u001b[38;5;222m=\u001b[38;5;226m=\u001b[38;5;154m=\u001b[38;5;157m=\u001b[38;5;118m=\u001b[38;5;123m=\u001b[38;5;81m=\u001b[38;5;31m=\u001b[38;5;27m=\u001b[38;5;57m=\u001b[38;5;93m=\u001b[38;5;128m=\u001b[0m\n===== Stats =====\nProduction: {self.p:.2f}\nDistribution: {self.d:.2f}\nTotal Waste: {self.w:.2f}\nHunger Rate: {self.h:.2f}'
        return s

    def describe_state(self):
        return str(self)

    '''SET THE END TIME lATER!! DO NOT FORGET THIS YOU IDIOT!!!!!'''
    def is_goal(self):
        return self.h <= 20 or self.m <= 0

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

  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)

INITIAL_STATE = State()

GOAL_MESSAGE_FUNCTION = lambda s: s.goal_message()

# (self, dp, dwp, dwd, dbh, dch, cost)

phi0 = Operator("Force people to eat their food", lambda s: s.can_move(0, 0, 0, 0, 25, 25),\
    lambda s: s.move(0, 0, 0, 0, 25, 25))

phi1 = Operator("Constant bonfire of usable food", lambda s: s.can_move(0, 0, 0, 0, -20, 50),\
    lambda s: s.move(0, 0, 0, 0, -20, 50))

phi2 = Operator("Better pesticides! :)", lambda s: s.can_move(10, 0, 0, 0, 0, 10),\
    lambda s: s.move(10, 0, 0, 0, 0, 10))

OPERATORS = [phi0, phi1, phi2]

s = State()
print(s)