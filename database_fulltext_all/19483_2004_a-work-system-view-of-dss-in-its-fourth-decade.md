---
otero_id: 19483
otero_key: "37HUZMGU"
title: "A work system view of DSS in its fourth decade"
authors: "Steven Alter"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2003.04.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A work system view of DSS in its fourth decade

Steven Alter\*

School of Business and Management, University of San Francisco, 2130 Fulton Street, San Francisco, CA 94117-1080, USA

Received 1 November 2002; accepted 1 April 2003

Available online 18 September 2003

## Abstract

The initially revolutionary DSS agenda is now ancient history. This paper argues that ‘‘decision support’’ provides a richer basis than ‘‘DSS’’ in both practice and research. Using a loan-processing example involving two banks, it shows how work system concepts might be applied to understand decision support in real world settings, and how decision support can come from many sources other than technical artifacts such as DSS. Shifting the focus from ‘‘DSS as artifact’’ to ‘‘decision support within a work system’’ reduces the chances of being misled by techno-hype, vendor sales pitches, and incomplete understanding of determinants of success in organizations. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Decision support system; Decision support; Work system; Work system method

## 1. Introduction

Initially, DSS was revolutionary idea. It attempted to move beyond MIS (summarizing transaction and operational data for managers), which had attempted to advance beyond EDP (collection and processing of transaction data through computers and electronic media). Launched before PCs existed, the initial concept of DSS focused on using interactive computing in semi-structured decision making. The emphasis on semi-structured decision making seemed important (in academic politics if not in other ways) because that distinguished DSS from OR, especially from optimization models, which attempted to automate decision making, or so it seemed. The interactive use of computers seemed important because it was unclear whether more than a small minority of managers would be willing or able to use computers directly in management work.

After 30 years, the original issues that led to the DSS movement have receded to ancient history. Computers are used interactively by managers, nonmanagers, and school children. Computerized data and models are used so commonly and for so many structured, semi-structured, and unstructured tasks that the non-use of computers in typical decision-oriented situations is sometimes a noteworthy exception. With today’s widespread adoption of PCs and the Internet, we should simply declare victory on the original DSS agenda that included interactive computing, application of computing to semi-structured problems, use of computers by managers, and the ability to analyze data and models. However, doing this would leave us with a question of whether DSS retains any useful meaning today. With or without the DSS label, researchers and practitioners will continue to do research about sense making and decision making in organizations and will continue to build tools and methods that support those activities. With or without the DSS label, important progress continues in developing tools and methods related to OLAP, data warehousing, data mining, model building, expert systems, neural networks, intelligent agents, group support systems, and communication capabilities for virtual teams. New umbrella terms have emerged, such as business intelligence and decision support applications, but behind the new details and capabilities are many of the same issues and risks that existed in the past. Regardless of whether the new DSS capabilities emphasize better data availability, data analysis, modeling, or communication and coordination, those capabilities have little or no impact until they are incorporated into work systems within organizations.

On the other hand, DSS does serve as an umbrella for convening groups of researchers interested in systematic and typically computer-based tools and systems related to sense making and decision making. The new SIGDSS within AIS is a prime example because it provides an institutional home base that supports what Keen [11] calls a self-defined community and what King [13, p. 293] calls an intellectual convocation.

But is that all? Could we do equally well if we called the umbrella BWT or XSS or any other three letter acronym? This paper summarizes why my ideas about DSS have moved from enthusiasm to disillusionment to abandonment during the 20+ years since I finished one of the first PhD theses in the area. Next, it reconsiders the notion of decision support from a different viewpoint by exploring how work system concepts might be used to understand decision support in real world settings. Approaching the general area of DSS from a work system viewpoint shifts the perspective and may provide new insights. Decision support is not about tools per se, but rather, about making better decisions within work systems in organizations. The common emphasis on features and benefits of DSS as artifacts rather than on how to improve decisional aspects of work systems in organizations may contribute to the frequently cited (e.g., Ref. [9]) and occasionally questioned (e.g., Ref. [10]) failure rates of data warehousing, CRM, and other technology-based innovations.

## 2. From enthusiasm to disillusionment to abandonment

I certainly was enthusiastic about the prospects for DSS in the 1970s when I started work that led to one of the first PhD theses, one of the first books, and a number of early articles about DSS. This section explains why my original enthusiasm eventually turned to disillusionment and abandonment of DSS in favor of a much more general focus.

