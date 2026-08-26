---
otero_id: 17707
otero_key: "J3S6Y9SQ"
title: "Towards integrating rule-based expert systems and neural networks"
authors: "Tong-Seng Quah; Chew-Lim Tan; Krishnamurthy S. Raman; Bobby Srinivasan"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00016-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Towards integrating rule-based expert systems and neural networks

Tong-Seng Quah ${}^{a,*}$ , Chew-Lim Tan ${}^{a}$ , Krishnamurthy S. Raman ${}^{a}$ , Bobby Srinivasan ${}^{b}$

$^{a}$ Department of Information Systems and Computer Science, National University of Singapore, 10 Kent Ridge Crescent, Singapore 0511 Singapore

$^{b}$ School of Business, Nanyang Technological University, Jurong, Singapore

## Abstract

This research explores a new approach to integrate neural networks and expert systems. The integrated system combines the strength of rule-based semantic structure and the learning capability of connectionist architecture. In addition, the approach allows users to define logical operators that behave much similar to that of human expert decision making process. Neural Logic Network (NEULONET) is used as the underlying building unit. A rule-based shell like environment is developed. The shell is used to built a prototype expert decision support system for future bonds trading. The system also provides a way to behave like different experts responding to different users and giving advice according to different environmental situations.

Keywords: Neural network expert system; Network element; Semantic structure; Learning; Inferencing mechanism; Rule editor

## 1. Introduction

Decision support system (DSS) is a powerful tool which can be used to support managers in making strategic decisions $[2,30]$ . A DSS places the immense data storage, computation and analysis capabilities of modern computers at the finger tips of managers. In the 1980s, the maturing expert system technology was incorporated into many DSS, resulting in a new type of decision support tools sometimes known as Intelligent Decision Support Systems. Such systems promote sound strategic decision making and have yielded many encouraging results. The ability of such systems in processing heuristic knowledge has led to cost savings, faster decision process, good payoff, and significant competitive advantage $[19,9,11,15,4,14,24,3]$ .

Despite its success, expert system technology has some drawbacks. In particular, the knowledge bases of expert systems do not evolve. They tend to be static because the conventional expert system architecture does not provide facilities to assimilate new knowledge through learning. Also, the domain coverage of an expert system is generally narrow and it cannot degrade gracefully when more difficult questions (such as those on the fringe of the domain area) are posed by the user.

Furthermore, due to the closed world assumption of classical AND/OR logic, many rule-based expert systems are not able to arrive at a meaningful conclusion when some input data are missing or not supplied by the user. Another weakness of expert systems is their tendency to break down when applied to problems that encompass substantial uncertainty on various levels of decision-making, or situations where the preferred solution is sensitive to the specific preferences and desires of one or several decision makers $[10,13,22]$ . To sum up, current expert systems are generally unadaptive to evolving user's needs and environmental factors.

In recent years, neural network technology has also been used for supporting business decisions $[33,12,34]$ . Neural networks, with their self-organization features, lend themselves well to learning and parallelism. In particular, their ability to adapt to changing circumstances and environmental factors, and handle the fuzziness and bias aspects of human decision making offer good promise to overcome the above mentioned problems inherent in rule-based systems. In addition, the massively parallel architecture of neural network enables such systems to tolerate errors, and prevent them from failing abruptly $[29,26,1,20]$ .

Several researchers have attempted to combine the best of both worlds by integrating ordinary rule-based systems with neural network architectures $[35,28,25,16]$ . Such hybrid systems are called expert networks. These systems generally inherit the numerical nature of neural networks, with little semantic meanings being represented by the connection weights. The knowledge bases of the expert networks are represented by the inference networks that result from trainings, and are difficult to understand and maintain $[23]$ . Moreover, incorporating new heuristic rules into any knowledge base generally requires re-training of the entire neural network. Another strategy to develop expert networks is through various methods of combining neural network and expert system modules together as components of the inference system $[6]$ . However, the interfaces between the symbolic and sub-symbolic components are generally difficult to build and this constrains the usefulness of such systems $[18]$ .

This paper explores the application of Neural Logic Network to develop a decision support system which integrates neural network and expert system technology. It uses Neural Logic Network ([8,7]) as a tool to integrate expert system with neural network for developing decision support system which supports a rich set of decision logic. The integrated system offers two strengths: (1) Semantically, it inherits the expressive logic representation of Neural Logic Network, (2) Numerically, the weights can be varied to allow situational (or personalized) decision making and to allow for knowledge base refinements. Section 2 is an overview of Neural Logic Network. Section 3 elaborates on the strengths of the above mentioned system, using examples to illustrate. Section 4 describes the shell built using Neural Logic Network. Section 5 briefly presents an application example – a future bond trading advisor developed using the shell. Section 6 discusses some further works and concludes the paper.

## 2. An overview of neural logic network NEU-LONET

A Neural Logic Network (NEULONET) is a finite directed graph. A typical NEULONET as shown in Fig. 1 contains a set of input nodes and an output node. Every node can take one of the three ordered pair activation values, (1,0) for true, (0,1) for false and (0,0) for don't know – so called the 3-valued NEULONET. The representation of (0,0) for “don't know” provides greater flexibility in knowledge representation as opposed to the classical logic which assumes the absence of “truth” as “false”. Every edge in the NEULONET is also associated with an ordered pair weight $(\alpha,\beta)$ where $\alpha$ and $\beta$ are real numbers.

![](/api/attachments/J3S6Y9SQ/fulltext/images/117534f9312f72090c8ef7864ae38696c5e940341641d1fa6937338ac6fb0dc5.jpg)  
Fig. 1. A simple neural logic network - NEULONET.

![](/api/attachments/J3S6Y9SQ/fulltext/images/63de590bc0667d7b73703e5018346beb76c4a9e04fd77b464fa588668f31c21f.jpg)  
Fig. 2. General structure of 2-input NEULONET.

Referring to Fig. 1, let Q be the output node and $P_{1}, P_{2}, \ldots, P_{N}$ be input nodes. Also, let values associated with the node $P_{i}$ be denoted by $(a_{i}, b_{i})$ , and the weight for the line connecting node $P_{i}$ to Q be $(\alpha_{i}, \beta_{i})$ . The rule of activation is defined as follows:

$$
\operatorname{Act} (\mathbf {Q}) = \left\{ \begin{array}{l l} (1, 0) & \text {if Net(Q)\geq\lambda} \\ (0, 1) & \text {if Net(Q)\leq - \lambda} \\ (0, 0) & \text {otherwise.} \end{array} \right.\tag{1}
$$

where $\lambda$ is the threshold, always set to 1, unless otherwise indicated.

Where $\operatorname{Net}(Q)$ is defined by the rule of propagation:

$$
\operatorname{Net} (\mathbf {Q}) = \sum_ {i = 1} ^ {N} \left(a _ {i} \alpha_ {i} - b _ {i} \beta_ {i}\right).\tag{2}
$$

<table><tr><td>P</td><td>Q</td><td>S</td><td>T</td><td>Net (P AND Q)</td><td>P AND Q</td></tr><tr><td>(1,0)</td><td>(1,0)</td><td>(0,0)</td><td>(1,0)</td><td>a+c+g</td><td>(1,0)</td></tr><tr><td>(1,0)</td><td>(0,1)</td><td>(1,0)</td><td>(0,0)</td><td>a+e-d</td><td>(0,1)</td></tr><tr><td>(1,0)</td><td>(0,0)</td><td>(0,0)</td><td>(0,0)</td><td>a</td><td>(0,0)</td></tr><tr><td>(0,1)</td><td>(1,0)</td><td>(0,1)</td><td>(0,0)</td><td>c-b-f</td><td>(0,1)</td></tr><tr><td>(0,1)</td><td>(0,1)</td><td>(0,0)</td><td>(0,1)</td><td>-b-d-h</td><td>(0,1)</td></tr><tr><td>(0,1)</td><td>(0,0)</td><td>(0,0)</td><td>(0,0)</td><td>-b</td><td>(0,1)</td></tr><tr><td>(0,0)</td><td>(1,0)</td><td>(0,0)</td><td>(0,0)</td><td>c</td><td>(0,0)</td></tr><tr><td>(0,0)</td><td>(0,1)</td><td>(0,0)</td><td>(0,0)</td><td>-d</td><td>(0,1)</td></tr><tr><td>(0,0)</td><td>(0,0)</td><td>(0,0)</td><td>(0,0)</td><td>0</td><td>(0,0)</td></tr></table>

Fig. 3. Example on construction algorithm.

![](/api/attachments/J3S6Y9SQ/fulltext/images/ef8c27287ac6bd13cb2bb9f5187bdcb86bc258d6a4ef1cdd8dd97dc1338d6c51.jpg)  
Fig. 4. "AND" logical operator.

2.1. Construction algorithm for NEULONET logical operators

While the simple network in Fig. 1 has only input and output layers, a hidden layer comprising a set of intermediate nodes may be necessary for some logical operations. Fig. 2 depicts a general structure of any 2-input NEULONET containing two hidden nodes. By applying the NEULONET propagation rule and activation rule (Equation 2 and 1, respectively) against the truth table of any desired logical operator, and solving for the variables $a - h$ and simplifying a NEULONET that represents the truth table can be obtained.

As an example to show the construction of an “AND” network, Fig. 3 gives the output values of the intermediate nodes S and T and the values of $Net(P AND Q)$ . Applying the activation rules on $Net(P AND Q)$ according to the expected output of $(P AND Q)$ shown in the last column of Fig. 3, a set of inequalities may be established. The solution to these inequalities is not unique and a convenient set of values is a = c = 0.5, b = d = 2, e = f = g = h = 0.

In this set of solution, the hidden nodes will not be of any influence as the connection weights from the hidden units to the output node are both $(0,0)$ . Thus, after simplification, the result is an “AND” operator in Fig. 4.

By following through the same procedure, the structure of “OR” and “XOR” NEULONETs can be obtained as depicted in the following diagram (Fig. 5). More examples can be found in [8].

## 3. NEULONET for decision support

This section illustrates how NEULONET can be used to represent rules in an expert system knowledge base. The duality of NEULONET rules (semantic and numerical features) is also discussed here.

![](/api/attachments/J3S6Y9SQ/fulltext/images/5cf3fe3af15dc30cf3cf459748bfd5f618aad7906813da11c27c45b1fba3a2f5.jpg)  
Fig. 5. "OR" and "XOR" logical operators.

## 3.1. Network element - netel

As different sets of weights on the edges of NEULONET correspond to different logical operators (Section 2.1) semantically we may map any rule from a conventional knowledge base into small NEULONET of equivalent meaning. In this paper, a small NEULONET representing a rule is called network element (netel). Netels make up the inference network tree during any consultation or training session in a NEULONET expert system.

A netel is a small NEULONET with n input nodes and one output node. It may also contain hidden nodes. Every netel has two equivalent forms, one is the usual textual form similar to that in the conventional rule-based system, and the other in a graphical form that pictorially represents the NEULONET.

This is illustrated by the following example.

The rule:

IF capital-utilization-high(cap-index)

AND money-supply-high(money-vol)

THEN inflationary

The equivalent netel is shown in Fig. 6. The weights attached to the edges correspond to the AND connective in the rule.

![](/api/attachments/J3S6Y9SQ/fulltext/images/844f65ed790061701d35393dbb259ef8e54e06c41fde9506ab50abcc52bd8cb0.jpg)  
Fig. 6. Netel as an equivalent of knowledge base rule.

During the inferencing process, initial data supplied by the user may turn on the input nodes. By applying the activation and propagation rules of the NEULONET (Equations 1 and 2, respectively), the chaining of netels may take place through linking up netels when the truth value for the output node of the $n^{th}$ layer netels agrees with the $(n + 1)^{th}$ layer netels input nodes.

## 3.1.1. Enhanced NEULONET

The basic NEULONET is an improvement over neural networks in general [8]. Additional features have been added to the original NEULONET to enhance its inference and learning mechanism [21]. These features are discussed here:

Learnability index: The netels in a knowledge base can generally be classified into two categories: Fundamental principles of the domain expertise (which should not be changed at will), and rules which are pure heuristics. As heuristics often carry a flavor of fuzziness and intuition, it is sometimes difficult for the domain experts to state them definitively. In an expert system, the captured heuristic rules may require refinements through usage. In neural network terminology, it means adjusting weights of the edge links to better reflect the relationship of the nodes. In order to distinguish these two groups of netels in the same knowledge base, the learnability index is introduced. The learnability index of a netel reflects how susceptible the weights on the edge links are to adjustments during training sessions. In the knowledge base, netels that represent the fundamental principles of a domain of expertise, or heuristic rules whose validity the domain experts are much confident with, the index will be set to nil or low value. By setting the learnability index of a rule to nil, the logical operator of the netel will not be altered by refinement trainings, thus the semantic meaning of the netel will be preserved. For netels that are pure heuristics, the user may set the value to reflect his certainty of the rule. The more a user is uncertain about a netel, the higher the user should set the learnability index value (range from 0:unchangeable to 9:highly updatable). In training sessions, the updatable netels will thus have their weights readily “carved” towards the correct values according to the training examples.

Pointer to situational weight file: In many application expert systems, the inability to explicitly represent the priorities and preferences of the decision makers seriously limits the usefulness of such systems [17]. Many of these systems rely on heuristics which contain implicit assumptions about the priorities and preferences of the domain expert who contributed the knowledge. For example, in currency option trading, the decisions for buying or selling of options are strongly influenced by the experience and the risk profile of individual experts (such as capital on hand and financial obligations) – some traders are more aggressive, others may be more conservative. Thus, in such domains the advices given by different experts will not be the same.

To enable the system to reason like different experts, a weight file pointer is attached to the netel knowledge base. Using the above currency option trading example, the knowledge engineer can create a set of netels to represent the general strategy in currency option trading. Associated with each knowledge base is a pointer which points to an auxiliary weight file. A default set of weights is loaded if the pointer points to nil, else it will load in a set of weights that represent the selected expert's opinions. Therefore, the weight file pointer serves as a function that is sensitive to expert identification. With different sets of weights on the edge links for different experts, different inferencing strategies may thus be achieved without needing to duplicate the same rules in the knowledge base, thus achieving the idea of personalization. Another example of application involving subjective knowledge is a stocks and shares investment expert system, where a buy-or-sell decision may be acceptable by a bullish buyer but unacceptable to a more conservative one.

By the same token as expert-sensitive reasoning, situationalization may also be achieved by the weight file pointer. A knowledge base set up for general consultations can be trained to work under varying environmental conditions. In this way, the strength of influence between any two nodes can vary by different consultation conditions, thus providing an environment to model dynamic knowledge. An example is the property investment domain, where the advices of an expert may differ according to whether the prices are on the upward or downward trends.

## 3.2. Semantics of netels

The choice of weights associated with edges offers a great variety of different logic operations for netels. For a netel with just two inputs each with three possible values (true (1,0), false (0,1) or don't know (0,0)), there are $3 \times 3 = 9$ combinations. These nine combinations can be specified on the P and Q column of the truth table (see Fig. 7). Each cell $(x_{i}, y_{i})$ of the output column, P opn Q, can also take one of the three possible outputs – (true (1,0), false (0,1) or don't know (0,0)). Therefore in theory there is a total of $3^{9}$ sets of logical operations. However, it is noted that (0,0) and (0,0) will always generate (0,0). That will still leave us with $3^{8}$ distinct meaningful binary logical operations. For netels with more than two input nodes, the number of possibilities increases exponentially.

<table><tr><td>P</td><td>Q</td><td> $P_{\text{opn}} Q$ </td></tr><tr><td>(1,0)</td><td>(1,0)</td><td> $(x_1,y_1)$ </td></tr><tr><td>(1,0)</td><td>(0,1)</td><td> $(x_2,y_2)$ </td></tr><tr><td>(1,0)</td><td>(0,0)</td><td> $(x_3,y_3)$ </td></tr><tr><td>(0,1)</td><td>(1,0)</td><td> $(x_4,y_4)$ </td></tr><tr><td>(0,1)</td><td>(0,1)</td><td> $(x_5,y_5)$ </td></tr><tr><td>(0,1)</td><td>(0,0)</td><td> $(x_6,y_6)$ </td></tr><tr><td>(0,0)</td><td>(1,0)</td><td> $(x_7,y_7)$ </td></tr><tr><td>(0,0)</td><td>(0,1)</td><td> $(x_8,y_8)$ </td></tr><tr><td>(0,0)</td><td>(0,0)</td><td> $(x_9,y_9)$ </td></tr></table>

![](/api/attachments/J3S6Y9SQ/fulltext/images/d6fddd7ddcc94fe5860b896ab35e536adf6c3dde2099dc42456d29b3089940d9.jpg)  
Fig. 7. Edge weights are computed base on functional definition of logical operator.

With the functional requirements specified in the truth table, the construction algorithm of Section 2.1 may then be applied to compute the appropriate edge weights of the logical operator.

Many of the logical operations other than the standard ones discussed in Section 2.1 can be used to mimic human reasoning process which is often guided by subjective opinions or biases. For instance, the weights in the AND and OR networks may be modified to represent some form of biased AND and biased OR operations, respectively. This is made possible by allowing favoured inputs to carry larger arc weights in order to assert greater influence than in the usual AND and OR operations.

A few examples of netel with human logic are illustrated as followed:

1. Levels of importance (Fig. 8): $P_{1}$ , $P_{2}$ and $P_{3}$ exhibit different degree of influence (in descending order) on the outcome Q. $P_{1}$ is the most important decision factor. Only when $P_{1}$ and $P_{2}$ have no input, i.e. both equal to $(0,0)$ , then $P_{3}$ factor will be considered. An example of such decision will be the procurement manager sourcing for component parts to be used in the manufacturing process, where reliability of the component $(P_{1})$ is of utmost importance, followed by any good discount $(P_{2})$ , and finally promptness in shipment $(P_{3})$ will be considered.

![](/api/attachments/J3S6Y9SQ/fulltext/images/71374d82dfaf52ea4435d986261ff15520d361c0c9c7265441eeed9a43ddeef5.jpg)  
Fig. 8. Levels of importance.

![](/api/attachments/J3S6Y9SQ/fulltext/images/66d6e0163a42c5d7f2b6456b92972ec9e450d556ed43cfb1f7cdf4a527569a76.jpg)  
Fig. 9. Majority influence.

2. Majority influence (Fig. 9): Decision factors $f_{1}, f_{2}, \ldots, f_{n}$ are of more or less equal importance. The final decision is dependent on what the majority of the factors indicates. A scenario of such decision making process is the future bond trading market, where there are many economic factors that can cause the bond prices to float up or down. A rational trader will attempt to gather as many economic statistics as possible and then make a decision based on what the majority of the economic factors point towards.

3. Overriding factor (Fig. 10): This is an extension to the majority influence netel. Often, in the decision process, there may be one or two factors which are so important that they can completely change the final decision outcome. Using the future bond trading market again, suppose the economic statistics generally point towards an downward pressure on the prices, traders will then start to sell bonds. However, the federal government may announce some plans to stimulate the economy. Such announcements may cause the traders to reverse their decisions.

4. At-least-k logic (Fig. 11): Using this logic, there must be at least k factors indicating positive results before an alarm for action is sounded. For example, in computer performance analysis, only when at least two of the symptoms slow response time, high swap rate, high process count and high supervisory state CPU are true before the administrator concludes that the computer system is having insufficient memory.

![](/api/attachments/J3S6Y9SQ/fulltext/images/072db82a441c440278a7daf629f6ab66a988dd6c1580a7bdb2eb266665f4117f.jpg)  
Fig. 10. Overriding factor.

## 3.3. Numerical computation of netels

When an inference process is instantiated by the user through supplying of initial data, an inference network tree will be chained up based on the netel structure described in Section 3.1. The forward and backward chaining of netels are discussed in Section 4.3.

User/situation sensitive inferencing: In domains where decision outcomes are sensitive to different environment conditions and different users, it is desired to have an expert system which can adjust its advices based on the different circumstances. This may in fact be accomplished by keeping separate sets of knowledge bases for all the various combinations of such influencing conditions. For instance, actions taken by investors in a bullish stock market vary greatly from a bearish market. Also, decisions of property investors would differ according to individuals' priorities and preferences. However, this method poses a difficult maintenance problem, and is also inefficient in the use of system resources. In netel knowledge base, the system overcomes the above problem by making use of the weight file pointer (Section 3.1.1.) to replace the appropriate weights on the influence network tree based on the environmental situations specified by the user. This process is equivalent to dynamically changing the logical operators of the netel rules. With such adjustments, firing characteristics of the netels will be different and the system will draw varied conclusions according to the changing situations.

Refinement trainings: The “dual” structure (rule and neural network) of netels enables them to be readily instantiated to form the inference trees of consultations by applying the activation and propagation rules (Equations 1 and 2, respectively) of NEULONET. Activation will propagate towards the conclusion nodes in consultation sessions. In refinement training sessions (Section 4.3.3), however, any discrepancy between a targeted conclusion and the system derived conclusion will be back-propagated into the inference network. Netels which are subjectable to trainings (learnability index >0) will absorb the “blame” and have their weights on the edge links updated.

Therefore, two types of netels will co-exist in the knowledge base after training sessions. All netels are first created as semantic rules by the knowledge engineer specifying appropriate logics and the learnability indices of these netels are set with different values according to expert confidence of the rules. Netels with non-zero learnability indices are subjected to refinement trainings and become converted into learned rules (or numerical rules) while netels with zero learnability indices are not subjected to changes and thus remain as semantic rules. All netels in the knowledge base, whether numeric or semantic, are utilized in future consultation inferences.

![](/api/attachments/J3S6Y9SQ/fulltext/images/e2583128f3e7f3db10bf2782c77919487b62e48f27c7107413f6ab250236dd3c.jpg)  
Fig. 11. At-least-k logic.

## 4. The netel-based expert system shell

In this research, an expert system shell was built upon the netel-based data structure and inference engine. It was constructed as a general purpose shell so that different domain specific expert systems may be built upon it (Fig. 12). On the surface, the system presents user with an environment that looks much like a familiar rule-based system. Underlying the user interface, however, is a knowledge base of netel rules and an inference engine to drive those rules. The result is a rule-based expert system that has the strengths of connectionist architecture. The system thus hides the complexity of neural network inference engine from the user.

## 4.1. System architecture

The architecture of the prototype netel-based shell is depicted in Fig. 13, from which the following four major components may be identified:

\- Rule editor for knowledge base maintenance.

\- Knowledge bases of various domain specific expert systems.

\- Inference engine to drive the consultation process as well as to perform learning.

\- Friendly and easy-to-use user interface.

The following sections will highlight the rule editor and the inference engine of the shell.

## 4.2. Rule editor

The rule editor is initiated from the user interface shell. It is a visual editing environment. Once the system is loaded with a knowledge base, the user can freely perform changes to any netel rule. Editing can be performed on either portion of the rule editor's split window. The upper portion (graphic editor) displays the rule in a graphical form whereas the lower portion (textual editor) displays the equivalent in textual form (Fig. 14). Changes made on either editor will be reflected on the other. Besides the normal rule maintenance functions (such as additions, deletions and modifications), the user may also use the rule editor to define logical operators, thus making them “known” to the system. In addition, the rule editor also allows users to specify values for the learnability index of each netel rule.

## 4.2.1.Text editor

The text editor presents the details of each netel rule in a form-filling screen. The user may add new rules, delete obsolete rules, modify existing rules, or simply browse through the knowledge base in its entirety or just some specific rules.

![](/api/attachments/J3S6Y9SQ/fulltext/images/a49492fef8e72dcc0ecdb47da431da3d1558da32393fbab371a1896d567a7ad2.jpg)  
Fig. 12. The layer structure.

The construction algorithm (Section 2.1) of the NEULONET is built into the editor so that when the user specifies any known logical operators, appropriate weights of the network edges will be calculated automatically and being displayed. For rules that can only be expressed appropriately with non-standard logical operators (such as human logic), the editor provides a means for the user to define those operators. As each netel rule in the knowledge base is basically a small rudimentary NEULONET, the rule editor is the avenue for the user to define the activation condition of each input node and the implication of an output node when it is “turned-on”.

![](/api/attachments/J3S6Y9SQ/fulltext/images/82ddbdf2cde80eb5afbd2a76c521b1b9b07da5ffe96031a0431c75534c162b44.jpg)  
Fig. 13. System architecture.

## 4.2.2. Graphic editor

The graphic editor operates on a click-and-enter strategy. To edit an input node, the user may click on the node or the edge link. For output node, click on the node itself. Such actions will pop-up a window with relevant details of the rule component being selected. Clicking on any other position on the graphic editor screen will bring up a guidance screen.

## 4.2.3. Entering situation / user sensitive rules

Certain heuristic rules (and the antecedent conditions) may have different degrees of applicability in different environmental situations. The rule editor allows the user to specify such information for any netel in the knowledge base.

To avoid overwhelming the rule editor screen with excessive information, situational weights for the displayed netel rule is only called up via a pop-up window. Such weights reflect the computational characteristics of the netel rule under varying users and conditions/situations. Every netel may carry several such logic-situation/user pairs, thus allowing the inference engine to behave differently for different user identifications or environment situations.

## 4.2.4. Defining non-standard logical operator

There are two ways whereby the user can define non-standard logical operators.

1. When the user knows the weights on the edge links: In this case, the user may make use of the rule editor main screen (Fig. 14) to define a new name for the non-standard logic operator and the desired weights for the edges $(wt_{1}, wt_{2}, \ldots)$ .

2. When the user only knows how the logical operator should behave for different input attribute patterns but does not know the numerical weights to represent the logic: In this case the user can define a new name for the nonstandard operator that is not previously known by the system and also leaving the weight fields $(wt_{1},wt_{2},\ldots)$ unfilled. This will cause the editor to pop up a truth table screen. Fields on the screen include node names for the input attributes, “on” and “off” patterns of the input attribute sets and the outcome on the consequence node for each of the input patterns. When the user has finished entering the desired behavior pattern of the logical operator, the rule editor will calculate the appropriate weight for each edge link of the operator by using the construction algorithm for NEULONET (Section 2.1).

![](/api/attachments/J3S6Y9SQ/fulltext/images/275413f6bed4244cfaab15dda6379f7511090f7bc42b4126e4b3a1fed6052968.jpg)  
Fig. 14. The netel rule editor.

New operators specified in either way will be captured into a library of known logical operators and may be used for future netel rule creations or editions.

## 4.3. Inference mechanism

The inference engine may run in consultation or training mode. In either case it chains active rules together into a Neural Logic Network. NEULONET propagation and activation rules are applied in the process.

With the netel knowledge representation scheme discussed in Section 3.1, the system's rules are essentially fragments of Neural Logic networks to be fitted together dynamically during the inferencing process, similar to the chaining of rules in the working memory of a conventional rule-based system. Two ways of chaining, i.e. forward and backward chaining, are possible. A combination of both ways are utilized during any inferencing. The chaining process continues until some goal nodes are activated, the conclusion will then be presented to the user (in consultation mode) or compared with the training example (in training mode). The inference engine back-tracks when no fruitful conclusion can be reached. In such situations, the system traces those inference tree branches that carry nodes yet to be activated. More inputs may be solicited from the user. As and when new activations are obtained for some nodes, forward inference can resume.

## 4.3.1. Forward chaining

NEULONET forward chaining is very much the same as the normal deductive reasoning from facts towards conclusions. The process begins with the supplying of initial data to the system from which successive deductions are made. Initial data or intermediate outputs in the deductive chaining propagate their activations to the following netel (Equation 2). There may be more than one potential candidate for linking, thus creating a tree structure of chaining, with each branch heading for a conclusion.

## 4.3.2. Backward chaining

Backward chaining works from a goal or a hypothesis to lead to available facts or data. Backward chaining is more difficult to implement as the netel chaining process is in the opposite direction to that of network activation. There may be no readily available input data to a candidate network to test if the network can achieve the current output (i.e. current goal or hypothesis). New hypotheses (i.e. new subgoals) may have to be assumed as inputs to test the network. This process is usually repeated until the input layer nodes of the network is reached. In the backtracking process, when the candidate netel to be chained contains a pure conjunction (“AND” operation), all inputs (i.e. output nodes of previous layer) to that current output node need to be tested to see if they can achieve the desired output under consideration. For a pure disjunction (“OR” operation) in the candidate netel, each single input will be tested one at a time until the desired output is attained. For other logical operations, it generally requires testing of different combinations of inputs until the network succeeds in generating the required output. Therefore, in a serial implementation, the chaining process is very similar to that of conventional rule-based systems. On the other hand, due to the neural network nature, concurrent chainings of netels are possible in a parallel environment. Such a massively parallel architecture may result in contention of resources, in particular, available processors. In such cases some ordering of priority may be implemented. A strategy that makes use of the edge weights in ranking the traceable paths is the heuristic search strategy [27]. The ranking of the paths is from one that is most resource economical to one that is most resource greedy. After the backward tracing paths are ranked, the subgoals are then traced with some computed order. In the process, new subgoals may be established and ranked, and the inference process continues.

Heuristic search: This strategy attempts to search all possible combinations of input values but in a sequence ranked by some heuristics given below:

1. A heuristic ordering is first established by ranking inputs in descending order of the “rank” value:

$$
\begin{array}{l l} \text {rank} _ {i} = & \max (1 x \alpha_ {i} - 0 x \beta_ {i}, 0 x \alpha_ {i} - 0 x \beta_ {i}, \\ & 0 x \alpha_ {i} - 1 x \beta_ {i}) - \\ & \min (1 x \alpha_ {i} - 0 x \beta_ {i}, 0 x \alpha_ {i} - 0 x \beta_ {i}, \\ & 0 x \alpha_ {i} - 1 x \beta_ {i}), \end{array}\tag{3}
$$

where $(\alpha_{i},\beta_{i})$ is the arc weight of input i, and $rank_{i}$ is an indication of the strength of a node in contributing either positively or negatively to the output value of a netel.

2. Input combinations with lesser number of nodes are ranked higher. Thus, a combination that contains only one input node (i.e. “don’t care” for other inputs) will have the highest ranking. Combinations with the same number of input nodes are ranked among themselves according to the heuristic ordering in step 1 above. This thus ensures the least possible number of inputs are tried first to arrive at the desired output and hence reduces the number of backward chaining paths since “don’t care” node need not be pursued further. By minimising the number of trial nodes, this step leads the system to pursue the most promising paths first.

Using the levels of importance (Fig. 8) as an example, the rank values of the three inputs are found as follows:

rank of $P_{1} = 4 - (-4) = 8$

rank of $P_{2} = 2 - (-2) = 4$

rank of $P_{3} = 1 - (-1) = 2$

The three inputs are thus heuristically ordered as $P_{1}$ , $P_{2}$ , $P_{3}$ according to step 1 above. Step 2 then orders the sequence of testing as follows:

1. test $P_{1}$

2. test $P_{2}$

3. test $P3$

4. test $P_{1}, P_{2}$

5. test $P_{1}, P_{3}$

6. test $P_{2}, P_{3}$

7. test $P_{1}, P_{2}, P_{3}$

## 4.3.3. Refinement training

In training mode, when a training example is presented to the system, it will chain up an inference tree from the input nodes to the desired goal node. Relevant netel rules are selected from the knowledge base depending on the input variables in the training example. After applying the activation and propagation rules, the activation state of the network output nodes is compared to the desired value in the training example. If the network is not able to derive at the desired conclusion, the error is back propagated, and the netels in the inference tree will have their connection weights adjusted. However, an assumption of the system is that the netel rules articulated by the human experts are sufficiently closed to the global minima of the neural network representing the domain knowledge. The constituent netels therefore only require small weight adjustments – perhaps output nodes of certain netels in the inference network slightly fall short of the threshold of the NEULONET activation rule (Equation 1).

![](/api/attachments/J3S6Y9SQ/fulltext/images/b5edf21cdbb89d2943a372e21601d6608a6996cbed04f5b682674cc9b4ce2b44.jpg)  
Fig. 15. Refinement training.

In Fig. 15, suppose that the output node of netel b should be true(1,0) but the network propagated value is false(0,1). Thus there is a positive error, and the weights $(\alpha,\beta)$ of those links connected to the output node of netel b should have the $\alpha$ value increased and $\beta$ value lowered.

Let the links connected from output node of netel b to the next layer of netels be represented as $(\gamma_{j},\sigma_{j})$ . Then:

$$
\alpha_ {i} = \alpha_ {i} + \eta \sum_ {j = 1} ^ {n} \alpha_ {i} \gamma_ {j},
$$

$$
\beta_ {i} = \beta_ {i} - \eta \sum_ {j = 1} ^ {n} \beta_ {i} \sigma_ {j}.
$$

Conversely, if the output node of netel b should be $false(0,1)$ but the computed value by the inference network is $true(1,0)$ , then:

$$
\alpha_ {i} = \alpha_ {i} - \eta \sum_ {j = 1} ^ {n} \alpha_ {i} \gamma_ {j}
$$

$$
\beta_ {i} = \beta_ {i} + \eta \sum_ {j = 1} ^ {n} \beta_ {i} \sigma_ {j},
$$

where $\eta = 0.1x$ (learnability index of netel b) and n = number of out-links from netel b.

## 5. NEULONET expert system for bond trading

A U.S. future bond trading advisory system was built on the prototype shell to illustrate the use of NEULONET for building decision support advisory system. In particular, the aspects of human logic, situation/user sensitive decision making, and learning were experimented.

## 5.1. The U.S. future bond market

The U.S. future-bonds is a fixed earning investment device. It is basically a form of borrowing by the government from the open market. Since the return is fixed, the price of the bonds fluctuates inversely with the prevailing interest rate in the market. Influencing the price movements is a set of statistics released periodically by the U.S. government. The statistics reflect the performance of the U.S. economy, which strongly affects the demand and supply in the money market and causes the interest rate to float up or down. Bond prices will follow swiftly in the opposite direction of anticipated interest rates movements $[31,5]$ .

Often, conflicting economic statistics may be released on the same day by the government agencies [32]. In such situations, the bond market may be rather unpredictable and depend heavily on the psychological states of the majority of traders in the market. Even an experienced trader may occasionally make the wrong move. Past experiences and gut feeling play an important part in the decision process under such situations.

The domain of future-bond trading is appropriate for testing the NEULONET shell because the trading rules for buying and selling carry heavy flavors of human decision making which cannot be appropriately expressed using conventional AND/OR logic. In fact, the final decision for buying or selling is also strongly influenced by the experience and the state of mind of individual experts at the point of transactions – some traders are more aggressive, others may be more conservative. These characteristics can be very well handled by the situational/user sensitive logic discussed in Section 4.2.3. Furthermore, these netels can be “fine-tuned” using real-life historical cases as training examples. The refined weights will very well represent human traders’ behaviors in actual situations.

## 5.2. Traders' judgements

Since speculation plays a major part in bond trading, good human judgment is important. In fact, when economic statistics are released, an aggressive trader will usually react stronger than a conservative one. The bond trading expert system allows training according to different expert identifications, thus realizing the idea of personalized expert decision support system.

In the event of multiple economic statistics being released on the same day, human judgment is even more essential. These statistics may point towards a concerted direction for the bond prices or they may contradict each other. When that is the case, economic indicators such as GNP statistics which influence a larger section of the economy usually have heavier effects on the price movements than economic indicators that reflect the performance of a smaller section of the economy, such as retail sales. However, decisions become tough when the released economic statistics give questionable weak signals. Under such circumstances, traders will act with caution. Generally, they will only enter the market if there are at least two important statistics pointing towards the same direction of economy movement. The netel which neatly represents this “at-least-two” decision process is illustrated in Fig. 11. To represent such human decision process using conventional logical operator such as “AND”, “OR” and “NOT” will not be as easy.

## 5.3. Situation decision makings

Another strength of the netel-based expert system is its ability to handle situational logic with ease. Usually, releasing of economic performance statistics by the government authorities will cause future-bond prices to fluctuate, as discussed in previous sections. However, if there are any special military, political or social upheavals, the psychological state of the traders will be stirred. Under such situations, bond prices will defy the normal economic pressures and move according to market confidence.

On the other hand, when unfavorable economic factors are released, government authorities may announce corrective measures to rectify the situations. Such comments made by the government officers may restore the traders' confidence and cause the bond prices to reverse their movements.

![](/api/attachments/J3S6Y9SQ/fulltext/images/d78051490605ff7767a33993cc04ceb6e9476e1330fe6162932c281ed8e8a1f6.jpg)  
Fig. 16. Netel rule for bond trading during war time.

To represent such a reasoning process using conventional rules is cumbersome. One possible representation is as follows:
IF economic-statistics is favorable
AND war-involvement is none
AND official-comment is none
THEN action is buy-bonds

IF war-involvement is imminent
AND official-comment is none
THEN action is sell-bonds

IF official-comment is good-news
THEN action is buy-bonds

IF economic-statistics is unsure
AND (war-news is favorable
OR official-comment is positive)
THEN action is buy-bonds

These rules are not exhaustive, other combinations of the antecedents and consequences are possible.

Using the netel-based expert system, however, only one netel rule (with “level of important” logic operator) is sufficient to represent the possibilities (Fig. 16).

The “Actions” node may be excited or inhibited depending on the activations of the antecedent nodes. In other words, buying or selling of bonds will only be dependent on economic factors if there are no major unplanned circumstances either within the economy or around the world.

Therefore, the netel-based expert system is able to represent heuristic rules in a much neater way than conventional expert systems do.

## 5.4. Implementation results

The bond trading advisory system was built on the NEULONET shell. The rule editor, which consists of a graphic editor and a textual editor (Section 4.2), was used to enter the netel rules into the knowledge base, which also contains weight files for performing situation/user sensitive inferencing. Besides, the rule editor was also used as the tool to define logical operators that are peculiar to human decision making. The inference engine fires netel rules in the knowledge base by applying NEULONET activation and propagation rules. Besides performing consultation inferences like a rule-based system, the inference engine also allows refinement trainings to be performed on netels which are learnable (Section 3.1.1). The inference engine refers to the weight files when loading netels into the working memory, thus achieving user sensitive inferencing.

## 5.4.1. Netel knowledge base

The netel knowledge base consists of heuristic rules and extended data structures of the enhanced NEULONET. These were created from the knowledge articulated by a domain expert. There are 46 netels in the knowledge base. They can be grouped into two major categories. The first category are netels that represent the macro economic principles, such as the relationship between interest rate movements and bond prices. There are 18 of such netels. The second category are netels that represent the domain expert's preferences and heuristics on how he derives the trading decisions based on the economic statistics – in particular, how he decides which pieces of economic statistics are more important. These second category of netels are mainly built with operators that depicts human decision logic, such as at-least-two, majority influence, levels of importance etc. Some of these logical operators are discussed in Section 3.2, 5.2 and 5.3. All the netels are created through the rule-editor of the prototype shell.

These netels represent the knowledge of a domain expert in bond trading. They form the basic knowledge of the expert system. With the flexibility provided by weight file pointers (Section 3.1.1), some netels carry several sets of weights. This is obtained by training the knowledge base using different experts' identifications and their buy-or-sell decisions (see experiment session 3 of Section 5.4.3).

![](/api/attachments/J3S6Y9SQ/fulltext/images/0123de64fca1cd51443d4b7f60720556866bb650497d1ef8821566d21c6b6cf7.jpg)  
Fig. 17. Personalized knowledge bases.

As different weights are loaded into the working memory according to expert identifications, semantically it is equivalent to having varying sets of rules for different users. This relationship is depicted in Fig. 17.

## 5.4.2. Refinement trainings

Using the basic knowledge base as a start, the untrained netel expert system was tested with historical cases of bond price movements and associated environmental factors taken from The Asian Wall Street Journal.

The results are in Table 1.

These 60 test cases will be referred to as test set A.

These results show that the netel rules are quite good in cases of single statistic releases. The few cases where the expert system was unable to make correct judgment were mainly due to weak signals given by the statistical figures. These weak cases were not able to activate the netel nodes sufficiently to trigger the firing of the goal nodes.

For complex cases (i.e. several pieces of statistics being released on the same day), the expert system is much less competent to give correct advices.

Table 1  
Performance data before refinement training

<table><tr><td></td><td>Simple stat.</td><td>Multi-stat.</td><td>Total</td></tr><tr><td>No. of cases</td><td>45</td><td>15</td><td>60</td></tr><tr><td>Successful</td><td>42</td><td>9</td><td>51</td></tr><tr><td>Successful(%)</td><td>93%</td><td>60%</td><td>85%</td></tr></table>

Table 2  
Performance data after refinement training with uniform learnability index

<table><tr><td></td><td>Simple stat.</td><td>Multi-stat.</td><td>Total</td></tr><tr><td>No. of cases</td><td>45</td><td>15</td><td>60</td></tr><tr><td>Successful</td><td>45</td><td>12</td><td>57</td></tr><tr><td>Successful(%)</td><td>100%</td><td>80%</td><td>95%</td></tr></table>

The netel rules were subjected to learning (refinement training) by using additional historical cases collected from the same journal from January 1989 to December 1991. This training set (set B) consists of 119 test cases of which 96 cases belong to bond price movements caused by single economic statistic releases and the remaining are due to complex statistics releases.

Three refinement training sessions, each with different setup conditions, were conducted. Before every training session, the working memory was initialized. The un-trained netels were then subjected to training examples taken from test set B. After each training session, the trained netels were subjected to test set A again to determine the performance improvements.

## 5.4.3. Results after each training session

Results of the netel performance after each refinement training session are:

Session 1: Training with uniform learnability index (set to 5) for all netels. The results is in Table 2. The netels perform better after retirement training. Upon analysis, it was discovered that the weights actually shifted towards flavoring paths connecting economic statistics that have larger impact on the economy, which also imply stronger influence on the traders decisions.

Session 2: Training with varying learnability index (0–9) for different netels. The results is in Table 3. The netels also perform better under this training session. However, their edge weights learn with different degrees of readiness. For example, those netels which inferring from macro economic conditions to inflationary or deflationary pressures have their learnability index set to zero, this is based on the assumption that such netels are representing the basic principles of macro economics, which are likely to be valid, so it is not logical to change the weights of those netels which theoretically means changing the economic principles. On the other hand, netels chaining the input statistical figures to the nodes depicting factors of production in the economy will have their learnability index set to higher values, so that training sessions can adjust the weights to reflect the relative significance of the various statistical figures.

Table 3  
Performance data after refinement training with varying learnability index

<table><tr><td></td><td>Simple stat.</td><td>Multi-stat.</td><td>Total</td></tr><tr><td>No. of cases</td><td>45</td><td>15</td><td>60</td></tr><tr><td>Successful</td><td>45</td><td>13</td><td>58</td></tr><tr><td>Successful(%)</td><td>100%</td><td>87%</td><td>97%</td></tr></table>

Session 3: Training with hypothetical expert decisions to experiment the effects of user-sensitive inferencing. In this session, an aggressive trader, y, was hypothesized by changing some of the historical training cases (in set B). The netels in the expert system knowledge base were then subjected to training using these modified cases. The results is in Table 4.

Upon analysis, the weights of the netels were found to have shifted towards higher values on paths that lead to “buy” decision and lower value on paths that lead to “sell” decision. Thus, it is not surprising that the decision nodes for buying bonds receive higher chances of being activated.

## 5.5. Benchmark comparison with conventional approaches

While the above implementation results demonstrate the strengths of the integrated approach in knowledge engineering and learning, it will be interesting to examine how this approach

Table 4  
Experiment on user sensitive inferencing

<table><tr><td></td><td>Buy decision</td><td>Sell decision</td><td>Indecisive</td><td>total</td></tr><tr><td>“Normal trader”</td><td>31</td><td>26</td><td>3</td><td>60</td></tr><tr><td>Trader y</td><td>37</td><td>21</td><td>2</td><td>60</td></tr></table>

Table 6

compares with conventional rule-based and neural network approaches. In this comparison, the bond trading data are used as a benchmark test for both the present system and the conventional systems. Furthermore, the present hybrid system is compared with a pure rule-based system on one extreme and a pure neural network on the other extreme on equal basis. Interestingly, the duality of Neural Logic Network allows one to turn the integrated system into purely rule-based as well as purely neural network without much difficulty. This provides a convenient common ground for comparing the three systems.

To convert the hybrid system into a pure rule-based system, a few changes were made:

Knowledge base: Netels were re-constructed with only standard logic AND, OR, and NOT. In the process, each netel rule with human logic operator was re-expressed using more than one rule carrying conventional logic operator as discussed in Section 5.3.

Inference engine: The ability of the inference engine to handle don't know (0,0) state was suppressed. Instead, any don't know input is treated as false (0,1), just as in conventional 2-valued logic. Further, the activation rule (Equation 1) of the inference engine was modified as:

$$
\operatorname{Act} (Q) = \left\{ \begin{array}{l l} (1, 0) & \text { if } \operatorname{Net} (Q) \geq \lambda \\ (0, 1) & \text { otherwise }, \end{array} \right.\tag{4}
$$

where $\lambda$ is the threshold, always set to 1, unless otherwise indicated.

Finally, the refinement learning capability of the system was disabled.

To convert the hybrid system into pure connectionist architecture, a massive neural network was constructed based entirely on random weights. The economic statistics were represented by the input nodes and the buy or sell decisions were represented by the output nodes. The entire network was then trained with examples in data set B (Section 5.4.2).

## 5.5.1. Results of comparisons

With the adjustments and trainings described in the preceding paragraphs, a comparative study using data set A was performed. For simple statistics (i.e. where the federal government releases a single piece of economic statistic in a day), the results yielded by the three systems are shown in Table 5.

Table 5  
Comparative study for single statistics releases

<table><tr><td>No. of cases = 45</td><td>Integrated system</td><td>Pure rule-based</td><td>Pure neural network</td></tr><tr><td>Successful</td><td>45</td><td>42</td><td>39</td></tr><tr><td>Successful(%)</td><td>100%</td><td>93%</td><td>87%</td></tr></table>

For multiple statistics (i.e. where the federal government releases more than one piece of economic statistics in a day), the results are shown in Table 6.

## 5.5.2. Explanation of the observed results

The pure rule-based system fares less well compared to the refined integrated system. Its performance is the same as that of the initial netel knowledge base of the hybrid system before refinement training. However, since the rule-based system is not amenable to trainings, its knowledge base remains static. Its performance cannot thus be further enhanced through training.

It is also noted that the rule-based system fares worse than the neural network counterpart in its prediction during multiple statistics releases. This observation may be explained by the fact that under situation of increased uncertainty, training data collected from actual market movement is a better reflection of collective investors' sentiment than heuristic rules articulated by one expert trader.

As for pure neural network, it is not able to achieve the same level of performance as that of the netel based system. There are two major contributing factors:

Comparative study for multiple statistics releases

<table><tr><td>No. of cases = 15</td><td>Integrated system</td><td>Pure rule-based</td><td>Pure neural network</td></tr><tr><td>Successful</td><td>13</td><td>9</td><td>10</td></tr><tr><td>Successful(%)</td><td>87%</td><td>60%</td><td>67%</td></tr></table>

(i) Knowledge from human expert is able to provide a good leverage point for starting the neural learning in the integrated system.

(ii) The ability to represent human logic allows the netel knowledge base to have a closer mapping of the expert knowledge. This further improves the efficiency of the integrated system learning process.

## 6. Conclusion and future work

The netel approach of integrating expert system and neural network has demonstrated to be a feasible solution to the learnability - semantic dilemma. The system allows semantic rules and netels with trained numerical weights to co-exist in the knowledge base. Furthermore, the duality of netel rules allows users to deal with rule creation and edition just like any rule-based system. This design shields the users from the complicated task of manipulating the numerical weights of neural networks.

Another strength of NEULONET netels is its ability to represent human logic easily. This is a major advantage over pure rule-based expert system as logic used by human beings is generally much more complicated than what conventional AND/OR logic is able to express neatly. In fact, allowing the user to express rules using human logic will make the system easier to use as its inferencing process will be closer to the reasoning process of human beings.

Viewing from neural network point of view, allowing users to express their thought using human logic will bring the system thus formed to be closer to the global minima, therefore shortening the refinement training time.

Therefore, the netel approach is an improvement over rule-based system with a static knowledge base. It also has an advantage over pure neural network which can be trained only by “brute force” using historical data. In that case, human’s knowledge will not be able to put to use in a straight forward manner.

A few topics for further research are discussed here. Surkan and Xingren [25] suggest simplifying a trained neural network to derive some bond rating formulae. However, complete and accurate transformation can be difficult to attain, especially when the semantic structures of the underlying bond trading rules is buried in pure numerical values of the connection weights of the trained network [18]. With the use of NEULONET propagation and activation rules, and the guidelines of the construction algorithm, each trained NEULONET netels may be readily converted into equations representing the relationship of the antecedent and consequence nodes. This is especially the case for NEULONET as the weights assigned to edge links carry the semantic meaning of the logical operator [8]. Thus, as a continuation of this research, it would be worthwhile to devise an automated strategy to convert the trained netels into equations quantifying the decision process of the bond traders. Such rules and equations may be verified by the human expert, and in a way crystallize their knowledge into symbols and formulae.

A strength of neural network is its massively parallel architecture, whereby inference activities propagate simultaneously and in parallel on different paths from the input layer to the final output layer (conclusion nodes). The error back propagation process will run in a similar manner in the opposite direction. Thus, many network nodes may be concurrently updated and their activation states referenced by other nodes for activation computation. In a sequential machine, however, this “ideal” condition can only be simulated. Instead of adopting strategies such as heuristic search (Section 4.3.2) for backward chaining, parallelism is simulated by randomly picking a path for tracing. This should be applied to both forward and backward chaining. In fact, it will be interesting to see if the system can yield the same conclusion (or sufficiently close ones) for different consultation sessions using the same input parameters.

Finally, the netel-based shell may be further experimented with other application domains which are rich in human logic. Some possible domains are currency future option tradings, portfolio management, and computer performance evaluation.

## Acknowledgements

This project is sponsored by National University of Singapore research grant RP900628.

## References

[1] Arie Ben-David and Yoh-Han Pao, Self-Improving Expert Systems, Information and Management 22 (1992) 323–331.

[2] Izak Benbasat, Gerarcine DeSanctis, and Barrie R. Nault, Empirical Research in Managerial Support Systems: A Review and Assessment, in: Clyde W. Holsapple and Andrew B. Whinston, Eds., Recent Developments in Decision Support Systems (Springer-Verlag, 1993) 383–437.

[3] Robert W. Blanning and David R. King, Decision Support and Knowledge-Based Systems, Journal of Management Information Systems 6, No. 3 (1989) 3–6.

[4] A Bonarini and V Maniezzo, Integrating Expert Systems and Decision-Support Systems: Principles and Practice, Knowledge-Based Systems (1991) 172–176.

[5] Galen Burghardt, Morton Lane, and John Papa, The Treasury Bond Basis -- An In-depth Analysis for Hedgers, Speculators and Arbitrageurs (Probus Publishing Company, First Edition, 1989).

[6] Maureen Caudill, Expert Networks, Byte (October 1991) 108–116.

[7] S.C. Chan, L.S. Hsu, and K.F. Loe, Fuzzy Neural-Logic Networks, in: P.Z. Wang and K.F. Loe, Eds., Advanced In Fuzzy Systems: Applications and Theory 1, Ch. 2 (World Scientific Publication, May 1993).

[8] S.C. Chan, L.S. Hsu, K.F. Loe, and H.H. Teh, Neural Logic Networks, in: Omid M. Omidvar, Ed., Progress in Neural Networks 2 (Albex Publication, 1993).

[9] Paul N. Finlay, IT for Competitive Advantage: The Place of Expert Systems, Journal of Strategic Information Systems (1992) 126–133.

[10] Hans W. Gottinger and Peter Weimann, Intelligent Decision Support Systems, Decision Support Systems (1992) 317–332.

[11] Marco Guida, Paola Marchesi, and Giorgio Basaglia, Knowledge-Based Decision Support Systems for Manufacturing Decision-Making, Information and Decision Technologies 18 (1992) 347–361.

[12] Tim Hill and William Remus, Neural Network Models for Intelligent Support of Managerial Decision Making, Decision Support Systems 11 (1994) 449–459.

[13] Donggill Jung and James R. Burns, Connectionist Approaches to Inexact Reasoning and Learning Systems for Executive and Decision Support, Decision Support Systems 10 (1993) 37–66.

[14] Dave King, Intelligent Decision Support: Strategies for Integrating Decision Support, Database Management,

and Expert System Technologies, Expert Systems With Applications 1 (1990) 23–38.

[15] Staffan Lof and Bjorn Moller, Knowledge Systems and Management Decision Support, Expert Systems With Applications 3 (1991).

[16] Ho-Chung Lui, Ah-Hwee Tan, et al., Practical Application of a Connectionist Expert System – The Inside Story, in: Jay Liebowitz, Ed., Proceedings of the First World Congress on Expert Systems (Pergamon Press, December 1991) 21–29.

[17] David McSherry, Mcexpert: An Integrated Knowledge Elicitation and Consultation Environment for Multi-Criterion Decision Making, in: Jay Liebowitz, Ed., Proceedings of the First World Congress on Expert Systems (Pergamon Press, December 1991) 1715–1731.

[18] Larry Medsker and Harold Szu, Synergism of Neural Networks and Expert Systems, in: Jay Liebowitz, Ed., Tutorial Notes of the First World Congress on Expert Systems (Pergamon Press, December 1991).

[19] Marc H. Meyer, Arthur DeTore, Stephen F. Siegel, and Kathleen F. Curley, The Strategic Use of Expert Systems for Risk Management in the Insurance Industry, Expert Systems With Applications 5 (1992) 15–24.

[20] Hiroshi Narazaki and Anca L. Ralescu, A Connectionist Approach for Rule-Based Inference Using an Improved Relaxation Method, IEEE Transactions on Neural Networks 3, No. 5 (September 1992) 741–751.

[21] Tong-Seng Quah, Chew-Lim Tan, Hoon-Heng Teh, and Zuliang Shen, An Enhanced Neulonet for Rule-Based Reasoning, in: Proceedings of the World Congress on Neural Networks 1 (International Neural Network Society, July 1993) 605–608.

[22] Alan J. Rowe, Ivan A. Somers, and Hal Schutt, Management Use of Artificial Intelligence, Applied Expert Systems (1988) 55–70.

[23] Shimon Schocken and Gad Ariav, Neural Networks for Decision Support: Problems and Opportunities, Decision Support Systems 11 (1994) 393–414.

[24] Daniel Schutzer, Business Expert Systems: The Competitive Edge, Expert Systems With Applications 1 (1990) 17–21.

[25] Alvin J. Surkan and Xingren Ying, Bond Rating Formulas Derived Through Simplifying a Trained Neural Network, in: Proceedings of the International Joint Conference on Neural Networks (IEEE Neural Network Council and International Neural Networks Society, IEEE, November 1991) 1566–1570.

[26] C.L. Tan, T.S. Quah, and H.H. Teh, Implementation of Rule-Based Expert Systems in a Neural Network Architecture, in: Proceedings of The First World Congress on Expert Systems (Pergamon Press, December 1991) 1843–1851.

[27] C.L. Tan, T.S. Quah, and H.H. Teh, A Neural Logic Based Expert System, in: Proceedings of the Expert Systems Applications Conference (Institute for Industrial Technology Transfer, November 1991) 301–306.

[28] G.E. Touretzky, Boltzcons: Dynamic Symbol Structure in

a Connectionist Network, Artificial Intelligence 46, No. 12 (November 1990) 5–46.

[29] Robert Trippi and Efraim Turban, The Impact of Parallel and Neural Computing on Managerial Decision Making. Journal of Management Information Systems 6, No. 3 (1989) 85–98.

[30] Efraim Turban, Decision Support and Expert Systems - Management Support Systems (Macmillan Publishing Company, Second Edition, 1990).

[31] Stuart R. Veale, Bond Yield Analysis - A Guide to Predicting Bond Returns (New York Institute of Finance, First Edition, 1988).

[32] Peter Wann, Inside the US Treasury Market (Woodhead-Faulkner, First Edition, 1989).

[33] Rick L. Wilson, A Neural Network Approach to Decision Alternative Prioritization, Decision Support Systems 11 (1994) 431–447.

[34] Rick L. Wilson and Ramesh Sharda, Bankruptcy Prediction Using Neural Networks, Decision Support Systems 11 (1994) 545–557.

[35] Youngohc Yoon, Tor Guimaraes, and George Swales, Integrating Artificial Neural Networks with Rule-Based Expert Systems, Decision Support Systems 11 (1994) 497–507.

![](/api/attachments/J3S6Y9SQ/fulltext/images/4a0fb04c637ab70af53168c2e7e458a573fbbf9595655ce100204b5ac37a42ea.jpg)  
Tong-Seng Quah is a Ph.D. student at the Department of Information Systems and Computer Science, National University of Singapore. He obtained his MSc in 1990 and is now at the final stage of his Ph.D. programme. His research interests are expert systems, neural networks, decision support systems, multi-media technology, and commercial value of computer virus.

![](/api/attachments/J3S6Y9SQ/fulltext/images/fd249466364610a6201325a69d6eb5f911c7e479a242926b5692e18beaabcb25.jpg)

Dr. Chew-Lim Tan is a Senior Lecturer at the Department of Information Science and Computer Science, National University of Singapore. He obtained his Ph.D. from the University of Virginia in 1986. His current research interests are artificial intelligence, computer vision, natural language processing and expert systems.

![](/api/attachments/J3S6Y9SQ/fulltext/images/ff1c566e932819be3a0b70c056032ac4480078242fcf95f6851145c031d9a989.jpg)

Dr. Krishnamurthy S. Raman is presently Adjunct Associate Professor at the Department of Information Systems and Computer Science, National University of Singapore. From 1984 to 1993 he was Senior Fellow and Co-ordinator of the Information Systems Area of the Department. His research interests include organisational decision support systems, application of IT in small businesses, organisational assimilation of IT, and

governmental policy and diffusion of IT. He has published several papers in these areas and served as an Associate Editor of MIS Quarterly.

![](/api/attachments/J3S6Y9SQ/fulltext/images/e7df543ce1218b49b47667c9888a638f6f2f3bc40a787fa75c98fd7874c217df.jpg)

Dr. Bobby S. Srinivasan is at present working as a Senior Lecturer at Nanyang Technological University. Over the years he has published articles in the Journal of Industrial Engineering, Socio-economic Planning Sciences of Great Britain, Canadian Journal of Statistics, Canadian Journal of Cash Management, Security Industry Review, Asia-Pacific Journal of Management, Singapore Accountant, Stock Exchange Journal of Singapore, etc.

He has also written a text book titled Quantitative Analysis for Business Decision Making, wich was published by McGraw-Hill.
