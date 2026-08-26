---
otero_id: 15660
otero_key: "688KZJKZ"
title: "On the relationship between number of votes and sentiment in crowdsourcing ideas and comments for innovation: A case study of Canada's digital compass"
authors: "Daniel E. O'Leary"
year: "2016"
journal: "Decision Support Systems"
doi: "10.1016/i.dss.2016.05.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# On the relationship between number of votes and sentiment in crowdsourcing ideas and comments for innovation: A case study of Canada's digital compass

Daniel E. O'Leary

University of Southern California, Marshall School of Business, Los Angeles, CA 90089, United States

a r t i c l e i n f o

Article history: Received 18 December 2015 Received in revised form 20 May 2016 Accepted 21 May 2016 Available online 31 May 2016

Keywords: Crowdsourcing Innovation Number of votes Sentiment analysis

## a b s t r a c t

Recently, PWC facilitated an innovation crowdsourcing effort entitled “Canada's Digital Compass” aimed at generating creative directions for Canada to pursue in its future. As part of this effort, over 70 ideas were submitted and over five hundred votes on those ideas were generated. This paper analyzes data developed as part of that effort, investigating a number of relationships between different variables elicited from the analysis and the number of votes for those ideas. The analysis confirms some previous results, provides a structure for interpreting those results and generates some new results. In particular, this paper generates sentiment measures for both the innovation ideas and for the comments. Using a decision tree approach we find that the number of comments and the extent to which the sentiment in those comments is positive are statistically significantly related to the number of votes. In addition, using regression analysis, this paper finds that the number of votes is statistically significantly related to the interaction between sentiment measures for ideas and comments. Finally, a rationale for these results, based on game theory is proposed and investigated.

© 2016 Elsevier B.V. All rights reserved

## 1. Introduction

Recently, there has been substantial interest in gathering the “wisdom of the crowd” (e.g., [19]). One application that has generated substantial interest is in the area of innovation (e.g., [5]). In particular, idea gathering and rating systems provide the opportunity to solicit information from the crowd about innovations. Such systems allow users to suggest ideas, vote on ideas and make comments on ideas. In practice, voting platform systems, such as Chaordix<sup>1</sup> and others have been developed and implemented in different environments to help organizations facilitate idea generation and enhancement. Such voting systems generally are used to gather ideas and information about ideas rather than facilitate any cocreation of ideas by creating virtual teams or groups.

Typically, the information that is gathered is immediately available to the crowd. Ideas are formulated and placed on line virtually immediately after their submission. Participant comments are made available to the other participants in real time and information about who made the comments is broadly available to all. User votes are then accumulated for the different ideas. As a result, as part of their use, these systems typically generate information about votes, ideas and comments. The number of votes for an idea provides a measure of the relative support for the innovation, the relative quality or the innovativeness of the idea, by the crowd, as compared to the other ideas. Accordingly, these systems provide decision support information to management and can help management focus on the better ideas. Thus, there is interest in understanding what factors relate to the number of votes that an innovation idea generates and how these variables are related.

Some characteristics and relationships between the number of votes, and idea and comment information have been analyzed by previous researchers. Gangi and Wasko [5] as part of an innovative analysis of using crowdsourcing for innovation using Dell's IdeaStorm found the strongest correlation (0.74) between “total number of votes” was with “total number of comments.” In particular, that relation was positive and statistically significant at better than .01.

However, that analysis also raised a number of additional questions. First, the analysis was a case study analyzing one set of innovations. As a result, there is interest in determining if that relationship holds in other settings. Second, it is not clear a priori why that relationship would hold in crowdsourcing votes on innovations. Why would voters tend to comment on those innovation ideas that they vote for? For example, it would seem that ideas with few votes could easily generate a substantial number of comments detailing how and why the ideas are not effective and why people did not or should not vote for them. In that case there would be a negative relationship between the number of comments and the number of votes. Accordingly, the empirical result suggests that voters largely limit their comments to those ideas that they also voted for. As a result there is interest in finding a theory or theories that might help explain that result. Third, although that analysis suggests that a model aimed at estimating the total number of votes for innovations, likely would include the total number of comments, it is not clear what other variables might be related to the number of votes. For example, does information about the idea count, is it related to the number of votes? Fourth, previously researchers in innovations have focused primarily on the quantitative variables that count the number of something, such as “number of comments,” and others. Accordingly, previous researchers have ignored information that relates to issues such as the sentiment of the ideas and the comments on the innovations. As a result, it is unclear how idea or comment sentiment might relate to the number of votes for innovations.

Accordingly, the purpose of this paper is to extend the research of Gangi and Wasko [5] to investigate those four issues associated with using the crowd to vote on innovations. Although Gangi and Wasko [5] did find a relationship between the number of comments and the number of votes, they did not propose a theory, discuss idea analytics or analyze the qualitative variables. Accordingly, this paper investigates those issues within a crowdsourcing idea voting system. The system used was Canada's Digital Compass project which was moderated by PWC. This resulted in the following findings.

## 1.1. Findings of this paper

