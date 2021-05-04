import os
import json
from Person import Person
from Message import Message


                 
#==================================================================================== 
# Filters out unwarranted text/content like links and also unknown users
# Input: text content
# Output Pass/Fail , filtered content
#==================================================================================== 
def filterMessageContent(sender, content):
    filterPass = True
    return filterPass


#==================================================================================== 
# Addes the sender to the peoplelist if not there already                         
#==================================================================================== 
def handleMesage(sender, content, peopleList_input, addedPeople_input):
    
    peopleList = peopleList_input
    addedPeople = addedPeople_input
    
    if sender in addedPeople:
        for p in peopleList:
            if(p.name == sender):
                p.handleMessage(content)
    else:
        addedPeople.append(sender)
        peopleList.append(Person(sender))
   
    return peopleList, addedPeople



#==================================================================================== 
#==================================================================================== 
# Returns a prepared list of people (with Person objects) that contains the full dictionary with counts
# Input: NA
# Output: peopleList <type: Person>
#==================================================================================== 
#==================================================================================== 
def doParsing(self):
    
    peopleList = []
    addedPeople = []
    messageList = []
    
    #-----------------------------------------------------------------------
    # Get all the conversation history files
    #----------------------------------------------------------------------- 
    fileNames = []
    for i in os.listdir("data/"):
            if i.endswith('.json'):
                fileNames.append(i)
                

    #-----------------------------------------------------------------------
    # Start importing messages
    #----------------------------------------------------------------------- 
    for f in fileNames:
        filePath = "data/" + f
        
        with open(filePath) as fp:
            data = json.load(fp)
            
            # Read messages
            for message in data['messages']:
                sender = None
                content = ""
                
                for msgData in message:
                    if(msgData == "sender_name"):
                        sender = message[msgData]
                    if(msgData == "content"):
                        content = message[msgData]
                
                if(filterMessageContent(sender, content) == True):
                    peopleList, addedPeople = handleMesage(sender, content, peopleList, addedPeople)
                    pass
                
                                    
       