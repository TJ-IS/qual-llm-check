---
otero_id: 28188
otero_key: "QJCFR6B8"
title: "Estimating the Impact of “Humanizing” Customer Service Chatbots"
authors: "Scott Schanke; Gordon Burtch; Gautam Ray"
year: "2021"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.1015"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Estimating the Impact of “Humanizing” Customer Service Chatbots

Scott Schanke,<sup>a</sup> Gordon Burtch,<sup>b</sup> Gautam Ray<sup>c</sup>

<sup>a</sup> Lubar School of Business, University of Wisconsin-Milwaukee, Milwaukee, Wisconsin 53202; <sup>b</sup>Questrom School of Business, Boston University, Boston, Massachusetts 02215; <sup>c</sup>Carlson School of Management, University of Minnesota, Minneapolis, Minnesota 55455 Contact: schanke@uwm.edu, https://orcid.org/0000-0001-8255-7651 (SS); gburtch@bu.edu, https://orcid.org/0000-0001-9798-1113 (GB); gautamr@umn.edu (GR)

Received: January 15, 2019 Revised: November 23, 2019; June 13, 2020 Accepted: December 3, 2020 Published Online in Articles in Advance: May 24, 202

https://doi.org/10.1287/isre.2021.1015

Copyright: © 2021 INFORMS

Abstract: We study the impacts of “humanizing” arti<sup>fi</sup>cial intelligence (AI)-enabled autonomous customer service agents (chatbots). Implementing a <sup>fi</sup>eld experiment in collaboration with a dual channel clothing retailer based in the United States, we automate a used clothing buy-back process, such that individuals engage with the retailer’s autonomous chatbot to describe the used clothes they wish to sell, obtain a cash offer, and (if they accept the offer) print a shipping label to <sup>fi</sup>nalize the transaction. We causally estimate the impact of chatbot anthropomorphism on transaction conversion by randomly exposing consumers to exogenously varied levels of chatbot anthropomorphism, operationalized by incorporating a random draw from a set of three anthropomorphic features: humor, communication delays, and social presence. We provide evidence that, in this retail setting, anthropomorphism is bene<sup>fi</sup>cial for transaction outcomes, but that it also leads to signi<sup>fi</sup>cant increases in offer sensitivity. We argue that the latter effect occurs because, as a chatbot becomes more human-like, consumers shift to a fairness evaluation or negotiating mindset. We also provide descriptive evidence suggesting that the bene<sup>fi</sup>ts of anthropomorphism for transaction conversion may derive, at least in part, from consumers’ increased willingness to disclose personal information necessary to complete the transaction.

History: This paper has been accepted for the Information Systems Research Special Section on Humans, Algorithms, and Augmented Intelligence: The Future of Work, Organizations and Society.

Funding: The authors acknowledge funding of this work by the Marketing Science Institute for Research Priorities [Grant 4000793].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.1015.

Keywords: chatbot arti<sup>fi</sup>cial intelligence intelligence augmentation human-computer interaction <sup>fi</sup>eld experiment customer service anthropomorphism

## 1. Introduction

Researchers, the general public, and organizations alike have become enamored with arti<sup>fi</sup>cial intelligence (AI). With recent breakthroughs in the <sup>fi</sup>eld, coupled with changes in public perception and advances in hardware, society has seen AI technologies move to the main stage. Organizations are looking to capitalize by putting these technologies into practice to both capture value and to hedge against the possibility of disruption (McKendrick 2018). AI technologies have seen widespread implementation in a variety of domains, from fraud detection to image recognition, voice recognition, and natural language processing (Dale 2016). Gartner predicts that 2.3 million AI-related jobs will be created by the year 2020.<sup>1</sup>

Although media and public interest have caused AI to reach what Gartner refers to as a state of “in<sup>fl</sup>ated expectations,” there is clear value in these technologies, if they are used appropriately and expectations are managed. One prominent example of an AI-based tool that has seen widespread adoption and value creation for <sup>fi</sup>rms of all sizes is the text-based chatbot. Chatbots are autonomous software agents that support textbased exchanges with human users, drawing on tools and techniques from the domain of natural language processing. Chatbots have the potential to automate basic, repeatable, standardized customer service interactions, relieving the need for those interactions to be handled by human employees (Fernandes 2017). Recognizing the potential of these sorts of AI-based autonomous agents, <sup>fi</sup>rms are adopting them at an extremely rapid pace. Google Search Trends indicates that interest in chatbots has grown by an order of magnitude in the last two years (see Figure 1), and industry estimates forecast that, by 2020, conversations with autonomous agents will be more common for the average individual than conversations with a spouse.<sup>2</sup>

The anticipated volume of customer interactions these digital agents will be expected to handle suggests that chatbots will soon become the main point of customer contact for many retail organizations. Organizations therefore need to be careful in their design and deployment of these technology artifacts, to ensure that the experience that customers have is both effective and enjoyable. Although many features warrant attention, one particularly important aspect to consider is the extent to which autonomous agents (and speci<sup>fi</sup>cally chatbots) are designed with social interaction, and speci<sup>fi</sup>cally anthropomorphism, in mind (Wilson et al. 2017).

Though anthropomorphism touches several academic disciplines, it can best be described as the attribution of human-like qualities to nonhuman entities such as machines, animals, and other objects (Duffy 2003). This phenomenon is a common occurrence when individuals interact with technology that possesses certain elements associated with human-to-human interaction, such as eye gaze (Kiesler et al. 1984), facial expressions (Kiesler et al. 2008), and conversational turn taking (Cassell and Bickmore 2000). How individuals humanize technology has been an important topic of inquiry in both human-computer interaction (HCI) and human-robot interaction (HRI) literature for decades. In some cases, making technology more human-like has proven to be bene<sup>fi</sup>cial, increasing user trust and satisfaction with the interface. However, in other cases, adding human-like social cues has led to negative consequences, such as social anxiety (Sproull et al. 1996) and reduced cooperation (Kiesler et al. 1996). As we articulate in our review of prior literature in later sections, a common feature of much of the prior work in this space is the inconsistency of the relationship between anthropomorphism and desirable user outcomes. This inconsistency speaks to the myriad contextual factors that can shape the relationship. With that in mind, in this work, we seek to understand the impact of integrating anthropomorphic features into AI-enabled autonomous customer service agents, that is, chatbots, particularly within a retail environment. Speci<sup>fi</sup>cally, we seek to empirically evaluate the effects of anthropomorphism on transaction conversion. Further, we explore the impact of anthropomorphism on consumer offer sensitivity, informed by prior work in the HCI literature that has drawn a connection from consumer perceptions of anthropomorphism to customer perceptions of fairness and trust. Formally, we evaluate the following two research questions:

<sub>•</sub> RQ1. How and to what degree does customer transaction probability depend on the anthropomorphism of AI-enabled automated customer service agents (chatbots)?

RQ2. To what degree does customer offer sensitivity vary with the anthropomorphism of AI-enabled automated customer service agents (chatbots)?

We examine these questions via a <sup>fi</sup>eld experiment, conducted in partnership with a dual channel clothing retailer based in the United States. Our retail partner has historically operated a used clothing buy-back program through a web-based form, and employee conversations with customers over email and Facebook Messenger. In the prior process, a customer would describe the clothes, obtain an offer estimate from an employee, provide mailing address info, and print a shipping label, before sending the clothes to the retailer for <sup>fi</sup>nal evaluation and payment. We insert ourselves into this process, automating the customer interactions with a Facebook Messenger chatbot, which is integrated with the retailer’s Facebook business page. In implementing the chatbot, we integrate a framework that enables us to randomly assign customers into various treatment conditions, such that customers ultimately converse with a chatbot that bears a randomly assigned set of anthropomorphic features. This randomized design allows us to experimentally evaluate the causal relationship between the degree of a chatbot’s anthropomorphism and the customer’s probability of completing the buy-back process. Moreover, we simultaneously introduce random variation into the cash offer each customer receives, which further enables us to assess the moderating effect of chatbot anthropomorphism on customers’ offer sensitivity.

Figure 1. (Color online) Google Trends Global Interest in the Term “Chatbot”  
![](/api/attachments/QJCFR6B8/fulltext/images/ab54581dc1f87806e5650dad34dcfcefc1d7545c62264e5bfed7c95acb1ad7ad.jpg)

We arrive at two notable <sup>fi</sup>ndings. First, we <sup>fi</sup>nd that incorporating anthropomorphism into autonomous customer service chatbots increases conversion rates. Second, we show that, in the presence of a suf<sup>fi</sup>- ciently large degree of anthropomorphism (three treatments), customers become more offer sensitive. This latter <sup>fi</sup>nding indicates that, as a chatbot becomes more human-like, consumers begin to scrutinize offers. This might occur because offers made by humans are more likely to be perceived as potentially opportunistic (price gouging) or inconsistent (noisy) by consumers, compared with computer-generated offers.

Our study contributes to a number of different streams of literature. First, we contribute to the literature in information systems by exploring the design and ef<sup>fi</sup>cacy of an increasingly prevalent form of information system, the customer service chatbot. In so doing, we build on an extensive literature in HCI related to anthropomorphism by evaluating these features in a <sup>fi</sup>eld setting. Second, we contribute to the marketing literature by considering a variety of practical and theoretical issues in the AI-enabled automation of customer service job roles. Building on the work of Wirtz et al. (2018), we empirically evaluate anthropomorphism, a critical design attribute of service robots, demonstrating its value in customer service settings. Third, our work contributes to the burgeoning literature on individual’s reactions to algorithmic forecasts and estimates (Dietvorst et al. 2015, 2018; Kleinberg et al. 2018; Tambe et al. 2019), and highlight how anthropomorphism could play a role. Finally, and more broadly, our work contributes to the literature on intelligence augmentation, or IA (Jain et al. 2018). In particular, our study demonstrates the potential to augment arti<sup>fi</sup>cially intelligent agents with human-like social intelligence (Wang et al. 2007b). Whereas the literature on IA to date has primarily focused on the possible applications of technology to augment human decision-making abilities, our work highlights opportunities for the reverse; that incorporating human-like behavior and decision making into autonomous agents can amplify their performance and ef<sup>fi</sup>cacy as well.

