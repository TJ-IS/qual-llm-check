---
otero_id: 6350
otero_key: "YSNXNNW5"
title: "Deep learning for decision making and the optimization of socially responsible investments and portfolio"
authors: "Nhi N.Y. Vo; Xuezhong He; Shaowu Liu; Guandong Xu"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113097"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Deep learning for decision making and the optimization of socially responsible investments and portfolio

![](/api/attachments/YSNXNNW5/fulltext/images/76abcaddf7a459aaa18a73bb8b0f089bf2b2ec4be020a8885c3a1ce788c7298b.jpg)

Nhi N.Y. Vo<sup>a</sup>, Xuezhong He<sup>b</sup>, Shaowu Liu<sup>a</sup>, Guandong Xu<sup>a,\*</sup>

<sup>a</sup> Advanced Analytics Institute, University of Technology Sydney, 2-12 Blackfriars Street, Chippendale NSW 2008, Australia <sup>b</sup> Business School, University of Technology Sydney, 14-28 Ultimo Rd, Ultimo NSW 2007, Australia

## A R T I C L E I N F O

Keywords: Socially responsible investment Portfolio optimization Multivariate analytics Deep reinforcement learning Decision support systems

## A B S T R A C T

A socially responsible investment portfolio takes into consideration the environmental, social and governance aspects of companies. It has become an emerging topic for both financial investors and researchers recently. Traditional investment and portfolio theories, which are used for the optimization of financial investment portfolios, are inadequate for decision-making and the construction of an optimized socially responsible investment portfolio. In response to this problem, we introduced a Deep Responsible Investment Portfolio (DRIP model that contains a Multivariate Bidirectional Long Short-Term Memory neural network, to predict stock returns for the construction of a socially responsible investment portfolio. The deep reinforcement learning technique was adapted to retrain neural networks and rebalance the portfolio periodically. Our empirical data revealed that the DRIP framework could achieve competitive financial performance and better social impact compared to traditional portfolio models, sustainable indexes and funds.

## 1. Introduction

Traditionally, investors have focused on the investment returns by actively looking at the financial reports to find the best performing stocks. With the recent mindset change towards sensitive topics like global warming or refugees, investors are becoming concerned with other aspects of companies rather than just earnings. They are shifting their investment towards companies which are actively doing good things for the environment, contributing to the society and operating with transparency. According to the 2018 Biennial Report On US Sustainable, Responsible and Impact Investing Trends [51], Socially Responsible Investment (SRI) assets accounted for \$12 trillion out of \$47 trillion in total assets under professional management in the United States in 2018, representing a sharp increase of 38% since 2016.

Conventional investment and portfolio theory focuses on financia performance, i.e., the returns and risks of the portfolio [55]. Direct application of the theory might not be suitable for SRI because it focuses more on non-monetary objectives [6]. Therefore, socially responsible investors need a modified version of the modern portfolio theory that can serve their purpose better [38]. Besides, SRI investors currently have to read Corporate Social Responsibility (CSR) reports to find good companies to invest in, which is time-consuming and difi cult. The lack of efective quantitative approaches for SRI makes it more dificult for not only professional investors, but also the vast majority of lay investors. Therefore, this research will provide an easy and automated way of doing such investments in an ethical manner, which greatly benefits their decision-making and secures the optimal investment returns. This is one of the main motivational purposes for thi research.

Recently, the Global Reporting Initiatives (GRI) and the United Nation Sustainable Development Goals (SDGs) have provided standardized metrics and frameworks for companies to disclose more information regarding their sustainability practices [14]. For example, Environmental, Social and Governance (ESG) metrics of companies have been derived from reports and news articles (e.g. CSR reports, news articles, carbon disclosure project ratings), evaluating the company in diferent prospects (e.g. air emissions and waste management, employee health and safety control, board transparency and diversity) including their controversies (e.g. involvement in adult entertainment or gambling). These metrics have been consolidated into the combined ESG ratings (see Fig. 1). The availability of ESG ratings has led to an emerging research topic in SRI portfolio.

With the availability of ESG metrics, quantitative methods can now be applied efectively to address the SRI portfolio construction problem. Current data mining approaches in this research field face a number of challenges. The first challenge is the accuracy of multivariate time series predictions. Stock return forecasts have been extensively studied with various quantitative finance and machine learning models [24,

![](/api/attachments/YSNXNNW5/fulltext/images/69849637baaf0a78a6a2b3c7cfbbf2a1283a97152983c76323a9de6cab13bd99.jpg)  
Fig. 1. Combined ESG ratings [50].

44]. Most of these works have been focused on univariate time series predictions because it is expected that multivariate data would contain too much noise for the neural network to perform well [20, 33]. However, stock movements in the financial market are highly correlated; thus a multivariate model can learn these deep insights better than a combination of univariate networks. Following recent advances in neural networks research, especially Long Short-Term Memory networks (LSTM) [26], the application of deep learning in the predictive investment field has become an alternative approach to the traditional financial model. In this paper, we propose a novel Multivariate Bidirectional LSTM neural network to predict multiple time series for stock returns.

The second challenge faced by current approaches in SRI is the application of multi-objective portfolio construction. Existing portfolio optimization methods are evolving around the standard Mean-Variance (MV) Portfolio [32], which focuses on maximizing returns and mini mizing risks. To incorporate corporate responsibility performance into our optimization problem, we introduced a modified MV model for SRI portfolio construction by integrating ESG ratings.

The third challenge for SRI portfolio is building a model that can adapt to market movements. As SRI in particular, and financial in vestment in general, are sensitive to market volatility, model para meters should be tuned up periodically to achieve both financial per formance and ESG rating objectives. By adopting reinforcement learning techniques, we introduced a Deep Responsible Investment Portfolio model to retrain the prediction model and rebalance the portfolios efectively and autonomously.

An advantage of our proposed approach, which incorporates a multivariate BiLSTM neural network and MV-ESG, is that the framework can be generalized and extended to other scenarios with a similar multivariate prediction and multi-objective optimization problem. The developed deep reinforcement learning framework could also accommodate diferent neural networks and AI algorithms to tackle other types of complex and highly intercorrelated problems.

The main contributions of our research are:

• A novel deep responsible investment portfolio framework to integrate deep neural networks, multi-objective optimization, and reinforcement learning. The framework could be applied to other similar contexts of multivariate predictive analytics.

• A novel DRIP model that can forecast the returns quarterly and yearly on investment instead of just daily, which is a more realistic scenario for investors. The model has been fully tested and deployed on real-life datasets containing 100 stocks over a period of 30 years.

• The first report (to the best of our knowledge) leverages deep learning and incorporates ESG ratings into a portfolio optimization

model.

This paper is organized as follows. In Section 1, we introduce the current background of socially responsible investment portfolios and their limitations, as well as give our motivation for our proposed reinforcement learning solution. In Section 2, we review the literature on socially responsible investment research, and the application of deep learning by focusing on recent methodologies that are closely related to this paper. In Section 3, we introduce the technical details of our DRIP model and in Section 4, we present our empirical studies that applied our novel algorithms to real-life financial datasets to construct socially responsible investment portfolios, evaluate the performance against some baseline models and explore the potential for further and related research. We provide our conclusions in Section 5.

## 2. Literature Review

## 2.1. Socially Responsible Investment

The optimization of financial portfolios has been researched extensively. Many approaches have been developed to build decision support systems for stock trading. This includes standard mathematical finance modeling, e.g. Mean-Variance (MV) [32], AutoRegressive Moving Average (ARMA) and Generalized AutoRegressive Conditional Heteroskedasticity (GARCH) models [18], text mining of financial news [35] and social media [25].

However, limited research has been carried out on socially responsible investment. Although the socially responsible investment was proposed in the 1980s [22], it only became a topic of interest for academia and industry in the past decade [15]. During this time, research has correlated ESG ratings with the financial performance of companies [16, 23] or socially responsible funds [2, 28, 34]. The availability of environmental, social and governance (ESG) ratings has enabled more research and application in this area in academia [54] and industry [51].

Many sustainability funds have ofered portfolios with certain values to attract investors to SRI. In management funds [46], there has been an increasing demand from sustainably conscious investors to have more SRI options [37]. Multiple sustainable indexes and funds have been constructed based on areas of investor interests (e.g. water treatment, clean tech, renewable energy, gender equality and diversity). The literature has shown that companies or sustainable funds with higher ESG ratings can outperform the lower ones financially in long-term investments [19].

The literature of qualitative research in SRI has focused on reviewing the performance of companies [4] and socially responsible indexes or funds [49], and not on a data-driven approach to incorporate sustainability into an investment system. Some of the research has criticized the current stock screening process of SRI funds [53] and has proposed that the full integration of ESG ratings would be more beneficial [1]. These findings underpin the main motivation for our research to develop a framework with full integration of ESG ratings. Our paper contributes to the current knowledge of the application of deep learning for the prediction of stock returns and ESG-based SRI portfolio opti mization.

## 2.2. Deep Learning for Stock Returns Forecasting

Researchers have undertaken extensive studies to solve the time series forecasting problem of stock returns using deep learning [9, 13, 33]. Many have suggested that diferent types of Recurrent Neural Networks (RNN) outperform traditional financial time series models in diferent markets [3, 7, 44]. RNN contains feedback loops in its recurrent layer, which enables the storage of information in the “memory cell” over time. However, it does not perform well when the learning requires long-term temporal dependencies.

Long Short-Term Memory (LSTM) is a special type of RNN that has been proven to be efective in text mining to predict stock returns [30]. LSTM contains “memory cells” that are able to retain information for longer periods of time [26]. Consequently, LSTM often performs better in sequential data and financial time series predictions compared with RNN [27, 36], particularly in the SRI context where investors are concerned more about long-term returns rather than the volatility of the short-term market.

Researchers have also compared the performance of diferent RNN architectures like LSTM and Gated Recurrent Unit (GRU) networks [40]. Others have suggested that Bi-directional LSTM (BiLSTM) might be a better option in a similar sequence prediction problem [8]. While the LSTM and GRU, with the unidirectional flow of information, might be adequate in most sequence prediction problems, the BiLSTM model reads the data one more time backward [42] which helps improve prediction accuracy, particularly in forecasting sequential data like financial time series.

Recently it was suggested that back-testing results could have given rise to false positives due to the normalization of testing data and prediction of the next time step only [43]. The next-time step prediction is only suitable for high-frequency trading strategies using intra-daily data, such as foreign exchange markets. In SRI, investors are more in terested in long-term returns on investment. Conversely, research has been conducted on the long-term prediction for financial indexes with 1-year and 2-year time gaps, suggesting that long-term forecasting is possible for stock returns [17].

Our paper contributes to the current deep learning methodologies through the design of a novel BiLSTM neural network that predicts a long-term multivariate time series. To avoid false positive results, the financial returns data is not normalized and the model predicts multiple steps ahead. By constructing the baseline models using diferent types of LSTM networks as undertaken previously, we evaluate the prediction accuracy of the LSTM networks in the forecasting of SRI stock returns.

## 2.3. Portfolio Optimization

Few socially responsible investment models have been developed and proposed that utilize ESG ratings [52]. [21], for example, suggested a modification to the standard portfolio selection model with ESG scores. They utilized the Mean-Variance Stochastic Goal Programming (MV-SGP) model with a statistical approach for ESG screening on stocks based on scores and controversy risk. However, they did not consider predictive analytics; they only used past returns and volatility to test their hypotheses. Furthermore, they did not validate their models with real financial data.

Multiple optimization functions are available, including the

Expectation Maximization (EM) algorithm [12], quasi-Newton [5] or Powell methods [39]. However, most of them are not multi-objective or allow the special limit conditions that are required in a complex context like in socially responsible investment. The Sequential Least SQuares Programming (SLSQP) method proposed by [29], for example, can be used to minimize a function of various variables with a diferent combination of bounds, equality and inequality constraints. However, its greedy behavior leads to a skewed distribution for the weights of stocks in the portfolio. This is not an optimum choice for investors who are worried about non-diversified portfolios with extreme exposure risk.

We have developed a financial model to construct a socially responsible investment portfolio that incorporates the Mean-Variance portfolio theory and ESG ratings (MV-ESG). Our model is not based on the ESG screening approach. Instead, it filters and leverages the ESG ratings in a multi-objective optimization function based on the SLSQP method. It also considers both past and predicted the future perfor mance of stocks in a portfolio selection. This is one of the first mathematical models for constructing a socially responsible investment portfolio that achieves both better ESG ratings and competitive financial performance.

## 3. Methodology

Our DRIP framework consists of three main components: a multivariate BiLSTM neural network to predict stock returns quarterly and yearly; these predicted values are then combined with ESG ratings in our MVP- ESG model for portfolio construction; reinforcement learning techniques are then leveraged to automatically retrain the prediction models and re-balance our MVP-ESG portfolios after each period. The full reinforcement learning DRIP framework is as shown in Fig. 4.

## 3.1. Multivariate BiLSTM Neural Networks

Standard feature engineering often includes a normalization step, which transforms the data range to [0,1]. This common approach can help to improve the prediction accuracy of the neural networks. However, in the time series model, this approach implicitly tells the trained model the movement range of future stock prices, which makes out-of-bag testing results unrealistically accurate. We processed the input data for our neural networks in a diferent approach. In our DRIP model, we did not normalize data but instead fed the stock returns directly into the neural networks. We also trained the model to predict values with a longer time gap instead of a next period prediction, which is a more suitable scenario for stock investors in real-life trading.

Let $p _ { i } ( t )$ be the price at time t $( t = 1 , \ldots T )$ for stock ${ \bf \Psi } ( i = 1 , . . . N )$ . Δt was the time gap $( 1 < \Delta t < T )$ . The return r (t) for stock i at time t was $\begin{array} { r } { r _ { i } ( t ) = p _ { i } ( t ) - p _ { i } ( t - \Delta t ) } \end{array}$ . In the DRIP model, we used the sliding window technique to perform a rolling forecast. Let δt be the sliding window size. The train features matrix $X _ { i } ( t )$ and return vector $Y _ { i } ( t )$ for stock i at time t were:

$$
X _ {i} (t) = \left[ \begin{array}{c c c c} r _ {i} (t - T - \delta t) & r _ {i} (t - T - \delta t + 1) & \dots & r _ {i} (t - T) \\ r _ {i} (t - T + 1 - \delta t) & r _ {i} (t - T + 1 - \delta t + 1) & \dots & r _ {i} (t - T + 1) \\ \dots & \dots & \dots & \dots \\ r _ {i} (t - \delta t) & r _ {i} (t - \delta t + 1) & \dots & r _ {i} (t) \end{array} \right]
$$

$$
Y = \left| \begin{array}{l} r _ {i} (t - T + \Delta t) \\ r _ {i} (t - T + 1 \Delta t) \\ \dots \\ r _ {i} (t + \Delta t) \end{array} \right|\tag{1}
$$

(2)

As suggested by [36], LSTM networks would outperform other neural networks in solving similar problems due to its information persistence characteristic. We considered three types of LSTM neural networks:

• LSTM, initially proposed by [26], is a special kind of RNN, which is capable of learning long-term dependencies. For each input vector $x _ { t }$ at time step t, LSTM network uses multiple gating functions: the input gate $i _ { t s }$ forget gate $f _ { v }$ and output gate $o _ { t } ,$ together with a memory cell $C _ { t }$ to preserve long-term information and keeps track of its flow. The forget gate $f _ { t }$ and input gate $i _ { t }$ generated at each time step t are defined as follows:

$$
f _ {t} = \sigma (W _ {f} {\cdot} [ h _ {t - 1}, x _ {t} ] + b _ {f})\tag{3}
$$

$$
i _ {t} = \sigma (W _ {i} [ h _ {t - 1}, x _ {t} ] + b _ {i})\tag{4}
$$

In the next step, a tanh layer generates a new memory cell $\boldsymbol { \widetilde { C } } _ { t } .$ . LSTM then updates the old memory cell $C _ { t }$ and generates the output gate o and hidden state $h _ { t \cdot }$

$$
i _ {t} = \tanh (W _ {C} [ h _ {t - 1}, x _ {t} ] + b _ {C})\tag{5}
$$

$$
C _ {t} = f _ {t} \odot C _ {t - 1} + i _ {t} \odot \tilde {C} _ {t}\tag{6}
$$

$$
o _ {t} = \sigma (W _ {o} [ h _ {t - 1}, x _ {t} ] + b _ {o})\tag{7}
$$

$$
h _ {t} = o _ {t} \odot t a n h (C _ {t})\tag{8}
$$

where σ is the sigmoid function and ⊙ is the element-wise multi plication. W is the weight matrix and b is the bias vector to be learned by the LSTM at each specific gate.

BiLSTM is a variation of the bidirectional RNN, firstly introduced by [42]. It concatenates a forward and backward unidirectional LSTM on the stock return time series Combined $( h _ { t } ) = [ \overrightarrow { h _ { t } } , \overleftarrow { h _ { t } } ]$ ]. Unidirectional LSTM only preserves long-term information of the past, while BiLSTM can preserve information from both past and future by using the combined two hidden states Combined(h ).

