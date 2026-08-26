---
otero_id: 19243
otero_key: "GAKNCAE7"
title: "An objective, entropy-based approach to evaluating migration issues in computer IS"
authors: "Roy Martin Richards"
year: "1995"
journal: "Information & Management"
doi: "10.1016/0378-7206(95)00035-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# An objective, entropy-based approach to evaluating migration issues in computer IS

Roy Martin Richards, Jr. \*

Department of Business Computer Information Systems, College of Business Administration, University of North Texas, Box 13677. Denton TX 76203-3677. USA

## Abstract

Recent breakthroughs in computing technology have created a set of perplexing new problems for information systems (IS) professionals. These revolve around decisions to be made about replacing current systems with newer technology, upgrading existing systems, and migrating to other platforms or environments. Many decision makers must rely on subjective assessments, such as their instincts or the recommendation of vendors rather than on an objective analysis of their information needs and how they can be met by various system alternatives. A model to quantify these issues, providing an objective measure for comparing system alternatives, including migration, would be valuable. Such a model is demonstrated here; it uses the Shannon–Weaver entropy model in conjunction with quality measures to quantify actual and potential system effectiveness.

Keywords: Information systems; Migration; Entropy; Quality

## 1. Introduction

Major technological advances in computer hardware and software, while creating new opportunities for system solutions, have created an entirely new set of problems for systems professionals. Questions such as, “Is our current system doing all that it can for us?” and “Should we move to another platform?”, or “If we change to another environment, which is the best?” are causing system managers much concern in their efforts to optimize the effectiveness of IS. Many systems professionals experience frustration in their deliberations, because no objective approach to analysis of alternatives is accepted as effective.

Total Quality Management (TQM) has created some inroads into the problem of identifying such phenomena as nonconformance with user requirements and system quality, even though some research indicates there may be potential for errors and biases in user response data, but it falls short of providing an objective measure of effectiveness that can be used to compare system alternatives $[10]$ . It has been shown that the quality of the planning process and the quality of implementation mechanisms are associated with the performance of the system $[15]$ . In the absence of quantitative measures, systems professionals may find themselves relying on more abstract criteria such as their own personal preferences or the information provided by somewhat less-than-objective sources, such as vendors and competitors [1]. An objective model is needed to aid in the building of an appropriate IS architecture [11].

This paper presents a successful model based on the Shannon–Weaver [17] maximum entropy principle, a model developed in the late 1940's in communication studies, and based on the second law of thermodynamics. One might wonder why such a model would apply to computer systems? The answer to that question is explained by general systems theory [20]. When used in conjunction with the concept of nonconformance to user requirements, the maximum entropy principle provides a model for assessment of quality by estimating the entropy of the system, leading to an objective measure of its effectiveness and a technique for comparing systems [8]. Entropy-based measures have been used successfully before in IS, especially in software engineering, but not in terms of a total system concept [9]. Assuming that this approach provides an acceptable estimate, entropy is relatively low in systems exhibiting high conformance with user requirements (relative conformance) and relatively high in systems with low levels of conformance. The identification of a distinct and thorough list of user requirements and a mechanism to monitor nonconformance provide the link between entropy, system quality, and performance.

## 2. Background literature

Migration is a relatively new topic, brought about by recent breakthroughs in chip speed, reduced instruction set computing, and the need for more flexibility and lower costs. The response to improvements has been dramatic. Recently it was reported that sixty percent of respondents to an annual survey of MIS managers plan to target PC's and work stations for their longer term applications development, indicating that the pace of migration has accelerated at large corporations [7]. Although the mainframe still has a firm place in enterprise architectures, the perceived need for graphical user interfaces (GUI) and advanced capabilities of local area networks (LAN) have caused a shift in computing platforms [12]. According to O'Connell [14], the debate is no longer whether to shift functions from the mainframe to smaller environments but how best to accomplish the task so that the added benefits of the new system exceed the costs of the changeover, thus maximizing system value $[13]$ . For large companies, networking has become synonymous with systems reengineering and substantial cost reductions can be achieved, especially in the area of file migration $[18,19]$ . The firm must be able to identify user needs, communicate them to systems personnel, know how to accomplish the system goals, and have a strategy to accomplish the move $[2]$ . Total commitment of top management is also critical to the effort $[5]$ , as is a realistic set of user expectations (see Other sources, Zellner and Highfield, 1988), and an appropriate method of system auditing $[22]$ .

