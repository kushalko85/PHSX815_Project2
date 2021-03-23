#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from MySort import MySort

# import our Random class from python/Random.py file
sys.path.append(".")
from Random import Random

# main function for our coin toss Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed <number>, -input0 <H0.txt>, -input1 <H1.txt>]" % sys.argv[0])
        print
        sys.exit(1)
    # default single coin-toss probability for hypothesis 0
    p0 = float(1/6)

    # default single coin-toss probability for hypothesis 1
    p1 = float(1/5)

    haveH0 = False
    haveH1 = False

    if '-prob0' in sys.argv:
        p = sys.argv.index('-prob0')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            p0 = ptemp
    if '-prob1' in sys.argv:
        p = sys.argv.index('-prob1')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            p1 = ptemp
    if '-input0' in sys.argv:
        p = sys.argv.index('-input0')
        InputFile0 = sys.argv[p+1]
        haveH0 = True
    if '-input1' in sys.argv:
        p = sys.argv.index('-input1')
        InputFile1 = sys.argv[p+1]
        haveH1 = True
    if '-h' in sys.argv or '--help' in sys.argv or not haveH0:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("   -input0 [filename]  name of file for H0 data")
        print ("   -input1 [filename]  name of file for H1 data")
        print ("   -prob0 [number]     probability of 1 for single toss for H0")
        print ("   -prob1 [number]     probability of 1 for single toss for H1")
        print
        sys.exit(1)
    
    Ntoss = 1
    Npass0 = []
    LogLikeRatio0 = []
    Npass1 = []
    LogLikeRatio1 = []

    Npass_min = 1e8
    Npass_max = -1e8
    LLR_min = 1e8
    LLR_max = -1e8
        
    with open(InputFile0) as ifile:
        nsix = 0
        Total = 0
        nones = 0
        ntwos = 0
        nthrees = 0
        nfours = 0
        nfives = 0
        for line in ifile:
            lineVals = line.split()
            Ntoss = len(lineVals)
            Npass = 0
            
            Total = Total +1 
            for v in lineVals:
                
                if int(v) == 6:
                    nsix = nsix + 1

                if int(v) == 1:
                    nones = nones +1

                if int(v) == 2:
                    ntwos = ntwos +1

                if int(v) == 3:
                    nthrees = nthrees + 1

                if int(v) == 4:
                    nfours = nfours +1

                if int(v) == 5:
                    nfives = nfives +1
        Nexp = Total
        #print(Nexp)
        pones = nones/(Ntoss*Nexp)
        ptwos = ntwos/(Ntoss*Nexp)
        pthrees = nthrees/(Ntoss*Nexp)
        pfours = nfours/(Ntoss*Nexp)
        pfives = nfives/(Ntoss*Nexp)
        psix = nsix/(Ntoss*Nexp)
        #print(psix)
        print(psix,pones,ptwos,pthrees,pfours,pfives)
    with open(InputFile0) as ifile:

        for line in ifile:
            lineVals = line.split()
            Ntoss = len(lineVals)
            Npass = 0
            LLR = 0.
            for v in lineVals:
                
                if int(v) == 6:
                    LLR += np.log(psix/(1./6.))
                    #print("six",psix)

                if int(v) == 1:
                    LLR += np.log(pones/(1./6.))

                if int(v) == 2:
                    LLR += np.log(ptwos/(1./6.))

                if int(v) == 3:
                    LLR += np.log(pthrees/(1./6.))

                if int(v) == 4:
                    LLR += np.log(pfours/(1./6.))

                if int(v) == 5:
                    LLR += np.log(pfives/(1./6.))

            
                Npass += float(v)

                    
            if Npass < Npass_min:
                Npass_min = Npass
            if Npass > Npass_max:
                Npass_max = Npass
            if LLR < LLR_min:
                LLR_min = LLR
            if LLR > LLR_max:
                LLR_max = LLR
            Npass0.append(Npass)
            LogLikeRatio0.append(LLR)

    if haveH1:
        with open(InputFile1) as ifile:
            nsix1 = 0
            Total1 = 0
            nones1 = 0
            ntwos1 = 0
            nthrees1 = 0
            nfours1 = 0
            nfives1 = 0
            for line in ifile:
                lineVals = line.split()
                Ntoss = len(lineVals)
                Npass = 0
                
                Total1 = Total1 +1 
                for v in lineVals:
                
                    if int(v) == 6:
                        nsix1 = nsix1 + 1
                        #print("red",psix1)

                    if int(v) == 1:
                        nones1 = nones1 +1

                    if int(v) == 2:
                        ntwos1 = ntwos1 +1

                    if int(v) == 3:
                        nthrees1 = nthrees1 + 1

                    if int(v) == 4:
                        nfours1 = nfours1 +1

                    if int(v) == 5:
                        nfives1 = nfives1 +1
            Nexp = Total1
            #print(Nexp)
            pones1 = nones1/(Ntoss*Nexp)
            ptwos1 = ntwos1/(Ntoss*Nexp)
            pthrees1 = nthrees1/(Ntoss*Nexp)
            pfours1 = nfours1/(Ntoss*Nexp)
            pfives1 = nfives1/(Ntoss*Nexp)
            psix1= nsix1/(Ntoss*Nexp)
            #print(psix1,pones1,ptwos1,pthrees1,pfours1,pfives1)
            #print(psix+pones+ptwos+pthrees+pfours+pfives)

        with open(InputFile1) as ifile:

            for line in ifile:
                #print("line",line)
                lineVals = line.split()
                Ntoss = len(lineVals)
                Npass = 0
                LLR1 = 0.
                for v in lineVals:
                    #print("this loop works",v)
                
                    if int(v) == 6:
                        LLR1 += np.log(psix1/(1./6.))
                        #print("red",psix1)

                    if int(v) == 1:
                        LLR1 += np.log(pones1/(1./6.))

                    if int(v) == 2:
                        LLR1 += np.log(ptwos1/(1./6.))

                    if int(v) == 3:
                        LLR1 += np.log(pthrees1/(1./6.))

                    if int(v) == 4:
                        LLR1 += np.log(pfours1/(1./6.))

                    if int(v) == 5:
                        LLR1 += np.log(pfives1/(1./6.))
            

                
                if LLR < LLR_min:
                    LLR_min = LLR
                if LLR > LLR_max:
                    LLR_max = LLR
                    
                LogLikeRatio1.append(LLR1)
                

    title = str(Ntoss) +  " tosses / experiment from 100 trials"


    Sorter = MySort()
    #print(LogLikeRatio1)
    LogLikeRatio0 =  np.array(Sorter.DefaultSort(LogLikeRatio0))
    LogLikeRatio1 =  np.array(Sorter.DefaultSort(LogLikeRatio1))

    N0 = len(LogLikeRatio0)
    N1 = len(LogLikeRatio1)
