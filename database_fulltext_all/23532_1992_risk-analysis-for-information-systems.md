---
otero_id: 23532
otero_key: "YWVFKKXV"
title: "Risk analysis for Information Systems"
authors: "David G W Birch; Neil A McEvoy"
year: "1992"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1992.7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
MANAGEMENT REPORT

# Risk analysis for Information Systems

DAVID G.W. BIRCH and NEIL A. McEVOY

Hyperion Systems Limited, Surrey, UK

This paper presents an integrated approach to risk analysis for Information Systems (IS) using the Structured Risk Analysis (SRA) methodology developed at Hyperion. SRA has been used, very successfully, to perform risk analysis both for security-oriented risk analysis in the City and safety-oriented risk analysis for the European Space Agency. This paper develops and describes a particular instance of the SRA methodology for IS. Excluding safety-critical applications allows certain simplifications to the methodology in the case of IS. These simplifications make structured risk analysis for information systems (SRA-IS) a practical and cost-effective basis for risk analysis and risk management in commercial organizations.

## Introduction

In the particular case of Information Systems (IS), there has been a reluctance to tackle the subject of risk – due to perceived complexity and inexactness – and therefore handle risk analysis and risk management effectively. This has led to a situation where many IS do not retain the simplest risk management techniques which were present in the paper systems that they are replacing (Dunn, 1990). Clearly, with the growing importance of IS in all aspects of corporate operation, IS must be made subject to appropriate risk analysis and risk management disciplines.

The purpose of risk analysis should be to assist managers in making informed decisions about investments and developing risk management policies. In the case of computers and communications, the countermeasures that can be employed to reduce risk are well-known and an array of techniques are available (Seburry and Pieprzyk, 1989). High countermeasures expenditure on every aspect of an IS is out of the question in a commercial organization. Therefore, this expenditure must be directed to reduce corporate exposure to IS risks in the context of overall business risks. In particular, risk analysis must be able to answer the following questions:

(1) how much is it appropriate to spend on countermeasures?

(2) where should spending be directed?

There are many insecure systems in operation which may cost businesses millions of pounds (or have equally deleterious effects on non-business organizations) if the insecurities are exploited. There are also many systems with inappropriate and over-expensive security countermeasures, which are just as responsible for losing money. By way of illustration, suppose a risk loses a business £10 000 per year. It is clearly inappropriate to spend £200 000 to close this risk, since the same investment would yield more than enough to cover the losses if placed in a bank.

Historically, the security side of IS has been driven by the development of countermeasures. The types of countermeasure and their use in different situations is a subject which has been well-developed (Landwehr, 1986) and is not relevant to this paper.

Investment decisions are complicated – it is important that an organization has the best possible information on risks in order to decide whether or not to invest (scarce) resources in countermeasures, and if so, how much. It should be remembered that risk is an inescapable part of being in business. IS risks are no different in this respect than any other business risk and may well be less in magnitude. In all cases, it is essential that risks are adequately managed and for this purpose, risks must be quantified.

## Business risks

## Context

Being in business is a risk. However strategic an IS may be to a business, the threats to that IS – whether fire, flood or hackers – are only part of the spectrum of threats that surround the business.

For most commercial organizations, the value of the information associated with an IS greatly exceeds the value of the technology associated with the IS (unless the

IT strategy of the organization is inappropriate). It can be the case that whereas the value of the technology assets is known to seven significant figures (because they appear on balance sheets), the value of the information assets is not known to the nearest order of magnitude. Proper business investment decisions cannot be made in such an environment.

The object of risk management is to reduce business exposure by balancing countermeasures investment against risk. It may be that the countermeasures expenditure would be better directed to other parts of the organization. If this is the case, then risk management should confirm it. It is important to remember that the purpose of risk analysis and risk management procedures is not simply the definition of countermeasures.

Risk analysis and risk management must be part of the ongoing operations of an organization but within that organization should be no more or less important than any of the other disciplines associated with IS.

## Risk analysis requirements

A great deal of work has already been undertaken in the general field of risk analysis and methodologies such as CRAMM (Moses, 1990) have been developed. In reviewing these existing methodologies and techniques, a number of problems were uncovered which made them unsuitable for current business needs. One of the major problems was that much of the work on the subject was rooted in the technology of the 1970s, assuming a large central 'hub' accessed through terminals, and did not assist in the analysis of decentralized and workstation/server IS (Davies, 1990).

