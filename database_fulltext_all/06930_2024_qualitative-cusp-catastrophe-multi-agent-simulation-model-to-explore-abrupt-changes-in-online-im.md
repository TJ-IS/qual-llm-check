---
otero_id: 6930
otero_key: "2DPA3VR6"
title: "Qualitative Cusp Catastrophe Multi-Agent Simulation Model to Explore Abrupt Changes in Online Impulsive Buying Behavior"
authors: "Xiaochao Wei; Yanfei Zhang; Xin (Robert) Luo; Gangmei Pan; Guihua Nie"
year: "2024"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00832"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
2024

# Qualitative Cusp Catastrophe Multi-Agent Simulation Model to Explore Abrupt Changes in Online Impulsive Buying Behavior

Xiaochao Wei , weixiaochaowin@163.com

Yanfei Zhang , 15171431742@163.com

Gangmei Pan , 1225985074@qq.com

Guihua Nie , niegh@whut.edu.cn

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# Qualitative Cusp Catastrophe Multi-Agent Simulation Model to Explore Abrupt Changes in Online Impulsive Buying Behavior

Xiaochao Wei,<sup>1</sup> Yanfei Zhang,<sup>2</sup> Xin (Robert) Luo, <sup>3</sup> Gangmei Pan,<sup>4</sup> Guihua Nie<sup>5</sup>

<sup>1</sup>Wuhan University of Technology, China, weixiaochaowin@163.com <sup>2</sup>Wuhan University of Technology, China, 15171431742@163.com <sup>3</sup>Anderson School of Management, The University of New Mexico, USA, xinluo@unm.edu <sup>4</sup>Wuhan University of Technology, China, 1225985074@qq.com <sup>5</sup>Wuhan University of Technology, China, niegh@whut.edu.cn

## Abstract

We develop a qualitative catastrophe (a nonlinear sudden violent change) multi-agent simulation model to investigate the evolution of group behavior, specifically abrupt changes in online impulsive buying (OIB) behavior. Studies have rarely investigated the mechanism of abrupt changes in OIB at the group level. To address the research gaps and advance this area of research, we employed a sequential multiple-methods approach. First, we designed a questionnaire to obtain and analyze consumer data to identify OIB drivers. Second, we built a qualitative catastrophe model based on empirical findings to describe sudden changes in the OIB behavior of individuals by merging catastrophe theory (CT) and qualitative simulation (QSIM). Finally, grounded in the qualitative catastrophe model, we constructed an agent-based model (ABM) to simulate group-level OIB behavior. The empirical findings revealed the following. (1) Sudden changes in group-level OIB occur as consumers’ sense of quantified self increases when self-control is low. (2) The greater the number of consumers with a proving preference (who prefer to prove their competence and performance to others) in the group, the higher the possibility of catastrophe; the scale of catastrophe increases significantly with the enhancement of product information features. (3) We identify optimal gamification for sudden increases in group-level OIB; the larger the degree of social networking is, the higher the likelihood of catastrophe behavior. Our proposed combination of a survey study, QSIM, and an ABM is a plausible solution for behavioral research on consumers, and the integration paradigm could help maintain market stability and promote products.

Keywords: Online Impulse Buying, Catastrophe Theory, Qualitative Simulation, Agent-Based Model, Empirical Study

John Qi Dong was the accepting senior editor. This research article was submitted on January 11, 2021 and underwent six revisions. Xin (Robert) Luo is the corresponding author.

## 1 Introduction

With the rapid rise of online shopping, online impulsive buying (OIB) has become an increasingly prevalent phenomenon that has aroused the interest of information systems (IS) researchers and practitioners. In essence, the convenience of online shopping and rich environmental incentives make it easier for consumers to make impulsive purchases in the online environment than in the offline environment. It is estimated that more than 50% of online purchases are impulsive (Kimiagari & Asadi Maladfe, 2021; Wu et al., 2020; Zheng et al., 2019). In 2019, the Double Eleven Alibaba Shopping Carnival in China generated 268.4 billion yuan in revenue, more than the combined revenue from Black Friday and Cyber Monday in the

United States. This astonishing figure unquestionably included many impulse purchases. It is critical to comprehend the mechanism behind this abrupt behavior change to regulate group OIB behavior.

In this study, OIB is defined as a spontaneous and unplanned internet purchase (Chan et al., 2017). This means that there is no demand prior to purchase; consumers make impulsive purchases because of stimuli such as personalized recommendations from ecommerce platforms or promotions from Facebook, Twitter, or Instagram influencers. In this abrupt change process, OIB is essentially the result of a shift in behavioral elements. Despite the momentum of this topic, only a limited number of studies on OIB have employed the mechanism of abrupt change and investigated the evolution of OIB behavior at the group level. OIB drivers, including external environmental stimuli (website environments or other offline stimuli), consumer personality traits, and purchase situational factors, have been the subject of most studies employing a survey approach (Dholakia, 2000; Verplanken & Herabadi, 2001; Wells et al., 2011; Floh & Madlberger, 2013; Vonkeman et al., 2017).

However, there are at least three fundamental limitations in previous studies. First, these empirical studies were typically confined to a single time period, making it difficult to investigate the dynamic behavioral trajectory of OIB. Second, rather than examining the dynamic rapid shift in OIB at the group level, they focused on identifying OIB factors and their relationships. Third, they cannot be applied to a sudden change in group-level OIB emerging from individual behavioral interaction. Thus, there is a need to curb the ambiguous, incomplete, and time-varying psychological or behavioral trajectory of OIB, that is, sudden and dynamic group-level changes in OIB (Davis et al., 1989; Davis, 1989).

Compared with individual-level mechanisms, social influence (i.e., social nature, social dynamics, and the bandwagon effect) in group-level OIB can more effectively promote market performance, and the use of quantified tools makes this process more convenient. For example, on social media, the stimulation of information sharing can increase the volume of impulse buying by more than 40%.<sup>1</sup> First, the social nature of OIB, which is increasingly reflected in the emergence of online communities with common interests, refers to the influence of peers on purchasing decisions. The presence of peers can increase the urge to purchase (Luo, 2005), and the quantified self (i.e., the process in which individuals use quantified tools to monitor their bodies, states, and behaviors and obtain timely and accurate feedback and recommendations to improve their self-knowledge) can change users’ buying habits and brand preferences (Fuel, 2014). Nearly 90% of Chinese consumers belong to such communities, and most prefer to buy products recommended by their community.<sup>2</sup> Second, the social dynamics of group-level OIB can also increase consumer buying intention by leveraging social media as a new platform for experience sharing and comment posting. The design of quantified-self features in online communities such as gamification also provides users with more information to share. According to a recent study, 87% of consumers were willing to share experiences and comments, and 55% already had. <sup>3</sup> For example, according to Bankrate, approximately half of social media users make impulse purchases based on what they see in their feeds compared with 75% in SoFi’s survey. <sup>4</sup> <sup>,</sup> <sup>5</sup> Third, the prevalence of the bandwagon effect in online communities can promote consumers’ purchasing level for better market performance. Previous studies have confirmed that groups subject to the bandwagon effect are more likely to be influenced by peers in their purchasing decisions (Tsai et al., 2013). Accordingly, group-level OIB can enhance consumers’ purchase levels for better market performance and support retail activity management and customer segmentation.

Guided by the above practical and theoretical motivations, we study the sudden and dynamic grouplevel changes in OIB. We address the following research question: “How can abrupt changes in grouplevel OIB emerge from individual interactions?” To answer this question, an integrated paradigm combining individual-level qualitative methods and group-level quantitative methods is needed.

We propose an integrated simulation framework subsuming a survey study, a qualitative simulation (QSIM), and an agent-based model (ABM) to probe sudden group-level changes in OIB. This multimethod approach can leverage mutually reinforcing strengths from different methods (Dong, 2022): the survey is exploratory and cross-sectional to identify attributes of OIB behavior, QSIM further uncovers the underlying mechanisms about how the attributes of OIB behavior work over time, and finally, the ABM allows for the analysis of OIB behavior from the individual to the group level. First, traditional empirical models of OIB must be modified to handle features of the IT-enabled quantified self in online communities (Wannheden et al., 2021; Huotari & Hamari, 2017; Vesa et al., 2017). To more accurately capture individual-level attributes and behavioral mechanisms underlying sudden grouplevel changes in OIB in this particular case with the ITenabled quantified self, we start with a survey rather than drawing on the literature to identify OIB factors and their underlying interactions and, in particular, to explore the impact of this emerging IS concept (i.e., the quantified self). Second, because of its advantage in modeling a system’s behavior with incomplete and erroneous information, we employ QSIM to extend a robust and rigorous mathematical catastrophe model into a qualitative catastrophe model <sup>6</sup> in order to describe the mechanism of sudden change in individuals (Flay, 1978; Hu & Xia, 2015). In particular, QSIM drives the evolution of the empirical relations that then serve as constraints in QSIM to filter the successive states of the qualitative variables. QSIM extracts specific individual peculiarities and mechanisms as the microfoundation of ABM. Third, as a widely utilized group modeling method, we built an ABM model, grounded in the qualitative catastrophe (single-agent) model, in order to explore the grouplevel OIB emerging from individual interactions. QSIM was used to tease out the individual-level mechanisms as the microfoundation of the ABM model (Jiang et al., 2016). Simulation is a relatively understudied but useful research methodology, especially given the increasing complexity of IS phenomena (Dong, 2022). The combination of ABM and QSIM in a qualitative-quantitative mixed approach can provide unique opportunities to potentially yield significant insights into sudden group-level changes in OIB emerging from individual interactions.

The remainder of this paper is organized as follows. Section 2 is a literature review. Section 3 examines sudden changes in OIB from the perspective of catastrophe theory (CT) and presents a multimethod integrated simulation framework. Section 4 shows a multi-agent simulation model grounded in a survey study and a qualitative catastrophe model to study dynamic and group-level OIB behavior. We verify the validity of the model in Section 5 and perform experiments to simulate the process of OIB behavior in Section 6. The discussions, contributions, and conclusions are presented in Sections 7-9.

## 2 Theoretical Foundation

## 2.1 Online Impulsive Buying Behavior

Extensive research has probed the factors that influence impulsive buying behavior. Scholars have grouped these factors into three categories—external environmental cues/stimuli, consumer personality traits, and purchase situation factors—using numerous conceptual frameworks (Dholakia, 2000; Verplanken & Herabadi, 2001). In addition, given the rapid development of e-commerce, scholars have investigated the effect of website environment construction on OIB. Collectively, the literature indicates that website quality (Wells et al., 2011), atmospheric cues (Floh & Madlberger, 2013), and online product presentations (Vonkeman et al., 2017) have positive effects on OIB. Moreover, Chen et al. (2019) proposed that the urge to buy impulsively is determined by both individuals’ affective trust in the recommender and their affection toward the recommended product. However, studies have mainly used empirical methods to observe the factors that influence individual OIB behavior rather than exploring the mechanism of sudden changes in and evolution of OIB behavior at the group level. To fill these gaps in OIB research, this study introduces a multimethod combination paradigm to probe OIB behavior at the group level more robustly and extensively.

## 2.2 Factors Influencing OIB Behavior

## 2.2.1 Social Influence

In online social networks, social influence refers to the way that interacting with others affects an individual’s attitude or behavior (Amblee & Bui, 2011; Goetzke, 2008). The mechanism of social influence can be conceptually divided into two categories: informational social influence and normative social influence (Lord & Lee, 2001; Deutsch & Gerard, 1955). Informational social influence causes a consumer to accept information from others as a reference to understand reality—i.e., individuals obtain information via social impact (Jorczak, 2011). This process is also known as internalization, which occurs when an individual accepts social influence because the content of the induced behavior is intrinsically rewarding (Deutsch & Gerard, 1955). Individuals can gain certain knowledge or information by conversing with others or making inferences based on neighbors’ behaviors (such as buying behavior), which assists them in understanding their environment and solving certain problems. For example, consumers can easily obtain information regarding product quality or discount promotions by communicating with their neighbors (Mailath & Postlewaite, 2003; Fang & Hu, 2018).

Normative social influence, in contrast, causes individuals to conform to the positive expectations of others, including compliance and identification (Deutsch & Gerard, 1955). Specifically, compliance occurs when people allow themselves to be socially influenced to obtain a specific reward or recognition from another person or group. Identification occurs when an individual accepts influence to establish or maintain a satisfactory customary relationship with others. Thus, individuals may observe and understand the decisions of others in their social groups and hope to engage in similar behaviors (such as consumption, particularly impulsive buying) to gain rewards, obtain approval, and enhance their self-image (Bearden et al., 1989; Burnkrant & Cousineau, 1975).

In social groups, individuals change strategies based on replication, imitation, and learning through a variety of principles, such as imitation of the best, win-stay-loselearn, and tit-for-tat (Szabó & Fáth, 2007; Perc et al., 2017). The most prevalent strategy-updating rule is imitation, when an individual emulates his or her neighbor’s strategy after comparing their gains (Szabó & Fáth, 2007). Two widely used imitation rules are the logit rule and the best response rule (Amaral & Javarone, 2018). According to the logit rule, an individual changes their strategy on the basis of external factors and is likely to learn from the neighbor with the highest gain (a Fermi-Dirac distribution).

Preferential selection also affects the imitation process. Because of the differences in social influences among individuals, the selection of imitation objects is often based on preferences rather than executed randomly. Individuals with a high level of social influence, for example, are more likely to be imitated. The degree to which an individual is imitated is determined by their neighbors (Szabó & Fáth, 2007; Amaral & Javarone, 2018). In our study, we used the preferential selection and imitation rules described above to investigate the effect of social influence on group-level OIB.

## 2.2.2 IT-Enabled Quantified-Self Design

Information technology (IT) has developed rapidly because firms’ investment in IT is widely regarded as a key driver of innovation (Karhade & Dong, 2021; Dong et al., 2021). In addition, wearable technology is also becoming widely used. These factors have led to the concept of the “quantified self” (Hamari et al., 2018; Hassan et al., 2019). The quantified self refers to the process in which individuals use quantified tools (e.g., smartwatches, smartphones, and quantified applications) to monitor their bodies, states, and behaviors and obtain timely and accurate feedback and recommendations to improve their selfknowledge (Liu et al., 2021). For example, fitnesstracking apps such as WeChat Sports can track users’ physical activities, including their daily step counts (Tu et al., 2018).

The quantified self has an important impact on adoption behavior. First, nonadopters are more receptive to quantified-self design (e.g., data collection/upload, analysis, and visualization). Generally, quantified data helps consumers intuitively understand their self-status (Schroeder et al. 2007) and judge product effectiveness through quantitative data information to establish the association between product data indicators and consumers themselves. This advantage can effectively drive adoption behavior, that is, attract nonadopters to make purchases. Lei et al. (2021) found that the quantified self is helpful for promoting purchase intention and purchase scale. Typical examples include gamification design, which increases the community experience of the quantified self and thus promotes adoption behavior. Second, the quantified self can change users buying habits and brand preferences, eventually influencing the buying behavior of nonadopters indirectly through social influence (e.g., imitation behavior and the conformity effect). Specifically, the quantified self can arouse consumers’ quantified consumption intentions and reveal precise preferences, thus optimizing purchase decisions (e.g., purchase intentions and purchase scale) (Lei et al., 2021). For example, the use of health and fitness tools can change consumers’ lifestyles and thus their consumption preferences. Research has shown that one in four participating consumers has changed food brands as a result of using quantified-self tools, and nearly one in five has changed brands of personal-care products (Fuel, 2014). According to social influence theory, these changes at the user-group level can eventually influence the buying behavior of nonadopters through their interaction with users (Fang & Hu, 2018). Third, precision marketing based on quantified user data can also drive the buying behavior of nonadopters because the majority of users are comfortable sharing their data with producers and advertisers, which contributes to consumer segmentation, new product design and development, and custom AD design. Such precision marketing strategies can better meet nonadopters demand and benefit them indirectly, resulting in a much stronger likelihood of adoption behavior (Fuel, 2014). One example of how quantified-self data can benefit businesses can be seen in the insurance industry, where companies can use personal quantified data to tailor policies according to customers’ activities and lifestyle choices (Spiller et al., 2017).

