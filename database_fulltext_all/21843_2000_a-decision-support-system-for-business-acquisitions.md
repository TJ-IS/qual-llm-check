---
otero_id: 21843
otero_key: "49MN6YYJ"
title: "A decision-support system for business acquisitions"
authors: "Kamalendu Pal; Owen Palmer"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00083-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision-support system for business acquisitions

Kamalendu Pal <sup>)</sup>, Owen Palmer

Department of Business Management, Greenwich College, Meridian House, Greenwich, London SE10 8RT, UK

Received 17 November 1999

## Abstract

In this paper, a hybrid Decision-support System for Business Acquisition Process DSBAP is presented. This applicationŽ . uses a hybrid knowledge-based system to place a bidding on the target company, formulating a strategy, and modification of the initial strategy if necessary for the acquisition processes. The whole system relies on two reasoning methods, rule-basedŽ . reasoning RBR and case-based reasoning CBR to assist in decision-making process for business professionals. It alsoŽ . Ž . describes an argument structure to generate plausible explanations for conclusion reached by RBR, and a means of integration with CBR. The RBR module dominates, but activates CBR explicitly at specific points in the reasoning process. The knowledge in rule form and previously decided case form are represented by using an object-oriented scheme. An overview of the functionality of the DSBAP system and a description of the represented knowledge are presented through the example of a set of business acquisition cases. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Hybrid decision-support system; Financial application of knowledge-based systems; Rule-based reasoning; Case-based reasoning; Business acquisition

## 1. Introduction

Decision-support systems DSSs are computer-Ž . based tools that help managerial decision-making by presenting information and interpretations for various alternatives. Such systems can assist managers in making strategic decision 2,40 . In the 1990s,<sup>w</sup> <sup>x</sup> knowledge-based systems development methods have been playing an important role in a new generation of decision-support tools sometimes known as Intelligent Decision Support Systems. The ability of such systems in processing knowledge has led to cost savings, faster decision process, good payoff, and significant competitive advantage 3,7,12,15,19, <sup>w</sup> 23,34, .<sup>x</sup>

There are three important approaches in the development of current business DSSs:

1. Rule-based reasoning RBR 17,18,21,24,37 ;Ž . <sup>w</sup> <sup>x</sup>

2. Case-based reasoning CBR 1,10,16,31 ; and Ž . <sup>w</sup> <sup>x</sup>

3. Hybrid i.e., a combination of RBR and CBRŽ <sup>w</sup> <sup>x</sup> 5,14,22,32 or an integration of other reasoning methods 29,35 .<sup>w</sup> <sup>x</sup>.

Each focuses on enriching some aspects of the traditional knowledge-based business DSSs.

In RBR systems, the specialised domain knowledge is represented as a set of IF ² precondition s( ): THEN ²conclusion s( ): rule format. It is often extremely difficult to obtain an appropriate set of rules in an application domain to cover all possible eventualities. Moreover, in certain circumstances whereŽ the situation is not so clear , decision-makers have. often relied on previously solved cases that are similar to the new case in hand. This reasoning process, where the past experiences are used in solving a new case, is known as CBR. The previously resolved cases can bridge at least some of the problems encountered in an RBR system by representing exceptions to the rule in the form of cases. This is Ž . because the facts of the previously resolved cases, like those of new cases, are expressed in the case-description language.

What is required, then, is a knowledge-based DSS that respects relevant information expressed in rules but that also comes closer to the task that confronts the business professional: the analysis of the present business situation in terms of previous experiences. This requires use of both RBR and CBR in an integrated environment 25 . There are numerous<sup>w</sup> <sup>x</sup> domains in which it is important to combine RBR and CBR, for example, the legal 5,32 and financial<sup>w</sup> <sup>x</sup> domains 11 . This paper is concerned with an imple- <sup>w</sup> <sup>x</sup> mented prototype system, Decision-support System for the Business Acquisition Process DSBAP ,Ž . which also integrates RBR and CBR.

## 2. Integration of RBR and CBR

In general, there are three different ways to combine RBR and CBR: i keep RBR and CBR as twoŽ . ‘‘equal’’ reasoning modules; ii let the CBR moduleŽ . use the inference capability of rules when needed; and iii have the RBR module dominate and make Ž . use of CBR categorically at particular points in the reasoning process.

The research of Rissland and Skalah 32 is an<sup>w</sup> <sup>x</sup> example of the first approach. They have built a system called CAse-BAsed REasoning Tool Ž . CABARET , as a hybrid system, which integrates RBR and CBR. CABARET’s application domain is that of income tax law concerning the deduction for expenses relating to an office maintained in one’s home. It deals with the circumstances under which a taxpayer may legitimately deduct, on a United States income tax return, expenses relating to an office return, expenses relating to an office maintained at the taxpayer’s expense. The integration of RBR and CBR methods is performed by using control heuristics. These control heuristics suggest how to interleave RBR and CBR to produce an argument to support a certain interpretation. CABARET interleaves CBR and RBR dynamically.

The second paradigm is exemplified by the work of Bonissone et al. in the development of the CARS system 4,9 . The CBR module in CARS is the<sup>w</sup> <sup>x</sup> dominant system and it activates PRIMO 8 , a rule-<sup>w</sup> <sup>x</sup> based reasoner that contain plausible rules of abstraction, evaluation, and modification. The rules in the PRIMO system are used in case indexing to augment the case. In case retrieval, the rules combine the similarity measures computed across the abstract features of cases.

The research presented in MARS 11 is an exam- <sup>w</sup> <sup>x</sup> ple of the third approach to combining RBR and CBR. In MARS, rules are used to represent the domain expertise that is required for structuring various parts of company mergers and acquisition deals or deciding upon the best course of action to determine which company to select as a possible target. CBR is activated by selective rules that state the need for integration. The RBR module dominates, but activates CBR explicitly at specific points in the reasoning process.

The present research i.e., DSBAP is also anŽ . example of the third approach to integrating RBR and CBR. In DSBAP, the business acquisition domain knowledge is represented mainly in different types of rule form. The system covers three aspects of a business acquisition process, namely, company Õaluation, strategy formulation, and strategy modification. The CBR module is explicitly used at the time of strategy modification only.

The MARS project was developed for the domain of mergers and acquisitions. However, DSBAP deals with the British business acquisitions only. In MARS, the individual cases are represented using rule templates. Hence, the integration of CBR and RBR was achieved without altering the inference engine of RBR. The DSBAP system research uses an objectoriented knowledge representation technique instead of abstracting the case description into rule form.

The main differences between DSBAP and MARS are: i DSBAP support a partial rule-based adviceŽ . facility, whereas MARS does not support any such

Table 1

facility; and ii DSBAP provides an argument struc-Ž . ture to generate plausible explanations for conclusions reached by RBR, and a means of integration with CBR. But in MARS, there is no argument generation facility and the integration technique of RBR and CBR is different from that of DSBAP.