## 2. Literature Review

## 2.1. Anthropomorphism and AI

Scholars of computer science and engineering have dedicated a great deal of attention to the ef<sup>fi</sup>cient performance of AI-based systems, with an eye toward operational performance. However, when it comes to the automation of job roles or processes that involve human touch points, social factors are likely to play a particularly prominent role as well. Fortunately, designing autonomous agents to account for social factors has been a focal subject in the human-computer interaction literature for many decades.

A central component in research on the effective design of autonomous agents has been the role of anthropomorphism. Anthropomorphism is a concept that touches several <sup>fi</sup>elds of study: psychology (Heider and Simmel 1944, Barrett and Keil 1996, Malle and Pearce 2001), marketing (Aaker 1997), computer science (Duffy 2003, Kiesler et al. 2008), and religion (Guthrie 1995). Although de<sup>fi</sup>nitions within these <sup>fi</sup>elds vary slightly, anthropomorphism, at broad scope, is the attribution of human-like qualities to nonhuman entities such machines, animals, and other objects (Duffy 2003). This attribution is generally the product of humans seeking to explain the actions and behaviors of nonhuman objects and beings in a way that they understand (Duffy 2003). Although assigning human-like qualities is a common occurrence that pervades several disciplines, this phenomenon is viewed by several scienti<sup>fi</sup>c disciplines, such as biology and psychology, as a nuisance that confounds causal mechanisms and hampers scienti<sup>fi</sup>c inquiry (Kennedy 1992).

Whereas some disciplines view anthropomorphism as a hindrance, others, such as HCI, view anthropomorphism as an inevitability that should be accounted for and acknowledged when designing the interface (Caporael 1986). A popular paradigm used in HCI is known as “computers are social actors,” or CASA, which suggests that people, when presented with technology that contains features such as dialogue and turn taking, identify those pieces of technology as a social actor (Nass et al. 1994, Moon 2000, Nass and Lee 2001). It is this conceptualization of digital agents as social actors that interface designers can apply theories from social sciences, which govern human-tohuman interaction such as politeness (Nass et al. 1994) and reciprocity (Moon 2000), and effectively carry these over to human-machine interactions (Nass et al. 1994). As such, designers can strategically utilize social cues such as small talk, greetings, and transitions to in<sup>fl</sup>uence user trust with the interface and elicit speci<sup>fi</sup>c behaviors such as self-disclosure (Cassell and Bickmore 2000) and persuasion (Xu and Lombard 2017).

Although anthropomorphic social cues can help designers create a more effective user interface, these features can also lead to unintended negative consequences. More speci<sup>fi</sup>cally, Ben Shneiderman, a critic of the use of anthropomorphic social cues in the technology interface (Don et al. 1992), contends that designers do not fundamentally understand the way users will perceive and interpret social cues. This lack of understanding can lead to unintended outcomes, namely undesirable perceptions of anthropomorphism (Duffy 2003). As a result, incorporating even minor social cues in an ad hoc (and ill considered) manner may lead to user disappointment when the human-like agent falls short of user expectations (Nass and Moon 2000, Duffy 2003). A delicate balance thus needs to be struck when it comes to the incorporation of social cues in chatbots. Accordingly, it should come as no surprise that so many chatbots on Facebook’s Messenger platform today are incapable of ful<sup>fi</sup>lling the basic requirements of users (Sun 2107).

We seek to evaluate the effects of introducing anthropomorphism in chatbots via the three commonly used social cues: social presence, communicative delay, and humor. We will explore how user (customer) exposure to greater levels of anthropomorphism in a chatbot, that is, greater numbers of features, in<sup>fl</sup>uence transaction outcomes in a live customer service interaction, as well as any associated shifts in customer offer sensitivity. We discuss the three anthropomorphic features next, referencing relevant literature for each.

2.1.1. Social Presence. A commonly discussed element in papers related to conversational agents is social presence (Verhagen et al. 2014, Sah and Peng 2015, Araujo 2018). In this technological context, adding social presence means adding sensitive human contact (Verhagen et al. 2014). In interacting with a chatbot, users have opportunities to make social presence attributions at the beginning (Holtgraves et al. 2007, Araujo 2018), middle (Holtgraves et al. 2007, Sah and Peng 2015), and end (Araujo 2018) of the conversation.

This social presence can prove to be a double-edged sword for practitioners. The more socially present the interactions are, the more engaging the interface; however, the more human-like the interface, the higher expectations that the user has of the machine’s communicative prowess (Nowak and Biocca 2003, Mone 2016). With this, designers of chatbots make a very important decision of how their conversational agent is perceived in the beginning of the interaction with a greeting (Gefen and Straub 2003, Araujo 2018). For example, a designer can either greet the user by introducing itself with a real human name, or level expectations of communicative capability by using a generic machine-like name. By setting the tone with a human name, the designer could elicit an anthropomorphic response to the chatbot leading to a more engaging customer experience. Alternatively, in giving the chatbot a human name, the designer could enforce unattainable human expectations on the chatbot, which could lead to frustration later in the experience.

In addition to the greeting, designers can in<sup>fl</sup>uence anthropomorphic perceptions through the language choices they make in the conversation. For example, using more polite (Fussell et al. 2008), informal (Holtgraves et al. 2007, Araujo 2018), or social (Verhagen et al. 2014) language can help induce anthropomorphic perceptions and also perceptions of social presence. Slight differences in agent language have shown to greatly impact a chatbot’s perceived personality (Holtgraves et al. 2007). It is with these linguistic features that designers help to enforce a feeling of social presence and further promote anthropomorphism in their chatbot.

Another method HCI designers use to achieve anthropomorphic attributions toward their machines is through physical social cues (Goetz et al. 2003, Fussell et al. 2008). Unlike embodied conversational agents, chatbots rely solely on text-based computer-mediated communication to communicate and cannot show physical nonverbal cues such as facial expressions or gaze (Kiesler et al. 1984). In computer-mediated communication, when these typical face-to-face social cues are not present, communicators shift focus to alternative cues available and make social interpretations (Walther 1992, Walther and Tidwell 1995). This theory is known as social information processing (SIP). Typically, this manifests itself in chronemic cues such as timestamps (Walther and Tidwell 1995, Liebman and Gergle 2016). Due to the disembodied nature of chatbots that exist on messaging platforms such as Facebook Messenger, Kik, or Telegram, designers only have a couple of chronemic social cues at their disposal to enforce feelings of a real socially present human. These include read receipts and ellipses during typing messages. Although, these two features are commonplace when two humans are talking via Facebook Messenger, these cues are not required from a chatbot as it neither types nor reads.

Although, these anthropomorphic perceptions could lead to higher amounts of sociability between the chatbot and the customer, these deviations from a more task-oriented style could lead to more dif<sup>fi</sup>culty and time for users to complete a self-service task. Additionally, it could also over promise the communicative prowess of the agent on the other end of the conversation. This could be counterproductive as users of self-service technologies do so because they are convenient, quick, and a means to circumvent interacting with service individuals (Meuter et al. 2000). As such, there is a potential that these communicative features could lead to one of two outcomes. The <sup>fi</sup>rst is that the more anthropomorphic the chatbot becomes, the more a customer is willing to engage with the artifact. This prolonged interaction would eventually lead to a resolution of the issue and save labor costs for the company. Alternatively, these anthropomorphic additions to the chatbot obfuscate the taskoriented nature of the typical self-service interaction, and could lead to frustration and dissatisfaction as the features add overhead to the experience and also mislead the user about the chatbot’s communicative prowess.

2.1.2. Communication Delays. In addition to language communication features, another social cue employed by both researchers and practitioners is delay (Holtgraves and Han 2007, Crozier 2017, Gnewuch et al. 2018). From one perspective, delays could be interpreted as the chatbot not working as expected. However, when implemented correctly, slight delays that are dynamic to the amount of text can dictate levels of persuasion (Moon 1999) and chatbot personality perceptions (Holtgraves and Han 2007). At face value, this anthropomorphic effect of delays seems somewhat intuitive as humans do not read and respond to messages sent through text-based mediums instantaneously.

Although these slight delays may lead to more anthropomorphic perceptions of the chatbot, they may also interrupt the service quality associated with the experience (Taylor 1994, Meuter et al. 2000). Thus delays in sending messages could lead to two different outcomes in a customer service interaction. If the anthropomorphic features of the interface lead to higher levels of trust in the interface, then potentially these slight delays would enhance the user experience and lead to higher levels of satisfaction with the experience. In contrast, delays can be viewed as an element that impedes the service encounter and prevents the customer from accomplishing the self-service task.

2.1.3. Humor. In the <sup>fi</sup>elds of sociolinguistics and pragmatics, humor has been shown to introduce feelings of common ground between two communicating social actors (Brown and Levinson 1987, Holtgraves 2013). Similar to human-to-human interactions, humor can be an effective way to personify systems, and create a more engaging interaction (Morkes et al. 1999, Niculescu et al. 2013). Additionally, humor in task-oriented communications has been shown to increase individuals satisfaction with the task (Morkes et al. 1999).

