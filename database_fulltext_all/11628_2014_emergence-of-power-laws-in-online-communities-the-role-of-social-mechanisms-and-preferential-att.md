---
otero_id: 11628
otero_key: "2YF2KDJ2"
title: "Emergence of Power Laws in Online Communities:  The Role of Social Mechanisms and Preferential Attachment"
authors: "Steven L. Johnson; Samer Faraj; and Sri Kudaravalli"
year: "2014"
journal: "MIS Quarterly"
doi: "10.25300/misq/2014/38.3.08"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# EMERGENCE OF POWER LAWS IN ONLINE COMMUNITIES: THE ROLE OF SOCIAL MECHANISMS AND PREFERENTIAL ATTACHMENT<sup>1</sup>

Steven L. Johnson Fox School of Business, Temple University, Philadelphia, PA 19122-6083 U.S.A. {steven@temple.edu}

Samer Faraj Desautels Faculty of Management, McGill University, Montreal, Quebec H3A 1G5 CANADA {samer.faraj@mcgill.ca}

Srinivas Kudaravalli HEC Paris,1, rue de la Liberation, 78351 Jouy en Josas Cedex FRANCE {kudaravalli@hec.fr}

Online communities bring together individuals with shared interest in joint action or sustained interaction. Power law distributions of user popularity appear ubiquitous in online communities but their formation mechanisms are not well understood. This study tests for the emergence of power law distributions via the mechanisms of preferential attachment, least efforts, direct reciprocity, and indirect reciprocity. Preferential attachment, where new entrants favor connections with already popular participants, is the predominant explanation suggested by prior literature. Yet, the attribution of preferential attachment or any other mechanism as a single unitary reason for the emergence of power law distributions runs contrary to the social nature of online communities and does not account for diversity of participants’ motivation. Agent-based modeling is used to test if a single social mechanism alone or multiple mechanisms together can generate power law distributions observed in online communities. Data from 28 online communities is used to calibrate, validate, and analyze the simulation. Simulated communication networks are randomly generated according to parameters for each hypothesis. The fit of the power law distribution in the model testing subset is then compared against the fit for these simulated networks. The major finding is that, in contrast to research in more general network settings, neither preferential attachment nor any other single mechanism alone generates a power law distribution. Instead, a blended model of preferential attachment with other social network formation mechanisms was most consistent with power law distributions seen in online communities. This suggests the need to move away from stylized explanations of network emergence that rely on single theories toward more highly socialized and multitheoretic explanations of community development.

Keywords: Online communities, scale-free, power law distribution, preferential attachment, social exchange, reciprocity, simulation

## Introduction

In recent years, online communities have emerged as a novel organizational form that differs from markets or hierarchies in their ability to bring together individuals with shared interest in joint action or sustained interaction. Online communities form when people rely upon social media to communicate with others with similar interests. They are highly dependent on the evolving IT infrastructure and have progressed from pre-Web bulletin board and Usenet technologies to more sophisticated social networking platforms. Millions of people participate daily in thousands of online communities where their interactions generate new knowledge and learning (Faraj et al. 2011; Rheingold 2000; Tapscott and Williams 2006).

With the development of the field of network science, researchers have established that many complex physical, biological, informational, and social systems follow similar network structures characterized by power law distributions (see Barabasi 2009; Newman 2003; Newman et al. 2006). Instead of following a normal distribution, these networks often follow a scale-free distribution of links where a few participants have an extremely high number of relationships to other participants and most participants have very few. Although there are many different theories for power law formation, the most prominent explanation is the Barabási and Albert (1999) model of preferential attachment. In fact, this model is so well established that the mere existence of a power law is sometimes seen as suggesting preferential attachment (e.g., Barabási 2012; Kwon et al. 2007; Ravid and Rafaeli 2004).

Early Internet researchers have focused on the egalitarian potential of the Internet and suggestions were put forth to eliminate participation inequalities (e.g., DiMaggio et al. 2001; Kraut 2003). Alternatively, the existence of power law distributions has also been viewed uncritically as a sustaining feature of online settings (Shirky 2008) or one that could simply lead most web knowledge to remain hardly accessed (Benkler 2006).

The goal of this paper is to further understand how power law distributions form in online community participation. What base interactions and linking mechanisms result in the generation of power law structures? Is it, as network scientists imply, that many forms of physical, biological, and human networks follow a power law distribution because of a unitary mechanism like preferential attachment, where new entrants prefer to link to more visible others: “based on information that is biased toward the more visible (richer) vertices [participants] irrespective of the nature and origin of this visibility” (Barabási and Albert 1999, p. 512)? Or, is it as organizational and social scientists offer, that a multiplicity of socialized explanations are needed to encompass the diversity of online human behavior (Andriani and McKelvey 2009; Faraj and Johnson 2011)? Understanding formation of uneven distribution has relevance not only to theories of online participation and community management but also to broader aspects of organizing and innovating in complex settings.

## Literature Review

Given that many technology-enabled communication networks follow power law distributions (Andriani and McKelvey 2009), it is important to establish their formation mechanisms. Much of online community research focuses on the factors that affect individual participation online. Motivations for individual online participation include access to information, advice seeking, experimentation, reputation building, expertise signaling, altruism, empathy, reciprocity, bonding with others, and commitment to community goals (Bateman et al. 2011; Kankanhalli et al. 2005; Kudaravalli and Faraj 2008; Lakhani and von Hippel 2003; Peddibhotla and Subramani 2007; Preece 2000; Ren et al. 2007; Wasko and Faraj 2005).

Over the last decade, empirical evidence collected in multiple ways across multiple settings has consistently shown that online communication and participation is highly skewed with a relatively small number of participants responsible for most interactions and knowledge production. For example, popularity of websites, email recipients, user-generated content, online social networks, blogs, and online communities follow a power law distribution (Adamic et al. 2003; Adamic and Huberman 2000; Faraj and Johnson 2011; Faraj et al. 2008; Kumar et al. 2010; Raban and Rabin 2009; Ravid and Rafaeli 2004; Shirky 2008; Wu et al. 2004). Power laws, also referred to as a Pareto or scale-free distribution, are typically calculated based on the rank/frequency distribution of indegree.<sup>2</sup> The Pareto (type 1) distribution is the most widely used power law distribution with scale-free properties (see Barabási and Albert 1999; Newman 2003) and serves the basis of most research on network structure.

Structural characteristics of an online community reflect accumulated behaviors of individual participants. People do not act randomly but rather, behave in response to shared motivations, practices, and technology that lead to the emergence of structural regularities (Monge and Contractor 2003). Structure matters because it both shapes and reflects behavior (Orlikowski and Iacono 2001). Identifying causes leading to power law distributions sheds light on individual-level actions, community-level dynamics, and technology affordances. Indeed, Barabási (2009) suggests that network science needs to now turn to understanding the processes that occur on networks and that shape their structure. Similarly, organizational scholars call upon a focus on discovering the mechanisms that drive network outcomes and to formulate the processes behind their emergence and evolution (Ahuja et al. 2002; Zaheer and Soda 2009). Indeed, the exploration of the underlying mechanisms that lead to the emergence of the power law structure suffers from a surprising lack of investigation. The almost tautological explanation, that new participants in such a network “choose” to attach to popular participants to create the visible structure, is seriously lacking in explanatory power because the economic or social mechanisms are left unspecified. It is becoming clear that sorting out the tangled effect of inter-related mechanisms is difficult to develop in the correlational framework typical in crosssectional network studies. For example, disentangling the effect of homophily and peer influence in networks is difficult in that they are historically co-occurring. This creates an identification problem in the form of endogeneity and thus requires using alternative methodologies or creative sample matching (Aral et al. 2009; Sundararajan et al. 2013).

One way to avoid identification issues like endogeneity is to use simulation-based theorizing. The approach entails starting with an outcome (in this case, the network in its current form) and relying on hypothesized but unobserved theoretical mechanisms to derive an evolutionary process that can lead to results close to the current data (Borgatti and Halgin 2011; Lave and March 1975). Thus, through specification of a computational model via building and testing a simulation, researchers can evaluate which mechanisms, alone or together, are operant and can test how closely results replicate the observed network data. The model is a formal (algorithmic) specification of rules, equations, parameters, and organizing principles that provide a framework for testing explanations of how organizational entities evolve over time from base principles (Burton and Obel 2011). Simulation modeling provides a powerful methodology for analyzing interdependent mechanisms operating concurrently but whose influence is difficult to disentangle. The simulation, often labeled virtual experiment to differentiate it from field experiments, starts with initial conditions, uses formal specifications, and generates results over a period of time. It provides insight in the working of complex systems, allows the evaluation of theoretical assumptions, and thus can be theory generative (Davis et al. 2007; Harrison et al. 2007; Lazer et al. 2009).

This paper uses simulation to investigate the formation of online communities and to explore how power law distributions emerge. Knowing what formation mechanisms, alone or in combination, lead to an observed network characteristic sheds light on what assumption, theories, and implications are most relevant to that network context. While most empirical work on online communication is based on trace data generated from the archival record of participant interactions (Howison et al. 2012; Monge and Contractor 2003), we chose to use simulation as a way to test theory. Building on classic network science models of preferential attachment in the form of participant in-degree (see Barabási and Albert 1999; Newman 2003), this paper evaluates to what extent the dominant mechanism of preferential attachment is operant in the realm of online community and contrasts its influence to a richer model based on multiple theories of social interaction.

The main thrust of this research is testing if one single mechanism alone or multiple network formation mechanisms together is more consistent with online community network generation. On one hand, the dominant explanation of preferential attachment assumes that participants in a network are aware of and motivated by the relative popularity of all other network participants. It posits a single motivation for all participants whereby any two participants sharing structurally equivalent network positions also share identical behavioral propensities. Alternatively, other social exchange mechanisms assume that participants are motivated by the history of egocentric and dyadic exchanges. For example, indirect exchange is a response to inbound communication and direct exchange is a response to the history of communication between two participants. There is an assumption of participation heterogeneity with the relative influence of mechanisms varying both for a single participant over time as well as for structurally equivalent participants at any given time. Recent empirical work focusing on fitting exponential random graph (p\*) models to data from 5 online communities over 27 months has shown that patterns based on both preferential attachment and reciprocity were present (Faraj and Johnson 2011). However, the study did not establish how observed structural patterns developed, either through a single mechanism or via multiple mechanisms together.

In summary, network formation mechanisms matter for understanding expected outcomes, for focusing research attention, and for directing practice. The next section proposes hypotheses for models of single and multiple mechanisms. The hypotheses are tested through agent-based simulation based on empirical observation of actual online communities.

## Models of Online Community Formation

The primary research question of this paper is to identify the network generation mechanisms that, either individually or in combination, lead to power law distributions observed in online communities. As such, an important research step is to choose which mechanisms to test. Although preferential attachment has received the most attention (as described in Table A4 in Appendix A), there are dozens of mechanisms known to generate power law distributions (Andriani and McKelvey 2009; Monge and Contractor 2003). Most of these mechanisms, however, are associated with physical, economic or biological processes rather than social ones.

