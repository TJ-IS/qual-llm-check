---
otero_id: 14882
otero_key: "3WJA55BY"
title: "Let's Shop Online Together: An Empirical Investigation of Collaborative Online Shopping Support"
authors: "Lei Zhu; Izak Benbasat; Zhenhui Jiang"
year: "2010"
journal: "Information Systems Research"
doi: "10.1287/isre.1080.0218"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/3WJA55BY/fulltext/images/27d3245dd300aff3eaa97bec01622b0cc5920f0eaa26e8ca28a3a40f15a1daa6.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Let's Shop Online Together: An Empirical Investigation of Collaborative Online Shopping Support

Lei Zhu, Izak Benbasat, Zhenhui Jiang,

## To cite this article:

Lei Zhu, Izak Benbasat, Zhenhui Jiang, (2010) Let's Shop Online Together: An Empirical Investigation of Collaborative Online Shopping Support. Information Systems Research 21(4):872-891. http://dx.doi.org/10.1287/isre.1080.0218

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2010, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/3WJA55BY/fulltext/images/c783ec5d0bb848c74e917ec610b98671c9215328f1b302d53db21f9d9ea59c7f.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Let’s Shop Online Together: An Empirical Investigation of Collaborative Online Shopping Support

Lei Zhu, Izak Benbasat

Sauder School of Business, University of British Columbia, Vancouver, British Columbia V6T 1Z2, Canada {leizhumis@gmail.com, izak.benbasat@sauder.ubc.ca}

Zhenhui Jiang

School of Computing, National University of Singapore, Singapore 117417, Republic of Singapore, jiang@comp.nus.edu.sg

rior studies investigating business-to-consumer e-commerce have focused predominantly on online shopping by individuals on their own, although consumers often desire to conduct their shopping activities with others. This study explores the important, but seldom studied, topic of collaborative online shopping. It investigates two design components that are pertinent to collaborative online shopping support tools, namely, navigation support and communication support. Results from a laboratory experiment indicate that compared to separate navigation, shared navigation effectively reduces uncoupling (i.e., the loss of coordination with one’s shopping partner) incidents per product discussed and leads to fewer communication exchanges dedicated to resolving each uncoupling incident, thereby enhancing coordination performance. Compared to text chat, voice chat does not help reduce the occurrence of uncoupling, but likely increases the efficiency in resolving uncou pling. The results further show that shared navigation and voice chat can significantly enhance the collaborative shoppers’ perceptions of social presence derived from their online shopping experiences. The interaction effect on social presence implies that the benefit of shared navigation is higher in the presence of text chat than in the presence of voice chat.

Key words: collaborative online shopping; shared navigation; common ground; media richness; uncoupling; social presence; electronic commerce

History: Laurie Kirsch, Senior Editor; Dennis Galetta, Associate Editor. This paper was received on May 28, 2006, and was with the authors 17 months for 3 revisions. Published online in Articles in Advance May 12, 2009.

## 1. Introduction

Shopping is often a social process in which a shopper is accompanied by friends or family members (Evans et al. 1996). Tauber (1972) has argued that one of the prime motives for shopping is the desire to communicate with others who have similar interests, to share ideas about particular products with shopping companions, to seek their feedback, and to enjoy leisure time with friends and family. Nevertheless, it is sometimes difficult to shop together simply because of physical separation, e.g., two friends may reside in different cities. Fortunately, this constraint may be alleviated by online shopping, because in a virtual shopping mall friends need not be collocated.

The need for social online shopping support is evident from prior studies (e.g., Tractinsky and Rao 2001). A survey by Jupiter Communications has found that 90% of online customers prefer some sort of human contact when they are conducting online transactions (Gutzman 2000). Correspondingly, Rayport and Jaworski (2001) have suggested that the capacity for online consumers to communicate with one another is critical to the success of Web stores.

In this study, we use the term collaborative online shopping to describe the activity in which a consumer shops at an online store concurrently with one or more remotely located shopping partners. Multiple techniques can be integrated to create a collaborative online shopping experience. For example, Landsend.com has deployed a feature called “shop with a friend<sup>™</sup>” that provides support for consumers at different locations to synchronize their Web navigation and to communicate online using text. These instant interaction functionalities have been acknowledged by practitioners to bolster a company’s Internet sales (Dukcevich 2002).

Indeed, technology-mediated person-to-person communication in organizational environments has been a subject of academic research for several decades (Short et al. 1976). For example, studies have investigated how people work collaboratively with the support of groupware technologies, such as e-mail, bulletin boards, group schedules, group support systems, workflow systems, and collaborative authoring tools (Ishii et al. 1994, Kayworth and Leidner 2002, Limayem and DeSanctis 2000). Additionally, a large number of empirical studies have compared computer-mediated communications to face-to-face interactions (Bordia 1997, Hoffman and Novak 1996). However, to date there has been little research attention paid to the phenomenon of collaboration in online shopping with new IT-enabled features, such as synchronized navigation and instant communication. Because of the lack of knowledge of these emerging collaborative technologies, as well as the social nature of online shopping, it may be presumptuous to apply the previous findings on the use and impact of collaborative technologies in working environments to an online shopping context. Therefore, additional research effort is needed to analyze and evaluate collaborative online shopping technologies theoretically and empirically to advance the IS knowledge concerning this important and expanding buying channel.

To address this deficiency, the present study investigates the design of a collaborative online shopping support tool by identifying its two primary features, namely, navigation support and communication support. These two features are related to the two fundamental processes of collaborative online shopping, i.e., to help shopping companions navigate to a particular product of potential interest and to allow for the exchange of ideas or opinions about that product. More specifically, this study evaluates the influence of different design choices for collaborative online shopping tools on shoppers coordination performance and their perceptions of social presence. Coordination performance reflects the utilitarian perspective when shoppers coordinate their product search and evaluation processes, whereas social presence represents the social perspective, i.e., the relational nature of collaboration that is exemplified by the feeling of intimacy and warmth (Kumar and Benbasat 2006). Both perspectives are relevant and complement each other, because the goal of collaborative online shopping is not only to assist a shopper in navigating to the right product to seek his companions’ opinions and suggestions, but also to fulfill his desire to interact with others and socialize with them (Tauber 1972). To the best of our knowledge, this study is among the first in the IS literature to evaluate the effectiveness of different techniques for collaborative online shopping.

This paper is organized as follows. The next section reviews previous literature and discusses the theoretical foundations. Section 3 identifies the two key technological components for designing collaborative online shopping. A research model is then developed in §4. The experimental research method used in the present study is described in §5. Section 6 discusses data analysis procedure and corresponding results. The final section concludes with the findings, contributions, and limitations of the study.

## 2. Theoretical Foundations

## 2.1. Collaborative Work

Collaborative technologies, such as e-mail, group support systems, and video conferencing, are used by members of groups or organizations to communicate with one another and coordinate their activities to execute tasks (Carte and Chidambaram 2004). In general, collaborative technologies have been found to be useful in enhancing the effectiveness of team collaboration (Goodman and Darr 1998) in various contexts, such as distributed learning (Alavi et al. 2002), virtual communities (Bieber et al. 2002), and system/product development (Scott 2000). For example, Easley et al. (2003) found that the use of collaborative systems could significantly increase creative performance for team-based work. Banker et al. (2006) found that the implementation of collaborative product design could improve product quality, reduce design cycle time, and lower product development costs. Similarly, Gallupe et al. (1992) compared electronic brainstorming with traditional verbal brainstorming and found group members to be more satisfied with the former.

Prior studies have also revealed that the processes of collaboration encompass both the detection and resolution of conflicts arising from collaboration (Chu-Carroll and Carberry 2000) as well as the facilitation of social awareness among team members (Burke 2001, Carroll et al. 2003). Therefore, two relevant theories on common ground and media richness are discussed below to provide the theoretical foundations for the design of collaborative online shopping tools.

## 2.2. Common Ground Theory

Research on situated cognition theorizes that people’s learning and cognition are highly dependent on the contexts in which learning and cognition take place (Lave 1988, Lave and Wenger 1990). For collocated collaborative work, collaborators share the same working environment and are exposed to the same contextual cues; hence, they are likely to be aware of one another’s concerns, opinions, and comments and to reach unanimity through this mutual awareness, thereby improving productivity (Olson and Olson 2000). In contrast, in distant collaboration, one person often fails to anticipate which features of his local context differ significantly from those of his remote partner, thereby leading to misunderstanding between the two (Cramton 2002). In both cases, the key to successful collaboration is whether collaborators can establish common ground, defined as the knowledge held in common by the collaborators, combined with their awareness that they have the knowledge in common (Clark and Brennan 1991, Olson and Olson 2000).

Common ground is considered to be vital for effective communication among collaborators, because it provides them with a shared referential base for discussion and ensures that the knowledge transferred connotes the same meaning for both the sender and the receiver (Clark 1996, Cramton 2002, Hanna et al. 2003). In contrast, without common ground, people speak and understand things that are communicated on the basis of their own information and interpretations of the situation, at times assuming incorrectly that the other speaks and understands on the basis of the same information and interpretations. In an ethnographic study, for example, Bechky (2003) observed how engineers, technicians, and assemblers on a product floor resolved misunderstandings among one another. He found that members of these communities overcame misunderstandings by cocreating common ground, which transformed their understanding of products and production processes. He also observed that verbal explanations alone did not suffice to create common ground. Instead, members used demonstrations with tangible and visible representations to establish common ground.

