import csv
class Node():
    def __init__(self , key , point):
        self.key = key
        self.point = point
        self.next = None

class read_file():
    def __init__(self):
        self.list_csv = []
        self.list_key_point = []
    def readCsv(self , file):
        infile = open(file , 'r')
        self.head = next(infile)
        csv_obj = csv.reader(infile)
        for i in csv_obj:
            self.list_csv.append(i)
        infile.close()
    def clean(self):
        for row in self.list_csv:
            self.list_key_point.append(row[0])
            fl = float(row[3])
            self.list_key_point.append(fl)
    def convert(self):
        dictt = {}
        for i in range(0 , len(self.list_key_point) , 2):
            dictt[self.list_key_point[i]] = self.list_key_point[i+1]
        return dictt

class Linkedlist():
    def __init__(self):
        self.head = None
        self.tail = None    
    def addtail(self , key , point):
        new_node = Node(key , point)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
    def mergeSort(self , h):
        if h is None or h.next is None:
            return h
        mid = self.getmid(h)
        next_mid = mid.next
        
        mid.next = None

        left = self.mergeSort(h)
        right = self.mergeSort(next_mid)
        
        sortedd = self.merge(left , right)
        return sortedd
    def getmid(self , h):
        if h == None:
            return h
        slow = h
        fast = h
        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self , left , right):
        result = None
        if left is None:
            return right
        if right is None:
            return left
        if left.point >= right.point:
            result = right
            result.next = self.merge(left , right.next)
        elif right.point >= left.point:
            result = left
            result.next = self.merge(left.next , right)
        return result

    def callmergeSort(self):
        self.head = self.mergeSort(self.head)
    def print_linkedlist(self):
        curr = self.head
        strings = ""
        while curr != None:
            strings += str(curr.key) + " : " + str(curr.point) + "  ->>  "
            curr = curr.next
        print(strings)

if __name__ == '__main__':
    rdcsv = read_file()
    rdcsv.readCsv('/Users/delphi/Desktop/works/python/SU/data.csv')
    rdcsv.clean()
    dictt = rdcsv.convert()
    
    print("Original Dictionary:", dictt)
    ls = Linkedlist()
    for key , point in dictt.items():
        ls.addtail(key , point)
    ls.callmergeSort()
    ls.print_linkedlist() 