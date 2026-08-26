---
otero_id: 13152
otero_key: "APKAA7D3"
title: "Assessing the Unacquainted: Inferred Reviewer Personality and Review Helpfulness"
authors: "Angela Xia Liu; Yilin Li; Sean Xin Xu"
year: "2021"
journal: "MIS Quarterly"
doi: "10.25300/misq/2021/14375"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# ASSESSING THE UNACQUAINTED: INFERRED REVIEWER PERSONALITY AND REVIEW HELPFULNESS<sup>1</sup>

Angela Xia Liu Belk College of Business, University of North Carolina at Charlotte Charlotte, NC, U.S.A. {xliu44@uncc.edu}

Yilin Li and Sean Xin Xu

School of Economics and Management, Tsinghua University Beijing, CHINA {liyl.16@sem.tsinghua.edu.cn} {xuxin@sem.tsinghua.edu.cn}

This work examines the question of who is more likely to provide future helpful reviews in the context of online product reviews by synergistically using personality theories and data analytics. It trains a deep learning model to infer a reviewer’s personality traits. This enables analyses to reveal the role of personality traits in review helpfulness among a large population of reviewers. We develop hypotheses on how personality traits are associated with review helpfulness, followed by hypotheses testing that confirms that higher review helpfulness is related to higher openness, conscientiousness, extraversion and agreeableness and to lower emotional stability. These results suggest the appropriateness of using these five personality traits as inputs for developing a model for predicting future review helpfulness. Based on an ensemble model using supervised classification algorithms, we develop a predictive model and demonstrate its superior performance. Theoretical and practical implications are discussed.

Keywords: Review helpfulness, personality, natural language processing, convolutional neural networks, machine learning, prediction

## Introduction

Recent years have witnessed an explosion of machine learning (e.g., neural network), aiding many advances in science and technology. One of the most exciting applications of machine learning has been the development of assessment tools to quantify individuals and predict human behavior (Brynjolfsson et al. 2016; Song et al. 2010). Traditional ways of assessing the traits of unacquainted people include surveys and interviews, which require substantial manual effort and cannot be done instantaneously. Currently, data scientists leverage increasingly rich online data to infer various aspects of people at zero acquaintance (Varian 2014). For instance, an individual’s personality can be inferred based on that person’s social networking activities (Youyou et al. 2015) or by natural language processing (NLP) techniques that analyze the individual’s writing (Adamopoulos et al. 2018). Such techniques have widespread implications for business. For example, marketing managers can analyze the textual content that unacquainted people leave online, assess their personalities, and design promotion packages at the individual level based on individual personality and/or personality profiles. The capital market enthusiastically embraces such techniques (Graves and Matz 2018). Research that documents the business value of these techniques is necessary (e.g., Gong et al. 2018 and Meyer et al. 2014; also see the recent MIS Quarterly Call for Papers on Managing AI). It is important to answer this call for research because relevant evidence can influence the attitudes of managers, investors, and scientists toward those techniques (Davenport 2015). We conduct research in this important area. Our research context is consumer-generated product reviews. We use a novel approach to assess reviewers’ personalities based on their review texts using a deep learning-based NLP model and then investigate the predictive power of the inferred personality for their future reviews. Below, we introduce what we do, what is new, and how we do it.

## Research Context and Motivations

Today’s consumers rely heavily on product review platforms (e.g., Yelp, TripAdvisor, Epinions) to obtain information about a variety of products and services (Forman et al. 2008; Ghose and Ipeirotis 2011). The number of reviews on a typical review platform is extremely high, sometimes overwhelmingly high, but the quality of those reviews varies substantially (Liu and Karahanna 2017). Consumers looking for needed information on a review platform bear a high mental burden when sorting through the reviews (Yin et al. 2014), which seriously hampers the value of these platforms (Chen and Xie 2008). Thus, a critical and challenging undertaking for product review platforms is to identify who will provide helpful reviews<sup>2</sup> and then encourage those reviewers to supply more reviews for the benefit of users. To illustrate, Taobao—one of the world’s largest e-commerce sites with 500 million registered users—launched a reviewreward scheme that offered coupons to reviewers. The scheme was found to be rather ineffective, however, because it is hard to predict the value of the reviews generated in exchange for the rewards (Cabral and Li 2015). Identifying who will provide helpful reviews is a challenging undertaking because a review platform typically has virtually no acquaintance (detailed information or personal interaction) with most of the reviewers.

We propose to inform review platforms of unacquainted reviewers’ personalities as an antecedent, or predictor, of review helpfulness. According to psychology research, personality plays a central role in describing a person and is considered to be the most fundamental dimension of variation among humans (McCrae and John 1992). Personality influences individual performance in various settings (e.g., Agarwal and Karahanna 2000; Poropat 2009; Venkatesh et al. 2014), one of which is information processing and sharing (e.g., DeYoung and Gray 2009; Muscanell and Guadagno 2012; Narvaez et al. 2006; Pacini and Epstein 1999). Generating and sharing product review information generally falls within that domain. As theorized below, three streams of literature—(1) knowledge sharing propensity, (2) reviewer persuasiveness, and (3) opinion leadership propensity—provide strong theoretical grounds for linking personality traits to review helpfulness.

Focusing on a reviewer’s personality inferred from existing review texts captures a salient factor in the research context. One of the characteristics of online product review platforms is the lack of face-to-face human interaction because the interactions are made mainly by communications through text. Visual and auditory cues, such as physical proximity, physical appearance, facial expressions, and auditory linguistic markers (e.g., tone, accent) that help people assess another person’s hidden characteristics (e.g., personality) in offline settings are absent or minimized. To help fill that void, natural language processing algorithms can convert the available information in a review platform—review texts— into an evaluation of reviewer personality that, as noted earlier, is proposed as an antecedent of review helpfulness.

## Contributions to the Product Review Literature and Actionable Implications

Prior research provides insights into factors explaining review helpfulness. (See Appendix A for a literature review.) The literature focuses mainly on review characteristics, such as review length, depth, readability, subjectivity, and sentiments. Some recent research pays attention to reviewer characteristics. One reviewer characteristic found to be a useful explanatory variable for review helpfulness is the number of helpfulness votes that reviewers have received for past reviews. This serves as a proxy for reviewer reputation/expertise but, in practice, it may take a long time for such information to surface after reviews are posted—i.e., one must wait for readers to vote (Huang et al. 2015).

Figure 1 distinguishes what we propose in this work from the prior research. Based on the rich evidence from existing literature about which characteristics of a review can influence review helpfulness, managers can use these characteristics to scrutinize existing reviews and find the helpful ones (e.g., Ghose and Ipeirotis 2011). A related but distinct question is: Who will provide future helpful reviews? According to prior literature, reviewer expertise—as proxied by the helpfulness votes for the reviewer’s previous reviews—can predict the helpfulness of the reviewer’s future reviews. This proxy, however, as noted earlier, usually takes a long time to emerge because of the time it takes for readers to leave feedback on the reviews (as illustrated in Figure 1).

This work takes a different approach and proposes using inferred reviewer personality to predict future review helpfulness. Psychologists maintain that personality remains stable for adults and, even if personality changes, it changes slowly (Costa and McCrae 2006). Thus, personality traits inferred from prior behaviors can serve as antecedents for predicting future behaviors—in our case, writing helpful or unhelpful reviews.

![](/api/attachments/APKAA7D3/fulltext/images/1a5595a2db09a0b9f1fb92cf9bd13daaa30df3f43f0a757950c7120a136a415f.jpg)  
Figure 1. Comparison of this Study and Prior Literature

A notable feature of our approach is that we use a deep learning-based NLP model to assess reviewers’ personality traits based on the reviewer’s existing reviews. This complements the traditional social science method of using surveys or interviews to assess personality. By using the NLP model, an information system (IS) can be designed to assess a reviewer’s personality automatically and instantaneously. This system can assess a reviewer’s personality at zero acquaintance as soon as the reviewer posts a review, making it possible to predict the helpfulness of the reviewer’s future reviews without the need to wait for readers’ appraisal of the reviewer’s review expertise. This adds a new piece of “invention” work from a design science perspective (Gregor and Hevner 2013) and provides practical and actionable implications for review platforms. <sup>3</sup>

## Research Design

Our research essentially advocates a novel NLP approach to operationalize writers’ (i.e., reviewers’) personalities in the context of online product reviews. Our research design is grounded in the notion of “operationalization” in the design science research, which includes two cohesive and complementary parts (Huang et al. 2018): (1) development of an IT artifact (a deep learning-based NLP model) to quantify reviewer personalities, and (2) evaluation of the IT artifact by predicting an outcome (future review helpfulness). We illustrate our research design in Figure 2 below and elaborate on it below.

Step 1: Train a deep learning model for personality. In our research context, the development of an IT artifact means training a leading-edge deep learning model to infer writers’ personality traits from texts (Majumder et al. 2017). Using a convolutional neural network, this model can infer a writer’s personality traits. We then evaluated the predictive power of the inferred personalities for predicting future review helpfulness in Steps 2 through 4.

Step 2: Theorizing and testing. We hypothesized how reviewer personality traits relate to review helpfulness. We then used a large dataset of Yelp reviews (Yelp Academic Dataset) to test the theorized relationships. Specifically, we regressed review helpfulness on the inferred reviewer personality traits (obtained at Step 1) on two thirds of the reviewers in the dataset.

![](/api/attachments/APKAA7D3/fulltext/images/f51c64893dbf57c9ae603cb82f569b1de2a39f8f78156ae2024f875cf57c1f92.jpg)  
Step 3: Train a predictive model. We trained a predictive model (for predicting review helpfulness) by integrating several ensemble machine learning techniques—ensemble support vector machine (E-SVM), random forest (RF), and adaptive boosting (AdaBoost)—using the same two thirds of the reviewers as in Step 2. The input variables used for training are what we found to be significant explanatory variables (for explaining review helpfulness) in the previous “theorizing and testing” step. This design responds to the recent call for research in the IS discipline to use theory and data synergistically and is grounded in a stream of machine learning research on variable selection, as elaborated below.

Scholars advocate that theory can provide powerful guidance on variable selection or conceptual framework construction in conjunction with machine learning techniques (e.g., Einav and Levin 2014; Varian 2014). To that end, having a strong theoretical foundation for identifying predictors of review helpfulness is critical because it is theory that helps ensure generalizability. Our research design thus devotes Step 2 to the theoretical development that relates review helpfulness to personalities and that guides variable selection for the prediction at Step 3. This design is consistent with suggestions by a seminal machine learning study (Guyon and Elisseeff 2006) on the selection of input variables for training a predictive model. The study submits that linear models (e.g., correlation and regression) are useful approaches for evaluating the relevance of candidate input variables. Machine learning techniques are often concerned with modeling complex relationships, but they are widely criticized for being a “black box” and for the possibility of overfitting (Domingos 2012; Koh and Liang 2017; Zeiler and Fergus 2014). Linear models are useful in terms of selecting the most relevant input variables for the outcome variable. Focusing on a set of selected input variables based on theories or domain knowledge helps preempt overfitting and facilitates data understanding (Guyon and Elisseeff 2006). Studies in various scientific areas (e.g., Cheng et al. 2006; Pal 2012; Pant et al. 2014) have followed this suggestion and, when selecting input variables for training a predictive model, have first regressed the outcome variable to be predicted on a set of candidate input variables from which they selected statistically significant explanatory variables of the regression as input variables for subsequent predictions. We followed this approach.

Step 4: Evaluation of predictive power. We used the remaining one third of the reviewers in our dataset to evaluate using inferred reviewer personality to predict the helpfulness of future reviews. Specifically, we used the first N reviews (N is a small number such as one or two) to infer a reviewer’s personality and then, based on the predictive model trained at Step 3, predicted the helpfulness of the reviewer’s future reviews. We then compared the recall and precision rates with those from a benchmark model. In doing so, we follow an established line of business practices that first uses people’s past behavior tracks to infer their traits (e.g., personality) that then are used to predict their future behaviors, thus providing bases for personalized targeting or marketing.<sup>4</sup> Given that personality traits are relatively stable over time (e.g., Costa and McCrae 2006), it is reasonable to expect that personality traits reflected in the first N reviews of a reviewer will carry over to the reviewer’s future reviews and thus impact the helpfulness votes of those future reviews. In particular, we advocate using a person’s parsimonious data (e.g., the first one or two reviews) to predict the person’s future behaviors (e.g., writing helpful reviews in the future), which can generate useful implications for practice (Kristensen et al. 2017).

## Hypotheses

We hypothesize relationships between reviewer personality and review helpfulness through three mechanisms: (1) knowledge sharing, (2) reviewer persuasiveness, and (3) opinion leadership. First, we assume that people with higher knowledge sharing propensity—more broadly, those who are intrinsically more willing to help others (Bock et al. 2005)—are more likely to provide reviews that contain knowledge (i.e., facts, information, and skills acquired by a person through experience or education) that will be more helpful to consumers in general, thus leading to more helpfulness votes.

Second, we anticipate that highly persuasive people induce others to agree with them because they are able to communicate information efficiently and effectively. It has long been established in most persuasion theories that personality traits play an important part in the persuasion process (e.g., Bostrom 1983), therefore reviewers with higher scores on traits that are positively linked to persuasiveness should be more likely to harvest more helpfulness votes on their reviews.

Third, opinion leadership is the process by which one person informally influences the attitudes or actions of another person informally (Tyagi and Kumar 2004). In the internet era when consumers have convenient access to multiple sources of information, including peer evaluations of products or businesses, the role of opinion leaders (i.e., consumers who exert a stronger influence on the attitudes and behaviors of other consumers than vice versa—Rogers

2003, chap. 8) has become salient. Opinion leaders facilitate consumers’ decision-making because they help consumers reduce uncertainty about their choices (Nair et al. 2010). At the same time, opinion leadership brings more credibility to their reviews. Our overarching idea is that personality traits positively associated with knowledge sharing propensity, reviewer persuasiveness, and opinion leadership are likely to increase review helpfulness.

Although there are different theories regarding personality, the Big Five personality traits model has a strong theoretical and practical foundation and has gained widespread acceptance across disciplines. It describes personality using five traits—openness to experience, conscientiousness, extraversion, agreeableness, and emotional stability— derived from factor analyses of a large number of self- and peer reports on personality-relevant adjectives and questionnaire items (Costa and McCrae 1994; McCrae and John 1992). The Big Five traits model provides a general taxonomy of personality traits and “serves an integrative function because it can represent the various and diverse systems of personality description in a common framework” (John and Srivastava 1999, p. 3). Table 1 describes these five personality traits in detail.

## Openness

Openness, also known as openness to experience, is characterized by active imagination, aesthetic sensitivity, attentiveness to inner feelings, preference for variety, and intellectual curiosity (McCrae and Costa 2003). Persons high in openness are more imaginative, curious, reflective, creative, and open-minded; therefore, they are more accepting of changes and also experience both positive and negative emotions more keenly (Matzler et al. 2008). In contrast, those lower in openness are considered to be conventional. They are bounded by traditions or familiar routines, are less open to new experiences, and generally have a narrower range of interests.

It is well established in the literature that openness to experience is positively related to knowledge sharing or knowledge exchange (e.g., Cabrera et al. 2006; Mooradian et al. 2006; Wang and Yang 2007). Individuals high in openness tend to have a high level of curiosity and enjoy seeking others' ideas and insights (Cabrera et al. 2006). Further, open individuals are more willing to transfer new skills and behaviors learned in one domain to benefit another (Wayne et al. 2004).

<table><tr><td colspan="2">Table 1. The Big Five Personality Traits</td></tr><tr><td>Trait</td><td>Description</td></tr><tr><td>Openness</td><td>Describes the breadth, depth, originality, and complexity of an individual&#x27;s mental and experiential life. Individuals high in openness are knowledgeable, perceptive, and analytical; they seek out experiences and are more artistic and investigative.</td></tr><tr><td>Conscientiousness</td><td>Describes the ability to control impulses to facilitate task- and goal-directed behavior. Those high in this trait follow norms and rules and are efficient at planning, organizing, and prioritizing tasks.</td></tr><tr><td>Extraversion</td><td>Describes an energetic and enthusiastic approach to the social and material world and includes traits, such as sociability, assertiveness, confidence, and positive emotionality.</td></tr><tr><td>Agreeableness</td><td>Describes a person&#x27;s level of altruism, cooperation, willingness to conform to group norms, trust, and modesty.</td></tr><tr><td>Emotional Stability</td><td>Contrasts with neuroticism, which features feelings of anxiety, nervousness, and depression. Those low in this trait are self-conscious, moody, impulsive, and prone to stress.</td></tr></table>

Note: Adapted from John et al. (2008).

Therefore, those individuals are likely to develop more expertise that enables them to give helpful advice and share their knowledge (Constant et al. 1996). Based on this argument, we expect persons high in openness will be more engaged in seeking and contributing knowledge and, in our setting, those persons would be expected to write more helpful reviews.

Openness to experience has also been shown to be positively associated with a person’s persuasiveness (Oreg and Sverdlik 2014). Conger (1998, p. 87) states that “effective persuaders seem to share a common trait: they are openminded, never dogmatic,” which enables them to bring forth creative arguments for their positions in persuasion (Oreg and Sverdlik 2014). Also, it is more likely that those high in openness “will engage targets, address their concerns, and at the same time help targets see their own (i.e., the source’s) perspective” because they are open to new ideas and are willing to take other’s perspectives (Oreg and Sverdlik 2014, p. 252). Therefore, it can be expected that reviewers high in openness will be more persuasive and, as a result, will obtain more helpful votes on their reviews.

