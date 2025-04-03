import random
import time



number=random.randint(1, 100)

def intro():
    print("Please Enter Your Name!!")

    global name
    name  input()
    print(name + ",This is an number guessing game and  chose any number between 1 to 100")
    if(num%2==0):
        x = 'even'
    else:
        x='odd' 
    print('\nThis is an {} number '.format(x))  
    time.sleep(.5)
    print('Start Guessing !!!!')

def pick():
    guessesTaken = 0

    while guessesTaken < 6:
		time.sleep(.25)
		enter=input("Guess: ") 

        try: 

            guess = int(enter)    

			if guess<=100 and guess>=1: #if they are in range
				guessesTaken=guessesTaken+1 #adds one guess each time the player is wrong
				if guessesTaken<6:
					if guess<number:
						print("The guess of the number that you have entered is too low")
					if guess>number:
						print("The guess of the number that you have entered is too high")
					if guess != number:
						time.sleep(.5)
						print("Try Again!")
                    
                    if guess==number:
						break 


            if guess>100 or guess<1: 
				print("NO! That number isn't in the range!")
				time.sleep(.25)
				print("Please enter a number between 1 and 100")
            
            print("Bro That is not  "+enter+" a number. So")

