class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def isempty(self):
        return len(self.items)==0

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if self.isempty()==False:
            self.items.pop(self.size() - 1)
   
    def top(self):
        if(self.isempty()==False):
            return self.items[self.size()-1]
        
    def print_stack(self):
        # Print the queue elements
        print("Stack:", " -> ".join(map(str, self.items)))

if __name__ == "__main__":
    st=Stack()
    
    st.print_stack()
    print(st.isempty())
    
    print("Top :",st.top())
    
    



    
    