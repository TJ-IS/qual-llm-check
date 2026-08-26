---
otero_id: 26750
otero_key: "XNBHXR6R"
title: "The Calculus of Reengineering"
authors: "Anitesh Barua; C. H. Sophie Lee; Andrew B. Whinston"
year: "1996"
journal: "Information Systems Research"
doi: "10.1287/isre.7.4.409"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [131.94.16.10] On: 25 August 2015, At: 12:25 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## HSR

## Information Systems Research

![](/api/attachments/XNBHXR6R/fulltext/images/6ced479b49dbfc22c270a9199131bcb66681ca75adc26848fa56da88443773af.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## The Calculus of Reengineering

Anitesh Barua, C. H. Sophie Lee, Andrew B. Whinston,

## To cite this article:

Anitesh Barua, C. H. Sophie Lee, Andrew B. Whinston, (1996) The Calculus of Reengineering. Information Systems Research 7(4):409-428. http://dx.doi.org/10.1287/isre.7.4.409

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article's accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1996 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/XNBHXR6R/fulltext/images/3310676b0824e3a880e9a34dce17901a46cc14ec048ab0ed38dca9a8d22f4c23.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# The Calculus of Reengineering

Anitesh Barua • C. H. Sophie Lee • Andrew B. Whinston

Department of Management Science and Information Systems, Graduate School of Business,

The University of Texas at Austin, Austin, Texas 78712

barua@mail.utexas.edu

Management Information Systems, College of Management, University of Massachusetts at Boston,

Boston, Massachusetts 02125

sophie@umbsky.cc.umb.edu

Department of Management Science and Information Systems, Graduate School of Business,
The University of Texas at Austin, Austin, Texas 78712
abw@uts.cc.utexas.edu

Advances in new Information Technologies (IT) and changes in the business environment such as globalization and competitive pressure have prompted organizations to embark on reengineering projects involving significant investments in IT and business process redesign. However, the evidence of payoff from such investments can be classified as mixed as best, a problem we partly attribute to the absence of a strong theoretical foundation to assess and analyze reengineering projects. We seek to apply complementarity theory and a business value modeling approach to address some questions involving what, when, and how much to reengineer. Complementarity theory is based on the notion that the value of having more of one factor increases by having more of another complementary factor. Further, related developments in the optimization of “supermodular” functions provide a useful way to maximize net benefits by exploiting complementary relationships between variables of interest. Combining this theory with a multi-level business value model showing relationships between key performance measures and their drivers, we argue that organizational payoff is maximized when several factors relating to IT, decision authority, business processes and incentives are changed in a coordinated manner in the right directions by the right magnitude to move toward an ideal design configuration. Our analysis further shows that when a complementary reengineering variable is left unchanged either due to myopic vision or self-interest, the organization will not be able to obtain the full benefits of reengineering due to smaller optimal changes in the other variables. We also show that by increasing the cost of changing the levels of design variables, unfavorable pre-existing conditions (e.g., too much heterogeneity in the computing environment) can lead to reengineering changes of smaller magnitude than in a setting with favorable conditions.

(Business Value; Complementarity; Reengineering; Organizational Design; Radical Change; Supermodularity)

## 1. Introduction

The nineties have witnessed dramatic advances in Information Technologies (IT), especially in the domains of networking and distributed computing. These new technologies have created new opportunities for improving the conduct of business. Such opportunities, coupled with major changes in the external environment (such as increased competition and globalization) have prompted organizations to reassess their basic operations. Many have undertaken large strategic reengineering projects to improve business processes, in an attempt to increase efficiency and stay competitive. Any major business process redesign (BPR) project involves large investment in IT (Davenport 1993). Since reengineering also entails major organizational changes and hence potential instability, decisions to invest in reengineering projects should be based on its bottom-line performance impacts. However, in the absence of clear guidelines of when, what, and how much to reengineer, many reengineering projects appear to be implemented on a leap of faith. There is no formal basis or a theoretical foundation to explain and guide what factors (external and internal to the firm) need to be assessed, and which target variables should be reengineered and to what extent.

Although reengineering has been one of the most popular concepts of this decade, anecdotal evidence suggest that the payoff from reengineering efforts and IT investments is mixed at best. Based on his observations of numerous reengineering projects, Michael Hammer estimates a failure rate of up to 70% (Leibs 1994). According to a Wall Street Journal article (Bleakley 1993), many firms find the effects of reengineering unsatisfactory or minor. A study by Bashein et al. (1994) reports that while some organizations have enjoyed very positive results from reengineering, 70% of projects have ended in failure. Based on interviews with 350 executives in 14 industries, an Arthur D. Little study in 1994 found that 85% of the executives were dissatisfied to some extent with their reengineering activities (Rock and Yu 1994). While several hypotheses have been put forth by reengineering experts (e.g., expecting too much too soon, Hammer and Champy 1993; lack of partnership between IT and business, Martinez 1995), we conjecture two more potential reasons for the mixed results reported in the literature. First, reengineering projects might have been undertaken without a complete understanding of associated costs and benefits. This problem can be partly attributed to the fact that the reengineering literature does not offer guidelines for tracing and measuring the impact of reengineering changes on organizational payoff. Second, while reengineering may be potentially profitable in a given setting, a lack of understanding of how to redesign a set of related activities may lead to disappointing results. To address these issues we present a theory we call business value complementarity. It combines two key elements for maximizing net value from reengineering investments:

(1) A business value model provides a basis for understanding linkages between critical performance measures, organizational parameters and design variables. The business literature provides examples of companies choosing inappropriate variables for reengineering projects (e.g., Stewart 1993). It may be the case that a reengineering project is targeted toward a set of variables which have little or no impact on the organizational payoff. Thus, even if the reengineering project is completed successfully (where the target variables are indeed affected as desired), the net value of the project may still be insignificant or negative due to the tenuous association between the target variables and financial performance metrics. To address this issue, we use a business value modeling approach for assessing the impacts of reengineering (decision) variables on intermediate level performance measures, and those of the latter on higher level measures such as profitability and growth.

(2) The notion of complementarity was originally introduced in economics by Edgeworth (1881) to reflect the idea that increasing one factor will increase the benefit of increasing its complementary factors, and it has been used by Milgrom and Roberts (1990) to rationalize a pattern of decisions made by modern manufacturing firms. Applying complementarity theory to the field of reengineering, we argue that IT is complementary with organizational characteristics and processes, and that investments in IT and reengineering cannot succeed if done in isolation. For instance, the same set of hardware and software platforms may generate high productivity in one company but not in another, because the former company may have characteristics (either pre-existing or redesigned) that are complementary with the nature of the technology. Thus, to maximize organizational payoff, complementary factors such as technology, decision authority, business processes, and incentives must all be changed in a coordinated fashion in the right direction by the right magnitudes to move toward an ideal design configuration. This is our complementarity theoretic interpretation of the prescription of “radical change” in the reengineering literature (e.g., Hammer and Champy 1993), and it implies a concerted change in a possibly large set of design variables. However, we do not interpret “radical change” as implying a change of large magnitude. In fact, our analysis reveals that when certain pre-existing organizational conditions (which affect reengineering and operating costs) are unfavorable, changes of smaller magnitude should take place in all complementary variables. Thus, we distinguish between coordinated changes in all complementary variables and the magnitudes of such changes. While coordinated changes are a must for any reengineering project, their magnitudes will decrease (increase) with increasingly unfavorable (favorable) pre-existing conditions.

Along similar lines, if individual managers or groups decide (due to a variety of reasons, including and self-interest lack of vision) not to change one or more complementary design variables, we show that the optimal levels of the other variables become smaller, and that it is not in the best interest of the organization. Thus, senior management vision regarding the overall business value model is critical for the organization to obtain maximum reengineering payoff. Our results imply that successful organizational design change management involves the creation and maintenance of a business value model, and the recognition and analysis of complementarity between various design variables and performance measures.

The tools used to study this complementarity effect are techniques for optimization and sensitivity analysis of “supermodular” functions (Topkis 1978, 1994, 1995). In order to apply results from the supermodularity literature to our business value model, we derive a new result based on a concept we call the “degree of supermodularity”; through this result, we establish conditions for a composite function to be supermodular in the lowest level decision variables. We believe that business value complementarity provides a qualitative yet powerful approach for managers to analyze and assess reengineering variables and their impacts on chosen measures of organizational performance. The business value analysis involves disciplining ourselves to consider organizational design problems from the standpoint of complementarity theory. It suggests that (1) we attempt to uncover complementary relationships, where the impact of joint changes is more pronounced than that in a relationship without complementarity, and (2) we define states of variables and order them in a way (when feasible) that makes them complementary with other variables.

## 2. Prior Literature and Motivation

We start with a brief review of the literature on reengineering and draw upon some theories of organizational change from the domain of organizational behavior. A basis for assessing the business value of IT is also summarized to provide the motivation for developing an integrated approach to analyzing the payoff from reengineering projects.

## 2.1. Literature on Business Process Reengineering

Reengineering recognizes the potentially global impact of IT and associated organizational changes. Reengineering involves the redesign of a company's processes in a "radical" fashion (Hammer and Champy 1993). Proponents of reengineering suggest that incremental changes are inadequate to keep firms efficient and competitive, and that reengineering projects must involve radical changes. Common reengineering practices include business process redesign (BPR), adoption of team-based structures, decision making empowerment, and gainsharing reward systems. IT acquisition plays an important enabling role in most reengineering projects (Davenport 1993). Several characteristics of reengineering are summarized below.

First, reengineering emphasizes a process oriented (and not functional) perspective (Hammer and Champy 1993). Instead of organizing the company vertically and functionally, reengineering principles assert that companies should envision themselves as a collection of horizontal processes. For instance, the process of resolving customer complaints used to be divided along functional lines: the customer service department would handle the call; the message would then be sent to the shipping and handling department; the order would be sent to the manufacturing department, which would send the product to the shipping and handling department and an invoice to the accounting department; the final notification letter would be mailed out by the customer service department. However, the business value is determined by the total quality of the entire process, which may be lost in the many fragmented activities among departments.

Second, reengineering emphasizes radical, not incremental, changes (Hammer and Champy 1993). Because of the speed of change in today's business environment, reengineering proponents suggest that incremental improvements will not enable companies to remain efficient and competitive. The commonly held view is that companies must challenge all existing rules and assumptions, and make “quantum-leap” improvements. Reengineering practices include work flow redesign to break the Adam Smith division-of-labor attitude and to shift to a process oriented frame of thinking (Hammer and Champy 1993), upgrading IT, structural changes such as replacing the conventional hierarchical structure with cross-functional teams (Stewart 1993), and decision making empowerment (Harrar 1994). Reengineering also appears to encourage more group-based compensation. Many companies are moving from a totally individual, salary-based reward system to gainsharing compensation plans. While group-based compensation may intuitively appear to support team activities, Barua et al. (1995) present a detailed mathematical model of team productivity, individual versus group-based incentive systems, and their interactions with IT design features and task characteristics. In fact, they show that with certain IT design features and team composition, group-based rewards can lead to significant shirking and free-riding problems.

## 2.2. Contingency and Socio-technical Theories

Organizational behavior is a natural domain for theories on managing technological and organizational changes. Two relevant lines of research in organizational behavior are contingency and socio-technical theories. Contingency theory is based upon the concept that an organization's structure or design is dependent upon the organization's context (e.g., technology and external environment). It relies on the assumption that organizational performance is an outcome of the "fit" between relevant variables. Van de Ven and Drazin (1985) categorize contingency theory studies into three distinct groups involving selection, interaction, and systems approaches. Each of these viewpoints provides a different interpretation of fit. The interaction and systems approaches are particularly relevant for understanding reengineering change. The interaction perspective focuses on organizational performance, and suggests that it is dependent upon the interaction between contextual and structural variables. The systems approach accounts for multiple as well as conflicting contingencies, and is therefore better positioned to address complex reengineering interactions.

While contingency theory provides a conceptual basis for understanding organizational and technological change, a problem which is often cited as the limitation of contingency theory is the lack of a theoretical justification for the "fit" between variables (e.g., Schoonhoven 1991). Empirical studies often fail to establish a relationship between contextual variables and performance. Additionally, new relationships (which were not anticipated a priori) are discovered during the data analysis phases, indicating shortcomings in the theoretical support for the hypotheses of interest. Sociotechnical theory recognizes the role of technology more explicitly than contingency theory, and suggests that organizational outcomes depend upon both social and technological factors. The performance of the organization is hypothesized to be impacted by the compatibility or fit between social and technological variables. Unfortunately, reviews of socio-technical studies (e.g., see Beekun 1989) suggest that the fundamental premise of socio-technical theories did not get significant empirical support. The organizational literature on fit theory offers a rich problem description; however, the primary limitations appear to be the lack of a theoretical basis of "fit" and a tenuous connection between fit and business value. However, any reengineering project must ultimately be related to the firm's payoff. As seen in the balance of this section, a business value modeling approach provides a more concrete basis for identifying key performance measures and their drivers. Further, complementarity theory and the optimization of supermodular functions provide more operational insights than fit theory into the nature of changes involved.

## 2.3. Review of Process Oriented IT Business Value Measurement

Some studies on measuring economic impacts of IT have employed a process oriented view of how IT affects performance $^{1}$ (e.g., Barua 1989, 1995; Weill 1992). Barua et al. (1989, 1995), and Barua (1991) propose and empirically test a multi-stage business value model in the manufacturing sector which relates IT and other inputs to high level performance indicators (such as return on assets and market share) through a web of relationships involving intermediate output variables (such as inventory turnover and capacity utilization) and exogenous variables (such as market growth and GDP). This approach becomes more useful when complementarity theory and the optimization of supermodular functions are added to the business value model to analyze the directions and magnitudes of changes in decision variables and their impact on organizational payoff. While the business value model helps in identifying key performance measures and design variables, the optimization techniques provide a normative basis for achieving maximum payoff.

## 2.4. Challenges and Motivation for This Paper

While the practices mentioned in §2.1 appear to have become rules of reengineering, there is a void in terms of a theoretical basis which can explain why such rules may or may not be justified. For example, what (if any) is the theoretical justification of radical changes? Will the radical change approach pay off in every organizational context? Even more importantly, in which directions and by what magnitudes should the variables be changed? In a similar vein, the recommendation of adopting a process and horizontal orientation may cause severe problems without appropriate changes in incentive schemes. Thus, it is evident that the one-size-fits-all nature of recommendations implied by many reengineering principles may be inadequate for handling a wide variety of organizational environments.

As discussed above, the reengineering literature focuses on doing the reengineering right (e.g., whether changes should be large or small, whether BPR must start from scratch, etc.). An equally important question (which is not addressed systematically by conventional reengineering principles) involves doing the right reengineering. The goal of any reengineering project should be to improve intermediate level performance measures such as customer lead time and satisfaction, percentage of rework, etc., which in turn will improve bottom-line performance. Therefore, choosing the right set of intermediate variables and their drivers is critical to the overall success of a reengineering project. While reengineering prescriptions in the business literature offer a valuable starting point, the mixed stories of success point to the need for a theoretical foundation.

Recently, we have witnessed the resurgence of complementarity theory (Edgeworth 1881, Samuelson

1974), an old but powerful concept in economics. In studying the adoption of modern manufacturing technologies, Milgrom and Roberts (1990) note that successful firms tend to adopt a certain activity pattern such as low price, higher number of improvements, short order processing time, and lower probability of defective products. They suggest that these factors are complementary, such that when the firm decides to move one factor, the impact on profitability is more pronounced when other complements are also moved in the same direction. Milgrom and Robert's study is the first to recognize the role of complementarity theory in rationalizing related patterns of decisions made by manufacturing firms.

In the MIS literature, Barua et al. (1995) develop an economic model to analyze different facets of team productivity from the standpoint of interactions between technological and organizational variables. Similarly, this paper derives its motivation from the need to develop a basis for analyzing and assessing the interdependency between various factors affected by a reengineering project. To the best of our knowledge, this is the first attempt in the field of MIS to present this complementarity theoretic perspective on reengineering.

For the mathematical analysis, we rely on the seminal work of Topkis (1978, 1994a, 1994b) in the area of supermodular functions. Our objective is to apply the analysis of supermodularity to a business value model, and to use the resulting framework to better understand the reengineering phenomenon. A multi-level business value model brings in additional complexity in the supermodularity analysis. For example, in a two-stage model, where a top level function is supermodular in the intermediate variables, and where each intermediate variable is a supermodular function in the design variables, it is not automatically true that the top level function is supermodular in the design variables. Accordingly, we derive conditions under which the above relationship holds. To summarize, inspired by the pioneering work of Milgrom and Roberts (1990) in modern manufacturing, using mathematical techniques developed by Topkis (1978, 1994a, 1994b), and deriving a new result involving multiple levels of supermodularity, we develop a business value complementarity model of reengineering investments, and present a rational basis for making design decisions which lead to maximum payoff.

2.5. Supermodular Functions and Complementarity The theory of supermodularity (Topkis 1978) involves general functions defined on lattice spaces and does not require specific functional forms, continuity, or differentiability. While the neoclassical economic analog of supermodularity of a function in two variables is a nonnegative cross partial derivative (Topkis 1978), various reengineering choices pertaining to technology and organizational factors may be discrete, making it difficult to justify differentiability. Fortunately, such assumptions are unnecessary for the optimization and sensitivity analysis of supermodular functions. Since this area has not been addressed in prior MIS research, we provide a brief exposition of some central ideas. A detailed treatment is provided by Topkis (1978, 1995). In order to motivate the application of this theory to our problem setting, we provide examples drawn from IT investment and organizational change. Thus, while the mathematical formulations deal with n choice variables, $x_{1}, x_{2}, \ldots, x_{n}$ (denoted by a vector x), for the purpose of illustration, we use only two choice variables: (i) the level of information sharing (as determined by the underlying IT infrastructure), and (ii) the degree of employee empowerment (as reflected in the decision authority structure).

A poset is a partially ordered set. Elements in a poset have a binary relation denoted by $\leq$ . For instance, with two choice variables “level of information sharing” ( $x_{1}$ ) and “degree of empowerment” ( $x_{2}$ ), for two design configurations $x' = (x_{1}', x_{2}')$ and $x'' = (x_{1}', x_{2}')$ , we have $x' \leq x''$ only if $x''$ represents a level of information sharing and a degree of empowerment no less than those in $x'$ (i.e., if $x_{1}' \leq x_{1}''$ , and if $x_{2}' \leq x_{2}''$ ). However, if $x''$ involves a higher level of information sharing but a lower degree of empowerment, then the two elements are not comparable. Note that the variable “level of information sharing” pertains to the choice of the technology. Other variables relating to technology may include “degree of flexibility” (the ability to adapt to changing user needs), and “degree of user-friendliness.” Of particular interest from a complementarity theoretic standpoint are the elements which have more (or less) of every variable than other elements: For any two elements $x'$ and $x''$ of a poset $X, x' \vee x''$ defined as $(\max (x_1', x_1''), \ldots, \max (x_n', x_n''))$ is called the join, while $x' \wedge x''$ defined as $(\min (x_1', x_1''), \ldots, \min (x_n', x_n''))$ is called the meet. Continuing the above example of organizational change, the join is the element representing highest levels of both information sharing and empowerment, while the lowest levels of information sharing and empowerment denote the meet. Of course, this is based on the definition of the order, i.e., less sharing and less empowered. Next we discuss some restrictions on the feasible design space, and proceed to introduce the concept of a supermodular function.

DEFINITION 1. (TOPKIS 1978). A poset that contains the joins and meets of all pairs of its elements is a lattice. Let a lattice S have a partial order $\leq$ . A subset X of S, which has the joins and meets of all pairs of its elements under the same order $\leq$ is a sublattice.

The feasible organizational design choices must lie in a sublattice. For example, the definition implies that if the level of information sharing is increased, it is also simultaneously possible to increase employee empowerment.

DEFINITION 2 (TOPKIS 1978). Let $f(x)$ be a real valued function defined on a sublattice $X$ of $R^n$ . If for any two elements $x', x'' \in X$ , we have $f(x' \vee x'') + f(x' \wedge x'') \geq f(x') + f(x'')$ , then $f$ and $-f$ are supermodular and submodular functions respectively on $X$ .

