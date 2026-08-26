---
otero_id: 9450
otero_key: "YX8UBM2E"
title: "Behavioral economics for decision support systems researchers"
authors: "David Arnott; Shijia Gao"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.05.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Behavioral economics for decision support systems researchers

David Arnott<sup>⁎</sup>, Shijia Gao

![](/api/attachments/YX8UBM2E/fulltext/images/6509a2fc60d2d10e5fb00f1fdc534ef8d142ac81f95b03004d370a046a97dbd7.jpg)

Faculty of Information Technology, Monash University, PO Box 197, Caulfield East, Victoria 3145, Australia

## A R T I C L E I N F O

Keywords: Behavioral economics Decision-making Dual process theory Heuristics and biases Decision support systems

## A B S T R A C T

Theories of decision-making, both prescriptive and descriptive, have long been important to decision support systems (DSS). Currently, the field of behavioral economics (BE) provides the dominant descriptive approach for understanding human decision-making. An indication of the field's standing is that three Nobel Prizes have been awarded to behavioral economics. Contemporary BE has two major theory foundations – the dual process theory of decision-making cognition and a set of judgment heuristics and cognitive biases. These foundations have been combined to create important theories like prospect theory and action strategies like nudging. Previous research has found that DSS has been slow to adopt recent advances in BE, even to the extent that some projects continue to use older theories like the phase model of decision making. This paper aims to make DSS researchers aware of contemporary BE, its nature, and its diferences with early BE. We believe that behavioral economics is a useful and productive foundation for DSS research and that the use of BE in DSS should be significantly expanded.

## 1. Introduction

Theories of decision-making have long been important to decision support systems (DSS) research. Decision theory can be broadly divided into economic decision-making and behavioral decision theory. Economic decision-making is largely prescriptive in nature and focuses on maximizing a decision outcome subject to constraints (typically budget and resource constraints) to reach an equilibrium in some form of a market. Behavioral decision theory on the other hand is largely descriptive in nature and has a focus on understanding how and why people make decisions. Browne and Parsons [1] argued that behavioral decision theory has had a profound efect on information systems (IS), and therefore DSS, scholarship. Over time, behavioral decision theory has morphed into the field of behavioral economics (BE), a field which has significant momentum in business research and practice. It is im portant to note that the prescriptive and descriptive views of decision theory coexist and are complementary. Occasionally, there is overlap between the two theory sets in DSS research (for example, [2,3]). There are reviews and summaries of aspects of BE available, mainly from a psychology perspective (for example, [4]). While useful, these reviews can be dificult for DSS researchers as they assume significant foundation knowledge of various psychology theories. This paper views the reference theory of BE through the lens of DSS research and aims to make DSS researchers more aware of the possibilities that the de scriptive theories of BE have for their research.

BE is widely believed to have started in the 1950's with the work of Herbert Simon. Simon won the Nobel Memorial Prize in Economic Sciences in 1978 “for his pioneering research into the decision-making process within economic organizations”.<sup>1</sup> Building on Simon's work, Daniel Kahneman won the 2002 Nobel Prize “for having integrated insights from psychological research into economic science, especially concerning human judgment and decision-making under uncertainty”.<sup>2</sup> Kahneman's prize-winning theory was developed with Amos Tversky. Most recently the 2017 Nobel Prize was awarded to Richard Thaler for “his contributions to behavioral economics”.<sup>3</sup> Chapman and Pike [5] in a significant review of the BE literature argued that Simon typifies the “old” BE, while Kahneman, Tversky, Thaler and their colleagues typify the “new”. This paper uses the terms “early” and “contemporary” BE as they are less value-loaded.

Over time a number of DSS researchers have commented that the decision-making theories broadly associated with contemporary behavioral economics should be used more widely in DSS research (for example, [6–9]). A central theme of this discussion is that the decision theory typified by Kahneman, Tversky and Thaler and related psychology and economics researchers should supplant some early BE theory, especially the phase model, as reference theory. Twenty-five years ago, Angehrn and Jelassi [10] argued that Simon's theory “has become a serious obstacle for the evolution of DSS theory and practice” (p. 269). Arnott and Pervan [11], in an analysis of 21 years of DSS research, found that 60% of citations to BE in the most recent period of their analysis were from Simon's theory.

This paper contributes to the ongoing discussion about the descriptive decision-making foundations of DSS research and practice by first familiarizing researchers with BE, both early and contemporary. It then discusses the use of BE in DSS research and provides examples that involve diferent BE theories and research methods. It ofers suggestion for how BE can be used in future DSS research.

## 2. Early behavioral economics

The early school of BE is very strongly identified with one researcher – Herbert Simon. Because of this, a discussion of his academic career is warranted in order to understand the emergence of BE in the latter part of the Twentieth Century. Herbert Simon (1916–2001) was a polymath who contributed to a wide range of scientific disciplines. His breadth of scholarship is so unusual that cognitive science researchers have even studied his Renaissance-like creativity and cognitive style [12]. He confessed a monomania for decision-making in Simon [13] and this is the thread that links his multi-disciplinary contributions. Simon was one of the most prolific scientific writers of the 20th Century. His bibliography identifies over 1000 items and when only research papers, refereed book chapters, and monographs are selected they total 696 significant, individual, scientific publications.

Simon's greatest contribution is possibly in economics, and in particular the microeconomics of decision-making. Simon's theory of bounded rationality first emerged in his 1942 PhD dissertation and was the foundation of his 1978 Nobel Prize. Bounded rationality will be discussed in more detail below. In addition to his key book Administrative Behavior [14] Simon laid the foundation of BE in the seminal papers “A behavioral model of rational choice” in the Quarterly Journal of Economics [15] and “Theories of decision-making in economics and behavioral science” in The American Economic Review [16].

In psychology Simon was awarded the American Psychological Association (APA) Award for Distinguished Scientific Contributions to Psychology in 1969 and the APA Award for Outstanding Lifetime Contributions to Psychology in 1993. Simon [17,18] collectively provides an overview of his approach to the psychology of decisionmaking. Simon also made significant contributions to computer science (for example, [19–21]) and in particular to the area of artificial in telligence, where he is regarded as the co-founder [22–24]. In 1975, he was awarded the A.M. Turing Award jointly with Allen Newell fo “basic contributions to artificial intelligence, the psychology of human cognition, and list processing.” The Turing Award is the most presti gious in IT; its US\$1 m award is of similar value to a Nobel Prize. In addition to his contributions to economics, psychology, and computer science, Simon made significant contributions to the philosophy of science [25–27], research methodology, especially with protocol analysis [28] and design science [29], management & organization theory [14,30–32], and education [33,34]. Table 1 provides a summary of the key events in Simon's decision-making research.

Before discussing the detail of Simon's theory of decision-making it is appropriate to consider the decision theory landscape before his 1955 “A behavioral model of rational choice” paper; it was a landscape dominated by neoclassical economics. Economic decision-making involves making an optimal judgment subject to context constraints. A decision outcome from this process is termed economically rational. The usual object that is being maximized is utility, defined as the sa tisfaction one obtains from consuming a good or service. Utility as a construct in decision-making can be traced to Daniel Benoulli in 1728 but it gained its modern version, expected utility, in the work of von Neuman and Morgenstern [35]. In economic decision making the decision maker is characterized as homo economicus or “economic man”. The perfect decision maker that is economic man underpins most economic theories and models; its conceptualization originated in Adam Smith's Wealth of Nations [36]. Economic man is an ideal decision maker who makes decisions with perfect knowledge of all aspects of the decision situation and has infinite information processing abilities. This neoclassical economic view of decision making was removed from any consideration of human psychology perhaps because when the theory was developed psychology as a social science was in its infancy and was considered unscientific ([4], p. 5). The rational decision-making paradigm of neoclassical economics remains the dominant prescriptive theory of decision making.

For Simon, the ideal view of economic rationality was at odds with his studies of administrative managers in the 1940s. He argued in Simon [14] and Simon [15] that decision makers could not have perfect knowledge of a decision situation and, further, they are limited in their cognitive and information processing abilities. In addition, they are normally subject to time pressure that means that perfect computations of utility functions are not possible. Simon's key insight was that decision makers' rationality was bounded rather than perfect. Rather than maximizing utility, they satisfice and make the best decision that they can in each situation. Under bounded rationality decision makers use heuristics or rules of thumb rather than optimization processes. In relaxing the perfect information and processing assumptions of economic decision making, Simon's bounded rationality changed the way many researchers viewed rational decisions. It remains contested in economic theory, especially in macroeconomics [37], although Keynes [38] hinted at bounded rationality when he said that decisions came about “not as the outcome of a weighted average of quantitative benefits multiplied by quantitative probabilities” (p. 161). Nobel Prize winners George Akerlof and Robert Shiller are leading advocates of the restoration of actual human behavior to the core assumptions of macroeconomics [39]. At the market, or microeconomic level of economic thought, the theory of bounded rationality has gained more acceptance.

Following bounded rationality, the second major aspect of Simon's decision-making theory is the phase model of decision-making. It is often called the phase theory or the phase theorem in decision-making

A timeline of key events in Simon's decision-making research.

<table><tr><td>Year</td><td>Item</td><td>Reference</td><td>Citesa</td><td>Comment</td></tr><tr><td>1945</td><td>Administrative Behavior</td><td>Simon [14]</td><td>27,855</td><td>A reworking of his PhD dissertation.</td></tr><tr><td>1955</td><td>A Behavioral Model of Rational Choice paper</td><td>Simon [15]</td><td>16,061</td><td>Seminal work in behavioral economics.</td></tr><tr><td>1960</td><td>The New Science of Management Decision</td><td>Simon [31]</td><td>7776</td><td>Popularizes Simon&#x27;s theories. Widely read by managers.</td></tr><tr><td>1969</td><td>The Sciences of the Artificial</td><td>Simon [29]</td><td>25,655</td><td>Argues for design science as the preferred research strategy for decision-making &amp; management research.</td></tr><tr><td>1972</td><td>Human Problem Solving</td><td>Newell &amp; Simon [24]</td><td>19,709</td><td>Seminal work in artificial intelligence.</td></tr><tr><td>1975</td><td>A.M. Turing Award</td><td></td><td></td><td>With Allen Newell.</td></tr><tr><td>1978</td><td>Nobel Prize in Economics</td><td></td><td></td><td>For the theory of bounded rationality.</td></tr><tr><td>1986</td><td>National Medal for Science (USA)</td><td></td><td></td><td>For contributions to behavioral and social science.</td></tr></table>

