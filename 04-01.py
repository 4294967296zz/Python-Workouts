# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 23:27:31 2023
@fileName: 04-01.py
@author: Jiho
"""
def CLS() :
    print( "\014" )
    
def makeMap( N ) :
    global Map
    Map = [ [ [ i, k ] for k in range( 1, N + 1 ) ] for i in range( 1, N + 1 ) ]


# basic func with if - success
def moveA01( command, N ) :
    global current
    
    if( command == "L" ) :
        if( current[ 1 ] > 1 ) :
            current = [ current[0], current[1] - 1 ]
    elif( command == "R" ) :
        if( current[ 1 ] < N ) :
            current = [ current[0], current[1] + 1 ]
    elif( command == "D" ) :
        if( current[ 0 ] > 0 and current[ 0 ] < N ) :
            current = [ current[0] + 1, current[1] ]
    elif( command == "U" ) :
        if( current[ 0 ] > 1 and current[ 0 ] < N ) :
            current = [ current[0] - 1, current[1] ]  
        

# improved func with if - success
def moveA02( command, N ) :
    global current
    
    if( command in "LR" ) :
        if( command > "L" and current [1] <= N ) :
            current[1] += 1
        elif( current[ 1 ] > 1 and current [ 0 ] < N ) :
            current[1] -= 1
    else :
        if( command > "D" ) :
            current[0] -= 1
        elif( current[ 0 ] > 0 and current[ 0 ] < N ) :
            current[0] += 1
            

# improved func with if and loop - success
def moveA03( command, N ) :
    global current
    
    if( command in "LR" ) :
        current[ 1 ] += 1
        if( command == "L" ) :
            current[ 1 ] -= 2
    else :
        current[ 0 ] += 1
        if( command == "U" ) :
            current[ 0 ] -= 2
            
    for k in range( 2 ) :
        if( current[ k ] < 1 ) :
            current[ k ] = 1
        
    if( current[ 0 ] > N ) :
        current[ 0 ] = N
        
    if( current[ 1 ] > N ) :
        current[ 1 ] = N
        

# improved func with if and loop and loop - success
def moveA04( command, N ) :
    global current
    
    if( command in "LR" ) :
        current[ 1 ] += 1
        if( command == "L" ) :
            current[ 1 ] -= 2
    else :
        current[ 0 ] += 1
        if( command == "U" ) :
            current[ 0 ] -= 2
            
    for k in range( 2 ) :
        if( current[ k ] < 1 ) :
            current[ k ] = 1
        
        if( current[ k ] > N ) :
            current[ k ] = N
        

def startTravle01( N = 5, command = "UUU" ) :
    global Map, current
    
    makeMap( N )
    current = [ 1, 1 ]

    for ch in command :
        moveA04( ch, N )
    print( current[ 0 ], current[ 1 ] )


# used lists - failed
def moveB01( command ) :
    global current, commands, moves
    
    idx = commands.index( command )
    current[ idx & 1 ] += moves[ idx ]
             

# improved func with lists - success
def moveB02( command, N ) :
    global current, commands, moves
    
    idx = commands.index( command )
    current[ idx & 1 ] += moves[ idx ]
    
    for k in range( len( current ) ) :
        if( current[ k ] < 1 ) :
            current[ k ] = 1
        
        if( current[ k ] > N ) :
            current[ k ] = N


# improved func with lists - failed
def moveB03( command, N ) :
    global current, commands, moves
    
    idx = commands.index( command )
    if( current[ idx & 1 ] >= 1 ) and ( current[ idx & 1 ] < N ) :
        current[ idx & 1 ] += moves[ idx ]
    

# improved func with lists - failed
def moveB03A01( command, N ) :
    global current, commands, moves
    
    idx = commands.index( command )
    cur = current[ idx & 1 ]
    if( cur > 0 ) and ( cur < N ) :
        current[ idx & 1 ] += moves[ idx ]


def startTravle02( N = 5, command = "DU" ) :
    global current, commands, moves
    
    current = [ 1, 1 ]
    commands = [ "U", "L", "D", "R" ]
    moves = [ -1, -1, 1, 1 ]
    
    for ch in command :
        moveB03A01( ch, N )
        
    print( startTravle02.__name__ + "() :")
    print( current[ 0 ], current[ 1 ] )


def startTravle03( N = 5, command = "DDD" ) :
    global current, commands, moves
    
    current = [ 1, 1 ]
    commands = [ "U", "L", "D", "R" ]
    moves = [ -1, -1, 1, 1 ]
    
    for k in range( len(command) ) :
        if( sum(current) > 2 ) and commands [ k ] in "DR" :
            moveB03A01( command[ k ], N )
            
    print( startTravle03.__name__ + "() :")
    print( current[ 0 ], current[ 1 ] )

    
# improved moveB01 without if - failed
def moveB04( command, N ) :
    global current, commands, moves
    
    idx = commands.index( command )
    compare = int( 1 <= current[ idx & 1 ] < N )
    current [ idx & 1 ] += compare * moves[ idx ]
    current [ idx & 1 ] += int( current[ idx & 1 ] < 1 )
    

# improved moveB04 without if - success
def moveB04A01( command, N ) :
    global current, commands, moves
    
    idx = commands.index( command )
    current [ idx & 1 ] += moves[ idx ]
    
    current [ idx & 1 ] += int( current[ idx & 1 ] < 1 )
    current [ idx & 1 ] -= int( current[ idx & 1 ] > N )
    

def startTravle04( N = 5, command = "UUDDRRR" ) :
    global current, commands, moves
    
    current = [ 1, 1 ]
    commands = [ "U", "L", "D", "R" ]
    moves = [ -1, -1, 1, 1 ]
    
    for k in range( len(command) ) :
        moveB04A01( command[ k ], N )
            
    print( startTravle04.__name__ + "() :", current[ 0 ], current[ 1 ])
    

# new way - range check failed
def moveB05( command ) :
    global current, commands, X, Y
    
    for k in range( len( commands ) ) :
        if command == commands[ k ] :
            current[ 0 ] += X[ k ]
            current[ 1 ] += Y[ k ]


# improving moveB05 - range check failed
def moveB05A01( command ) :
    global current, commands, X, Y
    
    idx = commands.index( command )
    current[ 0 ] += X[ idx ]
    current[ 1 ] += Y[ idx ]
    
    
def startTravle05( N = 5, command = "RR" ) :
    global current, commands, X, Y
    
    L = len( command )
    current = [ 1, 1 ]
    commands = [ "U", "L", "D", "R" ]
    X, Y = [ -1, 0, 1, 0 ], [ 0, -1, 0, 1 ]
    
    for k in range( L ) :
        moveB05A01( command[ k ] )
    
    print( startTravle05.__name__ + "() :", current[ 0 ], current[ 1 ])


# solution using range list - success
def startTravle06( N = 5, command = "UUUUUDDDDDLLLLLRRR" ) :
    global current, commands, moves
    
    L = len( command )
    current = [ 1, 1 ]
    commands = [ "U", "L", "D", "R" ]
    moves = [ -1, -1, 1, 1 ]
    R = [ 1 ] + [ k for k in range( 1, N + 1 ) ] + [ N ]
    
    
    for k in range( L ) :
        moveB01( command[ k ] )
        current[ 0 ] = R[ current[ 0 ] ]
        current[ 1 ] = R[ current[ 1 ] ]
    
    print( startTravle05.__name__ + "() :", current[ 0 ], current[ 1 ])



def main() :
    CLS()
    # startTravle01()
    # startTravle02()
    # startTravle03()
    # startTravle04()
    # startTravle05()
    startTravle06()
    
if( __name__ == "__main__" ) :
    main()