The paper contains five other sections. Section 3 introduces the basic idea of RBR and CBR. Section 4 presents the overview of our system DSBAP and gives a short description of the domain of the research. The knowledge-representation scheme is provided in Section 5. In particular, the similarity-assessment technique of the CBR part of DSBAP and different types of system outputs for a particular acquisition case are presented in Section 6. Finally, Section 7 provides some concluding remarks.

## 3. Basic ideas of RBR and CBR

This section gives a basic outline of RBR and CBR. In particular, it indicates how DSBAP’s knowledge base makes use of these reasoning methods.

## 3.1. RBR

It is often possible to represent declarative knowledge in the form of IF ² precondition s( ): THEN ²conclusion s( ): rules. Therefore, a typical rule has two parts: the precondition and the conclusion. The precondition contains information on which facts or situations must be true for the rule to be used. If these match exactly to facts of the current applications, the rule fires, and the conclusion then presents information on the consequences of the match.

For example, a small set of rules is shown in Table 1. These rules determine how the status ‘raider should send a copy of the notice to the company’ may be obtained 33 . There is one rule having<sup>w</sup> <sup>x</sup> ‘raider may give notice for the rest of the shareholders’ as the consequence, and another rule having as its precondition ‘raider may give notice for the rest of the shareholders’. This is a simple instance of how one can reason about even limited rule structures.

In essence, rules have enabled knowledge base designers Ž . KBD to represent problem-solving knowledge as models that could be implemented computationally. In rule-based systems, knowledge is represented as facts about the world i.e., relation-Ž ships between entities, e.g., A B and mechanisms. Ž . known as inference engine for manipulating the facts.

One might construct a network of rules that interconnect to form a repository of knowledge, known as a rule base. The reasoning architecture of rule-based systems has such a rule base plus an inference engine that performs inferences e.g.,Ž forward or backward chaining, or a combination of these two .. The general reasoning process of a rule-based system is shown in Fig. 1. Given a new case, applicable rules are first found by matching against the rules of the rule base. Then intermediate results are generated by the chosen inference mechanism, and the process is repeated until the desired solution state is reached. In the present business acquisition application, four different categories of rules are used. The syntax and purpose of these categories are discussed in the latter part of this paper. Next, we are going to explain how to develop knowledge-based systems that use previously solved cases to perform some of the CBR task s .Ž .

## 3.2. CBR

The main idea of CBR is to adapt solutions that were used to solve old problems and use them for solving new problems or cases . In other words,Ž . people reuse all their past problem-solving experience to deal with a new case e.g., Refs. 20,26,27 .Ž <sup>w</sup> <sup>x</sup> A CBR system consists of a case base Žwhich is the set of all cases that are known to the system and an. inferencing mechanism to derive a solution from the stored cases. Moreover, CBR follows a different process than RBR and when a new case is presented to the system, it proceeds as follows.

<table><tr><td colspan="2">A small set of rules relevant to business acquisitions</td></tr><tr><td>IF &lt;precondition(s)&gt; THEN &lt;consequence(s)&gt;</td><td>Symbolic representation</td></tr><tr><td>IF raider has contracted ninety percent of the sharesTHEN raider may give notice for the rest of the shareholders</td><td>A → B</td></tr><tr><td>IF raider may give notice for the rest of the shareholdersTHEN raider should send a copy of the notice to the company</td><td>B → C</td></tr></table>

![](/api/attachments/49MN6YYJ/fulltext/images/a541b88ea889a2b37018eeb59df949c3c9997f9574587b3c051050495b816ecd.jpg)  
Fig. 1. RBR process.

<sup>Ø</sup> The CBR system find those cases in the case base that solved problems similar to the current problem in hand, in a selection process.

<sup>Ø</sup> If at least one similar case is found, then the system retrieves that particular case and attempt to modify it if necessary , taking into account anyŽ . difference between the current and previous situations, to produce a potential solution for the new case. This process is known as adaptation.

The important steps in the inferencing mechanism of a CBR system are shown in Fig. 2. Finding relevant cases involves

<sup>Ø</sup> characterising the input problem, by assigning appropriate features to it,

<sup>Ø</sup> retrieving the cases from the case base withŽ . those features, and

<sup>Ø</sup> picking the case or cases that match the input best.

More formally, one can say that a previously solved case consists of a pair H, D where H standsŽ . for a case history and D is a decision for H. A case base is a set of such cases. Considering the discretionary nature of business acquisition related reasoning, one can assume that $\left( \mathrm { H } , \mathrm { D } _ { 1 } \right)$ and $\left( \mathrm { H } , \mathrm { D } _ { 2 } \right)$ does not imply $\mathbf { D } _ { 1 } = \mathbf { D } _ { 2 }$ . DSBAP’s CBR part operates as follows:

1. Receive a new case description $\mathrm { H } _ { n } .$

2. Select the case or cases $\{ ( \mathrm { H } _ { 1 } , \mathrm { D } _ { 1 } ) . . . ( \mathrm { H } _ { m } , \mathrm { D } _ { m } ) \}$ from the case base such that $\left\{ \operatorname { H } _ { 1 } \ldots \operatorname { H } _ { m } \right\}$ and $\mathrm { H } _ { n }$ are ‘similar ’.

3. Use the past decisions $\{ \mathsf { D } _ { 1 } \ldots \mathsf { D } _ { m } \}$ for $\left\{ \operatorname { H } _ { 1 } \ldots \operatorname { H } _ { m } \right\}$ to form the final decision $\mathrm { D } _ { n }$ for $\mathrm { H } _ { n }$

To assist this process, an automated business acquisition CBR system should find the cases that are most similar to the new case and each of them may therefore act a potential candidate for the new case. But this choice, which is cognitively a complex activity, is usually approximated by some simple metric scheme in case-based computing. Such a metric scheme for the present research work is described in the later part of this paper.

![](/api/attachments/49MN6YYJ/fulltext/images/78e05e1106764da1aee77e405dbac993f719d698a0821d5f96120147120b1d19.jpg)  
Fig. 2. CBR process.

## 4. Overview of DSBAP

DSBAP has been developed as a pure research product. The knowledge base consists of a rule base and a case base. The system covers three aspects of a business acquisition process, namely company valuation, strategy formulation, and strategy modification. It provides a text-based user interface and collects facts for a new case in a question-answering session with its user. The user inputs a case description to DSBAP and can select any of the appropriate options Ži.e., company valuation, strategy formulation, and strategy modification from the system menu. In the. case of first two options, the system provides advice for the user by using rules from the rule base only.

But in the case of the strategy modification option, the system uses both RBR and CBR in an integrated environment. The computational framework for DS-BAP is shown in Fig. 3. The different aspects of the system are discussed in the following subsections.

## 4.1. Company Õaluation

