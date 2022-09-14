SOLUZION_VERSION = "0.2"
PROBLEM_NAME = "The Hunger Game"
PROBLEM_VERSION = "alpha beta sigma chad male 3"
PROBLEM_AUTHORS = ['S. Mahankali', 'Z. Tu', 'A. Willis', 'D. Khani']
PROBLEM_CREATION_DATE = "9-SEP-2022"
PROBLEM_DESC = '\"It is bad for people to starve\" - Michael'

import Tk_SOLUZION_Client3 as tks3
import tkinter as tk
import sys
import random
import redraw

class CrisisEvent:

    def __init__(self, name, msg, dp, dwp, dwd, dbh, dch):
        self.name = name
        self.msg = msg
        self.dp = dp
        self.dwp = dwp
        self.dwd = dwd
        self.dbh = dbh
        self.dch = dch
        self.active = False
        self.turns_active = 0

    def activate(self):
        self.active = True

    def resolve(self):
        self.active = False

    def add_turn_active(self):
        self.turns_active += 1

    def __eq__(self, c2):
        return c2.name == self.name and c2.msg == self.msg and c2.dp == self.dp and c2.dwp == self.dwp and c2.dwd == self.dwd and c2.dbh == self.dbh and c2.dch == self.dch

    def __str__(self):
        return str(self.name)

# Crises - note: numerical parameters are multipliers

name = "Dry Dry Dennyville"
msg = "Dennyville is experiencing a severe drought, which has become all too common in recent years. Farms are struggling to upkeep their crops, which is making food harder to come by. A lot of people are praying to you right now. Do the right thing!"
crisis0 = CrisisEvent(name, msg, 0.7, 1, 1, 1.20, 1)

name = "Billionaire Blowout!"
msg = "Dennyville aristocrats are mad they have to pay more in taxes. One billionaire and CEO of [TBD] has threatened to withdraw their company from Dennyville if the taxes aren’t lowered soon."
crisis1 = CrisisEvent(name, msg, 1, 1, 1, 1, 1) # note: it may have no effect now, but this will cause problems down the road if not resolved in 5 years

name = "Enterprise Exodus"
msg = "After many long years of business, [TBD] has finally packed up its bags and left Dennyville, leaving many unemployed in its wake. Some families are struggling to put food on the table as a result."
crisis2 = CrisisEvent(name, msg, 1, 1, 1, 0.9, 1)

name = "Homicidal Hornets"
msg = "You thought the 2020 plot-writers forgot about murder hornets, didn’t you? Welcome to Season 2! Murder hornets have invaded Dennyville and are steadily taking out the native honeybee population, reducing fertilization of crops."
crisis3 = CrisisEvent(name, msg, 0.8, 1, 1, 1, 1)

name = "Sinkhole!"
msg = "A sinkhole cropped up straight in the middle of Interstate 420, making the route unnavigable and cargo delivery to Dennyville more difficult. This greatly affects the distribution of perishable goods like food."
crisis4 = CrisisEvent(name, msg, 1, 1.2, 1, 1, 1)

name = "War Lite"
msg = "The citizens of Dennyville are outraged that so many of them are hungry and nobody is doing anything about it. They’ve taken to the streets of the city center and, in addition to refusing to purchase food, are literally burning everything down. Many farmers are also on strike and refusing to produce food. Something tells me you should intervene..."
crisis5 = CrisisEvent(name, msg, 0.8, 1, 1, 0.7, 1)

CRISES = [crisis0, crisis1, crisis2, crisis3, crisis4, crisis5]

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

    def apply_crises(self):
        global CRISES
        for c in CRISES:
            if c.active:
                c.add_turn_active()
            if c.turns_active == 1:
                self.p *= c.dp
                self.wp *= c.dwp
                self.wd *= c.dwd
                self.bh *= c.dbh
                self.ch *= c.dch

    def resolve_crisis(self, crisis):
        global CRISES
        new = copy_state(self)
        new.p *= 1/crisis.dp
        new.wp *= 1/crisis.dwp
        new.wd *= 1/crisis.dwd
        new.bh *= 1/crisis.dbh
        new.ch *= 1/crisis.dch
        for c in CRISES:
            if c == crisis:
                c.resolve()
                c.turns_active = 0
        new.calc_total_distribution()
        new.calc_total_waste()
        new.calc_hunger()
        return new

    def move(self, t):
        # global ROOT
        global CRISES
        if self.is_goal():
            # holdwindow.destroy()
            # quit()
            # print("killing process")
            # sys.exit(1)
            # self.close_window()
            # newwindow = tk.Toplevel(State.holdwindow)
            # newwindow.geometry("500x500")
            # newwindow.title("YEET")
            redraw.Redraw.soloalert(State.holdwindow, "You LOSE")
        if random.randint(0, 0) == 0: #0, 10
            # c = random.choice(CRISES)
            c = CRISES[0]
            c.activate()
            print(str(c.msg))
        self.apply_crises()
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
        if self.h <= 20 or self.m <= 200 or self.h >= 90:
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
    
    @staticmethod
    def give_window(window):
        State.holdwindow = window

    def close_window(self):
        State.holdwindow.destroy()

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

