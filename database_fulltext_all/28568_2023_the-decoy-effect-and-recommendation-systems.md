---
otero_id: 28568
otero_key: "SHT7BCSS"
title: "The Decoy Effect and Recommendation Systems"
authors: "Nasim Mousavi; Panagiotis Adamopoulos; Jesse Bockstedt"
year: "2023"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.1197"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Decoy Effect and Recommendation Systems

Nasim Mousavi,<sup>a,</sup>\* Panagiotis Adamopoulos,<sup>a</sup> Jesse Bockstedt<sup>a</sup>

<sup>a</sup> Goizueta Business School, Emory University, Atlanta, Georgia 30322

\*Corresponding author

Contact: nasim.mousavi@emory.edu, https://orcid.org/0000-0003-0306-9209 (NM); padamop@emory.edu, https://orcid.org/0000-0002-4289-1767 (PA); bockstedt@emory.edu, https://orcid.org/0000-0002-4274-9744 (JB)

Received: November 12, 202 Revised: June 12, 2022 Accepted: December 3, 2022 Published Online in Articles in Advance: January 13, 2023

https://doi.org/10.1287/isre.2022.1197

Copyright: © 2023 INFORMS

Abstract. In this paper, we explore the decoy effect in recommendation systems. Including a decoy item in a set of alternatives can influence the attractiveness of the other items by facilitating decision making. Prior research literature has indeed shown the decoy effect to be robust in traditional choice settings, with consistent reporting of an overall positive impact. Practitioners often use decoys to help drive demand for specific items. Recommendation systems too are increasingly being used to present item choice sets to customers and users. Both recommendation systems and the decoy effect can be used as strategies to help facilitate decision making. However, previous work has not examined the decoy effect in the context of recommendations. The decoy effect may facilitate consumer decision making and positively impact user behavior when used with recommendation systems. However, in the recommendation context, customers often have different expectations for the reliability and quality of the presented information. Hence, a decoy as a recommendation could signal issues in system reliability, resulting in a negative effect. We perform a randomized, controlled laboratory experiment and use persuasion theory as the theoretical lens to demonstrate that the decoy effect works differently in the context of recommendation systems. Specifically, we show that depending on the recommendation context, the decoy effect can or cannot drive demand for target items. We find that including a decoy minimizes the demand for the target option when personalized recommendations are presented, which deviates from the traditional decoy effect. However, a decoy increases the target’s demand when nonpersonalized recommendations are shown, following the conventional decoy effect. We explore the mechanism behind these findings and show the robustness of our results by conducting multiple analyses and additional experiments. The findings of our paper have important implications for the design of recommendation systems and our understanding of consumer decision making.

History: Ravi Bapna, Senior Editor; Idris Adjerid, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.1197.

Keywords: recommendation system • personalization • decoy effect • user behavior • experimental methods

## 1. Introduction

E-commerce platforms often provide shoppers with exceedingly large product catalogs, inundating consumers with numerous choices. Studies and reports reveal significant consequences of choice overload for businesses and the need for strategies to combat this issue (Chernev et al. 2015, ChoiceHacking 2020). In fact, 54% of customers stopped purchasing a product from online retailers whose platforms make it challenging to find the desired product, and more than 70% of them switched to a competitor (Linder 2018). Product recommendation systems have been used to address this issue. These systems can assist customers in accessing the right information at the right time, enhancing their decision quality and online experience (Li and Karahanna 2015, Adomavicius et al. 2018). It has been estimated that 80% of what customers watch on Netflix and 35% of what they purchase on Amazon result from product recommendations (Evdelo 2020, Meltzer 2022). Although recommendation systems can be an effective online strategy, their current design also has limitations. One of the signifi cant issues associated with these systems is that they can provide much valuable information about too similarly attractive options (Adamopoulos and Tuzhilin 2013), leading to decision paralysis (Boag 2021). Realizing this issue, companies are in quest of strategies to mitigate this problem to provide more persuasive recommendations and offer high-quality services.

Despite the extensive research on designing such systems to achieve maximum predictive accuracy, relatively little attention has been devoted to the behavioral factors that can impact the persuasiveness of such systems and consumers’ decisions (Li and Karahanna 2015). In this paper, we focus on the recommendation set composition, an underexplored area (Xiao and Benbasat 2007), and examine how the choice overload issue in recommendation systems might be mitigated by a behavioral phenomenon discovered in choice settings: the decoy effect. Based on this effect, including an unattractive item beside an attractive one can create contrast and guide the user to clearly observe the superiority of the latter item and complete a purchase. Prior research has shown that this phenomenon can be used to simplify choice and improve customer outcomes in regular choice settings (Simonson 2014, Wu and Cosguner 2020). However, recommendation settings have unique features that might alter this effect. In this paper, we take a step forward and explore how the decoy strategy affects customer outcomes in recommendation settings, both personalized and nonpersonalized.

## 1.1. Research Motivation

Recommendation systems aim at making online shopping more pleasant for consumers by recommending items that fit their interests and reducing search costs. This objective cannot be achieved without understanding the factors that impact consumer behavior in different circumstances. For instance, it is well established, theoretically and practically, that consumers do not necessarily behave rationally to maximize their utility (Yagoda 2018), and much of their behavior could be irrational, depending on contextual factors that influence their cognition and emotion (Business Insider 2021). Factors such as the choice set composition, the presentation format of alternatives, and the relationship among options have consistently been shown to impact consumer decision making (Thomadsen et al. 2018).

However, insufficient attention has been paid to consumer psychology and behavioral issues in designing these systems (Theocharous et al. 2019). The underlying algorithms are usually formalized based on rational behavior and are focused on maximizing customers expected utility without considering the boundaries of rational behavior. As a result, these systems may not satisfy customers’ interests in certain contexts. Realizing this issue, practitioners discuss the necessity of studying and incorporating the psychology of human cognition and examining which factors could enhance the effectiveness of the systems (Theocharous et al. 2019). Among the factors influencing human behavior, the decoy effect has attracted practical attention because it has been recognized as an effective marketing strategy to drive sales and customer satisfaction in traditional choice settings (Robson 2019, Radova 2022). The decoy effect, which happens because of human cognitive bias, has primarily been argued to be beneficial in recommendation settings (Theocharous et al. 2019).

Popular product recommendation systems, such as the one incorporated by Netflix and Amazon, usually provide a set of items that are typical of high quality or highly fit consumers’ interests and needs. However, it is believed that this strategy can overwhelm customers with too many good options and create decision paralysis and over-specialization (Adamopoulos and Tuzhilin 2014a, Salazar and Moran 2019), having significant consequences such as creating content fatigue, reducing online experience quality, and making decision making more complex (Salazar and Moran 2019, ChoiceHacking 2020). When several viable alternatives are offered, consumers would have difficulty differentiating and ranking them; thus, decision making becomes frustrating. In this situation, including a decoy in a set of recommended items could facilitate decision making by creating a clear contrast among items in the collection and altering customers’ attention toward the target item (Page 2021). Despite the discussions, no industry report or research paper conclusively shows that the decoy effect can be used in the recommendation setting to facilitate consumer decision making.

Although the decoy effect might work in traditional choice settings, it might not be an effective strategy in the recommendation context because customers’ expectations of service quality can be different (Xiao and Benbasat 2007). Individuals are usually more sensitive to information quality when receiving advice and recommendations. Including a decoy in recommendations could decrease perceived quality, reducing custome satisfaction and trust. Even though there is evidence of strong and positive decoy effects (Dooley 2019, Sharma 2020) for driving demand for specific items, the unique features of recommendation systems could render decoys detrimental. In this paper, we try to address this issue and provide guidance for managers on the effectiveness of using decoys with recommendations.

## 1.2. Research Questions and Contributions

Studies have shown that providing a list of recommended items with similar utilities and attractiveness makes decision making complex for consumers, reducing the chance of purchase and decreasing customer satisfaction (Tsekouras et al. 2019). In traditional product listings, it has been shown that including a decoy in a set of items can create a clear contrast among items and make one of the items more attractive. Following these findings, scholars argue that this approach might also be useful in recommendation systems (Mathias and Dietmar 2021). However, despite the discussion, it has not been shown how consumers react to the presence of a decoy in the recommendation set. Because consumer behavior can be different in a recommendation setting, our research tries to answer the following question: “How does the decoy effect change the demand for items when used with recommendation systems?”

The answer to this question will help practitioners and recommendation designers determine whether using a decoy in a recommendation setting will generate sufficient value. Including a decoy could benefit a recommendation system as it could facilitate decision making and enhance customer satisfaction. Furthermore, it may drive demand for specific items by leveraging the standard decoy effect observed in prior literature. Alternatively, a decoy could be counterproductive due to the unique characteristics of the recommendation systems context. Notably, including a decoy in a set of recommendations may question the efficacy of such systems because customers expect to observe high-quality information aligned with their interests (Xiao and Benbasat 2007). This may result in different consumer choice behavior than is predicted by the prior literature. Both stated situations are theoretically plausible, providing a unique opportunity for empirical examination of the decoy effect in recommendation systems.

In practice, the two most common forms of recommendations used are personalized recommendations, where the system identifies items that should have high fit with a specific individual’s preferences (e.g., Netflix’s personalized movie recommendation), and nonpersonalized recommendations, where the system presents consumers with high-quality items typically chosen based on average user ratings (e.g., Amazon’s most highly rated products list). Studies show that consumers might behave differently depending on the type of recommendations presented (Adamopoulos et al. 2021, Adomavicius et al. 2021a) and their expectations and reliance on recommendations can differ based on whether they observe personalized or nonpersonalized recommendations (Xiao and Benbasat 2018, Adomavicius et al. 2021b). Hence, they might react differently toward a decoy in these two settings, and our study further aims to answer the research question: “Does the decoy effect manifest differently in a personalized recommendation setting compared to the non-personalized one?” Answering this question will guide managers on whether they need to incorporate various strategies in these two contexts.

We conducted a randomized controlled choice experiment using a state-of-the-art movie recommendation system to answer these questions. Specifically, we designed a platform to provide both personalized and nonpersonalized recommendations and tracked user behavior after encountering decoys. We compared user behavior in four conditions: personalized with a decoy, personalized without a decoy, nonpersonalized with a decoy, and nonpersonalized without a decoy. Our results indicate that, interestingly, the nature of the decoy effect changes substantially in personalized and nonpersonalized conditions. The decoy effect follows the traditional findings in the nonpersonalized setting, increasing the demand for a target item. However, in the personalized setting, the decoy effect deviates from what is expected from the traditional results. Particularly, including a decoy in a personalized recommendation set increases the selection likelihood of the no-choice option and reduces the target item’s demand. We believe that these findings are due to customers’ expectations toward the personalization systems. In this context, customers expect to see high-fit recommendations from exceptionally reliable sources and observing a decoy can negatively affect their behavior toward the system. We show the robustness of ou results through various additional experiments.

Our work also answers the call to action from scholars to explore the well-established cognitive biases in recommendation systems in a general and personalized setting (Theocharous et al. 2019, Mathias and Dietmar 2021). We contribute to the literature on personalization and recommendation systems by extending the current knowledge of the importance of contextual factors in the effectiveness of the systems. As the first study, we examine the decoy effect recommendation systems and demonstrate that it impacts customers’ behavior differently in personalized and nonpersonalized settings. The paper also broadens our understanding of the decoy effect by examining it in a unique set of recommendations. The results of our paper also respond to the practical controversy on the decoy effect in recommendation systems and provide guidance for platform providers. We specifically show that although practitioners can incorporate the decoy effect in the nonpersonalized setting, they should be more cautious about using decoys in a personalized strategy. Furthermore, our results emphasize the importance of differentiating recommendation contexts, as customers’ expectations can be dis tinct in various settings.

The paper is organized as follows. First, we provide a theoretical background on the decoy effect and contextual factors in recommendation systems, followed by our hypotheses. Afterward, we describe the research methodology and explain the empirical approach and the results. We then discuss the mechanism behind our findings and robustness checks. We conclude with a discussion of our research’s implications for designing and using personalization systems and platforms.

