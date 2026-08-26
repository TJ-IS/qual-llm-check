---
otero_id: 10192
otero_key: "JZWDFUFK"
title: "Modeling the benefit of e-recruiting process integration"
authors: "In Lee"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.12.011"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Modeling the bene<sup>fi</sup>t of e-recruiting process integration

In Lee ⁎

Information Systems, School of Computer Sciences, College of Business and Technology, Stipes Hall 447, Western Illinois University, Macomb, IL 61455, USA

a r t i c l e i n f o

Article history: Received 3 March 2009 Received in revised form 2 December 2010 Accepted 23 December 2010 Available online 11 January 2011

Keywords: Business value Investment evaluation Information technology value

## a b s t r a c t

While e-recruiting has been widely adopted as one of the most successful e-business applications, it constitutes an under-researched area in e-business research. This study reviews the integration issues in erecruiting and presents an e-recruiting integration decision model. The bene<sup>fi</sup>ts of the investment in erecruiting process integration are discussed in comparison to separate e-recruiting investments. We show that the optimal investment in the e-recruiting process integration results in a lower total cost than the separate e-recruiting investments. In addition, in light of the widely practiced resource constrained investments, we present the method of Lagrange multipliers which is used to <sup>fi</sup>nd the optimal investment under a budget constraint.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Organizations face recruiting challenges arising from intense knowledge work, labor shortages, competition for applicants, and workforce diversity [38]. E-recruiting is bringing radical changes to recruiting and job search process for both recruiters and job applicants. Driven by competition, technological advancements, and the tight labor market, almost every company has developed its own corporate recruiting web sites. E-recruiting decreases information asymmetry between recruiters and job applicants. Job applicants become more knowledgeable about the companies they are interested in applying to before they make a decision to apply and accept a job offer.

E-recruiting has fundamentally changed the corporate recruiting process from a batch mode into a continuous mode [28]. Traditional recruiting process is typically paper-based and characterized by numerous hard-copy forms, hand-written signatures, and internal and external communications performed in a batch mode throughout the hiring process. While traditional recruiting process may still be effective in most industries, recruiters must face challenges including a long hiring cycle time, high cost per hire, low advertisement coverage, and ineffective candidate management. E-recruiting improves the recruiters' ability to handle job applications and job postings by minimizing paperwork and automating key recruiting activities.

Evidence of cost savings abounds in e-recruiting. According to Aberdeen Group [1], cost savings in hiring depends on the number of positions that a company needs to <sup>fi</sup>ll. Results of this study indicate that savings in one company that hires 10,000 new employees in a year averaged \$900 per hire and total savings reached \$9 Million. Recruiting cycle time also dropped by 50% to 63% in the companies studied. The study reported that job advertising costs for one company dropped from \$27,000 a year to less than \$2000. Another study also shows conservative savings due to reduced employee turnover, reduced staf<sup>fi</sup>ng costs, and increased hiring-process ef<sup>fi</sup>- ciencies [13]. The authors reported that these cumulative savings yielded a return on investment of 6.0 to 1 (i.e., a return of \$6.00 for every \$1.00 invested in the e-recruiting technology). They argued that the system coupled with the planned enhancements should increase greater hiring ef<sup>fi</sup>ciency, employee quality, and cost savings.

Despite the widely circulated e-recruiting success stories, some companies abandoned e-recruiting after years of experimenting with it and fell back to traditional recruiting sources such as employee referrals and newspaper advertisements [45,46]. These companies struggled with too many unquali<sup>fi</sup>ed job applicants <sup>fl</sup>ooding their erecruiting systems and could hardly provide the necessary timely resources to process the over<sup>fl</sup>owing applications. The resource waste stemming from the ineffective processing of many unquali<sup>fi</sup>ed job applications offset the cost savings. Furthermore, front-end recruiting processes such as job posting and back-end recruiting processes such as screening and selection were not well coordinated. Companies began to realize that various recruiting activities need to be integrated seamlessly along the entire recruiting process to take a full advantage of the e-recruiting technologies [2,9–11].

Organizations have been diligently keeping abreast with new advances in e-recruiting technologies. Web standards such as HR-XML and Web Services are quickly integrated into the e-recruiting tools. Web 2.0 technologies such as AJAX and RSS feeds enable the recruiting web sites to be simple, interactive, collaborative, and informative. These new technologies also affect job applicants' search activities. Job applicants are creating blogs, posting video resumes, and participating in discussion forums for prospective companies. Online social networking is becoming part of overall corporate erecruiting strategy and is recognized as an effective method to review information posted by job candidates, and to locate passive but quali<sup>fi</sup>ed job candidates.

While e-recruiting is the second most widely practiced e-business areas in organizations, it is a somewhat neglected area of research where further efforts to address its effective deployment and performance measurement are not only warranted but desperately needed. In this paper we build on a surprisingly sparse literature regarding e-recruiting process management to show that e-recruiting process integration matters in realizing cost savings.

The main purposes of this study are (1) to present an e-recruiting integration decision model, (2) to analyze the effects of the process integration, and (3) to develop an optimal investment method with a budget constraint. We will show how a conceptual level understanding of e-recruiting processes can be utilized to provide an optimal investment decision for e-recruiting process integration. This study proceeds with a review of literature related to e-recruiting, an overview of a base model of the e-recruiting investment, a decision model for e-recruiting process integration., the analysis of the bene<sup>fi</sup>ts of the e-recruiting process integration, discussions on the optimal investment method under a budget constraint, and a conclusion with future research directions of this study.

## 2. Literature review

Before we start our literature review on e-recruiting, it would be worth de<sup>fi</sup>ning e-recruiting. Barber [3: p. 5] offered the de<sup>fi</sup>nition of recruitment as “recruitment includes those practices and activities carried on by the organization with the primary purpose of identifying and attracting potential employees” By extending Barber's de<sup>fi</sup>nition, we de<sup>fi</sup>ne e-recruiting as a hiring process that utilizes a variety of electronic means and technologies with the primary purpose of identifying, attracting, and selecting potential employees. In addition, e-recruiting technologies are de<sup>fi</sup>ned as web-based technologies that help recruiters and job applicants to complete their tasks more ef<sup>fi</sup>ciently and effectively by automating recruiting processes and providing the information necessary for making appropriate decisions. These technologies include career web sites, applicant tracking system, job search agent, prescreening/self-assessment tools, talent management system, steaming videos, RSS feeds, candidate relationship management system, HRXML, and social media, to name a few.

The rapid growth of e-recruiting can be explained by transaction cost economics (TCE) theory, agency cost theory (ACT), and network externality effects, all of which have been widely investigated in ecommerce literature. TCE theoretically explains why an organization chooses a particular organizational form for transaction [17,47,48]. TCE states that if it is cheaper to produce what it can buy on the market, <sup>fi</sup>rms expand vertically to minimize external business transactions. Two key assumptions underpin the behavioral aspects of TCE; bounded rationality and opportunism [49]. Researchers have focused on the ways of utilizing IT to reduce coordination costs and transaction risks [16]. TCE has become a viable theory for explaining the consumer's on-line shopping behaviors. Stein<sup>fi</sup>eld and Whitten [44] extended the TCE literature and suggested that TCE can be used to explain the phenomenal growth of B2C and B2B e-commerce. Since consumers can purchase products/services from either an on-line or an off-line channel, it is reasonable to assume that consumers will choose the channel that has the lower transaction cost [31].

