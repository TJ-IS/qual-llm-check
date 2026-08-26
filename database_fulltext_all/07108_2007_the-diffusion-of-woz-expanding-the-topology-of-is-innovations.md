---
otero_id: 7108
otero_key: "JGJDQUYG"
title: "The Diffusion of WOZ: Expanding the Topology of IS Innovations"
authors: "Gabriel J Costello; Brian Donnellan"
year: "2007"
journal: "Journal of Information Technology"
doi: "10.1057/palgrave.jit.2000085"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research Article

# The diffusion of WOZ: expanding the topology of IS innovations

Gabriel J Costello<sup>1</sup> and Brian Donnellan<sup>2</sup>

<sup>1</sup>Galway-Mayo Institute of Technology, Galway, Ireland; <sup>2</sup>National University of Ireland, Galway, Ireland

Correspondence:

GJ Costello, Galway-Mayo Institute of Technology, Dublin Road, Galway, Ireland.

Tel: þ 353 (0) 91 742382 3;

Fax: þ 353 (0) 758413;

E-mail: gabrielj.costello@gmit.ie

## Abstract

The growth and diffusion of self-service technology (SST) over the last decade has resulted in an increasing number of business and government transactions being completed without human assistance. One innovation in this area, the speech-enabled business system, is characterised by complex implementations that bring together languageprocessing technologies, applications development, and end-user psychology. A resulting secondary innovation, the Wizard-of-OZ (WOZ) experiment is a valuable technique for simulating and building human–machine prototypes to ensure successful deployment of the completed service. The objective of the paper is to examine these innovations in relation to the changing business landscape; the technology and innovation literature, and the population of likely adopters. The review is carried out by placing the authors’ former experience as practitioners within current theoretical research frameworks. The result is a number of suggestions relating to both IT technology research and IT innovation research. Firstly, it proposes the simplification and diffusion of the WOZ methodology to support the growth in demand for automated e-business transactions that is mindful of human and ethical challenges. Secondly, the paper argues that because SST and business extends the traditional boundaries of the customer service function, it now needs to be incorporated into Swanson’s tri-core innovation typology. The paper concludes by presenting the suggested reorientation of information systems research that incorporates an outward facing perceptive as a conceptual model.

Published online 5 December 2006

Keywords: Wizard-of-OZ (WOZ) experiments; self-service technology (SST); automatic speech recognition (ASR); innovation typology; diffusion of innovations, information technology adoption

## Introduction

he growth and diffusion of self-service technology (SST) over the last decade has enabled an increasing number of business transactions to be completed without human assistance. This phenomenon has propelled human–computer interaction (HCI) considerations from the realm of specialised basic research to the mainstream of business information systems (IS) innovation. Furthermore, this development must be assessed within the current context of some scholars calling for a Copernican revolution in the way in which, organisations introduce and use information and communications technology (ICT) (Ciborra, 2002). As a result, there is a need for reflection on the current position of self-service business within the field of IS research and to provide an impetus for future development. This paper proposes to make a contribution by addressing the following questions: Where is self-service business located within the current topology of IS innovation research? What innovations within the field are worthy of diffusion among the broader research community? Who are the likely innovators – the primary early-adopters? This objective will be pursued by firstly providing an overview of SST business applications, in particular speech-enabled systems, and secondly, by placing it within recent developments in IS innovation and diffusion theory.

The paper now proceeds as follows. The next section provides an overview of the chosen problem domain: SST and self-service business systems. This is followed by a technical description of speech and language processing, which is treated as a primary innovation in the area of SST. Then the testing of speech-enabled systems, which is critical to the deployment of resilient applications, is presented. In particular, the focus is on a test methodology called Wizard-of-OZ (WOZ) experiments, which is viewed as a secondary innovation. The following section considers these phenomena within current innovation and diffusion theory debates, and includes a review of the diffusion of WOZ experiments in areas outside of speechenabled business applications. The next section proposes that the growth of business critical SST appeals for the wider dissemination of knowledge and expertise in WOZ experiments, and argues that Swanson’s topology of IS innovation types should be updated to specifically include self-service business. It also discusses the implications for this emerging area for the wider area of IT and IS research. Finally, suggestions for future research to address limitations with the WOZ technique are presented.

## Background