• GRU is a more recent alteration of LSTM, suggested by [10]. It concatenates both the forget gate $f _ { t }$ and input gate $i _ { t }$ into a single update gate ${ z } _ { t } ,$ and merges the cell state $C _ { t }$ and hidden state $h _ { t } .$ The architecture of GRU is simpler than the standard LSTM one. The hidden state $h _ { t }$ generated at each time step t is defined as follows:

$$
z _ {t} = \sigma (W _ {z} \cdot [ h _ {t - 1}, x _ {t} ])\tag{9}
$$

$$
r _ {t} = \sigma (W _ {r} \cdot [ h _ {t - 1}, x _ {t} ])\tag{10}
$$

$$
\widetilde {h} _ {t} = \tanh (W \cdot [ r _ {t} \odot h _ {t - 1}, x _ {t} ])\tag{11}
$$

$$
h _ {t} = (1 - z _ {t}) \odot h _ {t - 1} + z _ {t} \odot \tilde {h} _ {t}\tag{12}
$$

By simplifying the architecture of the LSTM, GRU may learn the data at the combined gate. However, this single update gate might not learn some hidden information efectively. Hence, the performance of GRU networks may be less efective in forecasting long-term time series (Fig. 2).

For our DRIP model, we designed a special type of BiLSTM to perform multivariate time series prediction. The data input shape for the multivariate BiLSTM neural network was in the form of a three-dimensional matrix with sizes $( T \mathrm { ~ } - \Delta t - \delta t , \delta t , N )$ , where N was the number of stocks in total, δt was the sliding window size, and Δt was the prediction time gap (see Fig. 4).

