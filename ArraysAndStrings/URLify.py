class URLifier:
	def urlify(self, ls, l):
		# my approach
		shifted_dict={}
		d_20s=[]
		shifted = 0 
		for i in range(0, l):
			if(ls[i]==' '):
				d_20s.append(shifted+i)
				shifted+=2
			else:
				shifted_dict[shifted+i]= ls[i]
		for d in d_20s:
			ls[d:d+3]='%20'
		for d in shifted_dict:
			ls[d]= shifted_dict[d]
		return ls

	def urlify_sol(self, ls, l):
		# the given solution
		cnt_space = 0
		for i in range(0, l):
			if(ls[i]==' '):
				cnt_space+=1
		new_length=l+2*cnt_space
		ni = new_length-1

		for i in range(l-1, -1, -1):
			if(ls[i]==' '):
				ls[ni-2:ni+1]='%20'
				ni-=2
			else:
				ls[ni]=ls[i]
			ni-=1
		return ls


 
if __name__ == '__main__':
	s = "Mr John Smith"
	l = len(s)
	u = URLifier()
	ls = ['']*17 # initialize list long enough to hold the result
	ls[:l]=s
	print(u.urlify(ls, l))
	print(u.urlify_sol(ls, l))