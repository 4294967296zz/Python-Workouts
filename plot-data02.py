# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 14:52:56 2023
@fileName: plot-data02.py
@author: Jiho
@description : x = 100, y1 = 50, y2 = ?
"""
def CLS() :
    print( "\014" ) 


def dataPlotA01() :
    from matplotlib import pyplot as plt
    
    # kA = [0]*51 + [50]*50
    
    y0 = [0]*10 + [50]*80 + [0]*10
    y1 = [ k for k in range( 100 ) ]
    
    plt.plot( y0 )
    plt.plot( y1 )
    plt.ylim( 0, 100 )
    plt.title( dataPlotA01.__name__ + "()" )
    plt.show()    
    
    return y0, y1

def dataPlotA02() :
    from matplotlib import pyplot as plt
    
    # kA = [0]*51 + [50]*50
    
    y1 = []
        
    y0 = [0]*9 + [50]*80 + [0]*10
    y1 = [ (k * 25 / 10 ) for k in range( 100 + 1 ) ]
    
    for k in range( 0, 100 + 1 ) :
        if( 49 < y1[k] < 51 ) :
            print( k, y1[k] )
    
    plt.plot( y0 )
    plt.plot( y1 )
    plt.ylim( 0, 100 )
    plt.title( dataPlotA01.__name__ + "()" )
    plt.show()    

def dataPlotA03() :
    from matplotlib import pyplot as plt
    Target = 83
    Slope_X = 10
    Slope_Y = 25
    Slope = Slope_Y / Slope_X
        
    y0 = [0]*10 + [Target]*80 + [0]*10
    y1 = [ ( k * Slope ) for k in range( 100 + 1 ) ]
    
    for k in range( 0, 100 + 1 ) :
        if( Target - 1 < y1[k] < Target + 1 ) :
            print( k, y1[k] )
            if y1[ k ] != Target :
                print( y1[ k - 1 ], y1[ k ], y1[ k + 1 ] )
    
    plt.plot( y0 )
    plt.plot( y1 )
    plt.ylim( 0, 100 )
    plt.title( dataPlotA01.__name__ + "()" )
    plt.show()    
    
    return y0, y1

def dataPlotA04() :
    from matplotlib import pyplot as plt
    Target = 83
    Slope_X = 10
    Slope_Y = 25
    Slope = Slope_Y / Slope_X
        
    y0 = [0]*9 + [Target]*80 + [0]*10
    y1 = [ ( k * Slope ) for k in range( 100 + 1 ) ]
    
    for k in range( 0, 100 + 1 ) :
        if( Target - 1 < y1[k] < Target + 1 ) :
            print( k, y1[k] )
            if y1[ k ] != Target :
                print( y1[ k - 1 ], y1[ k ], y1[ k + 1 ] )
                
                target = k
                xt = [target] * 100
                for i in range( 100 ) :
                    xt[ i ] = xt[ i - 1 ] + 0.01
                    # print( '{:.2f}'.format(xt[i]) )
                
                yt = [ ( xt[ k ] * Slope ) for k in range( 100 ) ]
                
                for k in range( 0, 100 + 1 ) :
                    if( ( Target - 0.01 ) < yt[ k ] < ( Target + 0.01 ) ) :
                        print( k, '{:.2f}'.format(yt[ k ]) )
                        if yt[ k ] != Target :
                            print( yt[ k - 1 ], yt[ k ], yt[ k + 1] )
                            print( xt[ k - 1 ], xt[ k ], xt[ k + 1] )
                            print( '{:.2f}, {:.2f}, {:.2f}'.format(yt[ k - 1 ], yt[ k ], yt[ k + 1] ) )
                            print( '{:.2f}, {:.2f}, {:.2f}'.format(xt[ k - 1 ], xt[ k ], xt[ k + 1] ) )
                            break
                break
                
    plt.plot( y0 )
    plt.plot( y1 )
    plt.ylim( 0, 100 )
    plt.title( dataPlotA01.__name__ + "()" )
    plt.show()    
    
    
    return y0, y1

def main() :
    CLS()
    # dataPlotA01()
    # dataPlotA02()
    # dataPlotA03()
    dataPlotA04()
    
    
if( __name__ == "__main__" ) :
    main()

