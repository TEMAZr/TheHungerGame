SOLUZION_VERSION = "0.2"
PROBLEM_NAME = "The Hunger Game"
PROBLEM_VERSION = "alpha beta sigma male 2"
PROBLEM_AUTHORS = ['S. Mahankali', 'Z. Tu', 'A. Willis', 'D. Khani']
PROBLEM_CREATION_DATE = "9-SEP-2022"
PROBLEM_DESC = '\"It is bad for people to starve\" - Michael'

import sys

class State:

    holdwindow = None

    def __init__(self, old = None):
        self.p = 90 # production in a percentage of pop. that could be fed given no waste
        self.wp = 14 # waste after production, before distribution - same units
        self.wd = 5 # waste during distribution/transit - same units
        self.bh = 80 # percent of food distributed that people buy from corporations
        self.ch = 70 # percent of food that people buy, that they eat
        self.m = 1000 # amount of money available - change later
        self.time = 0 # time passed
        self.rocket_truck = False
        if old is not None:
            self.p = old.p
            self.wp = old.wp
            self.wd = old.wd
            self.bh = old.bh
            self.ch = old.ch
            self.m = old.m
            self.time = old.time
            self.rocket_truck = old.rocket_truck
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
        return max(0.01, self.h)

    def move(self, t):
        # global ROOT
        if self.is_goal():
            # holdwindow.destroy()
            # quit()
            # print("killing process")
            sys.exit(1)
        new = State(self)
        new.p += t.dp
        new.wp += t.dwp
        new.wd += t.dwd
        new.bh += t.dbh
        new.ch += t.dch
        new.m -= t.cost
        new.time += t.time
        new.d = new.calc_total_distribution()
        new.w = new.calc_total_waste()
        new.h = new.calc_hunger()
        t.done()
        if not t.can_do_again(): t.set_name("Unavailable") # truth be told, idk if this works, but I figured I'd try it so people don't keep trying to use it from the visual dropdown menu
        if t.times_used == 1: print(t.get_message())
        return new

    def can_move(self, t):
        global task5, task6
        if task5.times_used == 0 and t.name == task6.name: return False
        if not t.can_do_again(): return False
        if self.wp + self.wd + t.dwp + t.dwd > self.p + t.dp: return False
        if self.bh + t.dbh > 100 or self.bh + t.dbh < 0: return False
        if self.ch + t.dch > 100 or self.ch + t.dch < 0: return False
        if t.cost > self.m: return False
        return True

    # \u001b[38;5;##m
    # \u001b[0m
    def __str__(self):
        return f'\n=================\nMoney: {self.m:.2f}\n\
===== Stats =====\nProduction: {self.p:.2f}\nDistribution: {self.d:.2f}\nTotal Waste: {self.w:.2f}\nHunger Rate: {self.h:.2f}'

    def describe_state(self):
        return str(self)

    '''SET THE END TIME lATER!! DO NOT FORGET THIS YOU IDIOT!!!!!'''
    def is_goal(self):
        # figure out how to end game if there are no available tasks
        if self.h <= 35 or self.m <= 200 or self.h >= 90:
            print(self.goal_message())
            return True
        return False

    def __eq__(self, s2):
        if s2 is None: return False
        return str(self) == str(s2)

    def __hash__(self):
        return (str(self)).__hash__()

    def goal_message(self):
        if self.m <= 200: return "lol u broke, it's a skill issue"
        if self.h >= 90: return "the people of the Dennyville Statistical Area found a way to kill god because they hate you so much (it's impressive how they did it while so hungry)"
        return "Dennyville is ever grateful for your contributions! bye lul"

def copy_state(s):
    return State(old=s)

class Task:

    def __init__(self, name, msg, dp, dwp, dwd, dbh, dch, cost, max_times, time):
        self.name = name
        self.msg = msg
        self.dp = dp
        self.dwp = dwp
        self.dwd = dwd
        self.dbh = dbh
        self.dch = dch
        self.cost = cost
        self.time = time
        self.max_times = max_times
        self.times_used = 0

    def set_name(self, name):
        self.name = name

    def can_do_again(self):
        return self.times_used < self.max_times
    
    def done(self):
        self.times_used += 1

    def get_message(self):
        return str(self.msg)

    def __str__(self):
        return str(self.name)

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

