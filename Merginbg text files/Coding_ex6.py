import glob
import datetime
filenames = glob.glob("fi*.txt")
#print filenames
resultfile = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt"
#print outfile
with open(resultfile,'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line+"\n")
outfile.close()
