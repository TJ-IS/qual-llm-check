---
otero_id: 20721
otero_key: "CSCWWXKF"
title: "The social dilemma of big data: Donating personal data to promote social welfare"
authors: "Kirsten Hillebrand; Lars Hornuf; Benjamin Müller; Daniel Vrankar"
year: "2023"
journal: "Information and Organization"
doi: "10.1016/j.infoandorg.2023.100452"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The social dilemma of big data: Donating personal data to promote social welfare

![](/api/attachments/CSCWWXKF/fulltext/images/782a6bac6b38e9c3e2e8f86bbfcea6426211fef76367bf0cf8ab1821c31eadc9.jpg)

Kirsten Hillebrand <sup>a</sup>, Lars Hornuf <sup>b,\*</sup>, Benjamin Müller <sup>c</sup>, Daniel Vrankar <sup>c</sup>

<sup>a</sup> Bern University of Applied Sciences, Brückenstrasse 73, 3005 Bern, Switzerland

<sup>b</sup> Technische Universitat ¨ Dresden, Faculty of Business and Economics, Helmholtzstraße 10, 01069 Dresden, Germany

<sup>c</sup> University of Bremen, Faculty of Business Studies and Economics, Max-von-Laue-Straße 1, 28359 Bremen, Germany

## A R T I C L E I N F O

JEL classification: C71 H41 I18 O35 Q56

Keywords: Data governance Data philanthropy Sustainable development Decision-making Privacy Environmental protection Public health

## A B S T R A C T

When using digital devices and services, individuals provide their personal data to organizations in exchange for gains in various domains of life. Organizations use these data to run technologies such as smart assistants, augmented reality, and robotics. Most often, these organizations seek to make a profit. Individuals can. however. also provide personal data to public databases that enable nonprofit organizations to promote social welfare if sufficient data are contributed. Reg ulators have therefore called for efficient ways to help the public collectively benefit from its own data. By implementing an online experiment among 1696 US citizens, we find that individuals would donate their data even when at risk of getting leaked. The willingness to provide personal data depends on the perceived risk level of a data leak but not on a realistic impact of the data on social welfare. Individuals are less willing to donate their data to the private industry than to academia or the government. Finally, individuals are not sensitive to whether the data are pro cessed by a human-supervised or a self-learning smart assistant.

## 1. Introduction