Quantified-self platforms are often designed from a motivational revelation perspective. Some of the leading quantified-self platforms, such as the Fitbit Online Community (www.fitbit.com) and Strava (www.strava.com), offer a wealth of features to support these motivational revelations. These features mainly include social networking (Wannheden et al., 2021; Krasnova et al., 2015; Lin & Lu, 2011) and gamification designs (Deterding,

2015; Huotari & Hamari, 2017; Vesa et al., 2017; Wannheden et al., 2021). The literature has shown that designs that support social engagement and gamification can effectively facilitate long-term behavioral change (Schoech et al., 2013). Gamification features such as leaderboards turn sports into a social competition, while social interaction features, including “likes” and “teams,” provide avenues for users to interact with others.

Gamification refers to using game elements in nongame contexts to improve and sustain user engagement (McCallum, 2012). Typical examples of gamification elements are ranking systems and leaderboards that invoke a sense of competition among social members through levels and badges that motivate people to complete certain tasks (Xu et al., 2022). For example, the design of Nike+ incorporates milestone achievements and awards virtual badges to high-performing users (Charitsis et al., 2019). According to social comparison theory, people have a basic need to better understand and evaluate their own opinions and abilities by comparing them with others (Ho et al., 2016; Lee, 2014). Positive social comparison feedback from gamified experiences can enhance the perception of self-efficacy. Gamification design increases not only users’ motivation (e.g., learners’ motivation in educational settings) but also their interactions and the community experience of the quantified self (Schau et al., 2009; Buckley & Doyle, 2014; Van Roy & Zaman, 2017; Attig & Franke, 2018).

The social networking design of quantified-self platforms provides consumers with the opportunity to present themselves to others. Self-presentation theory holds that people need to properly present themselves to others according to their identity and good characteristics to thus feel supported, recognized, and understood (Lee & Borah, 2019; Grieve & Watkinson, 2016; Swann et al., 2000). Social engagement enables users to learn from similar individuals or role models in their community, and users tend to be interested in being role models and influencing others (Zhang, 2008). In addition, social engagement supports users in establishing friendships with other users and introducing close friends into quantified-self social networks. Communication among users and their friends greatly improves users’ selfefficacy (Anders, 2018; Ruggieri et al., 2021).

## 2.2.3 Individual Preferences

Preference reflects an individual’s liking for different products and services and implies that people make one choice among multiple options. Numerous studies in experimental economics have shown that human preferences are diverse and have long-term effects on people’s decisions and future choices (Meece et al., 2006; Osorio, 2017). Based on achievement goal theory, scholars have identified mastery, proving, and avoidance preferences. Individuals with a mastery preference focus on self-development and on the acquisition and development of skills (Mann et al., 2013; Zimmerman,

2013). For example, they may quantify their exercise data for the sake of personal development rather than showing off their health. Individuals with a proving preference use social comparison criteria to judge, showcase, and prove their competence and performance to others (Meece et al., 2006; Plante et al., 2013). For example, such individuals are prone to share their weight-loss success with others. Individuals with an avoidance preference tend to avoid failure and negative consequences; they suffer less from negative self-perception or from others’ low evaluation of them (Hackel et al., 2016; Roskes et al., 2014).

## 2.2.4 Product Information Features

There are many criteria for classifying product features, such as utilitarian products and hedonic products, lowinvolvement products, and high-involvement products. Nelson (1970) divides products into search products and experience products according to the classification of information characteristics. Search products refer to products whose key characteristics can be deciphered by a search prior to purchase and use, such as computers, mobile phones, and other electronic products. Experience products refer to products whose key characteristics can be determined only after consumers buy and use them, such as perfumes and clothes. Compared with other classification methods, the classification of search items and experience items focuses more on information pertaining to features. This classification method has been widely used in the field of online shopping and online word-of-mouth (Weathers et al., 2015; Benlian et al., 2012; Jiménez & Mendoza, 2013; Lu et al., 2021).

## 2.3 Catastrophe Theory

Catastrophe theory (CT) studies the phenomenon of sporadic change based on stability theory, singularity theory, and other mathematical theories. Its use is not limited to natural science disciplines such as mathematics, mechanics, and physics (Berlinski, 1978); rather, it has been widely employed in the social sciences to forecast stock market crashes (Barunik & Vosvrda, 2009; Tutek & Seven, 2013) and housing market crashes (Diks & Wang, 2016), to investigate human behavior (Guastello et al., 2013; Guastello et al., 2019), to predict workplace bullying (Escartin et al., 2013), and to analyze suicidal ideation (Bryan & Rudd, 2018).

The cusp catastrophe model has proven especially valuable for understanding a range of complex behavioral phenomena, particularly in the psychological and social arena (Grasman, 2010; Bryan et al., 2020; Butner et al., 2015). Its most significant strength is that it can accurately describe a person’s psychological and behavioral changing and jumping (Stewart & Peregoy, 1983), including nurses’ withdrawal behavior, nonsuicidal selfinjury, and alcohol use (Sheridan & Abelson, 1983; Sheridan, 1985; Butner et al., 2015). However, as a strict, rigorous, and static mathematical model, the cusp model shows the weakness of being unable to adapt to a vague, incomplete, and time-varying behavioral trajectory or mechanism. Hence, it needs to be combined with other methods (such as QSIM) to examine the dynamic sudden change mechanism in OIB.

As a sudden process, OIB behavior falls within the realm of psychology because it is steered by psychological activities that are suitable for being expressed by the cusp model. However, because individuals tend to make irrational decisions based on limited qualitative information, the mathematical cusp catastrophe model is considered too rigorous to be used in behavioral research. Consequently, Hu and Xia (2015) suggest a qualitative-quantitative hybrid catastrophe model integrating QSIM and fuzzy set theory to simulate a person’s sudden behavioral change. This integrated paradigm provides a novel method to investigate the sudden change process of OIB behavior.

## 2.4 Qualitative Simulation

QSIM, first proposed by Kuipers (1986), has become widely accepted as a viable technique to describe a physical system’s behavior with incomplete and spurious information. For example, Wang et al. (1996) used QSIM to carry out safety and operability assessments for processing plants. Cao et al. (2010) focused on the group safety behaviors and rules of miners and developed a qualitative model of miner groups’ safety behaviors to simulate these behaviors in different environments. Deng and Zhang (2013) introduced QSIM into the field of fault detection and diagnosis, and their detection and diagnosis study proved to be a useful and effective guide. Bellazzi et al. (2000) integrated the fuzzy system with the qualitative model to effectively establish a robust fuzzy neural model of the nonlinear system. Taken together, QSIM has been employed to infer all possible behaviors based on the available, if inadequate, a priori physical knowledge of the system, and this method has been effectively used as both a predictor and a simulator. Wei et al. (2013) leveraged QSIM in conjunction with empirical research to develop an optimization model of mobile banking adoption with incomplete information to minimize marketing costs while maximizing user-perceived utility.

Importantly, QSIM is capable of converting quantitative/mathematical catastrophe models into qualitative models (Hu & Xia, 2015). Although QSIM is relatively imprecise, we believe that a combination of QSIM and survey-based research can identify and describe the mechanism underlying sudden changes in OIB. In particular, we were able to examine the vague, incomplete, and time-varying individual behavioral trajectory or mechanism of OIB using QSIM because we were not constrained to a single time period (e.g., sudden change).

## 2.5 The Agent-Based Model

The agent-based model (ABM) technique is suitable for modeling complex systems and characterizing their dynamic evolution behavior (Jiang et al., 2016). As one of the most widely used simulation techniques by IS researchers to investigate a variety of topics, it can be used to discover the macro-evolution mechanism of the social economic system emerging from individual interactions as a bottom-up method based on interaction rules (Dong, 2022; Dong, 2019; Rahmandad & Sterman, 2008). ABM has advantages in researching complex IS phenomena (Benbya et al., 2020). In particular, it is a powerful approach to uncovering complex causal loops and capturing the massive interactions within and across different levels over time (Davis et al., 2007; Dong, 2022). Serrano and Iglesias (2016), for example, used multi-agent simulation to study viral marketing methods on Twitter. In the context of growing heterogeneous dispersed networks, Neville et al. (2015) described an agent-mediated electronic market for exploring social interaction. Regardless, the aforementioned ABM technique depicts that the decision-making process of consumers (such as online impulse purchases) is relatively simple, such that it cannot capture individual reasoning. In essence, group-level OIB behavior emerges from microlevel interactions among consumers. ABM is effective at simulating dynamic group behavior and can be used to model the group-level dynamics of OIB. To explore the evolution of OIB behavior at the group level, we considered the qualitative catastrophe model to be a decision-making agent and created agent interaction rules based on psychological theory.

## 3 A Conceptual Model for OIB

## 3.1 Cusp Catastrophe Model for OIB

The cusp catastrophe model can adapt to behavioral processes characterized by a sudden jump, bimodality, and hysteresis. OIB exhibits the peculiarities of sudden jumps (a sudden and immediate online purchase) (Rook & Fisher, 1995) and bimodality (a struggle between rational rejection and the momentary pleasure of OIB). Thus, the mathematical cusp catastrophe model with two control variables (quantified self and self-control) can be selected to analyze OIB as follows:

$$
V (f, u, v) = f ^ {4} + u f ^ {2} + v f\tag{1}
$$

where $f$ is individual OIB behavior, which has two stable states (purchase or refusal); ?? and ??, the normal control factor related to internal psychology and the splitting control factor related to the external environment, respectively, regulate the time and scale of this sudden change, respectively (Hu & Xia, 2015; Sheridan & Abelson, 1983; Sheridan, 1985). Thus, self-control directly controlled by psychological factors (such as self-evaluation) and a quantified self constructed through the use of external tools (such as a

Fitbit, Apple Watch, or mobile apps) can be defined as ?? and ?? , respectively. Lastly, $V ( f , u , v )$ is the potential function to measure the potential energy (state value) of the system formed by OIB behavior (??), internal psychology (??) and external environment (??) (Hu & $\mathrm { X i a , }$ 2015). Note that this mathematical cusp catastrophe model, which is merely the mathematical form of the cusp catastrophe model, will be transformed in Section 4 into a qualitative catastrophe model including qualitative variables, transition rules, and constraints.

The equilibrium surface ?? of individual OIB behavior is the critical point of the cusp potential function $V ( f , u , v )$ . The equilibrium state can be described by Equation (2) after taking a derivative of Equation (1):

$$
\frac {\partial V (f , u , v)}{\partial f} = 4 f ^ {3} + 2 u f + v = 0.\tag{2}
$$

The corresponding equilibrium surface ?? of consumer behavior (Figure 1) shows two stable regions, the upper-left area (surface of refusal) and the lower-right area (surface of purchase), with a sudden change between them. For example, $a ^ { \prime }$ indicates that both ?? and ?? are at a high level, and the corresponding $a _ { o }$ is on the surface of refusal. However, beyond these stable regions, ?? becomes sensitive to ?? and ??. For example, $c ^ { \prime }$ may correspond to two states $\left( \boldsymbol { c _ { o } } \right.$ and $c _ { 1 } )$ . In addition, the possible trajectories of the behavior change indicate the achievement or disruption of equilibrium over time. For instance, Lines C1 and C2 and Lines D1 and D2 represent sudden behavioral change from refusal to purchase or vice versa.

Equation (3) is the first derivative of Equation (2):

$$
1 2 f ^ {2} + 2 u = 0\tag{3}
$$

We obtain Equation (4) by substituting Equation (3) into Equation (2), which represents the singularity set of the behavior (??) on the control plane. Appendix A contains additional information.

$$
2 7 v ^ {2} + 8 u ^ {3} = 0\tag{4}
$$

The control plane below illustrates the changes in ?? and ?? , where the triangular region represents the singularity set. When ?? and ?? reach the singularity set, a sudden jump occurs.

However, OIB is essentially the result of interactions between consumers and empirical or qualitative information (Wei et al., 2013). The strict, rigorous, and static mathematical catastrophe model above cannot adapt to such a vague, incomplete, and time-varying behavioral trajectory or mechanism (i.e., a sudden change in OIB) (Hu & Xia, 2015), especially from a group-level perspective. Thus, an integrated paradigm is needed to address this problem (Davis et al., 1989; Davis, 1989). QSIM has been widely accepted to describe a physical system’s behavior with incomplete and spurious information (Bryan & Rudd, 2018; Forbus, 1984; Kuipers, 1993), whereas ABM can effectively model group behavior. Thus, we built a qualitative catastrophe simulation model grounded in a survey study to tease out the individual-level OIB mechanisms that would serve as the microfoundation of the ABM model.

![](/api/attachments/2DPA3VR6/fulltext/images/b7f0af0f72fd30e2f15d21673af3084878b8644e045244f0b748a18fa9903d3b.jpg)  
Figure 1. Catastrophe Model of the Sudden Change in Consumer Behavior

![](/api/attachments/2DPA3VR6/fulltext/images/9a72e0130c529fab5705739ab3501e468c10433cf13e8b7611c8531cced9e4ff.jpg)  
Figure 2. The Proposed Integrated Simulation Framework

## 3.2 The Proposed Integrated Simulation Framework

We propose an integrated framework to address the sudden change in OIB (Figure 2). Because a single method cannot capture a vague, incomplete, and timevarying psychological or behavioral trajectory or mechanism, we propose that the combination of a survey study, QSIM, and ABM can effectively identify and curb the sudden and dynamic group-level change in OIB. Our proposed sequential design incorporates three steps and leverages a variety of methodological approaches. First, a survey study was conducted to identify and determine the OIB factors and their interactions. Second, based on the empirical findings, a qualitative catastrophe model was developed to describe the specific mechanisms. In particular, QSIM drove the evolution of the empirical relations that then served as constraints in QSIM to filter the qualitative variables’ successive states. Third, based on the qualitative catastrophe (single-agent) model, an ABM model was built to explore the group-level dynamics of OIB, where QSIM was used to tease out the individual-level underlying mechanisms and serve as its microfoundation.

## 4 The Proposed Integrated Simulation Method

## 4.1 The Survey Study (to Extract Attributes)

To capture the sudden change in OIB, we conducted a survey study to identify the OIB factors and the correlations among them (see Appendix B for more details). Specifically, we used OIB as an example and used a questionnaire designed to obtain online data from consumers. These data were then statistically analyzed using SPSS to examine the interactions among OIB factors (see Figure 3). The findings indicated that (1) both the quantified self and self-control have a negative effect on OIB behavior $( c = - 0 . 3 2 0 , p < 0 . 0 1 ; b =$ −0.218 , ?? < 0.01 ); (2) the quantified self has a positive effect on self-control (?? = 0.350, ?? < 0.01); and (3) self-control acts as a mediator between the quantified self and OIB behavior (the indirect effect via self-control $c ^ { \prime } = - 0 . 1 2 0 , p < 0 . 0 1 )$ .

Traditional empirical approaches, however, are unable to accurately portray the dynamic nature of OIB behavior. Given its advantage in modeling a vague, incomplete, and time-varying psychological or behavioral trajectory or mechanism (Hu & Xia, 2015<sup>)</sup>, QSIM can be coupled with CT to quantitatively study the dynamics of OIB behavior (Thom, 1977). Based on the empirical findings, the combination can extend a robust and rigorous mathematical catastrophe model into a qualitative catastrophe model to describe the sudden change mechanism in OIB.

## 4.2 Qualitative Catastrophe Model (to Measure Behavior)

QSIM is designed to predict possible behaviors consistent with incomplete knowledge of a system (Kuipers, 1986). In this study, it was used to drive the evolution of consumers’ empirical relations. In essence, QSIM is a continuous inference process that deduces consumers’ subsequent state from their current qualitative state. It provides the mathematics that simulation relies on to develop computational models (Dong, 2022). The procedure and its linkage with other methods are illustrated in Figure 4, which includes qualitative descriptions, transition rules, and constraints.

![](/api/attachments/2DPA3VR6/fulltext/images/153ba235a3b263faf5486442793542bd6dbd8f8b2cfd4a8b255d0414231fbee8.jpg)  
Note. \*\*p < 0.01.

Figure 3. The Empirical Relation of OIB  
![](/api/attachments/2DPA3VR6/fulltext/images/fb3c845af7d83a6b441855270796729866727582dd66e921b944d86d7d1c1998.jpg)  
Figure 4. The Flowchart of the QSIM Algorithm.

## 4.2.1 Description of Qualitative Variables

According to the QSIM algorithm (Kuipers, 1986), a qualitative variable can be expressed in terms of two aspects—“level” and “change direction”—that indicate its magnitude and the change direction at the next step $t _ { n + 1 }$ , respectively. Thus, the qualitative value of ?? at time point $t _ { n }$ can be expressed as

$$
Q S (Z, t _ {n}) = <   q v a l, q d i r >
$$