Although humor may be bene<sup>fi</sup>cial, it does appear that there is some nuance required in implementing humor. For instance, in the medical <sup>fi</sup>eld, humor helps improve reassurance for patients, but only in the correct context (Francis et al. 1999). This also has been shown in human and robot interaction, where robots with a more playful personality gain more compliance from humans in a nonserious task, and more serious robots perform better in serious tasks (Goetz et al. 2003). Similarly, humor in both business and customer service interactions requires a more nuanced approach (Malone 1980, Dolen et al. 2008). More speci<sup>fi</sup>- cally, Dolen et al. (2008) <sup>fi</sup>nd that whereas humor in an electronic service encounter can help in some situations in which the process is to their liking, when the process is not to their liking, additions of humor exacerbate the negative feelings associated with the service experience. With this nuance of humor, in a customer service interaction, it is unclear whether humor will increase the satisfaction for users engaging with the chatbot or whether it will hinder the overall experience.

2.1.4. Humans and Algorithmic Decision Making. Several emerging studies in human resources (Tambe et al. 2019), economics (Kleinberg et al. 2018), and psychology (Dietvorst et al. 2015, 2018; Logg et al. 2019) have investigated how humans respond to algorithmic outcomes. Dietvorst et al. (2015) <sup>fi</sup>nd that in general humans are averse to forecasts made by an algorithm, even when they outperform their less accurate human counterparts. Dietvorst et al. (2018) further this line of inquiry and <sup>fi</sup>nd that algorithmic aversion can be reduced when individuals have the ability to manipulate and make adjustments to the algorithm. Similarly, Tambe et al. (2019) theorize that employees will be less accepting of algorithmically determined shift decisions than those determined by a supervisor, as they could potentially feel less involved in the decision. Interestingly, Tambe et al. (2019), further discuss an anecdote from Uber, describing that individuals negatively respond to surge pricing when they believe it is set by an algorithm.

Contrasting these <sup>fi</sup>ndings, Logg et al. (2019) <sup>fi</sup>nd that individuals can be appreciative of algorithmic judgements in numeric forecasts and recommendations for dating and music, as opposed to those made by humans. In addition, Logg et al. (2019) <sup>fi</sup>nd, similar to Dietvorst et al. (2018), that individuals prefer their own judgements over those of an algorithm. As this aforementioned research indicates, how individuals react to algorithmic outcomes is dependent on context and human involvement.

Behavioral economics has sought to understand how individuals reason through offers. One classic example is the ultimatum game (Guth et al.¨ 1982). In this game, a proposer makes an offer of money, and the offer receiver is to accept or reject the offer. The rational expectation is that the proposer is to make a small offer, and the recipient should accept the offer, regardless of its fairness, because this is the utility maximizing response, that is, take what you can get (Guth et al.¨ 1982). A fairly robust experimental <sup>fi</sup>nding, however, is that offers of 20% of the total funds available are rejected 50% of the time (Sanfey et al. 2003), because of perceived injustice or a lack of fairness.

Previous research has found that human players tend to reject unfair offers less when the actor making an offer is perceived as lacking intentionality, for example, a computer rather than a human. For example, Sanfey et al. (2003) and Moretti and Pellegrino (2010) report that recipient rejection rates for relatively low offers increase when the offer is made by a human versus when the offer is made by a computer (notably, a computer that is totally absent of anthropomorphic features). These authors argue that this occurs because human proposers are more likely to induce recipient emotions, such as disgust (Moretti and Pellegrino 2010).

However, other work has documented contradictory evidence. Torta et al. (2013) found that individuals rejected computer-generated offers in the ultimatum game more frequently than offers made by humans. Torta et al. (2013) theorize that this occurs because human actors have an easier time processing offers from other humans, but face some dif<sup>fi</sup>culty deciding how to respond to offers from computers. For example, the willingness to reject an offer may depend on the manifestation or conformity to social norms and etiquette. Thus, whereas a human actor may have no qualms about rejecting an offer from a nonhuman actor, off hand, social norms might dictate that the human be courteous and considerate when interacting with another human, imposing a sort of social friction on rejection.

More generally, the HCI literature has found that humans respond more socially when computer-based agents are more anthropomorphic (Nass et al. 1994, Kiesler et al. 1996). As one speci<sup>fi</sup>c example, Kiesler et al. (1996) found that human participants presented with a prisoner’s dilemma game tended to respond socially to humanized computer actors, in a manner similar to the response they would exhibit with a true human partner. These <sup>fi</sup>ndings further the notion that a potentially important element leading to offer receivers acceptance or rejection of offers is the level of anthropomorphism of the automated proposer.

As there is ample evidence to support the bene<sup>fi</sup>ts and detriments of including anthropomorphism in customer service chatbots, we take on this study and look to its data to help us reach a conclusion.

## 3. Study Context

As described previously, we conducted our <sup>fi</sup>eld experiment in partnership with a dual channel clothing retailer based in the United States, similar to other businesses such as Plato’s Closet and Clothes Mentor. This retailer buys and sells women’s used clothing, both online and through three brick and mortar locations in Iowa and Minnesota. We replaced the retailer’s prior manual clothing buy-back process with an AI-enabled chatbot. The process we automate was previously managed via web-form and email exchanges, or done in person at a store. We developed the chatbot using Google’s conversational AI platform, DialogFlow, incorporating Python-based customizations. DialogFlow enables the automated processing and generation of conversational prompts and utterances in exchanges employing natural language. The Python customizations were incorporated to implement required business rules and logic, as well as to manage the conversational <sup>fl</sup>ow (e.g., if customer says this, do that). The chatbot was integrated with the retailer’s Facebook business page as part of the retailer’s Facebook Messenger pro<sup>fi</sup>le. The retailer’s Facebook page has approximately 44,000 followers.

The chatbot is designed to interact with customers who are interested in selling their used clothing to the retailer. The overall conversational interaction model has three major steps. First, the chatbot begins by requesting information on the number and types of clothing that the customer wishes to sell. Then, the chatbot provides an estimated cash offer, indicating the expected value that the retailer would be willing to pay for the clothing described. If the customer accepts the offer, the chatbot then requests additional personal details that are required to complete the transaction, including a mailing address, full legal name, and phone number. Based on this information, a shipping label is generated, which the customer can print and use to send their clothes to the retailer.

## 4. Methods

## 4.1. Experiment Design

To causally identify the impact of the aforementioned anthropomorphic features on transaction outcomes, we implement three independently randomized treatments, one associated with each of three anthropomorphic features. When customers initiate a conversation with the chatbot for the <sup>fi</sup>rst time, they are randomized into receiving zero, one, two, or all three of the anthropomorphic features, in random combinations. We describe the implementation of each treatment in the following. Note that by independently randomizing each anthropomorphic feature, we ensure that there is no association between the number of features a customer receives and which features a customer receives. Our randomization is performed on a between-subjects basis. If a single customer revisits our chatbot and initiates additional conversations with our chatbot, we exclude any such subsequent observations from our analysis.

It is worth highlighting that our focus is not on any one of the anthropomorphic treatments, but rather on the number of treatments a subject receives. Our objective in delivering varied numbers of treatments is to causally shift a subject’s perception of anthropomorphism in the chatbot interaction. Conceptually, this approach is analogous to the notion of combination therapy or polytherapy in medicine, which refers to treating a single disease with multiple types of interventions in concert (e.g., Mott¨ onen et al.¨ 1999). We opt for this approach, rather than attempting to manipulate the intensity of a given anthropomorphic feature by shifting its level, for two reasons. First, it is not altogether clear how dosage manipulations could be achieved with each of the treatments, for example, it is not altogether clear what would constitute more versus less humor. Second, the perception that one is certainly interfacing with a human actor is unlikely to be achieved through a single manipulation, even in a text-based setting. A chatbot that responds instantaneously, yet also drops a joke into the conversation, may be perceived as having some human traits. However, it is unlikely that simply adding more jokes into the exchange will achieve further improvements. Thus, it is reasonable to assume that anthropomorphism depends a great deal on delivering a suf<sup>fi</sup>cient constellation of anthropomorphic features as part of the exchange.<sup>4</sup>

![](/api/attachments/QJCFR6B8/fulltext/images/f1c23c522de1bc646a197b27f0f9b63338a1f335e6d049153f73f5f5029a2d35.jpg)

Additionally, for all customers, we introduce random variation into the cash offer. In the original buyback process, the retailer would calculate an initial cash offer based on a <sup>fi</sup>xed amount of \$3.50 per clothing item. We randomly perturbed the offer around the <sup>fi</sup>xed baseline offer for each customer, drawing from a random normal distribution with mean 0 and variance 0.5. That is, our offer perturbations were implemented by taking the \$3.50 baseline offer previously employed by the retailer and adding a random value drawn from this normal distribution. Drawing from a normal distribution allowed us to accommodate concerns on the part of the retail partner that cash offers would be too extreme in either direction, creating customer experience issues on the one hand and economic losses for the retailer on the other hand.

4.1.1. Social Presence. To operationalize anthropomorphic social presence, we do so through a combination of a name, linguistic features, and social cues related to reading and authoring messages. We thus adopt a methodology similar to that of Araujo (2018). More speci<sup>fi</sup>- cally, in this treatment, we <sup>fi</sup>rst give the chatbot a randomly drawn human name from the 1990 census, which the chatbot uses to introduce itself at the outset of the conversation. Second, like Araujo (2018), the chatbot employs relatively informal, casual language (as opposed to more formal, professional language). An example of the initial greeting manipulation can be found in Table 1.

In the human-like condition, users will also see the cues typically associated with messages exchanged between humans. On the Facebook Messenger platform, these cues include both read receipts when a message is sent to the chatbot, as well as the display of a cue indicating that the chatbot is typing a message. Examples of the typing feature can be seen in Figure 2 and read receipts in Figure 3.

Table 1. Social Presence Manipulation

