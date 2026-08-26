---
otero_id: 21423
otero_key: "4JWC4CA3"
title: "Integrating arbitrage pricing theory and artificial neural networks to support portfolio management"
authors: "Shin-Yuan Hung; Ting-Peng Liang; Victor Wei-Chi Liu"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)80006-6"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Integrating arbitrage pricing theory and artificial neural networks to support portfolio management

Shin-Yuan Hung, Ting-Peng Liang \*, Victor Wei-Chi Liu

Department of Information Management, National Sun Yat-sen University, Kaohsiung, Taiwan 80424, Taiwan ROC

Received 2 November 1994; revised 10 July 1995; accepted 12 November 1995

## Abstract

The paper presents an innovative approach that integrates the arbitrage pricing theory (APT) and artificial neural networks (ANN) to support portfolio management. The integrated approach takes advantage of the synergy between APT and ANN in extracting risk factors, predicting the trend of individual risk factor, generating candidate portfolios, and choosing the optimal portfolio. It uses quadratic programming for identifying surrogate portfolios in APT and ANN to predict factor returns. Empirical results indicate that the integrated method beats the benchmark and outperforms the traditional method that uses the ARIMA model.

Keywords: Arbitrage pricing theory; Artificial neural networks; Portfolio management; Decision support systems; System integration; Unified programming

## 1. Introduction

Portfolio management is a major issue in investment. Its goal is to choose a set of risk assets to form a portfolio that can maximize the return under a given risk or minimize the risk for obtaining a given return. Due to the complexity in portfolio management, institutional investors often need decision support systems (DSS) to facilitate their decision making. A critical factor for developing a successful DSS for portfolio management is its stock selection model.

A good model allows good stocks to be selected to reach a higher performance.

The most popular model in portfolio management in recent years is the arbitrage pricing theory (APT) developed by Stephen Ross in 1976 [28–31]. Theoretically, the APT model can price risk assets of a portfolio efficiently from a few risk factors. It identifies three to five risk factors [2,27] from a number of possible candidates, and then selects securities based on their relative risks and returns compared to the market. In practice, however, heuristics are usually required to overcome bottlenecks in determining a proper set of stocks when APT is used alone. For instance, in the Roll and Ross investment review process (as shown in Fig. 1) [28], investors have to know the probability of success in meeting the specified target before they set up the desired performance level relative to the benchmark (i.e., the market index that they want to “beat”). Furthermore, once the target level of performance is set, they need heuristics to determine the levels of risk exposure with each factor and the weight of each risk asset in the portfolio to reach the goal. In general, these heuristics are hard to acquire and are considered highly sensitive in most investment firms.

Recently, much research has focused on using artificial intelligence (AI) techniques to predict stock prices. One technique of particular interests is the artificial neural networks (ANN) [11,12,14,16,23,34,36,40,41]. Cybento has proven that if correct interconnection weights can be found, an ANN with a sufficient number of neurons in the hidden layer can be used to approximate any multidimensional function to any specified degree of accuracy [7]. However, practical limitations exist when we use the ANN alone to support portfolio management. A major one is that it requires heavy computational efforts because the number of securities to be analyzed is usually very large. For instance, if we want to formulate an ANN model to analyze 100 stocks with each having data for 100 periods, we may need 10,000 neurons at certain ANN layers, which is computationally prohibitive.

Given the facts that using ANN models alone to analyze portfolio performance would be too complicated and the APT model can reduce the number of the risk factors, it seems to be beneficial to integrate these two approaches. The solution of the integrated approach requires to adopt both artificial intelligent and optimization paradigms in a unified manner [18]. Toward this end, this paper studies two issues: (1) how ANN can be integrated with APT to support portfolio analysis, and (2) how well the integrated method performs.

![](/api/attachments/4JWC4CA3/fulltext/images/810a6ab6d9f46698d4f380c2e6a47bb06ed096ba5d027c393cf330bda6c4bc0f.jpg)  
Fig. 1. The Roll and Ross investment review process.

In this research, a novel approach for integrating APT and ANN is developed. The approach suggests using quadratic programming to obtain the maximum explained variance of risk factors to risk assets returns for asset pricing in APT. Once risk assets have been priced, ANN can be applied to predict the effects of risk factors on assets prices. Investment alternatives can then be generated, and the optimal (most efficient) investment portfolio can be determined based on the prediction and the investor's preference. Through the unification of AI and optimization methods, the complex portfolio management can be solved.

To evaluate the integrated approach, empirical studies are conducted. We examine the number of risk factors determining assets pricing in the Taiwan stock market, and compare with the benchmark the performances of (1) integrating APT with the ANN model (IANN model) and (2) integrating APT with the ARIMA model (IARIMA model). The Taiwan Stock Exchange Weighted Price Index (TSEWPI) of the Taiwan stock market was chosen as the benchmark.

This research is an application and implementation of unifying mathematical programming and AI techniques. Its contribution is threefold. First, the integration of APT and ANN successfully eliminates the limitations of using APT or ANN models alone in portfolio management. Second, the integrated approach shows capabilities to effectively automate the portfolio management process. Finally, our findings also show a successful integration of optimization and AI techniques. This can provide insights into further integration of mathematical optimization models and AI techniques.

The remainder of the paper is organized as follows. First, the concepts of APT and ANN are discussed. This is followed by a description of our integrated approach that combines APT with the ANN model. Finally, empirical studies evaluating the performance of the integrated method and their findings are discussed.

## 2. Research background

## 2.1. Arbitrage pricing theory

It is a common believe that if you want to obtain a higher return in the financial market, you must bear higher risks. This simple concept raises at least two questions: (1) what do we mean by “risk”, and (2) how can it be measured? The capital asset pricing model (CAPM) [33] was an early approach to include risks in portfolio analysis. According to CAPM, the risks of a security are measured by its beta coefficient. The beta coefficient of a security is defined as the sensitivity of the security’s return compared to the return of the “market”. In theory, the market is the portfolio composed of all securities and assets available for investment. For example, when a security whose return variation is larger than that of the market, then its beta is greater than one. Its beta would be less than one, otherwise.

Since the CAPM uses a single factor to capture security risks, it is considered inadequate in many situations. To offset this problem, the APT model that refines CAPM to include multiple risk factors was developed later. The major assumption of the APT model is that the investment risks can be broken down into systematic and idiosyncratic risks $[28]$ . Systematic risks are market-oriented and pervasively influence virtually all security prices (e.g., interest rates or the business cycle). They are introduced by the limited number of risk factors we consider for constructing the portfolio. Idiosyncratic risks involve unexpected events peculiar to a single security or a limited number of securities (e.g., the loss of a key contract or a change in government policy toward a specific industry). They can be eliminated in large well diversified portfolios.

Basically, APT is a multiple-index model that uses a few influential risk (common) factors to determine asset prices. Ross was the first to show that a multiple index model would always lead to a unique relative pricing model [31]. The return calculation equation for each security is shown in Eq. (1). In equilibrium conditions, the relative price of each security can be described by the Eq. (2) [10].