Characteristics associated with openness also suggest opinion leadership: like opinion leaders, those high in openness are intellectually curious and likely to be interested in exploring new and unusual ideas (John et al. 2008). Opinion leaders are generally more innovative (Goldsmith et al. 2006; Ruvio and Shoham 2007) and well-informed about new developments in their areas of interest (Gnambs and Batinic 2012). Therefore, they are more likely to try different products and brands within their product class (Coulter et al. 2002). As noted above, open individuals are likely to develop more expertise, particularly with topics within their domains of influence. A high level of knowledge is typically a necessary characteristic for an opinion leader. Therefore, we expect that reviewers high in openness will be more likely to become opinion leaders, meaning that their reviews will be perceived as more helpful. Given that openness is positively related to all three of the mechanisms—knowledge sharing, persuasiveness, and opinion leadership—that lead to higher helpfulness votes, we hypothesize:

H1: Reviewer openness is positively related to review helpfulness.

## Conscientiousness

Conscientiousness refers to an individual’s tendency to be organized and dependable, show self-discipline, act dutifully, aim for achievement, and follow established rules rather than behave spontaneously (McCrae and Costa 2003). It describes an individual’s capacity to control, regulate, and direct impulses, delay gratification, complete tasks, and work toward long-term goals. Highly conscientious individuals have characteristics such as orderliness, self-discipline, and reliability as opposed to disorganization, inefficiency, and inconsistency.

It is well-established that conscientiousness is positively associated with knowledge sharing propensity (e.g., Cabrera et al. 2006; Matzler et al. 2008; Mohammadi et al. 2013; Wang and Yang 2007). This can be attributed to the “act dutifully and aim for achievement” attribute of conscientious individuals; they are willing to do what is necessary, including sharing knowledge with others, in order to reach a goal or complete a task (Liao and Chuang 2004). Therefore, highly conscientious reviewers will likely have stronger incentives to share their detailed knowledge (e.g., consumption experiences, product assessments, comparisons to related products) when they want to convey a message, which should thus attract more helpfulness votes.

Conscientiousness may also influence review helpfulness through reviewer persuasiveness. Highly conscientious individuals are associated with consistency and commitment, two major components of persuasiveness (Mohammadi et al. 2013). Highly conscientious individuals are also characterized by orderliness and logic (McCrae and Costa 2003), which also typically contribute to effective persuasion. Hence, we expect a positive relationship between conscientiousness and persuasiveness and thus a positive relationship between conscientiousness and review helpfulness.

Conscientiousness may also impact review helpfulness through its positive association with opinion leadership. As mentioned above, conscientious individuals tend to act dutifully and aim for achievement. Mooradian et al. (2006) found that conscientious individuals are more prone to setting goals (i.e., intended achievements) and tend to do what is necessary to accomplish those goals. Colbert and Witt (2009) also confirm that conscientious individuals are likely to act dutifully regarding the goals they set. These are important characteristics of opinion leaders. For instance, Park (2013) finds that opinion leaders on Twitter are highly goal-oriented (a prominent goal on Twitter is to exert influence and steer changes in followers’ opinions) and have greater motivation to conduct “information seeking, mobilization, and public expression” (p. 1642). Reviewers with high conscientiousness therefore will be more likely to be associated with opinion leadership, which, in turn, should lead to higher review helpfulness. Thus, we hypothesize:

H2: Reviewer conscientiousness is positively related to review helpfulness.

## Extraversion

Extraversion refers to an individual’s pronounced engagement with the external world that can be characterized by two ends of a single continuum: sociable, outgoing, energetic, and assertive versus solitary, distant, reserved, and shy. Extroverts enjoy interacting with people and often are perceived as talkative, enthusiastic, and energetic. They tend to express positive emotions and often take charge in group situations. In contrast, introverts are quiet, calm, laid back, and less social people who prefer to keep their thoughts and feelings to themselves. They are also associated with characteristics such as being low-key, deliberate, and shy.

Extraversion is positively associated with knowledge sharing propensity. Extroverts are more likely to share knowledge because of their propensity toward talkativeness and enthusiasm (de Vries et al. 2006). Talkativeness leads to more conversations and information exchanges, i.e., more knowledge sharing opportunities. Enthusiasm contributes to eagerness to share knowledge with others (Wang and Yang 2007). Thus, extroverts possess both the ability and the passion to share their information and knowledge. In addition, because extroverts are positively affective and satisfied when working with teams (McCrae and Costa 2003), they will likely seek to increase knowledge sharing among group members to ensure that the team remains viable (Pei-Lee et al. 2017). Empirical research also confirms the positive relationship between extraversion and individuals’ intentions to share knowledge (e.g., de Vries et al. 2006; Wang et al. 2014). This might be due to the positive link between extraversion and the need to gain status (Barrick et al. 2005), which has been identified as a motivating factor for knowledge sharing (Ardichvili 2008). Therefore, being positively associated with knowledge sharing propensity, extroverts are expected to provide reviews that contain more knowledge, thus leading to more helpfulness votes.

Extraversion may also influence review helpfulness through persuasiveness. Among all personality traits, we regard extraversion as the most salient at influencing a person’s persuasiveness. Wheeler et al. (2005) found that extroverted persons are more persuasive. This can be attributed to a general tendency of extroverts to communicate with others, exchange their ideas, and make contacts (McCrae and Costa 2003). They also exhibit greater dominance and are more likely to establish their authority in group situations where authoritative persons enjoy high levels of compliance from others (Cohrs et al. 2012). Compared to introverts, extroverts typically are more communicative and exhibit an energetic and confident communication style (Gloor et al. 2010), which is a key element of successful persuasion. By being positively linked to persuasiveness, extroverts should be able to deliver information more effectively, thus leading to more helpfulness votes for their reviews.

Extraversion may also influence review helpfulness through its positive association with opinion leadership. Extraversion is a central characteristic of opinion leaders (Judge et al. 2002). To be an opinion leader, people need to be willing and able to share their opinions, which are characteristics of extroverts. Previous research on opinion leadership has found that, in general, opinion leaders are more talkative than their peers (Gnambs and Batinic 2012), have more friends (Karlsen 2015), are more gregarious, and are more socially active (Kavanaugh et al. 2006), which are all characteristics of extroverts as well. Like opinion leaders, extroverts are generally more likely to influence the attitudes and actions of others. This influence is manifested in facilitating others’ decision-making in the context of reading reviews and making purchasing decisions. By definition, facilitating others’ decision-making suggests high levels of review helpfulness (Mudambi and Schuff 2010). Hence, we hypothesize a positive relationship between review helpfulness and extraversion.

H3: Reviewer extraversion is positively related to review helpfulness.

## Agreeableness

Agreeableness is associated with characteristics such as cooperation, likeability, forgivingness, kindness, sympathy, and trust (McCrae and Costa 2003). Highly agreeable persons are generally more trusting, generous, sympathetic, cooperative, and are the opposite of aggressive or cold. Previous research has found a positive relationship between agreeableness and an individual’s knowledge sharing behavior (Matzler et al. 2008; Mooradian et al. 2006; Wang and Yang 2007). Highly agreeable individuals are defined as helpful, generous, cooperative, and supportive, making them more likely to collaborate effectively and help others by suggesting ideas or sharing knowledge (Witt et al. 2002). Agreeableness facilitates knowledge transfer and knowledge sharing because others are more likely to seek information from more agreeable (and thus more approachable) persons (Magnini 2008). Therefore, we expect reviewers high in agreeableness to be positively associated with knowledge sharing, thus resulting in higher helpfulness votes for their reviews.

We also expect that higher agreeableness leads to higher persuasiveness. Conger (1998, p. 87) states that to achieve effective persuasion, one should be able to test and revise one’s ideas in concert with other’s concerns and needs and posits “the best persuaders not only listen to others, but also incorporate their perspectives into a shared solution.” Such responsiveness and flexibility are rooted in the flexible and cooperative nature of individuals who are high in agreeableness. In addition, given their courteous, flexible, trusting, and sympathetic nature, such individuals are willing and able to adjust their viewpoints and incorporate others’ ideas in the persuasion process. When others learn about a persuader’s eagerness to hear their views and willingness to make changes in response to their needs and concerns, they are likely to respond very positively (Oreg and Sverdlik 2014, p. 252). This positive dynamic typically induces more effective persuasion, leading to higher votes on helpfulness. However, previous research suggests that agreeableness is independent of opinion leadership (Gnamb and Batinic 2012). Therefore, we argue that it is mainly through knowledge sharing and persuasiveness that the agreeableness of reviewers influences the number of helpfulness votes left on their reviews.

H4: Reviewer agreeableness is positively related to review helpfulness.

## Emotional Stability

Emotional stability and neuroticism represent two ends of a continuum, usually characterized by secure and confident versus sensitive and nervous (Eysenck 2013). Emotionally stable individuals tend to be calm, optimistic, and free from persistent negative feelings. They are less likely to get upset, are less emotionally sensitive, and can easily control their emotions. At the other end, neuroticism is linked with low tolerance for stress and other aversive stimuli. Those with high neuroticism are more likely to experience negative emotions or feel threatened, and their bad moods tend to last longer.

Prior studies on emotional stability suggest a negative relationship between emotional stability and review helpfulness. The literature shows that emotional stimuli (e.g., emotional words) influences message recipients’ subconscious judgments and reactions toward that message (Murphy and Zajonc 1993). Prior research has also established a positive link between emotion in a message and the message’s persuasiveness across various settings (Brader 2006; Clore and Gasper 2000; Frijda et al. 2000). Following this line of research, we expect that reviews with more emotional stimuli induce higher persuasiveness and thus higher helpfulness, as confirmed by previous research (e.g., Cao et al. 2011; Yin et al. 2014; also see our review in Appendix A). Since emotionally stable individuals are less likely to express intense emotions and are less likely to manage and channel emotions for persuasive purposes, we expect that people with high emotional stability (inferred from their reviews) would be less persuasive and that their messages—product reviews, in our research context— would be less helpful.

For the same reason, emotions in the review text may help establish a reviewer’s opinion leadership. Recent research suggests that expressing emotions may help people become effective leaders (George 2000), which also applies to online opinion leaders. By showing emotions, leaders can motivate and inspire people (Goleman et al. 2013) because emotional expression can help them set a vision, make tough decisions, learn from failure, build trust, and strengthen relationships (Sundheim 2013). Therefore, on an online review platform, reviewers expressing emotions (thus being classified as low in emotional stability) may be more strongly associated with opinion leadership, which would also lead to higher helpfulness for their reviews. Based on the above reasoning specific to the context of our research, we propose a negative relationship between review helpfulness and emotional stability.

However, it is worth noting another expectation about the relationship between review helpfulness and emotional stability. Previous research found that self-confidence and selfesteem are positively linked to opinion leadership (Clark and Goldsmith 2005). Individuals high in emotional stability are likely to possess self-confidence and self-esteem (Robins et al. 2001). Hence, one may expect people who are emotionally stable to be associated with high opinion leadership and, therefore, to produce helpful reviews. However, as stated above, there are reasons specific to our research context suggesting a negative relationship between review helpfulness and emotional stability. We thus hypothesize a negative relationship and note that it is an empirical issue deserving a systematic test in the context of online product reviews.

H5: Reviewer emotional stability is negatively related to review helpfulness.

## Data And Variables

## Data