While many methodologies have recognized that risk analysis is now fundamental to the development and operation of IS (Reed and Watt, 1989), none had been able to deliver the prescriptive and specific information that managers require to make real business decisions. The approach to the risk analysis itself had largely been based on the use of checklists for managers to try to think of all possible risks and take appropriate action. It is possible to make very long lists that are reasonably comprehensive for a particular type of system (Jamieson and Low, 1990), but this approach does not give any confidence that all risks have been identified. Hence the need for an approach that is complete, consistent and correct.

The primary requirements for a risk analysis methodology were therefore determined to be that the methodology should:

(1) integrate fully with the structured methodologies that have been developed for IS analysis and for which CASE tool support exists

(2) not require specialized software or complicated training

(3) be sufficiently flexible to cope with all IS models: centralized, decentralized and distributed

(4) be both prescriptive and specific, so as to furnish manager with real decision-support information.

These requirements were the starting point for the development of SRA.

## Business analysis

## Structured analysis

One of the primary requirements for a cost-effective risk analysis methodology is that proper examination of IS risk should be founded on the same structured techniques as other IS analysis activities. Over the past few years, the use of structured analysis techniques to handle IS has become widespread and many methodologies are in use. Methodologies such as Structured System Analysis and Design Methodology (Nicholls, 1987) (SSADM) are in use in many organizations and are well supported by CASE tools, training courses and other materials. All of these methodologies share the use of structured models, easy to understand in diagram form, as the basis for collecting, verifying and disseminating information. They also share the same fundamental view of an IS, which separates the data structure, data processing and events in a system as shown in Figure 1. We are very much in favour of the use of such structured techniques for business analysis because:

(1) any policies developed will have a proper audit trail, allowing decisions to be traced and modified in the event of the structured models being updated (because of changes in the business or systems)

(2) standard structured analysis technique allow the use of off-the-shelf CASE tools and other support, making the analysis process more efficient

![](/api/attachments/YWVFKKXV/fulltext/images/fdebf94a6f995e12f53b10c649d783da8f9894412753e4feab28a6852ac8a9bd.jpg)  
Figure 1 Structured analysis concepts

(3) analysis techniques such as SSADM are widely used and therefore staff within the target organization will understand the model and be able to contribute to them

(4) they ensure the capture of all relevant information and therefore do not necessitate guesswork

There are a number of suitable structured techniques and whether ‘information modelling’, ‘enterprise modelling’ or ‘structured modelling’ is used, the benefits are the same. It is worth noting that a set of IBM case studies on the subject (Katz, 1990) showed that every single organization which adopted the technique found that it improved their business decision making.

Three structured analysis models are required to capture all of the information necessary to support risk analysis. These are the business model (often called the logical model or the service model), the information model (often called the logical data model or entity relationship model) and the technology model (often called the physical model or system model). The business model shows the organization and the services delivered to users, clients or whoever. The information model shows the corporate information entities and the relationship between them. The technology model shows the computer, communication and other systems used to support the provision of services.

## Business model

The business model shows the information flows in an organization, the sources and sinks of information and the information processing or retention centres. Business analysis begins by creating the Level-0 Business Model (L0BM) which treats the business (or the part of a business that is under examination) as a single information processing centre and identifies all of the sources/sinks of information. Analysis then proceeds to Level-1, which identifies major information processing centres (as shown in Figure 2).

The business model can be expanded to the necessary level of detail. We can assume in this case that one level of expansion is adequate, so the Level-1 Business Model (L1BM) is all that needs to be created. Note that once the business model is in place, a unique labelling scheme now exists for all information flows.

## Information model

The information model shows the elements of information (not data) in the business and the relationships between those elements. In essence, the elements of information are business entities and the relationships between them are business rules.

Figure 3 shows the Level-1 Information Model (L1IM) which corresponds to the business model in Figure 2. Each elements on the L1IM (i.e. each business entity) is an information asset. This L1IM is very small because of the highly simplified business model used in this example. In any case, in order to carry out high-level analysis to highlight the main areas of exposure, a high-level information model is sufficient to identify the primary corporate information assets. Once the information model exists, we have a unique labelling scheme for all information assets.

![](/api/attachments/YWVFKKXV/fulltext/images/73bc2c8101901b8efc03111430bf91734fd2f04110e341fba1080d0b8fbed6ba.jpg)  
Figure 2 Example business model

