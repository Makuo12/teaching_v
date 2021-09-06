
#Here is were we instantiate the class

from child_class import BadPlayers, GoodPlayers


player_1:GoodPlayers = GoodPlayers("Makuo","good","6.2inch")

player_2:BadPlayers = BadPlayers("Victor","bad","5.2inch")

if __name__ == "__main__":
   player_1.sayHello()

   player_2.sayHello()
