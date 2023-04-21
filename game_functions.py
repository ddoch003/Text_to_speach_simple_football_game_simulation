import random
import time
import pyttsx3
from defyning_players_oop_and_announcement import Player

real_madrid_result=0
barcelona_result=0

engine = pyttsx3.init()
engine.setProperty("rate", 180)


def initial_announcement():
    engine.say("This is Denislav Dochev here, good evening and welcome to the first El Clasico of the season. "
               "Real Madrid and Barcelona are ready to enter the field and deliver and unforgettable match. "
               "No injured or suspended players, both teams start with their best. "
               "The winner tonight will top the table.")
    engine.runAndWait()
    engine.stop()

def real_madrid_announcement():
    engine.say(f"Here are the 11 for Real Madrid. Goalkeeper with number {Player.real_madrid_starting_players[0].number} {Player.real_madrid_starting_players[0].name}.")
    engine.say("Defenders.")
    for defender in Player.real_madrid_starting_defenders:
        engine.say(f"Number {defender.number}: {defender.name} - the captain of the team" if defender.is_captain else f"Number {defender.number}: {defender.name}")
    engine.say("Midfielders.")
    for midfielder in Player.real_madrid_starting_midfielders:
        engine.say(
            f"Number {midfielder.number}: {midfielder.name} - the captain of the team" if midfielder.is_captain else f"Number {midfielder.number}: {midfielder.name}")
    engine.say("Forwards.")
    for forward in Player.real_madrid_starting_forwards:
        engine.say(f"Number {forward.number}: {forward.name} - the captain of the team" if forward.is_captain else f"Number {forward.number}: {forward.name}")
    engine.say(f"Head coach: {Player.real_madrid_coach}")
    engine.say("Substitutes.")
    for substitute in Player.real_madrid_substitutes:
        engine.say(f"Goalkeeper: {substitute.name}" if substitute.position=="goalkeeper" else f"{substitute.name}")
    engine.runAndWait()
    engine.stop()

def barcelona_announcement():
    engine.say(
        f"Starting 11 for Barcelona. Goalkeeper with number {Player.barcelona_starting_players[0].number} {Player.barcelona_starting_players[0].name}.")
    engine.say("Defenders.")
    for defender in Player.barcelona_starting_defenders:
        engine.say(
            f"Number {defender.number}: {defender.name} - the captain of the team" if defender.is_captain else f"Number {defender.number}: {defender.name}")
    engine.say("Midfielders.")
    for midfielder in Player.barcelona_starting_midfielders:
        engine.say(
            f"Number {midfielder.number}: {midfielder.name} - the captain of the team" if midfielder.is_captain else f"Number {midfielder.number}: {midfielder.name}")
    engine.say("Forwards.")
    for forward in Player.barcelona_starting_forwards:
        engine.say(
            f"Number {forward.number}: {forward.name} - the captain of the team" if forward.is_captain else f"Number {forward.number}: {forward.name}")
    engine.say(f"Head coach: {Player.barcelona_coach}")
    engine.say("Substitutes.")
    for substitute in Player.barcelona_substitutes:
        engine.say(f"Goalkeeper: {substitute.name}" if substitute.position == "goalkeeper" else f"{substitute.name}")
    engine.runAndWait()
    engine.stop()

def team_in_possession():
    global attacking_team
    global attacking_keeper
    global attacking_defenders
    global attacking_midfielders
    global attacking_forwards
    global defending_team
    global defending_keeper
    global defending_defenders
    global defending_midfielders
    global defending_forwards
    attacking_team=random.choice([Player.real_madrid_starting_players,Player.barcelona_starting_players])
    if attacking_team==Player.real_madrid_starting_players:
        engine.say("Real Madrid in possession.")
        engine.runAndWait()
        engine.stop()
        attacking_keeper=Player.real_madrid_starting_players[0]
        attacking_defenders=Player.real_madrid_starting_defenders
        attacking_midfielders=Player.real_madrid_starting_midfielders
        attacking_forwards=Player.real_madrid_starting_forwards
        defending_team=Player.barcelona_starting_players
        defending_keeper=Player.barcelona_starting_players[0]
        defending_defenders=Player.barcelona_starting_defenders
        defending_midfielders=Player.barcelona_starting_midfielders
        defending_forwards=Player.barcelona_starting_forwards
    else:
        engine.say("Barcelona in possession.")
        engine.runAndWait()
        engine.stop()
        attacking_keeper = Player.barcelona_starting_players[0]
        attacking_defenders = Player.barcelona_starting_defenders
        attacking_midfielders = Player.barcelona_starting_midfielders
        attacking_forwards = Player.barcelona_starting_forwards
        defending_team = Player.real_madrid_starting_players
        defending_keeper = Player.real_madrid_starting_players[0]
        defending_defenders = Player.real_madrid_starting_defenders
        defending_midfielders = Player.real_madrid_starting_midfielders
        defending_forwards = Player.real_madrid_starting_forwards
    return attacking_team

