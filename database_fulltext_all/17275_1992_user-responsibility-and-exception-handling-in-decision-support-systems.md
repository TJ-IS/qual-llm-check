---
otero_id: 17275
otero_key: "K5X73HA7"
title: "User responsibility and exception handling in decision support systems"
authors: "Z. Chen"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90045-q"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# User responsibility and exception handling in decision support systems

Z. Chen \*

University of Nebraska at Omaha, Omaha, NE, USA

The role of user responsibility in decision support systems (DSS) has been omitted in recent studies of some important issues. One such important issue is exception handling. In this short note, the role of user responsibility in exception handling is examined. The importance of user responsibility is emphasized, a possible approach is outlined which supports user responsibility in exception handling through the consideration of mental models.

Keywords: User responsibility, Mental models, Exception handling

## 1. Introduction

User responsibility is a crucial issue in designing decision support systems. However, recent studies of other important issues in decision support systems are not always consistent with the principle of user responsibility. One such important issue is exception handling $[4]$ of decision support systems. The theme of this short note is to emphasize the close relationship between user responsibility and exception handling, an important issue which so far has been omitted in the related studies.

Exception handling has drawn much attention from various researchers. For example, defeasible logic [5] has been introduced to control expert system recommendations with defeasible logic, and a scheme has been developed to represent exceptions in expert database systems [6]. The term ‘defeasibility’ is used in the following sense [2]. Generalizations like “birds fly” and “Matches burn when they are struck” apply to usual, typical, or normal cases. Unusual, atypical, or abnormal cases are exceptions to the rule. Such kind of generalizations is defeated when information is available to indicate that people are dealing with an exception to the rule. Because they can be defeated, these generalizations are termed as defeasible rules.

However, the schemes developed so far for exception handling can only work at the data or domain knowledge level, rather than at the system or user level; in other words, although schemes have now been developed to consider exceptions in making decisions, these decisions themselves are not defeasible at the system or user level. To defeat a rule at domain knowledge level requires only domain related knowledge, which can be handled through the knowledge base and/or the data base of the system. To defeat a decision or incorporate exception to a decision at the system level, however, requires meta knowledge about the system itself, which is not stored in the knowledge base. Chances are that the user may reject part of a decision made by the system, using some reason not captured as the domain knowledge. If this is the case, then the decision should not be simply thrown away; rather, user feedback should be incorporated by the system to revise that decision. How to incorporate the user's responsibility into the study of exception handling or defeasible reasoning in decision support systems, is an important issue to be included into researchers' agenda.

![](/api/attachments/K5X73HA7/fulltext/images/1763784d4b6c2d7a5291bf0b4e98d3150e76171dcdd1728bc4cc57419f7de3f9.jpg)  
Zhengxin Chen is an assistant professor of Department of Mathematics and Computer Science, University of Nebraska at Omaha. He received Ph.D. degree in computer science from Louisiana State University in 1988. He has taught courses in advanced artificial intelligence and expert systems at graduate level. Among his current interests are various theoretical and pragmatical issues in building intelligent systems.

In the remaining part of this paper, the relationship between decision making and user responsibility will be first briefly examined. A suggestion then follows.

## 2. Decision making and user responsibility

The general relationship between decision making and user responsibility can be summarized as follows. According to Hollnagel [3], in decision making, responsibility can both refer to who can be held responsible in legal terms and who is responsible in terms of having knowledge of what the decision was about (the conditions, the alternatives, the consequences). As the decision support systems become more intelligent through the use of knowledge processing, the problem of responsibility in decision making becomes more important. The solution to this problem depends very much on how the intelligent decision decision support system is applied in the task. The general attitude is that an intelligent decision support system should be a tool rather than a prosthesis for the decision maker, i.e. it should assist him rather than replace him. If the intelligent decision support system is a prosthesis then, clearly, the responsibility has, in fact, been taken away from the decision maker, at least for that particular task. However, if the intelligent decision support system is introduced as a tool, the decision maker has the final responsibility for the decision.

The problem of responsibility, in a sense, is the problem of understanding correctly the information and knowledge that describe the situation. The decision maker has dual responsibility: He is responsible for the decision, but also for providing information to the system which can be understood by it. If the decision maker lets the intelligent decision support system make some of the decisions (and he often has no choice in the matter), he must be able to get an explanation from the intelligent decision support system that he can understand, in order to agree or disagree with the intelligent decision support system [3].

In summary, there are cases in which the decision maker is given the option of vetoing or asking for revising the recommendations of the intelligent decision support system. The user has the responsibility to handle the exceptions, thus contributing to the decision making. However, current studies of defeasible reasoning and exception handling do not take this into consideration. User responsibility is omitted (or ruled out) in the current schemes of exception handling, since these schemes are only concerned at the domain knowledge level.

## 3. Two types of exceptions

Furthermore, in terms of the user responsibility, two types of exceptions can be distinguished (as suggested by [7]). As a first category, the exception is to provide some previously unknown fact to the system, thus extending the domain of the system. This type of exception reflects a kind of learning, and should be incorporated into the decision support systems. The second category reflects truly exceptional conditions. The boundary of these two categories may not be always clear, but in either case, the user may contribute to the decision making.

