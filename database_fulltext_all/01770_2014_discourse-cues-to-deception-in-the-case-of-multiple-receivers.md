---
otero_id: 1770
otero_key: "NXUKYYFV"
title: "Discourse cues to deception in the case of multiple receivers"
authors: "Lina Zhou; Jiang Wu; Dongsong Zhang"
year: "2014"
journal: "Information & Management"
doi: "10.1016/j.im.2014.05.011"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: Discourse Cues to Deception in the Case of Multiple Receivers

Author: Lina Zhou Jiang Wu Dongsong Zhang

![](/api/attachments/NXUKYYFV/fulltext/images/146767b3dd2807fa375f9f8758503f3a9193d74c03e85707f89d02c899a6971d.jpg)

PII: S0378-7206(14)00064-0

DOI: http://dx.doi.org/doi:10.1016/j.im.2014.05.011

Reference: INFMAN 2728

To appear in: INFMAN

Received date: 31-7-2012

Revised date: 10-5-2014

Accepted date: 20-5-2014

Please cite this article as: L. Zhou, J. Wu, D. Zhang, Discourse Cues to Deception in the Case of Multiple Receivers, Information and Management (2014), http://dx.doi.org/10.1016/j.im.2014.05.011

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Discourse Cues to Deception in the Case of Multiple Receivers

Lina Zhou Department of Information Systems University of Maryland Baltimore County Baltimore, MD 21250 zhoul@umbc.edu Phone: (410)4558628 Fax: (410)4551073

Jiang Wu School of Economic Information Engineering Southwestern University of Finance and Economics SiChuan, P.R.China Jiang.woo@gmail.com

Dongsong Zhang

Department of Information Systems

University of Maryland Baltimore County

Baltimore, MD 21250

zhangd@umbc.edu

## Research Highlights:

1. Systematic discovery and empirical validation of discourse cues to deception when a deceiver interacts with multiple receivers.

2. Investigation of deception behavior by looking into the discourse of online interaction.

3. Creation of a discourse framework that can guide the discovery of discourse features of deceptive communication.

4. Identification of new deception behaviors (e.g., disturbance) and discourse features (e.g., action-directive, change topic).

# Discourse Features of Deception Behavior in the Case of Multiple Receivers

## Abstract

primary sources of deception behavior, text has been analyzed at the level of subsentence or message but not the discourse of interaction. Additionally, empirical studies on cues to deception in the case of multiple receivers remain nonexistent. To fill these voids, we propose a discourse framework and six hypotheses about deception behaviors in a multi-receiver environment. The deception behaviors are operationalized by discourse features based on an analysis of real-world data. The results of statistical analysis validate the efficacy of discourse features in discriminating deceivers from truthtellers.

Keywords: Deception Behavior, Discourse of Interaction, Discourse Feature, Discourse Analysis, Deception Detection

## 1. Introduction

Deception has become increasingly prevalent, accelerated by the fast-evolving communication technologies and expanding online social networks. One recent study reported that 73% of Internet users believe that online deception is widespread [1]. Incidents like the “Craigslist killer” and frequent occurrences of identity theft via online phishing exemplify the severity and extent of deception. The impact of deception can be particularly widespread when it involves multiple targets or receivers. Unfortunately, the accuracy of deception detection by an average person remains poor [2, 3]. Deceivers‟ strategic behavior and information management makes it difficult for people to identify deceptive messages [4]. The low detection success rate is also attributable to our limited knowledge about cues to deception and their applicable context [5]. This research aims to advance knowledge about cues to deceptive communication that involves multiple receivers, which will lead to improvement in the performance of deception detection.

A significant percentage of existing cues to deception belong to verbal behavior (cf.

[6]), which is related to content production and language usage [7]. Text has been used as

the predominant source of verbal cues to face-to-face deception [6] as well as online

deception [8]. Moreover, text is the preferred discourse medium for online

communication [9] due to its affordability and accessibility in relation to video and audio.

However, being low in richness[10] and natural symbol sets [11], text constrains the

amount of incoming and outgoing information that could be used for detecting deception.

Previous research has focused on text-based features at the level of sub-sentence or

message level [7, 8, 12, 13]. The discourse of interaction remains under-explored for detection of deception. Therefore, there is a great need for deception detection researchers to tap into the full potential of text in discovering cues to deception.

Discourse looks beyond individual words and sentences in analyzing written or spoken communication, with the premise that individual elements of a system only have significance when they are considered in relation to the structure as a whole [14]. Some textual features such as restatement and agreement (cf. [6]) can only be interpreted in reference to the discourse of interaction. Therefore, studying discourse deception cues will help researchers extend and enrich the literature on cues to deception.

Modern technologies have made it increasingly common and easy for one user to however, have mainly focused on dyad and monologue contexts with few exceptions [5, 8] (cf. [6]). In view of the different group dynamics between large groups and dyads [15], a deceiver may change his behaviors when interacting with multiple receivers from that with a single receiver. An earlier study made several propositions about deceptive communication when engaged with a group of receivers [16]. However, these propositions are focused on some individual, situational, and group factors rather than deception behavior, A recent study examined the individual determinants of deception performance instead of deception behavior in group communication [17]. To fill these voids, this research aims to address the following question: What discourse features can be used to identify deceptive communication with multiple receivers?

This research potentially contributes to deception research in several important ways. To the best of our knowledge, this is the first research that systematically investigates discourse cues to deception. This study discovers and empirically validates discourse cues to deception when a deceiver interacts with multiple receivers. Fundamentally, our research findings suggest that the detection of deception should take into account features extracted from the discourse of interaction. The proposed discourse framework provides guidance for the discovery of discourse features of deceptive communication. New topic change) identified in this study advances the knowledge on cues to deception.

The rest of the paper is organized as follows. First, we review relevant research on deception and linguistic discourse, and introduce the possible role of discourse features in the detection of online deception, which leads to the proposition of hypotheses on deception behavior in the case of multiple receivers. Then, we introduce the procedure of data collection and data analysis, report the result of statistical analysis, followed by discussion of the findings of this study and their theoretical and practical implications. The final section concludes the paper.

## 2. Background

In this section, we classify text-based cues to deception, discuss the discourse characteristics of online communication, and review extant cues to online deception.

## 2.1. Classification of text-based cues to deception

A variety of information channels in face-to-face communication have been utilized to look for deception behavior, including verbal, vocal, visual, and proximal modalities. However, only a subset of those channels is commonly accessible in online communication. In particular, verbal behavior has been widely studied because deception is strategically manifested in information management. While deceiving others, deceivers usually start by employing various strategies to withhold truthful information, followed by opting for vagueness and uncertainty if withholding does not work, and finally resorting to non-immediacy if the first two fail [4, 18]. These strategies may be executed through a collection of linguistic choices. Text-based cues are proven effective for detecting face-to-face deception based on the results of a myriad of scientific investigations (cf.[6]).

[Insert Table 1 about here.]

Text analysis can be performed at five levels, including word, phrase, clause, sentence, and discourse, in the ascending order of the scope of context. As shown in Table 1, word is the smallest meaningful unit of speech that can stand by itself [19]. Words can be put together to build larger elements of language, such as phrases, clauses, and sentences. It should be pointed out that the lines between some of these linguistic constituents such as clauses and sentences are difficult to draw in online communication, especially for the synchronous modality. Unlike other linguistic units that are confined to the scope of a single sentence or sub-sentence, discourse involves a set of coherent utterances that constitute an intentionally meaningful message. It has been argued that the principal object of linguistic analysis should be texts rather than sentences [20]. In other words, the interpretation of particular linguistic functions or expressions ought not to be bounded by a sentence, but approached from the view of a coherent text.

Discourse analysis studies the way in which language is used in text and contexts by taking into account a unit of language larger than a single sentence [14]. In other words, the goal of discourse analysis is to understand the information in an extended sequence of utterances that goes beyond the meaning of individual utterances. For instance, the interpretation of two cues to face-to-face deception (cf. [6]), logical structure and external association, relies on understanding of the discourse of interaction. However, there is a lack of systematic investigation of the discourse features of deceptive communication in either traditional or online environment.

## 2.2.Discourse of Online Communication

Some characteristics of online discourse sets it apart from face-to-face communication. Text is the primary data type available in computer-mediated interaction, making linguistic information one of the few sources available to provide impressions and supply relational information [21].

Although many characteristics of oral and written discourse have been transposed onto online discourse [9], the latter is a unique form of speech. Emerging communication most important characteristics of online discourse include the ability of linking one online text to another to form a discursive thread, and the social aspects of online discourse that are implemented across time and space in unique, unprecedented ways [9]. Collectives of authors/readers can weave online discourses interactively through either implicit links (e.g., question-answer interaction in online chat or Web forums [22]) or explicit links (e.g., blog and wiki link structure). Therefore, discourse is one of the lenses that hold promise for understanding deception behavior in online communication.

