---
otero_id: 18787
otero_key: "6PTEHQVP"
title: "A case study of a tactical information system"
authors: "George P. Schell"
year: "1992"
journal: "Information & Management"
doi: "10.1016/0378-7206(92)90009-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# A case study of a tactical information system

George P. Schell

University of North Carolina at Wilmington, Wilmington, NC 28403, USA

Tactical information systems (TIS) are a type of decision support system. However, there are several characteristics which make them warrant separate study. They not only support the decision making process: they are able to replicate the decision maker's expertise. The characteristic of replicating decision expertise is generally reserved for expert systems. It is important to study the development of TIS for two reasons. First, they cross functional boundaries so their design must reflect the political realities of satisfying a group of users that may have conflicting interests. Second, TIS can be precursors of expert systems. They embody knowledge and are able to generate decisions that are sanctioned by the organization.

Keywords: Decision support systems, systems design, tactical information systems.

![](/api/attachments/6PTEHQVP/fulltext/images/bc314a307e435e8ef5922c6008a68f6ce2dae5bde2b8f6f6567308bd09abcab2.jpg)

George P. Schell is Associate Professor of Management Information Systems at the Cameron School of Business Administration, University of North Carolina at Wilmington. Dr. Schell holds bachelor's and master's degrees from the University of Florida and a Ph.D. from Purdue University. He has authored articles in several refereed journals and written two books. His research interests are in systems analysis and design and the implementation of large systems into senior level management.

Correspondence to: G.P. Schell, Cameron School of Business Administration, The University of North Carolina at Wilmington, Wilmington, NC 28403, USA. (919) 395-3675.

## Introduction

It has been suggested that decision support systems (DSS) lack theoretical and empirical support $[20]$ . While a number of articles and texts have been written on DSS, that opinion is not altogether unfair. The term DSS covers a wide range of applications and needs to be broken into various types that can be closely studied. The talents required to construct one type of DSS may be significantly different from the talents required to construct another.

Tactical information systems (TIS) are a subset of DSS that replicate a user's decision making process rather than merely model or support that process. They are capable of extrapolating solutions that the decision maker did not anticipate and explicitly include in the system. The power of extrapolation is a characteristic not traditionally associated with DSS.

TIS are not a variation of expert systems. Expert systems are a subset of artificial intelligence $[13,24]$ and require decision making rules to reside in a knowledge base. Those rules are selected and processed by a formal reasoning engine, such as resolution. TIS embody decision knowledge within fixed computer code, not within a knowledge base, and cannot be considered to be expert systems.

The models (decision knowledge) within a TIS represent its structured component. It also has an ill-structured component, because the validity of data used by models may be uncertain and the models may not accurately replicate the human decision process. The mixture of structured and ill-structured components implies shared decision making by the information system and its user.

TIS require hands-on use by the decision maker; a role that many of them seldom perform. Keen [17] suggested an intermediary between the user and the DSS. Culnan [7] refers to “chauffeurs” who retrieve information for users. But the use of a TIS requires intimate knowledge of the decision making process. In TIS, no intermediary exists between the user/manager and the system.

## Key features of tactical information systems

DSS have several important characteristics [6]; they aid the decision maker in ill-structured problems, possess an interactive feature, and communicate with the user via a high level dialogue. However, the requirement of an interactive component has been debated [18]. The debate will not be repeated here, except to state that the interactive characteristic is indispensable for complex decisions, because users/managers may not know all of the information they require for decision making prior to actually making the decision [14]. TIS also require these characteristics.

TIS have two additional characteristics that serve to classify them as a subset of DSS. First, part of the TIS is run in batch mode and second, the TIS replicates human decision making. TIS require access to large databases and it has been suggested that a comprehensive database is one element of a DSS [25]. Also, the important decisions addressed by TIS are not made in a single moment but are made over the course of hours or days. It would be infeasible for the user/manager to access such large databases interactively during the entire decision making process.

![](/api/attachments/6PTEHQVP/fulltext/images/ee5af2c391b73cd48e7fdf6d4229d1c330a820e1ee6059a4a5306184f5729055.jpg)  
Note: Meats may be processed iteratively.  
Fig. 1. Processing in the example organization.

