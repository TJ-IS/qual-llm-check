---
otero_id: 6168
otero_key: "W2FNUPAB"
title: "A Robust Inference Method for Decision-Making in Networks"
authors: "Aaron Schecter; Omid Nohadani; Noshir Contractor"
year: "2022"
journal: "MIS Quarterly"
doi: "10.25300/misq/2022/15992"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A ROBUST INFERENCE METHOD FOR DECISION-MAKING IN NETWORKS<sup>1</sup>

Aaron Schecter University of Georgia, Athens, GA, U.S.A. {aschecter@uga.edu}

Omid Nohadani Benefits Science Technology, Boston, MA, U.S.A. {onohadani@gmail.com}

Noshir Contractor Northwestern University, Evanston, IL, U.S.A. {nosh@northwestern.edu}

Social network data collected from digital sources is increasingly being used to gain insights into human behavior. However, while these observable networks constitute an empirical ground truth, the individuals within the network can perceive the network’s structure differently—and they often act on these perceptions. As such, we argue that there is a distinct gap between the data used to model behaviors in a network, and the data internalized by people when they actually engage in behaviors. We find that statistical analyses of observable network structure do not consistently take these discrepancies into account, and this omission may lead to inaccurate inferences about hypothesized network mechanisms. To remedy this issue, we apply techniques of robust optimization to statistical models for social network analysis. Using robust maximum likelihood, we derive an estimation technique that immunizes inference to errors such as false positives and false negatives, without knowing a priori the source or realized magnitude of the error. We demonstrate the efficacy of our methodology on real social network datasets and simulated data. Our contributions extend beyond the social network context, as perception gaps may exist in many other economic contexts.

Keywords: Robust optimization, social network analysis, maximum likelihood estimation, network cognition, inferential models, online networks

## Introduction

Social network analysis is an increasingly popular tool for studying behavior that is grounded upon the investigation of diverse relationships between various social entities (Monge & Contractor, 2003; Wasserman & Faust, 1994). Social network data, like most behavioral data, has traditionally been obtained through surveys or indirect observation of people’s choices. The empirical analysis of organizational phenomena such as social networks has become increasingly viable thanks in part to the proliferation of online data in all facets of life (Kane et al., 2014; Lazer et al., 2009; Lazer et al., 2020; Leonardi & Contractor, 2018). For each of the activities in which we engage online, electronic footprints or “digital traces” are created. Digital records include email exchanges, links between people’s social network sites like Facebook or Twitter, posts to online forums such as Reddit and GitHub, clickstream data, electronic transactions, and mobile app usage.

There are numerous examples in the IS field in which these digital traces are leveraged to examine human behavior and decision-making. In a study of content producers on social networking sites, Bhattacharya et al. (2019) found that individuals tend to form connections with others who produce similar content, but over time alter their posting behavior to be distinct from their contacts. Here, the authors leverage the friendship relations between users of the platform. Social networks have also been used to study software development and innovation. For instance, Singh et al. (2011) predicted the success of open source projects as a function of their internal and external ties. In this study, network ties are formed between individuals who edit the same projects. Finally, several studies have explored the role of social networks in the adoption of new technologies (Aral & Walker, 2014; de Matos et al., 2014) and the spread of user preferences (Dewan et al., 2017; Susarla et al., 2011). Underpinning each of these studies is a reliance on observable digital trace data to infer some type of relationship, such as friendship or knowledge sharing. These inferred relationships are then leveraged to understand how people behave, what their preferences are, or what expertise they contribute.

However, there is a caveat to the use of observational data, particularly those collected from online networks. Social science research has long been aware that in some cases, the “ground truth” is not the data observable by researchers, but the world as it is perceived by the actors themselves (Richards, 1985). Many social and psychological theories of human behavior are based on individuals’ perceptions—an assertion well captured by the observation that “if men [sic] define situations as real, they are real in their consequences” (Thomas & Thomas, 1928, p. 572). Inspired by the work of Thomas and Thomas (1928), network scholars such as Pattison (1994) and Krackhardt (1987, p. 128) observed that network “perceptions are real in their consequences even if they do not map one-toone onto observed behaviors.”

Following this logic, we distinguish between two distinct realities. The first, an individual belief, is one that a specific actor perceives. The individual belief system is composed of all entities, states, or events that the person believes exist. In the social network literature, the collection of individuals’ perceived networks is referred to as a cognitive social structure (Krackhardt, 1987). The second is an empirical instantiation that a third party such as a researcher witnesses or a computer server logs. Empirical instantiations are built from observed records such as digital trace data, with each data point representing actual events. While this “view from above” is reality for those studying the social system, there is no guarantee that the individual beliefs and empirical instantiations are the same. Yet, much of recent empirical research using digital trace data assumes, incorrectly, that these data are equivalent to individuals’ perceptions, and in particular their perceptions of the network. Accordingly, there is a definitive gap—what we call a perception gap— between the individual beliefs and the empirical instantiations. In network parlance, the perception gap manifests in a discrepancy between the collection of individual networks or CSS and the empirical network collected by researchers (Corman, 1990).

This perception gap is a particularly salient problem when conducting behavioral inference, a key focus of network research. As Brashears and Quintane (2015) argue, “[b]ecause individual, preference-driven decisions will be based not on the actual state of the network, but on the perceived state of the network, the manner in which social networks are encoded and represented in memory can have a profound impact on the ultimate structure of a network and the behavior of network members” (p. 113). Thus, when the network changes or when individuals take advantage of their network, either by activating it or mobilizing it (Smith et al., 2011, 2020), the rationale for such actions is derived from an individual’s goals, preferences, and their perspective on the network’s current state (Corman & Scott, 1994; Kilduff & Brass, 2010). This view contrasts with the assumption that the empirical network data is unequivocally ground truth when it comes to explaining individuals’ behaviors based on their perceptions of the network. More generally, individuals often take actions in any context based upon what they believe, not purely the empirical instantiations that researchers observe.

Our key research goal is to address the theoretical and methodological issues stemming from this perception gap. Thus, we ask: To what extent are inferences based on models that assume individuals have perfect knowledge of others network ties robust to the vagaries of individuals’ accurate perceptions of these ties? In addition, if they are not, can we develop robust inference techniques that have the capacity to identify variables that are statistically significant, even with contaminated data, while at the same time ruling out variables that might appear significant with the observed data but become nonsignificant under plausible assumptions of the observed data being contaminated? In this paper, we make three contributions.

1. First, we identify a problem in the way that social networks constructed from digital traces are analyzed, leading to a perception gap. We then formally model this perception gap and consider its impact on inference.

2. Second, we propose a method that remedies this issue by immunizing parameters from data errors. We present a novel extension of recent work on robust maximum likelihood estimation that applies to the exponential family of probability distributions.

3. Third, we derive a robust test statistic and demonstrate the potential for stronger statistical inference.

This paper is organized as follows. We first review studies that make use of digital network data and discuss their assumptions concerning perception. Further, we propose several relevant sources of discrepancy between these networks. Next, we discuss the potential impact these errors have on statistical inference. Finally, we propose a robust reformulation of inferential network models to address these various sources of error. To test our method we conduct three studies: a simulation study, a laboratory example, and an empirical example.

## Background & Motivation

## Interaction Data and Social Networks

Traditionally, empirical instantiations of networks were captured through individuals’ self-report of their interactions (Corman & Scott, 1994; Krackhardt, 1987). Network ties were in essence a measure of how frequently two individuals reported communicating with one another. Increasingly, interactions between two actors are captured through digital traces, rather than self-reports or direct observation. The broad availability of digital trace data has helped drive the growth of social network analysis within the IS field (Agarwal et al., 2008; Cao et al., 2015; Oinas-Kukkonen et al., 2010). We define digital trace data as electronic records of interactions captured by an information system (Berente et al., 2019; Contractor, 2018; Lazer et al., 2009). These data come in a variety of forms: clickstreams, messaging logs, forum posts, and software contributions are all records that information systems capture and store. Like other forms of observable interactions, digital traces can be converted into pairwise relations that connect two participants. Email messages can be treated as directed links from the sender to the recipient (e.g., Quintane & Carnabuci, 2016). Relations on social media sites such as “following” someone, “commenting” on a post, or “liking” a message provide data on who is engaging with whom (Kane et al., 2014). Online message forums can also be transformed into social networks by finding “who replies to whom” in a thread (Faraj & Johnson, 2011; Johnson et al., 2014).

The advantage of interaction data as compared to traditional sociometric survey data is that links between individuals represent actual connections and generally correspond to actions taken by people. Additionally, interaction data— particularly those that are digital—are cheaper to collect than surveys, are dynamically updateable, and do not suffer from a lack of responses or missing participants. Accordingly, much larger and more complex networks can be modeled and analyzed using online data (Lazer et al., 2009). More recently, there have been calls to use digital trace data generated in organizations to help HR leverage people analytics—to help identify influences, innovators, those likely to quit and those likely to work well on a team (Leonardi & Contractor, 2018).

Consequently, more IS research has leveraged digital traces to understand different aspects of human behavior (Berger et al., 2014; Howison et al., 2011). To demonstrate the pervasiveness of online network data in management studies, we conducted a survey of recent literature relevant to our study and summarize these observations in Table 1. However, relying solely upon digital trace data—or any interaction data for that matter—to conduct inference may lead to validity concerns (Howison et al., 2011; Vial, 2019). Namely, digital engagement or interactions do not necessarily signify a social relationship in the same way that a survey or interview might (Corman, 1990). For instance, the relation “friendship” could be determined by asking individuals who they consider to be their friends. With event data, one can only observe online engagements such as “liking” or “tagging” on platforms such as Facebook or YouTube.

Consequently, the network constructed from trace data is, at best, a proxy for the underlying pattern of social relations. Why is this problematic? As Howison et al. (2011) point out, digital traces are events and thus represent instances of a relation. They alone do not make a social tie. However, “when working with trace data, it seems there is a tendency to take evidence of instances (what was) and transmute that uncritically into evidence of topology (what could be/have been)” (Howison et al., 2011, p. 790). Accordingly, network measures constructed from any form of event data are prone to misalignment between the measurement and the underlying construct, even at the aggregate (i.e., population) level. Because of this misalignment, there is a gap between the observable network—constructed vis-à-vis digital trace data—and the relations as they are perceived by the individuals in the network. As a result, conducting inference on the observable network will not accurately capture certain patterns of social interaction such as trust, friendship, or leadership (Brashears & Quintane, 2015; Kilduff & Brass, 2010). However, despite the potential limitations of online social network data reflecting perceptions, these forms of data are frequently used to test hypotheses about human attitudes and behavior. In the following section, we describe a variety of potential causes—both technical and cognitive—for this perception gap.

## Perception Errors in Social Networks

## Prevalence of Perception Errors

Extant empirical research, while somewhat limited, has consistently shown that individuals’ beliefs do not align with empirical reality. Studies comparing email logs (Johnson et al., 2012; Quintane & Kleinbaum, 2011; Wuchty & Uzzi, 2011) show positive correlations between message exchanges and selfreported ties, but there are significant misalignments. In Johnson et al.’s (2012) study of email exchanges in a bank, for example, the authors found correlations of 0.20 to 0.30 between email links and self-reported friendship, advice, and information ties. Wuchty and Uzzi (2011) similarly studied email logs and selfreported networks in a professional services organization. Their model attempted to predict self-reported ties from email exchanges; their optimally-tuned models achieved a true positive rate of at most 83.6% and a false-positive rate of at minimum 12.2%. In other words, even the best models still incorrectly predicted the presence (or lack thereof) of a tie more than 12% of the time.

<table><tr><td colspan="3">Table 1. Summary of Digital Network Studies</td></tr><tr><td>Data source</td><td>Research topics</td><td>Exemplar studies</td></tr><tr><td>Social networks, messaging, and emails</td><td>Peer-to-peer influenceInformation diffusionProduct virality</td><td>Aral and Van Alstyne (2011)Aral and Walker (2012)Aral and Walker (2014)Bampo et al. (2008)Bapna and Umyarov (2015)Bapna et al. (2017a)Bapna et al. (2017b)Dewan et al. (2017)de Matos et al. (2014)Quintane and Carnabuci (2016)Susarla et al. (2011)</td></tr><tr><td>Software project affiliation</td><td>Developer learningDeveloper collaborationProblem solvingCore-periphery emergence</td><td>Brunswicker and Schecter (2019)Dahlander and O&#x27;Mahony (2010)Foss et al. (2016)Quintane et al. (2014)Singh and Phelps (2013)Singh and Tan (2010)Singh et al. (2011)</td></tr><tr><td>Online forums and communities</td><td>Patterns of contributionEmergence of structureEmergence of leadershipParticipant collaborationKnowledge sharing</td><td>Chen et al. (2017)Dahlander and Frederiksen (2011)Faraj and Johnson (2011)Johnson et al. (2014)Johnson et al. (2015)Kudaravalli and Faraj (2008)Lu et al. (2017)Bhattacharya et al. (2019)</td></tr></table>

Using Facebook interaction data, Gilbert and Karahalios (2009) built a predictive model to identify strong and weak friendship ties, as self-reported by participants in their sample. Their model was able to predict tie strength with a mean absolute error of approximately 10%. Other studies have used mobile phone proximity data (Eagle et al., 2009) and mobile phone call records (Onnela et al., 2007) to reconstruct networks and compare them to self-reported ties. Eagle et al. (2009) found that even among friends, there was only a correlation of 0.412 between mobile proximity records and reported proximity. Further, the authors found a strong effect of recency and determined that after approximately one week, recollection of interactions significantly degraded. Finally, Brashears and Quintane (2015) conducted an experiment to determine how well individuals are able to recall their communication interaction patterns in surveys. Using ERGMs, the authors found that participants were able to identify clusters of ties but were unable to identify individual links with any regularity. Collectively, these studies lend credence to the notion of the perception gap in networks across a variety of mediums.

Thus, while these reconstructed networks based on trace data correlate with the underlying perceived social networks—as reported by the participants—they are, at best, approximations. Given that these errors are present in empirical settings, we now review the literature on why these errors might arise.

## Errors Inherent to Online Networks

We argue that in an online environment, individuals’ ability to infer the network of interactions is difficult for three reasons: scale, rate of change, and the potentially translucent nature of online networks. First, a key feature of networks generated from digital trace data is their scale. Studies of networks in online communities often encompass thousands of messages among hundreds of actors (see for example Faraj & Johnson, 2011; Johnson et al., 2014) and can, conceivably in the future, be conducted on billions of messages among billions of actors. On social media platforms, actors are able to create a large number of ties, even though the number of connections may far exceed a person’s capacity to manage them (Kane et al., 2014), causing a sense of overload (Mariotti & Delbridge, 2012). Indeed, natural limitations on peoples’ time and cognitive capacity dictate that some of the thousands of links they form become forgotten or overlooked, causing these relationships to become “latent” (Mariotti & Delbridge, 2012)

or “dormant” (Levin et al., 2011; Walter et al., 2015). The variability in the scale contributes to potential sources of errors in online networks.

