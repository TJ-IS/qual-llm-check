---
otero_id: 20272
otero_key: "B78YGFSS"
title: "Choosing Response Strategies in Social Media Crisis Communication: An Evolutionary Game Theory Perspective"
authors: "Lan Wang; Christoph G. Schuetz; Dahai Cai"
year: "2021"
journal: "Information & Management"
doi: "10.1016/j.im.2020.103371"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

Choosing Response Strategies in Social Media Crisis Communication: An Evolutionary Game Theory Perspective

Lan Wang, Christoph G. Schuetz, Dahai Cai

![](/api/attachments/B78YGFSS/fulltext/images/8aed3032029ae14fcd21e35ee7d14b230005ec6671d1743cb6ebfbca41ddbe77.jpg)

PII: S0378-7206(20)30309-8

DOI: https://doi.org/10.1016/j.im.2020.103371

Reference: INFMAN 103371

To appear in: Information & Management

Received Date: 9 January 2020

Revised Date: 16 September 2020

Accepted Date: 19 September 2020

Please cite this article as: Lan Wang, Christoph G. Schuetz, Dahai Cai, Choosing Response Strategies in Social Media Crisis Communication: An Evolutionary Game Theory Perspective, <![CDATA[Information & Management]]> (2020), doi: https://doi.org/10.1016/j.im.2020.103371

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2020 Published by Elsevier.

Choosing Response Strategies in Social Media Crisis Communication: An Evolutionary Game Theory Perspective

## Abstract

When a company experiences the proliferation of negative information on social media, typically as a result of an incident in the real world, the company must decide whether to react positively, such as by responding in a timely manner, disclosing the facts, or ofering an apology or compensation, or by reacting negatively with a denial or threat of legal actions. Before responding, the company should consider the potential impacts due to the diferent reactions of stakeholders. A company’s ideal choice of strategy during a social media storm depends on the costs of that strategy for the company and the likelihood that netizens will publicly condemn the company on social media. In this study, we employ a model based on evolutionary game theory to investigate crisis communication on social media. The results show that the company’s choice of response strategy influences the evolution of the strategy pursued by Internet users. In the base model, we consider three possible actions for netizens on social media in reaction to an incident: ignoring the incident, noticing the incident but staying silent, and condemning the company and transmitting negative information. Subsequently, we extend the base model to consider complex network structures and defensive behavior. We also studied real-world cases of social media crisis communication and conducted numeric simulations with diferent parameters in order to determine the evolutionary equilibrium in diferent situations, which may inform the crisis response strategy selected by companies.

Keywords: Social media crisis communication, Crisis communication response strategy, Evolutionary game theory

## 1. Introduction

Crisis communication is an increasingly important topic of interest in management research in areas including political crises [1], acts of terrorism [2], and natural disasters [3]. Due to the rise of social media on the Web, crisis communication on social media has attracted much attention from both industry and academia. Social media provides netizens with the ability to create contents and disseminate them rapidly among friends and followers, who may then share these contents with their friends and followers. The behavior of netizens in a crisis may have significant impacts on the reputation of an enterprise, where a real-world crisis often causes a secondary crisis in the realm of social media [4]. During a social media crisis, when negative opinions proliferated among netizens, an enterprise may select diferent strategies that lead to the loss of reputation to diferent extents [5, 6]. An enterprise’s choice of strategy during a crisis afects the corporate governance structure [7] and overall economic performance of the enterprise [8].

In practice, due to a lack of reliable guidance, crisis managers often adopt an opportunistic approach, such as trying to limit negative media coverage [9] or pursuing private settlements with complainants, which may lead to the spread of negative opinions regarding the enterprise on social media spiraling out of control, thereby further damaging the enterprise’s reputation [4]. For example, the United Express Flight 3411 incident in April 2017 [10, 11, 12] may serve as a cautionary tale for executives who might be thrust into the role of crisis manager. United Airlines was faced with a deluge of negative posts online following the release of a video showing the rude and violent treatment of a passenger. The passenger was removed from th airplane in order to clear the seat for crew members who needed to relocate to another airport. In its initial statement, the airline failed to apologize for its mistakes and even referred to the passenger as “disruptive and belligerent” in an internal communication that eventually leaked to the public, thereby creating further uproar on social media and a loss of reputation for the company.

#

Research into social-mediated crisis management (SMCM) emphasizes the importance of adjusting the traditional perspective that is centered on the enterprise and inferring the stakeholder’s reaction based on the enterprise’s (perceived) responsibility in the event of a crisis [4] in favor of a view of crisis management that considers the interaction between the enterprise and stakeholders (netizens in this case) as a form of negotiation [13]. For example, in the traditional approach, a company may consider itself as not being responsible for a crisis, thereby assuming that the public will not blame the company, which may deviate from reality, especially on social media. Thus, the enterprise should actively observe the behavior of netizens and listen to their values before choosing an appropriate response strategy that balances the interests of both the netizens and the enterprise [14]. The response of the enterprise to a crisis on social media may then prompt netizens to change their initial behavioral strategies. Therefore, in this study, we propose an evolutionary game model to answer the following questions.

1. During a social media crisis, how does the response strategy adopted by an enterprise afect the strategy selected by netizens?

2. What is the optimal strategy for social media crisis communication by an enterprise in diferent situations?

Following the publication of negative information, netizens may ignore or silently acknowledge the negative information, and also further disseminate negative opinions on social media. In some cases, netizens might even defend the enterprise. The response of the enterprise to a crisis influences the subsequent loss of reputation. A negative reaction where the company tries to prevent the proliferation of negative opinions by deleting posts and possibly even pursuing legal action may lead to a huge loss of reputation for the company, which subsequently translates into a financial loss for the company. However, a positive reaction where the company embraces the negative situation by disclosing the full facts and possibly even ofering compensation also has costs, such as in terms of promotional activities, investments in customer service, or recalling a product.

In this study, we present an evolutionary game model that focuses on the evolution of the strategies adopted by the enterprise and netizens in diferent social media crisis situations. In this model, when an enterprise experiences a crisis on social media, the enterprise can select a positive or negative strategy. Netizens can react to an incident in three diferent ways in the basic model: by ignoring the incident, staying silent, or condemning the enterprise and transmitting negative information. Each of these strategies is chosen by a certain proportion of netizens. We extend the basic model to account for strategy learning efects by assuming that the strategy selected by individual netizens is influenced by other individuals in the social network. An adapted Fermi function is used to model the strategy learning process in complex networks. Diferent types of networks such as small-world networks with diferent characteristics, e.g., diferent clustering coeficients, can have diferent efects on strategy learning. We further extend the model to account for the possibility of netizens defending the enterprise. We also considered prominent real-world cases of crisis communication based on the proposed model and employed these cases as the starting points for numeric simulations to determine the equilibrium for strategies, given diferent parameter values. In order to estimate the parameter values for the diferent cases, we referred to informative resources and conducted sentiment analysis based on tweets. The equilibria determined in these simulations may help practitioners to determine a company’s optimal strategy when experiencing a crisis on social media, which depends on the costs of the respective positive or negative response, as well as the likelihood of netizens venting their frustration online.

The remainder of this paper is organized as follows. In Section 2, we review related research into (social media) crisis communication and game theory. In Section 3, we present an analysis of social media crisis communication based on evolutionary game theory. In Section 4, we introduce possible extensions to the proposed evolutionary game model by considering a complex network structure and defensive strategy. In Section 5, we present investigations of prominent cases of social media crisis communication based on the proposed evolutionary game model. In Section 6, we present the results obtained in the numeric simulations, where these cases were then used as the starting points for the simulations to obtain estimates of the model parameters. In Section 7, we discuss the model and its extensions. We conclude by suggesting the implications of our findings for practitioners and researchers.

#

## 2. Related Work

In this section, we review related research into crisis communication on social media, crisis communication response strategies, and netizen behavior during a social media crisis. We summarize previous research into crisis communication by emphasizing the influence of social media, and the interested reader may refer to Cheng’s [15] review of the impact of social media on crisis communication for a more comprehensive overview. We also provide background information regarding evolutionary game theory, which is the basis for our model of social media crisis communication.

## 2.1. Crisis Communication on Social Media

Classical crisis communication theories [16, 17] define crisis as an event that is not predictable, disrupts stakeholder expectations, and adversely afects an organization’s performance. Hence, traditional crisis communication research emphasizes organizations by focusing on the communication of crisis response information from the organization to stakeholders [18, 19]. In this approach, the stakeholder is largely passive, a target of crisis communication, and recipient of messages from the organization, and organizations use crisis communication to repair their image [19] and their bad reputations in the wake of a crisis [20].

Social media has considerably impacted crisis communication by organizations (cf. [15]). Coombs has identified social media as the “driving force in the bleeding edge of crisis communication” [21]. A recent review [15] showed that a third of the diferent types of crises discussed on social media were about mismanagement, and companies are among the main types of organizations involved, while stakeholders and their behaviors on social media have become an important research topic. Research into SMCM has extended the technical methods for implementing crisis communication to online chat rooms and social media while adjusting some traditional crisis communication strategies [22, 23]. Cheng [15] found inconsistencies in traditional crisis communication studies [24, 19, 25, 26] regarding the efects of specific response strategies.

At present, netizens are presented with unprecedented opportunities and capabilities regarding the expres sion and communication of opinions toward various issues. Thus, netizens can create and disseminate content on social media [27, 28], thereby resulting in the rise of potentially complex risks for crisis communication. Netizens who disseminate information about a crisis may also post negative comments online about the organization involved in the crisis, which is defined as secondary crisis communication (SCC) [4, 17, 6]. Secondary crisis communication and the reactions of stakeholders to it, e.g., willingness to boycott [4], may have severe adverse efects on an organization, potentially damaging the enterprise’s reputation with the stakeholders as well as reducing the value of a company and its profits [17]. The SCC process on social media is highly dynamic and it evolves rapidly, which means that the time left for organizations to respond to the crisis is shortened [29]. In a crisis, stakeholders are influenced by the source of an information, i.e., third party or organization, and the form of communication, e.g., word-of-mouth, social media, or traditional media [30, 31]. In addition, social media bestows non-negligible power upon netizens who achieve agenda-setting abilities through the use of social media, thereby allowing them to push enterprises to accept the demands of stakeholders [32, 33, 34].

Previous studies [15, 33, 34, 35] have called for more attention to the actions of netizens on social media. Some characteristics of the community of netizens have been verified, such as a lack of leadership and possibly intense reactions to real-world incidents [32, 36]. Social media provides organizations with the tools not only to keep in touch with their stakeholders through eficient, low-cost communication channels [37], but also to monitor the opinions held by stakeholders as well as their emotions and behavioral trends during a crisis by analyzing large volumes of data, which may serve as the fundamental basis of crisis communication.

Studies of SMCM have noted the importance of the interactions between enterprises and stakeholders, but there are no clear principles regarding how to make appropriate crisis response decisions. Counterproductive crisis communication will lead to greater crises, which spread rapidly throughout the vast and easy-to-use social media networks [38].

## 2.2. Crisis Communication Response Strategy

Crisis communication must be viewed in the wider context of the more general areas of communication policy and strategy with the aim of more efectively and eficiently influencing the development of the

#

public’s opinion on matters of importance to organizations [24]. Multiple theories and models of crisis management have been proposed, with the aim of assisting organizations with damage control during a crisis. In particular, three types of communication strategies have been identified, comprising instructing information, adjusting information, and internalizing information [24]. An empirical study [39] investigated the five potential responses to a crisis, i.e., no response, denial, excuse, justification, and concession, and concluded that concession was the most efective response option in the face of a crisis. Other widely known crisis communication theories include image repair theory (IRT) [19] and situational crisis communication theory (SCCT) [5].

Image repair theory focuses on the crisis communication strategies that an organization should adopt, rather than simply describing crisis situations [19]. Image repair theory provides a set of “image repair” strategies [19], including denial, evasion of responsibility, reducing the ofensiveness of the event, corrective action, and mortification. The first category comprising denial may involve simple denial of the incident or an attempt to divert the blame to another party. The second category comprising evasion of responsibility aims to minimize the perceived responsibility of the organization involved in the incident. In this case, four situations are distinguished as provocation, defeasibility, accidental, and good intentions. The third category comprising reducing the ofensiveness includes strategies such as bolstering, minimization, diferentiation, transcendence, attacking the accuser, and compensation. The fourth category comprising corrective action involves the organization attempting to find a solution to the problem while pledging to prevent the reoccurrence of the incident. Finally, the use of a mortification strategy allows the organization to admit its responsibility and issue a public apology.

Criticism of the IRT is based on the lack of evidence to support the efectiveness of the crisis communication strategies proposed by the IRT [40]. Image repair theory has also been found to provide no clear suggestions regarding specific strategy choices in the context of a certain crisis [15].

Situational crisis communication theory argues that the choice of the response strategy to a crisis is influenced by the organization’s responsibility for the crisis. Depending on whether the public attributes responsibility for a crisis to the organization, another party, or higher forces, SCCT identifies three crisis clusters: intentional cluster, victim cluster, and accidental cluster [5]. Coombs [41] listed the response strategies in order of the accommodative level from denial and diminishing to rebuilding and bolstering. The specific strategies mainly involve attacking the accuser by confronting a person or a group that criticizes the organization, asserting and insisting that no crisis actually exists, shifting blame for a crisis to a scapegoat, issuing an excuse by denying any intent to cause harm and/or claiming that the events triggering the crisis were outside the organization’s sphere of influence, justifying the actions and thus trying to minimize th damage, ofering compensation, i.e., money or in-kind benefits to victims, and apologizing, i.e., admitting the organization’s responsibility in the crisis situation while asking for forgiveness from the stakeholders [5].

Further research into SCCT based on experiments or case analyses has also confirmed that the crisis response strategy has a significant impact on organizational reputation [16]. In terms of strategic applications, the reputations of organizations that follow a rebuild strategy in response to a crisis appear to be generall more positive than those of organizations that follow a diminish strategy [42]. Other studies added response strategies in crisis communication, such as separation, i.e., the organization disconnecting from the responsible parties within their organization [43], ignorance, i.e., disregarding a crisis [44], and endorsement, i.e., gaining and highlighting support for the organization from third parties [45]. In addition, several studies have criticized the SCCT. From a historical and ethical perspective, the scapegoating response strategy should be removed from the canon of crisis communication strategies [46]. Criticism of SCCT has also focused on the lack of full investigations of media influence, especially the efects of social media on crisis communication [47].

By focusing on the perspective of the organization, SCCT ignores the viewpoint and response strategies of stakeholders during a crisis [15]. Situational crisis communication theory implicitly assumes that the stakeholders involved in a crisis can accurately and fairly attribute responsibility in a crisis, and the enterprise subsequently chooses the appropriate strategy according to the scenario, i.e., victim cluster or accidental, which reflects the diferent degrees of responsibility that an organization may have in a crisis. The assumption of accurate and fair attribution of responsibility may hold in the case of direct stakeholders who directly experience the crisis event or know the details. However, on social media, in the presence of a secondar crisis, netizens who lack the required information and investigative abilities will find it dificult to correctly

#