The rapid growth of e-recruiting can be explained by TCE. Erecruiting lowers transaction costs signi<sup>fi</sup>cantly for both recruiters and job applicants. In recruiting, transaction costs are incurred in job advertising, application processing, candidate evaluation, screening, and interviews. For recruiters, e-recruiting lowers job advertising and application processing costs, and provides transaction speed and access to larger labor markets. When compared with newspaper advertising, erecruiting enable companies to provide far more information to potential applicants, due to the interactive and multimedia capabilities of the Internet [33]. E-recruiting enables job seekers to conduct a much wider job search due to low search and application costs. Assuming they spend the same amount of time and money for on-line job search, job seekers are likely to <sup>fi</sup>nd more job openings from e-recruiting than from traditional recruiting sources. Job applicants will have a greater chance of getting job offers from better-<sup>fi</sup>t companies. On the company side, processing a large candidate pool becomes cost effective due to an automated screening and prescreening process, and recruiters will have a better chance of identifying more quali<sup>fi</sup>ed job applicants.

Along with the potential bene<sup>fi</sup>ts and opportunities, the need for an effective design of e-recruiting web sites has also arisen to materialize the transaction cost reduction. Poorly designed web sites have discouraged job applicants from submitting job applications on-line [12,35]. Related to the design issue of recruiting web sites are potential discrimination issues for on-line job applicants [18]. Security and privacy are also major concerns for on-line job applicants. Hackers may access corporate recruiting web sites and steal applicants' personal information. Recently, a Korean court ordered LG to pay \$700 per applicant to a total of 400 job applicants for the damage caused by the stolen personal information which was subsequently posted at another job board [15].

Different interests between principals and agents give rise to agency costs [23,40]. The goals and objectives of the principals and agents may not always fully correspond with each other, creating situations where the agents may not act in the best interests of the principals [23]. As companies grow, agency costs increase due to a rising complexity of management and control of the agents and a higher information asymmetry between the principals and the agents. Agency costs include costs of coordination and monitoring of operations, as well as opportunity costs arising when the agents make decisions that are not in the interests of the principals. Information technology (IT) has impacts on agency costs [20]. IT enables companies to lower agency costs through effective coordination and monitoring of agent activities. E-commerce is capable of reducing agency costs by effectively coordinating sales activities, monitoring web site activities, and improving customer communication. Likewise, e-recruiting reduces agency costs, since it facilitates the coordination and monitoring of activities among hiring managers, human resources staff, and job applicants.

Bene<sup>fi</sup>ts to network participation increase as the size of the network gets larger. This effect was labeled as network externality [24,25]. Shapiro and Varian [42] suggested that companies utilize the bene<sup>fi</sup>t of network externality in the formation of sales strategy. In the software industry, a positive effect of network externalities on price was observed [14]. General-purpose job boards such as Monster.com, HotJobs.com, and Careerbuilder.com are a recruiting intermediary and seek to take advantage of the bene<sup>fi</sup>ts of network externality. Numerous specialty job boards are also a many-to-many intermediary between recruiters and job applicants. When the job boards expand the network of recruiters and job applicants, bene<sup>fi</sup>ts to recruiters and job applicants grow signi<sup>fi</sup>cantly because they have a better chance of job-applicant match in a larger pool.

E-recruiting is becoming more sophisticated and ef<sup>fi</sup>cient with the adoption of new technologies and practices. Recently, some companies started to take advantage of on-line social networking such as MySpace, Facebook, and LinkedIn to recruit passive job candidates and to review information posted by job applicants [43]. Employees are encouraged to utilize electronic referral systems to notify their acquaintances and professional communities of newly available job opportunities. Companies started to use .jobs domain names as the Internet Top Domain. The jobs domain offers companies an effective conduit to direct job applicants to their corporate career web sites. A survey [43] shows that that companies with the .jobs domain often had better recruiting outcomes than the companies without such domain. Sound architecture is critical to the successful development of e-recruiting system. The architecture helps recruiters and system developers understand how various components of the e-recruiting system work together to achieve recruiting goals [30].

While early adopters achieved a short-term competitive advantage by reaching a broader pool of quali<sup>fi</sup>ed candidates in time of labor shortage, they could hardly create a sustainable competitive advantage with e-recruiting. Why can't e-recruiting technologies alone become the source of sustainable competitive advantage? Barney [5] suggested that advantage-creating resources must have four conditions: value, rareness, inimitability, and non-substitutability. E-recruiting technologies are now widely available in the form of in-house systems or integrated off-the-shelf software packages. As e-recruiting technologies become commoditized and easily substitutable, early adopters' advantages will be rapidly eroded.

While information system architectures are generally well established, the conceptual model of information systems for business process integration from a management perspective remains an open methodological issue [6]. In the past, heterogeneous information systems have evolved in organizations. Coordination of activities among these systems became costly and slow due to dif<sup>fi</sup>culty of inter-system communication. Enterprise resource planning (ERP) systems were introduced to overcome these process integration problems. The main technology behind ERP is the enterprise-wide database technology. Applications are built around the database and integrated with each other to support organization's functional units and managerial hierarchy. ERP vendors such as SAP and PeopleSoft started to introduce e-recruiting system modules which are fully integrated into their ERP systems.

A recent survey by ISACA [21] reveals that fewer than half of 1217 IT professionals have a shared understanding of value across the enterprise, and two thirds of them fail to fully measure it. Half of the respondents reported that accountability for the IT value measurements is delegated to the IT functions, not to the user departments. The lack of measurement leads to the suboptimal IT investment due to missed investment opportunities for value generating ITs or overinvestment to underperforming ITs. In light of the signi<sup>fi</sup>cant lack of IT valuation knowledge by the senior executives, it is urgent that IT researchers and professionals develop an education program to deliver executives the needed knowledge and skill sets.

A wide range of IT evaluation methodologies have been developed by researchers and practitioners including: simulation [27,34], option theory [4], IT portfolio management [22], business case [41], optimization approach [50], game theory [37,52], technology road-mapping [19], Activity Based Costing method [36], total value of ownership [32], and enterprise collaboration decision making protocol [51]. The challenge for IT managers is that the success of the translation of non-quanti<sup>fi</sup>able bene<sup>fi</sup>ts into <sup>fi</sup>nancial metrics often depends on the choice of justi<sup>fi</sup>cation methods and the validity of the assumptions made.

## 3. An e-recruiting investment decision model

This section provides an overview of the base decision model and presents a model of simultaneous investment decisions for erecruiting process integration. For a detailed discussion on the base model, refer to Lee [29]. With the overview of the base decision model as a backdrop, the simultaneous investment decisions will be discussed in Section 3.2.

## 3.1. Base decision model

Four major recruiting costs are identi<sup>fi</sup>ed in recruiting: <sup>fi</sup>xed recruiting, overstaf<sup>fi</sup>ng, understaf<sup>fi</sup>ng, and coordination costs. Fixed recruiting costs are typically dependent on the recruiting sources and are typically related to a recruiting setup process. For example, <sup>fi</sup>xed recruiting costs incurred by traditional newspaper advertising and recruiting agencies are generally more expensive than those of job boards and corporate career web sites. Coordination cost is dependent upon the business process. Overstaf<sup>fi</sup>ng and understaf<sup>fi</sup>ng costs per employee are relatively constant due to the requirement of the labor contract and are related to a staf<sup>fi</sup>ng process.