We also replicated neural network models with LSTM and GRU networks as in [40] to predict returns for every single stock in the portfolio. We constructed the neural networks with recurrent layer using the Adam optimizer from the “Keras” package [11]. This network also contained a dense layer and a final output layer with the “linear” activation function to predict the stock returns $r _ { i } ( t + \Delta t )$ in Δt periods of time.

## 3.2. MV-ESG Model

The Mean Variance portfolio (MV) of [32] has always been the standard portfolio selection model. Its mathematical principle is constructed by two main components: maximizing the return $r _ { p }$ and minimizing the risk $\sigma _ { p } .$ The output of this optimization process is the eficient frontier, which is a set of investment portfolios with a greater return than any other with the same or less risk, and a lower risk than any other with the same or greater return. For illustration, the eficient frontier is plotted in Fig. 3 with the risk on the horizontal axis and the return on the vertical axis.

The optimal portfolio based on the eficient frontier is commonly known as the maximum Sharpe portfolio (MAX-S), where the portfolio has a maximum Sharpe ratio calculated as $S _ { p } = ( r _ { p } - r _ { f } ) / \sigma _ { p }$ . For the MAX-S portfolio, considering the risk free rate $r _ { f }$ (normally the return on bond investment or the bank interest rate), it minimizes the negative Sharpe Ratio [45]:

$$
m i n (- S _ {p}) = m i n (- \frac {r _ {p} - r _ {f}}{\sigma_ {p}})\tag{13}
$$

$$
r _ {p} = \sum_ {i = 1} ^ {N} w _ {i} r _ {i}\tag{14}
$$

$$
\sigma_ {p} = \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} w _ {i} \sigma_ {i j} w _ {j}\tag{15}
$$

where $w _ { i }$ and $w _ { j }$ are the weights of stock i and $j ,$ with the boundary limit $w _ { i } w _ { j } \in [ 0 , 1 ]$ , and $\sigma _ { i j }$ is the covariance matrix of the two stock i and j in the portfolio. The initial weight of each stock in the computation will be equally allocated according to the total number of stocks N in the portfolio, $w _ { i } ( 0 ) = w _ { i } ( 0 ) = 1 / N$

In our MV-ESG model, we built a multi-objective algorithm based on the SLSQP method [29] with three objectives: maximizing returns, minimizing volatility and maximizing ESG ratings. This algorithm minimized: $m i n _ { w e s g } | | - G | |$ with G being a three-dimensional matrix of constraints of the three objectives and wesg being the ESG weights subject to boundary limits inferred from the companies' ESG ratings.

For comparison, we constructed a maximum ESG portfolio (MAX-ESG) for investors with low risk averse to compare with the standard MAX-S portfolio. In MAX-ESG, we minimized the negative Sharpe Ratio with the portfolio ESG ratings $( E S G _ { p } )$ as a new variable of the objective function.

$$
m i n (- \widetilde {S} _ {p}) = m i n (- E S G _ {p} \frac {r _ {p} - r _ {f}}{\sigma_ {p}})\tag{16}
$$

$$
E S G _ {p} = \sum_ {i = 1} ^ {N} w e s g _ {i} \frac {E S G _ {i} + E \bar {S} G _ {i}}{2}\tag{17}
$$

where $E S G _ { i }$ was the combined ESG ratings of company i in the past year, $E \bar { S } G _ { i }$ was the combined ESG ratings at the current prediction year, and wesg was the ESG weight of stock i in the portfolio.

In the traditional MV model, $r _ { p }$ and $\sigma _ { p }$ are the past returns $r _ { i }$ and volatility $\sigma _ { i s }$ which is often called ex-post MV. In recent years, researchers and investors have been using the expected returns r¯ and volatility $\bar { \sigma } _ { i } .$ This approach called ex-ante MV is more suitable for predictive analytics in real-world financial trading. In our MV-ESG model, we combined both ex-post MV and ex-ante MV for portfolio selection and replaced the standard weight boundary with our ESG ones calculated based on the combined ESG ratings for each stock. Our MV-ESG model was computed using:

Calculated Portfolio Optimization based on Efficient Frontier  
![](/api/attachments/YSNXNNW5/fulltext/images/55772cb8065dd70df71043718b690020f586fa5313fd88b2a1221238a4e39383.jpg)  
c) BiLSTM Network

Fig. 2. Graphical illustration of LSTM, GRU and BiLSTM.  
![](/api/attachments/YSNXNNW5/fulltext/images/9b4a1b8c794f5100e4a684f81fb15a8169309b1ef1b911dbbf215f55e60ca094.jpg)  
Fig. 3. Standard MV portfolio with eficient frontier.

$$
r _ {p} = \sum_ {i = 1} ^ {N} w e s g _ {i} \frac {r _ {i} + \bar {r} _ {i}}{2}\tag{18}
$$

$$
\sigma_ {p} = \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} w e s g _ {i} \frac {\sigma_ {i j} + \bar {\sigma} _ {i j}}{2} w e s g _ {j}\tag{19}
$$

where $r _ { i }$ and r¯ were the ex-post and ex-ante returns, σ and $\bar { \sigma } _ { i j }$ were the ex-post and ex-ante covariance matrix of the two stock i and j in the portfolio. wesg and wesg were the ESG weight of stock i and j in the portfolio, with the boundary limit wesg ,∈ [0,1] for the company with the highest combined ESG score, then gradually decreasing to wesg ∈ [0,0] for the company with the lowest combined ESG score. This means the allocation of the company $^ { * } N ^ { * }$ in the portfolio was zero, indicating no investment in that company. The initial weight of each stock in the computation was not to be equally allocated but assigned according to the ESG ratings.

## 3.3. DRIP Model with Reinforcement Learning

We combined the multivariate BiLSTM neural networks and the MV-ESG models into a single integrated reinforcement learning model named Deep Responsible Investment Portfolio (DRIP). Starting with a set of agent states S and a set of possible portfolio allocation sets $A ,$ we had the probability of the DRIP model selecting the specific portfolio allocation (the “action”) a when in state s at time step t as:

$$
\pi \colon S \times A \to [ 0, 1 ]\tag{20}
$$

$$
\pi (a | s) \colon P r (a _ {t} = a | s _ {t} = s)\tag{21}
$$

We defined a simple state-value function $V _ { \pi } ^ { s }$ as the expected reward starting with the state $s _ { 0 } = s$ and $R e _ { t }$ denoting the reward function calculated as the sum of future discounted rewards:

$$
V _ {\pi} ^ {s} = E [ R e ] = E [ \sum_ {t = 0} ^ {\infty} \gamma^ {t} R e _ {t} | s _ {0} = s ]\tag{22}
$$

$$
R e = \sum_ {t = 0} ^ {\infty} \gamma^ {t} \widetilde {S} _ {t} (1 / M S E _ {t})\tag{23}
$$

where $\gamma \in [ 0 , 1 ]$ was the discount rate. $\widetilde { S } _ { t }$ was the ESG-adjusted Sharpe Ratio [45], and MSE was the mean squared error of the prediction model. The DRIP model found a set of portfolio allocation to maximize

![](/api/attachments/YSNXNNW5/fulltext/images/9fce32b5cfb833971f894fa2623b20e5dca01dc6151c92ac213e64aa26413fa8.jpg)  
Fig. 4. Reinforcement learning DRIP model.

the expected return.

After each time gap Δt, DRIP retrained the prediction model with new stock prices data and then, together with the portfolio performance and stock weights from the previous period of time, constructed a new portfolio with updated allocation weights. The reinforcement learning was repeated on a predefined period basis, to improve the prediction model accuracy and the performance of the portfolio over time. The design of DRIP enabled its self-learning with the least human involve ment as possible. The reinforcement learning model is shown in Fig. 4.

## 4. Empirical Experiment

We designed experiments to test our proposed model in two parts: 1) DRIP model forecasts for quarterly and yearly returns of multivariate stock time series during the three year period from 2016 to 2018; and 2) Socially Responsible Portfolios optimization using the predicted returns and reinforcement learning DRIP model framework.

## 4.1. Datasets

Currently, there are various ESG rating services available [41], many of which ofer a subscription fee for data access which limits its availability to the public. In 2018 however, Yahoo Finance made some of the ESG ratings obtained from Sustainalytics [48] available publicly. In this research, we utilized Yahoo Finance to obtain both financial stock prices and public ESG rating datasets in our reinforcement learning DRIP framework.

We downloaded the daily closing prices of all stocks in the Standard and Poor 500 list (S&P500) from the past 30 years from 31 December 1988 to 31 December 2018. In order to ensure a suficient number of data points, we removed all the stocks which did not have a market price on 31 December 1988, which left us with 262 companies. SRI investors do not invest in companies with low ESG ratings; therefore we used a simple stock screening process to remove these unwanted stocks. From the shortlisted 262 stocks, we selected the top 100 companies with the highest combined ESG ratings according to Sustainalytics to construct the final dataset that contained a total of 756,000 data points.

