---
otero_id: 22463
otero_key: "79XT75QG"
title: "A comprehensive approach to assess the value of EDI"
authors: "Martijn R Hoogeweegen; Robert J Streng; René W Wagenaar"
year: "1998"
journal: "Information & Management"
doi: "10.1016/s0378-7206(98)00052-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A comprehensive approach to assess the value of EDI

Martijn R. Hoogeweegen $^{a,*}$ , Robert J. Streng $^{1,b}$ , René W. Wagenaar $^{2,c}$

$^{a}$ Erasmus University, Rotterdam, The Netherlands

$^{b}$ Origin Consulting, Utrecht, The Netherlands

$^{c}$ Free University Amsterdam and KPN Research, Leidschendam, The Netherlands

Received 28 February 1997; accepted 31 March 1998

## Abstract

We describe a comprehensive approach that helps to assess the value of various courses of action that can be taken in implementing Electronic Data Interchange (EDI). The approach consists of two components. The first relies on Activity-Based Costing and quantifies the costs and benefits that are to be expected in the information processes when EDI is being used. The second uses discrete-event computer simulation to quantify the costs and benefits to be expected in the physical logistic processes. The combination of the two results in an overall costs/benefits analysis for a diverse set of EDI scenarios. © 1998 Elsevier Science B.V. All rights reserved

Keywords: EDI; Simulation; Value assessment; Costs/benefits analysis; Information economics

## 1. Introduction

It is widely believed that the large-scale use of Electronic Data Interchange (EDI) leads to improvements in the communication infrastructure between organizations, and that this, in turn, strengthens the economy of a nation and possibly a group of nations. This is reflected in the foundation of the EDIFACT standardization boards and the stimulation programs initiated by several national and supranational governments (e.g. the TEDIS program of the European

Community). It is also widely recognized that EDI enables organizations to redesign their processes significantly (see e.g. [3]), because of its three main capabilities: high speed, reliability, and ease of data capture [21].

Despite these arguments in favor of EDI, organizations are still reluctant to implement it, unless they are forced to do so $[5, 15, 24]$ . One of the reasons for this is that companies do not know whether and to what extent they should invest in EDI and they are unable to assess the return on these investments. The managing director of Intis Inc., the EDI network provider in the Rotterdam port community (Netherlands), described this problem: “As long as it is not possible to give a clear overview of the costs and benefits of EDI and the way in which doing business will change, decision-makers in organizations will give priority to other investments than EDI, despite the fantastic and ‘obvious’ benefits.”

Business managers have alternative courses of action available in their use of EDI. They constitute a dilemma when they are all regarded as unsatisfactory. This basically involves a choice of two possibilities:

\- investing in EDI without knowing the costs, the benefits, and the consequences;

\- not investing in EDI and running the risk of missing opportunities.

In order to resolve this, the expected costs and benefits of EDI investments should be assessed prior to implementation. In recent years several methods have been proposed to assess these benefits. However, none of them are able to capture the full spectrum of potential benefits that may result from EDI implementation. In this paper we propose a new approach that is based on two previously developed methods: it combines Activity-Based Costing (ABC) with simulation in order to assess a more complete range of possible benefits of EDI in business process redesign projects.

## 2. Value elements of EDI

The three capabilities of EDI (speed, reliability and ease of data capture) enable organizations to redesign their processes. A wide range of benefits may arise and these can be classified in different ways. Firstly, benefits can be divided into those that can be quantified (the tangible benefits) versus those which cannot (intangible benefits). Secondly, benefits can be divided into those that are information processing-related versus those that accrue from improving the physical processes of an organization. The combination of these provides us the following matrix (Fig. 1).

