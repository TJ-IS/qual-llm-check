---
otero_id: 19956
otero_key: "3C5DZS8W"
title: "Exploring the spoiler effect in the digital age: Evidence from the movie industry"
authors: "Yang Li; Xin (Robert) Luo; Kai Li; Xiaobo Xu"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2022.113755"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Exploring the spoiler effect in the digital age: Evidence from the movie industry

![](/api/attachments/3C5DZS8W/fulltext/images/35c6e756efea238695f0d665efaa9d3fea870c680c3866810baebd0fbda8c7c8.jpg)

Yang Li <sup>a</sup>, Xin (Robert) Luo <sup>b</sup>, Kai ${ \mathrm { L i } ^ { \mathrm { c } , \mathrm { * } } }$ , Xiaobo Xu <sup>d</sup>

<sup>a</sup> Business School, Shandong Normal University, China

<sup>b</sup> Anderson School of Management, The University of New Mexico, USA

<sup>c</sup> Business School, Nankai University, China

<sup>d</sup> International Business School Suzhou, Xi’an Jiaotong-Liverpool University, China

## A R T I C L E I N F O

Keywords: Spoilers eWOM Movie reviews Box office revenue Narrative

## A B S T R A C T

For narrative products such as movies, books, and TV shows, electronic word of mouth (eWOM) can be a doubleedged sword. It provides consumers with useful information while potentially revealing the storyline, that is, spoiling the surprise of what will happen. Prior studies have focused on the impact of spoilers on consumers experiences through psychological experiments. However, the relationship between spoilers and narrative product sales has rarely been empirically explored. To fill this gap, the current study explores the impact of spoilers on the movie box office revenue and how this impact evolves over time. We collected 279,433 reviews of 465 films on a leading community website in China and constructed a dynamic generalized method of moments (GMM) model with instrumental variables to empirically examine the spoiler effect in the movie market. Our findings indicate that spoilers have a negative influence on the movie box office revenue. However, this impact is limited to the first 6 days after the movie is released. We also discover that spoilers have a stronger negative effect on narrative-based movies than non-narrative-based movies. Furthermore, eWOM volume and eWOM variance negatively moderate the spoiler effect on the box office revenue, but the moderating effect of eWOM valence is not significant. These findings can deepen movie industry decision makers’ and platform providers understanding of spoilers, helping them devise more feasible eWOM operation strategies.

## 1. Introduction

In recent years, the paradigm of electronic word of mouth (eWOM) has gained increased momentum as organizations continue to leverage information technologies within a myriad of industries and markets. Because eWOM is defined as the positive or negative statements made by potential, actual, and former customers about a product or company via the internet [28], this form of online feedback has been shown to have a substantial impact on product sales in a plethora of markets [3,10,13]. The movie industry, for example, is a huge business around the world, with a global box office revenue of \$42.5 billion in 2019. Much like books and TV shows, movies rely heavily on the narrative of stories [57]. Consumers can find relevant information for their movie-going decisions by browsing eWOM on a particular film. Meanwhile, they may also come across spoilers because eWOM is also likely to contain information about the film’s plot.

In essence, spoilers are information that reveals the key plot of a movie before it is released to the public [7]. According to data from IMDb, spoilers appear in approximately 31% of all movie reviews, implying that spoilers are widespread and that consumers are likely to be exposed to spoilers while browsing online movie reviews. Movie re view platforms such as IMDb and Douban feature spoiler warning labels after the titles of reviews that may reveal narrative details (as shown in Fig. 1). This design allows consumers to choose whether to view those spoilers. However, spoiler warning labels divide movie reviews into two categories: spoiled and unspoiled reviews. When consumers read movie reviews, these warning labels will make them aware of the presence of spoilers, and this perception may influence their movie-going decisions [14,51].

In practice, performance is the primary concern of motion picture production and distribution companies. For the movie market, the determining factor for a movie’s success is box office revenue. However, previous research on the spoilers effect has primarily focused on the relationship between spoilers and the enjoyment experienced by consumers [19,35,37,42], with the relationship between spoilers and the movie box office revenue receiving scant attention [53]. Moreover, in the age of social media, consumers can access a variety of online in formation such as movie information, eWOM information, and spoilers. There may be interactions between the influence of different informa tion on consumer decision-making. However, previous research has overlooked these interactions and focused solely on the effect of online information [30]. Therefore, more research is warranted to explore the spoiler effect and its interaction with other online information in the movie industry.

Ryoo et al. [51] presented the first empirical study on the relation ship between spoiler reviews and the box office revenue of movies; they proposed a spoiler intensity metric based on topic modeling to quantify the spoiler effect. Their results show that there is a significant and positive relationship between spoiler intensity and box office revenue. Moreover, uncertainty reduction is the behavioral mechanism underly ing the spoiler effect. Spoiler reviews include diagnostic information that may help reduce consumers’ perceived uncertainty before watching a movie. However, these findings cannot explain why there is still lots of people’s discomfort about spoilers [47]. Moreover, other empirical studies and online surveys have demonstrated that spoilers might have a negative effect because they undermine the surprise and suspense of the story [32]. Thus, it is key for researchers to explore whether and how spoilers in movie reviews affect consumers’ movie-going decisions. Based on the aforementioned research gaps, we propose the first research question: How do spoilers impact movie box office revenue?

Narrative is a concept similar to story, which is defined as a “rep resentation of connected events and characters that has an identifiable structure” that “contains implicit or explicit messages about the topic being addressed” [38]. Narrative exists in education, marketing, jour nalism, and many other fields, which has been proposed to impose a significant impact on economic outcomes. Shiller [53] emphasized the role of narrative in individual economic decision-making and aggregate economic phenomena; he systematically theorized it as “narrative eco nomics.” In the movie market, the role of narrative can also not be neglected. Research has shown that narrative can boost the movie’s return on investment [18]. However, for movies of different genres, the narrative may differ. For instance, suspense movies are often catego rized as narrative-based movies because they rely more on plot devel opment and twists. Action movies mainly focus on visual and audio factors, so they are often regarded as non-narrative-based movies. Given that spoilers are, to some extent, a reveal of a movie’s narrative, a movie’s reliance on narrative may help to moderate spoiler effects.

Clarifying the relationship between narrative and spoilers can further determine the theoretical boundary of spoiler effect and improve the effective management of spoilers in the movie market. Hence, we pro pose the second research question: Do spoilers have stronger impacts on the box office revenue of narrative-based movies than non-narrative-based movies?

The academic community has acknowledged eWOM as a major in fluence on product sales. The metrics most research considers are eWOM volume, eWOM valence, and eWOM variance [43,59]. In the movie market, movies have varying amounts of eWOM volume, valence, and variance, signifying that these levels may fluctuate depending on the three aspects of eWOM. In actuality, different levels of eWOM volume, valence, or variance may lead to differing attitudes toward movies when consumers read movie reviews. A movie with relatively high valence can be easily seen as well made. In contrast, a movie with a relatively low valence is often considered “rotten tomatoes.” The impact of spoilers on consumers’ movie-going decisions can vary with their different initial attitudes. For instance, Ryoo et al. found that the average user ratings can be a moderator of the spoiler effect. For movies with moderate or mixed ratings, the spoiler effect becomes stronger [51]. Thus, the moderating role of eWOM volume, valence, and variance should be investigated further. However, only a few studies have considered the role of eWOM in the spoiler effect, and the eWOM metrics chosen in these studies are not exhaustive. Based on the aforementioned reasons and research gaps, we put forward the third research question: Do spoilers have different impacts on the box office revenue of movies under different eWOM volume, valence, and variance?

