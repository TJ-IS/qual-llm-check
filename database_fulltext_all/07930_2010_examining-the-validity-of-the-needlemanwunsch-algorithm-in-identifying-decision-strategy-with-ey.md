---
otero_id: 7930
otero_key: "MFCDEEH5"
title: "Examining the validity of the Needleman–Wunsch algorithm in identifying decision strategy with eye-movement data"
authors: "Rong-Fuh Day"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.05.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Examining the validity of the Needleman–Wunsch algorithm in identifying decision strategy with eye-movement data

Rong-Fuh Day ⁎

Department of Information Management, National Chi-Nan University, No.1, University Rd, Puli, Nantou County, 54561 Taiwan, ROC

## a r t i c l e i n f o

Article history: Received 13 September 2009 Received in revised form 1 April 2010 Accepted 4 May 2010 Available online 31 May 2010

Keywords: Multi-attribute decision-making Eye-tracking approach Information search behavior Needleman–Wunsch algorithm Sequence alignment

## a b s t r a c t

A new generation of eye trackers shows us a promising alternative approach to tracing decision processes beyond the popular computerized-information-board approach. In order to exploit the eye-movement data, this study examined the validity of the Needleman–Wunsch algorithm (NWA) to characterize the decision process, and proposed an NWA-based classi<sup>fi</sup>cation method to predict which typical strategy an empirical search behavior might belong to. An eye-tracking based experiment was conducted. Our results showed that the resemblance score by NWA conformed to the assumption that the pair of information search behaviors based on the same strategy should have the closest resemblance. Moreover, with respect to our NWA-based classi<sup>fi</sup>cation method, our result showed that its overall prediction accuracy, hit-ratio, in identifying underlying strategies achieved 88%, signi<sup>fi</sup>cantly much higher than that gained from chance. On the whole, the combination of eye-<sup>fi</sup>xation data and our NWA-based classi<sup>fi</sup>cation method is quali<sup>fi</sup>ed.

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

The investigation of information search behavior has been a critical issue in the research <sup>fi</sup>eld of decision support systems [10,11,48]. Through observation of information search behavior, researchers can gain further insight into the decision process, which may lead to a deeper understanding of decision strategy. Theoretically, such insight is helpful in illuminating the mediating role of the mind, and offers more detailed explanations of the causal relationship between antecedent factors and the <sup>fi</sup>nal decision outcome. In addition, it contributes in particular to the effective designs of DSS, which serve to satisfy the diverse cognitive demands of users in terms of function, information display, etc. [14,41,47,51,53,54].

A prerequisite for success in this research area is an effective methodology to trace the inner operations of cognition. In general, this involves two interdependent principal parts: a process-tracing method followed by an analysis technique. In the past, several process-tracing methods have been proposed based on different kinds of behavioral cues, including think-aloud, information board, eye tracking, or computerized information board [8,11,30,35]. Among them, computerized information board (CIB) has been popular during the last two decades and, with its evolution, several aggregated indexes based on automatic analysis have also developed, which are dedicated to characterizing in a quantitative manner particular dimensions of information search processes. This has considerably advanced the objectivity of the research <sup>fi</sup>eld [8,30,49]. At the current stage of methodological development, one particularly signi<sup>fi</sup>cant attainment is that a theoretical distinction between compensatory and non-compensatory decision strategy can be easily made automatically, using the search direction index [8,35].

In addition to being a pure research methodology, the CIB approach has been considered for integration with DSS. One idea is to incorporate CIB and the analysis algorithm into DSS to enhance DSS's capacity to monitor users' information search behavior and to provide immediate, on-the-spot diagnosis of users' inner states. By so doing, DSS would be capable of providing responses better adapted to users' cognitive needs based on analysis results. For example, if a user were found to be prone to using attribute-based search strategies, DSS would be able to provide a more congruent information display to ease the execution of the strategies. Prior studies have shown evidence of such manipulations in information presentation experiments [5,7,22]. Alternatively, in line with the idea of decision-channeling [11,46,48,50], DSS would be able to respond in a totally different way by providing an incongruent information display to induce users to adopt the strategy preferred by the organization.

However, there have been hindrances in the development of the CIB approach. When applied to theoretical research or DSS design, one major inherent problem is that decision information on the CIB is always masked until users move the mouse pointer over it. This might cause two further limitations. One is that users' peripheral vision becomes constrained. Another is that it largely increases the effort required to access a piece of decision information, thus introducing additional interference to cognitive processes [30]. More seriously, when integrated into the interface design of DSS, the desired effects of some presentation designs on the screen are diminished. For example, highlighting information in salient colors or <sup>fl</sup>ashing changing information becomes ineffective because information is masked on CIB. In addition to the limitations derived from masking, relevant automatic analysis of process data seems inadequate to capture the diversity of search behaviors.

Recently, as a new generation of eye trackers has made great progress in terms of precision and convenience, a promising alternative approach has emerged which may alleviate the problems inherent in the CIB approach. Eye tracker has been traditionally used by psychological researchers to record eye movements considered as immediate cues to attention and cognitive process. Today's eye tracker has gained at least three remarkable advances with respect to functions. First, it provides abundant data about eye movements, such as <sup>fi</sup>xation, saccade, or pupil size, which supplies researchers with more thorough information on cognitive operations. Second, it is capable of tracking eyes in a more natural and non-intrusive manner, for example, by means of remote cameras. Third, in contrast with the traditional eye tracker, which provided behavioral research with merely a passive mode for post-experimentation access to eye-movement data, the modern eye tracker has an additional, active mode, in which eyemovement data can be accessed in real-time. As a consequence of these advances, researchers have argued for the need to re-evaluate the eyetracking approach for behavioral decision-making research [30] as well as for human–computer interaction [31,57].

In this study, we attempted to advance the traditional issue of identifying decision strategy in the following ways. First, we used the modern eye tracker to collect eye-<sup>fi</sup>xation data as cues for the decision process rather than mouse movements as used by CIB. Second, based on the <sup>fi</sup>ndings of previous research on decision-making, we proposed an automatic analysis method to identify speci<sup>fi</sup>c underlying decision strategies. Finally, we actually examined the effectiveness of our proposed method on eye-<sup>fi</sup>xation data.

Previous research in the domain of behavioral decision-making has established a solid body of knowledge about strategies used in solving choice problems, such as the weighted additive rule (WADD), the equal weight heuristic (EQW), the satis<sup>fi</sup>cing heuristic (SAT), the lexicographic heuristic (LEX), the elimination-by-aspects (EBA), the majority of con<sup>fi</sup>rming dimensions (MCD), etc. Moreover, based on the information processing perspective, a strategy can be broken down into a sequence of successive cognitive operations, or elementary information processes (EIPs) [4,37]. Taken together, it indicates to us that if a typical strategy is applied, we should describe in advance what serial steps, referred to in this paper as hypothetical steps, might be executed. Furthermore, this leads us to the idea that the strategy underlying an empirical search behavior can be inferred by observing how its actual steps resemble the hypothetical steps of known typical strategies. In other words, given a set of typical strategies and their corresponding hypothetical steps, the one with the highest resemblance in terms of executive steps is most likely to be the candidate strategy underlying the target information search behavior.