A second feature of online network data that affects perception is the rate at which these networks evolve. Digital network data are often collected over a period of months or even years (e.g., Zaheer & Soda, 2009). Links represent the presence of interactions during some portion of the observed interval. Some interactions may be long and recur frequently during a time period, while others may be short, intense periods of interaction. Clickstream data—such as forum posts or edits to an online repository—tend to be “bursty,” i.e., characterized by periods of high activity followed by lulls (Barabasi, 2010; Vu et al., 2015). The variability in the rate of messaging contributes to potential sources of errors in online social networks.

Finally, online social networks vary greatly in the technological affordances that users can enact. One such affordance is the degree of visibility, or the amount of effort individuals must expend to assess the state of the network (Treem & Leonardi, 2013). Further, digital networks vary on a second technological affordance, association, or the ability to determine which individuals and or content are related (Treem & Leonardi, 2013). For instance, social media networks such as Facebook allow users to see “who is friends with whom.” However, while individuals can view this information, they may vary greatly in how they use it, or if they use it at all (Kane et al., 2014). This variability in individuals’ perceptions contributes to potential sources of error in online social networks.

## Errors of Cognition

In addition to the technological sources discussed, there are cognitive sources that contribute to discrepancies between observed networks and individuals’ perceptions of these networks, whether the data are digital or not. Early studies on informant accuracy and recall focused on the ability of individuals to correctly report with whom they had interacted or what they had witnessed (Bernard et al., 1982; Freeman et al., 1987; Heald et al., 1998). In general, individuals had a difficult time recalling their own interactions, as well as observed interactions among others. Recollection can be biased by recency or regularity (Freeman, 1992), or can be triggered by engagement in a specific foci (Corman & Scott, 1994).

Further, individuals tend to view themselves as being more central, and perceive that there are more ties, more reciprocation, and more transitivity among those they report as friends (Krackhardt & Kilduff, 1999). Humans also demonstrate a tendency for remembering clusters of relations but perform poorly when asked to recall specific relationships (Brashears & Quintane, 2015). A consistent finding among these studies is the tendency towards simplicity (Burt et al., 2013) and a rejection of structures that are dissonant with the mental models of the individual. Alternatively, a person’s ability to accurately comprehend the structure around them may be impacted by their personality and affective state such as feelings of low power (Casciaro, 1998; Casciaro et al., 1999, 2014) or even their gender (Brashears et al., 2016). Personality traits such as a need for closure (Flynn et al., 2010) can bias individuals toward making errors in their perceptions of networks. Janicik and Larrick (2005) demonstrated that individuals who can effectively recall missing links are more accurate in comprehending incomplete network structures and recognizing brokerage opportunities.

## Impact of Errors on Inference

In order to determine how statistical inference is affected by discrepancies in an individual’s perceptions versus observed networks, we consider what types of errors of commission and omission may be caused by the factors previously detailed (Yenigun et al., 2017). The first error occurs when individuals mistakenly perceive ties that do not exist, i.e., an error of omission. Alternatively, individuals may make the error of ignoring ties that do indeed exist, i.e., an error of commission. Both errors can cause biased inference results. We proceed to compare these issues to the notion of measurement errors in econometrics.

## Perception Errors versus Measurement Errors

In econometric models, an inaccurate operationalization of a construct would result in a type of measurement error, or variance not accounted for by the statistics included in the model (Wooldridge, 2009). There are two types of measurement error models: the classical error model and the non-classical error model. The classical error model—or classical errors—assumes the measurement error to be additive and independent of the true measure and the residuals in the second stage estimation, whereas the non-classical model considers the measurement error to be non-additive or correlated with the true measure or residuals (Carroll et al., 2006). By this definition, errors in social networks are nonclassical for three reasons.<sup>2</sup> First, the errors can be asymmetric, i.e., they are not evenly distributed around zero because of consistent over- or underestimation. Second, the magnitude of the errors may depend on the value of the statistic. Finally, the prevalence and magnitude of errors can differ significantly across individuals.

Measurement errors compromise regression models by attenuating or amplifying the influence of the corresponding coefficient (Yang et al., 2018). Further, measurement errors can create bias in both the coefficient of the erroneous measurement and the other coefficients (Greene, 2003). To account for these misspecifications, correction techniques such as method-of-moments estimation (Carroll et al., 2006), instrumental variables (Carroll & Stefanski, 1994), or simulation extrapolation (Yang et al., 2018) can be applied. However, there are certain limitations to these techniques that are relevant when analyzing social network data. Many existing correction techniques such as method-of-moments or simulation extrapolation require measurement error variance to be known a priori and assume that the error variance is constant across the sample. With social networks, the error variance is a product of latent human perceptions that can only be captured through sociometric surveys. Implementing such a survey is typically infeasible for networks of even moderate size and surveying a subset of the network may not be representative of the true variance.

Conducting inference on social network data faces a variety of challenges. Coefficients may be attenuated when the error variance is large (Wooldridge, 2009). Alternatively, systematic perception biases could amplify coefficients in one direction or the other (Carroll & Stefanski, 1994; Yang et al., 2018). Because the magnitude and direction of perception errors can be difficult to identify, existing correction techniques are ill-suited to fix these issues. Of course, the degree to which measurement errors affect social network models is not known, particularly for techniques such as exponential random graph modeling (Lusher et al., 2012) which operates at the aggregate network level.

## Illustration: Krackhardt’s Office Managers

To demonstrate the potential influence of perception errors, we analyze a classic network dataset taken from Krackhardt’s (1987) study of CSS data collected from managers in a small manufacturing firm. Although they are not constructed through digital traces, these networks provide an empirical reality (the self-reported network) as well as a set of individually perceived networks for comparison. In these data, a sociometric survey was conducted for each of 21 employees, and each was asked to report their perceptions of the friendship among all 21 managers. For our purposes, we use the symmetric, binary friendship networks. These networks are the CSSs for each manager and represent the raw observable data which we notate as $\bar { Y } ^ { ( i ) } , i = 1 , \ldots , 2 1$ Following Krackhardt (1987), we compute the locally aggregated structure (LAS) from these CSSs, which we notate as $\overset { \sim } { Y ^ { \mathrm { L A S } } }$ . We apply the intersection rule, whereby $Y _ { i j } ^ { \mathrm { L A S } } = 1$ only if $Y _ { i j } ^ { ( i ) } = 1$ and $Y _ { i j } ^ { ( j ) } = 1$ (Batchelder et al., 1997). The LAS graph can be thought of as the “true” self-reported data for our analysis. Our aggregate network ??<sup>LAS</sup> has 35 edges— a density of 0.1667—and 12 total triangles. For each of the 21 managers, we counted the number of edges and the number of triangles reported, their accuracy compared to the “true” network by counting the number of false positives and false negatives as well as computing the Jaccard index as a measure of similarity. The results are presented in Table 2.

Relative to the aggregated “true” self-reported network, most managers make errors perceiving the network. False positives range from 0 to 78 with a median of 22, while false negatives range from 18 to 62 with a median of 44. The Jaccard index, which assesses overall agreement between two networks, ranges from 0.10 to 0.45 with a mean of 0.27. To place these numbers in context, the most accurate managers in the sample were still wrong about the state of a tie more often than they were correct. Interestingly, there is a strong and negative correlation between the errors $( \rho =$ −0.84). This observation indicates that people tend to systematically over- or underestimate the density of the overall network. This would correspond to systematically making more errors of commission or omission, respectively. We also find that most actors overestimate the number of triangles.

We demonstrate the impact of the bias in the data by running a series of ERGMs on the CSS as well as the aggregate data using the approach described by Hunter et al. (2008). We include two statistics in our model, edges and directed dyadwise shared partners. This statistic accounts for the prevalence of “two paths” in the network, i.e., a path from A to B is more likely if there is a path from A to C and C to B. We present the results in Figure 1. For the aggregate model, the coefficient for edges was -1.304 with a standard error of 0.096 $( p < 0 . 0 0 1 )$ . The dyadwise shared partner statistic had a coefficient of -0.186 with a standard error of 0.069 $( p <$ 0.01). For 17 out of 21 managers, the aggregated model significantly overestimated the edge statistic. The average raw bias $\left( \bar { \beta } _ { L A S } - \hat { \beta } _ { i } \right)$ in the coefficient was 1.05, which is equivalent to an 80.9% overestimation of the individual values. The shared partner statistic had mixed results; for 12 managers, the aggregate model underestimated the statistic, and in nine cases, the model overestimated the statistic. The overall raw bias for the coefficient was -0.176, which is equal to a 94.3%underestimation of the individual values.

Table 2. Descriptive Statistics and Error Rates for Krackhardt CSS Data

<table><tr><td>Manager</td><td>Edges</td><td>Triangles</td><td>False positives</td><td>False negatives</td><td>Jaccard index</td></tr><tr><td>1</td><td>36</td><td>22</td><td>40</td><td>38</td><td>0.29</td></tr><tr><td>2</td><td>14</td><td>1</td><td>6</td><td>48</td><td>0.29</td></tr><tr><td>3</td><td>5</td><td>1</td><td>2</td><td>62</td><td>0.11</td></tr><tr><td>4</td><td>25</td><td>10</td><td>22</td><td>42</td><td>0.30</td></tr><tr><td>5</td><td>49</td><td>48</td><td>46</td><td>18</td><td>0.45</td></tr><tr><td>6</td><td>20</td><td>7</td><td>16</td><td>46</td><td>0.28</td></tr><tr><td>7</td><td>61</td><td>80</td><td>78</td><td>26</td><td>0.30</td></tr><tr><td>8</td><td>4</td><td>0</td><td>0</td><td>62</td><td>0.11</td></tr><tr><td>9</td><td>4</td><td>0</td><td>0</td><td>62</td><td>0.11</td></tr><tr><td>10</td><td>28</td><td>12</td><td>32</td><td>46</td><td>0.24</td></tr><tr><td>11</td><td>49</td><td>39</td><td>56</td><td>28</td><td>0.33</td></tr><tr><td>12</td><td>18</td><td>4</td><td>10</td><td>44</td><td>0.33</td></tr><tr><td>13</td><td>25</td><td>2</td><td>24</td><td>44</td><td>0.28</td></tr><tr><td>14</td><td>38</td><td>27</td><td>32</td><td>26</td><td>0.43</td></tr><tr><td>15</td><td>20</td><td>13</td><td>22</td><td>52</td><td>0.20</td></tr><tr><td>16</td><td>20</td><td>4</td><td>18</td><td>48</td><td>0.25</td></tr><tr><td>17</td><td>30</td><td>13</td><td>28</td><td>38</td><td>0.33</td></tr><tr><td>18</td><td>14</td><td>1</td><td>8</td><td>50</td><td>0.26</td></tr><tr><td>19</td><td>51</td><td>45</td><td>52</td><td>20</td><td>0.41</td></tr><tr><td>20</td><td>8</td><td>0</td><td>8</td><td>62</td><td>0.10</td></tr><tr><td>21</td><td>31</td><td>21</td><td>24</td><td>32</td><td>0.40</td></tr></table>

![](/api/attachments/W2FNUPAB/fulltext/images/bb4f11860900e9dd5dd5700a73dcdd0d8ceb11535a901ed61100d4917f4e96ef.jpg)  
(a)

![](/api/attachments/W2FNUPAB/fulltext/images/e609793ae2dd0b25c8a20d7024f4ecd7b50b68072c68bc101d319a333e098257.jpg)  
(b)  
Note: Histograms of ERGM coefficients for (a) edge statistic and (b) shared partner statistic for 21 managers. Red line indicates aggregate estimate.

Figure 1. Parameter Estimates for Krackhardt CSS Data

This illustration demonstrates that errors caused by individual differences in perception can lead to systematic biases in estimates of the model parameters. Further, the bias is not strictly an attenuation or amplification. As such, we were not able to determine a priori how well the results reflect perceived reality. Thus, hypothesis testing using network data was subject to potentially significant errors.

## The Robust Inference Approach

Given that network data are subject to errors of omission as well as errors of commission, it is not appropriate to simply correct for one problem or the other. Rather, network inference methods should be immunized to errors in a general sense, so that a preponderance of bias in either direction can be handled. We therefore advance that a robust approach is the most appropriate; robust optimization methods do not rely on a priori information or any distributional assumptions. Instead, a solution is found that is the best in the worst case, i.e., the discrepancies are as egregious as possible. Thus, the method we proceed to outline is insular to both false-positive and false-negative errors, regardless of their source. We propose a conservative model that uses the observable network data but allows the perceptions of individuals to vary randomly within a pre-specified range. The inferred parameter then holds for any variability within the range, i.e., the parameter is robust to cognitive errors.

## Robust Optimization

Robust optimization broadly refers to the collection of techniques devised for finding optimal solutions to problems in the presence of uncertainties (for an overview, see Ben-Tal et al., 2009; Ben-Tal & Nemirovski, 2002; Bertsimas et al., 2011). For network models, data uncertainty takes the form of individual perceptions of the surrounding network. Specifically, the model assumes that an empirical network accurately reflects each actor’s individual network. However, errors such as those discussed earlier under the categories of errors inherent to online networks and errors of cognition, including perception errors, hidden information, or poor memory, could lead individuals to make choices based on perceptions of the network to which the researcher is not privy. As a result, the estimated parameters from the model from observed data may not accurately reflect the impact of the perceived network structure on decision-making. The elements of a robust optimization problem include nominal or original data (from the empirical network), an uncertainty set, and an objective function.

## Notation and Definitions

Throughout the rest of this paper, we will denote vectors with a lowercase bold letter, and matrices with an uppercase bold letter. We consider an ordered series of ?? social network actions or events, which constitute the addition, removal, or alteration of a tie or node in the network. At each point in time $t = 1 , \ldots , M ,$ , there are a set of these possible actions contained in the set $\mathcal { A } _ { t }$ . We assume that the set is finite with the cardinality $| \mathcal { A } _ { t } | = N _ { t }$ . It is possible that there are varying numbers of available actions at any given time. Let $N = \operatorname* { m a x } _ { \star } N _ { t }$ be the largest number of possible actions.

The network at each point in time can be described by a collection of ?? characteristics, which we refer to as sufficient statistics of the graph. These statistics correspond to some structural element of the social network, i.e., degree of transitivity or number of edges, or some exogenous covariate. Given these dimensions, our network data may be represented as a matrix $\pmb { X } \in \mathbb { R } ^ { M \times N \times P }$ . This matrix represents a series of social network actions at M points in time, each of which can entail as many as N actions and the network at each point in time is represented by P characteristics or sufficient statistics. From this representation, it follows that $x _ { t y p }$ ∈ ℝ is a scalar corresponding to the value of statistic ?? of action ?? at time ??. We may also define a slice of the matrix $\boldsymbol { x } _ { t y \bullet } \in \mathbb { R } ^ { P }$ as a vector of all sufficient statistics for action ?? at time ??.

Now, we assume that our network data is inaccurate because of a lack of coherence between the individual networks and the empirical network. Thus, while we observe $X ^ { \mathrm { n e t } }$ , that may not be the true value perceived by the actor. We thus represent our data as

$$
\boldsymbol {X} ^ {\mathrm{ind}} = \boldsymbol {X} ^ {\mathrm{net}} - \Delta \boldsymbol {X},\tag{1}
$$