Studies on deception behavior in online communication have generated promising results (e.g., [7, 8, 12, 13]). For example, deceptive messages have been found to be longer, more informal and uncertain, more expressive and non-immediate, less complex, and less diverse than truthful ones. However, previous studies share one common limitation in that they treat texts as bags of words and phrases, while ignoring the discourse of interaction. Speech act profiling [23, 24] has shown promise in aiding deception detection by identifying those speech acts that are related to uncertainty. Nevertheless, these studies are focused on developing speech act profiles of synchronous conversations instead of identifying specific discourse cues to deception.

In view of the potential of discourse information for understanding deception behavior, the unique characteristics of online discourse, and the dearth of research on discourse features of deceptive communication, this research aims to identify cues to deception by examining discourse of interaction.

## 3. Hypotheses Development

Drawing from traditional research on cues to face-to-face deception [6], discourse theories [25-27], and characteristics of online discourse, we propose some general hypotheses regarding discourse cues to deception with special focus on online communication involving multiple receivers.

According to Walczyk et al.‟s cognitive model of deception [28], a deceiver would start with deciding and planning what to say, namely the construction phase. During the following phase of social interaction, the deceiver would in general try to manage impressions and convey images of himself or herself in self presentation, which are different from what the truth-tell would do [6]. According to IDT (Interpersonal Deception Theory) [4], the deceiver engages himself in more strategic activities than the truth-teller to manage information, behavior, and image and to reduce suspicion. Deliberate self-regulatory efforts may be especially likely to usurp mental resources,

#

leaving deceivers more pre-occupied than truth tellers. It is suggested that when a deceiver try to avoid detection, he strives to avoid looking like the deceiver by suppressing those behaviors that can be controlled [29]. One common way of creating deception is thus to employ the substrategy of avoidance where deceivers are likely to hide information as much as possible by deviating from direct response and staying on topic [30]. Members of larger groups, as opposed to members of a dyad, are rarely connected directly to all other members [15]. Such a lack of direct connection would further motivate the deceiver to choose the avoidance strategy in interacting with multiple receivers. Therefore, deceivers tend to respond less and in less detail, and be holding back [6]. In other words, deceivers‟ messages seem less forthcoming.

H1 Deceivers’ messages will be less forthcoming than truth-tellers’ in case of multiple receivers.

Dominance is a behavioral state that reflects the actual attempts of influence or control of one person over another via communicative actions [18]. Substantial research has reported that deception is often characterized by less verbal or nonverbal dominance (or more submission) than truthful communication [31-34]. Individuals have difficulty in embracing their false claims as convincingly as truthful ones because in most societies, lying is against the social norms and deceivers may feel guilty. Thus, deceptive communication is likely to be more submissive than truth-telling.

Prior studies [18, 35, 36] have suggested that unlike a truth-teller, a deceiver would keep low-key to protect himself from being suspected at the beginning. Once the deceiver develops an interpersonal relationship with others, which reduces the immediate threat to the self-image, he will begin increasing dominance over time [18]. Since it takes more time and effort for a deceiver to build rapport when communicating with multiple receivers than with a single receiver, the deceiver in the former case would be more likely pre-occupied with protecting himself as much as needed before resorting to a dominant position. Therefore, we propose the following hypothesis:

H2 Deceivers’ messages will be less dominant than truth-tellers’ in case of multiple receivers.

Cooperativeness indicates a sender being supportive, helpful, and secure [6]. Deception is stressful. Cooperation with the group majority or agreement with multiple receivers would help a deceiver relieve stress without compromising his own deceptive goal. During the initial formation of a trust relationship, one of the contributing factors is categorization process such as “stereotyping” [37]. Stereotyping means placing one person into a general category of persons. In a group environment where members are working together toward a common goal, cooperation with receivers helps a deceiver being quickly placed into a favorable category and forming positive beliefs by receivers. Moreover, being cooperative by a deceiver also gives receivers the illusion of control in the process, making them over-confident about their judgment [38]. Furthermore, when a deceiver interacts with multiple receivers, the deceiver‟s opinions and attitudes appear to be under the normative social influence of receivers in that the deceiver senses the “strength in numbers” about the position of receivers from the same group. As a result, the deceiver would seek conformity, the most dominant form of social influence [39], to the group majority‟s viewpoint to avoid the disapproval or relationship conflict caused by possessing a minority viewpoint. These cooperative behaviors may lower the chance that receivers generate doubt on deceptive communication. In contrast, a truth-teller does not have to protect himself by compliance but focus on the group task at hand. Therefore, we propose that:

H3 Deceivers’ messages will be more cooperative than truth-tellers’ in case of multiple receivers.

Adapted from [40], logical expressions are defined as a coherent account of a collection of details. Deceptive communication is less likely to be structured in a logical and sensible way than truthful communication (cf. [6]). Even if individual deceivers overcome the deterrent of social norms, they may not have the same personal experience with their claims as truth tellers. Markus [41] argues that self-relevant claims are based on an accumulation of knowledge, experience, and wisdom that most liars can only imagine. Additionally, an expression of logical inference adds evidence and detail to a story, which may increase the possibility of self-contradiction due to faulty logic. For instance, if a deceiver lies not only about an event, but also about why and how it happened, he is more likely to be detected due to logical inconsistencies by multiple receivers. Thus, we propose the following hypothesis:

H4 Deceivers’ messages will be less logical than truth-tellers’ in case of multiple receivers.

Instead of being friendly, pleasant, and likable, the act of deception is typically associated with anxiety, shame, and guilt [6]. Deception produces arousal resulted from being fearful or apprehensive about being detected [42]. Previous research suggests that increased levels of negative emotion are expressed during deceptive communication compared with truthful communication [8, 43-45]. Deceivers may also experience guilt when they violate the conversational expectation for truth. Therefore, we propose that:

#

H5 Deceivers’ messages will be less pleasant than truth-tellers’ in case of multiple receivers.

In view of the similarity between online discourse and speech [7, 46], disturbance that reflects disfluency in spontaneous speech can be transposed onto online communication. Based on their underlying functions, verbal disturbances can be classified into two categories [47, 48]: non-ah disturbances that indicate the state of anxiety, and the common place filled pauses that occur “when the available options for what to say or how to say are many and complex” (cf. [6]). Some frequently occurring non-ah disturbances include interrupting the flow of a sentence, superfluous repetitions of words or phrases, incomplete sentences, intruding incoherent expressions, and so on [6]. Filled pauses are pauses filled with utterances that are not based on particular verbal expression systems such as online chatting. In addition to performing assigned tasks as truth-tellers do, deceivers have to invest greater amounts of effort regulating their own behavior based on the responses of receivers in order to evade from detection [4]. This may cause disrupt to deceptive communication. Consequently, despite strategic control, deceivers tend to leak behavioral cues via less controllable non-verbal channels [42, 49]. Moreover, people process concurrent information less deeply when they are preoccupied with intrusive mental contents such as deception, compared with those who are not such as truth-telling [50, 51]. Thus, deception has a disturbing and dampening effect on verbal expression [30, 52, 53]. Therefore, we propose the last hypothesis as follows:

H6 Deceivers’ messages will be more disturbed than truth-tellers’ in case of multiple receivers.

#

## 4. Research Design

We used a mixture of qualitative and quantitative methods in this study. The qualitative method was used to analyze discourse features of text messages collected from a mafia game website, and the quantitative method was used to test the proposed hypotheses.

## 4.1. A Discourse Framework

To support a systematic investigation of discourse features of deceptive communication, we proposed a discourse framework by drawing upon the literature from a multitude of relevant fields, including linguistics, deception, negotiation, computer-supported collaborative work, psychology, and computer-mediated communication.

[Insert Figure 1 about here.]

The framework contains four major components, including linguistic discourse, domain discourse, task discourse, and application discourse, which are described below.

 Linguistic discourse describes general discourse structure and relations like contingency, which are independent of a particular problem or domain.

Domain discourse describes discourse features characterizing a generic domain such as deception by particularizing the constructs introduced in the linguistic discourse.

 Task discourse describes the vocabulary related to a generic task or activity such as negotiation and decision making by particularizing the constructs introduced in the linguistic discourse.

 Application discourse is the most specific component, which corresponds to domain entities performing certain tasks in selected domains. In case of the mafia game, which will be introduced in section 4.3, a deceiver deceives other group members during a decision making task.