<table><tr><td>Condition</td><td>Message</td></tr><tr><td>0</td><td>Hello I am an automated service bot here to assist with shipping previously used maternity clothing for money.</td></tr><tr><td>1</td><td>Hi I&#x27;m Teddy here to help you with shipping previously loved maternity clothes for $.</td></tr></table>

In conditions where these cues are not present, the user sees simply the white messenger background without the read receipts or typing features.

4.1.2. Communication Delays. Similar to Moon (1999) and Holtgraves and Han (2007), we implement a dynamic delay of 70 words per minute. This is within the range of those that type professionally.<sup>5</sup> In the non-human-like condition, users will experience instant responses.

4.1.3. Humor. To operationalize the humor construct, we insert a random joke drawn from an approved list of four jokes. These jokes were deemed to be inoffensive and suitable for any age. The random jokes are added into the dialogue, right before customers receive the estimate for the clothes they will be selling to the retailer. In conditions that do not have humor present, customers are asked if they will wait a moment while the chatbot totals up their estimate, and a <sup>fi</sup>ve-second-long pause ensues. This interaction is depicted in Figure 4. A brief summary of all manipulations can be found in Table 2.

## 4.2. Empirical Specification, Variables, and Data

In our analyses, we are interested in understanding the effect of increasing humanization of the chatbot on (i) the probability of conversion and (ii) the moderating effect on the relationship between the randomly varied offer amount and conversion. Accordingly, our primary outcome variable of interest is a binary indicator of conversion. Our independent variables include a series of dummy variables re<sup>fl</sup>ecting different levels of the number of anthropomorphic treatments a subject received, Treatment\_Count, as well as a measure re<sup>fl</sup>ecting our offer perturbation, Cash Offer, which we mean-center for the sake of simplicity.

We <sup>fi</sup>rst estimate a series of linear probability models (LPMs), regressing conversion on our treatment count dummies and our offer deviation measure, to understand their direct effects. Subsequently, we interact the dummies and the offer measure to

Figure 2. (Color online) Typing Feature understand the moderating effects of interest, that is, how increasing anthropomorphism moderates offer sensitivity. Our <sup>fi</sup>nal cash offer sensitivity model is re-<sup>fl</sup>ected in Equation (1), where subjects are indexed by i.

$$
\begin{array}{r l} C o n v e r t _ {i} = & \alpha + \beta_ {1} \cdot 1 T r e a t m e n t _ {i} + \beta_ {2} \cdot 2 T r e a t m e n t s _ {i} \\ & + \beta_ {3} \cdot 3 T r e a t m e n t s _ {i} \\ & + \delta \cdot C a s h O f f e r _ {i} + \gamma_ {1} \cdot 1 T r e a t m e n t _ {i} \\ & \cdot C a s h O f f e r _ {i} + \gamma_ {2} \cdot 2 T r e a t m e n t s _ {i} \cdot C a s h O f f e r _ {i} \\ & + \gamma_ {3} \cdot 3 T r e a t m e n t s _ {i} \cdot C a s h O f f e r _ {i} + \epsilon_ {i}. \end{array}\tag{1}
$$

Our experiment includes 323 subjects who initiated a conversation with our chatbot between November 16 and December 31 of 2018. We present the descriptive statistics for our variables in Table 3. As can be seen, approximately 8.36% converted, meaning they completed the buy-back procedure and obtained a shipping label to send their clothes to the retailer. We also observe that the average user received 1.5 anthropomorphism treatments. Figure 5 depicts the distribution of randomized per-item offers that were assigned to subjects. As explained earlier, the distribution of offer deviations is normal.

## 5. Results

We begin by estimating a linear probability model, incorporating only the main effects of each variable. We then progress to incorporating interactions to recover any effect of cash offer increases on conversion outcomes under alternative levels of anthropomorphism.

Considering the results in Table 4, in column 1, the constant term indicates that the baseline rate of conversion in the control condition (no anthropomorphic treatments) is approximately 2.6%. We observe positive coef<sup>fi</sup>cients associated with all other variables in the model. Speci<sup>fi</sup>cally, we observe that a single anthropomorphic treatment is associated with a 6.7% increase in the probability of conversion $( p < 0 . 1 0 )$ , relative to control; a pair of treatments is associated with a 5.0% increase in the probability of conversion (though the result is not statistically signi<sup>fi</sup>cant relative to a null hypothesis of 0); and the receipt of all three treatments in tandem is associated with a 10.8% increase in the probability of conversion $( p < 0 . 0 5 )$ ). Although the coef<sup>fi</sup>cient on cash offer is positive as we expect (given this is a cash offer made to the customer, not a cash offer charged), the coef<sup>fi</sup>cient is not statistically signi<sup>fi</sup>cant. That said, the estimate indicates that a \$1.00 increase in the cash offer is associated, on average, with a 2.7% increase in the probability of conversion.

Figure 3. (Color online) Read Receipt Is Shown as Small Pro-<sup>fi</sup>le Image on Right  
![](/api/attachments/QJCFR6B8/fulltext/images/6a2205f1236bd729f67a1067727bd36573291476845bc1d9ca475152afa1691b.jpg)

Figure 4. (Color online) Joke Example  
![](/api/attachments/QJCFR6B8/fulltext/images/63ed232bfbe1855c3817d6e8ed2d65b4c7421798cb8dc44fdab508876048d9b5.jpg)

Next, considering the interaction model in column 2, the main effects associated with the intensity of anthropomorphism remain quite consistent, except that all three estimates are now statistically signi<sup>fi</sup>cant at commonly accepted thresholds (when our cash offer manipulation is 0). Additionally, considering the cash offer interactions, we see that all coef<sup>fi</sup>cients are positive and increasing in the number of treatments. Of particular note, we observe that the cash offer manipulation has a statistically signi<sup>fi</sup>cant interaction with the delivery of three anthropomorphic treatments, relative to the delivery of none $( p < 0 . 0 5 )$ . This <sup>fi</sup>nding indicates that, in the presence of suf<sup>fi</sup>cient anthropomorphism, consumers become signi<sup>fi</sup>cantly more offer sensitive.

## 6. Robustness

## 6.1. Estimator Choice and Regression Specification

We begin by considering the robustness of our results to possible concerns of multicollinearity, as well as to our choice of estimator. We report analyses addressing possible concerns of multicollinearity in the online appendix, where we provide evidence that this is not a serious concern in our analysis. Subsequently, in the online appendix, we explore the robustness of our results to our choice of estimator, namely the linear probability model. There, we demonstrate that our results remain stable under alternative estimator choices.

Table 2. Chatbot Features

<table><tr><td>Feature</td><td>Description</td></tr><tr><td>Social presence</td><td>Human name, informal language, typing cues</td></tr><tr><td>Delay</td><td>Dynamically typed 70 WPM delay</td></tr><tr><td>Humor</td><td>Randomly selected joke before estimate</td></tr></table>

Table 3. Descriptive Statistics

<table><tr><td>Variable</td><td>Mean</td><td>St. Dev.</td><td>Min</td><td>Max</td></tr><tr><td>Social Presence</td><td>0.56</td><td>0.50</td><td>0.00</td><td>1.00</td></tr><tr><td>Delay</td><td>0.48</td><td>0.51</td><td>0.00</td><td>1.00</td></tr><tr><td>Humor</td><td>0.46</td><td>0.50</td><td>0.00</td><td>1.00</td></tr><tr><td>Treatment Count</td><td>1.50</td><td>0.89</td><td>0.00</td><td>3.00</td></tr><tr><td>Cash Offer</td><td>-0.02</td><td>0.68</td><td>-1.82</td><td>1.43</td></tr><tr><td>Conversion</td><td>0.0836</td><td>0.2772</td><td>0</td><td>1</td></tr></table>

## 6.2. Replication

We next assessed the replicability of our main <sup>fi</sup>nding, that anthropomorphism increases transaction rates, conducting a second, simpler experiment in the same <sup>fi</sup>eld setting. With this replication, we sought to again address possible concerns that our results somehow derive from aggregating across multiple treatments. With that concern in mind, we sought to evaluate the treatment effect of just a single anthropomorphism treatment, relative to a control condition. This replication thus allowed us to assess whether, given suf<sup>fi</sup>- cient power, a single anthropomorphism intervention would yield statistically signi<sup>fi</sup>cant estimates of increased conversion. We focused on the social presence treatment in this replication, because it is the intervention that aligns most intuitively with anthropomorphism (Araujo 2018).

The replication was conducted in the same <sup>fi</sup>eld context. The only distinction in this case is that our experiment was limited to just two conditions: the control condition, in which no anthropomorphism treatment was delivered, and the social presence condition. As before, we assessed the relationship between the treatment and the probability of successful conversion. This experiment was carried out over a one-month period, from late June to late July of 2019. Recruitment for the replication study was conducted in the same manner, employing Facebook Messenger advertisements.

Figure 5. Distribution of Per-Item Offer Deviation  
![](/api/attachments/QJCFR6B8/fulltext/images/2327b7600ed1199c848ba1ed11debf94788795ce382e2ec1b8e6b814bea4a763.jpg)

Table 4. Treatment Count Model (LPM)

<table><tr><td>Variable</td><td>Dependent variable: Convert</td><td>Dependent variable: Convert</td></tr><tr><td>1 Treatment</td><td>0.067* (0.036)</td><td>0.076** (0.032)</td></tr><tr><td>2 Treatments</td><td>0.050 (0.034)</td><td>0.060** (0.030)</td></tr><tr><td>3 Treatments</td><td>0.108** (0.055)</td><td>0.109** (0.049)</td></tr><tr><td>1 Treatment · Cash Offer</td><td>—</td><td>0.052 (0.064)</td></tr><tr><td>2 Treatments · Cash Offer</td><td>—</td><td>0.086 (0.069)</td></tr><tr><td>3 Treatments · Cash Offer</td><td>—</td><td>0.211** (0.087)</td></tr><tr><td>Cash Offer</td><td>0.027 (0.022)</td><td>-0.058 (0.057)</td></tr><tr><td>Intercept</td><td>0.026 (0.023)</td><td>0.017 (0.017)</td></tr><tr><td>Observations</td><td>323</td><td>323</td></tr><tr><td> $R^2$ </td><td>0.016</td><td>0.037</td></tr><tr><td>F-Statistic</td><td>1.60 (4,319)</td><td>3.85*** (7,316)</td></tr></table>

