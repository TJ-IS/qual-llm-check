---
otero_id: 20241
otero_key: "HE53TUMV"
title: "Privacy and the Internet of Things−An experiment in discrete choice"
authors: "David Goad; Andrew T. Collins; Uri Gal"
year: "2021"
journal: "Information & Management"
doi: "10.1016/j.im.2020.103292"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Privacy and the Internet of Things−An experiment in discrete choice

David Goad\*, Andrew T. Collins, Uri Gal

The University of Sydney Business School, The University of Sydney, NSW 2006, Australia

## A R T I C L E I N F O

Keywords: Internet of Things IoT Privacy Discrete choice methods

## A B S T R A C T

The Internet of Things (IoT) is the concept that everyday devices are connected to the Internet generating data about us and the world around us. With the number of devices connected directly to the Internet expected to be three times the number of people by 2020, the potential for a reduction in personal privacy is evident. Thi research fills a gap in the literature by conducting a quantitative analysis of people’s privacy preferences as it relates to the IoT. Our findings provide potential guidance to practitioners in their IoT architectural design and increase our understanding of privacy preference overall.

## 1. Introduction and background

The Internet of Things (IoT) can be defined as everyday devices connected to the Internet providing highly useful integrated data about us and the world around us. It is expected that 20 Billion “Things” will be connected to the Internet by 2020 [1], which could exceed the number of people connected to the Internet by three to five times. These Things include but are not limited to wearable devices, newly purchased automobiles and smart home devices, such as smart speakers and smart TVs.

There have been many conceptualizations and definitions of the concept of Privacy in the literature. These include but are not limited to the right to be left alone, the ability to limit access to the self, secrecy and the concealment of matters from others, control over one’s persona information, the protection of one’s individuality and the ability to limit access to the intimate aspects of one’s life [2]. For the purposes of this research, we define Privacy as “the claim of individuals, groups, or institutions to determine for themselves when, how, and to what extent information about them is communicated to others” [3].

Since its inception, the Internet has generated concerns about privacy as users trade information about themselves for access to the services that the Internet can provide. Yet these same users often do not know how that information will be used or where it will end up. In a recent survey, 74 % of the respondents indicated that it was “very important” for them to be in control of who can get information about them [4]. Other cross-national surveys have demonstrated that most people (from 74 % to 90 % depending on the country) believe that laws that prohibit the buying and selling of information about them by businesses should be put into place [5].

The IoT promises to increase these previously held information privacy concerns with the Internet, in that the average number of Internet-enabled devices or “Things” in the home is projected to grow from 10 to 50 by 2020, bringing the level of available personal data to an all-time high [6]. Wearable devices that track our activities and vital health statistics are expected to be a \$61.7 Billion market by 2020 [7]. Many organizations generate significant revenue from the personal data that they collect about the people that use their products and services, which in turn encourages the collection of even more data [8]. A recent survey demonstrated that geospatial data collected from people’s movement, which is often derived from IoT devices, was the third lar gest category of Big Data being collected [9].

Against this backdrop, organizations deploying IoT solutions are facing increasing expectations from governments in terms of IoT privacy. For example, the Australian government recently enacted privacy legislation, which included a comprehensive duty to report any data breaches including the cause of the breach, and what has happened to that data [10]. Similarly the General Data Protection Regulation legislation enforced in the EU in 2018 has had and will have significant impacts, as it establishes whole new sets of expectations on organizations that collect personal data [11]. Meeting these expectations comes at increasing costs. Rising privacy regulations are expected to increase the amount businesses spend on privacy by 20 % from 2016 to 2019 [12]. Global privacy legislation is already estimated to cost multinational organizations an average of \$3.5 million per year per organization [13]. The impact on small and medium businesses will be disproportionate with an expected rise from 16 % to 40 % in those organizations’ IT budgets due to increased privacy legislation [14].

Organizations will face technical challenges in addressing these increasing privacy concerns. Security and privacy in IoT are known challenges due to the limited resources of the many diferent “Things”

in the IoT [15]. The “Things” in the IoT are commonly designed with limited memory, computational power and storage, to reduce cost, and achieve ubiquity of use. This means that standard security and privacy tools and protocols are often not natively present in these devices, which increases their vulnerability. By some estimates, by $2 0 2 0 > 5 0$ % of IoT implementations are likely to expose sensitive information due to inadequate controls [16].

Given the increasing costs and technical dificulties involved in complying with this new privacy regulation, which in general does not take into account the challenges of the IoT, a critical question to ask is “Which types of privacy and privacy-protection mechanisms are more important than others to users in the domain of the IoT?” To efectively debate this question one must first appropriately assess the value placed on privacy in an IoT context. This is of particular importance in light of the well-known Privacy Paradox, wherein individuals’ revealed privacy preferences are often much lower than their stated privacy preferences [4,5]. Research has also shown that increased privacy often does not create benefit for the person retaining the private information or society in general [17]. Consequently, the costs required to achieve these increases in privacy driven by these most recent legislations may not necessarily outweigh the actual value people associate with that increased privacy in the first place.

To address this question, we have adopted Discrete Choice Experiment (DCE) techniques to analyze and quantify individuals’ IoT privacy preferences and the valuation of privacy in an IoT context. We have done so by constructing a realistic IoT scenario, the purchase of an Internet connected everyday common fitness tracker. We asked survey participants to choose which of two presented fitness trackers they would purchase, wherein each tracker has a diferent set of attributes that afects privacy diferently and a diferent purchase price. By having to trade-of between the purchase price and the tracker features, with their associated privacy implications, a monetary valuation for privacy can be assigned. In this way we quantified, in monetary terms, peoples Willingness To Accept (WTA) clear infringements on their privacy. In a similar fashion but using diferent attributes, we also quantified their Willingness to Pay (WTP) for beneficial tracker features that inherently improve privacy. Further, we analyzed the impact of a number of respondent characteristics and types of private information on WTA and WTP. In some cases our research confirms previous findings in the literature regarding privacy preference and valuation in the context of the Internet and IoT, and in other cases it suggests that there are diferences in privacy preference and privacy valuation specific to the IoT.

We acknowledge that there is already a growing body of literature on the quantitative analysis of privacy preference in the context of the IoT [18–21]. By using DCE techniques to conduct our analysis, we add to this literature by using methods, which are consistent with theorie of consumer behavior. Privacy preference is expressed through a choice between alternative products as opposed to a stated preference for privacy, which may be an inaccurate representation of privacy preference [20,22–24]. The DCE method allows for the quantification of preference and monetary values of privacy preference within various contexts of the IoT. Compared to the rankings or rating responses of Conjoint Analysis (CA) [57], the choice response better matches market decisions (i.e., purchasing an IoT device), and results in less respondent burden. While novel to the use of privacy preference analysis in the IoT, these techniques are well established in the academic literature [25,26], and provide the ability to assess a commercial value to privacy preference and to observe how that commercial value is influenced by various factors and attributes. In this way, not only do we add to the growing academic literature around privacy in the IoT, but we also help facilitate a discussion around the importance that users place on dif ferent types of privacy and privacy-protection mechanisms in the domain of the IoT. Thus, we provide guidance to practitioners on what types of information should require stronger privacy controls based on their perceived value and in what context these controls should be in creased with a view to optimizing IoT security and privacy investments.

In addition to these contributions, we also suggest avenues for further research into IoT privacy preference.

## 2. Unpacking the concept of privacy

Privacy is a complex concept, but one that is relatively well developed in the literature. To build an efective scafold upon which to base our subsequent experimental design and analysis, we first review the existing literature on privacy in the IoT. Then, we define the concept of privacy that we use for our analysis. We then discuss the relationship between a person’s observed behavior and the influences that afect this behavior in the context of privacy, the IoT, and our proposed DCE. To do this, we draw on sources both from the privacy literature [27,28] and the DCE literature [25,29]. We then explore several theoretical models of privacy preference with a view to informing our research design. As our focus is to quantify people’s WTA a loss of privacy from a monetary perspective, we review previous quantitative studies on privacy valuation that have used other statistical techniques to provide a starting point for our analysis. After this, we go on to define our experimental design, our process for data collection and analysis, and then present our results.

## 2.1. Exploring privacy and the internet of things in the literature

Given the rapid increase in the amount of available data due to the IoT, it is not surprising that there is a rapidly developing body of literature related to understanding the impact of IoT on privacy preference. The current literature has developed along three broad themes: 1) understanding the impact of IoT on privacy concern and stated privacy preference; 2) understanding the antecedents, contributory factors, and privacy calculus that contribute to the creation of IoT privacy preference, and; 3) research into the development of tools and tactics (both technical and regulatory) to address the concern for privacy within the IoT.

First, regarding the impact IoT has on privacy preference, several authors have used IoT-based scenarios [20,30] or vignettes [19], to survey respondents on their stated privacy preference within a variety of IoT contexts. This research has concluded that respondents’ stated privacy preferences are diverse, context–dependent, and highly personal, but that there is a high degree of consistency when an individual respondent is presented with diferent contexts but which have similar attributes and are asked to state their privacy preference [19,20]. This line of research has also identified the need for technology that can provide an awareness of data collection, as awareness is considered an important factor in IoT privacy preference formation [19]. We will come back to this concept later when we discuss our research design and our inclusion of a feature in the fitness tracker that provides users with the ability to track the usage of data collected by the tracker. Consistent with these survey results, models have been developed which demonstrate that “tolerance or requirements with respect to privacy/security issues may not necessarily be the same across individuals and their associated IoT devices across diferent points in time” and that there is benefit to social welfare of privacy diferentiation in the IoT [31]. This potentially supports a view that “more privacy is not always better” and that there is an appropriate level of privacy based on the value attached to privacy by the individual in a specific context. We will explore this point more fully later in the paper when we develop our research design. This issue of the impact of IoT on privacy concern and privacy preference has also been investigated in a number of specific IoT contexts. For example there is an increasing body of literature on privacy preference specific to the “smart home” segment of the IoT [32–34]. Similarly, there has also been research into IoT privacy preference in the Health Care space [35]. All evaluate the influence of various IoT scenarios on privacy preference.

Second, regarding the antecedents, contributory factors, and calculus that contributes to IoT privacy preference, a number of articles have examined the antecedents and factors that contribute to stated privacy preference to unpack the privacy calculus that people undertake within the IoT [18,21,36]. For example, believing that a high degree of the benefit from an IoT device is derived from the direct and indirect network externalities [37] that it provides and the majority of the risk associated with the IoT derives from the Concern for Information Privacy (CFIP) [27] that it creates, one group of researchers [18] use structural equation modeling and a combination of online surveys and interviews to build a model, which can predict intention to use an IoT device. Notably, in their investigations, the CFIP had less efect than the network externalities on the intention to use the device and most of CFIP-derived information was from improper access and unauthorized secondary use and not the actual collection of the data itself. Building on previous research [18], there have been attempts [21] to build a more refined risk versus benefits model, which includes information sensitivity, trust, the number of IoT services, perception of critical mass, perception of compatibility, and perception of complementarity as the independent variables and willingness to provide the private information as dependent variables. This study’s conclusions confirm previous research that privacy risk factors, such as information sensitivity and trust, do not have a statistically significant impact on an individual’s intention to use an IoT device. Finally, other research has demonstrated that influencers such as friends and privacy experts [36] can have a significant impact on the intention to use an IoT device, and that any perceived benefit from reduced privacy seems to have a positive efect on the willingness to provide private information [21].