# cost is in millions
# (self, name, msg, dp, dwp, dwd, dbh, dch, cost, max_times)

name = "$165: Give silos to farms in need."
msg = "Some small-scale farms do not have access to modern storage equipment, or it is simply too expensive in the short-term. Changes so simple as supplying them with silos can cut their post-harvest losses from 40% to 2%! Thanks to your contribution, less food in Dennyville will go to waste."
task0 = Task(name, msg, 0, -3, 0, 0, 0, 165, 3, 1)
phi0 = Operator(task0.name, lambda s: s.can_move(task0), lambda s: s.move(task0))

name = "$1500: Reconstruct roads near the city"
msg = "Trucking is vital to farms’ success. In the United States, 70% of agricultural and food products travel by truck to their destinations. However, many roads aren’t in the best shape, which hinders transportation, especially of perishable goods. Because you fixed up major roadways in the Dennyville area, less food will be wasted in transit!"
task1 = Task(name, msg, 0, 0, -7, 0, 0, 1500, 1, 10)
phi1 = Operator(task1.name, lambda s: s.can_move(task1), lambda s: s.move(task1))

name = "$50: Ad campaign against household food waste."
msg = "You’ve pestered all of Dennyville with your relentless ads… but maybe that’s a good thing. A lot of people don’t know that households generate 31% of all food waste in industrialized countries. By encouraging Dennyville residents to build habits such as planning meals, eating leftovers, using the freezer to prolong shelf life, and donating excess food, the area has seen a decrease in food waste."
task2 = Task(name, msg, 0, 0, 0, -5, 15, 50, 1, 1)
phi2 = Operator(task2.name, lambda s: s.can_move(task2), lambda s: s.move(task2))

name = "$1000: Provide Dennyville residents with stimulus checks."
msg = "Its effect on better-off individuals is limited, but the stimulus check prompted a significant increase in spending among lower-income residents, who are now able to put more money toward food. Dennyville thanks you for the boost, although some residents still have an issue with “free money.”"
task3 = Task(name, msg, 0, 0, 0, 7, 0, 1000, 1, 0)
phi3 = Operator(task3.name, lambda s: s.can_move(task3), lambda s: s.move(task3))

name = "$100: Provide low-income students with free school lunch."
msg = "School lunch has a surprisingly large impact on hunger, with a 14% reduction in food insufficiency in United States households with one or more children receiving free or reduced-price school lunch. Dennyville’s families are very happy with your choice."
task4 = Task(name, msg, 0, 0, 0, 7, 0, 100, 1, 2)
phi4 = Operator(task4.name, lambda s: s.can_move(task4), lambda s: s.move(task4))

name = "$500: Convince Elon Musk to invent the rocket truck!"
msg = "Rocket trucks are so very fast, but they also liquidate their cargo and sometimes other vehicles. Ironically, with this advance in technology, you’ve caused the trucking industry a great setback and created a whole bunch of food waste. You’re lucky everyone is mad at Elon Musk and not the god that sent him down this wretched path."
task5 = Task(name, msg, 0, 0, 50, 0, 0, 500, 1, 5)
phi5 = Operator(task5.name, lambda s: s.can_move(task5), lambda s: s.move(task5))

name = "$250: Ban the rocket truck..."
msg = "As cool as rocket trucks are, you made the right choice. Maybe now Dennyville can begin to heal. (Though some people still use rocket trucks because they don’t care about the law and they’re too fast to get pulled over.)"
task6 = Task(name, msg, 0, 0, -45, 0, 0, 250, 1, 7)
phi6 = Operator(task6.name, lambda s: s.can_move(task6), lambda s: s.move(task6))

name = "+$500: Offerings to God"
msg = "The people of Dennyville appreciate your effort and raised money to give you more funds. Use them wisely!" 
task7 = Task(name, msg, 0, 0, 0, 5, 0, -500, 5, 2)
phi7 = Operator(task7.name, lambda s: s.can_move(task7), lambda s: s.move(task7))

# TODO: add money operator
# TODO: add other negative operators

TASKS = [task0, task1, task2, task3, task4, task5, task6, task7]
OPERATORS = [phi0, phi1, phi2, phi3, phi4, phi5, phi6, phi7]