def goal():
    global shooter
    global real_madrid_result
    global barcelona_result
    engine.say(f"{shooter.name} scores!")
    if attacking_team==Player.real_madrid_starting_players:
        real_madrid_result+=1
    else:
        barcelona_result+=1
    engine.say(f"The result is now: Real Madrid {real_madrid_result} - Barcelona {barcelona_result}.")
    engine.runAndWait()
    engine.stop()
    return

def corner():
    global shooter
    global attacking_team
    engine.say("The ball goes for a corner kick.")
    time.sleep(1)
    engine.say("Corner kick taken.")
    engine.runAndWait()
    engine.stop()
    corner_outcome=random.choice([goal,out,ball_clear])
    if corner_outcome==goal:
        shooter=random.choice(attacking_team[1:])
        goal()
    elif corner_outcome==out:
        out()
    elif corner_outcome==ball_clear:
        ball_clear()
    return

def shoot():
    global shooter
    engine.say(f"{shooter.name} shoots!")
    engine.runAndWait()
    engine.stop()
    shot_outcome=random.choice([goal,out,ball_clear,corner])
    if shot_outcome==goal:
        goal()
    elif shot_outcome==ball_clear:
        ball_clear()
    elif shot_outcome==out:
        out()
    elif shot_outcome==corner:
        corner()
    return

def out():
    engine.say(f"The shot goes away from the goal. Out.")
    engine.runAndWait()
    engine.stop()
    return

def ball_clear():
    ball_clearer=random.choice(defending_defenders+defending_midfielders)
    engine.say(f"{ball_clearer.name} clears away from danger.")
    engine.runAndWait()
    engine.stop()
    return

def cross():
    global shooter
    global attacking_team
    global attacking_keeper
    global attacking_defenders
    global attacking_midfielders
    global attacking_forwards
    global defending_team
    global defending_keeper
    global defending_defenders
    global defending_midfielders
    global defending_forwards
    passer=random.choice(attacking_defenders+attacking_midfielders)
    shooter=random.choice(attacking_forwards)
    engine.say(f"{passer.name} delivers to {shooter.name}.")
    engine.runAndWait()
    engine.stop()
    cross_outcome=random.choice([out,ball_clear,shoot])
    if cross_outcome==out:
        out()
    elif cross_outcome==ball_clear:
        ball_clear()
    elif cross_outcome==shoot:
        shoot()
    return

def start_game():
    engine.say("The referee whistles the first signal.")
    engine.runAndWait()
    engine.stop()
    return

def half_time():
    engine.say(f"Half time! The result is: Real Madrid {real_madrid_result} - Barcelona {barcelona_result}.")
    engine.runAndWait()
    engine.stop()
    return

def start_second_half():
    engine.say("Start of the second half.")
    engine.runAndWait()
    engine.stop()
    return

def final_result():
    engine.say("The referee whistles the end of the game.")
    engine.say(f"Final result: Real Madrid {real_madrid_result} - Barcelona {barcelona_result}.")
    if real_madrid_result==barcelona_result:
        engine.say("It's a draw!")
    elif real_madrid_result>barcelona_result:
        engine.say("Real Madrid wins!")
    elif real_madrid_result<barcelona_result:
        engine.say("Barcelona wins!")
    engine.runAndWait()
    engine.stop()
    return