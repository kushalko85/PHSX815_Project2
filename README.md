# PHSX815_Project2

# Role of number of trials and dynamic probability in testing bias of a dice

The codes in this repository (inside Python folder) is written to simulate fair and unfair dice and design a test statistic to test if we can distinguish the two different distributions or not. 

## How to run the codes ?
1) Run `Dice.py`. This gives plots for the outcomes from the biased dice and the distribution of number of sixes rolled by fair dice for different number of tosses and experiments. To run this program, type in: 
  `python3 Dice.py -seed <seed_number> -trial_b <number of trial of biased dice> -trial_n <number of experiment for fair dice> `
  
2) Run `Dice_Analysis.py`. This program saves the output of fair and unfair trials in a two different output files. To do that we have to run this program twice for biased and unbiased dice. To run this program, type in:
    `Dice_Analysis.py -Ntoss <no. of tosses to be done, default 250> -Nexp <no. of experiment, default 1000> -type <'nb' for unbiased dice roll and 'bi' for biased dice roll> -output <'H0.txt' or 'H1.txt' for unbiased and biased run respectively>`
    
3) Run `Dice_likeli.py`. This program gives the plot of the likelihood ratio test after taking in the inputs `H0.txt` and `H1.txt`. To run this program, type in:
      `Dice_likeli.py -input0 <H0.txt> -input1 <H1.txt>`
      
## Requirements:
-numpy
-scipy
-matplotlib

