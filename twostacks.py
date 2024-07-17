# https://github.com/wize73-ai/W10D2-2.git

class Stacker:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        self.stack1.append(value)
        
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        
    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2[-1]
        
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    queue = Stacker()
    index = 1
    results = []

    for _ in range(q):
        query_type = int(data[index])
        if query_type == 1:
            value = int(data[index + 1])
            queue.enqueue(value)
            index += 2
        elif query_type == 2:
            queue.dequeue()
            index += 1
        elif query_type == 3:
            results.append(queue.peek())
            index += 1
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
