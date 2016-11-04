#!/usr/bin/python

import sys
import csv
import random
import math

# returns a list of lists
def loadCsv(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	if(len(dataset[-1]) == 0):
		dataset = dataset[:-1] 			# trimming the last line of the csv file if it is empty

	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset

def separateByClass(dataset):
	separated = {}
	for i in range(len(dataset)):
		vector = dataset[i]
		if (vector[-1] not in separated):
			separated[vector[-1]] = []
		separated[vector[-1]].append(vector)
	return separated
 
def mean(numbers):
	return sum(numbers)/float(len(numbers))
 
def stdev(numbers):
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers))
	return math.sqrt(variance)
 
def summarize(dataset):
	summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
	del summaries[-1]
	return summaries
 
def summarizeByClass(dataset):
	separated = separateByClass(dataset)
	summaries = {}
	for classValue, instances in separated.iteritems():
		summaries[classValue] = summarize(instances)
	return summaries
 
def learn(filename):
	trainingSet = loadCsv(filename)

	# prepare model
	summaries = summarizeByClass(trainingSet)
	return summaries


def main():

	if len(sys.argv) != 3:
		print "Please provide proper arguments....\nTraining Mode Number:\n1)Small summaries\n2)Large Summaries\n3)Small and Large Summaries\npython train.py <no.of.training docs> <mode_no>"
		return
	try:
		num_train_docs = int(sys.argv[1])
		mode_num = int(sys.argv[2])
	except:
		print "Please provide proper arguments....\nTraining Mode Number:\n1)Small summaries\n2)Large Summaries\n3)Small and Large Summaries\npython train.py <no.of.training docs> <mode_no>"
		return
	
	training_data_file = "train_set.csv"
	f3 = open(training_data_file,"w")

	for i in range(1,num_train_docs + 1):
		str1 = "../TrainingData/Training/FullDocs/" + str(i) + "_fulldoc.txt"
		str2 = "../TrainingData/Training/SmallSumms/" + str(i) + "_smallsumm.txt"
		str21 = "../TrainingData/Training/LargeSumms/" + str(i) + "_largesumm.txt"
		str3 = "../TrainingData/Training/Vectors/" + str(i) + "_vec.csv"


		try:
			f1 = open(str1,"r")
			f2 = open(str2,"r")
			f21= open(str21,"r")
			sentenceVectors = loadCsv(str3)
		except Exception,e:
			#print "---Could not access doc no " + str(i) + "---"
			# print e
			continue

		list1 = f2.read().splitlines()
		list11 = f21.read().splitlines()
		full_doc_lines = f1.read().splitlines()

		if len(sentenceVectors) == len(full_doc_lines):
			list2 = []
			if mode_num == 3:
				for line in full_doc_lines:
					if line in list1:
						list2.append(2)
					elif line in list11:
						list2.append(1)
					else:
						list2.append(0)
			elif mode_num == 2:
				for line in full_doc_lines:
					if line in list11:
						list2.append(1)
					else:
						list2.append(0)
			elif mode_num == 1:
				for line in full_doc_lines:
					if line in list1:
						list2.append(1)
					else:
						list2.append(0)
			else:
				print "---Invalid mode number---\nGoing to exit..."
				return


			cnt = long(0)
			for sentVec in sentenceVectors:
				for featureVal in sentVec:
					f3.write(str(featureVal))
					f3.write(",")

				sentenceClassLabel = list2[cnt]
				f3.write(str(sentenceClassLabel))
				f3.write("\n")
				cnt += 1

		f1.close()
		f2.close()
		f21.close()

	f3.close()

	learned_feature_data = learn(training_data_file)

	store_name = "mined_data"
	if(mode_num == 1):
		store_name += "_small.txt"
	elif(mode_num == 2):
		store_name += "_large.txt"
	else:
		store_name += "_comb.txt"
	f1 = open(store_name,"w")

	for class_label in learned_feature_data:

		for feature_info in learned_feature_data[class_label]:
			f1.write("(")
			for val in feature_info[:-1]:
				f1.write(str(val))
				f1.write(";")
			f1.write(str(feature_info[-1]))
			f1.write("),")
		f1.write(str(class_label))
		f1.write('\n')

	f1.close()


main()