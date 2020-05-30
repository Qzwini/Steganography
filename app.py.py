import cv2
import string
import os
d={}
c={}

for i in range(255):
    d[chr(i)]=i
    c[i]=chr(i)
  

pic = input("Enter Pic name : ")
x=cv2.imread(pic)
i=x.shape[0]
j=x.shape[1]
print(i,j)


# encrip
key=input("Enter key to edit(Security Key) : ")
text=input("Enter text to hide : ")

kl=0
tln=len(text)
z=0 #decides plane
n=0 #number of row
m=0 #number of column
l=len(text)

for i in range(l):
    x[n,m,z]=d[text[i]]^d[key[kl]]
    n=n+1
    m=m+1
    m=(m+1)%3 #this is for every value of z , remainder will be between 0,1,2 . i.e G,R,B plane will be set automatically.
                #whatever be the value of z , z=(z+1)%3 will always between 0,1,2 . The same concept is used for random number in dice and card games.
    kl=(kl+1)%len(key)
    
cv2.imwrite("stph.jpg",x) 
os.startfile("stph.jpg")
print("Data Hiding in Image completed successfully photo name is stph.")
#x=cv2.imread(“encrypted_img.jpg")
    




# decrp
ch = int(input("\n\nEnter 1 to extract data from Image : "))
kl=0
tln=len(text)
z=0 #decides plane
n=0 #number of row
m=0 #number of column

if ch == 1:
    key1=input("\nEnter key to extract text : ")
    decrypt=""
    if key1 :
        for i in range(l):
            decrypt+=c[x[n,m,z]^d[key1[kl]]]
            n=n+1
            m=m+1
            m=(m+1)%3
            kl=(kl+1)%len(key1)
        print("Encrypted text was : ",decrypt)
    else:
        print("Key doesn't matched.")
else:
    print("Thank you. EXITING.")
   

    
    
 
    
    
    