An example will illustrate this situation [7]. Loan officers at a bank grant house loans based on certain criteria, such as ratio of debt to income. These criteria can be preprogrammed in the decision support system. Officers may supersede a decision based on these criteria by judging aspects not on the system such as stability, support by other family members, knowledge of the specific job market, and so on. Exceptions granted using these other criteria should eventually be incorporated into the system, as more complex model are built. This is a learning process. On the other hand, loans may be given to high-ranking officers, politicians, business partners, etc., regardless of the original criteria. These exceptions, based on possibly sound business reasons, do not however, reflect an intent to extend the original criteria.

## 4. User responsibility and mental models

The purpose of this note is to raise the problem rather than to propose a solution. Nevertheless, a possible approach can be sketched out as below, which provides user responsibility of exception handling by considering users' mental models.

In the context of human-computer interaction, the term mental model is most commonly used to refer to a representation (in the head) of a physical system or software being run on a computer [1]. Streitz [8] distinguished mental models from conceptual models. A mental model may be viewed as a 'subjective' knowledge representation about the domain, while a conceptual model is developed by designers to reflect about the system and the user in a systematic way. Streitz began with the notion of an abstract function, $f$ , as the functionality of the functional principle underlying an application program. Furthermore, Streitz used the following notations to indicate four kinds of primary models. $S(f)$ is used to denote system's realization or implementation of the basic functionality, and $U(f)$ is used to denote user's mental model. The designer's conceptual model is denoted as $D(f)$ , while the psychologist's conceptual model is denoted as $P(f)$ .

In addition, second order models can be built based on the primary models. First of all, $U(S(f))$ is the user's mental model of the system's realization of the function, f. The user develops a $U(D(f))$ , because he or she also makes inferences about the designer's conceptual model. Second-order models also include $D(U(f))$ and $P(U(f))$ , which reflect, respectively, the designer's and the psychologist's point of view about what user's mental models are like. The system builds up about the user's mental model, denoted as $S(U(f))$ .

Streitz's framework for representing human-computer interaction, as briefly summarized here, seems to be able to serve as the starting point of exception handling scheme with user responsibility incorporated. Let $f$ stand for the function defined above; but instead of being a fixed function, it is now re-defined as below to incorporate feedback [7]. Exceptions, denoted by $e$ , modify $f$ . To indicate this modification, the function $f$ will be denoted as $f_i$ , where the subscript $i$ indicates the version of the function; the initial function will thus be denoted as $f_1$ . The user responsibility for exception handling can then be perceived through the investigation of the model $U(f_i)$ , and the relationships between models such as $U(f_i)$ , $U(S(f_i))$ and $f_i$ .

In terms of the two types of exceptions as identified in the previous section, two different ways of handling exist. If an exception belongs to the first category, then some previously missing fact should be incorporated into the decision support system. Schemes are to be developed so that the user's consideration from the outside of the system can 'penetrate' into (or be reduced to) the innermost function $f_{i}$ , and the schemes developed for exception handling at the domain knowledge level can thus be extended to incorporate user feedback for future applications. Using notation introduced above, the function should be modified in the following manner

$$
f _ {i + 1} = f _ {i} + e,
$$

where the operation + denotes the integration of new knowledge (as indicated by e) into the function $f_{i}$ .

In case of exceptions that belong to the second category, however, the exception indicates a situation that the system was not designed to handle. It is necessary to keep track of those exceptions since they reflect functionality not originally intended. Using the notation introduced above, the following formula holds

$$
f _ {i + 1} = \left\{ \begin{array}{l l} f _ {i} & \text { if   no   exception }, \\ (f _ {i}, e) & \text { otherwise }, \end{array} \right.
$$

where the pair $(f_{i}, e)$ can be read as “ $f_{i}$ with special care of e.”

## 5. Concluding remark

The theme of this short note is that exception handling from the perspective of the user responsibility should be considered. Traditionally the issue of user responsibility and user modeling and the issue of exception handling have been investigated separately. Nothing is wrong in these studies. However, to make decision support systems able to handle real world problems, an integrated study which combines these two considerations is necessary.

## References

[1] J. Carroll and J.R. Olson, Mental models in human-computer interaction, Handbook of Human Computer Interaction, 50–51.

[2] M.A. Covington, D. Nute and A. Vellino, Prolog Programming in Depth (Scott, Foresman and Co., Glenview, IL, 1988).

[3] E. Hollnagel, Responsibility issues in intelligent decision support systems. In Berry, D. and Hart, A. (eds), Expert Systems: Human Issues, pp. 237–249.

[4] G.F. Luger, W.A. Stubblefield, Artificial Intelligence and the Design of Expert Systems (Benjamin–Cummings, Redwood City, CA, 1989).

[5] D. Nute, R.I. Mann and B.F. Brewer, Controlling expert system recommendations with defeasible logic. Decision Support Systems 6, pp. 152–164 (1990).

[6] R.G. Ramirez, R. Dattero and J. Choobineh, Representing generalizations and exceptions in expert database systems. Decision Support Systems 6, pp. 29–44 (1990).

[7] R.G. Ramirez, private communication (March 1991).

[8] R.A. Streitz, Mental models and metaphors: Implications for the design of adaptive usersystem interfaces. In H. Mandl and A. Lesgold (eds.), Learning Issues for Intelligent Tutoring Systems, 164–186.
