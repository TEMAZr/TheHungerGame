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

    def __init__(self, name, msg, res_msg, dp, dwp, dwd, dbh, dch, fix_cost):
        self.name = name
        self.msg = msg
        self.res_msg = res_msg
        self.dp = dp
        self.dwp = dwp
        self.dwd = dwd
        self.dbh = dbh
        self.dch = dch
        self.fix_cost = fix_cost
        self.turns_active = 0

    def add_turn_active(self):
        self.turns_active += 1

    def clear_turns_active(self):
        self.turns_active = 0

    def print_msg(self):
        print(str(self.msg))

    def __eq__(self, c2):
        if c2 is None: return False
        return c2.name == self.name and c2.msg == self.msg and c2.dp == self.dp and c2.dwp == self.dwp and c2.dwd == self.dwd and c2.dbh == self.dbh and c2.dch == self.dch

    def __str__(self):
        return str(self.name)

# Crises - note: numerical parameters are multipliers

name = "Dry Dry Dennyville"
msg = '''Dennyville is experiencing a severe drought, which has become all too common in recent years. Farms are struggling to upkeep their crops, which is making food harder to come by. A lot of people are praying to you right now. Do the right thing!
'''
res_msg = "For the short-term, you mandated that individuals conserve water, and reserved water for struggling farms. For the long-term, you expanded water storage in the region. Dennyville will be uncomfortable until conditions get less dry, but at least it's not a Grade A emergency anymore."
drought = CrisisEvent(name, msg, res_msg, 0.8, 1, 1, 1.10, 1, 300)

name = "Billionaire Blowout!"
msg = '''Dennyville aristocrats are mad they have to pay more in taxes. One billionaire and CEO of [TBD] has threatened to withdraw their company from Dennyville if the taxes aren’t lowered soon.
'''
res_msg = "Well... raising taxes was worth a try, though you did have to influence the Dennyville government to lower them again. By “influence,” I mean bribe. You bribed government officials. Good work."
blowout = CrisisEvent(name, msg, res_msg, 1, 1, 1, 1, 1, 200) # note: it may have no effect now, but this will cause problems down the road if not resolved

name = "Enterprise Exodus"
msg = '''After many long years of business, [TBD] has finally packed up its bags and left Dennyville, leaving many unemployed in its wake. Some families are struggling to put food on the table as a result.
'''
res_msg = "You enticed other companies with fiscal incentives to relocate to or expand in Dennyville, which has helped to fill [TBD]’s void. You also made sure the former [TBD] employees wouldn’t immediately fall into poverty, providing them with temporary unemployment benefits. The government will have to keep a close eye on the situation, and this is by no means a perfect solution, but for now Dennyville’s doing fine considering its great loss."
exodus = CrisisEvent(name, msg, res_msg, 1, 1, 1, 0.85, 1, 300)

name = "Homicidal Hornets"
msg = '''You thought the 2020 plot-writers forgot about murder hornets, didn’t you? Welcome to Season 2! Murder hornets have invaded Dennyville and are steadily taking out the native honeybee population, reducing fertilization of crops.
'''
res_msg = "Lots of murder hornets got into Dennyville, so you had to pour lots of money into a large-scale eradication effort. But, good news - by luring workers with sugar to follow them to their nests and killing queens during their reproductive stage, the Dennyville DoA and many paid volunteers took them all out! Or… *shudder* at least it seems so. The honeybee population is recovering, anyway."
hornets = CrisisEvent(name, msg, res_msg, 0.8, 1, 1, 1, 1, 200)

name = "Surprise Sinkhole"
msg = '''A sinkhole cropped up straight in the middle of Interstate 420, making the route unnavigable and cargo delivery to Dennyville more difficult. This greatly affects the distribution of perishable goods like food.
'''
res_msg = "You brought professionals and construction workers to the scene of the sinkhole to get the road back in order. This was costly but 100% worth it, as people and goods can travel easily and freely to and from Dennyville again."
sinkhole = CrisisEvent(name, msg, res_msg, 1, 1.2, 1, 1, 1, 100)

