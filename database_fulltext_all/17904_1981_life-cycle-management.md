---
otero_id: 17904
otero_key: "RB6K4XEA"
title: "Life cycle management"
authors: "Carl Hammer"
year: "1981"
journal: "Information & Management"
doi: "10.1016/0378-7206(81)90003-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Life Cycle Management

Carl Hammer

Director, Computer Sciences, Sperry Univac, Washington, DC 20007, USA

Life Cycle Management of electronic computer/communications systems is maturing after thirty years of experimentation and some false starts. This holistic concept provides an improved framework for planning, implementation and control of electronic hardware or software systems. It effects of symbiosis between users and suppliers who are both concerned with reliability of hardware and software, cost-effectiveness of applications, and the impacts of a rapidly changing technology. Improved cooperation between hardware/software vendors and users will undoubtedly result in significantly better product designs and services as well as their more intelligent use by sophisticated and concerned management.

Keywords: Electronic Systems, Hardware, Life Cycle Management, Planning, Project Control, Software.

![](/api/attachments/RB6K4XEA/fulltext/images/d2c52130135da7992ee62cd430ca6f17b20377dc21e5c84cd5d9a5c3766a9cb1.jpg)

Dr. Carl Hammer joined Univac in 1955 to take charge of the first European Univac I Computer installation in Frankfurt, Germany. From 1959 to 1963, at RCA, he supervised the initial design of the Minuteman Communications Systems and software development for the Ballistic Missile Early Warning System. In January 1963 he returned to Sperry Univac as Director of Computer Sciences in Washington DC.

Dr. Hammer received his Ph.D. in mathematical statistics at the University of Munich, Germany in 1938. He is a Senior Member of the IEEE and a Fellow of the Association for the Advancement of Science. By appointment of the Executive Office of the President, he has been a member of the National Defense Executive Reserve since 1970. In June of 1973 he was given the Computer Sciences Man-of-the-Year Award by the Data Processing Management Association and in October of 1979 the Association for Computing Machinery conferred upon him the Distinguished Service Award.

## 1. Introduction

The life cycle concept is well established in biology, the science of living organisms. Also, such eminent historians as Herbert George Wells (1866–1946), Oswald Spengler (1880–1936), Arnold Joseph Toynbee (1889–1975), and Pitirim Alexandrovitch Sorokin (1889–1961) have applied it to societal organisms, seeking to explain the nations' roots and birth, their growth, decline and eventual demise. Management science, too, has finally adopted this concept in an attempt to improve the cost-effective selection, installation and operation of electronic systems.

In the post-industrial society managers have learned to cope with limited and often declining natural resources; but they have a wealth of data at their disposal. Two-hundred years ago, the cottage industry owner-manager had an abundance of natural resources but little factual data; furthermore he personally had full knowledge of everything that concerned business. His successor, the small business owner-manager, found it more convenient to employ specialized talents to help him manage. Later, economy-of-scale considerations fostered big industry, often conglomerate and international in character. Extremes of specialization became commonplace and corporate memory evolved as a collective concept without physical realization. In fact, today's corporations are reversing the trend by decentralizing into hierarchies of cost or profit-and-loss centers; only the logical sum of their activities is reflected in the annual corporate report. As corporate structures or goals change, new departments are created and old ones are abolished – although the latter event does not occur nearly as often as many antibureaucrats would wish.

Fundamental to the industrial process is the manufacture, distribution and consumption of goods, as envisioned by Wassily Leontieff in terms of economic input-output matrices. Few consumer goods are still handmade; they are manufactured in an industrial production line, especially set up for that purpose. If the product falls out of favor the line is shut down or assigned to a different product. Here we have three examples of hierarchical life cycles: The manufactured unit, the product of which it is representative, and the whole production line. The unit life cycle commences on the production line where it is assembled; it ends with its ultimate consumption, be it eaten, worn, or otherwise disposed of. Some consumer goods warrant regular maintenance; others receive unscheduled repairs during their life span. On the other extreme, the life of a production line begins with a management plan. A feasibility study and an economic analysis are made before the line is built and operated. It might shut down temporarily, to open again -- perhaps with another product. Like the proverbial cat, it may have many lives but we count them all as one. Only when its machinery is junked or removed from the premises do we record its demise, as it were of an aggregate form of virtual life.