Based on these findings, it can be inferred that common ground could be useful in helping collaborative shoppers to coordinate their behavior; and that common ground could be established by showing the same Web contents to both participants simultaneously.

## 2.3. Media Richness Theory

Media richness theory is used to characterize a medium’s ability to change understanding within a specific time interval (Daft and Lengel 1986, Daft et al. 1987). According to the theory, the richness of media can be evaluated based on four criteria, namely, the ability of a medium to transmit multiple cues, allow for immediacy of feedback, support language variety, and provide personal focus. Based on these criteria, Daft and his colleagues propose that media can be ranked along a “media richness continuum” ranging from very rich to very lean. Face-to-face communication is considered to be the richest communication medium, followed by telephone, handwritten notes, addressed documents, and unaddressed documents.

Media richness theory divides information processes into two categories: reducing uncertainty (i.e., overcoming the absence of information) and lowering equivocality (i.e., removing ambiguity). Uncertainty can be reduced by supplying more relevant information, whereas equivocality can be lowered by using richer media. For example, in the context of interpersonal collaboration to interpret and resolve cognitively conflicting situations, richer media are often preferred and used by managers, as compared to lean media (Daft and Lengel 1986). Carlson and Davis (1998) have thus suggested that media richness is closely tied to people’s social communication, interpretation, and gain of consensus. Canessa and Riolo (2003) further noted that “if the intrinsic communication richness of the medium that members use is high, then the medium will effectively contribute to creating the overall shared meaning.”

The effects of richer media have been investigated in numerous studies. Kahai and Cooper (2003), for example, examined the effects of media richness on decision quality through three mediating constructs: social perception, message clarity, and the ability to evaluate others. In their study, subjects were asked to perform two tasks under conditions having different levels of media richness: face-to-face, electronic meetings, and electronic mail. Kahai and Cooper found that rich media enhanced social perception and increased individuals’ perceived ability to evaluate others. Complementing these findings, Kraut et al. (1992) investigated media choice in collaborative writing. They found that richer media (e.g., faceto-face interaction), as compared to leaner media (e.g., computer/phone and computer only), significantly alleviated coordination problems in collaborative writing, e.g., when people performed equivocal tasks such as planning and constructing a long document. The results also revealed that spoken annotations (i.e., voice) were preferred to, and were easier to use than, written annotations (i.e., text) when communicating complex and equivocal topics. Thus, their findings clearly support the media-task fit tenet proposed by media richness theory.

## 3. Support Technologies for Collaborative Online Shopping

Two facilitating mechanisms are important to designing an effective collaborative online shopping system. First, a well-designed collaborative online shopping interface should provide shoppers with a common context for product selection. More specifically, it should create a referential context that both shoppers can access and comment on, such as web pages that display products (Kraut et al. 2003). Without a common referential context, collaborative shopping is difficult because shoppers cannot ensure that their discussion refers to the same products or topics. Second, such a system must allow remote shoppers to engage in synchronous conversations, so that they can discuss products and services with each other, to share and exchange opinions.

Corresponding to these two mechanisms, a collaborative online shopping system can be designed using two types of technological support: navigation support and communication support.

## 3.1. Navigation Support

Navigation support determines how collaborative shopping companions navigate to the products of their interests. For example, if two people who are physically separated would like to shop for an item together on a website, they may first inform each other what website they will be visiting and what products they will be looking at. Next, the two shoppers need to navigate to the specific website and look for the products that they have agreed to explore. Here, the common website and products displayed that are visible to both parties serve as a referential context.

The two companions could conduct separate navigation, i.e., the paces of their navigation are independent and controlled by each individual. Alternatively, IT support, such as the shared navigation technique, enables two or more people to synchronously view the same Web pages through their individual Web browsers (Twidale 1995). Either one of the two shoppers, but only one at a time, can control what appears in both of their browsers, including the Web page content, navigation, and even mouse movement. In other words, shared navigation enforces synchronized browsing behavior. Similar applications can be found in work-related contexts, e.g., library representatives assist customers in finding the resources that they are looking for (Zou 2006); lecturers control the Web pages displayed on audiences’ monitors (Marais and Bharat 1997, Puglia et al. 2000).

## 3.2. Communication Support

Communication support ensures that shopping partners can communicate to share their interests, observations, and suggestions instantly. Two types of Web-based instant communication support, i.e., text chat and voice chat, are investigated in the present study. Both instant text chat and voice chat facilitate real-time communication between two users via the Internet. In text mode, text submitted via a chat window by one user appears instantly on another user’s computer screen. Voice chat uses Voice over Internet Protocol (VoIP) technologies to facilitate voice calls over the Internet instead of the traditional telephone landline system.

Figure 1 Research Model  
![](/api/attachments/3WJA55BY/fulltext/images/536a99073f9816252280b65544c30d3528b6e6b56b92ac090b132dff9094d6eb.jpg)

## 4. Research Model and Hypothesis Development

## 4.1. Overview

Prior research has suggested that collaboration involves action awareness and social awareness between collaborators (Carroll et al. 2003). Correspondingly, the present study investigates the impact of navigation support and communication support on the coordination performance of online shopping companions as a group and their perceptions of social presence (Figure 1). Two types of navigation support are studied, i.e., separate navigation versus shared navigation, together with two types of communication support, i.e., text chat versus voice chat.

## 4.2. Hypothesis Development

4.2.1. Dependent Variable: Coordination Performance. O’Keefe and McEachern (1998) have noted that an important stage for Web-based customer decision making is information search. For collaborative online shopping, because information search is a task performed jointly by both parties, it is not uncommon that conflicts may occur when the two shoppers follow divergent product search paths at times, thus leading to their actions interfering with each other (Shen et al. 2002). Therefore, the key to successful collaborative information search is to coordinate shopping companions’ browsing actions so as to accurately and efficiently locate product information of common interest (Diamadis and Polyzos 2004). If there is a lack of smooth coordination, one cannot easily locate and examine the product that his companion is commenting on; consequently, the primary purpose of collaborative online shopping cannot be achieved.

In this paper, we use the term uncoupling to describe the state in which collaborative shoppers lose coordination with their shopping companions. As such, to improve collaborative online shopping, shoppers require a collaborative technology that helps them (1) reduce the occurrence of uncoupling; and (2) facilitate the resolution of uncoupling.

One factor relevant to the extent of uncoupling is the number of uncoupling incidents that occur in a shopping task. Furthermore, in view of the previous findings that it is easier and faster to speak than to type (Kinney and Watson 1992, Walther 1992, Williams 1977), it is likely that collaborative shoppers discuss more products using voice than using text.<sup>1</sup> Discussing and exchanging opinions on more products implies that shoppers can perform a more thorough examination of displayed product alternatives, thereby potentially leading to a more-informed product decision (O’Keefe and McEachern 1998). On the other hand, the fact that more products are being discussed may increase the number of uncoupling incidents in collaborative shoppers’ communication. Therefore, to alleviate this confounding effect, it was decided to calculate the occurrence of uncoupling by dividing the number of uncoupling incidents by the number of products that were discussed in a shopping task, thus representing the average number of uncoupling incidents per product discussed.

On the other hand, when uncoupling occurs, collaborative shoppers usually resolve uncoupling by informing their partners of the product or the web page that they are looking at as well as their navigation intentions to coordinate their collaborative behavior. Hence, the extent to which a collaborative technology facilitates the resolution of uncoupling is calculated by dividing the number of communication exchanges dedicated to resolving uncoupling by the total number of uncoupling incidents that occur in a particular shopping task. In short, it refers to the average number of communication exchanges used to resolve each uncoupling incident.

4.2.2. Effects of Navigation and Communication Support on Coordination Performance. Uncoupling can occur in both separate and shared navigation conditions. With separate navigation, shopping partners<sup>2</sup> work with their own individual displays of the Web pages (a privileged ground situation, see Hanna et al. 2003). In such circumstances, it is likely that one shopper might assume incorrectly that the other is speaking about and understanding the situation on the basis of the first shopper’s privileged ground. Consequently, uncoupling incidents may occur because they cannot easily locate the same Web page or because they do not refer to the same product on a particular Web page. Furthermore, because of the lack of visible common ground, shoppers with separate navigation cannot resolve an uncoupling incident easily, but have to inform each other of their current location and the product that they are looking at, and, based on that, align their navigation with each other.

Uncoupling may occur in the shared navigation condition when both parties do not refer to the same product despite being on the same Web page. In addition, uncoupling can also be caused by poor coordination. For example, because two browsers are strictly synchronized, one’s full control over his own preferred way of navigation may be interfered with or infringed on by his companion’s unannounced act of moving to a different page. For example, assume that both shoppers are looking at the same screen. Whereas shopper A is focusing on examining product X, shopper B decides to navigate to a different Web page. Therefore, shopper A may get confused by shopper B’s unannounced act and thus suffer from the loss of coordination. Hence, if appropriate coordination is not developed, such interference leads to the unwanted outcome of disrupting one’s natural cognitive flow in product examination and increases the chance of loss of coordination with his companion.<sup>3</sup>