## 2.1. Enthusiasm—DSS as a new field in the 1970s

I was lucky to work at MIT with Peter Keen and Michael Scott Morton, early DSS proponents who wrote the first book on DSS [12]. My work started with eight lengthy case studies of systems that might fit under the DSS heading. These findings led to a 1975 thesis based on an exploratory study of 56 such systems. This was to be a thesis on DSS, yet I called it ‘‘A Study of Computer Aided Decision Making in Organizations’’ and avoided mentioning the term DSS even once. I feared that if I used a tight definition I would never be able to find a single example that qualified as a DSS. I would be like a researcher on unicorns, able to theorize about what the unicorns should be and how they should look, but unable to validate any particular assertion about unicorns. On the other hand, if I made the definition too broad my committee would ask me whether the definition distinguished DSS from anything else.

I repressed these compunctions after submitting the thesis and wrote a book about DSS [1] and a number of articles. Although I tried to be clear about the wide range of systems included under the general heading of DSS, I always wondered whether DSS were truly different from other types of information systems. If they were different, what were the significant differences? If they were not truly different, what was the big deal?

## 2.2. Disillusionment—developing a DSS in the 1980s without using the term DSS

I spent most of the 1980s with Consilium, a manufacturing software firm whose semiconductor industry customers used our software to track manufacturing execution through a 100+ step processes, collect engineering data, dispatch lots, plan work for today and for the next several weeks, generate warnings when lots went out of spec, and provide other information for execution and control. We often used DSS concepts while developing our software capabilities. For example, we often thought about the degree of structure in particular decision processes and considered whether particular data, models, or communication and coordination capabilities might help. Despite using DSS ideas, we never referred to our software or its subsystems as a DSS because the classification did not clarify anything.

Someone looking at our software might say that it included every type of DSS mentioned in the new SIGDSS web site:

 Data-driven DSS: Our software collected and provided real time access to a large operational database that factory technicians needed to make a range of structured, semi-structured, and unstructured decisions. It also provided queries and management reports.

 Model-driven DSS: Our software contained a number of models used for planning and scheduling; it could also link to engineering-related models.

 Knowledge-based DSS: Our software included a small rule-based dispatching system.

 Communication-based DSS: Our software provided warnings triggered by pre-specified conditions and sent automatic or manually generated messages to operators before they began processing particular lots to which exceptions applied.

 Document-driven DSS: The software contained a module for engineering specs.

Was it a DSS or wasn’t it? It was an interactive system that unquestionably supported a wide range of structured, semi-structured, and unstructured decisions by factory technicians, engineers, and managers. If it was a DSS, what kind was it? Was it every kind? Would it make sense to say it was 60% data-driven, 23% model-driven, 4% knowledge-driven, etc.? And if someone said that, would it matter?

## 2.3. Abandonment—moving toward a work system focus in the 1990s

While with Consilium, I had the impression that some customers bought our software without understanding that its value would be realized only if their firms used it to improve the way they did important work such as planning production, controlling operations, and identifying and responding to manufacturing defects. The problem seemed not to be about understanding the numerous features and details of the software because we had few complaints about our reasonably clear product concepts, consistent screen design, good documentation, and reasonably good demos. On the other hand, it sometimes seemed to me (without proof) that some of our customers and staff members did not see the relationship between software features and work practices.

When I returned to academia, I decided to try to focus my research on something that would have helped our customers and staff understand and collaborate around systems in organizations. Eventually, I concluded that most important issues related to understanding and analyzing information systems from a business viewpoint were actually related to the work system being supported, not the information system per se. Work systems and the work system method for analyzing systems are discussed in my Information System textbook [5] and a number of recently published articles [2–4,6,7]. Typical business organizations have work systems for obtaining materials from suppliers, producing and delivering end products, finding customers, creating financial reports, hiring employees, coordinating work across departments, and many other functions. A work system is a system in which human participants and/or machines perform a business process using information, technology, and other resources to produce products and/or services for internal or external customers. A work system operates within a surrounding environment, often using shared infrastructure, and sometimes within a conscious strategy for the organization or work system. Based on the definition, even a cursory understanding of a work system requires attention to nine elements: the business process, participants, information, technology, products and/ or services produced, customers, environment, infrastructure, and strategy. Unlike projects, work systems evolve through a life cycle that encompasses multiple iterations of four steps: (1) operation and maintenance of an existing system, (2) initiation of major changes, (3) development or acquisition of required hardware, software, documentation, and training material, and (4) implementation of the improved work system in the organization.