It is beyond the scope of a single paper to exhaustively consider all mechanisms that may generate power law distributions or all motivations identified for participation online. Four major network formation mechanisms were selected either because they are social mechanisms known to generate power law distributions in measures of communication (e.g., preferential attachment and least efforts) or because they have been empirically observed in online communities (e.g., direct reciprocity and indirect reciprocity). Preferential attachment is the tendency of network participants to form relationships with the most popular members of the network (Barabási and Albert 1999; Merton 1968). Least effort reflects that some participants require less effort to form relationships than others (Zipf 1949). Direct reciprocity is the tendency of any two participants (a dyad) to maintain mutuality in their relationship (see Wasserman and Faust 1994). Indirect reciprocity is the tendency of a participant to maintain symmetry in their relationship with the community (see Wasserman and Faust 1994).

## Single Mechanism Model

The preponderance of explanations for the formation of power law distributions consider single generation mechanisms operating at a time (Andriani and McKelvey 2009). Indeed, such is the popularity of unitary explanations that after Barabási and Albert (1999) proposed preferential attachment as the primary mechanism for the formation of scale-free networks, power law distributions in online settings are often attributed to preferential attachment (Barabási 2012; Kwon et al. 2007; Ravid and Rafaeli 2004). An illustrative example is this discussion of the formation of online networks:

There is cumulative advantage: The more connections you have, the more you get. The distribution often follows what mathematicians call a “power law.” This is a variation on what sociologist Robert K. Merton called the “Matthew effect”: The rich get richer and the poor get poorer (Rainie and Wellman 2012, pp. 48-49).

Preferential attachment occurs when “given newly arriving agents into a system, larger nodes with an enhanced propensity to attract agents will become disproportionately even larger” (Andriani and McKelvey 2009, p. 1058). The underlying cause for the emergence of a power law distribution is positive feedback whereby small initial differences in popularity “will mutually interact so as to spiral up to produce long-tailed distributions” (Andriani and McKelvey 2009, p. 1059). Two key conditions for preferential attachment are (1) an open system with new entrants, and (2) new entrants being aware of and acting on the preferences of existing participants (Barabási and Albert 1999). A critical requirement of preferential attachment is that new entrants can observe and learn the cumulative past preferences of existing network participants. In online communities, participants often read messages for extended periods of time before posting their first message (Preece et al. 2004). Many online communities make extensive archives of past messages available to new members for viewing. Also, online communities frequently display status indicators (e.g., join date, number of messages posted, reputation earned, membership levels) that further signal participant popularity. In summary, we propose

## H1a: The single network formation mechanism of preferential attachment leads to the formation of power law distributions in the participant in-degree in online communities.

Next we turn our attention to the social network formation mechanisms of least efforts, direct reciprocity, and indirect reciprocity. The theory of least effort was originally proposed to explain the power law rank/frequency distribution of language usage (Andriani and McKelvey 2009; Zipf 1949). At the start of a new community, no one yet knows what message characteristics are the most likely to be popular. Nonetheless, not all participants are equally likely to exhibit these characteristics. For example, participants with more experience in similar settings, more time to participate, or a greater interest in the online community topic may be more apt to generate more popular content. Least effort has been generalized beyond language usage and has found support in multiple organizational settings, predominantly in a context of change (Dahui et al. 2005; Ishikawa 2006) The initial formation of a new online community is a period of organizational change.

Multiple theories support the importance of reciprocity in online communities. Social exchange theory (e.g., Blau 1964)

suggests that as people share knowledge resources with one another, obligations for future exchange are created. Providing help with an expectation of receiving future aid in return binds the giver and receiver together in a reciprocal gift exchange (Fulk et al. 1996; Kollock 1999). Direct reciprocity is a motivation for user participation in online communities (Constant et al. 1996; Lakhani and von Hippel 2003).

Indirect reciprocity is the tendency to contribute back to a group (as opposed to specific individuals) in proportion to what is received. It arises when participants receive an exchange and “pay it forward” to someone other than the giver. Indirect reciprocity is a form of generalized exchange that emphasizes how receiving exchanges impacts the propensity to make further exchanges with a group as a whole. It is likely to emerge in settings where expertise is unevenly distributed and identification with a group is high, both conditions found in online communities. Altruistic norms, social solidarity, and willingness to help others have all been identified in online communities (Rheingold 2000; Sproull and Arriaga 2007; Wasko and Faraj 2000). Indirect reciprocity is consistent both with the observation of altruistic participation motivations in knowledge-intensive online communities (Kankanhalli et al. 2005), as well as the best practice in online communities of experienced members welcoming new participants (Joyce and Kraut 2006). Based on the evidence supporting the existence of these three mechanisms in online communities, we propose

H1b: As a single network formation mechanism, least efforts, direct reciprocity, or indirect reciprocity lead to the formation of power law distributions in the participant in-degree in online communities.

## Multiple Mechanism Model

In contrast to the support for a single network formation mechanism, online community research has identified a wide range of participation motivations and network participation patterns. Indeed, it seems unlikely that human motivation and behavior, whether face-to-face or online, could be explained via a single social mechanism. The multitheoretical multilevel perspective recognizes that multiple motivations will be present in the same network at the same time (Contractor et al. 2011; Monge and Contractor 2003). Further, rather than being merely a single set of closely related theories of communication network formation, there are multiple families of theories of network emergence including theories of selfinterest, exchange, collective action, and homophily. Indeed, there is strong empirical evidence for multiple online community motivations. For example, a survey of an online forum for legal professionals, Wasko and Faraj (2005) found that participants both wanted to improve professional reputations (self-interest) and also believed in norms of reciprocity (collective action). Investigating motivations to participate at an online writing forum, Lampe et al. (2010) found that individual- and organizational-oriented motivations to participate changed over time. Specifically, motivations to continue participation differed from initial motivations to contribute. In a network analysis of 27 months of communication history in five online forums, Faraj and Johnson (2011) found empirical support for both direct and indirect reciprocation in network structures.

It is certainly a compelling idea that the emergence of a complex network property can be attributed to a single participant-level mechanism. Nonetheless, this simplification runs counter to theoretical and empirical evidence of the heterogeneity of online community participant motivations. In contrast, in a blended model, multiple network formation mechanisms are present and operate simultaneously.

H2: A blend of multiple network formation mechanisms including preferential attachment, least effort, direct reciprocity, and indirect reciprocity leads to the formation of power law distributions in the participant indegree in online communities.

## Research Method

A great deal of research in network theory is analytical. However, analytical models are generally appropriate for instances when a small number of network participants make a problem tractable or when the rules of model construction can be specified in a deterministic way (Watts 1999). Computational models provide precision in phenomena representation, openness to unanticipated solutions, and the ability to represent a variety of mechanisms and formulations. Building simulations of computational models enables the exploration of complex network mechanisms and emergent outcomes. Compared to field or laboratory studies, computational models allow the representation and testing of a broader set of social systems while being less noisy, easier to organize, and capable of representing a broader and more complex set of theories (Carley and Lin 1997; McKelvey 2002). Compared to analytical models, they avoid the need to make simplifying mathematical assumptions for the sake of generating a tractable solution (Adner et al. 2009). Thus, computational models offer an effective way to advance theory because of their ability to represent complex social processes and to validate them against an empirical context.

This paper studies communication networks formed via participants in online communities supported by threaded discussion forums. The proposed hypotheses were tested with an agent-based simulation modeling the first year of an online community formation. Figure 1 depicts the research method (a more detailed description appears in Appendix A). There were four major steps: (1) collecting observation data and trace data from online communities; (2) developing an agentbased simulation model; (3) generating simulation data, validating it, and preparing a calibrated analysis sample; and (4) performing statistical tests to compare the estimated power law distribution fit of the analysis sample to the model testing sample.

![](/api/attachments/2YF2KDJ2/fulltext/images/86f1565f3cf9e14603c3e6ef18bb77594ed593226a3e175d4f992ba364bb23f6.jpg)  
Figure 1. Four Major Steps in Research Method with Types of Research Data

The first major step was to collect observational and trace data from online communities. Several hundred threaded discussion forums were informally observed. These online communities were identified using Yahoo! Search for the strings “Powered by vBulletin” and “software” to find technology-related discussion forums. The observational data was used to create a descriptive model of online community formation. The sample was further reduced to include only online communities where a full archive of the initial 15 months of posting history was available. An automated program was used to gather the first 15 months of communication for 28 randomly selected online communities. One third of the sample was randomly selected as a model specification sample (n = 9) and the remaining held out as a model testing sample (n = 19).<sup>3</sup> A larger subsample was assigned to the model testing sample to increase statistical power for hypothesis testing (Cohen 1992).

The next major step of the research method was to develop the simulation. The descriptive model developed in the first step was further developed as a formal network formation model. Where appropriate, the first 12 to 15 months of data from the model specification sample provided key simulation parameters. For example, the first year of data was used to estimate participant arrival rates and the first 15 months of data to estimate participant departure rates. By expressing key behaviors and rules in mathematical formulas, the formal model provided a detailed road map for implementing the agent-based model of network creation in the programming language of R. (The formal model and a pseudocode representation of the simulation are both provided in Appendix A.)

<table><tr><td colspan="3">Table 1. Measures Used for Validation, Calibration, and Testing</td></tr><tr><td>Step</td><td>Sample</td><td>Measures</td></tr><tr><td>Validate Model</td><td>Model Specification Sample</td><td>Est. Power Law Distribution Coefficient (b)Est. Power Law Distribution Fit ( $R^{2}$ )</td></tr><tr><td>Calibrate Model</td><td>Model Specification Sample</td><td>Thread DepthGraph DensityClustering Coefficient (Transitivity)</td></tr><tr><td>Test Hypotheses</td><td>Model Testing Sample</td><td>Est. Power Law Distribution Fit ( $R^{2}$ )</td></tr></table>

The third major step of the research method is to use the implemented simulation code to generate data to test the proposed hypotheses. Data was generated with parameters specific to each hypothesis, the entire set of generated data was compared to the model specification sample to establish that the simulation encompasses an appropriate range of networks, and then the simulation model was calibrated to create an analysis sample.

To test H1a, 40 networks were generated via the rules in the formal model for online community formation with only preferential attachment. Likewise, H1b was tested with 40 networks each for the mechanisms of least efforts, direct reciprocity, and indirect reciprocity. To test H2, 1,000 networks were generated using blends of preferential attachment and the three other network formation mechanisms. In a blended model multiple mechanisms are present during network formation. Weights were identified for each network formation mechanism and remain constant for that simulation run. The weights to test were chosen with a Monte Carlo method (see Law and Kelton 2000). A random number was chosen for each of the four mechanisms and then a percentage of total (0%–100%) was calculated for each mechanism. For each simulated day, an active agent was assigned a single network formation mechanism based on the weights for that simulation run.

With multiple input parameters, an agent-based simulation can create a nearly infinite variety of outputs. Model validation and calibration is a critical step to ensure that generated data is representative of a theoretically and practically meaningful range of observations (see Table 1 for measures). The model validation step provides confidence in the external validity of the simulation. For all 1,160 simulated networks and the 9 online communities in the model specification sample, the following values were calculated to validate the model: an estimated power law distribution degree (b) and power law distribution fit (R<sup>2</sup>). Appendix B provides detailed steps for estimating these values. The simulation model did indeed generate networks that cover the empirical range of the model specification sample for these values.