$$
R _ {i} = \alpha_ {i} + \sum_ {L = 1} ^ {k} \beta_ {i L} R _ {L} + e _ {i},\tag{1}
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
where:
$R_{i}$ = the return on risk asset $i$;
$α_{i}$ = the unique expected return associated with risk asset $i$;
$β_{iL}$ = the sensitivity of risk asset $i$ to index $L$, for $L=1\ldots k$;
$R_{L}$ = the return on index $L$;
$e_{i}$ = a random variable with a mean of zero and a variance of $\sigma_{e_{i}}^{2}$.

$\overline{R}_{i}=R_{F}+\sum_{L=1}^{k}b_{iL}\lambda_{L},\quad(2)$

where:
$\overline{R}_{i}$ = the average return on risk asset $i$;
$R_{F}$ = the risk-free return;
$b_{iL}$ = the estimated sensitivity of risk asset $i$ to index $L$;
$\lambda_{L}$ = the price of risk $L$.
</div>

A number of empirical studies have examined the validity of the APT model $[2-6,8,9,20,24,27,39]$ . For instance, Roll and Ross $[27]$ gathered the daily returns on 1,260 stocks listed on the New York and American Stock Exchanges between July 3, 1962 and December 31, 1972 (a total of 2,619 trading days). These data were then grouped into 42 groups, with each having 30 stocks. They used these data to evaluate APT and concluded that there were three to five risk factors that determined asset pricing. In Taiwan, Wu and Lin $[39]$ studied the explanation power of asset pricing models using the trading data at the Taiwan Stock Exchange. The results indicated that APT was indeed more powerful than the traditional CAPM model.

## 2.2. Applying APT to support portfolio management

Besides empirical studies verifying the validity of asset pricing models, there are studies that focus on the application of these models to portfolio management in practice [28,22]. For example, Roll and Ross [28] proposed an approach to use APT in investment decisions. As shown in Fig. 1, this approach includes six major steps. First, the historical data base of individual securities in various markets is updated using proprietary computer programs. Second, master portfolios that surrogate the underlying macro-economic risk factors are created. Third, the risk of each stock on a certain factor is measured using regression analysis. Fourth, the expected return or risk premium for each of the master portfolios is determined. The result can be used to construct portfolios. Fifth, the target exposures that tailor the client's portfolio based on the client's target performance are calculated. Finally, individual securities are selected to have low volatility and high return. The above six steps are repeated monthly to maintain a portfolio that tracks the movement of the benchmark with consistently higher additional incremental returns.

Empirical results [28] indicated that the return of the portfolio generated using APT exceeded the S&P 500 benchmark by an average of over 200 basis points per annum for the U.S.A. stocks, exceeded the performance of the Tokyo Stock Exchange Price Index by an average of 400 basis points per annum for the Japanese securities, and exceeded the EAFE by an average of over 500 basis points per annum for non-U.S.A. international stocks.

Lin et al. [22] also presented a method that tended to construct a portfolio whose performance is better than that of the industry indices by using the return generating process of the APT. The empirical results indicated that the portfolio constructed by the method outperformed the industry indices. Overall, most previous research provides strong evidence to support the usefulness of the APT model in portfolio construction.

## 2.3. Artificial neural networks

Artificial neural networks (ANN) are a special kind of modeling technique evolved from biological sciences. The basic component of an ANN model is artificial neurons. Each neuron is composed of inputs, processes, and outputs. A neural network is a connection of artificial neurons to simulate a biological neural network. Neurons can be connected and perform in many different ways. Rumelhart [32] specified eight major aspects to differentiate the structure and operation of the ANN: (1) set of processing units, (2) state of activation, (3) output function for each unit, (4) pattern of connectivity, (5) propagation rule for passing patterns of activities, (6)

activation rule for combining inputs affecting a unit with its present state to produce an output, (7) learning rule whereby interconnections can be modified on the basis of experience, and (8) environment within which the learning system must operate.

Since neurons can be connected differently, there are many types of ANN models (called “paradigms”). In general, we categorize these models according to their learning behavior. For example, we may categorize them into supervised or unsupervised learning based on the availability of the outcome class. Supervised learning learns from input data whose classes are known, whereas unsupervised learning groups data without known classes into clusters based on their similarity. In ANN, Perceptron and back-propagation network (BPN) are supervised learning models, whereas adaptive resonance theory (ART) and bi-directional associative memory (BAM) are unsupervised learning models. Among different models, BPN is the most popular and has the highest success rate.

A BPN model is composed of several layers (generally, more than two layers) of neurons. Each layer contains a predetermined number of neurons. Every neuron in a layer connects to all neurons in the adjacent layers. For example, a 4–5–4 BPN contains four neurons in the input layer, five neurons in the hidden layer, and four neurons in the output layer. Its architecture is shown in Fig. 2. The neurons at the input layer receive messages from the external environment, and those at the output layer send messages to the environment. One or more hidden layers are set between the input and output layers. The existence of the hidden layer enables the ANN to model complex causal structures through interactions among the neurons.

![](/api/attachments/4JWC4CA3/fulltext/images/05bd9e2286ef20348f94aff4d11df3174f981090e40ba015bda1ecebdb23c613.jpg)  
Fig. 2. A 4–5–4 back-propagation neural network structure.

A major step in building ANN models is to learn the connection weights through training. The process of training a BPN includes the following steps: (1) set the connection weights of a BPN model randomly, (2) select a training case from the training set and send its input vector to the input layer of the BPN, (3) calculate the output of the BPN, (4) calculate the error between the output of the model and the actual value, (5) adjust the connection weights based on the learning rule to remove the error, (6) repeat steps 2 to 6 until the sum of errors is below the specified tolerance level. A detailed description of the BPN algorithm can be found in [15].

ANN have advantages over traditional classification methods such as discriminant analysis. For instance, ANN can provide a proper solution for complex classification or prediction problems by the internal associative and adaptive abilities of the network. Moreover, ANN is fault-tolerant. ANN have disadvantages too. First, its learning process is very time-consuming. It could easily take hours of computation on a computer before a stable model can be built. Second, it is hard to explain how it solves the problem. The causal relationships are hidden in the network connections. Finally, the determination of an optimum network structure has remained as an art that must rely on trial and error. This adds more uncertainty into the model building process. Overall, it is a useful technique worth serious studies.

## 2.4. Applying ANN to support investment decisions

ANN has been used widely in financial analysis $[25,26,35]$ and investment prediction $[11,12,14,16,23,34,36,40,41]$ . For example, Tanigawa and Kamijo $[36]$ proposed a stock price pattern matching system using a Dynamic Programming

Neural Network (DNN). DNN is based on the integration of the neural network and Dynamic Programming matching method (DP-matching). The stock price patterns classified by DNN were evaluated by three chartists (human experts). It became clear that high correlation was found between the classification by DNN and the evaluation by chartists. The proposed DNN system was able to match patterns judged by the chartists as similar.