In 2014, the United Nations (UN. 2014) called for the mobilization of individual data and initiated a global data partnership (http://www.data4sdgs.org) and database (https://www.sdg.org/#catalog) to promote environmental and social sustainability. Bevond the often-heralded conviction that “data is the new oil" (The Economist. 2017)—making issues of data governance (Otto. 2011) a key concern for companies all over the world—the UN’s initiative highlights the importance for organizations to collect, process, and store data on a large societal scale that goes beyond purely economic motives. The recent case of apps introduced to support national track-and-trace efforts to combat the spread of COVID-19 (e.g.. Care19 and Healthy Together in the United States Corona-Warn-App in Germany) provides additional evidence for how important data can be to promote a public good.

Many people disclose their data to digital service providers and risk their privacy in exchange for even small rewards (Acquisti et al., 2013). The willingness to share data for personal benefits is well documented in literature (Choi et al., 2018: Dienlin and Metzger, 2016; Dinev and Hart, 2006; Grossklags and Acquisti, 2007; Kim and Kim, 2018; Sun et al., 2015). However, while this literature provides an increasingly detailed understanding of the calculus people employ to trade off privacy risks with some specific benefit, projects such as the UN’s do not provide any such direct and immediate benefit. A key question thus becomes to what extent does current knowledge about people’s willingness to disclose and share data also support decision makers’ efforts in the context of a public good.

Our research is an important complement to current debates on whether traditional approaches to data governance, which are often rooted in corporate contexts where the collector of the data retains exclusive control over that data (Carballa Smichowski, 2019), are of limited value when public goods are concerned. Tensions arising from simply transferring such corporate or industrial logics to more civic logics have emerged, for example, in the contexts of personal health information (e.g., Winter and Davidson, 2019, Reddy et al., 2020) as well as public administration and government data (e.g., Benfeldt et al., 2020; Janssen et al., 2020). In response to these tensions, the data governance literature has begun to propose alternative governance models for managing data as a public good (e.g., Carballa Smichowski, 2019; Liu, 2022; Micheli et al., 2020; Zygmuntowski et al., 2021). While our work is closely linked to governance models such as public data trusts (Micheli et al., 2020), our focus remains on the individual level and the calculus people use when considering donating their personal data. Our study extends the data governance literature by providing valuable insights into the micro-level processes that macro-level governance approaches need to consider.

In our study, we conduct an online survey experiment in which we examine several factors that encourage people to provide personal data to a database that promotes social welfare. Specifically, we investigate how the stated willingness to donate persona data (WDPD) to a database changes depending on the perceived likelihood of that database to be large enough to allow for effective decision making in certain areas of life. Bevond this key characteristic of data as a public good, we account for the risk of data leakage. the characteristics of the organization that manages the database, and whether the data provided to the database are processed by humans or algorithmically, to be able to compare and integrate our findings with extant literature. Our experiments comprise two domains of social welfare: a sustainable environment and a sustainable health system, We chose these two domains because they are often related to public goods (Abdalla et al., 2020; Hardin, 1968) and play a crucial role in current debates on sustainable development. We find evidence that individuals are willing to donate their data to a database to promote social welfare, even if these data might be at risk of leakage. Evidence further shows that the risk level of a data leak is decisive for the WDPD but that varying levels of impact that data realistically can have on social welfare are not. Furthermore, as individuals’ perceived moral obligation to donate data rises, their WDPD rises as well. Finally, individuals are less willing to provide their data to profit-oriented organizations than to academia or the government.

In Section 2, we relate our research question to existing literature and develop testable hypotheses. In Section 3, we describe the empirical implementation of our online experiment. Section 4 presents the data and outlines the empirical results. Section 5 presents a discussion of our findings, after which Section 6 concludes the paper.

## 2. Theoretical considerations and hypotheses development

## 2.1. Related literature

## 2.1.1. Data disclosure and privacy

Different disciplines have investigated data sharing under privacy risks. Information systems scholars developed the privacy cal culus model in the context of technology usage (Dinev and Hart, 2006), which has become a well-established concept to investigate data sharing under privacy risks on an individual level.¹ In the privacy calculus model, the term “calculus" refers to a rational cognitive cost-benefit trade-off that technology users face: realizing the expected utility by disclosing personal data versus avoiding the anticipated costs of a privacy violation by not disclosing personal data (Culnan and Armstrong, 1999; Dinev and Hart, 2006). The individual decision of whether to disclose personal data or not depends on the respective outcome of this cost–benefit analysis. Empirical research evidences that the individual benefits are often perceived as outweighing the costs of privacy risks. Individuals are willing to share their personal data and take privacy risks to, for example, participate in social media networks (Choi et al., 2018; Dienlin and Metzger, 2016), receive financial rewards (Grossklags and Acquisti, 2007), make e-commerce transactions (Dinev and Hart, 2006), or receive personalized content or recommendations (Kim and Kim, 2018; Sun et al., 2015). The emergence of the Internet of Things (IoT) and the use of mobile devices have further accelerated the type of technology that enables data generation and sharing through, for example, smartphones (Keith et al., 2010; Maus et al., 2021) and other IoT devices such as refrigerators (Kim et al., 2019).

The digital marketing and behavioral sciences literature streams have extended the rational perspective of the privacy calculus model by examining attitudinal and contextual factors that work as antecedents of individual data disclosure. Factors that complement the cost–benefit analysis of the privacy calculus model include trust (Joinson et al., 2010), anonymity (Pu and Grossklags, 2017), sensitivity of information (Mothersbaugh et al., 2012), past privacy experience (Xu et al., 2012), extroversion and attitude (Chen, 2013), and social privacy norms (Zlatolas et al., 2015).

While this growing body of literature provides an increasingly refined understanding of the calculus individuals employ to determine whether or not to share sensitive personal data, it generally rests on the assumption that using digital services with privacy risk equals an exchange of data for personal benefits (Xu et al., 2009). However, this assumption can cause privacy calculus–based work to fail to adequately account for individuals’ WDPD in instances when “not the benefit of the single citizen […] is at stake […], but rather the combined utility on a societal level” (Hauff & Nilsson, 2023, p. 8). Because of the resultant understanding that pro-socia motives might also play an essential role in individuals’ privacy calculus (Hauff & Nilsson, 2023), we also need to explore literature on data philanthropy to understand how the calculus can be advanced to incorporate data donations to a greater good.

## 2.1.2. Data philanthropy

Especially owing to recent experiences with the COVID-19 pandemic, research and society at large have become sensitized to the benefits associated with large-scale data disclosure, be it through singular acts of sharing data or ongoing monitoring through, for example, connected smart devices. In cases in which sharing data benefits society at large rather than any one individual directly, how do individuals decide in a cost-benefit trade-off whether to disclose their personal data to increase social welfare rather than their personal utility? When individuals rely on the rational approach of the privacy calculus model, they may not find it worthwhile to share their data and risk their privacy to promote social welfare. Nevertheless, individuals might engage in self-sacrificing behavior and disclose personal data, even though it may be rational for them to prioritize the protection of their privacy rights over remote and often uncertain societal benefits. Such behavior can occur if individuals view data disclosure less as a rational exchange of goods and more as a morally and emotionally motivated donation to a good cause.

Data donation behavior has mostly been studied empirically in three contexts: data donation in academia, medical data donation, and data disclosure for terror and disaster control. Regarding data donation in academia, scholars have studied the donation of data from non-researchers to academia (e.g., Liu et al., 2017) and the sharing of data sets between researchers (e.g., Fecher et al., 2015). The donation of data from non-researchers to academia is associated with individual costs, such as effort and loss of control, while the benefits are favorable to the public in general. for example. in the form of new basic knowledge (Bezuidenhout. 2013: Breeze et al.. 2012). Through the sharing of data sets between researchers, new knowledge is generated by reanalyzing existing data (Woolfrey, 2009). Open access to data can also provide transparency and protect against academic misconduct (Chawinga and Zinn, 2019). Research investigating what drives non-researchers to donate their data to academia shows that key determinants include the perceived need for donation (Nov et al., 2014), the perceived reputation of the organization (Liu et al., 2017), altruism (Goncalves et al., 2013; Rotman et al., 2012), and social signals and attitude (Liu et al., 2017). Studies investigating what prevents researchers from sharing their data with the wider academic community have identified factors such as a loss of control and fear of misuse (e.g., Acord and Harley, 2012; Bezuidenhout, 2013), time and effort (e.g., Breeze et al., 2012; Chawinga and Zinn, 2019; Huang et al., 2013), and sociodemographic variables such as age. nationality, and character traits (e.g., Acord and Harley. 2012: Enke et al., 2012: Fecher et al., 2015).

While medical data are particularly sensitive (Soni et al., 2020), the factors influencing data donations in a medical and health context have considerable overlap with the findings from the academic domain. Research has shown that, for example, time and effort (Morse, 2007; Rudolph and Davis, 2005; Wright et al., 2010), and the fear of misuse (Lopez, 2010) influence the decision to donate data in the medical and health context. Moreover, research investigating the trade-off between security and privacy in the contexts of terrorist crises and disaster control shows that fear contributes significantly to people’s WDPD (Davis and Silver, 2004; Pavone and Esposti, 2012), despite the risk of data leakage.

Taken together, the literature thus far suggests that even if people do not benefit directly from the disclosure of their data, they are still willing to donate their data to protect the population from, for example, terrorist attacks (Reuter et al., 2016).

## 2.1.3. The social dilemma of big data

Although data donations are beneficial to society, they can also constitute a social dilemma: While society at large can potentially benefit from data donations, each individual has an incentive not to donate personal data because such donations come with persona privacy risks. Individuals might therefore freeride on the contributions of others—an inherent characteristic of a public good (Olson, 1965; Stroebe and Frey, 1982). However, if an insufficient number of people donate their data, the respective database is not usable to operate a data-driven technology, and everyone is worse off than had they cooperated and donated their data. Such social dilemmas are “situations in which a non-cooperative course of action is (at times) tempting for each individual in that it yields superior (often short-term) outcomes for self, and if all pursue this non-cooperative course of action, all are (often in the longer-term) worse off than if all had cooperated” (Van Lange et al., 2013, p. 126). The social dilemma of big data involves not only a social conflict (individual vs. collective interests) but also a temporal conflict (short-term ys. long-term consequences). For the individual. the protection of privacy expires immediately, while for society, the positive impact of a sufficiently large database comes with a time delay (Van Lange et al., 2013).

In the context of our work, this leads us to define the social dilemma of big data as a delayed public good dilemma. That is, in dividuals must give their data so that, over time, a large and diverse data set emerges that various organizations can then use with the goal to increase social welfare. Individuals cooperate in public good dilemmas, for example, because they feel a moral obligation (Chen et al., 2009), because they know that their cooperation contributes positively to the public good (Kerr, 1992), and because they believe that other individuals will also cooperate and contribute (Dawes et al., 1976). However, whether and to what extent these factors play a role in the cost-benefit trade-offs that underpin individuals’ privacy calculus when determining how to handle personal data remain unstudied to date.

Another important characteristic of the social dilemma of big data is uncertainty. When disclosing personal data for a public good, individuals face two types of uncertainty: environmental uncertainty (i.e., uncertainty about the situation and conditions for obtaining the public good) and social uncertainty (i.e., uncertainty about the decisions of others) (Orbell et al., 1988). Thus, individuals do not know the exact threshold of data required to generate a usable database that can increase social welfare. The critical data mass depends on factors such as data quality, variety, and use. Furthermore, individuals do not know whether a sufficient number of other people are also cooperating and donating their data and, thus, whether an increase in social welfare can be achieved. Both social and environmental uncertainty lead to lower cooperation rates in public good dilemmas (Wit and Wilke, 1998), in some cases through a reduced perceived obligation to cooperate (Fleishman, 1980).

Both these issues—the underlying motivations for data philanthropy and the social dilemma of big data—suggest that the current understanding of the calculus people employ to determine their WDPD cannot easily be transposed to a context in which data are donated for a public good.

## 2.2. Hypotheses development

The costs and benefits of a product or service affect individual behavior. This relationship applies to charitable donations (e.g., Acord and Harley, 2012; Bezuidenhout, 2013) and technology usage behavior (Dinev and Hart, 2006) as well. Privacy costs are centra in the disclosure of personal data. If an individual’s privacy is violated, he or she may face severe negative long-term consequences. For example, the leakage of financial, health, or location data can serve as a diagnostic measure of sensitive individual attributes, such as religious or political views and possible health concerns (Gambs et al., 2011). Consequently, and as we argued previously, the sharing of personal data for a public good structurally resembles a social dilemma

In developing our hypotheses, we rely on the literature that investigates cooperative behavior in self-sacrificing dilemmas under risk and social uncertainty. What influences individual decision making in a social dilemma is its payoff structure (e.g., Komorita and Parks, 1994; Rapoport, 1967). It is well documented that negative payoffs such as personal costs lead to significantly lower cooperation rates in social dilemmas (e.g., Cress et al., 2006; Dawes, 1980; Gangadharan and Nemes, 2009). Thus, we hypothesize the following:

Hypothesis 1a. A lower perceived privacy risk increases the WDPD to a database that can be used to promote social welfare.

It is important to note that hypothesis 1a structurally resembles one of the key tenets of the privacy calculus model (Dinev and Hart, 2006), though it takes the point of view of logics that govern people’s decisions in social dilemma situations, such as whether to cooperate or not in offering personal data to improve the public good. This resemblance is critical for our findings to integrate well with extant literature, even though our conceptualization of a database as a public good is a key shift in thinking.

The WDPD varies with the nature of the generated benefit (e.g., Dienlin and Metzger, 2016; Sun et al., 2015). Benefits can be symbolic, hedonic (e.g., additional values such as better service or offer personalization), and utilitarian (e.g., goods, monetary ad vantages) (Sun et al., 2015; Xu et al., 2009). Individuals weigh their own privacy costs against the enhancement of social welfare using a cost-effectiveness analysis, a subcategory of a cost-benefit analysis (Newcomer et al., 2015). The perceived effectiveness of donations or social behavior increases the willingness to actually donate or perform social behavior. The greater the positive outcome of a donation, the greater is the willingness to donate (Ye et al., 2015).

The same is true for certain contexts of data donation. For example, people are more willing to release their data for terrorism protection if they believe the data will have an impact (Reuter et al., 2016). In social dilemmas, the positive outcome of individua cooperation is expressed in payoffs. Uncertainty in payoffs typically reduces the willingness to cooperate (Budescu et al., 1990; Levat and Morone, 2013), for example, by providing a justification for noncooperative behavior (Van Dijk et al., 2004). Moreover, in dividuals are more willing to incur personal costs and contribute to a public good the higher the payoff levels, even if they are uncertain (Balliet et al., 2011; Dawes, 1980; Dickinson, 1998). Efficacy plays a major role in cooperative behavior as well (Kerr, 1992). The greater the impact an individual can have through a cooperative action such as data disclosure, the more willing he or she is to incur personal costs such as privacy risk. This suggests that a positive expectation in terms of making a meaningful difference will lead individuals to be more willing to donate their personal data to promote a database as a public good.

A key question here is how to frame such an impact to make it understandable and tangible enough for individuals to factor it into their calculus considerations. To examine the factors that encourage individuals to provide their data. we focus on smart assistants as a data-driven technology to increase social welfare. Smart assistants can convert large amounts of data into personalized information and thereby nudge users to make socially desirable choices (e.g., Mele et al., 2021; Weinmann et al., 2016), such as by selecting relevant information according to consumption patterns and providing tips that are tailored to individual habits and easy to follow. However, to be able to offer informed and comprehensive decision support, a smart assistant must have access to a sufficiently large database of diverse, timely, and trustworthy data. Similarly, big-data-based decision-support systems also allow for efficient energy management in households (Kolokotsa et al., 2009), support smart initiatives (Wolfert et al., 2017), and improve health care decisions by providing intelligently filtered information to health care professionals (Musen et al., 2014). In effect, scenarios based on a smart assistant are likely to help people understand and account for the potentially positive impact of their data donation. Thus:

Hypothesis 1b. A greater perceived impact of the database-driven smart assistant on social welfare increases the WDPD.

We argue that hypothesis 1b provides more concrete grounds than more generic postulates related to, for example, public policy making, in which data donors might not fully comprehend how their data are used. In our experimental setting, we make clear that the people providing the data do not necessarily need to be users of the smart assistant, because otherwise they would again think about their individual benefits. The smart assistant angle is meant to make the question of how the database generates positive impacts more tangible, but should not be misconstrued as an avenue to any direct personal benefit. Our scenario descriptions reflect this.

In a social dilemma with privacy risk as a personal cost, no direct personal payoffs, and uncertain and delayed societal payoffs, it may not be rational for individuals to donate their data based on a cost-benefit analysis. However, individuals might do so anyway, because they perceive data donation as the morally appropriate action. Decisions are not always an outcome of a cost-benefit analysis but can also be influenced by personal beliefs about what is right and wrong. The importance of normative concerns in the context of social dilemmas is emphasized in popular models, such as the appropriateness framework of Weber et al. (2004). The appropriateness framework posits that cooperation decisions are essentially influenced by factors that make individuals ask themselves: What should a person like me do in a situation like this? One of Weber et al.’s factors is the use of decision rules and heuristics, such as treating others as one would like to be treated. Morality plays a central role in general prosocial and environmental behavior (Van Liere and Dunlap 1978), in charitable-giving behavior (Sanghera, 2016), and cooperative behavior in public good dilemmas (Chen et al., 2009). People often judge the morality or the moral obligation of certain decisions based on utilitarian criteria (Kahane et al., 2015). According to classical utilitarianism, decisions should be made according to the criterion of maximizing social welfare, regardless of what would be best for oneself or loved ones (Bentham, 1789; Sidgwick, 1907). Moral judgments play a critical role in motivating and enforcing human cooperation in social dilemmas (Gray et al., 2012). One of the underlying mechanisms is that people experience positive emotions after behaving according to their perceived moral obligations (Andreoni, 1990) and negative emotions such as guilt or remorse when ignoring perceived moral obligations (Rivis et al., 2009). We therefore expect individuals to be more likely to donate their data if they perceive data donation as morally obligatory based on their internal norms.

Hypothesis 2a. The perceived moral obligation to donate data to a database is associated with a greater WDPD.

Emotion-based moral judgments are based on intuitions and feelings and are often formed quickly and intuitively (Greene et al., 2001; Haidt, 2007; Wheatley and Haidt, 2005). Moral reasoning then follows ex post and affects behavioral outcomes, such as the WDPD (see Fig. 1). In our case, a greater impact of a data donation triggers a positive emotion-based moral judgment, which translates into a positive moral reasoning and, thus, a higher WDPD. In quick and intuitive gut reactions, moral evaluations may differ even in nearly identical scenarios: moral evaluations are situation-specific and dependent on framing (e,g.. Krebs. 2008). Judging with utilitarian criteria, the greater the positive impact on social welfare from an action, the greater is the perceived moral obligation to perform this action. We thus argue that donating data could be perceived as morally more obligatory the greater the impact of the database-driven smart assistant on social welfare. The impact of the smart assistant on social welfare may thus support the decision to donate data because of an increased perceived moral obligation to do so. Moral judgments can also be self-serving if people evaluate actions differently when the consequences affect them personally and their loved ones than when a third group is affected (Greene, 2014). Thus, when a prosocial action implies negative consequences for the individual, such as the risk of a data leak, he or she subconsciously tends to evaluate an action as less morally obligatory. In this way, individuals intuitively reduce cognitive dissonance and negative emotions, if a prosocial action is not actually undertaken. We argue that donating data could thus be perceived as less morally obligatory the higher the privacy risk the individual thereby incurs

Hypothesis 2b. The perceived moral obligation to donate data mediates the effects of the privacy risk and the impact of the smart assistant on the WDPD.

If a person chooses to donate his or her personal data to support a public good such as a database, he or she will subsequently have no insight into whether the data will actually be used for the declared purpose, such as to increase social welfare. Given this uncer tainty, the reputation of the data-collecting organization is an important factor when making the donation decision. Bednall and Bove (2011) find that a positive reputation of the collecting organization motivated people to donate more blood. The more positive the organization's reputation. the greater are the perceived integrity and trustworthiness and the lower is the perceived risk associated with the donation. Comparable effects are also observed for other donation behavior. A charity’s reputation has a significant influence on whether a donation is taken into consideration (Bendapudi et al., 1996). Drawing on these findings, Liu et al. (2017) examined the interplay between the reputation of the collecting organization and the willingness to donate data to academia. The results highlight the relevance of reputation in the context of data donation: A positive reputation promotes a willingness to donate data. This rela tionship is driven by a reduced fear of privacy violation, a more credible need to donate, and a more positive attitude toward data donation in general.

Complementarily, the reputation of an organization influences the trust people have in it. Trust is an important driver of coop erative behavior (Balliet and Van Lange, 2013; Bednall and Bove, 2011) and is especially relevant in cooperation decisions under uncertainty (Yamagishi, 2011), which characterize data donation decisions with privacy risks and uncertain outcomes. We therefore assume that individuals ascribe different attributes to organizations that collect data to build a database to increase social welfare and accordingly, vary in their willingness to disclose data to them. In particular, we expect the willingness to donate data to academic and governmental organizations to be greater than that to the private industry, because the private industry primarily pursues profitmaximizing interests (Bhattacharjee et al., 2017; Eyster et al., 2021) and are generally trusted less to promote social welfare (Lin-Hi et al., 2015).

Hypothesis 3. The WDPD is different for a database operated by academia, the government, and the private industry.

![](/api/attachments/CSCWWXKF/fulltext/images/14a6c5742c6db7d1910d652ad512c7dbaa7e5db77ce83748a366c631722c8bb2.jpg)  
Fig. 1. Schematic representation of main hypotheses.

Computers and algorithms become increasing important components of decision-making processes (Esmaeilzadeh et al., 2015; Inthorn et al., 2015). Although individuals consistently rely on technological support to make decisions, they tend to rely less on algorithm-generated information than on human-generated information (Onkal <sup>¨</sup> et al., 2009). People tend to have an algorithm aversion (Dietvorst et al., 2015). This aversion is particularly pronounced when people have seen an algorithm generate erroneous information; even if the algorithm is known to provide better decision support on average than a human (Dietvorst et al., 2015). People are more intolerant of small errors made by algorithms than of large errors made by humans (Dietvorst et al., 2015). The technica nature of algorithms is increasingly characterized not only by automation but also by autonomy (Baird and Maruping, 2021). De Visser et al. (2018, p. 1409) define autonomy as “technology designed to carry out a user’s goals, but that does not require supervision.” Smart assistants, such as the one we propose in our discussion of hypothesis 1b, are based on autonomous algorithms as well. When investigating data donation choices, it is therefore important to consider that the technical nature of a smart assistant determines how the data are analyzed to derive personalized information such as specific tips and action recommendations.

![](/api/attachments/CSCWWXKF/fulltext/images/470f87622e4fb1aace0a1907033cdfd6d825433532f62d6dcbdbbddc1a04f0d4.jpg)  
Fig. 2. Schematic flow of the experiment and treatments.

We assume that, in simplified terms, two types of algorithms vary in their autonomy degrees. In case of a smart assistant with a selflearning algorithm, rules for personalization autonomously change depending on how the user reacted to past information. Conse quently, the selected personalized recommendation will also change over time, depending on the rules the smart assistant automat ically modified. In case of a smart assistant with a human-supervised algorithm, rules for personalization do not autonomously change depending on how the user reacted to past information; however, a human can manually change the rules. Consequently, the selected personalized recommendations will change over time, depending on the rules a human manually modified. We hypothesize that because of algorithm aversion, individuals would prefer a smart assistant whose decision support is not fully automated but can, to some degree, be modified by a human. Research on how to overcome algorithm aversion shows that people do not prefer complete autonomy and are significantly more likely to use even imperfect algorithms if they themselves can easily modify the algorithm (Dietvorst et al., 2018).

A data-driven technology’s service such as a smart assistant’s decision support for a large group of people or entire societies could not or only with disproportionate effort be entirely provided by humans. Despite this general constraint, the autonomy of the smart assistant could, however, be designed to varying degrees, as in the case of a human-supervised and self-learning smart assistant. Drawing from the literature on algorithm aversion, we therefore hypothesize that individuals would be more likely to donate their data to a database if the data were used to operate a smart assistant with reduced autonomy.

Hypothesis 4. The WDPD is greater for a database that is used to develop a human-supervised smart assistant than for a database that is used to develop a self-learning smart assistant.

## 3. Empirical implementation

## 3.1. Experimental design and interventions

We conduct an online experiment with treatments that rely on between-subjects and within-subject designs to test our hypotheses The experiment has a $3 \times 3$ design and is followed by an online survey to control for potential confounding variables and charac teristics. The experiment considers two domains, both of which include the identical 3 × 3 design but vary in the social welfare domain promoted by the smart assistant: a sustainable environment (domain 1) and a sustainable health system (domain 2). The experiment has been preregistered at the AEA RCT Registry and obtained ethical approval from the Ethics Commission of the University of Bremen.

Before participating in the experiment, individuals received an explanation that the UN has launched a call for more data to support the Social Development Goals and how a public good benefits from that data. Participants learned what a smart assistant is, how it can use data to promote the goals, and why it needs a sufficient amount of data to do so. Participants were further advised that the disclosure of data always involves certain privacy risk. We then provided the participants with the following scenario (domain $1 ) \colon { } ^ { \ast } \mathbf { A }$ smart assistant could support US users in living environmentally friendlier everyday lives, thereby promoting a sustainable envi ronment. Every English-speaking person with a smartphone in the United States could use the smart assistant. However, to develop and operate an assistant that offers informed and comprehensive decision support on environmentally friendlier behavior, there must be access to a sufficiently large database of diverse and trustworthy data. The database requires a given list of data sets in an anonymized form.” We asked participants to imagine that they could easily and anonymously upload their personal data to the database. Partic ipants were then asked to indicate their WDPD on a scale from 0 to 100% with no preset value. The stated WDPD is thus the result of the participants’ evaluation regarding donating data to the database, contributing to the development of the respective public good, and accepting a certain level of privacy risk. On the other hand, they could choose not to donate their data and completely avoid the privacy risk by not contributing to the development of the public good.

The actual experiment consisted of three parts. In part 1, we provided participants with one of three varying levels of risk of their data getting leaked (treatment 1) combined with one of three varving levels of the impact of the smart assistant on social welfare (treatment 2). We randomly assigned the participants to the domains and nine treatment combinations through a designated function of the software Unipark. Fig. 2 depicts an overview of the experimental procedure and treatments per domain

The operationalization of the risk treatment was identically for both domains using the following wording: “The risk of data being leaked from this type of database is approx. [0.001/10/20]%. This corresponds to the leakage of data from [1 of 1,000/10 of 100/20 of 100] individuals." Because no reliable academic quantification of data leak probabilities exists, we consider the risk interval between 0.001% and 20% realistic, in line with a recent report of a large cybersecurity company (Varonis, 2019). We also calibrated the chosen risk levels in a pretest with 195 students from the faculty of business studies and economics at the University of Bremen. In the online experiment, we showed all participants a list of data types they would provide if they donated, because the WDPD clearly depends on the categories of data to be provided (Phelps et al.., 20o0). The shown list of data categories came from the Personal Information Protection Commission (2013) (see also Lim et al., 2018).

The operationalization of the impact treatment was different for each domain. In domain 1, the smart assistant supported its US users in living environmentally friendlier everyday lives, thereby promoting a sustainable environment. We operationalized the impact treatment using the following wording (domain 1): “By giving informed and relevant decision support, the smart assistant decreases the yearly $\mathrm { C O _ { 2 } }$ emissions of each user by approx. [50/30/10]%. This corresponds to planting [440/264/88] trees per year per user.” To consider realistic impact levels of the smart assistant, the environmental impact is an approximate calculation of a person’s $\mathrm { C O _ { 2 } }$ savings potential based on statistics from the German Federal Environment Agency (2020). To give participants a more intuitive measure of the avoidable $\mathrm { C O } _ { 2 }$ emissions, we reported the equivalent number of trees that would be required to compensate for the respective $\mathrm { C O _ { 2 } }$ emissions. The calculations are based on statistics from Klein (2009). In domain $^ { 2 , }$ the smart assistant supported its US users in living healthier everyday lives, thereby promoting a sustainable US health system. We operationalized the impact treatment using the following wording: “By giving informed and relevant decision support, the smart assistant decreases the probability of getting sick by approx. [50/30/10]%. This corresponds to a [five-/three-/one-] day decrease per year in the user getting sick.” To consider realistic impact levels of the smart assistant, we calculated the impact on the health system according to a person’s potential for health improvement, in line with Nieman et al. (2011), who reports a negative relationship between regular physical activity and upper respiratory tract infections. To illustrate the potential impact of health improvements to the participants, we reported the equivalent number of days a person would be sick less per year. The calculation is based on statistics from the Harvard School of Public Health (2016) and Molinari et al. (2007)

All participants took part in part 1 of the experiment (see Fig. 2 for an overview). Then, they were randomly assigned to either part 2a or part 2b of the experiment. In part 2a and 2b, participants could choose between different databases when donating their personal data. All databases required the same data, had an identical privacy risk, and were used to develop a smart assistant that promotes one of the two social welfare domains. The risk and impact levels corresponded to the treatment combination assigned in part 1. The databases in part 2a differed in terms of the organization that operates the respective database to develop and run a smart assistant: academia was operationalized by an Ivy League university, the government was operationalized by a federal US agency, and a profitoriented organization was operationalized by a large US tech company. We chose this representation because it is specific enough for participants to have an idea about what sharing data with this organization means but, at the same time, does not identify a specific organization that might be associated with a particular trait. Given that our experimental samples come from the United States, the framing as domestic organizations is intended to minimized any potential confounding influence of cultural or regulatory differences. The databases in part 2b differed in terms of the technical nature of the smart assistant, which would be developed depending on the respective database: a smart assistant using a self-learning algorithm and a smart assistant using a human-supervised algorithm to derive personalized information such as specific tips and action recommendations to promote environmentally friendlier or more healthful user behavior. We did not operationalize the individual algorithm type further but explained it to participants (see Online Appendix A, part A5).

## 3.2. Target population and sample

We test our hypotheses on US citizens. Participants were recruited from the crowdworking platform Amazon Mechanical Turk (MTurk). Although a sample from MTurk is not necessarily representative of the US population, various studies have successfully replicated a wide range of established economic and psychological effects and empirically validated the use of MTurk as a useful data collection tool (Becker et al., 2012; Crump et al., 2013; Gibson et al., 2011; Schnoebelen and Kuperman, 2010), and relevant research that relies on MTurk respondents has achieved robust results (Bonnefon et al., 2016). Furthermore, MTurk samples are considerably more heterogeneous than student samples from laboratory studies (Hussy et al., 2010). Crowdworkers on MTurk have a particularly diverse backgrounds (Mason and Suri, 2012), which are crucial for the external validity of our results. Despite some known disad vantages of collecting data via MTurk, we decided on this platform because we consider it to be particularly suitable in our specifio context. Although an MTurk sample may be subject to selection bias because digital workers potentially have more digital experience than the general population, this is beneficial in our case: For crowdworkers who have a strong digital affinity and who use online services not only for private purposes, a data leak could also have professional consequences. The scenarios described are therefore more credible and closer to the reality of the MTurk crowdworkers. Moreover, as we also highlight in Section 4.7. in which we discuss their external validity, our findings also hold for a US census representative sample.

We targeted the online study exclusively at workers who are US citizens and over 18 years of age.<sup>2</sup> We executed the experiment by posting a human intelligence task (HIT) on MTurk. The HIT provided a description of the task, the participation requirements, compensation, and instructions on how to proceed. Interested MTurk workers were instructed to click on a survey link, which forwarded them to an online survey in Unipark. Participants received between US\$0.40 and US\$0.55 for taking part in the HIT, depending on how they answered incentivized items on the expected donation behavior of others and their social value orientation in the survey. On the last page of the survey, the workers received an automatically generated unique code that they had to enter back on the MTurk website to trigger their payment. Workers could only participate once in the HIT.

We collected the data over a two-day period (September 14 and 15, 2020). Of the 2552 workers who clicked on the link, 1916 filled out the online survey completely. Responses from workers were excluded from the data set if they stated being non-US citizens. The final sample includes responses from 1707 participants with an average response time of 12 min. In a pretest, the average response time was 19 min. Because we requested participants in the pretest to carefully check and note all potential ambiguities in our survey, we consider the shorter response time during the HIT reasonable. The participants were randomly assigned to the domains and treatments.

## 3.3. Variables

We consider two dependent variables. First, we investigate participants’ WDPD depending on the risk level and impact of the smart assistant. Second, we investigate their relative WDPD to different managing organizations and types of algorithms. To test hypotheses 1a and 1b, participants needed to indicate their WDPD on a 1–100 slider. We adapted the original wording of Bonnefon et al. (2016) to the activity of data donation. The variable is the response to the following question: “How inclined are you to upload your personal data to the database?” (0% = not at all likely; 100% = extremely likely)

To test hypotheses 2a and $^ { 2 \mathrm { b } , }$ , we measure the moral obligation to donate data. Participants indicated their moral obligation on a $^ { 5 \mathrm { - } }$ point Likert scale. We adapted the original wording of Kahane et al. (2015) to the activity of data donation. The variable is the mean response to the following two questions: “Do you think that there is a moral obligation for people to upload their personal data to the database?" (1 = It would be wrong for people to upload their personal data to the database: 3 = People don't have to upload their personal data to the database, but it would be nice if they did; 5 = People must upload their personal data to the database) and “How morally wrong is it if people do not upload their personal data to the database?” (1 = perfectly fine; 3 = neither fine nor wrong; $5 =$ deeply wrong).

To test hypothesis $^ { 3 , }$ we investigate the relative WDPD to each of the presented operating organizations of the database (academic, governmental, and profit-oriented organizations). WDPD and relative WDPD rely on the same question; however, the question items differ in their respective answering options (Bonnefon et al., 2016). For WDPD, participants responded using a single slider. To identify the relative WDPD variable, participants needed to use multiple sliders in relation to each other, with the sum of the sliders equaling 100. Thus, indicating their individual willingness to donate data to one of the databases negatively correlated with their willingness to donate data to the alternative database. We used related sliders because we are primarily interested in ranking the WDPD per operating organization rather than the absolute magnitude of WDPD per operating organization. Survey items that use fixed total budget par titioning are particularly suitable for examining rankings and differences between interdepend options (Conrad et al., 2005; Fabbris, 2013). To test hypothesis $^ { 4 , }$ we investigate the relative WDPD to each of the databases used to develop smart assistants with different degrees of human involvement (self-learning algorithm vs. human-supervised algorithm).

In addition to the variables of interest that enable us to test our hypotheses, we consider control variables on participants’ soci odemographic situation, values, and attitudes in the final part of the survey. We collected the following variables to test explanatory channels: the perceived benefit to the individual user relative to the perceived benefit to the general public from the smart assistant, perceived individual preference for a sustainable environment and health system, profit-orientation, and trustworthiness and technica skills of each operating organization as perceived by the participants. Because psychological and attitudinal characteristics can explain cooperative behavior that includes temporal conflicts and technology usage, we consider the following control variables: humanassistant trust (Madsen and Gregor, 2000), interpersonal trust (Eurobarometer, 2014), future time orientation (specifically time perspective and anticipation of future consequences) (Gjesme, 1979; Steinberg et al., 2009), self-reported health (Idler and Angel, 1990), self-reported environmentally friendly behavior (Idler and Angel, 1990), and risk attitude (Weber et al., 2002). Given their particular relevance in explaining cooperative behavior under uncertainty, we collected social value orientation (Murphy et al., 2011) and the anticipated behavior of others using monetary incentivized tasks, to encourage honest and realistic responses (see Online Appendix $\mathbf { A } ,$ part A7). The anticipated behavior of others is a measure of the degree to which one believes others contribute to the public good. We collected the following demographic variables: age, citizenship, education, gender, income, living standard, and political and religious orientation, Control variables are balanced across treatments and domains: of 39 balance checks, only the comparison of living standard per domain shows a significant unequal distribution across domains (see Online Appendix Tables B-M10/11).

## 3.4. Empirical approach

To test hypotheses 1a and 1b, we use a Kruskal-Wallis $\mathrm { t e s t } ^ { 3 }$ to determine whether we can reject the following $\mathrm { H } _ { 0 }$ in a betweensubjects design (mean value of WDPD = μ; treatments: $R =$ risk of data getting leaked, I = impact of the smart assistant; treatment levels: 1 = low, m = medium. h = high):

$$
H _ {0} (r i s k): \mu_ {R l} = \mu_ {R m} = \mu_ {R h}
$$

$$
H _ {0} (i m p): \mu_ {I l} = \mu_ {I m} = \mu_ {I h}
$$

The alternative hypotheses, which we test using Dunn’s pairwise comparison, are

$$
H _ {A} (r i s k): \mu_ {R l} > \mu_ {R m} > \mu_ {R h}
$$

$$
H _ {A} (i m p): \mu_ {I l} <   \mu_ {I m} <   \mu_ {I h}
$$

To test hypothesis 2a in a within-subject design, we use the following ordinary least squares regression:

$$
\mathrm{WDPD} = \beta_ {0} + \beta_ {1} M O + \beta_ {2} \mathrm{R} + \beta_ {3} \mathrm{I} + \beta_ {4} \mathbf {C} + \varepsilon ,\tag{1}
$$

where MO is perceived moral obligation to donate data and C is a vector of control variables, such as risk attitude and social value orientation. hypothesis 2a is identified when a high MO is associated with a greater WDPD.

We expect a low risk of a data leak and a larger positive impact of the smart assistant on social welfare to have a positive and direct effect on WDPD. However, MO may mediate the effect of risk of a data leak and the impact on social welfare on WDPD. We therefore perform a mediation analysis to investigate the extent to which the effects of these two explanatory variables on WDPD pass through MO in our baseline specification. For mediation analysis, we need to also estimate the following two regressions.

$$
\mathrm{WDPD} = \beta_ {0} + \beta_ {1} \mathrm{R} + \beta_ {2} \mathrm{I} + \beta_ {3} \mathbf {C} + \varepsilon ,\tag{2}
$$

$$
\mathbf {M O} = \beta_ {0} + \beta_ {1} R + \beta_ {2} \mathbf {I} + \beta_ {3} \mathbf {C} + \varepsilon ,\tag{3}
$$

The mediation for the risk of a data leak (hypothesis 2b) is identified when four conditions are met (MacKinnon et al., 2007). First, the risk of a data leak variable (R) has a significant effect on WDPD in Model 2. Second, the risk of a data leak (R) has a significant effect on the mediator variable MO in Model 3. Third. in Model 1 the mediator variable MO has a significant effect on WDPD. Fourth, the coefficient of $\beta _ { 1 }$ must be smaller in absolute terms in Model 1 than in Model 2. The mediation for the smart assistant’s impact on social welfare is identified analogously.

To test hypothesis 3, we examine whether we can reject the following H0 in a between-subjects design:

$$
H _ {0}: \mu_ {r W D P D (g o v)} = \mu_ {r W D P D (t e c h)} = \mu_ {r W D P D (a c a d)},
$$

where rWDPD is relative WDPD, gov is a federal US agency, tech is a large US tech company, and acad is an Ivy League university. The alternative hypothesis is

$$
H _ {A}: \mu_ {r W D P D (g o v)} <   \mu_ {r W D P D (t e c h)} <   \mu_ {r W D P D (a c a d)}.
$$

We test the specified relationships of the parameters with a common two-step multiple comparison test procedure (Kao and Green, 2008). First, we perform a Kruskal-Wallis test to check whether there are differences between the mean values. Second, we perform a post hoc analysis using Dunn’s method of pairwise comparison to test the direction of the differences between mean values.

To test hypothesis 4, we use a Wilcoxon signed-rank test to examine whether we can reject the following H0 in the between-subjects design:

$$
H _ {0}: \mu_ {r W D P D (S L)} \geq \mu_ {r W D P D (H S)},
$$

where SL is the self-learning algorithm and HS is the human-supervised algorithm.

Table 1  
Comparison of MTurk and Prolific samples.

<table><tr><td></td><td colspan="4">MTurk sample</td><td colspan="4">Prolific sample</td></tr><tr><td>Data collection period</td><td colspan="4">September 13–14, 2020</td><td colspan="4">July 4–6, 2022</td></tr><tr><td>Restrictions for participants</td><td colspan="4">US citizens only</td><td colspan="4">US citizens only, US-census calibrated sample (age, sex, ethnicity)</td></tr><tr><td>n</td><td colspan="4">1707</td><td colspan="4">368</td></tr><tr><td>Variable</td><td>Mean</td><td>Std. Dev.</td><td>Min</td><td>Max</td><td>Mean</td><td>Std. Dev.</td><td>Min</td><td>Max</td></tr><tr><td colspan="9">Variables of interest</td></tr><tr><td>WDPD</td><td>54.329</td><td>30.298</td><td>0</td><td>100</td><td>29.590</td><td>32.524</td><td>0</td><td>100</td></tr><tr><td>Moral obligation</td><td>3.028</td><td>0.933</td><td>1</td><td>5</td><td>2.197</td><td>0.756</td><td>1</td><td>4.5</td></tr><tr><td>Expected behavior others</td><td>52.453</td><td>24.065</td><td>0</td><td>100</td><td>34.745</td><td>19.178</td><td>0</td><td>85</td></tr><tr><td>Future time orient.</td><td>3.212</td><td>0.749</td><td>1</td><td>5</td><td>2.823</td><td>0.400</td><td>1</td><td>4.3</td></tr><tr><td>Human-assistant trust</td><td>3.325</td><td>0.810</td><td>0.875</td><td>5</td><td>2.704</td><td>0.725</td><td>1</td><td>5</td></tr><tr><td>Interpersonal trust</td><td>3.380</td><td>1.039</td><td>1</td><td>5</td><td>2.799</td><td>1.544</td><td>1</td><td>5</td></tr><tr><td>Risk attitude</td><td>3.013</td><td>1.058</td><td>0.750</td><td>5</td><td>1.921</td><td>0.726</td><td>0.75</td><td>4</td></tr><tr><td>Social value orient.</td><td>0.470</td><td>0.211</td><td>-0.284</td><td>1.071</td><td>0.518</td><td>0.225</td><td>-0.284</td><td>1.071</td></tr><tr><td colspan="9">Demographics</td></tr><tr><td>Age</td><td>38.152</td><td>26.279</td><td>18</td><td>990</td><td>46.049</td><td>16.237</td><td>18</td><td>85</td></tr><tr><td>Education</td><td>4.873</td><td>1.034</td><td>1</td><td>7</td><td>4.345</td><td>1.360</td><td>1</td><td>6</td></tr><tr><td>Female</td><td>0.425</td><td>0.495</td><td>0</td><td>1</td><td>0.508</td><td>0.501</td><td>0</td><td>1</td></tr><tr><td>Income</td><td>5.636</td><td>1.993</td><td>1</td><td>9</td><td>5.481</td><td>2.276</td><td>1</td><td>9</td></tr><tr><td>Living standard</td><td>3.481</td><td>0.839</td><td>1</td><td>5</td><td>2.834</td><td>0.859</td><td>1</td><td>5</td></tr><tr><td>Political views</td><td>3.361</td><td>1.086</td><td>1</td><td>5</td><td>2.451</td><td>1.214</td><td>1</td><td>5</td></tr><tr><td>Religious views</td><td>3.312</td><td>1.292</td><td>1</td><td>5</td><td>2.321</td><td>1.422</td><td>1</td><td>5</td></tr></table>

T<sub>a</sub>bl<sub>e</sub> 2  
P<sub>earson corre</sub>l<sub>a</sub>ti<sub>on ma</sub>t<sub>r</sub>i<sub>x o</sub>f d<sub>emograp</sub>hi<sub>cs</sub> b<sub>e</sub>li<sub>e</sub>f<sub>s an</sub>d <sub>a</sub>ttit<sub>u</sub>d<sub>es</sub>.

<table><tr><td></td><td>Variable</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td></tr><tr><td>1</td><td>WDPD</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>Moral obligation</td><td>0.642</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>Age</td><td>-0.016</td><td>0.004</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>Education</td><td>0.198</td><td>0.174</td><td>0.009</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>Female</td><td>-0.113</td><td>-0.142</td><td>0.006</td><td>-0.074</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td>Income</td><td>0.026</td><td>-0.028</td><td>0.046</td><td>0.265</td><td>-0.017</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td>Living standard</td><td>0.411</td><td>0.415</td><td>0.029</td><td>0.274</td><td>-0.081</td><td>0.213</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8</td><td>Political views</td><td>0.279</td><td>0.341</td><td>0.038</td><td>0.066</td><td>-0.102</td><td>0.034</td><td>0.383</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9</td><td>Religious views</td><td>0.280</td><td>0.336</td><td>0.017</td><td>0.122</td><td>-0.034</td><td>0.028</td><td>0.363</td><td>0.536</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10</td><td>Expected behavior others</td><td>0.474</td><td>0.412</td><td>0.011</td><td>0.074</td><td>-0.094</td><td>-0.004</td><td>0.332</td><td>0.295</td><td>0.298</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>11</td><td>Future time orient.</td><td>0.251</td><td>0.360</td><td>0.055</td><td>0.096</td><td>-0.082</td><td>-0.063</td><td>0.270</td><td>0.270</td><td>0.252</td><td>0.161</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>12</td><td>Human-assistant trust</td><td>0.623</td><td>0.608</td><td>0.005</td><td>0.176</td><td>-0.133</td><td>0.018</td><td>0.470</td><td>0.401</td><td>0.389</td><td>0.444</td><td>0.318</td><td>1</td><td></td><td></td><td></td></tr><tr><td>13</td><td>Interpersonal trust</td><td>0.425</td><td>0.415</td><td>0.036</td><td>0.211</td><td>-0.110</td><td>0.029</td><td>0.436</td><td>0.331</td><td>0.334</td><td>0.337</td><td>0.283</td><td>0.515</td><td>1</td><td></td><td></td></tr><tr><td>14</td><td>Risk attitude</td><td>0.522</td><td>0.596</td><td>-0.002</td><td>0.206</td><td>-0.210</td><td>0.050</td><td>0.555</td><td>0.501</td><td>0.463</td><td>0.422</td><td>0.399</td><td>0.664</td><td>0.522</td><td>1</td><td></td></tr><tr><td>15</td><td>Social value orient.</td><td>0.011</td><td>-0.018</td><td>0.037</td><td>-0.046</td><td>-0.013</td><td>-0.063</td><td>-0.040</td><td>-0.127</td><td>-0.066</td><td>-0.018</td><td>-0.036</td><td>-0.027</td><td>0.057</td><td>-0.085</td><td>1</td></tr></table>

![](/api/attachments/CSCWWXKF/fulltext/images/2f0959841a56fa64c1810c1346144e8722be4064a6d2c26f8df7071dcd0b8aed.jpg)  
Fi<sub>g.</sub> 3<sub>.</sub> WDPD <sub>an</sub>d <sub>mora</sub>l <sub>o</sub>bli<sub>ga</sub>ti<sub>on</sub> t<sub>o</sub> d<sub>ona</sub>t<sub>e persona</sub>l d<sub>a</sub>t<sub>a</sub>

## 4. Results

## 4.1. The willingness and perceived moral obligation to donate data for a public good

Table 1 reports the descriptive statistics for the variables of interest and demographics of the participants. Of the variables of interest, the WDPD and the expected behavior of others have the highest standard deviations. Moreover, we find strongly varying values for the WDPD, depending on the specific treatment combination. Our sample consists of approximately 57% male participants, with an average age of 28 years and an average education of a bachelor’s degree. The mean income is in the range of $\$ 35,001-\$ 50,000$ and the average participant is religious and oriented slightly to the right of the political spectrum. Table 2 shows the correlations between our variables of interest and participants’ demographics. We find strong correlations between both the WDPD and the mora obligation to donate personal data and human-assistant trust. Participants’ risk attitude also correlates with human-assistant trust. Table B-M3 in Online Appendix B provides an additional summary of the domain and treatment-specific control variables.

Fig. 3 reports the mean WDPD and the mean moral obligation to donate personal data. The average willingness to donate data to a database to promote social welfare is $5 4 . 3 3 \ : ( \mathrm { S D } = 3 0 . 3 0 )$ on a scale from 1 to 100. Although the central tendency bias (Choi and Pak, 2005; Douven, 2018) would suggest that survey participants ignore extreme values and choose the mean as an answer, Fig. 4 shows that the WDPD is widely distributed. Thus. a significant number of participants show a relevant tendency to donate their data for a public good. We conducted a Kruskal-Wallis test to investigate whether there are significant differences between the WDPD in the environment domain (55.10) and that in the health domain (53.50). The results $( p = . 2 7 3 )$ provide no evidence for such a difference. The average perceived moral obligation to donate personal data to promote social welfare is 3.03 on a scale of 1 to 5. Thus, the average participant feels an above-average moral obligation to donate data (Wilcoxon signed-rank test, $\cdot p < . 0 0 1 )$ . Note, however, that there are differences between the domains (Kruskal-Wallis test for equality across domains, $\begin{array} { r } { p = . 0 6 2 ) } \end{array}$ . The participants feel a slightly greater moral obligation to donate their data for a sustainable environment $( \mu _ { M O \_ e n \nu } { = } 3 . 0 6 )$ than for a sustainable US health system (μ = 2.99).

One potential reason for this difference is that the distribution of the perceived benefits to social welfare differs across domains. To account for the different characters of the two domains in explaining the results, we asked participants to indicate on a scale from 1 to 100 how much an individual smart-assistant user and the general public benefit in each domain of social welfare. We find that par ticipants believe that individual users benefit significantly more from a smart assistant that improves their personal health status $( \mu _ { u s e r \ : h e a l t h } = 4 7 . 3 1 )$ than from a smart assistant that improves their carbon footprint $( \mu _ { u s e r \ : h e a l t h } = 4 4 . 8 0 ;$ Kruskal-Wallis test for equality across groups, $p = . 0 1 4 )$ . By contrast, the public apparently benefits significantly more from a smart assistant that promotes a sus tainable environment $( \mu _ { p u b \_ e n \nu } = 5 4 . 7 4 )$ than from a smart assistant that promotes a sustainable US health system $( \mu _ { p u b \ : h e a l t h } = 5 2 . 1 0 ;$ Kruskal-Wallis test for equality across groups $\pmb { p } = . 0 1 1 )$ . The higher ascribed utility for the general public could be an explanation for a greater perceived moral obligation to donate data in the environment domain, though this greater moral obligation does not translate into a greater WDPD.

## 4.2. Effects of risk of data leak and data’s impact on social welfare when donating data

Is a low risk of a data leak and/or a high impact of the smart assistant on social welfare associated with a greater WDPD (hypotheses

![](/api/attachments/CSCWWXKF/fulltext/images/6110df07d6afe995e44a10e8e35379b82effff75969467f9d9d83804dac0af25.jpg)  
Fig. 4. Distribution of WDPD over all treatments.

## WDPD per risk-treatment condition

![](/api/attachments/CSCWWXKF/fulltext/images/0ffc6fecc6c1c7561843d44641ae6de5410ff14768c05f22e3e956700380ac8b.jpg)

Sustainable environment\*\*  
![](/api/attachments/CSCWWXKF/fulltext/images/c50a5e6549fcd9cec61b20928eca8363ab5d4b69460f1c7648957b56677172b7.jpg)

Sustainable health system\*  
![](/api/attachments/CSCWWXKF/fulltext/images/16819508a7f37b6c4048800d026a0345c90a45b59ad522212e527db4ab4b7978.jpg)

## WDPD per impact-treatment condition

Overall  
![](/api/attachments/CSCWWXKF/fulltext/images/62b69ac17046da7a58bc6c424d40fcb14e6ff7becf0e92930d3554a107aad147.jpg)

Sustainable environment  
![](/api/attachments/CSCWWXKF/fulltext/images/4fe180735b26bfbde8fc53390dbd52e95965e899b476e4f6a680a648d9cc98d3.jpg)  
Fi<sub>g.</sub> 5<sub>.</sub> WDPD <sub>p</sub>er treatment and domain

Sustainable health system  
![](/api/attachments/CSCWWXKF/fulltext/images/c16f439a9571d573f6d875abae035d955399ce657b1c2d6aa6d4f095321b133a.jpg)

1a and 1b)? To answer this question, we compare the WDPD to a database. Fig. 5 summarizes the results per treatment and domain. In the risk treatment, the Kruskal-Wallis test (Online Appendix B, Table B-M5) shows that the WDPD across the three treatment conditions varies significantly depending on the level of risk (p = .005). The WDPD differs significantly between a low risk leve $( \mu _ { W D P D \_ R l } = 5 7 . 6 0 )$ and higher risk levels (medium: μ $\scriptstyle { R m = 5 2 . 4 3 , p = . 0 0 2 ; }$ high: μ $_ { R h } = 5 2 . 9 1 , p = . 0 0 4 )$ . However, whether the risk of a data leak is medium or higher is irrelevant for individuals’ WDPD, as the Dunn’s pairwise comparisons show no signficant differences in the WDPD $( p = . 3 9 4 $ for the overall sample) under medium (10%) or high (20%) risk levels. The insensitivity to higher risk levels is striking given that the percentage-point difference between the medium (10%) and high (20%) risk levels is nearly identical to the percentage-point difference between the low (0.001%) and medium (10%) risk levels. It seems that individuals consider the difference between 0.001% and higher risk levels binary; that is, a 0.001% risk is considered “no” risk of a data leak, while a 10% and 20% risk are considered “some” risk of a data leak. This finding is noteworthy considering the general notion of prospect theory (Kahneman and Tversky, 1979) that people do not weight probabilities equally. In particular, the general overweighting of small probabilities and the underweighting of large probabilities should reduce the difference in the treatment effects for smal (0.001%) and medium (10%) risk levels. Thus, in light of the insights from prospect theory, the effect of risk levels is likely even stronger in reality than the one we find. While in our sample the WDPD differs between low and medium risk levels in the environ mental domain $\left( { { p } \mathrm { ~ = ~ } } . 0 0 6 \right)$ , we find no such differences in the US health system domain $( p = . 0 5 7 )$ . Thus, hypothesis 1a receives support in the sustainable environment domain but not in the US health system domain. This finding, however, might be due to the reduced sample size and lack of statistical power and is not necessarily an indicator that no differences exist in the US health system domain.

Table 3  
OLS regression with WDPD as dependent variable.

<table><tr><td rowspan="2">Domain</td><td colspan="3">DV: WDPD (OLS regressions)</td></tr><tr><td>Overall</td><td>Sustainable environment</td><td>Sustainable health system</td></tr><tr><td>Moral obligation</td><td>11.679***(0.787) (p &lt; .001)</td><td>10.209***(1.133) (p &lt; .001)</td><td>9.568***(1.102) (p &lt; .001)</td></tr><tr><td>Risk</td><td>-3.913***(0.697) (p &lt; .001)</td><td>-4.219***(0.984) (p &lt; .001)</td><td>-3.380***(0.938) (p &lt; .001)</td></tr><tr><td>Impact</td><td>-0.333(0.615) (p = .589)</td><td>-1.659*(0.845) (p = .050)</td><td>0.948(0.818) (p = .247)</td></tr><tr><td>Age</td><td>-0.029***(0.010) (p = .003)</td><td>-0.0425(0.053) (p = .419)</td><td>-0.026***(0.010) (p = .004)</td></tr><tr><td>Education</td><td>1.455***(0.526) (p = .006)</td><td>1.646**(0.696) (p = .018)</td><td>0.280(0.740) (p = .706)</td></tr><tr><td>Female</td><td>0.152(1.058) (p = .886)</td><td>0.702(1.436) (p = .625)</td><td>0.473(1.472) (p = .748)</td></tr><tr><td>Income</td><td>0.198(0.275) (p = .473)</td><td>0.0891(0.377) (p = .813)</td><td>0.471(0.378) (p = .214)</td></tr><tr><td>Living standard</td><td>1.903**(0.792) (p = .016)</td><td>1.580(1.076) (p = .143)</td><td>1.747(1.163) (p = .133)</td></tr><tr><td>Political views</td><td>-1.031(0.679) (p = .129)</td><td>-0.126(0.902) (p = .889)</td><td>-0.529(0.934) (p = .571)</td></tr><tr><td>Religious views</td><td>-0.680(0.578) (p = .240)</td><td>-1.193(0.798) (p = .135)</td><td>-0.304(0.749) (p = .685)</td></tr><tr><td>Expected behavior others</td><td>0.216***(0.027) (p &lt; .001)</td><td>0.133***(0.036) (p &lt; .001)</td><td>0.196***(0.038) (p &lt; .001)</td></tr><tr><td>Future time orientation</td><td>-0.935(0.757) (p = .217)</td><td>0.317(0.997) (p = .750)</td><td>-1.371(1.077) (p = .203)</td></tr><tr><td>Human-assistant trust</td><td>10.694***(1.117) (p &lt; .001)</td><td>6.760***(1.528) (p &lt; .001)</td><td>6.706***(1.624) (p &lt; .001)</td></tr><tr><td>Interpersonal trust</td><td>1.368*(0.729) (p = .061)</td><td>0.773(1.094) (p = .480)</td><td>1.548*(0.934) (p = .098)</td></tr><tr><td>Risk attitude</td><td>-0.593(1.050) (p = .572)</td><td>-1.330(1.436) (p = .355)</td><td>-0.822(1.371) (p = .549)</td></tr><tr><td>High risk attitude × risk</td><td>1.933***(0.687) (p = .005)</td><td>2.505**(0.972) (p = .010)</td><td>1.330(0.916) (p = .147)</td></tr><tr><td>Social value orientation</td><td>3.629(2.588) (p = .161)</td><td>4.817(3.440) (p = .162)</td><td>-0.552(3.504) (p = .875)</td></tr><tr><td>Benefits for the public</td><td>0.0210(0.087) (p = .809)</td><td>0.0523(0.112) (p = .642)</td><td>-0.026(0.091) (p = .770)</td></tr><tr><td>Benefits for each user</td><td>0.0240(0.087) (p &lt; .784)</td><td>0.0757(0.113) (p = .503)</td><td>-0.0622(0.092) (p = .498)</td></tr><tr><td>Pref. database for environment</td><td></td><td>6.522***(1.017) (p &lt; .001)</td><td></td></tr><tr><td>Pref. sustainable environment</td><td></td><td>2.849***(0.920) (p = .002)</td><td></td></tr><tr><td>Previous environmental behavior</td><td></td><td>-0.280(0.984) (p = .0776)</td><td></td></tr><tr><td>Pref. database for health</td><td></td><td></td><td>7.411***(1.074) (p &lt; .001)</td></tr><tr><td>Pref. sustainable health system</td><td></td><td></td><td>-0.298(0.911) (p = .743)</td></tr><tr><td>Previous health behavior</td><td></td><td></td><td>1.816*(1.037) (p = .080)</td></tr><tr><td>Constant</td><td>-32.92***(9.770) (p = .001)</td><td>-45.16***(13.000) (p = .001)</td><td>-35.11***(11.400) (p = .002)</td></tr><tr><td>Observations</td><td>1704</td><td>862</td><td>842</td></tr><tr><td> $R^2$ </td><td>0.544</td><td>0.581</td><td>0.590</td></tr></table>

Note: Results are reported overall and per domain. Robust standard errors are reported in parentheses. OLS = ordinary least squares. $^ { * } p < . 1 ; ^ { * * } p <$ $. 0 5 ; ^ { \ast \ast \ast } p < . 0 1$

In the impact treatment, the results from the Kruskal-Wallis test and Dunn’s pairwise comparisons show that WDPD does not differ for the varving treatment levels of the smart assistant's impact on social welfare based on realistic values, neither overall $\left( { p = . 8 4 4 } \right)$ nor in either of the two domains (environment: $p = . 4 3 0 ;$ ; US health system: $p = . 6 2 6 )$ . The extent of the positive impact of the smart assistant on a sustainable environment or US health system appears largely irrelevant to the decision to donate data for realistic impact levels. Considering this result, we tested whether possibly unrealistically small impact levels (1% and 0.001%) make a difference for WDPD. In a non-preregistered experiment on Prolific with 368 participants, we find that participants overestimate the impact of the 0.001% impact treatments, especially in comparison with the 1% and low impact treatment (Online Appendix C. Fig. C3). Note that such extreme low levels of an impact make the treatment work for the overall sample (Kruskal-Wallis test for equality across groups, p $= . 0 0 6 )$ and the domain sustainable health system (Kruskal-Wallis test for equality across groups, $\underline { { p } } = . 0 4 5 )$ , which is interesting from an experimental standpoint (Online Appendix B, Table B-P9). However, these benefit levels are not realistic, which is why they do not help in the policy debate. Thus, we find no support for hypothesis 1b in line with our preregistered, realistic treatment levels.

## 4.3. Effect of perceived moral obligation when donating data

Is a high perceived moral obligation to donate personal data associated with a greater WDPD $( \mathrm { H } _ { 2 \mathrm { a } } ) ?$ If so, does the perceived moral obligation mediate the effect of risk or impact on the WDPD $\mathrm { ( H _ { 2 b } ) _ { : } }$ , or does it have a direct effect only? To answer these questions, we run three regressions.

Table 3 shows the regression results of Model 1 for the overall sample and the sustainable environment or US health system domain. The results show that a greater moral obligation to donate personal data is significantly associated with a greater WDPD $( p < . 0 0 1 )$ . An increase of the MO of one scale point increases the WDPD by 12 percentage points. The impact of MO on WDPD also holds when differentiating between the two domains of social welfare (sustainable environment: $\beta = 1 0 . 2 0 9 ; p < . 0 0 1$ ; sustainable US health system: $\beta = 9 . 5 6 8 ; p < . 0 0 1 )$ . Moreover, despite the correlation of WDPD, MO, and human-assistant trust, in the overall multivariate setting both explanatory variables are statistically significant, which shows that multicollinearity is not undermining the statistical significance of the explanatory variables. Thus, hypothesis 2a is supported and cannot be empirically rejected. The control variables with a positive and significant effect on WDPD are living standard $( \beta = 1 . 9 0 3 ; p = . 0 1 6 )$ , education $( \beta = 1 . 4 5 5 ; p = . 0 0 6 )$ , humanassistant trust $( \beta = 1 0 . 6 9 4 ; p < . 0 0 1 )$ , interpersonal trust $( \beta = 1 . 3 6 8 ; p = . 0 6 1 )$ , and the anticipated data donation behavior of others $( \beta = 0 . 2 1 6 ; p < . 0 0 1 )$ ; only age $( \beta = - 0 . 0 2 9 ; p = . 0 0 3 )$ has a negative and significant effect on WDPD. Model 1 further supports the previous results regarding the relevance of risk $( p < . 0 0 1 )$ and shows no significant effect for the smart assistant’s impact levels on WDPD, except for the domain of a sustainable environment $( \beta = - 1 . 6 5 9 ; p < . 0 5 0 )$ . Furthermore, while the risk level of the experi mental treatment affects the WDPD, our validated survey measure of individual risk attitude (Weber et al., 2002) does not. Thus, WDPD is highly correlated with the perceived risk of a data leak in general but not with the risk attitudes of the respective individual. We also split the risk attitude variable at the median and test whether more risk-taking individuals are also more strongly affected by the level of risk of the treatment in our regression setting. We find that individuals with an above-median risk attitude are also less reluctant to donate their data, even if the risk of a data leak increases. This observation is statistically significant for the overall sample $( p = . 0 0 5 )$ and the sustainable environment domain $( p = . 0 1 0 )$

Table 4 gives on overview of the mediation analysis results from regression Models 2 and 3. Overall and in both domains, three of the four mediation conditions are met in the risk treatment. Only the significance of the negative effect of risk on the perceived moral obligation is not statistically significant at conventional levels (overall: $\beta = - 0 . 4 3 2 ; p = . 0 5 1 )$ . In the impact treatment, the mediations conditions 2 and 4 are mainly not met. A differentiation between the domains also shows that there is no empirical support for hy pothesis 2b.

## Table 4

Summary of mediation analyses results per treatment and domain.

<table><tr><td rowspan="2">Mediation conditions</td><td colspan="2">Overall</td><td colspan="2">Sustainable environment</td><td colspan="2">Sustainable health system</td></tr><tr><td>Risk</td><td>Impact</td><td>Risk</td><td>Impact</td><td>Risk</td><td>Impact</td></tr><tr><td>1. Sig. effect of  $R / I$  on WDPD in Model 2</td><td>✓</td><td>X</td><td>✓</td><td>X</td><td>✓</td><td>X</td></tr><tr><td>2. Sig. effect of  $R / I$  on MO in Model 3</td><td>X</td><td>X</td><td>X</td><td>X</td><td>✓</td><td>X</td></tr><tr><td>3. Sig. effect of MO on WDPD in Model 1</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>4. Coefficient of  $\beta_1$  is smaller in Model 1 than in Model 2</td><td>✓</td><td>X</td><td>✓</td><td>X</td><td>X</td><td>X</td></tr><tr><td>Total conditions met</td><td>3 / 4</td><td>1 / 4</td><td>3 / 4</td><td>1 / 4</td><td>3 / 4</td><td>1 / 4</td></tr></table>

Database managed by...  
![](/api/attachments/CSCWWXKF/fulltext/images/1c643df4baa9f5d8d8d98c58680f27ca9fcd17442e93e63c6d7d3d3c772ef2e8.jpg)  
Fi<sub>g.</sub> 6<sub>.</sub> Relative WDPD <sub>p</sub>er o<sub>p</sub>eratin<sub>g</sub> or<sub>g</sub>anization

## 4.4. How the operating organization of the database matters when donating data

Is the WDPD different for a database operated by academia, the government, or the private industry? Fig. 6 reports the mean relative WDPD per domain and operating organization. The Kruskal-Wallis test results show that the WDPD varies significantly depending on which organization manages and operates the database to develop a smart assistant $( p = . 0 1 9 )$ (Online Appendix B, Table B-M5). The WDPD is significantly lesser when the database is operated by the private industry $( \mu _ { p r } = 3 0 . 5 1 )$ than by academia $( \mu _ { a c } = 3 3 . 0 9 ; p =$ .021) or the government $( \mu _ { g o \nu } = 3 3 . 7 6 ; p = . 0 0 3 )$ . However, individuals are statistically indifferent when the database is operated by academia or the government $\left( { p = . 2 4 6 } \right)$ . In the environment domain, the WDPD is lesser if the database is managed by the private industry $( \mu _ { p r \_ e n \nu } = 3 0 . 3 4 )$ than by the government $( \mu _ { g o \nu \_ e n v } = 3 4 . 6 2 ; p = . 1 0 0 )$ , and individuals are nearly indifferent whether the database is operated by academia or the government $\left( p = . 0 8 1 \right)$ . In the health domain, the average WDPD values show a similar tendency in absolute terms; however, Dunn’s pairwise comparison results show no statistically significant differences on conventional levels.

Our data provide a potential reason for the significantly lesser WDPD in case of an operation by the private industry. The survey questions asked participants to indicate how skilled they believe each operating organization is to develop a smart assistant and how trustworthy and profit oriented each organization is. The results of a pairwise comparison following Dunn’s method show that par ticipants perceive the private industry as more skilled in the development of a smart assistant than academia $( p < . 0 0 1 )$ or the gov ernment $( p < . 0 0 1 )$ , but also as significantly less trustworthy (academia: $p < . 0 0 1 ;$ government: $p = . 0 1 1 )$ and more profit oriented (academia and government: $p < . 0 0 1 $ . A regression analysis on the relative WDPD to the private industry verifies that high trust worthiness and low-profit orientation are significantly associated with a greater relative WDPD, but skill in developing a smart assistant is not (Online Appendix B, Table B-M7). An analogous comparison of the relative WDPD to academia and government also contributes to the explanation of the results. Participants perceive academia as slightly more trustworthy and skilled than the government. In addition, they perceive academia and the government to be less profit oriented than the private industry.

In summary, while there is no significant difference in the WDPD depending on whether the database is operated by academia or the government, operation by private industry is associated with a lesser WDPD overall and in each domain. Overall, we find support for hypothesis 3, which cannot not be empirically rejected.

## 4.5. How the type of algorithm matters when donating data

Is the WDPD greater for a database that is used to develop a human-supervised smart assistant than for a database that is used to develop a self-learning smart assistant? To answer this question, we compare the WDPD to each database using Wilcoxon signed-rank tests (Online Appendix B, Table B-M8). The results show that the algorithm type does not affect the WDPD either overall $( p = . 1 6 2 )$ or in the health domain $( \boldsymbol { p } = . 9 1 8 )$ . In the environment domain, the results show a tendency for participants to prefer a self-learning over a human-supervised smart assistan $( p = . 0 3 2 )$ . Overall, we find no empirical support for hypothesis 4. The type of algorithm is not decisive for the WDPD.

## 4.6. Manipulation check

As a manipulation check, we test whether participants perceived realistic risk and impact levels differently, given the established measures we have used. We therefore asked participants to assess the likelihood that their personal data would be leaked from the database and to assess the smart assistant’s impact on a sustainable environment or health system. We used the following items on a 5- point Likert scale: “Assess the likelihood that vour personal data will be leaked from the database" (1 = extremely unlikely: $5 =$ extremely likely) for the risk treatment, and “Assess the impact of the smart assistant on a sustainable environment [health system]” ( = no impact; $5 = { \mathrm { m a j o r } }$ impact) for the impact treatment. We ran a Kruskal-Wallis test followed by Dunn’s pairwise comparison to check whether participants actually perceive the risk and impact levels to be different across treatment conditions (see Online $\mathsf { A p - }$ pendix B, Table B-M9). The results are identical to those of the Kruskal-Wallis tests used to identify hypotheses 1a and 1b. When testing whether participants perceived realistic risk and impact levels differently, we find that they perceive the risk differently in case of a low risk level as compared with a medium risk level and high risk level. However, participants do not perceive a medium and high risk leve to be different from each another in the health domain. which indicates that they indeed consider the difference between 0.001% and higher risk levels as binary. Participants, however, do not perceive the smart assistant’s impact levels to be different. This finding is in line with the notion that the benefits of a smart assistant are attributed to society at large, and the individual share might be considered too small in large groups to make contributions worthwhile (Olson, 1965). In a broad sense, it is also consistent with a recent experimental result by Heeb et al. (2022). who evidence that investors put emphasis on whether an investment has a sustainable impact, but not how high the impact level actually is. The perceived indifference between impact levels is also a potential reason for the results of the main analysis, according to which the impact is not decisive for the individual WDPD to promote social welfare. We chose all impact levels on the basis of realistic assumptions and in line with real-world conditions.

## 4.7. Simplified scenario and external validity

We further tested whether the scenario is well understood and our findings externally valid. For this reason, we generated a scenario that used simpler language and, more importantly, employed a “chatbot” instead of a “smart assistant,” which may be better known to a large audience from personal experience (see Online Appendix A. part A8). We ran this simplified scenario on a US census representative sample of 368 participants on Prolific. Table 1 shows the summary statistics. In particular, we find that the overal WDPD and moral obligation to donate data were lower than those in the MTurk sample; however, the distributions of the respective variables were similar. We observe the same results for our risk treatments, with the exception of the difference between low risk and medium or high risk, which are now statistically different from the 1% level for the sustainable health domain. For our impact treatment, we now observe a statistically significant difference (Dunn’s pairwise comparison, $p = . 0 1 4 )$ between the WDPD in the low, medium, and high impact scenarios for the overall sample. Furthermore, we now find a statistically significant difference in the high versus low impact treatment and for the medium versus low impact treatment. However. the difference between the perceived moral obligation to contribute data for a sustainable environment and for a sustainable health system is no longer significant at conventiona levels (Kruskal-Wallis test for equality across groups, $p = . 0 6 2 )$ . We also find a stronger difference between the relative WDPD depending on the managing party (academia, government, or private industry). We find that this difference is statistically significant for the overall Prolific sample and the two domains, compared with a significant difference only for the overall sample and the sus: tainable environment domain for the MTurk sample. In addition, the relative WDPD to the private industry differs significantly (Dunn’s pairwise comparison, $p < . 0 5 )$ from the other two managing parties. We now also find stronger statistical evidence for our hypothesis that the WDPD differs depending on whether the smart assistant is self-learning or human supervised in the overall sample and the sustainable environment domain (see Online Appendix B, Table B-P8). Overall, we find stronger and more statistically significant results in the US census representative sample. Table 5 provides an overview and comparison of the results for the MTurk and US census representative Prolific sample.

As the recent emergence of tracing apps has shown. the number of people who contribute by donating their data can be critical to the effective functioning of the public good (Hinch et al., 2020; O’Neill, 2020). Therefore, we defined four levels that are necessary for the chatbot to work effectively. In line with O’Neill (2020), we varied whether 14%, 28%, 42% or 56% of the population had to contribute for the chatbot to work effectively. In another experiment on Prolific with 290 participants, we mentioned the respective minimum contribution level to the public good just before they indicated their WDPD. We find no evidence that the mean WDPD or the perceived moral obligation to donate data depends on the level of contribution necessary for the chatbot to work effectively, as the results from a Kruskal-Wallis test show $\left( p = . 9 7 3 \right)$ . However, our incentivized measure capturing the expected donation behavior of others, which accounts for the perceived contribution to the public good, does have a significant effect on the WDPD (see Table 3).

Finally, despite the concern that our results may not be valid because of experimenter demand effects or social desirability bias (Antin and Shaw, 2012), putting participants’ data at real risk would have been neither ethical nor practical. Moreover, according to Dohmen et al. (2011), with regard to risk, survey questions are often internally and externally valid. If anything, we expect the selfreported WDPD to be somewhat higher than the actual data donation behavior, because information privacy research shows an intention–behavior gap in self-disclosure (e.g., Joinson et al., 2010; Liu et al., 2017). Conversely, when data are donated in a real-world setting without our scenario description, people might disclose more information about themselves because the privacy risk is made less salient (Marreiros et al., 2017). In summary, if an experimenter demand effect exists in our survey experiment, positive and negative effects may well cancel each other out.

## 5. Discussion

We consider four issues central to the scholarly contribution of our work. First, we advance understanding of the factors that in dividuals consider in their calculus when determining when and under what conditions to share personal data. An extensive literature on the sharing of data has emerged in the past two decades. To this end, our work provides a twofold contribution. On the one hand, extant literature often neglects the social dilemma of data sharing and frequently presumes that data from a single individual alone are

## Table 5

Summary of results for the MTurk and Prolific sample.

<table><tr><td rowspan="2">Hypotheses</td><td colspan="2">Results</td><td rowspan="2">Method</td></tr><tr><td>MTurksample</td><td>Prolificsample</td></tr><tr><td>1a: A lower perceived privacy risk increases the WDPD to a database that can be used to promote social welfare.</td><td> $\checkmark^{1,2}$ </td><td> $\checkmark^2$ </td><td></td></tr><tr><td>1b: A greater perceived positive impact of the database-driven smart assistant on social welfare increases the WDPD.</td><td>X</td><td>X</td><td>Kruskal-Wallis test</td></tr><tr><td>2a: The perceived moral obligation to donate data to a database is associated with a greater WDPD.</td><td>√</td><td>√</td><td>OLS-regression</td></tr><tr><td>2b: The perceived moral obligation to donate data mediates the effects of the privacy risk and the impact of the smart assistant on the WDPD.</td><td>X</td><td>X</td><td>Testing the four conditions necessary for meditation (MacKinnon et al., 2007).</td></tr><tr><td>3: The WDPD is different for a database operated by academia, the government, and the private industry.</td><td> $\checkmark^3$ </td><td> $\checkmark^3$ </td><td>Kruskal-Wallis test &amp; Dunn&#x27;s method of pairwise comparison</td></tr><tr><td>4: The WDPD is greater for a database that is used to develop a human-supervised smart assistant than for a database that is used to develop a self-learning smart assistant.</td><td>X</td><td> $\checkmark^1$ </td><td>Wilcoxon signed-rank</td></tr></table>

utilizable (Cai and Zhu, 2015; UN, 2014). Our study differs from this literature in that it shows how individuals donate personal data in a scenario in which the corresponding database must be sufficiently large and diverse to develop and operate a technology that promotes social welfare. We thus shed light on the social dilemma of big data and provide insights into how society can benefit from the value of personal data. On the other hand, as argued previously, research has begun arguing that orthodox work based on a privacy calculus perspective fails to adequately account for individuals’ WDPD in instances when “not the benefit of the single citizen […] is at stake […], but rather the combined utility on a societal level” (Hauff & Nilsson, 2023, p. 8). In contrast with work that emphasizes different direct benefits, we complement the literature by exploring how individuals intend to act in situations when their donations contribute to building a public good.

Second, our study provides important complementarities to research that sheds light on how individual data donations to a public good can be encouraged. Recently, this issue has been at the heart of public and policy debates on strategies to mitigate the COVID-19- induced public health crisis. Other examples in which the mobilization of individual user data can promote social welfare include the tracking of human migration to ensure medical support during an earthquake (UN, 2015) and the tracking of deforestation combining satellite imagery and citizen-generated data (UN, 2020). In the future, data mobilization will become technologically feasible in evermore scenarios and increasingly relevant because of the simultaneous increase in data availability and global challenges. While understanding of the influence of digital technologies on various aspects of sustainable development—as expressed, for example, in the UN's Sustainable Development Goals—remains ambiguous (Popkova et al., 2022). it stands to reason that any data-driven technology’s ability to provide positive impacts rests on the availability of high-quality data that provide a faithful and current representation of the population. In this context, our study’s focus on willingness to donate thus provides an important complementary perspective to other current work investigating people’s willingness to use corresponding apps. For example, Naous et al. (2022) unpack aspects of app design that can positively influence users’ WDPD.

Third, our findings demonstrate an important link between users’ WDPD as a micro-level mechanism and broader organizationa and societal perspectives on macro-level data management. Understanding such connections is important, as the legal, societal, and ethical norms governing data—particularly big data—must not be viewed as mere matters of organizational structuring, but rather as comprehensive socio-technical imaginaries (Guay and Birch, 2022). Understanding the calculus that individuals use in deciding whether or not to donate personal data is essential to properly considering their perspective and upholding their rights as important stakeholders. This is particularly true given recent efforts to shift the discourse on the norms guiding technology and data use into a more ecosystem-based perspective in relation to data governance (e.g., Lis and Otto, 2021) and consumer protections more broadly (e. g., Mueller, 2022; Stahl, 2022).

Fourth, our research also makes a methodological contribution by showing that our results from the MTurk sample are largely identical to the US census representative sample. Given the externally valid results of the Mturk data, our research provides additiona corroboration of the findings of Schnoebelen and Kuperman (2010), Gibson et al. (2011), Becker et al. (2012), and Crump et al. (2013).

Beyond academia, our study also has important implications for decision makers, especially in light of recent policy developments On February 23, 2022, the European Commission voted to adopt the Regulation on harmonized rules on fair access to and use of data—also known as the Data Act. As part of the European Strategy for Data, the new legislation seeks to provide a set of rules to govern who can use and access what data for which purposes across all economic sectors to help companies build innovative data-based business models, improve citizens’ ability to protect their personal data, and enable societies to harness some of the potential asso ciated with digital transformation at large. For example. the EU estimates that a better use of data could unburden the union's health sector by up to EUR 120 bn each year (European Commission, 2022a) and that “consumers and users […] will be in a position to take better decisions such as buying higher quality or more sustainable products and services, contributing to the Green Deal objectives” (European Commission, 2022b). The legislation and debate behind the Data Act acknowledge the continued transition of economies around the globe to data economies. In such economies, data governance is critical to developing transparent, reliable, and enforceable structures that guide individuals, organizations, and institutional actors in their actions related to data. Data governance to increase social welfare particularly suggests the distribution of more rights to the individual (Van Zoonen, 2020). In this context, our study helps organizational decision makers better understand citizens’ perspective on the use of their data, so that their perspective can be understood and taken into account when undertaking data-based decision making to address the challenges of the times. Despite recent advancements such as the Data Act and user-centric data management models (e.g., Garcia-Font, 2020; Lepri et al., 2017; Qiu et al., 2019), society still lacks a coherent and large-scale approach to data governance that makes civic data sharing for social welfare just as easy and natural as sharing data with private industry for commercial purposes and individual benefits.

## 6. Conclusion

In a survey experiment using hypothetical scenarios, we provide empirical evidence that individuals are willing to donate their data to a database to promote social welfare, even if these data might be at risk of leakage. The evidence of our online experiment further shows that the risk level of a data leak is decisive for the WDPD but that varving levels of impact that data realistically can have on social welfare are not. A potential explanation for this finding is that for the individual, the consequences of a data leak are direct and privacy protection expires immediately in case of a data leak, while the positive impact of a sufficiently large database arises with a time delay, and the individual only benefits to a small degree from its contribution (Van Lange et al., 2013). We find the risk of a data leak is important for databases that are used to promote a sustainable environment but not for a sustainable health system. Moreover. as individuals’ perceived moral obligation to donate data rises, their WDPD rises too. Furthermore, individuals are less willing to provide their data to profit-oriented organizations than to academia or the government. In contrast with the algorithm aversion literature (Önkal et al.. 2009). individuals are generally not sensitive to whether the data are processed by a human-supervised or selflearning smart assistant. These insights from our online experiment extend the research on the disclosure of personal data by inves tigating data disclosure as a voluntary donation to promote social welfare. Because data donations involve privacy costs without providing personal benefits, individuals have an incentive not to cooperate, which results in the social dilemma of big data. Our results provide first evidence for how individuals donate personal data in a scenario in which a database resembles a public good and must be sufficiently large and diverse to enable technology to promote social welfare. Our results are novel in that they show that individuals would donate their data despite personal privacy costs, uncertainty about whether enough other people are donating their data, and uncertainty about the amount of data required for the database to increase social welfare.

Understanding the drivers and barriers of socially directed data donation is relevant for the research community, but also to legislators and practitioners such as non-profit organization representatives. The COVID-19 pandemic and associated tracking apps illustrate the high potential of data in promoting public health as a domain of social welfare. However, the severity of the pandemic also underscores the failure of governments to adequately encourage public debate and educate the public on the prosocial use of citizen data before crises. The majority of governmental data collection measures were discussed and implemented in the middle of a global emergency, a time when people may be fearing for their health, the health of others, and the consequences for society. The timing of the discussion on data disclosure may raise ethical concerns because fear favors consent to voluntary and mandatory data disclosure to the state (Hillebrand, 2021). To ensure ethical use of citizen data, policy makers and legislators need to address popu lation preferences and understand what factors should be considered when using data to promote social welfare—if data disclosure is voluntary, to create conditions that motivate individual data donation; if data disclosure is mandatory, to create conditions that reflect society’s preferences to ensure ethical use (Ali and B´enabou, 2020). This connects well with emerging discussions on corporate digita responsibility (Lobschat et al., 2021) in that our insights provide guidance for decision makers on how to design data governance schemes that support individuals in their calculus on whether or not to donate data to a public good. According to our findings, legislators should particularly focus on the risk of a data leak, the organization that collects and manages the data, and the purpose for which the data will be used. With these insights, we hope to further support non-profit organizations such as the UN, which has been working for years to mobilize citizen data, in designing structures that encourage more individuals to voluntarily donate their data.

## Pre-registration

The experiment was preregistered at the AEA RCT Registry.

(https://www.socialscienceregistry.org/trials/6241).

## IRB approval

The study obtained ethical approval from the Ethics Commission of the University of Bremen.

## CRediT authorship contribution statement

Kirsten Hillebrand: Conceptualization, Methodology, Formal analysis, Investigation, Data curation, Writing – original draft, Visualization. Lars Hornuf: Conceptualization, Methodology, Resources, Writing – original draft, Supervision, Project administration, Funding acquisition. Benjamin Müller: Writing – review & editing. Daniel Vrankar: Formal analysis, Investigation, Data curation Writing – review & editing, Visualization.

## Data availability statement

The data that support the findings of this study are available from the corresponding author on request.

## Acknowledgments

The authors thank Sebastian Fehrler, John Friedman, Katrin Goedker, Sabrina Jeworrek, Mingfeng Lin, Ximena Garcia-Rada, Christoph Siemroth, Lauri Wessel, Dong Jun Wu, Stefan Zeisberger, and the participants of the MPI Research Seminar (Max Planck Institute for Innovation and Competition), the Shanghai Research Seminar (Shanghai University), ITM Distinguished Guest Speaker Series (Georgia Tech), the Field Day in Field Experiments (University of Bremen), the virtual workshop AI and Finance (Goethe University Frankfurt). the Research Seminar at the European New School of Digital Studies (Europa Universität Viadrina), and EURAM 2022 Annual Conference (ZHAW School of Management and Law), where the paper received the best paper award, for their helpfu comments and suggestions. An earlier version of the article was circulated as Max Planck Institute for Innovation & Competition Research Paper No. 21-08.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at https://doi.org/10.1016/j.infoandorg.2023.100452.

## References

Abdalla, S. M., Maani, N., Ettman, C. K., & Galea. S. (2020). Claiming health as a public good in the post-COVID-19 era. Development, 63. 200–204

Acord, S. K., & Harley, D. (2012). Credit, time, and personality: The human challenges to sharing scholarly work using web 2.0. New Media & Society, 15(3), 379–397

Acquisti, A., John, L. K., & Loewenstein, G. (2013). What is privacy worth? The Journal of Legal Studies, 42(2), 249–274.

Ali, N., & B´enabou, R. (2020). Image versus information: Changing societal norms and optimal privacy. American Economic Journal: Microeconomics, 12(3), 116–164.

Andreoni, J. (1990). Impure altruism and donations to public goods: A theory of warm-glow giving. The Economic Journal, 100(401), 464–477.

Antin, J., & Shaw, A. (2012). Social desirability bias and self-reports of motivation: A study of amazon mechanical turk in the US and India. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (Association for Computing Machinery, New York) (pp. 2925–2934).

Baird, A., & Maruping, L. M. (2021). The next generation of research on is use: A theoretical framework of delegation to and from agentic is artifacts. MIS Quarterly, 45 (1), 315–341.

Balliet, D., & Van Lange, P. A. (2013). Trust, conflict, and cooperation: A meta-analysis. Psychological Bulletin, 139(5), 1090–1112.

Balliet, D., Mulder, L. B., & Van Lange, P. A. (2011). Reward, punishment, and cooperation: A meta-analysis. Psychological Bulletin, 137(4), 594–615

Becker, M., Nevins, A., & Levine, J. (2012). Asymmetries in generalizing alternations to and from initial syllables. Language, 88, 231–268

Bednall, T. C., & Bove, L. L. (2011). Donating blood: A meta-analytic review of self-reported motivators and deterrents. Transfusion Medicine Reviews, 25(4), 317–334.

B´elanger, F., & Crossler, R. E. (2011). Privacy in the digital age: A review of information privacy research in information systems. MIS Quarterly, 35(4), 1017–1041.

Bendapudi, N., Singh, S. N., & Bendapudi, V. (1996). Enhancing helping behavior: An integrative framework for promotion planning. Journal of Marketing, 60(3), 33–49.

Benfeldt, O., Persson, J. S., & Madsen, S. (2020). Data governance as a collective action problem. Information Systems Frontiers, 22(2), 299–313.

Bentham, J. (1789). A utilitarian view. In T. Regan, & P. Singer (Eds.), Animal rights and human obligations (pp. 25–26) (Englewood Cliffs, NJ).

Bezuidenhout, L. (2013). Data sharing and dual-use issues. Science and Engineering Ethics, 19(1), 83–92.

Bhattacharjee, A., Dana, J., & Baron, J. (2017). Anti-profit beliefs: How people neglect the societal benefits of profit. Journal of Personality and Social Psychology, 113

Bonnefon, J. F., Shariff, A., & Rahwan, I. (2016). The social dilemma of autonomous vehicles. Science, 352(6293), 1573–1576.

Breeze, J. L., Poline, J. B., & Kennedy, D. N. (2012). Data sharing and publishing in the field of neuroimaging. GigaScience, 1(1), 2047–2170.

Budescu, D. V., Rapoport, A., & Suleiman, R. (1990). Resource dilemmas with environmental uncertainty and asymmetric players. European Journal of Social Psychology, 20(6), 475–487.

Cai, L., & Zhu, Y. (2015). The challenges of data quality and data quality assessment in the big data era. Data Science Journal, 14, 2.

Carballa Smichowski, B. (2019). Alternative data governance models: Moving bevond one-size-fits-all solutions. Intereconomics. 54(4). 222–227

Chawinga, W. D., & Zinn, S. (2019). Global perspectives of research data sharing: A systematic literature review. Library & Information Science Research, 41(2), 109–122.

Chen, R. (2013). Living a private life in public social networks: An exploration of member self-disclosure. Decision Support Systems, 55(3), 661–668

Chen, X. P., Pillutla, M. M., & Yao, X. (2009). Unintended consequences of cooperation inducing and maintaining mechanisms in public goods dilemmas: Sanctions and moral appeals. Group Processes & Intergroup Relations, 12(2), 241–255.

Choi, B. C. K., & Pak, A. W. (2005). A catalog of biases in questionnaires. Preventing Chronic Disease, 2(1), A13.

Choi, B., Wu, Y., Yu, J., & Land, L. (2018). Love at first sight: The interplay between privacy dispositions and privacy calculus in online social connectivity management. Journal of the Association for Information Systems. 19(3). 124–151.

Conrad. F. G., Couper, M. P., Tourangeau. R., & Galesic, M. (2005). Interactive feedback can improve the quality of responses in web surveys. In Paper presented at ESF Workshop on Internet Survey Methodology (Dubrovnik, 26–28 September 2005)

Cress, U., Kimmerle, J., & Hesse, F. W. (2006). Information exchange with shared databases as a social dilemma: The effect of metaknowledge, bonus systems, and

Crump, M. J. C., McDonnell, J. V., & Gureckis, T. M. (2013). Evaluating Amazon’s mechanical Turk as a tool for experimental behavioral research. PLoS One, 8(3), Article e57410.

Culnan, M. J., & Armstrong, P. K. (1999). Information privacy concerns, procedural fairness, and impersonal trust: An empirical investigation. Organization Science, 10 (1), 104–115.

Davis, D. W., & Silver, B. D. (2004). Civil liberties vs. security: Public opinion in the context of the terrorist attacks on America. American Journal of Political Science, 48 (1), 28–46.

Dawes, R. M. (1980). Social dilemmas. Annual Review of Psychology, 31(1), 169–193.

Dawes, R. M., McTavish, J., & Shaklee, H. (1976). Behavior, communication, and assumptions about other people’s behavior in a commons dilemma situation. Journal of Personality and Social Psychology, 35, 1–11.

De Visser, E. J., Pak, R., & Shaw, T. H. (2018). From ‘automation’ to ‘autonomy’: The importance of trust repair in human–machine interaction. Ergonomics, 61(10), 1409–1427.

Dickinson, D. L. (1998). The voluntary contributions mechanism with uncertain group payoffs. Journal of Economic Behavior & Organization, 35(4), 517–533.

Journal of Computer-Mediated Communication. 21(5). 368–383.

Dietvorst, B., Simmons, J. P., & Massey, C. (2015). Algorithm aversion: People erroneously avoid algorithms after seeing them err. Journal of Experimental Psychology: General, 144(1), 114–126.

Dietvorst, B. J., Simmons, J. P., & Massey, C. (2018). Overcoming algorithm aversion: People will use imperfect algorithms if they can (even slightly) modify them. Management Science. 64(3), 1155–1170.

Diney, T.. & Hart, H. (2006), An extended privacy calculus model for e-commerce transactions, Information Systems Research. 17(1). 61–80.

Dohmen, T., Falk, A., Huffman, D., Sunde, U., Schupp, J., & Wagner, G. G. (2011). Individual risk attitudes: Measurement, determinants, and behaviora consequences, Journal of the European Economic Association. 9(3). 522–550.

Douven, I. A. (2018). Bayesian perspective on Likert scales and central tendency. Psychonomic Bulletin & Review, 25(3), 1203–1211

requirements to realize a sustainable use of research data. Ecological Informatics, 11, 25–33.

Esmaeilzadeh. P., Sambasivan, M., Kumar, N., & Nezakati, H. (2015). Adoption of clinical decision support systems in a developing country: Antecedents and outcomes of physician's threat to perceived professional autonomy. International Journal of Medical Informatics. 84(8). 548-560.

Eurobarometer. (2014). Europäische Bürger: zunehmend optimistische Zukunftserwartungen, In . 17. Eurobarometer 81: Sorgen und Hoffnungen der Europäer, Context (pp. 16–17).

European Commission. (2022a). Data act – Factsheet. https://digital-strategy.ec.europa.eu/en/library/data-act-factsheet

European Commission. (2022b). Data Act: Commission proposes measures for a fair and innovative data economy. Retrieved July 20 from https://ec.europa.eu/ commission/presscorner/detail/en/ip\_22\_1113.

Eyster, E., Madarász, K., & Michaillat, P. (2021). Pricing under fairness concerns. Journal of the European Economic Association. 19(3), 1853–1898.

Fabbris, L. (2013). Measurement scales for scoring or ranking sets of interrelated items. In Survey Data Collection and Integration (pp. 21–43). Berlin, Heidelberg: Springer.

Fecher, B., Friesike, S., & Hebing, M. (2015). What drives academic data sharing? PLoS One. 10(2), Article e0118053

Fleishman, J. A. (1980). Collective action as helping behavior: Effects of responsibility diffusion on contributions to a public good. Journal of Personality and Social Psychology, 38(4), 629–637.

Gambs, S., Heen, O., & Potin, C. (2011). A comparative privacy analysis of geosocial networks. In Proceedings of the 4th ACM SIGSPATIAL International Workshop on Security and Privacy in GIS and LBS (Association for Computing Machinery, New York) (pp. 33–40).

Gangadharan, L., & Nemes, V. (2009). Experimental analysis of risk and uncertainty in provisioning private and public goods. Economic Inquiry, 47(1), 146–164

Garcia-Font, V. (2020). SocialBlock: An architecture for decentralized user-centric data management applications for communications in smart cities. Journal of Parallel and Distributed Computing, 145, 13–23.

German Federal Environment Agency. (2020). UBA carbon calculator. https://uba.co2-rechner.de/en\_GB/.

Gibson, E., Piantadosi, S., & Fedorenko, K. (2011). Using mechanical turk to obtain and analyze English acceptability judgments. Lang & Ling Compass, 5, 509–524.

Gjesme, T. (1979). Future time orientation as a function of achievement motives, ability, delay of gratification, and sex. Journal of Psychology, 101(2), 173–188

Goncalves, J., Ferreira, D., Hosio, S., Liu, Y., Rogstadius, J., Kukka, H., & Kostakos, V. (2013). Crowdsourcing on the spot: altruistic use of public displays, feasibility, performance, and behaviours. In Proceedings of the 2013 ACM International Joint Conference on Pervasive and Ubiquitous Computing (Association for Computing Machinery, New York) (pp. 753–762).

Gray, K., Young, L., & Waytz, A. (2012). Mind perception is the essence of morality. Psychological Inquiry, 23(2), 101–124.

Greene, J. D. (2014). Moral tribes: Emotion, reason, and the gap between us and them. London: Penguin Books.

Greene, J. D., Sommerville. R. B., Nystrom, L. E., Darley, J. M., & Cohen, J. D. (2001). An fMRI investigation of emotional engagement in moral judgment. Science. 293 (5537), 2105–2108.

Grossklags, J., & Acquisti, A. (2007). When 25 cents is too much: An experiment on willingness-to-sell and willingness-to-protect personal information. In Annua Workshop on the Economics of Information Security (WEIS).

Guay, R., & Birch, K. (2022). A comparative analysis of data governance: Socio-technical imaginaries of digital personal data in the USA and EU (2008–2016). Big Data & Society, 9(2). https://doi.org/10.1177/20539517221112925

Haidt, J. (2007). The new synthesis in moral psychology, Science. 316, 998–1002.

Hardin, G. (1968). The tragedy of the commons. Science, 162(3859), 1243–1248.

Harvard School of Public Health. (2016, July 11). The Workplace and Health. https://www.rwjf.org/en/library/research/2016/07/the-workplace-and-health.html.

Hauff, J. C., & Nilsson, J. (2023). Individual costs and societal benefits: The privacy calculus of contact-tracing apps. Journal of Consumer Marketing, 40(2), 171–180

Heeb. F., Kölbel, J. F., Paetzold, F., & Zeisberger, S. (2022). Do inyestors care about impact? Review of Financial Studies. https://doi,org/10.1093/rfs/hhac066 (forthcoming).

Hillebrand, K. (2021). The role of fear and trust when disclosing personal data to promote public health in a pandemic crisis. In Wirtschaftsinformatik 2021 Proceeding (p. 2).

Hinch, R., Probert, W., Nurtay, A., Kendall, M., Wymant, C., Hall, M., … Fraser, C. (2020). Effective configurations of a digital contact tracing app (NHSX report).

Huang, X., Hawkins, B. A., & Qiao, G. (2013). Biodiversity data sharing: Will peer-reviewed data papers work? BioScience, 63(1), 5–6.

Hussy, W., Schreier, M., & Echterhoff, G. (2010). Forschungsmethoden in Psychologie und Sozialwissenschaften. Berlin: Springer Verlag.

Idler, E. L., & Angel, R. J. (1990). Self-rated health and mortality in the NHANES-I epidemiologic follow-up study. American Journal of Public Health, 80(4), 446–452.

Inthorn, J., Tabacchi, M. E., & Seising, R. (2015). Having the final say: Machine support of ethical decisions of doctors. In S. P. V. Rysewyk, & M. Pontier (Eds.), Machine medical ethics (pp. 181–206). Berlin: Springer.

Janssen, M., Brous, P., Estevez, E., Barbosa, L. S., & Janowski, T. (2020). Data governance: Organizing data for trustworthy artificial intelligence. Government Information Ouarterly. 37(3). Article 101493.

Joinson, A. N., Reips, U. D., Buchanan, T., & Schofield, C. B. P. (2010). Privacy, trust, and self-disclosure online. Human Computer Interaction, 25(1), 1–24.

Kahane, G., Everett, J. A., Earp, B. D., Farias, M., & Savulescu, J. (2015). ‘Utilitarian’ judgments in sacrificial moral dilemmas do not reflect impartial concern for the greater good. Cognition, 134, 193–209.

Kahneman, D., & Tversky, A. (1979). An analysis of decision under risk. Econometrica, 47(2), 263–291.

Kao, L. S., & Green, C. E. (2008). Analysis of variance: Is there a difference in means and what does it mean? Journal of Surgical Research, 144(1), 158–170.

Keith, M. J., Babb. J. S., Furner. C. P.. & Abdullat. A. (2010). Privacy assurance and network effects in the adoption of location-based services: An iPhone experiment. In Proceedings of the 2010 International conference on information systems (ICIS) (Association for Information Systems, St. Louis) (p. 237).

Kerr, N. L. (1992). Efficacy as a causal and moderating variable in social dilemmas. In W. B. G. Liebrand, D. M. Messick, & H. A. M. Wilke (Eds.), International Series in Experimental Social Psychology. Social Dilemmas: Theoretical Issues and Research Findings (pp. 59–80). Oxford: Pergamon Press.

Kim, M. S., & Kim, S. (2018). Factors influencing willingness to provide personal information for personalized recommendations. Computers in Human Behavior, 88, 143-152.

Behavior, 92, 273–281.

Klein, D. (2009). How many trees are needed to bind one ton of CO2? Das Handelsblatt. http://www.handelsblatt.com.

Kolokotsa, D., Diakaki, C., Grigoroudis, E., Stavrakakis, G., & Kalaitzakis, K. (2009). Decision support methodologies on the energy efficiency and energy management in buildings. Advances in Building Energy Research. 3(1), 121–146.

Komorita, S. S., & Parks, C. D. (1994). Social Dilemmas. Boulder, CO: Westview Press.

Krebs, D. L. (2008). Morality: An evolutionary account. Perspectives on Psychological Science, 3(3), 149–172.

Lepri, B., Staiano, J., Sangokova, D., Letouzé, E., & Oliver, N. (2017). The tyranny of data? The bright and dark sides of data-driven decision-making for social good. In Transparent Data Mining for Big and Small Data (pp. 3–24). Cham: Springer.

Levati, M. V., & Morone, A. (2013). Voluntary contributions with risky and uncertain marginal returns: The importance of the parameter values. Journal of Publi Economic Theory, 15(5), 736–744.

Lim, S., Woo, J., Lee, J., & Huh, S. Y. (2018). Consumer valuation of personal information in the age of big data. Journal of the Association for Information Science and Technology, 69(1), 60–71.

Lin-Hi, N., Horisch, ¨ J., & Blumberg, I. (2015). Does CSR matter for nonprofit organizations? Testing the link between CSR performance and trustworthiness in the nonprofit versus for-profit domain. Voluntas: International Journal of Voluntary and Nonprofit Organizations. 26(5), 1944–1974.

Lis, D., & Otto, B. (2021). Towards a taxonomy of ecosystem data governance. In Proceedings of the 54th Hawaii International Conference on System Sciences (Hawaii) (pp. 6067–6076).

action-taking. Interacting with Computers, 29(2), 132–146.

Lobschat, L., Mueller, B., Eggers, F., Brandimarte, L., Diefenbach, S., Kroschke, M., & Wirtz, J. (2021). Corporate digital responsibility. Journal of Business Research, 122, 875–888.

Lopez, A. D. (2010). Sharing data for public health: Where is the vision? Bull World Health Organization, 88(6), 467.

MacKinnon, D. P., Fairchild, A. J., & Fritz, M. S. (2007). Mediation analysis. Annual Review of Psychology, 58, 593–614.

Madsen, M., & Gregor, S. (2000). Measuring human-computer trust. In , Vol. 53. In 11<sup>th</sup> Australasian conference on information systems (Brisbane, Australia) (pp. 6–8).

Marreiros, H., Tonin, M., Vlassopoulos, M., & Schraefel, M. C. (2017). “Now that you mention it”: A survey experiment on information, inattention and online privacy. Journal of Economic Behavior & Organization. 140. 1–17.

Maus, B., Olsson, C. M., & Salvi, D. (2021). Privacy personas for IoT-based health research: A privacy calculus approach. Frontiers in Digital Heglth, 3. Article 675754

Business Research. 129, 949–960.

Micheli, M., Ponti, M., Craglia, M., & Berti Suman, A. (2020). Emerging models of data governance in the age of datafication. Big Data & Society, 7(2), 2053951720948087.

Schnoebelen, T., & Kuperman, V. (2010). Using Amazon mechanical Turk for linguistic research. Psihologija, 43, 441–464. Sidgwick, H. (1907). The methods of ethics. London: Macmillan

influenza in the US: Measuring disease burden and costs. Vaccine, 25(27), 5086–5096

Morse, S. S. (2007). Global infectious disease surveillance and health intelligence. Health Affairs, 26(4), 1069–1077.

Mothersbaugh, D. L., Foxx, W. K., Beatty, S. E., & Wang, S. (2012). Disclosure antecedents in an online service context: The role of sensitivity of information. Journal o Service Research, 15(1), 76–98.

Mueller, B. (2022). Corporate digital responsibility. Business and Information Systems Engineering, 64(5), 689–700. https://doi.org/10.1007/s12599-022-00760-0

Murphy, R. O., Ackermann, K. A., & Handgraaf, M. (2011). Measuring social value orientation. Judgment and Decision making, 6(8), 771–781.

Musen, M. A., Middleton, B., & Greenes, R. A. (2014). Clinical decision-support systems. In E. Shortliffe, & J. Cimino (Eds.), Biomedical informatics (pp. 643–674). London: Springer.

Naous, D., Bonner, M., Humbert, M., & Legner, C. (2022). Learning from the past to improve the future. Business and Information Systems Engineering. https://doi.org/ 10.1007/s12599-022-00742-2

Newcomer, K. E., Hatry, H. P., & Wholey, J. S. (2015). Cost-effectiveness and cost-benefit analysis. In Handbook of practical program evaluation (p. 636). Hoboken, NJ: John Wiley & Sons.

Nieman, D. C., Henson, D. A., Austin, M. D., & Sha, W. (2011). Upper respiratory tract infection is reduced in physically fit and active adults. British Journal of Sports Medicine, 45(12), 987–992.

Nov, O., Arazy, O., & Anderson, D. (2014). Scientists @ home: What drives the quantity and quality of online citizen science participation. PLoS One, 9(4), Article e90375.

Olson, M. (1965). The logic of collective action. Public goods and the theory of groups. Cambridge, MA: Harvard University Press.

O'Neill, P. H. (2020). No, coronavirus apps don't need 60% adoption to be effective. MIT Technology Review. https://www.technologyreview.com/2020/06/05 1002775/covid-apps-effective-at-less-than-60-percent-download/.

Onkal, <sup>¨</sup> D., Goodwin, P., Thomson, M., Gonül, ¨ M., & Pollock, A. (2009). The relative influence of advice from human experts and statistical methods on forecast adjustments. Journal of Behavioral Decision Making. 22(4), 390–409.

Orbell, J. M., Van de Kragt, A. J., & Dawes, R. M. (1988). Explaining discussion-induced cooperation. Journal of Personality and Social Psychology, 54(5), 811–819. Otto, B. (2011). Data governance. Business & Information Systems Engineering, 3(4), 241–244.

Pavone, V., & Esposti, S. D. (2012). Public assessment of new surveillance-oriented security technologies: Beyond the trade-off between privacy and security. Public Understanding of Science. 21(5). 556–572.

Personal Information Protection Commission. (2013). Assessing the value of personal information and social cost due to the invasion of personal information.

Phelps, J., Nowak, G., & Ferrell, E. (2000). Privacy concerns and consumer willingness to provide personal information. Journal of Public Policy & Marketing, 19(1), 27–41.

Popkova, E. G., De Bernardi, P., Tyurina, Y. G., & Sergi, B. S. (2022). A theory of digital technology advancement to address the grand challenges of sustainable development. Technology in Society, 68, 1–14.

Pu, Y., & Grossklags, J. (2017). Valuating friends’ privacy: Does anonymity of sharing personal data matter?. In Thirteenth symposium on usable privacy and security (pp. 339–355). Santa Clara: USENIX Association.

Qiu, H., Noura, H., Qiu, M., Ming, Z., & Memmi, G. (2019). A user-centric data protection method for cloud storage based on invertible DWT. In Transactions on cloud computing (p. 1). Piscataway Township, NJ: Institute of Electrical and Electronics Engineers.

Rapoport, A. (1967). A note on the “index of cooperation” for prisoner’s dilemma. Journal of Conflict Resolution, 11(1), 100–103

Reddy, S., Allan, S., Coghlan, S., & Cooper, P. (2020). A governance model for the application of AI in health care. Journal of the American Medical Informatics Association, 27(3), 491–497.

Reuter, C., Geilen, G., & Gellert, R. (2016). Sicherheit vs. Privatsphare: ¨ Zur Akzeptanz von Überwachung in sozialen Medien im Kontext von Terrorkrisen. Informatik 2016.

Rivis, A., Sheeran, P., & Armitage, C. J. (2009). Expanding the affective and normative components of the theory of planned behavior: A meta-analysis of anticipated affect and moral norms. Journal of Applied Social Psychology, 39(12), 2985–3019.

Rotman, D., Preece, J., Hammock, J., Procita, K., Hansen, D., Parr, C., … Jacobs, D. (2012). Dynamic changes in motivation in collaborative citizen-science projects. In Proceedings of the ACM 2012 Conference on Computer Supported Cooperative Work (pp. 217–226). New York: Association for Computing Machinery.

Rudolph, R., & Davis, R. (2005). Administrative data and disease surveillance: An integration toolkit. In Public Health Data Dissemination Guidelines: NAHDO Working Technical Paper Series (p. 18).

Sanghera, B. (2016), Charitable giving and lay morality: Understanding sympathy, moral evaluations and social positions. The Sociological Review, 64(2), 294–311

Soni, H., Grando, A.. Murcko. A., Diaz, S.., Mukundan, M., Idouraine, N.. ... Whitfield. M. J. (2020). State of the art and a mixed-method personalized approach to assess patient perceptions on medical record sharing and sensitivity. Journal of Biomedical Informatics. 101, Article 103338.

Stahl, B. C. (2022). From computer ethics and the ethics of AI towards an ethics of digital ecosystems. AI and Ethics, 2, 65–77. https://doi.org/10.1007/s43681-021- 00080-1

Steinberg, L., Graham, S., O’brien, L., Woolard, J., Cauffman, E., & Banich, M. (2009). Age differences in future orientation and delay discounting. Child Development, 80(1), 28–44.

Stroebe. W., & Frey, B. S. (1982). Self-interest and collective action: The economics and psychology of public goods. British Journal of Social Psychology. 21(2).

Sun, Y., Wang, N., Shen, X. L., & Zhang, J. X. (2015). Location information disclosure in location-based social network services: Privacy calculus, benefit structure, and gender differences. Computers in Human Behavior, 52, 278–292.

The Economist. (2017, May 6). The world’s most valuable resource is no longer oil, but data. https://www.economist.com/leaders/2017/05/06/the-worlds-mostvaluable-resource-is-no-longer-oil-but-data

UN. (2014). A world that counts. Mobilising the data revolution for sustainable development. Retrieved from: https://www undatarevolution org/wp-content uploads/2014/11/A-World-That-Counts.pdf.

UN. (2015). Transforming our world: The 2030 agenda for sustainable development. https://www.un.org/ga/search/view\_doc.asp?symbol=A/RES/70/1&Lang=E. UN. (2020). Big data for sustainable development. https://www.un.org/en/sections/issues-depth/big-data-sustainable-development/.

Van Dijk, E., Wit, A., Wilke, H., & Budescu, D. V. (2004). What we know (and do not know) about the effects of uncertainty on behavior in social dilemmas. In R. Suleiman. D. V. Budescu. I. Fischer, & D. M. Messick (Eds.). Contemporary Psychological Research on Social Dilemmas (pp. 315–331). Cambridge: Cambridge

Van Lange, P. A., Joireman, J., Parks, C. D., & Van Dijk, E. (2013). The psychology of social dilemmas: A review. Organizational Behavior and Human Decision Processes, 120(2), 125–141.

Van Liere, K. D., & Dunlap, R. E. (1978). Moral norms and environmental behavior: An application of Schwartz’s norm-activation model to yard burning. Journal of Applied Social Psychology, 8(2), 174–188.

Van Zoonen, L. (2020). Data governance and citizen participation in the digital welfare state. Data & Policy, 2.

Varonis. (2019). 2019 global data risk report from the Varonis data lab. Retrieved from: https://info.varonis.com/hubfs/Varonis%202019%20Global%20Data% 20Risk%20Report.pdf.

Making, 15(4), 263–290.

Social Psychology Review. 8. 281–307.

Weinmann, M., Schneider, C., & Vom Brocke, J. (2016). Digital nudging. Business & Information Systems Engineering, 58(6), 433–436.

Wheatley, T., & Haidt, J. (2005). Hypnotic disgust makes moral judgments more severe. Psychological Science, 16(10), 780–784

Winter, J. S., & Davidson, E. (2019). Big data governance of personal health information and challenges to contextual integrity. The Information Society, 35(1), 36–51.

Wit, A., & Wilke, H. (1998). Public good provision under environmental and social uncertainty. European Journal of Social Psychology, 28(2), 249–256.

Wolfert, S., Ge, L., Verdouw, C., & Bogaardt, M. J. (2017). Big data in smart farming–a review. Agricultural Systems, 153, 69–80.

Woolfrey, L. (2009). Knowledge utilization for governance in Africa: Evidence-based decision-making and the role of survey data archives in the region. Information Development, 25(1), 22–32.

Wright, G., Prakash, P., Abraham, S., & Shah, N. (2010). Open government data study: India. London: The Centre for Internet and Society.

Xu, H., Teo, H. H., Tan, B. C., & Agarwal, R. (2009). The role of push-pull technology in privacy calculus: The case of location-based services. Journal of Management Information Systems, 26(3), 135–174.

Xu, H., Gupta, S., Rosson, M. B., & Carroll, J. M. (2012). Measuring mobile users’ concerns for information privacy. In Thirty third international conference on information systems. Orlando: Association for Information Systems.

Yamagishi, T. (2011). Trust: The evolutionary game of mind and society. Tokyo: Springer Science & Business Media.

Ye, N., Teng, L., Yu, Y., & Wang, Y. (2015). “What’s in it for me?”: The effect of donation outcomes on donation behavior. Journal of Business Research, 68(3), 480–486.

Zlatolas, L. N., Welzer, T., Heriˇcko, M., & Holbl, ¨ M. (2015). Privacy antecedents for SNS self-disclosure: The case of Facebook. Computers in Human Behavior, 45, 158–167.

Zygmuntowski, J. J., Zoboli, L., & Nemitz, P. (2021). Embedding European values in data governance: A case for public data commons. Internet Policy Review, 10(3), 1–29.
