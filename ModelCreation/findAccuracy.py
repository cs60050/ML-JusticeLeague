import csv
import random
import math
import sys

# returns a list of lists
def loadCsv(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	if(len(dataset[-1]) == 0):
		dataset = dataset[:-1] 			# trimming the last line of the csv file if it is empty

	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]

	return dataset

def loadFeatureData(filename):
	lines = csv.reader(open(filename, "rb"))
	lines_list = list(lines)
	if(len(lines_list[-1]) == 0):
		lines_list = lines_list[:-1] 			# trimming the last line of the file if it is empty

	feature_data = {}
	for line in lines_list:
		class_label = float(line[-1])
		feature_data[class_label] = []

		for feature_info in line[:-1]:
			feature_info = feature_info[1:-1]	# trimming the brackets at the two ends
			feature_metrics = feature_info.split(";")
			feature_metrics = [float(x) for x in feature_metrics]
			(feature_data[class_label]).append(tuple(feature_metrics))

	return feature_data
 
def calculateProbability(x, mean, stdev):
	exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
	return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent
 
def calculateClassProbabilities(summaries, inputVector):
	probabilities = {}
	for classValue, classSummaries in summaries.iteritems():
		probabilities[classValue] = 1
		for i in range(len(classSummaries)):
			mean, stdev = classSummaries[i]
			x = inputVector[i]
			probabilities[classValue] *= calculateProbability(x, mean, stdev)
	return probabilities
			
def predict(summaries, inputVector):
	probabilities = calculateClassProbabilities(summaries, inputVector)
	bestLabel, bestProb = None, -1
	for classValue, probability in probabilities.iteritems():
		if bestLabel is None or probability > bestProb:
			bestProb = probability
			bestLabel = classValue
	return bestLabel
 
def getPredictions(summaries, testSet):
	predictions = []
	for i in range(len(testSet)):
		result = predict(summaries, testSet[i])
		predictions.append(result)
	return predictions
 
def classify(inputVectors, mode_num):
	if(mode_num == 1):
		filename = "mined_data_comb.txt"				# consider that learned data is present in this file in the current directory
	else:
		filename = "mined_data_large.txt"
	summaries = loadFeatureData(filename)

	# use the learned model for predictions
	predictions = getPredictions(summaries,inputVectors)
	return predictions


def evaluate(input_full_doc,input_vector_file,actual_summ, mode_num):
	try:
		f1 = open(input_full_doc,"r")
		inputVectors = loadCsv(input_vector_file)
		f2 = open(actual_summ,"r")
	except Exception,e:
		#print "---Could not access the some of the input files at their respective given location---"
		# print e
		return [0,0,0,0]

	full_doc_lines = f1.read().splitlines()
	summary_lines = f2.read().splitlines()
	pred = mode_num + 1
	if(pred > 2): pred = 1
	true_positives = 0
	true_negatives = 0
	false_positives = 0
	false_negatives = 0
	if len(inputVectors) == len(full_doc_lines):
		predictions = classify(inputVectors, mode_num)

		i = 0
		for line in full_doc_lines:
			if (predictions[i] == pred and line in summary_lines):	# consider class label for being present in the summary to be 1
				true_positives += 1
			elif (predictions[i] != pred and line not in summary_lines):
				true_negatives += 1
			elif (predictions[i] == pred and line not in summary_lines):
				false_positives += 1
			else:
				false_negatives += 1
			i += 1
	else:
		pass
		#print "---Given vector file is inconsistent with the given full_doc(" + input_full_doc + ")---"

	f1.close()
	f2.close()

	return [true_positives,true_negatives,false_positives,false_negatives]

def main():

	if len(sys.argv) != 2:
			print "Please provide proper arguments....\nTesting Mode Number:\n1)Small summaries\n2)Large Summaries\npython findAccuracy.py <mode_no>"
			return
	try:
		mode_num = int(sys.argv[1])
	except:
		print "Please provide proper arguments....\nTesting Mode Number:\n1)Small summaries\n2)Large Summaries\npython findAccuracy.py <mode_no>"
		return

	true_positives = 0
	true_negatives = 0
	false_positives = 0
	false_negatives = 0
	count = 0
	precision = 0
	recall = 0
	accuracy = 0
	for i in range(121,213):
		str1  = "../TrainingData/Test/FullDocs/" + str(i) + "_fulldoc.txt"
		str2  = "../TrainingData/Test/SmallSumms/" + str(i) + "_smallsumm.txt"
		str21 = "../TrainingData/Test/LargeSumms/" + str(i) + "_largesumm.txt"
		str3  = "../TrainingData/Test/Vectors/" + str(i) + "_vec.csv"

		if mode_num == 1:
			sum_str = str2
		elif mode_num == 2:
			sum_str = str21
		else:
			print "---Invalid mode number---\nGoing to exit..."
			return

		results = evaluate(str1,str3,sum_str, mode_num)
		true_positives += (results[0])
		true_negatives += (results[1])
		false_positives += (results[2])
		false_negatives += (results[3])

		precision += (float(true_positives)/(true_positives + false_positives))
		recall += (float(true_positives)/(true_positives + false_negatives))
		accuracy += (float(true_positives + true_negatives))/(true_positives + true_negatives + false_positives + false_negatives)
		count += 1

	print "Precision:",precision/count
	print "Recall:",recall/count
	print "Accuracy:",accuracy/count

main()