These questions lead to a number of findings. First, this paper finds a similar result to the previous literature for the correlation between the number of comments and the number of votes, with a positive and statistically significant result. Second, this paper investigates the relationship between number of votes and comments, in particular, those ideas that get comments (compared to those that do not). Voting systems provide a number of capabilities that have led to changes in transparency in information about content and contributors with some interesting implications. As a result of this transparency, the game theoretic notion of “tit-for-tat” is suggested as a potential rationale for why more popular ideas get comments and less popular ideas do not receive as many comments. Tit-for-tat is a notion that equivalent actions will be given in return. Thus if you give a negative comment on my idea, then I would give a negative comment on your idea, or conversely. This paper suggests that because of the transparency of such systems, crowdsourced voters tend to comment mostly on the high vote getting ideas and provide largely positive comments. Third, this paper finds that information about the idea is related to the number of votes. In particular, the number of words in the idea is related to the number of votes. Fourth, although such crowd voting systems provide many different structured variables to examine (e.g., number of comments, number of words, etc.) such variables do not account for the unstructured information resulting from such systems, e.g., the sentiment content of the ideas or the comments. As a result, this paper uses sentiment analysis in order to provide some structured analysis on unstructured text data as part of the analysis of the number of votes that an idea gets.

## 1.2. This paper

As a means of structuring the analysis of these findings, this paper proceeds as follows. Section 1 has reviewed and motivated the paper. Section 2 provides a brief review of some background concepts, such as crowdsourcing and a review of some of the previous literature in crowdsourcing and the number of votes. Section 3 provides some background information on the Digital Compass project. Section 4 summarizes the data and the variables used in this analysis. In particular, this section provides structured analytics to analyze unstructured text. Section 5 summarizes the expected relationships between the data variables and the number of votes that an idea gets. Section 6 investigates some of the findings from the summary data, the correlation matrix and the regression analyses between idea and comment variables as used to estimate the number of votes. Section 7 briefly summarizes the paper, reviews its implications, contributions and investigates some extensions.

## 2. Background and selected previous research in innovations and crowdsourcing

The notion of crowdsourcing was examined by Howe [10] and others, who distinguished between crowdsourcing and outsourcing. In particular, Howe [10] called crowdsourcing “… the process by which the power of the many can be leveraged to accomplish feats that were once the province of a specialized few.” While quoting a Vice President of Innovation at Procter & Gamble, Howe [10] notes “Outsourcing is when I hire someone to perform a service and they do it and that's the end of the relationship. That's not much different from the way employment has worked throughout the ages. We're talking about bringing people in from outside and involving them in this broadly creative, collaborative process. That's a whole new paradigm (crowdsourcing).”

Starting at least with IBM's Innovation Jams in 2007 [2,8] there has been interest in using crowdsourcing systems to facilitate innovation. As an example, Bjelland and Wood [2] focused on documentation of the process and outcomes. O′Leary [15] investigated a case focusing on Accenture's use of crowdsourcing to develop and rate innovations. As another example, Hossain and Islam [9] investigated Dell's IdeaStorm, focusing on the extent of implementation of proposed ideas.

However, there seems to have been limited empirical analysis of the relationships between key variables and the number of votes, associated with these crowdsourcing innovation system efforts. In particular, our scope of analysis of the previous literature is limited to the task of using crowdsource software for innovation and the resulting relationships between different characteristics and the number of votes an idea gets. Baily and Horvitz [1] investigated a number of variables related to innovation management systems, but provided limited analysis of relationships between sets of variables. Gangi and Wasko [5] found a statistically significant correlation between number of comments and number of votes, when they examined the broader innovation process. Similarly, Fuller et al. [4] also found that the number of comments was statistically related to the number of votes. Although other innovation researchers have investigated the correlation between different variables their analyses have not considered emerging variables, such as sentiment or the relationship between sentiment-based characteristics of ideas and comments.

Further, previous researchers have not fully examined the potential effects of transparency on the use of such crowdsourcing systems. Instead, previous research with transparency and voting systems has largely been concerned with government transparency [13]. However, in this paper we investigate the potential impact on innovation systems of requiring comments and ideas to be attributed to particular people, rather than allowing anonymity. Specifically, including identities of the participants on the ideas and the comments removes asymmetries of information.

2.1. Use of sentiment analysis in other settings: blogs, product reviews and on-line forums

There are a number of differences with the use of sentiment in crowdsourcing for innovation, in contrast to blogs, product reviews and other settings. In crowdsourcing for innovation, there is both an idea and the comments on the idea. As a result, there is a question as to the impact of sentiment from the idea statement, sentiment from the comments and potential interaction effects. In addition, it is not clear that settings designed for gathering innovations and innovation information from the crowd is directly comparable to other settings. In particular, different settings provide unique context capabilities that likely can be leveraged.

Although this paper focuses on using crowdsourcing for innovation, sentiment analysis has been used in the analysis of a range of different problem settings. Li and Wu [12] investigated sentiment in the analysis of on-line forums. O'Leary [14] investigated the use of sentiment analysis in blogs. Saleham and Kim [18] used sentiment analysis in online customer reviews. Ullah et al. [20] investigated the use of sentiment analysis and other approaches in the analysis of product reviews. Oliverva et al. [16] examined sentiment lexicon acquisition for stock market settings.

![](/api/attachments/688KZJKZ/fulltext/images/56787af332ca7b4ec6ddadf4e5f5d4638df45d49ec71c74338970045e8102cd2.jpg)  
Fig. 1. Canada's digital compass. Source (no longer valid): http://pwc-compass.chaordix.com/.

