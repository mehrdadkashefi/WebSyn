from Webread import Synonym
import time

text_file = open("Text.txt", "r")
text_ignore = open("Textignore.txt", "r")
text_file_Replaced = open("TextReplcaed.txt", "w+")

text  = text_file.read()
textignore = text_ignore.read()
Sent = text.split()

ReplacedSent=[]
for i in range(0,len(Sent)):
    time.sleep(20)
    print("Checking Word # ",i+1,"/",len(Sent))
    # Ask for the Synonym if the word is not in Ignore file
    if textignore.find(Sent[i])!=-1:
        pass
        text_file_Replaced.write(Sent[i]+" ")
        ReplacedSent.append(Sent[i])
    else:
        Syn = Synonym(Sent[i])
        if Syn==0:
            ReplacedSent.append(Sent[i])
            text_file_Replaced.write(Sent[i]+" ")
        else:
            ReplacedSent.append(Syn)
            text_file_Replaced.write(Syn +" ")
            
