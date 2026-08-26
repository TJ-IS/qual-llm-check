---
otero_id: 5676
otero_key: "AZ4C7ZE5"
title: "Contracting cleaning services in a European public underground transportation company with the aid of a DSS"
authors: "Antonio Jiménez; Alfonso Mateos; Sixto Ríos-Insua; Luis Carlos Rodríguez"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.06.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Contracting cleaning services in a European public underground transportation company with the aid of a DSS

Antonio Jiménez <sup>⁎</sup>, Alfonso Mateos, Sixto Ríos-Insua, Luis Carlos Rodríguez

Department of Artificial Intelligence, School of Computer Science, Technical University of Madrid Campus de Montegancedo s/n, 28660 Boadilla del Monte, Madrid, Spain

Available online 10 August 2006

## Abstract

This paper deals with the selection of a supplier for cleaning services in a European public underground transportation company as established in the European Community directives, where several conflicting criteria, such as improving service levels and reducing total service costs, must be taken into account simultaneously. The problem is analyzed in depth using the decision analysis methodology, and a decision support system, the Generic Multi-Attribute Analysis system, is used to allay the operational difficulties involved. This system can deal with incomplete information about decision-maker preferences, accounts for uncertainty about offer performance, and uses so-called decision-making with partial information to identify the best offer, taking advantage of imprecise inputs.

© 2006 Elsevier B.V. All rights reserved.

Keywords: Cleaning services; Decision analysis methodology; Decision support system; Incomplete information

## 1. Introduction

Cleaning is a part of a major service provided to underground transportation users. When done well, it is often taken for granted; when done poorly, it is immediately noticed. Cleanliness is directly tied to user satisfaction, as well as to performance quality levels for the public transportation services.

The appearance of the underground buildings, trains and public spaces, as measured by overall cleanliness, is one of the most significant criteria, in conjunction with reliability and safety, for assessing the effectiveness of underground management.

From a cost management perspective, the cleaning service amounts to an important part of the operating costs of an underground transportation service, accounting, in this case, for close to 10% of total annual operating expenses.

In the past, service contracting with both public agencies and private companies alike has suffered from systemic problems (i.e., cost overruns, delays and poor performance). The problems arise due to two fundamental premises: the intangibility and heterogeneity of the service and the idea that production and consumption are inseparable. Inherent service intangibility, heterogeneity and inseparability greatly constrain service acquisition and management, see Ref. [21].

No comprehensive view has been taken of available cleaning services measurement or of systems that can be easily used at the work place to inspect cleaning activities and provide an objective view of the results achieved, making an objective assessment of contractor performance difficult.

To improve cleaning services contracting, we worked on different initiatives throughout the acquisition process to improve the service level and to significantly reduce total service cost. In addition, as a public service, this acquisition process had been carried out according to the public procurement policies and legislation for the national and European public organizations, as established in directives 98/4/EC of the European Parliament and of the Council of 16 February 1998 amending Directive 93/38/EEC coordinating the procurement procedures of entities operating in the water, energy, transport and telecommunications sectors, and Directive 97/52/EC of the European Parliament and of the Council of 13 October 1997 amending Directives 92/50/EEC, 93/36/EEC and 93/37/EEC concerning the coordination of procedures for the award of public service contracts, public supply contracts and public works contracts, respectively.<sup>1</sup>

For the purpose of determining the most economically advantageous suppliers as regards the problem under consideration, several conflicting criteria were taken into account simultaneously to provide the most relevant information about what other factors, in conjunction with prices, to apply during the award of contract process, like delivery conditions and human resources, technical merit and resources, quality control procedures, etc. These criteria were compiled as a result of a team effort, including procurement and technical experts from the organizational areas responsible for cleaning services, finance and other departments or representatives, such as legal affairs and customer service. They were all integrated into a cross-functional team responsible for preparing the process and gathering all the information necessary to achieve the desired outcomes. From now on, we will denote this group of experts and representatives as decision-makers (DMs).

Preference trade-offs between differing levels of achievement of one criterion and another must be taken into account simultaneously. Moreover, it may be far from straightforward to specify how each offer will perform in the end. This requires formal analysis, because it is very difficult to deal with the above complexities informally in the mind.

The goal of Decision Analysis (DA) is to structure and simplify the task of making hard decisions, see Refs. [3], [8] and [9]. It is developed on the assumption that the alternatives (offers from suppliers) will appeal to the DMs depending on how each offer is likely to perform and what DM preferences are. The DA cycle can be divided into four steps: (1) structuring the problem (which includes specifying objectives, building a value hierarchy and establishing attributes for the lowest-level objectives); (2) identifying the feasible offers, their performances and uncertainty (if necessary); (3) quantifying preferences (which includes the assessment of the component attribute utilities, as well as the value tradeoffs); (4) evaluating offers and performing sensitivity analysis (SA).

