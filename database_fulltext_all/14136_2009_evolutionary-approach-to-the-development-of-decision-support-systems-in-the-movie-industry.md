---
otero_id: 14136
otero_key: "9JASZUP7"
title: "Evolutionary approach to the development of decision support systems in the movie industry"
authors: "Jehoshua Eliashberg; Sanjeev Swami; Charles B. Weinberg; Berend Wierenga"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.12.008"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Evolutionary approach to the development of decision support systems in the movie industry

Jehoshua Eliashberg <sup>a</sup>, Sanjeev Swami <sup>b,</sup>⁎, Charles B. Weinberg <sup>c</sup>, Berend Wierenga

<sup>a</sup> Wharton Business School, University of Pennsylvania, United States

<sup>b</sup> Department of Management, Faculty of Social Sciences, DEI, Agra, India

<sup>c</sup> Sauder School of Business, University of British Columbia, Canada

<sup>d</sup> Erasmus University, Rotterdam, The Netherlands

## a r t i c l e i n f o

Article history: Received 5 October 2007 Received in revised form 29 September 2008 Accepted 24 December 2008 Available online 9 January 2009

Keywords: Decision support systems Managerial decision making Motion picture industry models Scheduling

## a b s t r a c t

This paper reports the development and implementation of a decision support system in a non-traditional domain — the motion picture industry. The approach reported here is evolutionary, and the model was designed to assist exhibition executives in movie scheduling. After an earlier successful collaboration in scheduling a single theater with multiple screens, we now turn to the multi-theater multi screens situation, describing the problems encountered in that situation and how we have dealt with them. Using a quasiexperimental design, the decision support system was estimated to improve the net margin by over US \$ 900,000 on an annual basis. The paper describes the implementation process and the performance evaluation metrics that had been agreed upon with the management.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Over the years, decision support systems (DSS) have been applied and implemented in a variety of companies and organizations. The bulk of the work has concentrated in domains like the manufacturing and processing industry, supply chains, distribution, transportation, and <sup>fi</sup>nance. It is much more dif<sup>fi</sup>cult to <sup>fi</sup>nd applications of DSS in the so-called creative industries, such as leisure and entertainment. Nevertheless, we propose and demonstrate that even in these intuition-dominated domains, successful implementation of DSS is feasible. The work reported here combines elements of marketing and optimization (scheduling) in an unusual and challenging industry – motion picture – where management is not necessarily predisposed to accept analytical approaches.

Our strategy for implementing DSS in the movie industry was to follow an evolutionary approach. The implementation of decision support system in the motion picture industry concerns a situation of a structured problem (movie scheduling) which is quite amenable to optimization procedures. However, the implementation is in an organizational culture that is dominated by intuition rather than modeling and possibly not a positive a-priori attitude towards DSS. In such a situation, a well thought-out implementation strategy holds the key, where elements such as user involvement, top management support, and communication are important [26]. Resistance to change as a hurdle for the adoption of management support systems has been recognized in the DSS literature for a long time. In this context, the “unfreezing-moving-refreezing model” has often been recommended and used [22]. We believe that for the purpose of getting a DSS adopted in a new area with a potentially skeptical audience, as in the movie industry, it is better not to try to go through the unfreezing-movingrefreezing in one big jump. A step-by-step approach is more effective. It is delineated in this paper.

DSS should evolve over time in response to changing managerial levels of comfort and needs, increased data availability, and research advances [13,23,24]. Despite these dynamic aspects, there are relatively few published studies in the marketing of entertainment products reporting how models have actually evolved from both a technical and managerial standpoint (for exceptions, see [25,26]). We demonstrate this here with a model, SilverScreener [21], developed initially to assist managers of a Dutch movie exhibition chain, Pathé, to schedule movies in a single theater with multi screens. Having established a level of comfort with decision support systems and models, Pathé subsequently asked the modeling team to assist them in scheduling movies in multi theaters with multiple screens, within a single city, each week. We discuss in this paper our experience in addressing this new challenges, impacting decisions, policies, and practices. More speci<sup>fi</sup>cally, this paper reports how we modi<sup>fi</sup>ed the SilverScreener model for the multi-theater multiplex situation, how we made scheduling recommendations for a period of 26 weeks, and how we did all of this in close interaction with Pathé management. We present the results in terms of both how Pathé used the DSS' recommendations and the performance implications of the DSS implementation. We emphasize issues related to the interface of modelers and management. Therefore, we also pay attention to how the model was used in combination with the judgment of Pathé management, and how this particular multi-theater-multiplex scheduling application represents a speci<sup>fi</sup>c stage in the adoption process of DSSmethodology by this movie company.

![](/api/attachments/9JASZUP7/fulltext/images/745ab90ae9b131e3bef96f1f71815f2f45854d336c040c3bdafea496182b7ce3.jpg)  
Fig. 1. Evolutionary approach for DSS implementation in new settings.

The evolutionary approach followed in this paper builds upon previous research proposing a general framework integrating the elements that determine the success of a DSS [27]. Two critical elements of the framework in [27] are the demand side (characterized by the decision problem, the decision environment and the decision maker) — and the supply side (encompassing the functionality of the DSS and the decision support technology used) In the case of Pathé, we have here a very challenging demand side of the decision support system, with, on the one hand, a relatively structured problem (clear decision variables, predictable outcomes) and rich data, but on the other hand, a decision environment characterized by a heuristic decision style, and heavy reliance on intuition. The challenge is how to develop a DSS <sup>fi</sup>tting with this demand side, and to <sup>fi</sup>nd an effective implementation strategy so that the DSS is actually adopted and used. Elements of this strategy are: 1) evolutionary model development; 2) combining hard data and the intuition of the manager (e.g., in the classi<sup>fi</sup>cation of new movies; in the option to overrule the recommendation of the DSS); and 3) in providing a quantitative measure of the monetary value of performance improvement through the DSS. Our evolutionary approach can be summarized as shown in Fig. 1.

As shown in the <sup>fi</sup>gure, the evolutionary approach involved the following steps. We <sup>fi</sup>rst demonstrated that there exists a match (1) (room for improvement in decision-making) between the demand side and supply side of the DSS via ex-post analyses. This is based on demonstrating the effectiveness of our model on past data [21]. On the basis of these results, we established a relationship (2) with the organization through an internal champion. This champion is usually from the senior management. Gaining trust was relatively easy because of an earlier interaction when two members of the present SilverScreener team were involved in the successful launch of a DSS for the prediction of the number of visitors for new movies at one of the Pathé movie theaters in Holland [5]. In consultation with management, we agreed on meaningful metrics (3), and experimental setting to demonstrate our results in practice. We built the con<sup>fi</sup>dence of the management via implementation of our approach in simpler yet realistic settings, namely, in a single multi screens theater (4). We next proved the effectiveness of the approach in more complex situations, such as multiple theaters with multiple screens case (5). This is the topic of the present paper. The successful experience in this implementation will move us to the next level in complexity, namely, microscheduling (6) (i.e., within the theater scheduling movies showings for different hourly slots).

Related research on evolutionary development of DSS has appeared in contexts other than entertainment industry. [17] describes a multiyear effort, which resulted in the implementation of a series of human resource planning DSS applications in the U.S. Navy shipyard com munity. This paper concentrates on the development and implementation of a DSS in a large organization that is going through a personnel-downsizing process. [1] considers a customer-oriented catalog segmentation problem that addresses the crucial issue of the design of the actual contents of the catalogs. The DSS recommends alternative, satisfactory solutions to the decision maker. Using three algorithms, the DSS provides the decision maker with an easy-to-use, yet powerful tool to examine various catalog design options and their implications on the contents of the catalogs and the clusters of targeted customers. [2] models the constituents of a collaborative supply chain, the key parameters they in<sup>fl</sup>uence, and the appropriate performance measures in a decision support environment. Their paper shows how the constituents, key parameters and performance indicators are modeled jointly into the environment.

To illuminate the setting of the current project, Table 1 lists the Pathé movie theaters in Amsterdam with their seating capacities (for each screening room) and Table 2 provides, as an illustrative example, the actual weekly schedule of movies in one of Pathe's movie theaters, De Munt, for the <sup>fi</sup>rst eight calendar weeks of the year 2002. (See Table 3 for abbreviations and corresponding movie titles). The primary goal of the project described here was to provide, each week, recommendations for such movie schedules for each of the Pathé theaters in Amsterdam. This is called a macro-scheduling task. In the implementation section, presented later, we will provide movie theater speci<sup>fi</sup>c results from three major movie theaters in Amsterdam-Arena, City, and De Munt. These three major movie theaters together comprise 34 of Pathé's 41 screens in Amsterdam. In fact, this covers most of the movie supply in Amsterdam, because Pathé owns all the major movie theaters in Amsterdam (90% of box of<sup>fi</sup>ce sales).

Seating capacities of screening rooms at different Pathé movie theaters in Amsterdam.

<table><tr><td rowspan="2">Movie theater</td><td rowspan="2">Screen number</td><td colspan="14">Number of seats</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td></tr><tr><td>City</td><td></td><td>711</td><td>200</td><td>89</td><td>70</td><td>100</td><td>124</td><td>302</td><td>-*</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Bellevue</td><td></td><td>638</td><td>145</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Calypso</td><td></td><td>509</td><td>96</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Arena</td><td></td><td>161</td><td>183</td><td>205</td><td>282</td><td>205</td><td>148</td><td>118</td><td>149</td><td>183</td><td>205</td><td>282</td><td>205</td><td>322</td><td>602</td></tr><tr><td>Art House</td><td></td><td>135</td><td>105</td><td>135</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>De Munt</td><td></td><td>222</td><td>222</td><td>340</td><td>113</td><td>102</td><td>161</td><td>163</td><td>172</td><td>175</td><td>177</td><td>382</td><td>96</td><td>90</td><td>-</td></tr></table>

