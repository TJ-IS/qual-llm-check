---
otero_id: 7540
otero_key: "9BXNP724"
title: "Predicting corporate bankruptcy using a self-organizing map: An empirical study to improve the forecasting horizon of a financial failure model"
authors: "Philippe du Jardin; Eric Séverin"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.04.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Predicting corporate bankruptcy using a self-organizing map: An empirical study to improve the forecasting horizon of a <sup>fi</sup>nancial failure model

Philippe du Jardin <sup>a,</sup>⁎, Eric Séverin <sup>b,1</sup>

<sup>a</sup> Edhec Bussiness School, 393, promenade des Anglais, BP 3116, 06202 Nice Cedex 3, France

<sup>b</sup> Université Lille 1 – USTL, Batiment SHS – N3, BP 179, 59653 Villeneuve d'Ascq Cedex, France

## a r t i c l e i n f o

Article history: Received 15 September 2010 Received in revised form 26 January 2011 Accepted 11 April 2011 Available online 16 April 2011

Keywords: Financial failure prediction Self-organizing map Forecasting horizon

## a b s t r a c t

The aim of this study is to show how a Kohonen map can be used to increase the forecasting horizon of a <sup>fi</sup>nancial failure model. Indeed, most prediction models fail to forecast accurately the occurrence of failure beyond 1 year, and their accuracy tends to fall as the prediction horizon recedes. So we propose a new way of using a Kohonen map to improve model reliability. Our results demonstrate that the generalization error achieved with a Kohonen map remains stable over the period studied, unlike that of other methods, such as discriminant analysis, logistic regression, neural networks and survival analysis, traditionally used for this kind of task.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

A company that fails to ful<sup>fi</sup>ll its obligations, and especially to repay its debts, may then face a critical situation that, in the worst cases, leads to its failure. So the ability to predict the bankruptcy of a <sup>fi</sup>rm is crucial for an investor or a creditor who wishes to ensure that he will be reimbursed on time. It is for this reason that many banks have developed models to assess the risk associated with their loans or their receivables. These models allow them to decide whether to lend money and on what terms, but also to assess the interest rate depending on the anticipated risk of non-reimbursement.

This issue has been studied for many years by academics of many disciplines, and the very <sup>fi</sup>rst statistical models were developed in the late sixties [2]. As there is no general theory of business failure, all these models are empirical [1,33] and are designed mainly using datamining techniques.

Although these models differ greatly, depending on the modeling method, the variables or the samples used [10], they share at least one common characteristic: their forecasting horizon does not usually exceed 1 year. At horizons of more than 1 year, their accuracy falls substantially. Indeed, model accuracy, at horizons of between one and three years, falls by an average of 15%. For example, Altman's [2] model had an accuracy rate of 95% one year before failure and only 48% three years before failure. Altman et al.'s [5] model had an accuracy rate of 97.1% one year before failure and 69.7% three years before failure. With Blum's [14] model, the respective <sup>fi</sup>gures are 95% and 70%, with Brabazon and O'Neill's [16] they are 76.7% and 56.7%, with Dimitras et al.'s [24] 76.3% and 50%, with Moyer's [40] model 84.1% and 68.2%, and, <sup>fi</sup>nally, with Sharma and Mahajan's [49] model they are 91.7% and 73.9%. Regardless of the modeling technique (linear or non-linear, regression or classi<sup>fi</sup>cation), models always have the same drawback: a very short forecasting horizon.

This drawback is especially severe when the forecasting period does not coincide with the terms of the contract between the debtor and the creditor. Indeed, a creditor who accepts that his debt will be repaid over several years, when his debtor's risk has been assessed over a very short time period (usually 1 year), may face a much higher risk beyond the forecasting horizon of the model.

It is for this reason that we have studied a way to improve model accuracy over time. Our work relies on a very interesting result that has not yet been used to design <sup>fi</sup>nancial failure models. Research has shown that failure is a dynamic process [21,22,29,32], which may be analyzed over time, hence that the health of a company assessed at a given time depends heavily on its history. Thus, some <sup>fi</sup>rms can delay the onset of bankruptcy for many years because they have the resources or because they make a strategic commitment that allows them to change their fate, whereas others cannot. Still others may improve their situation, some more swiftly than others, even though their <sup>fi</sup>nancial pro<sup>fi</sup>le, measured at a given time, shows that such an improvement is not possible.

But traditional models rely only on a snapshot of a <sup>fi</sup>rm's <sup>fi</sup>nancial situation measured at time t to predict whether it is likely to fail at time t+1 [50,51]. Because these models assume that a <sup>fi</sup>rm's history has little or no in<sup>fl</sup>uence on its future behavior, they are unlikely to make allowances for a struggling <sup>fi</sup>rm's ability to recover or muddle through. They are also unlikely to take into account the effect of some signs of relative weakness which will result in failure only a few years later. For these reasons, these models have very short forecasting horizons.

Although businesses may well take different paths to bankruptcy, the assumption that including this time dimension might improve model accuracy has led to very little research. Pompe and Bilderbeek [46] have compared the performance of models using <sup>fi</sup>nancial ratios measured over 1 year, with other models using ratios measured over several consecutive years, and have analyzed their performance by forecasting horizons of between one and seven years. Paradoxically, models that incorporate a time dimension do no better than those that do not; indeed, models were not able to stabilize the error with data calculated more than two years before failure.

As a consequence, the aim of this study is to use what some researchers have called the “trajectory of corporate collapse” to examine another way of estimating the changes in <sup>fi</sup>rms' <sup>fi</sup>nancial health. Instead of using <sup>fi</sup>nancial variables measured at different time intervals to forecast failure, as Pompe and Bilderbeek [46] did, we propose to use these variables as a means to design trajectories, then to use these trajectories to make a forecast.

We used a Kohonen map to design these trajectories. First, the map was used to delimit boundaries between areas representing various stages of company <sup>fi</sup>nancial health. Second, we analyzed how companies moved over time within these areas to estimate a typology of behavior we called “trajectories”. Third, we used this typology to forecast <sup>fi</sup>nancial failure at horizons of one, two, and three years.

Finally, we compared the results achieved using the trajectories and results estimated using the most common methods of designing <sup>fi</sup>nancial failure models: discriminant analysis, logistic regression, and neural networks. We also compared the results achieved using the trajectories with those estimated with a survival analysis method. And these comparisons were done at each time horizon.

The remainder of this paper is organized as follows. In Section 2, we present a literature review that explains our research question. In Section 3, we describe the samples and methods used in our experiments. Finally, in Section 4, we present and discuss our results; in Section 5, we summarize our main <sup>fi</sup>ndings.

## 2. Literature review

Most <sup>fi</sup>nancial failure models are single-period models. They are estimated using variables (mostly <sup>fi</sup>nancial ratios) collected at time t, and their accuracy is measured at time t+1. Since Altman's [2] seminal work a large number of models have been designed in such a way. These models have come in for much criticism, mainly from a statistical point of view [10,24]. Problems such as the ways variables or samples are selected, the in<sup>fl</sup>uence of exogenous variables on model accuracy, the assumptions required by some methods, and the ways model accuracy is assessed have been highlighted.

However, the approach to failure at the root of these models is also a legitimate target of criticism. First, models assume that the length of the period during which a <sup>fi</sup>rm has been exposed to a risk of failure has no in<sup>fl</sup>uence on its probability of failure, because they do not take into account the history of the company. So the probability of failure does not depend on the age of the company. However, this assumption does not necessarily hold, as age is a major cause of failure [38,46,53].

Second, models assume that failure is the result of a sudden event, as their forecasting timeframe does not usually exceed 1 year. But companies may show signs of relative weakness many years before they fail [22,32,41]. They may survive in the face of evidence that suggests they might not.

Third, models do not take into account the diversity of paths to terminal failure, some of which can be more chaotic or more gradual than others [6,22,32]. Nevertheless, depending on the trajectory taken by the <sup>fi</sup>rm or on the way a company moves down a given trajectory, its horizon and its probability of failure may change considerably [32].

Because models fail to account for these factors, their forecasting ability is reduced. Indeed, their accuracy will depend heavily on the frequency of each distinctive path in the sample used to estimate them [10,32]. If <sup>fi</sup>rms in the terminal phase of failure are used to design a model, it will perform poorly with <sup>fi</sup>rms in an earlier phase.

The consequence of all these factors is presented in Table 1, which shows the studies devoted to designing <sup>fi</sup>nancial failure prediction systems (failure is usually de<sup>fi</sup>ned from a legal standpoint as liquidation or reorganization), within a timeframe varying from one to three years, and sometimes beyond 3 years. These studies dealt with models designed using data usually taken from the last accounts published before failure, that is, with an average lag of twelve to eighteen months.

Table 1 clearly shows that only very few models achieved stable results over time. Prediction rates are rather good one year before failure, but less so as the horizon recedes to two and three years.

Table 2 shows the same percentages, but classi<sup>fi</sup>ed as healthy or unsound companies. Overall, prediction rates fall, regardless of the company's status. But the larger the size of the sample used in the study, the lower the prediction rates of failed <sup>fi</sup>rms; it seems that, when the sample size is large and selection bias is thus reduced, the future of healthy companies is easier to forecast.

Results of the main studies dealing with <sup>fi</sup>nancial failure prediction at forecasting horizons of between one and three years.