More specifically, the levels of ?? and ?? and the corresponding meanings are elaborated as follows. For example, ?????????? = −2 indicates that the level of quantified self is very low at $t _ { n }$

$$
q v a l (u \text {or} v) = \left\{ \begin{array}{l l} - 2, & \text {Very low} \\ - 1, & \text {Low} \\ 0, & \text {Normal} \\ + 2, & \text {High} \\ + 2, & \text {Very high} \end{array} \right.
$$

Similarly, we define the level of the state variable ?? as

$$
q v a l (f) = \left\{ \begin{array}{l l} - 1, & R e f u s a l \\ + 1, & P u r c h a s e \end{array} \right.
$$

The change direction of the state variables ??, ??, and ?? at the next step $t _ { n + 1 }$ is expressed as follows. For example, $q d i r ( u ) = - 1$ indicates that the level of self-control will decrease at the next step, $t _ { n + 1 }$

$$
q d i r (u, v \text {or} f) = \left\{ \begin{array}{l l} - 1, & \text {Decrease} \\ 0, & \text {Standard} \\ + 1, & \text {Increase} \end{array} \right.
$$

## 4.2.2 Qualitative Catastrophe Model

With these qualitative variables, the model of Equation (2) can be transformed into a qualitative catastrophe model in Equation (5).

$$
\begin{array}{l} 4 Q S (f, t) ^ {3} + 2 Q S (u, t) \times Q S (f, t) + Q S (v, t) = \\ 0. \end{array}\tag{5}
$$

Divided by 4, the qualitative catastrophe simulation model above can be changed into

$$
\begin{array}{l} Q S (f, t) ^ {3} + \frac {1}{2} Q S (u, t) \times Q S (f, t) + \frac {1}{4} Q S (v, t) = \\ 0. \end{array}\tag{6}
$$

## 4.2.3 The Transition Rules

The I/P rules in the QSIM algorithm can be used to obtain the subsequent state of each variable (Hu & Xia, 2015). Specifically, the I-transition is the state transition from the time interval to the distinguished time point, while the P-transition is the state transition from the distinguished time point to the time interval. In this qualitative catastrophe model, the designed transition rules of variables $f ,$ ??, and ?? follow the I/P rules shown in Table 1, where $l _ { k + 1 }$ and $l _ { k - 1 }$ indicate that the variable moves to successive higher and lower levels, respectively. The system state can be obtained by combining the variable states at each time point. However, due to inadequate knowledge, each transition process may produce multiple subsequent states, some of which are impractical. Therefore, design constraints are needed to filter the results.

Table 1. I/P-Transition Rules.

<table><tr><td> $QS(f,t_n)$ </td><td> $QS(f,t_{n+1})$ </td></tr><tr><td rowspan="3"></td><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td rowspan="3"></td><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td rowspan="3"></td><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td rowspan="3"></td><td></td></tr><tr><td></td></tr><tr><td></td></tr></table>

Table 2. Qualitative State Constraints of QSIM Algorithm.

<table><tr><td>Type</td><td>Constraint meaning</td></tr><tr><td rowspan="4">Algebraic constraint</td><td> $ADD(f,g,h): (\forall t \in [a,b]) f(t) + g(t) = h(t)$ </td></tr><tr><td> $MULT(f,g,h): (\forall t \in [a,b]) f(t) \cdot g(t) = h(t)$ </td></tr><tr><td> $MINUS(f,g): (\forall t \in [a,b]) f(t) = -g(t)$ </td></tr><tr><td> $DERIV(f,g): (\forall t \in [a,b]) \frac{df(t)}{dt} = g(t)$ </td></tr><tr><td rowspan="2">Qualitative constraint</td><td> $M^{+}(f,g): (\exists H(u)) (\forall t \in [a,b]) (H'(g(t)) > 0 and f(t) = H(g(t)))$ </td></tr><tr><td> $M^{-}(f,g): (\exists H(u)) (\forall t \in [a,b]) (H'(g(t)) > 0 and f(t) = H(g(t)))$ </td></tr></table>

## 4.2.4 The Filtering Constraints

Constraints in QSIM always serve as a filter to prune any anomalies to avoid the explosion of all possible combinations of the qualitative variables’ subsequent behaviors. According to six constraints (see Table 2) in the QSIM algorithm (Hu & Xia, 2015; Kuipers, 1986), we transformed the qualitative catastrophe model (Equation 6) and empirical relations (Figure 3) into algebraic constraints and qualitative constraints, respectively:

1. Algebraic Constraints: Based on each part of the qualitative catastrophe model $\begin{array} { r l } { ( } & { { } Q S ( f , t ) ^ { 3 } } \end{array}$ + $\begin{array} { r } { \frac { 1 } { 2 } Q S ( u , t ) \times Q S ( f , t ) + \frac { 1 } { 4 } Q S ( v , t ) = 0 \ ) } \end{array}$ ), we assume the intermediate variables:

$$
x _ {1} = Q S (f, t) ^ {3}\tag{7}
$$

$$
x _ {2} = \frac {1}{2} Q S (u, t) \times Q S (f, t)\tag{8}
$$

$$
x _ {3} = - \frac {1}{4} Q S (v, t)\tag{9}
$$

To further describe Formula (7), we decompose it into

$$
x _ {4} = Q S (f, t) ^ {2}\tag{10}
$$

To further describe Formula (8), we decompose it into

$$
x _ {5} = Q S (u, t) \times Q S (f, t)\tag{11}
$$

Then, the empirical relationship between drivers (see Figure 3) and the mathematical relationship between variables in the cusp catastrophe model can be described as the following constraints:

The empirical results show a sudden change in OIB, consumers’ OIB intention, consumers’ quantified self, and the interaction effect of self-control and consumers’ OIB intention. We substitute Formulas (7)-(9) into $\begin{array} { r } { Q S ( f , t ) ^ { 3 } + \frac { 1 } { 2 } Q S ( u , t ) \times Q S ( f , t ) + } \end{array}$ $\begin{array} { r } { { \frac { 1 } { 4 } } Q S ( v , t ) = 0 } \end{array}$ to obtain the following constraint, indicating $x _ { 1 } + x _ { 2 } = x _ { 3 }$ . Thus, we propose the following constraint:

$$
A D D (x _ {1}, x _ {2}, x _ {3})\tag{12}
$$

Specifically, the cusp catastrophe model indicates a nonlinear relationship between consumers’ OIB intention and the sudden change in OIB. Therefore, according to Formula (10), we propose the following two constraints:

$$
M U L T (Q S (f, t), Q S (f, t), x _ {4})\tag{13}
$$

We substitute Formula (10) into Formula (7) to obtain $x _ { 1 } = Q S ( f , t ) \times x _ { 4 }$ as the constraint:

$$
M U L T (Q S (f, t), x _ {4}, x _ {1})\tag{14}
$$

The interaction effect of self-control and consumers OIB intention also plays a key role in the sudden change in OIB. According to Formula (11), the corresponding two constraints can be described as follows:

$$
M U L T (Q S (u, t), Q S (f, t), x _ {5})\tag{15}
$$

We substitute Formula (11) into Formula (8) to obtain the constraint, meaning that $\begin{array} { r } { x _ { 2 } = \frac 1 2 x _ { 5 } . } \end{array}$

$$
M U L T (\frac {1}{2}, x _ {5}, x _ {2})\tag{16}
$$

The quantified self has a negative linear effect on the sudden change in OIB. According to Formula (9), it is described as follows:

$$
M U L T (- \frac {1}{4}, Q S (v, t), x _ {3})\tag{17}
$$

2. Qualitative Constraints: The empirical relationships in Figure 3 can be transformed into qualitative constraints (Equations 18-20), indicating an identical change in direction between ?? and ?? (i.e., the moderating effect of self-control on quantified self in Figure 3) and an opposite change in direction between ?? and ?? and between ?? and ??.

$$
M + (Q S (u, t), Q S (v, t))
$$

$$
M - (Q S (u, t), Q S (f, t))\tag{18}
$$

(19)

$$
M - (Q S (v, t), Q S (f, t))\tag{19}
$$

## 4.2.5 Simulation Steps

Substep 1: Initialize the model and put the initial state into the active state table. Set the simulation depth to ??.

Substep 2: If the active state table is empty or the simulation depth has been reached, output the result $Q S ( f , t + 1 ) , Q S ( u , t + 1 ) , Q S ( v , t + 1 )$ and end; otherwise, go to the next step.

Substep 3: Take the top stake of the active state table as the current state $Q S ( f , t _ { n } ) , Q S ( u , t _ { n } ) , Q S ( v , t _ { n } )$ . Yield all possible $Q S ( f , t _ { n + 1 } ) , Q S ( u , t _ { n + 1 } ) , Q S ( v , t _ { n + 1 } )$ according to I/P-transition rules.

Substep 4: Filter out the illogical and irrational states according to the filtering constraints and add the remaining states into the activity state table.

Substep 5: Set $n = n + 1$ . Go to substep 2.

## 4.2.6 Sudden Change Rule

Based on the definitions of the qualitative variables, the condition for catastrophe is derived from Equation (4). This means that if ?? and ?? reach the singularity set, a sudden jump in behavior $( f )$ will occur, and the subsequent behavior of ?? reasoned by the QSIM model should be the opposite value of the former behavior (either from -1 to 1 or from 1 to -1).

$$
\begin{array}{l} P _ {s u d d e n c h a n g e} \\ = \left\{ \begin{array}{l l} 1 & i f 2 7 Q S (v, t) ^ {2} + 8 Q S (u, t) ^ {3} \leq 0 \\ 0 & i f 2 7 Q S (v, t) ^ {2} + 8 Q S (u, t) ^ {3} > 0 \end{array} \right. \end{array}\tag{21}
$$

where $P _ { s u d d e n c h a n g e }$ is the probability of sudden change in OIB and $2 7 Q S ( v , t ) ^ { 2 } + 8 Q S ( u , t ) ^ { 3 }$ is the condition for catastrophe.

## 4.3 ABM Model (to examine social influence)

QSIM can accurately describe a vague, incomplete, and time-varying individual psychological or behavioral trajectory. However, it is unable to describe group behavior over time that ABM can thoroughly investigate because it is powerful for uncovering complex causal loops (Jiang et al., 2016; Davis et al., 2007; Dong, 2022). Accordingly, based on the literature review, the empirical findings, and the catastrophe simulation findings, we built an ABM model to explain the group-level dynamics of OIB (see Figure 5). It can leverage strengths from analytical and empirical methodologies (Dong, 2022). Specifically, each customer is treated as an agent, with the OIB factors from the survey study serving as the agent’s attributes.

## 4.3.1 Individual Preference

According to the literature review in Section 2.2.3, consumers’ preferences can be divided into three categories – mastery, proving, and avoidance preferences – that have different implications for consumers’ willingness to use quantified-self tools. Specifically, mastery-preference consumers use tools for learning a skill rather than for showing off; thus, their willingness to use quantified-self tools is the strongest. Hackel et al. (2016) also found that the confirmatory factor between mastery and performance is $0 . 8 3 \ : \ : \mathrm { ~ ( ~ } p \ : < \ : 0 . 0 0 1 \ : \ : )$ ). In contrast, avoidancepreference consumers tend to avoid negative quantified-self results; thus, their willingness to use quantified-self tools is the lowest. The willingness of proving-preference consumers is between the two because they aim to prove their superiority over others and may give up if their quantified results fall short of their expectations. Hamari et al. (2018) found a positive relationship between proving preference and the IT-enabled quantified self (such as social networking) $( \beta ~ = ~ 0 . 2 8 3 , p ~ < ~ 0 . 0 0 0 )$ ) and a negative relationship between avoidance preference and quantified self $( \beta = - 0 . 3 2 1 , p < 0 . 0 0 0 )$ ).

According to these empirical findings, the probability of each type of consumer using quantified-self tools obeys a uniform distribution, i.e., $W _ { 1 } { \sim } U ( 0 . 8 , 1 ) , W _ { 2 } { \sim } U ( 0 . 8 , 0 . 3 ) , W _ { 3 } { \sim } U ( 0 . 3 , 1 )$

## 4.3.2 Online Interaction Evolution Rules

With incomplete information, individuals adjust their strategy according to their expected revenue (Simon, 1991). Homoplastically, in online social networks, the urge to buy impulsively is also affected by the decision-making of neighbors, such as affective trust in the recommender (Chen et al., 2019), the perception of the opinion leadership, and the volume of product usage (Iyengar et al., 2011). Therefore, we constructed a dynamic interaction rule including the preferential selection rule and the imitation rule.

![](/api/attachments/2DPA3VR6/fulltext/images/b6def6f8ea7f44aed3b67e4ca9d93e83deb7f496096c49653d998a584a1505a9.jpg)  
Figure 5. The Structure of the ABM Model.

1. The Preferential Selection Rule: According to the literature review on social influence, individuals select a neighbor to imitate when updating their strategies. The literature assumes that imitation behavior in the evolutionary process depends on social influence. However, the preferential selection between individuals is also affected by product features and consumer preferences. Accordingly, considering these effects comprehensively, we extended the traditional preferential selection rule as a function of product features, social influence, and consumer preferences. That is, the probability $P _ { s e l e c t i o n }$ that consumer ?? will choose a neighbor ?? to imitate is

$$
P _ {s e l e c t i o n} = \theta * \frac {k _ {i}}{\sum_ {j} k _ {j}} * \frac {m i n (W _ {i} , W _ {j})}{m a x (W _ {i} , W _ {j})},\tag{22}
$$

where the three expressions $( { \mathrm { i . e . , } } \theta , { \frac { k _ { i } } { \sum _ { j } k _ { j } } } , { \mathrm { a n d } } { \frac { m i n ( W _ { i } , W _ { j } ) } { m a x ( W _ { i } , W _ { j } ) } } )$ in the equation refer to the effect of product features, social influence, and consumer preferences, respectively. Specifically, ?? refers to the product information feature and $\theta \in [ 0 , 1 ]$ . The probability of imitation among consumers increases with the increase in the product information feature— $\mathbf { \nabla } \cdot k _ { i }$ is the connectivity degree of consumer ??. The influence of neighbors is a nonlinear function of their degrees; for instance, consumers with more interactions will attract more attention in the market. $W _ { i }$ and $W _ { j }$ refer to the willingness of consumers ?? and ?? to use quantified-self tools based on consumer preferences. The closer $W _ { i }$ and $W _ { j }$ are, the greater the possibility of mutual imitation in decision-making, according to interpersonal relationship theory (Roche et al., 2013).

2. The Imitation Rule: From the findings of the catastrophe simulation, we designed an imitation rule as a function of the OIB intention obtained in catastrophe simulation. The imitation rule, which is mathematically equivalent to the statistics on the dynamics of spins in a Fermi-Dirac distribution, has been widely used in evolutionary dynamics, that is, in human interactions (Amaral & Javarone, 2018; Amaral et al., 2017). It proposes the fittest strategy of reproducing to neighbors, indicating that changes in consumer behavior are also influenced by other external factors (Ye & Fan, 2017; Szabó et al., 2005; Yang & Tian, 2017). According to traditional imitation rules, we assume that individuals learn from their neighbors with the highest individual

OIB intention. The imitation rule can be denoted by the stochastic process as:

$$
P _ {i m i t a t i o n} = \frac {1}{1 + e ^ {- (f _ {j} - (1 + p (g)) f _ {i}) / z}},\tag{23}
$$

where $f _ { i }$ is the OIB intention of consumer $i , f _ { j }$ is the maximum OIB intention (consumer $j ~ )$ among neighborhood consumers, $p ( g )$ is gamification, $_ g$ is the degree of the quantified self-relevant product gamification design, and ?? is information noise due to social networking. According to the law of diminishing marginal utility, $p ( g )$ is designed as an increasing function of $_ { g \colon }$ $p ( g ) = ( 2 - g ^ { - 1 / 2 } )$ . As ?? gets larger, $p ( g )$ gets infinitely close to 2. When $( 1 + p ( g ) ) f _ { i }$ approaches $f _ { j } .$ ?? will approximate ${ } ^ { 1 / 2 , }$ equivalent to the result of a coin toss. In contrast, the greater the difference between (1 + $p ( g ) ) f _ { i }$ and $f _ { j }$ , the larger the imitation probability.

## 4.3.3 Strategy Change Rule

In group settings, sudden changes in OIB depend not only on the evolution of individual interior factors but also on social influence $( \mathrm { i . e . } ,$ , preferential selection and imitation). Thus, considering the probability of preferential selection (Equation 22) and imitation (Equation 23), we extend the individual-level condition (Equation 21) for sudden change into the group level as:

$$
P _ {c h a n g e} = \left\{ \begin{array}{l} P _ {s e l e c t i o n} * P _ {i m i t a t i o n} \\ i f S t r a t e g y _ {i} \neq S t r a t e g y _ {j} \\ \text {and} P _ {s u d d e n c h a n g e} = 1 \\ 1 - P _ {s e l e c t i o n} * P _ {i m i t a t i o n} \\ i f S t r a t e g y _ {i} = S t r a t e g y _ {j} \\ \text {and} P _ {s u d d e n c h a n g e} = 1 \end{array} \right.\tag{24}
$$

## 4.3.4 Simulation Flow

The simulation flow diagram of our ABM model is illustrated in Figure 6. In each time unit, consumers first calculate the probability of sudden change $( \ P _ { s u d d e n c h a n g e } )$ in their purchase decision by the qualitative catastrophe model according to their initial conditions. Then, with the function of social influence, they consider their neighbors’ decisions and finally make decisions. Over time, the group-level dynamics of OIB can eventually be determined. The simulation model was developed on the Anylogic 6.5.0 environment with the Microsoft Windows 8 operating system. All calculation experiments were conducted in the same environment.

![](/api/attachments/2DPA3VR6/fulltext/images/c86fd3c77164d8aed6739d1398156c808d0ecc2df4bed4aca46d8f2f9b2b6d6b.jpg)  
Figure 6. Simulation Flow

![](/api/attachments/2DPA3VR6/fulltext/images/510b6490bcc20348a93c934932745b72bbfb674c4812885e14e49556be157552.jpg)  
Figure 7. The Simulation Results of the Qualitative Catastrophe Simulation Model Fit Well with the Cusp Equilibrium Surface and Have Obvious Catastrophe Characteristics.

## 5 Validation of the Proposed Method

We applied qualitative verification to the qualitative catastrophe simulation model by comparing the simulation results with classical cusp CT. The ABM model was tested using conceptual model validation, data validity or empirical input validity, and operational validity or empirical output validity.

## 5.1 Validation of the Qualitative Catastrophe Simulation Model

The representative simulation results of the qualitative catastrophe simulation model are shown in Figure 7. Blue surfaces, white points, and black lines represent the classical cusp CT model, the possible decisions of consumers, and the decision path change, respectively. Figures 7a and 7b depict OIB behavior, while Figure 7c shows the process from the lower leaf to the upper leaf.

In Figure 7, all points fit well with the equilibrium surface, and the paths adequately reflect catastrophe characteristics such as divergence and hysteresis. Specifically, when comparing Figures 7a and 7b, the two paths have the same starting point but different outcomes. This reflects divergence, which means that minor changes in the control variables near the bias point will lead to significant differences in the ultimate state. A comparison of Figures 7a and 7c illustrates that the catastrophe path and the retrorse catastrophe path are not reciprocal, and the cusp points $( A _ { 3 }$ and $C _ { 4 } )$ are not the same. This situation reflects hysteresis, which means that the change in an outcome from one surface to the other cannot be determined by control variables of the same value.

The simulation results fit well with the cusp equilibrium surface and exhibit clear catastrophe characteristics. Therefore, the validity of the qualitative catastrophe simulation model can be verified so that the ABM model can also be further verified.

## 5.2 Validation of the ABM Model Using Real Case Data

The ABM model is difficult to validate because it subsumes many parameters and assumptions (Knoeri et al., 2011). Dong (2019) notes that validations by replicating prior results and/or comparing them with empirical findings can be used if the novelty of modeling is high. Thus, we performed a series of validations, including conceptual model validation, data validity or empirical input validity, and operational validity or empirical output validity (Sargent, 2013; Rand & Rust, 2011). First, based on CT, QSIM, ABM, OIB, and complex network theory, the conceptual model validation of our model was achieved to confirm the behavior of agents, and the system was reasonable.

Second, in terms of data validity or empirical input validity, we conducted extreme value tests and robustness checks, respectively. During testing and debugging, the values of input variables and parameters are changed to extreme levels to test whether the model works as expected. For example, in Figure 8, when the information noise is very large $\left( \ z = 1 0 0 0 \ \right)$ , the incidence of group-level OIB fluctuates greatly over time, while when ?? is very small $( z = 0 . 0 0 1 )$ ), the curve is relatively stable. This corresponds to the existing study: the greater noise the network information has, the less stable users’ behavior will be (Jiang et al., 2014). Then, robustness checks were used on the exponents of the cusp catastrophe model (Equation 1) and the empirical parameters $( a = 0 . 3 5 0$ $b = - 0 . 2 1 8$ $c =$ −0.320 , $c ^ { \prime } = - 0 . 1 2 0 \rangle$ ) to confirm that the results changed as expected. Figure 9 shows that a small change in the exponents of the cusp catastrophe model has a weak effect on the results. We compared the simulation outputs using the empirical parameters governed by two uniform distributions and two triangular distributions. The results were robust across distributions, providing further evidence of operational or empirical output validity (see Figure 10).

Third, in terms of operational validity or empirical output validity, we used real market data from China to test whether the output of the model conforms to the real world. The transaction volume on Singles’ Day, China’s largest shopping festival, constitutes highly representative sample data of OIB. We collected public sales data on the Tmall platform (www.tmall.com) during Singles’ Day from 2009 to 2020. Then, we adjusted the parameters according to the real situation (for example, consumers’ quantified self-level was very low and their self-control level was very high in 2009), set the time step to 12, and reran our simulation model 1000 times to obtain the average simulation results. By comparing the normalized actual data with the simulation data (Figure 11), it can be seen that the trends of the two lines are roughly the same ( ?? = 0.995 ). This is consistent with Rand and Rust’s guidelines for rigor in ABM; that is, real-world data validation involves showing that the average model results correlate with the real-world results (Rand & Rust, 2011). The validation results indicate that to some extent, our model accurately captures real-world behavior.

![](/api/attachments/2DPA3VR6/fulltext/images/fba540e23a5aee0d2ce6eefda02593870c86638681e38b64e0a24aa521605bca.jpg)  
Figure 8. Results of the Extreme Value Tests on Information Noise

![](/api/attachments/2DPA3VR6/fulltext/images/9b653fe163aced4fb59971ba7dde83be2ed52b977fefebb84fe0120897e0bffd.jpg)  
Figure 9. Results of the Robustness Checks on the Exponents of the Cusp Catastrophe Model

![](/api/attachments/2DPA3VR6/fulltext/images/2819dc9458d330fb1a402336721eab0a940a4e5c9a5fd449ae4483cd9e54a7ef.jpg)

![](/api/attachments/2DPA3VR6/fulltext/images/8da624a5e4bb3c3b43be05949cdb3a59404f4116cde59f6dc975f9850673970f.jpg)

![](/api/attachments/2DPA3VR6/fulltext/images/732773c42a3337632332b4f97ee1aecae714685e4450ecbc17d6a663fbd23597.jpg)

![](/api/attachments/2DPA3VR6/fulltext/images/d36f46bf2046aeae9a73674a9734611e2757bda99655d52eaac355cce665599e.jpg)  
Figure 10. Results of the Robustness Checks on the Distribution of the Empirical Parameters

![](/api/attachments/2DPA3VR6/fulltext/images/83b204880bfdb15385ed33e8c98e6c0f5b478e1b6a7dc15ee26c5e23252a29af.jpg)  
Figure 11. Comparison of Simulation Outcomes with Real-World Data

## 6 Simulation Analysis

We adjusted the values of the parameters in the experiments to conduct sensitivity analysis in order to explore the impact of each parameter on the sudden change in group-level OIB. To ensure the validity and robustness of the simulation outcomes, we implemented 1000 replications for each scenario in line with prior studies $( \mathrm { e . g . }$ , Hu et al., 2011; Dong, 2021). Then, we used a meaningful way to interpret the simulation results and derive deep theoretical insights from the findings (Dong, 2022). That is, we used the simulation outcomes to fit parameters ?? and $\beta$ in the cusp catastrophe model $( \mathrm { ~ \ } 4 f ^ { 3 } + 2 \alpha u f + \beta v = 0 )$ and qualitatively and quantitatively analyzed group-level catastrophe.

## 6.1 Parameters Related to the Quantified Self and Self-Control

To explore the effect of the quantified self on grouplevel OIB, we performed our experiments by varying the combinations of $\{ Q S ( v , t ) , Q S ( u , t ) \}$ (i.e., quantified self and self-control) from {−2, −2} to {+2, +2} with increments of 1. The mean and 95% CI of the fitted parameters ?? and $\beta$ are listed in Table 3. From the fit results, the corresponding catastrophe model can be constructed (as seen in Figure 12, where R means the ratio of impulse purchases by the consumer group, same as below). The singularity set on the control plane can be obtained by switching to the top view (Figure 13), and the effect of the quantified self is displayed in the side view (Figure 14).

Table 3. The Parameter Fitting Results of ?? and $\beta .$

<table><tr><td>Parameter</td><td>Mean</td><td>SE</td><td>95% CI</td></tr><tr><td>α</td><td>0.47</td><td>0.069</td><td>0.42, 0.52</td></tr><tr><td>β</td><td>0.92</td><td>0.072</td><td>0.89,0.94</td></tr></table>

![](/api/attachments/2DPA3VR6/fulltext/images/593ef3bcdf4dbf9748572c0fffa0263c4f51647dfa60c42a459f45f5908980d2.jpg)  
Figure 12. The Catastrophe Model of Group-Level OIB.

![](/api/attachments/2DPA3VR6/fulltext/images/f08192fc8730cfb800cf6727cd1fb4353e7516f34240889292e2cced05adf93b.jpg)  
Figure 13. The Singularity Set on a Control Plane.

![](/api/attachments/2DPA3VR6/fulltext/images/e4eb3b18927cec821dd9bfdfa088caf2374ae6ab716ef54f44c0fbf3fc9ca900.jpg)  
Figure 14. The Side View of Figure 12.

The results indicate that a sudden change in grouplevel OIB occurs as the quantified self $( Q S ( v , t ) )$ 0 increases when self-control is low. Specifically, when self-control is low (-2\~A) and the parameter combination reaches the singularity set, the grouplevel OIB changes abruptly (as seen in Figure 13). For example, a sudden change occurs when the quantified self approaches point B on the lower surface (see Figure 14). The key rationale is that consumer groups share more quantitative data about their behavior when they have low levels of self-control and high levels of quantified self. This can increase the community experience of the quantified self, thus attracting nonadopters to buy. Accordingly, businesses could leverage the quantified selves of consumers to boost their OIB to a high level through quantified-self online tools but they should be aware that this may involve business ethics issues, such as data breaches.

## 6.2 Parameters Related to Individual Preferences and Product Information Features

We further tested whether individual preference distribution had significant effects on group-level OIB. Figure 15 shows its effects on group-level OIB, with (mastery preference: proving preference: avoidance preference) = (7:1:2), (1:2:7), and (2:7:1), respectively. The mean and 95% CI of the fitted parameters ?? and $\beta$ are listed in Table 4.

Group-level OIB presents different folding features under different preference distributions (Figure 15). The simulation results reveal that the consumer group with a higher proving preference (Figure 15c) had a more explicit folding feature, thus indicating a higher possibility of catastrophe. The reason may be that proving-preference consumers are willing to compare themselves with others and are more inclined to learn from their neighbors. For instance, conspicuous consumption is a frequent and widespread type of consumer behavior in which people aim to visibly demonstrate their buying power rather than meet their demands. Therefore, e-shopping platforms can adopt effective measures to attract more consumers by proving preferences by making target customers think these products are worth their self-promotion.

Similarly, to observe the effect of product features on group-level OIB, we varied the product information feature ?? from 0.1 to 0.9 at increments of 0.4. Then, the corresponding catastrophe models with different product information features were constructed (as seen in Table 5 and Figure 16). The results (Figure 16) revealed that the scale of sudden change $( \mathrm { i } . \mathrm { e } . , S _ { 1 } , S _ { 2 } ,$ and $S _ { 3 } )$ increased significantly with enhanced product information features. This indicates that enhanced product information features ?? can elevate group-level OIB. For example, the “live-streaming economy,” which can conveniently display products to enhance their information features, has become a current ecommerce trend in China. This suggests that eshopping platforms are incentivized to offer more incentives to encourage sellers to enhance the information features of their products.

## 6.3 Parameters Related to IT-Enabled Quantified-Self Design

To explore the influence of gamification, an ITenabled quantified-self design, on group-level OIB, multiple experiments were conducted. We varied the initial value of gamification $( p ( g ) )$ from -2 to 2 at increments of 0.5 in the mastery-preference, avoidance-preference, and proving-preference groups: the fit results were $( \alpha , \beta ) = ( 0 . 3 2 , 0 . 4 4 )$ , (0.48,0.55), and (0.77,0.98), respectively. A sectional view of the corresponding catastrophe models with $u = - 2$ is shown in Figure 17.

Table 4. Parameter Fitting Results of ?? and $\beta .$

<table><tr><td>Parameter</td><td>Mean</td><td>SE</td><td>95% CI</td></tr><tr><td> $\alpha_a$ </td><td>0.24</td><td>0.086</td><td>0.20,0.28</td></tr><tr><td> $\beta_a$ </td><td>0.86</td><td>0.065</td><td>0.82,0.90</td></tr><tr><td> $\alpha_b$ </td><td>0.37</td><td>0.084</td><td>0.36,0.38</td></tr><tr><td> $\beta_b$ </td><td>0.94</td><td>0.057</td><td>0.92,0.96</td></tr><tr><td> $\alpha_c$ </td><td>0.58</td><td>0.060</td><td>0.55,0.61</td></tr><tr><td> $\beta_c$ </td><td>0.55</td><td>0.083</td><td>0.52,0.58</td></tr></table>

![](/api/attachments/2DPA3VR6/fulltext/images/173bc5c0303b81622009b1e8e1797cb1b630f8357d66d3c3123a5cf2dfd7d8b9.jpg)  
(a) (7: 1: 2)

![](/api/attachments/2DPA3VR6/fulltext/images/3a7d1161a9c99ef7e696dd74b65e802613a5946714c1fe9a0d84864e12bcb4dc.jpg)  
(b) (1: 2: 7)

![](/api/attachments/2DPA3VR6/fulltext/images/f619c74135969fce672971aa73208597274e2d88ba3ec656da94ef7b428e3fec.jpg)  
(c) (2: 7: 1)  
Figure 15. The Influence of Preference Distribution on Group-Level OIB.

Table 5. Parameter Fitting Results of ?? and $\beta .$

<table><tr><td>Parameter</td><td>Mean</td><td>SE</td><td>95% CI</td></tr><tr><td> $\alpha_{\theta=0.1}$ </td><td>0.02</td><td>0.076</td><td>0.01, 0.03</td></tr><tr><td> $\beta_{\theta=0.1}$ </td><td>0.04</td><td>0.071</td><td>0.02, 0.06</td></tr><tr><td> $\alpha_{\theta=0.5}$ </td><td>0.32</td><td>0.081</td><td>0.28, 0.36</td></tr><tr><td> $\beta_{\theta=0.5}$ </td><td>0.46</td><td>0.068</td><td>0.43, 0.49</td></tr><tr><td> $\alpha_{\theta=0.9}$ </td><td>0.47</td><td>0.050</td><td>0.45, 0.49</td></tr><tr><td> $\beta_{\theta=0.9}$ </td><td>0.83</td><td>0.082</td><td>0.80, 0.86</td></tr></table>

![](/api/attachments/2DPA3VR6/fulltext/images/70fc0708fea0426802d5fae77ee3a4575a11c7e91ea500ddd0c2c9220cbaf7ac.jpg)  
(a) ?? = 0.1

![](/api/attachments/2DPA3VR6/fulltext/images/e2e99673f055aca0b294882dfbbfbb9da520f2913e4ac24747cb4d52fee38d80.jpg)  
(b) ?? = 0.5

![](/api/attachments/2DPA3VR6/fulltext/images/a7dbba1c02f7e88f84f836a96841d3ac3baa67dc39641ea8b52d4b2ddb3ff058.jpg)  
(c) $\theta = 0 . 9$  
Figure 16. The Influence of Product Features on Group-Level OIB.

![](/api/attachments/2DPA3VR6/fulltext/images/b1692f757c44a8ebd13643398901c17b614a199b00047583d4da1fbf9bd24279.jpg)  
Figure 17. The Influence of Gamification on Group-Level OIB.