## 2. Literature Review

This section discusses the literature on the decoy effect and contextual factors in recommendation systems.

## 2.1. Decoy Effect

Context matters in everyday decision making and judgment (Tversky and Simonson 1993). Individuals typically make judgments on a relative basis and compare a given item to other available options (Stewart et al. 2005, Sharif and Oppenheimer 2021). For instance, the same circle could seem larger or smaller relative to other circles that are presented next to it. To illustrate, the classic example in Figure 1 shows that, although the middle circles in both pictures are equally sized, the circle surrounded by smaller circles seems bigger than the circle surrounded by bigger circles (Todorovic ´ 2010). This same relative comparison applies to consumer decision making. For instance, when selecting a restaurant, the restaurant’s quality is perceived relative to the other available restaurants (Huber et al. 1982). A restaurant can seem to be the best choice among a set of lowerquality restaurants. However, the same restaurant can seem to be low quality among a set of higher-quality restaurants.

Therefore, it is essential to consider contextual factors when analyzing consumer behavior and designing choice architecture. Choice architecture demonstrates how choices can be presented to consumers in different formats and how the different formats of choice presentations can impact consumers’ decision making (Thaler and Sunstein 2009). Nowadays, many companies use choice architecture to change their consumers’ behavior, drive demand, and increase revenue (Schneider et al. 2018, Adjerid et al. 2019, Shrupti et al. 2019). The idea behind choice architecture is that, because individuals have a limited cognitive capacity, they rely on heuristics. Hence, biases induced by the choice environment can impact their decision making (Acquisti et al. 2017, Adjerid et al. 2019).

For instance, in social psychology and consumer behavior, the presence of a decoy in a choice set has been shown to change the demand for the other items in that choice set. The effect is called the decoy or attraction effect, and interestingly, this phenomenon violates the independence of irrelevant alternatives (IIA) assumption in choice models. The IIA assumption states that the relative probability of selecting an item over another in a set of items does not change by adding a new alternative (Luce 2012). For example, in a set with two items, A and B, the selection likelihood of A relative to B should not depend on the presence or characteristics of another item. C. Huber et al. (1982) showed for the first time the existence of the decoy effect with multiple experiments using different product types, such as cars, restaurants, beers, and movies. They designed a set of options containing three items: a target, a competitor, and a decoy. The decoy item is asymmetrically dominated, which means the target item completely dominates it in all aspects. Compared with the competitor, the decoy is superior in some dimensions and inferior in others. The researchers showed that adding a decoy to a set with two items (target and competitor) changes the selection likelihood of the items in that set: the probability of choosing the target item increases at the competitor’s expense.

Figure 1. Example of Context Effect  
![](/api/attachments/SHT7BCSS/fulltext/images/e3d9fa9c55f8c8398c99d9b6a51381f0934a90aa770a71f2b26a64440476fa58.jpg)  
Source. Adapted from Todorovic ´ 2010

Figure 2. Example of the Decoy Effect  
![](/api/attachments/SHT7BCSS/fulltext/images/d5ed90f079758a45ff9d3afc07a4098f0c0c342b3e11ba967e5708ba9b881447.jpg)

For example, suppose a customer wants to buy a product with two important attributes, storage space, and processor speed (Figure 2). She initially has two options {A, B}. Option A has a higher processor speed with lower storage space, and B has a lower processor speed with higher storage space. Making a final choice between these two items can be a complex task because of the tradeoff between the two attributes. However, including item C in the set, which has a comparable processor speed to A, but lower storage space, makes A a clear superior item to C, and this comparison drives consumers’ attention toward item A.

The mechanism behind the decoy effect is based on the fact that choosing an item from a set generally involves a certain level of cognitive load for customers, which is a function of the complexity related to comparing and ranking the alternative items. When customers are offered a list of potential items to choose from, they need to compare the items across multiple dimensions and values. When there are no clear contrasts or clearly superior items, customers may engage in an exhaustive search. This process requires high cognitive resources and complicates the comparison (Chernev et al. 2015, Iyengar and Lepper 2000, Scheibehenne et al. 2010). Studies have found that including a decoy item can simplify the choice by creating clear contrasts between some items, requiring less cognitive burden, and increasing higher satisfaction and confidence (Huber et al. 1982, Simonson 1989, Simonson and Tversky 1992).

The decoy item is typically designed to be easily comparable to a target item in the set (e.g., sharing certain attributes with the target or being of the same product category) but less comparable to other competitor items (Huber et al. 1982, Simonson and Tversky 1992). This creates a clear contrast with the target item but not with the other items. As a result, the target item seems a clear winner compared with the decoy, gaining a positive weight in the evaluation (Huber et al. 1982, Simonson and Tversky 1992). However, nontarget items are not directly comparable with the decoy. Therefore, the customer will be less certain about the superiority of these items, assigning them less positive weight. Thus, the likelihood of selecting the target item increases disproportionately when a decoy is present.

Scholars have subsequently shown the robustness of the decoy effect in different contexts, including simple consumer product contexts, like purchasing orange juice and beer, and higher involvement contexts, such as apartment selection and car buying (Simonson and Tversky 1992, Ariely and Wallsten 1995, Bhargava et al. 2000, Hedgcock et al. 2009). Beyond purchasing, studies have also shown the decoy effect in other contexts, such as entertainment, policy evaluation, politics, and health (Herne 1997, Stoffel et al. 2019, Schumpe et al. 2020, Wu et al. 2020). However, all the studies were in the regular choice setting, and no study has explored this effect in a recommendation setting, in which a recommender offers a decoy. With the increasing importance of these systems in modern businesses, it is important to understand if including a decoy in a set of recommended items would also be beneficial.

## 2.2. Contextual Factors in Recommendation Systems

The decoy effect has been demonstrated in many contexts, with the Economist subscription experiment being one of the most famous examples (Ariely 2009). The author conducted an experiment to encourage subscrip tion to the magazine (Figure 3), with the options of online (\$59), print (\$125), and print and online (\$125). The result of their study showed that including the print (\$125) option as a decoy increased the demand for the option of print & online (\$125). Given the same price of the print-only and print and online, print-only is clearly inferior compared with print and online because customers pay the same amount of money for less service (clear dominance). Therefore, compared with the decoy, it seems more reasonable for consumers to select the clear superior item (print and online). However, the contrast is not that clear when comparing the print-only and online-only options because both qualities and prices are different (unclear dominance). Therefore, the print and online option may seem more attractive than the online-only option when the print-only option is present.

Since the Economist experiment, recommendation systems have increasingly become key drivers for content and product consumption. To be effective, these systems need to attract consumers’ attention and facilitate their decision-making process (Tam and Ho 2005, Li and Karahanna 2015). Thus, investigating factors that can satisfy consumers’ needs and improve their decision quality is important and practical. Although considerable research, primarily in computer science, focuses on the algorithmic design of such systems, insufficient attention has been paid to improving systems’ efficacy by focusing on behavioral factors.

Figure 3. Subscription Experiment  
![](/api/attachments/SHT7BCSS/fulltext/images/d9cd68875d489fb9e50b9eb20adc78df3887722cc1e2c38c06c9e60bf64e2b7b.jpg)  
Source. Adapted from Ariely 2009.  
Note. The numbers show the demands of each option.

Scholars have long believed that since customers have limited cognitive capacity, many contextual factors can impact their preferences and decisions (Tversky and Simonson 1993). Hence, considering those factors is essential to having a more effective recommendation system (Tam and Ho 2006). Examining the impact of contextual factors on consumer behavior, Cooke et al. (2002) explore how unfamiliar products should be recommended to consumers with higher chances of being accepted. Using laboratory experiments, the authors show that consumers positively evaluate the unfamiliar products when offered along with the familiar ones in a recommendation set. Therefore, familiar products can provide context for unfamiliar ones and impact their attractiveness. Moreover, Tam and Ho (2005) show the presentation format of the recommended items can impact the system’s efficacy. Using a field experiment in the context of mobile ringtones, the authors find that recommending a larger number of items increases the persuasiveness of the recommendation and attracts more users’ attention. In addition to the content of recommendation and presentation format, other contextual factors, such as explanation, type of explanations, the time of recommendation, and consumer mood, can also impact consumers’ decisions (Ho et al. 2011, Ho and Lim 2018, Gai and Klesse 2019, Adamopoulos et al. 2021).

In this study, we extend our current understanding of the role of contextual factors in the efficacy of recommendation systems. We specifically focus on how we can present a set of recommended items to have a highly effective system and the role of the decoy effect. The decoy effect is a well-studied phenomenon in regular product listings. Still, the recent pervasiveness of recommendation systems in modern business begs the question of whether decoys have the same effect on the recommended set of items. The prior research has demonstrated that the effectiveness of recommendation systems depends on several contextual and behavioral factors. The psychology and marketing literature have shown extensively that adding a decoy impacts consumer choice and facilitates decision making. However, to our knowledge, this paper is the first to examine the decoy effect in the recommendation setting.

## 3. Theoretical Framework and Developed Hypotheses

The decoy effect has previously been shown to facilitate decision making in the regular choice setting. In these studies, users were typically asked to choose an item among a small set of items, usually three, including target, competitor, and decoy (Simonson 1989, Simonson and Tversky 1992). Similarly, recommendation systems also facilitate decision making by reducing the item search space and focusing the consumers’ attention on recommended items. However, the question remains whether combining these two strategies, decoys and recommendations, can lead to synergies in facilitating consumer choice. Recommendation systems usually present users’ choice sets, so it is natural to think that the decoy effect may apply in these settings. However, depending on the recommendation settings, the decoy effect can be altered.

We apply persuasion theory to examine the interplay between the decoy effect and recommendation systems. Persuasion theory is particularly applicable in our context because recommendation systems as communication channels need to provide persuasive content to attract customer’s attention and be effective (Tam and Ho 2005, Adamopoulos et al. 2021). According to persuasion theory, the main factors that impact persuasion are source credibility, content quality, and fit with users preferences (Heesacker et al. 1983, Benoit 1987, Pornpitakpan 2004, Tormala and Petty 2004, Kumkale et al. 2010, Petty 2018). Source credibility implies the expertise, trustworthiness, and reliability of a communicator. Encountering content from a reliable source increases users’ attention and confidence and enhances the chances of message acceptance. Content from a credible source creates more favorable feelings and thoughts for customers, improving their attitudes toward it (Pornpitakpan 2004, Clark and Evans 2014, Petty 2018).

Content quality and fit are other determinants of persuasion (Petty 2018). High-quality content creates favorable user thoughts and feelings, resulting in positive attitudes and increasing the acceptance rate (Benoit 1987, Areni and Lutz 1988, O’Keefe and Jackson 1995). Furthermore, provided content is usually perceived as more persuasive when it fits individuals’ interests and needs (Tam and Ho 2005, Berkovsky et al. 2012, Hirsh et al. 2012). However, a decoy can reduce the source reliability and the persuasiveness of recommended content, decreasing the effectiveness of recommendation systems. Similarly, studies in the advice-seeking literature show that persuasive advice increases the chance of advice acceptance and encountering low-quality content unrelated to individuals’ needs enhances the chance of advice discounting (Bonaccio and Dalal 2006, Wang and Du 2018).

Considering the two common types of recommendations used in practice, personalized and nonpersonalized, we argue that the decoy effect should manifest differently in each context. Nonpersonalized recommendations are typically high-quality items that have received positive feedback from many consumers. For example, top-rated products are often recommended on e-commerce platforms to help consumers focus their attention on the highest-quality products available. These items are typically presented and ranked based on the average ratings provided by previous consumers. In this context, the recommender system is repeating information to the consumer that has been created by prior consumers, and thus, expectations of information quality for these types of recommendations follow directly from the information produced by those prior consumers. Alternatively, personalized recommendations typically include high-fit items that have been specifically selected for a user based on their tastes and preferences. These items may or may not be of high overall quality, based on the aggregate average ratings of prior consumers, but they are expected to be well received by the specific consumer. Personalized recommendations are determined using recommendation system algorithms, and their selection relies on the effectiveness of the system.

