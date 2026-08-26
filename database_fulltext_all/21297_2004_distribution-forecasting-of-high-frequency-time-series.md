---
otero_id: 21297
otero_key: "FZXYXJAE"
title: "Distribution forecasting of high frequency time series"
authors: "Andy Pasley; Jim Austin"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00083-6"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Distribution forecasting of high frequency time series

Andy Pasley, Jim Austin\*

Department of Computer Science, University of York, Heslington, York YO10 5DD, UK

Available online 9 July 2003

## Abstract

The availability of high frequency data sets in finance has allowed the use of very data intensive techniques using large data sets in forecasting. An algorithm requiring fast k-NN type search has been implemented using AURA, a binary neural network based upon Correlation Matrix Memories. This work has also constructed probability distribution forecasts, the volume of data allowing this to be done in a nonparametric manner. In assistance to standard statistical error measures the implementation of simulations has allowed actual measures of profit to be calculated.

Keywords: Financial forecasting; Neural networks; Associative memories; Probability distribution forecasting; High frequency time series

## 1. Introduction

Many techniques for forecasting nonlinear time series exist. Traditionally in finance forecasters have looked at daily or monthly prices. Recently the availability of large high frequency data sets has encouraged much more research into intra-day and even tick price forecasting. It has also made possible the use of very data-intensive forecasting techniques and the adjustment of traditional techniques. An introduction to this new field is Ref. [5].

The Farmer–Sidorowich [9] forecasting algorithm is well understood and many forecasting methods implement a variant of it. Delay coordinates are used to construct representations of the current and all previous states. The state at time t of a variable x, denoted S(x ) is constructed from the observed values:

$$
x _ {t}, x _ {t - 1}, x _ {t - 2}, \ldots , x _ {t - d + 1}
$$

The parameter d is considered the window size or embedding dimension, the number of most recent historical values that will be used to construct a state. It is assumed that a functional relationship between the current state and the future state exists.

$$
x _ {t + 1} = f (S (x _ {t}))
$$

For this function to exist the attractor must be static or evolving only slowly. At this stage, it is assumed that the time series shows this property (evidence of this relationship has been documented [19]) but it is tested for as part of this work.

The aim is to construct a predictor approximating the function f. A forecast of the next price is constructed from one or more ‘local’ states considered similar by some distance metric to the current state. For each local state, the next value is its evolution. The evolutions of the local states are used to forecast the evolution for the current state, often by fitting a linear polynomial. Delay coordinates require the window size to be determined but there are no clear rules on how this should be done. Several researchers have produced guidelines in line with the study of nonlinear dynamics [9,14,17], but embedding is still considered an art as much as a science. In the field of neural network design for forecasting, Genetic Algorithms have often been considered [16,18,24]. Other issues the technique introduces are which distance metric to use, how to implement it and how many neighbour states should be used to construct a forecast?

Traditional forecasting methods produce point forecasts, each prediction is a single value. Alternatively probability and interval forecasting has been reported in the literature, for example [1,4]. Full probability distribution forecasts contain extra information, which can be utilised by modern risk management systems or allow improved trading models. This work produces as forecasts, discrete probability distributions and is part of a new but expanding area of research.

## 2. AURA for Farmer –Sidorowich forecasting

The Farmer–Sidorowich algorithm relies on the implementation of a k-NN (or similar) search to decide on the local states. Also, with large data sets of high frequency data it is important that this search can be done quickly, producing forecasts in time for them to actually be used. This work uses the Advanced Uncertainty Reasoning Architecture (AURA) developed at the University of York to implement this search.

AURA is an implementation of associative memories using binary Correlation Matrix Memories (CMMs). CMMs are a form of static associative memory and are equivalent to a single layer fully connected feed-forward perceptron with binary weights. CMMs learn associations between patterns P and separators S, $p _ { i } \longrightarrow s _ { i } ,$ despite straightforward training (learning) and recall methods.

These patterns and separators (or classifiers) are presented to the CMM as bit (binary digit) vectors. During training each pattern and associated separator are presented to a matrix M, which is initially empty before any associations have been presented for training. For every association presented to the CMM during training, the CMM values only change where both the input (pattern) and output (separator) are set to one (Hebbian learning).

$$
M = \bigvee_ {i} s _ {i} ^ {T} p _ {i}
$$

The recall operation returns a vector of integers $\nu _ { k } .$ $\nu _ { k }$ can then be thresholded to recover individual separator(s).

$$
v _ {k} = M p _ {k} ^ {T}
$$