We used the Yelp Academic Dataset,<sup>5</sup> which provides the business profiles, reviewer profiles, and review contents of the closest 250 businesses to 30 universities across 15 states in the U.S. (Ning and Karypis 2012; Rabinovich and Blei 2014). We focused on the “restaurant” category because it is the top business type on Yelp.<sup>6</sup> We removed reviews with fewer than 50 words because the NLP algorithm requires outputs from the Linguistic Inquiry and Word Count (LIWC) program, which calls for “a certain degree of skepticism” on any text containing fewer than 50 words ( http://liwc.wpengine.com/ how-itworks/).<sup>7</sup> Our final sample consists of 160,578 reviews written by 74,480 reviewers for 4,244 restaurants.

Each review on Yelp comprises a star rating, review text, review date, associated business ID, and reviewer ID. For each restaurant, we had information about its location, accumulated average rating, categories, and business name. For each reviewer, we had the reviewer’s Yelp name, the date the reviewer joined Yelp, the reviewer’s number of reviews, and the reviewer’s average restaurant star rating. We also crawled location information from each reviewer’s Yelp homepage.

## Variables

Review helpfulness is measured as the total number of helpfulness votes for each review.<sup>8</sup> Yelp allows readers to vote “yes” on the helpfulness of each review. Amazon, in contrast, allows readers to vote either “yes” or “no” on the helpfulness of each review. Accordingly, our helpfulness variable is a discrete number of total votes and differs from the review helpfulness variable in studies that use Amazon’s review data, which is the ratio of helpfulness votes (“yes”) to total votes (“yes” + “no” votes). Given how review helpfulness is measured in our study, we needed to control for how long a review has existed on Yelp because longer time periods give reviews a greater likelihood of accumulating up-votes (e.g., Berger and Milkman 2012; Godes and Silva 2012; Mudambi and Schuff 2010).

Personality traits: Following Majumder et al. (2017), we trained a leading-edge deep learning-based NLP model to calculate the personality trait scores based on the review text. This model uses word-to-vector, a word embedding technique, to convert reviews into specified-length feature sets that are then fed into a convolutional neural network (CNN) to be processed in a hierarchical manner by combining words into n-grams, ngrams into sentences, and sentences into a whole review text. Then, it uses multiple-layer perceptron (MLP) as a classifier to make judgments on personality traits. This CNN-based method has a network architecture with seven layers, where each layer refers to a step of data processing in the neural network algorithm. Those layers are: input, convolution, max pooling, concatenate, 1-max pooling, linear with Sigmoid activation, and two neuron softmax output, which can be further divided into the following four steps.

(1) Word vectorization is the first layer of this network, in which all the words are mapped to vectors of real numbers using wordembedding algorithms (specifically Google’s pre-trained word2vec embeddings). This step turns each word into a realvalued vector with a fixed length.

(2) Sentence vectorization includes the convolution, max pooling, and concatenation layers through which the outputs of the first step (i.e., the word vectors of each sentence) are combined into n-grams, and n-grams are further transformed into fixed-length sentence vectors.

(3) Document vectorization includes the next layer in the network structure, 1-max pooling. In this step, the outputs from the previous step are first converted into document vectors that integrate all sentence vectors at the document level by taking the max values across sentences at each dimension. Further, stylistic features (Mairesse 2007) are linked with the previous document vectors for each review in order to produce final document vectors for classification.

(4) Classification includes the last two layers, linear with Sigmoid activation and two-neuron softmax output. This step further transforms the document vector to the final classification result and the probabilities associated with it.

To train the model, we used the negative log-likelihood as the objective function and used stochastic gradient descent with the AdaDelta update rule (Zeiler 2012) to minimize the error defined by the objective function. This CNN-based NLP method was trained using James Pennebaker and Laura King’s stream-of-consciousness essay dataset that contains 2,467 valid writing essays tagged with the authors’ personality traits, which has outperformed the state-of-theart techniques for all five personality traits (Majumder et al. 2017). We describe the method in detail in Appendix B.

Given that the predicted personality traits are based on the review text, we further conducted a validation test to confirm that those traits measured in this way indeed reflect the reviewer’s traits rather than the review’s characteristics. We achieved this by comparing the variance of personality scores within the reviewers to that across reviewers. We found that for each of the five personality traits, the average variance within reviewers (for reviewers who wrote at least two reviews in our data) is indeed smaller than that across reviewers (0.00119 vs. 0.28089 for openness; 0.00199 vs. 0.09116 for consciousness; 0.00054 vs. 0.25657 for extraversion; 0.00059 vs. 0.30555 for agreeableness; 0.00086 vs. 0.30355 for emotional stability).

Control variables: We identified control variables based on the prior literature (as reviewed in Appendix A). Those controls belong to three groups: reviewer characteristics (other than personality traits), review characteristics, and product (restaurant) characteristics. These control variables have been widely examined in the literature. Appendix C contains the operationalization and justification details.

Table 2 summarizes our variables and provides descriptive statistics. In our sample, the average word count is 155 words, the average review stars is 3.53, and the average readability index (Colemanliau) is 8.4. Table 3 presents the correlation matrix between the main independent variables. As Table 3 shows, the absolute values of correlations between covariates are less than or equal to 0.59, well below the threshold of 0.8 (Judge et al. 1998, p. 868). Thus, multicollinearity is not likely a concern for our analyses. In particular, correlations among the five personality traits are not high, with the highest value being 0.21. This is consistent with observations in prior literature (e.g., Cabrera et al. 2006; Matzler et al. 2008).

## Hypotheses Testing

## Regression Model and Estimation

The regression model for hypotheses testing is as follows:

$$
\begin{array}{r l} H e l p f u l n e s s _ {i j} & = \beta_ {0} + \beta_ {1} (O p e n n e s s _ {i j}) \\ & + \beta_ {2} (C o n s c i e n t i o u s n e s s _ {i j}) \\ & + \beta_ {3} (E x t r a v e r s i o n _ {i j}) \\ & + \beta_ {4} (A g r e e a b l e n e s s _ {i j}) \\ & + \beta_ {5} (E m o t i o n \_ s t a b i l i t y _ {i j}) \\ & + \beta_ {6 - 2 2} (C o n t r o l s _ {i j}) + \varepsilon_ {i j} \end{array}\tag{1}
$$

where ?????????????????????? indicates the log transformed total number of helpfulness votes (plus 1) of a review written by reviewer i for restaurant j. We obtain the five personality trait scores by using the abovementioned CNN-based NLP method. However, in estimating the regression model, we need to address a concern about endogeneity that can be introduced by omitted variables. This is discussed in detail below.

Although we have included a comprehensive set of controls, there may be unobservable restaurant factors that influence both personality scores and helpfulness votes. For instance, when composing reviews for a well-known, standardized chain restaurant, such as McDonald’s or Wendy’s, a reviewer might write a shorter and less passionate review compared to a review written for an exotic restaurant that provides a unique experience. Such a difference in writing can result in different personality scores for the same reviewer because the scores are calculated based on the review texts. At the same time, reviews for McDonald’s may be less likely to receive helpfulness votes because consumers are already familiar with the standardized food and service. This example illustrates the possibility that unobservable restaurant characteristics could invalidate the assumption of independence between independent variables (personality scores) and the error term, giving rise to endogeneity concerning personality traits in Eq. (1).

We used an instrumental variables (IV) approach to address this concern. The key to this approach is to find instruments that provide an exogenous source of variation for the endogenous variables (personality traits). We constructed two sets of IVs; The first set is as follows. For a focal review, we (1) collected the reviewer’s “location” information, as reported on the reviewer’s Yelp homepage, (2) identified all reviewers from the same location, (3) found all reviews written by those reviewers but for different restaurants, and (4) computed average personality scores based on those reviews in Step 3. These average personality scores became the IVs we used.

<table><tr><td colspan="4">Table 2. Variable Operationalization and Statistics</td></tr><tr><td>Variable</td><td>Operationalization</td><td>Mean</td><td>SD</td></tr><tr><td colspan="4">Dependent variable</td></tr><tr><td>Helpfulness</td><td>Total number of helpfulness votes for the review (log transformed)</td><td>0.468</td><td>0.586</td></tr><tr><td colspan="4">Reviewer characteristics</td></tr><tr><td>Openness</td><td>Openness stability score calculated using CNN model (see Appendix B for details)</td><td>0.802</td><td>0.157</td></tr><tr><td>Conscientiousness</td><td>Conscientiousness score calculated using CNN model</td><td>0.090</td><td>0.096</td></tr><tr><td>Extraversion</td><td>Extraversion score calculated using CNN model</td><td>0.237</td><td>0.094</td></tr><tr><td>Agreeableness</td><td>Agreeableness stability score calculated using CNN model</td><td>0.240</td><td>0.110</td></tr><tr><td>Emotion_stability</td><td>Emotional stability score calculated using CNN model</td><td>0.593</td><td>0.164</td></tr><tr><td>Review_rank_user</td><td>Sequential order of the review among all reviews written by the reviewer</td><td>6.323</td><td>11.732</td></tr><tr><td>Local</td><td>Dummy to indicate whether the reviewer is local (reviewer&#x27;s location city is the same as restaurant&#x27;s location city)</td><td>0.707</td><td>0.455</td></tr><tr><td colspan="2">Review characteristics</td><td colspan="2"></td></tr><tr><td>Word_count</td><td>Number of words in a review</td><td>155</td><td>105</td></tr><tr><td>Star</td><td>Review rating, from 1 to 5 with half-star increments (demeaned)</td><td>3.533</td><td>1.169</td></tr><tr><td>Star_square</td><td>Square of (demeaned) star</td><td>1.381</td><td>1.839</td></tr><tr><td>Colemanliau</td><td>The Coleman-Liau Readability Index score for each review</td><td>8.404</td><td>1.791</td></tr><tr><td>Existing_days</td><td>Days between the date the review was published and the last date in the dataset</td><td>832</td><td>585</td></tr><tr><td>Positivity</td><td>LIWC Posemo measure, which is the percentage of positive emotion words in the review using LIWC dictionary</td><td>5.217</td><td>2.572</td></tr><tr><td>Negativity</td><td>LIWC Negemo measure, which is the percentage of negative emotion words in the review using LIWC dictionary</td><td>1.149</td><td>1.212</td></tr><tr><td colspan="2">Product (restaurant) characteristics</td><td colspan="2"></td></tr><tr><td>Business_star</td><td>Star rating for business, used as control for restaurant quality</td><td>3.576</td><td>0.518</td></tr><tr><td>Price_range</td><td>Number of dollar signs of the restaurant on Yelp, ranging from 1 to 4 (1: &lt;$10; 2: $11-$30; 3: $31-$60; 4: &gt;$60)</td><td>1.708</td><td>0.657</td></tr><tr><td>Review_rank_business</td><td>Sequential order of the review among all reviews the restaurant received (in thousands)</td><td>0.101</td><td>0.135</td></tr><tr><td>Cuisine_type</td><td colspan="3">1=American (51.3%); 2=Asian (18.6%); 3=European (9.0%); 4=South American (6.6%); 5=Middle Eastern (6.2%); 6=other (8.3%)</td></tr></table>

Table 3. Correlation Matrix

<table><tr><td colspan="2"></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td></tr><tr><td>1</td><td>Openness</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>Conscientiousness</td><td>-0.01***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>Extraversion</td><td>-0.09***</td><td>0.04***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>Agreeableness</td><td>-0.11***</td><td>0.12***</td><td>0.19***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>Emotion_stability</td><td>0.06***</td><td>0.04***</td><td>0.20***</td><td>0.21***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td>Review_rank_user</td><td>0.02***</td><td>-0.02***</td><td>-0.01**</td><td>0.01***</td><td>0.01*</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td>local</td><td>0.00</td><td>0.02***</td><td>0.00</td><td>-0.02***</td><td>-0.02***</td><td>-0.07***</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>8</td><td>Word_count</td><td>0.27***</td><td>-0.03***</td><td>-0.15***</td><td>-0.05***</td><td>-0.03***</td><td>0.05***</td><td>0.02***</td><td>1</td><td></td><td></td><td></td></tr><tr><td>9</td><td>Star</td><td>-0.01***</td><td>0.01**</td><td>0.15***</td><td>0.10***</td><td>0.09***</td><td>-0.03***</td><td>-0.02***</td><td>-0.07***</td><td>1</td><td></td><td></td></tr><tr><td>10</td><td>Star_square</td><td>-0.02***</td><td>0.02***</td><td>-0.07***</td><td>-0.11***</td><td>-0.11***</td><td>-0.07***</td><td>0.03***</td><td>0.06***</td><td>-0.59***</td><td>1</td><td></td></tr><tr><td>11</td><td>Colemanliau</td><td>0.14***</td><td>-0.09***</td><td>-0.08***</td><td>0.06***</td><td>0.08***</td><td>0.06***</td><td>-0.04***</td><td>0.09***</td><td>0.06***</td><td>-0.04***</td><td>1</td></tr><tr><td>12</td><td>Existing_days</td><td>-0.01**</td><td>0.00</td><td>0.02***</td><td>0.00</td><td>0.01**</td><td>0.04***</td><td>-0.10***</td><td>-0.05***</td><td>0.01**</td><td>-0.04***</td><td>0.02***</td></tr><tr><td>13</td><td>Positivity</td><td>0.01**</td><td>0.02***</td><td>0.16***</td><td>0.02***</td><td>0.08***</td><td>-0.04***</td><td>0.00</td><td>-0.21***</td><td>0.36***</td><td>-0.27***</td><td>0.05***</td></tr><tr><td>14</td><td>Negativity</td><td>-0.01***</td><td>-0.13***</td><td>-0.10***</td><td>-0.31***</td><td>-0.26***</td><td>0.01**</td><td>0.00</td><td>0.02***</td><td>-0.33***</td><td>0.31***</td><td>0.00</td></tr><tr><td>15</td><td>Business_star</td><td>0.00</td><td>0.01***</td><td>0.05***</td><td>0.04***</td><td>0.03***</td><td>-0.03***</td><td>0.02***</td><td>0.02***</td><td>0.40***</td><td>-0.20***</td><td>0.04***</td></tr><tr><td>16</td><td>Price_range</td><td>0.06***</td><td>-0.01***</td><td>-0.05***</td><td>0.02***</td><td>0.03***</td><td>-0.03***</td><td>-0.04***</td><td>0.15***</td><td>0.01**</td><td>0.00</td><td>0.08***</td></tr><tr><td>17</td><td>Review_rank_business</td><td>0.00</td><td>0.00***</td><td>0.01***</td><td>0.00</td><td>0.00</td><td>-0.08***</td><td>0.08***</td><td>0.01**</td><td>0.08**</td><td>-0.02***</td><td>-0.03***</td></tr></table>

<table><tr><td colspan="8">Table 3. Correlation Matrix (Continued)</td></tr><tr><td colspan="2"></td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td></tr><tr><td>12</td><td>Existing_days</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>13</td><td>Positivity</td><td>-0.05***</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>14</td><td>Negativity</td><td>0.03***</td><td>-0.23***</td><td>1</td><td></td><td></td><td></td></tr><tr><td>15</td><td>Business_star</td><td>-0.09***</td><td>0.14***</td><td>-0.15***</td><td>1</td><td></td><td></td></tr><tr><td>16</td><td>Price_range</td><td>-0.04***</td><td>0.11***</td><td>-0.03***</td><td>0.03***</td><td>1</td><td></td></tr><tr><td>17</td><td>Review_rank_business</td><td>-0.33***</td><td>0.04***</td><td>-0.02***</td><td>0.24***</td><td>0.08***</td><td>1</td></tr></table>

Note: \*p < 0.10; \*\*p < 0.05; \*\*\*p < 0.01.

These are valid IVs for two reasons. First, psychology research has found strong evidence for geographic variation in personality (Hofstede and McCrae 2004; McCrae and Terracciano 2005; Schmitt et al. 2008), suggesting that people from the same location tend to share a degree of similarity in personality traits.<sup>9</sup> Second, given our concern about unobservable restaurant characteristics, we computed the average personality scores of other reviewers who came from the same location as the focal reviewer but who wrote reviews for different restaurants. For instance, to find IVs for a New Yorker writing a review for a specific restaurant (e.g., Neptune Oyster in Boston, MA), we used the personality scores of all other New Yorkers who wrote reviews for other restaurants. This process is analogous to that provided in Chintagunta et al. (2010)—the personality traits of people from the same region (e.g., New York) are likely to have similar magnitudes; however, the personality traits inferred from reviews for other restaurants are unlikely to be correlated with the specific restaurant’s unobservable idiosyncratic characteristics, or the error term.

The second set of IVs comprises words per sentence and word percentage of auxiliary verbs (e.g., am, will, have) calculated by LIWC for each review. Those two variables were correlated with a writer’s personality traits (Hirsh and Peterson 2009; Mairesse et al. 2007; Yarkoni 2010) but because they are linked to the individual’s linguistic style instead of specific content (Tausczik and Pennebaker 2010), they are less likely to be correlated with a specific restaurant’s unobservable characteristics. Further, we conducted the Hansen’s J of overidentifying restrictions to ensure the validity of our instruments (Hansen 1982). The test statistics (J statistic = 4.243, p = 0.1198) do not reject the null hypothesis that the instruments are valid because they are not correlated with the error term and the excluded instruments are correctly excluded from the estimated equation, thus confirming the legitimacy of our instruments.

In addition to the IV approach, we conducted a generalized method of moments (GMM) estimation and used clustered standard errors. Although we addressed potential endogeneity by using instruments, we still faced potential violation of the assumptions of conditional homoscedasticity and independence. We used a GMM procedure with robust error specification that has been shown to be more efficient than the traditional IV/2SLS procedure (Greene 2003). Further, to account for the possibility that regression residuals are not independent within each restaurant, we specified the residuals as clustered under each restaurant.

## Results of Hypotheses Testing

We randomly assigned two thirds of all reviewers (and their reviews) to the training sample and the remaining one third to the testing sample. Table 4 reports the results of our model estimations on the training sample. The three columns show that the three different estimations—(1) IV regression as our base mode, (2) IV regression with GMM and robust error terms but without clustering in errors, and (3) IV regression with both GMM and clustered robust error terms—yielded fairly consistent results. It is worth noting that we examined IV strength and validity using the underidentification test, the weak identification test, the overidentification test of all instruments, and the test of endogeneity. These all strongly supported our IV approach. We report details of these tests in Appendix D. As Table 4 shows, we found positive coefficients for openness, conscientiousness, extraversion, and agreeableness and a negative coefficient for emotional stability.

<table><tr><td colspan="7">Table 4. Results of Hypotheses Testing</td></tr><tr><td></td><td colspan="2">(1) Base model</td><td colspan="2">(2) GMM</td><td colspan="2">(3) GMM + clustered S.E.</td></tr><tr><td colspan="7">Reviewer characteristics</td></tr><tr><td>Openness</td><td>1.440(0.649)</td><td>**</td><td>1.474(0.649)</td><td>**</td><td>1.683(0.724)</td><td>**</td></tr><tr><td>Conscientiousness</td><td>3.103(1.677)</td><td>*</td><td>3.171(1.677)</td><td>*</td><td>3.890(1.919)</td><td>**</td></tr><tr><td>Extraversion</td><td>2.550(1.484)</td><td>*</td><td>2.636(1.483)</td><td>*</td><td>2.872(1.587)</td><td>*</td></tr><tr><td>Agreeableness</td><td>4.466(1.597)</td><td>***</td><td>4.394(1.596)</td><td>***</td><td>4.403(1.722)</td><td>**</td></tr><tr><td>Emotion_stability</td><td>-3.041(1.067)</td><td>***</td><td>-3.021(1.067)</td><td>***</td><td>-2.785(1.134)</td><td>**</td></tr><tr><td>Review_rank_user</td><td>0.007(0.000)</td><td>***</td><td>0.007(0.000)</td><td>***</td><td>0.007(0.000)</td><td>***</td></tr><tr><td>Local</td><td>0.002(0.007)</td><td></td><td>0.002(0.007)</td><td></td><td>0.002(0.008)</td><td></td></tr><tr><td colspan="7">Review characteristics</td></tr><tr><td>Word_count</td><td>0.001(0.000)</td><td>***</td><td>0.001(0.000)</td><td>***</td><td>0.001(0.000)</td><td>***</td></tr><tr><td>Star</td><td>(0.000)(0.014)</td><td></td><td>-0.004(0.014)</td><td></td><td>-0.004(0.015)</td><td></td></tr><tr><td>Star_square</td><td>0.012(0.006)</td><td>**</td><td>0.012(0.006)</td><td>**</td><td>0.010(0.006)</td><td>*</td></tr><tr><td>Colemanliau</td><td>0.029(0.009)</td><td>***</td><td>0.030(0.009)</td><td>***</td><td>0.030(0.01)</td><td>***</td></tr><tr><td>Existing_days</td><td>0.000(0.000)</td><td>***</td><td>0.000(0.000)</td><td>***</td><td>0.000(0.000)</td><td>***</td></tr><tr><td>Positivity</td><td>-0.006(0.012)</td><td></td><td>-0.007(0.012)</td><td></td><td>-0.009(0.012)</td><td></td></tr><tr><td>Negativity</td><td>0.080(0.064)</td><td></td><td>0.079(0.064)</td><td></td><td>0.097(0.072)</td><td></td></tr><tr><td colspan="7">Restaurant characteristics</td></tr><tr><td>Business_star</td><td>0.050(0.008)</td><td>***</td><td>0.050(0.008)</td><td>***</td><td>0.050(0.012)</td><td>***</td></tr><tr><td>Price_range</td><td>0.022(0.013)</td><td>*</td><td>0.022(0.013)</td><td>*</td><td>0.022(0.015)</td><td></td></tr><tr><td>Review_rank_business</td><td>-0.276(0.028)</td><td>***</td><td>-0.277(0.028)</td><td>***</td><td>-0.288(0.051)</td><td>***</td></tr><tr><td>Cuisine_type = 2 (Asian)</td><td>-0.002(0.012)</td><td></td><td>-0.002(0.012)</td><td></td><td>-0.002(0.016)</td><td></td></tr><tr><td>Cuisine_type = 3 (European)</td><td>-0.008(0.014)</td><td></td><td>-0.008(0.014)</td><td></td><td>-0.007(0.021)</td><td></td></tr><tr><td>Cuisine_type = 4 (South American)</td><td>-0.036(0.021)</td><td>*</td><td>-0.037(0.021)</td><td>*</td><td>-0.041(0.025)</td><td></td></tr><tr><td>Cuisine_type = 5 (Middle Eastern)</td><td>0.008(0.019)</td><td></td><td>0.009(0.019)</td><td></td><td>0.013(0.027)</td><td></td></tr><tr><td>Cuisine_type = 6 (Other)</td><td>0.017(0.012)</td><td></td><td>0.017(0.012)</td><td></td><td>0.014(0.019)</td><td></td></tr><tr><td>Constant</td><td>-1.743(0.994)</td><td>*</td><td>-1.789(0.994)</td><td>*</td><td>-2.223(1.143)</td><td>*</td></tr><tr><td>Observations</td><td colspan="6">994,995</td></tr><tr><td>Restaurants</td><td colspan="6">4,027</td></tr></table>

Note: Standard errors are reported in parentheses. \*p < 0.10; \*\*p < 0.05; \*\*\*p < 0.01.

Thus, the results support all our hypotheses (H1- H5).<sup>10</sup> We further ensured the robustness of our regression results by using a holdout sample validation and the k-fold crossvalidation. As reported in Appendix E, the test results increase our confidence that it is the five personality traits, instead of some random errors picked up by the regression analysis, that explain review helpfulness.

## Predictive Power

Through the above theory building and testing (Step 2 as shown in Figure 2 of our research design and reported above), we identified certain personality traits (high openness, high conscientiousness, high extraversion, high agreeableness, and low emotional stability) that can explain a high number of helpfulness votes, which allowed us to evaluate the predictive power of these personality traits (Steps 3 and 4 as shown in Figure 2 of our research design). We built an “ensemble of ensembles” model, a type of machine learning model, to achieve this goal. Modeling details and results are reported below.

Inputs (or features) used in training. In order to generate actionable and useful implications for practical applications, we examine how well we can predict the helpfulness of a reviewer’s future reviews based on the reviewer’s personality scores inferred from the review texts at a very early stage during which very limited information is available about this reviewer. In other words, we propose to use the first N reviews (N is a small number) that a reviewer posts as inputs for our prediction. This makes our proposed approach useful in practice. We use N = 2 to illustrate our procedure. Using other values of N, such as 1 and 3, also produced similar results. For a reviewer who published more than two reviews, we use the first two reviews to infer the reviewer’s personality trait scores, and then predict the helpfulness of the reviewer’s future reviews (e.g., 3rd, 4th). For a reviewer who published only two reviews in total, we use the first review to infer personality traits, then predicted the helpfulness of the second reviews.

A notable feature of our approach is it allows us to infer the reviewer’s personality immediately after a reviewer posts a review. Thus, to determine a benchmark model for comparison, we used (1) the number of the reviewer’s past reviews, and (2) a “local” variable indicating whether the reviewer is from the same city as the restaurant’s location.

These two variables are widely used in the previous literature and are available to managers. In comparison, for predicting the helpfulness of a future review, review characteristics (e.g., word count, emotion words) and restaurant characteristics (e.g., cuisine type and price level) remain unknown because the review is yet to be written. As such, it is fair to evaluate the predictive power of the inferred reviewer personalities by comparison with the above-mentioned benchmark model.

Labels (helpful/unhelpful). To train a model to predict whether a future review will be helpful or unhelpful, each of the sample reviews is labeled as either “helpful” or “unhelpful,” given the number of helpfulness votes it receives. The simplest way to do this is to select a threshold τ and label reviews that receive fewer votes (i.e., < τ) as unhelpful and the others as helpful. However, as discussed in Ghose and Ipeirotis (2011), the difficulty lies in setting a proper value for τ: setting τ too high results in fewer identified helpful reviews, whereas setting τ too low has the opposite effect. To avoid this pitfall and to demonstrate the robustness of our results, we tried a range of τ values from 1 to 10. We set the maximal value of τ as 10 because 95% of sample reviews received fewer than 10 helpfulness votes.

Training the ensemble model. Using the inferred reviewer personality scores (inputs or features) and the labels (helpful/unhelpful) for each review, we trained an “ensemble of ensembles” model to generate the best prediction. Ensemble methods are meta-algorithms composed of multiple independently trained algorithms and they make more accurate predictions than any single component model and the simple average method (Bauer and Kohavi 1999; Polikar 2006; Rokach 2010). Figure 3 graphically demonstrates the procedure of our “ensemble of ensembles” modeling that unfolds in three stages.

In the first stage, we separately trained three sets of models commonly used by prior research analyzing online reviews: support vector machine (SVM) (e.g., Kim and Pantel 2006; Jin and Liu 2010; Ghose and Ipeirotis 2011; Hong et al. 2012; Zheng et al. 2013), decision tree (e.g., Jin and Liu 2010; Zheng et al. 2013), and naive Bayes (e.g., Jin and Liu 2010; Zheng et al. 2013). In the second stage, we aggregated the three sets of models into ensemble SVM (E-SVM), random forest (RF), and adaptive boosting (AdaBoost), respectively. The three ensemble methods are multifeature voting, bagging, and boosting methods, respectively. (See Appendix F for details.).

![](/api/attachments/APKAA7D3/fulltext/images/8139c2762e4258b787405dc087ea4b00c9dbc69a2581e7b2c4fa6142d3241362.jpg)  
Figure 3. Ensemble of Ensembles Model

At this stage, we found that the classification results produced by those three ensemble models vary significantly and that the error rates have large variances. When there is a significant diversity among different models, an ensemble model tends to yield better results (Kuncheva and Whitaker 2003; Minku et al. 2010). Therefore, in the third stage, we used another layer of ensemble based on the three ensemble models. Specifically, we combined the three previously constructed ensemble models through majority voting to yield the final classification results.<sup>11</sup> Because we trained the three ensemble models separately, their outputs are independent, and therefore the majority voting combination is expected to lead to a performance improvement.

Predictive power (recall and precision). Consistent with our previous research design, we used two thirds of our reviewer sample (training set) to train our supervised classification models and then, based on the trained model, we used the remaining one third as our testing set to evaluate the predictive performance of our proposed model. We compared the classification results of the benchmark and personality models. Our evaluation results are based on a stratified 10-fold cross-validation and we computed both the recall (also known as sensitivity) and precision rates for the models using different thresholds. Recall rate measures the proportion of helpful reviews that are correctly identified as such, whereas precision expresses the ratio between correctly classified helpful reviews and the classified helpful reviews. Given that the ultimate goal of our classification is to determine whether using personality scores can help managers find reviewers who will ultimately produce more helpful reviews in the future, increasing the ability to find helpful reviews is more urgent and therefore recall is more relevant in our case.

Table 5 presents the recall and precision rates across a set of τ values (also shown in Figure 4 for ease of observation). The left panel (recall) shows that the personality models always significantly outperform the benchmark models with a 28.20% average improvement in recall. This confirms the superiority of the personality model for finding helpful reviews—adding reviewer’s personality scores into the model can accurately identify an average of 83.62% of helpful future reviews. The right panel (precision) shows that our personality models have an average of 6.89% improvement in precision, suggesting that the increase in recall rates does not come from sacrificing precision.

## Discussion

This research sets out to examine the question of who will provide future helpful product reviews by integrating theories related to personality and data analytics into a four-step procedure. We first trained a deep learning model to infer a reviewer’s personality traits. Second, we developed hypotheses on how personality traits are associated with review helpfulness based on personality theories. Third, our hypothesis testing results show that higher review helpfulness is related to higher openness, conscientiousness, extraversion, and agreeableness and to lower emotional stability. Fourth, we built an ensemble model using supervised classification algorithms to predict future review helpfulness based on the inferred personality traits. By including inferred personality, the ensemble model shows a notable improvement in both recall and precision, thus demonstrating its superior predictive power compared to the benchmark.

## Implications for Research

Our work joins the burgeoning scientific investigations in various domains that apply new methods of assessing unacquainted individuals—in our case, inferring their personality traits—by mining online data (Brynjolfsson et al. 2016; Varian 2014). Our findings illustrate the usefulness of such methods as alternatives to the traditional methods of surveys and interviews.

Although we only apply the deep learning NLP algorithms for inferring personality traits in the context of online product review platforms, there is a wide scope of contexts where such methods are applicable. As noted above, Taobao offered all reviewers coupons to encourage them to write more (Cabral and Li 2015). Using our methodology in such a research context, researchers could infer reviewer personalities and use that information to prioritize and individually incentivize reviewers based upon their different personality traits. In addition to reviews, e-commerce sites have rich information about reviewers, such as purchase history and browsing categories. Richer information generally allows researchers to develop predictive models with even better predictive power. This type of research is in line with state-of-the-art development of AI technologies and applications in industry, such as IBM Watson Personality Insights.<sup>12</sup>

This work identifies antecedents of review helpfulness using the lens of reviewer personality; it moves beyond prior research that mainly focuses on examining review characteristics and suggests that future research examine fundamental reviewer traits that are theoretically reasonable and practically meaningful. We do not deny the usefulness of attributing review helpfulness to review characteristics. However, we submit that reviewer personalities (that remain relatively stable over time) and review characteristics (that can capture contingencies concerning specific consumption experiences) can be used for different purposes. Although the latter can be used to explain review helpfulness after reviews are created, the former can be used to identify who will provide helpful reviews in the future. We advocate this as a promising avenue for future research.

Given how review helpfulness is defined (i.e., peer-generated information influencing consumers’ purchase decision process (Mudambi and Schuff 2010), our findings relating reviewer personality to review helpfulness shed light on what types of reviewers provide more influential information to others; thus, our research has implications for broader areas of research topics where individuals use information generated by peers. One such topic, for example, is new product diffusion. According to Rogers (2003), new product diffusion is associated with diffusion of information about the product. This suggests that each individual in a population is a potential source of information about the product. Early adopters possess information based on their interactions with the product. They supply information that influences the adoption decisions of others. One line of future research extends this logic by differentiating early adopters according to personality. Based on our findings, a reasonable hypothesis is that early adopters with high openness, high conscientiousness, high extraversion, high agreeableness, and low emotional stability serve as more influential sources of information and can thus play a more powerful role in the product diffusion process.

Another topic area that could benefit from our research is opinion leadership. Given the increasing popularity of social media and online product review platforms, opinion leaders now play an unprecedentedly large role in promoting products and services.

Panel A. Recall

<table><tr><td colspan="7">Table 5. Recall and Precision Rates</td></tr><tr><td rowspan="2">Threshold τ</td><td colspan="3">Recall</td><td colspan="3">Precision</td></tr><tr><td>Personality model</td><td>Benchmark model</td><td>Difference</td><td>Personality model</td><td>Benchmark model</td><td>Difference</td></tr><tr><td>1</td><td>82.28%</td><td>58.43%</td><td>23.85%</td><td>52.59%</td><td>51.60%</td><td>1.00%</td></tr><tr><td>2</td><td>78.68%</td><td>62.95%</td><td>15.73%</td><td>53.04%</td><td>49.66%</td><td>3.38%</td></tr><tr><td>3</td><td>79.88%</td><td>62.05%</td><td>17.83%</td><td>57.70%</td><td>51.50%</td><td>6.20%</td></tr><tr><td>4</td><td>79.58%</td><td>34.94%</td><td>44.64%</td><td>56.87%</td><td>50.88%</td><td>5.99%</td></tr><tr><td>5</td><td>90.66%</td><td>61.75%</td><td>28.92%</td><td>57.77%</td><td>51.14%</td><td>6.64%</td></tr><tr><td>6</td><td>84.00%</td><td>47.29%</td><td>36.71%</td><td>60.43%</td><td>51.58%</td><td>8.85%</td></tr><tr><td>7</td><td>79.70%</td><td>58.43%</td><td>21.27%</td><td>61.27%</td><td>50.26%</td><td>11.01%</td></tr><tr><td>8</td><td>80.00%</td><td>33.83%</td><td>46.17%</td><td>61.54%</td><td>54.22%</td><td>7.32%</td></tr><tr><td>9</td><td>89.39%</td><td>62.78%</td><td>26.61%</td><td>62.77%</td><td>52.96%</td><td>9.81%</td></tr><tr><td>10</td><td>92.00%</td><td>71.70%</td><td>20.30%</td><td>63.01%</td><td>54.29%</td><td>8.73%</td></tr><tr><td>Average</td><td>83.62%</td><td>55.42%</td><td>28.20%</td><td>58.70%</td><td>51.81%</td><td>6.89%</td></tr></table>

![](/api/attachments/APKAA7D3/fulltext/images/26bb546464cfd2ef0021bf1daac256bb03a1e9ce46cd368ecaa9316696439e3d.jpg)  
Figure 4. Recall and Precision Rates

![](/api/attachments/APKAA7D3/fulltext/images/7bd63e11a1d61ce1e44657f1869cc095493de63b5b3a641c1e44ac71176208f2.jpg)

However, few previous studies focus on identifying opinion leaders in the online context. Those that do (e.g., Li and Du 2011) tend to describe opinion leaders mainly on the basis of the characteristics of the messages they create and their positions in online social networks. Those angles are useful for pinpointing existing opinion leaders but are less useful for identifying potential leaders. In contrast, our focus on the personalities of information disseminators provides an alternative way to identify opinion leaders. In brief, future research could extend our approach to different settings and problems, such as identifying potential opinion leaders on social networks (e.g., Twitter and Facebook) or locating effective “seed customers” in new product diffusion.

Psychology research could also benefit from this work. First, our research illustrates a new method to evaluate personality, as a complement to traditional methods such as surveys and interviews, that could greatly broaden the scope of research samples. Beyond the obvious advantage of providing access to previously hard-to-reach populations, our findings could enable psychologists to obtain personality assessments under different contingencies by providing subsamples along different dimensions and further provides “contextual elaboration of theories” (Rai 2016). For instance, in reviewing the literature linking the Big Five personality traits with job performance, Penney et al. (2011) recommend that future research seek to identify new moderators at different levels. Our suggested method of evaluating personality would greatly facilitate the testing of those theories by providing larger samples that utilize work-related documents, such as reports and emails, generated by employees within the workplace.

Second, our research illustrates how theories related to personality can guide feature selection in predictive models and, in the process, how the validity of those theories can be tested using real-life data. As with other disciplines (e.g., economics and management), theories related to personality can inform the feature selection (out of a very large number of possibilities) and help construct the conceptual framework in predictive models. At the same time, predictive models, especially those using machine learning algorithms, can provide further tests of the theory’s validity using real-life data and enhance precision in theory testing with more granular observation of activities and outcomes (Einav and Levin 2014; Varian 2014).

Third, our research provides a promising new way to effectively evaluate personality at zero acquaintance, one of the most prominent features of various online settings. People continuously make judgments, consciously or unconsciously, about others’ personalities, which an important life skill in any social context (Funder 1995). The online review context, however, is different from traditional settings where people make judgments about others’ personalities based on face-toface interactions and other information cues such as physical appearance, body language, and gestures. In the online review environment, people can only infer others’ personalities under zero-acquaintance circumstances from online traces. Personality assessment at zero acquaintance, one of the traditional topics in psychology (e.g., Albright et al. 1988), primarily relies on human ratings in the past, which are not only readily influenced by stereotypes but are also particularly vulnerable to technological artifacts (Gill et al. 2006). Our research demonstrates the important role played by personality traits calculated from the linguistic cue—the most distinguished information cue in the online context. Along the same lines, a promising direction for future research is the application of psychological theory about personality traits to new and important environments where traditional information cues are missing or weakened, including text-based social networks (e.g., Boldomatic, Twitter) and information sharing platforms (e.g., Wikipedia). These are areas worthy of exploration because linguistic cues can play a salient role in inferring personality.

## Implications for Practice

Our work has useful implications for practice. In this work, we identified a connection between people’s personality traits and their review helpfulness. The literature on personality contains a rich stream of research connecting personality traits to individual performance in various contexts such as opinion leadership (e.g., Flynn et al. 1996, Batinic et al. 2016). Purely from a research perspective, our work is consistent with this research tradition. Practically, our proposed method can effectively predict most helpful reviewers soon after they post a review and it therefore offers great value for review-centric sites and platforms. When used appropriately, the method could raise the overall level of review helpfulness, thereby improving customers’ experience and satisfaction. These benefits notwithstanding, there are potential ethical issues that may emerge from the applications of our findings.

In reflecting on how to appropriately apply our findings, we considered the four principles of AI ethics based on Ethics Guidelines for Trustworthy AI by the European Commission (2018): beneficence (do good), non-maleficence (do no harm), justice (be fair), and explicability (operate transparently). These principles are widely echoed in the AI ethics principles of other organizations (see Jobin et al. 2019 for details) and are relevant to our research context.<sup>13</sup>

According to the principle of beneficence, practitioners must make sure that AI applications are designed to improve society’s well-being. One possible way to use our findings would be to invite review writers who are expected to generate helpful reviews in order to improve the overall quality of reviews. This belongs to the category of influencer marketing, a marketing strategy that uses the influence of key individuals to drive consumers’ brand awareness and purchasing decisions (Ahmad 2018). In practice, a case in point is Amazon’s Vine program, where Amazon invites influential reviewers to post opinions on new products. Prior research on product reviews has suggested using incentives, such as free samples, to lure more reviews from prominent reviewers (Jabr and Zheng 2014). Generating more helpful reviews would have a net positive impact on society because helpful reviews can assist other consumers. More broadly, our method could be adopted when impactful influencers are needed to promote initiatives that are beneficial to individual and social well-being (e.g., raising public attention to global warming, promoting a healthy lifestyle). For these initiatives, our method could be used to identify helpful writers to take the lead.

The principle of non-maleficence requires that AI applications should not harm human beings physically, psychologically, financially, or socially. Using personality as the base of influencer marketing has been gaining popularity in practice (Matz et al. 2017), yet we caution managers to watch for any possible inappropriate exploitation of our method. One warning sign is when it only helps them, not their customers. For instance, managers might use our method to link consumers’ personality traits to their price sensitivities in order to efficiently price discriminate among their consumers. This practice is unethical. The dangers associated with the misapplication of our method to specific areas and subjects should be carefully considered by scholars, managers, and policymakers.

Regarding “be fair” (the principle of justice), the Consumer Review Fairness Act (CRFA) provides relevant guidance on the practice of this principle. The CRFA “protects people’s ability to share their honest opinions about a business’s products, services, or conduct, in any forum, including social media.”<sup>14</sup> Practitioners should ensure that every consumer can freely share their honest opinions. Businesses could leverage our findings to help people willing to create online content. Plenty of businesses and platforms now offer advice about how to create useful content in order to increase social media influence; yet, to the best of our knowledge, none of this advice is given from the personality perspective. Our findings could guide improvements to online content; businesses and platforms could provide more guidance and advice, and even individual mentoring, even for those with personality traits related to low levels of review helpfulness.

Regarding explicability, AI-based initiatives should provide sufficient information to stakeholders and comply with laws and regulations. Helixa, an AI company in New York, developed predictive models that calculate Big Five personality traits based on individuals’ social media activities, using data from over 10,000 participants who gave Helixa permission to collect their social media data (Rivera 2019). This showcases explicability. In applying our approach, managers should establish data/application transparency and ensure the protection of consumer privacy.

## Limitations and Future Research

Our study is not without limitations. First, we use data from one review platform and we limit our sample to the restaurant category of the Yelp Academic Dataset. Although this is a widely used dataset and Yelp is a leading review platform, future research should apply our approach to other data sources and categories to test its validity. Second, we use historical data and thus cannot fully demonstrate causality and the power of the personality model for predicting who will provide more helpful reviews. We thus call for future research using other methods and data, such as field experiments, qualitative data, or mixed methods, to demonstrate causality and to evaluate the practical value of our approach. Third, we only analyze Big Five personality traits, but other personality insights could also be obtained through NLP. Future research should develop a rich understanding of personality characteristics, needs, and values, and use them to predict future behaviors (Song et al. 2010). Fourth, as with other machine learning models, the quality of personality quantification (as well as our prediction of review helpfulness) is determined by the quality of the labeled training data—essays corpus (Pennebaker and King 1999). Despite the fact that these data are widely used in many fields and have been recognized as one of the gold standard labeled datasets by the AAAI workshop on computational personality (Celli et al. 2013), our models could be significantly improved through better labeled training data. We leave this to future research.

## Concluding Remarks

This work discovers reviewers’ personality through a deep learning-based NLP approach and demonstrates the power of a personality model for predicting future review helpfulness. It illustrates two routes for synergistically leveraging theory and data. One is to measure constructs that were previously costly to measure (personality, in this study) by using increasingly available data and suitable analytic techniques. The other is to resort to theories (those relating personality to review helpfulness, in this study) that can provide powerful guidance on variable selection for predictive modeling. We hope our work will stimulate more research on the use of data and theory via these routes.

## Acknowledgments

The authors thank the senior editor and the four reviewers for their constructive feedback through the review process. The authors are grateful to the Natural Science Foundation of China (Grant No. 71490724, 71872099), and Tsinghua SEM Center for Artificial Intelligence and Management (AIM) for their financial support.

## References

Adamopoulos, P., Ghose, A., and Todri, V. 2018. “The Impact of User Personality Traits on Word of Mouth: Text-Mining Social Media Platforms,” Information Systems Research (29:3), pp. 612-640.

Agarwal, R., and Karahanna, E. 2000. “Time Flies When You’re Having Fun: Cognitive Absorption and Beliefs about Information Technology Usage,” MIS Quarterly (24:4), pp. 665-694.

Albright, L., Kenny D. A., and Malloy T. E. 1988. “Consensus in Personality Judgments at Zero Acquaintance,” Journal of Personality and Social Psychology (55:3) pp. 387-395.

Ardichvili, A. 2008. “Learning and Knowledge Sharing in Virtual Communities of Practice: Motivators, Barriers, and Enablers,” Advances in Developing Human Resources (10:4), pp. 541-554.

Baesens, B., Bapna, R., Marsden, J. R., Venthienen, J., and Zhao, J. L. 2016. “Transformational Issues of Big Data and Analytics in Networked Business,” MIS Quarterly (40:4), pp. 807-816.

Barrick, M. R., and Mount, M. K. 1991. “The Big Five Personality Dimensions and Job Performance: A Meta-Analysis,” Personnel Psychology (44:1), pp. 1-26.

Barrick, M. R., Parks, L., and Mount, M. K. 2005. “Self-Monitoring as a Moderator of the Relationships Between Personality Traits and Performance,” Personnel Psychology (58:3) pp. 745-767.

Barrick, M. R., Stewart, G. L., Neubert, M. J., and Mount, M. K. 1998. “Relating Member Ability and Personality to Work-Team Processes and Team Effectiveness,” Journal of Applied Psychology (83:3), pp. 377-391.

Batinic, B., Appel, M., and Gnambs, T. 2016. “Examining Individual Differences in Interpersonal Influence: On the Psychometric Properties of the Generalized Opinion Leadership Scale (GOLS),” The Journal of psychology (150:1), pp. 88-101.

Bauer, E., and Kohavi, R. 1999. “An Empirical Comparison of Voting Classification Algorithms: Bagging, Boosting, and Variants,” Machine Learning (36:1-2), pp. 105-139.

Berger, J., and Milkman, K. L. 2012. “What Makes Online Content Viral?” Journal of Marketing Research (49:2), pp. 192-205.

Bock, G. W., Zmud, R. W., Kim, Y. G., and Lee, J. N. 2005. “Behavioral Intention Formation in Knowledge Sharing: Examining the Roles of Extrinsic Motivators, Social-Psychological Forces, and Organizational Climate,” MIS Quarterly (29:1), pp. 87-111.

Bostrom, R. N. 1983. Persuasion, Upper Saddle River, NJ: Prentice Hall. Brader, T. 2006. Campaigning for Hearts and Minds, Chicago, IL: The University of Chicago Press.

Brodley, C. E., and Friedl, M. A. 1996. “Identifying and Eliminating Mislabeled Training Instances,” in Proceedings of the National Conference on Artificial Intelligence, pp. 799-805.

Brynjolfsson, E., Geva, T., and Reichman, S. 2016. “Crowd-Squared: Amplifying the Predictive Power of Search Trend Data,” MIS Quarterly (40:4), pp. 941-961.

Cabral, L., and Li, L. 2015. “A Dollar for Your Thoughts: Feedback-Conditional Rebates on eBay,” Management Science (61:9), pp. 2052-2063.

Cabrera, A., Collins, W. C., and Salgado, J. F. 2006. “Determinants of Individual Engagement in Knowledge Sharing,” The International Journal of Human Resource Management (17:2), pp. 245-264.

Cao, Q., Duan, W., and Gan, Q. 2011. “Exploring Determinants of Voting for the ‘Helpfulness’ of Online User Reviews: A Text Mining Approach,” Decision Support Systems (50:2), pp. 511-521.

Celli, F., Pianesi, F., Stillwell, D., and Kosinski, M. 2013. “Workshop on Computational Personality Recognition: Shared Task,” presented at the Seventh International AAAI Conference on Weblogs and Social Media, Cambridge, MA.

Chen, Y., and Xie, J. 2008. “Online Consumer Review: Word-Of-Mouth as a New Element of Marketing Communication Mix,” Management Science (54:3), pp. 477-491.

Cheng, Q., Varshney, P. K., and Arora, M. K. 2006. “Logistic Regression for Feature Selection and Soft Classification of Remote Sensing Data,” IEEE Geoscience and Remote Sensing Letters (3:4), pp. 491-494.

Chintagunta, P. K., Gopinath, S., and Venkataraman, S. 2010. “The Effects of Online User Reviews on Movie Box Office Performance: Accounting for Sequential Rollout and Aggregation across Local Markets,” Marketing Science (29:5), pp. 944-957.

Clark, R. A., and Goldsmith, R. E. 2005. “Market Mavens: Psychological Influences,” Psychology and Marketing (22:4), pp. 289-312.

Clore, G. L., and Gasper, K. 2000. “Feeling is Believing: Some Affective Influences on Belief,” in Emotions and Beliefs: How Feelings Influence Thoughts, N. H. Frijda, A. S. Manstead, and S. Bem (eds.), Cambridge: Cambridge University Press, pp. 10-44.

Cohrs, J. C., Kämpfe-Hargrave, N., and Riemann, R. 2012. “Individual Differences in Ideological Attitudes and Prejudice: Evidence from Peer-Report Data,” Journal of Personality and Social Psychology (103:2), pp. 343-361.

Colbert, A. E., and Witt, L. A. 2009. “The Role of Goal-Focused Leadership in Enabling the Expression of Conscientiousness,” Journal of Applied Psychology (94:3), pp. 790-796.

Conger, J. A. 1998. “The Necessary Art of Persuasion,” Harvard Business Review (76), pp. 84-97.

Constant, D., Sproull, L., and Kiesler, S. 1996. “The Kindness of Strangers: The Usefulness of Electronic Weak Ties for Technical Advice,” Organization Science (7:2), pp. 119-135.

Costa, P. T., and McCrae, R. R. 1994. “Set Like Plaster? Evidence for the Stability of Adult Personality,” in Can Personality Change? T. F. Heatherton and J. L. Weinberger (eds.), Washington, DC: American Psychological Association, pp. 21-40.

Costa, P. T., and McCrae, R. R. 2006. “Age Changes in Personality and Their Origins: Comment on Roberts, Walton, and Viechtbauer (2006),” Psychological Bulletin (132:1), pp. 26-28.

Coulter, R. A., Feick, L. F., and Price, L. L. 2002. “Changing Faces: Cosmetics Opinion Leadership among Women in the New Hungary,” European Journal of Marketing (36:11/12), pp. 1287-1308.

Davenport, T. H. 2015. “Analytics and Big Data: The New Kale?” Wall Street Journal (http://blogs.wsj.com/cio/2015/02/05/ analytics-andbig-data-the-new-kale/).

de Vries, R. E., Van den Hooff, B., and de Ridder, J. A. 2006. “Explaining Knowledge Sharing: The Role of Team Communication Styles, Job Satisfaction, and Performance Beliefs,” Communication Research (33:2), pp. 115-135.

DeYoung, C. G., and Gray, J. R. 2009. “Personality Neuroscience: Explaining Individual Differences in Affect, Behavior, and Cognition,” in The Cambridge Handbook of Personality Psychology, P. J. Corr and G. Matthews (eds.), Cambridge: Cambridge University Press, pp. 323-346.

Domingos, P. 2012. “A Few Useful Things to Know about Machine Learning,” Communications of the ACM (55:10), pp. 78-87.

Donovan, B. 2015. “Is There Personality in Big Data?,” Acxiom (http://www.acxiom.com/personality-big-data/).

Einav, L., and Levin, J. 2014. “Economics in the Age of Big Data,” Science (346:6210), pp. 1243089.

European Commission. 2018. “Ethics Guidelines for Trustworthy AI,” European Commission (https://ec.europa.eu/newsroom/dae/ document.cfm?doc\_id=57112).

Eysenck, H. J. 1967. The Biological Basis of Personality, Piscataway, NJ: Transaction Publishers.

Flynn, L. R., Goldsmith, R. E., and Eastman, J. K. 1996. “Opinion Leaders and Opinion Seekers: Two New Measurement Scales,” Journal of the Academy of Marketing Science (24:2), pp. 137-147.

Forman, C., Ghose, A., and Wiesenfeld, B. 2008. “Examining the Relationship Between Reviews and Sales: The Role of Reviewer Identity Disclosure in Electronic Markets,” Information Systems Research (19:3), pp. 291-313.

Frijda, N. H., Manstead, A. S., and Bem, S. 2000. “The Influence of Emotions on Beliefs,” in Emotions and Beliefs: How Feelings Influence Thoughts, N. H. Frijda, A. S. Manstead and S. Bem (eds.), Cambridge: Cambridge University Press, pp. 1-9.

Funder, D. C. 1995. “On the Accuracy of Personality Judgment: A Realistic Approach,” Psychological Review (102:4), pp. 652-670.

George, J. M. 2000. “Emotions and Leadership: The Role of Emotional Intelligence,” Human Relations (53:8), pp. 1027-1055.

Ghose, A., and Ipeirotis, P. G. 2011. “Estimating the Helpfulness and Economic Impact of Product Reviews: Mining Text and Reviewer Characteristics,” IEEE Transactions on Knowledge and Data Engineering (23:10), pp. 1498-1512.

Gill, A. J., Oberlander, J., and Austin, E. 2006. “Rating E-mail Personality at Zero Acquaintance,” Personality and Individual Differences (40:3), pp. 497-507.

Gloor, P. A., Oster, D., Raz, O., Pentland, A., and Schoder, D. 2010. “The Virtual Mirror: Reflecting on the Social and Psychological Self to Increase Organizational Creativity,” International Studies of Management and Organization (40:2), pp. 74-94.

Gnambs, T., and Batinic, B. 2012. “A Personality-Competence Model of Opinion Leadership,”Psychology and Marketing (29:8), pp. 606-621.

Godes, D., and Silva, J. C. 2012. “Sequential and Temporal Dynamics of Online Opinion,” Marketing Science (31:3), pp. 448-473.

Goldsmith, R. E., Clark, R. A., and Goldsmith, E. B. 2006. “Extending the Psychological Profile of Market Mavenism,” Journal of Consumer Behaviour: An International Research Review (5:5), pp. 411-419.

Goleman, D., Boyatzis, R., and McKee, A. 2013. Primal Leadership: Unleashing the Power of Emotional Intelligence, Boston, MA: Harvard Business Press.

Gong, J., Abhisek, V., and Li, B. 2018. “Examining the Impact of Keyword Ambiguity on Search Advertising Performance: A Topic Model Approach,” MIS Quarterly (42:3), pp. 805-829.

Graves, C., and Matz, S. 2018. “What Marketers Should Know About Personality-Based Marketing,” Harvard Business Review (https://hbr.org/2018/05/what-marketers-should-know-aboutpersonality-based-marketing/).

Greene, W. H. 2003. Econometric Analysis, Upper Saddle River, NJ: Prentice Hall.

Gregor, S., and Hevner, A. R. 2013. “Positioning and Presenting Design Science Research for Maximum Impact,” MIS Quarterly (37:2), pp. 337-355.

Guyon, I., and Elisseeff, A. 2006. “An Introduction to Feature Extraction,” in Feature Extraction, I. Guyon, S. Gunn, M. Nikravesh, and L. A. Zadeh (eds.), Berlin: Springer, pp. 1-25.

Hansen, L. P. 1982. “Large Sample Properties of Generalized Method of Moments Estimators,” Econometrica: Journal of the Econometric Society (50:4), pp. 1029-1054.

Hirsh, J. B., and Peterson, J. B. 2009. “Personality and Language Use in Self-Narratives,” Journal of Research in Personality (43:3), pp. 524-527.

Hofstede, G., and McCrae, R. R. 2004. “Personality and Culture Revisited: Linking Traits and Dimensions of Culture,” Cross-Cultural Research (38:1), pp. 52-88.

Hong, Y., Lu, J., Yao, J., Zhu, Q., and Zhou, G. 2012. “What Reviews Are Satisfactory: Novel Features for Automatic Helpfulness Voting,” in Proceedings of the 35th International ACM SIGIR Conference on Research and Development in Information Retrieval, pp. 495-504.

Huang, A. H., Chen, K., Yen, D. C., and Tran, T. P. 2015. “A Study of Factors that Contribute to Online Review Helpfulness,” Computers in Human Behavior (48:C), pp. 17-27.

Huang, H. C., Cheng, T. C. E., Huang, W. F., and Teng, C. I. 2018. “Who Are Likely to Build Strong Online Social Networks? The Perspectives of Relational Cohesion Theory and Personality Theory,” Computers in Human Behavior (82), pp. 111-123.

Jin, J., and Liu, Y. 2010. “How to Interpret the Helpfulness of Online Product Reviews: Bridging the Needs Between Customers and Designers,” in Proceedings of the 2nd International Workshop on Search and Mining User-Generated Contents, pp. 87-94.

Jindal, N., and Liu, B. 2008. “Opinion Spam and Analysis,” in Proceedings of the 2008 International Conference on Web Search and Data Mining, pp. 219-230.

John, O. P., Naumann, L. P., and Soto, C. J. 2008. “Paradigm Shift to the Integrative Big Five Trait Taxonomy,” in Handbook of Personality: Theory and Research, 3rd ed., O. P. John, R. W. Robins, and L. A. Pervin (Eds.), New York: Guilford Press, pp. 114- 158.

John, O. P., and Srivastava, S. 1999. “The Big Five Trait Taxonomy: History, Measurement, and Theoretical Perspectives,” in Handbook of Personality: Theory and Research, 2nd ed., O. P. John, R. W. Robins, and L. A. Pervin (Eds.), New York: Guilford Press, pp. 102- 138.

Judge, G., Rufus C. H., Griffiths, W., Lutkepohl, H., and Lee, T. C. 1988. Introduction to the Theory and Practice of Econometrics, 2nd ed., Hoboken, NJ: Wiley.

Judge, T. A., Bono, J. E., Ilies, R., and Gerhardt, M. W. 2002. “Personality and Leadership: A Qualitative and Quantitative Review,” Journal of Applied Psychology (87:4), pp. 765-780.

Karlsen, R. 2015. “Followers are Opinion Leaders: The Role of People in the Flow of Political Communication on and Beyond Social Networking Sites,” European Journal of Communication (30:3), pp. 301-318.

Kavanaugh, A., Zin, T. T., Carroll, J. M., Schmitz, J., Perez-Quinones, M., and Isenhour, P. 2006. “When Opinion Leaders Blog: New Forms of Citizen Interaction,” in Proceedings of the 2006 International Conference on Digital Government Research, pp. 79- 88.

Kim, S. M., Pantel, P., Chklovski, T., and Pennacchiotti, M. 2006. “Automatically Assessing Review Helpfulness,” in Proceedings of the 2006 Conference on Empirical Methods in Natural Language Processing: Association for Computational Linguistics, pp. 423- 430.

Koh, P. W., and Liang, P. 2017. “Understanding Black-Box Predictions Via Influence Functions,” in Proceedings of the 34th International Conference on Machine Learning, Sydney, Australia.

Kristensen, J. B., Albrechtsen, T., Dahl-Nielsen, E., Jensen, M., Skovrind, M., and Bornakke. T. 2017. “Parsimonious Data: How a Single Facebook Like Predicts Voting Behavior in Multiparty Systems,” PLoS ONE (12:9), e0184562.

Kuncheva, L. I., and Whitaker, C. J. 2003. Measures of Diversity in Classifier Ensembles and Their Relationship with the Ensemble Accuracy,” Machine Learning (51:2), pp. 181-207.

Li, F., and Du, T. C. 2011. “Who is Talking? An Ontology-Based Opinion Leader Identification Framework for Word-Of-Mouth Marketing in Online Social Blogs,” Decision Support Systems (51:1), pp. 190-197.

Liao, H., and Chuang, A. 2004. “A Multilevel Investigation of Factors Influencing Employee Service Performance and Customer Outcomes,” Academy of Management Journal (47:1), pp. 41-58.

Liu, Q. B., and Karahanna, E. 2017. “The Dark Side of Reviews: The Swaying Effects of Online Product Reviews on Attribute Preference Construction,” MIS Quarterly (41:2), pp. 427-448.

Lobel, T. E. 1987. “Extraversion, Trait-Anxiety and Expression of Positive Feelings,” Personality and Individual Differences (8:6), pp. 955-956.

Magnini, V. P. 2008. “Practicing Effective Knowledge Sharing in International Hotel Joint Ventures,” International Journal of Hospitality Management (27:2), pp. 249-258.

Mairesse, F., Walker, M. A., Mehl, M. R., and Moore, R. K. 2007. “Using Linguistic Cues for the Automatic Recognition of Personality in Conversation and Text,” Journal of Artificial Intelligence Research (30:1), pp. 457-500.

Majumder, N., Poria, S., Gelbukh, A., and Cambria, E. 2017. “Deep Learning-Based Document Modeling for Personality Detection from Text,” IEEE Intelligent Systems (32:2), pp. 74-79.

Matzler, K., Renzl, B., Müller, J., Herting, S., and Mooradian, T. A. 2008. “Personality Traits and Knowledge Sharing,” Journal of Economic Psychology (29:3), pp. 301-313.

McCrae, R. R., and Costa, P. T. 2003. Personality in Adulthood: A Five-Factor Theory Perspective, New York: Guilford Press.

McCrae, R. R., and John, O. P. 1992. “An Introduction to the Five-Factor Model and Its Applications,” Journal of Personality (60:2), pp. 175-215.

McCrae, R. R., and Terracciano, A. 2005. “Personality Profiles of Cultures: Aggregate Personality Traits,” Journal of Personality and Social Psychology (89:3), pp. 407-425.

Meyer, G., Adomavicius, G., Johnson, P., Elidrisi, M., Rush, W., Sperl-Hillen, J., and O’Connor, P. 2014. “A Machine Learning Approach

to Improving Dynamic Decision Making,” Information Systems Research (25:2), pp. 239-263.

Minku, L. L., White, A. P., and Yao, X. 2010. “The Impact of Diversity on Online Ensemble Learning in the Presence of Concept Drift,” IEEE Transactions on Knowledge and Data Engineering (22:5), pp. 730-742.

Mohammadi, G., Park, S., Sagae, K., Vinciarelli, A., and Morency, L. P. 2013. “Who is Persuasive? The Role of Perceived Personality and Communication Modality in Social Multimedia,” in Proceedings of the 15th ACM on International Conference on Multimodal Interaction, pp. 19-26.

Mooradian, T., Renzl, B., and Matzler, K. 2006. “Who Trusts? Personality, Trust and Knowledge Sharing,” Management Learning (37:4), pp. 523-540.

Mudambi, S. M., and Schuff, D. 2010. “What Makes a Helpful Review? A Study of Customer Reviews on Amazon.com,” MIS Quarterly (34:1), pp. 185-200.

Murphy, S. T., and Zajonc, R. B. 1993. “Affect, Cognition, and Awareness: Affective Priming with Optimal and Suboptimal Stimulus Exposures,” Journal of Personality and Social Psychology (64:5), pp. 723-739.

Muscanell, N. L., and Guadagno, R. E. 2012. “Make New Friends or Keep the Old: Gender and Personality Differences in Social Networking Use,” Computers in Human Behavior (28:1), pp. 107-112.

Nair, H. S., Manchanda, P., and Bhatia, T. 2010. “Asymmetric Social Interactions in Physician Prescription Behavior: The Role of Opinion Leaders,” Journal of Marketing Research (47:5), pp. 883- 895.

Narvaez, D., Lapsley, D. K., Hagele, S., and Lasky, B. 2006. “Moral Chronicity and Social Information Processing: Tests of a Social Cognitive Approach to the Moral Personality,” Journal of Research in Personality (40:6), pp. 966-985.

Ning, X., and Karypis, G. 2012. “Sparse Linear Methods with Side Information for Top-N Recommendations,” in Proceedings of the 6th ACM Conference on Recommender Systems, pp. 155-162.

Oreg, S., and Sverdlik, N. 2014. “Source Personality and Persuasiveness: Big Five Predispositions to Being Persuasive and the Role of Message Involvement,” Journal of Personality (82:3), pp. 250-264.

Pacini, R. and Epstein, S. 1999. “The Relation of Rational and Experiential Information Processing Styles to Personality, Basic Beliefs, and the Ratio-Bias Phenomenon,” Journal of Personality and Social Psychology (76:6), pp. 972-987.

Pal, M. 2012. “Multinomial Logistic Regression-Based Feature Selection for Hyperspectral Data,” International Journal of Applied Earth Observation and Geoinformation (14:1), pp. 214-220.

Pant, P., Heikkinen, V., Korpela, I., Hauta-Kasari, M., and Tokola, T. 2014. “Logistic Regression-Based Spectral Band Selection for Tree Species Classification: Effects of Spatial Scale and Balance in Training Samples,” IEEE Geoscience and Remote Sensing Letters (11:9), pp. 1604-1608.

Park, C. S. 2013. “Does Twitter Motivate Involvement in Politics? Tweeting, Opinion Leadership, and Political Engagement,” Computers in Human Behavior (29:4), pp. 1641-1648.

Pei-Lee, T., Chen, C. Y., Chin, W. C., and Siew, Y. Y. 2017. “Do the Big Five Personality Factors Affect Knowledge Sharing Behavior? A Study of Malaysian Universities,” Malaysian Journal of Library and Information Science (16:1), pp. 47-62.

Pennebaker, J. W., and King, L. A. 1999. “Linguistic Styles: Language Use as an Individual Difference,” Journal of Personality and Social Psychology (77:6), pp. 1296-1312.

Penney, L. M., David, E., and Witt, L. A. 2011. “A Review of Personality and Performance: Identifying Boundaries, Contingencies, and Future Research Directions,” Human Resource Management Review (21:4), pp. 297-310.

Polikar, R. 2006. “Ensemble Based Systems in Decision Making,” IEEE Circuits and Systems Magazine (6:3), pp. 21-45.

Poropat, A. E. 2009. “A Meta-Analysis of the Five-Factor Model of Personality and Academic Performance,” Psychological Bulletin (135:2), pp. 322-338.

Rabinovich, M., and Blei, D. 2014. “The Inverse Regression Topic Model,” in Proceedings of the 31st International Conference on Machine Learning, pp. 199-207.

Rai, A. 2016. “Synergies between Big Data and Theory,” MIS Quarterly (40:2), pp. iii-ix.

Rentfrow, P. J., Gosling, S. D., and Potter, J. 2008. “A Theory of the Emergence, Persistence, and Expression of Geographic Variation in Psychological Characteristics,” Perspectives on Psychological Science (3:5), pp. 339-369.

Rivera, C. 2019. “Marketing with Personality,” Helixa (https://www. helixa.ai/blog/marketing-with-personality).

Robins, R. W., Tracy, J. L., Trzesniewski, K., Potter, J., and Gosling, S. D. 2001. “Personality Correlates of Self-Esteem,” Journal of Research in Personality (35:4), pp. 463-482.

Rogers, E. M. 2003. Diffusion of Innovations, 5th ed., New York: Free Press.

Rokach, L. 2010. “Ensemble-Based Classifiers,” Artificial Intelligence Review (33:1-2), pp. 1-39.

Ruvio, A., and Shoham, A. 2007. “Innovativeness, Exploratory Behavior, Market Mavenship, and Opinion Leadership: An Empirical Examination in the Asian Context,” Psychology and Marketing (24:8), pp. 703-722.

Schmitt, D. P., Realo, A., Voracek, M., and Allik, J. 2008. “Why Can't a Man Be More Like a Woman? Sex Differences in Big Five Personality Traits Across 55 Cultures,” Journal of Personality and Social Psychology (94:1), pp. 168 -182.

Song, C., Qu, Z., Blumm, N., and Barabasi, A. 2010. “Limits of Predictability in Human Mobility,” Science (327:5968), pp. 1018- 1021.

Sundheim, D. 2013. “Good Leaders Get Emotional,” Harvard Business Review (https://hbr.org/2013/08/good-leaders-getemotional/).

Tausczik, Y. R., and Pennebaker, J. W. 2010. “The Psychological Meaning of Words: LIWC and Computerized Text Analysis Methods,” Journal of Language and Social Psychology (29:1), pp. 24-54.

Tyagi, C. L., and Kumar, A. 2004. Consumer Behaviour, New Delhi: Atlantic Publishers and Distributors.

Varian, H. R. 2014. “Big Data: New Tricks for Econometrics,” The Journal of Economic Perspectives (28:2), pp. 3-27.

Venkatesh, V., Sykes, T. A., and Venkatraman, S. 2014. “Understanding E-Government Portal Use in Rural India: Role of Demographic and Personality Characteristics,” Information Systems Journal (24:3), pp. 249-269.

Verbaeten, S., and Van Assche, A. 2003. “Ensemble Methods for Noise Elimination in Classification Problems,” in Proceedings of the Multiple Classifier Systems: 4th International Workshop, pp. 317-325.

Wang, C. C., and Yang, Y. J. 2007. “Personality and Intention to Share Knowledge: An Empirical Study of Scientists in an R&D Laboratory,” Social Behavior and Personality: An International Journal (35:10), pp. 1427-1436.

Wang, S., Noe, R. A., and Wang, Z. M. 2014. “Motivating Knowledge Sharing in Knowledge Management Systems: A Quasi-Field Experiment,” Journal of Management (40:4), pp. 978-1009.

Wayne, J. H., Musisca, N., and Fleeson, W. 2004. “Considering the Role of Personality in the Work–Family Experience: Relationships of the Big Five to Work–Family Conflict and Facilitation,” Journal of Vocational Behavior (64:1), pp. 108-130.

Wheeler, S. C., Petty, R. E., and Bizer, G. Y. 2005. “Self-Schema Matching and Attitude Change: Situational and Dispositional Determinants of Message Elaboration,” Journal of Consumer Research (31:4), pp. 787-797.

Witt, L. A., Burke, L. A., Barrick, M. R., and Mount, M. K. 2002. “The Interactive Effects of Conscientiousness and Agreeableness on Job Performance,” Journal of Applied Psychology (87:1), pp. 164-169.

Yarkoni, T. 2010. “Personality in 100,000 Words: A Large-Scale Analysis of Personality and Word Use among Bloggers,” Journal of Research in Personality (44:3), pp. 363-373.

Yin, D., Bond, S., and Zhang, H. 2014. “Anxious or Angry? Effects of Discrete Emotions on the Perceived Helpfulness of Online Reviews,” MIS Quarterly (38:2), pp. 539-60.

Youyou, W., Kosinski, M., and Stillwell, D. 2015. “Computer-Based Personality Judgments Are More Accurate than Those Made by Humans,” Proceedings of the National Academy of Sciences (112:4), pp. 1036-1040.

Zeiler, M. D., and Fergus, R. 2014. “Visualizing and Understanding Convolutional Networks,” in Proceedings of the 13<sup>th</sup> European Conference on Computer Vision, pp. 818-833.

Zeiler, M. D. 2012. “ADADELTA: An Adaptive Learning Rate Method,” arXiv.org (https://arxiv.org/pdf/1212.5701.pdf).

Zheng, X., Zhu, S., and Lin, Z. 2013. “Capturing the Essence of Word-Of-Mouth for Social Commerce: Assessing the Quality of Online E-Commerce Reviews by a Semi-Supervised Approach,” Decision Support Systems (56), pp. 211-222.

## About the Authors

Angela Xia Liu is an associate professor of marketing at the University of North Carolina at Charlotte. Her work has been published in Management Science, Journal of Marketing Research, Journal of Marketing, and Journal of Management Studies, among other outlets.

Yilin Li is a Ph.D. candidate in information systems at the School of Economics and Management, Tsinghua University. Her research interests are AI business value, online behavior, and social network.

Sean Xin Xu is a professor in the School of Economics and Management, Tsinghua University. His work has been published in MIS Quarterly, Information Systems Research, Journal of MIS, Management Science, Strategic Management Journal, and Contemporary Accounting Research, among other outlets. He won the MIS Quarterly Best Paper award for 2013. His editorial services include senior editor for MIS Quarterly (2016-present) and associate editor for Information Systems Research (2012-2015). Information Systems Research named him “Best Associate Editor” in 2013.

## Appendix A

Literature Review: Main Explanatory Factors for Review Helpfulness

<table><tr><td colspan="11">Table A1. Literature Review</td></tr><tr><td></td><td></td><td colspan="5">Review characteristics</td><td colspan="4">Reviewer characteristics</td></tr><tr><td>Studies</td><td>Context</td><td>Rating/extremity</td><td>Depth/length</td><td>Readability</td><td>Sentiment/emotion</td><td>Elapsed date</td><td>Disclosure</td><td>Reputation/expertise</td><td>Number of past reviews</td><td></td></tr><tr><td>Baek et al. (2012)</td><td>Amazon</td><td>√</td><td>√</td><td></td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Cao et al. (2011)</td><td>CNET</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td></td><td></td><td></td><td></td></tr><tr><td>Chua and Banerjee (2016)</td><td>Amazon</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Danescu-Niculescu-Mizil et al. (2009)</td><td>Amazon</td><td>√</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Forman et al. (2008)</td><td>Amazon</td><td>√</td><td></td><td></td><td></td><td></td><td>√</td><td></td><td>√</td><td></td></tr><tr><td>Ghose and Ipeirotis (2011)</td><td>Amazon</td><td>√</td><td></td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Huang et al. (2015)</td><td>Amazon</td><td>√</td><td>√</td><td></td><td></td><td></td><td></td><td>√</td><td>√</td><td></td></tr><tr><td>Karimi and Wang (2017)</td><td>Google Play</td><td>√</td><td>√</td><td></td><td></td><td></td><td>√</td><td></td><td></td><td></td></tr><tr><td>Kim et al. (2006)</td><td>Amazon</td><td>√</td><td>√</td><td>√</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Korfiatis et al. (2012)</td><td>Amazon</td><td>√</td><td>√</td><td>√</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Kwok and Xie (2016)</td><td>TripAdvisor</td><td>√</td><td>√</td><td></td><td></td><td></td><td></td><td>√</td><td></td><td></td></tr><tr><td>Liu and Park (2015)</td><td>Yelp</td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td></td><td></td></tr><tr><td>Lu et al. (2018)</td><td>Amazon</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td><td>√</td><td></td></tr><tr><td>Martin and Pu (2014)</td><td>Amazon, Yelp, TripAdvisor</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Mudambi and Schuff (2010)</td><td>Amazon</td><td>√</td><td>√</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>O&#x27;Mahony and Smyth (2010)</td><td>Amazon, TripAdvisor</td><td>√</td><td></td><td>√</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Pan and Zhang (2011)</td><td>Amazon</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td></td><td></td><td></td></tr><tr><td>Racherla and Friske (2012)</td><td>Yelp</td><td></td><td></td><td></td><td></td><td></td><td></td><td>√</td><td></td><td></td></tr><tr><td>Salehan and Kim (2016)</td><td>Amazon</td><td></td><td>√</td><td></td><td>√</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Singh et al. (2017)</td><td>Amazon</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Wang et al. (2018)</td><td>Meta-analysis</td><td>√</td><td>√</td><td>√</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Willemsen et al. (2011)</td><td>Amazon</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>√</td><td></td><td></td></tr><tr><td>Yang et al. (2017)</td><td>Yelp</td><td></td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td></td><td></td></tr><tr><td>Yin et al. (2014)</td><td>Yahoo!</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Zhang and Lin (2018)</td><td>Yelp</td><td>√</td><td>√</td><td></td><td>√</td><td></td><td></td><td>√</td><td>√</td><td></td></tr><tr><td>Zhu et al. (2014)</td><td>Yelp</td><td>√</td><td>√</td><td>√</td><td></td><td></td><td></td><td>√</td><td></td><td></td></tr></table>

## Appendix B

## Estimating Personality Based on Text

We use a deep learning-based NLP model to predict scores on different personality traits, based on algorithms developed by Majumder et al. (2017). The model combines two text modeling approaches, word-to-vector and n-gram, and utilizes the algorithms convolutional neural network (CNN) as the text feature extractor and multiple-layer perceptron (MLP) as the classifier.

CNN (LeCun et al. 1989; LeCun et al. 1998) is one kind of artificial neural network algorithm widely used in deep learning and it performs well in many areas, such as speech recognition, natural language processing (NLP) (dos Santos and Gatti 2014; Kim 2014; Zhang et al. 2015), and image classification (Krizhevsky et al. 2012). CNN is named after the convolution operation in the algorithm and it has a multi-layer network structure. It can extract and analyze global features of input data, which enables it to go beyond the syntactic or semantic structures of natural languages, thus giving it special advantages in analyzing text data. The performance of CNN on text classification has been proven to be competitive to other traditional models (Zhang et al. 2015).

In our model, the raw text data are input from the input layer and processed layer by layer through the middle layers (i.e., the convolution, pooling, and nonlinear mapping layers). The outputs are then fed into a classifier that identifies the final class (or group) of the text data. In training the CNN model, our goal is to learn reviewers’ personality traits according to their review texts, then classify the five personality traits, after which the trained CNN model can produce either a binary classification or a classification probability on each personality trait.

## Model Structure

In the neural network algorithms, each step of data processing is called a “layer.” The CNN model that we use consists of seven layers: input, convolution, max pooling, concatenation, 1-max pooling, fully connected and softmax output. The network structure is shown below in Figure B1.

We use an example to introduce how the CNN model works. As the figure shows, we use a text document with two sentences:

“I will visit India in winter. It is too hot in summer.”

Before extracting personality features, we first prepare the raw data using word segmentation and data cleaning by splitting the text into word or short phrases and removing the invalid words. We ignore sentences that do not carry any personality clues to improve the model performance. After that, the document is divided into two sentences and each sentence is converted into a word sequence:

Sequence 1: “I,” “will,” “visit,” “India,” “in,” “winter”

Sequence 2: “It,” “is,” “too,” “hot,” “in,” “summer”

Then the sequences are fed into the CNN model. The model can be further divided into the following four steps:

Word vectorization: This first layer of the CNN model maps all the words into real-valued vectors using Google’s pre-trained word2vec, a word embedding algorithm for learning vector representations of words. The linear relationships between word vectors reflect the relationship between words in normal parlance. These linear relationships between words in the embedding space also enable us to use word algebra, allowing words to be added and subtracted. For instance, $V _ { C h i n a } - \overline { { V } } _ { B e i j i n g } + V _ { F r a n c e } = V _ { P a r i s e } ,$ in which $V _ { w o r d }$ is the vector of a specific word (Mikolov et al. 2013). This step turns each word in a review into a real-valued vector with fixed length that is set at 300 in our model. Then, those word vectors are turned into a sentence matrix of size $W \times 3 0 0$ , in which ?? is the number of words in the sentence. In our example, the two sentences both have six words, so Sequence 1 and Sequence 2 now can be denoted as $S _ { 1 } , S _ { 2 } \in \mathbb { R } ^ { 6 \times 3 0 0 }$

Sentence vectorization: This step includes the convolution, max pooling, and concatenation layers. We combine the convolution operation with an n-gram linguistic model by using convolution filters with different sizes corresponding to different length n-grams. A n-gram refers to a contiguous sequence of n words in the given sentence (Brown et al. 1992). Many researches use n-gram models to perform text classification and they often choose a set of grams that occur more frequently than the others as the feature space (Cavner and Trenkle 1994; Doddington 2002; Lin and Hovy 2003). A convolution filter represents an array of N values that is convolved with the sentence matrix. In our model, we choose 200 highest-frequency n-grams as convolution filters for each $n = 1 , 2 , 3$ and we use the word vectors of n-grams to construct filter matrices. The $i ^ { \mathrm { { t h } } }$ n-gram filter is noted as $f _ { n i } ^ { c o n v } \in \mathbb { R } ^ { n \times 3 0 0 } , i = 1 , 2 , . . . , 2 0 0$ and row vectors of $f _ { n i } ^ { c o n v }$ are word vectors of the $i ^ { \mathrm { { t h } } }$ n-gram.

![](/api/attachments/APKAA7D3/fulltext/images/387eb8c2f2c4573d9d1e5f5fd6b662de844da70983bc860f24d726994bdcfd84.jpg)  
Note: The network consists of seven layers. The input layers (shown at the bottom) correspond to the sequence of input sentences (only two are shown). The next two layers include three parts, corresponding to trigrams, bigrams, and unigrams. The dotted lines delimit the area in a previous layer to which a neuron of the next layer is connected—for example, the bottom-right rectangle shows the area comprising three-word vectors connected with a trigram neuron. Adopted from Majumder et al. (2017).

Figure B1. Architecture of CNN Model

The filter is convolved with the $j ^ { \mathrm { t h } }$ sentence matrix and generates a feature vector $F V _ { n i } ^ { S _ { j } } \in \mathbb { R } ^ { ( W - n + 1 ) \times 1 }$ . For each $n ,$ we get 200 feature vectors and we combine them into a feature map $F M _ { n } ^ { S _ { j } } \in \mathbb { R } ^ { 2 0 0 \times ( W - n + 1 ) \times 1 } . ^ { 1 5 }$ The convolution layer further introduces nonlinearity by applying the Rectified Linear Unit (ReLU) function to those feature maps. In our example, $W = 6$ and there are two sentences, so we have six feature maps as below:

$$
F M _ {1} ^ {S _ {1}}, F M _ {1} ^ {S _ {2}} \in \mathbb {R} ^ {2 0 0 \times 6 \times 1};
$$

$$
F M _ {2} ^ {S _ {1}}, F M _ {2} ^ {S _ {2}} \in \mathbb {R} ^ {2 0 0 \times 5 \times 1};
$$

$$
F M _ {3} ^ {S _ {1}}, F M _ {3} ^ {S _ {2}} \in \mathbb {R} ^ {2 0 0 \times 4 \times 1}.
$$

After that, in the max pooling layer, each feature map is downsampled to a feature map $D F M _ { n } \in \mathbb { R } ^ { 2 0 0 \times 1 \times 1 }$ , or a feature vector of size 200. Each element in the feature vector is a scalar value equal to the maximum element along the second dimension in the original feature map. In the concatenation layer, three feature vectors are concatenated into a new one. In this way, three feature vectors of size 200 are turned into one sentence vector of length 600. In our example, we get two sentence vectors $s _ { 1 } , s _ { 2 } \in \mathbb { R } ^ { 6 0 0 }$

Document vectorization: This step includes the 1-max pooling layer that first integrates all the sentence vectors from the previous step. In our example, we have two sentence vectors of size 600, so we have a matrix of $2 \times 6 0 0$ . The max-pooling layer chooses the maximum value among the two (number of sentences) for each of the 600 dimensions and returns a document vector $d ^ { \bar { n } e t \bar { w } o r k } \in \mathbb { R } ^ { 6 0 0 }$ . Further, stylistic features (Mairesse $2 0 0 7 ) , \ d ^ { M a i r e s s e } \in \mathbb { R } ^ { 8 4 }$ , are linked with the previous document vectors, resulting in we have a final document vector $d =$ $\left( d ^ { n e t w o r k } , d ^ { M a i r e s s e } \right) \in \mathbb { R } ^ { 6 8 4 }$

Classification: This step includes the last two layers of a MLP classifier: linear with Sigmoid activation and two neuron softmax output. The goal of the linear with Sigmoid activation layer is to reduce the dimension of the document vector generated in the previous step to 200. We first multiply the document vector by a full-connection weight matrix $W ^ { f c } \in \mathbb { R } ^ { 6 8 4 \times 2 0 0 }$ and add a bias vector $B ^ { f c } \in \mathbb { R } ^ { 2 0 0 }$ , then use Sigmoid activation function to calculate the reduced document vector $\boldsymbol { d } ^ { f \bar { c } } \in \mathbb { R } ^ { 2 0 0 }$

$$
d ^ {f c} = \text { Sigmoid } (d W ^ {f c} + B ^ {f c}),
$$

where

$$
S i g m o i d (x) = \frac {1}{1 + \exp (- x)}.
$$

The two neuron softmax output determines the probability of the document vector belonging to the class yes or no by a softmax function and produces the final classification result as well as the probabilities associated with it. The output can be expressed as a binary vector of size 2:

$$
\left(x _ {y e s}, x _ {n o}\right) = d ^ {f c} W ^ {s o f t m a x} + B ^ {s o f t m a x},
$$

where $W ^ { s o f t m a x } \in \mathbb { R } ^ { 2 0 0 \times 2 }$ and $B ^ { s o f t m a x } \in \mathbb { R } ^ { 2 }$ . The class probability is calculated as:

$$
P (i | \text {network parameters}) = \frac {\exp (x _ {i})}{\exp (x _ {y e s}) + \exp (x _ {n o})} \text {for} i \in \{y e s, n o \}.
$$

## Model Training

The model was trained using stochastic gradient descent with Adadelta algorithm with negative log likelihood as the objective function (for details, see Zeiler 2012). It converged after 66 epochs and achieved 98.4% percent training accuracy.

## Appendix C

## Variables

## Dependent Variable

Our dependent variable is the number of helpfulness votes for each review on Yelp. Yelp only allows readers to vote “yes” on the review’s helpfulness if they choose to vote at all. Figure C1 shows a review for Café De Jour in the Pittsburgh, PA area. Readers of this review anonymously voted whether this review is useful, cool, and/or funny, although our study focuses only on the useful dimension. (As discussed in the text body we equate “helpfulness” with “useful” votes on Yelp to be consistent with the literature.) In this example, the review has three helpfulness votes. Given that the distribution of votes is heavily skewed, we follow the literature and use the logarithm transformation of (the number of useful votes plus 1) as the dependent variable.

![](/api/attachments/APKAA7D3/fulltext/images/5c1e943f76dc64736f7d2998f39207cf67803e241b5e33a2e007f6a79816b314.jpg)  
Figure C1. Screenshot of a Yelp Review

## Personality Traits

We follow the procedure described in Appendix B to estimate the Big Five personality traits: openness, conscientiousness, extraversion, agreeableness, and emotional stability.

## Control Variables—Characteristics of Review Text

Star rating of the review. Besides the review text, a reviewer also gives the restaurant a discrete number of stars (Star), ranging from 1 to 5 (1 is low), signifying his/her overall satisfaction with the dining experience. In the literature, star rating has been one of the most important predictors of review helpfulness (see previous literature review). The average star rating for our sample is 3.58.

Star square. Following the literature (Mudambi and Schuff 2010), we add a square term of the star rating to account for the possible nonlinear relationship between star rating and helpfulness votes.

Readability. Reading difficulty (or, conversely, understandability of the text) may also impact a reader’s evaluation of review helpfulness. Following previous literature (Ghose and Ipeirotis 2011; Pan and Zhang 2011; Yin et al. 2014), we calculate the Coleman-Liau Index, an estimate of the U.S. grade level necessary to read and understand the text (Coleman and Liau 1975), to control for review reading difficulty. On average, the reviews in our dataset were written at a ninth-grade level.

Existing days. An earlier review may accumulate more votes simply because it has been online for a longer time. Following previous literature (e.g., Berger and Milkman 2012; Godes and Silva 2012; Mudambi and Schuff 2010), we add a time control variable, Existing\_days, calculated as the days between the review’s publication date and the last date of the data sample (January 5, 2013).

Word count. A longer review may get more votes on helpfulness because it may contain more information (Yin et al. 2014). We use the total number of words contained in the review text. The average word count for our sample is 127 words.

Positivity and Negativity. Previous research shows that sentiments expressed in the review text influence its helpfulness (Berger and Milkman 2012; Yin et al. 2014). To control for the impact on review helpfulness from sentiment words, we use standardized percentages of positive and negative emotion words (as calculated by LIWC) in a review.

## Control Variables—Store Characteristics

Business star. Besides the characteristics associated with each review, the review helpfulness rating may be conditional on restaurant characteristics, such as overall reputation and cuisine type. Following previous literature (Yin et al. 2014), we use average star ratings as indices for restaurants’ overall reputations (Business\_star).

Price range. Most restaurants reviewed on Yelp are listed with dollar signs to signify the average spending per person—i.e., \$ = under 10 dollars; \$\$ = 11-30 dollars; \$\$\$ = 31-60 dollars; \$\$\$\$ = over 60 dollars. We crawled this data for each of the restaurants in our dataset.

Sequential effect at business level. Godes and Silva (2012) find that temporal (time) and sequential (rank) effects are two different dynamic processes. We control for the sequential effect of reviews for the same restaurant. The rank of a particular review among all reviews (Review\_rank\_business) may have great impact on its helpfulness votes, even after controlling for the time effect. For example, the first few reviews are likely to be read first and may provide readers with the most important information about the restaurant and therefore get more helpfulness votes. On the other hand, it is possible that later reviews build upon previous reviews and provide information from different angles, which may be appreciated by readers and therefore get more helpfulness votes.

Cuisine type. We use dummies to indicate the following cuisine types: Asian, European, South American, Middle Eastern, and Other, with American as the holdout category.

## Control Variables—Reviewer Characteristics

Sequential effect at reviewer level. A reviewer can learn from experience how to write a review to get more helpfulness votes. We use the rank of the review among all the reviews a reviewer published (Review\_rank\_user) to control for such a learning process. Local. Locals are presumed to have certain knowledge regarding the area and their reviews may be deemed as more reliable (and therefore helpful) than non-locals. Therefore, we create a dummy to indicate whether the reviewer is local (i.e., the reviewer’s location city is the same as the restaurant’s location city).

## Appendix D

## Instrumental Variable (IV) and Endogeneity Tests

## Tests of IV Strength and Validity (Bascle 2008)

To test IV strength, we use the Angrist-Pischke (2009) multivariate F-statistic. In the first-stage regressions of endogenous variables (openness to experience, conscientiousness, extraversion, agreeableness, and emotional stability), the p-values corresponding to the Angrist-Pischke F statistic are all below 0.001, thus rejecting the null hypothesis of weak instruments.

This is further confirmed by the Craig-Donald Wald F statistic (Cragg and Donald 1993) for weak identification. The result of the joint test of personality traits IVs (F (7, 4026) = 2.457, p-value=0.000) rejects the null hypothesis that the IVs are weak.

We use the Kleibergen-Paap rk LM statistic (Kleibergen, 2002) to test for underidentification of the instrument variables jointly. The results statistic (Chi-sq (3) = 18.473, p-value = 0.000) rejects the under-identification hypothesis.

We use the Hansen J test to test the overidentification condition of the IVs, or the null hypothesis that the IVs are uncorrelated with the error term (i.e., IV validity). The result is not significant (J statistic=4.243, p=0.120); we thus fail to reject the null. Based on these results, we conclude that the IVs are sufficiently valid.

## Tests of the Endogeneity of Personality Trait Variables

The difference-in-Sargan test statistics (chi2(5) = 283.358, p = 0.000) after the GMM specification rejects the null hypothesis that our personality variables are exogenous.

Similarly, the Wu-Hausman test statistic (F(5, 94967) = 59.213, p-value = 0.000) after 2SLS estimation again rejects the null hypothesis.

This is confirmed by the Durbin Chi-sq (chi2(5) = 295.233, p-value = 0.000). Therefore, we should address the endogeneity of personality trait scores and our IV approaches are more suitable than ones without considering endogeneity.

## Appendix E

## Cross-validation for Regression

To assess the generalizability of our model and to test for overfitting, we use a set of model evaluation methods called cross-validation (a.k.a., out-of-sample testing) (Picard and Cook1984). In cross-validation, the data are first split into subsets, then those subsets are used to test the performance of the model. Given that the training sample is independent from the test sample, cross-validation avoids an overfitting problem (Arlot and Celisse 2010). We use both the holdout sample validation and the k-fold cross-validation to ensure the robustness of our results.

To conduct the holdout sample validation, we use the parameter estimates from the training sample to forecast review helpfulness for the remaining test sample. Following Drèze et al. (2004), we compare the mean squared-errors (MSE) for both in-sample and out-of-sample to see if there is evidence of overfitting. Given the negligible difference in the MSE (0.883 for in-sample and 0.839 for out-of-sample), we did not find support for overfitting.

We then use k-fold cross-validation, with k equal to five, to derive a more accurate estimate of model prediction performance. In a way, k-fold cross-validation is an improvement over the holdout sample validation: Instead of being partitioned into two complementary subsets, the data are now divided into k equal-sized subsets and the sample validation is repeated k times. Each time, one of the k subsets is used as the test set and the other k-1 subsets are pooled together as the training set. Then the errors across all k trials are averaged to produce a single estimation of the performance measure. Compared to the holdout sample validation, k-fold cross-validation has merit because it matters less how the data are divided: Every data point in the dataset is eventually used for both training and testing and “all the data are used (randomly) as a holdout once” (Sood et al. 2009). Given the large sample size of our data, we conduct a five-fold cross-validation and compute the MAE to check for there is evidence of over-fitting (Blanchard et al. 2016; Sood et al. 2009). Again, we fail to find such evidence with an in-sample MAE of 0.664, while the five-fold cross-validation found a median MAE of 0.654 (Mean = 0.675, SD = 0.060; Min = 0.601, Max = 0.747).

## Appendix F

## Developing the Ensemble of Ensembles Model

In this appendix, we elaborate on the procedure for developing our predictive model, the ensemble of ensembles model (graphically shown in Figure 3 in the paper). We first select three algorithms commonly used by prior research to analyze online reviews—support vector machine (SVM) (e.g., Ghose and Ipeirotis 2011; Hong et al. 2012; Jin and Liu 2010; Kim and Pantel 2006; Zheng et al. 2013); decision tree (e.g., Jin and Liu 2010; Zheng et al. 2013); and naive Bayes algorithms (e.g., Jin and Liu 2010; Zheng et al. 2013)—and build three ensemble models based on them: that is, ensemble support vector machine (E-SVM) based on SVM; random forest (RF) based on decision tree; and adaptive boostin (AdaBoost) based on naive Bayes. We then combine the three ensemble models by the method of majority voting.

## E-SVM

We follow the literature (Huang and Zhang 2013; Wang et al. 2014 and used a multifeature voting method to develop the E-SVM model. Specifically, we used different sets of features to train multiple SVM classifiers and then determined the final classification by probability weighting based on the outcomes of those SVM classifiers. (See Wang et al. 2014 for details.) The procedure includes five steps as shown in Table F1.

<table><tr><td colspan="2">Table F1. E-SVM</td></tr><tr><td>Step 1</td><td>Train five SVM classifiers, corresponding to the five personality traits, respectively. For each personality trait, we train an SVM classifier by combing the personality trait with the benchmark features (i.e., the number of the reviewer&#x27;s past reviews and a “local” variable indicating whether the reviewer is from the same city as the restaurant&#x27;s location, as discussed in the Discussion section of the paper) as the input for the SVM classifier. Doing so gives us five independent SVM classifiers (for the five personality traits, respectively), denoted as  $SVM_i$  ( $i=1,2,3,4,5$ ).</td></tr><tr><td>Step 2</td><td>Calculate the probabilistic output of  $SVM_i$  for the  $j^{\text{th}}$  review,  $p_{ij}^{k}$ , where  $k (=1,-1)$  represents the class label (=helpful, unhelpful).</td></tr><tr><td>Step 3</td><td>Calculate the certainty of each SVM classification: $S_{ij} = p_{ij}^{1} - p_{ij}^{-1}$ . $S_{ij}$  is the specificity measure (Yager 1992), which gauges the certainty of the classifier  $SVM_i$ . The larger the value of  $S_{ij}$ , the more reliable the  $SVM_i$  classification for the  $j^{\text{th}}$  review.</td></tr><tr><td>Step 4</td><td>Calculate the probabilistic output of  $k=1$  for the  $j^{\text{th}}$  review using weight averaging as follows: $p_j^1 = \frac{\sum_{i=1}^{5} S_{ij} \cdot p_{ij}^1}{5}$ </td></tr><tr><td>Step 5</td><td>If  $p_j^1 \geq threshold$ :the  $j^{\text{th}}$  review is classified into the “helpful” class;else:the  $j^{\text{th}}$  review is classified into the “unhelpful” class.</td></tr></table>

## Random Forest

Random forest (RF) is a classical ensemble algorithm based on decision tree (Breiman 2001). It is one of the most popular machine learning algorithms and it performs well on various machine classification tasks (e.g., Díaz-Uriarte and De Andres 2006; Pal 2005; Rodriguez-Galiano et al. 2012). RF uses the bagging ensemble algorithm that bootstraps samples from the training data and correspondingly trains a set of decision trees based on the bootstrapped samples, respectively. This approach helps produce a more reliable model estimation. Based on predictions of the individual decision trees, RF uses the method of majority voting to determine the final classification. Table F2 presents the procedure of RF modeling in our study.

## AdaBoost

We used the AdaBoost algorithm (Freund and Schapire 1997) to implement an ensemble model based on a naive Bayes method. It uses boosting as the ensemble method, which involves incrementally building an ensemble by increasing the occurrence probability of previously misclassified examples (Gutierrez 2015). The procedure is shown in Table F3.

<table><tr><td colspan="2">Table F2. Random Forest</td></tr><tr><td>Step 1</td><td>Draw n bootstrapped samples from the training data, where n is the number of decision trees to be developed. In our work, we set n = 60.</td></tr><tr><td>Step 2</td><td>For each of the bootstrapped samples, randomly choose m features from all the input features and use them to train a decision tree. In our model, m equals 3.</td></tr><tr><td>Step 3</td><td>Aggregate the prediction results of the n decision trees by majority voting.Given the  $j^{th}$  review, if more than half of the decision trees predict the review as “helpful”:the  $j^{th}$  review is classified into the “helpful” class;else:the  $j^{th}$  review is classified into the “unhelpful” class.</td></tr></table>

<table><tr><td colspan="2">Table F3. AdaBoost</td></tr><tr><td>Step 1</td><td>Set parameters: k: current iteration number. The initial value of k is 0.  $k_{max}$ : the maximum iterations. We set it at 45. $W_k(i)$ : the weight of sample  $x_i$  while calculating the classification error rate in the  $K^{th}$  iteration. The initial value of  $W_k(i)$  is  $\frac{1}{N}$ , where N is the training sample size.</td></tr><tr><td>Step 2</td><td>Draw a set of training examples  $Train_k = \{(x_1,y_1),(x_2,y_2),..., (x_N,y_N)\}$  with weight  $W_k(i)$ , where  $x_i$  is the input variables for the  $I^{th}$  review (personality traits and benchmark features) and  $y_i \in \{+1,-1\}$  is the output variable (corresponding to “helpful” and “unhelpful,” respectively).</td></tr><tr><td>Step 3</td><td>Train a naive Bayes classifier  $C_k(x)$ :  $\mathcal{X} \to \{+1,-1\}$ .</td></tr><tr><td>Step 4</td><td>Calculate the training estimate error rate  $E_k = \sum_{i=1}^{N} W_k(i) I(C_k(x_i) \neq y_i)$ , where  $I(\cdot) = 1$  is an indicator function.</td></tr><tr><td>Step 5</td><td>Calculate  $\alpha_k$  and  $W_{k+1}(i)$ :  $\alpha_k = \frac{1}{2} \ln \frac{1 - E_k}{E_k}$ , $W_{k+1}(i) = \frac{W_k(i)}{Z_k} \exp(-\alpha_k y_i C_k(x_i))$ ,where  $Z_k = \sum_{i=1}^{N} W_k(i) \exp(-\alpha_k y_i C_k(x_i))$ .</td></tr><tr><td>Step 6</td><td>Back to Step 2, until =  $k_{max}$ .</td></tr><tr><td>Step 7</td><td>The ensemble classifier is  $C(x) = sign(\sum_{k=1}^{k_{max}} \alpha_k C_k(x))$ .</td></tr></table>

## Ensemble of Ensembles

Lastly, we used the majority voting method to aggregate the classification results of the three ensemble models as reported above.

## Appendix References

Angrist, J. D., and Pischke, J. S. 2009. Mostly Harmless Econometrics: An Empiricist’s Companion, Princeton, NJ: Princeton University Press.

Arlot, S., and Celisse, A. 2010. “A Survey of Cross-Validation Procedures for Model Selection,” Statistics Surveys (4), pp. 40-79.

Blanchard, S. J., Aloise, D., and DeSarbo, W. S. 2016. “Extracting Summary Piles from Sorting Task Data,” Journal of Marketing Research (54:3) pp. 398-414.

Baek, H., Ahn, J. H., and Choi, Y. 2012. “Helpfulness of Online Consumer Reviews: Readers’ Objectives and Review Cues,” International Journal of Electronic Commerce (17:2), pp. 99-126.

Bascle, G. 2008. “Controlling for Endogeneity with Instrumental Variables in Strategic Management Research,” Strategic Organization (6:3), pp. 285-327.

Berger, J., and Milkman, K. L. 2012. “What Makes Online Content Viral?” Journal of Marketing Research (49:2), pp. 192-205.

Breiman, L. 2001. “Random Forests,” Machine Learning (45:1), pp. 5-32.

Brown, P. F., Desouza, P. V., Mercer, R. L., Pietra, V. J. D., and Lai, J. C. 1992. “Class-Based N-gram Models of Natural Language,” Computational Linguistics (18:4), pp. 467-479.

Cao, Q., Duan, W., and Gan, Q. 2011. “Exploring Determinants of Voting for the ‘Helpfulness’ of Online User Reviews: A Text Mining Approach,” Decision Support Systems (50:2), pp. 511-521.

Cavnar, W. B., and Trenkle, J. M. 1994. “N-Gram-Based Text Categorization,” in Proceedings of 3rd Annual Symposium on Document Analysis and Information Retrieval, pp. 161-175.

Chua, A. Y., and Banerjee, S. 2016. “Helpfulness of User-Generated Reviews as a Function of Review Sentiment, Product Type and Information Quality,” Computers in Human Behavior (54:C), pp. 547-554.

Coleman, M., and Liau, T. L. 1975. “A Computer Readability Formula Designed for Machine Scoring,” Journal of Applied Psychology (60:2), pp. 283-284.

Cragg, J. G., and Donald, S. G. 1993. “Testing Identifiability and Specification in Instrumental Variable Models,” Econometric Theory (9:2) pp. 222-240.

Danescu-Niculescu-Mizil, C., Kossinets, G., Kleinberg, J., and Lee, L. 2009. “How Opinions Are Received by Online Communities: A Case Study on Amazon.com Helpfulness Votes,” in Proceedings of the 18th International Conference on World Wide Web, pp. 141-150.

Díaz-Uriarte, R., and De Andres, S. A. 2006. “Gene Selection and Classification of Microarray Data Using Random Forest,” BMC Bioinformatics (7:1), pp. 3.

Doddington, G. 2002. “Automatic Evaluation of Machine Translation Quality Using N-Gram Co-Occurrence Statistics,” in Proceedings of the Second International Conference on Human Language Technology Research, pp. 138-145.

dos Santos, C., and Gatti, M. 2014. “Deep Convolutional Neural Networks for Sentiment Analysis of Short Texts,” in Proceedings of the 25th International Conference on Computational Linguistics: Technical Papers, pp. 69-78.

Drèze, X., Nisol, P., and Vilcassim, N. J. 2004. “Do Promotions Increase Store Expenditures? A Descriptive Study of Household Shopping Behavior,” Quantitative Marketing and Economics (2:1), pp. 59-92.

Forman, C., Ghose, A., and Wiesenfeld, B. 2008. “Examining the Relationship Between Reviews and Sales: The Role of Reviewer Identity Disclosure in Electronic Markets,” Information Systems Research (19:3), pp. 291-313.

Freund, Y., and Schapire, R. E. 1997. “A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting,” Journal of Computer and System Sciences (55:1), pp. 119-139.

Ghose, A., and Ipeirotis, P. G. 2011. “Estimating the Helpfulness and Economic Impact of Product Reviews: Mining Text and Reviewer Characteristics,” IEEE Transactions on Knowledge and Data Engineering (23:10), pp. 1498-1512.

Godes, D., and Silva, J. C. 2012. “Sequential and Temporal Dynamics of Online Opinion,” Marketing Science (31:3), pp. 448-473.

Gutierrez, D. D. 2015. Machine Learning and Data Science: An Introduction to Statistical Learning Methods with R, Bradley Beach, NJ: Technics Publications.

Hong, Y., Lu, J., Yao, J., Zhu, Q., and Zhou, G. 2012. “What Reviews Are Satisfactory: Novel Features for Automatic Helpfulness Voting,” in Proceedings of the 35th International ACM SIGIR Conference on Research and Development in Information Retrieval, pp. 495-504.

Huang, A. H., Chen, K., Yen, D. C., and Tran, T. P. 2015. “A Study of Factors that Contribute to Online Review Helpfulness,” Computers in Human Behavior (48:C), 17-27.

Huang, X., and Zhang, L. 2013. “An SVM Ensemble Approach Combining Spectral, Structural, and Semantic Features for the Classification of High-Resolution Remotely Sensed Imagery,” IEEE Transactions on Geoscience and Remote Sensing (51:1), pp. 257-272.

Jin, J., and Liu, Y. 2010. “How to Interpret the Helpfulness of Online Product Reviews: Bridging the Needs Between Customers and Designers,” in Proceedings of the 2nd International Workshop on Search and Mining User-Generated Contents, pp. 87-94.

Karimi, S., and Wang, F. 2017. “Online Review Helpfulness: Impact of Reviewer Profile Image,” Decision Support Systems (96), pp. 39-48.

Kim, S. M., Pantel, P., Chklovski, T., and Pennacchiotti, M. 2006. “Automatically Assessing Review Helpfulness,” in Proceedings of the 2006 Conference on Empirical Methods in Natural Language Processing, pp. 423-430.

Kim, Y. 2014. “Convolutional Neural Networks for Sentence Classification,” in Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing, pp. 1746–1751.

Kleibergen, F. 2002. “Pivotal Statistics for Testing Structural Parameters in Instrumental Variables Regression,” Econometrica (70:5), pp. 1781-1803.

Korfiatis, N., García-Bariocanal, E., and Sánchez-Alonso, S. 2012. “Evaluating Content Quality and Helpfulness of Online Product Reviews: The Interplay of Review Helpfulness vs. Review Content,” Electronic Commerce Research and Applications (11:3), pp. 205-217.

Krizhevsky, A., Sutskever, I., and Hinton, G. E. 2012. “Imagenet Classification with Deep Convolutional Neural Networks,” in Advances in Neural Information Processing Systems, pp. 1097-1105.

Kwok, L., and Xie, K. L. 2016. “Factors Contributing to the Helpfulness of Online Hotel Reviews: Does Manager Response Play a Role?” International Journal of Contemporary Hospitality Management (28:10), pp. 2156-2177.

LeCun, Y., Boser, B., Denker, J. S., Henderson, D., Howard, R. E., Hubbard, W., and Jackel, L. D. 1989. “Backpropagation Applied to Handwritten Zip Code Recognition,” Neural Computation (1:4), pp. 541-551.

LeCun, Y., Bottou, L., Bengio, Y., and Haffner, P. 1998. “Gradient-Based Learning Applied to Document Recognition,” Proceedings of the IEEE (86:11), pp. 2278-2324.

Lin, C. Y., and Hovy, E. 2003. “Automatic Evaluation of Summaries Using N-Gram Co-Occurrence Statistics,” in Proceedings of the 2003 Conference of the North American Chapter of the Association for Computational Linguistics on Human Language Technology-Association for Computational Linguistics, pp. 71-78.

Liu, Z., and Park, S. 2015. “What Makes a Useful Online Review? Implication for Travel Product Websites,” Tourism Management (47:C), pp. 140-151.

Lu, S., Wu, J., and Tseng, S. L. A. 2018. “How Online Reviews Become Helpful: A Dynamic Perspective,” Journal of Interactive Marketing (44), pp. 17-28.

Mairesse, F., Walker, M. A., Mehl, M. R., and Moore, R. K. 2007. “Using Linguistic Cues for the Automatic Recognition of Personality in Conversation and Text,” Journal of Artificial Intelligence Research (30), pp. 457-500.

Majumder, N., Poria, S., Gelbukh, A., and Cambria, E. 2017. “Deep Learning-Based Document Modeling for Personality Detection from Text,” IEEE Intelligent Systems (32:2), pp. 74-79.

Martin, L., and Pu, P. 2014. “Prediction of Helpful Reviews Using Emotions Extraction,” in Twenty-Eighth AAAI Conference on Artificial Intelligence, pp. 1551-1557.

Mikolov, T., Chen, K., Corrado, G., and Dean, J. 2013. “Efficient Estimation of Word Representations in Vector Space,” arXiv.org (https://arxiv.org/abs/1301.3781).

Mudambi, S. M., and Schuff, D. 2010. “What Makes a Helpful Review? A Study of Customer Reviews on Amazon.com,” MIS Quarterly (34:1), pp. 185-200.

O’Mahony, M. P., and Smyth, B. 2010. “Using Readability Tests to Predict Helpful Product Reviews,” in Paper Presented at the 9th International Conference on Adaptivity, Personalization and Fusion of Heterogeneous Information, pp. 164-167.

Pal, M. 2005. “Random Forest Classifier for Remote Sensing Classification,” International Journal of Remote Sensing (26:1), pp. 217-222.

Pan, Y., and Zhang, J. Q. 2011. “Born Unequal: A Study of the Helpfulness of User-Generated Product Reviews,” Journal of Retailing (87:4), pp. 598-612.

Picard, R. R., and Cook, R. D. 1984. “Cross-Validation of Regression Models,” Journal of the American Statistical Association (79:387), pp. 575-583.

Racherla, P., and Friske, W. 2012. “Perceived ‘Usefulness’ of Online Consumer Reviews: An Exploratory Investigation Across Three Services Categories,” Electronic Commerce Research and Applications (11:6), pp. 548-559.

Rodriguez-Galiano, V. F., Ghimire, B., Rogan, J., Chica-Olmo, M., and Rigol-Sanchez, J. P. 2012. “An Assessment of the Effectiveness of a Random Forest Classifier for Land-Cover Classification,” ISPRS Journal of Photogrammetry and Remote Sensing (67), pp. 93-104.

Salehan, M., and Kim, D. J. 2016. “Predicting the Performance of Online Consumer Reviews: A Sentiment Mining Approach to Big Data Analytics,” Decision Support Systems (81), pp. 30-40.

Singh, J. P., Irani, S., Rana, N. P., Dwivedi, Y. K., Saumya, S., and Roy, P. K. 2017. “Predicting the ‘Helpfulness’ of Online Consumer Reviews,” Journal of Business Research (70), pp. 346-355.

Sood, A., James, G. M., and Tellis, G. J. 2009. “Functional Regression: A New Model for Predicting Market Penetration of New Products,” Marketing Science (28:1), pp. 36-51.

Wang, Y., Wang, J., and Yao, T. 2018. “What Makes a Helpful Online Review? A Meta-Analysis of Review Characteristics,” Electronic Commerce Research (19), pp. 1-28.

Wang, Y., Zhang, Y., Zhuo, T., and Liao, M. 2014. “Ensemble Learning Based on Multi-Features Fusion and Selection for Polarimetric SAR Image Classification,” in Proceedings of the 12th IEEE International Conference on Signal Processing, pp. 734-737.

Willemsen, L. M., Neijens, P. C., Bronner, F., and de Ridder, J. A. 2011. “‘Highly Recommended!’ The Content Characteristics and Perceived Usefulness of Online Consumer Reviews,” Journal of Computer-Mediated Communication (17:1) pp. 19-38.

Yager, R. R. 1992. “On the Specificity of a Possibility Distribution,” Fuzzy Sets and Systems (50:3), pp. 279-292.

Yang, S. B., Hlee, S., Lee, J., and Koo, C. 2017. “An Empirical Examination of Online Restaurant Reviews on Yelp.com: A Dual Coding Theory Perspective,” International Journal of Contemporary Hospitality Management (29:2), pp. 817-839.

Yin, D., Bond, S., and Zhang, H. 2014. “Anxious or Angry? Effects of Discrete Emotions on the Perceived Helpfulness of Online Reviews,” MIS Quarterly (38:2), pp. 539-560.

Zeiler, M. D. 2012. “ADADELTA: An Adaptive Learning Rate Method,” arXiv.org (https://arxiv.org/abs/1212.5701).

Zhang, Y., and Lin, Z. 2018. “Predicting the Helpfulness of Online Product Reviews: A Multilingual Approach,” Electronic Commerce Research and Applications (27), 1-10.

Zhang, X., Zhao, J., and LeCun, Y. 2015. “Character-Level Convolutional Networks for Text Classification,” in Advances in Neural Information Processing Systems, Montréal, Canada, December 7-12, pp. 649-657.

Zheng, X., Zhu, S., and Lin, Z. 2013. “Capturing the Essence of Word-Of-Mouth for Social Commerce: Assessing the Quality of Online E-Commerce Reviews by a Semi-Supervised Approach,” Decision Support Systems (56), pp. 211-222.

Zhu, L., Yin, G., and He, W. 2014. “Is This Opinion Leader’s Review Useful? Peripheral Cues for Online Review Helpfulness,” Journal of Electronic Commerce Research (15:4), pp. 267-280.