<table><tr><td rowspan="4">Studies</td><td colspan="3">% of correct classification</td><td colspan="3">Sample size</td></tr><tr><td colspan="3">All companies</td><td rowspan="3">Healthy</td><td rowspan="3">Failed</td><td rowspan="3">Total</td></tr><tr><td colspan="3">Years before failure</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>Altman [2]</td><td>95.0%</td><td>72.0%</td><td>48.0%</td><td>33</td><td>33</td><td>66</td></tr><tr><td>Altman et al. [5]</td><td>97.1%</td><td>88.2%</td><td>69.7%</td><td></td><td>34</td><td>34</td></tr><tr><td>Altman et al. [3]</td><td>91.0%</td><td>89.0%</td><td>84.0%</td><td>53</td><td>58</td><td>111</td></tr><tr><td>Altman et al. [4]</td><td>93.2%</td><td></td><td>91.1%</td><td>404</td><td>404</td><td>808</td></tr><tr><td>Atiya [7]</td><td>74.6%</td><td>66.7%</td><td></td><td>716</td><td>444</td><td>1160</td></tr><tr><td>Aziz et al. [8]</td><td>91.8%</td><td>84.7%</td><td>78.6%</td><td>39</td><td>39</td><td>78</td></tr><tr><td>Back et al. [9]</td><td>97.3%</td><td>73.0%</td><td>83.5%</td><td>37</td><td>37</td><td>74</td></tr><tr><td>Barniv and Hershbarger [11]</td><td>89.3%</td><td>87.7%</td><td></td><td>77</td><td>70</td><td>147</td></tr><tr><td>Barniv and McDonald [12]</td><td>83.7%</td><td>80.0%</td><td>71.9%</td><td>153</td><td>141</td><td>294</td></tr><tr><td>Betts and Belhoul [13]</td><td>90.1%</td><td>72.4%</td><td>64.7%</td><td>39</td><td>93</td><td>132</td></tr><tr><td>Blum [14]</td><td>95.0%</td><td>80.0%</td><td>70.0%</td><td>115</td><td>115</td><td>230</td></tr><tr><td>Brabazon and Keenan [15]</td><td>80.7%</td><td>72.0%</td><td>66.0%</td><td>89</td><td>89</td><td>178</td></tr><tr><td>Brabazon and O&#x27;Neill [16]</td><td>76.7%</td><td>73.3%</td><td>56.7%</td><td>89</td><td>89</td><td>178</td></tr><tr><td>Charitou et al. [17]</td><td>83.3%</td><td>76.2%</td><td>75.0%</td><td>51</td><td>51</td><td>102</td></tr><tr><td>Coats and Fant [18]</td><td>92.9%</td><td>86.2%</td><td>81.9%</td><td>188</td><td>94</td><td>282</td></tr><tr><td>Dambolena and Khoury [23]</td><td>91.2%</td><td>84.8%</td><td>82.6%</td><td>23</td><td>23</td><td>46</td></tr><tr><td>Dimitras et al. [24]</td><td>76.3%</td><td>60.5%</td><td>50.0%</td><td>40</td><td>40</td><td>80</td></tr><tr><td>Doumpos and Zopounidis [25]</td><td>71.1%</td><td>60.5%</td><td>57.9%</td><td>59</td><td>59</td><td>118</td></tr><tr><td>Gombola et al. [28]</td><td>89.0%</td><td>86.0%</td><td>72.0%</td><td>244</td><td>77</td><td>321</td></tr><tr><td>Kotsiantis et al. [30]</td><td>71.8%</td><td>71.1%</td><td>68.8%</td><td>100</td><td>50</td><td>150</td></tr><tr><td>Lacher et al. [31]</td><td>94.7%</td><td>89.4%</td><td>84.1%</td><td>188</td><td>94</td><td>282</td></tr><tr><td>Laitinen and Laitinen [34]</td><td>86.6%</td><td>68.3%</td><td></td><td>41</td><td>41</td><td>82</td></tr><tr><td>Laitinen and Laitinen [35]</td><td>74.7%</td><td>65.3%</td><td></td><td>85</td><td>85</td><td>170</td></tr><tr><td>Laitinen and Kankaanpaa [33]</td><td>86.9%</td><td>65.8%</td><td>71.1%</td><td>38</td><td>38</td><td>76</td></tr><tr><td>Lau [36]</td><td>80.0%</td><td>79.0%</td><td>85.0%</td><td>700</td><td>100</td><td>800</td></tr><tr><td>Lee et al. [37]</td><td></td><td>78.6%</td><td>76.2%</td><td>84</td><td>84</td><td>168</td></tr><tr><td>Moyer [40]</td><td>84.1%</td><td>79.6%</td><td>68.2%</td><td>22</td><td>20</td><td>42</td></tr><tr><td>Nam and Jinn [41]</td><td>84.4%</td><td>76.1%</td><td>76.1%</td><td>46</td><td>46</td><td>92</td></tr><tr><td>Piramuthu et al. [45]</td><td>89.1%</td><td>87.0%</td><td></td><td>91</td><td>91</td><td>182</td></tr><tr><td>Pompe and Bilderbeek [46]</td><td>80.0%</td><td>70.0%</td><td>68.0%</td><td>1800</td><td>1800</td><td>3600</td></tr><tr><td>Sharma and Mahajan [49]</td><td>91.7%</td><td>78.3%</td><td>73.9%</td><td>23</td><td>23</td><td>46</td></tr><tr><td>Tam and Kiang [52]</td><td>85.2%</td><td>88.8%</td><td></td><td>81</td><td>81</td><td>162</td></tr><tr><td>Yim and Mitchell [55]</td><td>92.0%</td><td>90.0%</td><td></td><td>80</td><td>20</td><td>100</td></tr><tr><td>Zurada et al. [56]</td><td>81.6%</td><td>76.6%</td><td>68.1%</td><td>253</td><td>92</td><td>345</td></tr></table>

Figures presented in this table correspond to the best results when many results were computed.  
Empty cells correspond to results that were not mentioned.

Results of the main studies dealing with <sup>fi</sup>nancial failure prediction at forecasting horizons of between one to three years according to <sup>fi</sup>rm status (healthy vs. unsound)

<table><tr><td rowspan="4">Studies</td><td colspan="6">% of correct classification</td><td rowspan="4">Sample size total</td></tr><tr><td colspan="3">Healthy companies</td><td colspan="3">Failed companies</td></tr><tr><td colspan="3">Years before failure</td><td colspan="3">Years before failure</td></tr><tr><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td></tr><tr><td>Altman [2]</td><td></td><td></td><td></td><td></td><td></td><td></td><td>66</td></tr><tr><td>Altman et al. [5]</td><td></td><td></td><td></td><td>97.1%</td><td>88.2%</td><td>69.7%</td><td>34</td></tr><tr><td>Altman et al. [3]</td><td></td><td></td><td></td><td></td><td></td><td></td><td>111</td></tr><tr><td>Altman et al. [4]</td><td>92.8%</td><td></td><td>90.3%</td><td>96.5%</td><td></td><td>86.4%</td><td>808</td></tr><tr><td>Atiya [7]</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1160</td></tr><tr><td>Aziz et al. [8]</td><td>98.0%</td><td>83.7%</td><td>77.6%</td><td>85.7%</td><td>85.7%</td><td>79.6%</td><td>78</td></tr><tr><td>Back et al. [9]</td><td>100.0%</td><td>2.22%</td><td>72.2%</td><td>94.7%</td><td>73.7%</td><td>94.7%</td><td>74</td></tr><tr><td>Barniv and Hershbarger [11]</td><td>89.3%</td><td>85.7%</td><td></td><td>89.3%</td><td>89.3%</td><td></td><td>147</td></tr><tr><td>Barniv and McDonald [12]</td><td>87.1%</td><td>84.2%</td><td>81.2%</td><td>80.0%</td><td>75.4%</td><td>61.1%</td><td>294</td></tr><tr><td>Betts and Belhoul [13]</td><td></td><td></td><td></td><td></td><td></td><td></td><td>132</td></tr><tr><td>Blum [14]</td><td></td><td></td><td></td><td></td><td></td><td></td><td>230</td></tr><tr><td>Brabazon and Keenan [15]</td><td>78.7%</td><td>69.33%</td><td>66.7%</td><td>82.7%</td><td>74.7%</td><td>65.3%</td><td>178</td></tr><tr><td>Brabazon and O&#x27;Neill [16]</td><td></td><td></td><td></td><td></td><td></td><td></td><td>178</td></tr><tr><td>Charitou et al. [17]</td><td>76.2%</td><td>76.19%</td><td>68.2%</td><td>90.5%</td><td>76.2%</td><td>81.8%</td><td>102</td></tr><tr><td>Coats and Fant [18]</td><td>97.9%</td><td>83.0%</td><td>83.0%</td><td>83.0%</td><td>89.4%</td><td>80.9%</td><td>282</td></tr><tr><td>Dambolena and Khoury [23]</td><td>100.0%</td><td>87.0%</td><td>87.0%</td><td>83.0%</td><td>83.0%</td><td>78.0%</td><td>46</td></tr><tr><td>Dimitras et al. [24]</td><td>57.9%</td><td>42.1%</td><td>57.9%</td><td>94.7%</td><td>78.9%</td><td>42.1%</td><td>80</td></tr><tr><td>Doumpos and Zopounidis [25]</td><td>63.2%</td><td>57.9%</td><td>63.2%</td><td>79.0%</td><td>63.2%</td><td>52.6%</td><td>118</td></tr><tr><td>Gombola et al. [28]</td><td></td><td></td><td></td><td></td><td></td><td></td><td>321</td></tr><tr><td>Kotsiantis et al. [30]</td><td></td><td></td><td></td><td></td><td></td><td></td><td>150</td></tr><tr><td>Lacher et al. [31]</td><td>97.9%</td><td>87.2%</td><td>78.7%</td><td>91.5%</td><td>91.5%</td><td>89.4%</td><td>282</td></tr><tr><td>Laitinen and Laitinen [34]</td><td>85.4%</td><td>61.7%</td><td></td><td>87.8%</td><td>65.9%</td><td></td><td>82</td></tr><tr><td>Laitinen and Laitinen [35]</td><td>75.3%</td><td>69.4%</td><td></td><td>74.1%</td><td>61.2%</td><td></td><td>170</td></tr><tr><td>Laitinen and Kankaanpaa [33]</td><td>89.5%</td><td>73.7%</td><td>84.2%</td><td>84.2%</td><td>57.9%</td><td>57.9%</td><td>76</td></tr><tr><td>Lau [36]</td><td></td><td></td><td></td><td></td><td></td><td></td><td>800</td></tr><tr><td>Lee et al. [37]</td><td></td><td>66.7%</td><td>71.4%</td><td></td><td>90.5%</td><td>1.0%</td><td>168</td></tr><tr><td>Moyer [40]</td><td>82.0%</td><td>86.0%</td><td>73.0%</td><td>95.0%</td><td>80.0%</td><td>70.0%</td><td>42</td></tr><tr><td>Nam and Jinn [41]</td><td></td><td></td><td></td><td></td><td></td><td></td><td>92</td></tr><tr><td>Piramuthu et al. [45]</td><td>92.7%</td><td>93.0%</td><td></td><td>85.4%</td><td>81.0%</td><td></td><td>182</td></tr><tr><td>Pompe and Bilderbeek [46]</td><td></td><td></td><td></td><td></td><td></td><td></td><td>3600</td></tr><tr><td>Sharma and Mahajan [49]</td><td></td><td></td><td></td><td></td><td></td><td></td><td>46</td></tr><tr><td>Tam and Kiang [52]</td><td>88.6%</td><td>80.0%</td><td></td><td>81.8%</td><td>97.5%</td><td></td><td>162</td></tr><tr><td>Yim and Mitchell [55]</td><td></td><td></td><td></td><td></td><td></td><td></td><td>100</td></tr><tr><td>Zurada et al. [56]</td><td>82.5%</td><td>80.6%</td><td>68.0%</td><td>79.0%</td><td>65.8%</td><td>68.4%</td><td>345</td></tr></table>