The increased deployment of SST in business to customer (B2C) transactions is being driven by the diffusion of ICT and the demand to move from high-cost manual transactions to low-cost automated self-service in enterprises and the public service. The Gartner Group have forecast that 70% of customer service contacts for information and remote transactions will be automated by the end of 2005 with an associated increase in investment in Web SST (Pujari, 2004). These services are becoming increasingly critical for enterprises challenged with providing e-commerce solutions and building relationships in a world where customer and vendor do not meet face-toface (Singh, 2002). Among SST interfaces, the use of speech is regarded as ideal because it is the most ‘natural, flexible, efficient and economic form of human-machine communication’ (Koumpis, 1998). However, creating conversational automated agents with responsibility for service levels and maintaining customer relationships is a complex challenge. Providing speech-enabled services requires capability in speech communication technologies, applications programming, and professional services developed in the environment of customer psychology and culture. Consequently, it is proposed that the implementation of such solutions brings together many features: cognitive, emotional, relational, and structural, which are relevant for the debate on the future direction of research in IT innovations. Also, it is argued that self-service business systems are a recent and increasingly important extension of the customer service functions in organisations, and by extension must be included in the typology of IS.

## Speech and language processing

Speech communication brings together a number of fields including: language processing, computational linguistics and psycholinguistics, voice technologies, grammar checking, and information retrieval (Jurafsky and Martin, 2000). Development of applications involve, dialog design, integration testing, data collection, tuning, and performance analysis resulting in expensive implementations. Gartner researchers have included Speech Recognition as one of the top 10 technologies that will have the biggest impact on enterprises in the period 2002–2007. Speech solution providers are citing high profile implementations including a UK bank, which is handling millions of calls per week and a US healthcare service with two million customers that has patients and physicians using its speech-enabled appointment facility (Nortel, 2005). However, it is worth noting that Speech Recognition has remained on the Gartner ‘Emerging Technologies Hype Cycle’ for the last 10 years (Gartner, 2005). Speech technologies include speech recognition, text-to-speech synthesis and speaker verification (authentication) which is a branch of biometrics. Recognition has evolved from initial basic discrete (isolated word) recognition to large vocabulary continuous speech recognition and natural language understanding. Figure 1 shows the main components of a typical conversational system (Zue and Glass, 2000). These systems can be speaker dependent as in the case of dictation products or speaker independent in the case customer service applications with large number of callers (Childers, 2000). The move to provide speech services via the Web is being facilitated by VXML (Voice eXtensible Mark-up Language), a standard of the World Wide Web Consortium (W3C, 2005), which allows conventional telephony interfaces such as IVR to evolve using voice gateways linked to a Web server.

## WOZ experiments

Three design principles proposed by Gould and Lewis (1985) to provide useful and easy-to-use computer systems, based on their study of the design of IBM’s Audio distribution system, are still relevant for designing contemporary dialogue services. These principles can be outlined as follows:

\- Early focus on users and tasks: the former by directly studying their cognitive, behavioural, anthropometric, and attitudinal characteristics: the latter by studying the nature of the work that is expected to be accomplished.

\- Empirical measurement using simulations and prototypes early in the process.

\- Iterative user testing to find and fix the problems.

A number of test methods are used to tune a speechenabled system: these include usability testing at various stages of the development process, focus groups, and piloting the service in a population of ‘friendly’ users. One technique developed to simulate human–computer dialogue systems is called a WOZ experiment, where a hidden human operator replaces the automated agent in order to experimentally investigate the usability of the system before being deployed in the field (McInnes et al., 1997). The WOZ is also known as a PNAMBIC (Pay No Attention to the Man BehInd the Curtain) system, where the human operator (the wizard) is disguised behind some interface software, and the caller thinks that they are interacting with an automated application. The concept originated from the 1899 book by Frank Baum and the 1939 MGM film where Dorothy, the Tinman, the Lion, and the Scarecrow follow the yellow brick road to Oz in order to make their requests to the awesome wizard. In the end, the awe-inspiring ruler of Oz turns out to be just a simulation controlled by a very ordinary human (Biberman et al., 1999). In WOZ experiments, the function of the wizard is played by a human but the user believes it is a computer. Figure 2 shows the typical architecture of a WOZ experiment designed to simulate a speech recognition application.

![](/api/attachments/JGJDQUYG/fulltext/images/a9f85b8ce1b47d2da1a367cad7aff8217975ec2d4c6cf614a254e2696ad50347.jpg)  
Figure 1 Generalised topology of a speech-enabled system.

