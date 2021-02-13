import random

from replit import clear
from hart import stages
from hart import logo
from wlist import word_list


print(logo)

rword = word_list[random.randint(0 ,len(word_list)-1)]
rworl = []
for i in rword:
    rworl+= i

cword =("")
for i in rworl:
   cword += i +" "

glist = [] 

lw = len(rworl)
for i in range (lw):
    glist += "_"

gword =("")
for i in glist:
        gword += i +" "
print("\n")
print(gword)


life = 6

ulist = [""]

while "_" in glist and life >0:
    utype = input ("\nguess a letter: ").lower()
    clear()
    print(logo)
    print("\n")
    for i in range(lw):
        if rworl[i] == utype:
            glist[i] = utype
    if  utype not in ulist:
        if utype not in rworl:
            life -= 1
            print(f"\nyou have guessed {utype}, that's not in the word. you lose a life")
        else :
            print("\ncorrect guess")
    elif utype == "":
        print("\nyou guessed nothing. please guess.")
    else:
        print(f"\nyou have already guessed {utype}. try again")
    print (f"\n{' '.join(glist)}" )
    print(stages[life])
    # print("\n-----------------------\n")
    ulist += utype
    


if "_" in glist:
    print(f"you lost. the correct word is '{cword}'")
elif life > 0:
    print(f"you win with {life} life")





































# utype = input ("guess a letter : ").lower()

# print (glist)

# def check ():
#     utype = input ("guess a letter : ").lower()

#     for i in range(len(rworl)):
#         let = rworl[i]
#         if let == utype:
#             glist[i] = utype
#     print("\n")
#     print(glist)
    







# def check ():
#     utype = input ("guess a letter : ").lower()

#     for i in range(len(rworl)):
#         let = rworl[i]
#         if let == utype:
#             glist[i] = utype
#     print("\n")
#     print(glist)
    
# life = 6

# print("you have 6 lifes\n")
# while life > 0 :
#     if not "_" in glist:
#         print("you win")
#     else:
#         check()
#         print(stages[arn])
#         print(f"\n{lif} tries left\n")
#     # print (f"arn2is{arn}")


    
    

    
    
        
        

# print (glist)

# while "_" in glist:
#      for i in rword:
#         poz += 1
#         if i == utype:
#             glist[poz-1] = utype
        
















# for i in rword:
#     poz += 1
#     if i == utype:
#         glist[poz-1] = utype
        

# print (glist)





# utype = input ("guess a letter : ").lower()


# glist = [] #glist-guess list

# for w in rword:
#     utype = input ("guess a letter : ").lower()
#     for i in rword:
#         if i == utype:
#     	    # print("right")
#             glist += i
#         else:
#             # print("wrong")
#     	    glist += "_"
#     print (glist)








# for i in rword:
#     if i == utype:
#     	# print("right")
#         glist += i
#     else:
#         # print("wrong")
#     	glist += "_"
# print (glist)
