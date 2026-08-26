---
otero_id: 20064
otero_key: "76SFVURK"
title: "Decision support system for policy-making: Quantifying skill and chance in daily fantasy sports"
authors: "Aishvarya; Tirthatanmoy Das; U. Dinesh Kumar"
year: "2024"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2024.114237"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support system for policy-making: Quantifying skill and chance in daily fantasy sports

![](/api/attachments/76SFVURK/fulltext/images/f51ba384d0793a2e91d1f172f5353a21ad0195d570696afd851403c7bdf83149.jpg)

Aishvarya <sup>a,\*</sup>, Tirthatanmoy Das <sup>b</sup>, U. Dinesh Kumar <sup>c</sup>

<sup>a</sup> Information Management & Analytics Area, S.P. Jain Institute of Management & Research (SPJIMR), Mumbai, India

<sup>b</sup> Economics Area, Indian Institute of Management, Bangalore, India

<sup>c</sup> Decision Sciences Area, Indian Institute of Management, Bangalore, India

## A R T I C L E I N F O

Keywords: Decision-making under uncertainty Data-driven policy making Daily fantasy sports Skill dominance Stochastic frontier analysis

## A B S T R A C T

We explore the question of skill versus chance dominance in Daily Fantasy Sports (DFS), which has been the subject of numerous legal disputes around the world. Our study examines whether a contestant’s winnability in DFS is influenced by factors reflecting skills using cricket-based daily fantasy contest data and a true fixed effects stochastic frontier model. We find that skill contributes significantly towards winnability in five ways. First, contestants performing well in the past do better in the present. Second, gaining more game experiences im proves performance. Third, contestants who participated recently, tend to exhibit higher winnability. Fourth, selecting an appropriate contest type enhances winnability. Fifth, the large estimated signal-to-noise ratio in dicates that the unobserved skill measured by a non-negative error has a much greater impact on winnability than the regular two-sided random shocks. These results are robust to varying specifications and subsets of data. Decision makers and regulators can use the model presented in the study to distinguish skill-dominant DFS from chance-dominant DFS.

## 1. Introduction

Decisions are almost invariably made in the face of risk. In some cases, the risk is relatively small, while in others, it is substantial [1–3]. For instance, decisions regarding mutual fund investments, sports stra tegies, employee selection, fishing activities, etc., involve a considerable amount of risk and require a significant amount of skill on the part of the decision-makers (see Table 1 for references). While research demon strates the importance of skill, there are often ambiguities about how much skill matters in comparison to pure chance. Due to this lack of clarity, the legal community sometimes restricts business activities to prevent gambling and addiction [4,5]. For instance, Daily Fantasy Sports (DFS) is a rapidly expanding industry generating billions of dol lars in revenue, but it is subject to numerous legal challenges across the globe due to the lack of clarity regarding its legal status [6–8]. Never theless, only a few studies have quantified the impact of skill versus chance. We explore this in the context of DFS. Using DFS data and a stochastic frontier approach, this study evaluates the relative impor tance of skill over chance.

Countries that consider gambling as an illegal activity use the “Dominant Factor” test to identify gambling activities. According to this test, if the outcome of a game is influenced more by a contestant’s skill than by chance, the game is referred to as “skill-dominant” or a “game of skill”. However, if the effect of chance dominates, it is referred to as “chance-dominant” or a “game of chance”, which falls under the pur view of gambling. In a DFS setup, contestants<sup>1</sup> create their own teams (commonly known as fantasy teams) for upcoming matches by choosing athletes expected to participate in those matches. Following the match, these fantasy teams are ranked based on the performance of the selected athletes. Some of these contests are free of cost, while others charge an entry fee. Depending on the type of contest, winner(s) of the contest receive a monetary reward. Since DFS offers a “pay-to-play” format, several countries have faced legal cases claiming DFS to be a form of online gambling. DFS operators like DraftKings, FanDuel and Dream11 have faced multiple legal cases [4,9,10]. For example, three public in terest litigations (PIL) were filed against Dream11, the largest Indian DFS operator, claiming that the format adopted by them amounts to gambling. Even though three regional High Courts and the Supreme Court of India held fantasy sports facilitated by Dream11 as a “Game of Skill” [9,11], many state governments later amended their gaming laws to ban pay-to-play formats of DFS and online games. Some of these amendments were later overturned by their respective state High Courts, ruling that it is unreasonable to put a ban on games of skill even if it involves money [10,12].

Table 1  
Studies examining influence of skill in different contexts.

<table><tr><td>Context</td><td>Author (Year)</td><td>Journal (Reference)</td></tr><tr><td>Mutual Fund Returns</td><td>Fama &amp; French (2010)</td><td>The Journal of Finance [50]</td></tr><tr><td>Mutual Fund Returns</td><td>Cuthbertson et al. (2008)</td><td>Journal of Empirical Finance [51]</td></tr><tr><td rowspan="2">Online Auction Market Organizational; Efficiency of CEO</td><td>Kaufman et al. (2009)</td><td>Decision Support Systems [52]</td></tr><tr><td>Bertrand &amp; Mullainathan (2011)</td><td>The Quarterly Journal of Economics [53]</td></tr><tr><td>Fishery</td><td>Alvarez &amp; Schmidt (2006)</td><td>J. of Productivity Analysis [54]</td></tr><tr><td>Poker</td><td>Croson et al. (2008)</td><td>Chance [13]</td></tr><tr><td>Poker</td><td>Levitt &amp; Miles (2014)</td><td>Journal of Sports Economics [15]</td></tr><tr><td rowspan="2">Texas Hold&#x27;em Games</td><td>Levitt et al. (2013)</td><td>Georgetown Law Journal [14]</td></tr><tr><td>Borm et al. (2004)</td><td>Mathematical Methods of Operations Research [55]</td></tr><tr><td>Games</td><td>Larkey et al. (1997)</td><td>Management Science [56]</td></tr><tr><td>Football</td><td>Reep &amp; Benjamin (1968)</td><td>Journal of the Royal Statistical Society. Series A [18]</td></tr></table>

Such legal cases involving DFS are generally challenged over the game’s rules and setup that can be highly subjective. This has led to legal turmoil in the sector resulting in several court cases, revenue losses, and bans on DFS operators. This not only impacts the DFS business, which has been expanding rapidly, but it also causes legal inconsistencies on multiple levels. This confusion is a global problem and not just restricted to a few countries, as explained in detail in Section 2. In fact, this am biguity extends beyond the DFS to all online games where the issue of skill versus chance dominance is debated. The absence of a standardized, quantitative approach to evaluate the effect of a contestant’s skill and chance in a DFS contest has led to inconsistencies in the law and business losses, which is why it is necessary to adopt a data-driven approach.

In any game setting, the distinction between skill and chance is seldom straightforward. In DFS, there can be various indicators of contestants’ skill (like their decision-making abilities in selecting ath letes, past performance, inherent interests, etc.) and chance elements (like an unexpected change in weather conditions, athlete injury or opponent’s skill). Contestants take a series of decisions under uncer tainty, and hence, it is important to first comprehend the process’s de cision points, define elements of skill and chance, and then identify the dominant factor. Studies examining the role of skill in other sports like poker [13–15], football [16–18], baseball [19,20], tennis [21] cannot be extended to DFS because they do not consider these inherent un certainties in a contestant’s decision-making. Unfortunately, the litera ture on skill versus chance evaluation in DFS is limited and lacks an approach that accounts for these uncertainties. Previous studies [8,22] have evaluated contestants’ performance based on the contest’s outcome, i.e., whether the contestant won or lost. However, these studies do not propose a method of defining a contestant’s performance because skill is a relative trait. This study, on the other hand, evaluates a contestant’s performance relative to the winner’s score or the extent to which they fall short of it. In addition, we base our study at the contest level and evaluate contestants’ performance for each of their team submissions, which has an advantage over previous studies that could not assess the impact of contestants’ pre-determined observable char acteristics on their performance [8,14].

We model the relative performance of a contestant in DFS as a function of a.) elements of their skill that vary with time, b.) elements of their skill that are time-invariant, and c.) chance elements that are beyond the contestant’s control. We identify these factors and use Greene’s True Fixed Effects (TFE) formulation of the stochastic frontier model [26,27] to measure the contestant’s efficiency. This study measures indicators of contestants’ skills, such as the impact of their previous performance, experience, recency, and contest choice on their winnability. By computing the signal-to-noise ratio, we quantify the relative effect of skill and chance on the contest outcome and hence determine the dominant factor. Utilizing panel data for cricket-based DFS contests from Dream11, the leading Indian DFS operator, we find that skill plays a dominant role in determining a contestant’s winn ability. We observe that a contestant’s past performance matters, i.e., contestants who have performed well in previous contests are more likely to perform well in subsequent contests. We also find that contes tants who participated recently, tend to exhibit higher winnability. Experience gained in paid contests and contest selection also have a significant impact on the contestant’s performance. These results together suggest that contestants’ performance in DFS is significantly influenced by their skill rather than the chance elements of the game.

This study offers an integrated decision support framework that a.) evaluates the relative importance of skill and chance, b.) studies a contestant’s observed and unobserved characteristics, c.) tests for other indicators of skill, and d.) can be replicated to other games, subject to data availability. The proposed approach not only contributes to the literature on skill versus chance evaluation but also offers a decision support system to help policymakers adopt a quantitative approach in resolving the ongoing debate, thus contributing to the literature on datadriven decision-making.

## 2. Literature review

Fantasy sports began around the 1950s in Oakland, USA [25]. These were initially limited to golf, baseball, and football. Until 1990, most of these were played in small groups but with the advent of the internet, fantasy sports began to gain popularity, and several operators eventually entered the market. DFS, a special format of Online Fantasy Sports (OFS) emerged in 2007, where instead of playing for an entire season, these are played for a shorter period (a day or a week). DraftKings and FanDuel, both of which began in the United States, are two of the most well known DFS operators. In India, Dream11 was the first DFS operator that emerged in 2008 and is currently one of the largest operators in the Indian DFS market [26]. The Indian DFS market, with the world’s largest user base of 130 million users, is expected to grow at a CAGR of 38 percent during FY21-FY27 [27]. Dream11 reported one million regis tered users in 2014, which eventually grew to 60 million in 2018 [28]. The number of Indian DFS operators also increased tremendously from 10 to 140 during 2016-2019 [7]. In Australia, DFS was first made available by Moneyball in 2015, which was followed by several other operators like Draftstars (2016). In 2018, DraftKings entered the Australian market, and PlayUp Interactive acquired Draftstars in 2018, opening doors to other international players to enter the Australian DFS market. In Europe, FanTeam which was founded in 2014 is the leading DFS operator with almost no competition in the DFS industry. DraftK ings acquired a license to operate in the UK and was launched officially in February 2016 with daily fantasy soccer.