The development of the e-recruiting decision model was based on the author's experience as a recruiting manager at multinational corporations, analytical methods, and literature review. The e-recruiting decision model is based on a number of assumptions. It is assumed that the initiation of each recruiting cycle incurs a certain <sup>fi</sup>xed recruiting cost. Overstaf<sup>fi</sup>ng occurs when the number of hired employees is higher than that of employees needed for business operations. The overstaf<sup>fi</sup>ng cost is derived from the underutilized labor portion of the total salaries paid to the employees. Understaf<sup>fi</sup>ng occurs when the number of hired employees is lower than that of employees needed for business operations. The understaf<sup>fi</sup>ng cost is derived from the overtime costs of the employees who were assigned to the overtime work. Due to the in<sup>fl</sup>exibility in the labor market and changes in the business environment, a company is typically in either overstaf<sup>fi</sup>ng or understaf<sup>fi</sup>ng situation most of the time. The total overstaf<sup>fi</sup>ng and understaf<sup>fi</sup>ng costs are linearly related to the average number of overstaffed and understaffed employees during the planning period, respectively. An investment decision horizon, T, may span multiple periods. T is related to the life cycle of the speci<sup>fi</sup>c e-recruiting technologies under investment consideration. Therefore, T needs to be set to the life cycle of the e-recruiting technologies under consideration. When a company needs to upgrade the erecruiting technologies, the new investment should consider the life cycle of the upgrade technologies with a new hiring need.

The model assumes that the hiring occurs at a uniform rate. While there may be <sup>fl</sup>uctuations of hiring needs during the planning horizon, the <sup>fl</sup>uctuations usually cancel out over time. For this investment model, the <sup>fl</sup>uctuations would not affect the investment decision making. The number of recruiting cycles per planning horizon is related to when to make a hiring decision. The hiring decision will be made at the beginning of each recruiting cycle. The actual employment is a continuous process in e-recruiting as opposed to the traditional batch hiring process. In the batch hiring, all employees are hired at once at the beginning of each recruiting cycle. In the continuous hiring, the new employment occurs close to the time of turnover or downsizing.

The recruiting decision model is deterministic in that it assumes that the total number of new employees, recruiting setup cost, and staf<sup>fi</sup>ng cost are known and constant. There are many situations in which a deterministic model yields good results. Corporate recruiting is planned, predictable, and stable, and therefore the deterministic model is very appropriate in this study.

The estimation of parameter values is a very important and challenging process. Some value estimations may require simulation and/or observation of historical data. Delphi method is very useful to estimate the parameter values when historical values are not readily available. The typical Delphi method requires the experts to answer questionnaires in two or more rounds. After each round, a facilitator provides an anonymous summary of the experts' parameter estimates from the previous round as well as the reasons for their judgments. Then, experts are asked again to revise their earlier estimates in light of the estimates of other members in the group. During this repetitive process, the range of the parameter values will decrease and the group will converge towards the best estimate. The black box approach can be used when it is dif<sup>fi</sup>cult to estimate parameter values. For example, one may use a variety of e-recruiting technology options on a small trial basis and see how much improvement/saving can be obtained. The black-box approach will facilitate the understanding of the impact of the e-recruiting investment and provide estimates of parameter values from the trial-runs of the technology. E-recruiting investment decisions can be also supplemented with the use of AHP and voting [26]. For example, AHP can be used to incorporate qualitative decision criteria on top of the proposed decision model. Next we introduce the nomenclature we use throughout this paper and discuss a model formulation.

## 3.1.1. Nomenclature Input parameters

$C _ { e }$ annual cost of overstaf<sup>fi</sup>ng per new employee (\$/employee period)

$C _ { s }$ annual cost of understaf<sup>fi</sup>ng per new employee (\$/employee/ period)

$C _ { a }$ a <sup>fi</sup>xed recruiting cost per recruiting cycle

$E$ the number of annual new employees

o daily hiring need

r daily recruiting rate

θ staf<sup>fi</sup>ng process improvement factor

$$
\theta = \left(\frac {r - o}{r}\right) = 1 - \frac {o}{r}, \quad 0 \leq \theta \leq 1
$$

T planning period

Decision variable

$N ^ { * }$ the optimal number of employment per recruiting cycle

Output variables

$t _ { e }$ time period of excessive employment stated as a fraction of a planning period T

$t _ { s }$ time period of labor shortage stated as a fraction of a planning period T

$t _ { e } + t _ { s }$ one recruiting cycle t

$N _ { e } ^ { * }$ the optimal number of excessive employees (overstaf<sup>fi</sup>ng) per recruiting cycle

$N _ { e } ^ { * } / 2$ the average number of excessive employees (overstaf<sup>fi</sup>ng) in a recruiting cycle

$N _ { s } ^ { * }$ the optimal number of understaf<sup>fi</sup>ng per recruiting cycle $N _ { s } ^ { * } / 2$ the average number of understaf<sup>fi</sup>ng in a recruiting cycle

## 3.1.2. Model formulation

Then, the total recruiting cost (TRC) of new employees during a planning period is derived by:

$$
T R C = \frac {C _ {e} N _ {e} ^ {2} T \theta}{2 N} + \frac {C _ {s} (N - N _ {e}) ^ {2} T \theta}{2 N} + \frac {C _ {a} E}{N}.\tag{1}
$$

If the <sup>fi</sup>rst derivative of Eq. (1) is taken with respect to $N _ { e } ,$ set it equal to zero, and solved, we have an optimal $N _ { e } ^ { * }$

$$
N _ {e ^ {*}} = N \frac {C _ {s}}{(C _ {e} + C _ {s})}\tag{2}
$$

By substituting $N _ { e } ^ { * }$ in Eq. (1), taking the <sup>fi</sup>rst derivative with respect to N, setting it equal to zero, and solving, we have an optimal number of employees $N ^ { \ast }$ to be recruited per recruiting cycle.

$$
N ^ {*} = \sqrt {\frac {2 C _ {a} E (C _ {e} + C _ {s})}{C _ {e} C _ {s} \theta}}, (\text { Planning   period } T = 1).\tag{3}
$$

Fig. 1 depicts overstaf<sup>fi</sup>ng and understaf<sup>fi</sup>ng of employees and the impact of staf<sup>fi</sup>ng process improvement factor, θ, on the number of overstaf<sup>fi</sup>ng and understaf<sup>fi</sup>ng of employees. When all the employees to be hired per recruiting cycle are employed at the same time (i.e., instantaneous employment), the staf<sup>fi</sup>ng process improvement factor θ is equal to one. As employees are hired at a time close to the time when they are actually needed, the staf<sup>fi</sup>ng process improvement factor, θ, approaches to zero. When the staf<sup>fi</sup>ng process improvement factor, θ, reaches zero, the timing of the actual employments matches exactly with that of the hiring needs and the overstaf<sup>fi</sup>ng and understaf<sup>fi</sup>ng costs are equal to zero.

The hiring process is turning into a continuous process due to erecruiting. A smaller value of θ represents a higher level of continuous recruiting process due to the fact that the recruiting activities occur more frequently to meet the hiring needs during each hiring cycle. The decreasing of θ is attributable to the fact that among others, erecruiting enhances the streamlining of recruiting activities and accuracy of recruiting information, resulting in a better control of the hiring process. A perfect continuous hiring process is the just-in-time recruiting (i.e., as soon as there is a job opening, e-recruiting ful<sup>fi</sup>lls the speci<sup>fi</sup>c hiring need immediately). The practice of continuous hiring process enabled by e-recruiting is evident at major corporate erecruiting sites where job openings are posted continuously each day as compared to the traditional recruiting practices with which where job openings are posted periodically in a batch mode.

The number of recruiting cycles during the planning horizon T is $E / N ^ { * }$ where E represents the number of annual new employees and $N ^ { * }$ represents the optimal number of employment per recruiting cycle. For example, if E is 1000 and $N ^ { * }$ is 100, then the number of recruiting cycles is 10 and the length of each recruiting cycle is 0.1 (i.e., 1/10).

