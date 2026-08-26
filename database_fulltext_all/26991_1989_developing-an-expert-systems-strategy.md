---
otero_id: 26991
otero_key: "55XCHQ74"
title: "Developing an Expert Systems Strategy"
authors: "Barbara Braden; Jerome Kanter; David Kopcso"
year: "1989"
journal: "MIS Quarterly"
doi: "10.2307/248733"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Developing an Expert Systems Strategy
Author(s): Barbara Braden, Jerome Kanter and David Kopcso
Source: MIS Quarterly, Vol. 13, No. 4 (Dec., 1989), pp. 459-467
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248733

Accessed: 09/05/2014 13:37

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Developing an Expert Systems Strategy

By: Barbara Braden
Bull HN Worldwide Information Systems
300 Concord Road
Billerica, Massachusetts 01821

Jerome Kanter
Center for Information
Management Studies
Babson College
Wellesley, Massachusetts 02157

David Kopcso
Mathematics and Science Division
Babson College
Wellesley, Massachusetts 02157

## Abstract

Bull HN Worldwide Information Systems planned and implemented an expert system that is being used for trouble-shooting the maintenance of its page printing system, a complex product akin to a printing press. Important aspects of the design and development of this expert system include stressing people skills, needing an expert willing to have his expertise cloned, and having a knowledge engineer able to translate the expert's experience into decision rules. This case study covers how the project was selected, how the benefits were determined, and how the implementation strategy has evolved, including future plans for enhancement and extension. Experience with this expert system serves as a base point of how a company can develop its own expert systems strategy, which includes searching for feasible applications, determining the resources required, and establishing the right organizational environment. Expert systems, although focused on a well-defined problem domain, can provide a company with competitive advantage.

Keywords: Expert systems, systems implementation, knowledge engineering, rule-based systems, case study

ACM Categories: H.4.m, I.2, I.2.1, I.2.4, I.2.5, I.2.6, J.2

## The Product and the Marketplace

A page printing system is a complex computer device that is employed to produce large volumes of printed output. It can produce 18,000 lines of print per minute. The system consists of a high-speed tape unit, an electrostatic printer, and a sophisticated paper-cutting and collating device. It has 25 subsystems, over 2,000 electromechanical components, and is considered difficult to trouble-shoot. Furthermore, these systems often are run around the clock with many problems occurring during the difficult-to-service second and third shifts.

Purchasers of page printing systems include Fortune 1,000 companies needing to produce manuals, order catalogues, parts listings, and large documents. The system is not a volume item like a personal computer, but rather a specialty one; thus the location of units is rather diverse throughout the United States and Canada. Approximately 400 systems currently are installed. The U.S. Government is a major customer. Service and response time are vital elements in the marketing strategy of the product.

## Problem Assessment

An expert systems solution was sought to address a situation where, for such a complex product, it was becoming increasingly more difficult and expensive to hire and train maintenance experts to the necessary quality level. In addition, equally complex new models were planned for subsequent years. The new models, though similar, were sufficiently different to require field engineers to continue updating their skills and knowledge, placing even greater demand on the few experts available.

The above characteristics appeared to fit the model of an expert system solution in the general area of diagnosis or trouble-shooting (Prerau, 1988); that is, a situation where:

\- The problem is sufficiently complex but narrow in scope.

\- There is at least one recognized expert who is willing to act as a source of information and is articulate enough to be effective.

\- It takes an expert minutes to a few hours to solve a problem.

\- The expertise is scarce.

\- There appears to be a logical process to diagnose the problem that does not require a great amount of intuition.

\- There is high pay-off in problem resolution.

Figure 1 is a general schematic of the problem-solving process, starting with the initial customer complaint. As can be seen, a difficult problem can require three on-site visits, by the field engineer, the specialist, and finally the expert. Obviously, there are cost savings to be made if, in a number of instances, the field engineer, via the expert system, can preclude interaction or visits by the specialist or expert. More importantly, from the customer's view, considerable time can be saved that otherwise would be expended by Bull Worldwide Information Systems' Customer Services Division (CSD) in matching the required people to the specific problem.

## The Approach

At the outset, every project must bear a code name or acronym, and this system was designated TAPPS (Trouble-shooting Aide for Page Printing System). Its current sobriquet is PAGE-X. Once the problem domain was identified, a three-stage development process was laid out.