Since TIS replicate decision making they are precursors to the genre of knowledge based systems $[21,22]$ known as “expert systems.” The major similarity between TIS and expert systems is that decision making expertise is codified in a manner that can be replicated by computerized systems. Like expert systems, TIS are capable of dynamic decision making. They both provide solutions to problems that the designer did not explicitly design into the computer code. Expert systems reason answers from knowledge bases using techniques such as resolution. TIS use more traditional mathematical models, such as optimization techniques and regression analysis. Although the difference between these two methods may be subtle, it is very important.

Expert systems have the ability to alter their reasoning steps based upon new facts and/or new rules in the knowledge base. They require no alteration of the inference engine. In contrast, TIS are not capable of controlling the logic used in problem solution. Their problem solving capabilities are frozen until the computer programs are modified.

## A case history

The case in this article focuses on the optimal formulation of sausage products. However, it is a mistake to believe that it is simply a management science application, where an information system was used to implement the linear program. Information systems are the mechanism that transform management science techniques into a driving force within a firm. Indeed, the 1989 Franz Edelman Award for Management Science Achievement was presented to a marketing information system [16]. Again, in 1990, the award went to an application of an information system [12].

Some steps in the development of the TIS deviate from prescribed methods of information analysis and systems design [8,28,29]. The design of the TIS example was subject to political, economic, and time constraints beyond the control of people involved in the design, and sometimes beyond the control of the organization.

The information system is “tactical” in the nomenclature of strategic/tactical/operational [3]. Strategic systems help define the broad, long-term goals set by senior management for the whole organization. Operational systems focus on reports used for control by low level management. Tactical systems address how middle management achieves the strategic goals of senior management.

The organization in this case study is a large meat processing company which slaughters animals, produces primal cuts of meat, produces “processed” meat products, and produces meat trimmings. Figure 1 depicts the major processes. Primal cuts of meat are those types of meat normally bought directly from a store: ham, pork chops, and others. These meats are not “processed” in that they are simply certain muscle groups from the slaughtered animal. Primal cuts of meat account for the vast majority of product which flows through the organization.

Processed meats are those which have been cooked, cured, smoked, blended with other meats, and/or supplemented with condiments. Although the volume by weight of processed meats is much smaller than primal cuts, the profit margins for this type of product are much larger.

Meat trimmings are the by-product of producing primal cuts and processed meat products. These trimmings may become ingredients for other products fabricated later in the production process; e.g. ham trimmings may be used in sausage. Trimmings are either used internally by the organization or sold as a commodity. Nothing is wasted in a meat processing plant, so the mathematical models enforce balancing constraints between inputs and outputs.

The TIS was designed to optimize the blending of ingredients in the production of sausage products. Such products include hot dogs, bologna, sandwich meats, and similar items. Three functional areas of the organization were involved in the decisions and conflicts between the areas was common. The model size was very large, in that hundreds of ingredients may be used for a given product and there are many constraints on the manufacture of these products. Constraints reflect governmental regulations, product quality, and production limitations. The organization learned through experience that simplified models of a few key products and ingredients did not adequately describe the production process.

The impetus for developing the TIS came from three sources. First, the organization was producing a product (red meat) for which demand was steadily decreasing. In such an environment one or more of the major producers would be forced to either go out of business or dramatically change its product line. Neither of these alternatives was acceptable to the organization. The strategic decision was made to increase the volume of its processed meat operations. The tactic to achieve this goal required more coordination and structure in sausage production: traditionally a loosely managed aspect of the business. The TIS would provide a weapon for pitting the company's sausage production operations against its competition.

People who have developed information systems which replicate the user/manager's decision processes have found that the decision making is enhanced because of the formal procedures used to codify the process [9,23]. It was felt that codifying the decision making process into models would force the critical analysis of each step. The result would be a more accurate and structured decision process.

The economic incentives were large. This was unrecognized until the organization began investigating the possibility of building the TIS. It would be devoted to processed meat operations and the organization had a firm mind-set that primal cuts (i.e., fresh meat operations) were the only economically important aspect of the business. Upon investigation, the board of directors discovered that over \$1 million per year of additional profits could be returned from the use of the TIS.

