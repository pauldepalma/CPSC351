'''
Python 3.9
DFA to recogniz L
Sigma = {0,1}
L = {s | s is an elememt of Sigma*, every odd position of is 1, length
  or s > 0}
'''

#Proecess using the Kilfoyle model
def process(M,string):
    Q = M[0]
    Sigma = M[1]
    delta = M[2]
    q0 = M[3]
    F = M[4]
    current_state = q0
    for symbol in string:
        if current_state not in Q or symbol not in Sigma:
            return "Reject"   #invalid symbol
        current_state = delta[(current_state, symbol)]  #process input
    if current_state in F:
        return "Accept"
    return "Reject"

def build_dfa():
    Q = {1,2,3,4}
    Sigma = {'0','1'}
    delta = {
        (1,'0'): 4,  #in state 1, read a 0 go to state 4 etc.
        (1,'1'): 2,
        (2,'0'): 3,
        (2,'1'): 3,
        (3,'0'): 4,
        (3,'1'): 2,
        (4,'0'): 4,
        (4,'1'): 4,
        }
    q0 = 1  #start state
    F = {2,3} #accept state
    M = (Q,Sigma,delta,q0,F)  #dfa is a 5-tuple
    return M

def main():
    M = build_dfa()
    
    while(True):
        string = input("enter a string or enter quit to stop ")
        if string =="quit":
            break
        print(process(M,string))

main()
        
        