The model calibration step identifies the most appropriate simulation configurations to analyze. First, thread depth was used as a simulation input parameter to facilitate creation of networks of a similar size as those comprising the specification sample. Second, the generated networks were filtered to retain only those with structural similarities to the Model Specification sample. The two network properties of clustering coefficient and graph density were used for this purpose (Barrat et al. 2004; Wasserman and Faust 1994). Blends with at least 75 percent of the results falling between the minimum and maximum values of the model specification sample for both measures were retained for further analysis. It is important to note that the parameters for filtering were (1) drawn from the model specification sample and (2) are conceptually and empirically separate from the outcome of interest in hypothesis testing.

The final major activity of the research method is the analysis step: calculating outcome measures and statistical results to test hypotheses. The estimated power law distribution R<sup>2</sup> fit was calculated both for the 19 online communities in the model testing sample as well as for the calibrated simulation runs comprising the analysis sample.<sup>4</sup> Support is found for a hypothesis if there is no statistically significant difference between the model testing sample and the calibrated simulation runs associated with that hypothesis in a two-tailed ANOVA test.

<table><tr><td colspan="4">Table 2. Average Values for Model Testing Subsample and Simulation Results</td></tr><tr><td>Measure</td><td>Model Testing Sample</td><td>H1a: Preferential Attachment</td><td>H2: Blend of Social Mechanisms</td></tr><tr><td>Observations</td><td>19</td><td>40</td><td>78</td></tr><tr><td>Average of Power Law Distribution Fit R2</td><td>0.944</td><td>0.895</td><td>0.933</td></tr><tr><td>Standard Deviation of Power Law Distribution Fit R2</td><td>0.030</td><td>0.029</td><td>0.024</td></tr><tr><td>Comparison: simulation results vs. model testing sample</td><td></td><td>F = 34.91, p &lt; .0001</td><td>F = 2.98, p &gt; .05</td></tr><tr><td>Interpretation</td><td></td><td>Model testing sample and calibrated H1 simulation runs are from different populations</td><td>Model testing sample and calibrated H2 simulation runs are from the same population</td></tr><tr><td>Conclusion</td><td></td><td>H1a not supported</td><td>H2 supported</td></tr></table>

Note: As none of the networks generated to test H1b met the calibration criteria, not support is found for H1b.

## Results

Results for H1a are presented in Table 2. For the model testing subsample (n = 19) the average power law distribution R<sup>2</sup> fit is 0.944 (s.d. = 0.030). For the test of the preferential attachment mechanism (H1a), the average for the simulation runs (n = 40) is 0.895 (s.d. = 0.029). This is statistically significantly different than the average for the model testing subsample (F = 34.91, p < .001). This is evidence that the networks generated by the preferential attachment mechanisms alone are drawn from a different population than the observed online communities in the model testing subsample. In the test of H1b, all of the generated networks failed to meet the calibration criteria. The networks generated with least efforts, direct reciprocity, or indirect reciprocity as a single mechanism did not fall within the range of observed networks for the calibration measures of thread depth, graph density, or clustering coefficient. Thus, no support is found for H1a or H1b.

For the test of the blended model of social mechanisms (H2), the average power distribution fit (n = 78) is 0.933 (s.d. = 0.024). The results of the test show no statistically significant difference between the blended calibrated models and the model testing subsample (F = 2.98, p > 0.05). This is evidence that the calibrated networks formed through a blended model of multiple social mechanisms are drawn from the same population as the observed online communities. Thus, support is found for H2.

In summary, we used the following research design to test hypotheses regarding how network formation mechanisms can generate power law distributions in online communities. First, we collected observation and trace data from a sample of 28 communities (split into a model specification sample and a model testing sample). Next, we developed a formal model, coded that model as an agent-based simulation, and identified simulation input parameters from the model specification sample. Third, we generated data with the computerbased simulation. The generated data was validated and calibrated with the model specification sample to generate an analysis sample (see Table 1). No networks testing H1b met the calibration criteria; therefore, the analysis sample includes networks generated via preferential attachment (for H1a) and a blended model of multiple mechanisms (for H2). Finally, we compared (using an ANOVA test) the analysis sample to the (hold-out) model testing sample. The findings of the H1a ANOVA test are that networks in the analysis sample generated by preferential attachment have power law distribution fits that differ from the model testing sample. The H2 ANOVA test finds no statistically significant difference in the power law distribution fits when comparing calibrated networks generated with a blended model to the model testing sample. Thus, we conclude that, in a simulation of online community network generation, preferential attachment alone does not generate networks similar to actual online communities. Networks generated with a blended model do generate networks that are similar to actual online communities.

To gain a better understanding of how the blended mechanisms combine to form power law distributions, Figure 2 shows the relative weights for the calibrated simulation runs. A commonality among the four is that the weight for preferential attachment is around 50 percent. Otherwise, the calibrated blends feature a large presence (> 5%) of at least two of the other three mechanisms. This further supports the conclusion of H2 that a combination of preferential attachment along with other social mechanisms is a necessary condition for power law distributions in the formation of communication networks in online communities.

![](/api/attachments/2YF2KDJ2/fulltext/images/76c91415fe636b6b6e303fabf0b3e4467979964fefd402745e0648e8e5669f9e.jpg)  
Figure 2. Mechanism Weights for Calibrated Blended Simulation Runs

## Discussion

In the emergent field of network science, preferential attachment has been offered as the predominant structuring mechanism applying to a broad range of physical, biological, and social domains (Barabási and Albert 1999; Newman 2003). The power law distributions observed in online settings are frequently attributed to preferential attachment (Barabási 2012; Kwon et al. 2007; Rainie and Wellman 2012; Ravid and Rafaeli 2004). In contrast, research on why people contribute to online communities identifies multiple mechanisms for network formation (Bateman et al. 2011; Kankanhalli et al. 2005; Kudaravalli and Faraj 2008; Lakhani and von Hippel 2003; Peddibhotla and Subramani 2007; Preece 2000; Ren et al. 2007; Wasko and Faraj 2005). This paper answers the call for a multitheoretical approach to further understand the mechanisms that underlie online community participation dynamics (Butler 2001; Contractor et al. 2011; Faraj and

Johnson 2011; Monge and Contractor 2003). Our major finding is that networks formed with a blend of preferential attachment with other social mechanisms are more consistent with the power law distributions found in online communities than networks formed by any single mechanism alone. This finding has implications for theories of online community development, for successfully building or moderating online communities, and for network formation mechanisms more broadly in social sciences.

## Implications for Online Community Theory

This finding adds to the broader research program on online community dynamics. Research attention has been directed to the management of online community boundaries when members are easily mobile and attracting new members is a goal (Wang et al. 2013). Beyond the awareness that participation and engagement in online communities is highly uneven, there is a growing interest in understanding the role played by the high activity core (Kuk 2006; Preece and Shneiderman 2009). Early empirical evidence indicates that different social mechanisms such as reciprocity can serve as an explanation for the complex interaction dynamics (Faraj and Johnson 2011). Promising developments include information flow through digital networks where emergent evidence points to the importance of interactions in influencing others (Aral et al. 2009; Sundararajan et al. 2013). Yet, to go beyond the perspective of participation as a popularity contest requires the elucidation of network tie formation and a nuanced understanding of interpersonal and group dynamics—a more complex research agenda than simply statically describing the structure of an online network.

Given the recent interest in how selection or interaction mechanisms can result in power laws (Andriani and McKelvey 2009), our study is generative and supportive of novel modeling approaches that carefully spell out the development and impact of social ties. Among the promising approaches are looking at the impact of “friend of friend” relationships to explain network evolution (Wong and Boh 2010), assortative mixing where similar participant characteristics lead to social connections (Aral et al. 2009), and attract and introduce models of behavior spread (Fowler et al. 2009). Also, organizational researchers looking at alliance formations have started to offer more complex and contextually embedded explanations of why organizations link to each other (Powell et al. 2005). Our work deepens the emergent understanding of the impact of micro-interactions on the higher level community structure.

As a formal tool, computational modeling requires a level of precision often missing even from well articulated constructs in social sciences (Adner et al. 2009). Starting from first principles and a clear modeling of formation mechanisms, we were able to accurately match the network structure and linking dynamics in our empirical sample. Thus, a secondary contribution of this study is to provide a validated specification of a model of online community interactions. As is often recognized in computational studies, the theoretical value of simulation findings is only as good as the assumptions that underlie them and the clarity of the mechanisms specified in the algorithms (Harrison et al. 2007; Van Maanen et al. 2007). The validity of our findings is strengthened by the careful calibration of our results against large scale empirical data. Our methodology is also fortified by the use of two separate subsamples to respectively validate and test our model. Such careful construction is considered essential when the goal is theory testing or establishing a novel theoretical logic (Davis et al. 2007). A final contribution is the contribution of a network-based simulation model that is useful to test emergent interactions, something that is called for by the emergent field of computational science (Lazer et al. 2009).

## Implications for Practice

For anyone involved with the development or moderation of an online community, a major implication is that highly skewed participation is an emergent property resulting from a diverse set of participant motivations. Although preferential attachment contributes to power law distributions in online communities, it is not a single unitary motivation for all participants at all times. Further, participant diversity is not just a matter of different subcommunities coalescing around different topic interests; the diversity is about unique complementary motivations. Thus, in interacting with community members it is helpful to activate multiple motivations. Whereas some participants will indeed be interested in interacting with the most popular community members, others may seek out ways to directly interact with peers or want to more generally give back to the community as a whole. Further, motivation to participate is not just about the quantity of participation, but also includes decisions about where to post.

This diversity has implications not only for communication with participants, but also for system design decisions. For example, preferential attachment algorithms remain useful for ranking content that do not lead directly to social interactions. For example, when returning results of documents in a frequently asked questions index, a combination of key word relevance and “most viewed” sort order is warranted. However, in situations where participants actively seek or will benefit from social interactions this algorithm may be suboptimal. If a participant is looking for an expert to answer a question, or to join a conversation about a topic of interest, then the most viewed topic may not be the best fit. Instead, a combination of interest matching and on-going participation by those most likely to respond may be most appropriate.

## Implications for Theory of Networks

Another contribution is that our findings offer a new understanding of the boundary conditions of the Barabási and Albert (1999) model of preferential attachment. In applying preferential attachment to online communities, the combination of participants departing and threads expiring differs from the assumptions of their classic model. In their model of network formation, once a participant has arrived they are available for unlimited future connections (attachments). In actual online communities, however, participants show a strong preference toward interacting through more recently created threads. Thus, a newer participant whose threads have not yet expired can grow more popular than a previously popular participant that ceases generating new message threads.

A challenge in applying theories from physical sciences to social sciences is that parallel conditions rarely exist between physical and social structures. For example, Van Maanen et al. (2007) apply the Ising theory of microscopic magnetism to explain herding behaviors in scale-free OSS developer collaboration networks. An explicit assumption in their model is that influence occurs only through “neighboring” developers. This assumption of scarce communication channels, similar to horizontal and vertical communication limits (Kwon et al. 2007), is not consistent with online community behavior. Such models of how information diffuses via adjacent neighbors run counter to the actual collaborative structure of online communities. Instead of strong information brokering limited by a fixed social structure, in online communities there is an abundance of information pathways as all members can read each other’s messages, membership of the network is openly visible, and anyone can initiate new discussions.