Life cycle management is a new tool which focusses on three major, concurrent, functional aspects: Planning, monitoring, and control. Without loss of generality, this paper deals with the application of this concept to the environment of electronic systems. Thus we must take into account the explosive growth of the computer industry, where today's maxi is tomorrow's mini; where the dividing line between the two is rapidly fading, revealing an almost continuous spectrum of computing and communicating capabilities which range from very small, low and low-cost to incredibly large, fast and expensive systems. A variety of concepts must be dealt with: Distributed systems, networks, data base management, even privacy regulation and security requirements. Hardware capabilities march on relentlessly and we must forever develop more complex applications. Finally, we need to improve software productivity through application of tools appropriately called Software Engineering [5].

## 2. Definitions and Viewpoints

We adopt the notion that the LCM (Life Cycle Management) concept has much in common with process control It is a management tool designed to provide a truly holistic view of some project or identifiable management entity. Thus it deals with all aspects of this managerially captured entity, from its very inception to its final dissolution, encompassing all real and virtual costs that can be associated with the project. These costs must include the obvious such as salaries, buildings, equipment, maintenance, and development of software (both systems and applications). They must also include the non-obvious such as eventual termination of the project for whatever reasons, corporate overhead, research and development, etc. The termination phase often parallels the initiation phase of another system which may be more powerful, have a different mission, or be located at another site.

For a more precise definition of terms we may consult several Government publications. The Code of Federal Regulations 41, Public Contracts and Property Management, defines

System or Items Life: A forecast or projection of the period of time which begins with the installation of the systems or items and ends when the need for those systems or items has terminated. Systems or items life is established by the Government on the basis of its requirements and is usually set forth in the RFP. Systems or items life is not synonymous with actual life of the equipment.

The same publication lists two Prime Factors in the Selection of Equipment:

(1) Its capability to fulfill the system specifications, (2) Its overall costs, in terms of acquisition, preparation for use, and operation.

Further, OMB Circular No. A-109 states that:

Life Cycle Cost means the sum total of the direct, indirect, recurring, nonrecurring, and other related costs incurred, or estimated to be incurred, in the design, development, production, operation, maintenance and support of a major system over its anticipated useful life span.

The Circular also lists some of the overall costs to be considered: Personnel, equipment purchase price or rental, maintenance, site preparation and installation, programming, training and conversion.

Finally, DoD Directive 7920.1 lists six major phases for Life Cycle Management which are shown diagrammatically in Fig. 1. The same Directive also details a number of specific tasks for each of these six phases.

Some observations should help clarify this conceptual approach. First, there is the concurrency of proprojects, already mentioned, the overlap between the end of one life cycle and the beginning of another. Next, we must anticipate that difficulties will arise with increasing orders of (hierarchical) complexity, often attractively packaged under the guise of economy-of-scale. But many large organizations have learned a bitter lesson when trying to implement top-down corporate management information systems, ostensibly designed to penetrate all administrative and operational management levels. Such integration efforts have often failed because the required systems complexity exceeds our limited design capabilities.

LCM can be applied in isolation to a single project unit, at the "local level". By advancing one or more steps in the hierarchical management structure, we can apply LCM also to a number of projects under a "global" umbrella. In either case, LCM will be concerned with the definition of deliverables; yet the exogenous variables on the higher levels are perhaps more difficult to assess than on the local level. Of course, we may proceed hierarchically, from one level to the next, until we reach the top of the organizational structure, but with decreasing hopes of ever achieving system implementation and successful operations. The USSR's Gosplan is an example of the highest order of systems integration and control, but it may take another century before its feasibility can be established.

![](/api/attachments/RB6K4XEA/fulltext/images/fe2e4a58d8b4a4abcce8163ce3bfbfab83dc3f6af2cb065654acd48241d4df8c.jpg)  
Fig. 1. Six Phases and Thirty Tasks Detailed for Project Life Cycle Management.

To illustrate the difference between local and global viewpoints, let us look at a specific case taken from the user's domain. Under the local view we might study a specific acquisition project, say of an EJE (Remote Job Entry) terminal whose location is distant from the host computer system. We begin with the planning phase, issue an RFP, evaluate the vendors' responses, make a decision, prepare the needed software, install the machine and go operational by developing additional applications over the course of several years. The local viewpoint thus offers no complications and proceeds in isolation and out of context with the management plan for the host computer system.