where $X ^ { \mathrm { i n d } }$ is the matrix of features perceived by the individuals in the network. We model networks and changes to them as reactions to the underlying individual structure, i.e., the network that individuals perceive. However, we consider here the case where we only have access to an empirical network that is collected through digital trace methods such as email or mobile data. Features derived from this network are represented by $X ^ { \mathrm { n e t } }$ . A consequence of this is an inherent bias in the variables we use to conduct inference. This discrepancy is captured by $\Delta { \boldsymbol { X } } \in \mathbb { R } ^ { M \times N \times P }$ . By modeling bias this way, we allow for the incorporation of internal, external, or data collection errors into our models without making any specific assumptions about their value, sign, or distribution.

We assume that, in general, we have no information about the nature of the errors and instead model them to reside in some bounded uncertainty set. In other words, an error may take on any value within this set. We describe this uncertainty set as

$$
\mathcal {N} = \{\Delta \mathbf {X} | \| \Delta \boldsymbol {x} _ {t z \bullet} \| \leq \rho , z \in \mathcal {A} _ {t}, t = 1, \dots , M \}.\tag{2}
$$

Here and throughout the remainder of the paper, we will use the Euclidian norm. An uncertainty set ?? is a collection of all possible errors that meet a basic criterion. In our case, we restrict the errors for each vector of statistics to be limited in magnitude by a tolerance parameter ??. This value corresponds to a level of discrepancy between our collected data and the true perceived information. A larger ?? will allow for greater deviance from the observed values, while a $\rho = 0$ will imply equality of observable and true data. Essentially, an uncertainty set is the collection of all possible differences between the true and observable data. While we refer to a single parameter $\rho$ for the sake of simplicity, it is possible to have a large number of these values. For instance, each sufficient statistic may be constrained by a unique parameter, or each individual may have an independent error tolerance.

Our definition of the uncertainty set raises two questions: First, how does one interpret the value o $\mathrm { : } \rho \mathrm { : }$ Second, how does one select an appropriate $\rho ?$ To answer these questions, we adopt a probabilistic view of ??. We construct the set such that it contains all errors we believe may occur with a nonnegligible probability. Put another way, errors of magnitude greater than $\rho$ are rare enough that we do not need to immunize our estimates from them. Thus, the value of $\rho$ should represent the threshold at which errors are no longer likely. To actually select a $\rho ,$ the underlying distribution of the data should be considered. Suppose that we knew the errors followed a standard normal distribution and the uncertainty set is modeled with a Euclidean norm. Then, for an ??- dimensional error vector, the tolerance parameter would be given as $\rho = \chi _ { m } ^ { 2 } ( \alpha )$ , i.e., the chi-squared test statistic at confidence level ?? (Bertsimas et al., 2007). It follows that for a single variable modeled with error, $\rho = 1 , 2 , 3$ corresponds to errors falling within one, two, or three standard deviations, respectively. Of course, in practice, we do not always know the distributions of the errors. In those cases, ?? can be estimated from the empirical data using a measure of spread, such as a standard deviation or quantile.

## Computing Robust Estimators

To compute a robust maximum likelihood estimate, we first need to specify a probability density function ?? for the data. Generally speaking, the robust methodology we present will hold for any differentiable density function ??. Traditionally, the probability density function for a social network has been considered part of the exponential family of probability distributions (Holland & Leinhardt, 1977, 1981). The exponential family broadly describes a variety of distributions, including the normal, gamma, Weibull, and multinomial. Common social network inference models such as ERGMs (Robins et al., 2007), stochastic actor-oriented models (Snijders, 1996), and relational event models (Butts, 2008) all employ an exponential probability distribution from this family. Other models including the Cox proportional hazards model (Cox, 1972) and the conditional logit model (McFadden, 1974) use the same specification. However, it is important to note that the method we are proposing is valid for any choice of probability density. Bertsimas and Nohadani (2019) have focused on the multivariate normal distribution, and in this paper, we extend the robust MLEs to the broader exponential family, which is central to social network analysis.

Social network models typically assume an exponential probability distribution parameterized by the vector $\pmb { \beta } \in \mathbb { R } ^ { P }$ Although these models typically use linear combinations of parameters and statistics, any differentiable function is valid for our method. Each element of $\pmb { \beta }$ is interpreted as an intensity parameter that contributes to the likelihood of the observed network. The probability density for a single observation ?? at time ?? is thus:

$$
f _ {t} \big (\pmb {\beta}; \pmb {x} _ {t y \bullet} ^ {\mathrm{ind}}, \mathcal {A} _ {t} \big) = \frac {\exp \big (\pmb {\beta} ^ {\prime} \pmb {x} _ {t y \bullet} ^ {\mathrm{ind}} \big)}{\sum_ {z \in \mathcal {A} _ {t}} \exp \big (\pmb {\beta} ^ {\prime} \pmb {x} _ {t z \bullet} ^ {\mathrm{ind}} \big)}.\tag{3}
$$

Given that we want to make inferences on the values of ?? corresponding to the true network structure, the typical methodology would be to perform a maximum likelihood estimation (MLE), i.e., finding the distribution parameters that maximize the probability density function and hence best fit the data. Inference based on the MLE procedure or derivations of it is a common method for social network analysis (Butts, 2008; Snijders et al., 2010; Stadtfeld, 2012).

In the remainder of this section, we generalize to multiple time slices for longitudinal data, though our method holds true for a single instance such as a traditional ERGM analysis. The likelihood of a sequence of network alterations or events is equivalent to a product of Equation (3) across all observations with the features $X ^ { \mathrm { n e t } }$ reflecting the changing network. We assume the presence of some error in our dataset, i.e., $X ^ { \mathrm { n e t } } \neq$ $X ^ { \mathrm { i n d } }$ , and so we recast the likelihood of the full sequence of network events as:

$$
\begin{array}{r l} & {\prod_ {t = 1} ^ {M} f _ {t} \big (\pmb {\beta}; \pmb {x} _ {t y \bullet} ^ {\mathrm{ind}}, \mathcal {A} _ {t} \big) = \prod_ {t = 1} ^ {M} f _ {t} \big (\pmb {\beta}; \pmb {x} _ {t y \bullet} ^ {\mathrm{net}} - \Delta \pmb {x} _ {t y \bullet}, \mathcal {A} _ {t} \big)} \\ & {\qquad = \prod_ {t = 1} ^ {M} \frac {\exp \left(\pmb {\beta} ^ {\prime} \big (\pmb {x} _ {t y \bullet} ^ {\mathrm{net}} - \Delta \pmb {x} _ {t y \bullet} \big)\right)}{\sum_ {z \in \mathcal {A} _ {t}} \exp \big (\pmb {\beta} ^ {\prime} (\pmb {x} _ {t z \bullet} ^ {\mathrm{net}} - \Delta \pmb {x} _ {t z \bullet}) \big)}.} \end{array}\tag{4}
$$

As discussed by Bertsimas and Nohadani (2019), maximizing the likelihood yields the same solution as maximizing the loglikelihood function, which is computationally more manageable. We define the log-likelihood function $\begin{array} { r } { \psi ( \pmb { \beta } ; \bar { \bf X } ^ { \mathrm { n e t } } - \Delta \mathbf { X } ) = \log \left( \prod _ { t = 1 } ^ { M } f _ { t } \left( \pmb { \beta } ; \pmb { x } _ { t y \bullet } ^ { \mathrm { n e t } } - \Delta \pmb { x } _ { t y \bullet } \mathcal { A } _ { t } \right) \right) } \end{array}$ Now, the maximum likelihood problem becomes the following constrained optimization problem:

$$
\max _ {\boldsymbol {\beta}} \{\psi (\boldsymbol {\beta}; \mathbf {X} ^ {\mathrm{net}} - \Delta \mathbf {X}): \Delta \mathbf {X} \in \mathcal {N} \}.\tag{5}
$$

It follows that the solution to the MLE problem (5) must be a valid solution for any of the errors that may reside within the uncertainty set ??. Consequently, a solution that satisfies this constraint must also fit the log-likelihood function under the worst-case errors. Hence, the robust estimator is also the solution to the following robust optimization problem:

$$
\max _ {\boldsymbol {\beta}} \min _ {\Delta \mathbf {X} \in \mathcal {N}} \psi (\boldsymbol {\beta}; \mathbf {X} ^ {\mathrm{net}} - \Delta \mathbf {X}).\tag{6}
$$

We solve the inner optimization problem (given in Equation 6) by decomposing it into an outer problem – maximization over parameters $\pmb { \beta }$ —and inner problem—minimization over errors Δ??. We focus first on the inner problem, which finds the set of feasible errors that minimize the log-likelihood function. The inner problem is equal to:

$$
\begin{array}{l} \phi (\boldsymbol {\beta}; \mathbf {X} ^ {\mathrm{net}}) = \underset {\Delta \mathbf {X} \in \mathcal {N}} {\min} \psi (\boldsymbol {\beta}; \mathbf {X} ^ {\mathrm{net}} - \Delta \mathbf {X}) \\ \qquad = \underset {\Delta \mathbf {X} \in \mathcal {N}} {\min} \log \left(\prod_ {t = 1} ^ {M} f _ {t} \big (\boldsymbol {\beta}; x _ {t y \bullet} ^ {\mathrm{net}} - \Delta x _ {t y \bullet}, \mathcal {A} _ {t} \big)\right) \\ \qquad = \underset {\| \Delta x _ {t z \bullet} \| \leq \rho} {\min} \sum_ {t = 1} ^ {M} [ \log f _ {t} \big (\boldsymbol {\beta}; x _ {t y \bullet} ^ {\mathrm{net}} - \Delta x _ {t y \bullet}, \mathcal {A} _ {t} \big) ]. \end{array}\tag{7}
$$

In Equation (7) we are summing the logarithm of a probability density function, which guarantees that we are summing numbers less than or equal to zero. Consequently, this problem is separable across time points $t = 1 , \ldots , M .$ . Applying the known density function, the inner problem reduces to solving:

$$
\min _ {\| \Delta x _ {z t} \| \leq \rho} \big (\boldsymbol {\beta} ^ {\prime} \big (\boldsymbol {x} _ {t y \bullet} ^ {\mathrm{net}} - \Delta \boldsymbol {x} _ {t y \bullet} \big) - \log \sum_ {z \in \mathcal {A} _ {t}} \exp \big (\boldsymbol {\beta} ^ {\prime} (\boldsymbol {x} _ {t z \bullet} ^ {\mathrm{net}} - \Delta \boldsymbol {x} _ {t z \bullet}) \big) \big),\tag{8}
$$

for each instance ??. We note that the objective function for each component of the inner optimization problem is decreasing in $\pmb { \beta } ^ { \prime } \Delta \pmb { x } _ { t y } .$ <sub>•</sub> and increasing in $\pmb { \beta } ^ { \prime } \Delta \pmb { x } _ { t z } .$ for all $z \neq y ;$ for proof, see the Appendix. As a result, the optimal value can be found by determining the maximum feasible value of $\pmb { \beta } ^ { \prime } \Delta x _ { t y } .$ <sub>•</sub> and the minimum value of $\pmb { \beta } ^ { \prime } \Delta \pmb { x } _ { t z } .$ for all $z \neq y .$ By applying Hölder’s inequality, we know that

$$
- \| \pmb {\beta} \| \| \Delta x _ {z t} \| \leq \pmb {\beta} ^ {\prime} \Delta x _ {z t} \leq \| \pmb {\beta} \| \| \Delta x _ {z t} \|.\tag{9}
$$

Applying the extreme limits and the known bounds of our uncertainty set, we can solve the inner problem for each event as:

$$
\begin{array}{r l} & {\underset {\| \Delta x _ {z t} \| \leq \rho} {\min} \Bigg (\boldsymbol {\beta} ^ {\prime} (x _ {t y \bullet} ^ {\mathrm{net}} - \Delta x _ {t y \bullet}) - \log \sum_ {z \in \mathcal {A} _ {t}} \exp \big (\boldsymbol {\beta} ^ {\prime} (x _ {t z \bullet} ^ {\mathrm{net}} - \Delta x _ {t z \bullet}) \big) \Bigg)} \\ & {\qquad = \boldsymbol {\beta} ^ {\prime} x _ {t y \bullet} ^ {\mathrm{net}} - \| \boldsymbol {\beta} \| \rho - \log \sum_ {z \in \mathcal {A} _ {t}} \exp (\boldsymbol {\beta} ^ {\prime} x _ {t z \bullet} ^ {\mathrm{net}} + (- 1) ^ {u _ {z}} \| \boldsymbol {\beta} \| \rho).} \end{array}\tag{10}
$$

Here we define $u _ { z }$ as an indicator variable that is equal to 1 if $z = y _ { t }$ and 0 otherwise. The specific solution for $\Delta x _ { t z } .$ is given by $\begin{array} { r } { \Delta x _ { t z \bullet } ^ { \star } ( \beta ) = ( - 1 ) ^ { 1 - u _ { z } } \rho \frac { \beta } { \| \beta \| } \times 1 \{ \beta \neq 0 \} } \end{array}$ . Thus, we combine all our elements into a single solution for the inner problem:

$$
\begin{array}{l} \phi (\boldsymbol {\beta}; \boldsymbol {X} ^ {o b s}) = \\ \sum_ {t = 1} ^ {M} \Bigg (\boldsymbol {\beta} ^ {\prime} \boldsymbol {x} _ {t y \bullet} ^ {\mathrm{net}} - \| \boldsymbol {\beta} \| \rho - \log \sum_ {z \in \mathcal {A} _ {t}} \exp (\boldsymbol {\beta} ^ {\prime} \boldsymbol {x} _ {t z \bullet} ^ {\mathrm{net}} + (- 1) ^ {u _ {z}} \| \boldsymbol {\beta} \| \rho) \Bigg). \end{array}\tag{11}
$$

We can now solve the robust outer MLE problem, $\operatorname* { m a x } _ { \beta } \phi ( \beta ; X ^ { \mathrm { n e t } } )$

$$
\max _ {\boldsymbol {\beta}} \sum_ {t = 1} ^ {M} \left(\boldsymbol {\beta} ^ {\prime} x _ {t y \bullet} ^ {\mathrm{net}} - \| \boldsymbol {\beta} \| \rho - \log \sum_ {z \in \mathcal {A} _ {t}} \exp (\boldsymbol {\beta} ^ {\prime} x _ {t z \bullet} ^ {\mathrm{net}} + (- 1) ^ {u _ {z}} \| \boldsymbol {\beta} \| \rho)\right)\tag{12}
$$

directly using a subgradient method. The subgradient is required because the gradient does not exist at the point $\pmb { \beta } =$ ??. For a derivation of the gradient, see the Appendix.

## Computing Standard Errors