Figures presented in this table correspond to the best results when many results were computed.  
Empty cells correspond to results that were not mentioned.

Some authors have mentioned that incorporating a time dimension into a model is an ef<sup>fi</sup>cient way to improve its accuracy. Edmister [27] speculated that measures of variation over several years of <sup>fi</sup>nancial ratios might be relevant variables to predict corporate failure. To test this hypothesis, he <sup>fi</sup>rst selected a set of nineteen ratios and added to this set a three-year trend (measured using up- and down-trend dummies) and a three-year average of each ratio. He then used an automatic search procedure to select the best of the variables and found that the measures representing variation of ratios were among the best predictors. Unfortunately, as he did not compare the results achieved with a model that includes measures of variation and those of another that might have been estimated without such variables, his research does not demonstrate whether data measured over time improve model accuracy. This hypothesis was <sup>fi</sup>nally examined by Dambolena and Khoury [23], as well as by Betts and Belhoul [13]. Both studies show that a model using variation of ratios calculated over time performed better than a model including only single-year ratios, up to <sup>fi</sup>ve years before failure. However, this improvement is not suf<sup>fi</sup>cient to stabilize model accuracy over time. In fact, the correct prediction rates calculated one year before failure are far better than those calculated between three and <sup>fi</sup>ve years before failure (see Table 1). Pompe and Bilderbeek [46] also examined this issue but used <sup>fi</sup>nancial ratios alone. They too failed to obtain stable results over time.

There is a consensus, then, that considering the nature of failure and its historical dimension will increase the reliability of the model. However, for the moment research has failed to stabilize model accuracy over time. For this reason, we have decided to study this issue, though not in the same way as previous research. Instead of using <sup>fi</sup>nancial indicators measured over several years to design a model, we chose to build a typology of failure paths and to use these paths as a prediction model. Our research builds on that of Laitinen [32], who considered that the performance of a model depends on its ability to represent the trajectories companies are likely to take in the real world. Kohonen maps were used to estimate trajectories, and their performance was then compared to that of traditional models at horizons of one, two, and three years.

## 3. Samples and methods

## 3.1. Sample selection

Data used in this study were selected from the French database Diane, which provides <sup>fi</sup>nancial data on more than one million French companies. We chose only companies required by law to <sup>fi</sup>le their annual reports with the French commercial courts. And to control for size and sector effects, we selected large samples made up of companies of the same size (assets of less than €750,000) and in the same activity (retail). We collected three samples of companies; no company appeared in more than one sample. The <sup>fi</sup>rst sample was used to select variables that were used to design models. The second (a learning sample) was used to estimate the parameters of the models and the third (a test sample) to estimate their generalization error, i.e., their true error. These samples are made up of income statement and balance sheet data, which have been the main sources of information for failure models since Altman [2]. We used these data to calculate a set of <sup>fi</sup>nancial ratios and one <sup>fi</sup>nancial variable (shareholder funds) measured over two consecutive years.

The <sup>fi</sup>rst sample is made up of 250 sound and 250 unsound <sup>fi</sup>rms, and we chose data published in 2002 (with one variable, shareholder funds, from 2001). Failed companies were liquidated or reorganized in 2003, and healthy companies were still in operation in 2005. These <sup>fi</sup>rms were chosen at random from among those in the database when they complied with the criteria described above.

The second sample (learning sample) is made up of 740 sound and 740 unsound <sup>fi</sup>rms, and data were published between 1996 and 2002. We collected data from seven consecutive years to calculate variables over a six-year period (the variation of shareholder funds is measured over two consecutive years). Healthy companies were selected at random from among those still in operation in 2003; likewise, failed companies were selected at random from among those liquidated or reorganized in 2003.

The third sample (test sample) is made up of 440 healthy and 440 failed companies. To compute the same variables as those calculated with the second sample, but over an eight-year period, we collected data published between 1995 and 2003. Healthy and failed companies were selected at random from among those that were still active in 2004 and from those that were liquidated or reorganized by court decision in 2004.

## 3.2. Variable selection

The <sup>fi</sup>rst sample (250 sound and 250 unsound <sup>fi</sup>rms) was used to select variables. We <sup>fi</sup>rst chose forty-one variables (forty ratios and one measure of variation of a balance sheet statement) from among those commonly used in the failure prediction literature. To select the <sup>fi</sup>nal set of variables, and to ensure that these variables were as sample- and selection-technique-independent as possible, we used six selection methods and <sup>fi</sup>nally chose the variables selected at least twice. We used the same sample, the same variables, and the same selection techniques as those used in du Jardin [26].

## 3.3. Model development

We selected two types of methods to design models. First, with a procedure presented below, we used a Kohonen map to design trajectories of failure. Second, we chose three of the most commonly used modeling techniques in the <sup>fi</sup>nancial literature [10]: discriminant analysis, often used as a benchmark of the forecast skill of other models since Altman's [2] research; logistic regression, <sup>fi</sup>rst introduced as a way to design bankruptcy models by Ohlson [43]; a neural network, and especially a multilayer perceptron, whose usefulness in <sup>fi</sup>rm failure prediction was popularized by Odom and Sharda [42], (this method makes it possible to overcome the shortcomings of such parametric methods as discriminant analysis and to account for any non-linearity between a probability of failure and a set of <sup>fi</sup>nancial ratios [35]). We also chose a fourth modeling technique (survival analysis) as a special benchmark of our trajectories. The three aforementioned methods, unlike the trajectories, rely not on data that measure changes to a <sup>fi</sup>rm's <sup>fi</sup>nancial health over several consecutive years but on a snapshot of a company's <sup>fi</sup>nancial pro<sup>fi</sup>le taken at a particular point in time. To assess the performance of trajectories, and to control for the in<sup>fl</sup>uence of this difference between data used with each method (single period data vs. time-series data), we selected a survival analysis method, Cox's proportional hazard model [20]. We chose this technique because it has proven reliable in the <sup>fi</sup>eld of bankruptcy prediction [33,50,54].

## 3.3.1. Kohonen map

Serrano-Cinca [48] demonstrated that a Kohonen map might be used to delimit and visualize “failing and non-failing regions”. Indeed, a Kohonen map is the result of a process in which a high-dimensional input space is mapped onto a two-dimensional map. This author has shown that the resulting quantization of data that characterized sound and unsound <sup>fi</sup>rms, made it possible to show different zones on the map, each of these zones accounting for a particular <sup>fi</sup>nancial pro<sup>fi</sup>le. Some regions, for example, correspond to very pro<sup>fi</sup>table, healthy companies, others to very unsound companies, still others to <sup>fi</sup>rms in intermediate <sup>fi</sup>nancial situations.

As a consequence, a Kohonen map may be used to delimit boundaries between regions at risk of failure and other regions at low risk or without any risk; each region accounts for a given <sup>fi</sup>nancial pro<sup>fi</sup>le associated with a probability of failure. If one considers a trajectory a change in the <sup>fi</sup>nancial situation of a company over time, then one may use a Kohonen map to design it: a trajectory shows the way companies move on the map, in regions at risk, over several consecutive years. A trajectory is then a sequence of positions on the map over a given period.

