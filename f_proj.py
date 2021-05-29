player = ""

questions = ["Question 8: Durand Cup is associated with the game of ",
 "Question 9: For galvanzing iron which of the following metals is used",
 "Question 10: How many teeth does a normal adult dog have "]
 
answers = [["a)Cricket ", " b)Football ", " c)Hockey ", " d)Volleyball "], 
 ["a)Aluminium ", " b)Copper ", " c)Lead ", " d)Zinc "], 
 ["a)32 ", " b)34 ", " c)38 ", " d)42 "]]

def player(player):
 return "Welcome ", player, "this is the first question is for 2000 ", questions[0]," and its answers are ", answers[0] 


def question1(answer1):
 total_money = 0
 if answer1 == "b":
  total_money += 2000
  print("You won ", total_money)
  print("Next question is for 5000", questions[1]," and its answers are ", answers[1])
 else:
  print("Better luck, next time") 
  
def question2(answer2):
 total_money = 2000
 if answer2 == "d":
  total_money += 5000
  print("Well done, the final question for 10000 is ", questions[2], " and its answers are ", answers[2])
 else:
  print("Better luck, next time") 
  
def question3(answer3):
 total_money = 7000
 if answer3 == "d":
  total_money += 10000
  print("Congratulations you won ", total_money)
 else:
  print("Oh well, you lost, maybe next time") 
 return "Thank u for playing"
 
def players(player1, player2):
 return "Welcome ", player1, "this is the first question and its answers ", questions[0], answers[0]
 



 


def game(question, points, money):
 return("The first question in ", questions[0], " and there are the possible answers ", answers[0])

def score_money(answer):
 total_money = 0
 for point in answer:
  total_money += questions_to_points.get(point, 0)
 return total_money
   
class players:
 def __init__(self, name, money):
  self.name = name
  self.money = money
 
 def 

class questions:
 def _init__(self, question, points):
  self.question = question
  self.points = points

"Question 1: Entomology is the science that studies ": ["a)Behavior of human beings ", " b)Insects ", " c)The origin and history of technical and scientic terms ", " d)The formation of rocks "],
 "Question 2: Galileo was an Italian astronomer who ": ["a)developed the telescope ", " b)discovered four satelites of Jupiter ", " c)discovered that the movement of pendulum ", " d)All of the above "],
 "Question 3: First China War was fought between ": ["a)China and Britain ", " b)China and France ", " c)China and Egypt ", " d)China and Greek "],
 "Question 4: Friction can be reduced by changing from ": ["a)sliding to rolling ", " b)rolling to sliding ", " c)potential energy to kinetic energy ", " d)dynamic to static "],
 "Question 5: Germany signed the Armistice Treaty on ___ and World War I ended ": ["a)January 19, 1918 ", " b)May 30, 1918 ", " c)November 11, 1918 ", " d)February 15, 1918 "],
 "Question 6: Filaria is caused by ": ["a)Bacteria ", " b)Mosquito ", " c)Protozoa ", " d)Virus "],
 "Question 7: Coral reefs in India can be found in ": ["a)the coast of Orissa ", " b)Waltair ", " c)Rameshwaram ", " d)Trivandrum "],
 70000, 85000 , 90000, 25000, 30000, , 45000