Bozman [3] reports that forty to fifty percent of current applications could be removed from the mainframe by 1996 but warns that the process is not inexpensive. Up-front costs are high and there is a time-consuming learning curve associated with migration, the initial rewriting of applications being most difficult. The decision to migrate to another environment is complex and subject to many pitfalls.

Many mainframe systems can be reengineered but companies must determine the suitability of a given application for the LAN environment and how the transition can best be made. According to Rao [16], the selection of system candidates for migration must be accomplished by performing an analysis of the current system including usage, complaints, system failures, and system successes. This “efficiency audit” must focus on current components and usage but must also look to future needs, users, and management. With the requirement for interoperability across platforms and the need to involve more than one brand of hardware or software, additional challenges face the systems professional in choosing the correct platform for a given setting. The need for a means to quantify the issues is clearly indicated. The maximum entropy model provides such a tool.

The Shannon–Weaver entropy model defines the entropy of a discrete set of probabilities as:

$$
H = - \Sigma (p _ {i} \log p _ {i})
$$

for a set of n independent events whose probabilities of choice are $p_{1}$ , $p_{2} \ldots p_{n}$ . Since the logarithms of numbers less than one are negative, the minus sign is necessary to be consistent with physical entropy, in which a decrease in entropy shows greater structure (or an increase gives less information content). When choosing between only two possible events whose probabilities are $p_{i}$ and $(1 - p_{i})$ , respectively, H is minimized when the probability of one alternative is equal to one (certainty) while the other is zero; it is maximized when the probability is 0.5. In this format, the maximum entropy model is stochastic, in that it produces entropy according to certain probabilities and is subject to a Markoff process, since the probabilities depend on previous events. It is also an ergodic system, that exhibits a “particularly safe and comforting sort of statistical regularity” [17]. For such reasons, the Shannon–Weaver model, with its roots in science and engineering, has proved highly attractive to IS and communications researchers.

One specific application is the Shannon diversity index [23]:

$$
H ^ {\prime} = - \Sigma (p _ {i} \log_ {2} p _ {i}),
$$

where $p_{i}$ is estimated from $n_{i}/N$ as the proportion of the total population of individuals (N) belonging to the ith species ( $n_{i}$ ); here, $H'$ measures the diversity in a many-species community. This index accounts for both relative abundance as well as the number of species and provides a structure within which probabilities of nonconformance in systems can be estimated [4].

## 3. The species diversity index

The Markoff process, in which probabilities depend on previous events, requires they be dependent on one another. Because user requirements can often be viewed as independent events, a method to treat nonconformance is needed. The Shannon–Weaver diversity index provides such a method: the number of instances of nonconformance for a requirement out of conformance $(n_{i})$ compared to the total number of nonconformances during a given time period $(N)$ provides an estimate of the probability of nonconformance. Species become nonconformances for our purposes.

Crucial to the entropy model is the event whose probability is being estimated, in this case, the probability of a given lack of conformance to known and measurable user requirements. Since the process is Markoff, the sum of the probabilities of the events must be one. This requires the identification of each lack of conformance over time for each requirement, and then dividing the number of instances of nonconformance for each user requirement by the total number of nonconformances to estimate the proportion of nonconformance for each user requirement. Only the user requirements not being met would be included for any given time period. If many requirements are out of conformance by only one factor each (low probability), H will be high. If there is only one item out of conformance, H will be low.

