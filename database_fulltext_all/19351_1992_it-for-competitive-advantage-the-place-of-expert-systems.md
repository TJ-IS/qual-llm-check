---
otero_id: 19351
otero_key: "H7KJ79JC"
title: "IT for competitive advantage: the place of expert systems"
authors: "Paul N. Finlay"
year: "1992"
journal: "The Journal of Strategic Information Systems"
doi: "10.1016/0963-8687(92)90025-r"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# IT for competitive advantage: the place of expert systems

Paul N. Finlay

Loughborough University Business School, Loughborough University of Technology, Loughborough, Leics LE11 3TU, UK

A somewhat different view of expert systems is taken in this paper. A comparison between expert systems and 'conventional' fourth generation systems leads to a grouping of the advances attributed to expert systems into four classes: similarities masked by the different terminologies used; developments associated with expert systems that are not new; the unfolding IT scene; and those developments that can truly be associated with expert systems. The conclusion is that there is little new about expert systems. The contribution that expert systems might be expected to make to an organization's competitive position is then discussed within the more general context of IT as a whole. The contribution hinges on the sort of task that the expert system is supporting or carrying out. The conclusion is that it is only for novel/unique situations that IT can provide competitive advantage and this is rarely the province of expert systems.

Keywords: expert systems, competitive advantage, decision support systems

The changes in information technology (IT) since the first working computers were built around 50 years ago have been enormous. These changes have not taken place at a uniform rate; rather there have been waves of change — termed ‘generations’ — in which a considerable advance has been followed by a period of exploitation and development. The generations are identifiable in terms of both hardware and software (see Table 1), although the hardware and software advances have not necessarily kept in step with one another.

The major organizational breakthrough came with third generation software, offering the development of systems that, inter alia, allowed for a fairly clear separation between logic and data models. The fourth generation software extended the developments into specific applications, offering enhanced ease of use and graphics: the spreadsheet is perhaps the best known example. Particularly significant were the advances in database management which made possible the efficient storage and accessing of large volumes of data.

One of the fifth generation's most pertinent developments for management appears to be expert systems (ES). An ES is a computing system that embodies organized knowledge concerning some specific area of human expertise, sufficient to perform as a skilful and cost-effective consultant $^{1}$ . Looked at simply, the goal for an ES is either to mimic an expert — for example, to mimic an experienced professional such as a doctor or a production manager — or to support the expert.

Some observers see enormous changes resulting from the use of ES. Moutinho and Paton $^{2}$ enthusiastically quote sources as stating: ‘... PC-based marketing assistants will replace 50% of all marketing consultant activity by 1990’. This was an exceedingly bold statement for the authors to make — making it as they did in summer 1988. To a large extent this optimism hinges on how the authors defined ES. Their list of ES included systems for automated forecasting, for capturing data from questionnaire forms and one for producing checklists. With this very wide perspective, anything that is user-friendly would seem to warrant the term ‘ES’.

Table 1. Generations of IT

<table><tr><td>Generation</td><td>Hardware</td><td>Software</td></tr><tr><td>1</td><td>Valves</td><td>Machine code</td></tr><tr><td>2</td><td>Transistors</td><td>Assembler</td></tr><tr><td>3</td><td>Integrated circuits</td><td>High-level languages (e.g. Basic, Fortran, Cobol, Pascal)</td></tr><tr><td>4</td><td>Large-scale integration</td><td>Application-specific packages (e.g. spreadsheets, database products)</td></tr><tr><td>5</td><td>Parallel processing Networking Very large-scale integration</td><td>Expert systems shells, environments</td></tr></table>

During the 1970s, great emphasis was placed on the success of the medical ES Mycin $^{3}$ . Over a decade has elapsed since this initial success and there is little evidence to show for any substantial subsequent advance. Why should this be? Medicine is an area of apparent shortage of experts, expert training is costly, health care is ever more expensive and the patients ever more demanding and, significantly, any ES would be usable in many locations, in some cases worldwide. The failure of the medical world to build on the early success of ES, when there would appear to have been a great impetus to push on with developments, should provide a warning that there may be grave problems in the development and acceptance of ES.

## Components of expert systems

