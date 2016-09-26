from PreProcess import doPreProcessing
import os

count = 1
for filename in os.listdir("./training/docs"):
	try:
		ip_file = open("./training/docs/"+filename,"r")
		ip_doc = ip_file.read()
		ip_file.close()
		smallsumm, largesumm, fulldoc, docwithoutstemming = doPreProcessing(ip_doc)
		f = open("./DocsWithoutStemming/"+str(count)+"_doc.txt","w")
		for sent in actualdoc:
			for word in sent:
				f.write(word+" ")
			f.write(".\n")
		f.close()
		f = open("./FullDocs/"+str(count)+"_fulldoc.txt","w")
		for sent in fulldoc:
			for word in sent:
				f.write(word+" ")
			f.write(".\n")
		f.close()
		f = open("./SmallSumms/"+str(count)+"_smallsumm.txt","w")
		for sent in smallsumm:
			for word in sent:
				f.write(word+" ")
			f.write(".\n")
		f.close()
		f = open("./LargeSumms/"+str(count)+"_largesumm.txt","w")
		for sent in largesumm:
			for word in sent:
				f.write(word+" ")
			f.write(".\n")
		f.close()
		count+=1
	except:
		continue
