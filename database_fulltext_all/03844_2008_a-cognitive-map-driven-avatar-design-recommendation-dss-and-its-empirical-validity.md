---
otero_id: 3844
otero_key: "Q99A2NDJ"
title: "A cognitive map-driven avatar design recommendation DSS and its empirical validity"
authors: "Kun Chang Lee; Soonjae Kwon"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.06.008"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# A cognitive map-driven avatar design recommendation DSS and its empirical validity

Kun Chang Lee <sup>a,⁎</sup>, Soonjae Kwon <sup>b,⁎</sup>

<sup>a</sup> Professor of MIS, School of Business Administration, Sungkyunkwan University, Seoul 110-745, South Korea

<sup>b</sup> Research Professor of MIS Research Group for Intelligent U-Logistics Technology In-Ha University, Incheon 402-751, South Korea

Available online 23 June 2007

## Abstract

With the advent of the Internet era and the maturation of electronic commerce, strategic avatar design has become an important way of keeping up with market changes and customer tastes. In this study, we propose a new DSS for an adaptive avatar design that uses a cognitive map (CM) as a what-if simulation vehicle. The main virtue of the proposed avatar design recommendation DSS (abbreviated as ADR-DSS) is its ability to change specific avatar design features with objective consideration of the subsequent effects upon other design features, thereby enhancing user satisfaction. An avatar represents a user's self-identity and desire for self-disclosure. Therefore, the claim is made that there is a relationship between the characteristics of avatar design features and the choice of avatar. The considerations in this study are props (garments, facial expression, and miscellaneous) and subjective judgments (self-image and user satisfaction). The results of both brainstorming and focus group interviews with a group of avatar experts were used to objectively organize the CM. All the experts who participated are currently working in developing and designing avatar features in portal websites. Incorporating the CM as a model base, the proposed ADR-DSS was implemented, and two scenarios were presented for illustration. To prove the validity of the ADR-DSS, a rigorous survey was performed, obtaining statistically significant results. © 2007 Elsevier B.V. All rights reserved.

Keywords: Avatar design; Cognitive map; Self-identity; Self-disclosure; Props; Subjective judgment; Actual self-image; Ideal self-image; User satisfaction

## 1. Introduction

In text-based communications, users can express their identity with their ID, nickname, and profile [5,61]. Recently, avatars, basically manipulative graphic characters, have become a main instrument to express users' identities online [34,49]. The development of a graphic interface for the Internet has enticed online users to possess a graphic avatar as an agent identity in virtual communities [38]. Avatars have a special meaning as a symbol of identity in a virtual community, which is not necessarily identical to a user's identity in the real word [72]. As Internet users have begun to express themselves more and more creatively in cyberspace, avatar design has become increasingly important [60]. The term avatar, which originated in the Sanskrit language, can be translated “incarnation” or “God's appearance on earth.” In cyberspace, avatars are the pictures, drawings, or icons that users choose to represent themselves [48], typically including images of animals, cartoons, celebrities, or user photographs that embody evil, idiosyncrasy, position, power, and seduction, among other things [72]. Props denote a variety of avatar design features used for decoration, such as garments, accessories, hairstyles, and facial expressions. Avatars are widely used in computer games, e-mail, chat rooms, and e-commerce, making them an embodiment of users in a collaborative virtual environment [24,29]. They become virtual characters that make communication among users more natural and interactive [10].

Several advantages have made avatar use become widespread in cyberspace. In particular, avatars provide users with a degree of anonymity, which allows users to act as another person or take on a new cyber identity [30] and also creates a kind of privacy [66]. This unique aspect of avatars appeals particularly to users who want to share some of their personal information with others while still maintaining anonymity. Users tend to put personal longings and feelings into their avatars by combining a number of props. A commercial avatar shopping mall such as http://mall.freechal.com/Avt/ImAvatarMain.asp offers a large number of avatar props at a wide range of prices [48]. Successful avatar design depends on the wellorganized integration of avatar props to improve users' self-images and satisfaction. However, previous avatar design studies have not discussed a possible combination of props to enhance users' self-images and satisfaction.

The main obstacle in recommending a combination of props is the existence of causal relationships among the props that should be dealt with properly in the process of the avatar design. We propose a cognitive map (CM) [1,18,46] as an effective mechanism for this purpose because CMs have proven particularly useful for solving problems in which a number of factors, controllable or uncontrollable, are causally interrelated with one another [44,45,53]. In this sense, the main objectives of this study are twofold: (1) to propose an avatar design recommendation, a DSS named ADR-DSS, for users, and (2) to investigate its performance statistically by adhering to a rigorous survey method.

Section 2 discusses the theoretical background for the ADR-DSS with an extensive literature survey. Based on the theoretical background, Section 3 elaborates the proposed ADR-DSS in terms of database, model base, and inference procedures with two scenarios. In addition, the statistical validity of the ADR-DSS is empirically tested with a survey method in which 40 valid questionnaires were collected and analyzed. Finally, this study ends with concluding remarks in Section 4.

## 2. Theoretical background

## 2.1. Overview of Avatars

Recently, avatars have been used for the sake of communication effectiveness [49]. For instance, LifeFX provides Facemail, an avatar email system for interpersonal communication. Facemail uses a biologically based modeling system to deliver email messages through virtual people (photorealistic digital faces) that read the content of email aloud to the recipient with accompanying facial movements, such as nods, winks, kisses, or grimaces. In South Korea, where commercialized Internet applications are very popular in many parts of daily life, avatars are enthusiastically welcomed as a vehicle representing peoples' desired (mostly unfulfilled) future selves or different aspects of their actual selves [48].

In the fields of computer science and graphics, many studies are concerned with making avatars move more natural in a target system using sophisticated algorithms and techniques [6,26,47,50,57,67,68,75]. In particular, Lee and Shin [47] introduced the application of a more efficient mathematical representation of the kinematics of avatars in virtual environments. However, despite such studies about avatar design, no studies have attempted to recommend an optimal combination of avatar props to increase users' self-images and satisfaction. Therefore, this study will add value to the avatar literature.

To consider the characteristics of self-identity and self-disclosure through avatars, let us review the previous studies about them.

## 2.2. Self-identity and self-disclosure on cyberspace

