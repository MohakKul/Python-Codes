T = int(input())
for i in range(T):
	N = int(input())
	string = input()
	string = string + "p"
	count = 0
	num = []
	cnt = 0
	if len(string)-1== N:
		count = 0
		num = []
		cnt = 0
		for i in range(0,len(string)):
			if string[i].isdigit():
				count = count + 1
			else:
				if count >= 1:
					cnt = cnt + 1
					count = 0
 
		print(cnt)