![](/api/attachments/YX8UBM2E/fulltext/images/420045761af07696e4f316e6a7ce69eacfdaced234f0c2787cc9f3936d1012a0.jpg)  
Fig. 1. Simon's phase model of decision-making.

research. A phase model specifies a number of stages or phases that are followed, and should be followed, in making a decision. Phase models of decision processes had existed for many years before Simon (for example, [40]) but Simon adapted the concept as a descriptive and explanatory model of the process of decision-making under bounded rationality. Simon's model is shown in Fig. 1 where the phases of intelligence, design, and choice define a decision process. Intelligence, which is taken from the military concept, involves “searching the environment for conditions calling for decision” ([31], p. 2) as well as collecting data about a potential decision. Design entails “inventing, developing, and analyzing possible courses of action”, and choice involves “selecting a particular course of action from those available” ([31], p. 2). The sequence of the phases in the figure is only one possible path; the phases may occur simultaneously or may occur in diferent sequences. They also occur iteratively as shown by the arrows in the figure. Further, the phase model is recursive. Each decision routine, or instance of a phase, may itself involve decision-making. For example, the intelligence phase may require decisions about what data to collect or what environments to scan. These sub-decisions can be described by their own intelligence, design, and choice routines. Simon's phase model can therefore be characterized as a staged, iterative, and recursive model of decision-making. Simon's phase model has been widely accepted in business research and his three core-decision-theory works currently have 51,692 citations. Another well-accepted extension of Simon's phase model is the five-stage model of Mintzberg, Raisin ghani, and Theoret [41].

The phase model of decision-making is often adopted in research designs without critique or citation and has assumed paradigm status in a similar manner to Anthony's levels of management activity [42]. However, as Lipschitz and Bar-Ilan [43] relate “Considering the variety and ubiquity of phase models, it is surprising to find that the empirical evidence for their descriptive and prescriptive validity is very slim.” Lipschiltz and Bar-Ilan conducted experimental research that found disconfirming evidence for the phase model's prescriptive validity and only weak support for its descriptive validity. The conclusion from the testing of the phase model is that, unfortunately, it has very little scientific validity. How is such a situation possible with such a popular, enduring, and widely accepted model? The answer lies in the nature of business research in the 1940s and 1950s, the period when Simon's phase model of decision-making was developed. Simon's is a diferent kind of scholarship to current experiment-based BE and general business research; most of Simon's publications would currently be classified as conceptual studies. The nature of business and behavioral science research is radically diferent today and the standards of rigor and validity, and the statistical techniques that are currently used, did not exist when Simon developed his theory of decision-making. Early in Simon's career, unreferred books, essays, and book chapters were often regarded as equivalent to empirical refereed journal papers.

The third major aspect of Simon's theory of decision-making is the concept of decision structuredness. Simon ofered the following definition: “Problems are well structured when the goal tests are clear and easily applied, and when there is a well-defined set of generators for synthesizing potential solutions. Problems are ill structured to the extent that they lack these characteristics.” ([14], p. 128). A totally structured decision is one where a computer program can be written to make the decision; a totally unstructured decision is one where no aspect of the decision process can be articulated. For Simon, the decisions people make are largely unstructured, where the decisions of economic man, by definition, are completely structured.

## 3. Contemporary behavioral economics

While Simon's research was having a fundamental influence on business and information systems research in the 1970s and 1980s, a new generation of psychologists and economists were using the relatively new, but now dominant, social science experimental research methods to explore the nature of human decision-making. The psychologists Daniel Kahneman and Amos Tversky took Simon's challenge to the rationality of economic man into the laboratory and developed the heuristics and biases research area. Kahneman and Tversky's work was founded on Simon's theory of bounded rationality, indeed, Kahneman titled his Nobel Prize Lecture “Maps of Bounded Rationality: A Perspective on Intuitive Judgment and Choice” [44]. Other psychologists that made significant contributions to the development of BE include Hillel Einhorn, Jonathon Evans, Baruch Fischhof, Robin Hogarth, and Paul Slovic. Young economists were attracted to Kahneman and Tversky's research and the first economist to publish in this new area was Richard Thaler [45]. Other major contributors to the development of BE are George Akerlof, Dan Ariely, Colin Camerer, Jack Knetsch, George Lowenstein, and Robert Shiller.

There are other significant branches of descriptive decision-making study arising from Simon's early BE, most notably the research associated with Gary Klein and Gerd Gigerenzer. These two quite diferent research groupings share two propositions: decision-making is best studied in the field with real decision makers, and expert intuition, through the action of heuristics, is a source of decision efectiveness rather than a flaw in decision making. Klein is best known for his landmark study of fire commanders in the field [46]. His resulting naturalistic decision-making approach and the recognition-primed decision model is the basis for tactical and strategic decision-making in US and European militaries [47,48]. Klein also collaborated with Kahneman to investigate under what circumstances expert intuition is preferable to analytic decision-making [49]. On the other hand, Gigerenzer's program of research is deeply critical of the heuristics and biases approach, even arguing that biases may be experimental artifacts ([50], ch. 12). His core proposition is that heuristics are a source of efectiveness in decision-making and that the Kahneman and Tversky approach has an overly negative frame. Gigerenzer's approach is summarized in Gigerenzer and Selten [51] and Gigerenzer [52]. Other researchers have questioned the validity of bounded rationality as a foundation for BE. For example, Cohen and Dickens [53] argue that evolutionary psychology is a superior theory base for BE and understanding how we evolved to cope with our limited capacity for rationality could illuminate human decision processes more efectively than a heuristics and biases approach.

Despite the criticisms and alternative research approaches described above, the BE that is typified by the research of Kahneman and Tversky has become the scientific orthodoxy in the understanding of human decision-making. In a commentary in the Harvard Business Review about the impact of the various streams of BE on business and management, Justin Fox concluded “The Kahneman-Tversky heuristics-and-biases approach has the upper hand right now, both in academia and in the public mind.” ([54], p. 84). Fox reported that 90% of current BE is in the Kahneman and Tversky camp. Table 2 provides a timeline of Kahneman and Tversky's research. A comparison of the citations to Simon's work in Table 1 to the Kahneman and Tversky citations in Table 2 highlights the impressive impact of the heuristics and biases program.

That Thinking Fast and Slow has attracted over 20,000 citations in eight years demonstrates the academic acceptance of the contemporary BE orthodoxy. Further, despite being 512 pages in length and a reasonably challenging read, in January 2017 Thinking Fast and Slow was ranked 44 by Amazon in all book sales. This is a remarkable achieve ment for any non-fiction book, let alone an economics-psychology hybrid. It received the National Academy of Sciences Best Book Award in 2012.

Unlike the situation with early BE where Simon was virtually the sole founder, the marketing of the heuristics and biases approach to the wider public has been more efective partly because many more researchers have been involved. They have successfully converted their scientific journal publications to popular books to educate the public. Thaler's Misbehaving: The Making of Behavioral Economics provides a chronicle of the history of the discipline [60]. Thaler and Sunstein's 2009 book Nudge showed how BE could be used to improve public policy and personal welfare and was a New York Times Best Seller as well as The Economist Best Book of the Year. It has also earned 11,886 academic citations. Dan Ariely's books Predictably Irrational [62] and The Upside of Irrationality [63] were both on the New York Times Best Seller List. Complementing this set of books on BE that are aimed at the general public is Bazerman and Moore [64]. First published in 1986 and now in its eighth edition, this relatively slim volume has been a vehicle for introducing heuristics and biases to managers and professionals. Special journal and magazine issues on heuristics and biases, like the May 2015 issue of the Harvard Business Review, have brought BE to the attention of managers and business professionals. There is even a Behavioral Economics for Dummies [65].

The dominant descriptive decision theory of contemporary BE has two main foundations: the first is the dual process theory of decisionmaking cognition; the second is a set of heuristics and cognitive biases that, in some circumstances, systematically prejudice decision quality. These foundations are discussed in the next two sections.

## 3.1. The dual process theory of decision-making cognition

The dual process theory holds that decision-making occurs within and between two cognitive processes or systems. Kahneman and Frederick [66] typified them as two families of cognitive operations. The dual processes have been known by many names; Evans [67] identified 14 diferent sets of titles for the two systems. For example, Thaler and Sunstein [61] termed the two systems the Automatic System and the Reflective System, while Sloman [68] used Associative System and Rule-based System. In an influential paper, Stanovich and West [69] termed them System 1 and System 2 in order to avoid descriptive labeling. Kahneman initially used the titles Intuition and Reasoning but he later adopted the value free terminology and his endorsement meant that the System 1 and 2 terms have become standard. The dual process theory is not restricted to cognitive psychology, Chaiken [70] and Deutsch and Starck [71] show the social psychology perspective on the theory.

Kahneman [59] provided the following definitions of the dual processes: “System 1 operates automatically and quickly, with little or no efort and no sense of voluntary control. System 2 allocates attention to the efortful mental activities that demand it, including complex computations.” (pp. 20–21). Table 3, that is partially based on Thaler & Sunstein ([61] Table 1.1), Evans ([67] Table 2), and Stanovich and West ([69] Table 3), shows the properties and nature of the two cognitive systems.

System 1 is fast, automatic, efortless, and intuitive. When facing a decision, System 1 is the first in action. It operates through innate, instinctive behavior. In an evolutionary sense, System 1 is the oldest form of decision-making and is the product of evolution to ensure survival and gene reproduction ([69], p.660; [59], p.301). System 1 is a set of universal cognitive processes, shared in varying degrees of effectiveness by all animal species. It is dificult to explain or document how System 1 arrives at a decision, we only know it has when the decision enters our consciousness.

System 2 is slow, deliberate and requires significant cognitive efort. The complex System 2 evolved uniquely in humans although other high performing species may have evolved their own form of System 2 and there is archaeological evidence of the dual processes in humans [72]. System 2's abilities are not innate and must be formed through education, both formally in schools and universities, and less formally in families and social interaction. The essence of System 2 is application of a set of rules or algorithms to a decision task.

