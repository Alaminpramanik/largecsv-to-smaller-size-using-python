import pandas as pd

#csv file name to be read in
in_csv = 'splitfile.csv'

#get the number of lines of the csv file to be read
number_lines = sum(1 for row in (open(in_csv)))

#size of rows of data to write to the csv,

#you can change the row size according to your need
rowsize = 5000
header= ['Year', 'Versions','Periods','ref3','ref2','ref1','Value']

#start looping through data writing it to a new file for each set
for i in range(0,number_lines,rowsize):
    df = pd.read_csv(in_csv,sep=';',nrows = rowsize,skiprows = i)
    df.columns = header
    
    #csv to write data to a new file with indexed name. input_1.csv etc.
    out_csv = 'Enronset' + str(i) + '.csv'
    
    df.to_csv(out_csv,
          index=False,
          header=True,
          mode='a',#append data to csv file
          chunksize=rowsize)