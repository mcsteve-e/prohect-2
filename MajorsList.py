class MajorsList:
    class MajorNode:
        def __init__(self, major):
            self.major = major
            self.StuPtr = None
            self.next = None

    class StuPtrNode:
        def __init__(self, StuRec):
            self.StuRec = StuRec
            self.next = None

    def __init__(self):
        self.head = None

    def print_majors(self):
        runner = self.head
        while runner != None:
            print(runner.major, ", ", sep="", end = "")
            runner = runner.next
        return

    def find_major(self, target):
        runner = self.head
        while runner != None:
            if runner.major == target:
                return runner
            runner = runner.next
        return None
    
    def insert_sorted(self, some_new_major):
        newMajor = MajorsList.MajorNode(some_new_major)
        runner = self.head
        if runner == None:
            self.head = newMajor
        elif newMajor.major < runner.major:
            newMajor.next = runner
            self.head = newMajor
        else:
            prev = runner
            while runner != None and newMajor.major > runner.major:
                prev = runner
                runner = runner.next
            newMajor.next = runner
            prev.next = newMajor
        return

    def insert_student(self, sturec_pointer):
        stu_major = sturec_pointer.major
        someMajor = self.find_major(stu_major)
        if someMajor == None:
            self.insert_sorted(stu_major)
            someMajor = self.find_major(stu_major)
        stu_node = MajorsList.StuPtrNode(sturec_pointer)
        stu_node.next = someMajor.StuPtr
        someMajor.StuPtr = stu_node
        return
    
if __name__ == "__main__":
    Justin = MajorsList()

    Justin.insert_sorted("CSC")
    Justin.insert_sorted("HIS")
    Justin.insert_sorted("DMA")
    Justin.insert_sorted("ABEC")
    Justin.insert_sorted("MAT")


    Justin.print_majors()