CMMs provide several key features, most notably partial matching. The CMM effectively uses the hamming distance to measure how close an input is to potential separators. As we are operating on binary values, the hamming distance is equivalent to euclidian distance.

 Quick training: Each association is only presented to the CMM once during training, as opposed to a typical MLP network which can require thousands of cycles through the data.

 Generalising on unseen data: Presented with a key that has not been seen before, a CMM can return the closest match.

 Nearest Neighbour searches: A CMM can be used to return several separators, those returned being the closest to the input pattern.

Further explanation of AURA and CMMs can be found in Ref. [2]. The use of associative memories for financial forecasting is a small area of work, but includes [10,12].

An investigation into the use of AURA for k-NN type problems has already been carried out [26] with promising results. The binary nature of AURA makes it fast, efficient and easy to implement into hardware for further improved performance [25]. AURA maps binary input vectors to binary output vectors which can be treated as classifiers or as the centre of a cluster. It allows partial matching from similar input vectors to the same output vector through the use of threshold logic. Adjusting a threshold allows easy control over the cluster size. One problem specified previously is that of how many states should be used to construct a forecast? It is easy using AURA to select states within a certain distance metric, allowing this value to vary depending upon the proximity of the neighbours.

Before being presented to AURA, data needs to be converted to binary codes for the construction of bit vectors. In the case of prices, this is a mapping from real numbers to a finite number of binary codes. These codes are then used to construct the state vectors which are presented to AURA as input. This encoding process must have certain properties which depend upon the specific problem.

## 3. Distribution forecasting

Producing distribution forecasts or measuring risk (especially the likelihood of extreme values) is simplified by making the assumption that financial returns follow a normal distribution. Under such an assumption, many simple measures of risk such as the Sharpe Ratio [3,20] have been developed. However, it is now fairly well accepted that financial returns do not follow a normal distribution, evidence for this being reported by Refs. [8,15,19,21]. This has encouraged the measurement of skewness and other properties of financial returns. The market is considered a chaotic system where the generating process varies over time. The actual distribution at any given time is not observed and cannot be known, making evaluating the distributions a difficult task.

The rejection of normality makes distribution forecasting a complex task. The fact that distributions are only now being researched is probably due to complexity in calculating the distribution and the lack of standard methods to evaluate it. Work by [7] highlights the advantages of distributions and their ability to allow calculation of all measures of risk. However the field of distribution forecasting is growing all the time as risk management advances. It is reported [6], that ‘The booming area of financial risk management is effectively dedicated to providing density forecasts of portfolio values.

How useful a distribution forecast is and how it should be used is related to an individuals’ loss function. This suggests that a density forecast must be tailored to particular requirements depending on how it is to be used, but fortunately this is not the case. A proof has been published [6], that ‘Regardless of loss function, we know that the correct density is weakly superior to all forecasts.

More flexible parametric distributions have been used, in particular the work of [7] showing promise. Different mixture model approaches have also been used, in particular [22,23]. The work reported here uses a completely nonparametric approach. The simplest nonparametrical technique is historical simulation. Each observation is weighted equally to construct a histogram, which is normalised and treated as a discrete probability distribution. This requires larger data sets, but such data sets are available for high frequency finance. The forecast then remains constant over time or is updated as new observations are made. However all historical data is used to construct each forecast and the distribution can only change slowly over time. This behaviour is unlikely to be repeated by financial data, which is considered the result of a nonlinear process showing chaotic behaviour.

Ideally a distribution forecasting technique that captures the dynamics of the system should be constructed. As part of this work, the Farmer – Sidorowich method has been modified for this purpose. With standard Farmer –Sidorowich, to produce each forecast a search for the local states is implemented. Then the evolutions are used to make a point forecast, usually by a simple linear process. Alternatively this work uses the evolutions to construct a frequency histogram. Effectively the data is being clustered (by the k-NN search used by the Farmer– Sidorowich algorithm) and a historical simulation performed on each cluster individually. This is a historical simulation based upon only historical data considered relevant.

## 4. Forecasting architecture

A novel forecasting architecture, AURA-FS has been constructed by bringing together the Farmer– Sidorowich method, AURA networks (including a new encoding scheme for financial data) and distribution forecasting. The form of distribution forecasting used is the variant of historical simulation described in the previous section. Data is pre-processed before presentation to AURA-FS in line with common practice. The series of prices is converted to the series of returns, expressed as the percentage change in price.

![](/api/attachments/FZXYXJAE/fulltext/images/2a46842127c3046db077774d1478cc160e32f133461a45afae09a0ae7a7cd091.jpg)  
Fig. 1. Training. The CMM is updated to learn the relationship between the input and the features (clusters). The frequency store holds a historical simulation for each cluster.