The results (Figure 17) indicate that gamification has a positive nonlinear effect on group-level OIB, and the optimal gamification (such as $g _ { 1 } , g _ { 2 } ,$ and $g _ { 3 } )$ for a sudden increase in group-level OIB can be identified. For example, the sudden increase in the proving-preference group (i.e., point $f _ { 3 } )$ occurred when $p ( g ) = g _ { 3 }$ . The gamification level can be divided into suboptimal gamification, optimal gamification, and overgamification. The level that falls between complete nongamification, and optimal gamification is called suboptimal gamification. At this stage, gradually increasing the level of gamification increases group-level OIB. This finding is consistent with the real-world case. For example, Nike+, a self-tracking system for runners, incorporates a gamification design that includes milestone achievements and cool virtual badges awarded to high-performing users, which increase user engagement. However, overgamification occurs when gamification levels exceed optimal levels, resulting in negative emotions among them. For example, an overgamified course obscures its main function of delivering learning by excessively providing gameful experiences (Yohannis et al., 2014; Heričko et al., 2021). Therefore, businesses could use optimal gamification designs in their quantified self-functions to promote sudden increases in group-level OIB.

With the development of IT, quantified self-platforms increasingly pay attention to social networking design. To test whether social networking ?? affected grouplevel OIB, we varied ?? from 1 to 100; ?? and ?? were obtained from the simulation results when $z = 1 , 1 0 _ { \scriptscriptstyle \mathrm { i } }$ and $1 0 0 ~ : ~ ( \alpha , \beta ) _ { z = 1 } ~ = ~ ( 0 . 2 5 , 0 . 5 6 ) , ~ ( \alpha , \beta ) _ { z = 1 0 } ~ =$ $( 0 . 5 5 , 0 . 9 0 )$ and $\begin{array} { r l r } { ( \alpha , \beta ) _ { z = 1 0 0 } } & { { } = } & { ( 1 . 0 8 , 1 . 5 2 ) } \end{array}$ respectively. Figure 18 displays three singularity sets $( O A _ { 1 } B _ { 1 } , O A _ { 2 } B _ { 2 }$ , and $O A _ { 3 } B _ { 3 } )$ when $z = 1 { , } 1 0$ , and 100 on one control plane.

Figure 18 illustrates the effect of social networking on group-level OIB. It reveals that the larger ?? is, the wider the singularity set will be, indicating a higher possibility of catastrophe. For example, when $u = - 1$ the catastrophe threshold increases $( H _ { 1 } ^ { } - H _ { 2 } ^ { } - H _ { 3 } ^ { } )$ with ?? increasing (?? = 1, 10, and 100). This result is also true in the context of the design of fitness apps. WeChat Sports, with social networking designs (such as ranking consumers’ and their friends’ step counts on a leaderboard and allowing consumers to add friends as teammates), can more effectively promote consumers participation in physical activity than fitness apps with simple gamification designs, such as Walkup. Therefore, businesses could also add the function of social networking when conducting gamificationbased IT-enabled quantified-self design.

![](/api/attachments/2DPA3VR6/fulltext/images/398d16d82a3a6a9b62ef10dcaa7952d5f2530856f3a2df5c44308e8d3576b8f6.jpg)  
Figure 18. The Influence of Social Networking on Group-Level OIB.

## 7 Discussion and Conclusion

## 7.1 Discussion

Empirical studies on OIB are generally confined to a single time period, which is inadequate to capture and investigate the dynamic behavioral trajectory of OIB. Furthermore, instead of examining the dynamic rapid shift in OIB at the group level, extant studies have focused on identifying OIB factors and their underlying interactions. Essentially, our comprehensive literature review revealed that a single methodological approach cannot be effectively applied to a dynamic and group-level analysis of abrupt changes in OIB. These theoretical and methodological issues thus necessitated the development of an integrated simulation paradigm to curb the ambiguous, incomplete, and time-varying psychological or behavioral trajectory or mechanism of OIB.

In this study, to answer the recent call for further research on OIB and to robustly and rigorously discover and analyze sudden changes in OIB, we proposed a sequential simulation approach subsuming a survey method, the QSIM technique, and the ABM model. We believe that this novel multimethod approach will shed new light on the emerging OIB literature and further advance this line of research. Importantly, we first employed an empirical method to identify the interior drivers of OIB and the relations among them. Second, according to the empirical results, a qualitative catastrophe model was built to describe the individual mechanism, with the empirical relations serving as constraints in QSIM to filter the successive states of the factors. Third, grounded in the qualitative catastrophe (single-agent) model, an ABM model was built to explore the group-level dynamics of OIB, where QSIM was used to tease out the underlying individual-level mechanisms and served as the microfoundation of the ABM model. The validation results indicate that this multimethod approach can serve as a plausible solution to the phenomenon of group-level OIB. It also provides an effective tool for managers to make decisions regarding product promotion and market stability.

In essence, the proposed simulation results reveal that (1) sudden changes in group-level OIB occurred as consumers’ sense of quantified self increased when self-control was low; (2) the greater the number of consumers with a proving preference in the group, the higher the possibility of catastrophe—and the scale of catastrophe increases significantly with the enhancement of product information features; (3) the optimal gamification for a sudden increase in grouplevel OIB can be identified, and the larger the extent of social networking, the easier it is for catastrophe behavior to occur.

Table 6. The Summary of Contributions to Theory.

<table><tr><td>Key findings</td><td>Literature gaps</td><td>Contributions</td></tr><tr><td colspan="3">Literature on OIB factors</td></tr><tr><td>External environmental cues/stimuli, consumer personality traits, and purchase situation factors (Dholakia, 2000; Verplanken &amp; Herabadi, 2001)</td><td rowspan="5">Less to quantify the dynamic evolution of OIB from the perspective of sudden change</td><td rowspan="5">Reveal the sudden change mechanism underlying OIB and the effect of IT-related factors by introducing catastrophe theory</td></tr><tr><td>Website quality (Wells et al., 2011)</td></tr><tr><td>Virtual atmospheric cues (Floh &amp; Madlberger, 2013)</td></tr><tr><td>Vividness and interactivity of online product presentations (Vonkeman et al., 2017)</td></tr><tr><td>Affective trust in the recommender and affection toward the recommended product (Chen et al., 2019)</td></tr><tr><td colspan="3">Literature on OIB mechanisms</td></tr><tr><td>Conceptualize impulse buying as a process-outcome mechanism within the domain of an individual-psychological approach (Rook &amp; Fisher, 1995; Verplanken &amp; Herabadi, 2001; Jones et al., 2003; Park et al., 2006; Wood, 1998; Coley &amp; Burgess, 2003; Siorowska, 2011; Kacen &amp; Lee, 2002; Lee &amp; Kacen, 2008)</td><td rowspan="2">Lack of study on group-level OIB mechanisms that emerge from individual interactions</td><td rowspan="2">An integrated simulation paradigm that combined a survey study, the QSIM technique, and the ABM model to investigate dynamic, group-level OIB mechanisms</td></tr><tr><td>Psychological mechanisms, such as personality traits related to impulsivity (including self-construal, self-esteem, variety-seeking, and depression) (Zhang &amp; Shrum, 2009; Harmancioglu et al, 2009; Sharma et al, 2010; Punj, 2011; Sneath et al, 2009)</td></tr><tr><td colspan="3">Literature on CT</td></tr><tr><td>The crash of stock exchanges (Barunik &amp; Vosvrda, 2009; Tutek &amp; Seven, 2013)</td><td rowspan="5">Failure to apply robust and rigorous CT to the analysis of ambiguous, incomplete, and time-varying psychological and behavioral mechanisms</td><td rowspan="5">Integrate QSIM and CT to transform a mathematical cusp catastrophe model into a qualitative catastrophe model to depict sudden changes in OIB with incomplete information</td></tr><tr><td>The dynamics of the housing market (Diks &amp; Wang, 2016)</td></tr><tr><td>Trends in team performance criteria (Guastello et al., 2013; Guastello et al., 2019)</td></tr><tr><td>Unhealthy behaviors at work (like workplace bullying) (Escartin et al., 2013)</td></tr><tr><td>A person&#x27;s sudden behavioral change (Hu &amp; Xia, 2015)</td></tr></table>

## 7.2 Contributions to Theory

As an early attempt to probe dynamic group-level OIB behaviors, our study contributes significantly to the emerging OIB literature in three distinct ways. First, we contribute to the OIB behaviors literature in the quantitative arena on consumer behavior by highlighting the perspective of sudden change offered by CT. Previous research on OIB has focused on the static level and has primarily used empirical investigations to identify OIB factors and their correlations, e.g., IT-enabled quantified-self designs (Wannheden et al., 2021; Huotari & Hamari, 2017; Vesa et al., 2017) and product information features (Weathers et al., 2015; Benlian et al., 2012; Jiménez & Mendoza, 2013; Lu et al., 2021), with a lesser focus on quantifying the dynamic evolution process of OIB (e.g., Dholakia, 2000; Verplanken & Herabadi, 2001; Wells et al., 2011; Floh & Madlberger, 2013; Vonkeman et al., 2017; Chen et al., 2019). We extend the literature by introducing catastrophe theory to reveal the nonlinear evolution mechanism underlying OIB. In addition, from a theoretical perspective, our study sheds light on the effect of IT-related factors on sudden changes in OIB. Addressing this issue reveals an unresolved theoretical question—namely, how to quantify the dynamic rapid shift in OIB, including the possibility and scale of sudden changes in OIB. Our contributions to theory are summarized in Table 6.

A key implication for future research is to avoid confining studies to a single time period, which makes it difficult to investigate the dynamic behavioral trajectory of OIB; instead, researchers should quantify the dynamic rapid shift in OIB. While our study focused on the effect of only several simple variables (e.g., quantified self) on sudden changes in OIB, future work could introduce more factors (such as product characteristics and personality factors) and examine how to incorporate optimization methods to identify the optimal combination of these OIB factors.

Second, our study contributes to the OIB behavior literature, which has mainly focused on individuallevel mechanisms, including impulse buying tendencies and other psychological mechanisms such as personality traits (Ma, 2013). There is scant research on group-level abrupt changes in OIB in the field of consumer behavior. As prior research has shown, macro-evolution mechanisms of group-level OIB emerge from individual interactions (Dong, 2022; Dong, 2019; Rahmandad & Sterman, 2008), which cannot be captured by prior research on individuallevel OIB. In light of this, our study extends these individual-level mechanisms to group-level mechanisms of OIB behavior. Specifically, our study significantly advances the current understanding of OIB behavior by highlighting the critical importance of sudden group-level changes in leveraging OIB in the market. Our findings complement existing research that explicates how group-level dynamics of OIB arise from individual interactions (Ma, 2013). Moreover, by focusing on how individual interactions (i.e., preferential selection and imitation) drive sudden group-level changes in OIB, our study responds to calls for research on understanding the “social influence” needed to successfully stimulate OIB, as exemplified by Ye and Fan (2017). Finally, our theorization sheds new light on the dynamic nature of group-level OIB by explicating how the sudden changes in OIB evolve over time at the group level.

Third, our study contributes to the extensive CT literature that has addressed several issues, such as stock market crash forecasting (Barunik & Vosvrda, 2009; Tutek & Seven, 2013), housing market crash prediction (Diks & Wang, 2016), human behavior investigation (Guastello et al., 2013; Guastello et al., 2019), workplace bullying prediction (Escartin et al., 2013), and suicidal ideation analysis (Bryan & Rudd, 2018). More recently, scholars have progressively applied CT to individual behaviors such as women’s decision-making in violent relationships (Katerndahl et al., 2017) and sudden employee resignations (Hu & Xia, 2015). While the literature has provided important insights, we know little about how to analyze consumers’ vague, incomplete, and time-varying psychological and behavioral trajectories or mechanisms (i.e., a system’s behavior with incomplete and erroneous information). Our study contributes to the literature by uncovering the underlying mechanisms of how the attributes of OIB behavior and their interactions work over time and evolve into the specific individual peculiarities and mechanisms forming the microfoundation of group-level OIB. We integrated QSIM and CT to transform a mathematical cusp catastrophe model into a qualitative catastrophe model to tackle sudden changes in OIB. Our key theoretical contribution goes beyond the research realm of OIB; this study statistically demonstrates that the qualitative catastrophe model, due to its underlying scientific rigor and realism, can be leveraged to explore other psychological or behavioral trajectories or mechanisms of consumers in future IS research.

Our study sheds new light on the use of multiple methodologies (a survey study, the QSIM technique, and the ABM model) to model group-level OIB, where a qualitative catastrophe model, based on a survey study, extracts specific individual peculiarities and mechanisms as the microfoundation of the ABM model. Our study underscores the importance of integrating multiple methods (mixed qualitativequantitative) to elicit deeper knowledge vis-à-vis OIB and other dynamic, group-level consumer behavior in future research. A key implication for future research is to not only consider the individual-level mechanism of OIB; rather, researchers should assess how various social influence factors (individual interactions) may result in sudden group-level changes in OIB. While the social network in our study is only a typification under certain assumptions (i.e., a static network), future work could build a dynamic social network to simulate the group-level OIB and reveal the influence of network dynamics.

## 7.3 Implications for Practice

Our findings offer several practical implications for businesses. First, sudden changes in group-level OIB occur as consumers’ sense of quantified self increases when self-control is low. Accordingly, businesses could leverage the quantified selves of consumers to boost their OIB to a high level. Specifically, quantified-self online tools could be enhanced to perform more sophisticated operations on user data to increase self-cognition. Effective measures for websites and mobile applications include recording, tracking, analyzing, and visualizing user data through gamification and social networking functions. This can be applied to marketing outlets to support retail campaign management.

Second, we found that the greater the number of consumers with a proving preference in a group, the higher the possibility of catastrophe; furthermore, the scale of catastrophe increases significantly with the enhancement of product information features. Therefore, e-shopping platforms can adopt effective measures to attract more consumers with a proving preference by making target customers think these products are worth their self-promotion. These measures include marketers finding the right positioning in product development and branding, adding targeted product labeling attributes (e.g., personality, trends, reputation, or taste), and establishing social platforms for consumers to display their taste, style, or status to satisfy consumers’ desire for conspicuous online consumption. E-shopping platforms are also incentivized to offer more incentives to encourage sellers to enhance the information features of their products. This could be applied to marketing outlets to support customer segmentation. For example, for search products, businesses could use social media to promote and display detailed product information through pictures and videos, and experience products could be displayed through reality shows and by live streaming using virtual reality and 5G technology. Third, optimal gamification for a sudden increase in group-level OIB could be identified; the larger the extent of social networking, the easier it is for catastrophe behavior to occur. Thus, businesses could use optimal gamification designs (such as virtual badges and milestones) in their quantified self-function designs to promote sudden increases in group-level OIB. However, overgamification occurs when gamification levels exceed optimal levels, such as gambling and highfrequency clicks, which can deplete users’ time, energy, and money, resulting in negative emotions. The optimal level of gamification design should be sustainable, comfortable for users when they are tired, or able to resist the absurdity of everyday life. Moreover, functions of social networking (such as leaderboards, “likes,” and “teams”) could be added to gamification-based IT-enabled quantified-self design. This approach would make it easier for enterprises to raise group-level OIB.

Although these measures could effectively raise grouplevel OIB, companies should also be aware of the ethical issues that may arise, such as data breaches, irrational consumption, obstruction of circular consumption, and overconsumption. First, despite the effectiveness in improving the retail campaign management level, the recent popularity of quantifiedself tools has been accompanied by the leakage of data generated by the quantified self to unethical large corporations or others, thus arousing wide concern about the privacy and security of these personal data, which may dissuade further adoption of quantified-self tools. Second, customer segmentation on the basis of individual preferences may result in excessive encouragement of consumers’ emotional shopping and other irrational consumption behaviors as an unfair business practice that manipulates consumers, which could greatly undermine consumer trust in the company or products. In addition, the phenomenon of precision marketing and the excessive information features in product development involve moral problems that hinder circular consumption. Third, overgamification and excessive functions of social networking in IT-enabled quantified-self design may encourage consumers to overspend. That is, the popularity of gamification and social networking tools could stimulate consumption desire and produce excessive consumption beyond the individual’s economic ability, which is likely to cause personal, family, and even larger scopes of financial crisis.