While described as discrete systems, System 1 and 2 can operate at the same time and can interact. Evans [72] described the situation as like two minds in the same body. Kahneman and Frederick [66] relate: “System 1 quickly proposes intuitive answers to judgment problems as they arise, and System 2 monitors the quality of these proposals, which it may endorse, correct, or override.” This efortful control of System 1 by System 2 is well established. Control can also pass from System 2 to 1. John Maynard Keynes in the General Theory of Employment, Interest and Money understood the interplay of System 1 and System 2. He famously related “individual initiative will only be adequate when rea sonable calculations are supplemented and supported by animal spirits” ([38], p.162).

Table 2  
A timeline of key events in Kahneman and Tversky's research.

<table><tr><td>Year</td><td>Item</td><td>Reference</td><td>Cites</td><td>Comment</td></tr><tr><td>1973</td><td>Availability heuristic</td><td>Tversky &amp; Kahneman [55]</td><td>9651</td><td>First major paper on heuristics and biases.</td></tr><tr><td>1974</td><td>Heuristics and biases</td><td>Tversky &amp; Kahneman [56]</td><td>48,113</td><td>Seminal paper of contemporary BE.</td></tr><tr><td>1979</td><td>Prospect theory</td><td>Kahneman &amp; Tversky [57]</td><td>53,339</td><td>Published in Econometrica; one of the most cited papers in social science.</td></tr><tr><td>1981</td><td>Framing bias</td><td>Tversky &amp; Kahneman [58]</td><td>18,333</td><td>Published in Science.</td></tr><tr><td>2002</td><td>Nobel Prize in Economics</td><td></td><td></td><td>Awarded to Kahneman.</td></tr><tr><td>2011</td><td>Thinking Fast and Slow</td><td>Kahneman [59]</td><td>20,080</td><td>Written for a general audience.</td></tr><tr><td>2013</td><td>Presidential Medal of Freedom</td><td></td><td></td><td>Awarded to Kahneman. Highest civilian award in the USA.</td></tr></table>

Table 3  
The two cognitive systems of decision making.

<table><tr><td>System 1</td><td>System 2</td></tr><tr><td>Unconscious</td><td>Conscious</td></tr><tr><td>High capacity</td><td>Low capacity</td></tr><tr><td>Automatic</td><td>Controlled</td></tr><tr><td>Holistic</td><td>Analytic</td></tr><tr><td>Associative</td><td>Rule based</td></tr><tr><td>Effortless – undemanding of cognitive capacity</td><td>Effortful – demanding of cognitive capacity</td></tr><tr><td>Fast</td><td>Slow</td></tr><tr><td>Skilled</td><td>Rule following</td></tr><tr><td>Highly contextualized</td><td>Decontextualized</td></tr><tr><td>Personalized</td><td>Depersonalized</td></tr><tr><td>Acquisition by biology, exposure, and experience</td><td>Acquisition by cultural and formal tuition</td></tr></table>

System 1 is associated with expertise and expert judgment while System 2 is the realm of the calm rational advisor, but also the learner and novice. Over time System 2 tasks can be converted to System 1 through exposure and experience. An example of this conversion is driving an automobile. Learning to drive requires significant cognitive efort - learning the road laws and the algorithms for controlling the vehicle. This is a System 2 dominant task. After considerable practice driving becomes automatic; it is common to drive a usual trip, say driving to work, and not remember the details of the driving task. This means that the task has been converted to an automatic and efortless System 1 process. Far from being inefective or second rate, in management decision-making the fast, intuitive processes of System 1 can lead to superior outcomes compared to System 2 dominated processes [46,73,74]. Dificult and strategic management tasks will likely be System 1 dominant and a decision maker's conception of such a task is likely to be volatile. Thaler [60] related “my hunch is that as the importance of a decision grows, the tendency to rely on quantitative analyses done by others tends to shrink. When the championship or the future of the company is on the line, managers tend to rely on their gut instincts.” Further, as Winter [75] related “In many cases a decision based on emotion or intuition may be more eficient – and indeed better – than a decision arrived at after thorough and rigorous analysis of all the possible outcomes and implications.”

System 2 managerial tasks are likely to be more stable in their in ternal representation. The extreme case of a System 2 process is the decision making of the perfectly rational but fictitious economic man. Knowing when to replace System 1 intuitions with System 2 rules and algorithms is a dificult decision for both managers and analysts. It is also a decision that depends on context, particularly the skills and experience of the decision maker. Bazerman and Moore [64] argued that “a complete System 2 process is not required for every managerial decision, a key goal for managers should be to identify situations in which they should move from the intuitively compelling System 1 thinking.” Somewhat ironically, this decision to replace System 1 with System 2 is likely to be an intuitive System 1 decision.

## 3.2. Heuristics and biases

The heuristics and bias stream of BE research is essentially devoted to understanding System 1 decision processes, how they are efective and how they fail. The seminal publication is Tversky and Kahneman [56], published in Science, a publication that marks the beginning of the contemporary BE. Klein [76] called heuristics and biases a paradigm rather than a theory or an approach. We believe that they are best thought of as a large collection of interrelated theories where each theory describes a particular aspect of human decision-making. Unfortunately, this collection of disparate efects makes it dificult to have a coherent overall view of the research.

## 3.2.1. General heuristics

The concept of heuristics in decision making was first developed by Herbert Simon as part of his theory of bounded rationality. Tversky and Kahneman [56] built on Simon's work to identify three general and innate heuristics that guide decision making. Being general and innate means that all humans have these heuristics as a fundamental part of their brain's function. The action of these general heuristics means that decision makers can quickly and efortlessly arrive at a decision. There are strong evolutionary benefits for the development of these general heuristics in humans. Tversky and Kahneman's original general heuristics are availability, representativeness, and adjustment and anchoring.

The availability heuristic is an efortless mental process whereby people assess the probability of an event by the degree to which instances are available in memory. Using availability people tend to favor more recent information. Under the availability heuristic decisions are based on what comes to mind easily and quickly. For example, a person could assess the likelihood of contracting a skin cancer by recalling incidences of skin cancer in friends and colleagues.

Using the representativeness heuristic people assess the likelihood of an occurrence by the similarity of that occurrence to the stereotype of a set of occurrences. Representativeness involves using categories in decision making. Judging an occurrence because it is similar to a broader category is usually an efective mental short-cut. Tversky and Kahneman provided the example of providing a profile of “Steve” as “a weak and tidy soul, he has a need for order and structures, and a passion for detail” ([56], p. 185). Participants were then asked if Steve is a farmer, salesman, airline pilot, librarian, or physician. Using the representativeness heuristic people will judge Steve's occupation according to stereotypes of the occupations compared to the profile – librarian is a popular response.

Under the third original heuristic, adjustment and anchoring, people make assessments by starting from an initial value and adjusting this value to arrive at the final decision. Anchoring on a starting point reduces the complexity of a decision scenario. The decision maker then makes a judgment of how much to move or change the decision from this anchor point. The prediction of future situations from an anchor is common to many human activities, for example when running for a ball while playing sport or forecasting future trafic positions while driving a car.

Since the publication of Tversky and Kahneman [56] there has been considerable research efort in identifying other general heuristics. These new heuristics often fail the criteria for being a general heuristic as they can be relatively specific and can be more accurately defined as a bias, or are primarily a function of System 2 rather than System 1. These proposed heuristics include the efort heuristic and the recognition heuristic. The efort heuristic [77] holds that people judge the quality of an object, process, or event by the amount of efort that has gone into its development. Interestingly, this is a similar concept to the Marxian labor theory of value. The recognition heuristic [78], also called the less-is-more efect, allows people to quickly judge the value of something based on their ease of recognition. The recognition heuristic can lead to situations where “less knowledge is better than more knowledge for making accurate inferences.” ([78], p.76).

The most important development in general heuristic research since Tversky and Kahneman [56] is the afect heuristic [79]. Slovic et al. found that “afect also plays a central role in … dual process theories of thinking, knowing, and information processing.” (p. 398). The afect heuristic operates because people tag memories and representations of things in their minds with previous assessments of afect (feeling and emotion). Put simply, afect can serve as a fast, efortless cue in decision making. Slovic et al. [79] found the afect heuristic was efective in judgments related to the cost and benefits of technologies, the safe level of chemicals, and in the prediction of the economic performance of various industries. Kahneman, Ritov, and Schkade [80] found that af fect is the principal determinant of the willingness to pay for public goods. Ariely [81] describes a series of experiments about dishonesty in decision making that are partly concerned with the afect heuristic. Kahneman and Fredrick [66] argued that the heuristics and bias re search has overly focused on the nature and efects of the availability and representativeness heuristics. In considering the role of emotion in decision making they noted that in the 1970s, when the heuristics and biases research stream was established, psychology had a strong emphasis on cognitive rather than emotional or motivational factors. They went further and stated, “It has become evident that an afect heuristic … should replace anchoring in the list of major general-purpose heuristics.” ([66], p. 56). They argued that anchoring and adjustment efects are best thought of as cognitive biases. This leaves availability, representativeness, and afect as the general decision-making heuristics.

Table 4 Typologies of biases.

<table><tr><td>Tversky &amp; Kahneman [56]</td><td>Hogarth [87]</td><td>Arnott [6]</td><td>Lovallo &amp; Sibony [89]</td><td>Bazerman &amp; Moore [64]</td></tr><tr><td>Representativeness biases</td><td>Acquisition biases</td><td>Memory biases</td><td>Action oriented biases</td><td>Overconfidence biases</td></tr><tr><td>Availability biases</td><td>Processing biases</td><td>Statistical biases</td><td>Interest biases</td><td>Availability biases</td></tr><tr><td rowspan="5">Adjustment &amp; Anchoring biases</td><td>Output biases</td><td>Confidence biases</td><td>Pattern recognition biases</td><td>Representativeness biases</td></tr><tr><td>Feedback biases</td><td>Adjustment biases</td><td>Stability biases</td><td>Confirmation biases</td></tr><tr><td></td><td>Presentation biases</td><td>Social biases</td><td>Bounded Awareness</td></tr><tr><td></td><td>Situation biases</td><td></td><td>Framing biases</td></tr><tr><td></td><td></td><td></td><td>Escalation biases</td></tr><tr><td colspan="5">Number of biases in typology:</td></tr><tr><td>15 biases</td><td>37 biases</td><td>37 biases</td><td>17 biases</td><td>23 biases</td></tr></table>

