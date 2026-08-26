---
otero_id: 16956
otero_key: "DWH4QMY2"
title: "The emerging role of DSS: From passive to active"
authors: "M.Tawfik Jelassi; Karen Williams; Christine S Fidler"
year: "1987"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(87)90101-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Emerging Role of DSS: From Passive to Active $^{1}$

M. Tawfik JELASSI \*, Karen WILLIAMS \*\* and Christine S. FIDLER \*\*\*

\* Indiana University, Bloomington, IN 47405, USA

\*\* Humberside College of Higher Education, Hull HU6 7RT, UK

\*\*\* University of York, Heslington, York Y01 5DD, UK

Existing decision support systems (DSS) are passive in their operation; their sole aim is to help maintain the current position of the firm. Conversely, Information Technology has recently adopted a more active role in the corporate strategy. This suggests that DSS could also undertake a far more active stance by identifying gaps in existing operations and suggesting ways to strengthen the standing of the firm. We renamed DSS containing this characteristic as Active Decision Support Systems (or ADSS) to emphasize their new orientation. Managers draw on their knowledge to suggest ways of alleviating problems or exploiting opportunities, and to evaluate each alternative in relation to the corporate objectives. Patterns and alternatives must be identified and incorporated into the ADSS. They should then be compared with the current position of the firm in order to determine whether any such problems/opportunities exist. This paper proposes an approach for designing ADSS; it introduces a knowledge-based component within the DSS framework and applies the concept of triggers to control the invocation of rule sets. A logical structure for ADSS is provided and the system use is illustrated through an example of strategic management. Issues for future research are highlighted.

Keywords: Decision Support Systems, Strategic Decisions. Knowledge-Based Decision Making, Expert Systems, Database Management.

## 1. Introduction

A DSS is a computer-based system which has the objective of enhancing the overall effectiveness (e.g., by increasing reliability, accuracy and efficiency of obtaining relevant information) of decision makers, especially in their unstructured and semi-structured tasks.

This definition implies that decision makers may be equipped with one or more DSS to assist in all their areas of interest, covering many of the problem domains that they face in their span of operations. For instance, a credit controller may require a DSS to assist decision making relating to

![](/api/attachments/DWH4QMY2/fulltext/images/13b20b7344f4983a3099ad9b294aa79be373aed2eaeae2c6cda0a70daa2158d5.jpg)

M. Tawfik Jelassi is an Assistant Professor of Management Information Systems at Indiana University. He received a Ph.D. in Computer Applications and Information Systems from New York University, and Diplomas in Computer Science and Business Administration from the University of Tunis and the University of Paris-Dauphine. Dr. Jelassi has published numerous book chapters and journal or conference articles in the areas of Decision Support Systems, Multiple

Criteria Decision Making, and Database Applications.  
![](/api/attachments/DWH4QMY2/fulltext/images/afbce95f78bcaba2d02b11697ed025ba58f81305e61e8a241a59d73a85c92426.jpg)

Christine Fidler is currently completing a Ph.D. dissertation in Computer Science at the University of York. During the 1986–87 academic year, she was a Visiting Scholar at the University of Pennsylvania Wharton School. Her research interests include various aspects of information systems, in particular, the computer-based support of managerial activities within the firm.

![](/api/attachments/DWH4QMY2/fulltext/images/0ad6cc972aa66467fae8ee8e83b3a8ec5179cbeb9cfe8bdf6f2950293d73900e.jpg)

Karen Williams graduated from Newcastle-Upon-Tyne Polytechnic with first class honors in business studies. She has been a lecturer in the systems management area at both Humberside College of Higher Education and the University of Hull. She has recently joined the Department of Business and Professional Studies at Teesside Polytechnic. The focus of her current research is fuzzy decision aids for investment decision making.

existing customer accounts such as credit amount and duration extensions. He might also require a DSS relating to new customer accounts such as the evaluation of a new customer's creditworthiness.

In this example the problems are fairly well defined, but if we broaden the scope of interest of the decision maker to include strategic management functions such as long-range planning, controlling and organising, then we begin to contend with an increasing number of less well-structured problems [3]. To cope with these, the assistance given by the DSS must likewise broaden viz., the DSS should also support ‘forward-looking’ decisions associated with opportunistic planning as well as historical-based decisions more generally concerned with problems of control.

