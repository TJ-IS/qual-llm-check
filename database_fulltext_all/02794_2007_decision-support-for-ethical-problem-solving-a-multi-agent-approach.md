---
otero_id: 2794
otero_key: "QXEWCJYC"
title: "Decision support for ethical problem solving: A multi-agent approach"
authors: "Russell W. Robbins; William A. Wallace"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.03.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support for ethical problem solving: A multi-agent approach

Russell W. Robbins <sup>a,⁎</sup>, William A. Wallace

<sup>a</sup> Computer Science and Mathematics, Marist College, 3399 North Road, Poughkeepsie, NY 12601, United States <sup>b</sup> Decision Sciences and Engineering Systems, Rensselaer Polytechnic Institute, United States

Available online 25 April 2006

## Abstract

This paper suggests that a multi-agent based decision aid can help individuals and groups consider ethical perspectives in the performance of their tasks. Normative and descriptive theories of ethical problem solving are reviewed. Normative theories are postulated as criteria used with practical reasoning during the problem solving process. Four decision aid roles are proposed: advisor, group facilitator, interaction coach, and forecaster. The research describes how the Theory of Planned Behavior from psychology can inform agent processing. The Belief–Desire–Intention model from artificial intelligence is discussed as a method to support user interaction, simulate problem solving, and predict future outcomes. © 2006 Elsevier B.V. All rights reserved.

Keywords: Ethical problem solving; Decision support; Multi-agent systems

## 1. Introduction

Ethics is the study of values, rules, and justifications ([69], p. 1). More specifically, ethics is “that branch of philosophy dealing with values relating to human conduct, with respect to the rightness and wrongness of certain actions and to the goodness and badness of the motives and results of such actions” ([54], p. 665). In other words, ethics is the study of what the appropriate actions are for an individual or a group in a moral dilemma. Considerations can be right versus wrong action (i.e., means) [35], good versus bad results (i.e., ends) [7], virtuous versus vicious character (leading to right action or good results) [4], fairness [56], and others [24,25,53,60,77].

Polya saw problem solving as understanding the problem, devising a plan, carrying out the plan, and evaluating the solution obtained by carrying out the plan [50]. Brim et al. saw problem solving as identifying the problem, describing the problem, diagnosing its causes, generating solutions, evaluating solutions, choosing a solution, and implementing and revising the selected solution ([11] in [40], p. 49). Pounds describes problem solving as choosing a model, comparing it to reality, identifying differences, selecting a difference, considering operators, evaluating consequences of operators, selecting an operator, and executing an operator ([51], in [40], p. 49).

Problems can be solved synthetically, analytically, or via a combination of synthetic and analytic techniques [73]. Decision-making is one component stage in the process ([41] in [75],[52]). Finally, problem solving can also be seen as “transforming a given situation into a desired situation or goal” ([30], in [64], p. 674). The

Four Component Model ([57], p. 3), a problem solving model focused exclusively upon morality, suggests four psychological processes that must occur prior to moral behavior: 1) interpret situation and create alternative actions, 2) choose alternative based upon some form of consideration, 3) prioritize this morally value laden choice above amoral values and associated choices, and 4) intend to perform action.

Integrating these definitions of “ethics” and “problem solving”, and the Four Component Model: ethical problem solving is the iterative process of interpreting one's environment by identifying a moral problem based upon what one values morally, framing and reframing the problem or sub-problems from various morally value laden perspectives in a synthetic or analytic fashion, applying knowledge to develop and consider alternatives, choosing an alternative or alternatives, intending to act morally, and then acting towards achieving those alternative(s). Sample ethical problem scenarios are boards or committees considering employment practices in production facilities located in third-world countries that may need to balance mores of their home country versus the needs of the families and children it hires or physician teams that must advise families regarding end-of-life care.

This paper suggests that a multi-agent based decision aid can complement approaches like ethics sensitivity training, codes of ethics, and regulation and legislation, and help individuals and groups in organizations consider alternative ethical perspectives in the performance of their tasks [79]. While people can and do act as decision aids to other humans, it is not feasible to train and employ humans as ethical advisors for each and every employee. It may be feasible to have “on call” ethics consultants serving large populations, much as technical help desks do today. Another, more aggressive solution is a population of decision support systems that aid individuals facing ethical problems, one-on-one, in whatever context those individuals find themselves. Some decision support systems and computational models for ethics have already been built [27,47,58]. While “on call” ethics consultants are only available at the reach of the phone, perhaps during restricted hours, computer-based “ethical assistants”, embedded within modern hardware, can accompany an employee wherever and whenever they carry out their tasks.

The remainder of this paper is organized as follows. Section 2.1 of this paper provides an introduction to traditional means of moral reasoning by discussing broad categories (character, duty, consequence, justice, etc.) for considering an ethical problem, and provides examples of the items within the categories. Section 2.2 discusses two foundational descriptive theories of ethical problem solving and describes pertinent research in values. Section 3 presents theories of psychology and artificial intelligence that can support a decision aid. Section 3.1 introduces the Theory of Planned Behavior from psychology [1]. This theory is used as the basis for our representation of antecedents to thinking and communication, in ethical problem solving. Section 3.2 discusses the Belief–Desire–Intention (BDI) model of practical reasoning and the last section introduces the postulated effect of personalities on ethical problem solving in groups [10,55,17,68,80,22,37,38,71].

Section 4 presents a framework of supporting roles that could be provided by ethical decision aids. Section 4.1 presents a summary of an ethical problem [13,62], used as an illustrative example throughout the remainder of the section. In Sections 4.2–4.5, four distinct roles for ethical problem solving support are described. In the first role, the decision aid's role is as an advisor. The advisor compares and contrasts a user's decisions (or heuristics used to arrive at those decisions) to alternatives suggested by normative ethics but not considered and suggests other solutions. In the second role, the decision aid acts as a group facilitator. A third role is as an interaction coach. The interaction coach helps individual group members understand the possible reactions of others to that individual's ideas, prior to that individual communicating to group members. While the group facilitator supports the group's process, the interaction coach helps an individual group member be more influential. A fourth role of the ethical problem solving decision aid is as a forecaster of future events or states. This forecaster helps users understand potential consequences of particular solutions to a problem, or the likelihood of an ethical issue surfacing, by “fastforwarding” to potential future worlds. Section 5 summarizes and concludes the paper by showing the relationships among the theories discussed in the paper and indicating future areas of research.

## 2. Ethical theories

In order to develop a decision support system for ethical problem solving, an understanding of both normative and descriptive theories of ethical behavior is necessary. This section reviews those found to be most relevant to this research.

## 2.1. Normative theories

Three categories of normative ethical problem solving techniques “stand out ([34], p. 1)”: characterbased, duties-based, and consequences-based. While these theories are normative, their rationales for determining moral essence are often what we refer to when we solve ethical problems. In this research, normative theories are postulated as criteria that are used with practical reasoning during the problem solving process [7,24,56,31,76,64]. We will refer to the prescriptive theories espoused by moral philosophers as “normative theories of ethical problem solving” or “normative theories” and to techniques used in practice as “moral reasoning heuristics” or “heuristics”. Selected theories (and their categories) are shown in Table 1.

Virtue (or character-based) theories [67] suggest that the right or good answer is the answer that is congruent with a person's own moral virtues. For example, Aristotelian moral virtues (Table 1, Item A) are those characteristics that enable a person to be the best they can be as they work towards fulfilling their distinctive purpose in life. To Aristotle, the distinctive purpose of human life was the pursuit of reason [4] and the ethical solution is the one that is reached by a person using the capability that is uniquely human, that is, the ability to reason. For virtue theories in general, the problem solver applies their unique “virtuous” characteristics when solving the problem, and because this occurs, the problem is solved ethically.

