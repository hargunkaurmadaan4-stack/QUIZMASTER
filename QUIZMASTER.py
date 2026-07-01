
while True :
 a = ("QUIZ MASTER")
 print(a.center(50))
 print("1. Start Quiz")
 print("2. Exit")
 score = 0 
 import random
 str1 = (input("Enter the choice ="))
 if str1 == "1" :
  str3 = (input(''' Choose Question Type :-
                      1. Addition
                      2. Subtraction
                      3. Multiplication
                      4. Square
                      5. Cube
                         = '''))
  if str3 == "1" :
   print("U CHOSSED ADDITION")
  elif str3 == "2" :
   print("U CHOSSED SUBTRACTION")
  elif str3 == "3" :
   print("U CHOSSED MULTIPLICATION")
  elif str3 == "4" :
   print("U CHOSSED SQAURE")
  elif str3 == "5" :
   print("U CHOSSED CUBE")
  else :
   print("enter the number again pls")
  print("Starting Quiz...")
  if str3 == "1" :
   for j in range (1,6):
    n= random.randint(0,20)
    m= random.randint(0,20)
    print("---------------------------------------")
    print (f"Question:{j}")
    print("---------------------------------------")
    print(f"{n} + {m} = ?")
    ans = (int(input("Enter the answer =")))
    if ans == n+m :
     print("🎉 Correct!")
     score = score + 1
    else :
      print(f"❌ Wrong! The correct answer was {n + m}")
  elif str3 == "2" :
   for j in range (1,6):
    n= random.randint(0,20)
    m= random.randint(0,20)
    print("---------------------------------------")
    print (f"Question:{j}")
    print("---------------------------------------")
    print(f"{n} - {m} = ?")
    ans = (int(input("Enter the answer =")))
    if ans == n-m :
     print("🎉 Correct!")
     score = score + 1
    else :
     print(f"❌ Wrong! The correct answer was {n - m}")
  elif str3 == "3" :
   for j in range (1,6):
    n= random.randint(0,20)
    m= random.randint(0,20)
    print("---------------------------------------")
    print (f"Question:{j}")
    print("---------------------------------------")
    print(f"{n} * {m} = ?")
    ans = (int(input("Enter the answer =")))
    if ans == n*m :
     print("🎉 Correct!")
     score = score + 1
    else :
     print(f"❌ Wrong! The correct answer was {n * m}")
  elif str3 == "4" :
   for j in range (1,6):
    n= random.randint(0,20)
    print("---------------------------------------")
    print (f"Question:{j}")
    print("---------------------------------------")
    print(f"{n}^2 = ?")
    ans = (int(input("Enter the answer =")))
    if ans == n**2 :
     print("🎉 Correct!")
     score = score + 1
    else :
     print(f"❌ Wrong! The correct answer was {n**2}")
  elif str3 == "5" :
   for j in range (1,6):
    n= random.randint(0,20)
    print("---------------------------------------")
    print (f"Question:{j}")
    print("---------------------------------------")
    print(f"{n}**3 = ?")
    ans = (int(input("Enter the answer =")))
    if ans == n**3 :
     print("🎉 Correct!")
     score = score + 1
    else :
     print(f"❌ Wrong! The correct answer was {n**3}")
  else :
      print("error")
  print("---------------------------------------")
  print("Quiz Finished Hurrahhh 🎉🎉")
  print("-----------------------------------")
  print(score,"/5")
  if score <= 2 :
   print("U can do better 😓🥲")
  elif score == 3 :
   print("Good effort 😊 ")
  else :
   print("Exellent 🎉")
  print("-----------------------------------")
 elif str1 == "2" :
  print("THANKS FOR USING QUIZ MASTER ")
 else : 
  print("invalid number")

 print('''Do you want to play again?
  1. Yes
   2. No''')
 choice = input("Play Again? (yes/no): ")
 if choice == "no" :
  print("THANKS FOR USING QUIZ MASTER")
  break