However, Decision Support Systems do not promote use in a forward-looking mode: they suggest a supportive but passive role within the organisation, providing information to management decision makers within which they themselves have to search and find new opportunities for development. Rather, systems should be equipped with ways of helping this task, perhaps by identifying gaps in existing procedures and methods and suggesting ways of using them to the company's advantage. They would then provide more positive, forward-looking contributions to the achievement of organisational objectives.

An example of a passive DSS is PMS (Portfolio Management System), developed by Gerrity in the early 1970s to assist the problems of allocating investment securities to portfolios [19]. Its design centres around the use of several predefined operations such as allowing the user to examine existing portfolio and security statistics (STATUS, HISTO and SCATTER) and to analyse how well a potential security profile fits in with a current portfolio contents (CREATE). As it stands, this system has no apparent active features. (This may well be due to technical constraints, most of which have been overcome in the last two decades). However, it may not be possible to incorporate some active features on top of the existing framework of the system. For example, a PMS facility to summarise the essential characteristics of a new security for a portfolio would enable users to become increasingly aware of the nature of securities for which they are searching. It can be seen as active in that rather than controlling existing portfolios of investments and looking how specific known securities may fit into a given portfolio, it aims to identify gaps in portfolios and initiate a searching mechanism for new opportunities.

We wish to emphasise that new DSS should be developed from the start with an active orientation. Obviously, this must only be considered if the current situation would benefit from active support. We have seen, in the last decade, an upsurge in DSS supporting more ad-hoc and semi-structured problems but still the emphasis is on maintaining the status-quo. It is towards the furthering of more forward-looking systems that this paper is addressed.

## 2. Information Technology as a Strategic Weapon: Why not DSS?

In the past, Information Technology (I.T.) has generally played a passive role in an organisation's corporate plan, with the EDP department being considered as the 'backroom-boys'. This opinion has considerably changed: I.T. is now playing a positive, central role in the corporate strategy with much success. Organisations now realise that it can be used as a competitive weapon in various ways, such as narrowing the chance of success of competitors after the same market share [22]. For example, a company supplying goods to a number of large retail outlets installed terminals (from which their central computer running a goods-ordering system could be directly accessed) in each of its major customer's premises free of charge. By providing this service, the incentive for the retailing outlet to switch to another supplier was greatly reduced. The original supplier thus gained greater security in its market share and an improved competitive advantage.

I.T. has also been used to enhance image in the market place. For instance, a hotel has its networked micro-computer terminals deliberately left on show in its restaurants, bars, hairdressing salon and reception in order to create an air of efficiency.

In short, I.T.'s importance to organisations has been recognised. (Nowadays, if often represents a large percentage of the company capital investment.) Management are eager to use I.T. to its full potential to maximise return on investment and contribution to corporate profits, and they achieve this by using it both supportively (e.g., in data processing) and actively (e.g., in marketing) [1].

We believe that DSS builders and users should adopt this ‘attitude’ towards DSS so that they gain full return on their investment viz. DSS should be applied more positively and actively to the attainment of corporate objectives.

## 3. Towards an ‘Active Decision Support System’ (ADSS)

We have already discussed the widespread lack of activeness in existing DSS. However, the recent meeting of the NATO Advanced Study Institute on DSS [29] entertained more ideas which, to some extent, can be termed active. For instance, Salas Fumas [26] suggested the use of Real-Time Strategic Planning (based on work by Ansoff [2]) as a way to deal with planning in a rapidly changing and surprising environment.

Others (e.g., Methlie [23]) demonstrated the suitability of integrating knowledge-based techniques and numerical/quantitative techniques (more usually associated with traditional DSS). In fact the framework of Bonczek, Holsapple and Whinston [5,6,7] bears more than just an apparent similarity to the common Expert System (ES) paradigm: they consider ES as a form of DSS.

What we will demonstrate in this section of the paper is why and how knowledge bases may be included in DSS to give them a dimension of activeness in a similar vein to that proposed by Salas Fumas [26] and Ansoff [2].

## 3.1. Knowledge Bases