$$
r _ {t} = \frac {p _ {t} - p _ {t - 1}}{p _ {t - 1}} \times 1 0 0
$$

where $p _ { t }$ is the price at time t and $r _ { t }$ is the return at time t.

AURA-FS consists of a training algorithm and a forecasting algorithm. During training the data is clustered, using CMMs partial matching capabilities to match many states as a single cluster. Each cluster represents a set of similar patterns and is considered a feature of the data. The training process is illustrated in Fig. 1. Each state and evolution (next observed value) are encoded into binary vectors to be used as inputs to a CMM. First a recall operation is performed on the CMM to see if the state fits any previous cluster(s). If so, the evolution is used to update the frequency store for all matching features. If this state is considered part of a new feature, the state and evolution are presented to the CMM for a learn operation, introducing a new feature into the system, for which the current evolution is the first observation for constructing a distribution.

Varying the threshold affects the size of clusters and therefore the number of features created and how many observations are used to construct the histogram for each feature.

Forecasting with AURA-FS requires the encoding of the current state, so it can be presented to the CMM as a bit vector. A recall on the CMM then retrieves the features which are best matched. The number of features returned can be altered by changing the threshold. Each feature has a histogram associated with it in the frequency store. A weighted average of these histograms provides the overall forecast. The weights are dependent upon how well a feature matches the current state. The forecasting process is illustrated in Fig. 2.

AURA requires binary inputs and therefore a quantisation process is necessary to convert data to binary codes before presentation to AURA. Many general techniques for this sort of encoding problem already exist, such as CMAC and CMAC-Gray [11]. These techniques have been developed without specific consideration of their use by AURA and CMMs. For a CMM to run more efficiently, more accurately and using the minimum amount of memory the codes produced by the encoder should ideally have certain properties.

![](/api/attachments/FZXYXJAE/fulltext/images/7daa900ac45530238186ed2eb9de2f0e620dc1127ec0c4934b7bf0e0f3724bf6.jpg)  
Fig. 2. Forecasting. A recall on the CMM produces the nearest neighbours from which the forecast is constructed. Each neighbour has its own distribution in the frequency store.

By definition a CMM is of a finite size which can’t change during its lifetime. Therefore all codes presented to it or recalled from it must be of a constant size. As more and more associations are presented to a CMM, the more and more bits in the memory are set and the probability of error in recall increases. Where this error is too high a CMM is said to be saturated. An efficient CMM holds as many associations as possible without being saturated. This requires the two extra conditions

 Sparse codes with only a few bits set.

 All bits equally likely to be set. The distribution of the codes should be as close to uniform as possible.

Where nearest neighbour seaching is to be implemented with a CMM, another requirement is input ordering preservation. It is clear that inputs which are close together must remain close together once encoded. For the purposes of implementing Farmer– Sidorowich type methods for financial forecasting, these extra properties have been suggested [12].

 Invariance to input distribution. As the forecasting algorithm makes no assumptions of the distribution of the data, nor can any encoding method used. This should be kept under consideration when ensuring the codes have a uniform distribution.

 Limited coding distortion. Error in the important/ relevant areas should be as small as possible at the expense of other areas.

The second of these points is too be discarded currently, as for financial forecasting purposes it is currently unclear where data should be considered particularly important or relevant. For all these constraints to be achieved, a coding technique designed specially for AURA-FS was required. An encoder utilising a quantisation process was constructed.

Quantisation is usually considered a process of assigning the data into different intervals or ‘bins’, each data point assigned to one bin. A one-dimensional quantiser (on an alphabet e) can be formally defined [12] as a collection of N levels or representative values $Y = y _ { 1 } , . . . , y _ { N } , y _ { i } { \in } \varepsilon ,$ and a set of crossover values $- \infty = x _ { 1 } < y _ { 1 } \leq x _ { 2 } < y _ { 2 } \leq x _ { 3 } . . . y _ { N - 1 } \leq x _ { N } <$ $y _ { N } { < } x _ { N + 1 } { = } \infty$ . The quantiser $Q ( x )$ maps $x { \in } \varepsilon$ into the level $y _ { j } , \mathrm { i f } \ x { \in } ( x _ { j } , x _ { j + 1 } )$

Traditionally quantisation is performed with a fixed interval size,

$$
\forall i (x _ {i + 1} - x _ {i} = x _ {i + 2} - x _ {i + 1})
$$