The Generic Multi-Attribute Analysis (GMAA) System, a user-friendly PC-based decision support system founded on an additive multi-attribute utility model (http://www.dia.fi.upm.es/∼ajimenez/GMAA), will be used to allay many of the operational difficulties involved in the DA cycle, see, e.g., Refs. [5], [7] and [17].

Note that the group of DMs were guided throughout the decision-making process by experts in DA methodology, specifically, the team that developed and implemented the GMAA system. Decision-theory concepts and tools included in the GMAA system were clarified at several meetings.

We have divided the paper, according to DA stages, into five sections, where we describe the cleaning service contracting problem and how it is modelled in the GMAA system and, finally, provide some conclusions.

## 2. Structuring the problem

An objective hierarchy including all the relevant aspects related to the problem under consideration was built, aimed at improving DM understanding of the decision. For our complex decision-making problem, it describes how offers have to be evaluated in terms of technical merits and costs, see Fig. 1.

There are five main top-level objectives: Delivery conditions and human resources (Delivery Con), which accounts for how consistent and coherent the human resources allocated to the services are; Technical merit and resources (Tech Resourc), which it is an important efficiency factor leading to a significant reduction in labor cost; Price (Price), which represents the lowest price offered by suppliers; Quality control procedures (Quality Mean), which accounts for accredited quality certifications and how quality systems and procedures are deployed; and Graffiti prevention and cleanup (Graffiti), which is one of the most common incidents detracting from the appearance of the underground buildings.

The objective Delivery conditions and human resources is split into three sub-objectives, Workload,

![](/api/attachments/AZ4C7ZE5/fulltext/images/6b97bd67986f33c306f6744feff9e56f3f79628d1fac0589efd29f5f44ddb29d.jpg)  
Fig. 1. Objective hierarchy.

Workload allocation and Cost optimization program. Workload (Workload) quantifies how much effort is deployed in terms of resources to achieve service performance objectives. Workload allocation (Wrk. Allocat) measures the coherence and consistency of the allocation of the resources throughout the underground facilities and buildings. Cost optimization program (Cost optimiz) measures the suitability of supplier cost reduction initiatives using four additional sub-objectives: Understanding of client's needs and issues (Understand), in which suppliers will be rewarded in as much as their offers show a good understanding of the cleaning needs regarding underground operations and public transportation services; Cost reduction approach (Cost Reduct.), in which case suppliers will be rewarded in as much as their offers develop a structured solution for minimizing service costs within the contract period and providing details on how other clients have successfully implemented cost reduction programs; Suitability of cost reduction initiatives (Suit Reduct), which quantifies how applicable and realistic the cost reduction initiatives are as things now stand and how they will ensure significant cost savings; and Cost reduction target setting and performance monitoring (Target Set), in which suppliers will be rewarded in as much as their offers include procedures and measures and key performance indicators, setting aggressive targets to drive for change. These metrics and measurements procedures will form a model for successfully budgeting for and tracking cost savings.

Technical merit and resources (Techn. Resources) is also split into two sub-objectives, Quantity of technical means and Technical resources suitability. Suppliers will be rewarded in as much as their offers include numerous and extensive use of technical resources by Quantity of technical means (Techn. Means). Technical resources suitability (Res. Suitab.) is measured taking into account three additional sub-objectives: Equipment suitability to client's buildings (S. Buildings), which quantifies its fitness for underground facilities (accessibility, building layout, types of surfaces, etc.) and possible adverse environmental impacts; Equipment technical documentation (Tech. Docum.), related to how well technical documentation describes the equipment providing a good specification and understanding of equipment performance; and Cleaning product technical documentation (Clean. Doc.), which accounts for how well technical documentation describes the cleaning products, providing a good specification and understanding of product performance.

The objective Quality control procedures is measured in terms of two sub-objectives, Number of quality certifications and Quality measurement systems and procedures. For Number of quality certifications (Qual. Certif), suppliers will be rewarded for having quality certifications accredited by national or European quality committees and institutions. Quality measurement systems, documentation and procedures (Sys/Doc/ Proc) accounts for how quality systems and procedures are deployed. This sub-objective is further split into five sub-objectives: Supplier quality control capabilities (Control Capa.), which quantifies current supplier capabilities in terms of the supplier's quality assurance organization, its structure, number of resources, current skills and attested competencies; Quality systems, plans and procedures described as required (As Required), in which suppliers will be rewarded in as much as their offer contents have been developed according to the tender guidelines; Poor performance corrective actions (Correc. Act.), which measures the proposed procedures and action plans to be put in place to remedy poor performance and incidents in cleaning services delivering; Change management approach and training (Training), which accounts for the communications and training actions to be adopted to ensure that all people (employees, contractors, users) have the required knowledge and meet the operational and business requirements for delivering the services; and Quality performance monitoring (P. Monitoring), which accounts for the measurement system to be implemented, i.e., what will be inspected, how the inspection will be carried out and the measurement criteria to be used during inspection are evaluated to verify that they guarantee greater objectivity, completeness and high quality services.

Finally, Graffiti prevention and cleanup takes into account two sub-objectives, past experiences and graffiti cleanup procedures and products. Past experiences in graffiti prevention and cleanup (Experience) verifies supplier competence, assessing details on how the supplier has successfully implemented these specific services for other clients. Graffiti cleanup procedures and product features (Proc and Prods) is measured by taking into account three additional sub-objectives: Suitability of graffiti cleanup procedures (Suit. Proced), which measures their fitness for underground facilities (building layout, types of surfaces, types of graffiti, etc.) and possible adverse environmental impacts, Technical solution for prevention and cleanup (Tech. Solut) and Suitability of graffiti cleaning products (Suit. Produc), which quantify how well the technical documentation describes the equipment, leading to a good specification and understanding of the equipment and product performance, respectively.

Once the objective hierarchy has been built, attributes must be established for the lowest-level objectives to indicate to what extent they are achieved by the respective offers. Table 1 shows the attribute names, units and ranges for cleaning service contracting.

Note that Experience and Qual. Certif are assigned discrete attribute values. For Experience, 0 means No references, 1—one reference, 2—two or three references, 3—two or three similar problems and 4—three or more similar problems; while for Qual. Certif, 0 means no certificate, 1—quality control proc./prog., 2— European certificates and 3—EN ISO 9001/ISO 9002. On the other hand, Workload, Wrk. Allocat, Techn.

Attribute names, units and ranges

<table><tr><td></td><td>Unit</td><td>Range</td></tr><tr><td>Workload</td><td>Absolute percentage error (APE)</td><td>[0, 50]</td></tr><tr><td>Wrk. allocat</td><td>Mean absolute percentage error (MAPE)</td><td>[0, 100]</td></tr><tr><td>Understand</td><td>Subjective scale</td><td>[0, 1]</td></tr><tr><td>Cost reduct.</td><td>Subjective scale</td><td>[0, 1]</td></tr><tr><td>Suit reduct</td><td>Subjective scale</td><td>[0, 1]</td></tr><tr><td>Target set</td><td>Subjective scale</td><td>[0, 1]</td></tr><tr><td>Techn. means</td><td>Number of pieces of equipment</td><td>[0, 90]</td></tr><tr><td>S. buildings</td><td>Subjective scale</td><td>[0, 1]</td></tr><tr><td>Tech. docum.</td><td>Subjective scale</td><td>[0, 1]</td></tr><tr><td>Clean. doc.</td><td>Subjective scale</td><td>[0, 1]</td></tr><tr><td>Price</td><td>Monetary units</td><td>[15,000, 30,000]</td></tr><tr><td>Qual. certif</td><td>Discrete values</td><td>0, 1, 2 and 3</td></tr><tr><td>Control capa</td><td>Subjective scale</td><td>[0, 1]</td></tr><tr><td>As required</td><td>Subjective scale</td><td>[0, 1]</td></tr><tr><td>Correc. act.</td><td>Subjective scale</td><td>[0, 1]</td></tr><tr><td>Training</td><td>Subjective scale</td><td>[0, 1]</td></tr><tr><td>P. monitoring</td><td>Subjective scale</td><td>[0, 1]</td></tr><tr><td>Experience</td><td>Discrete values</td><td>0, 1, 2, 3 and 4</td></tr><tr><td>Suit. proced</td><td>Subjective scale</td><td>[0, 1]</td></tr><tr><td>Tech. solut</td><td>Subjective scale</td><td>[0, 1]</td></tr><tr><td>Suit. produc</td><td>Subjective scale</td><td>[0, 1]</td></tr></table>

Means and Price are straightforward in the sense that they are directly related to their associated objectives, and a continuous scale is used.

The units for Workload and Wrk. Allocat, i.e., APE and MAPE, represent the following:

• If the number of offers is odd and higher than 3, they are ordered from the highest to the lowest value, and a mean (M) is assessed by discarding the highest and lowest values.

• If the number of offers is even and higher than 2, the mean is assessed considering all values. Then, the offer whose difference with respect to the mean is the highest, positive or negative, is discarded. A new mean (M) is then assessed taking the remaining values.

• If the number of offers is 2 or 3, the mean (M) is assessed considering all values.

Then, the absolute percentage error and the mean absolute percentage error for the j-th offer, APEj and MAPEj, are:

$$
\mathrm{APE} _ {j} = \frac {\mathrm{ABS} (M - \text { value } _ {j})}{M}
$$

$$
\mathrm{MAPE} _ {j} = \frac {1}{N} \times \sum_ {i = 1} ^ {N} \frac {(M - \text { value } _ {j}) \times 1 0 0}{M}
$$

where N is the number of offers. Consequently, the best value for attributes is 0, while the worst values are 50 and 100, respectively.

Finally, the remaining attributes are subjective, which means that there is no objective quantity, and a subjective index has been constructed associated with a scale from 0 (worst) to 1 (best).

## 3. Quantifying decision-maker preferences

Following the European Community directives, stating that criteria should be set and at least ordered by importance before examining the offers, stages 2 and 3 in the DA methodology must be switched around, i.e., DM preferences must be quantified before identifying offers.

Quantifying preferences involves assessing the single DM attribute utilities, which represent DM preferences concerning possible offer performances, and weights, which indicate the relative importance of criteria in the objective hierarchy. Both will be used later to evaluate the offers by means of an additive multi-attribute utility function.

Preferences were assessed as a result of a team effort, including procurement and technical experts from the organizational areas responsible for cleaning services, finance and other departments or representatives such as legal affairs and customer service. Procedures for preference assessment provided by the GMAA system were used, which can deal with incomplete information through value intervals as responses to the probability questions the DM is asked, see Ref. [17] or [7]. This is less stressful on experts, see Refs. [13], [19] and [20]. Moreover, it makes the system suitable for group decision support, because individual conflicting views or judgments in a group of DMs can be captured through imprecise responses, see, e.g., [10].

For attributes with a continuous scale (Price, Workload, Workload allocation and Quantity of technical means) precise linear piecewise utility functions were assessed. For attributes for which a set of discrete attribute values was defined (Number of quality certifications and Past experiences in graffiti prevention and cleanup), an imprecise utility for each discrete attribute value was provided. No preferences have to be assessed for the remaining attributes, all of which have a subjective scale. In this case, the subjective offer performances between 0 (worst value) and 1 (best value) shown in the next section were used directly as utilities.

Figs. 2 and 3 show the precise piecewise utility functions and imprecise utilities for discrete attribute values examined, respectively.

Note that utility functions are decreasing for Workload, Wrk. Allocat and Price, and increasing for Technical Means.

Additionally, attribute weights were hierarchically elicited, i.e., local objective weights along each branch and level of the hierarchy representing their relative importance were elicited in ascending order and then attribute weights were assessed by multiplying the local weights of the objectives along the path from the overall objective to each attribute.

Again, weighting procedures provided by the GMAA were used, a direct assignment and a method based on trade-offs, [8]. As in the utility assessment, imprecision concerning DM responses was allowed by means of ranges of responses. Then, a normalization process was automatically performed on the DM responses, leading to an average normalized weight and a normalized weight interval for each objective under consideration, see Refs. [5] and [7].

For instance, Table 2 shows the DM responses for top-level objectives weight elicitation by direct assignment and the respective average normalized weights and normalized weight intervals.

![](/api/attachments/AZ4C7ZE5/fulltext/images/9fc59b2c506a7118bf349a417e2f6198cea9b64dfb339820a805dd4bdff7145e.jpg)

![](/api/attachments/AZ4C7ZE5/fulltext/images/416dd9f7ae9139fce88cc5802425cdd621e1dea34179133ee4d71559037347c8.jpg)

![](/api/attachments/AZ4C7ZE5/fulltext/images/17634772681dee79311463551286cb844737fe81ab01f3e94806cdc929d7c3f8.jpg)

![](/api/attachments/AZ4C7ZE5/fulltext/images/b03d76dcb9235ab35e600f73cb55af8f38170ae2685752cb4d22616786726819.jpg)

![](/api/attachments/AZ4C7ZE5/fulltext/images/1476b11bba16e5f2ed35665e7c492cea98119c4055dfd46c6035b0ec8dac6622.jpg)  
Fig. 2. Piecewise linear utility functions.

Fig. 4 shows the local average normalized weights in the objectives hierarchy, and Fig. 5 illustrates attribute weights, calculated by multiplying local average normalized weights and the endpoints of the normalized weight intervals of the objectives along the path from the overall objective to the respective attribute.

Looking at the above figure, we can see that the most important attribute in the decision is Price, with an average normalized weight of 0.513, followed far behind by Workload (Workload), Quantity of Tech. Means (Techn. Means), N. quality certification (Qual. Certif), Experience with Graffiti (Experience) and Workload Allocation (Wrk. Allocat), with average normalized weights of 0.125, 0.082, 0.052, 0.052 and 0.036, respectively.

## 4. Alternatives identification

Next, the feasible supplier offers must be identified and measured in terms of attributes. Table 3 shows the scores or performances of the different attributes for the six offers considered.

Note that although the table includes precise performances, uncertainty about some of them was taken into account by means of percentage deviations. These percentage deviations represent tolerances or correction factors for offers where information provided by the bidders was somewhat ambiguous or was not clear enough.

Specifically, a 20% deviation was introduced in Workload for offers 5 and 6, and 15% for offer 4; a 10% deviation was introduced in Wrk. Allocat for offers 3 and 6, and 20% for offer 2; a 30% and a 15% deviation was introduced in Techn. Means for offers 3 and 5, respectively. In all these attributes the original offers included some overlapping information, e.g. resources and equipment overlaps.

![](/api/attachments/AZ4C7ZE5/fulltext/images/799099de596ecec6e41098c94a26444e7ffd8dcee99e03264fbe9192dbe0119f.jpg)

![](/api/attachments/AZ4C7ZE5/fulltext/images/9e4969a168da0c8e87f0f05d6be0ac45775bcd2cd4d7e65bc7337e44ded1a864.jpg)

![](/api/attachments/AZ4C7ZE5/fulltext/images/cce8fcd4abbe3e8dce51c853caf9dd339d4e06ad85cafc910da8faf8fa3553ab.jpg)  
Fig. 3. Imprecise utilities for discrete attribute.

Table 2  
DM responses and respective weights for top-level objectives

<table><tr><td></td><td>Responses</td><td>Avg. norm. weight</td><td>Norm. weight interval</td></tr><tr><td>Delivery con</td><td>[0.15, 0.20]</td><td>0.179</td><td>[0.154, 0.205]</td></tr><tr><td>Tech resourc</td><td>[0.10, 0.10]</td><td>0.103</td><td>[0.103, 0.103]</td></tr><tr><td>Price</td><td>[0.50, 0.50]</td><td>0.513</td><td>[0.513, 0.513]</td></tr><tr><td>Quality mean</td><td>[0.05, 0.15]</td><td>0.103</td><td>[0.051, 0.154]</td></tr><tr><td>Graffiti</td><td>[0.05, 0.15]</td><td>0.103</td><td>[0.051, 0.154]</td></tr></table>

Additionally, a 10% deviation was introduced in S. Buildings for offers 2 and 5, and 5% for offer 3; and a 10% deviation was introduced in Control Capa for offers 3 and 5, and in Suit. Proced for offers 3, 4, 5 and 6. In these cases, where a subjective scale has been used, the percentage deviations aimed to account for missing technical knowledge, e.g. the fitness of certain equipment and graffiti cleanup procedures for underground facilities and possible adverse environmental impacts, and, additionally, to match up different evaluations by members of the cross-functional team who used their own approach assessment based on their experience and knowledge, e.g. how a quality assurance organization has to be structured to be more effective.

## 5. Evaluating offers

This step involves evaluating each offer to help identify the best one by means of an additive multiattribute utility model, which takes the form

$$
\begin{array}{l} u (\text { Offer   } j) = \sum_ {i = 1} ^ {n} w _ {i} u _ {i} (x _ {i} ^ {j}) \\ \quad = w _ {1} u _ {1} (x _ {1} ^ {j}) +... + w _ {n} u _ {n} (x _ {n} ^ {j}), \end{array}
$$

where $x _ { j } ^ { i }$ is the consequence of the j-th offer for the attribute $X _ { i } , ~ u _ { i }$ are the single utilities assigned to the respective attribute $X _ { i }$ and $w _ { i }$ is the i-th attribute weight.

For the reasons described in Refs. [12] and [18], we consider the additive form to be a valid approach.

![](/api/attachments/AZ4C7ZE5/fulltext/images/cd2b7f495c7a37ee87cfaea8c28014eb4c367a1ffa5aa7c8f0f2d24512b754b6.jpg)  
Fig. 4. Local average normalized weights.

![](/api/attachments/AZ4C7ZE5/fulltext/images/831a7579919b87fca333daa7d4dbaa4e95a03fba4fd2b138f7b84d04bf6b6558.jpg)  
Fig. 5. The attribute weights.

As we have considered imprecision concerning single utilities and weights and uncertainty about the offer performances, the additive model is used to assess, on the one hand, average overall utilities, on which the ranking of offers is based and, on the other hand, minimum and maximum overall utilities, which give further insight into the robustness of this ranking, see Fig. 6.

Offers 3 and 6 are the best and worst ranked ones, with average overall utilities of 0.837 and 0.351, respectively. Looking at the utility intervals, we can discard offer 6, because 13 its maximum utility is lower than the minimum utility of offer 2. Consequently, we can conclude that it is dominated. However, although offer 3 appears to be the most highly recommended, the overlapped utility intervals (ranking robustness) should be examined in more detail through SA.

Also another intermediate objective can be selected to rank by. Fig. 7 shows the ranking of offers for Delivery conditions and human resources, where offer 1 is now the best-ranked and dominates the others, while offer 3 is the second best-ranked.

As shown in Fig. 6, the GMAA system provides different displays of ranking results, [16], such as a

Table 3 Offer performances

<table><tr><td></td><td>Offer 1</td><td>Offer 2</td><td>Offer 3</td><td>Offer 4</td><td>Offer 5</td><td>Offer 6</td></tr><tr><td>Workload</td><td>5.62</td><td>11.85</td><td>14.61</td><td>29.21</td><td>33.31</td><td>36.19</td></tr><tr><td>Wrk. allocat</td><td>13.63</td><td>30.66</td><td>19</td><td>5.78</td><td>16.27</td><td>26.6</td></tr><tr><td>Understand</td><td>0.46</td><td>0.49</td><td>0.74</td><td>0.21</td><td>0.34</td><td>0.33</td></tr><tr><td>Cost reduct.</td><td>0.35</td><td>0.64</td><td>0.20</td><td>0.83</td><td>0.24</td><td>0.36</td></tr><tr><td>Suit reduct</td><td>0.55</td><td>0.63</td><td>0.75</td><td>0.54</td><td>0.64</td><td>0.24</td></tr><tr><td>Target set</td><td>0.60</td><td>0.57</td><td>0.75</td><td>0.58</td><td>0.21</td><td>0.28</td></tr><tr><td>Techn. means</td><td>0.23</td><td>0.19</td><td>0.63</td><td>0.31</td><td>0.8</td><td>0.24</td></tr><tr><td>S. buildings</td><td>0.52</td><td>0.88</td><td>0.99</td><td>0.74</td><td>0.33</td><td>0.71</td></tr><tr><td>Tech. docum.</td><td>0.86</td><td>0.2</td><td>0.84</td><td>0.40</td><td>0.21</td><td>0.58</td></tr><tr><td>Clean. doc.</td><td>0.54</td><td>0.35</td><td>0.31</td><td>0.87</td><td>0.58</td><td>0.49</td></tr><tr><td>Price</td><td>18,088</td><td>19,329</td><td>17,083</td><td>17,994</td><td>17,549</td><td>21,993</td></tr><tr><td>Qual. certif</td><td>3</td><td>3</td><td>3</td><td>3</td><td>2</td><td>1</td></tr><tr><td>Control capa</td><td>0.76</td><td>0.84</td><td>1</td><td>0.86</td><td>0.71</td><td>0.22</td></tr><tr><td>As required</td><td>0.85</td><td>0.57</td><td>0.81</td><td>0.85</td><td>0.73</td><td>0.51</td></tr><tr><td>Correc. act.</td><td>0.84</td><td>0.65</td><td>0.84</td><td>0.96</td><td>0.86</td><td>0.51</td></tr><tr><td>Training</td><td>0.88</td><td>0.54</td><td>0.48</td><td>0.75</td><td>0.84</td><td>0.27</td></tr><tr><td>P. monitoring</td><td>0.74</td><td>0.60</td><td>1</td><td>1</td><td>0.59</td><td>0.33</td></tr><tr><td>Experience</td><td>1</td><td>3</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>Suit. proced</td><td>0.12</td><td>0.51</td><td>0.88</td><td>0.71</td><td>0.62</td><td>0.84</td></tr><tr><td>Tech. solut</td><td>0.33</td><td>0.48</td><td>0.97</td><td>0.80</td><td>0.49</td><td>0.78</td></tr><tr><td>Suit. produc</td><td>0.35</td><td>0.58</td><td>0.76</td><td>0.88</td><td>0.90</td><td>0.89</td></tr></table>

![](/api/attachments/AZ4C7ZE5/fulltext/images/a2b33d9577a4c16531e6729d6d908cb4c63547578caf1d6c92e4b65c6df28d5e.jpg)  
Fig. 6. Offer evaluation.

Stacked Bar Ranking (provides more detail on how the alternative's average utilities for the attributes affect the average utility of the overall objective, see Fig. 8), a Measure of Utilities for Alternatives (shows performance of a single offer for the attributes, taking into account average consequences and individual utilities, and where the width of an attribute is proportional to its weight), or a Compare Alternatives Graph (provides a detailed comparison of the differences between two alternatives, see Fig. 9).

Note that, according to attribute weights in the decision, a good performance for the Price attribute leads to higher utilities in the overall objective, as this attribute makes the biggest contribution.

Looking at the Compare Alternatives Graph we can see which of the two selected offers have the higher average utility associated with the different attributes. The length of the horizontal bars is proportional to the difference in utility among the two. Note that offer 3 is better than offer 4 for Price, Workload and Quantity of Tech. Means (their average weight in the decision adds up to 0.72).

## 6. Sensitivity analysis (SA)

DA is typically an iterative process. Once the model has been built, SA is performed. This step should be considered as a means of encouraging DMs to think about the problem in more depth and can give further insight into the robustness of the recommendations. Refs. [14] and [15] introduce a framework for SA in multi-objective decision-making.

![](/api/attachments/AZ4C7ZE5/fulltext/images/5d4fd14981ebf8a5d67904c8d940bf3027bd13f0295280f5af5ddf04b70efe9c.jpg)  
Fig. 7. Ranking of offers for Delivery conditions and human resources.

![](/api/attachments/AZ4C7ZE5/fulltext/images/e4eb8e71d75225a0457b36bab3f0d3114b8c83fecfe2c5916bd3867b4b1899e7.jpg)  
Fig. 8. Stacked bar ranking.

The GMAA system provides several types of SA, see [16]. Classical SA and the assessment of stability weight intervals can be considered as pure SA. Classical SA essentially involves examining changes in the ranking of offers as a function of the input parameters.

Any offer performance, component utility or weight can be changed and the system takes charge of how this change is propagated through the objective hierarchy and automatically recalculates the overall utilities for each offer and the resulting ranking.

Stability weight intervals, i.e., the interval where the average normalized weight for any objective at any level in the hierarchy can vary without the best-ranked offer changing, can also be assessed. Stability weights interval for all objectives throughout the hierarchy is [0, 1], which implies that whatever their relative importance offer 3 remains the best-ranked offer, except for Delivery conditions and human resources (Delivery Con), see Fig. 10, and Quality control procedures (Quality Mean) with stability weight intervals [0, 0.598] and [0, 0.748], respectively. Consequently, if the average normalized weight for either of these nodes is modified and the new value is higher than 0.598 and 0.748, respectively, offer 3 will not be the best-ranked offer.

![](/api/attachments/AZ4C7ZE5/fulltext/images/ea200d29ffc291cb7d92f1fa2afad2e9aa372451d85920b9e544528574125bcc.jpg)  
Fig. 9. Comparing offers 3 and 4.

![](/api/attachments/AZ4C7ZE5/fulltext/images/9c4dd364834e00409ca65f7bf8129f0ca718b49c73e9b9fdfc9a85f3e7e728b7.jpg)  
Fig. 10. Weight stability interval.

Taking into account that the narrower a stability weight interval is the more sensitive the offers ranking is, we can conclude that the offers ranking is robust with respect to the elicited weights.

The system also includes so-called decision-making with partial information, [14], which intends to take advantage of the imprecise information collected during the assignment of single utilities and weights and the alternative performances entered under uncertainty by computing non-dominated and potentially optimal offers and using Monte Carlo simulation techniques.

The assessment of non-dominated and potentially optimal offers can reduce the set of offers of interest, [14,15], mainly by discarding dominated and/or nonpotentially optimal offers. Note that offer i is dominated by offer j when for all the possible combinations of imprecise input parameters (performances, component utilities and weights), the ranking for offer i is better than for offer j, while an offer is potentially optimal when it is the best-ranked offer for at least one combination of imprecise input parameters. This involves dealing with non-linear optimization problems that can be transformed into linear problems and solved using the Simplex Method, see Ref. [11].

Fig. 11 shows that only offer 3 is non-dominated and potentially optimal, so we can definitively conclude that it is the best offer.

On the other hand, the system runs simulation techniques for SA. This kind of SA uses Monte Carlo simulation, [2,4,6], allows simultaneous changes to attribute weights and generates results that can be easily analyzed statistically to provide more insight into the multi-attribute model recommendations. We propose selecting the weights at random using a computer simulation program so that the results of many combinations of weights can be explored efficiently. The system uses a multiplicative linear congruential generator based on Schrage's method, see Ref. [1].

![](/api/attachments/AZ4C7ZE5/fulltext/images/0bd1c071841ecbd7c8f2c328ead781d7618f8079da03e806a34fe70a51cfb011.jpg)  
Fig. 11. Non-dominance and potential optimality.

![](/api/attachments/AZ4C7ZE5/fulltext/images/a92e99d7e99ef14263553d167db859e0bce69c9b88c03f11db8fcd07ab694ac5.jpg)  
Fig. 12. Partial attribute rank.

Three general classes of simulation can be used: Random weights, weights for the attributes are generated completely at random, which implies no knowledge whatsoever of the relative importance of the attributes; Rank order weights, weights are randomly generated preserving a total or partial attribute rank, which may provide more meaningful results; and Response distribution weights, attribute weights are now randomly assigned values taking into account weight intervals provided by the DM in the weight elicitation methods.

Once the simulation has been run, the system computes several statistics about the rankings of each offer, like minimum, maximum, mean… This information can be useful for discarding some available offers, aided by a multiple boxplot display.

For our specific problem it is pointless to use Response distribution weights, because, as shown earlier, the imprecise elicited attribute weights (Fig. 5) lead to just one non-dominated and potentially optimal offer; offer 3. Consequently, this offer would always be best-ranked and no further information would be gained. However, it would be interesting to use Rank order weights to analyze the robustness of this recommendation. In this case, on the basis of the information in Fig. 5, the partial attribute rank shown in Fig. 12 would be used.

Fig. 12 reflects that the most important attribute in the decision is Price, followed by Workload, Quantity of technical means, Number of quality certifications, Past experiences in graffiti prevention and cleanup and Workload allocation, respectively. The remaining attributes are less important than the above, but there is no information about their relative importance.

Fig. 13 shows the multiple boxplot for this type of simulation, whereas the associated statistic measures are shown in Fig. 14.

Offers 1, 3 and 4 are the only offers that are bestranked across all 10,000 simulations, and their worst ranking is fourth, fourth and fifth, respectively. Looking at mean classifications, however, the best value is for offer 3: 1.382. Consequently, we can conclude that the recommendation to select offer 3 is robust.

It is important to note that the DMs were completely satisfied with this recommendation. SA tools played a key role in this respect. The results achieved in the assessment of non-dominated and potentially optimal offers and the simulation techniques with Rank order weights were conclusive.

![](/api/attachments/AZ4C7ZE5/fulltext/images/5b3b4ea469cd54ef02362e48b3c7544d1b1463e6462b0ae957ace3bdc0dfde80.jpg)  
Fig. 13. Multiple boxplot.

![](/api/attachments/AZ4C7ZE5/fulltext/images/71a2cf95175dde37d23b3222905ad1b30760dd50585aa15a587aa6f5219331cf.jpg)  
Fig. 14. Associated statistics measures.

## 7. Conclusions

The selection of a supplier for cleaning services in underground facilities is a complex decision-making problem where several conflicting criteria must be taken into account simultaneously, including prices, delivery conditions and human resources, technical merit and resources, or quality control procedures.

Throughout the paper, the problem has been analyzed in depth on the basis of the decision analysis methodology. An objectives hierarchy including all the relevant aspects related to the problem under consideration has been built, decision-makers' preferences have been quantified and offers have been identified as well as their performances in terms of the attributes established for the lowest-level objectives. Finally, an additive multi-attribute utility model has been used to identify the best one offer, leading to imprecise overall utilities and an offer ranking on the basis of average overall utilities. As a result, offer 3 appears to be the best offer for selection.

Moreover, taking advantage of the sensitivity analysis tools provided by the Generic Multi-Attribute Analysis system, we have reached the conclusion that it is a robust recommendation. Specifically, stability weight intervals are wide, so the recommendation is not sensitive to the elicited objective weights; offer 3 is the only nondominated and potentially optimal offer; and the use of a ranking of attributes by partial importance attribute rank according to elicited attribute weights in simulation techniques confirms the above results.

Consequently, the GMAA system has been proven to be an adequate tool for modeling the problem under consideration on the basis of the decision analysis methodology and for achieving a better understanding of the recommendation and its robustness.

## Acknowledgments

This paper was supported by the Spanish Ministry of Education and Science Project TSI2004-06801-C04- 04 and the Madrid regional government project S-505/ TIC/02.

## References

[1] P. Bratley, B.L. Fox, E.L. Schrage, A Guide to Simulation, Springer-Verlag, New York, 1983.

[2] J. Butler, J. Jia, J. Dyer, Simulation techniques for the sensitivity analysis of multi-criteria decision models, European Journal of Operational Research 103 (1997) 531–546.

[3] R.T. Clemen, Making Hard Decisions: An Introduction to Decision Analysis, Duxbury Press, Beltmon, 1996.

[4] J.S. Dyer, T. Edmunds, J.C. Butler, J. Jia, A multiattribute utility analysis of alternatives for the disposition of surplus weaponsgrade plutonium, Operations Research 46 (6) (1998) 749–762.

[5] A. Jiménez, S. Ríos-Insua, A. Mateos, A decision support system for multiattribute utility evaluation based on imprecise assignments, Decision Support Systems 36 (1) (2003) 65–79.

[6] A. Jiménez, S. Ríos-Insua, A. Mateos, MonteCarlo simulation techniques in a multi-attribute decision support system, Proceedings of the 12th IASTED International Conference on Applied Simulation and Modelling, 2003, pp. 85–90.

[7] A. Jiménez, S. Ríos-Insua, A. Mateos, A generic multi-attribute analysis system, Computers and Operations Research (2004) (to appear).

[8] R.L. Keeney, H. Raiffa, Decision with Multiple Objectives: Preferences and Value-Tradeoffs, Wiley, New York, 1976.

[9] C.W. Kirkwood, Strategic Decision Making. Multiobjective Decision Analysis with Spreadsheets, Duxbury Press, Belmont, 1997.

[10] A. Mateos, A. Jiménez, S. Ríos-Insua, Modelling individual and global comparisons for multi-attribute preferences, Journal of Multicriteria Decision Analysis 13 (2003) 1–14.

[11] A. Mateos, A. Jiménez, S. Ríos-Insua, Solving dominance and potential optimality in imprecise multi-attribute additive models, Reliability Engineering and System Safety 79 (2) (2003) 253–262.

[12] H. Raiffa, The Art and Science of Negotiation, Harvard University Press, Cambridge, Mass., 1982

[13] S. Ríos, S. Ríos-Insua, D. Ríos Insua, J.G. Pachon, Experiments in robust decision making, in: S. Ríos (Ed.), Decision Theory and Decision Analysis: Trends and Challenges, Kluwer, Boston, 1994, pp. 233–242.

[14] D. Ríos Insua, Sensitivity Analysis in Multiobjective Decision Making, Springer, Berlin, 1990 LNEMS 347.

[15] D. Ríos Insua, S. French, A framework for sensitivity analysis in discrete multi-objective decision-making, European Journal of Operational Research 54 (1991) 176–190.

[16] S. Ríos-Insua, A. Jiménez, A. Mateos, Sensitivity analysis in a generic multi-attribute decision support system, in: K.J. Engemann, G.E. Lasker (Eds.), Advances in Decision Technology and Intelligent Information Systems, The International Institute for Advanced Studies in Systems Research and Cybernetics, Ontario, 2003, pp. 31–35.

[17] S. Ríos-Insua, A. Jiménez, A. Mateos, T. Prieto, A multiattribute decision support system with imprecise input and time-dependen modelling, International Journal of Technology, Policy and Management 3 (3) (2003) 230–250.

[18] T.J. Stewart, Robustness of additive value function method in MCDM, Journal of Multi-Criteria Decision Analysis 5 (1996) 301–309.

[19] R. von Nitzsch, M. Weber, Utility function assessment on a micro-computer: an interactive procedure, Annals of Operation Research 16 (1998) 149–160.

[20] M. Weber, Decision making with incomplete information, European Journal of Operational Research 28 (1987) 44–57.

[21] V.A. Zeithaml, L.L. Berry, A. Parasuraman, Delivering Quality Service: Balancing Customer Expectations and Perceptions, Free Press, Detroit, 1990.

![](/api/attachments/AZ4C7ZE5/fulltext/images/ef8de51e883ad19973543a05af50a26b10d1ad771bc9c60448909fccae50a711.jpg)  
Antonio Jiménez Martín obtained a Comput ing Science degree from Madrid Technical University. He is currently an Associate Professor of Operations Research and Simulation at School of Computer Science. His research interest is decision analysis and is involved in the development and implementation of decision support systems based on multi-attribute utility theory. His research has appeared mainly in Computers and Operations Research. DSS. EJOR. J. ofMulticriteria

Decision Analysis, GDN, JORS, Ecological Modelling, … and has coauthored three books.

![](/api/attachments/AZ4C7ZE5/fulltext/images/63aa83236256b2df73182af63fd38636c8b734264254101e158013956e3382d2.jpg)

Alfonso Mateos Caballero is an Associate Professor of Statistics and Operations Research at School of Computer Science (Madrid Technical University). His research interest is decision analysis and is currently involved in the development intelligent decision support systems based on influence diagrams and multi-attribute utility theory with applications to environment, medicine and e-democracy. His articles have appeared in various academic journals including:

Decision Support Systems, European Journal of Operational Research, J. Opl Res. Soc., Annals of Operations Research, Computational Optimization and Applications, OPSEARCH, JORS, Ecological Modelling, GDN and Journal of Multicriteria Decision Analysis.

![](/api/attachments/AZ4C7ZE5/fulltext/images/1028bb515ab55181786876ae8aebdd611698e3a40ca6e39dc3dc7dfb445a5d6a.jpg)

Sixto Ríos-Insua is a Professor of Statistics and Operations Research at Madrid Technical University. His research interest is decision analysis and is at present involved in the development intelligent decision support systems based on influence diagrams and multiattribute utility theory with applications to environment and medicine. His articles have appeared in various academic journals including: Computers and Operations Research, Theory and Decision, EJOR, JORS, Annals

of Operations Research, Computational Optimization and Applications, OPSEARCH and J. of Multicriteria Decision Analysis.

![](/api/attachments/AZ4C7ZE5/fulltext/images/24c0f7c9a62be1c82727260c749704c151f53ba291906d6042bc34133ccc6c84.jpg)

Luis Carlos Rodríguez obtained a Computing Science degree from Valencia Technical University (UNITEC). He is currently a Senior Manager in Supply Chain Services Line in Accenture with extensive experience in procurement strategies and procurement transformation programs. Luis Carlos recently led several procurement transformation programs in the natural gas, automotive and transportation industries. Focused on sourcing strategies and procurement processes, the

programs produced substantial savings. His research interest is decision analysis and is involved in the development and implementation of decision support systems based on multi-attribute utility theory.
