class queue:
    def __init__(self):
        self.stack1 = []

    def enqueue(self,x):
        self.stack1.insert(0,x)
        
    def dequeue(self):
        self.stack1.pop()

    def display(self):
        if len(self.stack1) != 0:
            print(self.stack1[-1])

if __name__ == '__main__':
    q = queue()
    for i in range(int(input())):
        option = list(map(int,input().split()))
        if option[0] == 1:
            q.enqueue(option[1])
        elif option[0] == 2:
            q.dequeue()
        else:
            q.display()