An acquisition process starts when the raider Ž . who usually initiates an acquisition attempt chooses a target Žwhich is the company of interest to the raider for takeover. The next important considera- . tion in any acquisition is the ability of the raider company to place a value on the target company. However, placing a value on a company is a very complicated process and there are no straightforward rules for doing this. It is possible to come up with a number of different valuations for a single company. Moreover, two raider companies can arrive at with different valuations of the same target company due to the different plans that each has for the target. Each method of valuation has its associated advantages and disadvantages and will be more or less appropriate according to the intentions of the raider towards its target. The different methods of company valuation used for the present project are: stock market Õaluation, net asset Õaluation, capitalised earning Õalue method, profit<sup>r</sup>earning PŽ . <sup>r</sup>E ratio Õaluation, Gorden growth model Õaluation, and discounted cash flow Õaluation. The detailed treatments for these methods can be found in any standard textbook on corporate finance e.g., Refs. 6,28 .Ž <sup>w</sup> <sup>x</sup>.

![](/api/attachments/49MN6YYJ/fulltext/images/327c7fe3b4a79ce7db32fd430705f8db8b54d22e8864813d7bc678a0a7ae39c4.jpg)  
Fig. 3. The computational framework for DSBAP.

## 4.2. Strategy formulation

In any acquisition process, strategy and tactics of the raider company play a very important role. Before a raider becomes involved in an acquisition process, it must satisfy itself that acquisition represents a more efficient alternative than organic growth or the independent purchase of required assets. Once a company has satisfied itself on these points, the strategic process that it should follow towards acquiring a target company can be summarised as follows:

<sup>Ø</sup> Select appropriate target companies.

<sup>Ø</sup> Find as much information about the target companies as possible.

<sup>Ø</sup> Value each of the possible target companies using the collected information.

<sup>Ø</sup> Determine which of the possible target companies is most suitable.

<sup>Ø</sup> Decide upon the best way to finance the acquisition, taking into account which methods of payment are agreeable to the shareholders.

Once a raider company has gone through this strategic process, it must then decide upon the acquisition tactics it will use. Failure to employ the right tactics can result in a predator paying over the odds or, in the worst-case scenario, failing to acquire its target altogether. In addition, companies must be aware of the rules and regulations governing acquisitions.

## 4.3. Strategy modification process

The target’s response Ž . acceptance or defiance to the raider’s acquisition offer determines how the raider subsequently modifies the chosen strategy. For example, a minority shareholder may refuse to sell his or her shares to the raider. In that situation, the raider may look for an alternative strategy e.g., an Ž approach involving exploitation of legal issues to . acquire the minority shares.

Keeping this brief introduction and the functionality in mind, we are now going to discuss the knowledge representation scheme for DSBAP.

## 5. Knowledge representation in DSBAP

Object-oriented knowledge representation method is used in DSBAP. The object-oriented method can be traced back to its pioneering days with SMALLTALK 13 . A good review of the approach<sup>w</sup> <sup>x</sup> can be found in Ref. 38 . We present a brief descrip-<sup>w</sup> <sup>x</sup> tion of it here to facilitate the discussion in the rest of the paper.

The object-oriented knowledge representation approach reflects our natural perceptions of the world as being composed of objects, classifiable into general types. This involves thinking about the world as a set of entities or objects that are related to and communicate with one another. Each real-world entity e.g., any thing, idea, or concept is modelled by Ž . an object. Each object is associated with a unique identifier that makes the object distinguishable from other objects. Each object has a set of attributes and methods operations . The value of an attribute can Ž . be an object or a set of objects. The set of attributes of an object and the set of methods represent the object structure and behaviour, respectively. The attribute values represent the object’s state. This state is accessed or modified by sending messages to the object to invoke the corresponding methods.

Objects sharing the same structure and behaviour are grouped into the same class. A class represents a template for a set of similar objects. Each object is an instance of some class. A class definition consists a set of instance attributes or simply attributes andŽ . methods. Strictly speaking, we should refer to a kind of an object such as a VRULE in Fig. 4 as anŽ . object type and a specific occurrence of that kind of object such as VRULE01 as an object instance. AnŽ . object class describes a set of object instances that have similar

<sup>Ø</sup> data characteristics,

<sup>Ø</sup> behaviour,

<sup>Ø</sup> relationships to other objects, and

<sup>Ø</sup> real-world meaning.

A case report as shown in Fig. 9 may have a Ž . name, source, court name <sub>–</sub> , participants, facts, main surface features, and so on. Thus, a specific case report e.g., CASE04 is an instance of the case Ž . report class. Individual object instances can be distinguished from other instances by differences in the actual values of the attributes and by associations with other object classes and object instances. Object instances that are members of the same class share a common real-world meaning in addition to their shared attributes and relationships.

Object models can be simplified by defining hierarchies of data structures. Two common kinds of data hierarchy are generalisation Žkind of or class structure and. Ž aggregation part of or object structure . Thus, generalisation is a kind of hierarchy. defines a relationship among classes, as shown in Fig. 4. Another type of hierarchies is aggregation. Aggregation relationships depict ‘part of’ hierarchies, as shown in Fig. 9 for a case description.

In DSBAP, all items of interest in the application domain, such as different aspects of case reports Ži.e., main surface features, case description, and case outcome , rules, and methods to manipulate. them are modelled as objects. Among them are aggregation association and generalisation association. For example, the ‘rule base’ consists of aggregation association of different classes of rules: V-type rules company valuation rules , S-type rules Ž . Ž . Ž strategy formulation rules , M-type rules strategy modification rules , and C-type rules control rules . . Ž .

![](/api/attachments/49MN6YYJ/fulltext/images/89868f8cfa79d973c7c71cc9b6f0b32a19f88dbbb1d9763b44d3df50bbde6b08.jpg)  
Fig. 4. The rule base organisation of DSBAP.

The rule base consists of 70 rules related to the different function of the system. The organisation of the rule base is shown in Fig. 4.

## 5.1. Organisation of rule base

In the present business application, four main types of rules are used: Õaluation rule, strategy formulation rule, control rule, strategy modification rule. The strategy modification rule set consists of two further subcategorise of rules: aÕailable-action s( ) rule and prediction rule. The descriptions and examples of the valuation rule, strategy formulation rule, and control rule are shown in Table 2.

## 5.1.1. Strategy modification rules

The strategy modification rules are used to modify the initial strategy whenever a problem arise in the acquisition process.

5.1.1.1. AÕailable-actions rules. The available-action s type of rule involves a straightforward trans- Ž .

formation of business statute law to rule form. An example of this type of rule is shown in Fig. 5. The label of the rule in Fig. 5 begins with ‘A’, to denote the type. An ‘A’ rule determines whether or not a court has the power to act or take a specific action. For example, an English court has a range of options available in a minority shareholder protection order case as itemised below:

raider shall not be entitled to acquire the minority shares;

– alteration of the terms of acquisition.

The available-action s rules determine which ofŽ . the option is applicable in a case.

In order for rules to be applied for a new problem, and, hence, for a rule-based system to be of any use, the system will need to have access to facts of that situation. In rule-based analysis, the valuation rules, the strategic rules, the control rules, the plan modification rules, and the available-action s rules areŽ .

Table 2  
Description of different types of rule

