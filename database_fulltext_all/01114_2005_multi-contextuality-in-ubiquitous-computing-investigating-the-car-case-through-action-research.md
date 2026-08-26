---
otero_id: 1114
otero_key: "EQWCDKFJ"
title: "Multi-contextuality in ubiquitous computing: Investigating the car case through action research"
authors: "Ola Henfridsson; Rikard Lindgren"
year: "2005"
journal: "Information and Organization"
doi: "10.1016/j.infoandorg.2005.02.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Multi-contextuality in ubiquitous computing: Investigating the car case through action research

Ola Henfridsson <sup>\*</sup>, Rikard Lindgren <sup>1</sup>

Viktoria Institute, Ho¨ rselga˚ ngen 4, 417 56 Go¨ teborg, Sweden

Accepted for publication 22 February 2005

## Abstract

Ubiquitous computing envisions seamless access of mass-scale services over the multitude of contexts that users encounter in their everyday mobility. However, to be successful such computing must simultaneously be designed to provide transparent, integrated, and convenient support in localized use contexts. Thus, the issue of multi-contextuality makes the design of ubiquitous computing services and environments a challenging endeavor. While ubiquitous computing requires attention to the multi-contextuality of peoples mobile device use encompassing spatial, temporal, and social dimensions of mobility, the typical avenue for IS research studies has been the single context (e.g., team, organization, or inter-organizational).

This paper reports on a grounded action research study with the objective of developing and testing design principles for handling multi-contextuality in an increasingly important ubiquitous computing environment – the car. Already supporting peoples everyday mobility and promising to provide ubiquitous availability of computing and communication infrastructure, the car is indeed a relevant setting for investigating the co-existence of diferent use contexts in ubiquitous computing. Contributing to the early stage of the ubiquitous computing research tradition, this paper not only empirically demonstrates that the car as a ubiquitous computing environment can improve the convenience of peoples everyday mobile device use by providing multi-contextual support. The paper also suggests our design principles and their associated socio-technical implications to be valid for other ubiquitous computing environments. Indeed, synchronizing fluid use patterns, scaling service manipulation, and signaling context-switches through awareness support lie at the heart of weaving ubiquitous computing environments conveniently into the fabric of peoples everyday mobility.

 2005 Elsevier Ltd. All rights reserved.

## 1. Introduction

Ever since Weiser (1991) coined the term ‘‘ubiquitous computing’’ some 13 years ago, increasing attention has been paid to technologies that provide seamless support to people on the move. While many have discussed such technologies in work settings (e.g., Fagrell, Ljungberg, & Kristofersen, 1999; Luf & Heath, 1998), others have highlighted the emergence of border-crossing use patterns in diferent instances of contemporary life (Cerf, 2001; Kleinrock, 2001). Enabled by the increasing miniaturization and connectivity of mobile devices, such use patterns are established over traditionally bounded use contexts (Makimoto & Manners, 1997).

Driven by increased mobility, digital convergence, and mass-scale devices and services (Lyytinen & Yoo, 2002), ubiquitous computing envisions seamless service access over the multitude of contexts that users encounter in their everyday life. At the same time, however, such computing must be designed to provide transparent, integrated, and convenient support in localized use contexts (Kleinrock, 2001). Because such use contexts typically vary in nature, multi-contextuality is challenging for anyone wishing to design useful services in ubiquitous computing environments.

The problem of multi-contextuality, i.e., the co-existence of diferent use contexts, is unique to ubiquitous computing. While the typical avenue for IS research studies is the single context (e.g., team, organization, or inter-organizational), ubiquitous computing requires attention to the multi-contextuality of peoples mobility. In fact, mobility that spans multiple contexts lays at the heart of weaving ubiquitous technologies into the fabric of everyday life (Weiser, 1991). As suggested by Lyytinen and Yoo (2002), this fact challenges IS researchers in their attempts to investigate phenomena that emerge when social and technical systems interact. For example, the pace of technological change calls for research alliances with those who drive that change. Asserting this, Lyytinen and Yoo (2002, p. 387) recommend that ‘‘IS researchers should be actively involved in studies where technologies are being built and tried out – not after the fact when they enter the market’’. In this way, IS researchers are better positioned to understand how the entanglement of socio-tech nical elements shapes our ubiquitous future.

An important element in information systems design is to identify user requirements associated with specific classes of systems (Markus, Majchrzak, & Gasser,

2002). In this vein, our paper addresses socio-technical design implications related to the coexistence of multiple contexts in an increasingly important ubiquitous computing environment – the car. Indeed, the car supports spatial mobility of people. As an example, 88% of US workers use the car as their means of transportation to work (Pucher & Renne, 2003). Because mobility often is associated with communication and coordination (Bellotti & Bly, 1996; Luf & Heath, 1998), it is therefore not surprising that the car also is a setting in which the use of mobile devices is frequent and increasing (Lamble, Rajalin, & Summala, 2002; Towers, 2002). In fact, using mobile devices in the car is a way to handle the temporality of our social activities related to both professional and private life (cf. Kakihara & Sørensen, 2002). The car is also expected to provide advanced computing and connectivity capabilities (Walker, Stanton, & Young, 2001). Equipped with computing platforms, input/output resources, as well as network technologies such as Bluetooth and WLAN, the future car has been described as a sit-in mobile device (May, 2001). Going in this direction, BMW and Saab Automobile, for example, recently launched car models with integrated Bluetooth support that enables connections to external mobile devices. This new technology not only promises to provide sophisticated in-car support for temporal mobility but can also come to support spatial context-switching between the car and outside contexts (Henfridsson, Wiberg, Lindgren, & Ljungberg, 2005).

To address the problem of multi-contextuality, we embarked on a 24-month grounded action research study (Baskerville & Pries-Heje, 1999) involving academics from the Viktoria Institute and practitioners from a car manufacturer (Saab Automobile), an automotive systems integrator (Mecel), and a mobile network operator (Vodafone). With its emphasis on both immediate problem-solving and empirically based knowledge generation, the grounded action research method resonates well with the need for up-close examination and active involvement in ubiquitous computing research (cf. Lyytinen & Yoo, 2002). Building on this action research study, the objective of this paper is to develop and evaluate design principles for handling multi-contextuality surrounding mobile device use in cars. Apart from outlining these principles and their associated socio-technical implications, the paper also provides a discussion of the generality of our findings beyond the car context.

The remainder of the paper is structured as follows. First, we review the literature on mobility in ubiquitous computing for developing a theoretical understanding of multi-contextuality. This is followed by a methodology section that describes our action research design as well as our data collection and analysis. Then, we diagnose multi-contextuality in practice by presenting empirical categories and concepts generated from a grounded analysis of mobile phone use in cars. On the basis of this analysis, section five generates design principles for handling multi-contextuality associated with mobile device use in the car context. Section six describes a prototype system – SeamlessTalk – that we developed for testing our design principles in a realistic use context. The following sections analyze empirical findings from the prototype evaluation, assess their implications for research and practice, and discuss the generality of our results beyond the car context. Finally, we conclude the paper with a summary of our findings and directions for future research on multi-contextuality in ubiquitous computing.

## 2. Multi-contextuality in ubiquitous computing

Already encompassing highly mobile aspects of peoples everyday life (Pucher & Renne, 2003) and promising to provide ubiquitous availability of computing and communication infrastructure (Bisdikian et al., 2002), the car can be seen as a ubiquitous computing environment, i.e., ‘‘a heterogeneous assemblage of interconnected technological and organizational elements, which enables the physical and social mobility of computing and communication services between organizational actors both within and across organizational borders’’ (Lyytinen & Yoo, 2002, p. 378). Indeed, drivers towards ubiquitous computing environments such as increased mobility, digital convergence, and mass-scale devices and services (Lyytinen & Yoo, 2002) have recently been recognized in the automotive industry. Given the increasing penetration of mobile devices with open standard communication protocols, for instance, many car manufacturers have developed so-called personal telematics strategies that integrate the computing power of external devices with embedded computer and communication platforms (Fuchs, 2003). Thus, they not only align their eforts with the installed base of mobile devices and services in order to become part of a positive standards reinforcement mechanism (cf. Grindley, 1995) but they also acknowledge the multi-contextual nature of in-car mobile device use.

As recognized in recent mobility studies (Kakihara & Sørensen, 2002; Wiberg & Ljungberg, 2001), however, anytime-anywhere computing does not come without constraints. Even though our modern society transforms time-space dimensions (Giddens, 1990), ubiquitous computing users are still actors in spatio-temporal contexts enabling and restricting their mobility and interaction in diferent ways. This complicates the design of transparent, integrated and convenient ubiquitous computing support in localized use contexts. To be sure, the problem of multi-contextuality in ubiquitous computing is pressing.

