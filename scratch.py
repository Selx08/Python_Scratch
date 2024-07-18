def plot1():
    print("Nick : Heyy Buddy!! How have you been these days?\
           Rigel : Oh Hii, I'm good buddy , I haven't seen you since many years where were you?\
           Nick : I was busy ghosting around! It's so nice to see you guys.\n")
    name=input("Nick : By the way who are you? ") #Nick asks to you your name
    print("\nOh Hey , I'm",name,"! Nice to meet you!")
    print("\nWhile the talks continued Nick asked you and Rigel if you guys want to have a meal together")
    choice=input("\nWill you join them to the feast? (yes/no)") #it's your call for the upcoming night
    if(choice=="yes" or choice=="Yes"):
        print("\n*all of them head to the local nearby restaurant*") #here the plot changes to the restaurant where they all find a table for them to eat and drink!
    else:
        ch=input("\nRigel : hey you can't turn us down like that, come with us- (yes/no)")
        if(ch=="yes" or ch=="Yes"):
            print("*all of them head to the local nearby restaurant*") #here the plot changes to the restaurant where they all find a table for them to eat and drink!
        else:
            print("Rigel : Come on man, It's weekend afterall tomorrow\
                  I'm not listening anything you are coming with us that's final!\n") #here after Rigel forcefully takes you to the restaurant to feast!
    return name

def plot2(name):
    print("\n*Walking together , you guys reached a local restaurant and sat on a table the three of you thinking to order some dishes*\n\
          Nick suspiciously took out a box of cigarette from his pocket and gave one to Rigel\n")
    print("\nNick : here you go",name)  #offering you a stick to smoke
    choice=input("\nWill you take the cigarette (yes/no)")
    if(choice=="yes" or choice=="Yes"):
        print("\nThnx for it!")
        return "yes"
    else:
        ch=input("\nRigel : Why not Man, have one with us!! (yes/no)")
        if(ch=="yes" or ch=="Yes"):
            print("\nAlright if you are insisting so much!")
            return "yes"
        else:
            print("\n",name,": Nahh, I'm good.")
            print("\nNick : Come on , we just met today",name)
            ch1=input("\nHave one drink atleast as a toast (yes/no)")
            if(ch1=="yes" or ch1=="Yes"):
                print("\nOkay, But just one drink!!")
                return "yes"
            else:
                print("\n",name,": I'll just skip, I'll be happy to have the dishes with you for our friendship.")
    
    return "no"

def plot3(decision):
    print("\n*After the drinks and dinner everyone reached their home, Having Rigel and Nick partically drunk*\n")
    
    print("\nAfter dropping Rigel his home, when you reached home ,you found that your elder brother was still awake waiting for you.\
      As soon as you reached, you told him about the feast and about Rigel's friend\
      you got late as Rigel was high and helped him reach his home safely\n")
    
    print("\nBrother : On which route you guys met his friend?\
          You : The pull, as the vehicels are not there that time so it is peaceful for a drive\
          Brother : Are you serious that Nick was Rigel's friend?\
          You : Yes,but you'd ask so?\
          Brother : Don't tell me he has a cigarette in his pocket too!!\
          You : Well, that's wierd, How would you know that?")
    
    print("\n*Your elder brother got nervous and hold you tightly while telling you the whole story!*")

    print("\nThere was a guy who'd smoke so much that one day he was murdered because of Claustrophobia\
          He was choked to died by his own cigarette smoke and was never found after that incident.\
          Since then it has become a rumour that who ever finds a guy who has cigarette in his pocket and claims to be your friend out of nowhere,\
          Can be a sign That it's his soul still roaming on the paths of that pull after the sun sets.")
    
    if(decision=="no"):
        print("\nYou : Jesus!! this is so unexpected and scary!!\
              Brother : I hope you haven't smoked or had a drink with him??\
              You : Ohh Noo, I refused it many times!! Thank god I did. But does that mean Rigel will die??\
              Brother : Call him!")
        
        print("\nThe call was not connected and the next morning you get a news that Rigel died!")
    else:
        print("\nYou : Jesus!! Brother i'm scared now!!\
              Brother : I hope you haven't smoked or had a drink with him??\
              You : I DID ,that means I will die too and what about Rigel ??\
              Brother : Holycrap why you'd so do!")
        
        print("\nUntil the next few mins you died and in the morning news comes that Rigel died too!")

    return 0

#Main starts here-
print("\nIt was a dark night when you and your friend Rigel are going out for fun after your 9-5 job work.\n")
print("while walking and talking , you both encounter a person who is a friend of Rigel\n")    
name=plot1()
decision=plot2(name)
plot3(decision)

print("It's not good to have addiction for cigarettes and drinking so much that it can take away your life and happy moments!") #the story ends here