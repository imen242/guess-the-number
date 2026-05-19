import random 
secret_number = random.randint(1,100)
print("welcome to guess the number game!")
print(" i'm thinking of a number between 1 and 100. can you guess it?")
while True :
  guess_str= input("enter you guess: ")
  guess= int(guess_str)
if guess> secret_number:
  print ("your guess is too high. guess again")
elif guess< secret_number:
  print(" your guess is too low. guess again")
else:
  print("congragulations! you guessed the number correctly!!!!")
  break
  
