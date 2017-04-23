
## Final Project _ End of Day Stock Prices Analysis
In this project, I explore and do some analysis on stock. I picked AAPL(Apple Inc.) to do some simple visualization and calcualte its moving average, EMA, DIF, DEM and MACD to analyze the trend of Apple stock.

### Data set
Data used in this priject is requested from Quandl(https://blog.quandl.com/api-for-stock-data). And then download it to data floder
    - raw_data = request.urlopen('https://www.quandl.com/api/v3/datasets/EOD/AAPL.csv?api_key='+api_key)

Data Format

Date	Open	High	Low	Close	Volume	Dividend	Split	Adj_Open	Adj_High	Adj_Low	Adj_Close	Adj_Volume
0	2017-04-21	142.44	142.68	141.85	142.27	17320928.0	0.0	1.0	142.44	142.68	141.85	142.27	17320928.0
1	2017-04-20	141.22	142.92	141.16	142.44	23319562.0	0.0	1.0	141.22	142.92	141.16	142.44	23319562.0
2	2017-04-19	141.88	142.00	140.45	140.68	17328375.0	0.0	1.0	141.88	142.00	140.45	140.68	17328375.0

### Analysis 1 - Calculate the moving average of Adj_Close and plot
"In statistics, a moving average (rolling average or running average) is a calculation to analyze data points by creating series of averages of different subsets of the full data set." -- Wiki

In this part, I visualize Adj_Close and Volume and then calcualte moving average of Adj_Close.
![alt](https://github.com/leileih/Hu_Leilei_Spring2017/blob/master/final/analysis/ana_1_output/Adj_Close.png?raw=true)
![alt](https://github.com/leileih/Hu_Leilei_Spring2017/blob/master/final/analysis/ana_1_output/Volume.png?raw=true)
![alt](https://github.com/leileih/Hu_Leilei_Spring2017/blob/master/final/analysis/ana_1_output/moving_average.png?raw=true)

#### Conclusion
Though Volume is noticeably volatile, Adj_Close and the moving average of Adj_Close shows that stock price of AAPL generally increases in past 2 years.

### Analysis 2 - Adj_Volume and its moving average in one plot
   Generate volume bar chart and add its moving average in lines. if close price is greater than open price, the volume bar that day is green, otherwise, it's red.
![alt](https://github.com/leileih/Hu_Leilei_Spring2017/blob/master/final/analysis/ana_2_output/volume+moving_average.png?raw=true)

#### Conclusion
This volume moving average plot shows the volums of AAPL is stable in these two years.

### Analysis 3 - EMA ,DIF, DEM, MACD
- What is EMA?
    - "An exponential moving average (EMA) is a type of moving average that is similar to a simple moving average, except that more weight is given to the latest data. It's also known as the exponentially weighted moving average. This type of moving average reacts faster to recent price changes than a simple moving average."(investopedia.com)
- DIF = EMA(close, 12) - EMA(close, 26)
- DEM = EMA(DIF, 9)
- MACD = (DIF - DEM) * 2
![alt](https://github.com/leileih/Hu_Leilei_Spring2017/blob/master/final/analysis/ana_3_output/EMA.png?raw=true)
![alt](https://github.com/leileih/Hu_Leilei_Spring2017/blob/master/final/analysis/ana_3_output/DIF+DEM+MACD.png?raw=true)

#### Conclusion
Same as MA, EMA shows this stock is increasing stable in these two years.
MACD is a trading indicator used in technical analysis of stock prices, professional could obtain amount of information from it. From this 4-month chart, maybe it's not a good chance to buy the stock in this two period if you would like to sell it in nearly period.


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
