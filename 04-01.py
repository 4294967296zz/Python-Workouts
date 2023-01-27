# 상하좌우 문제

def CLS() :
    print( "\014" )


def makeMap( N ) :
    global current, MAP
    MAP = [ [ [ i, k ] for k in range( 1, N + 1 ) ] for i in range( 1, N + 1 ) ]


def move( command, N ) :
    global current, MAP

    if command == "L" :
        if current[ 1 ] > 1:
            current[ 1 ] -= 1
    elif command == "R" :
        if current[ 1 ] <= N :
            current[ 1 ] += 1
    elif command == "D" :
        if current[ 0 ] > 1 :
            current[ 0 ] -= 1
    elif command == "U" :
        if current[ 0 ] >= N :
            current[ 0 ] += 1


def startTravel( N = 5 ) :
    global current, MAP
    current = [ 1, 1 ]
    makeMap( N )

    command = "DDR"
    for ch in command :
        move( ch, N )

    print( current )


def main() :
    CLS()
    startTravel()


if( __name__ == "__main__" ) :
    main()