The technique can provide data on the interaction, acoustic performance, language model, and semantics. It has the advantage of being able to test the proposed solution at an early stage of the development cycle as only the interface software and the databases are required. Other advantages include rapid iterations and the ability to compare a number of design solutions. However, as it is very difficult to cover all the errors, limitations, and constraints of the live application, the conclusions from WOZ experiments can to be rather idealised and even provide false-positive results (Jurafsky and Martin, 2000). Examples of in-house commercial use of the technique include the third-generation Wizard’s ANswering Device (WAND III), developed by Telia Research AB (Goldstein et al., 1999). In many cases, WOZ experiments are outsourced to specialist consultants. In connection with this, it is worth noting that research in the area of complex control software indicates that where development was outsourced, the testing process became significantly more difficult (Hunt, 1995). The present adopters of WOZ methodology can be approximately classified as follows:

![](/api/attachments/JGJDQUYG/fulltext/images/ef8bd07db22e48d5ac5427bbb38cb6d820373679c50087582719e63f8d294872.jpg)  
Figure 2 Typical architecture of a WOZ speech application experiment.

\- Practitioners: highly skilled applications developers of speech-enabled self-service (usually with software programming qualifications and experience).

\- Academics: usually involved in HCI research related to speech systems but increasingly exploring other areas such as graphical interfaces.

Having provided an overview of the business and technological setting, the next step will be to place it within the context of innovation literature.

## Theoretical considerations

In the previous section, this paper has described the emergence of a primary innovation (speech-enabled selfservice) and its relationship with a secondary innovation (WOZ experiments) during the design, and testing of B2C applications. This section will firstly review a number of theoretical frameworks that have had a major impact on the study of IS innovations in the period since the emergence of WOZ experiments in the HCI and computerised-speech literature (Fraser and Gilbert, 1991; Coutaz et al., 1993). Following this, a literature review of the diffusion of WOZ experiments will be presented.

## Diffusion of innovations

Rogers (2003) seminal work defined diffusion as the process by which ‘an innovation is communicated through certain channels over time among the members of a social system’. Furthermore, he classified adopters of innovation, developed during his doctoral research and first published in the Rural Sociology journal in 1958, into five major categories. This idealised taxonomy is approximately normally distributed over time and is summarised in Table 1.

It is important to note that, as pointed out in the work, the term ‘laggard’ is used as a classification and not pejoratively. Most related studies focus on diffusion among individuals, but it is interesting to note that he counsels the researcher to keep an open mind on other attributes that could be important in the adoption of unique innovations. When specifically addressing innovation in organisations, Rogers defines three types of innovation decisions:

\- Optional innovation decisions: choice is made by pro-active individuals within the organisation.

\- Collective innovation decisions: made by consensus.

Table 1 A presentation of Rogers’ adopter categories

<table><tr><td>Type</td><td>%</td><td>Attribute</td><td>Typical characteristics</td></tr><tr><td>Innovators</td><td>2.5</td><td>Venturesome</td><td>Control of substantial resourcesGate-keepers for complex technical knowledge</td></tr><tr><td>Early adopters</td><td>13.5</td><td>Role models</td><td>Widely respected opinion leaders</td></tr><tr><td>Early majority</td><td>34</td><td>Evaluators</td><td>Good social contacts but not leaders</td></tr><tr><td>Late majority</td><td>34</td><td>Sceptics</td><td>Motivated by economic necessity or peer pressure</td></tr><tr><td>Laggards</td><td>16</td><td>Suspicious</td><td>Lengthy decision processes; economically precarious</td></tr></table>

\- Authority innovation decisions: made by a minority having major influence due to power, status, or technical expertise.

In a review of the prolific growth in innovation literature, Wolfe (1994) concluded that it had made little contribution to the understanding of innovative behaviour in organisations and his evaluation of the results as being ‘inconclusive, inconsistent and characterised by low levels of explanation’ was surely an indictment of the field. To redress this situation, he made a number of recommendations including that more careful attention must be given to the ‘personal, organisational, technological and environmental contexts’ of the innovation phenomenon being studied. Moreover, he identified three streams of research that should branch from the swelling river of innovation studies:

1. Diffusion of innovation (DI): focused on the diffusion of an innovation over time and/or space.

2. Organisational innovativeness (OI): addressing the determinants of the innovativeness of organisation.

3. Process theory (PT): focused on the process of innovation within an organisation.

Further prescriptions for the malaise included moving the OI unit of analysis from the organisation itself to the ‘innovation-in-an-organisation’ and directing the research lens towards the examination of the features that influence the innovation process itself. Addressing the theoretical standpoint, the study proposed that a major source of promise was the widening of the research base to include more heterogeneous perspectives such as utilising interpretive methods. Two points are of particular interest here: firstly, the emphasis on multi-disciplinary research teams undertaking in-depth, inductive studies to provide greater insights and depth as well as the benefits of triangulation; and secondly, the need to differentiate primary from secondary innovation characteristics. However, this work perhaps should have provided more clarification between ‘OI’ and the ‘adoption of innovations by organisations’, which are not necessarily synonymous.