## Problem definition and objectives

The first stage was problem definition and statement of objectives. The objective, simply stated, was to aid the customer service engineer in troubleshooting the page printing system (PPS). The system had to be available as a 24-hour diagnostic aid, be a training aid (akin to a flight simulator) in lieu of hands-on experience, and provide a reservoir (knowledge base) for PPS product knowledge and know-how. The cost goal was to reduce the mean time to repair (MTTR) by 30 percent. Customer Services Division management estimated a cost savings of \$950,000 over a five-year period. At this stage there is no reason to doubt that those savings will be met or exceeded.

## Knowledge gathering

The second stage was the gathering of knowledge (the knowledge acquisition and assimilation process). This is the crux of an expert system solution. The problem was well-bounded, and the logic and knowledge rested in the head of a single expert. Unlike other systems' domains consisting of a great deal of output and input with minimal processing crossing multiple departments and functions, this application did not tap many minds for a variety of details. The key to an expert system is to leverage depth rather than breadth (Davis, 1984). This presents both positive and negative elements. In the case of PPS, there were few experts, and one was selected based on his proven knowledge and expertise through actual experience. The challenge at hand was, as nearly as possible, to clone PPS expert Earl Wielsma.

The first step was to read available manuals on PPS system maintenance and build a preliminary knowledge base through a general question-and-answer process with Mr. Wielsma. A knowledge base is a set of rules, mostly of the if-then variety, a sort of decision logic tree. For example, a problem symptom, erratic paper motion, is indicative of unevenly fed paper causing double printed lines or unplanned spacing. Figure 2 illustrates the potential causes of this problem and the chances of each cause occurring (as supplied by Mr. Wielsma).

An expert system can be classified by the number of rules in its knowledge base. A rough categorization is that small problems have under 350 rules, while large problems have from 3,000 to over 10,000 rules (Harmon and King, 1985). This type of classification can be misleading because some expert systems, including PAGE-X, use techniques such as semantic, hierarchical networks rather than the simpler rule-based approach. Since most expert systems employ the rule-based method, the rule index for complexity is the technique most commonly used. Also, it is true that the number of rules used is a function of the language used and the programmer's style and capability. PAGE-X is classified as a large system, with the equivalent of 3,000-plus rules.

![](/api/attachments/55XCHQ74/fulltext/images/28b3c0fb5d16515f615c5c73ed62ca8ffa43db7cde9e9cad542ab251b10face0.jpg)  
Figure 1. Page Printing Systems: Problem-Solving Process

![](/api/attachments/55XCHQ74/fulltext/images/c3b11704517f1d16af8e8976ac81f7c373ff1dedd6b1006b325260edd96330a0.jpg)  
Figure 2. Inference Network: Symptom and Causes

Another person, a “knowledge engineer,” was needed to establish the framework for the knowledge base. The knowledge engineer chosen, Chuck Strandberg, was exceptionally skilled in working with people; he could be inquisitive without being offensive. He had a background in cognitive psychology and expert systems. He not only had to build a base of PPS symptoms and causes but also develop a conceptual model of the expert’s approach to trouble-shooting. The knowledge engineer started with some PPS documentation, the most important part being a symptom-cause handbook. From these materials he constructed a preliminary knowledge base against which he could pose questions to the expert. He spent an intense two to three days with the expert twice a month over a period of about three months.

To expedite the knowledge acquisition process, a graphical tool was built that could display the multiple networks of relationships. Since an object-oriented programming language was the basis for this tool, information and attributes about each symptom and cause could be moved quickly around the networks and new relationships could be established. If one object (a symptom) became too complex, it could be subdivided with minimal effort. Eventually, the expert was able to make changes, additions, and corrections to an object at his own pace. The knowledge engineer would review these changes in terms of the overall design.

After the preliminary knowledge base was developed, Mr. Wielsma reviewed and thoroughly critiqued the logic, control, and protocol analysis. The knowledge base was also reviewed by other groups for verification and testing. However, the backbone of the knowledge base and rules reflected the problem-solving ability of Mr. Wielsma based on his background, experience, and proven expertise. His opinion became the final word.

## Implementation

