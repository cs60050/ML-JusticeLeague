# JusticeLeague
Welcome to the repository of Team - **JusticeLeague**.

This is the repository for our term project - **Automatic Document Summarization using a Machine Learning approach**.

![](http://media.comicbook.com/2016/07/justice-league-logo-191887.jpg)

##Team:
    Sai Sriharsha Annepu  -  13CS10012
    Ananth Pranihith. P   -  13CS10011
    Thejesh Venkata       -  13CS10013
    Pavan Reddy. B        -  13CS10015
    Jyothi Swaroop. B     -  13CS10016
    Prithvi Raj Reddy     -  13CS10029
    Konda Akhil           -  13CS10030
    Sai Sambasiva. P      -  13CS10034
    Supradeep Allu        -  13CS10050
    Aswanth Kumar         -  13CS30019
    Suryateja Chunduru    -  13EE10017
    Prasanth Balaga       -  09CS3031    
---------------------------------------------------------------------------------------------
Update: Dated 5th September, 2016

##Introductory Presentation:
 Please follow this link to the RoadMap Presentation - [DocSummarization-ML](https://github.com/cs60050/ML-JusticeLeague/blob/master/DocSummarization-ML.pdf)
 
---------------------------------------------------------------------------------------------
Update: Dated 23rd September, 2016

##Pre-Processing:
 The pre-processing is being done using the following steps -
 ![](./Pics/Pre-Processing.png)
---------------------------------------------------------------------------------------------
Update: Dated 23rd September, 2016

##Features Identified:
 Our summarizer produces summaries using a feature profile oriented sentence extraction stategy. The following features have been identified as important:
 
    1)  CUE PHRASES
    2)  SIMILARITY TO THE TITLE
    3)  TF-ISF
    4)  DEGREE CENTRALITY
    5)  C-LEX RANK
    6)  TEXT RANK
    7)  NON-ESSENTIAL WORDS (Like "Additionally")
    8)  NUMERICAl DATA
    9)  SENTENCE LENGTH
    10) WORDNET BASED RANKING

----------------------------------------------------------------------------------------------
Update: Dated 24th September, 2016

## Feature Extraction
  **Mean TF-ISF** 
  
  This feature is analogous to TF-IDF in the context of Information Retrieval. In IR, we have to select few documents which are most relevant from a given set of documents. Here, we have to select few sentences from the given document.The used feature is calculated as the mean value of the TF-ISF measure for all the words of each sentence. The feature is calculated in the following way-
  
  ![](./Pics/TF-ISF.png)  
  
  **Sentence Length** 
  
  Sentences of too short length add little value when included in the summary. This feature is used to penalize such sentences so that they will not be included in final summary.

  **Sentence Position** 
  
  Sentences at the start of the document and also at the end of the document generally have more importance and are candidates to be included in the summary. Even, sentence position in each paragraph is useful, but here the summarizer checks for the overall position and weights accordingly (as it summarizes news articles which generally tend to have information about a single aspect and not divided into paragraphs - Identified from the corpus present with us). This is the graph which shows the normalized weights assigned to sentences-
  
  ![](./Pics/SentencePosition.png)

 **Wordnet Ranking**

   We created list of Keywords by taking Adjectives,nouns and Propernouns.We have calculated number of times a particular word or its synonyms occured in document by using synset.Now if Keyword is a properNoun a score of 1 is assigned or else a highest similarity score is assigned which is calculated with respect to synonyms of other words present in document.Now for each sentence a score is assigned which is (sum of scores of all keywords present in the sentence)/(Number of keywords present in sentence).
