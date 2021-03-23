#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np

# import our Random class from python/Random.py file
sys.path.append(".")
from Random import Random


# main function for our coin toss Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed <number> , -Ntoss <no. of dice rolls>, -Nexp <no. of experiment>, -type <nb> or <bi> for not biased and biased types of dice, -output <H0.txt> or <H1.txt> for unbiased and biased trial, respectively]" % sys.argv[0])
        print
        sys.exit(1)

    # default seed
    seed = 5555

    # default type of dice roll
    type = "nb"
    

    # default number of coin tosses (per experiment)
    Ntoss = 1

    # default number of experiments
    Nexp = 1

    # output file defaults
    doOutputFile = False


    random_number = Random(seed)

    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-type' in sys.argv:
        p = sys.argv.index('-type')
        ptemp = sys.argv[p+1]
        type = ptemp

        
    if '-Ntoss' in sys.argv:
        p = sys.argv.index('-Ntoss')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            Ntoss = Nt
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True

    if doOutputFile:
        #wt = (1./6.)
        #wt = random_number.Exponential(1)
        
        outfile = open(OutputFileName, 'w')
        for e in range(0,Nexp):
            for t in range(0,Ntoss):
                if type == "nb":
                    outfile.write(str(random_number.Category6f())+" ")
                    

                if type == "bi":
                    wt = random_number.Exponential(1)
                    outfile.write(str(random_number.Category6(wt))+" ")
            outfile.write(" \n")
        outfile.close()