A later but similar interjection by Swanson (1994) argued that current innovation theory had done little to explain IS innovation and where it stood within the general debate on organisational innovation. To address this situation, he posited the following three types of IS innovation to provide a new theoretical impetus:

\- Type I: innovations confined to the IS task;

\- Type II: innovations supporting administration of the business; and

\- Type III: innovations imbedded in the core technology of the business.

To explain the concept, Swanson graphically presented this typology as a tri-core model of IS innovation with the innovation core sandwiched in a swiss-roll arrangement between the inner technical core and the outer administration core. A number of points in the model are important for this study. Firstly, the Type III category is further divided into three areas: Type IIIa-core technology process innovation such as Computer Integrated Manufacturing (CIM); Type IIIb-core technology product innovation such as Remote Customer Order Entry; and Type IIIc-core technology integration innovation such as Electronic Data Interchange. This begs the suggestion whether speechenabled self-service systems could be accommodated within an additional Type IIId classification due to relatively recent diffusion of this technological innovation. Secondly, the point is made that the cascading consequences of new technological developments can have far-reaching implica tions for IS innovations. Thirdly, he argues that it may not be sufficient to study IS innovations individually but bundled with associated innovations. Fourthly, the conclusion that there is a need for longitudinal studies that give due consideration to the institutional supports and constraints of the technological process is noteworthy. A subsequent empirical testing of the model resulted in ‘cautious optimism’ but suggested a need for further theoretical work to refine, elaborate, and extend the system (Grover et al., 1997). The implications for the emerging areas of self-service business on this typology of innovation types will be discussed later. In a more recent and influential paper, Swanson and Ramiller (2004) start by defining IT innovation as the process by which ‘IT comes to be applied in novel ways’ and conclude that the literature on bandwagon phenomena indicate that much supposedly innovative behaviour is actually ‘me too’ activities . This leads them to propose the application of the concepts of ‘mindfulness’ and ‘mindlessness’ to IT innovation theory. Their call for an enlarging of the IS academic research to ‘investigate the cognitive processes of organisations’ and to engage with the psychological as well as the organisational literature has relevance for the present discussion. Furthermore, their suggestion that studies should be undertaken to investigate how organisation (and by extension people) cope with the unexpected when dealing with a new IT application is particularly pertinent to automated business transactions. Fichman (2004) takes the concept of ‘mindfulness’ with six others (innovation configurations, social contagion, management fashion, technological destiny, quality of innovation, and performance impacts) and presents them as emerging perspectives that can take IT innovation research beyond its present ‘dominant paradigm’, which he believes is showing signs of exhaustion. He defines the ‘dominant paradigm’, derived from economic–rationalistic models, as positing that an organisation with the greater quantity of ‘Right Stuff’ will demonstrate a greater quantity of innovation and illustrates the concept diagrammatically. In his study, Fichman firmly pledges his allegiance to positivism, despite some of the rather interpretivistsounding constructs included above, so it is suggested that there should be no objection to attempting to represent the dominant paradigm as an equation.

$$
Q _ {I} = \alpha Q _ {R S}\tag{1}
$$

where $Q _ { I }$ is the quantity of innovation adoption – the dependant variable, $Q _ { R S }$ is the quantity of ‘Right stuff’ (innovation profile) – the independent variable, and a is the coefficient of innovativeness.

However, in a conciliatory gesture, he concedes that some extra-positivistic areas such as socio-technical approaches could assist in the overall objective of ‘breaking the dominant paradigm’.

Recently, a comprehensive analysis of an extensive body of research, based on Fichman’s description of the ‘dominant paradigm’, resulted in a revised depiction of the model that differentiated between individual and organisational characteristics, and prescribed the best predictors of IT adoption for each characteristic (Jeyaraj et al., 2006). This study concluded with a counter argument that the dominant IT paradigm was alive and well, and continues to make significant progress.

## Diffusion of WOZ

