import game_functions

#Announcements
game_functions.initial_announcement()

#Real Madrid squad
game_functions.real_madrid_announcement()

#Barcelona squad
game_functions.barcelona_announcement()

#Let the game begin!
game_functions.start_game()

for i in range(7):
    game_functions.team_in_possession()
    game_functions.cross()

game_functions.half_time()
game_functions.start_second_half()

for i in range(7):
    game_functions.team_in_possession()
    game_functions.cross()

game_functions.final_result()