Note. Robust standard errors.  
\*p < 0.10; \*\*p < 0.05; \*\*\*p < 0.01.

This experiment involved 546 subjects, who were approximately balanced in their assignment to treatment and control; the mean value of our treatment indicator, Social Presence, was 0.46. As before, we regressed a binary indicator of transaction conversion onto a treatment dummy, employing a linear probability model. As before, we observe a positive, statistically signi<sup>fi</sup>cant effect on conversion rates with this single, individual treatment. Speci<sup>fi</sup>cally, social presence features led to an approximate 5% increase in the transaction conversion rate $( p ~ = ~ 0 . 0 4 6 )$ . Thus, we successfully replicate the main result. Moreover, we conclude that, given suf<sup>fi</sup>- cient statistical power, we can detect that a single anthropomorphism treatment can translate to tangible bene<sup>fi</sup>ts for transaction conversion.

## 6.3. Manipulation and Randomization Checks

We performed a manipulation check with 19 volunteers to ensure that the various treatments were properly experienced by users, and that they had the expected effects on both anthropomorphism level and perceptions of manipulations. To determine if end users indeed experienced the delay and humor treatments, we asked participants to rate their agreement with certain statements, on a scale of 1 (strongly agree) to 6 (strongly disagree). For the humor treatment, the statement was: The customer service agent was humorous. For the delay treatment, the statement was: The customer service agent took a long time to respond. To analyze the survey responses, we used the Mann-Whitney U test (Mann and Whitney 1947). In Table 5, we <sup>fi</sup>nd that there is a signi<sup>fi</sup>cant difference between responses that were in the humor and nonhumor conditions and the delay and nondelay condition. This is signi<sup>fi</sup>cant at the $p \leq 0 . 0 1$ level.

Table 5. Results Mann-Whitney Rank Sum Test for Manipulation’s Perceptions of Delay and Humor

<table><tr><td>Condition comparison</td><td>p-value</td><td>z-score</td></tr><tr><td>Humor vs. nonhumor</td><td>0.0045</td><td>2.842</td></tr><tr><td>Delay vs. nondelay</td><td>0.0006</td><td>3.417</td></tr></table>

In addition to running the tests for both the humor and delay manipulations, we tested whether the delivery of these features in tandem with linguistic features led to a higher perception of anthropomorphism. To test this, we used a semantic differential scale, including survey items <sup>fi</sup>rst introduced by Powers and Kiesler (2006). These survey items are also a component of the Godspeed questionnaire (Bartneck et al. 2008), a widely used survey in the HCI and human-robot interaction literature to measure anthropomorphism (Weiss and Bartneck 2015). The semantic scale ranges from 1 to 6, for <sup>fi</sup>ve binary word associations: (fake, natural), (machinelike, human-like), (unconscious, conscious), (arti<sup>fi</sup>cial, lifelike), (moving rigidly, moving elegantly). The lower the score, the less anthropomorphic the artifact is perceived to be. Note that we adapted the <sup>fi</sup>nal word-pair to our textual context, replacing it with (messages rigidly, moving elegantly). The original scale was developed for use with physical artifacts, that is, robots, to capture perceptions of movement in physical space; however, because our artifact only exists on the Facebook Messenger platform, slight modi<sup>fi</sup>cation was necessary. We averaged the values across the <sup>fi</sup>ve semantic differential scale items to arrive at our <sup>fi</sup>nal measure.

To determine if the addition of these features leads to higher perceptions of anthropomorphism, we sum the treatment dummies associated with the features: social presence, communication delays, and humor, such that we construct a measure capturing the number of treatments a subject receives (which we expect to associate with increasing levels of perceived anthropomorphism). We then perform an ordinary least squares regression of the mean anthropomorphism differential scale response against the count of treatments received. Doing so, we <sup>fi</sup>nd a statistically significant, positive association $( \beta = 0 . 6 1 9 ; p < 0 . 1 \dot { 0 } )$ This manipulation check parallels our main analyses, described earlier, in which we explore the relationship between the number of treatments a subject receives, and their conversion response. Conceptually, our approach is analogous to the notion of combination therapy or polytherapy in medicine, which refers to efforts to tackle a single disease with multiple treatments in tandem (e.g., Mott¨ onen et al.¨ 1999). Measures similar to that we employ here have been advanced in the medical literature, that is, based on a summation over treatment interventions received by a patient or subject (Frei et al. 1998). Thus, rather than attempt to manipulate the intensity of anthropomorphism by shifting the levels of any given treatment (it is not altogether clear what would constitute more versus less humor, or greater versus less social presence), we opt for the delivery of more versus fewer treatment options, in combination, to achieve our manipulations.

In addition to these manipulation checks, we conducted a number of randomization checks to assess the ef<sup>fi</sup>cacy of our randomization procedure. Because we randomize in real time, as subjects arrive, and only have a small set of information describing our subjects available from Facebook, we are limited in the types of randomization checks we are able to perform. As such, one check we can perform is to assess the signi<sup>fi</sup>cance of the association between the number of treatments a subject was assigned and the day on which they entered our sample. To assess this, we perform a multinomial logistic regression of the number of treatments assigned on a vector of day of week indicators. We report the results of this regression in Table 6, where all coef<sup>fi</sup>cients are statistically insigni<sup>fi</sup>cant. A similar analysis performed as a ordinal logistic regression also yields null results. This provides some assurance that our randomization procedure was effective.

Beyond this assessment of intertemporal randomization, we also assessed randomization ef<sup>fi</sup>cacy in two other ways. Speci<sup>fi</sup>cally, we assessed possible systematic associations between the per-unit cash offer and the treatments a subject was assigned, as well as possible systematic associations between the per-unit cash offer and the number of clothes a subject wished to sell. Each evaluation was conducted via a series of pairwise t-tests, testing for signi<sup>fi</sup>cant differences in pairwise group means. This was done both in terms of treatment count assignments, as well as speci<sup>fi</sup>c treatment assignments. In all cases, we observe statistically insigni<sup>fi</sup>cant differences across groups. These results are presented in the online appendix.

## 7. Mechanism Exploration

Although we have demonstrated a robust, positive, causal relationship between anthropomorphism features and transaction conversion, it is important to also assess the boundary conditions for our <sup>fi</sup>ndings, as well as to assess the extent to which anthropomorphism is the primary mechanism behind this relationship. Accordingly, we undertook a variety of secondary analyses and controlled experiments. We <sup>fi</sup>rst sought to better understand the extent of perceived anthropomorphism associated with our most anthropomorphic chatbot, and how it compared with an obvious benchmark, namely a true human agent. This exercise is important, because it speaks to the potential for further gains, above and beyond the anthropomorphism levels we implemented in this study.

Table 6. Randomization Check (MLOGIT; Dependent Variable: Treatment Count)

<table><tr><td>Variable</td><td>Treatments = 1</td><td>Treatments = 2</td><td>Treatments = 3</td></tr><tr><td>Tuesday</td><td>0.872 (0.696)</td><td>0.280 (0.722)</td><td>0.118 (0.859)</td></tr><tr><td>Wednesday</td><td>1.034 (0.689)</td><td>1.069 (0.683)</td><td>0.929 (0.774)</td></tr><tr><td>Thursday</td><td>0.178 (0.599)</td><td>0.118 (0.596)</td><td>-0.352 (0.750)</td></tr><tr><td>Friday</td><td>0.588 (0.661)</td><td>0.057 (0.687)</td><td>0.300 (0.778)</td></tr><tr><td>Saturday</td><td>0.523 (0.630)</td><td>0.463 (0.627)</td><td>0.405 (0.728)</td></tr><tr><td>Sunday</td><td>0.187 (0.620)</td><td>0.554 (0.598)</td><td>-0.442 (0.794)</td></tr><tr><td>Constant</td><td>0.575 (0.417)</td><td>0.636 (0.413)</td><td>-0.118 (0.487)</td></tr><tr><td>Observations</td><td>324</td><td></td><td></td></tr><tr><td>Pseudo  $R^{2}$ </td><td>0.014</td><td></td><td></td></tr><tr><td>Wald Chi $^{2}$ </td><td>10.94 (18)</td><td></td><td></td></tr></table>

Note. The baseline outcome is 0 treatments; robust standard errors.

To assess this question, we recruited 54 turkers from Amazon Mechanical Turk and assigned them to interface either with (i) our most anthropomorphic chatbot or (ii) a human agent, drawn at random from a pool of four graduate research assistants.<sup>6</sup> These human customer service agents were given a high-level verbal instruction about the information they needed to supply and collect from visitors to complete the buy-back process, including examples of past chatbot interactions.

Each research assistant received a brief training session with one of the authors, and each was observed in a customer service interaction before the experiment was begun to ensure proper understanding of the script. Subsequent to interacting with a customer service agent (either the chatbot or a human), the turkers were asked to respond to a pair of survey items, rating their perceptions of the respective agent’s anthropomorphism. To gauge anthropomorphism, we utilized a semantic differential scale, including survey items <sup>fi</sup>rst introduced by Powers and Kiesler (2006), which ask the subject to rate their interaction on a 1 to 6 scale for <sup>fi</sup>ve binary word associations: (fake, natural), (machine-like, human-like), (unconscious, conscious), (arti<sup>fi</sup>cial, lifelike), (messages rigidly, messages elegantly).