In the previous sections, this paper has described the relationship between a primary innovation (speech-enabled self-service) and a secondary innovation (WOZ experiments) during the design and testing of B2C applications, such as a mobile-phone city guide service (Howell et al., 2005). Now, a number of research projects aimed at applying the methodology to other areas will be presented. Yang et al. (2000) have applied WOZ to the development of a learning interface agent in order to make the system more natural, intelligent, and even emotional. In another context, a WOZ experiment has been extended to involve a robotic interface that is capable of simulating a number of different social behaviours (deRuyter et al., 2005). The procedure has shown that the development of an artificial intelligence (AI) interface to provide ‘active help’ has benefited system users (Davis, 1998). Wider applications of the method include collection of empirical data on mathematics tutorials in German (Benzmu¨ller et al., 2003). One of the most novel implementations was the Neimo project that extended the WOZ technique to the study of multi-modal systems and provides evidence that the methodology can be broadened to designing, building, and evaluating services that allow the use of combined input media (Salber and Coutaz, 1993). Another area of research has focused on simplifying both the data collection function and the model building that presently makes implementation of the methodology time consuming and expensive (Munteanu and Boldea, 2000). A system called DiaWoZ has been designed to collect data in the complex domain of tutorial dialogues between university students and a mathematical tutoring system. The architecture places emphasis on modularity and clear interface requirements that allows for the progressive refinement of consecutive WOZ experiments (Fiedler and Gabsdil, 2002). In Sweden, an Ozlab is extending research of the WOZ technique to the manual prototyping of interactive graphical user interfaces (Pettersson, 2002). The objective of this pioneering project was to explore the practicality of allowing educationalists, with no programming experience, develop examples of multi-media applica tions to assist people with language disabilities. However, in spite of the implementation of the above applications, the evidence from the literature is that the technique is still very much in the realm of the innovator.

## A note on the research methodology

This paper emerged from the authors’ experience of new product introduction and product lifecycle management in the ICT industry during the 1990s. At the end of this period, there was a realisation that the main challenge was not the maturity of the underlying speech and language-processing technologies, but the development and deployment of robust customer solutions. This practitioner viewpoint has since been informed by the technical and innovation literature together with the perspective that serving an apprenticeship in academic research brings. It is suggested, hopefully without in any way sounding supercilious, that such a background provides a basis for the inductive extension of theory, suggested later in this work, in order to contribute something to the research and practitioner community. However, it is recognised that the arguments are rather limited due the lack of empirical or other evidence. Also, the authors are conscious that the juxtaposition of IT and IS in the text may grate on the finely tuned ear. Here, the only defence offered is to recall the last line of Yeats’ poem ‘Among Schoolchildren’ and propose that in some such situations ‘How can we know the dancer from the dance?’

## Discussion

Now, the paper will examine the implications of the preceding discussion for both IT research and the theoretical study of these innovations. Business analysts are predicting the continued rapid growth in automated ICT applications and deployment of SST. These services bring together leading edge technologies, the psychology of human–machine interaction, business processes, and the management of customer contacts. The resilience of the solution is critical in an environment where customer relationship management is being entrusted to a computer application and network. The focus on end-user-driven development is posing questions on how to overcome traditional barriers between the user and the developer (Pettersson, 2003), and how to assess interactive technology using a human reference standard (Cox et al., 1998). All of these challenges are presently being encountered in the deployment of speech-enabled business applications, which are currently limited to expensive implementations in verticals such as financial services, telecommunications and healthcare. WOZ experiments provide an effective early prototype environment to test interactions between humans and voice applications. The methodology requires a multidisciplinary approach bringing together psychology, culture, and technology as well as fields such as synthetic computer characters that look at making humanoid agents lifelike (Thorisson and Cassell, 1996). However, the technique needs to be diffused to a larger community especially through education, currently only being addressed on a small scale, for example, by Liberman (2005). Future cross-disciplinary research is required to simplify WOZ experiments and address the weaknesses outlined above to enable the diffusion of the methodology to the wider area of SST and automated Web services.

Based on this analysis, it is proposed that the diffusion of WOZ experiments will benefit research by providing a platform to contribute knowledge on the phenomenon of anthropomorphic business systems and assist practitioners with the human challenges resulting from the growing demand to implement such systems. Figure 3 presents the concept of multiple interfaces to a WOZ environment that is Internet Protocol-(IP) enabled and supported by a flexible development toolset, for instance, a ‘wizard’ for wizards. The proposed topology also includes the generation of statistical data for performance analysis of the design.