<table><tr><td>Different categories of rule</td><td>Example</td></tr><tr><td>Valuation rule: The valuation rules are used for target company valuation purpose. Each of these rules has a unique name (e.g., VRULE01, VRULE02, etc.) beginning with ‘V’.</td><td>VRULE01IFfixed assets? fanet current assets? ncalong term debt? ltdnet asset value (nav) = fa + nca - ltdTHENThe net asset value of the company is nav.</td></tr><tr><td>Strategy formulation rule: The strategy formulation rules are used to formulate a plan for the proposed business acquisition. The label of strategic rules starts with ‘S’ (e.g. SRULE01, SRULE02, etc.).</td><td>SRULE01IF(business type is restaurant)(target restaurant is well known for its food quality)(restaurant has been taken over by a raider)THENIn a strategic restructuring process, it is recommended not to replace the chef of the target restaurant.</td></tr><tr><td>Control rules: The control rules are used for rule-execution and other knowledge-manipulation purposes. Each of these rules has a unique name (e.g., CRULE01, CRULE02, etc.) beginning with ‘C’.</td><td>CRULE01IFSelection ? type = ‘company valuation’THENChoose all company valuation rules.</td></tr></table>

used as in a conventional expert system in one ofŽ . two modes: response or no response. A response is produced when all the preconditions of a particular rule are matched by the facts of the new problem in hand. However, when this situation does not hold, such rules are not considered in determining any conclusion.

5.1.1.2. Prediction rules. A prediction rule predicts actions a decision-maker is likely to take. When all the preconditions of a prediction rule are matched by the facts of a problem, the rule can give unconditional advice. The predictive rule-based part is able to produce some tentative or partial advice, which may be helpful or informative for the user. The prediction rules can generate any of three types of output: clear-prediction, speculation, or no-prediction. Clear-prediction is possible when at least one of the prediction rules has fired as a consequence of the facts of the new problem. The system presents what one can call speculation by applying a weighting criterion to the rule preconditions that are true, even when none of the rules is fired. A speculation consists of conclusions that would have followed if all the preconditions of a rule that has some relevance had been true, and also output focusing on the failed preconditions i.e., reasons why a conclusion cannot Ž be accepted without reservations ..

![](/api/attachments/49MN6YYJ/fulltext/images/380997d99f8904b46fa2251798a2a5dfb00b013b4d7b0e2bd26c4ea0cd69011b.jpg)  
Fig. 5. An ‘available-action s ’ rule for a minority-shareholder-protection order. Ž .

The first step in generating a speculation is to identify the rules that are nearly fired. A scoring mechanism is used to determine which rules are closest to firing. For this scoring mechanism, the preconditions of the prediction rules can be divided into three sub-classes: peripheral, significant, and essential. The justification for the scheme exemplified by equation 1 is as follows. In examining theŽ . previously decided case reports and the acquisition related legal text sources e.g., Refs. 28,30 , it wasŽ <sup>w</sup> <sup>x</sup>. observed that some of the preconditions of the rule base were of secondary importance in drawing conclusion from a rule and some were of little significance. Hence, the preconditions here fall into the above categories. Peripheral preconditions are of secondary importance in drawing a conclusion and are helpful in practice to provide information about the context. Essential preconditions are those that are critical in drawing conclusions. Significant preconditions are those that fall between essential and peripheral, in that though they are important when drawing the conclusion, they are not critical on their own.

Each of these rules has a unique name e.g., Ž BRULE01, BRULE02, etc. beginning with ‘B’. At. the time of specifying these rules, proper interpretation of the different business norms 28,30 and experts’ specific domain knowledge were taken into consideration. For example, the structure of a prediction rule is shown in Fig. 6.

It is found by experiment that there is a consistent threshold i.e., 0.40 in our score, below which anyŽ . information that DSBAP may give is unhelpful. A value of 0.40 or above in a scoring range between 0 and 1 indicates that the rule has some significant ability to provide a contribution towards advice that the user is likely to find helpful. The threshold value was determined by actual checks of relevance of retrieved material at a late stage of the knowledgeacquisition process. The system, therefore, offers no information unless at least one of its prediction rules has a score above the threshold. If there is no such score, one can say that the output is of a no-prediction type. The score $\left( { \mathrm { S c o r e } } _ { \mathrm { R i } } \right) $ of a predictive rule. can be defined as follows:

![](/api/attachments/49MN6YYJ/fulltext/images/7db7e399ecaa87b12d4291a230f0704584b64ae70b1ba11b8f27f4be415d5a1b.jpg)  
Fig. 6. A ‘prediction’ rule for a minority shareholders protection order.

![](/api/attachments/49MN6YYJ/fulltext/images/c74336626cb7ac25eca7e6ef2b219a05f485f8177616122a5bdb27e660ddd3c1.jpg)  
RES = Response NRE = No-response CPR = Clear-prediction SPE = Speculation NPR = No-prediction  
Fig. 7. Different types of behaviour leading to rule-based output.

$$
\mathrm{Score} _ {\mathrm{Ri}} = \frac {\mathrm{Score} _ {\mathrm{u}}}{\mathrm{Score} _ {1}}\tag{1}
$$

where Score $\ l _ { \mathrm { u } } = w _ { 1 } N _ { \mathrm { e } } + w _ { 2 } N _ { \mathrm { s } } + w _ { 3 } N _ { \mathrm { p } }$ and Score is the total number of preconditions of the rule in the equation. $N _ { \mathrm { e } } , \ N _ { \mathrm { s } } , \ N _ { \mathrm { p } }$ are the numbers of essential, significant and peripheral preconditions that are true for the current case. The weighting factors $w _ { 1 } , \ w _ { 2 }$ and $w _ { 3 }$ are for essential, significant and peripheral categories of preconditions. It has been found that the most convincing behaviour of DSBAP occurs when $w _ { 1 } = 0 . 7 5 , \ w _ { 2 } = 0 . 6 2$ , and $w _ { 3 } = 0 . 2 5$ . Moreover, these values were also agreed upon by the domain expert based on the retrieved information from the prototype system.

The prediction rules explain how a decision-maker is likely to act within the range of option available, which is circumscribed by the available-action sŽ . rules. One can say, for the purpose of distinction, that the available-action s rules give available ac-Ž . tion s with respect to the available options and the Ž . predictions rules provide prediction about what a decision-maker may conclude for a particular situation.

When a user asks for rule-based advice, DSBAP can provide one of three possible options: comprehensiÕe adÕice, partial adÕice, and no adÕice. In comprehensive advice, the system provides the possible available action s plus a predictive decision,Ž . provided that at least one of the prediction rules has fired. The partial rule-based advice can be in one of two categories. For category one of partial rule-based advice, DSBAP offers the relevant available action sŽ . and also presents a speculation. Category two of partial rule-based advice produces no prediction or speculation but does suggest some valid available action s . Finally, the system provides no rule-basedŽ . advice at all when it fails to come up with available action s or any kind of predictive information. TheseŽ . different types of behaviour leading to rule-based output are shown diagrammatically in Fig. 7. Additionally, the strategic modification module has a facility to generate argument for the advice.

## 5.1.2. Argument mechanism in DSBAP

