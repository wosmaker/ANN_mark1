
MAX_GEN = 14

DES_FILE = "history_all"
INPUT_filename = "history"
FILE_EXTENSION = ".csv"

with open( DES_FILE + FILE_EXTENSION , 'a') as outfile:
    for i in range(1,MAX_GEN):
        with open("{}{}{}".format(INPUT_filename,i,FILE_EXTENSION)) as infile:
            for j, line in enumerate(infile):
                if j > 0 or i == 1:
                    outfile.write(line)

    

