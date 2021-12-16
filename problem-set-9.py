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

def q1(state,st):
    st.push('$')
    state = 2
    return state,st

def q2(symbol, st):
    err = False
    if symbol == '0':
        st.push('0')
        state = 2
        return state, st, err

    if symbol == '1':
        if st.peek() == '0':
            st.pop()
            state = 3
            return state, st, err

    err = True
    return 'None', 'None', err

def q3(symbol,st):
    if symbol == '1' and st.peek() == '0':
        st.pop()
        state = 3
    if st.peek() == '$':
        state = 4
    return state,st

def q1q4(state,st,F):
    if state == 1:
        return 'Accept'
    print (state)
    if not st.isempty():
        if st.peek() == '$':
            if state in F:
                return "Accept"
    return "Reject"

def process(M,input):
    Q = list(M[0])
    Sigma = M[1]
    q0 = M[3]
    F = M[4]

    st = Stack()

    #init
    state = q0
    if len(input) > 0:
        state, st = q1(q0,st)
        if state not in Q:
            return "Reject"

    #process input
    for symbol in input:
        if symbol not in Sigma:
            return "Reject"
        if state == Q[1]:
            state, st, err = q2(symbol, st)
            if err or state not in Q:
                return "Reject"
            if state == Q[2]:
                state, st = q3(symbol,st)
                if state not in Q:
                    return "Reject"

    #Accept?
    return q1q4(state,st,F)

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



