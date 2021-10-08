# Analysis of Language Trends in Ulysses S. Grant's Memoirs.

In this project, I conduct an NLP no-code/low-code analysis on Ulysses S. Grant's Memoirs. The purpose of this project is to demonstrate that insightful, relatively in-depth analysis can be produced using no code/low code. The code that was involved in this project was hosted in a Jupyter Notebook in Google Colab and in an AWS Cloud9 environment—nothing was stored or computed locally.

For those that may not be familiar with Ulysses S. Grant, he is a very important figure in American history. While he was the 18th president of the U.S., he is perhaps more relevant historically for leading the Union to victory in the American Civil War. Thus, his memoirs may serve as a delight for many history enthusiasts. However, for someone who does not have hours upon hours (maybe even days!) to dedicate to reading this book, it could be a daunting endeavor, given that the book contains 39 chapters and over 600 pages long. Here, I investigate what insights we can glean from natural language processing (NLP) without reading the book.

## Google CoLab
  
First, I used the handy tool `wget` to load the book from the Guttenberg project into a Google CoLab notebook. In the notebook, I conducted an initial exploratory analysis of the book. A good initial tool to get the idea of a book's topics is to visualize a word cloud. In order to prepare the data for visualization, I tokenized the string into words and then removed "stop words." Stop words are wrods that occur very frequently, i.e. "the", "an", that are typically ignored in a variety of natural language processing tasks, both for space and efficiency. For example, if the word cloud just included stop words, that is not a very helpful visualization. After conducting these two tasks, I generated the word cloud using the Seaborn and matplotlib Python libraries. 

![alt text](https://github.com/razalamb1/exploratory-analysis-book/blob/main/wordcloud.png)

Even from this simple exploratory analysis, we can glean several useful insights about Grant's memoirs. A quick look at his [Wikipedia page](https://en.wikipedia.org/wiki/Ulysses_S._Grant) shows that he lived for ~63 years and had a long and varied career. In other words, his life was much more than just the Civil War. However, based on the word cloud, we can see that it is heavily focused on the Civil War, and perhaps army life in general. 

Another interesting aspect to invesgiate is locations. Using a Python list of U.S. states I found on the internet, I counted how often each state occurs within the Memoirs, and graphed it using pyplot. This graph is included below.

![alt text](https://github.com/razalamb1/exploratory-analysis-book/blob/main/states.png)

This graph also can provide some interesting insights into how Grant has written about his own life. The first thing to note, however, is that Washington occurs very frequently. Searching through the occurences of Washington in the book, simply using "ctrl+f", it is easily recognizable that most of these are either referencing a person or Washington, D.C. This is not surprising, given that the state of Washington was not given statehood until after Grant's death. However, putting that aside, we can see that Tennessee, Mississippi, and Virginia occur most frequently in the corpus. A trip back to Grant's Wikipedia page reveals that he spent his entire childhood in Ohio, which is interesting because Ohio is only the fourth most mentioned state (exlcuding Washington). The three most mentioned states can all be tied to war endeavors: Virginia was an incredibly important state in the Civil War, while Grant held military commands in Mississippi and Tennessee. Again, we can see that Grant appears to focus mostly on the war and other military endevaors, at least based on this exploratory analysis.

## Amazon Comprehend

There is another critical angle to approach text analysis from: sentiment. However, sentiment analysis can be complicated and time-consuming. Here, I utilize Amazon Comprehend as a no-code/low-code approach to sentiment analysis. In order to get a sense of the sentimental flow of Grant's memoirs, I used regular expressions to split the book into the preface and each of the 39 chapters, then engaged boto3 to utilize Amazon Comprehend on each Chapter. Subsequently, I graphed how the sentiments change across the course of the book.

![alt text](https://github.com/razalamb1/exploratory-analysis-book/blob/main/display.png)

While the graph is fairly noisy, and the most freqeuent sentiment is "neutral" (not surprising for a stoic military general), we can identify some negative (and a few positive) peaks in the book. We can then take these peaks and compare them to the names of the Chapters in the Memoirs. For example, the most positive chapter is: *"CHAPTER XIV. RETURN OF THE ARMY--MARRIAGE--ORDERED TO THE PACIFIC COAST--CROSSING THE ISTHMUS--ARRIVAL AT SAN FRANCISCO."* The keyword "marriage" may provide some substantial insight into why this chapter is positive. On the other hand, the most negative chapter is "CHAPTER XX. GENERAL FREMONT IN COMMAND--MOVEMENT AGAINST BELMONT--BATTLE OF BELMONT--A NARROW ESCAPE--AFTER THE BATTLE." However, this is more difficult to parse. Overall, we can see that while neutral is very common, the book is definitely more negative than positive, also somewhat unsurprising for a military general.

## Conclusion

From this no-code/low-code analysis using two different platforms, I was able to glean top level insights from Ulysess S. Grant's memoirs without actually reading all 600 pages. First of all, it is evident from the word cloud and the geographical bar chart that Grant heavily focuses on his military endevaours, especially the civil war, and does not focus as much on his presidency or childhood. Subsequetnly, using Amazon Comprehend, we can identify the sentiment of various chapters, and conclude that the book is largely neutral, but does have a few chapters that are largely negative, and one chapter that has measurable positive sentiments. Overall, this is a good demonstration of how low-code/no-code can be a beneficial approach to NLP tasks.