As shown in Figure 1, there are inheritance relationships between different types of discourse, as denoted by blank-headed arrows pointing to more abstract types of discourses. Moreover, all the four types of discourse are subject to the influence of communication media capabilities (e.g., parallelism in terms of transmissions that can take place simultaneously, and symbol sets that can be used to encode a message in different ways [11]), communicating partners (e.g., group size, familiarity, and experience), and conversation persistence (e.g., one-time vs. repeated interaction, and early vs. late phase of communication). For example, differences exist between online chat and email in terms of parallelism of media capability, group size of communicating discourse [7], whereas email is neither speech nor writing, but a hybrid discourse [54]. Additionally, the discourse of online chat is more intertwined and thus more difficult to disentangle than that of emails. Further, Channel Expansion Theory [55] suggests that a sender typically has less understanding of a task, media, and receiver(s) at an early than at a late stage of communication; and these understandings get improved over time as the communication evolves. According to Media Synchronicity Theory [11], communication will involve more conveyance processes at the early phase and more convergence process at the late phase. Such a shift in the fundamental process of communication can have significant implications for linguistic discourse or language use in general, irrespective of media selection.

## 4.2.Initial Discourse Features

The discourse framework provides guidance for our selection of discourse features. The initial selection process was focused on validated models and theories from related areas.

## 4.2.1. Linguistic discourse

We identified three models of linguistic discourse as the theoretical foundation for feature selection, including PDTB (Penn Discourse Treebank), LUNA (Language UNderstanding in multilinguAl communication systems), and DA (Dialogue Acts).

PDTB focuses on encoding discourse relations in corpora consisting of both written and spoken discourse [56]. One of the strengths of PDTB is that it follows a lexically grounded approach where discourse relations are triggered by explicit phrases and by structural adjacency [56]. This makes it easy to understand. PDTB provides sense annotations for explicit connectives, implicit connectives, and alternative lexicalizations. In all cases, sense tags provide a semantic description of a relation among the arguments of connectives. The tag set of senses is organized hierarchically into three levels: class, type, and subtype. The top-level semantic classes are refined by the second-level types, which are further refined by the third-level subtypes based on the semantic contribution of each argument. For instance, contingency class contains cause and condition types, among others, and cause is further specified by reason and result subtypes. PDTB has been adapted to analyze discourse features of languages such as Chinese [57]. Following the view of [57], we adopted a more semantically motivated sense annotation scheme for Chinese text.

The major portion of the text in PDTB corpora involves monologue such as Wall Street Journal articles. Online group chat, however, resembles conversational speech and is thus dialogic [7]. To this end, LUNA [58] revises the sense hierarchy and associated tags in PDTB by taking into account pragmatic aspects of conversational speech in spontaneous dialogs. Like PDTB, LUNA follows a three-layered classification scheme, with the top level containing four semantic classes describing the semantics of relations. The differences between LUNA and PDTB lie in the bottom two levels. For instance, cause type from the second level is further specified in terms of semantic, epistemic, and speech-act aspects at the third level. Because messages from synchronous online chatting are characterized as fragmented, short, and ungrammatical [7], relations among arguments of connectives are not always applicable. In addition, the third-level annotation schema is too detailed to be operable. Therefore, we mainly extracted discourse features from the second-level senses such as cause and condition [56].

The identification of DAs is considered as a useful first step in analyzing the discourse structure of conversational speech [59]. A DA represents the meaning of an utterance at the level of illocutionary force [60]. DAs could be thought of as a tag set that classifies utterances according to a combination of pragmatic, semantic, and syntactic criteria. There is a set of well-defined DAs consisting of 49 tags [59], which include statements (descriptive, narrative, or personal), opinions (other-directed opinions), questions (yes-no, declarative, and wh-questions), turn exits and abandoned utterances (i.e., breaking off words and following with a restart), answers, agreements, and so on. For example, statements may reveal someone‟s belief, personal experience, and identity; questions may entail collection of additional details based on the account of a sequence of interactions; and abandoned utterances indicate a state of verbal disturbance.

## 4.2.2. Task Discourse

We chose group negotiation and decision making as the task discourse. Accordingly, we drew upon the negotiation literature that explores the interaction between relational and strategic messages [61]. Accordingly, behavioral cues are created along a continuum of integrative–distributive orientations. Based on their relevance to the selected task, the following cues were selected, including complying, integrating, stating demands, rejecting other's demands, and threatening to take actions [61].

## 4.2.3. Domain Discourse

Traditional deception theories[62] suggest that some discourse features are associated with deception, such as agitation and guilty delight. Additionally, some discourse cues such as logical structure, reproduction, and subjective experience can be found in criteria-based content analysis, one of the most widely used veracity assessment technique for discriminating between accounts of true and fabricated events (e.g., [63, 64]). Further, a meta-analysis of 158 cues to deception reveals some effective discourse features such as cooperation and issue-related reporting style [6].

## 4.2.4. Application Discourse

In the selected mafia game, a group of players, consisting of both mafia and non-mafia members, collectively negotiate and make a decision about who is most likely to be the most votes as a mafia suspect will be eliminated from the game. The remaining members, if the mafia player is included, will proceed to the next round and the same process will be repeated. The winner of a game is either the mafia or the rest of the group depending on who survives at the end. In order to win the game, the mafia is motivated to deceive and non-mafia players are motivated to tell the truth. Once a player is identified as a mafia suspect, he/she would be accused of „wrong-doings‟. Thus, accusation is a promising discourse feature of the selected application.

Based on the above-mentioned various types of discourse features, two deception experts on the research team were asked to compile an initial list of discourse features. Each expert had extensive research experience on verbal deception behavior. The creation of the list at this stage was focused on relevance and coverage of discourse features. Based on the results of self-selection and subsequently two rounds of discussion, a list of 23 features was identified. The list reflects the consensus of the two experts, providing evidence for face validity of the selected features [65]. A subset of these features, and their discourse types, sources, and descriptions are summarized in Table 2. The remaining features, which were revised or introduced based on the results of discourse analysis, are listed in the last column of the table. The detailed procedure of discourse analysis is introduced in Section 4.4.

[Insert Table 2 about here.]

## 4.3.Data Collection

To test the hypotheses, we collected data from an online mafia game. Each game consisted of one mafia, one policeman, and multiple villager players (ranging from four to eight). The goal of the game is for each group to identify the member who plays the role of mafia. In order to win a game, the mafia has to simultaneously deceive and evade from detection, and the policeman and villagers detect the deceiver (i.e., mafia).

The game proceeds by runs, with each run consisting of two stages: group discussion and voting, and individual elimination or inspection. The entire group participates in the discussion and voting of mafia suspects through a public online chat room. During individual stage, the mafia player claims his privilege of eliminating one of the innocent receivers via voting in a private chat room, and the policeman uses his privilege of inspecting the true identity of a mafia suspect via a separate private chat room. The game moves into the next run unless one of the termination conditions is met: either the mafia or all the non-mafia participants have been eliminated. The side who stays the last wins. In view of the game role and composition, mafia was selected as the deceiver, policeman as the truth-teller, and villagers as receivers to investigate discourse cues to deception.

Stubbs [20] stresses the importance of naturally occurring linguistic data rather than intuitions in text or discourse analysis, which is consistent with the tradition of social linguistics. Thus, we crawled real-world data from a Chinese game website over a onemonth period. We collected group discussion messages in the order that they were received along with their senders‟ identifiers over all runs of each game. An excerpt of a chat session is shown in Appendix A.

From the collection of 1,192 valid games, we randomly selected 200 games according to the following two criteria: 1) the number of runs was three or more. Fewer runs seemed to be noisy and were thus excluded; and 2) the number of messages ranged between 60 and 110. The thresholds for the number of messages were set based on the mean (= 85.20) and standard deviation (= 28.5) of the entire data collection. In addition, none of the selected games shared the same pair of mafia and policeman players.

## 4.4.Discourse Analysis

Discourse analysis builds on both content analysis and conversation analysis but focuses on language constructions formed through a sequence of social interactions or verbal moves [66]. The discourse analysis in this research consists of two studies: pilot study and formal study. The pilot study was conducted with five new games separately selected from the dataset to test whether 1) the discourse features are defined clearly, 2) different features can be discriminated one from another, and 3) the discourse features are valid for the task environment.

Two native Chinese speakers were recruited as coders in the pilot study to analyze the data independently. To support data analysis, we prepared detailed instructions in Chinese that contained definitions and examples of the set of selected discourse features. The coders were first asked to prepare themselves in two ways: 1) getting familiar with the mafia game environment by playing ten or more games at the chosen game website over a one-week period, and 2) understanding the discourse features based on their descriptions and illustrative examples. The first author addressed any questions that the coders had about the discourse features and the coding process.

After the coders felt comfortable with the discourse features and the game data, they started analyzing messages extracted from the five games. The coders were presented with the entire body of messages and their associated senders of each game, and were asked to analyze the messages from two players while using the messages from other players as the context for discourse analysis. The two players assumed the role of mafia and policeman, respectively. Again, the mafia was treated as the deceiver and the policeman as the truth-teller by game design. The messages from the two roles were highlighted, but the coders were not informed of the role of each player. For each message, the coders were asked to annotate up to three discourse features, which could be either selected from the pre-compiled list or created from scratch.