In order to conduct hypothesis testing with the robust estimators, we need to calculate the standard errors of the estimates. Because we are conducting maximum likelihood estimation, we can approximate standard errors using the Fisher information matrix. The Fisher information ℐ is defined as ${ \mathcal { I } } ( \beta ) = \mathbb { E } \left[ - { \frac { \partial ^ { 2 } } { \partial \beta ^ { 2 } } } \mathrm { l o g } f ( X \mid \beta ) \right]$ . This value is equal to the negative expected value of the Hessian matrix for the likelihood function $f ,$ i.e., matrix of second derivatives, evaluated at $\beta .$ . Then, the variance of the optimal estimator, $\beta _ { p } ^ { \star } ,$ is defined as the ??th diagonal element of the inverse information matrix: ?????? $\left( \beta _ { p } ^ { \star } \right) \bar { = } [ \mathcal { I } ( \beta ^ { \star } ) ] _ { p , p } ^ { - 1 }$ . By plugging in the likelihood function from Equation (5) and the solution $\pmb { \beta } _ { \mathrm { R } } ^ { \star }$ , we can obtain estimates for the variance and subsequently the standard errors. The exact expression for the Hessian is given in the Appendix. Finally, the test statistic $z _ { \rho } =$ $\beta _ { R } ^ { \star } ( \rho ) / S E { \left( \beta _ { R } ^ { \star } ( \rho ) \right) }$ is asymptotically normal with a mean of 0 and standard deviation of 1. Using this fact, we can conduct hypothesis testing with the robust estimator.

## Interpretation of Robust Estimators

The goal of robust inference is to estimate a set of parameters from the empirical network data that will still provide a reasonable estimate of data that differs from what we used to tune the model. In other words, if we assume that our empirical network does not in fact match the individual networks, the nominal estimators could change significantly, whereas the robust estimators will remain stable, both in terms of likelihood and in terms of bias. We present Figure 2 to illustrate how robust estimators compare to nominal estimators.

![](/api/attachments/W2FNUPAB/fulltext/images/6bfc86737e3484b02a0f894554fac8ce9420b4d64f951725810ac5b71349f910.jpg)  
Note: The likelihood function of the data as perceived by the individuals in the network as a function of the nominal parameter’s $( { \pmb { \beta } } _ { \mathrm { N } } ^ { \star } )$ fit to the individual network data, parameter’s $( { \pmb { \beta } } _ { \mathrm { R } } ^ { \star } )$ fit to empirical network data, and nominal parameter’s $( { \pmb { \beta } } _ { \mathrm { N } } ^ { \star } )$ fit to the empirical network data.

## Figure 2. Impact of Robust Parameters on Likelihood

To show the benefits of the robust estimators $\beta _ { \mathrm { R } } ^ { \star } ,$ , we compare its likelihood $f ( B _ { \mathrm { R } } ^ { \star } )$ to that of standard estimators $f ( B _ { \mathrm { N } } ^ { \star } )$ which assumes data follows a distribution described by the nominal estimators. As input, we use true data $X ^ { \mathrm { i n d } }$ and observable data $X ^ { \mathrm { n e t } }$ , as discussed earlier. In general, it is expected that $f \bigl ( \pmb { \beta } _ { \mathrm { N } } ^ { \star } ( \pmb { X } ^ { \mathrm { n e t } } ) \bigr ) < f \bigl ( \pmb { \beta } _ { \mathrm { N } } ^ { \star } \bigl ( \pmb { X } ^ { \mathrm { i n d } } \bigr ) \bigr )$ because the assumptions are no longer met for $f { \big ( } { \pmb { \beta } } _ { \mathrm { N } } ^ { \star } ( X ^ { \mathrm { n e t } } ) { \big ) } $ . However, robust estimators are immune to assumption deviations, hence we observe $f \bigl ( \pmb { \beta } _ { \mathrm { N } } ^ { \star } ( X ^ { \mathrm { n e t } } ) \bigr ) < f \bigl ( \pmb { \beta } _ { \mathrm { R } } ^ { \star } ( X ^ { \mathrm { n e t } } ) \bigr ) < f \bigl ( \pmb { \beta } _ { \mathrm { N } } ^ { \star } \bigl ( X ^ { \mathrm { i n d } } \bigr ) \bigr )$ , i.e., the robust estimators outperform nominal estimators for observed data and cannot reach the optimality of $\beta _ { \mathrm { N } } ^ { \star } \mathopen { } \mathclose \bgroup \left( X ^ { \mathrm { i n d } } \aftergroup \egroup \right)$ because of a lack of accurate information. In summary, robust parameters are expected to better predict behaviors in a network than nominal parameters if the individual networks and empirical network differ, but will always perform worse than the hypothetical optimum. This phenomenon is referred to as “the price of robustness” (Bertsimas & Sim, 2004).

## Model Demonstration & Testing

## Study 1: Simulation Experiments

## Data Generation & Method

We first performed experiments on a set of computergenerated data. We generated a set of simulated sequences of networks that replicate common behaviors. By creating synthetic data, we were able to control ground-truth values for characteristics of the network at any point in the sequence. Because our method incorporated errors by design, we also randomly generated perturbations in the values of the statistics. For each simulated dataset, we fit a nominal network model and determined the parameters. We then fit a set of robust estimators for varying levels of ${ \bf { \dot { \rho } } } _ { \rho } .$ Finally, we tested the performance of the robust estimators against the nominal estimators on the contaminated data. We generated 100 sequences of network events, where each event was a link $( i , j )$ between two nodes in the network. Each sequence was composed of 5,000 events between 50 actors. We randomly assigned the 50 individuals to one of two groups for purposes of determining homophily. To generate a random sequence, we specified four mechanisms that drive the occurrence of a link: activity rate, reciprocity, homophily, and transitivity. The process for creating a sequence is as follows:

0. Initialize with a sequence $E = \{ ( i _ { 1 } , j _ { 1 } ) \}$ where $( i _ { 1 } , j _ { 1 } )$ is chosen randomly

1. For $t = 2 , \ldots , 5 0 0 0$ do:

a. For all $( i , j ) \in D$ compute $p _ { i j } ( t ) =$ $\lambda _ { i j } ( t ) / \sum _ { ( u , v ) \in D } \lambda _ { u v } ( t )$ where ?? is the set of all possible links

b. Draw an event $( i _ { t } , j _ { t } )$ from the multinomial probability distribution $p ( t )$

c. Add the event to the sequence: $E = \{ E , ( i _ { t } , j _ { t } ) \}$

2. Return sequence ??

In order to carry out these steps, we needed to define the rate for each dyad at a given step ??. Following our prior definition, log $\begin{array} { r } { \Big ( \lambda _ { i j } ( t ) \Big ) = \beta _ { 1 } x _ { i j } ^ { A } ( t ) + \beta _ { 2 } x _ { i j } ^ { R } ( t ) + \beta _ { 3 } x _ { i j } ^ { H } ( t ) + \beta _ { 4 } x _ { i j } ^ { T } ( t ) } \end{array}$ For simplicity, we set all parameters to 1, i.e., $\beta _ { 1 } = \beta _ { 2 } = \beta _ { 3 } = \beta _ { 4 } =$ 1. In Table 3, we provide descriptions of the four statistics. The count of times an event on dyad $( i , j )$ has occurred up to but not including step ?? is $n _ { i j t } .$ , and $y _ { i j }$ is a dummy variable taking a value of 1 if ?? and ?? share a group.

<table><tr><td colspan="3">Table 3. Statistics for Generating Sequences</td></tr><tr><td>Variable</td><td>Formula</td><td>Interpretation</td></tr><tr><td>Activity</td><td> $x_{ij}^{A}(t) = \sum_{k} n_{ikt}$ </td><td>As  $i$  sends more messages,  $i$  is more likely to send a new message.</td></tr><tr><td>Reciprocity</td><td> $x_{ij}^{R}(t) = n_{jit}$ </td><td>As  $j$  increasingly sends  $i$  messages,  $i$  becomes more likely to send a message to  $j$ .</td></tr><tr><td>Homophily</td><td> $x_{ij}^{H}(t) = y_{ij}$ </td><td> $i$  is more likely to send a message to  $j$  and not  $k$  if they are members if the same group and  $k$  is not.</td></tr><tr><td>Transitivity</td><td> $x_{ij}^{T}(t) = \sum_{k} \sqrt{n_{ikt} n_{kjt}}$ </td><td> $i$  is more likely to send a message to  $j$  if there are frequent messages from  $i$  to other actors  $k$  and from those actors to target  $j$ .</td></tr></table>

We assumed that an actor is cognizant of their own rate of communication, who they received links from, and who is in the same group. However, an individual who uses network transitivity as a decision criterion will tend to create links with second-degree connections, or “friends of friends.” Because of incomplete network awareness, we assumed that the network statistic transitivity would be subject to error. Essentially, we assumed that there is some value, $z _ { i j } ^ { T } ( t ) = x _ { i j } ^ { T } ( t ) + \varepsilon _ { i j t }$ , that is equal to the observable transitivity statistic, plus some perception error. We specified the error term in three ways. First, we considered the case where an individual overestimates the strength of third-party connections to the target. Then, we drew the errors from a uniform distribution: $\varepsilon _ { i j t } { \sim } U \left( 0 , \alpha x _ { i j } ^ { T } ( t ) \right)$ Here, ?? is a parameter we specify that dictates the extent of possible errors; for instance, setting ?? = 1 means an individual can perceive the value of transitivity as up to twice as larger as it actually is. Second, we considered the case in which an individual underestimates the strength of third-party connections. Then, we drew the errors from a uniform distribution: $\varepsilon _ { i j t } { \sim } U \big ( { - } \alpha x _ { i j } ^ { T } ( t ) , 0 \big )$ . Finally, we considered the case of random perception errors and drew these from a uniform distribution: $\varepsilon _ { i j t } { \sim } U \left( - \alpha x _ { i j } ^ { T } ( t ) , \alpha x _ { i j } ^ { T } ( t ) \right)$ . To account for a range of error magnitudes, we varied ?? from 0 (i.e., perception matches observable reality) to 1.

We calculated the robust estimators using observed data and using a tolerance parameter of $\rho = 0 , \rho = 0 . 5 * \sigma , \rho = 1 . 0 * \sigma ,$ and $\rho = 1 . 5 * \sigma$ , where ?? is the observed standard error of the transitivity statistic. These robust estimators are denoted $\beta ^ { \star } ( \rho )$ Note that when $\rho = 0$ , we have the nominal parameters of the standard MLE approach. After computing the robust estimators, we can compare them to the true values for the parameters. Specifically, there are two values of interest: (1) the bias in the transitivity parameter $\beta _ { \mathrm { ~ 4 ~ } } ^ { \star } ( \rho ) - \beta _ { 4 }$ , and (2) the overall bias in the parameter vectors $\| { \pmb { \beta } } ^ { \star } ( \rho ) - { \pmb { \beta } } \|$ . If the robust method we are proposing is superior, we would expect the bias to be closer to zero for $\rho > 0$ compared to $\rho = 0$ when some error is present, i.e., $\alpha > 0 .$

## Results

We first examined the level of bias in our estimation of the transitivity parameter at different error levels. The true value of the parameter is $\beta _ { 4 } = 1 ;$ ; when computing bias, values less than 1 indicate underestimation and vice versa. A value of zero for bias indicates a consistent estimator. In Figure 3, we illustrate the average bias across all simulations for underestimation errors, overestimation errors, and random errors. We first noted the nominal case with $\rho = 0 ,$ , i.e., the standard social network method. When any error was introduced $( \alpha > 0 )$ the estimated parameter quickly approached zero, indicated by a bias of approximately -1. This effect is an example of the attenuation bias in the measurement error literature. We also observed that when individuals underestimate transitivity, the nominal model tends to return a negative value for transitivity, i.e., bias of less than -1.

Conversely, when individuals overestimate transitivity, the nominal model tends to yield a somewhat lesser bias, indicating that the estimated parameter is small and positive. For random errors, the nominal model yielded an estimated parameter of approximately zero. What these results reveal is that even at small magnitudes, non-classical errors do not necessarily lead to an estimate of zero. In fact, the direction of the bias in the estimator is consistent with the direction of the errors. Thus, in larger datasets these effects could be magnified, leading to an amplification of the parameter estimates (e.g., Yang et al., 2018).

Turning to the robust models, we found significantly less bias in the estimated parameters when there are errors. Across all three levels of robustness (0.5??, 1.0??, 1.5??), the model produced relatively stable estimates, regardless of the magnitude of errors. We observed that at lower levels of robustness, there was understandably less bias (i.e., estimate is closer to 1), but the effect was small. Further, the value of the robust estimator was similar regardless of whether the errors represented underestimation, overestimation, or randomness. This finding is a feature of the robust approach; regardless of the direction of the errors, the model will return similar estimates of the parameters.

![](/api/attachments/W2FNUPAB/fulltext/images/d523ed034aeb0e3e0ee58bc1c810f733ed5196c1b0b1cd2fc6bebbaa08af8687.jpg)

![](/api/attachments/W2FNUPAB/fulltext/images/5a31a36f2d731014f5d55c9a9786f02f413602c966bfc59f86340bf0dd311048.jpg)

(c) Random Errors  
![](/api/attachments/W2FNUPAB/fulltext/images/5ac1e5b435e63263562270ce0717ef6232f9991ed482a90453741a9a1dde8d77.jpg)

(d) Underestimation Errors  
![](/api/attachments/W2FNUPAB/fulltext/images/450aa7b352125e3744a65dcd2d02c4bc05786a2fa741c574dfda1dd82ad2e1af.jpg)

(e) Overestimation Errors  
![](/api/attachments/W2FNUPAB/fulltext/images/88ac820b498837c7ac8594b14f555dd63af9fe26b202cd16474e136944801468.jpg)

(f) Random Errors  
![](/api/attachments/W2FNUPAB/fulltext/images/0e2e6e73f969173ce3536a446adc6d9597575dd5cf0f540cd1ef377c98b3c667.jpg)

Figure 3. Bias in Transitivity Parameter and Parameter Vector

We further explored the effect of robustness and error on the overall bias in the estimated parameters. We computed the norm of the difference between the real parameters $( \beta _ { 1 } = \beta _ { 2 } = \beta _ { 3 } = \beta _ { 4 } = 1 )$ and the estimated parameters. Smaller values indicated that the estimate, $\pmb { \beta } ^ { \star } ( \rho )$ , was closer to the real value. Again, we varied the magnitude of error ?? for underestimation, overestimation, and random errors. We found that when we introduced perception errors $( \alpha > 0 )$ , the nominal model exhibited significantly greater bias compared to the robust model. This observation held across error types and error magnitudes. Essentially, introducing errors to the transitivity term not only impacted our estimation of the transitivity parameter but also our estimation of each of the other terms as well. By contrast, the robust model consistently yielded a small total bias indicating minimal deviation across estimators. In sum, these results indicate that not only does the robust model provide a less biased estimator of the focal parameter, it also provides a less biased estimator of the entire parameter vector when errors are present.

Next, we considered the standard errors of the proposed robust coefficients, as well as the statistical power of the estimates. The results are presented in Figure 4. In Figures 4a-c, we observe that the robust estimators have much smaller standard errors, on average, relative to the uncorrected model. This holds true across error magnitudes and robustness levels. Turning to Figures 4d-f, we examine the power of the estimated coefficients. We computed statistical power by taking the percentage of the time the network model correctly identified the underlying effect at the 0.05 confidence level. Larger values indicate better power, i.e., greater ability to detect the effect.

We found that the robust model had significantly more power to detect transitivity, even in the presence of small deviations. This finding has clear implications for statistical inference: when errors are present, a robust model is more likely to correctly reject the null hypothesis. Finally, we compared the model fit of the different estimators. In this step, we fit a standard social network model to data with no errors $( \alpha = 0 )$ . We also fit our robust models to the same datasets. Then, we applied our estimated parameters to different sequences with progressively greater perception errors and calculated the likelihood of the sequences. By computing the likelihood using parameter estimates from an error-free model, we tested how well the different models could predict events out of sample. We present our results in Figure 5.