## 3. Crowdsourcing competition to define Canada's future role in the digital economy

PricewaterhouseCoopers (PWC), a “Big 4” professional services firms, hosted a crowdsourcing competition aimed at helping to define Canada's future role in the digital economy (see Fig. 1)[17]. The crowdsourcing effort was done using Chaordix's crowdsourcing platform.<sup>2</sup> Crowdsourcing allows users to present ideas, vote on ideas and comment on those ideas.

Chaordix has been used in a number of previous crowdsourcing events. Geraci [6] summarizes some of the history of Chaordix, including its evolution from Cambrian House in 2008, after being one of the first to offer crowdsourcing software.

The overall question addressed as part of the crowdsourcing task was “How can Canada best lead in a global digital economy?” Ideas were placed into five different categories (technology, education, media, connectivity and policy). Seventy-one ideas were presented and four hundred and five comments were made on those ideas. There were two hundred and seven participants. There were 543 votes cast. Individual category winners were chosen and then three overall winners, from the leading vote getters, were chosen by a panel of five experts.<sup>3</sup>

Corresponding to those five different categories, there were five innovation competitions. The first competition, for technology ideas, lasted two weeks. Each of the other competitions was given a single week.

• Technology — March 16–29, 2010

• Education — March 30–April 5, 2010

• Media production — April 6–12, 2010

• Connectivity — April 13–19, 2010

• Policy development — April 20–26, 2010

Canada's Compass discussion was moderated. Different moderators were used in each of the five different areas.

## 3.1. Ideas had a specified format

Ideas were provided a standard format to facilitate idea specification and comparison of the content in the ideas. That format contained the following information.

• Summary

• Why I believe in this idea

• Economic potential

• Unique opportunity for Canada

• Reflects Canada's value.

This format provides some assurance as to the comparability of the ideas to each other, and that the ideas are “thought through” before they are presented to the crowd.

## 3.2. Participants, voting and comments

The forum was an open one, but participants had to register. Participants could either vote for or against an idea. However, participants did not have to vote. As a result, an idea could have positive, negative or no votes. Although votes were anonymous, the crowd was aware of who had made which ideas and corresponding comments.

## 3.3. Importance of the data set

This data provides a relatively unique glimpse of the crowd's evaluation of a set of innovations. First, the innovations were aimed at a very important concern with potential substantial impact: developing recommendations for the Canada's digital future. Second, with seventyone ideas, there was a reasonably large group of ideas provided to be compared and analyzed. Third, although it is in North America, it provides a non-United States data set, thus providing additional evidence over and above studies from what are likely United States events (e.g. [5]). Fourth, since PWC was involved in managing the process, it is unlikely that the event reflected any hacking or attempts to defuse the crowdsourcing effort.

## 4. Data

This section summarizes the raw data analyzed in this paper. In addition, this section discusses generating the sentiment measures from the idea statements and the comments.

## 4.1. Crowdsourcing data

The data was originally gathered in September–October 2014 from PWC's web site “Canada's Digital Compass.” Unfortunately, the web site from which the data was gathered is no longer available on line. Although the Digital Compass project occurred roughly five years ago, this is the first analysis of the data of which the author is aware.

In order to access the data for this project the author joined the web site.<sup>4</sup> However, at no time did I make any comments or propose any ideas. After joining, I downloaded information that related to each of the projects that was available on the site.

## 4.2. Independent and dependent variables

The information was put into four categories: votes, ideas, comments and sentiment. Each idea had a certain number of votes as a consequence of the process. Number of votes is treated as a dependent variable, since the number of votes is a consequence of the idea, the write-up of the idea and the comments of the other participants. Data about the ideas and comments were treated as the independent variables. Similarly, data related to sentiment was treated as an independent variable.

## 4.3. Sentiment

Sentiment was gathered using Python NLTK (natural language tool kit)<sup>5</sup> for both the write-up of each idea and each idea's set of comments. Python NLTK has been used in a number of different settings to capture the “sentiment” of text. For example, Khan et al. [11] analyze online customer reviews and Ding et al. [3] were concerned with stock market prediction using sentiment analysis.

Python NLTK provides up to two sets of analytics: Subjectivity Measures and Polarity Measures. The subjectivity measures capture the extent to which the text is “neutral” and “polar” and the polarity measures capture the extent to which the text is “positive” and “negative” (see Fig. 2). Each of the measures is non-negative. Further, the neutral and polar measures sum to one, and the positive and negative measures sum to one. For example, in Fig. 2, the subjectivity measure has neutral of .1 and polar of .9, and it has polarity measures of pos (positive) of .2 and neg (negative) of .8. However, if the subjective polar measure is not large enough then no “polarity” measures are given (e.g., Fig. 3). In that case there is no positive sentiment or negative sentiment, the text is neutral.

Accordingly, this research captured the subjectivity analytics and the polarity analytics as measures of the sentiment for both the idea and the comments. Since the numbers sum to 1 only the “Subjectivity — Polar” and the “Polarity — Positive” numbers were captured. The “Subjectivity — Polar” also is referred to as “Idea Sentiment Polar” and “Comment Sentiment Polar.” The “Polarity — Positive” also is referred to as the “Idea Sentiment Positive” and the “Comment Sentiment Positive.”