In terms of overall coordination performance, the use of shared navigation is likely to alleviate the occurrence of uncoupling as compared to the use of separate navigation. Shared navigation allows people to view the same Web pages synchronously and to share their navigation. These shared visual and behavioral cues enhance both shoppers’ awareness of each other’s situations and their common ground (Kraut et al. 2003). Specifically, shared navigation enforces a temporal and spatial match between the information accessed by both shoppers, which enables them to understand each other’s contextual cues concurrently and is thus likely to reduce the occurrence of uncoupling. In addition, once uncoupling occurs, shared navigation facilitates the resolution of uncoupling by allowing shoppers to consciously rely on synchronized page navigation and to use pointing devices to show others the item one is looking at.

Because shared navigation helps establish better common ground between the two shoppers than separate navigation, we posit:

Hypothesis 1A (H1A). Compared to separate navigation, shared navigation reduces the number of uncoupling incidents per product discussed.

Hypothesis 1B (H1B). Compared to separate navigation, shared navigation leads to fewer communication exchanges used to resolve each uncoupling incident.

Media richness theory suggests that voice-based communication is ranked higher than text-based communication along the media richness continuum (Daft and Lengel 1986). This is because voice can deliver multiple cues beyond text. People can use their voices to emphasize important points, to reveal doubt or uncertainty, to display acceptance, to invoke dominance, and for other purposes, through nonverbal cues such as inflection, pitch, tone, and pauses (Williams and Cothrel 2000). Specifically, media richness theory also suggests media-task fit (McGrath and Hollingshead 1993), i.e., a task is most effectively performed in the “best-fitting” communication environment. In particular, equivocal messages are better communicated using rich media than lean media. This tenet was tested by Kraut et al. (1992), who found that in highly equivocal tasks such as collaborative writing, rich media led to better performance and fewer coordination problems than lean media.

With separate navigation, a coordination task requires collaborative shoppers to explicitly inform each other of the specific products that they are commenting on. Hence, it is necessary to convey information about product location, which often involves contextual information such as screen displays, landmarks, layout, and even salient product characteristics. Such information is usually difficult to describe clearly, leading to ambiguity and conflict in coordination (McGrath and Hollingshead 1993). Therefore, with separate navigation, the greater communicative needs and coordination difficulties make coordination tasks highly equivocal; consequently, voice is better than text in improving collaborative shoppers’ coordination performance. In contrast, with shared navigation, coordination tasks are minimally equivocal as collaborative shoppers are physically bound, i.e., are looking at the same screen, and can show each other a particular product by pointing their mice at the product. Therefore, the use of voice versus text is unlikely to cause significant differences in coordination performance. Thus, we predict the following interaction effects:

Hypothesis 2 (H2). There is an interaction effect between navigation support and communication support on the number of uncoupling incidents per product discussed, i.e., voice chat leads to fewer uncoupling incidents per product discussed than text chat in the separate navigation condition, but not in the shared navigation condition.

Hypothesis 3 (H3). There is an interaction effect between navigation support and communication support on the number of communication exchanges used to resolve each uncoupling incident, i.e., voice chat leads to fewer communication exchanges to resolve each uncoupling incident than text chat in the separate navigation condition, but not in the shared navigation condition.

4.2.3. Dependent Variable: Social Presence. Social presence refers to the degree to which a medium allows a user to establish personal connection with other users (Short et al. 1976). It represents the capability of a medium to allow a user to experience others as being psychologically present (Fulk et al. 1987). In general, social presence is found to be important in the context of task collaboration. Burke (2001), for example, argues that social presence is an important aspect of distant collaboration and that it is positively related to users’ participation in a learning environment because the lack of social cues may lead to feelings that the environment is cold and unfriendly. Other studies have also identified the important role of social presence in the context of Internet shopping. For example, Kumar and Benbasat (2006) indicate that social presence characterizes the relational nature of a shopping experience, thus complementing the utilitarian perspective. Gefen and Straub (2003) have found that social presence affects consumers’ trust, which in turn influences their purchase intentions. Because one of the main objectives of collaborative online shopping is to fulfill people’s desire for social interaction (Schubert 2000, Tauber 1972), social presence is particularly important in the present context.

4.2.4. Effects of Navigation and Communication Support on Social Presence. Compared to separate navigation, shared navigation enables both shoppers to view the same screen contents synchronously, thus generating a visible common ground. This experience where one can see his companion’s mouse movement and navigation process as well as examine the product or the Web page that his companion shows him, provokes their awareness of the common situation (Kraut et al. 2003) and is comparable to an instore social shopping experience where two shoppers jointly examine the same product (Jarvenpaa and Todd 1996–1997), thereby leading both shoppers to feel that they are together.

Hypothesis 4 (H4). Shared navigation generates higher social presence than separate navigation in collaborative online shopping.

Prior studies have found that media differing in richness affect the amount of social presence that communicators perceive (Burke and Chidambaram 1999, Chidambaram and Jones 1993, Yoo and Alavi 2001). In general, it is suggested that face-to-face interaction is ideal because it conveys not only verbal information, but also nonverbal information such as facial expression, tone, and gesture, which are, at times, important and even indispensable to revealing a communication stance (Chidambaram and Jones 1993). Similarly, because voice can deliver many nonverbal cues that cannot be communicated via text (Short et al. 1976), such as inflection, pitch, tone, and pauses, voice chat helps shoppers retain their habitual linguistic style and behavior, and hence is more natural and makes shopping companions feel socially closer to each other than text chat.

Hypothesis 5 (H5). Voice chat generates higher social presence than text chat in collaborative online shopping.

We also predict that the effect of navigation support on social presence may depend on the particular communication support technique used. In general, as discussed earlier, shared navigation is expected to lead to higher social presence than separate navigation because shoppers under shared navigation may sense each other’s mouse movement and navigation intention. However, these perceptions are relatively indirect because shoppers do not build substantial and direct interaction with each other; instead, they interact through manipulating the Web interface. On the other hand, voice chat, as compared to text chat, can significantly boost the feelings of social presence, because it provides a direct and substantial interaction between the two shoppers. Overall, the effect of communication support (voice versus text) is stronger, i.e., more salient, than the effect of navigation support (shared navigation versus separate navigation). Prior research has suggested that when people are presented with multiple stimulation cues, more-salient information cues play a disproportionately more important role than less-salient cues (Hutchinson and Alba 1991, McGill and Anand 1989). Therefore, although when text chat is used, shared navigation can lead to higher social presence than separate navigation, this increase may be less prominent when voice chat is used because the relatively less direct and less influential effect of shared navigation on social presence is overshadowed by the much stronger effect of voice.

Hypothesis 6 (H6). There is an interaction effect between navigation support and communication support on social presence, i.e., navigation support has a stronger effect in the text chat condition than in the voice chat condition.

## 5. Research Method

## 5.1. Experimental Design

A laboratory experiment with a mixed 2 × 2 design (Gravetter and Wallnau 2000, Sternthal and Craig 1982) was used to test the proposed hypotheses.<sup>4</sup> Navigation support was chosen as the between-subject factor (separate navigation versus shared navigation), and communication support as a within-group factor (text chat versus voice chat).

Two types of products—school bags and watches— were used to increase the generalizability and applicability of the potential findings. The two products were selected for this study for several reasons: (1) both products are social products, inasmuch as they are used in public settings and therefore serve to exhibit their owners’ tastes and values; (2) both contain a variety of attributes (e.g., functionality, look, and size) that can provoke discussion between two shopping partners; and (3) both products are gender-neutral products. Amazon.com was chosen as the experimental website because it provides a rich collection of school bags and watches (over 1,000 types of each product).

Four types of collaborative online shopping support were implemented using a Web collaboration tool, Microsoft MSN 8, which provides instant text/voice chat support, and shared/separate navigation support.

## 5.2. Experimental Procedures

Participants in this experiment were students from a public university. To ensure sufficient power of 0.8 with a medium effect size for a two-by-two mixed design, 128 participants (64 pairs) were recruited to participate in the final experiment.

Each person who volunteered was asked to invite a friend to participate, to emulate a real shopping situation. The pair was then randomly assigned to one of two experimental groups (separate versus shared navigation). Each participant was paid \$15 for participation. In addition, participants were told that they would have a one-in-four chance of receiving a \$60 bonus toward the purchase of the products they chose in the study.

Participants were randomly assigned the role of main buyer or opinion giver. They were placed in two separately located rooms equipped with computers and monitors of the same type. Each pair was then asked to perform two shopping tasks together with the goals of purchasing a school bag and a watch, respectively. Because communication support served as a within-subject factor, each pair would experience two different types of communication support, i.e., voice chat and text chat. The order of the two treatment conditions was counterbalanced across different groups. Similarly, the order in which participants shopped for the two products was controlled; i.e., half of the pairs purchased a watch for their first task and a school bag for their second task, and the product order was reversed for the other half of the participants. Upon completing each of the two shopping tasks, participants were asked to write down the product that they intended to purchase,<sup>5</sup> then to complete a questionnaire.

