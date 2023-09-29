class BinarySearchTreeNode:
    def __init__(self,data):
         self.data = data
         self.left = None
         self.right = None

    def add_child(self,data):
         if data == self.data :
              return
         if data < self.data :
              if self.left:
                    self.left.add_child(data)
              else:
                  self.left = BinarySearchTreeNode(data)  
              
         else:
             if self.right :
                    self.right.add_child(data)     
             else:
                 self.right = BinarySearchTreeNode(data)

    def inorderTraversal(self):
       elements = []

       if self.left:
            elements   += self.left.inorderTraversal()
       elements.append(self.data)
        
       if self.right :
           elements+= self.right.inorderTraversal()

       return elements   
    
    def find_min(self):
         if self.left is None :
              return self.data
         return self.left.find_min()

    def find_max(self):
         if self.right is None :
              return self.data
         return self.right.find_max()     

    def search(self,val):
        if val == self.data :
              return True
        elif val < self.data :
              if self.left:
                   return self.left.search(val)
              else:
                   return False
        elif val > self.data :
              if self.right:
                   return self.right.search(val)
              else:
                   return False
  

    def delete(self,val):
        if val < self.data :
            if self.left :
                self.left =self.left.delete(val)
        elif val > self.data :
            if self.right :
                self.right = self.right.delete(val)
        else :
            if self.left is None and self.right is None :
                return None 
            elif self.left is None:
               return self.right
            elif self.right is None:
               return self.left
        if self.right is None: 
            min_val = self.left.find_min() 

            self.data = min_val

            self.left = self.left.delete(min_val)           
        elif self.left is None:  
            min_val = self.right.find_min() 

            self.data = min_val

            self.right = self.right.delete(min_val) 
  
        return self                        




def build_binary_tree(elements):
        root = BinarySearchTreeNode(elements[0])                           

        for i in range(1,len(elements)):
            root.add_child(elements[i])
        return root
if __name__ == '__main__' :
    numbers = [17,1,4,5,2,6,8,99]

    result = build_binary_tree(numbers)    
    
    print(result.inorderTraversal())

    print(result.search(20))
    print(result.search(2))
    result.delete(4)
    print("After deleting element " +  str(result.inorderTraversal()))