In its crudest form, mobility can be seen as the physical movement between different locations. Much application-centered ubiquitous computing research focuses on spatiality because location forms the basis for adapting services to the situation in which users find themselves (Abowd & Mynatt, 2000). Following this, multicontextuality would be defined as the co-existence of diferent physical environments that ubiquitous users encounter. Clearly, spatial contexts such as the car, department store, home, and ofice influence the physical conditions under which ubiquitous computing services can be used (cf. Kristofersen & Ljungberg, 1998). Using the term ‘‘locales’’, Giddens (1984, p. 375) refers to such spatial contexts as the physical regions ‘‘. . .involved as part of the setting of interaction, having definite boundaries which help to concentrate interaction in one way or another’’.

Despite the centrality of physical environments of interaction, however, context is ‘‘. . .not something merely -in which interaction occurs’’ (Giddens, 1984, p. 71).

Mobility is also always positioned within a network of established social interactions (Jessup & Robey, 2002). Given the pervasiveness of ubiquitous technologies such as mobile phones, a particular users social interaction will vary with the enacted identity of a given situation (parent, co-worker, manager, or client). As Abowd and Mynatt (2000) highlight, the variety of social settings in which ubiquitous technologies are used makes their design dificult. The abundance of applications focusing on users location as the mere context impetus exemplifies this dificulty (Schmidt, Beigl, & Gellersen, 1999).

Apart from spatial and social dimensions of mobility, the temporality of social activity changes with seamless service access across diferent contexts (Kakihara & Sørensen, 2002). In particular, mobility seems to increase the pace of social activity (Dahlbom & Ljungberg, 1998). Increased mobility leads to more physical and social encounters both within (Dahlberg, Ljungberg, & Sanneblad, 2002) and outside the workplace (Tofler, 1970). This multitude of encounters breaks with the often taken-for-granted sequential nature of our everyday life. As suggested by Kakihara and Sørensen (2002), ubiquitous technologies facilitate polychronicity in that a given time period may not necessarily be shared with co-located people (cf. Lee, 1999). For instance, a mobile phone can be used to coordinate a household matter in the middle of a sales group meeting taking place in a car between home ofice and customer site. Indeed, new information technology afects the temporal order of everyday life and work (Barley, 1988).

Our literature review suggests that multi-contextuality in ubiquitous computing comprises variety over three dimensions (spatiality, social setting, and temporality). This variety is challenging for those who seek to design ubiquitous computing services and environments that are transparent, integrated, and convenient in situated use contexts. Beyond the single context setting characterizing the typical IS research endeavor, it is therefore vital to explore the consequences of multi-contextuality for ubiquitous computing design and use. As indicated earlier, the car is a relevant setting for such exploration in that it encompasses all three dimensions. Looking at the specific literature on mobile device use in cars, however, cars are primarily viewed as spatial locations with specific physical properties in which use of mobile technology endangers driving. The literature mostly concentrates on human-machine interaction aspects (e.g., Salvucci, 2001) and implications of mobile phone usage on driving behavior (Alm & Nilsson, 1995; Brookhuis, De Vries, & De Waard, 1991; Goodman, Tijerina, Bents, & Wierwille, 1999; Redelmeier & Tibshirani, 1997). In this way, this research both underestimates the ability of users to compensate for dangerous trafic situations (Esbjo¨rnsson & Juhlin, 2003) and oversees the multi-contextuality of mobile device use.

Informed by this literature review, we present an action research study that investigates the multi-contextuality surrounding mobile device use in cars. As part of this presentation, we develop and evaluate design principles for handling multi-contextuality that would improve the possibilities of transparent, integrated, and convenient ubiquitous computing in this particular ubiquitous computing environment. In the next section, we outline the action research methodology used for investigating multi-contextuality in the car case.

## 3. Research method

## 3.1. Research design

The action research reported in this paper was conducted between July 2002 and June 2004. The project was a collaborative study involving the Viktoria Institute (Go¨teborg, Sweden) and three firms operating in the automotive industry: Mecel (automotive systems integrator), Saab Automobile (car manufacturer), and Vodafone (mobile network operator). The first author of this paper acted as the project manager. Following Robey and Markus (1998) recommendation that practitioner sponsorship should be pursued to help overcome the commonly perceived rigor and relevance trade-of, the project was equally funded by the Swedish research funding agency VINNOVA (www.vinnova.se) and the participating organizations.

The research methodology used was that of grounded action research (Baskerville & Pries-Heje, 1999). Being a type of canonical action research (Davison, Martinsons, & Kock, 2004; Susman & Evered, 1978), the grounded action research method is characterized by its cyclical process model, rigorous structure, collaborative researcher involvement, and primary goals of organizational development and scientific knowledge (Baskerville & Wood-Harper, 1998). In addition, it represents a rigorous approach to theory formulation (Baskerville & Pries-Heje, 1999). Using the data analysis techniques of grounded theory (Strauss & Corbin, 1990), the grounded action research method complements practical intervention with an inductive and systematic method to generate qualitative and empirically validated insights. Since the investigation of ubiquitous computing requires up-close examination and active involvement on behalf of the researchers (Lyytinen & Yoo, 2002), the empirically solid and systematic nature of our chosen method combined with its emphasis on practical problem-solving can be considered particularly useful in this research.

Our grounded action research followed Susman and Evereds (1978) five traditional action research phases: diagnosing, action planning, action taking, evaluating, and specifying learning (see Table 1 for a summary of how our action research compares to these phases). Diagnosing refers to the joint (researcher and practitioner) identification of situated problems and their underlying causes. As a result of this phase, a working hypothesis of the research phenomenon is formulated as to guide the research to be done in the subsequent phases. Our diagnosing phase started with a series of project meetings and collaborative brainstorming sessions focusing on the role of mobile devices (such as mobile phones, smartphones, or handheld computers) in cars. This decision directed us to the ubiquitous computing literature and questions related to multi-contextuality in mobile phone use. On the basis of an interview study of mobile phone use, categories and concepts depicting typical aspects of mobile phone use in cars were outlined and linked to aspects of multi-contextuality. A working hypothesis was formulated based on this analysis.

Action planning is the process of specifying actions that can improve the problem situation. In collaboration with the practitioners, our action planning generated a set of design principles for handling multi-contextuality associated with mobile phone use in cars. Consistent with the selective coding technique of grounded theory (Strauss

<table><tr><td>AR Cycle (July 2002 to June 2004)</td></tr><tr><td>Research CollaboratorsViktoria InstituteMecelSaab AutomobileVodafone</td></tr></table>

Table 1 Summary of our action research project

## Phase 1. Diagnosing

Over a series of project meetings and workshops, we explored the future role of mobile devices (such as mobile phones, smartphones, or handheld computers) in cars. This decision directed us to the ubiquitous computing literature and questions related to multi-contextuality in mobile phone use. In order to better understand multi-contextuality in practice, an interview study was designed to identify and explore existing patters of mobile phone use in cars

As an outcome of the diagnosing phase including workshop sessions, technology review, and interview study, we formulated the following working hypothesis: the car as a ubiquitous computing environment can improve the convenience of peoples everyday mobile device use by providing multi-contextual support Data sources

 18 semi-structured interviews with IT professionals and frequent mobile phone users

 Technology review

 Workshop sessions

## Data analysis

The data collected through the interview study was analyzed using the open and axial coding techniques of grounded theory (Strauss and Corbin, 1990) prescribed by the grounded action research approach (Baskerville and Pries-Heje, 1999)

## Phase 2. Action planning

In collaboration with practitioners, a set of design principles for providing multi-contextual support in mobile phone use in the car context was developed on the basis of the our interview study and a technology review. Consistent with the selective coding technique of grounded theory (Strauss and Corbin, 1990), we formulated these principles by iterating between the generated categories and concepts of mobile phone use and the technical possibilities identified in the technology review. These principles were:

 The principle of contextually adapted manipulation

 The principle of context-sensitive service synchronization

 The principle of context switching support

## Phase 3. Action taking

Following our three design principles, the SeamlessTalk prototype was developed as a fully integrated system of the Saab 9-3 model. Six study participants were selected for evaluating the prototype and the design principles embedded in it in their everyday mobility

Saab Automobile modified their Saab 9-3 cars so that these became SeamlessTalk-compatible. Vodafone provided the study participants with SeamlessTalk-compatible mobile phones, which replaced their ordinary phones during the evaluation period

## Phase 4. Evaluation

Six respondents evaluated SeamlessTalk over 2 months of normal car and mobile phone use. They were asked to reflect upon the impact of the prototype on their everyday mobility and report any technical problems occurring during the field trial. Data sources

 Six semi-structured interviews

 Participant observation

 Ongoing user feedback throughout the evaluation period

(continued on next page)

Table 1 (continued)

<table><tr><td>AR Cycle (July 2002 to June 2004)</td></tr><tr><td>Data analysisThe evidence generated in the diagnosing phase was used for guiding the process of data analysis. The use experiences of the prototype system was contrasted with the initial concepts and categories generated.</td></tr><tr><td>Phase 5. Specifying learningOur assessment of the SeamlessTalk prototype basically confirmed our working hypothesis. However, our analysis highlights socio-technical implications related to designing ubiquitous computing environments for handling multi-contextuality. On the basis of this analysis, we outline the lessons learned and discuss the generality of our findings beyond the car context.</td></tr></table>

& Corbin, 1990), we formulated these principles by iterating between the generated categories and concepts of mobile phone use and the technical possibilities identified in the technology review. Action taking refers to the implementation of the interventions specified in the action planning phase. Following the design principles, we developed a prototype system that intended to support multi-contextuality in mobility associated with the car context. We named the prototype ‘‘SeamlessTalk’’ because of its objective to enable seamless use of mobile phone devices across contexts.