## 3.2.2. Cognitive biases

While general heuristics are a source of efectiveness in human decision making, they are subject to cognitive processes that can lead to poor decisions and, in some rare cases, catastrophic failure. These processes are the second part of the heuristics and bias part of BE - biases. Cognitive biases are cognitions or mental behaviors that prejudice decision quality in a significant number of decisions for a significant number of people; they are inherent in human reasoning. In the literature, these efects are often termed decision biases or judgment biases. Tversky and Kahneman [56] viewed biases as failures of general heuristics: “…they (heuristics) occasionally lead to errors in prediction or estimation.” An important word in the quotation is “occasionally” and the key issue is knowing when a particular bias is likely to ad versely afect a particular decision. Ceteris paribus biases are likely to afect complex decisions with time pressure and decisions that are new to the decision maker. This means that as Das and Teng [82] related “cognitive biases are systematically associated with strategic decision processes”.

There is insuficient space in this paper to adequately describe the dozens of biases that have been discovered in psychology and BE experiments. The heuristics and biases body of work is partly summarized in the article collections Kahneman, Slovic, and Tversky [83], Kah neman and Tversky [84], and Gilovich, Grifen, and Kahneman [85]. To provide an example of the action of biases the following provides a description of one bias that is important for IS – the confirmation bias. The confirmation bias acts against a fundamental principle of the scientific method, which holds that information that refutes a hypothesis is more valuable than information that supports it. However, under the confirmation bias, people tend to search for information that confirm their hypotheses and gloss over, or even actively ignore, disconfirming information ([64,86], ch. 3). Arnott [6] studied a decision in a services company that was subject to the confirmation bias. The Board, on the advice of the CEO, had made a prima facie decision to close a division of the company. The various information flows concerning the decision that the CEO and Directors received were analyzed and all but one were confirming in nature – they supported closure of the division. This information included formal financial statements, financial analyses and forecasts, and a detailed consultant's report. The one information flow that was not confirming was neutral; it provided no confirming or disconfirming information. The CEO and management were educated about the nature and efect of the confirmation bias and a search for disconfirming information was undertaken. Because of this new information and further analyses, the decision to close the division was reversed and the adverse efect of the confirmation bias was avoided. While the services company decision is organizational in scope, the confirmation bias can also afect a wide range of personal decisions.

Because a large number of biases have been identified in the literature it can be dificult to operationalize this theory in practice. This situation is further exacerbated by researchers using diferent and confusing names for a bias and the possible overlap and interaction between biases. For example, the confirmation bias described above has been termed the confirmation trap [64], selective perception [87], and the desire for self-fulfilling prophecies [88]. One strategy to aid the overall understanding of the range of cognitive biases has been to develop typologies of biases, examples of which appear in Table 4.

Tversky and Kahneman [56] classified biases by the three general judgment heuristics. Bazerman and Moore [64] followed a similar approach but argued for the primacy of overconfidence biases: “overconfidence efects are some of the most potent, pervasive, and pernicious of any of the biases …” (p.14). Bazerman and Moore's typology is aimed managers and senior professionals. Hogarth's [87] typology is ordered according to his general model of decision making. The Lovallo & Sibony [89] typology is from a McKinsey & Co report and is aimed at management consulting. Finally, the typology of Arnott ([6] Table 1) was developed specifically for systems analysis in DSS development projects. These typologies collectively ofer DSS researchers a portal into cognitive bias research.

## 3.2.3. Prospect theory: how humans make risky decisions

Various aspects of BE, dual processes and heuristics and biases, can be combined to create theories of human behavior in decision making situations. The most notable of these theories is prospect theory [57]. Thaler [60] related “Prospect theory is, of course, the seminal evidencebased theory in behavioral economics.” Prospect theory is a descriptive theory of decision making in risky situations. Further, it enables pre dictions of decision-making behavior. Fig. 2 shows prospect theory's value function. Each individual will have a diferent shape to their value function, but Fig. 2 portrays the most common shape based on empirical studies. The horizontal axis in Fig. 2 measures the monetary gains or losses that follow a decision relative to a reference or starting point. The vertical axis measures the psychological value that a gain or a loss yields to an individual. In Fig. 2, segments 2 and 4 represent risk seeking behavior and segments 1 and 3, risk avoidance. The dashed line in Fig. 2 is what standard economic theory (EU) posits as the situation for making risky decisions. On the dashed line decision makers treat the value of losses and gains equally; the line represents risk neutrality.

![](/api/attachments/YX8UBM2E/fulltext/images/6e8aa183273669fa76e1a6306be1553b58acd3e45dd0bf9b6f522a59ef6c2f52.jpg)  
Fig. 2. A value function from prospect theory.

The S-shaped value function shows the empirical results of Kahneman and Tversky's experimental studies. Three cognitive features, all operating characteristics of System 1, are the foundation of prospect theory ([59], p. 281–2). They are: 1. Evaluation is relative to a neutral reference point. This point defines what is a gain and what is a loss; 2. There is diminishing sensitivity to both increasing values and increasing gains or losses; and 3. Losses loom larger than gains in decision maker's minds. Risk seeking is the dominant behavior when assessing losses (segment 4) while risk avoidance is the dominant pattern when assessing gains (segment 1). As Camerer and Loewenstein [4] related “Prospect theory … explains experimental choices more accurately than EU because it gets the psychophysics of judgment and choice right.” Prospect theory is BE's alternative to expected utility theory.

## 3.2.4. Nudges

Nudging is not a theory of decision making but rather a strategy and process to use BE in an organization or government setting. Nudges are based on the action of dual process theory especially where the action of System 1 overwhelms System 2 in a negative way. Nudges are argued to be needed to lead people to superior decision outcomes because of the inherent flaws of human decision making, that is, the negative consequence of cognitive biases. The concept of nudges was developed by Thaler and Sunstein [61] who defined a nudge as “any aspect of the choice architecture that alters people's behavior in a predictable way without forbidding any options or significantly changing their economic incentives” (p. 6). Unfortunately, Thaler and Sunstein do not explicitly define “choice architecture” but its implied meaning is the context, structure, content, and processes of a decision situation. Thaler and Sunstein [61] argued “… people will need nudges for decisions that are dificult and rare, for which they don't get prompt feedback, and when they have trouble translating aspects of the situation into terms that they can easily understand.” Johnson et al. [90] provides a catalog of tools that can be used to afect a choice architecture while Thaler, Sunstein, and Balz [91] provide a concise summary of the six principles of an efective choice architecture.

Perhaps the most famous example of a nudge is changing the level of peoples' pension savings in a positive way by altering the default on employment contracts from opt-in to opt-out. Opt-in requires efort to commence or change pension saving and decision inertia can mean that people do not take the efort to opt-in. Opt-out requires no efort to engage in pension savings and significantly benefit employees in the future. The explicit use of the nudge strategy has been most prominent in government. In 2008 Sunstein (of Thaler and Sunstein) was appointed to head the White House Ofice of Information and Regulatory Afairs (OIRS) by President Obama. This ofice was charged with using a BE informed approach to government action. In 2010, on the other side of politics, a conservative UK government established the Behavioral Insights Team (BIT) in 10 Downing Street with a similar brief to OIRS. BIT is credited with saving many millions of pounds of government revenue and significantly changing citizen behavior towards better personal outcomes [92].

There has been some criticism of the nudge strategy. For example, Hausman and Welch [93] are highly critical of the political philosophy that Thaler and Sunstein espoused as the guiding principle behind nudges – libertarian paternalism ([61], ch. 1). They also strongly criticized what they believe to be the overly negative framing of human decision making that is portrayed by behavioral economists.

## 4. Behavioral economics in decision support systems research

The previous two major sections have provided an understanding of the complex web of theories, methods, and efects that is BE. This section takes this understanding to first provide an overview of the use of BE in DSS research over time, and second to identify potential areas and topics for BE-founded DSS research.

## 4.1. An overview of the use of behavioral economics in DSS research

There are some literature reviews that shed light on aspects of BE usage. In addition, there are some clear examples of the use of BE as a foundation for DSS research. Collectively, these articles can provide some insight into the use of BE in DSS research. As part of a longitudinal 21-year review of general DSS research, Arnott and Pervan [11] found that researchers were slowly shifting between early and contemporary BE as a reference discipline. At the end of their article sample in 2010, less than half of citations were to contemporary BE; Simon's theories, especially the phase model, still dominated DSS research. This position is surprising given that at the start of the analysis Tversky and Kahneman's work had been well known for around 20 years.

There are no detailed literature reviews of the use of the various aspects of BE in DSS research but there are two reviews of the use of BE in general IS. First, Fleischmann et al. [94] conducted a review of the use of cognitive biases in general IS research. Their article selection strategy did not include judgment heuristics, prospect theory, or multiple bias efects (for example, escalation to commitment). They focused on the terms “biases” and “non-rational behavior” for article selection and identified 84 articles from 1992 to 2013 that used biases in their research and found that the use of biases in IS research has been steadily increasing over time. Their analysis showed that framing [57] and anchoring [95] were the most popular biases in IS research. Most of the IS articles that Fleischmann et al. reviewed used experiments as their research strategy. The second general IS and BE literature review, Odnor and Oinas-Kukkonen [96], analyzed a wider range of aspects of BE in the Basket of Eight journals<sup>4</sup> from 2006 to 2014. Their article selection criteria of experiments and experiment-like surveys yielded a BE-using sample of 15 articles. They found significant diversity in the small sample with the main focus being Ecommerce, and recommender systems in particular. They argued that BE could have impact on studies on systems design and use but did not mention DSS explicitly.