To advance this line of research, we collected a data set of 279,433 online reviews for 465 movies released between 2015 and 2017 on Douban Movies (http://www.douban.com). Similar to IMDb, Douban Movies is the largest movie review platform in China. Using the daily box office revenue data collected from Endata (https://ys.endata.cn/ BoxOffice/Movie). we constructed a dynamic generalized method of moments (GMM) model with instrumental variables to explore the impact of spoilers on the movie market. Contrary to Ryoo et al.’s research, we find that spoilers are negatively associated with movie box office revenue. We also find that spoilers have a stronger negative effect on narrative-based movies than non-narrative-based movies. In addi tion, we further investigate whether spoilers can impose different im pacts under various eWOM volume, eWOM valence, and eWOM variance levels. The results indicate that eWOM volume and eWOM variance negatively moderate the spoiler effect on the box office reve nue, but the moderating effect of eWOM valence is not significant. The empirical findings contribute to the literature by providing a compre hensive understanding of the spoiler effect.

![](/api/attachments/3C5DZS8W/fulltext/images/c75679ada38d872153c8d47d873b84d01ceaac5042d41e76e28de8745c1fd293.jpg)  
Fig. 1. Spoiler warning feature on IMDb and Douban.

The current study makes two important contributions. First, although the spoiler effect on the movie box office revenue has been tested empirically [51], we demonstrate that it can also be negative rather than positive. We further show that this negative spoiler effect is significant in the early periods of a movie’s life cycle. This finding highlights the dark side of eWOM in the movie market because the findings provide further insights into the spoiler effect. Second, to the best of our knowledge, the present study is the first to empirically test the moderating effects of narrative and eWOM. The analysis of these moderating effects can help bridge the gap between contradictory empirical results, providing a better and holistic understanding of the spoiler effect for academics and industry.

The rest of the current paper is organized as follows: First, we present the theoretical background and hypothesis development. Next, we describe the research methodology and empirical analysis results of our study. Finally, we discuss our main findings, theoretical contributions, and managerial implications.

## 2. Theoretical background

## 2.1. Intuitive prediction and focusing illusion

Before consumers make purchase decisions, that is, in the prepurchase stage, pleasure stems from guessing the details of an experi ence and enjoying the emotional response of the upcoming purchase prospect [61]. Gilbert and Wilson [23] proposed that under uncertain conditions, people’s behavioral decision-making largely depends on their own predictions of the results of future events, which can help them prepare in advance and better invest resources and efforts to achieve the goals. Kahneman and Tversky [35] divided people’s pre dictions into categories: inside view and outside view. In the inside view, predictions are based on the specific scenarios and impressions of a particular case. In the outside view, the case at hand is treated as an instance of a broader class of similar cases, for which the frequencies of outcomes are known or can be estimated. In general, inside view pre diction relies on the characteristic information of the object itself, while outside view prediction relies on the overall information, which is similar to the predicted object. For example, when predicting the box office of a movie, the predictions based on the cast, genre, plot, and other information can be an inside view; the prediction based on some statistical information about the box office of similar movies and con sumer review information can be an outside view.

People may not be very good at predicting their future enjoyment; they tend to overestimate how an event will affect their feelings. Wilson and Gilbert [60] defined this phenomenon as impact bias. Numerous studies have found that focusing illusion is one of the main causes of impact bias. When a judgment about an entire object or category is made with attention focused on a subset of that category, a focusing illusion is likely to occur, whereby the focused subset is overweighted relative to the unfocused one [52]. For instance, people may overestimate the happiness of having a baby by focusing on rare but meaningful events (such as a newborn’s first smile) and ignoring smaller but frequent events (such as changing dirty diapers or getting up frequently in the night). In the movie-going decisions, consumers are faced with various types of information. When a certain type of information arouses con sumers’ attention, the focusing illusion may occur.

## 2.2. Spoiler effect

The emergence of social media has enabled consumers to commu nicate and interact more conveniently with one another. However, in the process of communication, information sources may intentionally or unintentionally reveal the key plot of a story [31]. Spoilers have become a common phenomenon in narrative product consumption, and they have piqued mounting attention in the fields of psychology and communication. Conflicting studies and results on whether spoilers actually enhance enjoyment have emerged [19]. Some works have suggested that spoilers have a positive impact on consumers’ enjoyment of narrative products, with information processing fluency mediating this relationship [40,41,31]. Spoilers can make the story easier to read and comprehend, hence resulting in increased enjoyment. In addition, spoilers have been found to increase enjoyment and decrease parasocial breakup distress after a TV series finale, with mental model resonance mediating this relationship [15]. In contrast, some studies have sug gested that spoilers undermine consumers’ enjoyment. Stories that have not been spoiled are more interesting because spoilers can reduce the uncertainty and suspense of the story [23]. The timing of when to spoil a plot is also important. When spoilers appear at the beginning of the story rather than in the middle, the negative impact of spoilers on consumers enjoyment becomes significant [42]. In addition, the research context is another important factor. Daniel and Katz [14] found no positive or negative spoiler effect on the enjoyment of short stories; however, spoilers hurt viewers’ enjoyment of full-length television episodes. Johnson and Rosenbaum [33] found that in the film context, spoilers can increase respondents’ state reactance rather than their expected enjoy ment. Here, state reactance refers to the feelings people experience when they believe they have lost certain freedoms and are subsequently motivated to regain those lost freedoms [48].

Some studies have attributed the paradox of the spoiler effect to individual factors, such as personality traits [43,49], construal levels [62], and involvement [33]. Individuals with a low need for cognition (NFC) enjoy spoiled stories, whereas individuals with a high need for effect (NFA) prefer unspoiled stories [43]. People tend to overestimate the impact of spoilers in the future, and this overestimation disappears when participants have chronic or situationally primed low (vs. high) construal levels [62].

## 2.3. Narrative

Narratives usually deliver information in the form of stories and can include vivid imagery and concrete details. Non-narratives communi cate through facts, explanations, and/or arguments and tend to be more abstract [20]. Previous studies have shown that narrative messages are more effective than non-narrative messages; they are more likely to capture and hold the audience’s attention, generate positive emotional responses, and produce fewer negative thoughts [21,36]. Narratives are powerful because of their ability to give concrete form to relatively abstract ideas by including a tangible context. This concreteness evokes greater credibility in the events/situations depicted in the narrative, prompting the viewer’s connection to the narrative [8]. In addition, narrative communication can reduce viewers’ resistance to persuasive messages because viewers are less likely to regard incoming messages as having a manipulative intent [20].

At the aggregation level, irrelevant events with narrative potential can affect economic or political outcomes [53]. At the individual level, narrative leads to the activation of affective, cognitive, and belief changes in story receivers; this can eventually affect their attitudes, in tentions, and behaviors [58]. The underlving mechanism of narrative persuasion is narrative transportation, which refers to the engrossing, transformational experience of being swept away by a story [26]. Van laer et al. [58] proposed that narrative transportation has three features: receiving and interpreting, empathy and mental imagery, and losing track of reality in a physiological sense. To some extent that the success of a movie depends on the narrative, Eliashberg et al. [18] proposed a new approach for forecasting a movie’s return on investment based only on the textual information available in movie scripts; the results showed narrative contributes to the movie’s return on investment.

## 2.4. Electronic word of mouth

Assessing eWOM’s impact on product sales has garnered a great amount of scholarly interest. The metrics most research considers are eWOM volume, eWOM valence, and eWOM variance [11]. There is disagreement, though, about which particular metrics of eWOM are the most effective at driving sales. EWOM volume represents the overall amount of eWOM interaction [10]. Most researchers believe that eWOM volume contributes to product sales and have conducted empirical tests [43,50]. Duan et al. [17] proposed that eWOM volume can create an awareness effect because it can reflect the popularity of products in the market and raise potential consumers’ awareness by conveying the ex istence of the product to them. However, some researchers have claimed that eWOM valence affects product sales [5,25]. EWOM valence refers to the emotional tendencies consumers display toward their purchased products, which can be positive, negative, or neutral [15]. Researchers have considered eWOM valence to be a persuasive effect; it demon strates how a product’s reputation and quality may form, reinforce, or alter potential consumers’ preferences for the product [37]. The het erogeneity in consumer opinions can be captured by eWOM variance. Low variance indicates that consumers can reach a consensus on product evaluation, while high variance signifies that the product is a niche that some people enjoy and others despise [55,59]. The impact of eWOM variance is complicated and understudied because the existing empirical findings are less consistent. Zhu and Zhang [66] found that high vari ance imposes a negative impact on sales when the product is not pop ular. On the contrary, Sun [55] found that high variance has a positive impact when the valence of user reviews is negative.

The movie industry is a very unique context for eWOM research. The movie diffusion pattern is typically characterized by a peak in box office revenue at the initial stage of the movie release, which is followed by a pattern of exponential decay over time [29]. The eWOM effect in the movie industry is expected to be dynamic rather than static in movie life cycles [54]. Indeed, prior research has examined the dynamic impact of providing a week-by-week breakdown in their analysis [43]. However, the research results have been inconsistent, and there is a lack of coherent theory considering why eWOM may differ in its impact across time [30]. In addition, movie eWOM can be divided into two categories according to the producer: consumer word of mouth and critics word of mouth. Peng et al. [46] found that consumer word of mouth was more persuasive than critic word of mouth.

## 3. Hypothesis development

## 3.1. Spoiler and movie box office revenue

People’s behavioral decision-making greatly depends on their own predictions for the outcomes of future events, which always present with great uncertainty [23]. Ryoo et al. [51] noted that exposure to spoilers helps reduce uncertainty, which has a positive impact on decision making. However, when considering the affective valence of a predicted event, this may be different. For consumers, going to the cinema to see a movie is expected to be a positive experience. The uncertainty following a positive event can prolong the pleasure it causes, whereas cognitive efforts to make sense of a positive event can reduce the pleasure people can obtain from it [16]. Moreover, the suspense and uncertainty of narration have been proven to be the most important factors in arousing pleasure [67]. When exposed to spoilers, the suspense and uncertainty of narration are undermined, and the pleasure of future experiences is reduced accordingly. In the movie industry, as the intensity of spoiler increases, the possibility of uncertainty and suspense can be shattered. Consumers will also be less willing to watch movies. Therefore, we hy pothesize the following:

H1. The spoilers in movie reviews negatively influence box office revenue.

## 3.2. Spoilers and narratives

Movies generally belong to one or more genres; some genres rely heavily on narrative development, while others do not. For example, for a comedy movie, the punchline is very important, while the generation of a punchline often depends on the narrative and context of the story. Therefore, comedy can be seen as narrative-based movies. For action movies, visual and audio factors, such as motion graphics and special effects, become more important than plot factors. Thus, action movies can be seen as non-narrative-based movies. According to intuition pre diction theory, as a critical attribute of movies, narrative can be classi fied as inside view information. Buehler and McFarland [9] argued that consumers with an inside view are more likely to be influenced by focusing illusion because their attention is focused on the event itself rather than on any external information related to the event. Therefore, we argue that when consumers predict future experiences based on in side view information, spoilers are likely to induce focusing illusion, which makes consumers pay more attention to the negative effect of plot destruction and underweight the information that has nothing to do with the movie plot. Based on previous works, we propose the following hypothesis:

H2. Spoilers have a stronger negative effect on narrative-based movies than on non-narrative-based movies.

## 3.3. Spoilers and eWOM volume

Apart from inside view information, consumers may also seek eWOM information on movie review sites. This type of information is inde pendent of the movie itself, which can be defined as outside view in formation. In the movie market, each movie may have a different level of eWOM volume, valence, and variance, and the impact of spoilers may vary under different conditions. A high eWOM volume delivers popular signals to consumers. This can increase their attention and lead to the bandwagon effect, which will ultimately positively affect the box office revenue [12]. It should be noted that the bandwagon effect is the result of focusing illusion, here manifested as blindly following the choices of the majority and ignoring other influencing factors. However, as eWOM volume decreases, the influence of outside view information gradually diminishes. As a result, the negative spoiler effect could dominate when a movie has a relatively low eWOM volume. Thus, we hypothesize the following:

H3a. EWOM volume negatively moderates the spoiler effect.

## 3.4. Spoilers and eWOM valence

Valence represents the customers’ attitudes toward the product, which is usually measured by the average rating value [27]. The average rating can affect consumers’ perceptions of product quality [22]. Spe cifically, movies with relatively high valence can be easily seen as well made. In contrast, those with relatively low valence are often considered as bad movies. Bar-Anan et al. [4] proposed the uncertainty intensifi cation hypothesis, whereby uncertainty makes unpleasant events more unpleasant and pleasant events more pleasant. For the audience, watching a movie with a relatively high valence is a pleasant event. Spoilers reduce the uncertainty of the movie, which reduces the pleasure audiences feel. Conversely, watching a movie with a relatively low valence is an unpleasant event. Although spoilers reduce the uncertainty of the movie. the displeasure the audience feels may be mitigated. Therefore, we propose the following hypothesis:

H3b. EWOM valence positively moderates the spoiler effect.

## 3.5. Spoilers and eWOM variance

Variance reveals the information consistency of consumer opinions about a product. High variance means that consumers cannot reach a consensus, which may enhance consumers’ perceptions of uncertainty and risk [63]. Although we contend that uncertainty can help stimulate consumers’ willingness to watch movies, there are undoubtedly boundary conditions on the pleasure of the uncertainty effect. Prior research has found that moderate levels of novelty and curiosity can be pleasurable, but not levels that are too low or too high [60]. To avoid uncertainty, consumers are more likely to pay more attention to narra tive evaluations than to numerical or pictorial information, such as re view volumes and ratings [59]. Under these circumstances, the role of spoilers is more reflected in uncertainty reduction rather than plot destruction. We conjecture that the negative spoiler effect may have a stronger influence on low-variance movies than high-variance movies. Building on this, we hypothesize the following:

H3c. EWOM variance negatively moderates the spoiler effect.

## 4. Research methodology

## 4.1. Data collection

To test and validate the hypotheses, we first collected movie-related information and movie box office revenue data from Endata. Endata is the first and most authoritative real-time movie box office database website in China, offering local movie showtimes, movie news, and box office data. Endata provided us with cast lists, genres, release dates, and daily box office revenue for the movies. We conducted our data collec tion program continuously from January 2015 to December 2017. From this list, we obtained 626 movies with daily box office revenue data available on Endata. To avoid cultural and audience characteristics in fluence, we eliminated foreign-made and animated kids movies. To ensure the sufficiency of the data, we excluded movies with insufficient eWOM information and screening dates shorter than 7 days. Finally, we obtained 465 movies as our study sample.

The eWOM data in our study were collected from Douban.com. Douban.com is one of the largest interest-oriented communities dedi cated to books, music, and movies. Users can read and write movie re views, create their favorite movie lists, and purchase movie tickets at Douban Movies. Most importantly, Douban Movies provides a spoiler warning mechanism that allows us to distinguish between spoiled and unspoiled reviews. We crawled eWOM data, including the ratings, the presence of spoiler warning labels, and the timestamp of each movie review during the movie’s release period.

## 4.2. Measurement and descriptive statistics

## 4.2.1. Dependent variable

The dependent variable is BoxOffice. We collected the daily box of fice revenue information for 465 movies from Endata. Then, we sorted the preceding data set and obtained 7825 records on the 465 movies. For each movie, we tracked the daily box office revenue for at least seven days.

## 4.2.2. Independent variable

The independent variable of our study is Spoilers. We aggregated eWOM data to the movie-day (i,t) level and calculated the proportion of spoilers to the total daily eWOM volume to measure spoilers. We used this proportion rather than the number of spoilers because spoilers are discretely distributed in the total eWOM. When consumers read movie reviews, they are more likely to generate awareness of the proportion of spoilers than of the number of spoilers.

## 4.2.3. Moderating variables

The moderating variables of this study include narrative, eWOM volume, eWOM valence, and eWOM variance. According to data from Statista, we selected the top five grossing movie genres from 1995 to

2019, including adventure, action, drama, comedy, and suspense. Then, we categorized movies according to whether they are highly dependent on narrative or not. We classified movies with comedy, drama, and suspense movies as narrative-based movies, while the rest of the movies were classified as non-narrative-based movies. Then, we created a dummy variable for narrative and set it to 1 if a movie belongs to narrative-based movies, and 0 otherwise. After aggregating eWOM data to the movie day level, eWOM volume was measured as the cumulative number of reviews; eWOM valence was measured as the mean of all users’ overall ratings; eWOM variance was measured as the variance in the overall ratings.

## 4.2.4. Control variable

To acquire a valid estimate of spoilers in the movie market, some movie-based features should be considered control variables. First, movie screens are a scarce resource; movie distributors have faced limited screen availability for their movies, yet they must manage screens very effectively to maintain and improve profitability. Studies have found a positive correlation between movie screen distribution and box office revenue [39,56]. Second, we used the holiday dummy vari ables to control for the influence of release dates, which equaled 1 if the screening day of the movie coincided with one of five major holidays in China (New Year, Spring Festival, International Labor Day, National Day, or Summer Vacation). Third, we controlled for the influence of run time using the number of days since the movie was released. Fourth, we also included indicator variables (Dayofweek) for each day of the week. Fifth, we included the box office revenue of the prior day to control for state dependence. In Table 1, we describe the variables and measures.

Table 2 summarizes the descriptive statistics of the key variables. Each movie has an average daily box office revenue of 12.91 million Renminbi (RMB), with 0.001 million RMB and 546.85 million RMB as the minimum and maximum revenues, respectively. These values indi cate that the box office revenue has great volatility, which is consistent with the characteristics of the movie market [43]. The average spoiler proportion is 0.32, indicating a certain amount of spoiler content in the movie reviews. These movies have an average of 31.47 daily reviews on Douban. with a minimum of 0 reviews and a maximum of 2335 reviews. The daily average eWOM valence is 3.51, and the eWOM variance is 0.83, which indicates that consumers generally have a good evaluation of movies. However, these values vary between different periods and movies. We plotted the average number of box office revenue, spoilers, eWOM volume, eWOM valence, and eWOM variance with respect to the number of days since the movie was released. Fig. 2 shows this plot. The dynamic trends of box office revenue have reached a peak since the opening day, followed by an exponential decline. The dynamic trends of eWOM volume and spoilers have a fast buildup and fast decay (the buildup time is from day 1 to day 3). The eWOM valence is relatively high at the later stage, decreases sharply, and eventually tends to be stable. The eWOM variance builds up in the first 3 days and decreases over time. This means that consumers’ opinions tend to be consistent at the later stage of the life cycle.

Table 1  
Variables and measures.

<table><tr><td>Variable</td><td>Meanings and measures</td></tr><tr><td colspan="2">Dependent variables</td></tr><tr><td>BoxOffice</td><td>Daily box office revenue</td></tr><tr><td colspan="2">Independent variables</td></tr><tr><td>Spoilers</td><td>Spoiler proportion in movie reviews</td></tr><tr><td colspan="2">Moderators</td></tr><tr><td>Narrative</td><td>1 = Narrative-based movie, 0 = Nonnarrative-based movie</td></tr><tr><td>Volume</td><td>Cumulative number of movie reviews</td></tr><tr><td>Valence</td><td>Average rating of movie reviews</td></tr><tr><td>Variance</td><td>Variance of movie review ratings</td></tr><tr><td colspan="2">Control variables</td></tr><tr><td>Screens</td><td>Daily number of screens during the release of the movie</td></tr><tr><td>Holiday</td><td>1 = shown on major holiday, 0 = other</td></tr><tr><td>Age</td><td>The number of days since the opening day</td></tr><tr><td>Dayofweek</td><td>Indicator variables, each day of the week</td></tr></table>

Table 2 Description statistics.

<table><tr><td>Variable</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td>BoxOffice</td><td>12.91</td><td>35.32</td><td>0.001</td><td>546.85</td></tr><tr><td>Spoilers</td><td>0.32</td><td>0.12</td><td>0</td><td>1</td></tr><tr><td>Narrative</td><td>0.74</td><td>0.44</td><td>0</td><td>1</td></tr><tr><td>Volume</td><td>31.47</td><td>105.7559</td><td>0</td><td>2335</td></tr><tr><td>Valence</td><td>3.51</td><td>0.86</td><td>1</td><td>5</td></tr><tr><td>Variance</td><td>0.83</td><td>0.93</td><td>0</td><td>8</td></tr></table>

## 4.3. Model specification

To estimate the spoiler effect in the movie market, we constructed the following econometric model:

$$
\begin{array}{r l} \ln \text {Boxoffice} _ {\mathrm{i}, \mathrm{t}} & = \beta_ {0} + \beta_ {1} \ln \text {Boxoffice} _ {\mathrm{i}, \mathrm{t} - 1} + \beta_ {2} \ln \text {Spoilers} _ {\mathrm{i}, \mathrm{t} - 1} + \beta_ {3} \ln \text {Volume} _ {\mathrm{i}, \mathrm{t} - 1} \\ & + \beta_ {4} \ln \text {Valence} _ {\mathrm{i}, \mathrm{t} - 1} + \beta_ {5} \ln \text {Variance} _ {\mathrm{i}, \mathrm{t} - 1} \end{array}
$$

$$
+ \beta_ {6} \ln \text { Screens } _ {\mathrm{i}, \mathrm{t}} + \beta_ {7} \ln \text { Age } _ {\mathrm{i}, \mathrm{t}} + \beta_ {8} \text { Dayofweek } _ {\mathrm{i}, \mathrm{t}} + \omega_ {\mathrm{i}, \mathrm{t}} + \varepsilon_ {\mathrm{i}, \mathrm{t}}.\tag{1}
$$

Let here i denotes movies and t denotes the days after release. The dependent variable is lnBoxoffice<sub>i,t</sub>, which represents the logtransformed daily box office revenue of movie i on day t. We included the lagged dependent variable lnBoxoffic $\mathbf { \vec { e } i , t { - } 1 }$ on the right-hand side of Eq. (1) to capture the dynamics and avoid a positive bias, as proposed by You et al. [65]; lagged sales are likely to be correlated positively with current-period eWOM-related variables and sales. To eliminate the possibility of reverse causality, we created a time lag between the in dependent variables and box office revenue. To reduce the influence of heteroscedasticity and outliers, we used the log transformation of daily values. The variable $\mathrm { \Delta G } _ { 1 , \ 1 }$ represents a fixed effect accounting for moviespecific heterogeneities that are invariant over time, including both observed and unobserved characteristics. Finally, the variable $\varepsilon _ { \mathrm { i } , \mathrm { ~ t ~ } }$ is the idiosyncratic error term with a mean of zero. We assessed multivariate multicollinearity by examining the variance inflation factor (VIF). The mean of VIF is 1.78, and its values ranged from 1.03 to 3.57, which is lower than the threshold of 10. Thus, multicollinearity was not an issue.

In our econometric model, one methodological concern is the endogeneity problem addressed by eWOM-related research. The re lationships among eWOM volume, eWOM valence, and box office rev enue may not be completely independent and exogenous. For instance, eWOM volume can be both a cause and outcome of sales. In addition to reverse causality problems, omitting variables can also lead to endoge neity. For instance, consumers’ preferences for different movie attri butes and other individual movie-level characteristics may be correlated with eWOM valence, which might influence the movie box office reve nue. Our model includes four potentially endogenous variables: volume, valence, variance, and screens. To address this concern, we used the instrumental variables (IV) approach, which is the most widely used statistical method for addressing endogeneity [44]. Instruments need to be correlated with the suspected endogenous variable but not with the error term, as in Eq. (1), $\varepsilon _ { \mathrm { i } , \ \mathrm { t \cdot } }$ Chintagunta et al. [12] argued that competitor movies (movies belonging to the same genre and that are screened at the same time) can provide a good set of IVs. The reason for this is that these movies are likely to be provided by online reviewers with similar underlying specific unobserved variables, such as taste.

Given the similarity of online contributors, the measures on competitor movies such as eWOM volume, eWOM valence, and eWOM variance are likely to be correlated with those of the focal movie. However, these instruments are not likely to be correlated with the box office revenue of the focal movie. In addition, many empirical studies have used lagged levels of endogenous variables as instruments. Therefore, we leveraged the longitudinal aspect of our data set to obtain additional instruments that can help identify the endogenous variables. To correct for potential endogeneity bias, we tested each potentially endogenous variable individually using the Durbin–Wu–Hausman test. Durbin–Wu–Hausman tests of endogeneity show that the null hypothesi of exogeneity can be rejected in each case (all with $p < 0 . 0 5 )$ . Thus, endogeneity problems do exist in our model.

![](/api/attachments/3C5DZS8W/fulltext/images/402281879132f4e0ebed154319ed0769215986d2a8eddb46afc0c203cf577485.jpg)

![](/api/attachments/3C5DZS8W/fulltext/images/f592a60043b88e1b162bb00588f380d2e964705f4e7eedb60a8d9845147e61a4.jpg)

![](/api/attachments/3C5DZS8W/fulltext/images/ff3f79e802364214fc49be21f84af3f64fb25748a746c59b652404f2a99a06f5.jpg)

![](/api/attachments/3C5DZS8W/fulltext/images/4cb95dc94bbc45e14861155045e54531948040aeb214ccca1d3be8293a733735.jpg)

![](/api/attachments/3C5DZS8W/fulltext/images/2b4a64acb68aa805b1ee0b555ab674f7cd10b8726e6096457870c77e19acf9d8.jpg)  
Fig. 2. The average numbers of box office revenue, spoilers, eWOM volume, eWOM Valence, and eWOM variance with respect to the number of days since movie release.

Then, we needed estimator selection for instrumental variable regression. Lu et al. [44] compared the GMM and two stage least squares (2SLS); these two estimators are the most commonly used in prior research [16]. Here, GMM will be more efficient if errors are considered to have arbitrary heteroscedasticity or intra-cluster correlation for an overidentified equation. Furthermore, the GMM estimator can also be used to generate standard errors that are robust to autocorrelation (in time series or long panel data) in the data. We used a two-step dynamic GMM to run the econometric panel data estimation developed by Are llano/Blundell Bond [2,6]. To ensure that our estimation and in struments were valid, we checked the validity of over-identifying restrictions and second-order autocorrelation with the Arellano-Bond test for AR (2). The results cannot reject the null hypothesis that there is no second-order serial correlation in errors $( p = 0 . 6 2 9 )$ . Therefore, there is no serial correlation concern in the GMM estimation. We also conducted a Hansen J test to check the validity of the instruments. The Hansen J statistics $( p = 0 . 1 9 0 )$ cannot reject the null hypothesis that the instruments are uncorrelated with the error terms, indicating that the instruments used in the GMM estimation are valid.

## 5. Key empirical findings

First, we examined the impact of spoilers on the movie box office revenue. We report the results of the GMM estimation with IVs in Table 3, Column 1, which shows a significant and negative effect of spoilers on the movie box office revenue (− 0.043, p < 0.01), thus sup porting H1. This conclusion is contrary to Ryoo et al.’s study, which may be related to discrepancies in the data sources. Unlike IMDb, Douban categorizes movie reviews into two types: short comments and long reviews. Long reviews are more than 140 characters, whereas short comments are less than 140 characters. The content of the shortest comments is simple and arbitrary, with little plot information. In addi tion, only the long reviews have spoiler warning labels. Therefore, our data is collected from long reviews. Ryoo et al. proposed two parallel mediations of spoilers on box office revenue: a positive path through uncertainty reduction and a negative path through reducing surprise. Our data set contains more abundant information that can make the negative path (surprise reduction mechanism) more significant than the positive path (uncertainty reduction mechanism).

Table 3  
Results of the main effect.

<table><tr><td></td><td>GMM with IV(1)</td><td>OLS(2)</td><td>FE(3)</td></tr><tr><td>Intercept</td><td>-3.028***(0.524)</td><td>-6.207***(0.080)</td><td>-1.919***(0.153)</td></tr><tr><td> $lnBoxoffice_{t-1}$ </td><td>0.725***(0.075)</td><td></td><td>0.371***(0.028)</td></tr><tr><td> $lnSpoiler_{t-1}$ </td><td>-0.043***(0.012)</td><td>-0.114***(0.024)</td><td>-0.032**(0.016)</td></tr><tr><td> $lnVolume_{t-1}$ </td><td>0.149***(0.034)</td><td>0.259***(0.011)</td><td>0.077***(0.018)</td></tr><tr><td> $lnValence_{t-1}$ </td><td>-0.038(0.034)</td><td>0.234***(0.030)</td><td>-0.023(0.023)</td></tr><tr><td> $lnVariance_{t-1}$ </td><td>-0.004**(0.002)</td><td>-0.004**(0.002)</td><td>-0.003*(0.002)</td></tr><tr><td> $Narrative_i$ </td><td>-0.035**(0.013)</td><td>-0.089**(0.037)</td><td>-</td></tr><tr><td> $lnScreens_t$ </td><td>0.356***(0.090)</td><td>1.117***(0.006)</td><td>0.614***(0.028)</td></tr><tr><td> $lnDay_t$ </td><td>-0.212***(0.031)</td><td>-0.268***(0.013)</td><td>-0.157***(0.028)</td></tr><tr><td> $Holiday_t$ </td><td>0.073*(0.037)</td><td>0.451***(0.020)</td><td>0.233***(0.026)</td></tr><tr><td>Day of week dummies</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Movie fixed effects</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Adjusted R-squared</td><td>-</td><td>0.920</td><td>0.942</td></tr><tr><td>Cluster-robust standard error</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Number of observations</td><td>7825</td><td></td><td></td></tr></table>

\* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01.

We also examined the impact of eWOM. The findings show a sig nificant and positive effect of eWOM volume (0.149, $p < 0 . 0 1 )$ on the movie box office revenue. The association between eWOM variance $( 0 . 0 0 4 , p < 0 . 0 5 )$ and box office revenue is significant and negative, and the impact of eWOM valence is not significant $( - 0 . 0 3 8 , p > 0 . 0 5 )$ Regarding the effects of the control variables, box office revenue is greater for movies released on a holiday and with more screenings. In addition, we also find that narrative $( - 0 . 0 3 5 , p < 0 . 0 5 )$ negatively influenced box office revenue.

To validate the robustness of our main findings, we re-estimated the main model using an ordinary least squares (OLS) regression and fixed effect (FE) model. Column 2 in Table 3 presents the results from the OLS model, and Column 3 in Table 3 demonstrates the results from the FE model with robust standard errors clustered at the movie level. In the FE model, movie genre dummies and narrative drop out because of moviespecific features do not vary over time. The estimates of the multiple models are largely consistent with our GMM model, indicating that spoilers in movie reviews negatively influence the box office revenue.

To further examine the dynamic impact of spoilers on the box office revenue, we referred to Liu [38] to conduct a spotlight analysis of the spoiler effect on different days after the movie’s release. Here, we found that the spoiler effect is the greatest on opening day $( - 0 . 1 2 7 , p < 0 . 0 1 )$ and then remains negative and significant for the next 5 days (Day 2:

− 0.123, Day 3: − 0.110, Day 4: − 0.085, Day 5: − 0.087, Day 6: − 0.060, all with $p < 0 . 0 5 )$ . During this period, the intensity of the spoiler effect generally steadily declines until it becomes statistically nonsignificant starting on the seventh day $( 0 . 1 1 1 , p > 0 . 0 5 )$ . This can be attributed to the increase in information accessibility. In the later stages of a movie’s release, consumers are able to obtain movie-related information from other channels (such as news and friends’ recommendations), which can reduce consumers’ curiosity and minimize the spoiler effect.

Next, we added the interaction term narrative to verify whether it imposes a moderating effect on the impact of spoilers. The results pre sented in Table 4, Column 1, show that the interaction term between spoilers and narrative is negative and significant $( - 0 . 0 2 1 , p < 0 . 0 5 )$ indicating that the spoiler effect on narrative-based movies is signifi cantly stronger than non-narrative-based movies. Considering that the moderating variable is a binary variable, we conducted a split sample analysis. Column 2 in Table 4 presents the results from narrative-based movies, and Column 3 in Table 4 presents the results from nonnarrative-based movies. The results show that the spoiler effect is sig nificant and negative on narrative-based movies $( - 0 . 0 5 7 , p < 0 . 0 1 )$ . For non-narrative-based movies, the spoiler effect is not significant (− 0.044, $p > 0 . 0 5 )$ . Therefore, the above results support H2.

To examine whether the spoiler effect varies with different eWOM volume, valence, and variance, we conducted interaction terms between spoilers and these variables, adding them into the GMM model. The results are presented in Table 5. We found that the interaction between spoilers and eWOM volume is statistically significant and positive $( 0 . 0 2 8 , p < 0 . 0 1 )$ , suggesting that eWOM volume negatively moderates the impact of spoilers on the box office revenue, which supports H3a. Our empirical results once again prove the critical role of eWOM volume in the movie market: it can directly boost the movie box office revenue while also induce focusing illusion, which weakens the impact of other influencing factors such as spoilers.

Moreover, the interaction between spoilers and eWOM variance is significant and positive $( 0 . 0 1 0 , p < 0 . 0 1 ) ;$ here, eWOM variance could weaken the negative spoiler effect. Therefore, H3c is also supported. In line with Ryoo et al.’s conclusion that the spoiler effect becomes stronger for movies with moderate or mixed ratings, we argue that the level of eWOM variance may be a moderator of two parallel paths: when eWOM variance is large, to a certain extent, consumers feel a strong sense of uncertainty and risk, and the mechanism for reducing uncer tainty may emerge. This opens a plausible avenue for future research to test this mechanism using individual-level data.

Table 4  
Moderating effect of narrative.

<table><tr><td></td><td>Narrative Interaction(4)</td><td>Narrative-based Movies</td><td>Non-narrative-based Movies</td></tr><tr><td>Intercept</td><td>-3.054***(0.529)</td><td>-2.906***(0.640)</td><td>-1.298(0.843)</td></tr><tr><td> $lnBoxoffice_{t-1}$ </td><td>0.735***(0.075)</td><td>0.675***(0.087)</td><td>0.851***(0.126)</td></tr><tr><td>Narrative × Spoilers</td><td>-0.054***(0.017)</td><td></td><td></td></tr><tr><td> $lnSpoiler_{t-1}$ </td><td>-0.039***(0.012)</td><td>-0.057***(0.012)</td><td>-0.044(0.045)</td></tr><tr><td> $lnVolume_{t-1}$ </td><td>0.152***(0.041)</td><td>0.174***(0.047)</td><td>0.105**(0.033)</td></tr><tr><td> $lnValence_{t-1}$ </td><td>-0.040(0.034)</td><td>-0.015(0.046)</td><td>-0.050(0.046)</td></tr><tr><td> $lnVariance_{t-1}$ </td><td>-0.004*(0.002)</td><td>-0.006**(0.002)</td><td>0.002(0.005)</td></tr><tr><td> $Narrative_i$ </td><td>-0.021**(0.010)</td><td></td><td></td></tr><tr><td> $lnScreens_t$ </td><td>0.353***(0.091)</td><td>0.413***(0.108)</td><td>0.216***(0.046)</td></tr><tr><td> $lnDay_t$ </td><td>-0.221***(0.032)</td><td>-0.235***(0.038)</td><td>-0.181***(0.063)</td></tr><tr><td> $Holiday_t$ </td><td>0.070*(0.037)</td><td>0.119**(0.049)</td><td>-0.032(0.052)</td></tr><tr><td>Day of week dummies</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Movie fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Cluster-robust standard error</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Number of observations</td><td>7825</td><td>2606</td><td>5219</td></tr></table>

\* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01.

Spoiler effect varies based on eWOM volume, valence, and variance.

<table><tr><td></td><td>Volume Interaction(1)</td><td>Valence Interaction(2)</td><td>Variance Interaction(3)</td></tr><tr><td>Intercept</td><td>-2.450***(0.518)</td><td>-2.998***(0.528)</td><td>-2.969***(0.513)</td></tr><tr><td> $lnBoxoffice_{t-1}$ </td><td>0.720***(0.074)</td><td>0.728***(0.075)</td><td>0.735***(0.072)</td></tr><tr><td>Volume × Spoilers</td><td>0.028***(0.010)</td><td></td><td></td></tr><tr><td>Valence × Spoilers</td><td></td><td>-0.105(0.097)</td><td></td></tr><tr><td>Variance × Spoilers</td><td></td><td></td><td>0.010***(0.003)</td></tr><tr><td>Narrative × Spoilers</td><td></td><td></td><td></td></tr><tr><td> $lnSpoiler_{t-1}$ </td><td>-0.040***(0.013)</td><td>-0.040**(0.017)</td><td>-0.037***(0.012)</td></tr><tr><td> $lnVolume_{t-1}$ </td><td>0.059***(0.013)</td><td>0.150***(0.041)</td><td>0.145***(0.039)</td></tr><tr><td> $lnValence_{t-1}$ </td><td>-0.037(0.034)</td><td>-0.033(0.034)</td><td>-0.039(0.034)</td></tr><tr><td> $lnVariance_{t-1}$ </td><td>-0.004*(0.003)</td><td>-0.003(0.003)</td><td>0.004*(0.002)</td></tr><tr><td>Narrativei</td><td>-0.034**(0.013)</td><td>-0.032**(0.012)</td><td>-0.032**(0.012)</td></tr><tr><td> $lnScreens_t$ </td><td>0.363***(0.090)</td><td>0.350***(0.091)</td><td>0.345***(0.088)</td></tr><tr><td> $lnDay_t$ </td><td>-0.214***(0.031)</td><td>-0.210***(0.031)</td><td>-0.210***(0.031)</td></tr><tr><td> $Holiday_t$ </td><td>0.068*(0.028)</td><td>0.070*(0.037)</td><td>0.069*(0.036)</td></tr><tr><td>Day of week dummies</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Movie fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Cluster-robust standard error</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Number of observations 7825.  
\* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01.

However, our result indicates that eWOM valence does not have a significant moderating effect $( - 0 . 1 0 5 , p < 0 . 0 5 )$ , so H3b is not sup ported. We develop H3b based on the uncertainty intensification hy pothesis proposed by Bar-Anan et al. [4], which states that uncertainty makes unpleasant events more unpleasant and pleasant events even more pleasant. However, for the receivers of eWOM, the existence of confirmation bias may affect consumers’ future movie-going decisions. Confirmation bias here means that consumers have a tendency to perceive reviews that confirm their initial beliefs as more helpful and that this tendency is moderated by their confidence in their initial beliefs [64]. Relatively low eWOM valence can cause consumers to have a poor initial belief about the movie. Therefore, they tend to seek negative information supporting their initial beliefs. This means that confirma tion bias can reinforce the negative spoiler effect for movies with low valence.

## 6. Discussion

## 6.1. Conclusion

Although the relationship between eWOM and product sales has received some attention [11], the existence of spoilers and their effects on narrative consumption are still neglected. Based on the theory of intuitive prediction and focusing illusion, we explored the spoiler effect and its moderating factors in the movie market. In the current study, we first identified spoilers in movie reviews using spoiler warning labels on review websites. Then, we constructed a dynamic GMM model based on the online secondary data and drew several important conclusions. Overall, spoilers have a negative impact on movie box office revenue. However, this effect is only significant in the first 6 days. We also found that spoilers have a stronger negative impact on narrative-based movies than non-narrative-based movies. For the moderators of the spoiler ef fect, we found that eWOM volume and eWOM variance negatively moderate the spoiler effect on the box office revenue, but the moder ating effect of eWOM valence is not significant.

## 6.2. Theoretical contributions

Spoilers are a crucial influencing factor in narrative product sales, even though there is scant research on them in the IS paradigm. Our study contributes to theory and research in several ways. First, the existing literature has starkly focused on the impact of spoilers on con sumers’ experience enjoyment, except for Ryoo et al. [51]. Our study delved into this issue from a novel perspective and empirically confirmed the presence of the detrimental influence of spoilers on movie box office revenue. This finding appears to defy Ryoo et al.’s [51] idea that spoilers can reduce uncertainty and boost movie box office revenue. Our study sheds light on the dark side of spoilers and proposes that spoilers can lower consumer expectations for a movie and hurt the movie box office revenue. This conflicting finding enriches the theo retical understanding of the spoiler effect and points to the possible existence of moderating variables.

Second, we further explored the boundary conditions of the spoiler effect in order to reconcile the inconsistent findings in the existing literature. To the best of our knowledge, our study is one of the first to examine the moderating effects of narrative and eWOM volume, eWOM valence, and eWOM variance on the relationship between spoilers and movie box office. We first showed that narrative, as the core attribute of narrative products such as movies, books, and TV series, can be a boundary condition of the spoiler effect, which remains overlooked by previous studies. Then, we provided the first empirical evidence sug gesting that eWOM volume and eWOM variance negatively moderate the spoiler effect. Considering these two eWOM metrics are related to consumer perception uncertainty, this finding can provide theoretical explanations for the existing paradoxes.

Third, the box office revenue is directly tied to consumers’ pur chasing behavior, which can be reflected in forecasting future experi ences rather than actual experiences [1]. Therefore, behavioral economics theory is suitable to explain the spoiler effect in the movie market. Most of the existing studies are grounded on the theories of consumer behavior and communication. In a bid to extend this line of research, we ushered the theory of intuitive prediction and focusing illusion and empirically gauged and validated the applicability of this theory using secondary data. We illustrate the theory of intuitive pre diction and focusing illusion can be fruitfully used in understanding the influence of multiple types of information on consumer decisionmaking. Therefore, this study makes a considerable theoretical contri bution to consumer behavior in general and spoiler literature in particular.

## 6.3. Practical implications

The findings of our study also have significant implications for practice. First, our research can alert movie producers and marketers to the important role of spoilers in the movie market. Based on the results of the current study, we highly recommend limiting the dissemination of spoilers in the first 6 days of the movie release, especially for narrativebased movies. Spoiler warnings can be an effective method to control the spoiler effect, which can give consumers the freedom to choose whether to read the spoiled reviews or not. Review websites may reveal spoiler warning labels in different forms. In Douban Movies, the spoiler warning states, “This review may contain spoilers.” This shows the partial text content of the movie reviews. In IMDb, the spoiler warning indicates “Warning: spoilers,” and it does not show any text content of the movie reviews. If consumers want to read the content of spoiled reviews, they must click the warning labels. The latter, we believe, may have a better spoiler warning effect because it promotes or increases the investment of consumers.

Second, a highly accurate algorithm or app (such as Spoiler Foiler, which was introduced by Netflix) to detect spoilers in movie reviews must be developed. Blocking spoilers in movie reviews is a challenging chore because there are so many different words associated with spoilers. Keywords alone cannot identify such terms. Review platforms can introduce and implement a voting or reporting function to obtain feedback from customers. These features may be useful in improving the precision of spoiler detection.

Third, marketers need to have a clear understanding of different factors to develop more effective eWOM operation strategies. The results of our study indicate that at different stages of a movie’s life cycle, the influencing factors of box office revenue are not all the same. Although consumers are aware of the existence of fake reviews and online water army which refers to a group of Internet ghostwriters paid to post online comments with particular content, eWOM volume is still the most essential factor that influences box office revenue throughout the whole product life cycle. In addition, eWOM variance can have an impact on consumer uncertainty perception, which may affect consumers’ atti tudes toward spoilers. When eWOM variance is up to a certain level, the positive impact of spoilers can also emerge. Therefore, we recommend that online review platforms develop more flexible operation strategie based on the different levels of eWOM volume and variance.

## 6.4. Limitations, and future research

Our work is subject to some inevitable limitations, all of which provide promising directions for future research. First, spoiler warning labels are not a direct measure for spoilers. Thus, we cannot determine whether consumers have read the movie reviews. Spoiler warning labels can be seen as a kind of negative framing, reminding consumers that the eWOM content may contain spoilers [34.45]. This framing information may influence consumers’ understanding of information and purchasing behavior [24]. Although Johnson and Rosenbaum [33] demonstrated that the framing effect does not affect consumers’ movie-going inten tion, ruling out the negative framing effect from spoilers has remained a challenge. Second, the data in this study is at the aggregate level. We cannot capture the heterogeneity at the individual level. Moreover, the spoiler effect may vary depending on individual factors, such as NFC, NFA [32], and the construal level [62]. Future studies could explore the impact of individual factors in the selection of consumer prediction in formation and the spoiler effect. Third, Yan and Tsang [62] divided spoilers into two types: process-oriented spoilers and ending-oriented spoilers. They found that consumers tend to overestimate the impact of ending-oriented spoilers on their enjoyment and underestimate the effect of process-oriented spoilers on their actual enjoyment. The spoilers are not classified according to their substance in this study. Thus, future research could extend our study by exploring the different impacts of spoiler types on box office revenue.

## Credit author statement

The authors have equally contributed to this study.

## Acknowledgements

The authors thank the editor and reviewers for their helpful com ments and suggestions, which improved the quality of this article significantly.

This article was supported by Scientific Research Project of Liberal Arts Development Fund of Nankai University (ZB21BZ0214), the Major Program of the National Natural Science Foundation of China (72091311), the Major projects of National Social Science Foundation of China (20ZDA039), Shandong Youth Innovation Technology Program ("Youth Sicence and Technology Innovation Plan" in Universities of Shandong Province, 2020RWG001).

Prof.Kai Li works as an corresponding author.

## References

[1] Icek Ajzen, T.J. Madden, Prediction of goal-directed behavior: attitudes, intentions, and perceived behavioral control, J. Exp. Soc. Psychol. 22 (5) (1986) 453–474.

[2] M. Arellano, S. Bond, Some tests of specification for panel data: Monte Carlo evidence and an application to employment equations, Rev. Econ. Stud. 58 (2) (1991) 277–297.

[3] A. Babi´c Rosario, F. Sotgiu, K. De Valck, T.H. Bijmolt, The effect of electronic word of mouth on sales: a meta-analytic review of platform, product, and metric factors, J. Mark, Res, 53 (3) (2016) 297–318

[4] Y. Bar-Anan. T.D. Wilson. D.T. Gilbert. The feeling of uncertainty intensifies

[5] J. Berger, A.T. Sorensen, S.J. Rasmussen, Positive effects of negative publicity: when negative reviews increase sales., Mark, Sci, 29 (5) (2010) 815–827.

[6] R. Blundell, S. Bond, Initial conditions and moment restrictions in dynamic pane

[7] P. Booth, Digital Fandom: New Media Studies, Peter Lang, 2010.

[8] J.M. Brechman, S.C. Purvis, Narrative, transportation and advertising, Int. J. Advert, 34 (2) (2015) 366–381.

[9] R. Buehler, C. McFarland, Intensity bias in affective forecasting: the role of temporal focus, Personal, Soc, Psychol, Bull, 27 (11) (2001) 1480–1493

[10] J.A. Chevalier, D. Mavzlin, The effect of word of mouth on sales: online book

[11] C.M.K. Cheung, D.R. Thadani, The impact of electronic word-of-mouth communication: a literature analysis and integrative model, Decis. Support. Syst 54 (1) (2012) 461–470

[12] P.K. Chintagunta, S. Gopinath, S. Venkataraman, The effects of online user reviews on movie box office performance: accounting for sequential rollout and aggregation across local markets, Mark. Sci. 29 (5) (2010) 944–957.

[13] E.K. Clemons, G.G. Gao, L.M. Hitt, When online reviews meet hyperdifferentiation:

[14] T.A. Daniel, J.S. Katz, Spoilers affect the enjoyment of television episodes but not short stories, Psychol. Rep. 122 (5) (2019) 1794–1807.

[15] C. Dellarocas, X.M. Zhang, N.F. Awad, Exploring the value of online product reviews in forecasting sales: the case of motion pictures, J. Interact. Mark. 21 (4) (2007) 23–45.

[16], C. Ding, H.K. Cheng. Y. Duan, Y. Jin, The power of the “like" button: the impact of social media on box office, Decis, Support, Syst, 94 (2017) 77–84

[17] W. Duan. B. Gu, A.B. Whinston, Do online reviews matter?—an empirical investigation of panel data, Decis. Support. Syst. 45 (4) (2008) 1007–1016.

[18] J. Eliashberg, S.K. Hui, Z.J. Zhang, From story line to box office: a new approach for green-lighting movie scripts, Manag. Sci. 53 (6) (2007) 881–893.

[19] M.E. Ellithorpe, S.E. Brookes, I didn’t see that coming: spoilers, fan theories, and their influence on enjoyment and parasocial breakup distress during a series finale, Psychol. Pop. Media Cult. 7 (3) (2018) 250–263.

[20] J.E. Escalas, Imagine yourself in the product: mental simulation, narrative transportation, and persuasion, J. Advert. 33 (2) (2004) 37–48.

[21] J.E. Escalas, Self-referencing and persuasion: narrative transportation versus analytical elaboration, J. Consum. Res. 33 (4) (2007) 421–429.

[22] A.J. Flanagin, M.J. Metzger, R. Pure, A. Markov, E. Hartsell, Mitigating risk in ecommerce transactions: perceptions of information credibility and the role of user-generated ratings in product quality and purchase intention, Electron. Commer. Res. 14 (1) (2014) 1–23.

[23] D.T. Gilbert, T. Wilson, D. Prospection: experiencing the future, Science 317 (5843) (2007) 1351–1354.

[24] K.H. Goh, J.C. Bockstedt, The framing effects of multipart pricing on consumer purchasing behavior of customized information good bundles, Inf. Syst. Res. 24 (2) (2013) 334–351.

[25] S. Gopinath, P.K. Chintagunta, S. Venkataraman, Blogs, advertising, and localmarket movie box office performance, Manag, Sci. 59 (12) (2013) 2635–2654

[26] M.C. Green, T.C. Brock, The role of transportation in the persuasiveness of public narratives, J. Pers. Soc. Psychol. 79 (5) (2000) 701–721.

[27] B. Gu, J.H. Park, P. Konana, Research note – the impact of external word-of-mouth sources on retailer sales of high-involvement products, Inf, Syst, Res. 23 (1) (2012 182–196.

[28] T. Hennig-Thurau, K.P. Gwinner, G. Walsh, D.D. Gremler, Electronic word-ofmouth via consumer-opinion platforms: what motivates consumers to articulate themselves on the internet? J. Interact. Mark. 18 (1) (2014) 38–52.

[29] T. Hennig-Thurau, C. Wiertz, F. Feldhaus, Does Twitter matter? The impact of microblogging word of mouth on consumers’ adoption of new movies, J. Acad. Mark, Sci, 43 (3) (2015) 375–394.

[3o] J. Huang. W.E. Boh. K.H. Goh. A temporal study of the effects of online opinions: information sources matter, J. Manag. Inf. Syst. 34 (4) (2017) 1169–1202

[31] S. Jeon, S. Kim, H. Yu, Spoiler detection in TV program tweets, Inf. Sci. 329 (2016) 220–235.

[32] B.K. Johnson, J.E. Rosenbaum, Spoiler alert: consequences of narrative spoilers for dimensions of enjoyment, appreciation, and transportation, Commun. Res. 42 (8) (2015)1068–1088.

[33] B.K. Johnson, J.E. Rosenbaum, (Don’t) tell me how it ends: spoilers, enjoyment, and involvement in television and film, Media Psychol. 21 (4) (2018) 582–612.

[34] B.K. Johnson, A. Udvardi, A. Eden, J.E. Rosenbaum, Spoilers go bump in the night: Impacts of minor and major reveals on horror film enioyment. Journal of Media Psychology: Theories, Methods, and Applications 32 (1) (2020) 14.

[35] D. Kahneman. A. Tversky. On the reality of cognitive illusions. Psychol. Rey. 103 (3) (1996) 582–591.

[36] E. Kim, S. Ratneshwar, E. Thorson, Why narrative ads work: an integrated process explanation, J. Advert. 46 (2) (2017) 283–296.

[37] J. Kim, P. Gupta, Emotional expressions in online user reviews: How they influence consumers’ product evaluations, J. Bus. Res. 65 (7) (2012) 985–992. King, R. A.; Racherla. P.: and Bush. V. D. What we know and don't know about online word-ofmouth: A review and synthesis of the literature. Journal of Interactive Marketing, 28, 3(2014), 167–183

[38] M.W. Kreuter, K. Holmes, L.J. Hinyard, T. Houston, S. Woolley, M.C. Green, D. Storey, Narrative communication in cancer prevention and control: a framework to guide research and application, Ann. Behay. Med. 33 (3) (2007) 221–235.

[39] M.T. Lash. K. Zhao, Early predictions of movie success: the who, what, and when of profitability, J. Manag. Inf. Syst. 33 (3) (2016) 874–903.

[40] J.D. Leavitt, N.J.S. Christenfeld, Story spoilers don't spoil stories, Psychol. Sci. 22 (9) (2011) 1152–1154.

[41] J.D. Leavitt, N.J.S. Christenfeld, The fluency of spoilers: why giving away endings improves stories, Scientific Study of Literature 3 (1) (2013) 93–104.

[42] W.H. Levine, M. Betzner, K.S. Autry, The effect of spoilers on the enjoyment of short stories, Discourse Process. 53 (7) (2016) 513–531.

[43] Y. Liu, Word of mouth for movies: its dynamics and impact on box office revenue,

[44] G. Lu, X.D. Ding, D.X. Peng, H.H.C. Chuang, Addressing endogeneity in operations management research: recent developments, common problems, and directions for

[45] K. Mulligan, P. Habel, An experimental test of the effects of fictional framing on attitudes, Soc, Sci, O. 92 (1) (2011) 79–99

[46] L. Peng, G. Cui, C. Li, The comparative impact of critics and consumers: applying the generalisability theory to online movie ratings, Int. J. Mark. Res. 55 (3) (2013) 413-436.

[47] LG. Perks, N. McElrath-Hart, Spoiler definitions and behaviors in the post-network

[48] S.A. Rains, The nature of psychological reactance revisited: a meta-analytic review,

[49] J.E. Rosenbaum, B. Johnson, K., Who’s afraid of spoilers? Need for cognition, need for affect, and narrative selection and enioyment. Psychol. Pop. Media Cult. 5 (3) (2016) 273–289.

[50] H. Rui, Y. Liu, A. Whinston, Whose and what chatter matters? The effect of tweets

[51] J.H. Ryoo, X. Wang, S. Lu, Do spoilers really spoil? Using topic modeling to measure the effect of spoiler reviews on box office revenue, J. Mark. 58 (2) (2021) 70–88.

[52] D.A. Schkade, D. Kahneman, Does living in California make people happy? A focusing illusion in judgments of life satisfaction, Psychol. Sci. 9 (5) (1998) 340–346.

[53] R.J. Shiller, Narrative Economics, Princeton University Press, 2020

[54] T. Song, J. Huang, Y. Tan, Y. Yu, Using user-and marketer-generated content for box office revenue prediction: differences between microblogging and third-party platforms, Inf. Syst. Res. 30 (1) (2019) 191–203.

[55] M. Sun, How does the variance of product ratings matter? Manag. Sci. 58 (4) (2012) 696–707.

[56] S. Swami, J. Eliashberg, C.B. Weinberg, SilverScreener: a modeling approach to movie screens management, Mark. Sci. 18 (3) (1999) 352–372.

[57] A.S.L. Tsang, D. Yan, Reducing the spoiler effect in experiential consumption, ACR North American Advances 36 (1) (2009) 708–709.

[58] T. Van Laer, K. De Ruyter, L.M. Visconti, M. Wetzels, The extended transportation imagery model: a meta-analysis of the antecedents and consequences of consumers’ narrative transportation, Journal of ConsumerResearch 40 (5) (2014) 797-817.

[59] F. Wang, X. Liu, E.E. Fang, User reviews variance, critic reviews variance, and product sales: an exploration of customer breadth and depth effects, J. Retail. 91 (3) (2015) 372–389.

[60] T.D. Wilson, D.B. Centerbar, D.A. Kermer, D.T. Gilbert, The pleasures of uncertainty: prolonging positive moods in ways people do not anticipate, J. Pers Soc. Psychol. 88 (1) (2005) 5–21.

[61] T.D. Wilson, D.T. Gilbert, Affective forecasting: knowing what to want, Curr. Dir. Psychol. Sci. 14 (2005) 131–134.

[62] D. Yan, A.S.L. Tsang, The misforecasted spoiler effect: underlying mechanism and boundary conditions, J. Consum. Psychol. 26 (1) (2016) 81–90.

[63] L. Yan, Y. Tan, The consensus effect in online health-care communities, J. Manag. Inf. Syst. 34 (1) (2017) 11–39.

[64] D. Yin, S. Mitra, H. Zhang, Research note—when do consumers value positive vs. negative reviews? An empirical investigation of confirmation bias in online word of mouth, Inf. Syst. Res. 27 (1) (2016) 131–144.

[65] Y. You, G.G. Vadakkepatt, A.M. Joshi, A meta-analysis of electronic word-of-mouth elasticity, J. Mark. 79 (2) (2015) 19–39.

[66] F. Zhu, X. Zhang, Impact of online consumer reviews on sales: the moderating role of product and consumer characteristics, J. Mark. 74 (2) (2010) 133–148.

[67] D. Zillmann, Excitation transfer in communication-mediated aggressive behavior, J. Exp. Soc. Psychol. 7 (4) (1971) 419–434.

Yang Li is an Assistant Professor of Management Information Systems in the Business School at Shandong Normal University, China. He received his Ph.D. in Management In formation Systems from Nankai University, China. His research interests include social commerce and electronic word-of-mouth. His research has appeared at Nankai Busines Review and Soft Science.

Xin (Robert) Luo is an Endowed Black, Albert & Mary Jane Professor in Economic Development and a Full Professor of Management Information Systems and Information Assurance in the Anderson School of Management at the University of New Mexico, Albuquerque, USA. He received his Ph.D. in Management Information Systems from Mississippi State University, USA. His research will be or has been published in leading IS business journals, including the Information Systems Research, Journal of Operations Man agement, Journal of Management Information Systems, Journal of the Association for Infor mation Systems, European Journal of Information Systems, Information Systems Journal, Journal of Strategic Information Systems, Decision Sciences, Decision Support Systems, Infor mation & Management, and IEEE Transactions on Engineering Management. He has served as an ad hoc Associate Editor for MIS Quarterly and an Associate Editor for European Journal of Information Systems, and currently serves as an Associate Editor for the Journal of the As sociation for Information Systems, Decision Sciences, Information & Management, Electronic Commerce Research, and the Journal of Electronic Commerce Research. His research interests center around information assurance. innovative technologies for strategic decision: making, and global IT management. He is the Co-Editor-in-Chief for the International Journal of Accounting and Information Management.

Kai Li is a Professor of Information Systems in Business School, Nankai University, China. He received his Ph.D. in Technical Economy and Management from Nankai University, China. His research interests include online platform, online privacy, social media analytics, search engine, and business intelligence. He has published papers in journals including Decision Support Systems. Information and Management. PLOS ONE. International Journal of Production Economics and so on.

Xiaobo Xu is a Professor of Information Management and Information Systems at Xi’an Jiaotong-Liverpool University, Suzhou, China. He received his BE in Management Engi neering from Fast China University of Science and Technology and his Ph D. in Man: agement Information Systems from University of Mississippi, USA. His primary research interests include information systems project success, business model innovation, research methodologies, shared economy, e-commerce success, supply chain management, etc. Hi published articles appear in Journal of Business Research, Project Management Journal, In formation Technology & Management. Information Systems Frontiers. International Journal of Information Management, Technological Forecasting and Social Change, and Internet Research, among others.