A pilot test with 32 subjects (16 pairs) was conducted prior to the main experiment to identify any problems that might occur. Subjects reported that it was difficult for them to answer survey questions, e.g., to judge the social presence derived from the shopping experience using a Likert scale. For example, some subjects tended to rate social presence rather highly because of the use of the normal individual shopping experience as a benchmark; whereas others evaluated social presence lower when they compared their experimental environment to physical collaborative shopping.

The problem identified suggested that subjects had not as yet accumulated a uniform experience with collaborative online shopping needed for them to form a mental reference benchmark to make their judgments. This observation is also consistent with Helson’s adaptation-level theory (Helson 1964), which suggests that people’s judgments are based on their past experiences, a context or background, and a stimulus. Because the objective of this study is to evaluate the effectiveness of different designs in the context of collaborative online shopping, it was decided to make the contextual cues more salient in the experimental and questionnaire design.

In fact, Hufnagel and Conca (1994) also noted the importance of contextual clarity in collecting user response data. They argued that “the likelihood of context-related errors and biases can be significantly reduced” by “specifying the population to which comparisons should be made” (p. 56). Accordingly, changes were made in the study’s design to provide subjects with a common reference framework or context. Specifically, in the main experiment, before subjects were exposed to their formal tasks, they were asked to perform a common task with the goal of purchasing T-shirts, under a base condition that used separate navigation support with text chat. Also, the questionnaire was adjusted to ask the subjects to compare the treatment condition they were assigned to with the base condition (see the appendix). The same design was used by Jiang and Benbasat (2005) and Kim and Benbasat (2006).

Two research assistants conducted the experiment, one with each subject in a separate room to provide assistance if needed. The assistants were also asked to unobtrusively monitor whether the participants used the tool properly. With the permission of participants, we recorded the entire experimental sessions, including the screen action and conversations between shoppers and their shopping partners, using Camtasia, a screen-capture software application. These screen files were viewed after each experiment. The review results as well as the research assistants’ observations indicated that the experimental manipulations were successful across all four conditions, i.e., all subjects used the collaborative support technologies that were assigned to their groups.

## 6. Data Analysis

## 6.1. Subject Demographics and Background Analysis

Among the 128 participants, 60 were females. The ages of the participants ranged from 17 to 33. They came from diverse academic backgrounds, such as science, arts, engineering, and business. Almost onethird (31%) had known their shopping partners for more than four years, 22% between two and four years, 20% between one and two years, and 27% less than one year.

No significant differences were found between subjects randomly assigned to each of the four experimental conditions with respect to age, gender, past Internet experience, the length of time shopping partners had known each other, sociability,<sup>6</sup> and social intimacy.<sup>7</sup> This evidence indicates that participants demographics were quite homogeneous across different conditions.

## 6.2. Measurement

Seven items to measure social presence were adapted from Short et al. (1976) (see the appendix). Because social presence was reported by both participants in each shopping pair, the data were averaged as an indicator of social presence for this dyad and used in later analysis.

The evaluation of navigation coordination performance encompasses the identification of uncoupling incidents. We noted that it was obtrusive to request participants to report the occurrence of uncoupling during their shopping experience because that would have distorted shoppers’ natural shopping behavior. We also noted that it was also impossible to accurately identify uncoupling incidents only based on reviewing the screen-capture files of subjects’ behavior because observers could not accurately gauge shoppers’ browsing and navigation intentions and therefore were unable to determine whether shoppers experienced any uncoupling. Hence, it was decided to judge the occurrence of uncoupling by reviewing shoppers’ conversations as transcripts of conversations can clearly show when people experience difficulties as well as how they coordinate.

Hence, shopping dyads’ conversation protocols were collected. Voice chat protocols were transcribed into text format and analyzed later, together with text chat protocols. Twenty-four thousand two hundered eighty-five communication exchanges were thus collected based on subjects’ conversations, in both voice and text.

Two graduate research assistants, who were not aware of the study’s purpose, were asked to go through all communication protocols and identify those incidents that evidenced the occurrence of uncoupling as well as subsequent communication exchanges dedicated to resolving these uncoupling incidents. When faced with difficulties in coding, the two judges were allowed to refer to the corresponding screen-capture files so as to better understand the context. To assess the reliability of coding and ensure the validity of the data analysis, Cohen’s Kappa was calculated to measure intercoder agreement (Todd and Benbasat 1987). The Kappa coefficient is 0.75, indicating substantial agreement between the two coders (Landis and Koch 1977). The differences were further resolved when compromise was reached between the two judges based on their follow-up discussion.

Below are a few conversational examples of uncoupling incidents:

Example 1 (Separate Navigation and Voice Chat Condition, in Collaborative Search for Bags):

Yeah. Oh, we have another CalPack 19 inches.

B: 19". Oh, okay. Where is it?

A: Multipockets. And it’s only \$30. \$30. And it has dual compartments.

B: Where ah? Where is it? Where is it?

A: It’s the next page. Second in the middle from the top.

B: Yeah?

A: It’s pretty good actually.

B: Oh, okay. This one. Yeah.

Example 2 (Shared Navigation and Voice Chat Condition; in Collaborative Search for Bags):

A: Ya, ok    Oh my goodness, do you see this Crumpler “wonder weenie” messenger bag? Oh, that’s horrible.

B: Which one? I don’t see it.

A: Wait    the page you’re on, the second row

B: The blue one?

A: No.

B: Ok, I see it. It’s only \$25.

Example 3 (Shared Navigation and Text Chat Condition; in Collaborative Search for Watches):

A: This one? It looks good.

B: Mm?

A: Where are we now? I am lost.

B: Hey, I clicked on the wrong spot and went into that company. I’m sorry. I should click the top one.

A: That’s ok. Let’s go back.

## 6.3. Preliminary Data Analysis

The two judges coded the products that were discussed during collaborative online shopping. Consistent with our prior expectation, voice chat leads to significantly more products being discussed than text chat does. Specifically, shopping dyads discussed 15.1 products per task on average when communicating via voice, as compared to 6.3 products per task when communicating via text $( p < 0 . 0 1 )$ . In contrast, navigation support did not make a difference in terms of the number of products on which collaborative shoppers exchanged ideas (p > 005).

Because communication support is the withinsubject factor, there is a potential task order effect (i.e., the order of text and voice chat tasks). Another concern pertaining to the internal validity of the experiment is the possible confounding effects of product type (i.e., watches versus bags) and product order (i.e., watches first and bags second versus bags first and watches second). A number of analyses of variance (ANOVA) were performed on the collected data by having these factors as covariates. Results show that none of these factors (i.e., task order, product type, or product order) affects any of the dependent variables (p > 005).

## 6.4. ANOVA Results

ANOVA was conducted to examine the effects of navigation support and communication support on coordination performance and social presence. Corresponding results are shown in Tables 1–6 and Figures 2–4.

In particular, Table 1 shows that the effect of navigation support on the number of uncoupling incidents per product discussed is significant, suggesting that shared navigation effectively reduces the occurrence of uncoupling per product discussed as compared to separate navigation. Therefore, H1A is supported. The main effect of communication support and the interaction effect are not significant, indicating that voice is not different from text in reducing the occurrence of uncoupling per product discussed, regardless of the particular navigation support mode used, thus failing to support H2.

Table 1 ANOVA Summary: The Number of Uncoupling Incidents per Product Discussed

<table><tr><td>Source</td><td>df</td><td>Mean square</td><td>F</td><td>Sig.</td></tr><tr><td colspan="5">Between-subjects</td></tr><tr><td>Navigation support</td><td>1</td><td>1.92</td><td>23.16</td><td>0.00</td></tr><tr><td colspan="5">Within-subjects</td></tr><tr><td>Communication support</td><td>1</td><td>0.29</td><td>2.43</td><td>0.15</td></tr><tr><td>Navigation support × Communication support</td><td>1</td><td>0.03</td><td>0.22</td><td>0.58</td></tr></table>

Table 3 indicates that navigation support has a significant main effect on the number of communication exchanges used to resolve each uncoupling incident, meaning that compared to separate navigation, shared navigation facilitates the resolution of uncoupling. Hence, H1B is supported. The absence of interaction effect suggests that the effect of communication support on the number of communication exchanges to resolve each uncoupling incident is not moderated by the type of navigation support. Thus, H3 is not supported. Furthermore, it is imperative to appropriately interpret the main effect of communication support. As Table 4 shows, both text and voice lead to a similar number of communication exchanges to resolve each uncoupling incident (5.47 versus 5.24, p > 005). However, given that it is much easier and faster to speak than to type (Kinney and Watson 1992, Walther 1992, Williams 1977), voice is likely to resolve uncoupling more efficiently than text.

Shared navigation and voice generate significantly higher social presence than separate navigation and text, respectively (see Table 5 and 6). Therefore, H4 and H5 are supported. In line with our prediction, the effect of navigation support is more prominent in the presence of text chat than in the presence of voice chat. In particular, when text chat is used, navigation support significantly boosts social presence (i.e., 0.17 for separate navigation versus 1.7 for shared navigation); when voice chat is used, navigation support can also increase social presence, but to a smaller extent (i.e., 2.9 for separate navigation versus 3.5 for shared navigation). Therefore, H6 is supported (p < 001).