A second form of reasoning is deontological (or dutybased) ethics (Table 1, Items B through E). Deontological ethics [15] prescribes the ethical solution to be the one that contains acts that have intrinsic moral worth, and does not contain acts with no intrinsic moral worth. Certain acts are, at their very core, right or wrong. What can and cannot be done exists as rules. The rules essentially define duties one person has to another, often to protect each person's inherent rights. A theorist in this school of thought is Immanuel Kant [35], who suggested that all of deontological ethics can be condensed to one rule, the Categorical Imperative. One form of Kant's Categorical Imperative is “Act only on that maxim which you can at that time will to be universal law” ([3], in [32], p. 436, about [35]). In other words, if you are acting in accordance with a rule, that particular rule is only morally permissible if you could wish that everyone else should act in accordance with that same rule.

Consequentialist approaches (Table 1, Items F and G) a third type of normative theories, do not focus on the character of the problem solver, or to the moral worth of acts within the ethical problem, but instead focus on the potential positive or negative consequences that may happen under alternative scenarios [28]. Acts are judged right or wrong based on their possible consequences. For example, Utilitarianism suggests the ethical solution to be the solution that provides the most good for the most number of people [7]. Additional types of normative theories that do not fit into the categories that “stand out” are those focused on 1) justice based upon rights, 2) caring and responsibility for others, and 3) belief in the application of theory that is most appropriate for the context (Table 1, Items H, I, and J, respectively) [25,56,77].

Normative theories of ethics, which are often used as heuristics in everyday ethical problem solving

<table><tr><td>Item</td><td>Category</td><td>Moral reasoning heuristic</td><td>Maxim(s)</td></tr><tr><td>A</td><td>Virtue</td><td>Aristotelian Virtue Theory [4]</td><td>One should apply and develop their characteristics towards their distinctive purpose; this will naturally lead to the best actions and best results. To Aristotle, a person&#x27;s distinctive purpose was to reason.</td></tr><tr><td>B</td><td>Duty</td><td>Categorical imperative [35]</td><td>Act towards others as you would have them act towards you -or- Treat people as ends, not means.</td></tr><tr><td>C</td><td>Duty</td><td>Religious Rule-based (form of deontology)</td><td>Ten Commandments; The Eight-Fold Path; etc.</td></tr><tr><td>D</td><td>Duty</td><td>Obligation-based [60]</td><td>1) Act according to our agreements, 2) Reciprocate help, 3) Be just (reward for merit, etc.), 4) Help those in need, 5) Perfect yourself, and 6) Do no harm.</td></tr><tr><td>E</td><td>Duty</td><td>Secular rule-based [24]</td><td>1) Don&#x27;t kill, 2) Don&#x27;t cause pain, 3) Don&#x27;t disable, 4) Don&#x27;t deprive people of freedom, 5) Don&#x27;t deprive people of pleasure, 6) Don&#x27;t deceive, 7) Keep your promises, 8) Don&#x27;t cheat, 9) Obey the law, and 10) Do your duty.</td></tr><tr><td>F</td><td>Consequence</td><td>Utilitarianism [7]</td><td>Act to reach the highest net ratio of good to bad results for the most number of people.</td></tr><tr><td>G</td><td>Consequence</td><td>Egoism [53]</td><td>Act to reach the greatest outcome possible for one&#x27;s self, irrespective to others.</td></tr><tr><td>H</td><td>Rights</td><td>Justice-based [56]</td><td>Seek fairness for all involved. Create a solution that has a balanced distribution of positives and negatives to parties involved.</td></tr><tr><td>I</td><td>Other</td><td>Ethic of Care and Responsibility [25]</td><td>Consider your feelings of interconnectedness with others. Think about the situation that each of these others and you are in. Use your experience; Nurture; Be responsible.</td></tr><tr><td>J</td><td>Other</td><td>Pluralism [77]</td><td>There is no one approach that is best. Using context to choose, and to use many techniques is appropriate.</td></tr></table>

It is important to consider these normative theories because they can be used as practical moral reasoning heuristics—as criteria to be used within everyday ethical problem solving. An individual that is concerned about duty will identify the problem differently than the person who is focused upon consequences. A person who is attempting to care for and be responsible for others may create a different set of alternatives than a person who believes that each person should look out for their own interests. And finally, the choices made by someone who is attempting to build character will be different than someone interested in minimizing bad and maximizing good outcomes.

## 2.2. Descriptive theories

Two descriptive theories that are important to include in any integrative model of ethical problem solving are the Theory of Moral Development and A Taxonomy of Ethical Ideologies [20,36]. Theories of personal values are also important and are also discussed in this section [59,63].

The Theory of Moral Development [36] postulates that individuals can move sequentially through six stages of development, beginning with a person following rules in order to avoid punishment and ending with a stage where individuals act in accordance with self chosen principles. Most adults stop at about stage 5, where individuals act so as to fulfill duties and obligations to which they have agreed. “These individuals aim to uphold laws except in extreme cases where they conflict with fixed social duties…” ([36], p. 67). The Theory of Moral Development does have critics. For example, Gilligan indicates that a bias exists (especially at the highest stages) within the Theory of Moral Development (because of its justice orientation) in favor of individuals that often hold a justice-oriented view (typically men) [25]. The integrated model of ethical problem solving presented in this paper uses the Theory of Moral Development modified to address Gilligan's concerns.

While people may be at a particular developmental level when solving an ethical problem, they also use particular “ethical perspectives” (i.e., ideologies), which can be considered lenses through which ethical problems are seen [20]. Ethical ideologies are postulated to vary by individual and described by their location with respect to two dimensions: relativistic/universalistic and idealistic/pragmatic. Davis and colleagues [16] find idealism and relativism to account for differences in ethical judgments in business practices and reports that “differences in relativism and idealism influence the individual's emphasis on various moral criteria when making ethical judgments. For example, individuals high in idealism display a predilection for invoking rules about justice and fairness.” ([16], p. 48).

However, to understand and simulate a particular person's ethical problem solving process, one needs to know more than his or her ethical ideology and his or her moral development level. One needs to understand what he or she values. The concept of a value is defined by Rokeach below:

“To say that a person has a value is to say that he has an enduring prescriptive or proscriptive belief that a particular mode of behavior or end-state of existence is preferred to an opposite mode of behavior or end state. This belief transcends attitudes toward objects and toward situations, it is a standard that guides and determines action, attitudes towards objects and situations, ideology, presentation of self to others, evaluations, judgments, justifications, comparisons of self to others, and attempts to influence others. Values serve as adjustive, ego-defensive, knowledge, and self-actualizing functions. Instrumental and terminal values are related yet are separately organized into relatively enduring hierarchical organizations along a continuum of importance ([59], p. 20, cited in [18]).”

A Model of Decision-Making Incorporating Ethical Values [21] is the first to explicitly consider personal values as underlying “antecedents of [ethical] behavior”. Glover et al. finds high levels of need for achievement (a value) correlated with higher levels of ethical behavior in two of four scenarios [26]. Singhapakdi and Vitell report marketers' ethical judgments can partially be explained by personal values [66]. Lin and Ding finds that personal values affect ethical attitude, which in turn affects behavioral intention [39]. Connor and Becker show that 12 of 14 Rokeach value clusters are significantly related to particular decision making styles [14].

Schwartz [63] developed and tested a typology of values “distinguished by the different motivational goals that the individual values express” ([18], p. 57). Most of Rokeach's [59] values are within the Schwartz typology. Schwartz's typology is used in this research because it is broad in terms of motivational goals, small in number of value sets that are mutually exclusive, and based on Rokeach's intensive work. These value sets are shown in Table 2.

The fact that the value sets are mutually exclusive supports the embedding of relationships between particular value sets and specific procedures within a software-based simulation model. For example, these values can be used to derive intentions used to drive reasoning or behavior within an agent. This agent would be internal to the decision support system and could simulate a person solving a problem.

## 3. Non-ethics-oriented supportive theories

## 3.1. The Theory of Planned Behavior