Under the global view, the acquisition of this RJE terminal is considered a modification to the LCM plan for the overall system, perhaps only a minor perturbation. Nevertheless, as shown in Phase 5 of Figure 1, this event may require that we update the total system's LCM plan in terms of its increased cost and added space or manpower requirements; the increased load on the host machine may perhaps push it closer to saturation than anticipated. Management's decision to adopt either view must thus be justified and documented since the extrapolation of costs and computer resource requirements is not likely to be linear – even the type of non-linearity is not too well understood.

## 3. Modelling and Simulation

One of the great contributions made by operations research during the past quarter century is the model concept. Its application to electronic systems management greatly enhances our ability to control endogenous variables; we have also learned how to make a better assessment of the exogenous environment. Thus it is not surprising that life cycle management has greatly benefitted [19] from such model developments.

The LCM model is the formalized management tool for project planning, monitoring and control. There is heavy emphasis [8] on financial components, whether derived from real monetary transactions or from their virtual equivalents in terms of labor, materials, or indirect costs and opportunity revenues. The sophistication of such models knows no upper bounds but realism dictates that only those variables be captured which have a significant impact on the decision making process.

In order to avoid unnecessary detail, such models are usually developed in top-down fashion. As a result, they will exhibit an hierarchical structure which provides a gross view at the highest level and gives increasing detail in successively lower model strata. This approach has two advantages: It reflects the organizational structure and provides a cutoff of contributory factors at the noise-level.

Figs. 2A–D illustrate one such model [14] for the life cycle costs of a typical vendor's mainframe. The model is for a single processor selling for \$ 100,000; one thousand copies are to be manufactured. Figure 2A shows that the shipment history begins three years after authorization of the processor design; it reaches a peak after six years; it ends after ten. This is also the year during which the number of installed processors reaches its peak.

Fig. 2B details the cost components associated with this hundred million Dollar project. Development costs peak after the third year; they end with the fifth. Marketing costs start after the second year, peak after the fifth and fade out after the ninth. Manufacturing can not begin until development is well under way; associated costs begin with the fourth year, peak after the sixth and terminate after the ninth year as the production line is shut down. Maintenance costs start up after the fourth year; they stretch out into the twentieth year but peak after eleven. Minor sustaining costs account for less than one percent of the total costs.

The model shows little flexibility in the control of these costs, in agreement with the generally accepted mainframer's view. However, it permits some alternatives in collecting revenue from two sources: Outright sales, or rentals and leases. If all processors were sold outright, gross revenues would show an initial bulge, peak at the sixth year and terminate after the tenth. On the other hand, if all processors were leased, the revenue would climb to a peak in the tenth year and then start its gradual decline to the twentieth year, the end of the product's life span. Figure 2C tracks the aggregate costs and revenues accruing from these two sources, assuming that 70% are leased and 30% are sold. Combination of expenses and revenues finally produces a cumulative cash flow picture, shown in Figure 2D. All of this information would be used by management to assess its options which range from all-sold to all-leased. With an assumed interest rate of ten percent for the cost of money, the cross-over point occurs during the twelfth year. At year nineteen the all-lease option produces a cumulative gross profit of \$ 300 million against \$ 200 million for the all-sold option. The former incurs a negative cash flow during the first seven years while the latter turns the corner at year five. These and related matters are discussed most elegantly by Phister [14].

![](/api/attachments/RB6K4XEA/fulltext/images/18a9ff2f8e4a865ffce0d9938836c49650d8908198bdaba067825eb399053a42.jpg)

![](/api/attachments/RB6K4XEA/fulltext/images/40330ffbdd1bfc774b07b590ec0850a6a2502e3c80d3b88b3d0bedd36debd9fc.jpg)

![](/api/attachments/RB6K4XEA/fulltext/images/3dc136e517a52b59a947d52fdd9991d759be8fc2675bf781f83f8c2ade080351.jpg)

Fig. 2. Life Cycle Costs – Typical Hardware Processor: Mainframe Vendor's View.  
![](/api/attachments/RB6K4XEA/fulltext/images/70aa2c549cdd145582c01ca150c04c95d074da048ed4990fe1b4de82abe3d3df.jpg)

