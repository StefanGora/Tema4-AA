from collections import defaultdict
import fileinput 

#function to sort pairs from list after second element
def Sort(sub_li): 
    l = len(sub_li) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (sub_li[j][1] > sub_li[j + 1][1]): 
                tempo = sub_li[j] 
                sub_li[j]= sub_li[j + 1] 
                sub_li[j + 1]= tempo 
    return sub_li 


#fuction to build a list of pairs of type (vertex, index)
#every vertex has a literal assigned
def build_multime(input_list):
    pair = []
    multime = []
    for i in range(1, int(input_list[1]) + 1):
        for j in range(1, int(input_list[0]) + 1  ):
                pair = [i, j]
                multime.append(pair)    
    return multime   
  


#functions used for building the first part
#  of the Sat expresion
def at_most_one( k, V):

    expresion = ''
    negation = "~"
    content = ''
    for i in range(k*V , k*V+V):
        for j in range(i + 1, k*V+V):
            li = negation + str(i+1)
        
            lj = negation + str(j+1)

            content = li + "V" + lj
            claus ="(" + content + ")" + "^"

            expresion += claus
    return expresion.rstrip("^")


#functions used for building the second part
#  of the Sat expresion
def at_least_one(literals):
    expresion = ''
    for i in range(0, len(literals)):
        claus = str(literals[i]) + "V"
        if i == len(literals) -1:
            claus = str(literals[i])   
        expresion += claus
    expresion = "(" + expresion + ")"
    return expresion


def build_F1(input_list, k, V): 
    f1 = ''
    for i in range(0, int(input_list[0])):
        claus = at_most_one(i, V) + "^"
        f1 += claus
    return f1.rstrip("^")



#function to assign the right literals for 
#at_least_one
def build_condition(edge, X, literals, k):
    condition = []
    buffer_literals = []
    parser = edge.split(" ")   
    for i in range(1,int(k) +1):
        start_edge = [int(parser[0]), i]
        end_edge = [int(parser[1]), i]
        buffer_literals.append(start_edge)
        buffer_literals.append(end_edge)
        buffer_literals.sort()
        buffer1 = []
        buffer2 = []    
    for i in range(0,len(buffer_literals)):
        for j in range(0,len(X)):
            if buffer_literals[i] == X[j]:
                condition.append(literals[j])
    return condition

def build_F2(edges, X, literals, k):
    f2 = ''
    for index in range (0, len(edges)):
        alo_input = (build_condition(edges[index], X, literals, k  ) )
        claus = at_least_one(alo_input)
        f2 += claus + "^"
        alo_input = []
        claus = []

    return f2.rstrip("^")



def main():
    input_list = []
    f = open("input/input00.txt")
    for line in f:
        token = line.rstrip("\n")
        input_list.append(token)
    buffer = []
    index = 1
    literals = []

    
    X = build_multime(input_list)
    X = Sort(X)
    
    k = input_list[0]
    V = int(input_list[1])
    edges = input_list[3:]




 
    for i in X:
        literals.append(index)
        index += 1

    f1 = build_F1(input_list, int(k), V)
    f2 = build_F2(edges, X, literals, k)   
    Sat = f1 + "^" + f2
    print(Sat)


if __name__ == "__main__":
    main()