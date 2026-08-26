---
otero_id: 21047
otero_key: "KCM4GPVU"
title: "Decision making under time pressure with different information sources and performance-based financial incentives—Part 1"
authors: "James R. Marsden; Ramakrishnan Pakath; Kustim Wibowo"
year: "2002"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(01)00135-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision making under time pressure with different information sources and performance-based financial incentives—Part 1

James R. Marsden <sup>a,</sup>\*<sup>,1</sup>, Ramakrishnan Pakath <sup>b,2</sup>, Kustim Wibowo <sup>b,2,3</sup>

<sup>a</sup>Shenkman Chair in e-Business, Operations and Information Management Department, School of Business U41 1M, University of Connecticut, Storrs, CT 06269-1041, USA

<sup>b</sup>Decision Science and Information Systems, School of Management, C.M. Gatton, College of Business and Economics, University of Kentucky, Lexington, KY, 40506-0034, USA

Received 1 August 2000; received in revised form 1 June 2001; accepted 1 August 200

## Abstract

We are witness to the communications revolution and the accompanying proliferation of narrow-purpose, mobile, computing and communication devices. Such devices tend to be smaller and lighter than their desktop and laptop counterparts. The tradeoff is that their displays and memory also tend to be relatively smaller. To date, they also rely on traditional English and/or icons for communicating with users. While icons have grown in usage, capturing any and all information using icons is impossible and/or prohibitively expensive. We examine the viability of developing new kinds of communication languages for such devices in a specific setting by considering an abstract classification task and examining the performance of subjects using a new, compact language that we have devised vis-a\`-vis written and spoken English. Our work draws on prior research on induced value experimentation and ex-ante system evaluation. In Part 1 of this two-part paper, we provide the necessary background, discuss the underlying motivations, and describe the construction and refinement of our experimental platform and an accompanying subject training software suite. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Decision making; Time pressure; Symbolic language; Multimedia systems; Mobile computing; Ex-Ante DSS evaluation; Induced value theory

## 1. Introduction

Consider the following scenarios.

(a) Arnold, a stockbroker, must assess and classify stocks based on a number of factors. He monitors specific information about stocks of interest using an electronic monitoring device and makes rapid sell/buy/ hold decisions.

(b) You are at home alone when you suspect a prowler. You press a special key on your telephone and a preformatted message ‘‘capsule’’ is routed to a 911 station. There, an operator receives and decodes the capsule and initiates appropriate steps, in real time.

(c) Virginia is a service specialist with Daimler-Chrysler. When something goes wrong with a customer’s late model Mercedes sedan on an important trip, the on-board computer sends short, precisely coded diagnostic information to Virginia’s small hand-held/ pocket device. The device alerts Virginia who decodes the received messages, enabling relatively quick diagnoses of what could be wrong with the vehicle. She is better prepared for all likely possibilities when she arrives at the scene for repairs within the hour.

(d) Jack, a hazardous materials expert, monitors packages on a conveyor system with the help of an expert system. The system scans each package and sends a report to the human decision maker. Based on this information, Jack makes a quick decision on how to deal with each package, without actually seeing or handling any of them.

Each of the above scenarios depicts a situation that conveys some urgency and involves ‘‘real-time’’ activity leading to categorizing or slotting the situation in some way during the course of making decisions. Some of the scenarios are realistic, others futuristic, even imaginary. In all of these examples, however, information concerning the situation must be conveyed quickly, yet precisely and unambiguously. Delays or errors in receiving a message, or in processing a received message, could have potentially serious consequences. Each represents a situation where speed and accuracy are both important.

Confusion is inherent in crisis situations. When a rape or knife-attack victim dials 911, she is in no condition to articulate her plea for help in the most ‘‘efficient and effective’’ way, especially if the perpetrator is suspected to be still in the vicinity. Yet, the nation’s aging 911 system continues to fully rely on audio phone calls to initiate its response. Improperly trained, inexperienced, overwhelmed, and, sometimes, callous operators tend to compound an already-difficult situation. Instead, a system where a precanned message is dispatched from a special device (perhaps, bundled with a telephone) could possibly help cut down on the likelihood of errors and delays in conveying/comprehending what occurred, to whom, and where. The hazardous materials expert must make quick, accurate decisions. If he takes an undue amount of time with one package, it or other packages awaiting examination may detonate. Yet, if he makes a mistake with a package, this again could result in equally serious repercussions. A system equipped to convey essential features of a package using a precise, predetermined vocabulary alleviates such costly risks.

It is desirable to keep message length short and precise for two reasons. First, a short, precise message helps quickly convey what needs to be conveyed by reducing communication delays and the likelihood of transmission and/or imprecision-induced human errors. Second, despite their plummeting prices, functionally versatile, electronic computing machines like the seemingly ubiquitous desktop and laptop PCs are seemingly giving way to smaller, lighter, and more mobile functionally ‘‘narrow’’ units, such as pagers, web phones and PDAs. This movement is being fueled by the communication revolution that has superseded the computing revolution of the 70s, 80s, and early 90s. The smaller and lighter the device, the more portable it is, but the less memory and display it usually accommodates. Of special interest to us are devices that are intended for handling short, ‘‘bursty’’ traffic (as in our example scenarios) rather than sustained, high-bandwidth communications (e.g., the contents of a book or a videocassette).

Our investigation occurs within a context of timepressured, performance-based incentive-driven settings, very similar to those faced by the decision makers in the example scenarios described above. We examine the performance of subjects when utilizing different kinds of information presentation ‘‘modes. In particular, we study the efficacy of a new, symbolic communication mode that we call ‘‘Image’’ (and which is distinct from the familiar ‘‘icons’’) vis-a\`-vis traditional written and spoken English which we call ‘‘Text’’ and ‘‘Audio,’’ respectively.

Given the small display of the decision support devices of interest, written English presents at least two disadvantages. First, it must be presented and understood linearly and sequentially, from left to right. This imposes time delays in both presentation and comprehension. Second, if the message being conveyed is not succinct enough for the display, then one must resort to moving (i.e., in ‘‘leading’’ form) displays or fragmented presentation. Both approaches have the disadvantage that the message is not available in its entirety or in substantial-enough chunks for sustained viewing. Spoken English has all of the disadvantages of a moving textual message (perhaps in exacerbated form) with the added drawback of offering no visual support.

Despite such drawbacks, traditional written and spoken communications dominate human – human interaction and, the former, much of human –machine interaction. The symbolic mode that we study is intended as one alternative, in the particular classification decision setting considered, to alleviate the drawbacks of the more traditional approaches. Yet, it is one that is entirely unfamiliar to new users, such as our subjects. Given identical experimental conditions for all modes, our subjects would have to comprehend and apply the novel Image mode within the same time and other restrictions made available to them when using the considerably more familiar Text and Audio. If our subjects performed just as well, or better, with the new language, then we would have a basis for further exploration of this and other such languages.

For ease of exposition, we report this study in two parts. Part 1 (the current paper) provides the motivation and background for the work reported in Part 2. Part 2 [28] describes the design, execution, and findings of an exploratory study of subject ability to recall and apply decision support information presented using each of the three communication modes—Text, Audio, and Image—in the presence of induced time pressure and performance-based financial incentives.

The remainder of Part 1 is organized as follows. In Section 2, we present a taxonomy and review of relevant literature. In Section 3, we describe key distinguishing features of our research vis-a\`-vis prior media-related and multimedia systems-related studies. Section 4 is concerned with the three kinds of information made available to a subject during experimentation: that concerning classification rules, sample objects, and to help make a final decision. The section concludes with a discussion on a product called the Training Tool Set developed for training our subjects. In order to make sure that the generic features and experiment-specific settings of the platform and tool set were adequate, we had these critiqued by a diverse group of individuals. Section 5 describes this effort. Section 6 contains concluding remarks.

## 2. A taxonomy and review of relevant literature

This section organizes and reviews relevant past literature. For convenience, we group this literature into the six categories shown in Table 1. Categories 1, 2, 3,

<table><tr><td>Literature on</td><td>Relevant papers</td></tr><tr><td>(1) Task PerformanceUnder Time Constraints</td><td>(1) Benbasat and Dexter [3](2) Chen and Tsoi [9](3) Chechile et al. [8](4) Hwang [19]</td></tr><tr><td>(2) LaboratoryExperimentation and Induced Value Theory</td><td>(1) Smith [38](2) Smith [39](3) Hoffman and Spitzer [18](4) Smith [40](5) Smith and Walker [41](6) Smith and Walker [42]</td></tr><tr><td>(3) Contrasting Ex-Ante and Ex-Post Systems Evaluation</td><td>Gardner et al. [14]</td></tr><tr><td>(4) Representative Ex-Ante Evaluations of(a) Support Systems</td><td>Gardner et al. [15](1) Sleeth et al. [37](2) Maltby [27]</td></tr><tr><td>(b) Media in Support Systems</td><td>(1) Sanders and Courtney [34](2) Mahmood and Medewitz [26](3) Snitkin and King [43](4) Doll and Torkzadeh [10](5) Money et al. [30](6) Sharda et al. [36](7) Barki and Hartwick [2](8) Madsen [25](9) Roth and Barthlome [33]</td></tr><tr><td>(5) Representative Ex-Post Evaluations of(a) Support Systems</td><td>(1) Sanders and Courtney [34](2) Mahmood and Medewitz [26](3) Snitkin and King [43](4) Doll and Torkzadeh [10](5) Money et al. [30](6) Sharda et al. [36](7) Barki and Hartwick [2](8) Madsen [25](9) Roth and Barthlome [33](1) Halasz [17](2) Carr [7](3) Sudhakar et al. [45](4) Kirschenbaum and Arruda [23](5) Fuerst et al. [13](6) Garzotto et al. [16](7) McFarland [29]</td></tr><tr><td>(b) Media in Support Systems</td><td>(1) Halasz [17](2) Carr [7](3) Sudhakar et al. [45](4) Kirschenbaum and Arruda [23](5) Fuerst et al. [13](6) Garzotto et al. [16](7) McFarland [29]</td></tr><tr><td>(6) Other Media-Related Studies</td><td>(1) Ware and Beatty [47](2) Fisher et al. [12](3) Fisher and Tan [11](4) Carlson and Ram [6](5) Pastoor [32](6) Travis et al. [46](7) Bieber and Kimbrough [5](8) Park and Hannafin [31](9) Lohse et al. [24](10) Bieber [4](11) Schwabe and Rossi [35](12) Steinmetz [44](33) Wolf [50]</td></tr></table>

4a, and 4b, are concerned with key aspects of our study—i.e., task performance under time constraints, the use of laboratory experimentation, induced value theory, and the ex-ante evaluation of systems and alternate media—and we restrict our review to these. In each case, we focus on experimental conditions, rather than findings, as the former is more relevant to this work. Categories 5a, 5b, and 6 are concerned with ex-post evaluation of support systems and recent media-related research. There is a rich literature in cognitive psychology relating to images in information processing and decision making; however, the direction and voluminous nature of this research suggests that attempting a thorough review here would lead us far a field. The interested reader is referred to the detailed summary provided in Ref. [49].

As Table 1 shows, we found a relatively larger number of studies pertaining to each of the categories 5a, 5b, and 6, spanning the last 10 to12 years. During the same period, available literature on decision making under time constraints (Category 1) and ex-ante experimental evaluation of media in support systems (Category 4b) are much smaller in number. Further, we have come across none that cut across categories 1, 2, and 4b, These findings reflect support for our opinion that no prior studies utilizing the kinds of features present in our study (as detailed in Section 3) are likely.

## 2.1. Literature on task performance under time constraints

Benbasat and Dexter [3] assess the influence of tabular reports, graphical reports, and combinations of the two under monochromatic and multicolor settings upon a budget allocation decision-making problem under two different time constraints. They used sixtyfive subjects (pretested for color blindness) across the twelve treatments. One training instance and two experimental instances of the problem were used for all subjects. To preserve experimental integrity, no immediate feedback on performance was provided to the subjects. The top three performers in each treatment were offered fixed monetary rewards. Each subject spent no more than 15 min on the experiment. Subjects were also given the opportunity of applying knowledge gained from the experiment to an actual problem as an added incentive. Because several subjects indicated that this opportunity, rather than the monetary rewards, was the main reason for their participating, the authors feel that ‘‘experimental realism’’ was preserved.

Chen and Tsoi [9] examine factors impacting the readability of moving text. In one experiment set, text was presented in ‘‘leading’’ format with discrete jumps of one or more characters as the text moved from right to left. Two display rates and three jump lengths were examined within two display window sizes for a total of 12 treatments. Thirty paragraphs from a book were used in the study of which six were used for practice sessions. Each paragraph was accompanied by four multiple choice comprehension questions. Twentyfour undergraduates participated for course credit in an introductory psychology class. In the second set, they examined the role of subject control over display rate on their performance. A different set of 24 subjects again participated for course credit in this experiment.

Chechile et al. [8] are concerned with modeling the ‘‘cognitive content’’ of displays and apply their approach to a dynamic display of avionics information. The typical approach to display quality analysis focuses on issues like luminance, contrast, resolution, legibility, and such. The authors believed that cognitive quality was the most important in display analysis and should be given adequate consideration during analysis rather that during design. They conducted a simulation experiment to assess four independent quantitative measures of cognitive complexity by exposing seventy university students to the same seven problem scenarios. Fifty-four chose to receive monetary compensation. Sixteen elected to receive participation credit in their introductory psychology course. Instruction time was varied to allow sufficient time for participants with different skill levels to get educated. Each subject spent about a 1.5 h on the experiment.

Hwang [19] presents a model for information systems research concerned with decision making under time pressure. While time has been examined as a dependent variable (e.g., response time) in the vast bulk of IS research, few studies have attempted to examine the impacts of time pressure and time horizon on performance. The author draws upon existing studies in psychology and the behavioral sciences to develop a model of decision making under time pressure. He uses this model to generate a series of research propositions.

## 2.2. ‘Literature on laboratory experimentation and induced value theory

Smith [38] describes and exemplifies his ‘‘theory of induced valuation’’ that forms the basis for ‘‘control’’ in laboratory experiments by using a suitable reward structure to induce prescribed monetary value on actions. Induced valuation relies upon the postulate of ‘‘non-satiation’’ which states:

Given a costless choice between two alternatives, identical except that the first yields more of the reward medium (usually currency) than the second, the first will always be chosen (preferred) to the second by an autonomous individual, i.e., utility is a monotonic increasing function of monetary reward, U(M), U V > 0.

Smith also offers several important qualifiers to the postulate that are relevant to our work. First, all situations may not be costless. Whenever subjective cost is present, induced value is diminished by some amount. An experimenter may overcome this difficulty in many ways, such as through raising the reward level and offering suitable commissions in addition to earned rewards. Second, rewards involving attaching ‘‘game value’’ to experimental outcomes in lieu of cash rewards could be weak, erratic, and easily dominated by subjective costs with subjects being readily satiated. Gaming boredom is more likely to follow an initial, pleasant experience of learning resulting in an increase in performance deviations with time.

Third, one must avoid needless ‘‘enrichment,’ such as when experimenters attempt to create the illusion of realism (e.g., by using jargon from the real world in describing an experiment to subjects). In order to try and maximize experimental control, the experimenter must try and ensure that the reward structure alone provides the singular source of valuation. Fourthly, individuals may not be autonomous own-reward maximizers if subjects have access to one another’s net rewards and are tempted to collude. Interpersonal considerations may overshadow autonomous behavior and special care must be taken to avoid this.

Smith [39] presents a highly theoretical treatment of laboratory experiments in economics and Smith [40] describes several illustrative market experimental methodologies. Hoffman and Spitzer [18] draw on the over twenty years of history of successful laboratory experimentation in economics to argue in favor of using this approach for testing legal theories and impacts of legal policies. Smith and Walker [41] examine the impact of substantial increases in the size of expected payoffs on subject behavior in an auction setting. They found that subjects did show a tendency to bid higher and that decision error decreased as payoff levels increased, although increasing expected payoff also increased the opportunity cost. Smith and Walker [42] observe that cognitive psychologists often take the position that either money does not matter or matters only insignificantly and, therefore, monetary rewards are unnecessary. The authors argue that rather than adopt either of the polar views—that ‘‘only rewards matter’’ or that ‘‘rewards do not matter at all’’—, it is better to acknowledge that ‘‘rewards do matter’’ and, therefore, ought not to be ignored. They survey a number of experimental studies, in support of their position, on the comparative effects of monetary rewards, including the absence of such rewards.

## 2.3. Literature contrasting ex-ante and ex-post systems’ evaluation

Our survey of the DSS evaluation literature shows a sizable bias toward ex-post evaluation. Gardner et al. [14] present arguments, based on Smith’s induced value theory, in favor of adopting ex-ante evaluation as a complement to ex-post evaluation. They present a pedagogical example from information economics where a subject must decide on the appropriate level of DSS consultations (i.e., information purchases) before making each production decision in a series of such decisions, given stochastic demand and three unreliable information sources.

## 2.4. Representative literature on ex-ante DSS evaluation

Gardner et al. [15] present a theory of the DSS evaluation/choice problem and test direct hypothesis concerning the theory and implications derived from it. They model the problem as a math program and apply this approach to the problem instance described in Ref. [14].

2.5. Representative literature on ex-ante media evaluation

Sleeth et al. [37] examine the effects of providing instructions and performance feedback using computerized speech synthesis on humans performing arithmetic manipulation tasks. Seventy-four undergraduate business majors enrolled in an organizational behavior class volunteered to participate. All subjects worked at separate times on the same series of four, timed, 5-min tasks.

Maltby [27] focuses on the issue of icon design within graphical user interfaces. The author notes that four popular Windows applications use different icons to represent five common tasks. Only one application allows icon customization. The experimental platform includes a matrix of twelve abstract word processing icons arranged randomly. The computer randomly generates and presents tasks to a subject who must select an appropriate icon. Maltby used 13 student volunteers from three graduate and undergraduate business computing courses. Each subject received immediate feedback on performance following each task. The same task set was used for all subjects, with 10 independent replications per subject. Up to five subjects performed the experiment concurrently, but independently.

## 3. Distinguishing features of this effort

This work differs from other media-related and multimedia systems-related studies in three important respects.

First, many prior studies (e.g., Refs. [3,8,9]) focus on the concept of ‘‘time horizon,’’ but not on ‘‘time pressure.’’ A time horizon is essentially a limit on an experiment’s duration. Pressure is induced when: (1) subjects are encouraged, through suitable incentive mechanisms, to not merely meet a time limit, but to beat it, perhaps by as much as they can; or (2) subjects must accomplish more difficult tasks within a time span more suited to relatively simpler tasks.

In our experiments, apart from an overall constraint on the duration of an entire experimental session, we established suitable time bounds for various activities within the session (including the ‘‘decision choice’’ step). We also constructed a reward/penalty structure that seeks to apply sustained, implicit time pressure on subjects by valuing speedy decision accuracy more than tardy accuracy, tardy accuracy more than tardy inaccuracy, and tardy inaccuracy more than speedy inaccuracy. The last of these reflects the fact that we wanted to encourage subject’s to try and succeed. Further, we constructed a task set containing tasks of three different complexity levels, all of which must be performed within the same time horizon and under the control of the same reward/penalty structure. Thus, we also attempt to exert explicit, increasing time pressure with increasing task complexity.

Second, in designing our experiment and choosing our incentive mechanism, we drew heavily upon pioneering work in induced value experimentation by Smith [38–40]. We took explicit steps to address the four concerns raised by Smith with regard to his postulate of non-satiation. Unlike earlier work (e.g., Refs. [3,8,9]), all subjects can earn performancebased rewards (including negative rewards) in real US dollars, where performance is measured in terms of speed, accuracy, and the willingness to commit to some decision as opposed to indecision.

Also, unlike previous work (e.g., Refs. [3,8]), we deliberately made the experimental task and its description (to subjects) as abstract and non-real-world as we could although, as described in Section 1, we had several real-world parallels in mind. To avoid collusion (see related discussions in Refs. [8,27,37]), our subjects work in isolation, we randomized problem instances across subjects, and permit no exchanges of any kind.

To mitigate the impacts, if any, of subjective costs, we structured a reward mechanism whereby a subject may earn as much as \$75.00 over a worst-case scenario of 6 h of participation (across three days). The prevailing minimum wage was \$4.25/h. The actual average payoff was about \$56.00 for an average duration of about 3 h, or a net of between four and five times the prevailing minimum wage. Finally, we offer continual performance feedback during the experiment whereby subjects can examine monetary and nonmonetary pastperformance statistics at any point.

Third, our study utilizes an ‘‘ex-ante’’ evaluation methodology [14,15], where subjects apply a hypothetical system to a hypothetical task in a tightly controlled laboratory setting. However, our exploratory work has implications for the kinds of example scenarios described in Section 1 and also for more refined studies in these and other domains.

Ex-ante evaluations offer a number of benefits. They help avoid the expense of creating and using fully implemented systems. Experimental controls are easier to administer in a laboratory. They facilitate the testing and modification of system theories prior to systems development. They can complement ex-post evaluation as each has unique virtues. In particular, ex-ante evaluation is useful at the start and early stages of ‘‘incremental’’ or ‘‘adaptive’’ system design posited by Keen [20 –22] with ex-post evaluations being used subsequently.

Despite such benefits, the vast bulk of studies on evaluating support systems (Category 5a of Table 1) and media influences in support systems (Category 5b) use ‘‘ex-post’’ evaluation where an actual, operational system is evaluated in either an actual task setting (i.e., fully ex-post) or a hypothetical setting (i.e., partially ex-post).

## 4. Prototype system characteristics and features

The remainder of Part 1 focuses on the design, development, and refinement of the experimental platform and related software that we believe are major contributions of this research. We created the platform and related software using the Asymetrix Multimedia ToolBook Version 3.0 package and deployed these on five Gateway 2000 P5-120 PCs running Windows 3.1 that were part of the erstwhile MIS Research Lab of the C.M. Gatton College of Business and Economics, University of Kentucky. Each station was equipped with a Creative Labs 16-bit SoundBlaster card, a pair of Optimus LV-20 Headphones, and a 15-in. Sony Vivitron 1572 (color) monitor.

Fig. 1 depicts the flow of events in a single experimental session (see Ref. [28] for a detailed description of the experimental study). From the figure, note that a session (E, in the figure) is made up of multiple experiments. Each experiment relies on a subject first having been exposed to a ‘‘classification rule set’’ (R). Following this, one or more ‘‘objects’’ (O) are presented to the subject for classification in accordance with some applicable rule from the set. If he/she is unable to recall the appropriate rule for each such object, a ‘‘system help’’ facility may be invoked to help with rule recollection. Once a rule is recalled/ chosen, the subject must apply it to classify the object (hopefully, correctly). As the figure shows, time bounds limit various epochs in this sequence. Further, the sooner a correct decision is made, the higher the reward earned and the sooner an incorrect decision is made, the more severe the penalty. The session ends when a predetermined number of objects, based on a predetermined number of rule sets, have been offered for classification and the session clock times out.

From the above synopsis and Fig. 1, observe that during the course of an experimental session a participant either seeks, or is offered, information concerning classification rules, objects offered for classification (i.e., samples), and to help make a final decision. In all three cases, depending on the session in question, the information is made available using a specific information ‘‘source.’’ In what follows, we discuss each of these three kinds of information and the different sources. Prerequisites for such a discussion include an understanding of concepts like information modes and flow rates (S, in Fig. 1), and rule complexity levels (L) that we introduce on an as-needed basis.

## 4.1. Classification rules

Classification rules tell a subject how objects (defined below) ought to be categorized based on their characteristics or features. Each rule has an IF part that describes what condition(s) must be met for the action in the THEN part to be taken. A rule’s complexity is based on the number of conditions involved. The simplest rules only have one condition. Rules with multiple conditions are stipulated by combining individual conditions with the connectives ‘‘AND’’ and ‘‘OR,’’ as appropriate. The most complicated rules have a combination of three conditions.

A ‘‘condition’’ describes the characteristics of an object as viewed from a certain perspective or ‘‘view.’’ An object can have as many as six views labeled View 1, View $2 , . . . ,$ View 6. Each view can contain as many as four ‘‘pins.’’ Its label and the number of pins it contains characterize a view. The action part of a rule tells which ‘‘bin’’ to place an object in if its characteristics match those in the rule’s condition. Depending on the experiment, as many as eight bins labeled Bin 1, Bin $2 , . . . ,$ Bin 8 may be offered. In what follows, we describe how we construct and present rules of various complexities to a subject.

![](/api/attachments/KCM4GPVU/fulltext/images/c9414e401c60a7d68ca1d71bbbe47ade1c4d33d745f2d28f2638d8f8d4edd3f5.jpg)  
Fig. 1. Event flow in a single experimental session.

## 4.1.1. Information sources

Rules (and other object-related information) are conveyed to a subject using one of several different sources. Each source combines an information presentation mode with an information presentation rate (the ‘‘flow rate’’ or ‘‘speed’’) and offers information of a certain complexity level. There are three modes (Text, Audio, and Image), three flow rates (Slower, Normal, and Faster), and three complexity levels (Level 1, Level 2, and Level 3). This results in 27 information sources (i.e., Text-Slower-Level 1, Text-Slower-Level 2, . . ., Image-Faster-Level 3). For example, a ‘‘Text-Level 1-Normal’’ source offers information about a single view in written English text that is rendered visually at Normal speed.

## 4.1.2. Information modes

Multimedia systems permit system-to-user dialog through different information modes like Text, (still) Image, Audio, Video (moving images), Stories (a sequence of still images), and combinations of these. Our experiment explores specific versions of the three basic modes, namely, Text, Image, and Audio. Further, we restricted ourselves to the use of gray scale colors for both Text and Image and, in the latter case, had our subjects rely on an image’s shape, rather than its color, to help differentiate it from another. In both cases, we refrained from using color for several reasons. First, given the exploratory scope of our study, we were not interested in examining the impact of color. Second, color had no natural role to play in our abstract object classification scenario. Third, using color for cosmetic appeal could result in unintentional biases. Fourth, because each subject would participate over several hours spread across multiple days, it would be necessary to continually monitor each participant to guard against the sudden onset of color blindness.

In Text and Image, each rule is displayed on the monitor. In Audio, a rule is identical in wording to its textual counterpart, but is conveyed orally via audio headphones. In the following two sections, we describe how rules were generated along with representative examples in Text and Image.

4.1.3. Rules characterized by a single view (Level 1 classification rules)

Rules involving a single view are the least complex of the three kinds of rules that we employ. Such rules involve information characterizing any one of the six possible views of an object in the IF portion. With six possible views and up to four pins per view, we can create $6 \times 4 = 2 4$ distinct rule conditions. For each condition, we used a random process to assign one of four bin number choices (i.e., action choices) to the THEN portion of the rule. The randomization was done to enable us to offer different rules to different subjects on (the same and) different days. This was to mitigate the risk of subjects exchanging rule knowledge with one another (within and) outside of the experimental setting. We refer to single-view rules as being of ‘‘Level 1’’ complexity. Here is an example Level 1 classification rule shown in actual font and size:

Level 1. Text Rule:

If View 2 has 3 pins, then choose Bin 3.

The same rule in Image:

![](/api/attachments/KCM4GPVU/fulltext/images/7929f31e04b06477b8a7788900b747a87a74109a245726acc047747ed3182e59.jpg)

![](/api/attachments/KCM4GPVU/fulltext/images/c42c09658d64b676bf46bdba214880af2cf55b260627974544baed2c75edf11e.jpg)

![](/api/attachments/KCM4GPVU/fulltext/images/bca6b1d739e7f0abeb6e983c27d883225ded82fb93ff6f81364925b1d552776c.jpg)

In Image, ‘‘View 2,’’ denoted using a square and ‘‘has three pins,’’ is captured using the three black dots within. ‘‘Bin 3’’ is denoted using a special symbol with the number three on its side. The arrow represents the words ‘‘then choose.’’ We used the following shapes to denote the six views:

![](/api/attachments/KCM4GPVU/fulltext/images/1522f21cea8e3f6c3ecff93e28b029e743d3f575d234010e31b6d8e5cce01f78.jpg)

![](/api/attachments/KCM4GPVU/fulltext/images/8cdafe4c024c9bad493449729cead5653483e69103ecf35a4b86606cf50d6653.jpg)

Triangle (for View 1)

![](/api/attachments/KCM4GPVU/fulltext/images/0e98be6edc4364ffea8062cacf80db21068b6903002cba8f75cec3200889e8c4.jpg)

Square (for View 2)

Circle (for View 3)

![](/api/attachments/KCM4GPVU/fulltext/images/adfd845ad6756f316ffeaeada2c81588399b7fbb6e0cb3e96331b47c81f54c44.jpg)

![](/api/attachments/KCM4GPVU/fulltext/images/ff772e73acc3cdd8e405755d40e867ec30f91722aa41c42888fbd09a261b59de.jpg)

![](/api/attachments/KCM4GPVU/fulltext/images/819a6face66befce7a8b06c5f46fb7d73e5c92ea7056d1a4cbff8db4349d4c8f.jpg)

Pentagon (for View 4)

Ellipse (for View 5)

Star (for View 6)

4.1.4. Rules characterized by two and three views (Level 2 and Level 3 rules)

More complex rules, involving two and three of the six possible views and the use of connectives are created in a similar manner and are referred to as Level 2 rules and Level 3 rules, respectively. Here are examples:

Level 2. Text Rule:

If View 2 has 3 pins and View 4 has 2 or 3 pins, then choose Bin 6.

The same rule in Image:

![](/api/attachments/KCM4GPVU/fulltext/images/de78ccbc628ae8da02663f59cf057aec1b47ad0992de55e6c2ebe3f1d5533d4b.jpg)

The symbol ‘‘-’’ represents ‘‘AND’’ and ‘‘V’’ represents ‘‘OR.’’ The phrase ‘‘and View 4 has two or three pins,’’ in Text is represented as, ‘‘and either View 4 has two pins or View 4 has three pins’’ in the Image equivalent. Thus, we use the most efficient way of conveying the same information in each mode.

A Level 3 rule features three views and the condition portions are even more complex than the twoview cases. For example:

Level 3. Text Rule:

If views 3 and 6 have 3 or 4 pins each and View 4 has 1 or 2 pins, then choose Bin 6.

The same rule in Image:

![](/api/attachments/KCM4GPVU/fulltext/images/bea945a020d8f780b073f921497a39f2220fb96fabb848883a53d6d8d8aa3eb3.jpg)

Complete rule listings for all three complexity levels are contained in Ref. [48].

## 4.1.5. Information speeds

Rules and other critical information are conveyed to a subject at one of three speeds called Slower, Normal, and Faster. To determine these speeds in each of the three modes and for each of the three complexity levels, we used ‘‘normal speech’’ as the base case. We measured the total time taken, and the pauses times between words, for a rule (of a given complexity) delivered using normal speech and used this information in two ways. First, these times helped us determine the timing characteristics for the Normal speed rendering of information using the remaining two modes—Image and Text. Second, we manipulated these times to determine the timing characteristics for the Slower and Faster speed renderings in all three modes. We detail the specifics in the following two sections.

## 4.1.6. The Audio-Normal information sources

Early in the research, we explored different approaches to generating synthesized voice on a computer to avoid having to depend on a human voice source. The monotonous sound, unnatural flow rate, background hiss, and the lack of clarity in some cases, disillusioned us. Our negative feelings are mirrored in prior studies like [37], where the authors note that synthesized audio:

(a) may be used for reprimands or negative feedback for correcting or improving performance; and

(b) needs comprehensive study in order to create productive matches and to avoid unproductive mismatches between individuals, voices, and tasks.

We, therefore, decided to record, manipulate, and replay actual human voice. Diction, accent, sentence delivery style, consistency, ad hoc availability, and affordability were paramount concerns in our final choice of a (female) human voice input source. We used a reasonably high quality Optimus Pro 50-MX head-mounted microphone and 16-bit SoundBlaster recording equipment to capture, manipulate, and replay audio. Recordings were done using the following Record Settings: Channels—mono; Sampling Rate—22050 Hz; Sampling Size—16 bits. These settings offered us the playback quality that we desired.

To satisfactorily address the concerns just mentioned, we used the following recording strategy. All of the rules at a given complexity level have several words in common. For example, consider the following two Level 1 rules:

Rule A. If View 1 has two Pins, then choose Bin 1.

Rule B. If View 1 has three Pins, then choose Bin 1.

When voiced, the two rules are identical except for the words ‘‘two’’ and ‘‘three.’’ Rather than record each rule in its entirety separately, we recorded Rule A first and then created other similar rules (like Rule B) by merely recording and substituting idiosyncratic words into a template generated from Rule A. We did our best to ensure that the quality of the voice recordings using this approach was indistinguishable (to the average human ear) from that of entirely recorded statements.

To listen to the replayed audio, each participant was supplied with a pair of Optimus LV-20 headphones.

Table 2  
Average times (seconds) needed to play audio rules at different speeds for different complexity levels

<table><tr><td colspan="4">Average total time</td></tr><tr><td>Speed/level</td><td>Level 1</td><td>Level 2</td><td>Level 3</td></tr><tr><td>Normal</td><td>5.00</td><td>8.17</td><td>10.64</td></tr><tr><td>Slower</td><td>6.56</td><td>11.23</td><td>17.83</td></tr><tr><td>Faster</td><td>4.04</td><td>6.62</td><td>8.72</td></tr></table>

We held the Creative Mixer sound replay settings and headphone volume controls at constant levels for all subjects.

## 4.1.7. The Audio-Slower and Audio-Faster information sources

We generated Slower and Faster versions of the Audio-Normal sources by manipulating the WAV files created for the latter. The Slower speed was achieved by increasing all pause times between words in Normal speed by approximately 50%. The Faster speed was achieved by reducing pause times by the same amount. The overall impacts of these manipulations on the total time needed to play back Audio rules at each of the three complexity levels are shown in Table 2. However, our final commitment to these times was based on feedback obtained from a group of volunteers (see Section 5).

## 4.1.8. Establishing rule flow rates in Text and Image

The times shown in Table 2 for Audio formed the bases for constructing rules at the three speeds in Text and Image. The time taken to display an Image component or a single word in Text is negligible compared to that needed to convey it orally. To keep each flow rate (i.e., Slower, Normal, and Faster) across the three modes mutually consistent, we adjusted the pause times between words in Text and Image such that the total time for rule display remained (approx imately) the same as in Audio.

To achieve this, we counted the number of pause occurrences between words in Text and Audio and between symbols in Image. The number of pauses is the same in Text and Audio whereas, because of its nature, fewer pauses are needed in Image. For example, there are nine pauses in the 10-word rule, ‘‘If View 1 has three pins, then choose Bin 3.’’ The same rule in Image appears as follows, with the white spaces preceding and following the arrow symbol denoting the two pauses:

![](/api/attachments/KCM4GPVU/fulltext/images/7ae72d7f5938e6d9419c2935a74d9f53ac9ed161a95f43a1c1aa7c09ca7dfd40.jpg)

Thus, each of the nine pauses in the Text and Audio renderings of the above example occupies 0.56 s at Normal speed, whereas the two pauses in the Image equivalent each occupies 2.50 s. Because of the near-instantaneous speed at which each Image component can be displayed by a modern computer, the Normal-Level 1 rule display time of 5.00 s for Image is (almost) entirely made up of the two pause times of 2.50 s each. Level 2 and Level 3 rules were similarly generated at all three speeds for Audio and Text.

## 4.1.9. Rule display

As Fig. 1 depicts, a subject participates in a series of experiments following exposure to a set of rules (in a given mode-speed-complexity level setting). This is followed by exposing the subject to another set of rules and a series of experiments based on the new set. This process continues for the duration of the experimental session.

Given the multiple rules in a set, we introduced a pause time between rules to allow subjects some time to examine a rule before presenting the next rule in the set. To hold this inter-rule pause time the same across all three modes, we used the constant pause time between the words of a rule in Text (or Audio) at a given speed-complexity setting as the basis for determining this time for all three modes at that setting. (Recall that the Text/Audio inter-word pause times are smaller than the inter-symbol pause times in Image.) The inter-rule pause times were established by doubling these inter-word pause times and are shown in Table 3.

Table 3  
Inter-rule pause times (seconds)

<table><tr><td colspan="4">Inter-rule pause time</td></tr><tr><td>Level/speed</td><td>Normal</td><td>Slower</td><td>Faster</td></tr><tr><td>Level 1</td><td>1.12</td><td>1.46</td><td>0.90</td></tr><tr><td>Level 2</td><td>0.96</td><td>1.32</td><td>0.78</td></tr><tr><td>Level 3</td><td>0.96</td><td>1.62</td><td>0.80</td></tr></table>

## 4.2. Presenting sample objects for classification

A rule set presentation (see Fig. 1) is followed by a series of samples offered for classification. Each such sample characterizes an object instance that fits one of the rules in the set and is presented using the same mode and speed as the rule set. A subject either tries to correctly classify a sample as belonging to a specific category (i.e., bin)—by recalling the appropriate rule or asking the system for help in recalling the rule (see Section 4.3)—or may fail to classify it. Here, we use the following Level 2 rule set instance in Image to illustrate the generation of samples:

![](/api/attachments/KCM4GPVU/fulltext/images/67f7fd15419a1510991bce60c932a98e0632d7348a08f81170ba286d14fc8383.jpg)

It is possible to generate six samples that fit the above rules. The two samples that fit the first rule are:

![](/api/attachments/KCM4GPVU/fulltext/images/606d687d0b4ba4d92e1f35468be9b9bb21d60a72ae670818fa0b5ac63769a437.jpg)

Being a Level 2 rule set, all samples are characterized by two views. In such, and other multiview, cases the first view in a sample is displayed first followed by a pause time that takes the place of the ‘‘AND’’ connective shown in the sample instances. At the end of the pause time, this view disappears and the next view appears followed by the same pause time. This process continues until a subject has ‘‘looked at’’ the object from all of the appropriate perspectives. As we did in the case of classification rules, we used data gathered from the Audio-Normal source as the basis for determining sample view display times at other mode-speed combinations. Table 4 displays the average times to convey information about one view (as in, ‘‘View 1 has three pins’’) at each of the three speeds for all three modes.

Average times (seconds) needed to convey information about a single sample view at different speeds

<table><tr><td>Speed</td><td>Average time</td></tr><tr><td>Normal</td><td>3.41</td></tr><tr><td>Slower</td><td>4.70</td></tr><tr><td>Faster</td><td>2.54</td></tr></table>

Inter-view pause times (seconds) for Level 2 and Level 3 samples at different speeds

<table><tr><td>Speed</td><td>Inter-view pause time</td></tr><tr><td>Normal</td><td>1.70</td></tr><tr><td>Slower</td><td>2.36</td></tr><tr><td>Faster</td><td>1.28</td></tr></table>

Table 5 shows the between-views pause times that we applied to the multiview Level 2 and Level 3 cases for all three modes.

## 4.3. The System Help facility

If a subject is unable to recall the applicable rule for a given sample, he/she may seek the system’s help in recalling it. The help facility prompts the subject to recall from memory the characteristics of the object that he/she was exposed to. The system then displays a rule that fits these characteristics. This rule may or may not be the correct one—it is entirely based on the subject’s recollection of the sample’s features.

The mechanics of how the help facility is invoked and how a subject interacts with it may be better understood by going through the detailed description of the Guided Platform Tour module of the Training Tool Set for the platform in Ref. [48]. A brief overview of the development of this tool set follows.

## 4.4. The Training Tool Set

In human subject-based experimentation, it is important that all subjects be exposed to the same set of instructions and the same types of training prior to beginning the actual experiments. Consistency in such regards may be attempted in a number of ways. For example, researchers often use written or taped (audio and/or video) instructions.

We experimented with a number of approaches to providing subjects with (a) an overview of the experiment that they would be participating in, and (b) a guided tour of the experimental platform that they would be using. After much deliberation and trial and error, we decided to make use of the same hardware used for the experiments along with custom-designed training software (also designed using Multimedia ToolBook) called ‘‘The Training Tool Set.’’ This software is made up of three modules: an ‘‘Experimental Overview,’’ a ‘‘Guided Platform Tour,’’ and a ‘‘Hands-on Session.’’ Each participant is automatically led from one module to the next once he/she begins training. Also, the modules were designed to be largely self-explanatory because we wished to minimize the extent of researcher interference during training to enhance training consistency across subjects.

The Experimental Overview module describes what is expected of a subject during the experiment. The Guided Platform Tour is an animated unit that leads a user through all of the salient features of the platform in a methodical way with significantly less effort than if the user had to manually ‘‘discover’’ its features. The Hands-on Session module allows a user to freely explore the actual platform to become more comfortable with it. Further module details and sequential screen dumps are contained in Ref. [48]. We next discuss how we refined these modules with the help of volunteer assessors. Section 5.5 contains a summarized discussion of the final experimental platform.

## 5. Prototype assessment and refinement

Prototype module assessment and refinement were done with the assistance of 31 volunteers. The group included nine doctoral, six masters, and ten undergraduate students as well as six Gatton College of Business and Economics, University of Kentucky, employees, including the MIS manager. The volunteers were brought into the lab at their convenience over a three-week period and asked to voice their opinions concerning the experimental environment, the Training Tool Set modules, and the actual experimental platform. Their concerns were recorded using pen and paper. If necessary, we asked for clarifications or for input on issues not already covered. Their criticisms enabled us to significantly enhance the setting and tools for the actual experiment. In what follows, we have classified the feedback obtained, and our reactions, into four categories: the Experimental Environment, the Experimental Overview module, the Guided Platform Tour module, and the Hands-on Session module.

## 5.1. The experimental environment

Four comments indicated crowding, one suggested untidiness, one suggested congestion, while thirteen others thought the general surroundings were convenient. The lab was thoroughly cleaned and configured as a decision room with ‘‘horse-shoe’’ seating. Fig. 2 shows the relocation of the five machines used in this experiment within this configuration. Subsequent volunteers found the new arrangement both comfortable and conducive enough to either explicitly comment on its convenience or not voice any complaints at all.

A few participants complained about the lighting and temperature conditions. All failed light bulbs were replaced and the room temperature was held at a constant 72<sup>j</sup> thereafter. Because outside light conditions could impact the lighting within the lab, we kept all window blinds closed to create a consistent, artificial lighting condition. Other concerns pertained to seating comfort and privacy. We equipped all five stations with adjustable chairs, encouraged participants to set chair heights to their convenience, and separated participants from one another using dividers.

## 5.2. The Experimental Overview module

Seven of the comments explicitly noted that the Experimental Overview module was good contentwise. Nine respondents, however, felt that it was too lengthy. Unfortunately, we were unable to reduce length without negatively impacting content and presentation quality. However, in response to the feedback that some sentences were too lengthy and that the pause between sentences was excessive, we reworded such sentences and reduced the pause times.

<table><tr><td></td><td colspan="4"></td><td colspan="2"></td></tr><tr><td>Chair</td><td colspan="4">Platform 5</td><td>Platform 1</td><td>Chair</td></tr><tr><td></td><td colspan="4"></td><td></td><td></td></tr><tr><td></td><td colspan="4"></td><td></td><td></td></tr><tr><td></td><td>Platform 4</td><td></td><td></td><td>Platform 3</td><td colspan="2">Platform 2</td></tr><tr><td></td><td>Chair</td><td colspan="2"></td><td>Chair</td><td colspan="2">Chair</td></tr></table>

Fig. 2. The location of the five platforms in the MIS research laboratory.

![](/api/attachments/KCM4GPVU/fulltext/images/21fb612da6f9a7539835635d5ea1a240bd39ae8304b67eba79c0fd148e07d323.jpg)  
Fig. 3. Navigational features of the ‘‘Experimental Overview’’ module.

While a negligible few expressed a desire for page numbers, we did introduce page numbers because a few others also wished to backtrack during the presentation to review select previous screens. This backtracking mechanism is depicted in Fig. 3. In response to a few comments, we also placed important terms in bullet form and underlined portions for added emphasis.

In using the Training Tool Set, subjects are required to either ‘‘click’’ or ‘‘press-and-hold’’ the left mouse button for a few seconds, depending on activity. Some respondents suggested that we substitute a mouse ‘‘right click’’ for press-and-hold while others suggested that we describe the operation using the words ‘‘click and hold’’ rather than merely saying ‘‘press.’’ While both suggestions have some merit, we also felt that:

(a) more computer users are used to the left click than the right click and to pressing (and holding)

the left button to drag objects around in a GUI environment;

(b) the term ‘‘press’’ was more succinct than ‘‘click and hold;’’ and

(c) the ‘‘press’’ operation was required very infrequently in comparison to the ‘‘click’’ in our platform.

The Experimental Overview and Guided Platform Tour modules were designed as audio–visual presentations, with subjects free to use either the aural or the visual component or both. We asked the volunteers to assess these modules with both components activated. A large number of volunteers complained that the audio was unintelligible unless the volume control device on the headset was kept at its maximum. We found that we could achieve better quality sound by manipulating the Creative Mixer settings instead and locked each participant’s headset volume control device at a specific position. A few volunteers also complained that the human voice used was monotonic, too dry, and/or too slow. We asked these individuals to specifically indicate which portions of the recordings were especially troublesome and redid these.

## 5.3. The Guided Platform Tour module

As with the Experimental Overview module some expressed concern over the length of this module. However, we were unable to find an effective way to reduce length without sacrificing content and clarity.

Recall that one kind of information available to a subject is that pertaining to applicable rules. We had initially used different examples in different modes to explain this facility. In response to four comments that the same example would help reinforce the facility better, we instituted this change.

A critical component of the user interface is a set of counters and clocks that display important information to the subjects. We adjusted both the location and contents of these windows in response to suggestions. Recall that different complexity levels offer different numbers of classification bin choices to the subject. In the prototype platform, the location of a specific bin button could change depending on the total number of bin buttons that had to be displayed. Two early volunteers strongly urged us to make sure that a specific bin button always appeared (if needed) at the same location on the interface, and we did. Likewise, due to space constraints, we had located a couple of Decision Cancel/Confirm buttons in an area of the screen called the Information Exchange area. We were asked to redesign the interface so that these buttons could also be located in the Control Panel area of the screen where all other non-informational buttons were located and we complied.

An excellent comment concerned the confusion that one assessor faced when he could not clearly distinguish between the terms ‘‘Bin’’ and ‘‘Pin’’ in Audio. He suggested that we use alphabets instead of numbers in one of the two cases. Unfortunately, we were unable to implement this suggestion as considerable time and money had already been spent in the audio recordings.

## 5.4. The Hands-On Session module

Initially, our Training Tool Set did not have an integrated Hands-on Session module. This module was added in response to a suggestion made by one of the early evaluators. The Hands-on Session is a time-limited version of the actual platform that enables a subject to carry on a mock experimental session. Subjects are provided with rule sets and samples involving all three modes, speeds, and complexity levels. Subjects make decision choices, etc., as they would in a real session. The only differences are that a subject does not earn real rewards and the duration is shorter than an actual session. While going through this process, volunteers came up with criticisms and complaints that they had overlooked when assessing the Experimental Overview and Guided Platform Tour modules.

Four volunteers indicated that the rule sets were too hard to comprehend in some cases and one comment indicated that the rule set display time was insufficient. We ignored these concerns as:

(a) the experiment was deliberately designed to contain some rule sets that were harder than others; and

(b) we intended determining a more suitable time for rule set displays through a pretest (see Ref. [28]).

Three participants found the multiple occurrences of numbers within a single rule in Text and Audio confusing. For example, a rule like ‘‘If View 1 has two pins and View 3 has one or two pins, then choose Bin 3,’’ contains six numerical entries. Some suggested using alphabets instead of numbers at some locations and changing some of the terminology (e.g., use ‘‘Bucket’’ instead of ‘‘Bin;’’ use ‘‘Face’’ instead of ‘‘View;’’ use ‘‘dot’’ instead of ‘‘pin’’). Recall that a participant had expressed a similar concern during the Guided Platform Tour assessment phase. Despite the small number of complaints, we felt that the suggestion was a good one; however, temporal and financial constraints prevented us from making the necessary changes.

A few people felt that the Hands-on Session module ought to offer more time with Image. While we did add more details to the explanation of this mode in the Guided Platform Tour, we refrained from offering more hands-on time with Image to maintain treatment consistency across modes. Further, some confusion with this mode was to be expected as, unlike Text and Audio, the ‘‘vocabulary’’ used in Image was unfamiliar to many of our subjects.

## 5.5. The final product and system – user interface

The final product and system–user interface were the result of a series of refinements made to the prototype based on various suggestions made by the assessors. Here, we outline key features of the refined product and provide an overview of how system–user interaction occurs. Key events in this dialog are depicted in Fig. 1.

The visual portion of the user interface is divided into two areas: the Control Panel area (the bottom third of the screen) and the Information Exchange area. The two areas are clearly visible in Fig. 4. Sometimes, the Control Panel may also occupy the right quarter of the screen. The Control Panel contains two main kinds of objects: buttons and information slots. There are four information slots located at the bottom right of the Control Panel area. These slots show the length of time a subject has been participating in the current experimental session, the length of time that the subject has spent on the current sample, the time remaining for the current sample, and the current sample number (see Fig. 4).

There are two kinds of buttons, namely, inactive and active. Active buttons appear in black and periodically blink to stimulate a subject to act. A subject may click or press on an active button. Whenever the cursor encounters an active button, it changes its shape from an ‘‘arrow’’ to a ‘‘pointing finger.’’ Inactive buttons appear in various shades of gray. As their name signifies, these buttons are currently unusable. Fig. 5, a screen shot from the preamble portion of the Training Tool Set, defines and exemplifies both types of buttons.

A subject begins his/her experimental session by clicking a special active button called the Start button. With Text or Image, a classification rule set containing three rules appears in the Information Exchange area. With Audio, the rule set is conveyed orally via the audio headset. In all three cases, the rule set is made available at a particular speed and pertains to a particular complexity level (depending on the experiment in progress).

A user may review a rule set by clicking yet another active button called the Redisplay button (for Text and Image) or the Repeat button (Audio).

![](/api/attachments/KCM4GPVU/fulltext/images/78f53bfc2de748597c9406a17196b74fa9566aaddf55e67f8c8c25a5f8378876.jpg)  
Fig. 4. ‘‘Control Panel’’ and ‘‘Information Exchange’’ areas of the user interface.

![](/api/attachments/KCM4GPVU/fulltext/images/0cc0b475a47b0621821e671ae87e7fa2aac75ba35ce65917b0c082459ccd13f2.jpg)  
Fig. 5. Roles played by ‘‘Active’’ and ‘‘Inactive’’ buttons on the user interface.

There is a finite time available for this activity called the Standard Rule Learning Time (SRLT; defined in Ref. [28]). An example rule set display in Text is shown in Fig. 6, a screen dump from the Guided Platform Tour module. Fig. 7 shows the same rule set in Image.

![](/api/attachments/KCM4GPVU/fulltext/images/5c0d06b586ebc5ac9b90a493179cc1a9eb52c9f1c19a71390ea23d79a1353bb1.jpg)  
Fig. 6. Example ‘‘Text Mode’’ rule set display in the ‘‘Guided Platform Tour’’ module.

![](/api/attachments/KCM4GPVU/fulltext/images/2128ffa7cde3a9707be23b33ed1edaa717071405230c632109b43d70647a20f4.jpg)  
Fig. 7. Example ‘‘Image Mode’’ rule set display in the ‘‘Guided Platform Tour’’ module.

Either when the SRLT expires or when the user clicks an active Continue button, the platform proceeds to the next stage, which is the generation and display of the first of a series of sample objects. Each sample in the series may be classified by recalling and using a specific rule from the rule set the subject was just exposed to. Information concerning the sample is also conveyed using the same mode-speed setting as the rule set. Depending on the complexity level involved, this information may pertain to one view, two views, or three views of an object.

A subject may examine an object and make a final decision within a prespecified time bound called the Standard Decision Making Time (SDMT; defined in Ref. [28]). Review of an object’s characteristics is possible through clicking or pressing down on a set of view redisplay buttons. Clicking on an active view button just reconveys information about that view whereas pressing on it reconveys information about all views characterizing the object beginning with that view.

At some point before the SDMT elapses the subject must make a classification decision. Otherwise, the system automatically records a ‘‘No Decision’’ outcome for this sample and computes an appropriate financial penalty (see Ref. [28] for details on the reward/penalty structure). Depending on how far the subject has progressed in the experiment, it then either proceeds on to the next sample for the current rule set, or the next rule set in the current session, or terminates the session by computing the total reward/penalty for the subject and reporting this to the researcher.

Within the SDMT, a subject may make a decision in one of two ways: without system help or with its help. If the subject requires help in reconstructing an applicable rule from the rule base, he/she invokes an active Help button. Upon invoking Help, the system prompts the user to supply it with characteristics of the sample in question. Based on the information the user supplies, the system retrieves a suitable rule from the rule base. Fig. 8 depicts an Image-mode dialog between the user and the system. Starting at the top of the figure, we see that the user has indicated (user selected responses are shown in black) that he/she was presented with a 1-View problem, that the view was an ellipse, and that it contained a single pin. The system has responded that the correct bin choice for such an object would be Bin 1.

The rule that is offered by the system in response to a help request is a function of the sample-related information that a user supplies. If this information were inaccurate, the rule offered would be inappropriate and could result in an incorrect final decision.

![](/api/attachments/KCM4GPVU/fulltext/images/1c22a5894cb7206aae9689be29342ee561caa95abe36238e954ead3095c19034.jpg)  
Fig. 8. Example use of the System Help Facility in the ‘‘Guided Platform Tour’’ module.

Regardless, the payoff for any correct decision made with the assistance of the Help facility is less than that made without such help. Likewise, the penalty for an incorrect decision made with system help is more severe than one made without help.

![](/api/attachments/KCM4GPVU/fulltext/images/fb64b606aa5e44aa96c621900b4cebec8264295af8e68963221cbf0c7ab845da.jpg)  
Fig. 9. Example ‘‘History’’ report display in the ‘‘Guided Platform Tour’’ module.

Eventually, a subject makes a decision by clicking on an active button called a Decision button. There are four decision choices (corresponding to the 4 bin choices) for the simplest, Level 1 problems. Level 2 and Level 3 problems employ eight such buttons. Fig. 8 also shows the four bin choices available for the 1-View problem the user was offered. Once the subject clicks a decision button, two active buttons called the Confirm and Cancel buttons appear in the Control Panel. The Cancel button enables the subject to change his/her mind about the final decision and to, optionally, backtrack to the sample review and/ or system help processes (if the SDMT has not elapsed).

Once the subject has made a firm bin choice, he/she clicks on the Confirm button. At this point the system calculates an appropriate reward or penalty for this decision. This quantity is then added to the existing total reward/penalty figure. The process continues with the system either displaying the next sample in the series, or displaying the next rule set in the session, or terminating the current session, as appropriate.

At any stage, a subject may review his/her current performance history by clicking a special, alwaysactive History button. The history displayed includes the number of experiments completed thus far, the number of Correct and Incorrect decisions made, the maximum, minimum, and average decision making times, and the net reward or penalty. An example History report is shown in Fig. 9.

## 6. Concluding remarks

In Part 1 of this two-part paper, we have:

(a) provided a strong motivation for this work by drawing on current technology trends and a review of the literature related to decision making under time pressure, induced value theory, ex-ante DSS evaluation, and ex-ante media evaluation;

(b) described how we constructed a prototype experimental platform to illustrate our ideas and an associated subject training application; and

(c) discussed how we assessed and refined these products to yield their final versions.

We parameterized the resultant final platform for use in the experiments reported in Ref. [28]. The platform is also flexible enough to permit a number of other experiments, such as the following.

One may allow a subject to choose an information source that is used with all experiments in a session or choose a source for each experiment in the session. In each case, we may then contrast performance using a fixed (either investigator- or subject-selected) information source against that using subject-selected sources.

One may apply the platform to competitive situations where subjects compete with one another for a share of a fixed reward pool. The experimental setting in this case must incorporate additional controls, most notably to guard against possible collusion between seeming competitors.

Extensions to the platform permit other interesting experiments. One may create ‘‘composite’’ sources that mix various modes and/or flow rates within a single experiment. For example, part of the information is supplied by a Text-Normal source while the remainder is offered by an Image-Faster source. One may add color as a control variable to Text and Image or examine alternate letter and image sizes. Likewise, one may also create variants of Audio by permitting voice to convey ‘‘moods’’ like happiness, excitement, urgency, exasperation, sadness, anger, and such.

One may define other kinds of sources than the three used here (e.g., those using colorized and/or monochrome full-motion video, still images, moving images, graphs, charts, music), broader speed ranges than the three that we studied, and other task complexity levels. Yet another extension [1] involves a scenario where decision making based on less than complete information is allowed. The focus is on discerning and evaluating participants’ subjective approaches to information gathering and decision making with different information sources in lieu of ‘‘optimal’’ strategies built into the experiment by the investigator.

## Acknowledgements

The authors express their sincere thanks to the three anonymous reviewers for their critical comments that enabled significant improvements to this two-part manuscript.

## References

[1] M. Aminilari, Searching for Information: Experiences with a Text-based and an Image-based Decision Support System, unpublished doctoral dissertation, Decision Science and Information Systems, School of Management, C.M. Gatton College of Business and Economics, University of Kentucky (2000).

[2] H. Barki, J. Hartwick, Measuring user participation, user involvement, and user attitude, MIS Quarterly 18 (1) (1994) 59– 82.

[3] I. Benbasat, A.S. Dexter, An investigation of the effectiveness of color and graphical information presentation under varying time constraints, MIS Quarterly 10 (1) (1986) 59 – 81.

[4] M.P. Bieber, On integrating hypermedia into decision support and other information systems, Decision Support Systems 14 (3) (1995) 251 – 267.

[5] M.P. Bieber, S.O. Kimbrough, On generalizing the concept of hypertext, MIS Quarterly 16 (1) (1992) 77 – 93.

[6] D.A. Carlson, S. Ram, HyperIntelligence: the next frontier, Communications of the ACM 33 (3) (1990) 311 – 321.

[7] H.H. Carr, Factors that affect user-friendliness in interactive computer programs, Information and Management 22 (3) (1992) 137–149.

[8] R.A. Chechile, R.G. Eggleston, R.N. Fleischman, A.N. Sasseville, Modeling the cognitive content of display, Human Factors 31 (1) (1989) 31– 43.

[9] H. Chen, K. Tsoi, Factors affecting the readability of moving text on a computer display, Human Factors 30 (1) (1988) 25 – 33.

[10] W.J. Doll, G. Torkzadeh, The measurement of end-user computing satisfaction, MIS Quarterly 12 (2) (1988) 259 – 274.

[11] D.L. Fisher, K.C. Tan, Visual display: the highlighting paradox, Human Factors 31 (1) (1989) 17– 30.

[12] D.L. Fisher, B.G. Coury, T.O. Tengs, S.A. Duffy, Minimizing the time to search visual displays: the role of highlighting, Human Factors 31 (2) (1989) 167 – 182.

[13] W.L. Fuerst, J.M. Ragusa, E. Turban, Expert systems and multimedia: examining the potential for integration, Journal of Management Information Systems 11 (3) (1995) 155–179.

[14] C. Gardner, J.R. Marsden, D.E. Pingry, The design and use of laboratory experiments for DSS evaluation, Decision Support Systems 9 (4) (1993) 369 – 379.

[15] C. Gardner, J.R. Marsden, D.E. Pingry, DSS evaluation: a comparison of ex-ante and ex-post evaluation methods, in: C.W. Holsapple, A.B. Whinston (Eds.), Recent Developments in Decision Support Systems, Springer, Berlin, 1993, pp. 439–455.

[16] F. Garzotto, L. Mainetti, P. Paolini, Hypermedia design, analysis, and evaluation issues, Communications of the ACM 38 (8) (1995) 74 – 86.

[17] F.G. Halasz, Reflections on notecards: seven issues for the next generation of hypermedia systems, Communications of the ACM 31 (7) (1988) 836– 852.

[18] E. Hoffman, M.L. Spitzer, Experimental law and economics: an introduction, Columbia Law Review 85 (5) (1985) 991–1036.

[19] M.I. Hwang, Decision making under time pressure: a model for information systems research, Information and Management 27 (4) (1994) 197– 203.

[20] P.G. Keen, Computer-based decision aids: the evaluation problem, Sloan Management Review 16 (3) (Spring 1975) 17–29.

[21] P.G. Keen, Adaptive design for decision support systems, Database 12 (1– 2) (1980) 15–25.

[22] P.G. Keen, Value analysis: justifying decision support systems, MIS Quarterly 5 (1) (1981) 1 – 15.

[23] S.S. Kirschenbaum, J.E. Arruda, Effects of graphic and verbal probability information on command decision making, Human Factors 36 (3) (1994) 406– 418.

[24] G.L. Lohse, H. Biolsi, N. Walker, H.H. Rueter, A classification of visual representations, Communications of the ACM 37 (12) (1994) 36–49.

[25] K.H. Madsen, A guide to metaphorical design, Communications of the ACM 37 (12) (1994) 57 – 62.

[26] M.A. Mahmood, J.N. Medewitz, Impact of design methods on decision support systems success: an empirical assessment, Information and Management 9 (3) (1985) 137–151.

[27] J.R. Maltby, An efficiency index for icon designs, Journal of Computer Information Systems 34 (4) (1994) 60 – 66.

[28] J.R. Marsden, R. Pakath, K. Wibowo, Decision making under time pressure with different information sources and performance-based financial incentives—Part 2, Decision Support Systems (current issue).

[29] R.D. McFarland, Ten design points for the human interface to instructional multimedia, T.H.E. Journal 22 (7) (1995) 67 – 69.

[30] A. Money, D. Tromp, T. Wegner, The quantification of decision support benefits within the context of value analysis, MIS Quarterly 12 (2) (1988) 223–236.

[31] I. Park, M.J. Hannafin, Empirically-based guidelines for the design of interactive multimedia, Educational Research and Technology Development 41 (3) (1993) 63– 85.

[32] S. Pastoor, Legibility and subjective preference for color combinations in text, Human Factors 32 (2) (1990) 151–171.

[33] L. Roth, L. Barthlome, The relationship between user participation in systems development and user satisfaction, Journal of Computer Information Systems 35 (1) (1994) 7 – 12.

[34] G.L. Sanders, J.F. Courtney, A field study of organizational factors influencing DSS success, MIS Quarterly 9 (1) (1985) 77– 93.

[35] D. Schwabe, G. Rossi, The object-oriented hypermedia design model, Communications of the ACM 38 (8) (1995) 45 – 46.

[36] R. Sharda, S.H. Barr, J.C. McDonnell, Decision support system effectiveness: a review and empirical test, Management Science 34 (2) (1988) 139 – 159.

[37] R.G. Sleeth, A.J. Wynne, G.S. Saunders, The case for speech synthesis: an experiment in human engineering, Information and Management 14 (5) (1988) 225 – 233.

[38] V.L. Smith, Experimental economics: induced value theory, American Economic Review 66 (2) (1976) 274– 279.

[39] V.L. Smith, Microeconomic systems in experimental science, American Economic Review 72 (5) (1982) 923 – 955.

[40] V.L. Smith, Experimental methods in economics, in: J. Eatwell, M. Milgate, P. Newman (Eds.), The New Palgrave: A Dictionary of Economics, vol. 2. Stockton Press, New York, 1987, pp. 241–249.

[41] V.L. Smith, J.M. Walker, Rewards, experience, and decision

costs in first price auctions, Economic Inquiry XXXI (2) (1993) 237– 245.

[42] V.L. Smith, J.M. Walker, Monetary rewards and decision costs in experimental economics, Economic Inquiry XXXI (2) (1993) 245– 261.

[43] S.R. Snitkin, W.R. King, Determinants of the effectiveness of personal decision support systems, Information and Management 10 (2) (1986) 83– 89.

[44] R. Steinmetz, Analyzing the multimedia operating system, IEEE Multimedia 2 (1) (1995) 68 – 84.

[45] G.N.M. Sudhakar, A. Karmouch, N.D. Georganas, Design and performance evaluation considerations of a multimedia medical database, IEEE Transactions on Knowledge and Data Engineering 5 (5) (1993) 888 – 894.

[46] D.S. Travis, S. Bowles, J. Seton, R. Peppe, Reading from color display: a psychophysical model, Human Factors 32 (2) (1990) 147–156.

[47] C. Ware, J.C. Beatty, Using color dimensions to display data dimensions, Human Factors 30 (2) (1988) 127 – 142.

[48] K. Wibowo, Subject Utilization of Alternate Information Sources in a Classification Task Setting: An Exploratory Study, unpublished doctoral dissertation, C.M. Gatton College of Business and Economics, University of Kentucky (1998).

[49] C.D. Wickens, Information processing, decision making, and cognition, in: G. Salvendy (Ed.), Handbook of Human Factors, Wiley, New York, 1987, pp. 72 – 107.

[50] B.P. Wolf, Intelligent multimedia tutoring systems, Communi cations of the ACM 39 (4) (1996) 30– 31.

![](/api/attachments/KCM4GPVU/fulltext/images/fccf0dedf893e0367bff80fdb21f65afb6a08b3db64f1baf5e4aadc64b4c8746.jpg)

Dr. James R. Marsden, the Shenkman Family Chair in e-Business, came to UConn in 1993 as Professor and Head, Department of Operations and Information Management, School of Business Administration, University of Connecticut. Dr. Marsden was part of a three-person concept development team that initiated and oversaw the development of the Connecticut Information Technology Institute and is currently serving as its Executive Direc-

tor. He developed and implemented the Treibick Electronic Commerce Initiative that is funded through a generous gift provided by Richard Treibick and the Treibick Family Foundation. Dr. Marsden also serves as Director of the OPIM/SBA MIS Research Lab and is a member of Advisory Board and Steering Committee of CIBER (Center for International Business Education and Research). He was a member of the edgelab development team and currently serves on the edgelab Steering Committee which selects and resources projects and oversees operations. Dr. Marsden was a winner of the initial Chancellor’s Award for IT Excellence and has a lengthy record in market innovation and analyses, economics of information, artificial intelligence, and production theory. His research work has appeared in Management Science; IEEE Transactions on Systems, Man, and Cybernetics; American Economic Review; Journal of Economic Theory; Journal of Political Economy; Computer Integrated Manufacturing Systems; Decision Support Systems; Journal of Management Information Systems, and numerous other academic journals. He was part of the IT Visioning and IT Planning Groups for the University and has played a leading role in developing the School of Business Administration as both a campus and national leader in IT education and research.

Professor Marsden received his AB (Phi Beta Kappa, James Scholar, Evans Scholar) degree from the University of Illinois and his MSc and PhD degrees from Purdue University. Having completed his J.D. while at the University of Kentucky, Jim has been admitted to both the Kentucky and Connecticut Bar. He is an Area Editor of Decision Support Systems and serves in a frequent external evaluator for major U.S. and international universities. He has held visiting positions at the University of York (England), University of Arizona, Purdue University, and the University of North Carolina. Jim was an Invited Lecturer at two NATO Advanced Study Institutes on Decision Support Systems and has given keynote addresses and university seminars throughout Europe and the Far East.

![](/api/attachments/KCM4GPVU/fulltext/images/84bd45c44ad62005ba905894377405fae557b4ab5cf66bf2463633a40fc27b7a.jpg)

Ramakrishnan Pakath is an Associate Professor of Decision Science and Information Systems at the University of Kentucky. Ram holds an MSE (OR and IE) degree from The University of Texas at Austin and a PhD (Management-MIS) degree from Purdue University. His research focuses on (a) designing and evaluating adaptive problem processors, and (b) assessing information source impacts on system user performance. Dr. Pakath’s

research articles have appeared in such refereed forums as Decision Sciences, Decision Support Systems, European Journal of Operational Research, IEEE Transactions on Systems, Man, and Cybernetics, Information and Management, and Information Systems Research. He is author of the book Business Support Systems: An Introduction published by Copley, now in its second edition. Dr. Pakath has also contributed refereed material to a number of wellknown books including Handbook of Industrial Engineering, Multimedia Technology and Applications, and Operations Research and Artificial Intelligence. He served as Director of the MIS Research Laboratory of the College of Business and Economics, University of Kentucky from 1993 to 1997. He is an Associate Editor for Decision Support Systems and an Editorial Board Member of Journal of End User Computing and Management.

![](/api/attachments/KCM4GPVU/fulltext/images/d165aeccd63701f58a2b6a89c427a8f01a1b25e0075a192f73a00ecc0125fb44.jpg)

Kustim Wibowo is an Associate Professor in the MIS and Decision Sciences Department of the Eberly College of Business and IT, Indiana University of Pennsylvania. He received his PhD in MIS from the University of Kentucky. Dr. Wibowo also holds an MSc in Computer Science from Baylor University. His current research interests include: e-commerce and web security, information systems for educational tech-

nology, human resource information systems, and OLAP (OnLine Analytical Processing) for managerial decision support.