Although these literature reviews have found that BE has had modest use as a foundation theory in DSS and IS research, there are examples of high quality relevant DSS research that use BE in a major way, that is, where BE is integral to the design and execution of the research. Table 5 shows 25 examples of the use of specific aspects of contemporary BE in DSS research over time. Some articles in the table were sourced from DSS articles in the general IS samples used by Fleischmann et al. [94] and Odnor and Oinas-Kukkonen [96]. The other articles were sourced by keyword searches of journal databases. The table is ordered by publication date and spans 30 years of DSS research from 1989 to 2019. All articles except Lim and Benbasat [101] were published in A\* journals,<sup>5</sup> a major indicator of publishing quality. As a result. Table 5 represents a representative set of quality DSS research that used BE in a major or integral way. Notably, 15 of the 25 articles in the table were published in the journal DSS.

Table 5  
Examples of the major use of behavioral economics in DSS research.

<table><tr><td>Article</td><td>BE Theory aspect</td><td>Decision support area</td><td>Research strategy</td><td>Decision task</td></tr><tr><td>Jacob, Moore, &amp; Whinston [97]</td><td>Bounded rationality. Heuristics</td><td>DSS theory</td><td>Conceptual study</td><td>Any</td></tr><tr><td>Kottemann, Davis, &amp; Remus [98]</td><td>Cognitive bias: Illusion of control</td><td>DSS use - scheduling</td><td>Experiment</td><td>Tactical</td></tr><tr><td>Remus &amp; Kottemann [99]</td><td>Cognitive bias: Anchoring</td><td>DSS use - Scheduling</td><td>Experiment</td><td>Operational</td></tr><tr><td>Roy &amp; Lerch [100]</td><td>Cognitive bias: base rate fallacy</td><td>DSS use -information presentation</td><td>Experiment</td><td>Operational</td></tr><tr><td>Lim &amp; Benbasat [101]</td><td>Heuristics: availability, representativeness</td><td>Group support systems</td><td>Design science</td><td>Tactical</td></tr><tr><td rowspan="2">van Bruggen, Smidts, &amp; Wierenga [102]</td><td>Dual process theory</td><td>Marketing decision support</td><td>Experiment</td><td>Tactical</td></tr><tr><td>Cognitive bias: Anchoring</td><td></td><td></td><td></td></tr><tr><td>Kahai, Solieri, &amp; Felo [103]</td><td>Cognitive bias: Illusion of control</td><td>DSS use - strategic decision</td><td>Experiment</td><td>Strategic</td></tr><tr><td>George, Duffy, &amp; Ahuja [104]</td><td>Cognitive bias: Anchoring</td><td>DSS use - house purchase</td><td>Experiment</td><td>Tactical</td></tr><tr><td rowspan="2">Chen &amp; Lee [105]</td><td>Heuristic: availability</td><td>DSS use -executive decision making</td><td>Design science</td><td>Tactical</td></tr><tr><td>Cognitive biases: confirmation, overconfidence, anchoring</td><td></td><td></td><td></td></tr><tr><td>Arnott [6]</td><td>Cognitive bias: confirmation</td><td>DSS use - executive decision making</td><td>Design science</td><td>Strategic</td></tr><tr><td>Jones et al. [106]</td><td>Cognitive bias: Anchoring</td><td>DSS use - Credit assessment</td><td>Experiment</td><td>Tactical</td></tr><tr><td>Hosack [107]</td><td>Cognitive bias: Framing</td><td>DSS use - Fund allocation</td><td>Experiment</td><td>Operational</td></tr><tr><td rowspan="2">Bhandari, Hassanein, &amp; Deaves [7]</td><td>Heuristic: Representativeness</td><td>DSS aid -Investment decisions</td><td>Experiment</td><td>Tactical</td></tr><tr><td>Cognitive bias: Framing</td><td></td><td></td><td></td></tr><tr><td>Kuo, Hsu, &amp; Day [108]</td><td>Cognitive bias: Framing</td><td>DSS theory</td><td>Experiment</td><td>Tactical, strategic</td></tr><tr><td>Looney &amp; Hardin [109]</td><td>Prospect theory</td><td>DSS design</td><td>Field experiment</td><td>Tactical</td></tr><tr><td>Watts, Shankaranarayanan, &amp; Even [110]</td><td>Dual process theory</td><td>DSS use - Advertising campaign</td><td>Experiment</td><td>Operational</td></tr><tr><td>Cheng &amp; Wu [111]</td><td>Cognitive bias: Framing</td><td>DSS use - Translation</td><td>Experiment</td><td>Operational</td></tr><tr><td>Huang, Hsu, &amp; Ku [9]</td><td>Cognitive bias: Confirmation</td><td>Debiasing with a DSS</td><td>Experiment</td><td>Tactical</td></tr><tr><td>Tan, Tan, &amp; Teo [112]</td><td>Cognitive bias: Overconfidence</td><td>Ecommerce decision aid</td><td>Experiment</td><td>Operational, tactical</td></tr><tr><td>Piramuthu et al. [113]</td><td>Cognitive biases: Sequential bias, Positivity bias</td><td>Recommender system</td><td>Conceptual study</td><td>Operational</td></tr><tr><td>Chen &amp; Koufaris [114]</td><td>Cognitive bias: Overconfidence</td><td>DSS use - Investment decision</td><td>Experiment</td><td>Operational</td></tr><tr><td>Arnott, Lizama, &amp; Song [115]</td><td>Dual process theory</td><td>Business intelligence</td><td>Secondary Data</td><td>Operational, tactical</td></tr><tr><td>Feris, Zwikael, &amp; Gregor [116]</td><td>Dual process theory</td><td>DSS development and use</td><td>Design science</td><td>Tactical</td></tr><tr><td>Kretzer &amp; Maedche [117]</td><td>Nudges</td><td>Business intelligence</td><td>Experiment</td><td>Operational</td></tr><tr><td>Ahsen, Ayvaci, &amp; Raghunathan [118]</td><td>Cognitive biases: Anchoring Confirmation, Ease of recall</td><td>Clinical decision support - Breast cancer diagnosis</td><td>Design science</td><td>Tactical, strategic</td></tr></table>

Table 5 shows that the use of BE has a long history in DSS research. The decision tasks that were studied in Table 5 are split between operational (n = 10, 40%), tactical decisions (n = 14, 56%) and a small number of strategic decisions (n = 4, 16%). This is a diferent distribution to general DSS research which has 68% operational decision support ([11], Table 16) and implies that BE-using DSS research is addressing tasks that are very significant to organizations. The articles in Table 5 all adopted a positivist philosophy of knowledge. This is both diferent to general IS, 81% positivist [119] and all DSS, 92% [120]. This philosophic orientation is a reflection of the strongly positivist nature of BE foundation research.

The BE aspects utilized in the DSS articles in Table 5 show a concentration on dual process theory (4 articles) and five biases - anchoring (n = 6), confirmation (n = 4), framing (n = 4), overconfidence (n = 3), and illusion of control (n = 2). The other theories, methods, and biases feature in only one article each. This represents a relatively shallow use of available BE theory in the article sample.

The research methods identified in Table 5 also show a diferent pattern to both general IS and DSS research. The details are shown in Table 6 which compares the BE-using DSS research in Table 5 with the most recent analyses of all IS and DSS. What stands out in Table 6 is the overwhelming use of experimental methods, around three times more than general DSS and six times more than general IS. This use of experiments, however, is similar to the pattern of methods in BE; it is a field dominated by experiments and field studies. It is understandable that IS researchers who are skilled at experimentation would be attracted to reference theory that uses experiments. Further, some BE papers can be dificult reading and to understand them requires a command of experimental methods and techniques. Another surprising situation in Table 6 is the lack of any survey or case study research. Survey research has long been the dominant IS quantitative method and case studies the dominant qualitative method; they are important to DSS research. It could be the case, as suggested above, that DSS researchers are mirroring the BE reference discipline's method.

## 4.2. Potential areas for the use of behavioral economics in DSS research

Table 7 shows a number of areas and topics in DSS research that have the potential to significantly benefit from the use of BE as reference theory. First, it is clear from Table 5 that heuristics and biases are the most used aspect of BE in DSS research. Dual process theory is increasing in use and prospect theory and nudging are emerging as reference theory. There is a danger that some biases may become over represented in DSS research. For example, in Table 5 anchoring is the most used BE foundation theory, closely followed by confirmation and framing. Recall from Table 4 that there are around 37 biases in the BE literature. A single-bias focus could be an artifact of DSS researchers educating themselves in the detailed background of a particular bias.

Table 6  
Research methods in DSS research with a major use of behavioral economics.

<table><tr><td>Research method</td><td>BE using DSS % (Table 5)</td><td>All DSS % [11]</td><td>All IS % [119]</td></tr><tr><td>Experiment</td><td>64</td><td>23</td><td>10</td></tr><tr><td>Field study</td><td>4</td><td>3</td><td>1</td></tr><tr><td>Survey</td><td>0</td><td>7</td><td>22</td></tr><tr><td>Case study</td><td>0</td><td>8</td><td>20</td></tr><tr><td>Action research</td><td>0</td><td>&lt; 0.5</td><td>2</td></tr><tr><td>Design science</td><td>20</td><td>36</td><td>45</td></tr><tr><td>Descriptive study</td><td>0</td><td>6</td><td></td></tr><tr><td>Secondary data</td><td>4</td><td>1</td><td></td></tr><tr><td>Conceptual study</td><td>8</td><td>15</td><td></td></tr><tr><td>Literature review</td><td>0</td><td>2</td><td></td></tr></table>

After a researcher has invested a large amount of time in understanding all aspects of a bias, they are more likely to use that bias as foundation theory in a research project even if alternative BE theory candidates are available. There is some danger in only using one bias as foundation theory as biases often overlap and interact. This interaction could be lost in single-bias experimentation. Deciding which heuristic or bias is the appropriate descriptive decision-making aspect to focus on in an DSS research project is itself a dificult decision. The bias typologies identified in Table 4 can provide important input for this decision. The wider bias set represents rich opportunities for many DSS projects.

BE has provided two main strategies or methods for improving decision outcomes – nudging, which was described in Section 3.2.4, and debiasing. The strategy of nudging and designing choice architectures has been slow to enter DSS research, although this could be changing. In a sense nudging builds on, or is aligned with, the theory of decision restrictiveness that originated in DSS [121–123]. A recent example of nudging in DSS research is Kretzer & Maedche [117] who investigated nudging in a laboratory experiment in a BI context. Outside the laboratory, nudges can have significant potential as an organizing strategy in DSS design science and action research. There are five design science projects mentioned in Table 5 and it is possible they could have benefited by using nudging as part of their project design.