We have described the resolution of an ethical dilemma as a problem solving process that is performed by a person who has a particular moral development level, a particular perspective (ethical ideology), particular values, and uses particular heuristic(s). However, beliefs that are used when a person solves a problem have not been discussed in detail. That is the purpose of this section.

Value sets (based on motivational goals) and corresponding values

<table><tr><td>Value set</td><td>Values</td></tr><tr><td>Power:</td><td>Social status and prestige, control and dominance over people and resources (social power, authority, wealth, preserving my public image)</td></tr><tr><td>Achievement:</td><td>Personal success through demonstrating competence according to social standards. (successful, capable, ambitious, influential, intelligent, self-respect)</td></tr><tr><td>Hedonism:</td><td>Pleasure and sensuous gratification. (pleasure, enjoying life)</td></tr><tr><td>Stimulation:</td><td>Excitement, novelty, and challenge in life. (daring, a varied life, an exciting life)</td></tr><tr><td>Self-direction:</td><td>Independent thought and action-choosing, creating, exploring. (creativity, freedom, independent, curious, choosing own goals, self-respect)</td></tr><tr><td>Universalism:</td><td>Understanding, appreciation, tolerance and protection for the welfare of all people and for nature. (broad-minded, wisdom, social justice, equality, a world at peace, a world of beauty, unity with nature, protecting the environment)</td></tr><tr><td>Benevolence:</td><td>Preservation and enhancement of the welfare of people with whom one is in frequent contact. (helpful, honest, forgiving, loyal, responsible, true friendship, mature love)</td></tr><tr><td>Tradition:</td><td>Respect, commitment and acceptance of the customs and ideas that traditional culture or religion provide the self. (humble, accepting my portion in life, devout, respect for tradition, moderate)</td></tr><tr><td>Conformity:</td><td>Restraint of actions, inclinations and impulses likely to upset or harm others and violate social norms. (politeness, obedient, self-discipline, honoring parents and elders)</td></tr><tr><td>Security:</td><td>Safety, harmony and stability of society, of relationships, and of self. (family security, national security, social order, clean, reciprocation of favors, sense of belonging, healthy)</td></tr></table>

Source: [63], derived in part from [59].

The Theory of Planned Behavior (Fig. 1(a)) postulates that behavior can be predicted by one's intention (combined with one's actual control over the behavior) [1]. Intention in turn has the following antecedents: Attitude toward the behavior, Subjective Norm, and Perceived Behavioral Control (Fig. 1(a)). A person's attitude toward a behavior can be predicted by the summation of the multiplicative relationship of the strengths of one's beliefs about the outcomes of a behavior and the associated positive or negative value associated with each of the outcomes. A person's subjective norm can be predicted by the summation of the similar relationship between the strengths of one's normative belief about the likelihood that important referent individuals or groups approve or disapprove of performing a given behavior and one's motivations to comply with referents. And finally, one's perceived behavioral control can be predicted by the summation of one's control beliefs (about the presence or absence of requisite resources and opportunities) and one's perceived powers to perform behaviors. The Theory of Reasoned Action was a precursor to the Theory of Planned Behavior [1] and did not include the Perceived Behavioral Control antecedent to Intention.

Loch and Conger used the Theory of Reasoned Action to study ethical decision making in the context of computer use [42]. Their model suggests a person's intentions are affected by ethical attitudes towards a behavior and social norms, and the relative importance of each, in the context of an ethical dilemma [42]. The research reported that both attitudes and social norms play an important role in determining an individual's intentions to perform computing acts related to privacy and ownership, where intentions are the result of the attitude toward the behavior, subjective norm(s) regarding the behavior, and the relative importance of each as a moderator [42]. Chang states “the Theory of Planned Behavior [1] can be used quite successfully to predict the intention to perform unethical behavior” ([12], p. 1833) and that “the Theory of Planned Behavior predicted unethical behavior better than the Theory of Reasoned Action...” ([12], p. 1831). Peace et al. tested a model developed from the Theory of Planned Behavior [49]. Their results suggested individual attitudes, subjective norms and perceived behavioral control are all significant pre-cursors to intending to illegally copy software. Leonard et al. finds that IT behavioral intention is influenced by attitude, personal normative beliefs, gender, moral judgment capability and ego strength, which refers the amount of control one has to refuse impulses and follow their convictions [38]. While the Theory of Planned Behavior helps us understand what types of beliefs are used during the development of intentions that can become behavior, it does so in a static fashion. The Theory describes what beliefs are used and the results of processing those beliefs (i.e., behavioral, normative, and control beliefs). Its weakness is that it does not describe the ethical problem solving process. In order to simulate the process of solving an ethical problem we need another model.

![](/api/attachments/QXEWCJYC/fulltext/images/4559f151aa7ed0c670cd59d2d11e1e7c5b7c8d4ebe9fd0f614724ec9725ed2fc.jpg)  
Fig. 1. (a)Theory of Planned Behavior [1]. (b) Belief–Desire–Intention Model [10,55,17].

## 3.2. The Belief–Desire–Intention model

The purpose of using a Belief–Desire–Intention (BDI) model [10,55,17] (Fig. 1(b)) is to simulate practical reasoning, which is “argument, intelligence, [or] insight directed to a practical and especially a moral outcome” ([31], in [32], p. 709). Alternatively, practical reasoning is “concerned not with matters of fact and their explanation, but with matters of value, and what is to be done” ([76], p. 11939). “In practical reasoning, agents attempt to assess and weigh their reasons for action…” ([76], p. 11939). Actions can be either mental states or behaviors ([76], p. 11939).

