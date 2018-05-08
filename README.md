# TwitterNYDataAnalysis
Data Aggregation, Big Data Analysis and Visualization of Twitter Data and NY Times Data
Implemented a model to collect tweets and news articles from Twitter and NYTimes using API for a keyword. Analyzed the data using Hadoop and visualized the high frequency words and their correlation using d3.js.
twitter.ipynb and nytimes_data.ipynb is used to collect tweets and news article related to a topic. The topic is currently hard-coded and can be changed in the file. NewsData\NewsData_1.txt, NewsData\NewsData_2.txt, TwitterData\TwitterData1.txt, TwitterData\TwitterData2.txt are the news articles and tweets collected using twitter.ipynb and nytimes.ipynb. These files are used as input to Hadoop.Hadoop\Twitter\WordCount contains the mapper and reducer for wordcount on Twitter data. Hadoop\News\WordCount contains the mapper and reducer for wordcount on News articles.Hadoop\News\CoOccurence contains the mapper and reducer for high frequency word cooccurence on News articles and Hadoop\Twitter\CoOccurence contains the mapper and reducer for high frequency word cooccurence on twitter data. After the analysis output from Hadoop, D3_js_input.ipynb needs to be used to create an input file for d3.js. Then d3-wordcloud-master\example\example can be used to create visualizations.