Despite the growth of fantasy sports across the world, it has not received adequate attention from researchers. Sports analytics as a field has been gaining attention from researchers who not only study prob lems related to sports [29–36], but also utilize sports as an example to test theories from other managerial disciplines like Operations Man agement, Economics, Supply Chain, Organizational Management and more [19,37–42]. To the best of our knowledge, fantasy sports have so far been the subject of three academic review publications [43–45]. As pointed out by Tacon and Vainker [45], most of the literature has focused on the consumer behavior aspect of fantasy sports, exploring users’ participation, motivation, and customer relationship manage ment. There is also a stream of literature that adopts qualitative methods to examine whether fantasy sports qualify as online gambling but has not gained much attention [46–49].

Two recent studies [8,22] have quantitatively assessed the effect of skill and chance in fantasy sports contests, and concluded that skill is more important than chance. Especially relevant to this subject is the recent work of [8], which analyses data from DFS contests run by Fan Duel and empirically tests for skill dominance based on the four tests of skill proposed by Levitt et al. [14]. Unlike their work, our approach allows us to investigate whether contestants’ predetermined observable characteristics influence their performance (one of the four tests of skill proposed in [14]). In contrast to [8], who use contestants’ winning fraction to derive a metric evaluating the relative role of skill and chance, our work is based on a much more granular level where we use the fantasy points scored by contestants for each of their team sub missions, giving us an added advantage to study contestant character istics. We model contestants’ performance by using a relative measure of their performance in a contest, and separate the effect of their timevarying skill, contestant-specific time-invariant characteristics, and chance elements on their performance in a DFS contest.

Like [24,57–60] who evaluated the efficiency of firms from different industries (health care, transport, supply chain, etc.), we evaluate the efficiency of contestants for each of their team submissions in a DFS contest. To the best of our knowledge, this is the first attempt at per formance evaluation using stochastic frontier analysis in a sports setting. We not only measure the effect of skill and chance on contestants performance but also quantify several other indicators of skill, like the effect of their past performance, experience, recent participation, and choice of contest, which have not been studied in the literature.

As mentioned earlier, most DFS-related judicial proceedings world wide have approached this problem subjectively, resulting in legal confusion (see supplementary material for details). Legal judgments based on the subjective assessment of skill-chance dominance of a DFS operator may not apply to other operators or other sports activities because of differences in rules, match format and point system. The policy think tank of the Government of India, NITI Aayog, published a draft for discussion on OFS regulation, emphasizing the need for "sta tistical and legal evaluation of such format to ascertain and confirm that such format is skill-predominant in determining the winning outcome" [61]. Hence, a data-driven approach is necessary that quantifies con testants’ skills and chance elements, measures their performance in a DFS contest, and then identifies the dominant factor. The literature lacks such an empirical study where we can quantify the dominance of skill and chance, and possibly replicate the analysis for other operators. Thi is one of the major contributions of this study.

## 3. Daily fantasy sports: setup and working

In this section, we explain how DFS contests work. Since we use contestant-level data of cricket-based DFS contests in this study, we explain the working of DFS contests with cricket as reference. In a DFS platform, contestants can view the list of athletes who are expected to play in upcoming matches, their “Points” and “Credits”. “Points” indi cate athletes’ past performance, while “Credits” represent their cost, both of which are decided by the operator. Contestants have a budget of 100 credits to select 11 athletes for their fantasy team. Points of each athlete are updated based on their performance in the match, and points of a fantasy team is sum of these updated points of the selected athletes. There are constraints on the team composition, i.e., the number of athletes allowed to be selected from each category (Table 2 shows an example). Once contestants have selected 11 athletes, they must also choose Captain and Vice-Captain among the selected athletes. The Captain receives twice the number of points scored in the match, while the Vice-Captain receives 1.5 times the number of points.

Table 2  
Constraints on team composition.

<table><tr><td>Athlete Category</td><td>Minimum</td><td>Maximum</td></tr><tr><td>Wicket Keeper – WK</td><td>1</td><td>3</td></tr><tr><td>Batter – BAT</td><td>3</td><td>6</td></tr><tr><td>All Rounder – AR</td><td>1</td><td>4</td></tr><tr><td>Bowler – BWL</td><td>3</td><td>6</td></tr></table>

Contestants can check the list of contests for upcoming matches and can submit their teams into one or more contests. These contests have different characteristics like entry fee, contest size, payoff structure (number of winners and their reward). Some of these contests are free of cost (Practice/Free Contests), and some have an entry fee (Paid/Pay-to-Play Contests). While some paid contests have a “winner take-all” format in which the contestant with the highest point wins, others have a “top heavy” and distributed payoff structure wherein the top few contestants win and their reward is predetermined. A few contest formats allow more than one team submission by a contestant. Once a match has begun, contestants cannot submit a new team or make changes in their existing fantasy team. After the match, the contest winner(s) are rewarded as per the contest’s payoff structure.

## 4. Stochastic frontier model: a brief overview

A brief summary of stochastic frontier analysis is provided in this section to help readers understand the method adopted in this study. The 1950s saw the beginning of the literature on productive efficiency measurement [62]. The idea of stochastic frontier was introduced by [63,64], where they separate the effect of random events (chance) from inefficiency. The basic form of stochastic frontier model is given as:

$$
y _ {i} = f (X _ {i}; \beta) + v _ {i} \pm S u _ {i}
$$

Here, y represents the output of unit i, $X _ { i }$ denotes the vector of input and β denotes the vector of parameters. The sign of the inefficiency term, $s ,$ depends on whether the frontier represents cost (+1) or production (-1). In this study, we consider contestants participating in a DFS contest as units (i). The composed error term consists of two parts, i.e., u and $\nu _ { i \cdot }$ $u _ { i }$ is one-sided (positive) error term representing technical inefficiency, and $\nu _ { i }$ is the symmetric error term with zero mean, which captures random events that are beyond the control of unit i. The relative importance of inefficiency and chance can be assessed by comparing variances in u and $\begin{array} { r } { \nu _ { i \cdot } \lambda = \frac { \sigma _ { u } ^ { 2 } } { \sigma _ { \nu } ^ { 2 } } } \end{array}$ is used as a measure of relative importance of skill and chance.

In a panel data setting, the model can be written as:

$$
y _ {i t} = \alpha + X _ {i t} \beta + v _ {i t} - u _ {i t}
$$

Schmidt and Sickles [65] and many other following studies assumed technical inefficiency to be time-invariant i.e., $u _ { i t } = u _ { i } . ~ { \bf S } 0 ,$ the model becomes:

$$
y _ {i t} = \alpha + X _ {i t} \beta + v _ {i t} - u _ {i}
$$

With $\alpha _ { i } = \alpha - u _ { i } ,$ this can be written as:

$$
y _ {i t} = \alpha_ {i} + X _ {i t} \beta + v _ {i t}
$$

The parameters can be estimated using within transformation. In efficiency of the $i ^ { t h }$ unit is estimated as the difference between unit’s estimated fixed effects (α̂ ) and the highest estimate of fixed effects i. $\mathrm { e . , \ } \widehat { \mathrm { u _ { i } } } = m a x _ { \mathrm { i } } ( \widehat { \mathrm { \alpha } } _ { \mathrm { { i } } } ) - \ \widehat { \mathrm { \alpha } } _ { \mathrm { { i } } }$ , ensuring $\widehat { u _ { i } } \geq 0 \forall i .$ . Unit-specific estimates of technical efficiency can be expressed as:

$$
\mathrm{TE} _ {\mathrm{i}} = e x p (\widehat {\mathbf {u}} _ {\mathrm{i}})
$$

The fixed effects approach discussed above is distribution-free and allows correlation with regressors. However, we end up interpreting unit-specific term as the inefficiency. In other words, this approach cannot help us in differentiating unit-specific effects from inefficiency. As a result, this approach does not allow us to capture time-invariant cross-unit heterogeneity, if any. The inefficiency estimates are only with respect to the ‘best’ unit in the sample. In addition, the above formulation assumes inefficiency to be time-invariant, which may not be true in our case. As explained in the following section, a contestant’s performance in DFS contests can be influenced by time-varying in efficiency, contestant-specific characteristics that are time-invariant, and the chance elements. $\mathsf { W e } ,$ thus, use the Greene’s True Fixed Effect (TFE) formulation to model contestants’ performance in DFS contests and segregate these components.

In general, Greene’s TFE formulation of stochastic frontier model is given as:

$$
y _ {i t} = \alpha_ {i} + X _ {i t} \beta + v _ {i t} - u _ {i t}
$$

where $y _ { i t }$ represents performance of $i ^ { t h }$ unit in time $t , \alpha _ { i }$ is the unitspecific constant, $X _ { i t }$ includes all time-varying regressors influencing the performance of unit i in time $t , \beta$ denotes the associated vector of parameters. The random error term $\nu _ { i t }$ is assumed to follow $N \left( 0 , \sigma _ { \nu } ^ { 2 } \right)$ and uncorrelated over i and t. It represents the chance elements and hence, its variance $\left( \sigma _ { \nu } ^ { 2 } \right)$ is a measure of importance of chance elements in explaining variation in performance of units. $u _ { i t }$ is the one-sided error term representing inefficiency of unit i in time t. As evident, this formulation considers inefficiency to vary with time.

Assuming $u _ { i t }$ to be half normally distributed, $\mathrm { i . e . , } u _ { i t } \sim N ^ { + } \big ( 0 , \sigma _ { u } ^ { 2 } \big )$ , the log likelihood for the above model is expressed as [23]:

$$
L o g L = \sum_ {i = 1} ^ {N} \sum_ {t = 1} ^ {T} l o g \left[ \frac {2}{\sigma} \Phi \left(- \lambda \left(\frac {y _ {i t} - \alpha_ {i} - X _ {i t} \beta}{\sigma}\right)\right) \phi \left(\frac {y _ {i t} - \alpha_ {i} - X _ {i t} \beta}{\sigma}\right) \right]
$$

where $\Phi ( . )$ and $\phi ( . )$ are the cumulative density function and prob ability density function of standard normal distribution, respectively. $\sigma = \sqrt { \left( \sigma _ { u } ^ { 2 } + \sigma _ { \nu } ^ { 2 } \right) }$ is the standard deviation of the composite error term $\begin{array} { r } { ( \epsilon _ { i t } = \nu _ { i t } - u _ { i t } ) . \lambda = \frac { \sigma _ { u } ^ { 2 } } { \sigma _ { v } ^ { 2 } } } \end{array}$ denotes the ratio of variance of inefficiency to that of the noise term, commonly known as the signal-to-noise ratio. A maximum likelihood dummy variables estimator (MLDVE) approach was suggested for this model [23,66], which showed that maximization of this likelihood function by ‘brute force’ is computationally feasible even in the presence of large number of nuisance parameters.

## 5. Theory

