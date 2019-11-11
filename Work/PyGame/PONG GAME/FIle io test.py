def write_hiscore(name, score):
    Rfolder = open("HighScore.txt", "rt")
    Rscore = Rfolder.read()
    Rlength = len(Rscore)
    index = Rscore.find(":")
    Rscore = Rscore[index+1:Rlength+1]
   
    if score>Rscore:
        Wfolder = open("HighScore.txt", "wt")
        Wfolder.write(name)
        Wfolder.write(":")
        Wfolder.write(score)
        Wfolder.close()
    #end if
#end procedure



    
    
    
    
    
    
