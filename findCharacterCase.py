#Question link is given below
#https://www.codingninjas.com/studio/problems/find-character-case_58513?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

#solution
alphabet = input("")

 

if alphabet.isalnum() and alphabet.isupper():

  print(1)

elif alphabet.isalnum() and alphabet.islower():

  print(0)

else:

  print(-1)