Since a major goal for an ES is to mimic an expert, the expert's knowledge must be available within the ES. His/her factual knowledge is held within a knowledge base. Additionally, the ES must also be able to mimic the procedure by which the expert reasons with the factual knowledge — to carry out inference. The part of the system that performs these inferences is termed the inference engine.

The knowledge base and the inference engine are the principal components of an ES. A further component is a natural language interface that allows the users to interact with the computer in a ‘natural’ manner — in their own natural language and using any jargon that they might use when normally consulting an expert. In a full ES it would be expected that the system would be able to give an explanation to the user; for example, of how it arrived at a particular answer or why a particular question is being asked.

Further components are a knowledge-refining program, giving the person maintaining the ES the ability to alter the knowledge base as the knowledge improves or as the scope of the system is widened, and the systems software that provides the infrastructure within which the knowledge can be coded, and which provides the facilities that ease systems development. This software may be an ES language, a shell or an environment.

Systems built using fourth generation tools have a very different feel about them. Panko $^{4}$ considers that DSS combine tools from three generic application areas: data management, analysis and presentation. Building on this approach, MSS are viewed as being composed of a data model, a logic model and the presentational (human-computer) interface between the user and the computer containing these models. A simple spreadsheet MSS is shown in Table 2. The logic model consists of the relation by which a value for revenue is calculated: the data model consists of the values for sales and price for three time-periods. The interface may display a range of outputs: the one shown is for the values of sales and those for revenue which have been calculated.

Comparing this extremely simple example of a fourth generation system with the description of the components of an ES given above would suggest that there is little in common. There do not appear to be the equivalents to the knowledge base, inference engine, shell and environment, natural language interface, explanation program, and knowledge-refining program.

Table 2. Elements of a spreadsheet model