attribute responsibility, e.g., netizens may misinterpret and not correctly understand all the facts related to a crisis gathered from the news or generated by other stakeholders on social media [48, 5]. Furthermore, it may not always be the case that netizens are impartial considering that netizens comprise a heterogeneous group of individuals who possibly have quite diferent personal preferences and individual desires. Consequently, the application of SCCT strategies may not lead to the expected and desired results. From a practical perspective, the enterprise must understand the wishes of netizens and their reactions to the organization’s crisis communication, thereby allowing the organization to optimize its crisis communication strategy [15]. Coombs [5] argued that all specific crisis communication strategies lie essentially somewhere between pure advocacy that only addresses the concerns of the organizations and the total accommodation of stakeholder interests. No consensus exists on the correct positioning of a specific strategy (cf. [15]), as shown by some contradictory research conclusions [24, 19, 25, 26]. Recent studies have also focused on the dynamics of crisis communication strategies. The enterprise may choose any strategy in a specific crisis context to select its position on the “advocacy-accommodation continuum” [5, 15]. In order to avoid excessive involvement with specific technical forms of strategies and to highlight the key trade-of for enterprises, we simplify the crisis communication strategies of enterprises as negative and positive, which represent a larger tendency to advocacy and a larger tendency to accommodation, respectively, in order to analyze the basic principles of crisis communication decision making.

## 2.3. Behavior of Netizens in a Social Media Crisis

The stakeholders in a crisis and the usage of media by these stakeholders have become the main focus of research in crisis communication [15]. The influence on the enterprise is an important criterion for measuring the importance of a stakeholder. In the era of social media, netizens have an important influence on enterprises.

During a crisis, the stakeholders (netizens) use social media likes, tags, tweets, shares, votes, etc., to indicate the relevance of an opinion as well as to seek and share information, and for emotional venting/support [47]. Netizens are concerned about the actual or potential damage to their interests, or they may be dissatisfied with the deviation between the status quo and the ideal state after the crisis. They expect desirable crisis communication from an enterprise (e.g., bolstering, compensation, or apology) [36]. Netizens want to achieve their expectations but due to the lack of unified organization [32] and the dificulty predicting the reactions of enterprises, the expectations of netizens and their expressions or actions are diferent, where they may b mild or active, and even radical, e.g., keeping track of progress, comments, and strong accusations. Studies have noted the diferent degrees of involvement by stakeholders in a crisis [35]. Modern technology greatly facilitates individual expression but focusing on one topic or taking an active part still requires expending time and energy, thereby constraining the persistence of the corresponding behaviors. Emotional factors such as anger and disappointment also afect the acceptance of crisis communication results among netizens [49]. Moreover, an individual netizen has an incentive to learn (emotionally) more profitable action strategies by observing others. Therefore, the behavioral trends of netizens may change constantly, with diferent action strategies and mutual learning. The attribution of responsibility for a crisis is not necessarily perfect among netizens, but a study showed that compared with information channels, diferent degrees of responsibility only have a weak influence on the efectiveness of crisis communication strategies [25]. An organization must trade of the cost with the actual efect of its strategies, as well as considering the impact of changes in behavioral trends among netizens on reputational loss.

Decision making by netizens is also influenced by bounded rational behavior in the learning process. An abundance of empirical evidence suggests that bounded rationality is important for decision making [50]. Individuals have limited cognitive and computational abilities, so the behavioral decisions of individuals will b bounded rational. Individuals have objective rationality but due to the complex, diverse, and uncertain social reality, their limited cognitive abilities mean that individuals will only achieve a satisfactory solution [51]. In practice, especially in a complex and diverse environment, human decisions can only lead to a satisfactory rather than optimal solution due to the limited capability of humans for processing information [51]. When netizens learn to optimize their action strategies through observation, they may not observe all of the information but instead they acquire it from limited channels due to their limited information resources, cognitive abilities, time, and energy. Moreover, benefits and losses are sometimes dificult to measure, especially when they involve emotional factors. However, previous crisis communication studies have paid little attention to the evolution of the strategic choices of netizens under bounded rationality.

## 2.4. Evolutionary Game Theory

Game theory is a mathematical method employed in operations research to study competitive phenomena that involve benefits for the diferent parties. Game theory considers the predicted and actual behaviors of individuals in a “game” and studies the optimization strategies of the individuals involved [52, 53]. Game theory can be used to analyze the choices and decisions of participants from a cost–benefit perspective.

Traditional game theory aims to analyze the optimal behavior of participants assuming that the participant are all completely rational [52, 54]. The extension of the traditional game model to account for the heterogeneous beliefs of participants is more aligned with the real nature of human beings, where the participants are not treated as perfectly rational beings. The subjects have bounded rationality, i.e., th cognitive abilities of individuals influence the choice of the strategy to maximize their interests [55].

Subsequently, concepts from evolutionary theory also influenced the study of game theory. In the continuous development of nature (human society), learning behaviors occur among individuals, which allow them to constantly adjust and improve their own behaviors to evolve to a higher level. Evolutionary game theory focuses on analyzing how bounded rational group participants can reach a stable equilibrium through the learning and imitation process [56, 57]. The evolutionary game replicator dynamics function is applied to socio-economic problems. Diferent strategies have specific strategy learning obstacles, which led to the proposal of a general replicator dynamic model [58, 59]. From the perspective of evolutionary games, social media crisis events involve the group behavior of parties that seek to change the rules of the game under an internal crisis and external impact. Among the participants, each individual observes the previous actions of others and replicates the actions of others according to a rule. The most eficient strategies will be replicated and the underperforming strategies are eliminated, thereby resulting in a stable distribution. Information exchange within the netizen group afects evolution toward convergence on a stable equilibrium through learning and imitation processes [59].

Previous studies were mainly based on case analysis or experimental methods, whereas the game behavior of organizations and stakeholders in the crisis communication process has rarely been studied. However, the behavior of netizens during a crisis will afect the losses of the organization and the corporate response strategies will also influence the behavioral choices of netizens. Game theory can be implemented to allow the crisis communication strategy choices to be considered from a cost–benefit perspective for both the enterprise and netizens.

## 3. Evolutionary Game Model

In this section, we present a model for social media crisis communication based on evolutionary game theory. First, we introduce the basic definitions and assumptions before explaining the model parameters. We then analyze the evolution process for the strategies of the players involved. The proposed model explains the strategy choices for players in diferent situations, and helps inform the decision made by an enterprise regarding how to respond to a crisis on social media. However, we share the SCCT’s view that enterprises should assume social responsibility after a crisis event, e.g., by mitigating risks to the public, before focusing on considering how to repair their reputation [5].

## 3.1. Basic Definitions and Assumptions

In the following, we describe the assumptions underlying the proposed evolutionary game model by referring to the players involved and their strategic choices.

Assumption 1. The game model comprises an enterprise involved in a crisis event and a group of heteroge neous netizens who select diferent action strategies. Individuals have limited cognitive and computational abilities, so the behavioral decisions of netizens are bounded rational (cf. [51], see Section 2.3). Netizens take action on social media first and the enterprise decides about the crisis communication response strategy after observing the netizens. Subsequently, netizens reevaluate their action strategies in response to the enterprise’s strategy.

#

We consider that the enterprise’s response strategy is based on observations of the strategies adopted by netizens. Owing to the complexity and dynamics of the actions of netizens, previous studies suggest that any crisis response should be made after observing and understanding the desires of stakeholders in order to avoid blind, counterproductive strategies [60, 15]. In particular, on social media, the enterprise can evaluate the potential damage caused by a crisis and adopt the optimal strategy by analyzing the data generated by netizens to conduct research into public opinion and prevalent emotions [61]. In addition, the time window before the crisis becomes widely known has been shortened by the emergence of digital media and modern communication technologies, thereby reducing the ability of the enterprise to act before widespread reaction from the public [29]. In particular, a survey of theories regarding crisis communication strategy in traditional crisis management and SMCM research showed that most strategies are designed to be used when the public has noticed the crisis [15].

Assumption 2. Netizens have an action set {I, S, T }, and each strategy can be adopted by a proportion of netizens. The I strategy refers to netizens not being concerned about or ignoring the crisis and the enterprise’s action. Netizens following the I strategy have no apparent behavior regarding the crisis and they do not even talk about it. The S strategy refers to netizens caring about the crisis but not expressing opinions on social media, i.e., netizens are still in “quiet mode.” The T strategy refers to the netizens paying attention to the crisis and actively expressing their concerns, appeals, and expectation, such as blaming/condemning the enterprise or transmitting their negative opinions. The proportions of netizens who follow the S and T strategies may be inferred from statistics related to messages, pictures, and videos posted on Twitter, Facebook, YouTube, etc., which indicate the number of people who have read or commented on the post.

Assumption 3. The enterprise has an action set {P, N }. The P strategy refers to the enterprise adopting a positive and open attitude when dealing with negative information, such as a timely response, disclosure of facts, apologies or sympathy, and corrective actions or improvements. The P strategy involves actively responding to netizens, thereby yielding emotional or financial benefits for netizens. The potential implemen tations and efects of the P strategy are diverse due to the diferent expectations of netizens, which might range from a simple demand for information about the crisis to actual (financial) compensation for damage to the public. Consequently, the cost of the P strategy also varies according to the diferent expectations of netizens. The cost of the P strategy comprises the (immaterial) costs of a simple expression of intent to improve, e.g., in the form of a public commitment statement, but also the actual financial costs incurred to actually address the concerns of netizens, e.g., paying for improvements in business policies. The N strategy refers to the enterprise adopting “tough and rude attitudes” by attacking the accuser, denying the truth or refusing to publish it, presenting a scapegoat, or not responding. The N strategy does not efectively respond to the expectations of netizens or address their concerns, and it yields no actual benefits for netizens. The N strategy does not require real efort by the enterprise, except for small social costs, e.g., issuing a perfunctory apology. In the case of the N strategy, we assume that both the benefits to the netizens and the costs for the enterprise are 0 in order to simplify the analysis.

In reality, an enterprise may employ a multitude of specific strategies for crisis communication. In order to avoid excessive involvement in the specific technical details and to highlight the crucial trade-of for enterprises, we abstract from the specific response methods by considering two broad strategy options as negative and positive. The former strategy represents the broader tendency of the enterprise to take a stance of advocacy (defending itself), whereas the latter involves taking the stance of accommodating the demands of netizens (listening to netizens). Accommodation reflects the level of willingness by the enterprise to assume responsibility beyond that required by law and to meet the expectations of netizens, thereby indicating the scale of the substantial benefits that the enterprise will cede to netizens.

The enterprise may also choose to pursue no action at all in response to a crisis. From a cost–benefit perspective, we consider that taking no action at all can be classified as a negative response because there are no actual benefits for netizens. Thus, inaction is essentially similar to perfunctory apologies, sophistry, and even proposing reverse charges. Furthermore, on today’s social media, no response can easily be interpreted as a negative response by both netizens and media commentators.

Table 1: Descriptions of model parameters

<table><tr><td>v</td><td>Total value that is at stake for the enterprise, e.g., the enterprise&#x27;s revenue.</td></tr><tr><td>c1</td><td>Cost of the P strategy for the enterprise, including apology and explanation, in the case where netizens choose the I or the S strategy.</td></tr><tr><td>c2</td><td>Cost of the P strategy for the enterprise, including apology and explanation, in case where netizens choose the T strategy.</td></tr><tr><td>d1</td><td>Cost of the S strategy for netizens, including time and emotional costs.</td></tr><tr><td>d2</td><td>Cost of the T strategy for netizens, including time and emotional costs. We assume that d2 &gt; d1.</td></tr><tr><td>r1</td><td>Loss by the enterprise including the loss of reputation in the case where netizens choose the S strategy and the enterprise chooses the N strategy.</td></tr><tr><td>r2</td><td>Loss by the enterprise, including the reputational loss, in the case where netizens choose the T strategy and the enterprise chooses the P strategy. We assume that r2 &gt; r1.</td></tr><tr><td>r3</td><td>Loss by the enterprise, including the reputational loss, in the case where netizens choose the T strategy and the enterprise chooses the N strategy. We assume that r3 &gt; r2.</td></tr><tr><td>θI</td><td>Proportion of netizens who choose the I strategy in response to negative information on social media. θI ∈ [0, 1].</td></tr><tr><td>θS</td><td>Proportion of netizens who choose the S strategy in response to negative information on social media. θS ∈ [0, 1].</td></tr><tr><td>θT</td><td>Proportion of netizens who choose the T strategy in response to negative information on social media. θT ∈ [0, 1], θI + θS + θT = 1.</td></tr></table>

## 3.2. Model Parameters

In the case of an online dispute on social media between netizens and an enterprise following the publication of negative information about the enterprise, both players incur diferent costs depending on the strategies adopted. For netizens, these costs mainly comprise emotional costs and the investment of time. The cost for netizens depend on the strategy selected: I, S, or $T .$ The costs may be financial for the enterprise, e.g., the costs of additional promotional activities or providing compensation. However, the costs may also include a loss of reputation, which depends on the strategy adopted by the enterprise and the behavior of netizens. Table 1 lists the model parameters and explanations for each parameter. Netizens can be divided into groups that adopt the I, S, or T strategy. The proportions of netizens that adopt a respective strategy are represented by the parameters $\theta _ { I } , \theta _ { S }$ , and $\theta _ { T }$

Figure 1 illustrates the costs for the netizens and enterprise according to the strategy adopted by netizens and the response of the enterprise. For netizens who ignore or do not care about the negative information, there are zero costs and benefits regardless of the subsequent response by the enterprise. For the enterprise, if netizens ignore the negative information, a negative response incurs no costs, including reputational loss for the enterprise, but a positive response diminishes the value v for the enterprise, e.g., the enterprise’s revenue, by the amount $c _ { 1 }$ . For netizens who pay attention to negative information but without taking to social media to condemn the enterprise, the costs $d _ { 1 }$ of the S strategy in the case of a positive response by the enterprise are reduced by the costs incurred $c _ { 1 }$ for the enterprise assuming that the value spent by the enterprise translates into direct or indirect benefit for the netizens, e.g., promotional activities or an increas in the emotional well-being of netizens after knowing that justice has been served. The value at stake for the enterprise is reduced by the cost of the positive response. In the case of a negative response by the enterprise, the costs of netizens are not reduced and the value at stake for the enterprise decreases by $r _ { 1 }$ , mainly in the form of reputational loss.

For netizens who observe the negative information and choose to further condemn and transmit it, the emotional and time costs $d _ { 2 }$ are reduced by the value $c _ { 2 }$ in the case of a positive response by the enterprise. For the enterprise, the value at stake is then reduced by the costs $c _ { 2 }$ of the $P$ strategy as well as the reputational loss $r _ { 2 } .$ . In the case where the enterprise adopts a negative strategy, the reputational loss $r _ { 3 }$ reduces the value at stake for the enterprise.

Netizens with greater expectations regarding the enterprise, and thus higher emotional or financial costs, are more involved in crisis matters. In order to satisfy netizens with greater involvement in a crisis, an enterprise must take firm positive action. When the enterprise positively responds, netizens with low expectations (or no expectations at all) may be satisfied with the status quo and no longer have a negative opinion of the enterprise, but netizens with high expectations still regard the crisis event as a stain on the reputation of the enterprise. When the enterprise negatively responds, netizens with higher expectations regarding the enterprise will generally feel disappointed, where the degree of disappointment and the corresponding loss of reputation for the enterprise are positively correlated with the level of expectation.