Finally, we note that this study has several limitations that should be addressed or overcome in the future. First, our behavior model, based on only a few simple variables, is far from a perfect representation of realistic OIB behavior. The constructs and relations that we investigated may vary across populations. For example, the survey results in Appendix B show that OIB is correlated with the educational background of consumers. Thus, more factors should be introduced into the model in the future to simulate more realistic OIB behavior. Second, in our model, the social network is only a typification under certain assumptions (i.e., a static network). Real social networks, on the contrary, are dynamic per se, with nodes entering or exiting and realtime changes occurring in their relationships. Therefore, future research could use an actual social network based on real-world data to extrapolate the impact of network dynamics on impulsive purchasing behavior.

## 7.4 Conclusion

With the rapid rise of online shopping, OIB has become an increasingly prevalent phenomenon. Prior studies have rarely investigated the mechanism of abrupt changes in OIB at the dynamic group level. To address the research gaps and advance this area of research and to answer the recent call for further research on OIB, we propose a sequential simulation approach subsuming a survey method, the QSIM technique, and the ABM model. The dynamic, group-level and abrupt change perspective enhances the understanding of OIB and reveals the important role of the combined effect of consumer selfcontrol and the quantified self on group OIB, factors related to individual preferences and product information features, and the effect of IT-enabled quantified-self design on dynamic group-level OIB. Our study breaks new theoretical ground for future research in this burgeoning area and potentially opens up new opportunities for the further investigation of OIB in IS. A key implication for future research is that researchers should quantify dynamic rapid shifts in OIB and assess how various social influence factors (individual interactions) may result in sudden group-level changes in OIB. This study has statistically demonstrated that because of its underlying scientific rigor and realism, the qualitative catastrophe model can be leveraged to explore other psychological or behavioral trajectories or mechanisms of consumers in future IS research. It also provides an effective tool for managers to support retail activity management and customer segmentation.

## Acknowledgements

This work was supported in part by the National Natural Science Foundation of China (Nos. 72271192, 71971093) and the Humanities and Social Science fund of the Ministry of Education of China (No. 22YJC630152). The corresponding author is Xin (Robert) Luo.

## References

Amaral, M. A., & Javarone, M. A. (2018). Heterogeneous update mechanisms in evolutionary games: Mixing innovative and imitative dynamics. Physical Review E, 97(4), Article 042305.

Amaral, M. A., Perc, M., Wardil, L., Szolnoki, A., da Silva Júnior, E. J., & da Silva, J. K. L. (2017). Role-separating ordering in social dilemmas controlled by topological frustration. Physical Review E, 95(3), Article 032307.

Amblee, N., & Bui, T. (2011). Harnessing the influence of social proof in online shopping: The effect of electronic word of mouth on sales of digital microproducts. International Journal of Electronic Commerce, 16(2), 91-114.

Anders, A. D. (2018). Networked learning with professionals boosts students’ self-efficacy for social networking and professional development. Computers & Education, 127, 13-29.

Attig, C., & Franke, T. (2018). I track, therefore I walk—Exploring the motivational costs of wearing activity trackers in actual users. International Journal of Human-Computer Studies, 127, 211-224.

Bakewell, C., & Mitchell, V. (2003), Generation Y female consumer decision‐making styles, International Journal of Retail & Distribution Management, 31(2), 95-106.

Barunik, J., & Vosvrda, M. (2009). Can a stochastic cusp catastrophe model explain stock market crashes? Journal of Economic Dynamics & Control, 33(10), 1824-1836.

Baumeister, R. F. (2002). Yielding to Temptation: Self‐Control Failure, Impulsive Purchasing, and Consumer Behavior. Journal of Consumer Research, 28(4), 670-676.

Bearden, W. O., Netemeyer, R. G., & Teel, J. E. (1989). Measurement of consumer susceptibility to interpersonal influence. Journal of Consumer Research, 15(4), 473- 481.

Bellazzi, R., Guglielmann, R., & Ironi, L. (2000). How to improve fuzzy-neural system modeling by means of qualitative simulation. IEEE Transactions on Neural Networks, 11(1), 249- 253.

Benbya, H., Nan, N., Tanriverdi, H., & Yoo, Y. (2020). Complexity and information systems research in the emerging digital world. MIS Quarterly, 44(1), 1-17.

Benlian, A., Titah, R., & Hess, T. (2012). Differential effects of provider recommendations and consumer reviews in e-commerce transactions: An experimental study. Journal of Management Information Systems, 29(1), 237- 272.

Berlinski, D. (1978). Catastrophe theory and its applications: A critical review. Behavioral Science, 23(4), 402-416.

Bossuyt, S., Vermeir, I., Slabbinck, H., De Bock, T., & Van Kenhove, P. (2017). The compelling urge to misbehave: Do impulse purchases instigate unethical consumer behavior? Journal of Economic Psychology, 58, 60-76.

Bryan, C. J., & Rudd, M. D. (2018). Nonlinear change processes during psychotherapy characterize patients who have made multiple suicide attempts. Suicide and Life-Threatening Behavior, 48(4), 386-400.

Bryan, C. J., Butner, J. E., May, A. M., Rugo, K. F., Harris, J. A., Oakey, D. N., & Bryan, A. O. (2020). Nonlinear change processes and the emergence of suicidal behavior: A conceptual model based on the fluid vulnerability theory of suicide. New Ideas in Psychology, 57, Article 100758.

Buckley, P., & Doyle, E. (2014). Gamification and student motivation. Interactive Learning Environments, 24(6), 1162-1175.

Burnkrant, R. E., & Cousineau, A. (1975). Informational and normative social influence in buyer behavior. Journal of Consumer Research, 2(3), 206-215.

Butner, J. E., Gagnon, K. T., Geuss, M. N., Lessard, D. A., & Story, T. N. (2015). Utilizing topology to generate and test theories of change. Psychological Methods, 20(1), 1-25.

Cao, Q., Chen, P., Zhang, G., Zhao, J., & Xin, A. C. (2010). Research on qualitative simulation of miners groups’ safety behaviors. Proceedings of the International Conference on Mine Hazards Prevention and Control (Vol. 10, pp. 603-609).

Chan, T. K. H., Cheung, C. M. K., & Lee, Z. W. Y. (2017). The state of online impulse-buying research: A literature analysis. Information & Management, 54(2), 204-217.

Charitsis, V., Yngfalk, A. F., & Skalen, P. (2019). “Made to run”: Biopolitical marketing and the making of the self-quantified runner. Marketing Theory, 19(3), 347-366.

Chen, Y., Lu, Y., Wang, B., & Pan, Z. (2019). How do product recommendations affect impulse

buying? An empirical study on WeChat social commerce. Information & Management, 56(2), 236-248.

Coley, A., & Burgess, B. (2003). Gender differences in cognitive and affective impulse buying. Journal of Fashion Marketing and Management: An International Journal, 7(3), 282-295.

Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. Psychometrika, 16(3), 297-334.

Danaher, J., Nyholm, S., & Earp, B. D. (2018). The Quantified Relationship. The American Journal of Bioethics, 18(2), 3-19.

Davis, F. D. (1989). Perceived usefulness, perceived ease of use and user acceptance of information technology. MIS Quarterly, 13(3), 318-340.

Davis, F. D., Bagozzi, R. P., & Warshaw, P. R. (1989). User acceptance of computer technology: A comparison of two theoretical models. Management Science, 35(8), 982-1003.

Davis, J. P., Eisenhardt, K. M., & Bingham, C. B. (2007). Developing theory through simulation methods. Academy of Management Review, 32(2), 480-499.

Deng, L. L., & Zhang, X. (2013). Fault detection and diagnosis based on qualitative simulation. Advanced Materials Research, 821-822, 1499- 1504.

Deterding, S. (2015). The lens of intrinsic skill atoms: A method for gameful design. Human-Computer Interaction, 30(3-4), 294-335.

Deutsch, M., & Gerard, H. B. (1955). A study of normative and informational social influences upon individual judgment. The Journal of Abnormal and Social Psychology, 51(3), 629- 636.

Dholakia, U. M. (2000). Temptation and resistance: An integrated model of consumption impulse formation and enactment. Psychology & Marketing, 17(11), 955-982.

Diks, C., & Wang, J. (2016). Can a stochastic cusp catastrophe model explain housing market crashes? Journal of Economic Dynamics & Control, 69, 68-88.

Dong, J. Q. (2019). Numerical data quality in simulation research: A reflection and epistemic implications. Decision Support Systems, 126, Article 113134.

Dong, J. Q. (2021). Technological Choices under uncertainty: Does organizational aspiration matter? Strategic Management Journal, 42(5), 898-916.

Dong, J. Q. (2022). Using simulation in information systems research. Journal of the Association for Information Systems, 23(2), 408-417.

Dong, J. Q., Karhade, P. P., Rai, A., & Xu, S. X. (2021). How Firms Make Information technology investment decisions: Toward a behavioral agency theory. Journal of Management Information Systems, 38(1), 29- 58.

Escartin, J., Ceja, L., Navarro, J., & Zapf, D. (2013). Modeling workplace bullying behaviors using catastrophe theory. Nonlinear Dynamics Psychology and Life Sciences, 17(4), 493-515.

Fang, X., & Hu, P.J.-H. (2018). Top persuader prediction for social networks. MIS Quarterly, 42(1), 63-82.

Fawcett, T. (2015). Mining the quantified self: Personal knowledge discovery as a challenge for data science. Big Data, 3(4), 249-266.

Festinger, L. (1962). Cognitive dissonance. Scientific American, 207(4), 93-102.

Flay, B. R. (1978). Catastrophe theory in socialpsychology: Some applications to attitudes and social-behavior. Behavioral Science, 23(5), 335-350.

Floh, A., & Madlberger, M. (2013). The role of atmospheric cues in online impulse-buying behavior. Electronic Commerce Research and Applications, 12(6), 425-439.

Forbus, K. D. (1984). Qualitative process theory. Artificial Intelligence, 24(1-3), 85-168.

Fuel, R. (2014). Quantified self digital tools: A CPG marketing opportunity. Technical Report. Rocket Fuel. Retrieved on October 6, 2020 from http://rocketfuel.com/blog/quantified-self

Gefen, D., Karahanna, E., & Straub, D. W. (2003). Trust and TAM in online shopping: An integrated model. MIS Quarterly, 27(1), 51-90.

Goetzke, F. (2008). Network effects in public transit use: Evidence from a spatially autoregressive mode choice model for New York. Urban Studies, 45(2), 407-417.

Grasman, R., van der Maas, H. L., & Wagenmakers, E. J. (2010). Fitting the cusp catastrophe in R: A cusp package primer. Journal of Statistical Software, 32, 1-27.

Grieve, R., & Watkinson, J. (2016). The psychological benefits of being authentic on Facebook. Cyberpsychology, Behavior, and Social Networking, 19(7), 420-425.

Guastello, S. J., Boeh, H., Gorin, H., Huschen, S., Peters, N. E., Fabisch, M., & Poston, K. (2013). Cusp catastrophe models for cognitive workload and fatigue: a comparison of seven task types. Nonlinear Dynamics Psychology and Life Sciences, 17(1), 23-47.

Guastello, S. J., Correro, A. N., II, & Marra, D. E. (2019). Cusp catastrophe models for cognitive workload and fatigue in teams. Applied Ergonomics, 79, 152-168.

Hackel, T. S., Jones, M. H., Carbonneau, K. J., & Mueller, C. E. (2016). Re-examining achievement goal instrumentation: Convergent validity of AGQ and PALS. Contemporary Educational Psychology, 46, 73-80.

Hair, J. F., Hult, G. T. M., Ringle, C. M., Sarstedt, M., & Thiele, K. O. (2017). Mirror, mirror on the wall: a comparative evaluation of compositebased structural equation modeling methods. Journal of the Academy of Marketing Science, 45(5), 616-632.

Hair, J. F., Sarstedt, M., & Ringle, C. M. (2019). Rethinking some of the rethinking of partial least squares. European Journal of Marketing.

Hamari, J., Hassan, L., & Dias, A. (2018). Gamification, quantified-self or social networking? Matching users’ goals with motivational technology. User Modeling and User-Adapted Interaction, 28(1), 35-74.

Harmancioglu, N., Zachary Finney, R. and Joseph, M. (2009), Impulse purchases of new products: an empirical analysis, Journal of Product & Brand Management, 18(1), 27-37.

Hassan, L., Dias, A., & Hamari, J. (2019). How motivational feedback increases user's benefits and continued use: A study on gamification, quantified-self and social networking. International Journal of Information Management, 46, 151-162.

Henseler, J., Ringle, C. M., & Sarstedt, M. (2015). A new criterion for assessing discriminant validity in variance-based structural equation modeling. Journal of the Academy of Marketing Science, 43(1), 115-135.

Ho, S. S., Lee, E. W. J., & Liao, Y. (2016). Social network sites, friends, and celebrities: The roles of social comparison and celebrity involvement in adolescents’ body image dissatisfaction. Social Media + Society, 2(3). https://doi.org/10.1177/2056305116664216

Hochwarter, W. A., Witt, L. A., & Kacmar, K. M. (2000). Perceptions of organizational politics as a moderator of the relationship between

consciousness and job performance. Journal of Applied Psychology, 85(3), 472-478.

Hoeppner, B. B., Kelly, J. F., Urbanoski, K. A., & Slaymaker, V. (2011). Comparative utility of a single-item versus multiple-item measure of self-efficacy in predicting relapse among young adults. Journal of Substance Abuse Treatment, 41(3), 305-312.

Hu, B., & Xia, N. (2015). Cusp catastrophe model for sudden changes in a person’s behavior. Information Sciences, 294, 489-512.

Huotari, K., & Hamari, J. (2017). A definition for gamification: anchoring gamification in the service marketing literature. Electronic Markets, 27(1), 21-31.

Iyengar, R., Van den Bulte, C., & Valente, T. W. (2011). Opinion leadership and social contagion in new product diffusion. Marketing Science, 30(2), 195-212.

Jiang, G., Ma, F., Shang, J., & Chau, P. Y. (2014). Evolution of knowledge sharing behavior in social commerce: An agent-based computational approach. Information Sciences, 278, 250-266.

Jiang, G., Tadikamalla, P. R., Shang, J., & Zhao, L. (2016). Impacts of knowledge on online brand success: An agent-based model for online market share enhancement. European Journal of Operational Research, 248(3), 1093-1103.

Jiménez, F. R., & Mendoza, N. A. (2013). Too popular to ignore: The influence of online reviews on purchase intentions of search and experience products. Journal of Interactive Marketing, 27(3), 226-235.

Jones, M. A., Reynolds, K. E., Weun, S., & Beatty, S. E. (2003). The product-specific nature of impulse buying tendency. Journal of Business Research, 56(7), 505-511.

Jorczak, R. L. (2011). An information processing perspective on divergence and convergence in collaborative learning. International Journal of Computer-Supported Collaborative Learning, 6(2), 207-221.

Kacen, J. J., & Lee, J. A. (2002). The influence of culture on consumer impulsive buying behavior. Journal of Consumer Psychology, 12(2), 163-176.

Karhade, P. P., & Dong, J. Q. (2021). Innovation outcomes of digitally enabled collaborative problemistic search capability. MIS Quarterly, 45(2), 693-717.

Katerndahl, D. A., Burge, S. K., Ferrer, R. L., Becho, J., & Wood, R. (2017). Is readiness to take action among women in violent relationships a catastrophic phenomenon? Journal of Interpersonal Violence, 35, (7-8), 1610-1634.

Kimiagari, S., & Asadi Malafe, N. S. (2021). The role of cognitive and affective responses in the relationship between internal and external stimuli on online impulse buying behavior. Journal of Retailing and Consumer Services, 61, Article 102567.

Knoeri, C., Binder, C. R., & Althaus, H. J. (2011). An agent operationalization approach for context specific agent-based modeling. JASSS: The Journal of Artificial Societies and Social Simulation, 14(2), Article 4.

Krasnova, H., Widjaja, T., Buxmann, P., Wenninger, H., & Benbasat, I. (2015). Why following friends can hurt you: An exploratory investigation of the effects of envy on social networking sites among college-age users. Information Systems Research, 26(3), 585-605.

Kuipers, B. (1986). Qualitative simulation. Artificial Intelligence, 29(3), 289-338.

Kuipers, B. (1993). Qualitative simulation: then and now. Artificial Intelligence, 59(1-2), 133-140.

Lee, D. K. L., & Borah, P. (2019). Self-presentation on Instagram and friendship development among young adults: A moderated mediation model of media richness, perceived functionality, and openness. Computers in Human Behavior, 103, 57-66.