In general, an argument consists of preconditions and conclusion of a RBR when at least one of the rules has fired. There is a vast literature on theories of argumentation, but we have used a simple theory proposed by Toulmin 39 . Toulmin Ref. 39 , p.126<sup>w</sup> <sup>x</sup> Ž <sup>w</sup> <sup>x</sup> . presents an interesting and commonsensical example of defensible reasoning: 1 Anne is one of Jack’sŽ . sisters; 2 All Jack’s sisters have previously been Ž . observed to have red hair; 3 So, presumably, AnneŽ . now has red hair, unless Anne has dyed her hair, gone white, lost her hair, etc. Toulmin has his own diagrammatic approach to representing arguments. In its simplest form, Toulmin’s model states that an argument can be thought of as a statement that a given set of data lead to a claimed result the claimŽ . as shown in Fig. 8.

![](/api/attachments/49MN6YYJ/fulltext/images/2cb95b54953c79e17d6957e0a714ab0488150155149500d9fbf9e9613c6d8688.jpg)  
Fig. 8. Toulmin’s argument structure.

In Toulmin’s theory, all arguments consists of four basic components: claim, data, warrant and backing. The assertion of an argument stands as the claim of the argument. Knowing the data and the claim does not necessarily convince one that the claim follows from the data. A mechanism is required to justify the claim given the data. This justification is known as the warrant. Useful warrants are based on analogies between cases, or even on the authority of a given speaker. Moreover, a warrant is a true reflection of the expertise used by a subject in solving a problem. The backing of an argument supports the validity of the warrant.

DSBAP’s argument mechanism uses legislative information and previously resolved case s for back-Ž .

ing. As this body of knowledge involves both cases and rules, the system uses both RBR and CBR in an integrated environment to produce an argument. A later part of this paper describes how this argument structure is used in DSBAP, with an example. First, it is important to explain how to develop business knowledge-based systems that use previous experience or previously solved cases to perform CBR Ž . tasks.

## 5.2. Organisation of case base

The present case base is comprised of 20 manually coded cases, labelled CASE01, CASE02, and so on. This can be expanded incrementally as new cases are collected. The overall organisation of a case description is shown in Fig. 9, where CASE04 illustrates some of the structure that occurs in each of the cases in the case base. The case\_index attribute refers to the unique characteristic associated with the case. For example, case index for CASE04 is IN-<sub>–</sub> DEX04 as shown in Fig. 9. For CASE04, the IN-DEX04 points to its characteristic features ‘right of minority shareholders’, ‘business type is restaurant’, ‘applicant is one of the shareholders’, ‘respondent is the raider’, ‘offer relates to purchase of the share’, ‘offer relates to a particular class of shares’, ‘respondent contracted 90% of the share’, ‘4 months has passed since the date of the offer’.

![](/api/attachments/49MN6YYJ/fulltext/images/f48d84ff53f3fa054ac480c13a992ee07aba6c950360ea3be3e61ea0e50f46b0.jpg)  
Fig. 9. The overall organisation of a case representation.

The case name <sub>–</sub> attribute is the name associated with a particular case. The source attribute represents the source of the case report. For example, the case in Fig. 10 has been published in the Butterworths Company Law Cases BCLC for 1992, at page 192. Ž .

The court name attribute is the name of the court that ruled on the case. In the present circumstance, COURT001 represents the ‘Chancery Division com-Ž panies court ’. The participants attributes contain all. the information associated with the participants and the relationships among them.

The fact attribute represents the history of the case briefly. Similarly, the appeal data structure describes who has applied for the present case, how many shares he or she has and the type of the shares Ž . e.g., ordinary or preference shares .

In the case base side of DSBAP, the cases that have the highest similarity rating with respect to a current problem are retrieved, and used for generating the argument for rule-based advice. The similarity is judged by comparing the main facts and events recorded in the histories of the cases. The similarity measure is based on numerical taxonomy 36 . <sup>w</sup> <sup>x</sup>

![](/api/attachments/49MN6YYJ/fulltext/images/7773be3a7d364f71f52bec9316c31cbc0d63fd96027f6e1f8adb40271d914939.jpg)

[b]that the shares which the offeror has acquired or contracted to acquire by virtue of acceptances of the offer, together with the shares held by the person or persons mentioned in paragraph [A], amount to not less than the minimum specified in the subsection; and

Fig. 10. Argument structure in DSBAP.

<table><tr><td colspan="3">Valentino Restaurants — key financial information</td></tr><tr><td colspan="2">Profit before interest and tax (PBIT)</td><td>£660,000</td></tr><tr><td colspan="2">Interest paid</td><td>£72,000</td></tr><tr><td colspan="2">Corporation tax</td><td>£176,400</td></tr><tr><td colspan="2">Distributable earnings</td><td>£411,600</td></tr><tr><td colspan="2">Earnings per share (EPS)</td><td>16.7p</td></tr><tr><td colspan="2">P/E ratio</td><td>12.87</td></tr><tr><td colspan="2">Market price of ordinary shares</td><td>£2.15</td></tr><tr><td colspan="2">Equity beta</td><td>1.17</td></tr><tr><td colspan="3">Gross profit forecast</td></tr><tr><td>Year</td><td>Sales</td><td>Increase</td></tr><tr><td>1995</td><td>205,000</td><td>-</td></tr><tr><td>1996</td><td>250,000</td><td>21.95%</td></tr><tr><td>1997</td><td>310,000</td><td>24.00%</td></tr><tr><td>1998</td><td>411,600</td><td>32.72%</td></tr><tr><td colspan="3">Dividends</td></tr><tr><td>Year</td><td colspan="2">Dividend</td></tr><tr><td>1998</td><td colspan="2">15p</td></tr><tr><td>1997</td><td colspan="2">14p</td></tr><tr><td>1996</td><td colspan="2">12p</td></tr><tr><td>1995</td><td colspan="2">10p</td></tr></table>

To illustrate the functionality of DSBAP’s target valuation, strategy formulation, and its strategy modification facilities, consider the example of the Ravenna Restaurants case, which involves a minority-shareholder-protection order issue. The bare facts of this case are stated in Section 6.

## 6. Example: minority-shareholder-protection order related case

Ravenna Restaurants is an Italian restaurant situated in southwest London. It was established 20 years ago, owned by two brothers, and is a wellknown restaurant for its authentic Italian food. One brother is the chef, and the other is the business manager. The chef is Nicholas Ladenis and business manager is Peter Ladenis. In the same locality, Valentino Restaurants is another Italian restaurant, which was set up in 1993. Ravenna Restaurants has distributable earnings of £727,000, a weighted average cost of capital of 14% and a P<sup>r</sup>E ratio of 18.7. It is in the process of acquisition of Valentino Restaurants whose financial details are as follows:

Valentino Restaurants — balance sheet 1998