Expertise relating to a wealth of subjects can be found in an organisation. For instance, financial experts due to their experience and training have, over the years, acquired a great body of knowledge on how to invest the company's capital in the best possible ways. Marketing have equally acquired knowledge on how to publicise and promote products given the resources and means available. As for top managers themselves, they have learned how to formulate corporate policy using information (both formal and informal) flowing from a multitude of different sources.

Traditional DSS do not explicitly apply this expertise to its maximum potential. Managers are provided with sets of tools which are used to generate different views of the same data (e.g., through aggregation). They then draw on their own knowledge and experience to interpret these views in the hope of understanding the corporate position and to subsequently identify new opportunities or existing problems. When an opportunity/problem is identified, the next step is to find a set of potential solutions. Some may already be known to managers, but sometimes further information gathering and analysis is necessary. Finally, options are evaluated against corporate objectives and the one that fairs best is chosen for implementation. (However, to reach agreement as to which is best is a taxing problem in its own right, as many of the objectives such as maximising profits, maintaining public interest and ensuring the interests of employees, are incomparable).

In the last score years, there has been a growing interest focusing on the potential of embodying human knowledge within computers. This potential has partially been realised in the form of Expert Systems (ES), a commercial spin-off from Artificial Intelligence (AI) research. These are systems which demonstrate a level of intelligence akin to human experts in certain specific subject domains.

In most ES implementations, the following sub-components are present:

(1) a knowledge base,

(2) a working memory, and

(3) an inference engine.

The knowledge base contains rules which encode the expert's rules of thumb or 'heuristics'. These are most commonly of the form:

IF $\langle$ condition-statement $\rangle$ THEN $\langle$ action-statement $\rangle$ .

The working memory holds facts relating to the current situation under investigation. It is dynamically updated as the system goes through its paces. Reasoning about the problem, by applying rules to the facts stored in the working memory or by asking the user, is the function of the inference engine.

Another feature, considered by some as vital to Expert Systems, is the system's ability to explain its line of reasoning. This allows the user to 'look inside' and see how the final decision or an intermediate hypothesis was reached. Users can use this facility to identify possibly crucial factors that were overlooked during the system's evaluation.

An ADSS, searching for new opportunities within the milieu of company facts and figures, needs access to corporate expertise. Where and how this expertise is to be used to equip systems with more active features will become apparent as we investigate the concept of triggers and the place of knowledge bases within an existing DSS framework – the topics of the following two sections respectively.

## 3.2. The Concept of Triggers

Triggers are certain prescribed conditions which, when true, invoke the use of rule sets. They have already been used in conceptual database modeling, in office automation [8,9], in Artificial Intelligence (disguised by the more amusing name: demons, e.g., see PTRANS [21] and HEARSAY-II [12] systems) and even briefly in the DSS literature [10,28]. Examples of use are to monitor the state of a system, to serve as prompts or reminders, and to detect exceptional circumstances.