The annotation results from the two coders were consolidated and differences were resolved via face-to-face discussion that involved the two coders and the first author. Their consensual assessments were used as the final results. For a small number of unresolved cases, the majority rule was applied. Based on the feedback from the pilot study, the initial list of discourse features was updated in the following ways: 1) features that were semantically similar or opposite to each other were grouped together, 2) rarely used features were removed (e.g., guilty delight), and 3) missing features were included (e.g., agitation and interrupted/continuer). For instance, interrupted/continuer, denoting that the sender interrupts the flow of a message and continue it in a following message during group online chat, was grouped into disfluency. Finally, we were left with 15 discourse features, as listed in feature column of Table 2. The descriptions of the updated features were revised and discourse types adjusted accordingly.

The formal study was performed on the 200 selected games. The procedure was similar to that of the pilot study with the two enhancements: 1) three coders were involved in the data analysis, and 2) the refined list of 15 discourse features was used. The data analyses and results reported hereafter would be based on the formal study.

## 4.5. Reliability Check

The three coding results were compared to check for inter-rater reliability. We selected Krippendorff‟s alpha interval statistic [67] because it can be applied to any number of observers, categories, scale values, or measures, and any metric or level of measurement without requiring a minimum. The results show that alpha values range between 0.435 and 0.877. Among the 15 features, five achieved acceptable levels of reliability based on the suggested threshold [67], including accusation, agreement/accept, action-directive, question, and non-verbal. To better explain the moderate levels of reliability of the remaining ten discourse features, we performed pair-wise inter-rater reliability tests. The results show that Krippendorff‟s alpha values for all the discourse features between two of the coders were consistently higher than the recommended threshold (i.e., 0.667) [67], suggesting possible systematic bias in the third coder‟s results. Thus, we adopted the rule of majority vote in consolidating the three sets of annotation results.

## 4.6. Grouping and Operationalization of Linguistic Discourse Features

Since different discourse features may manifest the same underlying deception behavior, we further grouped the list of discourse features under higher order deception behavior. Given the rich literature on deception theories and deception behavior on one hand and currently fragmented knowledge about discourse features of deception behavior on the other, the grouping process followed a combination of deductive and inductive methods (cf. [68]). Specifically, we first developed a categorization matrix of deception behavior based on the extant deception literature. By following a deductive process [69](cf. [68]), all the finalized discourse features were then reviewed for content and coded for exemplification of the identified categories of deception behavior. Finally, the discourse features that do not fit the categorization frame were used to create their own deception behavior based on the principles of inductive content analysis.

The above grouping tasks were performed collectively by the same two deception experts who had helped create the initial list of discourse features. To further test content validity of the deception behavior, we separately recruited five researchers who were not on the team to map the discourse features to the categorization matrix independently. The coders were provided with the list of 15 discourse features along with their descriptions and examples, as well as the extended category matrix of deception behavior produced by the two experts. The coding process was repeated by round. After each round, the independent researchers were provided with an anonymous summary of categorization results from the previous round, and they were also encouraged to revise their previous results and provide justifications for their answers in light of the responses of other members. This process was stopped after all the coding results became stable. Therefore, the proposed categories of deception behavior were both conceptually and empirically grounded [70].

Eight discourse features achieved consensus among the five coders in the first around, and another three in the second round. The coding results of the remaining features became stabilized after the third around. Since these remaining features, including reject, restatement, threat to take action, and agitation, all had a majority choice, allowing us to apply the majority rule to finalize the categorization results.

## [Insert Table 3 about here.]

The operationalizations of deception behaviors with discourse features are listed in Table 3. All of the manifesting features were aggregated at the game level for each participant and then normalized by the total number of messages sent by the participant.

## 4.7.Results

Table 4 reports the descriptive statistics of the discourse features. One-way repeated ANOVA was performed to test the possible effects of deception on discourse cues. The results are reported in Table 5. We reported exact p-values and used the accepted p<0.05 cutoff but did not apply the Bonferonni adjustment due to mathematical, logical, and practical concerns about applying the method in ecological studies, particularly for this current study presenting novel results that could advance knowledge within the field [71].

[Insert Table 4 about here.]

[Insert Table 5 about here.]

The results show that deceivers differ from truth-tellers in five discourse features, including self-disclosure (p<0.05), accusation (p<0.001), action-directive (p<0.05), nonverbal (p<0.01), and topic change (p<0.01). Specifically, deception led to increased levels of non-verbal and topic change, and decreased levels of self-disclosure, accusation, and action-directive. Given that all the hypotheses are directional, the two-tailed test results revealed that two other features, including reject and disfluency, which were greater for deceivers than truth-tellers (p<0.1). Nonetheless, reject showed the opposite direction to our prediction. Therefore, hypotheses H1 and H6 were supported, hypotheses H2 and H3 partially supported, and hypotheses H4 and H5 not supported.

## 5. Discussion

## 5.1. Findings

The primary objective of this research was to examine the discourse of deceptive question of interest was whether the discourse of someone who intends to deceive is different from another who truthfully communicates with multiple receivers. The results suggest that compared with truth-tellers, deceivers are less forthcoming, dominant, and cooperative, and more disturbed in some ways.

#

## 5.2.Additional and Alternative Explanations

The finding that deceivers are less forthcoming confirms the previous findings in faceto-face communication (cf. [6]). As predicted by H1, deceivers are less likely to disclose their own opinions than truth-tellers. The cognitive load of simultaneously forming one‟s deceiver into dodging the topics that may undermine an otherwise truthful interchange. In contrast, truth-tellers can leverage a large amount of evidence to make deception behavior become more salient [72]. Thus, truth-tellers are motivated to contribute relevant evidence to the group by sharing their personal opinions.

The findings on action-directive and accusation provide additional evidence for deceivers manipulating their dominance strategies [18, 73]. The finding of low accusation also suggests that deceivers try to avoid direct confrontation with other group members to reduce relationship conflicts and resulted argumentation and tension. However, deceivers‟ submission strategy discovered from this study runs against the finding of the only extant study of dominance associated with online deception [18]. A comparison of the communication environments of these two studies reveals some important differences: 1) the deceiver in the current study interacted with multiple instead of a single receiver as did in the previous study [18]; 2) the group task adopted in the current study has a demonstrable correct answer (i.e., who is the mafia), which is not the case with the previous group task (i.e., desert survival); and 3) the current communication media is synchronous, which is in contrast with asynchronous media employed in the previous study. One explanation for the lack of effect of threat to take actions can be drawn from animal studies where deception is viewed as one of the basic surviving skills

#

of animals. Animals with a low fighting ability use deception as a profitable tactic to repulse stronger opponents in a stable communication system [74]. The threat tactic can be utilized by the deceiver when he is greatly outnumbered by multiple receivers. On the other hand, such threat may not be effective against non-anxious individuals (cf. [75]). Thus, aggressive attacks toward receivers may not enhance, but instead weaken, the position of the deceiver.

As predicted, the results confirm that deceptive communication is more disturbed by displaying a higher level of disfluency, non-verbal, and topic change than truth-telling. The effort needed to manage fast-paced synchronous group interaction makes deceivers who are preoccupied with fabrication and dynamic adaptation of a complex lie become less fluent in expression and display a variety of disturbances. For instance, a deceiver may turn to non-verbal signals or interrupt message flow in order to keep themselves involved in communication and to gain more time to strategize. Even though the traditional voice channel is not available, non-verbal behavior is still abundant in textbased communication modalities. This is because some non-verbal behavior such as onomatopoeia and interjection can be textualized, particularly in synchronous online communication [7]. In addition, computer-mediated groups show a higher level of social equalization than their face-to-face counterparts [76]. The deceiver could strategically leverage the characteristics of online group communication to distract the group‟s limited attention from the task at hand by changing the topic, and to exert their influence on receivers‟ opinion by managing the timing of messages and frequency of turn-takings.

Contrary to our prediction, this study yields preliminary evidence for deceivers‟ being less cooperative than truth-tellers by showing a higher level of reject. One possible

#

explanation is that a deceiver mostly likely responds with denial when he is confronted with suspicion or when he attempts to prevent the rest of a group from reaching a majority decision. On the other hand, the tendency of deceivers‟ showing a higher level of supportiveness than truth-tellers suggests conflicting evidence. Thus, we cannot draw the conclusion that deceivers are less cooperative than their truthful counterparts. These findings suggest when faced with multiple receivers, a deceiver may try to behave cooperatively until his bottom-line is threatened. The deceiver would then switch to an unsupportive stance. This also partly explains the lack of support for agreement in the current results.