To fulfil the encoding criterion already discussed, variable width intervals are required for encoding financial values. This process is followed by generating a binary code for each bin. Assuming that a value $x _ { i }$ is encoded as a binary sequence $b _ { i } ,$ a state vector of the form $\left[ x _ { t - 1 } , x _ { t - 2 } , . . . , x _ { t - d } \right]$ for some window size $d ,$ this state will be presented to the CMM as the binary sequence $[ b _ { t - 1 } b _ { t - 2 } . . . b _ { t - d } ]$

The encoder used in AURA-FS performs a historical simulation on the full training set and uses this estimated distribution to place the bin boundaries so that the training set would be equally distributed about the bins created. Input order preservation is achieved by the use of codes with more than one bit set, selected so that there is an overlap between the codes of nearby values. This process makes no assumption of the distributional form of the data, maintaining the completely nonparametric manner of the algorithm. This leaves several parameters of AURA-FS which must be decided.

 Window Size

 Number of bins

 Training threshold

 Recall (forecasting) threshold

As discussed before, techniques exist for determining the window parameter, but they are no more than guidelines. The other parameters are particular to CMMs and haven’t been investigated elsewhere. Despite the large data sets being investigated, a full search of the parameter space was possible.

Traditional error measures such as Root Mean Square Error (RMSE) evaluate point forecasts only. The distribution forecasts produced here can be collapsed to point forecasts using simple techniques. Taking the mean or the highest point of the distribution produced similar results, but using the highest point proved slightly preferable. Ideally the full distribution forecast should be evaluated and this is returned to later in this work.

## 5. Simulations

AURA-FS was tested on a data set of exchange rates between Japanese Yen and US Dollars supplied by Olsen and Associates. From this data, sets of size 100,000 and 200,000 were used. They are high frequency sets, with the set of 100,000 prices covering only from 1 October 1992 to 8 December 1992. The first 75% of each data set was taken for training and the rest held back as an out of sample test set.

For finance, error measures such as RMSE and Mean Actual Percentage Error (MAPE) are considered unsuitable. Average Directional Accuracy (ADA) has been shown to closer match financial loss functions [13]. The following definition of ADA has been used [12].

$$
\mathrm{ADA} = \frac {1}{N} \sum_ {i = 1} ^ {N} f (\hat {x} _ {i}, x _ {i}, x _ {i + 1}) (1 0 0)
$$