The model does justice to the financial detail for which it was developed. Needless to say that in the real world additional data would be required, beyond the five types of costs and the two categories of revenue shown here. But even this overview illustrates clearly why a cash-rich organization may wish to defer its revenues by leasing rather than selling its products. Conversely, a manufacturer with cash-flow problems may wish to promote outright sales, even convert some of his rentals to alleviate his financial problems.

## 4. The Users' Viewpoint

Few users will be concerned about the life cycle management problems facing mainframe manufacturers [21]. Their pertinent interest might be sparked by a desire to improve their bargaining position through knowledge of the supplier's financial status. Furthermore, the user's concern with pure hardware costs has greatly diminished as software and operational costs consume the major portion of his budget.

Consider, therefore, the holistic LCM view of a typical computer system. First, there are users with existing, smoothly running installations. Should they take the trouble to develop an LCM Model? The answer is a resounding "yes" for two reasons. First, the learning process which is part of this effort will cause few, if any, undesirable perturbations. With everything (seemingly) under control, it is much easier to develop and implement the needed cost accounting procedures for the model's implementation. Second, by being forced to dig deeply into the refined data base developed in such an effort, management may learn that the alleged smoothness of the operation was only superficial; that there exist, in fact, areas of turbulence signalling the need for management attention and action. Perhaps the most intriguing aspect arising from the development of an LCM model for existing installations is the need to develop and report "honest" data. A thorough analysis of cost and expense data often yields surprising insights into "creative accounting" or other deceptive tactics widely used.

Next, there is the new user who does not now have an EDP system: A new application is being implemented, independently from other users and their organizational components; or a new organization or department has been created. Here, LCM will be at its best, giving the responsible manager a great opportunity to “do things right” from the very beginning. He can establish his own time table with critical dates and event milestones; he has time to develop methods and procedures; he can derive detailed cost data and obtain management participation and approval.

Finally, there is the user whose operational system approaches saturation; he aims for a systems upgrade or replacement. In either case, LCM principles will help him pinpoint any components currently not under control. In making equipment changes, for example, the manager might consider software redevelopment, rather than conversion, of current applications for greater efficiency, increased scope, improved throughput. This will be especially important in the transition from batch oriented operations to realtime transaction processing.

During three decades of electronic management adventuren many users have experienced traumatic changes in terms of relative hardware and software costs. A recent study by AFIPS [13] indicates that in twenty years the cost-performance of hardware has improved a millionfold. Yet programmer productivity has, at best, only doubled in the same time. It has been intimated that perhaps one reason for this rather startling discrepancy is the fact that programmers can now waste with impunity a million times more machine power – it certainly appears as if they feel compelled to do just that!

It has been estimated [20] that for 1955 systems the hardware component exceeded eighty percent of the system life cycle costs; that by 1965 this fraction had dropped to fifty percent; and that it has been below twenty percent since 1975. Recent technology forecasts indicate that this asymptotic trend will continue; after 1985 software costs will likely exceed ninety percent of the systems life cycle costs!

Thus we can downplay hardware costs in our LCM models. Even the cost of hardware maintenance contributes little, despite its labor intensive aspects. Meanwhile, the cost of designing, developing and testing software is reaching astronomical proportions, despite methodological improvements, such as software engineering [5] and other sophisticated, widely available software tools [10].

Software specialists assert [20,22] that the life cycle cost of software products has two major components. The initial investment consist of problem analysis and program design, coding and unit testing, finally system tests and integration; these account for 40, 20 and 40 percent respectively of the total development cost. Much larger are the later costs which accrue from the maintenance of the software product as "bugs" are discovered and corrected, modifications are made to extend its use, or its components are rewritten for new hardware features. It always comes as a shock to management to learn that such operational maintenance costs are four to ten times greater than the initial investment in the software product!

One major cost element incurred by software maintenance results from the deplorable practice of ignoring the need for good documentation. Without it, maintenance on object codes is very difficult with assembly language; still an unsatisfactory exercise with undocumented high-level language source code [1]. The Federal Government of the United States is the largest computer user in the world. Thus it is not surprising that she has issued a whole series of Federal Information Processing Standards through the National Bureau of Standards. FIPS PUB 38 [9] deals specifically with software life cycle documentation.