The results of this comparison are presented in Figure $6 ,$ which depicts group means and 95% con<sup>fi</sup>- dence intervals. A Mann-Whitney U test indicates that a randomly drawn human agent was perceived to be more anthropomorphic than the fully anthropomorphic chatbot, to a statistically signi<sup>fi</sup>cant degree $( p < 0 . 0 5 )$ . The difference on a six-point scale is 2.97 versus 3.93. This <sup>fi</sup>nding does suggest that there is room to further increase perceived anthropomorphism of our chatbot, and perhaps garner greater bene<sup>fi</sup>ts for transaction outcomes.

Next, we sought to understand the extent to which our results might derive from our anthropomorphic treatments causing subjects to believe they were truly interfacing with a human agent versus whether subjects were aware the agent was autonomous and were merely personifying its behavior. Understanding this aspect is important for two reasons. First, there has recently been a push from government regulators to require the disclosure of agents’ autonomous nature at the outset of any customer interactions (National Law Review 2019). Accordingly, from a practical perspective, if our results are somehow dependent on the absence of formal disclosure, this would be undesirable, as the value of these <sup>fi</sup>ndings would be undercut by ongoing regulatory changes in the market. Second, recent work involving voice-based chatbots has reported that a failure to disclose a bot’s autonomous nature at the outset of interactions can have detrimental effects on transaction outcomes, if a customer initially believes the agent to be a human, and discovers its autonomous nature only later (Luo et al. 2019).

Our analysis was conducted in a manner similar to the previous anthropomorphism bench-marking exercise. Speci<sup>fi</sup>cally, we recruited 52 turkers to interface with one of two chatbots: (i) our fully anthropomorphic chatbot (which lacks explicit disclosure that it is autonomous) and (ii) our fully anthropomorphic chatbot, incorporating disclosure. Up-front disclosure was achieved in the latter case by removing the human name and replacing it with the title “customer service chatbot.” Again, subsequent to these turkers’ interactions with their assigned agent, we asked them to respond to survey items. Because we lack objective transaction outcomes in this context, we instead relied upon a proxy response, namely an indication of likeability. For this purpose, we employed adaptations of the survey questions from Mathur and Reichling (2016), obtaining responses to the following prompt: “Rate how enjoyable/unpleasant it was interacting with your customer service agent,” responding using a sliding scale from 100 to 100. The results are presented in Figure 7, which again depicts group means and 95% con<sup>fi</sup>dence intervals.

Figure 6. Perceived Anthropomorphism: (Left) True Human vs. (Right) Anthropomorphic Chatbot  
![](/api/attachments/QJCFR6B8/fulltext/images/1f02daecd5fb79164eb95c9aac8295207ed9aae283df2252d0ab541b8cee788e.jpg)

Interestingly, in this case, we <sup>fi</sup>nd that, counter to expectation, the fully anthropomorphic chatbot without disclosure was perceived to be signi<sup>fi</sup>cantly less likeable than the same chatbot incorporating disclosure $( p < 0 . 1 0 )$ . Importantly, this <sup>fi</sup>nding indicates that the increases in transaction rates are not dependent upon a lack of disclosure that the agent is autonomous. To the contrary, explicit disclosure appears to improve customer perceptions. It is plausible that this occurs because, in our context, users can very quickly deduce that the agent is not human, based on its conversational behavior (even without disclosure). Thus, when the chatbot initially presents a human name, this may create an expectation of human interaction, only to be let down shortly thereafter when the customer perceives that responses are automated. What is more, such rapid realization of the chatbot’s autonomous nature may lead customers to perceive some attempt at deception. Under this logic, our <sup>fi</sup>ndings are in fact consistent with those recently reported by Luo et al. (2019), who found that individuals reacted negatively to delayed disclosure of a chatbot’s autonomous nature versus earlier disclosure.

Having evaluated the anthropomorphism of our chatbots relative to human agents, and having considered whether our results are somehow dependent upon a lack of disclosure, we next turned our attention to an exploration of the underlying mechanisms by which anthropomorphism may bene<sup>fi</sup>t transaction outcomes. Our earlier offer sensitivity result speaks to this somewhat, in that it suggests that subjects think differently when engaging with an anthropomorphic chatbot. However, we wished to identify concrete evidence of how this differential mindset may bene<sup>fi</sup>t transaction outcomes.

One particularly plausible mechanism pertains to humans’ trust and willingness to engage in information sharing with autonomous agents. Prior work has observed that a socializing technology can lead to increased persuasion of users (Holzwarth et al. 2006, Wang et al. 2007a) and can lead to more intimate selfdisclosure (Moon 2000). In a customer service interaction, social cues may thus lead to greater comfort with the automated customer service agent on the human customer’s part, which then leads to increased levels of information sharing (Sproull et al. 1996). It is therefore possible that the positive relationship between anthropomorphism and transaction conversion is driven, at least in part, by customers’ increased willingness to share sensitive data with the customer service agent that is necessary to complete the transaction.

Figure 7. Perceived Likeability: (Left) Undisclosed Chatbot vs. (Right) Disclosed Chatbot  
![](/api/attachments/QJCFR6B8/fulltext/images/286beeb5dd87411f83011cac14abd31e9c1e10a78cd6a663b0691481ca489a2c.jpg)

To explore this possibility, we revisited our original experimental results, considering the treatments’ relationship with different information disclosure milestones within the clothing buy-back process. After the offer is seen by a subject, the chatbot proceeds to ask a series of questions to collect contact information that is necessary to complete the transaction. Some of that information is innocuous (i.e., the required dimensions for a shipping box), whereas other information is relatively sensitive (i.e., mailing address, legal name, telephone number). In Table 7, we present the results of repeating our main regression using these different milestones as alternative dependent variables.

As we can see from the results, the anthropomorphic treatments begin to have a statistically signi<sup>fi</sup>cant effect as the customer moves further into the process, as the information becomes more sensitive. Although exploratory in nature, these initial results suggest a partial explanation for the effects we see. Certainly, they point to a potentially fruitful area for further inquiry and policy debate around the incorporation of features aimed to achieve anthropomorphism in autonomous, customer-facing agents.

## 8. Discussion and Conclusion

Our study offers a novel glimpse into how chatbot anthropomorphism, in a real-world customer service setting, in<sup>fl</sup>uences business outcomes. We explore prior design theory from HCI, which speaks to the consequences of incorporating anthropomorphic features into an autonomous agent, and the implication for various social outcomes, for example, trust. Although there is reason to believe that trust will lead to customer satisfaction, thereby translating to economic bene<sup>fi</sup>ts for the <sup>fi</sup>rm, it is important to recognize that customer trust and satisfaction with a service provider are only two mediating factors that determine transaction outcomes. For example, although customers may be more trusting of a human-like autonomous agent, they may simultaneously perceive operational inef<sup>fi</sup>- ciency, and then opt to transact with an alternative provider. Nonetheless, our results are consistent with the notion that anthropomorphic features have a direct, bene<sup>fi</sup>cial relationship with transaction outcomes. Our <sup>fi</sup>ndings are also consistent with prior studies of anthropomorphism’s impact upon trust.

Table 7. Information Disclosure Milestones (LPM)

<table><tr><td>Variable</td><td>Dependent variable: Box Size</td><td>Dependent variable: Mailing Address</td><td>Dependent variable: Legal Name</td><td>Dependent variable: Phone Number</td></tr><tr><td>1 Treatment</td><td>0.042 (0.0546)</td><td>0.063 (0.043)</td><td>0.078** (0.036)</td><td>0.078** (0.036)</td></tr><tr><td>2 Treatments</td><td>0.061 (0.0558)</td><td>0.056 (0.043)</td><td>0.071** (0.036)</td><td>0.071** (0.036)</td></tr><tr><td>3 Treatments</td><td>0.066 (0.0712)</td><td>0.113* (0.064)</td><td>0.136** (0.060)</td><td>0.136** (0.060)</td></tr><tr><td>Intercept</td><td>0.093 (0.045)</td><td>0.047 (0.032)</td><td>0.023 (0.0231)</td><td>0.023 (0.0231)</td></tr><tr><td>Observations</td><td>323</td><td>323</td><td>323</td><td>323</td></tr><tr><td> $R^2$ </td><td>0.004</td><td>0.009</td><td>0.015</td><td>0.015</td></tr><tr><td>F</td><td>0.46 (3,319)</td><td>1.30 (3,319)</td><td>2.88** (3,319)</td><td>2.88** (3,319)</td></tr></table>

Note. Robust standard errors.  
\*p < 0.10; \*\*p < 0.05; \*\*\*p < 0.01.

Interestingly, we also <sup>fi</sup>nd that whereas anthropomorphism in<sup>fl</sup>uences transaction conversion positively, it also impacts a customer’s offer sensitivity. Although our context is somewhat unique to retailers, our <sup>fi</sup>ndings do give reason to believe that high levels of anthropomorphism are not to be incorporated in all customer service chatbots, and its bene<sup>fi</sup>ts may be dependent on contextual factors. We also <sup>fi</sup>nd that anthropomorphism, in our context, plays the most important role in sensitive information disclosure. More speci<sup>fi</sup>cally, we analyzed how anthropomorphism in<sup>fl</sup>uenced conversion of intermediate variables within the buy-back process, and found that it plays a bigger role as customers input more personal information. Though preliminary, this highlights that in certain contexts in which <sup>fi</sup>rms require information from their customer, high levels of anthropomorphism could be advantageous. In further experiments discussed in the online appendix on Mechanical Turk, we also <sup>fi</sup>nd that the individual treatment drives likeability of the agent, and this in turn could be driving much of these conversion outcomes.