This information is valuable in at least two ways. First, the relative entropy value is a reflection of the disorder in the system over a given time period. Second, entropy values for different candidate systems can be estimated and compared with their effectiveness and cost.

## 4. Information capabilities of the entropy model

The entropy function is an estimate of the randomness or lack of structure of a system. To test the initial version of the model, two organizations were chosen to illustrate the extremes of the scale of system performance.

The first organization, Firm A, is a group of professionals using a network for processing activity data during the course of a day; for this, they require access to various data sets on the network. They just installed a new system and are highly satisfied with its performance. However, they are experiencing two persistent problems. In addition to other user requirements, the response time must be under one second for users of its network, and the number of ports must be sufficient for all authorized users who want to gain access to the system. To assess whether these user requirements were being met, Firm A logged nonconformances for a chosen time interval of one week. It was found that there were five instances of lack of conformance during that time, four incidents of response time that exceeded specifications and one instance of a user not being able to gain access due to the lack of an unused port. For this example, the sum of incidents of nonconformance would be five and the number of nonconformances to the response time requirement would be four giving a probability of 0.80 that if a nonconformance occurred, the nonconformance would be response time, and a probability of 0.20 that such a nonconformance would involve the lack of an available port. Since

$$
\begin{array}{r l r} H ^ {\prime \prime} = & - \Sigma (p _ {i} \log_ {2} p _ {i}) & \text { then } \\ H ^ {\prime \prime} = & - 0. 8 0 ^ {*} \log_ {2} 0. 8 0 & = 0. 2 5 8 \\ + & - 0. 2 0 ^ {*} \log_ {2} 0. 2 0 & = 0. 0 9 2 \\ & & = 0. 3 5 0. \end{array}
$$

In this case, $H''$ is relatively low, indicating a low state of entropy because only two items are out of conformance. If the indicated nonconformances are corrected, the system will approach the state of “zero defects” and will have even lower entropy. This is merely an indicator of the relative state of disorder in the system and does not reflect the relative costs involved. For example, in a mainframe system, a disk drive that is out of order would cause the same type of problem as a disk drive out of order in a microcomputer system. The costs of correcting the problems would, however, vary greatly. The cost issue is discussed later.

Now let us consider Firm B; they had many system problems. They had no clear set of user requirements, they just knew that something was wrong. A slightly different approach was taken. They set out to identify occurrences that they believed to be lack of conformance and used a detailed logging process.

The log showed the following problems during the trial week: their system crashed three times, they ran out of disk space twice and of main memory five times, the printer jammed once, the number of dial-up ports proved inadequate twelve times, and their Graphic User Interface (GUI) went down twice, forcing them to restore their system from hard disk backup files. Clearly, there are many requirements that are not being met with many occurrences of each.

The calculation for $H''$ in the case of Firm B produces a relatively large value. Table 1 lists the data used to make the calculations and shows $H''$ to be 2.11. This relatively high level of entropy indicates the system needs improvement. Action is indicated to improve system performance. The goal of system management is to reduce $H''$ by eliminating, as far as possible, all nonconformance and achieving close to zero defects. Again, the costs will vary for independent nonconformances across platforms, but the entropy calculation, while not the entire story, is a necessary first step towards estimating and managing costs.

While these two examples show extremes, they show how the model can be used to estimate entropy and indicate a promising potential for the effective use of this model.

## 5. Comparing systems using the entropy model

After calculating the entropy of two or more systems, the measures could be used to compare them. Instead of dealing with observed lack of correct performance over time, estimates can be made of how well a given solution addresses user requirements. For example, suppose one user requirement for a system may be the provision of a Graphic User

Illustration of entropy calculation for firm B