Evaluating denotes the joint assessment (researchers and practitioners) of the interventions implemented for testing the working hypothesis. The SeamlessTalk prototype and the design principles embedded in it was evaluated by six Saab company car drivers during a 2-month period. Specifying learning is the process of summing up the learning outcomes of the action research cycle. These learning outcomes should constitute knowledge contributions to both theory and practice. By considering all pieces of our action research, the outcomes and associated socio-technical implications of our design principles for multi-contextuality in cars were outlined.

## 3.2. Data collection and analysis

Concurring with the typical action research project, our data collection involved several data sources including project and workshop sessions, document review, technology review, and qualitative interviews. These were used in varying degrees during the diferent phases of our action research project (see Table 1). Throughout the whole project, a total of 23 project meetings and workshop sessions involving the four participating organizations were held and documented. Each chaired by the first author of this paper, these sessions were characterized by numerous discussion and decision items covering the empirical studies, technology reviews, prototype development, project deliverables, and so on. In this regard, the researchers had relatively high control over the actions taken in the project. In the words of Avison, Baskerville, and Myers (2001), the authority can be classified as staged.

As part of the diagnosing phase, semi-structured interviews were conducted with 18 frequent mobile phone users. Nine of these were women. In view of the expected versatility of future ubiquitous computing services and our interest in their multicontextuality, one important selection criterion of respondents was reasonably high mobile phone use level. High use level was important to increase opportunities to discover variations among use experiences, facilitating the design-orientation of our action research. While high use level was a common denominator of the selected respondents, we sought a mix of respondents within this group in order to yield more generalizable results.

Even though we did not use the principle of theoretical saturation (Glaser & Strauss, 1967), we noted how the concepts and categories emerging in our analysis stabilized at a relatively early stage. Given the consistency of the interviews, we believe that additional interviews primarily would confirm the already collected data material. The data generated by interviews, documentation, and workshop sessions were coded by focusing on the use experiences associated with mobile phones in cars. This technique is known as open coding (Strauss & Corbin, 1990), and it is characterized by its data-driven approach to identifying important concepts in the data material. Rather than imposing theoretical concepts from the outside, the open coding technique generates concepts that are suggested by the data (Walsham, 1995). In our data material, we identified seven concepts (meaningful time usage, time-dependent coordination, mobile device manipulation, call taking, context change, handsfree problems, work-arounds) suggested by our careful analysis of more than 250 pages documented and transcribed material associated with our first interview study. These concepts were then categorized with the intention of constructing more comprehensive themes which would make sense of the collected data. This technique is known as axial coding (Strauss & Corbin, 1990). Axial coding is inter-dependent with the open coding technique in that the iterative process of synthesizing the concepts also involves revising them. Our axial coding generated a total of three categories (use incentives, use problems, and work-arounds).

On the basis of the categories and concepts developed, we then formulated three design principles through an iterative process involving the categories and concepts depicting mobile phone use in cars and technical possibilities identified in a technology review (Henfridsson, Holmstro¨m, Lindgren, Olsson, & Svahn, 2003). This is known as the selective coding technique (Strauss & Corbin, 1990), and it is characterized by formulating the framework, or grounded theory, that reveals the core phenomenon studied (in our case, multi-contextuality). At this point, it must be emphasized that ‘‘action research and grounded theory cannot be completely integrated’’ (Baskerville & Pries-Heje, 1999, p. 7). Because the action research method is goal-directed, the selective coding simply cannot generate a descriptive story of the phenomenon under study. In our case, the selective coding procedure was therefore oriented towards identifying the design principles that bested matched the categories and concepts generated earlier.

As part of the evaluation phase, semi-structured qualitative interviews were conducted with 6 respondents who had their Saab 9-3 cars modified for a 2-month evaluation of the SeamlessTalk prototype. Because the SeamlessTalk prototype only worked on the latest version of the Saab 9-3 models infotainment system, the respondents could only be selected from a fairly large number of company car drivers at Saab Automobile. Avoiding the price paid for simple prototypes (Grudin, 2001), we had to restrain the selection of respondents in this way. In this context, however, it should be noted that none of them were associated with our project.

Because the respondents had their personal mobile phones replaced with a SeamlessTalk-compatible mobile phone, virtually all car traveling during the evaluation period involved SeamlessTalk use. This level of use was confirmed in the interviews. This meant that SeamlessTalk was used by all respondents in their everyday commuting, traveling between work and customer sites, weekend trips, and so on. The stated average mileage was around 9000 per year for the six respondents. Given that five of the six respondents had a second car in the household, we estimate that each respondent drove around 1000 miles with their Saab 9-3 during the 2-month period during which they used SeamlessTalk for almost all mobile phone use in the car context. However, it can be noted that, due to technical dificulties, respondent #5 could not use SeamlessTalk fully during the first three weeks of the evaluation.

In addition to a collection of documented technical and use problems reported by users throughout the evaluation, the evaluation data consisted of more than 80 pages of interview transcripts. Similar to Orlikowskis (1993) work on CASE tool adoption, we used the evidence generated in the diagnosing phase for guiding the process of data collection, coding, and analysis in the evaluation phase. Rather than contrasting two organizations, as in Orlikowskis work, we studied existing mobile phone use and contrasted it with the use of the prototype system. Because this system embraced the findings generated in the first interview study, the prototype evaluation turned into an opportunity to re-consider the selective coding done for formulating the design principles for in-car support systems for mobile phone use. The interview protocol used focused therefore on the design principles developed on the basis of the categories and concepts generated in the diagnosing phase. In order to validate these findings, the interview protocol also included a sub-set of questions about their mobile phone use in cars prior to SeamlessTalk. These questions were intended to confirm that the patterns of mobile phone use of the selected respondents did not differ from those of the respondents interviewed in the diagnosing phase. The data collected on this sub-set of questions confirmed the patterns of use identified. Indeed, the consistency of our findings over the two studies strengthens our belief in the outlined use incentives, use problems, and work-arounds.

## 3.3. Limitations of our study

Our action research study involved a number of limitations. First, our quest to actually develop a prototype that could be tested in a realistic setting constrained both sample size, data collection, and selection scope of the respondents. The sample size could not be increased because of the time and cost constraints involved in conducting a design-oriented action research study like ours. For example, we had to modify the participants cars with both new hardware and updated software in order to evaluate SeamlessTalk. In this modification process, we intended to install flight recorders facilitating quantitative data collection and analysis of prototype use. However, in view of other costly and complex problems associated with realizing the evaluation this installation was overlooked at a late stage. This was unfortunate since recorded frequencies of actual prototype use would have added another source of data facilitating triangulation of our findings. Moreover, our prototype functioned on a single car model only. This meant that the scope of candidates available for participating in the evaluation was limited. In particular, the focus on company car drivers was limiting in that this group of respondents was heterogeneous in terms of job positions and duties. An alternative focus on professional actors in, for example, rescue services or sales would perhaps have provided a more coherent work setting in which to assess multi-contextuality in ubiquitous computing.

Second, our diagnosing phase highlighted SMS to be an integral part of mobile phone use in the car context. Accordingly, SMS was a service included in the initial technical specification of SeamlessTalk. However, since the Saab 9-3 computing platform did not include voice control support we decided to exclude SMS due to safety reasons. Having said this, it must be emphasized that cumulative learning would benefit from studies incorporating the wealth of services promised by mobile devices of the future.

## 4. Diagnosing patterns of mobile phone use in cars

Over a series of project meetings and workshops, we started our action research by exploring the future role of mobile devices (such as mobile phones, smartphones, or handheld computers) in cars. This focus was motivated by the personal telematics trend found in the automotive industry, steering away from embedded and basically proprietary car communication and computing systems (see Fuchs, 2003). Recognizing this trend early on, Saab Automobile developed similar ideas in 1996. As one of the key participants in our action research study, Saab Automobiles infotainment product manager commented:

As early as in 1996, we said that we wouldnt go with the ordinary embedded in-car phone. [. . .] At that time, Bluetooth didnt exist so we had to develop the new concept on the basis of the electronic bus of the mobile phone. We codeveloped the application with Nokia. But just when it was ready-built, Nokia told us that they had changed the technical specification [of their phone models], meaning that we had to start all over again.