Kimoto et al. [16] proposed an ANN to determine the timing to buy or sell the TOPIX index. They trained and tested the ANN using the weekly data from January 1987 to September 1989. The result indicated that the ANN model performed better than the benchmark. If we set the TOPIX index of January 1987 as 1.00, the straight-forward buy-and-hold strategy would result in a performance of 1.67 by September 1989, whereas the performance of the ANN model would be 1.98.

Jang et al. [12] proposed a structure-level adaptive back-propagation learning algorithm that could automatically synthesize the structure of a neural network to fit the desired problem. The results indicated that, for the testing period between 1990 and 1991, the annual rates of return from trading decisions suggested by the proposed system were higher than those of the buy-and-hold strategy.

Although ANN have been used to predict stock prices, limitations exist when they are used for portfolio analysis. The major one is that the complexity of the network model increases dramatically as the number of stocks to be analyzed increases. This may make the model building extremely expensive and sometimes impossible.

## 3. Integrating arbitrage pricing theory with artificial neural networks

Given that both APT and ANN have their strengths and weaknesses, it is natural to seek an integration. Integration of mathematical optimization and artificial intelligence methods has been applied in several occasions [17-19,21]. For example, Liang et al. [21] developed an approach that integrates semi-Markov decision models and ANN for production scheduling. Empirical evidence indicated that the integrated method outperformed the individual method.

Lee and Song [17] proposed a method that integrates linear programming (LP) models and rule-based systems for the crude oil purchase scheduling. The LP model covers the monthly crude oil purchase plan, while the rule-based system covers the daily crude oil delivery schedule. The Post-Model Analysis (PMA) approach is necessary because the monthly optimal purchase plan must be adjusted during implementation to accommodate the dynamic situation of suppliers and tankers.

Lee et al. [19] proposed a K-FOLIO system, which integrates the Markowitz risk-return optimization model with the expert knowledge of specialists and managers, to support investment management. Empirical results indicated that the cumulated K-FOLIO returns from January to December 1987 were greater than the average market yield and the returns of the unenhanced Markowitz model in Korean Stock Exchange.

An integration of APT and ANN has certain advantages. The APT method has strong theoretical background but needs heuristics in practical applications. The ANN method is capable of providing reliable heuristic models when prediction of certain factors is necessary in constructing portfolios.

The integrated approach in our research includes three major components: APT, ANN, and a portfolio constructor. We need to use the APT model to price the risk assets available for building a portfolio. Once the prices are determined, we need to use the ANN model to predict the trend of each risk factor in the future. Finally, we use the portfolio constructor to generate investment alternatives and select the optimal (most efficient) portfolio from the candidates based on the investor's preference. Fig. 3 shows the process of the integrated approach. Individual modules are described in detail in the following.

## 3.1. Using APT to price risk assets

The first module of the integrated approach is to determine the prices of risk assets. Its primary purpose is to determine the factors having effects on the fluctuation of security returns and their effects on the return of individual securities. Using APT could identify these factors and price all the risk assets available for building a portfolio. It includes four major steps (Steps 1 to 4 in Fig. 3).

![](/api/attachments/4JWC4CA3/fulltext/images/1bffc871828de5633ea417883ad931fb410a62031706bb1ba4411a622cbd2b59.jpg)  
Fig. 3. The process of the integrated approach.

Step 1. Factor analysis.

The first step is to decide what kinds of risk assets are available for consideration in building a portfolio and what will be the benchmark. After the selection is done, factor analysis is used to determine factors effecting the fluctuation of security returns. The factor analysis includes two sub-steps: (1) The principle factor analysis is applied to determine the proper number of risk factors having effects on the fluctuation of security returns. A factor is selected if its eigenvalue is greater than one [13]. (2) After the number of risk factors is determined, the maximum-likelihood factor analysis is applied to extract the factor structures (including the factor loading matrices and a residual matrix). Statistical packages such as: SAS, SPSS, etc. are useful in this step.

## Step 2. Surrogate portfolios of risk factors.

After the factor analysis, we use the result to define the basis portfolios (also known as “master portfolios”) and the orthogonal portfolio. A basis portfolio is a collection of securities that can be used as a surrogate measure of a risk factor. An orthogonal portfolio is created to measure the risk-free return. In order to minimize the effect of idiosyncratic risk and maximize the effect of systematic risk, we adopt the minimum idiosyncratic risk procedure invented by Lehman and Modest [20]. Quadratic programming is used to determine the weights of each basis portfolio and the orthogonal portfolio from the factor structures. The weights determined by quadratic programming maximize the explained variance of risk factors to risk assets returns. Tools such as: GINO and LINDO are used at this step. The result of this step often extracts three to five basis portfolios from numerous securities. In our research, three basis portfolios in the former nine periods and four basis portfolios in the latter three periods are identified from 51 stocks.

## Step 3. Calculation of risk premiums.

In this step, we calculate all the extra returns (also known as “the risk premiums”) of various factors. After the orthogonal portfolio and the basis portfolios have been created, the extra return of each basis portfolio ( $\lambda_{L}$ in Eq. (2)) can be calculated. Similarly, the extra returns of the specified benchmark and each of the risk assets $(\overline{R}_{i}-\overline{R}_{F}$ in Eq. (2)) can be calculated.

## Step 4. Asset pricing.

Finally, we need to determine the sensitivity of individual asset's risk premium to the changes in certain risk factors. Since there are multiple risk factors surrogated by basis portfolios, each asset has an array of beta coefficients. The process of finding the beta coefficients of an asset is called asset pricing, which can be done by using multiple regression analysis. For the specified benchmark and each risk asset, the beta coefficients are determined from the regression against the risk premiums of each risk factors.

## 3.2. Using ANN to predict the future trend of each risk factor

Once all risk assets available for portfolio construction have been priced, we use ANN to predict the future trend of each risk factor for building the portfolio. This module includes three major steps (Steps 5, 6, and 7 in Fig. 3).

## Step 5. ANN model definition.

In order to use ANN to predict the future trend of a risk factor (basis portfolio) or the risk-free return (orthogonal portfolio), we have to define proper model structures. If four risk factors are identified for those stocks, then we need to define five ANN models, one for each risk factors and one for the risk-free return. For each model, an analysis period is an input node and a predictive period is an output node. The hidden nodes are determined by heuristics. For example, if we use four weekly returns to predict the following four weekly returns, then the ANN model will have four input and output nodes, respectively. The number of output nodes is determined by the number of predicted weekly risk premiums for the risk factor we need. The optimal numbers of input and hidden nodes are obtained by trial-and-error.

## Step 6. Learning.

After the structure of the BPNs has been determined and data are available, we begin to train the neural networks. First, the training data sets are used to train the BPNs. This step is very time-consuming. Then, the resulting models are evaluated using the testing data sets. If the test results are not good enough, they have to be retrained. NeuroShell [38] was the software we used in this research.

## Step 7. Return prediction.