Table 2 Descriptive Statistics: The Number of Uncoupling Incidents per Product Discussed

<table><tr><td></td><td>Text</td><td>Voice</td><td>Mean</td></tr><tr><td>Separate navigation</td><td>0.41</td><td>0.53</td><td>0.47</td></tr><tr><td>Shared navigation</td><td>0.19</td><td>0.25</td><td>0.22</td></tr><tr><td>Mean</td><td>0.30</td><td>0.39</td><td></td></tr></table>

Table 3 ANOVA Summary: The Number of Communication Exchanges Used to Resolve Each Uncoupling Incident

<table><tr><td>Source</td><td>df</td><td>Mean square</td><td>F</td><td>Sig.</td></tr><tr><td colspan="5">Between-subjects</td></tr><tr><td>Navigation support</td><td>1</td><td>46.64</td><td>3.92</td><td>0.05</td></tr><tr><td colspan="5">Within-subjects</td></tr><tr><td>Communication support</td><td>1</td><td>0.81</td><td>0.10</td><td>0.80</td></tr><tr><td>Navigation support × Communication support</td><td>1</td><td>5.23</td><td>0.64</td><td>0.47</td></tr></table>

## 6.5. Supplementary Analysis

Recall that when proposing H1A and H1B, we described how and why uncoupling may occur in both separate and shared navigation conditions. In this section, we explore in greater detail the formation of uncoupling. There are conceptually three major types of uncoupling: interscreen uncoupling, intrascreen focal uncoupling, and intrascreen navigational uncoupling.

Interscreen uncoupling occurs when both collaborative shoppers are not exposed to the same Web screen at the same time, and therefore, cannot accurately understand what product the other party is referring to (i.e., the absence of visual common ground). For example, if shopper A is looking at screen X and shopper B is looking at screen Y, interscreen uncoupling occurs when shopper A gets confused by shopper B’s comments on a product on screen Y (see Example 1 in §6.2).

Intrascreen focal uncoupling occurs when shoppers who are exposed to the same Web screen at the same time (i.e., with visual common ground) fail to properly coordinate their search for focal products. For example, shopper A is inspecting product P while shopper B is inspecting product Q, although both are on the same screen. Hence, shopper A has no idea about the product shopper B is referring to, and thus feels the loss of coordination (see Example 2 in §6.2).

Table 4 Descriptive Statistics: The Number of Communication Exchanges Used to Resolve Each Uncoupling Incident

<table><tr><td></td><td>Text</td><td>Voice</td><td>Mean</td></tr><tr><td>Separate navigation</td><td>6.04</td><td>6.38</td><td>6.21</td></tr><tr><td>Shared navigation</td><td>4.90</td><td>4.11</td><td>4.50</td></tr><tr><td>Mean</td><td>5.47</td><td>5.24</td><td></td></tr></table>

Table 5 ANOVA Summary: Social Presence

<table><tr><td>Source</td><td>df</td><td>Mean square</td><td>F</td><td>Sig.</td></tr><tr><td colspan="5">Between-subjects</td></tr><tr><td>Navigation support</td><td>1</td><td>39.46</td><td>34.82</td><td>0.000</td></tr><tr><td colspan="5">Within-subjects</td></tr><tr><td>Communication support</td><td>1</td><td>164.74</td><td>271.97</td><td>0.000</td></tr><tr><td>Navigation support × Communication support</td><td>1</td><td>6.16</td><td>10.16</td><td>0.002</td></tr></table>

Intrascreen navigational uncoupling occurs when a shopper’s action affects his companion’s product examination despite both looking at the same Web screen (i.e., with visual common ground). This typically happens in a shared navigation condition, where the navigation of both shoppers are strictly tied together, For example, shopper A may get confused by a sudden and unannounced navigation initiated by shopper B (see Example 3 in §6.2). Consequently, shopper B’s navigational action interrupts shopper A’s natural cognitive flow in product examination and increases the chances of loss of coordination.

Based on this categorization, intrascreen focal uncoupling may happen in both shared navigation and separate navigation. On the other hand, interscreen uncoupling will happen in separate navigation but not in shared navigation, where both shoppers always look at the same screen. In contrast, intrascreen navigational uncoupling will occur only in shared navigation but not in separate navigation, where both shoppers act freely on their own without interfering with each other. Specifically, our analysis of the

Table 6 Descriptive Statistics: Social Presence

<table><tr><td></td><td>Text</td><td>Voice</td><td>Mean</td></tr><tr><td>Separate navigation</td><td>0.17</td><td>2.87</td><td>1.52</td></tr><tr><td>Shared navigation</td><td>1.71</td><td>3.54</td><td>2.63</td></tr><tr><td>Mean</td><td>0.94</td><td>3.21</td><td></td></tr></table>

Figure 3  
Figure 2 Results on the Number of Uncoupling Incidents per Product Discussed  
![](/api/attachments/3WJA55BY/fulltext/images/e0086e852b90049df63e08d213214e178c6d0b1f3b00ca45a3c2dd437d30456d.jpg)  
conversation transcripts shows that separate navigation leads to 3.2 interscreen uncoupling incidents per shopping task as compared to, by definition, zero for shared navigation $( p < 0 . 0 1 )$ ). Shared navigation leads to 0.8 intrascreen navigational uncoupling incidents per shopping task as compared to zero for separate navigation $( p < 0 . 0 1 )$ . Results also show that navigation support does not impact intrascreen focal uncoupling, with 1.2 for separate navigation and 1.6 for shared navigation $( p > 0 . 1 ) .$ 8

## 7. Discussion and Concluding Remarks

## 7.1. Discussion of Results

The results show that shared navigation in general is superior to separate navigation in reducing the occurrence of uncoupling and facilitating the resolution of uncoupling. Although the overall results are consistent with common ground theory, the supplementary analysis reveals deeper insights about the formation of uncoupling and the specific applicability of the theory. It is observed that the difference between shared navigation and separate navigation in reducing uncoupling is more complex than what one might initially have expected. In particular, the overall beneficial effect of shared navigation derives mainly from its effect on eliminating interscreen uncoupling; in contrast and somewhat surprisingly, separate navigation is better to suppress intrascreen navigational uncoupling, and is not significantly different from shared navigation in terms of intrascreen focal uncoupling. Hence, although common ground theory plays a primary role in predicting overall uncoupling occurrences, coordination performance, such as the two types of intrascreen uncoupling, are also affected by the way in which collaborative shoppers manage and coordinate their product search and navigation intentions (Chu-Carroll and Carberry 2000). Therefore, an important research question is how to reduce the instances of intrascreen uncoupling to further enhance shared navigation. In the next section, we will provide several design suggestions that have the potential to do so and need to be assessed in future studies.

Results on the Number of Communication Exchanges Used to Resolve Each Uncoupling Incident  
![](/api/attachments/3WJA55BY/fulltext/images/01b1f48911478f55c05f9cb81692e7f2fe62d4e47fe58f179fad51277a996d52.jpg)

Prior to the experiment, we expected an interaction effect on coordination performance based on the media-task fit tenet suggested by Media Richness Theory (Daft and Lengel 1986, McGrath and Hollingshead 1993). In particular, we proposed that for separate navigation where coordination tasks become highly equivocal, voice would perform better than text; but for shared navigation, communication support would not make a difference. Indeed, our results have confirmed that separate navigation tasks are more equivocal than shared navigation tasks because more occurrence of uncoupling and greater communicative effort in resolving uncoupling were found in the separate navigation condition. However, contrary to the media-task fit tenet, the effects of communication support do not depend on navigation support.

In particular, we have found that, regardless of navigation support, voice is not significantly different from text, a leaner medium, in terms of the occurrence of uncoupling per product discussed. Nevertheless, once an uncoupling incident occurs, voice likely helps shoppers resolve the uncoupling more efficiently than text. The pattern of these findings is quite similar to Dennis and Kinney (1998), who found that matching media richness to task equivocality did not increase performance. They also found that compared to text-based computer-mediated communication (i.e., lean media), audio-video communication (i.e., richer media) was not different in terms of decision quality and consensus change, but improved decision efficiency significantly.

Hence, the results suggest that media richness theory (Daft and Lengel 1986, McGrath and Hollingshead 1993) does not hold in the context of collaborative online shopping. Indeed, some previous research argues that certain capabilities of new electronic media are not fully explained by media richness theory. For example, Dennis and Valacich (1999) have proposed a theory of media synchronicity that incorporates additional media characteristics to extend media richness theory. Rehearsability, for example, referring to the extent to which the media enables a sender to rehearse or fine-tune a message before sending it; and reprocessability, which is defined as the extent to which a message can be reexamined or processed again within the context of the communication event. Dennis and Valacich argue that text formats such as written mail and electronic mail are better than voice formats such as voice mail and telephone in allowing users to rehearse or fine-tune a message before sending it and to reexamine a message after receiving it. Therefore, in these aspects, text may help users better convey and understand contextual information in navigation coordination.