(a) Underestimation Errors  
![](/api/attachments/W2FNUPAB/fulltext/images/6ac137c30608e9ea7b04e276ccae585650ab6ed35f53d55e7e9e5bff8bcb8d3a.jpg)

![](/api/attachments/W2FNUPAB/fulltext/images/35c2583eafea7fb6f5f350cf07402c252a70d2b5a46d9d989486c159f6ef794b.jpg)

(c) Random Errors  
![](/api/attachments/W2FNUPAB/fulltext/images/6fdae7a8323c6d5e6bd8ff2bbb2aba1807b206fc99d51a0c17fe8d975517544b.jpg)

(d) Underestimation Errors  
![](/api/attachments/W2FNUPAB/fulltext/images/24d481ccc495ebb392be9813ab9e23143c36f80d842ccec60f718beac1ac4a5b.jpg)

![](/api/attachments/W2FNUPAB/fulltext/images/49559b1c9a014603546700b3f65abf007be215e1254d0c99cf4264eb0f4e24c9.jpg)

(f) Random Errors  
![](/api/attachments/W2FNUPAB/fulltext/images/c86c45a1497dffb018ae458b0f7b0d32b1d84b299e7083bc81e9ee2d191e615e.jpg)  
― Nominal ― ?? = 0.5?? ― ?? = 1.0?? ― ?? = 1.5??

## Figure 4. Standard Errors and Statistical Power of Estimates

(a) Underestimation Errors  
![](/api/attachments/W2FNUPAB/fulltext/images/bffaa1f26f786daccfbf145db543f576e0a0895b95f2e6ae9ed46b430d2f8dfa.jpg)

(b) Overestimation Errors  
![](/api/attachments/W2FNUPAB/fulltext/images/7ecb0df140ad57284df12b741ef07cb61951cf2e901b3400ca043b4599725786.jpg)

(c) Random Errors  
![](/api/attachments/W2FNUPAB/fulltext/images/8f45e51aa458c5e6f54d7a2246f82dead9443ab29b4d81266d0c8cfa9d697a83.jpg)

$$
- \text {Nominal} - \rho = 0. 5 \sigma - \rho = 1. 0 \sigma - \rho = 1. 5 \sigma
$$

We observed that the robust models outperform the nominal models in all cases where an error is present. The difference between the nominal and robust fit grew as more error was introduced into the model, i.e., ?? increased. Further, while all models fared worse when more errors were added, the model with the most robustness $( \rho = 1 . 5 \sigma )$ degraded most slowly. In summary, if we fit a robust social network model to a dataset, then it will have greater predictive power when applied to observations with more errors.

## Study 2: Laboratory Example

## Dataset & Analyses

As a further illustration of the robust network model, we applied our methodology to data collected from experiments on team decision-making. Our sample is composed of twenty 20-person multiteam systems (MTS, or teams of teams), (N = 400) engaged in a military-style strategic coordination task, collected as part of a larger research project. Each twentyperson MTS comprised four 5-person teams. Participants were recruited at a midwestern US university and participated in the study in exchange for either research credit or \$35. Participants reported to a laboratory in groups of 20 and were randomly assigned to four teams. Each MTS session was divided into three phases: training, practice mission, and performance mission. During the training phase, the entire 20-person group trained together in a large room where they all watched a video explaining the enemy occupation and the nature of their mission. When the video concluded, participants completed a brief survey including demographic and prior familiarity items. The participants then performed a 15-minute practice mission during which they familiarized themselves with the game functionality, the communication channels, and their role responsibilities. After the practice mission, the main observation period began. The overarching goal of the group was to guide a convoy through a region comprised of four equally sized subregions. Each team worked in a distinct subregion to clear obstacles in the convoy’s path. The conditions of the subregion represented a local team goal not shared with the other teams.

We collected data in a variety of formats. Surveys were given at the beginning and end of the session. At the beginning, participants answered questions regarding demographics, personality traits, and experience with video games. At the end, participants were asked a variety of team process questions. We also asked each participant to answer the following question: “With whom did you communicate during the mission?” Participants then checked a box for each of the other members of the group with whom they recalled communicating. Their responses thus constitute an individual network, i.e., they represent the links that the members of the population believe exist. In addition to the survey measures, we collected digital trace data in the form of communication transcripts. Participants communicated with one another solely through Skype and could choose chat or audio messages. All audio messages were transcribed using audio and video files to ensure accuracy. Chat messages were downloaded from our game server. We then combined these two data streams to form a complete timestamped transcript, with each observation formatted as <Timestamp, Sender, Receiver, Message, Channel>.

For each of the 20 sessions, we created two networks, which are denoted as $z _ { k }$ and $y _ { k }$ . Network $z _ { k }$ represents the individual network for session ??. For every pair of individuals $( i , j )$ then, a link was present, i.e., $z _ { i j k } = 1$ , if individual ?? reported that they communicated with ??. Otherwise, each link had zero value. The network $y _ { k }$ represented the empirical network for session ??. Here, we created a dichotomous network by setting $y _ { i j k } = 1$ if there were any messages sent from ?? to ?? during the session, and zero otherwise. Thus, $y _ { k }$ represents the typical “digital trace network” that can readily be collected through technology (i.e., Skype). To determine whether the digital trace operationalization leads to biased inference, we estimated ERGMs on both networks. We included four common network statistics: edges, mutual ties, in-degree centralization, and out-degree centralization. The edge statistic represents the network density, while the mutual statistic represents the frequency with which ties are reciprocated. In- and out-degree centralization represent the variance in the degree distribution and can be loose proxies for power law tendencies. The parameter estimates from the ERGMs are denoted as $\pmb { \beta } ^ { \star } { } ^ { z }$ and $\pmb { \beta } ^ { \star \mathcal { Y } }$

## Findings

Descriptive statistics for the 20 networks are presented in Table 4. We calculated the parameter estimates $\bar { \pmb { \beta } } ^ { \star 2 }$ and $\pmb { \beta } ^ { \star \mathcal { Y } }$ for every session, as well as robust estimates $\beta ^ { \star } ( \rho )$ for different levels of robustness. We set three levels of $\rho$ based on the standard deviation of the underlying statistic. For instance, the in-degree centralization statistic had a standard deviation of approximately 0.20 across the 20 sessions; we thus set $\sigma = 0 . 2$ for that statistic.

After fitting the models, we computed the bias in the individual parameters, as well as the parameter vector as a whole. For the parameters, we calculated a standardized bias, then squared it to compare absolute magnitudes (i.e., the mean square error). The formula for the bias in parameter ?? at $\begin{array} { r } { \left( \beta _ { p } \right) _ { \rho } ^ { 2 } = \left( \frac { \left( \hat { \beta } _ { p } ^ { z } - \hat { \beta } _ { p } ^ { y } ( \rho ) \right) } { \hat { \beta } _ { p } ^ { z } } \right) ^ { { \mathrm { ~ : ~ } } } } \end{array}$ 2 robustness level ?? is: ???????? . This value is comparable across sessions as well as across statistics. Larger numbers indicate greater bias, while a value of zero would be a consistent estimate. We also computed total bias by taking the norm difference between the parameter vectors, $\| \pmb { \beta } ^ { \star \cal Z } -$ $\pmb { \beta } ^ { \star y } ( \rho ) \big | \big | / \big | \big | \pmb { \beta } ^ { \star z } \big | \big |$ . We report the results in Table 5.

Overall, our findings indicate that the robust model is significantly less biased with respect to the individual network as compared to the nominal digital trace empirical network. As indicated by the bold italics in Table 5, a non-zero level of robustness consistently resulted in the lowest bias for the individual statistics and for the parameter vector as a whole. Using a tolerance of one standard deviation overall yielded the best performance, with all but one parameter being less biased than the nominal model.

In addition to analyzing bias, we also examined the error rates of each model with respect to statistical inference. We coded a model as giving a false positive if it yielded a significant estimate of a coefficient, while the coefficient for the survey network was nonsignificant. Similarly, a false negative occurs when the model determines a coefficient is nonsignificant; however, in the survey network, that coefficient was significant. We report the error rates, as well as the total error rate, in Table 6.

<table><tr><td colspan="3">Table 4. Descriptive Statistics for Networks</td></tr><tr><td>Variable</td><td>Mean</td><td>SD</td></tr><tr><td>Survey density</td><td>0.416</td><td>0.066</td></tr><tr><td>Survey in-centralization</td><td>6.735</td><td>2.914</td></tr><tr><td>Survey out-centralization</td><td>15.324</td><td>7.981</td></tr><tr><td>Number of messages</td><td>948</td><td>130</td></tr><tr><td>Observed density</td><td>0.192</td><td>0.009</td></tr><tr><td>Observed in-centralization</td><td>4.554</td><td>2.098</td></tr><tr><td>Observed out-centralization</td><td>5.496</td><td>2.713</td></tr></table>

<table><tr><td colspan="5">Table 5. Model Bias for ERGM Parameters</td></tr><tr><td></td><td colspan="4">Squared Parameter Bias (standardized)</td></tr><tr><td>Variable</td><td> $\rho = 0$ </td><td> $\rho = {0.5\sigma }$ </td><td> $\rho = {1.0\sigma }$ </td><td> $\rho = {1.5\sigma }$ </td></tr><tr><td>Edges</td><td>0.144</td><td>0.173</td><td>0.096</td><td>0.111</td></tr><tr><td>Mutual</td><td>4.427</td><td>3.736</td><td>3.036</td><td>3.780</td></tr><tr><td>In-centralization</td><td>0.667</td><td>0.456</td><td>0.789</td><td>1.228</td></tr><tr><td>Out-centralization</td><td>0.309</td><td>0.330</td><td>0.202</td><td>0.160</td></tr><tr><td>Standardized norm bias</td><td>0.464</td><td>0.457</td><td>0.434</td><td>0.494</td></tr></table>

<table><tr><td colspan="5">Table 6. Error Rates for Standard and Robust Models</td></tr><tr><td>Error type</td><td> $\rho = 0$ </td><td> $\rho = {0.5\sigma }$ </td><td> $\rho = {1.0\sigma }$ </td><td> $\rho = {1.5\sigma }$ </td></tr><tr><td>False positive (%)</td><td>8.75%</td><td>10.00%</td><td>10.00%</td><td>10.00%</td></tr><tr><td>False negative (%)</td><td>10.00%</td><td>2.50%</td><td>3.75%</td><td>6.25%</td></tr><tr><td>Total (%)</td><td>18.75%</td><td>12.50%</td><td>13.75%</td><td>16.25%</td></tr></table>

We found that when conducting hypotheses tests, models with robustness (?? > 0) made fewer inference errors than a nominal model (?? = 0). In particular, we found that the driving factor was the false-negative rate. On average, running a model on the network from digital trace data yielded a falsenegative rate of 10%, while the robust model yielded a falsenegative rate of at most 6.25%. This finding indicates that analyzing a network using raw digital trace data will cause researchers to miss important effects about one in ten times. However, accounting for errors through robustness significantly reduces this problem. Further, all models had comparable false-positive rates, which suggests that reducing false negatives does not mean increasing false positives.

There are three key takeaways from this analysis. First, a robust model will return parameter estimates that are closer in value to the perceived network, as determined by the bias in the estimation. Second, a nominal model tends to yield parameter estimates that are biased relative to the underlying perceived network, and the problem is worse for more complex statistics (e.g., centralization). Third, a robust model makes fewer inference errors, particularly false negatives. These findings have direct implications for statistical inference and hypothesis testing. Given that the robust model is less biased and less prone to inference errors relative to the perceived network, we posit that the corresponding parameter estimates are better representations of the network structure as it relates to individual decision-making. Thus, when hypotheses are formulated at an individual level, the robust model may be more appropriate. Finally, because the nominal model yields biased estimates, we argue that not using the robust model increases the risk of incorrectly rejecting (or failing to reject) the null hypothesis.

## Study 3: Empirical Example

## Dataset & Analyses

In our final study, we present evidence using real-world data to support the contention that measurement errors are prevalent and can have significant effects when using digital trace data. We sought a context that would enable us to generalize beyond a strictly social network. We analyzed data from the online encyclopedia Wikipedia. We accessed data used in a recently published study (Lerner & Lomi, 2020) that has been made publicly available for research.<sup>3</sup> Our sample is composed of all recorded edits to articles during October and November of 2017. In total, we analyzed 141,364 edit events made by 2,665 unique users on 49,914 unique pages. Every observation was recorded in the format $( t , u , v )$ which represents <Time, User, Article>. The full dataset is the ordered sequence $E = \{ e _ { 1 } , e _ { 2 } , \dots , e _ { 1 4 1 3 6 4 } \}$ where $\boldsymbol { e } _ { i } = ( t _ { i } , u _ { i } , v _ { i } )$ and $t _ { i + 1 } > t _ { i }$ for all $i = 1 , \ldots , 1 4 1 , 3 6 4$

We conducted an analysis of contributor behavior—namely, the probability that a user ?? would contribute to article ?? at time ??. As predictors, we used four explanatory mechanisms used in prior studies: inertia, activity, popularity, and four-cycle (Brunswicker & Schecter, 2019; Lerner & Lomi, 2020; Quintane et al., 2014). To calculate each of these statistics, we used the weight $\omega _ { u v } ( t )$ , which captured the frequency of ?? editing ?? up to time ??, weighted by recency. Specifically, the formula for ??(??) that we used was: $\begin{array} { r } { \omega _ { u v } ( t ) = \sum _ { i : t _ { i } < t } 1 \{ t _ { i } = } \end{array}$ $\begin{array} { r } { \tau , u _ { i } = u , v _ { i } = v \} \times \exp \left( - \frac { ( t - \tau ) \log 2 } { T _ { 1 / 2 } } \right) } \end{array}$ . We can interpret $\omega _ { u v } ( t )$ as the instances of ?? editing ?? up to time $t ,$ with the weight of each prior event decayed according to a half-life $T _ { 1 / 2 } .$ By using a half-life, we were able to account for the relative salience of more recent events compared to events in the distant past. For our analyses, we used the half-life of $T _ { 1 / 2 } = 7$ days.

Variable inertia measures the frequency with which ?? has edited ?? prior to the present time ??. The formula for inertia is $x _ { u v } ^ { I } ( t ) = \omega _ { u v } ( t )$ . Activity represents the frequency with which user ?? made edits in the past, and popularity represents the frequency with which article ?? received edits in the past. We calculate activity as $\begin{array} { r } { x _ { u v } ^ { A } ( t ) = \sum _ { h } \omega _ { u h } ( t ) } \end{array}$ and popularity as $\begin{array} { r } { x _ { u v } ^ { P } ( t ) = \sum _ { k } \omega _ { k v } ( t ) } \end{array}$ . Finally, the four-cycle captures the extent to which ?? will edit ??, as a function of how frequently ?? jointly edited other articles ℎ with other users ?? and how frequently those users contributed to ??. The formula for a four-cycle is $\begin{array} { r } { x _ { u v } ^ { C } ( t ) = \sum _ { k } \omega _ { k v } ( t ) \sum _ { h } \omega _ { u h } ( t ) \omega _ { k h } ( t ) } \end{array}$ . Essentially, the fourcycle measures the tendency for editors to work in local clusters on the same subset of articles.

