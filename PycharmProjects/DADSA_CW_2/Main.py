# Initalizing Patient class
class Patient():
    global feeding, grv, issue
    def __init__(self):
        self.items = self
        self.items.feeding = [[0] * 24 for i in range(24)]
        self.items.grv = [[0] * 24 for i in range(24)]
        self.items.issue = [[0] * 24 for i in range(24)]
    def getFeedingStatus(self,day,hr):
        return self.items.feeding[day][hr]
    def setFeedingStatus(self,day,hr,value):
        self.items.feeding[day][hr] = value
    def getGRVStatus(self,day,hr):
        return self.items.grv[day][hr]
    def setGRVStatus(self,day,hr,value):
        self.items.grv[day][hr] = value
    def getIssueStatus(self,day,hr):
        return self.items.issue[day][hr]
    def setIssueStatus(self,day,hr,value):
        self.items.issue[day][hr] = value
class List():
    def __init__(self):
        self.items = []
    def add(self,item):
        self.items.append(item)
    def size(self):
        return len(self.items)
    def removeAt(self,i):
        self.items.remove(self.items[i])
PA1 = Patient()
for i in range(0,4):
    for k in range(0,24):
        PA1.setFeedingStatus(i,k,"Hello World")
        print("Feeding Status Day ",i + 1," Hr ",k," Value ",PA1.getFeedingStatus(i,k))