A software implementation of the dynamic Belief– Desire–Intention (BDI) model can be used to simulate the process that is implicitly suggested by the static Theory of Planned Behavior (TPB) [1]. See Fig. 1(a) and (b). In the context of the BDI model, practical reasoning can be simulated by having software agents choose “cognitions” and “behaviors” in response to a “thought or a sensory perception”, based upon its “desires” and “beliefs” about the world and its “abilities”. In our research, “beliefs” are descriptive or procedural data a software agent (that simulates a person) believes are true or valuable, respectively. “Desires” are goals that an agent is interested in. The desires may be long-term, as in the case of values, or may be short term, as in the case of a software agent desiring acknowledgement from another agent or during a discussion. “Plans” are ways for a software agent simulating a person to solve a particular problem. “Events” are outputs of [any agent's] plans that trigger more processing on another plan, based on updated values of beliefs and desires, and a choice of that plan. Plans that are chosen to be executed are considered “intentions”.

Values (instrumental or terminal goals) are referred to as motives in TPB and desires in BDI. The TPB includes motives as precursors to behavioral, normative and control beliefs. Motives are “the goal or object of a person's actions” ([54], p. 1254) and (referring to our previous discussion of values) when values are used to direct thought or behavior, the two are synonymous. Static TPB Motives (values in the case of ethical problem solving) can be implemented as Desires in a dynamic BDI model. Behavioral, normative, and control beliefs (from TPB) can be embedded [as Beliefs] within a BDI model. Practical reasoning procedures that process behavioral, normative, and control beliefs to yield attitudes towards a behavior, social norms and perceived behavioral control can be implemented as Plans. Intention is theorized to lead to actual behavior in TPB, however, in BDI, an “Intention” is a chosen plan that results in an event, which represents an instance of an internal thought or external behavior. Moral development level, ethical perspective (ideology), and personality traits are theories not within BDI or TPB that support simulating (and hence, supporting) ethical problem solving, and can be represented with additional [object-oriented programming language] classes. These additional classes complete the dynamic model by affecting the choice of BDI Plans during the execution cycle.

## 3.3. Groups and personality traits

While there is an extensive literature addressing how individuals solve ethical problems, research regarding how groups solve ethical problems has focused on how groups decide among alternatives, specifically in the case of juries [29]. Studies of jury decisions have focused on either the criminal guilty/not guilty verdict decision or the civil award determination decision (choice of amount of money). Unfortunately, this work does not describe how groups transform a problem into a solution but instead focuses on determining guilt (a decision between yes and no) of parties presumably acting unethically or indemnifying parties (e.g., choosing a currency amount on a spectrum) that have [possibly] received a negative effect of a mishandled problem. The focus of our research is how groups (and individuals) solve ethical problems.

One approach to looking at groups is “a functionalist strategy for personality and social behavior [68,80].” This theory purports that behavior in groups is equally dependent upon characteristics of the situation as the characteristics of individuals within the group. As part of the discussion of the theory, values and personality traits are identified. Relationships between individual characteristics (primarily personality) and intra-group behavior have been described [6,8,9,68]. Individuals in groups can identify personality characteristics of others, such as outgoing (extroverted), shy (introverted), and intelligent (intellect) [2].

Many personality trait researchers have accepted the Five-Factor Model [22] which suggests individuals have five dimensions that endure over time and situation: extroversion, agreeableness, conscientiousness, neuroticism, and openness [46,22]. Extraversion can be described as tendencies towards sociability, assertiveness, high activity level, positive emotions, and impulsivity [44]. Agreeableness is the degree to which a person is willing to consent to another's wishes [54]. Conscientiousness is the degree to which a person is controlled by their inner sense of what is right and wrong [54]. Neuroticism can be described as the amount to which a person sees his surroundings as stressful, threatening, problematic; Neurotic individuals experience negative emotions more frequently than those who are not [78]. Openness is the degree to which one is accessible to appeals, ideas or offers [54]. Some readers may point to situational factors as important in ethical problem solving. Indeed this is the case. In defense of personality characteristics as foci for ethical problem solving, as opposed to situational constructs, they are as effective, and in some cases, more effective [6]. Personality and characteristics of the situation are not the only factors that affect group process. For example, individuals with status (as determined by characteristics of the perceived and attributed by the perceiver) have more opportunity to influence and are allowed more variation in their actions than those with lower status [74].

## 4. Decision aid roles

As mentioned, the proposed decision aid can support a user four ways: advisor, group facilitator, interaction coach, and forecaster. In a computer-based aid, these four roles would be agent-based and goal and event driven, and therefore will interact on their own volition with the user. The next section (4.1) introduces and summarizes an illustrative problem whose resolution could be supported by the prospective decision aid. Sections 4.2–4.5 describe (through the illustrative problem) the ways the proposed computer based decision aid could provide support.

## 4.1. An ethical problem

The case that will be used to describe how the roles in the decision aid will work is British Columbia's Pharmanet Project [13,62].

“This case is centered on the issue of what information technology can do versus what it should do in a larger, societal view. Secondary to that is the issue of information system implementation to strike the best balance between these two forces. The information system in question, Pharmanet, a publicly funded system with clearly stated goals for meeting private consumer needs. [These goals included reduced adverse drug interactions, tailored information for consumers, and streamlined billing procedures.—authors' insertion] The case's primary decision maker, Paul Tier, must struggle with three overriding sensitive public issues: personal health, government oversight, and personal data privacy.” ([62], p. 1)

Paul Tier, the project manager in charge of implementing the system which would “…give pharmacists full access to the prescription histories of all British Columbians,” ([13], p. 1) was faced with what decisions he needed to make in order to appropriately deal with the concerns. The Ministry of Health was primarily interested in reducing the number of adverse drug reactions, which in 1992, occurred in close to 10,000 individuals, but was also interested in reducing fraud (e.g., individuals getting prescriptions from multiple physicians and pharmacies) and streamlining billing processes. Pharmacists were worried about costs and risks of converting, spending more time filling prescriptions, and (with physicians) were concerned their regulatory bodies would use Pharmanet to monitor their professional practices. A third group of individuals were also interested in understanding, and providing solutions for, potential ramifications of a pharmacy wide database. The main concern they had was for personal information privacy. Privacy has been identified as one of the four ethical issues of the information age [45].

Questions posed by the Information and Privacy Commissioner, the B.C. Civil Liberties Association, and the B.C. Freedom of Information and Privacy Association were about 1) unauthorized “surfing” of the database, 2) additional uses of the database that had not been considered, planned for, or regulated, and 3) the fact that consumers and pharmacies could not “opt” out of participating in the program.

## 4.2. Advisor