We can see a tremendous application for triggers in DSS: to invoke appropriate subsystems into action when the 'state of the system' permits. (How and when the system's state is evaluated is readdressed in later sections of this paper.)

At Imperial College, London, triggering is being implicitly used in an on-going project that combines spreadsheet and expert system concepts using a common development language, PROLOG [18]. At present, the domain of expertise is cash flow analysis. When a situation is identified as hindering the attainment of a positive cash balance, a subset of PROLOG rules is invoked to suggest how the cash balance can be rectified. This so-called ‘Management by Objectives’ is one way by which people actually find problems that need solving.

Whilst this demonstrates the use of triggers for remedial purposes, there has been little movement in the DSS field about triggers to promote desirable organisational activity. That is to say, while the current position of the firm is not necessarily unfavourable with respect to corporate objectives, gaps in existing procedures might be identified. These could, if successfully exploited, strengthen the company's standing still further.

In this paper, we separate triggers into two ‘role’ categories: as either active/promotional or passive/remedial.

## 3.3. The Logical Structure of an ADSS

In this section, we first survey the logical structure of a decision support system that will be used as a foundation for constructing an ADSS.

For Sprague and Carlson [28], the major sub-systems are

(1) a data manager,

(2) a model manager, and

(3) a dialog manager.

The inter-relationships between these three managers and the decision maker are shown in. fig. 1.

An ADSS is an extension of this structure to include a knowledge-based component in the manner shown in fig. 2.

The user interacts with the models, data and knowledge base via a common interface. The database is perceived as a universal repository of data which stores both raw and elaborate data, as well as intermediate and final decision results [16]. The user can select a decision model, extract rele-

![](/api/attachments/DWH4QMY2/fulltext/images/3549b9b2702de31f9f08935c512bd272d492d068879caf9008a8cceea0a2491c.jpg)

KEY RELATIONSHIPS :

① Request for action, data

② Retrieved data, results from action

③ Invoke, interrupt model, collection of model parameters

④ Parameter request, notification of interrupt

⑤ Request retrieval, update, creation of data

⑥ Present data to user

⑦ Input data to model from database(s)

⑧ Output data from model for storage (temporarily or permanent)

Fig. 1. The DSS Framework [28].

5 Requested information transmitted to the knowledge base.

![](/api/attachments/DWH4QMY2/fulltext/images/9284c611a87433c8a55ed56edbe89f668bd3075b61d8a6d8c2b7414184a2781d.jpg)

EXTRA KEY RELATIONSHIPS

1 Current state of system evaluated against trigger conditions to see if any problems /opportunities can be determined.

2 Remedial triggers invoke rule sets to suggest remedies and how each should be evaluated

3 Promotional triggers invoke rule sets to suggest ways to exploit the opportunities and how these should be evaluated.

4 Information requested by Knowledge Base of user/ database / via model invocation (output)

Fig. 2. Logical Structure of an ADSS.

vant data from internal and/or external sources and customise his/her decision making problem by means of sophisticated view definition capabilities (for further details see [14,15,17]).

Thus, the ‘state of the system’ (or the ‘working memory’, using ES terminology) is reflected in the current state of the database. How often the state of the system has to be evaluated is a critical issue, but when this occurs, two sets of circumstances may be identified. Firstly, circumstances that are perceived as preventing the maintenance of the status-quo are uncovered by remedial triggers. Secondly, circumstances, which, if exploited, could strengthen the company’s future standing are uncovered by promotional triggers. Triggers are themselves rules, conceptually of the form

IF condition-1 AND condition-2 AND ... AND condition-n THEN investigate Option-1, Option-2, Option-3,...,

Option-m).

where n and m are arbitrary numbers. Conditions may invoke other rules if their values cannot be directly established from the available data. For example, consider the following remedial trigger:

IF NOT (sales have increased > 0% for product-A in Our Company)

AND (sales have increased > 0% for product-A in Competitor-Company)

THEN investigate (sales promotion campaign, decrease price).

Both conditions require the use of a further rule

IF sales (this year, company, product, x)

AND sales (last year, company, product, y)

AND $(\mathbf{x} - \mathbf{y}) / \mathbf{y}*\mathbf{100} > \mathbf{z}$

THEN sales have increased > z% for product in company.

As an example of a promotional trigger, acting upon competitor production data (for a product manufactured by the company) and market research data, consider the following rule:

If (competitor x production of product-A increases)

AND NOT (total competitor production of product-A increases)

OR (new customer appears on market)

THEN (investigate possibility of supplying newly freed demand).

The sales production and market research data may be directly established from the working memory, or provided by an appropriate model or function $[15,25]$ . As a last resort, the system asks the user for their values.

Triggers form part of the knowledge base (see areas C and D in fig. 2). Both types of triggers, when true, invoke rule sets. Remedial triggers suggest likely remedies (area B in fig. 2) and promotional triggers suggest ways of manipulation (area A in fig. 2). So in the example above, a sales promotion campaign or the possibility of undercutting the competitor by decreasing the price of the product are suggested as possible actions to pursue. The user may then wish to investigate various options more thoroughly in order to determine their applicability to the situation in hand.

From the user point of view, the entire operation is seen as a continuous consultation session with the system similar to that of existing expert systems such as MYCIN [27]. (Consultation is represented by lines 4 and 5 in fig. 2.) During consultation, the user is asked to provide those facts not available from the database (or not provided by the results of DSS model invocation). All requests for data, model invocation and user replies are completed via the Dialog Manager.

