class Cricket:

    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f'Player name: {self.__player} \nPlayer score: {self.__score}')

    def play(self):
        print(f'{self.__player} has scored a sixer.')

    def score_getter(self):
        return self.__score

    def score_setter(self, score2):
        if score2 >= 0:
            self.__score = score2
            print(f'The updated cricket score is: {self.__score}')
        else:
            print('Score cannot be negative')


class Football:

    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f'Player name: {self.__player} \nPlayer score: {self.__score}')

    def play(self):
        print(f'{self.__player} has scored a goal.')

    def score_getter(self):
        return self.__score

    def score_setter(self, score2):
        if score2 >= 0:
            self.__score = score2    
            print(f'The updated football score is: {score2}')
        else:
            print('Score cannot be negative')


# Object instantiation and polymorphism loop
football = Football('Suarez', 3)
kricket = Cricket('Kholi', 6)

for sport in (football, kricket):
    sport.info()
    sport.play()
    print()

# Correctly capturing input and using the setter method
new_score = int(input("Set new score: "))

print(f'The old cricket score was: {kricket.score_getter()}')

kricket.score_setter(new_score)