After all the ANN models have been trained, we use the predictive data sets to forecast the risk-free return and the returns of each risk factor in the succeeding weeks. For each risk asset and the benchmark, its beta coefficients (obtained in Step 4), the predicted risk-free return and the predicted returns of each risk factor are then combined to calculate the predictive returns of the asset. For example, a risk asset has been found to be effected by three risk factors, and its beta coefficients to those factors are 0.1, 0.2, and 0.3 respectively. The predicted risk-free return (for the first week) is 0.5. The predictive returns of each risk factor (for the first week) are 0.6, 0.7, and 0.8, respectively. Given these, the predicted return of the risk asset (for the first week) can be calculated as $0.5 + 0.1^{*}(0.6 - 0.5) + 0.2^{*}(0.7 - 0.5) + 0.3^{*}(0.8 - 0.5) = 0.64$ .

## 3.3. Using portfolio constructor and selection mechanism to generate the suggested portfolio

Once the model for predicting future returns of the risk assets has been constructed, we can build portfolios based on the predicted returns and risks of the risk assets. In our research, we use a simulation-based approach that first generates a number of candidate portfolios and then chooses the optimal among the candidates. It includes three major steps (Steps 8, 9, and 10 in Fig. 3).

## Step 8. Generation of candidate portfolios.

Given the predictive return and risk of each risk asset, we can construct portfolios by combining different assets. In this step, we use simulation to generate a number of candidate portfolios and calculate their returns and risks. The process of generating a candidate portfolio includes two sub-steps: (1) a set of asset weights $(w_{i1}, w_{i2}, \ldots, w_{in})$ are generated randomly to simulate a possible portfolio. An asset weight is the proportion of the risk asset in a portfolio. The sum of the asset weights must be equal to one; (2) the predictive return and risk of the portfolio $(\overline{Ri},\sigma_{i})$ are estimated using the predicted return of the risk assets. Each portfolio generated in this step is a candidate $(w_{i1},w_{i2},\ldots,w_{in};\overline{Ri},\sigma_{i})$ for selection later.

## Step 9. Setting goals.

Once enough candidate portfolios are generated, we can choose the optimal among them to meet our investment goals. In general, our investment goals include predetermined return and risk levels that are considered satisfactory. Although the goals may be set up arbitrarily, a better way is to use the expected performance of the benchmark.

In this step, we first estimate the future return and risk (variance) of the benchmark. Then, the investor uses the estimated performance of the benchmark to determine the proper levels of return and risk. For example, a user may set up goals such as a return being 0.2 above the benchmark return and the volatility being 0.2 less than the standard deviation of the weekly return.

## Step 10. Portfolio selection.

In the last step, the optimal portfolio is chosen among the candidates based on the investor's goals. The selection mechanism uses the return and risk of a candidate portfolio to compute its performance score. The formula for calculating the scores for candidates is listed in Appendix A. The optimal portfolio is chosen according to the performance score of the candidate portfolio.

## 4. Empirical evaluation

Although the integrated method seems to be promising, empirical studies are necessary to evaluate its value. In this section, we present the empirical findings from applying the integrated method to the stocks traded in the Taiwan Stock Exchange. Two major issues were examined in the study. First, whether the portfolios constructed by the integrated method perform better than the benchmark. The benchmark chosen was the TSEWPI, the weighted stock price index published by the Taiwan Stock

Table 1  
Hypotheses for the empirical study

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$H_{0}^{1}:\mu(\mathrm{Rp}_{IANN}-\mathrm{Rp}_{TSEWP_{I}})=0$ $H_{0}^{2}:\mu(\mathrm{Rp}_{IARIMA}-\mathrm{Rp}_{TSEWP_{I}})=0$ $H_{0}^{3}:\mu(\mathrm{Rp}_{IANN}-\mathrm{Rp}_{IARIMA})=0$ $H_{0}^{4}:\mu[\mathrm{E}(\mathrm{Rp}_{IANN})-\mathrm{E}(\mathrm{Rp}_{TSEWP_{I}})]=0$ $H_{0}^{5}:\mu[\mathrm{E}(\mathrm{Rp}_{IARIMA})-\mathrm{E}(\mathrm{Rp}_{TSEWP_{I}})]=0$ $H_{0}^{6}:\mu[\mathrm{E}(\mathrm{Rp}_{IANN})-\mathrm{E}(\mathrm{Rp}_{IARIMA})]=0$ $H_{0}^{7}:\mu[\mathrm{SD}(\mathrm{Rp}_{IANN})-\mathrm{SD}(\mathrm{Rp}_{TSEWP_{I}})]=0$ $H_{0}^{8}:\mu[\mathrm{SD}(\mathrm{Rp}_{IARIMA})-\mathrm{SD}(\mathrm{Rp}_{TSEWP_{I}})]=0$ $H_{0}^{9}:\mu[\mathrm{SD}(\mathrm{Rp}_{IANN})-\mathrm{SD}(\mathrm{Rp}_{IARIMA})]=0$
</div>

Notations: Rp: means the return of the portfolio; E(Rp): means the expected value of Rp; SD(Rp): means the standard deviation of Rp.

Exchange. The integrated method must beat the benchmark to be useful.

The second issue studied was whether the ANN module plays a major role in the integrated method. We chose another method that integrates the traditional ARIMA model $[1,37]$ for time series analysis with APT as a basis for comparison. In other words, the ANN model in Step 6 of the integrated method presented in the previous section was replaced by the ARIMA model. The rest procedures were the same. The original method that integrates APT and ANN is called the IANN approach, whereas the one that integrates APT and ARIMA is called the IARIMA approach. If ANN plays a significant role, we would expect that the former performs better than the latter.

The performance of a portfolio is often measured by its average return and the variance of its return. Most investors desire a higher average return and lower variance. In the study, we chose three key performance indices: weekly return, monthly return, and the standard deviation of the weekly return. Nine null hypotheses for testing, as listed in Table 1, are formed. In the Table, Rp stands for the weekly return of a portfolio. E(Rp) stands for the average of the weekly return by four weeks of a portfolio. SD(Rp) stands for the standard deviation of the weekly return in a month. The italic subscripts stand for the portfolio construction method. Therefore, Rp $_{IANN}$ stands for the weekly return of the portfolio constructed by the IANN method.

Table 2  
The training and evaluation periods

<table><tr><td>Window</td><td>Training period</td><td>Evaluation period</td></tr><tr><td>1</td><td>11/25/90-11/21/92</td><td>11/28/92-12/19/92</td></tr><tr><td>2</td><td>12/23/90-12/19/92</td><td>12/26/92-01/16/93</td></tr><tr><td>3</td><td>01/20/91-01/16/93</td><td>01/23/93-02/13/93</td></tr><tr><td>4</td><td>02/17/91-02/13/93</td><td>02/20/93-03/13/93</td></tr><tr><td>5</td><td>03/17/91-03/13/93</td><td>03/20/93-04/10/93</td></tr><tr><td>6</td><td>04/14/91-04/10/93</td><td>04/17/93-05/08/93</td></tr><tr><td>7</td><td>05/12/91-05/08/93</td><td>05/15/93-06/05/93</td></tr><tr><td>8</td><td>06/09/91-06/05/93</td><td>06/12/93-07/03/93</td></tr><tr><td>9</td><td>07/07/91-07/03/93</td><td>07/10/93-07/31/93</td></tr><tr><td>10</td><td>08/04/91-07/31/93</td><td>08/07/93-08/28/93</td></tr><tr><td>11</td><td>09/01/91-08/28/93</td><td>09/04/93-09/25/93</td></tr><tr><td>12</td><td>09/29/91-09/25/93</td><td>10/02/93-10/23/93</td></tr></table>