<table><tr><td>Event</td><td>Number of Occurrences</td><td>Probability</td><td> $p_i \log_2 p_i^*$ </td><td> $p_i \log p_i^*$ </td></tr><tr><td>System crash</td><td>3</td><td>0.12</td><td>0.37</td><td>0.11</td></tr><tr><td>Disk Space</td><td>2</td><td>0.08</td><td>0.29</td><td>0.09</td></tr><tr><td>Main Memory</td><td>5</td><td>0.20</td><td>0.46</td><td>0.14</td></tr><tr><td>Printer jam</td><td>1</td><td>0.04</td><td>0.19</td><td>0.06</td></tr><tr><td>Ports notavailable</td><td>12</td><td>0.48</td><td>0.51</td><td>0.15</td></tr><tr><td>Restore System</td><td>2</td><td>0.08</td><td>0.29</td><td>0.09</td></tr><tr><td>Total</td><td>25</td><td>1.00</td><td>2.11</td><td>0.64</td></tr></table>

While numbers are actually negative, they are reported as positive since the minus sign in the summation formula will change their sign upon summation.

Interface (GUI). Any system based on 16-bit or lower technology may create nonconformance today. While less expensive, much functionality is lost by not procuring new technology, so the value for $H''$ would be high. Alternatively, obtaining a system based on 32-bit technology would result in fewer problems running the GUI and $H''$ would be low, indicating less probable entropy than the 16-bit system but at a higher cost.

It is not uncommon for decision makers to opt for less expensive “solutions” to their systems problems. Cost savings may be realized up front, but they must be balanced against future expenditures necessary to replace outdated technology. Thus, entropy may be inadvertently designed into the system. If a system manager expects to save short term dollars by purchasing old technology with its inherent entropy, that expectation must be balanced by the realization that such a decision will simply defer the cost into the future, not avoid it, and will allow only suboptimal utilization of the system due to its limited capabilities for its entire life span. However, it has been noted that keeping up with the latest technology can bankrupt a firm and that for a firm that is out of business, entropy means virtually nothing. Clearly a balance must be sought between the entropy in the existing system and the firm’s ability to reduce nonconformance. At least, the entropy model provides an estimate for decision making concerning the balance.

## 6. Quantifying the cost of entropy

The entropy model seeks to minimize $H''$ subject to a thorough analysis of user requirements and a philosophy of zero defects. $H''$ can then be minimized. All instances indicate a relative level of entropy which is manifested in a price of nonconformance. There is a cost of entropy and (PONC) provides an indication of that cost which is estimable [6]. As entropy increases, the PONC also increases and vice versa, given equal levels of technology. To compare the PONC for a microcomputer system with PONC for a mainframe may be ill-advised given independent events (failures) have different costs. The relationship should hold for equivalent system platforms.

In estimating entropy, specific nonconformances are identified and their respective probabilities derived as a proportion of the whole, providing a measure of regularity of occurrence. By estimating the sum of all direct and indirect costs associated with the nonconformance in a given system at a certain level of technology, an average measure of cost can be provided for each occurrence in that system. Those that occur regularly and cost a great deal of money to correct will probably be given priority over less-regular occurrences that are not very costly while those exhibiting a relatively low frequency and cost per occurrence will probably be considered less of a priority. Considering that there are two costs for a nonconformance, direct and indirect, a cost function might look like this:

$$
C = \Sigma (D _ {i} + I _ {i}),
$$

where $D_{i}$ and $I_{i}$ are the direct and indirect costs, respectively, for the ith nonconformance. It is, of course, assumed that these costs can be estimated. From this, the mean cost of a nonconformance in a given system would be C/N, where N is the total number of nonconformances. Various other statistical measures would also be appropriate, given the attributes of the entropy model, from which this is derived. The association of estimated costs with specific system nonconformances, for which relative contribution to total entropy can be calculated, provides decision criteria as to a level of expenditure appropriate to bring a given requirement into conformance. So,

$$
C _ {i} = p _ {i} ^ {*} \left(D _ {i} + I _ {i}\right)
$$