The hypothesis that deceivers are less pleasant than truth-tellers did not receive support in this study, which confirms an early finding from triadic groups but contradicts that from dyads[45]. Take together, these findings suggest that the deceiver is more motivated to fake “friendly” demeanor while attempting to achieve the hidden deception agenda in larger groups. Additionally, the avoidance strategy adopted by a deceiver when faced with multiple receivers may also help conceal and control his negative emotions [17]. Similarly, the hypothesis about logical expressions did not receive support. The finding on question confirms the finding from an early study [45].One alternative explanation is that some characteristics of synchronous online discourse, such as informal language and short and rapid turn-taking [7], make it difficult to fully develop logical arguments using causal and conditional contingency. Another explanation is that although a truth-teller who becomes suspicious of a target may also use questions to verify the credibility of information provided by the target [34, 77, 78] and to curtail lies of omission [79], a deceiver may initiate questions to shift the focus of discussion to other innocent receivers

#

and/or to avoid direct response. Further, based on IDT‟s interactivity principle, deceivers should attempt to engage communication partners in interpersonal communication. Asking questions increases the perceived interactivity of communication, which in turn helps to enhance the believability of a deceiver to multiple receivers. Nevertheless, deceivers displayed a tendency of using less restatement than truth-tellers, which implies their preferences for submission strategies. In group online communication where loafing is a viable option, restatement helps a person reinforce the point that he tries to make. Since a deceptive message deviates from the deceiver‟s true belief and/or actual experience, so minimizing the repetition of the same message helps the deceiver reduce the level of guilty arousal.

It is observed from Table 5 that there are large variations among the participants in usage of some discourse features such as threat to take actions, supportiveness, and agreement/accepting. In other words, some discourse features manifesting deception behavior are subject to individual differences. For instance, deceivers who have strong social skills and are more experienced with the group task may be more capable of concocting „convincing‟ lies by use of causes or conditions.

## 5.3. Theoretical Contributions

This research extends our understanding of deception behavior from the discourse perspective. Fundamentally, the findings of the current study suggest that the investigation of deception behavior should incorporate discourse of interaction that takes into account a larger context than individual messages. To the best of our knowledge, this is the first research that systematically examines discourse features of deception behavior. In addition, this is the first study that identifies and empirically validates discourse cues to deception when a deceiver interacts with multiple receivers. This research provides several major theoretical contributions and implications.

First, this study demonstrates the utility of discourse features for deception detection. It provides theoretical insights on what discourse features are available in or can be transposed onto online communication and how effective these features are for detecting deception. Specifically, seven discourse features, including self-disclosure, accusation, action-directive, topic change, non-verbal, disfluency, and reject, were proven effective.

Second, the proposed theoretical discourse framework provides guidance for the discovery of new discourse cues to deceptive communication. The occasional inclusion of discourse deception behavior in previous studies was ad-hoc and lacking theoretical guidance. The proposed framework enables a systematic investigation of discourse of interaction from linguistics, domain, task, and application aspects, which are both distinctive and interdependent. In addition, the framework suggests that the effectiveness of discourse features is subject to the influence of communication environment (e.g., synchronous online communication).

Third, this study discovers new types of deception behavior such as disturbance and submission, and a number of new discourse features reflecting the deceptive behaviors such as action-directive, accusation, topic change, non-verbal, and disfluency.

Fourth, this research shows that deception behavior identified via the lens of discourse analysis of deceptive communication with multiple receivers and is largely consistent with the submission and avoidance strategies of deception in face-to-face communication [33, 34, 73, 80-82]. The findings of this study indicate that submission strategies could well be extended to online deception, particularly when involved with multiple receivers.

Fifth, a comparison of current findings on online deception behavior and previous findings on face-to-face deception reveals that some deception behaviors such as less forthcoming are generalizable, while some other behaviors such as being cooperative are moderated by the communication environment. A comparison of the findings on pleasantness between the current and a previous study [45] suggests that the behavior is moderated by group size.

Last but not the least, the study of deception in a non-English language remains lacking [83]. This study enriches the deception literature with not only the discourse features but also deception behavior from a non-English context.

## 5.4. Practical Implications

The research findings provide several practical implications. First, the validated discourse cues to deception can be directly used to detect online deception and to develop training material for deception detection. These cues can also be used to develop detection aids that provide deception alerts and explanations. In view that discourse looks beyond individual words, phrases, and messages, incorporating discourse-level cues can be expected to enhance the performance of deception detection.

Second, given the demonstrated value of discourse information in the detection of online deception, designers of computer-based communication tools should provide users with the context of online interaction to facilitate the task of detecting deception.

Third, speaking from our own experience, discourse analysis is by no means simple and straightforward. Detangling the discourse of multi-party communication requires understanding of a complex interaction network formed by multiple messages and their senders. As a result, the analysis of online discourse is both time-consuming and subjective. We were only able to arrive at a list of discourse features after going through multiple rounds of refinements and consolidations over the course of two years. In order to empower general users with behavioral cues to deception, ease-of-use could be factored in selecting promising discourse features of deceptive communication.

## 5.5. Limitations and Future Research

This research motivates future research in multiple directions. First, like other empirical deception studies, we collected deception data from a specific communication environment (e.g., text in a single language). It is important to test the generality of discourse cues to deception discovered in this study to other types of contexts that involve different types of language, domains, group tasks, and/or communication media. Second, there are other discourse features such as m-up and silence for future exploration of deception behavior. Additionally, some of the discourse features identified in the present study such as question, can be further refined. Third, because of the challenges of manually extracting discourse features, it would be highly desirable to develop techniques to automate the process of discourse analysis. It should be noted that discourse techniques still face their own challenges, which need to be addressed in future studies. Fourth, According to an early study of cues to online deception [18], deceivers tend to adjust their language dominance more frequently and more remarkably than truthtellers. Thus, it would be interesting to find out whether and how the use of discourse features in deceptive communication changes over time. Fifth, the efficacy of combining previous low-level text-based cues to deception with current high-level discourse cues warrantees future investigation. Last but not the least, the results of statistical power analysis (see Table 5) show that the observed power of three discourse features of deceptive communication was greater than the suggested threshold (.80) [84], and that of the other four ranged from .455 to .724. Several relatively high p-values are stronger evidence against a null hypothesis than one moderately low value [85], thus the chance of all these results being spurious is extremely improbable. Nevertheless, replication of the current ecological study with a controlled laboratory experiment would help improve the statistical power.

## 6. Conclusion

The increasingly pervasive and evolving online communication has made it ever prone to deception practices. Through both qualitative and quantitative data analyses, this study makes several contributions to the literature by providing some insights into the discourse of deceptive interaction with multiple receivers through the discovery of discourse cues indicative of online deception. These results have significant implications for both research and development in the areas of deception detection and discourse analysis. As online discourse grows and accumulates at an accelerated rate, irrespective of business, interpersonal, or group communications, discourse features will become increasingly important for detection of online deception.

## Acknowledgements

The authors would like to thank the following researchers who have kindly offered tremendous help with the data analysis, XXXXX. This research is supported in part by the National Science Foundation (XXXX: removed due to anonymization). Any opinions, findings, or recommendations expressed here are those of the authors and are not necessarily those of the sponsors of this research.

## References

[1] A. Caspi, P. Gorsky, Online deception: prevalence, motivation, and emotion, CyberPsychology & Behavior, 9 (2006) 54-59.

[2] J.C.F. Bond, B.M. DePaulo, Accuracy of deception judgments, Personality & Social Psychology Review, 10 (2006) 214-234.

[3] J.F. George, K. Marett, P. Tilley, Deception detection under varying electronic media and warning conditions, in: Hawaii International Conference on System Sciences, IEEE, Big Island, HI, 2004.

[4] D.B. Buller, J.K. Burgoon, Interpersonal deception theory, Communication Theory, 6 (1996) 203-242.

[5] L. Zhou, D. Zhang, Automatic deception detection in computer-mediated communication, IEEE Intelligent Systems, 27 (2012) 73-75.

[6] B.M. DePaulo, J.J. Lindsay, B.E. Malone, L. Muhlenbruck, K. Charlton, H. Cooper, Cues to deception, Psychological Bulletin, 129 (2003) 74-112.

[7] L. Zhou, An empirical investigation of deception behavior in Instant Messaging, IEEE Transactions on Professional Communication, 48 (2005) 147-160.

[8] L. Zhou, J.K. Burgoon, J.F. Nunamaker, D. Twitchell, Automated linguistics based cues for detecting deception in text-based asynchronous computer-mediated communication: An empirical investigation, Group Decision & Negotiation, 13 (2004) 81-106.

[9] U. Mejias, Online discourse: past, present and future, in: The 16th Annual Instructional Technology Institute Conference, Utah State University, Logan, Utah, 2004.

[10] R.L. Daft, R.H. Lengel, Organizational information requirements, media richness and structural design, Management Science, 32 (1986) 554-571.

[11] A.R. Dennis, R.M. Fuller, J.S. Valacich, Media, tasks, and communication processes: A theory of media synchronicity, MIS Quarterly, 32 (2008) 575-600.