## 4.1. Data selection

The data used for the empirical study were the return of the stocks listed on the Taiwanese Stock Exchange. Fifty-one stocks were selected among the more than 300 traded stocks. The name of the companies are listed in Appendix B. The criteria for selection include the following:

1. The stock must be actively traded.

2. The company had never had any major business crisis.

3. The stock must have been traded for more than three years by the beginning of the sample period.

4. The sample must cover every industry listed on the exchange.

The time period chosen for research was from November 25, 1990 to October 23, 1993. The daily return of each stock during the period was obtained from the econometrics programming system (EPS) database maintained by the Ministry of Education.

Table 3  
The results of the factor analysis

<table><tr><td>Window</td><td>Identified number of factors</td><td>% of explained variance</td></tr><tr><td>1</td><td>3</td><td>73.94%</td></tr><tr><td>2</td><td>3</td><td>72.95%</td></tr><tr><td>3</td><td>3</td><td>71.32%</td></tr><tr><td>4</td><td>3</td><td>70.95%</td></tr><tr><td>5</td><td>3</td><td>69.62%</td></tr><tr><td>6</td><td>3</td><td>69.05%</td></tr><tr><td>7</td><td>3</td><td>69.35%</td></tr><tr><td>8</td><td>3</td><td>69.27%</td></tr><tr><td>9</td><td>3</td><td>69.17%</td></tr><tr><td>10</td><td>4</td><td>70.50%</td></tr><tr><td>11</td><td>4</td><td>68.65%</td></tr><tr><td>12</td><td>4</td><td>68.57%</td></tr></table>

Note: A factor was selected if its eigenvalue was greater than one.

## 4.2. Portfolio construction and evaluation

After data selection, the whole time period was divided into 12 sets of training and evaluation periods, as shown in Table 2. Each set was an experimental window that included 103 weeks of data for training and four weeks of data for evaluation. Portfolios were constructed using the training data. Their performance were then evaluated using the evaluation data in the following four weeks. In other words, the investment strategy was to use two years' data to build a portfolio and hold the portfolio for the following four weeks before making changes. The return of the portfolio at each of the four evaluation weeks was calculated.

![](/api/attachments/4JWC4CA3/fulltext/images/407d375d2aaee6d7feb0c91eea8810355b5e7cff9fd6a0a41d1ae216186945d0.jpg)  
Fig. 4. The process of the empirical study.

Table 4  
Performances of IANN, IARIMA, and TSEWPI

<table><tr><td>Window</td><td>Rp IANN</td><td>Rp IARIMA</td><td>Rp TSEWPI</td><td>E(Rp) IANN</td><td>E(Rp) IARIMA</td><td>E(Rp) TSEWPI</td><td>SD(Rp) IANN</td><td>SD(Rp) IARIMA</td><td>SD(Rp) TSEWPI</td></tr><tr><td rowspan="4">1</td><td>1.14763</td><td>-2.53519</td><td>-0.69</td><td>0.02904</td><td>-0.12077</td><td>-0.3575</td><td>2.847399</td><td>2.109173</td><td>1.472127</td></tr><tr><td>2.83716</td><td>-0.00024</td><td>1.13</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>-0.00083</td><td>2.58677</td><td>0.39</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>-3.8678</td><td>-0.53442</td><td>-2.26</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="4">2</td><td>-3.14597</td><td>-4.44424</td><td>-5.52</td><td>-0.46953</td><td>-1.95593</td><td>-2.0275</td><td>3.14811</td><td>3.630031</td><td>3.810699</td></tr><tr><td>0.78375</td><td>-1.50322</td><td>-2.28</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>-2.91904</td><td>-4.87912</td><td>-3.64</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3.40315</td><td>3.00287</td><td>3.33</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="4">3</td><td>2.15706</td><td>2.3856</td><td>1.73</td><td>2.719778</td><td>3.024635</td><td>3.5975</td><td>3.241825</td><td>4.561217</td><td>4.214605</td></tr><tr><td>-0.85834</td><td>-0.5943</td><td>-1.35</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7.00779</td><td>9.61702</td><td>8.03</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2.5726</td><td>0.69022</td><td>5.98</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="4">4</td><td>8.32671</td><td>6.40028</td><td>4.97</td><td>3.750413</td><td>3.97834</td><td>3.5625</td><td>5.856301</td><td>5.375198</td><td>6.891876</td></tr><tr><td>5.41121</td><td>4.40336</td><td>8.11</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6.09709</td><td>8.74272</td><td>7.73</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>-4.83336</td><td>-3.633</td><td>-6.56</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="4">5</td><td>7.39059</td><td>3.27437</td><td>3.62</td><td>3.07694</td><td>1.963683</td><td>1.7025</td><td>7.512785</td><td>6.48066</td><td>5.802025</td></tr><tr><td>4.57874</td><td>2.0493</td><td>0.72</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8.27949</td><td>9.11718</td><td>8.16</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>-7.94106</td><td>-6.58612</td><td>-5.69</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="4">6</td><td>-7.83004</td><td>-4.94645</td><td>-4.42</td><td>0.55999</td><td>2.183615</td><td>-0.0575</td><td>5.882015</td><td>5.142435</td><td>3.622636</td></tr><tr><td>2.26519</td><td>4.55688</td><td>1.59</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5.92113</td><td>2.15888</td><td>-1.34</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1.88368</td><td>6.96515</td><td>3.94</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="4">7</td><td>0.90926</td><td>4.1923</td><td>-2.41</td><td>0.789898</td><td>-0.35062</td><td>-1.6575</td><td>3.079681</td><td>4.217338</td><td>3.304304</td></tr><tr><td>-3.46007</td><td>-5.66295</td><td>-5.92</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1.8945</td><td>1.48371</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3.8159</td><td>-1.41555</td><td>1.7</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="4">8</td><td>-2.39141</td><td>-2.79901</td><td>-3.37</td><td>-1.74686</td><td>-2.65451</td><td>-2.665</td><td>2.196361</td><td>1.324963</td><td>2.555132</td></tr><tr><td>-2.14899</td><td>-2.63767</td><td>-2.52</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1.3598</td><td>-0.97246</td><td>0.69</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>-3.80684</td><td>-4.2089</td><td>-5.46</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="4">9</td><td>5.31882</td><td>6.67742</td><td>4.14</td><td>1.092418</td><td>0.988207</td><td>0.33</td><td>3.683057</td><td>5.899683</td><td>3.931878</td></tr><tr><td>-3.54375</td><td>-3.70537</td><td>-4.15</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2.08921</td><td>5.46665</td><td>3.07</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.50539</td><td>-4.48587</td><td>-1.74</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="4">10</td><td>2.88936</td><td>0.22467</td><td>1.67</td><td>0.755673</td><td>-0.37031</td><td>-0.1825</td><td>3.190654</td><td>3.582</td><td>2.553878</td></tr><tr><td>3.9722</td><td>4.38446</td><td>2.36</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>-2.73483</td><td>-2.264</td><td>-2.46</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>-1.10404</td><td>-3.82636</td><td>-2.3</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="4">11</td><td>-7.73562</td><td>-6.08531</td><td>-1.82</td><td>0.264435</td><td>-1.18447</td><td>-0.3075</td><td>5.744527</td><td>4.437982</td><td>1.912405</td></tr><tr><td>1.14462</td><td>-1.32663</td><td>0.48</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5.93113</td><td>4.67864</td><td>2.03</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1.71761</td><td>-2.00457</td><td>-1.92</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="4">12</td><td>0.55258</td><td>-0.32221</td><td>-1.74</td><td>1.497963</td><td>2.166475</td><td>1.425</td><td>0.72593</td><td>1.662023</td><td>2.293244</td></tr><tr><td>2.24654</td><td>2.87147</td><td>1.99</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1.82814</td><td>3.11129</td><td>3.74</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1.36459</td><td>3.00535</td><td>1.71</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Average</td><td></td><td></td><td></td><td>1.02668</td><td>0.639029</td><td>0.280208</td><td></td><td></td><td></td></tr></table>