Persuasion factors, source credibility, content quality, and fit differ based on users’ motivation to process the content (Petty and Cacioppo 1979, Pornpitakpan 2004). Users usually desire more accurate information that fits their interests when the content is more personally relevant (Petty and Cacioppo 1984). In personally relevant conditions, users are more sensitive to making the best decision. They desire to receive content highly related to their interests from an expert (Czapin´ ski and Lewicka 1979, Petty 2018). In these situations, observing low-fit content from an expert may lead to negative expectation disconfirmation (Xiao and Benbasat 2007), which creates a substantial negative bias toward the content and its source, resulting in the boomerang effect (Czapin´ ski and Lewicka 1979, Pornpitakpan 2004).

This dynamic helps explain how the decoy effect might work differently across personalized and nonpersonalized settings. In the personalized setting, because the content is expected to better match customers’ needs and interests compared with the nonpersonalized setting, the system’s reliability plays a more critical role in accepting the message (Adomavicius et al. 2013). Customers expect the personalization system to know their needs and interests and offer products and services without bias or manipulation. Including a low-fit item (i.e., a decoy) can signal that the system does not have enough knowledge about the consumers’ interests, undermining the system’s reliability (Lankton et al. 2014). Low-fit items can also be seen as a signal of manipulation and bias by the system, jeopardizing consumer trust, which is one of the fundamental elements of the acceptance of personalization (Benbasat and Wang 2005, Bleier and Eisenbeiss 2015). Similarly, because personalized content is more matched to consumers’ interests, they are more likely to process the provided content to a greater extent (Tam and Ho 2005). Observing a decoy that is not highly matched with consumer’s preferences could negatively affect the users’ attitudes toward the agent (Ho and Bodoff 2014). These differences in consumer expectations between personalized and nonpersonalized recommendation contexts lead us to the following hypotheses. First, because nonpersonalized recommendations are repeating quality information from other sources, we hypothesize the following.

Hypothesis 1. In a nonpersonalized recommendation setting, we expect the decoy effect to drive demand for the target item, as has been shown in traditional choice settings.

Alternatively, because consumers are expected to be more sensitive to system reliability and information quality in a personalization context, we expect a decoy to create an opposite effect, and thus we hypothesize the following.

Hypothesis 2. In the personalized recommendation set ting, we expect the decoy effect to drive demand away from the target item.

## 4. Experiment Design and Procedure

To assess our hypotheses, we conducted a controlled randomized laboratory experiment with 632 undergraduate students in a leading U.S. business school. The ages of the participants ranged from 17 to 25 years, and 348 of them were women. Following the laboratory experiment, we replicated the study using Amazon Mechanical Turk (AMT) to evaluate the robustness and generalizability of our findings (discussed in Section 7). Furthermore, we conducted several additional experiments to test the robustness of our findings, which are discussed in Section 8.

## 4.1. Online Platform and Recommendation System Ratings Seed

For our study, we developed an online platform that provides personalized and nonpersonalized movie recommendations using the MovieTweetings database (Dooms et al. 2013). MovieTweetings is a database that captures movie ratings through the Twitter API. We used the 2018 version of the database that contains more than 600,000 ratings from more than 50,000 users for approximately 7,000 movies. For our experiments, we chose to use the most recent movies, and hence we limited the data set to the set of movies released between 2000 and 2018, resulting in 4,079 movies (the descriptive statistics are provided in Table A1 in Online Appendix A).

At the beginning of the experiment, a brief explanation of the movie recommendation platform was provided to the participants (see Figure B1 in the online appendix). At the first step of the experiment, we provided each participant with a list of 100 movies and required users to rate at least 20 movies before moving on to the next phase of the experiment (see Figure B2 in the online appendix); the rating scale was 0 to 10 (0 � you like the movie the least, 10 � you like the movie the most). We asked participants to rate at least 20 movies for two reasons: to seed the recommendation systems for the personalized treatment groups and to familiarize the participants with the platform. To enhance the chances that users were familiar with the movies and could rate them accurately, we selected the 100 most popular movies for the rating task based on their number of reviews and ratings in the MovieTweetings database. We also provided relevant additional information for each movie, such as the name, year, movie poster, synopsis, and a link to the YouTube trailer.

## 4.2. Experimental Design and Procedure

To measure the decoy effect in the personalized and nonpersonalized conditions, we used a within-subject design with four conditions: personalized (with and without a decoy) and nonpersonalized recommendations (with and without a decoy). We should note that to check the robustness of our results, we also conducted between-subject design experiments, as explained in Section 8. Participants were randomly assigned to one of the four conditions: personalized without a decoy, personalized with a decoy, nonpersonalized without a decoy, and nonpersonalized with a decoy. The assignment of users to conditions was random with one rule: the two personalized and the two nonpersonalized conditions must appear together, albeit in random order. This choice was made to clearly separate the personalized or nonpersonalized phases for users, making it easier for users to differentiate between the personalized and nonpersonalized conditions. For instance, if a user is first randomly assigned to the personalized-withdecoy condition, the next condition will be personalizedwithout-decoy. Similarly, the next two conditions will be non-personalized-with-decoy and non-personalizedwithout-decoy in random order.

For each condition, the users were shown an explanation of what they would see in the next step. The explanation for the personalized recommendation condition was “In the next round, the system will provide some movies that are specifically chosen based on your preferences and the ratings you provided at the beginning.” For the nonpersonalized recommendations, the explanation was “In the next round, the system will provide some movies that many people have watched, and you also might be interested in watching.”

4.2.1. Recommendations. For the personalized conditions, the movies were selected based on their predicted ratings using our personalization system. For the nonpersonalized conditions, the movies were chosen based on their aggregate ratings in the MovieTweetings database. For the nonpersonalized conditions in our study, the recommendations we presented to participants were based on the general popularity of movies, measured by the number of reviews and average rating for each movie in the database. To generate personalized recommendations, we used singular value decomposition (SVD), a popular collaborative filtering algorithm (Herlocker et al. 2004). We selected this algorithm because it has the lowest prediction error in our test sample (a detailed comparison of different recommendation algorithms is provided in Table C1 of the online appendix). We excluded any movies the users rated at the beginning of the experiment. We also ensured that the users saw unique movies in each condition. These precautions also ensured that the same set of movies with the same order did not repeatedly appear for different users.

Overall, in each condition, users observed a page with five movies with different genres, which were shown vertically sorted by either predicted scores (personalized) or aggregate ratings (nonpersonalized), depending on the condition. At the top of the page, we included a sentence about the recommended items to further reinforce personalized and nonpersonalized treatment conditions and their differences. For the personalized condition, the sentence was “Below is a set of top 5 recommended movies that the system predicts you might be interested in watching.” For the nonpersonalized condition, the sentence was “The following is a set of 5 movies that many people have watched, and you might also be interested in watching.”

4.2.2. Decoy. In the conditions involving a decoy, the decoy should be comparable to the target to create asymmetric domination (Huber et al. 1982, Huber and Puto 1983, Mishra et al. 1993). Thus, the decoys were selected from the same genre as the first movie presented in the list in each of the decoy conditions. Within that genre, decoys were randomly selected movies with a low predicted rating in the personalized setting and a low average rating in the nonpersonalized setting. We should note that we purposefully made the ratings salient because the decoy needs to be recognizable by users to be effective (Simonson 2014, Wu and Cosguner 2020). We also checked the robustness of our results in the personalized setting by controlling for the quality (average rating) of the decoy, presented in Section 8.2.

Following the work of Ariely (2009), we placed the decoy next to the target item as the second item on the list. The first movie on the list thus became the target item. Moreover, because we are more interested in com paring the users’ choices across different conditions, we did not randomize the order of items in the list. Instead, they were sorted in descending rating order except for substituting the decoy in the decoy conditions. This way, we could compare the conditions with similar item ordering patterns. This choice also allows users to easily observe the contrast between target and decoy and have a more consistent experience across the four conditions.

4.2.3. User Choice and Follow-Up Survey. For each movie, the title, predicted score (or aggregate ratings in the nonpersonalized setting), synopsis, poster, and a link to the YouTube trailer were provided, as previously described. Participants were given enough time to evaluate each movie, read the description, and watch the trailers. They were then asked to select the movie that they would most like to watch. We also provided a no-choice (outside) option, so the users had, in total, six options to choose from (examples of recommendation pages shown to users are provided in the online appendix; see Figures B5 and B6). After selecting a movie, users answered a survey of questions related to their perception of the system and manipulation checks.

In addition, after completing all four conditions, users responded to a set of control questions to gather demographic information, their familiarity with recommendation systems, and their overall experience with movies (see Figures B7 and B8 in the online appendix). All steps in the experiment were mandatory, and users could not skip any steps. The details of each experiment step are provided in the online appendix (Figures B1–B8). Participants in the university laboratory experiment were compensated with course credit for their participation. Participants in the AMT replication study were paid for their participation (details are provided in Section 7).

## 5. Analysis and Results

In this section, we explain our study’s empirical analyses and results. We first provide the results of the manipulation checks of our treatments. Then we present modelfree evidence, followed by the empirical analyses.

## 5.1. Manipulation Check

We first check the personalization and decoy manipulation. At the end of each condition, we asked users a Likert-type question with a one to seven scale: “The recommended movies were personalized for me,” and “The recommended movies were well-chosen,” which gauged the perceived level of personalization and presence of decoy, respectively. To check the manipulation, we estimate a fixed-effects model, and the result (Table 1) confirms that the perceived personalization was significantly higher in the personalized conditions than in the nonpersonalized conditions $( \beta = 0 . 4 1 2 , p < 0 . 0 0 1 )$ Furthermore, the result from the decoy manipulation test in Table 2 indicates that in conditions with a decoy, the perceived fit of the items was significantly less than that of items in conditions without a decoy $( \beta = - 0 . 4 0 6 , p < 0 . 0 0 1 )$ ).

Table 1. Personalization Manipulation Test

<table><tr><td></td><td>Main effects</td></tr><tr><td>Personalized</td><td>0.412***(6.00)</td></tr><tr><td>Constant</td><td>3.983***(82.04)</td></tr><tr><td>Log-likelihood</td><td>-4,603</td></tr><tr><td>AIC</td><td>9210</td></tr><tr><td>N</td><td>2,528</td></tr></table>

Note. t statistics are in parentheses.  
\*\*\*p < 0.001.

Table 2. Decoy Manipulation Test

<table><tr><td></td><td>Effect</td></tr><tr><td>Decoy</td><td>-0.406***(-6.91)</td></tr><tr><td>Constant</td><td>4.182***(100.70)</td></tr><tr><td>Log-likelihood</td><td>-4,208</td></tr><tr><td>N</td><td>2,528</td></tr><tr><td>AIC</td><td>8,419</td></tr></table>

Note. t statistics are in parentheses.  
\*\*\*p < 0.001.

## 5.2. Model-Free Evidence

Examining the effect of interest, the model-free evidence (Figure 4) demonstrates that adding a decoy in the nonpersonalized setting generates the traditional decoy effect, increasing the likelihood of selecting the target item from 0.25 in the without-decoy condition to 0.31 in the with-decoy condition. However, in the personalized condition, the opposite occurs. Adding a decoy reduces demand for the target item. The likelihood of choosing the target item in the personalized setting decreases from 0.34 to 0.2 when a decoy is present. Most of that demand shifts to the no-choice option, whose likelihood increases from 0.05 to 0.16.

These results suggest that personalization meaningfully alters the decoy effect. The traditional decoy effect predicts that the presence of the decoy moves demand to the target item; however, the presence of the decoy in the personalized setting shifts demand to the outside, no-choice option and reduces demand for the target item.

## 5.3. Empirical Analysis

To thoroughly evaluate the statistical significance of the change in the target and no-choice options, we use the following logit models:

$$
y _ {i j} = \beta_ {0} + \beta_ {1} D e c o y _ {i j} + \beta_ {2} P e r s o n a l i z e d _ {i j} + \alpha_ {i} + \varepsilon_ {i j},\tag{1}
$$

