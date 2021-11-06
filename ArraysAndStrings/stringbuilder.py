class StringBuilder:
 def __init__(self):
  self.strs=[]
  self.length = len(self.strs)
  self.cur=0
 def insert(self,word):
  lw = len(word)
  if(self.length<self.cur+lw):
   new_strs = ['']*(self.length*2)
   new_strs[:self.length]=self.strs
   self.length=self.length*2
  self.strs[self.cur:self.cur+lw] = word
  self.cur=self.cur+lw+1


 def ret_str(self):
  return ''.join(self.strs)

if __name__ == '__main__':
    test_str = ["this", "is", "a", "test", "for", "stringbuilder"]

    sb=StringBuilder()

    for t in test_str:
        sb.insert(t)

    print(sb.ret_str())
