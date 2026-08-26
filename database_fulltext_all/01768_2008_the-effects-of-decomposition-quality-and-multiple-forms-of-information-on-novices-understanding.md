---
otero_id: 1768
otero_key: "WZPNHRD8"
title: "The Effects of Decomposition Quality and Multiple Forms of Information on Novices’ Understanding of a Domain from a Conceptual Model"
authors: "Andrew Burton-Jones; Peter Meso"
year: "2008"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00179"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Volume 9 Issue 12

Article 1

12-6-2008

# The Effects of Decomposition Quality and Multiple Forms of Information on Novices’ Understanding of a Domain from a Conceptual Model

Andrew Burton-Jones , andrew.burton-jones@sauder.ubc.ca

Peter Meso , pnmeso@gmail.com

Follow this and additional works at: https://aisel.aisnet.org/jais

# Journal of the Association for Information Systems JAIS

Research Article

The Effects of Decomposition Quality and Multiple Forms of Information on Novices’ Understanding of a Domain from a Conceptual Model\*

Andrew Burton-Jones University of British Columbia andrew.burton-jones@sauder.ubc.ca

Peter N. Meso Georgia State University pmeso@cis.gsu.edu

## Abstract

Individuals can often use conceptual models to learn about the business domain to be supported by an information system. We investigate the extent to which such models can help novices (i.e., individuals who lack knowledge in the business domain and in conceptual modeling) to obtain an understanding of the domain codified in the model. We focus on two factors that we predici will influence novices' understanding: (1) decomposition quality: whether the conceptual model manifests a good decomposition of the domain, and (2) multiple forms of information: whether the conceptual model is accompanied by information in another form (e.g., a textual narrative). We hypothesize that both factors will have positive effects on understanding and that these effects depend on whether the individual seeks a surface or deep understanding. Our results are largely in line with our predictions. Moreover, our results suggest that while novices are generally aware that having multiple forms of information affects their understanding, they are unaware that decomposition quality affects their understanding. Based on these results, we recommena that practitioners include complementary forms of information (such as a textual narrative) along with conceptual models and be careful to ensure that their conceptual models manifest a good decomposition of the domain.

Keywords: conceptual model, decomposition quality, form of information, novice understanding.

# The Effects of Decomposition Quality and Multiple Forms of Information on Novices’ Understanding of a Domain from a Conceptual Model

## 1. Introduction

Because business domains are so complex, many practitioners use models to understand them. For example, strategists create mind maps (Huff 1990), supply chain managers create decision models (Pidd 2003), and systems analysts create conceptual models (Davies et al. 2006). Conceptual models, also referred to as conceptual modeling scripts, describe aspects of a business domain that are to be supported by an information system. They can be used by various stakeholders of an information system. For example, analysts can use them to help themselves reason about the domain, users and analysts can use them to communicate their understanding of the domain to each other, designers can use them to check their understanding of the domain during systems design, and maintenance programmers can use them to understand the domain that the system was designed to support (Kung and Solvberg 1986, Wand and Weber 2002).

Conceptual models are created using a conceptual modeling grammar. A grammar consists of constructs (e.g., entities and attributes) and rules for using the constructs (e.g., entities can have attributes but attributes cannot have attributes). Many conceptual modeling grammars exist, ranging widely in formality, from the relatively informal “rich pictures” technique (Checkland 1999) to the more software-oriented “unified modeling language” (Kobryn 1999). Motivated by the importance of conceptual modeling, and by the number of modeling grammars that exist, many researchers have set out to determine: (1) whether some grammars are better than others (referred to as inter-grammar research) (Vessey and Conger 1994, Agarwal et al. 1996), and (2) how to create better conceptual models using a given grammar (referred to as intra-grammar research) (Gemino and Wand 2005, Shanks et al. 2008). Drawing primarily on the second stream of research, this study aims to identify factors that impact the extent to which conceptual models help individuals to understand a domain.

Although many individuals can use conceptual models, one common context in which such models are used is to support business/systems analysis (Dawson and Swatman 1999, Sarker and Lee 2006). The aim in such projects is for users and analysts to reach a shared understanding of how a business works (“as is”) and how it should work (“to be”). Ideally, analysts will reflect this shared understanding correctly in the conceptual model and, likewise, the model will help analysts and users understand the current and future business. In this way, analysts and users can use the conceptua model to: (1) validate their understanding (e.g., an analyst might show a model to an expert user and ask her to verify whether it reflects the domain correctly), or (2) facilitate understanding (e.g., a user or analyst might look at the model to gain a better understanding of the current/future business) (Davies et al. 2006). Both uses are clearly important, but to scope our study, we focus on the second type of use alone.

Because the focus of our paper is individuals’ understanding of a business, it is important to note that users’ and analysts’ understanding will be affected by their prior knowledge (Patel et al. 2004). Table 1 shows two ways in which users’ and analysts’ prior knowledge might vary, distinguishing among analysts and users who are knowledgeable in (a) conceptual modeling, (b) the business, (c) both, or (d) neither. In practice, all four sets of individuals can be involved in a systems analysis project, such as when a consulting firm assigns both new and experienced consultants to a client’s systems analysis project (cells 1 and 3) and when the client assigns a combination of new users, experienced users, and internal analysts to the same project (cells 2, 3, and 4). To scope our research, we examine only the context in cell 3, i.e., we study the extent to which conceptual models help novices understand a business. We recognize that perhaps the most interesting cases are those in which individuals have varying levels of knowledge, but such cases are also the most complex, and we believe that it is useful to understand a context involving novices prior to introducing the effects of expertise. As we will show, the process by which novices gain an understanding is already quite complex.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Individuals’ Domain Knowledge</td></tr><tr><td>None to Low</td><td>Moderate to High</td></tr><tr><td rowspan="2">Individuals’ Modeling Knowledge</td><td>Moderate to High</td><td>1. Experienced external analysts</td><td>2. Experienced internal analysts</td></tr><tr><td>None to Low</td><td>3. Novice users, novice analysts (the context studied in this paper)</td><td>4. Experienced users</td></tr><tr><td colspan="4">Table 1: Types of Analysts and Users who Employ Conceptual Models</td></tr></table>

We focus on two factors that we predict will influence the understanding of a business that novices obtain from a conceptual model: the quality of information they receive (i.e., whether the conceptual model reflects the business domain accurately and clearly), and the form of information they receive (i.e., whether the conceptual model is accompanied by additional information about the domain in an alternative form). To investigate these two factors, we draw on two theories: the Good Decomposition Model (Wand and Weber 1990) and the Multimedia Theory of Learning (Mayer 2001). Based on these theories, we hypothesize that novices will understand a domain better when they are provided with a conceptual model that (1) manifests a good decomposition of the business domain, and (2) is accompanied by information about the domain in a different form (e.g., a textual narrative). Moreover, we hypothesize that these two factors will have different effects on novices’ understanding, depending on the facet of understanding studied. Specifically, we study three facets of understanding: surface understanding (understanding the elements of a business domain), deep understanding (understanding the actual and possible relationships among elements in a business domain), and ease of understanding (the effort required to understand the domain).

In the remaining sections of this paper, we first present our theoretical model and hypotheses. We then outline an experiment we ran to test these hypotheses and a follow-up protocol analysis study that we ran to determine the reasons for some of our results. Finally, we discuss the limitations of our study and its implications for research and practice.

## 2. Theoretical Background

Figure 1 shows our theoretical model. The model proposes that domain understanding is a function of two factors: decomposition quality and multiple forms of information.

Decomposition quality refers to the extent to which an analyst has broken down a business domain into parts, or subsystems, in a clear manner. Practitioners and academics have long stated the importance of decomposing systems in a clear manner (Larman 2001, Simon 1996). In practice, an analyst can break down a domain in many ways, reflected in his/her choices about what parts or subsystems to show in the conceptual model, what attributes to show, what level of detail to use when describing events, and so forth. Depending on the analyst’s choices, the decomposition can vary widely in quality. To assess its quality, we need a theory of decomposition. The only such theory, to our knowledge, is the Good Decomposition Model (Wand and Weber 1990). This theory offers five criteria for assessing a decomposition:

o Minimal coupling: Subsystems should have minimal interaction:

o For example, two classes in a UML sequence diagram should pass as few messages between them as possible.

o Maximal cohesion: Subsystems should perform as few functions as possible:

o For example, a use case in a UML use case diagram should address one function rather than many different functions.

o Minimality: Subsystems should contain no redundant elements:

o For example, a class in a UML class diagram should only contain attributes that are used by at least one method in the class diagram.

o Losslessness: Subsystems should show all (i.e., not lose) relevant emergent properties: o For example, in a “whole-part” relationship in a UML class diagram, the whole should show any important properties in the domain that emerge from its parts.

o Determinism: Subsystems should interact in a well-defined manner:

o For example, in a UML statechart, any event should lead to just one post-event state. If an event leads to multiple post-event states, a condition should be shown to indicate when the system would move to one event or the other.

![](/api/attachments/WZPNHRD8/fulltext/images/83bd8bd67029de9959bd6d44b598dab79e74bf1affc3260ada1d0f59e6eeb4c4.jpg)  
Figure 1: The effects of quality and form of information on domain understanding  
Key: F: Theoretical factor, O: Operationalization of the factor in our study

The second antecedent in our theoretical model—multiple forms of information—refers to whether the novice reader receives a conceptual model on its own or accompanied by information about the domain in an alternative form. To define this construct, we follow Gemino (2004, p. 163) in making a distinction between “how content is presented, [and] what content is provided.” While decomposition quality assesses what content is provided, we use the term “form” to reflect how content is presented. Although most conceptual models utilize a diagrammatic form, they could use alternative forms. Likewise, if a conceptual model is created in a diagrammatic form, it could be accompanied by information about the domain in another form. Ultimately, we suggest that domain information can be delivered to an individual in any multimedia form, i.e., using any combination of words or pictures. Mayer’s (2001, 2005) theory of multimedia learning characterizes the variety of forms that such information can take:

I define multimedia as presenting both words (such as spoken text or printed text) and pictures (such as illustrations, photos, animations, or video). By words, I mean that the material is presented in verbal form, such as using printed text or spoken text. By pictures, I mean that the material is presented in pictorial form, such as using static graphics, including illustrations, graphs, diagrams, maps, or photos, or using dynamic graphics, including animation and video (Mayer 2005, p. 2).

Therefore, following Mayer (2005), we suggest that domain information can be presented to an individual in any combination of words and/or pictures. In this research, we examine the effect of providing a novice with a conceptual model in the traditional form—a diagram—accompanied by information in an alternative form—narrative text. Our interest is not in examining which form is best, but rather whether (and if so, when and why) a combination of forms is beneficial.

In choosing these two antecedents—decomposition quality and multiple forms of information—we are extending a new line of conceptual modeling research. To our knowledge, only one study has examined the effect of decomposition quality on understanding (Burton-Jones and Meso 2006) and only two have examined the effect of providing multiple forms of information on understanding (Chen et al. 2002, Gemino 2004). We extend these studies by explaining how decomposition quality and multiple forms of information work together to affect understanding.

Figure 1 highlights several aspects of understanding. First, it distinguishes between the process and product of understanding. The process refers to the activities a novice reader engages in to understand the domain. Following past studies (Gemino and Wand 2005, Burton-Jones and Meso 2006), we study one aspect of this process, the individual’s ease of understanding the domain. Second, Figure 1 distinguishes between two products of understanding: surface understanding and deep understanding. These are best seen as occupying two ends of a continuum. Both types of understanding require an individual to understand the elements and relationships among elements in a domain. However, whereas surface understanding places more weight on an individual’s understanding of the elements, deep understanding places more weight on his/her understanding of the actual and possible relationships among elements. For example, Mayer (1989, 2001, 2005) has tested surface understanding via comprehension questions and deep understanding via problemsolving questions. A typical comprehension question asks an individual to describe one or more elements in a domain (e.g., the nature of one or more events). A typical problem-solving question describes a problem in the domain (e.g., an element that is not working) and asks the individual to explain how this occurred based on his/her understanding of the elements in the domain and their interrelationships. Following Gemino and Wand (2005) and Burton-Jones and Meso (2006), we adopt Mayer’s distinction between surface and deep understanding and his measurement approach in this study.

<table><tr><td colspan="3">Table 2: Theoretical effects</td></tr><tr><td>Effect</td><td>Explanation</td><td>Implication for understanding</td></tr><tr><td>1. Direct information content effect</td><td>When a reader attempts to learn a domain from a representation (e.g., a conceptual model or a textual narrative), problems in the representation (e.g., unclear, incomplete, or irrelevant information) can directly affect the reader&#x27;s understanding.</td><td>Decomposition quality will have a direct positive effect on actual understanding (surface and deep), but it will not necessarily affect ease of understanding.</td></tr><tr><td>2. Multimedia effect</td><td>When a reader has two alternative representations of a domain (e.g., a conceptual model and a textual narrative), the reader can use one to aid his understanding of the other and can integrate both sources to reach a better understanding of the domain.</td><td>Providing multiple forms of information will have a positive effect on understanding.</td></tr><tr><td>3. Cognitive economy effect</td><td>When a reader has two alternative representations of a domain, s/he will tend to utilize only one of them (the more parsimonious one) if s/he only needs to obtain a surface understanding, but will tend to utilize both if s/he needs to obtain a deep understanding.</td><td>The positive effect of multiple forms of information will be greater on tests of deep understanding than on tests of surface understanding.</td></tr><tr><td>4. Incidental processing effect</td><td>When a reader attempts to gain a deep understanding of a domain (whether from a conceptual model, a textual narrative, or both), the presence of unclear information will increase the incidental processing s/he must perform, which will reduce his/her understanding.</td><td>Both decomposition quality and multiple form of information will lead to improvements in deep understanding and ease of understanding.</td></tr></table>

Figure 1 does not specify the relationships between each antecedent and each aspect of understanding. To do so, we consider four theoretical effects, outlined in Table 2.

The direct information content effect occurs when a reader relies on inaccurate information, leading him/her to misunderstand the domain. For example, assume that a conceptual model for an employee hiring system includes an attribute that is not a relevant part of the domain (such as applicant’s age, which in many jurisdictions is an illegal attribute to consider during the hiring process), thereby violating minimality. If a novice reader receives such a model, s/he may mistakenly assume that this attribute is, in fact, relevant. As Table 2 shows, if this occurred, we should be able to detect it in tests of surface understanding (e.g., by asking the reader whether applicant age is a relevant attribute in the domain) and deep understanding (e.g., by asking the reader to describe solutions to problems in the domain and seeing if s/he considers applicant age when coming up with solutions). However, we predict that it will generally not affect a reader’s ease of understanding the domain. This is because ease of understanding is driven by the mental resources a reader expends. As long as the change in the model (e.g., the addition of an attribute for applicant age) does not dramatically affect the reader’s ability to process information (e.g., overloading his/her working memory), then it should not affect his/her ease of understanding. In effect, we are assuming the reader has a “zone of tolerance” (Kettinger and Lee 2005) within which changes in a model will not alter significantly the mental resources s/he expends to understand the domain. Clearly, there will be times where the alteration of content affects ease of understanding; this relates to the incidental processing effect, discussed later.

The multimedia effect stems from the Multimedia Theory of Learning. According to this theory, people can sometimes learn more deeply from words and pictures than from words alone. As Mayer (2005, p. 4) explains, this is because “humans have two information-processing systems – one for verbal material and one for visual material…. [Using both words and pictures] takes advantage of the full capacity of humans for processing information.” Mayer goes on to explain:

Why might two channels be better than one? … The quantitative rationale is that more material can be presented on two channels than on one channel – just like more traffic can travel over two lanes than one lane. …. I reject [this view] because … I am concerned about the assumption that the verbal and visual channels are equivalent…. In contrast, the qualitative rationale is that words and pictures, while qualitatively different, can complement one another and that human understanding is enhanced when learners are able to mentally integrate visual and verbal representations (Mayer 2005, pp. 4-5).

As Table 2 shows, the multimedia effect predicts that a reader’s understanding of a domain will increase if s/he receives both a conceptual model (diagram) of the domain and a narrative (text) describing the domain than if s/he only receives a conceptual model of the domain. It should be noted that Mayer (2001) describes many additional principles for how to combine words and pictures most effectively (e.g., spoken narrative with pictures is better than textual narrative with pictures). Some of these have been tested by Gemino (2004). Moreover, we acknowledge that words and pictures can themselves vary in richness (e.g., words as spoken or as text, and pictures as diagrams or photos). Rather than examine different types of words and pictures, or different ways of combining them, we simply focus on the overall multimedia effect.

The cognitive economy effect refers to individuals’ tendency to trade off effort and performance (Payne et al. 1993). The cognitive economy effect constrains the multimedia effect because it suggests that if a reader is given multiple forms of information, s/he will only read both forms if s/he thinks this effort will be worthwhile. Therefore, if a reader receives a conceptual model and a textual narrative of a domain, and if s/he believes that both forms of information contain much the same information, s/he is likely to focus on just one of these forms because this would maximize his/her understanding/effort ratio. Moreover, if s/he believes that it takes less effort to read one of these forms than the other, s/he will focus on the form that takes the least effort. This is a crucial point, because notwithstanding Mayer’s belief (quoted above) that diagrams and text are not equivalent, it is often thought that diagrams and text can provide equivalent representations of a domain, and that compared to text, diagrams can provide such information in a way that people find more efficient to obtain (Siau 2004, Larkin and Simon 1987).

As Table 2 shows, we draw on the cognitive economy effect to propose that having multiple forms of information will improve deep understanding more than surface understanding. We do so because we believe that individuals will only read both forms of information if they perceive it to be a worthwhile investment. In this light, assume that a reader is given a diagram and a narrative describing the same domain. If s/he is asked a comprehension question about the domain (a test of surface understanding), we believe s/he will focus on the diagram because s/he will perceive that to be the most efficient way to answer the question (i.e., s/he will only read the narrative if s/he cannot find the answer in the diagram). In contrast, if the reader is asked a problem-solving question (a test of deep understanding), we believe s/he is more likely to examine the diagram and the narrative. This is because considering multiple representations of a problem space is well-known to be helpful when solving problems (Newell and Simon 1972, Ashcraft 2002), thus we predict that the reader will perceive the effort to be worthwhile.

The final effect in Table 2 is the incidental processing effect. Incidental processing is processing that a reader undertakes to deal with confusing or extraneous material in information s/he receives (Mayer and Moreno 2003, p. 46). As Table 2 shows, we expect decomposition quality will directly affect incidental processing. For example, if a novice reader receives a model that contains an irrelevant attribute (such as applicant’s age), s/he may spend time trying to decide whether or not it is relevant. If the individual has no additional information about the domain, s/he may be unable to decide whether it is relevant, and this may cause him/her difficulty when answering questions about the domain. Whereas the direct information content effect occurs when an individual is untroubled by incorrect information (s/he simply assumes it is correct), incidental processing occurs when s/he is troubled by incorrect information. Thus, incidental processing should have a negative effect on ease of understanding. As Table 2 explains, we expect that incidental processing will be less when the reader can access another form of information. This is because s/he should be able to use the second form of information to help him/her resolve confusions that s/he finds in the first form. For example, if an individual sees an attribute for applicant age in the conceptual model and thinks it is irrelevant, s/he might check the narrative and if it does not exist there, s/he might conclude that it is indeed irrelevant.

Based on the four effects outlined in Table 2, we draw three hypotheses regarding the effects of decomposition quality and multiple forms of information on novices’ understanding. Table 3 illustrates and explains our reasoning for each hypothesis. Following Table 3, we briefly summarize our reasoning for each dependent measure and state our formal hypotheses.

Our first hypothesis concerns surface understanding. As Table 3 shows, we predict that individuals will focus mainly on the diagrams to answer comprehension questions because of the cognitive economy effect. Thus, if the diagrams manifest a poor decomposition, the direct information content effect will lead readers to answer the comprehension questions poorly:

Hypothesis 1: Decomposition quality will have a significant positive impact on comprehension performance. Multiple forms of information will not have a significant impact on comprehension performance. Decomposition quality and multiple forms of information will not interact significantly in affecting comprehension performance.

<table><tr><td colspan="3">Table 3: Hypothesized relationships</td></tr><tr><td>Outcome</td><td>Hypothesized relationship</td><td>Relevant effects and explanation</td></tr><tr><td>1. Surface understanding (comprehension)</td><td>HighComprehension performanceLowDecomposition quality</td><td>Direct information content effect, Cognitive economy effect.Diagrams that manifest a poor decomposition will lead readers to misunderstand the domain. The effect on comprehension performance will be strong even when the reader has access to the narrative, because the reader will focus on the diagram to answer comprehension questions.</td></tr><tr><td>2. Deep understanding (problem-solving)</td><td>HighProblem-solving performanceLowDecomposition quality</td><td>Direct information content effect, Multimedia effect, Incidental processing effect.Diagrams that manifest a poor decomposition will lead readers to misunderstand the domain and bear more incidental processing, both of which will reduce problem-solving performance. Misunderstandings caused by both of these effects (the direct information content effect and the incidental processing effect) will be less if a reader has access to the narrative because the narrative can help him/her understand the domain and the diagram.</td></tr><tr><td>3. Ease of understanding</td><td>HighEase of understandingLowDecomposition quality</td><td>Multimedia effect, Incidental processing effect.Diagrams that manifest a poor decomposition will increase readers&#x27; incidental processing, which will lead them to perceive a lower ease of understanding. Incidental processing will be less if a reader has access to the narrative because he/she can use it to help him/her understand the domain and the diagram.</td></tr></table>

Hypothesis 3: Decomposition quality and multiple forms of information will both have significant positive impacts on ease of understanding. In addition, decomposition quality and multiple forms of information will interact, such that the effect of decomposition quality will be greater when the reader has access to only one form of information (the diagrams alone).

Overall, our model aims to contribute to research by showing how two theories that researchers have recently studied (the Good Decomposition Model, Burton-Jones and Meso 2006, and the Multimedia Theory of Learning, Gemino 2004) can be used together to explain how and when a conceptua model can be used to improve a novice’s understanding of a domain.

## 3. Method

Because this is the first test of our theoretical model, we chose to use an experimental method because it affords a higher internal validity than other methods (Cook and Campbell 1979).

## 3.1. Experimental Design

We used a 2\*2 between-groups design with two treatments: decomposition quality and multiple forms of information. We manipulated decomposition quality in the same way as in Burton-Jones and Meso (2006). That is, we used a narrative adapted from Conger (1996) that described an IT contracting domain, and we gave each participant a set of three UML diagrams that varied in the quality of their decomposition of this domain. To manipulate multiple forms of information, we provided some participants with the set of UML diagrams alone while other participants received the set of UML diagrams accompanied by the narrative of the domain. We employed three dependent variables: participants’ performance in a comprehension test about the domain (surface understanding), their performance in a problem-solving test about the domain (deep understanding), and their perceived ease of understanding the domain. In principle, we could have used both objective (actual) and subjective (self-report) measures to rate our three dependent variables. However, consistent with recent studies (Gemino and Wand 2005, Burton-Jones and Meso 2006), we used only one measure of each type: actual measures for surface and deep understanding and a self-report measure for ease of understanding. We return to this measurement issue in our limitations section.

## 3.2. Participants

Undergraduate students in a Canadian business school participated voluntarily. Three sets of students participated: 27 second-year students in a pencil-and-paper pre-test, 69 first-year students in an online pilot test, and 168 second-, third-, and fourth-year students in the main experiment. In each case, students were randomly assigned to treatments and all were novices, i.e., none had learned UML prior to the study, nor had they any knowledge of the business domain examined in the study (per Table 1). Although the sample was a convenience sample, most business school students will serve as business employees, and hence as end-users, in the future. Moreover, some of them will likely work as business or systems analysts in the future too. Thus, we believe they are a reasonable sample of novices for testing our hypotheses. Students were offered \$20 for participation and a one-in-three chance of receiving an additional \$50 based on their performance in the tasks. The compensation included a relatively large performance-based component to motivate students to perform well in the tasks. For the main experiment, participants took part in one of 22 sessions in a university computer laboratory during fall 2007, with between three and 14 students in each session.

## 3.3. Materials

The Appendix includes all of the experimental materials. We briefly describe each element of the materials below (in the same sequence in which they are presented in the Appendix):

o Pre-experiment questionnaire:

The pre-experiment questionnaire asked participants whether they had previously learned UML and to rate their experience with UML and their knowledge of the IT contracting domain (which was the domain shown in the UML diagrams).

## o UML tutorial:

The tutorial covered all aspects of UML that participants would need to know to perform the task, e.g., the elements of class diagrams, use case diagrams, and statecharts. In addition, the tutorial included 11 quiz questions. This gave us a measure of actual UML knowledge that we could use in our data analysis.

## o ICI Diagram Quiz:

The ICI diagram quiz tested each student’s ability to understand the diagrams (which described a company called ICI). The questions were designed so that the answers would be the same for both sets of diagrams (higher and lower quality decomposition). Although our study focuses on individuals’ understanding of the business domain (not the diagrams per se), we included this measure as a control to test whether there was a difference in the understandability of the diagrams. We expected that there would be no difference in the understandability of the diagrams. After performing the quiz, students were provided with the answers to help them check their understanding.

## o ICI Diagrams:

Our diagrams were based on those in Burton-Jones and Meso (2006), but we changed their names and content to increase construct validity. We outline these changes first before describing how we manipulated each decomposition criterion.

In relation to naming, we refer to the two sets of diagrams in our experiment as “higher quality” and “lower quality” decompositions (rather than “good” and “bad” as in Burton-Jones and Meso 2006). The Good Decomposition Model provides a way to describe a good decomposition, but it does not offer an algorithm (or set of steps) for creating a good decomposition, or for proving whether a given decomposition is good. Rather than create such algorithms, we simply chose to manipulate the “degree” of decomposition quality. Thus, we make no claim that our “higher quality” decomposition is a “good” decomposition; it is simply better than the “lower quality” decomposition.

In relation to content, we changed the content of the diagrams so that they would be more consistent with the ontological theory underlying the Good Decomposition Model (Bunge 1977). To do so, we consulted rules for creating conceptual models consistent with Bunge’s ontological theory (Wand and Woo 1993, Wand et al. 2000). These rules, known as “Object Oriented Enterprise Modeling,” or OOEM rules, use a syntax different from UML. By adapting the rules to a UML context, we were able to create UML diagrams that were more in line with the ontological theory. For example, the UML diagrams in Burton-Jones and Meso (2006, p. 47) included a class named “Interview” with methods such as “Create” and “Schedule.” In Bunge’s (1977) ontological theory, it makes no sense to say that an event such as an interview can create or schedule itself. In contrast, our class diagram distinguishes between actors who perform actions (such as a manager who schedules interviews) and static objects that record actions (such as interview results). We consulted with two experts in OOEM during the development of our diagrams. Then, we gave our final diagrams to a third expert and asked: “To what extent is the difference between the “higher quality” diagrams and “lower quality” diagrams a valid manipulation of the five “good decomposition” criteria (described in Paulson and Wand 1992 and Weber 1997)? On a five-point Likert scale (from 1 = not at all to 5 = a great extent), this expert rated the diagrams as valid to a “large extent” (i.e., 4). The expert commented that the main reason why the rating was not “a great extent” (i.e., 5) was that no method exists for proving the quality of a given decomposition, as noted earlier. As a result, we believe that the diagrams are as valid as they can be given the current state of research on the Good Decomposition Model.

As shown in the Appendix, we made the manipulation of each decomposition criterion strong to avoid type-2 error. That is, if the difference between the diagrams did not result in a significant difference between groups on the dependent measures, we wanted to maximize the likelihood that this was a “true” non-effect rather than a result of an insufficiently strong treatment. With this in mind, we made the following manipulations:

Coupling: We manipulated coupling on the Class diagram by increasing the interaction between the Manager and the Clerk in the “lower quality” decomposition and adding methods to reflect these interactions in the Manager class. These interactions do not reflect new relationships between the Manager and Clerk. Rather, they simply reflect a different way of showing the assignment of duties in the Class diagram. That is, in both Class diagrams, the Clerk’s duties are shown as methods in the Clerk class. However, in the “lower quality” decomposition, the Manager also sends a request to the Clerk to perform every one of her duties. While conceivable, these interactions are redundant because the Clerk has already been assigned these duties. Thus, the Manager is more tightly coupled to the Clerk in the “lower quality” decomposition simply because the modeler has represented the assignment of duties in two ways (in the assignment of methods, and as explicit requests to perform work). It suggests to the reader that the Manager is tightly involved in the Clerk’s work.

Cohesion: We manipulated cohesion on the Class and Use Case diagrams. On the “higher quality” Class diagram, we separated the Manager’s activities into four cohesive roles, each with its own methods and attributes. On the “lower quality” decomposition, we collapsed these roles into one “Manager” role, reducing cohesion. Likewise, on the “higher quality” Use Case diagram, we showed separate Use Cases for each value-adding function, whereas we collapsed them all into one Use Case in the “lower quality” decomposition, reducing cohesion.

Minimality: We manipulated minimality on the UML Class diagram by adding redundant attributes to each class, e.g., we added “Desired investment income” to the Manager class and “Room number” to ICI’s record of interviews. We expected the redundancy of some attributes to be less obvious and cause subjects more problems than others. Accordingly, we included a range of such attributes in the diagrams to capture the full range of problems caused by minimality. For example, we expected subjects to realize that “Room number” was an irrelevant attribute of ICI’s interview record, but we expected them not to know whether “Desired investment income” was relevant (e.g., if it concerned the Manager’s private investments or something to do with ICI’s investments).

Losslessness: We manipulated losslessness on the Class diagram in two ways. First, as in Burton-Jones and Meso (2006), we included attributes to reflect “Average job performance” and “Average job satisfaction” in ICI’s records of applicants and clients. These emergent properties were not shown on the “lower quality” decomposition. Second, the “higher quality” Class diagram showed that Applicants and Clients were both part of a market and showed emergent properties of the market (such as the number of applicants in the market). These emergent properties were lost (not shown) on the “lower quality” diagram.

Determinism: We manipulated determinism on the statechart. In the “lower quality” decomposition, the statechart had several non-deterministic events. For example, in the On-call state, it is not clear after the interview why the applicant would move to the “In Market” state or to the “Pre-selected” state. A reader might be able to use his/her background knowledge to infer a reason (e.g., the interview result was negative), but the diagram itself is not deterministic. In contrast, the “higher quality” diagram is deterministic, i.e., it is always clear what external or internal event must occur to move an applicant to or from any state.

## o Example Tasks:

We included example tasks to help students understand how to answer the comprehension and problem-solving questions. Students were shown one comprehension question and its answer, and one problem-solving question and its answers (as shown in the Appendix).

## o Practice tasks:

We included a practice comprehension task and a practice problem-solving task to further help students understand how to answer comprehension and problem-solving questions and to provide us with a measure of each student’s latent “task ability.” The practice task used the same types of diagrams that were in the main task (i.e., Class diagram, Use Case diagram, and Statechart). After answering the questions, each student was shown the suggested answers to help him/her check his/her understanding of the task.

## o Narrative and Quiz:

Because students had been shown the diagrams of ICI in the ICI diagram quiz (noted above), it was critical that we allow students in the “multiple forms of information group” to see the narrative before beginning the primary task. Otherwise, these students’ greater familiarity with the diagrams (versus the narrative) might have confounded the results. Therefore, we included a task in which both groups of students received a narrative about a domain. Students in the “multiple forms of information” group received the narrative of ICI, whereas students in the “single form of information” group received a narrative about an unrelated domain. We also included two quizzes, one for each domain. The narratives were designed to be similar in length and the quizzes were designed to be difficult to answer without reading the narrative, but fairly easy to answer if students had read the narrative. Thus, we could use students’ scores on the ICI narrative quiz as a manipulation check for whether students in the “multiple forms of information” group had read and understood the narrative.

## o Comprehension questions:

We asked ten comprehension questions about ICI’s business, two for each of the five decomposition criteria. For example, the first question asked students whether the number of potential clients in the market was an important attribute at ICI. The narrative (for the “multiple forms of information” group) and the Class diagram (for the “higher quality” decomposition group) both included this information. Because our interest is in individuals’ understanding of the domain, not the diagrams per se, we coded answers based on whether they reflected a correct understanding of the domain. For example, the correct answer for the first question was “yes” for all students in all groups. The ICI diagram quiz, mentioned earlier, tested students’ understanding of the diagrams.

## o Problem-Solving Questions:

We adapted the problem-solving questions and answers from Burton-Jones and Meso (2006). Each question began by stating a problem. It then tested the student’s ability to use his/her knowledge of the domain to: (a) suggest causes of, or solutions for, the problem; and (b) justify why these causes or solutions were reasonable. Each question had a set of acceptable answers, but students could also be awarded points if they gave other reasonable answers. Each answer had two parts: the answer and an explanation, with 0.5 points for each part. Consistent with the comprehension questions, we coded students’ answers based on whether they reflected a good understanding of the domain. Unlike the comprehension questions, we could not direct the problem-solving questions to specific violations of the decomposition criteria. This was because the decomposition violations were spread throughout the diagrams and it was possible to come up with answers from multiple parts of the diagrams. Ideally, we would have adopted a separate treatment for each decomposition criterion, but this would have required a much larger sample size than we could obtain. We return to this limitation in the Discussion.

## o Use of Information:

After both the comprehension questions and problem-solving questions, students were asked to what extent they relied on the information in the diagrams and, if they had access to the narrative, the narrative. We collected this information so that we could determine later, if need be, potential reasons for our pattern of results.

## o Questionnaire:

We included a questionnaire to ask students their ease of understanding the diagrams and their ease of understanding ICI’s business domain. Although we were interested solely in their ease of understanding the business, we included both sets of questions to allow us to test for convergent and discriminant validity. As shown in the Appendix, one item was: “to what extent did you find ICI’s business to be difficult to understand?”

## 3.4. Procedures

The experiment took two hours, including 10 minutes for administration. We created a web-based application (with ASP.net and SQL server) that enabled students to complete the exercise online. Students performed the tasks in a university computer lab, so bandwidth was sufficient. The application gave participants a set time for each task. When the time for each task expired, the system saved and closed their work on that task and moved participants on to the next task. The sequence and times allowed for all tasks are shown in the Appendix.

To ensure participants received treatments on a random basis, they entered a randomly assigned ID number on the opening webpage, which presented participants with relevant materials. We created a set number of IDs for each treatment (many more than we required).

Prior to the main experiment, we ran a pencil-and-paper pre-test and an online pilot test to ensure the procedure and manipulations worked effectively. Minor improvements were made based on the results of the pre- and pilot tests. Some problems with the ASP application were also identified during the pilot test and these were ironed out before running the full experiment.

## 4. Results

The results were examined in two steps. We first screened the data for its conformance with the assumptions of our tests. We then examined the tests of our predictions.

## 4.1. Data Screening

Table 4 shows the descriptive statistics. Although most of the results were in line with our expectations, five results deserve note. First, although 168 students participated, three students dropped out of the study during the experiment, resulting in 165 data points for most variables. Second, Table 4 shows that subjects reported a low-to-moderate level of UML experience (1.4/4.0).

<table><tr><td colspan="6">Table 4: Descriptive statistics</td></tr><tr><td>Type of variable</td><td>Variable</td><td>N</td><td>Mean</td><td>Std. Dev.</td><td>Scale</td></tr><tr><td rowspan="7">Control variables and manipulation checks</td><td>Self-report UML experience</td><td>165</td><td>1.41</td><td>0.88</td><td>0-4</td></tr><tr><td>Self-report domain knowledge</td><td>164</td><td>2.43</td><td>1.44</td><td>0-4</td></tr><tr><td>UML quiz</td><td>165</td><td>8.32</td><td>1.09</td><td>0-11</td></tr><tr><td>ICI diagram quiz</td><td>165</td><td>14.02</td><td>2.28</td><td>0-18</td></tr><tr><td>Practice comprehension</td><td>165</td><td>4.84</td><td>0.58</td><td>0-6</td></tr><tr><td>Practice problem-solving</td><td>165</td><td>2.13</td><td>0.91</td><td>0-5</td></tr><tr><td>ICI narrative quiz</td><td>165</td><td>6.89</td><td>3.11</td><td>0-11</td></tr><tr><td rowspan="4">Dependent variables</td><td>Comprehension correct</td><td>165</td><td>6.13</td><td>2.47</td><td>0-10</td></tr><tr><td>Problem-solving (total correct)</td><td>165</td><td>7.79</td><td>4.25</td><td>0-37</td></tr><tr><td>Problem-solving (% correct)</td><td>165</td><td>0.31</td><td>0.15</td><td>0-1</td></tr><tr><td>Ease of understanding domain*</td><td>161</td><td>2.06</td><td>0.99</td><td>0-4</td></tr><tr><td rowspan="4">Process variables (sources of information)</td><td>Diagram usage during comprehension</td><td>162</td><td>2.99</td><td>0.90</td><td>0-4</td></tr><tr><td>Narrative usage during comprehension**</td><td>83</td><td>1.20</td><td>1.08</td><td>0-4</td></tr><tr><td>Diagram usage during problem-solving</td><td>163</td><td>1.87</td><td>1.09</td><td>0-4</td></tr><tr><td>Narrative usage during problem-solving**</td><td>83</td><td>2.19</td><td>1.33</td><td>0-4</td></tr><tr><td colspan="6">Key: * Ease of understanding was measured in terms of difficulty (see the scale in the Appendix), but reverse coded so that higher scores reflect greater ease. **The values for “using the narrative” stem from only 83 students because only students who received the narrative could rate their use of it.</td></tr></table>

This is surprising because all 165 participants reported that they had never learned UML, thus their self-reported UML experience should have been zero, rather than low-to-moderate. Thus, we are not sure of the validity of our self-reported scale for UML experience. Third, subjects’ scores in the practice comprehension results showed little variation. We had hoped to use this variable as a control in our tests of comprehension performance. Because of the low variation, it might not serve as a good control. (As we show later, this did not affect our results because our model explained comprehension performance satisfactorily). Fourth, subjects performed poorly on the problemsolving test, recording a mean of 7.8 out of a potential maximum of 37.0. Only 31 percent of the answers they gave were correct. This poor performance was expected because the problem-solving questions were challenging. Nonetheless, this should be borne in mind when generalizing from our study, i.e., we cannot assume the results would be the same if we had used easy problem-solving questions. Finally, consistent with the arguments we used to derive our hypotheses, subjects reported that they used the diagrams more than the narrative during the comprehension questions (2.99-1.20) and that they used the diagrams about the same amount as the narrative during the problem-solving questions (1.87-2.19).

Table 5 shows the correlation matrix. We discuss three types of variables in this matrix in turn. First, we discuss our control measures and manipulation checks. As noted earlier, we collected data on several variables that might serve as controls. Table 5 shows that only a few of them would likely serve as useful control variables. The order of tasks and the UML quiz scores did not correlate significantly with any dependent measure. The self-reported measures of UML experience and domain knowledge did correlate significantly with comprehension and problem-solving performance, even if only slightly. However, these correlations were negative, which is counter-intuitive, because it implies that greater knowledge is associated with lower performance. These two self-report measures were also strongly correlated (0.56), which is not intuitive. These counter-intuitive results, coupled with the surprising result for UML expertise in the descriptive statistics, led us to question the validity of these self-report measures. The objective measures behaved more predictably. The ICI diagram quiz scores correlated significantly with problem-solving performance. The correlation between the ICI diagram quiz score and decomposition quality was also insignificant (r = -0.09), indicating that as we predicted, decomposition quality did not affect students’ understanding of the diagrams. The final control variables were the practice tasks. Table 5 shows that the practice comprehension task was not significantly correlated with comprehension performance, but the practice problem-solving task was significantly correlated with problem-solving performance.

