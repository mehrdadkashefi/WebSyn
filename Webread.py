# This program extracts synonym form websites
# Programmer: Mehrdad Kashefi

def Synonym(Vocab):
    # Import libraries
    import subprocess
    import numpy as np
    # Specify the word (Sample Vocab)
    #Vocab = "عشق"
    link = 'https://dictionary.abadis.ir/fatofa/'+Vocab+'/'
    # Browse The online dictionary
    Command = "w3m "+link+" > SynonymDump.txt"
    #print(Command) Printing the command
    subprocess.check_output(["bash","-c",Command])
    # Load the text file
    text_file = open("SynonymDump.txt", "r")
    Fulltext = text_file.read()
    CheckExistance = Fulltext.find("مترادف "+Vocab)
    text_file.close()
    if CheckExistance==-1:
        print("Could not find synonym")
        return 0
    else:
        text_file = open("SynonymDump.txt", "r")
        lines = text_file.readlines()
        for i in range(0,len(lines)):
            Check = lines[i].find("مترادف")
            if Check!=-1:
                SynLine = lines[i]
                SynLine = SynLine.replace('،' ,' ')
                Synonyms = SynLine[8+len(Vocab):len(SynLine)].split()
                # Randomly select one of possible Synonyms
                #SynSelect = Synonyms[round(len(Synonyms)*np.random.uniform())]
                SynSelect = Synonyms[0]
                #print("The selected synonym is ",SynSelect)
                return SynSelect
                break