In the management of a software project FIPS PUB 38 distinguishes three major phases. During the first (initiation) phase an appropriate program plan is developed and authorized. The second (development) phase has four stages; definition to design, to programming and testing. It concludes with product acceptance which comes at the beginning of the third (operational) phase. The emphasis during the second phase is first on documentation for functional and data requirements; second on specification documents for data base, programs and systems/subsystems, all of this before a single line of coding is written! Thirdly, the programming effort should be supported by at least three manuals for users, operations and maintenance. Finally, an extensive report about testing of program components and the entire system should be prepared. Despite its thoroughness, FIPS PUB 38 fails to mention the need for "unfriendly" program tests, conducted by a special team to complement "friendly" tests made by project programmers and coders.

## 5. Some Illustrative Examples

Industrial users of the LCM concept are reluctant to share data and experience with the general public. The reason most often cited is that such information is proprietary [7] and cannot be divulged without giving unfair advantage to the competition. However, the U.S. Government policy of critically examining its own operations provides several examples of interest.

A typical case study [17] is shown in Table 1. It details the cost benefit analysis for a specialized Internal Revenue Service computer with a ten-year economic life. The debit side for this special-purpose tax administration system adds up to the formidable figure of \$1,264.3 millions. The basic hardware cost of \$M260.5 represents 20.6 percent of the systems life costs, well within the earlier mentioned range. Even adding \$M84.5 for "Lease and Other Costs" raises hardware costs to less than twenty-seven percent as not all of this amount is for hardware. Unfortunately, figures for software maintenance (\$M121.9) and system development (\$M107.0) can not be compared as they include both hardware and software. Regardless, twelve million Dollars per year for software maintenance is not exactly a trivial amount! Finally, we observe that the "People Costs" exceed half-a-billion Dollars over ten years, reaffirming our assertion that electronic data processing [15, 16] after thirty years has become highly labor intensive.

On the credit side we find that the system will more than earn its keep. Computerized tax audits are expected to bring nearly a hundred million Dollars annually into the coffers of the Federal Government; processing of intelligence data would provide another twenty million Dollars per year. Preparing tax-payers' returns eliminates many erroneous filings with another plus of sixteen million Dollars annually on the credit side. Finally, during the months the system is not saturated with its primary function (say, July through December of each calendar year) the IRS expects to pick up another twenty-two million Dollars annually by selling unused computer resources to other government agencies. The bottom-line for this system life cycle is a respectable annual net gain of S M27.45 which pales only if we learn that in 1979 the IRS actual collected \$ 159,330,829,000 from individual taxpayers!

Another typical LCM case study (17) is shown in Table 2. It describes the cost-benefit analysis of a system in the Defense Logistics Agency. This example illustrates an interesting point: How does one quantify the benefits of military and/or defense operations? Although the GAO report indicates "Zero Dollars" for the quantifiable benefits, it must be intuitively clear to everyone that a much larger, positive number better describes the "value" of these benefits – but what is it?

In this second example we see additional evidence for the labor intensive nature of EDP. Only 12.8 percent of the initial investment is for hardware; annual operating costs equal nearly half of the total initial investment! Most of this initial cost, by the way, is for program conversion. This step is often unavoidable when we convert from second or early third generation systems – here we have an indication of the magnitude of such an effort.

## 6. Planning for Software Productivity

Now that we have established that software is indeed the major component in the life cycle cost of EDP systems we are naturally curious how to manage it more effectively, how to increase the productivity of software shops and what danger signals LCM can perhaps provide.

Frederick P. Brooks [6] observes that planning of a software project is its most important aspect. He recommends budgeting one-third of the total resources to it. One-sixth of the project funds should be allocated for coding and another quarter each to testing of initial program modules and the final system. Brooks also warns against crash assignment of additional staff to a software project which has slipped in its schedule. Indoctrination of the new team members to the project will only eat into the time of the old team, thus delaying the project even further.

David S. Alberts [2] examined the impact of programming errors on the life cycle cost of software. Such errors may occur early in the development phase, or later during the operational phase when software maintenance (i.e., change) is required. He found that about half of the software life cycle costs are attributable to errors which are made with equal probability in these two phases. Our inability to hold down the software error levels, especially in the development phase, is further supported by the work of Marc Bendick [4]. He analyzed several software products having from thirty to two hundred thousand lines of coding. He discovered that the average cost of 'repairing' an error made during the development phase but not discovered until the software attained operational status was 139 times greater than the cost of writing that one line in the first place!