We separated the train and test datasets using an out-of-bag approach, which excludes the testing period data from the past historical data at time t to avoid feeding the model any unknown future information. Our data splitting ratio is 9:1, which meant that the training data was from the year 1989 to 2015 for each stock, and the testing data was the three-year period from the year 2016 to 2018. We also adopt the rolling forecast approach to further split the data in the testing period into validation and test sets. For quarterly return prediction, we used $^ { \alpha } Q 4 / 2 0 1 5 ^ { \gamma }$ and $^ { \ d } \mathrm { Q } 1 / 2 0 1 6 ^ { \dprime }$ as the validation and test set for the first period. We then moved to the next quarter period until “Q3/2018” and “Q4/2018” as validation and test sets in the last period. We applied the same data splitting process to the yearly return prediction dataset.

## 4.2. Evaluation Metrics

To test our DRIP model, we used the Mean Absolute Error (MAE) and the Root Mean Squared Error (RMSE) as the evaluation metrics for the absolute value prediction:

$$
\mathrm{MAE} = 1 / N \sum_ {i = 1} ^ {N} | \widetilde {r _ {i}} - r _ {i} |\tag{24}
$$

$$
\mathrm{RMSE} = \sqrt {1 / N \sum_ {i = 1} ^ {N} (\widetilde {r _ {i}} - r _ {i}) ^ {2}}\tag{25}
$$

where N = 100 was the total number of stocks in the portfolio and r<sup>\~</sup> and $r _ { i }$ were the predicted and actual return of stock i for that period.

We also converted the predicted value to a binary label to evaluate the performance of uptrend or downtrend forecast using the prediction accuracy metric and the Area Under the Curve (AUC) scores with the Receiver Operating Characteristic (ROC) curve. The lower MAE and RSME together with the higher prediction accuracy and AUC scores indicate the better performance of the prediction model. Our baseline models for comparison are the LSTM and GRU neural networks as in [40] and a univariate standard BiLSTM model (Uni).

To evaluate the performance of our socially responsible portfolios using MV-ESG model, we compared its Sharpe Ratio against those of the standard MV portfolios and the reported financial performance from similar sustainable indexes and funds. The Sharpe Ratio was defined a $S = ( r _ { p } - r _ { f } ) / \sigma _ { p }$ where $r _ { p }$ was the portfolio annualized return, $\sigma _ { p }$ was the portfolio annualized volatility, and $r _ { f } = 2 \%$ was the nominal risk-free rate. A better performing portfolio had a higher Sharpe Ratio, which yielded higher returns if the risks were similar or a lower risk if the returns were the same.

The sustainable indexes for comparison were: Dow Jones Sustainability World Index (DJSI World), Dow Jones Sustainability World Diversified Select Index (DJSI WD), and S&P500 ESG Factor Weighted Index (S&P500 ESG). All indexes data were obtained on the 31 December 2018 from S&P Dow Jones Indices, a division of S&P Global. The sustainable Exchange Traded Funds (ETF) with their symbol codes in the brackets were: iShares Global Clean Energy ETF (ICLN), Invesco Solar ETF (TAN), iShares MSCI USA ESG Select ETF (SUSA) and Workplace Equality Portfolio (EOLT). All funds data were obtained on 31 December 2018 from Morningstar.

## 4.3. Prediction Model Results

First of all, we tested the performance of DRIP model on the pre diction of quarterly returns. The hyperparameters in our neural networks were set as: the number of units in the deep learning layers equaled to 100, batch size equaled to 1, the loss was the mean squared error and random seed equaled 0. We used Adam optimizer with learning rate $l r = 0 . 0 0 1 , \beta _ { 1 } = 0 . 9 , \beta _ { 2 } = 0 . 9 9 9$ , fuzz factor $\epsilon = 1 e - 7 ,$ and decay equaled to 0. We also set the number of epochs equaled to 10 with a checkpoint after each epoch and only saved the best model for prediction.

Our experiment setup was as follows: $\Delta t = 6 3 , \delta t = 6 3$ and the time gap was set to 63 representing the total number of trading days in a quarter. This meant that the model predicted the prices and returns three months ahead in time. After each period, the model was retrained and validated with the out-of-bag three-month data and predicted the next return in 63 days. The testing data for each quarter of each yea from 2016 to 2018 were referred to as $^ { \mathfrak { a } } \mathrm { Q } 1 ^ { \mathfrak { p } } , \ ^ { \mathfrak { a } } \mathrm { Q } 2 ^ { \mathfrak { p } } , \ ^ { \mathfrak { a } } \mathrm { Q } 3 ^ { \mathfrak { p } }$ and $^ { \mathfrak { a } } Q ^ { 4 ^ { \mathfrak { n } } }$ respectively.

We then tested the performance on the prediction of yearly returns with $\Delta t = 2 5 2 , \delta t = 2 5 2$ representing the 252 trading days in a typica year. The other setup was the same as in the quarterly returns predic tion model. The empirical results in Table 1 showed the performance evaluation for the quarterly and yearly returns prediction models using the multivariate financial time series as input. The reported RMSE and AUC Scores were averages for 100 stocks in each time period.

Our DRIP models, which used multivariate financial returns as the input significantly outperformed the other baseline models for most prediction periods in term of MAE and RMSE. We can conclude that the prediction model using multivariate financial returns and BiLSTM neural networks in our design was a better solution for this predictive analytic problem. Focusing on the trend prediction accuracy, except for the slightly worse results in $^ { \mathrm { 4 } } \mathrm { Q } 2 / 1 6 ^ { \prime \prime }$ and “Q3/18”, our DRIP models that used BiLSTM achieved higher prediction accuracy and AUC scores regardless of the time periods or of the quarterly or yearly returns. These results demonstrated the efectiveness of our approach, that the reinforcement learning had successfully captured the underlying hidden information in the inter-correlated multivariate series and improved itself over time.

Receiver Operating Characteristic Curve  
![](/api/attachments/YSNXNNW5/fulltext/images/4e2f83d78e876e9c35857ccb8475206d9a7e3dac61b20140e02888b4290bc215.jpg)  
Fig. 5. ROC curves.

The value predictions of quarterly returns generally had lower MAE and RSME than the yearly forecast. This result was expected as the time gap was smaller; hence, it was easier to forecast the absolute stock return values. The ROC curves in Fig. 5 showed a performance lift in the quarterly returns prediction model compared to other baselines for the entire 3-year testing period. Conversely, the trend prediction was more accurate in yearly return models, which proved that the reinforcement learning model could filter out the market noise in short-term price changes. Overall, our DRIP model efectively and accurately predicted the annual returns in all three years and the quarterly returns in 10 out of 12 testing periods. It showed that our prediction model was not overfitted to a certain dataset period, and it could be generalized for similar applications.

Table 1  
DRIP model evaluation.