## Limitations and Future Directions

In general, simulation studies such as this one are limited to their reliance on modeling inputs to outcomes. As stated by Adner et al. (2009, p. 204), “simulations have the disadvantage of only being able to prove the existence of a relationship between a set of inputs and an outcome; they cannot determine the necessity of a set of conditions.” Beyond this wellknown aspect of the method, we focus on two specific limitations. First, the study design supports the assertion that a blend of mechanisms is superior to a single mechanism alone. Yet, it does not rule out that other untested mechanisms may also be capable of generating power law distributions in online communities. Second, the design does not falsify earlier findings that preferential attachment can generate power law distributions. Instead, this study clarifies the boundary conditions for applying theories of preferential attachment—it suggests they do not universally apply to online communities. Nonetheless, the preponderance of preferential attachment theory development has been through network simulations and, thus, is subject to these same theory-building limitations.

Specific assumptions in the model of online communities point to fruitful avenues for future research. For example, restricting thread duration to eight days is a simplified way to maintain a limited number of open threads. A future model extension could identify more complex modeling rules and assumptions for determining how many threads are likely to remain active in a group at a particular time and which threads are the most likely to be active. This paper is necessarily limited in the mechanisms it tests. Other fruitful modeling approaches such as those based on attractor principles and assortive mixing (Aral et al. 2009; Fowler et al. 2009; Wong and Boh 2010) could be combined with this method to yield more comprehensive models of online behavior.

Both a strength and a limitation of the simulation model in this paper is that differentiation of agent behavior is derived from shared rules. That is, although differentiated behavior is observed in the agents (indeed, otherwise there would be no long tail distribution) it is an emergent property based on network history and position. An alternative approach might involve defining different rules for different classes or categories of agents—for example, more experienced, expert, or “core” participants may have entirely different sets of behaviors than new, novice, or peripheral participants. Likewise, as participants differ in strength of identification or bond basis with a group they may demonstrate different classes of behaviors (Ren et al. 2007).

Finally, to facilitate comparison to classic preferential attachment models, an even more fundamental design choice for this simulation was to model network formation from online community inception. An alternative approach would be to start from a preexisting set of active network participants to investigate characteristics of more mature online communities. Additional research is also warranted to investigate alternative outcomes such as critical mass (Oliver and Marwell 2001; Peddibhotla and Subramani 2007).

## Summary

In summary, this study contributes to our understanding of online communities and other social communication networks by illuminating the relationships between specific behavioral tendencies of participants and emergent structural network characteristics. We find no evidence that preferential attachment or any other single mechanism alone explains the presence of power laws in online communities. We find that a combination of preferential attachment along with least effort, direct reciprocity, and indirect reciprocity is most consistent with observed power law distributions. Consistent with the limitations of our research approach, we cannot rule out that additional mechanisms are also present in online communities at some level. Nonetheless, we propose that a blended model merits further study and should, given the paucity of empirical or theoretical evidence for preferential attachment as a unitary network formation mechanism in online communities, be viewed as a more likely explanation for power laws in these networks. As such, power law rank/ frequency distributions emerge from pro-social behaviors and can be viewed as a normative characteristic of online communities.

## Acknowledgments

The authors thank the senior editor, Joe Valacich, the associate editor, and the reviewers for their valuable comments during the review process. We also acknowledge valuable feedback from participants at presentations at the International Conference on Information Systems, the University of of Maryland, Temple University, the University of Minnesota, and New York University.

## References