Table 1 Cost Benefit Analysis: Internal Revenue System

<table><tr><td>Category</td><td>Adjusted Costs (Millions)</td><td>Category</td><td>Adjusted Benefits (Millions)</td></tr><tr><td>Development Cost</td><td>$ 107.0</td><td>Audit</td><td>$ 956.4</td></tr><tr><td>Capital Investment</td><td>260.5</td><td>Intelligence</td><td>195.2</td></tr><tr><td>Lease and other Costs</td><td>84.5</td><td>Tax Return Processing</td><td>164.8</td></tr><tr><td>Equipment Maintenance</td><td>137.9</td><td>Other</td><td>122.4</td></tr><tr><td>Software Maintenance</td><td>121.9</td><td></td><td></td></tr><tr><td>Operating Personnel</td><td>552.5</td><td></td><td></td></tr><tr><td>Total Costs</td><td>$ 1,264.3</td><td>Total Benefits</td><td>$ 1,538.8</td></tr></table>

Source: ref. [23].

Table 2 Cost Benefit Analysis: Department of Defense System - Development and Implementation Costs (Thousands)

<table><tr><td>Capital Cost</td><td></td><td>$ 8,455.9</td></tr><tr><td colspan="3">Conversion Costs</td></tr><tr><td>ADP Salaries</td><td>$ 22,406.5</td><td></td></tr><tr><td>Other Salaries</td><td>$ 23,314.1</td><td></td></tr><tr><td>Other</td><td>$ 20,156.4</td><td></td></tr><tr><td>Subtotal</td><td></td><td>$ 65,877.0</td></tr><tr><td>Total DoD Cost</td><td></td><td>$ 74,322.9</td></tr><tr><td>Annual Operating Costs</td><td></td><td>$ 38,200.0</td></tr><tr><td>Quantifiable Dollar Benefits</td><td></td><td>0</td></tr></table>

Source: ref. [24].

Thun we come to appreciate the enormous value of the tools collectively referred to as "Software Engineering". Alvin L. Kustanowitz [11] gives an excellent overview of how managers should monitor and control software production costs. He observes that "All programming projects have one thing in common: A Life Cycle. They begin and sooner or later, they end". But if we insist on simply good, common sense management principles, we can create an environment which is very conducive to improved productivity. Both Kustanowitz and Ware Myers [12] recommend the use of structured programming, top-down design and development, HIPO, chief programmer team operations, development support libraries and structured walkthroughs. Since neither author mentions specifically the need for quality documentation, we cannot resist the temptation to close this section by reprinting two important laws:

Hammer's Second Law: If it isn't documented, it doesn't count.

Hammer's First Law: Too many people ignore Hammer's Second Law.

## 7. Management Considerations

Life Cycle Management for EDP systems is not a static process, nor a one-shot event. As with many other management tools, it requires periodically revised planning horizons and many unscheduled updates. The initial LCM plan is conceived at the time when a project is first considered for authorization. At that time certain bounds are established for its scope and hierarchical levels. Specifically, management must decide then how "local" or "global" the LCM plan is to be. This decision is crucial as it determines the fundamental structure of the plan which cannot easily be altered later.

Within this frame of reference the LCM plan must capture all relevant cost data, both direct and indirect. General overhead costs, especially for global type plans, must be apportioned according to some agreed upon formula, authorized and approved by higher level management. This procedural approach will facilitate conflict resolution with other existing or planned LCM plans within the global organizational structure. It is also mandatory that appropriate accounting methods and procedures are put into place to allow identification and costing of all relevant financial data by category and type.

In the EDP environment two major categories are easily identified [3]. Hardware costs will involve the host computer, its satellites and terminals. Also included must be hardware maintenance, perhaps through a facilities management contract. Operations at central and remote sites as well as communication costs also fall into this category.

On the software side [18] the LCM plan will surely have to include development, conversion and maintenance of systems and applications programs; also training of systems analysts, programmers, coders and operators; and a projection of user support costs if the machine is used by groups and individuals from other departments.

The ground rule is quite simply that during the planning stage every conceivable cost or revenue category should be examined for relevance and possible inclusion into the LCM plan. Some of these data will be estimates and projections which require that applicable ratios be developed relating these figures to internal or external information sources. If model planners must resort to "guestimates" they can refine them during later cycles and planning horizons: A poor initial guess is still better than a non-entry into the complicated, hierarchically structured LCM Data Base.