Avatars are used to represent a user's need for selfidentity and self-disclosure in cyberspace. Therefore, we need to discuss those two qualities in depth. First, selfidentity is the unique characteristics of oneself formed by social interactions, developed continuously in time and place, and distinguished from other people [14,25]. In real worlds, self-identity can be defined according to diverse social roles, but it should be consistent with a person's real identity. Likewise, in cyberspace, users can have various self-identities, an ideal type or an unconscious type, by changing the avatar appearances. Baym [4] insists that users can create any type of self-identity in cyberspace, and the new online self-identity could be similar to or different from their real selves. Jordan [30] contended that the online self-identity should be flexibly connected to the offline self-identity of real worlds.

Second, self-disclosure refers to the process of telling another person about oneself: honestly sharing thoughts and feelings that may be very personal or private [32]. It is telling the truth, not just presenting your good side or your social mask. Jourard [31] particularly emphasized the importance of self-disclosure for intimate relationships with another person, which is also true in cyberspace. Self-disclosure is not only the basic activity of building a self in cyberspace; it is also an important occasion that triggers interaction with other people in cyberspace [51]. It is well-known that in cyberspace, the desire for self-disclosure is stronger than the desire to retain anonymity because people are more likely to enjoy freedom of expression unshackled from the various restrictions of reality [70].

![](/api/attachments/Q99A2NDJ/fulltext/images/242cd44696c00ba8ce4247044ede623a9a16e1fe156243089514706618836d77.jpg)  
Fig. 1. ADR-DSS architecture.

As mentioned so far, users' need for self-identity and self-disclosure in cyberspace is relatively stronger than it is offline in the real world. Therefore, avatars able to represent multiple aspects of users' self-identities, ideal or real, could become a natural and effective vehicle for actualizing their desire to reveal part of their selfidentities in acts of self-disclosure with others.

## 2.3. Cognitive map

A cognitive map (CM) is composed of (1) concept nodes that represent the factors describing a target problem; (2) arrows that indicate causal relationships between two concept nodes; and (3) causality coefficients on each arrow indicating the positive (or negative) strength with which a node affects other nodes. CMs allow a set of identified causality coefficients to be organized in an adjacency matrix. Since its introduction [73], the CM has been quite useful in political science [1] and administrative science [18]. CM has been especially effective in resolving problems in which many relevant factors are causally interrelated with one another and that require decisionmakers to analyze the causal relationships before solving the problems [16–18,36,43,53,58].

Various types of studies apply CM. For instance, CM was robustly used to solve distributed decision process modelling in networks [79], decision analysis [78], stock investment analysis problems [43], and business process redesign [42]. Causation in static and dynamic processes was represented using an M-labelled digraph to find solutions for unstructured problems [8,9]. Also, an inference via semantic networking was suggested using binary matrices and matrix multiplication [9].

Information requirement analysis was performed using a CM [53]. Kim and Pearl [35] suggested an inference engine for causal and diagnostic reasoning based on Pearl's [59] causal network formalism. Eden and Ackermann [16] proposed SODA (strategic options development and analysis) to encourage organizational members to actively define their own strategies. Lee et al. [44] developed COCOMAP (collective cognitive modelling) to support group cognitive processes and organizational learning through the creative use of CMs. Wellman [76] extended the applicability of CMs by proposing a qualitative probabilistic network based on formalisms about CMs. Similarly, a time variable was introduced into CMs [58] so they could be applied to cases that vary with time. Recently, a robust program called the Quanta application tool has allowed developers to visualize fuzzy CMs (FCMs) in an attempt to solve reasoning issues related to measuring performance-driven changes caused by business process reengineering (BPR) activities [77]. Furthermore, casebased reasoning techniques were successfully integrated with CMs to solve highly unstructured decision problems such as B2B negotiations [45].

CMs have also been used in engineering applications to represent graph-theoretic behaviour when investigating electrical circuits [71], describing plant controls [27], and considering geographical information collectively with all the relevant factors [63,64]. They provide a theoretical framework for semantic manipulation, knowledge representation, and approximate reasoning [78,79]. An adaptive CM was used to describe virtual worlds [13].

## 3. The proposed DSS

The proposed avatar design recommendation DSS (ADR-DSS) is based on a database of avatars and a CM as a model base. The ADR-DSS architecture is illustrated on Fig. 1.

## 3.1. Database

The ADR-DSS database stores props, including garments, facial expressions, and miscellany such as hairstyle, accessories, pets, and celebrity images to help users design their own personalized avatars. Table 1 shows details about the props and related subjective judgments such as self-images and user satisfaction. The props were extracted from the relevant literature [3,20,33,41,52,62,74]. Six universal facial expressions – happy, sad, angry, disgusted, surprised, and fearful – come from Ekman [20], Rizzo et al. [62] and Kleinsmith et al. [37]. Six types of garments – classical, party, designer, hip-hop, casual, bizarre – are identified from Kaiser [33] and Miller [52], and miscellaneous props – hairstyle, accessories, pets, celebrity characters – are taken from Balsamo [3]. Refer to Table 1 for details.

Because avatars have already been used extensively to represent self-images in cyberspace, we incorporate the two types of self-images addressed by Sirgy [69] as part of the subjective judgments: actual self-image and ideal selfimage. A user's actual self-image contains some aspects that the user actually possesses and wants to show to others via the avatar design; whereas a user's ideal selfimage contains aspects of self which the user is afraid to possess because of peer pressure or possible isolation from others, but which he or she is eager to embody in real life. An ideal self-image is therefore easily implemented in avatar design. User satisfaction with the avatar design can also be regarded as a subjective judgment to measure the validity of the design. Table 1 summarizes all the information about props and subjective judgments.

Props and subjective judgments related to avatar design

<table><tr><td>Avatar Design Features</td><td colspan="2">Types</td></tr><tr><td>Classical garments</td><td>Garments</td><td>Props</td></tr><tr><td>Party garments</td><td></td><td></td></tr><tr><td>Designer garments</td><td></td><td></td></tr><tr><td>Hip-hop garments</td><td></td><td></td></tr><tr><td>Casual garments</td><td></td><td></td></tr><tr><td>Bizarre garments</td><td></td><td></td></tr><tr><td>Sad facial expression</td><td>Facial expression</td><td></td></tr><tr><td>Happy facial expression</td><td></td><td></td></tr><tr><td>Anger facial expression</td><td></td><td></td></tr><tr><td>Disgust facial expression</td><td></td><td></td></tr><tr><td>Surprise facial expression</td><td></td><td></td></tr><tr><td>Fear facial expression</td><td></td><td></td></tr><tr><td>Hairstyle</td><td>Miscellaneous</td><td></td></tr><tr><td>Accessory</td><td></td><td></td></tr><tr><td>Pet animals</td><td></td><td></td></tr><tr><td>Celebrity characters</td><td></td><td></td></tr><tr><td>Actual Self-Image</td><td>Self-image</td><td>Subjective judgments</td></tr><tr><td>Ideal Self-Image</td><td></td><td></td></tr><tr><td>User satisfaction with avatar</td><td>Satisfaction</td><td></td></tr></table>

