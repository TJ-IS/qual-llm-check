---
otero_id: 15022
otero_key: "B7HDHPNW"
title: "Machine learning the harness track: Crowdsourcing and varying race history"
authors: "Robert P. Schumaker"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.013"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Machine learning the harness track: Crowdsourcing and varying race history

Robert P. Schumaker

Management Information Systems, Central Connecticut State University, New Britain, CT 06050, USA

## a r t i c l e i n f o

Article history: Received 29 September 2011 Received in revised form 9 November 2012 Accepted 4 December 2012 Available online 28 December 2012

Keywords: Business intelligence Data mining Support Vector Regression Harness racing S&C Racing system Crowdsourcing Dr. Z System

## a b s t r a c t

Racing prediction schemes have been with mankind a long time. From following crowd wisdom and betting on favorites to mathematical methods like the Dr. Z System, we introduce a different class of prediction system, the S&C Racing system that derives from machine learning. We demonstrate the S&C Racing system using Support Vector Regression (SVR) to predict <sup>fi</sup>nishes and analyzed it on <sup>fi</sup>fteen months of harness racing data from North<sup>fi</sup>eld Park, Ohio. We found that within the domain of harness racing, our system outperforms crowds and Dr. Z Bettors in returns per dollar wagered on seven of the most frequently used wagers: Win \$1.08 return, Place \$2.30, Show \$2.55, Exacta \$19.24, Quiniela \$18.93, Trifecta \$3.56 and Trifecta Box \$21.05. Furthermore, we also analyzed a range of race histories and found that a four race history maximized system accuracy and payout. The implications of this work suggest that an informational inequality exists within the harness racing market that was exploited by S&C Racing. While interesting, the implications of machine learning in this domain show promise.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Prediction, the art of divining future events has always had a certain appeal. From the earliest of times, man casts lots to determine outcomes. Within these early times, lots<sup>1</sup> of sticks and pebbles were given interpretations where an even number indicates a positive outcome and an odd number was viewed as negative. Gradually these divinations grew more complex with rituals, sacri<sup>fi</sup>ce and complicated interpretations [16].

Today, the grip of prediction still has its appeal with gamblers and academics alike. While no longer considered an art but more of a science, prediction and probability are better understood, but are still complex by design. The most dif<sup>fi</sup>cult aspect of prediction rests within identifying the most relevant parameters. Critical parameters are sometimes dif<sup>fi</sup>cult to identify/measure, are constantly changing or may not have been fully explored. The inability to correctly identify the most relevant parameters can sometimes lead to crippled systems relying on unimportant data, or worse, not based on sound science (e.g., basing predictions on the color of a horse).

Racing, like so many other domains including the stock market, trades on information. In harness racing it is assumed that all relevant information is public. Therefore everyone should have a fair chance of achieving success. Instead, what has been found is that information markets all have inequalities within them, either through withheld information or a human tendency to discount certain information or weight it incorrectly. These informational inequalities lead to arbitrage opportunities. The key to unlocking successful prediction rests on making unbiased decisions using measurable parameters of the most critical values.

To a large extent, individual bettors will base wagering decisions on a mixture of quantitative and qualitative methods as well as instinct. Before making a wager, a bettor will typically read all the information on the race card and gather as much information about the race participants as possible. They will also examine data concerning a horse's physical condition, how they have performed historically, breeding and bloodlines, trainer or owner, as well as odds of winning.

Automating this decision process and removing the biases using machine learning may yield as equally good results as greyhound racing, which is considered to be the most consistent and predictable form of racing [4]. Consistency lends itself well to machine learning algorithms that can learn patterns from historical data and apply itself to previously unseen racing instances. The mined data patterns then become a type of arbitrage opportunity where an informational inequality exists within the market. However, like other market arbitrages, the more it is exploited the less the expected returns, until the informational inequality returns the market to parity.

Our research motivation is to demonstrate a decision support system that can learn from historical harness race data and leverage the information arbitrage through its predictions. Since nothing of this nature has been performed before in harness racing, we ground ourselves in using similar techniques used in greyhound racing research and then compare our artifact against bettors and other successful wagering strategies; testing how well such a system performs.

The rest of this paper is as follows. Section 2 provides an overview of literature concerning prediction techniques, algorithms and common study drawbacks. Section 3 presents our research questions. Section 4 introduces the S&C Racing system and explains the various components. Section 5 sets up the experimental design. Section 6 is the experimental <sup>fi</sup>ndings and a discussion of implications. Finally Section 7 delivers the conclusions and limitations of this stream of research.

## 2. Literature review

Harness racing is a fast-paced sport where horses pull two-wheeled sulkies (e.g., carts) with jockeys inside. Quite popular in North America, there are 42 sanctioned USTA tracks mostly throughout the Midwest. Races are completed with two different gaits; pacing or trotting which has to do with leg positioning. In pacing, leg movements are laterally coordinated, the left side moves together and opposite of right side movement. In trotting, leg movement is coordinated diagonally. A majority of harness races are pacing races because of the faster speeds.

## 2.1. Predicting outcomes

Participants can use a wide variety of prediction techniques to divine potential race outcomes. Many of the techniques can be reduced to three major areas; market ef<sup>fi</sup>ciency, mathematics or data mining [20]. Market ef<sup>fi</sup>ciency focuses on the psychological aspects of a bettor and how motivations can lead to informational inequalities. While typically applied to stock markets where information inequalities can arise from public versus private information, the same concept can be applied to other information-centric markets. This area relies on using statistical tests, models of human behavior, historical forecasting and crowdsourcing.

A second branch of prediction techniques is that of mathematical models where problem sets of variables are reduced to a solvable model. Examples include using joint probabilities, the Dr. Z System and the mathematics of streaky behavior.

A third major branch of prediction techniques is data mining. In this branch, algorithms are harnessed to learn from historical data and gen eralize to new instances. Examples include performing simulations, using arti<sup>fi</sup>cial intelligence and machine learning algorithms [20].

## 2.1.1. Market efficiency

Market ef<sup>fi</sup>ciency is all about the movement and use of information within a tradeable environment. Market ef<sup>fi</sup>ciency includes the use of statistical tests, conducting behavioral modeling of trading activity and forecasting models of outcomes to create rules from observation [5]. Crowdsourcing, or using the wisdom of crowds, is another form of market ef<sup>fi</sup>ciency where groups of individuals perform forecasts on provided information and results are averaged for use as a predictive tool [26]. Since market ef<sup>fi</sup>ciency is such a broad <sup>fi</sup>eld, we constrain our discussion to the narrowly scoped domain of sports gaming.

In statistical testing, it is assumed that outcomes will mirror expectations and no betting strategy should win in excess of 52.4% provided that all participants share the same information [5]. Deviations from these expectations could indicate the introduction of new or privately held information.

In behavioral models, bettor biases are tested to determine predictable decision-making tendencies. Perhaps the best known behavioral model is the longshot bias where a bettor will over-value horses with higher odds to offset losses [15]. Gamblers tend to favor the low probability, high payout combinations for luck, entertainment or desperation, but it has never been found to yield sustainable positive returns on combination bets [8]. It has been argued that betting on favorites should be as pro<sup>fi</sup>table as betting on longshots [24], however in practice this is not the case. The longshot bias is not constrained to one particular sport and has been observed in boxing, cricket, horse racing, snooker and tennis [2].