⁎The symbol ‘–’ denotes that a particular movie theater does not have that screening room. Thus, City is a 7-screen movie theater; Bellevue is a 2-screen movie theater, and so on.

Table 2  
Actual schedule of movies at De Munt theater, Amsterdam for weeks 1 to 8, 2002

<table><tr><td>Week\screen</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td></tr><tr><td>1</td><td>DSAW</td><td>OT, HPNL</td><td>HPOV</td><td>BDTS</td><td>SDT, LB, ANL</td><td>DOH, MN</td><td>ST, OT</td><td>SDT, ANL</td><td>LOTR1</td><td>PD</td><td>LOTR1, MN, BIBEV</td><td>ZL</td><td>AS</td></tr><tr><td>2</td><td>DSAW</td><td>HPOV</td><td>OE</td><td>BDTS, OT</td><td>LB, SDT</td><td>DOH</td><td>OT, MN</td><td>SDT, HPNL</td><td>LOTR1</td><td>ST, PD</td><td>LOTR1</td><td>ZL, MN</td><td>AS, ANL</td></tr><tr><td>3</td><td>BEL</td><td>HPOV</td><td>LOTR1</td><td>SDT</td><td>LB, ST, ANL</td><td>HPNL, OT</td><td>EW, MN</td><td>DSAW</td><td>LOTR1</td><td>JC</td><td>OE</td><td>DOH, PD</td><td>BDTS, MN, ZL</td></tr><tr><td>4</td><td>VS</td><td>HPOV</td><td>LOTR1</td><td>SDT, OE</td><td>ST, ZL, MN</td><td>HPNL, OT</td><td>DSAW, MN</td><td>BEL</td><td>LOTR1</td><td>JC</td><td>OE</td><td>DOH, PD</td><td>BDTS,TTO</td></tr><tr><td>5</td><td>VS</td><td>LAH</td><td>LOTR1</td><td>BEL</td><td>SDT, MN</td><td>HPOV</td><td>DSAW, HPNL</td><td>ENGM</td><td>LOTR1</td><td>JC, MECO</td><td>OE</td><td>ST, PD</td><td>OT, TTO</td></tr><tr><td>6</td><td>VS</td><td>LOTR1</td><td>SG</td><td>BEL, MN</td><td>SDT, LAH</td><td>HPOV</td><td>MIOV</td><td>ENGM, MECO</td><td>LOTR1</td><td>JC, MECO</td><td>OE</td><td>DSAW, PD, HPNL</td><td>OT, TTO</td></tr><tr><td>7</td><td>VS</td><td>LOTR1</td><td>SG</td><td>HPOV</td><td>BEL, JC, MN</td><td>GW</td><td>MIOV</td><td>ENGM, MECO</td><td>LOTR1</td><td>KL</td><td>OE</td><td>DSAW, PD, HPNL</td><td>OT, MECO</td></tr><tr><td>8</td><td>VS</td><td>LOTR1</td><td>SG</td><td>HPOV</td><td>MIOV</td><td>GW</td><td>MD, MECO</td><td>BMA</td><td>LOTR1, HPNL</td><td>KL</td><td>OE</td><td>DSAW, MN</td><td>OT, MECO</td></tr></table>

The movie macro-scheduling problem represents an area where DSS has a high potential in helping managers, but an unpredictable chance to succeed. While many of its managerial problems tend to be fairly structured, the decision environment is quite dynamic, contractual arrangements between parties are complex, and the cognitive style of the decision makers is often non-analytical or heuristic [27]. These characteristics represent challenges in developing implementable models for decision makers in this industry. Despite the above-noted challenges, a stream of research that addresses these and related issues in the area of movies is emerging. Forecasting, for example, has received an increasing amount of attention. Work has been reported on forecasting the enjoyment of movies at the individual level [6] and on predicting commercial success of movies at the aggregate level [5,8,16,20,21]. Other topics that have received research and modeling attention include release timing of movies and videos [10,14,10], assessing the impact of advertising on box-of<sup>fi</sup>ce performance of new <sup>fi</sup>lms [28], and designing contracts in the <sup>fi</sup>lm's supply chain [18]. However, the above mentioned research has taken an ‘one-shot’ type approach and no study to date has focused on developing and implementing decision support models and systems over time, working closely with managers in the movie exhibition industry and assisting them in their decision-making. This paper reports the implementation efforts aimed at ful<sup>fi</sup>lling this gap.

List of movies used in the actual schedule at De Munt Theater, Amsterdam for weeks 1 to 8,2002.

<table><tr><td>Movie number</td><td>Movie name</td><td>Abbreviation</td></tr><tr><td>1</td><td>Don&#x27;t Say A Word</td><td>DSAW</td></tr><tr><td>2</td><td>Behind Enemy Lines</td><td>BEL</td></tr><tr><td>3</td><td>Vanilla Sky</td><td>VS</td></tr><tr><td>4</td><td>Others, The</td><td>OT</td></tr><tr><td>5</td><td>Harry Potter (Dutch)</td><td>HPNL</td></tr><tr><td>6</td><td>Harry Potter</td><td>HPOV</td></tr><tr><td>7</td><td>Life As A House</td><td>LAH</td></tr><tr><td>8</td><td>Lord Of The Rings-1</td><td>LOTR1</td></tr><tr><td>9</td><td>Ocean&#x27;s Eleven</td><td>OE</td></tr><tr><td>10</td><td>Spy Game</td><td>SG</td></tr><tr><td>11</td><td>Bandits</td><td>BDTS</td></tr><tr><td>12</td><td>Serendipity</td><td>SDT</td></tr><tr><td>13</td><td>Minoes</td><td>MN</td></tr><tr><td>14</td><td>Legally Blonde</td><td>LB</td></tr><tr><td>15</td><td>Atlantis NL</td><td>ANL</td></tr><tr><td>16</td><td>Score, The</td><td>ST</td></tr><tr><td>17</td><td>Zoolander</td><td>ZL</td></tr><tr><td>18</td><td>Jeepers Creepers</td><td>JC</td></tr><tr><td>19</td><td>Monsters Inc OV</td><td>MIOV</td></tr><tr><td>20</td><td>Discovery Of Heaven</td><td>DOH</td></tr><tr><td>21</td><td>Ghost World</td><td>GW</td></tr><tr><td>22</td><td>Evil Woman</td><td>EW</td></tr><tr><td>23</td><td>Mulholland Drive</td><td>MD</td></tr><tr><td>24</td><td>Enigma</td><td>ENGM</td></tr><tr><td>25</td><td>Monsters En Co</td><td>MECO</td></tr><tr><td>26</td><td>Beautiful Mind, A</td><td>BMA</td></tr><tr><td>27</td><td>Princess Diaries</td><td>PD</td></tr><tr><td>28</td><td>Kate &amp; Leopold</td><td>KL</td></tr><tr><td>29</td><td>Blub, Ik Ben Een Vis</td><td>BIBEV</td></tr><tr><td>30</td><td>America&#x27;s Sweetheart</td><td>AS</td></tr><tr><td>31</td><td>Tom &amp; Thomas</td><td>TTO</td></tr></table>

The remainder of the paper proceeds in the following manner. Section 2 presents a more detailed description of the problem. Section 3 presents the development of the multi screens macroscheduling algorithm used. Section 4 describes our forecasting process for weekly attendance and our analysis of the accuracy of the system. Section 5 provides an evaluation of the success of the implementation, and the last section (Section 6) deals with the lessons learned for the implementation of DSS in “non-traditional” domains.

## 2. Problem description

Every week, movie distributors typically have 3 to 5 new movies available for release into the market and movie exhibitors need to decide which, if any, of those movies to show in their movie theaters, and which old movies to stop showing if necessary. While exhibitors at times make commitments months in advance to show a speci<sup>fi</sup>c movie, typically for blockbusters such as, Lord of the Rings, most exhibitors have a management meeting every Monday morning to review the past weekend's box of<sup>fi</sup>ce results and make decisions about which movies to drop and which to add. An important part of this adaptive process is forecasting revenues for each of the movies. As typical data show (see Fig. 2), many movies decline in appeal over time, but the movie theater retains an increasing portion of box of<sup>fi</sup>ce receipts (and all concession revenues) the longer the movie is playing. Movie theater screens space is particularly scarce in the peak seasons — more movies are available than screen capacity is available.

At Pathé Holland, a three-person management committee meets every Monday morning to schedule movies to speci<sup>fi</sup>c screens in all Pathé movie theaters throughout the country. The committee's information set includes box of<sup>fi</sup>ce data on all currently showing movies through the last weekend, a list of new movies and number of copies (prints) available to Pathé, a list of movies that were precommitted to each screen, and contract terms for each movie. With eleven Pathé movie theaters in Holland (six in Amsterdam), with up to <sup>fi</sup>fteen screens per movie theater, and over forty candidate movies per week (many with multiple copies available), it can readily be seen that assigning movies to screens is a challenging combinatorial problem.

![](/api/attachments/9JASZUP7/fulltext/images/16b10b4e4446a68810362ba79c9311eff07d3abc224a9fa2ad88a73489743965.jpg)

