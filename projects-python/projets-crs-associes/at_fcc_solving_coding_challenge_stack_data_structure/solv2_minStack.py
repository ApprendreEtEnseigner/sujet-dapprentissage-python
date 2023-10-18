
class get_min_stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    # push operation in stack
    def push(self, x):
        self.stack.append(x)
        
        if self.min_stack:
            self.min_stack.append(
                min(x, self.stack[-1])
            )
        else:
            self.min_stack.append(x)
            
    # pop operation in stack 
    def pop(self, x):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
        else:
            return -1
    
    # top operation in stack 
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1    
    # min operation in stack
    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1] 
        else:
            return -1
        
        
essai1 =  get_min_stack()

print(essai1.push(2))