As mentioned earlier, the Advisor role will support reasoning by “listening” to its user, comparing heuristics and decisions of the user to alternatives suggested by normative ethics, and suggesting additional heuristics to the user. (Using current technologies, “listening” could occur when the decision aid user types their thoughts into a screen's text field. Using future technologies, perhaps the advisor could actually listen.) Instead of the Advisor giving answers, it will ask questions, whenever possible. When questioned, it will be able to explain why a particular moral reasoning approach results in a particular solution. The decision aid will store information about the user that it supports, such as his or her moral development level, perspective, values and preferred moral reasoning heuristics in order to be more effective in its communication with the user. By having this functionality, the decision aid is less cumbersome to use and more realistic for its user to interact with. In essence, the decision aid will “know” some qualities (e.g., values valued or perspectives held) of the decision aid user, so therefore it can interact better, much as people interact better with those they know than those they do not know.

The Advisor's behavior is enabled via the dynamic BDI model. Problem solving heuristics can be stored as BDI Beliefs and these beliefs can be considered and expressed to the user by the implementation of a BDI Plan. For the near future this expression would be via words written to screen. The aforementioned BDI Plan is triggered by BDI Events that occur (such as a user saying a particular phrase) as well as BDI Desires (e.g., goals) that the BDI agent has. (An example desire that the BDI agent may have is the desire to inform its user whenever possible and appropriate.) As the user responds to the Advisor, these responses are handled as BDI Events, and the decision aid will again cycle through its BDI model to select an appropriate response (i.e., behavior), which can be implemented via a BDI Plan. An ontology will be used to determine meaning from sentences expressed by the user [70]. (An ontology is a data structure which has words (that describe a concept) as data, and which shows relationships between the meanings of words.)

An example of the use of the Advisor role follows. This example is based upon the illustrative problem described in Section 4.1. Paul Tier, the primary decision maker in the case may use a hybrid moral reasoning approach during his day-to-day problem solving. His hybrid approach integrates his belief that he needs to consider what the effects of his decision are (i.e., consequentialism, see Items F and G in Table 1) and his belief that he needs to follow certain basic rules (for example, see Items C and E in Table 1) as well. If this were the case, he may decide that he had done all that was necessary in terms of his set of rules, since he had not killed anyone, caused pain to anyone, etc. In fact, in terms of Paul's use of his consequence-oriented heuristics, the Pharmanet system could be seen to save lives. Since adverse drug interactions would no doubt be reduced, it may be reasonable (to him) to assume that some lives are lost from adverse drug reactions in a population of 10,000 incidents, and that reducing interactions could very well lead to saved lives. Also in terms of consequences, there may be no question in his mind that the Pharmanet system in the end would provide many more benefits (e.g., reduced adverse drug reactions and easier, faster payment of expenses for economically disadvantaged pharmacy patrons). He does believe though, in this example, that “the government” or “the legislature” has an obligation to handle concerns regarding creating penalties and agencies to enforce penalties for inappropriate use of the Pharmanet database.

The sample session shown in Fig. 2 could be entered via keyboard or spoken by Paul and written to the screen (or spoken) by the decision aid acting as an advisor. The dialog in Fig. 2 is referred to in the material to follow.

During the following explanation of the dialog between Paul and the advisor role of the decision aid (Fig. 2), references will be made to blocks of dialog that are encapsulated between English capital letters (and a hyphen). For example, at the top of Fig. 2, there is a block of dialog, encapsulated between “A-“ and “-A” that begins with “Paul: So I think the answer…”.

Beginning with section A, as the decision aid “listens” to Paul, it notes that the words “owe” and “liberal” have parents within its ontology. For more information on the concept of an ontology, see [70] (pp. 492–512). Based on the ontology, the decision aid determines that “owe” is-a-child-of “oblige”, “supposed” is-a-child-of “oblige” and that “liberal” is-achild-of “person”. While processing the second sentence spoken by Paul, the decision aid parses the sentence, using the ontology, and transforms it into the following form (subject–verb–object–preposition). The result is “not(I,owe,anything,group).” It then works through the following algorithm:

Rule 1: If any [of my] rules has an “or” in the Then portion of the rule, then clarify (call a function to determine) which type of user the current user is.

Rule 2: If verb has parent which is “oblige”, Then the user type is obligatory or user type is secular rule based or user type is both.

Based on the application of these rules (and others not shown for brevity), the decision aid then asks Paul “It seems as if you are highly focused upon rules or duties, Paul?” and confirms this in the dialog encapsulated with “B”. The choice of “rules” from the set (rules, obligations) is made randomly using a function or a class such as Random in Java. If rules are chosen, then the decision aid might clarify between religiously based rules and secular rules. (In this example, this dialog has been omitted to save space). Continuing to the dialog section contained between the “C”s, upon hearing this, the decision aid recognizes the question as rhetorical, and therefore does not respond. The decision aid also updates the BDI Beliefs of the instance of Paul it has in memory with “rules are an appropriate way to solve ethical problems.” The sequence of procedures used and the resulting beliefs follow:

Pseudocode: NoteUserMoralReasoning (“rulebased”);

Pseudocode: NoteUserMoralReasoning (“consequence-based”);

Pseudocomment: New Belief records for Paul Tier BDI Model follow:

Pseudodata: valid (moral\_reasoning\_approach, rulebased);

Pseudodata: valid (moral\_reasoning\_approach, consequence-based);

Subtype heuristics for rules and consequences would exist and be determined by the advisor via further querying of Paul. For the moment the decision aid now approaches the problem with Paul from a obligationoriented moral reasoning perspective (which Paul has not confirmed, but which the decision aid has inferred by Paul's words) since the decision aid has counted 2 words (see discussion in section A above) that link to oblige in its ontology. It will come back to consequenceoriented reasoning later.

Moving on to section D, the decision aid now attempts to determine the person who owes a duty to the liberal (who it knows is a person because of its ontology). It does this because, in obligation-oriented approaches to solving ethical problems, one must know who is obliged to whom. Within its beliefs, the decision aid has this concept encoded as [person][duty][person], which has now, in reaction to Paul's statement in section A, been transformed into a question, [?person][duty] [person:liberal]. Note the object of the sentence is now labeled liberal (the plural was ignored). This kind of information can be used in discussions with the decision aid user.

![](/api/attachments/QXEWCJYC/fulltext/images/e8271245b55c75321e52d31ecb34c8b784234d6f9212dc78b08d02c1361c1eee.jpg)  
Fig. 2. Example dialog between Paul (decision aid user) and decision aid (advisor role).

Based on Paul's response (within the dialog in section E) the decision aid now labels the noun of the sentence, that is, person, with “legislator”. In memory, the decision aid now has [person:legislator][duty] [person:liberal] stored (i.e., there is a fact that has been confirmed by my user and it is ‘legislators owe duties to liberals’.).

Now, in terms of section F: At this point either the decision aid knows (using a combination of its ontology and dictionaries of meanings) what a legislator does (that is, a legislator makes laws to preserve rights), or if it does not, the decision aid will ask Paul to give him a definition of what a legislator does. A dictionary entry might be:

Key==‘legislator’, Value==‘makes laws’, Value== ‘preserves rights’.

In terms of sections G and H: After some clarification, the decision aid understands what Paul is saying. The decision aid, after confirmation, stores the following belief, in the BDI instance of Paul that it is maintaining:

{[person][need][law]}[avoid][inappropriate use]

At section I, after following the sequence of instructions shown as pseudocode below,

Pseudocode: IF [person][need][law]and

Pseudocode: [legislator][make][law]

Pseudocode: THEN [legislator?][know?]

Pseudocode: ([person][need][law]) AND

Pseudocode: should([law][to be][content?])the decision aid asks Paul “Do the legislators know that a law may be necessary?” and “What should the content of the law be?”

The dialog continues with the decision aid following procedural logic, instantiating question oriented beliefs as described above. During this effort, it is attempting to achieve the goal of reducing the number of questions available (not answered) for all ethical reasoning approaches that Paul will entertain. Of course, if Paul wishes for no more advice, this can be accommodated as well.

## 4.3. Group Facilitator

The Group Facilitator decision aid role has all the characteristics and skills of an Advisor, but its distinct purpose is to support a group's processes. Prior to use, groups can provide information regarding each member's values, ethical ideologies, moral reasoning heur istics, and personality traits, via a querying session with the decision aid, or alternatively, the decision aid, will perceive this information via analysis of communications among group members. The aid will maintain the shared mental image in the form of a conceptual graph [70] that can be understood and manipulated by individual group members. But its real purpose is to identify group members that have one or more of the following characteristics: 1) introversion, 2) low locus-of-control, 3) low ego strength, 4) high agreeableness, 5) low conscientiousness, 6) high neuroticism and 7) low levels of openness, and support these individuals. The Group Facilitator decision aid role will model each person in the group using a BDI model (Fig. 1(b)). It will also build a tailored strategy for supporting each group member; based upon their values, ethical ideology, heuristics and personality. The Group Facilitator updates the BDI model beliefs as individual beliefs are discovered from communications. It will implement each strategy, which may include talking (for now, via a computer screen) directly to members or joining subgroups of members. If particular statements made by the less influential person can be made defensible via use of its knowledge bases, the aid will express a supporting argument to the group. The decision aid will also have its own Main BDI instance, which is essentially the advisor BDI instance discussed in Section 4.2, but complemented with knowledge about how groups work, such as typical roles and characteristics of individuals within those roles or effects of status on group process, as well as a data structure that stores group interaction history. This Main BDI instance also keeps information about the problem and the developing solution. The information is kept within the Main BDI instance's beliefs. The BDI model instances for each group member provide support for the decision aid's main BDI instance that interacts with the actual group. Another sample session, based upon the problem discussed in Section 4.1, is now used to illustrate the Group Facilitator.

After Paul sends a memo to the Minister of Health, he finds himself invited to a meeting with a staff person of the Ministry of Health, Robert McElroy, and a staff person of the Information and Privacy Commissioner, Michelle Leahy. The dialog of the meeting is shown in Fig. 3. The material to follow is based upon the dialog in Fig. 3.

Beginning at section J, the decision aid notes directed speech to Robert, but not Paul, and the following updates occur to the beliefs within the Main BDI instance.

[Michelle]→[communicate]→[Robert]→[content]→ [acknowledgement]

[Michelle]→[chose]→[communicate]→[Robert] (count==1)

not{[Michelle]→[chose]→[communicate]→[Paul]} (count==1)

Again, at dialog section K, the decision aid again notes the directed speech to Robert, but not Paul:

[Michelle]→[chose]→[communicate]→[Robert] (count==2)

not{[Michelle]→[chose]→[communicate]→[Paul]} (count==2)

Now, in terms of section L, the decision aid notes broadcast communication and notes phrasing to be not a resounding affirmative, possibly implying that this speaker (Michelle) is not high on the personality factor ‘agreeableness’. The BDI instance that models Michelle now receives a low value for agreeableness which is inserted into its personality data structure. The BDI Personality record for Michelle that has “agreeablenesslow” placed within it also receives a subjective probability of “somewhat certain” since the behavior exemplifying this personality trait has not been observed repeatedly in the Group Facilitator's interaction with Michelle. Continuing with how the Group Facilitator may arrive at values for personality traits, in section M, the decision aid notes that it is probable that Michelle's directive statement indicates a strong locus of control. In section N, because of the use of the word “wrong” the decision aid recognizes that the discussion definitely has an ethical component. At section O, the decision aid, by referring to a dictionary that shows dependency relationships between the words “law” and “enforcement” now uses this information to drive the leading statement “It seems like laws are just the beginning.”

