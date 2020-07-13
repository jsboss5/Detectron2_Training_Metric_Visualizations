import json
import csv


def parser(filename):
    list = []
    retList = []

    for line in open(filename, 'r'):
        list.append(json.loads(line))

    for L in list:
        dict = {}
        dict["iteration"] = L["iteration"]
        dict["total_loss"] = L["total_loss"]
        retList.append(dict)

    return retList

def CSVwrite(listDicts, outputFile):
    toCSV = listDicts
    print(toCSV[0])
   
    keys = toCSV[0].keys()
    
    with open(outputFile, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV)

if __name__ == "__main__":
    targetList = (parser('ExampleMetrics.json')) 
    CSVwrite(targetList, 'ExampleCSV.csv')