Another market ef<sup>fi</sup>ciency tool is forecasting where models of historical data (e.g., seasonal averages, basic statistics and prior outcomes)

are extrapolated and tested against current data [5]. This technique was found to be too simplistic and a poor predictor of future activity.

Crowdsourcing is another tool of market ef<sup>fi</sup>ciency where an average of crowd forecasts is used to predict future events [26]. In harness racing, this behavior translates into betting on the favorites. This technique has been found to be fairly accurate and a reliable indicator of expectations. In a study of UFC <sup>fi</sup>ghts, crowds were able to better predict wins (85.7%) than bookies (67.6%) [30]. In a study of German Premier League soccer, crowds were found to be more accurate than bookies [25]. In a study of FIFA World Cup 2006, crowds were better able to predict winners than rankings or random chance [13]. Although crowdsourcing has been shown to be an effective prediction tool, critics maintain that it could be susceptible to the free-riders problem where certain bettors may simply follow the crowd favorite themselves rather than evaluate the data independently [17]. This could lead to an over-emphasis on the crowd favorite, more so than what the data should demand.

## 2.1.2. Mathematics

Mathematics in sports racing focuses on problem sets of observable variables and reducing them to a solvable model. It differs from market ef<sup>fi</sup>ciency where the focus is on market information (public, semipublic and private information) among participants. This branch of prediction techniques includes the Harville formulas, the Dr. Z System and streaky player performance [9].

Harville formulas [7] are a collection of equations that establish a rank order of <sup>fi</sup>nish by using combinations of joint probabilities [19]. It is believed that in certain instances the odds can be over-estimated on favorites leading to an arbitrage opportunity.

A derivative work of the Harville formulas is the Dr. Z System. In this system, a potential gambler is leveraging odds over-estimation by waiting 2 min before the race and making Place wagers (i.e., the horse will <sup>fi</sup>nish in 2nd place or better) on those with a win frequency to place frequency greater than or equal to 1.15 and betting Show (i.e., the horse will <sup>fi</sup>nish in 3rd place or better) on races with a win to show frequency greater than or equal to 1.15 [31]. This system proved successful during the 1980s and received considerable attention from academics and gamblers alike. Follow-up studies later found that bettors were effectively arbitraging the tracks (over-using the system) and any opportunity for gain using Dr. Z was mitigated [18].

In streaky behavior, player performance is analyzed for the so-called “hot-hand” effect to determine if recent player performance in<sup>fl</sup>uences current performance [27]. The belief is that a player performing statistically better than average, will continue to do so in the near future. While Tversky and Gilovich studied the phenomenon in basketball and did not <sup>fi</sup>nd evidence of streaky behavior [27], academics studying baseball found just the opposite. In a study modeling baseball player performance, it was found that certain players exhibit signi<sup>fi</sup>cant streakiness, much more so than what probability could allow [1].

## 2.1.3. Data mining

While mathematics and statistics are the underlying foundation of data mining, they are very different from one another. Statistics are typically used to identify an interesting pattern in a signal and allow for theory testing of hypotheses on known relations [14]. Without knowing what to look for, researchers using statistics alone cannot explain an observed relationship; that is the purpose of data mining [22]. As an example, a particular baseball batter may have a substantial batting average. Statistics can tell us the value but not answer why that is the case. If we knew what we were looking for, or embarking upon an exploratory analysis of the data, we may arrive at the elevated batting average on a 3–2 pitch count with 2 outs and runners in scoring position while facing a left-handed pitcher. Data mining can identify this important nugget from the data, but statistics would require manual iteration and an idea of what to look for in order to arrive at the same conclusion. Therefore it could be said that data mining provides more explanatory power than statistics. Data mining can be broken into three areas; Simulations, Arti<sup>fi</sup>cial Intelligence and Machine Learning.

Statistical simulations involve the imitation of new game data by using historical data as a reference. Once constructed, the simulated play can be compared against actual game play to determine the predictive accuracy of the simulation. Entire seasons can be constructed to test player substitution or the effect of player injury.

Arti<sup>fi</sup>cial Intelligence differs from other methods by applying a heuristic algorithm to the data. This approach attempts to balance out statistics by implementing codi<sup>fi</sup>ed educated guesses to the problem in the form of appropriate rules or cases. Heuristic solutions may not be perfect, however, the solutions generated are considered adequate [22].

The third area, machine learning, uses algorithms to learn and induce knowledge from the data [3,6]. Examples of these algorithms include both supervised and unsupervised learning techniques such as genetic algorithms, neural networks and Bayesian methods. These techniques can iteratively identify previously unknown patterns within the data and add to our understanding of the composition of the dataset [22]. These systems are better able to generalize the data into recognizable patterns [12].

Neural networks are widespread within sport prediction studies. With neural networks, dataset patterns are learned and hidden trends can be exploited for a competitive advantage. Other machine learning techniques include genetic algorithm, the ID3 decision tree and the regression-based variant of the Support Vector Machine (SVM) classi-<sup>fi</sup>er, called Support Vector Regression (SVR) [28]. SVM is a classi<sup>fi</sup>cation algorithm that seeks to maximally separate high dimension data while minimizing <sup>fi</sup>tting error. This technique was used in a similar context to predict stock prices from <sup>fi</sup>nancial news articles [23] and credit ratings [10]. Within these studies, it was found that the SVR algorithm was able to exploit arbitrage opportunities that were the result of market inef<sup>fi</sup>ciencies with respect to the information present.

## 2.2. Racing prediction studies

Predictive algorithms have been adopted successfully in nontraditional sports, such as greyhound and thoroughbred racing. These types of predictions generally involve machine learning techniques to train the system on the various data components, feed in new data and then extract predictions from it. The highlights of several studies are presented below.

## 2.2.1. Neural networks and ID3

In a prior study of greyhound races, Chen et al. tested an ID3 and Back Propagation Neural Network (BPNN) on 100 races at Tucson

![](/api/attachments/B7HDHPNW/fulltext/images/47ec75e3eb87ab74bb790d9b86079c79a6094956f58cc43354abbc57c8fbc3be.jpg)  
Fig. 1. The S&C Racing system.

Greyhound Park [4]. They further limited themselves to ten racerelated variables over a seven race history. These ten race-related variables on a seven race history were given to Chen et al. by greyhound domain experts and were never systematically explored to ensure a maximal return.

In Chen et al.'s work they made binary decisions as to whether or not each greyhound would win based on historic race data (Win versus not Win). If a dog was predicted to <sup>fi</sup>nish <sup>fi</sup>rst (Win), the system would make a \$2 wager. Their ID3 decision tree was accurate 34% of the time with a \$69.20 payout while the BPNN was 20% accurate with a \$124.80 payout. This disparity in decreased accuracy and increased payout is justi<sup>fi</sup>ed by arguing that the BPNN was selecting longshot winners. By doing so, accuracy would decrease but higher payouts could be gained because of the longer odds. When comparing machine learning techniques to track experts, the experts managed a dismal 18% accuracy with a payout loss of \$67.60. It was speculated that the system was taking advantage of informational inequalities by successfully selecting longshot wagers more often than chance, however, given the black-box nature of BPNN, it is hard to be certain.