[12] J.K. Burgoon, J.P. Blair, T. Qin, J.F. Nunamaker, Detecting deception through linguistic analysis, in: H. Chen, R. Miranda, D. Zeng, C. Demchak, J. Schroeder, T. Madhusudan (Eds.) First NSF/NIJ Symposium on Intelligence and Security Informatics, LNCS 2665, Springer-Verlag, Tucson, AZ, 2003, pp. 91-101.

[13] J.T. Hancock, L. Curry, S. Goorha, M.T. Woodworth, Automated linguistic analysis of deceptive and truthful synchronous computer-mediated communication, in: Hawaii International Conference on Social Systems, 2005.

[14] D. Howarth, Discourse, Open University Press, Philadelphia, PA, 2000.

[15] D.R. Forsyth, Group Dynamic, Wadsworth, Cengage Learning, Belmont, CA, 2010.

[16] L.K. Marett, J.F. George, Deception in the case of one sender and multiple receivers, Group Decision and Negotiation, 24 (2004) 29-44.

[17] L. Zhou, Y. Sung, D. Zhang, Deception performance in online group negotiation and decision making: The effects of deception experience and deception skill, Group Decision and Negotiation, 22 (2013) 153-172.

[18] L. Zhou, J.K. Burgoon, D. Zhang, J.F. Nunamaker, Language dominance in interpersonal deception via computer-mediated communication, Computers in Human Behavior, 20 (2004) 381-402.

[19] F. Katamba, English Words: Structure, History, Usage, Routledge, Loudon, 2005.

[20] M. Stubbs, Text and Corpus Analysis: Computer Assisted Studies of Language and Culture, Wiley, 1996.

[21] J.R. Carlson, J.F. George, J.K. Burgoon, M. Adkins, C. White, Deception in computermediated communication, Group Decision and Negotiation, 24 (2004) 5-28.

[22] S.N. Kim, L. Cavedon, T. Baldwin, Classifying dialogue acts in one-on-one live chats, in: Proceedings of the 2010 Conference on Empirical Methods in Natural Language Processing (EMNLP 2010), Boston, USA, 2010, pp. 862–871.

[23] D.P. Twitchell, N. Forsgren, K. Wiers, J.K. Burgoon, J.F.N. Jr., Detecting Deception in Synchronous Computer-Mediated Communication Using Speech Act Profiling, in: P.K.e. al. (Ed.) IEEE International Conference on Intelligence and Security Informatics, LNCS 3495, Springer-Verlag Berlin Heidelberg, Atlanta, GA, 2005, pp. 471-478.

[24] D.P. Twitchell, M.L. Jensen, J.K. Burgoon, J.F. Nunamaker, Jr., Detecting deception in secondary screening interviews using linguistic analysis, in: Intelligent Transportation Systems, 2004. Proceedings. The 7th International IEEE Conference on, 2004, pp. 118-123.

[25] D. Marcu, The theory and practice of discourse parsing and summarization, MIT Press, Cambridge, Massachusetts, London, England, 2000.

[26] J. Baldridge, A. Lascarides, Probabilistic Head-Driven Parsing for Discourse Structure, in: Proceedings of the Ninth Conference on Computational Natural Language Learning (CoNLL), Ann Arbor, MI, pp. 96-03.

[27] C. Sporleder, A. Lascarides, Exploiting linguistic cues to classify rhetorical relations, in: Recent Advances in Natural Langauge Processing (RANLP), Bulgaria, 2005.

[28] J.J. Walczyk, K.S. Roper, E. Seemann, A.M. Humphrey, Cognitive mechanisms underlying lying to questions: Response time as a cue to deception, Applied Cognitive Psychology, 17 (2003) 755–774.

[29] J.E. Hocking, D. Leathers, Nonverbal indicators of deception: a new theoretical perspective, Communication Monographs, 47 (1980) 119–131.

[30] D.B. Buller, J.K. Burgoon, A. Buslig, J. Roiger, Testing Interpersonal Deception Theory: The language of interpersonal deception, Communication Theory, 6 (1996) 268-288.

[31] B.M. DePaulo, Decoding discrepant nonverbal cues, Journal of Personality & Social Psychology, 36 (1978) 313–323.

[32] M. Zuckerman, M.D. Amidon, S.E. Bishop, S.D. Pomerantz, Face and tone of voice in the communication of deception, Journal of Personality and Social Psychology, 43 (1982) 347–357.

[33] D.B. Buller, J.K. Burgoon, A.L.S. Buslig, J.F. Roiger, Interpersonal deception VIII. Further analysis of nonverbal and verbal correlates of equivocation from the Bavelas et al. (1990) research, Journal of Language and Social Psychology, 13 (1994) 396-417.

[34] J.K. Burgoon, D.B. Buller, K. Floyd, Does participation affect deception success? A test of the interactivity principle, Human Communication Research, 27 (2001) 503-534.

[35] R.E. Kraut, Verbal and nonverbal cues in the perception of lying, Journal of Personality and Social Psychology, 36 (1978) 380-391.

[36] J.B. Stiff, G.R. Miller, "Come to think of it ....": Interrogative probes, deceptive communication, and deception detection, Human Communication Research, 12 (1986) 339-358.

[37] D.H. McKnight, L.L. Cummings, N.L. Chervany, Initial trust formation in new organizational relationships, The Academy of Management Review, 23 (1998) 473-490.

[38] P.W. Paese, J.A. Sniezek, Influences on the appropriateness of confidence in judgment: Practice, effort, information, and decision-making, Organizational Behavior and Human Decision Processes, 48 (1991) 100-130.

[39] L. Zhou, D. Zhang, Typing or messaging? Modality effect on deception detection in computer-mediated communication, Decision Support Systems, 44 (2007) 188-201.

[40] J. Zaparniuk, J.C. Yuille, S. Taylor, Assessing the credibility of true and false statements, International Journal of Law and Psychiatry, 18 (1995) 343–352.

[41] H. Markus, Self-schemata and processing information about the self, Journal of Personality and Social Psychology, 35 (1977) 63–78.

[42] D.B. Buller, J.K. Burgoon, Emotional Expression in the Deception Process, in: P.A. Andersen, L.K. Guerrero (Eds.) Handbook of communication and emotion : research, theory, applications, and contexts, Academic Press, San Diego, 1998, pp. 590.

[43] M.L. Newman, J.W. Pennebaker, D.S. Berry, J.M. Richards, Lying words: Predicting deception from linguistic styles, Journal of Personality and Social Psychology Bulletin, 29 (2003) 665-675.

[44] A. Vrij, Detecting lies and deceit: the psychology of lying and the implications for professional practice, John Wiley, New York, 2000.

[45] L. Zhou, D. Zhang, A Comparison of Deception Behavior in Dyadic and Triadic Group Decision Making in Synchronous Computer-mediated Communication, Small Group Research, 37 (2006) 140-164.

[46] A. Voida, W.C. Newstetter, E.D. Mynatt, When conventions collide: The tensions of instant messaging attributed, in: Conference on Human Factors in Computing Systems (CHI), ACM Press, Minneapolis, MN, 2002, pp. 187-194.

[47] G.F. MaHl, Explorations in nonverbal and vocal behavior, Erlbaum, Hillsdale, NJ, USA, 1987.

[48] S. Schachter, N. Christenfeld, B. Ravina, F. Bilous, Speech Disfluency and the Structure of Knowledge, Journal of Personality and Social Psychology, 60 (1991) 362-367.

[49] P. Ekman, W.V. Friesen, Nonverbal leakage and clues to deception, Psychiatry, 32 (1969) 88- 106.

[50] D.T. Gilbert, D.S. Krull, Seeing less and knowing more: The benefits of perceptual ignorance, Journal of Personality and Social Psychology, 54 (1988) 193–202.

[51] K.M. Richards, J.J. Gross, Composure at any cost? The cognitive consequences of emotion suppression, Personality and Social Psychology Bulletin, 25 (1999) 1033–1044.

[52] B.M. DePaulo, J.T. Stone, G.D. Lassiter, Deceiving and detecting deceit, in: B.R. Schlenker (Ed.) The Self and Social Life, McGraw-Hill, New York, 1985, pp. 323-370.

[53] P. Ekman, Telling lies: clues to deceit in the marketplace, politics, and marriage, W.W. Norton, New York, 2001.

[54] N. Baron, Who sets e-mail style? Prescriptivism, coping strategies, and democratizing communication access, The Information Society, 18 (2002) 403-412.

[55] J.R. Carlson, R.W. Zmud, Channel expansion theory and the experiential nature of media richness perceptions, Academy of Management Journal, 42 (1999) 153-170.

[56] PDTB-Group, The penn discourse treebank 2.0 annotation manual, in, Insitute for Research in Cognitive Science, University of Pennsylvania, 2008.