Ideas underlying the work system approach can be applied to DSS as follows:

1. DSS as a type of work system: Information systems, projects, value chains, and supply chains are special cases of work systems. In each case, human participants perform a business process using information, technology, and other resources to product products and services for internal and/or external customers. What Sprague and Carlson [14] once called ‘‘specific DSS’’ might be viewed as a special type of information system, and an information system is a special type of work system in which the business process is limited to processing information. Sprague and Carlson contrasted ‘‘specific DSS’’ with ‘‘DSS generator’’. . . ‘‘a package of related hardware and software which provides a set of capabilities to build a specific DSS.’’ [15]. Notice the implication: If a DSS can be either a specific work system (a specific DSS) or a technology used to build a DSS (a DSS generator), almost nothing of significance can be said about DSS in general, just as little can be said in general about the term computer if it might mean both a machine that computes and a person who computes (the original meaning).

2. Inheritance of success factors and operational principles: Success factors, operational principles, and analysis methods that apply to work systems in general should be ‘‘inherited’’ by the special cases. If inheritance of success factors and operational principles applies to ‘‘specific DSS’’ as a special case of work system, then many basic ideas about DSS are probably ideas about work systems in general, such as the importance of management support, adequate resources, commitment and involvement by participants, and adequate skills.

3. Different degrees of overlap: There are many forms of overlap between information systems and the work systems they support. In cases such as brokerage transaction systems, payroll systems, and E-commerce web sites, these systems overlap greatly. In other cases, the information system may support many disparate work systems. If a DSS overlaps significantly with the work system being supported, focusing on the separate identity and capabilities of the DSS instead of viewing it as an integral part of a work system becomes less and less useful to anyone trying to improve either system.

4. Analysis from a business viewpoint: A set of general principles applies for any work system. For example, any work system should please its customers, perform its work efficiently, and serve its participants. These principles form the basis of a method for analyzing any work system from a business viewpoint. If there is a good way to analyze work systems, then DSS that are work systems should be analyzed as any other work system should be analyzed, at least at a first approximation.

5. Creating or improving a DSS in an organization: Since a DSS is a special case of a work system, the work system life cycle should apply to DSS, at least as a first approximation, and many of the basic ideas for creating or improving a DSS should be similar or equivalent to the basic ideas for creating or improving work systems in general. Since there is no compelling distinction between DSS and other types of information systems, the processes for creating and improving a DSS may be similar to those for creating and improving information systems in general, and possibly, work systems in general.

These points imply that little can be said about DSS in general other than statements such as ‘‘Systems of types X, Y, and Z are typically included under the general umbrella of DSS.’’ By placing disparate approaches under the same umbrella, the broader, more encompassing definitions of DSS tend to blur any distinguishing characteristics. In effect, DSS becomes all information systems that are used by managers or business professionals and do not fall into some other category.

Having moved from enthusiasm to disillusionment and finally abandonment of DSS as a useful concept, this paper will now take a different tack by using the work system ideas to discuss decision support without talking about DSS.

## 3. A different umbrella: ‘‘Decision Support’’ rather than DSS

This section explores the assumption that stripping the word ‘‘system’’ from DSS, focusing on decision support, and using ideas related to the work system method might generate some interesting directions for research and practice. Some of these directions fit under the DSS umbrella and some seem to be excluded because they are not directly related to a technical artifact called a DSS.

Decision support is the use of any plausible computerized or non-computerized means for improving sense making and/or decision making in a particular repetitive or non-repetitive business situation in a particular organization.

Defining the topic as decision support rather than DSS expands the landscape to include decision improvement interventions and strategies that might or might not involve a technical artifact called a DSS. Embracing this broader perspective is totally sensible from the viewpoint of a typical business professional who cares about improving decisions, does not view DSS from a vendor’s viewpoint, and is has no special preferences about using DSS or alternative approaches for improving decisions. The broader perspective is also useful for IT professionals who want to do more than just pursuing their own personal interests and treating everything unrelated to technical DSS components as someone else’s problem. The ‘‘analytic applications’’ that were recently described on the Data Warehousing Institute’s web site as an emerging trend in business intelligence [8] represent a step toward this type of approach, Finally, it makes sense for DSS researchers concerned with determinants of decision quality and DSS success in real world situations. (This switch of perspective is less important to those DSS researchers who focus on designing and experimenting with new algorithms and tools, and who therefore leave real world application to others.)

