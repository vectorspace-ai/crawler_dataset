# crawler_dataset
Shouldn't be too hard to run or understand...I hope<br/>
1. Make a virtual environment folder, generate the virtual environment and put the Crawler_Trainer_Matrix-generator inside here preferably<br/>
2. Be sure to have pandas, scrapy, gensim, nltk(with stopwords and punkt)<br/>
3. In the folder, open crappy_scrapy/spiders and run the crawler with the following command: scrapy runspider reuters_spider.py -o output.csv   (or whatever you want to call your output file, just make sure it's .csv)<br/>
4. wait for 30min-1hr until all possible combinations have been scraped<br/>
5. take the output file, copy it to the word2vec folder, and run processor.py with the output file as argument<br/>
6. after this is done, run correlation_matrix_generator<br/>
7. Now you should have a horrendous but cool looking dataset<br/>
<br/>
<br/>
TODO: include all of the stocks from markets other than NASDAQ<br/>
Actually assign proper labels to each document so that the vector for each symbol is associated with the words in their associated documents<br/>
Include contexts like the industries the companies specialize in and maybe even key people<br/>