[57] Y. Zhou, N. Xue, PDTB-style discourse annotation of Chinese text, in: The 50th Annual Meeting of the Association for Computational Linguistics, Association for Computational Linguistics, Jeju, Republic of Korea, 2012, pp. 69-77.

[58] S. Tonelli, G. Riccardi, R. Prasad, A. Joshi, Annotation of discourse relations for conversational spoken dialogues, in: The Seventh International Conference on Language Resources and Evaluation (LREC), Malta, 2010.

[59] A. Stolcke, K. Ries, N. Coaacro, E. Shriberg, R. Bates, D. Jurafsky, P. Taylor, R. Martin, C.V. Ess-Dykema, M. Meteer, Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech, Computational Linguistics, 26 (2000).

[60] J.L. Austin, How to Do Things With Words, Oxford University Press, Oxford, England, 1962.

[61] W.A. Donohue, A.J. Roberto, An empirical examination of three models of integrative and distributive bargaining, International Journal of Conflict Management, 7 (1996) 209 - 229.

[62] M. Zuckerman, B.M. DePaulo, R. Rosenthal, Verbal and nonverbal communication of deception, in: L. Berkowitz (Ed.) Advances in experimental social psychology, Academic Press, New York, 1981, pp. 1-59.

[63] A. Vrij, W. Kneller, S. Mann, The effect of informing liars about Criteria-Based Content Analysis on their ability to deceive CBCA-raters, Legal and Criminological Psychology, 5 (2000) 57-70.

[64] I. BlandóN-Gitlin, K. Pezdek, D.S. Lindsay, L. Hagen, Criteria-based content analysis of true and suggested accounts of events, Applied Cognitive Psychology, 23 (2009) 901–917.

[65] W. R.P., Basic Content Analysis, Sage Publications, Newburry Park, CA, 1990.

[66] H.K. Klein, D.P. Truex III, Discourse Analysis: A Semiotic Approach to the Investigation of Organizational Emergence, in: P.B. Andersen, B. Holmqvist (Eds.) The Semiotics of the Workplace, Walter De Gruyter, Berlin, 1995.

[67] K. Krippendorff, Content Analysis: An Introduction to Its Methodology, Sage, Thousand Oaks, CA, 2004.

[68] S. Elo, H. Kyngӓs, The qualitative content analysis process, Journal of Advanced Nursing, 62 (2008) 107-115.

[69] P. D.F., B. C.T., Nursing Research. Principles and Methods, Lippincott Williams & Wilkins, Philadelphia, PA, 2004.

[70] I. Dey, Qualitative Data Analysis: A User-Friendly Guide for Social Scientists, Routledge, London, 1993.

[71] M.D. Moran, Arguments for rejecting the sequential Bonferroni in ecological studies, Oikos, 100 (2003) 403-405.

[72] F. Clemens, P.A. Granhag, L.A. Strömwall, A. Vrij, S. Landström, E.R.a. Hjelmsäter, M. Hartwig, Skulking around the dinosaur: Eliciting cues to children's deception via strategic disclosure of evidence, Applied Cognitive Psychology, 24 (2010) 925-940.

[73] J.K. Burgoon, N.E. Dunbar, An interactionist perspective on dominance-submission: Interpersonal dominance as a dynamic, situationally contingent social skill, Communication Monographs, 67 (2000) 96-121.

[74] E.S. Adams, M. Mesterton-Gibbons, The costs of threat displays and the stability of deceptive communication, Journal of Theoretical Biology, 175 (1995) 405-421.

[75] Y. Bar-Haim, D. Lamy, L. Pergamin, M.J. Bakermans-Kranenburg, M.H.V. IJzendoorn, Threatrelated attentional bias in anxious and nonanxious individuals: a meta-analytic study, Psychological Bulletin, 133 (2007) 1-24.

[76] J. Siegel, V. Dubrovsky, S. Kiesler, T.W. McGuire, Group processes in computer-mediated communication, Organizational Behavior and Human Decision Process, 37 (1986) 157-187.

[77] J. Burgoon, D. Buller, L. Dillman, J. Walther, Interpersonal deception: IV. Effects of suspicion on perceived communication and nonverbal behavior dynamics, Human Communication Research, 22 (1995) 163-196.

[78] J.K. Burgoon, D.B. Buller, C.H. White, W. Afifi, A.L.S. Buslig, The role of conversational involvement in deceptive interpersonal interactions, Personality & Social Psychology Bulletin, 25 (1999) 669-685.

[79] M.E. Schweitzer, R. Croson, Curtailing deception: The impact of direct questions on lies and omissions, International Journal of Conflict Management, 10 (1999) 225-248.

[80] M.J. Cody, H.D. O'Hair, Nonverbal communication and deception: Differences in deception cues due to gender and communicator dominance, Communication Monographs, 50 (1983) 175- 192.

[81] C.F. Keating, K.R. Heltman, Dominance and deception in children and adults: Are leaders the best misleaders?, Personality and Social Psychology Bulletin, 20 (1994) 312-321.

[82] M. Zuckerman, M.D. Amidon, S.E. Bishop, S.D. Pomerantz, Face and tone of voice in the communication of deception, Journal of Personality and Social Psychology, 32 (1982) 347-357.

[83] C.C. Lewis, J.F. George, Cross-cultural deception in social networking sites and face-to-face communication, Computers in Human Behavior, 24 (2008) 2945-2964.

[84] J. Cohen, Statistical Power Analysis for the Behavioral Sciences, Lawrence Erlbaum Associates, Hillsdale, New Jersey, 1988.

[85] R. Rosenthal, Combining results of independent studies, Psychological Bulletin, 85 (1978) 185-193.

[86] P. Kroeger, Analyzing Grammar: An Introduction, Cambridge University Press, Cambridge, UK, 2005.

Table 1.A taxonomy of text-based cues to deception and examples

<table><tr><td>Linguistic levels</td><td>Descriptions [14, 19, 86]</td><td>Sample cues</td></tr><tr><td>Word</td><td>The smallest meaningful unit of speech that can stand by themselves</td><td>we, not, because</td></tr><tr><td>Phrase</td><td>A group of words that function as a single unit in the syntax of a sentence</td><td>You and I (noun phrase), accuse him (verb phrases)</td></tr><tr><td>Clause</td><td>The smallest grammatical unit that can express a complete proposition.</td><td>If you trust me... ...because he always distract us.</td></tr><tr><td>Sentence</td><td>A grammatical unit that consists of one or more clauses and a full stop (including both written language and silence in speech).</td><td>I agree with him.</td></tr><tr><td>Discourse</td><td>Sequence of sentences that have internal relations to themselves as well as external to other sentences.</td><td>A: If you trust me,A: I am going to help you to win.A: Vote for Mike?B: Yes, let&#x27;s do it.A: Very good.</td></tr></table>

a:

Table 2. A list of selected discourse features

<table><tr><td>Discourse type</td><td>Sourcea</td><td>Featureb</td><td>Description</td><td>Grouping notes</td></tr><tr><td rowspan="9">Linguistic</td><td rowspan="2">PDTB LUNA</td><td>Contingency (Cause)</td><td>causal relationship between adjacent sentences</td><td></td></tr><tr><td>Contingency (Condition)</td><td>conditional relationship between adjacent sentences</td><td></td></tr><tr><td>PDTB LUNA DA</td><td>RestatementDT</td><td>stating the preceding messages again in the same or a different way</td><td>Hold before answer/agreement(DA)Repeat-phrase(DA)</td></tr><tr><td rowspan="6">DA</td><td>Self-disclosureDT</td><td>describing his/her role, identity, belief, personal experience, perception, events in a personal and revealing way</td><td>statement (DA)opinion(DA)guilty delight (DT)</td></tr><tr><td>Question</td><td>all types of questions seeking to get information in reply, such as Wh-, Yes/No, tag, and backchannel questions</td><td>various types of questions (DA)</td></tr><tr><td>Non-verbal</td><td>intruding incoherent, non-lexical vocables or expressions that occur within the flow of otherwise natural text; special expressions of non-verbal behavior such as emotion and emphasis</td><td></td></tr><tr><td>Agreement/Accepting</td><td>agreeing and accepting; compliment; acknowledgement</td><td></td></tr><tr><td>RejectBG</td><td>disagreeing and denigrating; denial of compliance; downplaying</td><td>Reject Other&#x27;s Demand (BG)</td></tr><tr><td>Action-directiveBG</td><td>calling the receiver to take a particular action, yet do not require the sender to reciprocate any action of his own</td><td>Statement of Demand (BG)</td></tr><tr><td rowspan="2">Task</td><td rowspan="2">BG</td><td>Threat to Take Action</td><td>an expression of intention to take action that inflicts damage on or hurts chance of the receiver</td><td></td></tr><tr><td>Supportiveness DT</td><td>seems cooperative, helpful, and secure.</td><td>Integrate(BG)</td></tr><tr><td rowspan="3">Domain</td><td rowspan="3">DT</td><td>Topic change</td><td>The sender changes the content of a message to something irrelevant to the task at hand</td><td></td></tr><tr><td>Agitation</td><td>expressing a mental state of extreme emotional disturbance, or worry; affective reactions to a situation</td><td></td></tr><tr><td>DisfluencyOMG</td><td>the sender interrupts the flow of a message or continues it in a subsequent message; incomplete message</td><td>Interrupted/Continuer (OMG)</td></tr><tr><td>Application</td><td>OMG</td><td>Accusation</td><td>an assertion that someone is guilty of or innocent of a fault/offence</td><td></td></tr></table>