<table><tr><td rowspan="2"></td><td colspan="15">Mean Absolute Error (MAE)</td></tr><tr><td>Q1/16</td><td>Q2/16</td><td>Q3/16</td><td>Q4/16</td><td>Q1/17</td><td>Q2/17</td><td>Q3/17</td><td>Q4/17</td><td>Q1/18</td><td>Q2/18</td><td>Q3/18</td><td>Q4/18</td><td>2016</td><td>2017</td><td>2018</td></tr><tr><td>DRIP</td><td>0.0547</td><td>0.0880</td><td>0.0578</td><td>0.0814</td><td>0.0600</td><td>0.0551</td><td>0.0555</td><td>0.0601</td><td>0.0692</td><td>0.0667</td><td>0.0771</td><td>0.0948</td><td>0.0754</td><td>0.0830</td><td>0.1017</td></tr><tr><td>Uni</td><td>0.0656</td><td>0.0930</td><td>0.0678</td><td>0.0999</td><td>0.0633</td><td>0.0704</td><td>0.0679</td><td>0.0683</td><td>0.0714</td><td>0.0882</td><td>0.0854</td><td>0.1096</td><td>0.0821</td><td>0.0974</td><td>0.1157</td></tr><tr><td>LSTM</td><td>0.0771</td><td>0.0960</td><td>0.0734</td><td>0.1043</td><td>0.0.0677</td><td>0.0767</td><td>0.0707</td><td>0.0718</td><td>0.0650</td><td>0.0986</td><td>0.0788</td><td>0.1404</td><td>0.0889</td><td>0.1074</td><td>0.1122</td></tr><tr><td>GRU</td><td>0.0652</td><td>0.0950</td><td>0.0723</td><td>0.1139</td><td>0.0623</td><td>0.0793</td><td>0.0776</td><td>0.0729</td><td>0.0801</td><td>0.0993</td><td>0.1003</td><td>0.0936</td><td>0.0819</td><td>0.1018</td><td>0.1332</td></tr><tr><td rowspan="2"></td><td colspan="15">Root Mean Squared Error (RSME)</td></tr><tr><td>Q1/16</td><td>Q2/16</td><td>Q3/16</td><td>Q4/16</td><td>Q1/17</td><td>Q2/17</td><td>Q3/17</td><td>Q4/17</td><td>Q1/18</td><td>Q2/18</td><td>Q3/18</td><td>Q4/18</td><td>2016</td><td>2018</td><td>2018</td></tr><tr><td>DRIP</td><td>0.0672</td><td>0.1080</td><td>0.0754</td><td>0.1209</td><td>0.0768</td><td>0.0741</td><td>0.0750</td><td>0.0790</td><td>0.0858</td><td>0.0843</td><td>0.1202</td><td>0.1165</td><td>0.1014</td><td>0.1062</td><td>0.1273</td></tr><tr><td>Uni</td><td>0.0822</td><td>0.1189</td><td>0.0863</td><td>0.1534</td><td>0.0806</td><td>0.0933</td><td>0.0887</td><td>0.0939</td><td>0.0926</td><td>0.1120</td><td>0.1333</td><td>0.1402</td><td>0.1135</td><td>0.1241</td><td>0.1461</td></tr><tr><td>LSTM</td><td>0.0957</td><td>0.1225</td><td>0.0911</td><td>0.1637</td><td>0.0847</td><td>0.0991</td><td>0.0944</td><td>0.1029</td><td>0.0849</td><td>0.1233</td><td>0.1238</td><td>0.1739</td><td>0.1287</td><td>0.1355</td><td>0.1425</td></tr><tr><td>GRU</td><td>0.0812</td><td>0.1254</td><td>0.0914</td><td>0.1708</td><td>0.0801</td><td>0.1041</td><td>0.0952</td><td>0.0981</td><td>0.1057</td><td>0.1238</td><td>0.1536</td><td>0.1191</td><td>0.1086</td><td>0.1286</td><td>0.1659</td></tr><tr><td rowspan="2"></td><td colspan="15">Area Under the Curve (AUC) Scores</td></tr><tr><td>Q1/16</td><td>Q2/16</td><td>Q3/16</td><td>Q4/16</td><td>Q1/17</td><td>Q2/17</td><td>Q3/17</td><td>Q4/17</td><td>Q1/18</td><td>Q2/18</td><td>Q3/18</td><td>Q4/18</td><td>2016</td><td>2018</td><td></td></tr><tr><td>DRIP</td><td>0.8392</td><td>0.5809</td><td>0.8387</td><td>0.8286</td><td>0.8495</td><td>0.7659</td><td>0.7521</td><td>0.8170</td><td>0.8165</td><td>0.8045</td><td>0.7024</td><td>0.9407</td><td>0.9525</td><td>0.9546</td><td>0.8989</td></tr><tr><td>Uni</td><td>0.7443</td><td>0.5803</td><td>0.7876</td><td>0.6603</td><td>0.8522</td><td>0.6052</td><td>0.6297</td><td>0.7486</td><td>0.7441</td><td>0.6477</td><td>0.6952</td><td>0.8502</td><td>0.9339</td><td>0.9397</td><td>0.8899</td></tr><tr><td>LSTM</td><td>0.7115</td><td>0.5946</td><td>0.7719</td><td>0.6320</td><td>0.8790</td><td>0.5069</td><td>0.5739</td><td>0.7001</td><td>0.7516</td><td>0.5692</td><td>0.7549</td><td>0.7278</td><td>0.9348</td><td>0.9106</td><td>0.8989</td></tr><tr><td>GRU</td><td>0.6821</td><td>0.5954</td><td>0.7522</td><td>0.5202</td><td>0.8281</td><td>0.5427</td><td>0.5632</td><td>0.7287</td><td>0.6642</td><td>0.5692</td><td>0.6884</td><td>0.8820</td><td>0.9142</td><td>0.9537</td><td>0.8720</td></tr><tr><td rowspan="2"></td><td colspan="15">Trend Prediction Accuracy (%)</td></tr><tr><td>Q1/16</td><td>Q2/16</td><td>Q3/16</td><td>Q4/16</td><td>Q1/17</td><td>Q2/17</td><td>Q3/17</td><td>Q4/17</td><td>Q1/18</td><td>Q2/18</td><td>Q3/18</td><td>Q4/18</td><td>2016</td><td>2018 2017</td><td>2018</td></tr><tr><td>DRIP</td><td>77%</td><td>50%</td><td>74%</td><td>76%</td><td>80%</td><td>66%</td><td>70%</td><td>77%</td><td>72%</td><td>76%</td><td>73%</td><td>85%</td><td>92%</td><td>92%</td><td>80%</td></tr><tr><td>Uni</td><td>69%</td><td>50%</td><td>73%</td><td>62%</td><td>77%</td><td>58%</td><td>65%</td><td>75%</td><td>65%</td><td>64%</td><td>70%</td><td>76%</td><td>91%</td><td>91%</td><td>78%</td></tr><tr><td>LSTM</td><td>64%</td><td>53%</td><td>76%</td><td>61%</td><td>75%</td><td>52%</td><td>66%</td><td>75%</td><td>66%</td><td>57%</td><td>74%</td><td>60%</td><td>92%</td><td>85%</td><td>79%</td></tr><tr><td>GRU</td><td>67%</td><td>57%</td><td>70%</td><td>48%</td><td>75%</td><td>56%</td><td>58%</td><td>73%</td><td>58%</td><td>58%</td><td>62%</td><td>84%</td><td>92%</td><td>92%</td><td>73%</td></tr></table>

Table 2  
Benchmarking prediction model with multiple hyperparameters.

<table><tr><td rowspan="2">Units</td><td rowspan="2">BS</td><td rowspan="2">LR</td><td colspan="2">Validation set</td><td colspan="2">Test set</td></tr><tr><td>MAE</td><td>Accuracy</td><td>MAE</td><td>Accuracy</td></tr><tr><td>100</td><td>1</td><td>0.001</td><td>0.05468</td><td>0.89635</td><td>0.09335</td><td>0.86111</td></tr><tr><td>100</td><td>20</td><td>0.001</td><td>0.04906</td><td>0.93016</td><td>0.09682</td><td>0.83270</td></tr><tr><td>300</td><td>10</td><td>0.001</td><td>0.04515</td><td>0.94413</td><td>0.09705</td><td>0.83841</td></tr><tr><td>300</td><td>20</td><td>0.001</td><td>0.04514</td><td>0.93460</td><td>0.10181</td><td>0.81857</td></tr><tr><td>100</td><td>10</td><td>0.0001</td><td>0.08325</td><td>0.78762</td><td>0.09744</td><td>0.81921</td></tr><tr><td>200</td><td>1</td><td>0.0001</td><td>0.06186</td><td>0.86063</td><td>0.09823</td><td>0.80857</td></tr><tr><td>300</td><td>1</td><td>0.001</td><td>0.04553</td><td>0.94000</td><td>0.09875</td><td>0.83413</td></tr><tr><td>100</td><td>1</td><td>0.0001</td><td>0.06901</td><td>0.82190</td><td>0.09913</td><td>0.78571</td></tr><tr><td>200</td><td>10</td><td>0.0001</td><td>0.07367</td><td>0.82063</td><td>0.09957</td><td>0.77841</td></tr><tr><td>300</td><td>20</td><td>0.0001</td><td>0.07198</td><td>0.79937</td><td>0.09988</td><td>0.79444</td></tr><tr><td>300</td><td>20</td><td>0.01</td><td>0.05908</td><td>0.86794</td><td>0.10055</td><td>0.80841</td></tr><tr><td>100</td><td>20</td><td>0.01</td><td>0.05021</td><td>0.92175</td><td>0.10056</td><td>0.82317</td></tr><tr><td>200</td><td>20</td><td>0.001</td><td>0.04866</td><td>0.93952</td><td>0.10097</td><td>0.78095</td></tr><tr><td>300</td><td>10</td><td>0.0001</td><td>0.07087</td><td>0.83746</td><td>0.10174</td><td>0.75841</td></tr><tr><td>100</td><td>10</td><td>0.01</td><td>0.04902</td><td>0.91206</td><td>0.10176</td><td>0.78556</td></tr><tr><td>100</td><td>10</td><td>0.001</td><td>0.05525</td><td>0.89238</td><td>0.10188</td><td>0.78444</td></tr><tr><td>200</td><td>10</td><td>0.001</td><td>0.05029</td><td>0.91651</td><td>0.10234</td><td>0.81032</td></tr><tr><td>200</td><td>20</td><td>0.0001</td><td>0.08412</td><td>0.79683</td><td>0.10321</td><td>0.78000</td></tr><tr><td>300</td><td>1</td><td>0.0001</td><td>0.05370</td><td>0.90238</td><td>0.10436</td><td>0.78762</td></tr><tr><td>100</td><td>1</td><td>0.01</td><td>0.06871</td><td>0.82365</td><td>0.10709</td><td>0.75921</td></tr><tr><td>200</td><td>20</td><td>0.01</td><td>0.05432</td><td>0.91683</td><td>0.11083</td><td>0.78190</td></tr><tr><td>200</td><td>1</td><td>0.001</td><td>0.04542</td><td>0.93571</td><td>0.11203</td><td>0.75000</td></tr><tr><td>100</td><td>20</td><td>0.0001</td><td>0.08296</td><td>0.75698</td><td>0.11208</td><td>0.70444</td></tr><tr><td>200</td><td>10</td><td>0.01</td><td>0.08924</td><td>0.82016</td><td>0.12027</td><td>0.74190</td></tr><tr><td>300</td><td>10</td><td>0.01</td><td>0.08880</td><td>0.76238</td><td>0.12863</td><td>0.74048</td></tr><tr><td>300</td><td>1</td><td>0.01</td><td>0.09793</td><td>0.74810</td><td>0.13317</td><td>0.65349</td></tr><tr><td>200</td><td>1</td><td>0.01</td><td>0.11110</td><td>0.76635</td><td>0.13671</td><td>0.74825</td></tr></table>