When the user has adopted his/her own or the system's recommended solution, implementation can take place. This may be a lengthy process (in some cases a matter of years); but, as time passes its effect will propagate throughout the company and, subsequently, to its information systems. As a consequence, further triggers might be activated when future evaluations take place.

## 3.4. ADSS Use: A Hypothetical Example

To illustrate what has been said so far, consider the situation of WASHBRIGHT, a company that manufactures automatic washing powders. Its organizational objective (for the sake of simplicity) is to maximise corporate profits. The company presently uses a DSS to monitor and control corporate expenditures and revenues. The objectives of this DSS are to keep expenditure within tolerable limits and maintain revenues above an absolute minimum respectively. Both adhere to the achievement of total organisational objectives, but both are geared towards the maintenance of the status-quo, since if expenditures and revenue targets are met, management are happy and for all intents and purposes, the DSS employed is a success.

For the current fiscal year, the profit margin set by WASHBRIGHT was agreed at 20% of the total revenue. The budgets for all separate departments were subsequently set with this figure in mind. In reality, however, it was extremely difficult to keep within a tight limit of resources and, in some departments (e.g., marketing where the price of advertising rose sharply over the year), monthly budgets were exceeded. It is the task of remedial triggers to alert the DSS user of such deviations so that the problems can be immediately assessed and, where possible, overcome. It may be the case that the overexpenditure of the marketing department can be compensated by the under-expenditure of another department (e.g., production). Alternatively, the company may have some surplus capital and can withstand the extra cost with no serious repercussions. As a last resort, the company may have to review its existing advertising campaign and search for less expensive media for publicising their product. These are just some of the options that could be suggested by computer and subsequently investigated.

Let us now add to WASHBRIGHT's business armoury an ADSS for detecting new market opportunities. Like the aforementioned decision support systems, the ADSS must adhere to corporate objectives, so the system's objective is to highlight and model potential profitable opportunities. The database holds (or has access to) production, sales, market research and investment data of the company's existing markets as well as competitor and associated markets (what an associated market is is subjective).

As indicated by recent market surveys, WASHBRIGHT currently has a very strong hold on the market share of automatic washing powders. Everything seems to be going according to plan: the yearly profit estimate seems to be within easy reach. However, winter is approaching and, with it, more woolens will be hand washed. A leading competitor has a substantial stronghold on the non-automatic washing powder market, but charges relatively high prices for the product. WASHBRIGHT has all the production facilities (which at present are not used to its full capacity) to manufacture a non-automatic powder: the only difference is the ratio of the raw materials required. The procurement of these additional resources is guaranteed by the existing suppliers. With regards to labor, two options are available; either to give existing employees the opportunity of overtime, or to increase the size of the workforce at least for a trial period.

In short, the possibility of increasing the scope of WASHBRIGHT's operations to include non-automatic washing powder might well be an opportunity that, economically speaking, should not be ignored. Obviously, a full investigation into the appropriate cash inflows and outflows is necessary before an estimate of potential profit can be determined with any degree of accuracy.

It is the task of promotional triggers to identify these types of opportunities and to suggest ways to effectively exploit them. They are not concerned with maintaining the status-quo, but aim to help strengthen the position of the firm still further.

## 4. Related Issues for Further Research

Although the logical structure outlined above seems plausible, there are many issues yet to be resolved before an ADSS can be realised. Those identified are discussed below, namely

(1) Timing of trigger evaluation,

(2) Cycling/Recursion,

(3) Divergent triggers,

(4) Specifying triggers for ADSS,

(5) Problems in ES also apply to ADSS, and

(6) Subjectiveness of 'good' opportunities.

## 4.1. Timing of Trigger Evaluation

The question is when do we evaluate triggers? Too frequent evaluation can increase user response time severely. Furthermore, it could be extremely frustrating to the user. On the other hand, too infrequent evaluation may lead to vital issues being delayed. We have suggested that a ‘sufficient’ change in the state of the database should initiate an evaluation of the triggers, but what we mean by ‘sufficient’ has yet to be resolved.

## 4.2. Cycling / Recursion

Consider the following relationships:

'Sales determines Volume',

'Volume determines Price', and

'Price determines Sales'.

