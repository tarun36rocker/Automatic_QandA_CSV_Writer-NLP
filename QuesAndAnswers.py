import csv
import re

file = open('Input.txt','r', encoding="utf8") #reads the text file
f = file.readlines()

newList = [] #extracts the lines into list
ques='' #used for RE to match question at start of string
ques1='' #used for RE to match question at end of string
quesfin='' #used to hold the actual question
ans='' #used to hold the answer

#used to append and remove the spaces from the sentences into a list
for line in f:
    newList.append(line.strip())
#print(newList)  

with open('finalqanda.csv','w',newline='') as out_file: #write mode into the csv created
    
        writer = csv.writer(out_file)
        writer.writerow(('Questions','Answers'))#first row inserted
        
        for i in newList: #every word in the list 
            if(i==''):#if space encountered in list -> ignore 
                continue
            ques = re.search(pattern="^[0-9]",string=i)#matches start of string with number
            ques1 = re.search(pattern="\?$",string=i)#matches end of string with question mark '?'
            
            if(ques and ques1): #if question is found
                writer.writerow((quesfin,ans)) #write question and answer
                quesfin=i #replace new question
                ans='' #make answer empty again
            else:
                ans=ans+i #append to the answer
                
    