We will distinguish between the three cases of

• existence of positive sentiment (pos ≥ .1),

• equal positive and negative sentiment (pos = .5) and

• more positive than negative sentiment (pos ≥ .6).

In each of these three cases, the comment or idea is not neutral, and does have some positive sentiment, with varying amounts of negative sentiment. In the second case, the amounts of negative and positive sentiment are equal. In the third case there is more positive sentiment than negative.

## 4.4. Approach

Each idea and set of corresponding comments was captured as a file. The number of words in each idea and in each set of comments was generated. In addition, since each idea and each set of comments was separately available, each of the files was used to separately determine the related sentiment measure using Python NLTK.

## 4.5. Variables

Accordingly, based on the available data, there were eight available different variables

• Number of votes

• Number of words in the idea

• Number of comments

• Number of words in the comments

• Idea sentiment (positive and polar)

• Comment sentiment (positive and polar).

Because of the nature of the sentiment development process, only idea sentiment (polar) was available for all 71 ideas. In some cases the algorithm also found some positive sentiment associated with the ideas (n = 33). In addition to sentiment information for the ideas, sentiment information also was gathered for those ideas with comments. 63 ideas had comments and 55 of those 63 generated positive sentiment measures, in addition to their polarity estimates. Ultimately, these different sets of available variables guided the analysis.

## 5. Expected relationships between variables

There are a number of characteristics of both ideas and comments that can be measured and analyzed. This section analyzes some of the anticipated relationships between those characteristics and the number of votes.

## 5.1. Number of votes

Perhaps the most important variable is the number of votes that an idea gets. In this setting, the number of votes provides one of the key analytics leading to which ideas are chosen for implementation. We investigate whether the number of votes for an idea is related to

• Number of words in the idea

• Idea sentiment

![](/api/attachments/688KZJKZ/fulltext/images/9e52bd1cc06b72b25a1f87cbcdd9ce3c3747008b6d6c4900bd930620925cadb4.jpg)  
http://text-processing.com/demo/sentiment/

Fig. 2. Sentiment — subjectivity and polarity measures.  
![](/api/attachments/688KZJKZ/fulltext/images/3cfef6cfe2db7a6997cc4af073580fbda0fcb34a6381eecc6d7211c11f2a16ab.jpg)  
http://text-processing.com/demo/sentiment/  
Fig. 3. Sentiment — subjectivity measure only.

• Number of comments

• Comment sentiment

• Number of words in the comments.

## 5.2. Number of words in the idea

It is not clear, a priori, if the number of words in the idea would be related to the number of votes in this context. As noted above, each of the ideas presented in this analysis were generated using the same format template. Accordingly, a certain number of words are required to meet the requirements of the format.

Voters can easily compare the ideas for the extent to which they have completed the appropriate form and provide sufficient discussion. If an idea does not meet the minimal descriptor requirements then the idea is likely to have fewer words. Further, if the idea discussion does not fully describe the idea then it might not garner all of the votes that it potentially could gather. In addition, if an idea presenter provides more words it can appear that the idea has greater substance. Finally, the number of words may provide some measure of complexity of the idea.

However, there have been a number of literary analysts indicating the importance of fewer rather than more words.<sup>6</sup> For example, Anatole

France is reported to have said “The best sentence? The shortest.” Blaise Pascal suggested that “The letter I have written today is longer than usual because I lacked the time to make it shorter.” Accordingly, there are equivocal expectations about the relationship between the number of words in the idea and the number of votes.

## 5.3. Idea sentiment

It is likely that the idea sentiment should be at least neutral or positive. However, putting too much of a positive sentiment spin on an idea may have a negative effect on potential voters if they see the spin as exaggerated or false praise. Alternatively, too much of a neutral presentation may not convince potential voters about the potential for the idea. In contrast, if the idea sentiment was negative then that would suggest that even the idea proposer was not in favor of the idea. If the proposer is not in favor of the idea then that likely would have a negative impact on the number of votes. Accordingly, this would suggest that each idea should at least have idea sentiment polarity, but not necessarily positive idea sentiment.

However, it is not clear that simply having a neutral or positive sentiment in the idea would generate more votes. Accordingly, there are equivocal expectations about the relationship between idea sentiment and the number of votes.

5.4. Number of comments and comment sentiment: visibility vs. potential for recourse

Digital Canada used a crowdsourcing system that made the identities of the idea contributors and the idea commentators visible. Potentially, that visibility can impact the actions of the participants resulting in game-like behavior. In particular, visibility could influence whether or not someone comments on an idea. In contrast to the situation with “Digital Compass,” on the Internet, in general, there is substantial anonymity. As a result, on the Internet it is easy to criticize and not be held accountable for those criticisms.

However, with Digital Compass's moderation and registration of names, contributors could be tracked by other contributors. For that setting, consider two cases, one where the idea seems promising and one where the idea does not seem promising.

First, suppose that a commentator identifies an idea that seems promising. There are at least two sets of actions. First, they could comment positively about the idea. In that case their positive comments would be traceable to them. If the commentator also had an idea contributed to the system then there may be a quid pro quo exchange of positive comments. Second, they could just vote for the idea, however, in that setting they would miss the opportunity for a positive exchange of comments. As a result, we would expect that those ideas that were seen as attractive would be commented on, resulting in more comments for those ideas with more votes.