To design these trajectories, we used data from the learning sample (740 sound and 740 unsound <sup>fi</sup>rms) and a Kohonen map made up of 100 neurons, 10 per row and 10 per column. The number of neurons we chose is somewhat arbitrary as there are no theoretical guidelines for the size of the map. We used 100 units because it is a common practice [19]. We also used Sammon's mapping method [47] to examine the topology of the data and to determine the form of the map (i.e., the number of rows and columns). This map provides a general overview of the shape of the data and makes it possible to determine whether we may use a rectangular or a square map. We chose a square map as there was no evidence that a rectangular one was better.

We used a two-step procedure to design company trajectories.

First, we used data from 2002 to calculate a map. The algorithm used during the learning phase of the map can be described as follows:

1. Initialize the weights of the neurons and set the value of the initial learning parameters; all neurons have the same dimension as the vector of data that characterized each company.

2. Repeat step 3 to step 7 until a stopping criterion is reached.

3. For each vector x representing data belonging to one company, compute the distance (usually the Euclidean one):

4. For each neuron j:

$$
D (j) = d \left(x, w _ {j}\right)
$$

where w<sub>j</sub> is the weight vector of neuron j.

5. Find neuron $w _ { i }$ that is the closest to x according to the distance de<sup>fi</sup>ned in 4.

6. Update the weights of the neurons that lie within the neighborhood of neuron w found in 5:

$$
w _ {j} (t) = w _ {j} (t - 1) + \alpha^ {*} h _ {i j} ^ {*} \left(x - w _ {j} (t - 1)\right)
$$

where t is time, α the learning step, h the neighborhood function, and x the input vector. The neighborhood function is traditionally a decreasing function of both time and the distance between any neuron w on the map and neuron w that is the closest to the input vector at time t.

7. Adjust learning parameters.

At the end of the learning process, the resulting map depicts an ordered, abstract space of the variable space. Indeed, each neuron, the weights of which were updated during the learning process so as to get closer to the input vectors that were close to them, represents a particular company <sup>fi</sup>nancial pro<sup>fi</sup>le. Moreover, thanks to the neighborhood function, the topology of the input space is preserved: all companies that are close to each other in the variable space are also close on the map.

Table 3 Table 3  
Variables used to design models.

<table><tr><td>Variables</td><td>Description</td></tr><tr><td>SF/TA</td><td>Shareholder funds/Total assets</td></tr><tr><td>TD/SF</td><td>Total debt/Shareholder funds</td></tr><tr><td>CMS/TA</td><td>(Cash + Marketable securities)/Total assets</td></tr><tr><td>C/CL</td><td>Cash/Current liabilities</td></tr><tr><td>C/TD</td><td>Cash/Total debt</td></tr><tr><td>EBITDA/TA</td><td>EBITDA/Total assets</td></tr><tr><td>EBIT/TA</td><td>EBIT/Total assets</td></tr><tr><td>CSE</td><td>Change in shareholders&#x27; equity</td></tr><tr><td>C/TS</td><td>Cash/Total sales</td></tr><tr><td>EBIT/TS</td><td>EBIT/Total sales</td></tr></table>

Once the learning phase was completed, we looked for neurons that can be considered prototypes of failed and non-failed companies. For this, we compared data from the learning sample and all neurons one more time, then we calculated the percentage of healthy and failed companies that were the closest to each neuron. Finally, neurons were given the label of the class (healthy or failed) whose percentage was higher. If the percentages were equal, neurons were assigned to the class to which the majority of its nearest neighbors belong. Once neurons are labeled, the map makes it possible to visualize two regions – a failure region and a non-failure one – and their boundaries.

Second, we computed company trajectories, that is, the positions of companies on the map over the six-year period for which we gathered data. The length of this period is the same as that used by Laitinen [32]. To calculate the different positions of a company on the map, we compared its vector of data to all neurons, for a given year, and we looked for the closest neuron. These neurons represent the six positions of a company on the map over the period analyzed here. A trajectory is then a sequence of six positions.

However, since the map is made of a huge number of units, the number of combinations of neurons is also huge and it makes it impossible to analyze all possible trajectories. For this reason, we used a classi<sup>fi</sup>cation method to reduce the number of possible positions and to group the 100 neurons into a small number of groups called superclasses. Because of the self-organizing nature of the Kohonen algorithm, such a clustering ensures that the resulting super-classes are made of contiguous neurons [19] and that these super-classes are fairly distinct and easily analyzable.

We used a clustering method (hierarchical ascending classi<sup>fi</sup>cation) to group all neurons and we assessed the quality of a few partitions made up of six to eleven super-classes. The clustering was done using three different aggregation criteria (average linkage, complete linkage, and Ward criterion) to avoid criterion-dependant classi<sup>fi</sup>cation. Within each partition, neurons were assigned the label of the class selected by at least two criteria. When all criteria led to different results, neurons were labeled with the class to which the majority of their nearest neighbors belong (there were no ties).

Once the super-classes were designed within all partitions, we looked for the best one, that is, the partition whose classes are as homogenous as possible. We used the three best indexes mentioned in the research done by Milligan [39], and we selected the best partition according to these measures.

We then ranked the super-classes on the <sup>fi</sup>nancial health of the companies they represent, ranging from companies in bad shape to those in good shape. This ranking enabled us to estimate a set of prototype trajectories according to <sup>fi</sup>rm position on the map over the <sup>fi</sup>rst year of the period covered by our study (1997). We <sup>fi</sup>rst calculated trajectories of companies whose initial position on the map in 1997 was super-class 1, then trajectories of companies whose initial position was super-class 2, and so on. There are as many sets of trajectories as super-classes.

Each set of trajectories was designed using a one-dimensional, sixneuron Kohonen map. This <sup>fi</sup>gure was assessed after several trials, and it corresponds to an optimal solution: with more than six neurons, some trajectories were replicated several times; with fewer, some no longer existed.

We then calculated the percentage of healthy and failed <sup>fi</sup>rms whose trajectories were the closest to each of all prototype trajectories. And we labeled each prototype trajectory with the class (sound or unsound) whose percentage was higher.

Finally, we grouped all six-neuron maps into a <sup>fi</sup>nal set, and we used it to complete the forecast.

## 3.3.2. Methods used as benchmark

With data from the learning sample and the year 2002, we estimated three models using methods commonly found in the bankruptcy literature: one with discriminant analysis, one with logistic regression, and a <sup>fi</sup>nal one with a neural network called multilayer perceptron. We also estimated one model with Cox's proportional hazard method, and with data from the learning sample, but the model was designed with data from the period from 2002 to 1997.

Network parameters were set up with data from 2002 using a tenfold cross validation. We used a steepest descent, as an optimization technique during the learning process, because this technique has been widely used to design failure models since Odom and Sharda [42], and a hyperbolic tangent as a neuron activation function. We used a network with only one hidden layer, but we tested several combinations of parameters: learning steps, momentum terms, weight decays, numbers of hidden nodes, and numbers of iterations of the learning process. Finally, the architecture that led to the lowest error was selected for our experiments.

## Table 4

Characteristics of variables.

<table><tr><td rowspan="3">Variables</td><td colspan="6">Percentiles</td><td colspan="2">S-W</td><td rowspan="3">t</td><td rowspan="3">U</td></tr><tr><td colspan="3">Healthy companies</td><td colspan="3">Failed companies</td><td rowspan="2">Healthy</td><td rowspan="2">Failed</td></tr><tr><td>25%</td><td>50%</td><td>75%</td><td>25%</td><td>50%</td><td>75%</td></tr><tr><td>SF/TA</td><td>0.14</td><td>0.33</td><td>0.55</td><td>-0.47</td><td>-0.05</td><td>0.23</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>TD/SF</td><td>-0.02</td><td>0.00</td><td>0.05</td><td>-0.14</td><td>-0.02</td><td>0.07</td><td>0.0000</td><td>0.0000</td><td>0.0830</td><td>0.0000</td></tr><tr><td>CMS/TA</td><td>-0.60</td><td>0.03</td><td>0.84</td><td>-0.81</td><td>-0.66</td><td>-0.17</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>C/CL</td><td>-0.23</td><td>-0.05</td><td>0.25</td><td>-0.33</td><td>-0.26</td><td>-0.15</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>C/TD</td><td>-0.24</td><td>-0.04</td><td>0.29</td><td>-0.36</td><td>-0.27</td><td>-0.16</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>EBITDA/TA</td><td>0.09</td><td>0.21</td><td>0.37</td><td>-0.38</td><td>-0.07</td><td>0.13</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>EBIT/TA</td><td>0.12</td><td>0.20</td><td>0.30</td><td>-0.31</td><td>-0.02</td><td>0.14</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>CSE</td><td>-0.16</td><td>0.11</td><td>0.11</td><td>0.11</td><td>0.11</td><td>0.11</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>C/TS</td><td>-0.13</td><td>0.01</td><td>0.21</td><td>-0.28</td><td>-0.15</td><td>-0.03</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>EBIT/TS</td><td>0.18</td><td>0.30</td><td>0.51</td><td>-0.66</td><td>-0.03</td><td>0.25</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr></table>

Figures were calculated with the learning sample and data from 2002.  
S–W, p-value of a Shapiro–Wilks normality test  
t, p-value of a Student t test for differences between the means of the two groups.  
U, p-value of a Mann–Whitney test for the equality of the sum of ranks of each group.

Table 5 Correlation matrix.

