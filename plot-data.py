# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 17:25:32 2023
@fileName: plot-data.py
@author: Jiho
"""
def CLS() :
    print( "\014" ) 

def sum02( N = 100, kA = [] ) :
    C = N // 2
    for k in range( C + 1 ) :
        kA[ k ] = C
         
    return kA


def sum02_Test( N = 100 ) :
    kA = [0] * ( N + 1 )
    print( sum02.__name__ + "()") 
    kA = sum02( N, kA )
    
    return kA


def sum02_plot_Test( N = 100 ) :
    from matplotlib import pyplot as plt
    
    # kA = sum02_Test()
    kA = [0]*51 + [50]*50
    plt.plot( kA )
    plt.ylim( 0, 100 )
    plt.title( sum02_plot_Test.__name__ + "()" )
    plt.show()
    
def main() :
    CLS()
    # sum01_plot_Test()
    sum02_plot_Test()
    
if( __name__ == "__main__" ) :
    main()