The mathematical procedures for the optimal investment decisions for recruiting setup process improvement and staf<sup>fi</sup>ng process improvement are detailed in Lee [29].

## 3.2. Simultaneous investment decisions for E-recruiting process integration

Even though e-recruiting is widely implemented at the organization, its bene<sup>fi</sup>ts may not be materialized without the integration of interdependent processes, as inef<sup>fi</sup>cient bottleneck activities delay the entire recruiting process. With e-recruiting technologies, it is relatively easy to improve the recruiting setup process. However, it is more complicated to coordinate the entire recruiting process. The bene<sup>fi</sup>ts of a fully automated, integrated recruiting system are frequently lost when the front-end e-recruiting setup process is ineffective. When interdependent processes exist, for example, the recruiting cycle for the front-end recruiting process should be synchronized with that for the back-end staf<sup>fi</sup>ng process to avoid any delay in the recruiting activities in the entire process.

![](/api/attachments/JZWDFUFK/fulltext/images/6fcce321f686a62be49394296dece09df1e8aff89d83495487f714f9a068d333.jpg)  
Fig. 1. Staf<sup>fi</sup>ng of employees and staf<sup>fi</sup>ng process improvement factor θ.

To improve the recruiting setup process and minimize overstaf<sup>fi</sup>ng or understaf<sup>fi</sup>ng costs, we develop a simultaneous investment decision model for e-recruiting process integration. We developed mathematical procedures to solve simultaneous investment decisions for e-recruiting system integration. Since we consider both setup process and staf<sup>fi</sup>ng process, investment cost of S for the recruiting setup process improvement and investment cost V for staf<sup>fi</sup>ng process improvement are included in Eq. (4).

$$
\text { Min } \quad T R C = \frac {C _ {e} N \left(\frac {C _ {s}}{C _ {e} + C _ {s}}\right) ^ {2} \theta}{2} + \frac {C _ {s} N \left(\frac {C _ {e}}{C _ {e} + C _ {s}}\right) ^ {2} \theta}{2} + \frac {C _ {a} E}{N}\tag{4}
$$

We assume that the $C _ { a }$ is an exponential function with a base e where an e-recruiting investment cost of S is related to the recruiting setup process improvement. A similar exponential function with base e and a logarithmic setup cost function to determine the optimal investment cost for the reduction of setup costs in the classic EOQ model [7,8,39]. An exponential investment function for the reduction of $C _ { a }$ is de<sup>fi</sup>ned in Eq. (5).

$$
C _ {a} = L + (H - L) e ^ {- \lambda S}, \quad S \geq 0\tag{5}
$$

where H is the highest <sup>fi</sup>xed recruiting cost incurred when there is no investment in e-recruiting technology and L is the lowest <sup>fi</sup>xed recruiting cost achievable by the investment of S for the setup process improvement. The mathematics of the procedure to derive the optimal solution for the technology investment is presented below.

The <sup>fi</sup>rst derivative of Eq. (4) is taken with regard to S and set to zero, and solved. The result is given by

$$
\frac {\partial C _ {a}}{\partial S} = - \frac {N}{E}.\tag{6}
$$

The <sup>fi</sup>rst derivative of Eq. (5) is taken with regard to S. The result is given by

$$
\frac {\partial C _ {a}}{\partial S} = - \lambda (H - L) e ^ {- \lambda S} = - \lambda (C _ {a} - L) <   0.\tag{7}
$$

Setting Eq. (6) equal to Eq. (7) results in Eq. (8).

$$
C _ {a} = \frac {N + \lambda E L}{\lambda E}\tag{8}
$$

The investment in the improvement of the staf<sup>fi</sup>ng process decreases the overstaf<sup>fi</sup>ng and understaf<sup>fi</sup>ng costs by narrowing the time gap between the point of employment and the time of the employment need. There exist two possibilities in reducing total overstaf<sup>fi</sup>ng and understaf<sup>fi</sup>ng costs: (1) reduction of overstaf<sup>fi</sup>ng and understaf<sup>fi</sup>ng cost per employee and (2) reduction of staf<sup>fi</sup>ng factor. In reality, the reduction of overstaf<sup>fi</sup>ng and understaf<sup>fi</sup>ng costs per employee is dif<sup>fi</sup>cult to achieve because it is bound by the requirements of the labor contract. On the other hand, staf<sup>fi</sup>ng is a technologyenabled process. Decreasing staf<sup>fi</sup>ng factor is achieved with the investment in a particular e-recruiting technology and accompanying business process redesign.

When θ is equal to 1, all new employees are assumed to start employment at the beginning of the recruiting cycle, resulting in the highest level of total overstaf<sup>fi</sup>ng and understaf<sup>fi</sup>ng cost (i.e., noninstantaneous employment). When θ is equal to 0, no overstaf<sup>fi</sup>ng and understaf<sup>fi</sup>ng costs are incurred (i.e., instantaneous employment). θ of 0 implies that all new employees start employment immediately when the needs for overtime assignments arise. Let V represent the investment in staf<sup>fi</sup>ng process improvement. Mathematically, the staf<sup>fi</sup>ng function is de<sup>fi</sup>ned as follows.

$$
\theta = G + (F - G) e ^ {- \beta V}, \quad G \leq 1 \text { and } 0 \leq \theta \leq 1\tag{9}
$$

where F is the highest staf<sup>fi</sup>ng factor incurred when there is no investment in e-recruiting technology and G is the lowest staf<sup>fi</sup>ng factor achievable by the investment of V. The estimation of the parameter values for F and G is a critical process for the validity of the model. Suppose we need to determine the values of F and G. The value of F can be assumed to be 1.0 (i.e., a complete batch processing). The value of G may require a considerable amount of thinking and parameter re<sup>fi</sup>nements. If a perfect just-in-time hiring is possible, the value of G would be 0.0. Otherwise, the best possible recruiting scenario needs to be developed to estimate G. As a simple example, suppose that a daily hiring need is 4 employees and on average 5 employees are hired daily during the recruiting cycle until all recruiting needs are met. Then, G is estimated to be 0.2 using $\begin{array} { r } { \theta = ( \frac { r - o } { r } ) = 1 - \frac { o } { r } , 0 \leq \theta \leq 1 } \end{array}$

The mathematics of the procedure to derive the optimal investment needed for the staf<sup>fi</sup>ng process improvement is presented below.

If the <sup>fi</sup>rst derivative of Eq. (4) is taken with regard to V and set to zero, and solved, then the result is given by

$$
\frac {\partial \theta}{\partial V} = - \frac {1}{\left(\frac {C _ {e} \omega + C _ {s} \eta}{2}\right) N}.\tag{10}
$$

The <sup>fi</sup>rst derivative of Eq. (9) with regard to V is given by

$$
\frac {\partial \theta}{\partial V} = - \beta (1 - G) e ^ {- \beta V} = - \beta (\theta - G) <   0.\tag{11}
$$

Setting Eq. (10) equal to Eq. (11) results in Eq. (12).

$$
\begin{array}{l} \theta = \frac {2 (C _ {e} + C _ {s}) + \beta G N C _ {e} C _ {s}}{\beta N (C _ {e} C _ {s})} \\ \text { Since } \frac {\lambda (C _ {a} - L)}{\beta (\theta - G)} = \frac {C _ {a}}{\theta}, \text { substituting } \frac {N + \lambda E L}{\lambda E} \text { for } C _ {a} \text { and } \frac {2 (C _ {e} + C _ {s}) + \beta G N C _ {e} C _ {s}}{\beta N (C _ {e} C _ {s})} \\ \text { for } \theta \text { results in Eq. (13) }. \end{array} \tag {12}
$$