The TIS would have to cross several functional boundaries. This would benefit the firm, since the individual functional areas would have to subjugate their interests to the greater interests of the total firm. Functional area managers were reluctant to surrender control of part of their activities to what might be considered a rival area of the firm, since it (as well as the rest of the industry) was suffering from reduced demand. The TIS provided a vehicle for cross-boundary cooperation: it removed some of the stronger personalities from direct conflict.

## The least cost system: getting started

The tactical information system to be developed was named the “Least Cost System” (LCS) since its main objective was to minimize the cost of ingredients used to formulate sausage products. The name of the project did not adequately describe the scope of the problem. Since the system would make decisions that crossed functional area boundaries, it was critical to express the design in a manner that met the consensus of requirements.

The decision making mechanism had been wielded by a triumvirate in the organization consisting of members from the Sausage Department, the Operations Department, and the Quality Assurance Department. In theory, all members worked in unison to achieve the organization's goals. In fact, each unit tried to impose its own view. Changes to the status quo could be effectively pocket vetoed by any member: i.e. any

Table 1
Major components of the least cost system

II. Database
A. key data elements
B. interpolated data elements
C. product demand, raw materials supply
D. ingredient characteristics (fat, protein, etc.)
E. reports for historical analysis
F. ad hoc reports

III. Weekly Production Reports
A. optimization of all products at the plant
B. procurement reports and vendor analysis
C. material usage reports
D. formulations for the production line
E. standards for input into accounting systems

IV. Crisis Management
A. individual product tableaus
B. modification of product constraints
C. modification of ingredient characteristics
D. link to main database

member could delay its response until the opportunity that precipitated the request had passed.

The Sausage Department often desired to relax product constraints in order to reduce costs and thereby increase profit margins. The Operations Department wanted control because the scheduling of several different products required machine setup, labor scheduling, and cleaning difficulties that were not considered by the other departments. The Quality Assurance Department was responsible for assuring that products met governmental regulations; some of the regulations were obscure and could be overlooked by other departments. Development of the LCS provided a forum for each department to voice its concern and to have objective, reasonably nonpolitical input in areas that affected the operations of other departments.

Defining the problem in a form that was acceptable to all parties was difficult. It has been found that identifying a complex problem can be more difficult than solving it $[10,19,27]$ . Many persons were interviewed: senior vice presidents, workers on the production line, purchasing agents, chemists, and more. The major components of the LCS which arose from the problem definition are listed in Table 1.

An unforeseen benefit emerged during the course of determining the requirements. The models for optimizing formulations required more specific chemical information than the organization had previously gathered. Materials were tested for an array of chemical attributes. It was discovered that the quality of materials changed dramatically from one vendor to the other and even among shipments from the same vendor. The development of the TIS was the precipitating event that brought this fact to light.

The Quality Assurance Department (which performed chemical analyses) had suspected the wide variation in the past, but had no reason to act on the information. With the TIS, the implications for processing were acted upon by the organization as a whole instead of being ignored by a department that had no direct use for the information.

Once the information analysis was completed, the requirements for hardware were addressed. The secondary storage and remote terminal requirements for the LCS were substantial and normally would have been sufficient to acquire hardware dedicated to the application. However, political considerations had the greatest impact here.

The senior vice president who championed the LCS made a deal with the senior vice president to whom the Data Processing Department reported. If the Data Processing VP would support the LCS, then the champion would support earlier requests for an upgrade for computer hardware to an IBM 370/158. Although specific hardware needs of the LCS were not considered, the ally was important.

The board of directors gave tentative approval for the LCS during feasibility analysis. Final judgement was reserved until a proposal with authenticated dollar payoffs could be produced. A consultant was hired to develop models of sausage products and their constraints. The entire LCS database could not be modeled in the weeks before the next board meeting: data had to be manually input and converted into appropriate reports. The results were surprising, especially since all three members of the “triumvirate” contributed to the model and could vouch for its authenticity.

During presentations to the board of directors the consultant demonstrated economic benefits 40% in excess of those originally proposed; i.e. the LCS would increase profits by \$1.4 million per year. The benefits were based upon a three month history of material prices, availabilities, and production volumes. Benefits reflected actual operational constraints faced in the plants. Use of “live” data convinced the board that the projected benefits were accurate.

