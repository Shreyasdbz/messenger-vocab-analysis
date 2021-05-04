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
            
    def handleMessage(message):
        pass   
        
    def handleWord(word):
        pass