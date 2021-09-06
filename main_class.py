#Create three classes a superclass called Characters that will be defined with the following attributes and methods:

#1)Attributes: name,team,height,weight
#2)Methods: sayHello

#this would be the parent class(super class)
class Characters:
   
   #here we intialize the class 
   #this process is called creating the class
   def __init__(self,name:str,team:str,height:str) -> None:
      self.team_types = ["bad","good"]
      self.name = name.lower()
      self.height = height.lower()
      #we want to raise an error if the team enter is not bad or good
      if team not in self.team_types:
         raise ValueError("Please enter whether the team is bad or good")
      self.team = team
   
   #Below we have the say hell function  
   def sayHello(self)->None:
      print(f"Hello, my name is {self.name.title()} and I'm on the {self.team} guys")
         