To see the implications of the above definition, we rewrite the supermodularity condition as in Milgrom and Roberts (1990):

$$
\begin{array}{r l} f (x ^ {\prime} \vee x ^ {\prime \prime}) - f (x ^ {\prime} \wedge x ^ {\prime \prime}) & \geq [ f (x ^ {\prime}) - f (x ^ {\prime} \wedge x ^ {\prime \prime}) ] \\ & + [ f (x ^ {\prime \prime}) - f (x ^ {\prime} \wedge x ^ {\prime \prime}) ]. \end{array}\tag{1}
$$

If $f$ is increasing in $x$ , then the condition implies that increasing all choice variables simultaneously from $x' \wedge x''$ to reach $x' \vee x''$ has higher value than the sum of the values derived by moving from $x' \wedge x''$ to $x'$ , and from $x' \wedge x''$ to $x''$ . The arguments of a supermodular function are complementary in nature. To see this, rewrite the condition of supermodularity as

$$
f (x ^ {\prime} \vee x ^ {\prime \prime}) - f (x ^ {\prime}) \geq f (x ^ {\prime \prime}) - f (x ^ {\prime} \wedge x ^ {\prime \prime}).\tag{2}
$$

Equivalently, we have

$$
f (x ^ {\prime} \vee x ^ {\prime \prime}) - f (x ^ {\prime \prime}) \geq f (x ^ {\prime}) - f (x ^ {\prime} \wedge x ^ {\prime \prime}).\tag{3}
$$