The third stage was implementation. This is a recursive process that requires several reimplementations before the design can be considered complete. This stage involves first tackling the simplest and best understood versions of critical tasks, next dealing with the most familiar and accessible portions of the process, and then getting a subset working as quickly as possible. Finally, the output of this subset is tested and evaluated by the expert to ascertain future direction. This technique, called prototyping, is currently coming into vogue in designing conventional data processing systems (Alavi, 1989) but has been a standard and necessary part of artificial intelligence software. The implementation evolves from prototyping to fine tuning. Mr. Wielsma played a critical role in this entire process and devoted approximately 12 weeks toward the 4.3 man-year implementation effort.

## User Interfaces

As for all expert systems, effective user interfaces were an important element of PAGE-X. End users ranged from professional experts to a variety of semi-knowledgeable people to trainees. During the development stage of an expert system, users are the system developers (knowledge engineers) and implementers. The key questions to be answered are: Just who are the other classes of users? How do they view the system? To what information do they need access? And what do they need to be able to do with the information? Multiple interfaces geared to the knowledge required and the knowledge level of each class of user are essential. There is nothing as frustrating to an expert as having to step through a host of procedures that for him or her are basic and completely unnecessary, but are vital for the beginning user (Hoffman, 1987).

On the other hand, too precipitous a lead into the subject will lose the neophyte. The modular approach adopted kept the user interface separate from the functioning of the expert system itself. This allowed a variety of user interface modules to be developed without significant changes to the expert system. Development time was thereby reduced substantially. The user interface is the most volatile and unpredictable part of the total process, and by modularizing the interfaces, work at several user levels could be conducted in parallel.

Four major user-mode functions were developed. The first and probably most important is for the field engineer, who trouble-shoots and maintains the equipment. The main system criterion was an easy-to-use default operation, which could limit the amount of input by defaulting to a standard set that operates in the largest majority of cases. The interface had to allow for help and feedback facilities and had to give a good deal of control to the field engineer. The other classes of user interface were the expert, who must be able to easily review and adjust the rules as necessary and add to the knowledge base; the knowledge engineer, who uses expert system tools to develop the system; and the programmer, who must be able to change and alter the system software as conditions dictate.

The user interfaces to PAGE-X comprise almost 65 percent of the expert system code. Balancing sufficient information content with user skill level required multiple iterations of the user interface and the symptom-fault structure as viewed by the user.

Some of the interface issues were resolved by incorporating multiple modes of access, in terms of experience, for the PAGE-X beginning, intermediate, and advanced users. Moreover, an enengineer could approach problem-solving in several ways. One approach was a set of lists containing symptoms by category. As many symptoms as appeared relevant could be selected. A second approach was through keyword search (one or more). All symptoms containing the keywords could be presented. At this juncture the engineer could move to a Q&A session to isolate the fault and try different tests and remedies or simply examine all the causes of particular symptoms. Since PAGE-X solves multiple faults, each could be examined separately or in combination. Without the above features, the desired level of user acceptance and effective system employment could not have been reached.

## Tools Employed for Development

PAGE-X runs on a Xerox 1108 using the Inter-lisp dialect of the LISP programming language and LOOPS. Xerox, Texas Instruments, and Symbolics have been leaders in developing hardware that have the speed and instruction sets to efficiently go through the lengthy series of decision rules necessary for problem resolution. The most popular languages in which to develop expert systems are LISP and PROLOG, the latter being the basis of the publicized Japanese 5th generation computer. Because the specialized nature of expert systems is built around a rule or knowledge base, expert system implementation was initially accomplished on unique hardware/software platforms like those mentioned above. However, as general purpose hardware and software develop, they will be able to handle all but the very large expert systems.

Expert systems can be implemented with standard computer hardware and software. Currently, there are a growing number of expert systems running on 386 processor PCs. Small systems are running on microcomputers using software systems such as Level5 EXSYS, VP-Expert, PC Easy, Goldworks and PC Prolog. Dupont alone has implemented several thousand small expert systems. Larger systems run on conventional mini and mainframe computers such as Digital's VAX Line, IBM's 3080 series, or Bull Worldwide Information Systems' DPS 9X and 8X line using FORTRAN, Pascal, or C as the software language. Over the past five years the trend has been away from using special purpose computers to run expert systems. The emphasis is on developing expert systems to run on more conventional machines.

## Status and Future Enhancements

