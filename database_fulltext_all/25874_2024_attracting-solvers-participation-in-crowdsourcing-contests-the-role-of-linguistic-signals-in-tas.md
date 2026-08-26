---
otero_id: 25874
otero_key: "VN2Z443D"
title: "Attracting solvers' participation in crowdsourcing contests: The role of linguistic signals in task descriptions"
authors: "Shuang Wu; Qian Liu; Xin Zhao; Baowen Sun; Xiuwu Liao"
year: "2024"
journal: "Information Systems Journal"
doi: "10.1111/isj.12462"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
RESEARCH ARTICLE

# Attracting solvers' participation in crowdsourcing contests: The role of linguistic signals in task descriptions

Shuang Wu $^{1}$ | Qian Liu $^{2}$ | Xin Zhao $^{3}$ | Baowen Sun $^{2}$ | Xiuwu Liao $^{1}$

$^{1}$ School of Management, Xi'an Jiaotong University, Xi'an, Shaanxi, People's Republic of China

$^{2}$ China Center for Internet Economy Research, Central University of Finance and Economics, Beijing, People's Republic of China

$^{3}$ School of Economics and Management, Xi'an University of Technology, Xi'an, Shaanxi, People's Republic of China

## Correspondence

Qian Liu, China Center for Internet Economy Research, Central University of Finance and Economics, 39 South College Road, Haidian District, Beijing 100081, People's Republic of China.

Email: liuqianlf@cufe.edu.cn

## Funding information

National Natural Science Foundation of China, Grant/Award Numbers: 72172168, 71872149, 71872144; Double First-class construction project of Central University of Finance and Economics

## Abstract

Many companies gain external expertise, lower their costs and generate publicity by using crowdsourcing platforms to complete tasks by leveraging the power of the crowd. However, the number of solvers attracted by crowdsourcing tasks varies widely. Although some well-known crowdsourcing contests have attracted large numbers of participants, many tasks still suffer from low participation rates. Prior research aimed at solving this problem has focused on factors such as task rewards and durations while overlooking whether a well-written description might motivate solvers to choose a task. Based on signalling theory, this study investigates the effect of task descriptions on solvers' participation by focusing on informational and affective linguistic signals. Our model is validated by analysing 13 929 descriptions posted in single-winner tasks on epwk.com, a Chinese competitive crowdsourcing platform. For informational linguistic signals, the results reveal that there are inverted U-shaped relationships between both concreteness and specificity and solver participation, whereas linguistic accuracy has a positive effect on solver participation. For affective linguistic signals, positive emotional words have a positive relationship with solver participation, whereas negative emotional words have the opposite effect. Theoretical and practical implications are discussed.

KEYWORDS

crowdsourcing contests, linguistic signals, solver participation,

task description

## 1 | INTRODUCTION

Crowdsourcing contests are an increasingly important way for companies and institutions to complete creative tasks by leveraging the capabilities of a crowd instead of internal employees or machines (Brabham, 2008). On competitive crowdsourcing platforms, companies or employers can launch tasks, select bids, and issue rewards to the solver who provides the best solution (Brabham, 2008; Howe, 2006; Vukovic, 2009). Solver participation is vital to task success in crowdsourcing contests, as more solvers bring more diverse solutions, thus increasing the chances that at least one solution will be suitable (Boudreau et al., 2011; Terwiesch & Xu, 2008). Moreover, some companies are strongly incentivised to launch contests involving more participants because of their potential to generate publicity and brand awareness (Thorbjørnsen & Supphellen, 2004). The McDonald's ‘Mein Burger’ campaign, recognised as an exemplary use of crowdsourcing, created an online buzz that was converted into the best sales numbers of any McDonald's promotional campaign at the end of 2011, which was especially remarkable considering the low media budget (Awards, 2015).

However, many tasks on crowdsourcing platforms suffer from low solver activity (Stewart et al., 2010), for example, about 20% of the tasks posted on CrowdSPRING attract fewer than 15 solvers (Mo et al., 2018). To alleviate this concern regarding low participation rates, researchers have suggested that appropriate task design in terms of factors such as the setting of rewards and durations can increase solvers' motivation and subsequent participation in crowdsourcing (Goh et al., 2017; Ye & Kankanhalli, 2013). As a core element of the task design, the task description shows an employer's detailed demands, usually in text form (Brabham, 2009; Jian-Gang, 2015; Suri & Watts, 2011). A survey of microtask crowdsourcing found that more than 50% of workers claimed that over 30% of the tasks they completed lacked clarity. Poor, vague task descriptions become a barrier to their participation in microtasks (Gadiraju et al., 2017). While previous research has highlighted the importance of task descriptions by exploring the effect of the length of task descriptions or the number of requirements on solver participation (Jiang et al., 2021; Yang et al., 2009), the comprehensibility of task descriptions has not received full attention, in particular, how linguistic signals embedded in task descriptions operate.

Linguistic signal refers to how a task employer communicates with potential solvers through the task description's linguistic features (Mairesse & Walker, 2011; Vasiloaia, 2009). Regarding the asymmetric information between employers and solvers, signalling theory is used for explaining how one party uses extrinsic cues (signals) to convey information with hidden or limited quality or intent to the other party to facilitate a purchase or exchange (Blankenship & Craig, 2011; Ludwig et al., 2013). Linguistic signals may not necessarily change the content but can influence how both the communicator and the message are perceived (Holtgraves, 2013). Choosing appropriate linguistic features in the task description is critical to crowdsourcing's success, as various linguistic features can enhance signals' understandability and observability, making employers' requirements and intentions more visible by conveying different types of information or affections. Potential solvers use these signals to infer the employer's properties and intentions, thus impacting their cognition and behaviour (Bryden et al., 2013; Gonzales et al., 2010). Although some studies have preliminarily explored the impact of task descriptions' linguistic features on solvers' participation in crowdsourcing contests (Wu et al., 2019; Yang et al., 2021), they have failed to develop a full justification of linguistic features' signalling properties and theoretical effects. To fill this gap, this study explores the following research question:

RQ: How do linguistic signals in task descriptions affect solvers' participation in crowdsourcing contests?

Based on signalling theory, we propose that, in the task description, the employer will convey both informational and affective linguistic signals to potential solvers to attract more participation. Informational attributes can make information more understandable, whereas affective attributes express emotions or feelings, which can enhance observability. Informational linguistic signals can be analysed in terms of information diagnosticity (represented by concreteness and specificity) and linguistic accuracy (represented by textual errors), which in linguistics research describes good and acceptable writing, can reduce information acquisition costs for signal receivers. Affective linguistic signals include both positive and negative emotional words; research shows that they either can trigger or evoke emotional responses in recipients, thus influencing their participation. By building on text mining and empirical analysis, our study suggests that for informational linguistic signals, there are inverted U-shaped relationships between both concreteness and specificity and solver participation, whereas linguistic accuracy has a positive effect on solver participation. For affective linguistic signals, positive emotional words have a positive relationship with solver participation, whereas negative emotional words have the opposite effect.

This study contributes to the literature in the following ways. First, we extend the research on crowdsourcing contests by investigating an under-studied topic: the role of linguistic signals in task descriptions. To our knowledge, our study is the first to explore the influence of task descriptions' linguistic features on solvers' participation in crowdsourcing contests from a signalling theory perspective. Secondly, our research develops the signalling theory by exploring the transmission of linguistic signals from employers to potential solvers, which fills the gap in the discussion of signalling transmission in the crowdsourcing context without the employer's perspective. Our empirical results validate the important role of rhetorical signals—language-based signals, which have been downplayed by traditional signal theory. Third, we propose a new theoretical explanation for the relationship between information diagnosticity and solvers' participation by proposing an inverted U-shaped effect based on uncertainty-related logic. Proposing the curvilinear relationship may solve the controversy of if high-diagnosticity task descriptions contribute to mass participation. Fourth, on the basis of information signals, we further explore the influence of affective signals in task descriptions on solvers' participation, which enrich the existing literature on crowdsourcing participation and lays a foundation for further study of other kinds of affective signals.

The remainder of this paper is organised as follows. The next section provides a literature review. The third section discusses the research model, which elaborates on the influence of linguistic signals in task descriptions on solver participation. Then, we test the hypotheses with data. After testing for robustness in Section 5, the last section discusses implications, limitations and directions for future research.

## 2 | LITERATURE REVIEW

## 2.1 | The crowdsourcing contest and the role of task description

Coined by Howe (2006), ‘crowdsourcing’ is defined as ‘the act of a company or institution taking a function once performed by employees and outsourcing it to an undefined (and generally large) network of people in the form of an open call. The crucial prerequisite is the use of the open call and a large network of potential laborers’. Crowdsourcing contests (or competitive crowdsourcing tasks) are a type of open innovation that can involve a competitive relationship among solvers participating in the same tasks (Di Gangi et al., 2010; Kohli & Melville, 2019; Terwiesch & Xu, 2008). Companies (i.e. employers) offer tasks on crowdsourcing platforms, and potential solvers choose whether to participate in them based on their considerations. If solvers choose to tackle a task, they use their professional knowledge and skills to provide the employer with creative and efficient solutions (Bayus, 2013; Pedersen et al., 2013; Zhao & Zhu, 2014). Based on the employer's evaluation, they may win the crowdsourcing contest and receive a reward for their time and effort (Archak, 2010; Terwiesch & Xu, 2008). Many companies save time, human resources, and money by gathering creative solutions to their problems through crowdsourcing platforms (Brabham, 2008; Liu et al., 2020; Vukovic, 2009).

The commercial value of crowdsourcing contests has prompted practitioners and researchers to look into factors affecting crowdsourcing performance, such as solver participation (Javadi Khasraghi & Aghaie, 2014; Sun et al., 2011; Walter & Back, 2011). Yang et al. (2009) suggested that a larger population of solvers generates more diverse ideas, that is the chance of better ideas being generated increases as the number of solvers grows. Thus, the more solvers in a competitive crowdsourcing task, the more likely it is to be successful. Previous research found that solvers' participation is mainly affected by three types of factors: task-design factors (e.g. rewards, task specificity, contest duration, task type, and description length; see (Boudreau et al., 2011; Walter & Back, 2011; Yang et al., 2009), individual-level factors (e.g. solvers' motivation, employers' brand strength; see (Daugherty et al., 2005; Nov et al., 2009; Taylor & Joshi, 2019; Walter & Back, 2011), and environmental factors (e.g. task density, competition intensity (Shao et al., 2012; Yang et al., 2010; see Table 1).

Although much research has been conducted on solver participation, the role of task descriptions has yet to be adequately considered. On competitive crowdsourcing platforms, the task description is a detailed introduction to the task. Sun et al. (2011) proposed that companies (or employers) should describe their crowdsourcing tasks clearly at the beginning to increase the number of solvers. Based on the switching cost theory, Yang et al. (2009) found that longer descriptions increase learning costs, thus reducing solvers' participation. Jiang et al. (2021) found that, with more conceptual objectives disclosed in the problem specification, contest participants eventually decreased. Moreover, Walter and Back (2011) failed to find that task description length has a significant effect. Chen et al. (2021) controlled for task description length as an indicator of project scale and also found no significant effect on the number of solvers. Wu et al. (2019) and Yang et al. (2021) conducted preliminary discussions on task descriptions' linguistic features and found that they played an essential role in influencing solvers' participation. Regrettably, these two studies did not fully demonstrate the theoretical logic of linguistic features' effect, lacking unified theoretical guidance on variable selection and hypotheses construction. Therefore, we aim to fill this gap by analysing the properties, classifications, effects, and theoretical logic behind the linguistic features in task descriptions from a signalling theory perspective.

## 2.2 | Receiver perception of linguistic cues

Linguistic cues can provide us with essential clues that indicate people's attentional focus, emotionality, social relationships, thinking styles, and personal characteristics, among others (Abe, 2011; Toma & D'Angelo, 2014). For example, the use of personal pronouns can reveal people's implicit intentions or statues (Hancock et al., 2007; Rude et al., 2004; Simmons et al., 2005). People experiencing physical or emotional pain tend to pay more attention to themselves and their situations and thus tend to use singular first-person pronouns more often (Rude et al., 2004). When interviewers asked married couples to evaluate their marriages, more frequent use of the pronoun 'we' by the subjects indicated a better marital status (Simmons et al., 2005). Linguistic cues can also be utilised by perceivers when processing and interpreting information (Larrimore et al., 2011; Rodriguez et al., 2010; Toma & D'Angelo, 2014). Engaging with and comprehending verbal communication is linked to a range of favourable results, including improved salesperson effectiveness, enhanced relationship dynamics, and increased customer contentment (Packard & Berger, 2021). Linguistic cues facilitate both the recipient's comprehension of the message content and the inference of the speaker's hidden state, aiding decision-making on how to respond. For instance, Parhankangas and Renko (2017) examined the relationship between language use and crowdfunding success, proving that entrepreneurs can optimise their persuasiveness by employing appropriate linguistic styles which can help overcome communication challenges and establish a closer connection with the audience. Toma and D'Angelo (2014) analysed how perceivers use linguistic cues to assess the expertise of online medical advice. Without knowing the messages' authors, the perceivers could still discern between messages written by doctors and those written by laypersons.