$$
y _ {i j} = \beta_ {0} + \beta_ {1} D e c o y _ {i j} + \beta_ {2} P e r s o n a l i z e d _ {i j}
$$

$$
+ \beta_ {4} D e c o y _ {i j} \times P e r s o n a l i z e d _ {i j} + \alpha_ {i} + \varepsilon_ {i j},\tag{2}
$$

where the dependent variable, $y _ { i j } ,$ indicates whether a specific alternative $( { \mathrm { i . e . } }$ , no-choice, target item) was chosen by user i in condition $j ; D e c o y _ { i j }$ is a binary variable that captures whether this observation corresponds to user i be shown a condition with decoy/without $\mathrm { d e c o y } ; P e r s o n a l i z e d _ { i j }$ is a binary variable showing whether in this observation user i was presented a personalized/ nonpersonalized condition; $\alpha _ { i }$ is the user-specific fixed effect; and $\varepsilon _ { i j }$ is the stochastic error term. The descriptive statistics of all the variables are provided in the online appendix (Table D1). Because of laboratory limitations, we ran the same experiment across three sessions over the course of a semester. Random treatment assignment was used throughout all sessions. We also include a session dummy variable in the model to control for any variation among the three sessions. To examine the decoy effect, we estimated a fixed-effect logit model with standard error clustered by users. Our primary dependent variables are the selection of the target and no-choice options. We also estimated a random-effect version of the logit model (not reported), which provided consistent results.

Figure 4. Decoy Effect in the Personalized and Nonpersonalized Conditions  
![](/api/attachments/SHT7BCSS/fulltext/images/88638a633e3d70616dc7b55b4171005d9641426851644ba5a7ce82240685b4f5.jpg)  
Note. The error bars represent standard deviation.

![](/api/attachments/SHT7BCSS/fulltext/images/0ee06e7a490f96eb4930969c3d953e770a50239da81b984a00f2423c26aabe8d.jpg)

## 5.4. Decoy Effect on the Target Item

First, we examine the impact of the decoy effect on the target option. Table 3 presents the results. As the main effects model indicates, adding a decoy significantly decreases the selection likelihood of the target item. A decoy reduces the odds of selection of the target item by 18% $\stackrel {  } { ( { e } ^ { - 0 . 1 9 1 } } = 0 . 8 2 )$ . However, the main effects mode does not consider the interaction between the decoy and the personalization context, which is our main treatment manipulation. The results of the interaction model demonstrate that the decoy increases demand for the target item in the nonpersonalized setting but decreases the likelihood of selecting the target item in the personalization context (Decoy × Personalization: $\beta _ { 3 } = - 1 . 0 0 5 ,$ $p < 0 . 0 0 1 )$ : This result confirms our hypotheses.

Figure 5 illustrates the interaction between the presence of the decoy and the recommendation conditions (personalized/nonpersonalized). In the nonpersonalized condition, the decoy increases the selection likelihood of the target item from 0.33 to 0.45. In the personalized condition, the decoy decreases the likelihood from 0.51 to 0.25. This behavior likely occurred because participants expected the personalized system to know their interests, and the presence of the decoy item contradicted their expectations, creating a conflicting environment (Fitzsimons and Lehmann 2004). Moreover, the presence of the decoy could suggest that the personalized system is less knowledgeable and less reliable. Because the target item has more similar attributes to the decoy (i.e., matched genre in our case), the decoy item could be tainting its attribute space and other items that have similar attributes, thus decreasing their selection likelihood (Frederick et al. 2014, Simonson 2014, Yang and Lynn 2014). This may create a reactance toward the decoy item and other items with similar attributes (Fitzsimons and Lehmann 2004). These results guide practitioners by suggesting that using the decoy effect may not always be an effective strategy in the recommendation setting. Depending on the recommendation context and customers’ expectations, the decoy effect can be productive (in the nonpersonalized setting) or counterproductive (in the personalized setting).

## 5.5. Decoy Effect on the No-Choice Option

We then assess the statistical significance of the change in the selection of the no-choice option. Table 4 shows the corresponding results. As the main effects model indicates, adding a decoy significantly increases the selection likelihood of the no-choice option. In other words, having a decoy increases the odds of selecting the no-choice option by 150% $( e ^ { 0 . 9 1 0 } = 2 . 5 )$ . The interaction model demonstrates that the decoy increases demand for the no-choice option in the personalized setting but does not significantly change the likelihood of selecting that option in the nonpersonalized condition (Decoy × Personalization: $\beta _ { 3 } = 1 . 5 \bar { 4 } 4 , p < 0 . 0 0 1 )$ , as can be seen in the interaction graph (Figure 6).

Table 3. Fixed Effects Logit Model on the Target Option

<table><tr><td></td><td>Main model</td><td>Interaction model</td></tr><tr><td rowspan="2">Decoy</td><td>-0.191*</td><td>0.300*</td></tr><tr><td>(-2.13)</td><td>(2.38)</td></tr><tr><td rowspan="2">Personalization</td><td>-0.056</td><td>0.424***</td></tr><tr><td>(-0.62)</td><td>(3.39)</td></tr><tr><td rowspan="2">Decoy × Personalization</td><td></td><td>-1.005***</td></tr><tr><td></td><td>(-5.52)</td></tr><tr><td>Log-likelihood</td><td>-689</td><td>-673</td></tr><tr><td>N</td><td>1,820</td><td>1,820</td></tr><tr><td> $\chi^2$ </td><td>5</td><td>36</td></tr><tr><td>AIC</td><td>1,381</td><td>1,352</td></tr></table>

Note. t statistics are in parentheses  
\*p < 0.05; \*\*\*p < 0.001.

Figure 5. Interaction Effect of the Decoy and Personalization for the Target Item  
![](/api/attachments/SHT7BCSS/fulltext/images/9fcc01ebe793513520114394041c4d79e3cc77680441e762f8bbf7f3fdff3995.jpg)

This result is the opposite of what the decoy effect predicts. The results indicate that adding a decoy does not facilitate choice in the personalized setting, and many participants preferred not to choose any recommended items. Based on our findings, including a decoy in the personalized recommendation set not only reduces the demand for the target item but also negatively impacts the acceptance of the whole recommendation set from the system, decreasing the system’s effectiveness.

## 5.6. Relative Changes of All Options

To investigate the relative changes of other options compared with the target, we estimated a multinomial logit model with the target option used as the base outcome (results in Table 5). Relative to the target item (choice 1), adding a decoy decreases the selection likelihood of the decoy option, which is expected because the decoy has a lower quality. However, relative to the target item, the selection likelihood of all other options has increased, and the effect is mainly present in the personalized setting as indicated by the interaction term: Decoy × Personalized. The no-choice option experiences the largest increase in selection likelihood. Plots of the selection likelihoods for all options are presented in Online Appendix E.

## 6. Underlying Mechanism Test

We believe the mechanism behind our findings can be explained by the fact that, in the personalized context, customers expect to observe items that are highly aligned with their preferences and are more sensitive to system reliability (Tam and Ho 2005). Personalization systems, as intelligent agents, are expected to be aware of customer preferences and provide information that is highly likely to interest them, which ultimately reduces the difficulty in making choices and increases decision confi dence (Xiao and Benbasat 2007). Adding a decoy to a personalized list of items reduces the perceived fit of the recommended items and the system’s perceived reliability, disconfirming customers’ expectations (Brown et al. 2014, Shen 2014). Consumers have been shown to discontinue using personalized recommendation systems when they provide information that disconfirms their expectations (Fitzsimons and Lehmann 2004, Komiak and Benbasat 2006). Hence, observing a decoy in the personalized recommendations results in a negative decoy effect.

Table 4. Fixed Effects Logit Model on the No-Choice Option

<table><tr><td></td><td>Main model</td><td>Interaction model</td></tr><tr><td>Decoy</td><td>0.910***(5.29)</td><td>-0.134(-0.45)</td></tr><tr><td>Personalization</td><td>1.116***(6.25)</td><td>0.157(0.56)</td></tr><tr><td>Decoy × Personalization</td><td></td><td>1.544***(4.12)</td></tr><tr><td>Log-likelihood</td><td>-190</td><td>-181</td></tr><tr><td>N</td><td>636</td><td>636</td></tr><tr><td> $\chi^2$ </td><td>74</td><td>91</td></tr><tr><td>AIC</td><td>384</td><td>368</td></tr></table>

Note. t statistics are in parentheses.  
\*\*\*p < 0.001.

Our results are also supported by findings of the advice-judgment literature, based on which individuals expect to observe accurate advice from experts (Swol and Sniezek 2005). A piece of advice with low accuracy from an expert increases the chance of advice discounting (Burgman 2016). In our personalized context, users were asked to reveal their preferences, so the system could offer items that interest them. Hence, the system was expected to be knowledgeable and provide high-fit information. Observing a decoy item runs counter to their expectations and results in lower recommendation acceptance.

To examine the mechanism, we explicitly asked participants for their opinions of the recommended items and the recommendation system in our experiments. At the end of each condition in the experiment, we asked users two Likert-type questions with a one to seven scale based on items used in prior recommendation research: “The system is able to identify good movies” and “I rely on the system for deciding what movies to watch” (Benbasat and Wang 2005, Komiak and Benbasat 2006). If the presence of a decoy does not impact the users’ perception of system quality and reliability, then there should not be significant differences between the responses in the conditions with and without the decoy. Otherwise, we can conclude that the decoy impacts the perceived reliability.

Figure 6. Interaction Effect of the Decoy and Personalization for the No-Choice  
![](/api/attachments/SHT7BCSS/fulltext/images/fb28c2695222e3b53b273332a4d69f0e2137275adc8d7014576fe31805387126.jpg)

We first analyzed users’ assessment of the recommended movies in each condition. Figure 7 demonstrates that users perceive the recommended items as less acceptable in conditions with a decoy in both personalized and nonpersonalized conditions. However, the reduction is larger in the personalized condition. To statistically measure the effect of decoy on users’ opinions about movies, we used a fixed-effects linear regression model (Table 6 demonstrates the results). As the main effects model shows, adding a decoy significantly decreases the acceptability of content $( \beta _ { 1 } = - 0 . 5 5 6 , p <$ 0:001): Moreover, the interaction model shows that the negative effect of the decoy is larger in the personalized condition $( \beta _ { 3 } = - 0 . 6 3 8 , ~ p < 0 . 0 0 1 )$ :

We also analyzed the impact of decoy on the perceived reliability of the system. Figure 8 demonstrates the perceived reliability of the system in personalized and nonpersonalized conditions with and without a decoy. As the figure indicates, overall, the perceived reliability of the recommendation systems decreases by adding a decoy. Table 7 demonstrates the results. As the main effects model shows, adding a decoy decreases the perceived reliability of the system $( \beta _ { 1 } =$ $- 0 . 6 7 3 , p < 0 . 0 0 1 )$ : Moreover, the interaction model shows, that although adding a decoy decreases the perceived reliability in the nonpersonalized condition, its reduction is more significant in the personalized condition $( \beta _ { 3 } = - 0 . 8 1 5 , ~ p < 0 . 0 0 1 )$

## 7. Replication Study