Notations: Rp: weekly return of the portfolio; E(Rp): the monthly average return of the portfolio; SD(Rp): the standard deviation of the weekly returns in a month of the portfolio.

The portfolio construction process follows the procedures specified in Fig. 4. We first applied factor analysis to identify key risk factors. Daily return data were used in this step. The result indicated that three or four factors were identified in different data sets (as shown in Table 3). This is consistent with the findings by Roll and Ross [27], Brown and Weinstein [2], and Fogler [9].

Then, multiple regression analysis was used to price the assets. ANN and ARIMA methods were used to build risk models for return prediction. One hundred and three weekly return data were used at this step to shorten the model building time at a slight cost of precision. Two models (IANN and IARIMA each) were built. Through a trial-and-error process, we found that a 4–5–4 BPN was the most suitable for our data. The weekly return data were grouped into 96 training sets. Each set includes four weekly returns as the input and four weekly returns as the output. ANN models were built from the training data.

Finally, a set of candidate portfolios were built based on the predicted return and risk of each stock. The optimal was chosen among the candidates and its performances in the following four weeks were observed for evaluation. The performance of the TSEWPI was also calculated.

## 4.3. Results

Table 4 shows the results of the study. The left three columns show the weekly return of IANN,

IARIMA, and TSEWPI (the benchmark). The middle three columns show the average monthly return of the portfolios constructed from the above three methods. The right three columns show the standard deviation of the returns. It is obvious that IANN portfolios produced the highest average monthly return among the three. The performance rank is IANN > IARIMA > TSEWPI.

The paired t-test was used to test the hypotheses in Table 2. The result is shown in Table 5. In the Table, only two relations are statistically significant. They are $[Rp_{IANN} - Rp_{TSEWPI}]$ ( $p \leq 0.05$ ) and $[E(Rp_{IANN}) - E(Rp_{TSEWPI})]$ ( $p \leq 0.01$ ). In other words, both the weekly return and monthly average return of the portfolios constructed by IANN are significantly higher than the benchmark. Since the standard deviations of the return between IANN and TSEWPI are not significantly different, we can conclude that IANN builds better portfolios.

Regarding the difference between IANN and IARIMA, the results in Tables 4 and 5 indicate that, though IANN performed better, their difference in performance is not significant. The performance of the IARIMA portfolios was not significantly better than the benchmark either.

Overall, the empirical study has shown that the IANN performs significantly better than the benchmark. A further comparison between IANN and IARIMA allows us to assume that both the ANN model and APT have contributions to the superior performance of IANN. Unfortunately, our data does not allow us to quantify the contribution of each element.

Table 5  
Results of the paired t-test

<table><tr><td>No.</td><td>Variable</td><td>Mean</td><td>Std. Dev.</td><td>P-value</td></tr><tr><td>1</td><td> $Rp_{IANN} - Rp_{TSEWPI}$ </td><td>0.7464715</td><td>2.3250799</td><td> $0.0310^a$ </td></tr><tr><td>2</td><td> $Rp_{IARIMA} - Rp_{TSEWPI}$ </td><td>0.3588208</td><td>2.1768369</td><td>0.2592</td></tr><tr><td>3</td><td> $Rp_{IANN} - Rp_{IARIMA}$ </td><td>0.3876506</td><td>2.4329529</td><td>0.2753</td></tr><tr><td>4</td><td> $E(Rp_{IANN}) - E(Rp_{TSEWPI})$ </td><td>0.7464715</td><td>0.8308131</td><td> $0.0099^b$ </td></tr><tr><td>5</td><td> $E(Rp_{IARIMA}) - E(Rp_{TSEWPI})$ </td><td>0.3588208</td><td>0.8313988</td><td>0.1630</td></tr><tr><td>6</td><td> $E(Rp_{IANN}) - E(Rp_{IARIMA})$ </td><td>0.3876511</td><td>0.9722737</td><td>0.1946</td></tr><tr><td>7</td><td> $SD(Rp_{IANN}) - SD(Rp_{TSEWPI})$ </td><td>0.3953197</td><td>1.6037874</td><td>0.4114</td></tr><tr><td>8</td><td> $SD(Rp_{IARIMA}) - SD(Rp_{TSEWPI})$ </td><td>0.5048245</td><td>1.2293494</td><td>0.1826</td></tr><tr><td>9</td><td> $SD(Rp_{IANN}) - SD(Rp_{IARIMA})$ </td><td>-0.1095048</td><td>1.1249790</td><td>0.7423</td></tr></table>

$^{a}$ is significant at 0.05 level.  
$^{b}$ is significant at 0.01 level.

## 5. Conclusions

Portfolio analysis is a key area in investment. In this paper, we have presented an integrated approach that combines APT with ANN to provide a better support. The integrated approach can effectively alleviate the shortcomings of using APT or ANN alone. Empirical results indicate that this integrated approach beats the benchmark, and outperforms other integrated approaches such as integrating APT with ARIMA.

This study is one of the first to investigate the integration of portfolio management theories and ANN. The findings in this research are helpful to further research in the application and implementation of unified programming. Naturally, limitations exist when we generalize the results. Many interesting areas for further research can also be identified. First, the portfolio generated by the integrated approach may not always be the most efficient. At present, the method focused on generating a portfolio whose performance is better than the specified benchmark. Unless the alternative generator provides the selector with a set of portfolios on the efficient frontier, there is no guarantee that the suggested portfolio will be efficient. Therefore, an interesting research issue is how to modify the approach to ensure the generation of efficient portfolios. One possible approach is to use an optimization technique such as the quadratic programming method again to replace the simulation-based approach.

