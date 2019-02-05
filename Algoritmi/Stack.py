class Stack:
        array=[]
        number_of_elements = 0
        array_size = 0

        def __init__(self , size):
                self.number_of_elements = 0
                self.array_size=size
                self.array=[]

        def push(self,a):
                if self.array_size==self.number_of_elements:
                        print ("no memory")
                        return
                self.array.append(a)
                self.number_of_elements+=1

        def pop(self):
                if len(self.array)==0:
                        return "Error"
                last = self.array[-1]
                del self.array[-1]
                self.number_of_elements-=1
                return last

st=Stack(5)
st.push(5)
st.push(2)
st.push(1)
st.push(11)
st.push(11)
st.push(4)
st.push(11)
st.push(411)
print(st.array)
print(st.pop())
print(st.pop())
print(st.pop())