For a simple illustration, consider two design variables, $x_{1}$ and $x_{2}$ , such that $x_{1}^{\prime} > x_{1}^{\prime\prime}$ , and $x_{2}^{\prime} < x_{2}^{\prime\prime}$ . Then Equation (2) can be rewritten as

$$
f (x _ {1} ^ {\prime}, x _ {2} ^ {\prime \prime}) - f (x _ {1} ^ {\prime}, x _ {2} ^ {\prime}) \geq f (x _ {1} ^ {\prime \prime}, x _ {2} ^ {\prime \prime}) - f (x _ {1} ^ {\prime \prime}, x _ {2} ^ {\prime}).\tag{4}
$$

Equation (4) shows that with the same amount of domain increase $(x_{2}^{\prime\prime}-x_{2}^{\prime})$ , the function value increases more when the design configuration moves from point $x^{\prime}$ to $x^{\prime}\vee x^{\prime\prime}$ than that from $x^{\prime}\wedge x^{\prime\prime}$ to $x^{\prime\prime}$ . That is, a given amount of increase in $x_{2}$ will increase the function value more when $x_{1}$ is at a high level than when $x_{1}$ is at a low level. Equation (3) can be interpreted similarly.

To provide an example of complementarity from our problem setting, consider an organization with a mainframe-based computing environment and a hierarchical decision structure. If the company were to migrate to a distributed computing environment with high connectivity (where it may be easier to share and get access to information) without changing the decision making structure, the payoff obtained from the investment in distributed computing may be limited. Without the empowerment, the new technology platform for better information sharing may not have a significant impact on business value. Similarly, changing decision rules to a flatter structure may not provide any benefit unless the old technology is replaced with one that enables seamless sharing of relevant information throughout the company.

Complementary changes in characteristics of IT, decision authority, business processes and incentives move the organizational design towards a new “ideal” configuration. We enhance the concept of “ideal types” (Weber 1968, Mintzberg; 1983) by suggesting that exogenous changes such as technological advances create the opportunity to make complementary changes to attain a better design.

## 3. A Business Value Complementarity Model of Reengineering

In order to derive insights into the nature of organizational decisions which will lead to maximum payoff from a reengineering project, we present an approach we call business value complementarity. Business value deals with the identification of key drivers of organizational value, while complementarity and techniques for optimization of supermodular functions provide a basis for exploiting any synergy between these value drivers. There are three issues that senior management must consider in managing organizational design changes:

1. Is there any stimulus (internal and/or external), the response to which is a change in organizational design? As an illustration, through the late eighties and early nineties, the oil industry faced increased uncertainty due to environmental and safety regulations, increasing global competition and a weak economy. Disappointing financial performance made Phillips 66 analyze their business and conclude that the key to profitability in the new world would involve cost efficiency (Applegate 1994a, 1994b). Similarly, an aggressive pricing policy by a competitor may force an organization to become more efficient through restructuring its operations. The change need not be the response to an immediate crisis—it could be “anticipatory” in nature, based on a consideration of economic and technological trends (Applegate 1994b).

2. If the answer to question 1 is in the affirmative, what are the drivers of value that we need to improve through the design change? Addressing this question will require the development of a multi-level business value model showing the relationship between critical success factors and their drivers. At the highest level, we have factors which are considered as overall measures of performance (e.g., profitability, return on investment, market growth, etc.). At the lowest level, we have design variables, the values of which are to be determined. Between the design variables and the highest level performance measures, we have an additional layer in the form of intermediate variables (e.g., customer satisfaction, turnaround/response time, coordination levels within and outside an organization, capacity utilization and inventory turnover, etc.). These variables are not financial measures by themselves, but may be key drivers of financial performance. The motivation for having these intermediate variables is twofold. First, demand depends on customers' perception of the quality of products and services. Quality, in turn, is affected by the choice of design variables pertaining to IT and organizational characteristics. Thus, demand is influenced by the design variables pertaining to IT and organizational characteristics. Thus, demand is influenced by the design variables via the quality variable. This leads to a multi-level model specification, which is not a simple hierarchy of accounting identities. Second, individual managers or groups may not be able to assess how their choices of decision variables and performance measures relate to the business unit's payoff. The business value model enables them to analyze such relationships.

The design variables include IT, organizational and business process characteristics, and are chosen by organizational designers to enable the organization to improve measures like customer satisfaction and coordination across activities. If the above step of identifying the value model is ignored, a successful reengineering project on the wrong performance and design variables may not lead to increased payoff for the organization.

3. What specific changes in factors pertaining to decision authority, business processes, incentives and IT should we implement to increase the payoff? By how much and in which direction should these factors change? What is the impact of these changes on the performance measures we chose in 2? To address these questions, we need to understand the complementarity that might exist between variables at different levels in the business value model. The presence of complementarity is addressed by the question: Does the value derived by increasing one factor increase by increasing the other factors in appropriate directions? The most important point here is the coordinated nature of change in multiple factors. While synergy is not a new concept, making design decisions based upon an explicit recognition of the value created through the synergy is clearly a new approach to managing organizational design dynamics.

As we articulated above, there are three design issues involving change: (1) which factors to change, (2) in which directions the change should occur, and (3) the magnitude of change. Our view of reengineering is that of a significant investment in technology and people, which must be justified on the basis of maximum payoff. This is similar to the notion of selecting a project with the maximum net present value in finance theory, except for the fact that we explicitly recognize and model complementarity effects of IT and organizational decision variables on the benefit to the firm. We consider a stylized profit function of a business unit with three arguments, unit operating cost, the size of the customer base, and the reengineering cost. Reengineering costs involve capital and noncapital components. Capital costs will be incurred in acquiring new IT, which will enable improvements in business processes. Non-capital costs involve analysis and redesign of business processes, and retraining of employees in new processes and technologies.

Our purpose in specifying this model is to highlight the concept of complementary changes in a hierarchical set of relationships and to illustrate some techniques of model building to analyze reengineering issues. To support our choice of performance and design variables and complementary relations among the variables, we use anecdotal evidence available in the reengineering literature. The assumptions of the model are general enough to include a broad class of business environments. However, each business unit must consider its specific internal and external environment in developing its own business value model. Thus, we are not developing universal value models which can be used by any organization in their reengineering projects. We also do not make a claim regarding the completeness of the list of performance and choice variables in the model.

The organizational payoff function (see Figure 1.) is denoted by

$$
\begin{array}{r l} \Pi & = p d (f, g) - o (a, b, h, v, r, s, q, e, c, t) d (f, g) \\ & \quad - K _ {1} (a, b, h, v, r, c) - K _ {2} (s, q, e, t) \end{array}
$$

with the following notation:

p: unit price or service fee.

$K_{1}(a, b, h, v, r, c)$ : capital cost.

a: level of intraprocess information sharing. It involves access to workgroup database servers, local area networks, and systems integration at the process level. Such access will be required on a regular basis for routine transactions.

b: level of access to information sources external to a process. This type of access will be required to handle exception cases.

h: functionality and user-friendliness of interface design.

v: functionality of decision aids available to a decision maker.

Figure 1 A Business Value Model of Reengineering  
![](/api/attachments/XNBHXR6R/fulltext/images/1c476ef581aa5828737dcab7052634291c04028fa2bf45c551178bbabc608f8a.jpg)

r: level of computer-based performance monitoring for routine transactions.

c: extent to which applications help identify and record employee contribution to helping customers. The design of incentive systems are contingent on the availability of such information. For example, if an employee in engineering provides a piece of information which helps a service representative solve a customer's problem, and if the actions are recorded in the system, both the employees can be rewarded for their respective contributions.

$K_{2}(s, q, e, t)$ : noncapital cost of reengineering.

s: transaction simplicity.

q: level of integration in business processes.

e: scope of decision authority.

t: number of tasks performed by an employee. $d(f(s, q, t, a, r), g(b, h, v, e, c))$ : size of customer base. $f(s, q, t, a, r)$ : quality of routine transactions. $g(b, h, v, e, c)$ : quality of handling exception cases. $o(a, b, h, v, r, s, q, e, c, t)$ : unit operating cost.

## 3.1. Selection of Performance Variables

Reducing operating cost has been an important issue for many reengineering projects. Increased competition and globalization of markets are forcing organizations to adopt cost cutting measures. For instance, through reengineering, IBM Credit Corp (an IBM subsidiary) was able to significantly reduce the processing time of a credit card application, along with a major reduction in the number of employees (Hammer and Champy 1993). The reduced cost of operation can have a major impact on profitability in a highly competitive business. Phillips 66 is another example where management sought to increase profitability through improved cost efficiency (Applegate 1994a, 1994b). A second variable which may be a key determinant of profitability is the size of the customer base (or its growth rate). In the financial service sector (e.g., credit card business), market growth (or lack thereof) is often considered critical to success (Harrar 1994). The case of Frito Lay also illustrates the importance of the market growth variable. In the 1980s, Frito Lay determined that in order to succeed in a saturating market with increasingly aggressive competitors, it must achieve sustained growth (Applegate 1992, 1994b).

Service has been an important factor for customer loyalty, and satisfying customers with timely and high quality service is critical to the success of a service oriented business. Reengineering experts unanimously agree that customer processes (e.g., customer service, order fulfillment, sales, etc.) are some of the key target areas for reengineering (e.g., Davenport 1993). For example, facing aggressive competition, GTE decided that it had to offer highly improved customer service (Stewart 1993). Finally, companies spend hundreds of millions of dollars on reengineering projects involving extensive redesign of processes, employee retraining and new IT acquisition. Thus, this cost must be weighed against the benefits that the project might bring.

Intermediate performance variables in our business value model are the quality of routine transactions and exception cases, and the capital and noncapital costs of reengineering. These variables were selected from a review of the business literature on reengineering in the manufacturing and financial service sector (references provided throughout this section).

## 3.2. Reengineering (Choice) Variables

The high level performance variables are affected by reengineering or choice variables through a set of intermediate target variables. The choice variables pertain to IT, business processes, organizational structure and incentive systems. Note that all the variables are defined as levels or characteristics. For example, instead of using client/server or mainframe computing as realizations of the technology variable, levels of information sharing, user-friendliness, etc. are used. Next we state and justify certain complementarity related assumptions of the above model. They enable us to derive qualitative implications regarding the nature of technological and organizational changes that should be implemented in a reengineering project.

## 3.3. Model Assumptions and Rationale

ASSUMPTION 1. The capital cost function $K_{1}(a, b, h, v, r, c)$ is increasing and submodular in its arguments.

More often than not, reengineering is accompanied by heavy investments in IT. While fast and seamless information flow is critical for the success of the reengineered organization, the cost of providing seamless access to relevant information will be generally high. For example, in the course of its reengineering project, Aetna had to consolidate two large and incompatible systems which serviced separate lines of business (Rifkin 1993). The systems used different codes and interfaces, and making them work together turned out to be costly and difficult. Since this represents a familiar computing scenario, we can justify that increasing the level of access to information and the user-friendliness of the interface increases the IT investment. The development of decision aids such as decision support or expert systems also requires significant investments. Similar arguments apply to electronic monitoring and applications which help identify actions taken by employees and their outcomes.