In DFS, contestants make several decisions while creating their fan tasy team(s). Due to the uncertainties involved, contestants make many of these decisions under uncertainty. Factors like athletes’ past perfor mance act as a signal for the contestant, helping them decide whether the athlete should be included in the fantasy team. A contestant’s se lection of athletes is similar to that of a company’s hiring process. The seminal work of Michael Spence [67] recognizes hiring process as an investment under uncertainty. An employer has information on some of the observable characteristics of potential employees such as their educational background, work experience, criminal, service records, etc. These characteristics act as signals that help them assess the candidate’s capacity. The contestants determine which athletes to include in their fantasy teams similar to the manner employers determine which employee to hire based on the signals they present. Like employee hir ing, creating a fantasy team involves uncertainties. After selecting ath letes based on their signals and ensuring that team composition and budget constraints are met, contestants decide which contest(s) to enter their fantasy team into, much like portfolio risk management [31]. In risk management, researchers often use the known-unknown framework to classify risks as known unknowns, known knowns, unknown unknowns, and unknown knowns. This framework acknowledges that there are certain risks that cannot be identified no matter how careful we are. Similarly. due to the risks and uncertainties involved in DFS. it becomes difficult for contestants to come up with the best team by selecting the set of most efficient athletes (By efficient, we mean selecting athletes with highest realized (ex-post) fantasy points). In their book titled “Radical uncertainty: Decision-making $f o r$ an unknowable future”, Kay and King [2] discuss situations involving deeper level of uncer tainty. As mentioned in the book, Gary Klein, an American psychologist studied the decision-making behavior of accomplished professionals. Klein’s main findings were as follows:

Decision-makers usually look for the first workable option they can find, not the best option. Since the first option they consider is usu ally workable, they do not have to generate a large set of options to be sure they get a good one. (p. 173)

As a result, athletes selected by contestants reflect their behavioral decision-making abilities, personal beliefs and understanding of the game. Massey and Thaler [68] used National Football League (NFL) data to determine whether incentives and experience influence the decisionmaking biases. They concluded that the decisions taken by managers and owners of NFL teams were not consistent with rational expectations but are biased and consistent with psychological research. Therefore, contestants’ choices of athletes in a DFS contest could depend not only on their behavioral decision-making abilities but also on their personal preferences, bias, tendency to follow their hunch, select favorite athlete, and other personal beliefs. Therefore, it is crucial to comprehend the process’s decision points, identify and characterize these decisions to evaluate contestants’ performance.

There are typically three types of decisions a contestant makes when submitting a team in a DFS contest (Fig. 1):

1) Based on their knowledge on pitch conditions, weather conditions and home versus away effect, contestants decide which athletes are likely to perform well in that match.

2) Taking into consideration the rules and constraints of the fantasy team (Table 2), contestants decide which athletes can be selected to satisfy all the team composition constraints.

3) Once contestants have created their team(s), they decide on the choice of the contest. Contestants choose which contest(s) to participate based on contest characteristics like size, type (Private/ Public, Free/Paid), and payoff structure (entry amount, winning amount, winning positions).

The first and third decision-points will be the same regardless of the sport activity or DFS operator; the second decision-point may vary slightly because different operators may have different rules for team creation. However, the overall decision mechanism remains the same. While the first decision requires a sound understanding of the sport and is unrelated to DFS, the second decision depends largely on the con testant’s ability to create a team under the strict rules set forth for team selection. The third decision, $\mathrm { i . e . , }$ , contest selection, is influenced by contestants' understanding of DFS contests and its characteristics

Apart from the above three decisions, there are two more important factors that can affect a contestant’s performance:

1) There are few elements that are contestant-specific, and largely affect the choices made by the contestant. Contestants may come from a background or have friends or colleagues who are avid sports enthusiasts and discuss sports and/or DFS. They may also have fol lowed sports for a long time and have developed a good under standing of the game. Although these are not considered as decisions made by the contestant directly, such contestant-specific elements are likely to affect their performance.

2) There can be certain elements of the game that are beyond the contestant’s control. Chance-based elements that can affect the outcome of a contest can be classified into two categories: One in volves chance elements relating to the on-field game played by athletes, while the other is related to DFS contests. An unexpected injury to an athlete during the game, an unanticipated change in the weather conditions are examples of chance elements in the first category. When contestants submit their team to a DFS contest, they are unaware of the opponents they are competing with, their skill levels, and their fantasy teams. These are examples of chance ele ments in the second category.

![](/api/attachments/76SFVURK/fulltext/images/ddf0480ed78160f783bf958c2d70fb3fb0becbb06bdd402667b9c6c9aaead76f.jpg)  
Fig. 1. Elements affecting contestants’ performance in DFS.

Accordingly, we define indicators of contestant’s skill in a DFS contest. In a skill-dominant game, these should have a positive effect on contestant’s performance:

1.) Contestant’s Experience: In a skill-dominant game, a contestant should be able to learn as they play more. In a chance-dominant game, on the contrary, contestant’s experience should not influ ence their performance.

2.) Contestant’s Consistency: In a skill-dominant game, past perfor mance should matter, i.e., contestants performing consistently well in previous contests should be likely to perform well in the current contest too.

3.) Contestant’s Recent Participation: A contestant’s recent partici pation in DFS contests should have an effect on their performance in current contests. In other words, in contrast to those who participated in DFS contests long ago, contestants who have been active and participated recently should experience an improve ment in their performance.

4.) Contestant’s Choice of Contest: Due to the differences in contest characteristics and winning structure, the same fantasy team submitted to different contests can yield different ranking posi tions for contestants. thus affecting their winnability. Hence, the ability to decide the contest where the fantasy team should be submitted is important, and whether a contestant is able to choose the right contest for team submission is an indicator of their skill.

## 6. Data and the empirical model

We utilize contestant data that has been anonymized from the leading Indian DFS operator, Dream11, between 2013 and $2 0 1 6 ^ { 2 } .$ . The dataset comprises contest-level information, such as contestant list, contest type, contest size, and other variables. This dataset is based on total 0.27 million contestants, who played during 2013-2016. This in cludes information on total 3624 matches and 1.4 million contests. For the purpose of this study, we draw a random sample of 1000 contestants. Observations in this sample include 2951 matches and 0.16 million contests. Description of information available in the dataset and the variables constructed for this study is provided in Table 3. Appendices B and C provide summary statistics and an exhaustive list of notations used throughout this paper, respectively.

The major purpose of this study is to compare the effect of skill and chance in determining the winnability in cricket-based DFS contests. A contestant’s success in a DFS contest is not solely determined by her performance, but also by the performances of the other contestants. We consider this aspect of competitiveness and construct a contestant’s winnability as follows:

$$
y _ {i c t} = w _ {c} - S _ {i c t}\tag{1}
$$

$S _ { i c t }$ represents score of contestant i for whom contest c is her $t ^ { t h }$ contest. As such, c represents contest identifier, and t captures experi ence of contestant i while playing the contest c. For instance, while participating in contest $c ,$ two contestants i and j may have different experiences (t) prior to playing contest c. w is the winner’s score in contest c that contestant i faces during her $t ^ { \mathrm { { t h } } }$ contest. $y _ { i c }$ is the difference between a contestant’s score and the winner’s score, i.e., the score gap, which reflects winnability of contestant i.

The Winner’s Score $( w _ { c } ) { : } \mathsf { A }$ -priori, contestants do not know who will win, and hence have no knowledge of the winner’s score (w ). Contes tants also do not know the attributes of the other contestants, especially in public contests. As a result, the winner’s actual observed/realized score (the ex-post score) serves as a random uncertainty for a contes tant’s ex-ante decision makings or strategies that ultimately affect her performances. Clearly, a contestant’s relative score is affected by the winner’s ex-post score, however no one knows that beforehand. Due to this uncertainty, our model uses determinants of winner’s scores as random noises that contribute to contestant i’s winnability y .

Table 3 Variable description.

<table><tr><td>Variable</td><td>Description</td></tr><tr><td>Date</td><td>Refers to date of the match</td></tr><tr><td>Match ID</td><td>Uniquely identifies a match</td></tr><tr><td>Contest ID</td><td>Uniquely identifies a contest</td></tr><tr><td>Contestant ID</td><td>Uniquely identifies a contestant</td></tr><tr><td>Team ID</td><td>Uniquely identifies team submitted by a contestant for a given match</td></tr><tr><td>ContestCategory</td><td>Paid/ Free Contest</td></tr><tr><td>Points Scored</td><td>Fantasy Points scored by the contestant&#x27;s team</td></tr><tr><td>ScoreGapict</td><td>Difference in score of contestant  $i's t^{th}$  contest (labelled as ‘c’) and score of winner of the same contest</td></tr><tr><td>Prop10ict</td><td>Proportion of times contestant  $i$  was in the top 10thpercentile before her  $t^{th}$  contest (labelled as ‘c’)</td></tr><tr><td>Prop25ict</td><td>Proportion of times contestant  $i$  was in the top 25thpercentile before her  $t^{th}$  contest (labelled as ‘c’)</td></tr><tr><td>Prop40ict</td><td>Proportion of times contestant  $i$  was in the top 40thpercentile before her  $t^{th}$  contest (labelled as ‘c’)</td></tr><tr><td>ContestSize $_{c}$ </td><td>Number of contestants allowed to participate in contest  $c$ </td></tr><tr><td>ContestType $_{c}$ </td><td>1, if the contest  $c$  was a private contest and 0, if the contest  $c$  was a public contest</td></tr><tr><td>CovidDummy $_{c}$ </td><td>1, if the contest  $c$  was scheduled in 2020-21 and 0, otherwise</td></tr><tr><td>LastPlayed $_{ict}$ </td><td>Number of days since  $i^{th}$  contestant’s last participation, i.e., number of days between her  $t^{th}$  and  $(t-1)^{th}$  contest</td></tr><tr><td>ExpPaid $_{ict}$ </td><td>Number of paid contests played by the contestant  $i$  before her  $t^{th}$  contest (labelled as ‘c’)</td></tr><tr><td>ExpFree $_{ict}$ </td><td>Number of free contests played by the contestant  $i$  before her  $t^{th}$  contest (labelled as ‘c’)</td></tr></table>

A contestant’s score: There are many factors that affect contestants scores. Some of them are observed, while others are not. Examples of such factors include the number of contests played previously, an in dividual’s ability, the type of contest, etc. Contestants face several random determinants as well. Fantasy points earned by a contestant depends entirely on the performance of her chosen athletes who actually play in the match. Typically, contestants may not be completely aware of all the athlete-specific factors that influence their performance. Furthermore, they have little control over these factors. Additionally, there may be other factors that are also outside of the contestants control (e.g., weather conditions). As such, these are all unpredictable determinants of contestants’ scores, which are denoted as $\eta _ { i c t } .$ . In addi tion, there are parameters that affect winner’s score $( w _ { c } )$ , which are random and beyond the contestant’s control. Since the winnability of a contestant depends on the performance of other competitors, we include the effect of determinants of $w _ { c }$ and denote them as $\delta _ { c }$

