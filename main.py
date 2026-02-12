
import sys


def getOrderRotationSequence_aux(S, b, e):
    if S[b] <= S[e]:
        return b
    if S[b] == S[e]:
        return b
    
    q = (b + e) // 2

    if S[q] >= S[q+1]:
        return q + 1
    if S[q] < S[q-1]:
        return q


    if S[q] >= S[b]:
        return getOrderRotationSequence_aux(S, q + 1, e)
    elif S[q] < S[b]:
        return getOrderRotationSequence_aux(S, b, q - 1)


def getOrderRotationSequence(S):
    return getOrderRotationSequence_aux(S,0,len(S)-1)

def testOrderSequence(S, order):
    """
    Prueba si la secuencia está corrida en el orden indicado
    :param S: Secuencia de elementos
    :param order: Número de rotaciones que deben realizarse sobre la secuencia
    :return: True si la solución es correcta
    """

    for i in range(order+1,len(S)):
        if S[i-1] > S[i]:
            return False
    for i in range(1, order+1):
        if S[i-1] > S[i]:
            return False
    return True



if __name__ == '__main__':
    if sys.argv < 2:
        print("Usage is python main.py file")
        sys.exit(0)

    file = sys.argv[1]
    # Read file into sequence
    S=[]
    for line in open(file):
        S.append(int(line))

    print(f'Rotation order of sequence is {getOrderRotationSequence(S)}')




