class Player:
    real_madrid_starting_players=[]
    real_madrid_starting_defenders=[]
    real_madrid_starting_midfielders=[]
    real_madrid_starting_forwards=[]
    real_madrid_substitutes=[]
    real_madrid_coach="Carlo Ancelotti"
    barcelona_starting_players=[]
    barcelona_starting_defenders=[]
    barcelona_starting_midfielders=[]
    barcelona_starting_forwards=[]
    barcelona_substitutes=[]
    barcelona_coach="Xavi"

    def __init__(self,name,number:int,team,position,is_captain:bool):
        self.name=name
        self.number=number
        self.team=team
        self.position=position
        self.is_captain=is_captain
        self.yellow_card=False
        self.red_card=False
        self.injured=False

        if self.team=="Barcelona":
            if len(Player.barcelona_starting_players)<11:
                Player.barcelona_starting_players.append(self)
                if self.position=="defender":
                    Player.barcelona_starting_defenders.append(self)
                elif self.position=="midfielder":
                    Player.barcelona_starting_midfielders.append(self)
                elif self.position=="forward":
                    Player.barcelona_starting_forwards.append(self)
            else:
                Player.barcelona_substitutes.append(self)
        else:
            if len(Player.real_madrid_starting_players)<11:
                Player.real_madrid_starting_players.append(self)
                if self.position=="defender":
                    Player.real_madrid_starting_defenders.append(self)
                elif self.position=="midfielder":
                    Player.real_madrid_starting_midfielders.append(self)
                elif self.position=="forward":
                    Player.real_madrid_starting_forwards.append(self)
            else:
                Player.real_madrid_substitutes.append(self)

#initiating Real Madrid players
real_madrid_player_1=Player("Tibo Courtois",1,"Real Madrid","goalkeeper",False)
real_madrid_player_2=Player("Daniel Carvajal",2,"Real Madrid","defender",False)
real_madrid_player_3=Player("Eder Militao",3,"Real Madrid","defender",False)
real_madrid_player_4=Player("David Alaba",4,"Real Madrid","defender",False)
real_madrid_player_5=Player("Eduardo Camavinga",12,"Real Madrid","midfielder",False)
real_madrid_player_6=Player("Luka Modric",10,"Real Madrid","midfielder",False)
real_madrid_player_7=Player("Toni Kroos",8,"Real Madrid","midfielder",False)
real_madrid_player_8=Player("Federico Valverde",15,"Real Madrid","midfielder",False)
real_madrid_player_9=Player("Karim Benzema",9,"Real Madrid","forward",True)
real_madrid_player_10=Player("Vinicius Junior",20,"Real Madrid","forward",False)
real_madrid_player_11=Player("Rodrygo",21,"Real Madrid","forward",False)

real_madrid_player_12=Player("Lunin",13,"Real Madrid","goalkeeper",False)
real_madrid_player_13=Player("Mendy",23,"Real Madrid","defender",False)
real_madrid_player_14=Player("Lucas Vasquez",17,"Real Madrid","defender",False)
real_madrid_player_15=Player("Antonio Rudiger",22,"Real Madrid","defender",False)
real_madrid_player_16=Player("Daniel Ceballos",19,"Real Madrid","midfielder",False)
real_madrid_player_17=Player("Marco Asensio",11,"Real Madrid","forward",False)
real_madrid_player_18=Player("Mariano",24,"Real Madrid","forward",False)

#initiating Barcelona players
barcelona_player_1=Player("Andre Ter Stegen",1,"Barcelona","goalkeeper",False)
barcelona_player_2=Player("Araujo",4,"Barcelona","defender",False)
barcelona_player_3=Player("Jules Kounde",23,"Barcelona","defender",False)
barcelona_player_4=Player("Marcos Alonso",17,"Barcelona","defender",False)
barcelona_player_5=Player("Alejandro Balde",12,"Barcelona","defender",False)
barcelona_player_6=Player("Sergio Busquets",5,"Barcelona","midfielder",True)
barcelona_player_7=Player("Franck Kessie",19,"Barcelona","midfielder",False)
barcelona_player_8=Player("Sergi Roberto",20,"Barcelona","midfielder",False)
barcelona_player_9=Player("Robert Lewandowski",9,"Barcelona","forward",False)
barcelona_player_10=Player("Raphinha",20,"Barcelona","forward",False)
barcelona_player_11=Player("Gavi",30,"Barcelona","forward",False)

barcelona_player_12=Player("Pena",13,"Barcelona","goalkeeper",False)
barcelona_player_13=Player("Andreas Christensen",15,"Barcelona","defender",False)
barcelona_player_14=Player("Jordi Alba",18,"Barcelona","defender",False)
barcelona_player_15=Player("Eric Garcia",24,"Barcelona","defender",False)
barcelona_player_16=Player("Pedri",8,"Barcelona","midfielder",False)
barcelona_player_17=Player("Frankie de Jong",21,"Barcelona","midfielder",False)
barcelona_player_18=Player("Ousmane Dembele",7,"Barcelona","forward",False)
barcelona_player_19=Player("Ansu Fati",10,"Barcelona","forward",False)