In summary, Table 5 indicates that we did not have any useful control variables for comprehension performance or ease of understanding, but that we should control for students’ performance in the ICI diagram quiz and the practice problem-solving task when testing for problem-solving performance. Table 5 also shows that the manipulation check for the narrative worked. Recall that in Table 4, the average performance on the ICI narrative quiz was 6.9 out of 11.0. Although not shown to conserve space, the average quiz performance was 9.3 for the 83 students who received the ICI narrative and 4.5 for the 82 students who received the alternative narrative. As Table 5 shows, this resulted in a significant difference between groups (r = 0.77, p < .01), indicating that the manipulation worked, i.e., students generally read the narrative of ICI when they received it.

Second, we discuss the correlations that relate to our hypotheses, Table 5 shows that comprehension performance was driven by decomposition quality, problem-solving performance was driven by both multiple forms of information and decomposition quality, and ease of understanding was driven by multiple forms of information but not by decomposition quality. The first two results supported our hypotheses, but the last result did not. We examine these results further in the next section.

Finally, Table 5 provides information about process variables. Specifically, it shows that the quality of decomposition did not significantly affect participants’ choice to use one source of information (the diagram or narrative) more or less, and that participants’ self-reported use of each source of information did not significantly affect their results in the comprehension and problem-solving tests. We return to this process information later, in our protocol analysis.

##

<table><tr><td></td><td>Form</td><td>Decomp</td><td>Order</td><td>UML ex</td><td>Dom kn</td><td>UML Q</td><td>ICI diag</td><td>Prac C</td><td>Prac P</td><td>ICI narr</td><td>Comp</td><td>Prob C</td><td>Prob %</td><td>Ease</td><td>Comp-D</td><td>Comp-N</td><td>Prob-D</td></tr><tr><td>Decomp</td><td>0.01</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Order</td><td>0.01</td><td>-0.02</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>UML ex</td><td>0.04</td><td>-0.09</td><td>0.01</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dom kn</td><td>-0.17*</td><td>-0.05</td><td>0.02</td><td>0.56*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>UML Q</td><td>0.09</td><td>0.02</td><td>0.08</td><td>-0.12</td><td>-0.05</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ICI diag</td><td>-0.02</td><td>-0.09</td><td>-0.08</td><td>-0.13</td><td>-0.14</td><td>0.30*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Prac C</td><td>0.25*</td><td>0.00</td><td>0.02</td><td>-0.05</td><td>-0.11</td><td>0.18*</td><td>0.19*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Prac P</td><td>-0.01</td><td>0.00</td><td>0.06</td><td>-0.06</td><td>-0.12</td><td>0.02</td><td>0.28*</td><td>-0.05</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ICI narr</td><td>0.77*</td><td>-0.06</td><td>-0.02</td><td>0.03</td><td>-0.15</td><td>0.18*</td><td>0.26*</td><td>0.30*</td><td>0.05</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Comp</td><td>0.02</td><td>0.75*</td><td>0.03</td><td>-0.17*</td><td>-0.11</td><td>0.07</td><td>0.03</td><td>0.10</td><td>0.14</td><td>0.09</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Prob C</td><td>0.19*</td><td>0.26*</td><td>-0.14</td><td>-0.17*</td><td>-0.19*</td><td>0.06</td><td>0.31*</td><td>0.16*</td><td>0.19*</td><td>0.35*</td><td>0.27*</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Prob %</td><td>0.17*</td><td>0.34*</td><td>-0.10</td><td>-0.16*</td><td>-0.21*</td><td>0.05</td><td>0.22*</td><td>0.10</td><td>0.20*</td><td>0.28*</td><td>0.31*</td><td>0.86*</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Ease</td><td>0.36*</td><td>0.02</td><td>0.08</td><td>0.01</td><td>-0.08</td><td>0.09</td><td>0.10</td><td>0.14</td><td>0.04</td><td>0.40*</td><td>0.07</td><td>0.32*</td><td>0.23*</td><td></td><td></td><td></td><td></td></tr><tr><td>Comp-D</td><td>0.06</td><td>0.01</td><td>-0.24*</td><td>-0.12</td><td>-0.11</td><td>0.26*</td><td>0.16*</td><td>0.25*</td><td>0.09</td><td>0.04</td><td>0.07</td><td>0.06</td><td>0.02</td><td>0.02</td><td></td><td></td><td></td></tr><tr><td>Comp-N</td><td>(a)</td><td>0.01</td><td>-0.10</td><td>-0.07</td><td>0.03</td><td>-0.10</td><td>-0.13</td><td>-0.09</td><td>0.15</td><td>-0.03</td><td>-0.04</td><td>-0.16</td><td>-0.16</td><td>-0.06</td><td>-0.17</td><td></td><td></td></tr><tr><td>Prob-D</td><td>-0.21*</td><td>0.15</td><td>-0.07</td><td>-0.10</td><td>-0.03</td><td>0.03</td><td>0.13</td><td>-0.01</td><td>0.02</td><td>-0.18*</td><td>0.08</td><td>0.08</td><td>0.09</td><td>-0.20*</td><td>0.22*</td><td>-0.05</td><td></td></tr><tr><td>Prob-N</td><td>(a)</td><td>-0.20</td><td>0.20</td><td>-0.02</td><td>-0.18</td><td>0.15</td><td>0.04</td><td>0.08</td><td>0.10</td><td>0.19</td><td>-0.24*</td><td>-0.13</td><td>-0.13</td><td>-0.18</td><td>0.20</td><td>0.24*</td><td>-0.10</td></tr></table>

