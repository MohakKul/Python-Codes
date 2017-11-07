    from sys import stdin
     
    line_index = -1
    lines = stdin.readlines()
     
    def get_line():
    	global lines, line_index
    	
    	line_index += 1
    	return lines[line_index]
     
    t = int(get_line())
    for _ in range(t):
    	n, curr = map(int, get_line().split())
    	stack = [curr]
    	
    	for __ in range(n):
    		p = get_line().split()
    		
    		if p[0] == 'P':
    			stack.append(p[1])
    		elif p[0] == 'B':
    			second = stack.pop()
    			first  = stack.pop()
    			
    			stack.append(second)
    			stack.append(first)
    	
    	print("Player %s" % stack[-1])