![](/api/attachments/YWVFKKXV/fulltext/images/389b4f63a84a1ee09dc47b4e377c6a3c3602d76bf8879ea6afc7ff91ea06cfeb.jpg)  
Figure 3 Example information model

## Technology model

The technology model shows the actual computer and communications systems that are in place in an organization, with no reference as to their actual purpose or use. This separation of concerns is fundamental to the structured business analysis procedures.

Each entity in the technology model is a physical asset of the IS. These physical assets may be hardware, software, communications links and so on. Given our assumption that the value of information assets greatly exceeds the value of the physical assets, it is not necessary to determine the value of these physical assets: in fact, we can assume that these physical assets are covered by insurance and so it is not necessary to include them in calculations.

Figure 4 shows the Level-1 Technology Model (L1TM) for our example which corresponds to the business model in Figure 2 and information model in Figure 3. Note that any one of a number of technology models could support any given business model, a property which becomes very useful when evaluating potential implementation of an IS that is still at the feasibility or specification stage.

## Construction

The construction of the business and technology models, using a structured methodology, can be achieved using any one of the myriad of Computer-Assisted Software Engineering (CASE) tools on the market. In many

![](/api/attachments/YWVFKKXV/fulltext/images/c599265459c0a130475dc7647de7f147b9b8e41b88e8ae651bb72eeaa492f221.jpg)  
Figure 4 Example technology model

There is a threat that a competitor might undercut us and take our business

organizations, these structured models should already exist anyway and are not put into place solely for the purpose of risk analysis.

## Risk analysis

## Concepts

Risk analysis is based on the principal concepts of threat, vulnerability, countermeasure, risk and attack. These basic concepts, as shown in Figure 5, exist in one form or another in all risk analysis techniques. It is the precision of their specification in SRA which makes the results of SRA prescriptive (and therefore of value to business).

A threat is something which will have an adverse effect on an organization. A threat exists whether or not there are any practical or apparent ways in which it might ever be manifested. The threats to an IS are independent from the physical implementation of the IS.

A vulnerability is a characteristic of a physical system which, while being independent from any specific threat, allows (in principle) a threat to be exploited. Vulnerabilities are a property of the physical implementation of the IS and are independent from any threats to the IS.

A risk is something which exists when a threat and a vulnerability overlap. That is, there is a threat to the business and a vulnerability which may be exploited to

There is a vulnerability that our customer records are copied and left in various offices

There is a risk that a competitor will see our customer and discount list and undercut us

![](/api/attachments/YWVFKKXV/fulltext/images/9285b053cbbdec7cd1ff8eba600c0cf9f3e7d6ffff526dcf97e84ed3eaa6a2ca.jpg)

There is an attack when a competitor tries to see the customer records to obtain the customer and discount list

There is a countermeasure that we lock away customer records when we're not using them

Figure 5 Structured risk analysis concepts realize this threat. An attempt to exploit a risk – that is, to realize a threat – is called an attack and the person, agency or organization attempting to exploit that risk is the attacker. Note that the same attack may be attempted by different attackers: in each case, this constitutes a separate risk. In the exposition of SRA–IS in this paper, we have made the simplification that there is only one attacker for each attack. This reduces the complexity of the analysis.

A countermeasure is something which reduces exposure, either by reducing the probability of attack (reducing vulnerability), the business losses associated with a threat (reducing impact) or the losses resulting from a successful attack (reducing exposure).

## Threat analysis

Threat analysis consists of cataloguing each and every threat to a business. In the case of IS, this means cataloguing the threats to the information assets on the information model. Given the structured approach, this is straightforward. Thus, for every information asset on the information model, three threats are catalogued: the integrity threat (TI), the confidentiality threat (TC) and the availability threat (TA). Each information flow is already uniquely labelled (because of the structured analysis) and so each individual threat is similarly labelled for cataloguing. So, information assets 3 (say) would have three entries in the threat catalogue: TI3, TC3 and TA3.

This approach may seem broad, but it works very well. There is no point in analysing the system down to the nth degree at the beginning. Instead, the broad analysis of Level-1 is used to identify ‘problem’ areas (i.e. areas of high exposure) of the system. Then, it is only necessary to analyse those particular areas down to Level-2 (and so on, as necessary, through the levels).