To assess the generalizability and robustness of the results, we conducted the same experiment on the AMT platform using a participant sample with more diverse backgrounds and demographics. We selected workers with a human intelligent task approval rate greater than 95%. We limited the participants’ age to 18 to 65 to ensure that users were familiar with and comfortable using technology. Because the experiment is in English, we limited the pool to the participants who are currently U.S. citizens and can speak English fluently. On average, the study took 15 minutes to complete, and we paid the workers \$2 for the study (based on the federal mini mum wage of \$7.25). Two hundred individuals completed our study. We also checked for lack of attention (e.g., not spending enough time in each step or having

Table 5. Multinomial Logit Model

<table><tr><td colspan="2"></td><td>Main effects model</td><td>Interaction</td></tr><tr><td rowspan="3">Choice2</td><td>Decoy</td><td>-1.375***(-8.31)</td><td>-1.363***(-8.21)</td></tr><tr><td>Personalized</td><td>-0.002(-0.02)</td><td>0.036(0.22)</td></tr><tr><td>Decoy × Personalized</td><td></td><td>0.729*(2.26)</td></tr><tr><td rowspan="4">Choice3</td><td>Constant</td><td>-1.013***(-12.50)</td><td>-0.996***(-12.24)</td></tr><tr><td>Decoy</td><td>0.588***(5.05)</td><td>0.602***(5.12)</td></tr><tr><td>Personalized</td><td>-0.138(-1.24)</td><td>-0.117(-1.04)</td></tr><tr><td>Decoy × Personalized</td><td></td><td>0.735**(3.15)</td></tr><tr><td rowspan="4">Choice4</td><td>Constant</td><td>-0.250***(-4.21)</td><td>-0.233***(-3.88)</td></tr><tr><td>Decoy</td><td>0.306*(2.46)</td><td>0.323*(2.55)</td></tr><tr><td>Personalized</td><td>0.004(0.03)</td><td>0.014(0.11)</td></tr><tr><td>Decoy × Personalized</td><td></td><td>1.058***(4.21)</td></tr><tr><td rowspan="4">Choice5</td><td>Constant</td><td>-0.537***(-8.62)</td><td>-0.524***(-8.27)</td></tr><tr><td>Decoy</td><td>0.307*(2.47)</td><td>0.322*(2.57)</td></tr><tr><td>Personalized</td><td>0.016(0.13)</td><td>0.029(0.22)</td></tr><tr><td>Decoy × Personalized</td><td></td><td>1.011***(3.80)</td></tr><tr><td rowspan="9">Choice6</td><td>Constant</td><td>-0.633***(-9.93)</td><td>-0.618***(-9.52)</td></tr><tr><td>Decoy</td><td>0.972***(5.21)</td><td>0.711***(3.52)</td></tr><tr><td>Personalized</td><td>1.067***(5.97)</td><td>0.904***(4.82)</td></tr><tr><td>Decoy × Personalized</td><td></td><td>2.108***(5.40)</td></tr><tr><td>Constant</td><td>-1.572***(-14.96)</td><td>-1.563***(-15.62)</td></tr><tr><td>Log-likelihood</td><td>-4,203</td><td>-4,183</td></tr><tr><td> $\chi^2$ </td><td>187</td><td>242</td></tr><tr><td>AIC</td><td>8,437</td><td>8,405</td></tr><tr><td>N</td><td>2,528</td><td>2,528</td></tr></table>

Note. t statistics are in parentheses  
\*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001.

Figure 7. Decoy Effect on Perceived Recommendations Attractiveness  
![](/api/attachments/SHT7BCSS/fulltext/images/3bad20b6238bd3b0b77115d6b613623ee5e79e3895049297c962b1d1bed722ce.jpg)  
Note. The error bars represent standard deviation.

no variation in survey responses) and removed five participants from our data. A total of 195 AMT participants remained, with ages ranging from 19 to 50 years, with a mean of 34 years, and 103 of them were women.

As Figure 9 shows, consistent with the results of the laboratory experiments (Figure 10), the decoy effect is reduced in the personalized condition compared with the nonpersonalized condition. In the context of nonpersonalized recommendations, without a decoy, the average selection likelihood of the target option is 0.27, and adding a decoy increased that to 0.29; in the laboratory experiment, the selection likelihood increased from 0.25 to 0.31. Additionally, the decoy decreases the selection likelihood of the no-choice option from 0.07 to 0.04 in the nonpersonalized setting; in the laboratory experiment, the selection likelihood decreased from 0.04 to 0.03. However, in the personalized setting, without a decoy, the selection likelihood of the target option is 0.27, and adding a decoy reduces that likelihood to 0.22; in the laboratory experiment, the selection likelihood decreased from 0.34 to 0.2. In the personalized setting, the decoy increases the selection likelihood of the no-choice option from 0.06 to 0.14; in the laboratory experiment, the selection likelihood increased from 0.05 to 0.16. The overall selection likelihoods for each option are highly similar when comparing our laboratory and AMT experiments (see Figures E1–E4 in the online appendix).

Table 6. Fixed Effects Model for the Perceived Recommendations Attractiveness

<table><tr><td></td><td>Main effects model</td><td>Interaction</td></tr><tr><td>Decoy</td><td>-0.556***(-11.08)</td><td>-0.237***(-3.60)</td></tr><tr><td>Personalized</td><td>-0.313***(-5.31)</td><td>0.006(0.08)</td></tr><tr><td>Decoy × Personalized</td><td></td><td>-0.638***(-6.42)</td></tr><tr><td>Constant</td><td>5.223***(137.42)</td><td>5.063***(117.05)</td></tr><tr><td>Log-likelihood</td><td>-3,974</td><td>-3,950</td></tr><tr><td>AIC</td><td>7,952</td><td>7,906</td></tr><tr><td>N</td><td>2,528</td><td>2,528</td></tr></table>

Note. t statistics are in parentheses  
\*\*\*p < 0.001.

Figure 8. Decoy Effect on Perceived System Reliability  
![](/api/attachments/SHT7BCSS/fulltext/images/8d00728d6525f458922df7af331b241adf12f333e500450d600f1c195f302abd.jpg)  
Note. The error bars represent standard deviation.

## 8. Robustness Checks

In this section, we check the robustness of our results by performing additional analyses and conducting additional experiments to consider factors that might impact user behavior.

## 8.1. Between-Subject Analysis

We initially conducted within-subject experiments, and to ensure that these results would also hold in the between-subject design, we analyzed data with this perspective. Specifically, in the original design, each user randomly started the experiment with one of the four conditions and then continued with other rounds. To be able to conduct a between-subject analysis for each user, we kept the observations related to the first round and filtered out all additional rounds (Tabachnick et al. 2007). This strategy mimics a betweensubject design in which users were randomly assigned to one of the four conditions. Because we no longer have repeated observations in this analysis, we also control for individual characteristics by using a set of control variables described in Table 8.

Notably, the interaction model in Table 9 shows that including a decoy significantly increases the selection likelihood of the target option in the nonpersonalized condition while significantly decreasing it in the personalized condition (Decoy × Personalization: $\beta _ { 3 } = - 1 . 6 1 0 ,$ $p < 0 . 0 0 1 )$ ). Furthermore, the results in Table 10 indicate that including a decoy significantly increases the selection likelihood of the no-choice option (Decoy: $\beta _ { 1 } =$ $1 . 4 7 3 , p < 0 . 0 1 )$ , and the interaction model shows this effect is more prominent in the personalized condition (Decoy × Personalization: $\beta _ { 3 } = 2 . 4 8 9 , p < 0 . 0 5 )$ . We should note that in comparison with the within-subject analysis, the significance of the effects decreased in the betweensubject comparison, which is expected due to the reduction in sample size.

Table 7. Fixed Effects Model for the Perceived Reliability

<table><tr><td></td><td>Main effects model</td><td>Interaction</td></tr><tr><td>Decoy</td><td>-0.673***(-12.15)</td><td>-0.266***(-3.86)</td></tr><tr><td>Personalized</td><td>-0.205**(-3.15)</td><td>0.203*(2.39)</td></tr><tr><td>Decoy × Personalized</td><td></td><td>-0.815***(-7.64)</td></tr><tr><td>Constant</td><td>4.848***(114.81)</td><td>4.644***(98.46)</td></tr><tr><td>Log-likelihood</td><td>-4,214</td><td>-4,181</td></tr><tr><td>AIC</td><td>8,431</td><td>8,368</td></tr><tr><td>N</td><td>2,528</td><td>2,528</td></tr></table>

Note. t statistics are in parentheses.  
\*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001.

## 8.2. Role of Item Quality

In the original personalized experimental setting, we focused on how the recommended items fit with users interests and did not control their quality. We selected movies based on personalized predicted preference scores from our recommendation system and defined a decoy as a movie with a low prediction score. However, one might argue that the quality of the movie might also play a role in the personalized setting, especially for the decoy item. The interaction between the quality and the fit of the recommended movies may be driving the observed behavioral changes. To address this issue, we first repeat our main analysis and control for movie quality using average user ratings. To further disentangle the quality and fit effects, we also conducted additional experiments in the personalized setting.

8.2.1. Control for Item Quality. First, we estimate a fixed effects logit model that includes the average user ratings of the movies that each user observed in each round in our original experiment. Tables 11 and 12 demonstrate the results, which are consistent with our initial find ings. Specifically, in Table 11, we can see that, even when controlling for movie quality, adding a decoy significantly reduces demand for the target item in the personalized setting (Decoy × Personalization: $\beta _ { 3 } = - 1 . 0 3 1$ $p < 0 . 0 0 1 )$ ). In Table 12, the interaction model shows the decoy significantly increases the selection of the nonchoice option in the personalized setting (Decoy × Personalization: $\beta _ { 3 } = 1 . 7 0 \bar { 4 } , p < 0 . 0 0 1 )$

8.2.2. Quality in the Backend, Fit in the Frontend. To further ensure that the quality of the decoy does not play a significant role in user behavior in the personalized setting, we conducted a new experiment with different treatment groups based on the quality of the decoy item, measured by average user rating. In this experiment, like the original experiment presented in this paper, we showed the personalized preference prediction score of each movie and defined the decoy based on the prediction score. However, in this experiment, we controlled for movie quality in the backend using average user ratings. Specifically, movies were pseudo-randomly selected such that all movies except the decoy had high average user ratings (quality) in addition to the prediction score (shown in the frontend). The quality (average user rating) of the decoy is controlled in the backend to be low or high, depending on the treatment conditions. We designed three experimental groups: control, treatment I, and treatment II. In the control group, users were presented with a list of five personalized recommendations, all of which had high quality and high fit. In treatment I, we introduced a decoy as an item with high quality and low fit; all other movies had high quality and high fit. In treatment II, the decoy was introduced as an item with low quality and low fit; all other movies had high quality and high fit. Like our initial design, in the treatment groups, the decoy had a matched genre with the target item (first item in the list) and was placed as the second item in the set. Besides controlling for the quality of movies, all other experimental procedures and steps were the same as our initial experiment, described in Section 4.

Figure 9. Decoy Effect on the No-Choice and Target Options (AMT Experiment)  
![](/api/attachments/SHT7BCSS/fulltext/images/70f39e6a24887986893b5c1f0ccf75b9f49d87d39d1db1d0f2583b1414dd1a4e.jpg)  
Note. The error bars represent standard deviation.

![](/api/attachments/SHT7BCSS/fulltext/images/39978dfa13510e9837b44619459f5f6ddde6f62d5f806ae2acf08833e33f6bc4.jpg)

Figure 10. Decoy Effect on the No-Choice and Target Options (Laboratory Experiment)  
![](/api/attachments/SHT7BCSS/fulltext/images/38ae528b9ed273c8666f4fc9668ea78376d542a761a1073c7ad2530c51caf226.jpg)  
Note. The error bars represent standard deviation.

For this experiment, we updated the database to include more updated movies, resulting in 4,432 movies from 2000 to 2021. Moreover, we included a lottery in the study to make the experiment choice task more incentive compatible and in line with the online choice environment with actual behavioral outcomes. Specifically, we informed users that one of the participants would randomly win a gift card to purchase their selected movie to watch. We conducted a betweensubject experiment on AMT with 205 participants. The study took 10 minutes on average to complete, and we paid \$1.25 to each participant (based on the national average wage of \$7.25). We checked the quality of users responses and the time spent on the study and removed four of the participants that did not meet our quality standard.

We analyzed the remaining 201 users’ choices using a logit model, with the selection of no-choice and target items as the dependent variable. We include user char acteristics as control variables. As the results in Table 13 show, interestingly, the quality of movies does not change the decoy effect we initially found in the personalized setting. Regardless of the quality of the decoy item, users behave the same toward the decoys with low prediction scores. Specifically, in both treatment groups, including a decoy significantly increases the selection likelihood of the no-choice option while decreasing the selection likelihood of the target options.