While the capital cost increases with an improvement in information access, user-friendliness, etc., we suggest that an additional investment in a technology characteristic reduces the marginal investment required to improve other characteristics. We use a pairwise comparison of the arguments of the capital cost function to justify its submodular nature (see Topkis 1978 for the mathematical foundation for such pairwise comparison). The marginal cost of developing distributed information repositories (which will enhance access to both internal and external information) will be lowered when there is a parallel development of powerful, user-friendly client application interfaces, which can mask the location of the servers on a network. For example, in integrating two isolated and incompatible systems, Aetna provided its employees with a PC graphical user interface (GUI), whereby the users could invoke a variety of applications such as operations, payment, time and expense, email, word processing, spreadsheet, communications, and medical references from a single front-end tool (Rifkin 1993). Without such front-end development, the company would have to invest a large amount of money in merging the two systems on a common hardware and operating system platforms with a single networking standard to achieve a desired level of access to information.

INFORMATION SYSTEMS RESEARCH
Vol. 7, No. 4, December 1996

Along similar lines, implementing a seamless architecture of distributed database servers (based on open systems or widely recognized standards) will reduce the need for developing complex client-side requesters and middleware products. Hence the submodularity between the investment in information repositories (the server side) and that in user-friendly interfaces (the client side). The submodularity between the costs of providing access to internal and external sources of information can be attributed to common infrastructure requirements. A network infrastructure developed for sharing information within a business process also helps reduce the marginal investment for access to sources of information external to the process. While the latter may have additional complexity such as wide area connectivity, and potentially more heterogeneity of networking standards, it also requires the same infrastructure (e.g., local area networks, network operating systems, and internet-working devices such as bridges, routers and gateways) as that of intra-process information sharing.

ASSUMPTION 2. The noncapital cost of reengineering $K_{2}(s, q, e, t)$ is increasing and submodular in its arguments.

Reengineering projects are usually characterized by heavy investments in retraining and reskilling employees. Integrating business processes, empowering employees by increasing the scope of their decision authority, and making them handle multiple roles with the help of IT applications require substantial retraining programs and long periods of adjustment. For example, GTE embarked on a major retraining project where repair clerks, who previously filled out “trouble tickets” for customers, started playing the role of “front-end technicians” with testing and switching equipment (Stewart 1993). Customer service personnel at AT&T Universal Card Services had to attend intensive retraining programs in order to learn new desktop technologies (Harrar 1994). Along similar lines, when Aetna’s reengineering effort resulted in the consolidation of eight claim centers into one, 225 customer service representatives, who were brought to work in the consolidated facility, had been using different applications at various centers (Rifkin 1993). Clearly, process integration and consolidation is a costly commitment in terms of training for both redesigned business processes and new IT.

While the cost increases with each reengineering variable, it is cost efficient to increase all the variables at the same time. For example, the cost of retraining newly empowered employees will increase at a slower rate when the business processes are made simpler. Similarly, although the cost of redesigning business processes increases as the organizational designer attempts to integrate isolated processes, the cost will increase at a slower rate as the designer also spends effort on simplifying each sub-process.

ASSUMPTION 3. The size of the customer base $d(f, g)$ is increasing and supermodular in f (quality of routine transactions) and g (quality of handling exception cases).

For routine transactions, quality is embodied in the accuracy and the speed with which the transactions are completed. For example, Bell Atlantic reduced the time to connect customers to long distance carriers from up to 16 days to a few hours, and started winning back market share (Stewart 1993). For exception cases, however, quality stands for how satisfactorily a customer's problem or complaint is mitigated/addressed. As an illustration, GTE measures its performance with respect to customer problems as the percentage of problems that are fixed with one call, and not by how fast the call is handled (Stewart 1993).

The supermodularity of the customer base in f and g implies that the effect of increasing the speed of routine transactions on the size of customer base will be more significant if it is matched by a high quality of service when exception situations arise. However, exception handling requires the satisfactory resolution of a problem, which is likely to take more time than a routine transaction. This assumption implies that an organization which can handle both routine and exception cases efficiently is likely to have a large customer base (for a given price). Indeed, the reengineering effort at AT&T Universal Card Services focused on both routine and exception transaction handling (Harrar 1994).

ASSUMPTION 4. The quality of routine transactions $f(s, q, t, a, r)$ is increasing and supermodular in its arguments.

The need for simple and integrated business processes is typified by the situation faced by GTE. As Stewart (1993) summarized: "GTE customers wanted one-stop shopping: One number to fix an erratic dial tone, question a bill, sign up for call waiting, or all three, any time of the day." This called for simplifying and integrating unnecessarily complex and disjoint processes.

Manganelli (1993) provides an example where reengineering helped a manufacturer increase the accuracy of its order fulfillment process by 100%. The process originally involved 83 cumbersome steps and was streamlined into 23 value added steps. This led to a major improvement in customer satisfaction within one year. Along similar lines, Hammer and Champy (1993) describe the reengineering of IBM Credit Corp's operations. For credit authorization, 14 employees would perform a variety of separate activities which took between six and fourteen days, with a high risk of losing a customer to a competitor. Senior managers at IBM Credit found out that the whole process actually took only 90 minutes, and that the delay was primarily due to queuing at each person's desk. They also found that each subtask was quite simple, and that a properly trained person could manage the entire process with the help of IT applications. The complexity of intrinsically simple processes can be unnecessarily high, as exemplified by Ford's accounts payable function, which employed 500 people as compared to Mazda's headcount of five (Hammer and Champy 1993).

These examples highlight that successful BPR will eliminate redundant processing, unnecessary management and supervisory roles (Jeffery 1994). Jeffery also observes that “decision making tends to be pushed down to front-line staff at lower organizational levels as management layers, supervisory functions, and administrative staffing are cut. Chains of command are shortened, and fewer actions require approval from higher management levels.” As a result, an employee in a reengineered organization will be expected to perform multiple tasks.

As an enabler of process simplification and integration, IT also plays a major role in increasing the quality of routine transactions. For example, GTE developed software applications which allow service representatives to handle any customer request (Stewart 1993). Aetna built a Windows-based PC front-end application that enables customer service representatives "to handle a loss report, make a payment access to a database on the mainframes simply by clicking on an icon" (Rifkin, 1993). It has helped Aetna consolidate 65 claim centers into 22 regional centers, with expected savings of \$100 million. As an example of improved access to information leading to faster routine transactions, Rifkin (1993) reports that health care claims mailed to Aetna would sit without being processed for days or weeks. Aetna used image processing technology to digitally scan the claim, so that any representative or claim processor could get immediate access to this information. This investment led to a major reduction in repeat calls from customers. Electronic monitoring is expected to reduce the amount of supervisory intervention, and hence reduce overall response time. For example, AT&T Universal Card Services invested in electronic monitoring of customer representatives to ensure efficiency, accuracy and courtesy in handling customers (Harrar 1994).

The supermodularity between the IT and process variables is best studied through the following examples. AT&T Universal Card Services “empowered” its representatives, but initially did not give them the IT they needed to handle customer requests (Harrar, 1994). The dumb terminals the representatives had to work with could not integrate information from multiple mainframes; a representative had to shift from screen to screen, and had to recall or look up access codes for different computers while being on the phone with a customer. Even a simple activity like changing a customer’s address required manual inputs to three separate databases (Harrar, 1994).

Jeffery (1994) highlights the synergy between process redesign and support IT applications: "While staff is cut, one person may handle tasks which were previously handled by two or three. Applications must reflect these changes quickly. Decision makers in a reengineered organization are notoriously intolerant when told that while they are changing business processes, it will be two or three years before applications are available to support these changes." Users need access to much more information in a reengineered organization than in a traditional business environment.

ASSUMPTION 5. The quality of handling exception cases $g(b, h, v, e, c)$ is increasing and supermodular in its arguments.

Exception handling is exemplified by "The Power of One" award at AT&T Universal Card Service, which is given to employees for demonstrating exceptional commitment to helping the customer. Harrar (1994) describes how one AT&T Universal representative went out of his way to help a customer who had lost his wallet (and hence his card and money) at an airport. Such actions require motivation (provided by the identification of and the reward for the contribution) and expanded scope of decision authority. Additionally, it is vital to have access to information outside the customer service process (and possibly outside the business unit itself), user-friendly application interfaces which provide employees easy access to diverse information resources, and decision aids which help in making more accurate decisions.

The complementarity between the scope of decision authority and reward systems is evident from the fact that neither one is enough in isolation to ensure a high quality of handling exception situations. For example, motivated employees (a result of identifying and rewarding contribution) will still find it difficult to accomplish their task in the absence of appropriate IT support. Similarly, providing faster access to external information sources (which are frequently required for handling exception cases) will increase the transaction quality much more when it is also accompanied by an expanded scope of decision authority (with fewer vertical decisions involving supervisory approvals).

The IT variables themselves are supermodular. For example, while decision aids and user-friendliness of applications are both expected to help solve complex problems faster, the effectiveness of decision aids is expected to increase with a user-friendly interface that provides a high level of functionality relating to the decision problem of interest, and vice versa. Similarly, information access will be easier and faster if the level of information sharing enabled by distributed database technologies is augmented by powerful front-end applications, and vice versa.

Based on several case studies, Applegate (1994b) describes the joint impact of changing the decision authority and information sharing capabilities on the roles of line employees and supervisors: “. . . the roles of line employees and their direct supervisors also changed. As members of interfunctional work teams, they became actively involved in defining and managing the tasks needed to execute day-to-day operations. They managed relationships with customers and had the authority, accountability and information necessary to ensure that customer needs were identified and met." Applegate (1994b) also describes the interplay between IT design and employee incentives: "In addition to its role in expanding information processing capacity, the information infrastructure also played a key role in enabling development of complex, interlocking authority and incentive systems."

ASSUMPTION 6. The unit operating cost $o(a, b, h, v, r, s, q, e, c, t)$ is decreasing and submodular in its arguments.

Operating cost includes direct employee compensation, materials, supplies and services, and overheads (indirect costs) such as supervisors, inspectors, land and building. While some of the indirect elements of operating cost (e.g., supervisory compensation) may not vary proportionately with demand, they may not be completely fixed either. For example, the required number of supervisors may increase when the demand exceeds a certain threshold. In other words, these elements may be semi-variable, i.e., fixed only within specific ranges of demand. Accordingly, we consider unit operating cost in our analysis. $^{2}$

Jeffery (1994) notes that process simplification and integration cut overheads and supervisory positions, and speeds up transaction processing. The cycle time to deliver a product or service is reduced because fewer stages are handled more efficiently. Margulis (1994) suggests that 85% of Fortune 1000 organizations have downsized their white-collar workforce in recent times, and that the key underlying reason appears to be overhead reduction. Since salaries and benefits are a significant portion of administrative costs (up to 80%, Margulis, 1994), running a business with a smaller workforce appears to be a natural way to reduce both direct and indirect employee costs.

