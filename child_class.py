#this would be the child classes (cubclasses)
#next we import the superclass
from main_class import Characters

class GoodPlayers(Characters):
   
   def __init__(self, name: str, team: str, height: str) -> None:
      super().__init__(name, team, height)
      
class BadPlayers(Characters):
   
   def __init__(self, name: str, team: str, height: str) -> None:
      super().__init__(name, team, height)