The proposed ADR-DSS is supposed to help users find best combination of props to maximize their satisfaction with the avatar design while maintaining their preferred self-images. Samples of props and avatar designs are illustrated in Fig. 2.

## 3.2. Model base

The model base of the ADR-DSS comes from the construction of the CM and its inference mechanism, the usefulness of which has already been proved in the literature, especially in representing the causal relationships among the elements of a given object and/or problem and providing what-if and goal-seeking simulation capabilities.

![](/api/attachments/Q99A2NDJ/fulltext/images/1c91960d4a294f9e1d411c43d501dea5ed36124921dc005c5127655cfc8d3b1d.jpg)  
Fig. 2. Samples of props and avatar designs.

People who work in any problem domain have individual mental cognitive maps that represent their beliefs about how the major variables in the domain influence one another [23]. The challenge here is to extract these cognitive maps from the experts and then combine them into a single collective cognitive map [65]. For this purpose, two methods – brainstorming and focus group interviews – have been used in the literature. First, brainstorming can be used to create a CM by allowing every participant to contribute his or her own ideas to the final CM [21]. Formal brainstorming is accomplished through a structured group workshop using the nominal group technique [12,28,56]. Bryson et al. [7] provide several helpful heuristic rules for managing the brainstorming process to create a cognitive map. Brainstorming methods enable participants to develop a sense of ownership and commitment to the final cognitive map. The common understanding that comes out of the brainstorming process helps build a common language and shared meaning upon which a consensus can rest.

Focus group interviews are another approach for capturing CMs [15,54]. In Qualitative and open-ended questions are posed to experts to obtain raw data in the form of narratives. The interview process follows either a deductive approach [55] or an inductive approach [11]. In the deductive approach, experts use a hierarchical structure to approach problems, whereas in the inductive approach, experts use a bottom-up structure and have no precise exemplars for many potential problems [22]. In the inductive approach, the CM emerges from the narrative of the experts after being refined based on a consensus among the experts; thus it is more exploratory than a CM created using a deductive approach. In either case, the interviewer must code the data from the interviews to create the causal relationships used in the final CM.

This study used brainstorming and focus group interviews to determine causal relationships between the relevant avatar design features and their causality coefficients. The goal was to construct an appropriate CM that can help users create the avatar design that would meet their self-images and improve their satisfaction.

![](/api/attachments/Q99A2NDJ/fulltext/images/7702d0e0b7927c227bae137d915eb24668c1b44af38eeb2ed9043ac47a922565.jpg)  
Fig. 3. A cognitive map used as a model base of the ADR-DSS.

<table><tr><td> $N_1$ </td><td> $N_2$ </td><td> $N_3$ </td><td> $N_4$ </td><td> $N_5$ </td><td> $N_6$ </td><td> $N_7$ </td><td> $N_8$ </td><td> $N_9$ </td><td> $N_{10}$ </td><td> $N_{11}$ </td><td> $N_{12}$ </td><td> $N_{13}$ </td><td> $N_{14}$ </td><td> $N_{15}$ </td><td> $N_{16}$ </td><td> $N_{17}$ </td><td> $N_{18}$ </td><td> $N_{19}$ </td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>-1</td><td>-1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>-1</td><td>-1</td><td>-1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>-1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>-1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>-1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>-1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-1</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td></tr></table>

Fig. 4. Adjacency matrix for the cognitive map of the ADR-DSS.

• Step 1: Causal Relationships and Causality. The first step configures the causal relationships among the relevant avatar design features. We performed brainstorming and a focus group interview with 9 avatar experts currently working in development and design of avatar features in portal websites in South Korea. The experts were required to examine the basic (although rough) causal relationships among the 19 proposed avatar design features in Table 1. After three rounds of feedback and subsequent adjustments, a final CM was derived as depicted in Fig. 3, in which a set of causal relationships exists among the design features. With regard to causality, we assumed that the real line indicated a positive causality (+1), and the dotted line denoted a negative causality (−1).

• Step 2: Adjacency Matrix for Avatar Design. Fig. 4 depicts an adjacency matrix for avatar design derived from the CM in Fig. 3. This adjacency matrix needs to be arranged for further what-if simulation to find avatar designs that maximize user satisfaction while maintaining users' self-images. The concept node vector (N) includes the 19 elements shown in Table 2.

## 3.3. Simulations

We view the CM as a dynamic system that settles into a specific stable state over time. Therefore, the causal dynamic system represented by the CM responds to external stimuli, and we take its equilibrium behavior as an inference. For the sake of illustrating the what-if simulation capabilities of the ADR-DSS, let us consider three scenarios in which users can find their own personalized set of avatar design features, maximizing their satisfaction while maintaining their self-images.

## 3.3.1. Scenario 1

If users want to use such design features as happy facial expression $( N _ { 3 } )$ , designer garments $( N _ { g } )$ ,or hairstyle $( N _ { I 4 } )$ for their avatars, how satisfied would they be with the avatar design? Are there any other design features that users should consider to improve their satisfaction as well as their self-images?

Concept nodes denoting avatar design features

<table><tr><td>Node</td><td>Design features</td></tr><tr><td> $N_{1}$ </td><td>Sad facial expression</td></tr><tr><td> $N_{2}$ </td><td>Fear facial expression</td></tr><tr><td> $N_{3}$ </td><td>Happy facial expression</td></tr><tr><td> $N_{4}$ </td><td>Disgust facial expression</td></tr><tr><td> $N_{5}$ </td><td>Anger facial expression</td></tr><tr><td> $N_{6}$ </td><td>Surprise facial expression</td></tr><tr><td> $N_{7}$ </td><td>Casual garments</td></tr><tr><td> $N_{8}$ </td><td>Hip-hop garments</td></tr><tr><td> $N_{9}$ </td><td>Designer garments</td></tr><tr><td> $N_{10}$ </td><td>Classical garments</td></tr><tr><td> $N_{11}$ </td><td>Party garments</td></tr><tr><td> $N_{12}$ </td><td>Bizarre garments</td></tr><tr><td> $N_{13}$ </td><td>Accessory</td></tr><tr><td> $N_{14}$ </td><td>Hairstyle</td></tr><tr><td> $N_{15}$ </td><td>Pet animals</td></tr><tr><td> $N_{16}$ </td><td>Celebrity characters</td></tr><tr><td> $N_{17}$ </td><td>Actual self-image</td></tr><tr><td> $N_{18}$ </td><td>Ideal self-image</td></tr><tr><td> $N_{19}$ </td><td>User satisfaction with avatar design</td></tr></table>