However, the joint impact of redesigning IT and business processes on the unit operating cost is more favorable than simply streamlining operations or empowering employees, as seen earlier in the case of AT&T Universal Card Services. Of course, there is cost submodularity between the organizational variables such as the level of empowerment and process simplicity. Simpler processes enable an employee to perform many tasks and roles, when the scope of decision authority is also increased, leading to a reduction in the unit operating cost.

ASSUMPTION 7. The customer base d and the “degree of supermodularity” of f and g satisfy conditions stated in Lemma 1 in the appendix.

This assumption ensures that the customer base is supermodular in the IT and process related reengineering variables. The conditions imply that if the customer demand is increasing and concave in the quality of routine and exception transactions, then the functions f and g have to be “strongly supermodular” to ensure the supermodularity of the customer base in the reengineering variables. Note that Lemma 1 deals with purely discrete functions, without any assumptions of continuity. For the sake of comparison, the discussion of the Lemma in the appendix provides the corresponding requirements for continuous and differentiable functions.

## 3.4. Impact of Choice Variables on Payoff

To illustrate the importance of choosing all the reengineering variables in a coordinated manner, we first show that the profit function is supermodular in the reengineering variables. Further, for the sake of generality, instead of referring to the ten specific decision variables in the above model, we state all propositions in terms of a vector of decision variables, z. Further, two nonoverlapping subsets of z (whose union is z) are denoted by x and y. Similarly, two other subsets with the same property are referred to as u and w. $^{3}$

PROPOSITION 1. Let $\Pi = [p - o(z)]d(f(x), g(y)) - K_1(u) - K_2(w)$ , where $x \in X$ ( $X$ is a sublattice of $R^n$ ), $y \in Y$ ( $Y$ is a sublattice of $R^{m}$ ), $z \in Z$ (where $z = (x_1, \ldots, x_{n}, y_1, \ldots, y_{m})$ ), whereby $Z$ is a sublattice of $R^{n+1m}$ . $u \subset z$ , $w \subset z$ (i.e., $u$ and $w$ represent subsets of the variables $x_1, \ldots, x_n, y_1, \ldots, y_{m}$ ). Further, $u \cap w = \emptyset$ (empty set), and $u \cup w = z$ . Let $p$ ( $a$ constant) $\geq o(z)$ for all $z \in Z$ . $o(z)$ is decreasing and submodular in $z$ . $d(f(x), g(y)), f(x)$ and $g(y)$ follow the definitions in Lemma 1. $K_1$ and $K_2$ are increasing and submodular in $u$ and $w$ respectively. Then $\Pi$ is supermodular in $z$ .

The proof of this and other propositions are provided in the appendix. Proposition 1 supports the “radical change” view, which we interpret as changes in several related variables in tandem. $^{4}$ The proposition implies that the net payoff to the business unit increases more when the levels of all the complementary design variables are chosen together than when they are selected in isolation. There are several cases in the literature which describe how problems surfaced when isolated changes were implemented without an overall vision. As with the case of empowered employees of Universal Card Services with dumb terminals, Frito Lay’s attempt to decentralize decision making authority initially failed due to the lack of parallel improvements in the IT infrastructure (Applegate 1994b).

The above model and Proposition 1 were developed under the assumption that all factors can be changed in the course of a reengineering project. How is a firm's design problem affected when one or more of these factors is (are) not changed due to a variety of organizational reasons? A related but distinct issue is the impact of pre-existing organizational conditions (e.g., heterogeneity of computing platforms and standards, employee computing skills, resistance to change, etc.) which may complement or hinder proposed changes.

## 3.5. Reengineering Decisions When All Design Variables Are Not Changed Together

As we have argued earlier, successful reengineering effort which maximizes bottom-line payoff requires top management vision in recognizing key design variables. If such decisions are left to managers within individual and isolated units, they may not be able to envision the complementarity that possibly exists between variables within and outside their domain. For example, a commonly encountered problem in reengineering appears to be the lack of understanding on the part of IS regarding business processes and user needs (Manganelli 1993, Monteleone 1994). Manganelli (1993) argues that a CIO often perceives his/her main challenge as staying within the IS budget. Not surprisingly, in a national survey conducted by Gateway Consulting, the CIOs' top priority was cost, rather than flexibility, service, availability and user satisfaction. By solely focusing on cost, many CIOs transform a reengineering project into a cost reduction effort (Manganelli 1993). However, along with cost reduction, reengineering must also focus on several critical criteria such as quality and customer base, which may require more drastic and creative IT changes. Monteleone (1994) indicates that IS managers often say they are too busy reengineering their internal IS processes, and that they do not have enough resources to work on business process reengineering. Such an isolated effort goes against the complementary relationship between IT and non-IT reengineering variables, and is likely to result in low performance improvements.

Sometimes, it may also be the case that individual managers are reluctant to change certain variables because it will affect themselves or their departments in a negative fashion, even though it could be in the best interest of the organization. Martinez (1995) provides the example of an insurance company where the claims investigation process was being reengineered. The claims investigation functions of several insurance lines would be consolidated into a single unit for better efficiency. Being threatened by possibility of job loss, claims managers “forcefully argued that their fiscal responsibility required that all suspect claims be investigated,” thereby hoping to maintain status quo. The reluctance on part of a manager (either due to lack of vision or self-interest) to change the level of a given set of variables reduces the optimal levels of other variables, as seen in Proposition 2.

PROPOSITION 2.5 Let $\Pi(z)$ be supermodular in $z\in Z$ (as in Proposition 1), where $Z$ is a sublattice of $R^{n+m}$ . Let $Z^{*}$ denote the set of maximizers for $\Pi$ . Assume that $Z^{*}$ is nonempty. Let the $i$ th element of $z$ be constrained to the value $z_{i}^{\prime}$ . Further, let $z_{i}^{\prime}\leq inf z_{i}^{*}$ , where $z_{i}^{*}$ is the $i$ th element of $z^{*}\in Z^{*}$ . Let the nonempty set of maximizers of $\Pi$ with $z_{i}=z_{i}^{\prime}$ be denoted by $Z^{\prime}$ . Then $Z^{\prime}\leq Z^{*}$ in the sense that for any $z^{\prime}\in Z^{\prime}$ and $z^{*}\in Z^{*},z^{*}\vee z^{\prime}\in Z^{*}$ , and $z^{*}\wedge z^{\prime}\in Z^{\prime}$ .

The proposition shows that the optimal levels of the other variables may become smaller due to their complementarity with the variable which is left unchanged at or constrained to a level which is less than its minimum optimal level in the unconstrained maximization problem.

Martinez (1995) describes the reengineering effort in a service organization which failed to give IS a prominent role in the process of reengineering. As a result, frustrated IS managers did not engage themselves in developing aggressive and challenging plans, and went on preserving status quo. Note that this situation described by Martinez (1995) is in contrast to the scenarios depicted by Manganelli (1993) and Monteleoni (1994), where IS failed to see the complementarity between variables in their domain and those in other areas. Unfortunately, both cases lead to the undesirable outcome of leaving out key variables from the reengineering effort, and slow down the overall change.

## 3.6. Reengineering Decisions and Pre-existing Organizational Conditions

At any time, different organizations may be in different stages of computing. For instance, many organizations have large installed bases of "legacy" systems and a large number of disjoint networks and applications. Under such circumstances, migrating to a more flexible computing platform is not easy, as succinctly described (for the situation at Aetna) by Rifkin (1993): "Aetna's technology vision is clouded by both technical and cultural obstacles that prohibit rapid change. The company, for example, has a huge capital investment in mainframe-based computing. Fifteen IBM behemoths are at work in Aetna's two main data centers in Connecticut. Though Aetna has tens of thousands of PCs and is committed to a client/server strategy of its own, Aetna's management has concluded that it cannot simply scrap its mainframes. Therefore, new projects require massive adaptation of new PC-based hardware and software into the old mainframe mentality. Not surprisingly, with such heavy baggage, many of the reengineering projects are ramping up slowly."

To add to the problems of this large installed base, as of 1989, Aetna had 19 different email systems, more than 100 word processing packages, 80 different spreadsheets, 36 communication networks, and numerous brands of PCs (Rifkin 1993). Such heterogeneity (a pre-existing condition) clearly increases the cost of providing a given level of information access in a user-friendly way. In Proposition 3, we show that these pre-existing conditions may be detrimental to the overall reengineering effort.

PROPOSITION 3. Let $Z$ and $\Psi$ be sublattices of $R^{n+m}$ and $R^1$ , respectively. Consider the function $\Pi = pd(z) - o(z, \psi)d(z) - C(z, \psi)$ , where $z \in Z$ , $\psi$ (a parameter vector) $\in \Psi$ , and $p$ (a constant) $\geq c(z, \psi)$ for all $(z, \psi)$ . $d(z)$ is increasing and supermodular in $z$ . $o(z, \psi)$ is decreasing and submodular in $(z, \psi)$ . $C(z, \psi)$ is submodular in $(z, \psi)$ . Let $Z^*$ and $Z^{**}$ denote the sets of maximizers of $\Pi$ for $\psi = \psi'$ and $\psi''$ respectively (with $\psi' > \psi''$ ). Assume that both $Z^*$ and $Z^{**}$ are nonempty. Then $Z^{**} \leq Z^*$ .

Several points should be noted about the proposition. First, a pre-existing condition (denoted by the vector $\psi$ ) affects the operating and capital costs (and therefore appears in those functions as a parameter), $^{6}$ but does not enter the demand function directly. For example, a customer is unlikely to care if a company has many different computing platforms or networking standards. But s/he cares about the quality of product/service, which in turn are determined by the reengineering variables like level of information access. When the computing infrastructure of the company is fragmented, it will cost more to provide a high level of information access. If this cost is excessive, management may have to settle for a lower level of information access, which will then have a negative impact on demand via the quality of service.

Second, we do not imply that the pre-existing conditions should not be changed. In fact, that would go against the very notion of complementarity. We only suggest that unfavorable pre-existing conditions will increase the cost of achieving given levels of the reengineering variables, and may therefore reduce their optimal levels in the payoff maximization problem. Third, there is a key difference between the scenarios in §§3.5 and 3.6. In §3.5, we analyzed a situation where a decision variable, which is complementary with other variables, is not changed during the reengineering project, due to either self-interest or myopic vision of individual managers or groups. In such a setting, the organization cannot obtain the maximum benefit that reengineering can offer by exploiting complementary relationships, since the optimal levels of the other variables may get reduced. However, the situation depicted in §3.6 indicates that coordinated changes of smaller magnitude may be a rational response from senior management for an organization with “unfavorable” existing conditions. It is important that such conditions are carefully assessed and taken into consideration in deciding the magnitude of change.

## 4. Future Research and Conclusion