# Define alpha and get beta

    Alpha = .05
    la = LogLikeRatio0[min(int((1-Alpha)*N0),N0-1)]
    leftover= np.where(LogLikeRatio1 > la)[0][0]
    beta = leftover/N1
    print(la,beta)

    #weights = np.ones_like(LogLikeRatio0) / len(LogLikeRatio0)
    #weights1 = np.ones_like(LogLikeRatio1) / len(LogLikeRatio1)
    #LogLikeRatio0 = [float(i)/sum(LogLikeRatio0) for i in LogLikeRatio0]
    # make LLR figure
    plt.figure()
    plt.hist(LogLikeRatio0,bins = 20, facecolor='b', alpha=0.6, label="assuming $\\mathbb{H}_0$")
    plt.axvline(la, color='r',label = '$\lambda_a=0.290$')

    plt.hist(LogLikeRatio1,bins =20, facecolor='g', alpha=0.8, label="assuming $\\mathbb{H}_1$")
    plt.legend()

    plt.xlabel('X = $\\log({\\cal L}_{\\mathbb{H}_{1}}/{\\cal L}_{\\mathbb{H}_{0}})$')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.grid(True)
    alp_values = "α = " + str(Alpha)+"\n"+"β = " + str(beta)
    plt.text(-1.5, 10, alp_values)
    plt.legend()
    plt.show()



    