name = "War Lite"
msg = '''The citizens of Dennyville are outraged that so many of them are hungry and nobody is doing anything about it. They’ve taken to the streets of the city center and, in addition to refusing to purchase food, are literally burning everything down. Many farmers are also on strike and refusing to produce food. Something tells me you should intervene...
'''
res_msg = "You had to round up a whole lot of firefighters, a whole lot of police, and a whole lot of everything in general to put an end to this one outburst. You even had to call in Big Chungus and pay him handsomely for his damage control. But Dennyville’s citizens are still ravenous, and there’s nothing to guarantee its citizens won’t take to the streets again. You’d best start feeding them. That’s the point of this game anyw- oh shoot, I just broke the fourth wall."
war_lite = CrisisEvent(name, msg, res_msg, 0.8, 1, 1, 0.7, 1, 500)

class State:

    holdwindow = None
    last_news = None

    def __init__(self, old = None):
        self.p = 90 # production in a percentage of pop. that could be fed given no waste
        self.wp = 14 # waste after production, before distribution - same units
        self.wd = 5 # waste during distribution/transit - same units
        self.bh = 80 # percent of food distributed that people buy from corporations
        self.ch = 70 # percent of food that people buy, that they eat
        self.m = 1200 # amount of money available - change later
        self.time = 0 # time passed
        self.rocket_truck = False
        self.operMSG = '''Welocome to the Hunger Game! You find yourself in the town of Dennyville.
        This city is in a crisis: hunger rates have spiked to a new high. \nYou, as the god controlling this city, must help the citizens get hunger rates under control. \nYou have various operators at your disposal, all of which cost or give you money. \nHelp Dennyville lower its hunger rate under 35% as fast as possible! \nAs an extra challenge, random crises will occur, especially if the hunger rate is high... Good Luck!'''
        self.crisis = None
        self.crisisMSG = ""
        self.turns_without_crisis = 0
        if old is not None:
            self.p = old.p
            self.wp = old.wp
            self.wd = old.wd
            self.bh = old.bh
            self.ch = old.ch
            self.m = old.m
            self.time = old.time
            self.rocket_truck = old.rocket_truck
            self.operMSG = old.operMSG
            self.crisis = old.crisis
            self.crisisMSG = old.crisisMSG
            self.turns_without_crisis = old.turns_without_crisis
        self.d = 0
        self.calc_total_distribution()
        self.w = 0
        self.calc_total_waste()
        self.h = 0
        self.calc_hunger()
        self.d = min(100,max(0, self.d))
        self.h = min(100,max(0, self.h))
    
    def calc_total_distribution(self):
        self.d = self.p - self.wp - self.wd # food that gets off farms and to corps/retailers
        return max(0, self.d)

    def calc_corporation_waste(self):
        return max(0, self.d - (self.d * self.bh/100))

    def calc_household_waste(self):
        return max(0, (self.d-self.calc_corporation_waste()) - (self.d-self.calc_corporation_waste()) * self.ch/100)
    
    def calc_total_waste(self):
        self.w = self.wp + self.wd + self.calc_corporation_waste() + self.calc_household_waste()
        return min(self.p, max(0, self.w))

    def calc_hunger(self):
        self.h = 100 - (self.p - self.w)
        return max(0.01, self.h)

    def apply_crisis(self):
        if self.crisis is not None and self.crisis.turns_active == 0:
            self.p *= self.crisis.dp
            self.wp *= self.crisis.dwp
            self.wd *= self.crisis.dwd
            self.bh *= self.crisis.dbh
            self.ch *= self.crisis.dch
            self.crisis.add_turn_active()
            self.calc_total_distribution()
            self.calc_total_waste()
            self.calc_hunger()
            self.turns_without_crisis = 0
        elif self.crisis is None: self.turns_without_crisis += 1

    def resolve_crisis(self):
        new = copy_state(self)
        new.p *= 1/self.crisis.dp
        new.wp *= 1/self.crisis.dwp
        new.wd *= 1/self.crisis.dwd
        new.bh *= 1/self.crisis.dbh
        new.ch *= 1/self.crisis.dch
        new.m -= self.crisis.fix_cost
        State.last_news = str(new.crisis.res_msg)
        redraw.Redraw.newsreport(State.holdwindow, State.last_news, 15000)
        new.crisis.clear_turns_active()
        new.crisisMSG = "No crisis at the moment!\n"
        new.operMSG = new.crisis.res_msg
        new.crisis = None
        new.calc_total_distribution()
        new.calc_total_waste()
        new.calc_hunger()
        return new

    def move(self, t):
        # global ROOT
        # print("\033[31;1;4mExecuting move()\033[0m")
        if t == task5: self.rocket_truck = True
        global drought, blowout, exodus, hornets, sinkhole, war_lite
        new = State(self)
        new.p += t.dp
        new.wp += t.dwp
        new.wd += t.dwd
        new.bh += t.dbh
        new.ch += t.dch
        new.m -= t.cost
        new.time += t.time
        new.operMSG = ""
        new.d = new.calc_total_distribution()
        new.w = new.calc_total_waste()
        new.h = new.calc_hunger()
        t.done()
        if t.times_used == 1: print(t.get_message())
        if new.h > 80:
            if random.randint(0, 3) == 0:
                if new.crisis is not None:
                    new.crisis.clear_turns_active()
                new.crisis = war_lite
                new.crisisMSG = new.crisis.msg
        if new.crisis is None:
            if t.name == "+$150: Raise taxes on the top 1%" and t.times_used >= 2:
                if random.randint(0, 2) == 0:
                    new.crisis = blowout
                    new.crisisMSG = new.crisis.msg
            if self.turns_without_crisis >= 3:
                if random.randint(0, 7) == 0:
                    list = [drought, sinkhole, hornets]
                    new.crisis = random.choice(list)
                    new.crisisMSG = new.crisis.msg
        if new.crisis == blowout and new.crisis.turns_active >= 3:
            new.crisis = exodus
            new.crisisMSG = new.crisis.msg
        new.apply_crisis()
        # print("\033[31;1;4mmove() finished\033[0m")
        if new.is_goal()[0]:
            # print("\033[35;1;4mAttempting to close window\033[0m")
            # holdwindow.destroy()
            # quit()
            # print("killing process")
            # sys.exit(1)
            # self.close_window()
            # newwindow = tk.Toplevel(State.holdwindow)
            # newwindow.geometry("500x500")
            # newwindow.title("YEET")
            # redraw.Redraw.soloalert(State.holdwindow,"get rekt", 2000)
            redraw.Redraw.quick_facts(State.holdwindow)
            if new.is_goal()[1].find("broke") != -1 or new.is_goal()[1].find("kill") != -1:
                State.holdwindow.after(1000, lambda:redraw.Redraw.losswindow(State.holdwindow,new.is_goal()[1],10000))
            elif new.is_goal()[1].find("grateful") != -1:
                State.holdwindow.after(1000, lambda:redraw.Redraw.winwindow(State.holdwindow,new.is_goal()[1],10000))
            State.holdwindow.after(10000, State.holdwindow.destroy)
        # if new.crisis is not None:
        #     redraw.Redraw.crisisalert(State.holdwindow, new.crisis)
        State.last_news = str(t.msg)
        redraw.Redraw.newsreport(State.holdwindow,State.last_news,15000)
        if t.name.find("Ban the rocket truck") != -1:
            new.rocket_truck = False
        # if new.rocket_truck == True:
        #     new.rocket_truck = False
        return new

    def can_move(self, t):
        global task5, task6
        # print("\033[31;1;4mExecuting can_move()\033[0m")
        if task5.times_used == 0 and t.name == task6.name: return False
        if not t.can_do_again(): return False
        if self.wp + self.wd + t.dwp + t.dwd > self.p + t.dp: return False
        if self.bh + t.dbh > 100 or self.bh + t.dbh < 0: return False
        if self.ch + t.dch > 100 or self.ch + t.dch < 0: return False
        if t.cost > self.m: return False
        # print("\033[31;1;4mcan_move returning true\033[0m")
        return True

    # \u001b[38;5;##m
    # \u001b[0m
    def __str__(self):
        return f'\n=================\nMoney: {self.m:.2f}\n\
===== Stats =====\n' + f"{f'Production: {self.p:.2f}  |  Distribution: {self.d:.2f}':^45}" + "\n" + f"{f'Total Waste: {self.w:.2f}  |  Hunger Rate: {self.h:.2f}':^45}"

    def describe_state(self):
        return str(self)

    '''SET THE END TIME lATER!! DO NOT FORGET THIS YOU IDIOT!!!!!'''
    def is_goal(self):
        # figure out how to end game if there are no available tasks
        # print("\033[35;1;4mExecuting is_goal()\033[0m")
        if self.h <= 30 or self.h >= 90:
            print(self.goal_message())
            return [True, self.goal_message()]
        elif self.m <= 50:
            if not task8.can_do_again() and not task10.can_do_again():
                print(self.goal_message())
                return [True, self.goal_message()]
        # print("\033[35;1;4mis_goal() returning false\033[0m")
        return [False, self.goal_message()]


    def __eq__(self, s2):
        if s2 is None: return False
        return str(self) == str(s2)

    def __hash__(self):
        return (str(self)).__hash__()

    def goal_message(self):
        if self.m <= 50 and not task8.can_do_again() and not task10.can_do_again(): return "lol u broke, it's a skill issue."
        if self.h >= 90: return '''the people of the Dennyville Statistical Area found a way to kill god because they hate you so much (it's impressive how they did it while so hungry).\n\nget rekt.'''
        if self.h <= 30: return "Dennyville is ever grateful for your contributions! \n\nbye lul."
        return "You haven't won yet!"
    
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

    def __eq__(self, t2):
        return self.name == t2.name and self.msg == t2.msg and self.dp == t2.dp and self.dwp == t2.dwp and self.dwd == t2.dwd and self.dbh == t2.dbh and self.dch == t2.dch

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
msg = '''Some small-scale farms do not have access to modern storage equipment, or it is simply too expensive in the short-term. Changes so simple as supplying them with silos can cut their post-harvest losses from 40% to 2%! Thanks to your contribution, less food in Dennyville will go to waste.'''
task0 = Task(name, msg, 0, -3, 0, 0, 0, 165, 3, 1)
silos = Operator(task0.name, lambda s: s.can_move(task0), lambda s: s.move(task0))