As a result, Saab stalled all attempts to further pursue the personal telematics agenda. However, some five years later the momentum of the Bluetooth protocol awakened this idea. The infotainment product manager explained:

Now, the technology is in place. We have overcome the barriers associated with proprietary standards in mechanics, electronics, buses, and so on. General standards such as the Bluetooth protocol now exist, making us believe that this will actually work, also beyond a particular phone models life-cycle.

Saabs recently launched car model – Saab 9-3 – became one of the first production cars in the world equipped with the new wireless network protocol. Despite the fact that the Bluetooth standard was in place, no services were available for facilitating the use of personal mobile devices in the new car model. Without approved services, the Bluetooth protocol was merely used for establishing wireless connections between the ordinary embedded phone and headsets.

In view of Saabs hesitation to abandon the embedded phone paradigm, the action research group (researchers and practitioners) decided that an empirical confirmation would be useful for determining whether personal telematics was a worthwhile direction. This would not only require prototype development and evaluation but also mobile device use data on which such development could be based. Acknowledging that current use practice is an important starting-point for ubiquitous computing inquiry (Davis, 2002), the action research group therefore decided in autumn 2002 that a grounded understanding of the current state of mobile phone use was needed. As suggested by the researchers, such an understanding would also form a solid basis for grasping the multi-contextual nature of mobile device use in cars.

In order to better understand multi-contextuality in practice, an interview study was designed to identify and explore existing patters of mobile phone use in cars. The use incentives and problems perceived by the respondents in our qualitative interview study are shown in Table 2. The table specifies the categories and concepts that emerged from the data analysis. We propose these categories and concepts to depict typical aspects of mobile phone use in the car context. While these can be seen as illustrative dimensions of the general nature of todays mobile phone use, they are not claimed to be exhaustive. Additional studies of both professional and everyday usage of mobile phones are likely to add or modify the categories and concepts identified.

## 4.1. Use incentives

Findings from our research clearly indicate that mobile phone use in cars is governed by important use incentives. Our open coding generated two general concepts, pointing to diferent types of incentives for mobile phone usage in the car: meaningful time usage and time-dependent coordination.

## 4.1.1. Meaningful time usage

Meaningful time usage refers to mobile phone use related to peoples ambition to use the time spent in cars in a useful way. Many people spend lots of time in cars as they commute, travel between work and customer sites, and go from work to sport facilities. Our interviews highlighted that almost all of our respondents viewed the time spent in their cars as an opportunity to make both professional and private calls. Simply put, the time spent in the car is an opportunity for people to make calls that they typically would not have the time to do. According to the interview data collected, this type of mobile phone usage was often related to longer trips. A representative comment in relation to private matters was:

‘‘Often youre so stressed at work that you dont have the time to make that phone call. [. . .] When you sit in the car during the half-hour it takes from down town to the sports centre youre not that productive though. However, it can be really productive by talking to someone over the phone’’. (R.1)

Table 2  
Mobile phone use: categories, concepts, and data

<table><tr><td>Categories</td><td>Concepts</td><td>Data</td></tr><tr><td rowspan="2">Use incentives</td><td>Meaningful time usage</td><td>Time usageSocial network maintenanceClient interactionType of office hours</td></tr><tr><td>Time-dependent coordination</td><td>Household managementMeeting-time coordinationLocation coordination</td></tr><tr><td rowspan="4">Use problems</td><td>Mobile device manipulation</td><td>Phone number retrievalDialing</td></tr><tr><td>Call taking</td><td>Device is missingDevice is inconveniently placed</td></tr><tr><td>Context change</td><td>Initiate driving while using the mobile deviceLeaving the car while using the mobile device</td></tr><tr><td>Hands-free problems</td><td>Wire tanglingInsufficient integration</td></tr><tr><td>Work-arounds</td><td></td><td>Attention shiftingShort-cutsConversation interruptions</td></tr></table>

Indeed, meaningful time usage is important in professional contexts too. For example, consider the following quotation from an account manager at a small software company:

‘‘The time spent in the car is often the opportunity to actually talk on the phone. Youre not busy with client meetings or planning. When being in the car, its hard to do other things: you cannot use the computer nor write any document. Youre busy driving but talking on the phone is one of the few things you can do simultaneously. And Ill try to do that. I update myself with what happens at the ofice; I keep up with things going on. And I also talk to clients as much as I can’’. (R.18)

As illustrated in the quotation, the account manager job involves a significant portion of client meetings and ofice interaction. In the car setting, the mobile phone plays an important role in that it facilitates a meaningful use of the time spent. Indeed, because many people commute on regular hours, the time spent in the car can work as a type of ofice hours. This is especially true for people holding a job position that makes them virtually unavailable at the ofice. The commuting between home and work can thus be an important time slot for the busy manager. Considering the following quotation:

‘‘I have a colleague who I try to reach during the 45 min he sits in the car between his home in Alingsa˚ s and Go¨ teborg. And everybody knows that you call him between 7.45 and 8.30, because then hes available. Hes in the car’’. (R.15)

In sum, as the respondents expressions illustrate, meaningful time usage can be seen as a use incentive important for mobile phone usage in cars.

## 4.1.2. Time-dependent coordination

Time-dependent coordination refers to everyday coordination calls made in both work and private life. Traveling by car often means that you are on your way from one context to another (home to work, work to events, between customer sites, and so forth). As most of us are familiar with, such context changes usually involve diferent types of time-dependent coordination. Involving coordination of mundane obligations and tasks, this type of mobile phone use is typical for shorter trips. An illustrative comment related to household matters was:

‘‘I make many but short calls. For example, I might be on my way home from work and check whether the kids are ready to be picked up or if we need any items from the grocery store’’. (R.4)

Furthermore, our interviews also indicate that mobile workers usage of mobile phones in the car context is devoted to time-dependent coordination. Consider the following comment articulated by a former service technician describing his earlier work situation:

‘‘I got a flight ticket, went there, rented a car, and called the home ofice for the customer address. Once I got the address, I had to call the customer for local guidance. [. . .] I was totally dependent on the mobile phone’’. (R.8)

From our empirical data it was evident that most private and all professional users included in the study recognized time-dependent coordination of work-related activities as an important incentive for using the mobile phone while driving.

## 4.2. Use problems

Mobile phone usage in the car context is also governed by a number of use problems. On the basis of our open coding, four concepts associated with use problems of mobile phone use in cars were derived: mobile device manipulation, call taking, context change, and hands-free problems.

## 4.2.1. Mobile device manipulation

Mobile device manipulation concerns diferent types of practical moves needed to handle the mobile phone. In this case, typical user moves refer to contact list search, dialing, and so on. Elaborating on dificulties in connection with using the mobile phone while driving, our respondents highlighted several critical aspects, as illustrated by the quotations below:

‘‘Its dificult [to manipulate the device]. Youll have to have one hand on the steering wheel, look at the road at the same time as you search for a number in the contact list. Of course, Im not that concentrated on the road when doing this’’. (R.7)

‘‘I try to avoid initiating calls. Its rather tricky to find the right number while driving. But if its urgent Ill do it anyway’’. (R.14)

Whereas quite a few respondents articulated their hesitation to initiate calls while driving, the overwhelming portion of them viewed call initiation to be dificult but necessary in order to enjoy the meaningful time usage and time-dependent coordination incentives.

## 4.2.2. Call taking

A recurring theme in the interview transcripts was the experienced inconvenience of taking calls in the car setting. While this issue was recognized by almost all interviewees, some respondents reported detailed observations:

‘‘The recurring scenario is that the phone is in your bag when you get a call. You dont know exactly where it is, reach for it, and trying to find it. And it keeps ringing. The caller usually hangs up before you find it’’. (R.4)

‘‘In many cases, the phone rings and you have it in your pocket. The seat belt is in the way, you dont get to it, and it-s just a mess. When I-m alone in the car, Ive started to put the phone on the passenger seat before I start driving’’. (R.12)

As these transcripts highlight, people on the move typically have their mobile phones placed in their pocket or bag when starting to drive. Evidently, taking a call would then cause considerable inconvenience in terms of locating, reaching, and manipulating the device. Needless to say, apart from the inconvenience aspects, this is of course also a safety issue.

## 4.2.3. Context change

Context change can broadly be described as transitions between diferent mobile settings such as situations in which mobile users approach, enter, and leave the car while having ongoing calls. There were qualitatively diferent user approaches for handling context change:

‘‘I take the call with me [into the car]. Thats pretty much the point with wireless devices. [. . .] There are some tricky steps. When starting to drive, or parking, it can be dificult to continue talking’’. (R.11)

‘‘No, I dont do that [keep the call when entering the car]. It involves so much trouble. When approaching the car while having a call, I usually hang up and re-initiate the call later. First, youve to unlock the car and stuf your things, and then get seated, buckle up, and start the car. All these things are obstacles in my mobile phone use. So, I often say that Im in the car; I call you back in a few minutes’’. (R.12)

