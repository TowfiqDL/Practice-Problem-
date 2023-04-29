##Tower of Hanoi Problem 
##hanoi(num_rings, start, end) -> hanoi(3, 1, 3)
##Expected Outputs: 1->3, 1->2, 3->2, 1->3, 2->1, 2->3, 1->3 

def towerHanoi(num_rings, start, end): 
  ##Base case: if number of rings == 0 
  if num_rings == 0: 
    return
  other = 6 - (start+end) 
  towerHanoi(num_rings - 1, start, other) 
  print(f'{start} -> {end}')
  towerHanoi(num_rings - 1, other, end) 
  
##With Visualization 
##Pegs list at the start : [[3, 2, 1], [], []]
##Pegs lsit at the end : [[], [], [3, 2, 1]]

num_pegs = 3
def towerOfHanoi(num_rings): 
  ##from_pegs : initial position, from_pegs : final destination, use_pegs : intermediate rod
  def helper(num_rings, from_pegs, to_pegs, use_pegs):
    if num_rings > 0: 
      helper(num_rings - 1, from_pegs, use_pegs, to_pegs)
      pegs[to_pegs].append(pegs[use_pegs])
      result.append([from_pegs, to_pegs]) 
      helper(num_rings - 1, use_pegs, to_pegs, from_pegs) 
  
  result = []
  pegs = [list(reversed(range(1, num_rings+1)] + [[] for _ in range(1, num_pegs)]
  helper(num_rings, 0, 2, 1) 
  return result 
                        
 