Second, the empirical study only evaluates the stock portfolio. To extend this research, we may include different types of risk assets, such as bonds, future contracts, and foreign stocks in our analysis. It would be interesting to see whether the integrated method can perform as well in handling different types of assets.

Third, the empirical research studied 12 periods. This may be short for a complete evaluation. Therefore, the empirical findings from our research may be representative of the short-term performance of the integrated approach. When longer time intervals are available in the future, we would like to examine its long-term performance and time dependencies.

Forth, the empirical data were collected from the Taiwan stock market in this research, we may further extend it to other markets such as the U.S.A., Japan, and Hongkong market in the future.

Finally, one drawback of ANN is that it is unable to provide good explanation of its decisions. Therefore, the integrated approach may be used to combine with the rule-based approach to build expert systems for portfolio management. This may allow the reasoning to be explained by the knowledge base. It is useful for giving investors more confidence in the suggestions from the system.

## Appendix A

The formula for calculating the score of each candidate:

1. Use the extra return (ER) to be the Y-axis, and the risk (standard deviation, SD) to be the X-axis. The investor's preference (SD, ER) is the original point.

2. Divide all candidates into four quadrants using their predicted returns and risks. The predicted extra return of a candidate is the ERhat, and the predicted risk of a candidate is the SDhat. For each candidate: (1) if SDhat > SD and ERhat ≥ ER, then it belongs to the first quadrant (moderate quadrant); (2) if SDhat ≤ SD and ERhat ≥ ER, then it belongs to the second quadrant (excellent quadrant); (3) if SDhat ≤ SD and ERhat < ER, then it belongs to the third quadrant (moderate quadrant); (4) if SDhat > SD and ERhat < ER, then it belongs to the forth quadrant (bad quadrant).

3. Assign score to each candidate based on the following equation:

candidates in the first quadrant:

$$
\text { score } = - \text { distance } (S D - S D h a t, E R - E R h a t), \tag {A.1}
$$

candidates in the second quadrant:

$$
\text { score } = \text { distance } (S D - S D h a t, E R - E R h a t), \tag {A.2}
$$

candidates in the third quadrant:

$$
\text { score } = - \text { distance } (S D - S D h a t, E R - E R h a t), \tag {A.3}
$$

candidates in the forth quadrant:

$$
\begin{array}{r l} \text { score } & = - \text { distance } (S D - S D h a t, E R - E R h a t) \\ & - 1 0, \end{array} \tag {A.4}
$$

$$
\text { where   distance } (X, Y) = (X ^ {\wedge} 2 + Y ^ {\wedge} 2) ^ {\wedge} (1 / 2).
$$

<table><tr><td colspan="3">FOOD:</td></tr><tr><td>Wei Chuan FoodPresident Enterprise</td><td>Great Wall Enterprise</td><td>Charoen Pokthand Enterprise</td></tr></table>

## Appendix B

The 51 stocks selected are (listed by industry):

## CEMENT:

<table><tr><td>Taiwan Cement</td><td>Asia Cement</td><td>China Rebar</td></tr></table>

## PLASTICS:

Formosa Plastic
Taita Chemical

China General Plastics Corp. Asia Polymer

## TEXTILES:

Far East Textile
Carnival Textile
Formosa Chemical & Fibre

Hualon-Teijran
Pao Shiang Ind.

Chung Shing Textile
Taroko Textile

## ELECTRICAL MACHINERY:

Tatung

Shihlin Elec. & Eng.

## ELECTRICAL APPLIANCES,

WIRE AND CABLE: Taiwan Fluorescent

Sampo

Kolin

CHEMICALS:
China Chemical
Formosan Union Chemical

Namchow Chemical

Lee Chang Yung Chemical Ind.

GLASS: Taiwan Glass

PULP AND PAPER:
Shihlin Paper
Long Chen Paper

Chung Hwa Pulp

Ban Yu Paper

## IRON AND STEEL:

China Steel

U-Lead Ind.

## RUBBER:

Tay Feng Tire

China Synthetic Rubber

## AUTOMOBILE:

Yue Loong Motor

ELECTRONICS:

Rectron Ltd.

United Micro Electronics

CONSTRUCTION:
Kuochan Devel. & Const.

Pacific Const.

SHIPPING:
Evergreen Marine

TOURIST:
Ambassador Hotel

BANKING AND INSURANCE:
Chang Hwa Bank First Bank
The Medium Business Bank of Hsin Chu

China Development I.C.B.C.
The Medium Business Bank of Taiwan

## DEPARTMENT STORE:

Far East Dept.

## References

[1] G.E.P. Box and G.M. Jenkin, Time Series Analysis - Forecasting and Control (Holden-Day, San Francisco, 1976).

[2] S.J. Brown and M.I. Weinstein, A New Approach to Testing Asset Pricing Models: The Bilinear Paradigm, Journal of Finance 3 (June 1983) 711–743.

[3] S.K. Chang, C.H. Loo and C.W. Chang, The Pricing of Futures Contracts and Arbitrage Pricing Theory, Journal of Financial Research 13 (Winter 1990) 297–306.

[4] N.F. Chen, R. Roll and S.A. Ross, Economics Forces and the Stock Market, Journal of Business 59 (July 1986) 383–403.

[5] N.F. Chen, Some Empirical Tests of the Theory of Arbitrage Pricing, Journal of Finance 38, No. 5 (Dec. 1983) 1393–1414.

[6] S.J. Chen and B.D. Jordan, Some empirical tests in the arbitrage pricing theory: Macrovariables vs. derived factors, Journal of Banking and Finance 17 (Feb. 1993) 65–89.

[7] G. Cybento, Approximation by Superposition of a Sigmoidal Function, Mathematics of Control, Signals, and Systems (Springer-Verlag, New York Inc., 1989).

[8] P. Dhrymes, I. Friend and B. Gultekin, A Critical Reexamination of the Empirical Evidence of the Arbitrage Pricing Theory, Journal of Finance 39, No. 2 (June 1984) 323–346.

[9] H.R. Fogler, Common Sense on CAPM, APT and Correlated Residuals, Journal of Portfolio Management (Summer 1982) 20–28.

[10] M.J. Gruber, Arbitrage Pricing Theory and Portfolio Management, The Second International Conference on Asian-Pacific Financial Markets (Sep. 1991).

[11] G.S. Jang, F. Lai and T.M. Parng, Intelligent Stock Trading Decision Support System Using Dual Adaptive-Structure

Neural Networks, Journal of Information Science and Engineering 9 (1993) 271–297.

[12] G.S. Jang, F. Lai, B.W. Jiang and T.M. Parng, Intelligent Stock Trading System with Price Trend Prediction and Reversal Recognition Using Dual-Module Neural Networks, Journal of Applied Intelligent 3 (1993) 225–248.

[13] H. Kaiser, The Varimax Criterion for Analytic Rotation in Factor Analysis, Psychometrika 23 (1958) 187–200.

[14] K. Kamijo and T. Tanigawa, Stock Price Pattern Recognition: A Recurrent Neural Network Approach, Proceedings of the International Joint Conference on Neural Networks 1990 I (1990) 215–221.