## 4.4. Robustness Test

To test the robustness of our model, we first benchmarked the prediction model using diferent combinations of the neural network hyperparameters. We split the dataset into train, validation and test sets with the ratio 8:1:1. The hyperparameter sets were: number of units in the deep learning layers was in [100,200,300], batch size (BS) was in [1,10,20] and learning rate (LR) was in [0.0001,0.001,0.01] accord ingly. The MAE and prediction accuracy results of both validation and test set are presented in Table 2.

Table 2 showed that diferent hyperparameter sets could result in varied MAE and prediction accuracy. The gap between validation and test results are not significantly large, which indicates that our model was not overfitted. Our setting to generate the best results in the test set was: number of units equaled 100, batch size equaled 1 and learning rate equaled 0.01. In our rolling forecast and reinforcement learning model, the hyperparameters could be automatically tuned using grid search after each period.

We then used this set of hyperparameters to test the prediction model on three diferent datasets with 50, 100 and 200 randomly selected stocks (denoted as “Random50”, “Random100”, “Random200”). We also split these datasets into train, validation and test sets with the ratio 8:1:1. The results of this experiment are presented in Table 3.

Table 3 showed that our model still achieved a good prediction accuracy in randomly selected stock datasets. It is worth noticing that the MAE and the prediction accuracy are not worsened for the larger dataset but varied due to the randomness of stock selection. These results indicated that our prediction model is robust and generalizable with diferent data sizes.

Table 3  
Benchmarking model with randomly selected datasets.

<table><tr><td rowspan="2">Data</td><td colspan="2">Validation set</td><td colspan="2">Test set</td></tr><tr><td>MAE</td><td>Accuracy</td><td>MAE</td><td>Accuracy</td></tr><tr><td>Random50</td><td>0.064246</td><td>0.85205</td><td>0.058508</td><td>0.779762</td></tr><tr><td>Random100</td><td>0.058567</td><td>0.809696</td><td>0.059457</td><td>0.755221</td></tr><tr><td>Random200</td><td>0.067143</td><td>0.827499</td><td>0.056684</td><td>0.818358</td></tr></table>

Table 4  
MV-ESG model evaluation.

<table><tr><td rowspan="2"></td><td colspan="2">2016</td><td colspan="2">2017</td><td colspan="2">2018</td></tr><tr><td>MAX-S</td><td>MAX-ESG</td><td>MAX-S</td><td>MAX-ESG</td><td>MAX-S</td><td>MAX-ESG</td></tr><tr><td>Return</td><td>32.73%</td><td>28.47%</td><td>47.76%</td><td>50.78%</td><td>30.33%</td><td>26.60%</td></tr><tr><td>Volatility</td><td>17.22%</td><td>14.89%</td><td>19.37%</td><td>19.18%</td><td>16.84%</td><td>14.31%</td></tr><tr><td>Sharpe ratio</td><td>1.7845</td><td>1.7777</td><td>2.3624</td><td>2.5431</td><td>1.6823</td><td>1.7191</td></tr><tr><td>ESG score</td><td>70</td><td>74</td><td>70</td><td>75</td><td>68</td><td>71</td></tr></table>

## 4.5. Portfolio Optimization Model Results

We used the predicted returns from the DRIP model as input for ou MV-ESG model to construct socially responsible investment portfolios. We constructed the MAX-ESG portfolios using predicted returns. The nominal risk free rate was set to 2%, $r _ { f } = 0 . 0 2$ . After obtaining the stock allocation in each portfolio, we calculated the actual annualized returns and volatility using real stock prices for that period. The annualized returns, volatility, Sharpe Ratio and ESG Score given in Table 4 were averaged for the entire year, for each year in the testing period.

The results showed that our MAX-ESG portfolios had consistently higher ESG ratings (3 to 5 points above). Even though the MAX-S portfolios had better financial returns in 2016 and 2018, they also showed a relatively higher volatility level. Conversely, our MAX-ESG portfolios still achieved great financial returns with lower risk. The Sharpe Ratios of the MAX-ESG portfolios were higher than those of the MAX-S ones for 2017 and 2018. In 2017, the MAX-ESG portfolio achieved a better financial return 50.78% at a lower risk level 19.19%, compared with 47.76% return at 19.37% volatility in the MAX-S portfolio. These findings showed that achieving a socially responsible investment portfolio, with higher ESG ratings, and without the sacrifice of a large financial return, was achievable with our MV-ESG model.

We compared the performance of our final MAX-ESG portfolio with reported financial returns in 2018 obtained from similar sustainable indexes and funds. The results in Table 5 show that our portfolio outperformed other indexes and funds in terms of financial performance and achieved the Sharpe Ratio of 2.0634. Our portfolio had the best 3- year annualized return of 35.28%. Particularly in 2018, all indexes and funds had negative returns because many large stocks were in the downtrend. Our MAX-ESG portfolio was still able to achieve a positive return. This was mainly because the portfolio constructed was based on the maximization of Sharpe Ratio in the MV-ESG model, which optimally selects stocks with higher returns.

Our model's 3-year annualized volatility was in third place with 16.13%. This higher level of risk aligned with common investment knowledge on diversification [47]. Because the indexes often consist of a larger number of stocks, they generally had lower risks. However, the level diversification of our SRI portfolio was suficient for individual investors. Our best MAX-ESG portfolio, for example, consisted of 7 stocks in 2016, 18 stocks in 2017 and 12 stocks in 2018 with the allocation as shown in Fig. 6. The model could be enhanced to construct a more diversified portfolio for sustainable investment funds with further constraints on weights.

Since all these indexes and funds published diferent types of sustainability metrics, we could not directly compare our portfolio ESG ratings to their benchmarks. We also could not report the net returns on investment due to the lacking of fund fees and tax calculation. In general, these results showed the efectiveness of our DRIP framework, not only for the optimization of socially responsible investment portfolios but also for financial stock investments in general.

Table 5  
Benchmarking MAX-ESG portfolio with sustainable indexes and funds in 2018.

<table><tr><td rowspan="2"></td><td colspan="3">Period returns</td><td colspan="3">3-year Annualized</td></tr><tr><td>2016</td><td>2017</td><td>2018</td><td>Return</td><td>Volatility</td><td>Sharpe ratio</td></tr><tr><td>MAX-ESG</td><td>28.47%</td><td>50.78%</td><td>26.60%</td><td>35.28%</td><td>16.13%</td><td>2.0634</td></tr><tr><td>S&amp;P500</td><td>11.29%</td><td>23.28%</td><td>-3.35%</td><td>10.41%</td><td>10.88%</td><td>0.7727</td></tr><tr><td>S&amp;P500 ESG</td><td>14.52%</td><td>21.24%</td><td>-8.44%</td><td>9.11%</td><td>11.76%</td><td>0.6043</td></tr><tr><td>DJSI World</td><td>8.23%</td><td>27.98%</td><td>-8.03%</td><td>9.39%</td><td>11.52%</td><td>0.6418</td></tr><tr><td>DJSI WD</td><td>10.71%</td><td>24.00%</td><td>9.54%</td><td>14.75%</td><td>10.48%</td><td>1.2166</td></tr><tr><td>ICLN</td><td>-16.91%</td><td>21.48%</td><td>-9.02%</td><td>-1.48%</td><td>17.11%</td><td>-0.2036</td></tr><tr><td>TAN</td><td>-43.23%</td><td>54.39%</td><td>-25.66%</td><td>-4.83%</td><td>23.00%</td><td>-0.2971</td></tr><tr><td>SUSA</td><td>12.15%</td><td>22.53%</td><td>-5.65%</td><td>9.68%</td><td>11.42%</td><td>0.6722</td></tr><tr><td>EQLT</td><td>13.93%</td><td>21.33%</td><td>9.22%</td><td>14.83%</td><td>11.80%</td><td>1.0870</td></tr></table>

## 4.6. Reinforcement Learning Test

Our reinforcement learning DRIP framework could be used to con struct socially responsible portfolios with higher ESG ratings that still achieved competitive financial returns. Our DRIP model could predict multiple time steps ahead, which is an important feature for stock investors. Furthermore, the model significantly outperformed the univariate networks in both prediction accuracy and training speed with the same epoch size in terms of both prediction accuracy and training speed. In our experiments, it took one hour to perform reinforcement learning with the multivariate BiLSTM: a combination of 100 univariate neural networks with 10 epochs typically takes 100-times more training duration compared to our approach. This finding could lead to a better computationally eficient approach because the multivariate BiLSTM takes N times less in total training duration.

![](/api/attachments/YSNXNNW5/fulltext/images/05139b0c4b15c42bebc910815fdf2898003488eff5d7b53421e6427694feae17.jpg)

![](/api/attachments/YSNXNNW5/fulltext/images/26f48e12c4b6e34232cd68f67550b086de9bacc405cce4e1dbe340b6820281eb.jpg)