Debiasing is a process whereby the negative consequences of a cognitive bias are reduced or mitigated. There are a number of methods that can be used to undertake debiasing [124,125]. Debiasing requires the DSS analyst to understand the mechanisms underlying the particular bias that is subject of change. Each bias can have a diferent debiasing approach and this makes debiasing dificult in practice as this requires significant efort from the analyst. In Table 5, Arnott [6], Bhandari, Hassanein, and Deaves [7], and Cheng and Wu [111] are examples of the explicit use of a DSS as an integral part of debiasing a decision.

As mentioned above in Section 4.1, the lack of case study research in Table 6 both surprising and an opportunity. Case studies have been slowly declining since 1990 as a fraction of DSS research ([11], Table 4) but occupy a large share of IS research (see Table 6). Case studies can illuminate the nature of IS/IT phenomena in ways that are not possible with experiments and surveys. The use of descriptive BE theory in DSS case studies, particularly exploratory case studies that aim for deep understanding of a decision support process, method, or instantiation, could lead to a significant increase in our knowledge of DSS phenomena. Table 6 also showed a lack of BE founded survey research. Survey-based research informed by BE constructs are an obvious direction for DSS research. They could be particularly useful in reconnaissance style research that explores a topic and organizes ideas before undertaking experimental and field research.

Business intelligence (BI) systems are large-scale decision support systems (DSS). According to studies by industry analyst Gartner Inc., BI has been the top technology priority for CIOs throughout this century [126] while Kappelman et al. [127] found that BI is the largest IT expenditure in organizations world-wide. Arguably BI is the most important DSS to research in current organizations and BE theories can provide foundation theories for such studies. An important aspect of this BI research could be studying the behavior of a large number of decision makers using a single system. Two articles in Table 5 have studied BI using dual process theory and nudges.

Two developing areas for the future of BE and DSS also feature in Table 7 – neuroeconomics and cognitive computing. Studies in the relatively new research area of neuroeconomics have investigated brain activity while subjects are undertaking decision tasks [128]. Although the dual process theory does not require physical proof of its existence to be an efective foundation of BE, the neuroscience research on dual processes is encouraging and could eventually lead to significant theoretical insights. Neuroscience is making similar inroads into IS research [129] and has much to ofer DSS. BE informed neuro-DSS could involve studies of decision making supported by various classes of DSS while participants are monitored by functional MRI and EEG devices. The second emerging DSS area, cognitive computing, involves the use of AI in DSS. This new generation of technologies and their relevance to DSS have been described by Watson [130]. Watson focused on the technological and prescriptive aspects of decision support with cognitive computing, but the descriptive theories of BE may assist with the development of the cognitive generation of DSS in organizations, especially in understanding how these technologies afect decisionmaking processes.

Table 7  
Potential Use of BE in DSS Research.

<table><tr><td>Research topic or area</td><td>Description</td></tr><tr><td>Utilizing the bias set</td><td>DSS research has only utilized a small sub-set of the cognitive biases identified by BE research. Greater knowledge of what biases exist and their action could expand the phenomena that DSS researchers investigate.</td></tr><tr><td>Design science nudges</td><td>Nudges based on relatively small field experiments can be the theory foundation for the use of a DSS artifact in an organizational setting.</td></tr><tr><td>Debiasing (improving decision outcomes)</td><td>DSS can be used as the vehicle for an explicit debiasing strategy for important decisions. This involves educating decision makers about the action of one or more cognitive biases.</td></tr><tr><td>DSS use case studies</td><td>Case studies can illuminate the deep structure of phenomena more effectively than other methods. Case studies are common in DSS research but the use of BE as a theory foundation in case studies has been modest.</td></tr><tr><td>DSS surveys</td><td>Survey research informed by BE constructs could be especially useful early in a DSS project. This research could provide a foundation and ideas for further investigations using other research methods.</td></tr><tr><td>BI use</td><td>BI systems can support many decisions for many decision makers. Researching this radically different DSS context can benefit from most aspects of BE theory.</td></tr><tr><td>Neuro DSS research</td><td>The methods and findings from the relatively new field of neuroeconomics could have a profound impact on DSS research. This area could involve studies of decision making supported by various classes of DSS while participants are monitored by functional MRI and EEG devices.</td></tr><tr><td>Cognitive DSS</td><td>Research in the AI-based cognitive computing area has been mainly prescriptive and technology focused. BE-based decision support research could focus on the decision-making processes of the users of these systems.</td></tr><tr><td>Senior executive decision support</td><td>DSS has been relatively unsuccessful in supporting senior executives. The dual process theory provides a theory foundation for both studying and developing systems for these unique users.</td></tr><tr><td>Recommender systems</td><td>Recommender systems have become integral to social media and Ecommerce. They predict what a consumer may wish to consume in the future. Such systems are subject to a host of biases and BE could help research in this area.</td></tr></table>

There are other aspects of DSS research could benefit from a BE foundation. An under-researched area that could benefit from a BE theory foundation is the study of senior executive information behaviors [131]. Dual process theory and the action of System 1 decision making could be a focus of this work. Further, Goes [132] in an MIS Quarterly editorial suggested inter alia recommender systems as a potential area for BE in IS research. Recommender systems, in a sense, form the intersection between Ecommerce and DSS. Piramuthu, Kapoor, Zhou, & Mauw [113] is an example of the use of BE to investigate the decision support aspects of recommender systems.

The areas of BE and DSS identified and discussed in this section only represent a preliminary analysis. Armed with the rich set of BE reference theory DSS researchers will find many other productive uses of the theory.

## 5. Concluding comments

It is axiomatic that DSS research should be grounded in the most scientifically valid foundation theory. Descriptive theories of decision making are particularly important for DSS research; they sit beside and are complementary to, the prescriptive theories of neoclassical economics. Beginning with [15] article on bounded rationality BE has blossomed into a complex web of theories that describes human decision making. Given the current dominant status of BE in human decision-making research it is hard to imagine why an DSS project that takes a descriptive view of decision making would not consider using BE in some way. It is important for DSS researchers to understand that BE is much more than a set of heuristics and biases and that theories and methods like the dual process theory, prospect theory, and nudging hold significant potential for DSS research. This paper has viewed BE from the perspective of DSS research with the aim of encouraging its use in DSS.

Using a complex theory base like BE for DSS research can be subject to limitations. Taking foundation theory from another field places a responsibility on researchers to keep up to date with debates, controversies, and developments in the foundation discipline. It is not suficient to adopt a foundation theory at a particular point in time and then cease engagement with the area. This can lead to foundation knowledge obsolescence. An example of major change in BE foundation theory is the status of anchoring and adjustment. Originally conceived as a fundamental judgment heuristic by Kahneman and Tversky in the 1970s, in the early 2000s its place as a judgment heuristic was taken by the afect heuristic and anchoring and adjustment was reconceived as a cognitive bias. Nevertheless, some research still uses anchoring and adjustment as a heuristic. It is an onerous but necessary task of DSS researchers who use descriptive decision theory to maintain currency with BE developments.

In conclusion, the dominant descriptive decision-making theories of BE have a long history in DSS research although the use of BE has been relatively modest. BE is a complex set of sometimes overlapping theories, methods, and efects that describe decision making at diferent levels of abstraction. BE is also a field with two major generations of theory, generations which co-exist in DSS research. It can be dificult to conceive the contemporary BE field because of this complexity, and also because concepts and efects often have diferent terms in the psychology and BE literature. This paper provides an insight into this complex theory landscape from the perspective of DSS researchers and provides suggestions for areas where BE may be particularly useful for DSS research.

## References

[1] G.J. Browne, J. Parsons, More enduring questions in cognitive IS research, Journa of the Association for Information Systems 13 (12) (2012) 1000–1011.

[2] C.L. Gardner, J.R. Marsden, D.E. Pingry, The design and use of laboratory experiments for DSS evaluation, Decision Support Systems 9 (4) (1993) 369–379

[3] J.R. Marsden, D.E. Pringy, Theory of decision support systems portfolio evaluation, Decision Support Systems 9 (1993) 183–199.

[4] C.F. Camerer, G. Loewenstein, Behavioral economics: Past, present, future, in: C.F. Camerer, G. Loewenstein, M. Rabin (Eds.), Advances in Behavioral Economics, Princeton University Press, Princeton, NJ, 2003, pp. 3–51.

[5] K. Chapman, L.E. Pike, Literature on behavioral economics, part 1: introduction and books. Behavioral & Social Sciences Librarian 32 (4) (2013) 205–223

[6] D. Arnott, Cognitive biases and decision support systems development: a design science approach, Information Systems Journal 16 (1) (2006) 55–78.

[7] G. Bhandari, K. Hassanein, R. Deaves, Debiasing investors with decision support systems: an experimental investigation, Decision Support Systems 46 (2008) 399–410.

[8] J.J. Elam, S.L. Jarvenpaa, D.A. Schkade, Behavioral decision theory and DSS: New opportunities for collaborative research, in: E.A. Stohr, B.R. Konsynski (Eds.), Information Systems and Decision Processes, IEEE Computer Society Press, Los Alamitos. CA. 1992, pp. 51–74.

[9] H.-H. Huang, J.S.-C. Hsu, C.-Y. Ku, Understanding the role of computer-mediated counter-argument in countering conformation bias. Decision Support Systems 53 (2012) 438–447.

[10] A.A. Angehrn, T. Jelassi, DSS research and practice in perspective, Decision Support Systems 12 (1994) 257–275.

[11] D. Arnott, G. Pervan, A critical analysis of decision support systems research revisited: the rise of design science, Journal of Information Technology 29 (2014) 269-293.

[12] S. Dasgupta, Multidisciplinary creativity: the case of Herbert Simon, Cognitive Science 27 (2003) 683–707.

[13] H.A. Simon, On simulating Simon, his monomania, and its sources in bounded rationality, Studies in the History and Philosophy of Science Part A 32 (2001) 501–505.

[14] H.A. Simon, Administrative Behavior, 4th ed., The Free Press, New York, 199 (First published 1945.).