Life Cycle Management can be an invaluable tool if properly supported and implemented. In the struggle for optimal utilization of our limited resources, LCM will pay for itself by providing the needed data base for better planning, monitoring and control of computer installations. It may well be the best, all-around firing insurance an EDP manager can obtain ...

## References

[1] ADP Project Management, Department of Defense Computer Institute, Washington Navy Yard, Washington DC 20374.

[2] David S. Alberts, The Economics of Software Quality Assurance, 1976 National Computer Conference, AFIPS Proceedings, Volume 45, pp. 433–442.

[3] Ramesh Barasia and Dave Klang, The Life Cycle Cost Model, Telesis, Volume 5, Number 12, December 1978. pp. 367–372.

[4] Marc Bendick, Error Rate as a Management Tool, 1976 National Computer Conference, Session F-5, 8 June 1976 (unpublished report)

[5] Barry W. Boehm, Software Engineering, IEEE Transactions on Computers, Vol. C-25, No. 12, December 1976, pp. 1226–1241.

[6] Frederic P. Brooks, Jr., Mythical Man-Month, Datamation, Volume 20, Number 12, December 1974, pp. 45–52.

[7] George A. Champine, Univac's Financial Model for Computer Development, Datamation, February 1977, pp. 53–57.

[8] Ray Caudill, Understanding the Developmental Life Cycle; Proceedings of the 1977 National Computer Conference, AFIPS Press, Volume 46, pp. 269–275.

[9] FIPS PUB 38, Documentation of Computer Programs and Automated Data Systems, National Bureau of Stan-

dards/U.S. Department of Commerce, 15 February 1976.

[10] Werner L. Frank, The New Software Economics, Computerworld, 1979, Part 1 (8 January), Part 2 (15 January), Part 3 (22 January), part 4 (29 January).

[11] Alvin L. Kustanowitz, System Life Cycle Estimation, IEEE COMPSAC 77, Proceedings, pp. 226–232.

[12] Ware Myers, The Need for Software Engineering, Computer (IEEE), February 1978, pp. 12–26.

[13] Philip S. Nyborg, Pender M. McCarter and William Erickson (eds.), Information Processing in the United States: A Quantitative Summary, American Federation of Information Processing Societies, Inc., Montvale NJ 1978.

[14] Montgomery Phister, Jr., Data Processing Technology and Economics, Santa Monica Publishing Company, 1976, pp. 234–236.

[15] Montgomery Phister, Jr., Analyzing Computer Technology Costs – Part I: Development and Manufacturing, Computer Design, September 1978, pp. 91–98.

[16] Montgomery Phister, Jr., Analyzing Computer Technology Costs – Part II: Maintenance, Computer Design, October 1978, pp. 109–118.

[17] Harold J. Podell, (U.S. General Accounting Office, Washington DC 20548) Life Cycle Costing of Computer Systems in the Federal Government, (Private Communication), 1978.

[18] Lawrence H. Putnam and Ann Fitzsimmons, Estimating Software Costs, Datamaticn, 1979, Volume 25; Number 10, September, pp. 188–198; Number 11, October, pp. 171–178; Number 12, November 1979, pp. 137–140.

[19] Virgil Rehg, A Life Cycle System Simulation, Proceedings, Fourth Annual Simulation Symposium, Gordon and Breach, 1971.

[20] Alfred E. Sorkowitz (U.S. Department of Housing and Urban Development, Washington DC 20410), Planning for Life Cycle Management (Private Communication), April 1978.

[21] Harold S. Stone, Life-Cycle Cost Analysis of Instruction-Set Architecture Standardization for Military Computer Systems, (IEEE-CS) Computer, Volume 12, Number 4, April 1979, pp. 35–47.

[22] Richard H. Thayer and John H. Lehman, Software Engineering Project Management, Dept. of the Air Force, Report SM-ALC/ACD TR-77-02, McClellan Air Force Base, CA 95652, 1 November 1977.

[23] GAO Report, 10 Year Economic Life for the Tax Administration System (LCD-76-114, 23 November 1976).

[24] GAO Report, Defense Logistic Agency, Defense Integrated System, Eight Year Economic Life (LCD-77-227, 20 December 1977).
