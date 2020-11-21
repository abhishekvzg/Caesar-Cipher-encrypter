from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
def cipher(direction, text, shift):
  secret=""
  if(direction=="encode"):
    for char in text:
      ind=alphabet.index(char)
      if((ind+shift)>25):
        ind-=26
      secret+=alphabet[ind+shift]
  elif(direction=="decode"):
    for char in text:
      ind=alphabet.index(char)
      if((ind-shift)<0):
        ind+=26
      secret+=alphabet[ind-shift]
  print("Your encrypted code is: ",secret)
should_end=False
while not should_end:
  direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text=input("Type your message: ")
  shift=int(input("Type the shift number: "))
  print(cipher(direction, text, shift))
  ans=input("Do you want to go again? Type 'yes' or 'no' \n").lower()
  if(ans=="no"):
    print("Good Bye")
    should_end=True
    

