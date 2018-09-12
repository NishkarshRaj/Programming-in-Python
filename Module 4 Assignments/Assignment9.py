#Assignment 9

class Store:
    __item_count = 100 #private class variable

    #Adds to count to __item_count
    '''Instance method because transactions are done from individual counters'''
    def addItem(self,count):
        self.__item_count += count

    #Subtracts count from __item_count
    '''Instance method because transactions are done from individual counters '''
    def issueItem(self,count):
        self.__item_count -= count

    #Returns __item_count
    '''Class method because total amount is of the entire store '''
    def getItemCount(self):
        return self.__item_count #cannot directly return private member

counter1 = Store()
counter2 = Store()

#add 2 items from counter 1
counter1.addItem(2)

#issue 1 items from counter 1
counter1.issueItem(1)

#get item count in the store
count = counter1.getItemCount()
print(count)