The next step is to assign impacts to the threats in the threat catalogue. In this simplified case, only one impact is assigned to each threat because we have made the assumption that there is only one attacker for each attack. It is not possible to define a generalized impact metric because the nature of business impact varies from business to business. In the case of commercial information systems, a money-based metric is obviously useful. To avoid the difficulty of working with large numbers, a logarithmic metric can be used. As an example, a suitable impact metric (based on the Federal Information Processing Standard metrics (1990) might be as shown in Table 1.

Assigning an impact to each of the threats determined from the information flows on the information model leads to the creation of the threat catalogue. A section from an example threat catalogue is shown in Table 2. This shows an excerpt from the threat catalogue for the example system.

Table 1 Example impact metric

<table><tr><td>Maximum potential loss</td><td>Assigned impact metric</td></tr><tr><td>£0</td><td>0</td></tr><tr><td>£10</td><td>1</td></tr><tr><td>£100</td><td>2</td></tr><tr><td>£1000</td><td>3</td></tr><tr><td>£10 000</td><td>4</td></tr><tr><td>£100 000</td><td>5</td></tr><tr><td>£1 000 000</td><td>6</td></tr><tr><td>etc.</td><td>etc.</td></tr></table>

## Vulnerability analysis

As in the case of threat analysis, vulnerability analysis proceeds by cataloguing all vulnerabilities of a system (this time using the technology model) and then assigning a probability of the vulnerability being exploited in a given time. The number and diversity of vulnerabilities that need to be covered is the factor which causes the most problems. To assist in dealing with vulnerabilities, it is worth developing a broad classification of vulnerabilities. The use of some recent examples will illustrate these basic categories:

(1) the recent theft of automobile blueprints from BAe through unauthorized access to a satellite communications link is an example of the malicious exploitation of an IT vulnerability of an IS—this is a Class A vulnerability (malacious, IT)

(2) the collapse of the AT&T long distance telephone network because of a software fault is an example of the non-malicious attack on an IT vulnerability (the telephone switch software) of an IS—this is a Class B vulnerability (non-malicious, IT)

(3) the disruption of the ICAO AFTN network (a worldwide message switching network used by airlines) because of the failure of the Kuwait switching centre following the recent trouble in the area is an example of malicious attack on a non-IT vulnerability of an IS—this is a Class C vulnerability (Malicious, non-IT)

(4) the recent failure of our office file server because someone spilt coffee in the power supply is an example of a non-malicious attack on a non-IT vulnerability of an IS—this is a Class D vulnerability (non-malicious, non-IT).

The vulnerabilities are catalogued against the physical assets in the technology model. Again, each vulnerability must be uniquely labelled for cataloguing. Each data flow on the technology model is already uniquely labelled, so each of the four vulnerabilities will be similarly labelled. Data flow 2.2 of the technology model has the vulnerabilities VA2.2, VB2.2, VC2.2 and VD2.2 associated with it.

Next, a probability of occurrence must be assigned to each vulnerability. As in the case of threat impacts, we will in this case use a general purpose logarithmic occurrence metric as shown in Table 3. This metric shown is sufficient for a wide spectrum of commercial systems.

Table 2 Excerpt from threat catalogue

<table><tr><td>Item</td><td>Name</td><td>Threat</td><td>Description</td><td>Impact</td></tr><tr><td rowspan="3">1</td><td>Customer</td><td>|1</td><td>Customer lost/corrupt</td><td>3</td></tr><tr><td>Customer</td><td>C1</td><td>Customer disclosed</td><td>2</td></tr><tr><td>Customer</td><td>A1</td><td>Customer not available</td><td>2</td></tr><tr><td rowspan="3">2</td><td>Supplier</td><td>|2</td><td>Supplier lost/corrupt</td><td>2</td></tr><tr><td>Supplier</td><td>C2</td><td>Supplier disclosed</td><td>2</td></tr><tr><td>Supplier</td><td>A2</td><td>Supplier not available</td><td>2</td></tr><tr><td rowspan="3">3</td><td>Sales order</td><td>|3</td><td>Sales order lost/corrupt</td><td>2</td></tr><tr><td>Sales order</td><td>C3</td><td>Sales order disclosed</td><td>2</td></tr><tr><td>Sales order</td><td>A3</td><td>Sales order not available</td><td>2</td></tr><tr><td rowspan="3">4</td><td>Purchase order</td><td>|4</td><td>Purchase order lost/corrupt</td><td>3</td></tr><tr><td>Purchase order</td><td>C4</td><td>Purchase order disclosed</td><td>1</td></tr><tr><td>Purchase order</td><td>A4</td><td>Purchase order not available</td><td>2</td></tr><tr><td rowspan="3">5</td><td>Customer delivery</td><td>|5</td><td>Customer delivery lost/corrupt</td><td>3</td></tr><tr><td>Customer delivery</td><td>C5</td><td>Customer delivery disclosed</td><td>2</td></tr><tr><td>Customer delivery</td><td>A5</td><td>Customer delivery not available</td><td>2</td></tr><tr><td rowspan="3">6</td><td>Supplier delivery</td><td>|6</td><td>Supplier delivery lost/corrupt</td><td>4</td></tr><tr><td>Supplier delivery</td><td>C6</td><td>Supplier delivery disclosed</td><td>2</td></tr><tr><td>Supplier delivery</td><td>A6</td><td>Supplier delivery not available</td><td>3</td></tr><tr><td rowspan="3">7</td><td>Stock</td><td>|7</td><td>Stock lost/corrupt</td><td>4</td></tr><tr><td>Stock</td><td>C7</td><td>Stock disclosed</td><td>2</td></tr><tr><td>Stock</td><td>A7</td><td>Stock not available</td><td>2</td></tr></table>

Table 3 Example frequency metric

<table><tr><td>Likely frequency of exploitation</td><td>Assigned frequency metric</td></tr><tr><td>More than daily</td><td>3</td></tr><tr><td>More than weekly</td><td>2</td></tr><tr><td>More than monthly</td><td>1</td></tr><tr><td>More than yearly</td><td>0</td></tr><tr><td>Every decade</td><td>-1</td></tr><tr><td>Every 100 years</td><td>-2</td></tr><tr><td>Less frequently</td><td>-3</td></tr></table>

The frequency of occurrence of the exploitation of any particular vulnerability is actually a very complex function. This function depends on such elements as the gain to the attackers, the cost of the attack, the chance of detection and so forth. More complex models can, and have, been developed (Harris and McEvoy, 1990) and may be used where more detailed or specialized analysis is required. In our simplified case, the assumption that there is only one attacker means that we need assign only one frequency of occurrence value to each vulnerability.

Although there may be a great many physical assets (depending on the level to which the technology model has been developed, of course) it is usually straightforward to assign the vulnerabilities and probabilities because they are generic – it takes the same effort to tap a PSTN connection whether the PSTN line is being used for credit card verification or playing games over a network.

The catalogue of vulnerabilities derived from the technology model, together with the assigned frequency of occurrence metric, forms the vulnerability catalogue. An excerpt from an example vulnerability catalogue is shown in Table 4.

## Risk catalogue

Now that threats and vulnerabilities have been catalogued, a risk becomes something very precise and specific. In the general case, a risk can be said to exist where there is a correspondence between a threat and a vulnerability which share an attacker.

In our simplified case, a risk exists where there is a threat and a vulnerability that coincide. In order to find risks, each threat in the threat catalogue is examined and matched against the vulnerability catalogue. The best way to do this is in two stages. First, a cross-reference between the business model and the technology model is created (this may already be present in system architecture documentation). Then a further cross-reference between the information model and the business model is created. Thus, we can match threats and vulnerabilities in the following way:

(1) for each threat, select the underlying information asset

(2) cross reference the information asset to the business model to determine which information flows involve that asset

(3) cross reference the information flows from the business model to physical assets in the technology model

(4) for each physical asset, select the associated vulnerabilities.

If no vulnerabilities corresponding to the threat are found, then there is no risk. Where one or more vulnerabilities are found, the risks must be (as always) uniquely labelled. For example, if threat TI7 can be exploited through two vulnerabilities, say VA2.2 and VA2.4, then two risks must be entered in to the catalogue: RI7-A2.2 and RI7-A2.4.

Table 4 Excerpt from vulnerability catalogue

<table><tr><td>Item</td><td>Name</td><td>Vulnerability</td><td>Description</td><td>Frequency</td></tr><tr><td>1</td><td>Despatch PC</td><td>A1</td><td>Despatch PC unauthorized access</td><td>-1</td></tr><tr><td>1</td><td>Despatch PC</td><td>B1</td><td>Despatch PC equipment/sware failure</td><td>-1</td></tr><tr><td>1</td><td>Despatch PC</td><td>C1</td><td>Despatch PC vandalized/destroyed</td><td>0</td></tr><tr><td>1</td><td>Despatch PC</td><td>D1</td><td>Despatch PC fire/flood/strike/power</td><td>0</td></tr><tr><td>2</td><td>Goods in PC</td><td>A2</td><td>Goods in PC unauthorized access</td><td>-1</td></tr><tr><td>2</td><td>Goods in PC</td><td>B2</td><td>Goods in PC equipment/sware failure</td><td>-1</td></tr><tr><td>2</td><td>Goods in PC</td><td>C2</td><td>Goods in PC vandalized/destroyed</td><td>0</td></tr><tr><td>2</td><td>Goods in PC</td><td>D2</td><td>Goods in PC fire/flood/strike/power</td><td>0</td></tr><tr><td>3</td><td>Factory VAX</td><td>A3</td><td>Factory VAX unauthorized access</td><td>-1</td></tr><tr><td>3</td><td>Factory VAX</td><td>B3</td><td>Factory VAX equipment/sware failure</td><td>-1</td></tr><tr><td>3</td><td>Factory VAX</td><td>C3</td><td>Factory VAX vandalized/destroyed</td><td>1</td></tr><tr><td>3</td><td>Factory VAX</td><td>D3</td><td>Factory VAX fire/flood/strike/power</td><td>0</td></tr><tr><td>4</td><td>EDI gateway PC</td><td>A4</td><td>EDI gateway PC unauthorized access</td><td>-1</td></tr><tr><td>4</td><td>EDI gateway PC</td><td>B4</td><td>EDI gateway PC equipment/sware failure</td><td>-1</td></tr><tr><td>4</td><td>EDI gateway PC</td><td>C4</td><td>EDI gateway PC vandalized/destroyed</td><td>1</td></tr><tr><td>4</td><td>EDI gateway PC</td><td>D4</td><td>EDI gateway PC fire/flood/strike/power</td><td>0</td></tr></table>

![](/api/attachments/YWVFKKXV/fulltext/images/6468e994eee974414a885a698ecc8867695836e887a5d88ae4f6aa5418f91a38.jpg)  
Figure 6 Risk catalogue creation

Since, for each of the risks in the catalogue, we know the frequency of occurrence (from the vulnerability catalogue) and the impact (from the threat catalogue), we can define the exposure, as shown in Figure 6. Once again, the metric varies depending on the system but will we continue with the general case and measure exposure using a logarithmic money per time period metric. The simple metrics set out in Table 1 and Table 3 mean that we can define the annual exposure to a risk as the sum of the impact (of the associated threat) and the frequency (of the associated vulnerability). An excerpt from such a risk catalogue is shown in Table 5.

The various catalogues can be stored in any PC-based spreadsheet or database package, so the exposure calculations are trivial to automate. Furthermore, since the catalogues are automated, the risk analysis model can be used to extract a wide variety of types of information.

At the end of this step, the exposures for each risk in the risk catalogue can be totalled (remembering they are logarithmic) and converted back to money to obtain a good approximation to the total financial exposure of the business for the system under consideration.

## Countermeasure identification

Countermeasures are applied to reduce exposure. Depending on the nature of the risk, an organization may choose from a range of countermeasures. For the purposes of SRA, we can categorize these as:

(1) risk shifting, where the risk is shifted by applying a countermeasure (such as insurance or subcontracting) to the risk itself which moves all or part of the exposure to a third-party – such countermeasures involve no change to the business or technology models

(2) risk reduction, where the annual exposure is reduced because a countermeasure is applied to the vulnerability which, in essence, reduces the frequency of occurrence – such countermeasures involve a change to the technology model but no change to the business model or information model

Table 5 Excerpt from risk catalogue

<table><tr><td>Tht</td><td>TA</td><td>Vul.</td><td>#</td><td>Ex.</td><td>Attack</td></tr><tr><td>5</td><td>1.1</td><td>A1.1</td><td>257</td><td>2</td><td>Customer delivery lost/corrupt because unauthorized access</td></tr><tr><td>5</td><td>1.1</td><td>B1.1</td><td>258</td><td>2</td><td>Customer delivery lost/corrupt because equipment/sware failure</td></tr><tr><td>5</td><td>1.1</td><td>C1.1</td><td>259</td><td>4</td><td>Customer delivery lost/corrupt because vandalized/destroyed</td></tr><tr><td>5</td><td>1.1</td><td>D1.1</td><td>260</td><td>3</td><td>Customer delivery lost/corrupt because fire/flood/strike/power</td></tr><tr><td>5</td><td>3</td><td>A3</td><td>261</td><td>2</td><td>Customer delivery lost/corrupt because unauthorized access</td></tr><tr><td>5</td><td>3</td><td>B3</td><td>262</td><td>2</td><td>Customer delivery lost/corrupt because equipment/sware failure</td></tr><tr><td>5</td><td>3</td><td>C3</td><td>263</td><td>4</td><td>Customer delivery lost/corrupt because vandalized/destroyed</td></tr><tr><td>5</td><td>3</td><td>D3</td><td>264</td><td>3</td><td>Customer delivery lost/corrupt because fire/flood/strike/power</td></tr><tr><td>C5</td><td>1.1</td><td>A1.1</td><td>265</td><td>1</td><td>Customer delivery disclosed because unauthorized access</td></tr><tr><td>C5</td><td>1.1</td><td>B1.1</td><td>266</td><td>1</td><td>Customer delivery disclosed because equipment/sware failure</td></tr><tr><td>C5</td><td>1.1</td><td>C1.1</td><td>267</td><td>3</td><td>Customer delivery disclosed because vandalized/destroyed</td></tr><tr><td>C5</td><td>1.1</td><td>D1.1</td><td>268</td><td>2</td><td>Customer delivery disclosed because fire/flood/strike/power</td></tr><tr><td>C5</td><td>3</td><td>A3</td><td>269</td><td>1</td><td>Customer delivery disclosed because unauthorized access</td></tr><tr><td>C5</td><td>3</td><td>B3</td><td>270</td><td>1</td><td>Customer delivery disclosed because equipment/sware failure</td></tr><tr><td>C5</td><td>3</td><td>C3</td><td>271</td><td>3</td><td>Customer delivery disclosed because vandalized/destroyed</td></tr><tr><td>C5</td><td>3</td><td>D3</td><td>272</td><td>2</td><td>Customer delivery disclosed because fire/flood/strike/power</td></tr><tr><td>A5</td><td>1.1</td><td>A1.1</td><td>273</td><td>1</td><td>Customer delivery not available because unauthorized access</td></tr><tr><td>A5</td><td>1.1</td><td>B1.1</td><td>274</td><td>1</td><td>Customer delivery not available because equipment/sware failure</td></tr><tr><td>A5</td><td>1.1</td><td>C1.1</td><td>275</td><td>3</td><td>Customer delivery not available because vandalized/destroyed</td></tr><tr><td>A5</td><td>1.1</td><td>D1.1</td><td>276</td><td>2</td><td>Customer delivery not available because fire/flood/strike/power</td></tr><tr><td>A5</td><td>3</td><td>A3</td><td>277</td><td>1</td><td>Customer delivery not available because unauthorized access</td></tr><tr><td>A5</td><td>3</td><td>B3</td><td>278</td><td>1</td><td>Customer delivery not available because equipment/sware failure</td></tr><tr><td>A5</td><td>3</td><td>C3</td><td>279</td><td>3</td><td>Customer delivery not available because vandalized/destroyed</td></tr><tr><td>A5</td><td>3</td><td>D3</td><td>280</td><td>2</td><td>Customer delivery not available because fire/flood/strike/power</td></tr></table>

(3) risk avoidance, where the exposure is reduced because a countermeasure is applied to the threat which reduces the impact of the threat – such countermeasures involve a change to the business model but no change to the technology model.

Countermeasure identification tends to be an interactive process. Some vulnerabilities, for example, lead to more risks than others and therefore overall exposure can be minimized by applying countermeasures to these vulnerabilities. A simple way to determine these 'hotspots' is by sorting the risk catalogue twice, first by vulnerability and then by exposure. A pattern will generally emerge which will direct effort in the most productive way by helping to close vulnerabilities which have the major effect on high exposures.

The catalogues created by SRA-IS therefore give a simple and straightforward means of evaluating the effect of various countermeasures on organizational exposure. Once again, assuming that the catalogues have been implemented using standard database or spreadsheet technology, it is an interactive process to insert different countermeasures and let the model recalculate the new exposures.

The models give results that have confidence attached. If the effect of a countermeasure is to reduce exposure by more than the cost of the countermeasure, then the countermeasure is worth implementing. In this case, the cost of the countermeasure and the resulting reduction in exposure can be factored into business planning.

## Conclusions

SRA has been developed by Hyperion over the last three years. SRA-IS is a subset of SRA specific to IS. It has been simplified by taking into account certain characteristics of IS—in particular, the fact that the value of information assets is substantially greater than the value of physical assets—so that it provides a simple but powerful means of dealing with risk in commercial organizations.

SRA has been applied, very successfully, to a number of systems. These include an information gathering and dissemination network for the International Stock Exchange and IT for the European Space Agency manned space mission Colombus.

The SRA-IS methodology outlined in a very simplified form in this paper represents a major step forward in the handling of risk analysis and management. It provides a structured method of dealing with the broad class of IS in such a way as to give specific and prescriptive results. It is:

(1) complete and consistent, fully integrated with structured analysis methodologies—it uses standard structured models which already exist in many organizations and so does not require a large initial investment

(2) straightforward, as it does not require special software or over-complex training—it is hierarchical in the same way that the structured models are, so high level analysis can be used to identify areas requiring further attention and then more detailed analysis can be applied to these specific areas

(3) able to cope with all implementations of information systems, whether centralized or fully-distributed - it makes no assumptions as to the characteristics of the technology model (or models) that will be supporting the business model.

As the procedures can be automated using readily-available spreadsheet or database programs, risk management becomes a cost-effective and interactive process. This means that the cost of countermeasures and resulting reduction in exposures can be evaluated in their proper business context. This further means that decisions on countermeasure expenditure can be taken in confidence.

The use of the methodology to maintain a management picture of risk and to assess the effect of changes in the business, information or technology models on organizational exposure provides a structured basis for effective risk management. This topic will be covered in detail in a future paper.

## References

Davies, D. (1990) Computer Risk Management. Computer Law and Security Report, 5 (Eclipse).

Dunn, R. (1990) Data integrity and executive Information Systems. Computer Control Quarterly, 8, 23–25.

Federal Information Processing Standard (FIPS) (1979) Publication 65.

Harris, R. and McEvoy, N. (1990) Security analysis in SSADM presented at SSADM User's Conference, Keele University, UK.

Jamieson, R. and Low, G. (1990) Local area network operations: a security, control and audit perspective. Journal of Information Technology, 5, 63–72.

Katz (1990) Business/enterprise modelling. IBM Systems Journal, 28.

Landwehr, C. (1986) The best available technologies for computer security. Computer, July, 86–95.

Moses, R. (1990) The Current Status of CRAMM — The CCTA Risk Analysis Methodology, in Information Security: Confidentially, Integrity and Availability, (Unicorn, London).

Nicholls, M. (1987) Introducing SSADM — The NCC Guide, (NCC Publications, Manchester).

Reed and Watt (1989) Computer Risk Manager — A Manual for EDP Contingency Planning (2nd Edn) (Elsevier).

Seberry and Pieprzyk (1989) Encryption methods of information protection, in Cryptography: An Introduction to Computer Security (Prentice-Hall, London).

## Biographical note

David G.W. Birch graduated from the University of Southampton with a BSc (Hons) in Physics and then joined Logica, where he spent several years working as a consultant specializing in communications. In 1986, he was one of the founders of Hyperion Systems Limited and now provides specialist consultancy to a variety of clients. He has worked on a wide range of systems in the UK, Europe, the Far East and North America for clients as diverse as SWIFT, the International Stock Exchange, the Ministry of Defence and the Indonesian PTT. He is a

Visiting Lecturer in Information Technology Management at the City University Business School in London and the author of numerous papers and articles.

Neil A. McEvoy graduated from Oxford University with an MA before joining Logica as a consultant. After playing a key role in the development of a major image processing product range, he moved on to specializing in security and networking. In 1986, he was one of the founders of Hyperion Systems Limited and now provides specialist consultancy to a variety of clients. He has worked on a wide range of projects in the UK and Europe, for clients including the European Space Agency, APACS and the Ministry of Defence. He has sat on a number of BSI Technical Committees and represented the UK interest at ISO level.

Address for correspondence: Hyperion Systems Limited, 8 Frederick Sanger Road, Surrey Research Park, Guildford, Surrey GU2 5YD, UK.