name = "$1200: Reconstruct roads near the city"
msg = '''Trucking is vital to farms’ success. In the United States, 70% of agricultural and food products travel by truck to their destinations. However, many roads aren’t in the best shape, which hinders transportation, especially of perishable goods. Because you fixed up major roadways in the Dennyville area, less food will be wasted in transit!'''
task1 = Task(name, msg, 0, 0, -9, 0, 0, 1200, 1, 10)
roads = Operator(task1.name, lambda s: s.can_move(task1), lambda s: s.move(task1))

name = "$50: Ad campaign against household food waste."
msg = '''You’ve pestered all of Dennyville with your relentless ads… but maybe that’s a good thing. A lot of people don’t know that households generate 31% of all food waste in industrialized countries. By encouraging Dennyville residents to build habits such as planning meals, eating leftovers,using the freezer to prolong shelf life, and donating excess food, the area has seen a decrease in food waste.'''
task2 = Task(name, msg, 0, 0, 0, -5, 15, 50, 1, 1)
ads = Operator(task2.name, lambda s: s.can_move(task2), lambda s: s.move(task2))

name = "$1000: Provide Dennyville residents with stimulus checks."
msg = '''Its effect on better-off individuals is limited, but the stimulus check prompted a significant increase in spending among lower-income residents, who are now able to put more money toward food. Dennyville thanks you for the boost, although some residents still have an issue with “free money.”'''
task3 = Task(name, msg, 0, 0, 0, 7, 0, 1000, 1, 0)
stimulus = Operator(task3.name, lambda s: s.can_move(task3), lambda s: s.move(task3))