The formation of the initial distribution of strategies pursued by the heterogeneous group of netizens is not explained in the present study. The distribution may be related to the enterprise’s responsibility, past reputation, and history of crises, as mentioned by SCCT [5]. For example, an empirical study demonstrated that the social performance of an enterprise at the beginning of a crisis has a positive efect on the enterprise’s financial performance [62]. The precise distribution of strategies will of course remain unknown to companies, but we consider that good estimates can be obtained relatively easily for the initial proportions of the strategies adopted given the prevalence and public nature of social media data. Thus, an enterprise can observe the number of posts about an incident as well as the total views of posts on social media.

![](/api/attachments/B78YGFSS/fulltext/images/c0a1b4a5d92db24450459b8a1bb80ff39693095b61f76cb1853ab1837ef5f88e.jpg)  
Figure 1: Dynamic game model of crisis communication on social media.

## 3.3. Generalized Replicator Dynamics Equation

We analyze the evolution of the imitative behavior of netizens on social media based on the replicator dynamics equation from evolutionary game theory [58, 59]. We refer to the following equation as the model’s learning rule, where it models the evolution of a netizen’s strategy choice based on observations of the strategy choices of other netizens.

$$
\frac {\partial \theta_ {f}}{\partial t} = \theta_ {f} [ u (f, t) - \bar {u} (t) ]\tag{1}
$$

The function $u ( f , t )$ denotes the utility of $\mathrm { a }$ particular strategy $f$ at time $t ,$ and $\bar { u } ( t )$ denotes the average utility of all the strategies over all individuals at time t. It should be noted that the average utility u¯ depends on the strategy distribution ratios, which change over time. The variable $f$ refers to the $I ,$ S, or $T$ strategy. In evolutionary game analysis, we can use Equation 1 to find evolutionary equilibira. The change in the proportion of a strategy over the course of evolution is related to the diference between the strategy’s returns and the average returns of all the strategies. In particular, if a strategy’s utility is lower than the average utility of strategies over the course of evolution, then the proportion of that strategy will gradually decrease until it is zero. $\mathrm { B y }$ contrast, if a strategy’s utility is greater than the average utility of strategies over the course of evolution, then the proportion of that strategy will gradually increase and become an equilibrium strategy.

We now consider the proposed evolutionary game model for crisis communication on social media and substitute the elemental game revenue function into the generalized replicator dynamics equation. It should be noted that for brevity, we omit t in the utility functions $u ( f , t )$ and $u \bar { ( t ) }$ , and write $u ( f )$ and u¯ instead in the following analysis. We then calculate the proportional distribution of the various strategies of netizens according to Equation 1. In particular, we distinguish two diferent situations.

## 3.3.1. Situation 1: Netizens Pursue I and S Strategies Only

In general, under the assumption that netizens adopt $I , S ,$ , and $T$ strategies, if the enterprise adopts the $P$ strategy, then the expected utility $U _ { P }$ for the enterprise depends on the proportions of netizens who choose the $I , S$ , and $T$ strategies, respectively, as follows.

$$
U _ {P} = \theta_ {I} (v - c _ {1}) + \theta_ {S} (v - c _ {1}) + \theta_ {T} (v - c _ {2} - r _ {2})\tag{2}
$$

Similarly, if the enterprise adopts the N strategy, then the expected utility $U _ { N }$ is defined as follows:

$$
U _ {N} = \theta_ {I} v + \theta_ {S} (v - r _ {1}) + \theta_ {T} (v - r _ {3})\tag{3}
$$

If $\theta _ { T } = 0$ , the netizens do not publicly criticize the enterprise and the proportional distribution of the $I ,$ $S ,$ and $T$ strategies is $( \theta _ { I } , \theta _ { S } , 0 )$ . Now, by comparing the values of $U _ { P }$ and $U _ { N }$ , if netizens choose only the I and S strategies, then we note that $U _ { P }$ is greater than $U _ { N }$ if: first, the cost $c _ { 1 }$ of the $P$ strategy for the enterprise is first smaller than the loss $r _ { 1 }$ of the enterprise when choosing the $N$ strategy while the netizens observe the negative information but stay silent; and second, the proportion of netizens who observe the negative information but stay silent is greater than the ratio of $c _ { 1 }$ to $r _ { 1 }$ . By contrast, $U _ { P }$ is smaller than $U _ { N }$ if the ratio of $c _ { 1 }$ to $r _ { 1 }$ is greater than the proportion of netizens who observe the negative information abou the enterprise or the cost of the $P$ strategy is higher than the loss in case of the $N$ strategy.