Another notable <sup>fi</sup>nding comes from our follow-up studies involving crowd workers. We sought to evaluate whether the practice of disclosing the chatbot’s autonomous nature would in<sup>fl</sup>uence user perceptions of likeability (our proxy for customer satisfaction). Ultimately, we found that disclosure (i.e., a chatbot that uses a name like customer service chatbot) was more likeable than the undisclosed chatbot (employing a human name). As we noted earlier, we believe this occurs because customers quickly come to realize that they are not interacting with a human, even in the absence of explicit disclosure. Whereas disclosure makes this clear immediately, a failure to disclose may thus translate to delayed (and unplanned) disclosure, which customers could interpret as an attempt at deception, or falling short of their expectations (Oliver 1977). This <sup>fi</sup>nding once again points to the importance of context and customer expectations. If customers are operating in an environment where they anticipate engaging with automated customer service agents, their expectations for the exchange may be quite different than alternative settings in which a human agent is expected. Recent research has observed that many consumers have grown more comfortable with the notion of algorithms in their daily lives, going so far as to exhibit algorithm appreciation (Logg et al. 2019). This aspect is important for <sup>fi</sup>rms considering the design and implementation of autonomous customer service agents.

Additionally, chatbots represent a means by which <sup>fi</sup>rms can ensure consistent performance in their human-facing customer service roles. In many customer service jobs, individuals are expected to perform routinized tasks with nearly mechanistic ef<sup>fi</sup>ciency and perfection. This is dif<sup>fi</sup>cult because individual workers behave differently from each other, and individuals vary their behavior throughout the day. This standardization of service delivery is both a chief concern among most retailers today,<sup>7</sup> as well as a key reason many <sup>fi</sup>rms are considering implementing autonomous customer service agents.<sup>8</sup> As such, a potentially effective compromise that simultaneously leverages the social intelligence of humans, in tandem with the standardized delivery enabled by autonomous agents, is to imbue chatbots with social intelligence (Wang et al. 2007b). Although current conversational technologies are unlikely to replace the best human customer service agents in the short term, it is plausible that socially intelligent chatbots could lead to improvements in the customer experience if employees exhibit issues with consistency of service delivery and service experience. This observation resonates with the <sup>fi</sup>ndings of Luo et al. (2019) that autonomous agents may perform better than inexperienced workers in a sales context.

Our research also points to possible opportunities for intelligence augmentation (Jain et al. 2018). First, our work demonstrates that augmenting AI-enabled autonomous agents with human-like social intelligence can increase their performance in customer service settings (Wang et al. 2007b). What is more, our research design suggests a procedure by which <sup>fi</sup>rms might leverage autonomous chatbot implementations to experimentally evaluate the most effective patterns of customer interaction, with an eye toward informing the training of human customer service agents. For instance, our experimental results demonstrated that some degree of humor (discussed in the online appendix) can lead to increased conversion rates in this clothing buy-back process. Accordingly, companies might leverage this approach to deduce what works in their context, with their customer base.

Also important to note, our <sup>fi</sup>ndings are particular to this retailing cash offer scenario. Whether these results will translate to a purchasing, frequently asked questions, or healthcare implementation of a chatbot, requires more research. Where anthropomorphism could keep users more engaged in some scenarios, it could also lead to further user frustrations. For example, in a medical diagnosis context, incorporating these anthropomorphic features could inadvertently trigger patients to try and portray themselves in a more positive light (Sproull et al. 1996), and give less accurate depictions of their symptoms. Although anthropomorphism is one aspect that AI designers can use to impact user experience, we also believe that there is fruitful future work evaluating many other aspects such as chatbot personality and user-based customization.

In summary, our work provides a unique <sup>fi</sup>rst step toward understanding social and behavioral factors that are worth considering in <sup>fi</sup>rms’ deployment of autonomous, AI-enabled systems in customer-facing roles. We show that whereas overall transaction conversion positively increases with anthropomorphism, anthropomorphizing agents can come with several unintended consequences, such as greater offer sensitivity. Given that the deployment of chatbots is already quite common, it behooves researchers to further our understanding of best practices for design and implementation of these systems, and what collateral consequences such design decisions may have on the human agent interaction. It is our hope that this study will spur a new stream of literature in that direction.

## Endnotes

<sup>1</sup> See https://www.gartner.com/en/newsroom/press-releases/2017- 12-13-gartner-says-by-2020-artificial-intelligence-will-create-more-jobsthan-it-eliminates.

<sup>2</sup> See https://www.gartner.com/smarterwithgartner/gartner-predictsa-virtual-world-of-exponential-change/.

We opt to implement the intensity of anthropomorphism via introducing combinations of treatments, rather than manipulating the level of one treatment, because this enables us to abstract away from any specific cue, to infer effects from anthropomorphism more broadly. In our robustness checks section, we explore the pattern of effects that emerges when we estimate the effect of different combinations of specific cues. There, we demonstrate a pattern consistent with the idea that each cue has a directionally consistent effect on conversion, indicating that our abstraction away from particular cues to anthropomorphism more broadly is justified.

<sup>4</sup> We offer later analyses, namely manipulation checks, that indicate that perceived anthropomorphism is increasing in the number of treatments received, providing support for our argued mechanism.

<sup>5</sup> See https://www.livechatinc.com/typing-speed-test/#/.

<sup>6</sup> The use of multiple human agents is particularly important for this analysis, if we wish our results to be plausibly generalizable. If we were to compare our chatbot against a single human agent, it would be quite difficult to draw conclusions about how the bot might compare with human agents, broadly, versus the particular human agent participating in the study.

<sup>7</sup> See https://www.emarketer.com/chart/229895/leading-businesschallenges-facing-in-store-retail-according-us-retailers-may-2019-ofrespondents.

<sup>8</sup> See https://www.drift.com/wp-content/uploads/2018/01/2018- state-of-chatbots-report.pdf.

## References

Aaker JL (1997) Dimensions of brand personality. J. Marketing Res. 34(3):347–356.

Araujo T (2018) Living up to the chatbot hype: The in<sup>fl</sup>uence of anthropomorphic design cues and communicative agency framing on conversational agent and company perceptions. Comput. Human Behav. 85:183–189.

Barrett JL, Keil FC (1996) Conceptualizing a nonnatural entity: Anthropomorphism in god concepts. Cognitive Psych. 31(3):219–247.

Bartneck C, Kulić D, Croft E, Zoghbi S (2008) Measurement instruments for the anthropomorphism, animacy, likeability, perceived intelligence, and perceived safety of robots. Internat. J. Soc. Robotics 1(1):71–81.

Brown P, Levinson SC (1987) Politeness: Some Universals in Language Use (Cambridge University Press, Cambridge, UK).

Caporael L (1986) Anthropomorphism and mechanomorphism: Two faces of the human machine. Comput. Human Behav. 2(3):215–234.

Cassell J, Bickmore T (2000) External manifestations of trustworthiness in the interface. Comm. ACM 43(12):50–56.

Crozier R (2017) Lufthansa delays chatbot’s responses to make it more ‘human’. iTnews (May 24), https://www.itnews. com.au/news/lufthansa-delays-chatbots-responses-to-make-itmore-human-462643.

Dale R (2016) The return of the chatbots. Natl. Language Engrg. 22(05):811–817.

Dietvorst BJ, Simmons JP, Massey C (2015) Algorithm aversion: People erroneously avoid algorithms after seeing them err. J. Experiment. Psych. General 144(1):114–126.

Dietvorst BJ, Simmons JP, Massey C (2018) Overcoming algorithm aversion: People will use imperfect algorithms if they can (even slightly) modify them. Management Sci. 64(3):1155–1170.

Dolen WMV, Ruyter KD, Streukens S (2008) The effect of humor in electronic service encounters. J. Econom. Psych. 29(2):160–179.

Don A, Brennan S, Laurel B, Shneiderman B (1992) Anthropomorphism: from Eliza to Terminator 2. Bauersfeld P, Bennett JL, Lynch GF, eds. Proc. SIGCHI Conf. Human Factors Comput. Systems (Association for Computing Machinery, New York), 67–70.

Duffy BR (2003) Anthropomorphism and the social robot. Robotics Autonomous Systems 42(3–4):177–190.

Fernandes A (2017) Chatbots vs apps: The <sup>fi</sup>nal frontier. Chatbots Magazine (December 8), https://chatbotsmagazine.com/chatbotsvs-apps-the-<sup>fi</sup>nal-frontier-a0df10861c48.

Francis L, Monahan K, Berger C (1999) A laughing matter? The uses of humor in medical interactions. Motivation Emotion 23:155–174.

Frei E, Elias A, Wheeler C, Richardson P, Hryniuk W (1998) The relationship between high-dose treatment and combination chemotherapy: The concept of summation dose intensity. Clinical Cancer Res. 4(9):2027–2037.

Fussell SR, Kiesler S, Setlock LD, Yew V (2008) How people anthropomorphize robots. Fong T, Dautenhahn K, Scheutz M, Demiris Y, eds. Proc. 3rd Internat. Conf. Human Robot Interaction (HRI). (Association for Computing Machinery, New York).

Gefen D, Straub DW (2003) Managing user trust in B2C e-services. e-Service J. 2(2):7–24.

Gnewuch U, Morana S, Adam M, Maedche A (2018) Faster is not always better: Understanding the effect of dynamic response delays in human-chatbot interaction. Twenty-Sixth Eur. Conf. Inform. Systems, Portsmouth, UK.

Goetz J, Kiesler S, Powers A (2003) Matching robot appearance and behavior to tasks to improve human-robot cooperation. Proc. 12th IEEE Internat. Workshop Robot Human Interactive Comm. (IEEE, Piscataway, NJ), 55–60.