Figure 4 Results on Social Presence  
![](/api/attachments/3WJA55BY/fulltext/images/94c79ca052ba0c30ce18f4d8b3ed4abd5f0613313673ce8e7499d14891554640.jpg)

Furthermore, text is likely better than voice in terms of locating Web pages in URL navigation. For example, text chat makes it easier for one shopper to send text-based URL addresses to others through a text chat window using “copy and paste,” rather than trying to spell it out verbally. Indeed, we have examined experimental participants’ communication transcripts and identified the use of URLs in directing navigation. The results show that participants used URLs significantly more often in the text condition (2.59 per task) than in the voice condition (0.04 per task) (p < 005).

In summary, although voice is richer than text along the traditional media richness continuum, such as cue multiplicity and language variety, in the context of collaborative online shopping, text may also benefit from higher rehearsability, higher reprocessability, and better URL navigability. Consequently, as a trade-off, we did not find any difference between text and voice in terms of the occurrence of uncoupling per product discussed. On the other hand, when an uncoupling incident occurs, shoppers may focus their attention on resolving it, and thus be prudent in communicating with each other; therefore, the relative advantage of text as compared to voice on rehearsability and reprocessability may diminish. Also, the resolution of uncoupling often involves explaining detailed contextual information, which cannot be achieved simply by text-based URL navigation. Consequently, as to resolving uncoupling, the advantage of voice plays a primary role, leading to voice being more efficient than text.

Our results also show that shared navigation leads to higher social presence than separate navigation, thus lending further support to common ground theory. The visible browsing behavior of the other party and the awareness of the shared context (Kraut et al. 2003) enhance shoppers’ perceptions that their shopping companions are socially close to them. The superior effect of voice over text on social presence is also consistent with previous research that voice generally corresponds to higher social presence than text (Carlson and Davis 1998). The interaction effect between navigation support and communication support further implies that communication support (voice versus text) has a much stronger impact on social presence than navigation support (shared navigation versus separate navigation), as voice chat builds a direct connection between collaborative shoppers and therefore establishes much stronger social presence (Nass and Brave 2005).

Whereas coordination performance is on a dyadic level and calculated based on the activities of shopping pairs as a group, social presence is scored by both shoppers separately. This may raise a concern as to whether the roles of two shoppers in each dyad can moderate the effect of navigation support and communication support on social presence perceptions. In view of this, a follow-up analysis was conducted by treating shoppers’ roles (i.e., buyers or opinion givers) as a separate factor. Results show that the role of shoppers does not have a significant effect on social presence (p > 005), nor does it have any interaction effect with navigation support and communication support (p > 005). Therefore, the role of shoppers is not a confounding factor that affects our findings.

Furthermore, coordination performance and social presence only characterize two specific aspects of a collaborative shopping process. A natural question that might arise is what collaborative technologies are more likely to retain collaborative shoppers on a website. Reichheld and Schefter (2000), for example, have argued that a successful Web store needs to be sticky, that is, it should be able to hold online consumers’ interests and attention for long periods of time. Indeed, we measured collaborative shoppers’ intentions to continue collaborative shopping and investigated the effects of navigation support and communication support on continuance intentions.<sup>9</sup> It was found that both shared navigation and voice could significantly enhance shoppers’ continuance intentions to use collaborative online shopping, as compared to separate navigation and text, respectively, and that their interaction was not significant. Therefore, it seems that the combination of shared navigation and voice can best retain collaborative shoppers online.

## 7.2. Contributions

Social shopping with friends and family is an important part of daily shopping and, at times, a major motive for a consumer to visit a store (Tauber 1972, Zhu et al. 2006). For example, Shen et al. (2002) have argued that “shopping is an activity that is socially facilitated, meaning that when done in the company of others, people engage in it more” (p. 282). In fact, some early research effort has already been devoted to understanding how to facilitate online consumers collaboration indirectly. Schubert (2000), for instance, has proposed a participatory product catalog to allow customers to collaborate via a community knowledge repository. Diamadis and Polyzos (2004) contend that online customers’ collaborative search can be enhanced by relying on the interaction history information that is generated when browsing Web pages. Nevertheless, very few empirical studies have investigated the use of collaborative technologies, such as navigation support and communication support, to build direct connection among shopping companions. Therefore, in view of the rapid development in online collaborative technologies, it is paramount for researchers as well as practitioners to understand the design alternatives for collaborative online shopping as a new paradigm of e-commerce, and the impacts of collaborative technologies on collaborative shoppers behavior.

This study makes several contributions. First, it sheds light on designing collaborative online shopping by identifying its two technological components: navigation support and communication support. Second, it tests the effects of navigation support and communication support in a laboratory environment. Two perspectives are relevant to assessing collaborative online shopping tools: utilitarian and social. From a utilitarian perspective, successful collaborative online shopping depends on the actual performance of the coordination of a collaborative navigation process. In particular, we use the construct uncoupling to represent the status where collaborative partners lose coordination with each other. Complementing the utilitarian perspective, the social perspective concerns the degree of social presence that shoppers experience during their interaction with their companions. Prior research has suggested that shoppers engage in collaborative shopping not only for a second opinion toward a product, but also for the fulfillment of social interaction (Tauber 1972). For example, Schubert (2000) suggests that the invisibility of other customers exacerbates the feeling of aloneness. Hence, social presence, which characterizes a computer-mediated communication as warm and human, is used as a suitable indicator of social fulfillment.

Furthermore, coordination performance and social presence are measured using different methods. Whereas the former is measured based on the analysis of communication protocols, the latter is measured by eliciting perceptions via questionnaires. The use of different measuring techniques represents an effort to reduce common method bias (Podsakoff et al. 2003). In fact, our results show that the effects of navigation support and communication support on coordination performance and social presence do not parallel each other.

Previous studies on common ground theory and media richness theory have focused predominantly on organizational communication, particularly in working environments (Daft et al. 1987, Olson and Olson 2000). Compared to these prior endeavors, this study links the two theories to the two technological aspects of collaborative online shopping tools, i.e., navigation support and communication support. The experimental results provide considerable evidence for the applicability of common ground theory to collaborative online shopping, but are inconsistent with media richness theory in terms of explaining and predicting collaborative shoppers’ coordination performance. Our results have also echoed Dennis and Valacich’s (1999) call to examine other media characteristics that are not covered by media richness theory.

Our results suggest that, in general, the use of shared navigation is beneficial for collaborative coordination performance. However, we have observed that shared navigation has a double-edged effect on reducing different types of uncoupling incidents. Indeed, its overall beneficial effect is mainly because of its effect on suppressing interscreen uncoupling that is caused by collaborators’ not being at the same screen at the same time. However, compared to separate navigation, enforced shared navigation has a negative effect on intrascreen navigational uncoupling and does not appear to reduce intrascreen focal uncoupling. Therefore, a practical design implication to improve shared navigation is to support it with technologies that can allow collaborators to better understand each other’s product search and navigation intentions to reduce intrascreen uncoupling. For example, with the aid of eye-tracking technologies (Oyekoya and Stentiford 2006), a collaborative shopper could be made aware of the focal item that his shopping companion is examining on the same screen; hence, the two can better coordinate their product search and navigation pace to reduce intrascreen focal and navigational uncoupling. A similar, but less expensive, approach is to use an enhanced restricted focus viewer (ERFV), which makes everything blurry except the focal area around the cursor, to show the collaborators each other’s eye scan paths (Tarasewich and Fillion 2004). A third option is to provide a split screen, one allowing the shoppers to have shared navigation and the other separate navigation. This wil alleviate the problem of two shoppers being strictly tied together at all times (as in the case with shared navigation only). It will allow each shopper to conduct some independent searches on his own without interfering with the cognitive processing of his partner, while still having the option of getting back to a fully coordinated mode when the shopping partner so desires.

## 7.3. Limitations

This study is subject to several limitations. First, the effects of collaborative online shopping may depend on the type of products being evaluated. For example, Jahng et al. (2000, 2002, 2006) suggest that e-commerce interface characteristics must match product characteristics to yield the best consumer outcomes. In our experiment, subjects were asked to shop for watches and school bags. Our analysis has shown that the choice of either watches or bags does not make a difference in the results, thus lending confidence to the explanation of the effects of navigation and communication support. However, it is worth noting that both products contain many attributes that are likely to be judged based on individuals’ taste and preferences. Therefore, the evaluation of this type of product usually requires seeking a second opinion from other persons. In contrast, for simple products (e.g., groceries) or personal products (e.g., medicine or hygiene products), consumers may not want to share their consumption processes with other people, hence they may not benefit from shared navigation.

Furthermore, the effects of navigation support and communication support were investigated in a context where shoppers search and evaluate online products with friends. Therefore, we do not attempt to generalize the results to collaborative shopping between a shopper and a Web store sales representative. This is because the relationship between two friends is very different from that between a shopper and a sales person (Qiu and Benbasat 2005). Consumers shop with friends for social interaction and consultation without any compulsion to complete a purchase. In contrast, consumers generally communicate with sales persons purely for consultation, and they usually exercise caution because advice from the representative is likely biased toward a commission or profit for the store.