At this point, some readers (but probably not all) might complain that ‘‘decision support’’ is what DSS is about and that no one actually takes the term DSS literally anymore, so what’s the big deal? If that is true, why do we still have textbooks about DSS (not decision support) and why do some information system textbooks devote a chapter to DSS? Similarly, why are books about information systems titled ‘‘MIS’’ when MIS is now a subset of the IS field. Furthermore, why do most expert systems not conform to the idealized definitions of that category? In my view, using terminology that garbles or contradicts current reality simply encourages confusion and sloppy thinking.

## 3.1. Possible sources of better decision support

Based on the definition of work system, decision support may come from many different aspects of the work system. Variations or modifications in any of the nine work system elements might provide better support for sense making or decision making. The resulting improvements might be measured in terms of decision quality, business process efficiency, the psychological well being of the participants, the satisfaction of the customers, or other possible performance variables. Consider some of the possible sources of improvement:

Business process: Variations in the process rationale, sequence of steps, or in the methods used for performing particular steps.

Participants: Better training, better skills, higher levels of commitment, and better real time or delayed feedback.

Information: Better information quality, information availability, and information presentation.

Technology: Better data storage and retrieval, models, algorithms, statistical or graphical capabilities; better computer interaction.

Product and services: Better ways to evaluate potential decisions.

Customers: Better ways to involve the customers in the decision process and to obtain greater clarity about their needs.

Infrastructure: More effective use of shared infrastructure might lead to improvements.

Environment: Better methods for incorporating concerns from the surrounding environment.

Strategy: A fundamentally different operational strategy for the work system.

If it is true that decision support might come from any of these nine elements, business and IT professionals and researchers concerned with decision quality have little reason to focus only on a particular part of the work system’s technology (the DSS). The following hypothetical example is based on two real world situations and is constructed to illustrate the wide range of concerns that a work system viewpoint brings to the discussion of decision support.

## 3.2. Example: alternative methods for loan approvals

Assume that managers from Bank X want to improve its loan approval system and therefore visit non-competing Banks R and S, both of which provide business loans elsewhere. In Bank R’s highly automated method for loan approvals, a proprietary algorithm processes information compiled by the loan officer and generates an approval or disapproval decision. The loan officer may protest some decisions by arguing that the situation warrants a different interpretation, but the bank usually stays with the algorithm-generated decision because the average performance of a loan committee will probably be no better than the average performance of a historybased algorithm. In Bank S’s relatively non-automated method, the loan officer presents a credit report, standard loan calculations, and other supporting material to a loan committee that meets periodically. Consider aspects of decision support that Bank X might explore after examining these dissimilar approaches:

Business process: Various business process characteristics highlight many possible sources of decision support.

Degree of structure: Bank R uses a much more structured method than Bank S. Even if the final decision is not totally automated, the use of this type of algorithm may support decision making by an individual or a committee.

 Range of involvement: The method at Bank S uses a much wider range of involvement. Getting more people involved may support more effective decisions or, alternatively, may simply slow things down.

 Level of integration: Banks R and S both rely on the loan officer to compile data that is the starting point of the approval process. A higher level of integration between the data compilation and the approval decision might support the decision more efficiently and effectively, particularly by reducing the amount of time and effort the loan officer devotes to compiling data instead of generating new loan opportunities.

Complexity: The method at Bank S is more complex because it incorporates more types of quantitative and qualitative information. The simpler method at Bank R is based on a particular set of information that can be defined in advance.

 Rhythm: The method at Bank R generates the approval whenever the required information about the loan and the borrower is complete. On average, this improves decision turnaround by about three days.

Degree of reliance on machines: The method at Bank R relies on machines much more heavily than the method at Bank S. This probably increases consistency, although it is not obvious that consistency leads to better results than a method than incorporates more business judgment and intuition related to specific loan requests.

