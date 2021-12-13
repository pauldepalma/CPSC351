'''
PDA to recognize T = {0^n1^n + n>= 9}
PDA diagram from Sipser, Fig. 2.15, p. 115
'''

#Stack to be used by PDA simulater
class Stack:
    def __init__(self):
        self.stk = []

    def push(self,elt):
        self.stk.append(elt)

    def pop(self,elt):
        return self.stk.pop()

    def peek(self):
        top = len(self.stk) - 1
        return self.stk[top]

    def isempty(self):
        if self.length() == 0:
            return True
        else:
            return False

    def length(self):
        return len(self.stk)

    def display(self):
        for elt in self.stk:
            print(elt)

def build_PDA():
        Q = {1,2,3,4}
        Sigma = {'0','1'}
        Gamma = {'0','$'}
        delta =  "defined as functions functions q1q4, q2, q3"
        start = 1
        F = {1,4}
        M =(Q,Sigma,Gamma,delta,start,F) #A PDA is a six-tuple
        return M

def simulate(M,input):
    Q = list(M[0])
    Sigma = M[1]
    state = M[4]
    F = M[5]
    stk = Stack()

    result, state, stk = q1(input,stk)
    if result == "Accept":
        return result
    
    #process
    for symbol in input:
        if symbol not in Sigma:
            return "Reject"
        if state == 2:
            state,stk = q2(symbol,stk)
        else:
            if state == 3:
                state,stk = q3(state,symbol,stk)

    if state == 4:
        return q4(stk)
    else:
        return "Reject"
            

#The transition functions follow. They are identical to those found on p. 115
def q1(input,stk):
    result = ''
    state = 2
    if len(input) == 0:
        result =  'Accept'
    else:
        stk.push('$')
    return result,state,stk

def q2(symbol, stk):
    print(symbol)
    stk.display()
    print()
    if symbol == '0':
        stk.push('0')
        state = 2
        return state,stk
        
    if symbol == '1':
        if stk.peek == '0':
            stk.pop()
            state = 3
            return state,stk
    quit()
    

def q3(symbol, stk):
    state = -1
    if symbol == '1' and stk.peek() == '0':
        stk.pop()
        state = 3
    if stk.peek() == '$':
        stk.pop()
        state = 4
    return state, stk

def q4(stk):
    if stk.isempty():
        return 'Accept'
    return 'Reject'
    
def main():
    M = build_PDA()

    while(True):
        inp = input("Enter a string, enter 'quit' to quit: ")
        if inp == 'quit':
            break
        print(simulate(M,inp))

main()