Utilising words as implicit behavioural indicators can help avoid many reaction biases or social approbation problems commonly faced in studies using self-responsive questionnaires (Pennebaker et al., 2003). Examining the use of such words can provide cues for psychological analyses and serve as valid behavioural indicators for psychological constructs in studying psychological mechanisms (Pennebaker & Lay, 2002). In the study of Parhankangas and Renko (2017), concrete language (measured by articles, prepositions, and quantifiers), precise language (measured by Johnson's type-token ratio), interactive style (measured by questions), and psychological distance (measured by first-person pronouns and negative emotion words) in a project description will affect crowdfunding success. Also in the crowdfunding context, Gorbatai and Nelson (2015) controlled for three compositional characteristics in their model to capture the holistic qualities of the description text: lexical diversity, readability, and concreteness, which are measured by type-token ratio, McLaughlin's SMOG formula, and length of the path to the root word, respectively. Although well-researched in areas such as crowdfunding, P2P and online reviews, as mentioned in the previous section, linguistic cues in the crowdsourcing context are still poorly studied. Following these studies, we analyse the textual forms participants perceive when reading task descriptions in crowdsourcing contests. Task descriptions' linguistic factors may contain meaningful information and serve as linguistic signals promoting communication between employers and potential solvers.

TABLE 1 Factors influencing crowdsourcing participation.

<table><tr><td>Group</td><td>Variable</td><td>Definition</td><td>Effect</td><td>Related works</td></tr><tr><td rowspan="3">Task Design</td><td>Reward</td><td>Amount of money to be awarded to the author of the winning work in the contest</td><td>Positive</td><td>Archak (2010); Boudreau et al. (2011); Yang et al. (2008)</td></tr><tr><td>Task duration</td><td>Length of time allowed to finish a task</td><td>Positive</td><td>DiPalantino and Vojnovic (2009); Walter and Back (2011); Yang et al. (2009)</td></tr><tr><td>Task specificity</td><td>Skill level necessary to submit a work to a contest</td><td>Negative</td><td>Walter and Back (2011)</td></tr><tr><td rowspan="2">Individual factors</td><td>Solver dimensions</td><td>For exampleExtrinsic factorsIntrinsic factors</td><td>PositivePositive</td><td>Chiu et al. (2006); Daugherty et al. (2005); Nov et al. (2009)</td></tr><tr><td>Employer dimensions</td><td>For exampleBrand strength</td><td>Positive</td><td>Walter and Back (2011)</td></tr><tr><td rowspan="3">Environmental factors</td><td>Task density</td><td>Number of other tasks in the same category within a certain number of days</td><td>Negative</td><td>Shao et al. (2012)</td></tr><tr><td>Market price</td><td>The average price of other competing tasks during the same period</td><td>Positive/ No significant effect</td><td>Shao et al. (2012); Yang et al. (2010)</td></tr><tr><td>Competition intensity</td><td>Solvers&#x27; perception of the probability of winning. Operationalised by the number of solvers and the experience that solvers bring to the competition</td><td>Negative</td><td>Liu et al. (2011); Yang et al. (2010)</td></tr><tr><td colspan="5">A specific table for task description and participation</td></tr><tr><td rowspan="2">Task description</td><td>Task description (length/number of requirements)</td><td>The number of words used to describe the task in a contestThe number of solution criteria, technical requirements, conceptual objectives, or execution guidelines</td><td>NegativeNo significant effect</td><td>Jiang et al. (2021); Yang et al. (2009)Jiang et al. (2021); Pollok et al. (2019); Walter and Back (2011)</td></tr><tr><td>Task description (linguistic features)</td><td>For exampleSelf-distancingCognitive complexity CausalityTentative language</td><td>Positive or Negative</td><td>Wu et al. (2019); Yang et al. (2021)</td></tr></table>

## 2.3 | Theoretical foundation: Signalling theory

Signalling theory, first proposed by Spence (1978), studies how, in a case of information asymmetry, the signal sender, who has an information advantage, can effectively transmit information to the signal receiver, who has an information disadvantage, through 'signal transmission' to realise market equilibrium (Wells et al., 2011). Based on asymmetric information between two parties in a transaction, signalling theory provides a framework for explaining how a signaller uses extrinsic cues (signals) to convey information with hidden or limited quality or intent to the receivers to facilitate a purchase or exchange (Blankenship & Craig, 2011; Ludwig et al., 2013). Although the information asymmetry in crowdsourcing exists between both sides, the employers and the solvers, in literature, the application of signalling theory in the crowdsourcing context was often reflected in how the solver serves as a signaller sending signals to the employer, for example, Durward et al. (2016) shows that quality signals of crowdworkers increase the bargaining power toward crowdsourcers. Piazza et al. (2022) found that solvers can signal their quality attributes through online profiles and the discussion blog of the crowdsourcing platform to improve their chances of winning crowdsourcing contests. Little literature systematically discusses how employers actively signal their intentions by task descriptions to reduce information asymmetry and attract participation. Employers are incentivised to show their real needs and intentions because doing so will make them more likely to get solutions matching their desires. Especially given that the prime communication signal between individuals who do not always have access to the same information is textual, the efficiency of transmission of signals relies more on the signals being accurately sent, observed and understood (Wang et al., 2022). Traditional signalling theory has always downplayed the impact of rhetorical signals (relevant, language-based information) (Bergh et al., 2014; Farrell & Rabin, 1996). The discord between established management research and signalling theory's assessment of rhetoric hampers the development of signalling theory (Steigenberger, 2017). Recent developments in the signalling theory have showcased rhetoric being operationalised as a signal (Anglin et al., 2018; Steigenberger & Wilhelm, 2018), wherein signalers indicate underlying qualities or intentions via text. Those studies provide a basis for using signalling theory as theoretical foundation to analyse linguistic features and suggests that choosing appropriate linguistic features in the task description is critical to a crowdsourcing venture's success, as various linguistic features can enhance the observation and understanding of signals, thus making employers' requirements and intentions more visible.

Signals can be divided into different types according to different dimensions. Studying the classification of signals can deepen the understanding of the relationship between different signals (Kirmani & Rao, 2000). Table 2 summarises some signal classification methods in the literature. Internal and external emphasise the source of the signal (Mavlanova et al., 2016); online and offline distinguish signal transmission channels (Li, Tang, et al., 2019); textual and image-based distinguish the presentation of signals (Fan & Zhang, 2020); objective and subjective distinguish between objective facts and subjective feelings (Wang et al., 2021). The task description in crowdsourcing is an internally generated online textual description of an employer's subjective requirements, which means that the above distinction is unsuitable. Informational and affective signals emphasise the information and emotions conveyed by the text content, which fits more closely with the textual characteristics of task descriptions (Chen et al., 2020). Based on previous studies, we propose that when two types of linguistic signals—informational and affective linguistic signals—are embedded in crowdsourcing task descriptions, they may also affect potential solvers' participation.

TABLE 2 Several studies related to signal classification.

<table><tr><td>Studies</td><td>Context</td><td>Classification</td><td>Definition</td><td>Findings</td></tr><tr><td rowspan="2">Mavlanova et al. (2016)</td><td rowspan="2">E-commerce</td><td>Internal signals</td><td>Arise as a consequence of the seller&#x27;s internal decision to project a specific image or communicate a specific company policy, e.g. the privacy or return policy display.</td><td rowspan="2">The results suggest that external and internal signals, if believable, have a significant effect on buyer perceptions; buyers find external signals more salient than internal ones.</td></tr><tr><td>External signals</td><td>Are those that imply an endorsement from a third party, e.g. third-party verification seals</td></tr><tr><td rowspan="2">Li, Tang, et al. (2019)</td><td rowspan="2">E-consultation</td><td>Online signals</td><td>Online knowledge contribution (seller signals) and online reputation (market signals)</td><td rowspan="2">The two types of online signals are substitutes for each other; the impacts of knowledge contribution and reputation obtained from the website were negatively moderated by the offline signals (status).</td></tr><tr><td>Offline signals</td><td>Offline status, e.g. a physician&#x27;s position (i.e. chief physician or associate chief physician) in the offline hospital</td></tr><tr><td rowspan="2">Fan and Zhang (2020)</td><td rowspan="2">Mobile phone selling</td><td>Textual signal</td><td>The text contains a more detailed description of product attributes, contributing to the diagnosticity of reviews.</td><td rowspan="2">Both signal types positively impact review helpfulness, while their interaction has a negative influence. The signalling environment enhances the effect of textual signals and mitigates the negative impact of signal interaction on review helpfulness.</td></tr><tr><td>Imagery signal</td><td>Images are visually more attention-grabbing on the screen, contributing to the accessibility of reviews.</td></tr><tr><td rowspan="2">Chen et al. (2020)</td><td rowspan="2">Online health communities</td><td>Informational signal</td><td>Linguistic features allow more efficient information processing by potential support-givers in the communities.</td><td rowspan="2">Affective linguistic signals effectively evoke informational and emotional support from the community. Informative signals, including readability, post length, and spelling, positively associate with support receipt, while readability and spelling also evoke emotional support.</td></tr><tr><td>Affective signal</td><td>Linguistic features of OHC posts provide heuristic cues for motivating greater social support exchange in the community through emotion-invoking linguistic mechanisms.</td></tr><tr><td rowspan="2">Wang et al. (2021)</td><td rowspan="2">Crowdfunding</td><td>Objective narratives</td><td>It can be viewed as a factual state of reality and a ‘correspondence, grounded in correctness, between thought and reality’.</td><td rowspan="2">To court investors, the title, detailed textual description, and biography should be phrased subjectively. For the detailed textual description, the objective contents should be positioned at the start of the narrative, followed by the subjective statements, to enhance the success of online fundraising.</td></tr><tr><td>Subjective narratives</td><td>The collection of emotions, perceptions, experiences, expectations, evaluations, and personal or cultural understandings of and beliefs about an external phenomenon specific to a subject</td></tr></table>

## 3 | RESEARCH MODEL AND HYPOTHESES

## 3.1 | Research model

People have limited insight into each other's feelings, goals, needs, desires, and social intentions. This lack of information is a source of challenges in social activities. Therefore, people may use each other's informational and emotional expressions to understand ambiguous social situations (Manstead & Fischer, 2001; Van Kleef, De Dreu, & Manstead, 2010b). Informational and affective attributes are the two main attributes embedded in online content (Denecke & Nejdl, 2009; Ni et al., 2007). Informational attributes can disclose highly accurate information to reduce information asymmetry between two communicating parties (Montiel et al., 2012), whereas affective attributes express emotions or feelings (Denecke & Nejdl, 2009). For example, Xiang et al. (2019) summarised how crowdfunding entrepreneurs leverage the power of messages to attract as many backers as possible, using cognitive (e.g. project characteristic signals) and affective (e.g. entrepreneurial passion) communication techniques.

This phenomenon also exists in the crowdsourcing context; crowdsourced task participation can be regarded as a social exchange process (Ye & Kankanhalli, 2017). On one hand, potential solvers will pay attention to informational linguistic signals in the task description to help them understand the task requirements and measure the probability of completing their work and receiving benefits from this (Steigenberger & Wilhelm, 2018). On the other hand, Lawler and Thye (1999) regard emotion as an important signal displayed to exchange participants: the trust, kindness and affection conveyed by affective signals may also affect the willingness of potential solvers to participate. As shown in Figure 1, our research model uses signalling theory to interpret how informational and affective linguistic signals in crowdsourcing contest task descriptions can help employers convey task requirements and intentions to attract more participants.

![](/api/attachments/VN2Z443D/fulltext/images/e1fea5903897bbe07c0a2f0fe406140ce96ebf284b08775178f97c4b350e163c.jpg)  
FIGURE 1 Research model.

## 3.2 | Hypotheses

## 3.2.1 | Informational linguistic signals

Research in linguistics has shown that in many writing contexts, performance errors and a lack of explicitness at the level of meaning and content are frequent and will rarely go unnoticed; thus, they may influence the success of communication (Connor et al., 1995). Likewise, Hynninen and Kuteeva (2017) described good and acceptable writing as having two linguistic properties: ‘clarity’ of expression and ‘correct’ linguistic form. Based on their research, our study designs a similar classification, using the concept of information diagnosticity to describe how task descriptions provide ‘clarity’ of expression—thus contributing to the informed decision-making process of potential solvers in determining participation intentions—and using linguistic accuracy to describe the ‘correct’ linguistic form. When these linguistic features are embedded and highlighted, they may affect potential solvers' understanding of the employer's task requirements and the cognitive effort required to process the relevant information (Chen et al., 2020). From a signalling theory perspective, informational linguistic signals can enhance the understandability of signals sent by employers (Chen et al., 2020; Chua & Banerjee, 2016).

## Information diagnosticity and solver participation

Information diagnosticity is defined as the extent to which a given piece of information discriminates between alternative hypotheses, interpretations or categorizations, thus helping reduce uncertainty and improve understanding or knowledge about an object (like a product) (Evers & Lakens, 2014; Filieri, 2015; Herr et al., 1991). In the crowdsourcing context, we adapt and adjust the expansive classification of information diagnosticity proposed by Weathers et al. (2015), suggesting that information diagnosticity means that the text should be careful not to lack any information, as well as reduce equivocality. Thus, we represent these two aspects of information diagnosticity in terms of concreteness and specificity. Concreteness refers to a type of linguistic style closely related to more contextual information and detailed representations that enables readers to process the message faster and more efficiently, thus facilitating the understandability of the information and hence more effectively reducing uncertainty (Markowitz & Hancock, 2016; Paivio, 1986, 1991; Ter Doest et al., 2002). In addition, specificity means descriptions are more specific and precise in expressing complex thinking (Hancock et al., 2007), inhibitions (Creswell et al., 2007) and categorization (Abe, 2011), thus potentially reducing ambiguity or the plausibility of multiple interpretations, which can lead to uncertainty and inaction (Daft & Lengel, 1986; Daft & Macintosh, 1981).

However, there is still limited agreement if concrete and specific task descriptions contribute to mass participation. On one hand, lacking clarity impacts workers' acceptance of a task and decreases the number of participants (Gadiraju et al., 2017; Schulze et al., 2011). On the other hand, tasks without constraints lead to a higher quantity of brainstorming ideas (Paulus et al., 2011). A high level of contest autonomy may enhance the solver's intrinsic motivation to participate (Zheng et al., 2011). These inconclusive findings indicate that the relationship between diagnostic information and solvers' participation may not be linear. In a contest, if the task description cannot provide any concrete or specific information, the potential solvers may lack enough understanding of the employer's requirements. Additionally, they will also doubt the employer's reliability on whether they have consistent and objective criteria to select the winning work. At this point, the potential solvers are in a highly uncertain state. Based on uncertainty reduction theory, uncertainty denotes an individual's mental state of uncertainty when they are unable to make a specific and clear identification and evaluation of their own psychology and behaviour (Berger & Calabrese, 1974). It encourages an individual to change their current situation by seeking information to acquire knowledge in order to achieve a psychological sense of certainty. Thus, potential solvers are motivated to participate in other tasks with more concrete and specific requirements to lower their level of uncertainty. For example, in a logo design task with high concreteness and specificity, an employer may provide suggestions regarding the features they want, such as the type of colour, shape (e.g. a red triangle mark), format (in jpg or png format), design elements (e.g. three circles), and specific restrictions (e.g. 'The elements should not be represented by text, but you can use symbols or patterns. No strong colors'). If the seeker provides these execution guidelines, this will save designers from spending time and effort determining such details (Jiang et al., 2021). Moreover, concrete and specific expressions can convey a sense of expertise (Toma & D'Angelo, 2014). Potential participants will perceive that the employer has a clear understanding of their own needs and may possess a certain level of knowledge in the relevant field. In such cases, as long as they adhere to the requirements, there is a high probability of achieving a result that aligns with the employer's needs. Therefore, the information diagnosticity of the task description is positively correlated with the number of solvers attracted by the task.

Nonetheless, more diagnostic information in a task description is not necessarily better. Although uncertainty is always assumed to be aversive, theories based on uncertainty reduction often overlook the opportunities arising from uncertainty creation (McMullen & Shepherd, 2006; Shen et al., 2015; Smith & Lewis, 2011). Griffin and Grote (2020) claimed an inverted U-shaped function exists between an individual's experience of uncertainty and the level of uncertainty preferred in a particular situation, such as fulfilling a specific work task. When low levels of uncertainty are experienced, individuals are motivated to increase uncertainty. Conversely, when high levels of uncertainty are experienced, motivation to reduce uncertainty is likely. When employers' task requirements are too concrete or specific, potential solvers face very low uncertainty about employers' demands. However, most tasks in crowdsourcing competitions are creative in nature, meaning that solvers are given free rein, which can lead to parallel effects and increase the diversity of solutions (Boudreau et al., 2011). This kind of working freedom for solvers is reflected in their sense of job autonomy (Hackman & Oldham, 1976). According to job characteristics theory, when solvers are more autonomous, they will be more interested in their tasks and enjoy performing them more (Garcia Martinez, 2015; Morgeson & Humphrey, 2006). On the contrary, a more detailed specification may generate more constraints without creating more value for the employer and requires solvers to carry out more targeted work, increasing the cost of effort and limiting original work habits, thus decreasing potential solvers' creativity and proactivity (Baxter et al., 2008; Erat & Krishnan, 2012; Ohly et al., 2006). In this case, potential solvers begin to seek out tasks with higher uncertainty to explore more possibilities and have more autonomy, and the positive role of information diagnosticity diminishes. Therefore, we assume the following:

H1. In competitive crowdsourcing tasks, there is an inverted U-shaped relationship between the concreteness of the task description and the solvers' participation.

H2. In competitive crowdsourcing tasks, there is an inverted U-shaped relationship between the specificity of the task description and the solvers' participation.

## Linguistic accuracy and solver participation

In addition, our study focuses on a particular informational signal, linguistic accuracy (also called linguistic correctness), which is determined 'by the number of errors, whether in spelling, punctuation, semantics, or grammar per 100 words' (Shuqiang, 1987). When such errors appear, the task description's linguistic accuracy is reduced (Xie, 2019). We put it alongside the concept of information diagnosticity because we believe that a few punctuational or grammatical and spelling errors should not really change the meaning of an employer's needs. However, studies in many other contexts have shown that a text with spelling and grammatical errors may undermine people's reading comfort and slow their reading speed (Connor et al., 1995; Pengnate & Riggins, 2020). According to cognitive load theory, the number of errors in a text can overwhelm readers' cognitive effort to absorb information, negatively influencing the readers' perceptions (Petty et al., 1980). Research has investigated how spelling errors affect customer attitudes and responses. For example, punctuational errors and typos indicating low conformance to common writing practices are reported to reduce readers' perceived quality of social media content (Agichtein et al., 2008). In online reviews, previous studies have suggested that the number of spelling errors is considered one of the peripheral text features that can impact review helpfulness (Ghose & Ipeirotis, 2010; Srivastava & Kalro, 2019). Since accuracy and errors can be regarded as two sides of the same coin, we assume the following:

H3. In competitive crowdsourcing tasks, linguistic accuracy is positively related to solvers' participation.

## 3.2.2 | Affective linguistic signals

Psycholinguistic research on the effect of language suggests that language has the power to shape emotions (Blankenship & Craig, 2011; Lindquist & Gendron, 2013) and to shape preferences during decision-making (Van Kleef, 2010; Van Kleef, De Dreu, et al., 2010; Van Kleef et al., 2006). Research has demonstrated that readers can easily perceive and differentiate emotional words (Barrett, 2007), which are processed faster and more efficiently than non-emotional ones or even automatically (Gendron et al., 2012; Kousta et al., 2009). Accordingly, emotional content is easily recognised and can be regarded as a signal for social functions because of its high epistemic motivation, producing interpersonal consequences (Van Kleef, Anastasopoulou, & Nijstad, 2010a). Thus, emotional words can serve as affective linguistic signals that can influence the signal observer by triggering an emotional response (Maaravi et al., 2019; Wang et al., 2020; Yang et al., 2023). Evidence from previous studies that use experimental manipulations to prime affective states suggests that exposure to affective cues influences evaluations and judgements of attitude objects, such as brands and products: Positive (negative) affective cues lead to more positive (negative) evaluations and judgements (e.g. Lau-Gesk & Meyers-Levy, 2009).

This assessment is also applicable in the crowdsourcing context. Some employers share the task background and requirements in crowdsourcing task descriptions positively and passionately. For example, they can explain their business positively: 'Our company has international leading technology, first-class R&D ability, an excellent team, has applied for and obtained many national invention patents, and maintains good cooperation with many universities'. These kinds of descriptions can generate positive psychological capital, which refers to the existence of hope, optimism, resilience, and confidence in a person or organisation (Anglin et al., 2018; McKenny et al., 2013). The positive psychology literature suggests that this kind of capital can improve company performance and provide a competitive advantage (Luthans & Youssef, 2004). Signalling theory applied at the organisational level often focuses on the 'intentional communication of positive information to convey positive organizational attributes' (Connelly et al., 2011). Past studies have indicated that participants often seek employers with higher brand strength, which may reflect higher levels of credibility (Kim et al., 2008; Walter & Back, 2011). Moreover, studies have shown that the induction of positive emotions can produce mutual well-being and positive impressions conducive to interpersonal interaction, promote cooperation and improve the quality of agreements (Kopelman et al., 2006). In sum, in crowdsourcing task descriptions, positive emotions can convey a positive image of the employer, promote a feeling of pleasure and trust in potential solvers, and thus promote participation.

Correspondingly, in some task descriptions, some employers use words associated with negative emotions, especially words related to anxiety and dissatisfaction, to describe their challenges (especially challenges that can be overcome by the crowd's participation in the task), thus revealing their vulnerability (Davis & Brock, 1975; Toma & D'Angelo, 2014). For example, when posting an interior design task, an employer may write, 'I am distraught; the designer we hired before was terrible and wasted our time—I need a design for a Chinese-style reception hall within three days. Hurry! Hurry! Hurry!' Crowdsourcing contests differ from traditional social support behaviours like asking for help; the employer chooses the best solution from a large pool of solver contributions and offers the reward. From this bargaining position, potential participants may hope employers can choose the best work carefully. The emphasis on anxiety and urgency in task descriptions tends to make potential participants feel that employers are likely to pick winners from earlier submissions as quickly as possible rather than carefully evaluating all submissions, thus reducing the employer's credibility (Parhankangas & Renko, 2017). Moreover, expressing negative emotions may also trigger a bad mood and negative impressions, undermining cooperative social communication (Dickert et al., 2011; Dickert & Slovic, 2009; Kogut & Ritov, 2005). Thus, we assume the following:

H4. In competitive crowdsourcing tasks, positive emotional words are positively related to solvers' participation.

H5. In competitive crowdsourcing tasks, negative emotional words are negatively related to solvers' participation.

## 4 | DATA

## 4.1 | Sample

This study investigated a large-scale dataset of real-world crowdsourcing contests conducted online. The data were collected from epwk.com, a major Chinese crowdsourcing platform. Established on 1 July 2010, epwk.com is a professional e-commerce platform for trading creative products and services. It is a communication platform for solving scientific, technological, living, and learning problems through the internet and has become a leading brand among the new Chinese crowdsourcing websites. The website includes more than 10 categories of reward tasks, such as logo design, naming services, advertising, creative writing, and program planning. The website also combines various crowdsourcing modes, such as pricing, hiring and bidding. On this platform, employers can start a task with an award deposit. Solvers first browse the task list to receive information such as the task title, type, reward, and duration. They then select a task that interests them and click to see the Task Details page, where they can read the task description information (in the hiring mode, solvers can only view a brief description unless they are hired) and decide whether to participate. According to data provided by the website, by 2019, there were more than 20 million registered users, and the total value of transactions conducted was close to RMB 2 billion. The website and an example of a task are presented in the Appendix A.

The study collected tasks published from July 2012 to July 2019. For the following reasons, only single-winner tasks were selected for analysis. First, this study focused on competitive crowdsourcing and did not examine tasks that used the piece-counting or hiring modes. In the piece-counting mode, anyone can participate in the task; as long as the work submitted meets the requirements, the solvers receive a bounty based on the number of pieces. Second, in the hiring mode, the solvers recommend themselves to employers, or employers hire a solver directly. After the employment relationship is established, the requirements are elaborated on (usually privately), meaning that the impact of the task description on participation is difficult to assess. Third, in the multi-person bid-winning mode, the employer does not set the number of bid-winning persons in advance, and the participants do not know the employer's expected adoption number, which increases the randomness. In total, approximately 17 000 single-winner contest projects were collected. After eliminating some tasks with incomplete data, the total sample data for the study is 13 929 contests published by 9754 employers. The average cumulative number of published tasks per employer was 20.8. Table 3 provides the annual release of tasks.

## 4.2 | Variable measurements

## 4.2.1 | Dependent variable

The dependent variable, solver participation in a crowdsourcing contest, can be measured by the number of solvers submitting bids. The website also displays the number of submissions for a given task, which indicates the total number of submissions received, including multiple submissions by the same solver. However, some solvers upload multiple submissions for one task, and the resubmitted works may contain only a few or meaningless changes. Because this study focuses on measuring solver participation in the context of psychology, the number of solvers is selected as the variable measuring participation. Given the skew of the dependent variable, we apply a natural log transformation to the number of solvers.

TABLE 3 Single-winner task publication.

<table><tr><td>Year</td><td>Freq.</td><td>Percent</td></tr><tr><td>2012</td><td>326</td><td>2.34</td></tr><tr><td>2013</td><td>1428</td><td>10.25</td></tr><tr><td>2014</td><td>1302</td><td>9.35</td></tr><tr><td>2015</td><td>1936</td><td>13.90</td></tr><tr><td>2016</td><td>2135</td><td>15.33</td></tr><tr><td>2017</td><td>3004</td><td>21.57</td></tr><tr><td>2018</td><td>2573</td><td>18.47</td></tr><tr><td>2019</td><td>1225</td><td>8.79</td></tr><tr><td>Total</td><td>13 929</td><td>100.00</td></tr></table>

## 4.2.2 | Independent variables

Concreteness can be defined as the ‘degree to which the concept denoted by a word refers to a perceptible entity’ (Brysbaert et al., 2014). The operationalization of concreteness by using the number of articles (e.g. a, an, the), prepositions (e.g. at, on, in), and quantifiers (e.g. a lot, many) in a text has been widely used in literature (Markowitz & Hancock, 2016; Parhankangas & Renko, 2017). These words signal concreteness because concrete words ‘are associated with more contextualised and detailed representations of objects’ (Larrimore et al., 2011). Specifically, articles signal an upcoming concrete object, prepositions specify relationships between objects and people, and quantifiers express degrees of difference between objects. Their functions are considered in line with the definition above of concreteness (Elliott et al., 2015; Larrimore et al., 2011; Tausczik & Pennebaker, 2010).

Requirement specificity describes how this style can reduce ambiguity or the plausibility of multiple interpretations in a task requirement. Similar to goal specificity in goal-setting theory, increasing the specificity of a goal increases the consensus regarding the interpretation of that goal (Klein et al., 1990). As specificity increases, room for interpretation decreases, as does the number of outcomes consistent with the requirement. To measure this concept from a linguistic perspective, we refer to the study of (Pennebaker & King, 1999), which factor-analysed word-use dimensions and extracted four principal components, one of them is labelled ‘making distinctions’, including word categories such as discrepancies, exclusionary words, and negations. Those words can help speakers to categorise different choices, thus helping reduce ambiguity. Specifically, drawn from literature, exclusive words (e.g. ‘but’, ‘except’, ‘without’, and ‘exclude’) are the language used when people are trying to differentiate a concept from another concept (Mehl & Pennebaker, 2003; Oliver et al., 2008; Pennebaker et al., 2003), for example, ‘I’d like to order the egg rolls but without bean sprout’. The words but and without are making a finer distinction than just ordering egg rolls. Similarly, negations (e.g. ‘no’, ‘never’, ‘not’) also serve as the inhibition and distinction markers, helping the expression to be more specific and precise (Creswell et al., 2007; Hancock et al., 2007; Handelman & Lester, 2007). Then, for discrepancies words (most of the words are modals like ‘should’, ‘ought’, ‘must’, also have some words like ‘prefer’, ‘rather’), it can describe the discrepancies seeking process (Beevers & Scott, 2001), giving explicit indications of the tense, mood, or voice of another verb (Taylor & Thomas, 2008), and indicating the speakers’ degree of certainty about their statement (Li, Pham, & Chuang, 2019a). This word category can be used to convey commands (Brett et al., 2007), tell someone else what they should be doing, and convey the expectation that the recipient will comply with the directive (Pennebaker et al., 2003).

In summary, linguistic cues associated with concreteness primarily serve the purpose of providing solvers with detailed and contextual information, which facilitates better understanding. On the other hand, linguistic cues linked to specificity emphasise the distinguishing attributes, reflecting the employer's inclination or reluctance attitudes toward such details and reducing ambiguity. It is notably that, the use of a word category is only probabilistically associated with a psychological meaning (Tausczik & Pennebaker, 2010). In the measurement of concreteness and specificity, given that certain words can fall into multiple categories, it is inevitable that they may appear in the measurement of different variables simultaneously (Toma & D'Angelo, 2014). However, based on probability rules, the greater the occurrence of words within the categories related to a specific variable, the higher the probability of reflecting the psychological constructs associated with that variable.

We analysed these independent variable indicators and positive and negative emotional words using the Linguistic Inquiry and Word Count (LIWC) 2015 software. LIWC can be used instead of a professional grader to analyse texts—it uses natural language processing to quantify the content of a given text and calculate the different types of words used therein. The current version contains language variables such as language categories (e.g. personal pronouns, auxiliary verbs, conjunctions, and prepositions), psychological categories (e.g. social process words, emotional process words, cognitive process words, and physiological process words), individual categories (e.g. work, leisure, family, and money), categories for paralinguistic terms (e.g. appropriate words, pause words, and filled verbs), and punctuation categories (e.g. periods, commas, colons, and semicolons). This version of LIWC has 90 word categories, covering approximately 6400 words, and has a new Chinese language processing function unavailable in past versions. Python code using the JieBa segmentation package was written to perform Chinese word segmentation on each description text. The LIWC program then processed each task description separately, producing an output indicating the word frequency for each category. However, given the fundamental differences between the Chinese and English languages (Chinese does not have the concept of an article), we used a category unique to the Chinese dictionary: special article words (specArt). Furthermore, we employed google translation API to convert the task text into English using a standardised criterion and then rectify any deviations caused by the omission of word categories due to differences between the Chinese and English languages, ensuring the consistency of the involved word categories. Finally, we present a short table summarising the findings of the word categories associated with our independent variables from a large group of studies (see Table 4).

For the measurement of linguistic accuracy, the IFlyTEK textual error correction API is used to realise error recognition in task descriptions. The error types identified include errors in spelling, grammar, punctuation, and other problems in the text. We also used manual verification to ensure accuracy.

## Control variables

This study follows previous studies on comparable online contests and controls for several factors associated with crowdsourcing success. These control variables are divided into four major categories: task design elements, task release strategies, employer information, and environmental factors. Task design elements represent the task reward amount, duration (in days), number of attachments, number of demand complements, number of alternatives, task title length, task description length (i.e. number of Chinese characters), the frequency of content words, and task background. The length of a task description represents another important piece of language information. As such, controlling for the length of task descriptions can highlight the importance of other linguistic variables. In addition, the frequency of content words is added as the textual indicator of requirements. Moreover, if the description has task background information is controlled to eliminate the influence of non-task-related information.

The task release strategies show whether markers such as ‘urgent demand’, ‘price-increasing’, and ‘bid-hidden’ are associated with the tasks. Employer information includes the employer's experience level, VIP level, and whether they have passed real-name authentication. Environmental factors include task density and market price. Further, to rule out the impact of time, we control for the release time of the tasks by generating and using dummy year and dummy month variables.

<table><tr><td colspan="6">TABLE 4 Summary table linking LIWC word categories to published research studies.</td></tr><tr><td>Variables</td><td>Indicators</td><td>Examples</td><td>Words in category</td><td>Psychological correlates</td><td>Related literature</td></tr><tr><td rowspan="3">Concreteness</td><td>Articles</td><td>A, an, the</td><td>Function words</td><td>Use of concrete nouns, interest in objects and things</td><td>Centerbar et al., 2008; Guastella &amp; Dadds, 2006; Heberlein et al., 2003</td></tr><tr><td>Prepositions</td><td>To, with, above</td><td>Function words</td><td>Concreteness, describing relationships between objects</td><td>Heberlein et al., 2003; Newman et al., 2003; Pennebaker &amp; Lay, 2002</td></tr><tr><td>Quantifiers</td><td>Few, many, much digitals</td><td>Function words</td><td>Use of concreteness provide details regarding situations, objects, and people</td><td>Elliott et al., 2015; Toma &amp; D&#x27;Angelo, 2014; Toma &amp; Hancock, 2012</td></tr><tr><td rowspan="3">Specificity</td><td>Negations</td><td>No, not, never</td><td>Function words</td><td>Inhibition categorization</td><td>Creswell et al., 2007; Hancock et al., 2007; Handelman &amp; Lester, 2007</td></tr><tr><td>Exclusive words</td><td>but, without, exclude</td><td>Function words/cognitive processes</td><td>Cognitive complexity, distinction marker</td><td>Mehl &amp; Pennebaker, 2003; Oliver et al., 2008; Pennebaker et al., 2003</td></tr><tr><td>Discrepancy</td><td>Should, must, could</td><td>Function words/cognitive processes</td><td>Making distinction, command</td><td>Beevers &amp; Scott, 2001; Brett et al., 2007; Li, Pham, &amp; Chuang, 2019; Taylor &amp; Thomas, 2008</td></tr><tr><td rowspan="2">Affective expression</td><td>Positive emotional words</td><td>Love, nice, sweet</td><td>Affective processes</td><td></td><td>Baikie et al., 2006; Bono &amp; Ilies, 2006; Cohen et al., 2008</td></tr><tr><td>Negative emotional words</td><td>Worried, hate, sad</td><td>Affective processes</td><td></td><td>Alvarez-Conrad et al., 2001; Arguello et al., 2006; Bantum &amp; Owen, 2009</td></tr></table>

The number of attentions, representing the number of users who click to access the Task Details page, is also controlled. Only when a potential solver clicks on the details page can they see the task description text and decide whether to participate. It is an important control variable; after introducing the variable, the task description can really play a role, and the model's R square is significantly increased. To deal with the skewness of some independent and control variables and ease the heteroscedasticity of the data, we used logarithmic transformations and square roots transformations (indicated by superscripts a and b) to arrive at distributions more closely approximating the assumption of normality. The descriptive statistics and correlation matrix are presented in Tables 5 and 6.

## 5 | EMPIRICAL METHODOLOGY

## 5.1 | Results

We investigated VIF and correlation coefficients between the independent and control variables to rule out multicollinearity. As Table 7 shows, the correlations are generally moderate or low. A base model including only the control variables was run first (see Table 7, Model 1). In line with past research, most were significantly associated with crowdsourcing participation (Walter & Back, 2011; Yang et al. 2009). In the next step, we investigated whether the variables related to linguistic signals significantly impacted crowdsourcing participation to verify our hypotheses (see Model 2).

Regarding Model 2, the p-value is found to be less than 0.001, and the model explains 55.54% of the variance in the dependent measure ( $R^{2} = 0.5568$ , $R^{2}_{adj} = 0.5554$ ). For informational linguistic signals, textual errors have a negative effect, which consists with our hypothesis. Then, according to the summary by Haans et al. (2016) on the test procedure for an inverted U-shaped relationship, the inverted U-shaped relationship between the independent and dependent variables needs to meet three conditions: (1) The coefficient of the quadratic term of the independent

TABLE 5 Descriptive statistics of the main variables.

<table><tr><td>Variable</td><td>Mean</td><td>Std dev.</td><td>Min</td><td>Max</td><td>Variable</td><td>Mean</td><td>Std dev.</td><td>Min</td><td>Max</td></tr><tr><td>Number of Solvers $^a$ </td><td>3.82</td><td>0.98</td><td>0</td><td>6.92</td><td>Real-name authentication</td><td>0.85</td><td>0.36</td><td>0</td><td>1</td></tr><tr><td>Reward $^a$ </td><td>5.96</td><td>0.81</td><td>3.91</td><td>9.90</td><td>Price-increasing</td><td>0.08</td><td>0.27</td><td>0</td><td>1</td></tr><tr><td>Duration $^a$ </td><td>2.85</td><td>0.96</td><td>0</td><td>6.89</td><td>Bid-hidden</td><td>0.07</td><td>0.26</td><td>0</td><td>1</td></tr><tr><td>Number of attentions $^a$ </td><td>8.16</td><td>0.73</td><td>6.07</td><td>17.64</td><td>Urgent demand</td><td>0.02</td><td>0.13</td><td>0</td><td>1</td></tr><tr><td>Number of attachments $^a$ </td><td>0.22</td><td>0.32</td><td>0</td><td>1.10</td><td>Market Price $^a$ </td><td>6.19</td><td>0.45</td><td>3.91</td><td>8.10</td></tr><tr><td>Number of demand complements $^b$ </td><td>0.22</td><td>0.48</td><td>0</td><td>1.73</td><td>Task Density $^a$ </td><td>1.94</td><td>0.57</td><td>0</td><td>3.14</td></tr><tr><td>Title length $^a$ </td><td>2.40</td><td>0.36</td><td>1.10</td><td>3.97</td><td>Concreteness $^b$ </td><td>2.24</td><td>0.84</td><td>0</td><td>6.71</td></tr><tr><td>Description Length $^a$ </td><td>4.92</td><td>0.92</td><td>0.69</td><td>7.57</td><td>Specificity $^b$ </td><td>0.73</td><td>0.64</td><td>0</td><td>3.91</td></tr><tr><td>Background information</td><td>0.16</td><td>0.37</td><td>0</td><td>1</td><td>Textual Errors $^b$ </td><td>0.05</td><td>0.07</td><td>0</td><td>0.5</td></tr><tr><td>Content words $^b$ </td><td>8.83</td><td>0.42</td><td>6.78</td><td>10</td><td>PosEmo words $^b$ </td><td>1.36</td><td>0.85</td><td>0</td><td>5.22</td></tr><tr><td>Employers&#x27; experience level</td><td>2.29</td><td>1.48</td><td>1</td><td>9</td><td>NegEmo words $^b$ </td><td>0.14</td><td>0.38</td><td>0</td><td>3.16</td></tr><tr><td>Employers&#x27; VIP level</td><td>0.04</td><td>0.26</td><td>0</td><td>3</td><td>Observation Numbers</td><td>13 929</td><td></td><td></td><td></td></tr></table>

$^{a}$ Means the natural logarithmic transformation.  
$^{b}$ Means the square root transformation.

TABLE 6 Correlation matrix.

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td></tr><tr><td>1 Number of solversa</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2 Number of attentionsa</td><td>0.21***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3 Rewarda</td><td>-0.10***</td><td>-0.09***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4 Durationa</td><td>0.24***</td><td>0.11***</td><td>-0.07***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5 Number of attachmentsa</td><td>-0.32***</td><td>-0.08***</td><td>0.20***</td><td>-0.040***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6 Number of demand complementsb</td><td>0.02*</td><td>0.08***</td><td>0.05***</td><td>0.003</td><td>0.140***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7 Urgent demands</td><td>-0.01</td><td>0.17***</td><td>0.03***</td><td>-0.04***</td><td>-0.01*</td><td>0.01</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8 Price-increasing</td><td>0.03***</td><td>0.08***</td><td>0.14***</td><td>0.17***</td><td>0.09***</td><td>0.18***</td><td>-0.04***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9 Bid-hidden</td><td>0.05***</td><td>0.11***</td><td>0.10***</td><td>0.01</td><td>0.004</td><td>0.04***</td><td>-0.04***</td><td>-0.08***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10 Employers&#x27; experience level</td><td>-0.02*</td><td>-0.07***</td><td>0.33***</td><td>0.02**</td><td>0.14***</td><td>0.04***</td><td>-0.02**</td><td>0.09***</td><td>0.02**</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>11 Real-name authentications</td><td>-0.02*</td><td>0.04***</td><td>-0.01</td><td>-0.05***</td><td>-0.03***</td><td>-0.02***</td><td>0.03***</td><td>-0.01</td><td>0.03***</td><td>-0.01</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>12 Employers&#x27; VIP level</td><td>0.06***</td><td>-0.04***</td><td>0.11***</td><td>-0.03***</td><td>-0.02**</td><td>-0.02*</td><td>-0.02**</td><td>-0.004</td><td>-0.04***</td><td>0.02**</td><td>-0.004</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>13 Market Pricea</td><td>0.10***</td><td>-0.20***</td><td>0.46***</td><td>0.04***</td><td>0.08***</td><td>-0.01</td><td>-0.04***</td><td>0.04***</td><td>0.03***</td><td>0.20***</td><td>-0.03***</td><td>0.07***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>14 Task Densitya</td><td>0.08***</td><td>-0.32***</td><td>0.10***</td><td>0.05***</td><td>0.03***</td><td>-0.03***</td><td>-0.10***</td><td>0.01</td><td>-0.04***</td><td>0.10***</td><td>-0.03***</td><td>0.05***</td><td>0.26***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15 Title lengtha</td><td>-0.15***</td><td>-0.06***</td><td>0.25***</td><td>-0.07***</td><td>0.04***</td><td>0.01</td><td>0.03***</td><td>0.01</td><td>0.02***</td><td>0.06***</td><td>0.03***</td><td>0.04***</td><td>0.05***</td><td>-0.04***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>16 Description Lengtha</td><td>-0.09***</td><td>0.10***</td><td>0.20***</td><td>0.01</td><td>0.05***</td><td>0.03***</td><td>0.05***</td><td>0.04***</td><td>0.10***</td><td>0.04***</td><td>0.01</td><td>0.003</td><td>0.05***</td><td>-0.05***</td><td>0.18***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>17 Background information</td><td>-0.015*</td><td>0.061***</td><td>0.075***</td><td>0.013</td><td>-0.041***</td><td>-0.011</td><td>0.030***</td><td>0.008</td><td>0.046***</td><td>-0.003</td><td>-0.038***</td><td>-0.006</td><td>-0.009</td><td>-0.048***</td><td>0.093***</td><td>0.299***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>18 Content wordsb</td><td>-0.014*</td><td>-0.087***</td><td>0.182***</td><td>-0.063***</td><td>-0.062***</td><td>-0.047***</td><td>0.003</td><td>-0.006</td><td>-0.004</td><td>0.075***</td><td>0.001</td><td>0.038***</td><td>0.061***</td><td>0.015*</td><td>0.100***</td><td>0.002</td><td>-0.015*</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>19 Concretenessb</td><td>-0.03***</td><td>0.03***</td><td>-0.01</td><td>0.001</td><td>-0.004</td><td>0.01</td><td>0.03***</td><td>-0.004</td><td>0.01</td><td>-0.01</td><td>0.02*</td><td>-0.02**</td><td>-0.04***</td><td>-0.02**</td><td>-0.003</td><td>0.15***</td><td>0.069***</td><td>0.033***</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>20 Specificityb</td><td>-0.16***</td><td>-0.02***</td><td>0.16***</td><td>-0.09***</td><td>0.09***</td><td>0.03***</td><td>0.01</td><td>0.03***</td><td>0.02**</td><td>0.06***</td><td>0.003</td><td>0.01</td><td>0.03***</td><td>-0.01</td><td>0.11***</td><td>0.26***</td><td>0.056***</td><td>-0.246***</td><td>0.03***</td><td>1</td><td></td><td></td><td></td></tr><tr><td>21 Textual errorsb</td><td>0.03***</td><td>0.05***</td><td>-0.02**</td><td>0.002</td><td>-0.003</td><td>0.01</td><td>0.02***</td><td>-0.01</td><td>0.06***</td><td>0.01</td><td>-0.01</td><td>-0.02**</td><td>-0.01</td><td>-0.02***</td><td>-0.01</td><td>0.25***</td><td>0.029***</td><td>-0.111***</td><td>0.07***</td><td>0.12***</td><td>1</td><td></td><td></td></tr><tr><td>22 PosEmo wordsb</td><td>0.06***</td><td>0.08***</td><td>-0.04***</td><td>0.003</td><td>-0.10***</td><td>0.001</td><td>0.02**</td><td>-0.01</td><td>0.02*</td><td>-0.06***</td><td>0.01</td><td>0.01</td><td>-0.04***</td><td>-0.03***</td><td>0.02*</td><td>0.18***</td><td>0.043***</td><td>-0.041***</td><td>0.03***</td><td>-0.01</td><td>0.11***</td><td>1</td><td></td></tr><tr><td>23 NegEmo wordsb</td><td>0.01</td><td>0.03***</td><td>-0.03***</td><td>0.01</td><td>0.037***</td><td>0.02***</td><td>-0.01</td><td>0.01</td><td>0.01</td><td>-0.02**</td><td>-0.004</td><td>-0.002</td><td>-0.001</td><td>0.004</td><td>-0.01</td><td>0.16***</td><td>-0.017**</td><td>-0.113***</td><td>0.04***</td><td>-0.03***</td><td>0.11***</td><td>0.02***</td><td>1</td></tr></table>

## $^{*}p<0.05$ ; $^{**}p<0.01$ ; $^{***}p<0.001$ . $^{a}$ Means the natural logarithmic transformation. $^{b}$ Means the square root transformation.

variable X is negative and significant; (2) The slope of the curve is positive when X is at its lowest value and negative when X is at its highest value; (3) The X value is within the value range at the inflection point of the curve. According to Model 2, the quadratic coefficients of concreteness ( $\beta = -0.03$ , p < 0.001) and specificity ( $\beta = -0.04$ , p < 0.001)

TABLE 7 Regression results.

<table><tr><td></td><td>Model 1</td><td>Model 2</td></tr><tr><td>Constant</td><td>-11.43*** (1.66)</td><td>-8.17*** (1.69)</td></tr><tr><td colspan="3">Control variables</td></tr><tr><td>Number of attentionsa</td><td>0.79*** (0.03)</td><td>0.79*** (0.03)</td></tr><tr><td>Rewarda</td><td>0.03* (0.01)</td><td>0.02* (0.01)</td></tr><tr><td>Durationa</td><td>0.06*** (0.01)</td><td>0.06*** (0.01)</td></tr><tr><td>Number of attachmentsa</td><td>-0.73*** (0.02)</td><td>-0.70*** (0.02)</td></tr><tr><td>Number of demand complementsb</td><td>0.07*** (0.01)</td><td>0.07*** (0.01)</td></tr><tr><td>Urgent demand</td><td>0.21*** (0.05)</td><td>0.20*** (0.05)</td></tr><tr><td>Price-increasing</td><td>-0.06** (0.02)</td><td>-0.06* (0.02)</td></tr><tr><td>Bid-hidden</td><td>0.12*** (0.02)</td><td>0.12*** (0.02)</td></tr><tr><td>Employers&#x27; experience level</td><td>-0.01* (0.004)</td><td>-0.01* (0.004)</td></tr><tr><td>Real-name authentication</td><td>-0.06*** (0.02)</td><td>-0.06*** (0.02)</td></tr><tr><td>Employers&#x27; VIP level</td><td>0.13*** (0.01)</td><td>0.13*** (0.01)</td></tr><tr><td>Market pricea</td><td>0.002 (0.02)</td><td>0.003 (0.02)</td></tr><tr><td>Task densitya</td><td>-0.01 (0.01)</td><td>-0.01 (0.01)</td></tr><tr><td>Title lengtha</td><td>0.04* (0.02)</td><td>0.03* (0.02)</td></tr><tr><td>Description lengtha</td><td>-0.08*** (0.01)</td><td>-0.10*** (0.01)</td></tr><tr><td>Background information</td><td>0.13*** (0.01)</td><td>0.13*** (0.01)</td></tr><tr><td>Content wordsb</td><td>1.67*** (0.37)</td><td>0.89* (0.39)</td></tr><tr><td>Content wordsb * Content wordsb</td><td>-0.09*** (0.02)</td><td>-0.04* (0.02)</td></tr><tr><td>Task type</td><td>Included</td><td>Included</td></tr><tr><td>Year dummies</td><td>Included</td><td>Included</td></tr><tr><td>Month dummies</td><td>Included</td><td>Included</td></tr><tr><td colspan="3">Independent variables</td></tr><tr><td>Concretenessb</td><td></td><td>0.09*** (0.02)</td></tr><tr><td>Concretenessb * Concretenessb</td><td></td><td>-0.03*** (0.01)</td></tr><tr><td>Specificityb</td><td></td><td>0.12*** (0.02)</td></tr><tr><td>Specificityb * Specificityb</td><td></td><td>-0.04*** (0.01)</td></tr><tr><td>Textual errorsb</td><td></td><td>-0.15* (0.08)</td></tr><tr><td>Positive emotional wordsb</td><td></td><td>0.30*** (0.07)</td></tr><tr><td>Negative emotional wordsb</td><td></td><td>-0.07*** (0.02)</td></tr><tr><td>R2/R2adj</td><td>0.5525/0.5513</td><td>0.5568/0.5554</td></tr><tr><td>SigFchange</td><td>0.000***</td><td>0.000***</td></tr><tr><td>N</td><td>13 929</td><td></td></tr></table>

Note: The values in parentheses denote robust standard deviations. For the two-tailed test $*p < 0.05$ ; $**p < 0.01$ ; $***p < 0.001$ .  
$^{a}$ Means the natural logarithmic transformation.  
$^{b}$ Means the square root transformation.

are negative and significant, satisfying the first condition. In addition, as shown in Model 2, the extreme value point of concreteness is 1.53, which is within its value range. The extreme point of specificity is 1.73, which is also within its value range. According to the extreme points and the value ranges, the slopes of concreteness's lowest and highest points are 0.09 and -0.29, respectively, and the slope of specificity's lowest and highest points are 0.12 and -0.27, respectively. Conditions Two and Three are satisfied. According to these results, all hypotheses about the inverted U-shaped effect of informational diagnosticity signals are supported. Our study verifies that the growth of concreteness and specificity can improve the task's solver participation initially, but after reaching a peak (concreteness: 1.53, specificity: 1.73), solver participation declines (see Figure 2).

Then, for affective linguistic signals, positive emotional words are positively related to solvers' participation, and negative emotional words are negatively related to solvers' participation. Specifically, higher participation rates are exhibited when the description shows more positive emotional words and fewer negative emotional words. Thus, the effects of affective linguistic signals on participation are also consistent with the hypotheses.

## 5.2 | Robustness check

To validate our estimation results, we identified a sample of 17 240 tasks hosted on TaskCN.com to exclude the possibility that our results were driven by the sample crowdsourcing platform's characteristics. We then re-ran our main analysis for a robustness check. TaskCN.com was once a major Chinese crowdsourcing platform. Within just 6 months of its establishment in early 2006, it accounted for approximately 60% of the domestic crowdsourcing market in China and became an industry leader. Both TaskCN.com and epwk.com have similar single-winner reward modes. Because TaskCN.com was the earliest practical Chinese crowdsourcing website, it lagged behind in terms of website design, user-friendliness, customer service, and organisational structure. The results of our analysis of this sample remained similar to those of our main analysis. Overall, these results confirm our predictions: both informational and affective linguistic signals affect solver participation, and there is an inverted U-shaped relationship between informational linguistic signals and solver participation (see Table 8).

In addition, to rule out the alternative explanation that the converted U-shape relationship is caused by the distribution of these tasks in their diagnosticity, we conduct two extra control variables to eliminate the possible familiarity of the potential solvers to the tasks. We divided the distribution of concreteness and specificity into a value range of 0.1, then calculated the distribution density by counting the number of tasks within the same range of concreteness or specificity before the task was published, then took the natural logarithm. Our results for the independent variables remain significant after adding the concreteness distribution and the specificity distribution (see Table 9). Thus, we have ruled out the alternative explanation for the inverted U-shaped relationship.

![](/api/attachments/VN2Z443D/fulltext/images/7cd143b6383c3bff2ca377ab3353a41c0eeccfd6e41c2c0a200d4e0752f41995.jpg)  
FIGURE 2 Inverted U-shaped relationships.

![](/api/attachments/VN2Z443D/fulltext/images/ff1edb8110fd8cd41ef48dc1b8f79a015d9b032633612da246e49749add802be.jpg)

TABLE 8 Regression results for TaskCN.

<table><tr><td></td><td>Model 1</td><td>Model 2</td></tr><tr><td>Constant</td><td>-11.49*** (0.38)</td><td>-10.76*** (0.33)</td></tr><tr><td colspan="3">Control variables</td></tr><tr><td>Number of attentionsa</td><td>1.53*** (0.02)</td><td>1.51*** (0.02)</td></tr><tr><td>Rewardb</td><td>0.01*** (0.001)</td><td>0.01*** (0.001)</td></tr><tr><td>Durationa</td><td>0.15*** (0.01)</td><td>0.14*** (0.01)</td></tr><tr><td>Number of attachmentsa</td><td>-0.22*** (0.02)</td><td>-0.20*** (0.02)</td></tr><tr><td>Demand complement</td><td>0.04 (0.03)</td><td>0.05 (0.03)</td></tr><tr><td>Employers&#x27; experience level</td><td>-0.0001*** (0.00002)</td><td>-0.0002*** (0.00003)</td></tr><tr><td>Real-name authentication</td><td>0.01 (0.04)</td><td>-0.05 (0.03)</td></tr><tr><td>Market pricea</td><td>0.17*** (0.01)</td><td>0.22*** (0.01)</td></tr><tr><td>Task densitya</td><td>-0.06* (0.02)</td><td>-0.07** (0.02)</td></tr><tr><td>Title lengtha</td><td>-0.35*** (0.01)</td><td>-0.34*** (0.01)</td></tr><tr><td>Description lengtha</td><td>-0.02* (0.01)</td><td>-0.05*** (0.01)</td></tr><tr><td>Background information</td><td>0.21*** (0.02)</td><td>0.22*** (0.02)</td></tr><tr><td>Content wordsb</td><td>0.15* (0.07)</td><td>0.21*** (0.06)</td></tr><tr><td>Content wordsb * Content wordsb</td><td>-0.02*** (0.04)</td><td>-0.02*** (0.04)</td></tr><tr><td>Task type</td><td>Included</td><td>Included</td></tr><tr><td>Year dummies</td><td>Included</td><td>Included</td></tr><tr><td>Month dummies</td><td>Included</td><td>Included</td></tr><tr><td colspan="3">Independent variables</td></tr><tr><td>Concretenessb</td><td></td><td>0.12*** (0.02)</td></tr><tr><td>Concretenessb * Concretenessb</td><td></td><td>-0.03*** (0.004)</td></tr><tr><td>Specificityb</td><td></td><td>0.08*** (0.02)</td></tr><tr><td>Specificityb * Specificityb</td><td></td><td>-0.04*** (0.01)</td></tr><tr><td>Textual errorsb</td><td></td><td>-0.29*** (0.09)</td></tr><tr><td>Positive emotional wordsb</td><td></td><td>0.08*** (0.01)</td></tr><tr><td>Negative emotional wordsb</td><td></td><td>-0.05*** (0.01)</td></tr><tr><td>R2/R2adj</td><td>0.6834/0.6827</td><td>0.6898/0.6890</td></tr><tr><td>SigFchange</td><td>0.000***</td><td>0.000***</td></tr><tr><td>N</td><td>17 240</td><td></td></tr></table>

Note: The values in parentheses denote robust standard deviations. For the two-tailed test $*p < 0.05$ ; $**p < 0.01$ ; $***p < 0.001$ .  
$^{a}$ Means the natural logarithmic transformation.  
$^{b}$ Means the square root transformation.

## 6 | DISCUSSION

## 6.1 | Key findings

From a linguistic signalling perspective, we distinguished between two types of linguistic signals and tested their role in solver participation. Our research findings are twofold. First, we find that giving well-defined instructions is not always good. The inverted U-shaped relationship between information diagnosticity and solvers' participation indicates that an appropriate level of diagnosticity is helpful for potential solvers to gain an understanding of the employer's needs, thus reducing uncertainty and promoting participation. However, after reaching a peak, when the description is too concrete or specific, the space for autonomy and creativity for potential solvers diminishes, thus decreasing its attractiveness. Moreover, we examined the negative effect of textual errors, demonstrating the importance of linguistic accuracy. Second, our study proposed and identified different effects of positive and negative emotional words, both of which serve as affective linguistic signals influencing solver participation. To attract more solvers, employers can show their passion and friendliness while avoiding showing negative emotions like anger or anxiety.

TABLE 9 Regression results to rule out alternative explanation.

<table><tr><td></td><td>Model 1</td><td>Model 2</td></tr><tr><td>Constant</td><td>-10.27*** (1.67)</td><td>-7.98*** (1.69)</td></tr><tr><td colspan="3">Control variables</td></tr><tr><td>Number of attentionsa</td><td>0.79*** (0.03)</td><td>0.79*** (0.03)</td></tr><tr><td>Rewarda</td><td>0.03* (0.01)</td><td>0.02* (0.01)</td></tr><tr><td>Durationa</td><td>0.06*** (0.01)</td><td>0.06*** (0.01)</td></tr><tr><td>Number of attachmentsa</td><td>-0.73*** (0.02)</td><td>-0.70*** (0.02)</td></tr><tr><td>Number of demand complementsb</td><td>0.07*** (0.01)</td><td>0.07*** (0.01)</td></tr><tr><td>Urgent demand</td><td>0.20*** (0.05)</td><td>0.20*** (0.05)</td></tr><tr><td>Price-increasing</td><td>-0.06* (0.02)</td><td>-0.06* (0.02)</td></tr><tr><td>Bid-hidden</td><td>0.12*** (0.02)</td><td>0.12*** (0.02)</td></tr><tr><td>Employers&#x27; experience level</td><td>-0.01* (0.004)</td><td>-0.01* (0.004)</td></tr><tr><td>Real-name authentication</td><td>-0.06*** (0.02)</td><td>-0.06*** (0.02)</td></tr><tr><td>Employers&#x27; VIP level</td><td>0.13*** (0.01)</td><td>0.13*** (0.01)</td></tr><tr><td>Market pricea</td><td>0.003 (0.02)</td><td>0.003 (0.02)</td></tr><tr><td>Task densitya</td><td>-0.01 (0.01)</td><td>-0.01 (0.01)</td></tr><tr><td>Title lengtha</td><td>0.04* (0.02)</td><td>0.03 (0.02)</td></tr><tr><td>Description lengtha</td><td>-0.08*** (0.01)</td><td>-0.10*** (0.01)</td></tr><tr><td>Background information</td><td>0.13*** (0.01)</td><td>0.13*** (0.01)</td></tr><tr><td>Content wordsb</td><td>1.34*** (0.38)</td><td>0.82* (0.38)</td></tr><tr><td>Content wordsb * Content wordsb</td><td>-0.07*** (0.02)</td><td>-0.04* (0.02)</td></tr><tr><td>Task Type</td><td>Included</td><td>Included</td></tr><tr><td>Year Dummies</td><td>Included</td><td>Included</td></tr><tr><td>Month Dummies</td><td>Included</td><td>Included</td></tr><tr><td>Concreteness distributiona</td><td>0.03*** (0.01)</td><td>0.01 (0.01)</td></tr><tr><td>Specificity distributiona</td><td>0.006 (0.005)</td><td>0.001 (0.005)</td></tr><tr><td colspan="3">Independent Variables</td></tr><tr><td>Concretenessb</td><td></td><td>0.08*** (0.02)</td></tr><tr><td>Concretenessb * Concretenessb</td><td></td><td>-0.03*** (0.01)</td></tr><tr><td>Specificityb</td><td></td><td>0.07** (0.03)</td></tr><tr><td>Specificityb * Specificityb</td><td></td><td>-0.02** (0.01)</td></tr><tr><td>Textual errorsb</td><td></td><td>-0.18* (0.07)</td></tr><tr><td>Positive emotional wordsb</td><td></td><td>0.27*** (0.07)</td></tr><tr><td>Negative emotional wordsb</td><td></td><td>-0.08*** (0.02)</td></tr><tr><td>R2/R2adj</td><td>0.5537/0.5525</td><td>0.5569/0.5554</td></tr><tr><td>SigFchange</td><td>0.000***</td><td>0.000***</td></tr><tr><td>N</td><td>13 929</td><td></td></tr></table>

Note: The values in parentheses denote robust standard deviations. For the two-tailed test $*p < 0.05$ ; $**p < 0.01$ ; $***p < 0.001$ .  
$^{a}$ Means the natural logarithmic transformation.  
$^{b}$ Means the square root transformation.

## 6.2 | Theoretical implications

This study contributes to the growing literature on competitive crowdsourcing platforms. First, we extend the research on crowdsourcing contests by investigating an under-studied topic: the role of linguistic signals in task descriptions. Although previous studies have fully explored crowdsourcing participation from three aspects: task design, individual characteristics, and environmental factors (Nov et al., 2009; Taylor & Joshi, 2019), only a few antecedents, such as length and the number of requirements have been considered from a task description perspective (Jiang et al., 2021; Walter & Back, 2011; Yang et al. (2009)). Notably, Wu et al. (2019) and Yang et al. (2021) attempted to explore the linguistic features of task descriptions and preliminarily discussed the influence of self-distancing, cognitive complexity, causality, tentative language, and other linguistic features on solvers' participation. However, these two studies ignored the signal properties of linguistic features and the theoretical logic behind them. Based on signalling theory, we introduce linguistic signals, distinguish between informational and affective signals, and discuss the influence of the two kinds of signals on solver participation. We propose a new theoretical perspective on linguistic signals that expands the boundaries of research and lays a theoretical foundation for future research on crowdsourcing participation.

Second, our study developed the signalling theory by focusing on transmitting linguistic signals from employers to potential solvers. Although the information asymmetry in crowdsourcing applies to both sides, the employers and the solvers, in literature, the application of signal theory in the crowdsourcing context was often reflected in how the solvers send signals to the employer to increase the likelihood of winning the contest (Piazza et al., 2022; Situmeang et al., 2019) or improve bargaining power (Durward et al., 2016; Hong & Pavlou, 2012). Little literature systematically discusses how employers try to signal their intentions to potential solvers actively. In addition, traditional signalling theory has always downplayed the impact of rhetorical signals (that is, relevant, language-based information) (Bergh et al., 2014; Farrell & Rabin, 1996). The discord between established management research and signalling theory's assessment of rhetoric hampers the development of signalling theory (Steigenberger, 2017). Recent developments in the signalling theory have showcased rhetoric being operationalised as a signal (Anglin et al., 2018; Steigenberger & Wilhelm, 2018), wherein signalers can indicate underlying qualities or intentions via text. However, this frontier view still needs sufficient empirical support in different research contexts. By exploring the signal attributes of the linguistic cues transfer from crowdsourcing employers to potential solvers, our study filled the gaps mentioned above, thus contributing to the signal theory itself.

Third, we introduce the effect of uncertainty and propose a new theoretical explanation for the inverted U-shaped relationship between information diagnosticity and solvers' participation. Proposing the curvilinear relationship may solve the controversy of if high-diagnosticity task descriptions contribute to mass participation. Information diagnosticity focuses on exploring how task descriptions provide 'clear' expression, which helps to reduce uncertainty and alleviates the information asymmetry between employers and potential solvers. In general, the psycholinguistic literature suggests that an improvement in the information recipients' understanding of the content should produce a perceived reduction in uncertainty, thus contributing to their behavioural decisions (Larrimore et al., 2011; Toma & D'Angelo, 2014). However, previous studies have overemphasised the positive effect of reducing uncertainty while ignoring the opportunity for creativity that can be embedded in uncertainty (Shen et al., 2015; Shepherd et al., 2012). In the face of creative crowdsourcing tasks, we believe that an appropriate degree of uncertainty provides more possibilities for solvers to develop novel solutions. Therefore, our study proposes an inverted

U-shaped relationship between the informational diagnosticity of task descriptions and solvers' participation. Specifically, tasks with higher diagnostic information (i.e. higher concreteness and specificity) alleviate uncertainty and thus increase participation; however, with increasing concreteness and specificity, over-defined task descriptions reduce the space for autonomy and creativity allowed to potential solvers of the tasks, thus making them less attractive. The proposed inverted U-shaped relationship makes up for the limitations of previous studies focusing only on the positive aspects of uncertainty reduction and provides a new theoretical explanation for the relationship between information diagnosticity and solver participation.

Last, we also found that task descriptions' positive/negative affective signals can promote or weaken task attraction. Based on information signals, our study further explores the effect of affective linguistic signals in task descriptions on solvers' participation, which makes up for the gap resulting from the failure of previous empirical studies to consider the effect of emotional arousal in task descriptions. Specifically, positive emotional words stimulated the positive emotional responses of potential solvers and thus positively influenced their behavioural decisions in crowdsourcing tasks. Negative emotional words had the opposite effect. The conclusions of the research on affective signals enrich the existing crowdsourcing participation literature and lay a foundation for further research on other types of affective signals.

## 6.3 | Practical implications

From a pragmatic perspective, this study's findings indicate that crowdsourcing employers can write task descriptions to adequately and reliably present their demands, intentions, and expectations to elicit a more significant response from a willing and able crowd. This focus on the task description compensates for the usual emphasis on task design, which is often limited to discussing rewards and deadlines and ignores the inadequacy of the employer's editing and generating of tasks. Our study fills these gaps and provides practical operational suggestions for employers to attract solvers to crowdsourcing competition tasks.

First, potential solvers read a crowdsourcing task description to confirm employers' requirements. In this respect, when writing their task descriptions, employers should use particular ways to transmit their needs more clearly and comprehensively. If the description is not concrete and specific, for example, just saying, 'Eye hospital logo needed'. potential solvers will be full of uncertainty and unwilling to participate. At this point, the employer can add more concrete and specific information to reflect their preferences better, such as, 'I need a circular icon but without any Chinese characters in it'. However, because of the inverted U-shaped relationship, employers should not state their needs too concretely or specifically. Perhaps, seekers can even increase ambiguity by not specifying their questions in full detail, thus increasing the breadth of search that the solvers undertake within a set of known solution approaches. Moreover, the negative effect of textual errors shows that employers should also be aware of linguistic accuracy when delivering their demands because more textual errors affect the reading feelings of potential solvers in a manner detrimental to attracting more participants.

In addition, according to the analysis and robustness tests, the results for the two platforms show that although our conclusions are universal and robust across different platforms, the coefficients of the same dependent variables are different, and the peak values of the inverted U-shaped relationship are located in different locations. Furthermore, the way we examine variables is lexical, so subtly manipulating the description is not easy. Overall, our findings shed light on this phenomenon, and employers need to balance adequately presenting their needs and getting more participation. Different employers may make different choices according to their own needs.

Finally, besides detailed requirements, employers can also give affective linguistic signals to evoke the emotional response of potential solvers through their crowdsourcing task descriptions. Using positive emotional words helps evoke positive emotions, build a positive image, and evoke trustworthiness, thereby increasing engagement. In addition, employers should be careful not to include negative emotions in their descriptions. Instead of arousing sympathy and eliciting help, these emotional words are detrimental to building the image and trust of the employer, which in turn decreases solver participation.

## 6.4 | Limitations and future research

Despite its merits, this study leaves us with some unanswered questions. First, some tasks may provide additional instructions at later stages of the work. Such extensions can contain useful linguistic information relevant to the field. Moreover, because this additional information is typically issued later than the description, the time difference can significantly affect the role of the task description. Thus, another potential avenue for relevant future research is identifying and analysing the additional instructions offered in crowdsourcing tasks.

Second, a word-counting methodology is used in this study to measure the linguistic signals in employers' crowdsourcing task descriptions. Despite the accuracy and effectiveness of this methodology in processing large amounts of data, it misses the nuances of more complex and underlying phenomena (Jiang et al., 2022; Toma & D'Angelo, 2014). The linguistic categories used in this study are similar to those used in past studies on topics such as P2P lending, fraud detection, and crowdfunding. However, it must be noted that, naturally, many other interesting qualitative aspects can be studied in future research on a topic that is not bounded. Moreover, the variations between different languages are very subtle, and measuring such differences using methodologies that resort to simple quantification is sometimes tricky. Given these considerations, future research could employ a multi-level approach that combines computerised content analysis with qualitative discourse analysis.

Moreover, since the task publication precedes users' perceptions of the description and their subsequent decision to participate, there is a temporal order that suggests potential causal effects to some extent. However, regression models mainly validate correlation relationships, and indeed, the evidence for causal relationships is insufficient. Future studies could explore empirical settings that allow for causal inferences or incorporate experimental methods to establish causal relationships more effectively.

## 7 | CONCLUSION

Many employers are keenly interested in how to present crowdsourcing tasks as attractively as possible on online platforms. As this study demonstrates, the participation of solvers in crowdsourcing tasks is heavily influenced by the linguistic signals which employers send when writing their task descriptions. Understanding the effects of linguistic signals in task descriptions on solver participation in crowdsourcing is essential not only for employers and solvers but also for other online communication media that seek to attract greater participation. It is an important area for future research development.

## ACKNOWLEDGEMENTS

This work received support from the National Natural Science Foundation of China (72172168; 71872149; 71872144) and Double First-class construction project of Central University of Finance and Economics.

## DATA AVAILABILITY STATEMENT

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## ORCID

Qian Liu https://orcid.org/0000-0001-9125-808X

## REFERENCES

Abe, J. A. A. (2011). Changes in Alan Greenspan's language use across the economic cycle: A text analysis of his testimonies and speeches. Journal of Language and Social Psychology, 30(2), 212–223.

Agichtein, E., Castillo, C., Donato, D., Gionis, A., & Mishne, G. (2008). Finding high-quality content in social media. Paper presented at the Proceedings of the 2008 international conference on web search and data mining.

Alvarez-Conrad, J., Zoellner, L. A., & Foa, E. B. (2001). Linguistic predictors of trauma pathology and physical health. Applied Cognitive Psychology, 15(7), S159–S170.

Anglin, A. H., Short, J. C., Drover, W., Stevenson, R. M., McKenny, A. F., & Allison, T. H. (2018). The power of positivity? The influence of positive psychological capital language on crowdfunding performance. Journal of Business Venturing, 33(4), 470–492.

Archak, N. (2010). Money, glory and cheap talk: Analyzing strategic behavior of contestants in simultaneous crowdsourcing contests on TopCoder. Com. Paper Presented at the Proceedings of the 19th International Conference on World Wide Web.

Arguello, J., Butler, B. S., Joyce, E., Kraut, R., Ling, K. S., Rosé, C., & Wang, X. (2006). Talk to me: Foundations for successful individual-group interactions in online communities. Paper Presented at the Proceedings of the SIGCHI Conference on Human Factors in Computing Systems.

Awards, A. (2015). Piece# 1-Make Your Own Burger. http://www.ameawards.com/winners/2012/piecesmobile.php?iid=429740&pid=1

Baikie, K. A., Wilhelm, K., Johnson, B., Boskovic, M., Wedgwood, L., Finch, A., & Huon, G. (2006). Expressive writing for high-risk drug dependent patients in a primary care clinic: A pilot study. Harm Reduction Journal, 3(1), 1–8.

Bantum, E. O. C., & Owen, J. E. (2009). Evaluating the validity of computerized content analysis programs for identification of emotional expression in cancer narratives. Psychological Assessment, 21(1), 79–88.

Barrett, P. (2007). Structural equation modelling: Adjudging model fit. Personality and Individual Differences, 42(5), 815–824.

Bayus, B. L. (2013). Crowdsourcing new product ideas over time: An analysis of the Dell IdeaStorm community. Management Science, 59(1), 226–244.

Beevers, C. G., & Scott, W. D. (2001). Ignorance may be bliss, but thought suppression promotes superficial cognitive processing. Journal of Research in Personality, 35(4), 546–553.

Berger, C. R., & Calabrese, R. J. (1974). Some explorations in initial interaction and beyond: Toward a developmental theory of interpersonal communication. Human Communication Research, 1(2), 99–112.

Bergh, D. D., Connelly, B. L., Ketchen, D. J., Jr., & Shannon, L. M. (2014). Signalling theory and equilibrium in strategic management research: An assessment and a research agenda. Journal of Management Studies, 51(8), 1334–1360.

Blankenship, K. L., & Craig, T. Y. (2011). Language use and persuasion: Multiple roles for linguistic styles. Social and Personality Psychology Compass, 5(4), 194–205.

Bono, J. E., & Ilies, R. (2006). Charisma, positive emotions and mood contagion. The Leadership Quarterly, 17(4), 317–334.

Boudreau, K. J., Lacetera, N., & Lakhani, K. R. (2011). Incentives and problem uncertainty in innovation contests: An empirical analysis. Management Science, 57(5), 843–863.

Brabham, D. C. (2008). Crowdsourcing as a model for problem solving: An introduction and cases. Convergence, 14(1), 75–90.

Brabham, D. C. (2009). Crowdsourcing the public participation process for planning projects. Planning Theory, 8(3), 242–262.

Brett, J. M., Olekalns, M., Friedman, R., Goates, N., Anderson, C., & Lisco, C. C. (2007). Sticks and stones: Language, face, and online dispute resolution. Academy of Management Journal, 50(1), 85–99.

Bryden, J., Funk, S., & Jansen, V. A. (2013). Word usage mirrors community structure in the online social network twitter. EPJ Data Science, 2(1), 1–9.

Brysbaert, M., Warriner, A. B., & Kuperman, V. (2014). Concreteness ratings for 40 thousand generally known English word lemmas. Behavior Research Methods, 46, 904–911.

Centerbar, D. B., Schnall, S., Clore, G. L., & Garvin, E. D. (2008). Affective incoherence: When affective concepts and embodied reactions clash. Journal of Personality Social Psychology, 94(4), 560–578.

Chen, L., Baird, A., & Straub, D. (2020). A linguistic signaling model of social support exchange in online health communities. Decision Support Systems, 130, 113233.

Chen, P. Y., Pavlou, P., Wu, S., & Yang, Y. (2021). Attracting high-quality contestants to contest in the context of crowdsourcing contest platform. Production and Operations Management, 30(6), 1751–1771.

Chiu, C.-M., Hsu, M.-H., & Wang, E. T. (2006). Understanding knowledge sharing in virtual communities: An integration of social capital and social cognitive theories. Decision Support Systems, 42(3), 1872–1888.

Chua, A. Y., & Banerjee, S. (2016). Helpfulness of user-generated reviews as a function of review sentiment, product type and information quality. Computers in Human Behavior, 54, 547–554.

Cohen, A. S., Minor, K. S., Baillie, L. E., & Dahir, A. M. (2008). Clarifying the linguistic signature: Measuring personality from natural speech. Journal of Personality Assessment, 90(6), 559–563.

Connelly, B. L., Certo, S. T., Ireland, R. D., & Reutzel, C. R. (2011). Signaling theory: A review and assessment. Journal of Management, 37(1), 39–67.

Connor, U., Davis, K. W., & De Rycker, T. (1995). Correctness and clarity in applying for overseas jobs: A cross-cultural analysis of US and Flemish applications. Text & Talk, 15(4), 457–476.

Creswell, J. D., Lam, S., Stanton, A. L., Taylor, S. E., Bower, J. E., & Sherman, D. K. (2007). Does self-affirmation, cognitive processing, or discovery of meaning explain cancer-related health benefits of expressive writing? Personality and Social Psychology Bulletin, 33(2), 238–250.

Daft, R. L., & Lengel, R. H. (1986). Organizational information requirements, media richness and structural design. Management Science, 32(5), 554–571.

Daft, R. L., & Macintosh, N. B. (1981). A tentative exploration into the amount and equivocality of information processing in organizational work units. Administrative Science Quarterly, 26, 207–224.

Daugherty, T., Lee, W.-N., Gangadharbatla, H., Kim, K., & Outhavong, S. (2005). Organizational virtual communities: Exploring motivations behind online panel participation. Journal of Computer-Mediated Communication, 10(4), JCMC10414.

Davis, D., & Brock, T. C. (1975). Use of first person pronouns as a function of increased objective self-awareness and performance feedback. Journal of Experimental Social Psychology, 11(4), 381–388.

Denecke, K., & Nejdl, W. (2009). How valuable is medical social media data? Content analysis of the medical web. Information Sciences, 179(12), 1870–1880.

Di Gangi, P. M., Wasko, M. M., & Hooker, R. E. (2010). Getting customers' ideas to work for you: Learning from Dell how to succeed with online user innovation communities. MIS Quarterly Executive, 9(4), 213–228.

Dickert, S., Sagara, N., & Slovic, P. (2011). Affective motivations to help others: A two-stage model of donation decisions. Journal of Behavioral Decision Making, 24(4), 361–376.

Dickert, S., & Slovic, P. (2009). Attentional mechanisms in the generation of sympathy. Judgment and Decision Making, 4, 297–306.

DiPalantino, D., & Vojnovic, M. (2009). Crowdsourcing and all-pay auctions. Proceedings of the 10th ACM conference on electronic commerce.

Durward, D., Blohm, I., & Leimeister, J. M. (2016). Rags to riches-how signaling behaviour causes a power shift in crowdsourcing markets. Paper presented at the European Conference on Information Systems (ECIS), Istanbul, Turkey.

Elliott, W. B., Rennekamp, K. M., & White, B. J. (2015). Does concrete language in disclosures increase willingness to invest? Review of Accounting Studies, 20(2), 839–865.

Erat, S., & Krishnan, V. (2012). Managing delegated search over design spaces. Management Science, 58(3), 606–623.

Evers, E. R., & Lakens, D. (2014). Revisiting Tversky's diagnosticity principle. Frontiers in Psychology, 5, 875.

Fan, L., & Zhang, X. (2020). The combination signaling effect of text and image on mobile phone review helpfulness-the moderating effect of signaling environment. IEEE Access, 8, 122736.

Farrell, J., & Rabin, M. (1996). Cheap talk. Journal of Economic Perspectives, 10(3), 103–118.

Filieri, R. (2015). What makes online reviews helpful? A diagnosticity-adoption framework to explain informational and normative influences in e-WOM. Journal of Business Research, 68(6), 1261–1270.

Gadiraju, U., Yang, J., & Bozzon, A. (2017). Clarity is a worthwhile quality: On the role of task clarity in microtask crowdsourcing. Paper presented at the Proceedings of the 28th ACM Conference on Hypertext and Social Media.

Garcia Martinez, M. (2015). Solver engagement in knowledge sharing in crowdsourcing communities: Exploring the link to creativity. Research Policy, 44(8), 1419–1430.

Gendron, M., Lindquist, K. A., Barsalou, L., & Barrett, L. F. (2012). Emotion words shape emotion percepts. Emotion, 12(2), 314–325.

Ghose, A., & Ipeirotis, P. G. (2010). Estimating the helpfulness and economic impact of product reviews: Mining text and reviewer characteristics. IEEE Transactions on Knowledge and Data Engineering, 23(10), 1498–1512.

Goh, D. H.-L., Pe-Than, E. P. P., & Lee, C. S. (2017). Perceptions of virtual reward systems in crowdsourcing games. Computers in Human Behavior, 70, 365–374.

Gonzales, A. L., Hancock, J. T., & Pennebaker, J. W. (2010). Language style matching as a predictor of social dynamics in small groups. Communication Research, 37(1), 3–19.

Gorbatai, A., & Nelson, L. (2015). The narrative advantage: Gender and the language of crowdfunding (pp. 1–32). Haas School of Business UC Berkeley. Research Papers.

Griffin, M. A., & Grote, G. (2020). When is more uncertainty better? A model of uncertainty regulation and effectiveness. Academy of Management Review, 45(4), 745–765.

Guastella, A. J., & Dadds, M. R. (2006). Cognitive-behavioral models of emotional writing: A validation study. Cognitive Therapy Research, 30(3), 397–414.

Haans, R. F., Pieters, C., & He, Z. L. (2016). Thinking about U: Theorizing and testing U-and inverted U-shaped relationships in strategy research. Strategic Management Journal, 37(7), 1177–1195.

Hackman, J. R., & Oldham, G. R. (1976). Motivation through the design of work: Test of a theory. Organizational Behavior and Human Performance, 16(2), 250–279.

Hancock, J. T., Curry, L. E., Goorha, S., & Woodworth, M. (2007). On lying and being lied to: A linguistic analysis of deception in computer-mediated communication. Discourse Processes, 45(1), 1–23.

Handelman, L. D., & Lester, D. (2007). The content of suicide notes from attempters and completers. Crisis, 28(2), 102–104.

Heberlein, A. S., Adolphs, R., Pennebaker, J. W., & Tranel, D. (2003). Effects of damage to right-hemisphere brain structures on spontaneous emotional and social judgments. Political Psychology, 24(4), 705–726.

Herr, P. M., Kardes, F. R., & Kim, J. (1991). Effects of word-of-mouth and product-attribute information on persuasion: An accessibility-diagnosticity perspective. Journal of Consumer Research, 17(4), 454–462.

Holtgraves, T. M. (2013). Language as social action: Social psychology and language use. Psychology Press.

Hong, Y., & Pavlou, P. (2012). An empirical investigation on provider pricing in online crowdsourcing markets for IT services. Paper presented at the ICIS 2012 Proceedings.

Howe, J. (2006). The rise of crowdsourcing. Wired Magazine, 14(6), 1–4.

Hynninen, N., & Kuteeva, M. (2017). “Good” and “acceptable” English in L2 research writing: Ideals and realities in history and computer science. Journal of English for Academic Purposes, 30, 53–65.

Javadi Khasraghi, H., & Aghaie, A. (2014). Crowdsourcing contests: Understanding the effect of competitors' participation history on their performance. Behaviour & Information Technology, 33(12), 1383–1395.

Jiang, T., Kang, F., Guo, W., He, W., Liu, L., Lu, X., Xu, Y., & Cui, L. (2022). CK-encoder: Enhanced language representation for sentence similarity. International Journal of Crowd Science, 6(1), 17–22.

Jiang, Z., Huang, Y., & Beil, D. R. (2021). The role of problem specification in crowdsourcing contests for design problems: A theoretical and empirical analysis. Manufacturing & Service Operations Management, 23(3), 637–656.

Jian-Gang, P. (2015). The risk management mechanism of crowdsourcing community innovation. China Soft Science, 2, 19.

Kim, D. J., Ferrin, D. L., & Rao, H. R. (2008). A trust-based consumer decision-making model in electronic commerce: The role of trust, perceived risk, and their antecedents. Decision Support Systems, 44(2), 544–564.

Kirmani, A., & Rao, A. R. (2000). No pain, no gain: A critical review of the literature on signaling unobservable product quality. Journal of Marketing, 64(2), 66–79.

Klein, H. J., Whitener, E. M., & Ilgen, D. R. (1990). The role of goal specificity in the goal-setting process. Motivation and Emotion, 14, 179–193.

Kogut, T., & Ritov, I. (2005). The “identified victim” effect: An identified group, or just a single individual? Journal of Behavioral Decision Making, 18(3), 157–167.

Kohli, R., & Melville, N. P. (2019). Digital innovation: A review and synthesis. Information Systems Journal, 29(1), 200–223.

Kopelman, S., Rosette, A. S., & Thompson, L. (2006). The three faces of eve: Strategic displays of positive, negative, and neutral emotions in negotiations. Organizational Behavior and Human Decision Processes, 99(1), 81–101.

Kousta, S.-T., Vinson, D. P., & Vigliocco, G. (2009). Emotion words, regardless of polarity, have a processing advantage over neutral words. Cognition, 112(3), 473–481.

Larrimore, L., Jiang, L., Larrimore, J., Markowitz, D., & Gorski, S. (2011). Peer to peer lending: The relationship between language features, trustworthiness, and persuasion success. Journal of Applied Communication Research, 39(1), 19–37.

Lau-Gesk, L., & Meyers-Levy, J. (2009). Emotional persuasion: When the valence versus the resource demands of emotions influence consumers' attitudes. Journal of Consumer Research, 36(4), 585–599.

Lawler, E. J., & Thye, S. R. (1999). Bringing emotions into social exchange theory. Annual Review of Sociology, 25(1), 217–244.

Li, J., Tang, J., Jiang, L., Yen, D. C., & Liu, X. (2019). Economic success of physicians in the online consultation market: A signaling theory perspective. International Journal of Electronic Commerce, 23(2), 244–271.

Li, S.-T., Pham, T.-T., & Chuang, H.-C. (2019). Do reviewers' words affect predicting their helpfulness ratings? Locating helpful reviewers by linguistics styles. Information & Management, 56(1), 28–38.

Lindquist, K. A., & Gendron, M. (2013). What's in a word? Language Constructs Emotion Perception. Emotion Review, 5(1), 66–71.

Liu, Q., Du, Q., Hong, Y., Fan, W., & Wu, S. (2020). User idea implementation in open innovation communities: Evidence from a new product development crowdsourcing community. Information Systems Journal, 30(5), 899–927.

Liu, T. X., Yang, J., Adamic, L. A., & Chen, Y. (2011). Crowdsourcing with all-pay auctions: A field experiment on Taskcn. Paper presented at the Proceedings of the American Society for Information Science and Technology.

Ludwig, S., De Ruyter, K., Friedman, M., Brüggen, E. C., Wetzels, M., & Pfann, G. (2013). More than words: The influence of affective content and linguistic style matches in online reviews on conversion rates. Journal of Marketing, 77(1), 87–103.

Luthans, F., & Youssef, C. M. (2004). Human, social, and now positive psychological capital management: Investing in people for competitive advantage. Organizational Dynamics, 33(2), 143–160.

Maaravi, Y., Idan, O., & Hochman, G. (2019). And sympathy is what we need my friend—Polite requests improve negotiation results. PLoS One, 14(3), e0212306.

Mairesse, F., & Walker, M. A. (2011). Controlling user perceptions of linguistic style: Trainable generation of personality traits. Computational Linguistics, 37(3), 455–488.

Manstead, A., & Fischer, A. H. (2001). Social appraisal: the social world as object of and influence on appraisal processes. In K. R. Scherer, A. Schorr, & T. Johnstone (Eds.), Appraisal Processes in Emotion: Theory, Methods, Research, (pp. 221–232). Oxford Univ. Press.

Markowitz, D. M., & Hancock, J. T. (2016). Linguistic obfuscation in fraudulent science. Journal of Language and Social Psychology, 35(4), 435–445.

Mavlanova, T., Benbunan-Fich, R., & Lang, G. (2016). The role of external and internal signals in E-commerce. Decision Support Systems, 87, 59–68.

McKenny, A. F., Short, J. C., & Payne, G. T. (2013). Using computer-aided text analysis to elevate constructs: An illustration using psychological capital. Organizational Research Methods, 16(1), 152–184.

McMullen, J. S., & Shepherd, D. A. (2006). Entrepreneurial action and the role of uncertainty in the theory of the entrepreneur. Academy of Management Review, 31(1), 132–152.

Mehl, M. R., & Pennebaker, J. W. (2003). The sounds of social life: A psychometric analysis of students' daily social environments and natural conversations. Journal of Personality and Social Psychology, 84(4), 857–870.

Mo, J., Sarkar, S., & Chen, J. (2018). Sponsored tasks and solver participation in crowdsourcing contests, Available at SSRN 3388758.

Montiel, I., Husted, B. W., & Christmann, P. (2012). Using private management standard certification to reduce information asymmetries in corrupt environments. Strategic Management Journal, 33(9), 1103–1113.

Morgeson, F. P., & Humphrey, S. E. (2006). The work design questionnaire (WDQ): Developing and validating a comprehensive measure for assessing job design and the nature of work. Journal of Applied Psychology, 91(6), 1321–1339.

Newman, M. L., Pennebaker, J. W., Berry, D. S., & Richards, J. M. (2003). Lying words: Predicting deception from linguistic styles. Personality and Social Psychology Bulletin, 29(5), 665–675.

Ni, X., Xue, G.-R., Ling, X., Yu, Y., & Yang, Q. (2007). Exploring in the weblog space by detecting informative and affective articles. Paper presented at the Proceedings of the 16th international conference on World Wide Web.

Nov, O., Naaman, M., & Ye, C. (2009). Motivational, structural and tenure factors that impact online community photo sharing. Paper presented at the Third International AAAI Conference on Weblogs and Social Media.

Ohly, S., Sonnentag, S., & Pluntke, F. (2006). Routinization, work characteristics and their relationships with creative and proactive behaviors. Journal of Organizational Behavior, 27(3), 257–279.

Oliver, E. J., Markland, D., Hardy, J., & Petherick, C. M. (2008). The effects of autonomy-supportive versus controlling environments on self-talk. Motivation and Emotion, 32(3), 200–212.

Packard, G., & Berger, J. (2021). How concrete language shapes customer satisfaction. Journal of Consumer Research, 47(5), 787–806.

Paivio, A. (1986). The role of topic and vehicle imagery in metaphor comprehension. Communication and Cognition, 19(3), 367–387.

Paivio, A. (1991). Dual coding theory: Retrospect and current status. Canadian Journal of Psychology/Revue Canadienne de Psychologie, 45(3), 255–287.

Parhankangas, A., & Renko, M. (2017). Linguistic style and crowdfunding success among social and commercial entrepreneurs. Journal of Business Venturing, 32(2), 215–236.

Paulus, P. B., Kohn, N. W., & Arditti, L. E. (2011). Effects of quantity and quality instructions on brainstorming. The Journal of Creative Behavior, 45(1), 38–46.

Pedersen, J., Kocsis, D., Tripathi, A., Tarrell, A., Weerakoon, A., Tahmasbi, N., ... De Vreede, G.-J. (2013). Conceptual foundations of crowdsourcing: A review of IS research. Paper presented at the 2013 46th Hawaii international conference on system sciences.

Pengnate, S. F., & Riggins, F. J. (2020). The role of emotion in P2P microfinance funding: A sentiment analysis approach. International Journal of Information Management, 54, 102138.

Pennebaker, J. W., & King, L. A. (1999). Linguistic styles: Language use as an individual difference. Journal of Personality and Social Psychology, 77(6), 1296–1312.

Pennebaker, J. W., & Lay, T. C. (2002). Language use and personality during crises: Analyses of mayor Rudolph Giuliani's press conferences. Journal of Research in Personality, 36(3), 271–282.

Pennebaker, J. W., Mehl, M. R., & Niederhoffer, K. G. (2003). Psychological aspects of natural language use: Our words, our selves. Annual Review of Psychology, 54(1), 547–577.

Petty, R. E., Harkins, S. G., & Williams, K. D. (1980). The effects of group diffusion of cognitive effort on attitudes: An information-processing view. Journal of Personality and Social Psychology, 38(1), 81–92.

Piazza, M., Mazzola, E., & Perrone, G. (2022). How can I signal my quality to emerge from the crowd? A study in the crowdsourcing context. Technological Forecasting and Social Change, 176, 121473.

Pollok, P., Lüttgens, D., & Piller, F. T. (2019). Attracting solutions in crowdsourcing contests: The role of knowledge distance, identity disclosure, and seeker status. Research Policy, 48(1), 98–114.

Rodriguez, A. J., Holleran, S. E., & Mehl, M. R. J. J. o. p. (2010). Reading between the lines: The lay assessment of subclinical depression from written self-descriptions. Journal of Personality, 78(2), 575–598.

Rude, S., Gortner, E.-M., & Pennebaker, J. (2004). Language use of depressed and depression-vulnerable college students. Cognition & Emotion, 18(8), 1121–1133.

Schulze, T., Seedorf, S., Geiger, D., Kaufmann, N., & Schader, M. (2011). Exploring task properties in crowdsourcing—An empirical study on mechanical Turk. Paper presented at the ECIS 2011 Proceedings.

Shao, B., Shi, L., Xu, B., & Liu, L. (2012). Factors affecting participation of solvers in crowdsourcing: An empirical study from China. Electronic Markets, 22(2), 73–82.

Shen, L., Fishbach, A., & Hsee, C. K. (2015). The motivating-uncertainty effect: Uncertainty increases resource investment in the process of reward pursuit. Journal of Consumer Research, 41(5), 1301–1315.

Shepherd, D. A., Haynie, J. M., & McMullen, J. S. (2012). Confirmatory search as a useful heuristic? Testing the veracity of entrepreneurial conjectures. Journal of Business Venturing, 27(6), 637–651.

Shuqiang, Z. (1987). Cognitive complexity and written production in English as a second language. Language Learning, 37(4), 469–481.

Simmons, R. A., Gordon, P. C., & Chambless, D. L. (2005). Pronouns in marital interaction: What do “you” and “I” say about marital health? Psychological Science, 16(12), 932–936.

Situmeang, F., Loke, R. E., de Boer, N., & de Boer, D. (2019). Empowered by innovation: Unravelling determinants of idea implementation in open innovation platforms. Paper presented at the 8th International Conference on Data Science, Technology and Applications, DATA 2019.

Smith, W. K., & Lewis, M. W. (2011). Toward a theory of paradox: A dynamic equilibrium model of organizing. Academy of Management Review, 36(2), 381–403.

Spence, M. (1978). Job market signaling. In Uncertainty in economics (pp. 281–306). Academic Press.

Srivastava, V., & Kalro, A. D. (2019). Enhancing the helpfulness of online consumer reviews: The role of latent (content) factors. Journal of Interactive Marketing, 48, 33–50.

Steigenberger, N. (2017). Why supporters contribute to reward-based crowdfunding. International Journal of Entrepreneurial Behavior & Research, 23(2), 336–353.

Steigenberger, N., & Wilhelm, H. (2018). Extending signaling theory to rhetorical signals: Evidence from crowdfunding. Organization Science, 29(3), 529–546.

Stewart, O., Lubensky, D., & Huerta, J. M. (2010). Crowdsourcing participation inequality: a SCOUT model for the enterprise domain. Paper presented at the Proceedings of the ACM SIGKDD Workshop on Human Computation.

Sun, Y., Wang, N., & Peng, Z. (2011). Working for one penny: Understanding why people would like to participate in online tasks with low payment. Computers in Human Behavior, 27(2), 1033–1041.

Suri, S., & Watts, D. J. (2011). Cooperation and contagion in web-based, networked public goods experiments. PLoS One, 6(3), e16836.

Tausczik, Y. R., & Pennebaker, J. W. (2010). The psychological meaning of words: LIWC and computerized text analysis methods. Journal of Language and Social Psychology, 29(1), 24–54.

Taylor, J., & Joshi, K. (2019). Joining the crowd: The career anchors of information technology workers participating in crowdsourcing. Information Systems Journal, 29(3), 641–673.

Taylor, P. J., & Thomas, S. (2008). Linguistic style matching and negotiation outcome. Negotiation and Conflict Management Research, 1(3), 263–281.

Ter Doest, L., Semin, G. R., & Sherman, S. J. (2002). Linguistic context and social perception: Does stimulus abstraction moderate processing style? Journal of Language and Social Psychology, 21(3), 195–229.

Terwiesch, C., & Xu, Y. (2008). Innovation contests, open innovation, and multiagent problem solving. Management Science, 54(9), 1529–1543.

Thorbjørnsen, H., & Supphellen, M. (2004). The impact of brand loyalty on website usage. Journal of Brand Management, 11(3), 199–208.

Toma, C. L., & D'Angelo, J. D. (2014). Tell-tale words: Linguistic cues used to infer the expertise of online medical advice. Journal of Language and Social Psychology, 34(1), 25–45.

Toma, C. L., & Hancock, J. T. (2012). What lies beneath: The linguistic traces of deception in online dating profiles. Journal of Communication, 62(1), 78–97.

Van Kleef, G. A. (2010). The emerging view of emotion as social information. Social and Personality Psychology Compass, 4(5), 331–343.

Van Kleef, G. A., Anastasopoulou, C., & Nijstad, B. A. (2010). Can expressions of anger enhance creativity? A test of the emotions as social information (EASI) model. Journal of Experimental Social Psychology, 46(6), 1042–1048.

Van Kleef, G. A., De Dreu, C. K., & Manstead, A. S. (2010). An interpersonal approach to emotion in social decision making: The emotions as social information model. In Advances in experimental social psychology (Vol. 42, pp. 45–96). Academic Press.

Van Kleef, G. A., De Dreu, C. K., Pietroni, D., & Manstead, A. S. (2006). Power and emotion in negotiation: Power moderates the interpersonal effects of anger and happiness on concession making. European Journal of Social Psychology, 36(4), 557–581.

Vasiloaia, M. (2009). Linguistic features of the language of advertising. Economy Transdisciplinarity Cognition, 1, 294–298.

Vukovic, M. (2009). Crowdsourcing for enterprises. Paper presented at the 2009 congress on services-I.

Walter, T., & Back, A. (2011). Towards measuring crowdsourcing success: An empirical study on effects of external factors in online idea contest. Paper presented at the 6th Mediterranean Conference on Information Systems (MCIS), Limassol, Cyprus.

Wang, W., He, L., Wu, Y. J., & Goh, M. (2021). Signaling persuasion in crowdfunding entrepreneurial narratives: The subjectivity vs objectivity debate. Computers in Human Behavior, 114, 106576.

Wang, W., Xu, Y., Wu, Y. J., & Goh, M. (2022). Linguistic understandability, signal observability, funding opportunities, and crowdfunding campaigns. Information & Management, 103591, 103591.

Wang, X., Guo, J., Wu, Y., & Liu, N. (2020). Emotion as signal of product quality: Its effect on purchase decision based on online customer reviews. Internet Research, 30(2), 463–485.

Weathers, D., Swain, S. D., & Grover, V. (2015). Can online product reviews be more helpful? Examining characteristics of information content by product type. Decision Support Systems, 79, 12–23.

Wells, J. D., Valacich, J. S., & Hess, T. J. (2011). What signal are you sending? How website quality influences perceptions of product quality and purchase intentions. MIS Quarterly, 35, 373–396.

Wu, S., Liu, Q., Sun, B., & Zhao, X. (2019). Understanding the effect of task descriptions on user participation in crowdsourcing contests: A linguistic style perspective. Paper presented at the proceedings of the 52nd Hawaii international conference on system sciences.

Xiang, D., Zhang, L., Tao, Q., Wang, Y., & Ma, S. (2019). Informational or emotional appeals in crowdfunding message strategy: An empirical investigation of backers' support decisions. Journal of the Academy of Marketing Science, 47(6), 1046–1063.

Xie, Q. (2019). Error analysis and diagnosis of ESL linguistic accuracy: Construct specification and empirical validation. Assessing Writing, 41, 47–62.

Yang, J., Adamic, L. A., & Ackerman, M. S. (2008). Crowdsourcing and knowledge sharing: strategic user behavior on taskcn. Paper presented at the Proceedings of the 9th ACM conference on Electronic commerce.

Yang, K., Qi, H., & Huang, Q. (2021). The impact of task description linguistic style on task performance: A text mining of crowdsourcing contests. Industrial Management & Data Systems, 122(1), 322–344.

Yang, Y., Chen, P.-Y., & Pavlou, P. (2009). Open innovation: An empirical study of online contests. Paper presented at the ICIS 2009 Proceedings.

Yang, Y., Chen, P.-Y., & Pavlou, P. (2010). Managing open innovation contests in online market. Working paper.

Yang, Z., Liu, Q., Zhao, X., & Zhao, Y. (2023). Empirical evidence of idea generation in open innovation community. International Journal of Crowd Science, 7(1), 40–45.

Ye, H., & Kankanhalli, A. (2013). Leveraging crowdsourcing for organizational value co-creation. Communications of the Association for Information Systems, 33(1), 13.

Ye, H. J., & Kankanhalli, A. (2017). Solvers' participation in crowdsourcing platforms: Examining the impacts of trust, and benefit and cost factors. The Journal of Strategic Information Systems, 26(2), 101–117.

Zhao, Y., & Zhu, Q. (2014). Evaluation on crowdsourcing research: Current status and future direction. Information Systems Frontiers, 16(3), 417–434.

Zheng, H., Li, D., & Hou, W. (2011). Task design, motivation, and participation in crowdsourcing contests. International Journal of Electronic Commerce, 15(4), 57–88.

## AUTHOR BIOGRAPHIES

Shuang Wu is a Ph.D. student from the School of Management, Xi'an Jiaotong University. She received her master's degree from Central University of Finance and Economics. Her research interests include crowdsourcing, user-generated content and short video platforms. Her research has appeared in Information Systems Journal, Hawaii International Conference on System Sciences (HICSS) and Pacific Asia Conference on Information Systems (PACIS).

Qian Liu is an Associate Professor of China Center for Internet Economy Research at Central University of Finance and Economics, People's Republic of China. She received her Ph.D. in Business Administration from the School of Management at Xi'an Jiaotong University, People's Republic of China, in August 2016. Her research interests are in the areas of crowdsourcing and open innovation. Her research has appeared in Information & Management, Journal of the Association for Information Science and Technology, Information Systems Journal, Industrial Management & Data Systems, International Journal of Information Management.

Xin Zhao is a Professor of School of Economics and Management, Xi'an University of Technology, China. He received his Ph.D. degree from the School of Management of Xi'an Jiaotong University, China, in 2012. His current research interests focus on knowledge co-construction, knowledge creation, user behaviour of online community.

Baowen Sun is a Professor and the Dean of China Center for Internet Economy Research at Central University of Finance and Economics. He received his Ph.D. from the Central University of Finance and Economics in 2003, majoring in National Economics. His main research areas are e-commerce and internet economics, as well as crowd science. He is one of the initiators of the Association of Crowd Science and Engineering (ACE) and serves as an editorial board member for the International Journal of Crowd Science.

Xiuwu Liao received the Ph.D. degree in management science and engineering from the Dalian University of Technology, Dalian, China, in 2002. He is currently a Professor with the School of Management, Xi'an Jiaotong University, Xi'an, China. His current research interests include intelligent decision-making and machine learning, IT economics, social e-commerce. His papers published in Information Systems Research, INFORMS Journal on Computing, International Journal of Electronic Commerce, European Journal of Operational Research, and so on.

How to cite this article: Wu, S., Liu, Q., Zhao, X., Sun, B., & Liao, X. (2024). Attracting solvers' participation in crowdsourcing contests: The role of linguistic signals in task descriptions. Information Systems Journal, 34(1), 6–38. https://doi.org/10.1111/isj.12462

## APPENDIX A

Figures A1–A3 are presented to show the Home Page, the Task List Page, and the detailed page of a contest on epwk.com. These web pages are translated into English using translation plugins.

![](/api/attachments/VN2Z443D/fulltext/images/e594b187f2d5e72ba47b7dc42f40651ed3ae865aa17a136ee302c07dd5c4a08a.jpg)  
FIGURE A1 Home page of epwk.com.

Eye hospital logo design

![](/api/attachments/VN2Z443D/fulltext/images/3419f560d84f83e16507d407d20b983df4304327946abefeb8e938bd820d8980.jpg)  
FIGURE A2 Task list.

Why choose Yipin
Witkey

Free appointment

![](/api/attachments/VN2Z443D/fulltext/images/461b2fe94558de301247b4301b186737df88f0d45162e358a5f3b850ec401d4f.jpg)

![](/api/attachments/VN2Z443D/fulltext/images/3d6389c7216a716faa6f33145f86243559624d3060e90fefb36a78ef484b93a3.jpg)

![](/api/attachments/VN2Z443D/fulltext/images/e8c1b86ba2e55c5e23917dda730e7c7fae407ceedbd8ebd6d20345746f9e95b5.jpg)

No risk, full refund
reciation of the latest case
Zero submission and zero

![](/api/attachments/VN2Z443D/fulltext/images/8280642656ec753743d28ddb3e7684327ec163e21847f64c393283fc59e7f97d.jpg)

Bounty: ¥1000
Plans: 69

## Task requirement

![](/api/attachments/VN2Z443D/fulltext/images/a907b530ba75d54b5fd452c677d357569bab854a8ed8df7f7e9ab380990a63df.jpg)  
Xiamen Information Investment Co.,  
has gathered 4,108,897 professional LOGO design talents. If you are also seeking similar help, we can easily handle it for you!

Company name: Yiwu Mingsheng Eye Hospital Co., Ltd. The

Logo design, reflecting the elements of the ophthalmology hospital, not in the form of words, but can be symbols or letter combinations or patterns.

![](/api/attachments/VN2Z443D/fulltext/images/dc24b88017b42ecbd4c4d85c8116ab7947065d8083f3417c96abeb70a6baab3c.jpg)  
Check whether a trademark can be registered for free

Task Number: 872040

Zhejiang Pro...

Collection task

![](/api/attachments/VN2Z443D/fulltext/images/61263cc62881766b3b7f4f2dfd125eca88bb04c2e40d23c6d06ba82b2b6db654.jpg)

![](/api/attachments/VN2Z443D/fulltext/images/f4b7f981ecfb360b299128fb2c229afd99998fa0c4f0a8d9706fbf33c48b4ebd.jpg)

2020-06-20

![](/api/attachments/VN2Z443D/fulltext/images/38846d6fb0e275969e589a29cb9aaceaefe010e97ebb08354d846abd14eb52e4.jpg)

![](/api/attachments/VN2Z443D/fulltext/images/54145cf462387b1efae3b887472a25b495e78c2f30a1687c376639f901046d7e.jpg)

This task has ended

Task feedback

Task feedback

![](/api/attachments/VN2Z443D/fulltext/images/a78922be1a586a85a5f7acab6d8c331f928fa759771cdf2b07c694e95eecb8bd.jpg)

Task message

Real estate brokerage company logo design 64 bids

## Popular Q&A

Popular topics

1 What should be paid attention to in

6 logo design logo design issues?