Movie A.I. in Year 2001 in Theater De Munt  
![](/api/attachments/9JASZUP7/fulltext/images/733254253e0e4cd97c3c1f7e1d172b5448422ba770ac20ac91dd83edd23720d5.jpg)  
Fig. 2. Representative revenue decay patterns of two movies in year 2001.

This complex assignment poses a number of challenges. The <sup>fi</sup>rst concerns the heterogeneity among theaters. There are different numbers of screens in the different theaters, different screening room capacities, different consumer preferences and demand situations (translating into different prognoses for box of<sup>fi</sup>ce sales for the same movie in different theaters, and different consideration sets (sets of possible movies to be shown). A second challenge concerns the special treatment required for certain movies. For example, several pre-commitments have to be taken into account (e.g., contractual agreements with distributors to show a particular movie in a particular screening room of a particular theater during a speci<sup>fi</sup>ed number of weeks). Also, special treatment is required for kid's movies and matinee movies.

Forecasting the box-of<sup>fi</sup>ce is a particularly challenging problem. One issue is the generation of forecasts for newly released movies, for which no historical box of<sup>fi</sup>ce data are available. In an earlier onetheater with 6 screens implementation case [7], we simply asked management to make judgmentally numerical predictions, based on their experience, or to provide a “matching (comparative) movie,” a movie that is similar to the new one, and for which historical data are available. For this large number of theaters and screens, this method is not feasible. Moreover, we found management to be quite uncomfortable in making predictions, because these could possibly be held against the managers if sales were lower than predicted. Still, because of their extensive experience, the Pathé managers are in the best position to judge the potential of a new movie. Therefore, we devised a movie classi<sup>fi</sup>cation scheme, which utilizes and integrates managerial judgments with hard data, alleviating the demanding task of managers having to make speci<sup>fi</sup>c numerical forecasts for individual movies (described in more detail in Section 4.3).

Before we describe the implementation process that was ultimately adopted, we want to elaborate on our modeling philosophy in the movie domain. We think that there are two conditions for successful DSS in environments such as the entertainment world. First, we have to demonstrate with hard <sup>fi</sup>gures that the DSS generate better outcomes. For that reason we carried out a quasi experiment (with and without the use of the DSS). Second, we should realize that in an environment like the movie industry, intuition remains important. We think that a good deal of progress can be made by making better use of the numbers (which abound in the movie industry) and the application of optimization procedures, but at the same time we do not advocate the elimination of intuition altogether. Domain experts have intuitive knowledge, which often is not included in models, and they are able to recognize cases, distinctive in<sup>fl</sup>uence factors, and rare events that are dif<sup>fi</sup>cult to anticipate and to include in models [11,15]. Political conditions or other events (e.g. wars, terrorist attacks, tsunamis) may suddenly change the movie interests of moviegoers. Ethnic tensions may make it risky to show particular movies (as actually happened in Amsterdam). In that case, managerial judgment may prevent a particular movie from being screened, even if the predicted numbers would recommend otherwise. Another example of managerial judgment is the decision to acquire two copies of a particular movie for a particular theater (double booking). Managers do this if they feel that there will be extraordinary interest in the <sup>fi</sup>lm. For these reasons, we embedded the use of our scheduling algorithm within the managerial decision-making context and style of

![](/api/attachments/9JASZUP7/fulltext/images/46842cb1d3921a9199a0304320aea32638b6e414ea384c00139ca462387878d7.jpg)  
Fig. 3. Conceptual view of multi-theater screen scheduling implementation.

Pathé. We think that in the movie industry, combining models with intuition is the best recipe for improving decisions [3].

## 3. Development of the scheduling algorithm

We begin the exposition with the formulation of the basic theater programming problem, which was solved every week for the six movie theaters considered in this study. The scheduling algorithm, an integer programming problem which optimizes each theater's net margin over a (rolling) planning horizon of W weeks, is built on a core theater programming model (see Appendix A for a detailed description). System-wide constraints imposed because of the multiple theaters operated by Pathé have been handled through an algorithm described in Appendix B. (Note: we carried out an analysis to determine if there is signi<sup>fi</sup>cant competition among the Pathe theaters in Amsterdam. In agreement with [4], we found that, from a demand standpoint, each theater primarily draws its own audience and that there is little internal competition amongst theaters.).

A separate consideration set of movies was constructed for each movie theater, in consultation with the manager, to deal with the limited number of prints across movie theaters by omitting some potentially scarce movies from the overall consideration set for speci<sup>fi</sup>c movie theaters. The weekly scheduling problem was solved by an adaptive scheduling (or rolling horizon) approach. A conceptual view of our implementation plan, as explained above, is shown in Fig. 3.

As shown in the <sup>fi</sup>gure, some additional managerial requirements stipulated that certain screen-time slots may be <sup>fi</sup>xed as precommitments, and that provisions must be made to accommodate special movies such as kids' movies and matinee movies. The resulting multi-theater screen-scheduling algorithm is used in the implementation. The various steps of the multiple theaters multiple screens implementation are presented as a <sup>fl</sup>ow chart in Fig. 4. The entire algorithm is coded in AMPL [9], a modeling language for mathematical programming.

We now explain in detail the extensions and procedural enhancements to the core theater programming model.

## 3.1. Pre-commitments

Under the contract terms of certain movies, Pathé management is committed to play these movies for a speci<sup>fi</sup>ed number of weeks on a speci<sup>fi</sup>c screen in a speci<sup>fi</sup>c movie theater (mostly for new movies). For such movies the obligation period variable (OPD) was <sup>fi</sup>xed for the weeks (mostly one or two weeks) for which a commitment was made.

![](/api/attachments/9JASZUP7/fulltext/images/6643183c5e87ef962758447985d964f419459698920c1f4726f46638ef6e1a04.jpg)  
Fig. 4. Flow chart of multi-theater screen scheduling implementation approach.

Once this commitment was ful<sup>fi</sup>lled, these commitment restrictions were relaxed and such movies were treated as normal movies.

## 3.2. Double-booking

Occasionally, Pathé management considered the possibility of showing a particular movie on more than one screen in the same movie theater. This is usually done to accommodate the expected demand beyond the capacity of a single screen. Since weekend days (Friday, Saturday, and Sunday) are usually the days of high demand in a week, our approach focuses on the weekend periods. To examine the possibility of double bookings of a movie at a movie theater, we <sup>fi</sup>rst determine the capacity of any given screen of a movie theater in terms of maximum number of tickets it can potentially sell over the weekend. Thus,

$$
\mathrm{WCAP} _ {s} = \text { NSEAT } _ {s} * \text { SHOW } * \text { WDAYS }\tag{1}
$$

where,

$$
\begin{array}{l l} \text {WCAP} _ {s} & \text {weekend capacity of screen s}, \\ \text {NSEAT} _ {s} & \text {number of seats in screen s}, \\ \text {SHOW} & \text {average number of shows in a day, and} \\ \text {WDAYS} & \text {weekend days per week (3)} \end{array}
$$

Beginning with the largest capacity screen, we could then compare WCAP with ${ \mathrm { W D E M A N D } } _ { j w } ,$ the prediction of the demand of a movie j on the weekend of week w. In the current implementation, managerial judgment indicated that, on an average, ${ \mathrm { W D E M A N D } } _ { j w }$ is a fraction z of the weekly demand (note: managerial estimates at the time of the study indicated that z should be 0.75). Thus, $\mathsf { W D E M A N D } _ { j w } =$ $z ^ { * } \mathrm { D E M A N D } _ { j w } ,$ where $\mathsf { D E M A N D } _ { j w }$ is the predicted weekly demand (discussed in Section 4.1) for movie j for week w. $\mathrm { I f } \ \mathsf { W D E M A N D } _ { j w } { > }$ $\mathsf { W C A P } _ { s } ,$ then movie j is considered as a candidate for double booking in week w by the algorithm. The spillover demand $( \mathsf { W D E M A N D } _ { j w } -$ $\mathsf { W C A P } _ { s } )$ is demand for the recommended “extra” movie for double booking.

## 3.3. Screen allotment

The different screens at various movie theaters operated by Pathé have different seating capacities (see Table 1). SilverScreener's algorithm provides initially, as the output, a set of movies to be played that week. We then use the following heuristic for screen allotment: In each week, allocate the movie with highest weekly predicted demand to the highest capacity screen, the movie with the next highest predicted weekly demand to the next highest capacity screen, and so on. This heuristic rule appears to be effective. Given the opportunity to double book very popular movies, our analysis of the attendance data for the implementation period of our DSS indicated that sellouts rarely occur.

## 3.4. Kids' movies

In some speci<sup>fi</sup>c scheduling instances, Pathé management wanted the children and family type movies to be played alongside some other mainstream movies. This meant that, on a particular day of the week and a speci<sup>fi</sup>ed screen, for approximately half of the showings a mainstream movie would be playing on that screen, and for the other half, a children's movie would be playing. To incorporate this in the algorithm, and in order to generate a feasible solution of the SilverScreener's algorithm, we arti<sup>fi</sup>cially “added” as many screens as there were such movies to be scheduled in that movie theater. While sorting the predicted revenues for screen allotment, the better children's movies, as selected by SilverScreener algorithm, are allocated to the arti<sup>fi</sup>cial screens. Eventually, the arti<sup>fi</sup>cial screens are discarded from the system, and a selected children movie is “clubbed” with that mainstream movie whose revenue stream appears similar to that of the children's movie (note: since the extra children's movies had lower attendance than the average movie in the main set, children's movies were usually matched with lower grossing mainstream movies. In matching revenues, management used as a judgment tool, that daytime showings of a mainstream movie would provide half the revenue that was forecasted for that movie. Children's movies would only be shown in the daytime, so their total revenue was used in the matching process.). The two combined movies are recommended by SilverScreener to be played together, as explained earlier, on the screen allotted to the mainstream movie.

## 3.5. Matinee movies

Pathé management also required that for every movie theater, some matinee movies should be accommodated. These are usually the movies that were not recommended by SilverScreener, but, in management judgment, might still be good candidates to be played during matinee hours, in addition to the recommended movie. Past managerial practice suggested that every week there would be a maximum of three such movies. A practical approach was developed to ful<sup>fi</sup>ll this managerial requirement. In the historical database, it was observed that major movies usually started as mainstream weekly movies in the schedule and became matinee movies later on in their run. The standard application of SilverScreener generates the “best” S weekly movies for a single movie theater with S screens. To accommodate matinee movies, the problem was formulated to solve an “expanded problem” to recommend (S 3) movies for an S-screen movie theater. After sorting for screen allotment, the <sup>fi</sup>rst S movies were recommended as mainstream weekly movies and the last 3 were recommended as matinee movies for that week.

## 4. Forecasting weekly attendance

## 4.1. The demand model and seasonality

To forecast weekly attendance for a movie at the individual movie theater level, we used an exponential decay model. Previous researchers have shown that, to a <sup>fi</sup>rst degree of approximation, most mass-market movies follow an exponentially decaying pattern once it has been widely released [12]. For a given movie, the exponential model, stated in logarithmic form, is the following:

$$
\begin{array}{l} L n (A t t e n d a n c e _ {w}) = \alpha - \beta w, \text { where } w = 0, 1, 2,... \\ \text { is   the   week   since   the   movie   was   first   shown. } \end{array}\tag{2}
$$

The values of the two parameters α and β vary, of course, by movie. They may also vary by movie theaters. In addition, there could be other effects on demand such as holidays and seasonal factors. In the earlier (single-theater) implementation [7], certain weeks were identi<sup>fi</sup>ed as holiday weeks for which demand estimates need to incorporate the increased effect of leisure time. The holiday's weeks relevant to the current study are: week 8 (Spring vacation), week 42, week 43 (Autumn holiday) and week 52 (Christmas holiday). Based on the single theater results [7], the following seasonal factors (in<sup>fl</sup>ators) were used for demand estimation to account for the holiday effects: weeks 8, 42 and 43: 1.47 and week 52: 2.37. Before using the actual data for these weeks in demand estimation, the demand data were deseasonalized, dividing the demand for these weeks by their respective seasonal factors. The forecasting procedure then used the deseasonalized demand data for estimating the two-parameter exponential decay model. Subsequently, the projected demand on the basis of the estimated model was multiplied by the seasonal factors for the above weeks with their respective seasonal factors.

Eq. (2) was estimated using ordinary least squares (OLS) for each movie in each theater and was updated weekly, as new data became available. We chose this simple yet robust method because each movie had a limited number of data points available, the need to produce many forecasts each week, and the pressure to prepare these forecasts in a short period of time Although these forecasts, as discussed below, proved to be quite accurate, as newer forecasting technologies that meet the timeliness requirement become available, such as Bayesian methods [19], their possible usefulness in applied settings such as ours may be established.

## 4.2. The initial forecasting process

Given that a movie's attendance varies by movie theaters and that weekly results are readily available, our approach was to use, to the extent possible, the actual attendance data for forecasting. However, the two-parameter exponential decay model could only be <sup>fi</sup>t to the data for movies that had been running for at least two weeks. In order to address cases in which a movie has not been released or has played for only one week, we asked management to provide an estimate of attendance for each of the <sup>fi</sup>rst three weeks of the movie's run. This is in line with other studies advocating the intimate engagement of management in DSS practice [15]. Once the movie had run for two weeks, we had access to two weeks of its actual performance data, which could then be used for demand forecasting. Thus, our overall approach towards demand forecasting involved the following three phases: (i) before opening — use manager's judgments for each of the <sup>fi</sup>rst three weeks data and <sup>fi</sup>t an exponential curve to these data, (ii) after the <sup>fi</sup>rst week — use actual attendance to estimate parameter α, and use manager's judgments for weeks 2 and 3 to <sup>fi</sup>t an exponential curve to these data, and (iii) second week onwards — <sup>fi</sup>t an exponential curve to as many weeks of actual data as possible.

Occasionally, a movie became available at the last minute and the manager did not have suf<sup>fi</sup>cient time to provide an estimate. In such cases, we used the movie's genre (e.g., comedy, action) and its MPAA rating (e.g., PG, R) to generate forecasts based on the average performance of movies previously played in that movie theater with those characteristics.

While a reasonable forecasting procedure, this demand system with its high reliance on detailed managerial inputs for new movies faced many challenges. Major movies were often pre-committed to speci<sup>fi</sup>c screens and at several occasions, explicit forecasts were not seen as necessary. Managers found that far too many explicit forecasts were required and felt it was too demanding to provide them. Moreover, they may have been reluctant to provide explicit forecasts, which could be used as an evaluation tool of their forecasting pro<sup>fi</sup>ciency. Also, because of the scale of the operation, with a number of different theaters, and a much larger number of screens, it became practically impossible to collect detailed prediction data for all new movies, every week. We therefore had to modify the initial forecasting process.

## 4.3. The revised process of forecasting weekly attendance: movie classification scheme

Based on the considerations described above, we developed a new procedure where management only had to classify each movie in one of sixteen categories according to the expected opening strength and decay rate of the movie. The primary motivation for the revised scheme of forecasting attendance was to expedite the process and avoid having the manager provide exact three-week data points for every movie in every possible movie theater, but instead, to have them simply provide an overall ordinal (rather than a cardinal <sup>fi</sup>gure) “code” for a movie. Towards this end, the researchers in consultation with the manager developed a movie classi<sup>fi</sup>cation scheme. It was based on the two parameters of the demand curve, which are often employed in the movie business terminology: opening (referred to as the SIZE parameter in the industry) and decay rate (LEGS) (Note: in the movie industry, a movie that keeps drawing many visitors, even a long time after the opening week is said to have long legs. This corresponds to a low decay factor or a large β.). It was decided to have four categories of size (from highest to lowest): A, B, C and D; and four categories of legs 1, 2, 3, 4. Together, these values de<sup>fi</sup>ne 16 types of movies: A1, A2, …. B1, ….., D1, …. D4. The ultimate objective of this scheme was to have the size of a movie as a surrogate for the parameter α, and the legs category as a surrogate for β (refer to Eq. (2)). With this procedure, the manager does not need to forecast the number of visitors for new movies for each movie theater, but only has to indicate to which category a new movie belongs.

To operationalize and calibrate the classi<sup>fi</sup>cation scheme, the manager was sent a list of 108 movies that had played in the three major Amsterdam movie theaters before Week 32 of year 2001. To classify movies into various size sub-classes, the manager indicated that the researchers make use of the frequency distribution of the <sup>fi</sup>rst week (opening) revenues of the movies. The following procedure was followed as per the suggestion of the manager. The range of opening revenues (ranging from € 622 to € 178423) was divided into four quartiles. The movies in the fourth quartile (i.e., top 25%) were assigned category A. Those in the third quartile (i.e., 50–75%) were assigned category B and so on. To classify movies into various legs subclasses, a ratio was de<sup>fi</sup>ned by the manager as FFWR/LTR, where FFWR=<sup>fi</sup>rst <sup>fi</sup>ve week revenue of a movie, LTR=Lifetime revenue of a movie. The calculation of this ratio was performed for each of the 108 movies by the researchers. The manager then speci<sup>fi</sup>ed the following rule for the classi<sup>fi</sup>cation: if the ratio for a movie was less than or equal to 0.7, it was assigned legs category 1 (speci<sup>fi</sup>ed as “long legs”), if the ratio was between 0.7–0.8, it was assigned category 2 (“middle legs”), between 0.8–0.9 category 3 (“limited legs”) and between 0.9–1.0 category 4 (“short legs”). Out of these 108 classi<sup>fi</sup>ed movies, the movies of a particular type that had played in a particular movie theater were then separated out by the research team.

With 16 movie sub-classes and 108 movies, there is clearly insuf<sup>fi</sup>cient data to use the average value for each cell as an estimate. For a number of theaters, there are no observations in some cells. In order to overcome these limitations, the following dummy variable regression model was used.

$$
\begin{array}{r l} & L n \left(\mathrm{Rev} _ {j w t}\right) = a + b w + d _ {1} D _ {t 1} + d _ {2} D _ {t 2} + d _ {3} D _ {t 3} + a _ {1} A _ {s b} \\ & \qquad + a _ {2} A _ {s c} + a _ {3} A _ {s d} + b _ {1} B _ {l 2} w + b _ {2} B _ {l 3} w \\ & \qquad + b _ {3} B _ {l 4} w + \text {error} \end{array}\tag{3}
$$

where

${ \sf R e v } _ { j w t }$ box-of<sup>fi</sup>ce revenue of movie $" j "$ in week $" w "$ in movie theater t,

$D _ { t 1 , } \ D _ { t 2 , } \ D _ { t 3 }$ movie theater-speci<sup>fi</sup>c dummy variable (Base case — ARENA, Theater represented by $D _ { t 1 }$ is Bellevue/Calypso, $D _ { t 2 }$ is City, and $D _ { t 2 }$ is De Munt),

$A _ { s b , } A _ { s c , } A _ { s d }$ size class dummy variable (Base case — Class A),

where $A _ { s b }$ represents size Class B, etc.

$B _ { l 2 } , B _ { l 3 } , B _ { l 4 }$ legs class dummy variable (Base case — Class 1),

where $B _ { l 2 }$ denotes legs class 2, etc.

Notice that this regression is performed by pooling the observations over all the weeks that the 108 movies played in each movie theater. The analysis was run for four of the Pathé movie theaters in Amsterdam, with 1654 observations in total.<sup>1</sup> After obtaining the estimates for the respective coef<sup>fi</sup>cients $( a , b , d _ { 1 } , d _ { 2 } , d _ { 3 } , a _ { 1 } , a _ { 2 } , a _ { 3 } , b _ { 1 } ,$ $b _ { 2 } , \ b _ { 3 } )$ , the α and $\beta$ parameters for various movie types could be estimated by dummy variable coef<sup>fi</sup>cients. For example, the coef<sup>fi</sup>- cients for a B2 movie in the ARENA movie theater in week 1 would be $( a + a _ { 1 } , b + b _ { 1 } )$ . The regression results obtained were as follows.

Table 4  
Value of R<sup>2</sup> (actual vs. forecast) by movie theaters.

<table><tr><td>Week\theater</td><td>De Munt</td><td>City</td><td>Arena</td></tr><tr><td>Week 1</td><td>0.32(n=22)</td><td>0.71(n=16)</td><td>0.69(n=28)</td></tr><tr><td>Week 2</td><td>0.32(n=18)</td><td>0.77(n=12)</td><td>0.78(n=21)</td></tr><tr><td>Weeks 3</td><td>0.52(n=132)</td><td>0.82(n=41)</td><td>0.79(n=119)</td></tr></table>

$$
\begin{array}{c} L n \left(\mathrm{Rev} _ {j w t}\right) = 1 0. 1 2 - 0. 1 2 w + 0. 4 7 D _ {t 1} + 0. 2 2 D _ {t 2} + 0. 6 4 D _ {t 3} \\ - 0. 6 6 A _ {s b} - 1. 1 9 A _ {s c} - 1. 1 1 A _ {s d} \\ - (2 5 0. 2 6) (- 2 6. 3 8) (7. 6 3) (5. 0 2) (1 7. 6 9) (- 1 6. 3 0) \\ \times (- 2 2. 3 3) (- 1 5. 0 2)   0. 0 3 B _ {l 2} w - 0. 0 7 B _ {l 3} w \\ -   0. 0 8 B _ {l 4} w + \text { error } \\ \times (- 4. 0 2) (- 8. 5) (- 9. 3 1) \\ \Big (t \text {-statistics are in parentheses,} R ^ {2} = 0. 5 1, n = 1 6 5 4 \Big), \\ F (1 0, 1 6 4 3) = 1 7 1. 1 7 (p <   0. 0 1) \end{array}\tag{4}
$$

Based on the above results, in which all the coef<sup>fi</sup>cients turned out to be signi<sup>fi</sup>cant, we generated α and $\beta$ values for the 16 movies categories in the four movie theaters as discussed above (note: Eq. (4) explicitly allows for a movie theater speci<sup>fi</sup>c effect on SIZE, but not for LEGS. A regression allowing for a movie theater speci<sup>fi</sup>c effect on LEGS turned out to not signi<sup>fi</sup>cantly improve the regressions results.). The magnitude of various coef<sup>fi</sup>cients was found to be appropriate according to the ordering of the various categories (A, B, C, D and 1, 2, 3, 4). The respective revenue streams were then generated and sent to the manager for checking their face validity. These revenue streams were found reasonable by the manager and were therefore used for the rest of the implementation period. From then on, for each new movie, the managers had only to indicate the SIZE and the LEG category of a new movie.

To assess the accuracy of the above forecasting scheme, the forecast of revenue generated for each week in each movie theater was regressed on the corresponding actual value for a new set of data. The results of these regressions in terms of $R ^ { 2 }$ are reported in Table 4 for the three major movie theaters, Arena, City and Munt.

As shown in the table, the results are reported for three types of observational periods: (i) Week 1 (ii) Week 2 and (iii) all the observations consolidated from Week 3 onwards. Overall, the $R ^ { 2 }$ results in Table 4 show that the predictions are quite accurate. The somewhat weaker results for the Munt can be explained by the fact that the Munt is a new movie theater, which opened one year prior to the implementation of the decision support system. Hence, the current database for this movie theater has not yet reached a steady-state condition. As new data come in, the forecasting accuracy is likely to improve. Overall, the forecasting method of predicting the numbers of visitors for new movies met the needs of Pathe's management.

## 5. Evaluation of the SilverScreener DSS' performance

The performance evaluation of the DSS is an extremely important issue. Clear and operational measures have to be established before the implementation begins. It was decided jointly by Pathé's management and the modeling team that the evaluation of this application of the SilverScreener system would be based on output metrics, such as attendance and net margin, as well as on behavioral measures, such as, the extent to which managers followed the DSS recommendations, and the extent to which they want us to assist them in extensions of this effort. The latter point is particularly critical in the evolutionary development of DSS, that is, to what extent is the management interested in continuing system development, enhancements, and implementation.

## 5.1. Net margin impact

With management's input, a quasi-experimental design was implemented to evaluate the impact of using SilverScreener. It is important to note that we agreed with management on the metric needed to evaluate the DSS before we started its implementation. Although the same management committee made scheduling decisions for all movie theaters in Holland, speci<sup>fi</sup>c SilverScreener recommendations were made available only for the screens in Amsterdam. Two other large cities in the same “Randstad region” of Holland, Rotterdam and The Hague as well as a base period, January–August 2001 were chosen as benchmarks. Attendance and net margin<sup>2</sup> results were measured for approximately six months (September 2001–February 2002) at all Pathé movie theaters in each of these cities. In addition to the relative improvement of € 277,959 in net margin from admissions, as shown in Table $5 ,$ Pathé earned an additional € 64,112 in net concession revenues (estimated by management for this purpose at a rate of € 1 per visitor) for a total improvement in the SilverScreener supported theaters of € 342,000. This is a 4.8% improvement in net margin due to SilverScreener's effect on Pathé's theaters over approximately six month implementation period. After adjustments for seasonality, these results were projected to an annual relative improvement in overall net margin of approximately € 710,000, or over \$900,000.

## 5.2. Did management always follow our advice? Matching between actual and recommended schedules

It is interesting to note that the increase in the net margins occurred despite the fact that the management committee did not consistently follow the SilverScreener's recommendations. Management could differ from the model's recommendation by choosing the same movie but showing it in different theater, different screen, different week, or by not showing it at all. Hence, there are different degrees to which management could adopt the model recommendations. (An example for a partial adoption would be playing the recommended movie in the same theater, on the recommended week, but on a different screen). To examine the extent to which management fully adopted the model recommendations, we employ the metric of weighted capacity match for the period of Week 45, 2001 to Week 9, 2002, considering the <sup>fi</sup>rst 4 weeks as an initializing subperiod.

The following example illustrates how the weighted capacity match metric was operationalized. Consider a hypothetical 2-screen movie theater with screen capacities as 1000 and 500 seats, respectively. Suppose, in a given week, the SilverScreener recommended movie and the actual movie played were the same for the <sup>fi</sup>rst screen, but not for the second. Then, the weighted screen capacity match, in percentage terms, would be=1000/(1000 500) or 66.7%.

Thus; Weighted Screen Capacity Match

5

Sum of Capacity of Screens with Match 4100 Total Screen Capacity of the Theater

Table 5  
Analysis of the impact of using SilverScreener for Pathé-Amsterdam.

<table><tr><td>Period</td><td>Rotterdam + The Hague</td><td></td><td>Amsterdam</td></tr><tr><td>Jan 20/01-Aug 20/01 (base period)</td><td>€ 6,010,007(a)</td><td></td><td>€ 5,982,099(b)</td></tr><tr><td rowspan="4">Sept 20/01-Feb 20/02 (implementation period)</td><td rowspan="4">€ 5,787,333(c)</td><td>Projected (w/o SilverScreener)</td><td>€ 5,760,459(**)</td></tr><tr><td>Actual</td><td>€ 6,038,419</td></tr><tr><td>Difference</td><td>€ 277,959</td></tr><tr><td>Percentage improvement relative to performance without SilverScreener</td><td>4.8%</td></tr></table>

Numbers in the table represent net margin (⁎) for Pathé from admissions.  
(⁎) Concession sales not included (⁎⁎) calculated as: $( b / a ) ^ { * } { \mathsf { c } } .$

Based on the above analysis, the weighted screen capacity match <sup>fi</sup>gures for a continuous portion (Week 45, 2001 to Week 9, 2002) of the implementation period, broken into four time intervals, were calculated as shown in Table 6. The higher the number, the more closely management followed the system's recommendations.

As can be seen, the average match percentages are in the range of 58% to 60% across weeks, and in the range of 52% to 63% across movie theaters. The results in Table 6 suggest that Pathé management actual decisions were compatible, to a large extent, with the recommendations from SilverScreener. Note that this is a very stringent test, as even small changes, such as showing a recommended movie in a 177 instead of a 172-seat room would be counted as “not matching.” At “steady state,” the weighted screen capacity index is about 60% of the cases. Apparently, judgmental considerations, outside the model, are responsible for the 40% mismatching. Managers always have more information and other concerns that are not re<sup>fl</sup>ected in the model. One reason for the observed discrepancy between the model scheduling recommendation and the actual schedule is the distributor's pressure that exhibitors in the motion picture industry have to live with. This implicit threat “if you do not free up a screen for my new movies, I will keep it in mind when our new blockbuster is released” is an inherent part of the relationship management between the two supply-chain parties in this industry. Other reasons for not following SilverScreener's recommendations include unexpected events in the city, the country or the world, sudden changes in the numbers of visitors which are not yet re<sup>fl</sup>ected in the forecasts used by the model, and participation in movie festivals. It is interesting to observe that a substantial increase in net margin was obtained (about \$900,000 on an annual basis) with the observed “60% model–40% judgment” combination.<sup>3</sup> This is similar to the results reported by [3], which show that a 50–50 combination of the model and the expert is close to optimal.

We also investigated whether the weighted match percentage in a theater was related to the net margin of that theater for that week. We tested this effect with a regression analysis that controlled for the different theaters and for the week, as some weeks have movies which are much more attractive than others, as shown in [7]. We found no signi<sup>fi</sup>cant relationship between capacity match and net margin. We believe these results are not surprising for several reasons. First, as discussed above, management has certain information not explicitly included in the DSS and we expect management to utilize that information effectively. The DSS reduces the complexity of the problem, thus allowing management to focus on critical and unusual information. In addition, the range of variation in screen capacity match was rather small, so it would be dif<sup>fi</sup>cult for any effects to emerge given the overall variability in movie demand.

## 6. Decision support systems in new domains

As mentioned earlier, the motion picture industry is an unusual application area for DSS. The organizational culture does not favor mathematical models, and the cognitive models of the decision makers are heuristics rather than analytical. Furthermore, the products, that is, the movies are changing all the time and their demand is highly uncertain and location speci<sup>fi</sup>c. In such an environment it is not easy to implement decision support systems, and it requires a lot of effort on the part of the model developers to gain the trust of the management. In this case, trust was built in an evolutionary way. After the interaction with the prediction DSS [5], the next step was the implementation of a DSS for scheduling movies in a single movie theater [7]. The development and implementation of a multi-theater multi-screen system as described in the present paper was the next step. After the present work, the Pathé management expressed a strong interest in continued involvement with the research team in developing DSS approaches to further help management decision-making. It became clear that a critical need was the detailed micro-scheduling of movies into a movie theater within a day. The management committee assigns movies to each movie theater and each screen by noon on Monday, but the local manager needs to set precise starting times for each movie by later that day. There are constraints that need to be accommodated. They include: opening and closing times of the movie theater, time needed to clean the screening room and prepare it for the next showing, avoiding the possibility that two movies end at the same time and thus creating jams. An enhancement of SilverScreener along these lines is now in progress.

This experience reported in this paper shows that it is possible to implement DSS in new domains. What can we learn from the present application? First, it is important to gain the con<sup>fi</sup>dence of the management. As demonstrated in Fig. 1, by acting in a step-by-step fashion, and by demonstrating in each step the value (incremental performance) of the DSS to the decision makers, it was possible to gain and maintain the con<sup>fi</sup>dence of management. Second, a critical aspect of the development process was maintaining managerial involvement in the model development process and accommodating their needs. As the system evolved over time, we learned more about managers' constraints and assumptions and built them into the model. As an illustrative example, in the single theater implementation [7], we had limited consideration for matinees and kids movies, but in the current implementation, we treated them in a more systematic manner. The system that was developed is a hybrid of optimal mathematical programming, demand forecasting, and heuristic procedures that meets management needs in a timely manner while improving managerial practice. Third, we believe that in a domain like the movie industry, there is no point in trying to have a model that makes all the decisions, and “automates” the process. Here, models typically have to play a decision support role. There are simply too many judgmental elements, to leave 100% of the decisions to the model. But the model and the intuition of the manager together, constitute a very powerful combination.

The current approach can be generalized to other settings within the movie exhibition sector. Here, we have already included the case of several larger theaters. It is possible that these other managerial settings in the theatrical exhibition industry may have their own set of

## Table 6

Weighted screen capacity match (in %) by movie theater over time

<table><tr><td>Week/theater</td><td>De Munt</td><td>City</td><td>Arena</td><td>Average</td><td></td></tr><tr><td>Week 1–4</td><td>44</td><td>62</td><td>49</td><td>52</td><td></td></tr><tr><td>Week 5–8</td><td>62</td><td>62</td><td>64</td><td>62</td><td></td></tr><tr><td>Week 9–12</td><td>53</td><td>60</td><td>65</td><td>59</td><td></td></tr><tr><td>Week 13–17</td><td>72</td><td>54</td><td>62</td><td>63</td><td></td></tr><tr><td>Average</td><td>58</td><td>59</td><td>60</td><td>59</td><td>Overall Average</td></tr></table>

constraints. Some of these can be handled in a similar way as done in this paper. Some other situations may involve constraints that are “micro” in nature, that is, requiring addressing issues at the “within-the-day-scheduling” level. Such issues are beyond the scope of the current model and paper, and are proposed to be addressed in future research.

The present work can also be extended to other parts of the entertainment industry, such as facilities for plays and music performances, and the scheduling of sporting events. In such areas, modeling the demand both for subscriptions (or season tickets) and for individual tickets sales would add further complication (and modeling challenge). While there is less information and consequently less knowledge about the demand for entertainment products than for frequently purchased consumer goods, substantial progress can be made in applying DSS in such <sup>fi</sup>elds. As our experience demonstrates, critical components include not only technical expertise, but also the willingness of both managers and researchers to engage in a long-term relationship and allow the DSS to evolve over time. Fig. 1 presents our process for accomplishing these goals.

Another interesting future research issue would be to compare the performance of our approach to the forecasting approaches employed by other researchers (e.g., [5]). For example, a Bayesian model might be a useful idea in more general situations. This might be of particular interest for new movies. Given a number of characteristics of a movie, one might construct a prior distribution and combine it with the <sup>fi</sup>rst weekend's results to produce a posterior forecast. Another possibility could be to consider a non-parametric approach. However, the advantage of parameterization is that the results are more readily interpretable and hence management inputs can be used to operationalize them.

## Acknowledgement

The authors thank the management of Pathé chain of movie theaters for their help and cooperation. The authors gratefully acknowledge the computational support provided by Sumit Raut.

## Appendix A. Core theater programming model

This appendix summarizes the core (or single) theater programming model which is based on the model initially used by Pathé [21]. The model is as follows:

$$
\max \sum_ {j = 1} ^ {N} \quad \sum_ {i = 0} ^ {k _ {j}} \quad \sum_ {w = r _ {j}} ^ {W - \mathrm{SCR} _ {j i} + 1} R _ {j i w} x _ {j i w}\tag{A.1}
$$

subject to

$$
\sum_ {i = 0} ^ {k _ {j}} \quad \sum_ {w = r _ {j}} ^ {W - \mathrm{SCR} _ {j i} + 1} x _ {j i w} \leq 1, \quad j = 1, \dots , N\tag{A.2}
$$

$$
\sum_ {j = 1} ^ {N} \sum_ {i = 0} ^ {k _ {j}} \sum_ {q _ {j} = w - \mathrm{SCR} _ {j i} + 1} ^ {w} x _ {j i q _ {j}} \leq H, \quad w = 1, \dots , W\tag{A.3}
$$

$$
r _ {j} \leq q _ {j} \leq W - \operatorname{SCR} _ {j i} + 1, j = 1, \dots , N; i = 0, \dots , k _ {j}\tag{A.4}
$$

$$
x _ {j i w} \varepsilon \{0, 1 \}\tag{A.5}
$$

where

N total number of movies considered during a planning horizon, x<sub>jiw</sub> 0–1 variable (1 if movie j is scheduled for i weeks beyond its obligation period starting in week w),

$R _ { j i w }$ revenue received by the exhibitor if $x _ { j i w }$ is equal to 1, ${ \mathrm { G R O S } } _ { j w }$ box-of<sup>fi</sup>ce gross revenue generated by movie j in week w, $\mathrm { P O P } _ { j w }$ concession pro<sup>fi</sup>t generated by movie j in week w,

EXSHARE exhibitor's share of box-of<sup>fi</sup>ce revenue for movie j in week w,

OPD<sub>j</sub> obligation period (the contract between the distributor and Pathé) typically speci<sup>fi</sup>es that if a movie is shown in a theater, it must be shown for a pre-speci<sup>fi</sup>ed minimum number of weeks) of movie j,

C house nut (a small <sup>fi</sup>xed amount paid every week by the distributor to exhibitor for running expenses)

$k _ { j } = W - r _ { j } - \mathrm { O P D } _ { j } + 1$ maximum possible number of weeks movie j can be shown beyond its obligation period starting in $r _ { j }$ or any feasible week thereafter, and

$\mathrm { S C R } _ { j i } = 0 \mathrm { P D } _ { j } + \mathrm { i }$ total screening period for movie j if it is shown for i weeks beyond its obligation period, where $i { = } 0 , . . . , k _ { j } .$

The net margin, $R _ { j i w }$ generated by movie j if it plays for i weeks starting in week w, is the sum of two components — (a) concession pro<sup>fi</sup>ts (e.g., popcorn and soft drinks sales) and (b) exhibitor's share of the movie's box-of<sup>fi</sup>ce gross revenue. The exhibitor's share is the fraction of the box of<sup>fi</sup>ce revenue received after paying the distributor's share (rental cost) and tax deductions. The exhibitor's share is not <sup>fi</sup>xed, but varies from movie to movie and is generally higher the longer the movie plays at the movie theater. Accordingly, $R _ { j i w }$ is given by the following expression.

$$
\begin{array}{l} R _ {j i w} = \sum_ {u = w} ^ {w + i - 1} \text {POP} _ {j u} + \text {EXSHARE} _ {j u} * \text {GROSS} _ {j u}, \\ j = 1, \dots , N; \quad i = 1, \dots , W - r _ {j} + 1; \quad w = r _ {j}, \dots , W - i + 1. \end{array}\tag{A.6}
$$

where

$\mathrm { P O P } _ { j u }$ concession pro<sup>fi</sup>ts (e.g., popcorn and soft drinks sales) generated by movie j in week u,

GROSS box-of<sup>fi</sup>ce gross revenue generated by movie j in week u, EXSHARE exhibitor's share of the box-of<sup>fi</sup>ce gross revenue of movie j in week u.\

The exhibitor's share, $\operatorname { E X S H A R E } _ { j u } ,$ is speci<sup>fi</sup>ed by the contract terms between the respective distributor–exhibitor pairs and is movie speci<sup>fi</sup>c. Following managerial practice, $\mathsf { P O P } _ { j u }$ is considered directly proportional to the attendance of a movie in a week. The attendance of a movie is determined by the demand function, which is explained in Section 4.

Denoting the attendance for movie j in week u by Attendanc $\mathrm { e } _ { j u } ,$ the corresponding revenue, ${ \mathrm { G R O S S } } _ { t j u } ,$ , is given by

$$
\mathrm{GROSS} _ {j u} = \mathrm{ATP} ^ {*} \text { Attendance } _ {j u}\tag{A.7}
$$

where ATP is average ticket price at Pathé and is estimated to be € 5.46 (the corresponding pro<sup>fi</sup>t contribution from concessions, $\mathrm { P O P } _ { j u } ,$ is estimated as follows.

$$
\mathrm{POP} _ {j u} = \text { Average   Concession   Profit   Contribution   per   Visitor*Attendance } _ {j u}\tag{A.8}
$$

The average concession pro<sup>fi</sup>t per visitor at Pathé is estimated to be € 1.00.

Statement(A.1) denotes the obiective function. which maximizes cumulative revenues over the season. Constraint(A.2) ensures that a movie is played in only consecutive weeks, if scheduled. The decision variable $, x _ { j i w }$ , denotes the length of time for which a movie is scheduled starting in a particular week. The de<sup>fi</sup>nition of this binary variable itself ensures that if a movie is scheduled, it is scheduled only for a continuous length of time. When the sum of all such possible scheduling combinations of a movie is restricted to be less than or equal to 1, at the most, only one of these combinations is chosen. This makes sure there are no multiple runs of the movie. Note that this constraint is repeated for every movie. The next constraint restricts the total number of movies scheduled in any week to the total number of screens in the multiplex. This is accomplished by summing the binary scheduling variables of all the movies either released in a week or a week before that. Restricting it to a maximum value of H, the number of screens in the multiplex, we make sure total number of movies scheduled in a week are less than or equal to the number of screens in the multiplex. The set of inequalities denoted by $\operatorname { E q . } ( \mathsf { A . 4 } )$ is an indexing constraint. Eq. (A.5) de<sup>fi</sup>nes the decision variable to be binary.

The above model is repeatedly used in the multi-theater scheduling algorithm as presented inAppendix B below.

## Appendix B. Multi-theater screen scheduling algorithm

In this appendix, we present the algorithm for assigning movies to the six Pathé theaters in Amsterdam. As can be seen, the algorithm involves recursively solving a set of single theater screening problems, while also considering some system-wide constraints.

The notation is as described below.

Indices t movie theaters [6] j number of movies [\~30] w, u calendar weeks [8] l run length of movies in number of weeks [8] s numbers of screens [14]

Parameters Parameters

$T$ number of movies theaters $S _ { t u }$ set of screens in theater t in week u $M _ { t u }$ set of movies in theater t in week u $W$ length of planning horizon $M _ { t u } ^ { k }$ set of kid movies in theater t in week u $S _ { t u } ^ { k }$ set of arti<sup>fi</sup>cial screens added in theater t for kid movies in week u $M _ { t u } ^ { m }$ set of matinee movies in theater t in week u $S _ { t u } ^ { m }$ set of arti<sup>fi</sup>cial screens added in theater t for matinee movies in week u $M _ { t u } ^ { p }$ set of pre-commitment movies in theater t in week u $S _ { t u } ^ { p }$ set of pre-commitment screen-slot in theater t for precommitment movies in week u $C _ { s }$ capacity of screen s $D _ { w j } ^ { m }$ demand of matinee movie j in week w $D _ { w j } ^ { k }$ demand of kid movie j in week w $D _ { w }$ demand matrix of movie set $X _ { w }$ in week w $D _ { w }$ $\{ D _ { w } ^ { n } , D _ { w } ^ { k } , D _ { w } ^ { m } \}$

Decision variables lables

$X _ { w }$ movies set allocation in week w $X _ { w }$ $\{ X _ { w } ^ { n } , X _ { w } ^ { k } , X _ { w } ^ { m } \}$ $X _ { w j }$ movie j allocated in week w $X _ { w j } ^ { n }$ normal movie j allocated in week w $X _ { w j } ^ { k }$ kid movie j allocated in week w $X _ { w j } ^ { m }$ matinee movie j allocation in week w

Algorithm Step 1: Set t = 1. Step 2: (initialization) Initial movie set $\overline { { M _ { w t } } } = \{ 1 , 2 , . . , m v _ { w t } \}$ , screen set, $S _ { w t } = \{ 1 , 2 , . . . , s _ { w t } \}$ on week w. Planning horizon $W { = } \{ 1 , 2 , . . . , w \}$

Step 3: (kids movie expansion set) Addition of kid movie set, $M _ { w t } ^ { k } = \{ 1 , ~ 2 , . . . , ~ m v _ { w t } ^ { k } \}$ and arti<sup>fi</sup>cial screens for kid movies allocation, $S _ { w t } ^ { k } = \{ 1 , 2 , . . . , s _ { w t } ^ { k } \}$ . The expanded sets of movies and screens are as $S _ { t w } { = } S _ { t w } { + } S _ { t } ^ { k } , M _ { t w } { = } M _ { t w } { + } M _ { t } ^ { k } .$

Step 4: (matinee movie expansion set) Addition of matinee movie set, $M _ { w t } ^ { m } = \{ 1 , 2 , . . . , m v _ { w t } ^ { m } \}$ and arti-<sup>fi</sup>cial screens for matinee movies allocation, $S _ { w t } ^ { m } = \{ 1 , 2 , . . . , s _ { w t } ^ { m } \}$ The expanded sets of movies and screens are as $S _ { t w } { = } S _ { t w } { + } S _ { t } ^ { m }$ $M _ { t w } = M _ { t w } + M _ { t } ^ { m }$

Step 5: (allocate pre-commitment movies)

Allocate pre-committed movies in the schedule matrix. Hence, The expanded sets of movies and screens are as $S _ { t w } { = } S _ { t w } { - } S _ { t w } ^ { p } ,$ $M _ { t w } = M _ { t w } - M _ { t w } ^ { p } .$

Step 6: (apply SSCR algorithm (Appendix A)) to <sup>fi</sup>nd optimal allocation for week t for the expansion set $\{ S _ { t w } , M _ { t w } \}$ problem to generate $X _ { w } = \{ X _ { w } ^ { n } , X _ { w } ^ { k } , X _ { w } ^ { m } \}$

Step 7: (screen allotment heuristic) set $w = 1$

Step 8: select the movie $j ^ { n } { \in } X _ { w } ^ { n }$ , such that, $( D _ { j w } ^ { n } = \underset { l \in { \cal X } _ { \ldots } ^ { n } } { m a x } [ D _ { l w } ^ { n } ] )$ w Select the screen $s { \in } S _ { t w } ,$ such that, $s = \mathop { m a x } _ { s \in S _ { t w } } [ C _ { s } ]$ where $C _ { w }$ is capacity of screen $s , D _ { j w } ^ { n }$ is the demand of normal movie $j ^ { n }$ at time w. If there are ties, choose the least index. Allocate movie $j ^ { n }$ on screen s.

Step 9: (double booking)

$$
f \left(D _ {j w} ^ {n} <   C _ {s}\right)
$$

$$
X _ {w} ^ {n} = X _ {w} ^ {n} - \{j ^ {n} \}.
$$

else

$D _ { j w } ^ { n } { = } D _ { j w } ^ { n } { - } C _ { s }$ and $X _ { w } ^ { n } = X _ { w } ^ { n } .$

Step 10: (kids movies)

Select kid movie $j ^ { k } { \in } X _ { w } ^ { k }$ , such that $D _ { j w } ^ { k } = { m a x } \Big [ D _ { l w } ^ { k } \Big ]$

I $\begin{array} { r } { \mathrm { ~ f ~ } D _ { j w } ^ { k } - \frac { D _ { j w } ^ { n } } { 3 } > \delta , } \end{array}$ allocate kid movie $j ^ { k }$ in screen s.

Step 11: if $D _ { i w } ^ { k } - { \textstyle \frac { D _ { j w } ^ { n } } { 3 } } > \delta ,$

$X _ { w } ^ { k } = X _ { w } ^ { k } - \{ j ^ { k } \}$ , and go to Step 14.

else

$X _ { w } ^ { k } = X _ { w } ^ { k }$ and go to Step 12.

Step 12: (matinees movies)

$$
j ^ {m} \in X _ {w} ^ {m}
$$

$$
D _ {j w} ^ {m} = \max _ {l \in X _ {w} ^ {k}} [ D _ {l w} ^ {m} ]
$$

If $\begin{array} { r } { { \bf \ddot { \theta } } _ { j w } ^ { m } - \frac { D _ { j w } ^ { n } } { 3 } > \delta , } \end{array}$ , allocate matinee movie $j ^ { m }$ in screen s. laX<sup>k</sup>

Step 13: i $\begin{array} { r } { \mathrm { ~ f ~ } D _ { i w } ^ { m } - \frac { D _ { j w } ^ { n } } { 3 } > \delta , } \end{array}$

$X _ { w } ^ { m } = X _ { w } ^ { m } - \{ j ^ { m } \}$ , and go to Step 14.

else

$X _ { w } ^ { m } = X _ { w } ^ { m }$ and go to Step 14.

Step 14: set $S _ { t w } { = } S _ { t w } { - } \{ s \} .$

I $\Gamma S _ { t w } \# \theta ,$ go to Step $^ { 8 , }$ otherwise go to Step 15.

Step 15: i $\mathrm { f } w { > } W \mathrm { g } 0$ to Step 16, otherwise, set $w = w \ : 1 , s = 1$ and go to Step 8.

Step 16: if tNT Stop, otherwise $t = t + 1$ and go to Step 2.

## References

[1] A. Amiri, Customer-oriented catalog segmentation: effective solution approaches, Decision Support Systems 42 (3) (2006) 1860–1871.

[2] B.J. Angerhofer, M.C. Angelides, A model and a performance measurement system for collaborative supply chains, Decision Support Systems 42 (1) (2006) 283–301.

[3] R.C. Blattberg, S.J. Hoch, Database models and managerial intuition: 50% models and 50% manager, Management Science 38 (8) (1990) 887–899.

[4] P. Davis, Spatial Competition in Retail Markets: Movie Theaters, forthcoming RAND, Journal of Economics 37 (4) (2008) 964–982.

[5] J. Eliashberg, J. Jonker, M.S. Sawhney, B. Wierenga, MOVIEMOD: an implementable decision support system for pre-release market evaluation of motion pictures, Marketing Science 19 (3) (2000) 226–243.

[6] J. Eliashberg, M.S. Sawhney, Modeling goes to Hollywood: predicting individual differences in movie enjoyment, Management Science 40 (9) (1994) 1151–1173.

[7] J. Eliashberg, S. Swami, C.B. Weinberg, B. Wierenga, Implementing and evaluating SilverScreener: a marketing management support system for movie exhibitors, Interfaces: Special Issue on Marketing Engineering 31 (3) (2001) S108–S127 Part 2

[8] J. Eliashberg, S.M. Shugan, Film critics: in<sup>fl</sup>uencers or predictors? Journal of Marketing 61 (2) (1997) 68–78.

[9] R. Fourer, D.M. Gay, B.W. Kernighan, AMPL: A Modeling Language for Mathematical Programming, The Scienti<sup>fi</sup>c Press, San Francisco, CA, 1993.

[10] T. Hennig-Thurau, V. Henning, H. Sattler, F. Eggers, M.B. Houston, The last picture show? Timing and order of movie distribution channels, Journal of Marketing 71 (4) (2007) 63–83.

[11] S.J. Hoch, Combining models with intuition to improve decisions, in: S.J. Hoch, H.C. Kunreuther (Eds.), Wharton on Making Decisions, Wiley, New York, 2001, pp. 81–101.

[12] R.E. Krider, C.B. Weinberg, Competitive dynamics and the introduction of new products: the motion picture timing game, Journal of Marketing Research 35 (1) (1998) 1–15.

[13] P.S. Lee<sup>fl</sup>ang, D.R. Wittink, M. Wedel, P.A. Naert, Building Models for Marketing Decisions, Springer-Verlag, 2000 Ch 7 and 19.

[14] D.R. Lehmann, C.B. Weinberg, Sales via sequential distribution channels: an application to movies and videos, Journal of Marketing 64 (3) (2000) 18–33.

[15] J.D.C. Little, Models and managers: the concept of a decision calculus, Management Science 16 (1970) B466–B485.

[16] R. Neelamegham, P. Chintagunta, A Bayesian model to forecast new product performance in domestic and international markets, Marketing Science 18 (2) (1999) 115–136.

[17] R.J. Niehaus, Evolution of the strategy and structure of a human resource planning DSS application, Decision Support Systems 14 (3) (July 1995) 187–204.

[18] S. Raut, S. Swami, E. Lee, C.B. Weinberg, How complex do movie channel contracts need to be? Marketing Science 27 (July–August 2008) 627–641.

[19] P.E. Rossi, G. Allenby, R. McCulloch, Bayesian Statistics and Marketing, John Wiley and Sons, December 2005.

[20] M.S. Sawhney, J. Eliashberg, A parsimonious model for forecasting gross box of<sup>fi</sup>ce revenues of motion pictures, Marketing Science 15 (2) (1996) 113–131.

[21] S. Swami, J. Eliashberg, C.B. Weinberg, SilverScreener: a modeling approach to movie screens management, Marketing Science 18 (3) (1999) 352–372 (Special Issue on Managerial Decision Making).

[22] TurbanEfraim , Decision Support and Expert Systems: Management Support Systems, 4th Edition, Prentice Hall, 1995, NJ, USA.

[23] G.L. Urban, R. Karash, Evolutionary model building, Journal of Marketing Research 8 (1971) 62–66.

[24] H.J. Van Heerde, P.S.H. Lee<sup>fl</sup>ang, D.R. Wittink, How promotions work: scan⁎probased evolutionary model building, Schmalenbach Business Review 54 (3) (2002) 198–220.

[25] C.B. Weinberg, ARTS PLAN: implementation, evolution and usage, Marketing Science 5 (2) (1986) 143–158.

[26] C.B. Weinberg K.B. Shachmut, ARTS PLAN: a model based system for use in planning a performing arts series, Management Science (February 1978) 654-664.

[27] B. Wierenga, G.H. Van Bruggen, R. Staelin, The success of marketing management support systems, Marketing Science 18 (3) (1999) 196–207.

[28] F.S. Zufryden, Linking advertising to box of<sup>fi</sup>ce performance of new <sup>fi</sup>lm releases — a marketing planning model, Journal of Advertising Research (July–August 1996) 29–41.

Sanjeev Swami has joined Faculty of Social Sciences, DEI, Agra, India as Professor and Head, Department of Management. Prior to joining DEI, he was Associate Professor in Industrial and Management Engineering at IIT, Kanpur, India. He holds an undergraduate degree in Production and Industrial Engineering from University of Allahabad, a master in Industrial and Management Engineering from IIT, Kanpur, and Ph.D. in Marketing from University of British Columbia, Canada. He is a doctora consortium fellow of American Marketing Association, a recipient of University Graduate Fellowship at UBC, and career awards from Department of Science and Technology, India and All India Council of Technical Education. His research work has been published in Marketing Science, International Journal of Non-pro<sup>fi</sup>t and Voluntary Sector Marketing, Journal of Operational Research Society, DEIJSER, M&SOM, Interfaces, Marketing Letters, and Vikalpa.

Jehoshua (Josh) Eliashberg is the Sebastian S. Kresge Professor of Marketing and Professor of Operations and Information Management, at the Wharton School of the University of Pennsylvania. His research interests are in developing models and methodologies to solve business problems. His research has focused on various issues including new product development and feasibility analysis, marketing/manufacturing/R&D interface, and competitive strategies. He has particular interest in the media and entertainment. pharmaceutical. and the hi-tech industries. He has authored numerous articles appearing in major journals such as: European Journal of Operational Research, Group Decision and Negotiation, Interfaces, Journal of Economic Psychology, Journal of Marketing, Journal of Marketing Research, Management Science, Manufacturing and Service Operations Management, Marketing Science, and Optimal Control Applications & Methods. His work in the entertainment industry has been the subject of articles appearing in Businessweek, The Christian Science Monitor, The Financial Post, Financial Times, Forbes, Fortune, Los Angeles Times, The New York Times Variety, Newsweek The Wall Street Journal and The Washington Post

Berend Wierenga is Professor of Marketing at the Rotterdam School of Management, Erasmus University. His main research area is marketing decision making and marketing decision support. Together with Gerrit van Bruggen he published a book on Marketing Management Support Systems (Kluwer Academic Publishers 2000). He has (co-) authored several articles on decision support systems in the domain of marketing (e.g. Journal of Marketing, Marketing Science, International Journal of Research in Marketing, Management Science), as well as in the general IS/DSS domain (e.g. MISQ, Communications of the ACM, and Decision Support Systems). Berend Wierenga is also the Editor of the Handbook of Marketing Decision Models (2008), published by Springer Science +Business Media.

Charles B. Weinberg is the President of SME Vancouver Professor of Marketing at the Sauder School of Business, University of British Columbia, Vancouver, Canada. In 2008, he was selected as one of the <sup>fi</sup>rst ten fellows of the INFORMS Society for Marketing Science. His research focuses on analytical marketing, services, and public and nonpro<sup>fi</sup>t marketing. His work in the nonpro<sup>fi</sup>t sector includes pricing, the marketing of safer sex practices, portfolio management and competition. For more than 30 years, he has studied the arts and entertainment industries. His early work focused on live entertainment and included the ARTS PLAN model for marketing and scheduling performing arts events. More recently, he has focused on the movie industry in which he has studied such issues as competitive dynamics, scheduling of movies into theaters, sequential release of movies and DVDs, and contract terms. He is a former editor of Marketing Letter and former area editor of Marketing Science. He served as chair of the 2008 Marketing Science conference in Vancouver.