Given these four statistics, we estimated the following model predicting the probability of an edit event at a particular time:

$$
\mathrm{logit} (p _ {u v t}) = \beta_ {1} x _ {u v} ^ {I} (t) + \beta_ {2} x _ {u v} ^ {A} (t) + \beta_ {3} x _ {u v} ^ {P} (t) + \beta_ {4} x _ {u v} ^ {C} (t) + \varepsilon_ {u v t}.
$$

The solution to this model, $\pmb { \beta } ^ { \star }$ , is the nominal estimator for our dataset. We then calculated our robust estimator, $\pmb { \beta } ^ { R } ( \rho )$ , at three levels of robustness. These levels of robustness were premised on the assumption that editors might be inaccurate in their recollections of their own prior editing activities or those with whom they coedited. The values we used are $\rho = 0 . 1 , 0 . 3 , 0 . 5 .$ which are roughly equal to 0.5x, 1.0x, 1.5x the standard errors of the four variables.

Finally, we conducted experiments on the sampled data to determine the fit and bias of the robust estimator. We began by generating an artificial “measurement error” in our dataset by randomly perturbing each statistic by a small amount. Namely, each statistic $x _ { u v } ( t )$ was replaced by $\overline { { { x } } } _ { u v } ( t ) = x _ { u v } ( t ) + \delta ,$ where ?? was a random error drawn from a uniform (−????, ????) distribution. The value ?? is the standard error of the statistic and ?? is a parameter controlling the magnitude of the errors; we test $\alpha = 0 . 5$ to 1.5 in increments of 0.25. By adding random errors of various magnitudes, we preserved the average values of all four statistics while increasing the amount of variance in our data. By adding errors from the uniform distribution, we allowed for any error within that range to be equally likely.<sup>4</sup> Essentially, we replicated a scenario where our data contained some degree of measurement error made by editors that we did not capture but which may have influenced their actions. The statistics $\overline { { x } } _ { u v } ( t )$ can be thought of as the individual beliefs, while ${ \pmb x } _ { u v } ( t )$ is the empirical instantiation we observed. Then, we were able to refit the prior logit regression which yielded the estimated parameters $\pmb { \beta } ^ { E }$ , or parameters under error. We compared $\pmb { \beta } ^ { \star }$ and $\pmb { \beta } ^ { R } ( \rho )$ to $\pmb { \beta } ^ { E }$ in order to determine which estimates were less biased with regard to the perturbed data. The model with the least bias should be the one that best approximates the parameters related to individual beliefs.

## Results

We report the nominal and robust estimators in Table 7. In the nominal case, all four variables were positive and significant, indicating that each of the mechanisms influenced an individual’s decision regarding which article to contribute to. Likewise, at all three levels of robustness, we found consistent results; thus, we would reach the same qualitative conclusions from an explanatory perspective. As expected, the log-likelihood for the robust models was worse than the nominal case. Interestingly, we note that the robust model attenuated some variables but amplified others.

In particular, the effect of inertia was attenuated in each of the robust models, indicating that the models reduced the effect of inertia. On the other hand, activity, popularity, and the four-cycle were all amplified by the robust models. We also found that the parameter estimates did not increase or decrease linearly with the robustness parameter $\rho .$ This finding demonstrates the capacity of robust optimization to find different local solutions, compared to nonlinear data. Finally, the standard errors of the robust estimates were smaller than the nominal standard errors, often by an order of magnitude. Further, the standard errors for the robust estimates were relatively consistent compared to values of ${ \dot { } } _ { \rho . }$ This finding reflects an important characteristic of the robust method; estimates are significantly more precise, even for small error tolerances.

We next compared the performance of the robust and nominal models when measurement errors were added to the dataset. In Figure 6a we present the normalized deviation of the nominal $\frac { \mathbb { | } \beta ^ { E } - \beta ^ { \star } \mathbb { | } | } { \| \beta ^ { E } \| }$ and robust parameters $\frac { \| \pmb { \beta } ^ { E } - \pmb { \beta } ^ { R } \| } { \| \pmb { \beta } ^ { R } \| }$ (from Table 7), and in Figure 6b we present the model fit of the estimates to the perturbed dataset. We found that the robust estimators $\pmb { \beta } ^ { R } ( \tilde { \rho } )$ deviated significantly less, relative to the estimates under measurement error $\pmb { \beta } ^ { E }$ (see Figure 6a). Essentially, if measurement errors had been present in our dataset, the typical estimator $\pmb { \beta } ^ { \star }$ would have been significantly different than the true population parameters. The robust estimator on the other hand would have been closer in value to those true parameters.

Further, in Figure 6b we see that the robust estimators exhibit a better fit to the data under measurement error, indicating that the robust estimator has greater predictive power. It’s worth noting that if the measurement error is significantly smaller than the robust tolerance, the nominal model still has a better overall fit (for example, ?? = 0.5 and ?? = 0.5). However, with large errors, all robust models outperform the nominal model.

Overall, our findings indicate that if empirical data contains some unobserved measurement error, a robust estimator will be less biased with respect to the parameters and exhibit better model fit than the nominal approach. Further, the robust model is able to achieve these performance gains while preserving the explanatory conclusions.

## Discussion

In this study, we explore how discrepancies between observable network data and perceived network data can bias statistical analyses. We delineate a number of sources of contamination in social network data. These include technical features of the nature of online data sources, including the size and magnitude of online networks, the rate at which they evolve, and the varying degrees of people’s perceptions of the network (its translucency or visibility) across online platforms. The second source of discrepancy stems from natural cognitive tendencies of the individuals within the network, such as compression, personality traits, and positions such as power. Despite this evidentiary body of literature, social network inference methodologies generally treat observable data, such as networks collected from online sources, as accurate proxies for the perceived network on the bases of which people often act. Inference about human behavior is derived from measures of this empirical information, which may deviate from the internal schema that individuals believe to be true. And, as discussed earlier, many social science theories, and more specifically IS studies, offer explanations based on people’s perceptions of actions and interactions rather than their objective occurrences as captured, say, by digital trace data.

Our primary contribution is to introduce a methodology that significantly reduces the bias in estimates of error-laden social network patterns, and subsequently leads to more accurate statistical inference. We extend the work of Bertsimas and Nohadani (2019) by deriving a robust maximum likelihood estimator for the exponential family of probability distributions. Further, we introduce a robust test statistic that allows researchers to conduct hypothesis testing after correcting for errors. Our framework preserves the techniques of classic network analysis while making the estimates resilient to the discrepancies we recognize are present in our data. In both our simulation experiments and empirical examples, the robust MLE produced estimates that were less biased relative to ground-truth values. Further, our method produced more accurate hypothesis testing; we found that the robust method had greater statistical power and resulted in fewer incorrect conclusions.

Beyond the quantitative advantages enabled by our approach, there are also qualitative advantages to the robust method. Robust estimation acts as a type of filter for cognitive effects, essentially imposing a larger burden of proof on structures that may be difficult for individuals to detect. Researchers can now incorporate explanations based on people’s agency into their network hypotheses, knowing that the robust parameters broadly incorporate potential sources of bias. By accounting for cognition, the standard and robust models ask inherently different questions. Standard network inference asks: “What is the effect of structure ?? on behavior $y ,$ assuming that the perceived structure matches the truth?” In contrast, robust network inference asks: “What is the effect of structure ?? on behavior ??, if the actor responsible for that behavior perceives structure ?? somewhat differently than what is assumed to be the truth?”

The differences between a nominal approach to network inference and a robust approach are subtle, but they highlight an important deviation from the standard method of analyzing networks. Current models of agentic behavior model cognition—e.g., recency effects incorporated in Butts’s (2008) relational event framework—but only to the extent that empirical observation matches perceived reality. Taking a robust approach to analysis makes the interpretation of true agency more realistic since it directly incorporates the systematic errors that are likely to occur.

(a) Parameter Deviation  
![](/api/attachments/W2FNUPAB/fulltext/images/7177c4d4df95d8725f45f36c22576310e1950f375fe59b9c2feaca69d2f8f614.jpg)

(b) Model Fit  
![](/api/attachments/W2FNUPAB/fulltext/images/4c0c6714abc70125738050d8cb95ced59cdc315fd339720b23c7be0a34cc4f54.jpg)

$$
- \text {   Nominal   } - \rho = 0. 1 - \rho = 0. 3 - \rho = 0. 5
$$

Figure 6. Deviation and Fit to Data with Measurement Error

<table><tr><td colspan="5">Table 7. Nominal and Robust Estimates for Wikipedia Data</td></tr><tr><td></td><td>Nominal</td><td> $\rho = 0.1$ </td><td> $\rho = 0.3$ </td><td> $\rho = 0.5$ </td></tr><tr><td>Inertia ( $\beta_1$ )</td><td>11.210*(0.213)</td><td>7.092*(0.003)</td><td>7.738*(0.003)</td><td>5.978*(0.004)</td></tr><tr><td>Activity ( $\beta_2$ )</td><td>1.131*(0.004)</td><td>1.288*(0.001)</td><td>2.108*(0.001)</td><td>2.404*(0.001)</td></tr><tr><td>Popularity ( $\beta_3$ )</td><td>0.570*(0.011)</td><td>1.112*(0.002)</td><td>0.973*(0.002)</td><td>1.449*(0.004)</td></tr><tr><td>Four-Cycle ( $\beta_4$ )</td><td>0.325*(0.017)</td><td>1.296*(0.002)</td><td>0.740*(0.001)</td><td>1.015*(0.002)</td></tr><tr><td>Log Likelihood</td><td>-90,103</td><td>-165,490</td><td>-386,300</td><td>-317,830</td></tr></table>

Note: Standard errors in parentheses. $^ { \star } p < 0 . 0 0 1$

## Applying the Robust Method

Considering the findings of our study, we provide a general template for conducting statistical inference on digital trace network data with robust maximum likelihood. We identify four key steps in the process, which we illustrate in Figure 7. First, the researcher should construct the network and compute the necessary statistics (e.g., transitivity or preferential attachment). The choice of statistics should be informed by the relevant theory or theories being tested. Second, the researcher should determine the appropriate levels of robustness, with the robustness level corresponding to confidence bounds on the error magnitudes. In this paper, we used multiples of the standard deviations of the network statistics. This approach would be appropriate when considering multiple observations of networks (e.g., Faraj & Johnson, 2011) or multiple individual-level actions (e.g., Quintane & Carnabuci, 2016). In situations where only one network is being considered, uncertainty bounds could be selected based on percentages of the statistic value (e.g., 10% variation). Ideally, a range of robustness levels would be selected for analysis. Third, the researcher should fit multiple models: the nominal model as well as a robust model for each of the specified tolerance levels.

This step will yield the nominal parameters $\beta _ { N } ^ { \star } ,$ robust parameters $B _ { R } ^ { \star } ( \rho )$ , and the standard errors for each coefficient using the procedure described. Finally, the researcher should conduct statistical inference by computing the test statistic $\beta / S E ( \beta )$ for each coefficient across the robustness levels. The researcher will reach one of four conclusions for each level of robustness tested.

Case 1: The nominal coefficient is significant (indicating a strong effect) and the robust coefficient at level $\rho$ is also significant. Here, we conclude that even if the underlying data is not accurate (within a range given by $\rho ) ,$ the effect is still strong enough to be detected. This case would lead the researcher to conclude their effect is resilient to measurement errors of magnitude $\rho .$

Case 2: The nominal coefficient is significant, but the robust coefficient at level $\rho$ is not. Essentially, the hypothesized effect disappears if bias of magnitude $\rho$ is present in the observed data, suggesting an amplification bias. The researcher would then conclude that the measure is sensitive to measurement errors of magnitude $\rho ;$ in other words, there is a greater probability of false-positive errors.

![](/api/attachments/W2FNUPAB/fulltext/images/75457f11ba4d65f0956b2914f76e6a1aae3aad07d30535499ffe7eb5c66ccb70.jpg)

Case 3: The nominal coefficient is not significant, but the robust estimate is significant at level ??. When ?? is small (e.g., a fraction of one standard deviation), then this scenario could represent attenuation, i.e., a measurement error leading to a bias towards zero. The robust estimator would account for that error and would thus potentially remedy a false-negative error. However, the larger the value of ??, the less likely it is that the underlying effect is present.

Case 4: Neither the nominal nor robust coefficients are significant. In this scenario, the researcher can conclude that the lack of observed effect is not due to simple errors.

As the above cases make clear, robust optimization should be used in addition to standard methods, not in place of them. The results obtained from the nominal data are important because they identify key patterns in the data, but they may be misleading with regard to network perception and individual decision-making. If the nominal model identifies an independent variable as significant, but the robust version does not, then the effect should be interpreted through a more conservative lens, particularly regarding cognition. Conversely, if the robust model identifies an effect that the nominal model does not, then that measure may be suffering from attenuation bias. In both cases, the robust approach improves our ability to make accurate inferences and subsequently improves our ability to conduct hypothesis testing.

## Limitations

While the robust approach produces results that are more sensitive to cognitive issues, there are still limitations to our interpretations. First, the method introduced in this study reduces the likelihood of falsely concluding an association between two variables but still does not imply what an individual does or does not perceive. Second, there are alternative methods for correcting biased observable networks. We could obtain CSS information from every individual at every time point being considered. For a single network this may be reasonable, but for longitudinal networks this process becomes increasingly impractical. Additionally, these reports would have to be collected when the tie was formed, otherwise the data would still subject to errors in recollection. Alternatively, we could infer an individual’s perceived network, based on systematic biases found empirically. The challenge with this approach is the impracticality in empirically identifying a specific underlying distribution for cognition that takes all theoretical sources of bias into account. This approach could potentially provide a less conservative alternative to robust estimation, but further research is needed.

A third general limitation stems from the modeling decisions of the practitioner. Because we are explicitly assuming no a priori knowledge of the errors, our choice in the geometry of the uncertainty sets in fact represents our implicit assumptions about the errors. To mitigate the bias that could be injected by this process, we recommend testing a variety of uncertainty sets and carefully documenting the discrepancies between various models. When we have reason to believe that the errors follow some distribution, then an ellipsoidal geometric set becomes a natural choice (see Bertsimas & Nohadani, 2019). On the other hand, when only maximum errors are known, a polyhedral set—as used in our implementation—offers a good description. Likewise, the analyses presented in this paper assume an exponential likelihood function for the network data. Although this assumption is common in network analysis, there are other ways to model the data that we do not consider. Examples include multilevel models (Sweet et al., 2013), quadratic assignment (Krackardt, 1987), and graph embedding (Cui et al., 2017). Robust optimization could be used to find estimators that are immunized to errors in these models. However, future research is needed.

Finally, given the difficulty of collecting both trace data and self-reports for large networks, there are limited studies directly measuring the extent of perception errors, particularly in IS settings. However, evidence from largescale studies of email exchanges, social media, and proximity data from wearable or mobile devices suggests that while trace information is relatively consistent with sociometric surveys, there is a persistent misalignment. Future research should more thoroughly examine the prevalence and magnitude of this perception gap.