However, the board “adjusted” the economic benefits back to the originally proposed \$1 million figure. The excess 40% was credited to the actions of personnel in one functional area (the Operations Department). This saving resulted from increased understanding of the production process gleaned from developing the proposal and they would be gained even if the proposed information system was never developed.

## Development of the least cost system

TIS must be able to replicate the decision making process. They must be able to act as the agent of an absent decision maker. The LCS had to act as the agent for the decision making triumvirate, reacting to changing inputs.

Another consideration was the intense need for accurately modeling the decision making process. A DSS is a tool for its user, who may choose to ignore the results of when making the decision. However, a TIS cannot rely upon the final review of the user, since it goes beyond supporting the user to acting as the user's agent.

The literature contains numerous examples of information systems designed to improve and augment decision making that caused horrible, costly errors $[26,30]$ . A common explanation is inadequate testing of the system. Unverified models of may not even correctly represent the organization $[1,2,4]$ and users/managers may reject TIS because of a lack of confidence in the adequacy of models contained in the system $[15]$ .

Development of the prototype LCS became a key element, since it provided a concrete, common basis for examining models and reports. The triumvirate and the TIS developers thoroughly reviewed results from each iteration of the prototype. It required substantially more effort to develop the prototype than expected due to the complexity of the models and the length of time required to “deprogram” the experts.

A decision was made to develop mathematical formulations based upon product descriptions expressed in the managers' vernacular. A Fortran program was written to translate traditional formulation specifications (e.g. lean beef, ham trimmings, no frozen meats, etc.) into a format that was optimized using the linear programming package MPS III. Development of the generator allowed specification of product revisions in functional areas without requiring intervention by an information specialist.

During prototype development it is always important to take advantage of unexpected opportunities. In this case, a raw materials purchaser desired a change in the information shown on the optimal product formulations report. That document included a summary containing upper and lower price levels for each raw material that would keep the solution optimal. The purchaser's request was to add a sensitivity analysis for material volume as well as price.

The purchaser intended to make preemptive purchases. Since all major producers of sausage products made similar product lines, knowing which materials were important for his own company meant that he knew materials important to competitors. The purchaser targeted key ingredients and purchased them before competitors realized their value. By depriving competitors of key ingredients, their products became more expensive and therefore the LCS organization's product was more attractive. To implement this strategy the purchaser had to know the largest amount of materials that could be purchased before the costs of his own products were affected.

Other surprises were not flattering. Foremen on the production line had traditionally been able to question the product formulations. They occasionally found arithmetic errors in the previous system of manually derived formulations and corrected them. At their request, a blank space was left on formulation sheets that allowed foremen to manually check the arithmetic of the computer before blending products.

Deeming the foremen's request pointless would have alienated them. The request was implemented since it carried no cost and it demonstrated that the formen's concerns were seriously considered.

The need for rigorous testing of the TIS cannot be over emphasized. It is critical to perform a sensitivity analysis on the results of the entire TIS and not simply upon its separate components [5]. The TIS, like the decision maker it replicates, must be able to solve problems under new circumstances. The organization must have faith that the TIS will correctly make the new decisions based upon data that are valid but have not been observed before. A measure of the organization's faith was that it used the LCS as the accounting standards for sausage product production.

Unusual sets of data were fed to the TIS so that it would respond to unprecedented scenarios. The TIS produced sound results; even results that initially appeared odd were later found to be rational.

## Individual LCS components and performance

Use of the information system was broken into model generation, ad hoc database queries, weekly product formulations, and crisis management. The sausage operations of each plant were modeled separately. Each had similar equipment and raw materials but had differences that required separate production constraints.

The LCS was originally designed to use its own database. Several months after it was in operation, the Accounting Department completed the implementation of a company-wide general ledger system. The schema of this latter database was modified to accommodate data from chemical analyses and other data. The database for the LCS was then eliminated and LCS programs modified to access material prices, availabilities, and other facts from the new joint database. A supplementary program was developed to allow users to interface with the database using LCS menus and product terminology.

Models of plant operations were generated a few times a year when sausage formulations changed. A typical linear programming model for a plant contained approximately 8,500 columns and 2,500 rows. The matrices were not sparse, because many ingredients could be used in most products. Five to seven million database queries might be required to provide data for a plant's initial linear programming tableau.

