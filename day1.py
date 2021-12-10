# day 1 challenge
with open('part1-data.txt') as f:
    depths = [int(i.strip()) for i in f.readlines()]
    
# part 1 
increases = sum([1 if depths[i]>depths[i-1] else 0 for i in range(len(depths)) if i != 0])

# part 2
window_increases = sum([1 if sum(depths[i-1:i+2])>sum(depths[i-2:i+1]) else 0 for i in range(len(depths)) if (i > 1 and i != len(depths)-1)])