Second, suppose that a potential commentator identifies an idea that does not seem promising. There are at least two actions that they can pursue. First, they could comment negatively about the idea. In that case their negative comments would be traceable back to them. As a result, if they had an idea under consideration, then the originator of the idea being criticized could comment negatively on that person's idea. Thus, there could be recourse against a negative comment. Second, alternatively the commenter could just “not” vote for the idea or vote negatively against the idea. In that setting there would be no potential recourse, since there was no information captured about who voted for which ideas. Accordingly, in a system where the commenter can be identified (i.e., is visible or transparent) and there is the potential for recourse, it likely is more prudent to not comment on the idea. As a result, we would expect that those ideas that were not seen as attractive, would not be commented on or have as many comments as those ideas seen as more attractive.

This discussion suggests a game theory structure (e.g. [7]) to the provision of comments, and whether those comments are positive or negative in their sentiment. For example, the classic “tit-for-tat” solution to the prisoner's dilemma provides one potential description to the situation. The results of this discussion are summarized in Fig. 4.

Accordingly, this discussion suggests that the number of comments will be positively related to the number of votes and the positive sentiment of the comments will be positively related to the number of votes.

## 5.5. Number of words in the comments

A priori, the number of words in the comments is likely to be highly correlated with the number of comments. As a result, we would expect that the number of words in the comments would be related to the number of votes. However, as with the number of words in an idea, it is not clear that there are any particular rationales between the number of words in the comments and the number of votes.

## 5.6. Interaction of idea and comment sentiment

If the idea sentiment is positive and the comment sentiment is positive, then that likely would suggest a situation most conducive to the reception toward an idea: the innovator likes the idea and provides a positive statement of it and the commenters speak favorably about the idea. As a result, the interaction between idea and comment sentiment is likely to be positively related to the number of votes.

## 6. Findings

This paper summarizes findings from analyzing the data. The summary statistics are presented in Table 1.

## 6.1. Correlation analysis

The correlational relationships between the variables and their statistical significance are summarized in Table 2. The number of votes was positively and statistically significantly correlated with a number of variables: number of words in idea, number of comments, number of words in comments and idea sentiment positive.

Some of the sentiment measures were positively and statistically significantly correlated with each other. Positive idea sentiment and positive comment sentiment were correlated at .2086 (p = .0632, on a one tail test), while polar idea and polar comment sentiment measures were correlated at .2434 (p = .0273 on a one tail test). These last two findings suggest that there may be some interaction between the sentiment measures for ideas and comments and for the subjectivity measures for ideas and comments.

## 6.2. Comparison of sentiment for ideas and comments

As seen in Table 1, the average idea polarity was 0.480 (n = 71) and the average comment polarity was 0.735 (n = 63). Accordingly, the ideas were written with greater neutrality than the comments. Using a two-tailed test of proportions the two average polarity measures (from sentiment and comments) are statistically significantly different at better than .0019. Further, both of the average polarities were statistically significantly different than zero.

The average positive idea sentiment was 0.764 (n = 33) and the average positive comment sentiment was 0.573 (n = 55). Accordingly, using a two-tail test of the statistical significance of the difference between the average positive sentiment measures of the idea and the comments, was statistically significant at p = .0584.

Each of the 71 idea statements was measured as either positive (33) or neutral (38). There were no ideas with negative sentiment (idea sentiment positive), i.e., Pos ≥ .5 for each of those with an estimate, providing additional evidence that each idea was written to either a neutral or positive sentiment.

## 6.3. Visibility–recourse theory

Four different sets of results support the visibility–recourse theory (Fig. 4). First, an analysis of the data finds that only one of the top 44 (out of 71) vote getting ideas (4 or more votes) did not get any comments, whereas 7 out of the remaining 27 ideas (3 or fewer votes) did not get any comments. A Z-test finds the difference between those two proportions has a Z-score of 3.0599, where p = .00222.

Second, Fig. 5 summarizes the number of ideas and votes for different comparison states, and the Z-test results for the test of proportions. At the first level, the number of ideas with no comments (8) and the number of votes (15) are compared to the number of ideas with comments (63) and the corresponding number of votes (528). Using a Z test of difference of proportions, the difference was p = .000. As a result, the lack of comments apparently is a strong signal suggesting that an idea will not get many votes.

Third, on the third level of Fig. 5, where the positive sentiment is grouped into those ideas with “Pos b .6” and “Pos ≥ .6,” using the Ztest of difference of proportions the probability was $\mathsf { p } = . 0 0 0 1 2$ . This finding suggests the relationship between positive comment sentiment and the number of votes.

Summary of data.  
![](/api/attachments/688KZJKZ/fulltext/images/b7b1a2a39354b876276fa6de6ff54748aa4e68f6a06ee5b4a8dcb91c42742cf2.jpg)  
True Identity of Commenter Visible  
Fig. 4. Visibility vs. recourse.

Fourth, if we combine the first two levels in Fig. 5 we determine that we have 16 ideas that generate 60 votes (no comments or no positive sentiment in the comments) and 55 ideas that generate 483 votes (with positive sentiment). A Z-test of difference in means yielded a Z score of 3.311 and p = .00094. This indicates that the average number of votes is statistically significantly different based on the sentiment in the comments.