Whereas respondents associated context changes with certain dificulties, our interviews indicated that people handled these changes in diferent ways. Some terminated their calls and re-initiated them once seated in the car, while other people simply continued their conversations when entering and/or leaving the car.

## 4.2.4. Hands-free problems

Hands-free problems refer to specific obstacles related to usage of diferent forms of hands-free systems. Despite the fact that most of our respondents had used mobile phones extensively for several years, however, it can be noted that the average use level of hands-free systems was low in the test group. The data collected included some elaborate thoughts, tracing this fact to specific obstacles of using such support technology:

‘‘Its really a disadvantage that they [the wires of the hands-free set] tangle. So, if youve not talked for a while and the phone rings, you often drag it out [of your pocket] and dismantle the headset because you dont want to sort out the mess’’. (R.2)

‘‘Either you press a button for using hands-free, or you lift the handset for getting a private conversation. But this phone doesnt work; its an Ericsson and it doesnt fit the cradle. It-s a pity’’. (R.4)

The general idea of in-car hands-free support systems is to increase both convenience and safety for car users. While appreciating the basic idea behind such solutions, our respondents requested improvements, facilitating seamless integration of in-car resources and mobile phones.

## 4.3. Work-arounds

Our analysis of mobile phone use in the car context exhibits interesting and challenging use incentives and problems. Although participants of the study characterized driving as a demanding and sometimes dangerous activity, most respondents recognized the use incentives to be higher than the problems perceived. Many respondents had developed diferent routines or work-arounds for adjusting their phone use to specific trafic situations. Responding to the use problems experienced, the following interviewees describe how they combine driving with SMS use or phone number retrieval:

‘‘I hold the phone quite high so that I can keep my eyes on the phone and the trafic simultaneously. In that way, I view at least a silhoutte of whats in front of me. Then I switch my attention between the phone and the windscreen’’. (R.6)

‘‘Its dificult to retrieve phone numbers from the contact list while driving. So Ive created ten short-cuts for people who I often call. It works fairly well’’. (R.12)

‘‘If Im going for a little longer drive, I place the phone so that it is easily reached. If I get a SMS, I pick up the phone and hold it against the steering wheel so that I can at least see who sent it. If its not important, I might look it up later. This depends on the situation. . .’’ (R.20)

In addition to work-arounds for supporting mobile phone manipulation and driving, our respondents elaborated on diferent types of routines to facilitate, for example, gear-shifting while having an ongoing call:

‘‘The gear-shifting is much messier when you use the phone. Then you have to ask [when he shifts gears] the recipient to wait a little. [. . .] If you have a larger phone, you can facilitate this process like this [the respondent shows how it is possible to squeeze the phone between ear and shoulder]’’. (R.16)

In sum, the benefits of using mobile phones in the car context are perceived to be so high that people typically invent work-arounds. Including attention shifting, short-cuts, and conversation interruptions, such work-arounds were all intended to facilitate meaningful time usage and time-dependent coordination in their everyday mobility.

## 4.4. Working hypothesis

In view of this mobile device use data, our action research group concluded that the inconvenience of mobile phone use in cars needs to be addressed. On the basis of the diagnosing phase, we therefore formulated the following working hypothesis: the car as a ubiquitous computing environment can improve the convenience of peoples everyday mobile device use by providing multi-contextual support.

## 5. Action planning and taking

## 5.1. Design principles for handling multi-contextuality

Guided by our working hypothesis, we then set out to develop a design framework that would address the experienced inconvenience of mobile phone use in cars. Formulating this framework, we relied on the concepts and categories depicting the typical mobile phone use found in cars (see Table 2) and our technology review. As prescribed by the grounded action research method (Baskerville & Pries-Heje, 1999), we used Strauss and Corbins (1990) selective coding technique for framework formulation. During collaborative workshop sessions, we iterated between the generated concepts and categories of mobile phone use and the technical possibilities identified in the technology review.

In view of our design interest and the centrality of design in the IS discipline (Hevner, March, Park, & Ram, 2004; Lindgren, Henfridsson, & Schultze, 2004; Markus et al., 2002), our theory formulation consisted of developing design principles that handle multi-contextuality and thereby improve the possibilities of convenient mobile phone use in the car as a ubiquitous computing environment. We developed the following three design principles:

1. The principle of context-sensitive service synchronization: The car as a ubiquitous computing environment should make selective services associated with the mobile device available to users. This means that services deemed plausible for the car setting should be synchronized with the ubiquitous computing environment. While this principle addresses insuficient integration problems related to hands-free usage, it is also necessary to leverage the full value of the use incentives identified (meaningful time usage and time-dependent coordination).

2. The principle of contextually adapted manipulation: The car as a ubiquitous computing environment should provide the user with device or service controls adapted to the spatio-temporal conditions of cars. The call taking and mobile device manipulation problems identified in the interview study indicate that mobile devices are ill-suited to these conditions. This principle responds to these problems.

3. The principle of context switching support: The car as a ubiquitous computing environment should support switching between diferent physical and social contexts. This principle addresses the context change problem in that it supports seamless transitions across contexts necessary for sustained services.

These three design principles were then applied in the design of a prototype – SeamlessTalk – that would enable us to test these principles in practical use situations.

## 5.2. SeamlessTalk

SeamlessTalk is a prototype that facilitates driver (or passenger) control of Bluetooth-equipped mobile phones brought into the car. SeamlessTalk is developed as a component of the top-end infotainment system of the Saab 9-3 car (see Figs. 1 and 2). Equipped with a Bluetooth access point and an hands-free interface including dashboard control buttons, a 5,8<sup>0</sup> <sup>0</sup> dashboard screen, a microphone, and an in-car audio system; this Saab model provides an interesting ubiquitous computing environment for developing applications that support multi-contextuality in the car case.

![](/api/attachments/EQWCDKFJ/fulltext/images/88d02750572a821cbbb86c7babc5a2e0be10e5ee220feafde084dae94150d13b.jpg)  
Fig. 1. The dashboard of a Saab 9-3 equipped with the infotainment system.

![](/api/attachments/EQWCDKFJ/fulltext/images/d3c7cd019eb52ad8f1a2d58170e32afef9af2faed082921bef0336a1b5566d99.jpg)  
Fig. 2. The main menu of the infotainment system.

![](/api/attachments/EQWCDKFJ/fulltext/images/fecf546dff0c354ab16c1649894fab018a7f7280cf7d5fb5557a41495a6b845b.jpg)  
Fig. 3. SeamlessTalk is controlled by the multi-functional control of the infotainment system.

As illustrated in Fig. 2, the SeamlessTalk prototype is accessible as the ‘‘phone’’ option from the main menu of the infotainment system. In a Saab 9-3 production car (currently available at Saab car dealers), this option provides driver (or passenger) access and control of the embedded in-car phone. Given our objective of developing and testing design principles that handle multi-contextuality and thereby render convenient mobile phone use in the car, we developed SeamlessTalk so that it by-passes the embedded phone by establishing a Bluetooth connection between the car (and its in-car phone resources such as dashboard control buttons, dashboard-integrated screen, microphone, and in-car audio system) and the mobile phone. Because Bluetooth is implemented differently across diferent mobile devices, the prototype system only supports the Nokia 6310i and Nokia 6650 (a 3G terminal, see Fig. 4) phones in its current version.

![](/api/attachments/EQWCDKFJ/fulltext/images/2d887c0bef8ed0b8077fc856c5c95a24891c3c343c342c0991ea1bb76846203e.jpg)  
Fig. 4. Nokia 6650 was the phone used in our evaluation.

SeamlessTalk embraced all three of our design principles: contextually adapted manipulation, context-sensitive service synchronization, and context switching support. First, with SeamlessTalk, users are able to use dashboard controls for controlling the device. The infotainment unit consists of a complete dial pad. Moreover, calls can be executed and terminated by using the yes/no buttons on the steering wheel. Apart from dashboard buttons, the mobile phone can also be manipulated by navigating the menus of the infotainment system. The navigation is controlled by a multi-functional control placed just outside the lower right corner of the screen (see Fig. 3).

Second, context-sensitive service synchronization is achieved by using the Bluetooth ad hoc networking standard with the service discovery protocol and the hands-free profile. Users are thus able to use the call service available via the mobile device by selecting the hands-free option in the infotainment system (see Fig. 5). In this way, the mobile phone is not involved at all from a user perspective. Following the context-sensitiveness specified by this design principle, we did not include SMS support in SeamlessTalk since we did not consider text messaging plausible in a car without voice control support. However, the contact list service could not be synchronized with SeamlessTalk due to time and resource constraints.

![](/api/attachments/EQWCDKFJ/fulltext/images/34eb9fb82dd31c967a5127c026723180edd36be84ffb539fad4bfebd6fc6584a.jpg)  
Fig. 5. The ‘‘handsfree’’ option is used for connecting the mobile phone to SeamlessTalk.

