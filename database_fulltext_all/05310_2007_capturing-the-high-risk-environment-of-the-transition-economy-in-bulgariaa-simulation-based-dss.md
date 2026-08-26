---
otero_id: 5310
otero_key: "TBAU443K"
title: "Capturing the high-risk environment of the transition economy in Bulgaria—a simulation-based DSS"
authors: "David L. Olson; Margaret Shipley; Madeline Johnson; Nikola Yankov"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.11.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Capturing the high-risk environment of the transition economy in Bulgaria—a simulation-based DSS

David L. Olson <sup>a,\*</sup>, Margaret Shipley <sup>b</sup>, Madeline Johnson <sup>b</sup>, Nikola Yankov <sup>c</sup>

<sup>a</sup> Deparment of Management, University of Nebraska, Lincoln, NE 68588-0491, United States

<sup>b</sup> University of Houston-Downtown, United States

<sup>c</sup> Tsenov Academy of Economics, Svishtov, Bulgaria

Available online 13 December 2004

## Abstract

Eastern European countries have undergone a transition from centralized economic planning to more open economic systems. Hard data based upon past experience are inappropriate for decision making in this radically changed environment. A team of Bulgarian and U.S. researchers utilized system dynamics simulation to model the microeconomic environment of a Bulgarian winery expanding into regional and international markets. Expert opinion was provided for both micro- and macroeconomic factors. Given the uncertainty of the data and the ambiguity in the experts’ opinions, fuzzy logic was used to model the transitional economic firm’s decision making. <sup>D</sup> 2004 Elsevier B.V All rights reserved

Keywords: Transition economies; System dynamics; Fuzzy models; Simulation

## 1. Introduction

The transition from a planned economy to a market economy for former Soviet bloc countries involve high levels of uncertainty. Firms in the transition economies faced an ambiguous set of information and cues that directly challenged existing ownership, operating principles and practices, and market structure. For example, in the centrally planned economy decisions regarding products, quantity, price, suppliers, and market were determined outside of the firm. Therefore, managers at the firm level made operating decisions rather than strategic decisions and made them in a relatively risk-free environment. This type of decision-making environment represented a sharp contrast to the risk-rich environment of capitalist markets. Consequently, managers of firms in the transition economies were thrust into a position where their personal knowledge, as well as the organizational knowledge, that supported the firm’s operations proved to be inadequate to support decision making. In addition, managers faced uncertainty in the flow of resources into the firm. The process of privatization created ambiguity about the ownership of assets and, in some instances, resulted in the destruction of income-producing assets.

The transition economies followed a pattern of economic development during the first 10 years of transition. All of these countries went through a recession with corresponding drastic declines in real output. The number of consecutive years of real output decline ranged from 2 years in the case of Poland to 10 years for the Ukraine [20]. Bulgaria’s initial recession lasted 4 years. However, unlike most of the other transition economies that began a slow but constant recovery after the initial period, Bulgaria had a second recession after their initial recover. Consequently, managers in Bulgarian firms faced a particularly bumpy economic ride during the first 10 years.

The chaotic environment of the transition period coupled with the lack of experience in operating in a market economy presented new decision-making challenges for transition economy managers. Data were no longer readily available, and uncertainty surrounded the sources and validity of data that could be gathered. Managers understood the firm’s operations, but had little or no knowledge of markets outside of the local area. Managers made decisions that moved the firm slowly from the status quo that existed under the old planned economy, because they operated within the principle of ambiguity and risk aversion. Research on ambiguity and risk aversion has revealed that a decision maker’s reluctance to accept a risky alternative depends on the decision maker’s confidence in forecasting outcomes relative to others [14]. In transition economies, the established management tended to choose uncertain outcomes tied to status quo options where they felt relatively more competent than to choose uncertain outcomes tied to new opportunities requiring organizational knowledge that the firm did not possess. This phenomenon frustrated political leaders who wanted firms to adapt more quickly and led to recommendations that government policies should encourage existing enterprises to release assets to a new breed of entrepreneurs [20]. Unfortunately, one of the consequences of forcing existing management out of firms is a loss of operational experience, particularly in managing large organizations. This raises the question of whether a decision support tool can be developed that will help experienced managers in transition firms predict outcomes in the new competitive environment.

One way to move beyond acceptance of the status quo is to simulate possible events and outcomes. Simulation allows microeconomic and macroeconomic factors to be modeled and input values to be varied. Then, by observing the potential for profitability within identified markets, more informed decision making can take place. A realistic simulation representative of the transition economy, thus, provides a tool by which levels of uncertainty can be modeled, risk-averse status quo decisions can be replaced, and the transition economy manager can better visualize competition in the free market economy.

Collaboration with Bulgarian colleagues verified that a systems simulation model was desirable because it allows decision makers the opportunity to investigate the impact of various business decisions, such as product promotion, pricing, capital replenishment, and labor force development on a variety of outcomes, specifically, expected profit, market share, perceptions of product quality, and cash flow. Originally, all input and output parameters were viewed as stochastic variables with a traditional normal distribution. However, during the collaboration, the uncertainty of data availability and accuracy, as well as reliance on expert opinion with inherent ambiguity, led to the consideration of fuzzy set distributions.