represents the expected cost per review period for the ith nonconformance. The ratio of $C_{i}$ to $H_{i}$ gives a cost per unit of entropy measure for the given nonconformance, which simplifies to:

$$
\left(D _ {i} + I _ {i}\right) / \left(\log_ {2} p _ {i}\right).
$$

The cost/entropy measure becomes the cost of an occurrence of nonconformance divided by the logarithm base 2 of its probability.

There are three types of information provided by this ratio. If cost is low and nonconformance (entropy) is high, the ratio produced will be low, indicating many small but less costly occurrences. If cost is high and nonconformance low, a less than adequate job of identifying nonconformance or requirements might be indicated. In the unlikely event that cost and nonconformance are close in value, results will contain very little information until absolute values of the variables are examined as well as the relative values produced by the ratio of cost to nonconformance. The ideal state would be to combine low PONC with low entropy indicating a cost effective system in the early stages of its lifetime and in compliance with a well-defined set of user requirements.

## 7. Summary

For some time now, systems professionals have sought evaluation models for information systems, generally with only limited success. Adapting the entropy model to information systems as a tool for evaluation of the system migration problem provides some promise.

Some form of an entropy calculation can be made for information systems by using a careful statement of user requirements and with a review of their lack of conformance in the given system. As entropy goes up, quality goes down.

Using this model, relative entropies for alternative system platforms can be estimated. The system alternative exhibiting the lowest entropy may be preferred in the long run. The evaluation model should be helpful to systems professionals in making recommendations for computer information systems.

## 8. Other sources

Arizona, Y. Cui, and H. Ohta, “An Analysis of M/M/s Queuing Systems Based on the Maximum Entropy Principle”, Journal of the Operational Research Society, Vol. 42, Issue 1, January, 1991, pp. 69–73.

Attaran and M. Zwick, “Entropy and Other Measures of Industrial Diversification”, Quarterly Journal of Business & Economics, Vol. 26, Issue 4, Autumn, 1987, pp. 17–34.

Bejan, “Advanced Energy Systems: Minimizing Entropy in Thermal Systems”, Mechanical Engineering, Vol. 111, Issue 8, August, 1989, pp. 88–91.

Stuart Bretschneider and Dennis Wittmer, "Organizational Adoption of Microcomputer Technology: The Role of Sector", Information Systems Research, Vol. 4, No. 1, March, 1993, pp. 88–108.

A. Carroll, “Is the Mainframe Dead, Dying, or Just Convalescing?”, CMA Magazine, Vol. 66, Issue 8, October, 1992, pp. 15–20.

Delgado and S. Moral, “Reliability Concepts Under the Theory of Evidence”, European Journal of Operational Research, Vol. 35, Issue 1, April, 1988, pp. 89–97.

Faegre, “Lessons from a Seasoned Downsizer”, Computerworld, Vol. 26, Issue 32, August 10, 1992, p. 68.

Golany and F.Y. Phillips, “A Maximum-Entropy Based Heuristic for Density Estimation from Data in Histogram Form”, Decision Sciences, Vol. 21, Issue 4, Fall, 1990, pp. 862–881.

Varun Grover, Myun Joong, and James T.C. Chen, “A Descriptive Study on the Outsourcing of Information Systems Functions”, Information and Management, Vol. 27, Issue 1, July, 1994, pp. 33–44.

Juhani Iivari and Irja Ervasti, “User Information Satisfaction: IS Implementability and Effectiveness”, Information and Management, Vol. 27, Issue 4, October, 1994, pp. 205–220.

J. Lee, and P.B. Kantor, “A Study of Probabilistic Information Retrieval Systems in the Case of Inconsistent Expert Judgments”, Journal of the ASIS, Vol. 42, Issue 3, April, 1991, pp. 166–172.

T. Lee, “An Information-Theoretic Analysis of Relational Databases-Part I: Data Dependencies and Information Metric”, IEEE Transactions on Software Engineering, Vol. SE-13, Issue 10, October, 1987, pp. 1049–1061.