In order to realize the idea, an effective algorithm for automatic analysis is necessary. Since both hypothetical serial steps and actual serial steps of information search behaviors may be viewed as sequential data, we can reframe our analysis goal by comparing the similarity between two sequences in more general terms. For this purpose, we consider appropriate the sequence alignment algorithm, Needleman–Wunsch algorithm (NWA) [32]. In the past, this algorithm and its variants have been widely used in a variety of contexts, for example, bioinformics, sociology [1,2,17], customer retention[40], medical diagnosis[56], and communication [21], and in recent years, have gradually become accepted by eye-tracking based studies to analyze scanning path [9,15,24,34,45,55].

In order to validate our proposed method, we hypothesized that if the method is valid, it should re<sup>fl</sup>ect that an empirical search behavior and hypothetical search behavior, both based on the same strategy, are more similar in terms of resemblance score by NWA than pairs based on different strategies. In addition, we developed an NWAbased classi<sup>fi</sup>cation to predict which typical strategy an empirical search behavior might belong to. If the NWA is valid, the hit-ratio, i.e. percentage correctly predicted by this NWA-based classi<sup>fi</sup>cation, should be signi<sup>fi</sup>cantly higher than the percentage correctly predicted by chance. For this purpose, we designed a laboratory experiment for the multi-attribute and multi-alternative choice problem and used the modern eye tracker to collect <sup>fi</sup>xation data during decision-making, before implementing the Needleman–Wunsch algorithm to analyze the empirical data.

## 2. Literature review

## 2.1. Multi-attribute decision-making

A multi-attribute decision is characterized by a decision-maker's need to choose one brand out of a set of alternatives, where each alternative is described by a common set of attributes. Multi-attribute choice has been viewed as a typical decision problem requiring further support by IS. For example, researchers have suggested that IS can facilitate the decision-making problem through function design [51] or information display design [13,22,26]. In fact, this kind of decision-making problem is also important in the <sup>fi</sup>eld of decision behavioral research and consumer behavior because it is seen widely in daily life [4,6,37].

One approach to the study of decision-making stems from the information processing perspective. From this perspective, decisionmaking is viewed as a kind of problem-solving in which, given an initial problem state and goal, the decision-maker transforms the initial problem state into an array of temporal problem states step-bystep in the working memory until the goal state is achieved [20,33,37]. Therefore, the decision-making process can be subdivided into a set of elementary information processes (EIPs), such as read, compare, difference, add, product, eliminate, move, choose, etc. [3,4,23,36,37]. They are responsible for transforming problem states; for example, EIP add represents the cognitive operation of “adding the values of an attribute in STM”. Based on the set of EIPs, researchers are able to model a variety of decision-making strategies, and to estimate more precisely the processing effort for each decision strategy. We use the following example to explain the above idea in more detail. Suppose that, as Table 1 shows, a decision-maker needs to choose one protection lotion among two alternatives, where each is described by two common attributes, such as SPF and Polished. The numbers in parentheses are labels used to identify each entry for the following explanation. Using the weighted additive rule, a decision-maker is expected to read the <sup>fi</sup>rst weight (3) and then the rating on the <sup>fi</sup>rst attribute (5). The two numbers are then multiplied and the result score 2 is kept. The process is repeated on (4) and (6), and the result score 15 is attained. For Protection Lotion 1, the total score is 17, achieved by adding 2 and 15. A similar process is applied to Protection Lotion 2, and its total score is 18. Finally, the total scores for the two alternatives are compared; Protection Lotion 1 is eliminated and Protection Lotion 2 is chosen. More speci<sup>fi</sup>cally, using the EIPs, the entire decision process detailed above can be modeled as the following sequence: read (3), read (5), product, read (4), read (6), product, add, read (3), read (7), product, read (4), read (8), product, add, compare, eliminate, and choose. Further, based on the sequence of EIPs, the external information search behavior following the decision strategy should be observed in the following order: read (3), read (5), read (4), read (6), read (3), read (7), read (4), and read (8). The main difference between the sequence of EIPs and the sequence of external information search behaviors is that the latter sequence excludes some unobservable cognitive operations from the former. In other words, in this way, a typical abstract decision strategy can be embodied by a series of observable information acquisition steps. Here, for the ease of communication afterwards, such hypothetical behavioral steps simulated for a typical strategy is termed typical information search sequence (TISS). In contrast to TISS, the sequence of empirical external information search in decisionmaking is termed empirical information search sequence (EISS).

An illustrative multi-attribute and multi-alternative choice problem

<table><tr><td></td><td>SPF</td><td>Polished</td></tr><tr><td>Cutoff</td><td>4(1)</td><td>1(2)</td></tr><tr><td>Weight</td><td>2(3)</td><td>5(4)</td></tr><tr><td>Protection Lotion 1</td><td>1(5)</td><td>3(6)</td></tr><tr><td>Protection Lotion 2</td><td>4(7)</td><td>2(8)</td></tr></table>

## 2.2. Eye movement and cognitive processes

Previous research has suggested that eye movements are directly related to the underlying cognitive process, which is also known as the eye–mind assumption [25,42]. Just and Carpenter, for example, suggested that eyes often <sup>fi</sup>xate on the external referents whose corresponding internal representations are being processed. Various studies on tracking eye movements have produced evidence to illuminate the relationship between eye movement and cognitive processes in a variety of contexts, such as reading, perception, visual search, arithmetic education [18,19,27,28,39,42]. In the <sup>fi</sup>eld of behavioral decision-making, the application of eye movements to infer decision strategies also has a long history. For example, Russo and Rosen [44] recorded subjects' eye movements to observe how subjects solved a multi-attribute choice problem. Due to its high costs and poor performance, the eye-track approach has not been popular in the <sup>fi</sup>eld of behavioral decision-making.

The modern eye tracker has recently re-raised the interest of researchers in the eye-tracking approach. Currently, there are two different research directions in applying this approach, one of which focuses more on the problems of methodology itself. For example, Lohse and Johnson [30] performed several fundamental examinations of the differential impacts of two competing methods, the eyetracking method and the computerized information board, on a variety of aggregated indexes relating to information search behaviors. They found there existed signi<sup>fi</sup>cant differences, which they attributed mainly to the effort differential with respect to information acquisition in the two methods. Another approach simply uses the eye-tracking method as a type of process-tracing method. For example, Day et al. focused on the impacts of antecedent factors, such as <sup>fl</sup>ash banner and background music, on the decision strategy and thus, the <sup>fi</sup>nal performances [12]. The eye-tracking approach was used as a substitute for CIB because eye-movement data was considered to be more immediate to cognitive processes. The present study adheres more closely to the former approach rather than to the latter because we focus both on the development of a new framework to analyze eye-movement data and on assessment of the effectiveness of the framework.

