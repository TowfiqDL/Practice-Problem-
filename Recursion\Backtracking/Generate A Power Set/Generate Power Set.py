##Traversing Through the input at each recursive step either we selct an item or choose an empty set. For example, our recursive tree at each branch has two nodes. 

def generate_power_set(elements):
  def helper(indx, currSet, subSets): 
    ##Base Case: if indx is == len(elements) then we have exhaust our current path 
    if indx >= len(elements):
      ##Currset is a global variable
      subSets.append(currset.copy())
      return
    
    currSet.append(elements[i])
    helper(i+1, currSet, subSets)
    currSet.pop()
    helper(i+1, currSet, subSets) 
    
  ##
  currSet, subSets = [], []
  helper(0, currSet, subsets)
  return subSets
