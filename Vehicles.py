print("Select your ride: ")
print("1. Bike")
print("2. Car")
print("3. Aeroplane")
print("4. Train")
#take input of number 1 or 2
#select your ride
choice = int( input("Enter your choice: ") )
#User entering option 1 
if( choice == 1 ): #condition 1 outer if statement
  print( "what type of bike? " )
  print("1.Suzuki Hayabusa\n")
  print("2.Kawasaki Ninja\n")

  #Condition for selecting the type of bike
  choice2=int(input("Enter you choice2: "))
  if choice2==1: #inner if statement
    print("you have selected Suzuki Hayabusa")
  else:
    print("you have selected Kawasaki Ninja")

#User entering option 2
elif( choice == 2 ): #outer elif statement
  print( "what type of car?" )
  print("1.Lamborghini Aventador.")
  print("2.LA Ferrari")
  choice3=int(input("enter your choice3: "))
  if choice3==1: #inner if statement
  #condition for selecting the type of car
    print("you have selected Lamborghini Aventador")
  else:
    print("you have selected LA Ferrari")

elif( choice == 3 ): #outer elif statement
  print( "what type of Aeroplane?" )
  print("1.Boeing 747")
  print("2.Airbus A380")
  choice3=int(input("enter your choice3: "))
  if choice3==1: #inner if statement
  #condition for selecting the type of car
    print("you have selected Boeing 747")
  else:
    print("you have selected Airbus A380")

elif( choice == 4 ): #outer elif statement
  print( "what type of Bus?" )
  print("1.Vande Bharat")
  print("2.Shadabti Express")
  choice3=int(input("enter your choice3: "))
  if choice3==1: #inner if statement
  #condition for selecting the type of car
    print("you have selected Vande Bharat")
  else:
    print("you have selected Shadabti Express")


else: #outer else statement
  print("Wrong choice!")