$$
\left\{ \begin{array}{l l} U _ {P} > U _ {N} & \text {if c_{1} <  r_{1} and \theta_{S} >c_{1} /r_{1}} \\ U _ {P} <   U _ {N} & \text {if (c_{1} <  r_{1} and \theta_{S} <  c_{1} /r_{1}) or c_{1} >r_{1}} \end{array} \right.\tag{4}
$$

We now determine the strategy equilibrium for the netizens by comparing the utilities $U _ { P }$ and $U _ { N }$ of the enterprise’s two strategy choices. If $c _ { 1 } < r _ { 1 }$ and $\theta _ { S } > c _ { 1 } / r _ { 1 }$ , i.e., $U _ { P } > U _ { N }$ , then the enterprise adopts the P strategy and in case where the netizens only pursue the I and $S$ strategies, the average utility u¯ of the strategies for netizens is defined as follows.

$$
\bar {u} = \theta_ {I} \cdot 0 + \theta_ {S} (- d _ {1} + c _ {1})\tag{5}
$$

$$
\partial \theta_ {I} / \partial t = \theta_ {I} [ u (I) - \bar {u} ] <   0, \theta_ {I} \rightarrow 0\tag{6}
$$

$\partial \theta _ { I } / \partial t < 0$ means that the proportion of netizens who adopt the I strategy will decrease and approach 0 during the course of evolution. Similarly, $\partial \theta _ { S } / \partial t > 0$ means that the proportion of netizens who adopt the S strategy will increase and approach 1 during the course of evolution, i.e., $\theta _ { S }  1$

Inference 1. If the netizens choose the S strategy and the cost of the P strategy for the enterprise is less than the loss of the N strategy, then the enterprise will finally adopt the P strategy. In this case, the S strategy distribution for the netizens approaches 1. The proportion of the final strategy for the netizens will be afected by the proportion of each strategy in the initial state. The resulting strategy equilibrium is the S strategy for the netizens and the P strategy for the enterprise, i.e., the equilibrium is (S, P ).

If $c _ { 1 } < r _ { 1 }$ and $\theta _ { S } < c _ { 1 } / r _ { 1 } , \mathrm { i . e . , } U _ { P } < U _ { N }$ , then the enterprise adopts the N strategy and the average utility ¯u of the strategies for netizens is defined as follows:

$$
\bar {u} = \theta_ {I} \cdot 0 + \theta_ {S} (- d _ {1})\tag{7}
$$

$$
\partial \theta_ {I} / \partial t = \theta_ {I} [ u (I) - \bar {u} ] = \theta_ {I} \theta_ {S} d _ {1} > 0, \theta_ {I} \rightarrow 1\tag{8}
$$

The proportion of netizens who adopt the I strategy approaches 1. Similarly, $\theta _ { S }  0 , \mathrm { i . e . }$ ., the proportion of netizens who adopt the S strategy is close to 0.

Inference 2. In the case where $c _ { 1 } < r _ { 1 }$ and $\theta _ { S } < c _ { 1 } / r _ { 1 }$ , the enterprise adopts the N strategy and the netizens tend to choose the I strategy. If the proportion of netizens who choose the S strategy is small in the initial state, then the netizens will tend to choose the I strategy. The resulting strategy equilibrium is (I, N ).

3.3.2. Situation 2: Netizens Pursue I, S, and T Strategies

If $\theta _ { T } > 0 .$ , then some of the netizens will publicly condemn the enterprise in negative comments and repost negative content on social media. In this case, the distribution of the strategies adopted by the netizens is $( \theta _ { I } , \theta _ { S } , \theta _ { T } )$

If the loss $r _ { 3 }$ for the enterprise that chooses the N strategy under a T strategy pursued by netizens is small, i.e. $, r _ { 3 } < ( c _ { 1 } - r _ { 1 } \theta _ { S } ) / \theta _ { T } + r _ { 2 } + c _ { 2 } - c _ { 1 }$ , then the loss caused by the N strategy is manageable for the enterprise, and thus the condemnation of by netizens has little impact on the reputation of the enterprise. In this case, the enterprise adopts the N strategy and we can determine the equilibrium strategy of netizens by comparing the benefits of the three strategies for the netizens.

$$
\partial \theta_ {I} / \partial t = \theta_ {I} [ - \theta_ {S} (- d _ {1}) - \theta_ {T} (- d _ {2}) ] > 0\tag{9}
$$

The proportion of netizens who adopt the I strategy will increase.

$$
\partial \theta_ {T} / \partial t = \theta_ {T} [ - \theta_ {S} (- d _ {1}) + (1 - \theta_ {T}) (- d _ {2}) ] <   0\tag{10}
$$

The proportion of netizens who adopt the T strategy will decrease.

$$
\partial \theta_ {S} / \partial t = \theta_ {S} [ (1 - \theta_ {S}) (- d _ {1}) - \theta_ {T} (- d _ {2}) ]\tag{11}
$$

If the following condition holds:

$$
\theta_ {S} <   1 - d _ {2} / (d _ {2} - d _ {1}) \theta_ {I}, \partial \theta_ {S} / \partial t > 0,\tag{12}
$$

then $\theta _ { I }  \theta _ { I } ^ { * } , \theta _ { S }  \theta _ { S } ^ { * }$ , and depending on the original distribution of the strategies, the strategic equilibrium result is (I or S, N ). Otherwise, if the following condition holds:

$$
\theta_ {S} > 1 - d _ {2} / (d _ {2} - d _ {1}) \theta_ {I}, \partial \theta_ {S} / \partial t <   0,\tag{13}
$$

then $\theta _ { S }  0 \ , \theta _ { I }  1 .$ In this case, the strategic equilibrium result is $( I , N )$

Inference 3. If the netizens adopt the T strategy and the loss for the enterprise that adopts the N strategy is small, then during the course of evolution, the enterprise will finally choose the N strategy and the netizens will gradually adopt non-condemnation, i.e., I or $S$ strategy. If the enterprise always chooses a negative strategy, then the strategy of the netizens will gradually shift to an attitude of non-condemnation, and th final equilibrium state depends on the initial distribution of the I and S strategies. In this situation, the resulting strategy equilibrium is (I or S, N ).

If $r _ { 3 }$ is large, then the dominant strategy for the enterprise is the P strategy, i.e., the enterprise makes a positive response by apologizing and promising improvements. We now analyze the strategy equilibrium fo both participants in this case. According to the general replication equation, the proportional distribution of the netizens who follow the I strategy is as follows:

$$
\partial \theta_ {I} / \partial t = \theta_ {I} [ u (I) - \bar {u} ] = - \theta_ {I} [ \theta_ {S} (- d _ {1} + c _ {1}) + \theta_ {T} (- d _ {2} + c _ {2}) ] <   0, \theta_ {I} \rightarrow 0\tag{14}
$$

450 The proportional distribution of the netizens who follow the $S$ strategy is as follows:

$$
\partial \theta_ {S} / \partial t = \theta_ {S} [ u (S) - \bar {u} ] = \theta_ {S} [ (1 - \theta_ {S}) (- d _ {1} + c _ {1}) - \theta_ {T} (- d _ {2} + c _ {2}) ]\tag{15}
$$

The proportional distribution of the netizens who follow the T strategy is as follows:

$$
\partial \theta_ {T} / \partial t = \theta_ {T} [ u (T) - \bar {u} ] = \theta_ {T} [ (1 - \theta_ {T}) (- d _ {2} + c _ {2}) - \theta_ {S} (- d _ {1} + c _ {1}) ]\tag{16}
$$

If the enterprise adopts the P strategy and the utility of the netizens who adopt the S strategy is greater than the utility of the netizens who adopt the T strategy, $\mathrm { i . e . , ~ } - d _ { 1 } + c _ { 1 } > - d _ { 2 } + c _ { 2 } > 0$

$$
\partial \theta_ {S} / \partial t > 0, \theta_ {S} \rightarrow 1, \theta_ {T} \rightarrow 0,\tag{17}
$$

and the netizens will tend to adopt the S strategy. In this case, the strategy equilibrium is (S, P ).

If the enterprise adopts the P strategy and the utility of the netizens who adopt the T strategy is greater than the utility of the netizens who adopt the S strategy, $\mathrm { i . e . , ~ } - d _ { 2 } + c _ { 2 } > - d _ { 1 } + c _ { 1 } > 0 .$ then:

$$
\partial \theta_ {T} / \partial t > 0, \theta_ {T} \rightarrow 1, \theta_ {S} \rightarrow 0,\tag{18}
$$

and the netizens will tend to adopt the T strategy. In this case, the strategy equilibrium is $( T , P )$

If the enterprise adopts the P strategy and the utility of the netizens who adopt the T strategy is equal to the utility of the netizens who adopt the S strategy, $. . . , - d _ { 1 } + c _ { 1 } = - d _ { 2 } + c _ { 2 } > 0$ , then:

$$
\partial \theta_ {S} / \partial t > 0, \partial \theta_ {T} / \partial t > 0, \theta_ {S} \rightarrow \theta_ {S} ^ {*}, \theta_ {T} \rightarrow \theta_ {T} ^ {*}\tag{19}
$$

and the strategy selected by the netizens depends on the initial distribution of S and T strategies. In this case, the strategy equilibrium is $( S \mathrm { o r } T , P )$ , depending on the original distribution of S and T strategies.

Inference 4. When the enterprise faces a crisis due to negative information appearing on the Internet and the netizens already exhibit large-scale activity on social media, adopting the N strategy will incur a great loss for the enterprise. Consequently, in this case, the dominant strategy that the enterprise should adopt is the P strategy. In addition, if the cost of the P strategy for the enterprise meets certain conditions, then resistance by the netizens can lead to greater benefits, i.e., the enterprise adopts the S strategy. The netizens will then be more inclined to actively express their opinions and protest in order to obtain a positive response from the enterprise.

## 4. Model Extensions

In this section, we introduce possible extensions of the basic model. First, we introduce complex networks into the strategy learning rule, before extending the model with a defend strategy for netizens.

## 4.1. Extension for Complex Networks

The learning rule in the proposed evolutionary game model (Equation 1) assumes that each individual observes the strategies of all the other agents and chooses the optimal strategy based on these observations. However, in real-world social media, an individual with limited time and energy only considers a limited number of selected individuals, e.g., friends and opinion leaders. Thus, netizens form a structured network on social media. In this context, an individual with bounded rationality is not always able to identify the optimal strategy, especially when the assessment of a strategy’s utility involves emotional factors, such as fairness, morality, or social responsibility. Netizens may make mistakes or ignore some important factors, thereby leading to the selection of a suboptimal strategy.

In order to make the evolutionary game model described in the previous section more realistic, we modify the learning rule to consider the social network structure. Hence, a network graph represents the communities on social media, where each node represents an individual netizen and the connecting edges between nodes represent the social relationships between individuals. Then, the strategy choice made by an individual netizen i is determined by comparing the utility of the diferent strategies for the individual i with the utilit of the strategies for the individuals (neighbors) adjacent to i.

The edges in a network are defined by an adjacency matrix. For an entry $A _ { i j }$ in this adjacency matrix for any two netizens i and j such that $i \neq j , A _ { i j } = A _ { j i } = 1$ means that there is a connection between netizens i and $j ,$ and $A _ { i j } = A _ { j i } = 0$ means that there is no connection between i and $j .$ Let I denote the set of individuals connected to an individual i and the value of $A _ { i j }$ is defined as follows:

$$
A _ {i j} = \left\{ \begin{array}{l l} 1 \mathrm{if} j \in \mathcal {I} \\ 0 \mathrm{if} j \notin \mathcal {I} \end{array} \right.
$$

Diferent types of complex network structures may be considered, $\mathrm { e . g . } , \mathrm { g . . }$ Erd˝os–R´enyi (ER) random graph [63, 64], Watts–Strogatz (WS) small world network [65], and the Barab´asi–Albert (BA) scale-free network [66]. An important attribute of a network is the clustering coeficient:

$$
\rho = \frac {\text {Number of actual links}}{\text {Theoretical maximum number of links}}
$$

. In Section $6 ,$ we present the results of numeric simulation experiments that we conducted to determine the results obtained from evolutionary games with the proposed model using diferent, randomly set-up networks with ER and WS structures, and various clustering coeficients.

As the new learning rule for our model, we employ a modified Fermi function [67, p. 378] and further adapt this Fermi function for our model. The Fermi function originally proposed in statistical physics has been employed previously to evolutionary games on lattices [68] and graphs [69], as well as adaptive social networks [67]. Thus, the learning process for a netizen i at time t is as follows: The netizen i compares the utility of a neighbor $j ^ { \cdot } \mathrm { s }$ strategy with the mean utility among the neighbors (including i) and learns from a neighbor j according to the probability determined by the Fermi function. Consistent with the aims of Equation 1, which implies that the choice of strategy depends on comparing the benefit of each strategy for netizen $j$ and the mean benefit of the strategies adopted by all netizens, we employ an adapted Fermi function that determines the probability of netizen i learning a strategy from a netizen $j$ based on the utility of the strategy, as follows:

$$
P _ {i \rightarrow j} = \frac {1}{1 + e ^ {- \beta (u _ {j} - \bar {u} _ {\mathcal {I}})}}\tag{20}
$$

In our adapted Fermi function, the utility

$$
\bar {u} _ {\mathcal {I}} = \frac {1}{| \mathcal {I} |} \sum_ {l \in \mathcal {I}} u _ {l}
$$

refers to the average utility of strategies for the netizens connected to i and $| \mathcal { T } |$ is the number of netizens in the set $\mathcal { T } ,$ which comprises all the netizens connected to i. It should be noted that $u _ { l }$ refers to the utility $u _ { l } ( f )$ of netizen $l \in \mathcal { T }$ given $l \mathrm { { ^ { \circ } s } }$ current choice of strategy f (at time $t ,$ , which is omitted for brevity). The parameter $\beta$ is referred to as the “intensity of selection” [67, p. 378] and it represents a form of system “noise” [69]. A larger $\beta$ denotes less noise, which means that individuals can distinguish optimal and suboptimal strategies more readily.

The adapted Fermi function has the following three important characteristics. First, the probability of learning is directly proportional to the diference in utility. Second, there is a certain probability that an individual netizen learns a strategy with low utility. Finally, system noise afects the probability of learning.

A social network of netizens comprises n individuals, where each initially follows the I, S, or T strategy. Thus, in the network, each netizen chooses one of three strategies for negative events, and $f$ denotes the strategy that an agent i chooses. According to the proposed dynamic game model, $u _ { i } ( f )$ denotes the utility of a strategy $f$ for an individual i. If the enterprise chooses the $P$ strategy, the utility $u _ { i } ( f )$ is defined as follows:

$$
u _ {i} (f) = \left\{ \begin{array}{l l} 0 & \text {if f = I} \\ - d _ {1} + c _ {1} & \text {if f = S} \\ - d _ {2} + c _ {2} & \text {if f = T} \end{array} \right.
$$

If the enterprise chooses the N strategy, the utility $u _ { i } ( f )$ is defined as follows:

$$
u _ {i} (f) = \left\{ \begin{array}{l l} 0 & \text {if} f = I \\ - d _ {1} & \text {if} f = S \\ - d _ {2} & \text {if} f = T \end{array} \right.
$$

The introduction of the Fermi function makes it dificult to analyze the theoretical equilibrium solutions. Thus, as shown in Section 6.2, we conducted simulations to investigate the probability of a certain strategy dominating in diferent situations.

## 4.2. Extension for Defend Strategy

For diferent reasons, netizens may also pursue a strategy of defending the enterprise during a social media crisis. This behavior could be based on benefit, personal preference (such as the loyalty of fans), or belief (e.g., an individual with racist beliefs will defend a company under fire for allegedly having discriminatory business policies). If the defending behavior can be understood as benefit based, then our extended model addresses the situation where netizens view defending behavior as an optional strategy to cope with a crisis. Some netizens may not blame the company for negative feedback (even temporarily) and expect and praise possible positive feedback from the company. This can be viewed as a strategy of showing tolerance, thereby encouraging the company’s positive behavior with reputation rewards rather than punishment. If the defending behavior is based on personal preferences or beliefs, then the defending behavior may be rooted in a personal trait, which may be due to a long-term relationship with the company or personal experience and values. This trait is unlikely to be learned by observing the behavior of others, and thus it cannot be covered by our model. Therefore, in this study, we only conducted an initial investigation of defending behavior and future research should aim to provide answers regarding the intrinsic motivation of defending behavior.

We add the D strategy to the action set of netizens and Figure 2 shows the extended model. In some situations, such as when the responsibility for an incident is ambiguous or the company is innocent, netizens could have the option to tolerate the company’s negative responses, and reward the company if it makes a positive response. In particular, netizens who take the D strategy incur a cost $d _ { 3 }$ to defend the enterprise, where we assume that $d _ { 3 } > d _ { 1 }$ because a defending action is usually more dificult than silence. The D strategy will not cause additional losses for the company that adopts a negative strategy (such as not responding). If the company adopts a positive strategy and incurs $c _ { 3 }$ as a response to the defense, then the D group of netizens obtains a benefit equal to the payof obtained minus the cost paid $\left( c _ { 3 } - d _ { 3 } \right)$ . In addition, the defending netizens give a reputation reward $r _ { 4 }$ to the company.

Similar to the analysis of the basic model, when comparing the values of $U _ { P }$ and $U _ { N }$ , we have the following.

$$
U _ {P} - U _ {N} = - c _ {1} \theta_ {I} + (r _ {1} - c _ {1}) \theta_ {S} + (r _ {3} - c _ {2} - r _ {2}) \theta_ {T} + (r _ {4} - c _ {3}) \theta_ {D}\tag{21}
$$

As shown by Equation 21, the reputation reward $r _ { 4 }$ ofered by the D group of netizens makes the enterprise tend to choose the $P$ strategy. Specifically, $U _ { P } > U _ { N }$ if and only if

$$
r _ {4} > c _ {3} + \frac {(c _ {1} - r _ {1}) \theta_ {S} + c _ {1} \theta_ {I} + (c _ {2} + r _ {2} - r _ {3}) \theta_ {T}}{\theta_ {D}}\tag{22}
$$

Next, we use Equation 1 to determine the evolutionary process for the D strategy. If the company adopts the N strategy, it is clear that the D strategy will not dominate because it has not the highest benefit. If the company adopts the $P$ strategy, then we have the following.

![](/api/attachments/B78YGFSS/fulltext/images/4e6838578f2608aa8ca08d02cbd42181116a1796fd7c50a76714573485fbb211.jpg)  
Figure 2: Extension of the model with defending behavior of netizens.

$$
\frac {\partial \theta_ {D}}{\partial t} = \theta_ {D} [ u (D) - \bar {u} ] = \theta_ {D} [ (1 - \theta_ {D}) (c _ {3} - d _ {3}) - \theta_ {S} (c _ {1} - d _ {1}) - \theta_ {T} (c _ {2} - d _ {2}) ]\tag{23}
$$

If $c _ { 3 } - d _ { 3 } > m a x ( 0 , c _ { 1 } - d _ { 1 } , c _ { 2 } - d _ { 2 } )$ , then: $\begin{array} { r } { \frac { \partial \theta _ { D } } { \partial t } > m a x ( \frac { \partial \theta _ { I } } { \partial t } , \frac { \partial \theta _ { S } } { \partial t } , \frac { \partial \theta _ { T } } { \partial t } ) } \end{array}$ , thus $\theta _ { D }  1$ , which means that the proportion of netizens who adopt the D strategy will continuously increase if it has the highest benefit among the netizens’ strategies.

According to the results above, the D strategy will finally dominate if and only if it has the highest benefit, $\mathrm { i . e . , } \ c _ { 3 } > d _ { 3 } + m a x ( 0 , c _ { 1 } - d _ { 1 } , c _ { 2 } - d _ { 2 } )$ . If the reputation reward ofered to the enterprise by the netizens who adopt the D strategy is suficiently high, the enterprise will maintain the P strategy, i.e., the condition expressed in 22 holds. We can also show that the condition expressed in 22 is satisfied if $\begin{array} { r } { r _ { 4 } > c _ { 3 } + \frac { ( 1 - \theta _ { D } ^ { 0 } ) } { \theta _ { D } ^ { 0 } } c _ { 1 } } \end{array}$ where $\theta _ { D } ^ { 0 }$ is the initial proportion of the D strategy.

Proof: $\begin{array} { r } { c _ { 3 } + \frac { ( c _ { 1 } - r _ { 1 } ) \theta _ { S } + c _ { 1 } \theta _ { I } + ( c _ { 2 } + r _ { 2 } - r _ { 3 } ) \theta _ { T } } { \theta _ { D } } } \end{array}$ has an upper bound $\begin{array} { r } { c _ { 3 } + \frac { ( 1 - \theta _ { D } ) c _ { 1 } } { \theta _ { D } } } \end{array}$ , which is decreasing in $\theta _ { D }$ . In addition, with $\theta _ { D } ^ { 0 }$ , the initial proportion of the D strategy, $\theta _ { D } \geq \theta _ { D } ^ { 0 }$ if and only if the proportion of the D strategy increases continuously. Therefore, $\begin{array} { r } { c _ { 3 } + \frac { ( 1 - \theta _ { D } ^ { 0 } ) c _ { 1 } } { \theta _ { D } ^ { 0 } } > c _ { 3 } + \frac { ( 1 - \theta _ { D } ) c _ { 1 } } { \theta _ { D } } > c _ { 3 } + \frac { ( c _ { 1 } - r _ { 1 } ) \theta _ { S } + c _ { 1 } \theta _ { I } + ( c _ { 2 } + r _ { 2 } - r _ { 3 } ) \theta _ { T } } { \theta _ { D } } } \end{array}$

In addition, we find that when $r _ { 4 } ~ < ~ c _ { 3 }$ , even if the company sets a high c to ensure the highest benefit of the D strategy, when $\theta _ { I } , \ \theta _ { S } , \ \theta _ { T }$ decrease and approach 0 because of $\theta _ { D } \  \ 1$ , then $\begin{array} { r } { c _ { 3 } + \frac { ( c _ { 1 } - r _ { 1 } ) \theta _ { S } + c _ { 1 } \theta _ { I } + ( c _ { 2 } + r _ { 2 } - r _ { 3 } ) \theta _ { T } } { \theta _ { r } } \ \to \ c _ { 3 } } \end{array}$ , and thus $\begin{array} { r } { r _ { 4 } < c _ { 3 } + \frac { ( c _ { 1 } - r _ { 1 } ) \bar { \theta } _ { S } + c _ { 1 } \theta _ { I } + ( c _ { 2 } + r _ { 2 } - r _ { 3 } ) \theta _ { T } } { \theta _ { D } } } \end{array}$ holds, which implies that $U _ { P } \leq \stackrel { \theta _ { D } } { U } _ { N }$ . The company will then adopt the N strategy and the D strategy cannot finally dominate. As a result, Inference 5 follows:

Inference 5. If $\begin{array} { r } { r _ { 4 } > c _ { 3 } + \frac { ( 1 - \theta _ { D } ^ { 0 } ) } { \theta _ { D } ^ { 0 } } c _ { 1 } } \end{array}$ , then the company has an incentive to set a high $c _ { 3 }$ such that $c _ { 3 } >$ $d _ { 3 } + m a x ( 0 , c _ { 1 } - d _ { 1 } , c _ { 2 } - d _ { 2 } )$ , in order to ensure that the proportion of netizens who adopt the D strategy increases until it dominates, whereas if $r _ { 4 } < c _ { 3 }$ , the D strategy cannot dominate.

Inference 5 implies that if the reputation reward is suficiently large, then the company obtains suficient benefit to provide part of it as encouragement to netizens to adopt the D strategy, thereby causing the D strategy to dominate. If the reputation reward is less than the cost of the D strategy, the D strategy cannot dominate because encouraging the D strategy will eventually lead to a deficit for the enterprise.

In other situations, specifically when $\begin{array} { r } { c _ { 3 } < r _ { 4 } < c _ { 3 } + \frac { ( 1 - \theta _ { D } ^ { 0 } ) } { \theta _ { D } ^ { 0 } } c _ { 1 } } \end{array}$ , the equilibrium result depends on the specific evolutionary process. We present investigations of these situations in Section 6.

## 5. Case Studies

In this section, we present investigations of two cases of social media crisis communication in the context of the proposed evolutionary game model, which comprise the Chinese writer Liu Liu’s dispute with online retailer Jingdong (JD) during March 2018 and the Starbucks racial bias crisis in Philadelphia during April 2018. In particular, we studied the evolution of posts on Weibo and Twitter, and consulted informative resources in order to estimate parameter values. We then interpreted the actions of the actors from the perspective of evolutionary game theory. The estimated parameter values were used as the starting points for the numeric simulations described in Section 6.

## 5.1. Liu Liu vs. Jingdong

JD is a large electronic commerce platform in China, which runs its own online trading business while also ofering a third-party marketplace where external sellers may ofer their products. On March 13, 2018, the Chinese writer Liu Liu $( \overrightarrow { \prime } \overrightarrow { \prime } \overrightarrow { \prime } \cdot \overrightarrow { \Big ) }$ published a blog post that she later shared in a message (tweet) on the Chinese microblogging service Weibo, in which she complained about JD following a friend’s purchase of a product via a third-party shop on the JD platform. Liu Liu’s friend claimed to have received “fake goods” [70] from an external seller, which JD initially denied, and thus compensation was refused. Liu Liu’s friend and JD did not reach a settlement. After posting a link to her blog on Weibo, Liu Liu received the attention of netizens on social media, followed by a negative first response by JD, which accused Liu Liu and her friend of foul play, and even threatening Liu Liu with legal actions. JD’s negative reaction caused uproar among netizens according to the vast increase in the forwards of Liu Liu’s original blog post (see Figure 3). Finally, JD had to publicly apologize to Liu Liu and her friend.

Table 2 shows the estimated parameter values for the proposed evolutionary game model. Some values are dificult to estimate correctly. Costs and benefits, especially for netizens, are often of an immaterial and emotional nature, which is especially true in this case. Indeed, what did netizens gain from publicly shaming JD? Liu Liu’s post may have resonated with netizens who were dissatisfied with JD in the past. Thus, netizens may have vented their anger online and the gain was mainly emotional. The company could have averted the crisis by responding more positively through increased PR eforts and possibly the announcement of changes in its business policies. However, JD seems to have underestimated the situation, thereby resulting in a huge loss of shareholder value.

From the viewpoint of the proposed evolutionary game model, the costs of the N strategy for JD were very high. By contrast, netizens had considerably more to gain from the T strategy than the S strategy, thereby making the T strategy advantageous. Therefore, netizens chose the T strategy and JD should have pursued the P strategy to minimize the damage. Indeed, JD later put efort into improving the quality of its after-sales service [71].

## 5.2. Starbucks Racial Bias Crisis

On April 12, 2018, police removed two African-American men from a Starbucks store in Philadelphia after having been alerted by the manager of the store. The two men were waiting in the store without ordering anything. The scene was captured on video by other patrons and posted on Twitter, which sparked social media outrage as well as physical protests. Users and protesters accused Starbucks of racial bias and called out the police for detaining two innocent citizens without just cause. On April 16, 2018, Starbucks CEO Kevin Johnson apologized publicly in a TV interview. Subsequently, on April 17, 2018, Johnson announced the closure of all US Starbucks stores on May 29, 2018 in order for employees to undergo special training to counter racial bias. Starbucks had generally succeeded in containing the crisis by that date.

Table 2: Estimated parameter values (in hundreds of millions of yuan) for the Liu Liu vs. JD dispute

<table><tr><td>Parameter</td><td>Value</td><td>Rationale</td></tr><tr><td> $v$ </td><td>20</td><td>Revenue generated by third-party merchants on JD, mainly derived from platform usage fees and sales. JD receives an average platform fee of 1,000 yuan per merchant [72]. On September 30, 2018, there were approximately 200,000 contracted merchants on JD&#x27;s third-party platform, and the revenue from the platform fee was 2 billion yuan.</td></tr><tr><td> $r_1$ </td><td>2.4</td><td>We used the value of Liu Liu&#x27;s fans to estimate  $r_1$ . Liu Liu had about 12 million fans on Weibo, which we assumed had low opinions of JD due to their negative strategy. Assuming a value of 20 yuan for each fan, the value of  $r_1$  was then estimated at 240 million yuan. The value of an individual fan was derived from figures published in the context of Yuye Co.&#x27;s intended acquisition of Shenzhen Quantum Cloud Technology Co., which was announced on April 27, 2018, as well as 981 WeChat public accounts. The purchase price was 3.8 billion yuan. According to the data regarding the proposed acquisition, the value of each fan was estimated at 20 yuan.</td></tr><tr><td> $r_2$ </td><td>15</td><td>When netizens condemned the company, the cost of the company&#x27;s positive response  $r_2$  was estimated at 1.5 billion yuan, which was mainly due to the decline in the reputation of the company caused by netizens. This value was obtained by taking the average change in the stock price for JD on March 13 before JD&#x27;s negative response.</td></tr><tr><td> $r_3$ </td><td>100</td><td>Following Liu Liu&#x27;s complaint about JD, the company gave a negative response. We used the changes in the market value of JD&#x27;s stock listed on NASDAQ for the next two days (March 13 and 14, 2018) as JD&#x27;s loss. By comparing the volatility in JD&#x27;s stock price (-4.1522%) with the average market volatility (-1.7137%) in the same period, we estimated JD&#x27;s loss at 1.6 billion USD, which is equal to around 10 billion yuan.</td></tr><tr><td> $c_1$ </td><td>5</td><td>We based  $c_1$  on the volume of the contract between JD and the PR company Blue Focus in the 2017 financial report of the latter. We assumed that the contract&#x27;s focus was on regular PR activities to positively influence the image of the company, which might have been sufficient in times of crisis if netizens remained silent.</td></tr><tr><td> $c_2$ </td><td>7</td><td>In times of crisis, additional effort will be needed if netizens blame the company on social media. We did not know the exact amount, but we assumed a value higher than the volume of the contract between JD and Blue Focus.</td></tr><tr><td> $d_1$ </td><td>0.5</td><td>The cost of the S strategy for netizens was difficult to estimate. We assumed that it was rather low in this case.</td></tr><tr><td> $d_2$ </td><td>2</td><td>We consider that the revenue of Sina Weibo&#x27;s advertising and marketing business could represent the cost of attention and condemnation by netizens. According to the revenue from the advertising and marketing business in the first three quarters for Sina Weibo, the number of monthly active users (446 million), and the average attention time of users on the event (one week), we estimated the cost of the T strategy for netizens at about 200 million yuan.</td></tr></table>

![](/api/attachments/B78YGFSS/fulltext/images/4c750bccaa25bc744e4b8bbed6113d5d3d95ca4a047f00f2afede5fd07055a8d.jpg)  
Figure 3: Accumulated number of forwards on Weibo for Liu Liu’s original blog post.

We conducted sentiment analysis to illustrate how the crisis unfolded on Twitter. Sentiment analysis aims to extract “subjective information from texts in natural language” [73, p. 1], e.g., by classifying messages as positive, negative, or neutral [73, p. 7], where an optional sentiment score indicates the degree to which a sentiment is positive or negative. Analyzing the evolution of the sentiment in tweets related to Starbucks showed that the tweets generally became more negative following the Philadelphia incident. The left column in Figure 4 shows the evolution of the number of positive, neutral, and negative tweets as well as their proportions, and the evolution of the mean sentiment score per day around the time of the incident. Tweet sentiment scores on a continuous range from –1 (negative) to +1 (positive), where 0 is neutral, were obtained via Google’s Natural Language API<sup>1</sup>, which provides pre-trained machine learning models for natural language processing. Tweets were collected on December 27, 2019 for each day from April 7 to April 25, 2018 by scraping the top tweets returned by Twitter’s advanced search feature using variations in the search term (to:Starbucks) (@Starbucks) lang:en until:2018-04-07 since:2018-04-08, with changing dates. We collected the top tweets in order to obtain a representative sample of the general sentiment toward Starbucks. Automatic sentiment analysis is not perfect but we obtained a quantifiable measure of general sentiment.

The timeline of the Starbucks racial bias crisis can be roughly divided into three time periods comprising the time period immediately before the incident (T1), that between the incident and CEO Johnson’s interview with the announcement of racial-bias training (T2), and that after that interview (T3). The right column in Figure 4 shows the tweet sentiment evolution during the three periods (T1–T3). The time period immediatel before the incident (T1) was characterized by generally positive tweets and an overall positive mean sentiment score. In the aftermath of the incident (T2), the proportion of negative tweets increased and the mean

![](/api/attachments/B78YGFSS/fulltext/images/f08014c6592358029b8b99129e68b0b67500e59e7c53dff441ac282b7be42d88.jpg)  
Figure 4: Sentiment analysis based on the top tweets related to Starbucks around the time of the racism incident in Philadelphia during 2018.

#

sentiment score for tweets decreased significantly in that period, with a p-value $< 0 . 0 5$ , and the mean sentiment score in T2 was significantly less than that in T1. Following Starbucks’ positive response (T3), the proportion of negative tweets decreased and the mean sentiment score in T3 was significantly higher than that in T2. However, the general sentiment after the response was still significantly more negative than that before the incident

The sentiment analysis results were used to estimate the initial distribution of the netizen strategies for the numeric simulations. It can be assumed that if the crisis has no impact, then the ratios of positive, neutral, and negative comments would remain roughly unchanged, and the ratios in T1 served as the baseline. In T2, the ratio of positive comments decreased by 28.59%. With 14.50% of the positive comments remaining, we consider that this indicated the persistence of positive emotions after the emergence of the crisis event, which suggests that these individuals were basically unafected by the event. From the perspective of crisis PR, individuals who still hold positive emotions do not actually consider that the reputation of the company has declined. The increase in the ratio of negative comments by 27.13% can be considered to indicate the proportion with the $T$ strategy. The ratio of neutral comments increased by 1.45%, which can be considered to indicate the proportion with the S strategy. In T3, the ratio of positive comments increased by 13.40%, i.e., increased to 27.90%. A positive comment may have been posted either by an individual who did not care about the incident (estimated at 4.08%) or by an individual who was satisfied with the company’s response (estimated 17.48%) (neither caused a decline in the corporate reputation). The decrease in the ratio of negative comments to 46.41% (constituting a decrease of 17.48%) can be explained by the decrease in the proportion with the T strategy. The ratio of neutral comments increased to 25.69% (constituting an increase of 4.08%), which can be considered the proportion with the S strategy. Thus, we use the ratios of positive comments in periods T2 and T3 as the proportion with the I strategy, and the increases in negative and neutral comments from T1 to T2 and T3 as the proportions with T and S strategies. The estimated initial ratios of the I, S, and T strategies were $3 4 \% = 1 4 . 5 \% / ( 2 7 . 1 3 \% + 1 . 4 5 \% + 1 4 . 5 \% )$ , 3% $= 1 . 4 5 \% / ( 2 7 . 1 3 \% + 1 . 4 5 \% + 1 4 . 5 \% )$ , and $6 3 \% = 2 7 . 1 3 \% / ( 2 7 . 1 3 \% + 1 . 4 5 \% + 1 4 . 5 \% )$ , respectively.

Table 3 shows the estimated parameter values in the Starbucks racial-bias crisis, which were used as the basis for the numeric simulations presented in Section 6. The parameter values depend on multiple factors and they can often only be approximated in practice. For example, the value of an individual fan is not the same for diferent companies. Twitter lets companies run “followers campaigns” that typically cost \$2.50–\$3.50 per newly created follower [74]. However, the real value of each fan is higher than that. Many companies use coupons to attract fans to register. Hence, to estimate the value of fans, we referred to the cost of new customers and the value of Twitter followers. We then obtained an approximate value of each fan of \$10. This value could be adjusted according to the situation.

The Starbucks incident is an example of positive crisis communication ofering non-discriminatory compensation to netizens who adopted $S$ and T strategies, i.e., there was not a great diference between $c _ { 1 }$ and $c _ { 2 }$ . The returns from the T strategy were lower due to the cost of the netizens choosing the T strategy exceeding the cost of the I strategy $( d _ { 2 } > d _ { 1 } )$ . From a numerical perspective, negative comments still occurred after the company responded (T3 period), i.e., some netizens maintained a T strategy, but the net utility of the S strategy was slightly greater than that of the T strategy. The logical rationale for the reaction by Starbucks was to rapidly reduce the number of people with the $T$ strategy. When the proportion of the population with the T strategy was reduced to a certain level, the company’s crisis communication could be ended, before keeping silent about the incident and transitioning to the N strategy.

Pundits generally lauded Starbucks for its decisive response to the incident and taking action despite the costs. Starbucks’ response to the crisis has been described as “renewing” and the crisis contributed toward “organizational rebirth, development and long-term survival” [75]. However, some commentators questioned whether a one-of training event would have a truly lasting impact and Starbucks itself acknowledged that the training event could only be a start [76]. Further developments partially confirmed that opinion. For example, at a discussion event in February 2019, Melissa DePino, who posted the original video of the incident, called out ex-CEO Howard Schultz for wrongly describing the incident and perpetuating the problem [77]. Thus, one might argue that Starbucks switched to a more negative strategy after the worst of the public outcry was over. Indeed, the model shows that in some situations, a company may switch from an initially positive strategy to a more negative strategy (see Simulation 5 in Section 6). The enterprise first adopts the P strategy to rapidly solve the problem, and the proportion of netizens who adopt the T strategy decreases rapidly, before the company switches to the N strategy and does not respond to it again. From another perspective, Starbucks gave a relatively high-cost positive response to the initial video in order to try to decrease the proportion of netizens who adopted the T strategy, thereby ending negative comments on the company. Subsequently, people occasionally mentioned the racial bias crisis, which risked another crisis for the company, but each time, netizens selected the S strategy because most considered that the enterprise had already done enough. The company selected its strategy as a reaction to the behavior of netizens and then finding that the risk of huge losses was small, the company changed to the (moderate) N strategy by not responding. However, on the occasion of the incident’s second anniversary in 2020, Starbucks reafirmed its commitment to promoting diversity, hinting at a continued generally positive strategy [78].

Table 3: Estimated parameter values (in hundreds of millions of US dollars) for the Starbucks racial bias crisis

<table><tr><td>Parameter</td><td>Value</td><td>Rationale</td></tr><tr><td> $v$ </td><td>170</td><td>Revenue for Starbucks in the United States for the 2018 fiscal year was 17 billion USD.</td></tr><tr><td> $r_1$ </td><td>3.6</td><td>We used the value of fans to measure  $r_1$ . Starbucks has a large fanbase on social media, with more than 36 million followers on Facebook, 11 million on Twitter, and 12 million on Instagram. Considering the overlap in the fanbases on different platforms, we considered that Starbucks had a fanbase on social media of at least 36 million. Taking a value of 10 USD per fan, the total value of the Starbucks fan base was estimated at 360 million USD.</td></tr><tr><td> $r_2$ </td><td>6</td><td>When netizens condemned the company, the loss due to the company&#x27;s positive response  $r_2$  was estimated at 600 million USD. After the company&#x27;s positive response, the proportion of negative comments was still higher than that before the crisis.</td></tr><tr><td> $r_3$ </td><td>32</td><td>Due to the lack of comparison, we referred to the JD case, with a decrease in the stock price of 4.1522%. Thus, we estimate that if Starbucks gave a negative response in this incident, it might have caused a loss of 3.2 billion USD.</td></tr><tr><td> $c_1$ </td><td>2.6</td><td>We based  $c_1$  on Starbucks&#x27; regular advertising costs of 260 million USD.</td></tr><tr><td> $c_2$ </td><td>3</td><td>The cost of closing more than 8000 stores in the United States for half a day was estimated to cost Starbucks about 16.7 million USD in lost sales, and the cost of training employees and daily PR ( $c_1$ ) was estimated at 300 million USD.</td></tr><tr><td> $d_1$ </td><td>1</td><td>The cost of the S strategy for netizens was difficult to estimate. For the simulation, we set this value to 100 million USD.</td></tr><tr><td> $d_2$ </td><td>1.7</td><td>We considered that the revenue from Twitter&#x27;s advertising and marketing business could represent the cost of attention and condemnation by netizens. For the second quarter of 2018, this revenue was 711 million USD. Assuming an average attention time of users to the event of one week, we estimated the cost of the T strategy by netizens at about 170 million.</td></tr></table>

## 6. Simulations

In order to confirm the theoretical analysis of the model presented in Section 3 and to study the implications of the model that cannot be deduced by theoretical analysis alone, we conducted numeric simulations using the parameter values estimated from the case studies in Section 5. We conducted simulations using both th basic model and the extended models with complex learning networks and defending behavior to study the evolutionary equilibrium and dominant strategies in diferent situations.

## 6.1. Basic Model Simulations

In the following, we present the results obtained in numeric simulations using the evolutionary game model with the basic learning rule and various parameter values. The estimates obtained from the Liu Liu vs. Jingdong case (Section 5.1) were used as the starting points for the parameter values. We aimed to determine evolutionary equilibria for strategies under diferent conditions. For a company afected by a social media incident, the equilibrium indicates the ideal strategy, given a certain situation.

Simulation 1. First, we assumed that netizens adopted only the I and S strategies (Situation 1), and the cost of the enterprise adopting the N strategy was less than the cost of adopting the P strategy. We set $c _ { 1 } = 5 , r _ { 1 } = 2 . 4$ , and thus $c _ { 1 } \geq r _ { 1 }$ . We assumed that the initial distributions for adopting the I, S, and $T$ strategies were 40%, 60%, and 0%, respectively, i.e., the majority of netizens observed the negative information whereas a minority ignored the incident but nobody took any action. Under these conditions, companies should adopt the N strategy, and thus the proportion of netizens who chose the I strategy eventually approached 100% (Figure 5a). Once the company adopts the N strategy, the company’s choice will lead netizens to eventually adopt the I strategy.

Simulation 2. We again assumed that netizens only adopted the I and S strategies, but in this case, the cost of the enterprise adopting the N strategy was more than the cost of adopting the P strategy. We varied the model parameters and set $c _ { 1 } = 2 , r _ { 1 } = 2 . 4$ , and thus $c _ { 1 } < r _ { 1 }$ . We assumed that the initial distributions for adopting the I, S, and T strategies were 15%, 85%, and 0%, respectively, which satisfied the condition that $\theta _ { S } > c _ { 1 } / r _ { 1 }$ . When the proportion of the netizens choosing the S strategy is high and the benefit for the enterprise adopting the $P$ strategy is greater than the benefit of choosing the N strategy, the enterprise should adopt the P Strategy. The netizens eventually adopted the S strategy (Figure 5b).

Simulation 3. We assumed that netizens only chose the I and S strategies, and the cost of the enterprise adopting the N strategy was more than the cost of adopting the P strategy. We set $c _ { 1 } = 2 , r _ { 1 } = 2 . 4$ , and thus $c _ { 1 } < r _ { 1 }$ . We assumed that the initial distributions for adopting the $I , S _ { ; }$ , and T strategies were 70%, 30%, and $0 \%$ , respectively, which satisfied the condition that $\theta _ { S } < c _ { 1 } / r _ { 1 }$ In this case, the proportion of netizens who adopted the S strategy and who noticed the negative information at the beginning was relatively small, and most netizens did not pay attention and they ignored relevant negative information. Eventually, the proportion of netizens who selected the I strategy approached 100% (Figure 5c). Despite the cost $r _ { 1 }$ , the enterprise continued to adopt the N strategy to control the evolution of events, thereby reflecting the reality that some enterprises hastily aim to limit the further proliferation of negative information through deterrence and by deleting posts in the immediate aftermath of the appearance of negative information on social media, where they hope that the strategy selected by netizens will evolve into the I strategy.

Simulation 4. We next assumed that netizens chose the I, S, and T strategies (Situation 2), and that the loss was large for the enterprise that chose the N strategy $\left( r _ { 3 } \right)$ , and it was more profitable for netizens to choose the $T$ strategy than the S strategy, $\mathrm { i . e . , ~ } - d _ { 2 } + c _ { 2 } > - d _ { 1 } + c _ { 1 }$ , which corresponds to the situation in the Liu Liu vs. Jingdong case. When $r _ { 3 }$ is large, the enterprise should choose the $P$ strategy. In this case, the benefit of choosing the $T$ Strategy was greater than that of the S strategy, so the proportion of netizens who selected the T strategy approached 100% (Figure 5d). The company needed to adopt a positive strategy to ensure that its loss was minimized. The benefits of the S strategy were greater than the benefits of the I strategy, so when the company adopted the $P$ strategy, the netizens who originally adopted the I strategy began to pay attention to the negative information and gradually changed to the $T$ strategy. This explains why the proportion of netizens who adopted the $S$ strategy increased slightly initially during the course of evolution and then approached 0%. Thus, the netizens changed to the $T$ strategy in this situation. The evolutionary equilibrium for the strategies was determined as $( T , P )$

Simulation 5. We assumed that a certain proportion of netizens (10%) chose the $T$ strategy and the loss was large for the enterprise that selected the N strategy $\left( r _ { 3 } \right)$ . For the netizens, choosing the $S$ strategy was more profitable than choosing the T strategy. We assumed that $c _ { 2 } = 6$ and the other initial values remain unchanged, where they satisfied $- d _ { 2 } + c _ { 2 } < - d _ { 1 } + c _ { 1 }$ . Figure 5e shows the distribution obtained sfor the strategies adopted by netizens. At the beginning, the proportion of netizens who selected the T strategy was relatively high, and thus adopting the P strategy had a significant impact on the enterprise. During the course of evolution, netizens who adopted the S strategy found that the free-riding behavior was cost-efective and profitable, so they increasingly choose to behave as a free-loader. The proportion of netizens who selected the $T$ strategy became smaller. Consequently, the risk of great loss for the company also became smaller. By monitoring public opinion, the enterprise could observe the change and quietly reverse its strategy by changing to a negative strategy. At this time, netizens wanted to force companies to adopt the $P$ strategy but found that more efort was required, which did not pay of, and they finall settled for the $S$ strategy. The costs for netizens $( d _ { 1 }$ and $d _ { 2 } )$ could be influenced by many factors, such as the activity of netizens, diferent cultural backgrounds, and awareness of the rights of netizens. However, the enterprise could control the costs $c _ { 1 }$ and $c _ { 2 }$ to some extent to influence whether netizens selected the S or $T$ strategy.

Simulation 6. We assumed that a larger proportion of netizens chose the $T$ strategy, the loss was large for the enterprise when selecting the N strategy, and the payof for the netizens who chose the $T$ strategy was equal to that with the $S$ strategy. We assumed that $c _ { 2 } = 6 . 5$ and the other initial values from the Liu Liu vs. Jingdong case remained unchanged, thereby satisfying the condition that $- d _ { 1 } + c _ { 1 } = - d _ { 2 } + c _ { 2 } > 0$ The initial distributions of the three strategies for netizens comprised 60% for the I strategy, 30% for the $S$ strategy, and 10% for the $T$ strategy. In this situation, enterprises should always adopt a $P$ strategy. The proportion of netizens who chose the I strategy approached 0%, and the distribution of the S and $T$ strategies depended on the initial distribution of the strategy (Figure 5f).

Simulation 7. We continued with the values used in Simulation 6, where $- d _ { 1 } + c _ { 1 } = - d _ { 2 } + c _ { 2 } > 0$ and the distribution of the $I , S ,$ and $T$ strategies depended on the initial distribution. We then varied the proportions of netizens who chose the I, S, and $T$ strategies to 60%, 10%, and 30%, respectively. Figure 5g shows th evolution of the strategy distribution in this scenario, which confirms that the distribution of the I and S strategies depended on the initial distribution.

Simulation 8. We considered the case where only a small proportion of netizens initially selected the T strategy and the loss was relatively small for the enterprise choosing the N strategy, with $r _ { 3 } = 3 0$ . The other parameter values remained unchanged. Figure 5h illustrates the evolution of the strategic choices over time. The enterprise always chose the N strategy. The proportion of netizens who chose the $T$ strategy approached $0 ,$ and the distribution of the I and S strategies depended on the initial proportions as well as the values of $d _ { 1 }$ and $d _ { 2 }$

When past experience shows that a company has always chosen a negative strategy and that it will probably continue to do so, the strategic choice of netizens will gradually deviate from the $T$ strategy during the course of evolution. When the attention of netizens incurs only a small loss for the enterprise and it does not constitute a deterrent, netizens will gradually shift to the I or S strategy. To explain this behavior, we may consider a monopolistic/oligopolistic company that holds (almost) absolute control (or at least a large share of influence) over the resources and market. This company does not have to be greatly concerned about a public outcry on social media.

## 6.2. Simulations with Complex Networks

In contrast to the learning process represented by replicator dynamics equations, real individuals may learn sub-optimal strategies from peers in the social network, especially when the benefits of the strategy are influenced by sentiment. In addition, the distribution of information may be asymmetric among netizens, where some individuals possess more information than others and diferent insights. It is dificult for an individual to observe the decisions made in the entire social network by all netizens that are active on social media. Frequently, an individual can only observe the decisions made by known, connected individuals. From a network-theoretic viewpoint, the community of netizens corresponds to a non-fully connected network structure comprising a non-complete graph. Therefore, in order to study the evolutionary game under more realistic assumptions, we then considered a group of netizens connected in a more complex network structure in our simulation experiments.

In the following, we present the results of simulations obtained using the Fermi function as a learning rule and with randomly generated ER and WS networks. In our simulations, we systematically varied the ratio k between the $S$ strategy and $T$ strategy benefit for netizens, as well as the clustering coeficient $\rho$ for the underlying ER and WS networks. We did not change the benefits of the I strategy because we made the realistic assumption that it did not change most of the time and it usually remained at 0. By contrast, th benefits of the S and $T$ strategies are readily afected by corporate decisions. The clustering coeficient of the network measures the connectivity between netizens and it is an important factor that afects learning and communication inside the social network. We did not include the results obtained for BA network structures because a small clustering coeficient generally below 0.2 is an inherent characteristic of BA networks. We experimented with BA networks but the clustering coeficient was excessively small to make a diference to the results. We conducted the following simulation experiments.

![](/api/attachments/B78YGFSS/fulltext/images/830f6212819a77ac0f144053ab9fa18958b6c013b69d878afaf38290d15f526d.jpg)  
(a) Simulation 1

![](/api/attachments/B78YGFSS/fulltext/images/51fa1eaa4cd6fca7ad238a8677116509f1b7874d9c031ed9278cadc48fae36be.jpg)  
(b) Simulation 2

![](/api/attachments/B78YGFSS/fulltext/images/b5cc787283fefdd5fab87f0da3010cf39aaabbdc9f98fc152b4a5d34bb6a55cf.jpg)  
(c) Simulation 3

![](/api/attachments/B78YGFSS/fulltext/images/b9268ae6588c1b20a6ae340531147a404d4d4cb82b1a84be999665760e1d3ddc.jpg)  
(d) Simulation 4  
Figure 5: Simulated evolution of distribution of netizen strategies according to the basic game model. (cont. next page)

![](/api/attachments/B78YGFSS/fulltext/images/05251fe70dbc4c9809f7d15a98e01b4127cc58ff482cac444a61515190cc208e.jpg)  
(e) Simulation 5

![](/api/attachments/B78YGFSS/fulltext/images/7a96ceb9fc5262edbaf015eb431c5f321ef4a17a905cf938f47d72593eb3d5b4.jpg)  
(f) Simulation 6

![](/api/attachments/B78YGFSS/fulltext/images/5c28f1d3f895686803ba96f8faa79712638bda73d4dc6cd66aeecf459598ff97.jpg)  
(g) Simulation 7

![](/api/attachments/B78YGFSS/fulltext/images/d04fa983a72b764bc237eb5cc6120600ad63b65b788689bfc231a4489c9b91af.jpg)  
(h) Simulation 8  
Figure 5 (cont.): Simulated evolution of the proportions of netizen strategies according to the basic game model.

• The parameter values were estimated based on the Starbucks racial bias crisis case (Table 3). We fixed the initial proportions of netizens choosing I, S, and T strategies at 34%, 3%, and 63%, respectively, which we estimate by analyzing the sentiment in tweets from the Starbucks racial bias crisis case (see Section 5.2).

• The intensity of selection β in the Fermi function was set to 3, 30, and 100.

• We randomly built ER networks and WS networks with 100 nodes.

• For each simulated evolution process, when the process entered a state where the standard deviation of each strategy’s proportion for the last three evolutionary steps was less than $1 0 ^ { - 4 }$ , we considered that the simulation had reached an evolutionarily stable state

• For each set of parameters, we ran 100 evolution processes in order to obtain the mean proportion of each strategy in the evolutionarily stable state. A strategy with a proportion exceeding 90% in the evolutionarily stable state during an evolution process was defined as the dominant strategy. We designated the frequency of a strategy being dominant as the dominant probability.

The contour graphs in Figures 6 and 7 show the dominant probabilities of the T strategy in the diferent evolution processes under various benefits for the S and T strategies expressed as the ratio k on the Y-axis and the network’s clustering coeficient on the X-axis. Simulation 9 employed an ER network (Figure 6) and simulation 10 utilized a WS network (Figure 7). The clustering coeficient ρ indicates the degree to which a network tends to cluster, where the network is more clustered when ρ is higher. k denotes the ratio between the S strategy returns and T strategy returns $( k = ( c _ { 1 } - d _ { 1 } ) / ( c _ { 2 } - d _ { 2 } ) )$ ), where the relative advantage of the S strategy is greater when k is higher. The diferent contours indicate parameter combinations with the same dominant probability. In our simulations, only the T and S strategies were dominant. In our analysis, the probability of the T strategy dominating was more interesting because the T strategy is the least desirable strategy from an enterprise’s viewpoint.

In contrast to the results obtained from the simulations using the basic model with the replicator dynamics equation, the strategy with the higher benefits, i.e., T in our case, was not necessarily dominant when considering the Fermi function and complex networks. This is highly intuitive because netizens had the possibility of choosing a sub-optimal strategy learned from their neighbors. However, the probability of a certain strategy dominating increased when that strategy’s benefit became higher compared with those of other strategies.

After increasing the network clustering coeficient, the probability of the strategy with higher benefits (i.e., T ) dominating decreased, whereas the probability of the strategy with lower benefits (i.e., S) dominating increased. A larger clustering coeficient implies that each individual in the social network had more connections (neighbors). Correspondingly, the likelihood of learning based on comparisons with the strategy benefits obtained by neighbors increased, and thus the probability of learning a strategy increased for a larger proportion of netizens, even if that strategy had lower benefits. Therefore, the presence of more connections and increased communication activity in the network increased the chance of learning a suboptimal strategy. This result is also intuitive when considering real-world social media because sentiment tends to be magnified in social networks. Netizens imitate the behavior of their peers even if it is not the optimal strategy. We found that a weaker selection intensity in the Fermi function (which implies that it was more dificult for netizens to distinguish between the optimal strategy and suboptimal strategies) also reduced the probability of the more profitable strategy dominating.

![](/api/attachments/B78YGFSS/fulltext/images/4f6a98a2164d0bf328a8ddae7ae3635b43c1ee1c56931482b7d5a4793d12b693.jpg)  
(a) β = 3

![](/api/attachments/B78YGFSS/fulltext/images/a02dd60896cdc45e25274e01b64e8f5b175db8188e7b4ee1075ec052223564f9.jpg)  
(b) β = 30

![](/api/attachments/B78YGFSS/fulltext/images/81c67ef1c60c2d537e394e6d4e710eb08183bedbea045d4ad5cf035c8fa045a3.jpg)  
(c) β = 100

Figure 6: Probability of the T strategy dominating with an ER network (Simulation 9)  
![](/api/attachments/B78YGFSS/fulltext/images/d32f1c5bc76e4fbe7580b1d895e1ac03ed7e825a85ca940e7917eb70efdef13a.jpg)  
(a) β = 3

![](/api/attachments/B78YGFSS/fulltext/images/b181b714edc43a147e7ff045204fc9546aa8c5e6d03de503bdde6dcbc9e932ed.jpg)  
(b) β = 30

![](/api/attachments/B78YGFSS/fulltext/images/ebc39481f095e443f243b7d9222a8a0b71899c387469d52ae512f08ffd28200e.jpg)  
(c) β = 100  
Figure 7: Probability of the T strategy dominating with a WS network (Simulation 10).

## 6.3. Simulations with Defend Strategy

We then conducted simulations to confirm our findings and to continue the (theoretical) investigations presented in Section 4.2. We selected the general settings for the basic model simulations as the starting point and extended them by setting a proportion for the D strategy group. In particular, we set $c _ { 1 } = 5 , d _ { 1 } =$ $0 . 5 , c _ { 2 } = 6 , d _ { 2 } = 2 , r _ { 1 } = 2 . 4 , r _ { 2 } = 1 5 , r _ { 3 } = 1 0 0$ , while the proportions of the $I , S , T$ , and $D$ strategy groups were 60%, 25%, 10%, and 5%, respectively, and the cost of the D strategy $d _ { 3 } = 1$ . We varied $r _ { 4 }$ and $c _ { 3 }$ to verify the results presented in Section 4.2, and investigated cases where the reputation reward exceeded the company’s response cost for the D group, but the cost was not suficiently high to ensure that the D strategy would dominate, i.e., $\begin{array} { r } { c _ { 3 } < r _ { 4 } < c _ { 3 } + \frac { ( 1 - \theta _ { D } ^ { 0 } ) } { \theta _ { D } ^ { 0 } } c _ { 1 } } \end{array}$ , which implies that $6 < r _ { 4 } < 1 0 1$ for the settings used in this simulation.

Simulation 11. We set $c _ { 3 } = 6 ,$ which was suficiently high to ensure that the benefit of the D strategy was the highest among all of the strategies for netizens. We found that for a range of relatively large $r _ { 4 }$ values, the evolutionary process led to the same result where the proportion of netizens adopting the D strategy increased to become dominant. Two cases can illustrate the results, where $r _ { 4 } = 1 0 2$ ensured the domination of the D strategy, and $r _ { 4 } = 7$ was relatively high but it did not guarantee the domination of the D strategy. The simulation results were similar for both cases (Figure 8a). These results imply that in a situation where the company initially chooses the $P$ strategy and the greatest incentive is for netizens who adopt the D strategy, if the reputation reward $r _ { 4 }$ is relatively large, the company will maintain the $P$ strategy, thereby leading to domination of the D strategy. The diference between the two settings comprising $r _ { 4 } = 1 0 2$ and $r _ { 4 } = 7$ can be summarized as follows. In the case where $r _ { 4 } = 7$ , the evolutionary result depended on the changes in the selection of other strategies and the corresponding damage to reputation. When $r _ { 4 }$ was suficiently large $( r _ { 4 } = 1 0 2 )$ , the enterprise always adopted the P strategy. When $r _ { 4 } = 7 .$ , in the evolutionary process, the choice of whether the enterprise adopted the P strategy was based on the joint efect of the threat of a loss caused by netizens adopting the T strategy when the enterprise adopted the N strategy $( r _ { 3 } = 1 0 0 )$ and the reputational reward caused by the D strategy when the enterprise adopted the P strategy $( r _ { 4 } = 7 )$ The revenue from the D strategy $\left( c _ { 3 } - d _ { 3 } \right)$ was the highest among the various strategies, and the group of netizens adopting the D strategy provided a continuous positive benefit to the enterprise $( - c _ { 3 } + r _ { 4 } > 0 )$ , and thus the final result involved the D strategy dominating.

![](/api/attachments/B78YGFSS/fulltext/images/a443f160b13fc4fec507c457875c31e3b7721a9c54fbdc7c937774f8bb627491.jpg)  
(a) Simulation 11

![](/api/attachments/B78YGFSS/fulltext/images/f48bf374182ec75acf5e7f71f43c2ab573139da84316a8c012a4124e84293bac.jpg)  
(b) Simulation 12  
Figure 8: Simulated evolution of the proportions of netizen strategies according to the extended game model with the defend strategy.

Simulation 12. In this simulation, we again set $c _ { 3 } = 6$ and decreased the reputation reward. We considered two cases where $r _ { 4 } = 6 . 2$ and $r _ { 4 } = 5$ , and both resulted in a similar evolutionary process (Figure 8b). The results showed that the proportion with the D strategy increased in the early stage, but when the proportions with the S and T strategies both decreased to a certain degree, the proportion with the D strategy began to decrease. For the case where $r _ { 4 } = 6 . 2$ , the result can be explained by the fact that when the proportions of the S and T strategies decreased, there was a decrease in the potential threat to the enterprise’s reputation (the reputation loss caused by the company pursuing the N strategy). In addition, the reputation reward due to the group of netizens increasingly adopting the D strategy was not suficiently large (although it exceeded the cost of responding to the group of netizens who adopted the D strategy) to compensate for the costs of responding to netizens who adopted the S or T strategies. Therefore, the company changed from the P strategy to the N strategy due to the deficit caused by the P strategy, and the D strategy became suboptimal for netizens. For the case where $r _ { 4 } = 5$ , as predicted by Inference 5, the D strategy could not dominate because it inevitably led to a deficit before domination, which made the company change from P to N.

The simulation results confirmed Inference 5. The D strategy dominated if it provided suficient reputation reward for the enterprise, whereas it failed to dominate if the reputation reward was below the response costs. Interestingly, for situations where the reputation reward could cover the response costs but it was not excessively high, the final evolution results showed the important influence of the reputation threat due to netizens selecting other strategies on the tendency for the D strategy to finally dominate. In particular, when the proportions of the other strategies declined rapidly in the evolutionary process to cause a rapid decrease in the potential reputation threat, the company had an incentive to change from the P strategy to the N strategy in order to cut costs, and thus the D strategy became a suboptimal strategy, thereby preventing its increased adoption by netizens. When the threat of reputation loss caused by other strategies for the enterprise remained significant for a relatively long time, the enterprise had a greater incentive to promote the adoption of the D strategy by netizens in order to improve its reputation, thereby leading to the continuous increase and final domination of the D strategy.

## 7. Discussion

In this section, we discuss the basic model, the extended model with complex networks, and the extended model with defending behavior.

## 7.1. Basic Model

According to traditional crisis PR theory, the choice of strategy is mainly afected by the degree and properties of the company’s responsibility during the crisis. Hence, the company needs to respond to direct stakeholders. When confronted by the spread of negative information among the public about a real-world incident, i.e., a secondary crisis on social media, the company needs to pay attention to direct stakeholders but also to the diferent reactions among the public regarding the company’s choice of strategy. From a cost–benefit perspective, we investigated the interaction among the strategy choices made by netizens and a company. By considering the diferentiation of the initial strategies among netizens who are bounded rational and constantly learning from the strategies employed by other individuals to maximize their benefits, we used a general dynamic replication equation in an evolutionary game approach to analyze the dynamic learning process by netizens and its mutual influence on the strategy choices of netizens. Theoretical analysis and simulations of the equilibrium solutions of the model showed that enterprises can influence the strategy choices made by the public by adjusting/setting the compensation value for diferent strategies or costs of actions.

The game starts with the initial distribution of actions by netizens comprising I, S, and T strategies. The initial proportions of the strategies adopted will influence the reputation benefits for the enterprise. In particular, the initial proportion of netizens who adopt the T strategy and the extent of the reputation loss for a company that adopts the N strategy are the factors that determine whether the company adopts the P strategy. The response strategy employed by the enterprise determines the benefits for netizens, thereby leading netizens to learn the strategies with the highest net benefit, i.e., material and emotional benefits from the enterprise’s response, and the main emotional cost of action. Learning leads to changes in the proportions of the diferent netizen strategies, thereby changing the benefits for the enterprise and afecting the crisis communication decisions made by the company.

If an enterprise wants to adopt a more proactive and rather positive stance in its communication strategy, the enterprise should not respond positively only to the agitated netizens who adopt a T strategy, such as by giving positive feedback or compensation only to those who complain, but instead it should give all informed netizens a non-discriminatory positive crisis response, e.g., by ofering apologies and compensation in the form of vouchers. Responding only to the publicly complaining individuals may lead more netizens to adopt a radical T strategy. Giving a positive reaction to all informed netizens will reduce the relative net income of netizens who adopt an aggressive condemnation strategy. The net returns of the T strategy will then potentially be even lower than the returns of the S strategy since the cost of netizens adopting the T strategy is higher $\left( d _ { 2 } > d _ { 1 } \right)$ ), thereby reducing the number of netizens who adopt the T strategy.

## 7.2. Extended Model with Complex Networks

The connection structure on social media is a complex network. The influence of the structural characteristics of the network on the strategy learning behavior of the netizen group is mainly reflected in the diferent information exchange objects. Most social network sites employ broadcast modes of communication, such as hot-topic search or lists of popular, trending stories. However, for individual netizens, the objects that form the basis of their learning behavior are often still the individuals with whom they are connected and the learning behavior is also afected by noise. Diferent clustering coeficients for network connectivity and noise will afect the learning behavior of netizens, i.e., whether they can learn the optimal strategy. More connections and increased communication activity in the network increase the likelihood of learning a suboptimal strategy. By introducing the Fermi function for strategy learning in complex networks and relaxing the assumption of a closed world where everyone knows everyone else, we showed that netizens may choose a suboptimal strategy, which may lead to a change in the dominant strategy. For example, in the basic model, if the S strategy has relatively greater returns than the T strategy, then after the process of evolution, the equilibrium strategy for netizens is the S strategy. However, in the extended model with the addition of bounded rationality assumptions and complex network structures, our simulation results showed that there is a certain probability that the T strategy with comparatively smaller returns become the dominant strategy, e.g., individuals raging over a relatively minor incident. From a business perspective, it is necessary to ensure that the benefits of the S strategy become higher than those of the T strategy to a certain extent in order to avoid continued condemnation by stubborn netizens.

Individuals in the network learn from neighbors and frequent learning increases the chance of making mistakes, i.e., learning a suboptimal strategy. From the perspective of the enterprise, when the optimal strategy of netizens is beneficial to the company (such as the S strategy), the company should try to disincentivize the communication of negative information to prevent netizens from learning other strategies by mistake. Conversely, if the optimal strategy for netizens is not beneficial for the enterprise (such as the T strategy), the enterprise should try to shape the discussion to give netizens the opportunity to learn other strategies. Intuitively, if netizens tend to be moderate, i.e., the S strategy is more profitable, then netizens should be disincentivized from following the lead of more agitated individuals. If netizens tend to be aggressive, i.e., the T strategy is more profitable, netizens should be encouraged to communicate more to adopt other actions.

## 7.3. Extended Model with Defend Strategy

Netizens have the option to defend the company (D strategy) in some situations (such as an irresistible accident), where the company can avoid condemnation for a negative response and be applauded for a positive response. We introduced this strategy to the action set of netizens and showed that the company can give the D strategy group suficient positive feedback to induce the netizens to constantly learn the D strategy only if the praise from the defending group of netizens brings suficient reputation benefit. Otherwise, the company may give up substantive positive feedback in order to save costs, thereby leading the group of netizens who adopt the D strategy to decrease or even disappear.

Simulation analysis showed that the potential threat to the company’s reputation from groups of netizens adopting strategies other than the D strategy is an important factor for motivating the company to pay attention to and positively encourage the D strategy among netizens. The company will give up the positive response when the reputation threat weakens rapidly due to the decreased adoption of other strategies among netizens because the reputation benefits from the increasing D strategy group are not suficiently high to cover the cost of the company’s positive actions.

## 8. Conclusion

In this section, we discuss the theoretical contributions of our research findings and their practical implications. Furthermore, we discuss the limitations of our study as well as identifying open issues for future research.

## 8.1. Theoretical Contributions

We considered the financial and reputational benefits/penalties of adopting diferent strategies based on evolving trends in terms of netizen behavior. Our results also highlight the impact of the strategic choice adopted by an enterprise on the evolution of the behavior of netizens. From a cost–benefit perspective, we considered the interaction between a company and a large, heterogeneous group of stakeholders in crisis communication, i.e., social media netizens. Traditional theories stress that the company should choose an appropriate strategy according to the degree of its own responsibility for the crisis event, but netizens do not necessarily respond to the actions of companies based on the correct attribution of responsibility. We assume that netizens have expectations regarding the actions of a company during a crisis, and the company must decide how much benefit it is willing to concede to netizens. The actions of netizens and a company both

#

have costs, and each player may obtain corresponding benefits, e.g., the fulfillment of expectations in the case of netizens or a reputation gain in the case of the company. The cost–benefit trade-of is the key factor that influences the choice of action strategies.

The expectations of netizens regarding a company are diferentiated, and thus we introduced an evolutionary game model that treats netizens as a heterogeneous group with diferent initial strategies. Netizens influence each other in their choice of strategy, which may be imperfect due to the restricted number of observable action samples and benefit evaluation errors. In an extension to the basic model, we also considered the less common strategy of netizens defending a company during a crisis event.

## 8.2. Implications for Practice

We highlighted the crisis communication principle based on realistic and real-time public behaviors. For companies, it is necessary to improve the monitoring of public opinion on social media and to determine the opinions and actions of netizens in order to respond appropriately when negative information appears on social media. When assessing the potential reputation loss caused by netizens, a company should consider the group of netizens who care but have not yet made clear comments or taken actions.

The results obtained in this study should remind companies to be cautious when they respond to the public. An active response is often necessary but a crisis manager confronted by complex expressions of public opinion has a dangerous intuitive tendency to pay too much attention to the most radical members of the public while ignoring the silent observers, which may finally lead to the radicalization of public opinion and actions. We suggest a more balanced response strategy to encourage desirable netizen behavior, i.e., using a moderate tone in public expressions about the company.

Due to the limits of individual social relations and information channels, as well as the possibility of errors in human judgment and learning, companies should adopt a response strategy that is suficiently friendly to encourage netizen behaviors that are favorable to the company as well as being suficiently firm to avoid continued condemnation by stubborn netizens. Moreover, companies should take measures to encourage or avoid social discussion related to diferent crisis situations in order to influence the public to change their opinions and actions. When the opinions or behaviors of netizens are generally beneficial for the company, the company should avoid public communication and discussion in order to avoid involvement in extended exchanges and risk subsequent radicalization of the discussion. When the opinions and behaviors of netizens are not favorable to the company, i.e., the tone of social media toward the company has become more aggressive, the company should encourage more social discussion to give netizens the opportunity to consider other choices. When the public has a tendency to defend or support companies, companies should encourage this behavior under certain conditions. If the supporters bring suficient reputation improvements, companies should provide rather friendly feedback to strive for a win–win situation, rather than insisting that the company is absolutely not at fault.

## 8.3. Limitations and Future Work

This study had the following limitations. One limitation concerns defending behavior as an option that allows netizens to show tolerance and goodwill to the company with the expectation of a positive response. The model may not explain all types of defending or supportive behavior, e.g., by extremists, loyal fans, or Internet trolls. This behavior seems to involve complex emotional factors and personal characteristics, and thus further study is required to fully understand the defending behavior phenomenon.

We did not focus on how the company might act better during the early stages of a crisis, i.e., from the start of the crisis event to the initial actions of netizens, because this stage is typically very brief and accompanied by much uncertainty. However, this is an interesting and important topic that should be studied in the future. Other interesting topics related to communication during the early stages of a crisis includ the trade-of between an early response and accelerating the difusion of negative information, i.e., companies risk accelerating the spread of negative information if they respond early, the risk of communicating too frequently about the crisis, the response cost constraint, and the principal-agent problem of crisis managers.

In this study, we proposed a framework for crisis communication research based on evolutionary game theory. Future research may consider: (i) the influences of third-party organizations such as the government (influencing the payof of both parties through reward and punishment mechanisms), social media platforms (via content approval or disapproval), and competitors; (ii) the social influence of netizens and the selforganization of netizens, such as the behavior of opinion leaders or the launch of group petitions during a crisis; and (iii) the introduction of psychological theories on discussion, including how anger, optimism/pessimism, overconfidence, and group polarization afect the game equilibrium.

The behavior of netizens is represented as a discrete strategy choice in our model, whereas the actual opinions of netizens are continuous. Future research may study the dynamic evolution of the opinions of netizens and how companies can influence these opinions.

Our preliminary theoretical model also proposes a testable game behavior framework, thereby facilitating further experimental and empirical studies.

## 8.4. Concluding Remarks

Owing to the increasing frequency of PR activities by enterprises on social media, it is necessary to establish a systematic and efective management method for dealing with potential PR crises. Based on a perspective of weighing costs and benefits, we used an evolutionary game model to analyze the interaction between netizens and enterprises during crisis communication, thereby providing guidance for enterprises regarding the appropriate response to a crisis on social media in order to induce netizens with diferent behavioral tendencies to adopt a more favorable position toward the company.

## 1070 References

[1] A. Boin, P. ’t Hart, A. McConnell, Crisis exploitation: political and policy impacts of framing contests, Journal of European Public Policy 16 (1) (2009) 81–106. doi:10.1080/13501760802453221.

[2] J. Falkheimer, Crisis communication and terrorism: The Norway attacks on 22 july 2011, Corporate Communications: An International Journal 19 (1) (2014) 52–63.

[3] J. Choi, S. Lee, Managing a crisis: A framing analysis of press releases dealing with the fukushima nuclear power station crisis, Public Relations Review 43 (5) (2017) 1016–1024. doi:10.1016/j.pubrev.2017.09.004.

[4] F. Schultz, S. Utz, A. G¨oritz, Is the medium the message? perceptions of and reactions to crisis communication via twitter, blogs and traditional media, Public Relations Review 37 (1) (2011) 20–27. doi:10.1016/j.pubrev.2010.12.001.

[5] W. T. Coombs, Protecting organization reputations during a crisis: The development and application of situational crisis communication theory, Corporate Reputation Review 10 (3) (2007) 163–176. doi:10.1057/palgrave.crr.1550049.

[6] B. Zheng, H. Liu, R. M. Davison, Exploring the relationship between corporate reputation and the public’s crisis communication on social media, Public Relations Review 44 (1) (2018) 56–64. doi:10.1016/j.pubrev.2017.12.006.

[7] A. Dyck, N. Volchkova, L. Zingales, The corporate governance role of the media: Evidence from russia, The Journal of Finance 63 (3) (2008) 1093–1135.

[8] L. Fang, J. Peress, Media coverage and the cross–section of stock returns, The Journal of Finance 64 (5) (2009) 2023–2052.

[9] J. Nijkrake, J. F. Gosselt, J. M. Gutteling, Competing frames and tone in corporate communication versus media coverage during a crisis, Public Relations Review 41 (1) (2015) 80–88. doi:10.1016/j.pubrev.2014.10.010.

[10] B. R. Brunner (Ed.), Public Relations Theory: Application and Understanding, Wiley Blackwell, 2019.

[11] T. Bang, Ethics, in: B. R. Brunner (Ed.), Public Relations Theory: Application and Understanding, Wiley Blackwell, 2019, pp. 63–78.

[12] A. Selk, A man wouldn’t leave an overbooked united flight. so he was dragged of, battered and limp, The Washington Post. URL https://www.washingtonpost.com/news/dr-gridlock/wp/2017/04/10/a-man-wouldnt-leave-an-overbookedunited-flight-so-he-was-dragged-of-battered-and-limp (Accessed: 4<sup>th</sup> January 2020).

[13] F. Schultz, J. Raupp, The social construction of crises in governmental and corporate communications: An interorganizational and inter-systemic analysis, Public Relations Review 36 (2010) 112–119. doi:10.1016/j.pubrev.2009.11. 002.

[14] J. Grunig, D. Dozier, Excellence in public relations and communication management, Routledge, 1992.

[15] Y. Cheng, How social media is changing crisis communication strategies: Evidence from updated literature, Journal of Contingencies and Crisis Management 26 (1). doi:10.1111/1468-5973.12130

[16] W. T. Coombs, S. J. Holladay, The handbook of crisis communication, John Wiley & Sons, 2010.

[17] W. T. Coombs, Ongoing crisis communication: Planning, managing, and responding, Sage Publications, 1999.

[18] M. W. Seeger, Best practices in crisis communication: An expert panel process, Journal of Applied Communication Research 34 (3) (2006) 232–244, doi: 10.1080/00909880600769944 doi: 10.1080/00909880600769944. doi:10.1080/ 00909880600769944

[19] W. L. Benoit, Image repair discourse and crisis communication, Public Relations Review 23 (2) (1997) 177–186. doi: 10.1016/S0363-8111(97)90023-0.

[20] E. J. Avery, R. W. Lariscy, S. Kim, T. Hocke, A quantitative review of crisis communication research in public relations from 1991 to 2009, Public Relations Review 36 (2) (2010) 190–192. doi:https://doi.org/10.1016/j.pubrev.2010.01.001.

[21] W. T. Coombs, State of crisis communication: Evidence and the bleeding edge, Research Journal of the Institute for Public Relations 1 (1) (2014) 1–12.

[22] M. Taylor, D. C. Perry, Difusion of traditional and new media tactics in crisis communication, Public Relations Review 31 (2) (2005) 209–217.

[23] S. Kim, B. F. Liu, Are all crises opportunities? a comparison of how corporate and government organizations responded to the 2009 flu pandemic, Journal of Public Relations Research 24 (1) (2012) 69–85.

[24] D. L. Sturges, Communicating through crisis: A strategy for organizational survival, Management Communication Quarterly 7 (3) (1994) 297–316. doi:10.1177/0893318994007003004.

[25] S. Utz, F. Schultz, S. Glocka, Crisis communication online: How medium, crisis type and emotions afected public reactions in the fukushima daiichi nuclear disaster, Public Relations Review 39 (1) (2013) 40–46. doi:10.1016/j.pubrev.2012.09.010.

[26] T. W. Coombs, Crisis management and communications (updated September 2014), Tech. rep., Institute for Publi Relations, accessed: 22 May 2020 (9 2014).

URL https://instituteforpr.org/crisis-management-communications/

[27] S. R. Veil, T. Buehner, M. J. Palenchar, A work–in–process literature review: Incorporating social media in risk and crisis communication, Journal of contingencies and crisis management 19 (2) (2011) 110–122.

[28] D. Liu, W. Wang, H. Li, Evolutionary mechanism and information supervision of public opinions in internet emergency, Procedia Computer Science 17 (2013) 973–980.

[29] D. Gilpin, Organizational image construction in a fragmented online media environment, Journal of Public Relations Research 22 (3) (2010) 265–287.

[30] B. F. Liu, L. Austin, Y. Jin, How publics respond to crisis communication strategies: The interplay of information form and source, Public Relations Review 37 (4) (2011) 345 – 353. doi:10.1016/j.pubrev.2011.08.004.

1130 [31] B. F. Liu, Y. Jin, R. Briones, B. Kuch, Managing turbulence in the blogosphere: Evaluating the blog-mediated crisis communication model with the american red cross, Journal of Public Relations Research 24 (4) (2012) 353–370. doi: 10,1080/1062726X.2012,689901

[32] N. A. Brown, A. C. Billings, Sports fans as crisis communicators on social media websites, Public Relations Review 39 (1) (2013) 74 – 81. doi:10.1016/j.pubrev.2012.09.012.

[33] Y. Choi, Y.-H. Lin, Consumer responses to mattel product recalls posted on online bulletin boards: Exploring two types of emotion, Journal of Public Relations Research 21 (2) (2009) 198–207.

[34] C. Greer, K. Moreland, United airlines’ and american airlines’ online crisis communication following the september 11 terrorist attacks, Public Relations Review 29 (4) (2003) 427–441.

[35] K. Hallahan, Inactive publics: the forgotten publics in public relations, Public Relations Review 26 (4) (2000) 499–515.

[36] K. K. Stephens, P. Malone, If the organizations won’t give us information...: The use of multiple new media for crisis technical translation and dialogue, Journal of Public Relations Research 21 (2) (2009) 229–239.

[37] W. L. Bennett, S. Iyengar, A new era of minimal efects? the changing foundations of political communication, Journal of Communication 58 (4) (2008) 707–731.

[38] Y. Cheng, Social media keep buzzing! a test of the contingency theory in China’s red cross credibility crisis, International Journal of Communication 10 (2016) 20.

[39] J. L. Bradford, D. E. Garrett, The efectiveness of corporate communicative responses to accusations of unethical behavior, Journal of Business Ethics 14 (11) (1995) 875–892. doi:10.1007/BF00882067.

[40] D. Holtzhausen, G. Roberts, An investigation into the role of image repair theory in strategic conflict management, Journal of Public Relations Research 21 (2009) 165–186. doi:10.1080/10627260802557431.

1150 [41] W. T. Coombs, S. J. Holladay, Helping crisis managers protect reputational assets, Management Communication Quarterly 16 (2) (2002) 165–186. doi:10.1177/089331802237233.

[42] A.-S. Claeys, V. Cauberghe, P. Vyncke, Restoring reputations in times of crisis: An experimental study of the situational crisis communication theory and the moderating efects of locus of control, Public Relations Review 36 (3) (2010) 256–262. doi:10.1016/j.pubrev.2010.05.004.

1155 [43] K. M. Hearit, Crisis Management By Apology: Corporate Response to Allegations of Wrongdoing, LEA’s communication series 0, Routledge Ltd, 2006.

[44] B. F. Liu, Distinguishing how elite newspapers and a-list blogs cover crises: Insights for managing crises online, Public Relations Review 36 (1) (2010) 28–34.

[45] B. F. Liu, Efective public relations in racially charged crises: Not black or white, in: Handbooks in Communication and Media, Wiley-Blackwell, Oxford, UK, 2010, pp. 335–358.

[46] M. L. Kent, B. C. Boatwright, Ritualistic sacrifice in crisis communication: A case for eliminating scapegoating from the crisis/apologia lexicon, Public Relations Review 44 (4) (2018) 514–522. doi:10.1016/j.pubrev.2018.06.006.

[47] Y. Jin, B. F. Liu, The blog-mediated crisis communication model: Recommendations for responding to influential externa blogs, Journal of Public Relations Research 22 (4) (2010) 429–455. doi:10.1080/10627261003801420.

[48] C. Carroll, How the mass media influence perceptions of corporate reputation : exploring agenda-setting efects within business news coverage, Ph.D. thesis, University of Texas at Austin (2004).

[49] W. Coombs, S. Holladay, The negative communication dynamic: Exploring the impact of stakeholder afect on behavioral intentions, Journal of Communication Management 11 (2007) 300–312.

[50] J. Conlisk, Why bounded rationality?, Journal of Economic Literature 34 (2) (1996) 669–700.

[51] H. A. Simon, Theories of bounded rationality, Decision and organization 1 (1) (1972) 161–176.

[52] E. Rasmusen, Games and information: An introduction to game theory, Blackwell Oxford, 1989.

[53] R. B. Myerson, Game theory, Harvard university press, 2013.

[54] J. W. Weibull, Evolutionary game theory, MIT press, 1997.

[55] J. Hofbauer, K. Sigmund, Evolutionary game dynamics, Bulletin of the American Mathematical Society 40 (4) (2003) 479–519.

[56] J. M. Smith, Evolution and the Theory of Games, Cambridge university press, 1982.

[57] D. Friedman, On economic applications of evolutionary game theory, Journal of Evolutionary Economics 8 (1) (1998) 15–43. doi:10.1007/s001910050054.

[58] P. D. Taylor, L. B. Jonker, Evolutionary stable strategies and game dynamics, Mathematical biosciences 40 (1-2) (1978) 145–156.

[59] R. Sethi, Strategy-specific barriers to learning and nonmonotonic selection dynamics, Games and Economic Behavior 23 (2) (1998) 284–304. doi:10.1006/game.1997.0613.

[60] M. Taylor, M. L. Kent, Taxonomy of mediated crisis responses, Public Relations Review 33 (2) (2007) 140 – 146.

[61] K. Fearn-Banks, Crisis Communications: A Casebook Approach, 2nd Edition, Routledge, 2001.

[62] I. Ducassy, Does corporate social responsibility pay of in times of crisis? an alternate perspective on the relationship between financial and corporate social performance, Corporate Social Responsibility and Environmental Management 20 (3) (2013) 157–167.

[63] P. Erd˝os, A. R´enyi, On the evolution of random graphs, Publ. Math. Inst. Hung. Acad. Sci 5 (1960) 17–60.

science.286.5439.509.

341 – 346. doi:10.1016/S0375-9601(99)00757-4.

[66] S. Boccaletti, V. Latora, Y. Moreno, M. Chavez, D.-U. Hwang, Complex networks: Structure and dynamics, Physics Reports 424 (4) (2006) 175 – 308. doi:10.1016/j.physrep.2005.10.009.

[67] S. Van Segbroeck, F. C. Santos, A. Traulsen, T. Lenaerts, J. M. Pacheco, Evolution of cooperation in adaptive social networks, in: Handbook on Biological Networks, World Scientific, 2009, pp. 373–392. doi:10.1142/9789812838803\_0016.

[68] G. Szabo, C. T˝oke, Evolutionary prisone’s dilemma game on a square lattice, Physical Review E 58 (1998) 69–73. doi:10.1103/PhysRevE.58.69.

[69] A. Szolnoki, M. Perc, G. Szab´o, Phase diagrams for three-strategy evolutionary prisoner’s dilemma games on regular graphs, Physics Review E 80 (2009) 056104. doi:10.1103/PhysRevE.80.056104.

[70] L. Liu, Rogue Jing Dong, in Chinese, URL https://weibo.com/ttarticle/p/show?id=2309404217132555625111 (Accessed: 15<sup>th</sup> September 2020) (2018).

[71] T. Paper, Jingdong established a new customer experience department at the group level: “youngest vice president” yu rui was at the helm, in Chinese, URL https://www.thepaper.cn/newsDetail forward 2025467 (Accessed: 15<sup>th</sup> September 2020) (2018).

[72] Jingdong, Jing dong 2019 open platform various types of target fees, URL https://rule.jd.com/rule/ruleDetail.action?ruleId=4245 (Accessed: 7<sup>th</sup> January 2020) (2019).

[73] F. Pozzi, E. Fersini, E. Messina, B. Liu, Challenges of sentiment analysis in social networks: An overview, in: F. A. Pozzi, E. Fersini, E. Messina, B. Liu (Eds.), Sentiment Analysis in Social Networks, Morgan Kaufmann, 2017, pp. 1–11. doi:10.1016/B978-0-12-804412-4.00001-2

[74] Twitter, Create a followers campaign, URL https://business.twitter.com/en/help/campaign-setup/create-a-followerscampaign.html (Accessed: 15<sup>th</sup> September 2020) (2020).

[75] A. R. Peiritsch, Starbucks’ racial-bias crisis: Toward a rhetoric of renewal, Journal of Media Ethics 34 (4) (2019) 215–227. doi:10.1080/23736992.2019.1673757.

1215 [76] D. Pontefract, Did the starbucks racial-bias training plan work?, ForbesURL https://www.forbes.com/sites/danpontefract/2018/06/01/did-the-starbucks-racial-bias-training-plan-work/ (Accessed: 9<sup>th</sup> January 2020).

[77] A. Orso, One year later: A timeline of controversy and progress since the Starbucks arrests seen ’round the world, The Philadelphia Inquirer.

[78] D. T. Dingle, Two years after landmark racial bias training, starbucks advances civil rights and inclusion agenda, Black EnterpriseURL https://www.blackenterprise.com/two-years-after-racial-incident-starbucks-advances-civil-rights-andinclusion-agenda/ (Accessed: 15<sup>th</sup> September 2020).