We showed that the recommendation of radical change (when interpreted as coordinated changes in a set of design variables) is supported by the theory of complementarity. However, the optimal magnitudes of such changes cannot be uniform across organizations. For example, we showed that unfavorable pre-existing organizational conditions may render changes of large magnitude economically infeasible. We also established that when some complementarity variables are left out of the reengineering exercise either due to myopic vision or self-interest, the optimal levels of the other variables will become smaller, to the detriment of the organization. This result provides a complementarity theoretic foundation for the need for top management vision and involvement in reengineering projects.

We believe that our business value complementarity approach can be applied to analyze why many organizations are engaging in “evolutionary” or incremental changes. $^{7}$ Is it the lack of senior management vision or unfavorable pre-existing conditions that is prompting these organizations to adopt such a strategy? While we briefly addressed both issues in the paper, these topics deserve much more detailed analysis, especially from the standpoint of budget limitations for any given period. A key attendant question to be addressed is whether an evolutionary approach can work where changes are taking place incrementally, but in the right directions in a complementary manner.

A related but distinct problem involves the selection of appropriate IT platforms. Since advances in technology occur on a continual basis, the option of future investments must be considered in the analysis of current IT acquisition plans. Selecting a technology today may create or destroy complementary options of investing in future technologies. For example, investing in features such as open standards, flexible architectures, and transparent information access may enable an organization's IT platform to easily integrate with future technologies. This notion of creating (or destroying) complementary options through the choice of current technologies will also be taken up in future research.

The theoretical approach, the model assumptions and implications presented in the paper can lend themselves to empirical testing. However, it will be a challenge to find appropriate functional forms which will allow the testing of supermodularity without a priori restrictions. While considerable empirical investigation is required in this area, we have presented a clear basis for managing reengineering and IT investments in a manner which will help enhance organizational payoff. $^{8}$

$^{8}$ We are indebted to Professors Lynda Applegate, Aimo Hinkkanen, and Preston R. MacAfee for many helpful insights and suggestions. We are also grateful to the Associate Editor, anonymous reviewers, and Professor John L. King for helpful comments and suggestions. An earlier version of this paper was presented at the 1994 Workshop on Information Systems and Economics, Vancouver, Canada. The authors have greatly benefited from the input provided by the workshop participants

## Appendix.

## Mathematical Derivations