Each of these results is consistent with the visibility–recourse theory presented above. Voters tend to ignore ideas that they do not vote for, and comment on ideas that they do vote for. In addition, the last two sets of analyses suggest a positive relationship between positive comment sentiment and the number of votes.

## 6.4. Regression analyses

This section summarizes the findings associated with estimating the number of votes based on information from the ideas and comment variables using regression analysis. Table 3 contains the results of estimating the number of votes from five different models.

Model 1 uses those variables that were available for all 71 ideas: number of words in the idea, the number of words in the comments and the number of comments and the idea sentiment (polar). Only the number of comments was statistically significant although idea sentiment (polar) was the closest of the remaining variables. The coefficient on number of comments was positive. Unfortunately, the

## Table 1

<table><tr><td></td><td>Number of words in idea</td><td>Number of comments</td><td>Number of words in comments</td><td>Idea sentiment (positive)</td><td>Idea sentiment (polar)</td><td>Comment sentiment (positive)</td><td>Comment sentiment (polar)</td><td>Product of “positive” senti-ment</td><td>Product of “polar” senti-ment</td></tr><tr><td>Maximum</td><td>1121</td><td>19</td><td>2529</td><td>0.9</td><td>0.8</td><td>0.8</td><td>0.9</td><td>0.72</td><td>0.72</td></tr><tr><td>Minimum</td><td>130</td><td>0</td><td>0</td><td>0.5</td><td>0.1</td><td>0.2</td><td>0.2</td><td>0.24</td><td>0.04</td></tr><tr><td>Average</td><td>390</td><td>5.7</td><td>499.62</td><td>0.76</td><td>0.48</td><td>0.57</td><td>0.73</td><td>0.44</td><td>0.38</td></tr><tr><td>Number of ideas</td><td>71</td><td>63</td><td>63</td><td>33</td><td>71</td><td>55</td><td>63</td><td>29</td><td>63</td></tr></table>

## Table 2

Correlation coefficients.

<table><tr><td>Column</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Variable</td><td>Number of words in idea</td><td>Number of comments</td><td>Number of words in comments</td><td>Idea sentiment (positive)</td><td>Idea sentiment (polar)</td><td>Comment sentiment (positive)</td><td>Comment sentiment (polar)</td></tr><tr><td>Number of votes</td><td>0.3252***</td><td>0.7067***</td><td>0.6548***</td><td>0.3037*</td><td>-0.0374</td><td>0.1791</td><td>0.0851</td></tr><tr><td>Number of words in idea</td><td></td><td>0.3664***</td><td>0.4342***</td><td>-0.1851</td><td>-0.0449</td><td>0.0439</td><td>0.1658</td></tr><tr><td>Number of comments</td><td></td><td></td><td>0.8828***</td><td>0.2884</td><td>0.1338</td><td>0.3089**</td><td>0.2177*</td></tr><tr><td>Number of words in comments</td><td></td><td></td><td>0.1492</td><td>0.1066</td><td>0.1863</td><td>0.1602</td><td></td></tr><tr><td>Idea sentiment (positive)</td><td></td><td></td><td></td><td></td><td>0.1455</td><td>0.2086</td><td>0.0703</td></tr><tr><td>Idea sentiment (polar)</td><td></td><td></td><td></td><td></td><td></td><td>0.0937</td><td>0.2434*</td></tr><tr><td>Comment sentiment (positive)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-0.1113</td></tr><tr><td>Number</td><td>71</td><td>71</td><td>71</td><td>33</td><td>71</td><td>55</td><td>63</td></tr></table>

Two tail test probabilities.  
⁎ p ≤ .1.

![](/api/attachments/688KZJKZ/fulltext/images/a074150aebe4d3703dcb382ce7885db71fb6f1fe45ebcc31c7576abb1f86c673.jpg)  
Fig. 5. Tree of comment sentiment using test of proportions.

maximum VIF measure (4.8428) suggested potential moderate multicollinearity.<sup>7</sup> As a result, those variables were tested in additional models.

In model 2, the number of votes is modeled using the comment information (excluding number of comments — found to be significant in model 1), in particular, the number of words in comments, the comment sentiment (positive) and the comment sentiment (polar), and the maximum VIF measure was 1.0490, suggesting no multicollinearity. The results indicate that number of words in the comments is statistically significant at better than .0001.

In model 3, the number of votes is modeled using the idea information, in particular, the number of words in the idea is found to be positively and statistically significantly related to the number of votes. The maximum VIF measure was 1.0020, indicating no multicollinearity. Perhaps the number of words provides one measure of the complexity of the idea write-up. Together, models 2 and 3 suggest that the number of words in the ideas and comments provide important information for estimating the number of votes.

In model 4, in conjunction with number of words in comments and the interaction between idea sentiment (positive) and comment sentiment (positive) was found to be statistically significant at p = .0326, with a maximum VIF of 1.0986. This model was developed after eliminating one of two outliers.<sup>8</sup> In model 5, in conjunction with the number of words in the idea, the interaction between idea sentiment (positive) and comment sentiment (positive) was found to be statistically significant at .0241. The maximum VIF measure was 1.0292 indicating no multicollinearity. In model 6, the interaction between idea sentiment (positive) and comment sentiment (positive), by itself, was found to be statistically significant at .0204. Accordingly, these models suggest that positive sentiment about an idea and positive sentiment in the comments interact to provide insight into the estimation of the number of votes. In particular, measures of qualitative sentiment matter.

