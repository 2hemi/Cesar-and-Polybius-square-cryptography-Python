#Library declaration
import string
import numpy as np
import re


#Cesar method

#creating alphabet list with a given rotation order
def cesarCipherBuild(x):
	crypAlphabet = []
	for i in range(0,len(alphabet)):
		if i<len(alphabet)-x:
			crypAlphabet.append(alphabet[i+x])

		else :
			crypAlphabet.append(alphabet[i-len(alphabet)+x])

	return crypAlphabet


#Crypting method 
def cesarCry(txt):
	while True:
		string = ''
		x = input("Give the rotation order : ")
		if x.isnumeric(): #check if X superior than 26 if yes X = X-26
			x = int(x)%26
			if x == 0: 
				print('\nWARNING!! the message gonna stay the same\n')
				string = input("continue(y/n)default no : ")
			if string == 'y' or x != 0:
				crypAlphabet = cesarCipherBuild(x)
				cipherText = ""
				for i in txt:
					if i == " " :
						cipherText += " "
					else :
						cipherText += crypAlphabet[alphabet.index(i)]
				break
			else:
				continue	
		else :
			print('\nERROR!! Please give a number\n')			


	print('\n"""""""""""""""""""\n  >>  "'+cipherText+'"\n"""""""""""""""""""')


#Decrypting method
def cesardecry(txt):
	while True: 
		string = ''
		x = input("Give the rotation order : ")
		if x.isnumeric():
			x = int(x)%26
			if x == 0:  #check if X superior than 26 if yes X = X-26
				print('\nWARNING!! the message gonna stay the same\n')
				string = input("continue(y/n)default no : ")
			if string == 'y' or x != 0:
				crypAlphabet = cesarCipherBuild(x)
				plainTxt =""
				for i in txt:
					if i == " " :
						plainTxt += " "
					else :
						plainTxt += alphabet[crypAlphabet.index(i)] #concatination des alphabet decrypter
				break
			else:
				continue
		else :
			print('\nERROR!! Please give a number\n')
			

	print('\n"""""""""""""""""""\n  >>  "'+plainTxt+'"\n"""""""""""""""""""')


#/***************************************************\

# Polybius Square method

# check if the all the numbers in the text are between 0 and 5
def check(txt):

	for i in txt:
		if int(i) > 5 or int(i)<=0:
			return True
	return False


#Crypting method 
def polybiusCry(txt,ps):

	txt = txt.replace(" ","") #deleting spaces

	cipherText = ""

	for i in txt:
		if i == "i" or i == "j":
			cipherText+=str(24)
		else:
			cipherText += str( np.argwhere(ps == i)+1)  #concatinating numbers
		
	cipherText = cipherText.replace(" ","")  
	cipherText = cipherText.replace("[","")  
	cipherText = cipherText.replace("]","") 
	print('\n"""""""""""""""""""\n  >>  "'+cipherText+'"\n"""""""""""""""""""')


#Decrypting method
def polybiusDecry(txt,ps):

	
	plainText = ""
	cipherText = ""
	for i in txt:
		cipherText += str(int(i)-1)

	cip = [] #list to devide numbers two by two
	for i in range(0,len(cipherText),2):
		cip.append([cipherText[i],cipherText[i+1]]) 

	cip = np.array(cip)
	for i in range(0,len(cip)):
		plainText += str(ps[int(cip[i,0]),int(cip[i,1])])  #convering numbers to letters

	print('\n"""""""""""""""""""\n  >>  "'+plainText+'"\n"""""""""""""""""""')



#/***************************************************\


#Main program

#Polybius Square declaration
arr = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i/j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
PolybiusSquare = arr.reshape(5,5)

#Alphabet declaration
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


while True:
	
	choose = input("\nChoose method : \n 1.Cesar\n 2.Polybius Square \n 3.Exit\n >> ")

	if choose == '1':

		while True:
			
			choose = input("    1.Crypting\n    2.Decrypting \n    3.Exit\n >> ")
			if choose == '1':
				while True:
					plainText = input("\nGive a message to cipher : ")
				
					if re.match('[a-zA-Z\s]+$', plainText):
						plainText = plainText.lower()
						cesarCry(plainText)
						break
					else :
						print('\nERROR!! the message should contain ONLY lettres and spaces\n')
				break

			elif choose == '2':
				while True:
					cipherText = input("\nGive a message to decipher : ")
					if re.match('[a-zA-Z\s]+$', cipherText): 
						cipherText = cipherText.lower()
						cesardecry(cipherText)
						break
					else :
						print('\nERROR!! the message should contain ONLY lettres and spaces\n')
					
				break

			elif choose == '3':
				break

			else :
				print('\nINVALID CHOICE\n')

	elif choose == '2':
		
		while True:
			
			choose = input("    1.Crypting\n    2.Decrypting \n    3.Exit\n >> ")			
			if choose == '1':
				while True:
					plainText = input("\nGive a message to cipher : ")
					if re.match('[a-zA-Z\s]+$', plainText):
						plainText = plainText.lower()
						polybiusCry(plainText,PolybiusSquare)
						break
					else :
						print('\nERROR!! the message should contain ONLY lettres and spaces\n')
						
				break

			elif choose == '2':
				while True:
					
					cipherText = input("\nGive a message to decipher : ")
					if cipherText.isnumeric() == False:
						print("\nERROR!! the message should contain ONLY numbers\n")
					
					elif len(cipherText)%2 == 1: 
						print("\nERROR!! the message length should be divideble by 2\n")

					elif check(cipherText):  
						print("\nERROR!! the numbers in the text sould be between 1 and 5\n")
					else:
						break
				polybiusDecry(cipherText,PolybiusSquare)
				break

			elif choose == '3':
				break
			
			else :
				print('\nINVALID CHOICE\n')

	elif choose == '3':
		break

	else : 
		print('\nINVALID CHOICE\n')
		