Benefits that belong to categories A and B are, in fact, ‘displacement’ benefits. They accrue due to a change in a particular performance indicator, like costs and lead time; for example, EDI may lower current communication costs (a category A benefit). The communication cost level in an EDI-based situation may be lower than the cost without EDI. We term the difference as an EDI benefit. Category A benefits refer to the costs that are related to the exchange of information between organizations. They can be divided into communication, labor, and material. Category B benefits refer to the performance indicators that are related to the physical processes of an organization. The indicators are resource utilization, inventory costs, and lead time. In contrast to benefits that belong to categories A or B, benefits of category C refer to value adding on strategic advantages over competitors. They are often discussed in the literature (see e.g. [4, 6, 18, 19], but are very difficult to assess quantitatively.

![](/api/attachments/79XT75QG/fulltext/images/53f83f1c6ffcfd780d0c2634f20fb9f93fa7ab7e7a41055c1e94401311301cfd.jpg)  
Fig. 1. Classification of benefits.

Over the last 15 years, a wide variety of methods have been developed to assess the expected benefits of IT investment. Only recently, EDI-investments have become the subject of such assessment methods. Those discussed in the literature vary in scope and type of benefits they assess. Farbey et al. [8] made a taxonomy of evaluation methods based on the appropriateness of the method to the system, the organizational context, and the purpose of the evaluation. Here, we focus on how EDI-investments can be assessed in terms of category A and B benefits. Therefore, we are looking for a method that meets the following requirements:

\- It should allow for a focus on EDI-type investments; that is, be able to capture the relationship between intra- as well as inter-organizational processes. Therefore, the method should deal with the interdependence of benefits between organizations. Such benefits occur when an organization benefits from EDI when its partners implement EDI properly and are willing to change the way that they do business [17].

\- It should provide results that support business managers in the EDI decision making process. Therefore, results should be quantitative (preferably in terms of money saved), traceable, and recognizable. Thus the manager must be able to follow the process of applying the method within his or her organization. By recognizable, we mean that the manager understands the operation of his or her organization when it is modeled during the assessment.

Table 1
Overview of assessment methods
Name (Reference) Requirements

<table><tr><td rowspan="2">Name (Reference)</td><td colspan="8">Requirements</td><td rowspan="2">Brief description</td></tr><tr><td>Focus on EDI</td><td>Quantitative</td><td>Traceable results</td><td>Recognizable results</td><td>Quick scan</td><td>in depth</td><td>Category A</td><td>Category B</td></tr><tr><td>Value analysis [12]</td><td></td><td>●</td><td></td><td></td><td>●</td><td></td><td></td><td></td><td>A two-staged method: (1) assess expected benefits and a cost threshold for a small-scale system; (2) assess expected costs and a benefit threshold for full system</td></tr><tr><td>Financial analysis [9]</td><td></td><td>●</td><td></td><td></td><td>●</td><td></td><td></td><td></td><td>Discussion of following financial analysis techniques: (1) payback period; (2) average return on investment; (3) net present value; and (4) internal rate of return</td></tr><tr><td>Multiple criteria [2]</td><td></td><td></td><td></td><td></td><td>●</td><td></td><td></td><td></td><td>A multiple criteria approach to assess the importance of IS investment alternatives to the focal organization</td></tr><tr><td>Cost/benefit analysis [13]</td><td></td><td>●</td><td></td><td></td><td>●</td><td></td><td></td><td></td><td>Introduction of a plan of approach to apply net present value for IS justification</td></tr><tr><td>Decision analysis [20]</td><td></td><td>●</td><td></td><td></td><td>●</td><td></td><td></td><td></td><td>The development of decision trees to assess expected payoffs under risk of IS investments</td></tr><tr><td>Information economics [16]</td><td></td><td>●</td><td>●</td><td>●</td><td></td><td>●</td><td>●</td><td>●</td><td>Combination of a quantitative assessment of IT-enabled business process improvement with a multiple criteria approach to assess expected strategic effects</td></tr><tr><td>Option theory [7]</td><td></td><td>●</td><td></td><td></td><td>●</td><td></td><td></td><td></td><td>Argumentation to include within the assessment the possible benefits of future IT investment projects based on the focal IT investment project</td></tr><tr><td>Simulation [25]</td><td></td><td>●</td><td>●</td><td>●</td><td></td><td>●</td><td>●</td><td>●</td><td>Simulation to assess the impact of IT on the ordering policies within a three-staged supply chain (factory-distributor-retailer).</td></tr><tr><td>Inventory holding cost model [1]</td><td>●</td><td>●</td><td>●</td><td></td><td>●</td><td></td><td></td><td>●</td><td>Inventory holding cost models to assess the impact of EDI on inventory costs</td></tr><tr><td>LANE approach [22]</td><td>●</td><td>●</td><td>●</td><td>●</td><td></td><td>●</td><td></td><td>●</td><td>Simulation to assess the impact of EDI on the physical processes within logistical chains</td></tr><tr><td>Edialysis [10]</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td></td><td>●</td><td></td><td>An Activity-Based Costing (ABC) approach to assess the impact of EDI on the information processes of a single organization</td></tr><tr><td>Stakeholder analysis [11]</td><td></td><td>●</td><td>●</td><td>●</td><td>●</td><td></td><td></td><td></td><td>Argumentation for recovery mechanisms for those stakeholders of IT implementation projects which will benefit less than other stakeholders</td></tr><tr><td>Interdependent benefits [17]</td><td>●</td><td>●</td><td>●</td><td>●</td><td></td><td>●</td><td>●</td><td></td><td>Focus on the interdependent benefits of EDI within a buyer-supplier relationship</td></tr><tr><td>Simulation [14]</td><td>●</td><td>●</td><td>●</td><td>●</td><td></td><td>●</td><td></td><td>●</td><td>Simulation to assess the impact of EDI on inventory holding costs within a three-staged supply chain</td></tr></table>

\- The application should be conducted as efficiently and effectively as possible in order to minimize the costs. It should approach the speed and ease of use of a quick scan. On the other hand, the method should, where necessary, be based on an in-depth analysis of current information and physical processes within an organization in order to be able to assess the expected impact of EDI investment.

## 3. Available methods

Table 1 provides an overview of the available methods. It appears that no single method meets all the requirements. Only a handful of methods focus explicitly on EDI investment. Several do not focus on the type of benefit to be expected from an IS investment, but rather on the process of evaluating the expected impact of the IS investment. Only two methods focus on both category A and category B benefits. However, because these methods focus on IT investments in general, they have to be adapted before they can be applied properly to EDI-type investments.

Since no single method meets all the requirements we advise the integration of two methods into a new approach: this is called CAVALIER (Comprehensive Approach for the Value AnaLysIs of EDI-Investments). Its latest version is Release 2. The two methods which we input to this integration are the Edialysis system developed by Hoogeweegen and Wagenaar [10] and the simulation-based method developed by Streng [22]. This latter method, contrary to the typical simulation methods, uses high-level building blocks to accelerate application time and animation that can create traceable and recognizable results.

## 4. CAVALIER: A comprehensive method for value assessment of EDI

CAVALIER focuses on the benefits to be expected in a single organization. However, it considers the position of the organization within its business network in order to allow analyses of inter-organizational business process redesign, or business network redesign, effects [23].

![](/api/attachments/79XT75QG/fulltext/images/9009d8aa9dcd02d2d6243a10bb6b8937ca376b0ce67a18e2d8585f15606c4bfc.jpg)  
Fig. 2. Basic idea of CAVALIER.

CAVALIER uses the principle of comparison (see Fig. 2). Benefits of future EDI-based scenarios can be assessed only when they are compared with another scenario, like the current situation. Benefits accrue because of the displacement of costs. These should be compared with the costs of effectuating a particular scenario (e.g. investments in hardware and software).

The use of CAVALIER should be inexpensive and lead to a rapid conclusion. This is possible when spreadsheet-based modeling is the default technique. Obviously, simulation modeling is needed when the real-world complexity and dynamics are so high that a spreadsheet is not adequate. Furthermore, CAVALIER should be easy to use. A user-friendly interface has to be built on top of the spreadsheet system, while the simulation environment must involve standard high-level building blocks that can be used to give an animated view in addition to the numbers provided by the spreadsheet system and the simulation model.

The basic idea is translated into an activity plan that is illustrated in Fig. 3. The use of CAVALIER starts with problem definition. This can be as broad as: 'Analyze what EDI can do for my business,' but, in the typical case, the problem definition narrows the scope of the study. For example, when a partner proposes a particular EDI investment, the problem to solve may be: 'What does it mean for my business when I make the proposed EDI-investment?' Another question can be 'Can I save parking space when I use EDI?' or 'Can my order handling department deal with $10\%$ business growth with the same amount of staff members when I use EDI?' The user of CAVA-

![](/api/attachments/79XT75QG/fulltext/images/4b854ed2566304f615d8f46c43dfe090103cba25cd14098deff687d02cc37baf.jpg)  
Fig. 3. The steps in CAVALIER.

LIER should be aware, at this point, that he or she has to balance between two extremes: solving the world's problem (focus too broad) or throwing away all flexibility by making the problem definition too narrow.

Phases 2 to 4 of CAVALIER involve the assessment of the current situation. This is very important, because it supports the formulation of EDI-based scenarios and establishes the point of reference that is used to assess benefits of EDI-based scenarios. In phase 2, a conceptual model is developed. Business partners are defined as well as the business and information processes. The question is: 'How does my organization fit in the world' while applying Baron von Munchhausen's approach $^{3}$ on physical and information items that enter and leave the organization. The standard building blocks developed for CAVALIER can be used to develop a conceptual model where all parameters are defined. In phase 3, data are collected.

Detailed parameters need to be specified or estimated when they are not available. $^{4}$ In phase 4, the data and the conceptual model are combined to provide a model of the current situation for analysis.

Based on the results of the analysis, the definition of EDI scenarios takes place in the fifth phase. However, it may be possible to derive more than one EDI scenario and thus creativity plays a major role. In our experience, the best and most successful EDI scenarios required some ‘out of the box’ (or non-traditional) thinking. CAVALIER provides reports of the current situation to aid in this phase. Furthermore, an animated simulation model is provided to clarify the solution.

The sixth phase is concerned with the analysis of the future, that is, simulated implementation of the EDI scenario – by using the model of the current situation as a substitute. After results have been analyzed, the implementation of the scenario may start, or a new scenario can be defined; this, in turn, leads to an iteration of phases 5 and 6.

## 5. CAVALIER in practice

Our example deals with a business network that produces and distributes mineral and vegetable oils from a production plant in the northern part of the Netherlands for the Western European market. AVL $^{5}$ produces annually about 20,000 tank loads of oil with their products; 15,000 of them are transported directly by truck from the production plant to the customer. About 5000 tank loads are transported overseas to Great Britain and Ireland, in which case tank containers are first sent by truck from the production plant to the port of Rotterdam, after which the container is transported by ship.

## 5.1. Phase 1: Define the problem

The costs of order handling and transport take up a substantial part of the overall price of the product and international competition has forced the business management of AVL Inc., and particularly that of its transportation subsidiary AVL/Logistics, to look for ways to decrease costs. One of the techniques being considered is EDI. It may be used for two reasons: (1) to reduce the costs of the information process (or, as an executive said: “Sometimes we have the feeling that every tanker with oil is followed by a tanker of paperwork”), and (2) to help in reducing waiting times, costs, and irritation that currently occur at the tanker filling facility.

## 5.2. Phase 2: Conceptual modeling

In one session with AVL, the scope of the EDI study was determined. In Fig. 4, this is depicted in terms of business partners. AVL/Logistics is at the center of this picture. It communicates with AVL (the mother company that receives the customer orders, that produce the oils, and that keeps the customer informed); Holland Tanker Transport (takes care of inland transportation); Customs (which checks the cargo when it is transported outside the European Community); Worldwide Shipping Lines (performs the transport overseas), Rotterdam Container Terminals (takes care of the loading and unloading of tanker containers in the case of overseas transport); and Delta Container Rentals (provides the tank containers).

![](/api/attachments/79XT75QG/fulltext/images/9922cc7dbbd12e1061eb80b89af3f90a68ea79d52e492384ab99b3fcf2973de6.jpg)  
Fig. 4. AVL/Logistics and its partners.

<table><tr><td rowspan="7">AVL/Logistics</td><td>Container overseas transport order</td><td>→</td></tr><tr><td>Container call down order</td><td>→</td></tr><tr><td>Overseas transport confirmation</td><td>→</td></tr><tr><td>Container call down confirmation</td><td>→</td></tr><tr><td>Shipping instruction</td><td>→</td></tr><tr><td>Empty container disposition order</td><td>→</td></tr><tr><td>Container pickup confirmation</td><td>→</td></tr></table>

Fig. 5. Information flows between AVL and Worldwide Shipping Lines.

In CAVALIER, all flows between AVL/Logistics and the business partners were explicitly named; this includes information flows, as well as physical flows that are controlled by them. Fig. 5 gives an example of the flows that exist between AVL/Logistics and Worldwide Shipping Lines.

In addition, the dynamic process at the filling facility has to be investigated and modeled. This is done using the simulation component of CAVALIER. Fig. 6 gives a screen print out of the simulation model, where trucks arrive at AVL, wait until one of the two filling facilities is available, wait until this filling facility is cleaned, and the trucks are then filled with oil. The model was built by using the high-level building blocks provided in CAVALIER.

## 5.3. Phase 3: Data collection

For each of the flows that has been defined, detailed information has to be gathered about the frequency of information exchange and the costs of each message. Examples are: the amount of time and thus expense of an employee handling the incoming message, the total volume of messages and the costs associated with the message (such as telephone, paper and copies). Figs. 7 and 8 give an impression of the kind of information that is required and the way this information is entered in CAVALIER. Fig. 7 shows the number of ‘Overseas Transport Confirmation Messages’ that is sent every year, and the means of communication that is used for the message (in this example: 20% by phone, 70% by fax and 10% by courier). In Fig. 8, a number of input parameters are entered; all of them deal with a single activity: handling incoming overseas transport confirmation messages arriving by fax at AVL/Logistics.

![](/api/attachments/79XT75QG/fulltext/images/bb3302d3b03d9e6b66e71e1ce80c3c5bce72d247280b60c8d38f4d3255b54317.jpg)  
Fig. 6. Screen print of the simulation model.

![](/api/attachments/79XT75QG/fulltext/images/4f31ad9d6e7d3d426fd1276110486e547e1fc22172d2d30c82a500ef1553db7a.jpg)  
Fig. 7. Frequencies per means of communication.

In this example the user has stated that every fax requires 2 min of labor time at a rate of 75 cents per minute. This kind of (estimated) information has to be filled in for every activity and for every means of communication.

![](/api/attachments/79XT75QG/fulltext/images/be9ebf3f80adc82c669a617876be4e875a1bda734afc40d81ae39b53f61a8d50.jpg)  
Fig. 8. Costs per message-type.

## 5.4. Phase 4: Analysis of the current situation

The conceptual model and the collected data are combined in a comprehensive model of the current situation. The following reports are provided:

\- report of the cost per message-type, with separate columns for labor, material and communication;

\- report of the total number of messages per message-type;

\- report of the handling time, transport time, and wait time of elements in the information flow (fax messages, letters);

\- report of the handling time, transport time and wait time of elements in the physical flows (containers, trucks).

In our example, the following conclusions could be drawn:

\- the costs for information processing are very high: for every tanker, information processing costs are about NLG. 104, –;

\- the average filling time for trucks is 9 min. As the facility is cleaned after each filling, the truck occupies the facility for about 22 min. The total handling time (including waiting time) for each truck is about 57 min.

## 5.5. Phase 5: Define the scenario

Here, we give an example scenario which includes the exchange of EDI messages with Worldwide Shipping Lines, Rotterdam Container Terminals, and Customs. This information exchange takes place using faxes, phone calls, forms, and letters. In addition, an EDI connection is assumed to be established between AVL and Holland Tanker Transport, which will send an EDI message every time a truck is heading for AVL. Such a pre-arrival notice does not replace existing information flow; it is new. At AVL, a computer receives the pre-arrival notice, and schedules the loading of the truck in such a way that the number of cleaning operations is minimized.

This scenario could be implemented by using the model of the current situation as an alternative. This requires changing parameter values in CAVALIER. In addition, two new model elements have to be entered. The first concerns the investment costs that are associated with implementing the scenario; this requires an estimate of the hardware, software, project and mobilization costs. The second element concerns the new process that takes place at the loading facility; the new information flow must be defined and a specification made of how incoming EDI messages are handled.

In general, the definition of an EDI scenario requires a mixture of business knowledge, technical knowledge, and creativity. In our experience, an animated model provides a good foundation on which to bring up ideas and discuss them in a JSD $^{6}$ session.

![](/api/attachments/79XT75QG/fulltext/images/435adde3a28eb89ee2c69dd1797564955158f60af94b09a13a7fd557d4aeca75.jpg)  
Fig. 9. Handling times of individual trucks (old and new situation).

## 5.6. Phase 6: Analysis of the scenario

CAVALIER provides tools to simulate and calculate the value of the proposed scenario. For the costs and benefits that can be expressed directly in money, it reports the Return on Investment (ROI) and Net Present Value (NPV) of the proposed EDI investment. For the costs and benefits that cannot be expressed directly in terms of money, it guides the user through several steps that help the designers to estimate the money value of certain improvements.

Fig. 9 for example, provides the handling times of trucks at the filling facility in the old situation (the narrow line) and the new situation (the thick one). Note that the handling time is reduced significantly (although a few trucks will have to wait longer). On average, handling time is reduced from 57 min to about 30 min. The designer is then asked to enter the value of this time reduction. In this case, the AVL management has asked (as part of the annual negotiations) the Holland Tanker Transport management how much they would reduce the transport price if such a reduction in handling time were accomplished. This leads to a estimation of the benefits that can be used by CAVA-LIER to calculate a new ROI or NPV. Fig. 10 gives the NPV for our example scenario for the next 5 years.

## 5.7. Phase 7: Implement scenario

Phases 5 and 6 will be iterated several times, until desirable and financially satisfactory results are achieved. The step towards implementation follows; this is far from easy, but, in our experience a clear definition of the scenario, its outcomes, and the animation that is provided aids in the decision to start the implementation project, especially when it comes to convincing business partners to use EDI. In their turn, these business partners can apply CAVALIER in their own organization. Thus a CAVALIER model can be developed that comprises the whole organizational network and that clearly calculates and demonstrates the costs and benefits of EDI, not only for each organization, but also the network as a whole.

![](/api/attachments/79XT75QG/fulltext/images/1b22f055c0a2d768a39e9d7c3031a4e38557f3195f825c099672fb1eb93019b1.jpg)  
Fig. 10. The NPV for the example scenario.

## 6. Conclusion

A new method, CAVALIER, has been proposed. It allows the user to assess ex ante both reduced data handling costs, process lead time reductions and improved physical resource utilization as a result of EDI-enabled process redesign in inter-organizational settings. The method is basically an integration of two distinct, separately developed methods, one based on Activity-Based Costing, the other on discrete event simulation with animation. Although it is not an ironclad rule that the integration of two methods leads to an overall method that fills the blank spots of each of the underlying methods, it is our strong opinion that CAVALIER does fulfill these requirements. Parts of CAVALIER have been applied within companies in the Port community of Rotterdam and have played a significant role in the decision to invest in EDI technology there.

In our research, we try to apply the CAVALIER method in business areas that are not seen as ‘traditional logistics-oriented’ but have nonetheless much in common with logistics. Examples are insurance companies and the Dutch tax offices. In these areas, EDI can speed up the handling of insurance claims and tax return forms, and it is our hypothesis that CAVALIER can be applied in basically the same way there as it is applied in ‘traditional’ logistic organizations.

## References

[1] M. Anvari, Electronic data interchange and inventories, International Journal of Production Economics 26(1–3), 1992.

[2] E.F. Bedell, The Computer Solution: Strategies for Success in the Information Age, Homewood, Dow-Jones Irwin, 1985.

[3] R.I. Benjamin, D.W. de Long, M.S. Scott Morton, Electronic Data Interchange: How much competitive advantage? Long Range Planning 23(1), 1990.

[4] F. Bergeron, L. Raymond, Managing EDI for corporate advantage: A longitudinal study, Information and Management 31, 1997, pp. 319–333.

[5] L. Bouchard, Decision criteria in the adoption of EDI, in: J. deGross, R. Bostrom, D. Robey (Eds.), Proceedings of the 14th International Conference on Information Systems, Orlando, FL, USA, 1993.

[6] B. Dearing, The strategic benefits of EDI, Journal of Business Strategy 11(1), 1990.

[7] B.L. Dos Santos, Justifying investments in new information technologies, Journal of Management Information Systems 7(4), 1991.

[8] B. Farbey, F. Land, D. Targett, A taxonomy of evaluation methods, First European Conference on IT Investment Evaluation, Henley Management College, London, UK, September 1994.

[9] T. Guimaraes, W.E. Paxton, Impact of financial analysis methods on project selection, Journal of Systems Management, February 1984.

[10] M.R. Hoogeweegen, R.W. Wagenaar, A method to assess expected net benefits of EDI investments, International Journal of Electronic Commerce 1(1), 1996, pp. 73–94.

[11] J. Jurison, Measurement and evaluation of IT benefits, a stakeholder-based approach, First European Conference on IT Investment Evaluation, Henley Management College, London, UK, September 1994.

[12] P.G.W. Keen, Value analysis: Justifying decision support systems, MIS Quarterly 5(1), 1981.

[13] P.M.Q. Lay, Beware for the cost-benefit model for I.S. project evaluations, Journal of Systems Management 36(1), 1985.

[14] N.A. Mylonopoulos, G.I. Doulidis, Assessing the expected benefits of Electronic Data Interchange through simulation modelling techniques, Proceedings of the 3rd European Conference on Information Systems, Athens, Greece, 1995.

[15] B.S. Neo, P.E. Khoo, S. Ang, The adoption of TradeNet by the trading community: An empirical analysis, in: J.I. deGross, S.L. Huff, M.C. Munro (Eds.), Proceedings of the 15th International Conference on Information Systems, Montreal, Canada.

[16] M.M. Parker, R.J. Trainor, H.E. Benson, Information economics: Linking business performance to information technology, Prentice-Hall, 1988.

[17] F.J. Riggins, T. Mukhopadhyay, Interdependent benefits from interorganizational systems: Opportunities for business partner reengineering, Journal of Management Information Systems, Fall, 1994.

[18] J.B. Rochester, The strategic value of EDI, IS/Analyzer 27(8), 1989.

[19] S. Scala, R. McGrath, Advantages and disadvantages of electronic data interchange, Information and Management 25, 1993, pp. 85–91.

[20] G.P. Schell, Establishing the value of information systems, Interfaces 16(3), 1986.

[21] H.S. Sheombar, R.W. Wagenaar, The impact of EDI on logistical organization: Towards a method for business redesign, In: J. Gricar (Ed.), Proceedings of the Fourth annual EDI conference, Bled, Yugoslavia, 1991.

[22] R.J. Streng, Dynamic modelling to assess the value of electronic data interchange: A study in the Rotterdam port community, Dissertation, Delft University of Technology, 1993.

[23] N. Venkatraman, IT-enabled business reconfiguration, in: M.S. Scott Morton (Ed.), The Corporation of the 1990s: Information Technology and Organizational Transformation, Oxford University Press, 1991.

[24] J. Webster, Networks of collaboration or conflict? Electronic data interchange and power in the supply chain, Journal of Strategic Information Systems 4(1), 1995.

[25] J. Wikner, D.R. Towill, M.M. Naim, Smoothing supply chain dynamics, International Journal of Production Economics, 22(3), 1991.

![](/api/attachments/79XT75QG/fulltext/images/4c2ad1be600f65b4cb8a2ec9fb7c2caa5e41af413318edb59b23cba199ac7604.jpg)

Martijn Hoogeweegen received his Ph.D. in General Management from Erasmus University, Rotterdam. The title of his thesis is: Modular Network Design: Assessing the impact of EDI. He recently joined Multimedia Skills, an international consultancy group specializing in project and change management, technical and business skills in telecommunications and multimedia. He has written several articles and confer-

ence papers on EDI and inter-organizational process redesign.

![](/api/attachments/79XT75QG/fulltext/images/0eb0d67db1b76a625a9f31bb85d0fe7201dc0818f1efb5d8cb2d370af88c2998.jpg)

Robert-Jan Streng received his Ph.D. in MIS from Delft University of Technology. The title of his thesis is: Dynamic Modeling to Assess the Value of Electronic Data Interchange. He is currently managing consultant at Origin Consulting in the Netherlands. He has written several articles on EDI, telecommunications and process innovation. He is co-author of the books Scientific Research on EDI and Tools for Business Process Redesign.

![](/api/attachments/79XT75QG/fulltext/images/ef2c9dc0e3d4e1ce61355d749a806b532205fdf639728bc9f84cd941458b2f43.jpg)

René Wagenaar works as strategy consultant at KPN Research, the R&D group of the Royal PTT Netherlands (KPN). He also holds the part-time chair on the Economics of Tele-informatics at the Faculty of Economics of the Free University, Amsterdam. Before he joined KPN, he worked as associate professor at the Faculty of Business Administration of the Erasmus University, Rotterdam.

He started his career in 1984 at the Data and Telecommunications Systems division of Philips Netherlands NV. He holds a Ph.D. in physics and a bachelor's degree in economics. Prof. Wagenaar's current activities concern KPN's strategy and business planning for Electronic Commerce services. He has written numerous articles and conference papers in this field and is a frequent speaker in seminars and conferences on issues concerning Ecommerce. He is member of the programme Council of the Telematics Top Institute in the Netherlands and consultative expert of the G7 Initiative in Electronic Commerce for SMEs.