Third, acknowledging the increased concern for privacy with the IoT, there have been several studies on how privacy related to the IoT might actually be achieved. Some authors [38] have broken down the typical IoT architecture used in industry into an application layer, transport layer, network layer, and perception layer. They analyzed the architectural and technology privacy issues related to each layer and identified a number of opportunities for increased privacy through an improved technical architecture. Other authors [39] have looked at architectural issues for specific types of IoT devices (e.g., fitness trackers) to improve privacy. Still other authors [40] have looked at the issue of user interface (UI) design to improve privacy. By using machine learning to group the potentially large number of IoT privacy choice settings, they aimed to create a more user friendly UI for improved device adoption and a closer fit to a user’s privacy preference. Finally, other authors have considered the role that legislation will play in achieving privacy preference. For example, recent research which considers current privacy regulation in Australia has concluded that it does not efectively cover many IoT scenarios and made several sug gestions for revision [41].

Summarizing the current state of the literature, it is possible to conclude that the role that privacy has in one’s decision to use an IoT device is inconclusive and requires further study. Furthermore, privacy preferences related to the IoT are very personal, highly variable, and context specific, and there is a high potential for design solutions that can provide a personalized privacy solution for IoT use. Thus, there is an opportunity to further understand privacy preference in the IoT and to assign a valuation to that preference with a view to influence future investments into IoT privacy (both regulatory and technical).

## 2.2. The relationship between influences and behaviors in a consumer choice process that involves privacy and the IoT

There is a complex interplay between influences and behaviors in an IoT-based consumer privacy choice process. We illustrate these processes in Fig. 1 and discuss these processes through the lens of Privacy Concern and Discrete Choice in the following sections.

## 2.2.1. Privacy concern as it relates to the consumer choice process

Privacy Concern derives from one’s desire for Privacy and is defined as a person’s concerns associated with loss of privacy or loss of control over their personal information [42]. Measures of Privacy Concern in the literature have varied, e.g., “Willingness to provide privacy information” [21] and “Continued intention to ${ \mathrm { u } } s { \mathrm { e } } ^ { \mathfrak { n } }$ [18], and whether they would allow data collection [19]. They are commonly Likert scale responses integrated into structural equation models, and sometimes a mix of machine learning and statistical techniques. These may be expressed in the context of an individual’s exposure to IoT devices at the time of the study [18], a single IoT device scenario [21], or combina tions of privacy related information that is systematically varied by the researcher [19]. In analyzing Privacy Concern, it is important to note that there are a number of Influences that can impact on the level of concern, and therefore the degree to which a person wants to control their personal information. This will influence their choice of IoT device. These Influences can include but are not limited to product features, personal dispositions, covariates (such as age, sex, etc.) and contextual variables [28].

In undertaking product choices in relation to Privacy Concern, individuals undertake complex internal calculations around the potential benefit and risks associated with disclosing private personal information. This process is called the Privacy Calculus [42]. This Privacy Cal culus then leads to a demonstrated Privacy Preference. We provide a detailed discussion of the various proposed theoretical models for how this Privacy Calculus is undertaken by an individual in a subsequent section.

As preference is a process, which involves the choice between alternatives [43], we define Privacy Preference as the choice between al ternatives as they relate to decisions about controlling information about oneself. Privacy Valuation is the monetary value, which an individual assigns to a Privacy Preference and is essentially one form of quantification of that preference. The assignment of a monetary value to both privacy preference and product features results is an observed choice between alternatives when a consumer is asked to make a purchase decision. By including the purchase price as one of the features of the product and observing the choice between features, we can assign an inferred value to both privacy preference and product features. The purchase and subsequent use of an IoT device is a useful and consequential measure of the extent to which privacy is traded of with other benefits and risks. If the various benefits outweigh the risk, in cluding privacy impacts and the cost of the device, then an IoT device will be purchased and used.

## 2.2.2. Discrete choice theory as it relates to the consumer choice process

We can draw upon the consumer behavior literature, which recognizes that goods are purchased because of the utility provided by their characteristics and features [44,45]. Conceptual models devel oped in this stream of scholarly work have been adopted by the discrete choice literature [46].

The literature [25] has detailed how the various conceptual models of choice can be operationalized with discrete choice models. These choice models link product features to choice through the estimation of latent (dis)utility values that capture the preferences of decision makers for or against those features.

We extend the privacy calculus discussed in other studies and consider the calculus in a broader purchase/use calculus that includes privacy dimensions as well as other product features such as cost. Of particular interest is the trade-of between privacy features and product cost, as this allows WTP measures to be derived for privacy in a way that does not rely on directly stated WTP measures.

## 2.2.3. A summary of the consumer choice process that involves privacy and the IoT

This proposed model for consumer choice in an IoT/privacy context extends on models from the existing general privacy literature for measuring privacy preference [27,28] and models from the IoT privacy literature for measuring IoT privacy attitudes [18,21] by using consumer choice concepts from the existing DCE literature [25]. In thi way, we measure privacy preference through an observed choice as opposed to a stated preference, which avoids many of the well-docu mented challenges in the literature [20,22–24] with using stated privacy preference. In so doing, we are able to observe both a utility and a monetary valuation associated to privacy as a function of various covariates, contextual variables, product features, and privacy preferences.

![](/api/attachments/HE53TUMV/fulltext/images/0dde69a8ff6123199af908ff1fd4325c2ec6a01fa490ce8b230a92ede095aab9.jpg)  
Fig. 1. The Relationship between Influences and Behaviors in a Consumer Choice Process that involves Privacy and the IoT.

## 2.3. Privacy theoretical underpinnings and their implications for IoT privacy research design

## 2.3.1. Privacy Calculus models and their impact on privacy research design

A variety of Privacy Calculus models have been introduced in the literature to explain privacy preference in traditional IT or Internet information scenarios. One author [42] identified 15 distinct privacyrelated theories in the literature. We select for our review and in corporation into our study theoretical models that focus on the individual factors that influence privacy preference and therefore privacy valuation. We do this for two reasons. First, the implementation of privacy regulation discussed above is mostly framed around concerns for individual privacy. Therefore, it is important to understand how individuals consider privacy. Second, the impact of the loss of privacy in an IoT environment mostly afects individuals rather than organizations or institutions. Based on these selection criteria and considerations, we specifically consider Protection Motivation Theory, Information Boundary Theory, Social Cognitive Theory and Personality Theory in our literature review as they address the individual factors that may afect IoT privacy preference and therefore privacy valuation. We subsequently incorporate the learnings from these theories into our research design.

Protection Motivation Theory considers an individual’s intent to protect against threats [47]. This theory asserts that individuals conduct a threat appraisal and a coping appraisal assessing the degree of threat and their ability to address that threat when evaluating what actions they intend to take. Thus, an individual will consider the context in which the information he or she discloses will be used, and the potential threats that arise from this disclosure. This theory indicates that the type of private information disclosed would have an impact on the individual’s perceived threat. We factor this into our research design by analyzing a number of diferent types of private information across a number of diferent contexts as these may impact the privacy preference and therefore privacy valuation.

Information Boundary Theory states that individuals set boundarie around themselves. which determine what information can be shared to other individuals or organizations [48]. Individuals and organizations that attempt to penetrate those boundaries are perceived as a threat. The theory posits that boundaries are regulated by issues such as the cost-benefit of releasing personal information and the context as to why it is being released. Therefore, this theory supports the idea that personal benefit is a key input into any individual’s privacy calculus, which then impacts privacy preference and therefore privacy valuation. These considerations will be factored into our research design as well by using realistic scenarios that generate personal benefit from disclosing private information as well as scenarios, which attempt to generate no personal benefit such that we can assess to what degree personal benefit impacts privacy valuation.

In our research design, we also draw on Social Cognitive Theory as it relates specifically to privacy [49]. This theory posits that an individual's knowledge acquisition is related to their observations of others, direct experiences as well as outside media influence. This theory also identifies previous experiences with privacy breach and previous news media exposure around privacy breach as influential in an individual’s calculus around the disclosure of private information. We include these factors into our research design by asking our respondents about their previous experiences with privacy breach and news media exposure, to see what efect these influencers have on their privacy concern and therefore privacy preference and valuation.

Finally, we also draw on the Personality Theory [50]. This theory posits that an individual’s personal attributes - such as agreeableness, conscientiousness, neuroticism, and intellect - will contribute to their natural disposition toward privacy. We mention this theory because it highlights the need to have a methodology for analyzing privacy preference, which addresses unmeasured heterogeneity in the sample population and can account for unforeseen influences. As we will be discussing later, one of the reasons why we chose DCE techniques was specifically because of their ability to handle this type of heterogeneity.

## 2.3.2. The privacy paradox and its impact on privacy research design

Having discussed Privacy Preference models and their impact on privacy valuation, we now consider another significant theme in the literature called the Privacy Paradox. The Privacy Paradox is defined a the discrepancy between people’s stated and revealed privacy preferences [51]. When asked to state their privacy preference, individuals would indicate a higher preference for privacy than they would reveal in their everyday actions. Initial studies on the topic hypothesized that this diference exists because of diferences in the perception of Risk and

Trust at the time the question is asked versus the time the action needs to be taken. Some [52] argue that the Privacy Paradox is a result of bounded rationality (limited information) in the individuals decisionmaking process. Accordingly, because of the Privacy Paradox, other researchers [53] have stated that “experiments should be conducted in realistic settings that provide a rich and relevant context” and “survey research should take into account the fact that self-reports on privacy behavior are unreliable.”

We conclude from this research that it is preferable to design privacy preference studies that use realistic scenarios that require participants to make a choice between the benefits and potential losses associated with disclosing private information, and weigh the tradeof of privacy decisions. As we will discuss in the research design section, the novel use of a DCE and a realistic IoT-based scenario (the purchase of a fitness tracker) to evaluate privacy preference, efectively addresses the identified concerns related to the Privacy Paradox and privacy studies regarding an individual’s privacy calculus. It does so by forcing the participant to choose between two proposed and realistic scenarios forcing them to balance the risks versus benefits and make a choice. This represents a significant contribution to the existing literature on IoT Privacy Valuation.

## 2.3.3. The variable nature of privacy valuation and its impact on privacy research design

Another important issue to take into consideration regarding our research design is whether more privacy will always be perceived positively to a survey respondent. While there is general consensus that legislation to improve privacy standards should be put into place [5], there are instances where increased privacy benefits neither the individual nor society and that there is a benefit to the social welfare of privacy diferentiation in the IoT [31]. As previously noted, increased privacy results in increased costs [12]. These costs have to be weighed against benefits to the individual and society in securing personal in formation.

From the perspective of the individual, providing access to their personal information can allow for targeted and relevant marketing, thereby increasing their access to relevant information and saving them time and money [54]. Disclosing private information may also provide more convenience in daily transactional activities and increase individual health by allowing healthcare providers to use private information to make accurate and proactive diagnoses [55].