Based on the basic information given in the If-clause, the first concept node vector can be prepared as follows: $\mathbf { N } _ { 1 } = ( 0 \mathrm { ~ 0 ~ 1 ~ 0 ~ 0 ~ 0 ~ 0 ~ 0 ~ 1 ~ 0 ~ 0 ~ 0 ~ 0 ~ 1 ~ 0 ~ 0 ~ 0 ~ 0 ~ 0 ~ } )$

Using $\Nu _ { 1 }$ as a starting input vector and applying a 1/2 threshold for the convergence check [39,40], the ADR-DSS computes the following CM-based simulation process. →, which is used to secure convergence within a finite number of iterations. It denotes application of the 1/2 threshold to the simulation result, where 1 if the result is greater than 0.5, otherwise 0. Based on $\Nu _ { 1 }$ and $\mathrm { E , }$ the ADR-DSS performs the following inference processes.

<table><tr><td colspan="20">Inference 1:</td></tr><tr><td> $N_1$ xE=</td><td>(0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>2</td><td>2</td><td>0)</td></tr><tr><td>→</td><td>(0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0) = $N_2$ </td></tr><tr><td colspan="20">Inference 2:</td></tr><tr><td> $N_2$ xE=</td><td>(0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>4</td><td>4</td><td>2)</td></tr><tr><td>→</td><td>(0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1) = $N_3$ </td></tr><tr><td colspan="20">Inference 3:</td></tr><tr><td> $N_3$ xE=</td><td>(0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>4</td><td>4</td><td>2)</td></tr><tr><td>→</td><td>(0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1) = $N_4$ </td></tr></table>

As can be seen from the inference processes, ${ \mathrm { N } } _ { 3 } = { \mathrm { N } } _ { 4 } ,$ implying that the inference processes reach equilibrium and that both actual self-image $( \Nu _ { 1 7 } )$ and ideal self-image $( N _ { I \vartheta } )$ are activated successfully, and that user satisfaction with avatar design $( N _ { I 9 } )$ is also secured. The fact that the user's subjective judgments, including two self-images $( N _ { I 7 } , \ N _ { I 8 } )$ as well as user satisfaction $( N _ { I ^ { g } } ) _ { : }$ , are successfully activated with 1 in the equilibrium state vector $\mathrm { N } _ { 4 }$ shows that the ADR-DSS can recommend avatar design features that meet users' subjective judgments.