The following equation defines a stochastic frontier function. For given $x ,$ the frontier $f ( \boldsymbol { x } , \beta ) e ^ { \delta _ { c } + \eta _ { i c } }$ t denotes the maximum possible score gap and is stochastic because of the two-sided random terms $\delta _ { c }$ and $\eta _ { i c t }$ : y ≤ f (x , β) e<sup>δc+η</sup>ict (2)

where $\eta _ { i c t } \sim N \big [ 0 , \sigma _ { \eta } ^ { 2 } \big ] ; \delta _ { c } \sim N \big [ 0 , \sigma _ { \delta } ^ { 2 } \big ]$ . Since both are independent of each other and normally distributed, we define $\nu _ { i c t } = \eta _ { i c t } + \delta _ { c }$ . This random variable $\nu _ { i c t } \sim N \big [ 0 , \sigma _ { \nu } ^ { 2 } \big ]$ with variance $\sigma _ { \nu } ^ { 2 } = \sigma _ { \eta } ^ { 2 } + \sigma _ { \delta } ^ { 2 }$ . With this trans formation, the above equation becomes:

$$
y _ {i c t} \leq f (x _ {i c t}, \beta) e ^ {\nu_ {i c t}}\tag{3}
$$

We introduce the one-sided disturbance term $u _ { i c t } \geq 0$ , representing the contestant’s time-varying inefficiency. Growth in contestant’s timevarying skill $\left( u _ { i c t } \right)$ reduces the score gap, indicating improvement in the

contestant’s performance:

$$
y _ {i c t} = f (X _ {i c t}, \beta) e ^ {\nu_ {i c t}} e ^ {- u _ {i c t}}\tag{4}
$$

The scores that a contestant receives will vary depending on how she picks the athletes, given the rules of the game. Some of the available athletes are superstars (great performers). Typically, contestants can easily select some of these superstars to raise their scores because their performance signals are strong. Since these athletes are superstars, their inclusion significantly raises a contestant’s score [69] and reduces their score gaps without much skill or intellectual effort. However, the se lection of mid-ranking athletes requires additional skillfulness, experi ence, etc. Therefore, it requires more intellectual energy and skill even to achieve a relatively modest increase in score. This underlying pattern results in a downward-sloping concave relationship between the total score gap and score-enhancing explanatory variables. We represent this relationship between score gaps and performance determinants with the following exponential function:

$$
y _ {i c t} = e ^ {- (X _ {i c t} \beta + \alpha_ {i})} e ^ {\nu_ {i c t} - u _ {i c t}}\tag{5}
$$

Taking log on both sides yields our estimable equation:

$$
\ln \left(\mathbf {y} _ {i c t}\right) = - \left(X _ {i c t} \beta\right) - \alpha_ {i} + v _ {i c t} - u _ {i c t}
$$

Defining $\widetilde { \beta } = - \beta$ and $\widetilde { \alpha } _ { i } = - \alpha _ { i } ,$ , and rearranging (5) yields:

$$
l n (\boldsymbol {y} _ {i c t}) = X _ {i c t} \widetilde {\beta} + \widetilde {\alpha} _ {i} + \nu_ {i c t} - u _ {i c t}\tag{6}
$$

Note that shrinking $l n ( y _ { i c t } )$ implies rising winnability. Hence, a rise in $u _ { i c t }$ lowers $l n ( y _ { i c t } ) .$ , meaning that rise in time-varying inefficiency $\left( u _ { i c t } \right)$ raises winnability.

## 7. Estimation strategy

We estimate (6) to evaluate the role of skill versus chance. As such, the true fixed effect stochastic frontier model [23,24] is suitable for this estimation. As stated above, the estimable equation is:

$$
l n (y _ {i c t}) = X _ {i c t} \widetilde {\beta} + \widetilde {\alpha} _ {i} + v _ {i c t} - u _ {i c t}
$$

In the specific form:

$$
\begin{array}{r l} \ln (S c o r e G a p _ {i c t}) & = \widetilde {\alpha} _ {i} + \beta_ {1} \text {Prop25} _ {i c t} + \beta_ {2} \text {ContestSize} _ {c} + \beta_ {3} \text {ContestType} _ {c} \\ & + \beta_ {4} \text {ExpPaid} _ {i c t} + \beta_ {5} \text {ExpFree} _ {i c t} + \beta_ {6} \text {LastPlayed} _ {i c t} \\ & + v _ {i c t} - u _ {i c t} \end{array}\tag{7}
$$

Log of score gap $( S c o r e G a p _ { i c t } )$ measures a contestant’s score relative to the winner’s score. For a given contest $c ,$ which is the $t ^ { t h }$ contest for contestant $i , S c o r e G a p _ { i c t }$ is the difference between the score of the winner of contest c and $i ^ { t h }$ contestant’s score. Since smaller gaps indicate closer to winning the contest, it measures winnability.

Prop $2 5 _ { i c t }$ measures the contestant’s past performances: Before her $t ^ { \mathrm { { t h } } }$ contest $( \mathrm { i . e . , }$ contest $\prime c \prime )$ , the proportion of times the contestant i was in the top $2 5 ^ { \mathrm { t h } }$ percentile. It considers the consistency of contestants performance in their previous contests. By considering proportion, we are scaling this number by the contestant’s experience. ContestSize represents the number of contestants allowed to participate in the $c ^ { \mathrm { t h } }$ contest. It is a measure of the number of competitors in the $c ^ { \mathrm { t h } }$ contest. ContestType specifies whether the contest $\cdot _ { c } ,$ was a public or a private contest. Public contests are open for all to participate while private contests are closed-group contests; only contestants with the invite link can participate in such contests. $E x p P a i d _ { i c t }$ and $E x p F r e e _ { i c t }$ denote the number of paid and free contests played by the contestant excluding the $t ^ { t h }$ contest (i.e., contest ‘c’), respectively. LastPlayed indicates the number of days since the $i ^ { t h }$ contestant’s last participation, i.e., how recently did she participate in a DFS contest. It captures the recency effect of a contestant’s participation. The term ̃α captures the effect of contestant i’s all time-invariant factors on their winnability. Commonly, this is known as the heterogeneity. This includes time-invariant features such as contestant i’s smartness, prior knowledge, understanding of the game, peer-effect or other similar factors. The one-sided error $u _ { i c t }$ denotes time-varying inefficiency. We interpret this term as the timevariant ability that can only enhance one’s performance [65,70]. Any random time-varying element that only enhances winnability, like contestant’s learning with time, is included in $u _ { i c t }$ . Due to the onesidedness of this term, $u _ { i c t } \geq 0$

## 7.1. Model assumptions

We maintain all the necessary assumptions required for true fixed effect model estimation. To see the viability of these assumptions, consider the elements of the estimable function below:

$$
\begin{array}{r l} \ln (S c o r e G a p _ {i c t}) & = \widetilde {\alpha} _ {i} + \beta_ {1} P r o p 2 5 _ {i c t} + \beta_ {2} C o n t e s t S i z e _ {c} + \beta_ {3} C o n t e s t T y p e _ {c} \\ & \quad + \beta_ {4} E x p P a i d _ {i c t} + \beta_ {5} E x p F r e e _ {i c t} + \beta_ {6} L a s t P l a y e d _ {i c t} \\ & \quad + v _ {i c t} - u _ {i c t} \end{array}\tag{7}
$$

Assumption 1. The components $\nu _ { i c t }$ and $u _ { \mathrm { i c t } }$ are statistically indepen dent. Independence of $\eta _ { \mathrm { i c t } }$ and $u _ { \mathrm { i c t } }$ makes sense in a wide number of circumstances and is widely assumed in this literature [63,65,70,71]. In Eq. $^ { ( 7 ) } ,$ the term $\eta _ { \mathrm { i c t } }$ represents random shocks to the winnability, which is unlikely to influence a contestant’s learnings over time. For instance, a team’s bad performance due to bad weather condition or athletes facing unforeseen injury is unlikely to be related to a contestant’s learnings or skills evolution over time. In a similar way, the determinant of winner’s score, $\delta _ { c } ,$ is unlikely to be related to $u _ { i c t } .$ , making them mutually inde pendent. Since $\nu _ { i c t } = \delta _ { c } + \eta _ { \mathrm { i c t } } .$ , the composite two-sided error $\nu _ { i c t }$ is in dependent of $u _ { i c t } .$

Assumption 2. The one-sided skill $u _ { \mathrm { i c t } }$ is unrelated to all included variables represented by $X _ { \mathrm { i c t } }$ . This assumption is logical since no component of $X _ { \mathrm { i c t } }$ is related to $u _ { \mathrm { i c t } }$ given that we are already controlling for the fixed effect $\widetilde { \alpha } _ { i } .$ . For instance, consider the experience variable measured by the number of contests one plays. It is unlikely that the contestant’s time-varying skills determine how many times they participated in a contest. Similarly, whether the contestant is choosing a private or a public contest is unlikely to be determined by their timevarying skills.

## 7.2. Distribution of $u _ { i c t }$

A critical component of the estimation process is the choice of the distribution for $u _ { i c t }$ . In essence, $u _ { i c t }$ denotes the contestant’s capabilities, which can vary over time. It is on the basis of this interpretation that we choose the form of distribution. According to the influential book “The Bell Curve” [72], abilities follow a bell-shaped pattern. To reflect this assertion, we choose a truncated normal distribution that is capable of resembling a bell-shaped curve:

$$
u _ {i c t} \sim T N ^ {+} [ \mu , \sigma_ {u} ^ {2} ]
$$

The advantage is that truncated normal distribution can easily pro duce a bell-shaped curve in the positive domain of abilities, which is more appropriate for our purposes. Unlike exponential and half-normal distributions, it is more flexible, while being computationally more manageable than gamma distributions. Of course, as a matter of course, to assess the results’ sensitivity to the distributional assumption, we replicate our results with the other distributions as well (Section 8).

## 7.3. Skill versus chance

One of the major objectives of this paper is to examine the degree to which the outcome of DFS contests is influenced by skill rather than chance. To do so, we compare the features of $u _ { i c t }$ and $\nu _ { i c t } .$ As such, u represents the useful knowledge and skills that a contestant acquires regardless of her winning potential. It is not a component of abilities or skills that remains constant over time. It always contributes positively to winnability, though the extent of the contribution may vary from time to time. In contrast, a chance would imply that no one knows what the outcome will be. A random shock can contribute positively or negatively to winnability. The fact that $\nu _ { i c t }$ meets that requirement makes it a suitable candidate to represent the chance component.

To implement it empirically, we compare the variance in score-gap explained by a contestant’s skill $( \sigma _ { u } ^ { 2 } )$ to the variance of the random chance $( \sigma _ { \nu } ^ { 2 } )$ . This particular comparison was made possible as the sto chastic frontier analysis enables one to compute these variance terms. The parameters of model $( 7 )$ are estimated using maximum likelihood estimation. For estimation of $u _ { i c t } ,$ the conditional estimator of $\dot { u } _ { i c t }$ (JLMS) [73] is used. For the normal-truncated normal specification, the JLMS estimator is given as [23]:

$$
E \left(u _ {i c t} \mid \varepsilon_ {i c t}\right) = \left(\frac {\sigma \lambda}{1 + \lambda^ {2}}\right) \left[ \widetilde {\mu} _ {i t} + \frac {\phi (\widetilde {\mu} _ {i c t})}{\Phi (\widetilde {\mu} _ {i c t})} \right]\tag{8}
$$

where $\begin{array} { r } { \varepsilon _ { i c t } = ( \nu _ { i c t } - u _ { i c t } ) , \widetilde { \mu } _ { i c t } = \bigg ( \frac { \mu \sigma _ { u } ^ { 2 } } { \sigma ^ { 2 } } \bigg ) - \bigg ( \frac { \lambda \varepsilon _ { i c t } } { \sigma } \bigg ) . \phi ( . ) } \end{array}$ and $\Phi ( . )$ are the density and CDF of standard normal distribution, respectively. We examine the signal-to-noise ratio of the model to determine the relative importance of skill and chance.

As such, we consider:

$$
\lambda = \frac {\sigma_ {u} ^ {2}}{\sigma_ {\nu} ^ {2}}\tag{9}
$$

and test the hypothesis:

$$
H _ {0}: \lambda \leq 1 \text {   against   } H _ {A}: \lambda > 1
$$

The value λ = 1 indicates that neither skill nor chance has a relative dominant influence on winnability. $\lambda < 1$ indicates chance dominates skill. $\mathrm { I f } \lambda > 1$ , however, skill dominates chance, albeit to what extent will depend on the magnitude of λ. If λ is large, skill is significantly more dominant than chance, and vice versa. We not only use the value of λ as an indicator of skill-chance dominance in DFS contests, but also quantify the effect of other indicators of a skill-dominant game, i.e., a positive relation between the contestant’s experience, winning consistency, and choice of contest on winnability, as explained at the end of Section 5.

## 8. Results

We find that skill plays a dominant role in determining winnability in cricket-based DFS contests. As such, four major results emerge from our analysis. First, consistent high performers in the past are likely to perform well in current contests. Second, contestants who participated recently, tend to exhibit higher winnability. Third, choice of the contest influences contestants’ winnability. Fourth, contestants with more experience with paid contests tend to exhibit higher winnability, while contestants with more experience with free contests do not show any additional winning capacity. Fifth, the unobserved components of skill play a far greater role in determining winnability than pure random shocks. All these findings together strongly suggest that cricket-based DFS is a skill-dominant game. If not, none of the above factors would determine winnability, but that is not the case here.

To see these in detail, consider Model 1 of Table 4, our benchmark model. This shows that a one percentage-point increase in the variable Prop25 reduces the score gap by 17 percent (Model 1 corresponds to Eq. (7)). As defined already, Prop25 measures the proportion of times a contestant appears within the top $2 5 ^ { \mathrm { t h } }$ percentile of the scoring distri bution in her previous contests. Thus, this positive effect indicates that consistently high-performing contestants perform better in the current

Result from Eqs. (7), (10)–(12).

<table><tr><td>Variables</td><td>Model (1)(Corresponds to Eq. (7))</td><td>Model (2)(Corresponds to Eq. (11))</td><td>Model (3)(Corresponds to Eq. (12))</td><td>Model (4)(Corresponds to Eq. (10))a</td></tr><tr><td>Prop40</td><td></td><td>-0.103*(0.045)</td><td></td><td></td></tr><tr><td>Prop25</td><td>-0.184**(0.049)</td><td></td><td></td><td>-0.186**(0.05)</td></tr><tr><td>Prop10</td><td></td><td></td><td>-0.31**(0.057)</td><td></td></tr><tr><td>ContestSize</td><td>0.1 × 10-3**(1.5 × 10-5)</td><td>0.1 × 10-3**(1.5 × 10-5)</td><td>0.1 × 10-3**(1.5 × 10-5)</td><td>1.52 × 10-6**(3.76 × 10-7)</td></tr><tr><td>ContestType (Public)</td><td>-0.337**(0.063)</td><td>-0.337**(0.063)</td><td>-0.336**(0.063)</td><td>-0.330**(0.063)</td></tr><tr><td>ExpPaid</td><td>-0.81 × 10-4*(0.4 × 10-4)</td><td>-0.8 × 10-4*(0.4 × 10-4)</td><td>-0.81 × 10-4*(0.4 × 10-4)</td><td>-0.95 × 10-4*(0.41 × 10-4)</td></tr><tr><td>ExpFree</td><td>1.71 × 10-5(0.13 × 10-4)</td><td>1.67 × 10-5(0.14 × 10-4)</td><td>1.65 × 10-5(0.13 × 10-4)</td><td>2.00 × 10-5(0.14 × 10-4)</td></tr><tr><td>LastPlayed</td><td>1.38 × 10-3**(0.29 × 10-3)</td><td>1.39 × 10-3**(0.29 × 10-3)</td><td>1.37 × 10-3**(0.29 × 10-3)</td><td>1.40 × 10-3**(0.28 × 10-3)</td></tr><tr><td>CovidDummy</td><td></td><td></td><td></td><td>0.132(0.103)</td></tr><tr><td>σu2</td><td>3.143**(0.073)</td><td>3.143**(0.072)</td><td>3.143**(0.072)</td><td>3.205**(0.081)</td></tr><tr><td>σv2</td><td>0.362**(0.003)</td><td>0.362**(0.004)</td><td>0.362**(0.004)</td><td>0.361**(0.003)</td></tr><tr><td>λ</td><td>8.683**(0.074)</td><td>8.685**(0.074)</td><td>8.68**(0.073)</td><td>8.88**(0.082)</td></tr></table>

\*\*p < 0.01, $\begin{array} { r } { { \bf \ddot { \rho } } p < 0 . 0 5 . } \end{array}$ Robust standard errors in parentheses  
Note: Since the above formulation is log-linear, we apply 100 $\times \left[ e ^ { \beta } - 1 \right]$ to compute the partial effects.  
<sup>a</sup> These results are based on the updated dataset that includes contestants from 2020-23. Since the updated timeline includes Covid-19-impacted years, which had an impact on the number of on-field matches and the match format, thereby possibly affecting the scores and score gaps, we introduce a dummy variable in the model to control these effects:  
ln(ScoreGap ) = ̃α + β Prop25 + β ContestSize + β ContestType + β ExpPaid + β ExpFree + β LastPlayed + β CovidDummy $+ \nu _ { i c t } - u _ { i c t }$

(10)

contests. As such, this is our first result showing that capabilities matter in DFS contests. A pure chance-based game would mean that past per formances would not determine a contestant’s present performances.

We also find that the contest type matters. Whether a contest is private (the variable ContestType), and whether a contest admits a large number of contestants (the variable ContestSize) influence the contes tant’s relative performance. Usually, the participants of private contests show a higher degree of homogeneity, even though they may not have known about their fellow contestants at the time of selecting athletes. Hence, on average, one would expect a smaller score gaps (higher competitiveness) in private contests. The results support this hypothesis. Table 4 Model (1) shows that contestants in private contests tend to have about 29 percent lower score gap on average than the ones participating in public contests. On the impact of contest size, we hypothesized that for larger contests, average scores gaps should be bigger as larger con tests tend to enroll more heterogeneous contestants. Our results support this hypothesis, though the impact is rather moderate. With every 100 additional contestants, the score gap rises by 1 percent on average, holding other factors constant.

Additionally, our results show that playing experience matters. Table 4 shows that contestants who played higher number of paid contests in the past (i.e., ExpPaid) tend to be closer to the winning scores. All else equal, one additional paid contest played in the past tends to lower the score gap by 0.0081 percent, on average. This result is somewhat expected. Compared to free contests, paid contests are the ones where contestants usually put in substantial effort and carefully construct their teams. This arguably leads to better learnings from experience, which often reflects through their future performances. This finding clearly indicates that people learn from experience which en hances their productivity, which is contrary to the hypothesis that DFS is a chance-based sports. In the case of free contests, we find that the experience gained does not have a significant effect on the contestant’s

winnability.

We find that the variable LastPlayed has a significant effect on the dependent variable, the score gap. The positive coefficient suggests that with an increasing number of days since the contestant’s last partici pation, there is an increase in the score gap. Contestants participating in DFS after a gap of 30 days tend to have 4 percent increase in their score gap on average, holding other factors constant. In other words, contes tants who participated recently, exhibit higher winnability, which is consistent with the concept of skill depreciation used in human capital theory [74]. As reported by Edin & Gustavsson [75], who study the relation between time out of work and skill depreciation, time out of employment leads to human capital depreciation viz. longer time out is associated with larger loss of skills.

Another strong evidence in favor of skill-dominant hypothesis is that variance of unobserved skill appears to be far more important than chance. As explained already, $u _ { i c t }$ represents the unobserved skill and $\nu _ { i c t }$ represents the chance elements. Given this structure, the dominance of u over $\nu _ { i c t }$ in explaining the variance of skill gap would indicate that the game is skill-dominant. In other words, if the variance of $u _ { i c t } \left( i . e . , \sigma _ { u } ^ { 2 } \right)$ is larger than the variance of $\nu _ { i c t } \left( \mathrm { i } . \mathrm { e } . , \sigma _ { \nu } ^ { 2 } \right)$ , one can infer that skill is more important than chance. We indeed find that variances are different from zero (i.e., $\sigma _ { u } ^ { 2 } > 0 ; \sigma _ { \nu } ^ { 2 } > 0 )$ and $\sigma _ { u } ^ { 2 } > \sigma _ { \nu } ^ { 2 } .$ . First, our estimates suggest that $\sigma _ { u } ^ { 2 } = \ 3 . 1 4 2$ and $\sigma _ { \nu } ^ { 2 } = \ 0 . 3 6 2$ . Both these are statistically significant meaning that both unobserved skill and chance determine winnability Secondly, the signal-to-noise ratio estimate indicates that $\begin{array} { r } { \frac { \sigma _ { u } ^ { 2 } } { \sigma _ { \nu } ^ { 2 } } = 8 . 6 8 3 . } \end{array}$ This is statistically significant and above 1. meaning the game is skilldominant (See Appendix A). As such, this evidence shows that skills of various kinds matter significantly in determining a contestant’s perfor mance in DFS.

## 8.1. Estimated distribution of unobserved skill

To assess the unobserved skill further, we construct the conditional mean of $u _ { i c t }$ given the estimated composite error $( \mathrm { i . e . , } E [ u _ { i c t } | \widehat { \epsilon } _ { i c t } ] )$ based on [73]. As such, these values serve as the best linear unbiased predictor of $u _ { i c t } . \ \mathrm { F i g } . \ 2$ presents the distribution of $E [ u _ { i c t } | \widehat { \epsilon } _ { i c t } ]$ . Two points are noteworthy here. First, the estimated distribution looks like a somewhat bell-shaped distribution, which is similar to the distribution of skill postulated by many [72]. Most of the contestants have skills around the average skill, only a limited number of contestants exhibit high skills, while very few have extremely low skills. Second, the average estimated skill is 2.1, which is approximately 77 percent of the average log of skill gap. This estimate confirms that unobserved skill accounts for a signif icant portion of contestants’ winnability.