Lee, J. A., & Kacen, J. J. (2008). Cultural influences on consumer satisfaction with impulse and planned purchase decisions. Journal of Business Research, 61(3), 265-272.

Lee, S. Y. (2014). How do people compare themselves with others on social network sites? The case of Facebook. Computers in Human Behavior, 32, 253-260.

Lei, L., Zhu, Y., & Liu, Q. (2021). Analysis on quantified self-behavior of customers in food consumption under the perspective of social networks. Complexity, 2021. https://doi.org/ 10.1155/2021/6001654

Lin, K.-Y., & Lu, H.-P. (2011). Why people use social networking sites: An empirical study integrating network externalities and motivation theory. Computers in Human Behavior, 27(3), 1152-1161.

Liu, Y., Lv, X., & Tang, Z. (2021). The impact of mortality salience on quantified self behavior during the COVID-19 pandemic. Personality

and Individual Differences, 180, Article 110972.

Lord, K. R., and Lee, M. S. (2001). Differences in normative and informational social influence. Advances in Consumer Research, 28, 280-285.

Lu, J., Su, X., Diao, Y., Wang, N., & Zhou, B. (2021). Does online observational learning matter? Empirical evidence from panel data. Journal of Retailing and Consumer Services, 60, Article 102480.

Luo, X. (2005). How does shopping with others influence impulsive purchasing? Journal of Consumer Psychology, 15(4), 288-294.

Ma, W. (2013). To buy or not to buy? A behavioural approach to examine consumer impulse buying choice in various situations [Unpublished doctoral dissertation]. Durham University.

Mailath, G. J., & Postlewaite, A. (2003). The social context of economic decisions. Journal of the European Economic Association, 1(2-3), 354- 362.

Maltseva, K., & Lutz, C. (2018). A quantum of self: A study of self-quantification and self-disclosure. Computers in Human Behavior, 81, 102-114.

Mann, T., de Ridder, D., & Fujita, K. (2013). Selfregulation of health behavior: Social psychological approaches to goal setting and goal striving. Health Psychology, 32(5), 487- 498.

McCallum, S. (2012). Gamification and serious games for personalized health. Studies in Health Technology and Informatics, 177, 85-96.

Martíns, J. J. G., Moayery, M., & Cantín, L. N. (2019). How does self-control operate? A focus on impulse buying. Papeles del Psicólogo, 40(2), 149-156.

Meece, J. L., Anderman, E. M., & Anderman, L. H. (2006). Classroom goal structure, student motivation, and academic achievement. Annual Review of Psychology, 57, 487-503.

Moore, P., & Robinson, A. (2016). The quantified self: What counts in the neoliberal workplace. New Media & Society, 18(11), 2774-2792.

Nelson, P. (1970). Information and consumer behavior. Journal of Political Economy, 78(2), 311-329.

Neville, B., Fasli, M., & Pitt, J. (2015). Utilising social recommendation for decision-making in distributed multi-agent systems. Expert Systems with Applications, 42(6), 2884-2906.

Osorio, A. (2017). Self-interest and equity concerns: A behavioural allocation rule for operational problems. European Journal of Operational Research, 261(1), 205-213.

Park, E. J., Kim, E. Y., & Forney, J. C. (2006). A structural model of fashion‐oriented impulse buying behavior. Journal of Fashion Marketing and Management, 10(4), 433-446.

Perc, M., Jordan, J. J., Rand, D. G., Wang, Z., Boccaletti, S., & Szolnoki, A. (2017). Statistical physics of human cooperation. Physics Reports, 687, 1-51.

Plante, I., O'Keefe, P. A., & Theoret, M. (2013). The relation between achievement goal and expectancy-value theories in predicting achievement-related outcomes: A test of four theoretical conceptions. Motivation and Emotion, 37(1), 65-78.

Preacher, K. J., & Hayes, A. F. (2004). SPSS and SAS procedures for estimating indirect effects in simple mediation models. Behavior Research Methods Instruments & Computers, 36(4), 717- 731.

Punj, G. (2011). Impulse buying and variety seeking: Similarities and differences. Journal of Business Research, 64(7), 745-748.

Rahmandad, H., & Sterman, J. (2008). Heterogeneity and network structure in the dynamics of diffusion: Comparing agent-based and differential equation models. Management Science, 54(5), 998-1014.

Rand, W., & Rust, R. T. (2011). Agent-based modeling in marketing: Guidelines for rigor. International Journal of Research in Marketing, 28(3), 181-193.

Roche, M. J., Pincus, A. L., Hyde, A. L., Conroy, D. E., & Ram, N. (2013). Within-person covariation of agentic and communal perceptions: Implications for interpersonal theory and assessment. Journal of Research in Personality, 47(4), 445-452.

Rook, D. W., & Fisher, R. J. (1995). Normative influences on impulsive buying behavior. Journal of Consumer Research, 22(3), 305- 313.

Roskes, M., Elliot, A. J., & De Dreu, C. K. W. (2014). Why is avoidance motivation problematic, and what can be done about it? Current Directions in Psychological Science, 23(2), 133-138.

Ruckenstein, M., & Pantzar, M. (2017). Beyond the Quantified Self: Thematic exploration of a dataistic paradigm. New Media & Society, 19(3), 401-418.

Ruggieri, S., Bonfanti, R. C., Passanisi, A., Pace, U., & Schimmenti, A. (2021). Electronic surveillance in the couple: The role of selfefficacy and commitment. Computers in Human Behavior, 114, Article 106577.

Sangle, P. S., & Awasthi, P. (2011). Consumer's expectations from mobile CRM services: a banking context. Business Process Management Journal, 17(6), 898-918.

Sargent, R. G. (2013). Verification and validation of simulation models. Journal of Simulation, 7(1), 12-24.

Schau, H. J., Muñiz Jr, A. M., & Arnould, E. J. (2009). How brand community practices create value. Journal of Marketing, 73(5), 30-51.

Schoech, D., Boyas, J. F., Black, B. M., & Elias-Lambert, N. (2013). Gamification for behavior change: Lessons from developing a social, multiuser, web-tablet based prevention game for youths. Journal of Technology in Human Services, 31(3), 197-217.

Schroeder, T. C., Tonsort, G. T., Pennings, J. M. E., & Minter, J. (2007). Consumer food safety risk perceptions and attitudes: Impacts on beef consumption across countries. The B. E. Journal of Economic Analysis and Policy, 7(1). https://doi.org/10.2202/1935-1682.1848

Serrano, E., & Iglesias, C. A. (2016). Validating viral marketing strategies in Twitter via agent-based social simulation. Expert Systems with Applications, 50, 140-150.

Sharma, P., Sivakumaran, B., & Marshall, R. (2010). Impulse buying and variety seeking: A traitcorrelates perspective. Journal of Business Research, 63(3), 276-283.

Sheridan, J. E. (1985). A catastrophe model of employee withdrawal leading to low job performance, high absenteeism, and job turnover during the first year of employment. Academy of Management Journal, 28(1), 88- 109.

Sheridan, J. E., & Abelson, M. A. (1983). Cusp catastrophe model of employee turnover. Academy of Management Journal, 26(3), 418- 436.

Simon, H. A. (1991). Bounded rationality and organizational learning. Organization Science, 2(1), 125-134.

Siorowska, A. G. 2011. Gender as a moderator of temperamental causes of impulse buying tendency. Journal of Customer Behaviour, 10, 119-142.

Sneath, J. Z., Lacey, R., & Kennett-Hensel, P. A. (2009). Coping with a natural disaster: Losses, emotions, and impulsive and compulsive buying. Marketing Letters, 20(1), 45-60.

Spiller, K., Ball, K., Bandara, A., Meadows, M., McCormick, C., Nuseibeh, B., & Price, B. A. (2017). Data privacy: Users’ thoughts on quantified self personal data. In B. Ajana. (Ed.), Self-tracking (pp. 111-124). Palgrave Macmillan.

Stewart, I. N., & Peregoy, P. L. (1983). Catastrophe theory modeling in psychology. Psychological Bulletin, 94(2), 336-362.

Stragier, J., Vanden Abeele, M., Mechant, P., & De Marez, L. (2016). Understanding persistence in the use of online fitness communities: Comparing novice and experienced users. Computers in Human Behavior, 64, 34-42.

Straub, D. W. (1989). Validating instruments in MIS research. MIS Quarterly, 13(2), 147-169.

Survey Office of the National Bureau of Statistics in Beijing. (2020). Strong will to buy the online potential to continue to release—2019 Beijing online shopping user survey report. Beijing Municipal Bureau Statistics. http://www.beijing.gov.cn/gongkai/shuju/sjjd/ 202006/t20200605\_1917363.html.

Swann, W. B., Jr., Milton, L. P., & Polzer, J. T. (2000). Should we create a niche or fall in line? Identity negotiation and small group effectiveness. Journal of Personality and Social Psychology, 79(2), 238-250.

Szabó, G., & Fáth, G. (2007). Evolutionary games on graphs. Physics Reports, 446(4-6), 97-216.

Szabó, G., Vukov, J., & Szolnoki, A. (2005). Phase diagrams for an evolutionary prisoner’s dilemma game on two-dimensional lattices. Physical Review E, 72(4), Article 047107.

Tangney, J. P., Baumeister, R. F., & Boone, A. L. (2004). High self‐control predicts good adjustment, less pathology, better grades, and interpersonal success. Journal of Personality, 72(2), 271-324.

Thom, R. (1977). Structural stability, catastrophe theory, and applied mathematics. Siam Review, 19(2), 189-201.

Tsai, W. S., Yang, Q., & Liu, Y. (2013). Young Chinese consumers’ snob and bandwagon luxury consumption preferences. Journal of International Consumer Marketing, 25(5), 290- 304.

Tu, R., Hsieh, P., & Feng, W. (2018). Walking for fun or for “likes”? The impacts of different gamification orientations of fitness apps on consumers’ physical activities. Sport Management Review, 22(5), 682-693.

Tutek, H. H., & Seven, U. (2013). An application of the cusp catastrophe theory to the Istanbul stock exchange crash of 2008. Iktisat Isletme Ve Finans, 28(330), 41-60.

Van Roy, R., & Zaman, B. (2017). Why gamification fails in education and how to make it successful: Introducing nine gamification heuristics based on self-determination theory. In M. Ma& A. Oikonomou (Eds), Serious games and edutainment applications (pp. 485- 509). Springer.

Verhagen, T., & van Dolen, W. (2011). The influence of online store beliefs on consumer online impulse buying: A model and empirical application. Information & Management, 48(8), 320-327.

Vesa, M., Hamari, J., Harviainen, J. T., & Warmelink, H. (2017). Computer games and organization studies. Organization Studies, 38(2), 273-284.

Vonkeman, C., Verhagen, T., & van Dolen, W. (2017). Role of local presence in online impulse buying. Information & Management, 54(8), 1038-1048.

Wang, X. Z., Yang, S. A., Yang, S. H., & McGreavy, C. (1996). The application of fuzzy qualitative simulation in safety and operability assessment of process plants. Computers & Chemical Engineering, 20, S671-S676.

Wannheden, C., Stenfors, T., Stenling, A., & Schwarz, U. (2021). Satisfied or frustrated? A qualitative analysis of need satisfying and need frustrating experiences of engaging with digital health technology in chronic care. Frontiers in Public Health, 8, Article 623773.

Weathers, D., Swain, S. D., & Grover, V. (2015). Can online product reviews be more helpful? Examining characteristics of information content by product type. Decision Support Systems, 79, 12-23.

Wei, X., Hu, B., & Carley, K. M. (2013). Combination of empirical study with qualitative simulation for optimization problem in mobile banking adoption. JASSS-The Journal of Artificial Societies and Social Simulation, 16(3) Article 10.

Wells, J. D., Parboteeah, V., & Valacich, J. S. (2011). Online impulse buying: Understanding the interplay between consumer impulsiveness and

website quality. Journal of the Association for Information Systems, 12(1), 32-56.

Wood, M. (1998). Socio-economic status, delay of gratification, and impulse buying. Journal of Economic Psychology, 19(3), 295-320.

Wu, I.-L., Chiu, M.-L., & Chen, K.-W. (2020). Defining the determinants of online impulse buying through a shopping process of integrating perceived risk, expectationconfirmation model, and flow theory issues. International Journal of Information Management, 52, Article 102099.

Xu, L., Li, J., Zhang, X., Pang, Y., Yu, T., Lian, X., ... & Li, F. (2022). Mobile health-based gamification intervention to increase physical activity participation among patients with coronary heart disease: study protocol of a randomised controlled trial. BMJ Open, 12(1), Article e054623.

Yang, H.-X., & Tian, L. (2017). Enhancement of cooperation through conformity-driven

reproductive ability. Chaos, Solitons & Fractals, 103, 159-162.

Ye, W., & Fan, S. (2017). Evolutionary snowdrift game with rational selection based on radical evaluation. Applied Mathematics and Computation, 294, 310-317

Zhang, P. (2008). Technical opinion motivational affordances: Reasons for ICT design and use. Communications of the ACM, 51(11), 145-147.

Zhang, Y. & Shrum, L. J. (2009). The influence of selfconstrual on impulsive consumption. Journal of Consumer Research, 35, 838-850.

Zheng, X., Men, J., Yang, F., & Gong, X. (2019). Understanding impulse buying in mobile commerce: An investigation into hedonic and utilitarian browsing. International Journal of Information Management, 48, 151-160.

Zimmerman, B. J. (2013). From cognitive modeling to self-regulation: A social cognitive career path. Educational Psychologist, 48(3), 135-147.

## Appendix A

Mathematically, the cusp potential function is given as Equation (A1):

$$
V (f, u, v) = f ^ {4} + u f ^ {2} + v f. \mathrm{(A1)}
$$

Taking the derivative of Equation (A1), we have:

$$
\frac {\partial V (f , u , v)}{\partial f} = 4 f ^ {3} + 2 u f + v = 0.\tag{A2}
$$

Then taking the derivative of Equation (A2), we have:

$$
\frac {\partial^ {2} V (f , u , v)}{\partial f ^ {2}} = 1 2 f ^ {2} + 2 u = 0. \mathrm{(A3)}
$$

From Equation (A3), we can conclude that:

$$
f ^ {2} = - \frac {1}{6} u.\tag{A4}
$$

Substituting Equation (A4) into the equation(A2) gives $\begin{array} { r } { 4 f * \left( - \frac { 1 } { 6 } u \right) + 2 u f + v = 0 } \end{array}$ , namely:

$$
\frac {4}{3} u f + v = 0.\tag{A5}
$$

From Equation (A5), we can conclude that:

$$
f = - \frac {3 v}{4 u}. (\mathrm{A6})
$$

Substituting Equation (A6) into the equation (A3) gives $\begin{array} { r } { 1 2 * ( - \frac { 3 v } { 4 u } ) ^ { 2 } + 2 u = 0 } \end{array}$ , namely:

$$
\frac {2 7 v ^ {2}}{4 u ^ {2}} + 2 u = 0.\tag{A7}
$$

From Equation (A7), we can conclude that:

$2 7 v ^ { 2 } + 8 u ^ { 3 } = 0 .$ . (A8)

## Appendix B

## Empirical Model and Analysis

To identify OIB’s interior drivers and the interactions among them, a questionnaire was designed to obtain and statistically analyze data from consumers. OIB is a type of individual behavior influenced by psychological processes. To accurately describe the mechanism of sudden changes caused by those psychological activities, we selected factors that could directly reflect the psychological activities of individuals as constructs. OIB is an increasingly frequent phenomenon with the development of e-commerce and is marked by consumers’ irrationality and lack of willpower (Bossuyt et al., 2017). According to the cognitive dissonance theory (Festinger, 1962) and self-concept theory (Baumeister, 2002), the quantified self and self-control influence the psychology of individuals during the process of OIB. The quantified self allows consumers to follow more rational and precise consumption patterns through objective quantification (Ruckenstein & Pantzar, 2017), and self-control reflects individual willpower by shaping human behavior (Martíns et al., 2019). Accordingly, the quantified self and self-control were selected as the constructs of our model.

## Hypotheses

The quantified self: The quantified self involves ordinary people recording and analyzing multitudinous aspects of their lives to understand and improve themselves (Fawcett, 2015). For example, many people are now in possession of devices such as a Fitbit, Jawbone UP, or an Apple Watch to voluntarily log and track numerous data points in their daily lives (Danaher et al., 2018). Meanwhile, many websites and mobile apps such as Taobao, Alipay, and WeChat automatically record and analyze user data in the background via consumption records and relay the results of their analysis to users. According to cognitive dissonance theory (Festinger, 1962), when people recognize their overspending, they feel mental anguish. To rectify this imbalance, they engage in management of their consumption behavior and attempt to reduce the number of their impulse purchases. Therefore, we posit that consumers with a high level of self-quantification will decrease their OIB behavior:

H1: The quantified self has a negative effect on OIB behavior.

Self-control: In this paper, self-control, seen as one of the most powerful and beneficial human capacities, means that consumers sacrifice short-term choices that bring immediate happiness for long-term benefits. Failure to exercise selfcontrol usually means that consumers choose short-term instant happiness at the expense of long-term benefits, which may be an important cause of impulsive purchasing (Baumeister, 2002). People with high levels of self-control show fewer impulse control problems (Tangney et al., 2004). For example, people with specific weight loss goals are more likely to resist the temptation of placing dessert orders at restaurants. When people consciously monitor their spending, they can control themselves to reduce the occurrence of impulse buying behaviors. Inadequate ability or failure to exercise self-control is more likely to induce consumers into making impulsive decisions. Therefore, we posit that self control might reduce the risk of OIB:

## H2: Self-control has a negative effect on OIB behavior.

The quantified self and self-control: Effective self-control depends on three major factors: the standards, a monitoring process, and the operational capacity to alter one’s behavior (Baumeister, 2002). Quantifying one’s own self can be viewed as a self-monitoring process. When consumers quantify themselves, the unknown aspects of their lives become clear and predictable. Through reexamination and reflection, they can control themselves effectively and curb impulse purchases. Relevant research has emphasized the positive effect of the quantified self on the optimization and control of consumer behavior (Ruckenstein & Pantzar, 2017; Moore & Robinson, 2016). In practice, tracking data (such as daily activity and caloric intake) on eating and health status can help people control their body shape. Therefore, we posit that:

H3: The quantified self has a positive effect on self-control.

Based on the above hypothesis, we posit that:

H4: Self-control has a mediating effect between quantitative self and OIB.

Control variables: Besides the above core constructs, we also incorporate three demographic variables (i.e., age, gender, and educational background) suggested by Hochwarter et al. (2000), Bakewell & Mitchell (2003), and Coley & Burgess (2003).

## Measurement

To investigate the relationship between quantified self, self-control, and OIB, a measurement scale was developed and validated. The sample was collected through a prevalent online survey platform (www.wjx.cn) in China. The survey hyperlink was placed online, and only those who had online shopping experiences were targeted for data gathering. They had a chance to win some reward after completing the questionnaire. Out of the total of 250 distributed questionnaires, 207 were returned, yielding a 75.6 percent usable response rate (18 incomplete responses excluded). The majority of this sample consisted of young people with a higher educational background (as Table B1 shows). This a good sample as it fits the profile of the typical online shopper in China (Beijing Municipal Bureau Statistics, 2020).

Table B1. Sample Characteristics

<table><tr><td>Gender</td><td>Percentage</td><td>Age</td><td>Percentage</td><td>Educational background</td><td>Percentage</td></tr><tr><td>Female</td><td>63.5%</td><td>18 – 30</td><td>57.1%</td><td>undergraduates and above</td><td>90.5%</td></tr><tr><td>Male</td><td>36.5%</td><td>others</td><td>42.9%</td><td>others</td><td>9.5%</td></tr></table>

Single-item OIB measure: A widely used single-item measure developed by Rook was used (Rook & Fishe,1995), in which respondents will project themselves into the shopping scenario presented in this imaginary stimulus situation. Compared to the questionnaire investigation and simple recall method, this method is closer to the actual daily lives of consumers. Simultaneously, the projective effect of the subjects was utilized to reduce the occurrence of social desirability biases (Rook & Fishe, 1995). Also, it has been shown that single-item measures have comparable or equal predictive validity compared to multiple-item measures for constructs in psychological, marketing, and medical research (Hoeppner et al., 2011). This single-item measure forces respondents to choose what the consumer described in the following imaginary online shopping situation (see Table B2, where five options are designed to represent varying levels of buying impulsiveness from low to high) and the results can ensure authenticity and objectivity.

The quantified self: We developed a set of six items to measure the quantified self, based on the Self-Quantification Scales (Maltseva & Lutz, 2018), and items about the Strava using research (Stragier et al., 2016). Respondents were asked to state their agreement on a 5-point Likert scale. Initial principal component analysis of all six items showed low loadings on two items. Therefore, we excluded those two items from the analysis leaving a parsimonious four item solution. All measures and corresponding items are included in Table B3.

Self-control: Self-control was measured with the widely applied “Self-Control Scale” developed by Tangney et al. (2004). We simplified the scale to include 4 measurement items, which are rated on a 5-point Likert scale from strongly disagree (1) to strongly agree (5). Again, Table B3 shows the wording.

Table B2. Single-Item Measurement of OIB

<table><tr><td>Virtual situation</td><td colspan="2">You are a college student and your income is paid by your family each month at a fixed time. You currently have little money left, and there is a week before receiving your remittance. However, you need to buy a formal suit for tomorrow&#x27;s interview. You are currently browsing an online shopping website and have selected a formal suit. Suddenly, you find that one of your favorite shoe brands is offering a 30% discount. This brand has very few promotions. You like a pair of shoes in this shop very much. In addition, if you purchase more than two items, you can enjoy an additional 20% discount.</td></tr><tr><td>Option 1</td><td>Buying the formal suit only and do not consider the shoes at all.</td><td>□</td></tr><tr><td>Option 2</td><td>Buying the formal suit, and considering the shoes but not buying it.</td><td>□</td></tr><tr><td>Option 3</td><td>Buying the shoes, but not the formal suit.</td><td>□</td></tr><tr><td>Option 4</td><td>Buying both the formal suit and the shoes by either borrowing money from friends or using Ant Credit Pay or other credit products</td><td>□</td></tr><tr><td>Option 5</td><td>Buying both the formal suit and the shoes by either borrowing money from friends or using Ant Credit Pay or other credit products, as well as buying other items for sale in the store.</td><td>□</td></tr></table>

Table B3. Measurement Items and Reliability

<table><tr><td>Measurement item</td><td>AVE</td><td>Alpha</td><td>FL</td><td>CR</td></tr><tr><td>Quantified Self (QS):</td><td>0.566</td><td>0.837</td><td></td><td>0.839</td></tr><tr><td>QS1: I monitor my behavior through mobile apps.</td><td></td><td></td><td>0.733</td><td></td></tr><tr><td>QS2: I collect and analyze data on my specific activities to better adjust the activities.</td><td></td><td></td><td>0.824</td><td></td></tr><tr><td>QS3: I am eager to acquire more data about myself to better understand and control myself.</td><td></td><td></td><td>0.738</td><td></td></tr><tr><td>QS4: I prefer to use data rather than practical experience to make decisions.</td><td></td><td></td><td>0.710</td><td></td></tr><tr><td>Self-control (SC):</td><td>0.538</td><td>0.822</td><td></td><td>0.823</td></tr><tr><td>SC1: I have a hard time breaking a bad habit (reversely coded).</td><td></td><td></td><td>0.736</td><td></td></tr><tr><td>SC2: I am lazy (reversely coded).</td><td></td><td></td><td>0.763</td><td></td></tr><tr><td>SC3: People would say that I have iron self-discipline.</td><td></td><td></td><td>0.717</td><td></td></tr><tr><td>SC4: I can work effectively toward long-term goals.</td><td></td><td></td><td>0.716</td><td></td></tr></table>

## Measurement Reliability Analysis and Validity Analysis

Before further analysis, reliability analysis was performed by Cronbach’s alpha and composite reliability (CR) to the quantified self and self-control. Cronbach’s alpha, as a coefficient of internal consistency, was utilized to assess the reliability of scales. The internal consistency was further examined by CR to test the stability of the individual measurement items. Cronbach's alpha and CR all well exceeded the recommended value level of 0.8 (Cronbach, 1951; Gefen et al., 2003), which revealed adequate reliability of the factors (see Table B3).

Construct validity includes convergent validity and discriminate validity (Straub, 1989). We tested convergent validity by average variance extracted (AVE). The AVEs were all well above the recommended value level of 0.50 (see Table B3). Furthermore, convergent validity was also demonstrated by factor loading of the measurement items (Preacher & Hayes, 2004). Almost all of the factor loadings (FL) exceeded 0.70 (see Table B 3), which suggested adequate convergent validity.

Discriminant validity of this model was determined by calculating the heterotrait–monotrait (HTMT) ratio of correlations and the square root of AVE. The HTMT ratio of correlations introduced by Henseler et al. (2015) is a convenient and reliable discriminant validity test method. After calculation, the HTMT value between QS and $\mathbf { S C } = 0 . 4 2 2 ( < 0 . 8 5 )$ which is favorable (see Table B4). In general, discriminant validity is satisfactory when AVE from the construct is greater than the variance shared between the construct and other constructs. The square root of AVE on the diagonal was greater than correlations among constructs (see Table B5). For further discriminant validity, the exploratory factor analysis was performed (see Table B6). Factor loadings using varimax rotation exceeded the cut-off point of 0.6 (Sangle & Awasthi, 2011).

Table B4. The Correlation Coefficient between Items and the HTMT Ratio of Correlations

<table><tr><td></td><td>QS2</td><td>QS4</td><td>QS5</td><td>QS6</td><td>SC2</td><td>SC3</td><td>SC5</td><td>SC6</td></tr><tr><td>QS2</td><td>—</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>QS4</td><td>0.622</td><td>—</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>QS5</td><td>0.494</td><td>0.605</td><td>—</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>QS6</td><td>0.503</td><td>0.581</td><td>0.574</td><td>—</td><td></td><td></td><td></td><td></td></tr><tr><td>SC2</td><td>0.217</td><td>0.314</td><td>0.184</td><td>0.152</td><td>—</td><td></td><td></td><td></td></tr><tr><td>SC3</td><td>0.244</td><td>0.265</td><td>0.182</td><td>0.141</td><td>0.576</td><td>—</td><td></td><td></td></tr><tr><td>SC5</td><td>0.323</td><td>0.370</td><td>0.312</td><td>0.245</td><td>0.498</td><td>0.538</td><td>—</td><td></td></tr><tr><td>SC6</td><td>0.274</td><td>0.225</td><td>0.143</td><td>0.123</td><td>0.532</td><td>0.544</td><td>0.536</td><td>—</td></tr><tr><td>HTMT</td><td>0.422</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Table B5. Discriminant Validity and Correlations of Construct

<table><tr><td></td><td>QS</td><td>SC</td><td>OIB</td></tr><tr><td>QS</td><td>0.752</td><td></td><td></td></tr><tr><td>SC</td><td>0.429**</td><td>0.736</td><td></td></tr><tr><td>OIB</td><td>-0.473**</td><td>-0.380**</td><td>1</td></tr><tr><td>AVE</td><td>0.566</td><td>0.538</td><td>1</td></tr><tr><td colspan="4">Note: **p &lt; 0.01. Diagonal elements (in bold) are the square root of the average variance extracted (AVE). Off-diagonal elements are the</td></tr></table>

Note: \*\*p < 0.01. Diagonal elements (in bold) are the square root of the average variance extracted (AVE). Off-diagonal elements are the correlations among latent variables.

Table B6. Rotated Component Matrix

<table><tr><td>Component emerged</td><td>QS</td><td>SC</td><td>OIB</td></tr><tr><td>QS2</td><td>0.725</td><td></td><td></td></tr><tr><td>QS4</td><td>0.830</td><td></td><td></td></tr><tr><td>QS5</td><td>0.797</td><td></td><td></td></tr><tr><td>QS6</td><td>0.829</td><td></td><td></td></tr><tr><td>SC2</td><td></td><td>0.776</td><td></td></tr><tr><td>SC3</td><td></td><td>0.800</td><td></td></tr><tr><td>SC5</td><td></td><td>0.759</td><td></td></tr><tr><td>SC6</td><td></td><td>0.821</td><td></td></tr><tr><td>OIB</td><td></td><td></td><td>-0.912</td></tr></table>

## Hypotheses Testing

First, we used partial least squares structural equation modeling (PLS-SEM) to verify H1-H3 because it can offer solutions with small sample sizes (Hair et al., 2017). Compared with CB-SEM, PLS-SEM is not based on covariances and much less relies on the concept of model fit, and thus does not have a fit measure (Hair et al., 2019). Figure B1 summarizes the results of H1-H3 testing and gives the fully normalized path coefficients and their significance levels. Specific analysis shows that: (1) There is a significant negative correlation between OIB and the quantified self (?? = −0.320, ?? < 0.01, H1 supported). (2) There is a significant negative correlation between OIB and self-control (?? = −0.218, ?? < 0.01, H2 supported). (3) There is a significant positive correlation between the quantified self and selfcontrol $( a = 0 . 3 5 0 , \ p < 0 . 0 1$ , H3 supported). Among the three control variables, only education background has a significant effect on OIB.

Second, the mediation effect is further analyzed (see Table B8). The mediation model was estimated using SPSS and AMOS 21. Bootstrapping based on 5000 bootstrap samples was used to handle the non-normality of the data (Preacher & Hayes, 2004). The indirect effects of the quantified self on OIB through the mediation of self-control were assessed. Bootstrapping was used to calculate the significance of the indirect effects. The standardized total effect of the quantified self on OIB was -0.613 (p<0.01). The standardized indirect effect of the quantified self on OIB was -0.494 (p < 0.01). The standardized indirect effect of the quantified self on OIB through the mediation of self-control was - 0.120 (p < 0.01). It shows that self-control plays a mediation effect between quantified self and OIB (H4 supported). It indicates that self-control plays a partial mediation effect between the quantified self and OIB.

![](/api/attachments/2DPA3VR6/fulltext/images/722a16d59f7c3f0086175c3ccf6bd756219505f033d06861f5cc04466e2c56bb.jpg)  
Note. \*\*p < 0.01.

Figure 1. Results of Testing H1-3.  
Table B8. Summary of Results

<table><tr><td></td><td>Effect</td><td>BootSE</td><td>95% CI</td><td>Mediation proportion</td></tr><tr><td>Total effect</td><td>-0.613**</td><td>0.103</td><td>-0.816 ~ -0.411</td><td></td></tr><tr><td>Direct effect</td><td>-0.494**</td><td>0.107</td><td>-0.704 ~ -0.283</td><td>80.492%</td></tr><tr><td>Indirect effect via SC</td><td>-0.120**</td><td>0.028</td><td>-0.138 ~ -0.024</td><td>19.508%</td></tr><tr><td colspan="5">Note. **p&lt; 0.01</td></tr></table>

## About the Authors

Xiaochao Wei received a PhD degree in management science and engineering from the Huazhong University of Science and Technology in 2013. He is currently a professor of economics at the Wuhan University of Technology. He has published research papers in leading journals including Information Sciences, Journal of Artificial Societies and Social Simulation, Expert Systems with Applications, Scientific Programming. His research interest includes management information systems simulation.

Yanfei Zhang received an ME degree in applied economics from the Wuhan University of Technology in 2021, where she is currently pursuing a PhD degree in applied economics. Her research interests include consumer behavior and multi-agent simulation.

Xin (Robert) Luo is a special assistant to the dean for Research Advancement, an Endowed Dean’s Professor of Research Excellence, and a full professor of MIS at the Anderson School of Management of the University of New Mexico, USA. He received his PhD in MIS from Mississippi State University, USA. He has published in leading journals, including the Information Systems Research, Journal of Operations Management, Production and Operations Management, Journal of Management Information Systems, Journal of the Association for Information Systems, European Journal of Information Systems, Information Systems Journal, Journal of Strategic Information Systems, Journal of Information Technology, Decision Sciences, Decision Support Systems, and Information & Management. He has served as an ad hoc associate editor for MIS Quarterly and as an associate editor for the European Journal of Information Systems. He currently serves as an associate editor for the Journal of the Association for Information Systems, Decision Sciences, Decision Support Systems, Information & Management. He sits on the Editorial Review Board of Information Systems Research. He is the co-editor-in-chief of the International Journal of Accounting and Information Management.

Gangmei Pan received an ME degree in applied economics from the Wuhan University of Technology, in 2022. Her research interests include game theory and multi-agent simulation.

Guihua Nie received a PhD degree in management science and engineering from the Huazhong University of Science and Technology, in 1999. He is currently a professor of economics at the Wuhan University of Technology. His research interests include business intelligence, human resource management, information resource management, knowledge management, and knowledge engineering.