Adamic, L. A., Buyukkokten, O., and Adar, E. 2003. “A Social Network Caught in the Web,” First Monday (8:6) (http://firstmonday.org/ojs/index.php/fm/article/view/1057/977).

Adamic, L. A., and Huberman, B. A. 2000. “Power-Law Distribution of the World Wide Web,” Science (287:5461), p. 2115.

Adner, R., Polos, L., Ryall, M., and Sorenson, O. 2009. “The Case for Formal Theory,” Academy of Management Review (34:2), pp. 201-208.

Ahuja, M., Chudoba, K., George, J. F., Kacmar, C., and McKnight, H. 2002. “Overworked and Isolated? Predicting the Effect of Work–Family Conflict, Autonomy, and Workload on Organizational Commitment and Turnover of Virtual Workers,” in Proceedings of the 35<sup>th</sup> Annual Hawaii International Conference on System Sciences, Los Alamitos, CA: IEEE Computer Society Press, pp. 3586-3593.

Andriani, P., and McKelvey, B. 2009. “From Gaussian to Paretian Thinking: Causes and Implications of Power Laws in Organizations,” Organization Science (20:6), pp. 1053-1071.

Aral, S., Muchnik, L., and Sundararajan, A. 2009. “Distinguishing Influence-Based Contagion from Homophily-Driven Diffusion in Dynamic Networks,” Proceedings of the National Academy of Sciences (106:51), pp. 21544-21549.

Barabási, A. L. 2009. “Scale-Free Networks: A Decade and Beyond,” Science (325), pp. 412-413.

Barabási, A. L. 2012. “Network Science: Luck or Reason,” Nature (489:7417), pp. 507-508.

Barabási, A. L., and Albert, R. 1999. “Emergence of Scaling in Random Networks,” Science (286), pp. 509-512.

Barrat, A., Barthelemy, M., Pastor-Satorras, R., and Vespignani, A. 2004. “The Architecture of Complex Weighted Networks,” Proceedings of the National Academy of Sciences of the United States of America (101:11), pp. 3747-3752.

Bateman, P. J., Gray, P. H., and Butler, B. S. 2011. “The Impact of Community Commitment on Participation in Online Communities,” Information Systems Research (22:4), pp. 841-854.

Benkler, Y. 2006. The Wealth of Networks: How Social Production Transforms Markets and Freedom, New Haven, CT: Yale University Press.

Blau, P. M. 1964. Exchange and Power in Social Life, New York: Wiley.

Borgatti, S. P., and Halgin, D. S. 2011. “On Network Theory,” Organization Science (22:5), pp. 1168-1181.

Burton, R. M., and Obel, B. 2011. “Computational Modeling for What-Is, What-Might-Be, and What-Should-Be Studies—And Triangulation,” Organization Science (22:5), pp. 1195-1202.

Butler, B. S. 2001. “Membership Size, Communication Activity, and Sustainability: A Resource-Based Model of Online Social Structures,” Information Systems Research (12:4). pp. 346-362.

Carley, K., and Lin, Z. 1997. “A Theoretical Study of Organizational Performance under Information Distortion,” Management Science (43:7), pp. 976-997.

Cohen, J. 1992. “A Power Primer,” Psychological bulletin (112:1), pp. 155-159.

Constant, D., Sproull, L., and Kiesler, S. 1996. “The Kindness of Strangers: The Usefulness of Electronic Weak Ties for Technical Advice,” Organization Science (7:2), pp. 119-135.

Contractor, N., Monge, P. R., and Leonardi, P. 2011. “Multidimensional Networks and the Dynamics of Sociomateriality: Bringing Technology Inside the Network,” International Journal of Communication (5), pp. 682-720.

Dahui, W., Menghui, L., and Zengru, D. 2005. “True Reason for Zipf’s Law in Language,” Physica A: Statistical Mechanics and its Applications (358:2), pp. 545-550.

Davis, J. P., Eisenhardt, K. M., and Bingham, C. B. 2007. “Developing Theory Through Simulation Methods,” Academy of Management Review (32:2), pp. 480-499.

DiMaggio, P., Hargittai, E., Neuman, W., and Robinson, J. 2001. “Social Implications of the Internet,” Annual Review of Sociology (27:1), pp. 307-336.

Faraj, S., Jarvenpaa, S. L., and Majchrzak, A. 2011. “Knowledge Collaboration in Online Communities,” Organization Science (22:5), pp. 1224-1239.

Faraj, S., and Johnson, S. L. 2011. “Network Exchange Patterns in Online Communities,” Organization Science (22), pp. 1464-1480.

Faraj, S., Wasko, M., and Johnson, S. L. 2008. “Electronic Knowledge Networks: Processes and Structure,” in Knowledge Management: An Evolutionary View of the Field, I. Becerra-Fernandez and D. Leidner (eds.), Armonk, NY: M. E. Sharpe, Inc., pp. 270-291.

Fowler, J. H., Dawes, C. T., and Christakis, N. A. 2009. “Model of Genetic Variation in Human Social Networks,” Proceedings of the National Academy of Sciences (106:6), pp. 1720-1724.

Fulk, J., Flanigan, A. J., Kalman, M. E., Monge, P. R., and Ryan, T. 1996. “Connective and Communal Public Goods in Interactive Communication Systems,” Communication Theory (6:1), pp. 60-87.

Harrison, J. R., Carroll, G. R., and Carley, K. M. 2007. “Simulation Modeling in Organizational and Management Research,” Academy of Management Review (32:4), pp. 1229-1245.

Howison, J., Wiggins, A., and Crowston, K. 2012. “Validity Issues in the Use of Social Network Analysis with Digital Trace Data,” Journal of the Association for Information Systems (44:2), pp. 767-797.

Ishikawa, A. 2006. “Pareto Index Induced from the Scale of Companies,” Physica A: Statistical Mechanics and its Applications (363:2), pp. 367-376.

Joyce, E., and Kraut, R. E. 2006. “Predicting Continued Participation in Newsgroups,” Journal of Computer-Mediated Communication (11:3), Article 3.

Kankanhalli, A., Tan, B. C. Y., and Kwok-Kee, W. 2005. “Contributing Knowledge to Electronic Knowledge Repositories: An Empirical Investigation,” MIS Quarterly (29:1), pp. 113-143.

Kollock, P. 1999. “The Economies of Online Cooperation: Gifts, and Public Goods in Cyberspace,” in Communities in Cyberspace, M. A. Smith and P. Kollock (eds.), London: Routledge, pp. 220-239.

Kraut, R. E. 2003. “Applying Social Psychological Theory to the Problems of Group Work,” in HCI Models, Theories and Frameworks: Toward A Multidisciplinary Science, J. Carroll (ed.), New York: Morgan Kaufman, pp. 325-356.

Kudaravalli, S., and Faraj, S. 2008. “The Structure of Collaboration in Electronic Networks,” Journal of the Association for Information Systems (9:10/11), pp. 706-726.

Kuk, G. 2006. “Strategic Interaction and Knowledge Sharing in the KDE Developer Mailing List,” Management Science (52:7), pp. 1031-1042.

Kumar, R., Novak, J., and Tomkins, A. 2010. “Structure and Evolution of Online Social Networks,” in Link Mining: Models, Algorithms, and Applications, P. S. Yu, J. Han, and C. Faloutsos (eds.), New York: Springer, pp. 337-357.

Kwon, D., Oh, W., and Jeon, S. 2007. “Broken Ties: The Impact of Organizational Restructuring on the Stability of Information-Processing Networks,” Journal of Management Information Systems (24:1), pp. 201-231.

Lakhani, K., and von Hippel, E. 2003. “How Open Source Software Works: ‘Free’ User-to-User Assistance,” Research Policy (32), pp. 923-943.

Lampe, C., Wash, R., Velasquez, A., and Ozkaya, E. Year. “Motivations to participate in online communities,” Proc. CHI2010, pp. 1927-1936.

Lave, C. A., and March, J. G. 1975. An Introduction to Models in the Social Sciences, New York: Harper & Row.

Law, A. M., and Kelton, W. D. 2000. Simulation Modeling and Analysis, New York: McGraw-Hill.

Lazer, D., Pentland, A. S., Adamic, L., Aral, S., Barabási, A. L., Brewer, D., Christakis, N., Contractor, N., Fowler, J., and Gutmann, M. 2009. “Life in the Network: The Coming Age of Computational Social Science,” Science (323:5915), pp. 721-723.

McKelvey, B. 2002. “Model-Centered Organization Science Epistemology,” in Companion to Organizations, A. C. Baum (ed.), Thousand Oaks, CA: Sage Publications, pp. 752-780.

Merton, R. 1968. “The Matthew Effect in Science: The Reward and Communication Systems of Science Are Considered,” Science (159:3810), pp. 56-63.

Monge, P. R., and Contractor, N. S. 2003. Theories of Communication Networks, Oxford, UK: Oxford University Press.

Newman, M. E. J. 2003. “The Structure and Function of Complex Networks,” SIAM Review (45:2), pp. 167-256.

Newman, M. E. J., Barabási, A. L., and Watts, D. J. 2006. The Structure and Dynamics of Networks, Princeton, NJ: Princeton University Press.

Oliver, P. E., and Marwell, G. 2001. “Whatever Happened to Critical Mass Theory? A Retrospective and Assessment,” Sociological Theory (19:3), pp. 292-311.

Orlikowski, W. J., and Iacono, C. S. 2001. “Research Commentary: Desperately Seeking the ‘IT’ in IT Research—A Call to Theorizing the IT Artifact,” Information Systems Research (12:2), pp. 121-134.

Peddibhotla, N. B., and Subramani, M. R. 2007. “Contributing to Public Document Repositories: A Critical Mass Theory Perspective,” Organization Studies (28:3), pp. 327-346.

Powell, W., White, D., Koput, K., and Owen Smith, J. 2005. “Network Dynamics and Field Evolution: The Growth of

Interorganizational Collaboration in the Life Sciences,” American Journal of Sociology (110:4), pp. 1132-1205.

Preece, J. 2000. Online Communities: Designing Usability, Supporting Sociability, Chichester, UK: John Wiley & Sons.

Preece, J., Nonnecke, B., and Andrews, D. 2004. “The Top Five Reasons for Lurking: Improving Community Experiences for Everyone,” Computers in Human Behavior (20:2), pp. 201-223.

Preece, J., and Shneiderman, B. 2009. “The Reader-to-Leader Framework: Motivating Technology-Mediated Social Participation,” AIS Transactions on Human–Computer Interaction (1:1), pp. 13-32.

Raban, D. R., and Rabin, E. 2009. “Statistical Inference from Power Law Distributed Web-Based Social Interactions,” Internet Research (19:3), pp. 266-278.

Rainie, L., and Wellman, B. 2012. Networked: The New Social Operating System, Cambridge, MA: MIT Press.

Ravid, G., and Rafaeli, S. 2004. “Asynchronous Discussion Groups as Small World and Scale Free Networks,” First Monday (9:9) (http://firstmonday.org/article/view/1170/).

Ren, Y., Kraut, R., and Kiesler, S. 2007. “Applying Common Identity and Bond Theory to Design of Online Communities,” Organization Studies (28:3), pp. 377-408.

Rheingold, H. 2000. The Virtual Community: Homesteading on the Electronic Frontier, Cambridge, MA: MIT Press.

Shirky, C. 2008. Here Comes Everybody: The Power of Organi zing Without Organizations, New York: Penguin Press.

Sproull, L., and Arriaga, M. 2007. “Online Communities,” in Handbook of Computer Networks, Volume 3, H. Bidogli (ed.), New York: Wiley, pp. 248-279.

Sundararajan, A., Provost, F., Oestreicher-Singer, G., and Aral, S. 2013. “Information in Digital, Economic, and Social Networks,” Information Systems Research (24:4), pp. 883-905.

Tapscott, D., and Williams, A. D. 2006. Wikinomics: How Mass Collaboration Changes Everything, New York: Portfolio.

Van Maanen, J., Sorensen, J. B., and Mitchell, T. R. 2007. “The Interplay between Theory and Method,” Academy of Management Review (32:4), pp. 1145-1154.

Wang, X., Butler, B. S., and Ren, Y. 2013. “The Impact of Membership Overlap on Growth: An Ecological Competition View of Online Groups,” Organization Science (24:2), pp. 424-431.

Wasko, M. M., and Faraj, S. 2000. “‘It Is What One Does’: Why People Participate and Help Others in Electronic Communities of Practice,” Journal of Strategic Information Systems (9), pp. 155-173.

Wasko, M. M., and Faraj, S. 2005. “Why Should I Share: Examining Social Capital and Knowledge Contribution in Electronic Networks of Practice,” MIS Quarterly (29:1), pp. 35-47.

Wasserman, S., and Faust, K. 1994. Social Network Analysis: Methods and Applications, Cambridge, UK: Cambridge University Press.

Watts, D. J. 1999. Small Worlds: The Dynamics of Networks between Order and Randomness, Princeton, NJ: Princeton University Press.

Wong, S. S., and Boh, W. F. 2010. “Leveraging the Ties of Others to Build Managerial Peer Reputation for Trustworthiness,” Academy of Management Journal (53:1), pp. 129-148.

Wu, F., Huberman, B. A., Adamic, L. A., and Tyler, J. R. 2004. “Information Flow in Social Groups,” Physica A (337), pp. 327-335.

Zaheer, A., and Soda, G. 2009. “Network Evolution: The Origins of Structural Holes,” Administrative Science Quarterly (54:1), pp. 1-31.

Zipf, G. K. 1949. Human Behavior and the Principle of Least Effort, Oxford, UK: Addison-Wesley Press.

## About the Authors

Steven L. Johnson is an assistant professor in the Management Information Systems Department at the Fox School of Business, Temple University. He received his Ph.D. from the Smith School of Business at the University of Maryland at College Park. His major research focus is online communities as a form of social media that supports organizational knowledge management. Before pursuing his doctoral studies, he worked in the information technology industry for 15 years.

Samer Faraj is Professor and Canada Research Chair in Technology, Management, and Healthcare at the Desautels Faculty of Management, McGill University. He is head of the research group on Complex Collaboration and director of the PhD program. He previously served as a senior editor for Organization Science and currently serves as a senior editor for Information Systems Research. He research interests focus on theorizing the technology–organizing nexus. He is currently working on knowledge collaboration, new forms of organizing, and technology performativity in settings such as online communities and healthcare organizations. He has won multiple best paper awards, most recently the AIS 2012 Best Published Paper Award and the 2013 best doctoral advisor award at the Desautels faculty.

Srinivas Kudaravalli is an assistant professor in the Operations Management and Information Technology Department at HEC Paris. He received his Ph.D. from the Smith School of Business at the University of Maryland at College Park. He studies the technologies and processes that facilitate effective collaboration in knowledge work, in settings such as online communities, large-scale distributed groups, and organizational teams. Prior to joining academia, he consulted for various organizations for a decade.

# EMERGENCE OF POWER LAWS IN ONLINE COMMUNITIES:THE ROLE OF SOCIAL MECHANISMS AND PREFERENTIALATTACHMENT

Steven L. Johnson Fox School of Business, Temple University, Philadelphia, PA 19122-6083 U.S.A. {steven@temple.edu}

Samer Faraj

Desautels Faculty of Management, McGill University, Montreal, Quebec H3A 1G5 CANADA {samer.faraj@mcgill.ca}

Srinivas Kudaravall

HEC Paris,1, rue de la Liberation, 78351 Jouy en Josas Cedex FRANCE {kudaravalli@hec.fr}

## Appendix A

## Detailed Description of Research Method

As summarized in Table A1, this appendix provides a detailed description of the research method used to test the proposed hypotheses. The first major step was to collect observational and trace data from online communities. The observational data supported creation of a descriptive model of online community formation. The trace data encompasses the first 12 to 15 months of communication in 28 online communities that were randomly selected into a model specification sample and a model testing sample. In the next major step, the descriptive model was turned into a formal model of online community formation and then implemented in R. The first 12 to 15 months of data from the online communities in the model specification sample provide key simulation parameters (e.g., participant arrival and departure rates).

<table><tr><td colspan="3">Table A1. Research Method</td></tr><tr><td>Activity</td><td>Steps</td><td>Description</td></tr><tr><td rowspan="3">Collect Data</td><td>Observe Online Communities</td><td>Through observation of online communities identify behaviors, rules, and tendencies guiding communication network formation.</td></tr><tr><td>Prepare Descriptive Model</td><td>Complement observation data with existing theory and empirical research to prepare descriptive model of online community network formation.</td></tr><tr><td>Collect Trace Data</td><td>Collect 15 months of message history for multiple online communities and randomly split into model specification sample and model testing sample.</td></tr><tr><td rowspan="3">Develop Simulation</td><td>Create Formal Model</td><td>Document formal rules and assumptions. Identify functional forms for agents and mechanisms.</td></tr><tr><td>Calculate Input Parameters</td><td>Use model specification sample to calculate input variables for simulation.</td></tr><tr><td>Code Simulation</td><td>Implement formal model as an agent-based simulation in R.</td></tr><tr><td rowspan="3">Run Simulation</td><td>Generate Data</td><td>Generate simulation data by varying parameters associated with each hypothesis. Run single mechanism setting for test of H1 (n = 40 per individual mechanism) and run 50 Monte Carlo mechanism combinations (n = 20 per mechanism combination) for test of H2 (total n = 20 * 50 = 1,000).</td></tr><tr><td>Validate Simulation Output</td><td>Compare model specification sample and simulation data to validate simulation model generates data in empirical range of interest.</td></tr><tr><td>Calibrate Simulation Parameters</td><td>Prepare analysis sample of networks with similar structural characteristics as model specification sample.</td></tr><tr><td rowspan="2">Model Testing</td><td>Calculate Outcome Measures</td><td>Calculate outcomes in the model testing sample and the calibrated simulation output.</td></tr><tr><td>Analyze Model</td><td>Compare outcomes to test hypothesis.</td></tr></table>

In the third major step of the research method, simulation data was generated to test each of the proposed hypotheses. First, data was generated with parameters specific to each hypothesis. Second, the entire set of generated data was compared to the model specification sample to establish that the simulation encompasses an appropriate range of networks. Next, the simulation model was calibrated to create an analysis sample. The final major step was to analyze the similarity of the model testing sample and the analysis sample. The estimated power law distribution was calculated for all of the networks in both samples. Then, two-tailed ANOVA tests were performed to test each hypothesis. All four major steps are described in more detail in this appendix.

## Collect Data

This paper studies communication networks formed via participants in online communities supported by threaded discussion forums. The first major activity in the research method was to collect observation data and trace data to prepare a descriptive model of the network formation process. Several hundred threaded discussion forums were informally observed. These online communities were identified using Yahoo! Search for the strings “Powered by vBulletin” and “software” to find technology-related discussion forums that share a common technology infrastructure. The sample was further reduced to include only online communities where a full archive of the initial 15 months of posting history was available. An automated program was used to gather the first 15 months of communication for 28 online communities randomly selected.

Table A2. Model Specification and Model Testing Subsamples

<table><tr><td>Website</td><td>Subssample</td><td>Inception</td><td>Participants</td><td>Messages</td><td>Threads</td></tr><tr><td>forums.3dcart.com</td><td>Specification</td><td>2/24/06</td><td>78</td><td>950</td><td>254</td></tr><tr><td>bid-alot.com/forum</td><td>Test</td><td>8/11/04</td><td>62</td><td>1492</td><td>291</td></tr><tr><td>bibleworks.com/forums</td><td>Test</td><td>4/1/04</td><td>345</td><td>3388</td><td>647</td></tr><tr><td>forums.builtbp.com</td><td>Test</td><td>2/8/06</td><td>140</td><td>247</td><td>114</td></tr><tr><td>archive.burningsea.com/forums</td><td>Test</td><td>10/25/01</td><td>214</td><td>2156</td><td>382</td></tr><tr><td>codenewbie.com/forum</td><td>Specification</td><td>5/6/02</td><td>248</td><td>5596</td><td>893</td></tr><tr><td>forum.conceiva.com</td><td>Specification</td><td>12/24/07</td><td>84</td><td>434</td><td>133</td></tr><tr><td>cruisersforum.com/forums</td><td>Test</td><td>2/24/03</td><td>297</td><td>3319</td><td>686</td></tr><tr><td>developers.evrsoft.com/forum</td><td>Test</td><td>9/5/02</td><td>959</td><td>8996</td><td>1425</td></tr><tr><td>forums.foxitsoftware.com</td><td>Test</td><td>6/27/08</td><td>699</td><td>3429</td><td>895</td></tr><tr><td>fsdeveloper.com</td><td>Test</td><td>6/1/04</td><td>281</td><td>5758</td><td>953</td></tr><tr><td>gamefileforums.com/forums</td><td>Test</td><td>1/31/05</td><td>1112</td><td>5703</td><td>1047</td></tr><tr><td>forums.hostrocket.com</td><td>Specification</td><td>5/10/02</td><td>389</td><td>8022</td><td>1388</td></tr><tr><td>jpsoft.com/forums</td><td>Test</td><td>5/20/08</td><td>214</td><td>4074</td><td>851</td></tr><tr><td>forum.k-billing.com</td><td>Specification</td><td>9/11/06</td><td>127</td><td>1181</td><td>285</td></tr><tr><td>libertystreet.com/forums</td><td>Specification</td><td>11/5/05</td><td>131</td><td>2279</td><td>332</td></tr><tr><td>forums.mxhub.com</td><td>Test</td><td>5/12/01</td><td>85</td><td>519</td><td>172</td></tr><tr><td>npowersoftware.com/forums</td><td>Test</td><td>9/4/03</td><td>65</td><td>434</td><td>106</td></tr><tr><td>programmersresource.com/forum</td><td>Test</td><td>5/21/03</td><td>615</td><td>4409</td><td>1390</td></tr><tr><td>siginetsoftware.com/forum</td><td>Specification</td><td>5/16/06</td><td>222</td><td>1238</td><td>137</td></tr><tr><td>stormlabstuff.com/board</td><td>Test</td><td>6/1/07</td><td>106</td><td>1560</td><td>286</td></tr><tr><td>forums.swordsearcher.com</td><td>Specification</td><td>5/16/06</td><td>65</td><td>927</td><td>168</td></tr><tr><td>teamd86.com</td><td>Test</td><td>11/27/02</td><td>86</td><td>3880</td><td>552</td></tr><tr><td>bb.turtlesoft.com</td><td>Test</td><td>9/13/06</td><td>26</td><td>280</td><td>83</td></tr><tr><td>vintage-computer.com/vcforum</td><td>Test</td><td>4/27/03</td><td>266</td><td>5184</td><td>883</td></tr><tr><td>vjforums.com</td><td>Test</td><td>4/8/02</td><td>830</td><td>17057</td><td>2110</td></tr><tr><td>weathergraphics.com/forum</td><td>Specification</td><td>11/23/03</td><td>141</td><td>1763</td><td>493</td></tr><tr><td>forums.winxpcentral.com</td><td>Test</td><td>7/29/01</td><td>453</td><td>8929</td><td>2233</td></tr></table>

<table><tr><td>Table A3. Descriptive Model</td></tr><tr><td>Participants</td></tr><tr><td>Participants are limited to these actions:</td></tr><tr><td>• Enter system</td></tr><tr><td>• Post a message that starts a new thread</td></tr><tr><td>• Post a message that adds to an existing thread</td></tr><tr><td>• Exit system</td></tr><tr><td>All participants share these behaviors:</td></tr><tr><td>• New participants may arrive at any time</td></tr><tr><td>• Any active participant can post a message to start a new thread</td></tr><tr><td>• Any active participant can post a message in response to the an open thread</td></tr><tr><td>• Active participants may depart the system at any time</td></tr><tr><td>To facilitate modeling, participants are assumed to behave in this way:</td></tr><tr><td>• Immediately upon arrival a participant posts a message that starts a new thread</td></tr><tr><td>• After a participant exits the system they may not reenter</td></tr><tr><td>• No participants are present in the system when the simulation begins</td></tr><tr><td>• Participants will have between 1 and a preset maximum number of opportunities to post per turn</td></tr><tr><td>Messages</td></tr><tr><td>Rules for messages:</td></tr><tr><td>• Every message belongs to one and only one message thread</td></tr><tr><td>• All message are treated as responses to the message starting the message thread</td></tr><tr><td>Threads</td></tr><tr><td>Rules for threads:</td></tr><tr><td>• New message threads may be created with a new message by already active or newly entering participants at any time</td></tr><tr><td>• Any active or newly entering participant may respond to any open message thread</td></tr><tr><td>As an approximation of observed preferences for newer threads, this assumption is made:</td></tr><tr><td>• A message thread is made inactive (closed) 8 clicks (days) after it is created†</td></tr></table>

<sup>†</sup>Across all of the model specification subsample, 82% of the message threads received all of their responses within 8 days; 85% received all but one message, and 91% received all but two messages.

## Online Community Sample

Online communities in Table A2 were randomly assigned to a model specification and model test subsample. Each online community was assigned a random number using the Microsoft Excel RAND() function. The list was then sorted in ascending order with the one third (the first 9 groups) assigned to the model specification subsample and the remaining 19 groups assigned to the model test subsample. The original online community URL is listed. Since the research data was collected, some online communities have moved to a new URL, migrated to a different software platform, or closed altogether.

## Descriptive Model of Online Community Threaded Discussion Board

This paper simulates the formation of online community communication networks formed via threaded discussion boards. The rules and assumptions described in Table A3 were used to model the formation of and communication within a threaded discussion board. The primary entities in modeling an online community threaded discussion board are participants, messages, and threads.

## Develop Simulation

The next major step of the research method was to develop the simulation. The descriptive model developed in the first step was further developed as a formal network formation model. Where appropriate, the first 12 to 15 months of data from model specification sample provided key simulation parameters. For example, the first year of data was used to estimate participant arrival rates and the first 15 months of data to estimate participant departure rates. By expressing key behaviors and rules in mathematical formulas, this detailed formal model provided the basis for implementing the agent-based model of network creation in the programming language of R.

![](/api/attachments/2YF2KDJ2/fulltext/images/fbcf157f00075771a6b506e0336d0f5cc49e9047d33d6d1d88ab723a9b989175.jpg)  
Figure A1. Example Participant Arrival and Departure Functions

## Formal Model for Online Community Formation

Because no existing theoretical basis was found to develop arrival and departure functions, the new participant entry and participant departure functions were based on empirically derived formulas calculated from the model specification subsample. New participant entry was modeled as a function of time and active participant departure as a function of individual tenure.

To analyze new participant entry, a cumulative distribution function was calculated based on when participants posted their first message. It was found that the cumulative distribution functions for the online communities in the model specification subsample closely fit a linear model (average R<sup>2</sup> = 0.88; s.d. = 0.09; n = 9).

To analyze participant departure, the cumulative distribution function was calculated based on the length of time between a participant’s first message and their final message in the first year. Any participant who posted a message during months 12–15 was considered as remaining active. The best fitting model for the cumulative distribution function for participant departure was found to be a logarithmic function (average R<sup>2</sup> = 0.96; s.d. = 0.03; n = 9).

Figure A1 shows an example cumulative distribution function for arrival and departure. The observed arrival pattern is straightforward: new participants arrive in a relatively steady pace with minor variations. The departure function shows that although a high percentage of participants depart between one day and one month of arrival (in Figure A1 almost 70% and 85%, respectively), if a participant remains active beyond approximately one month, their marginal probability of departure decreases. That is, participants who have been participating for a longer period of time are less likely to discontinue participating than those who have been participating for a shorter period of time.

## Selecting Network Generation Mechanisms

The primary research question for the paper is to identify network generation mechanisms that lead to the power law distributions observed in online communities. A critical step in the research process is identifying the most relevant mechanisms to test. We selected mechanisms that meet one of the following two criteria: (1) they are relevant mechanisms known to create power law distributions in other settings or (2) they are mechanisms identified in previous studies of online communities. The latter is described in the body of the paper, the former below.

<table><tr><td colspan="3">Table A4. Generation Mechanisms for a Power Law Distribution</td></tr><tr><td>Dominant Domain</td><td>Mechanism</td><td>Relevance to Online Community Formation</td></tr><tr><td>Biology</td><td>Contagion bursts</td><td>Is based on contagions and epidemics; no parallel exists in online community formation.</td></tr><tr><td>Biology</td><td>Hierarchical modularity</td><td>A model of cellular level growth through cell fission; online community growth based on arriving and departing participants.</td></tr><tr><td>Biology</td><td>Interacting fractals</td><td>Is based on fractal structure of food webs and predators; no parallel exists in online community formation.</td></tr><tr><td>Economics</td><td>Niche proliferation</td><td>Based on effects of scale in markets; no parallel exists in online community formation.</td></tr><tr><td>Economics</td><td>Random walk</td><td>Describes distribution of losses before a finite resource depleted in a stochastic process; no parallel exists in online community formation.</td></tr><tr><td>General</td><td>Combination theory</td><td>Combination theory is not, by itself, a generation mechanism; instead, it suggests that power laws can form through the combination of complex subtasks. A blended model of network formation may be consistent with combination theory but does not directly test it.</td></tr><tr><td>General</td><td>Event bursts</td><td>Describes prioritization of activity, such as bursts of communication; no empirical evidence for existence in online community formation.</td></tr><tr><td>General</td><td>Interactive breakage theory</td><td>Interactive breakage theory is not, by itself, a generation mechanism; instead, it suggests that power laws can form through positive feedback loops. A blended model of network formation may be consistent with interactive breakage theory but does not directly test it.</td></tr><tr><td>General</td><td>Spontaneous order creation</td><td>Spontaneous order creation is not, by itself, a generation mechanism; instead, it suggests that power laws can form through positive feedback loops. A blended model of network formation may be consistent with spontaneous order creation but does not directly test it.</td></tr><tr><td>Physical</td><td>Irregularity generated gradients</td><td>Is based on autocatalytic processes; no parallel exists in online community formation.</td></tr><tr><td>Physical</td><td>Phase transition</td><td>Is based on autocatalytic processes; no parallel exists in online community formation.</td></tr><tr><td>Physical</td><td>Self-organized criticality</td><td>A physical theory related to the effects of gravity; no parallel exists in online community formation.</td></tr><tr><td>Physical</td><td>Surface-volume law</td><td>Based on relationship between 2D surface and 3D volume; no parallel exists in online community formation.</td></tr><tr><td>Social</td><td>Least effort</td><td>Applies in situations like online communities where some nodes have varying connection costs.</td></tr><tr><td>Social</td><td>Preferential attachment</td><td>Applies in situations like online communities where new entrants choose among existing entrants for connections</td></tr></table>

To identify relevant mechanisms, we started with the list identified in Andriani and McKelvey’s (2009) comprehensive review (see Table A4). As a next step, building on theoretical and empirical work on online communities, we developed criteria as to what characteristics those mechanisms would have. Based on literature on online communities (Butler 2001; Faraj and Johnson 2011; Preece 2000; Ren et al. 2012) , we selected only the social mechanisms. That is, the mechanisms that are likely to build member attachment and participation in online communities.

Our fundamental argument is that models borrowing from areas such as heat transfer, gravity, phase transition, contagion, fractals, or random walk may be useful descriptive metaphors and empirical descriptions of a static network, but they cannot be considered relevant as explanatory mechanisms for the highly social process involving human actors interacting in online communities—as is now well established in the above cited literature. Thus, this paper is not focused on proving or disproving the families of models coming from other scientific domains. Instead, the focus is on evaluating socially relevant mechanisms.

## Power Law Distribution Generation Mechanisms

In the implementation of preferential attachment, the likelihood of selecting an agent to respond to is in proportion to the number of previous responses they have received (their in-degree). The linearized chord diagram (LCD) implementation (Kolaczyk 2009, pp. 173-175) of the Barabási and Albert (1999) model of preferential attachment was used. The LCD implementation disambiguates the original Barabási and Albert model in regard to both starting conditions for a new network, as well as selection for new connections.

In the implementation of least efforts, every active agent was assigned a relative weight representing the ease with which they may be responded to. This parallels the logic of least efforts that, just as there are shorter words in a vocabulary that are easier to use than longer ones, within an online community, there are some people who consistently create threads that are easier to respond to than others. The probability was assigned once for each agent and remains constant for the entire simulation of that communication network formation. In determining who a focal agent will respond to, an agent was selected randomly, weighted by the least effort weight. If the selected agent has more than one active thread, the active thread that was created first was responded to.

In the implementation of direct reciprocity, the likelihood of selecting an agent to respond to was based on prior dyadic communication history. First a weight was calculated for each potential agent as follows, where $\Gamma _ { \mathrm { i j } }$ was the number of previous messages from the focal agent (i) to the potential agent (j) and ${ \bf r } _ { \mathrm { j i } }$ was the number of messages from the potential agent to the focal agent:

$\operatorname { I f } \mathbf { r } _ { \mathrm { i j } }$ is 0 and $\mathrm { r _ { \mathrm { i i } } } > 0$ then set weight to 2

$\operatorname { I f } \mathbf { r } _ { \mathrm { i j } }$ is 0 and $\mathbf { r } _ { \mathrm { i i } }$ is 0 then set weight to 1

$\mathrm { I f r } _ { \mathrm { i j } } > 0$ and $\Gamma _ { \mathrm { j i } } > 0$ then set weight to $\mathrm { ~ ( ~ 1 + ( r _ { i j } - r _ { j i } ) / \Gamma ( r _ { i j } + r _ { j i } ) ~ ) ~ }$

The intuition of this formula is that when two participants have not interacted, they start with a weight of 1. When a focal agent has not yet reciprocated a tie from an alter, motivation is greatly increased (weight = 2); when a focal agent has unreciprocated ties, motivation decreases in proportion to the number of unreciprocated ties. Once the weights were calculated for an agent and all potential alters, an alter was randomly selected weighted by the calculated values. If the selected agent has more than one active thread, the active thread that was created first was responded to.

With indirect reciprocity, an agent’s likelihood of creating new links is determined by its previous history of posts and replies to those posts (Faraj and Johnson 2011). The formula was calculated based on the ratio of an agent’s in-degree divided by the agent’s out-degree. If an agent has received many replies, but not made many posts themselves, their in-degree will exceed their out-degree. The ratio of the in-degree to the out-degree will be greater than one and an agent will have an above-average probability of creating new ties. If an agent has made many replie to others, but not yet received as many replies to their own threads, the situation was reversed. The ratio will be less than one and that agent’s probability of creating new ties will be less than average. In either case, when agents create new ties, they select them at random from all othe active agents in the network. In the starting condition, when an agent has not yet posted any replies (e.g., their out-degree is zero), they were assigned the average propensity to form new ties.

## Calculate Input Parameters

The shaded values in Table A5 were used as simulation input parameters.

Table A5. Key Statistics From Model Specification Subsample

<table><tr><td>Website</td><td>Thread Depth</td><td>Departure Parameter (b)</td><td>Departure Parameter (Int)</td><td>Participants</td><td>Messages</td><td>Threads</td></tr><tr><td>forums.3dcart.com</td><td>3.740</td><td>0.07</td><td>0.18</td><td>78</td><td>950</td><td>254</td></tr><tr><td>codenewbie.com/forum</td><td>6.279</td><td>0.06</td><td>0.49</td><td>248</td><td>5569</td><td>887</td></tr><tr><td>forum.conceiva.com</td><td>3.273</td><td>0.07</td><td>0.51</td><td>84</td><td>432</td><td>132</td></tr><tr><td>forums.hostrocket.com</td><td>5.782</td><td>0.09</td><td>0.23</td><td>389</td><td>7996</td><td>1383</td></tr><tr><td>forum.k-billing.com</td><td>4.144</td><td>0.08</td><td>0.38</td><td>127</td><td>1181</td><td>285</td></tr><tr><td>libertystreet.com/forums</td><td>6.865</td><td>0.04</td><td>0.70</td><td>131</td><td>2279</td><td>332</td></tr><tr><td>siginetsoftware.com/forum</td><td>9.074</td><td>0.05</td><td>0.60</td><td>222</td><td>1225</td><td>135</td></tr><tr><td>forums.swordsearcher.com</td><td>5.518</td><td>0.05</td><td>0.57</td><td>65</td><td>927</td><td>168</td></tr><tr><td>weathergraphics.com/forum</td><td>3.551</td><td>0.09</td><td>0.22</td><td>141</td><td>1747</td><td>492</td></tr><tr><td>Average (n = 9)</td><td>5.358</td><td>0.067</td><td>0.431</td><td>165.0</td><td>2478.4</td><td>452.0</td></tr></table>

![](/api/attachments/2YF2KDJ2/fulltext/images/cc9785b3563a7fc3981d126fe6b93fae9e9bc7a0830283a82004ac6fa05459bd.jpg)

## Code Simulation

The formal model was implemented in computer code; a pseudocode representation is provided below. The computational model was implemented in the statistical package R (R Development Core Team 2009). Additional packages used include igraph (http://igraph.sourceforge.net), MASS (http://www.stats.ox.ac.uk/pub/MASS4/), and sampling (Matei and Tillé 2006). Consistent with best practices of simulation development, common random number queues were used across simulation runs as a variance reduction technique (Law and Kelton 2000). The first author programmed the simulation and the second author reviewed the code. The portion of the pseudocode shown in Figure A3 demonstrates overall flow control.

## Figure A3. Overall Flow Control

The portion of the pseudocode shown in Figure A4 describes the network formation function.

```txt
# comment: network formation function

IF network formation mechanism is Preferential Attachment THEN
    # comment: randomly select reply 'to' weighted by in-degree
    Set RandomThread to thread containing a randomly selected post
    Set "to" agent as agent that started RandomThread
    IF any threads started by "to" agent are active THEN
    Post to earliest active thread of 'to' agent
    ENDIF
ENDIF

IF network formation mechanism is Least Efforts THEN
    # comment: randomly select reply 'to' weighted by ease of replying to
    Set agentlist to all agents with active threads
    Set 'to' agent as random selection from agentlist using LeastEffortsWeights
    Post to earliest active thread of 'to' agent
ENDIF

IF network formation mechanism is Direct reciprocity THEN
    # comment: randomly select reply 'to' weighted by past history
    Set agentlist to all agents with active threads
    FOR all agents in the agentlist
    Set Rij to number of posts from focal agent to agent in agentlist
    Set Rji to number of posts to focal agent by agent in agentlist
    IF Rij is zero and Rji > 0 THEN Set weight to 2
    ELSE IF Rij + RJI is zero THEN Set weight to 1
    ELSE Set weight to 1 + (Rij - Rij) / (Rij + Rji)
ENDFOR
Set 'to' agent as random selection from agentlist using weights
Post to earliest active thread of 'to' agent
ENDIF

IF network formation mechanism is Indirect Reciprocity THEN
    # comment: randomly select reply 'to' agent
    Set agentlist to all agents with active threads
    Set 'to' agent as random selection from agentlist
    Post to earliest active thread of 'to' agent
ENDIF

Figure A4. Network Formation Function
```

In a blended model, multiple mechanisms are present during network formation. Weights were identified for each network formation mechanism that remain constant for that simulation run. The weights to test were chosen with a Monte Carlo method (see Law and Kelton 2000). A random number was chosen for each of the four mechanisms and then a percentage of total (0%–100%) calculated for each mechanism. For each simulated day, an active agent is assigned a single network formation mechanism based on the weights for that simulation run.

Prior to running the simulation code, the list of random number seeds was selected by randomly selecting numbers between 1 and 10,000 using the R command:

$$
\text { sort } (\text { trunc } (\text { runif } (1 0, 1, 1 0 0 0 0)))
$$

This command returns 10 randomly selected values from a uniform distribution, converts them to an integer value via truncation and then sorts the list in ascending order. The pseudocode shown in Figure A5 describes how the random number seeds are incorporated into the simulation model.

```txt
# comment: blended model algorithm (Monte Carlo)
Set RandomNumberList to list of random number seeds

FOR all seeds in RandomNumberList
    Set Random1 to randomly selected number between 0 and 1
    Set Random2 to randomly selected number between 0 and 1
    Set Random3 to randomly selected number between 0 and 1
    Set Random4 to randomly selected number between 0 and 1
    Set TotalRandom = Random1 + Random2 + Random3 + Random4
    Set PreferentialAttachmentWeight = Random1 / TotalRandom
    Set LeastEffortsWeight = Random2 / TotalRandom
    Set DirectReciprocityWeight = Random3 / TotalRandom
    Set IndirectReciprocityWeight = Random4 / TotalRandom

[ ... call flow control code ... ]

# Where the command reads:
# Set network formation mechanism for this agent for this click
# Randomly select mechanism weighted by the mechanism weights
# PreferentialAttachmentWeight, LeastEffortsWeight,
# DirectReciprocityWeight and IndirectReciprocityWeight

ENDFOR
```

Figure A5. Incorporating Random Number Seeds into the Simulation Model

## Run Simulation

## Generate Simulation Data

Each set of simulation parameters was run with multiple random number queues. A simulation run was comprised 365 iterations, simulating the first 365 days of an online community formation. An active agent could create zero to three responses to existing messages and could initiate zero or one new message threads per iteration. The ability to create multiple messages per period is consistent with actual participant behavior and also assisted in creating networks of similar size to the model specification sample.

## Validate Simulation

A comparison of simulated data to observed data validates that the simulation generates results consistent with reality. As demonstrated visually in Figure A6, the simulated data covers the range of observed data. It is unsurprising that some simulated networks were out of range and encouraging that others were a closer fit. In this way we can establish what mechanisms are most consistent with the emergence of power laws in online communities and can also provide confidence that our computational model provides a faithful simulation.

![](/api/attachments/2YF2KDJ2/fulltext/images/345dbfea59126f891035c8067c565113287c2b61d5413b6374b1a30a19391d92.jpg)

![](/api/attachments/2YF2KDJ2/fulltext/images/e23cb03b00a77ba5d2dfa45e9acb7f8130875581d02c3ecb8e3201484abfd2f4.jpg)  
Estimated Power Law Exponent (b) and fit (R<sup>2</sup>) for Calibration Sample (n=9) and Simulation Runs (n=1040)

Figure A6. Model Validation

Table A6. Additional Calibration Variables From Model Specification Sample

<table><tr><td>Website</td><td>Graph Density</td><td>Clustering Coefficient</td></tr><tr><td>forums.3dcart.com</td><td>0.042</td><td>0.274</td></tr><tr><td>codenewbie.com/forum</td><td>0.016</td><td>0.204</td></tr><tr><td>forum.conceiva.com</td><td>0.014</td><td>0.021</td></tr><tr><td>forums.hostrocket.com</td><td>0.012</td><td>0.155</td></tr><tr><td>forum.k-billing.com</td><td>0.012</td><td>0.027</td></tr><tr><td>libertystreet.com/forums</td><td>0.009</td><td>0.038</td></tr><tr><td>siginetsoftware.com/forum</td><td>0.006</td><td>0.009</td></tr><tr><td>forums.swordsearcher.com</td><td>0.046</td><td>0.269</td></tr><tr><td>weathergraphics.com/forum</td><td>0.021</td><td>0.160</td></tr><tr><td>Minimum</td><td>0.006</td><td>0.009</td></tr><tr><td>Maximum</td><td>0.046</td><td>0.274</td></tr></table>

## Calibrate Simulation

The calibration of a simulation model provides confidence in finding robust configuration to compare against the model testing sample (Sanchez and Lucas 2002). Two methods were employed to calibrate the simulation. First, to simulate networks of matching size and complexity, the target number of message per threads from subsample A was used (5.4) as a target value. Simulation runs resulting in an average number of messages per thread +/- 10% of this target were retained. Simulation runs falling below the target thread percentage range were dropped because it is an indication that network formation mechanisms were not being consistently triggered. In essence, the mechanisms did not have enough power compared to the modeling assumption that a new entrant starts a new thread upon arrival. Simulation runs where the target thread percentage was overshot were dropped because it is an indication that the rule to keep thread length in balance is overwhelmed by the mechanisms. Table A6 shows the additional calibration variables (thread depth appears in Table A4). Table A7 summarizes the relationship between the model specification sample, model testing sample, and analysis sample.

<table><tr><td>Major Activity</td><td>Sample</td><td>Sample Size</td></tr><tr><td rowspan="3">Prepare Descriptive Model</td><td>Observation Sample</td><td>Full message history for first 12–15 months of 28 online communities.</td></tr><tr><td>Model Specification Sample</td><td>n = 9; randomly selected third of observation sample</td></tr><tr><td>Model Testing Sample</td><td>n = 19; remainder of observation sample</td></tr><tr><td rowspan="2">Run Simulation</td><td>Generate Data</td><td>For H1 test: 40 runs with each single mechanism setting (total n = 40 * 4 = 160)For H2 test: 50 Monte Carlo mechanism combinations with 20 runs per mechanism combination: total n = 20 * 50 = 1,000.</td></tr><tr><td>Validate Simulation Output</td><td>Comparison of model specification sample (n = 9) and simulation runs (n = 1,160)</td></tr><tr><td>Model Testing</td><td>Analyze Model</td><td>For H1 test: analysis sample (n = 40) compared to model testing sample (n = 19)For H2 test: analysis sample (n = 78) compared to model testing sample (n = 19)</td></tr></table>

## Calculate Outcome Measures

For the analysis of the simulation outcome measures from the model test sample were compared to output measures for the analysis sample. Table A8 provides the estimated power law distribution fit for online communities in the model testing sample.

<table><tr><td>Website</td><td>Est. Power Law Fit (R2)</td></tr><tr><td>bid-alot.com/forum</td><td>0.92</td></tr><tr><td>bibleworks.com/forums</td><td>0.94</td></tr><tr><td>forums.builtbp.com</td><td>0.96</td></tr><tr><td>archive.burningsea.com/forums</td><td>0.93</td></tr><tr><td>cruisersforum.com/forums</td><td>0.97</td></tr><tr><td>developers.evrsoft.com/forum</td><td>0.97</td></tr><tr><td>forums.foxitsoftware.com</td><td>0.98</td></tr><tr><td>fsdeveloper.com</td><td>0.91</td></tr><tr><td>gamefileforums.com/forums</td><td>0.97</td></tr><tr><td>jpsoft.com/forums</td><td>0.95</td></tr><tr><td>forums.mxhub.com</td><td>0.96</td></tr><tr><td>npowersoftware.com/forums</td><td>0.90</td></tr><tr><td>programmersresource.com/forum</td><td>0.95</td></tr><tr><td>stormlabstuff.com/board</td><td>0.91</td></tr><tr><td>teamd86.com</td><td>0.87</td></tr><tr><td>bb.turtlesoft.com</td><td>0.98</td></tr><tr><td>vintage-computer.com/vcforum</td><td>0.97</td></tr><tr><td>vjforums.com</td><td>0.92</td></tr><tr><td>forums.winxpcentral.com</td><td>0.97</td></tr><tr><td>Average Power Law Fit (n = 19)</td><td>0.944</td></tr><tr><td>Standard Deviation</td><td>0.031</td></tr></table>

## Appendix B

## Measuring Power Law Distributions

A power law distribution is a long-tailed distribution of the form: $\mathbf { y } = \mathbf { a x } ^ { b } .$ The b term is the power law distribution degree, a further measure of the shape of the power law distribution. A power law distribution’s fit is a statistical estimate of how closely an observed distribution is to a power law distribution. To accomplish this, the computationally parsimonious method of calculating a linear regression fit of the log-log rank-frequency cumulative distribution function (Newman 2005) is used.

This linear regression-based method for measuring a power law distribution has the advantages of computational simplicity and of generating an estimated $\bar { \mathsf { R } } ^ { 2 }$ value (Clauset et al. 2009). Although this method has been criticized for failing to differentiate between multiple types of nonnormal distributions and for potentially inaccurate estimations of power law distribution degree, it has been commonly used (Barabási and Albert 1999; Newman 2003) and is sufficient to identify which network mechanisms are consistent with the formation of the range of nonnormal distributions observed in our online community reference sample. Caution is warranted, however, in making precise determinations based on the reported power law distribution degrees or in making differentiations between various extreme forms of non-normal distributions (e.g., exponential and power law).

Arithmetic Scale  
![](/api/attachments/2YF2KDJ2/fulltext/images/417df281bd4407080fd0e522929ed47bfa837c6ac01838813a7d5ed98992d472.jpg)

Logarithmic Scale  
![](/api/attachments/2YF2KDJ2/fulltext/images/c6dff8e13979e4cc147fd6ae6e12d3f4cf3d127107927dacf65389181fd444b4.jpg)

Figure B1. Fit of In-Degree Distribution of Online Community jpsoft.com/forums to Power Law Distribution

The detailed procedure used to calculate the online community participant in-degree rank/frequency Pareto (Type 1) distribution fit is

1. A full year of network history is gathered from an online community (e.g., the model calibration and model testing subsamples) or generated via simulation.

2. In-degree is calculated for each network participant as the total number of messages posted by other participants to message threads started by focal participant.

3. Participants are rank ordered from highest in-degree to lowest in-degree. Zero values are dropped.

4. The upper probability from the cumulative distribution function of distinct rank values is calculated for each distinct rank (shown in left side of Figure B1

5. Both distinct rank values (Y-axis in Figure B1) and upper probability values (X-axis) are log-transformed (right side of Figure B1).

6. The transformed values are fitted with an OLS regression. The adjusted R<sup>2</sup> value is the estimated power law distribution fit. The estimated slope coefficient is the estimated power law distribution degree (the b coefficient).

Steps 4, 5, and 6 are implemented in R using functions developed by (Clauset et al. 2009).

## References

Andriani, P., and McKelvey, B. 2009. “From Gaussian to Paretian Thinking: Causes and Implications of Power Laws in Organizations,” Organization Science (20:6), pp 1053-1071.

Barabási, A. L., and Albert, R. 1999. “Emergence of Scaling in Random Networks,” Science (286), pp. 509-512.

Butler, B. S. 2001. “Membership Size, Communication Activity, and Sustainability: A Resource-Based Model of Online Social Structures,” Information Systems Research (12:4). pp. 346-362.

Clauset, A., Shalizi, C. R., and Newman, M. E. J. 2009. “Power-Law Distributions in Empirical Data,” SIAM Review (51:4), pp. 661-703.

Faraj, S., and Johnson, S. L. 2011. “Network Exchange Patterns in Online Communities,” Organization Science (22), pp. 1464-1480.

Kolaczyk, E. D. 2009. Statistical Analysis of Network Data: Methods and Models, Heidelberg: Springer Verlag.

Law, A. M., and Kelton, W. D. 2000. Simulation Modeling and Analysis, New York: McGraw-Hill.

Matei, A., and Tillé, Y. 2006. “The R ‘Sampling’ Package,” paper presented at the European Conference on Quality in Survey Statistics, Cardiff.

Newman, M. E. J. 2005. “Power Laws, Pareto Distributions and Zipf’s Law,” Contemporary Physics (46), pp. 7057-7062.

Preece, J. 2000. Online Communities: Designing Usability, Supporting Sociability, Chichester, UK: John Wiley & Sons.

R Development Core Team. 2009. “R: A Language and Environment for Statistical Computing,” R Foundation for Statistical Computing, Vienna, Austria

Ren, Y., Kraut, R., and Kiesler, S. 2007. “Applying Common Identity and Bond Theory to Design of Online Communities,” Organization Studies (28:3), pp. 377-408.

Sanchez, S. M., and Lucas, T. W. 2002. “Exploring the World of Agent-Based Simulations: Simple Models, Complex Analyses,” in Proceedings of the 34<sup>th</sup> Conference on Winter Simulation: Exploring New Frontiers, December 8-11, San Diego, CA, pp. 116-126.
