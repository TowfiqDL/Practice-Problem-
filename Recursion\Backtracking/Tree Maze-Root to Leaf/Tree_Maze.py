## Retrun Boolean(True or False) whether the tree contains any path from root to leaf 

def tree_maze(root): 
  ##Base case 
  if not root or root.value == 0: 
    return False 
  ##Base Case: Leaf Node 
  if not root.left and not root.right: 
    return False
  
  if tree_maze(root.left): 
    return True 
  
  if tree_maze(root.right): 
    return True
  
  return False 
  
  
##Return The Path From Root to Leaf in an array 

def tree_maze(root, path): 
  ##Base case 
  if not root or root.value == 0: 
    return False 
  path.append(root.value)
  ##Base Case: Leaf Node 
  if not root.left and not root.right: 
    return False
  
  if tree_maze(root.left): 
    return True 
  
  if tree_maze(root.right): 
    return True
  
  path.pop()
  return False 