$$
\frac {2 \left(C _ {e} + C _ {s}\right) + \beta G N C _ {e} C _ {s}}{\beta E C _ {e} C _ {s}} = \frac {2 \left(C _ {e} + C _ {s}\right) N + 2 \left(C _ {e} + C _ {s}\right) \lambda E L}{N C _ {e} C _ {s} \lambda E}\tag{13}
$$

By rearranging terms in terms of N in Eq. (13), we get Eq. (14)

$$
\frac {1}{2} N ^ {2} + \frac {(\lambda - \beta) (C _ {e} + C _ {s})}{\lambda \beta G (C _ {e} C _ {s})} N - \frac {(C _ {e} + C _ {s}) E L}{(C _ {e} C _ {s}) G} = 0.\tag{14}
$$

Deriving a quadratic solution for N from Eq. (14) leads to an optimal value of N in Eq. (15).

$$
N ^ {*} = - \Phi \Psi + \sqrt {(\Phi \Psi) ^ {2} + \frac {2 \Psi E L}{G}}\tag{15}
$$

where

$$
\Phi = \frac {(\lambda - \beta)}{\lambda \beta G}\tag{16}
$$

and

$$
\Psi = \frac {(C _ {e} + C _ {s})}{(C _ {e} C _ {s})}\tag{17}
$$

Given the optimal number of employment per recruiting cycle, $N ^ { * }$ $C _ { a } ^ { * } , { \theta } ^ { * } , S ^ { * }$ , and $\boldsymbol { \dot { V } } ^ { * }$ needed for recruiting process integration are given by:

$$
C _ {a ^ {*}} = \frac {N ^ {*} + \lambda E L}{\lambda E}\tag{18}
$$

$$
\theta^ {*} = \frac {2 (C _ {e} + C _ {s}) + \beta G N ^ {*} C _ {e} C _ {s}}{\beta N ^ {*} (C _ {e} C _ {s})}\tag{19}
$$

$$
S ^ {*} = \frac {\left(l n \frac {(C _ {a} ^ {*} - L)}{(H - L)}\right)}{- \lambda}\tag{20}
$$

$$
V ^ {*} = \frac {\left(l n \frac {(\theta^ {*} - G)}{(F - G)}\right)}{- \beta}.\tag{21}
$$

Note that the optimal number of employment per recruiting cycle, $N ^ { * }$ is the same for both front-end recruiting setup process and backend staf<sup>fi</sup>ng process, leading to coordinated recruiting activities between the two processes.

## 3.2.1. Critical value for e-recruiting process integration decision

Even though process integration is desirable for many business applications, the investment for process integration typically requires a larger amount of resource (e.g., money) than an investment in a single process. In e-recruiting, evidence shows that as the number of employees to be recruited increases, the bene<sup>fi</sup>t of the investment increases due to the effect of setup cost and staf<sup>fi</sup>ng cost reduction per hire. Therefore, the minimum number of employees to be recruited serves as a critical value for the process integration. That is, if the number of employees to be recruited is smaller than the critical value, the process integration is costly.

The minimum number of employees to be recruited during a planning period for the optimal investment in the setup process improvement is given by

$$
E \geq \frac {- 2 \Psi \big ((H - L) \lambda \Phi - \frac {L}{G} \big)}{(H - L) ^ {2} \lambda^ {2}}.\tag{22}
$$

The minimum number of employees to be recruited during a planning period for the optimal investment in the staf<sup>fi</sup>ng improvement process is given by

$$
E \geq \frac {G \left[ \left(\frac {2 \psi}{\beta (1 - G)} + \Phi \Psi\right) ^ {2} - (\Phi \Psi) ^ {2} \right]}{2 \Psi L}.\tag{23}
$$

The larger number of employees between Eqs. (22) and (23) serves as the minimum number of employees to be recruited for the simultaneous investments in the e-recruiting integration.

## 4. Analysis of e-recruiting process integration

This section examines experimentally the performance of different investment strategies discussed above and conducts sensitivity analyses for the simultaneous investment decisions for process integration by changing values of the important parameters. The base parameter values are presented below.

## 4.1. Base parameters

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$C_e$ $5000/planning period  
$C_s$ $6000/planning period  
$H$ $1000  
$L$ $200  
$F$ 1.0  
$G$ 0.1  
$\lambda$ 0.0004  
$\beta$ 0.0004  
Base $C_a$ $1000  
Base $\theta$ 1.0  
E 500
</div>

First, the critical value of 15 for e-recruiting integration was derived using Eqs. (22) and (23), and it is lower than the number of employees to be recruited, 500. Therefore, the investment in the erecruiting process integration is warranted. For comparison, Table 1 presents a summary of results for (1) no investment in e-recruiting, (2) optimal investment in $C _ { a }$ only, (3) optimal investment in θ only, and (4) simultaneous investment for the process integration (i.e., use the mathematical procedures provided in the previous section).

The results show that the optimal investment in $C _ { a }$ only and the optimal investment in θ only were able to reduce the total cost compared to the no investment in e-recruiting. The investment in both $C _ { a }$ and θ for the process integration performs better than the optimal investment in $C _ { a }$ only and the optimal investment in θ only, respectively. We observed that the bene<sup>fi</sup>t stems from the synchronized recruiting cycle for both the recruiting setup process and staf<sup>fi</sup>ng process.

Next, we examine how the number of employees to be recruited will affect the total recruiting cost. Industry evidence shows that the larger the number of employees to be recruited in a given period, the larger the cost saving of e-recruiting is due to economies of recruiting scale. Fig. 2 shows that as the number of employees to be recruited gets larger, the total cost difference gets smaller. This result indicates that when a large investment is required for any technology-enabled process improvement, the integration of multiple processes is more bene<sup>fi</sup>cial than when a small investment is needed.

Next, we examine how two e-recruiting processes interact with each other for the simultaneous optimal investment. To understand the interactions, we change $\alpha ,$ the investment effect rate for the recruiting setup process, while β is <sup>fi</sup>xed. Fig. 2 shows that as α increases, both S and V change systematically. V continues to decrease as α increases. However, S increases rapidly until α reaches 0.0003 and then decreases gradually. The investment difference between S and V becomes greater when α is greater than 0.0003. When α and $\beta$ are 0.0004, the difference in the optimal investments get the smallest. It is noted that as α increases, $V ,$ which is affected by $\beta ,$ continues to decline, but the rate of the decrease slows down. The results indicate that any changes in one process affect the performance of other related processes. Therefore, managers need to be aware of the possible interactions among related processes and conduct a systematic impact assessment when needs arise for process integration.

Comparison of different investment strategies.

<table><tr><td>Parameters</td><td>No investment in e-recruiting</td><td>Optimal investment in  $C_a$ </td><td>Optimal investment in  $\theta$ </td><td>Simultaneous investment in both  $C_a$  and  $\theta$  for process integration</td></tr><tr><td>Critical Value</td><td></td><td>8</td><td>6</td><td>15</td></tr><tr><td> $C_a^a$ </td><td></td><td>247.6454</td><td></td><td>335.4006</td></tr><tr><td> $\theta^a$ </td><td></td><td></td><td>0.135205</td><td>0.1677</td></tr><tr><td> $S^a$ </td><td></td><td>7052.065</td><td></td><td>4440.934</td></tr><tr><td> $V^a$ </td><td></td><td></td><td>8103.032</td><td>6468.26</td></tr><tr><td> $N^a$ </td><td>20</td><td>10</td><td>53</td><td>28</td></tr><tr><td> $TRC^a$ </td><td>52,223.30</td><td>33,040.46</td><td>27,305.64</td><td>23,294.68</td></tr></table>