Fuzzy set theory became a key consideration for this simulation because it deals with uncertainty where ambiguous terms are present. When a decision maker uses subjective judgment to specify an optimal level of each attribute necessary for the product to be successful in the marketplace, he/she does so under conditions of uncertainty. Extant methods that utilize classical logic or statistics are inadequate for effectively dealing with situations where limited information is available. The inadequacies of probability theory and other traditional quantitative techniques to account for uncertainty in personal judgments have been noted by behavioral and expected utility theorists [7,13].

One of the initial questions to be addressed in simulating the transition firm was whether to base the simulation on a normal or fuzzy model. The goal of this research was to compare the output from a simulation built on a normal model to the output from a simulation built on a fuzzy model. This comparison would help identify a systems dynamics model that would best fit the dynamics of the transition economy, specifically the Bulgarian economy.

## 2. System dynamics and fuzzy sets

System dynamics was developed by Forrester et al. [9,10,17]. It has its roots in general systems theory [21] and the work on cybernetic systems of Stafford Beer [2] and others. Open systems theory views an organization as residing within an environment from which there is a continuous flow of information between the organization and the environment. System dynamics models can reflect interaction among dynamic markets, uncertain production systems, and cash flow features of operating businesses. Cybernetic systems are complex, probabilistic, and purposive, with feedback and control. This feedback and control is a characteristic of system dynamic simulation models. More recent books in system dynamics include Coyle [6] and Sterman [19]. Sterman has been especially active in publishing accounts of the application of system dynamics in academic research. Such applications include development of simulation models to analyze public policy issues [5], as well as issues of quality [1,16]. Gregoriades and Karakostas [11] provided a recent system dynamics implementation of a decision support system.

Checkland [4] extended the idea of systems modeling to include mental models, viewing systems as consisting of interacting parts working toward some end, with the same feedback control discussed by Beer. The primary extension provided by Checkland was a soft systems view, incorporating expert (or at least experienced participant) input of subjective data as the basis for hypothesized relationships.

The main idea behind the concept of a fuzzy set is the generalization of the concept of the characteristic function of a set. Let X denote a universal set and denote by A some subset of X.

Then the characteristic function of set A is

$$
I _ {\mathrm{A}} (x) = \left\{ \begin{array}{l} 1 \text {   if   } x \in \mathrm{A} \\ 0 \text {   if   } x \notin \mathrm{A} \end{array} \right..\tag{1}
$$

With an ordinary (i.e., crisp) set, the characteristic function is always 0 or 1. That is, any element of universal set X, clearly is in set A or is not in set A. In fuzzy set theory, it is no longer certain whether an element is or is not in a certain set. Thus, any element can belong to some degree to any set. Suppose, for example, that A denotes the set of all <sup>b</sup>tall men<sup>Q</sup>. John is 6 feet tall. Does John belong in set A? Belonging or not belonging to set A is to some extent a matter of opinion.

To deal with such uncertainty, the generalization of the concept of a characteristic function becomes a fuzzy membership function. Associated with every $x { \in } X ,$ there is a value $m _ { \mathrm { A } } ( x )$ , which indicates the degree to which it is believed that element x belongs to fuzzy set A. This membership function can take any value on the closed interval [0,1]. Membership equal to zero says that element x is definitely not in A, while membership equal to one says that x definitely is in A. Values between zero and one represent varying degrees of uncertainty as to whether or not x is a member of set A. In mathematical terms, $m _ { \mathrm { A } } \colon$ $X { \longrightarrow } [ 0 , 1 ]$ , X is called the universe of discourse of $m _ { \mathrm { A } } \ [ 2 3 ]$

The usual set operations of complementation, union, and intersection are extended to fuzzy sets through the membership function. Specifically, the membership function of the complement of fuzzy set $\mathbf { A } ,$ designated by $\neg \mathrm { A } ,$ is $m _ { \neg \mathrm { A } } ( x ) { = } 1 { - } m _ { \mathrm { A } } ( x )$ ; the membership function of the union of fuzzy set A with fuzzy set B, designated by A\_B is $m _ { \mathrm { A V B } } ( x ) =$ Max $\{ m _ { \mathrm { A } } ( x ) , m _ { \mathrm { B } } ( x ) \}$ }, and the membership function of the intersection of fuzzy set A with fuzzy set B, designated by $\mathbf { A } \wedge \mathbf { B }$ is $m _ { \mathrm { A } \land \mathrm { B } } ( x ) { = } \mathrm { M i n } \{ m _ { \mathrm { A } } ( x ) , m _ { \mathrm { B } } ( x ) \}$