![](/api/attachments/YSNXNNW5/fulltext/images/62d6763017ea91b1b456a75b93a5d954efb3e607e88243cd173c89f9f4769584.jpg)  
Fig. 6. MAX-ESG portfolio allocation (labels are trade symbols of companies).

Table 6  
Reinforcement learning test results

<table><tr><td rowspan="2"></td><td colspan="4">Prediction model</td></tr><tr><td>MAE</td><td>RSME</td><td>AUC</td><td>Accuracy</td></tr><tr><td>DRIP</td><td>0.0867</td><td>0.1117</td><td>0.9354</td><td>88%</td></tr><tr><td>Non-RL</td><td>0.1098</td><td>0.1499</td><td>0.5515</td><td>55%</td></tr><tr><td rowspan="2"></td><td colspan="4">MAX-ESG portfolio</td></tr><tr><td>Return</td><td>Volatility</td><td>Sharpe ratio</td><td>ESG score</td></tr><tr><td>DRIP</td><td>35.28%</td><td>16.13%</td><td>2.0634</td><td>73</td></tr><tr><td>Non-RL</td><td>5.30%</td><td>14.00%</td><td>0.2357</td><td>68</td></tr></table>

We also tested the performance of reinforcement learning by com paring the results to those without prediction model retraining and portfolio rebalancing (Non-RL). In the “Non-RL” framework, we still used the Multivariate BiLSTM networks for prediction model and the MV-ESG for SRI portfolio optimization. However, the models were retrained after each testing period (each quarter or each year) without any pre-trained model and parameter learning from previous periods. The results in Table 6 showed that reinforcement learning had significantly improved the model performance in terms of both the prediction of stock returns and the optimization of portfolios. Since we were working with multivariate time series, retraining models and rebalancing portfolios were proven to be essential. Therefore, our reinforcement learning approach within the DRIP system was suitable for this time-sensitive data analytics problem.

## 4.7. Discussion of Research

Overall, our research demonstrated a promising trend in applying deep learning techniques for the selection of socially responsible investment portfolios. With the current progress in artificial intelligence, we believe it will bring further breakthroughs in socially responsible investment research. Our research will not only contribute directly to current literature in various disciplines but also translate into benefits for responsible investors, funds or indexes in markets. In the AI research field, our prediction model with a BiLSTM network could serve as a baseline for further research of long-term stock return forecasting using neural networks. In this research, we only used a single type of neural networks and structured data (stock prices and ESG ratings) as input. Studying the diferent variations and combination of the deep neural networks, as well as incorporating unstructured data (news, company reports or social media content) with text mining approaches in SRI, was beyond the scope of this paper. However, our framework was designed with the flexibility to adopt diferent data mining approaches, neural networks or optimization algorithms in our future research.

Please be aware that by focusing on policies and rewards, our system might fail under extreme situations, e.g. a financial crisis. Our model's performance and applicability are subject to the hypothesis of stable company performances and normal finance market scenario. To safeguard investments in such cases, we would need additional failsafe measures when applying our model in practice.

From the financial research aspect. the MV-ESG model was one of the first to combine ESG ratings with a math finance model. Further research on how to incorporate this with other quantitative finance models such as GARCH [18] would be relevant to both SRI scholars and investors. As many researchers are working on similar approaches for oil price forecasting [31], we believe a further investigation into this direction would be beneficial for SRI researchers. For simplicity purpose, we did not take into account income tax rates, inflation rates, trading fees, and other financial fund management costs. Further calculation of these fees would help the model implementation in the realworld investment scene. Moreover, ESG ratings are not the only metrics to measure corporate social responsibility. The integration of hundreds of ESG sub-categorical ratings (e.g. greenhouse gas emissions or community support) could improve the model significantly. In our future research, we could study the potential of using deep learning approaches for a personalized stock recommendation system in the SRI context.

## 5. Conclusions

Socially responsible investment is an emerging research topic with potential for long-term social impact. In this research, we proposed the DRIP model, which leveraged deep learning techniques to predict financial returns and construct a socially responsible investment port folio. Validated with real-world data, our DRIP model, with a multivariate time series model, was able to accurately predict the stock returns three months ahead of time. It is possible that our framework could be generalized to build decision-support systems for similar multivariate prediction problems.

The socially responsible portfolios that we constructed using our novel MV-ESG model and reinforcement learning achieved much higher ESG ratings and a competitive financial performance overall compared with standard MV portfolio models and similar sustainable indexes and funds. With this rising trend in socially responsible investment, financial capital will diverge into good companies that contribute to a cleaner environment and a better society. This research also highlights a new direction for the use of more advanced deep learning approaches for quantitative finance research.

## Acknowledgment

This research is partly supported by Australian Research Council Linkage Project Scheme under Grant LP170100891. We also thank University of Technology Sydney for supporting us with the infrastructures and computing power for empirical studies. We would also like to thank the editor and anonymous reviewers for their constructive and insightful feedbacks.

## Refrences

[1] A. Amel-Zadeh, G. Serafeim, Why and how investors use ESG information: evidenc from a global survey, Financ. Anal. J. 74 (3) (2018) 87–103.

[2] B.R. Auer, F. Schuhmacher, Do socially (ir) responsible investments pay? New evidence from international ESG data, Q. Rev. Econ. Finance 59 (2016) 51–62

[3] W. Bao, J. Yue, Y. Rao, A deep learning framework for financial time series using stacked autoencoders and long-short term memory, PloS one 12 (2017) e0180944.

[4] I. Bose, R. Pal, Do green supply chain management initiatives impact stock prices of firms? Decis. Support. Syst. 52 (3) (2012) 624–634.

[5] C.G. Broyden, J. Dennis Jr, J.J. Moré, On the local and superlinear convergence of quasi-Newton methods, IMA IMA J. Appl. Math. 12 (3) (1973) 223–245.

[6] C. Calvo, C. Ivorra, V. Liern, Fuzzy portfolio selection with non-financial goals: exploring the efficient frontier, Ann, Oper, Res, 245 (1) (2016) 31–46

[7] K. Chen, Y. Zhou, F. Dai, A LSTM-based method for stock returns prediction: a case study of China stock market. Proceedings of the 2015 JEEE International Conference on Big Data, IEEE, 2015, pp. 2823–2824.

[8] T. Chen, R. Xu, Y. He, X. Wang, Improving sentiment analysis via sentence type classification using BiLSTM-CRF and CNN, Exp. Syst. with Appl. 72 (2017) 221–230.

[9] W. Chiang, D. Enke, T. Wu, R. Wang, An adaptive stock index trading decision support system, Exp, Syst, with Appl. 59 (2016) 195–207

[10] K. Cho, B. Van Merriënboer, C. Gulcehre, D. Bahdanau, F. Bougares, H. Schwenk, Y. Bengio. Learning phrase representations using RNN encoder-decoder for statistical machine translation, arXiv preprint arXiv:1406.1078. (2014).

[11] F. Chollet, et al., Keras, https://keras.io. 2015.

[12] A.P. Dempster, N.M. Laird, D.B. Rubin, Maximum likelihood from incomplete data via the EM algorithm, J. of the Royal Stat. Soc.: Ser. B (Metho.) 39 (1977) 1–22.

[13] L. Di Persio, O. Honchar. Artificial neural networks architectures for stock price prediction: comparisons and applications, Int. J. of Circuits, Syst. and Signal Process. 10 (2016) 403–413

[14] J. Dumay, J. Guthrie, F. Farneti, GRI sustainability reporting guidelines for public and third sector organizations: a critical review, Public Manag, Rey, 12 (4) (2010) 531–548.

[15] N. Eccles, S. Viviers, The origins and meanings of names describing investment practices that integrate a consideration of ESG issues in the academic literature, J. Bus, Ethics 104 (3) (2011) 389–402

[16] A. Fatemi, M. Glaum, S. Kaiser, ESG performance and firm value: the moderating role of disclosure, Glob. Financ. J. 38 (2018) 45–64 special Issue on Corporate Social Responsibility and Ethics in Financial Markets

[17] S. Feuerriegel, J. Gordon, Long-term stock index forecasting based on text mining of regulatory disclosures, Decis. Support. Syst. 112 (2018) 88–97.

[18] C. Francq, J.-M. Zakoian, GARCH Models: Structure, Statistical Inference and Financial Applications, Wiley, 2019.

[19] G. Friede, T. Busch, A. Bassen, ESG and financial performance: aggregated evidence from more than 2000 empirical studies, J. Sustain. Finance and Invest. 5 (4) (2015) 210–233.

[20] S. Gadre-Patwardhan, V.V. Katdare, M.R. Joshi, A review of artificially intelligen applications in the financial domain, Artificial Intelligence in Financial Markets, Springer, 2016, pp. 3–44.

[21] A. Garcia-Bernabeu. D. Pla. M. Bravo. B. Perez-Gladish. Mean-variance stochastic goal programming for sustainable mutual funds' portfolio selection, Rect @ 16 (2) (2015) 135.

[22] H. Gray, New Directions in the Investment and Control of Pension Funds, Investor Responsibility Research Center, 1983.

[23] G. Halbritter, G. Dorfleitner, The wages of social responsibility-where are they? A critical review of ESG investing, Rev. Financ. Econ. 26 (2015) 25–35.