The study’s contributions may also be limited by using subject pairs to act as collaborative online shopping groups. It is natural that people tend to shop in groups with someone with whom they feel comfortable. In the advertisements for recruiting subjects, we asked each of our subjects to participate in the study with a friend with whom he or she would be willing to shop. However, the actual participants might not desire to be shopping buddies, but just convenient friends whose schedule could fit with each other’s to permit participation at the same time. In other words, participants’ relationships may not represent the relationships between typical shopping buddies. Thus, the generalizability of this study’s findings might be limited. Fortunately, our conversation analyses<sup>10</sup> have shown that subjects were generally happy with their shopping partners, therefore the above concern can be alleviated somewhat. Also, our data analysis indicates that the social intimacy<sup>11</sup> between the two participants of each pair has not affected our experiment results, providing additional evidence that our findings should be largely reliable.

## 7.4. Future Research

Although this study has found an overall benefit for shared navigation as compared to separate navigation, it has also revealed that shared navigation may lead to more intrascreen uncoupling incidents. Hence, future research could test the effects of the three designs proposed earlier in the contribution section, namely, the use of eye-tracking, ERFV, and split screens, on reducing intrascreen uncoupling. Furthermore, this study has examined the effects of collaborative support tools on collaborative shoppers’ coordination performance and their perceptions of social presence, but it is yet unknown whether the two types of technological support can improve the quality of consumers’ product decisions. It is possible that collaborative shoppers who can perform effective and efficient coordination and experience high social presence fail to reach an agreement on an optimal decision about product choice. For example, previous research (e.g., Heath and Gonzalez 1995) has found that social interaction forces people to explain their choices to others, thus increasing decision confidence; however, decision quality is not necessarily improved. Therefore, it would be interesting for future research to examine how navigation support and communication support can be designed to facilitate mutual agreement and optimize consumers’ purchase decisions.

## Acknowledgments

The authors thank the Social Sciences and Humanities Research Council of Canada (SSHRC) and the Ministry of Education (MOE) of Singapore for their support of this study. The authors also thank the senior editor, the associate editor, the three anonymous reviewers, and Sameh Al-Natour for their valuable comments on this paper, as well as Cheng Yi and Dong Zhang for their assistance in data analysis. The three authors have contributed equally to the paper.

## Appendix

The following questions ask you to compare the two collaborative online shopping experiences you have just experienced, and to indicate to what extent you prefer one or the other.

For example, three participants, named a, b, and c, have the following feeling toward the collaborative shopping tools they used:

Q: Which support tool did you find more attractive?

1. Person a found the FIRST collaborative shopping tool much more attractive;

2. Person b found both collaborative shopping tools equally attractive;

3. Person c found the SECOND collaborative shopping tool a little more attractive;

Their responses are shown below:

The First collaborative online shopping tool Equal The Second collaborative online shopping tool

![](/api/attachments/3WJA55BY/fulltext/images/37206a9a1346a80458b4c49e2b958f3a5bc7b738d872e66c0e008e0a75c0fdb9.jpg)

That is, person a would select 4 on the left, person b would select 0, while person c would select 2 on the right.

## Social Presence

The items used to assess social presence in this study are adapted from the scale used by Short et al. (1976).

SP1: Which collaborative online shopping experience gave you a stronger feeling that the interaction with your shopping partner was personal?

The First collaborative online shopping experience Equal The Second collaborative online shopping experience

<table><tr><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr></table>

SP2: Which collaborative online shopping experience made you feel warmer with the interaction with your shopping partner?

SP3: Which collaborative online shopping experience made you feel that the interaction with your shopping partner was closer?

SP4: Which collaborative online shopping experience made you have a feeling that the interaction with your shopping partner was more humanizing?

SP5: Which collaborative online shopping experience made you have a less strong feeling that the interaction with your shopping partner was expressive?

SP6: Which collaborative online shopping experience gave you a less strong feeling that the interaction with your shopping partner was emotional?

SP7: Which collaborative online shopping experience made you feel that the interaction with your shopping partner was more sensitive?

## References

Alavi, M., G. M. Marakas, Y. Yoo. 2002. A comparative study of distributed learning environments on learning outcomes. Inform. System Res. 13(4) 404–415.

Banker, R. D., I. Bardhan, O. Asdemir. 2006. Understanding the impact of collaboration software on product design and devel opment. Inform. Systems Res. 17(4) 352–373.

Bechky, B. A. 2003. Sharing meaning across occupational communities: The transformation of understanding on a production floor. Organ. Sci. 14(3) 312–330.

Bhattacherjee, A. 2001. Understanding information systems continuance: An expectation-confirmation model. MIS Quart. 25(3) 351-370.

Bieber, M., D. Engelbart, R. Furuta, S. R. Hiltz, J. Noll, J. Preece, B. V. D. Walle. 2002. Toward virtual community knowledge evolution. J. Management Inform. Systems 18(4) 11–35.

Bordia, P. 1997. The cyborg’s dillemma: Progressive embodiment in virtual environment. J. Bus. Comm. 34(1) 99–120.

Burke, J. A. 2001. Collaborative accounting problem solving via group support systems in a face-to-face versus distant learning environment. Inform. Tech. Learn. Performance J. 19(2) 1–19.

Burke, K., L. Chidambaram. 1999. How much bandwidth is enough? A longitudinal examination of media characteristics and group outcomes. MIS Quart. 23(4) 557–580.

Canessa, E., R. L. Riolo. 2003. The effect of organizational communication media on organizational culture and performance: An

agent-based simulation model. Comput. Math. Organ. Theory 9(2) 147–176.

Carlson, P. J., G. B. Davis. 1998. An investigation of media selection among directors and managers: From “self” to “other” orientation. MIS Quart. 22(3) 335–362.

Carroll, J. M., D. C. Neale, P. L. Isenhour, M. B. Rosson, D. S. McCrickard. 2003. Notification and awareness: Synchronizing task-oriented collaborative activity. Internat. J. Human-Comput. Stud. 58(5) 605–632.

Carte, T., L. Chidambaram. 2004. A capabilities-based theory of technology deployment in diverse teams: Leapfrogging the pitfalls of diversity and leveraging its potential with collaborative technology. J. Assoc. Inform. Systems 5(11–12) 448–471.

Chidambaram, L., B. Jones. 1993. Impact of communication medium and computer support on group perceptions and performance: A comparison of face-to-face and dispersed meetings. MIS Quart. 17(4) 465–491.

Chu-Carroll, J., S. Carberry. 2000. Conflict resolution in collaborative planning dialogs. Internat. J. Human-Comput. Stud. 53(6) 969–1015.

Clark, H. H. 1996. Using Language. Cambridge University Press, New York.

Clark, H. H., S. E. Brennan. 1991. Grounding the communication. S. D. Teasley, ed. Perspectives on Socially Shared Cognition. APA, Washington, DC, 127–149.

Cramton, C. D. 2002. Finding common ground in dispersed col laboration. Organ. Dynam. 30(4) 356–367.

Daft, R., R. Lengel. 1986. Organizational information requirements, media richness and structural design. Management Sci. 32 554–571.

Daft, R., R. Lengel, L. Trevino. 1987. Message equivocality, media selection, and manager performance: Implications for information systems. MIS Quart. 17 355–366.

Dennis, A. R., S. T. Kinney. 1998. Testing media richness theory in the new media: The effects of cues, feedback, and task equivocality. Inform. System Res. 9(3) 256–274.

Dennis, A. R., J. S. Valacich. 1999. Rethinking media richness: Towards a theory of media synchronicity. Proc. 32nd Hawaii Internat. Conf. System Sci., Maui, Hawaii.

Diamadis, E. T., G. C. Polyzos. 2004. Efficient cooperative searching on the Web: System design and evaluation. Internat. J. Human Comput. Stud. 61(5) 699–724.

Dukcevich, D. 2002. Lands’ End’s instant business. Available at http://www.forbes.com/2002/07/22/0722landsend.html, July 22.

Easley, R. F., S. Devaraj, J. M. Crant. 2003. Relating collaborative technology use to teamwork quality and performance: An empirical analysis. J. Management Inform. Systems 19(4) 247–268.

Eid, M., R. Riemann, A. Angleitner, B. Peter. 2003. Sociability and positive emotionality: Genetic and environmental contributions to the covariation between different facets of extraversion. J. Personality 71(3) 319–346.

Evans, K. R., T. Christiansen, J. D. Gill. 1996. The impact of social influence and role expectations on shopping center patronage intentions. J. Acad. Marketing Sci. 24(3) 208–218.

Fulk, J. W., S. C. Schmitz, G. J. Power. 1987. A social information processing model of media use in organizations. Comm. Res. 14(5) 520–552.

Gallupe, R. B., W. H. Cooper, M. L. Grise, L. M. Bastianutti. 1992. Electronic brainstorming and group size. Acad. Management J. 35(2) 350–369.

Gefen, D., D. Straub. 2003. Managing user trust in B2C e-services. e-Service J. 2(2) 7–24.