[15] H.A. Simon, A behavioral model of rational choice, Quarterly Journal of Economics 69 (1955) 99–118

[16] H.A. Simon, Theories of decision-making in economics and behavioral science, The American Economic Review 49 (3) (1959) 253–283

[17] H.A. Simon, Information processing models of cognition, Annual Review of Psychology 30 (1979) 363–396.

[18] H.A. Simon, The behavioral and social sciences, Science 209 (1980) 72–78.

[19] A. Newell, A.J. Perlis, H.A. Simon, What is computer science? Science 157 (1967) 1373–1374.

[20] A. Newell, H.A. Simon, Computer science as empirical inquiry: symbols and search. [1975 ACM Turing award lecture.]. Communications of the Association for Computing Machinery 19 (3) (1976) 113–126

[211 H.A, Simon, What computers mean for man and society, Science 195 (1977) 1186-1191

[22] A. Newell, J.C. Shaw, A. Simon, A variety of intelligent learning in a general problem solver, in: M.C. Ovits, S. Cameron (Eds.), Self-Organizing Systems: Proceedings of an Interdisciplinary Conference, Pergamon Press, New York, 1960, pp. 153–189.

[23] A. Newell, H.A. Simon, Computer simulation of human thinking, Science 134 (1961) 2011–2017.

[24] A. Newell, H.A, Simon, Human Problem Solving, Prentice-Hall, Englewood Clif NJ. 1972.

[25] H.A. Simon, The axiomatization of physical theories, Philosophy of Science 37 (1970) 16–26.

[26] H.A. Simon, Reason in Human Affairs, Stanford University Press, Stanford, CA 1983.

[27] H.A. Simon, The theory of scientific discovery, in: J. Goetschl (Ed.), Revolutionary Changes in Understanding Man and Society, Kluwer Academic Publishers. Amsterdam, 1995, pp. 55–73.

[28] K.A. Ericsson, H.A. Simon, Protocol Analysis: Verbal Reports as Data, rev. ed., Th MIT Press, Cambridge, MA, 1993.

[29] H.A. Simon, The Sciences of the Artificial, MIT Press, Cambridge, MA, 1969.

[30] J.G. March, H.A. Simon, Organizations, Wiley, New York, 1958.

[31] H.A. Simon, The New Science of Management Decision, Harper, New York, 1960.

[32] H.A. Simon, Bounded rationality and organizational learning, Organization Science 2 (1991) 125–134

[33] H.A. Simon, Computers in education: realizing the potential. American Educatior (December) (1983) 17–23

[34] H.A. Simon, What we know about learning, Journal of Engineering Education 87 (4) (1998) 343–348.

[35] J. von Neumann, O. Morgenstern, Theory of Games and Economic Behavior, Princeton University Press. Princeton, NJ. 1944

[36] A. Smith, An Inquiry into the Nature and Causes of the Wealth of Nations, Penguin edition, Penguin Books, Harmondsworth, UK, 1776 (published 1970).

[37] D. Ross, Psychological versus economic models of bounded rationality, Journal of Economic Methodology 21 (4) (2014) 411–427.

[38] JM. Kevnes. The General Theory of Employment. Interest and Money. Macmillar and Co. London. 1960 (First published 1936.)

[39] G.A. Akerlof, R.J. Shiller, Animal Spirits: How Human Psychology Drives the Economy, and Why it Matters for Global Capitalism, Princeton University Press, Princeton. NJ. 2009.

[40] J. Dewey, How we Think, Health, New York, 1933 (Originally published 1910).

[41] H. Mintzberg, D. Raisinghani, A. Theoret, The structure of ‘unstructured’ decision processes, Administrative Science Quarterly 21 (2) (1976) 246–275.

[42] R.N. Anthony, Planning and Control Systems: A Framework for Analysis, Harvard University Press, Boston, 1965.

[43] R. Lipschitz, O. Bar-Ilan, How problems are solved: reconsidering the phase theorem, Organizational Behavior and Human Decision Processes 65 (1) (1996) 48–60.

[44] D. Kahneman, Maps of bounded rationality: A perspective on intuitive judgment and choice, Nobel Prize in Economic Sciences Lecture, 2002 Retrieved May 25, 2015 from http://www.nobelprize.org/nobel\_prizes/economic-sciences/ laureates/2002/kahnemann-lecture.pdf.

[45] R.H. Thaler, Toward a positive theory of consumer choice, Journal of Economic Behavior and Organization 1 (1) (1980) 39–60.

[46] G. Klein, R. Calderwood, A. Clinton-Cirocco, Rapid decision making on the fire ground: the original study plus a postscript. Journal of Cognitive Engineering and Decision Making 4 (3) (2010) 186–209.

[47] G. Klein, Sources of Power: How People Make Decisions, MIT Press, Cambridge, MA, 1999.

[48] G. Klein, The Power of Intuition: How to Use Your Gut Feelings to Make Bette Decisions at Work, Currency-Doubleday, New York, 2004.

[49] D. Kahneman, G. Klein, Conditions for intuitive expertise: a failure to disagree, American Psychologist 64 (2009) 515–526.

[50] G. Gigerenzer, Adaptive Thinking: Rationality in the Real World, Oxford University Press, New York, 2000.

[51] G. Gigerenzer, R. Selten, Bounded Rationality: The Adaptive Toolbox, MIT Press, Cambridge, MA, 2001.

[52] G. Gigerenzer, Risk Savvy: How to Make Good Decisions, Allen Lane, London, 2014.

[53] J.L. Cohen, W.T. Dickens, The role of nature versus nurture in determining economic outcomes: the foundations of behavioral economics, American Economic Review 92 (2) (2002) 335–338

[54] Fox, J. (2015). A short history of modern decision making: from “economic man” to behavioral economics. Harvard Business Review, May, 79–85.

[55] A. Tversky, D. Kahneman, Availability: a heuristic for judging frequency and probability. Cognitive Psychology 5 (1973) 207–232

[56] A. Tversky, D. Kahneman, Judgment under uncertainty: heuristics and biases, Science 185 (1974).1124–1131

[57] D. Kahneman, A. Tversky, Prospect theory: an analysis of decision under risk, Econometrica 47 (1979) 263–291.

[59] D. Kahneman, Thinking Fast and Slow, Farrar, Straus and Giroux, New York, 2011.

[58] A. Tversky, D. Kahneman, The framing of decisions and the psychology of choice, Science 211 (1981) 453–458

[60] R.H. Thaler, Misbehaving: The Making of Behavioral Economics, W.W. Norton & Company, New York, 2015.

[61] R.H. Thaler, C.R. Sunstein, Nudge: Improving Decisions about Health, Wealth, and Happiness (rev. ed.), Penguin Books, London, 2009.

[62] D. Ariely, Predictably Irrational: The Hidden Forces That Shape Our Decisions, rey, exp, ed., Harper Perennial. New York. 2010 (First published 2008.).

[63] D. Ariely. The Upside of Irrationality. Harper Perennial. New York. 2010.

[64] M. Bazerman. D. Moore, Judgment in Managerial Decision Making, 8th ed., Johr Wilev & Sons. Hoboken. NJ. 2013

[65] A. Morris, Behavioural Economics for Dummies, John Wiley & Sons, Mississauga, Ontario. Canada. 2012

[66] D. Kahneman, S. Frederick. Representativeness revisited: attribute substitution in intuitive judgment, in: T. Gilovich. D. Griffin, D. Kahneman (Eds.). Heuristics and Biases: The Psychology of Intuitive Judgment, Cambridge University Press, New York, 2002, pp. 49–81.

[67] J.StB.T Evans, Dual-processing accounts of reasoning, judgment, and social cognition, Annual Review of Psychology 59 (2008) 255–278.

[68] S.A. Sloman, The empirical case for two systems of reasoning, Psychological Bulletin 119 (1) (1996) 3–22

[69] K.E. Stanovich, R.F. West, Individual differences in reasoning: implications for the rationality debate, Behavioral and Brain Sciences 23 (5) (2000) 645–665

[70] S. Chaiken, Heuristic versus systematic information processing and the use of source versus message cues in persuasion, Journal of Personality and Social Psychology 39 (5) (1980) 752–766.

[71] R. Deutsch, F. Starck, Duality models in social psychological: from dual processe to interacting systems, Psychological Inquiry 17 (3) (2006) 166–172.

[72] J.StB.T Evans, In two minds: dual-process accounts of reasoning, Trends in Cognitive Sciences 7 (10) (2003) 454–459.

[73] A. Dijksterhuis, M.W. Bos, L.F. Nordgren, R.B. van Baaren, On making the right choice: the deliberation-without-attention effect, Science 311 (2006) 1005–1007

[74] Reyna, How people make decisions that involve risk: a dual-processes approach, Current Directions in Psychological Science 13 (2) (2004) 60–66

[75] E. Winter. Feeling Smart: Why our Emotions Are more Rational than we Think Public Afairs, New York, 2014.

[76] G. Klein, Naturalistic decision making, Human Factors 50 (3) (2008) (456-450).

[77] J. Kruger, D. Wirtz, L. Boven, T. Altermatt, The effort heuristic, Journal of Experimental Social Psychology 40 (2004) 91–98.

[78] D.G. Goldstein, G. Gigerenzer, Models of ecological rationality: the recognition heuristic, Psvchological Review 109 (1) (2002) 75–90.

[79] P. Slovic, M. Finucane, E. Peters, D.G. MacGregor, The afect heuristic, in:

T. Gilovich, D. Grifin, D. Kahneman (Eds.), Heuristics and Biases: The Psychology of Intuitive Judgment, Cambridge University Press, New York, 2002, pp. 397–420.

[80] D. Kahneman, I. Ritov, D. Schkade, Economic preferences or attitude expressions? An analysis of dollar responses to public issues. Journal of Risk and Uncertainty 19 (1999) 203–235.

[81] D. Ariely, The (Honest) Truth About Dishonesty, Harper Perennial, New York, 2013.

[82] T.K. Das, B.-S. Teng, Cognitive biases and strategic decision processes: an integrative perspective, Journal of Management Studies 36 (6) (1999) 757–778.

[83] D. Kahneman, P. Slovic, A. Tversky (Eds.), Judgment under Uncertainty: Heuristics and Biases, Cambridge University Press, Cambridge, UK, 1982

[84] D. Kahneman, A. Tversky (Eds.), Choices, Values, and Frames, Cambridge University Press, Cambridge, UK, 2000.

[85] T. Gilovich, D. Grifin, D. Kahneman (Eds.), Heuristics and Biases: The Psychology of Intuitive Judgment. Cambridge University Press. New York. 2002

[86] J.E. Russo, V.H. Medvec, M.G. Meloy, The distortion of information during decisions, Organizational Behaviour and Human Decision Processes 66 (1996) 102–110.

[87] R. Hogarth, Judgement and Choice: The Psychology of Decision, 2nd ed., Wiley, Chichester, UK, 1987.

[88] A.P. Sage, Behavioural and organisational considerations in the design of information systems and processes for planning and decision support, IEEE Transactions on Systems. Man and Cybernetics 11 (9) (1981) 640–678

[89] D. Lovallo, O. Sibony, The case for behavioral strategy, McKinsey Quarterly (2010). http://www.mckinsey.com/business-functions/strategy-and-corporatefinance/our-insights/the-case-for-behavioral-strategy (March).

[90] E.J. Johnson, S.B. Shu, B.G.C. Dellaert, C. Fox, D.G. Goldstein, G. Haubl, R.P. Larruick, J.W. Payne, E. Peters, D. Schkade, B. Wansink, E.U. Weber, Beyond nudges: tools of a choice architecture, Marketing Letters 23 (2012) 487–504.

[91] R.H. Thaler, C.R. Sunstein, J.P. Balz, Choice architecture, Retrieved from https:// www.sas.upenn.edu/\~baron/475/choice.architecture.pdf, (2014) (February 4, 2019).

[92] D. Halpern, Inside the Nudge Unit, WH Allen, London, 2015.

[93] D.M. Hausman, B. Welch, Debate: to nudge or not to nudge, Journal of Political Philosophy 18 (1) (2010) 123–136.

[94] M. Fleischmann, M. Amirpur, A. Benlian, T. Hess, Cognitive biases in information systems research: A scientometric analysis, Proceedings of the European Conference on Information Systems (ECIS) 2014, Tel Aviv, Israel, June 9–11, 2014, 2014.

[95] G.B. Chapman, E.J. Johnson, The limits of anchoring, Journal of Behavioral Decision Making 7 (1994) 223–242

[96] M. Odnor, H. Oinas-Kukkonen, Behavioral economics in information systems research: A persuasion context analysis, Proceedings of the 19<sup>th</sup> International Conference on Enterprise Information Systems (ICIES 2017), vol. 3, 2017, pp. 17–28.

[97] V.S. Jacob, J.C. Moore, A.B. Whinston, An analysis of human and computer decision-making capabilities, Information & Management 16 (1989) 247–255.

[98] J.E. Kottemann, F.D. Davis, W.E. Remus, Computer-assisted decision making: performance, beliefs, and the illusion of control, Organizational Behavior and Human Decision Processes 57 (1) (1994) 26–37.

[99] W. Remus. J. Kottemann. Anchor-and-adiustment behavior in a dynamic decisior environment, Decision Support Systems 15 (1995) 63–74.

[1oo] M.C. Rov. F.J. Lerch. Overcoming ineffective mental representations in base-rate problems, Information Systems Research 7 (2) (1996) 233–247.

[101] L.-H. Lim. I. Benbasat. The debiasing role of group support systems: an experi. mental investigation of the representativeness bias, International Journal of Human-Computer Studies 47 (1997) 453–471.

[102] G.H. van Bruggen, A. Smidts, B. Wierenga, Improving decision making by means of a marketing decision support system, Management Science 44 (5) (1998) 645-658

[103] S.S. Kahai, S.A. Solieri, A.J. Felo, Active involvement, familiarity, framing, and the illusion of control during decision support system use, Decision Support Systems 23 (2) (1998) 133–148

[104] J.F. George, K. Dufy, M. Ahuja, Countering the anchoring and adjustment bias with decision support systems, Decision Support Systems 29 (2) (2000) 195–206.

[105] J.Q. Chen, S.M. Lee, An exploratory cognitive DSS for strategic decision making, Decision Support Systems 36 (2) (2003) 147–160

[106] D.R. Jones, P. Wheeler, R. Appan, N. Saleem, Understanding and attenuating decision bias in the use of model advice and other relevant information, Decision Support Systems 42 (2006) 1917–1930.

[107] B. Hosack, The efect of system feedback and decision context on value-based decision-making behavior, Decision Support Systems 43 (2007) 1605–1614.

[108] F. Kuo, C. Hsu, R. Day, An exploratory study of cognitive efort involved in decision under framing—an application of the eye-tracking technology, Decision Support Systems 48 (1) (2009) 81–91.

[109] C.A. Looney, A.M. Hardin, Decision support for retirement portfolio management: overcoming mvopic loss aversion via technology design. Management Science 55 (10) (2009) 1688–1703.

[110] S. Watts, G. Shankaranarayanan, A. Even, Data quality assessment in context: a cognitive perspective, Decision Support Systems 48 (2009) 202–211

[111] F. Cheng, C. Wu, Debiasing the framing efect: the efect of warning and involvement, Decision Support Systems 49 (3) (2010) 328–334.

[112] W.-K. Tan, C.-H. Tan, H.-H. Teo, Consumer-based decision aid that explains which to buy: decision confirmation or overconfidence bias? Decision Support Systems 53 (2012) 127–141.

[113] S. Piramuthu, G. Kapoor, W. Zhou, S. Mauw, Input online review data and related bias in recommender systems, Decision Support Systems 53 (2012) 418–424.

[114] C.-W. Chen, M. Koufaris, The impact of decision support system features on user overconfidence and risky behavior, European Journal of Information Systems 24 (2015) 607–623.

[115] D. Arnott, F. Lizama, Y. Song, Patterns of business intelligence systems use in organizations. Decision Support Systems 97 (2017) 58–68

[116] M.A. Feris, O. Zwikael, S. Gregor, QPLAN: decision support for evaluating planning quality in software development projects, Decision Support Systems 96 (2017) 92–102.

[117] M. Kretzer, A. Maedche, Designing social nudges for enterprise recommendation agents: an investigation in the business intelligence systems context, Journal of th Association for Information Systems 19 (12) (2018) 1145–1186.

[118] M.E. Ahsen, M.U.S. Ayvaci, S. Raghunathan, When algorithmic predictions use human-generated data: a bias-aware classification algorithm for breast cancer diagnosis, Information Systems Research 30 (1) (2019) 97–116.

[119] W.-S. Chen, R. Hirschheim, A pragmatic and methodological examination of information systems research from 1991 to 2001, Information Systems Journal 14 (2004) 197–235.

[120] D. Arnott, G. Pervan, A critical analysis of decision support systems research, Journal of Information Technology 20 (2) (2005) 67–87.

[121] A. Hardin, C.A. Looney, G.D. Moody, Assessing the credibility of decisional guidance delivered by information systems, Journal of Management Information Systems 34 (4) (2017) 1143–1168.

[122] M.S. Silver, Decisional guidance for computer-based decision support, MIS Quarterly 15 (1) (1991) 105–122.

[123] M.S. Silver, Decisional guidance: Broadening the scope, in: P. Zhang, D.J. Galletta (Eds.). Human-Computer Interaction and Management Information Systems: Foundations. Routledge. New York. 2006, pp. 90–119.

[124] B. Fischhof, Debiasing, in: D. Kahneman, P. Slovic, A. Tversky (Eds.), Judgement under Uncertainty: Heuristics and Biases, Cambridge University Press, New York 1982, pp. 422–444.

[125] G. Keren, Cognitive aids and debiasing methods: Can cognitive pills cure cognitiv ills, in: J.P. Caverni, J.M. Fabre, M. Gonzalez (Eds.). Cognitive Biases, North-Holland, Amsterdam, 1990, pp. 523–555

[126] Gartner, Mastering the New Business Executive Job of the CIO: Insights from the 2018 CIO Agenda Report, Gartner Inc., Stamford, CT, 2018 Retrieved 05 Octobe 2018 from https://www.gartner.com/imagesrv/cio-trends/pdf/cio\_agenda\_2018.

pdf.

[127] L. Kappelman, V. Johnson, C. Maurer, E. McLean, R. Torres, A. David, N. Quynh, The 2017 SIM IT issues and trends study, MIS Quarterly Executive 17 (1) (2018) 53–88.

[128] G. Loewenstein, S. Rick, J.D. Cohen, Neuroeconomics, Annual Review of Psychology 59 (2008) 647–672.

[129] J.V. Brocke, T.-P. Liang, Guidelines for neuroscience studies in information systems research, Journal of Management Information Systems 30 (4) (2014) 211–233.

[130] H.J. Watson, Preparing for the cognitive generation of decision support, MIS Quarterly Executive 16 (3) (2017) 153–169.

[131] F. Adam, C. Murphy, Information flows amongst executives: their implications for systems development, Journal of Strategic Information Systems 4 (4) (1995) 341–355.

[132] P.B. Goes. Editor's comments: information systems research and behavioral eco: nomics, MIS Ouarterly 37 (3) (2013) jii–viji

David Arnott is Emeritus Professor of Information Systems at Monash University, Melbourne, Australia. His research areas are personal decision support systems, business intelligence, and behavioral economics. He is the author of many papers in the decision support area, including papers in the European Journal of Information Systems, Information Systems Journal, Journal of the Association of Information Systems, Decision Support Systems, and the Journal of Information Technology. A pioneer in management support education, he first taught graduate courses in the area in 1980. He is a Fellow of the Australian Computer Society and a Senior Editor for the journal Decision Support Systems.

Shijia (Caddie) Gao is a lecturer at the Faculty of Information Technology, Monash University. She received her PhD degree in Business Information Systems from the University of Queensland Business School. Her research interests include business in telligence, decision support systems, decision theory, risk management, financial information systems, business process management, and knowledge management. Her research has appeared in Decision Support Systems, Journal of Knowledge Management, Journal of Decision Systems, Journal of Database Management, Expert Systems with Applications, among others.