[24] B.M. Henrique, V.A. Sobreiro, H. Kimura, Literature review: machine learning techniques applied to financial market prediction, Expert Syst. with Appl. 124 (2019) 226–251.

[25] C.-S. Ho, P. Damien, B. Gu, P. Konana, The time-varying nature of social media sentiments in modeling stock returns. Decis. Support. Syst. 101 (2017) 69–81.

[26] S. Hochreiter, J. Schmidhuber, Long short-term memory, Neural Comput. 9 (8) (1997) 1735–1780.

[27] Q. Jiang, C. Tang, C. Chen, X. Wang, Q. Huang, Stock price forecast based on LSTM neural network, in: Jiuping. Xu, Fang Lee. Cooke, Mitsuo. Gen, Syed Ejaz. Ahmed (Eds.), Proceedings of the Twelfth International Conference on Management Science and Engineering Management, Springer International Publishing, Cham, 2019, pp. 393–408

[28] A. Kempf, P. Osthof, The efect of socially responsible investing on portfolio per formance, Eur. Financ. Manag. 13 (5) (2007) 908–922.

[29] D. Kraft, A software package for sequential quadratic programming, Forschungsbericht-Deutsche Forschungs- und Versuchsanstalt fur Luft- und Raumfahrt 1988.

[30] M. Kraus, S. Feuerriegel, Decision support from financial disclosures with deep neural networks and transfer learning, Decis, Support, Syst, 104 (2017) 38–48.

[32] H. Markowitz, Portfolio selection, J. Financ. 7 (1) (1952) 77–91.

[31] W. Kristjanpoller, M.C. Minutolo, Forecasting volatility of oil price using an artificial neural network-GARCH model, Exprt. Syst. with Appl. 65 (2016) 233–241.

[33] A.H. Moghaddam, M.H. Moghaddam, M. Esfandyari, Stock market index prediction using artificial neural network, J. Econ. Finance Adm. Sci. 2077-1886, 21 (41) (2016) 89–93.

[34] F. Munoz, M. Vargas, I. Marco, Environmental mutual funds: financial performance and managerial abilities, J. Bus, Ethics 124 (4) (2014) 551–569

[35] K. Nam, N. Seong, Financial news-based stock movement prediction using causality analysis of influence in the Korean stock market, Decis. Support. Syst. 117 (2019) 100-112

[36] D.M. Nelson, A.C. Pereira, R.A. De Oliveira, Stock market's price movement prediction with LSTM neural networks. Proceedings of the 2017 International Joint Conference on Neural Networks (IJCNN) JEEE. 2017. pp. 1419–1426.

[37] J. Nilsson. Investment with a conscience: examining the impact of pro-social attitudes and perceived financial performance on socially responsible investment be: havior, J. Bus. Ethics 83 (2) (2008) 307–325.

[38] B.T. Peylo, A synthesis of modern portfolio theory and sustainable investment, J. Invest, 21 (4) (2012) 33–46.

[39] M.J. Powell. An efficient method for finding the minimum of a function of severa variables without calculating derivatives, Comput. J. 7 (2) (1964) 155–162.

[40] A. Samarawickrama, T. Fernando, A recurrent neural network approach in predicting daily stock prices an application to the Sri Lankan stock market. Proceedings of the 2017 IEEE International Conference on Industrial and Information Systems (ICIIS), JEEE, 2017, pp. 1–6.

[41] H. Schäfer, Corporate Social Responsibility Rating, A Handbook of Corporate Governance and Social Responsibility, (2016), p. 449.

[42] M. Schuster, K.K. Paliwal, Bidirectional recurrent neural networks, IEEE Trans. Signal Process. 45 (11) (1997) 2673–2681.

[43] S. Selvin, R. Vinayakumar, E. Gopalakrishnan, V.K. Menon, K. Soman, Stock price prediction using LSTM, RNN and CNN-sliding window model, Proceedings of the 2017 International Conference on Advances in Computing, Communications and Informatics, IEEE, 2017, pp. 1643–1647.

[44] G. Sermpinis, A. Karathanasopoulos, R. Rosillo, D. de la Fuente, Neural networks in financial trading, Ann. Oper. Res. (2019) 11–16 Special Issue: Networks and Risk Management

[45], W.E. Sharpe, Mutual fund performance, J. Bus. 39 (1) (1966) 119–138.

[46] A.I. Siddiqui, D. Marinova, A. Hossain, V. Todorov, Socially responsible investment

in Australia, Sustainability And Development In Asia And The Pacific: Emerging Policy Issues, (2011), p. 249.

[47] M. Statman, The diversification puzzle, Financ. Anal. J. 60 (4) (2004) 44–53.

[48] C. Stay, Corporate Social Responsibility, Sustainalytics 2010.

[49] S. Stephen, Financial performance of environmentally responsible investment funds: a systematic review, Academy of Management Proceedings, 2018 2018, p 12451. Academy of Management Briarclif Manor, NY 10510.

[50] Thomson Reuters, Thomson Reuters ESG Scores, Technical Report Thomson Reuters 2019.

[51] US SIF Foundation, 2018 Biennial Report On US Sustainable, Responsible And Impact Investing Trends, US SIF Foundation 2018.

[52] E. Van Duuren, A. Plantinga, B. Scholtens, ESG integration and the investment management process: fundamental investing reinvented, J. Bus. Ethics 138 (3) (2016) 525–533.

[53] T. Verheyden, R.G. Eccles, A. Feiner, ESG for all? The impact of ESG screening on return, risk, and diversification, J. Appl. Corp. Financ. 28 (2) (2016) 47–55.

[54] M. Von Wallis, C. Klein, Ethical requirement and financial interest: a literature review on socially responsible investing, J. Bus. Res 8 (1) (2015) 61–98.

[55] C. Zopounidis, E. Galariotis, M. Doumpos, S. Sarri, K. Andriosopoulos, Multiple criteria decision aiding for finance: an updated bibliographic survey, Eur. J. Oper. Res, 247 (2) (2015) 339–348

Nhi Vo is a Ph.D. Candidate at Advanced Analytics Institute, Faculty of Engineering and Information Technology, University of Technology Sydney, Australia. She received her M.Sc. in Quantitative Finance from Christian-Albrechts-Universität zu Kiel, and her main research interests include financial data analytics, financial services, consumer personality, and socially responsible investment. She has published works at some of the top peer-reviewed conferences in data mining field, such as BESC 2017, PAKDD 2018 and DASFAA 2018.

Tony He has been a Professor in Finance at University of Technology Sydney (UTS) since 2010. He has been a co-editor of Journal of Economic Dynamics and Control (an ABDC A\* journal) since 2013. Prof. Tony He received his Ph.D. in Finance in 2001 from UTS and Ph.D. in Applied Mathematics in 1995 from Flinders University, the two fundamental disciplines that underpin his areas of teaching and research. Tony is an internationally recognized expert in financial market modelling and nonlinear dynamics in finance and economics. His research interests cover a broad area of theoretical asset pricing and financial market modelling with heterogeneous beliefs, adaptive learning, and social interaction, and empirical testing on various financial market anomalies and stylized facts such as volatility clustering, profitability of optimal trading, and return predictability. His international research profile is attested by his more than 40 publications in the field of finance and economics, invited contributions to the prestigious Handbook of Financial Markets and Handbook of Computational Economics, numerous keynote talks in the international conferences, and a number of competitively national and international research grants. As a mathematician in his earlier career, Tony has established an international reputation in the field of the theory and application of nonlinear dynamical systems and published more than 40 papers in this area. He has organized and served as committee member of international workshops and conferences. He has also served as associate editor and reviewer of a number of journals in finance. economics and mathematics.

Shaowu Liu received his doctorate from Deakin University in the field of machine learning. He is currently a postdoctoral research fellow at the University of Technology Sydney. Since 2012. he has published 25 + papers in the arena of data mining and machine learning, including Machine Learning Journal (MLJ), Future Generation Computer Systems (FGCS), IEEE Transactions on SMC(C), Enterprise Information Systems (EIS), and AAAI conference. For the community, he has served as co-chair of ES 2016, IIP 2016, KSEM 2017, and KSEM 2019.

Guandong Xu is a Full Professor in Data Analytics at School of Software and Advanced Analytics Institute, the University of Technology Sydney with a Ph.D. degree in Computer Science. His research interests cover Data Science, Data Analytics, Recommender Systems, Web Mining, User Modelling, NLP, Social Network Analysis, and Social Media Mining. He has published three monographs in Springer and CRC press, and 190+ journal and conference papers including ACM Transactions on Information Systems, ACM Transaction on Intelligent Systems and Technology. JEEE Transactions on Neural Networks and Learning Systems, IEEE Transactions on Services Computing, IEEE Transactions on Information Forensics and Security, IEEE Intelligent Systems, Information Sciences, IJCAI. AAAI. WWW. ICDM. ICDE, and CIKM conferences. He is the assistant Editor-in-Chief of World Wide Web Journal and has been serving in editorial board or as guest editors for several international journals, such as Social Network Analysis and Mining, the Computer Journal, Journal of Systems and Software, World Wide Web Journal. Multimedia Tools and Applications. and Online Information Review He has received a number of Industry Awards from the Australian industry community, such as the 2018 Top-10 Australian Analytics Leader Award