Goodman, P. S., E. D. Darr. 1998. Computer-aided systems and commuities: Mechanisms for organizational learning in distributed environments. MIS Quart. 22(4) 417–440.

Gravetter, F. J., L. B. Wallnau. 2000. Statistics for the Behavioral Sciences A First Course for Students of Psychology and Education. Wadsworth, Belmont, CA.

Gutzman, A. 2000. Real-time chat: What are you waiting for? (March 16), http://www.ecommerce-guide.com/solutions/ technology/article.php/322551.

Hanna, J. E., M. K. Tanenhaus, J. C. Trueswell. 2003. The effects of common ground and perspective on domains of referential interpretation. J. Memory Language 49(1) 43–61.

Heath, C., R. Gonzalez. 1995. Interaction with others increases decision confidence but not decision quality: Evidence against information collection views of interactive decision making. Organ. Behav. Human Decision Process 61(3) 305–326.

Helson, H. 1964. Adaptation-Level Theory. Harper & Row, New York.

Hoffman, D., T. Novak. 1996. Marketing in hypermedia computermediated environments: Conceptual foundations. J. Marketing Res. 60(3) 50–68.

Hufnagel, E. M., C. Conca. 1994. User response data: The potential for errors and biases. Inform. Systems Res. 5(1) 48–73.

Hutchinson, J. W., J. W. Alba. 1991. Ignoring irrelevant information: Situational determinants of consumer learning. J. Consumer Res. 18(3) 325–345.

Ishii, H., M. Kobayashi, K. Arita. 1994. Iterative design of seamless collaboration media. Comm. ACM 37(8) 83–90.

Jahng, J., H. Jain, K. Ramamurthy. 2000. Effective design of electronic commerce environments: A proposed theory of congruence and an illustration. IEEE Trans. Systems, Man, Cybernetics—Part A Systems and Humans 30(4) 456–471.

Jahng, J., H. Jain, K. Ramamurthy. 2002. Personality traits and effectiveness of presentation of product information in e-business systems. Eur. J. Inform. Systems 11(3) 181–195.

Jahng, J., H. Jain, K. Ramamurthy. 2006. An empirical study of the impact of product characteristics and electronic commerce interface richness on consumer attitude and purchase inten tions. IEEE Trans. Systems, Man, Cybernetics—Part A Systems and Humans 36(6) 1185–1201.

Jarvenpaa, S. L., P. A. Todd. 1996–1997. Consumer reactions to electronic shopping on the World Wide Web. Internat. J. Electronic Commerce 1(2) 59–88.

Jiang, Z., I. Benbasat. 2005. Virtual product experience: Effects of visual & functional control of products on perceived diagnosticity and flow in electronic shopping. J. Management Inform. Systems 21(3) 111–148.

Kahai, S. S., R. B. Cooper. 2003. Exploring the core concepts of media richness theory: The impact of cue multiplicity and feedback immediacy on decision quality. J. Management Inform. Systems 20(1) 263–299.

Kayworth, T. R., D. E. Leidner. 2002. Leadership effectiveness in global virtual teams. J. Management Inform. Systems 18(3) 7–41.

Kim, D., I. Benbasat. 2006. The effects of trust-assuring arguments on consumer trust in Internet stores: Application of Toulmin’s model of argumentation. Inform. Systems Res. 17(3) 286–300.

Kinney, S. T., R. T. Watson. 1992. The effect of medium and task on dyadic communication. Proc. Internat. Conf. Inform. Systems, Dallas, 107–117.

Kraut, R. E., S. R. Fussell, J. Siegel. 2003. Visual information as a conversational resource in collaborative physical tasks. Human-Comput. Interaction 18(1) 13–49.

Kraut, R. E., J. Galegher, R. S. Fish, B. Chalfonte. 1992. Task requirements and media choice in collaborative writing. Human Comput. Interaction 7(4) 375–407.

Kumar, N., I. Benbasat. 2006. The influence of recommendations and consumer reviews on evaluations of websites. Inform. Systems Res. 17(4) 425–439.

Landis, J. R., G. G. Koch. 1977. The measurement of observer agreement for categorical data. Biometrics 33(1) 159–174.

Lave, J. 1988. Cognition in Practice Mind, Mathematics, and Culturein Everyday Life. Cambridge University Press, Cambridge, UK.

Lave, J., E. Wenger. 1990. Situated Learning Legitimate Peripheral Participation. Cambridge University Press, Cambridge, UK.

Limayem, M., G. DeSanctis. 2000. Providing decisional guidance for multicriteria decision making in groups. Inform. System Res. 11(4) 386–401.

Marais, H., K. Bharat. 1997. Supporting cooperative and personal surfing with a desktop assistant. Proc. User Interface Software Tech. Conf., Banff, Alberta, Canada, 129–138.

McGill, A. L., P. Anand. 1989. The effect of vivid attributes on the evaluation of alternatives: The role of differential attention and cognitive elaboration. J. Consumer Res. 16(2) 188–196.

McGrath, J. E., A. B. Hollingshead. 1993. Putting the “group” back in group support systems: Some theoretical issues about dynamic processes in groups with technological enhancements. L. M. Jessup, J. S. Valacich, eds. Group Support Systems New Perspectives. Macmillan, New York, 78–96.

Miller, R. S., H. M. Lefcourt. 1982. The assessment of social intimacy. J. Personality Assessment 46(5) 514–518.

Nass, C., S. Brave. 2005. Wired for Speech How Voice Activates and Advances the Human-Computer Relationship. The MIT Press, Cambridge, MA.

O’Keefe, R. M., T. McEachern. 1998. Web-based customer decision support systems. Comm. ACM 41(3) 71–78.

Olson, G. M., J. S. Olson. 2000. Distance matters. Human Comput. Interaction 15(2) 139–178.

Oyekoya, O. K., F. W. M. Stentiford. 2006. Eye tracking—A new interface for visual exploration. BT Tech. J. 24(3) 57–66.

Podsakoff, P. M., S. B. MacKenzie, J.-Y. Lee, N. P. Podsakoff. 2003. Common method biases in behavioral research: A critical review of the literature and recommended remedies. J. Appl. Psych. 88(5) 879–903.

Puglia, S., C. Robert, R. Jain. 2000. MultECommerce: A distributed architecture for collaborative shopping on the WWW. Proc. EC’00, Minneapolis, 215–223.

Qiu, L., I. Benbasat. 2005. An investigation into the effects of textto-speech voice and 3D avatars on the perception of presence and flow of live help in electronic commerce. ACM Trans. Comput.-Human Interaction 12(4) 329–355.

Rayport, J., B. Jaworski. 2001. Introduction to E-Commerce. McGraw-Hill, New York.

Reichheld, F. F., P. Schefter. 2000. E-loyalty: Your secret weapon on the Web. Harvard Bus. Rev. 78(4) 105–113.

Schubert, P. 2000. The participatory electronic product catalog: Supporting customer collaboration in e-commerce applications. Electronic Markets 10(4) 229–236.

Scott, J. E. 2000. Facilitating interorganizational learning with information technology. J. Management Inform. Systems 17(2) 81–113.

Shen, X., T. Radakrishnan, N. D. Georganas. 2002. vCOM: Electronic commerce in a collaborative virtual world. Electronic Commerce Res. Appl. 1(3–4) 281–300.

Short, J., E. Williams, B. Christie. 1976. The Social Psychology of Telecommunications. Wiley, London.

Sternthal, B., C. S. Craig. 1982. Consumer Behavior-An Information Processing Perspective. Prentice-Hall, Englewood Cliffs, NJ.

Tarasewich, P., S. Fillion. 2004. Discount eye tracking: The enhanced restricted focus viewer. Proc. Tenth Americas Conf. Inform. Systems, New York.

Tauber, E. M. 1972. Why do people shop? J. Marketing 36(4) 46–49.

Todd, P., I. Benbasat. 1987. Processing tracing methods in decision support systems research: Exploring the black box. MIS Quart. 11(4) 493–512.

Tractinsky, N., V. S. Rao. 2001. Incorporating social dimensions in Web-store design. Human Systems Management 20(2) 105–121.

Twidale, M. 1995. How to study an design for collaborative browsing in the digital library. Proc. 37th Allerton Institute Graduate School of Library Inform. Sci., Monticello, IL.

Walther, J. B. 1992. Interpersonal effects in computer-mediated interaction. Comm. Res. 19(1) 52–90.

Williams, E. 1977. Experimental comparisons of face-to-face and mediated communication: A review. Psych. Bull. 84(5) 963–976.

Williams, R. L., J. Cothrel. 2000. Four smart ways to run online communities. Sloan Management Rev. 41(4) 81–91.

Yoo, Y., M. Alavi. 2001. Media and group cohesion: Relative influences on social presence, task participation, and group consensus. MIS Quart. 25(3) 371–391.

Zhu, L., I. Benbasat, Z. Jiang. 2006. Investigating the role of presence in collaborative online shopping. Proc. Twelfth Americas Conference on Information Systems, Acapulco, NM, 2952–2962.

Zou, S. 2006. A dyadic analysis of media synchronicity and task type in live chat online customer service. Unpublished doctoral dissertation, Temple University, Philadelphia.