Challenges include language and cultural localisation, cost-effective implementation, accessibility, and ethical considerations of using people in usability testing. The last point is of particular importance in research that involves vulnerable populations such as children and people with special needs (Pettersson, 2002). In terms of the broader research and educational agenda, the wonderful WOZ has become a popular teaching tool in the area of economics, although not without some concerns on the danger of reading to much into the story (Hansen, 2002). Some scholars would go so far as to say the story is an allegorical commentary on the politics and economics of the era in which it was set (Rockoff, 1990), but this argument is contentious. In a debate within the corporate ethics literature, Kerlin (1997) uses the WOZ story to develop an argument that challenges the prevailing wisdom that a group or organisation can be treated as a moral agent per se. His metaphysical thesis is that business ethics is the responsibility of the people that make the decisions and not some abstract corporate entity. Such philosophical reflection has surely become relevant in the light of recent high-profile business scandals and could instigate debate on the rationale for differentiation between individual and organisational innovations in the area of IT and IS.

The second area the paper addresses is the implication for this study on the development of concepts and hypotheses related to IT and IS innovations. It is argued that the present tri-core typology of IS innovations in organisations must re-align its focus outside of the host organisation itself due to increasing ether-shoring of customer interactions to self-service systems. This proposed extension of Swanson’s typology is presented in two ways: firstly, Figure 4 re-fashions the present triangle of technology, IS, and administration to a diamond shape. The aim is to illustrate the proposal that IS research develops an extra-organisational focus which, like Janus, must also face outwards to the customer transaction itself now being instantaneously transported to the digital front-door via broadband ICT.

The resulting extension of the typology of innovation types to include a Type IIId classification is shown in Table 2 with the addition shown in bold. It is argued that the innovations discussed previously, have implications for the technological and business core that encompass both product and process.

It is perhaps worth making a comment on predictors of adoption at this juncture, in particular the prevalence of ‘Top Management Support’ as a best indicator of acceptance by both individuals and organisations (Jeyaraj et al., 2006). The decision to employ a test technique is almost universally made by the technical professionals in conjunction with their functional manager operating with the product development and/or operations organisations. Therefore, it is suggested that seeding the knowledge of the technique must be directed toward this present population and its future members (hence the importance of being included in computing, IS, IT and engineering curricula). Using Rogers’ taxonomy, outlined previously, adoption of the technique would be viewed as an ‘authority innovation-decision’ made by professionals having specialised technical expertise.

Figure 3 Future work on multiple input WOZ toolset.  
![](/api/attachments/JGJDQUYG/fulltext/images/d09b87589b0efe129f7c63a75952e8eaff7253dfafb97f0f0c9c8ec7962e6ecc.jpg)  
Figure 4 Expanding the perspective of IS innovation types.

Table 2 Proposed addition to table of innovation types (Swanson, 1994: 1076)

<table><tr><td>Innovation type</td><td>Description</td><td>Illustrations</td></tr><tr><td>Type IIIa</td><td>IS product and business technology process innovation</td><td>Material Requirements Planning (1950s and 1960s)Computer Integrated Manufacturing (1980s and 1990s)</td></tr><tr><td>Type IIIb</td><td>IS product and business product innovation</td><td>Airline Reservation Systems (1970s and 1980s)Remote Customer Order Entry and Follow-onCustomer Service Systems (1980s)</td></tr><tr><td>Type IIIc</td><td>IS product and business process innovation</td><td>Inter-organizational Information Systems (1990s)Electronic Data Interchange (1980s and 1990s)</td></tr><tr><td>Type IIId</td><td>IS product and business technology product and process innovation</td><td>Self-service business systems (1990s)Speech-enabled business systems (1990s and 2000s)</td></tr></table>

## Conclusions

This paper has explored the implications for the recent rapid development of self-service business systems and related technological developments for IT and IS innovation research. The business factors driving the growth in automated e-business solutions were first described. An overview was given of the complexity of speech and language processing and the skills required to deploy voice enabled B2C services while managing customer relationships. The important part played by WOZ experiments for the early simulation and testing of such systems was illustrated. Examples were provided of research into the dissemination of the methodology beyond present expensive customer contact solutions. It was argued that the increasing demand for resilient automated e-business and the associated capability to integrate enduser psychology with technology calls for the wider diffusion of WOZ techniques. Future work is proposed in a number of areas: the re-orientation of IT research from the system to the human person, the development of the technology itself, the adopters of the technology, the role of education in the DI to technical professionals, the relationship between a primary and secondary innovation and the resulting broader ramification for theoretical frameworks.

For example at the technological level , the need to simplify and automate the method to bring it to a wider audience and address concerns with the validity and reliability of results is stressed. B2C self-service applications of the future will, like the Tinman, need to have a heart. Furthermore it was proposed that these innovations had consequences for the present theoretical framework of innovation research and that the radical shift brought about by self-service systems requires accommodation within the current research typology. It is hoped that fears in some quarters of congestion in IT/IS innovation research will be at least slightly allayed by this proposal to widen the yellow brick road.