## 8.2. Sensitivity analysis

In the analysis presented in the previous section, Prop25 serves as a measure of contestants’ past performance. This is our constructed vari able. To examine whether the findings are dependent on the method of defining past performance variables, we replicated the exercise using two alternate definitions of the term: Prop40 and Prop10. Prop40 (see Eq. (10)) measures the proportion of times a contestant appears within the top $4 0 ^ { \mathrm { t h } }$ percentile of the scoring distribution in her previous contests; and Prop10 (see Eq. (11)) measures the proportion of times a contestant appears within the top $1 0 ^ { \mathrm { t h } }$ percentile of the scoring distribution in her previous contests:

Table 5  
Choice of inefficiency distribution.

<table><tr><td>Variables</td><td>Truncated Normal</td><td>Half Normal</td><td>Exponential</td></tr><tr><td>Prop25</td><td>-0.184**(0.049)</td><td>-0.187**(0.05)</td><td>-0.172**(0.046)</td></tr><tr><td>Contest Size</td><td>0.1 × 10-3**(1.5 × 105)</td><td>0.11 × 10-3**(1.6 × 105)</td><td>0.8 × 10-4**(9.36 × 10-6)</td></tr><tr><td>ContestType (Public)</td><td>-0.337**(0.063)</td><td>-0.35**(0.06)</td><td>-0.3**(0.06)</td></tr><tr><td>ExpPaid</td><td>-0.81 × 10-4*(0.4 × 104)</td><td>-0.8 × 10-4*(4.25 × 10-5)</td><td>-0.89 × 10-4*(3.85 × 10-5)</td></tr><tr><td>ExpFree</td><td>1.71 × 10-5(0.13 × 104)</td><td>1.77 × 10-5(1.38 × 10-5)</td><td>1.61 × 10-5(1.23 × 10-5)</td></tr><tr><td>LastPlayed</td><td>1.38 × 10-3**(0.29 × 10-3)</td><td>1.34 × 10-3**(0.31 × 10-3)</td><td>1.48 × 10-3**(2.74 × 10-4)</td></tr><tr><td>σu2</td><td>3.143**(0.073)</td><td>2.864**(0.019)</td><td>2.052**(0.021)</td></tr><tr><td>σv2</td><td>0.362**(0.003)</td><td>0.351**(0.005)</td><td>0.42**(0.005)</td></tr><tr><td>λ</td><td>8.683**(0.074)</td><td>8.153**(0.017)</td><td>4.886**(0.018)</td></tr></table>

Note: Since the above formulation is log-linear, we apply $1 0 0 \times \left[ \mathbf { e } ^ { \beta } - 1 \right]$ to compute the partial effects.  
${ } ^ { \ast \ast } p < 0 . 0 1 ,$ ${ } ^ { \ast } p < 0 . 0 5 .$ . Robust standard errors in parentheses

Model 2 to Model 3), the score gap decreases drastically. One percentage point increase in the variable Prop40 reduces the score gap by 10 percent, while one percentage point increase in the variable Prop10 reduces the score gap by 27 percent. Therefore, better past performers

$$
\ln (S c o r e G a p _ {i c t}) = \widetilde {\alpha} _ {i} + \beta_ {1} P r o p 4 0 _ {i c t} + \beta_ {2} C o n t e s t S i z e _ {c} + \beta_ {3} C o n t e s t T y p e _ {c} + \beta_ {4} E x p P a i d _ {i c t} + \beta_ {5} E x p F r e e _ {i c t} + \beta_ {6} L a s t P l a y e d _ {i c t} + v _ {i c t} - u _ {i c t}\tag{11}
$$

$$
l n (S c o r e G a p _ {i c t}) = \widetilde {\alpha} _ {i} + \beta_ {1} P r o p 1 0 _ {i c t} + \beta_ {2} C o n t e s t S i z e _ {c} + \beta_ {3} C o n t e s t T y p e _ {c} + \beta_ {4} E x p P a i d _ {i c t} + \beta_ {5} E x p F r e e _ {i c t} + \beta_ {6} L a s t P l a y e d _ {i c t} + v _ {i c t} - u _ {i c t}\tag{12}
$$

These estimates confirm the qualitative results of the benchmark model above. All three models produce virtually similar results. As we move from the top $4 0 ^ { \mathrm { t h } }$ percentile to the top $1 0 ^ { \mathrm { t h } }$ percentile (see Table 4:

tend to perform better in the present and future contests, irrespective of the definition of past performance.

![](/api/attachments/76SFVURK/fulltext/images/666cf46eb50d81732dc938fc4b2a672a1ae2a9d2a69f981f7e29fd604a2eb8d8.jpg)  
Fig. 2. Kernel density estimate of contestants’ mean inefficiency.

Pearson and spearman rank correlations for inefficiency estimates.<sup>1</sup>

<table><tr><td></td><td>Truncated Normal</td><td>Half Normal</td><td>Exponential</td></tr><tr><td>Truncated Normal</td><td>1</td><td>0.9998</td><td>0.9981</td></tr><tr><td>Half Normal</td><td>0.9999</td><td>1</td><td>0.9976</td></tr><tr><td>Exponential</td><td>0.9987</td><td>0.9984</td><td>1</td></tr></table>

<sup>1</sup> Spearman rank correlations above the diagonal; Pearson correlations below the diagonal (Results based on a sample of 200 contestants)

![](/api/attachments/76SFVURK/fulltext/images/dac39a000c61205ef99b46a7473a9bb67dd875849f605c5c085153d6367e2aa5.jpg)  
Fig. 3. Decision support framework to distinguish games of skill and games of chance.

## 8.3. Robustness to the choice of distribution of $u _ { i c t }$

Our benchmark model assumes that the distribution of the unob served skill is truncated normal. To check the robustness of the findings with respect to the choice of this distribution, we replicate our estima tion for two separate distributions, half-normal and exponential, for the unobserved skills $\left( u _ { i c t } \right)$ . As such, the results from Table 5 show that slope parameter estimates are stable, irrespective of the choice of the distributions.

We also find that the different distributional assumptions did not make much difference in $\sigma _ { u } ^ { 2 } , \sigma _ { \nu } ^ { 2 }$ estimates, though the signal-to-noise ratio is somewhat lower in case of the exponential distribution. Addi tionally. we also find that estimates of skills $( E [ u _ { i c t } | \widehat \epsilon _ { i c t } ] )$ from different distributions of $u _ { i c t }$ are highly correlated. Table 6 shows that the raw and rank correlations among these estimates are strikingly similar and range between 0.997 and 0.999. This high correlation estimates support the previous studies on sensitivity of the inefficiency estimates to the choice of distributions [70,71].

## 9. Conclusion and implication

This paper proposes a data-driven approach to address the skill versus chance dominance debate in Daily Fantasy Sports (DFS). The approach adopted by legal bodies to resolve this issue is often subjective in nature, resulting in inconsistent judgments and loss of business rev enue [14]. This study presents a decision support framework that quantifies the effect of contestants’ skill and chance on contestants performance, and then objectively determines the dominant factor. Using a true fixed-effect stochastic frontier technique, we model con testants’ skills and the random chances they face as two distinct error components determining their success in DFS contests. Taking the case of cricket-based DFS contests, we utilize anonymized data from Dream11, a prominent Indian DFS operator, and find that the effect of the contestant’s skill is significantly more than that of chance, in determining the winnability in a DFS contest. This finding strongly suggests that DFS is a skill-dominant game. We also quantify other in dicators of skill, like contestants’ past performance, experience, recent participation and their choice of contest, and find that these have sig nificant effect on their performance in a DFS contest.

This paper offers an integrated decision support framework that a.) evaluates relative importance of skill and chance, b.) studies a contes tant’s observed and unobserved characteristics, c.) tests for other in dicators of skill, and d.) can be replicated to other games, subject to data availability. Fig. 3 presents a framework that can utilize data from an online gaming platform and test for skill dominance, using the approach proposed in this paper. This framework has implications for policy makers who have emphasized the need of a data-driven approach to resolve the ongoing debate of skill versus chance dominance in DFS and other online gaming platforms [61]. With the proposed approach, we contribute to the literature on data-driven decision-making that can help the DFS business and regulators adopt a quantitative approach to address this problem, thus promoting evidence-based decision-making.

## CRediT authorship contribution statement

Aishvarya: Writing – review & editing, Writing – original draft, Methodology, Formal analysis, Data curation, Conceptualization. Tir thatanmoy Das: Writing – review & editing, Supervision, Methodology, Conceptualization. U. Dinesh Kumar: Writing – review & editing, Su pervision, Resources, Conceptualization.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

The authors do not have permission to share data.

## Appendix A. Appendix

To evaluate dominance of $\sigma _ { \mathrm { u } } ^ { 2 }$ over $\sigma _ { \mathrm { v } } ^ { 2 } ,$ the hypothesis is formulated as:

$H _ { o } : \sigma _ { u } ^ { 2 } \le \sigma _ { \nu } ^ { 2 }$ against $H _ { a } : \sigma _ { u } ^ { 2 } > \sigma _ { \nu } ^ { 2 }$

We reject $\mathrm { H } _ { 0 }$ at 1% level of significance $( F _ { \alpha } = 1 . 0 1 $ and F-statisti $: = 8 . 6 )$

Appendix B. Appendix

Table A.1  
Summary statistics.

<table><tr><td></td><td>Mean</td><td>Max</td><td>Min</td><td>SD</td></tr><tr><td>Points Scored by Contestant</td><td>267</td><td>1609</td><td>2</td><td>122</td></tr><tr><td>Contest Size</td><td>12</td><td>8770</td><td>2</td><td>188</td></tr><tr><td>Experience in Paid Contests</td><td>235</td><td>969</td><td>1</td><td>205</td></tr><tr><td>Experience in Free Contests</td><td>372</td><td>11683</td><td>1</td><td>707</td></tr><tr><td>Highest Score in a Contest</td><td>309.8</td><td>1608.5</td><td>2.5</td><td>131.7</td></tr><tr><td>Score Gap</td><td>42</td><td>703.75</td><td>0</td><td>49</td></tr></table>

## Appendix C. Appendix

The following is a list of all notations and abbreviations used in the study:

