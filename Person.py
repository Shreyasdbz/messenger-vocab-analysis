class Person:
    def __init__(self, name_input):
        self.name = name_input
        self.totalWords = 0
        self.uniqueWords = 0
        self.userDict = {}
        
    def doTotals(self):
        for i in self.userDict:
            self.uniqueWords += 1
            self.totalWords += self.userDict[i]
            
    def handleMessage(self, message):
        split = message.split(' ')
        if(len(split) == 0):
            pass
        elif(len(split) == 1):
            self.handleWord(split[0])
        else:
            for w in split:
                self.handleWord(w)
            pass
        
    def handleWord(self, word):
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        word = word.lower()
    
        approved = True
    
        if(len(word) == 1):
            if(word[0] not in alphabets):
                approved = False    
            else:
                pass
        elif(len(word) == 0):
            pass
        else:
            if(word[0] not in alphabets):
                word = word[1:]
            if(word[len(word) - 1] not in alphabets):
                word = word[0:len(word)-2]
            pass

        if(approved == True):
            if word in self.userDict:
                self.userDict[word] += 1
            else:
                self.userDict[word] = 1            