Guth W, Schmittberger R, Schwarze B (1982) An experimental anal- ¨ ysis of ultimatum bargaining. J. Econom. Behav. Organ. 3(4):367–388.

Guthrie SE (1995) Faces in the Clouds: A New Theory of Religion (Oxford University Press, New York).

Heider F, Simmel M (1944) An experimental study of apparent behavior. Amer. J. Psych. 57(2):243–259.

Holtgraves T (2013) Language as Social Action: Social Psychology and Language Use (Lawrence Erlbaum Associates, Mahwah, NJ).

Holtgraves T, Han TL (2007) A procedure for studying online conversational processing using a chat bot. Behav. Res. Methods 39(1):156–163.

Holtgraves T, Ross S, Weywadt C, Han T (2007) Perceiving arti<sup>fi</sup>cial social agents. Comput. Human Behav. 23(5):2163–2174.

Holzwarth M, Janiszewski C, Neumann MM (2006) The in<sup>fl</sup>uence of avatars on online consumer shopping behavior. J. Marketing 70(4):19–36.

Jain H, Padmanabhan B, Pavlou PA, Santanam RT (2018) Call for papers—Special issue of Information Systems Research—Humans, algorithms, and augmented intelligence: The future of work, organizations, and society. Inform. Systems Res. 29(1):250–251.

Kennedy JS (1992) The New Anthropomorphism (Cambridge University Press, New York).

Kiesler S, Siegel J, Mcguire TW (1984) Social psychological aspects of computer-mediated communication. Amer. Psych. 39(10):1123–1134.

Kiesler S, Sproull L, Waters K (1996) A prisoners dilemma experiment on cooperation with people and human-like computers. J. Personality Soc. Psych. 70(1):47–65.

Kiesler S, Powers A, Fussell SR, Torrey C (2008) Anthropomorphic interactions with a robot and robot-like agent. Soc. Cognition 26(2):169–181.

Kleinberg J, Lakkaraju H, Leskovec J, Ludwig J, Mullainathan S (2018) Human decisions and machine predictions. Quart. J. Econom. 133(1):237–293.

Liebman N, Gergle D (2016) It’s (not) simply a matter of time: The relationship between CMC cues and interpersonal af<sup>fi</sup>nity. Proc. 19th ACM Conf. Comput. Supported Cooperative Work Soc. Comput. (Association for Computing Machinery, New York), 570–581.

Logg JM, Minson JA, Moore DA (2019) Algorithm appreciation: People prefer algorithmic to human judgment. Organ. Behav. Human Decision Processes 151:90–103.

Luo X, Tong S, Fang Z, Qu Z (2019) Frontiers: Machines vs. humans: The impact of arti<sup>fi</sup>cial intelligence chatbot disclosure on customer purchases. Marketing Sci. 38(6):937–947.

Malle BF, Pearce GE (2001) Attention to behavioral events during interaction: Two actor-observer gaps and three attempts to close them. J. Personality Soc. Psych. 81(2):278–294.

Malone PB (1980) Humor: A double-edged tool for today’s managers? Acad. Management Rev. 5(3):357–360.

Mann HB, Whitney DR (1947) On a test of whether one of two random variables is stochastically larger than the other. Ann. Math. Statist. 18(1):50–60.

Mathur MB, Reichling DB (2016) Navigating a social world with robot partners: A quantitative cartography of the uncanny valley. Cognition 146:22–32.

McKendrick J (2018) Arti<sup>fi</sup>cial intelligence isn’t killing jobs; it’s killing business models. Forbes (January 25), https://www.forbes. com/sites/joemckendrick/2018/01/25/arti<sup>fi</sup>cial-intelligence-isntkilling-jobs-its-killing-business-models/?sh=736be6315ea0.

Meuter ML, Ostrom AL, Roundtree RI, Bitner MJ (2000) Self-service technologies: Understanding customer satisfaction with technology-based service encounters. J. Marketing 64(3):50–64.

Mone G (2016) The edge of the uncanny. Comm. ACM 59(9):17–19.

Moon Y (1999) The effects of physical distance and response latency on persuasion in computer-mediated communication and human–computer communication. J. Experiment. Psych. Appl. 5(4):379–392.

Moon Y (2000) Intimate exchanges: Using computers to elicit self disclosure from consumers. J. Consumer Res. 26(4):323–339.

Moretti L, Pellegrino GD (2010) Disgust selectively modulates reciprocal fairness in economic interactions. Emotion 10(2):169–180.

Morkes J, Kernal HK, Nass C (1999) Effects of humor in task-oriented human-computer interaction and computer-mediated communication: A direct test of SRCT theory. Human–Comput. Interaction 14(4):395–435.

Mott¨ onen T, Hannonen P, Leirisalo-Repo M, Nissil¨ a M, Kautiainen¨ H, Korpela M, Laasonen L, et al (1999) Comparison of combination therapy with single-drug therapy in early rheumatoid arthritis: A randomised trial. Lancet 353(9164):1568–1573.

Nass C, Lee KM (2001) Does computer-synthesized speech manifest personality? Experimental tests of recognition, similarityattraction, and consistency-attraction. J. Experiment. Psych Appl 7(3):171–181.

Nass C, Moon Y (2000) Machines and mindlessness: Social responses to computers. J. Soc. Issues 56(1):81–103.

Nass C, Steuer J, Tauber ER (1994) Computers are social actors. Adelson B, Dumais ST, Olson J, eds. Conf. Companion Human Factors Comput. Systems (CHI) (Association for Computing Machinery, New York), 72–78.

National Law Review (2019) Get all of your bots in a row: 2018 California bot disclosure law comes online soon. (June 7), https:// www.natlawreview.com/article/get-all-your-bots-row-2018- california-bot-disclosure-law-comes-online-soon.

Niculescu A, Dijk BV, Nijholt A, Li H, See SL (2013) Making social robots more attractive: The effects of voice pitch, humor and empathy. Internat. J. Soc. Robotics 5(2):171–191.

Nowak KL, Biocca F (2003) The effect of the agency and anthropomorphism on users sense of telepresence, copresence, and social presence in virtual environments. Presence Teleoperators Virtual Environments 12(5):481–494.

Oliver RL (1977) Effect of expectation and discon<sup>fi</sup>rmation on postexposure product evaluations: An alternative interpretation. J. Appl. Psych. 62(4):480–486.

Powers A, Kiesler S (2006) The advisor robot. Goodrich MA, Schultz AC, Bruemmer Dj, eds. Proc. 1st ACM SIGCHI/SIGART Conf. Human Robot Interaction (HRI) (Association for Computing Machinery, New York).

Sah YJ, Peng W (2015) Effects of visual and linguistic anthropomorphic cues on social perception, self-awareness, and information disclosure in a health website. Comput. Human Behav. 45:392–401.

Sanfey AG, Rilling JK, Aronson JA, Nystrom LE, Cohen JD (2003) The neural basis of economic decision-making in the ultimatum game. Sci. 300(5626):1755–1758.

Sproull L, Subramani M, Kiesler S, Walker J, Waters K (1996) When the interface is a face. Human Comput. Interaction 11(2):97–124.

Sun L (2107) Facebook Inc's chatbots hit a 70% failure rate. Motley Fool (February 28), https://www.fool.com/investing/2017/02 28/facebook-incs-chatbots-hit-a-70-failure-rate.aspx.

Tambe P, Cappelli P, Yakubovich V (2019) Arti<sup>fi</sup>cial intelligence in human resources management: Challenges and a path forward. California Management Rev. 61(4):15–42.

Taylor S (1994) Waiting for service: The relationship between delays and evaluations of service. J. Marketing 58(2):56–69.

Torta E, Dijk EV, Ruijten PAM, Cuijpers RH (2013) The ultimatum game as measurement tool for anthropomorphism in human–- robot interaction. Herrmann G, Pearson MJ, Lenz A, Bremner P, Spiers A, Leonards U, eds. Social Robotics Lecture Notes in Computer Science, (Springer International Publishing, Switzerland), 209–217.

Verhagen T, Nes JV, Feldberg F, Dolen WV (2014) Virtual customer service agents: Using social presence and personalization to

shape online service encounters. J. Comput. Mediated Comm. 19(3):529–545.

Walther JB (1992) Interpersonal effects in computer-mediated interaction. Comm. Res. 19(1):52–90.

Walther JB, Tidwell LC (1995) Nonverbal cues in computer mediated communication, and the effect of chronemics on relational communication. J. Organ. Comput. 5(4):355–378.

Wang LC, Baker J, Wagner JA, Wake<sup>fi</sup>eld K (2007a) Can a retail website be social? J. Marketing 71(3):143–157.

Wang FY, Carley KM, Zeng D, Mao W (2007b) Social computing: From social informatics to social intelligence. IEEE Intelligent Systems 22(2):79–83.

Weiss A, Bartneck C (2015) Meta analysis of the usage of the Godspeed questionnaire series. 2015 24th IEEE Internat. Sympos. Robot Human Interactive Comm. (RO-MAN), Kobe, Japan, 381–388.

Wilson H, Daugherty P, Bianzino N (2017) When AI becomes the new face of your brand. Harvard Bus. Rev. (June 27), https:// hbr.org/2017/06/when-ai-becomes-the-new-face-of-your-brand.

Wirtz J, Patterson PG, Kunz WH, Gruber T, Lu VN, Paluch S, Martins A (2018) Brave new world: Service robots in the frontline. J. Service Management 29(5):907–931.

Xu K, Lombard M (2017) Persuasive computing: Feeling peer pressure from multiple computer agents. Comput. Human Behav. 74:152–162.

C<sub>opy</sub>ri<sub>g</sub>ht 202 1 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>express wr</sub>itt<sub>en perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