When fuzzy sets are defined on a finite support (i.e., finite universal set), a commonly used notation is $a { = } a _ { 1 } /$ $x _ { 1 } { + } a _ { 2 } { / } x _ { 2 } { + } . \ldots { + } a _ { n } { / } x _ { n }$ . This statement is read, element $x _ { 1 }$ is in fuzzy set a with membership $a _ { 1 } .$ , element $x _ { 2 }$ is in fuzzy set a with membership $_ { a _ { 2 } , }$ etc. Fuzzy sets of course, can have nonfinite support, but for our purposes, finite support will suffice. (For more on the theory of fuzzy sets, the interested reader is referred to one of the many references available [3,12,15,22–27]).

There are many fuzzy functions that can be used. Rizzi et al. [18] gave trapezoidal fuzzy numbers as one of the most frequently used methods of incorporating fuzzy concepts in models. Since the base model was normally distributed, triangular functions were deemed to be most appropriate and satisfied the literature as a form of trapezoidal function with 0 plateau.

## 3. Model development process

Model building began at an international workshop held at Tsenov Academy of Economics in 2002. The soft systems methodology, including the definition of an unstructured problem and the development of a mental picture, was followed. The workshop activities included the identification of modeling tools, the choice of a winery as the representative firm in transition, and the functional components of the model. In October 2003, a second meeting was held in Bulgaria at which the model was revised to reflect changes identified by the winery experts (faculty from the Tsenov Academy of Economics), the economic experts (the two Bulgarian Academy of Science participants), and the modelers (the four U.S. faculty). Included in this meeting was a discussion about the fit between the original conceptual model and the real world.

Consistent with other system dynamics models, most of the data were subjective (expert opinion). The experts in this case included winery managers and faculty from Tsenov Academy of Economics, whose previous research had given them extensive knowledge of winery operations. Researchers from the Institute of Economics of the Bulgarian Academy of Sciences provided concrete data on economic conditions, as well as prices and volumes for the Bulgarian wine industry.

The system dynamics model was implemented on an Excel spreadsheet, supplemented by the simulation software Crystal Ball. Crystal Ball was selected by the Bulgarian and United States collaborative team after demonstration of other more sophisticated software packages, such as iThink and Vensim. First, given the novice status of the Bulgarian simulator, the ease of use was considered. Spreadsheet software can accommodate time-oriented relationships very well. A Crystal Ball extension from an Excel model includes features of an advanced Monte Carlo simulation, such as generating thousands of sample runs and displaying probabilistic outcomes of the simulation model. This approach has been used for system dynamic simulations [8]. Second, the transition economy itself imposed some financial restrictions on the selection of simulation packages due to software costs and hardware maintenance. Crystal Ball was chosen by the team of researchers to respond to constraints of the Bulgarian researchers, to satisfy the needs of the

Bulgarian firm, and to allow investigation of the best fit model since fuzzy set based simulations can be performed.

## 4. Model of transition firm

The model included wine production to meet regional, national, and international demands. Each of these demand levels involved probabilistic, interrelated demand growth that could be influenced by firm efforts. The firm makes decisions concerning price, promotion, capital expenditure, and training. The firm’s crop yield is probabilistic. In the regional market, demand is probabilistic. At the industry level, competitors make decisions concerning their pricing, promotion, and capacity. At the national level, governments make decisions relative to taxes and restrictions on production or trade. National as well as the export market demand are probabilistic.

Monthly operations over a 6-year period were chosen as the time frame. This time frame is long enough to show the impact of input decisions in the subject winery. Extensions beyond 6 years are easy to add to the model. Model components are listed in Table 1. Output measures include profit, cash flow, net present worth, and market share by market. User inputs include promotion, product quality, and price decisions.

Promotion is lagged over 3 months, with weights of 0.5 for prior month effort, 0.35 for efforts 2 months prior, and 0.15 for efforts 3 months prior. The primary impact on quality is the source of grapes. Management felt that those grapes grown on their own fields had higher quality control. These grapes would be used first, supplemented by grapes purchased on the open market for any extra production planned. Prices were set by market. Place decisions allowed management to block marketing wines in any of the three markets (local, national, export).

Table 1 Winery model elements

<table><tr><td colspan="2">Inputs</td><td>System measures</td></tr><tr><td>Promotion</td><td>Lagged over 3 months</td><td>Profit</td></tr><tr><td>Product quality</td><td>Grown grapes higher quality</td><td>Cash flow</td></tr><tr><td>Price</td><td></td><td>Market share</td></tr><tr><td>Place</td><td>Market selections</td><td>Net present worth</td></tr><tr><td>Growth</td><td>Units of land planted</td><td></td></tr></table>

Growth decisions involved how many units of land to plant in grapes. Planting was assumed to involve seasonal expenses. Output from growth decisions would be available during the harvesting season 3 years later, assumed to be 20% in July, 30% in August, 40% in September, and 10% in October. Acquiring land involved a one-time capital investment in January. Owning land involved monthly maintenance reflected in labor (with a minimum of one person). Growing grapes involved expenses in February through June. Harvesting expenses occurred in July through October. Relative data by month used in the model are given in Table 2.

Management made decisions about how much to produce by product. This impacted the gross quantity of grapes required. If growth on owned land was insufficient, the purchasing decision was the quantity purchased to fill production levels decided by management. Expenses for purchased grapes were paid in the month of wine production.