Modern eye tracking is also characterized by its active mode in use, which allows information systems to access eye-movement data in real-time. Based on this mode, a variety of innovative interface designs have been proposed; for example, attentive user interfaces [52], capable of adjusting resolutions of each region of the screen according to the <sup>fi</sup>xations of a user, or affective computing [38], which uses eye movements to estimate the affective states of users and to make adaptive responses to those users. Although the current applications seem not to be immediately relevant to DSS, they provide us with a promising way to improve the user interfaces and functions of DSS.

In light of this trend, researchers and designers in the <sup>fi</sup>eld should learn more about eye movements, eye tracker and relevant analysis algorithms in order to gain maximum bene<sup>fi</sup>t from the advantages provided by the emerging approach. This study may be seen as an attempt to accumulate relevant knowledge and experience to this end.

## 2.3. Fixation sequence and the Needleman–Wunsch algorithm

Since eye-<sup>fi</sup>xation data inherently contains strong chronic information, which generally implies a decision process, the string-editing approach has been suggested for unearthing such information [9,15,24,34,45,55]. The main idea of the string-editing approach is to measure the resemblance/or dissimilarity between two strings (i.e. sequences) by calculating the minimum number of edit operations needed to modify one string to obtain another. Edit operations generally include insertion, deletion, and substitution. For example, supposing there are two strings, “bce” and “abcde”, we could perform two edit operations of inserting spaces into the former string in order to make the two look more similar, “\_bc $\underline { { \boldsymbol { \mathrm { e } } } } "$ and “abcde”. This index of resemblance is also known as Levenshtein distance in the <sup>fi</sup>eld of computer science [29]. The general way to arrive at the minimum number of edit operations is by means of the dynamic programming approach. In recent years, string-editing has gradually become popular in the eye-tracking approach. For example, in a study on perception of the same visual scene [28], subjects were instructed to perceive the “checkerboard” <sup>fi</sup>rst and then image it in an eye-tracking experiment. Researchers then used the string-editing method to analyze <sup>fi</sup>xation sequences to show that the scanning order of the elements during imagery correlated to the original order during perception. Josephson et al. [24] applied the string-editing method to validate the hypothesis that web viewers have habitual preferred scanning paths. Pan et al. [34] used this method to analyze the scanning path on web pages. Their <sup>fi</sup>ndings showed that the complexity of web page design in<sup>fl</sup>uences the degree of scanning path variation among different subjects on the same page.

In the present study, we utilize the Needleman–Wunsch algorithm, which is a variant of the string-editing algorithm. The main improvement afforded by NWA is that it uses a more <sup>fl</sup>exible scoring scheme, allowing the user to specify scoring parameters optimal for a given situation. This algorithm can be used to maximize the alignment scores between the sequences along the entire length of the sequences. For this reason, it is also called global sequence alignment. The work of NWA is described in brief in the following way. Suppose that there are two sequences X and Y. X consists of $x _ { 1 } x _ { 2 } x _ { 3 \dots } x _ { \mathrm { { m } } } ,$ and Y consists of $y _ { 1 } ~ y _ { 2 } ~ y _ { 3 \ldots y _ { \mathrm { n } } }$ . Initially, NWA set up a scoring schema, S, which is responsible for assigning scores for different two-character alignment scenarios. For example, a scoring schema can be as follows:

$$
\bullet \text {   If   } x _ {\mathrm{m}} = y _ {\mathrm{n}}, S (x _ {\mathrm{m}}, y _ {\mathrm{n}}) = 5.
$$

[This denotes that when the aligning characters match, 5 is attained.]

$$
\bullet \text {   If   } x _ {\mathrm{m}}! = y _ {\mathrm{n}}, S (x _ {\mathrm{m}}, y _ {\mathrm{n}}) = - 3.
$$

[This denotes that when the aligning characters mismatch, 3 is attained.]

$$
\bullet S (_ {-} y _ {\mathrm{n}}) = S (x _ {\mathrm{m}, -}) = - 1.
$$

[This denotes that when one character is aligned with an inserted $\mathtt { g a p } , - 1$ is attained. This score is also called gap penalty.]

With the scoring schema, we then build a matrix M of $( m + 1 ) ^ { * } ( n + 1 )$ where $M ( i , j )$ represents the score for the optimal alignment of partial sequences, $x _ { 1 } x _ { 2 } x _ { 3 \ldots } x _ { \mathrm { i } } ,$ and $y _ { 1 } y _ { 2 } y _ { 3 \ldots y _ { \mathrm { j } } } .$ The matrix is built via the steps that follow. First, M is initialized by the following rules: $M ( 0 , 0 ) = 0 ;$ $M ( i , 0 ) = i { \mathrm { ~ g a p } } _ { \ }$ \_penalty; $m ( 0 , j ) = j$ gap\_penalty. Second, each entry in the matrix is <sup>fi</sup>lled from upper-left to lower-right. This step needs further detailed explanation. Suppose we have <sup>fi</sup>lled in M $( i - 1 , j - 1 ) , M ( i - 1 , j )$ , and $M ( i , j - 1 )$ , i.e., the three entries above, to the left, and diagonally above and left of $M ( i , j )$ . These three entries indicate three corresponding ways to determine the i-th character of X and the j-th character of Y (as Fig. 1 shows); that is, we can either align $x _ { \mathrm { i } }$ with $y _ { \mathrm { j } }$ (in the <sup>fi</sup>rst case), align $x _ { \mathrm { i } }$ with a new gap (in the second case), or align $y _ { \mathrm { j } }$ with a new gap (in the third case). Each way then can generate an aligning score for the partial sequences respectively, and we choose the highest among them as the optimal score for $M ( i , j )$ . The corresponding direction for calculating the optimal score is registered as the optimal path for the use of the latter in backtracking. As Eq. (1) illustrates, S is a scoring function for different scenarios for aligning two characters, with each entry being determined by this formula recursively.

![](/api/attachments/MFCDEEH5/fulltext/images/26281e43e238178bb69c1759ebd2b80ce0c57d119634f8ff52764f84f98beb50.jpg)  
Fig. 1. There are three possible ways to calculate the value of $M ( i , j )$ with the highest score among the three ways being retained in M(i,j).