At section P, the decision aid recognizes Paul did not speak and that this fact, combined with the fact that its previous history of analyzing Paul's (lack of) interactions indicates that Paul is very introverted and that it (the decision aid) needs to pull Paul into the conversation. Finally, at section Q, by requesting Michelle's permission to continue, the decision aid addresses Michelle's strong locus-of-control again, after first referencing a dictionary for message content.

## 4.4. Interaction Coach

An Interaction Coach while containing the moral reasoning heuristics of the advisor, and the capabilities of

(a)

Robert (to Michelle): Michelle, thanks so much for taking the time to meet with us.

J-Michelle (to Robert): I’m with you Robert. -J

Paul (awkwardly): Michelle, good to meet you. I’m sure we can figure most of this out. The benefits seem to tremendously outweigh the costs, but that’s just me. And I know I can see the technica aspects and that, to many folks out there, it’s a big unknown black box.

K-Michelle (to Robert): Robert, so where do you want to start? -K

Robert: Well, first things first. Paul has this new gadget, he calls it his “ethics decision aid”. It is supposed to keep up with you and help out here and there. Do you see any reason why we can’t let it be part of the festivities today?

L-Michelle (to Robert and for the first time, Paul): Anything to help with the scenario, guys. -L

Paul: I turned it on just before you walked in the room. I wanted to make sure my “helper” had the same information we had.

M-Michelle: Hmm…ok…Well let’s get kicking. -M

N-Michelle (to Robert): Robert, you know my main concerns already I’m sure. But basically I’m worried about folks using this thing for the wrong purposes. -N

Robert (to Michelle): Do we have a list?

Michelle: Sure do. George, my human assistant, (with emphasis) has been working on it all morning,…here it is.

Robert: So we need to suggest some ideas for the legislative bills.

Decision Aid: Excuse me, can I jump in?

Fig. 3. A portion of a sample session with the group facilitator role of the decision aid.

(b)

Michelle: (surprised) Sure.

O-Decision aid: It seems that the laws are just the beginning. -O

Robert: How so. Decision aid: Well, laws need to be enforced, right?

P-Michelle and Robert in unison: Yes. -P

Decision aid: Paul, what do you think?

Paul: Yes, I agree.

Q-Decision aid: Iíll log that in as an open item. Iíll keep going here, if that’s ok, Michelle? -Q

Decision aid: What do we need for enforcement for these laws? My database tells me that enforcemen is dependent upon an ability to monitor, is this right?

Michelle: of course.

Decision aid: Is there anything else we need to look at?

[Robert and Michelle now somewhat bored with the dry conversation led by the decision aid, jump in and discuss content of bills for laws and suggested enforcement processes for several minutes. Paul, because he believes he is the least powerful person in the room, remains quiet.]

Decision aid: Iím sorry to speak up again, but my program keeps telling me to break in, and I havenít got a chance to … can I jump in?

[Paul looks at Robert and Michelle, and Michelle gives an approving nod.] Paul: Sure.

Decision aid: Well, folks, pardon me for saying so, and since I’m a machine I don’t have to worry about my ego or yours, but I’ve really noticed that you really arenít including Paul in your conversation. It seems such a waste of the Ministry’s time and money not to be using this gentleman’s knowledge just because he appears to be a little bit shy. Oh, and just one more thing, we still haven’t gotten to “monitoring” the appropriate use of Pharmanet. Perhaps Paul could enlighten us with his thoughts, what do you think?

[and so on]

continued

the group facilitator, will additionally focus on helping an individual represent and communicate their ideas to the group. In order for the Interaction Coach to act in this role,

BDI model instances will need to simulate each person within the decision aid. As with the Group Facilitator, the instances will have embedded values, ethical ideologies, and beliefs about their capabilities (e.g., locus of control), ego strength, knowledge about the world around them and themselves, and personalities that mimic the persons these models simulate. For each BDI model instance that simulates a person, that agent's moral reasoning heuristics and communications within the group will be driven by those embedded characteristics.

As mentioned, the Belief–Desire–Intention (BDI) model will be used to simulate and inform ethical reasoning (and the communication) within this multiagent system. In the work described here, however, a production system ([65]) framework is proposed to be embedded within the BDI framework, within BDI Plans. A primary characteristic of production systems is the use of the IF (conditions) THEN (actions) rule type [65]. Production systems are “widely employed for representing the processes that operate in models of cognitive systems ([65], p. 676)”. These BDI Plans are implemented based upon the states of an agent's Beliefs or conditions in the agent's environment, perceived via Events. In essence, the BDI Plans composed of production rules can simulate “cognitions” and create “communicative behaviors”, based upon what is “happening” in the simulated environment, and what the agent “believes”.

The Interaction Coach also has a Main BDI model instance. Its Main BDI model instance has (pre-stored) the empirical relationships that exist between various combinations of moral development levels, values, ethical ideologies and moral reasoning heuristics, as well as personality traits and communication behavior. (This type of information is currently being researched by the authors.)

The Interaction Coach can apply this productionrule-BDI-Plan knowledge to transform a problem into potential future states, which it accepts as input explicitly from the user or implicitly via conversations. A session with the decision aid in this context would begin with Paul entering information into the decision aid for each person in the group that will be addressing the ethical problem. Paul will enter what he believes to be the moral development level, values, ideology, ego strength, locus of control, and personality characteristics for each person in the room [33].

Paul will also need to input the information he believes each person knows about the problem. At this point, Paul would place himself within the virtual meeting room (Note: Paul has already entered in his own values, ethical ideology, etc.), and he starts the session off with a particular question or statement. Paul then iteratively plays out various questions. For example, he might ask, “How will Robert respond if I suggest to him that we need another 6 months so that we can consider the issues more fully?” Alternatively, if Paul is going to be meeting with individuals that he does not know, Paul could ask the decision aid to execute a large number of runs with randomized values for the each of the ethical problem solving parameters (i.e., moral development level, values, ethical ideology), and see how a particular suggestion is received (or not received) by the “average” participant.

## 4.5. Forecaster

The decision aid may also perform the role of Forecaster. An individual (or group) that is considering a problem can use the forecaster to determine the effects of instituting a particular solution to an ethical problem, or more importantly, to provide information regarding the likelihood of an ethical problem surfacing. The components of the Forecaster are: individual software agents that simulate communicative behaviors of individuals within the environment of the ethical problem. In the case of Pharmanet, the types of individuals that would be modeled by software agents are pharmacy patrons, pharmacists, physicians, government employees related to initiating or implementing the project such as the Minister of Health or Paul Tier, the project manager. Other individuals would be advocates of rights of individuals, including government employees (e.g., the Information and Privacy Commissioner) as well as members of groups such as the B.C. Civil Liberties Association and the B.C. Freedom of Information and Privacy Association. Over time, distributions regarding factors like values, ethical ideology, and personality that affect ethical problem solving will be discovered scientifically, as suggested above. Not only will this information be known, but it will be known at the detail of “types” of people. When this information is known, probability distributions about the likelihood of an issue arising can be determined by using empirically grounded models of how the various types of people interact (as well as how values, ethical ideology, moral development level affect cognitions or personality affect behavior), and executing the software implementation iteratively. The resultant distribution (created by the Forecaster role) can then inform the decision aid user as to whether an ethical problem will surface. If an ethical problem will surface, the Advisor, Group Facilitator, or Interaction Coach roles may be used.

## 5. Conclusion and summary

Ethics has traditionally been normative. In the second half of the twentieth century, descriptive ethics matured, providing theories such as the Theory of Moral Development [36], a Taxonomy of Ethical Ideologies [20], the Four Component Model [57] and others [5,19,43]. Meanwhile, various communities in psychology created theories of values [59,63], personality traits [22,46], planned behavior [1], group process [37,71,74], and cognition [64,65,73] and the operations research modelers formalized the concept of problem solving [40,41]. Concurrently, the artificial intelligence community engineered the multi-agent [79] concept and developed the Belief–Desire–Intention (BDI) model [10,17,55]. This research suggests that computer-based support for ethical problem solving can be provided by integrating this knowledge in a dynamic computational model, providing support in the roles of Advisor, Group Facilitator, Interaction Coach, and Forecaster. Future researchers should also consider other factors such as emotion [23,48], situational factors [61] and inherent abilities [72].