## Conclusion

The increasing availability of digital trace data is celebrated as a bonanza for computational social science approaches, including social network analytics. The problem of perception limits the interpretation of hypothesized mechanisms in social network analysis conducted using digital trace data that offer varying degrees of technological affordances. Hence, explanations that assume individuals act and interact based on the observed network in the digital trace data are not always warranted. We propose a novel method that looks for inferences that are robust to differences between the observed network data and individuals’ perceptions of those data. Our proposed method applies advances in robust optimization to the field of social networks by integrating robust techniques into common inferential models. Using data from computer simulations, laboratory experiments, digital sources, and field settings, we illustrate the efficacy of our technique in adjusting the effects of variables impacted by perception and providing overall better predictive capabilities.

## Acknowledgments

The authors would like to thank the senior editor, associate editor, and reviewers for their constructive comments. N.C. was supported by funding from NASA award 80NSSC21K0925 and NSF award 2052366.

## References

Agarwal, R., Gupta, A. K., & Kraut, R. (2008). Editorial overview: The interplay between digital and social networks. Information Systems Research, 19(3), 243-252.

Aral, S., & Van Alstyne, M. (2011). The diversity-bandwidth tradeoff. American Journal of Sociology, 117(1), 90-171.

Aral, S., & Walker, D. (2012). Identifying influential and susceptible members of social networks. Science, 337(6092), 337-341.

Aral, S., & Walker, D. (2014). Tie Strength, Embeddedness, and Social Influence: A Large-Scale Networked Experiment. Management Science, 60(6),1352-1370.

Bapna, R., Gupta, A., Rice, S., & Sundararajan, A. (2017). Trust and the strength of ties in online social networks: An exploratory field experiment. MIS Quarterly, 41(1), 115-130.

Bapna, R., Qiu, L., & Rice, S. (2017). Repeated interactions versus social ties: quantifying the economic value of trust, forgiveness, and reputation using a field experiment. MIS Quarterly, 41(3), 841-866.

Bapna, R., & Umyarov, A. (2015). Do your online friends make you pay? A randomized field experiment on peer influence in online social networks. Management Science, 61(8), 1902- 1920.

Barabási, A. L. (2010). Bursts: The hidden patterns behind everything we do, from your e-mail to bloody crusades. Penguin.

Batchelder, W. H., Kumbasar, E., & Boyd, J. P. (1997). Consensus analysis of three‐way social network data. Journal of Mathematical Sociology,22(1), 29-58.

Ben-Tal, A., El Ghaoui, L., & Nemirovski, A. (2009). Robust Optimization, Princeton University Press.

Ben-Tal, A., & Nemirovski, A. (2002). Robust optimizationmethodology and applications. Mathematical Programming, 92(3), 453-480.

Berente, N., Seidel, S., & Safadi, H. (2019). Research commentary: Data-driven computationally-intensive theory development. Information Systems Research, 30(1), 50-64.

Berger, K., Klier, J., Klier, M., & Probst, F. (2014). A review of information systems research on online social networks. Communications of the Association for Information Systems, 35, 145-172.

Bernard, H. R., Killworth, P. D., & Sailer, L. (1982). Informant accuracy in social-network data V. An experimental attempt to predict actual communication from recall data. Social Science Research, 11(1), 30-66.

Bertsimas, D., Brown, D. B., & Caramanis, C. (2011). Theory and applications of robust optimization. SIAM Review, 53(3), 464- 501.

Bertsimas, D., & Nohadani, O. (2019). Robust maximum likelihood estimation. INFORMS Journal on Computing, 31(3), 445-458.

Bertsimas, D., Nohadani, O., & Teo, K. M. (2007). Robust optimization in electromagnetic scattering problems. Journal of Applied Physics, 101(7), Article 074507.

Bertsimas, D., Nohadani, O., & Teo, K. M. (2010). Robust optimization for unconstrained simulation-based problems. Operations Research, 58(1), 161-178.

Bertsimas, D., & Sim, M. (2004). The price of robustness. Operations Research, 52(1), 35-53.

Bhattacharya, P., Phan, T. Q., Bai, X., & Airoldi, E. M. (2019). A coevolution model of network structure and user behavior: The case of content generation in online social networks. Information Systems Research. 30(1), 117-132.

Brands, R. A. (2013). Cognitive social structures in social network research: A review. Journal of Organizational Behavior, 34(S1), S82-S103.

Brashears, M. E., & Quintane, E. (2015). The microstructures of network recall: How social networks are encoded and represented in human memory. Social Networks, 41, 113-126.

Brunswicker, S., & Schecter, A. (2019). Coherence or flexibility? The paradox of change for developers’ digital innovation trajectory on open platforms. Research Policy, 48(8), Article 103771.

Burt, R. S., Kilduff, M., & Tasselli, S. (2013). Social network analysis: Foundations and frontiers on advantage. Annual Review of Psychology, 64, 527-547.

Butts, C. T. (2008). A relational event framework for social action. Sociological Methodology, 38(1), 155-200.

Cao, J., Basoglu, K. A., Sheng, H., & Lowry, P. B. (2015). A systematic review of social networks research in information systems: Building a foundation for exciting future research. Communications of the Association for Information Systems, 36, 727-758.

Carroll, R. J., Ruppert, D., Stefanski, L. A., & Crainiceanu, C. M. (2006). Measurement error in nonlinear models: A modern perspective. Chapman & Hall/CRC.

Carroll, R. J., & Stefanski, L. A. (1994). Measurement error, instrumental variables and corrections for attenuation with applications to meta-analyses. Statistics in Medicine, 13(12), 1265-1282.

Casciaro, T. (1998). Seeing things clearly: Social structure, personality, and accuracy in social network perception. Social Networks, 20(4), 331-351.

Casciaro, T., Carley, K. M., & Krackhardt, D. (1999). Positive affectivity and accuracy in social network perception. Motivation and Emotion, 23(4), 285-306.

Casciaro, T., Gino, F., & Kouchaki, M. (2014). The contaminating effects of building instrumental ties: How networking can make us feel dirty. Administrative Science Quarterly, 59(4), 705-735.

Chen, W., Wei, X., & Zhu, K. X. (2017). Engaging voluntary contributions in online communities: A hidden Markov model. MIS Quarterly, 42(1), 83-100.

Contractor, N. (2018). How can computational social science motivate the development of theories, data, and methods to advance our understanding of communication and organizational dynamics? In B. F. Welles & S. González-Bailón (Eds.), The Oxford handbook of networked communication. Oxford University Press.

Corman, S. R. (1990). A model of perceived communication in collective networks. Human Communication Research, 16(4), 582-602.

Corman, S. R., & Scott, C. R. (1994). Perceived networks, activity foci, and observable communication in social collectives. Communication Theory, 4(3), 171-190.

Cox, D. R. (1972). Regression Models and Life-Tables. Journal of the Royal Statistical Society. Series B (Methodological), 34(2),187-220.

Cui, P., Wang, X., Pei, J., & Zhu, W. (2017). A survey on network embedding. Available at http://arxiv.org/abs/1711.08752.

de Matos, M. G., Ferreira, P., & Krackhardt, D. (2014). Peer influence in the diffusion of iPhone 3G over a large social network. MIS Quarterly, 38(4), 1103-1134..

Dahlander, L., & Frederiksen, L. (2011). The core and cosmopolitans: A relational view of innovation in user communities. Organization Science, 23(4),988-1007.

Dahlander, L., & O’Mahony, S. (2010). Progressing to the center: Coordinating project work. Organization Science, 22(4),961- 979.

Dewan, S., Ho, Y.-J. (Ian), and Ramaprasad, J. (2017). Popularity or proximity: characterizing the nature of social influence in an online music community. Information Systems Research, 28(1), 117-136.

Eagle, N., Pentland, A. S., & Lazer, D. (2009). Inferring friendship network structure by using mobile phone data. Proceedings of the National Academy of Sciences, 106(36), 15274-15278.

Faraj, S., & Johnson, S. L. (2011). Network exchange patterns in online communities. Organization Science, 22(6),1464-1480.

Flynn, F. J., Reagans, R. E., & Guillory, L. (2010). Do you two know each other? Transitivity, homophily, and the need for (network) closure. Journal of Personality and Social Psychology (99:5), 855-869.

Foss, N. j., Frederiksen, L., & Rullani, F. (2016). Problemformulation and problem-solving in self-organized communities: How modes of communication shape project behaviors in the free open-source software community. Strategic Management Journal, 37(13), 2589-2610.

Freeman, L. C. (1992). Filling in the blanks: A theory of cognitive categories and the structure of social affiliation. Social Psychology Quarterly, 55(2), 118-127.

Freeman, L. C., Romney, A. K., & Freeman, S. C. (1987). Cognitive structure and informant accuracy. American Anthropologist, 89(2), 310-325.

Gilbert, E., & Karahalios, K. (2009. Predicting tie strength with social media. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 211-220).

Greene, W. H. (2003). Econometric analysis. Pearson Education India.

Heald, M. R., Contractor, N. S., Koehly, L. M., & Wasserman, S. (1998). Formal and emergent predictors of coworkers’ perceptual congruence on an organization’s social structure. Human Communication Research, 24(4), 536-563.

Holland, P. W., & Leinhardt, S. (1977). A dynamic model for social networks. Journal of Mathematical Sociology, 5(1), 5-20.

Holland, P. W., & Leinhardt, S. (1981). An exponential family of probability distributions for directed graphs. Journal of the American Statistical Association, 76(373), 33-50.

Howison, J., Wiggins, A., & Crowston, K. (2011). Validity issues in the use of social network analysis with digital trace data.

Journal of the Association for Information Systems, 12(12), 767-797.

Hunter, D. R., Handcock, M. S., Butts, C. T., Goodreau, S. M., & Morris, M. (2008). ergm: A package to fit, simulate and diagnose exponential-family models for networks. Journal of Statistical Software, 24(3), Article nihpa54860.

Janicik, G. A., & Larrick, R. P. (2005). Social network schemas and the learning of incomplete networks. Journal of Personality and Social Psychology, 88(2), Article 348.

Johnson, R., Kovács, B., & Vicsek, A. (2012). A comparison of email networks and off-line social networks: A study of a medium-sized bank. Social Networks, 34(4), 462-469.

Johnson, S. L., Faraj, S., & Kudaravalli, S. (2014). Emergence of power laws in online communities: The role of social mechanisms and preferential attachment. MIS Quarterly, 38(3), 795-808.

Johnson, S. L., Safadi, H., & Faraj, S. (2015). The emergence of online community leadership. Information Systems Research, 26(1), 165-187.

Kane, G. C., Alavi, M., Labianca, G. J., & Borgatti, S. (2014). What’s different about social media networks? a framework and research agenda. MIS Quarterly, 38(1), 274-304.

Kilduff, M., & Brass, D. J. (2010). Organizational social network research: Core ideas and key debates. The Academy of Management Annals, 4(1), 317-357.

Krackardt, D. (1987). QAP partialling as a test of spuriousness. Social Networks, 9(2), 171-186.

Krackhardt, D. (1987). Cognitive social structures. Social Networks, 9(2), 109-134.

Krackhardt, D., & Kilduff, M. (1999). Whether close or far: Social distance effects on perceived balance in friendship networks. Journal of Personality and Social Psychology, 76(5), 770-782.

Lazer, D., Pentland, A. (Sandy), Adamic, L., Aral, S., Barabasi, A. L., Brewer, D., Christakis, N., Contractor, N., Fowler, J., Gutmann, M., Jebara, T., King, G., Macy, M., Roy, D., & Van Alstyne, M. (2009). Life in the network: The coming age of computational social science. Science, 323(5915), 721-723.

Lazer, D. M. J., Pentland, A., Watts, D. J., Aral, S., Athey, S., Contractor, N., Freelon, D., Gonzalez-Bailon, S., King, G., Margetts, H., Nelson, A., Salganik, M. J., Strohmaier, M., Vespignani, A., & Wagner, C. (2020). Computational social science: Obstacles and opportunities. Science, 369(6507), 1060-1062.

Leonardi, P., & Contractor, N. (2018). Better people analytics. Harvard Business Review. https://hbr.org/2018/11/betterpeople-analytics.

Lerner, J., & Lomi, A. (2020). Reliability of relational event model estimates under sampling: How to fit a relational event model to 360 million dyadic events. Network Science, 8(1), 97-135.

Lu, Y., Singh, P. V., & Sun, B. (2017). Is a core-periphery network good for knowledge sharing? A structural model of endogenous network formation on a crowdsourced customer support forum. MIS Quarterly, 41(2), 607-628.