<sup>a</sup> Optimal value.

![](/api/attachments/JZWDFUFK/fulltext/images/66c33af807e7e967337622ad65a013d9a8447d82569bf38a7c108a0a35b4ab12.jpg)  
Fig. 2. Optimal investment with regard to α.

Next, we change $\beta ,$ the investment effect rate for the staf<sup>fi</sup>ng process, while α is <sup>fi</sup>xed. Fig. 3 shows a similar investment pattern to that of the previous experiment. While V was always higher than S in the previous experiment, V is higher when $\beta$ is between 0.0002 and 0.0009. V decreases when $\beta$ is greater than 0.0002. We note that $\beta$ affects S. However, the effect becomes marginal when $\beta$ is greater than 0.0007.

Finally, by changing α and $\beta$ together, we obtained S and V for the process integration. Fig. 4 shows that as both α and β increase (i.e., the technologies for both processes become more cost effective), both C and V decline. While V is always greater than C, its decrease rate is faster than that of $S ,$ and both converge to the same investment level. The increase of the investment effect rates, and $\beta ,$ reduces the total investment level $( \mathrm { i } . \mathrm { e } . , \mathsf { S } + \mathsf { V } )$

## 5. Process integration under a budget constraint

While the previous integration method shows that there are simultaneous optimal investment points without a budget constraint, many companies have limited <sup>fi</sup>nancial resources and set an affordable level of information technology investment based on their enterpriselevel investment plan. Therefore, we present a method for optimally allocating limited <sup>fi</sup>nancial resources for process improvement. Our study utilizes the method of Lagrange multipliers to <sup>fi</sup>nd the optimal investment under a budget constraint. First, to apply a budget constraint on the investments, S and V, we introduce the following minima function and a Lagrange multiplier, ξ.

Optimal Investment over Change of β  
![](/api/attachments/JZWDFUFK/fulltext/images/70ce261d1fcbadf70f77e8d176f3af149949761b2692f4f3cd105cd3c177c2ce.jpg)  
Fig. 3. Optimal investment with regard to β.

![](/api/attachments/JZWDFUFK/fulltext/images/0a309f198d600c8ecd8f1c6e1b44032bee45e246cad2c324cae45b7c4641934a.jpg)  
Fig. 4. Optimal investment with regard to both α and β.

$$
\text { Min } \quad T R C = \frac {C _ {e} N \left(\frac {C _ {s}}{C _ {e} + C _ {s}}\right) ^ {2} \theta}{2} + \frac {C _ {s} N \left(\frac {C _ {e}}{C _ {e} + C _ {s}}\right) ^ {2} \theta}{2} + \frac {C _ {a} E}{N}\tag{24}
$$

Subject to $S + V = B$ where B is a budget constraint.

The following function, Y, introduces the Lagrange multiplier, ξ.

$$
\begin{array}{l} Y (S, V, \xi) = \frac {C _ {e} N \left(\frac {C _ {s}}{C _ {e} + C _ {s}}\right) ^ {2} \theta}{2} + \frac {C _ {s} N \left(\frac {C _ {e}}{C _ {e} + C _ {s}}\right) ^ {2} \theta}{2} + \frac {C _ {a} E}{N} \\ \qquad + C _ {c} E + S + V + \xi (S + V - B) \end{array}\tag{37}
$$

To <sup>fi</sup>nd critical points for $Y ,$ solve the following system.

$$
Y _ {s} = \frac {C _ {a} ^ {\prime} E}{N} + 1 + \xi = 0\tag{25}
$$

$$
Y _ {v} = \left(\frac {C _ {e} \omega + C _ {s} \eta}{2}\right) N \theta^ {\prime} + 1 + \xi = 0\tag{26}
$$

$$
Y _ {\xi} = S + V - B = 0\tag{27}
$$

Given $N ^ { * }$ (the optimal number of employment per recruiting cycle), $C _ { a } ^ { * } , \theta ^ { * } , S ^ { * }$ , and $\boldsymbol { \dot { V } } ^ { * }$ needed for the recruiting process integration are given by:

$$
C _ {a} ^ {*} = \frac {N ^ {*} (1 + \xi) + \lambda E L}{\lambda E}\tag{28}
$$

$$
\theta^ {*} = \frac {2 (C _ {e} + C _ {s}) (1 + \xi) + \beta G N ^ {*} (C _ {e} C _ {s})}{\beta N ^ {*} (C _ {e} C _ {s})}\tag{29}
$$

$$
S ^ {*} = \frac {\left(l n \frac {(C _ {a} ^ {*} - L)}{(H - L)}\right)}{- \lambda}\tag{30}
$$

$$
V ^ {*} = \frac {\left(l n \frac {(\theta^ {*} - G)}{(F - G)}\right)}{- \beta}.\tag{31}
$$

Substituting Eqs. (28), (29), (30), and (31) into Eq. (32) and solve for ξ.

$$
S ^ {*} + V ^ {*} = B\tag{32}
$$

![](/api/attachments/JZWDFUFK/fulltext/images/826a6ce0ce6c4b76a7a18979450aea097765e0f58088707779211bce79edb6a3.jpg)  
Fig. 5. Change of optimal investment under a budget constraint.

Due to the logarithmic nature ${ \mathrm { 0 f } } S ^ { * }$ and $V ^ { * } ,$ we apply a simple linear search to <sup>fi</sup>nd the value of $\xi$ in Eq. (32) which satis<sup>fi</sup>es the budget constraint.

## 5.1. An illustrative example

For an illustrative example, we use the same parameter values as the ones used in Section 5. In Section $5 , S ^ { * } , V ^ { * } ,$ , and $T R C ^ { * }$ without the budget constraint were 4440.934, 6468.26, and 23294.68, respectively. In this illustrative example, we set the budget constraint to 5000. Applying the method of Lagrange multipliers, we <sup>fi</sup>nd the optimal investment points $( S ^ { * } , V ^ { * } , \xi )$ under the budget constraint of 5000 as (1486.39, 3513.71, 2.2604). $T R C ^ { * }$ is 28687.09. In this illustrative example, increasing the investment budget from 5000 to 5010 results in an approximate decrease in the total cost by 22.604 (i.e. 2.2604\*10).

Fig. 5 shows that as α and $\beta$ increase together, $S ^ { * }$ increases, but $V ^ { * }$ decreases. The investment pattern with the budget constraint is different from that without the budget constraint (refer to Fig. 5 for comparison). $S ^ { * }$ and $V ^ { * }$ with the budget constraint show a symmetrical investment pattern with the investment amount of 2500 as an axis.

Fig. 6 shows how α and $\beta$ affect the value of the Lagrange multiplier. The positive value of the Lagrange multiplier is called the marginal productivity of money and gives the approximate decrease in the total cost for a dollar spent on the investment. Fig. 6 shows that as α and $\beta$ increase together, ξ decreases, indicating the decreasing marginal productivity of money. Positive value of ξ would indicate that an underinvestment was made due to a budget constraint, and the negative value of $\xi$ would indicate that an overinvestment was made to meet a budget constraint.

![](/api/attachments/JZWDFUFK/fulltext/images/f32e46ec91f1ca4817145b836639a65273ef19a3e2bf7019134457a3d4045951.jpg)  
Fig. 6. Change of value of Lagrange multiplier.