The generation of an initial tableau required 15 to 20 minutes of CPU time and approximately two hours of wall-clock time. The program was never allowed to be run during prime computing hours because of the heavy database access. Prime time access to the database was reserved for order entry and certain financial accounting systems. Plant operation models were usually generated during the weekend.

Optimal product formulations for plants were generated weekly, because the industry generally operates on weekly prices for most materials. Materials, such as pork bellies, were commodity items and the overwhelming majority were contractually committed within a few hours after trading opened on Wednesday morning. Prices for thousands of materials had to be forecast for each weekly run.

A regression model used historical costs and other factors as the basis for initial forecasts. Next, forecasted prices and availabilities for selected materials were presented to purchasers. They were also given a copy of the previous week's regression forecast, their predictions, and the actual material prices and availabilities. They modified these based upon their judgement of the market. The revised forecasts of selected materials were used to generate the final forecast of all materials available for formulations.

Weekly database queries were only required for material price and availability, not for production constraints. The linear programming package, MPS III, saved each plant's optimal tableau and used it as the initial tableau for the next solution. Using these shortcuts, the optimal formulations for a plant were generally computed in less than 12 seconds of CPU time (about 15 minutes of wall-clock time).

A computer error or hardware failure sometimes caused one or more of the weekly plant formulations to abort. That plant's formulations would be rerun on Wednesday during prime computing hours. When the models were run during prime computing hours the wall-clock time would exceed three hours.

Managers at a plant might need to modify formulations based upon unforeseen events from one to five times a week. These reformulations were run during prime time, but there were not enough slack computer resources to resolve the plant's entire optimal formulation. The LCS dealt with this problem by generating individual models of each plant's products at the same time the model of the entire product line was generated. These individual product models were accessed by an interactive program called “crisis management.”

## Crisis management

The development of a TIS must compensate for any constraint on prime time computer resource use. The practical constraint in this case study was not raw CPU power but access to the database without disrupting other vital applications. Model decomposition is one practical way to address this problem.

A crisis could occur because of the delay of a truck carrying necessary materials, equipment failure, or some other unexpected situation. A production delay of minutes could cost thousands of dollars. The organization decided that certain persons within each plant would be trained to use the crisis management feature, since even the delay of placing a phone call to the headquarters office could be costly.

The LCS developed crisis management models for individual products (reflecting problem decomposition) at the same time that the comprehensive model of all products was created. Each decision period (weekly) the database was accessed to produce a file of current material prices and availabilities. Since only the current decision period was included in the file, it was small enough to be quickly processed. A separate computer program was developed to optimize the crisis management models.

The full range of decision making prerogatives were available in the crisis management mode. The decision maker could interactively modify material prices and availabilities for any product, as well as add, modify, or delete product constraints. Many managers took advantage of this “hands on” feature to simulate various production scenarios.

After several months of use, some managers were able to discern patterns that led to economic opportunities. By experimenting with the crisis management feature, they were able to learn which situations led to opportunities. Some managers actively attempted to position themselves in situations where their expertise with crisis management would give them an advantage.

## Unanticipated uses

The mangers in charge of sausage operations at two of the plants became proficient in the crisis management feature to simulate various raw material scenarios. They generally concentrated their efforts on materials from plants where production operations had unexpectedly changed.

For example, one week the manager in charge of sausage operations at one plant found out that a significant portion of hogs to be slaughtered at a supplier's plant were unusually small. This would result in much leaner trimmings. However, trimming prices were based upon industry standards for fat, protein, and moisture contents so these trimmings would be a bargain.

This information was not sufficient, because competitors also knew that unusually lean trimmings would come from the supplier's plant. Crisis management was used to reformulate a few critical products. From these the manager knew the amount of lean trimmings that he should buy, the price range he would be willing to pay, and other orders for trimmings that would need to be canceled or renegotiated.

The TIS provided knowledge of the total impact on production to give an advantage over competitors. The profit gained by this manager's actions was recognized by headquarters staff and other plants in the organization. Proficient use of the crisis management feature became a criteria for promotion from plant operations to headquarters. Plant personnel used the crisis management feature on a regular basis to seek economic advantage from unexpected changes in material prices and availabilities.