name = "$100: Provide low-income students with free school lunch."
msg = '''School lunch has a surprisingly large impact on hunger, with a 14% reduction in food insufficiency in United States households with one or more children receiving free or reduced-price school lunch. Dennyville’s families are very happy with your choice.'''
task4 = Task(name, msg, 0, 0, 0, 7, 0, 100, 1, 2)
lunch = Operator(task4.name, lambda s: s.can_move(task4), lambda s: s.move(task4))

name = "$500: Convince Elon Musk to invent the rocket truck!"
msg = '''Rocket trucks are so very fast, but they also liquidate their cargo and sometimes other vehicles. Ironically, with this advance in technology, you’ve caused the trucking industry a great setback and created a whole bunch of food waste. You’re lucky everyone is mad at Elon Musk and not the god that sent him down this wretched path.'''
task5 = Task(name, msg, 0, 0, 50, 0, 0, 500, 1, 5)
truck = Operator(task5.name, lambda s: s.can_move(task5), lambda s: s.move(task5))

name = "$250: Ban the rocket truck..."
msg = '''As cool as rocket trucks are, you made the right choice. Maybe now Dennyville can begin to heal. (Though some people still use rocket trucks because they don’t care about the law and they’re too fast to get pulled over.)'''
task6 = Task(name, msg, 0, 0, -45, 0, 0, 250, 1, 7)
ban_truck = Operator(task6.name, lambda s: s.can_move(task6), lambda s: s.move(task6))

