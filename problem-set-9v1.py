'''
Python 3.9
DFA to recognize L
Sigma = {0,1}
L = {s | s is an elememt of Sigma*, every odd position of is 1, length
  of s >= 0}
'''

class Stack:
    def __init__(self):
        self.stk = []

    def push(self, elt):
        self.stk.append(elt)

    def pop(self):
        return self.stk.pop()

    def peek(self):
        return self.stk[-1]

    def isempty(self):
        if len(self.stk) == 0:
            return True
        else:
            return False

    def length(self):
        return len(self.stk)

def q1(input,st):
    #input is empty, accept
    if len(input) == 0:
        return 'Accept', state, st
    #Go to the next state
    st.push('$')
    state = 2
    return 'None',state,st

def q2(symbol, st):
    if symbol == '0':
        st.push('0')
        state = 2
        return 'None', state, st

    if symbol == '1':
        if st.peek() == '0':
            st.pop()
            state = 3
            return 'None', state, st
    
    return 'Reject', 'None', 'None'

def q3(symbol,st):
    if st.peek() == '0':
        st.pop()
    if st.peek() == '$':
        state = 4
    else:
        state = 3

    return 'None', state,st

def q4(state,st):
    if st.peek() == '$':
            return "Accept"
    return "Reject"

def process(M,input):
   
    #initialize
    Q = list(M[0])
    st = Stack()
    condition, state, st = q1(input, st)
    if condition == 'Accept':  #input string is empty
        return 'Accept'

    #process input
    for symbol in input:
        if state == Q[1]:
            print("state: ", state)
            condition, state, st = q2(symbol, st)
            print(symbol)
            print(condition)
            print(state)
            print()
            if condition == 'Reject':
                return "Reject"  #invalid input
        continue
        if state == Q[2]:
            print("state: ", state)
            condition, state, st = q3(symbol,st)
            print(symbol)
            print(condition)
            print(state)
            print()
            if condition =='Reject':
                return "Reject" #invalid input
        
                    
    if state == Q[3]:
        return q4(state,st)
    else:
        return "Reject"
    
def build_PDA():
    Q = {1,2,3,4}
    Sigma = {'0','1'}
    Gamma = {')', '$'}
    delta = "See functions q11\q4, q1 q2,q3"
    q0 = 1
    F = {1,4}
    return (Q,Sigma,delta,q0,F)
    

def main():

    M = build_PDA()
    while(True):
        inp = input("enter a string, enter 'quit' to quit ")
        if inp == 'quit':
            break
        print(process(M,inp))

main()