The LCS was occasionally used to support strategic decisions, such as the change of the product mix at a plant. The LCS was used to simulate product strategies that would impact the set of products at a plant. For example, a new product was developed that showed great promise: it commanded a high profit margin but required select raw materials. The organization had to assess the economic impact of dramatically increasing the production volume of the premium product.

A fictitious plant model was generated. It was run through historical data (prices, availabilities, etc.) for the previous 13 weeks except that the production levels for the premium product were increased to the proposed volume. Although the new product showed excellent profitability, the impact on the collective product line was negative.

## The LCS thinks for itself

A computer program cannot generate a problem solution unless all of the prerequisite facts and algorithms are coded. However, the complexity of facts and algorithms may produce so many possible combinations that the user fails to consider many of them because he or she has a mind-set that those solutions will never be practical. The system may extrapolate an unanticipated solution and therefore appear intelligent. The following is an example of the LCS's apparent intelligence.

Chicken meat is a nontraditional ingredient in hot dogs. Such hot dogs have been produced for some time but they have been a specialty item aimed at consumers who avoid red meat products. Chicken meat may be included in hot dogs as an ingredient if the amount is consistent with package labeling.

The LCS seemed to exhibit independent thought when formulations in certain plants suddenly called for a drastic increase in the amount of chicken meat in certain hot dog formulations. It took considerable research to explain why these unusual formulations were accurate.

At that time the industry was slaughtering fewer hogs than usual which led to higher prices for pork trimmings. The conventional wisdom of people in the plants held that since pork prices had increased, the formulations would call for reduced amounts of pork in the product. Since product labels listed pork before chicken, there would be even less use of chicken meat.

The LCS had discerned a pattern unrecognized by its users. The hot dogs contained beef as well as pork and chicken. Much of the beef trimmings used were frozen at the suppliers' plants so that they would preserve longer. As the price of pork trimmings rose, the relative price of beef trimmings fell but that created an unusually large portion of frozen materials in the formulations. The plants with the unusual formulations were not designed to utilize such high proportions of frozen materials.

Chicken meat was not a frozen ingredient and was being substituted for some of the frozen beef. The result was that chicken ingredients were being used to satisfy production constraints that had not been binding in the past. As a result of this experience, LCS users began to view the LCS as if it had a personality.

## Summary

Tactical information systems are an important subset of decision support systems. Their output can be used as a surrogate for the user/manager's instructions to subordinates. Instead of simply supporting the decision making process, TIS can replicate the process.

TIS tend to cross functional area boundaries in an organization. Users are managers who are responsible for implementing the goals of senior management. Users in different functional areas may have conflicting requirements from the system and these conflicts may require political remedies. Political considerations are thus important in the development of TIS since it must produce organizationally sanctioned decisions.

TIS must also cross layers of management in the firm. A complex decision making process is not completely contained in one manager or even one functional area. TIS decisions are addressed by higher level management, but the decisions descend through layers of management before they are implemented. These political realities impact TIS design.

A TIS establishes authority by the users' faith in its encoded decision making process. The belief that the user's decision making criteria are embedded in the TIS is a prerequisite for its acceptance.

The TIS must be able to make decisions that do not require the final approval of the user. It is necessary that the TIS be robust enough to handle unusual variations of the problems it is designed to address. The TIS should be thoroughly tested to provide evidence of robustness.

The TIS will require complex models and substantial database access and therefore significant computing resources. Since the period of problem solving is typically long (such as days) and many aspects of problem solution do not require an interactive attribute, the design of the TIS should be divided into batch and interactive sections.

The crisis management feature was developed to allow managers interactive use of the LCS to accommodate unforeseen situations. It required that key elements of the TIS be designed in parallel, one side for batch and one for interactive processing. The functionality of the system must be maintained at the interactive level. That is, the interactive feature must not be a pale copy of the comprehensive system.

## References

[1] Ackoff, Russell L. Management misinformation systems. Management Science, Vol. 14, No. 4 (December 1967) B147–B156.

[2] Ackoff, Russell L. Management In Small Doses. New York, Wiley, 1986.

[3] Bartol, Kathryn M. and Martin, David C. Management. New York, McGraw-Hill Inc., 1991, 161–162.

[4] Bekey, G.A. Models and reality: some reflections on the art and science of simulation. Simulation, Vol. 29, No. 5 (November 1977) 161.