From the equilibrium state vector $\mathrm { N } _ { 4 }$ suggested by the ADR-DSS, we can identify new information regarding the avatar design. Several new design features (in correspondence with 1's in $\mathrm { N } _ { 4 } )$ could improve user satisfaction, including party garments $( N _ { I I } ) ,$ , accessories $( N _ { I 3 } )$ , and pets $( N _ { I 5 } )$ . Accordingly, another round of simulation can be carried out by the ADR-DSS using a new stimulus vector, $\mathrm { N } _ { 1 } ,$ , in which six design features are taken into consideration in line with the recommendation of the ADR-DSS: happy facial expression $( N _ { 3 } )$ , designer garments $( N _ { g } )$ or hairstyle $( N _ { I 4 } ) _ { \ l }$ , party garments $( N _ { I I } ) _ { }$ , accessories $( N _ { I 3 } ) .$ and pets $( N _ { I 5 } )$ . The new inferences by the ADR-DSS are as follows:

<table><tr><td> $N_1=$ </td><td>(0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0)</td><td></td></tr><tr><td colspan="21">Inference 1:</td></tr><tr><td> $N_1xE=$ </td><td>(0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>4</td><td>4</td><td>0)</td><td></td></tr><tr><td>→</td><td>(0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0)</td><td> $=N_2$ </td></tr><tr><td colspan="21">Inference 2:</td></tr><tr><td> $N_2xE=$ </td><td>(0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>4</td><td>4</td><td>2)</td><td></td></tr><tr><td>→</td><td>(0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1)</td><td> $=N_3$ </td></tr><tr><td colspan="21">Inference 3:</td></tr><tr><td> $N_3xE=$ </td><td>(0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>4</td><td>4</td><td>2)</td><td></td></tr><tr><td>→</td><td>(0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1)</td><td> $=N_4$ </td></tr></table>

The equilibrium state vector $\mathrm { N } _ { 4 }$ shows that there is no need to consider another design feature because all the user subjective judgments are satisfied.

## 3.3.2. Scenario 2

If users want to design avatars using props such as sad facial expression $( N _ { I } )$ , casual garments $( N _ { 7 } )$ , and celebrity character $( N _ { I 6 } )$ , the initial stimulus vector, N , is as follows: ${ \bf N } _ { 1 } = ( 1 \mathrm { ~ 0 ~ 0 ~ 0 ~ 0 ~ 0 ~ 0 ~ 1 ~ 0 ~ 0 ~ 0 ~ 0 ~ 0 ~ 0 ~ 0 ~ 0 ~ 1 ~ 0 ~ 0 ~ 0 ~ } )$ The ADR-DSS performs the simulation as follows.

<table><tr><td colspan="20">Inference 1:</td></tr><tr><td> $N_1$ xE=</td><td>(0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>-1</td><td>-1</td><td>1</td><td>1</td><td>0)</td></tr><tr><td>→</td><td>(1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0) = $N_2$ </td></tr><tr><td colspan="20">Inference 2:</td></tr><tr><td> $N_2$ xE=</td><td>(0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>-1</td><td>-1</td><td>2</td><td>4</td><td>2)</td></tr><tr><td>→</td><td>(1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1) = $N_3$ </td></tr><tr><td colspan="20">Inference 3:</td></tr><tr><td> $N_3$ xE=</td><td>(0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>-1</td><td>-1</td><td>2</td><td>4</td><td>2)</td></tr><tr><td>→</td><td>(1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1) = $N_4$ </td></tr></table>

From the final equilibrium state vector, $\mathrm { N } _ { 4 } ,$ the ADR-DSS recommends the need to consider such additional design features as designer garments(N ), party garments $( N _ { I I } )$ , bizarre garments $( N _ { I 2 } )$ ,and accessories $( N _ { I 3 } )$ to further improve users' subjective judgments. Based on this recommendation, users can start the next round of avatar design simulation with the ADR-DSS. The results are as follows, showing that there is no room for improvement in the users' subjective judgments.

<table><tr><td> $N_1=$ </td><td>(1 0 0 0 0 0 1 0 1 0 1 1 1 0 0 1 0 0 0)</td></tr><tr><td colspan="2">Inference 1:</td></tr><tr><td> $N_1xE=$ </td><td>(0 0 0 0 0 0 1 0 1 0 1 1 1 0 -1 -1 2 4 0)</td></tr><tr><td>→</td><td>(1 0 0 0 0 0 1 0 1 0 1 1 1 0 0 1 1 1 0 = $N_2$ </td></tr><tr><td colspan="2">Inference 2:</td></tr><tr><td> $N_2xE=$ </td><td>(0 0 0 0 0 0 1 0 1 0 1 1 1 0 -1 -1 2 4 2)</td></tr><tr><td>→</td><td>(1 0 0 0 0 0 1 0 1 0 1 1 1 0 0 1 1 1 1 = $N_3$ </td></tr><tr><td colspan="2">Inference 3:</td></tr><tr><td> $N_3xE=$ </td><td>(0 0 0 0 0 0 1 0 1 0 1 1 1 0 -1 -1 2 4 2)</td></tr><tr><td>→</td><td>(1 0 0 0 0 0 1 0 1 0 1 1 1 0 0 1 1 1 1 = $N_4$ </td></tr></table>

In this way, the ADR-DSS can recommend additional avatar design features based on each user's initial design requirements. To prove the statistical validity of the proposed ADR-DSS performance, a survey was taken.

## 3.4. Statistical evaluation of the ADR-DSS

To prove the statistical validity of the proposed ADR-DSS, we conducted a survey method in which valid questionnaires were collected from 40 undergraduate students who volunteered to participate in the experiment because they expressed a desire to experience the ADR-DSS personally. It is worth noting that avatars are very popular among young people in South Korea — most of them operate their own personal mini-homepages, decorating them with a wide variety of avatars. One interesting phenomenon easily observed among Korean young people is that it is a part of their daily life activities to often present many types of avatar props to their friends as birthday gifts or to celebrate special events. Therefore, it is no surprise that most portal websites in South Korea, such as Naver (www.naver.com), Daum (www.daum. net), Paran (itemmall.paran.com), and Freechal (www. freechal.com), operate avatar item shopping malls to sell a wide variety of props.

Because decision performance by the proposed ADR-DSS should be tested statistically, our first job was to configure a questionnaire to evaluate the decisionmakers' psychological attitudes towards the proposed ADR-DSS, as well as its quantitative aspects. Before proceeding further, it seems necessary to consider the meaning of decision performance. Decision performance is “to evaluate the outcomes generated by individuals or groups in accomplishing their task” [19]. According to Aldag and Power [2], such evaluation measures fall into seven general categories: (1) confidence in decision quality; (2) enhancement of problem-solving ability; (3)

<table><tr><td rowspan="2" colspan="2">Explanatory variables</td><td colspan="2">ADR-DSS</td><td colspan="2">Non-ADR-DSS</td><td rowspan="2">T-value for difference</td><td rowspan="2">P-value</td></tr><tr><td>Mean</td><td>Standard deviation</td><td>Mean</td><td>Standard deviation</td></tr><tr><td rowspan="3">Confidence in decision quality</td><td>My avatar design solution was a good one</td><td>2.30</td><td>0.76</td><td>4.33</td><td>0.47</td><td>11.93</td><td>.000***</td></tr><tr><td>I am not sure my avatar design solution was appropriate (R)</td><td>3.58</td><td>0.75</td><td>1.93</td><td>0.80</td><td>9.50</td><td>.000***</td></tr><tr><td>I am not confident about my avatar design solution (R)</td><td>3.63</td><td>0.59</td><td>1.98</td><td>0.77</td><td>11.33</td><td>.000***</td></tr><tr><td rowspan="3">Enhancement of problem-solving ability</td><td>Analyzing the avatar design problem with this approach improved my problem-solving skills</td><td>2.78</td><td>0.86</td><td>4.55</td><td>0.60</td><td>8.21</td><td>.000***</td></tr><tr><td>Analyzing the avatar design problem with this approach was a useful learning experience</td><td>2.73</td><td>0.88</td><td>4.43</td><td>0.75</td><td>8.50</td><td>.000***</td></tr><tr><td>I&#x27;ll be able to handle future avatar design problem better because of the approach I used to analyze this avatar design problem</td><td>2.38</td><td>1.10</td><td>4.00</td><td>0.60</td><td>8.06</td><td>.000***</td></tr><tr><td rowspan="3">Satisfaction with resource expenditure</td><td>It took too much time to solve the avatar design problem (R)</td><td>4.08</td><td>0.73</td><td>2.43</td><td>0.81</td><td>8.08</td><td>.000***</td></tr><tr><td>The time and effort used to analyze the avatar design problem were well spent (R)</td><td>3.93</td><td>0.83</td><td>2.80</td><td>0.85</td><td>5.22</td><td>.000***</td></tr><tr><td>The approach used to analyze the avatar design problem wasn&#x27;t worth the effort (R)</td><td>2.88</td><td>0.94</td><td>2.15</td><td>0.43</td><td>4.22</td><td>.000***</td></tr><tr><td rowspan="3">Perceived acceptability of solution</td><td>People in the avatar design problem who would be affected by my avatar design solution would probably be satisfied with it</td><td>2.75</td><td>0.90</td><td>4.33</td><td>0.57</td><td>7.67</td><td>.000***</td></tr><tr><td>I might find it hard to get my avatar design solution implemented (R)</td><td>3.35</td><td>1.03</td><td>2.63</td><td>0.70</td><td>4.65</td><td>.000***</td></tr><tr><td>I could easily justify my avatar design solution</td><td>2.28</td><td>1.04</td><td>3.65</td><td>1.21</td><td>7.58</td><td>.000***</td></tr><tr><td rowspan="3">Perceived process structure</td><td>The approach taken to solving the avatar design problem was very structured</td><td>2.00</td><td>0.91</td><td>4.53</td><td>0.51</td><td>13.10</td><td>.000***</td></tr><tr><td>My analysis of the avatar design problem was systematic</td><td>1.90</td><td>0.84</td><td>4.65</td><td>0.48</td><td>15.14</td><td>.000***</td></tr><tr><td>I analyzed the avatar design problem in a step-by-step manner</td><td>2.25</td><td>0.87</td><td>4.35</td><td>0.48</td><td>12.28</td><td>.000***</td></tr><tr><td rowspan="3">Perceived process adequacy</td><td>I wish I had approached the avatar design problem differently (R)</td><td>3.70</td><td>0.69</td><td>1.88</td><td>0.40</td><td>13.68</td><td>.000***</td></tr><tr><td>I really felt lost in trying to tackle the avatar design problem (R)</td><td>3.65</td><td>0.58</td><td>2.08</td><td>0.42</td><td>11.40</td><td>.000***</td></tr><tr><td>I may have missed important things in the avatar design problem (R)</td><td>4.25</td><td>0.98</td><td>1.75</td><td>0.74</td><td>12.97</td><td>.000***</td></tr><tr><td rowspan="3">Positive affect toward the decision process</td><td>I am pleased with the approach used to analyze the avatar design problem</td><td>2.30</td><td>0.91</td><td>4.25</td><td>0.54</td><td>10.12</td><td>.000***</td></tr><tr><td>Analyzing the avatar design problem with this approach was frustrating to me (R)</td><td>3.58</td><td>0.98</td><td>1.85</td><td>0.43</td><td>9.45</td><td>.000***</td></tr><tr><td>Analyzing the avatar design problem with this approach was interesting</td><td>2.30</td><td>0.88</td><td>4.73</td><td>0.45</td><td>13.31</td><td>.000***</td></tr></table>

<sup>⁎⁎⁎</sup>pb0.001.

satisfaction with resource expenditure; (4) perceived acceptability of solution; (5) perceived process structure; (6) perceived process adequacy; (7) positive affect toward process. Therefore, we adopted Aldag and Power's [2] seven categories to organize our questionnaire, which contained 21 items as shown in Table 3. To maintain methodological rigor, we invited four doctoral students to check the questionnaire items.

For the sake of the experiment, the 40 students who volunteered are taking electronic commerce, Internet programming courses offered by the School of Business Administration. Each participant was given two kinds of DSSs — the ADR-DSS and a non-ADR-DSS that just shows final avatar designs that meet the user's initial requirements without recommending additional avatar design features based on the CM. Each participant was given 10–15nmin to experience both the ADR-DSS and the non-ADR-DSS with the two scenarios. Then they were asked to answer the questionnaire of 21 items as shown in Table 3 by circling a number from one to five arranged horizontally beneath anchor point descriptions “Strongly Disagree (1),” “Neutral (3),” and “Strongly Agree (5)”. It is noteworthy that several items are reverse, denoted by (R). Because each participant was asked to evaluate the questionnaire for the two kinds of DSSs, survey results are analyzed statistically using the paired t-test. To prevent the learning effect that could occur through repeated use of the ADR-DSS, a counterbalancing method was used. During the experiment, participants were assigned randomly to one of the DSSs and asked to experience that DSS with the two scenarios discussed in Section 3.3.

Table 3 shows the paired t-test results, revealing that for all 21 items, the participants perceived a significant difference between the ADR-DSS and the non-ADR-DSS. Statistical results show that the ADR-DSS was clearly favored over the non-ADR-DSS. All the mean values of the 21 items for the ADR-DSS are greater than those for the non-ADR-DSS, and the t-test results of the mean differences revealed that the ADR-DSS yields higher results than the non-ADR-DSS in all the questionnaire items with 99% statistical significance.

## 4. Concluding remarks

This study proposes a new type of the avatar design recommendation DSS named the ADR-DSS able to recommend a number of additional avatar design features that can best satisfy user subjective judgments such as actual self-image, ideal self-image, and user satisfaction. Through extensive brainstorming and focus group interviews with avatar experts, we organized a cognitive map.

The usability of the cognitive map is strategically incorporated into the ADR-DSS to improve recommendation effectiveness. Two scenarios were suggested showing how the ADR-DSS works. The main contributions of this study are as follows. First, we proved that the effectiveness of the avatar design recommendation DSS can be significantly improved by taking advantage of the what-if inference capability of a cognitive map. Second, by classifying the props in terms of users' subjective judgments, we were able to recommend the best combination of avatar design features to meet the users' design requirements.

The practical implications of the proposed approach are as follows: the most prominent advantage of our approach is that users can predict the chain of effects that results from changes in avatar design features before actually making any design changes. Also, the proposed ADR-DSS makes it possible for decision-makers to detect the most influential design features. In this way, decision-makers can reduce the risks inherent in changing their avatar design. Because the CM permits all related avatar design features to be viewed graphically in a single interrelated diagram and organized numerically into an adjacency matrix, users can perform a number of what-if simulations to see whether such changes would lead to improvement in actual self-image, ideal selfimage, and user satisfaction.

Despite these contributions, further research issues still remain. The performance of the ADR-DSS can be upgraded by integrating artificial intelligence methods such as neural networks, genetic algorithms, etc., because those heuristic methods are known to have great potential to solve highly unstructured problems. Another issue worthy of being explored is that avatar designs may affect the degree of trust users perceive during electronic communications with others. In other words, how much an avatar design would affect trust transference can be tackled seriously by using the proposed ADR-DSS as an engine to produce various types of avatars that may be attached to electronic messages.

## References

[1] R.J. Aldag, D.J. Power, An empirical assessment of computerassisted decision analysis, Decision Science 17 (4) (1986).

[2] R. Axelrod, Structure of Decision: The Cognitive Maps of Political Elites, Princeton University Press, 1976.

[3] A. Balsamo, The virtual body in cyberspace, Research in Philosophy & Technology 13 (1993).

[4] N.K. Baym, The Emergence of Community in Computer-Mediated Communication, in: S.G. Jones (Ed.), CyberSociety: Computer-Mediated Communication and Community, Sage, London, 1995.

[5] H. Bechar, From bonehead to clonehead: nicknames, play, and identity on Internet relay chat, Journal of Computer Mediated Communication 1 (2) (1995).

[6] R. Boulic, P. Becheiraz, L. Emering, D. Thalmann, Integration of Motion Control Techniques for Virtual Human and Avatar Real-Time Animation, Proceedings of the ACM Symposium on Virtual Reality Software and Technology, 1997.

[7] J.M. Bryson, F. Ackermann, C. Eden, C.B. Finn, Visible thinking: Unlocking causal mapping for practical business results, Wiley, San Francisco, 2004.

[8] J.R. Burns, W.H. Winstead, M-labeled digraphs: An aid to the use of structural and simulation models, Management Science 31 (3) (1985).

[9] J.R. Burns, W.H. Winstead, D.A. Haworth, Semantic nets as paradigms for both causal and judgmental knowledge representation, IEEE Transactions on Systems, Man and Cybernetics 19 (1) (1989).

[10] E. Daniel, H. Wilson, M. McDonald, Towards a map of marketing information systems: An inductive study, European Journal of Marketing 37 (5/6) (2003).

[11] M. Del, P. Carretero, D. Oyarzum, A. Ortiz, I. Aizpurua, J. Posada, Virtual characters facial and body animation through the edition and interpretation of mark-up language, Computers & Graphics 29 (2) (2005).

[12] A.L. Delbecq, A.H. Van de Ven, D.H. Gustafson, Group techniques for program planning: A guide to nominal group and Delphi processes, Scott, Foresman, 1975.

[13] J.A. Dickerson, B. Kosko, Adaptive Cognitive Maps in Virtual Worlds, International Neural Network Society Annual Meeting World Congress Neural Networks, 1994.

[14] M.H. Dignan, Ego identity and maternal identification, Journal of Personality and Social Psychology 1 (1965) 476–483.

[15] C. Eden, Cognitive mapping: a review, European Journal of Operational Research 36 (1) (1988).

[16] C. Eden, F. Ackermann, Strategic options development and analysis (SODA) — using a computer to help with the management of strategic vision, in: G. Doukidis, F. Land, G. Miller (Eds.), Knowledge-Based Management Support Systems, Ellis Horwood, UK, 1989

[17] C. Eden, S. Jones, Publish or perish? — A case study, Journal of the Operational Research Society 31 (2) (1980).

[18] C. Eden, S. Jones, D. Sims, Thinking in Organizations, Macmillian Press Ltd, London England, 1979.

[19] M.A. Eierman, F. Niederman, C. Adams, DSS theory: A model of constructs and relationships, Decision Support Systems 14 (1) (1995).

[20] P. Ekman, The argument and evidence about universals in facial expressions of emotion, in: H. Wagner, A. Manstead (Eds.), Handbook of Social Psychology, Wiley, Chichester, U.K, 1989.

[21] J.R. Evans, Total quality management, organization, and strategy, 4th ed., Mason, Thomson Smith-Western, 2005.

[22] R. Fisher, Public relations problem solving: heuristics and expertise, Journal of Public Relations Research 10 (2) (1998).

[23] R. Franzosi, Content analysis, in: M.S. Lewis-Beck, et al., (Eds.), The SAGE encyclopedia of social science research methods, Sage, Thousand Oaks, CA, 2004.

[24] M. Gerhard, D. Moore, User embodiments in educational CVEs: towards continuous presence, Proceedings of the International Conference on Network Entities (NETIES), Leeds, UK, 1998.

[25] A. Giddens, Modernity & Self-identity, Stanford University Press, 1991.

[26] M. Gillies, N.A. Dodgson, Behaviorally rich actions for usercontrolled characters, Computers & Graphics 28 (6) (2004).

[27] K. Gotoh, J. Murakami, T. Yamaguchi, Y. Yamanaka, Application of fuzzy cognitive maps to supporting for plant control,

SICE Joint Symposium of 15th Systems Symposium and 10th Knowledge Engineering Symposium, 1989.

[28] D.M. Hegedus, R.V. Rasmussen, Task effectiveness and interaction process of a modified nominal group technique in solving an evaluation problem, Journal of Management 12 (4) (1986).

[29] J. Huang, Y. Du, C. Wang, Design of the server cluster to support avatar migration, Proceedings of the IEEE virtual reality, Los Angeles, 2003.

[30] T. Jordan, Cyber Power: The Culture and Politics of Cyberspace and the Internet, Routledge, 1999.

[31] S.M. Jourard, Healthy personality, MacMillan Co, New York, 1974.

[32] S.M. Jourard, P. Lasakow, Some factors in self-disclosure, Journal of Abnormal and Social Psychology 56 (1) (1958).

[33] S. Kaiser, The Social Psychology of Clothing: Symbolic Appearance in Context, Second Edition RevisedFairchild, New York, 1997.

[34] H.S. Kang, H.D. Yang, The visual characteristics of avatars in computer-mediated communication: comparison of Internet relay chat and instant messenger as of 2003, International Journal of Human Computer Studies 64 (12) (2006).

[35] J.H. Kim, J. Pearl, CONVINCE: a conversational inference consolidation engine, IEEE Transactions on Systems, Man and Cybernetics 17 (2) (1987).

[36] J.C. Klein, D.F. Cooper, Cognitive maps of decision makers in a complex game, Journal of the Operational Research Society 33 (1) (1982).

[37] A. Kleinsmith, R. De Silva, N. Bianchi-Berthouze, Cross-cultural differences in recognizing affect from body posture, Interacting with Computers 18 (6) (2006).

[38] E. Kolko, Representing bodies in virtual space: the rhetoric of avatar design, The Information Society 15 (3) (1999).

[39] A. Kosko, Fuzzy cognitive maps, International Journal of Man-Machine Studies 24 (1) (1986).

[40] B. Kosko, Neural Networks and Fuzzy Systems: A Dynamical Systems Approach to Machine Intelligence, Prentice-Hall, 1992.

[41] J. Ku, H.J. Jang, K.U. Kim, J.H. Kim, S.H. Park, J.H. Lee, J.J. Kim, I.Y. Kim, S.I. Kim, Experimental results of affective valence and arousal to avatar's facial expressions, CyberPsychology & Behavior 8 (5) (2005).

[42] K.Y. Kwahk, Y.G. Kim, Supporting business process redesign using cognitive maps, Decision Support Systems 25 (2) (1999).

[43] K.C. Lee, H.S. Kim, A fuzzy cognitive map-based bi-directional inference mechanism: an application to stock investment analysis, International Journal of Intelligent Systems in Accounting, Finance & Management 6 (1) (1997).

[44] K.C. Lee, S.J. Kwon, The use of cognitive maps and case-based reasoning for B2B negotiation, Journal of Management Information Systems 22 (4) (2006).

[45] K.C. Lee, S. Lee, A cognitive map simulation approach to adjusting the design factors of the electronic commerce web sites, Expert Systems with Applications 24 (1) (2003).

[46] J. Lee, K.H. Lee, Precomputing avatar behavior from human motion data, Graphical Models 68 (2) (2006).

[47] O. Lee, M. Shin, Addictive consumption of avatars in cyberspace, CyberPsychology & Behavior 7 (4) (2004).

[48] S. Lee, J.F. Courtney, R.M. O'Keefe, A system for organizational learning using cognitive maps, Omega 20 (1) (1992).

[49] Y. Lee, K.A. Kozar, K.R. Larsen, Does avatar email improve communication? Seeking to enhance communication systems by adding expressive cues, Communications of the ACM 48 (2) (2005).

[50] C. Luciano, P. Banerjee, Avatar kinematics modeling for telecollaborative virtual environments,, Proceedings of the 2000 Winter Simulation Conference, vol. 2, 2000.

[51] E. Merkle, R. Richardson, Digital dating and virtual relating: conceptualizing computer mediated romantic relationships, Family Relations 49 (2) (2000).

[52] K.A. Miller, Dress: private and secret self-expression, Clothing and Textiles Research Journal 15 (4) (1998).

[53] A.R. Montazemi, D.W. Conrath, The use of cognitive mapping for information requirements analysis, MIS Quarterly 10 (1) (1986).

[54] K.M. Nelson, S. Nadkarni, V.K. Narayanan, M. Ghod, Understanding software operations support expertise: a revealed causal mapping approach, MIS Quarterly 24 (3) (2000).

[55] S. Newstead, S. Handley, C. Harley, H. Wright, D. Farrelly, Individual differences inductive reasoning, Quarterly Journal of Experimental Psychology: Section A 57 (1) (2004).

[56] J.D. Novak, Learning, creating, and using knowledge: Concept maps as facilitative tools, Erlbaum, Mahwah, 1998.

[57] J. Ohya, R. Nakatsu, S. Kawato, T. Sakaguchi, Virtual me: A virtual communication method that enables simultaneous multiple existence as an avatar and/or agents, Proceedings of the IEEE International Conference on Multimedia and Expo, vol. 3, 2000.

[58] K.S. Park, S.H. Kim, Fuzzy cognitive maps considering time relationships, International Journal of Human-Computer Studies 42 (2) (1995).

[59] J. Pearl, Fusion, propagation, and structuring in belief networks, Artificial Intelligence 29 (3) (1986).

[60] P. Plantec, Virtual Humans: A Build-It-Yourself Kit Complete with Software and Step-by-Step Instructions, American Management Association, NY, 2004.

[61] E.M. Reid, Identity and the cyborg body, cultural formation in text-based virtual realities, , 1994.

[62] A.A. Rizzo, U. Neumann, R. Encisco, D. Fidaleo, J.Y. Noh, Performance-driven facial animation: basic research on human judgments of emotional state in facial avatars, CyberPsychology & Behavior 4 (4) (2001).

[63] R. Satur, Z.Q. Liu, A contextual fuzzy cognitive map framework for geographic information systems, IEEE Transactions on Fuzzy Systems 7 (5) (1999).

[64] R. Satur, Z.Q. Liu, A context driven intelligent database processing system using object-oriented fuzzy cognitive maps, International Journal of Intelligent Systems 11 (9) (1996).

[65] A.J. Scavarda, T. Bouzdine-Chameeva, S.M. Goldstein, J.M. Hays, A.V. Hill, A methodology for constructing collective casual maps, Decision Science 37 (2) (2006).

[66] R. Schroeder, The social life of avatars, Springer-Verlag London Limited, 2002.

[67] S.K. Semwal, R. Hightower, S. Stansfield, Closed form and geometric algorithms for real-time control of an avatar, Proceedings of the Virtual Reality Annual International Symposium, 1996.

[68] J. Shi, T.J. Smith, J.P. Granieri, N.I. Badler, Smart avatars in JackMOO, Proceedings of IEEE Virtual Reality (1999).

[69] M.J. Sirgy, Self-concept in consumer behavior and consumer decision making, Journal of Consumer Research 9 (3) (1982).

[70] L. Sproull, S. Kiesler, Reducing social context cues: electronic mail in organizational communication, Management Science 32 (11) (1986).

[71] M.A. Styblinski, B.D. Meyer, Fuzzy cognitive maps, signal flow graphs, and qualitative circuit analysis, Proceedings of the 2nd IEEE International Conference on Neural Networks, 1988.

[72] J. Suler, The psychology of cyberspace, in: M. Beiswenger (Ed.), Ibidem, Chat Communication, 1999, Stuttgart.

[73] E.C. Tolman, Cognitive maps in rats and men, Psychological Review 55 (4) (1948).

[74] V. Vesna, Marketplace: from agents and avatars to the information personae, Digital Creativity 9 (3) (1998).

[75] Waller, G. Dodds, Reactive agent based planning for an avatar, Proceedings of the International Conference on Advanced Intelligent Mechatronics, 1999.

[76] M. Wellman, Inference in cognitive maps, Mathematics and Computers in Simulation 36 (2) (1994).

[77] G. Xirogiannis, M. Glykas, Fuzzy cognitive maps in business analysis and performance-driven change, IEEE Transactions on Engineering Management 51 (3) (2004).

[78] W.R. Zhang, S.S. Chen, J.C. Bezdek, Pool2: a generic system for cognitive map development and decision analysis, IEEE Transactions on Systems, Man and Cybernetics 19 (1) (1989).

[79] W.R. Zhang, W. Wang, R.S. King, A-Pool: an agent-oriented open system shell for distributed decision process modeling, Journal of Organizational Computing 4 (2) (1994).

![](/api/attachments/Q99A2NDJ/fulltext/images/8b7aa8fc597249fae9b094d26f7ef05cabbf9be2c79e9942aa5cdf09c2f6c161.jpg)

Kun Chang Lee is a full professor of MIS at Sungkyunkwan University in Seoul, Korea. He received his Ph.D. in MIS from Korea Advanced Institute of Science and Technology (KAIST), a Master of Sciences in MIS from KAIST, and a B.A. in business administration from Sungkyunkwan University, Seoul, Korea. His research focuses on decision analysis involved in electronic commerce management. Recently, he is developing several working papers specializing in knowl-

edge management, artificial intelligence-based analysis of IS performance, and schema-based decisions. His research findings have been published in Journal of Management Information Systems, IEEE Transactions on Engineering Management, Decision Support Systems, International Journal of Production Research, Expert Systems with Applications, Fuzzy Sets and Systems, among others.

![](/api/attachments/Q99A2NDJ/fulltext/images/230393ae35af8271dba1bfeeefad8842e30d007a26b0f7823e88fa584c3aa1c1.jpg)

Soonjae Kwon received his Ph.D. in MIS, an M.S. in Business Administration, and a B.A. in Accounting, all from Sungkyunkwan Uni versity. He is currently preparing working papers about recommendation systems, consumer decision and behavior in electronic commerce, and ubiquitous commerce. His research findings appeared or are forthcoming in Journal of Management Information Systems, Decision Support Systems, and Expert Systems with Applications.
