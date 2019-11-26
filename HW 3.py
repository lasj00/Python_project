import csv
import os

directory = "/Users/honza/Desktop/"

for file in os.listdir(directory):

    if os.path.splitext(file)[-1].lower() == ".csv":
        with open(directory+file,'r') as csvinput:

            with open(directory+"/Outputs/"+"Change_of_"+file, 'w') as csvoutput:
                writer = csv.writer(csvoutput, lineterminator='\n')
                reader = csv.reader(csvinput)

                all = []
                row = next(reader)
                row.append('Change')
                all.append(row)

                for row in reader:
                    row.append(str(round((float(row[4])-float(row[1]))/float(row[1]),5)) + "%")
                    all.append(row)

                writer.writerows(all)
    else:
        continue