Y. Lee, S.M. Alexander and J.H. Graham, “A Diagnostic Expert System Prototype for CIM”, Computers and Industrial Engineering, Vol. 22, Issue 3, July, 1992, pp. 337–352.

Lawrence Loh and N. Venkatraman, “Diffusion of Information Technology Outsourcing: Influence Sources and the Kodak Effect”, Information Systems Research, Vol. 3, No. 4, December, 1992, pp. 334–358.

Maasoumi and S. Zandvakili, “Generalized Entropy Measures of Mobility for Different Sexes and Income Levels”, Journal of Econometrics, Vol. 43, Issues 1 and 2, Jan/Feb, 1990, pp. 121–133.

Ronald E. McGaughey, Jr., Charles A. Snyder, and Houston H. Carr, “Implementing Information Technology for Competitive Advantage: Risk Management Issues”, Information and Management, Vol. 26, Issue 5, May, 1994, pp. 273–280.

Maximum Entropy in Action: A Collection of Expository Essays, Brian Buck and Vincent A. Macaulay (Eds.), Oxford: Clarendon Press; New York: Oxford University, 1991.

C. Rodrigues, “A Proposed Entropy Measure for Assessing Combat Degradation”, Journal of the Operational Research Society, Vol. 40, Issue 8, August, 1989, pp. 789–793.

Stonier, “Towards a New Theory of Information”, Journal of Information Science Principles & Practice, Vol. 17, Issue 5, 1991, pp. 257–263.

Bernadette Szajna, and Richard W. Scamell, “The Effects of Information System User Expectations on Their Performance and Perceptions”, MIS Quarterly, Vol. 17, Issue 4, December, 1993, pp. 493–516.

S. Tsao, J., S.C. Fang and D.N. Lee, “On the Optimal Entropy Analysis”, European Journal of Operational Research, Vol. 59, Issue 2, June 10, 1992, pp. 324–329.

S. Wu and W.C. Chan, “Maximum Entropy Analysis of Multiple-Server Queuing Systems”, Journal of the Operational Research Society, Vol. 40, Issue 9, September, 1989, pp. 815–825.

T. Young, “Is the Entropy Law Relevant to the Economics of Natural Resource Scarcity?”, Journal of Environmental Economics & Management, Vol. 21, Issue 2, September, 1991, pp. 169–179.

Yourdon, Modern Structured Analysis, Prentice-Hall, Englewood Cliffs, New Jersey, 1989.

Zellner and R.A. Highfield, “Calculation of Maximum Entropy Distributions and Approximation of Marginal Posterior Distributions”, Journal of Econometrics, Vol. 37, Issue 2, February, 1988, pp. 195–209.

## References

[1] Ritu Argarwal, Linda Roberge, and Mohan R. Tanniru, “MIS Planning: A Methodology for Systems Prioritization”, Infor-

mation and Management, Vol. 27, Issue 5, November, 1994, pp. 261–274.

[2] Rajiv D. Banker and Chris F. Kemerer, “Performance Evaluation Metrics for Information Systems Development: A Principal-Agent Model”, Information Systems Research, Vol. 3, No. 4, December, 1992, pp. 379–400

[3] J.S. Bozman, “Downsizing, Rightsizing, Somethingsizing”, Computerworld, Vol. 27, Issue 1, December 28, 1992/January 4, 1993, pp. 6–7.

[4] J.E. Brower, J.H. Zar and C.N. von Ende, Field and Laboratory Methods for General Ecology, Third Edition, Wm. C. Brown Publishers, Dubuque, Iowa, 1990.

[5] C. Bruno, “Downsizing from the Top Down”, Network World, Vol. 8, Issue 23, June 10, 1991, pp. 39–40, 50.

[6] P. Crosby, Quality Improvement Through Defect Prevention, Philip Crosby and Associates, Winter Park, Florida, 1985.