q eii litr =  iii it = 1 ilit) Vois ts til nt l il io   i il io = Ds ot  i iol orii ition (at  s  ot o ss  s ss  o   t   s o onn e. Sigs  s ds S   =

rob i Iiai I -lui. p   u  :.     :  :  : c   -  c uce Coni rln  n (r n s-r =  r  oin =    r rs r omml

ofhtheng u-lrd ng u it io ns. nare pe-n u-os sun u-ueo  u e  o s p- -o suon os g u etne rie o es ee-es -o son ose g u sere t o s ee-e -o :sete es oues (ft r e s  e      e e o se) oq pi oi ot, rei oee  oi-oe  oe oi o-oe : oe o osi, i, :oete oey

## 4.2. Tests of Hypotheses

We describe the results for each hypothesis in turn. For Hypothesis 1, we first checked whether the data met the assumption of equal variance in the dependent measure across groups. The data met this assumption (Levene’s test was insignificant, $\mathsf { F } = 0 . 3 9 , \mathsf { p } > 0 . 7 5 )$ . We then ran a univariate ANOVA with decomposition quality and multiple forms of information as factors and comprehension performance as the dependent measure. Table 6 shows the results, which show that comprehension performance was driven by decomposition quality (rather than multiple forms of information), supporting Hypothesis 1. Figure 2a shows the mean difference in performance across groups, which was in line with our prediction for this hypothesis in Table 3.

<table><tr><td colspan="5">Table 6: Results for Hypothesis 1: Comprehension performance</td></tr><tr><td colspan="5">Table 6a: Differences among groups</td></tr><tr><td>Form of Information</td><td>Decomposition quality</td><td>N</td><td>Mean</td><td>Std. Deviation</td></tr><tr><td>Single form</td><td>Lower quality</td><td>42</td><td>4.19</td><td>1.52</td></tr><tr><td></td><td>Higher quality</td><td>40</td><td>8.08</td><td>1.51</td></tr><tr><td>Multiple form</td><td>Lower quality</td><td>42</td><td>4.43</td><td>1.70</td></tr><tr><td></td><td>Higher quality</td><td>41</td><td>7.98</td><td>1.78</td></tr><tr><td colspan="5">Table 6b: Univariate ANOVA</td></tr><tr><td>Source</td><td>df</td><td>F</td><td>Sig.</td><td>Eta Squared*</td></tr><tr><td>Corrected Model</td><td>3</td><td>71.46</td><td>0.00</td><td>0.57</td></tr><tr><td>Intercept</td><td>1</td><td>2357.09</td><td>0.00</td><td>0.94</td></tr><tr><td>Form of information</td><td>1</td><td>0.07</td><td>0.79</td><td>0.00</td></tr><tr><td>Decomp. quality</td><td>1</td><td>213.90</td><td>0.00</td><td>0.57</td></tr><tr><td>Form * Decomp</td><td>1</td><td>0.44</td><td>0.51</td><td>0.00</td></tr><tr><td>Corrected Total</td><td>164</td><td></td><td></td><td></td></tr><tr><td></td><td colspan="4">Adjusted  $R^2$  = .56</td></tr></table>

Eta squared represents the proportion of variance in the dependent variable (DV) explained by the independent variable (IV).

We ran a MANOVA to check whether the results were consistent across decomposition criteria. The MANOVA contained five dependent measures, one for each criterion. Figures 2b-f summarize the results. The results were consistent for three criteria (determinism, coupling, and cohesion). However, the results for two criteria were slightly different. For losslessness (Figure 2b), decomposition quality had a positive effect as expected, but so too did multiple forms of information. For minimality (Figure 2c), decomposition quality had a positive effect as expected, but there was a slight unexpected interaction effect such that students who received the higher-quality decomposition did slightly worse when they had the narrative. While any explanation of these unexpected results can only be speculative, it is worth noting that the questions for losslessness and minimality were the first questions of the comprehension test. Thus, there may have been a carry-over effect from a previous task (from a prior problem-solving question or from the narrative that students just read, depending on the order of treatment that a student received). Moreover, it is important to note that these slight unexpected results did not change the overall result, which was in line with our hypothesis (Figure 2a). Thus, although these results should be borne in mind, we believe there is sufficient evidence to accept Hypothesis 1.

For Hypothesis 2, we first checked whether the coding of students’ problem-solving answers was reliable. The answers were coded by one independent coder. We then had a second independent coder grade approximately half the cases (80 of 165), chosen at random. The coders’ scores showed sufficient inter-rater reliability (ICC[2, 2] varied from 0.72 to 0.90 for the seven questions, Shrout and Fleiss 1979). We then checked whether the data met the assumption of equal variance in the dependent measure across groups. The data met this assumption (Levene’s test was insignificant, F = 1.91, p > 0.10). We then ran a univariate ANOVA with decomposition quality and multiple forms of information as factors and problem-solving performance as the dependent measure. Table 7 shows the results, which indicate that comprehension performance was driven by both factors, but the interaction effect was insignificant. This only partially supports Hypothesis 2, which had predicted a significant interaction effect. Figure 3a shows the mean difference in performance across groups.

![](/api/attachments/WZPNHRD8/fulltext/images/b9192c8c29ef2297fc4180bd7e184458ec2afb24e1b1f1d95adf2a383879ee23.jpg)  
Figure 2a

![](/api/attachments/WZPNHRD8/fulltext/images/2af67a74461bf9cf1d6a464ea8a44016f5c769c0a30d3768b597605fb605909a.jpg)  
Figure 2b

![](/api/attachments/WZPNHRD8/fulltext/images/80b208aa810bfebab9898db146b8cb87232611eb7f7ab3c89c52b0609343debf.jpg)  
Figure 2c

![](/api/attachments/WZPNHRD8/fulltext/images/d91638cbf91c56a621b9ca1000c827e6a31b9b61536cda981ab7ece26ac6f1c6.jpg)

![](/api/attachments/WZPNHRD8/fulltext/images/5a4903ea1e940b63542738585aa86cca0804f03cd67fc5f5d797af2c136d35e8.jpg)  
Figure 2e

Figure 2d  
![](/api/attachments/WZPNHRD8/fulltext/images/ee1fb75fe024ef9648f7fcebe917652727ea03f79181eaac29ad1c7abb0745f8.jpg)  
Figure 2f  
Figure 2: Mean differences in comprehension performance (Hypothesis 1)

Table 7: Results for Hypothesis 2: Problem-solving performance Table 7a: Differences among groups

<table><tr><td colspan="5">Table 7a: Differences among groups</td></tr><tr><td>Form of Information</td><td>Decomposition quality</td><td>N</td><td>Mean</td><td>Std. Deviation</td></tr><tr><td>Single form</td><td>Lower quality</td><td>42</td><td>5.52</td><td>3.04</td></tr><tr><td></td><td>Higher quality</td><td>40</td><td>8.48</td><td>4.98</td></tr><tr><td>Multiple form</td><td>Lower quality</td><td>42</td><td>7.93</td><td>3.65</td></tr><tr><td></td><td>Higher quality</td><td>41</td><td>9.32</td><td>4.31</td></tr><tr><td colspan="5">Table 7b: Univariate ANOVA</td></tr><tr><td>Source</td><td>df</td><td>F</td><td>Sig.</td><td>Eta Squared*</td></tr><tr><td>Corrected Model</td><td>4</td><td>11.23</td><td>0.00</td><td>0.22</td></tr><tr><td>Intercept</td><td>1</td><td>0.19</td><td>0.67</td><td>0.00</td></tr><tr><td>ICI diagram quiz **</td><td>1</td><td>22.09</td><td>0.00</td><td>0.12</td></tr><tr><td>Form of information</td><td>1</td><td>8.00</td><td>0.01</td><td>0.05</td></tr><tr><td>Decomp. quality</td><td>1</td><td>16.47</td><td>0.00</td><td>0.09</td></tr><tr><td>Form * Decomp</td><td>1</td><td>1.16</td><td>0.28</td><td>0.01</td></tr><tr><td>Corrected Total</td><td>164</td><td></td><td></td><td></td></tr><tr><td></td><td colspan="4">Adjusted  $R^{2} = .20$ </td></tr></table>

Eta squared represents the proportion of variance in the DV explained by the IV.  
\*\* We only include this one covariate because when we ran a model including the practice problem-solving test as an additional covariate, this latter variable was not significant.

Problem Solving (Total Correct)  
![](/api/attachments/WZPNHRD8/fulltext/images/b84d97d2447b6697ca6991006adb41d0b23935e10f548d94452d8f736792cefe.jpg)  
Figure 3a

Problem-Solving (Percentage Correct)  
![](/api/attachments/WZPNHRD8/fulltext/images/1554947b9157c39fe4bbf051ab2a4d98aacb3d276ce7d9880dd53f2ce716fba5.jpg)  
Figure 3b  
Figure 3: Mean differences in problem-solving performance (Hypothesis 2)

To see if the lack of a significant interaction effect in our ANOVA had been driven by just one or two questions, we ran a MANOVA with all seven problem-solving questions as the dependent measures. The results were generally consistent with the ANOVA: form of information had a significant positive main effect for four of the problem-solving questions (Questions 1, 2, 3, and 7), decomposition quality had a significant positive main effect for six of the questions (all except Question 5), and the interaction effects were not significant.

Despite no statistically significant interaction effect in the ANOVA or MANOVA, the mean difference in problem-solving results (in Figure 3a above) appears to show a slight interaction effect in the direction we hypothesized. To follow this up, we performed two post-hoc tests.

First, we ran an ANOVA with students’ percentage of correct answers (i.e., correct answers divided by total answers) as the dependent measure rather than students’ total number of correct answers. In this model, the main effects for each factor were significant (i.e., decomposition quality: $\mathsf { F } = 1 2 . 8 , \mathsf { p } <$ .01 one tailed; form of information: $\mathsf { F } = 5 . 3 , \mathsf { p } < 0 . { \overset { \cdot } { 0 } } 2$ one tailed), and the interaction was significant (i.e., decomposition quality \* form of information: $\mathsf { F } = 2 . 9 , \mathsf { p } < . 0 5$ one tailed), consistent with Hypothesis 2. Although we omit the detailed table of results to conserve space, Figure 3b (above) shows the mean difference in performance across groups, which clearly shows an interaction effec consistent with the hypothesis.

Second, we performed sub-sample tests in which we kept one factor constant (by selecting only that half of the sample) while varying the other factor. We performed this for both versions of the dependent measure: students’ total number of correct answers and their percentage of correct answers (correct answers divided by offered answers). Table 8 shows the results. These results suggest that when a novice has a high level on one antecedent factor (either decomposition quality or form of information), an increase in the second factor does not have a major impact on problemsolving performance, but when a novice has a low level on one of the antecedent factors (either decomposition quality or form of information), an increase in the second factor has a significant impact on understanding. This is consistent with Hypothesis 2.

<table><tr><td colspan="4">Table 8: Sub-sample analysis for interaction effect (Hypothesis 2)</td></tr><tr><td rowspan="2">Sub-sample</td><td rowspan="2">Comparison</td><td colspan="2">Significant difference on dependent variable (DV)?</td></tr><tr><td>DV: Correct (Total)</td><td>DV: Correct (Percentage)</td></tr><tr><td>Single form of information</td><td>Decomposition quality: Lower versus higher</td><td>Yes: F = 11, p &lt; .01, eta $^{2}$ =.12</td><td>Yes: F = 18, p &lt; .01, eta $^{2}$ =.18</td></tr><tr><td>Multiple forms of information</td><td>Decomposition quality: Lower versus higher</td><td>No: F = 3, p &gt;.10, eta $^{2}$ =.03</td><td>Yes: F = 5, p = .01, eta $^{2}$ =.06</td></tr><tr><td>Lower quality decomposition</td><td>Form of information: Single versus multiple</td><td>Yes: F = 11, p &lt; .01, eta $^{2}$ =.12</td><td>Yes: F = 12, p &lt; .01, eta $^{2}$ =.13</td></tr><tr><td>Higher quality decomposition</td><td>Form of information: Single versus multiple</td><td>No: F = 1, p &gt;.40, eta $^{2}$ =.01</td><td>No: F = .1, p &gt;.70, eta $^{2}$ &lt;.01</td></tr></table>

Eta squared represents the proportion of variance in the DV explained by the IV.

In summary, while the results from our overall ANOVA and MANOVA only partially supported Hypothesis 2, our two follow-up tests fully supported it. Therefore, we believe there is enough evidence to tentatively support Hypothesis 2.

For Hypothesis 3, we first checked the reliability of our scale, which was adequate (Cronbach’s alpha = 0.77). We then checked for convergent and discriminant validity. The results showed that our items converged and discriminated in the expected way. In a principal component analysis with varimax rotation, the items for ease of understanding the domain loaded on one factor (> 0.85), the items for ease of understanding the diagrams loaded on a separate factor (> 0.85), and the cross loadings were less than 0.20. Finally, we checked whether the data met the assumption of equal variance in the dependent measure across groups. The data met this assumption (Levene’s test was insignificant, $\mathsf { F } = 1 . 4 3 , \mathsf { p } > 0 . 2 0 )$ Given that our data passed all three tests, we then ran an ANOVA with ease of understanding the domain as the dependent measure. Table 9 presents the results, and Figure 4 shows the mean differences. As Table 9 and Figure 4 show, the results do not support Hypothesis 3. Consistent with the hypothesis, students who received multiple forms of information found the domain to be easier to understand. However, in contrast to the hypothesis, decomposition quality had no effect on ease of understanding, nor was there a significant interaction effect.

Table 9: Results for Hypothesis 3: Ease of understanding the domain\*\* Table 9a: Differences among groups

<table><tr><td>Form of Information</td><td>Decomposition quality</td><td>N</td><td>Mean</td><td>Std. Deviation</td></tr><tr><td>Single form</td><td>Lower quality</td><td>41</td><td>1.73</td><td>0.98</td></tr><tr><td></td><td>Higher quality</td><td>39</td><td>1.68</td><td>0.82</td></tr><tr><td>Multiple form</td><td>Lower quality</td><td>40</td><td>2.36</td><td>0.90</td></tr><tr><td></td><td>Higher quality</td><td>41</td><td>2.46</td><td>1.00</td></tr></table>

Table 9b: Univariate ANOVA

<table><tr><td>Source</td><td>df</td><td>F</td><td>Sig.</td><td>Eta Squared*</td></tr><tr><td>Corrected Model</td><td>3</td><td>7.91</td><td>0.00</td><td>0.13</td></tr><tr><td>Intercept</td><td>1</td><td>705.00</td><td>0.00</td><td>0.82</td></tr><tr><td>Form of information</td><td>1</td><td>23.42</td><td>0.00</td><td>0.13</td></tr><tr><td>Decomp. quality</td><td>1</td><td>0.03</td><td>0.87</td><td>0.00</td></tr><tr><td>Form * Decomp</td><td>1</td><td>0.27</td><td>0.60</td><td>0.00</td></tr><tr><td>Corrected Total</td><td>160</td><td></td><td></td><td></td></tr><tr><td></td><td colspan="4">Adjusted  $R^2$  = 12</td></tr></table>

$$
R ^ {2} = . 1 2
$$

大 Eta squared represents the proportion of variance in the DV explained by the IV \*\* The scale for each of understanding asked about “difficulty” (see the Appendix) but the scores were reverse coded so that higher values reflect greater ease.

Ease of Understanding the Domain  
![](/api/attachments/WZPNHRD8/fulltext/images/69b9f48bee11f75392b9ed5a9c39ea6d7afda4f8221fc6d7a297883337d5b198.jpg)  
Figure 4: Mean differences in perceived ease of understanding (Hypothesis 3)

## 4.3. Summary of the Results

Our results suggest that we can accept Hypothesis 1, tentatively accept Hypothesis 2, and reject Hypothesis 3. At first glance, these results might not seem surprising because Burton-Jones and Meso (2006) also found significant differences on tests of actual understanding, but not on tests of perceived ease of understanding. However, the results were quite surprising to us because we had made the treatment for decomposition quality very strong, i.e., the lower quality decomposition was much worse, in our view, than the higher quality decomposition.

Because this result was a surprise, we set out to determine a possible explanation. Recall from our theory section (see Table 3) that the difference between our hypothesis for problem-solving and our hypothesis for ease of understanding was that for problem-solving, we hypothesized that our manipulation of decomposition quality would result in a direct information content effect and an incidental processing effect. For ease of understanding, we hypothesized that our manipulation of decomposition quality would result in an incidental processing effect only. In this light, given that decomposition quality affected our problem-solving results but not our ease of understanding results, one possible reason for this pattern of results is that the direct information content effect did occur but that the incidental processing effect was marginal or non-existent. To determine whether this explanation was plausible, we ran a protocol study.

## 4.4. Protocol Study

Twenty-six students from the same student body as that used in the full experiment (i.e., second-, third-, and fourth-year business school students) participated voluntarily. Each student performed the task singly (i.e., there were 26 sessions), and each session was recorded. Because of technical/administrative limitations, we were only able to use the data from 20 of these 26 sessions (the online application had an error in two cases, one student misunderstood the instructions, one student turned off the recording device, and one student’s voice could not be understood by the coders). Each student was randomly assigned to one of the four groups, which resulted in one group of four students, two groups of five, and one group of six. The materials and procedures were the same as in the full experiment except that students were asked to talk aloud during the tasks and they were given five minutes per problem-solving question rather than 3.5 minutes because of the extra time required to speak aloud (as in Burton-Jones and Meso 2006). Each student’s session was recorded using Camtasia Studio<sup>TM</sup> (http://www.techsmith.com/camtasia.asp) from TechSmith Corp. Using this application, we simultaneously recorded: 1. screen-cam records at five screens per second of the student’s computer screen, 2. the student’s voice recorded into a headset microphone that s/he wore, and 3. a video recording of the student as s/he worked, captured via a Webcam connected to the computer (allowing us to see the user’s facial expressions as s/he talked and worked on the task). All three types of data were saved in an integrated file in .avi format, which coders could then view in a video player.

An independent coder transcribed all of the recordings and coded the protocols. The coder coded for two types of evidence. The first was incidental processing. Incidental processing reflects additional processing that an individual has to undertake to deal with confusing or extraneous material in information s/he receives (Mayer and Moreno 2003, p. 46). Following Burton-Jones and Meso (2006), we used the notion of a cognitive breakdown to measure incidental processing. Cognitive breakdowns occur when a line of thought fails. They are reflected in long pauses or in comments that reflect an individual’s inability to come up with an answer to a question. Given a fixed amount of cognitive processing available to a subject, we hypothesized that all else being equal, an increase in incidental processing would cause the participant more difficulty understanding the material, and hence, s/he would suffer more breakdowns. We felt that this would be particularly likely in the context of our problem-solving task because it was designed to be challenging (as discussed in Section 4.1), thus subjects were likely working near the limits of their cognitive capacity. As in Burton-Jones and Meso (2006), we recognize that a student might be able to recover from some of his/her breakdowns. Therefore, we used two measures of breakdowns: total number of breakdowns: the total number of breakdowns a student experienced during the problem-solving task (whether s/he recovered from these breakdowns or not); and net breakdowns: the total number of breakdowns experienced during the problem-solving task from which s/he did not recover (i.e., breakdowns minus recoveries).

The second type of evidence was the source of information that students used during the tasks (i.e., the narrative or diagram). As noted in the data screening section of our analysis from the main experiment, students reported that they used the diagrams more than the narrative during the comprehension test but about the same during the problem-solving task. We wanted to check the video recordings to see if the same pattern was evident in the objective video data. Thus, our final measure was information seeking time, which reflects the time that students spent seeking information to an answer from the narrative (if available) or the diagrams.

To check whether the independent coders’ ratings were reliable, we selected five students’ recordings at random and had a second independent coder rate each recording. We found that the ratings were reliable (total number of breakdowns, ICC[2,2] = 0.87; total number of breakdowns not overcome, ICC[2,2] = 0.89, time looking at the diagram, ICC[2,2] = 0.96, time looking at the narrative, ICC[2,2] = 0.85). We also recruited two independent coders to score students’ answers to the problem-solving

<table><tr><td colspan="9">Table 10: Descriptive statistics for the protocol study</td></tr><tr><td></td><td colspan="2">Single/Lower quality N=6</td><td colspan="2">Single/Higher quality N=5</td><td colspan="2">Multiple/Lower quality N=4</td><td colspan="2">Multiple/Higher quality N=5</td></tr><tr><td></td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td></tr><tr><td>Dependent variables:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Comp</td><td>4.0</td><td>1.3</td><td>7.2</td><td>1.1</td><td>3.8</td><td>1.3</td><td>7.2</td><td>2.2</td></tr><tr><td>Prob C</td><td>6.7</td><td>3.4</td><td>9.1</td><td>1.8</td><td>12.3</td><td>4.2</td><td>12.7</td><td>2.6</td></tr><tr><td>Prob %</td><td>0.3</td><td>0.1</td><td>0.4</td><td>0.1</td><td>0.4</td><td>0.1</td><td>0.5</td><td>0.1</td></tr><tr><td>Ease</td><td>2.2</td><td>0.7</td><td>2.9</td><td>0.7</td><td>2.5</td><td>0.9</td><td>2.4</td><td>0.6</td></tr><tr><td>Breakdowns:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Break</td><td>8.2</td><td>4.1</td><td>6.4</td><td>5.0</td><td>6.8</td><td>3.1</td><td>4.8</td><td>2.4</td></tr><tr><td>Break (Net)</td><td>7.8</td><td>3.9</td><td>4.6</td><td>3.4</td><td>5.3</td><td>1.0</td><td>4.6</td><td>2.1</td></tr><tr><td>Info. seeking time:</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Comp-N Video</td><td>na</td><td>na</td><td>na</td><td>na</td><td>25.5</td><td>50.3</td><td>69.5</td><td>39.8</td></tr><tr><td>Comp-D Video</td><td>191.0</td><td>65.0</td><td>204.8</td><td>56.5</td><td>128.5</td><td>95.3</td><td>142.0</td><td>64.7</td></tr><tr><td>Comp-N Self</td><td>na</td><td>na</td><td>na</td><td>na</td><td>1.3</td><td>1.9</td><td>1.4</td><td>0.9</td></tr><tr><td>Comp-D Self</td><td>2.5</td><td>0.8</td><td>2.8</td><td>0.5</td><td>3.0</td><td>0.8</td><td>2.8</td><td>0.8</td></tr><tr><td>Prob-N Video</td><td>na</td><td>na</td><td>na</td><td>na</td><td>38.8</td><td>10.1</td><td>33.8</td><td>22.3</td></tr><tr><td>Prob-D Video</td><td>101.3</td><td>42.1</td><td>85.2</td><td>26.5</td><td>50.5</td><td>28.4</td><td>40.2</td><td>32.3</td></tr><tr><td>Prob-N Self</td><td>na</td><td>na</td><td>na</td><td>na</td><td>3.3</td><td>1.0</td><td>2.6</td><td>0.9</td></tr><tr><td>Prob-D Self</td><td>1.7</td><td>0.8</td><td>2.6</td><td>1.1</td><td>1.3</td><td>1.3</td><td>1.6</td><td>0.9</td></tr><tr><td colspan="9">Key:Groups: Single: Single form of information; Multiple: Multiple forms of information; Lower quality: Lower quality decomposition; Higher quality: Higher quality decomposition.Dependent variables: Comp: Comprehension correct; Prob C: Problem-solving (total number of correct answers); Prob %: Problem-solving (% correct answers); Ease: Ease of understanding the domain.Breakdowns: Break: Total number of breakdowns; Break (Net): Total number of breakdowns not overcome.Information seeking variables: Comp-N Video: Seconds using the narrative during the comprehension questions; Comp-D Video: Seconds using the diagrams during the comprehension questions; Comp-N Self: Self-reported use of the narrative during the comprehension questions (0-4 scale); Comp-D Self: Self-reported use of the diagrams during the comprehension questions (0-4 scale); Prob-N Video: Seconds using the narrative during the problem-solving questions; Prob-D: Seconds using the diagrams during the problem-solving questions; Prob-N Self: Self-reported use of the narrative during the problem-solving questions (0-4 scale); Prob-D Self: Self-reported use of the diagrams during the problem-solving questions (0-4 scale).na: No statistic because the narrative was only offered when students received multiple forms of information.For Hypothesis 1, the results were the same as in the main experiment. Comprehension performance was influenced strongly by decomposition quality, but it was not affected by having multiple forms of information. Recall from Table 3 that we hypothesized that students would look primarily at the diagrams rather than the narrative to answer the comprehension questions. The evidence of “information seeking” supports this view. Table 10 shows that students used the diagrams much more than the narrative to answer the comprehension questions (indicated in both the objective measures and the self-reported measures).</td></tr></table>

For Hypothesis 2, our results also mirror those of the full experiment. The self-reported and objective data on information-seeking times were slightly different, but the objective data supported our expectation that subjects would use the narrative and diagrams to a similar extent during the problemsolving task. Also, consistent with the full experiment, having multiple forms of information and higher quality decompositions helped problem-solving performance. While not shown to conserve space, the detailed results showed an interaction effect similar to that in Figure 3. Interestingly, the data on breakdowns supports these results, but only in part. Specifically, Tables 10 and 11 show that students had fewer breakdowns when they had multiple forms of information and higher quality decompositions, consistent with our hypothesis, but Table 11 shows that these correlations were insignificant. Moreover, Table 10 shows that students’ total number of breakdowns varied from 4 to 8 depending on the experimental group. As there were 7 problem-solving questions, this reflects only half-to-one breakdown per question. Thus, although multiple forms of information and higher quality decompositions led to fewer breakdowns, there were very few breakdowns in any of the groups.

Table 11: Correlation matrix from the protocol study (Spearman’s rho)

<table><tr><td></td><td>Form</td><td>Decomp</td><td>Comp</td><td>Prob C</td><td>Prob %</td><td>Break</td><td>Break (Net)</td></tr><tr><td>Decomp</td><td>0.10</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Comp.</td><td>0.01</td><td>0.78**</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Prob C</td><td>0.61**</td><td>0.26</td><td>0.21</td><td></td><td></td><td></td><td></td></tr><tr><td>Prob %</td><td>0.47**</td><td>0.50**</td><td>0.24</td><td>0.79**</td><td></td><td></td><td></td></tr><tr><td>Break</td><td>-0.23</td><td>-0.26</td><td>-0.12</td><td>0.05</td><td>0.01</td><td></td><td></td></tr><tr><td>Break (Net)</td><td>-0.26</td><td>-0.26</td><td>-0.08</td><td>-0.08</td><td>-0.14</td><td>0.95**</td><td></td></tr><tr><td>Ease</td><td>-0.05</td><td>0.22</td><td>0.24</td><td>-0.08</td><td>0.13</td><td>-0.31*</td><td>-0.28</td></tr></table>

Key: Variable names defined above in Table 10. \*\* = p < 0.05 (one-tailed), \* = p < 0.10 (one-tailed)

This is an important result because it allows us to draw a more precise conclusion regarding H2. Recall from Table 3 that we predicted that problem-solving performance would be driven by the multimedia effect, the direct information content effect, and the incidental processing effect. These results suggest that the multimedia effect was significant (because the correlation between multiple forms of information and problem-solving performance was significant), the direct information content effect was significant (because the correlation between decomposition quality and problem-solving performance was significant), but the incidental processing effect was insignificant (because the correlation between breakdowns and both of the antecedents [multiple forms of information and decomposition quality] was insignificant).

The results for Hypothesis 3 differed slightly from those in the full experiment. In the full experiment, form of information had a significant effect on ease of understanding, while decomposition quality did not. In the protocol study, Table 11 shows that neither factor had a significant effect on ease of understanding. Again, the data on breakdowns help explain this result. Specifically, Table 11 shows that the number of breakdowns was significantly correlated with ease of understanding (as expected). However, as noted above, subjects did not suffer many breakdowns, and our treatments (form of information and decomposition quality) only slightly increased the number of breakdowns. Thus, the effect on incidental processing seemed to be too slight to affect ease of understanding. This confirmed the expectation we drew at the conclusion of the full experiment.

## 4.5. Summary of the Results

On the basis of the results from our full experiment and protocol study, we conclude that multiple forms of information and higher quality decompositions can significantly affect individuals understanding (both surface and deep understanding). However, although individuals sometimes find a domain easier to understand when they have access to multiple forms of information (as we found in the full experiment), they do not appear to find the domain easier to understand when they have access to a higher quality decomposition. Therefore, decomposition quality appears to affect individuals’ understanding of the domain directly (without their awareness) rather than having an indirect effect through changing the amount of incidental processing that they undertake to

understand the domain.

## 5. Discussion

We first discuss the implications of our study for research and practice and then its limitations.

## 5.1. Implications for Research

We believe that our results have five implications for research. First, our study is the first to our knowledge to have integrated a theory that focuses on the quality of information in a conceptual model (such as the Good Decomposition Model) with a theory that focuses on the form in which information is provided (such as Multimedia Learning Theory). We believe these two types of theories are complementary and that further opportunities exist to integrate them. For example, Wand and Weber (1990) proposed three theories that can be used to assess the quality of information in a conceptual model: the Representation Model, State-Tracking Model, and Good Decomposition Model. We only investigated one of these theories. Other theories (such as semiotics) could also be used to explain variations in the quality of conceptual models (Lindland et al. 1994). Similarly, Mayer (2005, p. 6) describes seven basic principles of multimedia learning. We only investigated one of these principles (the multimedia principle). Great opportunities exist for future researchers to extend different elements of Wand and Weber’s theories (or other theories such as semiotics) and different principles from Mayer’s theory to determine what information to show in a conceptual model and in what form, or forms, to show it.

Another way to extend our work would be to use theories of cognitive fit (Khatri et al. 2006). The theories we used in our study are somewhat universal in orientation – they do not account for contingencies, such as the nature of the person reading the model, that prior studies suggest will affect readers’ understanding (Gemino and Wand 2003, p. 82). Theories of cognitive fit would be particularly useful to explain when the effort required to achieve high decomposition quality or provide multiple forms of information would be most beneficial. Based on prior studies (Burton-Jones and Weber 1999, Parsons and Cole 2005), we believe a prima facie case could be made that higher quality decompositions and multiple forms of information would be most useful for novice users or analysts who have no or little knowledge of the domain shown in the model, but less useful for experts with substantial knowledge of the domain. It would be useful to test this (both in laboratory experiments and in the field) because researchers would then be in a better position to make recommendations to practice about the likely benefits of following good decomposition principles and good multimedia principles. Research with practitioners would be especially valuable because, according to Norman (1993, p. 258), “It takes a minimum of five thousand hours to turn a novice into an expert” Therefore, researchers may have to recruit practitioners with substantial experience instead of or in addition to student subjects if they really wish to study the effects of expertise.

A third research direction flows from our findings regarding decomposition quality. As we noted earlier, no algorithm exists to create a good decomposition or to prove that a decomposition is, in fact, good. Given that two studies have shown that good decompositions are helpful (Burton-Jones and Meso 2006, and the present study), we believe researchers should have sufficient motivation to develop algorithms or rules that modelers can use to create models that manifest a good decomposition. The development of rules for conceptual modeling is a burgeoning field (Evermann and Wand 2006). Such work would contribute greatly to research and practice.

Fourth, our results help clarify and extend the findings of earlier work by Burton-Jones and Meso (2006). As in our study, Burton-Jones and Meso (2006) found that decomposition quality affected understanding. However, the reasons given in the two studies differed. Burton-Jones and Meso (2006) argued that higher quality decompositions increase understanding by helping individuals to overcome cognitive breakdowns they experience when trying to understand the domain. Our theory and results were different and suggest that decomposition quality affects understanding in two ways: primarily by affecting a reader’s interpretation of the domain directly (i.e., s/he simply assumes that the information in the conceptual model is correct), and secondarily, by causing the reader to engage in additional incidental processing, which, in turn, results in higher cognitive breakdowns. Although more research is needed to verify the pathway between decomposition quality and understanding, we believe the explanation in our study is more complete and more accurate than that in Burton-Jones and Meso (2006).

Finally, we believe that our results for perceived ease of understanding, and our post-hoc analysis of why these result occurred, help contribute to the literature on individuals’ perceptions of conceptual models and the domains they represent (Maes and Poels 2007). Although Burton-Jones and Meso (2006) also found that decomposition quality had no effect on ease of understanding, we did not expect this to occur in our study because we made the treatment for decomposition quality very strong. However, it seems that our subjects were not troubled by the deficiencies in our lower-quality models, despite these deficiencies having a direct effect on subjects’ understanding. Importantly, this result does not appear to be a methodological artifact. That is, it is not the case that subjects do feel the domain is harder to understand but that our measures do not pick up this difficulty. Rather, our results suggest that it is a substantive issue. That is, it seems that subjects simply do not experience significant difficulties understanding the domain – they interpret the information without any difficulties, and then rely on it even if the information is deficient. We believe that this is an interesting research outcome and deserves future research. For example, one immediate follow-on question would be whether the result would be the same if subjects were made aware of the potential for errors in the conceptual models or the actual errors in their understanding of the domain (reflected in their answers to the comprehension and problem-solving questions). Cognitive dissonance theory (Festinger 1957) would suggest that when individuals are given feedback about their understanding of the domain, they will revise their perceptions so that they are consistent with the feedback (i.e., their actual understanding). It would be interesting to empirically test whether this prediction holds.

## 5.2. Implications for Practice

The research has two general implications for practice. First, our results confirm those from two earlier studies (Burton-Jones and Meso 2006, Gemino 2004) and suggest that it would be useful for modelers to ensure that they: (a) create models that manifest a good decomposition of the domain, and (b) use multimedia principles when preparing and delivering conceptual models, such as accompanying a conceptual model with a textual narrative of the domain. Our study also suggests that, while modelers would benefit from performing both of these activities, one will sometimes be more useful than the other. For example, given that diagrams are more parsimonious than text, individuals may sometimes focus more on the models than the narrative (as we found in our comprehension test). In such cases, ensuring the model manifests a good decomposition is more important than having an accompanying textual narrative. However, if practitioners find it too costly or too difficult to ensure that their models manifest a good decomposition (e.g., due to an inability to train staff in good decomposition techniques), our results suggest that they should not only accompany the conceptual model with alternative forms of information such as a textual narrative but also encourage staff to read this additional information rather than relying solely on the models.

Interestingly, after conducting this study, we came across a methodology called “literate modeling” developed a decade ago by British Airways that instructs modelers to include narratives together with UML diagrams in a similar, but even more detailed fashion, than we studied (Arlow et al. 1999). Based on their personal experience at British Airways, Arlow et al. (1999) concluded that literate modeling was especially helpful for individuals who lacked domain knowledge, modeling knowledge, or both. We are unaware of any scientific study of the effectiveness of their technique, but given the results of our study, we are not surprised that practitioners have discovered the benefits of including UML diagrams together with alternative forms of information. It would be interesting to discover what other techniques practitioners are using along these lines and to extend and test them using the theories discussed in this study.

The second main implication for practice is that our results suggest that practitioners should be cautious not to read too much into individuals’ feedback about how easy it was for them to understand the domain shown in a conceptual model. In our study and in Burton-Jones and Meso (2006), the correlation between individuals’ perceptions of how easy it was to understand the domain and their actual understanding was low (varying from -.08 to .32 in this study). Certainly it would be useful in practice if modelers could create models that both convey accurate information and convey it in an easy-to-understand manner. However, research is not sufficiently advanced to inform practitioners about the most effective way to do so.

## 5.3. Limitations

Although we believe our study makes a good contribution, it also has important limitations. In terms of internal validity, our use of a randomized experiment helped eliminate many confounding factors. However, recall that we verified that each decomposition condition affected subjects’ comprehension, but we did not do so for subjects’ problem-solving or ease of understanding. Thus, while we can conclude that each decomposition condition affected surface understanding, we cannot draw the same conclusion for our other dependent measures. Also, recall that we found what appeared to be a carry-over effect in our comprehension test in the main experiment (for our test of losslessness). However, this was only a speculation; we could not verify it because we only included the comprehension questions in one order. If we had randomized the order of comprehension questions, we would have been able to test whether it was, in fact, a carry-over effect or, instead, a substantive effect.

In terms of construct validity, we operationalized each construct in our study in limited ways. Following Campbell and Fiske (1959), it would have been ideal if we manipulated each treatment in multiple ways (e.g., by manipulating each decomposition condition in several ways, as described in Burton-Jones and Meso 2006, p. 44), if we had measured each dependent variable in multiple ways (e.g., by having objective and subjective measures for each dependent variable), and if we had studied the effects of our treatments on our dependent variables in the context of different tasks. However, we did not do so. Thus, the reader should not over-generalize from our results – they are limited to the treatments, measurement methods, and tasks that we used. While the consistency of support for the Good Decomposition Model and Multimedia Learning Theory in our study and prior studies (Burton-Jones and Meso 2006, Gemino 2004, Masri et al. 2006) should give readers comfort, more research is needed using different treatments, dependent measures, and tasks before we can draw general conclusions.

In terms of statistical conclusion validity, the samples in our full experiment and protocol study were relatively small. Thus, some of our insignificant results might reflect Type 2 error. Based on our protocol study, we believe this is unlikely to be the case for Hypothesis 3 (i.e., we believe that decomposition quality does not have a significant effect on ease of understanding). Given that we found partial support for the interaction effect in our tests of Hypothesis 2, it is possible that the lack of a significant interaction effect in our ANOVA for that hypothesis reflects Type 2 error. However, it is important to keep in mind that the effect size for that interaction effect was small. Thus, even if we had used a larger sample size and found a statistically significant interaction effect, the practical significance of the effect would likely have still been low.

Finally, in terms of external validity, we used a sample of university students rather than a sample of practitioners. Moreover, we cannot say that the materials, tasks, or experimental procedures we used faithfully reflect those used in organizations in practice. In our design, we have traded off internal validity for external validity (Parsons and Cole 2005). Very little is actually known of how conceptual models are used in practice (Dawson and Swatman 1999, Sarker and Lee 2006). Clearly, more field studies are needed on this topic so that laboratory researchers can know how to create tasks and procedures that faithfully reflect those in real life.

## 6. Conclusion

Our study aimed to determine what factors affect the extent to which a conceptual model can help novices (i.e., individuals who lack an understanding of conceptual modeling techniques and the business domain) to obtain an understanding of a business domain. We focused on two aspects of understanding: process (reflected in individuals’ ease of understanding) and product (reflected in individuals’ surface and deep understanding). We also focused on two factors that we predicted would affect novices’ ability to obtain an understanding of a domain: decomposition quality and multiple forms of information. Our results suggest that both factors are influential, but the two factors work differently depending on the type of understanding sought.

When novices sought a surface understanding, we found that they looked to the most parsimonious form of information, which in our study was a conceptual model rather than a textual narrative. Deficiencies in that form (such as decomposition deficiencies in the model) then had a direct affect on their understanding. When novices sought a deep understanding, we found that they used whatever forms of information they were given. Their deep understanding was greatest when they were given multiple forms of information and when the models they received manifested a good decomposition.

Finally, we found that novices’ perceptions of how easy it was to understand the domain did not reflect the accuracy of the understanding they obtained. Instead, our protocol study revealed that subjects generally relied on the information they read. Rather than being confused by questionable, unclear, or obscure information, subjects seemed to simply take the information at face value, report that it was easy to understand, and then rely on the information, often leading them to perform poorly in tests of actual understanding.

Overall, our results suggest that it would be fruitful for researchers and practitioners to further investigate the benefits that can be obtained by following decomposition principles and multimedia principles when preparing conceptual models, and that researchers and practitioners should be aware of the extent to which individuals’ actual understanding and their self-reported ease of understanding can be disconnected in practice.

## Acknowledgements

We thank Palash Bera, Sase Singh, Carson Woo, and Yair Wand for their advice during our research, Mohammed Issah, Yow-Hann Lee, and Roger Yin for developing and maintaining the systems used in our experiments, King-yi Chan, Ivie Ko, Fei Sun, and Bessie Wu for coding our data, and Fei Sun for his help supervising the experiments. The research was supported by funds from the Natural Sciences and Engineering Research Council of Canada. We thank the SE and our review team for very constructive advice that greatly improved the paper.

## References

Agarwal, R., Sinha, A.P., and Tanniru, M. "Cognitive Fit in Requirements Modeling: A Study of Object and Process Methodologies," Journal of Management Information Systems, (13:2) 1996, pp. 137–164.

Arlow, J., Emmerich, W., and Quinn, J. "Literate Modelling — Capturing Business Knowledge with the UML," in J. Bézivin and P.-A. Muller (Eds.) UML '98, Lecture Notes in Computer Science 1618, Springer-Verlag Berlin Heidelberg, 1999, pp. 189-199.

Ashcraft, M.H. Cognition. Prentice Hall, Upper Saddle River, NJ., 2002.

Boehm, B., and Basili, V.R. "Software Defect Reduction Top-10 List," IEEE Computer (34:1), 2001, pp. 135-137.

Bunge, M. 1977. Treatise on Basic Philosophy: Vol. 3: Ontology I: The Furniture of the World. Reidel, Boston, MA.

Burton-Jones, A. and Meso, P.M. “Conceptualizing Systems for Understanding: An Empirical Test of Decomposition Principles in Object-oriented Analysis,” Information Systems Research, (17:1), 2006, pp 38-60.

Burton-Jones, A., and Weber, R. "Understanding Relationships with Attributes in Entity-Relationship Diagrams," in Proceedings of the 20<sup>th</sup> International Conference on Information Systems (ICIS), P. De & J. DeGross (eds.), Charlotte, NC, 1999, pp. 214-228.

Campbell, D.T., and Fiske, D.W. "Convergent and Discriminant Validity by the Multitrait-Multimethod Matrix," Psychological Bulletin (56) 1959, pp 81-105.

Checkland, P.B. Systems Thinking, Systems Practice, John Wiley & Sons, UK, 1999.

Chen, D., Chen W., and Kavi, K. "Visual Requirement Representation," The Journal of Systems and

Software, (61) 2002, pp. 129–143.

Conger, S. The New Software Engineering. Wadsworth Publishing Co., Belmont, CA., 1994

Cook, T.D., and Campbell, D.T. Quasi-Experimentation: Design & Analysis Issues for Field Settings Houghton Mifflin Company, USA, 1979.

Davies, I., Green, P., Rosemann, M., Indulska, M., and Gallo, S. “How Do Practitioners Use Conceptual Modeling in Practice?” Data & Knowledge Engineering, (58:3), 2006, 358-380.

Dawson, L., and Swatman, P. "The Use of Object-Oriented Models in Requirements Engineering: A Field Study," in Proceedings of the 20<sup>th</sup> International Conference on Information Systems, P. De and J. I. DeGross (eds.), Charlotte, NC, 1999, pp. 260-273.

Evermann, J. and Wand, Y. "Ontological Modelling Rules for UML: An Empirical Assessment," Journal of Computer Information Systems (47:1), Fall 2006.

Festinger, L. A Theory of Cognitive Dissonance, Stanford University Press, CA. 1957.

Gemino, A. "Empirical Comparisons of Animation and Narration in Requirements Validation," Requirements Engineering Journal (9), 2004, pp. 153-168.

Gemino, A. and Wand, Y. "Evaluating Modeling Techniques Based on Models of Learning," Communications of the ACM (46:10) Oct 2003, pp. 79-84.

Gemino, A. and Wand Y. “Complexity and Clarity in Conceptual Modeling: Comparison of Mandatory and Optional Properties,” Data & Knowledge Engineering (55:3) 2005, pp. 301-326.

Huff, A.S. Mapping Strategic Thought. New York: Wiley, 1990.

Kettinger, W.J., and Lee, C.C. "Zones of Tolerance: Alternative Scales for Measuring Information Systems Service Quality," MIS Quarterly (29:4), 2005, pp. 607-621.

Khatri, V., Vessey, I., Ramesh, V., Clay, P., and Park, S. "Understanding Conceptual Schemas: Exploring the Role of Application and IS Domain Knowledge," Information Systems Research (17:1), 2006, pp. 81-89.

Kobryn, C. "UML 2001: A Standardization Odyssey," Communications of the ACM (42:10), 1999, pp. 29-37.

Kung, C.H., and Solvberg, A. "Activity Modelling and Behavior Modelling," in: Information Systems Design Methodologies: Improving the Practice, T.W. Olle, H.G. Sol and A.A. Verrijn-Stuart (eds.), IFIP, Amsterdam, North-Holland, 1986, pp. 145-171.

Larkin, J., and Simon, H. “Why a Diagram is (Sometimes) Worth Ten Thousand Words,” Cognitive Science (11) 1987, pp. 65-99.

Larman, C. Applying UML and Patterns: An Introduction to Object-Oriented Analysis and Design and the Unified Process, Prentice Hall, Englewood Cliffs, N.J. 2001.

Lindland, O.I., Sindre, G., and Solvberg, A. "Understanding Quality in Conceptual Modeling," IEEE Software (11:2) March 1994, pp. 42-49.

Maes, A., and Poels, G. "Evaluating Quality of Conceptual Modeling Scripts Based on User Perceptions," Data & Knowledge Engineering (63:3) 2007, pp. 701-724.

Masri, K., Gemino, A., and Parker, D. "What Are You Staring at? Comparing Iconic Graphics with Text in Entity Relationship Diagramming," Proceedings of the Administrative Sciences Association of Canada, 2006, Banff, AB, Canada.

Mayer, R.E. "Models for Understanding," Review of Educational Research, (59:1), 1989, pp. 43-64.

Mayer, R.E. Multimedia Learning, Cambridge University Press, New York, New York, 2001.

Mayer, R.E. (Ed.) The Cambridge Handbook of Multimedia Learning, Cambridge University Press, New York, New York, 2005.

Mayer, R.E. and Moreno, R. "Nine Ways to Reduce Cognitive Load in Multimedia Learning," Educational Psychologist (38:1) 2003, pp. 43-52.

Norman, D. Things that Make us Smart, Addison Wesley, Reading Massachusetts 1993.

Newell, A., and Simon, H.A. Human Problem Solving, Prentice Hall, Englewood Cliffs, NJ, 1972.

Parsons, J., and Cole, L. "What do the Pictures Mean? Guidelines for Experimental Evaluation of Representation Fidelity in Diagrammatical Conceptual Modeling Techniques," Data and Knowledge Engineering (55:3), 2005, pp. 327-342.

Paulson, D., Wand, Y. "An Automated Approach to Information Systems Decomposition," IEEE Transactions on Software Engineering," (18:3), 1992, pp. 174–189.

Patel, V.L., Allen, V.G., Arocha, J.F., and Shortliffe, E.H. "Representing Clinical Guidelines in GLIF: Individual and Collaborative Expertise," Journal of the American Medical Informatics Association (5:5) 1998, pp. 467-483.

Payne, J.W., Bettman, J.R., and Johnson, E.J. The Adaptive Decision Maker, Cambridge University Press, Cambridge UK., 1993.

Pidd, M. Tools for Thinking: Modelling in Management Science. Wiley, Chichester, 2003.

Sarker, S. and Lee, A.S. "Does the Use of Computer-Based BPC Tools Contribute to Redesign Effectiveness? Insights From a Hermeneutic Study," IEEE Transactions on Engineering Management , 2006, pp. 1-16.

Shanks, G., Tansley, E., Nuredini, J., Tobin, D., and Weber, R. "Representing Part-Whole Relationships in Conceptual Modeling: An Empirical Evaluation," MIS Quarterly, 2008, forthcoming.

Shrout, P.E., and Fleiss, J.L. "Intraclass Correlations: Uses in Assessing Rater Reliability," Psychological Bulletin (86:2) 1979, pp 420-428.

Siau, K. "Informational and Computational Equivalence in Comparing Information Modeling Methods," Journal of Database Management (15:1), 2004, pp. 73-86.

Simon, H. A. The Sciences of the Artificial. MIT Press, Cambridge, MA., 1996.

Vessey, I. and Conger, S.A. "Requirements Specification: Learning Object, Process, and Data Methodologies," Communications of the ACM (37:5) 1996, pp. 102–113.

Wand, Y., and Weber, R. "An Ontological Model of an Information System," IEEE Transactions on Software Engineering (16), 1990, pp. 1282-1292.

Wand, Y. and Weber, R. "Information Systems and Conceptual Modeling—A Research Agenda," Information Systems Research, (13:4) 2002, pp. 363–376.

Wand, Y. and Woo, C.C. “Object-Oriented Analysis -- Is it Really that Simple?” Proceedings of the Third Workshop on Information Technologies and Systems (WITS’93), (Orlando, Florida, December 4-5, 1993), pp. 186-195.

Wand, Y., Woo, C.C. and Jung, D. "Object-Oriented Modeling: From Enterprise Model to Logical Design," Proceedings of the Tenth Workshop on Information Technologies and Systems (WITS'00, Brisbane, Australia, December 9-10, 2000), pp. 25-30.

Weber, R. Ontological Foundations of Information Systems, Coopers & Lybrand and Accounting Association of Australia and New Zealand, Melbourne, Australia, 1997.

## Appendix: Experimental materials

## 1. Exercise Instructions (35 seconds)

The exercise will take 1 hour and 50 minutes. Each task has a fixed amount of time. When the time expires for each task, the system will automatically move you on to the next task. If you have any questions during the exercise, please ask your instructor.

## Tasks:

1. Read these instructions (35 seconds)

2. Pre-Experiment Questionnaire (1 minute)

3. UML tutorial (12 minutes)

4. Review UML diagrams and complete quiz (20 minutes)

5. Review example questions and answers (5 minutes)

6. Practice task test (10 minutes, 15 seconds)

7. Read narrative and complete quiz on the narrative (25 minutes)

8. Review UML diagrams and complete questions (35 minutes, 20 seconds)

You have a one-in-three chance of receiving \$50 based on your performance in this exercise.

## 2. Pre-Experiment Questionnaire (1 minute)

o Have you ever learned UML (Unified Modeling Language)? Yes/No o Compared to a professional object oriented designer, I would rate my level of experience in interpreting UML diagrams (including Class, Use Case, and State Transition diagrams) as: (7-point scale from very low to very high).

o Compared to someone who works in an employee contracting organization, I would rate my level of knowledge of activities in employee contracting business (such as screening and hiring applicants, contracting with firms, and managing client requests) as: (7-point scale from very low to very high).

## 3. UML Tutorial (12 minutes):

Page 1 (30 seconds):

UML (or “Unified Modeling Language”) is a diagramming method that can be used to represent objects, attributes, events, states, and processes in organizations. The following pages describe the syntax used in three types of UML diagrams and include questions to test your understanding.

Page 2 (3 minutes):

Class Diagram

<table><tr><td>Student</td></tr><tr><td>-GPA-Student number</td></tr><tr><td>+Enrol()+Borrow book()</td></tr></table>

![](/api/attachments/WZPNHRD8/fulltext/images/c46e730c125a4bd34a20344edefce4eb41c6957ce13c727f75cd0fee1ecbe97f.jpg)

In most organizations, there are many phenomena. For example, your university has over 30,000 students, many employees, lots of books, etc. Often, sets of phenomena have similar characteristics. We use a class diagram to show these common characteristics.

The figures above are called “classes.” They represent a class of objects. For example, the figures above show three classes of objects at a university: students, employees, and books. These figures imply that the university has many students, many employees, and many books but that each class of objects has some common characteristics.

The class symbol has three rows:

\- The first row lists the name of the class, e.g., “student” and “book.”

The second row lists the attributes of the class. For example, students have a GPA and a student number, and books have a title, author, and library code.

The third row lists the operations of the class. Operations are what members of the class “do.” Note that some objects have operations but others do not. For example, students enroll in courses and borrow books, but books do not “do” anything by themselves.

From the information in the diagrams above, please answer the following questions:

Question 1: Does a university have more than one student? (Yes, No, Not enough information in the diagram)

Question 2: Do books have a title? (Yes, No, Not enough information in the diagram)

Note that certain things in a domain could be members of more than one class. A common example of this occurs when people have different “roles” in a domain. For example, in a university, it is quite possible that one person could have several roles at the same time, such as being a student and an employee. The particular classes shown in a diagram reflect the classes (and roles) that were deemed important from the perspective of the person who drew the diagram.

Question 3: Could some students in the university potentially be employees? (Yes, No, Not enough information in the diagram)

Page 3 (3.5 minutes):

Classes can be linked by lines called “associations.” Associations have two parts:

![](/api/attachments/WZPNHRD8/fulltext/images/bf3139b66a46a2767e7ea79d810bfd6a6697703698106d2c0311acc63c6271ae.jpg)

a name that describes the association. For example, students can borrow books and enroll in courses.

\- “multiplicity,” which are numbers that explain how classes interact.

Multiplicity is shown by two numbers. The two numbers state the minimum and maximum number of objects that can participate in an association. For example, in this diagram, 0..5 means a students can borrow 0 to 5 books at a time.

Question 4: Can a student borrow 6 books at a time? (Yes, No, Not enough information in the diagram)

In this diagram, the student-course association is linked by two 1..\* associations. The \* [star] symbol means “many.” For example, 1..\* means 1 to many. We use this type of multiplicity when either:

\- there is no specific maximum number, or

we know the maximum number is greater than 1 but we don’t know exactly what it is.

Question 5: Can a student enroll in many courses? (Yes, No, Not enough information in the diagram)

Question 6: Can a student enroll in 5000 courses? (Yes, No, Not enough information in the diagram)

To read multiplicity, look at a class, consider one member of this class, then consider the association, and then look at the numbers closest to the “other” class. For example:

\- One student can borrow from 0 to 5 books at a time

\- One book can be borrowed by 0 to 1 students at a time

\- One student can enroll in 1 to many courses at a time

\- One course can have 1 to many students at a time

Question 7: Can a student enroll in no courses? (Yes, No, Not enough information in the diagram)

Page 4 (1.5 minutes):

![](/api/attachments/WZPNHRD8/fulltext/images/85c6e20df3661a86ceac0a2861402a1713c27314f6a76d818120b206ae6a87bb.jpg)

A “part of” relationship is shown as a line with a black diamond on the end. It indicates that a member of one class is part of a member of another class.

For example, this diagram shows that courses are part of degrees. As a result, students complete “credit hours” in each course, which eventually add up to the “total credit hours” required for the degree. The multiplicity on this diagram says that each course is part of one degree and that each degree can have many courses.

Question 8: Does a degree consist of many courses? (Yes, No, Not enough information in the diagram)

Question 9: Can a course be part of many degrees? (Yes, No, Not enough information in the diagram)

Page 5 (1.5 minutes):

Use Case Diagram

![](/api/attachments/WZPNHRD8/fulltext/images/a785eaa585e10013751100401a57d40607e6bac593fc3b86b73269103cd9b08a.jpg)

A use case diagram contains three parts:

1. The name of the work system, e.g., “course management system.” A work system is a business function, not a computer system.

2. The use cases. These are shown in ovals and describe activities performed in the work system, such as registering for courses and submitting grades.

3. Actors that participate in use cases. This diagram shows that students and professors both participate in registering for courses, but only professors participate in submitting grades.

Question 10: Are students involved in submitting grades? (Yes, No, Not enough information in the diagram)

Page 6 (2 minutes):

![](/api/attachments/WZPNHRD8/fulltext/images/8ba842fdf604f351b9fb72e0324cb9d27fa4b77cae4c3aa62e8ed9eab7d01ec6.jpg)

A statechart contains three parts:

1. The name of the object. For example, this diagram shows the states of a student.

2. The states of the object. For example, students can be undergraduates, graduates, or postgraduates. A dark circle is used to show the “starting state.”

3. The events that determine when an object moves from one state to another. For example, students must complete their degrees to become graduates.

Question 11: Can a student become a postgraduate without being admitted to the postgraduate program? (Yes, No, Not enough information in the diagram)

## 4. ICI Diagram Quiz (20 minutes):

Shown below are three UML diagrams of a company called IT Contracting Inc (ICI). To test your understanding of UML, please answer the following 18 questions. [All 18 questions used the same answer format: Yes/No/Not sure/There is not enough information to know].

## Page 1: Questions (12 minutes):

## Use Case Diagram

1. Do clients interact with ICI?

2. Are jobs matched to services and applicants at ICI?

3. Are interviews scheduled and managed at ICI?

4. Does the Use Case diagram explicitly distinguish between actors who are employees of ICI and other actors?

5. Does ICI appear to deal with investors?

## Class Diagram

6. Are there more than 10 classes on the class diagram of ICI?

7. Does the Class diagram explicitly distinguish between actors who are external to ICI and other actors?

8. On the Class diagram of ICI, some classes reflect people while other classes reflect records. Is the difference between them that records contain no operations (i.e., they don’t “do” anything by themselves)?

9. Does each record of a client reflect the state of one and only one client?

10. Are contracts at ICI maintained by many managers?

11. Can ICI’s record of clients be updated by one and only one clerk?

12. Can an applicant record be related to many interview records?

13. Is ICI’s record of client contracts maintained by the manager?

## Statechart

14. Are there more than 5 states of the statechart?

15. Does the statechart reflect the states of a client?

16. Does the transition from “In Market” to “Prospective” depend on the clerk recording the application?

17. Is there an explicit start-state on the statechart?

18. Does the move from the “on-call” state back to the “prospective” state depend in some way on the client?

## Page 2: Answers (8 minutes):

The answers to the questions you just answered are shown below. Please review the answers to the questions to test your understanding of the UML diagrams.

## Use Case Diagram

1. Do clients interact with ICI? Yes

2. Are jobs matched to services and applicants at ICI? Yes

3. Are interviews scheduled and managed at ICI? Yes

4. Does the Use Case diagram explicitly distinguish between actors who are employees of ICI and other actors? No

5. Does ICI appear to deal with investors? No

## Class Diagram

6. Are there more than 10 classes on the class diagram of ICI? Yes

7. Does the Class diagram explicitly distinguish between actors who are external to ICI and other actors? Yes

8. On the Class diagram of ICI, some classes reflect people while other classes reflect records. Is the difference between them that records contain no operations (i.e., they don’t “do” anything by themselves)? Yes

9. Does each record of a client reflect the state of one and only one client? Yes

10. Are contracts at ICI maintained by many managers? No

11. Can ICI’s record of clients be updated by one and only one clerk? No

12. Can an applicant record be related to many interview records? Yes

13. Is ICI’s record of client contracts maintained by the manager? Yes

## Statechart

14. Are there more than 5 states of the statechart? Yes

15. Does the statechart reflect the states of a client? No

16. Does the transition from “In Market” to “Prospective” depend on the clerk recording the application? Yes

17. Is there an explicit start-state on the statechart? Yes

18. Does the move from the “on-call” state back to the “prospective” state depend in some way on the client? Yes

If you finish this task with time remaining, please continue to review all three UML diagrams shown below.

Higher Quality Decomposition

IT Contracting Inc. (ICI) Use Case Diagram  
![](/api/attachments/WZPNHRD8/fulltext/images/55632b6dfc32fbee8b34fa3f9aa8e7f7204487412c4ace4620d8fc62e7016153.jpg)

<table><tr><td colspan="101">IT Contracting Inc. (ICI)Class Diagram</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="100">Assess applicant</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..0</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..1</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..2</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..3</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..4</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..5</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..6</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..7</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..8</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..9</td><td>1..10</td><td>1..10</td><td>1..10</td><td>1..10</td><td>1..10</td><td>1..10</td><td>1..10</td><td>1..10</td><td>1..10</td><td>1..10</td><td>1..10</td><td>1..10</td><td>1..10</td><td>1..10</td><td>1..10</td><td>1..10</td><td>1..10</td><td>1..10</td><td>1..10</td><td>1..10</td><td>1..11</td><td>1..11</td><td>1..11</td><td>1..11</td><td>1..11</td><td>1..11</td><td>1..11</td><td>1..11</td><td>1..11</td><td>1..11</td><td>1..11</td><td>1..11</td><td>1..11</td><td>1..11</td><td>1..11</td><td>1..11</td><td>1..11</td><td>1..11</td><td>1..11</td><td>1..11</td><td>1..12</td><td>1..12</td><td>1..12</td><td>1..12</td><td>1..12</td><td>1..12</td><td>1..12</td><td>1..12</td><td>1..12</td><td>1..12</td><td>1..12</td><td>1..12</td><td>1..12</td><td>1..12</td><td>1..12</td><td>1..12</td><td>1..12</td><td>1..12</td><td>1..12</td><td>1..12</td><td>1..13</td><td>1..13</td><td>1..13</td><td>1..13</td><td>1..13</td><td>1..13</td><td>1..13</td><td>1..13</td><td>1..13</td><td>1..13</td><td>1..13</td><td>1..13</td><td>1..13</td><td>1..13</td><td>1..13</td><td>1..13</td><td>1..13</td><td>1..13</td><td>1..13</td><td>1..13</td><td>1..14</td><td>1..14</td><td>1..14</td><td>1..14</td><td>1..14</td><td>1..14</td><td>1..14</td><td>1..14</td><td>1..14</td><td>1..14</td><td>1..14</td><td>1..14</td><td>1..14</td><td>1..14</td><td>1..14</td><td>1..14</td><td>1..14</td><td>1..14</td><td>1..14</td><td>1..14</td><td>1..15</td><td>1..15</td><td>1..15</td><td>1..15</td><td>1..15</td><td>1..15</td><td>1..15</td><td>1..15</td><td>1..15</td><td>1..15</td><td>1..15</td><td>1..15</td><td>1..15</td><td>1..15</td><td>1..15</td><td>1..15</td><td>1..15</td><td>1..15</td><td>1..15</td><td>1..15</td><td>1..16</td><td>1..16</td><td>1..16</td><td>1..16</td><td>1..16</td><td>1..16</td><td>1..16</td><td>1..16</td><td>1..16</td><td>1..16</td><td>1..16</td><td>1..16</td><td>1..16</td><td>1..16</td><td>1..16</td><td>1..16</td><td>1..16</td><td>1..16</td><td>1..16</td><td>1..16</td><td>1..17</td><td>1..17</td><td>1..17</td><td>1..17</td><td>1..17</td><td>1..17</td><td>1..17</td><td>1..17</td><td>1..17</td><td>1..17</td><td>1..17</td><td>1..17</td><td>1..17</td><td>1..17</td><td>1..17</td><td>1..17</td><td>1..17</td><td>1..17</td><td>1..17</td><td>1..17</td><td>1..18</td><td>1..18</td><td>1..18</td><td>1..18</td><td>1..18</td><td>1..18</td><td>1..18</td><td>1..18</td><td>1..18</td><td>1..18</td><td>1..18</td><td>1..18</td><td>1..18</td><td>1..18</td><td>1..18</td><td>1..18</td><td>1..18</td><td>1..18</td><td>1..18</td><td>1..18</td><td>1..19</td><td>1..19</td><td>1..19</td><td>1..19</td><td>1..19</td><td>1..19</td><td>1..19</td><td>1..19</td><td>1..19</td><td>1..19</td><td>1..19</td><td>1..19</td><td>1..19</td><td>1..19</td><td>1..19</td><td>1..20</td><td>1..20</td><td>1..20</td><td>1..20</td><td>1..20</td><td>1..20</td><td>1..20</td><td>1..20</td><td>1..20</td><td>1..20</td><td>1..20</td><td>1..20</td><td>1..20</td><td>1..20</td><td>1..20</td><td>1..20</td><td>1..20</td><td>1..20</td><td>1..20</td><td>1..20</td><td>1..21</td><td>1..21</td><td>1..21</td><td>1..21</td><td>1..21</td><td>1..21</td><td>1..21</td><td>1..21</td><td>1..21</td><td>1..21</td><td>1..21</td><td>1..21</td><td>1..21</td><td>1..21</td><td>1..21</td><td>1..21</td><td>1..22</td><td>1..22</td><td>1..22</td><td>1..22</td><td>1..22</td><td>1..22</td><td>1..22</td><td>1..22</td><td>1..22</td><td>1..22</td><td>1..22</td><td>1..22</td><td>1..22</td><td>1..22</td><td>1..22</td><td>1..22</td><td>1..22</td><td>1..22</td><td>1..22</td><td>1..22</td><td>1..23</td><td>1..23</td><td>1..23</td><td>1..23</td><td>1..23</td><td>1..23</td><td>1..23</td><td>1..23</td><td>1..23</td><td>1..23</td><td>1..23</td><td>1..23</td><td>1..23</td><td>1..23</td><td>1..23</td><td>1..23</td><td>1..23</td><td>1..23</td><td>1..23</td><td>1..23</td><td>1..24</td><td>1..24</td><td>1..24</td><td>1..24</td><td>1..24</td><td>1..24</td><td>1..24</td><td>1..24</td><td>1..24</td><td>1..24</td><td>1..24</td><td>1..24</td><td>1..24</td><td>1..24</td><td>1..24</td><td>1..24</td><td>1..24</td><td>1..24</td><td>1..24</td><td>1..24</td><td>1..25</td><td>1..25</td><td>1..25</td><td>1..25</td><td>1..25</td><td>1..25</td><td>1..25</td><td>1..25</td><td>1..25</td><td>1..25</td><td>1..25</td><td>1..25</td><td>1..25</td><td>1..25</td><td>1..25</td><td>1..25</td><td>1..25</td><td>1..25</td><td>1..25</td><td>1..25</td><td>1..26</td><td>1..26</td><td>1..26</td><td>1..26</td><td>1..26</td><td>1..26</td><td>1..26</td><td>1..26</td><td>1..26</td><td>1..26</td><td>1..26</td><td>1..26</td><td>1..26</td><td>1..26</td><td>1..26</td><td>1..26</td><td>1..26</td><td>1..26</td><td>1..26</td><td>1..26</td><td>1..27</td><td>1..27</td><td>1..27</td><td>1..27</td><td>1..27</td><td>1..27</td><td>1..27</td><td>1..27</td><td>1..27</td><td>1..27</td><td>1..27</td><td>1..27</td><td>1..27</td><td>1..27</td><td>1..27</td><td>1..27</td><td>1..27</td><td>1..27</td><td>1..27</td><td>1..27</td><td>1..28</td><td>1..28</td><td>1..28</td><td>1..28</td><td>1..28</td><td>1..28</td><td>1..28</td><td>1..28</td><td>1..28</td><td>1..28</td><td>1..28</td><td>1..28</td><td>1..28</td><td>1..28</td><td>1..28</td><td>1..28</td><td>1..28</td><td>1..28</td><td>1..28</td><td>1..28</td><td>1..29</td><td>1..29</td><td>1..29</td><td>1..29</td><td>1..29</td><td>1..29</td><td>1..29</td><td>1..29</td><td>1..29</td><td>1..29</td><td>1..29</td><td>1..29</td><td>1..29</td><td>1..29</td><td>1..29</td><td>1..30</td><td>1..30</td><td>1..30</td><td>1..30</td><td>1..30</td><td>1..30</td><td>1..30</td><td>1..30</td><td>1..30</td><td>1..30</td><td>1..30</td><td>1..30</td><td>1..30</td><td>1..30</td><td>1..30</td><td>1..30</td><td>1..30</td><td>1..30</td><td>1..30</td><td>1..30</td><td>1..31</td><td>1..31</td><td>1..31</td><td>1..31</td><td>1..31</td><td>1..31</td><td>1..31</td><td>1..31</td><td>1..31</td><td>1..31</td><td>1..31</td><td>1..31</td><td>1..31</td><td>1..32</td><td>1..32</td><td>1..32</td><td>1..32</td><td>1..32</td><td>1..32</td><td>1..32</td><td>1..32</td><td>1..32</td><td>1..32</td><td>1..32</td><td>1..32</td><td>1..32</td><td>1..32</td><td>1..32</td><td>1..32</td><td>1..32</td><td>1..32</td><td>1..32</td><td>1..33</td><td>1..33</td><td>1..33</td><td>1..33</td><td>1..33</td><td>1..33</td><td>1..33</td><td>1..33</td><td>1..33</td><td>1..33</td><td>1..33</td><td>1..33</td><td>1..33</td><td>1..33</td><td>1..33</td><td>1..33</td><td>1..33</td><td>1..33</td><td>1..33</td><td>1..33</td><td>1..34</td><td>1..34</td><td>1..34</td><td>1..34</td><td>1..34</td><td>1..34</td><td>1..34</td><td>1..34</td><td>1..34</td><td>1..34</td><td>1..34</td><td>1..34</td><td>1..34</td><td>1..34</td><td>1..34</td><td>1..34</td><td>1..34</td><td>1..34</td><td>1..34</td><td>1..34</td><td>1..35</td><td>1..35</td><td>1..35</td><td>1..35</td><td>1..35</td><td>1..35</td><td>1..35</td><td>1..35</td><td>1..35</td><td>1..35</td><td>1..35</td><td>1..35</td><td>1..35</td><td>1..35</td><td>1..35</td><td>1..35</td><td>1..35</td><td>1..35</td><td>1..35</td><td>1..35</td><td>1..36</td><td>1..36</td><td>1..36</td><td>1..36</td><td>1..36</td><td>1..36</td><td>1..36</td><td>1..36</td><td>1..36</td><td>1..36</td><td>1..36</td><td>1..36</td><td>1..36</td><td>1..36</td><td>1..36</td><td>1..36</td><td>1..36</td><td>1..36</td><td>1..36</td><td>1..36</td><td>1..37</td><td>1..37</td><td>1..37</td><td>1..37</td><td>1..37</td><td>1..37</td><td>1..37</td><td>1..37</td><td>1..37</td><td>1..37</td><td>1..37</td><td>1..37</td><td>1..37</td><td>1..37</td><td>1..37</td><td>1..37</td><td>1..37</td><td>1..37</td><td>1..37</td><td>1..37</td><td>1..38</td><td>1..38</td><td>1..38</td><td>1..38</td><td>1..38</td><td>1..38</td><td>1..38</td><td>1..38</td><td>1..38</td><td>1..38</td><td>1..38</td><td>1..38</td><td>1..38</td><td>1..38</td><td>1..38</td><td>1..38</td><td>1..38</td><td>1.39</td><td>1.39</td><td>1.39</td><td>1.39</td><td>1.39</td><td>1.39</td><td>1.39</td><td>1.39</td><td>1.39</td><td>1.39</td><td>1.39</td><td>1.39</td><td>1.39</td><td>1.39</td><td>1.39</td><td>1.39</td><td>1.39</td><td>1.39</td><td>1.39</td><td>1.39</td><td>1.38</td><td>1.38</td><td>1.38</td><td>1.38</td><td>1.38</td><td>1.38</td><td>1.38</td><td>1.38</td><td>1.38</td><td>1.38</td><td>1.38</td><td>1.38</td><td>1.38</td><td>1.38</td><td>1.38</td><td>1.38</td><td>1.38</td><td>1.38</td><td>1.38</td><td>1.38</td><td>1.39</td><td>.   |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  | .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  ,  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |
|</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Higsir iir Dion

![](/api/attachments/WZPNHRD8/fulltext/images/2413b86759ce131e1c10a0d086a84a25cb5a44daf771466a3ba222339c0b0d3f.jpg)  
thecc   aa l lass Re atug asttus, atg attug Sta  a lant

![](/api/attachments/WZPNHRD8/fulltext/images/dc35b0f14d78711cae178f300c9ee97f6ca37b48aa2e21902f0d12c7df544e60.jpg)

IT Contracting Inc. (ICI) Use Case Diagram

Lower Quality Decomposition

Receive and update applications, schedule and manage interviews, develop and manage job requests, monitor business performance, match jobs to services and applicants, receive and update client details and job requests, and develop and manage job contracts

Clas Dam

<table><tr><td rowspan="5"></td><td colspan="101">Related to</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="100">0..*</td><td colspan="96">0..*</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="100">ICI record of job matches</td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td></tr><tr><td colspan="100">Machine used for records</td></tr><tr><td colspan="100">Service(s) matched</td><td>0.0*0.0*0.0*0.0*0.0*0.0*0.0*0.0*0.0*0.0*0.0*0.0*0.0*0.0*0.0*0.0*0.0*0.0*0.0*0.0*0.0*0.0*0.0*0.0*0.0*0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%-0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%(0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%
-0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%,0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%;0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%.0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0 %0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0%0.0</td><td>ICI record of job requests</td><td>ICI record of interviews</td><td>ICI record of client contracts</td><td>ICI record of job receipts</td><td>ICI record of job receipts</td><td>ICI record of client contracts</td><td>ICI record of client contracts</td><td>ICI record</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td rowspan="3">Clerk [Record application]</td><td rowspan="2">Prospective</td><td>Client message</td><td>On call</td><td>Pre-selected</td><td>Selected</td><td>Contracted</td></tr><tr><td>Manager [Matching done]</td><td>Manager [Interview done]</td><td>Manager [Interview done]</td><td>Manager [Interview done]</td><td>Manager [Contract updated]</td></tr><tr><td>In market</td><td></td><td></td><td></td><td></td><td>Lower Quality Decomposition</td></tr></table>

## 5. Example Tasks (5 minutes):

## Page 1 (30 seconds):

In a later exercise, you will need to review UML diagrams and answer questions about them. There are two types of questions. On the next two pages, we will show you examples of these types of questions and the types of answers you will need to give.

## Page 2 (30 seconds):

Example Comprehension Question:

Question: What is the maximum number of departments that an employee can work for?

![](/api/attachments/WZPNHRD8/fulltext/images/ddf988014cdd0f7c84cfb8bb29120962b81f6cfe809e14a217398a52418011ed.jpg)  
Answer: 1 (because the association is 0..1)

## Page 3 (4 minutes):

## Example Problem-Solving Question:

Question: A professor is especially popular with students writing theses. Why might he/she be so popular? From the information in the model, give as many reasons as you can and explain each o your reasons.

![](/api/attachments/WZPNHRD8/fulltext/images/5c6477bfd9670324da4ab8a1c223550496b1fe41e9e7714d6f611e9d646eb55e.jpg)

## Example Answers

As shown on the figure above, you come up with answers by making inferences based on the information in the diagram combined with your own background knowledge. This is the style of answer that you will need to give in later exercises.

For example, to come up with Answer 1, the person who answered this question looked at two attributes of professors (“research area” and “#publications”) and inferred, based on his/her own knowledge of students, that students might prefer to work for professors who are top researchers. The other answers were created via the same process.

Burton-Jones & Meso/Decomposition Quality and Forms of Information

<table><tr><td>Answer</td><td>Explanation</td></tr><tr><td>1. The professor is a very productive researcher (has many publications)</td><td>Students want to work for a leading professor</td></tr><tr><td>2. Supervises popular thesis topics, due to:A. type of research area</td><td>Students like his/her research area</td></tr><tr><td>B. type of courses taught</td><td>Students like the topics in his/her courses</td></tr><tr><td>3. Is a good reviewer of theses (e.g., makes sure they are good quality)</td><td>Students want to write a good quality thesis</td></tr><tr><td>4. Will provide students with a thesis topic</td><td>Being given a topic by the professor saves time</td></tr><tr><td>5. Student likely to get good grade</td><td>Students want to get good grades</td></tr><tr><td>6. Is a good supervisor of students (e.g., easy to get along with/helpful)</td><td>Students want a nice person to supervise them</td></tr><tr><td>7. Willing to supervise many students</td><td>Students feel more confident in their choice of professor if other students made the same choice</td></tr><tr><td>8. Doesn’t teach too many courses (hence, has more time to supervise)</td><td>Students want to have access to the professor when needed</td></tr></table>

## 6. Practice Tasks (10 minutes 15 seconds):

Page 1 (15 seconds):

Please click the following link to see three UML diagrams: [URL]

Additional (clicked) page: [Available while answering all of the following questions]

Class Diagram

![](/api/attachments/WZPNHRD8/fulltext/images/23a86d2e59de3ac376510326ddb0ceab0cfadf9eb3fd274bddbbddf3c3f24104.jpg)

## Use Case Diagram

![](/api/attachments/WZPNHRD8/fulltext/images/406d35eaba82cbe0b8e8fa6863919ded2fd3e2ec034ebee4f02256b6de401ffd.jpg)

State Transition Diagram  
![](/api/attachments/WZPNHRD8/fulltext/images/1895e27fc5ee2c7b46545e8043dd5f0fd1edc00daed38ce74371251aad746299.jpg)

## Page 2 (4 minutes):

## Comprehension questions:

1. Do borrowers and clerks both deal with fines? (Yes, No, Not enough information in the diagram)

2. Must a book be on the shelf before it is borrowed? (Yes, No, Not enough information in the diagram)

diagram)

4. Can postgraduates borrow more than 4 journals at a time? (Yes, No, Not enough information in the diagram)

5. Are clerks involved in sourcing new books? (Yes, No, Not enough information in the diagram)

6. Is there an explicit time limit on returning books? (Yes, No, Not enough information in the diagram)

## Page 3 (1 minute):

## The answers to the comprehension questions are shown below:

1. Do borrowers and clerks both deal with fines? Yes

2. Must a book be on the shelf before it is borrowed? Yes

3. Can an undergraduate student borrow a research journal? No

4. Can postgraduates borrow more than 4 journals at a time? Not enough information in the diagram

5. Are clerks involved in sourcing new books? No

6. Is there an explicit time limit on returning books? No

## Page 4 (4 minutes):

## Problem-solving questions

1. Undergraduate students at the university have complained that they are not able to borrow all the materials they need for their work. From the information in the models, list up to three reasons why this might be the case.

2. The librarian wants to find a way to improve the number of books available to students. From the information in the models, list up to two ways the librarian might consider doing this.

## Page 5 (1 minute):

Some possible answers to the problem-solving questions are shown below.

1. Undergraduate students at the university have complained that they are not able to borrow all the materials they need for their work. From the information in the models, list up to three reasons why this might be the case. Undergraduate students might need to borrow journals, but cannot do so. Students might not have been returning books on time, hence are not available when needed The number of books in the collections may be too small for some or all of the student majors

2. The librarian wants to find a way to improve the number of books available to students. From the information in the models, list up to two ways the librarian might consider doing this. Students could be involved in sourcing books, e.g., by suggesting topics/books they need. The librarian could use the number of students in each major to determine the number of books to keep in each collection.

## 7a. Narrative & Quiz (25 minutes) [For the multiple forms of information group]:

This page contains two sets of questions:

1. For the first set of questions, please answer them based on your own prior knowledge. If you don’t know the answers, please select “don’t know.”

2. For the second set of questions, please read the narrative that follows the questions to obtain the answers.

If you finish all questions within the time allowed, please continue to read the narrative carefully.

## Questions about IS development

1. What was the main motivation behind the development of the software development life-cycle: a. Recognition that information systems have social as well as productivity effects b. Time and cost overruns in systems development c. Not understanding user requirements d. User resistance to systems development e. Don’t know.

2. Users are aggressively resisting the implementation of a new system. In response, the company asks several users to join the project team so that their concerns can be addressed in the implementation process. Which of the following approaches is the organization most likely using: a. Systems development lifecycle b. Political approach c. Socio-technical design d. Soft systems e. Don’t know.

3. In a prototype methodology, developers build prototypes to help users understand their requirements. This is most likely an extension of the following approach: a. Soft systems b. Systems development lifecycle c. Political approach d. Not clear (could be more than one approach) e. Don’t know.

4. An organization has decided to cut costs. Employees need to work long hours and the company has reduced spending on IT systems. The systems are very effective but users find that they are dull and frustrating to use. The organization is least likely to be using the following approach: a. Political approach b. Systems development lifecycle c. Soft systems d. Socio-technical design e. Don’t know.

5. When would the political approach be most applicable: a. When the new system would dramatically alter the power structure in the organizations b. When the system is being implemented in government c. When a detailed project management plan is not feasible d. When workers have very low morale e. Don’t know.

6. What is a central concern in the software development life-cycle methodology: a. Agility b. Project management c. Ethics d. Quality of life e. Don’t know.

7. What type of organizations are most likely to adopt socio-technical design principles: a. Start-up businesses b. Large bureaucracies c. Organizations with a sole mission of maximizing profits d. Organizations that want their employees to have a good work-life balance e. Don’t know.

8. If the soft-systems approach and socio-technical approach were combined, an example activity that might occur during systems development is: a. Meetings with users and designers to understand users’ work-life balance issues b. Meetings with managers to convince them of the importance of the project c. Meeting with users to convince them of the importance of the project d. Designing a detailed project management plan e. Don’t know.

9. Which of the following approaches to systems development are feasible in practice: a. The systems development life-cycle approach b. The systems development life-cycle combined with the socio-technical approach c. The systems development life-cycle combined with the political approach d. Any of the above (a, b, or c) e. Don’t know.

10. When would the socio-technical approach be most applicable: a. When management want to improve the business as well as employees’ quality of life b. When a detailed project management plan is feasible c. When the system is being implemented in charity d. When workers have very high morale e. Don’t know.

11. What type of educational background would be most suitable for socio-technical designers: a. Political science and psychology b. Political science only c. Business, computer science, and psychology d. Computer science and business e. Don’t know.

## Questions about ICI

1. How does ICI make money? a. Selling computer equipment b. Receiving sales commissions c. Obtaining payments for contract work d. Performing IT services over the web e. Don’t know.

2. When do applicants become employees at ICI? a. When ICI determines that the applicant has in-demand skills b. When a client requests an applicant and the manager activates the contract c. When the applicant performs well in the sample interview d. When the client employs the applicant e. Don’t know.

3. How are contracts developed at ICI: a. Two contracts are created – one for the applicant and one for the clien b. Applicants are contacted directly to the client c. ICI does not develop any contracts d. Applicants have one contract and it is updated for each job that they do e. Don’t know.

4. How does ICI interview applicants for jobs? a. The client first interviews the applicant. The applicant then interviews with ICI. b. Applicants first perform a sample interview. Those who do well have a client interview. c. The clerk interviews applicants and then contracts with the applicant and the client. d. ICI doesn’t use interviews. e. Don’t know.

5. How does ICI keep track of changes in its market: a. By conversing with managers at other similar firms in its industry b. By conducting web-based research on trends in the market c. By obtaining estimates of the applicant and client market d. All of the above e. Don’t know.

6. How are applicants matched to jobs: a. Clients choose applicants from a list available to them b. Applicants choose jobs from a list available to them c. The manager matches applicants to jobs based on their skills and availability d. ICI clerks match applicants to jobs on a first-come first-served basis e. Don’t know.

7. How do clients request jobs: a. ICI clerks contact clients on a daily basis to obtain new job requests b. Client companies send job requests to ICI by phone/mail c. The manager contacts clients each month to obtain their latest job requests d. Clients send their requests directly to applicants e. Don’t know.

8. What is the relationship between services and jobs at ICI: a. Services are pre-defined types of work that ICI can perform. Jobs are the work that clients need done (which may involve no pre-defined services or several of them). b. Services are jobs performed for clients c. Services are jobs performed internally at ICI d. The distinction between jobs and services is based on the length of difficulty and duration of the required work. Longer, more difficult jobs are called “services.” e. Don’t know.

9. What does the manager focus on to increase business performance: a. Improving clerk motivation via salary adjustments b. Improving the matching process, applicant performance, and client satisfaction c. Increasing the number of meetings with clients to understand their requirements d. Increasing the size of the applicant market e. Don’t know.

10. What will the manager likely do if there have been many unfulfilled job requests:

a. Meet with clients to understand their needs

b. Meet with clerks to improve the matching process

c. Change the charge out rate for services and improve advertising

d. Change the contracting approach so that it is more efficient

e. Don’t know.

## 11. How does ICI attract applicants?

a. ICI uses advertising to attract applicants who have skills required for in-demand services

b. ICI relies on word-of-mouth advertising between applicants

c. ICI relies on clients locating good applicants that can serve their needs

d. ICI relies on on-line recruitment websites to attract potential applicants

e. Don’t know.

NB: If you finish these questions and have time remaining, please continue to read the narrative.

## Narrative:

IT Contracting Inc (ICI) is a rapidly expanding business that contracts IT personnel to organizations in Houston (TX). ICI receives about 10 new applications each week from prospective contractors. Each application includes the applicant’s resume, which outlines his/her skills. ICI clerks record all the details of new applicants. ICI currently has 300 applicants on file and the clerk updates them every six months for changes to applicants’ skills and level of certification.

ICI clerks are responsible for recording the status of applicants and jobs. Clerks record applicants’ status as Prospective when they receive their applications. If the manager matches them to a job, they are moved to the On Call state. If they perform to a high quality in the sample interview, the manager updates the interview record accordingly and they are moved to a Pre-Selected state. If a client notifies ICI that they want the applicant, the manager updates the interview record accordingly and the applicant is moved to the Selected state. Once the contracts have been signed, the manager updates the contract records to indicate that the contract is active. At this point, the applicant becomes Contracted. The applicant remains in this state until the contract is complete and the manager updates the contract record to indicate that the contract has ended.

Client companies send their job requests to ICI by phone or mail. For each job request, the details of the job are recorded, including the date requested, duration, and level of difficulty. Clerks make updates to client details and job request details when required (e.g., to update whether the job has been fulfilled and to indicate the client’s satisfaction with a job once completed).

Client requests may relate to one or more services offered by ICI. Services are pre-defined types of work that ICI can perform (e.g., in operating systems, systems analysis, or systems design). New services are added by ICI’s manager. For each service, the manager keeps a record of its level of demand, charge-out rate per hour, and the number of advertisements paid for in that month. The level of demand for each service is determined by counting the number of requests for related jobs received in the last month.

Once a day, ICI’s manager matches clients’ requests to ICI’s list of services based on the availability of applicants with relevant skills. The manager reviews the matches and based on her knowledge of applicants’ skills and past performance, she selects applicants for potential interviews. Two rounds of interviews are required. To ensure the client meets quality applicants, the manager first prepares a sample interview. Applicants who perform to the highest quality in the sample interview are asked to remain “on call” until the client interview is scheduled. After the client interview, the client notifies ICI of the result (accept/reject).

Once an applicant has been requested by a client, the manager draws up two sets of contracts. A contract between ICI and the client is developed. Client contracts describe the total charge the client will pay for the work and any discounts that apply (e.g., because multiple contractors are placed on the contract or because the contractors are engaged for a long period). A contract is also developed between ICI and the Applicant to stipulate the applicant’s salary and union representative when working on the job. The applicant is an employee of ICI for the duration of the contract. For each new contract, the manager records the start and end dates. Applicants and clients are under contract from the contracts’ start dates.

To improve its ability to match applicants and jobs, ICI keeps information on the level of demand for each service it offers and whether it has applicants with the required skills. On a monthly basis, the manager monitors the demand for each service. She also examines whether there were any instances where three or more client requests were not fulfilled because of unavailability of skilled applicants. The manager uses this information to consider adjusting services, e.g., changing the hourly charge-out rate for services that are in demand or advertising for skills that ICI requires in greater number.

The number of unfulfilled requests in a month is one of ICI’s key performance indicators. The manager also reviews two other key performance indicators: applicant performance and client satisfaction. Applicants’ performance is rated for each job and their average performance is reviewed at the end of the month. Likewise, clients’ satisfaction is reviewed at the end of each job and their average satisfaction is reviewed at the end of the month.

Like all businesses, ICI must continue to survive and improve in a changing environment. To help it do this, ICI obtains market estimates regarding its potential clients (e.g., the potential number of clients and the potential number of jobs) and applicants (e.g., the potential number of applicants and average level of skills). The manager uses this information to assess its share of the contracting market in Houston and to adjust its business practices (e.g., charge-out rates, matching procedures, and contract discounts) to meet the opportunities and constraints in the market.

## 7b. Narrative & Quiz (25 Minutes) [For the single form of information group]:

This page contains two sets of questions:

1. For the first set of questions, please answer them based on your own prior knowledge. If you don’t know the answers, please select “don’t know.”

2. For the second set of questions, please read the narrative that follows the questions to obtain the answers.

If you finish all questions within the time allowed, please continue to read the narrative carefully.

## Questions about ICI

For this section, we used the same questions and answers as used for the multiple forms of information group (above). The only difference was that students did not have access to the narrative.

## Questions about IS development

For this section, we used the same questions and answers as used for the multiple forms of information group (above). The only difference was that students had access to the narrative below.

## Narrative:

## Systems Development Life-Cycle Approach

Traditionally, systems development personnel have thought about the systems development process in terms of a lifecycle comprising various major phases. The life-cycle approach arose from early efforts to apply project management techniques to the systems development process. Historically, major systems were characterized by massive cost overruns, inadequate economic evaluations, inadequate system design, management abdication, poor communications, inadequate direction, and so on. The life-cycle approach was developed to help overcome some of these problems. By clearly defining tasks in terms of the life cycle, project management techniques can be applied. To develop high-quality systems, each phase of the life cycle should be planned and controlled, comply with developed standards, be adequately documented, be staffed by competent personnel, have project checkpoints and signoffs, and so on.

There are many forms of the systems development life cycle. A typical version comprises the following eight phases: feasibility study, information analysis, system design, program development, procedures and forms development, acceptance testing, conversion, and operation and maintenance. The life-cycle approach does not imply that all these phases must be carried out serially. Some can proceed concurrently. Moreover, some phases might require several iterations. The general notion, however, is that phases “cascade” into new phases—hence, the life-cycle approach is sometimes called the “waterfall model” of systems development.

## Sociotechnical Design Approach

After substantial experience with the life-cycle approach to systems development, researchers and practitioners recognized that it was not a panacea for the problems encountered during the design and implementation of information systems. In particular, severe behavioral problems sometimes arose when the life-cycle approach was used. Users might show apathy or outright resistance to a proposed system, or they might even attempt to sabotage the system.

In the mid-late 1970’s, a new approach emerged that focused on these behavioral problems. This approach, called the sociotechnical design approach, seeks to optimize two systems jointly: (a) the technical system, in which the objective is to maximize task accomplishment; and (b) the social system, in which the objective is to maximize the quality of working life of system users.

Like the life-cycle approach, the sociotechnical design approach has several major phases: diagnosis and entry, management of the change process, system design, adjustment of coordinating mechanisms, and implementation. Note that these phases do not negate the importance of the traditional life-cycle model. Project management techniques and a systematic approach to design are still critical. The sociotechnical design approach, however, forced designers to take a broader and richer view of the development process.

## Political Approach

Early versions of sociotechnical design emphasized the importance of involving users in systems development to produce high-quality design of the social system and to reduce behavioral problems that arise during implementation. As experience with the approach was gained, it became clear that user involvement might be problematical. In some cases, users employed their opportunities to be involved with systems development to undermine progress.

In the late 1970s and early 1980s, the political approach to systems development emerged to try to explain why user involvement was not always an appropriate strategy. It identified the need for designers to take into account the ways in which information systems could change the distribution of power within organizations.

When the political approach to systems development is adopted, a critical task is to study the history of the organization. The designer can then evaluate whether the desired system will necessitate changes to the existing power structure. If the proposed system will leave the power structure intact, user participation in the design process is important. If the system will change the power structure, user participation must be replaced with negotiation between designers and users where compromise is an accepted outcome. Designers must seek out resistance early, build personal rapport, co-opt users from the start, and attempt face-to-face negotiations.

## Soft-Systems Approach

An important tenet underlying traditional approaches to systems development is that users understood and could articulate their systems requirements. Indeed, users were often denigrated by information systems professionals if they could not communicate their needs.

In the mid to late 1970s, however, researchers in the UK developed an approach that was designed to assist decision makers to understand ill-structured problems. They called their approach “soft systems methodology” (SSM).

SSM involves seven steps: (1) recognize the problem situation; (2) express the problem situation; (3) produce “root definitions” of relevant systems; (4) develop conceptual models of relevant systems; (5) compare conceptual models with the perceived problem situation, (6) identify desirable and feasible changes, (7) take action to improve the situation.

SSM initially was not developed to address systems development needs. Rather, its focus was illstructured problems in general. In the early 1980’s, however, some of its proponents recognized that it could assist users to articulate their information system requirements in situations in which substantial uncertainty surrounded the system to be developed. Accordingly, they adapted existing information systems development approaches to incorporate SSM procedures. These efforts were perhaps the first to recognize formally that uncertainty was an intrinsic part of many information systems development situations and that developers and users needed tools to help resolve the problems that arose when uncertainty existed.

Source: Weber, R. Information Systems Audit and Control, Prentice Hall, 1999.

## 8. Dependent measures (35 minutes, 20 seconds)

Page 1 (2 minutes):

In this section, you will be asked questions about IT Contracting Inc (ICI). When the time expires for each question, the system will save your work and move you on to the next question.

• Please click on the following URL to see three UML diagrams of ICI: zzz.html.

o This link was available for all students, linking to different diagrams depending on the group.

• Please click on the following URL to see the narrative of ICI: zzz.html.

o This link was only available for students in the multiple forms of information group.

In two minutes, you will start receiving questions about ICI. If you have time before the questions begin, please familiarize yourself with ICI’s business based on the information you have received.

[Although the comprehension questions are shown first below, students received questions in either order (comprehension questions first or problem-solving questions first) via random assignment.]

Page 2 (7 minutes):

Please answer the following questions about ICI based on the information you have received about ICI’s business:

## Comprehension questions (with answers highlighted):

Questions addressing violations in losslessness:

1. Is the # potential clients in the market an important attribute at ICI? (Yes/No/Not sure/There is not enough information to know)

2. Is clients’ average level of satisfaction with jobs an important attribute at ICI? (Yes/No/ Not sure/ There is not enough information to know)

Questions addressing violations in minimality:

3. Is “insurance number” a relevant attribute of ICI’s clerks? (Yes/No/ Not sure/ There is not enough information to know)

4. Is “# children” a relevant attribute of the manager at ICI? (Yes/No/ Not sure/ There is not enough information to know)

Questions addressing violations in determinism:

5. Does an applicant’s move from the “On Call” state back to the “Prospective” state depend on what has happened to a job? (Yes/No/ Not sure/ There is not enough information to know)

6. Is the event that leads an applicant from “On Call” to “Pre-selected” the same as the event that leads an applicant from “Pre-selected” to “Selected”? (Yes/No/ Not sure/ There is not enough information to know)

Questions addressing violations in cohesion:

7. Does the manager have several roles at ICI (where a role involves several duties)? (Yes/No/ Not sure/ There is not enough information to know)

8. Does any activity in ICI’s business require the involvement of all four parties (applicant, clerk, client, and manager)? (Yes/No/ Not sure/ There is not enough information to know) Questions addressing violations in coupling:

9. Is the manager involved in updating applications? (Yes/No/ Not sure/ There is not enough information to know)

10. Does the manager explicitly request ICI clerks to code applications? (Yes/No/ Not sure/ There is not enough information to know)

Page 3 (0.5 minutes):

To answer the previous 10 comprehension questions:

\- to what extent did you rely on the information in the diagrams?

to what extent did you rely on the information in the narrative?

Both questions used a 5-point Likert scale from “Not at all” to “A great extent.”

Page 4 (3 min, 30 seconds):

Problem-Solving Question 1 (with suggested answers):

1. ICI is concerned that the manager has too many duties. To address this issue, ICI wants to create a new “coordinator” role. The coordinator would be more junior than the manager but more senior than the clerk. Based on your understanding of ICI’s business, list up to five duties that you think could be delegated from the manager to the coordinator and explain why it would be useful to do so.

Page 5 (3 min, 30 seconds):

<table><tr><td>Duties delegated from manager to coordinator</td><td>Why useful to do so?</td></tr><tr><td>Adding new services</td><td>Decision to add is a managerial task, but adding it is an administrative task.</td></tr><tr><td>Calculating the demand for each service</td><td>Administrative, fairly easy to automate</td></tr><tr><td>Matching job requests to services and applicants</td><td>Simple task, fairly easy to automate</td></tr><tr><td>Administering/scheduling the interviews</td><td>Simple task, much of it could be automated</td></tr><tr><td>Updating interview records</td><td>Clerical task, it could be delegated entirely</td></tr><tr><td>Drawing up the contracts</td><td>Administrative task, much of it could be delegated</td></tr><tr><td>Collecting information (e.g., % fulfillment of job requests or market estimates) for the manager to assess</td><td>Administrative task, manager should focus on analysis rather than information gathering</td></tr><tr><td>Other if reasonable (1 or 1⁄2 point per answer)</td><td></td></tr></table>

Problem-Solving Question 2 (with suggested answers):

2. ICI’s manager is increasingly concerned about ICI’s business performance. What trends might she be concerned about? Based on your understanding of ICI’s business, list up to six trends and explain why each trend would be important.

Burton-Jones & Meso/Decomposition Quality and Forms of Information

<table><tr><td>Trend</td><td>Why important</td></tr><tr><td>Clients are demanding more discounts</td><td>Profit margin will reduce</td></tr><tr><td>Applicants are demanding higher salaries</td><td>Profit margin will reduce</td></tr><tr><td>Applicant performance is low or decreasing</td><td>Won&#x27;t be able to service clients</td></tr><tr><td>The number of skilled applicants in the market is reducing</td><td>Won&#x27;t be able to service clients</td></tr><tr><td>Client satisfaction is low or decreasing</td><td>Clients will leave</td></tr><tr><td>The number of unfulfilled client requests is high or increasing</td><td>Clients will leave</td></tr><tr><td>The demand for services is low or decreasing</td><td>Revenue will drop</td></tr><tr><td>The number of clients or jobs in the market is reducing</td><td>Revenue will drop</td></tr><tr><td>Clients are submitting fewer job requests</td><td>Revenue will drop</td></tr><tr><td>ICI&#x27;s market share is low or decreasing (or the # competitors is increasing)</td><td>Will have more difficulty attracting good clients and good applicants</td></tr><tr><td>Other if reasonable (1 or 1⁄2 point per answer)</td><td></td></tr></table>

Page 6 (3 min, 30 seconds):

## Problem-Solving Question 3 (with suggested answers):

3. ICI has a number of applicants with skills in high demand but who are not yet contracted with a client. Based on your understanding of ICI’s business, list up to six possible causes for this and explain how each might have led to this situation.

<table><tr><td>Factor</td><td>Explanation</td></tr><tr><td>They did poorly in the sample interview</td><td>Therefore don’t get hired</td></tr><tr><td>They get bad results in the client interview</td><td>Therefore don’t get hired</td></tr><tr><td>Jobs are being cancelled by clients</td><td>They may be demanded but just don’t get contracted/ signed</td></tr><tr><td>Certification is too low</td><td>Therefore not good enough</td></tr><tr><td>Low performance rating</td><td>Therefore not good enough</td></tr><tr><td>The manager is not matching job requests well</td><td>They are good enough but the manager is not</td></tr><tr><td>The manager is not scheduling interviews well</td><td>They are good enough but the manager is not</td></tr><tr><td>The contract terms were not acceptable</td><td>The applicants or clients were not willing to be contracted</td></tr><tr><td>Other if reasonable (1 or 1⁄2 point per answer)</td><td></td></tr></table>

Page 7 (3 min, 30 seconds):  
Problem-Solving Question 4 (with suggested answers):

4. Although ICI’s manager has spent time trying to improve ICI’s business, she has not managed to improve it as much as she had desired. Based on your understanding of ICI’s business, list up to five ways in which ICI’s business may not be as good as the manager desired.

<table><tr><td>Aspect of business at ICI</td><td>Why important</td></tr><tr><td>Applicant performance is not as good as desired</td><td>Won’t be able to satisfy clients’ needs</td></tr><tr><td>Client satisfaction is not as good as desired</td><td>Clients less likely to hire ICI again</td></tr><tr><td>Fulfillment of job requests is not as good as desired</td><td>Clients less likely to hire ICI again</td></tr><tr><td>Demand for services is not as good as desired</td><td>Revenue stream is uncertain</td></tr><tr><td>Market share is not as good as desired</td><td>Less revenue, therefore less chance for profits</td></tr><tr><td>Other if reasonable (1 or 1⁄2 point per answer)</td><td></td></tr></table>

Page 8 (3 min, 30 seconds):

## Problem-Solving Question 5 (with suggested answers):

5. ICI has increasingly been unable to fulfill client requests. Based on your understanding of ICI’s business, list up to seven reasons why this could be occurring and explain the basis for your answer.

<table><tr><td>Reason</td><td>Basis for answer</td></tr><tr><td>Applicants have too low performance</td><td>Not getting hired</td></tr><tr><td>Applicants have too low certification</td><td>Not getting hired</td></tr><tr><td>Applicants have too few skills</td><td>Not getting hired</td></tr><tr><td>Too few applicants</td><td>Can’t meet demand</td></tr><tr><td>Interviews too poor quality</td><td>Client not impressed</td></tr><tr><td>Have not tracked changes in in-demand services</td><td>No longer have services that clients want</td></tr><tr><td>Job requests are for too long or too high difficulty</td><td>Unable to provide service</td></tr><tr><td>Too few clerks to manage the volume of requests</td><td>Unable to manage the fulfillment process well</td></tr><tr><td>Manager not monitoring unfulfilled requests per mth</td><td>Poor monitoring led to slippage in providing services</td></tr><tr><td>The client market has increased in size</td><td>There are now more requests to deal with</td></tr><tr><td>Each client has been submitting more requests</td><td>There are now more requests to deal with</td></tr><tr><td>Other if reasonable (1 point or 1⁄2 point per answer)</td><td></td></tr></table>

Page 9 (3 min, 30 seconds):

## Problem-Solving Question 6 (with suggested answers):

6. ICI has been receiving a declining number of client requests over the past year. Based on your understanding of ICI’s business, give up to four likely reasons why and explain your answer for each.

<table><tr><td>Reason</td><td>Explanation</td></tr><tr><td>Clients are not satisfied</td><td>Clients no longer want to put in requests</td></tr><tr><td>Employee performance has been low leading to lower satisfaction</td><td>Clients no longer want to put in requests</td></tr><tr><td>Not meeting in-demand services</td><td>Services no longer relevant to clients</td></tr><tr><td>Services no longer meet client requirements, e.g. duration/difficulty</td><td>Services no longer relevant to clients</td></tr><tr><td>There have been charging/discount problems</td><td>Clients are put off by changed financials</td></tr><tr><td>There have been too many/too frequent unfulfilled requests</td><td>Clients moved to a more reliable company</td></tr><tr><td>The contracting/interviewing process has been managed inefficiently</td><td>Clients moved to a faster company</td></tr></table>

Burton-Jones & Meso/Decomposition Quality and Forms of Information

<table><tr><td>Reason</td><td>Explanation</td></tr><tr><td>The client market has reduced in size</td><td>Fewer clients means fewer requests</td></tr><tr><td>Each client has fewer jobs to be done</td><td>Fewer jobs to be done means fewer requests</td></tr><tr><td>Other if reasonable (1 point or 1⁄2 point per answer)</td><td></td></tr></table>

Page 10 (3 min, 30 seconds):

## Problem-Solving Question 7 (with suggested answers):

7. Although the sample interview went well, you notice two weeks later that the applicant has not been contracted with the client. Based on your understanding of ICI’s business, list up to four reasons why this could be possible and explain the basis for each answer.

<table><tr><td>Reason</td><td>Basis for answer.</td></tr><tr><td>The job is cancelled</td><td>There is no job left</td></tr><tr><td>The client interview result is negative</td><td>The interview didn’t meet the client’s requirements</td></tr><tr><td>There were problems in developing the contract terms (e.g., salary, discount, charges, end dates)</td><td>A complete contract does not get developed</td></tr><tr><td>The contract start date has not been reached</td><td>The applicant is not yet contracted</td></tr><tr><td>Other if reasonable (1 point or 1⁄2 point per answer)</td><td></td></tr></table>

## Page 11 (0.5 minutes):

To answer the previous 7 problem-solving questions:

\- to what extent did you rely on the information in the diagrams?

Page 12 (50 seconds):

Overall, based on your experience in this exercise:

Ease of Understanding ICI Diagrams

\- to what extent did you find the three diagrams of ICI to be complex?

\- to what extent did you find the three diagrams of ICI to be difficult to understand?

## Ease of Understanding ICI’s Business

\- to what extent did you find ICI’s business to be complex?

\- to what extent did you find ICI’s business to be difficult to understand?

All of these questions used a 5-point Likert scale from “Not at all” to “A great extent.”

End of Experimental Materials

## About the Authors

Andrew Burton-Jones is an Assistant Professor in the Sauder School of Business, University of British Columbia. He holds a B. Comm., and M.I.S. from the University of Queensland and a Ph.D. from Georgia State University. His first research stream seeks a deeper understanding of the meaning and consequences of system usage. His second seeks to improve representationa techniques used in systems analysis and design. He has published in Data & Knowledge Engineering, Database for Advances in Information Systems, Information & Management, Information Systems Research, and MIS Quarterly. Prior to his academic career, he was a senior consultant in a Big-4 consulting firm.

Peter Meso is a member of faculty in the Computer Information Systems Department of Georgia State University’s J Mack Robinson College of Business, located in Atlanta, Georgia, USA. He is also the co-editor in chief of the African Journal of Information Systems and a member of the Editorial Review Boards of the Journal of Global Information Management and the Electronic Journal of Information Systems in Developing Countries respectively. Dr. Meso earned his PhD degree in Information Systems from Kent State University, and holds a Bachelor of Science degree (Information systems) and a Master of Business Administration (MBA) degree from the United States International University - Africa. He conducts research in the areas of information systems development and global information technology with a key interest in researching information technology in the developing economies. Dr Meso’s research appears in a number of journals, among them: Information Systems Research, Communications of the ACM, Information Systems Journal, Journal of Systems and Software, Information Systems Management, Journal of Global Information Management, IEEE Transactions on Information Systems in Biomedicine, and the Journal of the American Society for Information Sciences and Technology

Copyright © 2008, by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers for commercial use, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via e-mail from ais@gsu.edu.

# 1JA  omn Ses

ISSN: 1536-9323

Editor Kalle Lyytinen Case Western Reserve University, USA

<table><tr><td colspan="4">Senior Editors</td></tr><tr><td>Robert Fichman</td><td>Boston College, USA</td><td>Dennis Galletta</td><td>University of Pittsburgh, USA</td></tr><tr><td>Varun Grover</td><td>Clemson University, USA</td><td>Rudy Hirschheim</td><td>Louisiana State University, USA</td></tr><tr><td>Robert Kauffman</td><td>University of Minnesota, USA</td><td>Frank Land</td><td>London School of Economics, UK</td></tr><tr><td>Jeffrey Parsons</td><td>Memorial University of Newfoundland, Canada</td><td>Suzanne Rivard</td><td>Ecole des Hautes Etudes Commerciales, Canada</td></tr><tr><td>Ananth Srinivasan</td><td>University of Auckland, New Zealand</td><td>Bernard C.Y. Tan</td><td>National University of Singapore, Singapore</td></tr><tr><td>Michael Wade</td><td>York University, Canada</td><td>Ping Zhang</td><td>Syracuse University, USA</td></tr><tr><td colspan="4">Editorial Board</td></tr><tr><td>Steve Alter</td><td>University of San Francisco, USA</td><td>Kemal Altinkemer</td><td>Purdue University, USA</td></tr><tr><td>Michael Barrett</td><td>University of Cambridge, UK</td><td>Cynthia Beath</td><td>University of Texas at Austin, USA</td></tr><tr><td>Michel Benaroch</td><td>University of Syracuse, USA</td><td>Francois Bodart</td><td>University of Namur, Belgium</td></tr><tr><td>Marie-Claude Boudreau</td><td>University of Georgia, USA</td><td>Susan A. Brown</td><td>University of Arizona, USA</td></tr><tr><td>Tung Bui</td><td>University of Hawaii, USA</td><td>Andrew Burton-Jones</td><td>University of British Columbia, Canada</td></tr><tr><td>Dave Chatterjee</td><td>University of Georgia, USA</td><td>Patrick Y.K. Chau</td><td>University of Hong Kong, China</td></tr><tr><td>Mike Chiasson</td><td>Lancaster University, UK</td><td>Mary J. Culnan</td><td>Bentley College, USA</td></tr><tr><td>Jan Damsgaard</td><td>Copenhagen Business School, Denmark</td><td>Samer Faraj</td><td>McGill university, Canada</td></tr><tr><td>Chris Forman</td><td>Carnegie Mellon University, USA</td><td>Ola Henfridsson</td><td>Viktoria Institute &amp; Halmstad University, Sweden</td></tr><tr><td>Hitotora Higashikuni</td><td>Tokyo University of Science, Japan</td><td>Kai Lung Hui</td><td>National University of Singapore, Singapore</td></tr><tr><td>Hemant Jain</td><td>University of Wisconsin-Milwaukee, USA</td><td>Bill Kettinger</td><td>University of South Carolina, USA</td></tr><tr><td>Rajiv Kohli</td><td>College of William and Mary, USA</td><td>Mary Lacity</td><td>University of Missouri-St. Louis, USA</td></tr><tr><td>Ho Geun Lee</td><td>Yonsei University, Korea</td><td>Jae-Nam Lee</td><td>Korea University</td></tr><tr><td>Kai H. Lim</td><td>City University of Hong Kong, Hong Kong</td><td>Ji-Ye Mao</td><td>Renmin University, China</td></tr><tr><td>Anne Massey</td><td>Indiana University, USA</td><td>Emmanuel Monod</td><td>Dauphine University, France</td></tr><tr><td>Michael Myers</td><td>University of Auckland, New Zealand</td><td>Fiona Fui-Hoon Nah</td><td>University of Nebraska-Lincoln, USA</td></tr><tr><td>Mike Newman</td><td>University of Manchester, UK</td><td>Jonathan Palmer</td><td>College of William and Mary, USA</td></tr><tr><td>Paul Palou</td><td>University of California, Riverside, USA</td><td>Brian Pentland</td><td>Michigan State University, USA</td></tr><tr><td>Yves Pigneur</td><td>HEC, Lausanne, Switzerland</td><td>Jaana Porra</td><td>University of Houston, USA</td></tr><tr><td>Sandeep Purao</td><td>Penn State University, USA</td><td>T. S. Raghu</td><td>Arizona State University, USA</td></tr><tr><td>Dewan Rajiv</td><td>University of Rochester, USA</td><td>Balasubramaniam Ramesh</td><td>Georgia State University, USA</td></tr><tr><td>Timo Saarinen</td><td>Helsinki School of Economics, Finland</td><td>Susan Scott</td><td>The London School of Economics and Political Science, UK</td></tr><tr><td>Ben Shao</td><td>Arizona State University,USA</td><td>Olivia Sheng</td><td>University of Utah, USA</td></tr><tr><td>Carsten Sorensen</td><td>The London School of Economics and Political Science, UK</td><td>Katherine Stewart</td><td>University of Maryland, USA</td></tr><tr><td>Mani Subramani</td><td>University of Minnesota, USA</td><td>Burt Swanson</td><td>University of California at Los Angeles, USA</td></tr><tr><td>Dov Te&#x27;eni</td><td>Tel Aviv University, Israel</td><td>Jason Thatcher</td><td>Clemson University, USA</td></tr><tr><td>Ron Thompson</td><td>Wake Forest University, USA</td><td>Christian Wagner</td><td>City University of Hong Kong, Hong Kong</td></tr><tr><td>Eric Walden</td><td>Texas Tech University, USA</td><td>Eric Wang</td><td>National Central University, Taiwan</td></tr><tr><td>Jonathan Wareham</td><td>ESADE, Spain</td><td>Stephanie Watts</td><td>Boston University, USA</td></tr><tr><td>Bruce Weber</td><td>London Business School, UK</td><td>Tim Weitzel</td><td>Bamberg University, Germany</td></tr><tr><td>Richard Welke</td><td>Georgia State University, USA</td><td>George Westerman</td><td>Massachusetts Institute of Technology, USA</td></tr><tr><td>Kevin Zhu</td><td>University of California at Irvine, USA</td><td>Ilze Zigurs</td><td>University of Nebraska at Omaha, USA</td></tr><tr><td colspan="4">Administrator</td></tr><tr><td>Eph McLean</td><td>AIS, Executive Director</td><td colspan="2">Georgia State University, USA</td></tr><tr><td>J. Peter Tinsley</td><td>Deputy Executive Director</td><td colspan="2">Association for Information Systems, USA</td></tr><tr><td>Reagan Ramsower</td><td>Publisher</td><td colspan="2">Baylor University</td></tr></table>