## Acknowledgements

We thank the IFIF8.6 2006 editorial team for their very enlightening comments on a previous version of this paper. We also acknowledge our many former colleagues in the ICT industry who indirectly provided such a rich experience from which this paper emerged.

## References

Benzmu¨ller, C., Fiedler, A., Gabsdil, M., Horacek, H., Kruijff-Korbayova´, I., Pinkal, M., Siekmann, J., Tsovaltzi, D., Vo, B.Q. and Wolska, M. (2003). A Wizard-of-Oz Experiment for Tutorial Dialogues in Mathematics, in V. Aleven, U. Hoppe, J. Kay, R. Mizoguchi, H. Pain, F. Verdejo, and K. Yacef (eds.) AIED2003 – Supplementary Proceedings of the 11th International Conference on Artificial Intelligence in Education, Vol. VIII, Advanced Technologies for Mathematics Education. Sydney: Australia, pp. 471–481.

Biberman, J., Whitty, M. and Robins, L. (1999). Lessons from Oz: Balance and wholeness in organisations, Journal of Organizational Change 12(3): 243–254.

Childers, D.G. (2000). Speech Processing and Synthesis Toolboxes, New York: John Wiley & Sons.

Ciborra, C. (2002). The Labyrinths of Information: Challenging the Wisdom of Systems, Oxford: Oxford University Press.

Coutaz, J., Salber, D. and Balbo, S. (1993). Towards Automatic Evaluation of Multi-Modal User Interfaces, Knowledge-Based Systems 6(4): 267–274.

Cox, S.J., Linford, P.W., Hill, W.B. and Johnson, R.D. (1998). Towards Speech Recognizer Assessment Using a Human Reference Standard, Computer Speech & Language 12: 375–391.

Davis, J.S. (1998). Active Help Found Beneficial in Wizard of Oz Study, Information and Software Technology 40: 93–103.

deRuyter, B., Saini, P., Markopoulos, P. and van Breemen, A. (2005). Assessing the Effects of Building Social Intelligence in a Robotic Interface for The Home, Interacting with Computers 17(5): 522–541.

Fichman, R.G. (2004). Going Beyond the Dominant Paradigm for Information Technology Innovation Research: Emerging concepts and methods, Journal of the Association for Information Systems 5(8): 314–355.

Fiedler, A. and Gabsdil, M. (2002). Supporting Progressive Refinements of Wizard-of-Oz Experiments, in C.P. Rose´ and V. Aleven (eds.) Proceedings of the ITS2002 — Workshop on Empirical Methods for Tutorial Dialogue Systems, Spain: San Sebastian, pp. 62–69.

Fraser, N.M. and Gilbert, G.N. (1991). Simulating Speech Systems, Computer Speech & Language 5(1): 81–99.

Gartner (2005). Gartner Highlights Key Emerging Technologies in 2005 Hype Cycle [WWW document]www.gartner.com (accessed 31st October 2005).

Goldstein, M., Bretan, I., Sallna¨s, E.-L. and Bjo¨rk, H. (1999). Navigational Abilities in Audial Voice-Controlled Dialogue Structures, Behaviour & Information Technology 18(2): 83–85.

Gould, J.D. and Lewis, C. (1985). Designing for Usability: Key principles and what designers think, Communications of the ACM 28(3): 300–311.

Grover, V., Fiedler, K. and Teng, J. (1997). Empirical Evidence on Swanson’s Tri-Core Model of Information Systems Innovation, Information Systems Research 8(3): 273–287.

Hansen, B.A. (2002). The Fable of the Allegory: The wizard of oz in economics, Journal of Ecomomic Education 33(3): 254–264.

Howell, M., Love, S. and Turner, M. (2005). The Impact of Interface Metaphor and Context of Use on the Usability of a Speech-Based Mobile City Guide Service, Behaviour & Information Technology 24(1): 67–78.

Hunt, J. (1995). Testing Control Software using a Genetic Algorithm, Engineering Applications of Artificial Intelligence 8(6): 671–680.

Jeyaraj, A., Rottman, J.W. and Lacity, M.C. (2006). A Review of the Predictors, Linkages, and Biases in IT Innovation Adoption Research, Journal of Information Technology 21: 1–23.

Jurafsky, D. and Martin, J.H. (2000). Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition, New Jersey: Prentice-Hall Inc.