## 7. Summary, implications, contributions and extensions

This paper provides an analysis of the data of a crowdsourcing study designed to elicit Canada's digital future. In so doing this paper generated an analysis of some of the structured and unstructured data relating number of votes received to characteristics of ideas and comments. Along with structured variables of number of comments, number of words in comments and number of words in the idea, the interaction of positive idea sentiment and positive comment sentiment was found to be statistically significant in the estimation of the number of votes. A summary of the results generated in this paper are given in Table 4.

## 7.1. Implications

There are a number of implications of the findings in this paper. First, the visibility-recourse argument (“tit-for-tat”) suggests that the idea and comment process could be inhibited because of the lack of information asymmetries. Accordingly, organizations may wish to try using both approaches (blind comments and non-blind comments) and see which seems to work best in their setting. Second, these results suggest that sentiment plays an important role in estimating the number of votes that an idea receives. Fig. 5 suggests that just a comparison of whether or not an idea got any comments will provide important insight into the estimation of the number of votes. Third, Fig. 5 also emphasizes the importance of sentiment positive (≥.6) in estimating the number of votes. Finally, as seen in Table 3 models 4, 5 and 6, the interaction of positive idea and comment sentiment is positively and statistically related to the number of votes.

## 7.2. Contributions

This paper has a number of contributions. First, this paper substantiates the relationship between the number of votes and the number of comments on innovations by the crowd with another case study. Second, this paper also found that a measure of the idea, the number of words, is positively related to the number of votes. Thus, both the idea and the comments matter. Third, this paper expands the base of variables that have been analyzed in crowdsourcing to include sentiment. In particular, sentiment, in both comments and ideas, and their interaction, is found to be related to the number of votes that an innovation idea generates. Fourth, this paper presented a framework to analyze why some innovation ideas get comments and others do not resulting in the visibility and recourse framework.

Regression models.  
Table 3

<table><tr><td>Model</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Model variables</td><td>Ideas and comments</td><td>Comment only</td><td>Ideas only</td><td>Comment and comment * idea</td><td>Idea and comment * idea</td><td>Comment * idea</td></tr><tr><td>Number of ideas</td><td>71</td><td>55</td><td>71</td><td> $28^a$ </td><td>29</td><td>29</td></tr><tr><td>R-square</td><td>0.5223</td><td>0.4185</td><td>0.1063</td><td>0.2955</td><td>0.1837</td><td>0.1835</td></tr><tr><td>Number of words in idea</td><td>0.0024</td><td></td><td>0.0157</td><td></td><td>0.0007</td><td></td></tr><tr><td>Prob &gt; |t|</td><td>0.6098</td><td></td><td>0.0062</td><td></td><td>0.9386</td><td></td></tr><tr><td>Number of comments</td><td>1.1918</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Prob &gt; |t|</td><td>0.0013</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Number of words in comments</td><td>0.0018</td><td>0.0108</td><td></td><td>0.0035</td><td></td><td></td></tr><tr><td>Prob &gt; |t|</td><td>0.5601</td><td>0.0001</td><td></td><td>0.1378</td><td></td><td></td></tr><tr><td>Idea sentiment (polar)</td><td>-4.3076</td><td></td><td>-0.7666</td><td></td><td></td><td></td></tr><tr><td>Prob &gt; |t|</td><td>0.1413</td><td></td><td>0.8428</td><td></td><td></td><td></td></tr><tr><td>Comment sentiment (positive)</td><td></td><td>5.2641</td><td></td><td></td><td></td><td></td></tr><tr><td>Prob &gt; |t|</td><td></td><td>0.5943</td><td></td><td></td><td></td><td></td></tr><tr><td>Comment sentiment (polar)</td><td></td><td>-3.2536</td><td></td><td></td><td></td><td></td></tr><tr><td>Prob &gt; |t|</td><td></td><td>0.8252</td><td></td><td></td><td></td><td></td></tr><tr><td>Idea sentiment (positive) * comment sentiment (positive)</td><td></td><td></td><td></td><td>28.1329</td><td>37.2809</td><td>37.0767</td></tr><tr><td>Prob &gt; |t|</td><td></td><td></td><td></td><td>0.0326</td><td>0.0241</td><td>0.0204</td></tr></table>

<sup>a</sup> Excludes one outlier.

## 7.3. Extensions

This paper can be extended in a number of directions. First, this paper investigated data generated from a crowdsourcing effort designed around Canada's digital future. Future research could examine other such crowdsourcing efforts or internal efforts for which data is available. Second, this paper examined sentiment gathered using Python NLTK. An alternative approach would be to extend the paper to include additional sentiment measurement sources. Third, this paper captured statistics, such as number of words in both ideas and comments. In addition, other related statistics. such as number of characters, was found to be highly correlated with such variables as number of votes. Fourth, this discussion has ignored the opportunity for manipulation of the voting. In particular, since there is system visibility, participants could contact each other and arrange for inappropriate commenting or voting outside the structure of the system. Fifth, these results could be extended to further examine different subsets of the data. For example, future research might examine the factors associated with those ideas where there were no comments or those

## Table 4