## References

[1] I. Ajzen, The theory of planned behavior, Organizational Behavior and Human Decision Processes 50 (1991) 179–211.

[2] L. Albright, D.A. Kenny, T.E. Malloy, Consensus in personality judgments at zero acquaintance, Journal of Personality and Social Psychology 55 (1988) 387–395.

[3] H.E. Allison, Kant, Immanuel, in: T. Honderich (Ed.), The Oxford Companion to Philosophy, Oxford University Press, Oxford, 1995, pp. 435–438.

[4] Aristotle, in the Nichomacheon Ethics of Aristotle, translated by F.H. Peters (K. Paul, Trench, Trubner, and Co., 350 BCE/1901).

[5] D. Bartlett, Management and business ethics: a critique and integration of ethical decision-making models, British Journal of Management 14 (2003) 223–235.

[6] R.F. Baumeister, J.M. Twenge, Personality and social behavior, in: N.J. Smelser, P.B. Baltes (Eds.), International Encyclopedia of the Social and Behavioral Sciences, Elsevier Science Publishers B.V., Amsterdam, 2004, pp. 11276–11281.

[7] J. Bentham, in: W. Harrison (Ed.), Introduction to the Principles of Morals and Legislation, Hafner Press, Oxford, 1789/1945.

[8] M.H. Bond, W.F. Shiu, The relationship between a group's personality resources and the two dimension of its group process, Small Group Research 28 (2) (1987) 265–280.

[9] B.L. Bonner, The effects of extroversion on influence in ambiguous groups tasks, Small Group Research 31 (2) (2000) 225–244.

[10] M.E. Bratman, Intentions, Plans, and Practical Reason, Harvard University Press, Cambridge, MA, 1987.

[11] O.G. Brim, D.C. Glass, D.E. Lavin, N. Goodman, Personality and Decision Processes: Studies in the Social Psychology of Thinking, Stanford University Press, Stanford, CA, 1962.

[12] M.K. Chang, Predicting unethical behavior: a comparison of the theory of reasoned action and the theory of planned behavior, Journal of Business Ethics 17 (16) (1998) 1825–1834.

[13] E. Chee, S. Schneberger, British Columbia's PHARMANET Project, University of Western Ontario—Richard Ivey School of Business (1998).

[14] P.E. Connor, B.W. Becker, Personal value systems and decisionmaking styles of managers, Public Personnel Management 32 (1) (2003) 155–180

[15] R. Crisp, Deontological ethics, in: T. Honderich (Ed.), The Oxford Companion to Philosophy, Oxford University Press, New York, 1995, pp. 187–188.

[16] M.A. Davis, M.G. Anderson, M.B. Curtis, Measuring ethical ideology in business ethics: a critical analysis of the ethics position questionnaire, Journal of Business Ethics 32 (1) (2001) 35–53.

[17] M. d'Inverno, M. Luck, M. Georgeff, D. Kinny, M. Wooldridge, The dMARS Architecture: a specification of the distributed multi-agent reasoning system, Autonomous Agents and Multi-Agent Systems 9 (2004) 5–53.

[18] N.T. Feather, Values, Achievement, and Justice: Studies in the Psychology of Deservingness, Kluwer/Plenum, New York, 1999.

[19] R.C. Ford, W.D. Richardson, Ethical decision making: a review of the empirical literature, Journal of Business Ethics 13 (3) (1994) 205–221.

[20] D.R. Forsyth, A taxonomy of ethical ideologies, Journal of Personality and Social Psychology 39 (1) (1980) 175–184.

[21] D.J. Fritzsche, A model of decision-making incorporating ethical values, Journal of Business Ethics 10 (11) (1991) 841–922.

[22] D.C. Funder, Personality, Annual Review of Psychology 52 (2001) 197–221.

[23] A. Gaudine, L. Thorne, Emotion and ethical decision making in organizations, Journal of Business Ethics 31 (2) (2001) 175–187.

[24] B. Gert, Morality: A New Justification of the Moral Rules, Oxford University Press, New York, 1988.

[25] C. Gilligan, Concepts of the Self and of Morality, Harvard Educational Review (November 1977): 481–517. Reprinted In a Different Voice: Women's Conceptions of Self and of Morality, in: M. Pearsall (Ed.), Women and Values: Readings in Recent Feminis Philosophy, Wadsworth, Belmont, CA, 1993, pp. 342–368.

[26] S.H. Glover, M.A. Bumpus, J.E. Logan, J.R. Ciesla, Re-examining the influence of individual values on ethical decision making, Journal of Business Ethics 16 (12/13) (1997) 1319–1329.

[27] I.M. Goldin, K.D. Ashley, R.L. Pinkus, in: H. Prakken, R.P. Loui (Eds.), Introducing PETE: Computer Support for Teaching Ethics, Proceedings of the Eighth International Conference on Artificial Intelligence and Law (ICAIL-2001), Association of Computing Machinery, New York, 2001.

[28] J.P. Griffin, Consequentialism, in: T. Honderich (Ed.), The Oxford Companion to Philosophy, Oxford University Press, New York, 1995, pp. 154–156.

[29] R. Hastie, H.R. Arkes, L. Lopes, J. Baron (Eds.), Inside the Juror: The Psychology of Juror Decision Making, (Cambridge Series on Judgment and Decision Making), Cambridge University Press, Cambridge, 1993.

[30] J.R. Hayes, The Complete Problem Solver, 2nd ed.,Erlbaum, Hillsdale, NJ, 1989.

[31] R.W. Hepburn, Practical Reason, In T. Honderich, The Oxford Companion to Philosophy, Oxford University Press, Oxford, p. 709.

[32] T. Honderich (Ed.), The Oxford Companion to Philosophy, Oxford University Press, Oxford, 1995.

[33] J.N. Hooker, Can I Be Transplanted into a Computer, 1989/1991. http://web.tepper.cmu.edu/jnh/papers.html.

[34] J.N. Hooker, Three Kinds of Ethics, 1996. http://web.tepper.cmu. edu/jnh/papers.html.

[35] I. Kant, Grounding of the Metaphysics of Morals, Hackett Publishing Company, Indianapolis, IN, 1785/1981 (translated by J.W. Ellington).

[36] L. Kohlberg, Stage and sequence: the cognitive-development approach to socialization, in: D.A. Goslin (Ed.), Handbook of Socialization Theory and Research, Rand McNally, Chicago, 1969.

[37] P.R. Laughlin, Collective induction: twelve postulates, Organizational Behavior and Human Decision Processes 80 (1) (1999) 50–69.

[38] L.N.K. Leonard, T.P. Cronan, J. Kreie, What influences IT ethical behavior intentions—planned behavior, reasoned action, perceived importance, or individual characteristics? Information and Management 42 (2004) 143–158.

[39] C. Lin, C.G. Ding, Modeling information ethics: the joint moderating role of locus of control and job insecurity, Journal of Business Ethics 48 (4) (2003) 335–346.

[40] R. Lipshitz, O. Bar-Ilan, How problems are solved: reconsidering the phase theorem, Organizational Behavior and Human Decision Processes 65 (1) (1996) 48–60.

[41] J.D.C. Little, On model building, in: W.A. Wallace (Ed.), Ethics in Modeling, Elsevier, New York, 2004, pp. 167–182.

[42] K.D. Loch, S. Conger, Evaluating ethical decision making and computer use, Communications of the ACM 39 (7) (1996) 74–83.

[43] T.W. Loe, L. Ferrell, P. Mansfield, A review of empirical studies assessing ethical decision making in business, Journal of Business Ethics 25 (3) (2000) 185–204.