8.2.3. Quality and Fit in the Frontend. To further disentangle the effects of quality and fit, we performed another experiment in which, for each movie, we showed both the quality (average user rating) and fit (personal ized predicted preference score) indicators for users. This design follows a real-world setting, such as Google Reviews, in which, for each recommended item, both the prediction scores and average user ratings are presented to users. Particularly, we designed four experimental groups: control, treatment I, treatment II, and treatment III. In the control group, all the movies had high quality and high fit. In treatment I, the decoy was introduced as a movie with low quality and a high fit. In treatment II, the decoy was a high-quality movie with a low fit. In treatment III, the decoy has both low quality and low fit. All movies other than the decoy had high quality and high fit. Furthermore, in all treatment groups, the decoy had a matched genre with the target item (the first item in the list) and was placed as the second item. All other experimental procedures and steps were identical to our initial experiment, as described in Section 4.

Table 8. Definition of Control Variables

<table><tr><td>Variable</td><td>Definition</td></tr><tr><td>RS_Familiarity</td><td>The level of familiarity of the participants with the recommendation systems, on a scale of zero to seven</td></tr><tr><td>Age</td><td>Age of participants</td></tr><tr><td>Gender</td><td>Gender of participants: $\left\{ \begin{array}{l} 1 = Female \\ 0 = Male \end{array} \right.$ </td></tr><tr><td>Movie_Experience</td><td>The level of movie experience of the participants; measured by how many movies the participants watched in a month.</td></tr><tr><td>Native_Speaker</td><td>A binary variable indicating whether the participant is a native English speaker: $\left\{ \begin{array}{l} 1 = \text{The participant is a native English speaker} \\ 0 = \text{The participant is not a native English speaker} \end{array} \right.$ </td></tr></table>

Table 9. Between-Subject Analysis of Target Option

<table><tr><td></td><td>Main model</td><td>Interaction model</td></tr><tr><td>Decoy</td><td>-0.221(-1.18)</td><td>0.569*(2.13)</td></tr><tr><td>Personalized</td><td>0.013(0.07)</td><td>0.771**(2.91)</td></tr><tr><td>Decoy × Personalized</td><td></td><td>-1.610***(-4.17)</td></tr><tr><td>Constant</td><td>-2.133(-1.46)</td><td>-2.495(-1.65)</td></tr><tr><td>User characteristics</td><td>Yes</td><td>Yes</td></tr><tr><td>Log-likelihood</td><td>-351</td><td>-342</td></tr><tr><td>N</td><td>632</td><td>632</td></tr><tr><td> $\chi^2$ </td><td>6</td><td>24</td></tr><tr><td>AIC</td><td>723</td><td>707</td></tr></table>

Note. t statistics are in parentheses.  
ˆp < 0.10; \*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001.

Like the previous experiment, in this study, we used the updated database with 4,432 movies released from 2000 to 2021, and we used the same lottery to make the choice task more incentive compatible. We conducted a between-subject experiment on AMT with 205 participants. The study again took about 10 minutes on average to complete, and we paid users \$1.25 for each participant (based on the national average wage of \$7.25). Two participants’ responses were removed because of quality issues. We analyzed the remaining 203 observations using a logit model with the selection of no-choice and target items as the dependent variable. As shown in Table 14, in treatment group III, where the decoy has low quality and low fit, the selection likelihood of the no-choice option significantly increased (β � 1:594, p < 0:05). In contrast, the target selection sig nificantly decreased (β � �1:102, p < 0:05). In treatment group II, where the decoy has high quality and low fit, we observe the same pattern; a decoy increases the selection likelihood of the no-choice option (β � 1:362, p < 0:05) but decreases the selection likelihood of the target option $( \beta = - 0 . 7 4 0 , \ p < 0 . 1 )$

Table 10. Between-Subject Analysis of No-Choice Option

<table><tr><td></td><td>Main model</td><td>Interaction model</td></tr><tr><td>Decoy</td><td>1.473**(3.19)</td><td>-0.310(-0.39)</td></tr><tr><td>Personalized</td><td>1.657***(3.45)</td><td>-0.008(-0.01)</td></tr><tr><td>Decoy × Personalized</td><td></td><td>2.489*(2.46)</td></tr><tr><td>Constant</td><td>-4.415*(-2.00)</td><td>-3.272(-1.47)</td></tr><tr><td>User characteristics</td><td>Yes</td><td>Yes</td></tr><tr><td>Log-likelihood</td><td>-117</td><td>-114</td></tr><tr><td>N</td><td>632</td><td>632</td></tr><tr><td> $\chi^2$ </td><td>39</td><td>50</td></tr><tr><td>AIC</td><td>254</td><td>249</td></tr></table>

Note. t statistics are in parentheses  
\*p < 0.05; \*\*p < 0.01; \*\*\*p < 0.001

Table 11. Fixed Effects Logit Model on the Target Option (Movie Quality Controlled)

<table><tr><td></td><td>Main model</td><td>Interaction model</td></tr><tr><td>Decoy</td><td>-0.008(-0.04)</td><td>0.214(1.02)</td></tr><tr><td>Personalized</td><td>-0.309(-1.14)</td><td>0.571 $^{ \uparrow }$ (1.80)</td></tr><tr><td>Decoy × Personalized</td><td></td><td>-1.031***(-5.45)</td></tr><tr><td>Average quality</td><td>Yes</td><td>Yes</td></tr><tr><td>N</td><td>1,820</td><td>1,820</td></tr><tr><td>Log-likelihood</td><td>-688</td><td>-673</td></tr><tr><td> $\chi^2$ </td><td>6</td><td>36</td></tr><tr><td>AIC</td><td>1,382</td><td>1,354</td></tr></table>

Note. t statistics are in parentheses  
ˆp < 0.10; \*\*\*p < 0.001.

These results follow our initial findings indicating that the decoy with low fit can signal the incompetence of the personalization systems in recognizing users needs and interests, increasing the selection of no-choice options. However, interestingly we do not observe such an effect in treatment group I, where the decoy was defined as an item with a low-quality and high prediction score. Such a decoy does not significantly increase the selection likelihood of no-choice. These results demonstrate that in the personalized setting, users weigh prediction scores more than average user ratings. This follows the prior findings indicating that people usually rely more on prediction scores than average ratings (Adomavicius et al. 2021a, b) when choosing recommended items. Together, these results demonstrate that including a decoy as an item with a low prediction score, regardless of quality, increases the selection likelihood of the no-choice option and decreases the selection of the target option.

Table 12. Fixed Effects Logit Model on the No-Choice Option (Movie Quality Controlled)

<table><tr><td></td><td>Main model</td><td>Interaction model</td></tr><tr><td>Decoy</td><td>1.175**(2.97)</td><td>0.411(0.94)</td></tr><tr><td>Personalized</td><td>0.789*(1.67)</td><td>-0.761(-1.26)</td></tr><tr><td>Decoy × Personalized</td><td></td><td>1.704***(4.39)</td></tr><tr><td>Average quality</td><td>Yes</td><td>Yes</td></tr><tr><td>N</td><td>636</td><td>636</td></tr><tr><td>Log-likelihood</td><td>-190</td><td>-180</td></tr><tr><td> $\chi^2$ </td><td>75</td><td>94</td></tr><tr><td>AIC</td><td>385</td><td>367</td></tr></table>

Note. t statistics are in parentheses  
ˆp < 0.10; \*\*p < 0.01; \*\*\*p < 0.001.

Table 13. Logit Model Quality Controlled in the Backend

<table><tr><td></td><td>No-choice option</td><td>Target option</td></tr><tr><td rowspan="2">Treatment I</td><td>1.320*</td><td>-0.660*</td></tr><tr><td>(1.93)</td><td>(-1.70)</td></tr><tr><td rowspan="2">Treatment II</td><td>1.636*</td><td>-0.841**</td></tr><tr><td>(2.45)</td><td>(-2.09)</td></tr><tr><td rowspan="2">Constant</td><td>-3.060**</td><td>-0.583*</td></tr><tr><td>(-5.17)</td><td>(-2.28)</td></tr><tr><td>User characteristics</td><td>Yes</td><td>Yes</td></tr><tr><td>Log-likelihood</td><td>-75</td><td>-112</td></tr><tr><td>N</td><td>201</td><td>201</td></tr><tr><td> $\chi^2$ </td><td>6</td><td>5</td></tr><tr><td>AIC</td><td>153</td><td>231</td></tr></table>

Note. t statistics are in parentheses.  
\*p < 0.05; \*\*p < 0.01.

## 8.3. Saliency of the Decoy

Based on the original definition of the decoy effect and following the author’s emphasis (Simonson 1989, 2014), this effect is expected to occur when the decoy is saliently shown to users and creates a clear contrast between the decoy and target items. Other studies also showed that the chance that users could detect the decoy without it being saliently shown to them is low (Wu and Cosguner 2020). Therefore, in the personalized setting, we made the decoy salient based on attributes of prediction scores, which usually impact consumer choice in movie selection. To further check if the saliency of a decoy is a crucial element in observing the decoy effect, we conducted a final experiment in the personalized setting. Instead of showing prediction scores, we showed average ratings for each movie. Using this strategy, we eliminated the saliency of the prediction score and made the movies’ average user ratings a salient decoy signal. We specifically showed users a set of personalized movie recommendations based on their interests and informed them that the movie choices were personalized movies for them. However, instead of showing the prediction score, we showed the average user rating of each movie and labeled them as such.

We designed two experimental groups: a control and a treatment. In the control group, all movies had a high fit (prediction scores controlled in the backend) and high quality (average ratings shown in the front end). The movies had different genres and were sorted in descending order based on the average user rating. In the treatment group, we defined the decoy as a movie that had a high fit (prediction scores controlled in the back end) and a low quality (average rating shown in the front end). The decoy had a matched genre with the target item and was placed as the second movie on the list. Like the previous experiments, in this study, we used the updated database to include more recent movies, 4,432 movies from 2000 to 2021, and we included a lottery to make it more realistic. We conducted a new between-subject experiment on AMT with 205 participants, which took 10 minutes to complete on average, and we paid users \$1.25 each (based on the national average wage of \$7.25). Three of the participants did not meet our quality standard and were removed. We analyzed the choice of the remaining 202 participants.

Table 14. Logit Model of Fit and Quality Scores Shown Together

<table><tr><td></td><td>No-choice option</td><td>Target option</td></tr><tr><td>Treatment I</td><td>0.553(0.73)</td><td>-0.168(-0.41)</td></tr><tr><td>Treatment II</td><td>1.362*(1.96)</td><td>-0.740(-1.69)</td></tr><tr><td>Treatment III</td><td>1.594*(2.34)</td><td>-1.102*(-2.36)</td></tr><tr><td>Constant</td><td>-2.773**(-4.65)</td><td>-0.438(-2.36)</td></tr><tr><td>User characteristics</td><td>Yes</td><td>Yes</td></tr><tr><td>Log-likelihood</td><td>-81</td><td>-119</td></tr><tr><td>N</td><td>203</td><td>203</td></tr><tr><td> $\chi^2$ </td><td>7</td><td>7</td></tr><tr><td>AIC</td><td>170</td><td>246</td></tr></table>

Note. t statistics are in parentheses.  
ˆp < 0.10; \*p < 0.05; \*\*p < 0.01.

We analyzed user behavior using a logit model with the selection of no-choice and target items as the dependent variable. As the results in Table 15 indicate, interestingly, including a decoy with emphasizing movies average rating results in findings similar to our initial findings on nonpersonalized conditions. Including such a decoy significantly increases the selection likelihood of the target option $( \beta = 0 . 6 5 1 , p < 0 . 0 5 )$ . It does not significantly decrease the no choice. These results reaffirm prior findings in the decoy effect literature, based on which the decoy effect can be observed when a decoy is saliently shown to users (Wu and Cosguner 2020). Because the decoy is saliently presented using item quality and we observe the standard decoy effect, these results also provide additional evidence that using a decoy that is salient based on item fit in personalized recommendations is what drives the counter effect observed in our previous experiments.

Table 15. Logit Model of Quality Shown in the Personalized Setting

<table><tr><td></td><td>No-choice option</td><td>Target option</td></tr><tr><td>Treatment</td><td>-0.947(-1.11)</td><td>0.651*(2.10)</td></tr><tr><td>Constant</td><td>-2.944**(-6.40)</td><td>-1.099**(-4.75)</td></tr><tr><td>User characteristics</td><td>Yes</td><td>Yes</td></tr><tr><td>Log-likelihood</td><td>-30</td><td>-123</td></tr><tr><td>N</td><td>202</td><td>202</td></tr><tr><td> $\chi^2$ </td><td>1</td><td>4</td></tr><tr><td>AIC</td><td>63</td><td>250</td></tr></table>

Note. t statistics are in parentheses  
\*p < 0.05; \*\*p < 0.01.

## 9. Discussion

Our paper contributes to the literature on recommendation systems and the decoy effect. Regarding recommendation, a growing body of literature has demonstrated the importance of considering contextual factors on the effectiveness of such systems (Ho and Lim 2018, Kawaguchi et al. 2019, Adamopoulos et al. 2021). Despite the extant work, various underexplored contextual factors can still influence the system’s efficacy. We take another step forward in this stream and are the first to explore the decoy effect in this setting. The existing literature on the decoy effect prescribes recommendation systems that benefit from adding decoy items to a choice set (Huber et al. 1982, Simonson 1989, Sue O’Curry and Pitts 1995). However, our study shows that this strategy cannot be practical in all recommendation settings. Although it can be a helpful strategy in a nonpersonalized environment, using decoys can be counterproductive in a personalized one. Given the growing pervasiveness of recommendation systems and their increasing presence in the consumption process, it is essential to understand how existing theories change in these new technological contexts. We argue that although using decoys may be an effective marketing strategy in traditional settings, it can have unintended consequences in the personalized context, hurting system reliability.

This study also has important practical and managerial implications. Recommendation systems usually provide a set of attractive items to consumers. However, this can overwhelm customers with many viable options, creating choice overload and over-specialization issues (Long et al. 2022). Choice overload has been shown to impact recommendation systems’ effectiveness negatively. One well-known strategy that has been shown to be effective in mitigating choice overload in traditional choice settings is the decoy effect. Companies also use this technique to drive sales in their digital marketing and increase their profits. Large technology companies, such as Apple, Netflix, and Spotify, use this technique to sell more of their higher-priced products and services (Tomer Hochma 2017, Design for Growth 2020).

Based on these observations, practitioners have discussed the potential benefits of using the decoy effect in recommendation systems as a nudge to change consumers’ choices toward their business goals (Theocharous et al. 2019). For example, it has been discussed that dating apps like Tinder can use decoys to influence users’ dating behavior (The Decision Laboratory 2021).

However, our study demonstrates that the decoy effect is not necessarily a helpful strategy for all recommendation settings. The effect can be positive or negative depending on the recommendation context and user expectations. Our results show that the decoy effect can be used in nonpersonalized recommendation settings to drive user attention toward the target option. However, this strategy is unsuitable for personalized contexts because the presence of decoy can drive consumers to opt out of purchasing altogether. Recommendation systems generate more than \$1 billion of Netflix’s annual revenue (Goled 2021). Given that we observe that including a decoy could decrease the likelihood of purchases by 11% in the personalized setting, using decoys with personalized recommendations could decrease the platform’s revenue by more than \$110 million. Alternatively, our findings suggest that decoys could lead to increased revenue and profit in the nonpersonalized setting because a decoy increases the likelihood of selecting a target item. Hence, platforms could use this strategy to increase their profit if they use decoys to direct customers to a specific item that has higher profit levels.

Our findings highlight the importance of differentiating various product recommendations since they can bring different consumer expectations, resulting in different behaviors. Studying the differences between contexts is especially important because managers are considering various behavioral strategies to improve the effectiveness of recommendation systems. For instance, considering consumers’ psychology, many companies are trying to induce diversity, novelty, serendipity, and so on, to satisfy consumer needs from different dimensions (Adamopoulos and Tuzhilin 2014b, Ricci et al. 2015). Based on our research, managers need to explore user behavior toward these strategies in personalized and nonpersonalized settings before implementing them on a large scale. Furthermore, firms like Amazon are integrating personalized recommendations with other types of content, such as popular and trending items, new items, expert recommendations, and even advertising. Our results show consumer expectations are different in a personalized setting, and practitioners need to be cautious about mixing other content with personalized recommendations to avoid any unintended effects.

Beyond showing the nuances of the decoy effect, this paper also has broader implications for designing recommendation systems. First, our study highlights the potential differences between traditional and recommendation choice settings and underscores the importance of examining the established theories in this environment. Additionally, our study draws the attention of researchers and practitioners to the importance of a comprehensive approach to recommendation system design. Specifically, our findings underscore the importance of contextual factors in the effectiveness of these systems and consumer behavior. Our research reaffirms that online consumer behavior needs to be further studied and incorporated into the design of recommendation systems. Moreover, our results reaffirm that items in a set are not independent and thus should not be picked independently. Our results demonstrate how the composition of a recommended list of items impacts consumers’ behavior, their evaluation of the system, and their acceptance of the recommendations. Currently, in research and practice, much of the focus on recommendation systems revolves around the characteristics of a single recommended item and how that item can impact consumers’ behavior. In contrast, the presence of other alternatives and the relations among them have largely been ignored (Adamopoulos 2013). Our study is among the first to demonstrate the value of considering a set of recommended items together and presenting those items to have more effective personalization systems.

Future research can explore other contextual factors known to impact consumer decisions in the recommendation setting. Furthermore, in this study, we focus on movies, which are experience products; future studies can extend our work by exploring the decoy effect with other types of products, such as search products and durable goods. Additionally, it would be interesting to examine the role of the decoy effect on diverse types of consumer behavior, such as information gathering.

## 10. Conclusion

Recommendation systems have become an integral part of corporate online strategies. Such systems can significantly impact corporate profits by influencing consumers’ choice, satisfaction, and loyalty toward the companies and brands. Thus, it is crucial to investigate how the effectiveness of these tools can be improved. This research investigates the decoy effect in recommendation systems and shows how including a decoy impacts consumer behavior differently in personalized and nonpersonalized settings. We demonstrate that adding a decoy to a personalized setting can be counterproductive, decreasing the demand for the target item and increasing the chance of no-choice. However, decoys can be an effective strategy to use in nonpersonalized recommendations to drive consumer attention toward the target item. To examine the mechanism behind the findings, we analyzed users’ opinions on the quality of recommendations and the reliability of the system. We showed that in the personalized setting, adding a decoy, which is less aligned with users’ interests, diminishes the perceived recommendation quality and system’s reliability, ultimately reducing the recommendation’s effectiveness. We furthermore checked our findings’ robustness and generalizability by conducting multiple experiments in the laboratory and on the AMT platform with different sets of users.

## References

Acquisti A, Adjerid I, Balebako R, Brandimarte L, Cranor LF, Komanduri S, Leon PG, et al. (2017) Nudges for privacy and security: Understanding and assisting users’ choices online. ACM Comput. Survey 50(3):1–41.

Adamopoulos P (2013) Beyond rating prediction accuracy: On new perspectives in recommender systems. Proc. 7th ACM Conf. Recommender Systems (ACM, New York), 459–462.

Adamopoulos P, Tuzhilin A (2013) Recommendation opportunities: Improving item prediction using weighted percentile methods in collaborative filtering systems. Proc. 7th ACM Conf. Recommender Systems (ACM, New York), 351–354.

Adamopoulos P, Tuzhilin A (2014a) On over-specialization and concentration bias of recommendations: Probabilistic neighborhood selection in collaborative filtering systems. Proc. 8th ACM Conf. Recommender Systems (ACM, New York), 153–160.

Adamopoulos P, Tuzhilin A (2014b) On unexpectedness in recommender systems: Or how to better expect the unexpected. ACM Trans. Intelligent Systems Tech. 5(4):1–32.

Adamopoulos P, Ghose A, Tuzhilin A (2021) Heterogeneous demand effects of recommendation strategies in a mobile application: Evidence from econometric models and machine-learning instruments. MIS Quart. 46(1):101–150.

Adjerid I, Acquisti A, Loewenstein G (2019) Choice architecture, framing, and cascaded privacy choices. Management Sci. 65(5): 2267–2290.

Adomavicius G, Bockstedt J, Curley S, Zhang J (2021a) Effects of personalized and aggregate Top-N recommendation lists on user preference ratings. ACM Trans. Inform. Systems 39(2):1–38.

Adomavicius G, Bockstedt J, Curley S, Zhang J (2021b) Effects of per sonalized recommendations versus aggregate ratings on postconsumption preference responses. MIS Quart. 46(1):627–644.

Adomavicius G, Bockstedt JC, Curley SP, Zhang J (2013) Do recommender systems manipulate consumer preferences? A study of anchoring effects, Inform, Sustems Res, 24(4):956–975

Adomavicius G, Bockstedt JC, Curley SP, Zhang J (2018) Effects of online recommendations on consumers’ willingness to pay. Inform. Systems Res. 29(1):84–102.

Areni CS, Lutz RJ (1988) The role of argument quality in the elaboration likelihood model. ACR North Amer. Adv. 15(1):197–203.

Ariely D (2009) Predictably Irrational: The Hidden Forces that Shap Our Decisions (HarperCollins Publishers, New York).

Ariely D, Wallsten TS (1995) Seeking subjective dominance in multidimensional space: An explanation of the asymmetric dominance effect. Organ. Behav. Human Decision Processes 63(3):223–232.

Benbasat I, Wang W (2005) Trust in and adoption of online recom mendation agents. J. Assoc. Inform. Systems 6(3):72–101.

Benoit WL (1987) Argumentation and credibility appeals in persuasion. Southern J. Comm. 52(2):181–197.

Berkovsky S, Freyne J, Oinas-Kukkonen H (2012) Influencing indi vidually: Fusing personalization and persuasion. ACM Trans Interactive Intelligent Systems 2(2):1–8.

Bhargava M, Kim J, Srivastava RK (2000) Explaining context effects on choice using a model of comparative judgment. J. Consume Psych. 9(3):167–177.

Bleier A, Eisenbeiss M (2015) The importance of trust for personal ized online advertising. J. Retailing 91(3):390–409.

Boag P (2021) 5 ways to overcome choice paralysis and improve conversion. Accessed August 30, 2022, https://www.shopify.com partners/blog/choice-paralysis.

Bonaccio S, Dalal RS (2006) Advice taking and decision-making: An integrative literature review, and implications for the organizational sciences. Organ. Behav. Human Decision Processes 101(2): 127–151.

Brown SA, Venkatesh V, Goyal S (2014) Expectation confirmation in information systems research: A test of six competing models. MIS Quart. 38(3):729–756.

Burgman MA (2016) Trusting Judgements: How to Get the Best Out of Experts (Cambridge University Press, Cambridge, UK).

Business Insider (2021) Context is often the most influential factor driving consumer choices, according to recent research. Here’s why. Accessed August 10, 2022, https://www.businessinsider.com/sc/ how-context-influences-consumer-shopping-decisions-2021-1.

Chernev A, Bo¨ckenholt U, Goodman J (2015) Choice overload: A conceptual review and meta-analysis. J. Consumer Psych. 25(2): 333–358.

ChoiceHacking (2020) The choice overload effect: Why simplicity is the key to winning customers. Accessed August 10, 2022, https://www.choicehacking.com/2020/07/08/the-choice-over load-effect/.

Clark JK, Evans AT (2014) Source credibility and persuasion: The role of message position in self-validation. Personality Soc. Psych. Bull. 40(8):1024–1036.

Cooke ADJ, Sujan H, Sujan M, Weitz BA (2002) Marketing the unfamiliar: The role of context and item-specific information in electronic agent recommendations. J. Marketing Res. 39(4):488–497.

Czapin´ ski J, Lewicka M (1979) Dynamics of interpersonal attitudes: Positive–negative asymmetry. Political Psych. Bull. 10(1):31–40.

Design for Growth (2020) Are you using the decoy effect in your favour? Accessed July 29, 2021, http://pony.studio/design-forgrowth/decoy-effect.

Dooley R (2019) Decoy marketing. Accessed August 10, 2022, https://www.neurosciencemarketing.com/blog/articles/decoymarketing.htm.

Dooms S, De Pessemier T, Martens L (2013) Movietweetings: A movie rating dataset collected from Twitter. Workshop Crowdsourcing Human Comput. Recommender Systems (CrowdRec at RecSys) (ACM, New York), 43.

Evdelo (2020) Amazon’s recommendation algorithm drives 35% of its sales. Accessed August 10, 2022, https://evdelo.com/ama zons-recommendation-algorithm-drives-35-of-its-sales/

Fitzsimons GJ, Lehmann DR (2004) Reactance to recommendations: When unsolicited advice yields contrary responses. Marketing Sci. 23(1):82–94.

Frederick S, Lee L, Baskin E (2014) The limits of attraction. J. Market ing Res. 51(4):487–507.

Gai PJ, Klesse AK (2019) Making recommendations more effective through framings: Impacts of user- vs. item-based framings on recommendation click-throughs. J. Marketing 83(6):61–75.

Goled S (2021) Inside Netflix’s recommendation engine. Accessed December 19, 2022, https://analyticsindiamag.com/inside-netfli xs-recommendation-engine/.

Hedgcock W, Rao AR, Chen H (2009) Could Ralph Nader’s entrance and exit have helped Al Gore? The impact of decoy dynamics on consumer choice. J. Marketing Res. 46(3):330–343.

Heesacker M, Petty RE, Cacioppo JT (1983) Field dependence and attitude change: Source credibility can alter persuasion by affecting message-relevant thinking. J. Personality 51(4):653–666.

Herlocker JL, Konstan JA, Terveen LG, Riedl JT (2004) Evaluating col laborative filtering recommender systems. ACM Trans. Inform. Systems 22(1):5–53.

Herne K (1997) Decoy alternatives in policy choices: Asymmetric domination and compromise effects. Eur. J. Political Econom. 13(3):575–589

Hirsh JB, Kang SK, Bodenhausen GV (2012) Personalized persuasion: Tailoring persuasive appeals to recipients’ personality traits. Psych. Sci. 23(6):578–581.

Ho SY, Bodoff D (2014) The Effects of web personalization on user attitude and behavior: An integration of the elaboration likelihood model and consumer search theory. MIS Quart. 38(2):492–520.

Ho SY, Lim KH (2018) Nudging moods to induce unplanned purchases in imperfect mobile personalization contexts. Management Inform. Systems Quart. 42(3):757–778.

Ho SY, Bodoff D, Tam KY (2011) Timing of adaptive web personalization and its effects on online consumer behavior. Inform. Sys tems Res. 22(3):660–679.

Huber J, Puto C (1983) Market boundaries and product choice: Illustrating attraction and substitution effects. J. Consumer Res. 10(1):31–44.

Huber J, Payne JW, Puto C (1982) Adding asymmetrically dominated alternatives: Violations of regularity and the similarity hypothesis. J. Consumer Res. 9(1):90–98.

Iyengar SS, Lepper MR (2000) When choice is demotivating: Can one desire too much of a good thing? J. Personality Soc. Psych. 79(6):995.

Kawaguchi K, Uetake K, Watanabe Y (2019) Effectiveness of prod uct recommendations under time and crowd pressures. Marketing Sci. 38(2):253–273.

Komiak SY, Benbasat I (2006) The effects of personalization and familiarity on trust and adoption of recommendation agents. Management Inform. Systems Quart. 30(4):941–960.

Kumkale GT, Albarrac´ın D, Seignourel PJ (2010) The effects of source credibility in the presence or absence of prior attitudes: Implications for the design of persuasive communication campaigns. J. Appl. Soc. Psych. 40(6):1325–1356.

Lankton N, McKnight DH, Thatcher JB (2014) Incorporating trustin-technology into expectation disconfirmation theory. J. Strategic Inform. Systems 23(2):128–145.

Li SS, Karahanna E (2015) Online recommendation systems in a B2C e-commerce context: A review and future directions. J. Assoc. Inform. Systems 16(2):72–107.

Linder M (2018) Make e-commerce more human to cure choice overload. Accessed August 30, 2022, https://www.mytotalretail. com/article/make-online-shopping-more-human-to-cure-choice overload/.

Long X, Sun J, Dai H, Zhang DJ, Zhang J, Chen Y, Hu H, et al. (2022) The choice overload effect in online recommender systems: Theoretical framework and field experiment. Working paper.

Luce RD (2012) Individual Choice Behavior: A Theoretical Analysis (Courier Corporation, Chelmsford, MA).

Mathias J, Dietmar J (2021) Digital nudging with recommender systems: Survey and future directions. Comput. Human Behav. Rep 3(2021):100052.

Meltzer R (2022) How Netflix utilizes data science. Accessed August 22, 2022, https://www.lighthouselabs.ca/en/blog/how-netflixuses-data-to-optimize-their-product

Mishra S, Umesh UN, Stem DE (1993) Antecedents of the attraction effect: An information-processing approach. J. Marketing Res. 30(3):331–349.

O’Keefe DJ, Jackson S (1995) Argument quality and persuasive effects: A review of current approaches. Argumentation Values: Proc. 9th Alta Conf. Argumentation (Speech Communication Association, Annandale, VA), 88–92.

Page A (2021) 5 ways to use cognitive bias to your e-commerce or retail store’s advantage. Accessed August 30, 2022, https:// www.agiliron.com/blog/2021/07/5-ways-to-use-cognitive-biasto-your-ecommerce-or-retail-stores-advantage/.

Petty RE (2018) Attitudes and Persuasion: Classic and Contemporary Approaches (Routledge, London).

Petty RE, Cacioppo JT (1979) Issue involvement can increase or decrease persuasion by enhancing message-relevant cognitive responses. J. Personality Soc. Psych. 37(10):1915.

Petty RE, Cacioppo JT (1984) The effects of involvement on responses to argument quantity and quality: Central and peripheral routes to persuasion. J. Personality Soc. Psych. 46(1):69.

Pornpitakpan C (2004) The persuasiveness of source credibility: A critical review of five decades’ evidence. J. Appl. Soc. Psych. 34(2):243–281.

Radova K (2022) The decoy effect: Everything you need to know. Accessed August 14, 2022, https://insidebe.com/articles/thedecoy-effect/.

Ricci F, Rokach L, Shapira B (2015) Recommender Systems: Introduction and Challenges. Recommender systems handbook (Springer, New York), 1–34.

Robson D (2019) The trick that makes you overspend. Accessed August 14, 2022, https://www.bbc.com/worklife/article/20190801-thetrick-that-makes-you-overspend.

Salazar K, Moran K (2019) The dangers of overpersonalization. Accessed July 27, 2022, https://www.nngroup.com/articles/ overpersonalization/.

Scheibehenne B, Greifeneder R, Todd PM (2010) Can there ever be too many options? A meta-analytic review of choice overload. J. Consumer Res. 37(3):409–425.

Schneider C, Weinmann M, Vom Brocke J (2018) Digital nudging: Guiding online user choices through interface design. Comm. ACM 61(7):67–73.

Schumpe BM, Be´langer JJ, Nisa CF (2020) The reactance decoy effect: How including an appeal before a target message increases persuasion. J. Personality Soc. Psych. 119(2):272–292.

Sharif MA, Oppenheimer DM (2021) The effect of categories on relative encoding biases in memory-based judgments. Organ. Behav. Human Decision Processes 162(2021):1–8.

Sharma I (2020) How to make more profit with decoy effect. Accessed September 5, 2021, https://medium.com/global-startup-corner/ how-to-make-more-profit-with-decoy-effect-f97b8f08aeec.

Shen A (2014) Recommendations as personalized marketing: Insights from customer experiences. J. Service Marketing 28(5):418–427.

Shrupti S, John O, Jim G, Jane H (2019) Nudging for good. Accessed June 30, 2021, https://www2.deloitte.com/content/www/us/ en/insights/industry/public-sector/government-trends/2020/ government-nudge-thinking.html.

Simonson I (1989) Choice based on reasons: The case of attraction and compromise effects. J. Consumer Res. 16(2):158–174.

Simonson I (2014) Vices and virtues of misguided replications: The case of asymmetric dominance. J. Marketing Res. 51(4):514–519.

Simonson I, Tversky A (1992) Choice in context: Tradeoff contrast and extremeness aversion. J. Marketing Res. 29(3):281–295.

Stewart N, Brown GD, Chater N (2005) Absolute identification by relative judgment. Psych. Rev. 112(4):881.

Stoffel ST, Yang J, Vlaev I, von Wagner C (2019) Testing the decoy effect to increase interest in colorectal cancer screening. PLoS One 14(3):e0213668.

Sue O’Curry YP, Pitts R (1995) The attraction effect and politica choice in two elections. J. Consumer Psych. 4(1):85–101.

Swol LM, Sniezek JA (2005) Factors affecting the acceptance of expert advice. British J. Soc. Psych. 44(3):443–461.

Tabachnick BG, Fidell LS, Ullman JB (2007) Using Multivariate Statis tics (Pearson, Boston).

Tam KY, Ho SY (2005) Web personalization as a persuasion strategy: An elaboration likelihood model perspective. Inform. Systems Res. 16(3):271–291.

Tam KY, Ho SY (2006) Understanding the impact of web personali zation on user information processing and decision outcomes. Management Inform. Systems Quart. 30(4):865–890.

Thaler RH, Sunstein CR (2009) Nudge: Improving Decisions About Health, Wealth, and Happiness (Penguin, London).

The Decision Laboratory (2021) The decision laboratory. Accessed July 29, 2021, https://thedecisionlab.com/biases/decoy-effect/.

Theocharous G, Healey J, Mahadevan S, Saad M (2019) Personalizing with human cognitive biases. Accessed August 13, 2022, https://research.adobe.com/publication/personalizing-with-hu man-cognitive-biases.

Thomadsen R, Rooderkerk RP, Amir O, Arora N, Bollinger B, Hansen K, John L, et al. (2018) How context affects choice. Customer Needs Solutions 5(1):3–14.

Todorovic ´ D (2010) Context effects in visual perception and their explanations. Rev. Psych. 17(1):17–32.

Tomer Hochma (2017) Decoy effect: A complete practical guide to the psychological pricing and marketing hack. Accessed July 29, 2021, http://humanhow.com/the-decoy-effect-complete-guide/.

Tormala ZL, Petty RE (2004) Source credibility and attitude certainty: A metacognitive analysis of resistance to persuasion. J. Consumer Psych. 14(4):427–442.

Tsekouras D, Dellaert BG, Donkers B, Ha¨ubl G (2019) Product set granularity and consumer response to recommendations. J. Acad. Marketing Sci. 48(2):186–202.

Tversky A, Simonson I (1993) Context-dependent preferences. Man agement Sci. 39(10):1179–1189.

Wang X, Du X (2018) Why does advice discounting occur? The combined roles of confidence and trust. Frontiers Psych. 9(2018):238

Wu C, Cosguner K (2020) Profiting from the decoy effect: A case study of an online diamond retailer. Marketing Sci. 39(5): 974–995.

Wu L, Liu P, Chen X, Hu W, Fan X, Chen Y (2020) Decoy effect in food appearance, traceability, and price: Case of consumer preference for pork hindquarters. J. Behav. Experiment. Econom. 87(2020):101553.

Xiao B, Benbasat I (2007) E-commerce product recommendation agents: Use, characteristics, and impact. Management Inform. Systems Quart. 31(1):137–209.

Xiao B, Benbasat I (2018) An empirical examination of the influence of biased personalized product recommendations on consumers decision-making outcomes. Decision Support Systems 110(2018): 46–57.

Yagoda B (2018) The cognitive biases tricking your brain. Accessed August 14, 2022, https://www.theatlantic.com/magazine/archive/ 2018/09/cognitive-bias/565775/.

Yang S, Lynn M (2014) More evidence challenging the robustness and usefulness of the attraction effect. J. Marketing Res. 51(4): 508–513.

C<sub>opy</sub>ri<sub>g</sub>ht 2023 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