$$
f (i, j, k) = \left\{ \begin{array}{l l} 1 & \text { if } \operatorname{sgn} (i - j) = \operatorname{sgn} (k - j), \\ 0 & \text { otherwise } \end{array} \right. \quad \operatorname{sgn} (i) = \left\{ \begin{array}{l l} - 1 & \text { if } i <   0, \\ 0 & \text { if } i = 0, \\ 1 & \text { if } i > 0. \end{array} \right.
$$

Theil’s U statistic is another directional measure, the ratio of RMSE from the forecasts compared to RMSE where a simple no change forecast is issued. This measure offers a quick comparison with a naive forecast. A lower value is preferable and where a set of forecasts are less accurate than a no change model an error measure above 1 will be returned. To provide a benchmark for the ADA results the accuracy of another naive forecast was calculated on the data. Predicting the future movement as the previous direction of movement achieved an ADA of 46.2%.

The effect of parameter values on the model was investigated by calculating the error measures for thousands of models. Fig. 3 shows the ADA results and Fig. 4 shows the Theil’s U statistic over a range of values for the window size and number of bins. Visual inspection is aided by colouring the surface, the colour depending upon the error value. Similar experiments have been run to determine the influence of other parameters but not included here. Where no result is given for a set of parameters, this is because no forecasts were made. This can occur depending on the parameters and is due to no state in the test set matching any state encountered during training. This is a symptom of too small clusters and with lower thresholds, smaller bin widths and/or a smaller window size can be avoided. Alternatively larger data sets could be investigated, despite those already in use being significantly larger than usual financial data sets.

Theil’s U statistic shows that varying the parameters impacts strongly upon the error with some models comparing badly to a naive forecast. In many areas of the parameter space the error is consistently below one however, demonstrating theoretical forecasting power of a market considered very efficient. The best results returned are a Theil’s of 0.892 and an ADA of 56.9%. The ADA results show even stronger variation over the parameter space, producing clear regions of high and low accuracy. The relationship of individual parameters to the error can easily be noted.

Using a simple technique, the forecasts were converted to BUY, HOLD or SELL signals. Based upon these signals a simple trading strategy could be implemented and its return calculated. At this point it must be pointed out that this simulation includes no transaction charges or costs. Also the ability to trade as suggested by the trading strategy could be affected by practical considerations ignored here (e.g. barriers to market entry). The simulations in Fig. 5 show the effect of the parameters on the return (calculated from the resultant value of trading with an initial investment of 100 USD). The graph shows that many models return excess profit and some produce large returns.

The current method of converting the AURA-FS forecasts to trades is very simple and produces a large volume of trading. It is expected that this large trading volume would incur high costs and/or practical difficulties. Preliminary work in translating this to a measure of actual profit has been completed but not included here due to the long discussion it would require. It is believed that improvements in the trading strategy could produce less trading volume, improving the potential for profit.

During this technique, the distributions from several clusters are used to construct each overall forecast. This can be thought of as a mixture model approach but has clear differences between most

![](/api/attachments/FZXYXJAE/fulltext/images/57c7c930061a8ebc7dab0a84cb4fb2d444c6594e50aa22928951a200c46bfd55.jpg)  
Fig. 3. The effect of the window size and number of bins on the ADA error measure. The x and y axes show the parameter values and the z axis shows the error value.

mixture model implementations. For each forecast made the majority of clusters (experts in mixture model terminology) are given a weight of zero. For simplicity mixture models are normally implemented so that each expert’s forecast is Gaussian. While this does not require that the overall forecast should be of Gaussian nature, this is not ideal.

It was important to check that this fusing of different forecasts was occurring and determining the effect this had on results in comparison to a

![](/api/attachments/FZXYXJAE/fulltext/images/fa7990ca10a3523c8c36372df704c98b7e4897cdeece234558ee912c1a0f8da1.jpg)  
Fig. 4. The effect of the window size and number of bins on the Theil’s U statistic error measure. The x and y axes show the parameter values and the z axis shows the error value.

![](/api/attachments/FZXYXJAE/fulltext/images/7886c717419b4cfdba18e0c6646116965920202f43bd295219a3e070dbf72c44.jpg)  
Fig. 5. The effect of the window size and number of bins on the simulation return. The x and y axes show the parameter values and the z axis shows the return.

system using just one cluster (the best match to the current state) for each forecast. These different approaches are referred to as ‘Combining’ and ‘Best only’ throughout the results presented. Fig. 6 displays results for a particular parameter set which had achieved good results in the previous experiments. It is demonstrated that as the recall threshold is lowered (while the training threshold remains constant) the average number of features used to make each forecast increases rapidly. This is proof that the architecture combines different features as intended. The results also show the value of this combining, with an increase from 53.1% to 56.9% in directional accuracy resulting from using more than one feature.

![](/api/attachments/FZXYXJAE/fulltext/images/0d66a76545c2da535f4df8b533a27c4bc1f1b57eb0313a9be7db180916642d25.jpg)  
Fig. 6. The effect of lowering the recall threshold on forecast accuracy and the number of features used. The average given is the mean number of features used per forecast over the whole test set.

The effect of lowering the recall threshold on forecast accuracy for a range of parameter sets

<table><tr><td rowspan="2">Number of features</td><td colspan="2">ADA (%)</td><td colspan="2">Theil&#x27;s</td></tr><tr><td>Combining</td><td>Best only</td><td>Combining</td><td>Best only</td></tr><tr><td>372</td><td>56.6</td><td>56.1</td><td>0.897</td><td>0.900</td></tr><tr><td>987</td><td>56.9</td><td>56.1</td><td>0.892</td><td>0.892</td></tr><tr><td>7450</td><td>56.9</td><td>53.2</td><td>0.897</td><td>0.931</td></tr></table>

This pattern is repeated for other parameter sets. Table 1 shows a comparison for several parameter sets, for which the total number of features found is stated. Again an improvement is clear between the two approaches.

## 6. Extending the forecasts

The simulation results highlighted both the promise of the forecasts and the problems of working with high frequency data. Forecasting only the next value provides a trading intensive algorithm, with a large number of transactions being created. This becomes an issue due to the margin between the bid and ask prices. For currency markets this margin is typically only a few basis points (the smallest amount a price can move) and is usually considered negligible for long term trading. For high frequency forecasting it is a barrier which can only be overcome by forecasting accurately the magnitude of changes rather than just direction.

An improved trading strategy could use forecasts further into the future than ‘next-step’, while still using all of the data available in a high frequency data set. The current architecture, while at time t, produces a forecast for t + 1. During this work, an extension of length k refers to a forecast for t + 1 + k. There were different methods by which the existing algorithm could be changed to produce such ‘extended’ forecasts.

A simple and intuitive method is to modify the training phase to take into account the required extension. For an extension of length k, the evolution of the state for time $S _ { t }$ in the training set is now $x _ { t + 1 + k } .$ The forecasting process remains unchanged but now produces a distribution for $x _ { t + 1 + k }$ . This is referred to as training extension.

The alternative is to leave the existing algorithm unchanged, construct a next-step forecast and treat the forecast as an observed value to produce another next-step forecast for further ahead. Using this iterative process a forecast can be extended as many time steps as required. AURA-FS requires that an observed value is a point rather than a distribution. Forecasts can be collapsed to point forecasts in the same manner as used previously, referred to here as iterative point extension. Alternatively, the full distribution forecast can be used by calculating a forecast for every value with a probability greater than 0. These different forecasts can be weighted by the probability given to them by the original forecast. Fig. 7 shows this process, termed iterative distribution extension here. The further ahead the forecast is required the more computationally expensive the forecasting process becomes. This currently prevents the use of this technique for large values of k, but if considered necessary the use of specialist hardware (discussed previously) could allow for longer extensions.

![](/api/attachments/FZXYXJAE/fulltext/images/1f6944c7d820ac6901ebdd1f3ed30edf1c244ebede84e5280963511d4f27d0b5.jpg)  
Fig. 7. Iterative extension using the distribution forecast. All possible values given by the previous forecast are treated as observations to make a possible forecast for one further step ahead. An average of all possible forecasts combines them to a single forecast. The weighted average is calculated by the probability given by the distributions of the series following that path.

![](/api/attachments/FZXYXJAE/fulltext/images/5c3586734f7688b5763c4c11277af5b695e6834f2de1b10bd93984d4a622366a.jpg)  
Fig. 8. The effect of extending k on forecast accuracy.

For training extension and iterative point extension a full study of the effect of k on the accuracy was possible. Fig. 8 shows a comparison between the two methods. The error measures for each k are a mean average of several parameter sets.

A comparison with iterative distribution extension over small extension lengths is displayed in Table 2.

The results demonstrate clearly that the training extension outperforms the iterative point extension, for all values of k. The level of accuracy achieved by training extension at larger values of k is very promising, directional remaining over 50% and Theil’s continuing to show an improvement on a no change forecast.

Table 2  
A comparison of different techniques for forecast extension

<table><tr><td rowspan="2">(k) Extension</td><td colspan="3">Directional accuracy(%)</td></tr><tr><td>Training</td><td>It. point</td><td>It. distribution</td></tr><tr><td>1</td><td>54.5</td><td>28.3</td><td>54.4</td></tr><tr><td>2</td><td>56.1</td><td>44.3</td><td>55.8</td></tr><tr><td>3</td><td>55.4</td><td>35.4</td><td>55.0</td></tr></table>

Iterative Distribution Extension shows comparable performance with Training Extension, but the latter involves much less computation and is considered preferable. Importantly, iterating the distribution is a clear improvement on iterating point forecasts. This is evidence that the excess information in the distribution is being used and is of sufficient accuracy to improve the forecast.

Overall, extending the forecast is clearly possible with the accuracy decaying only slowly as k increases. Work in progress involves using such extended forecasting for improved simulation results.

## 7. Evaluating the distribution forecast

The results and evaluation reported previously are for point forecasts. These forecasts have been constructed from the probability distribution forecasts produced by AURA-FS. The aim of this work was to produce accurate distributions which could be used by a risk management system or trading model. Evaluation of the full distributions is required.

The only technique known to the author of evaluating distribution forecasts using the observed values is to use the cumulative density function (cdf) of the forecast. The values of the cdf for the observed values should be uniformly distributed and iid. This method has been used in Refs. [6,23] where further details of implementing the test can be found.

As an alternative to using the observed values and the cdf it was preferable to test the behaviour of the time series in comparison to the assumptions made which influenced design of AURA-FS. The main requirements made by the Farmer–Sidorowich algorithm is that the series shows nonlinear ‘chaotic’ behaviour and the past can be used to predict the future.

For the particular implementation of Farmer – Sidorowich described here, this can be stated more precisely. During the training process the input space is clustered. The distribution for each cluster is observed during the training set and used to construct the forecasts. For forecasts constructed in this way to be accurate the distributions observed for each cluster must not vary over time, or at least not vary too much between the data used for training and the values being forecast. Whether this behaviour occurs depends on the attractor. Perfect performance from Farmer–Sidorowich forecasting requires a static attractor. If the attractor is evolving then forecast accuracy will decay depending on how quickly the attractor is changing. It was considered important to check whether the attractor behaviour allowed distribution forecasting.

An experiment can be constructed to check the behaviour of the data in this regard. The training stage is run as before to cluster the data and the observed distribution for each cluster stored. The data in the test set is then also used to construct an alternative distribution for each cluster. For each cluster we now have two observed distributions which have been stored as frequency histograms. They can be treated as two samples which (if time series behaviour is as expected) are drawn from a generating distribution. To test whether two samples are drawn from identical distributions, the Mann–Whitney and Smirnov tests were used as they are nonparametric and assume no form of the generating distribution. The results of these tests are given in Table 3.

The results are impressive for most of the clusters. Many passing the test at high levels of significance. They provide encouraging evidence that the distribution forecasts will be accurate, as they use distributions observed during training to forecast the distribution in the test set. Unfortunately the required level of accuracy for a forecast to be practically useable is difficult to answer, requiring further information on trading conditions. However, the accuracy suggested by these tests is very promising.

Results of check that the training distributions and test distributions are samples of the same distribution

<table><tr><td rowspan="2">Confidence level (α)</td><td colspan="2">Number of passes (%)</td></tr><tr><td>Mann-Whitney</td><td>Smirnov</td></tr><tr><td>0.05</td><td>94.2</td><td>98.9</td></tr><tr><td>0.10</td><td>88.0</td><td>97.6</td></tr><tr><td>0.20</td><td>74.7</td><td>95.0</td></tr></table>

The Mann – Whitney and Smirnov tests have been carried out for each feature.

Currently no further training occurs while forecasting the test set. In practice new observations could be used to make the distributions for each cluster adaptive. It is also simple to weight the distribution so that emphasis is placed upon more recent observations. This is done by giving each observation a decaying weight in the distribution, by weighting the new observation a and the previous distribution 1  a to construct the new histogram. It is easy (by varying a) to control how quickly the adaptive distribution changes. An adaptive distribution could model the behaviour of an evolving attractor and improve forecast accuracy.

## 8. Conclusion

Financial markets are considered very efficient and therefore difficult to forecast. Our work provides further evidence that this is so. The best Theil’s U statistic of 0.892 suggests only a 10% reduction in error than a naive forecast. There are however reasons to be optimistic about the obtained AURA-FS results. The best ADA of 56.9% and the Theil’s error show improvement upon the values reported for financial data previously in Ref. [12]. Unfortunately, there is little work in the literature for which direct comparison can be made, despite the suitability of these error measures for finance.

The point forecasts are constructed from full probability distribution forecasts that offer additional information which can be incorporated into a trading strategy. Investigation into the accuracy of the distributions provided evidence that the assumptions made of the algorithm are repeated in the high frequency data sets, suggesting that the distributions are accurate. Their use within a traditional risk management framework has not been explored currently but is an exciting area of future work.

Simulations which assume a perfect market with no barriers to market entry and no transaction costs have shown the possibility of excess profit. Currently a trading intense strategy is constructed by the algorithm which could strongly affect reported profit values. This situation could be improved by producing extended forecasts and a more intelligent trading strategy. It has been shown that the accuracy of forecasts falls slowly the further ahead in time forecasts are made. This extension requires only a small change to the algorithm and requiring no more memory or computational power. The current trading strategy implemented is simple and with further understanding can be improved. There is potential for better measurement of forecast utility and promise that the results have practical value.

## Acknowledgements

The research reported here has been supported by an EPSRC studentship.

## References

[1] Y. Ait-Sahalia, A. Lo, Nonparametric estimation of state-price densities implicit in financial asset prices, Journal of Finance 53 (1998) 499 – 547.

[2] J. Austin, Distributed associative memories for high speed symbolic reasoning, International Journal on Fuzzy Sets and Systems 82 (1996) 223– 233.

[3] M. Choey, A.S. Weigend, Nonlinear trading models through sharpe ratio maximization, International Journal of Neural Systems 8 (1997 August) 417 – 431.

[4] R.T. Clemen, A.H. Murphy, R.L. Winkler, Screening probability forecasts: constrasts between choosing and combining, International Journal of Forecasting 11 (1995) 133 – 146.

[5] M. Dacorogna, R. Gencay, U. Muller, R. Olsen, O. Pictet, An Introduction to High-Frequency Finance, Academic Press, London, San Diego, 2001.

[6] F.X. Diebold, T.A. Gunther, A.S. Tay, Evaluating density forecasts with applications to financial risk management, International Economic Review 39 (1998) 863–883.

[7] E. Eberlein, J. Breckling, P. Kokic, A tailored suit for risk management: the hyperbolic model, in: J. Franke, W. Ha¨rdle, G. Stahl (Eds.), Measuring Risk in Complex Stochastic Systems, Lecture Notes in Statistics, Springer, 2000, pp. 189 – 202.

[8] E.F. Fama, The behaviour of stock market prices, Journal of Business 38 (1965) 34– 105.

[9] J.D. Farmer, J.J. Sidorowich, Predicting chaotic time series, Physical Review Letters 59 (8) (1987) 845– 848.

[10] J. Jiminez, J.A. Moreno, G.J. Ruggeri, A. Marcano, Detecting chaos with local associative memories, Physics Letters A 169 (1992) 25– 30.

[11] A.R. Kolcz, N.M. Allinson, Enhanced n-tuple approximators, in: N.M. Allinson (Ed.), Proceedings of the Weightless Neural Network Workshop, University of York, York, UK, 1993, pp. 38– 45.

[12] D. Kustrin, Forecasting Financial Time Series with Correlation Matrix Memories for Tactical Asset Allocation. PhD thesis, Department of Computer Science, University of York, Heslington, York, YO10 5DD, England, July 1998.

[13] G. Leitch, J.E. Tanner, Economic-forecast evaluation-profits versus the conventional error measures, American Economic Review 81 (3) (1991) 580–590.

[14] P.S. Linsay, An efficient method of forecasting chaotic time series using linear interpolation, Physics Letters A 153 (1991) 353 – 356.

[15] B. Mandelbrot, The variation of certain speculative prices, in: P. Cootner (Ed.), The Random Character of Stock Prices, M.I.T. Press, Cambridge, 1964.

[16] G.F. Miller, P.M. Todd, S.U. Hegde, Designing neural networks using genetic algorithms, in: D.J. Schaffer (Ed.), Third International Conference on Genetic Algorithms, George Mason University, Arlington, VA, 1989 June, pp. 379–384.

[17] D.B. Murray, Forecasting a chaotic time series using an improved metric for embedding space, Physica D 68 (3) (1993) 318–325.

[18] D. Patel, Using genetic algorithms to construct a network for financial prediction, SPIE International Society for Optical Engineering, vol. 2664, 1996, pp. 204 – 213.

[19] E.E. Peters, Chaos and Order in the Capital Markets: A New View of Cycles, Prices and Market Volatility, Wiley, New York, NY, USA, 1991.

[20] W.F. Sharpe, The sharpe ratio, Journal of Portfolio Management 21 (1994) 49–58.

[21] A.J. Sterge, On the distribution of financial futures price changes, Financial Analysts Journal 45 (3) (1989) 74 – 78.

[22] A.S. Weigend, M. Mangeas, Analysis and prediction of multistationary time series, International Conference on Neural Networks in the Capital Markets, 1996, pp. 597 – 611.

[23] A.S. Weigend, S. Shi, Predicting daily probability distributions of S and P500 returns, Journal of Forecasting 19 (2000) 375–392.

[24] D. Whitley, T. Starkweather, C. Bogart, Genetic algorithms and neural networks: optimising connections and connectivity, Parallel Computing 14 (1990) 347 – 361.

[25] P. Zhou, J. Austin, A binary correlation matrix memory k-NN classi<sub>e</sub>r with hardware implementation, British Machine Vision Conference (1998 September) 214–223.

[26] P. Zhou, J. Austin, J. Kennedy, A high performance k-NN classifier using a binary correlation matrix memory, in: M. Kearns, S. Solla, D. Cohn (Eds.), Advances in Neural Information Processing Systems (NIPS 1998), vol. 11, MIT Press, CA, 1999, pp. 713– 722.

![](/api/attachments/FZXYXJAE/fulltext/images/83c92c349c10b160bf4df386e2d0c94507c25b929a2c1b848ab10a8b854963da.jpg)  
Andy Pasley is a PhD student at the University of York, Computer Science Department. His research interests are binary neural networks and time series forecasting, particularly in regard to financial and electricity demand data. Current work focuses on producing full probability distribution forecasts and evaluating their use in risk management.

![](/api/attachments/FZXYXJAE/fulltext/images/27d5016ba8817efc5da3dc79d87e71619e5d4057c730ed0b7fc4eddfb62cb1f9.jpg)  
up to exploit the AURA technology.  
Jim Austin is the Professor of Neural Computation at the University of York, Computer Science Department, where he directs the Advanced Computer Architectures Group. He is best known for his work in binary neural networks through the development of the AURA high performance pattern recognition system. He has over 150 publications in neural networks, computer architectures and computer vision. He is the founder and Director of Cybula set