<table><tr><td>DFS</td><td>Daily Fantasy Sports</td></tr><tr><td>OFS</td><td>Online Fantasy Sports</td></tr><tr><td>TFE</td><td>True Fixed Effects</td></tr><tr><td> $S_{ict}$ </td><td>Score of contestant i in her  $t^{th}$  contest (labelled as contest ‘c’)</td></tr><tr><td> $w_c$ </td><td>Score of the winner of contest c</td></tr><tr><td> $ScoreGap_{ict}\ or\ y_{ictv}$ </td><td>ifference in a contestant’s score and winner’s score ( $w_c - S_{ict}$ )</td></tr><tr><td> $PropM_{ict}$ </td><td>Proportion of times contestant i was in the top ‘M’ percentile before her  $t^{th}$  contest (i.e., contest ‘c’), where M = 10, 25, 40</td></tr><tr><td> $ContestSize_c$ </td><td>Number of contestants allowed to participate in contest c</td></tr><tr><td> $ContestType_c$ </td><td>1, if the contest c was a private contest and 0, if it was a public contest</td></tr><tr><td> $CovidDummy_c$ </td><td>1, if the contest c was played in 2020-21 and 0, otherwise</td></tr><tr><td> $ExpPaid_{ict}$ </td><td>No. of paid contests played by contestant i before her  $t^{th}$  contest (contest ‘c’)</td></tr><tr><td> $ExpFree_{ict}$ </td><td>No. of free contests played by contestant i before her  $t^{th}$  contest (contest ‘c’)</td></tr><tr><td> $\delta_c$ </td><td>Unpredictable determinants of score of  $c^{th}$  contest’s winner</td></tr><tr><td> $\eta_{ict}$ </td><td>Unpredictable determinants of contestant i’s score in her  $t^{th}$  contest (contest ‘c’)</td></tr><tr><td> $v_{ict}$ </td><td> $\eta_{ict} + \delta_c$ . Denotes time-varying chance elements influencing contestant i’s winnability in her  $t^{th}$  contest (i.e., contest ‘c’)</td></tr><tr><td> $\sigma_v^2$ </td><td> $\sigma_\eta^2 + \sigma_\delta^2$ . Denotes variance in time-varying chance elements</td></tr><tr><td> $\widetilde{\alpha}_i$ </td><td>Contestant (i)-specific effects</td></tr><tr><td> $u_{ict}$ </td><td>Time-varying inefficiency of contestant i in her  $t^{th}$  contest (i.e., contest ‘c’)</td></tr><tr><td> $\sigma_u^2$ </td><td>Variance in time-varying inefficiency</td></tr><tr><td> $\varepsilon_{ict}$ </td><td> $v_{ict} - u_{ict}$ </td></tr><tr><td>μ :</td><td>Mean value of time-varying inefficiency</td></tr><tr><td>λ</td><td> $\frac{\sigma_u^2}{\sigma_v^2}$  Indicates relative importance of inefficiency and chance</td></tr></table>

## Appendix D. Supplementary data

Supplementary data to this article can be found online at https://doi.org/10.1016/j.dss.2024.114237.

## References

[1] C.H. Antunes, L.C. Dias, Managing uncertainty in decision support models foreword to the special issue, Decis. Support. Syst. 43 (2007) 1451–1453, https:// doi.org/10.1016/j.dss.2006.06.007.

[2] J. Kay, M. King, Radical Uncertainty: Decision-making for an Unknowable Future, The Bridge Street Press. London 2020

[3] F. Burstein, G. Widmeyer, Decision support in an uncertain and complex world, Decis. Support. Syst. 43 (2007) 1647–1649, https://doi.org/10.1016/j. dss.2006.09.001.

[4] D. Roberts, DraftKings and FanDuel Banned in New York After New Ruling, Fortune. https://fortune.com/2015/12/11/draftkings-fanduel-shut-down-in-new york/, 2015 (accessed November 22, 2022).

[5] S. Vikas, Tamil Nadu cabinet passes ordinance to ban online games with stakes, MoneyControl. https://www.moneycontrol.com/news/business/tamil-nadu-cabin et-passes-ordinance-banning-online-games-with-stakes-9234211.html. 2022 (accessed November 22, 2022).

[6] Arizton Advisory & Intelligence, Fantasy Sports Market, Size, Share Report 2026. https://www.arizton.com/market-reports/fantasy-sports-market, 2021 (accessed October 29. 2022).

[7] FIFS, The Business of Fantasy Sports. A Study in Collaboration with KPMG in India. https://fifs.in/publication/. 2020 (accessed June 29. 2021)

[8] D. Getty, H. Li, M. Yano, C. Gao, A.E. Hosoi, Luck and the law: quantifying chance in fantasy sports and other contests, SIAM Rev. 60 (2018) 869–887, https://doi. org/10.1137/16M1102094.

[9] Varun Gumber v. Union Territory of Chandigarh, 2017.

[10] S. Imranullah, Court Strikes Down TN Law Banning Online Games with Stakes - The Hindu. https://www.thehindu.com/news/national/tamil-nadu/court-strikes-d own-tn-law-banning-online-games-with-stakes/article35697113.ece, 2021 (accessed September 20, 2021).

[11] Gurdeep Singh Sachar v. Union of India and Others, 2019.

[12] D. Choudhary, S. Jacob, Karnataka HC lifts online gaming ban, big relief for fantasy sports, Bus. Stand. News (2022). https://www.business-standard.com/article /companies/karnataka-high-court-strikes-down-state-govt-ban-on-online-gamblin g-122021400527\_1.html (accessed October 29, 2022).

[13] R. Croson, P. Fishman, D.G. Pope, Poker superstars: Skill or luck? Chance 21 (2008) 25–28, https://doi.org/10.1007/s00144-008-0036-0.

[14] S.D. Levitt, T.J. Miles, A.M. Rosenfield, Is Texas hold ’em a game of chance? A legal and economic analysis, Georgetown Law J. 101 (2013) 581–636.

[15] S.D. Levitt, T.J. Miles, The role of skill versus luck in poker evidence from the world series of poker, J. Sports Econ. 15 (2014) 31–44, https://doi.org/10.1177/ 1527002512449471.

[16] D.G. Morrison, M.U. Kalwani, The best NFL field goal kickers: are they lucky or good? in: J. Albert, J. Bennett, J.J. Cochran (Eds.). Anthology of Statistics in Sports Society for Industrial and Applied Mathematics, 2005, pp. 45–52, https://doi.org/ 10.1137/1.9780898718386.ch7

[17] C. Reep, R. Pollard, B. Benjamin, Skill and chance in ball games, J. R. Stat. Soc. Ser. A (Gen.) 134 (1971) 623, https://doi.org/10.2307/2343657.

[18] C. Reep, B. Benjamin, Skill and chance in association football, J. R. Stat. Soc. Ser. A (Gen.) 131 (1968) 581, https://doi.org/10.2307/2343726.

[19] B. Green, J. Zwiebel, The hot-hand fallacy: cognitive mistakes or equilibrium adjustments? Evidence from major league baseball, Manag. Sci. 64 (2018) 5315–5348, https://doi.org/10.1287/mnsc.2017.2804.

[20] G.R. Lindsey, The progress of the score during a baseball game, J. Am. Stat. Assoc. 56 (1961) 703–728, https://doi.org/10.1080/01621459.1961.10480656.

[21] D. Jackson, K. Mosurski, Heavy defeats in tennis: psychological momentum or random effect? in: J. Albert. J. Bennett. JJ. Cochran (Eds.). Anthology of Statistics in Sports Society for Industrial and Applied Mathematics, 2005, pp. 303–310, https://doi.org/10.1137/1.9780898718386.ch42

[22] T. Easton, S. Newell, Are daily fantasy sports gambling? JSA 5 (2019) 35–43, https://doi.org/10.3233/JSA-180240.

[23] W. Greene, Fixed and random effects in stochastic frontier models, J. Prod. Anal. 23 (2005) 7–32, https://doi.org/10.1007/s11123-004-8545-1.

[24] W. Greene, Distinguishing between heterogeneity and inefficiency: stochastic frontier analysis of the World Health Organization’s panel data on national health care systems, Health Econ. 13 (2004) 959–980, https://doi.org/10.1002/hec.938.

[25] B.J. Ruihley, J. Chamberlin, The history and evolution of the fantasy sport voice: an oral account of the major aspects forming the fantasy sports and gaming association, Int. J. Hist. Sport 38 (2021) 135–151, https://doi.org/10.1080/ 09523367.2021.1876675

[26] IFSG, KPMG, The Evolving Landscape of Sports Gaming in India. https://assets. kpmg/content/dam/kpmg/in/pdf/2019/03/online-gaming-india-fantasy-sports. pdf, 2019.

[27] FIFS. Deloitte, Fantasy Sports: Creating a Virtuous Cycle of Sports Development https://www2.deloitte.com/in/en/pages/technology-media-and-telecommun cations/articles/fantasy-sports.html, 2022 (accessed June 13, 2022).

[28] K. Singh, Big game: How a fantasy sports startup is making money from India’s IPL fever, Scroll.In, 2019. https://scroll.in/article/919582/big-game-how-a-fantasy-s ports-startup-is-making-money-from-indias-ipl-fever (accessed October 29, 2021).

[29] F. Zambom-Ferraresi, V. Rios, F. Lera-Lopez, ´ Determinants of sport performance in European football: What can we learn from the data? Decis. Support. Syst. 114 (2018) 18–28, https://doi.org/10.1016/j.dss.2018.08.006.

[30] M.D. Bailey, M. Nowak, MeetOpt: A multi-event coaching decision support system, Decis. Support. Syst. 112 (2018) 60–75, https://doi.org/10.1016/j. dss.2018.06.007.

[31] M.B. Haugh, R. Singal, How to play fantasy sports strategically (and win), Manag. Sci. 67 (2021) 72–92, https://doi.org/10.1287/mnsc.2019.3528.

[32] M. Muniz, T. Flamand, Sports analytics for balanced team-building decisions, J. Oper. Res. Soc. (2022) 1–18, https://doi.org/10.1080/ 01605682.2022.2118634

[33] H.A. Arslan, R.F. Easley, R. Wang, O. <sup>¨</sup> Yılmaz, Data-driven sports ticket pricing for multiple sales channels with heterogeneous customers, M&SOM 24 (2022) 1241-1260. https://doi.org/10.1287/msom.2021.1005

[34] R.P. Schumaker, A.T. Jarmoszko, C.S. Labedz, Predicting wins and spread in the Premier League using a sentiment analysis of twitter, Decis. Support. Syst. 88 (2016) 76–84. https://doi.org/10.1016/i.dss.2016.05.010

[35] J.H. Hyeong, K.J. Choi, J.Y. Lee, T.-H. Pyo, For whom does a game update? Players’ status-contingent gameplay on online games before and after an update, Decis. Support. Syst. 139 (2020) 113423, https://doi.org/10.1016/j. dss.2020.113423.

[36] G.-Y. Liao, T.C.E. Cheng, W.-L. Shiau, C.-I. Teng, Impact of online gamers conscientiousness on team function engagement and loyalty, Decis. Support. Syst. 142 (2021) 113468, https://doi.org/10.1016/i.dss.2020.113468.

[37] R.P. Schumaker, C.S. Labedz, A.T. Jarmoszko, L.L. Brown, Prediction from regional angst – A study of NFL sentiment in Twitter using technical stock market charting Decis, Support, Syst. 98 (2017) 80–88. https://doi,org/10.1016/i,dss,2017.04.010.