<table><tr><td>Variables</td><td>SF/TA</td><td>TD/SF</td><td>CMS/TA</td><td>C/CL</td><td>C/TD</td><td>EBITDA/TA</td><td>EBIT/TA</td><td>CSE</td><td>C/TS</td></tr><tr><td>TD/SF</td><td>0.030</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CMS/TA</td><td>0.148</td><td>-0.011</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>C/CL</td><td>0.172</td><td>-0.002</td><td>0.553</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>C/TD</td><td>0.204</td><td>-0.006</td><td>0.590</td><td>0.833</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EBITDA/TA</td><td>0.504</td><td>0.013</td><td>0.097</td><td>0.125</td><td>0.081</td><td></td><td></td><td></td><td></td></tr><tr><td>EBIT/TA</td><td>0.606</td><td>0.008</td><td>0.034</td><td>0.066</td><td>0.075</td><td>0.715</td><td></td><td></td><td></td></tr><tr><td>CSE</td><td>-0.071</td><td>-0.004</td><td>-0.108</td><td>-0.055</td><td>-0.066</td><td>-0.102</td><td>-0.093</td><td></td><td></td></tr><tr><td>C/TS</td><td>0.102</td><td>-0.009</td><td>0.392</td><td>0.557</td><td>0.352</td><td>0.053</td><td>0.044</td><td>-0.036</td><td></td></tr><tr><td>EBIT/TS</td><td>0.520</td><td>0.009</td><td>0.188</td><td>0.180</td><td>0.162</td><td>0.462</td><td>0.473</td><td>-0.196</td><td>0.016</td></tr></table>

## 3.4. Evaluation of model performance

Models designed with discriminant analysis, logistic regression, neural networks, and Cox's method were used with data from the test sample (440 failed and 440 non-failed <sup>fi</sup>rms) to estimate their generalization ability.

With the three aforementioned methods, forecasts up to one year ahead were achieved with data from 2003, and compared with company status (failed or non-failed) in 2004. Forecasts up to two years ahead were then estimated with data from 2002, and forecasts up to three years ahead, with data from 2001, and the results were compared to company status in 2004. With Cox's model, forecasts up to one year ahead were achieved with data from 2003 to 1998, forecasts up to two years ahead with data from 2002 to 1997, and <sup>fi</sup>nally forecasts up to three ahead were achieved with data from 2001 to 1996, and the results were also compared to company status in 2004.

As far as the trajectories are concerned, we <sup>fi</sup>rst calculated the positions of companies on the map over the eight-year period for which we collected data, using the test sample. Then, for each period of six consecutive years (2003–1998, 2002–1997, 2001–1996), we calculated trajectories. As a consequence, we got three trajectories per company: the <sup>fi</sup>rst corresponds to the evolution of its <sup>fi</sup>nancial situation over the period that ends 1 year before the date on which its status was assessed; the second corresponds to the same evolution but over a period that ends 2 years before the date on which its status was assessed. It is the same for the third one, but with an additional year.

Forecasting was done by comparing all company trajectories with the set of prototype trajectories using a Euclidian distance, and this was done for the three periods. A company was classi<sup>fi</sup>ed as healthy (or failed) over a given period, if the prototype trajectory that was the closest to its own trajectory was labeled as healthy (or failed).

## 4. Results and discussion

## 4.1. Variables used to design models

The <sup>fi</sup>rst sample (250 sound and 250 unsound <sup>fi</sup>rms) was used to select the variables. Their characteristics are presented in Tables 3 and 4. Figures in Table 4 were calculated with data from the learning sample and year 2002, with zero mean and unit variance. The quartiles of each variable show the discrepancy of the deviations in and between the two groups of <sup>fi</sup>rms. Table 4 also indicates the p-values of a Shapiro–Wilks normality test and the p-values of two tests for differences between the means of each variable within each group. As the Shapiro–Wilks test shows that none of the variables are normally distributed, the Mann– WhitneyU test is more reliable than Student t test. This test underscores that all variables present signi<sup>fi</sup>cant differences between the two groups.

Table 5 shows the correlation matrix and points out that several variables are highly correlated, as is often the case with <sup>fi</sup>nancial ratios. These <sup>fi</sup>gures show that some of the assumptions on which discriminant analysis relies are not met. As none of the variables are normally distributed, the joint distribution cannot be multi-normal and some correlations are so high they certainly affect the estimation of discriminant function coef<sup>fi</sup>cients. However, we have still chosen to use this method as a benchmark method, as Alfaro et al. [1] did, because discriminant analysis is certainly the most widely used means of designing <sup>fi</sup>nancial failure prediction models.

![](/api/attachments/9BXNP724/fulltext/images/857ad5fde8ef7117f06153c94519e250faa30d929be1e9fce695273f588e5e6b.jpg)  
Fig. 1. Distribution of neurons on the Kohonen map. Neurons in light gray represent healthy companies, those in dark gray, failed companies. Figures are the proportion of healthy or failed companies used to assign each neuron a label.

Table 6  
Rank of the partitions by homogeneity indexes.

<table><tr><td rowspan="2">Number of super-classes</td><td rowspan="2">Point biserial correlation</td><td rowspan="2">C-index – Hubert and Levin</td><td rowspan="2">Gamma – Baker and Hubert</td><td>Point biserial correlation</td><td>C-index – Hubert and Levin</td><td>Gamma – Baker and Hubert</td></tr><tr><td>Ranking</td><td>Ranking</td><td>Ranking</td></tr><tr><td>4-2</td><td>0.480</td><td>0.122</td><td>-0.172</td><td>1</td><td>6</td><td>2</td></tr><tr><td>5-2</td><td>0.478</td><td>0.116</td><td>-0.184</td><td>2</td><td>4</td><td>3</td></tr><tr><td>4-3</td><td>0.467</td><td>0.116</td><td>-0.367</td><td>3</td><td>3</td><td>4</td></tr><tr><td>5-3</td><td>0.466</td><td>0.109</td><td>-0.368</td><td>4</td><td>1</td><td>5</td></tr><tr><td>5-4</td><td>0.433</td><td>0.131</td><td>-0.037</td><td>5</td><td>8</td><td>1</td></tr><tr><td>6-2</td><td>0.428</td><td>0.133</td><td>-0.376</td><td>6</td><td>9</td><td>6</td></tr><tr><td>6-4</td><td>0.418</td><td>0.117</td><td>-0.377</td><td>7</td><td>5</td><td>9</td></tr><tr><td>6-3</td><td>0.417</td><td>0.123</td><td>-0.377</td><td>7</td><td>7</td><td>8</td></tr><tr><td>6-5</td><td>0.414</td><td>0.114</td><td>-0.377</td><td>8</td><td>2</td><td>7</td></tr></table>

## 4.2. Kohonen map, super-classes and trajectories

Fig. 1 shows the Kohonen map achieved at the end of the learning process. This map shows to distinct areas: one representing sound companies (part of the map in light gray), coded using sixty-seven neurons, and the other, more compact (in dark gray), representing unsound <sup>fi</sup>rms, and coded using only thirty-three neurons.

The distribution of neurons within each group of companies shows that healthy <sup>fi</sup>rms have a wider range of <sup>fi</sup>nancial pro<sup>fi</sup>les than failed ones. To design the super-classes we took into account this difference. Indeed, if the quantization of healthy <sup>fi</sup>rms requires twice as many neurons as the quantization of unhealthy <sup>fi</sup>rms, we may suppose that a good clustering of neurons should highlight such a difference. As we were seeking a relatively small number of super-classes (between six and eleven), we analyzed several partitions made up of four to six super-classes encoding healthy companies, and of two to <sup>fi</sup>ve encoding failed ones.

The best partition assessed using three indexes of homogeneity [39], as shown in Table 6, is made up of four super-classes representing healthy companies, and two representing failed <sup>fi</sup>rms.

Within each super-class, we calculated the means of all variables to rank the super-classes by <sup>fi</sup>nancial health. These statistics, calculated with data with 0 mean and unit variance, are shown in Table 7.

Table 7 shows that super-class 1 is made up of very healthy, pro<sup>fi</sup>table, and liquid companies, as opposed to super-class 6, which is made up of unsound <sup>fi</sup>rms with the lowest pro<sup>fi</sup>tability and solvency. This table also indicates the p-values of a Kruskal–Wallis test and underscores that all variables present signi<sup>fi</sup>cant differences between the six super-classes.

Fig. 2 shows the Kohonen map depicted in Fig. 1 as well as the six super-classes within the map. Companies located in the lower left part of the map are the strongest, whereas those in the upper right part are those which face huge <sup>fi</sup>nancial constraints and which are in very bad shape. Companies located in the lower right part are also in bad shape, with a low pro<sup>fi</sup>tability but are rather liquid.

Characteristics of the variables within each super-class calculated with data from 2002

