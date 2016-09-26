##Dataset Description

This README describes the dataset from Woodsend and Lapata (ACL, 2010).

The dataset consists of online news articles collected from the CNN corpus. Each article comes with a set of highlights written by the author detailing the key points. These highlights are used to acquire our ground truth extractive summaries for training.
![](http://i.imgur.com/v7qBBKP.png)

There are two folders: *training* and *test*. The *training* folder contains CNN articles and their corresponding highlights. 
Each document and its highlight have the same prefix but different suffixes. So for example the highlights for the article 
*tiger.conservation2008.doc.txt* are *tiger.conservation2008.hlights.txt*. 
Highlights and documents are in different directories (training/hlights and training/docs, respectively).

The training files have been annotated as follows. In the beginning of each line there is a number, ranging from 1, 2, and 3. 
The numbers denote whether the document sentence corresponds to a highlight. 

 	label (1) means that the sentence must be in the highlights
 	label (2) that the sentence could be in the highlights
 	label (3) that the sentence is not in the highlights.

The structure of the *test* folder is analogous to *training*. Again it has two directories (test/doc and test/hlights), each containing files corresponding to the documents and their highlights. The test files have no alignment annotations. The files are all one sentence per line, and tokenized.