![](/api/attachments/EQWCDKFJ/fulltext/images/7849e3c5b057b999b538a653d42f546106a1513f2a0532546caa9f6069e46f28.jpg)  
Fig. 6. The ‘‘transfer to mobile’’ is used for disconnecting the mobile phone from SeamlessTalk.

Third, with SeamlessTalk, users can conveniently switch context during on-going calls. In the case of entering the car with an ongoing call, the call can be transferred by using the ‘‘hands-free’’ option of the infotainment system (see Fig. 5). Similarly, the call can be transferred to the mobile phone in case of leaving the car (see Fig. 6). This can also be used in situations where several people are in the car and the SeamlessTalk user wants to make or take a private call, i.e., a social context switch.

## 6. Evaluation

The SeamlessTalk prototype was evaluated over a 2-month period (November 2003 to January 2004). In total, the evaluation involved five SeamlessTalk-equipped Saab 9- 3 cars and six respondents (two of the respondents used the same car). At a meeting at Saab Automobiles head ofice in Trollha¨ttan, Sweden, the participants were introduced to the rationale behind the prototype design and informed about our evaluation strategy. We explained that they were expected to use SeamlessTalk in their everyday life including commuting, traveling between customer and work sites, leisure trips, and so on. They were also asked to reflect upon the impact of SeamlessTalk on their day-today mobility and report any technical problems occurring during the field trial. In our quest for realistic evaluation conditions, (1) Saab Automobile modified the participants cars (both new hardware and updated software) so that SeamlessTalk could be installed, and (2) the participants were provided SeamlessTalk compatible 3G mobile phones (Nokia 6650) that they were obliged to use as their everyday phones throughout the evaluation period. Contact lists were transferred to the new SIM-card and calls were re-directed from their ordinary phone numbers to the new ones.

Our thorough evaluation highlighted anticipated design outcomes and sociotechnical implications of our prototype and the three design principles embedded in it (see Table 3).

Table 3  
Evaluation overview

<table><tr><td>Design principles</td><td>Design outcomes</td><td>Socio-technical implications</td></tr><tr><td>Context-sensitive service synchronization(Use problem addressed:Hands-free problems)</td><td>Increased convenienceEnhanced hands-free use</td><td>The persistence of various individual use patterns (e.g., recent number access for call initiation) over contexts complicates service synchronization</td></tr><tr><td>Contextually adapted manipulation (Use problems addressed:Call taking, mobile device manipulation)</td><td>Improved call taking abilitiesFacilitated mobile device manipulation</td><td>Integration of services relying on different interaction models makes contextually adapted manipulation difficult in ubiquitous computing environments</td></tr><tr><td>Context-switching support(Use problem addressed:Problems of context change)</td><td>Generally convenient context switches</td><td>Insufficient mode awareness undermines trustful context-switches</td></tr></table>

With regard to intended design outcomes, our respondents considered the context-sensitive service synchronization support ofered by the prototype to be useful. Typical comments were:

‘‘I think this [solution] kills the idea of an integrated car phone. This is a solu tion that provides hands-free support in the car without the need for wires or dash-mounted solutions’’. (R.1)

‘‘The added value is the freedom you experience. You dont have any wires. [. . .] You dont have to think about those things, you just sit down and start to drive’’. (R.5)‘‘Personally, I think it was great. The phone can remain in the bag, jacket or anywhere. You dont lose your attention [on the road] in the way you normally do’’. (R.6)

In particular, they seemed to appreciate the convenience of using their everyday mobile phone. The service synchronization principle was seen as addressing both aspects of the hands-free problems (wire tangling and insuficient integration). In this way, the principle enhanced the use incentives (meaningful time-usage and time-dependent coordination) associated with such use.

Clearly, the service synchronization principle rendered to the support that we had anticipated. However, we did not succeed in implementing SeamlessTalk as to embrace this principle fully. Indeed, work-arounds involving the mobile phone existed:

‘‘Suddenly, you realized that you needed a number that you had not entered manually. [. . .] Oh, Id like to call that person but I dont have the number stored [in the car infotainment system]. Then, I had to find my mobile phone and retrieve the number’’. (R.3)

Given our objective to place the mobile phone backstage, synchronization of the contact list would have been a natural design decision. Also related to call initiation, one respondent said:

‘‘Today, you never actually dial a number on a mobile phone but you search the contacts youve got. Once you dialed them, you use the recent number list. Thats the routinized behavior once you get seated in the car. Then, youve to search for numbers. . . Thats a bit stupid. Even more so in this case when the contact list [in the mobile phone] and the application are separated’’. (R.5)

Highlighting SeamlessTalks lack of support for recent number access, this testimony revealed the fact that individuals seem to develop their own routines for handling mobile devices. These ingrained routines also tend to be enacted over contexts. Given that there are many ways to initiate calls, the persistence of individual user patterns over different contexts complicates synchronization eforts intended for a mass-scale market.

Furthermore, the respondents generally valued our implementation of the contextually adapted manipulation principle. They found it beneficial to use the car interface for mobile phone manipulation, asserting that the in-car controls were more adjusted to driving situations. Two respondents commented:

‘‘You can overview [the trafic situation] in a better way, compared to situations in which you manipulate the mobile phone using a screen that is virtually unreadable. [. . .] I drive much safer in this way. Also, when it rings you just have to push the button and take the call instead of the typical case of searching your jacket or bags or what have you’’. (R.2)

‘‘A real advantage has been the car dial pad. Compared with manipulating the mobile phone. . . With this, you can actually search for numbers while driving; in a reasonable safe way too’’. (R.3)

The perceived increase in safety was strongly appreciated by the respondents. This can be traced to the convenience of using the steering wheel controls and the multi-functional control of the infotainment system when, for instance, taking a call. In fact, most of the respondents reported that they had increased their mobile device use in cars. This was especially true for respondents (R.2 and R.3) who frequently used their car for longer trips on weekends. It can therefore be concluded that the principle of contextually adapted manipulation addressed the mobile device manipulation and call taking problems as intended.

In addition to these anticipated outcomes of our contextually adapted manipulation principle, our evaluation also highlighted a socio-technical implication of the principle. In our attempts to adapt SeamlessTalk to the spatio-temporal conditions of the car, the prototype was implemented as an integrated component of the Saab 9- 3 infotainment system, meaning that it shared resources with other car infotainment applications (e.g., CD/radio and navigation system). As an example, we used the hierarchical menu structure of the infotainment system for enabling prototype manipulation. The evaluation highlighted some drawbacks of this approach. One respondent recognized the diferent interaction models required for manipulating the SeamlessTalk service and the navigation system:

‘‘I think that a phone must be very direct. [. . .] Its diferent from a navigation system where you normally do little while driving. [. . .] In the phone case, I might get an impulse that I want to call that or that person. You cannot plan your calling in the same way’’. (R.1)

This respondent suggested that the number of moves needed to drill down the hierarchical tree structure worked as a barrier to retrieving a phone number. Obviously, because SeamlessTalk and the in-car navigation system required diferent interaction models, their co-existence as components of the Saab 9-3 infotainment system caused problems. Their co-existence was nevertheless the only technically feasible solution with current technologies. Integration of services relying on diferent interaction models makes contextually adapted manipulation a challenging issue in ubiquitous computing environments.

A number of the interviewees remarked on the advantages of our context-switching support principle. They saw the value in switching seamlessly from hands-free mode to mobile device in case of ongoing calls, especially with regard to work situations in which calls are frequent and function as important coordination mechanisms.

‘‘Its definitely an advantage. [. . .] A couple of times on the way home from work Ive had ongoing calls that Ive taken with me and finished at home’’. (R.3)

In this regard, the context switching support principle embedded in SeamlessTalk addressed the problem of context change as identified in our diagnosis of mobile phone use in cars. This was typically true for situations in which the user left the car with ongoing calls. However, our evaluation also highlighted dificulties involved in technically realizing this design principle. For instance, it took several seconds for the in-car computing platform to be up-and-running, once the power had been turned on. Indeed, this delay reduced the value of the switching support ofered by SeamlessTalk. In some situations, this ultimately meant that people did not care to use the prototype at all. One of the respondents said:

‘‘It was irritating that it took a little while before the system woke up. [. . .] If youre in a hurry, it must be quicker. When I went for shorter trips, I sometimes didnt bother to use it [SeamlessTalk]’’. (R.1)

The fact that the prototype remained unused in time-critical situations was a disap pointing and counter-productive outcome compared to our initial intentions.

Furthermore, a socio-technical implication was that SeamlessTalk users were sometimes unsure whether the hands-free mode really was activated. Discussing context switches with or without ongoing calls, two respondents expressed:

‘‘It [SeamlessTalk] should visualize when the hands-free option is active. I was sometimes unsure about what mode it was in’’ (R.1)