Phase I of systems implementation commenced with management approval of the project and the selection and funding of the design team. As noted, the design/implementation process required nearly four and one-half man-years, including 12 weeks' involvement of expert Earl Wielsma. The process featured an early prototype with a preliminary user interface design and the acquisition of 20 to 30 percent of the decision rules comprising the knowledge base. This phase took seven months with the remaining five months (Phase II) spent on acquiring the remaining 70 to 80 percent of the knowledge base, expanding the user interfaces, and continued testing and verification of the rules. Phase III was the use of the system in specific sites, with use gradually incorporating all sites. It should be noted that developing expert systems for follow-on products takes far less time than the original effort. As in any major systems development, the initial process must be expanded and modified as actual usage increases. The current priority list of modifications includes incorporating the rules for new versions of the page printing system as they are announced and adding and modifying rules as experience dictates. It is significant that since the implementation of PAGE-X, the Customer Services Division has developed similar expert systems for other products it maintains.

Since PAGE-X was a first-of-a-kind development, the plan was to reimplement the system on a general purpose machine so that wider, more responsive, more economic use could be made of the system. Currently, the system is a single-station operation. A machine is needed for each trouble-shooting episode, which normally involves 15 to 45 minutes of online time. The current objective is to deliver a fully functional PAGE-X on a top-of-the-line personal computer within the next year.

The technology available when the project first began was exploited to the fullest. However, stand-alone workstations are not appropriate for geographically dispersed field organizations that require access to the system at customer sites.

Moreover, the engineers wanted PAGE-X to include more information found on traditional internal systems. For large expert systems, until the technology is part and parcel or at least complimentary to ongoing data processing and communication systems, the significant payoff in their deployment is limited. The future will see small expert systems embedded in the product.

In terms of implementation within the organization, the value of PAGE-X was almost immediately recognized by experienced engineers. It may have had even greater acceptance if it were not viewed as a singular application that required non-standard access.

Relating back to the original system objectives, the Customer Services Division of Bull Worldwide Information Systems does have an effective 24-hour diagnostic aid that continues to build user confidence. Moderately trained field engineers are using the system based on previous experience and records, and analysis shows that the MTTR (Mean Time To Repair) has been materially reduced. The implementation approach was a laissez-faire one where field engineers could opt to use the system or not. Most are now using the system, and experience shows that once introduced the engineer becomes dependent on it as a primary source of diagnostic information.

## Developing an Expert Systems Strategy

What should be a company's strategy on the employment of expert systems? This was raised by both the management and system designers at the start of the development cycle of PAGE-X and was discussed periodically throughout the cycle.

## Feasibility and justification

Expert Systems are no different than any other sweeping new technology; the “front-end” probing and analysis are essential for deciding the extent of technology employment. The first concern is to understand the problem domains and determine how important these are to your company’s competitive stance or bottom line. Information systems are being used more strategically in a growing number of industries and companies. Porter’s (1985) theory states that information systems can give a company a competitive edge if they can: (1) reduce the cost of the product or service; (2) differentiate a product or service; or (3) develop a new market niche. If expert systems can affect any of these three areas in a major way, they must be considered seriously. PAGE-X plays an important role in cost reduction and also provides improved customer service. This creates a compelling selling point to customers concerned about the maintenance of their page printing system. A delay in turning out a manual or a product catalogue could be most damaging for a company.

CSD anticipated the effect of expert systems in these three areas in management meetings that preceded work on the system. A committee was established at the onset to look into areas of potential expert systems application, and over 40 areas were uncovered. Through the committee process and periodic reviews with senior management, the 40 were finally culled to the eventual PAGE-X implementation. Since then, several additional implementations have been introduced.

A prominent force in CSD's expert system strategy was the commitment and leadership from the top. From the beginning, Sy Kraut, then vice president and general manager of CSD, insisted that the team be formed and the meetings be held. He envisioned that expert systems could give CSD a competitive advantage, and he would not allow the quest to falter. In all major systems development, it has been said that top management commitment is crucial. This applies even more to systems where the technology is new and still in a test mode where the system gestation period is lengthy.

An organized search for key application areas and the determination of strategic areas of opportunity where competitive edge is apparent are prerequisites for the employment of expert systems. Relative payoffs or justification of alternate opportunities should be carefully evaluated. Several insurance companies are developing expert systems that qualify prospective policy holders and write insurance policies at unattended kiosks in shopping malls through an online interactive dialogue. Oil companies have developed expert systems that analyze geodetic factors and direct oil drilling operations. Expert systems-based financial analysis systems are projecting cash flow and future profit-and-loss scenarios for new companies and are analyzing investment portfolios.

