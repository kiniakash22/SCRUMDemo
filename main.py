from operator import attrgetter

ID = 1 
class Backlog:
    def __init__(self):
        self.listOfItems = []

    def addItem(self, item):
        self.listOfItems.append(item)

    def showAllItemDetails(self):
        for i in range (len(self.listOfItems)):
            self.listOfItems[i].show_item_details()
        
    def showAllSnippets(self):
        for i in range (len(self.listOfItems)):
            self.listOfItems[i].show_item_snippet()

    def showByPriority(self, priority):
        print("\nAll the Requirements with priority '", priority, "' are as follows:", sep="")
        for i in range (len(self.listOfItems)):
            if self.listOfItems[i].priority == priority:
                self.listOfItems[i].show_item_details()

    def showByTimeEstimate(self):
        sorted_list = sorted(self.listOfItems, key=attrgetter("timeEstimate"))
        for item in sorted_list:
            print(item)
        pass


class Item:
    def __init__(self, summary, priority, timeEstimate):
        global ID
        self.summary = summary
        self.priority = priority
        self.timeEstimate = timeEstimate
        self.id = ID
        ID += 1

    def show_item_details(self):
        print("\nRequirement ID:", self.id)
        print("Requirement Summary:", self.summary)
        print("Requirement Priority:", self.priority)
        print("Requirement Time Estimate (in hrs.):", self.timeEstimate)
    
    def __str__(self):
        return ("\nRequirement ID:"+str(self.id)+"\nRequirement Summary:"+str(self.summary)+"\nRequirement Priority:"+str(self.priority)+"\nRequirement Time Estimate (in hrs.):"+str(self.timeEstimate))

    
    def show_item_of_priority(self, priority):
        if self.priority == priority:
            self.show_item_details()

    def show_item_snippet(self):
        print("Item ID:", self.id, "\tSummary: ", self.summary)


#projManName = input("Enter Product Manager's name:")
print("Welcome to SCRUM Demo")


backlog1 = Backlog()


while True:
    print("-"*50,"""\nEnter one of the options from below:\n1. To insert new requirement\n2. To view the entire backlog\n3. Show snippets of all requirements
4. View all requiremnts by selected priority\n5. View all requirements sorted by time (in Asc. order)\n0. Exit""")
    choice = int(input("Enter you choice: "))

    if choice == 1:
        print("-"*50)
        summary = input("Enter Summary of Requirement: ")
        priority = input("Enter Priority of Requirement (A, B, C): ")
        timeEstimate = int(input("Enter Time Estimate of Item (in hrs.): "))
        item1 = Item(summary, priority, timeEstimate)
        backlog1.addItem(item1)
        print("New requirement successfully added with ID: ", ID)
    
    elif choice == 2:
        print("-"*50, "\nAll requirements in the backlog are as follows:")
        backlog1.showAllItemDetails()

    elif choice == 3:
        print("-"*50)
        backlog1.showAllSnippets()

    elif choice == 4:
        print("-"*50)
        priority = input("Enter the priority of the Items which you would like to print (A/B/C): ").upper()
        backlog1.showByPriority(priority)

    elif choice == 5:
        print("-"*50)
        backlog1.showByTimeEstimate()

    elif choice == 0:
        break