This may well lead to problems of infinite triggering; as one is amended, another may be in need of amendment. The system should be sensitive of such cycles, and should take appropriate action (with the provision that the user is made aware of the system's actions at all times).

![](/api/attachments/DWH4QMY2/fulltext/images/b2201772be8eff8460bdd4f88cfec3c89e2b9b1a4091e9d71ec3a048e95bb37b.jpg)  
Fig. 3. Amending Triggers: The 'Explosion Effect'.

## 4.3. Divergent Triggers

One amendment may subsequently lead to more than one trigger being invoked in the next evaluation. There is a similar problem in Expert Systems (e.g., DENDRAL [20]) commonly known as 'Combinatorial Explosion' (see fig. 3). As in the second point above, the system should, in theory, be able to cope with such circumstances.

## 4.4. Specifying Triggers for ADSS

Although the company objectives are set by the board of directors and are upheld throughout the company, the methods by which these objectives are achieved by different managers are often subject to debate. The system must permit users to have these differences of opinion and to tailor the triggers accordingly. In short, language constructs should be made available to permit users to have customised triggers.

It may well be the case that a Managerial Support Environment (MSE) will support the definition of triggers. Such a system is defined as 'network and computer-based facilities which permit management to carry out their activities quickly and easily through special purpose workstations' [13]. To function successfully, a MSE must integrate naturally with current management practice. As Mintzberg [24] states, empirical studies show that 'the manager works in an environment of stimulus-response, and he develops in this work, a clear preference for live action'. Triggers can provide management with such opportunities of stimulus-response and live action: they identify problems and opportunities as they emerge.

## 4.5. Problems for ES also Apply to ADSS

Since we are applying ES technology to ADSS, we must expect problems arising from the former to also apply to the latter. Knowledge acquisition has always been considered a major bottleneck in the development of ES. At present, there are very few experienced people that have the techniques and know-how to elicit appropriate knowledge from experts and to present it in a machine-readable form. (In ES terminology, the men and women involved in the design of knowledge-based systems are known as ‘knowledge engineers’.) As more becomes known through successful and notso successful case studies, general guidelines may be developed to aid the inexperienced in this task.

We, as humans, keep building on our existing store of knowledge as we become more experienced through trial and error. Likewise, a knowledge base should never remain static: it should learn from its mistakes and thus become more proficient in its task. However, as little headway has been made by AI researchers towards machine learning, we must rely on manual updating at present.

However, there are some systems that facilitate the process of adding new knowledge manually. The most famous is that of TEIRESIAS (developed by Davis in conjunction with research into the MYCIN system) which uses self-knowledge for knowledge acquisition. For further information see $[4,11]$ .

## 4.6. Subjectiveness of 'Good' Opportunities

One of the problems of defining promotional triggers (i.e., identifying good opportunities for an organisation) is that they are subjective. What must be aimed for in the modeling is a consensus between members of management as to what may be correctly construed as a good opportunity. 'Since often the identification of a good opportunity may be based on informal and ill-defined data and 'hunches', there is a need to recognise and operate on the fuzzy terms and situations (e.g., 'useful profit', and 'unhealthy economy') of various decision-makers within the organization' [30].

## 5. Summary

It is the authors' belief that the full potential of decision support systems can only be realised through the active as well as supportive utilisation of these systems.

The idea of ADSS – a DSS which provides a greater ‘forward-looking’ emphasis on decision support – has been investigated in this paper. The concepts of active/promotional triggers, which highlight new desirable situations of the company, as well as passive/remedial triggers for maintaining the existing corporate position are of tremendous importance in achieving this type of support.

The logical structure of an ADSS has been described, and an illustrative example of the system use for management decision making has been provided. Technical and organizational issues yet to be overcome have been outlined as areas of further research.

## References

[1] Arthur Andersen and Co., Trends in Information Technology: 1985 (Arthur Andersen and Co., Chicago, Ill, 1984).

[2] J. Ansoff, Implanting Strategic Management, (Prentice-Hall, Englewood Cliffs, NJ, 1984).

[3] R.N. Anthony, Planning and Control Systems: A Framework for Analysis, Harvard School of Business Administration, Harvard University (1965).

[4] A. Barr and E.A. Feigenbaum, The Handbook of Artificial Intelligence 2, (Kaufman, Los Altos, CA, 1982).

[5] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems (Academic Press, New York, 1981).

[6] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, A Generalized Decision Support System using Predicate Calculus and Network Data Base Management, Operations Research 29, Nr. 2 (1981).

[7] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Developments in Decision Support Systems, Advances in Computers 23 (1984) 141–175.

[8] G. Bracchi and B. Pernici, Decision Support in Office Information Systems, in: [29].

[9] O.P. Buneman and H.L. Morgan, Implementing Alerting Techniques in Database Systems, Proceedings of the IEEE-COMPSAC Conference (Nov., 1977) 463–469.

[10] E.K. Clemons, Database Design for Decision Support, Proceedings of the 14th Hawaii International Conference on Systems Sciences (1981).

[11] R. Davis, Interactive Transfer of Expertise: Acquisition of New Inference Rules, Proceedings of the Fifth International Joint Conference on Artificial Intelligence (Aug., 1977).

[12] L.D. Erman, F. Hayes-Roth, V.R. Lesser and D.R. Reddy, The HEARSAY-II Speech Understanding System: Integrating Knowledge to Resolve Uncertainty, Computing Surveys 12, Nr. 2 (1980) 213–253.

[13] C.S. Fidler and C.J. Tully, Towards a Model of Managerial Activities: A Foundation for the Design of A Management Support Environment, Working paper, University of York (1986).

[14] M. Jarke, M.T. Jelassi and E.A. Stohr, A Data-Driven User Interface Generator for A Generalized Multiple-Criteria Decision Support System, Proceedings of the IEEE-Computer Society Workshop on Languages for Automation (Nov., 1984) 121–127.

[15] M.T. Jelassi, A Relational Database Extension for Generalized Multiple Criteria Decision Support Systems, Ph.D. Dissertation, Department of Computer Applications and Information Systems, New York University (1985).

[16] M.T. Jelassi, M. Jarke and A. Checroun, A Database

Approach for Multiple Criteria Decision Support Systems, in: G. Fandel and J. Spronk, eds., Multiple Criteria Decision Making: Theory, Applications and Software (Springer-Verlag, Berlin and New York, 1985).

[17] M.T. Jelassi, M. Jarke and E.A. Stohr, Designing a Generalized Multiple Criteria Decision Support System, Journal of Management Information Systems 1, Nr. 4 (1985) 24–43.

[18] J. Jenkins and E. Politzer, Application of Expert Systems to Cash Flow Analysis, Working paper, Imperial College, London (1986).

[19] P.G.W. Keen and M. Scott Morton, Decision Support Systems: An Organisational Perspective (Addison-Wesley, Reading, MA, 1978).

[20] R.K. Lindsay, B.G. Buchanan, E.A. Feigenbaum and J. Lederberg, Applications of Artificial Intelligence for Organic Chemistry: The DENDRAL Project, (McGraw-Hill, New York, 1980).

[21] J. McDermott, Building Expert Systems, in: W. Reitman, ed., Artificial Intelligence: Applications for Business (Ablex Norwood, NJ, 1984) 11–22.

[22] F.W. McFarlan, Information Technology Changes the

Way You Compete, Harvard Business Review (May/June, 1984).

[23] L.B. Methlie, On Knowledge-Based Decision Support Systems for Financial Diagnosis, in: [29].

[24] H. Mintzberg, The Nature of Managerial Work (Harper and Row, New York, 1973).

[25] L. Orman, A Multi-Level Design Architecture for Decision Support Systems, Data Base (Spring, 1984).

[26] V. Salas Fumas, Strategic Planning: Implications for the design of DSS, in: [29].

[27] E.H. Shortliffe, Computer-based Consultation Systems: MYCIN (American Elsevier, New York, 1976).

[28] R.H. Sprague, Jr. and E.D. Carlson, Building Effective Decision Support Systems (Prentice-Hall, Englewood Cliffs, NJ, 1982).

[29] A.B. Whinston and C.W. Holsapple, eds., Decision Support Systems: Theory and Applications, NATO-Asi-Series 31, Springer-Verlag (1987).

[30] K.A. Williams, Investment Decision-Making Using Fuzzy Logic, Working paper, Newcastle-upon-Tyne Polytechnic (1986).