Three markets (local, national, and export) were modeled, in compliance with data in Table 1. At this stage, only two wine products were modeled (low quality and high quality). This creates six productmarkets: low quality/local, high quality/local, low quality/national, high quality/national, low quality/ export, and high quality/export.

The system dynamics model consisted of timevariant variables in three classes: exogenous variables representing the environment, input variables relating to labor, promotion and investment decisions, and system variables measuring different types of output. Each variable is described below.

Relative product demand and labor required by month  
Table 2

<table><tr><td>Month</td><td>Relative demand</td><td>Relative farming labor</td><td>Relative bottling labor</td></tr><tr><td>January</td><td>0.6</td><td>1.3</td><td>0.8</td></tr><tr><td>February</td><td>0.7</td><td>1.3</td><td>0.8</td></tr><tr><td>March</td><td>0.8</td><td>0.8</td><td>0.8</td></tr><tr><td>April</td><td>0.9</td><td>0.8</td><td>0.8</td></tr><tr><td>May</td><td>1.0</td><td>0.8</td><td>0.8</td></tr><tr><td>June</td><td>0.9</td><td>0.8</td><td>1.4</td></tr><tr><td>July</td><td>0.8</td><td>1.3</td><td>1.4</td></tr><tr><td>August</td><td>0.7</td><td>1.3</td><td>1.4</td></tr><tr><td>September</td><td>1.0</td><td>1.3</td><td>1.4</td></tr><tr><td>October</td><td>1.2</td><td>0.5</td><td>0.8</td></tr><tr><td>November</td><td>1.5</td><td>0.5</td><td>0.8</td></tr><tr><td>December</td><td>1.9</td><td>1.3</td><td>0.8</td></tr></table>

## 5. Exogenous variables

Exogenous variables are model elements out of the control of the firm’s management.

## 5.1. Demand

The natural rate of growth of demand (independent of promotion by the firm and its competitors) was entered for the industry by market (local, national, and export). A normally distributed random variable was generated for the change in demand, with a mean of 0.01 and standard deviation of 0.03 per month. Demand changed randomly, but was also influenced by seasonal tendencies. Demand change was modeled to affect all six productmarkets the same (perfect correlation of demand across product-markets). This could be modified should expert assessment of detailed conditions call for a change. For the first 12 months, the initial year’s demand was multiplied by the appropriate monthly proportion of demand given in Table 3, as well as by one plus the randomly generated change in demand for that month. Demands by month for years two through six were based upon the demand 12 months prior multiplied by one plus the random change in demand. Monthly demand changes were not correlated.

## 5.2. Competitor’s product-market price

The product-market price of competitors was assumed to be independent of the firm. Change in price for each of the six product-markets was assumed to depend on a common normally distributed variable with mean 0.005 lev and a standard deviation of 0.01. Product-market price was generated as the prior month’s price plus the generated price change.

## 5.3. Competitor promotion

Initial competitor promotion levels by product are input as data. Change in competitor promotion is generated from a normal distribution. Means and standard deviations varied by market.

Table 3  
System dynamic distributions and parameters

<table><tr><td>Probabilistic model element</td><td>Base model</td><td>Fuzzy model</td></tr><tr><td>Change in demand</td><td>No(0.01,0.03)</td><td>T(-0.02,0.01,0.06)</td></tr><tr><td>Change in market price</td><td>No(0.005,0.01)</td><td>T(-0.01,0.005,0.02)</td></tr><tr><td>Change in Mkt Ad—local low</td><td>No(0,0.1)</td><td>T(-0.3,0,0.5)</td></tr><tr><td>Change in Mkt Ad—local high</td><td>No(0.01,0.2)</td><td>T(-0.5,0.01,0.8)</td></tr><tr><td>Change in Mkt Ad—nat&#x27;l low</td><td>No(0,0.2)</td><td>T(-0.6,0,0.8)</td></tr><tr><td>Change in Mkt Ad—nat&#x27;l high</td><td>No(0.02,0.2)</td><td>T(-0.6,0.2,0.8)</td></tr><tr><td>Change in Mkt Ad—exp. low</td><td>No(0,0.2)</td><td>T(-0.7,0,0.9)</td></tr><tr><td>Change in Mkt Ad—exp. high</td><td>No(0.03,0.2)</td><td>T(-0.8,0.03,0.9)</td></tr><tr><td>Crop yield</td><td>No(1,0.2)</td><td>T(0.4,1,1.8)</td></tr></table>

No(mean, standard deviation): normal distribution.  
T(min,mode,max): triangular (fuzzy) distribution.

## 5.4. Market share possibilities