From a societal perspective, there are several reasons why increased privacy is not necessarily preferable. The first involves security. With global terrorism, the ability for security agencies to skim the public’s personal data and proactively identify potential threats is becoming of increasing importance. Second, there are economic reasons couched in information asymmetries due to increased privacy, which may lead to an ineficient redistribution of wealth [56]. For example, health in surance companies that are not aware of preexisting medical condi tions, might provide a lower rate to one individual but increased rates overall to cover the distributed risk. Another example is vendors that sell an individual something on credit not realizing that the person is in imminent risk of bankruptcy and therefore losing their money. Other authors have argued that the free flow of individual credit data allows the eficient allocation of credit among borrowers [57].

In sum, the privacy calculus that an individual will undertake to determine a privacy preference will be highly contextual [20,30] as their privacy concerns are influenced by increased perceived benefits (both societal and personal) of providing personal information in specific contexts [58]. This was recognized in earlier models of privacy concern, such as Internet users' information privacy concerns, IUIPC [28]. We extend on this analysis by not only taking into account the type of private information in our research design, but by also considering the context of the IoT use cases in a combination of scenarios constructed so that in some cases more personal benefit is generated from the disclosure of private information provided.

2.3.4. Previous attempts at privacy valuation and their impact on future privacy research design

As we aim to understand various influences that lead to a diferent Privacy Valuation, it is important to consider previous studies that have attempted to assign a monetary value to privacy. If a value is to be placed on privacy, some unit of measure is required to quantify that value. In general terms, we wish to derive a marginal rate of substitution (MRS), which will indicate the extent to which some intrusion on privacy can be compensated by some other outcome. The most com monly used form of MRS in the privacy literature is WTP, which is the amount of money that an individual would pay to acquire a certain privacy state. Some authors [59] have suggested that monetary valuations of privacy are of interest because they inform businesses about whether to invest in privacy features, inform the legal profession about the extent to which individuals value privacy, and help policy makers make decisions about the trade-of between privacy and other goals. Furthermore, monetary valuations provide a standardized measure of privacy that can be compared between studies, in a way that other privacy measures cannot.

Any quantitative analysis of IoT privacy preference requires a methodology to elicit and measure those preferences. The diversity of measurements that have been used by researchers poses a challenge to the interpretation of results across various studies [51]. One approach has been to elicit privacy-related attitudes and beliefs. For example, it has been shown that attitudes, values, and beliefs around privacy vary by the type of organization a person works for [60]. A limitation of this approach is that attitudes may not translate to actions. Another stream of privacy research focuses on privacy-related behaviors. For example, one group of researchers [51] investigated if survey participants would disclose personal information in the context of a credit check by a bank. They captured two types of disclosure choice: stated preferences and actual choices. By comparing counts of the number of pieces of information revealed, they concluded that peoples’ actual preference was to provide more personal information than their stated preference. While this study usefully demonstrates the privacy paradox, the methodology used is not informative about how people value the privacy of specific types of information, or about the intensity with which they value keeping this information private. This highlights the benefits of using monetary valuations of privacy based on transactions.

Often, individuals do not make choices about specific pieces of information in isolation, but instead choose products or oferings that contain a mix of features, some of which may be privacy related. Some authors [59] have noted that decisions about privacy are mostly made as part of larger economic transactions. In their study, privacy preference is inferred through the choice of gift cards, which difer in the value of the card, and the requirement to provide a name to redeem the card. The choice is made about which gift card to accept – the cheaper card that may be perceived to compromise privacy, or the more expensive card that can be used anonymously. From the choices of individuals who are performing a privacy calculus, the analyst can infer the extent to which they value privacy. In this case, this study shows that the monetary value attached to privacy depends on the context of the transaction.

Previous research [58] has utilized an experimental approach called CA to calculate people’s WTP for certain privacy features in relation to websites. In the study, subjects were presented with a set of alternatives, each described by attributes, where each attribute can assume a certain level, which generates a certain amount of (dis)utility. The website alternatives were categorized by three privacy related attributes: secondary use of data, improper access to data, and the ability to review personal information for mistakes. Two further attributes represented compensating positive features: a monetary reward and time savings. Test subjects were asked to rank 18 alternatives, with these rankings being used as the dependent variable in an ANOVA analysis to estimate the utility coeficients. Participants assigned a Privacy Valuation of between \$7.98 USD and \$16.58 USD to improve each of the three privacy attributes. This study demonstrated a more complex privacy calculus than previous research [59], with multiple privacy and benefit dimensions typical of a real world privacy choice context. While CA is similar to the DCE methods employed in this research, there are certain advantages of DCE over CA, which we will explore in the Methodology section of this paper.

![](/api/attachments/HE53TUMV/fulltext/images/0d4b42457a9b2e8c5d9c40811304305b1373574c0fd0c0748557a72da6cccfa9.jpg)  
Fig. 2. The Relationship between Influences and Behaviors in an IoT-based Consumer Privacy Choice Process including our Hypothesis about those Influences and Behaviors.

Some authors [59] have highlighted the importance of distin guishing between WTP and WTA. The WTP/WTA distinction requires the presence of a status quo. In the context of privacy, the status quo may be if privacy has already been compromised, WTP is the amount of money that an individual is prepared to pay to reduce an existing privacy violation, and WTA is the amount of monetary compensation that an individual requires to allow some intrusion on their privacy. These researchers [59] endowed study participants with one of the two gift card types and found that WTP to improve privacy from a more compromised privacy state was less than the amount of money subjects were prepared to accept to allow privacy to deteriorate from a more private state. Therefore, it is important to be cognizant of the WTP/ WTA distinction in our analysis.

## 3. Proposed contributions to the existing literature

In summarizing the preceding literature review, we identify several potential contributions to existing research on IoT privacy that our study will make, a number of which is derived from the use of DCE techniques. These are:

1) The use of analysis techniques (DCE) that are grounded in theory and have sound econometric properties;

2) The ability to assign a monetary valuation (WTP/WTA) to IoT privacy preference; and

3) The establishment of privacy preference through consequential choices of products as opposed to relying on declared preference, which is more rigorous and addresses issues related to the Privacy Paradox.

In addition to these contributions we also:

4) Explore further the contexts under which perceived benefits may influence privacy preference in the IoT;

5) Explore further the degree to which information type afects privacy preference in the IoT; and

6) Explore further the degree to which personal characteristics or covariates afect IoT Privacy Preference.

## 4. Research design

Our previous discussion indicated that the need for privacy is challenged within an IoT environment. This is because of the increased amount of data that connected devices generate, and the fact that these devices do not inherently provide the same security and privacy as traditional IT or the Internet has. To study this, we designed a realistic DCE, utilizing the scenario of the purchase of a fitness tracker, to test people’s willingness to use IoT services and products even when their privacy was knowingly compromised by the providers of those services and products. The structure of the experiment ofers a way to quantify people’s willingness to disclose various types of private information. The DCE further allows us to examine what contributes to Privacy Concern and therefore Privacy Valuation, specifically related to concern over privacy of the body, personal behavior, and personal data.

In designing our experiment, we developed a series of Privacy Preference hypothesis for the IoT, which are based on our consideration of the literature and the perceived diferences between traditional Internet and the new IoT. We posit how these diferences may impact Privacy Preference and therefore Privacy Valuation, and we categorize our hypothesis into a number of specific areas of investigation, speci fically:

1 The Valuation of Privacy in an IoT context,

2 The impact of specific contexts and how private data is used on Privacy Preference and Privacy Valuation in IoT,

3 The types of private information and how this impacts Privacy Preference and Privacy Valuation in IoT, and finally

4 Who is providing the Private Data and how this afects their Privacy Preference and Privacy Valuation in the IoT?

These categories of investigation are illustrated in our conceptual model of privacy concern and privacy valuation in an IoT-based Consumer Privacy Choice Process shown in Fig. 2. They represent influences on the Privacy Concerns described in the previously presented model in Fig. 1, which would impact the Privacy Calculus and therefore Privacy Preference, and result in specific Privacy Valuations for the dif ferent types of information given the specific contexts presented. These Privacy Valuations are demonstrated through the choice of IoT device that the survey respondent makes. We construct a number of hypotheses related to these influences, which we present in subsequent sections:

## 4.1. The value of privacy in an IoT context

The first hypothesis we put forth involves an assessment of the monetary value people assign to privacy in an IoT environment. This is the amount of money they were willing to accept for providing basic private information. Recent privacy studies have demonstrated valuations for private information as low as \$2 [59] and \$7 [61]. Recent studies on IoT privacy preference have struggled to demonstrate a statistically significant efect of privacy on the purchase decision for an IoT product [18]. This leads to the following hypotheses:

Hypothesis 1. That the monetary valuation people place on privacy in the IoT will not be statistically diferent to zero.

4.2. The impact of specific contexts and how private data is used on privacy preference and privacy valuation in the IoT

A number of studies have established that privacy is contextual [51,53,62]. When asked to reveal a specific set of information, people’s response will depend on the context in which the question is asked, who is receiving the information, and the person's understanding of how data will be used and for what purpose. When people are uncertain about their preferences, they often search for cues in their environment to provide guidance and inform their behavior. Previous research has also shown that the reasoning as to why IoT data are being solicited will impact IoT privacy preference [61]. If providing data generate benefit for the individual, they will value their privacy less than if it is being used by other parties or society as a whole. We therefore posit that context and how data will be used will impact privacy preference and valuation in the IoT.

Hypothesis 2. The monetary value people place on privacy in an IoT context depends on their determination of the personal benefit they will gain from disclosing private information. Increased personal benefit will reduce the preference for more privacy preference, and thus its monetary valuation in the IoT.

In addition, consistent with previous literature on IoT privacy preference, which “underlines the need for technology to support the awareness of data collection” [19], we posit that awareness of the use of private information will have a significant impact on privacy preference and the monetary value one assigns to privacy:

Hypothesis 3. The ability to monitor how one’s private information is being used will reduce privacy preference and decrease the monetary value one assigns to their privacy within an IoT context.

4.3. Information type and how this impacts privacy preference and privacy valuation in the IoT

It has been demonstrated that diferent types of information have diferent perceptions in terms of sensitivity and that sensitivity of the information has an impact on privacy preference and willing to disclose the information [28]. As the IoT may impact the availability of diferent types of private information diferently, and that these types of information have diferent sensitivities, we posit that there will be dif ferent privacy preferences and privacy valuations for the diferent types of private information:

Hypothesis 4. The monetary value people place on privacy within an IoT context will vary depending on the type of private information being considered.

4.4. Who is providing private data and how this afects their privacy preference and privacy valuation in the IoT?

As privacy preference can be impacted by various individual factors, we consider a number of these factors that previous studies have indicated impact privacy preference and examine whether they will have the same impact under the IoT.

First, previous research has demonstrated that those respondents that have been exposed to a recent privacy breach will have difering Privacy Preference from the general population [63]. We posit that this efect will continue under the IoT:

Hypothesis 5. Exposure to a recent personal privacy breach negatively impacts a person’s willingness to accept the disclosure of private data and increases their monetary valuation of privacy within an IoT context.

Our second hypothesis related to personal factors is driven by research, [4] which indicated that exposure to media regarding privacy breaches may impact a person’s privacy preference. We therefore posit that exposure to recent news articles on privacy may also have an impact on privacy preference under the IoT:

Hypothesis 6. Exposure to recent news about high profile privacy breaches will negatively impact a person’s willingness to accept the disclosure of their private data and increase their monetary valuation of privacy in an IoT context.

The next set of hypotheses considers the impact of age on privacy preference and valuation. Some authors [64] have suggested that age has an impact on privacy behavior and that the younger people will have lower privacy preference and valuation than older people. In their study, they found that there was no statistically significant diference in the stated privacy preference of people from diferent age categories. They therefore posited that “a gap in privacy knowledge provides one explanation for the apparent license with which the young behave online” [64]. Conversely others [65] have argued that younger people have a higher privacy preference based on their more frequent manipulation of their privacy settings on social network sites. The question to ask is does more frequent adjustment of one’s privacy settings equate to a preference for more privacy in general or simply a preference for a more tailored approach to privacy based on context. This would be consistent with the findings of the IoT literature on privacy [19,20]. Consistent with this view that privacy preference and valuation is contextual not age-based, we posit that age will not have an impact on privacy preference in an IoT context:

Hypothesis 7. Age does not have an impact on a person’s privacy preference or the monetary valuation of privacy in an IoT context.

Also consistent with previous literature [64] on privacy preference we believe that the knowledge of privacy regulations does have an impact on privacy preference and valuation:

Hypothesis 8. Knowledge of privacy laws and regulation does have an impact on a person’s privacy preference increasing the monetary valuation of privacy in an IoT context.

Previous research has also identified a positive relationship between income and privacy preference with increasing income and wealth leading to more preference for privacy [22,61]. We posit that income and wealth may have an impact on respondents’ privacy preference, with those that have more money (and therefore more to lose) having a stronger preference for privacy:

Hypothesis 9. Increasing income and personal wealth have a positive impact on a person’s privacy preference and the valuation of privacy in an

## IoT context.

Some researchers have proposed that the knowledge of IT may have a positive impact on Privacy Preference [66], and have claimed that the knowledge of technical issues may make people more sensitive to the potential for hacking and misuse of data. This leads us to our next hypothesis:

Hypothesis 10. Knowledge of information technology has the impact of increasing a person’s privacy preference and their monetary valuation of privacy under the IoT.

Previous studies have also demonstrated an impact of gender on privacy preference with women typically preferring more privacy $\left[ 6 1 , 6 7 , 6 8 \right]$ because of the fact that they have a greater fear of being the victims of aggression of crime [67]. Implicit in these discussions is a linkage between physical security and privacy. We expect privacy preference and privacy valuation for women will increase under the IoT as the IoT provide more information particularly around physical lo cation. This leads us to our last hypothesis:

Hypothesis 11. A person’s gender has an impact on a person’s privacy preference and the monetary valuation of privacy under the IoT with women having higher privacy preference.

## 5. Methodology

In this section, we outline the various components of the metho dology we used for our study. We begin by detailing the DCE method, comparing it to the closest methodology, CA, and noting its econometric and behavioral advantages. We then outline the design of our survey, and explain how it addresses our hypotheses. This is followed by an outline of our data collection techniques.

## 5.1. The use of discrete choice experimental techniques

In this paper, we measure Privacy Valuation using a DCE, which is underpinned by the estimation of discrete choice models. DCEs have been used to investigate choice behavior in a wide range of literatures, including an extensive history in transportation [69] environmental and resource economics [70], health economics [71], and tourism [72].

DCE difers from methods outlined in our literature review on Privacy Valuation, but bears the most similarity to CA. In practice, there is often ambiguity about the diferences between DCEs and CA [73]. A common element is the recognition that the utility of an alternative is the sum of the utilities associated with the attributes that describe the alternative [44]. Both approaches are experimental in nature, use stated preference data, and present subjects with a set of alternatives for consideration, although the discrete choice models used with DCEs can also be used with revealed preference data.

What difers is the response mechanism, and the models estimated, with CA using rankings or ratings, and DCEs using choices. With CA, the rank of alternative i is generated as a direct function of the utility ex pression, as

$$
R a n k i n g _ {i} = \alpha + \beta^ {\prime} X _ {i} + \varepsilon_ {i},
$$

where is a constant, $\beta ^ { \prime }$ is a vector of estimated utility coeficients, and X is a vector of variables including attribute levels. There is no reason why the utility expression should consistently generate integer rank ings, and so an error term is used to handle this disparity.

With DCEs by contrast, the utility U of alternative i for individual n on choice occasion t is not measured directly, but treated as a latent construct, expressed as

