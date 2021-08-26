from collections import deque



class stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        return self.container.append(val)

    def pop(self):
        return self.container.pop()

    def print_stack(self):
        return self.container




if __name__=="__main__":

    print("Stack Implemention and push, pop operations!")
    
    new_stack = stack()

    for i in range(11, 21):
        new_stack.push(i)
    
    print(new_stack.print_stack())

    new_stack.pop()

    print(new_stack.print_stack())
    


 
    