For each product-market $" p " .$ , the possible market share for the firm was generated. This market share was constrained to fall between zero and one. The formula was to take the prior possible market share $[ \mathrm { M S } _ { t - 1 , p } ]$ and multiply it by the ratio of prior firm promotion $[ 0 . 5 \times \mathrm { P F } _ { t - 1 , p } + 0 . 3 5 \times \mathrm { P F } _ { t - 2 , p } + 0 . 1 5 \times \mathrm { P F } _ { t - 3 , p } ]$ divided by base firm promotion $[ \mathrm { P F } _ { 0 , p } ]$ (set initially) over competitor promotions $\mathrm { [ P C } _ { t , p } ]$ multiplied by one plus the ratio of current firm price $[ \mathrm { P r } F _ { t , p } ]$ minus current market price $[ \mathrm { P r } M _ { t , p } ]$ over base price in that productmarket $[ \mathrm { P r } F _ { 0 , p } ]$ . This formula, for clarification:

$$
\begin{array}{l} \mathrm{MS} _ {t, p} = \operatorname{MIN} \left(1, \mathrm{MS} _ {t - 1, p} \times \text { MAX } \right. \\ \times \left[ 0, \frac {\left(\frac {0 . 5 \times \mathrm{PF} _ {t - 1 , p} + 0 . 3 5 \times \mathrm{PF} _ {t - 2 , p} + 0 . 1 5 \times \mathrm{PF} _ {t - 3 , p}}{\mathrm{PF} _ {0 , p}}\right)}{\mathrm{PC} _ {t , p} \times \left(1 + \frac {\mathrm{Pr} F _ {t , p} - \mathrm{Pr} M _ {t , p}}{\mathrm{Pr} F _ {0 , p}}\right)} \right] \end{array}\tag{2}
$$

## 5.5. Crop yield

Annual crop yield is a function of land planted in grapes, as well as a normally distributed random variable with mean 1.0 and standard deviation 0.2. Annual crop yield is allocated 0.2 to July, 0.3 to August, 0.4 to September, and 0.1 to October.

## 6. Input variables

Input variables are the model elements that can be changed by the firm management.

## 6.1. Price

The firm can enter monthly prices for each of its products for each market over the entire range of time periods.

## 6.2. Promotion

The firm can enter monthly promotion expenditures for each product-market over the entire range of time periods.

## 6.3. Plant capacity

Prior plant capacity depreciates at the rate of 0.005 per month. The firm can add capacity in any month with a 3-month construction lag.

## 6.4. Labor

Labor is needed for planting, harvesting, and bottling. The firm has two choices. Labor costs incurred as needed would yield a lower-quality output. A permanent labor force would yield a higher-quality output. Labor cost per time period has a modeled inflation rate of 3% per year.

## 7. System variables

System variables in this study relate to performance measures of interest.

## 7.1. Sales

Sales by product-market are generated as available inventory on hand for each product, capped by possible sales (market demand by product times market share possibility). Priority was given to export sales, followed by national sales, and last to local sales.

![](/api/attachments/TBAU443K/fulltext/images/aaf59487568a00a39ab00d3dac34d0f999cd6eada99475d8b09e2e48da5a6242.jpg)  
Fig. 1. End bank balance—base model.

## 7.2. Inventory

Bottles of wine are produced in high and low quality. Firm grown grapes are required for highquality bottles, which are given top priority. Any excess bottling capacity is applied to bottling low-quality wines, which determines grapes purchased (up to available purchase maximum).

## 7.3. Bank balance

The bank balance is simply initial cash on hand plus revenues for the month, minus expenditures for the month, plus interest. Interest is received if the ending balance is positive (at the rate of 5% per year). Interest is paid if the ending balance is negative (at the rate of 15% per year). Expenses are incurred for promotion, purchasing grapes, adding capacity, hiring labor, and holding inventory.

## 8. Simulation results

For comparison, we ran two simulation models: (1) a base model for which all variables are assumed to be normally distributed, and (2) a fuzzy set based model using a triangular distribution with parameters roughly similar to the normal distribution (fuzzy model). The distribution parameters by model element are given in Table 3.

![](/api/attachments/TBAU443K/fulltext/images/211eff275c0d55e7598ed63111a22eaea1c715a8bfd339f28a47433a7425b62e.jpg)  
Fig. 2. End bank balance—fuzzy model.

![](/api/attachments/TBAU443K/fulltext/images/eb4cda1c22647ffb7bdbb706c4bf2cc3762dc269da1a4ee922f3af7a4894bbc0.jpg)  
Fig. 3. Market share–low-quality product–base model.

Forecast: Market Share low - end year 6  
![](/api/attachments/TBAU443K/fulltext/images/127488bf8a4a09154be80cccdc4ab6452da6806812ed37262ae530bf709222b3.jpg)  
Fig. 4. Market share–low-quality product–fuzzy model.

![](/api/attachments/TBAU443K/fulltext/images/eaf4a9fdf3ed214bfdfe0de42cac70b132a4a0b21b6cd611aa38739555f48394.jpg)  
Fig. 5. Market share–high-quality product–base model.

Forecast: Market share high - end year 6  
![](/api/attachments/TBAU443K/fulltext/images/86b334cf2c4721c1ed5e6725aa21a1ae9dc0d63ec0aa3084e80124338a5b4db1.jpg)  
Fig. 6. Market share–high-quality product–fuzzy model.

Simulation outputs measured were the bank balance after 6 years and market shares for lowquality and high-quality wine products. One thousand repetitions of each combination of inputs were obtained using Crystal Ball.

The ending bank balance results for the base model are displayed in Fig. 1, and the ending bank balance results for the fuzzy model are shown in Fig. 2.

Several differences in the ending bank balance between the two simulation models are noteworthy. First, the range of ending banking balances is greater for the fuzzy model than for the base (normally distributed) model. Second, the mean for the fuzzy model is 1.4 million lev compared to 2.2 million lev for the base model. Third, the distribution of output from the fuzzy model was skewed more toward negative outcomes than the distribution from the base model.

Fig. 3 shows the market share output for the lowquality products using the base model, and Fig. 4 shows the same using the fuzzy model.

Once again, the range of outcomes from the fuzzy model was wider (0–61%) than those generated from the base model (0–37%). The means for the two models were similar with a 19% market share for lowquality wines under the base model and a 20% market share for low-quality wines under the fuzzy model. Also noteworthy are the greater dispersion of occurrences across the entire range under the fuzzy model in comparison to the base model.

Finally, the results for market shares for highquality wines are shown in Fig. 5 (base model) and Fig. 6 (fuzzy model).

Interestingly, the differences between the two models in the market share outputs for high-quality wine were not as striking as those shown for lowquality wines. The range of outputs from the base model was 0–23% market share compared to 0–28% market share under the fuzzy model. However, the medians were further apart. Under the base model, the median was 14% while the median of the fuzzy model was 17%. The shape of the dispersions for market share outputs for high-quality wines was more similar than the shape associated with market shares for lowquality wines.

Table 4  
Summary of simulation output measures

<table><tr><td></td><td>End balance (after 6 years)</td><td>End bal</td><td>End bal</td><td>Market share</td><td>Market share</td></tr><tr><td>Model</td><td>μ (mean)</td><td>Pr{&lt;0}</td><td>Pr{&lt;1,000,000)</td><td>Low</td><td>High</td></tr><tr><td>Base (normal)</td><td>2,221,079–705,769 τo 5,683,566</td><td>0.111</td><td>0.298</td><td>0.19, 0 to 0.37</td><td>0.14, 0 to 0.23</td></tr><tr><td>Fuzzy (triang.)</td><td>1,407,749–1,094,282 τo 5,993,370</td><td>0.250</td><td>0.480</td><td>0.20, 0 to 0.61</td><td>0.17, 0 to 0.28</td></tr></table>

Table 5

<table><tr><td colspan="3">Wider fuzzy model inputs</td></tr><tr><td>Probabilisticmodel element</td><td>Fuzzymodel</td><td>Wide fuzzymodel</td></tr><tr><td>Change in demand</td><td>T(-0.02,0.01,0.06)</td><td>T(-0.05,0.02,0.11)</td></tr><tr><td>Change in market price</td><td>T(-0.01,0.005,0.02)</td><td>T(-0.025,0.005,0.035)</td></tr><tr><td>Change in Mkt Ad—local low</td><td>T(-0.3,0,0.5)</td><td>T(-0.6,0,1)</td></tr><tr><td>Change in Mkt Ad—local high</td><td>T(-0.5,0.01,0.8)</td><td>T(-1.02,0.01,1.59)</td></tr><tr><td>Change in Mkt Ad—nat’l low</td><td>T(-0.6,0,0.8)</td><td>T(-1.2,0,1.6)</td></tr><tr><td>Change in Mkt Ad—nat’l high</td><td>T(-0.6,0.2,0.8)</td><td>T(-1.24,0.02,1.58)</td></tr><tr><td>Change in Mkt Ad—exp. low</td><td>T(-0.7,0,0.9)</td><td>T(-1.4,0,1.8)</td></tr><tr><td>Change in Mkt Ad—exp. high</td><td>T(-0.8,0.03,0.9)</td><td>T(-1.57,0.03,1.77)</td></tr><tr><td>Crop yield</td><td>T(0.4,1,1.8)</td><td>T(0.2,1,2.6)</td></tr></table>

A summary of the key differences between the base model using normal distributions and the fuzzy model using triangular distributions (approximating normal distributions) is found in Table 4.

The outcome differences between the base and fuzzy model can be explained by the difference in the distributions. Although, the triangular distribution (and the widely used trapezoidal distribution) can, in theory, be set to satisfy a normal distribution, the results show some differences. In general, the fuzzy model produced a greater range of values for every output parameter. The mean was lower than that of the base model for the bank balance after 6 years, but the median was higher for market share. Therefore, the measure of central tendency cannot be determined to be more realistic for one model over the other. However, a vast difference in the thickness of the region toward the tails is observable for all parameters. This would be indicative of a decline in expected performances, which is further supported by the results in Fig. 4, which show a higher probability for lower-ending balances when fuzzy models are used.

## 9. Conclusions

While the input for the fuzzy models was similar to that of the normal distributions used in the base model, there was a clear decline in expected profits. This decline could be attributed to the interactions in the time-oriented system dynamics model. While the normal distribution has the opportunity for more extreme events (due to its infinite tails), the triangular distributions used for the fuzzy models had a greater dispersion of events due to the thicker tails. While these more extreme events were both large and small, the impact was a more negative result.

The greater ranges and volatility of the fuzzy model appears to provide a more credible representation of possible outputs. A decision maker’s willingness to accept the outcomes from a simulation as realistic is partially determined by his/her knowledge of current and past events. If the events, such as those existing in Bulgaria, supported a sense of pessimism and uncertainty about moving forward economically, then the simulation model that produces outcomes that are more negative and uncertain has more face validity.

The premise of the model as a comparison of base and fuzzy systems dynamics models for best fit decision making within a transition economy, appears to support the use of fuzzy sets. Since the transition economy being modeled contains high levels of vagueness, the fuzzy model better captures the risks involved and identifies risky outcomes. Although our conversations with our Bulgarian colleagues suggest that managers in transition economies seek global markets much like mangers operating in free market economies, a degree of over optimism may best be tempered by the wider range of possible outcomes and the higher probability for lower returns identified by the fuzzy set based systems dynamic model. Rational decision making occurs when confronted with worst, as well as best case scenarios to handle uncertainty.

Table 6  
Wider fuzzy model results

<table><tr><td></td><td>End balance (after 6 years)</td><td>End bal</td><td>End bal</td><td>Market share</td><td>Market share</td></tr><tr><td>Model</td><td>μ (mean)</td><td>Pr{&lt;0}</td><td>Pr{&lt;1,000,000)</td><td>Low</td><td>High</td></tr><tr><td>Fuzzy (triang.)</td><td>1,407,749–1,094,282 τo 5,993,370</td><td>0.250</td><td>0.480</td><td>0.20, 0 to 0.61</td><td>0.17, 0 to 0.28</td></tr><tr><td>Wide fuzzy</td><td>311,030–1,168,581 τo 5,339,889</td><td>0.520</td><td>0.728</td><td>0.09, 0 to 0.52</td><td>0.11, 0 to 0.30</td></tr></table>

## 10. Future research

Another point for consideration is that the fuzzy input obtained from a group of people will likely result in even wider ranges for input parameters due to natural differences of opinion, suggesting an even more pessimistic set of results based on group opinions. A hypothesis for future in-depth research is that the larger the group membership, the wider the range (possibly related to some root of the number of group members, similar to the central limit theorem).

Preliminary to this hypothesis, investigation into the fuzzy model versus a similar model with wider ranges for maximum and minimum values was conducted, with inputs shown in Table 5.

Based upon these results, support for the fuzzy set model may be further supported by a triangular function with wider ranges (Table 6).

Future research will continue this investigation by derivation of fuzzy probability distributions for each input value rather than assumption of triangular functions approximating a normal distribution. Transition to more rigorous simulation packages will be undertaken and results compared.

## Acknowledgements

The authors acknowledge the input of our Bulgarian colleagues: Maria Andreeva, Tsenov Academy of Economics; Paraskeva Dimitrova-Davidova, Bulgarian Academy of Sciences, Institute of Economics; Radoslav M. Gabrovsky, Tsenov Academy of Economics; Anastasiya Marcheva, Tsenov Academy of Economics; Ivan Martchevski, Tsenov Academy of Economics; Agop Sarkisyan, Tsenov Academy of Economics, Ivan Stoykov, Bulgarian Academy of Sciences, Institute of Economics; and our U.S. colleagues: Richard Alo, University of Houston-Downtown, Patrick O. Bobbie, Southern Polytechnic State University of Georgia; Ratan Guha, University of Central Florida; and Gary

B. Jackson, University of Houston-Downtown, who participated in NSF Award No. INT-0207141.

## References

[1] N.P. Archer, G.O. Wesolowsky, A dynamic service quality cost model with word-of-mouth advertising, European Journal of Operational Research 78 (1994) 355– 366.

[2] S. Beer, Brain of the Firm, Penguin Press, Harmondsworth, England, 1967.

[3] R.E. Bellman, L.A. Zadeh, Decision making in a fuzzy environment, Management Science 17 (1970) B141 – B164.

[4] P. Checkland, Systems Thinking, Systems Practice, John Wiley and Sons, Chicester, 1984.

[5] N. Choucri, R. Berry, Sustainability and diversity of development: toward a generic model, System Dynamics Proceedings 1 (1995) 30– 39.

[6] R.G. Coyle, System Dynamics Modeling: A Practical Approach, Chapman and Hall, London, 1996.

[7] H.J. Einhorn, R. Hogarth, Ambiguity and uncertainty in probabilistic inference, Psychological Review (1985) 433 – 461.

[8] J.R. Evans, D.L. Olson, Introduction to Simulation and Risk Analysis, 2nd ed., Prentice Hall, Upper Saddle River, NJ, 2002.

[9] J.W. Forrester, Industrial Dynamics, The MIT Press, Cambridge, MA, 1961.

[10] J.W. Forrester, World Dynamics, Wright-Allen Press, Cambridge, MA, 1971.

[11] A. Gregoriades, B. Karakostas, Unifying business objects and system dynamics as a paradigm for developing decision support systems, Decision Support Systems 37 (2004) 307– 311.

[12] R. Jain, A procedure for multiple aspects decision making using fuzzy sets, International Journal of Systems Science 8 (1977) 1 –7.

[13] D. Kahneman, A. Tversky, Prospect theory: an analysis of decision under risk, Econometrica (1979) 263– 291.

[14] D. Kahneman, A. Tversky, The psychology of preferences, Scientific American 39 (1982) 136– 142.

[15] G. Klir, B. Yuan, Fuzzy Sets and Fuzzy Logic, Prentice-Hall, Upper Saddle River, NJ, 1995.

[16] P. Mandal, A. Howell, A.S. Sohal, A systemic approach to quality improvements: the interactions between the technical, human and quality systems, Total Quality Management 9 (1) (1998) 79–100.

[17] G.P. Richardson, A.L. Pugh, Introduction to System Dynamics: Modelling with DYNAMO, MIT Press, Cambridge, MA, 1981.

[18] L. Rizzi, F. Bazzana, N. Kasabov, M. Fedrizzi, L. Erzegovesi, Simulation of ECB decisions and forecast of short term Euro rate with an adaptive fuzzy expert system, European Journal of Operational Research 145 (2003) 361– 381.

[19] J. Sterman, Business Dynamics: Systems Thinking and Modeling for a Complex World, Irwin/McGraw-Hill, Boston, 2000.

[20] The World Bank, Transition: The First Ten Years, Analysis and Lessons for Eastern Europe and the Former Soviet Union, The World Bank, Washington, DC, 2002.

[21] L. von Bertalanffy, General System Theory: Foundations, Development, Applications, George Braziller, New York, 1968.

[22] R. Yager, A general approach to decision making with evidential knowledge, in: L.N. Kamal, J.F. Lemmer (Eds.), Uncertainty in Artificial Intelligence, North Holland, Amsterdam, 1986, pp. 317–327.

[23] L. Zadeh, Fuzzy sets, Information and Control 8 (1965) 338– 353.

[24] L.A. Zadeh, Outline of a new approach to the analysis of complex systems and decision processes, IEEE Transactions on Systems, Man and Cybernetics MC 3 (1973) 38 – 45.

[25] L.A. Zadeh, Fuzzy sets as a basis for a theory of possibility, Fuzzy Sets and Systems 1 (1978) 3 – 28.

[26] L.A. Zadeh, A simple view of the Dempster–Shafer theory of evidence and its implication for the rule of combination, The AI Magazine (1986) 85–90.

[27] H. Zimmerman, Fuzzy Set Theory—And Its Applications, Kluwer Academic Publishers, Massachusetts, USA, 1996.

![](/api/attachments/TBAU443K/fulltext/images/5302e135fdcfed1e08321aa6346b9630a89084936f31f30346e28ed107d4253d.jpg)

David L. Olson is the James and H.K. Stuart Professor in MIS and Othmer Professor at the University of Nebraska. He has published research in over 60 refereed journal articles, primarily on the topic of multiple objective decision making, has authored or coauthored nine books (five in multiple editions), and has made over 100 presentations at international and national conferences on research topics. He is a member of the Association for

Information Systems, the Decision Sciences Institute, the Institute for Operations Research and Management Sciences, and the Multiple Criteria Decision Making Society. He is a Fellow of the Decision Sciences Institute.

![](/api/attachments/TBAU443K/fulltext/images/76b136034a4a4ad2f026a1f81106e2ca36a987442eab1da9e96abc5eae02e6ee.jpg)

Margaret F. Shipley is Professor of Management at the University of Houston-Downtown (UHD) in Houston, TX, USA. Dr. Shipley’s primary research interests are multicriteria decision making, project management, entrepreneurship/small business management, and quality management. Her work has involved the use of fuzzy logic in the decision making process. She has published in numerous journals in management science and oper-

ations research. She is the coauthor of Cases in Operations Management and the accompanying Instructor’s Resource for the casebook. She is the recipient of the UHD Scholarly and Creativity Award, and the Dean’s Award for Faculty Excellence. She is a past officer of the Institute for Operations Research and Management Science (INFORMS) College of Technology and Engineering Management.

Madeline Johnson is a Professor of Marketing at the University of Houston Downtown. She received a PhD from the University of Houston and a JD from the University of Texas. She has published in the Journal of Advertising, Journal of Public Policy and Marketing, and Qualitative Market Research: An International Journal.

Nikola Yankov is Director of the Institute for Academic Research and Professor of Planning and Marketing at the D. Tsenov Academy of Economics in Svishtov, Bulgaria. Dr. Yankov also serves as the Marketing Coordinator for the Masters Program. In addition to his teaching expertise, he is experienced in practical winery operations.