## 2.2.2. Neural networks and betting engines

In a follow-up study that took Chen et al.'s variables and expanded them to 18, Johansson and Sonstrod also used a BPNN but also investigated the effect of more exotic wagers such as Quiniela (i.e., selecting the <sup>fi</sup>rst two dogs to <sup>fi</sup>nish in any order) and Exacta (i.e., selecting the <sup>fi</sup>rst two dogs to <sup>fi</sup>nish in order) [11]. Their study on 100 races at Gulf Greyhound Park in Texas found 24.9% accuracy for Wins and a \$6.60 payout loss. This seemingly improved accuracy came at the cost of decreased payout as compared to Chen et al. and would imply that either the additional variables or too few training cases (449 as compared to Chen's 1600) hampered the ability to identify longshots. However, exotic wagers did better. Quinielas had 8.8% accuracy with a \$20.30 payout, while Exacta had 6.1% accuracy with a \$114.10 payout.

## 2.2.3. Discrete prediction

In another study that focused on using discrete numeric prediction rather than binary assignment, Schumaker and Johnson used Support Vector Regression (SVR) on Chen et al.'s 10 performance-related variables [21]. Their study of 1953 greyhound races across the US managed a 45.35% Win accuracy with a \$75.20 payout. To maximize payout, AZGreyhound had 23.00% Win accuracy with a \$1248.40 payout. They found the same tradeoff between accuracy and payout

## 2.2.4. Neural networks on thoroughbreds

In a study of thoroughbred racing, Williams and Li measure 8 race performance variables on 143 races and built a BPNN for each horse that raced [29]. This differed from other BPNN studies that created one network for all races. The system did manage 74% accuracy in selecting a winner.

## 2.3. Research gaps

From our investigation, we noticed several gaps in the literature. The <sup>fi</sup>rst of which is a lack of machine learner study within the domain of harness racing. Although there are a scant few studies within the related race areas of greyhound and thoroughbred racing, harness racing may be similar enough that techniques used in similar domains can be ported to harness racing.

Another gap was a lack of study of machine learners versus the wisdom of crowds. Several studies offered insight between crowds and experts, but none could be found that explored how well a machine learning platform could perform versus crowd wisdom. Perhaps a machine learning algorithm can <sup>fi</sup>nd patterns that others miss.

A third gap was that nearly every racing study discussed has relied on the ten race-related variables and a seven race history which was derived from an interview of human domain experts in Chen et al. [4].

The use of these ten variables and seven race history has never been examined to our knowledge to determine if they are ideal. We take this opportunity to investigate what amount of race history can lead to optimal results and why.

## 3. Research questions

From our analysis we propose the following research questions.

♦ Can a Machine Learner predict Harness races better than established prediction methods?

Crowdsourcing and Dr. Z methods have been well established within the racing domain. However, both of these methods are susceptible to human biases and risk avoidance tendencies. Machine learning is devoid of these human characteristics and should be able to outperform the established prediction methods in a bias-free decision-making environment.

♦ How important is race history to a machine learner?

Prior research has almost exclusively relied upon a seven race history to make predictions. We question whether this amount of race history is optimal within the harness racing domain. Perhaps a differing amount of race history will provide better performance.

♦ What wager combinations work best and why?

Most prior studies were <sup>fi</sup>xated on Win-only wagers. While Win is still an important aspect in sports wagering, perhaps wagers on Place and Show may be more pro<sup>fi</sup>table. Likewise, more exotic wagering types might hold some promise as well. By looking at maximizing the return per wager, we can <sup>fi</sup>nd the answer.

## 4. System design

To address these research questions, we built the S&C Racing system shown in Fig. 1.

The S&C Racing system consists of several major components: a web scraper/parser to gather the online odds and race history from race programs, the machine learning tool that takes different models and learns the patterns, a betting engine to make different wagers and evaluation metrics to measure system performance. For odds data, harness track odds are pari-mutuel where the track sets the odds to balance the amount of money transfer from losing to winning wagers, minus a commission. Thus if a particular horse is the favorite and is heavily bet upon, the odds are decreased, which decreases payout. To offset favorite betting, the track will increase odds on less favored horses to give bettors an incentive to wager longshots.

These odds are made for a variety of wagers aside from just Win where the bettor receives a payout only if the selected horse comes in <sup>fi</sup>rst place. Place produces two differing payouts depending upon whether the selected horse comes in either <sup>fi</sup>rst or second place. A Show bet has three differing payouts that depend on whether the selected horse comes in <sup>fi</sup>rst, second or third place. These differing payouts are dependent upon the odds of each <sup>fi</sup>nish. For exotic wagers, an Exacta bet receives a payout by successfully picking both the <sup>fi</sup>rst and second place horse. A Quiniela wager is like an Exacta except the order of <sup>fi</sup>nish does not matter, only that the selected two horses <sup>fi</sup>nish within the top two spots. Trifecta, or Trifecta Straight, is where the bettor wagers on the <sup>fi</sup>rst three horses, in order. For a Trifecta Box wager, the bettor still wagers on the <sup>fi</sup>rst three horses, but the order does not matter as long as all three <sup>fi</sup>nish within the top 3 spots.

![](/api/attachments/B7HDHPNW/fulltext/images/ef38a9506b8766ef6e42472097e3bd446c936c61e5edb4a969ca9eda11e0094c.jpg)  
Fig. 2. Support Vector Machine.

Table 1 Miss HKB data.

<table><tr><td>Fastest time</td><td>119.56</td></tr><tr><td>Win percentage</td><td>14.29%</td></tr><tr><td>Place percentage</td><td>42.86%</td></tr><tr><td>Show percentage</td><td>14.29%</td></tr><tr><td>Break average</td><td>5.14</td></tr><tr><td>Finish average</td><td>2.71</td></tr><tr><td>Time7 average</td><td>120.19</td></tr><tr><td>Time3 average</td><td>119.90</td></tr><tr><td>Predicted finish</td><td>2.9259</td></tr></table>

The other system input is the race program which contains historical performance data on each horse. There are generally 14 races per program where each race averages 8 or 9 entries. Each horse has speci<sup>fi</sup>c data such as name, driver, trainer, color, sire and dam. Race-speci<sup>fi</sup>c information includes gait (pacing versus trotting), race date, track, fastest time, break position, quarter-mile position, stretch position, <sup>fi</sup>nish position, lengths won or lost by, average run time and track condition.

From this data we create speci<sup>fi</sup>c models to train the S&C Racing system. The system is tested with different wagers and results are tested along three dimensions of evaluation: accuracy, payout and ef<sup>fi</sup>ciency. Accuracy is the number of winning bets divided by the number of bets made. Payout is the monetary gain or loss derived from the sum of wagers. Ef<sup>fi</sup>ciency is the payout divided by the number of bets.

## 5. Experimental design

