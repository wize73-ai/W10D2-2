# W10D2-2 two stacks hacker rank

Solving the Queue using Two Stacks Problem

 

Objective:

Improve your problem-solving skills by solving the Queue using Two Stacks problem on HackerRank and documenting your solution approach.

 

Problem Statement:

Solve the HackerRank problem: https://www.hackerrank.com/challenges/queue-using-two-stacks/problem?isFullScreen=trueLinks to an external site.

 

Steps to Complete the Exercise:

Understand the Problem:
   - Carefully read the problem statement.

        A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

        A basic queue has the following operations:

        Enqueue: add a new element to the end of the queue.
        Dequeue: remove the element from the front of the queue and return it.
        In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following  types:

        1 x: Enqueue element  into the end of the queue.
        2: Dequeue the element at the front of the queue.
        3: Print the element at the front of the queue.
        Input Format

        The first line contains a single integer, , denoting the number of queries.
        Each line  of the  subsequent lines contains a single query in the form described in the problem statement above. All three queries start with an integer denoting the query , but only query  is followed by an additional space-separated value, , denoting the value to be enqueued.



   - Identify the inputs and expected outputs.

                    STDIN   Function
            -----   --------
            10      q = 10 (number of queries)
            1 42    1st query, enqueue 42
            2       dequeue front element
            1 14    enqueue 42
            3       print the front element
            1 28    enqueue 28
            3       print the front element
            1 60    enqueue 60
            1 78    enqueue 78
            2       dequeue front element
            2       dequeue front element

                    STDOUT
            14
            14

        Explanation

            Perform the following sequence of actions:

            Enqueue 42
            Dequeue the value at the head of the queue, 42.
            Enqueue 14
            Print the value at the head of the queue,14.
            Enqueue 14,28.
            Print the value at the head of the queue,14.
            Enqueue 60 .
            Enqueue 78.
            Dequeue the value at the head of the queue, 14 .
            Dequeue the value at the head of the queue, 28 .



   - Note the constraints and possible edge cases.

        Constraints

        It is guaranteed that a valid answer always exists for each query of type .
        Output Format

        For each query of type , print the value of the element at the front of the queue on a new line.


Plan Your Approach:
   - Consider different strategies to solve the problem.

   - Choose the most efficient algorithm considering time and space complexity.

   - Outline your solution before coding.

Write the Code:
   - Use your preferred coding environment.

   - Implement your solution clearly and concisely.

   - Use meaningful variable names and comments to explain your code.

Test Your Solution:
   - Test your code with various test cases, including edge cases.

   - Ensure your solution passes all test cases on HackerRank.

Document Your Solution:
   - Create a documentation file in PDF or Markdown format.

   - Explain your code design choices.

        boilerplate stacker class from classwork environment

        logic:

            the input is read and split into list of strings
            perform each numerical task in order decoding the task instruction and pass it to boilerplate
            the STDOUT is only for peek, considered print statement in class or logic, chose logic to preserve boilerplate

   - Describe any specific algorithms or data structures used.

        Why Use Two Stacks?
            Efficient Enqueue and Dequeue Operations:

            Enqueue (push operation): Adding elements to a stack is O(1) in time complexity.
            Dequeue (pop operation): Removing elements from a stack is also O(1) in time complexity.

   - Detail your approach and reasoning for solving the problem.

Submit Your Solution:
   - Ensure your solution passes the HackerRank submission.

        see attached screenshot in repo 

   - Submit your documentation and HackerRank solution via HackerRank.






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