name = "$70: Donate Usable Food Waste"
msg = '''You have observed that large amounts of usable food are being wasted by corporate policies and overspending by households. You encourage food donations from corporations and households which helps people in need and reduces the amount of food going to landfills.'''
task7 = Task(name, msg, 0, -5, 2, 10, 9, 70, 5, 2)
donate = Operator(task7.name, lambda s: s.can_move(task7), lambda s: s.move(task7))

name = "+$150: Raise taxes on the top 1%"
msg = '''Down with the rich! In order to help the starving population, you elect to add extra taxes on the top 1% of residents, income-wise. This may make them buy a little less food, but you have more funds to use now!'''
task8 = Task(name, msg, 0, 0, 0, 2, 0, -150, 2, 1)
raise_taxes = Operator(task8.name, lambda s: s.can_move(task8), lambda s: s.move(task8))

name = "$100: Mitigate Climate Change Damages"
msg = '''Climate change frequently affects how much food production can be made and disasters can damage infrastructure and homes. By funding repairs of infrastructure, you made a valiant effort to repair climate change effects, but what happens when the next disaster comes through? Better luck slowing climate change instead!'''
task9 = Task(name, msg, 0, 0, 0, 0, 1, 100, 2, 3)
mitigate = Operator(task9.name, lambda s: s.can_move(task9), lambda s: s.move(task9))

name = "+$200: Raise funds for people in need"
msg = '''People need food, but you don’t seem to have the means to help! You look to your beloved subjects for help. Thankfully, they agree that there is a need for action and raise some funds to help your cause. It seems Dennyville has got your back.'''
task10 = Task(name, msg, 0, 0, 0, 0, 0, -200, 2, 4)
raise_funds = Operator(task10.name, lambda s: s.can_move(task10), lambda s: s.move(task10))

