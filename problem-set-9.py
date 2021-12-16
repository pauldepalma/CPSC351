'''
Python 3.9
DFA to recognize L
Sigma = {0,1}
L = {0^i1^i | i >= 0} 
A PDA is a 6-tuple:
    Q is the set of states
    Sigma is the input alphabet
    Gamma is the stack alphabet
    delta: Q X Sigma X Gamma --> P(Q X Gamma)
    q1 is an element of Q and is the start state
    F is a subset of Q and contains the accept states
'''

#Auxilary functions and Stack class
def no_inp(inp):
    if len(inp) == 0:
        return True
    else:
        return False

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
    
def build_PDA():
    Q = ['q1','q2','q3','q4']
    Sigma = {'0','1'}
    Gamma = {'0', '1', '$'}
    delta = 'Q X Sigma X Gamma --> P(Q X Gamma)'
    q1 = Q[0]
    F = {'q1','q4'}
    return (Q,Sigma,Gamma,delta,q1,F)

def simulate(PDA,inp):
    Q = PDA[0]
    Sigma = PDA[1]
    Gamma = PDA[2]
    q1 = PDA[4]  # start state
    q2 = Q[1]
    q3 = Q[2]
    q4 = Q[3]
    F = PDA[5]

    #init
    idx = 0 #index into the input string
    state = q1 
    stk = Stack()

    #in state q1
    if no_inp(inp) and state in F:
        return "Accept"
    
    #go to state q2
    if inp[idx] not in Sigma:
        return 'Reject'
    if state == q1:
        stk.push('$')
        state = q2

    #in state q2
    if inp[idx] not in Sigma:
        return 'Reject'
    while(idx < len(inp) and inp[idx] == '0'):  
        stk.push('0')
        idx = idx + 1
    if idx == len(inp): #no 1s
       return 'Reject'
    state = q3

    #go to state q3
    #pop the stack
    if inp[idx] not in Sigma:
        return 'Reject'
    if stk.peek() != '0':  #no 0s have been pushed 
        return 'Reject'
    if inp[idx] == '1' and stk.peek() == '0':
        stk.pop()
        idx = idx + 1
    state = q3

    #in state q3
    if stk.peek() == '0' and idx == len(inp):  #unbalanced on left
        return 'Reject'
    while (stk.peek() == '0' and inp[idx] == '1'):
        stk.pop()
        idx = idx + 1
        if stk.peek() == '0' and idx == len(inp):  #unbalanced on left
            return 'Reject'
    state = q4

    #go to state q4
    #pop the stack
    if stk.peek() == '$':  
       stk.pop() 
    if (idx != len(inp)):  #unbalanced on the right
        return 'Reject'

    #in state q4
    if state in F:
        return 'Accept' 
    else:
        return 'Reject'



def main():
    PDA = build_PDA()
    while(True):
        inp = input("enter a string, enter 'quit' to quit ")
        if inp == 'quit':
            break
        print(simulate(PDA,inp))

main()