## 6. Discussion

E-recruiting has changed the landscape in the labor market and become an irreversible trend. Most large business organizations are using e-recruiting as the primary method for job-searching and recruiting activity. Traditional recruiting methods have been plagued with high hiring costs and frequent hiring delays. The widespread adoption of corporate career web sites is driven by the rising cost and in<sup>fl</sup>exibility of using the third-party job boards and traditional media advertisements. E-recruiting is letting recruiters serve job applicants in ways that were unimaginable a few years ago. E-recruiting technologies and practices are keeping up with the advances of overall $\mathrm { e \mathrm { - } }$ commerce technologies, as are the knowledge and expectations of job applicants. The e-recruiting technologies expanded the reach of recruiting and the enhanced richness of information and made the job application simple and easy.

While the investment decisions for the recruiting setup cost and staf<sup>fi</sup>ng cost reduction in Lee [29] are made independent of each other, the simultaneous investment decision is made by considering the interdependence of the two decisions. ‘The simultaneous investment decision’ refers to the investment consideration in which both recruiting setup cost and staf<sup>fi</sup>ng cost decision variables are solved at the same time in the hope of saving the total recruiting cost further. The rationale for the simultaneous investment is to consider the interaction between the recruiting setup cost and staf<sup>fi</sup>ng cost. The separate investment decisions do not consider the interaction effect, and therefore are likely to result in the overinvestment in each cost category. The simultaneous investment decision will lead to a globally optimal investment, considering the interaction between the recruiting setup and staf<sup>fi</sup>ng cost.

Another important contribution is the development of a method for optimally allocating <sup>fi</sup>nancial resources under budget constraints for the recruiting setup cost reduction and staf<sup>fi</sup>ng cost reduction. Budget constraints are common in corporations. Due to limited <sup>fi</sup>nancial resources in companies, individual projects are frequently bound by budget constraints. Limited resources can be allocated based on a variety of budgeting criteria and portfolio of investment projects. Popular budgeting criteria include marginal productivity, return on investment, revenue level, or strategic considerations. The result shows the ef<sup>fi</sup>cacy of the Lagrange multipliers method which takes marginal productivity into the consideration of the budget allocation.

While business organizations are adopting e-recruiting at a fast rate, little has been known on the return-on-investment on the erecruiting process integration. We cannot emphasize enough the importance of technology investment management, as there is a cost/ bene<sup>fi</sup>t tradeoff and each organization has a different need for technology. Therefore, a legitimate question arises: will the investment in e-recruiting technology be <sup>fi</sup>nancially justi<sup>fi</sup>able? When the investment in e-recruiting technology is not carefully evaluated, the history of e-commerce overinvestment may repeat in e-recruiting.

## 7. Conclusions

We demonstrated how the conceptual level understanding of erecruiting processes leads to an e-recruiting investment decision for process integration. The e-recruiting investment decision model shows the implications of various investment options that would be overlooked without its use. Our results show that there exists a closed form solution for e-recruiting process integration, and the investment for process integration reduces the total cost signi<sup>fi</sup>cantly compared to the investment without process integration. As shown, the key to success in the e-recruiting technology investment lies not in the lavish investment, but in the sound e-recruiting technology decision.

We observed that as the number of employees to be recruited increases, the total cost for the process integration increase much slower than those of separate e-recruiting investments. Many companies set an affordable level of technology investment based on an enterprise-level investment plan. In light of the widely practiced resource constrained investments, we utilized the method of Lagrange multipliers to <sup>fi</sup>nd the optimal investment under a budget constraint. Given the Lagrange multipliers set to a constant, as the number of employees to be recruited increases, the cost savings of process integration under a budget constraint get larger than those of separate e-recruiting investments.

The operation of this model requires recruiters and human resources professionals to identify all the information needed to make an investment decision and recruiting plan. Relevant costs can be reasonably estimated as today's computerized accounting systems can easily store, retrieve, and sort costs and expenses related to recruiting activities. Certain parameters such as idiosyncratic investment functions may require estimations for which numerous scienti<sup>fi</sup>c methods such as Analytic Hierarchy Process (AHP), Nominal Group Technique, and Delphi Method coupled with group decision support systems can be combined.

While this study focuses on the e-recruiting investment, the proposed model is generalizable to any computerized recruiting applications as long as the applications help reduce the recruiting setup cost and/or staf<sup>fi</sup>ng cost. The use of the proposed model for other recruiting investment decisions would not require major modi<sup>fi</sup>cations of the existing model components, but needs a different set of parameter values and assumptions. For example, for the IT investment in the recruiting staf<sup>fi</sup>ng cost reduction, the lowest staf<sup>fi</sup>ng cost achievable by the investment in e-recruiting would be different from the lowest staf<sup>fi</sup>ng cost achievable by traditional computerized recruiting applications. In addition, the shape of the function for an e-recruiting investment cost would be different from that of the function for other computerized recruiting investment cost.

In our opinion, research opportunities abound in e-recruiting. It would be worthwhile to explore from a practical standpoint the issue of how e-recruiting process integration manifests in practice. Research on the perception of job seekers on different e-recruiting methods and web site attributes will give a valuable design guideline to recruiters. The longitudinal study of recruiting methods and their impacts on the quality and turnover rate of new hires may provide important information that can be used to optimize the mix of recruiting methods and budget allocations. Identifying and measuring success factors for e-recruiting and human resource information systems can be another interesting avenue of research.

## References

[1] Aberdeen Group, The e-recruiting payoff: the ROI of online hiring management systemsRetrieved from, https://www.talentxpress.com/collateral/E-recruiting. pdf, 2004.

[2] Asian Paints, SAP Customer Success Story Chemicals — Home Paint SolutionsRetrieved from:, http://download.sap.com/download.epd?context=C3DCAC97 C38795E4A6D537E29D2194030A46D6F5E1AA887C90DD32F07979A1AD8 C728EC0A95074561749F9C6185811CAFD870B87F416C2EA, 2007.

[3] A.E. Barber, Recruiting Employees, Sage Publications, Thousand Oaks, CA, 1998.

[4] I. Bardhan, S. Bagchi, R. Sougstad, Prioritizing a portfolio of information technology investment projects, Journal of Management Information Systems 21 (2) (2004) 33–60.

[5] J.B. Barney, Firm resources and sustained competitive advantage, Journal of Management 17 (March 1991) 99–120.

[6] J. Becker, A. Dreiling, R. Holten, M. Ribbert, Specifying information systems for business process integration — a management perspective, Information Systems and E-Business Management 1 (3) (2003) 231–263.

[7] P.J. Billington, The classic economic production quantity model with setup cost as a function of capital expenditure, Decision Sciences 18 (1) (1987) 25–42.

[8] P.J. Billington, Holding cost reduction in the EOQ model, Journal of American Academy of Business 3 (1) (2003) 409–415.