Summary of primary results.

1Number of votes is positively and statistically significantly correlated with number of comments, number of words in idea, number of words in comments and idea positive sentiment.

2 Only one of top 44 vote getting ideas did not have a comment, but 7 of remaining 27 did not have a comment, a statistically significant difference.

3 Proportion of votes for ideas that had no comments is statistically significantly different than proportion that had comments.

4 Proportion of ideas with positive comment sentiment ≥ .6 had statistically significantly more votes than those with positive comment sentiment < .6

5 Number of comments was statistically significantly related to number of votes (regression)

6 Number of words in comments was statistically significantly related to number of votes (regression)

7 Number of words in idea was statistically significantly related to number of votes (regression)

8 Interaction of idea sentiment positive and comment sentiment positive was statistically significantly related to number of votes (regression)

where the idea did not have positive sentiment and the comments did not have positive sentiment.

## Acknowledgments

The author would like to thank the two anonymous referees for their substantial comments on two earlier versions of this paper. An earlier version of this paper was presented at Rutgers University in November 2015. The author would like to thank the participants for their comments on that version of the paper.

## References

[1] B.P. Bailey, E. Horvitz, What's your idea?: A case study of a grassroots innovation pipeline within a large software company, Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, ACM 2010 pp. 2065–2074

[2] O. Bjelland, R. Wood, An inside view of IBM's innovation jam, Sloan Management Review 50 (1) (Fall 2008) 32–40

[3] T. Ding, V. Fang, D. Zuo, Stock market prediction based on time series data and market sentiment, http://murphy.wot.eecs.northwestern.edu/\~pzu918/EECS349/final\_ dZuo tDing yFang,pdf2013.

[4] J. Fuller, K. Moslein, K. Hutter, J. Haller, Evaluation games: how to make the crowd your jury, Füller, GI Jahrestagung, 1, 2010.

[5] P. Gangi, M. Wasko, Steal my idea! Organizational adoption of user innovations from a user innovation community: a case study of Dell IdeaStorm, Decision Support Systems 48 (2009) 303–312.

[6] M. Geraci, Crowdsourcing: leveraging your social networks, Interface: The Journal of Education, Community and Values 9 (6/26/2014).

[7] N. Halevy, E. Chou, K. Murnighan, Mind games: the mental representation of conflict, Journal of Personality and Social Psychology 102 (1) (2012) 132–148.

[8] M. Helander, R. Lawrence, Y. Liu, C. Perlich, C. Reddy, S. Rosset, Looking for great ideas: analyzing the innovation jam, Proceedings of the 9th WebKDD and 1st SNA-KDD 2007 Workshop on Web Mining and Social Network Analysis, ACM 2007, pp. 66–73.

[9] M. Hossain, K. Islam, Ideation through online open innovation platform: Dell IdeaStorm, Journal of the Knowledge EconomySpringer, 2015.

[10] J. Howe, The Rise of Crowdsourcing, Wired, 2006 (http://archive.wired.com/wired/ archive/14.06/crowds.html

[11] A. Kahn, B. Baharudin, K. Khan, Sentence based sentiment analysis from online consumer reviews Proceedings of the 8th International Conference on Frontiers of Information Technology, 2010

[12] N. Li, D.D. Wu, Using text mining and sentiment analysis for online forums hotspot detection and forecast, Decision Support Systems 48 (2) (2010) 354–368.

[13] P. Nixon, H. Johansson, Transparency through technology: the Internet and political parties, Digital Democracy: Discourse and Decision Making in the Information Age, 135, 2005.

[14] D.E. O'Leary, Blog mining-review and extensions: “from each according to his opinjon" Decision Support Systems 51 (4) (2011) 821–830

[15] D. O'Leary, Driving innovation and knowledge management using crowdsourcing, International Conference on Information Systems, Milano, Italy, 2013.

[16] N. Oliveira, P. Cortez, N. Areal, Stock market sentiment lexicon acquisition using microblogging data and statistical measures, Decision Support Systems 85 (2016) 62–73.

[17] D. Rowney, J. Draker, PwC announces winners of ‘crowdsourcing’ competition to define Canada's future role in the digital economy, http://www.newswire.ca/en story/583803/pwc-announces-winners-of-crowdsourcing-competition-to-definecanada-s-future-role-in-the-digital-economyMay 13, 2010.

[18] M. Salehan, D.J. Kim, Predicting the performance of online consumer reviews: a sentiment mining approach to big data analytics, Decision Support Systems 81 (2016) 30–40.

[19] J. Surowiecki, The Wisdom of Crowds, Anchor, 2005.

[20] R. Ullah, N. Amblee, W. Kim, H. Lee, From valence to emotions: exploring the distribution of emotions in online product reviews, Decision Support Systems 81 (2016) 41–53.

Daniel O'Leary is a Professor in the Marshall School of Business at the University of Southern California, focusing on prediction markets, crowdsourcing, innovations and social media. Dan received his Ph.D. from Case Western Reserve University. He is the former editor of IEEE Intelligent Systems and current editor of John Wiley's Intelligent Systems in Accounting, Finance and Management. His book, Enterprise Resource Planning Systems, published by Cambridge University Press, has been translated into both Chinese and Russian. Much of Professor O'Leary's research has studied emerging technologies and their use in business settings.