Treatment of errors and exceptions: The method at Bank R provides a feedback mechanism that tries to assess whether past decisions were errors. This feedback aids in the continuing improvement of the algorithm, and may also support the evaluation of appeals by the loan officer. The method at Bank S provides no direct feedback of this type. Both banks use data filtering programs that support the identification of likely errors in the credit reports and other loan justification data.

Participants: Loan officers in both banks feel burdened by the extensive data compilation required for loan approval. Bank S tries to help by providing clerical assistance for data entry, thereby helping loan officers obtain and verify information by spending more time with customers. Bank R provides a series of small, personalized spreadsheet models to support decisions about how to respond to appeals of the automated decisions.

Information: Insuring data accuracy is a key issue in both loan approval processes. In both cases, a set of filtering programs identifies likely data errors, thereby supporting the process of verifying the inputs.

Technology: Both banks provide laptop computers for entering loan data and negotiating rates with customers. Bank R uses technology more extensively because the decision itself is typically automated. Bank R provides a filter for identifying loan applications that might be outliers in the statistical sample used to generate the decision algorithm. In these cases, the automatically generated decision receives closer scrutiny, including additional analysis of the nature of the exception.

Products and services: The primary product of both decision processes is approval or disapproval of the loan. At Bank R, the decision comes with several numerical ratings that summarize the reason for the decision. These ratings support the loan officer’s decision of whether to appeal and the management decision of whether to reverse a rejection.

Customers: These include the loan applicant and the loan officer. The satisfaction of both depends most directly on whether the loan is granted, and secondarily on whether the loan application is handled quickly and fairly. Bank S provides a useful set of guidelines that supports a customer’s decisions about typical loan provisions and what types of inquiries to expect.

Infrastructure: Both banks provide shared technology infrastructure for submitting applicant related data and for many other tasks. The infrastructure supports decision quality from a customer’s viewpoint by expediting the process.

Environment: Government concerns about discrimination and redlining have resulted in governmental reporting requirements related to the relative success of loan applications from applicants with different profiles. Bank R addressed this issue by building an explanation module that provides an after-the-fact rationale for why each decision was made.

Strategy: Differences in process strategy are linked to strategic differences between the two banks. In both cases, methods used for supporting decision making were developed consistent with the bank’s strategy. At least in theory, each bank’s approval decisions could be supported by quantitative measures related to loan criteria derived from the bank’s strategy.

## 4. Conclusion

The first part of this paper argued that DSS has little meaning other than as an umbrella covering a cluster of research interests related to using technology to support sense making and decision making.

The second, more useful part of the paper suggested that decision support is a more useful concept than DSS for most purposes related to practice and research. This is based on the belief that most work systems of any significance include some form of computerized support for sense making and decision making. Possible sources of better decision support may include variations or modifications in any of the nine work system elements, not just the technology, and certainly not just technical artifacts that are sometimes called DSS.

Furthermore, any DSS of genuine significance is usually an integral part of a work system and often cannot be separated out easily. For example, the loan approval process at Bank R simply would not operate without the algorithm, and the algorithm is designed specifically to serve this particular work system. Analyzing the algorithm might be interesting, but anyone trying to understand its implementation and success in the organization would need to look at the work system. In addition, the difference between automating and not automating the decision can describe strategy alternatives for a work system, but is less interesting for classifying DSS. For example, whether or not Bank R’s highly automated approach fits under the DSS umbrella depends jointly on the definition of DSS that one chooses and on where Bank R sets the bar concerning the conditions and frequency of appeals.

The above points do nothing to diminish the importance of creating new DSS theory or building new DSS tools. The development and experimentation required for these pursuits is necessary and significant source of innovations that later may be applied in real world situations.

Although research on DSS per se certainly needs to continue, switching the perspective from ‘‘DSS as artifact’’ to ‘‘decision support within a work system’’ encourages consideration of research topics related to each of the work system elements, and this leads to a broader range of potentially valuable research:

Business process: How changes in particular business process characteristics (such as degree of structure, range of involvement, complexity, and so on) affect the process efficiency and decision quality.

Participants: Both for isolated individuals and for individuals working in teams, how individual characteristics such as personality type, risk aversion, gender, background, and status affect sense making and decision making; how to recognize and address significant differences concerning assumptions, goals, and understanding related to a particular decision.

Information: How information and DSS tools can be used within work systems to minimize the effects of common flaws in decision making such as primacy effects, recency effects, overconfidence, poor probability estimation, and groupthink.