<table><tr><td colspan="3">Valentino Restaurants — balance sheet 1998</td></tr><tr><td></td><td>£000</td><td>£000</td></tr><tr><td>Fixed asset</td><td></td><td>265</td></tr><tr><td>Current assets</td><td>60</td><td></td></tr><tr><td>Current liabilities</td><td>43</td><td></td></tr><tr><td>Net current assets</td><td></td><td>17</td></tr><tr><td></td><td></td><td>282</td></tr><tr><td>Long-term debt</td><td></td><td>72</td></tr><tr><td></td><td></td><td>210</td></tr><tr><td>Financed by:</td><td></td><td></td></tr><tr><td>Ordinary shares (50p)</td><td></td><td>123</td></tr><tr><td>Reserves</td><td></td><td>87</td></tr><tr><td></td><td></td><td>210</td></tr></table>

Valentino Restaurants is optimistic that it will be able to maintain an annual increase in distributable earnings of 5% per annum due to anticipated synergy as a result of the takeover. The company will also be able to sell duplicated assets which will realise £60,0000 in 1 year’s time. The risk-free rate of return is 9% and the return on the market as a whole is 15%.

On 31 January 1999, Nicholas and Peter wrote to the petitioner, a shareholder in Valentino Restaurants, repeating an invitation that had been made before to all shareholders, that the petitioner offer his shares to them for purchase and stating that the invitation would remain open until 28 February 1999. The date within which shareholders could take up the invitation was subsequently extended to 10 March. The petitioner was served with a notice under Section 429 of the Companies Act 1985 to buy out his shares at 40 pence. The Section 429 notice sent to the petitioner was not signed by the Ladenis brothers but by their solicitor and the statutory declaration under Section 429 4 was not made until 2Ž . weeks after the first notice had been given.

In a question-answering session, DSBAP gathers the facts of this particular case. The facts are as follows: ‘business type is restaurant’, ‘applicant is one of the shareholders’, ‘respondent is the raider’, ‘right of minority shareholders’, ‘offer relates to purchase of the shares’, ‘offer relates to a particular class of shares’, ‘respondent contracted ninety percent of the share’, ‘offer notice has been given to the applicant’, ‘three months has passed since the date of the offer’.

When a user selects the company valuation mode of DSBAP for this case, the system provides the target valuation analysis as follows:

The valuation of Valentino Restaurants that has been obtained:

Stock market valuation<sup>s</sup>£529,000

Net asset valuation using book valueŽ .<sup>s</sup>£210,000

Capitalised earning value<sup>s</sup>£528,000

P<sup>r</sup>E ratio valuation<sup>s</sup>£528,000 or £682,000

or £769,000

Gorden growth model valuation<sup>s</sup>£771,000

Discounted cash flow valuation<sup>s</sup>£861,000

The accuracy of different valuations will depend on the reliability of the information used. Which valuation method is most appropriate will depend upon the information available to you. The above output is designed to help the user to arrive at a reasonable decision. Using the same case, we now describe how DSBAP formulates the initial strategy by the following.

The strategy for the present case includes the following.

<sup>w</sup> <sup>x</sup> 1 This restaurant business has demonstrated very good growth and exhibits that it is under excellent management. Moreover, it is well established that small restaurants have rather traditionally considered their approximate values to be slightly under 1<sup>=</sup> gross income 41 . For this restaurant, the approxi- <sup>w</sup> <sup>x</sup> mate initial bidding price would be:

0.75<sup>1 =</sup>£441,600<sup>s</sup>£331,200

<sup>w</sup> <sup>x</sup> 2 There are two options to finance the present acquisition:

<sup>Ø</sup> firstly, share-for-share offers; and

<sup>Ø</sup> secondly, cash offers.

In the present case, 90% of the target company’s shares are held, so the bidder has to make a cash offer to all remaining shareholders at a price no less than the highest price paid in the preceding 12-month period.

<sup>w</sup> <sup>x</sup> 3 In terms of achieving economies of scale, the following objectives are important for the present acquisition:

<sup>Ø</sup> Two restaurant rationalisation.

<sup>Ø</sup> Combine some functions such as purchasing, support functions, and marketing.

None of these objectives outlined above are achieved simply by doing the deal; they must be implemented in order to be successful. Thus, these objectives can serve as basis for post-acquisition decisions.

<sup>w</sup> <sup>x</sup> 4 The acquisition implementation process for the present situation depends on many of the choices made during the pre-acquisition phase:

<sup>Ø</sup> What is the degree of integration chosen?

<sup>Ø</sup> What is to be the role of the target’s management in the post-acquisition restaurant?

<sup>Ø</sup> Will employees be merged?

Bearing in mind the uniqueness of the implementation process in light of these factors should be considered for the present acquisition plan.

<sup>w</sup> <sup>x</sup> 5 The target restaurant is well known for its food quality. If there is any organisational restructuring of the target, then it is recommended not to replace the chef of the target restaurant in the initial phase.

In order to show how the strategy modification works, let us consider that a minority shareholder is not ready to sell his share to the raider. The shareholder has applied for an order under Section 430c that he should not be under a duty to sell his shares to Ladenis brothers.

DSBAP can provide certain relevant information to its user here. This information consists of legislative information and the appropriate precedent s . Ž . Moreover, according to the facts, DSBAP presents a comprehensive predictive rule-based advice, which consists of the output of the rules ARULE05 and BRULE02. The respective outputs are shown by the following.

The present situation has triggered the availableaction s rule ARULE05. Its preconditions and possi-Ž . ble actions are as follows:

Preconditions of ARULE05

Ž . applicant is one of the shareholders

Ž . respondent is the raider

Ž . offer notice has been given to the applicant

Ž . applicant is not ready to sell the share to the raider

Ždate of application is within six weeks of the notice period.

AÕailable action s( )

The court may make one of the following orders:

<sup>w</sup> <sup>x</sup> 1 an order requiring that the raider shall not be entitled and bound to acquire the shares; or

<sup>w</sup> <sup>x</sup> 2 an order specifying terms of acquisition different from those of the offer.

All the preconditions of BRULE02 are matched as a consequence of the facts of the Ravenna Re-Ž staurants case. Due to this, DSBAP provides a. clear-prediction that is a possible outcome of this case. The preconditions, prediction and argumentation or justification for the prediction of BRULE02Ž . are shown in Fig. 10.

DSBAP can provide further information and justification for the above argumentation scheme. On demand, the system is able to provide the text of the particular section or subsection of the legislation Ž . e.g., Section 429 of the Companies Act 1985 . Furthermore, DSBAP can justify its previously decided case selection process and show how a case amplifies a predicted rule-based outcome. For example, the selection of a case Re Chez Nico Restaurants is justified to its user by displaying both the common and non-shared surface features of the new case with respect to that case. It also shows the legal implications of Re Chez Nico Restaurants in the light of the new case.

It is now helpful to discuss how a case has been selected in DSBAP for supporting the system argument scheme.

## 6.1. Case selection process

The represented cases are given unique identifications e.g., CASE01, CASE02 for use in the caseŽ .

base. All the cases are indexed. The INDEX is used for similarity assessment between cases. From the case base, two cases have been selected to show the similarity assessment between them. In order to illustrate by an example, we consider the legal problem of protection of minority shareholders in acquisition-related cases.