<table><tr><td rowspan="4">Variables</td><td colspan="6">Means</td><td rowspan="4">H</td></tr><tr><td colspan="4">Healthy</td><td colspan="2">Failed</td></tr><tr><td colspan="4">Super-classes 1–4</td><td colspan="2">Super-classes 5–6</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>SF/TA</td><td>0.46</td><td>0.29</td><td>0.36</td><td>0.06</td><td>-0.48</td><td>-0.39</td><td>0.00000</td></tr><tr><td>TD/SF</td><td>0.00</td><td>0.00</td><td>0.05</td><td>0.08</td><td>0.04</td><td>-0.08</td><td>0.00000</td></tr><tr><td>CMS/TA</td><td>1.11</td><td>-0.38</td><td>0.21</td><td>-0.73</td><td>0.21</td><td>-0.73</td><td>0.00000</td></tr><tr><td>C/CL</td><td>0.59</td><td>-0.16</td><td>0.21</td><td>-0.38</td><td>-0.09</td><td>-0.33</td><td>0.00000</td></tr><tr><td>C/TD</td><td>0.58</td><td>-0.16</td><td>0.30</td><td>-0.42</td><td>-0.05</td><td>-0.36</td><td>0.00000</td></tr><tr><td>EBITDA/TA</td><td>0.41</td><td>0.37</td><td>0.08</td><td>0.26</td><td>-0.56</td><td>-0.30</td><td>0.00000</td></tr><tr><td>EBIT/TA</td><td>0.35</td><td>0.31</td><td>0.09</td><td>0.25</td><td>-0.52</td><td>-0.25</td><td>0.00000</td></tr><tr><td>CSE</td><td>-0.23</td><td>-0.09</td><td>0.01</td><td>0.04</td><td>0.08</td><td>0.15</td><td>0.00000</td></tr><tr><td>C/TS</td><td>0.40</td><td>-0.07</td><td>0.22</td><td>-0.33</td><td>0.06</td><td>-0.30</td><td>0.00000</td></tr><tr><td>EBIT/TS</td><td>0.62</td><td>0.51</td><td>0.11</td><td>0.41</td><td>-0.65</td><td>-0.56</td><td>0.00000</td></tr></table>

H, p-value of a Kruskal–Wallis test for the equality of the sum of ranks of each group.

The positions of companies (1480 <sup>fi</sup>rms from the learning sample) on the map over the six-year period were used to calculate trajectories. As we designed six super-classes and six trajectories per super-class, we <sup>fi</sup>nally obtained thirty-six trajectories. Fig. 3 shows these trajectories.

Each line represents a set of trajectories according to the initial position of companies on the map in 1997. The <sup>fi</sup>rst line (trajectories 1–6) corresponds to companies in super-class 1 in 1997, the second line (trajectories 7–12) to those in super-class 2 in 1997, and so on. On each graph, the scale of the X-axis corresponds to the 6 years and the scale of the Y-axis to the six super-classes. The percentages in columns are the percentages of <sup>fi</sup>rms located in each super-class in 1997, and the percentages in rows are the same but within each trajectory.

The <sup>fi</sup>rst graph, in the upper left part of Fig. 3, displays a trajectory whose origin in 1997 is super-class 1, and whose destination 6 years later is the same super-class. This trajectory represents the behavior of companies that were very healthy in 1997 and that remain in the same <sup>fi</sup>nancial state over time. Conversely, the sixth graph, in the upper right part, displays the behavior of <sup>fi</sup>rms that were very healthy in 1997, but whose health has continued to deteriorate over time; they shifted from super-class 1 to super-class 2, then 3, and so on, to super-class 6 in 2002.

## 4.3. Forecasting results