For our collection we automatically gathered data of prior race results and wager payouts at North<sup>fi</sup>eld Park; a USTA sanctioned harness track outside of Cleveland, Ohio. We further chose a study period of October 1, 2009 to December 31, 2010 and divided it into two periods; training (October 1, 2009 to September 30, 2010) and testing (October 1, 2010 to December 31, 2010). Fifteen months were selected because it gave us a comparable amount of training races/cases as prior studies. In all, we gathered 2558 useable training cases covering 309 races and tested our system on 91 testing races covering 770 testing cases. By comparison, Chen et al. [4] used 1600 training cases from Tucson Greyhound Park, Johansson and Sonstrod [11] used 449 training cases from Gulf Greyhound Park in Texas and Schumaker and Johnson used 41,473 training cases from across the US.

Part of the challenge in constructing this system was in maintaining consistency with Chen et al.'s approach which required a race history of the prior seven races. Each usable race needed a complete 7 race history of each horse participating, otherwise the entire race was discarded. Since new entries would arrive in the North<sup>fi</sup>eld market frequently, only a portion of all races during this period could meet our stringent requirement.

Table 2 Predicted values.

<table><tr><td>Horse name</td><td>Predicted finish</td></tr><tr><td>Miss HKB</td><td>2.9259</td></tr><tr><td>B B Big Girl</td><td>3.9036</td></tr><tr><td>Friendly Kathy</td><td>4.3016</td></tr><tr><td>ShadyPlace</td><td>5.2731</td></tr><tr><td>St Jaded Strike</td><td>5.7243</td></tr><tr><td>Honey Creek Abby</td><td>5.7831</td></tr><tr><td>Mad Cap</td><td>5.9335</td></tr><tr><td>Pamela Lou</td><td>6.5066</td></tr><tr><td>Winning Yankee</td><td>6.8589</td></tr></table>