Lusher, D., Koskinen, J., & Robins, G. (2012. Exponential random graph models for social networks: Theory, methods, and applications. Cambridge University Press.

McFadden, D. (1974). Conditional logit analysis of qualitative choice behavior. In P. Zarembka (Ed.), Frontiers in Econometrics (pp. 105-142). Academic.

Monge, P. R., & Contractor, N. S. (2003). Theories of communication networks. Oxford University Press.

Oinas-Kukkonen, H., Lyytinen, K., & Yoo, Y. (2010). Social networks and information systems: Ongoing and future research streams. Journal of the Association for Information Systems, 11(2),61-68.

Onnela, J.-P., Saramäki, J., Hyvönen, J., Szabó, G., Lazer, D., Kaski, K., Kertész, J., & Barabási, A.-L. (2007). Structure and tie strengths in mobile communication networks. Proceedings of the National Academy of Sciences, 104(18), 7332-7336.

Quintane, E., & Carnabuci, G. (2016). How do brokers broker? Tertius gaudens, tertius iungens, and the temporality of structural holes. Organization Science, 27(6), 1343-1360.

Quintane, E., Conaldi, G., Tonellato, M., & Lomi, A. (2014). Modeling relational events: A case study on an open source software project. Organizational Research Methods, 17(1), 23- 50.

Quintane, E., & Kleinbaum, A. M. (2011). Matter over mind? E-mail data and the measurement of social networks. Connections, 31(1), 22-46.

Singh, P. V., Tan, Y., & Mookerjee, V. (2011). Network effects: The influence of structural capital on open source project success. MIS Quarterly, 35(4), 813-829.

Smith, E. B., Brands, R. A., Brashears, M. E., & Kleinbaum, A. M. (2020). Social networks and cognition. Annual Review of Sociology, 46, 159-174.

Smith, E. B., Menon, T., & Thompson, L. (2011). Status differences in the cognitive activation of social networks. Organization Science, 23(1), 67-82.

Snijders, T. A. B., Koskinen, J., & Schweinberger, M. (2010). Maximum likelihood estimation for social network dynamics. The Annals of Applied Statistics, 4(2), 567-588.

Stadtfeld, C. (2012. Events in social networks: A stochastic actororiented framework for dynamic event processes in social networks. KIT Scientific Publishing.

Susarla, A., Oh, J.-H., & Tan, Y. (2011). Social networks and the diffusion of user-generated content: Evidence from YouTube. Information Systems Research, 23(1), 23-41.

Sweet, T. M., Thomas, A. C., & Junker, B. W. (2013). Hierarchical network models for education research hierarchical latent space models. Journal of Educational and Behavioral Statistics, 38(3), 295-318.

Treem, J. W., & Leonardi, P. M. (2013). Social media use in organizations: Exploring the affordances of visibility, editability, persistence, and association. Annals of the International Communication Association, 36(1), 143-189.

Vial, G. (2019). Reflections on quality requirements for digital trace data in IS research. Decision Support Systems, 126, Article 113133.

Wasserman, S., & Faust, K. (1994). Social network analysis: Methods and applications, Cambridge University Press.

Wooldridge, J. M. (2009). Introductory econometrics: A modern approach (4th ed.). Cengage Learning.

Wuchty, S., & Uzzi, B. (2011). Human communication dynamics in digital footsteps: A study of the agreement between self-reported ties and email networks. PloS One, 6(11), Article e26972.

Yang, M., Adomavicius, G., Burtch, G., & Ren, Y. (2018). Mind the gap: Accounting for measurement error and misclassification in variables generated via data mining. Information Systems Research, 29(1), 4-24.

## About the Authors

Aaron Schecter is an assistant professor of management information systems at the University of Georgia, Terry College of Business. He received his PhD in industrial engineering and management science from Northwestern University. Professor Schecter’s research interests include new forms of teamwork, digital innovation, and the role of artificial intelligence in the workplace. His work draws on computational social science techniques such as social network analysis, econometrics, and operations research modeling. Professor Schecter’s work has been published in outlets such as Journal of Operations Management and Organizational Research Methods, and he has received funding from the US Department of Defense and NASA.

Omid Nohadani is the director of AI and Data Science at Benefits Science Technology, developing optimization and machine learning solutions for managing and structuring risk in health plans. He was previously an associate professor at Northwestern and Purdue universities. He received his PhD in physics from the University of Southern California, was a postdoctoral researcher at the Massachusetts Institute of Technology and was a research fellow at Harvard Medical School. His research is at the intersection of optimization and machine learning to control risk in complex systems under uncertainty, with applications in healthcare, supply chain management, analytics, and technology. In particular, he studies dynamic and data-driven systems with decision makers who face complex risk requirements. Methodologically, his research is on robust optimization that is capable of improving performance by accounting for uncertainties. A number of his results have already been implemented in medical and industrial applications. He has received several research awards, including the Pierskalla Best Paper Award (2020), best paper award for IISE Transactions on Healthcare Systems Engineering (2018), and the best regional paper award of the American Association for Physicists in Medicine (2013).

Noshir Contractor is the Jane S. & William J. White Professor of Behavioral Sciences at Northwestern University. He investigates how networks form and perform. He is a Distinguished Scholar of the National Communication Association and is a Fellow of the International Communication Association, the American Association for the Advancement of Science, and the Association for Computing Machinery. He received the Distinguished Alumnus Award from the Indian Institute of Technology, Madras where he received a bachelor’s degree in electrical engineering. His PhD is from the Annenberg School of Communication at the University of Southern California.

## Appendix

## Technical Details

## Proof of Solution to Inner Problem

In order to determine the exact solution to the inner problem, we first compute the gradient of the objective function with respect to the value $\pmb { \beta } ^ { \prime } \Delta \pmb { x } _ { t q } .$ . For notational purposes, let $\begin{array} { r } { h _ { t } = \beta ^ { \prime } \big ( x _ { t y \bullet } - \Delta x _ { t y \bullet } \big ) - \log { \sum _ { z \in \mathcal { A } _ { t } } \exp \big ( \beta ^ { \prime } ( x _ { t z \bullet } - \Delta x _ { t z \bullet } ) \big ) } } \end{array}$ .

$$
\begin{array}{r l} & {\frac {\partial}{\partial (\pmb {\beta} ^ {\prime} \Delta \pmb {x} _ {t q \bullet})} (h _ {t}) = - \mathbf {1} \{q = y _ {t} \} + \frac {\exp (\pmb {\beta} ^ {\prime} (\pmb {x} _ {t q \bullet} - \Delta \pmb {x} _ {t q \bullet}))}{\sum_ {z \in \mathcal {A} _ {t}} \exp (\pmb {\beta} ^ {\prime} (\pmb {x} _ {t z \bullet} - \Delta \pmb {x} _ {t z \bullet}))}} \\ & {\quad = \left\{ \begin{array}{l l} {- 1 + \frac {\exp (\pmb {\beta} ^ {\prime} (\pmb {x} _ {t q \bullet} - \Delta \pmb {x} _ {t q \bullet}))}{\sum_ {z \in \mathcal {A} _ {t}} \exp (\pmb {\beta} ^ {\prime} (\pmb {x} _ {t z \bullet} - \Delta \pmb {x} _ {t x \bullet}))}, q = y _ {t}} \\ {\quad \quad \quad \exp (\pmb {\beta} ^ {\prime} (\pmb {x} _ {t q \bullet} - \Delta \pmb {x} _ {t q \bullet}))} \\ {\quad \quad \quad \frac {\exp (\pmb {\beta} ^ {\prime} (\pmb {x} _ {t z \bullet} - \Delta \pmb {x} _ {t z \bullet}))}{\sum_ {z \in \mathcal {A} _ {t}} \exp (\pmb {\beta} ^ {\prime} (\pmb {x} _ {t z \bullet} - \Delta \pmb {x} _ {t x \bullet}))}, q \neq y _ {t}} \end{array} \right.} \end{array}
$$

Here, ${ \bf 1 } \{ { q = y } \}$ is an indicator function, taking a value of 1 if $q = y$ and 0 otherwise. Because the value of $\frac { \exp \Bigl ( \beta ^ { \prime } \bigl ( x _ { t q } . - \Delta x _ { t q } . \bigr ) \Bigr ) } { \sum _ { z \in \mathcal { A } _ { t } } \exp \bigl ( \beta ^ { \prime } ( x _ { t z } . - \Delta x _ { t z } . ) \bigr ) }$ is nonnegative and at most 1, we can conclude that $\frac { \partial h _ { t } } { \partial ( \beta ^ { \prime } \Delta x _ { t q } . ) } \leq 0$ for $q = y$ , and $\frac { \partial h _ { t } } { \partial \left( \beta ^ { ' } \Delta x _ { t q } . \right) } \geq 0$ for all other ??. Thus, $h _ { t }$ is a monotonically decreasing function of $\pmb { \beta } ^ { \prime } \Delta \pmb { x } _ { t y } .$ and a monotonically increasing function of $\pmb { \beta } ^ { \prime } \Delta \pmb { x } _ { t z } .$ <sub>•</sub> for all $z \neq y$

## Solving the Robust Estimator

We summarize the process of determining the robust estimators in the Algorithm 1. If the step-length parameter is chosen such that it has diminishing size, i.e., $\begin{array} { r } { \sum _ { k } \alpha _ { k } = \infty , } \end{array}$ and $\alpha _ { k }  0$ as $k  \infty ,$ then the outlined procedure will converge to a locally optimal solution $\pmb { \beta } ^ { \star }$ in polynomial time (Bertsimas et al. 2010). We used a step length of $\begin{array} { r } { \alpha _ { k } = \frac { \lVert \nabla \phi \left( \beta ^ { ( 0 ) } \right) \rVert } { k } . } \end{array}$

## Algorithm 1:

1. Initialize with an estimator $\pmb { \beta } ^ { ( 0 ) }$ . Set $k = 0$

2. Solve the inner problem for all $t = 1 , \dots , M$ to obtain the optimal errors $\Delta x _ { t z \bullet } ^ { \star } \big ( \pmb { \beta } ^ { ( k ) } \big )$ for each $z \in \mathcal { A } _ { t }$

3. Using the worst case errors $\Delta \mathbf { X } ^ { \star } \big ( \pmb { \beta } ^ { ( k ) } \big )$ , calculate $\phi \big ( \pmb { \beta } ^ { ( k ) } ; \mathbf { X } ^ { o b s } \big ) = \psi \left( \pmb { \beta } ^ { ( k ) } ; \mathbf { X } ^ { o b s } - \Delta \mathbf { X } ^ { \star } \big ( \pmb { \beta } ^ { ( k ) } \big ) \right)$ . By applying Danskin’s theorem, we know that computing $\nabla \psi \big ( \pmb { \beta } ^ { ( k ) } \big )$ is equivalent to computing $\nabla \phi \big ( \pmb { \beta } ^ { ( k ) } \big )$ (Bertsimas and Nohadani, 2019). If the gradient does not exist, compute a subgradient. Denote the gradient or subgradient as $g .$

4. Update ${ \pmb \beta } ^ { ( k + 1 ) } = { \pmb \beta } ^ { ( k ) } + \alpha _ { k } g$ , where $\alpha _ { k }$ is a step-length parameter.

5. Stop when the relative change in objective function is less than $\epsilon , \epsilon > 0$ is a stopping criterion. Otherwise, $k = k + 1$ and return to Step 2.

## Computation of the Subgradient

To solve the robust maximum likelihood problem, the gradient of the outer problem—assuming a known solution to the error terms $\Delta x ^ { \star } ( \beta ) \cdot$ —must be computed. We assume that the norm $\| \bullet \|$ refers to the Euclidean norm. For our specified likelihood function, the gradient is as follows:

$$
\begin{array}{r l} & {\nabla \phi_ {p} (\pmb {\beta}) = \frac {\partial}{\partial \beta_ {p}} \Bigg (\sum_ {t = 1} ^ {M} \pmb {\beta} ^ {\prime} x _ {t y \bullet} ^ {\mathrm{net}} - \| \pmb {\beta} \| \rho - \log \sum_ {z \in \mathcal {A} _ {t}} \exp (\pmb {\beta} ^ {\prime} x _ {t z \bullet} ^ {\mathrm{net}} + (- 1) ^ {u _ {z}} \| \pmb {\beta} \| \rho) \Bigg)} \\ & {\quad = \sum_ {t = 1} ^ {M} x _ {t y p} ^ {\mathrm{net}} - \frac {\beta_ {p}}{\| \pmb {\beta} \|} \rho - \frac {\sum_ {z \in \mathcal {A} _ {t}} \left(x _ {t z p} ^ {\mathrm{net}} + (- 1) ^ {u _ {z}} \frac {\beta_ {p}}{\| \pmb {\beta} \|} \rho\right) \exp (\pmb {\beta} ^ {\prime} x _ {t z \bullet} ^ {\mathrm{net}} + (- 1) ^ {u _ {z}} \| \pmb {\beta} \| \rho)}{\sum_ {z \in \mathcal {A} _ {t}} \exp (\pmb {\beta} ^ {\prime} x _ {t z \bullet} ^ {\mathrm{net}} + (- 1) ^ {u _ {z}} \| \pmb {\beta} \| \rho)}} \end{array}
$$

In the case that the vector ${ \pmb \beta } = { \pmb 0 }$ , then the gradient cannot be directly computed. Instead, we may compute a subgradient. Given the convexity of the norm, the logarithmic function, and the exponential function, and that the objective function is the negation of these functions, we may conclude that the log-likelihood function for the robust problem is concave. As such, the subgradient is a vector ?? that satisfies the following inequality

$$
\psi \big (\pmb {\beta} _ {2}; \mathbf {X} ^ {\mathrm{net}} - \Delta \mathbf {X} ^ {\star} (\pmb {\beta} _ {2}) \big) - \psi \big (\pmb {\beta} _ {1}; \mathbf {X} ^ {\mathrm{net}} - \Delta \mathbf {X} ^ {\star} (\pmb {\beta} _ {1}) \big) \leq \pmb {v} \cdot (\pmb {\beta} _ {2} - \pmb {\beta} _ {1}).
$$

Thus, the subgradient used in the optimization of the outer objective function is as follows:

$$
g (\boldsymbol {\beta}) = \left\{ \begin{array}{c} \nabla \phi (\boldsymbol {\beta}), \boldsymbol {\beta} \neq \mathbf {0} \\ \boldsymbol {v}, \boldsymbol {\beta} = \mathbf {0}. \end{array} \right.
$$

## Computation of the Hessian Matrix

The robust standard errors for the estimator are derived from the inverse information matrix at the optimal solution. To obtain this matrix we require the matrix of second derivatives of the likelihood function, i.e., the Hessian. We proceed to take the derivative of the subgradient as defined previously.

$$
\begin{array}{r l} & {\nabla^ {2} \phi_ {p q} (\pmb {\beta}) = \frac {\partial^ {2}}{\partial \beta_ {p} \partial \beta_ {q}} \Bigg (\sum_ {t = 1} ^ {M} \pmb {\beta} ^ {\prime} x _ {t y _ {\bullet}} ^ {\mathrm{net}} - \| \pmb {\beta} \| \rho - \log \sum_ {z \in \mathcal {A} _ {t}} \exp (\pmb {\beta} ^ {\prime} x _ {t z _ {\bullet}} ^ {\mathrm{net}} + (- 1) ^ {u _ {z}} \| \pmb {\beta} \| \rho) \Bigg)} \\ & {\quad = \frac {\partial}{\partial \beta_ {q}} \Big (\nabla \phi_ {p} (\pmb {\beta}) \Big)} \\ & {\quad = \sum_ {t = 1} ^ {M} - \mathbb {I} [ p = q ] + \frac {\beta_ {p} \beta_ {q}}{\| \pmb {\beta} \| ^ {3}} - \frac {A}{C} + \frac {B}{C ^ {2}}} \end{array}
$$

The values $A , B ,$ and ?? above are simply placeholders for more complex expressions. Below, we provide the equations for each. Note that ??[… ] is the indicator function.

$$
\begin{array}{r l} & A = \sum_ {z \in \mathcal {A} _ {t}} \left[ \exp (\pmb {\beta} ^ {\prime} \pmb {x} _ {t z \bullet} ^ {\mathrm{net}} + (- 1) ^ {u _ {z}} \| \pmb {\beta} \| \rho) \left(x _ {t z p} ^ {\mathrm{net}} x _ {t z q} ^ {\mathrm{net}} + \frac {\beta_ {q}}{\| \pmb {\beta} \|} \rho + (- 1) ^ {u _ {z}} \left[ x _ {t z p} ^ {\mathrm{net}} \frac {\beta_ {q}}{\| \pmb {\beta} \|} \rho + x _ {t z q} ^ {\mathrm{net}} \frac {\beta_ {p}}{\| \pmb {\beta} \|} \rho + \mathbb {I} [ p = q ] - \frac {\beta_ {p} \beta_ {q}}{\| \pmb {\beta} \| ^ {3}} \right]\right) \right] \\ & B = \sum_ {z \in \mathcal {A} _ {t}} \left[ \exp (\pmb {\beta} ^ {\prime} \pmb {x} _ {t z \bullet} ^ {\mathrm{net}} + (- 1) ^ {u _ {z}} \| \pmb {\beta} \| \rho) \left(x _ {t z q} ^ {\mathrm{net}} + (- 1) ^ {u _ {z}} \frac {\beta_ {q}}{\| \pmb {\beta} \|} \rho\right) \right] \\ & C = \sum_ {z \in \mathcal {A} _ {t}} \exp (\pmb {\beta} ^ {\prime} \pmb {x} _ {t z \bullet} ^ {\mathrm{net}} + (- 1) ^ {u _ {z}} \| \pmb {\beta} \| \rho) \end{array}
$$