[7] R. Francis, “Downsizing: The Application Migration”, Datamation, Vol. 38, Issue 23, November 15, 1992, pp. 36–48.

[8] Amy W. Gatian, “Is User Satisfaction a Valid Measure of System Effectiveness?”, Information and Management, Vol. 26, Issue 3, March, 1994, pp. 119–131.

[9] Warren Harrison, “An Entropy-Based Measure of Software Complexity”, IEEE Transactions on Software Engineering, Vol. 18, Issue 11, November, 1992, pp. 1025–1029.

[10] Ellen M. Hufnagel and Christopher Conca, “User Response Data: The Potential for Errors and Biases”, Information Systems Research, Vol. 5, No. 1, March, 1994, pp. 48–73.

[11] Young-Gul Kim and Gordon C. Everest, “Building an IS Architecture”, Information and Management, Vol. 26, Issue 1, January, 1994, pp. 1–11.

[12] Nancy Kronenberg, Thomas R. Benson, and Wayne M. Cardoza, “Porting Open VMS from VAX to Alpha AXP”, Communications of the ACM, Vol. 36, Issue 2, February, 1993, pp. 45–53.

[13] Vijay S. Mookerjee and Brian L. Dos Santos, “Inductive Expert System Design: Maximizing System Value”, Information Systems Research, Vol. 4, No. 2, June, 1993, pp. 111–140.

[14] B. O'Connell, "Networking", CFO Magazine, Vol. 8, Issue 6, June, 1992, pp. 47–55, 57.

[15] G. Premkumar and William R. King, “The Evaluation of Strategic Information System Planning”, Information and Management, Vol. 26, Issue 6, June, 1994, pp. 327–340.

[16] A.V. Rao, “Moving Mainframe Applications to LANs”, Business Communications Review, Vol. 22, Issue 11, November, 1992, pp. 43–48.

[17] C.E. Shannon and W. Weaver, The Mathematical Theory of Communication, The University of Illinois Press: Urbana, 1949.

[18] Olivia Sheng, “Optimization of File Migration Policies in Distributed Computer Systems”, Computers and Operations Research, Vol. 19, Issue 5, July, 1992, pp. 335–351.

[19] Olivia Sheng, “Analysis of Optimal File Migration Policies in Distributed Computer Systems”, Management Science, Vol. 38, Issue 4, April, 1992. pp. 459–482.

[20] P.P. Schoderbeck, C.G. Schoderbeck and A.G. Kefalas. Management Systems, BPI-Irwin, Homewood Illinois, Third Edition, 1985.

[22] J. Christopher Westland, “Assessing the Economic Benefits of Information Systems Auditing”, Information Systems Research, Vol. 1, No. 3, September, 1990, pp. 309–324.

[23] R.G. Wetzel, Limnology, Second Edition, Saunders College Publishing, a division of Holt, Rinehart & Winston, Orlando, Florida.

![](/api/attachments/GAKNCAE7/fulltext/images/f3a5ab78b5b0d8a9059ea0ee00b1b55b02ae19a8ad2e6944e9f3903daa8d5e73.jpg)

Roy Martin Richards, Jr., is an Associate Professor of Business Computer Information Systems and Assistant Dean of the College of Business Administration at the University of North Texas in Denton. In his fourteenth year at UNT, Dr. Richards received his Doctor of Philosophy degree from the University of Georgia in 1978 after earning the Master of Business Information Systems and Bachelor of Arts degrees from Georgia State University in 1972 and 1970, re-

spectively. His recent research interests have included the system life/death cycle, assessment of effectiveness and performance in system roles, the relationship between level of IT expertise and decision making, and IS curriculum development. Recent publications have appeared in Information and Management, International Business Schools Computing Quarterly, Computers and Education, and Journal of Systems Management. Dr. Richards currently teaches a campus-wide computer literacy course and a graduate “topics” course, both of which have received excellent reviews.