‘‘It [the wireless connection] creates a sense of uncertainty. If you plug in a wire, this procedure works as some sort of a confirmation [that the system works]’’ (R.4)

This problem can be seen as a product of the mode unawareness resulting from the lack of tangible confirmations when using the system. One of the respondents continued:

‘‘The context switches are somewhat unpredictable and creates uncertainty. I dont know what it is, how it works. . . Consider what happened yesterday: I stopped at the corner shop and switched of the engine. Attempting to avoid disconnecting the phone I left it in the car. When I came back I was still connected, wasnt I? But I dont know, do I?’’ (R.4)

As a consequence of the experienced ambiguity, this respondent hesitated to use SeamlessTalk when awaiting important incoming calls.

## 7. Discussion

This paper reports a grounded action research study (Baskerville & Pries-Heje, 1999) with the objective of developing and testing design principles for handling the multi-contextuality associated with mobile device use in cars. In collaboration with practitioners from Mecel, Saab Automobile, and Vodafone, we completed one full action research cycle (Susman & Evered, 1978) including an interview study of mobile phone use in cars, design principles development, a car-integrated prototype implementation, and a 2-month evaluation involving five cars and six respondents.

Our action research indicated that the three design principles (context-sensitive service synchronization, contextually adapted manipulation, and context switching support) developed for handling multi-contextuality were efective in that they contributed to the anticipated outcomes. In fact, they addressed each of the use problems diagnosed in our investigation of existing patterns of mobile phone use in cars. Thus, the working hypothesis, specifying that the car as a ubiquitous computing environment can improve the convenience of peoples everyday mobile device use by providing multi-contextual support, was confirmed. However, the evaluation also highlighted that there were specific socio-technical implications of the design principles. We suggest these implications to be valid for other ubiquitous computing environments too. As outlined by Walsham (1995), such implications should be seen as tendencies rather than predictions in that they describe generative mechanisms noted in a specific research endeavor that might prove to be useful for related research in other contexts.

## 7.1. Synchronizing fluid use patterns

The principle of context-sensitive service synchronization stipulates that the car as a ubiquitous computing environment should make selective services (deemed plausible in the car setting) associated with the mobile device available to users. This principle was developed to address the hands-free problem identified in the interview study. As illustrated by the evaluation, its implementation contributed to users increased convenience and enhanced hands-free use. Supporting users utilization of their everyday mobile phones, this principle was perceived to facilitate meaningful time usage and time-dependent coordination, both of which were recognized as important incentives in peoples mobility. Contrasted with dedicated in-car phones, the possibility of synchronizing the mobile phone with the car contributed to user convenience.

However, our research also showed that the seamlessness enabled by the service synchronization principle can be dificult to achieve. The fact that SeamlessTalk did not synchronize contact and recent number lists with the mobile phone caused some frustration among our respondents. As observed in both rounds of interviewing, people typically establish, routinize, and enact particular mobile phone use patterns. Our SeamlessTalk evaluation indicates that the persistence of diferent individual use patterns (e.g., recent number access for call initiation) over contexts complicates service synchronization.

Diferences in individual use patterns make it hard to deliver mass-scale services since the openness of mobile devices can trigger an abundance of such patterns. To identify and verify which set of use patterns are to be supported by allowing synchronization to specific ubiquitous computing environments is thus a challenging task. Such prioritization of use patterns is, however, necessary in environments (such as the car) with limited bandwidth and resources. Given that ubiquitous computing environments host more than one service, this is even more challenging when one considers the increasing number of services (such as SMS, MMS, e-mail, and calendar functions) provided through todays advanced multi-purpose devices. This means that the fluid use patterns emerging and disappearing with the on-going difusion of new ubiquitous computing devices and services require more intense re-development eforts compared to traditional information systems particularly developed for organizations characterized by enduring patterns of use.

## 7.2. Scaling service manipulation

The principle of contextually adapted manipulation prescribes that the car as a ubiquitous computing environment should provide the user with device or service controls adapted to spatio-temporal conditions of cars. This principle was intended to address the call taking and mobile device manipulation problems identified in our diagnosing phase. The evaluation of the principle showed that it improved call taking abilities and facilitated mobile device manipulation. Specifically, the in-car controls including steering-wheel controls, dial pad, and the multi-functional control of the infotainment system catered for the users convenient service manipulation. According to our respondents, this increased convenience contributed also to safer mobile device use while driving. Their main argument was basically that SeamlessTalk was more in tune with the specifics of driving situations. Worth noting is that several users reported that they had indeed increased their in-car mobile phone use.

However, our evaluation also highlighted that shared resources ofered by a ubiquitous computing environment cannot always be assumed to meet the specific requirements of the services hosted. For example, while the hierarchical menu structure of the infotainment system worked as a resource for enabling service manipulation, the number of moves needed to drill down the menu structure was an obstacle for users trying to retrieve a phone number. This obstacle can be traced to the seemingly ill-suited interaction model of the infotainment system. Contrasting the polychronic nature of mobile phone usage, the hierarchical models monochronicity was at odds with typical user behavior.

On the basis of this observation, scaling of ubiquitous computing environments to host mobile devices and services on a mass-scale can be regarded as a design problem central to ubiquitous computing. Even though devices and services are interoperable with ubiquitous computing environments through ad hoc network connectivity, novel service manipulation strategies are critical for handling situations where ubiquitous services difer in temporal assumptions. In addition to supporting a set of diferent service interaction models, however, ubiquitous computing environments must also be aware of the multi-contextual conditions changing with users mobility in order to determine the appropriate way to host services. In the car context, for instance, this would not only mean that services are associated with specific service manipulation models but also that the car can use diferent data sources (e.g., vehicle data such as the drivers workload, position, and speed) for conditioning the use of these services at given points in time. Such conditioning can be important for insurance deals, law enforcement, and other activities surrounding personal telematics use in our everyday life. Given this range of issues related to scaling service manipulation, ubiquitous computing environments expected to host a range of services can be said to face integration challenges beyond those associated with mainstream information systems.

## 7.3. Signaling context-switches through awareness support

The principle of context-switching support specifies that the car as a ubiquitous computing environment should support transitions between diferent physical and social contexts. The principle was anticipated to tackle the context change problem as observed in our diagnosis of existing patterns of mobile device use in cars. As the evaluation highlighted, the implementation of this principle facilitated convenient context switches. This was especially true for situations where users left the car having ongoing calls that were subsequently terminated in another spatial context. In the reverse case, the start-up process of the car infotainment system delayed the context switch, causing irritation among the participants evaluating SeamlessTalk. This example pinpoints the time-criticality associated with transitions between diferent contexts.

Our evaluation also highlighted that context-switching can be a source of uncertainty. On some occasions, respondents were unsure as to whether or not the handsfree mode was activated. Indeed, such uncertainty downplays the perceived value of using ubiquitous computing environments. Convenience relies heavily on switches that function consistently over many use situations so that users need not worry about unwanted breakdowns.

Somewhat ironic in light of the vision of the disappearing computer, our research indicates that signaling context-switches is an appropriate way to place computing in the background. However, the implementation of awareness support in ubiquitous computing environments including various devices, services, and diferent mobile use situations is complicated. Due to the multi-contextual nature of ubiquitous service use, a well-balanced mix of signaling techniques involving audio, motion, and visual feedback is required to ofer awareness support. Because transparent transitions across diferent contexts and devices lie at the heart of well-working ubiquitous computing environments, finding the right mix of such techniques is important for trustful context-switches when computing is placed backstage. Indeed, it goes without saying that the user feedback is an even more challenging issue when it comes to ubiquitous computing environments than conventional information systems.

## 8. Conclusion

This paper investigates the problem of multi-contextuality in ubiquitous computing. While mass-scale ubiquitous computing services are intended to work on a global scale (Lyytinen & Yoo, 2002), they are at the same time expected to ofer transparent, integrated, and convenient support in localized use contexts (Kleinrock,

2001). This makes the problem of multi-contextuality challenging for designers of ubiquitous computing environments. Addressing this challenge, we embarked on a grounded action research study with the objective of developing and testing design principles for handling multi-contextuality in an increasingly important ubiquitous computing environment – the car. In particular, we focused on how to support the multi-contextuality of mobile phone use in cars and what socio-technical design implications such support would render.

Contributing to the early stage of the ubiquitous computing research tradition, our design principles empirically demonstrate that the car as a ubiquitous computing environment can improve the convenience of peoples everyday mobile device use by providing multi-contextual support. We also suggest that our design principles and their associated socio-technical implications (synchronizing fluid use patterns, scaling service manipulation, and signaling context-switches through awareness support) are valid for other ubiquitous computing environments.