[9] C. Bizer, R. Heese, M. Mochol, R. Oldakowski, R. Tolksdorf, R. Eckstein, The impact of semantic web technologies on job recruitment processes, International Conference Wirtschaftsinformatik (WI'05), Springer, 2005, pp. 1367–1381.

[10] S. Bonadio, HR Field Guide 5 Tips to Effective Hiring & Recruiting. TheFreeLibrary Retrieved from: http://www.thefreelibrary.com/HR+Field+Guide+5+Tips+ to+Effective+Hiring+&+Recruiting-a01073981515, 2009.

[11] J.A. Breaugh, M. Starke, Research on employee recruitment: so many studies, so many remaining questions, Journal of Management 26 (3) (2000) 405–434.

[12] D. Brown, Unwanted job seekers swamp HR staff, Canadian HR Reporter 17 (7) (2004) 1–2.

[13] P. Buckley, K. Minette, D. Joy, J. Michaels, The use of an automated employment recruiting and screening system for temporary professional employees: a case study, Human Resource Management 43 (2–3) (2004) 233–241.

[14] S. Chakravarty, K. Dogan, N. Tomlinson, A hedonic study of network effects in the market for word processing software, Decision Support Systems 41 (4) (2006) 747–763.

[15] Ilbo Chosun, Retrieved from: http://news.chosun.com/site/data/html\_ dir/2008/01/03/2008010300938.html, 2008.

[16] E.K. Clemons, M.C. Row, Information technology and industrial cooperation: the changing economics of coordination and ownership, Journal of Management Information Systems 9 (2) (1992) 9–28.

[17] R.H. Coase, The nature of the <sup>fi</sup>rm, Economica 4 (16) (1937) 386–405.

[18] G. Flynn, E-recruiting ushers in legal dangers, Workforce 81 (4) (2002) 70–72.

[19] P. Groenveld, Roadmapping integrates business and technology, Research Technology Management 40 (5) (1997) 48–55.

[20] V. Gurbaxani, S. Whang, The impact of information systems on organizations and markets, Communications of the ACM 34 (1) (1991) 59–73.

[21] ISACA, Retrieved from: http://www.isaca.org/About-ISACA/Press-room/News-Releases/2009/Pages/Nine-country-ISACA-Survey-andnbsp-andnbsp-Twothirds-of-Companies-Not-Fully-Measuring-IT-Value-Negl.aspx, 2009.

[22] M. Jeffery, I. Leliveld, Best practices in IT portfolio management, MIT Sloan Management Review 45 (3) (2004) 41–49.

[23] M.C. Jensen, W.H. Meckling, Theory of the <sup>fi</sup>rm: managerial behavior, agency costs and ownership structure, Journal of Financial Economics 3 (October 1976) 305–360.

[24] M.L. Katz, C. Shapiro, Network externalities, competition, and compatibility, American Economic Review 75 (3) (1985) 424–440.

[25] M.L. Katz, C. Shapiro, Technology adoption in the presence of network externalities, Journal of Political Economy 94 (1986) 822–841.

[26] S. Koch, J. Mitlöhner, Software project effort estimation with voting rules, Decision Support Systems 46 (4) (2009) 895–901.

[27] I. Lee, Evaluating business-process integrated information technology investment Business Process Management Journal 10 (2) (2004) 214–233

[28] I. Lee, The evolution of e-recruiting: a content analysis of Fortune 100 career web sites, Journal of Electronic Commerce in Organizations 3 (3) (2005) 57–68.

[29] I. Lee, An analytical model of e-recruiting investment decision: an economic employment approach, IEEE Transactions on Engineering Management 52 (4) (2005) 486–496.

[30] I. Lee, An architecture for a next-generation holistic e-recruiting system, Communications of the ACM 50 (7) (2007) 81–85.

[31] T.P. Liang, J.S. Huang, An empirical study on consumer acceptance of products in electronic markets: a transaction cost model, Decision Support Systems 24 (1) (1998) 29–43.

[32] J. Luftman, H. Muller, Total value of ownership: a new model, Optimize 4 (7) (2005) 51–54.

[33] H.L. Murphy, Top job sites, Marketing News 33 (1999) 13–17.

[34] D.L. Olson, M. Shipley, M. Johnson, N. Yankov, Capturing the high-risk environment of the transition economy in Bulgaria — a simulation-based DSS, Decision Support Systems 42 (4) (2007) 2004–2015.

[35] M. Pastore, Web expands role in corporate recruitingRetrieved from, http://www. clickz.com/showPage.html?page=330331, 2000.

[36] E. Peacock, M. Tanniru, Activity-based justi<sup>fi</sup>cation of IT investments, Information & Management 42 (3) (2005) 415–424.

[37] E. Pettersen, A.B. Philpott, S.W. Wallace, An electricity market game between consumers, retailers and network operators, Decision Support Systems 40 (3–4) (2005) 427–438.

[38] R.E. Ployhart, Staf<sup>fi</sup>ng in the 21st century: new challenges and strategic opportunities, Journal of Management 32 (6) (2006) 868–897.

[39] E.L. Porteus, Investing in reduced setups in the EOQ model, Management Science 31 (8) (1985) 998–1010.

[40] S. Ross, The economic theory of agency: the principal's problem, American Economic Review 63 (2) (1973) 134–139.

[41] J.W. Ross, C.M. Breath, Beyond the Business Case: New approaches to IT investment, MIT Sloan Management Review 43 (2) (2002) 51–59.

[42] C. Shapiro, H.R. Varian, Versioning: the smart way to sell information, Harvard Business Review 76 (November–December 1998) 106–114.

[43] Society for Human Resource Management, Advances in e-recruiting: leveraging the jobs domainRetrieved from:, http://www.shrm.org/hrresources/surveys\_ published/22007%20Advances%20in%20E-Recruiting%20Leveraging%20the%20. Jobs%20Domain%20Survey%20Report.pdf, 2007.

[44] C. Stein<sup>fi</sup>eld, P. Whitten, Community level socio-economic impacts of electronic commerce, Journal of Computer Mediated Communication 5 (2) (1998)8 Retrieved from: http://icmc.indiana.edu/vol5/issue2/steinfield.html

[45] UK Net Guide, The Pros and Cons of Online RecruitmentRetrieved from:, http:// www uknetguide.co.uk/Employment/Article/The Pros and Cons of Online Recruitment-100038 html.2009

[46] Washington Federation of State Employees, E-recruiting ends — well, sort ofRetrieved from: http://wfse.blogspot.com/2009/09/e-recruiting-ends-wellsort-of.html, 2009.

[47] O.E. Williamson, Markets and Hierarchies: Analysis and Antitrust Implications, The Free Press New York 1975

[48] O.E. Williamson, Transaction-cost economics: the governance of contractual relations, Journal of Law and Economics 22 (2) (1979) 233–261.

[49] O.E. Williamson, The Economic Institutions of Capitalism, The Free Press, New York, 1985.

[50] D.J. Wu, P.R. Kleindorfer, Y. Sun, Optimal capacity expansion in the presence of capacity options, Decision Support Systems 40 (3–4) (2005) 553–561.

[51] S.W. Yoon, S.Y. Nof, Demand and capacity sharing decisions and protocols in a collaborative network of enterprises, Decision Support Systems 49 (4) (2010) 442–450.

[52] K. Zhu, J.P. Weyant, Strategic decisions of new technology adoption under asymmetric information: a game-theoretic model, Decision Sciences 34 (4) (2003) 643–675.

In Lee is a professor in the School of Computer Sciences in the College of Business and Technology at Western Illinois University. He received his Ph.D. from University of Illinois at Urbana-Champaign. He is a founding editor-in-chief of the International Journal of E-Business Research. He has published his research in such journals as Communications of the ACM, IEEE Transactions on Systems, Man, and Cybernetics, IEEE Transactions on Engineering Management, International Journal of Production Research, International Journal of Production Economics, Computers and Education, Computers in Human Behavior, Computers and Operations Research, Computers and Industrial Engineering, Business Process Management Journal, Journal of E-Commerce in Organizations, International Small Business Journal, and others. His current research interests include e-commerce technology development and management, investment strategies for computing technologies, and intelligent simulation systems