Forecasting results were estimated using the test sample. Table 8 shows the correct classi<sup>fi</sup>cation rates calculated using the <sup>fi</sup>ve methods (discriminant analysis, logistic regression, neural networks, Cox's model, and trajectories) and data collected one, two, and three years before the date on which company status (failed or non-failed) was assessed.

Table 8 shows that, one year before failure, trajectories and the neural network achieved similar results (with respective <sup>fi</sup>gures for correct classi<sup>fi</sup>cation of 82.73% and 82.61%), but slightly higher than those obtained with discriminant analysis (81.93%), logistic regression (81.14%) and Cox's model (80.80%). Two years before failure, the correct classi<sup>fi</sup>cation rate achieved with trajectories fell by only 1.03%, whereas the rate achieved with Cox's model fell by 1.14%, that achieved with logistic regression by 1.59%, that achieved with the neural network by 2.72% and that achieved with discriminant analysis by 3.41%. Three years before failure, differences between the four models are even greater: the correct prediction rate of trajectories – 80.34% – was only 2.39 percentage point lower than the rate one year before failure, whereas Cox's model fell by 4.32 percentage point, logistic regression fell by 5.80 percentage point, the neural network by 6.59 percentage point and discriminant analysis by 6.70 percentage point.

Are the observed differences between the results achieved with the four models statistically signi<sup>fi</sup>cant? Table 9 shows, for each pair of results achieved with two different methods one, two, and three years before failure, the p-value of a test for differences between proportions.

![](/api/attachments/9BXNP724/fulltext/images/0ace51b885feefc936df1d35dc5d902b1331f79c0b15fcedc9c4787840a2e300.jpg)  
Fig. 2. Distribution of super-classes on the map.

Table 9 shows that the differences between correct rates achieved with trajectories and the four other methods become signi<sup>fi</sup>cant three years before failure, at the conventional threshold of 5%; the p-value is

0.010 between trajectories and discriminant analysis, 0.012 between trajectories and logistic regression, 0.028 between trajectories and the neural network, and 0.049 between trajectories and Cox's model. However, the same differences one may observe between results achieved two years before failure are not large enough, given the sample size, to be signi<sup>fi</sup>cant.

![](/api/attachments/9BXNP724/fulltext/images/3dda120d68ede81e469773f2b7f72e9128eb540ccec25ce51dedfc3568438c6e.jpg)  
Fig. 3. Distribution of trajectories by initial company position on the map in 1997

Table 8  
Table 10  
Correct classi<sup>fi</sup>cation rates calculated with data from the test sample.

<table><tr><td rowspan="2">Methods</td><td colspan="3">Years before failure</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>DA</td><td>81.93%</td><td>78.52%</td><td>75.23%</td></tr><tr><td>LR</td><td>81.14%</td><td>79.55%</td><td>75.34%</td></tr><tr><td>NN</td><td>82.61%</td><td>79.89%</td><td>76.02%</td></tr><tr><td>CM</td><td>80.80%</td><td>79.66%</td><td>76.48%</td></tr><tr><td>TR</td><td>82.73%</td><td>81.70%</td><td>80.34%</td></tr></table>

DA: Discriminant analysis.  
LR: Logistic regression.  
NN: Neural network.  
CM: Cox's model.  
TR: Trajectories.

From a general standpoint, trajectories are signi<sup>fi</sup>cantly more stable than are conventional methods; they are also more stable than Cox's model, even though this model relies on the same data as those used to design trajectories.

We have also analyzed the differences between the results achieved with the four models depending on whether companies are healthy or have failed. Table 10 shows the percentage of correct classi<sup>fi</sup>cation for these two groups.

Table 10 indicates that, in almost every case, discriminant analysis, logistic regression, the neural network and Cox's model do better than trajectories at predicting the fate of healthy companies, especially two and three years before failure. Thus, for two and three years before failure trajectories led to <sup>fi</sup>gures for correct classi<sup>fi</sup>cation of 81.14% and 80.91% respectively, compared to 87.27% and 85.00% for discriminant analysis, 87.95% and 84.77% for logistic regression, 87.27% and 83.64% for the neural network and 82.27% and 83.64% for Cox's model.

Nevertheless, when it comes to predicting the fate of failed <sup>fi</sup>rms, the results are completely different. For one year before failure, trajectories had an accuracy rate of 84.09%, as opposed to 82.05% for the neural network, 81.82% for logistic regression, 81.59% for discriminant analysis and 80.00% for Cox's model. The gap between trajectories and the other methods grows even wider when accuracy two or three years out is measured. For trajectories the <sup>fi</sup>gures are 82.27% and 79.77%, for Cox's model they are 77.05% and 69.32%, for the neural network they are 72.50% and 68.41%, for logistic regression they are 71.14% and 65.91%, and, <sup>fi</sup>nally, for discriminant analysis they are 69.77% and 65.45%. Actually, the good performance of traditional methods achieved with sound <sup>fi</sup>rms is at the expense of their accuracy with failed ones.

Analysis of the differences between correct classi<sup>fi</sup>cation rates, presented in Table 11, shows that traditional methods do not perform signi<sup>fi</sup>cantly better than trajectories, with healthy <sup>fi</sup>rms, and when the forecasting horizon is one or three years. However, except for Cox's model, they do when the horizon is 2 years (the p-value of the difference between trajectories and logistic regression is 0.005, and 0.013 between trajectories and the neural network as well as between trajectories and discriminant analysis). Conversely, with failed <sup>fi</sup>rms, such differences are statistically signi<sup>fi</sup>cant when the horizon is two or three years. On the whole, with sound companies, trajectories did slightly worse than other techniques, but much better with failed companies.

Correct classi<sup>fi</sup>cation rates calculated with data from the test sample by company group (healthy and failed).

<table><tr><td rowspan="2">Methods</td><td colspan="3">Years before failure</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td colspan="4">Healthy companies</td></tr><tr><td>DA</td><td>82.27%</td><td>87.27%</td><td>85.00%</td></tr><tr><td>LR</td><td>80.45%</td><td>87.95%</td><td>84.77%</td></tr><tr><td>NN</td><td>83.18%</td><td>87.27%</td><td>83.64%</td></tr><tr><td>CM</td><td>81.59%</td><td>82.27%</td><td>83.64%</td></tr><tr><td>TR</td><td>81.36%</td><td>81.14%</td><td>80.91%</td></tr><tr><td colspan="4">Failed companies</td></tr><tr><td>DA</td><td>81.59%</td><td>69.77%</td><td>65.45%</td></tr><tr><td>LR</td><td>81.82%</td><td>71.14%</td><td>65.91%</td></tr><tr><td>NN</td><td>82.05%</td><td>72.50%</td><td>68.41%</td></tr><tr><td>CM</td><td>80.00%</td><td>77.05%</td><td>69.32%</td></tr><tr><td>TR</td><td>84.09%</td><td>82.27%</td><td>79.77%</td></tr></table>

The results we obtain with conventional methods of designing failure models are consistent with the results of many studies published in the <sup>fi</sup>nancial literature.

First, as shown in Tables 1 and 2, models tend to have asymmetric results; indeed, very few models are as accurate with sound <sup>fi</sup>rms as they are with unsound <sup>fi</sup>rms. When a model does very well with healthy <sup>fi</sup>rms, it does worse with failed <sup>fi</sup>rms, and vice-versa.

Second, that model accuracy tends to worsen over time has a similar effect on both classes. Models seem no more accurate when they estimate a probability of failure than when they estimate a probability of survival unless the sample size is taken into account; indeed, a few studies using samples of more than 250 <sup>fi</sup>rms led to models that are more likely to predict accurately the fate of healthy <sup>fi</sup>rms than that of failed <sup>fi</sup>rms. One possible rationale for this result is that, as demonstrated in this research, and as stated by Pérez [44], sound companies have a much wider variety of <sup>fi</sup>nancial pro<sup>fi</sup>les than unsound companies. Since the sample size is reasonably large, this phenomenon seems to affect the results. Indeed, in such a situation, the proportion of companies that manage to survive, though their <sup>fi</sup>nancial situation is similar to that of some failed <sup>fi</sup>rms, is so large that models fail to discriminate between them. Classi<sup>fi</sup>cation errors then occur when models faced healthy <sup>fi</sup>rms having pro<sup>fi</sup>les similar to those of failing companies; failed <sup>fi</sup>rms may continue to do business, but it is much more unusual for healthy <sup>fi</sup>rms to go suddenly bankrupt.

Third, and <sup>fi</sup>nally, model accuracy tends to worsen as the forecasting horizon increases.

The advantage of trajectories over traditional methods should therefore be interpreted in light of the results that these conventional methods usually achieved. First, trajectories lead to rather wellbalanced results for failed and non-failed <sup>fi</sup>rms, although they are slightly in favor of failed companies when forecasts are made within a one- or two-year periods, and slightly in favor of non-failed companies when made within a three-year period. Second, the decrease in their accuracy over time is slight, making it a much more reliable tool for medium-term forecasts than traditional, single-period and multi-period models. Cox's model, using the same amount of data as the trajectories, is unable to capture the information that is contained in time-series data in the same way as trajectories do. Third, this slight decrease in accuracy does not come at the expense of failed companies, even though it is more pronounced for the latter than for sound <sup>fi</sup>rms (a reduction of 0.45% for healthy companies on a forecast made within a one-year period and a forecast within a three-year period, against a reduction of 4.32% for failed companies). This point is of particular importance. Indeed, the cost of misclassifying a failed <sup>fi</sup>rm (type I error) is far greater than the cost of misclassifying a healthy <sup>fi</sup>rm (type II error). In the <sup>fi</sup>rst case, for an investor or a creditor, a type I error involves the loss of an investment or debt that will not be reimbursed, while a type II error involves the loss of a potential bargain. This suggests that a good model should minimize type I error.

Test for differences between correct classi<sup>fi</sup>cation rates achieved one, two, and three years before failure.

<table><tr><td rowspan="3">Methods</td><td colspan="3">LR</td><td colspan="3">TR</td><td colspan="3">NN</td><td colspan="3">CM</td></tr><tr><td colspan="3">Years before failure</td><td colspan="3">Years before failure</td><td colspan="3">Years before failure</td><td colspan="3">Years before failure</td></tr><tr><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td></tr><tr><td>DA</td><td>0.667*</td><td>0.598</td><td>0.522</td><td>0.662</td><td>0.094</td><td>0.010</td><td>0.708</td><td>0.481</td><td>0.698</td><td>0.540</td><td>0.558</td><td>0.540</td></tr><tr><td>CM</td><td>0.855</td><td>0.953</td><td>0.577</td><td>0.294</td><td>0.277</td><td>0.049</td><td>0.324</td><td>0.906</td><td>0.823</td><td></td><td></td><td></td></tr><tr><td>NN</td><td>0.421</td><td>0.859</td><td>0.739</td><td>0.950</td><td>0.333</td><td>0.028</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TR</td><td>0.386</td><td>0.252</td><td>0.012</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

p-value of a test for differences between proportions.

Table 11  
Test for differences between correct classi<sup>fi</sup>cation rates achieved one, two, and three years before failure by company group.

<table><tr><td rowspan="3">Methods</td><td colspan="3">LR</td><td colspan="3">TR</td><td colspan="3">NN</td><td colspan="3">CM</td></tr><tr><td colspan="3">Years before failure</td><td colspan="3">Years before failure</td><td colspan="3">Years before failure</td><td colspan="3">Years before failure</td></tr><tr><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td></tr><tr><td colspan="13">Healthy companies</td></tr><tr><td>DA</td><td>0.489*</td><td>0.759</td><td>0.925</td><td>0.727</td><td>0.013</td><td>0.053</td><td>0.721</td><td>1.000</td><td>0.578</td><td>0.793</td><td>0.039</td><td>0.578</td></tr><tr><td>CM</td><td>0.667</td><td>0.018</td><td>0.644</td><td>0.931</td><td>0.663</td><td>0.289</td><td>0.536</td><td>0.039</td><td>1.000</td><td></td><td></td><td></td></tr><tr><td>NN</td><td>0.294</td><td>0.759</td><td>0.644</td><td>0.480</td><td>0.013</td><td>0.289</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TR</td><td>0.732</td><td>0.005</td><td>0.129</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="13">Failed companies</td></tr><tr><td>DA</td><td>0.931</td><td>0.658</td><td>0.887</td><td>0.325</td><td>0.000</td><td>0.000</td><td>0.861</td><td>0.372</td><td>0.352</td><td>0.549</td><td>0.015</td><td>0.222</td></tr><tr><td>CM</td><td>0.493</td><td>0.045</td><td>0.280</td><td>0.114</td><td>0.054</td><td>0.000</td><td>0.493</td><td>0.121</td><td>0.771</td><td></td><td></td><td></td></tr><tr><td>NN</td><td>0.930</td><td>0.653</td><td>0.430</td><td>0.419</td><td>0.001</td><td>0.000</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TR</td><td>0.370</td><td>0.000</td><td>0.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

\* p-value of a test for differences between proportions.

## 5. Conclusion

In this research, we have proposed a new way of assessing a company's <sup>fi</sup>nancial health. Unlike common practice in much of the <sup>fi</sup>nancial literature, our proposal is to use what we called “trajectories”, and a Kohonen map to quantize such trajectories, to measure it over time, rather than at a given moment in time. We also suggested using such a representation to do forecasting, and we compared the predictive ability of these trajectories to that of modeling methods traditionally used to design <sup>fi</sup>nancial failure models.

The performance of traditional models is fairly good when the forecast horizon is 1 year but is much less good at more than 1 year; nonetheless, our results showed that trajectories are as accurate as these models at short-term predictions (i.e., 1 year) and that their accuracy declines less swiftly when medium-term predictions (i.e., two or three years) are made. Trajectories are therefore a valuable tool for any <sup>fi</sup>nancial institution whose aim is to assess the risk of an investment or a debt over a longer period than usual. They are also a valuable tool for companies seeking to measure their <sup>fi</sup>nancial health, a tool that allows them, if necessary, to take a corrective action. Indeed, the forecast horizon of single-period models is far too short to enable companies to react to <sup>fi</sup>nancial threats. Trajectories, by contrast, make it possible to assess a medium-term trend and to detect <sup>fi</sup>nancial threats early enough for companies to deal with them.

## References

[1] E. Alfaro, N. Garcia, M. Games, D. Elizondo, Bankruptcy forecasting: an empirical comparison of adaboost and neural networks, Decision Support Systems 45 (2008) 110–122

[2] E.I. Altman, Financial ratios, discriminant analysis and the prediction of corporate bankruptcy, Journal of Finance 23 (1968) 589–609.

[3] E.I. Altman, R. Haldeman, P. Narayanan, Zeta analysis: a new model to identify bankruptcy risk of corporations, Journal of Banking and Finance 1 (1977) 29–51.

[4] E.I. Altman, G. Marco, F. Varetto, Corporate distress diagnosis: comparisons using linear discriminant analysis and neural network — the Italian experience, Journal of Banking and Finance 18 (1994).505–529

[5] E.I. Altman, Y.H. Eom, D.W. Kim, Failure prediction: evidence from Korea, Journal of International Financial Management and Accounting 6 (1995) 230–249

[6] J. Argenti, Corporate Collapse: The Causes and Symptoms, Halsted Press, New York, 1976.

[7] A.F. Atiya, Bankruptcy prediction for credit risk using neural networks: a survey and new results, IEEE Transactions on Neural Networks 7 (2001) 929–935.

[8] A. Aziz, D.C. Emanuel, G.C. Lawson, Bankruptcy prediction: an investigation of cash <sup>fl</sup>ow based models, Journal of Management Studies 25 (1988) 419–437.

[9] B. Back, G. Oosterom, K. Sere, M. van Wezel, Choosing Bankruptcy Predictors Using Discriminant Analysis, Logit Analysis and Genetic Algorithms, Technical Report, Turku Centre for Computer Science, 1996.

[10] S. Balcaen, H. Ooghe, 35 years of studies on business failure: an overview of the classical statistical methodologies and their related problems, British Accounting Review 38 (2006) 63–93.

[11] R. Barniv, A. Hershbarger, Classifying <sup>fi</sup>nancial distress in the life insurance industry, Journal of Risk and Insurance 57 (1990) 110–136.

[12] R. Barniv, J.B. McDonald, Identifying <sup>fi</sup>nancial distress in the insurance industry: a synthesis of methodological and empirical issues, Journal of Risk and Insurance 59 (1992) 543–574

[13] J. Betts, D. Belhoul, The effectiveness of incorporating stability measures in company failure models, Journal of Business Finance and Accounting 14 (1987) 323–334.

[14] M. Blum, Failing company discriminant analysis, Journal of Accounting Research 12 (1974) 1–25.

[15] A. Brabazon, P.B. Keenan, A hybrid genetic model for the prediction of corporate failure, Computational Management Science 1 (2004) 293–310.

[16] A. Brabazon, M. O'Neill, Diagnosing corporate stability using grammatical evolution, International Journal of Applied Mathematics and Computer Science 14 (2004) 363–374.

[17] A. Charitou, E. Neophytou, C. Charalambous, Predicting corporate failure: empirical evidence for the uk, European Accounting Review 13 (2004) 465–497.

[18] P.K. Coats, L.F. Fant, Recognizing <sup>fi</sup>nancial distress patterns using a neural network tool, Financial Management 22 (1993) 142–154.

[19] M. Cottrell, P. Rousset, The Kohonen algorithm: a powerful tool for analysing and representing multidimensional quantitative and qualitative data, in: J. Mira, R. Moreno-Diaz, J. Cabestany (Eds.), Lecture Notes in Computer Science, 1997, pp. 861–871.

[20] D. Cox, Regression models and life-tables, Journal of the Royal Statistical Society 34 (1972) 187–202.

[21] P.J. Cybinski, The dynamics of the <sup>fi</sup>rm's path to failure: towards a new methodology for modeling <sup>fi</sup>nancial distress, Ph.D. thesis, Grif<sup>fi</sup>th University, Brisbane, 1998.

[22] R.A. D'Aveni, The aftermath of organizational decline: a longitudinal study of the strategic and managerial characteristics of declining <sup>fi</sup>rms, Academy of Management Journal 32 (1989) 577–605.

[23] I.G. Dambolena, S.J. Khoury, Ratio stability and corporate failure, Journal of Finance 35 (1980) 1017-1026

[24] A.I. Dimitras R. Slowinski R. Susmaga C. Zopounidis Business failure prediction using rough sets, European Journal of Operational Research 114 (1999) 263–280.

[25] M. Doumpos, C.A. Zopounidis, Multicriteria discrimination method for the prediction of <sup>fi</sup>nancial distress: the case of Greece, Multinational Finance Journal 3 (1999) 71–101.

[26] P. du Jardin, Predicting bankruptcy using neural networks and other classi<sup>fi</sup>cation methods: the in<sup>fl</sup>uence of variable selection techniques on model accuracy, Neurocomputing 73 (2010) 2047–2060.

[27] R.O. Edmister, An empirical test of <sup>fi</sup>nancial ratio analysis for small business failure prediction, Journal of Financial and Quantitative Analysis 7 (1972) 1477–1493.

[28] M.J. Gombola, M.E. Haskins, J.E. Ketz, D.D. Williams, Cash <sup>fl</sup>ow in bankruptcy prediction, Financial Management 16 (1987) 55–65.

[29] D.C. Hambrick, R.A. D'Aveni, Large corporate failures as downward spirals, Administrative Science Quarterly 33 (1988) 1–23.

[30] S. Kotsiantis, D. Tzelepis, E. Koumanakos, V. Tampakas, Ef<sup>fi</sup>ciency of machine learning techniques in bankruptcy prediction, 2nd International Conference on Enterprise Systems and Accounting, 2005, pp. 39–49.

[31] R.C. Lacher, P.K. Coats, S.C. Sharma, L.F. Fant, A neural network for classifying the <sup>fi</sup>nancial health of a <sup>fi</sup>rm, European Journal of Operational Research 85 (1995) 53–65.

[32] T. Laitinen, Financial ratios and different failure processes, Journal of Business Finance and Accounting 18 (1991) 649–673.

[33] T. Laitinen, M. Kankaanpaa, Comparative analysis of failure prediction methods: the Finnish case, European Accounting Review 8 (1999) 67–92.

[34] E.K. Laitinen, T. Laitinen, Cash management behaviour and failure prediction, Journal of Business Finance and Accounting 25 (1998) 893–919.

[35] E.K. Laitinen, T. Laitinen, Bankruptcy prediction: application of the Taylor's expansion in logistic regression, International Review of Financial Analysis 9 (2000) 327–349.

[36] A.H. Lau, A <sup>fi</sup>ve-state <sup>fi</sup>nancial distress prediction model, Journal of Accounting Research 25 (1987) 127–138.

[37] K. Lee, D. Booth, P. Alam, A comparison of supervised and unsupervised neural networks in predicting bankruptcy of Korean <sup>fi</sup>rms, Expert Systems with Applications 29 (2005) 1–16.

[38] D.A. Levinthal, Random walks and organizational mortality, Administrative Science Quarterly 36 (1991) 397–420.

[39] G.W. Milligan, A Monte-Carlo study of thirty internal criterion measures for cluster analysis, Psychometrika 46 (1981) 187–199.

[40] R.C. Moyer, Forecasting <sup>fi</sup>nancial failure: a re-examination, Financial Management 6 (1977) 11–17.

[41] J.H. Nam, T. Jinn, Bankruptcy prediction: evidence from Korean listed companies during the IMF crisis, Journal of International Financial Management and Accounting 11.(2000).178–197

[42] M.C. Odom, R. Sharda, A neural network model for bankruptcy prediction, the IEEE International Joint Conference on Neural Networks, 1990, pp. 163–168.

[43] J.A. Ohlson, Financial ratios and the probabilistic prediction of bankruptcy, Journal of Accounting Research 18 (1980) 109–131.

[44] M. Pérez, From performance analysis to <sup>fi</sup>nancial failure prediction: the contribution of neural classi<sup>fi</sup>cation, Ph.D. thesis, Jean-Moulin University, Lyon III, 2002.

[45] S. Piramuthu, H. Ravagan, M.J. Show, Using feature construction to improve the performance of neural networks, Management Science 44 (1998) 416–430.

[46] P.P.M. Pompe, A.J. Bilderbeek, Bankruptcy prediction: the in<sup>fl</sup>uence of the year prior to failure selected for model building and the effects in a period of economic decline, International Journal of Intelligent Systems in Accounting, Finance and Management 13 (2005) 95-112

[47] J.W. Sammon, A nonlinear mapping for data structure analysis, IEEE Transactions on Computers c-18 (1969) 401–409.

[48] C. Serrano-Cinca, Self-organizing neural networks for <sup>fi</sup>nancial diagnosis, Decision Support Systems 17 (1996) 227–238.

[49] S. Sharma, V. Mahajan, Early warning indicators of business failure, Journal of Marketing 44 (1980) 80–89.

[50] T. Shumway, Forecasting bankruptcy more accurately: a simple hazard model, Journal of Business 74 (2001) 101–124.

[51] R.J. Taf<sup>fl</sup>er, The assessment of company solvency and performance using a statistical model, Accounting and Business Research 13 (1983) 295–3074.

[52] K.Y. Tam, M.Y. Kiang, Managerial applications of neural networks: the case of bank failure predictions, Management Science 38 (1992) 926–947.

[53] S. Thornhill, R. Amit, Learning about failure: bankruptcy, <sup>fi</sup>rm age, and the resource-based view, Organization Science 14 (2003) 497–509.

[54] W.L. Tung, C. Quek, P. Cheng, GenSo-EWS: a novel neural-fuzzy based early warning system for predicting bank failures, Neural Networks 17 (2004) 567–587.

[55] J. Yim, H. Mitchell, A comparison of corporate failure models in Australia: hybrid neural networks, logit models and discriminant analysis, Working Paper, RMIT Business, School of Economics and Finance, 2002.

[56] J.M. Zurada, B.P. Foster, T.J. Ward, R.M. Barker, Neural networks versus logit regression models for predicting <sup>fi</sup>nancial distress response variables, Journal of Applied Business Research 15 (1998) 21–29.

![](/api/attachments/9BXNP724/fulltext/images/e28f17461109d5e52a64a42bf5b85abbcd407a5b668415f90a0ed9cf666375ed.jpg)  
Philippe du Jardin is currently a Professor of computer science at Edhec Business School and Head of the Information Technology Department. He received his Ph.D. in business administration from University of Nice — France. Prior to coming to Edhec, he held academic appointments in various French business schools and universities. In addition, he has signi<sup>fi</sup>cant working experience with different companies as a consultant and continues to consult regarding data analysis and statistical studies. His research interests are mainly in the application of neural networks to corporate <sup>fi</sup>nance.

![](/api/attachments/9BXNP724/fulltext/images/8299a211c7c4e441c6477b07b80194c4c295ef629af7cf83f25624eeb4d01a71.jpg)  
Eric Séverin is a Professor of <sup>fi</sup>nance at USTL (University of Lille) and he is a specialist in corporate <sup>fi</sup>nance. His research interests are twofold: bankruptcy forecasting and the relationship between economics and <sup>fi</sup>nance.