<table><tr><td rowspan="2">Logic model</td><td colspan="4">Sales = 30 × (competitors&#x27; price/own price)</td></tr><tr><td colspan="4">Revenue = sales × price</td></tr><tr><td rowspan="2">Data model</td><td>Own price</td><td>5</td><td>6</td><td>6</td></tr><tr><td>Competitors&#x27; price</td><td>5</td><td>7</td><td>8</td></tr><tr><td rowspan="2">Output</td><td>Sales</td><td>30</td><td>35</td><td>40</td></tr><tr><td>Revenue</td><td>150</td><td>210</td><td>240</td></tr></table>

However, a more thoughtful enquiry might indicate a fair measure of similarity.

## Aims

The aim here is to help manage expectations as regards the contribution that expert systems might be expected to make to an organization's competitive position. It does this in two major sections. In the first section the 'newness' of ES is explored, with ES compared to systems built around such fourth generation IT tools as the spreadsheet, financial planners, PERT and database products. The second section examines where the use of information technology and specifically ES is likely to provide competitive advantage.

## Is there anything new about ES?

It is convenient to bring together the discussion concerning the newness of ES under four headings: the terminology of fourth generation systems and ES, apparent developments in ES that are not new, developments that are simply part of the unfolding IT scene and being applied in many areas of IT, and finally those developments that appear to be truly new and unique to ES. These are summarized in Table 3.

## Fourth generation and ES terminology

One reason why fourth generation systems and ES seem so different is due to the different nomenclature used by the workers in the two fields. Systems with any significant measure of complexity in their logic models have traditionally been developed by management scientists. Systems where the complexity lies in the data modelling have traditionally been developed by computer scientists. This in itself has led to two different terminologies being developed, and the problem has been further compounded by information scientists and the introduction of their terms.

The most often used terms with both fourth generation systems and ES are summarized and compared in the first section of Table 3.

In ES parlance, the area of expertise covered by an ES is termed the ‘knowledge domain’, or simply the ‘domain’. The fourth generation systems builder would refer to this as the ‘range of application of the model’. Downloading the knowledge from the expert and placing it into the computer is termed ‘knowledge engineering’ by the ES professional, ‘modelling’ by the builder of a fourth generation system.

Knowledge may be regarded as any construct or fact about the real world that is being modelled. Clark and Staunton $^{5}$ view IT as embodied knowledge. The builders of knowledge-based systems recognize three types of knowledge $^{6}$ : factual knowledge, inductive knowledge (the rules of inference) and procedural knowledge $^{7}$ (also termed ‘metaknowledge’).

Table 3. Categorization of ES developments

<table><tr><td colspan="2">a. Terminology of fourth generation systems and ES</td></tr><tr><td>Fourth Generation Systems</td><td>Expert Systems</td></tr><tr><td>Range of application of the model</td><td>Domain</td></tr><tr><td>Modelling</td><td>Knowledge engineering</td></tr><tr><td>Modeller</td><td>Knowledge engineer</td></tr><tr><td>Logic</td><td>Knowledge</td></tr><tr><td>Logic model</td><td>Knowledge base</td></tr><tr><td>Data</td><td>Factual knowledge</td></tr><tr><td>Data model/database</td><td>Data base</td></tr><tr><td>Judgemental relation</td><td>Heuristic</td></tr><tr><td>Relation</td><td>Rule</td></tr><tr><td>Variable</td><td>Attribute</td></tr><tr><td>Entity</td><td>Object</td></tr><tr><td>Record</td><td>Frame</td></tr><tr><td>Field</td><td>Slot</td></tr><tr><td>Value</td><td>Value</td></tr><tr><td>Designer</td><td>Designer</td></tr><tr><td>Package/MSS generator</td><td>Shell/environment</td></tr><tr><td>Computer</td><td>Inference engine</td></tr><tr><td colspan="2">b. Apparent ES developments that are not new</td></tr><tr><td colspan="2">Forward chaining</td></tr><tr><td colspan="2">Frames</td></tr><tr><td colspan="2">Declarative programming</td></tr><tr><td colspan="2">Inference procedures per se</td></tr><tr><td colspan="2">Inexact reasoning</td></tr><tr><td colspan="2">c. The unfolding IT scene</td></tr><tr><td colspan="2">Improved technology</td></tr><tr><td colspan="2">Move to end-user computing</td></tr><tr><td colspan="2">‘user-friendly’ interfaces</td></tr><tr><td colspan="2">self-documentation</td></tr><tr><td colspan="2">more done by machine</td></tr><tr><td colspan="2">application-directed software</td></tr><tr><td colspan="2">Less integrated structures</td></tr><tr><td colspan="2">separation of data from logic</td></tr><tr><td colspan="2">separation of input from output</td></tr><tr><td colspan="2">More ways of representing knowledge</td></tr><tr><td colspan="2">d. ES developments</td></tr><tr><td colspan="2">Software (languages, shells and environments)</td></tr><tr><td colspan="2">Explanation programs</td></tr><tr><td colspan="2">Separation of procedural knowledge from content knowledge</td></tr><tr><td colspan="2">Backward chaining</td></tr><tr><td colspan="2">Rule induction</td></tr><tr><td colspan="2">Deductive inferencing procedures</td></tr></table>

Factual knowledge is simply data, if the term 'data' is not restricted to cover only numerical quantities. Referring to the spreadsheet model of Table 2, factual knowledge is the knowledge held in the data model — the values of the prices. Inductive knowledge is knowledge about how to reason with the data to produce further factual knowledge: in the example this induction is represented by the relations in the logic model. Note that sometimes these relations are definitional (such as revenue = sales × price), sometimes they are judgemental (such as sales = 30 × [competitors' price/own price]). Judgemental relations are termed heuristics or 'rules of thumb' in ES parlance.

ES builders use the term ‘rule’ (or ‘production rule’) where the fourth generation systems fraternity tend to use the term ‘relation’ or ‘relationship’. Interestingly, the financial modelling package FCS $^{8}$ has for 20 years used the term ‘rules’ for the relations in a logic model.

The concept of a set of rules or relations in the logic model of a fourth generation system is identical to the concept of the knowledge base of ES.

ES designers prefer the term ‘object’ where the fourth generation system designer would use the term ‘entity’, and the term ‘attribute’ (as do database designers) where management scientists use the term ‘variable’. As discussed below, the frame representation is very similar to that used for many years in database design, with the term ‘record’ used instead of ‘frame’ and ‘field’ used instead of ‘slot’.

ES builders make use of software tools called shells. A shell is software that provides a suitable framework within which knowledge can be held and manipulated: the shell itself is empty of knowledge. This is exactly the same situation with many forms of software used for fourth generation systems development: specifically, spreadsheets offer an empty matrix with simple manipulatory facilities. Shells are simply another form of software, on a par with such packages, and the terms package and shell are used in an identical way.

## Apparent ES developments that are not new

Inference is the process of drawing a conclusion from a premise. The fourth generation system of Table 2 was doing just that when 'sales' was derived from the mathematical relations. Both fourth generation systems and ES need some form of inferencing mechanism.

The inference engine of an ES takes the rules that define how the expert processes his/her factual knowledge and interprets them as appropriate. The engine is providing a control structure to enable decisions to be taken on what rule to apply next. Conventional programs have a large sequential element to them and the programming is termed procedural. By contrast, ES programs seek to be what are termed declarative: the knowledge is simply stated within the software and the computer interprets it as appropriate, following on from the data input and the results obtained at earlier stages in the use of the system.

However, the difference between fourth generation systems and ES is not as marked as this brief description might suggest, since some fourth generation systems are fully declarative. Much software developed for the well-known management science technique of simulation is declarative, with activities dynamically determined depending on inputs and the (random) determination of consequences. Similarly, linear programming packages take in declarative statements concerning the constraints of the problem, allowing the software to determine how and when each statement should be interpreted. The financial planning package System-W $^{9}$ has, since the early 1980s, allowed a developer of a financial planning system to insert rules in any sequence, allowing the most appropriate sequence of rule firings to be determined 'by the computer'.

The inference engine can work in either forward chaining or backward chaining mode or both. Forward chaining occurs when data is collected and results determined from them: it is simply a new term for what has been the norm in computer programs for many years. Continuing with Table 2, the system receives data on prices and moves forward to calculate the sales and then the revenue. Generally this progress is determined through following an algorithm and thus differs from the way an ES would move forward depending on the values of variable at the time of execution. However, both of the management science techniques already mentioned (linear programming and simulation) would execute instructions dynamically as determined by the values of variables in a manner very close to that in an ES.

There is a range of techniques available to the ES developer for eliciting knowledge from the expert (see, for example, Turban $^{10}$ ). With the exception of rule induction (see a later section) all have been in use for many years by psychologists. Most revolve around interviewing the expert and using techniques such as the laddered grid, card sort, repertory grid and protocol analysis to structure the expert-interviewer interaction. The process of knowledge elicitation has been identified by researchers and practitioners $^{10}$ as the bottleneck that most constrains ES development.

As well as shells discussed in the previous section, there are also ‘environments’ for building ES. These are shells enhanced with additional facilities such as editors and graphics to allow for the easier building of complete systems. These have their parallel in the software available to develop systems such as executive information systems and software such as Express $^{11}$ . Thus each type of software available for ES development (basic languages such as LISP, shells and environments) has its conceptual parallel in fourth generation systems.

A contrast often cited is that ES deal largely with heuristics and seldom with mathematical relations whilst the reverse is the case in fourth generation systems. Whilst on balance this difference undoubtedly exists, it is a difference in emphasis. Fourth generation systems do contain heuristics although they are called judgemental relations, and ES often need to contain mathematical relations to keep the size of the knowledge base to manageable proportions.

Production rules and frames and the object-attribute-value triplets are by far the commonest ways of representing knowledge in ES: they differ very little from the common ways of representing knowledge in fourth generation systems.

A feature of frames is that the slots may be used to accommodate instructions rather than simply data. In some respects this is a throwback to an earlier age of programming in which the logic and data were held together. The frame approach is very similar to that of object oriented programming that is now finding application in the development of systems that are not ES. Object-oriented programming and frame-based ES offer ‘inheritance’ — the facility for a ‘child’ to inherit the ‘parents’ characteristics.

One of the features claimed for ES is that they are able to deal with inexact reasoning, and that this is a revolutionary development. This view fails to take into account the use that has been made of probability and statistical theory over many years by statisticians and management scientists.

There are four main ways in which inexact reasoning has been dealt with in ES. The first is through the direct application of Bayesian statistics, an approach that has been in use for decades. The second way allows an expert to express his/her views in an inexact fashion, using terms such as 'likely' and 'possibly', associate these terms with numerical values 'behind the scenes' and subsequently to manipulate them using the conventional rules of probability. This approach lies behind the fuzzy logic espoused by Zadeh $^{12}$ .

The third way of dealing with inexactitude is to explicitly write into the knowledge base the inexact relations. In this formulation a rule might be written as:

If it is likely that new competitors will enter the market OR it is quite possible that raw material prices will rise THEN it is very likely that revenue will fall.

The fourth way of representing inexact reasoning is through the use of confidence factors $^{3}$ . This is new and is discussed in a later section.

## The unfolding IT scene

There are several trends that have been in evidence from the beginnings of business computing. The first is improving technology, seen most recently in colour displays, graphics, higher processing speeds and much greater storage capacities. All these technological developments have found application in fourth generation systems.

The second major trend is the move towards end-user computing, necessitating user-friendly interfaces, self-documentation of programs and software that is nearer the application than to the machinery. Put another way, there has been a consistent trend of shifting the boundary between what the computer does and what the human does, getting the computer to do ever more.

The third major trend is towards less integrated structures. Early computer programs combined the logic and data together in one program. The logic and data were then separated, with the data put into separate files. This process continued with database developments, which had the attraction of separating the form of the outputs from the inputs, allowing great flexibility in information reporting. (Interestingly however, object-oriented programming is a move towards more integrated structures.)

The fourth trend is that there has been a consistent move to represent knowledge in different ways: for example, knowledge representations are now available in the form of spreadsheets, decision trees, graphs of many forms, icons, pictures and engineering drawings.

## ES developments

There are some developments that can be ascribed specifically to ES. New software has been developed to handle the type of knowledge the experts often have, particularly metaknowledge, which can claim to be a property of ES not present in fourth generation systems. Although inference itself is not new, ES exhibit a more refined deductive logic than do fourth generation systems.

The explanation programs of ES are a new departure. There is no real equivalent in fourth generation systems: the nearest things are routines to check for input errors and the assistance provided through help facilities. Where explanation is needed, it has been one of the roles of an intermediary to understand the system and interpret its output for the decision maker. In this regard, intermediaries were part of the fourth generation system, and it was they who provided any explanation that might be required. Interestingly, the financial planning package Javelin $^{13}$ has the facility for showing its rules and the path whereby a variable is calculated from the sequence of values obtained by other rules. This bears a rudimentary similarity to the explanations automatically offered by ES shells and environments.

The separation of procedural knowledge from content knowledge may be considered a new development (pace LP, simulation and financial modelling software) since it is so strongly part of ES. The same can be said of backward chaining.

Rule induction is a new development in which the expert is asked to provide a set of cases he/she has dealt with. These examples are then analysed by computer and a set of rules are identified that best explains the expert's conclusions from the set of cases. Although it is a new approach, it has many conceptual similarities to discriminant analysis.

A novel way of representing inexact reasoning is through the use of confidence factors as was done with Mycin $^{3}$ . This approach does not rely on classical statistical theory. Confidences that the expert has in the elements of the content knowledge are combined in an empirical way to form the confidence in the inferred knowledge. Although the method of combination has commonsense appeal, it is worrying that it has no theoretical standing.

ES that maintain their own knowledge base would certainly be an enhancement on fourth generation systems.

## Interim summary and discussion

Superficially, ES and fourth generation systems appear to have little in common. However, an examination of the features of ES and fourth generation systems reveals that the two types of system exhibit many common characteristics. In terms of content the difference between the two types of system is primarily one of emphasis in the employment of these features: for example, both are likely to include heuristics and textual data and both are likely to include mathematical relations and numerical data, but with many more heuristics in an ES and many more mathematical relations in a fourth generation system.

Many developments that appear in ES and so-called ES are developments that have found expression in fourth generation systems and form part of the general development in end-user computing and end-user involvement in computing. Specifically, ES software should be regarded as just another form of systems generator, one that allows one type of (predominantly, non-mathematical) knowledge to be readily handled. In this sense ES software can be considered as a productivity tool rather than a means of allowing something to be done that could not have been done at all. ES provide better representations of some form of knowledge since they divorce the system more from the computational mechanisms than is customary. This separation is part of the general trend in computing.

The main advance offered by ES is in the form of deductive inferencing that many ES shells support. The choice of suitable applications for ES is rather restrictive (see, for example, Waterman $^{14}$ ): in particular one criterion is that 'the task is not poorly understood' and that possible outcomes need to be known before an ES can be made operational. Knowledge elicitation techniques remain rather rudimentary and thus ES domains chosen for practical application are unlikely to be complex. Little substantially new in the way of handling probabilities is evident.

## IT and competitive advantage

In order to answer the question of whether ES will provide competitive advantage it is important to consider first the contribution that IT can make to an organization. To do this it is necessary to look at the tasks that organizations are performing and at the technological environment within which they are operating.

## Structured and ill-structured tasks

Simon $^{15}$ and Dermer $^{16}$ have looked at activities undertaken in business and categorized them into structured and un- or ill-structured activities. (In reality there is a continuum.) Structured activities are repetitive and routine — definite procedures have been worked out for handling these situations. Thus, structured activities can be well defined and nowadays mostly are. This definition has been achieved through professional standards (accountants and engineers are in the forefront here) and because many activities, such as order processing and stock control, can only feasibly be performed in a few well defined ways.

## Need for a wider analysis — the technological environment

An organization can be considered to operate within a competitive arena defined by itself and its competitors $^{17}$ . This competitive arena is itself part of an industry involving customers and suppliers. The whole industry can be considered as operating within a wider environment, whose dimensions are generally known in strategic management circles by the acronym PEST (Political, Economic, Social and Technological). A PEST analysis is a determination of how events and trends in these four dimensions affect the industry under study. The technological dimension has a particular significance because developments in IT are overwhelmingly coming from outside the organizations that are using their offerings. Whilst this occurs in other fields, it is seldom as marked as in the case of IT.

In a recent paper Cragg and Finlay $^{18}$ have characterized this environment as a global marketplace with many suppliers, offering many powerful, relatively cheap, ‘robust’ and user-friendly products with information on these products easily and usually freely available.

## IT and structured activities

The consequences for structured activities in an environment where this structure is apparent is that it is relatively easy for IT providers to know what to provide, generally for many customers, and thus to spread development costs over many sales. Thus products are cheap and it is easily feasible for organizations to acquire the appropriate IT capability. Thus sustainable competitive advantage through the use of IT with structured activities is only likely to arise in exceptional circumstances. The only known cases are those where an organization was first and kept the opposition out, if only for a short time (see, for example the much publicized cases of American Hospital Supplies and American Airlines $^{19,20}$ ).

However, it may be argued that competitive advantage can arise through the use of these tools, i.e. through the information that is produced. However, given the ‘obvious’ advantage of obtaining the technology and the ‘obvious’ way of using it and given that advice is freely available about how to use it, this would appear doubtful. In such circumstances all organizations in the competitive arena will use the technology with the lion’s share of the rewards accruing to the IT providers in the technological environment. An exception may occur in the case of diversified organizations (see below).

## IT and ill-structured situations

The characteristics of ill-structured situations is that they have not before been encountered in exactly the same form, and the discussion about ways of proceeding includes a large element of judgement: no prescription or recipe exists by which to proceed. The situation as regards the industrial environment is the same as for structured activities except for one very special and important factor — the IT industry in this case is supplying much less in terms of help: it is supplying the shells and frameworks which the organization can use as it sees fit.

With ill-structured activities much of the value is being added by the organization, because it is specific to the organization. With an organization inputting more of the value to IT than it is able to do with structured activities, it should reap the rewards.

Thus the creative challenge facing many organizations is to determine how to support ill-structured areas. Any solution is more likely to centre on the effective use of information that is unique to the organization rather than on IT (which generally is not).

## IT and the diversified firm

Porter $^{17}$ believes that the only value that a diversified firm has over the single product/service organization is the synergy that it can obtain from the diverse activities. Porter and Millar $^{21}$ argue that information can enable latent synergies to be realized. To quote, 'Careful management of linkages is often a powerful source of competitive advantage because of the difficulty rivals have in perceiving these linkages and in resolving trade-offs across organizational lines' (authors' emphasis). Rockart and Short $^{22}$ take a complementary view, arguing that IT's most important role is allowing firms to manage organizational interdependence. However, they do not go as far as do Porter and Millar $^{21}$ who see IT as enabling new and innovative lines of synergy to be developed, rather than simply managing diversity better. Here again is the case of the use of information being important, and with the organization itself adding value, not the purveyor of IT.

## Expert systems and competitive advantage

The foregoing discussion has indicated that it is in ill-structured decision areas where competitive advantage from the use of IT may lie. A feature of ill-structured decision making is the reliance on soft information. Soft information may be defined as information that lacks objectivity, and is generally qualitative. Brookes $^{23}$ has pointed out a number of problems that arise in efforts to build strategic DSS that can handle soft information. These he listed as:

\- its access and indexation is likely to be difficult;

● its existence is often not known to those who need it;

\- its owners often place tight constraints on its distribution;

\- its interpretation is intimately linked to the context in which it is received;

\- it tends to have a very short lifespan.

Additionally, it is generally the case that ill-structured decision making takes place within a context of high uncertainty. A matching of Brookes's information requirements within such a context with those associated with the feasible domains for ES applications discussed previously, shows that the correspondence is slight. This in itself suggests that the application of ES to ill-structured situations, and thus their contribution to competitive advantage, is unlikely in the foreseeable future.

## Implementation of ES

There is some evidence to support this view. Mingers and Adlam $^{24}$ have analysed the state of ES development and usage as indicated by published articles. They surveyed journals, government reports, conference proceedings and books published over the period 1984–88. They uncovered around 1000 articles. Analysis showed only 10 ES that could classify as 'real systems in use'; all the others were either prototypes or experimental systems. The review by Mingers and Adlam is not conclusive. That few working systems were found described in the literature does not necessarily mean that such systems do not exist: it could be that commercial confidentiality prevents the publication of successful cases. However, this embargo on publication would not be expected for ES in the public domain, or those which were funded by government departments.

On the other hand there is considerable evidence of ES finding application in business $^{25, 26}$ . These apparently conflicting findings arise because what appears to be happening is that the advocates of ES have been able to do two things at the same time. First, they have been able to capture the intellectual ‘high ground’ by writing and talking about systems that will be as good as if not better than the best expert, about arcane knowledge engineering and inexact reasoning.

Table 4. ES development cost and timeframe

<table><tr><td>Size of system</td><td>Type of system</td><td>Cost ($US 103)</td><td>Time (months)</td></tr><tr><td rowspan="2">Small system(100–500 rules)</td><td>Prototype</td><td>10</td><td>0.5</td></tr><tr><td>Pilot</td><td>20–40</td><td>1–2</td></tr><tr><td rowspan="2">Medium system(600–19 000 rules)</td><td>Prototype</td><td>60–150</td><td>2–3</td></tr><tr><td>Pilot</td><td>200–800</td><td>6–8</td></tr><tr><td rowspan="2">Large system(2000–10 000 rules)</td><td>Prototype</td><td>200–400</td><td>4–6</td></tr><tr><td>Pilot</td><td>1–3000</td><td>18–36</td></tr></table>

Source: after Cook and Schleede $^{27}$

Their papers are accepted for publication, yet few of the ES that they discuss are developed into working systems. Second, at the same time these advocates can point to the implementation of many rather mundane systems that, because they possess some state-of-the-art features, are termed ES. Thus the high road is often publicized, but in practice, it is the low road that is taken.

The costs associated with the design and implementation of ES are not trivial. In Table 4 are reproduced the estimates given by Cook and Schleede $^{27}$ for the costs associated with the development of ES in advertising.

The Mingers and Adlam $^{24}$ findings and the costs strongly suggest that the development of ES applications will follow the evolutionary path taken by IT in the past: with operational systems developed first where the payoffs are very tangible, followed by application to those aspects of management information systems where the activities are well-structured. Only when these two types of information systems are firmly in place will corporate monies be made available for ES to be applied to decision support systems.

Over the next decade the major contribution that ES would appear to be capable of making to strategic performance is through their being embedded within conventional information systems $^{23, 25, 28}$ .

## Summary and conclusion

It is presently strongly advocated that IT can convey sustainable strategic advantage $^{21, 22, 26}$ and by implication and extension that this also applies to ES. The arguments put forward in this paper suggest that there is a need to consider the technological environment within which the industry is operating and the tasks that the organization is undertaking. With well-structured activities the use of IT can produce competitive advantage for an individual firm in a competitive arena, but since IT is generally easily transferable within the arena, any gains from the use of IT will soon become known, with competitors keeping broadly in step with each other. Thus any gains will be tactical and short-lived.

With ill-structured activities, the situation is different, because the organization itself adds value through the use of the information made available through the use of the technology.

The analysis suggests that little in ES is new. ES as presently implemented are suitable for well structured situations. Thus their use, although likely to provide tangible payoffs is unlikely to result in sustainable strategic advantage.

## References

1 Bramer, M A Survey and Critical Review of Expert Systems Research Introductory Readings in Expert Systems, Gordon and Breach, London (1982)

2 Moutinho, L and Paton, R 'Expert systems: a new tool in marketing' Q. Rev. Marketing (Summer 1988) pp 5-15

3 Buchanan, B G and Shortliffe E H Rule-Based Expert Programs. The MYCIN Experiments of the Stanford Heuristic Programming Project Addison-Wesley, New York (1981)

4 Panko, R R End User Computing: Management, Applications, and Technology John Wiley and Sons, Chichester (1988)

5 Clark, P and Staunton, N Innovation in Technology and Organization Routledge, London (1989)

6 Jackson, P Introduction to Expert Systems 2nd edition, Addison-Wesley, New York (1990)

7 Kim, J and Courtney, J F 'A survey of knowledge acquisition techniques and their relevance to managerial problem solving' Decision Support Syst. Vol 4 (1988) pp 269–284

8 FCS Thorn-EMI Computer Software Ltd., Sunbury House, 79 Staines Road West, Sunbury on Thames, Middlesex TW16 7AH, UK

9 System-W Comshare Inc., Corporate Headquarters, 3001, South State Street, MI 48108, USA

10 Turban, E Decision Support and Expert Systems 2nd edition, MacMillan, New York (1990)

11 Express Information Resources Inc., DSS Division Headquarters, 200, Fifth Avenue, Waltham, MA 02154-9911, USA

12 Zadeh, L A 'Fuzzy sets' Inf. and Control, Vol 8 (1965)

13 Javelin Information Resources Inc., Javelin Products Group, 200, Fifth Avenue, Waltham, MA 02154-9911, USA

14 Waterman, D A A Guide to Expert Systems Addison Wesley, New York (1986)

15 Simon, H A The New Science of Management Decision 3rd edition, Harper and Row, New York (1977)

16 Dermer, J Management Planning and Control Systems: Advanced Concepts and Cases, Irwin, New York (1977)

17 Porter, M E Competitive Advantage: creating and sustaining superior performance The Free Press, New York (1985)

18 Cragg, P B and Finlay P N 'IT: running fast and standing still?' Inf. and Manag. Vol 21 (1991) pp 193-200

19 Vitale, M R 'The growing risks of information systems success' MIS Quarterly Vol 10, No 4 (December 1986) pp 327-334.

20 King, W R, Grover, V and Hufnagel, E H 'Using information and information technology for sustainable

competitive advantage: some empirical evidence' Inf. and Manag. Vol 17 (1989) pp 87-93

21 Porter, M E and Millar, V E 'How information gives you competitive advantage' Harvard Bus. Rev. (July-August 1985) pp 149-160

22 Rockart, J F and Short, J E 'IT in the 1990s: managing organizational interdependence' Sloan Manag. Rev. (Winter 1989) pp 7–17

23 Brookes, C H P 'A framework for DSS development'. In Proc. DSS-85 San Francisco, CA (1985) pp 80-97

24 Mingers, J and Adlam, J 'Where are the "real" expert systems?' OR Insight Vol 2 No 3 (July-September 1989) pp 6-9

25 Ignizio, J P An Introduction to Expert Systems: The Development and Implementation of Rule-Based Expert Systems McGraw-Hill, New York (1991)

26 Chorafas, D N Applying Expert Systems in Business McGraw-Hill, New York (1987)

27 Cook, R L and Schleede, J M 'Applications of expert systems to advertising' J. Adv. Res. (June/July 1988) pp 47–56

28 Turban, E and Watkins, P R 'Integrating expert systems and decision support systems'. In Sprague, R H Jr and Watson, H J (eds) Decision Support Systems, putting theory into practice Prentice Hall, New York (1986)