These are instances, and there are many more, where expert systems afford competitive advantage by reducing costs dramatically, differentiating a product, or opening up a new market niche.

Usually the projects selected are long-term. CSD mandated that its initial application of expert systems be completed in one year, but the actual time was a bit longer. Although the initial costs were high for hardware/software (probably \$80,000-\$100,000) and personnel (3 to 4 man years), each succeeding implementation of an expert system requires significantly less money and time. But large, multi-year projects that promise competitive advantage to a company must have staying power to withstand the changes in business conditions and company environment that will inevitably occur over the project's life cycle. Top management sponsorship is essential to protect these systems from cost-cutting programs and reorganizations that are common in the merger/acquisitions-oriented business world.

## Resources to implement

The need for a willing, competent expert or experts has already been mentioned as a prerequisite to development. Equally important is a group of analysts who have the capabilities to translate the expert's knowledge into a workable expert system.

There is as yet no training program or educational process that turns out qualified “knowledge engineers,” as these analysts are called. The CSD experience shows it is difficult for a run-of-the-mill systems analyst to become a knowledge engineer. Expert systems require dealing with incomplete data, hypotheses, percentages, and, in general, a host of what are termed “fuzzy data” (Kopcso, et al., 1988). This is often counter to the precise, structured world of the conventional systems analyst. What is required is a high comfort level when there is ambiguity (Henk and Woods, 1987). A company undertaking expert systems implementation should ensure that such people are available. In this regard, consultant or outside project help, at least for the first system, may well be a requirement.

In addition to the human resources, the technical resources must also be in place. Fortunately, progress is being made in the field, and today the CSD implementation would be materially easier because of new hardware and particularly software developments. So called “shells”

are now available that provide systems languages, as well as the structure to organize and enter the data, that become the knowledge base of the system. Hardware platforms are continuing to benefit from the dramatic improvements in performance-to-price of processing and memory units.

## Establishing the organizational environment

Typically, we continue to overlook the human factors in our quest to install new technologies. There are lessons to be learned in this area from the CSD experience. The first and vital prerequisite, that of senior management commitment, has already been discussed. CSD provided an open, honest company climate regarding the PAGE-X implementation. Progress was continually reported in project updates, regular meetings, and periodic management reviews. The field management were kept apprised as to what was happening.

As mentioned, a laissez-faire approach was used, and no field engineer was forced to use the system. There were natural leaders in the use of new systems, and they were allowed to emerge. The pioneers had a chance to experiment, interact with developers, and see the benefits at their own pace. Other field engineers had time to observe and discuss progress with the system users and decide, on their own, when it was time to adopt the system. A great deal of time was devoted to changing the user interface based on the experience of the initial users; different trouble-shooting styles had to be accommodated. An interesting by-product of the special tools developed to support the system's maintenance is that complete control of the system has been given to Earl Wielsma, the expert. There is no further need of knowledge engineers.

This approach may appear to some to be too haphazard and to take too much time. However, CSD realized the importance of success in their initial expert systems implementation. Taking into account human factors and the organizational environment was top priority. Subsequent implementations could move along at a faster pace. A full recognition that human or political factors can affect a project as much or more than technical factors is a sound precept to bear in mind. Making PAGE-X as non-threatening as possible was a vital implementation philosophy throughout the project.

## Conclusion

The PAGE-X design implementation provides lessons to be learned that are helpful to a company that is considering expert systems. The basic criteria for considering the design and implementation of expert systems are:

\- Feasibility and justification of expert systems in your industry and in your company. A key question is, “Can the system enhance an already existing business strategy or can it be a vehicle for a new business strategy?”

\- Propensity for risk. As in any new technology, there are risks to be evaluated, namely that the project will fail, the project will be late and well in excess of cost estimates, or the project will fail to fully meet the specifications. Another type of risk inherent in an expert systems implementation is that the system will work but the algorithms will be so constituted that they do not accurately reflect the expert's thought processes (Frank, 1988). This may be difficult to detect and may only be possible after mistakes have been made. Although not severe in an application like PAGE-X where there is an immediate feedback loop (e.g., "Does the printer work after repair?"), it can be more serious in implementations such as medical diagnosis. An expert systems strategy must carefully consider, weigh, and evaluate these risks.