The represented cases are given unique identifications for use in the case base, a part of which is shown in Table 3. Let INDEX01, and INDEX02 be the two indexes for CASE01 and CASE02, respectively.

The indexes attribute of CASE01 refers to the main surface features. For example, in Re BUGLE PRESS i.e., CASE01 , the indexes INDEX01Ž . Ž . refers to the surface features ‘right of minority shareholders’, ‘business type is publishing and selling’, ‘applicant is one of the shareholders’, ‘respondent is the raider’, ‘offer relates to purchase of the share’, ‘offer relates to a particular class of shares’, ‘respondent contracted 90% of the share’.

Similarly, in Re PRESS CAPS i.e., CASE02 ,Ž . the indexes INDEX02 refers to the surface featuresŽ . ‘right of minority shareholders’, ‘business type is engineering company’, ‘applicant is one of the shareholders’, ‘respondent is the raider’, ‘offer relates to purchase of the share’, ‘offer relates to a particular class of shares’, ‘respondent contracted 97% of the share’.

The simplest of all association measures is CASE01<sup>l</sup>CASE02, which produces five shared main surface features. Taking into account the number of main surface features, the total number of matched features for CASE01 and CASE02, the similarity coefficient Ž . S of CASE01 and CASE02 is

Table 3  
Cases relating to a minority shareholders protection order

<table><tr><td>Case no.</td><td>Source</td></tr><tr><td>CASE01</td><td>Re BUGLE PRESS [1960] 1 All ER 768</td></tr><tr><td>CASE02</td><td>Re PRESS CAPS [1949] 1 All ER 1013</td></tr><tr><td>CASE03</td><td>Re HOARES [1933] All ER 105</td></tr><tr><td>CASE04</td><td>Re Chez Nico (Restaurants) [1992] BCLC 192</td></tr><tr><td>CASE05</td><td>Re GRIERSON, OLDHAM and ADAMS [1967] 1 All ER 192</td></tr></table>

calculated as below:

$$
S \langle \text { is\_similar } \rangle (\text { CASE01 }, \text { CASE02 }) = \frac {5}{7}
$$

Similarly,

$$
S \langle \text { is\_similar } \rangle (\text { CASE02 }, \text { CASE01 }) = \frac {5}{7}
$$

Therefore, the mutual similarity coefficient is:

S² : both way similarity CASE01, CASE02 <sub>– –</sub> Ž .

$$
= \frac {1}{2} [ 0. 7 1 + 0. 7 1 ] = 0. 7 1.
$$

Using the above similarity assessment method, DSBAP can calculate the similarity between the new case in hand and the stored cases in the case base. The cases that have the highest similarity rating with respect to a new case are retrieved, and used in the DSBAP argument scheme. Only, the cases with scores above 0.5 are selected for this purpose. We have determined this threshold value by experiment. A value of 0.5 or above indicates that the case has some significant ability to provide a contribution towards the generated argument.

## 7. Conclusions

In this paper, a DSS has been presented which uses both RBR and CBR for solving a particular type of business problem. It has been shown how a complex business situation can be represented using an object-oriented scheme. The performance of the system as judged by criteria such as completeness, Ž relevance, etc. applied by business specialist users is . generally good. However, our implementation is a prototype. The production of partial rule-based advice and the argument generation facilities reflect the intelligent ability of the implemented system to use the rule and case knowledge in ways that correspond to how humans use it.

We conclude our discussion by noting some of the limitations of the system described in this paper and proposing further efforts aimed at strengthening this approach. The company valuation methods, in the project, are very much theoretical in nature and therefore require further work. This future work should be conducted in three areas. Firstly, consultation with a real-world company valuation expert to build an appropriate model is needed which shouldŽ produce many more rules and even cases . Secondly, . there is a huge amount of data on company acquisition and valuation that are accessible for research. We intend to analyse these data to find out a pattern Ž . if there are any to form a model and possible application of CBR method to do this valuation. Thirdly, we are planning to do research work on company valuation based on machine learning e.g.,Ž Neural network to determine whether it can provide. any better valuation model for the present system.

Lastly, we have used different threshold values for case and rule selection process. These values are very appropriate for the present knowledge base. But the number of cases and rules in the knowledge base will increase in the future and, hence, these threshold values may change accordingly to reflect the retrieved information. All these issues will be the focus of our future research to enhance the performance of the implemented system.

## Acknowledgements

The authors would like to thank Professor John A. Campbell for providing useful suggestions on an early draft of this paper. The authors also thank the anonymous reviewers for their helpful comments.

## References

<sup>w</sup> <sup>x</sup> 1 K. Ashley, Modelling Legal Argument: Reasoning With Cases and Hypothetical, PhD thesis, Department of Computer and Information Science, University of Massachusetts, Amherst, USA, 1987.

<sup>w</sup> <sup>x</sup> 2 I. Benbasat, G. DeSanctis, R. Nault, Empirical research in managerial support systems: a review and assessment, in: C.W. Holsapple, B. Whinston Eds. , Recent DevelopmentsŽ . in Decision Support Systems, Springer-Verlag, 1993, pp. 383–437.

<sup>w</sup> <sup>x</sup> 3 R.W. Blanning, D.R. King, Decision support and

knowledge-based systems, Journal of Management Information Systems 6 3 1989 3–6.Ž . Ž .

4 L. Blau, P.P. Bonissone, S. Ayub, Planning with dynamic cases, in: Proceedings of Case-Based Reasoning Workshop, Morgan Kaufmann, San Mateo, CA, 1991, pp. 295–306.

<sup>w</sup> <sup>x</sup> 5 L. Branting, Integrating Rules and Precedents for Classification and Explanation: Automating Legal Analysis, PhD thesis, Department of Computer Science, University of Texas, Austin, USA, 1991.

<sup>w</sup> <sup>x</sup> 6 R. Brealey, S. Myers, Principles of Corporate Finance, Mc-Graw-Hill, London, 1996.

<sup>w</sup> <sup>x</sup> 7 A. Bonarini, V. Maniezzo, Integrating expert systems and decision-support systems: principles and practice, Knowledge-Based Systems 1991 172–176.Ž .

<sup>w</sup> <sup>x</sup> 8 P.P. Bonissone, J. Aragones, J. Stillman, PRIMO: a tool for reasoning with incomplete and uncertain information, in: Proceedings of the Third International Conference on Information Processing and Management of Uncertainty in Knowledge-Based System, IPMU 90 , France,1990, pp.Ž . 325–327.

<sup>w</sup> <sup>x</sup> 9 P.P. Bonissone, L. Blau, S. Ayub, Leveraging the integration of approximate reasoning systems, in: Proceedings of 1990 AAAI Spring Symposium in Case-Based Reasoning,1990, pp. 1–6.

<sup>w</sup> <sup>x</sup> 10 O. Curet, M. Jackson, Evaluting a case-based learning and reasoning applications: the top management fraud diagnostic tool TMFDT , in: H. Burkhard, M. Lenz Eds. , ProceedingŽ . Ž . of Fourth German Workshop on Case-Based Reasoning — System Development and Evaluation, Vol. Informatik — Bericht Nr. 55, 1996, pp. 10–18, Computer Science Department, Humboldt University.

