import random
alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
char_sym=["!","@","#","$","%","^","&","*"]
char_min_rec=int(input("How many characters does your password need to be? "))
track=0
new_password=[]
new_password_output=""
while char_min_rec!= 1101:
  new_password.append(alpha[random.randint(0, 25)].upper())
  new_password.append(char_sym[random.randint(0, 7)])
  while track<char_min_rec-4:
    ran=random.randint(0, 3)
    if ran==0:
      new_password.append(alpha[random.randint(0, 25)].upper())
    elif ran==1:
      new_password.append(alpha[random.randint(0, 25)])
    elif ran == 2:
      new_password.append(char_sym[random.randint(0, 7)])
    else:
      new_password.append(str(random.randint(0, 9)))
    track=track+1
  new_password.append(alpha[random.randint(0, 25)])
  new_password.append(str(random.randint(0, 9)))
  for i in new_password:
    new_password_output= new_password_output+i
  print(new_password_output)
  char_min_rec=int(input("How many characters does your password need to be? "))
  track=0
  new_password=[]
  new_password_output=""