DA: Dialogue act modeling for automatic tagging and recognition of conversational speech  
PDTB:The Penn Discourse TreeBank 2.0  
LUNA:Annotation of Discourse Relations for Conversational Spoken Dialogs  
BG: An empirical examination of three models of integrative and distributive bargaining  
DT: Deception theories; OMG: Online mafia game

Duplicated features from different types of discourse are listed only once in the first appearing discourse type, and overlapping discourse types are displayed as superscripts.

Table 3. Discourse Behavior and Manifesting Discourse Features

<table><tr><td>Deception Behavior (deceiver seems...)</td><td>Discourse Features</td></tr><tr><td>less forthcoming</td><td>a) self-disclosure (reverse)</td></tr><tr><td>less dominant</td><td>a) accusation (reverse)b) action-directive (reverse)c) threat to take action</td></tr><tr><td>more cooperative</td><td>a) agreement/acceptingb) supportivenessc) reject (reverse)</td></tr><tr><td>less logical</td><td>a) contingency cause (reverse)b) contingency condition (reverse)c) restatement (reverse)d) question (reverse)</td></tr><tr><td>less pleasant</td><td>a) agitation</td></tr><tr><td>more disturbed</td><td>a) disfluencyb) non-verbalc) topic change</td></tr></table>

Table 4. Descriptive statistics of discourse features

<table><tr><td>Discourse Feature</td><td>Condition</td><td>Mean</td><td>Std. dev.</td></tr><tr><td rowspan="2">Self-disclosure</td><td>D</td><td>.201</td><td>.130</td></tr><tr><td>T</td><td>.232</td><td>.128</td></tr><tr><td rowspan="2">Accusation</td><td>D</td><td>.147</td><td>.130</td></tr><tr><td>T</td><td>.216</td><td>.148</td></tr><tr><td rowspan="2">Action-directive</td><td>D</td><td>.115</td><td>.099</td></tr><tr><td>T</td><td>.137</td><td>.099</td></tr><tr><td rowspan="2">Threat to Take Action</td><td>D</td><td>.009</td><td>.029</td></tr><tr><td>T</td><td>.008</td><td>.022</td></tr><tr><td rowspan="2">Agreement/Accepting</td><td>D</td><td>.029</td><td>.051</td></tr><tr><td>T</td><td>.024</td><td>.044</td></tr><tr><td rowspan="2">Supportiveness</td><td>D</td><td>.019</td><td>.043</td></tr><tr><td>T</td><td>.013</td><td>.031</td></tr><tr><td rowspan="2">Reject</td><td>D</td><td>.066</td><td>.074</td></tr><tr><td>T</td><td>.053</td><td>.068</td></tr><tr><td rowspan="2">Contingency(Cause)</td><td>D</td><td>.041</td><td>.060</td></tr><tr><td>T</td><td>.037</td><td>.051</td></tr><tr><td rowspan="2">Contingency(Condition)</td><td>D</td><td>.022</td><td>.042</td></tr><tr><td>T</td><td>.025</td><td>.043</td></tr><tr><td rowspan="2">Restatement</td><td>D</td><td>.032</td><td>.056</td></tr><tr><td>T</td><td>.038</td><td>.057</td></tr><tr><td rowspan="2">Question</td><td>D</td><td>.172</td><td>.128</td></tr><tr><td>T</td><td>.151</td><td>.125</td></tr><tr><td rowspan="2">Agitation</td><td>D</td><td>.032</td><td>.055</td></tr><tr><td>T</td><td>.025</td><td>.044</td></tr><tr><td rowspan="2">Disfluency</td><td>D</td><td>.035</td><td>.055</td></tr><tr><td>T</td><td>.025</td><td>.043</td></tr><tr><td rowspan="2">Non-verbal</td><td>D</td><td>.161</td><td>.149</td></tr><tr><td>T</td><td>.117</td><td>.122</td></tr><tr><td rowspan="2">Topic change</td><td>D</td><td>.016</td><td>.041</td></tr><tr><td>T</td><td>.007</td><td>.030</td></tr></table>

Table 5. Results of One-way Repeated Measures ANOVA (two-tailed)

<table><tr><td>Feature</td><td>Mean Difference</td><td>Std. Error</td><td>Partial η2</td><td>Observed power</td><td>p-value</td><td>Supported?</td></tr><tr><td>Self-disclosure</td><td>-.0314</td><td>.0122</td><td>.032</td><td>.724</td><td>.011*</td><td>Y</td></tr><tr><td>Accusation</td><td>-.0690</td><td>.0141</td><td>.108</td><td>.998</td><td>.000***</td><td>Y</td></tr><tr><td>Action-directive</td><td>-.0217</td><td>.0102</td><td>.022</td><td>.564</td><td>.034*</td><td>Y</td></tr><tr><td>Threat to take action</td><td>.0011</td><td>.0026</td><td>.001</td><td>.071</td><td>.670</td><td>N</td></tr><tr><td>Agreement/Accepting</td><td>.0049</td><td>.0044</td><td>.006</td><td>.201</td><td>.263</td><td>N</td></tr><tr><td>Supportiveness</td><td>.0056</td><td>.0036</td><td>.012</td><td>.339</td><td>.123</td><td>N</td></tr><tr><td>Reject</td><td>.0128</td><td>.0069</td><td>.017</td><td>.455</td><td>.065&#x27;</td><td>N</td></tr><tr><td>Contingency(Cause)</td><td>.0037</td><td>.0057</td><td>.002</td><td>.099</td><td>.519</td><td>N</td></tr><tr><td>Contingency(Condition)</td><td>-.0029</td><td>.0043</td><td>.002</td><td>.105</td><td>.492</td><td>N</td></tr><tr><td>Restatement</td><td>-.0069</td><td>.0052</td><td>.009</td><td>.260</td><td>.188</td><td>N</td></tr><tr><td>Question</td><td>.0204</td><td>.0130</td><td>.012</td><td>.346</td><td>.118</td><td>N</td></tr><tr><td>Agitation</td><td>.0065</td><td>.0048</td><td>.009</td><td>.268</td><td>.180</td><td>N</td></tr><tr><td>Disfluency</td><td>.0097</td><td>.0050</td><td>.019</td><td>.487</td><td>.054&#x27;</td><td>N</td></tr><tr><td>Non-verbal</td><td>.0437</td><td>.0132</td><td>.052</td><td>.909</td><td>.001**</td><td>Y</td></tr><tr><td>Topic change</td><td>.0090</td><td>.0031</td><td>.042</td><td>.835</td><td>.004**</td><td>Y</td></tr></table>

\*\*\*: significant at .001, \*\*: significant at .01; \*: significant at .05; ': significant at .1.

![](/api/attachments/NXUKYYFV/fulltext/images/c14fb802c33c2ebe004ccd2c129bdf5725935bfd1c33b6fd3871777bd9b4bad4.jpg)  
Figure 1. A discourse framework

Player A: 看这家伙目光游移，肯定心怀鬼胎，就选他了[X is accused as the mafia]

Player C: 看这家伙目光游移，肯定心怀鬼胎，就选他了[X is accused as the mafia]

Player A: Player C 是杀手[Player C is the mafia]

Player B: 我们自己人拿到警察了 [The police is on my side]

Player C: 看这家伙目光游移，肯定心怀鬼胎，就选他了 [X is accused as the mafia]

Player A: Player C 采取主动了[Player C is making a move]

Player C: Player B 查杀[Based on my inspection,Player B is the mafia]

Player B: 看这家伙目光游移，肯定心怀鬼胎，就选他了 [X is accused as the mafia]

Player C: 我主动的查杀了 Player B [I just inspected that Player B is the mafia]

Player B: …………你又来 [……Again?]

Player D: 看这家伙目光游移，肯定心怀鬼胎，就选他了 [X is accused as the mafia]

Player C: 时间不够 [We are running out of time]

Player A: 我相信 [I agree]

Player A: 跟 [I follow]

Player A: 等 [Wait]

Notes: Player A: mafia; Player B: Police; Player C-D: Villagers; X: the identifier of one of the players.