Technology: How better tools can help people understand situations and deal with information overload; continued development of established tools and techniques such as mathematical modeling, statistical methods, OLAP, data mining, and group support.

Product and services: How to evaluate the quality of decisions, especially as part of the decision process rather than after the fact.

Customers: How to involve customers in the decision process and obtain greater clarity about their needs and goals.

Infrastructure: More effective ways to exploit shared infrastructure within decision processes.

Environment: How to visualize whether a possible decision might conflict with the surrounding environment, and how to adjust the decision accordingly.

Strategy: How to assess and represent the extent to which a possible decision is aligned with the corporate, departmental, and individual strategies.

The topics above are just a subset of the research topics that fit under a broadly construed view of decision support. Focusing on ‘‘decision support within a work system’’ rather than ‘‘DSS as artifact’’ helps align the interests of practitioners and researchers because both groups care about improving decisions within work systems even if only a few members of either group care about DSS as an artifact. Whether or not we retain DSS as an umbrella for getting together at conferences, a deeper look at the idea of decision support without the second S and from a work system viewpoint might help in exploring new directions for research with a high potential for real world application.

## References

[1] S. Alter, Decision Support Systems: Current Practices and Continuing Challenges, Addison-Wesley, Reading, MA, 1980.

[2] S. Alter, A general, yet useful theory of information systems, Communications of the AIS 1 (13) (1999 Mar.).

[3] S. Alter, Are the fundamental concepts of information systems mostly about work systems? Communications of the AIS 5 (11) (2001 Apr.).

[4] S. Alter, Which life cycle—work system, information system, or software? Communications of the AIS 7 (17) (2001 Oct.).

[5] S. Alter, Information Systems: Foundation of E-Business, 4th ed., Prentice-Hall, Upper Saddle River, NJ, 2002.

[6] S. Alter, Navigating the Collaboration Triangle, CIO Insight 9 (2002 Jan.) (http://www.cioinsight.com/article/0,3658,s = 307&a=22258,00.asp)

[7] S. Alter, The work system method for understanding information systems and information system research, Communications of the AIS 9 (6) (2002 Sep.).

[8] W.W. Eckerson, Excerpt from TDWI’s research report— the rise of analytic applications: build or buy? Journal of Data Warehousing 8 (1) (2003 Winter) (retrieved March 30, 2003 from http://www.dw-institute.com/research/display. asp?id=6588).

[9] M.N. Frolick, K. Lindsey, Critical factors for data warehouse failure, Journal of Data Warehousing 8 (1) (2003 Winter) (retrieved March 30, 2003 from http://www.dw-institute.com/ research/display.asp?id=6592).

[10] B. Inmon, Information Management: Charting the Course: Little White Lies, DM Review (August 2001) (retrieved March 30, 2003, from http://www.dmreview.com/master. cfm?NavID=198&EdID=3819).

[11] P.G.W. Keen, Relevance and rigor in information systems research: improving quality, confidence, cohesion, and impact, in: H.E. Nissen, H.K. Klein, R. Hirschheim (Eds.), Information Systems Research: Contemporary Approaches and Emergent Traditions, North-Holland, Amsterdam, 1991, pp. 27 – 49.

[12] P.G.W. Keen, M.S. Scott Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, MA, 1987.

[13] J.L. King, Editorial notes, Information Systems Research 4 (4) (1993 Dec.) 291–298.

[14] R.H. Sprague Jr., E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

[15] R.H. Sprague Jr., H.J. Watson (Eds.), Decision Support Systems: Putting Theory into Practice, 3rd ed., Prentice-Hall, Englewood Cliffs, NJ, 1993.

Steven Alter is Professor of Information Systems at the University of San Francisco. He earned a PhD from MIT and extended his thesis into one of the first books on decision support systems. He served as Vice President of Consilium, a manufacturing software firm that went public in 1989 and was acquired by Applied Materials in 1998. His research for the last decade has concerned developing systems analysis concepts and methods that can be used by typical business professionals and can support communication with IT professionals. His textbook Information Systems: Foundation of E-Business is in its fourth edition. His articles have been published in Harvard Business Review, Sloan Management Review, MIS Quarterly, Interfaces, Communications of the ACM, Communications of the AIS, CIO Insight, and elsewhere. He is a senior editor of the Communications of the AIS.
