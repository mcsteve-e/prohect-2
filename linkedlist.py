class LinkedList:
        class Node:
                def __init__(self, payload):
                        self.payload = payload
                        self.next = None

        def __init__(self):
                self.head = None

        def addNode(self, newpayload, where="end"):
                if where == "beginning":
                        node = LinkedList.Node(newpayload)
                        node.next = self.head
                        self.head = node
                else:
                        self.appendAtEnd(newpayload)

        def appendAtEnd(self, newpayload):
                if self.head == None:
                        self.head = LinkedList.Node(newpayload)
                        return
                node = LinkedList.Node(newpayload)
                runner = self.head
                while runner.next != None:
                        runner = runner.next
                runner.next = node

        def printList(self):
                runner = self.head
                while runner != None:
                        print(runner.payload, ", ", sep = "", end = "")
                        runner = runner.next
                print()

        def defFront(self):
                if self.head != None:
                        self.head = self.head.next
                else:
                        return

        def __len__(self):
                count = 0
                runner = self.head
                while runner != None:
                        count += 1
                        runner = runner.next
                return count

        def clear(self):
                self.head = None
                

        def delLast(self):
                runner = self.head
                temp = runner
                while runner.next != None:
                        temp = runner
                        runner = runner.next
                temp.next = None

        def find(self, target):
                runner = self.head
                while runner != None:
                        if runner.payload == target:
                                return runner
                        runner = runner.next
                return None

        def getNth(self, n):
                '''
                return a pointer to the nth node in the list where the first node is 0.
                Return None if the list has fewer than n nodes.
                '''
                assert type(n) is int, "first parameter must be an int"
                count = 0
                runner = self.head
                while runner != None:
                        if count == n:
                                return runner
                        runner = runner.next
                        count += 1
                return None

        def insert_sorted(self, some_new_sturec):
                node = LinkedList.Node(some_new_sturec)
                temp = self.head
                if temp == None:
                        temp = node
                elif temp.payload > node.payload:
                        node.next = self.head
                        self.head = node
                else:
                        prev = self.head
                        runner = self.head.next
                        while runner != None:
                                if node.payload < runner.payload:
                                        break
                                else:
                                        prev = runner
                                        runner = runner.next
                        prev.next = node
                        node.next = runner

if __name__ == "__main__":
        j = LinkedList()
        j.addNode(26, "beginning")
        j.addNode(99, "beginning")
        j.addNode(47, "end")
        j.addNode(344, "end")
        j.printList()
        print (len(j),"nodes")
        print (j.__len__(), "nodes")
        j.delLast()
        j.printList()
        x = LinkedList()
        x.insert_sorted(5465)
        x.insert_sorted(40)
        x.insert_sorted(1)
        x.insert_sorted(26)
        x.insert_sorted(350)
        x.insert_sorted(99)
        x.printList()
        print("Found 26? ",j.find(26))
        print("Found 100? ",j.find(100))
        print("Nth element: ",j.getNth(1).payload)