<sup>w</sup> <sup>x</sup> 11 S. Dutta, P.P. Bonissone, Integrating case- and rule-based reasoning, International Journal of Approximate Reasoning 8 Ž .1993 163–203.

<sup>w</sup> <sup>x</sup> 12 P.N. Finlay, IT for competitive Advantage: the place of expert systems, Journal of Strategic Information Systems Ž .1992 126–133.

<sup>w</sup> <sup>x</sup> 13 A.D. Goldbert, J. Robson, SMALLTALK-80: the language and its implementation, Addision-Wesley, Reading, MA, 1983.

<sup>w</sup> <sup>x</sup> 14 R. Golding, P.S. Rosenbloom, Improving rule-based systems through case-based reasoning, in: Proceedings of the Ninth National Conference on Artificial Intelligence AAAI- Ž 91 ,1991, pp. 22–27. .

<sup>w</sup> <sup>x</sup> 15 M. Guida, P. Marchesi, G. Basaglia, Knowledge-based decision support systems for manufacturing decision-making, Information and Decision Technology 18 1992 347–361.Ž .

<sup>w</sup> <sup>x</sup> 16 W. Huang, G. Cross, Reasoning about Trademark infringement cases, in: Proceedings of DARPA Case-Based Reasoning Workshop, Florida,1989, pp. 270–274.

<sup>w</sup> <sup>x</sup> 17 R.N. James, DISXPERT: a rule-based vocational rehabilition risk assessment system, Expert Systems With Applications 12 4 1997 465–472.Ž . Ž .

<sup>w</sup> <sup>x</sup> 18 B. Kim, S. Lee, A bond Rating expert system for industrial companies, Expert Systems With Applications 9 1 1995Ž . Ž . 63–70.

<sup>w</sup> <sup>x</sup> 19 D. King, Intelligent decision Support: strategies for integrating decision support, database management, and expert system technologies, Expert Systems With Applications 1 1990Ž . 23–38.

<sup>w</sup> <sup>x</sup> 20 J. Kolodner, Case-based Reasoning, Morgan Kaufmann, San Mateo, CA, 1993.

<sup>w</sup> <sup>x</sup> 21 S. Lee, C. Wu, CLXPERT: a rule-based scheduling system, Expert Systems With Applications 2 2 1995 153–164.Ž . Ž .

<sup>w</sup> <sup>x</sup> 22 R. McIvor, K. Mulvenna, P. Humphreys, Hybrid knowledgebased system for strategic purchasing, Expert Systems With Applications 12 4 1997 497–512.Ž . Ž .

<sup>w</sup> <sup>x</sup> 23 H. Meyer, A. D.Tore, F. Siegel, F. Curley, The strategic use of expert systems for risk management in the insurance industry, Expert Systems With Applications 5 1992 15–24.Ž .

<sup>w</sup> <sup>x</sup> 24 R. Michaelsen, An expert system for federal tax planning, Expert Systems 1 2 1984 149–167.Ž . Ž .

<sup>w</sup> <sup>x</sup> 25 K. Pal, A. Campbell, A hybrid system for decision-making about assets in English divorce cases, in: Advances in Case Based Reasoning: First UK CBR Workshop, LNAI 1020 ,Ž . Springer-Verlag, 1995, pp. 152–165.

<sup>w</sup> <sup>x</sup> 26 K. Pal, J.A. Campbell, A hybrid Legal decision-support system using both rule-based and case based reasoning, Information and Communications Technology Law 5 1996Ž . 227–245.

<sup>w</sup> <sup>x</sup> 27 K. Pal, A. Campbell, An application of rule-based and case-based reasoning within a single legal knowledge-based system, The DATA BASE for Advances in Information Systems 28 1997 48–63.Ž .

<sup>w</sup> <sup>x</sup> 28 R. Pike, B. Neale, Corporate Finance and Investment: Decisions and Strategies, Prentice-Hall Europe, London, 1999.

<sup>w</sup> <sup>x</sup> 29 T. Quah, C. Tan, K.S. Raman, B. Srinivasan, Towards integrating rule-based expert systems and neural networks, Decision Support Systems 17 2 1996 99–118. Ž . Ž .

<sup>w</sup> <sup>x</sup> 30 L. Rabinowitz, Weinberg and Blank on Takeovers and Mergers, Sweet & Maxwell, London, 1997.

<sup>w</sup> <sup>x</sup> 31 L. Rissland, K. Ashley, HYPO: a precedent-based legal reasoner, in: G. Vandenberghe Ed. , Advanced Topics ofŽ . Law and Information Technology, Kluwer, 1989, pp. 213– 234.

<sup>w</sup> <sup>x</sup> 32 E.L. Rissland, D.B. Skalak, CABARET: rule interpretation in a hybrid architecture, International Journal Man–Machine Studies 34 1991 839–887.Ž .

<sup>w</sup> <sup>x</sup> 33 C. Ryan, Company Law, Butterworths, London, 1997.

<sup>w</sup> <sup>x</sup> 34 D. Schutzer, Business expert systems: the competitive edge, Expert Systems With Applications 1 1990 17–21.Ž .

<sup>w</sup> <sup>x</sup> 35 K. Shin, I. Han, Case-based reasoning supported by genetic algorithms for corporate bond rating, Expert Systems With Applications 16 2 1999 85–95.Ž . Ž .

<sup>w</sup> <sup>x</sup> 36 P.H.A. Sneath, R.R. Sokal, Numerical Taxonomy, Freeman, San Francisco, 1976.

<sup>w</sup> <sup>x</sup> 37 P. Steinbart, The Construction of a Rule-based Expert System as a Method for Studing Materiality Judgements, PhD thesis, Michigan State University, 1984.

<sup>w</sup> <sup>x</sup> 38 D. Thomas, What’s in an object, BYTE 1989 . Ž .

<sup>w</sup> <sup>x</sup> 39 S. Toulmin, The Uses of Argument, Cambridge Univ. Press, 1958.

<sup>w</sup> <sup>x</sup> 40 E. Turban, Decision Support and Expert Systems — Management Support Systems, Macmillan, 1990.

<sup>w</sup> <sup>x</sup> 41 W.M. Yegge, A Basic Guide for Valuing a Company, Wiley, 1996.

![](/api/attachments/49MN6YYJ/fulltext/images/f7f57563f3d774e80aae6c722fefb2f00e2a0df5f42d3a42618bbf22e93f21a6.jpg)  
Kamalendu Pal is a postgraduate student in the department of Business Management at Greenwich College. His research interests include knowledgebased systems, decision-support systems, computer integrated design, data mining, and management information system.

![](/api/attachments/49MN6YYJ/fulltext/images/6fa5b835703169c34890237b3597481d9b6ca0d93a6657ca5174f357e6937e75.jpg)  
Owen Palmer is a senior lecturer in the department of Business Management at Greenwich College. His research interests include marketing management, sales management, and decision-support systems.