Kerlin, M.J. (1997). Peter French, Corporate Ethics and The Wizard of Oz, Journal of Business Ethics 16: 1431–1438.

Koumpis, K. (1998). Corporate Technological Positioning in Automatic Speech Recognition and Natural Language Processing, Master of Science Dissertation, Science and Technology Policy Research (SPRU), University of Sussex.

Liberman, H. (2005). Intelligent Interface Agents, [WWW document]http:// www.media.mit.edu/lieber/(accessed 3rd November 2005).

McInnes, F.E., Jack, M.A., Carraro, F. and Foster, J.C. (1997). User Responses to Prompt Wording Styles in a Banking Service with a Wizard-of-Oz Simulation of Word-Spotting, IEE Colloquim on Advances in Interactive Response Technologies for Telecommunications Services. IEE Digest No. 1997/147 PP. 7/1–6.

Munteanu, C. and Boldea, M. (2000). MDWOZ: A Wizard of Oz Environment for Dialog Systems Development, Second International Conference on Language Resources and Evaluation-LREC 2000, Athens, Greece.

Nortel (2005). Position Paper: The power of speech [WWW document]www. nortel.com(accessed 1st November 2005).

Pettersson, J.S. (2002). Visualising Interactive Graphics Design for Testing with Users, Digital Creativity 13(2): 144–156.

Pettersson, J.S. (2003). Prototyping Interactivity before Programming, Position paper to the workshop on End User Development, Conference on Human Factors in Computing Systems (CHI 2003).

Pujari, D. (2004). Self-Service with a Smile?: Self-service technology (SST) encounters among Canadian business-to-business, International Journal of Service Industry Management 15(2): 200–219.

Rockoff, H. (1990). The ‘Wizard of Oz’ as a Monetary Allegory, Journal of Political Economy 98(4): 739–760.

Rogers, E.M. (2003). Diffusion of Innovations, 5th edn New York: Free Press.

Salber, D. and Coutaz, J. (1993). Applying the Wizard of Oz technique to the Study of Multimodal Systems, in L.J. Bass, J. Gornostaev and C. Unger (eds.) Human–Computer Interaction Selected Papers, Lecture Notes in Computer Science, no. 753, Berlin: Springer-Verlag, pp. 219–230.

Singh, M. (2002). E-Services and their Role in B2C e-commerce, Managing Service Quality 12(6): 434–446.

Swanson, E.B. (1994). Information Systems Innovation among Organisations, Management Science 40(9): 1069–1092.

Swanson, E.B. and Ramiller, N.C. (2004). Innovating Mindfully with Information Technology, MIS Quarterly 28(4): 553–583.

Thorisson, K. and Cassell, J. (1996). Why put an agent in a body: The importance of Communicative Feedback in Human–Humanoid Dialogue. Lifeline computer Characters ‘96, Snowbird, Utah.

W3C (2005). World Wide Web Consortium (W3C): Voice Extensible Markup Language (VoiceXML) Version 2. [WWW document].http://www.w3.org/ (accessed 1st November 2005).

Wolfe, R.A. (1994). Organizational Innovation: Review, critique and suggested research directions, Journal of Management Studies 31(3): 405–431.

Yang, Y., Okamoto, M. and Ishida, T. (2000). Applying Wizard of Oz Method to Learning Interface Agent, IEICE Trans Fundamentals E00-A(1): 223–230.

Zue, V.W. and Glass, J.R. (2000). Conversational Interfaces: Advances and challenges, Proceedings of the IEEE, August 2000 Special Issue on Spoken Language Processing 88: 1166–1180.

## About the authors

Gabriel J. Costello is a lecturer in engineering at the Galway-Mayo Institute of Technology, Galway, Ireland since 2001. Prior to this, he worked for 20 years in the telecommunications industry with Nortel where he held engineering, new product introduction, and product line management positions. Presently, he is undertaking a Ph.D. in the Business Information Systems Group, National University of Ireland, Galway. Research interests include: innovative enterprises, Speech-enabled self-service IT systems, and using IS to support RUE (rational use of energy) in organisations.

Dr Brian Donnellan is a lecturer in the Cairnes Postgraduate School of Business and Public Policy in the National University of Ireland, Galway (NUIG). Prior to joining NUIG faculty, he spent 20 years working in industry. Dr Donnellan is one of the research project leaders in The Centre for Innovation & Structural Change (CISC), an interdisciplinary research centre in NUIG where he is responsible for the ‘Inter-Organizational Systems’ research stream. His research interests lie primarily in the area of innovation systems, a broad area that encompasses knowledge management, new product development, and technology management.