\- Evaluation of competing demands for limited resources. Expert systems compete with these demands and must be evaluated against alternative investments. At this stage of development of expert systems, the investment may at least partially be considered as research and development. A company invests in R&D in other technologies (e.g., production machinery, manufacturing processes). Why shouldn't it consider investing in information systems technology?

\- Availability of “knowledge engineers” to design and implement expert systems. Knowledge engineers must be willing to repeatedly ask the expert to explain what he or she knows, be willing to be continually corrected by the expert, and be capable of eliciting information that is “second nature” to the expert.

One important conclusion is that it is unwise to look at expert systems as just a natural extension of traditional information systems. Expert systems are aimed at a different type of problem domain, one in which there are a great number of if-then logic steps to be analyzed in order to develop an answer. In addition, the logic is fuzzy or probabilistic in nature. Expert systems look at problems with a different lens set, and the solutions can be imaginative and far-reaching. The investment in time, cost, and personnel is heavy, but it is just this type of imaginative investment that can create competitive business advantage that others may find difficult to emulate.

## References

Alavi, M. “An Assessment of the Prototyping Approach to Information Systems Development,” Communications of the ACM (27:6), June 1989, pp. 556-563.

Davis, R. “Amplifying Expertise with Expert Systems,” in The AI Business, P.H. Winslow and K.A. Prendergast (eds.), the MIT Press, Cambridge, MA, 1984, pp. 17-40.

Frank, S.J. "What AI Practitioners Should Know about the Law, Part I," AI Magazine (9:1), Spring 1988, pp. 63-75.

Harmon, P. and King, D. Expert Systems, John Wiley & Sons, New York, NY, 1985.

Henk, R.F. and Woods, D.L. "How Humans Process Uncertain Knowledge," AI Magazine (8:3), Fall 1987, pp. 41-53.

Hoffman, R.R. “The Problem of Extracting the Knowledge of Experts from the Perspective of Experimental Psychology,” AI Magazine (8:2), Summer 1987, pp. 53-67.

Kopcso, D.P., Pipino, L.L. and Rybolt, W.H. “A Comparison of the Manipulation of Certainty Factors by Individuals and Expert Systems Shells,” Journal of Management Information Systems (5:1), Summer 1988, pp. 66-81.

Porter, M. Competitive Advantage, The Free Press, New York, NY, 1985.

Prerau, D.S. “Selection of an Appropriate Domain for an Expert System,” Al Magazine (9:2), Summer 1988, pp. 63-75.

## About the Authors

Barbara Braden is director of advanced technologies at Bull HN Worldwide Information Systems. During her nine years with the company, she has held management positions in marketing, information systems, and in the application of advanced technology in solving business problems. She has also worked for several high-technology companies. She holds a bachelor's degree in mathematics from Boston University, a master's degree in education from Northeastern University, and a Ph.D. in education from the Harvard Graduate School of Education.

Jerome Kanter is director of Babson College's Center for Information Management Studies, a cooperative effort of business and academia to improve the use of information systems. Prior to starting the center, he served in a variety of information systems management and technical positions at the Honeywell Company in Boston and at the Kroger Company in Cincinnati. His most recent position was as a consultant specializing in information systems planning, end-user computing, and organizational issues. He has written several books, most recently Computer Essays for Management, published by Prentice-Hall in 1987. His book Management Information Systems is a standard text at many universities. He has also written many articles for professional journals and has lectured at schools such as Harvard, Dartmouth, Baylor, Northwestern, Oxford, and Cambridge. He is a frequent speaker at information systems conferences. He received a bachelor's degree from Harvard University and an MBA from the Harvard Business School.

David Kopcso is professor in the Mathematics and Science Division at Babson College. He serves as chairperson of Babson's Board of Research and is faculty director of its Center for Information Management Studies. He is also director of the Information System Faculty at Babson. He consults in the areas of management information systems and the application of artificial intelligence to business. He is author or co-author of numerous articles in the fields of artificial intelligence, entrepreneurship, and statistics. His current research interests include the development and integration of decision support systems, business expert systems, and neural networks, especially regarding the incorporation of uncertainty. A member of AAAI, ACM, AMS, ASA, IEEE, INNS, and SIM, he received a Ph.D. in mathematics from Rutgers University and has been a visiting professor at the Massachusetts Institute of Technology.