[44] R.E. Lucas, E. Diener, Extraversion, in: N.J. Smelser, P.B. Baltes (Eds.), International encyclopedia of the social and behavioral sciences, Elsevier Science Publishers B.V., Amsterdam, 2001, pp. 5202–5205.

[45] R.O. Mason, Four ethical issues of the information age, MIS Quarterly 10 (1) (1986) 5–12.

[46] R.R. McCrae, O.P. John, An introduction to the five-factor model and its applications, Journal of Personality 60 (1992) 175–215.

[47] B.M. McLaren, Extensionally defining principles and cases: an AI model, Artificial Intelligence Journal 150 (2003 (November)) 145–181.

[48] K. Oatley, Emotion in cognition, International Encyclopedia of the Social and Behavioral Sciences, Elsevier Science Publishers B.V., Amsterdam, 2001, pp. 4440–4444.

[49] A.G. Peace, D.F. Galletta, J. Thong, Software piracy in the workplace: a model and empirical test, Journal of MIS 20 (1) (2003) 153–177.

[50] G. Polya, How to Solve It, Basic Books, New York, 1957.

[51] W.F. Pounds, The process of problem finding, Industrial Management Review 11 (1969) 1–19.

[52] B. Puka, Report on documenting a step-by-step procedure for solving ethical problems, Fifth Annual Computer Ethics, Philosophical Enquiry Conference. International Society for Ethics and Information Technology. Boston, MA. June 2003.

[53] A. Rand, The Virtue of Selfishness, New American Library, New York, 1964.

[54] Random House, Inc., Webster's Unabridged Dictionary of the English Language (New York, 1987).

[55] A.S. Rao, M.P. Georgeff, Modeling rational agents with a BDIarchitecture, in: A.J. Fikes, E. Sandwell (Eds.), Proceedings of Knowledge Representation and Reasoning, KR and R91, Morgan Kaufmann, San Mateo, CA, 1991, pp. 473–484.

[56] J. Rawls, A Theory of Justice, Harvard University Press, Cam bridge, MA, 1971.

[57] J.R. Rest, Moral Development: Advances in Research and Theory, Praeger, New York, 1986.

[58] R.W. Robbins, W.A. Wallace, B. Puka, Supporting ethical problem solving: an exploratory investigation, Proceedings of the Association for Computing Machinery, SIGMIS-CPR, Associa tion for Computing Machinery, Tucson, AZ, (April 2004).

[59] M. Rokeach, The Nature of Human Values, The Free Press, New York, 1973.

[60] W.D. Ross, The Right and the Good, Oxford University Press, Oxford, 1930.

[61] W.T. Ross, A typology of situational factors: impact on salesperson decision-making about ethical issues, Journal of Business Ethics 46 (3) (2003) 213–234.

[62] S. Schneberger, E. Chee, British Columbia's PHARMANET Project: Teaching Note, University of Western Ontario, Richard Ivey School of Business, London, Ontario, 1999.

[63] S.H. Schwartz, Value priorities and behavior: Applying a theory of integrated value systems, in: C. Seligman, J.M. Olson, M.P. Zanna (Eds.), The Psychology of Values: The Ontario Symposium, vol. 8, Erlbaum, Mahweh, NJ, 1996, pp. 1–24.

[64] H.A. Simon, Problem solving, in: R.A. Wilson, F.C. Keil (Eds.), The MIT Encyclopedia of the Cognitive Sciences, MIT Press, Cambridge, MA, 1999, pp. 674–676.

[65] H.A. Simon, Production systems, in: R.A. Wilson, F.C. Keil (Eds.), The MIT Encyclopedia of the Cognitive Sciences, MIT Press, Cambridge, MA, 1999, pp. 676–677.

[66] A. Singhapakdi, S.J. Vitell, Personal and professional values underlying the ethical judgments of marketers, Journal of Business Ethics 12 (1993) 525–533.

[67] M. Slote, Virtues, in: T. Honderich (Ed.), The Oxford Companion to Philosophy, Oxford University Press, New York, 1995, pp. 900–901.

[68] M. Snyder, N. Cantor, Understanding personality and social behavior: a functionalist strategy, in: D.T. Gilbert, S.T. Fiske, G. Lindzey (Eds.), The Handbook of Social Psychology, vol. one, McGraw-Hill, Boston, 1998, pp. 635–679.

[69] R.C. Solomon, J.K. Greene, Morality and the Good Life: An Introduction to Ethics through Classical Sources, McGraw-Hill, New York, 1999.

[70] J.R. Sowa, Knowledge Representation: Logical, Philosophical, and Computational Foundations, Brooks/Cole-Thomson Learning, Pacific Grove, CA, 2000.

[71] I.D. Steiner, Task-performing groups, in J.W. Thibaut, J.T. Spence, R.C. Carson (Eds.) Contemporary topics in social psychology (General Learning Press, Morristown, NJ, 1976) 393–422.

[72] R.J. Sternberg, J.C. Kaufman, Human abilities, Annual Review of Psychology 49 (1998) 479–502.

[73] M. Wagman, Problem-Solving Processes in Humans and Computers—Theory and Research in Psychology and Artificial Intelligence, Praeger, Westport, CT, 2002.

[74] D.G. Wagner, J. Berger, Status characteristics theory: the growth of a program, in: J. Berger, M. Zelditch Jr. (Eds.), Theoretical Research Programs: Studies in the Growth of Theory, Stanford University Press, Stanford, CA, 1993, pp. 24–63.

[75] W.A. Wallace (Ed.), Ethics in Modeling, Elsevier, New York, 1994.

[76] R.J. Wallace, Practical reasoning: philosophical aspects, in: N.J. Smelser, P.B. Baltes (Eds.), International Encyclopedia of the Social and Behavioral Sciences, Elsevier Science, Oxford, 2001, pp. 11939–11945.

[77] M. Walzer, Spheres of Justice: A Defense of Pluralism and Equality, Basic Books, New York, 1983.

[78] D. Watson, Neuroticism, International Encyclopedia of the Social and Behavioral Sciences, Elsevier Science Publishers B.V., Amsterdam, 2001, pp. 10609–10612.

[79] M.P. Wellman, Multiagent Systems, The MIT Encyclopedia of the Cognitive Sciences, MIT Press, Cambridge, MA, 1999, p. 573.

[80] G.M. Wittenbaum, A.B. Hollingshead, P.B. Paulus, R.Y. Hirokawa, D.G. Ancona, R.S. Peterson, K.A. Jehn, K. Yoon, The functional perspective as a lens for understanding groups, Small Group Research 35 (1) (2004) 17–43.

![](/api/attachments/QXEWCJYC/fulltext/images/55d42696fc08525de6fb69b102f0dcd0f2ec6e9e75213ddbd3dffd028932dc8b.jpg)  
Russell W. Robbins is an assistant professor of information systems at Marist College in Poughkeepsie, New York. He was one of four finalists in the 2004 Excellence in Ethics: Dissertation Proposal competition held at the Institute for Ethical Business Worldwide in the Mendoza College of Business at the University of Notre Dame.

![](/api/attachments/QXEWCJYC/fulltext/images/2450bee42d3efa02082a31e506e288185047b4a1fadc1b600602a359dbd370ab.jpg)

William A. Wallace is a professor of decision sciences and engineering systems at Rensselaer Polytechnic Institute in Troy, New York. He has joint appointments in cognitive science and civil and environmental engineering. Since 1990, he has authored and edited six books and over 100 articles and papers, with more than 250 publications in total. He has published in journals such as Management Science, IEEE Transactions on Systems, Man and Cybernetics, IEEE Transactions in

Engineering Management, Decision Support Systems, and MIS Quarterly. Professor Wallace received the 2004 Institute for Operations Research and the Management Sciences (INFORMS) President's Award for his work in public service systems, is an Institute of Electrical and Electronics Engineers' Fellow and received the Institute of Electrical and Electronics Engineers' Third Millennium Medal.