$$
M (i, j) = M a x \left\{ \begin{array}{l} M (i - 1, j - 1) + S (i, j) \\ M (i - 1, j) + S (i, \_) \\ M (i, j - 1) + S (\_, j) \end{array} \right.\tag{1}
$$

Once M has been built, backtracking is started from M(m,n), i.e. the lower-right entry, to the upper-left corner of M. In this step, we establish a way consisting of optimal paths registered. By backtracking, new aligned sequences, i.e. X′ and ${ \cal Y } ^ { \prime } ,$ are generated in the following ways:

$\mathfrak { H } M ( i , j )$ results from the diagonal above and left entry, $M ( i - 1 , j - 1 )$ then at the very beginning of $X ^ { \prime }$ and $Y ^ { \prime }$ would be placed x and $y _ { \mathrm { j } } .$

$\mathfrak { H } M ( i , j )$ results from the left entry, $M ( i , j - 1 )$ , at the beginning of X and $Y ^ { \prime }$ would be inserted respectively $\ " \_ { }$ (insert a space) and $Y _ { \mathrm { j } } .$

• If matrix M results from the above entry, $M ( i - 1 , j )$ , at the beginning of X′ would be inserted $x _ { \mathrm { i } } ,$ and at that of Y′ would be inserted “\_”(insert a space).

Finally, the similarity between X and Y can be computed in Formula (2).

$$
\text { Similarity } = \frac {A}{B}\tag{2}
$$

In Formula (2), A denotes the number of identical characters between X′ and Y′, and B denotes the length of X′.

## 3. Method

## 3.1. Overview

In this experiment, our goal was to collect empirical <sup>fi</sup>xation sequences while participants executed typical assigned decision strategies. These <sup>fi</sup>xation sequences were used as the representatives of EISSs and then further compared with TISSs.

We presumed that the EISS and the TISS derived from the same typical decision strategy should be the most similar. Based on this assumption, we further hypothesized that if NWA were a valid algorithm, it would produce the highest similarity score for the bEISS, TISSN pairs derived from the same typical decision strategy.

## 3.2. Participants

A total of 47 college students at the Southern Taiwan University of Technology, Taiwan, 13 males and 34 females (age range 18–28 years), were recruited as participants, each of whom was paid a cash reward of NT\$ 300 for their participation. In order to encourage them to make accurate decisions, an extra NT\$ 100 reward was granted when subjects demonstrated their intention to apply right decision strategies to trials.

## 3.3. Stimulus materials

The decision information necessary for the multi-attribute choice problem was arranged and displayed in the shape of an alternativeattribute matrix, which has been widely used in previous research on decision-making [4,7,37]. As Appendix A reveals, the information matrix consisted of four alternatives, each with four attributes. The layout of the information matrix was displayed in the medium resolution mode of 800 600 pixels.

## 3.4. Apparatus

An EyeLink II eye-tracking system (SR Research, Canada) with a sampling rate of 500 Hz was used to track and record the participants' eye movements (saccades and <sup>fi</sup>xations) while they performed the decision-making task.

## 3.5. Task and strategies

The experimental task was to apply typical assigned strategies to solve choice problems, the weighted additive rule (WADD), the satis<sup>fi</sup>cing heuristic (SAT), the equal weight heuristic (EQW), the lexicographic heuristic (LEX), the elimination-by-aspects (EBA), and the majority of con<sup>fi</sup>rming dimensions (MCD). Our operational de<sup>fi</sup>nitions of the decision strategies meticulously followed those of Payne et al. [37].

In order to keep each choice problem relative to another, we created equivalent variants of information matrix for a choice problem. The idea was randomly to switch columns designating the four attributes or rows designating the four alternatives in the matrix of decision information. In this way, we ensured that the variants derived from the same choice problem were equivalent in terms of level of complexity and other dimensions.

## 3.6. Design and procedure

One within-subjects factor was manipulated in the experiment, i.e. typical decision strategy, which consisted of 6 levels: the weighted additive rule (WADD), the satis<sup>fi</sup>cing heuristic (SAT), the equal weight heuristic (EQW), the lexicographic heuristic (LEX), the elimination-by-aspects (EBA), and the majority of con<sup>fi</sup>rming dimensions (MCD). That is, each subject was required to apply these six typical strategies to an equivalent choice problem respectively. The presentation order of all the six choice problems for each subject was randomized by the experimental program.

Before the actual experiment was conducted, participants were taught to use the six strategies in two training courses for a total of 2 h. Then the participants were tested individually in the actual experiment.

In the experiment, the experimenter <sup>fi</sup>rst put the eye tracker's leather-padded headband on the participant's head and calibrated the eye tracker. The calibration and subsequent validation took approximately 7 min to complete. Then, an experimental program designed for the study was launched. The program showed six trials randomly. Each trial consisted of two sections: First, the instruction screen was presented to instruct the participant to solve a follow-up choice problem with a typical assigned decision strategy, and to encourage him/her to arrive at a decision as quickly and accurately as possible. Second, an information matrix for a choice problem was shown. The main theme of the choice problem was to select one brand out of four protection lotion brands, each of which was described with the same set of four attributes. The information matrix was kept on the screen until the subject arrived at a decision and keyed in his/her choice. In addition, the participant's <sup>fi</sup>xations were recorded by the eye tracker through the whole section, with the duration time of the section and his/her <sup>fi</sup>nal choice also being recorded by the program.

## 4. Result and discussion

In the experiment, each subject performed six typical strategies, and a total of 282 EISSs (6×47) were collected. For convenience in later discussion, the set of EISSs based on a typical strategy was also termed a speci<sup>fi</sup>c strategy EISS group, for example, if an EISS was based on the WADD, then it was viewed as an instance of the WADD EISS group. Thus, there were six groups, i.e., WADD, SAT, EQW, LEX, EBA, and MCD EISS Groups.

Before applying NWA, preparation work had to be undertaken. First, it was necessary to recode the <sup>fi</sup>xation sequences. The raw data on a <sup>fi</sup>xation only provides the coordinates on the screen. In order to interpret what information a <sup>fi</sup>xation is intended for, the coordinates need to be further mapped to the stimulus (i.e. decision information matrix). We used the following method to map <sup>fi</sup>xations. First, the decision information matrix was divided into regions, i.e. areas of interest (AOIs), each covering a piece of decision information. Each region was assigned a character or a number. Second, <sup>fi</sup>xations were re-coded in the character or number code for the AOI at which each <sup>fi</sup>xation was located, and successive <sup>fi</sup>xations falling in the same AOI were represented by only one code for that AOI [9,55]; for example, a sequence of AABCCD was collapsed into ABCD. In this way, we recoded sequences of raw <sup>fi</sup>xations into sequences of AOI codes, which explicitly indicated the sequence of decision information being processed during decision-making. These re-coded sequences were viewed as EISSs. Similarly, TISS for the typical decision strategies were also re-coded in the same way. It is worth noting that each typical strategy might be embodied by two or more synonymous TISSs. For example, given a choice problem as shown in Table 1, TISSs for the WADD typical strategy can be modeled as “read (3), read (5), …, read (4), read (8)”, as well as, “read (5), read (3), …, read (8), read (4)”. The above two synonymous TISSs differ mainly in that in the former case, reading weight value goes <sup>fi</sup>rst, while in the latter case, reading attribute value goes <sup>fi</sup>rst. Appendix A illustrates the WADD TISS used in this experiment and its correspondent choice problem.

The second important task was to decide on scoring parameters for the algorithm, including gap penalty, matched alignment, and mismatched alignment. We knew that there was no well-learned method to determine con<sup>fi</sup>gurations appropriate for our on-hand analysis. Therefore, using the collected EISS and TISS data, we applied simulations to <sup>fi</sup>nd out the con<sup>fi</sup>guration which could yield an optimal hit-ratio. After the simulation, we set the gap penalty at −1, the score for matched alignment at 3, and the score for mismatched alignment at −5. This set of parameters resulted in the optimal hit-ratio being achieved after our repeated simulations (also refer to Section 4.4).

## 4.1. Averaged similarity scores of EISS groups by TISSs

After the completion of the preparation work, we applied NWA to compute similarity scores for eachbEISS,TISSNpair. A total of 2538 comparisons (47 subjects×6 EISS groups×9 TISSs) were made. We averaged the similarity scores ofbEISS, TISSNpairs by each EISS Group versus each TISS. The resultant averaged scores for eachbEISS Group versus TISSNpair are presented in matrix form in Table 2. The entries on the diagonal of the matrix represent the averaged similarity score for eachbEISS Group versus TISSNpair based on the same typical strategy. There are consistent indications that, with respect to each EISS group, the averaged similarity scores with the TISS based on the same strategy are higher than the scores with the TISS based on different strategies, as shown in each row of Table 2.

## 4.2. Averaged similarity scores of EISS groups versus EISS groups

We also applied NWA to compute similarity scores for each bEISS, EISSN pair, with the exception of the pairs by the same subject. A total of 38,916 comparisons were made. Further, we averaged the similarity scores of bEISS,EISSN pairs by each EISS Group versus each EISS Group. The resultant averaged scores for each bEISS Group, EISS GroupN pair are presented in matrix form in Table 3. The entries on the diagonal of the matrix represent the averaged similarity score for each EISS Group versus itself. There is a clear indication that, with respect to each EISS group, the averaged similarity score with itself was higher than the scores with the other EISS groups, as shown in each row of Table 3.

## 4.3. NWA-based classification method and hit-ratio

We presumed that the EISS and the TISS derived from the same typical decision strategy should be the most similar and that, if NWA was a valid algorithm, it would produce the highest similarity score for the bEISS,TISSN pairs derived from the same typical decision strategy. Therefore, based on the assumption and the similarity score from NWA, we developed a NWA-based classi<sup>fi</sup>cation method for predicting underlying cognitive strategy. We also estimated the hitratio, which indicates the success of the predictive nature of the method [16][pp.264].

The algorithm of the NWA-based classi<sup>fi</sup>cation method is simple, and may be illustrated in the following way: suppose that the strategy underlying an EISS case is unknown and that there is a set of TISSs whose corresponding strategies are well known. We then align the target case with each TISS and identify the TISSs with the most similar scores to the target case. After that, we designate the strategies underlying the TISSs to the target case. Note that if there are two or more TISSs with the same score to the target case, we regard all the strategies underlying these TISSs to have equal likelihood of being representative of the target case.

Table 2  
Averaged similarity score of EISS group by TISS. A star (\*) indicates there is a signi<sup>fi</sup>cant difference (p b .001) between this entry with its corresponding entry within the same column.

<table><tr><td>TISS EISS</td><td>WADD01</td><td>WADD02</td><td>SAT01</td><td>SAT02</td><td>EQW01</td><td>MCD01</td><td>MCD02</td><td>LEX01</td><td>EBA01</td></tr><tr><td>WADD</td><td>0.256</td><td>0.265</td><td>0.048*</td><td>0.047*</td><td>0.141*</td><td>0.158*</td><td>0.152*</td><td>0.078*</td><td>0.135*</td></tr><tr><td>SAT</td><td>0.155*</td><td>0.148*</td><td>0.229</td><td>0.218</td><td>0.126*</td><td>0.119*</td><td>0.113*</td><td>0.101*</td><td>0.156*</td></tr><tr><td>EQW</td><td>0.257</td><td>0.248</td><td>0.086*</td><td>0.091*</td><td>0.336</td><td>0.264*</td><td>0.226*</td><td>0.111*</td><td>0.132*</td></tr><tr><td>MCD</td><td>0.176*</td><td>0.172*</td><td>0.062*</td><td>0.064*</td><td>0.214*</td><td>0.279</td><td>0.265</td><td>0.070*</td><td>0.119*</td></tr><tr><td>LEX</td><td>0.180*</td><td>0.163*</td><td>0.101*</td><td>0.112*</td><td>0.143*</td><td>0.128*</td><td>0.127*</td><td>0.373</td><td>0.203*</td></tr><tr><td>EBA</td><td>0.170*</td><td>0.158*</td><td>0.077*</td><td>0.079*</td><td>0.095*</td><td>0.119*</td><td>0.109*</td><td>0.105*</td><td>0.264</td></tr></table>

Averaged similarity score of EISS group by EISS group. A star (\*) indicates there is a signi<sup>fi</sup>cant difference (pb.001) between this entry with its corresponding entry within the same column.

<table><tr><td>EISS EISS</td><td>WADD</td><td>SAT</td><td>EQW</td><td>MCD</td><td>LEX</td><td>EBA</td></tr><tr><td>WADD</td><td>0.293</td><td>0.129*</td><td>0.173*</td><td>0.178*</td><td>0.104*</td><td>0.180*</td></tr><tr><td>SAT</td><td>0.133*</td><td>0.251</td><td>0.137*</td><td>0.121*</td><td>0.132*</td><td>0.156*</td></tr><tr><td>EQW</td><td>0.169*</td><td>0.140*</td><td>0.395</td><td>0.272*</td><td>0.121*</td><td>0.133*</td></tr><tr><td>MCD</td><td>0.172*</td><td>0.114*</td><td>0.269*</td><td>0.319</td><td>0.092*</td><td>0.148*</td></tr><tr><td>LEX</td><td>0.102*</td><td>0.121*</td><td>0.109*</td><td>0.090*</td><td>0.301</td><td>0.130*</td></tr><tr><td>EBA</td><td>0.176*</td><td>0.154*</td><td>0.135*</td><td>0.152*</td><td>0.135*</td><td>0.303</td></tr></table>

On the basis of the above NWA-based classi<sup>fi</sup>cation method, we classi<sup>fi</sup>ed the cases in each EISS group to one or more predicted TISS groups and calculated the number of cases in each predicted TISS group. This calculation is done in the following way: if a target case is designated to only one predicted TISS group, then one is added to the number of observations of the predicted TISS group. On the other hand, if a target case is designated to two or more TISSs, then all the predicted TISS groups share the one. For example, if a case is assigned to 2 predicted TISS groups, then 1/2 respectively is added to the number of cases of each predicted TISS group. The size of each predicted group by each actual group is presented in Table 4. The entries on the diagonal of the matrix represent the number of cases correctly classi<sup>fi</sup>ed; the numbers off the diagonal represent incorrect classi<sup>fi</sup>cation. The entries under the column labeled Actual Group Size represent the number of cases in each EISS group.

Finally, we calculated the hit-ratio for overall <sup>fi</sup>t assessment. The hitratio is derived from the following formula: numberXcorrectlyXclassified × 100% totalXnumberXof Xobservations [16][pp.267]. On the basis of the formula, the hit-ratio of our NW-based classification method was ${ \frac { 4 7 + 2 6 . 5 + 4 4 + 4 6 + 3 9 . 5 + 4 5 } { 4 7 + 4 7 + 4 7 + 4 7 + 4 7 + 4 7 } } \times 1 0 0 \% = 0 . 8 8 .$ We then computed Press's Q statistic to assess whether our accuracy ratio was signi<sup>fi</sup>cantly better than that correctly predicted by chance. The Q statistic is calculated by means of the following formula: $\frac { \left[ N - ( n K ) \right] ^ { 2 } } { N ( K - 1 ) } ,$ where N=total sample size, n=number of observations correctly classi<sup>fi</sup>ed, and K=number of groups. The calculated value is then compared with a critical chi-square value for 1df at the desired con<sup>fi</sup>dence level [16][pp.270]. On the basis of the formula, the Q statistic for our prediction accuracy is $\begin{array} { r } { \frac { [ 2 8 2 - ( 2 4 8 \times 6 ) ] ^ { 2 } } { 2 8 2 ( 6 - 1 ) } = 1 0 3 1 . 5 6 . } \end{array}$ This result indicates that our overall prediction accuracy is signi<sup>fi</sup>cantly higher than that gained from chance $( \chi ^ { 2 } ( 1 ) = 1 0 3 1 . 5 6 , p < . 0 0 1 )$ .

## 4.4. Parameter estimation by means of Monte-Carlo simulations

With respect to the NW, there are three important parameters which considerably in<sup>fl</sup>uence the analysis result, i.e., gap penalty, score for matched alignment, and score for mismatched alignment.

Since there are many possibilities for their con<sup>fi</sup>guration, in this study, the Monte-Carlo simulation was used to test different sets of parameters against the hit-ratio. In the simulation, the value of gap penalty ranged from 0 to −5; the value for matched alignment ranged from 0 to 5; and the value for mismatched alignment ranged from 0 to −5. Finally, we selected the set of values which attained an 88% hitratio to con<sup>fi</sup>gure NWA: gap penalty −1, score for matched alignment 3, and score for mismatched alignment −5.

## 5. Conclusion

From our results, we conclude that the combination of eye-<sup>fi</sup>xation data and NWA supports the assumption that the pair of information search behaviors based on the same strategy should have the closest resemblance. This implies that the combination of eye-<sup>fi</sup>xation data and NWA is quali<sup>fi</sup>ed to characterize decision process and strategy. However, the similarity scores of our results seem, on average, somewhat low. The possible reasons for this phenomenon are threefold. Firstly, the set of EIPs used may not have been well-de<sup>fi</sup>ned, leading our TISS not truly to re<sup>fl</sup>ect the actual steps taken, i.e. EISS, by a decision-maker. For example, it is obvious that individuals might reread some information to refresh fading information in the working memory during a decision process, but such an operation is not speci<sup>fi</sup>cally de<sup>fi</sup>ned in the current set of EIPs. Secondly, our construction of the hypothetical courses of decision processes from a top-down perspective may have been somewhat simplistic. Such construction may have overlooked the possibility of individuals switching to the bottom-up mode, where they can become ensnared in some local contexts of a choice problem. Finally, the more basic level of eye-movement mechanism was not taken into account when constructing the hypothetical search behaviors. For example, it is found that, when reading proceeds, there is a 10–15% likelihood that an individual's <sup>fi</sup>xation may move backwards. These backward movements, termed regressions, may be caused partially by the problems with cognitive processing and partially from oculomotor error [43][pp.48]. Similarly, regression is also likely to occur in reading decision information and interfere with EISSs, thus leading to greater deviation from TISSs. It would be useful for future research to address these theoretical issues to advance the EIP theory and elevate the performance of NWA.

Moreover, with respect to our NWA-based classi<sup>fi</sup>cation method, our result demonstrates its accuracy in identifying underlying strategies. This has some important implications for behavioral decision research and DSS interface design. In terms of behavioral decision research, this method has considerable potential to develop a new construct which automatically characterizes the decision process as a sort of typical decision strategy by analogy. With regard to DSS design, the method utilizing real-time eye tracking may be integrated into DSS for diagnosing which strategy a decision-maker might use. Such integration will possibly enable DSS to respond to users in a more adaptive manner.

Table 4  
Classi<sup>fi</sup>cation matrix for our NWA-based classi<sup>fi</sup>cation analysis and hit-ratio

<table><tr><td>Predicted groupActual group</td><td>WADD</td><td>SAT</td><td>EQW</td><td>MCD</td><td>LEX</td><td>EBA</td><td>Actual group size</td><td>Percentage correctly classified</td></tr><tr><td>WADD</td><td>47</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>47</td><td>1.00</td></tr><tr><td>SAT</td><td>14</td><td>26.5</td><td>3</td><td>1</td><td>1</td><td>1.5</td><td>47</td><td>0.56</td></tr><tr><td>EQW</td><td>2</td><td>0</td><td>44</td><td>0</td><td>1</td><td>0</td><td>47</td><td>0.94</td></tr><tr><td>MCD</td><td>0</td><td>0</td><td>1</td><td>46</td><td>0</td><td>0</td><td>47</td><td>0.98</td></tr><tr><td>LEX</td><td>3</td><td>0.5</td><td>0</td><td>0</td><td>39.5</td><td>4</td><td>47</td><td>0.84</td></tr><tr><td>EBA</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>45</td><td>47</td><td>0.96</td></tr><tr><td>Predicted size for each typical strategy</td><td>67</td><td>27</td><td>48</td><td>48</td><td>41.5</td><td>50.5</td><td>282</td><td>Hit-ratio 0.88</td></tr></table>

Thirdly, in the study, we used the Monte-Carlo simulation to ascertain a set of parameters for NWA against the criterion of hit-ratio. This procedure has been demonstrated to be useful in optimizing the hitratio from .40 to .88. Moreover, the simulation result implies that the performance of NWA with respect to eye-<sup>fi</sup>xation data <sup>fl</sup>uctuates dramatically when different sets of parameters are con<sup>fi</sup>gured. Therefore, caution is advised for researchers with regard to the con<sup>fi</sup>guration of NWA parameters.

## 5.1. Limitation and future research

When interpreting our results, the reader should be aware of certain limitations. First, the EISS in the study was generated by trained individuals. The purpose of doing so was to make the EISS more adherent to typical strategies and to control possible interferences to the performance of NWA. However, in reality, EISS may have greater variation. In future, researchers might seek to relax this limitation to re-examine the robustness of the NWA-based classi<sup>fi</sup>- cation method. Secondly, the decision information layout was based on the tradition of behavioral decision-making. This simpli<sup>fi</sup>ed the actual purchase information environment in order to exclude irrelevant confounding factors. In spite of the bene<sup>fi</sup>ts of this more abstract approach, it would be of value for future research to be undertaken in a more realistic environment. Finally, with regard to NWA, future researchers might wish to try a more complicated scoring mechanism, such as af<sup>fi</sup>ne gap penalty, to improve the performance of NWA. Alternatively, researchers could take into account some vision mechanisms while developing a scoring mechanism. For example, as it is very likely that individuals read information with peripheral vision, scoring for unmatched alignment might take into account the closeness of the two corresponding AOIs.

## Acknowledgement

This research is sponsored by the NSC of Taiwan, grant no. 97-2410- H-218-022-.

Appendix A

<table><tr><td></td><td>SPF</td><td>Polished</td><td>Moisture</td><td>Fresh</td></tr><tr><td>Cutoff value</td><td> $4_{AOI(21)}$ </td><td> $1_{AOI(22)}$ </td><td> $3_{AOI(23)}$ </td><td> $2_{AOI(24)}$ </td></tr><tr><td>Weight</td><td> $2_{AOI(17)}$ </td><td> $5_{AOI(18)}$ </td><td> $4_{AOI(19)}$ </td><td> $1_{AOI(20)}$ </td></tr><tr><td>Protection Lotion 1</td><td> $1_{AOI(01)}$ </td><td> $3_{AOI(02)}$ </td><td> $2_{AOI(03)}$ </td><td> $4_{AOI(04)}$ </td></tr><tr><td>Protection Lotion 2</td><td> $4_{AOI(05)}$ </td><td> $2_{AOI(06)}$ </td><td> $3_{AOI(07)}$ </td><td> $1_{AOI(08)}$ </td></tr><tr><td>Protection Lotion 3</td><td> $4_{AOI(09)}$ </td><td> $1_{AOI(10)}$ </td><td> $4_{AOI(11)}$ </td><td> $3_{AOI(12)}$ </td></tr><tr><td>Protection Lotion 4</td><td> $2_{AOI(13)}$ </td><td> $1_{AOI(14)}$ </td><td> $3_{AOI(15)}$ </td><td> $4_{AOI(16)}$ </td></tr></table>

The choice problem was presented for the experimental trial using the WADD strategy. The dashed rectangles represent the areas of interest, AOIs, and the numbers in parentheses are labels used to identify each AOI. With respect to this choice problem, two TISSs based on the WADD strategy were modeled:

(1) 17,1,18,2,19,3,20,4,17,5,18,6,19,7,20,8,17,9,18,10,19,11,20,12,17,13,18,14,19,15,20,16. (2) 1,17,2,18,3,19,4,20,5,17,6,18,7,19,8,20,9,17,10,18,11,19,12,20,13,17,14,18,15,19,16,20.

In the above sequences, number denotes AOI code.

## Reference

[1] A. Abbott, J. Forrest, Optimal matching methods for historical sequences, Journal of Interdisciplinary History 16 (3) (1986) 471–494.

[2] A. Abbott, A. Tsay, Sequence analysis and optimal matching methods in sociology, Sociological Methods & Research 19 (1) (2000) 3–33

[3] I. Benbasat, P. Todd, The effects of decision support and task contingencies on model formulation: a cognitive perspective, Decision Support Systems 4 (4) (1996) 241–252.

[53] I. Vessey, The effect of information presentation on decision making: a cost– bene<sup>fi</sup>t analysis, Information & Management 27 (1994) 103–117.

[4] J.R. Bettman, E.J. Johnson, J.W. Payne, A componential analysis of cognitive effort in choice, Organizational Behavior and Human Decision Processes 45 (1990) 111–139.

[5] J.R. Bettman, P. Kakkar, Effects of information presentation format on consumer information acquisition strategies, Journal of Consumer Research 3 (1977) 233–240

[6] J.R. Bettman, M.F. Luce, J.W. Payne, Constructive consumer choice processes, Journal of Consumer Research 25 (3) (1998) 187–217.

[7] J.R. Bettman, M.A. Zins, Information format and choice task effects in decision making, Journal of Consumer Research 6 (1979) 141–153.

[8] U. Bockenholt, L.S. Hynan, Caveats on a processing-tracing measure and a remedy, Journal of Behavioral Decision Making 7 (1994) 103–117.

[9] S.A. Brandt, L.W. Stark, Spontaneous eye movements during visual imagery re<sup>fl</sup>ect the content of the visual scene, Journal of Cognitive Neuroscience 9 (1) (1997) 27–38.

[10] G.J. Cook, An empirical investigation of information search strategies with implications for decision support system design, Decision Sciences 24 (3) (1993) 683–697.

[11] G.J. Cook, M.R. Swain, A computerized approach to decision process tracting for decision support system design, Decision Sciences 24 (5) (1993) 931–952.

[12] R.-F. Day, T.-W. Shy, J.-C. Wang, The effect of <sup>fl</sup>ash banners onmulti-attribute decision making: is the <sup>fl</sup>ash banner a distractor or a source of arousal? Psychology & Marketing 23 (5) (2006) 369–382.

[13] A.R. Dennis, T.A. Carte, Using geographical information systems for decision making: extending cognitive <sup>fi</sup>t theory to map-based presentation, ISR 9 (2) (1998) 194–203.

[14] B. Fazlollahi, M.A. Parikh, S. Verma, Adaptive decision support systems, Decision Support Systems 20 (4) (1997) 297–315.

[15] S.S. Hacisalihzade, et al., Visual perception and sequences of eye movement <sup>fi</sup>xations: astochastic modeling approach, IEEE Transactions on Systems, Man and Cybernetics 22 (3) (1992) 474–481.

[16] J.F. Hair, et al., Multivariate Data Analysis, 5 edPrentice-Hall, London, 1998.

[17] B. Halpin, T.W. Cban, Class careers as sequences: an optimal matching analysis of work-life histories, European Sociological Review 14 (2) (1998) 111–130.

[18] M. Hegarty, R.E. Mayer, C.E. Green, Comprehension of arithmetic word problems: evidence from students' eye <sup>fi</sup>xations, Journal of Educational Psychology 84 (1) (1992) 76–84.

[19] M. Hegarty, R.E. Mayer, C.A. Monk, Comprehension of arithmetic word problems: a comparison of successful and unsuccessful problem solvers, Journal of Educational Psychology 87 (1) (1995) 18–32.

[20] J.H. Holland, et al., Induction: Processes of Inference, Learning, and Memory, MIT Press, Cambridge, MA, 1986.

[21] M.E. Holmes, Optimal matching analysis of negotiation phase sequences in simulated and authentic hostage negotiations, Communication Reports 10 (1) (1997) 1–8.

[22] S.L. Jarvenpaa, The effect of task demands and raphical formation on information processing strategies, Management Science 35 (3) (1989).

[23] E.J. Johnson, J.W. Payne, Effort and accuracy in choice, Management Science 31 (4) (1985) 395–414.

[24] S. Josephson, M.E. Holmes, Visual attention to repeated internet images: testing the scanpath theory on the world wide web, Proceedings of the 2002 Symposium on Eye Tracking Research & Applications ACM, New Orleans, Louisiana, 2002.

[25] M.A. Just, P.A. Carpenter, Eye <sup>fi</sup>xations and cognitive processes, Cognitive Psychology 8 (1976) 441-480.

[26] N. Kumar, I. Benbasat, The effect of relationship encoding, task type, and complexity on information representation: an empirical evaluation of 2D and 3D line graphs, MISQ 28 (2) (2004) 255–281.

[27] F.-Y. Kuo, C.-W. Hsu, R.-F. Day, An exploratory study of cognitive effort involved in decision under framing—an application of the eye-tracking technology, Decision Support Systems 48 (1) (2009) 81–91.

[28] B. Laeng, D.-S. Teodorescu, Eye scanpaths during visual imagery reenact those of perception of the same visual scene, Cognitive Science 26 (2002) 207–231.

[29] V.I. Levenshtein, Binary codes capable of correcting deletions, insertions and reversals, Doklady Physics 10 (1966) 707–710.

[32] S.B. Needleman, C.D. Wunsch, A general method applicable to search for similarities in the amino acid sequence of two proteins, Journal of Molecular Biology 48 (1970) 443–453.

[33] A. Newell, H.A. Simon, Human Problem Solving, Prentice-Hall, NJ, 1972.

[34] B. Pan, et al., The determinants of web page viewing behavior: an eye-tracking study, Proceedings of the 2004 Symposium on Eye Tracking Research & Applications, ACM, New York, 2004

[35] J.W. Payne, Task complexity and contigent processing in decision making: an information search and protocol analysis, Organizational Behavior and Human Decision Processes 16 (2) (1976) 366–387.

[36] J.W. Payne, J.R. Bettman, E.J. Johnson, Adaptive strategy selection in decision making, Journal of Experimental Psychology: Learning, Memory, and Cognition 14 (3) (1988) 534–552.

[37] J.W. Payne, J.R. Bettman, E.J. Johnson, The Adaptive Decision Maker, Cambridge University Press New York 1993

[38] R.W. Picard, Affective Computing, MIT Press, Cambridge, Mass, 1997.

[39] M. Pomplug, et al., Comparative visual search: a difference that makes a difference, Cognitive Science 25 (2001) 3–36.

[40] A. Prinzie Test, Incorporating sequential information into traditional classi<sup>fi</sup>cation models by using an element/position-sensitive SAM, Decision Support Systems 42 (2) (2006) 508–526.

[41] A. Ramaprasad, Cognitive process as a basis for MIS and DSS design, Management Science 33 (2) (1987) 139–148

[42] K. Rayner, Eye movements in reading and information processing: 20 years of research, Psychological Bulletin 124 (3) (1998) 372–422.

[43] E.D. Reichle, K. Rayner, P. A., The E–Z reader model of eye-movement control in reading: comparisons to other models, Behavioral and Brain Sciences 26 (4) (2003) 445–526.

[44] J.E. Russo, L.D. Rosen, An eye <sup>fi</sup>xation analysis of multialternative choice, Memory & Cognition 3 (3) (1975) 267–276

[45] D.D. Salvucci, J.R. Anderson, Automated Eye-Movement Protocol Analysis, Human–Computer Interaction 16 (2001) 39–86.

[46] M.S. Silver, Decision support systems: directed and nondirected change, Information Systems Research 1 (1) (1990) 47–70.

[47] D.T. Singh, Incorporating cognitive aids into decision support systems: the case of the strategy execution process, Decision Support Systems 24 (2) (1998) 145–163.

[48] C.B. Stabell, A decision-oriented approach to building DSS, in: J.L. Bennett (Ed.), Building Decision Support Systems, Addison-Wesley, MA, 1983.

[49] D.N. Stone, K. Kadous, The joint effects of task-related negative effect and task difficulty in multiattribute choice, Organizational Behavior and Human Decision Processes 70 (2) (1997) 159–174.

[50] M. Tabatabaei, An experimental analysis of decision channeling by restrictive information display, Journal of Behavioral Decision Making 15 (5) (2002) 419–432.

[51] P. Todd, I. Benbasat, The in<sup>fl</sup>uence of decision aids on choice strategies: an experimental analysis of the role of cognitive effort, Organizational Behavior and Human Decision Processes 60 (1994) 36–74.

[52] R. Vertegaal, Attentive user interfaces, Communications of the ACM 46 (3) (2003) 30–33.

[54] I. Vessey, D. Galletta, Cognitive <sup>fi</sup>t: an expirical study of information acquisition, JSR 2 (1) (1991) 63–84

[55] J.M. West, et al., eyePatterns: software for identifying patterns and similarities across <sup>fi</sup>xation sequences, Proceedings of the 2006 Symposium on Eye tracking Research & Applications, ACM. New York, 2006.

[56] J.G. Wolff, Medical diagnosis as pattern recognition in a framework of information compression by multiple alignment, uni<sup>fi</sup>cation and search, Decision Support Systems 42 (2) (2006) 608–625.

[57] S. Zhai, C. Morimoto, S. Ihde, Manual and gaze input cascaded (MAGIC) pointing, Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, ACM, New York, 1999.