$$
U _ {n i t} = \alpha_ {i} + \beta^ {'} X _ {n i t} + \varepsilon_ {n i t},
$$

where $\alpha _ { i }$ is an alternative specific constant, $\beta ^ { ' }$ is a vector of estimated utility coeficients, and $X _ { n i t }$ is a vector of attribute levels and potentially also interactions between attribute levels and individual characteristics, allowing individual diferences in utility based on observed characteristics to be directly tested. DCEs typically present each respondent with multiple ‘choice tasks,’ hence subscript t. Collectively, $\beta ^ { \prime } X _ { n i t }$ is referred to as the systematic component of utility. The random component of utility, $\varepsilon _ { i t } ,$ captures unidentified influences on choice, as well as differences across individuals that cannot be explained by the systematic component of utility. If we assume that $\varepsilon _ { i t }$ is distributed Extreme Value Type 1, it can be shown that the probability $P _ { n i t }$ of individual n choosing alternative i in a choice set of J alternatives is

$$
P _ {n i t} = \frac {e ^ {\alpha_ {i} + \beta^ {\prime} X _ {n i t}}}{\sum_ {j = 1} ^ {J} e ^ {\alpha_ {j} + \beta^ {\prime} X _ {n j t}}}
$$

The random component of utility plays an important behavioral role in the model, as when the magnitudes of the utility coeficients increase relative to the variance of , the choices will become more deterministically explained by the utility coeficients, and behavior will be less random. Indeed, DCEs are consistent with an underlying behavioral theory, Random Utility Theory (RUT), in a way that CA is not [74]. The underlying models are thus informed by a coherent theory, rather than being driven by model fit. Ordered logit and probit models are also based on RUT, and thus have a sound behavioral underpinning [75]; however, ranking has a heavy cognitive burden, which can result in inconsistencies in the ranking task and excess noise in the resulting models. Thus, the DCE literature has generally advocated obtaining multiple best choices instead of rankings of a single set of alternatives [74]. For these reasons, we advocate the use of DCEs for the elicitation of privacy preference when dealing with complex privacy calculi, such as choosing IoT devices. The choice response naturally aligns with the purchase of an IoT device, which is the point at which the individual starts to bear the privacy consequences of their decision. Furthermore, the representation of the IoT device as a bundle of privacy-related and other features allows privacy to be measured as a tradeof with other features.

As with CA, the DCE approach can readily calculate MRS between the attributes investigated, including WTP and WTA measures. Consider the WTA attribute k, through compensation in cost attribute c:

$$
W T A _ {k} = \frac {\frac {\partial}{\partial_ {k}} \beta_ {k} x _ {k}}{\frac {\partial}{\partial_ {c}} \beta_ {c} x _ {c}} = \frac {\beta_ {k}}{\beta_ {c}}
$$

Standard errors can be calculated for this WTA function using the Delta method. In this paper, we will report the significance of both the utility coefficients, and the WTA/WTP measures.

## 5.2. A discrete choice experiment for IoT privacy

As mentioned previously, we measure IoT Privacy Preference and IoT Privacy Valuation by asking survey respondents to participate in a realistic IoT privacy scenario, which was the choice between two diferent options in terms of the purchase of a fitness tracker with each option having a diferent combination of features. In these scenarios the dependent variable is the choice of IoT device, and from this we use the choice model to infer the WTA or WTP. It is then the WTA that we test for statistical significance. The independent variables are the features of the fitness tracker, each chosen for their perceived privacy impact.

Our survey participants were screened to only include respondents who indicated an interest to purchase a fitness tracker in the near future helping to ensure that they had some understanding of what a fitness tracker was. To set a common baseline for all hypothetical fitnes trackers presented to respondents, all trackers were described as a small wrist band, which can track heart rate, number of steps taken, body temperature, and physical location through a built-in global positioning system. The trackers also fully integrate with smart phones through Bluetooth to sync with calendars and contacts. A sequence of choice

Based on the stated features below which would be your most preferred fitness tracker?

<table><tr><td>Feature Category</td><td>Fitness Tracker Feature</td><td>Fitness Tracker Option #1</td><td>Fitness Tracker Option #2</td></tr><tr><td rowspan="2">Personal Health Information Features</td><td>Your health and fitness information is used by health insurance companies for their commercial benefit</td><td>✕</td><td>√</td></tr><tr><td>Automatic notification to emergency services in certain personal critical health situations (e.g. heart attack)</td><td>✕</td><td>√</td></tr><tr><td rowspan="2">Physical Location Information Features</td><td>Your location information is used by retailers for their commercial benefit</td><td>✕</td><td>√</td></tr><tr><td>Personalized traffic and travel safety and security warnings are provided to you based on your location</td><td>√</td><td>✕</td></tr><tr><td rowspan="2">Financial Features</td><td>Your purchase history information derived from the built-in payment functionality is used by retailers for their commercial benefit</td><td>✕</td><td>✕</td></tr><tr><td>Built in payment functionality to allow you to make purchases with your fitness tracker</td><td>√</td><td>✕</td></tr><tr><td>Administrative Features</td><td>History is available on how your data has been used by third parties</td><td>√</td><td>✕</td></tr><tr><td colspan="2">Price (in USD):</td><td>$85</td><td>$115</td></tr></table>

Fig. 3. Example Choice Task.

tasks then described those attributes that varied across devices and asked respondents to make a choice between the two fitness trackers.

Fig. 3 shows an example choice task. Respondents had to choose their most preferred of the two alternatives, which were referred to as fitness tracker options. Each alternative was described by seven features (excluding the price).

The first seven features were grouped into four categories: ‘personal health information,’ ‘physical location information,’ ‘financial,’ and ‘administrative.’ Each of the first three categories has two features, each of which is either present or absent. The first feature per category, which we will call “commercial benefit features,” involves the sharing of information with businesses for their commercial benefit. None of the categories indicate whether respondents would obtain a personal benefit from their information being shared. The second feature in each category (“personal benefit features”) may generate personal benefit, but requires sharing private information gathered by the fitness tracker. This allowed for the analysis of the role that personal benefit would play in the privacy calculus the individual undertook.

To facilitate the monetary valuation of the privacy-related attributes, an eighth feature was included, the price that the respondent would need to pay for the fitness tracker with the remaining seven features. The possible price levels were \$85, \$100, \$115, \$130, and \$145. Whether the monetary valuations are WTA or WTP measures will depend on the status quo for the consumer seeking to purchase an IoT device. Given the respondent is purchasing the device, we assume that the health, physical location, and financial information is not currently being shared with businesses. Consequently, the sharing of this information will represent a loss of privacy for the respondent, who will need to be compensated for this loss through a reduced price. Thus, we report WTA for the commercial benefit features. We further assume that the respondent does not currently have access to the personal benefit features, and so the associated monetary valuations are measures of their WTP for this product feature¹ . However. as the personal benefit features also require the sharing of information, privacy concerns may reduce the WTP.

The significance of the commercial benefit features informs us about H1. The significance of the personal benefit features would suggest that personal benefit can ofset any associated privacy concerns, in support of H2. To ascertain whether privacy preference varies across the types of privacy (H4), we created features that directly afect privacy of the person’s body (first category), behavior (second category), and personal data (third category).

A single-feature administrative category provides history on how data have been used by third parties. This is used to test if the potential secondary use of the data has an impact on privacy preference and valuation (H3). In this scenario, visibility of secondary use is equated to awareness and control over that secondary use by the respondent as they can choose not to use the fitness tracker.

We tested hypotheses 5 through 11 by relying on additional ques tions in the survey, which were presented after the choice tasks, listed in Table 1 below. Responses were in some cases recoded, based on a model specification search. For example, the recency of the privacy breach was found to be insignificant, and this was entered into the model as a binary variable representing whether there was any prior breach, regardless of when that breach occurred. Responses were analyzed for interaction with the commercial benefit attributes, allowing the WTA to be decomposed based on characteristics of respondents, or on their experience.

Table 1  
Supplementary questions used to test hypotheses 5 – 11.

<table><tr><td>Hypothesis</td><td>Question</td><td>Responses</td></tr><tr><td>5</td><td>Have you yourself ever experienced a breach of your own personal privacy?</td><td>Never, within the last 5 years, 2 years, 1 year, 6 months, and 1 month</td></tr><tr><td>6</td><td>How recently have you seen or heard an article in the news that talked about a breach of privacy?</td><td>Never, within the last 5 years, 2 years, 1 year, 6 months, and 1 month</td></tr><tr><td>7</td><td>To what age group do you belong?</td><td>18–24, 25–29, 30–34, 35–39, 40–44, 45–49, 50–54, 55–64, and 65+</td></tr><tr><td>8</td><td>How do you rate your knowledge of Privacy Law and the rules and regulations governing the use of your personal information?</td><td>None at all, some, knowledgeable, very knowledgeable, and expert</td></tr><tr><td>9</td><td>What is your current personal annual income in USD?</td><td>$0, $1 to $15,000, $15,001 to $31,000, $31,001 to $52,000, $52,001 to $78,000, $78,001 to $130,000, $130,001 or greater</td></tr><tr><td>10</td><td>How do you rate your knowledge of Information Technology?</td><td>None at all, some, knowledgeable, very knowledgeable, and expert</td></tr><tr><td>11</td><td>Please select your gender</td><td>Male, female, or other</td></tr></table>

Those hypotheses that directly related to privacy knowledge or experience (H5, H6, H8, and H10) were also analyzed to see the efect on WTP for personal benefit features. It was not possible to evaluate the interaction of the sociodemographic responses (H7, H9, and H11) with personal benefit features, as it would not be possible to determine if diferences in utility are due to difering preferences for the personal gain of the features, or difering degrees of privacy concern.

Hypotheses 5–11 were also tested for each of health, location, and financial privacy, to determine if the hypotheses can only be accepted for certain types of privacy. Only significant interactions were retained in the reported models.

In total the complete experimental design contained 20 unique choice tasks, split into two blocks of 10. To obtain more information per respondent, each respondent was assigned to a block and completed 10 choice tasks. They were then asked the supplementary questions listed in Table 1. An eficient design was generated in the Ngene software package [76] to maximize the information gain, with Bayesian priors used to account for uncertainty [77]. Some 400 respondents were tar geted to ensure adequate variation in sociodemographic characteristics, with 411 respondents recruited. Two multinomial logit (MNL) model were then estimated. The first only included the attributes as ex planatory variables and was used to test hypotheses from 1 to 4. The second model additionally included various interactions between attributes and the supplementary questions, and tested hypotheses from 5 to 11. All models were estimated with the Nlogit software package, which is a commercially available software package used for this type of analysis.

## 5.3. Data collection

Participants were crowd sourced from Mechanical Turk an online panel. The viability of using Mechanical Turk as a tool for crowdsourcing respondents for social science research has been demonstrated in the academic literature [78]. There has also been specific research on the eficacy of Mechanical Turk for privacy studies [66]. This research has demonstrated that compared to other sample providers, the MTurkers’ “greater knowledge of technical issues may make them more sensitive to the potential for hacking and misuse of online data,” and therefore generate a more conservative result when calculating disutility over lost privacy and the WTA for privacy loss [66]. Mechanical Turk has other advantages as a tool for social science research. Given the large pool of MTurkers, it is easy to source survey respondents quickly from a broad base. The tool also allows responses to be collected anonymously, while preventing the same anonymous respondent from completing the same survey twice.

To ensure data quality, we applied several filters prior to completing the survey. These included a CAPTCHA question to guarantee the survey was not being completed by a Robot. The design of the Mechanical Turk survey also prevented a person with the same login ID from answering the same survey twice. Also, respondents were restricted to those workers who had greater than a 90 % approval rate for tasks they had previously completed on MTurk, which helped to ensure that the respondents participating would provide a quality response. Respondents who had not completed the last question in our survey, where they needed to enter a five-digit number were also excluded from our analysis.

A number of filters were also applied, such as postsurvey completion and preanalysis, to ensure the quality of the results. Participants were asked a simple logical question: “Whilst watching the television, have you ever sufered a fatal heart attack?” Respondents that provided a response other than “Never” were excluded from analysis. Also, respondents that took less than two minutes to complete the survey were filtered from the survey results assessing that they had not taken sufficient time to read and understand the questions asked. As a prerequisite to taking the survey was that respondents had to have the intention to purchase a fitness tracker in the near future (and therefore have a basic understanding of the technology), anyone who answered that they had no intention of purchasing a fitness tracker were filtered out. After applving those filters, 352 respondents (sufficient to obtain statistically significant results) were remaining upon whom we based our analysis.

Previous studies have shown that Mechanical Turk Workers demographically are generally representative of the population as a whole [79]. The demographics of our Mechanical Turk sample set were consistent with that view in that both respondent age and income were well-distributed; geographically the respondents were drawn from across the greater United States of America and were 48.86 % male and 50.85 % female.

## 6. Results

## 6.1. MNL model without interactions

The first MNL model, used to test Hypotheses 1–4, does not include any interactions, and is reported in Table 2. In addition to absolute values, WTA and WTP measures are reported as a percentage of the average cost of the fitness trackers in the experiment, to provide some context for these figures. All utility coeficients bar one are significant at a 99 % confidence level. All three personal benefit features have significant, positive utility coefficients. The WTP measures for these features are also significant, ranging from \$33.53 for built-in payment functionality, to \$44.62 for personalized location-based personalized trafic, and travel safety and security warnings, to \$99.78 for automatic notification to emergency services. The utility coeficients for the commercial benefit features are negative and significant in two feature categories. The two associated WTA measures are also significant, with the use of health information by insurance companies requiring \$38.66 in compensation, and the use of location information by retailers requiring \$30.79 in compensation. By comparison, the utility of commercial use of financial information by retailers is not statistically significantly diferent from zero, and a significant monetary valuation cannot be generated, demonstrating a degree of indiference as to how one’s personal financial information is being used.

<table><tr><td>Feature category</td><td>Fitness tracker feature</td><td>Feature Benefit Type</td><td>Utility coefficient</td><td>Willingness to Accept Value (and % of average cost)</td><td>Willingness to Pay Value (and % of average cost)</td></tr><tr><td rowspan="2">Personal health information features</td><td>Your health and fitness information is used by insurance companies for their commercial benefit</td><td>Commercial</td><td>-0.2260***</td><td>$38.66** (33.6 %)</td><td></td></tr><tr><td>Automatic notification to emergency services in certain personal critical health situations (e.g., heart attack)</td><td>Personal</td><td>0.5833***</td><td></td><td>$99.78*** (86.7 %)</td></tr><tr><td rowspan="2">Physical location information features</td><td>Your location information is used by retailers for their commercial benefit</td><td>Commercial</td><td>-0.1780***</td><td>$30.79** (26.8 %)</td><td></td></tr><tr><td>Personalized traffic and travel safety and security warnings are provided to you based on your location</td><td>Personal</td><td>0.2608***</td><td></td><td>$44.62*** (38.8 %)</td></tr><tr><td rowspan="2">Financial features</td><td>Your purchase history information derived from the built-in payment functionality is used by retailers for their commercial benefit</td><td>Commercial</td><td>0.0677</td><td></td><td>$11.58 (10 %)</td></tr><tr><td>Built-in payment functionality to allow you to make purchases with your fitness tracker</td><td>Personal</td><td>0.1960***</td><td></td><td>$33.53** (29 %)</td></tr><tr><td rowspan="2">Administrative features Price</td><td>History is available to you on how your data have been used by third parties</td><td></td><td>0.1236***</td><td></td><td>$21.15** (18.4 %)</td></tr><tr><td></td><td></td><td>-0.0059***</td><td></td><td></td></tr><tr><td colspan="6">Note: Confidence levels: *** 99 %, ** 95 %, and * 90 %. The average attribute cost = $115.</td></tr></table>

In these results, we observe a pattern across feature categories, with personal health information category having the greatest monetary valuations for both personal and commercial benefit features, the financial category having the lowest monetary valuations for both (including indiference to commercial use of financial information), and the physical location category lying in between. The personal health and physical location categories are both contingent on the IoT, whereas the financial category is not. We posit that the higher valuation for the former two categories is due in part to the novelty of these factors. While financial information has been transmitted frequently over the Internet for years, the idea that someone can be physically tracked at all times and that their health information may be collected and used by service providers is relatively new. Our conclusion is that those forms of privacy more negatively impacted by the IoT generate higher levels of privacy concern, but that the overall level of privacy concern in the IoT is statistically significant.

Base MNL model with no interactions. Table 2

Reject Hypothesis 1: That the monetary valuation people place on privacy in the IoT will not be statistically diferent to zero.

Personal benefit also appears to bear an influence on the privacy calculus. All personal benefit features generated positive utility, and thus individuals are prepared to pay a premium for the features, despite the privacy compromises they entail. Thus we

Failed to Reject Hypothesis 2: The monetary value people place on privacy in an IoT context depends on their determination of the personal benefit they will gain from disclosing private information. Increased personal benefit will reduce the preference for more privacy preference and thus its monetary valuation in the IoT.

The utility coeficient for “History is available to you on how your data have been used by third parties” was positive and significant to the 99 % level. The valuation of this information was \$21.15 USD and significant to the 95 % level. In this context, we interpret awareness of how private IoT information is being used as a form of control over their data, and therefore an important factor in the individuals IoT privacy calculus:

Failed to Reject Hypothesis 3: The ability to monitor how ones private information is being used will reduce privacy preference and decrease the monetary value one assigns to their privacy within an IoT context.

The diferences in sensitivity to aggregate commercial benefit features across the feature categories are supportive of H4. Personal health and physical location have WTA measures of \$38.66 and \$30.79 respectively, and both measures are significantly diferent from WTA the financial features (p = 0.013 and p = 0.027). Conversely, personal health and physical location WTA measures are not significantly different to each other (p = 0.377). However, once we disaggregate the monetary valuations using interactions in our second model reported below, we will see that diferences between personal health and physical location privacy will exist for people of certain age, gender, and privacy breach history. It could be argued that the sensitivity of individuals to their data being used for commercial benefit might vary depending on the commercial entity receiving the data. In the choice experiment, health information was shared with insurance companies, while physical location and financial information was shared with retailers. That the WTA difered between physical location and financial information, despite this information being shared with the same commercial entity, suggests that the diferences are due to diferent types of privacy, not just diferent recipients of the data. Overall, we

<table><tr><td>Feature category</td><td>Fitness Tracker Feature</td><td>Parameter</td><td>Utility coefficient</td><td>Related hypotheses</td></tr><tr><td rowspan="6">Personal health information features</td><td rowspan="4">Your health and fitness information is used by insurance companies for their commercial benefit</td><td>Main effect</td><td>0.2801**</td><td></td></tr><tr><td>x Any privacy breach history</td><td>-0.3142***</td><td>H5</td></tr><tr><td>x Age in years</td><td>-0.0117***</td><td>H7</td></tr><tr><td>x Male</td><td>0.1785**</td><td>H11</td></tr><tr><td rowspan="2">Automatic notification to emergency services in certain personal critical health situations (e.g., heart attack)</td><td>Main effect</td><td>0.6751***</td><td></td></tr><tr><td>x Any privacy breach history</td><td>-0.1414*</td><td>H5</td></tr><tr><td rowspan="5">Physical location information features</td><td rowspan="3">Your location information is used by retailers for their commercial benefit</td><td>Main effect</td><td>-0.1596**</td><td></td></tr><tr><td>x Any privacy breach history</td><td>-0.1844***</td><td>H5</td></tr><tr><td>x Male</td><td>0.1690**</td><td>H11</td></tr><tr><td rowspan="2">Personalized traffic and travel safety and security warnings are provided based on your location</td><td>Main effect</td><td>0.3670***</td><td></td></tr><tr><td>x Any privacy breach history</td><td>-0.1783**</td><td>H5</td></tr><tr><td rowspan="2">Financial features</td><td>Your purchase history information derived from the built-in payment functionality is used by retailers for their commercial benefit</td><td>Main effect</td><td>0.0681</td><td></td></tr><tr><td>Built-in payment functionality to allow you to make purchases with your fitness tracker</td><td>Main effect</td><td>0.1993***</td><td></td></tr><tr><td rowspan="2">Administrative features</td><td rowspan="2">History is available to you on how your data have been used by third parties</td><td>Main effect</td><td>0.3537***</td><td></td></tr><tr><td>x Any privacy knowledge</td><td>-0.2558**</td><td>H8</td></tr><tr><td>Price</td><td></td><td>Main effect</td><td>-0.0061***</td><td></td></tr></table>

MNL model with interactions. Table 3  
Note: Confidence levels: \*\*\* 99 %, \*\* 95 %, \* 90 %.

Failed to Reject Hypothesis 4: The monetary value people place on privacy within an IoT context will vary depending on the type of private information being considered.

## 6.2. Extended MNL model with interactions

The second MNL model, reported in Table 3, is the consequence of the model specification search process described earlier, which tested all the individual factors listed in Table 1. Table 3 reports the utility coeficients for both the main efects for each product feature, and all significant interactions. For any given feature, a unique WTA or WTP can be generated for each combination of significant interaction responses<sup>2</sup>, and these values are reported in Table 4. When testing the hypotheses that rely on the interactions, we will report two p–values. The first reports the significance of the utility coeficient. The second reports the significance of the marginal contribution of the interaction term to the WTA/WTP, and is more conservative as it includes the variance associated with the cost parameter. We retain all interactions for which p < 0.1 for the utility coeficients.

First we consider the personal factors related to previous exposure to privacy issues. Exposure to recent media on privacy breach had no statistically significant impact on privacy preference. In contrast, personal exposure to privacy breach has a significant impact across all of the health and location features. Respondents with a privacy breach history were more sensitive to commercial use of health, with an additional WTA of \$51.41 $( \mathbf { p } = 0 . 0 0 0 ; \mathbf { p } = 0 . 0 1 6 )$ . For example, 55- to 64- year-old male respondents without a privacy breach history need to be compensated \$39.85 for the health commercial benefit feature, but this increases to \$91.26 for the same demographic who has had a privacy breach at some point in the past. Likewise, those with a privacy breach history are more sensitive to commercial use of their location, with an additional WTA of \$30.17 $( \mathbf { p } = 0 . 0 0 9 ; \mathbf { p } = 0 . 0 5 1 )$ . For example, male respondents without a history are not sensitive at all to this use (with an insignificant WTP of \$1.53), but those with a history have a WTA of \$28.63. Health personal gain (notification to emergency services) is reduced by \$23.14 (although only with marginal significance: p = 0.059; 0.110), from \$110.48 to \$87.34 for all respondents, and location personal gain is reduced by \$29.17, from \$60.06 to \$30.89 for all respondents $\left( \mathbf { p } = 0 . 0 1 5 ; \ \mathbf { p } = 0 . 0 6 1 \right)$ . This strongly suggests that these individuals are more concerned about the privacy implications of these features that otherwise bring personal gain. No statistically significant impact on financial information privacy preference was found because of personal privacy breach or exposure to privacy media. What becomes clear from this analysis is that for there to be an impact on privacy preference, the experience with privacy issues needs to be personal with the individual having had their own privacy breach and that simple media exposure is not suficient. In summary:

Failed to Reject Hypothesis 5: Exposure to a recent personal privacy breach negatively impacts a person’s willingness to accept the disclosure of private data and increases their monetary valuation of privacy within an IoT context

## … and …

Reject Hypothesis 6: Exposure to recent news about high-profile privacy breaches will negatively impact a person’s willingness to accept the disclosure of their private data and increase their monetary valuation of privacy in an IoT context.

<sup>2</sup> Consider the WTP for the administrative feature. For individuals without privacy knowledge, WTP = -1\*(0.3537+0x-0.2558)/-0.0061 = \$57.88, and for individuals with privacy knowledge, WTP = -1\*(0.3537+1x-0.2558)/- 0.0061 = \$16.02. The values reported here are rounded, with the WTP values calculated from the precise estimated coeficients.

WTA/WTP decomposed by privacy breach, privacy knowledge, gender and age. <sub>a</sub>b<sup>le</sup> <sup>4</sup>

<table><tr><td>Feature category</td><td>Fitness Tracker Feature</td><td>Privacy breach history (H5)</td><td>Age (H7)</td><td>Privacy knowledge (H8)</td><td>Gender (H11)</td><td>% sample</td><td>WTA (and % of Average Cost)</td><td>WTP (and % of Average Cost)</td></tr><tr><td rowspan="10">Personal health information features</td><td rowspan="8">Your health and fitness information is used by insurance companies for their commercial benefit</td><td>No</td><td>18-24</td><td>-</td><td>Female</td><td>4.1 %</td><td></td><td>$5.62 (4.9 %)</td></tr><tr><td>Yes</td><td>18-24</td><td>-</td><td>Female</td><td>1.9 %</td><td>$45.79** (39.8 %)</td><td></td></tr><tr><td>No</td><td>18-24</td><td>-</td><td>Male</td><td>3.3 %</td><td></td><td>$34.83** (30.3 %)</td></tr><tr><td>Yes</td><td>18-24</td><td>-</td><td>Male</td><td>3.0 %</td><td>$16.58 (14.4 %)</td><td></td></tr><tr><td>No</td><td>55-64</td><td>-</td><td>Female</td><td>1.4 %</td><td>$69.06** (60 %)</td><td></td></tr><tr><td>Yes</td><td>55-64</td><td>-</td><td>Female</td><td>1.9 %</td><td>$120.47*** (105 %)</td><td></td></tr><tr><td>No</td><td>55-64</td><td>-</td><td>Male</td><td>1.1 %</td><td>$39.85* (34.6 %)</td><td></td></tr><tr><td>Yes</td><td>55-64</td><td>-</td><td>Male</td><td>2.4 %</td><td>$91.26*** (79.3%)</td><td></td></tr><tr><td rowspan="2">Automatic notification to emergency services in certain personal critical health situations (e.g., heart attack)</td><td>No</td><td>-</td><td>-</td><td>-</td><td>56.6 %</td><td></td><td>$110.48*** (96 %)</td></tr><tr><td>Yes</td><td>-</td><td>-</td><td>-</td><td>43.4 %</td><td></td><td>$87.34*** (75.9 %)</td></tr><tr><td rowspan="6">Physical location information features</td><td rowspan="4">Your location information is used by retailers for their commercial benefit</td><td>No</td><td>-</td><td>-</td><td>Female</td><td>22.0 %</td><td>$26.11* (22.7 %)</td><td></td></tr><tr><td>Yes</td><td>-</td><td>-</td><td>Female</td><td>28.7 %</td><td>$56.28** (48.9 %)</td><td></td></tr><tr><td>No</td><td>-</td><td>-</td><td>Male</td><td>21.4 %</td><td></td><td>$1.53 (1.3 %)</td></tr><tr><td>Yes</td><td>-</td><td>-</td><td>Male</td><td>27.9 %</td><td>$28.63** (24.9 %)</td><td></td></tr><tr><td rowspan="2">Personalized traffic and travel safety and security warnings are provided to you based on your location</td><td>No</td><td>-</td><td>-</td><td>-</td><td>56.6 %</td><td></td><td>$60.06*** (52.7 %)</td></tr><tr><td>Yes</td><td>-</td><td>-</td><td>-</td><td>43.4 %</td><td></td><td>$30.89** (26.9 %)</td></tr><tr><td rowspan="2">Financial features</td><td>Your purchase history information derived from the built-in payment functionality is used by retailers for their commercial benefit</td><td>-</td><td>-</td><td>-</td><td>-</td><td>100 %</td><td></td><td>$11.14 (9.7 %)</td></tr><tr><td>Built-in payment functionality to allow you to make purchases with your fitness tracker</td><td>-</td><td>-</td><td>-</td><td>-</td><td>100 %</td><td></td><td>$32.62** (28.4 %)</td></tr><tr><td rowspan="2">Administrative features</td><td rowspan="2">History is available to you on how your data have been used by third parties</td><td>-</td><td>-</td><td>No</td><td>-</td><td>11.7 %</td><td></td><td>$57.88** (50.3 %)</td></tr><tr><td>-</td><td>-</td><td>Yes</td><td>-</td><td>88.3 %</td><td></td><td>$16.02** (13.8 %)</td></tr></table>

Note: Confidence levels: \*\*\* 99 %, \*\* 95 %, \* 90 %. The average attribute cost = \$115.

The next series of personal factors we consider are self-reported knowledge of IT and privacy regulation. The question here being would knowledge and education impact a person’s privacy preference and WTA the disclosure of private IoT-based information. Our analysis here indicates limited impact on privacy preference. We find the only efect being self-reported knowledge of privacy law and regulation moderating a person’s desire to understand how their private information is being used, with WTP reduced for the history feature, from \$57.88 to $\$ 16.02( p$ . The specific causal factors for this are unclear but perhaps may be due to respondents experienced in privacy regulation considering these controls either inefective or unnecessary. In summary, it is concluded that there is no clear relationship between IT and privacy regulation knowledge and privacy preference in general. We therefore:

Failed to Reject (Partially) Hypothesis 8: Knowledge of privacy laws and regulation does have an impact on a person’s privacy preference increasing the monetary valuation of privacy in an IoT context.

… and …

Reject Hypothesis 10: Knowledge of information technology has the impact of increasing a person’s privacy preference and their monetary valuation of privacy under the IoT.

The final series of personal factors that we consider as part of the Extended MNL Model are demographic factors such as age, sex, and personal income and health. Contrary to previous research there appears to be no relationship between income, wealth, and personal privacy preference in this fitness tracker IoT context. As predicted by the literature [64], in terms of age the only relationship that was sig nificant was related to health information, with WTA for the health commercial benefit feature increasing by \$1.92 for each additional year of age $( \mathbf { p } = 0 . 0 0 0 ; \ \mathbf { p } = 0 . 0 2 2 )$ . For example, for female respondents with no privacy breach history, WTA increases from \$45.79 for 21 year old to \$139.62 for 70 year old respondents. We posit that the efect here is due to a personal benefits calculus in the most elderly of respondents, which considers the disclosure of private health information related to their bodies as potentially damaging financially (i.e., higher health insurance premiums).

As also predicted by the literature [61,67,68], there is a linkage between privacy preference and gender, with men having a lower WTA in all categories as compared to women. This is particularly true for those two factors, such as health and location information, which are more directly linked to the IoT. Men clearly have lower privacy preference for commercial use of health and location information. The health commercial benefit feature WTA is \$29.21 lower for male than female respondents (p = 0.011; p = 0.049), with, for example, 70 year old respondents with a privacy breach history having a WTA of \$110.41 if they are male, versus \$139.62 if they are female respondents. The location commercial benefit feature WTA is \$27.65 lower for male than female (p = 0.015; p = 0.056) respondents. For those with a privacy breach history, the WTA is \$28.63 if they are male and \$56.28 if they are female. In conclusion we:

Reject (Partially) Hypothesis 7: Age does not have an impact on a person’s privacy preference or the monetary valuation of privacy in an IoT context.

…and…

Reject Hypothesis 9: Increasing income and personal wealth have a positive impact on a person’s privacy preference and monetary valuation of privacy in an IoT context.

…and…

Failed to Reject Hypothesis 11: A person’s gender has an impact on a person’s privacy preference and the monetary valuation of privacy under the IoT with women having higher privacy preference.

## 7. Discussion

## 7.1. Implications for theory

Having presented and discussed our results, we now consider their implications for Privacy Theory in the IoT. Our analysis shows that context plays a heavy role in an individual’s privacy calculus, privacy preference, and privacy valuation. This is consistent with the previous theory on IoT Privacy [19,20].

What our research also indicates is that the type of private information and personal factors play a significant part in a person’s privacy calculus, privacy preference, and privacy valuation. This sug gests that other studies that do not vary on the type of privacy information or investigate diferences based on sociodemographic, experience, and knowledge may average out a much more nuanced distribution of privacy valuation.

There is also a clear diference in those types of private information, which are more significantly impacted by newer technologies like the IoT; whereas those types of private information which are not novel to the IoT are less impacted. We posit then that as those forms of technology become more broadly used and gain some form of cognitive legitimacy that privacy concern and the resultant privacy preference will likely decrease [80,81]. However, any decrease in concern might be ofset by high levels of privacy breaches, which we have shown increases privacy valuation.

## 7.2. Implications for practice

There are three main implications for practice that could be concluded from our study. First is that the WTA a reduction in privacy for the various IoT scenarios ranged in value from as low as \$30.79 USD per person for individuals to provide their location data to as high as \$139.62 USD per person for individuals in certain demographics to provide their health information. This indicates that process, procedures, and technology, which cost an organization more than these amounts, may be inappropriate and need to be reconsidered. In this context, there is a “right amount of privacy” depending on the type of information, the context, and the individual in question. Treating everyone equally in terms of privacy is not necessarily the best strategy.

The second conclusion is that because the WTA varies significantly based on the type of private information, practitioners are well advised to adjust the level of process, procedures, and technology used to ensure privacy based on the type of private information being captured. Otherwise, they may either be ofering too much or too little privacy. In other words, a “one solution fits all” approach does not apply to privacy concern. Just how much efort should be expended to ensure privacy will depend on the type of information, and so it may be advisable to conduct studies such as the one herein to determine sensitivity to specific information types before the deployment of an IoT-based solution.

The third implication from this research is that the degree to which individuals are aware of how their private information is being used will impact their privacy preference and associated privacy valuation. This means that organizations may optimize their privacy processes, procedures, and technologies by ensuring full and complete disclosure of how the private information they collect may be used.

## 7.3. Limitations

The use of DCE methods, realistic choice scenarios, and a broader data set means that the statistical results are robust and nuanced. However, this study has relied on the standard DCE assumption that the choice process is compensatory. This implies that the privacy calculus is itself compensatory, and trade-ofs can and will be made between privacy and other features. Other possibilities that could be modeled with appropriate extensions to the choice models are the elimination of devices from consideration that have certain levels of privacy intrusion [82] and complete indiference to privacy by segments of the population [83]. There is also the question of the generalizability of the study findings outside of the consumer products vertical in IoT.

## 7.4. Future research opportunities

We posited that as these technologies are more broadly used that they gain some form of cognitive legitimacy and that privacy preference decreases. It would be useful therefore to prove out this notion by conducting research into the legitimation process of adopting the IoT and how this impacts privacy preference. One way would be to conduct a longitudinal study over time of how individuals value the various types of privacy concern in various contexts understanding whether privacy concern decreases over time as these technologies gain cognitive legitimacy [80].

Further cross-sectional studies across a number of diferent IoT scenarios in diferent industries within the diferent types of privacy concern would also be useful. This would prove out the generalizability of the initial findings in our study to other IoT verticals.

Modeling alternative privacy calculi would provide insight into the extent to which privacy can be traded away.

Finally, we identified a focus on individual factors that may influence privacy concern and therefore privacy valuation. It would be of interest to attempt a study, which looked to understand institutional factors which afect privacy. These institutional factors could include (but are not necessarily limited to) the medium of communication used as indicated in the Social Presence Theory [84] or the degree of information disclosure reciprocity as indicated in the Social Response Theory [85].

## 8. Conclusions

The IoT now enables certain forms of private information (e.g., location and health) to be more readily collected than before. As a result, these new forms of information collection experience a higher sensitivity to privacy concern on the part of the individual. In part, this is due to the novelty of the data collection process and in part due to a perceived lack of cognitive legitimacy about that same process. Therefore, individuals will exhibit a higher preference for privacy in these cases, and will be willing to pay more to address their privacy concerns in these contexts. We also conclude that the degree to which individuals have awareness of how their private information is used will moderate that privacy preference and valuation within the IoT but that the perceived benefits from control are in turn moderated by the knowledge of privacy regulations.

What is important to consider through all of this is that the valuations that people assign to privacy are low and heavily afected by the personal benefit that disclosing this private information provides. This reinforces the view that more privacy is not always better and that in some cases the costs of additional regulation regarding privacy outweigh the benefits and the actual desire on the part of the individual to “pay” for that regulation. The overall conclusion is that privacy legislation to enforce more privacy does need to be judicious and specific to the use cases for the private information in question and the types of private information involved.

## Funding

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

## CRediT authorship contribution statement

David Goad: Conceptualization, Methodology, Investigation, Formal analysis, Data curation, Writing - original draft, Visualization. Andrew T. Collins: Methodology, Software, Formal analysis,

Validation, Writing - review & editing, Visualization. Uri Gal: Writing - review & editing.

## Appendix A. Supplementary data

Supplementary material related to this article can be found, in the online version, at doi:https://doi.org/10.1016/j.im.2020.103292.

## References

[1] F. Tully, Lheureux, Hung Geschlickter, Internet of things primer, Gartner Research, (2016).

[2] D.J. Solove, Conceptualizing privacy, Cal. Law Rev. 90 (2002) 1087.

[3] A.F. Westin, O.M. Ruebhausen, Privacy and Freedom Vol. 1 Atheneum, New York, 1967.

[4] M. Madden, R. Lee, American’s attitudes about privacy, security and surveillance, in: M. Dugan (Ed.), Pew Research Centre, 2015.

[5] EMC, The EMC Privacy Index: Global and In-Depth Country Results, (2014)

[6] BBVA. Leer (Ed.). Internet of Things: Connected Home. 2015.

[7] A. McIntyre, B. Blau, M. Reitz, Forecast: wearable electronic devices worldwide, Gartner Research, (2016).

[8] S. Zuboff. Big other: surveillance capitalism and the prospects of an information civilization, J. Inf. Technol. 30 (1) (2015) 75–89.

[9] N.H. Heudecker, Jim, Survey analysis: Big data investments begin tapering in 2016, Gartner Research, (2016).

[10] C. Pache, B. Taney, Complaince with Notifiable Data Breaches Scheme, Available from: (2018) https://www.australasianlawyer.com.au/sections/features compliance-with-the-notifiable-data-breaches-scheme-246600.aspx

[11] B. Goodman, S. Flaxman, European Union Regulations on Algorithmic Decision making and a" Right to Explanation, arXiv preprint arXiv:1606.08813 (2016).

[12] B. Willemsem, S. Matthew, T. Ayol, Predicts 2017: privacy becomes a necessity with opportunity, Gartner Research, (2016).

[13] Ponemon, The True Cost of Compliance: A Benchmark Study of Multinationa Organizations, Ponemon Institute, 2011 P. Institute, Editor.

[14] L.R. Christensen, F. Etro, European Data Protection: Impact of the EU Data-pro tection Regulation, Vox EU, 2013.

[15] M. Hung, A. Singh, D. Mahdi, Hardware security and its impact on IoT projects, Gartner Research, (2016).

[16] M. Hung, A. Singh, D.A. Mahdi, Hardware security and its impact on IoT projects, Gartner Research, (2016).

[17] A. Acquisti, C.R. Taylor, L. Wagman, The Economics of Privacy, Available at SSRN 2580411 (2016).

[18] C.-L. Hsu, J.C.-C. Lin, An empirical examination of consumer adoption of Internet of Things services: network externalities and concern for information privacy perspectives, Comput. Human Behay. 62 (2016) 516–527

[19] P.E. Naeini, et al.. Privacy expectations and preferences in an IoT world. Thirteenth Symposium on Usable Privacy and Security ({SOUPS} 2017) (2017).

[21] D. Kim, et al., Willingness to provide personal information: perspective of privacy calculus in IoT services, Comput. Human Behav. 92 (2019) 273–281.

[22] A. Acquisti, J. Grossklags, Privacy and rationality in individual decision making, IEEE Secur. Priv. 3 (1) (2005) 26–33.

[23] C. Jensen, C. Potts, C. Jensen, Privacy practices of Internet users: self-reports versus observed behavior, Int. J. Hum. Comput. Stud. 63 (1-2) (2005) 203–227.

[24] K. Connelly, A. Khalil, Y. Liu, Do I do what I say?: Observed versus stated privacy preferences, IFIP Conference on Human-Computer Interaction, Springer. 2007.

[25] J.J. Louviere, D.A. Hensher, J.D. Swait, Stated Choice Methods: Analysis and Applications, Cambridge University Press, 2000.

[26] D.J. Street, L. Burgess, The Construction of Optimal Stated Choice Experiments: Theory and Methods Vol. 647 John Wiley & Sons, 2007.

[27] H.J. Smith, S.J. Milberg, S.J. Burke, Information privacy: measuring individuals concerns about organizational practices, MIS O. (1996) 167–196.

[28] N.K. Malhotra, S.S. Kim, J. Agarwal, Internet users’ information privacy concerns (IUIPC): the construct, the scale, and a causal model, Inf. Syst. Res. 15 (4) (2004) 336-355.

[29] K.E. Train, Discrete Choice Methods With Simulation, Cambridge University Press 2009.

[30] R. Chow, et al., HCI in business: a collaboration with academia in IoT privacy. International Conference on HCI in Business, Springer 2015

[31] W. Zhou, S. Piramuthu, Information relevance model of customized privacy for IoT, J. Bus, Ethics 131 (1) (2015) 19–30

[32] J. Lau, B. Zimmerman, F. Schaub, Alexa, are you listening?: Privacy perceptions concerns and privacy-seeking behaviors with smart speakers, Proceedings of the ACM on Human-Computer Interaction (2018) 102 2(CSCW).

[33] N. Apthorpe, et al., Discovering smart home internet of things privacy norms using contextual integrity, Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (2018) 59 2(2).

[34] S. Zheng, et al., User perceptions of smart home IoT privacy, Proceedings of the ACM on Human-Computer Interaction (2018) 200 2(CSCW).

[35] V. Kisekka, J.S. Giboney. The effectiveness of health care information technologies evaluation of trust, security beliefs. and privacy as determinants of health care outcomes. J. Med. Internet Res. 20 (4) (2018) e107.

[36] P. Emami Naeini, et al., The influence of Friends and experts on privacy decision making in IoT scenarios, Proceedings of the ACM on Human-Computer Interaction (2018).48.2(CSCW).

[37] M.L. Katz, C. Shapiro, Network externalities, competition, and compatibility, Am. Econ, Rev, 75 (3) (1985) 424–440.

[38] Y. Yang, et al., A survey on security and privacy issues in Internet-of-Things, IEEE Internet Things J. 4 (5) (2017) 1250–1258.

[39] W. Zhou, S. Piramuthu, Security/privacy of wearable fitness tracking IoT devices, 2014 9th Iberian Conference on Information Systems and Technologies (CISTI), IEEE, 2014.

[40] P. Bahirat, et al., A data-driven approach to developing iot privacy-setting interfaces, 23rd International Conference on Intelligent User Interfaces, ACM, 2018.

[41] X. Caron, et al., The Internet of Things (IoT) and its impact on individual privacy: an Australian perspective, Comput. Law Secur. Rep. 32 (1) (2016) 4–15.

[42] Y. Li, Theories in online information privacy research: a critical review and an in tegrated framework, Decis. Support Syst. 54 (1) (2012) 471–481.

[43] S. Lichtenstein, P. Slovic, The Construction of Preference, Cambridge University Press, 2006.

[44] K.J. Lancaster, A new approach to consumer theory, J. Polit. Econ. 74 (2) (1966) 132-157

[45] S. Rosen, Hedonic prices and implicit markets: product diferentiation in pure competition, J. Polit. Econ. 82 (1) (1974) 34–55.

[46] D. McFadden, Conditional logit analysis of qualitative choice behavior, Front. Econometrics (1973).

[47] R.W. Rogers, A protection motivation theory of fear appeals and attitude change1, J. Psychol. 91 (1) (1975) 93–114.

[48] S. Petronio, Communication boundary management: a theoretical model of mana ging disclosure of private information between marital couples, Commun. Theory 1 (4) (1991) 311–335.

[49] A. Bandura, Social cognitive theory: an agentic perspective, Annu. Rev. Psychol. 52 (1) (2001) 1–26.

[50] I.A. Junglas, N.A. Johnson, C. Spitzmüller, Personality traits and concern for privacy: an empirical study in the context of location-based services, Eur. J. Inf. Syst. 17 (4) (2008) 387–402.

[51] P.A. Norberg, D.R. Horne, D.A. Horne, The privacy paradox: personal information disclosure intentions versus behaviors, J. Consum. Af. 41 (1) (2007) 100–126.

[52] S. Pötzsch, Privacy awareness: a means to solve the privacy paradox? IFIP Summer School on the Future of Identity in the Information Society, Springer, 2008.

[53] S. Kokolakis, Privacy attitudes and privacy behaviour: a review of current research on the privacy paradox phenomenon, Comput, Secur, 64 (2017) 122-134.

[54] J.A. Deighton, R.C. Blattberg, Interactive marketing: exploiting the age of addres sability, Sloan Manage. Rev. 33 (1) (1991) 5–14.

[55] R. Page, Your Health E-Wallet, Choice (2017) [cited 2018 15 Oct 2018]; Available from: https://www.choice.com.au/electronics-and-technology/internet/using online-services/articles/ehealth-records-online

[56] R.A. Posner, The economics of privacy, Am. Econ. Rev. 71 (2) (1981) 405–409.

[57] P.H. Rubin, T.M. Lenard, Privacy and the Commercial Use of Personal Information, Springer Science & Business Media, 2002.

[58] I.-H. Hann, et al., Overcoming online information privacy concerns: an informationprocessing theory approach, J. Manag. Inf. Syst. 24 (2) (2007) 13–42.

[59] A. Acquisti, L.K. John, G. Loewenstein, What is privacy worth? J. Legal Stud. 42 (2) (2013) 249–274.

[60] E.F. Stone, et al., A field experiment comparing information-privacy values, beliefs, and attitudes across several types of organizations. J. Appl. Psychol. 68 (3) (1983) 459.

[61] J.P. Carrascal, et al., Your browsing behavior for a big mac: economics of persona information online. Proceedings of the 22nd International Conference on World Wide Web, ACM. 2013.

[62] A. Acquisti, L. Brandimarte, G. Loewenstein, Privacy and human behavior in the age of information, Science 347 (6221) (2015) 509–514.

[63] H. Cho, J.-S. Lee, S. Chung, Optimistic bias about online privacy risks: testing the moderating effects of perceived controllability and prior experience, Comput. Human Behav. 26 (5) (2010) 987–995.

[64] C.J. Hoofnagle, et al., How Diferent Are Young Adults From Older Adults When It Comes to Information Privacy Attitudes and Policies? (2010).

[65] G. Blank, G. Bolsover, E. Dubois, A New Privacy Paradox, (2014).

[66] S. Schnorf, et al., A comparison of six sample providers regarding online privacy

benchmarks, SOUPS Workshop on Privacy Personas and Segmentation (2014)

[67] D.M. Moscardelli, R. Divine, Adolescents’ concern for privacy when using the Internet: An empirical analysis of predictors and relationships with privacy‐pro tecting behaviors. Fam. Consum. Sci, Res, J. 35 (3) (2007) 232-252.

[68] J. Fogel, E. Nehmad, Internet social network communities: risk taking, trust, and privacy concerns, Comput. Human Behav. 25 (1) (2009) 153–160.

[69] D.A. Hensher, Stated preference analysis of travel choices: the state of practice, Transportation 21 (2) (1994) 107–133.

[70] D. Hoyos, The state of the art of environmental valuation with discrete choice ex periments, Ecol. Econ. 69 (8) (2010) 1595–1603.

[71] E.W. de Bekker‐Grob, M. Ryan, K. Gerard, Discrete choice experiments in health economics: a review of the literature, Health Econ. 21 (2) (2012) 145–172.

[72] T. Huybers, Domestic tourism destination choices—a choice modelling analysis, Int. J. Tour. Res. 5 (6) (2003) 445–459.

[73] R.T. Carson, J.J. Louviere, A common nomenclature for stated preference elicitation approaches, Environ, Resour. Econ, 49 (4) (2011) 539–559.

[74] J.J. Louviere, T.N. Flynn, R.T. Carson, Discrete choice experiments are not conjoint analysis, J. Choice Model. 3 (3) (2010) 57–72.

[75] W.H. Greene, D.A. Hensher, Modeling Ordered Choices: a Primer, Cambridge University Press, 2010

[76] ChoiceMetrics, Ngene 1.2 User Manual & Reference Guide, (2018)

[77] Z. Sandor, M. Wedel, Designing conjoint choice experiments using managers’ prior beliefs, J. Mark. Res. 38 (4) (2001) 430–444.

[78] W. Mason, S. Suri, Conducting behavioral research on amazon’s mechanical turk, Behay, Res. Methods 44 (1) (2012) 1–23.

[79] N. Stewart, C. UngeMach, A. Harris, The Average Population of Mechanical Turn Workers, (2015).

[80] C. Binz, et al., The thorny road to technology legitimation—institutional work for potable water reuse in California, Technol. Forecast. Soc. Change 103 (2016) 249.

[81] C. Johnson, T.J. Dowd, C.L. Ridgeway, Legitimacy as a social process, Annu. Rev. Sociol. 32 (2006) 53–78.

[82] T.T. Koo, A.T. Collins, A. Williamson, C. Caponecchia, How safety risk information and alternative forms of presenting it afect traveler decision rules in international flight choice, J. travel res. 58 (3) (2019) 480–495.

[83] D. Campbell, W.G. Hutchinson, R. Scarpa, Incorporating discontinuous preferences into the analysis of discrete choice experiments, Environ. Resour. Econ, 41 (3) (2008) 401–417.

[84] R.E. Rice, Media appropriateness: using social presence theory to compare tradi tional and new organizational media. Hum. Commun, Res. 19 (4) (1993) 451–484

[85] Y. Moon, Intimate exchanges: using computers to elicit self-disclosure from con sumers, J. Consum. Res. 26 (4) (2000) 323–339.

David Goad, Postgraduate Fellow, Business Information Systems, The University of Sydney. David's research interests include the Internet of Things and Artificial Intelligence. He teaches Digital Innovation and Digital Transformation at The University of Sydney and The University of New South Wales. David has degrees in Engineering and Business, several technical qualifications and has over 20 years of industry and academic experience. He actively advises large enterprises on their IT, AI and IoT strategies. David has a pumber of previously published academic articles including articles on the Internet of Things and Algorithmic Decision Making/ Artificial Intelligence.

Andrew T. Collins, Senior Lecturer, Institute of Transport and Logistics Studies, The University of Sydney. Andrew's research interests focus on the behavioral influences of decision makers in a range of fields, including logistics, supply chain management, and transport. He also has methodological research interests, in the areas of discrete choice modelling, choice heuristics, and stated choice experimental design. He is a codeveloper of Ngene, a widely used software package which generates stated choice experimental designs.

Uri Gal, is an Associate Professor of Business Information Systems at the University of Sydney Business School., His research takes a social view of organisational processes in the context of the implementation and use of digital technologies. He is particularly interested in the relationships between people and technology in organisations, and the changes in the nature of work practices, organisational identities, and interactions associated with the introduction of algorithmic technologies
