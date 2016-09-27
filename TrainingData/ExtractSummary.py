from os import listdir
from random import shuffle
from PreProcess import doPreProcessing

def extractSummary():
    count = 1
    op_folder = "./Training/"

    data_dir = listdir("./Dataset/training/docs")
    shuffle(data_dir)
    for filename in data_dir:

        if count == 121:
            op_folder = "./Test/"

        ip_file = open("./Dataset/training/docs/"+filename, "r")

        ip_doc = ip_file.read()
        ip_file.close()
        smallsumm, largesumm, fulldoc, fulldocwithoutStemming = doPreProcessing(ip_doc,count)

        op_file = open(op_folder+"FullDocsWithoutStemming/"+str(count)+"_fulldocwithoutstemming.txt", "w")
        for sent in fulldocwithoutStemming:
            for word in sent:
                op_file.write(word+" ")
            op_file.write(".\n")
        op_file.close()

        op_file = open(op_folder+"FullDocs/"+str(count)+"_fulldoc.txt", "w")
        for sent in fulldoc:
            for word in sent:
                op_file.write(word+" ")
            op_file.write(".\n")
        op_file.close()

        op_file = open(op_folder+"SmallSumms/"+str(count)+"_smallsumm.txt", "w")
        for sent in smallsumm:
            for word in sent:
                op_file.write(word+" ")
            op_file.write(".\n")
        op_file.close()

        op_file = open(op_folder+"LargeSumms/"+str(count)+"_largesumm.txt", "w")
        for sent in largesumm:
            for word in sent:
                op_file.write(word+" ")
            op_file.write(".\n")
        op_file.close()
        count += 1

if __name__ == "__main__":
    extractSummary()
