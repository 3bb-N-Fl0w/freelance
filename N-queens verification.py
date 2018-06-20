N = 0 #board size/number of queens
QUEENS_LIST = []
VALID_CERTIFICATE = False



def boardSize (): #ask user input for board size

    global N

    while True: #keep asking until getting a valid result
        try:
            N = int(input('\nboard size/number of queens: ')) #try to convert into an int type
            if N < 0:
                continue
            else:
                return None
        except ValueError:
            pass


def queenLocation ():

    global QUEENS_LIST

    for column in range (N):
        check = False
        while not check:
            try:
                row = int(input('\nrow location of queen in column ' + str(column) + ':'))
                if row < N:
                    check = True

            except ValueError:
                pass

        QUEENS_LIST.append([row, column])

def twoQueensAttack (queenOne, queenTwo):
    if queenOne[0] == queenTwo[0] or ((queenOne[0] - queenOne[1]) == (queenTwo[0] - queenTwo[1])):
        return True
    return False


def checkQueenList ():
    global N
    global QUEENS_LIST
    global VALID_CERTIFICATE

    for i in range (N):
        for j in range (N):
            if i != j:
                VALID_CERTIFICATE = twoQueensAttack(QUEENS_LIST[j], QUEENS_LIST[i])
                if VALID_CERTIFICATE:
                    VALID_CERTIFICATE = not VALID_CERTIFICATE
                    return None
    VALID_CERTIFICATE = not VALID_CERTIFICATE
    return None


def printCertificate ():
    global VALID_CERTIFICATE

    if VALID_CERTIFICATE:
        print('\nA valid solution of the N-Queens problem, with N of', N)
    else:
        print('\nNot a valid solution')


def singleInstance ():
    boardSize()
    queenLocation()
    checkQueenList()
    printCertificate()


singleInstance()