[38] J. Miklós-Thal, H. Ullrich, Career prospects and effort incentives: evidence from professional soccer, Manag, Sci. 62 (2016) 1645–1667, https://doi.org/10.1287/

[39] S.S. Padhi, S. Mukherjee, Optimal portfolio choices to split orders during supply disruptions: An application of sport's principle for routine sourcing, Decis, Sci. (2021), https://doi.org/10.1111/deci.12511.

[40] S. Szymanski, The Economic Design of Sporting Contests, J. Econ. Lit. 41 (2003) 1137–1187.

[41] F. Fonti, J.-M. Ross, P. Aversa, Using sports data to advance management research: a review and a guide for future studies, J. Manag. (2022), https://doi.org 10.1177/01492063221117525.

[42] K.W. Rockmann, A Whole Different Ball Game—Exploring the Modern Organizational Context Through the Lens of Sports [Special Research Forum], Academy of Management Discoveries, 2022.

[43] A. Baerg, Just a fantasy? Exploring fantasy sports, Electron. J. Commun. 19 (2009) 3–4.

[44] S.G. Hill, C.W. Woo, New media, new audiences, and new questions: exploring a communication research agenda for fantasy sports, J. Sports Media 6 (2011) 85–114, https://doi.org/10.1353/jsm.2011.0005.

[45] R. Tacon, S. Vainker, Fantasy sport: a systematic review and new research directions, Eur. Sport Manag. Q. 17 (2017) 558–589, https://doi.org/10.1080 16184742.2017.1347192.

[46] B. Bernhard, V. Eade, Gambling in a fantasy world: an exploratory study of rotisserie baseball games, UNLV Gaming Res. Rey. J. 9 (2012). https://digitalscho larship.unlv.edu/grrj/vol9/iss1/3

[47] S.M. Weiss, R.M. Demski, G.J. Backen, Fantasy baseball: A new way to gamble or just another game? JGI 126 (2011) https://doi.org/10.4309/jgi.2011.26.9.

[48] R.J. Martin, S. Nelson, Fantasy sports, real money: Exploration of the relationship between fantasy sports participation and gambling-related problems, Addict. Behav. 39 (2014) 1377–1382, https://doi.org/10.1016/j.addbeh.2014.05.017.

[49] R.J. Martin, S.E. Nelson, A.R. Gallucci, Game on: past year gambling, gamblingrelated problems, and fantasy sports gambling among college athletes and nonathletes, J. Gambl. Stud. 32 (2016) 567–579, https://doi.org/10.1007/s10899- 015-9561-y.

[50] E.F. Fama, K.R. French, Luck versus skill in the cross-section of mutual fund returns, J. Financ. 65 (2010) 1915–1947, https://doi.org/10.1111/j.1540- 6261.2010.01598.x

[51] K. Cuthbertson, D. Nitzsche, N. O’Sullivan, UK mutual fund performance: Skill or luck? J. Empir. Financ. 15 (2008) 613–634, https://doi.org/10.1016/j. iempfin.2007.09.005

[52] R.J. Kauffman, T.J. Spaulding, C.A. Wood, Are online auction markets efficient? An empirical study of market liquidity and abnormal returns, Decis. Support. Syst. 48 (2009) 3–13. https://doi.org/10.1016/i.dss.2009.05.009

[53] M. Bertrand, S. Mullainathan, Are CEOs rewarded for luck? The ones without principals are, Q. J. Econ. 116 (2001) 901–932, https://doi.org/10.1162 00335530152466269.

[54] A. Alvarez, P. Schmidt, Is skill more important than luck in explaining fish catches? J. Prod. Anal, 26 (2006) 15–25, https://doi.org/10.1007/s11123-006-0002-x

[55] P.E.M. Borm, M.R.M. Dreef, B.B. Van Der Genugten, Measuring skill in games: Several approaches discussed — Tilburg University Research Portal, Math, Meth Oper, Res, 59 (2004) 375–391.

[56] P. Larkey, J.B. Kadane, R. Austin, S. Zamir, Skill in games, Manag. Sci. 43 (1997) 596–609, https://doi.org/10.1287/mnsc.43.5.596.

[57] Y.-C. Chou, B.B.M. Shao, W.T. Lin, Performance evaluation of production of IT capital goods across OECD countries: A stochastic frontier approach to Malmquist index, Decis. Support. Syst. 54 (2012) 173–184, https://doi.org/10.1016/j. dss.2012.05.003

[58] C.-M. Chen, J. Du, J. Huo, J. Zhu, Undesirable factors in integer-valued DEA: Evaluating the operational efficiencies of city bus systems considering safety records, Decis. Support. Syst. 54 (2012) 330–335, https://doi.org/10.1016/j. dss.2012.05.040.

[59] M. Jabbari, S. Sheikh, M. Rabiee, A. Oztekin, A collaborative decision support system for multi-criteria automatic clustering, Decis. Support. Syst. 153 (2022) 113671, https://doi.org/10.1016/j.dss.2021.113671.

[60] M. Filippini, W. Greene, Persistent and transient productive inefficiency: a maximum simulated likelihood approach, J. Prod. Anal. 45 (2016) 187–196, https://doi.org/10.1007/s11123-015-0446-y.

[61] N.I.T.I. Aayog, Guiding Principles for the Uniform National-Level Regulation of Online Fantasy Sports Platforms in India: Draft for Discussion. https://www,niti gov.in/sites/default/files/2020-12/FantasySports\_DraftForComments.pdf, 2020.

[62] M.J. Farrell, The measurement of productive efficiency, J. R. Stat. Soc. Ser. A (Gen.) 120 (1957) 253, https://doi.org/10.2307/2343100.

[63] D. Aigner, C.A.K. Lovell, P. Schmidt, Formulation and estimation of stochastic frontier production function models, J. Econ, 6 (1977) 21–37. https://doi,org 10.1016/0304-4076(77)90052-5

[64] W. Meeusen, J.D. Broeck, Efficiency estimation from cobb-douglas production functions with composed error, Int. Econ. Rev. 18 (1977). https://www.jstor. org/stable/pdf/2525757.pdf

[65] P. Schmidt, R. Sickles, Production frontiers and panel data, J. Bus. Econ. Stat. 367–374 (1984).

[66] W. Greene, Reconsidering heterogeneity in panel data estimators of the stochastic frontier model, J. Econ. 126 (2005) 269–303, https://doi.org/10.1016/j. ieconom.2004.05.003

[67] M. Spence, Job market signaling, Q. J. Econ. 87 (1973), https://doi.org/10.2307 1882010.

[68] C. Massey. R.H. Thaler. The loser's curse: decision making and market efficiency in the national football league draft, Manag. Sci. 59 (2013) 1479–1495, https://doi org/10.1287/mnsc.1120.1657

[69] D. Unnikrishnan, S. Grover, S. Sringeswara, Fantasy Sports: A Game of Skill or Chance. https://hbsp,haryard.edu/product/IMB781-PDF-ENG. 2019.

[70] S.C. Kumbhakar, C.A.K. Lovell, Stochastic Frontier Analysis, 1st ed., Cambridge University Press, 2000 https://doi.org/10.1017/CBQ9781139174411.

[71] H.O. Fried, C.A.K. Lovell, S.S. Schmidt, The Measurement of Productive Efficiency and Productivity Change, Oxford University Press, 2008, https://doi.org/10.1093 acprof:oso/9780195183528.001.0001.

[72] R.J. Herrnstein, C.A. Murray, The Bell Curve: Intelligence and Class Structure in American Life. Free Press. 1994.

[73] J. Jondrow, C.A. Knox Lovell, I.S. Materov, P. Schmidt, On the estimation of technical inefficiency in the stochastic frontier production function model. J. Econ 19 (1982) 233–238, https://doi.org/10.1016/0304-4076(82)90004-5.

[74] Y. Ben-Porath, The production of human capital and the life cycle of earnings, J. Polit. Econ, 75 (1967) 352–365

[75] P.-A. Edin, M. Gustavsson, Time out of work and skill depreciation, ILR Rev. 61 (2008) 163–180.

Dr. Aishvarya is an Assistant Professor in the Information Management & Analytics area at the S.P. Jain Institute of Management & Research (SPJIMR), Mumbai. Her research interests are in the areas of data-driven decision-making, applied statistics, and business analytics, with a focus on sports and the retail sector. Her thesis focuses on addressing contemporary business and legal challenges in the online gaming sector using data-driven methodologies. She completed her Ph.D. in the Decision Sciences area at the Indian Institute of Management. Bangalore (IIMB). She was awarded the prestigious Intel India Research Fellowship for her dissertation work. Prior to joining IIMB as a PhD student, she earned her Bachelor’s and Master’s degrees in statistics and worked as a Data Scientist a IBM, where she received the IBM Eminence & Excellence Rising Star Award.

Dr. Tirthatanmoy Das is an Associate Professor and Chairperson of the Economics area at the Indian Institute of Management, Bangalore (IIMB). He is also a Research Fellow at the IZA Institute of Labor Economics and a Fellow at the Global Labor Organization (GLO).

Prior to joining IIM Bangalore, he was an Assistant Professor of Economics at the Uni versity of Central Florida, USA from 2014 – 2017, and at Temple University, USA from 2012 – 2014. His research spans topics in Econometrics, Behavioural Economics, Labour Economics and Health Economics. He has published in leading peer-reviewed journal such as the Journal of Econometrics and the Journal of Political Economy.

Dr. U Dinesh Kumar is a Professor in the Decision Sciences area at the Indian Institute of Management, Bangalore (IIMB). He is also the Chairperson of IIMB’s Data Centre and Analytics Lab (DCAL) and IIMB Chair of Excellence. He has published several research articles in reputed academic journals such as the European Journal of Operational Research, Annals of Operations Research, International Journal of Production Economics, Journal of the Operational Research Society, Computers and Operations Research, IEEE Transactions on Reliability, International Journal of Reliability, Quality and Safety Engi neering and more. He has published more than thirty case studies on Business Analytics and Machine Learning Algorithms based on Indian and multinational organizations such as Hewlett and Packard, Larsen & Toubro, Hindustan Aeronautics Limited, Indian Premier League, Flipkart.com, Apollo Hospitals, BigBasket, VMWare and more at the Harvard Business Publishing’s case portal. He has provided analytics consulting services to orga nizations such as Boston Consulting Group, GE Healthcare, General Motors, Hindustan Aeronautics Limited, Indian Army, TVS Motors, Wipro, and more. He was one of the winners of the Analytics India Magazine Data Science Faculty Awards 2021 in the ‘Distinguished Award’ category. He has authored a book titled, “Business Analytics – The Science of Data Driven Decision Making”, published by Wiley in 2017, and co-authored books titled “Machine Learning using Python” published by Wiley in 2019, “Machine Learning Using R”, “Data Visualization – Storytelling Using Data” published by Wiley in 2022, and “Reliability and Six Sigma” by Springer, USA in 2006.