LEMMA 1 Let $f(x)$ and $g(y)$ be monotone increasing real-valued functions of $x$ and $y$ , respectively, where $x \in X$ and $y \in Y$ , and where $X$ and $Y$ are sublattices of $R''$ and $R'''$ , respectively. Let $f(x)$ and $g(y)$ be "strongly"

supermodular in $x$ and $y$ in the following sense. There is a $\delta_1 > 0$ such that for any $x', x'' \in X$ ,

$$
\begin{array}{r l} & f (x ^ {\prime} \vee x ^ {\prime \prime}) + f (x ^ {\prime} \wedge x ^ {\prime \prime}) - f (x ^ {\prime}) - f (x ^ {\prime \prime}) \\ & = \delta_ {1} (f (x ^ {\prime}) - f (x ^ {\prime} \wedge x ^ {\prime \prime})) (f (x ^ {\prime \prime}) - f (x ^ {\prime} \wedge x ^ {\prime \prime})) \end{array}\tag{5}
$$

Similarly there is a $\delta_{2} > 0$ such that for any $y', y'' \in Y$ ,

$$
\begin{array}{l} g (y ^ {\prime} \vee y ^ {\prime \prime}) + g (y ^ {\prime} \wedge y ^ {\prime \prime}) - g (y ^ {\prime}) - g (y ^ {\prime \prime}) \\ \geq \delta_ {2} (g (y ^ {\prime}) - g (y ^ {\prime} \wedge y ^ {\prime \prime})) (g (y ^ {\prime \prime}) - g (y ^ {\prime} \wedge y ^ {\prime \prime})). \end{array}\tag{6}
$$

Let the ranges of $f(x)$ and $g(y)$ be contained in $\Theta \subseteq R^1$ and $\Phi \subseteq R^1$ . Let $d(\theta, \phi)$ be a real-valued function which is monotone increasing and supermodular in $\theta \in \Theta$ and $\phi \in \Phi$ . Further, for any $\phi, d$ satisfies

$$
d (\theta_ {1}, \phi) + d (\theta_ {1}, \phi) - d (\theta_ {3}, \phi) - d (\theta_ {2}, \phi) \geq 0,\tag{7}
$$

whenever $\theta_{1} \leq \theta_{2} \leq \theta_{4}, \theta_{1} \leq \theta_{3} \leq \theta_{4}$ , and $\theta_{4} + \theta_{1} - \theta_{2} - \theta_{3} \geq \delta_{1}(\theta_{2} - \theta_{1})(\theta_{3} - \theta_{1})$ Similarly for any $\theta, d$ satisfies

$$
d (\theta , \phi_ {4}) + d (\theta , \phi_ {1}) - d (\theta , \phi_ {2}) - d (\theta , \phi_ {3}) \geq 0,\tag{8}
$$

whenever $\phi_1 \leq \phi_2 \leq \phi_4, \phi_1 \leq \phi_3 \leq \phi_4$ , and $\phi_4 + \phi_1 - \phi_2 - \phi_3 \geq \delta_2(\phi_2 - \phi_1)(\phi_3 - \phi_1)$ . Then $d$ is supermodular in $x, y$ , and jointly supermodular in $x$ and $y$

PROOF OF LEMMA 1 For any $x', x'' \in X$ , let $f(x' \vee x'') = \overline{\theta}$ , $f(x' \wedge x'') = \underline{\theta}$ , $f(x') = \theta'$ and $f(x'') = \theta''$ . Note that $\underline{\theta} \leq \theta' \leq \overline{\theta}$ , and that $\underline{\theta} \leq \theta'' \leq \overline{\theta}$ . Thus, for any given $\phi \in \Phi$ , if $f$ is strongly supermodular in $x$ (as in Condition (5)) such that $\overline{\theta} + \underline{\theta} - \theta' - \theta'' \geq \delta_1(\theta' - \underline{\theta})(\theta'' - \underline{\theta})$ , then according to Condition (7). $d$ is supermodular in $x$

To show that $d$ is also supermodular in $y$ , let $g(y' \vee y'') = \bar{\phi}$ , $g(y' \wedge y'') = \phi$ , $g(y') = \phi'$ and $g(y'') = \phi''$ . For any $\theta \in \Theta$ , if $g$ is strongly supermodular in the sense of Condition (6), then from Condition (8), $d$ is also supermodular in $y$

To show that $d$ is jointly supermodular in $x$ and $y$ , we apply the supermodularity of $d$ to the points $(\underline{\theta}, \phi')$ and $(\theta'', \underline{\phi})$ to obtain:

$$
d (\theta^ {\prime \prime}, \phi^ {\prime}) + d (\underline {{\theta}}, \underline {{\phi}}) \geq d (\underline {{\theta}}, \phi^ {\prime}) + d (\theta^ {\prime \prime}, \underline {{\phi}})\tag{9}
$$

Similarly, applying the supermodularity of $d$ to the points $(\overline{\theta}, \phi')$ and $(\theta'', \overline{\phi})$ , we have

$$
d (\bar {\theta}, \bar {\phi}) + d (\theta^ {\prime \prime}, \phi^ {\prime}) \geq d (\bar {\theta}, \phi^ {\prime}) + d (\theta^ {\prime \prime}, \bar {\phi}).\tag{10}
$$

Adding (9) and (10), subtracting $p(\theta', \phi') + p(\theta'', \phi'')$ on both sides, and arranging terms, we have

$$
\begin{array}{l} d (\bar {\theta}, \bar {\phi}) + d (\underline {{\theta}}, \underline {{\phi}}) - d (\theta^ {\prime}, \phi^ {\prime}) - d (\theta^ {\prime \prime}, \phi^ {\prime \prime}) \\ \geq [ d (\bar {\theta}, \phi^ {\prime}) + d (\underline {{\theta}}, \phi^ {\prime}) - d (\theta^ {\prime}, \phi^ {\prime}) - d (\theta^ {\prime \prime}, \phi^ {\prime}) ] \\ + [ d (\theta^ {\prime \prime}, \bar {\phi}) + d (\theta^ {\prime \prime}, \underline {{\phi}}) - d (\theta^ {\prime \prime}, \phi^ {\prime}) - d (\theta^ {\prime \prime}, \phi^ {\prime \prime}) ]. \end{array}\tag{11}
$$

The expression within the first set of square brackets on the right-hand side of (11) is positive from the conditions for d being supermodular in x. Similarly, the expression within the second set of square brackets is also positive from the supermodularity of d in y. Hence we have

$$
\begin{array}{l} d (f (x ^ {\prime} \vee x ^ {\prime \prime}), g (y ^ {\prime} \vee y ^ {\prime \prime})) + d (f (x ^ {\prime} \wedge x ^ {\prime \prime}), g (y ^ {\prime} \wedge y ^ {\prime \prime})) \\ \geq d (f (x ^ {\prime}), g (y ^ {\prime})) + d (f (x ^ {\prime \prime}), g (y ^ {\prime \prime})) \quad \text {Q.E D} \end{array}\tag{12}
$$

## Discussion of Lemma 1

For a pair of functions d and f, such that if d satisfies a condition that still is satisfied by some concave functions, and if f is strongly supermodular in a suitable sense, then the composite function $d(f(x))$ is supermodular in x. The condition on d is obtained by taking a condition that characterizes convex functions and restricting it so that a certain expression is required to be positive only under more limited circumstances than for convex functions. It implies that the new condition will also be satisfied by some functions that are not convex. This is important for demand functions which are more likely to be concave than convex in quality related variables. Later we provide some examples of concave functions which satisfy Lemma 1

A useful observation is that if $f$ and $g$ are strongly supermodular, if $d(\theta, \phi)$ is supermodular in $(\theta, \phi)$ , and if, for each $\phi$ , $d(f(x), \phi)$ is supermodular in $x$ , and if, for each $\theta$ , $d(\theta, g(y))$ is supermodular in $y$ , then $d(f(x), g(y))$ is supermodular in $(x, y)$ . This reduces the problem of composite functions to finding conditions that guarantee that $d(f(x))$ is supermodular in $x$ (suppressing $\phi$ in the notation)

The conditions of Lemma 1 should also be necessary in the following precise sense: If $d$ is given, and if $\delta_{1}$ is taken to be the smallest number that works for $d$ , then one can find, for each $\delta_{1}^{\prime}<\delta_{1}$ , a supermodular function $f$ satisfying

$$
\begin{array}{l} f (x ^ {\prime} \vee x ^ {\prime \prime}) + f (x ^ {\prime} \wedge x ^ {\prime \prime}) - f (x ^ {\prime}) - f (x ^ {\prime \prime}) \\ \geq \delta_ {1} ^ {\prime} (f (x ^ {\prime}) - f (x ^ {\prime} \wedge x ^ {\prime \prime})) (f (x ^ {\prime \prime}) - f (x ^ {\prime} \wedge x ^ {\prime \prime})), \end{array}
$$

such that $d(f(x))$ is not supermodular in $x$

Having provided conditions for the supermodularity of $d$ in $(x, y)$ for any lattice, let us derive similar conditions for continuous functions for the sake of comparison. Starting with a function defined on discrete lattice points, we can bring adjacent points sufficiently close to each other, whereby the above analysis can be redone in terms of continuous and differentiable functions. Let $d(\theta, \phi)$ be continuous, increasing, and twice differentiable in $\theta$ and $\phi$ , and where $\theta = f(x_1, \ldots, x_n)$ and $\phi = g(y_1, \ldots, y_m)$ . Define a function $\xi$ such that

$$
d (f (x _ {1}, \dots , x _ {n}), g (y _ {1}, \dots , y _ {m})) = \xi (x _ {1}, \dots , x _ {n}, y _ {1}, \dots , y _ {m})
$$

Differentiating $\xi$ with respect to $x_{i}$ , we have

$$
\frac {\partial \xi}{\partial x _ {i}} = \frac {\partial d}{\partial \theta} \frac {\partial f}{\partial x _ {i}}\tag{13}
$$

Differentiating again with respect to $x_{i} (i \neq j)$ , we have

$$
\frac {\partial^ {2} \xi}{\partial x _ {i} \partial x _ {j}} = \frac {\partial^ {2} d}{\partial \theta^ {2}} \frac {\partial f}{\partial x _ {i}} \frac {\partial f}{\partial x _ {j}} + \frac {\partial d}{\partial \theta} \frac {\partial^ {2} f}{\partial x _ {i} \partial x _ {j}}\tag{14}
$$

We are specially interested in the case where $\xi$ is increasing and concave in x and y, and would like to derive conditions for $\xi$ to be supermodular in x and y. For $\xi$ to be supermodular in x, we must have the right-hand side of Equation (14) $\geq 0$ . Let $\delta_{i} > 0$ be such that

$$
\frac {\partial^ {2} d}{\partial \theta^ {2}} / \frac {\partial d}{\partial \theta} \geq - \delta_ {1} \geq - \frac {\partial^ {2} f}{\partial x _ {i} \partial x _ {i}} / \frac {\partial f}{\partial x _ {i}} \frac {\partial f}{\partial x _ {i}}\tag{15}
$$

Note that for concave $\xi, \partial^2 d / \partial \theta^2 < 0$ , and that

$$
\frac {\partial^ {2} f}{\partial x , \partial x _ {i}} \geq \delta_ {1} \frac {\partial f}{\partial x _ {i}} \frac {\partial f}{\partial x _ {j}}
$$

is a sufficient condition for supermodularity Since both $\partial f / \partial x_{i}$ and $\partial f / \partial x_{i} > 0$ , the condition implies that as $\xi$ becomes "more" concave, i.e., as the smallest $\delta_{1}$ which satisfies (15) increases, the function $f$ must become "more strongly" supermodular in $x$ to ensure that $\xi$ will also be supermodular in $x$

Following the above approach for $y_{i}, y_{j} (i \neq j)$ , we have

$$
\frac {\partial^ {2} g}{\partial y _ {i} \partial y _ {i}} \geq \delta_ {2} \frac {\partial g}{\partial y _ {i}} \frac {\partial g}{\partial y _ {i}}
$$

as a sufficient condition for $\xi$ to be supermodular in $y$ , where

$$
\left. \frac {\partial^ {2} d}{\partial \phi^ {2}} \right/ \frac {\partial d}{\partial \phi} \geq - \delta_ {2},
$$

and where $\delta_2 > 0$ .

For $x_{i},y_{i}$ (any $\iota ,j)$ , we have

$$
\frac {\partial^ {2} \xi}{\partial x _ {i} \partial y _ {i}} = \frac {\partial^ {2} d}{\partial \theta \partial \phi} \frac {\partial f}{\partial x _ {i}} \frac {\partial g}{\partial y _ {i}} \geq 0.\tag{16}
$$

Since $d$ is supermodular in $\theta$ and $\phi$ by hypothesis, $\xi$ is jointly supermodular in $x_{i}$ and $y_{i}$

Note that there is a nice correspondence between the discrete and the continuous cases. For example, Condition (5) for the discrete case clearly corresponds to the restriction on the mixed partial derivative of $f$ for the continuous case. Similarly, as in the discrete case, the conditions in the continuous case also turn out to be separable in $f$ and $g$ .

One example of a concave function which will satisfy the conditions of Lemma 1 is $d(\theta) = \theta^{1/2}$ for $\delta_1 = \frac{1}{2}$ and $\theta \geq 1$ . Similarly, a concave function $d(\theta) = \theta^n$ ( $0 < \alpha < 1$ and $\theta \geq 1$ ) will also satisfy Lemma 1 for $\delta_1 = (1 - \alpha)$

PROOF OF PROPOSITION 1 From Lemma 1, d is supermodular in $(x, y)$ , therefore, we can write $D(z) = d(f(x), g(y))$ , where $D(z)$ is increasing and supermodular in z. $p - o(z)$ is increasing and supermodular in z, which is easily verified by taking any two points $z', z'' \in Z$ , and applying the submodularity of o in z. Since the product of two nonnegative, increasing and supermodular functions is also supermodular (Topkis 1978, 1995), $(p - o(z))D(z)$ is increasing and supermodular in z.

Let $C(u, w) = K_1(u) + K_2(w)$ . It is evident that $C(u, w)$ is increasing in $(u, w)$ . To show that $C$ is submodular in $(u, w)$ , for any two $u', u''$ , we have (from the submodularity of $K_1$ )

$$
K _ {1} (u ^ {\prime} \vee u ^ {\prime \prime}) + K _ {1} (u ^ {\prime} \wedge u ^ {\prime \prime}) \leq K _ {1} (u ^ {\prime}) + K _ {1} (u ^ {\prime \prime})\tag{17}
$$

From the submodularity of $K_{2}$ , for any two $w'$ , $w''$ , we have

$$
K _ {2} (w ^ {\prime} \vee w ^ {\prime \prime}) + K _ {2} (w ^ {\prime} \wedge w ^ {\prime \prime}) \leq K _ {2} (w ^ {\prime}) + K _ {2} (w ^ {\prime \prime})\tag{18}
$$

Adding (17) and (18), we find that

$$
\begin{array}{l} C (u ^ {\prime} \vee u ^ {\prime \prime}, w ^ {\prime} \vee w ^ {\prime \prime}) + C (u ^ {\prime} \wedge u ^ {\prime \prime}, w ^ {\prime} \wedge w ^ {\prime \prime}) \\ \leq C (u ^ {\prime}, w ^ {\prime}) + C (u ^ {\prime \prime}, w ^ {\prime \prime}). \end{array}\tag{19}
$$

Thus $C$ is submodular in $(u, w)$ . For notational simplicity, we simply write $C(z)$ instead of $C(u, w)$ . Since $C(z)$ is submodular, $-C(z)$ is supermodular. Therefore, $\Pi$ is supermodular in $z$ Q.E.D

PROOF OF PROPOSITION 2 Choose any $z^{*} \in Z^{*}$ and $z' \in Z'$ . From the optimality of $z^{*}$ , we have

$$
\Pi (z ^ {*}) \geq \Pi (z ^ {*} \vee z ^ {\prime})\tag{20}
$$

From the optimality of $z'$ with the constraint $z_i = z'_i$ , we have

$$
\Pi (z ^ {\prime}) \geq \Pi (z ^ {*} \wedge z ^ {\prime})\tag{21}
$$

From the supermodularity of $\Pi$ in $z$ , we have

$$
\Pi (z ^ {*} \vee z ^ {\prime}) + \Pi (z ^ {*} \wedge z ^ {\prime}) \geq \Pi (z ^ {*}) + \Pi (z ^ {\prime})\tag{22}
$$

From (20), (21), and (22), we find that equality must hold in each case. Therefore, $\Pi(z^{*}) = \Pi(z^{*} \vee z')$ , which implies that $z^{*} \vee z' \in Z^{*}$ . Similarly, $z^{*} \wedge z' \in Z'$ . Thus $Z' \leq Z^{*}$ Q.E.D

PROOF OF PROPOSITION 3 We follow Topkis' (1978) general approach of comparing optimality and supermodularity conditions Let $z^{*} \in Z^{*}$ and $z^{**} \in Z^{**}$ be two maximizers of $\Pi$ corresponding to $\psi'$ and $\psi''$ , respectively From the optimality of $z^{*}$ ,

$$
\begin{array}{r l} & p d (z ^ {*}) - d (z ^ {*}) o (z ^ {*}, \psi^ {\prime}) - C (z ^ {*}, \psi^ {\prime}) \geq p d (z ^ {*} \vee z ^ {* *}) \\ & - d (z ^ {*} \vee z ^ {* *}) o (z ^ {*} \vee z ^ {* *}, \psi^ {\prime}) - C (z ^ {*} \vee z ^ {* *}, \psi^ {\prime}) \end{array}\tag{23}
$$

Rearranging terms in (23), we obtain

$$
\begin{array}{r l} 0 & \geq p d (z ^ {*} \vee z ^ {* *}) - p d (z ^ {*}) - d (z ^ {*} \vee z ^ {* *}) o (z ^ {*} \vee z ^ {* *}, \psi^ {\prime}) \\ & + d (z ^ {*}) o (z ^ {*}, \psi^ {\prime}) - C (z ^ {*} \vee z ^ {* *}, \psi^ {\prime}) + C (z ^ {*}, \psi^ {\prime}) \end{array}\tag{24}
$$

From the optimality of $z^{**}$ ,

$$
\begin{array}{l} p d (z ^ {* *}) - p d (z ^ {*} \wedge z ^ {* *}) - d (z ^ {* *}) o (z ^ {* *}, \psi^ {\prime \prime}) \\ + d (z ^ {*} \wedge z ^ {* *}), o (z ^ {*} \wedge z ^ {* *}, \psi^ {\prime \prime}) - C (z ^ {* *}, \psi^ {\prime \prime}) \\ + C (z ^ {*} \wedge z ^ {* *} \psi^ {\prime \prime}) \geq 0 \end{array}\tag{25}
$$

According to Lemma 2, $\Pi$ is supermodular in $(z, \psi)$ . Thus for $(z^{*}, \psi')$ and $(z^{**}, \psi'')$ , we have

$$
\begin{array}{l} p d (z ^ {*} \vee z ^ {* *}) - d (z ^ {*} \vee z ^ {* *}) o (z ^ {*} \vee z ^ {* *}, \psi^ {\prime}) - C (z ^ {*} \vee z ^ {* *}, \psi^ {\prime}) \\ \qquad + p d (z ^ {*} \wedge z ^ {* *}) - d (z ^ {* *}) o (z ^ {* *}, \psi^ {\prime \prime}) - C (z ^ {*} \wedge z ^ {* *}, \psi^ {\prime \prime}) \\ \geqslant p d (z ^ {*}) - d (z ^ {*}) o (z ^ {*}, \psi^ {\prime}) - C (z ^ {*}, \psi^ {\prime}) \\ \qquad + p d (z ^ {* *}) - d (z ^ {* *}) o (z ^ {* *}, \psi^ {\prime \prime}) - C (z ^ {* *}, \psi^ {\prime \prime}) \end{array}\tag{26}
$$

Combining the inequalities in (24), (25), and (26) (after rearranging terms), we see that equality must hold Hence,

$$
\begin{array}{r l} & p d (z ^ {*}) - d (z ^ {*}) o (z ^ {*}, \psi^ {\prime}) - C (z ^ {*}, \psi^ {\prime}) \\ & = p d (z ^ {*} \vee z ^ {* *}) - d (z ^ {*} \vee z ^ {* *}) o (z ^ {*} \vee z ^ {* *}, \psi^ {\prime}) \\ & - C (z ^ {*} \vee z ^ {* *}, \psi^ {\prime}). \end{array}\tag{27}
$$

INFORMATION SYSTEMS RESEARCH
Vol. 7, No. 4, December 1996

Therefore, $z^{*} \vee z^{**}$ must also be a maximizer of $\Pi$ for $\psi = \psi'$ , and must therefore lie in $Z^{*}$ . Similarly, we can show that $z^{*} \wedge z^{**}$ lies in $Z^{**}$ . Thus $Z^{**} \leq Z^{*}$ QED

LEMMA 2 Let $Z$ and $\Psi$ be sublattices of $R^{n+m}$ and $R'$ respectively. Consider the function $\Pi = pd(z) - o(z, \psi)d(z) - C(z)$ , where $z \in Z$ , $\psi \in \Psi$ , and $p$ (a constant) $\geq o(z, \psi)$ for all $(z, \psi)$ $d(z)$ is increasing and supermodular in $z$ . $o(z, \psi)$ is decreasing and submodular in $(z, \psi)$ . $C(z, \psi)$ is submodular in $(z, \psi)$ . Then $\Pi$ is supermodular in $(z, \psi)$ .

PROOF OF LIMMA 2 First we prove that $p - o(z, \psi)$ is supermodular in $(z, \psi)$ . For any two $z', z'' \in Z$ and $\psi', \psi'' \in \Psi$ , let $\overline{z} = z' \vee z'', \underline{z} = z' \wedge z'', \bar{\psi} = \psi' \vee \psi''$ , and $\underline{\psi} = \psi' \wedge \psi''$ . Let $p - o(z, \psi) = \eta(z, \psi)$ . Then we have

(28)

Next we show that $(p - v(z, \psi))d(z)$ is supermodular in $(z, \psi)$ . Note that

$$
\begin{array}{r l} & {\eta (\overline {{{z}}}, \overline {{{\psi}}}) d (\overline {{{z}}}) - \eta (z ^ {\prime}, \psi^ {\prime}) d (z ^ {\prime})} \\ & {\geq \eta (z ^ {\prime}, \psi^ {\prime}) [ d (\overline {{{z}}}) - d (z ^ {\prime}) ] + \eta (z ^ {\prime \prime}, \psi^ {\prime \prime}) d (z ^ {\prime \prime}) - \eta (\underline {{{z}}}, \underline {{{\psi}}}) d (z ^ {\prime \prime})} \\ & {- \eta (\underline {{{z}}}, \underline {{{\psi}}}) d (\underline {{{z}}}) + \eta (\underline {{{z}}}, \underline {{{\psi}}}) d (\underline {{{z}}}) \geq \eta (z ^ {\prime \prime}, \psi^ {\prime \prime}) d (z ^ {\prime \prime}) - \eta (\underline {{{z}}}, \underline {{{\psi}}}) d (\underline {{{z}}})} \\ & {+ \eta (z ^ {\prime}, \psi^ {\prime}) [ d (\overline {{{z}}}) - d (z ^ {\prime}) - d (z ^ {\prime \prime}) + d (\underline {{{z}}}) ]} \\ & {\geq \eta (z ^ {\prime \prime}, \psi^ {\prime \prime}) d (z ^ {\prime \prime}) - \eta (\underline {{{z}}}, \underline {{{\psi}}}) d (\underline {{{z}}})} \end{array}\tag{29}
$$

Finally, to show that $\Pi = \eta(z, \psi)d(z) - C(z, \psi)$ is supermodular in $(z, \psi)$ , note that

$$
\begin{array}{r l} & {\Pi (\overline {{{z}}}, \overline {{{\psi}}}) - \Pi (z ^ {\prime}, \psi^ {\prime})} \\ & {\qquad \geq \eta (z ^ {\prime}, \psi^ {\prime}) d (\overline {{{z}}}) + \eta (z ^ {\prime \prime}, \psi^ {\prime \prime}) d (\overline {{{z}}}) - \eta (\underline {{{z}}}, \underline {{{\psi}}}) d (\overline {{{z}}}) - \eta (z ^ {\prime}, \psi^ {\prime}) d (z ^ {\prime})} \\ & {\qquad - C (z ^ {\prime \prime}, \psi^ {\prime \prime}) + C (\underline {{{z}}}, \underline {{{\psi}}}) \geq [ \eta (z ^ {\prime \prime}, \psi^ {\prime \prime}) d (z ^ {\prime \prime}) - C (z ^ {\prime \prime}, \psi^ {\prime \prime}) ]} \\ & {\qquad - [ \eta (\underline {{{z}}}, \underline {{{\psi}}}) d (\underline {{{z}}}) - C (\underline {{{z}}}, \underline {{{\psi}}}) ]} \\ & {\qquad + \eta (z ^ {\prime}, \psi^ {\prime}) [ d (\overline {{{z}}}) + d (\underline {{{z}}}) - d (z ^ {\prime}) - d (z ^ {\prime \prime}) ]} \\ & {\qquad \geq [ \eta (z ^ {\prime \prime}, \psi^ {\prime \prime}) d (z ^ {\prime \prime}) - C (z ^ {\prime \prime}, \psi^ {\prime \prime}) ] - [ \eta (\underline {{{z}}}, \underline {{{\psi}}}) d (\underline {{{z}}}) - C (\underline {{{z}}}, \underline {{{\psi}}}) ]} \\ & {= \Pi (z ^ {\prime \prime}, \psi^ {\prime \prime}) - \Pi (\underline {{{z}}}, \underline {{{\psi}}}) Q E. D.} \end{array}\tag{30}
$$

## References

Applegate, L. M., Frito Lay, Inc. A Strategic Transition (Consolidated), Harvard Business School Publishing, Boston, MA, 1992.

——, Phillips 66 Transforming the Organization of the 1990s, Harvard Business School Publishing, Boston, MA, 1994a.

—, "Managing in an Information Age. Transforming the Organization for the 1990s," in S Smithson, R Baskerville, O Ngwenyama. and J DeGross (Eds.), Information Technology and Emergent Forms of Organization, Elsevier, North Holland, 1994b

Barua, A, C H Kriebel, and T Mukhopadhyay, "A New Approach to Assessing the Economic Impacts of Information Technology Investments," presented at the first Workshop on Information

Systems and Economics (WISE), MIT Sloan School, Cambridge, MA, December, 1989

——, ——, and ——, "Information Technologies and Business Value An Analytical and Empirical Investigation," Information Systems Res., 6, 1 (1995), 3–23

——, C.-H S Lee, and A B. Whinston, "Incentives and Computing Systems for Team Based Organizations," Organization Sci, 6, 4 (1995), 487–504.

Bashein, B, L. Markus, and P Riley, "Preconditions for BPR Success," Information Systems Management, Spring (1994), 27–38

Beekun, R. I, "Assessing the Effectiveness of Sociotechnical Interventions. Antidote or Fad?" Human Relations, 42, 10 (1989), 877–898

Bleakley, F R., "Many Companies Try Management Fads, Only To See Them Flop," The Wall Street Journal, July 6, 1993

Davenport, T. H., Process Innovation: Reengineering Work through Information Technology, Harvard Business School Press, Boston, MA, 1993

Edgeworth, F Y, Mathematical Psychics, Kegan Paul, London, 1881

Hammer, M and J Champy, Reengineering the Corporation A Manifesto for Business Revolution, Harper Business, New York, 1993

Harrar, G, “Baldrige Notwithstanding,” Forbes, 153, 5 (1994), 44–49.

Jeffery, B, "A Clean Slate. Reengineering Can be the Greatest Challenge IS has Ever Confronted," MIDRANGE Systems, 7, 14 (1994), p. 23.

Leibs, S., "Hammer's Belief—Reengineering Requires Passionate Leadership," Information Week, June 20, 1994.

Manganelli, R. L., "Define 'Re-engineer'", Computerworld, July 19, 1993.

Margulis, S., "Bad News, Good News About Downsizing, Guidelines for Successful Corporate Downsizing," Modern Office Technology, 39, 4 (1994), 23–24

Martinez, E. V., "Successful Reengineering Demands IS/Business Partnerships," Sloan Management Review, Summer (1995), 51–60

Milgrom, P and J Roberts, "The Economics of Modern Manufacturing: Technology, Strategy, and Organization," American Economic Review, June (1990), 511–528

Mintzberg, H., Structure in Fives Designing Effective Organizations, Prentice Hall, Englewood Cliffs, NJ, 1983.

Monteleone, F, "Re-engineering: Don't Miss This Train," Computerworld, January 31, 1994

Rifkin, G, "Reengineering Aetna," Forbes, 151, 12 (1993), 78–86

Rock, D and D. Yu, "Improving Business Process Reengineering," AI Expert, 26, 10 (1994), 27–34.

Samuelson, P A., "Complementarity," J Economic Literature, 12 (1974), 1255–1289

Schoonhoven, C B, "Problems with Contingency Theory Testing Assumptions Hidden Within the Language of Contingency 'Theory'", Admin. Sci Quarterly, 26 (1981), 349–377

Stewart, T., "Reengineering. The Hot New Managing Tool," Fortune, 128, 4 (1994), 40–46

Topkis, D M, "Minimizing a Submodular Function on a Lattice," Oper Res, 26 (April 1978), 305–321.

——, "Comparative Statics of the Firm," J Economic Theory, 67, 2 (Dec 1995), 370–401.

——, "Modern Manufacturing Revisited," Technical Report, University of California at Davis, Davis, CA, 1994b.

Van de Ven, A H and R Drazin, "The Concept of Fit in Contingency Theory," in Barry M. Staw and Larry L. Cummings (Eds), Research in Organizational Behavior, Volume 7, JAI Press, Greenwich, CT, 1995, 333–365.

Weber, M., "Economy and Society," Bedminster Press, New York, 1968

Weill, P, "The Relationship Between Investment in Information Technology and Firm Performance: A Study of the Valve Manufacturing Sector," Information Systems Res, 3, 4 (1992), 307–333

Seungjin Whang, Associate Editor This paper was received on September 7, 1994 and has been with the authors 8 months for 2 revisions