[5] Blanning, R.W. A relational framework for model management in decision support systems. DSS-82 Transactions (1982) 16–28.

[6] Bonczek, Robert II., Holsapple, Clyde, and Whinston, Andrew. Foundations of Decision Support Systems. New York, Academic Press, 1981.

[7] Culnan, Mary J. Chauffeured versus end user access to commercial databases: the effects of the task and individual differences. MIS Quarterly, Vol. 10, No. 3 (September 1986) 289–302.

[8] Davis, Gordon B. and Olson, Margrethe H. Management Information Systems: Conceptual Foundations, Structure, and Development, 2nd Ed. New York, McGraw-Hill, 1985, 570–591.

[9] Dhar, Vasant. On the plausibility and scope of expert systems in management. Journal of Management Information Systems, Vol. 4, No. 1 (Summer 1987) 25–41.

[10] Dillon, J. Problem finding and solving. Journal of Creative Behavior, Vol. 16, No. 2 (1983) 97–111.

[11] Edmunds, Robert A. The Prentice Hall Guide to Expert Systems. Englewood Cliffs, New Jersey, Prentice Hall, 1988.

[12] Fetter, Robert B. Diagnosis related groups: understanding hospital performance. Interfaces, Vol. 21, No. 1 (January–February 1991) 6–26.

[13] Firebaugh, Morris W. Artificial Intelligence: A Knowledge-Based Approach, Boston, Boyd and Fraser Publishing, 1988, page 335.

[14] Fowler, F. Parker, Jr. The executive intelligence system as a design strategy. MIS Quarterly, Vol. 3, No. 4 (December 1979) 21–29.

[15] Fuerst, William L. and Martin, Merle P. Effective design and use of computer decision models. MIS Quarterly, Vol. 8, No. 1 (March 1984) 17–26.

[16] Gensch, Dennis H., Aversa, Nicola, and Moore, Steven P. A choice-modeling market information system that enabled ABB Electric to expand its market. Interfaces, Vol. 20, No. 1, January–February 1990, 6–25.

[17] Keen, Peter G.W. Interactive computer systems for man-

agers: a modest proposal. Sloan Management Review (Fall 1976) 1–17.

[18] Keen, Peter G.W. and Scott Morton, Michael S. Decision Support Systems: an Organizational Perspective. Reading, Massachusetts, Addison-Wesley, 1978.

[19] Mover, R.E. The psychology of how novices learn computer programming. ACM Computer Surveys, Vol. 13, No. 1 (March 1981) 121-141.

[20] Meador, C. Lawrence, Guyote, Martin J., and Rosenfeld, William L. Decision support planning and analysis: the problems of getting large-scale DSS started. MIS Quarterly, Vol. 10, No. 2 (June 1986) 159–177.

[21] Nilsson, Nils J. Principals of Artificial Intelligence, Palo Alto, California, Tioga Publishing Co., 1980.

[22] Rich, Elaine. Artificial Intelligence, New York, McGraw-Hill, 1983.

[23] Stone, Jeffrey. Commercial AI trends seen at AAAI-87. AI Magazine, Vol. 8, No. 4 (Winter 1987) 93–95.

[24] Turban, Efraim. Decision Support and Expert Systems, New York, Macmillan Publishing Co., 1988, page 346.

[25] Turban, Efraim and Watkins, Paul R. Integrating expert systems and decision support systems. MIS Quarterly, Vol. 10, No. 2 (June 1986) 121–136.

[26] Weber, E. Sue and Konsynski, Benn R. Problem management: neglected elements in decision support systems. Journal of Management Information Systems. Vol. 4, No. 3 (Winter 1987–88) 64–81.

[27] Watson, Hugh J. and Marett, Patricia Gill. A survey of management science implementation problems. Interfaces, Vol. 9, No. 4 (August 1979) 124–127.

[28] Whitten, Jeffrey L., Bentley, Lonnie D., and Ho. Thomas I.M. Systems Analysis and Design Methods. St. Louis, Times Mirror, 1986.

[29] Yourdon, Edward. Modern Structured Analysis. Englewood Cliffs, New Jersey, 1989, 78–94.

[30] Zmud, Robert W. Individual differences and MIS success: a review of the empirical literature. Management Science, Vol. 25, No. 10 (October 1979) 966–977.