name = "$120: Creating more GMOs. They look strange..."
msg = '''One aspect of food waste is the short longevity of food and the refusal of shoppers to buy food over ‘sell by’ dates and if they look strange. You try to preserve food longer by injecting produce with an experimental serum. Now the food looks a bit… alien. Looks like you did the opposite of what you wanted…'''
task11 = Task(name, msg, 0, 15, 0, -10, -5, 120, 2, 5)
gmos = Operator(task11.name, lambda s: s.can_move(task11), lambda s: s.move(task11))

name = "$500: Add wind farm around Dennyville"
msg = '''As god, you encourage all of your disciples, aka the people of Dennyville, that renewable energy is the way of the future! They, of course, agree and install a wind farm on the outskirts of town. The new wind farm is a good way to slow the effects of climate change, prolongs production and bonus, your farmers now have a long term source of income using harvestable wind!'''
task12 = Task(name, msg, 10, 0, 0, 5, 6, 500, 2, 6)
wind_farm = Operator(task12.name, lambda s: s.can_move(task12), lambda s: s.move(task12))

name = "$300: Mechanize food factories"
msg = '''Human error? Why not use robots instead! You decide to mechanize major food production facilities in the Dennyville area, production has increased. But, there are a lot of people out of a job now… Would sustainability be better than more industrial work?'''
task13 = Task(name, msg, 8, 0, 0, -12, 2, 300, 2, 4)
mechanize = Operator(task13.name, lambda s: s.can_move(task13), lambda s: s.move(task13))

name = "$100: Raise grocery tax by 5 percent"
msg = "People don't love having to spend more on essentials like food. For every percent increase in grocery tax, there is a 0.7 percent decrease in overall food spending."
task14 = Task(name, msg, 0, 0, 0, -3.5, 0, 100, 3, 0)
grocery_tax = Operator(task14.name, lambda s: s.can_move(task14), lambda s: s.move(task14))

name = "$300: Shoot Elon Musk into the sun"
msg = "Wow... you really just did that. Sent Elon Musk into the sun to disintegrate in his own invention, the rocket truck. Dennyville's clan of Elon fanboys are in mourning."
task15 = Task(name, msg, 0, 0, 0, 0, 0, 300, 1, 0)
musk_sun = Operator(task15.name, lambda s: s.rocket_truck and s.m >= task15.cost, lambda s: s.move(task15))

resolve_drought = Operator("$300: Resolve Dry Dry Dennyville", lambda s: s.crisis == drought and s.m >= drought.fix_cost, lambda s: s.resolve_crisis())

resolve_hornets = Operator("$200: Resolve Homicidal Hornets", lambda s: s.crisis == hornets and s.m >= hornets.fix_cost, lambda s: s.resolve_crisis())

resolve_sinkhole = Operator("$100: Resolve Sinkhole", lambda s: s.crisis == sinkhole and s.m >= sinkhole.fix_cost, lambda s: s.resolve_crisis())

resolve_blowout = Operator("$200: Resolve Billionaire Blowout", lambda s: s.crisis == blowout and s.m >= blowout.fix_cost, lambda s: s.resolve_crisis())

resolve_exodus = Operator("$300: Resolve Enterprise Exodus", lambda s: s.crisis == exodus and s.m >= exodus.fix_cost, lambda s: s.resolve_crisis())

resolve_war_lite = Operator("$500: Resolve War Lite", lambda s: s.crisis == war_lite and s.m >= war_lite.fix_cost, lambda s: s.resolve_crisis())

# TODO: add money operator
# TODO: add other negative operators

OPERATORS = [raise_funds, raise_taxes, ads, donate, lunch, mitigate, grocery_tax, gmos, silos, ban_truck, mechanize, musk_sun, truck, wind_farm, stimulus, roads, resolve_drought, resolve_hornets, resolve_sinkhole, resolve_blowout, resolve_exodus, resolve_war_lite]