Future research in this area could possibly inquire into the design and methodological challenges related to socio-technical implications of ubiquitous computing. For instance, the combination of fluid use patterns and the increasing numbers of ubiquitous services following todays multi-purpose devices suggests that we need to reconsider traditional assumptions about IS development and use. Moreover, scaling of ubiquitous computing through increased system interoperability via ad hoc network connectivity triggers new issues related to user interface design as well as the integration of services into users everyday mobility. Because such inquires deal with phenomena that emerge when social and technical systems interact, IS researchers are well positioned for doing this. Reflecting Lyytinen and Yoos (2002) call for up-close IS studies of ubiquitous computing, our own study, which blends prototyping with action research, can function as an example of how such studies can be designed.

## Acknowledgements

VINNOVA and the participating organizations funded this work. We are also deeply indebted to all industry participants of our action research project. Special thanks to Hele´n Eliasson and Per Lindberg at Saab Automobile. Thanks are also due to Carl Magnus Olsson, the special issue editors, Kalle Lyytinen and Youngjin Yoo, and two anonymous reviewers for their useful comments.

## References

Abowd, G. D., & Mynatt, E. D. (2000). Charting past, present, and future research in ubiquitous computing. ACM Transactions on Computer-Human Interaction, 7(1), 29–58.

Alm, H., & Nilsson, L. (1995). The efects of a mobile telephone task on driver behaviour in a car following situation. Accident, Analysis, and Prevention, 27(5), 707–715.

Avison, D., Baskerville, R., & Myers, M. (2001). Controlling action research projects. Information Technology & People, 14(1), 28–45.

Barley, S. R. (1988). On technology, time, and social order: Technology induced change in the temporal organization of radiological work. In F. A. Dubinskas (Ed.), Making time: Ethnographies of hightechnology organizations. Philadelphia, PA: Temple University Press.

Baskerville, R., & Pries-Heje, J. (1999). Grounded action research: a method for understanding IT in practice. Accounting, Management & Information Technologies(9), 1–23.

Baskerville, R., & Wood-Harper, A. T. (1998). Diversity in information systems research methods. European Journal of Information Systems, 7(2), 90–107.

Bellotti, V., & Bly, S. (1996). Walking away from the desktop computer: distributed collaboration and mobility in a product design teamProceedings of CSCW96 (pp. 209–218). Cambridge, MA: ACM.

Bisdikian, C., Boamah, I., Castro, P., Misra, A., Rubas, J., Villoutreix, N., Yeh, D., Rasin, V., Huang, H., Somonds, C. (2002). Intelligent pervasive middleware for context-based and localized telematics services. In Proceedings of WMC02 (pp. 15–24).

Brookhuis, K. A., De Vries, G., & De Waard, D. (1991). The efects of mobile telephoning on driving performance. Accident Analysis & Prevention(23), 309–316.

Cerf, V. G. (2001). Beyond the post-PC internet. Communications of the ACM, 44(9), 35–37.

Dahlberg, P., Ljungberg, F., & Sanneblad, J. (2002). Proxy lady – mobile support for opportunistic communication. Scandinavian Journal of Information Systems(14), 3–17.

Dahlbom, B., & Ljungberg, F. (1998). Mobile informatics. Scandinavian Journal of Information Systems, 10(1& 2), 227–234.

Davis, G. B. (2002). Anytime/anyplace computing and the future of knowledge work. Communications of the ACM, 45(12), 67–73.

Davison, R. M., Martinsons, M. G., & Kock, N. (2004). Principles of canonical action research. Information Systems Journal(14), 65–86.

Esbjo¨rnsson, M., Juhlin, O. (2003). Combining mobile phone conversations and driving – studying mundane activity in its naturalistic setting. In Proceedings of ITS2003.

Fagrell, H., Ljungberg, F., Kristofersen, S. (1999). Exploring support for knowledge management in mobile work. In Proceedings of ECSCW99.

Fuchs, A. (2003). Personal telematics – a global paradigm change. Telematics Update Magazine, 21, 14–15.

Giddens, A. (1984). The constitution of society – outline of the theory of structuration. Cambridge, UK: Polity Press.

Giddens, A. (1990). The consequences of modernity. Cambridge, UK: Polity Press.

Glaser, B., & Strauss, A. (1967). The discovery of grounded theory. Hawthorne, NY: Aldine.

Goodman, M. J., Tijerina, L., Bents, F. D., & Wierwille, W. W. (1999). Using cellular telephones in vehicles: safe or unsafe?. Transportation Human Factors, 1(1), 3–42.

Grindley, P. (1995). Standards, strategy, and policy: cases and stories. New York: Oxford University Press.

Grudin, J. (2001). Desituating action: digital representation of context. Human-Computer Interaction(16), 269–286.

Henfridsson, O., Holmstro¨m, H., Lindgren, R., Olsson, C. M., Svahn, F. (2003). Framtidens Fordon: Mo¨tet Mellan Tva˚ Mobila Va¨rldar (In English: The Future Vehicle: The Convergence of Two Mobile Worlds), VINNOVA rapport VR 2003:04/TELDOK Rapport 149, Stockholm.

Henfridsson, O., Wiberg, M., Lindgren, R., & Ljungberg, F. (2005). SeamlessTalk: User-controlled session management for sustained car conversations. In M. Wiberg (Ed.), The interaction society: Practice, theories, and supportive technologies (pp. 304–318). Hershey: Idea Group.

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75–105.

Jessup, L. M., & Robey, D. (2002). The relevance of social issues in ubiquitous computing environments. Communications of the ACM, 45(12), 88–91.

Kakihara, M., & Sørensen, C. (2002). Mobility: An extended perspectiveProceedings of HICSS35. Big Island, Hawaii: IEEE.

Kleinrock, L. (2001). Breaking loose. Communications of the ACM, 44(9), 41–45.

Kristofersen, S., Ljungberg, F. (1998). Representing modalities in mobile computing. In Proceedings of interactive applications of mobile computing (IMC98), Rostock, Germany.

Lamble, D., Rajalin, S., & Summala, H. (2002). Mobile phone use while driving: public opinions on restrictions. Transportation(29), 223–236.

Lindgren, R., Henfridsson, O., & Schultze, U. (2004). Design principles for competence management systems: a synthesis of an action research study. MIS Quarterly, 28(3), 435–472.

Lee, H. (1999). Time and information technology: monochroncity, polychronicity and temporal symmetry. European Journal of Information Systems, 8(1), 16–26.

Luf, P., & Heath, C. (1998). Mobility in collaborationProceedings of CSCW98 (pp. 305–314). Seattle, USA: ACM.

Lyytinen, K., & Yoo, Y. (2002). Research commentary: the next wave of nomadic computing. Information Systems Research, 13(4), 377–388.

Makimoto, T., & Manners, D. (1997). Digital nomad. Chichester, UK: Wiley.

Markus, M. L., Majchrzak, A., & Gasser, L. (2002). A design theory for systems that support emergent knowledge processes. MIS Quarterly, 26(3), 179–212.

May, P. (2001). Mobile commerce – opportunities, applications, and technologies of wireless business. Cambridge, MA: Cambridge University Press.

Orlikowski, W. J. (1993). CASE tools as organizational change: investigating incremental and radical changes in systems development. MIS Quartely, 17(3), 309–340.

Pucher, J., & Renne, J. L. (2003). Socioeconomics of urban travel: evidence from the 2001 NHTS. Transportation Quartely, 57(3), 49–77.

Redelmeier, D. A., & Tibshirani, R. J. (1997). Association between cellular-telephone calls and motor vehicle collisions. The New England Journal of Medicine(336), 453–458.

Robey, D., & Markus, M. L. (1998). Beyond rigor and relevance: producing consumable research about information systems. Information Resources Management Journal, 11(1), 7–15.

Salvucci, D. D. (2001). Predicting the efects of in-car interfaces on driver behavior using a cognitive architectureProceedings of SIGCHI 2001 (pp. 120–127). Seattle, WA: ACM.

Schmidt, A., Beigl, M., & Gellersen, H.-W. (1999). There is more to context than location. Computers & Graphics(23), 893–901.

Strauss, A., & Corbin, J. (1990). Basics of qualitative research: Grounded theory procedures and techniques. Newbury Park: Sage.

Susman, G., & Evered, R. (1978). An assessment of the scientific merits of action research. Administrative Science Quartely(23), 582–603.

Tofler, A. (1970)Future shock (pp. 1970). London: Pan Books.

Towers, M. (2002). Is 2003 the year for bluetooth in the car?. Telematics Update Magazine, 19.

Walker, G. H., Stanton, N. A., & Young, M. S. (2001). Where is computing driving cars?. International Journal of Human-Computer Interaction, 13(2), 203–229.

Walsham, G. (1995). Interpretive case studies in IS research: nature and method. European Journal of Information Systems(4), 74–81.

Weiser, M. (1991). The computer for the 21st century. Scientific American(Sept), 94–104.

Wiberg, M., & Ljungberg, F. (2001). Exploring the vision of anytime, anywhere in the context of mobile work. In Y. Malhotra (Ed.), Knowledge management and business model innovation (pp. 153–165). Idea Group Publishing.