Following the work of Chen et al. [4], we limited ourselves to the following eight variables over a seven race history (two of Chen et al.'s original 10 variables could not be used because they are speci<sup>fi</sup>c to greyhound race grades which have no equivalent in harness racing):

♦ Fastest Time—horse's time in the previous race

♦ Win Percentage—the number of wins divided by the number of races ♦ Place Percentage—the number of places divided by the number of races

♦ Show Percentage—the number of shows divided by the number of races

♦ Break Average—the horse's average position out of the starting gate

♦ Finish Average—the horse's average <sup>fi</sup>nishing position

♦ Time7 Average—the average <sup>fi</sup>nishing time over the last 7 races

♦ Time3 Average—the average <sup>fi</sup>nishing time over the last 3 races.

## 5.1. Machine learning

For our machine learning component we used Support Vector Machines (SVM). SVM is a machine learning classi<sup>fi</sup>er that attempts to maximally separate the classes by computing a hyperplane equidistant from the edges of each class [28], as shown in Fig. 2.

Aside from dividing classes, the hyperplane can also be used as a regression estimate where independent variables are projected onto the hyperplane in order to derive the dependent variable. This variation of SVM is called Support Vector Regression (SVR) which allows for a continuous numeric prediction instead of classi<sup>fi</sup>cation. This allows us the freedom to rank predicted <sup>fi</sup>nishes rather than perform a win/lose classi<sup>fi</sup>cation.

As an example of how the system works once it has been trained, each horse in the testing set is given a predicted <sup>fi</sup>nish position by the SVR algorithm. Looking at the horse Miss HKB on Oct. 8, 2010 in race 4, we compute the variables for the prior seven races as shown in Table 1.

For this particular race, Miss HKB has a Fastest Time value of 119.56 which is the time in the last race. Miss HKB has a Win percentage of 14.29%, a Place percentage of 42.86% and a Show percentage of 14.29% indicating how often they <sup>fi</sup>nish in each of those positions. The Break

![](/api/attachments/B7HDHPNW/fulltext/images/0c49083859c13efcf0d6ba5159076db6354c50ee9d16a62ad9bee5e7c5481be5.jpg)

![](/api/attachments/B7HDHPNW/fulltext/images/42830148c137f1e275c058d740df7967f2abbdd4ff8468a79dee52d333e4430b.jpg)  
Fig. 3. S&C Racing for traditional wagers (7 race history).

Table 3  
Comparing established methods in traditional wagers (7 race history)

<table><tr><td rowspan="2"></td><td colspan="3">Accuracy</td><td colspan="3">Payout</td></tr><tr><td>Win</td><td>Place</td><td>Show</td><td>Win</td><td>Place</td><td>Show</td></tr><tr><td>S&amp;C Racing</td><td>18.75%(3.4)</td><td>83.33%(2.7)</td><td>100.0%(2.7)</td><td>—$4.80(3.6)</td><td>$50.70(4.0)</td><td>$168.60(5.6)</td></tr><tr><td>Crowdsourcing</td><td>41.67%</td><td>65.63%</td><td>73.96%</td><td>$46.60</td><td>$115.00</td><td>$119.90</td></tr><tr><td>Dr. Z Bettors</td><td></td><td>24.43%</td><td>36.59%</td><td></td><td>—$44.10</td><td>$72.60</td></tr><tr><td>Random chance</td><td>11.82%</td><td>23.64%</td><td>35.45%</td><td>—$431.20</td><td>—$143.60</td><td>$119.50</td></tr></table>

Average is 5.14 meaning that this horse is typically in the middle to the back of the pack coming out of the gate. The Finish Average is 2.71 indicating plenty of second and third place <sup>fi</sup>nishes. The Time7 Average shows that over the past seven races, Miss HKB has had an average time of 120.19 s. The impressive Time3 Average of 119.90 indicates speed improvement in the last three races. S&C Racing predicts from its internal model that Miss HKB should <sup>fi</sup>nish 2.9259 which is a good <sup>fi</sup>nish, but cannot be fully interpreted until compared with the predicted <sup>fi</sup>nishes of other horses in the race. The lower the predicted <sup>fi</sup>nish number, the stronger the horse is expected to be and the predicted <sup>fi</sup>nish value is independent of the other horses in the race. As a visual aid, Table 2 shows the race output for North<sup>fi</sup>eld Park's race 4 on October 8, 2010.

From this table, we can wager on Miss HKB to win, B B Big Girl to place and Friendly Kathy to show based on S&C Racing's predicted <sup>fi</sup>nish.

## 5.2. S&C betting engine

Once we have the predicted <sup>fi</sup>nishes, we pass operations to the betting engine to make the appropriate wagers. In order to interrogate the betting engine and avoid having it wager on every race, we performed a sensitivity analysis by introducing a variable cutoff that ranges from 1 to 8 and is incremented by 0.1. The betting engine is then limited to wagering on races in which the strongest predicted <sup>fi</sup>nish exceeds the cutoff. Given our previous example of Table 2, if the predicted <sup>fi</sup>nish cutoff variable was 2.9, no wagers would be made as Miss HKB has a higher predicted <sup>fi</sup>nish of 2.9259. If we increment the cutoff to 3.0, now Miss HKB is under the cutoff and this race can be wagered upon.

![](/api/attachments/B7HDHPNW/fulltext/images/9583f2766f0a0390307a7a0aa8fec2b8cccf0e083f67212afbb7a95e510f02a1.jpg)

![](/api/attachments/B7HDHPNW/fulltext/images/01632f020feb9ebf43c42fac444f3762eb28ae2c613ef38d3d777b8a83f8ba85.jpg)  
Fig. 4. S&C Racing for exotic wagers (7 race history).

Comparing Established methods in exotic wagers (7 race history).

<table><tr><td rowspan="2"></td><td colspan="4">Accuracy</td><td colspan="4">Payout</td></tr><tr><td>Exacta</td><td>Quiniela</td><td>Trifecta</td><td>Trifecta Box</td><td>Exacta</td><td>Quiniela</td><td>Trifecta</td><td>Trifecta Box</td></tr><tr><td>S&amp;C Racing</td><td>3.23% (3.6)</td><td>37.50% (2.9)</td><td>1.28% (4.6)</td><td>3.70% (4.7)</td><td>$55.60 (3.6)</td><td>$76.80 (3.6)</td><td>-$6.00</td><td>-$36.00</td></tr><tr><td>Crowdsourcing</td><td>15.38%</td><td>26.37%</td><td>8.79%</td><td>19.78%</td><td>$25.40</td><td>$56.00</td><td>$181.00</td><td>$380.40</td></tr><tr><td>Random chance</td><td>1.58%</td><td>2.79%</td><td>0.25%</td><td>1.47%</td><td>-$1412.40</td><td>-$1428.60</td><td>-$1517.40</td><td>-$4945.20</td></tr></table>

Measures are then taken of prediction accuracy, payout and betting ef<sup>fi</sup>ciency of each wager for each increment. We feel that this type of analysis provides a clearer understanding of performance data than a single value could.

## 5.3. Crowdsourcing, Dr. Z and random chance

In order to best compare the S&C Racing results, we compare them against established prediction methods of crowdsourcing, Dr. Z Bettors and random chance. For the crowdsourcing comparison we use pre-race odds where the crowd favorite, the animal with the lowest odds, was selected and wagered upon. For Dr. Z Bettors, Place wagers (betting the animal comes in 2nd) were placed on animals with win percentage to place percentage ratios greater than or equal to 1.15, and Show wagers (betting the animal comes in 3rd) were placed with win percentage to show percentage ratios greater than or equal to 1.15. For random chance, a random animal is selected and wagered upon for each race.

## 6. Experimental <sup>fi</sup>ndings and discussion

## 6.1. Evaluating a seven race history

To answer our <sup>fi</sup>rst research question of can a machine learner predict harness races better than established prediction methods we present Fig. 3a that looks at accuracy through Chen et al. variables (7 race history) for the three wager types and compares it to established prediction methods in Table 3.

From our data, Win maxed out at 18.75% at a predicted <sup>fi</sup>nish of 3.4 or better. Place maxed out at 83.33% at a predicted finish of 2.7 or better and Show maxed out at 100.0% accuracy at a predicted <sup>fi</sup>nish of 2.7 or better

Comparing S&C Racing to the established prediction methods of Crowdsourcing, Dr. Z Bettors and random chance; S&C Racing underperformed Crowdsourcing on Win (18.75% to 41.67%), but outperformed Crowdsourcing Place (83.33% to 65.63%) and Show (100.0% to 73.96%) (p-values b0.1 and b0.05 respectively). S&C Racing also outperformed Dr. Z Bettors (p-values b0.01) and random chance (p-value b0.1 for Win, b0.01 for Place and Show).

Looking at just S&C Racing and Crowdsourcing, both methods increased accuracy when wagering on lower placed <sup>fi</sup>nishes (i.e.; moving from Win to Place to Show). This was expected behavior because wagering on these <sup>fi</sup>nishes will still garner a payout and count towards accuracy totals if the animal <sup>fi</sup>nishes at or higher than the <sup>fi</sup>nish wagered upon (as evidenced by random chance). However, S&C Racing exhibited a superior curve in predicting accuracy through the lower placed <sup>fi</sup>nishes. Our intuition is that Crowdsourcing was much more ef<sup>fi</sup>ciently optimizing for Win, perhaps through knowledge external to the system, yet was overtaken by S&C's ef<sup>fi</sup>ciency when it came to non-win traditional wagers which may imply that S&C Racing is taking advantage of an arbitrage opportunity.

While the results are showing that S&C Racing is performing at least as well as other prediction methods in terms of accuracy, Fig. 3b looks at how well S&C Racing compares in terms of wagering payout.

From this data, Win performed poorly in terms of payout, and minimized its losses at (\$4.80). Place and Show did better with maximized returns of \$50.70 and \$168.60 respectively. However, by comparison, S&C Racing Win and Place underperformed Crowdsourcing ( \$4.80 to \$46.60 and \$50.70 to \$115.00 respectively), while Show outperformed (\$168.60 to \$119.90, p-valueb0.01). The S&C Racing wagers both outperformed Dr. Z Bettors and random chance (p-valuesb0.01 each). Again, returning to just S&C Racing and Crowdsourcing, payouts increase on the progression through the lower placed <sup>fi</sup>nishes which was not unexpected. For S&C Racing, Win started with a negative payout but by Show it exhibited a superior payout. This is further evidence that Crowdsourcing is better optimized on Win but is soon overtaken by S&C Racing.

![](/api/attachments/B7HDHPNW/fulltext/images/4e901b8e1de040d435973076800c0243c4397674f3d4a0d826ac0375bb4c933c.jpg)

b  
![](/api/attachments/B7HDHPNW/fulltext/images/287a7a30a1034d680888ce45a2fd01ec4095e9593aac7dc2518664ca69433a04.jpg)

C  
![](/api/attachments/B7HDHPNW/fulltext/images/79f7216d60958ee516a8fb8c93c3e7da902d5ddcb188e184688de9c8c0038597.jpg)

d  
![](/api/attachments/B7HDHPNW/fulltext/images/25d8f28922df5d412fe866e06d9daa76e69422965ba700d4afad92220595509a.jpg)  
Fig. 5. Examining wagers across race history.

Table 5  
Sum of maximized accuracies and payouts across all seven wagers.

<table><tr><td>Race history</td><td>Accuracy</td><td>Payout</td></tr><tr><td>1</td><td>339.03%</td><td>$1621.20</td></tr><tr><td>2</td><td>339.11%</td><td>$1603.50</td></tr><tr><td>3</td><td>353.07%</td><td>$861.10</td></tr><tr><td>4</td><td>353.09%</td><td>$4265.40</td></tr><tr><td>5</td><td>224.55%</td><td>$2424.60</td></tr><tr><td>6</td><td>215.03%</td><td>$1791.90</td></tr><tr><td>7</td><td>247.94%</td><td>$304.90</td></tr><tr><td>8</td><td>328.91%</td><td>$325.00</td></tr><tr><td>9</td><td>202.35%</td><td>$108.50</td></tr><tr><td>10</td><td>200.69%</td><td>$438.40</td></tr></table>

The values in bold represent maximum values.

In terms of exotic wagers, Fig. 4a shows the accuracy of S&C Racing's exotic wagers in comparison to the established predictors in Table 4.

From the data, S&C Racing's exotic wagers mostly underperformed Crowdsourcing in terms of accuracy, with the exception of Quiniela, 37.50% to 26.37% (p-valueb0.2). Versus random chance, only the combination wagers of Quiniela and Trifecta Box exhibited a statistically positive difference, 37.50% to 2.79% (p-valueb0.05) and 3.70% to 1.47% (p-valueb0.15) respectively. Although Exacta and Trifecta did exhibit a positive difference versus random chance counterparts, they were statistically equivalent.

Switching to exotic wager payouts, Fig. 4b shows us the four S&C Racing wagers on the <sup>fi</sup>eld of predicted horse strength. From this data, both Exacta and Quiniela outperformed the Crowdsourcing counterparts, \$55.60 to \$25.40 and \$76.80 to \$56.00 respectively (p-valuesb0.01). The wagers of Trifecta and Trifecta Box underperformed Crowdsourcing which was unexpected given S&C Racing's success at Exacta and Quiniela wagering. S&C Racing also outperformed random chance in all four wager types (p-valuesb0.01).

a  
![](/api/attachments/B7HDHPNW/fulltext/images/ccc1fae12262183c2d602acfa0be284a68d5c46baf548f3e2340b19d8578181b.jpg)

b  
![](/api/attachments/B7HDHPNW/fulltext/images/ba090ca4c26e0af50688629b362003044f68d82f80071e50be47d646a595ebb1.jpg)  
Fig. 6. S&C Racing for traditional wagers (4 race history).

Table 6  
Comparing established methods in traditional wagers (4 race history)

<table><tr><td rowspan="2"></td><td colspan="3">Accuracy</td><td colspan="3">Payout</td></tr><tr><td>Win</td><td>Place</td><td>Show</td><td>Win</td><td>Place</td><td>Show</td></tr><tr><td>S&amp;C Racing</td><td>37.50%(3.3)</td><td>75.00%(3.3)</td><td>100.0%(3.3)</td><td>$28.20(3.5)</td><td>$122.70(4.5)</td><td>$526.50(5.1)</td></tr><tr><td>Crowdsourcing</td><td>45.50%</td><td>69.00%</td><td>78.00%</td><td>$135.40</td><td>$257.80</td><td>$283.50</td></tr><tr><td>Dr. Z Bettors</td><td></td><td>23.53%</td><td>35.21%</td><td></td><td>$4.30</td><td>$103.90</td></tr><tr><td>Random chance</td><td>11.74%</td><td>23.47%</td><td>35.21%</td><td>—</td><td>—</td><td>$415.10</td></tr><tr><td></td><td></td><td></td><td></td><td>$813.20</td><td>$328.60</td><td></td></tr></table>

Looking at just S&C Racing and Crowdsourcing between Exacta and Quiniela, again we witness an increase in both Accuracy and Payout which is not unexpected given the better odds of a Quiniela wager versus Exacta. Again S&C Racing exhibits a superior curve between these two wagers versus Crowdsourcing. However, when it came to the Trifecta and Trifecta Box pair, S&C Racing posted dismal results. Taken together, the slow starts and poor performance on Trifecta straight and box, we are reminded that these results are based upon a seven race history handed down from greyhound racing. While the Time7 variable was given the most weight by the SVR algorithm and could be argued to be the most important of the eight input vari ables; we contemplate whether this seven race history is leading to calibration issues with S&C Racing and whether an alternative race history would provide better results.

## 6.2. Evaluating a four race history

To answer our second research question of how important is race history to a machine learner, we look at maximized accuracy across predictions using race histories of one to ten races, as shown in Fig. 5a and b, and maximized payouts as shown in Fig. 5c and d.

From these <sup>fi</sup>gures, if we were to take all seven wager accuracies together, we would <sup>fi</sup>nd that the four race history had the best performance (353.09%), albeit marginally, as shown in Table 5. Similarly, by looking at the maximized payouts across race histories as shown in Fig. 5c and d, we would again <sup>fi</sup>nd the four race history providing the highest payouts (\$4265.40), Table 5. Taken together, this would indicate that the four race history is performing better than any of the other racing histories, including the seven race history which was used in studies by Chen et al. [4] and Schumaker and Johnson [21]. It is interesting to note that the four race history is a trade-off between the intuition of professional wagerers and data miners; whereas the professional wagerer would focus more heavily on the most recent races (following the adage that you are only as good as your last race) and the data miner would want as many races as possible to develop a fuller picture of performance.

![](/api/attachments/B7HDHPNW/fulltext/images/b9d7b7ad61e8cfb4b23a550e03d495e15df7a2ff10df016cb28c593e913ede6f.jpg)

![](/api/attachments/B7HDHPNW/fulltext/images/800613d02305acbfa3b5ce78e1c6b2c7ba8757b5755cf4f29b6f0250fea8f641.jpg)  
Fig. 7. S&C Racing for exotic wagers (4 race history).

Comparing established methods in exotic wagers (4 race history).

<table><tr><td rowspan="2"></td><td colspan="4">Accuracy</td><td colspan="4">Payout</td></tr><tr><td>Exacta</td><td>Quiniela</td><td>Trifecta</td><td>Trifecta Box</td><td>Exacta</td><td>Quiniela</td><td>Trifecta</td><td>Trifecta Box</td></tr><tr><td>S&amp;C Racing</td><td>11.43% (3.7)</td><td>25.71% (3.7)</td><td>3.45% (3.6)</td><td>12.50% (3.3)</td><td>$450.40 (4.2)</td><td>$479.00 (4.2)</td><td>$385.00 (4.2)</td><td>$2273.60 (4.2)</td></tr><tr><td>Crowdsourcing</td><td>19.59%</td><td>30.41%</td><td>7.73%</td><td>15.98%</td><td>$139.40</td><td>$197.40</td><td>$223.40</td><td>-$145.00</td></tr><tr><td>Random chance</td><td>1.56%</td><td>3.12%</td><td>0.24%</td><td>1.44%</td><td>-$873.60</td><td>-$955.00</td><td>-$939.00</td><td>-$2170.60</td></tr></table>

We suspect that the four race history could be the result of peculiarities in racing schedule at North<sup>fi</sup>eld Park. There are typically four races over the weekend with a several day break during the midweek. We feel that this midweek break may be introducing confounding variables such as additional training, adjustments to food, medicine and/or routine (e.g.; moving to a different stable or track). Whereas during the weekend race period, less variable change can occur and hence the animals behave in a more predictable manner.

Restating our model in terms of a four race history, there are 698 training races on 5777 training cases, 194 testing races on 1653 testing cases with an average of 8.52 horses per race. Looking again at maximizing accuracy of traditional wagers but this time with a four race history, we present Fig. 6a and Table 6.

From the four race history data, Win still underperformed Crowdsourcing (37.50% to 45.50%), Place was statistically equivalent and Show outperformed its Crowdsourcing counterpart (100.0% to 78.00%) (p-valueb0.01). S&C Racing also outperformed the Dr. Z Bettors (p-valuesb0.01) and random chance (p-valueb0.1 for Win, b0.01 for Place and Show).

Statistically speaking, the accuracies of the four race history exhibited a similar performance to the seven race history seen earlier. However, the differences became apparent when looking at the maximized payouts as shown in Fig. 6b. From the data, Win and Place underperformed Crowdsourcing but Show outperformed it \$526.50 to \$283.50 (p-valueb0.01). S&C Racing also outperformed Dr. Z Bettors and random chance (p-valuesb0.01). It is interesting to note the comparatively smaller payout increase in Crowdsourcing versus S&C Racing. This may indicate that Crowdsourcing is experiencing a marginal return on the lower placed <sup>fi</sup>nishes (i.e.; Place and Show), whereas S&C Racing is capitalizing on additional knowledge not widely known by the crowds.

![](/api/attachments/B7HDHPNW/fulltext/images/065009c86f4fbc3e4598bb4cad8a76b2da9a5d19d36e01b394e3d371d815c843.jpg)

![](/api/attachments/B7HDHPNW/fulltext/images/1bf9b5ac2a64acd4a1d2f600c704a4bcb58037a425f7693340c915d63ba2dd6b.jpg)  
Fig. 8. Betting ef<sup>fi</sup>ciency of wagers (4 race history).

In terms of maximized accuracy on exotic wagers, we present Fig. 7a and Table 7.

From the data, S&C Racing all underperformed Crowdsourcing in terms of accuracy but outperformed random chance (p-valuesb0.01). However, the results were different when looking at payouts in Fig. 7b. It can be noted that S&C Racing outperformed all Crowdsourcing and random chance wagers (p-valuesb0.01).

Now it becomes a question of calibration. While the seven wager types as a whole had better accuracy than the seven race counterparts, the wagers for Crowdsourcing exhibited slightly better accuracy. However, that accuracy did not translate into better payout gains. By contrast, <sup>fi</sup>ve of S&C Racing's wagers outperformed in terms of payout leading us to suspect that S&C Racing was able to capitalize on longshot wagers (decreased accuracy, increased payout). We saw a similar accuracy/payout trade-off in Chen et al. [4] and Schumaker and Johnson [21]. We feel that this result stems from S&C Racing better able to identify the longshot wagers with higher payouts than crowds whom may be wagering more conservatively.

## 6.3. Evaluating betting efficiency

To answer our third research question of what wager combinations work best and why, we analyze each wager in terms of betting ef<sup>fi</sup>ciency, or the amount of return for every \$1 wagered. Fig. 8a demonstrates betting ef<sup>fi</sup>ciency on traditional wagers while Fig. 8b shows the ef<sup>fi</sup>ciencies of exotic wagers. Table 8 provides numerical descriptions of the observed peaks.

From the data, S&C Racing outperformed Crowdsourcing in all seven wagers (p-valuesb0.01), outperformed the Dr. Z Bettors (p-valuesb0.01) and outperformed random chance in all wagers (p-valuesb0.01). While it could be argued that S&C Racing is wagering on the strongest races, Dr. Z is similarly selective and Crowdsourcing should be just as strong assuming rational bettors with the same access to information that S&C Racing uses. However, the discrepancies would appear to indicate that S&C Racing is exploiting an informational inequality within the harness racing market. Even more interesting is the Trifecta Box wager; when applied to every race, this wager was still able to obtain a \$6.63 return per dollar wagered, which still performs better than Crowdsourcing. Digging further

## Table 8

Betting ef<sup>fi</sup>ciency of wagers (4 race history).

<table><tr><td></td><td>Win</td><td>Place</td><td>Show</td><td>Exacta</td><td>Quiniela</td><td>Trifecta</td><td>Trifecta Box</td></tr><tr><td>S&amp;C Racing</td><td>$1.08(3.5)</td><td>$2.30(3.3)</td><td>$2.55(3.3)</td><td>$19.24(3.5)</td><td>$18.93(3.5)</td><td>$3.56(4.2)</td><td>$21.05(4.2)</td></tr><tr><td>Crowdsourcing</td><td>$0.68</td><td>$1.29</td><td>$1.42</td><td>$0.72</td><td>$1.02</td><td>$1.15</td><td>-$0.75</td></tr><tr><td>Dr. Z Bettors</td><td></td><td>$0.00</td><td>$0.06</td><td></td><td></td><td></td><td></td></tr><tr><td>Random chance</td><td>—</td><td>—</td><td>$0.25</td><td>-$4.50</td><td>-$4.93</td><td>-$4.84</td><td>—</td></tr><tr><td></td><td>$0.49</td><td>$0.20</td><td></td><td></td><td></td><td></td><td>$11.19</td></tr></table>

a  
![](/api/attachments/B7HDHPNW/fulltext/images/f30fd38486b3057bce5b4ed7de234abc9e769af4f4b2db85f0183499b9b6064c.jpg)

b  
![](/api/attachments/B7HDHPNW/fulltext/images/17c43110c263aa29366ddb79a1cefd63e853ee9207ab57b983fe8c9d757a7cc8.jpg)  
Fig. 9. Comparing Dr. Z to S&C Racing (4 race history).

into this result, Trifecta Straight was correct 6 times on 194 wagers (3.09% accuracy), but offsets its losses with enough successful longshot returns.

The other interesting item of note was the performance of the Dr. Z System. It has been observed that since its widespread usage at tracks, bettors have effectively arbitraged the Dr. Z System to nil gain. In fact, we observed this effect in Table 8 where Place betting for the Dr. Z System provides a \$0.00 return. If instead of applying the Dr. Z System to every race, as the strict book implementation would allow, we couple it with a predicted <sup>fi</sup>nish measure, like S&C Racing, and make wagers accordingly, we would have Fig. 9a and b.

From Fig. 9a, we note that S&C Racing's Place and Dr. Z's PlaceZ run identical, as does S&C Racing's Show and Dr. Z's ShowZ (running atop one another). This interesting result indicates that both systems have identical accuracies and hints that S&C Racing may be employing a similar mechanism as Dr. Z, albeit from a machine learning perspective. However, if we dig further into this relationship, we notice that the payouts differ in Fig. 9b. This means that while the accuracies were identical; both systems were wagering on different races making the identical accuracy more of a coincidence. From Fig. 9b, S&C Racing's Place outperformed Dr. Z's PlaceZ until the predicted <sup>fi</sup>nish of 4.7 when the roles reversed. For Show, S&C Racing's Show outperformed Dr. Z's ShowZ on all <sup>fi</sup>nishes. It was further interesting to note that both Show and ShowZ outperformed Place and Place Z wagers, meaning that Show and ShowZ wagers are more pro<sup>fi</sup>table.

While the book implementation of Dr. Z has been effectively arbitraged to zero, coupling it with a competent <sup>fi</sup>nish strength predictor can provide similar results to S&C Racing in terms of accuracy, but not payout. This observation could perhaps breathe new life into Dr. Z variations.

## 7. Conclusions and future directions

The seven race history has been a defacto standard in several racing studies. We sought to empirically test whether this standard is optimal within the harness industry. By evaluating the seven race history as a baseline, we found that S&C Racing mostly outperformed random chance, Dr. Z Bettors and had mixed results versus Crowdsourcing in both accuracy and payouts. Taken alone, S&C Racing shows promise similar to better performance than the well-established prediction methods.

When evaluating a range of different race histories to track accuracy and payouts, we found that a four race history performed best. Comparing this four race history against established predictors we found that S&C Racing outperformed both random chance and Dr. Z Bettors in both accuracy and payouts. When compared against Crowdsourcing, S&C Racing exhibited a mixture of results with the exception of Show wagers which consistently outperformed Crowdsourcing in both accuracy and payout; and exotic wagers which similarly outperformed the Crowdsourcing counterparts in terms of payouts. We found that S&C Racing was better able to identify top contenders than the crowds were.

In terms of betting ef<sup>fi</sup>ciency, S&C Racing outperformed all other models easily. It is speculated that S&C Racing was exploiting abnormal payouts arising from informational inequalities within the harness market.

Future directions for this stream of research include tweaking other Chen variables and building a fraud detection framework. This paper investigated manipulating only one of the Chen variables. Perhaps further advances could be found by adjusting other variables as well. For a fraud detection network, now that a robust model of prediction has been built, can we use it to detect unknown/undisclosed injuries or fraudulent behavior (e.g., jockeys/trainers/etc. that consistently over/ underperform versus projected <sup>fi</sup>nish). Clearly more study within this domain is needed.

## References

[1] J. Albert, Streaky hitting in baseball, Journal of Quantitative Analysis in Sports 4 (1) (2008).

[2] M. Cain, D. Law, D. Peel, The favourite-longshot bias, bookmaker margins and insider trading in a variety of betting markets, Bulletin of Economic Research 55 (3) (2003) 263–273.

[3] H. Chen, M. Chau, Web mining: machine learning for web applications Annual Review of Information Science and Technology (ARIST) 38 (2004) 289–329.

[4] H. Chen, et al., Expert prediction, symbolic learning, and neural networks: an experiment on greyhound racing, IEEE Expert 9 (6) (1994) 21–27.

[5] J. Dana, M. Knetter, Learning and ef<sup>fi</sup>ciency in a gambling market, Management Science 40 (10) (1994) 1317-1328

[6] DataSoftSystems, Data mining—history and in<sup>fl</sup>uences. Accessed from http://www. datasoftsystem.com/articles/article-1380.html (on Sept. 2, 2009).

[7] D. Harville, Assigning probabilities to the outcomes of multi-entry competitions, Journal of the American Statistical Association 68 (342) (1973) 312–316.

[8] D. Hausch, W. Ziemba, M. Rubinstein, Ef<sup>fi</sup>ciency of the market for racetrack betting, Management Science 27 (12) (1981) 1435–1452.

[9] D. Hausch, V. Lo, W. Ziemba, Ef<sup>fi</sup>ciency of Racetrack Betting Markets, B&JO Enterprises, Singapore, 2008.

[10] Z. Huang, et al., Credit rating analysis with support vector machines and neural networks: a market comparative study, Decision Support Systems 37 (4) (2004) 543–558.

[11] U. Johansson, C. Sonstrod, Neural networks mine for gold at the greyhound track, International Joint Conference on Neural Networks: Portland, OR, 2003

[12] A. Lazar, Income prediction via support vector machine, International Conference on Machine Learning and Applications: Louisville, KY, 2004

[13] S. Luckner, J. Schroder, C. Slamka, on the forecast Accuracy of Sports Prediction Markets, in: H. Gimpel, et al., (Eds.), Negotiation, Auctions, and Market Engineering, Springer, Berlin, 2008, pp. 227–234.

[14] G. Piatetsky-Shapiro, Difference between data mining and statistics. Accessed from http://www.kdnuggets.com/faq/difference-data-mining-statistics.html (on Oct 2, 2008).

[15] J. Pratt, Risk aversion in the small and in the large, Econometrica 32 (1–2) (1964) 122–136.

[16] Progress Publishing, A history of gambling. Accessed from http://www. crapsdicecontrol.com/gambling\_history.htm (on Sept. 28, 2011).

[17] L. Qiu, H. Rui, A. Whinston, A Twitter-based Prediction Market: Social Network Approach, ICIS, Shanghai, China, 2011.

[18] J. Ritter, Racetrack betting—an example of a market with ef<sup>fi</sup>cient arbitrage, in: D. Hausch V. Lo W. Ziemba (Eds.). Efficiency of Racetrack Betting Markets Academic Press, San Diego, 1994

[19] R. Sauer, The economics of wagering markets, Journal of Economic Literature 36 (4) (1998) 2021–2064.

[20] R.P. Schumaker, Using SVM regression to predict harness races: a one year study on North<sup>fi</sup>eld Park, Midwest Decision Sciences Institute Conference: Indianapolis, IN, 2011.

[21] R.P. Schumaker, J.W. Johnson, Using SVM regression to predict greyhound races, International Information Management Association (IIMA) Conference: San Diego CA 2008

[22] R. Schumaker, O. Solieman, H. Chen, Sports Data Mining, Springer, New York, 2010.

[23] R.P. Schumaker, et al., Evaluating sentiment in <sup>fi</sup>nancial news articles, Decision Support Systems 53 (3) (2012) 458–464.

[24] R. Sobel, T. Raines, An examination of the empirical derivatives of the favouritelongshot bias in racetrack betting, Applied Economics 35 (4) (2003) 371–385.

[25] M. Spann, B. Skiera, Sports forecasting: a comparison of the forecast accuracy of prediction markets, betting odds and tipsters, Journal of Forecasting 28 (1) (2008) 55–72.

[27] A. Tversky, T. Gilovich, The cold facts about the “hot hand” in basketball, in: J. Albert, J. Bennett, J. Cochran (Eds.), Anthology of Statistics in Sports, SIAM, Philadelphia, 2005.

[26] J. Surowiecki, The Wisdom of Crowds, Doubleday, New York, 2004.

[28] V. Vapnik, The Nature of Statistical Learning Theory, Springer, New York, 1995.

[29] J. Williams, Y. Li, A case study using neural network algorithms: horse racing predictions in Jamaica, International Conference on Arti<sup>fi</sup>cial Intelligence: Las Vegas NV 2008

[30] S. Wise, Testing the effectiveness of semi-predictive markets: are <sup>fi</sup>ght fans smarter than expert bookies? Collaborative Innovation Networks Conference: Savannah, GA, 2009.

[31] W. Ziemba, D. Hausch, Beat the Racetrack, Harcourt, Brace & Jovanovich, San Diego, 1984.

![](/api/attachments/B7HDHPNW/fulltext/images/2b780776a9af8e356ec8f79cd8fbcaf05ae522b5cf9f6092ad5955fb5d25ecca.jpg)

Dr. Robert P. Schumaker is an Associate Professor in Management Information Systems at Central Connecticut State University. He received his undergraduate degree in Civil Engineering from the University of Cincinnati, an MBA degree in Management and International Business from the University of Akron and his Ph.D. degree in Management from The University of Arizona. His interests include Stock Price Prediction, Natural Language systems, Textual Analysis techniques and Sports Data Mining.