[15] T. Khanna, Foundations of Neural Networks (Addison-Wesley Publishing Company, 1989).

[16] T. Kimoto, K. Asakawa, M. Yoda and M. Takeoka, Stock Market Prediction System with Modular Neural Networks, Proceedings of the International Joint Conference on Neural Networks 1990 I (1990) 1–6.

[17] J.K. Lee and Y.U. Song, Unification of Linear Programming with a Rule-Based System by the Post-Model Analysis Approach, Management Science 41, No. 5 (1995) 835–847.

[18] J.K. Lee, Integration and Competition of AI with Quantitative Methods for Decision Support, Expert Systems with Applications 1, No. 4 (Mar. 1990) 1–16.

[19] J.K. Lee, R.R. Trippi, S.C. Chu and H.S. Kim, K-FOLIO: Integrating the Markowitz Model with a Knowledge-Based System, The Journal of Portfolio Management (Fall 1990) 89–93.

[20] B.N. Lehmann and D.M. Modest, The Empirical Foundations of the Arbitrage Pricing Theory, Journal of Financial Economics 21 (1988) 213–254.

[21] T.P. Liang, H. Moskowitz and Y. Yih, Integrating Neural Networks and Semi-Markov Process for Automated Knowledge Acquisition: An Application to Real-Time Scheduling, Decision Sciences 23, No. 6 (Nov./Dec. 1992) 1297–1314.

[22] C.Y. Lin, V.W.C. Liu and J.F. Chu, A Research of Examining the Macroeconomics Factors and Constructing the Optimal Portfolio for the Taiwan Stock Market – Using the Arbitrage Pricing Theory Approach, NSC Report 81-0301-H-110-501, Taiwan (Sep. 1992).

[23] I. Matsuba, Application of Neural Sequential Associator to Long-Term Stock Price Prediction, Proceedings of the International Joint Conference on Neural Networks 1991 II (Nov. 1991) 1196–1201.

[24] C.B. McGowan, Jr. and K. Tandon, A Test for the Cross-Sectional Robustness of the Arbitrage Pricing Model Using Foreign Exchange Rates, Decision Sciences 20 (1989) 142–148.

[25] S. Piramuthu, M.J. Shaw and J.A. Gentry, A Classification Approach Using Multi-Layered Neural Networks, Decision Support Systems 11 (1994) 509–525.

[26] D.L. Reilly et al., Risk Assessment of Mortgage Applications with a Neural-Network System: An Update as the Test Portfolio Ages, Proceedings of the International Joint Conference on Neural Networks 1990 Wash. II (1990) 479–482.

[27] R. Roll and S.A. Ross, An Empirical Investigation of the Arbitrage Pricing Theory, Journal of Finance 35, No. 5 (1980) 1073–1103.

[28] R. Roll and S.A. Ross, APT - Balancing Risk and Return (The Roll and Ross Asset Management Corporation, 1991).

[29] R. Roll and S.A. Ross, Regulation, the Capital Asset Pricing Model, and the Arbitrage Pricing Theory, Public Utilities Fortnightly (May 26, 1983) 22–28.

[30] R. Roll and S.A. Ross, The Arbitrage Pricing Theory Approach to Strategic Portfolio Planning, Financial Analysts Journal (May/June 1984) 14–26.

[31] S.A. Ross, The Arbitrage Theory of Capital Asset Pricing, Journal of Economic Theory 13 (Dec. 1976) 341–360.

[32] D.E. Rumelhart, J.L. McClelland and the PDP Research Group, Parallel Distributed Processing Explorations in the Microstructure of Cognition, Vol. 1: Foundations (The MIT Press, 1986).

[33] W.F. Sharp, Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk, The Journal of Finance 19, No. 3 (Sep. 1964) 425–442.

[34] S. Srirengan and C.K. Looi, On Using Backpropagation for Prediction: An Empirical Study, Proceedings of the International Joint Conference on Neural Networks 1991 II (1991) 1284–1290.

[35] A.J. Surkan and X. Ying, Bond Rating Formulas Derived through Simplifying a Trained Neural Network, Proceedings of the International Joint Conference on Neural Networks 1991 II (1991) 1566–1570.

[36] T. Tanigawa and K. Kamijo, Stock Price Pattern Matching System: Dynamic Programming Neural Network Approach, Proceedings of the International Joint Conference on Neural Networks 1992 II (1992) 465–471.

[37] W. Vandaele, Applied Time Series and Box-Jenkins Models (The Academic Press, 1983).

[38] Ward Systems Group, Inc., NeuroShell: Neural Network Shell Program (245 W. Patrick St., Frederick, MD 21701, Feb. 1990).

[39] C.S. Wu and J.Y. Lin, The Influence of Factors Affecting Price Change on the Explanation Power of Asset Pricing Models: An Empirical Evidence on the Listed Stocks in Taiwan Securities Exchange, Journal of Management Science 7, No. 2 (Dec. 1990) 155–180.

[40] C.C. Yang, S.C.T. Chou, F. Lai and G.S. Jang, Optimization of Neural Stock Market Prediction Systems Using Parallel Distributed Genetic Algorithm, Neural Network World (June 1993) 883–894.

[41] Y. Yoon and G. Swale, Predicting Stock Price Performance: A Neural Network Approach, Proceedings of the 24th Annual Hawaii International Conference on Systems Sciences 4 (1991) 156–162.

![](/api/attachments/4JWC4CA3/fulltext/images/0669c003d9f85dbaa46801cf04ab785dcb8a432a884db552fdc549c0825a4a51.jpg)

Shin-Yuan Hung is a doctoral student in the MIS program at the National Sun Yat-sen University (Taiwan, ROC). He received his Masters degree in MIS from the same University and his Bachelors degree in Statistics from the National Chung Hsing University (Taiwan, ROC). In addition to financial support systems, his current research interests include executive information systems and group decision support systems.

![](/api/attachments/4JWC4CA3/fulltext/images/2c01456d00bd435d21f5c903c5dda9832355db1b6328c70f6f36fc7d830d09b8.jpg)

Ting-Peng Liang is Professor in Information Systems and Dean of the College of Management at the National Sun Yat-sen University. Prior to the current position, he had been Director of the Institute of Information Management at the same university and on the faculties of the Purdue University and the University of Illinois at Urbana-Champaign. He has served on the editorial boards of eight professional journals and the program committees of many international

conferences. His papers have appeared in journals such as Management Science, Operations Research, Decision Support Systems, MIS Quarterly, Journal of MIS, IEEE Computer, among others.

![](/api/attachments/4JWC4CA3/fulltext/images/549f66a9714d27b42d219737b795c82f9f52879f2854bd1363962a5f24b607dd.jpg)

Victor Wei-Chi Liu has recently been appointed president of the national Sun Yat-Sen University. Prior to that appointment, he was the president of the Central Investment Holding Company in Taiwan. He received his Ph.D. degree from the Kellogg Graduate School of Management, Northwestern University. He is also a part-time professor at the National Sun Yat-sen University. His research interests include corporate finance, portfolio management and agency theory.