name = "$70: Donate Usable Food Waste"
msg = "You have observed that large amounts of usable food are being wasted by corporate policies and overspending by households. You encourage food donations from corporations and households which helps people in need and reduces the amount of food going to landfills."
task7 = Task(name, msg, 0, -5, 2, 10, 9, 70, 5, 2)
phi7 = Operator(task7.name, lambda s: s.can_move(task7), lambda s: s.move(task7))

name = "+$100: Raise taxes on the top 1%"
msg = "Down with the rich! In order to help the starving population, you elect to add extra taxes on the top 1% of residents, income-wise. This may make them buy a little less food, but you have more funds to use now!" 
task8 = Task(name, msg, 0, 0, 0, -2, 0, -100, 2, 1)
phi8 = Operator(task8.name, lambda s: s.can_move(task8), lambda s: s.move(task8))

name = "$100: Mitigate Climate Change Damages"
msg = "Climate change frequently affects how much food production can be made and disasters can damage infrastructure and homes. By funding repairs of infrastructure, you made a valiant effort to repair climate change effects, but what happens when the next disaster comes through? Better luck slowing climate change instead!" 
task9 = Task(name, msg, 0, 0, 0, 0, 1, 100, 2, 3)
phi9 = Operator(task9.name, lambda s: s.can_move(task9), lambda s: s.move(task9))

name = "+$200: Raise funds for people in need"
msg = "People need food, but you don’t seem to have the means to help! You look to your beloved subjects for help. Thankfully, they agree that there is a need for action and raise some funds to help your cause. It seems Dennyville has got your back." 
task10 = Task(name, msg, 0, 0, 0, 4, 3, -200, 3, 4)
phi10 = Operator(task10.name, lambda s: s.can_move(task10), lambda s: s.move(task10))

name = "$120: Creating more GMOs. They look strange..."
msg = "One aspect of food waste is the short longevity of food and the refusal of shoppers to buy food over ‘sell by’ dates and if they look strange. You try to preserve food longer by injecting produce with an experimental serum. Now the food looks a bit… alien. Looks like you did the opposite of what you wanted…" 
task11 = Task(name, msg, 0, 15, 0, -10, -5, 120, 2, 5)
phi11 = Operator(task11.name, lambda s: s.can_move(task11), lambda s: s.move(task11))

name = "$500: Add wind farm around Dennyville"
msg = "As god, you encourage all of your disciples, aka the people of Dennyville, that renewable energy is the way of the future! They, of course, agree and install a wind farm on the outskirts of town. The new wind farm is a good way to slow the effects of climate change, prolongs production and bonus, your farmers now have a long term source of income using harvestable wind!" 
task12 = Task(name, msg, 10, 0, 0, 5, 6, 500, 2, 6)
phi12 = Operator(task12.name, lambda s: s.can_move(task12), lambda s: s.move(task12))

name = "$300: Mechanize food factories"
msg = "Human error? Why not use robots instead! You decide to mechanize major food production facilities in the Dennyville area, production has increased. But, there are a lot of people out of a job now… Would sustainability be better than more industrial work?" 
task13 = Task(name, msg, 8, 0, 0, -12, 2, 300, 2, 4)
phi13 = Operator(task13.name, lambda s: s.can_move(task13), lambda s: s.move(task13))

phi14 = Operator("Resolve Dry Dry Dennyville", lambda s: True, lambda s: s.resolve_crisis(crisis0))

# TODO: add money operator
# TODO: add other negative operators


TASKS = [task0, task1, task2, task3, task4, task5, task6, task7,\
     task8, task9, task10, task11, task12, task13] 
OPERATORS = [phi0, phi1, phi2, phi3, phi4, phi5, phi6, phi7,\
    phi8, phi9, phi10, phi11, phi12, phi13, phi14]