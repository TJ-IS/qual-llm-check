---
otero_id: 28530
otero_key: "QZSRGDDW"
title: "Single-Sourcing vs. Multisourcing: An Empirical Analysis of Large Information Technology Outsourcing Arrangements"
authors: "Ravi Bapna; Alok Gupta; Gautam Ray; Shweta Singh"
year: "2023"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.1170"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Single-Sourcing vs. Multisourcing: An Empirical Analysis of Large Information Technology Outsourcing Arrangements

Ravi Bapna,<sup>a</sup> Alok Gupta,<sup>a</sup> Gautam Ray,<sup>a</sup> Shweta Singh<sup>b,</sup>\*

<sup>a</sup> Information and Decision Sciences Department, Carlson School of Management, University of Minnesota, South Minneapolis, Minnesota 55455; <sup>b</sup> Information Systems and Management Department, Warwick Business School, University of Warwick, Coventry CV4 7AL, United Kingdom \*Corresponding author

Contact: rbapna@umn.edu, https://orcid.org/0000-0002-5251-7218 (RB); alok@umn.edu, https://orcid.org/0000-0002-2097-1643 (AG); gautamr@umn.edu, https://orcid.org/0000-0001-8567-5952 (GR); shweta.singh@wbs.ac.uk, https://orcid.org/0000-0002-5024-3444 (SS)

Received: Revised: July 1, Accepted: <sup>August 17, 2022</sup>Published Online in Articles in Advance: November 4. 2022

https://doi.org/10.1287/isre.2022.1170

Copyright:

Abstract. As the information technology (IT) services landscape matures, clients are increasingly adopting multisourcing arrangements that involve multiple vendors. Although a large body of information systems (IS) literature addresses issues of whether to outsource (to a single vendor), what types of contracts to use, and how to achieve optimal relational governance, little is known about the antecedents and consequents of the single versus mul tisourcing decision. Moreover, while conceptual and analytical models of single-sourcing versus multisourcing have been developed, there is no empirical IS research using a largescale data set with rigorous econometric analysis that examines the antecedents and consequents of multisourcing in the IT context. This paper <sup>fi</sup>lls this void, using the transaction cost economic lens and a data set of 49,057 large IT outsourcing arrangements that spans multiple industries and dates back 25 years. We <sup>fi</sup>nd that there is a curvilinear relationship between number of IT services in an IT outsourcing arrangement and the likelihood of multisourcing. This relationship increases as the number of IT services increases to up to <sup>fi</sup>ve services and then decreases. For managers who plan to multisource IT outsourcing arrangements, this research provides guidance to minimize exchange hazards through a better understanding of the relationship between sourcing choice, client IT outsourcing capabilities, the competitiveness of the vendor landscape, and the number of IT services in an IT outsourcing arrangement. We provide empirical evidence that the choice between single-sourcing and multisourcing is material to the performance of outsourcing contracts as an incorrect sourcing choice is likely to result in negative contract outcomes.

History: Paul A. Pavlou, Senior Editor; Ning Su, Associate Editor.

Keywords: IT outsourcing single-sourcing multisourcing sourcing choice misalignment dynamic panel model XGBoost

## 1. Introduction

A large body of research in the information technology (IT) outsourcing area (Dibbern et al. 2004, Oshri et al. 2015, Kotlarsky et al. 2018) examines questions such as when and what IT services work clients outsource (Loh and Venkatraman 1992a; 1992b; Lacity and Hirschheim 1993; Grover and Teng 1993); how to contract for outsourcing (Koh et al. 2004, Aron et al. 2008, Gopal and Koka 2010, Susarla et al. 2010, Han et al. 2011, Susarla 2012); and how to manage the client-vendor relationship (Sabherwal 1999; Choudhury and Sabherwal 2003; Kishore et al. 2003; Kirsch 2004; Levina 2005; Levina and Vaast 2005; 2008; Bandopadhyay and Pathak 2007; Sia et al. 2008; Gopal and Gao 2009; Mani et al. 2012; Vaidyanathan et al. 2012; Su et al. 2016). However, this body of research largely focuses on the dyadic client-vendor relationships where a client outsources to just one IT vendor, commonly referred to as single-sourcing. Increasingly, clients are entering into IT outsourcing arrangements with not just one vendor but instead with a multitude of vendors (Cohen and Young 2006, Bapna et al. 2010, Karamouzis 2011, Anderson and Parker 2013, Bala et al. 2014, Mishra et al. 2015, Oshri et al. 2019), which is commonly referred to as multisourcing.

Though academic research on IT outsourcing has largely focused on single-sourcing, the trend toward multisourcing is not surprising. As prior research suggests (e.g., Levina and Ross 2003), clients outsource IT work to take advantage of economy of scale and spe cialization of IT vendors. As the size and complexity of outsourced IT work increases and involves different IT services (e.g., application management, network management, systems integration, data center outsourcing, desktop outsourcing, IT help desk, etc.), it is likely that one IT vendor does not possess the economy of scale and specialization in all of the different services involved in an outsourced arrangement. Thus, multisourcing provides the bene<sup>fi</sup>ts of best-of-breed vendors and facilitates exploratory learning (Koo et al. 2017). In this way, when an IT outsourcing deal involves more IT services, clients may involve multiple vendors in the arrangement (Bapna et al. 2010, 2013a; Anderson and Parker 2013; Bhattacharya et al. 2018).

Involving multiple vendors in an IT outsourcing arrangement may increase competition between vendors and mitigate operational and strategic risks (Richardson 1993, Lacity and Willcocks 1998, Aron et al. 2005, Levina and Su 2008, Aubert et al. 2016). For example, involving multiple vendors may reduce vendor lock-in and holdup costs. When these vendors are distributed globally, there is also the potential to reduce labor costs and increase ef<sup>fi</sup>ciency by executing the work around the clock (Gokpinar et al. 2013). However, involving multiple vendors in one IT outsourcing arrangement reduces a vendor’s incentive to make client-speci<sup>fi</sup>c investments and requires clients to develop capabilities for monitoring and coordinating multiple vendors and integrating their deliverables (Bakos and Brynjolfsson 1993, Clemons et al. 1993, Levina and Su 2008, Anderson and Parker 2013, Tripathy and Eppinger 2013, Bala et al. 2014, Hao et al. 2016, Mishra and Sinha 2016). Nevertheless, if a client has IT outsourcing capabilities—if it can specify requirement speci<sup>fi</sup>cations and performance goals to be met by different vendors and monitor, coordinate, and integrate the deliverables from different vendors (Bapna et al. 2013a, Mishra and Sinha 2016, Oshri et al. 2019)— then a client can take advantage of specialization in the IT industry by using multiple vendors and itself act as the chief integrator.

The ability and opportunities to multisource in this way are contingent on the availability and presence of different vendors with distinctive capabilities. Hence, the number of services in an IT outsourcing arrangement, the IT outsourcing capabilities of the client, and the availability of distinctive vendors with required capabilities are likely to determine the optimal sourcing choice. The question of whether to outsource or not is often examined using the transaction cost framework as a trade-off between the exchange hazards faced in terms of the monitoring, coordination, and integration cost incurred by the client versus the bene-<sup>fi</sup>ts from the scale and specialization of the market vendor (Loh and Venkatraman 1992a, Ang and Straub 1998). However, how the transaction cost perspective extends to the single-sourcing versus multisourcing decision has not been studied in prior research. In this research, we extend the transaction cost perspective and position the choice between single-sourcing and multisourcing as an examination of the interplay between the client’s IT outsourcing capabilities to manage the exchange hazards and the availability of specialized capabilities in the market as the number of services in an IT outsourcing arrangement increases.

Using a data set of 49,057 large IT outsourcing arrangements (average size of about \$58 million) from

1989–2014 through <sup>fi</sup>xed effect panel logit and dynamic panel logit models, we present four key <sup>fi</sup>ndings. First, we <sup>fi</sup>nd that as the number of services in an IT outsourcing arrangement increases up to about <sup>fi</sup>ve, the likelihood of multisourcing increases; however, beyond <sup>fi</sup>ve IT services, the increased coordination costs exceed the bene<sup>fi</sup>ts of specialization and single-sourcing is again the preferred alternative. Second, if the client develops IT outsourcing capabilities, the client has a broader range of sourcing choices available to outsource IT work, as the coordination and integration capabilities of the client open opportunities to take advantage of the economy of specialization and multisource vendors. Third, we <sup>fi</sup>nd that an increase in vendor specialization and competition increases the probability of <sup>fi</sup>nding specialty vendors for different services, which enhances the opportunity to multisource. Finally, we test our multisourcing theory using 1,588 contracts with known contract outcomes and <sup>fi</sup>nd that misalignment in sourcing choice leads to contract failure. This test provides evidence that the single versus multisourcing choice is important for the success of the IT outsourcing contract and that a suboptimal sourcing choice can result in contract cancellation or renegotiation.

The theoretical contribution of the study is to extend the transaction cost framework used to make the insourcing versus outsourcing decision to the singlesourcing versus multisourcing decision. We <sup>fi</sup>nd that as the number of different services in an IT outsourcing arrangement increases up to a point, as a client’s IT outsourcing capability to manage exchange hazards increases, and when competition/capabilities in the IT services market increases, the likelihood of multisourcing increases compared with single-sourcing.

The remainder of the paper is organized as follows: The second section situates the paper in the context of the IT outsourcing literature. Section 3 details the theory and hypothesis development for the antecedents and consequences of sourcing choice; Section 4 describes the data and variables; Section 5 describes the empirical approaches and presents the econometric models and results; Section 6 discusses the robustness tests; Section 7 examines the implications of the <sup>fi</sup>ndings.

## 2. Literature Review

We use the framework from Kotlarsky et al. (2018) to highlight how this work is positioned in the overall landscape of information systems (IS) research in the IT outsourcing area. Table 1 summarizes the body of IS literature and pinpoints a critical gap in the understanding of the antecedents and consequents of multisourcing, which we <sup>fi</sup>ll with this paper. As evident from Table 1, the vast majority of the IS literature has focused on the insourcing versus outsourcing decision and has covered topics ranging from making the sourcing choice (Loh and Venkatraman 1992b, Slaughter and Ang 1996, Ang and Straub 1998, Lee et al. 2004) to designing the outsourcing contracts (Walden 2005, Gopal and Konduru 2008, Dey et al. 2010, Fitoussi and Gurbaxani 2012) and managing the outsourcing relationship (Sabherwal 1999, Choudhury and Sabherwal 2003, Koh et al. 2004, Levina and Vaast 2008). We further nuance the differences across various key papers in each section by focusing on their key research question, theoretical perspective, and methodology used. The IS literature focusing on single-sourcing versus multisourcing is sparse, and most of it falls under managing the outsourcing relationship (Levina and Su 2008, Wiener and Saunders 2014, Aubert et al. 2016, Plugge and Bouwman 2018, Lioliou et al. 2019). All of these are in-depth case studies that focus on the question of how to manage multisourcing arrangements. We argue that prior to managing a relationship, there is the question of selecting the right type of outsourcing relationship. That issue is the focus of this paper.

Table 1. Literature Review

<table><tr><td colspan="4">Insourcing vs. outsourcing</td><td colspan="4">Single-sourcing vs. multisourcing</td></tr><tr><td colspan="4">Making the sourcing decision</td><td colspan="4">Making the sourcing decision</td></tr><tr><td>Research question</td><td>Theoretical perspective</td><td>Methodology</td><td>Key authors</td><td>Research question</td><td>Theoretical perspective</td><td>Methodology</td><td>Key authors</td></tr><tr><td>Why to outsource and the determinants of outsourcing</td><td>Innovation diffusion</td><td>Empirical (data on large U.S. firms)</td><td>Loh and Venkatraman (1992b)</td><td>Why hospitals are trending toward single-sourcing and find the organizational level antecedents that impact the rate of this trend</td><td>Institutional theory</td><td>Empirical (data on U.S. hospitals)</td><td>Angst et al. (2017)</td></tr><tr><td>Determinants of insource versus outsource choice</td><td>Labor economics</td><td>Empirical (data on IS job ads)</td><td>Slaughter and Ang (1996)</td><td>Client's optimal sourcing strategy</td><td>Game theory</td><td>Mathematical modelling (principal agent framework: simultaneous move game)</td><td>Bhattacharya et al. (2018)</td></tr><tr><td>How to make the sourcing choice (economic determinants)</td><td>Transaction cost economics</td><td>Empirical (survey &amp; archived data)</td><td>Ang and Straub (1998)</td><td>How the number of services in an arrangement, client's IT outsourcing capabilities and the availability of distinctive vendor capabilities interact to influence client's single-sourcing versus multisourcing choice</td><td>Transaction cost economics</td><td>Empirical (data on large IT outsourcing arrangements)</td><td>Current paper</td></tr><tr><td>Configurational approach to understand impact of sourcing strategy on its success</td><td>Residual rights theory</td><td>Empirical (survey data)</td><td>Lee et al. (2004)</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="4">Insourcing vs. outsourcing</td><td colspan="4">Single-sourcing vs. multisourcing</td></tr><tr><td colspan="4">Designing the outsourcing contract</td><td colspan="4">Designing the outsourcing contract</td></tr><tr><td>Research question</td><td>Theoretical perspective</td><td>Methodology</td><td>Key authors</td><td>Research question</td><td>Theoretical perspective</td><td>Methodology</td><td>Key authors</td></tr><tr><td>Intellectual property rights division (for software created) between client and vendor</td><td>Transaction cost economics and property rights</td><td>Analytical modelling</td><td>Walden (2005)</td><td>Forced coopetition as risk sharing mechanism in contract design</td><td>Strategic management coopetition theory</td><td>Qualitative case study</td><td>Wiener and Saunders (2014)</td></tr><tr><td colspan="4">Designing the outsourcing contract</td><td colspan="4">Designing the outsourcing contract</td></tr><tr><td>Research question</td><td>Theoretical perspective</td><td>Methodology</td><td>Key authors</td><td>Research question</td><td>Theoretical perspective</td><td>Methodology</td><td>Key authors</td></tr><tr><td>Choice between fixed price and time &amp; material contracts (role of various profit drivers)</td><td>Transaction cost economics</td><td>Empirical (data on offshore projects)</td><td>Gopal and Konduru (2008)</td><td></td><td></td><td></td><td></td></tr><tr><td>Performance comparison of various contract types (fixed price &amp; time and material)</td><td>Contract theory</td><td>Analytical modelling</td><td>Dey et al. (2010)</td><td></td><td></td><td></td><td></td></tr><tr><td>Contract design and its performance measurement in IT outsourcing</td><td>Contract theory</td><td>Empirical (data on outsourcing contracts)</td><td>Fitoussi and Gurbaxani (2012)</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="4">Insourcing vs. outsourcing</td><td colspan="4">Single-sourcing vs. multisourcing</td></tr><tr><td colspan="4">Managing the outsourcing relationship</td><td colspan="4">Managing the outsourcing relationship</td></tr><tr><td>Research question</td><td>Theoretical perspective</td><td>Methodology</td><td>Key authors</td><td>Research question</td><td>Theoretical perspective</td><td>Methodology</td><td>Key authors</td></tr><tr><td>Role of trust in outsourced IS projects and ways to build trust between clients and vendors</td><td>Organizational trust theory</td><td>Qualitative case study</td><td>Sabherwal (1999)</td><td>Theoretical framework for multivendor management in sourcing</td><td>Organizational process and change theory</td><td>Qualitative case study</td><td>Levina and Su (2008)</td></tr><tr><td>Mechanisms to design portfolio of controls in outsourced IS projects</td><td>Organizational control theory and agency theory</td><td>Qualitative case study</td><td>Choudhury and Sabherwal (2003)</td><td>Foster and manage competition &amp; cooperation in multisourcing</td><td>Strategic management coopetition theory</td><td>Qualitative case study</td><td>Wiener and Saunders (2014)</td></tr><tr><td>Managing outsourcing relationship through phycological contracting</td><td>Phycological contracting theory</td><td>Sequential qualitative and quantitative field study</td><td>Koh et al. (2004)</td><td>To understand knowledge sharing in multisourcing between clients and vendors and design ways to remove barriers</td><td>Resource-based view</td><td>Qualitative case study</td><td>Plugge and Bouwman (2018)</td></tr><tr><td>How to establish collaborative practices in offshored projects</td><td>Practice theory</td><td>Qualitative case study</td><td>Levina and Vaast (2008)</td><td>Understand opportunistic vendor behavior and facilitate coopetition among vendors in multisourcing</td><td>Coopetition theory and transaction cost economics</td><td>Qualitative case study</td><td>Lioliou et al. (2019)</td></tr></table>

Su and Levina (2011) argue that although multisourcing is a new area of research in IT outsourcing, it has been extensively studied in manufacturing; thus, there emerges a need to map and integrate existing knowledge from manufacturing to IT outsourcing; for instance, the automotive industry has also seen a move toward managing multiple vendor relationships (Ahmadjian and Lincoln 2001). This governance form facilitates faster knowledge sharing within the organization via vendors’ knowledge-sharing networks, leading to increased <sup>fi</sup>rm pro<sup>fi</sup>t (Dyer and Hatch 2004). Along the same lines, Japanese automakers use a hybrid organizational form called parallel sourcing to achieve high vendor performance while still preserving the relationship and commitment bene<sup>fi</sup>ts of single-sourcing (Richardson 1993).

Our work relates to the operations management literature that has examined the single-sourcing versus multisourcing issue from a supply chain risk-management perspective (Tomlin and Yimin 2005, Narasimhan and Talluri 2009, Wang et al. 2010, Aydin et al. 2011, Yang et al. 2012, Pournader et al. 2020). This literature focuses on understanding which vendors to choose, selecting the optimal number of vendors, and understanding how to divide IT-enabled services among multiple vendors (Anupindi and Akella 1993, Dada et al. 2007, Federgruen and Yang 2008, Hu and Kostamis 2015, Ang et al. 2017, Bimpikis et al. 2019); however, the primary methodology employed in this literature is analytical modeling, and there is a dearth of empirical analyses studying the antecedents and outcomes of multisourcing.

We position the current research paper in the area of making the single-sourcing versus multisourcing IT outsourcing decision. Extant research in this area is limited to Bhattacharya et al. (2018), who use analytical modelling and a game theoretic approach to <sup>fi</sup>nd a client’s optimal sourcing strategy; Angst et al. (2017), who use institutional theory and data on U.S. hospitals to study why hospitals are trending toward singlesourcing; and Handley et al. (2022), who use a knowledge-based framework to understand the trend toward IT multisourcing.

We address the single-sourcing versus multisourcing question using an extensive multi-industry data set on large IT outsourcing arrangements to examine how the number of services in an IT outsourcing deal, a client’s IT outsourcing capabilities to manage exchange hazards, and the availability of distinctive vendor capabilities interact to in<sup>fl</sup>uence the single-sourcing versus multisourcing choice. Further, we extend our analysis to also examine the consequences of an incorrect sourcing choice. By providing data-driven insights into both the antecedents and consequents of the multisourcing (or not) decision, we <sup>fi</sup>ll a signi<sup>fi</sup>cant gap in the information technology outsourcing literature, as identi<sup>fi</sup>ed in Table 1.

## 3. Theory And Hypothesis Development

The insourcing versus outsourcing decision in IT sourcing is often examined using a transaction cost framework (Loh and Venkatraman 1992a, Ang and Straub 1998, Whitten and Leidner 2006, Aral et al. 2018). IT vendors typically have the advantage of economy of scale and specialization; however, clients incur lower monitoring, coordination, and integration costs for insourced IT compared with when the work is outsourced. The coordination costs when working with external vendors stem from exchange hazards (Williamson 1985, Nickerson and Silverman 2003), in particular, the key transaction characteristics of asset speci<sup>fi</sup>city, uncertainty, and frequency (Williamson 1979, Poppo and Zenger 2002). Further, asset speci<sup>fi</sup>city creates lock-in and motivates <sup>fi</sup>rms to develop longterm relationships with fewer vendors (Kishore et al. 2003, Su et al. 2016, Aral et al. 2018). Transaction cost economics (TCE) recommend that arrangements that are highly asset speci<sup>fi</sup>c, involve high uncertainty, and occur frequently are more suitable to insource (Sia et al. 2008), which means that, in the TCE-based literature, as exchange hazards increase, <sup>fi</sup>rms are more likely to insource compared with outsourcing; but as the capability to manage exchange hazards increases, <sup>fi</sup>rms outsource. In other words, if the vendors’ economy of scale and specialization advantage dominates, out sourcing is chosen. On the other hand, if exchange hazards increase the cost of monitoring, coordination, and integration of work of external vendors beyond the bene<sup>fi</sup>ts of the vendor’s scale and specialization, in sourcing is preferred. In this paper, we extend the traditional insource versus outsource trade-off to the single-source versus multisource trade-off and show that as the capability to manage exchange hazards increases, clients are more likely to multisource in comparison with single-sourcing.

## 3.1. Antecedents of Sourcing Choice

Relative to multisourcing, single-sourcing has the economy of scale and integration advantage. If the client outsources IT services to one vendor, the vendor can offer an integrated solution. Similarly, the client’s cost of monitoring and coordination is lower when it needs to monitor and coordinate with one vendor. On the other hand, multisourcing has the advantage of economics of specialization (Koo et al. 2017); if the client chooses a specialist for each separate service in an IT outsourcing arrangement, the client receives the bene<sup>fi</sup>t of economy of specialization but incurs a higher monitoring, coordination, and integration cost (Anderson and Parker 2013). This cost is even higher when the client chooses vendors across different time zones and from different cultural backgrounds (Bala et al. 2014, Hao et al. 2016). Thus, the choice between single-sourcing and multisourcing is a trade-off between the economy of scale and integration of single-sourcing with the economy of specialization of multisourcing (Koo et al. 2017).

The difference between single-sourcing and multisourcing can be described in this way: a generalist IT vendor has a lower average cost across a set of IT services compared with a client or a specialist IT vendor. A vendor that offers services across different areas/ domains can grow in scale, realizing economies of scale through economies of scope. Such a vendor can offer clients bene<sup>fi</sup>ts of economies of scale and integration. However, a specialist IT vendor has a lower average cost for a speci<sup>fi</sup>c IT service compared with the client and the generalist IT vendor. A vendor that focuses in just one area of IT service can also achieve economies of scale through specialization.

## 3.2. The Number of Services in an IT Outsourcing Arrangement and Sourcing Choice

As IT outsourcing arrangements become larger, they are more likely to include services that require distinct capabilities that no one vendor is likely to have. As global supply markets with different specialization and cost advantages emerge, different outsourcing strategies become available (Levina and Su 2008, Anderson and Parker 2013, Mishra and Sinha 2016, Oshri et al. 2019), so a client is more likely to consider multisourcing for an IT outsourcing arrangement with many different services because the economics of specialization are likely to dominate the economy of scale and integration advantage of single-sourcing. Thus, an IT outsourcing arrangement that includes different services is more likely to be multisourced rather than single-sourced.

For a client to be able to involve multiple vendors in an IT outsourcing arrangement, the client needs to de<sup>fi</sup>ne the different IT services that can be awarded to different specialist vendors (Bhattacharya et al. 2018). Delineating the different services in a large IT outsourcing arrangement that can be executed by different vendors also reduces exposure to and reliance on any one vendor and consequently reduces risks attributable to opportunistic behavior, such as shirking (deliberate underperformance), opportunistic renegotiation, and vendor lock-in (Aron et al. 2005, Aubert et al. 2016). Therefore, if an IT outsourcing arrangement includes distinct services, then the client can bene<sup>fi</sup>t from different vendors’ specialization (Bapna et al. 2010).

On the other hand, as the number of distinct services in an IT outsourcing arrangement increases, if there is a commensurate increase in the number of vendors, the cost of monitoring, coordinating, and integrating the work of different vendors also increases exponentially (Bakos and Brynjolfsson 1993, Clemons et al. 1993, Anderson and Parker 2013, Bala et al. 2014, Hao et al. 2016, Mishra and Sinha 2016). Though there are bene<sup>fi</sup>ts from specialization, beyond a certain number of services/vendors, the cost of monitoring, coordination, and integration is likely to outweigh the bene<sup>fi</sup>ts of specialization, making single-sourcing the preferred sourcing choice (Bakos and Brynjolfsson 1993, Clem ons et al. 1993, Bhattacharya et al. 2018). Thus, a client is likely to choose single-sourcing for an IT outsourcing arrangement with a very small or very large number of services and choose multisourcing for IT outsourcing arrangements with an intermediate number of services. This leads to the following hypothesis.

Hypothesis 1. As the number of services in an IT out sourcing arrangement increases, the likelihood of multisourcing first increases and then decreases.

## 3.3. Client IT Outsourcing Capabilities and Sourcing Choice

Client IT outsourcing capabilities refer to a client’s understanding of the vendor landscape and expertise, experience in requirements de<sup>fi</sup>nition and performance measurement, and intervendor monitoring and coordination. Aubert et al. (2016) discuss how a client with signi<sup>fi</sup>cant IT outsourcing capabilities can get vendors with overlapping expertise and capabilities to collaborate by using clear separation of requirement de<sup>fi</sup>nition and responsibility. Similarly, Wiener and Saunders (2014) describe how clients with signi<sup>fi</sup>cant IT outsourcing capabilities can get multiple vendors to coop erate and compete at the same time. Consequently, a client with signi<sup>fi</sup>cant IT outsourcing capabilities may be able to choose the multisourcing approach to source a large IT outsourcing deal. In contrast, a client without signi<sup>fi</sup>cant IT outsourcing capabilities in choosing specialist vendors, de<sup>fi</sup>ning distinct IT services, and specifying requirements and performance measures will face signi<sup>fi</sup>cant exchange hazards and struggle to manage and coordinate multiple vendors (Lioliou et al. 2019). The value of IT outsourcing capabilities increases with the number of services in an IT outsourcing deal because the economy of specialization advantage of multisourcing is likely to be higher for IT outsourcing arrangements with more services. When an IT outsourcing arrangement includes distinct IT services with clearly speci<sup>fi</sup>ed requirements and performance goals, it requires less information coordination to achieve integration, as de<sup>fi</sup>ning distinct services reduces a client’s coordination and integration costs and facilitates multisourcing (Langlois 2002, Tiwana 2008, Cabigiosu and Camuffo 2012). Therefore, we hypothesize that

Hypothesis 2. A client with higher levels of IT outsourcing capabilities is more likely to be associated with multisourcing.

## 3.4. Industry Characteristics and Sourcing Choice

For a client to be able to take advantage of economies of specialization, there must be enough specialist IT vendors. IT vendors develop different capabilities by learning by doing (Zollo and Winter 2002, Li et al. 2010). These capabilities include marketing capability to understand customer needs, research and development (R&D) capability to develop products and services that meet customer needs, and operations capability to make ef<sup>fi</sup>cient and effective use of resources required to maintain viability and achieve growth (Zollo and Winter 2002, Li et al. 2010). As more IT vendors develop different capabilities, competition in the IT outsourcing industry increases. As competition in the IT outsourcing industry increases, clients can <sup>fi</sup>nd specialist providers who may meet the speci<sup>fi</sup>c needs of their distinct services more ef<sup>fi</sup>ciently than a generalist vendor, although a multisourcing agreement may include a combination of generalist and specialist vendors. Therefore, as the competition in the IT outsourcing industry increases, one expects to see an increase in multisourcing.

From an IT-vendor perspective, when the cost advantage of being a specialist vendor outweighs the economy of scale and integration advantage of being a generalist IT vendor, one expects to see entry and growth of specialist IT vendors. In aggregate, as more IT vendors with specialized IT capabilities establish themselves in the increasingly global IT industry, competition in the IT industry increases; it is natural to expect that this competition will also increase the likelihood of multisourcing. Thus, we hypothesize the following:

Hypothesis 3. Multisourcing is likely to increase with competition in the IT industry.

## 3.5. Effect of Sourcing Choice on Contract Outcome

Despite the popularity of IT outsourcing as a business strategy, <sup>fi</sup>rms fail to achieve successful performance outcomes from IT outsourcing (Narayanan et al. 2011, Brown and Fersht 2014). TCE recognizes coordination costs attributable to exchange hazards such as asset speci<sup>fi</sup>city and uncertainty as a driver of inferior outsourcing performance (Williamson 1985, Nickerson and Silverman 2003). To avoid suboptimal outcomes, <sup>fi</sup>rms outsource IT when vendors have economy of scale and specialization and coordination costs are low and clients insource IT work when coordination costs with vendors are higher than the vendors’ scale and specialization advantages. Deviation from this prescribed decision mode is referred to as sourcing misalignment, and such misalignment leads to inferior performance outcomes (Leiblein et al. 2002, Handley 2017). Although some <sup>fi</sup>rms fail to make the appropriate sourcing decision in the <sup>fi</sup>rst place (as <sup>fi</sup>rms differ in their ability to address sourcing challenges arising from exchange hazards), others experience sourcing misalignment over time based on the dynamic nature of the <sup>fi</sup>rm capabilities, cost structures, etc. (Handley 2017).

Industry reports suggest that <sup>fi</sup>rms experience value leakage of 17%–40% of their annual contract value over the life of the contract because of sourcing misalignment (Nyden and Kane 2019). Similarly, other industry reports indicate that 64% of <sup>fi</sup>rms bring outsourcing jobs back home after sourcing misalignment (Deloitte Consulting 2005). A few empirical studies have also examined the relationship between the degree of sourcing misalignment and performance outcomes. Argyres and Bigelow (2007) study the U.S. auto industry; Leiblein et al. (2002) study semiconductor manufacturing; Nickerson and Silverman (2003) study the U.S. trucking industry; Sampson (2004) studies R&D alliances in the telecommunication equipment industry. In the IT domain, Susarla and Barua (2011) examine application service providers (ASPs) and show that contract misalignment between clients and ASPs lowers the survival probability of providers in the ASP market. Similarly, Handley (2017) studies manufacturing and logistics/supply chain process outsourcing and shows that sourcing misalignment leads to inferior outsourcing performance.

Prior research suggests principles for optimal (i.e., in-house versus outsourced) sourcing choice and indicates that suboptimal outcomes occur when deviation or misalignment from optimal sourcing choice occurs.

In this study, we propose sourcing misalignment as a deviation from optimal single-source versus multisource choice and contend that sourcing misalignment will lead to a negative contract outcome. Speci<sup>fi</sup>cally, using single-sourcing when multisourcing is the optimal sourcing choice may lead to a negative contract outcome. For example, using a generalist vendor to perform a set of specialized IT services may have performance implications if the chosen generalist vendor lacks the capabilities to ef<sup>fi</sup>ciently perform all the distinct services involved in the IT outsourcing arrangement. In this case, although single-sourcing may save on coordination costs (Aubert et al. 2016), the chosen IT vendor’s inability to ef<sup>fi</sup>ciently execute all the different services in the IT outsourcing arrangement may increase holdup costs (Aubert et al. 2016) and miss opportunities for exploratory learning (Koo et al. 2017).

Similarly, using multisourcing when single-sourcing is the optimal sourcing choice may have a negative contract outcome. For example, using multiple best-of-breed vendors without the ability to monitor, coordinate, and integrate their work may exacerbate moral hazard problems (Anderson and Parker 2013, Bala et al. 2014, Hao et al. 2016, Mishra and Sinha 2016, Bhattacharya et al. 2018). Lioliou et al. (2019) detail how the inability to specify requirements and outcome measures, as well as overdependence on informal monitoring among selfinterested parties in a multisourced arrangement, led to negative outcomes. Thus, we expect sourcing misalignment (i.e., a deviation from optimal single-source versus multisource sourcing choice) to be negatively associated with contract outcome.

Hypothesis 4. Sourcing misalignment with respect to the sourcing choice is likely to be negatively associated with contract outcome.

## 4. Data And Variables

We primarily rely on International Data Corporation’s (IDC) services contract database (SCD) for our data. The IDC database includes more than 49,000 large IT outsourcing arrangements signed from 1989–2014. Out of these, 44,558 were single-sourced and 4,499 were multisourced. We use two related data sets for the analysis. Data set I is used to evaluate the determinants of sourcing choice, that is, test Hypothesis 1–Hypothesis 3; Data set II is used to examine the effect of sourcing choice misalignment, that is, test Hypothesis 4.

## 4.1. Data Set I: Evaluating the Determinants of Sourcing Choice (Hypothesis 1, Hypothesis 2, and Hypothesis 3)

4.1.1. Dependent Variable. We measure Sourcing Choice as a binary variable. We distinguish between singlesourcing (when a client involves one vendor in an outsourcing arrangement, coded as zero) and multisourcing (when a client involves multiple vendors in an outsourc ing arrangement, coded as one).

4.1.2. Independent Variables. We examine the antecedents of the single-sourcing versus multisourcing choice. The IT outsourcing arrangement level antecedent considered includes the number of IT services in the deal. The number of services (NumberOfServices) is the number of distinct IT services (e.g., application man agement, network management, systems integration, data center outsourcing, desktop outsourcing, IT help desk, etc.) that are included in the outsourcing arrangement. The client-level antecedent is the client’s IT out sourcing capabilities associated with selecting vendors, contracting out IT work, de<sup>fi</sup>ning requirements, specifying performance goals, monitoring external vendors, and integrating the deliverables provided by different vendors. Client IT outsourcing capabilities (Customer-OutsourcingCapabilities) is assessed as the dollar value of all the IT outsourcing deals signed by the client before signing the current deal (Bapna et al. 2016, Mishra and Sinha 2016, Anderson et al. 2019). The industry-level antecedent is the level of competition in the IT outsourcing industry. It is expected that as the industry matures, more <sup>fi</sup>rms enter the industry, build specialized capabil ities, and compete for market share. Thus, as an industry matures, the number of <sup>fi</sup>rms in the industry increases and the market share of each <sup>fi</sup>rm decreases. We compute industry competition (Industry Competi tion) as one minus the Her<sup>fi</sup>ndahl index in a particular year. Thus, industry competition is given as $\begin{array} { r } { 1 - \sum _ { i = 1 } ^ { N } } \end{array}$ $\mathbf { \bar { \it V } } _ { i } { } ^ { 2 }$ , where $V _ { i }$ is the market share of vendor i and N is the number of vendors in a particular year. Industry competition increases with the number of vendors where each vendor has a smaller market share.

4.1.3. Control Variables. We control for the complexity of an outsourcing arrangement. Complexity arises in IT outsourcing arrangements that involve a number of parts that interact in a nondeterministic manner (Simon 1962). Application development, business con sulting, IT consulting, and systems integration deals require creation of new knowledge that involves a large number of parts and uncertainty in the interconnection between the means and ends (Susarla 2012). Thus, following Susarla (2012), we code EngagementTypeComplexity as a binary variable that takes a value of one for complex deals that include services such as application development, business consulting, IT consulting, and systems integration, etc. and a value of zero for simpler arrangements that include services such as learning and education, IT education and training, business outsourcing, deploy and support, contract labor and capacity engagement, and business support engagements, etc. We control for contract size using the dollar value of the contract (ContractValue) as its measure. We also control for client size, as larger <sup>fi</sup>rms may have more resources to single-source and act as the chief integrator. We use the annual revenue (CustomerRevenue) as a proxy for <sup>fi</sup>rm size. Also, based on the past relationship between client and vendor, it is expected that clients are more likely to single-source to vendors with whom they have worked in the past. We control for strength of past relationship between the client and the vendor (ExistingRelationshipStrength) and measure it as the count of the number of different contracts the vendor had held with the client before signing the current contract. It is also likely that certain IT services are more prone to certain sourcing strategies (Handley et al. 2022), so we use IT service dummies (such as application management, network management, systems integration, data center outsourcing, desktop outsourcing, hardware deploy and support, IT help desk, software deploy and support, hosted application management, network consulting and integration) as a control variable for that.

## 4.2. Data Set II: Evaluating the Effect of Sourcing Choice Misalignment (Hypothesis 4)

To examine the implications of sourcing choice misalignment, we identify 1,588 contracts with known contract outcomes from the SCD database. We measure contract outcome (Outcome) as a binary variable based on the contract status information provided in SCD. Following Bapna et al. (2016), a contract is coded as one if it was extended or expanded and zero if it was renegotiated or cancelled. The rationale is that if the vendor is meeting the client’s expectation, the contract is likely to be extended or expanded, which is a positive outcome for the client and the vendor. However, if a contract is not meeting the client’s expectations, the contract is likely to be cancelled or renegotiated, which may not be a positive outcome for the client or the vendor.<sup>1</sup>

4.2.1. Independent Variables. We compute the predicted sourcing choice from our theory of sourcing choice as de<sup>fi</sup>ned by Hypotheses 1–3. Mathematically, predicted sourcing choice is computed by estimating the predicted values from the <sup>fi</sup>xed effect model (Model 2 in Table 2). This is the ideal sourcing choice as predicted by the theory presented in the paper. Next, actual sourcing choice is what the client has chosen. We observe this variable as the actual choice the client has made using the SCD data. At this point, sourcing choice misalignment is computed as the absolute value of the difference between the predicted and the observed sourcing choice, following Susarla and Barua (2011).

$$
\text { Sourcing   Choice   Misalignment }
$$

$$
= \left| \text {   Predicted   Sourcing   Choice   } \right.
$$

$$
- \text { Actual   Sourcing   Choice } |
$$

4.2.2. Control Variables. Contract outcome is likely to depend on contract, client, and vendor characteristics. At the contract level, it is believed that larger contracts (ContractValue) with more services (NumberOfServices)

Table 2. Fixed Effect Logit Model for the Sourcing Choice Analysis

<table><tr><td>Variables</td><td>Model 1Sourcing choice</td><td>Model 2Sourcing choice</td></tr><tr><td>ContractValue</td><td>0.050***(0.136)</td><td>0.103**(0.006)</td></tr><tr><td>NumberOfServices</td><td>0.029***(0.022)</td><td>0.035***(0.133)</td></tr><tr><td>CustomerOutsourcingCapabilities</td><td>0.199***(0.267)</td><td>0.026**(0.177)</td></tr><tr><td>EngagementTypeComplexity</td><td>0.123(0.051)</td><td>0.191(0.083)</td></tr><tr><td>CustomerRevenue</td><td>0.045(0.028)</td><td>0.022(0.030)</td></tr><tr><td>Industry Competition</td><td>0.264***(0.186)</td><td>0.071***(0.093)</td></tr><tr><td>ExistingRelationshipStrength</td><td>-0.015*(0.008)</td><td>-0.090*(0.021)</td></tr><tr><td>NumberOfServices * NumberOfServices</td><td></td><td>-0.271***(0.173)</td></tr><tr><td>Customer fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>49,057</td><td>49,057</td></tr><tr><td>Number of unique customers</td><td>22,502</td><td>22,502</td></tr><tr><td></td><td> $\chi^2 = 129.32^{***} (7)$ </td><td> $\chi^2 = 136.61^{***}(8)$ </td></tr></table>

Note. Standard errors are in parentheses  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

Table 3. Summary Statistics and Correlations for the Sourcing Choice Analysis (49,057 Arrangements)

<table><tr><td>Variables</td><td>Mean</td><td>Std. dev.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>1. ContractValue ($ millions)</td><td>58.3</td><td>313M</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. NumberOfServices</td><td>1.352</td><td>0.934</td><td>0.31</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. CustomerOutsourcingCapabilities ($ billions)</td><td>1.67</td><td>8.54</td><td>0.35</td><td>0.01</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. EngagementTypeComplexity</td><td>0.433</td><td>0.495</td><td>-0.23</td><td>-0.32</td><td>-0.05</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>5. CustomerRevenue ($ billions)</td><td>17.1</td><td>251</td><td>0.27</td><td>0.06</td><td>0.24</td><td>0.18</td><td>1</td><td></td><td></td><td></td></tr><tr><td>6. Industry Competition</td><td>0.562</td><td>0.032</td><td>0.13</td><td>0.05</td><td>-0.17</td><td>-0.04</td><td>0.12</td><td>1</td><td></td><td></td></tr><tr><td>7. ExistingRelationshipStrength</td><td>1.38</td><td>1.34</td><td>0.15</td><td>0.09</td><td>0.31</td><td>0.05</td><td>0.11</td><td>0.09</td><td>1</td><td></td></tr><tr><td>8. Sourcing Choice</td><td>0.091</td><td>0.288</td><td>0.23</td><td>0.03</td><td>0.33</td><td>0.01</td><td>-0.06</td><td>0.17</td><td>0.04</td><td>1</td></tr></table>

Note. Std. dev., standard deviation.

that have higher complexity (EngagementTypeComplexity) are less likely to be successful. We also control for the strength of the client-vendor relationship prior to signing the contract (ExistingRelationshipStrength). A strong prior relationship between the client and the vendor may increase the likelihood of a successful contract outcome, as a prior relationship may mean a better understanding of the client’s requirements by the vendor and/or a better understanding of the vendors’ capabilities by the client. The nature of the contract (<sup>fi</sup>xed price or time and material) may also in<sup>fl</sup>uence contract outcomes, as a time-and-material contract may reduce risk for the vendor side and increase vendor commitment to achieve a positive contract outcome (Gopal and Konduru 2008, Gopal and Koka 2010). We use a dummy variable (FixedPriceY/N) to control for contract type.

Contract outcome is also likely to be in<sup>fl</sup>uenced by client characteristics. Larger clients (CustomerRevenue) with more resources may have a higher likelihood of contract success. Similarly, clients with signi<sup>fi</sup>cant IT outsourcing capabilities (CustomerOutsourcingCapabilities) may have developed routines to work in partnership with external vendors, and thus they are more likely to achieve positive contract outcomes.

The vendor’s capabilities may also in<sup>fl</sup>uence contract outcome. For example, vendors with signi<sup>fi</sup>cant experience may have developed capabilities from learning by doing that lead to higher contract success rates. The vendor’s outsourcing capabilities (VendorOutsourcing-Capabilities) is measured as the dollar value of all the IT contracts executed by the vendor before signing the contract under consideration.

Table 3 presents the summary statistics and the correlations between the dependent (sourcing choice), independent, and control variables for 49,057 IT out sourcing arrangements in Data set I, which is used to test Hypothesis 1–Hypothesis 3. Out of the 49,057 arrangements, 4,499 (about 9.2%) are multisourced. The data set includes more than 22,500 individual clients from 17 different industries, from government to transportation to discrete manufacturing. The average client has an annual revenue of \$17.1 billion and an average outsourcing capability of \$1.67 billion. The average contract value of these arrangements is \$58.3 million. Similarly, Table 4 presents the summary statistics and the correlations between dependent (contract outcome), independent, and control variables for 1,588 contracts<sup>2</sup> in Data set II, which is used to test Hypothesis 4.

## 5. Empirical Analysis

## 5.1. Econometric Models

We observe sourcing choice as a binary variable. There are two modes of sourcing: single-sourcing (zero) and multisourcing (one). The <sup>fi</sup>xed effect panel logit approach (Wooldridge 2002) is used in the analysis to predict the probabilities of the different outcomes of sourcing choice (see Table 2). Our panel is constructed by observing different IT outsourcing arrangements of the same client <sup>fi</sup>rm over multiple years.<sup>3</sup> Fixed effect panel logit controls for time invariant sources of unobserved heterogeneity. Equation (1) captures the likelihood of sourcing choice of the outsourcing arrangement signed by client i at time t on how many different IT services are involved in the IT outsourcing arrangement (NumberOfServices , the client’s IT outsourcing capabilities in period t (CustomerOutsourcingCapabilities ), and the competition in the IT industry in period t (IndustryCompetition<sub>t)</sub> along with the control variables and IT service dummies (Model 1 of Table 2).

Table 4. Summary Statistics and Correlations for the Contract Outcome Analysis (1,588 Contracts)

<table><tr><td>Variables</td><td>Mean</td><td>Std. dev.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>1. ContractValue ($ Millions)</td><td>285</td><td>706</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. NumberOfServices</td><td>2.276</td><td>1.548</td><td>0.28</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. CustomerOutsourcingCapabilities ($ billions)</td><td>0.79</td><td>3.96</td><td>0.19</td><td>-0.09</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. VendorOutsourcingCapabilities ($ billions)</td><td>30.2</td><td>52.5</td><td>0.25</td><td>0.16</td><td>0.13</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5. EngagementTypeComplexity</td><td>0.561</td><td>0.231</td><td>-0.25</td><td>-0.20</td><td>-0.01</td><td>-0.04</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6. CustomerRevenue ($ billions)</td><td>18.7</td><td>55.6</td><td>0.34</td><td>0.08</td><td>0.29</td><td>0.19</td><td>-0.12</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>7. FixedPrice(Y/N)</td><td>0.488</td><td>0.51</td><td>-0.21</td><td>-0.04</td><td>0.03</td><td>-0.01</td><td>0.08</td><td>-0.06</td><td>1</td><td></td><td></td><td></td></tr><tr><td>8. ExistingRelationshipStrength</td><td>1.39</td><td>0.88</td><td>0.02</td><td>0.07</td><td>0.21</td><td>0.18</td><td>-0.13</td><td>0.08</td><td>0.08</td><td>1</td><td></td><td></td></tr><tr><td>9. SourcingChoiceMisalignment</td><td>0.13</td><td>0.15</td><td>0.39</td><td>-0.02</td><td>0.32</td><td>0.11</td><td>-0.01</td><td>0.29</td><td>-0.01</td><td>0.29</td><td>1</td><td></td></tr><tr><td>10. Outcome</td><td>0.77</td><td>0.41</td><td>0.30</td><td>0.09</td><td>0.02</td><td>0.05</td><td>-0.01</td><td>0.04</td><td>0.11</td><td>0.02</td><td>-0.08</td><td>1</td></tr></table>

Note. Std. dev., standard deviation.

$$
\begin{array}{r l} \text { Sourcing   Choice } _ {i, t} & = \alpha_ {i} + \beta_ {1} \text { NumberOfServices } _ {i, t} \\ & + \beta_ {2} \text { CustomerOutsourcingCapabilities } _ {i, t} \\ & + \beta_ {3} \text { IndustryCompetition } _ {t} \\ & + \beta_ {4} \text { Control   Variables } _ {i, t} + \varepsilon_ {i, t} \end{array} \tag {1}
$$

Then, to determine whether the likelihood of multisourcing <sup>fi</sup>rst increases and then decreases as the number of services in an IT outsourcing arrangement increases, we add a square term to the <sup>fi</sup>xed effect logit model (Equation (1)). The curvilinear effects of the number of services in an IT outsourcing arrangement is captured in Equation (2), which again includes IT service dummies and control variables (Model 2 of Table 2).

$$
\begin{array}{l} \text { Sourcing   Choice } _ {i, t} = \alpha_ {i} + \beta_ {1} \text { NumberOfServices } _ {i, t} \\ \quad + \beta_ {2} \text { CustomerOutsourcingCapabilities } _ {i, t} \\ \quad + \beta_ {3} \text { IndustryCompetition } _ {t} \\ \quad + \beta_ {4} [ (\text { NumberOfServices }) _ {i, t} \\ \quad * (\text { NumberOfServices }) _ {i, t} ] \\ \quad + \beta_ {6} \text { Control   Variables } _ {i, t} + \varepsilon_ {i, t} \end{array} \tag {2}
$$

Next, we use a logit model (Equation (3)) to examine the relationship between sourcing choice misalignment (SourcingChoiceMisalignment of contract k between client i and vendor j on contract outcome (Contract $O u t c o m e _ { k , t } )$ . This model controls for contract characteristics (Contract Value, NumberOfServices, EngagementType-Complexity, ExistingRelationshipStrength, FixedPriceY/N), client characteristics (CustomerRevenue, CustomerOutsourcingCapabilities), and vendor characteristics (VendorOutsourcingCapabilities) and includes IT service dummies to capture the effect of sourcing choice misalignment on contract outcome (see Table 5).

$$
\begin{array}{r l} C o n t r a c t O u t c o m e _ {k, t} & = \beta_ {0} + \beta_ {1} C o n t r a c t V a l u e _ {k, t} \\ & \quad + \beta_ {2} N u m b e r O f S e r v i c e s _ {k, t} \\ & \quad + \beta_ {3} E n g a g e m e n t T y p e C o m p l e x i t y _ {k, t} \\ & \quad + \beta_ {4} E x i s t i n g R e l a t i o n s h i p S t r e n g t h _ {k, t} \\ & \quad + \beta_ {5} F i x e d P r i c e Y / N _ {k, t} \\ & \quad + \beta_ {6} C u s t o m e r R e v e n u e _ {i, t} \\ & \quad + \beta_ {7} C u s t o m e r O u t s o u r c i n g C a p a b i l i t i e s _ {i, t} \\ & \quad + \beta_ {8} V e n d o r O u t s o u r c i n g C a p a b i l i t i e s _ {j, t} \\ & \quad + \beta_ {9} S o u r c i n g C h o i c e M i s a l i g n m e n t _ {k, t} + \varepsilon_ {1} \end{array}
$$

## 5.2. Results

(3)

Model 1 in Table 2 is used to test Hypotheses 2 and 3, and Model 2 (also in Table 2) is used to test Hypothesis 1. This approach for testing the hypotheses using different models is appropriate in this case because the square term is constructed to be orthogonal to the corresponding singular term. Orthogonalization is used to avoid collinearity between the main effect and the square term (Little et al. 2006). In this approach, the indicator of the squared term is <sup>fi</sup>rst created by multiplying the main effect construct. Next, the squared term indicator is regressed on the main effect indicator. We then retain the residual from this regression as an indicator of the squared latent variable that is orthogonal to the main effect latent variable.

Table 5. Logit Model to Study the Impact of Sourcing Choice Misalignment on Contract Outcome

<table><tr><td>Variables</td><td>Outcome Model 1</td></tr><tr><td>ContractValue</td><td>0.110(0.039)</td></tr><tr><td>NumberOfServices</td><td>0.190(0.134)</td></tr><tr><td>CustomerOutsourcingCapabilities</td><td>0.011(0.135)</td></tr><tr><td>VendorOutsourcingCapabilities</td><td>0.113(0.175)</td></tr><tr><td>EngagementTypeComplexity</td><td>-0.170*(0.012)</td></tr><tr><td>CustomerRevenue</td><td>0.281*(0.172)</td></tr><tr><td>FixedPrice(Y/N)</td><td>0.102(0.039)</td></tr><tr><td>ExistingRelationshipStrength</td><td>0.091*(0.029)</td></tr><tr><td>SourcingChoiceMisalignment</td><td>-0.121**(0.043)</td></tr><tr><td>Constant</td><td>0.005(0.025)</td></tr><tr><td>Observations</td><td>1,588Pseudo  $R^{2}$  = 0.482</td></tr></table>

Note. Standard errors are in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

Results of the <sup>fi</sup>xed effect model models (see Table 2, Models 1 and 2) indicate that the coef<sup>fi</sup>cient of the number of services is positive and signi<sup>fi</sup>cant $( p < 0 . 0 1 )$ . Further, the coef<sup>fi</sup>cient of the square of the number of services is negative and signi<sup>fi</sup>cant $( p < ~ 0 . 0 1 )$ . These results suggest that as the number of services increases, the likelihood of multisourcing <sup>fi</sup>rst increases and then decreases. This <sup>fi</sup>nding is illustrated graphically in Figure 1, indicating that the likelihood of multisourcing increases up to <sup>fi</sup>ve services and decreases after that. These results indicate that the bene<sup>fi</sup>ts of specialization increase with up to about <sup>fi</sup>ve services, which increases the likelihood of multisourcing. However, beyond <sup>fi</sup>ve services the increase in coordination costs exceed the bene<sup>fi</sup>ts of specialization and single-sourcing is again the preferred alternative. This analysis provides support for Hypothesis 1.

These results (see Table 2, Models 1 and 2) also indicate that an increase in client IT outsourcing capabilities increases the likelihood of multisourcing $( p \ <$ 0.01). This <sup>fi</sup>nding is consistent with Hypothesis 2 and implies that if the client develops IT outsourcing capabilities in vendor selection, requirements de<sup>fi</sup>nition, and performance measurement, along with intervendor monitoring and coordination, the client has a broader range of sourcing choices available to outsource IT work. It is the coordination and integration capabilities of the client that open opportunities to take advantage of the economy of specialization and use multisourcing.

Next, the coef<sup>fi</sup>cient of industry competition is positive and signi<sup>fi</sup>cant $( p < 0 . 0 1 )$ in both Models 1 and 2 in

Table 2. These results suggest that increase in vendor specialization and competition increases the probability of <sup>fi</sup>nding specialist vendors for different services that increases the opportunity to take advantage of multisourcing. This <sup>fi</sup>nding supports Hypothesis 3.

Further, in both Models 1 and 2 in Table 2, our proxy for <sup>fi</sup>rm size (CustomerRevenue) is not signi<sup>fi</sup>cant, indicating that size of the <sup>fi</sup>rm does not affect sourcing choice; but our proxy for contract size (ContractValue) is positive and signi<sup>fi</sup>cant $( p < 0 . 0 1 )$ , indicating that larger deals are more likely to be multisourced. We also acknowledge that the nature of the service may in<sup>fl</sup>uence the sourcing choice (Susarla 2012), so we control for deal complexity (EngagementTypeComplexity). However, the coef<sup>fi</sup>cient of EngagementTypeComplexity is not signi<sup>fi</sup>cant, suggesting that the nature and complexity of the deal does not seem to in<sup>fl</sup>uence sourcing choice (see both Models 1 and 2 in Table 2). To stress test, we also include IT service dummies (such as application management, network management, systems integration, data center outsourcing, desktop outsourcing, IT help desk, etc.) in the main model (Table 2) and do not <sup>fi</sup>nd that these services affect the sourcing choice. This result again suggests that the nature of the IT service doesn’t affect the sourcing choice. And <sup>fi</sup>nally, our proxy for past relationship strength between the client and the vendor (ExistingRelationshipStrength) is negative and signi<sup>fi</sup>cant $( p < 0 . 1 )$ , indicating that if there is past relationship between a client and a vendor, the client is more likely to choose singlesourcing (see Models 1 and 2 in Table 2).

Table 5 presents the analysis of the effect of sourcing choice misalignment on contract outcome. Model 1 in Table 5 indicates that contracts with larger clients and instances where there is a strong relationship between the client and vendor are more likely to be successful, whereas more complex contracts are likely to be cancelled or renegotiated. Most interestingly, we <sup>fi</sup>nd that contracts with a higher level of misaligned sourcing choice are more likely to fail (p < 0.05). This <sup>fi</sup>nding supports Hypothesis 4 and emphasizes that sourcing choice is important for the success of the IT outsourcing contract, as a suboptimal sourcing choice can result in contract cancellation or renegotiation.

Figure 1. (Color online) (Hypothesis 1) As the Number of Services in an IT Outsourcing Arrangement Increases, the Likelihood of Multisourcing First Increases and Then Decreases  
![](/api/attachments/QZSRGDDW/fulltext/images/0ce5f9d68fdcfd929d2fca519379ad8526db0ad685e5c6c6f06813d01a352d3d.jpg)

## 6. Robustness Tests

## 6.1. Endogeneity and Reverse Causality

We used <sup>fi</sup>xed effect panel logit models that control for time invariant sources of unobserved heterogeneity. However, there may be time-varying client characteristics that are correlated with sourcing choice and key independent variables, raising potential unobserved heterogeneity and endogeneity concerns. Moreover, although we propose that the number of services leads to multisourcing, it is plausible that sourcing choice leads to decomposing an IT outsourcing arrangement into a set of services, raising endogeneity concerns due to reverse causality. Similarly, although we propose that an increase in vendor specialization increases the probability of <sup>fi</sup>nding specialist vendors for different services, which increases the opportunity to take advantage of multisourcing, it is possible that the trend toward multisourcing leads to an increase in vendo specialization (again, raising endogeneity concerns due to reverse causality).

To mitigate concerns with time variant sources of unobserved heterogeneity and endogeneity, we use a dynamic panel logit model to study the sourcing choice decision. Dynamic panel models are a powerful tool to handle endogeneity due to reverse causality and unobserved heterogeneity, as they disentangle the dynamic interplay between independent and depend ent variables over time by including lagged values of the dependent variable on the right-hand side of the estimation equation to produce unbiased and ef<sup>fi</sup>cient estimators for endogenous variables (Blundell and Bond 1998, Bapna et al. 2013b). In particular, we used the dynamic logit model designed by Hsiao (2005) and estimated it using the cquad package developed by Bartolucci and Pigini (2017). In Table 6 (Models 1 and 2), we present the results of the dynamic panel logit model that correspond to Models 1 and 2 in Table 2. The estimates in both models are consistent with our main results in Table 2. Further, we <sup>fi</sup>nd the presence of state dependence, as the p-value (or t test) associated with the lagged dependent variable (lagged sourcing choice) is signi<sup>fi</sup>cant (p < 0.01) in both Models 1 and 2 in Table $^ { 6 , }$ thus mitigating possible concerns with unobserved heterogeneity and endogeneity.

Table 6. Robustness Checks for Endogeneity and Reverse Causality

<table><tr><td>Variables</td><td>Model 1Dynamic logitMain effect</td><td>Model 2Dynamic logitInteraction effect</td><td>Model 3FE (using lagged NumberOfServices)Sourcing choice</td><td>Model 4FE (using lagged Industry Competition)Sourcing choice</td></tr><tr><td>Lagged(Sourcing Choice)</td><td>0.044***(0.116)</td><td>0.091***(0.103)</td><td></td><td></td></tr><tr><td>ContractValue</td><td>0.252***(0.073)</td><td>0.135**(0.262)</td><td>0.062***(0.124)</td><td>0.015**(0.003)</td></tr><tr><td>NumberOfServices</td><td>0.234***(0.136)</td><td>0.127***(0.104)</td><td></td><td>0.022***(0.011)</td></tr><tr><td>Lagged (NumberOfServices)</td><td></td><td></td><td>0.255***(0.031)</td><td></td></tr><tr><td>CustomerOutsourcingCapabilities</td><td>0.203***(0.182)</td><td>0.166**(0.052)</td><td>0.167***(0.158)</td><td>0.028***(0.017)</td></tr><tr><td>EngagementTypeComplexity</td><td>0.052(0.218)</td><td>0.172(0.163)</td><td>0.291(0.189)</td><td>0.002(0.024)</td></tr><tr><td>CustomerRevenue</td><td>0.164(0.009)</td><td>0.241(0.199)</td><td>0.104(0.323)</td><td>0.008(0.003)</td></tr><tr><td>Industry Competition</td><td>0.155***(0.261)</td><td>0.107**(0.031)</td><td>0.025***(0.122)</td><td></td></tr><tr><td>Lagged(Industry Competition)</td><td></td><td></td><td></td><td>0.018***(0.043)</td></tr><tr><td>ExistingRelationshipStrength</td><td>-0.047*(0.022)</td><td>-0.162**(0.091)</td><td>-0.210**(0.164)</td><td>-0.008*(0.141)</td></tr><tr><td>NumberOfServices * NumberOfServices</td><td></td><td>-0.185***(0.144)</td><td></td><td></td></tr><tr><td>Observations</td><td>42,494 $\chi^2 = 191.61^{***}(8)$ </td><td>42,494 $\chi^2 = 200.31^{***}(9)$ </td><td>42,494 $\chi^2 = 144.03^{***}(7)$ </td><td>42,494 $\chi^2 = 131.57^{***}(7)$ </td></tr></table>

Note. Standard errors are in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

In addition, to address concerns with reverse causality because of the number of services (multisourcing trend), we tested the sourcing choice model where we use the lagged value of number of services (industry competition) as an explanatory variable (see Table 6, Model 3 and Model 4, respectively). Our logic is that although sourcing choice may drive disaggregation of IT sourcing arrangements into distinct services (industry competition), it should not drive disaggregation of deals (industry competition) in prior years. The results in Table 6 (Models 3 and 4) are consistent with our main results in Table 2, thus mitigating the possibility of reverse causality due to the number of services (industry competition).

## 6.2. Customer Outsourcing Capabilities as Single-Sourcing Capabilities and Multisourcing Capabilities

In Hypothesis 2, we argued that the client’s IT outsourcing capabilities lead to more multisourcing. It may be argued that it is multisourcing capabilities that lead to more multisourcing. In other words, it may be useful to differentiate single-sourcing capabilities from multisourcing capabilities. Thus, in this analysis we focus on those clients (418 clients in our case) who use both single-sourcing and multisourcing. These 418 clients executed 9,076 arrangements/deals. Out of 9,076 arrangements, 5,029 are single-sourced and 4,047 are multisourced, so they have single-sourcing as well as multisourcing capabilities. We calculate their singlesourcing capabilities (as the dollar value of only the single-sourced IT deals executed by them before the current deal) and multisourcing capabilities (as the dollar value of only the multisourced IT deals executed by them before the current deal). We cannot include single sourcing capabilities as well as multisourcing capabilities in the same model because they are highly correlated, so Table 7 includes multisourcing capabilities and Table 8 includes single-sourcing capabilities. The coef<sup>fi</sup>cient of multisourcing capabilities is not signi<sup>fi</sup>cant in Table 7, but the coef<sup>fi</sup>cient of single-sourcing capabilities is signi<sup>fi</sup>cant in Table 8; the results are consistent with the results of our baseline analysis in Table 2. This analysis suggests that IT outsourcing capabilities that include single-sourcing capabilities help to develop capabilities that increase multisourcing. This <sup>fi</sup>nding also has managerial implications for clients who plan to multisource IT outsourcing arrangements and suggests that clients should develop IT outsourcing capabilities through <sup>fi</sup>rst engaging in single-sourcing prior to multisourcing larger IT outsourcing deals.

Table 7. Fixed Effect Logit Model for the Sourcing Choice Analysis-Client IT Outsourcing Capabilities Measured as Multisourcing Capabilities

<table><tr><td>Variables</td><td>Model 1 Sourcing choice</td><td>Model 2 Sourcing choice</td></tr><tr><td>ContractValue</td><td>0.254***(0.176)</td><td>0.271***(0.012)</td></tr><tr><td>NumberOfServices</td><td>0.026***(0.032)</td><td>0.185**(0.066)</td></tr><tr><td>MultisourcingCapabilities</td><td>0.072(0.189)</td><td>0.298(0.006)</td></tr><tr><td>EngagementTypeComplexity</td><td>0.275(0.088)</td><td>0.267(0.019)</td></tr><tr><td>CustomerRevenue</td><td>0.114(0.008)</td><td>0.322(0.104)</td></tr><tr><td>Industry Competition</td><td>0.075**(0.116)</td><td>0.051***(0.209)</td></tr><tr><td>ExistingRelationshipStrength</td><td>-0.171*(0.002)</td><td>-0.028**(0.243)</td></tr><tr><td>NumberOfServices * NumberOfServices</td><td></td><td>-0.157***(0.181)</td></tr><tr><td>Customer fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>9,076</td><td>9,076</td></tr><tr><td>Number of unique customers</td><td>418</td><td>418</td></tr><tr><td></td><td> $\chi^2 = 118.21^{***}(7)$ </td><td> $\chi^2 = 166.32^{***}(8)$ </td></tr></table>

Note. Standard errors are in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

Table 8. Fixed Effect Logit Model for the Sourcing Choice Analysis—Client IT Outsourcing Capabilities Measured as Single-Sourcing Capabilities

<table><tr><td>Variables</td><td>Model 1 Sourcing choice</td><td>Model 2 Sourcing choice</td></tr><tr><td>ContractValue</td><td>0.128***(0.035)</td><td>0.192***(0.181)</td></tr><tr><td>NumberOfServices</td><td>0.046**(0.144)</td><td>0.150**(0.276)</td></tr><tr><td>SinglesourcingCapabilities</td><td>0.266***(0.227)</td><td>0.133***(0.162)</td></tr><tr><td>EngagementTypeComplexity</td><td>0.038(0.299)</td><td>0.123(0.281)</td></tr><tr><td>CustomerRevenue</td><td>0.216(0.301)</td><td>0.318(0.001)</td></tr><tr><td>Industry Competition</td><td>0.214**(0.211)</td><td>0.168**(0.177)</td></tr><tr><td>ExistingRelationshipStrength</td><td>-0.134**(0.281)</td><td>-0.146**(0.040)</td></tr><tr><td>NumberOfServices * NumberOfServices</td><td></td><td>-0.233***(0.191)</td></tr><tr><td>Customer fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>9,076</td><td>9,076</td></tr><tr><td>Number of unique customers</td><td>418</td><td>418</td></tr><tr><td></td><td> $\chi^2 = 151.22^{***}(7)$ </td><td> $\chi^2 = 168.13^{***}(8)$ </td></tr></table>

Note. Standard errors are in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

## 6.3. Imbalance in the Number of Single-Sourced and Multisourced Arrangements

6.3.1. Sourcing Choice Analysis. Out of 49,057 arrangements in the sample, 44,558 arrangements are singlesourced and 4,499 arrangements are multisourced. This breakdown creates the issue of imbalanced data distribution across two classes (single-sourcing and multisourcing), potentially introducing biased estimates of coef<sup>fi</sup>cients of interest. To address the issue of data distribution across two classes, we use choice-based sampling. Choice-based sampling is a strati<sup>fi</sup>ed sampling technique. Here data are strati<sup>fi</sup>ed on the target and a sample is taken from each stratum so that the underrepresented class is more represented in the <sup>fi</sup>nal sample. The motivation behind this sampling scheme is to oversample underrepresented alternatives in order to improve the accuracy of econometric analysis (Manski and McFadden 1981, Imbens 1992, Imbens and Lancaster 1996). Thus, we combine the 4,499 observations with sourcing choice 1 (for multisourcing) along with a random sample of 4,499 observations with sourcing choice 0 (for single-sourcing) and repeat the <sup>fi</sup>xed effect logit analysis. The results are presented in Table 9 (Models 1 and 2) and are consistent with the analysis in Table 2 (Models 1 and 2).

6.3.2. Outcome Sample. Out of 1,588 contracts with known outcomes, 1,555 are single-sourced and 33 are multisourced contracts. The small number of multisourced contracts may bias results in the analysis examining the effect of sourcing choice misalignment on contract outcome. To mitigate this concern, we create new matched data sets using k-nearest neighbor technique (k-NN). k-NN is the simplest and best known nonparametric method, meaning we don't have to assume an explicit functional form, which provides a more <sup>fl</sup>exible approach (Bishop 2006). It uses the closest data points for estimation and therefore takes full advantage of local information to form highly nonlinear and adaptive decision boundaries for each data point. Corresponding to each of 33 multisourced contracts, we match the top k (<sup>fi</sup>ve and three in our case) nearest neighbors from 1,555 single-sourced contracts. Contracts are matched using the size of the contract, the number of services, client size, client IT outsourcing capabilities, complexity of the contract, year, and client industry. Models 1 and 2 in Table 10 show the results of the logit model for <sup>fi</sup>ve and three nearest neighbors, respectively. The results are consistent with the results in Table 5 (Model 1).

## 6.4. Coarsened Exact Matching (on the Outcome Sample)

To reduce heterogeneity between contracts with different sourcing choice and mitigate the issue of prediction bias of our outcome logit model (Model 1 in Table 5), we treat sourcing choice misalignment as treatment and apply coarsened exact matching (CEM) procedure on the outcome sample (Blackwell et al. 2009, Iacus et al. 2012, Bapna et al. 2016). Unlike propensity score

Table 9. Fixed Effect Logit Model for the Sourcing Choice Analysis (Choice-Based Sampling)

<table><tr><td>Variables</td><td>Model 1(Choice-based sampling)Sourcing choice</td><td>Model 2(Choice-based sampling)Sourcing choice</td></tr><tr><td>ContractValue</td><td>0.028**(0.038)</td><td>0.137***(0.044)</td></tr><tr><td>NumberOfServices</td><td>0.086***(0.283)</td><td>0.298***(0.063)</td></tr><tr><td>CustomerOutsourcingCapabilities</td><td>0.117***(0.019)</td><td>0.088**(0.091)</td></tr><tr><td>EngagementTypeComplexity</td><td>0.141(0.231)</td><td>0.187(0.096)</td></tr><tr><td>CustomerRevenue</td><td>0.046(0.032)</td><td>0.310(0.175)</td></tr><tr><td>Industry Competition</td><td>0.051**(0.239)</td><td>0.214**(0.139)</td></tr><tr><td>ExistingRelationshipStrength</td><td>-0.087**(0.388)</td><td>-0.177**(0.002)</td></tr><tr><td>NumberOfServices * NumberOfServices</td><td></td><td>-0.081***(0.253)</td></tr><tr><td>Customer fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>8,998</td><td>8,998</td></tr><tr><td>Number of unique customers</td><td>2,033</td><td>2,033</td></tr><tr><td></td><td> $\chi^2 = 109.14^{**}(7)$ </td><td> $\chi^2 = 145.96^{***}(8)$ </td></tr></table>

Note. Standard errors are in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

matching, CEM does not require a predetermined functional form and generates solutions that have lower estimation error and are better balanced (Bapna et al. 2016, King and Nielsen 2019). CEM coarsens a set of the observed covariates, then performs an exact match on the coarsened data and discards the unmatched data (Blackwell et al. 2009, Iacus et al. 2012, Bapna et al. 2016). To generate a coarsened matched sample, we focus on key covariates that affect the sourcing choice misalignment, namely, contract value, number of services, customer IT outsourcing capabilities, engagement type complexity, and customer revenue. Then we repeat the logit model analysis on the CEM sample (Model 1 in Table 11). The results are consistent with the primary analysis, suggesting that sourcing choice misalignment leads to contract failure.

Table 10. Logit Model to Study the Impact of Sourcing Choice Misalignment on Contract Outcome (Using k-NN)

<table><tr><td>Variables</td><td>Model 1Outcome (5NN)</td><td>Model 2Outcome (3NN)</td></tr><tr><td>ContractValue</td><td>0.231(0.017)</td><td>0.149(0.169)</td></tr><tr><td>NumberOfServices</td><td>0.169(0.015)</td><td>0.117(0.127)</td></tr><tr><td>CustomerOutsourcingCapabilities</td><td>0.183**(0.043)</td><td>0.122***(0.014)</td></tr><tr><td>VendorOutsourcingCapabilities</td><td>0.018*(0.171)</td><td>0.181***(0.120)</td></tr><tr><td>EngagementTypeComplexity</td><td>-0.256*(0.137)</td><td>-0.139***(0.071)</td></tr><tr><td>CustomerRevenue</td><td>0.310**(0.132)</td><td>0.361**(0.211)</td></tr><tr><td>FixedPrice(Y/N)</td><td>0.115(0.182)</td><td>0.159(0.170)</td></tr><tr><td>ExistingRelationshipStrength</td><td>0.276**(0.081)</td><td>0.012**(0.001)</td></tr><tr><td>SourcingChoiceMisalignment</td><td>-0.317**(0.133)</td><td>-0.220***(0.007)</td></tr><tr><td>Constant</td><td>0.155(0.111)</td><td>0.019(0.036)</td></tr><tr><td>Observations</td><td>198Pseudo $R^2$ =0.516</td><td>132Pseudo $R^2$ =0.721</td></tr></table>

Note. Standard errors are in parentheses  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

## 6.5. eXtreme Gradient Boost (XGBoost) (on the Outcome Sample)

To provide further robustness analysis of our outcome logit model (Model 1 in Table 5), we use a machinelearning-based model—XGBoost (by Chen and Guestrin 2016)—to compute our predicted sourcing choice variable. XGBoost is known as one of the most successful and potent prediction algorithms developed over the last few years. Unlike classical decision trees, which predict class labels, XGBoost employs boosted treebased models, thus bootstraps several decision trees; the <sup>fi</sup>nal prediction is based on the sum of predictions across multiple trees. Thus, it maximizes the out-ofsample-predictive accuracy and simultaneously corrects for over<sup>fi</sup>tting as well. Further, it is scalable and is shown to have advantages of both speed and performance (Chen and Guestrin 2016).

Table 11. Logit Model (on CEM sample) to Study the Impact of Sourcing Choice Misalignment on Contract Outcome

<table><tr><td>Variables</td><td>Model 1Outcome</td></tr><tr><td>ContractValue</td><td>0.216(0.004)</td></tr><tr><td>NumberOfServices</td><td>0.081(0.115)</td></tr><tr><td>CustomerOutsourcingCapabilities</td><td>0.067***(0.006)</td></tr><tr><td>VendorOutsourcingCapabilities</td><td>0.192**(0.181)</td></tr><tr><td>EngagementTypeComplexity</td><td>-0.211**(0.162)</td></tr><tr><td>CustomerRevenue</td><td>0.262***(0.033)</td></tr><tr><td>FixedPrice(Y/N)</td><td>0.064(0.330)</td></tr><tr><td>ExistingRelationshipStrength</td><td>0.088**(0.061)</td></tr><tr><td>SourcingChoiceMisalignment</td><td>-0.136***(0.258)</td></tr><tr><td>Constant</td><td>0.037(0.151)</td></tr><tr><td>Observations</td><td>1,418Pseudo  $R^{2}$  = 0.632</td></tr></table>

Note. Standard errors are in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1.

In our case, to construct the training data for our predictive model, we use only the contracts that were extended or expanded. Our assumption is that these contracts performed well and thus had the right sourcing choice. Then, we apply the XGBoost model (R software package by Chen and Guestrin 2016) to compute predictive sourcing choice using the key covariates (contract value, number of services, client IT outsourcing capabilities, engagement type complexity, and customer revenue). To prevent over<sup>fi</sup>tting, we use <sup>fi</sup>vefold cross validation on the training set and <sup>fi</sup>nd the optimal hyperparameters for our XGBoost model (max depth: four; learning rate: 0.03; n estimator: 94). The other parameters were kept at their default values. In this way, we build an XGBoost model with a prediction accuracy area under the ROC curve (AUC) value of 0.87 (which is higher than the predictive accuracy of a logit model with an AUC value of 0.74). Further, we also observe the actual sourcing choice the client has made using the SCD data. Next, we compute the sourcing choice misalignment variable, as the absolute value of the difference between the predicted sourcing choice (computed using XGBoost model) and the observed sourcing choice. Then, we repeat the logit model analysis on the contract outcome data set, using the above computed sourcing choice misalignment variable. The results (Model 1 in Table 12) are consistent with the primary analysis, suggesting that sourcing choice misalignment leads to contract failure.

## 7. Discussion and Conclusion

There is a large body of research in the IT outsourcing area; however, this body of work largely focuses on dyadic client-vendor relationships. Although theoretical and analytical models of single-sourcing versus multisourcing have been developed (Bhattacharya et al. 2018) and there is empirical research (Angst et al. 2017) that analyzes multisourcing trends in one industry (healthcare), there is no empirical research that examines the antecedents and consequents of multisourcing in the context of IT across multiple industries. The extant studies in multisourcing (e.g., Levina and Su 2008, Wiener and Saunders 2014, Aubert et al. 2016, Plugge and Bouwman 2018, Lioliou et al. 2019) are predominantly in-depth case studies that focus on the question of how to manage multisourcing arrangements. Our contention is that prior to managing a relationship, the client needs to <sup>fi</sup>rst make sure to enter into the right type of outsourcing arrangement; so in this paper, we focus on the determinants of the right type of outsourcing arrangement and the consequences of not entering into the correct outsourcing arrangement.

Table 12. Logit Model to Study the Impact of Sourcing Choice Misalignment (Computed Using XGBoost) on Contract Outcome

<table><tr><td>Variables</td><td>Outcome Model 1</td></tr><tr><td>ContractValue</td><td>0.178(0.152)</td></tr><tr><td>NumberOfServices</td><td>0.127(0.016)</td></tr><tr><td>CustomerOutsourcingCapabilities</td><td>0.084(0.005)</td></tr><tr><td>VendorOutsourcingCapabilities</td><td>0.108(0.112)</td></tr><tr><td>EngagementTypeComplexity</td><td>-0.193*(0.147)</td></tr><tr><td>CustomerRevenue</td><td>0.168*(0.004)</td></tr><tr><td>FixedPrice(Y/N)</td><td>0.185(0.171)</td></tr><tr><td>ExistingRelationshipStrength</td><td>0.182*(0.163)</td></tr><tr><td>SourcingChoiceMisalignment</td><td>-0.233***(0.158)</td></tr><tr><td>Constant</td><td>0.033(0.019)</td></tr><tr><td>Observations</td><td>1,588Pseudo  $R^{2}$  = 0.523</td></tr></table>

Note. Standard errors are in parentheses.  
\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.1

Our work builds on Bhattacharya et al. (2018), who develop a game theoretic approach to <sup>fi</sup>nd a client’s optimal sourcing strategy based on risk aversion of the vendor, coordination cost, modularity of the task, and misalignment between project revenue and veri<sup>fi</sup>able performance metric. Similarly, Angst et al. (2017) <sup>fi</sup>nd that hospitals are trending toward single-sourcing and <sup>fi</sup>nd the key organizational characteristics, such as formal structure and internal dynamics, that predict this trend. Likewise, Handley et al. (2022) examine the effect of experiential learning on the IT multisourcing trend. We conceptualize the choice between singlesourcing and multisourcing as the interplay of two opposing forces: (1) the ability to overcome coordination challenges and capability to manage exchange hazards, and (2) risks associated with sourcing, which shrinks with IT vendor industry competition (as it reduces the chances of lock-in and opportunism) but heightens with the number of different services in an IT outsourcing arrangement. We delve into the interplay between these forces and argue that both of these opposing forces are consequential to the single- versus multisourcing decision.

## 7.1. Theoretical Contribution and Empirical Findings

The theoretical contribution of the study extends the transaction cost framework used to make the insourcing versus outsourcing decision to the single-sourcing versus multisourcing decision. In the traditional transaction cost argument, outsourcing increases with the client’s ability to manage exchange hazards and the scale and specialization advantage of IT vendors. However, multisourcing exacerbates exchange hazards faced by clients, as it involves multiple vendors to take advantage of best-of-breed vendors, as no single vendor possesses specialization in all of the different IT-enabled services involved in an arrangement. Thus, we position the choice between single-sourcing and multisourcing as examining the trade-off between the client’s ability to manage the exchange hazards (as manifested in the client’s IT outsourcing capabilities) and the availability of specialized capabilities in the market (as manifested in the intensity of competition in the IT services market) as the number of services in an IT outsourcing arrangement increases. We <sup>fi</sup>nd that as the number of services increases to up to <sup>fi</sup>ve services, the likelihood of multisourcing increases; however, further increase in the number of services decreases the likelihood of multisourcing. Similarly, we show that as the client’s ability to manage exchange hazards increases, multisourcing increases relative to single-sourcing; as specialized capabilities become available in the IT services market, multisourcing also increases relative to single-sourcing.

The analysis suggests that if an IT outsourcing arrangement can be divided into separate services, a client is more likely to multisource. Disaggregating an IT outsourcing deal into distinct services enables clients to leverage specialized capabilities of different vendors; however, coordination cost increases with the number of services and vendors. Thus, beyond <sup>fi</sup>ve services, the increase in coordination costs dominates the bene<sup>fi</sup>ts of specialization and single-sourcing is preferred to multisourcing. Next, as a client’s IT outsourcing capabilities increase, a client is more likely to select multisourcing over single-sourcing. This suggests that as a client’s capability to manage exchange hazards and coordinate different vendors increases, the client is more likely to choose multisourcing. Moreover, as industry competition increases, the likelihood of multisourcing goes up. This is in line with the argument that as the IT services market matures and more specialist vendors establish themselves, <sup>fi</sup>rms have more opportunities to take advantage of specialization by multisourcing IT outsourcing arrangements that include different services. For vendors, it means that clients reward specialization. If a vendor can achieve scale economies in one service, the vendor can grow without the need to be a one-stop shop for integrated solutions. Most interestingly, we <sup>fi</sup>nd that if the sourcing choice is misaligned with the theory dis cussed above, the contract is more likely to be cancelled or renegotiated. In other words, sourcing choices that are incongruent with the number of services in an IT outsourcing arrangement, the IT outsourcing capabilities of the client or the capabilities and competition in the IT services market are more likely to be cancelled or rene gotiated. This study highlights the importance of the single-sourcing versus multisourcing choice by provid ing evidence that the single-sourcing versus multisourc ing choice has a material effect on contract outcome.

## 7.2. Managerial Implications

This research offers two key managerial insights for clients who want to engage in large IT outsourcing arrangements. First, the results of this study suggest that for multisourcing, clients need IT outsourcing capabilities. But how should clients build this capability? What kind of experience should they start with? Prior research on <sup>fi</sup>rm capabilities has shown that <sup>fi</sup>rms learn and grow through imitating successful strategies of other <sup>fi</sup>rms (Winter and Szulanski 2001, Helfat and Peteraf 2003), so it is natural to assume that clients will look at past sourcing strategies of <sup>fi</sup>rms that have contracted using both single-sourcing and multisourcing and follow their footsteps to develop successful sourcing strategies for themselves. To this end, the study suggests that clients who plan to multisource should develop IT outsourcing capabilities through <sup>fi</sup>rst engaging in single-sourcing.

Next, it may be believed that the sourcing choices depend upon the nature and complexity of the services— for instance, more complex services such as systems integration may be multisourced, and less complex services such as support engagement may be single-sourced. However, we do not <sup>fi</sup>nd suf<sup>fi</sup>cient evidence that service complexity affects sourcing choice. Exchange hazard risks that affect the sourcing decisions for large IT outsourcing arrangements do not arise from service complexity but rather from the number of services in an IT outsourcing arrangement. Our research suggests that with up to about <sup>fi</sup>ve services, the likelihood of multisourcing increases; beyond <sup>fi</sup>ve services, the increase in coordination costs exceed the bene<sup>fi</sup>ts of specialization and single-sourcing is again the preferred alternative. For large IT outsourcing arrangements (across multiple industries), we have found this to be the consistent optimal strategy between the number of services and sourcing choice, so for managers who plan to execute multisource arrangements, this research proposes mechanisms to minimize exchange hazards through better understanding of the relationship between the number of services in an IT outsourcing arrangement and sourcing choice.

## 7.3. Limitations and Directions for Future Research

This study has certain limitations that suggest directions for future research. In this data set, although we know that in multisourcing arrangements multiple vendors work together to provide services to the client, we don’t know the degree of the interdependence between the various services they perform. As prior research has noted, structuring a large IT outsourcing arrangement into distinct but interdependent services that can be assigned to different vendors is by itself a challenging endeavor (Gokpinar et al. 2013, Tripathy and Eppinger 2013, Mishra et al. 2015). Understanding the nature of the service interdependence may provide insight into how risk is shared by multiple vendors in the multisourcing model; however, access to such granular data continues to remain a challenge for the research community. Different vendors in a multisourcing arrangement may live in different time zones, and they may differ culturally from the client. In our data set, we know the identity of the vendor(s) but not their speci<sup>fi</sup>c location, so data limitations preclude us from examining the coordination cost implications of physical and cultural distance.

Prior research (Bapna et al. 2010) highlighted the coordination and cooperation issues that arise from multisourcing and proposed sourcing architectures, such as operating-level agreements and prime-vendor models, to mitigate some of the risks. More research is needed in teasing out the ef<sup>fi</sup>cacy of these proposed solutions. Prior research (Levina and Su 2008) has also identi<sup>fi</sup>ed four archetypes of multisourcing relationships as a function of variation of breadth and depth of the multisourcing supply base: concentrated transactions, concentrated partnerships, diversi<sup>fi</sup>ed transactions, and diversi<sup>fi</sup>ed partnerships. Similarly, Wiener and Saunders (2014) de-<sup>fi</sup>ne multisourcing as being mediated, direct, or directoverlapping. Future empirical research may re<sup>fi</sup>ne the characterization of multisourcing as described in these papers. Future research should also tackle the relationship between the degree of service interdependence, service and output veri<sup>fi</sup>ability, and the design of optimal compensation schemes in the context of multisourcing.

## 7.4. Conclusion

As clients sign large IT outsourcing deals/arrangements, it becomes more and more likely that the outsourcing arrangement demands different IT specializations that no single vendor may possess. Given that one of the key rationales for outsourcing includes bene<sup>fi</sup>ting from a vendor’s scale and specialization, it is only natural to expect that multisourcing increases with deal size. Accordingly, industry reports and academic research indicate an increase in multisourcing (Cohen and Young 2006, Anderson and Parker 2013, Mishra et al. 2015). However, multisourcing is not without its challenges (Hao et al. 2016, Mishra and Sinha 2016, Oshri et al. 2019). Complex coordination with multiple vendors exacerbates the challenges associated with multisourcing (Whitten and Leider 2006). Through TCE framework and a datadriven approach, we shed light on both the antecedents and consequents of the decision to multisource or not; yet there remain many unanswered questions about how to design, contract, and manage multisourcing relationships. As the volume of multisourcing increases, we hope that this research will engender further enquiry into this important phenomenon.

## Endnotes

<sup>1</sup> It is plausible that contract renegotiation is not a necessarily bad outcome if the client and vendor renegotiate the contract as conditions change (Susarla 2012). A robustness check with contract extension and expansion coded as positive outcome and contract cancellation coded as negative outcome also produces consistent results.

<sup>2</sup> We also conducted a series of Kolmogorov-Smirnov tests (on key variables that are common between the sourcing choice and the outcome model) to check for any potential bias in the contract outcome sample compared with the sourcing choice sample. Results of the tests indicated that there is no difference in the distributions in the common variables across two samples.

<sup>3</sup> Our panel is unbalanced, which raises a potential selection bias issue in fixed effect panel models with binary responses. In order to handle this issue and to examine if there is selection bias as a result of the unbalanced panel, we conducted the Semykina and Wooldridge (2018) test. The results of this test show no evidence for selection bias due to the structure of an unbalanced panel and provides additional robustness check and consistency of our fixed effect panel models.

<sup>4</sup> Analysis without the orthogonalization of the square term also produces results that are consistent with these findings.

## References

Ahmadjian CL, Lincoln JR (2001) Keiretsu, governance, and learning: Case studies in change from the Japanese automotive industry. Organ. Sci. 12(6):683–701.

Anderson EG, Parker GG (2013) Integration in global knowledge networks. Production Oper. Management 22(6):1446–1463.

Anderson EG, Jiang X, Parker GG, Tan B (2019) Systems integration and the dynamics of partial outsourcing. Production Oper. Man agement 28(2):319–340.

Ang E, Iancu DA, Swinney R (2017) Disruption risk and optimal sourc ing in multitier supply networks. Management Sci. 63(8):2397–2419.

Ang S, Straub D (1998) Production and transaction economies and IS outsourcing: A study of the U.S. banking industry. MIS Quart. 22(4):535–552.

Angst CM, Wowak KD, Handley SM, Kelley K (2017) Antecedents of information systems sourcing strategies in U.S. hospitals: A longitudinal study. MIS Quart. 41(4):1129–1152.

Anupindi R, Akella R (1993) Diversi<sup>fi</sup>cation under supply uncertainty. Management Sci. 39(8):944–963.

Aral S, Bakos Y, Brynjolfsson E (2018) IT, repeated contracts, and the number of suppliers. Management Sci. 64(2):592–612.

Argyres N, Bigelow L (2007) Does transaction misalignment matter for <sup>fi</sup>rm survival at all stages of the industry life cycle? Management Sci. 53(8):1332–1344.

Aron R, Bandyopadhyay S, Jayanty S, Pathak P (2008) Monitoring process quality in off-shore outsourcing: A model and <sup>fi</sup>ndings from multi-country survey. J. Oper. Management 26(2):303–321.

Aron R, Clemons EK, Reddi S (2005) Just right outsourcing: Understanding and managing risk. J. Management Inform. Systems 22(2):37–55.

Aubert BA, Saunders C, Wiener M, Denk R, Wolfermann T (2016) How Adidas realized bene<sup>fi</sup>ts from a contrary IT multisourcing strategy. MIS Quart. Executive 15(3):179–194.

Aydin G, Babich V, Beil DR, Yang ZB (2011) Handbook of Integrated Risk Management in Global Supply Chains (John Wiley & Sons, New York).

Bakos Y, Brynjolfsson E (1993) From vendors to partners: Information technology and incomplete contracts in buyer-supplier relationships. J. Organ. Comput. 3(3):301–328.

Bala R, Krishnan V, Zhu W (2014) Distributed development and product line decisions. Production Oper. Management 23(6):1057–1066.

Bandopadhyay S, Pathak P (2007) Knowledge sharing and cooperation in outsourcing projects—A game theoretic analysis. Deci sion Support Systems 43(2):349–358.

Bapna R, Barua A, Mani D, Mehra A (2010) Research commentary—Cooperation, coordination, and governance in multisourcing: An agenda for analytical and empirical research. Inform. Systems Res. 21(4):785–795.

Bapna R, Gupta A, Ray G, Singh S (2013a) Specialization, integration, and multisourcing: A study of large IT outsourcing projects. Proc. Internat. Conf. Inform. Systems (ICIS, Milan), 3537–3551.

Bapna R, Gupta A, Ray G, Singh S (2016) Research note—IT outsourcing and the impact of advisors on clients and vendors. Inform. Systems Res. 27(3):636–647.

Bapna R, Langer N, Mehra A, Gopal R, Gupta A (2013b) Human capital investments and employee performance: An analysis of IT services industry. Management Sci. 59(3):641–658.

Bartolucci F, Pigini C (2017) cquad: An R and Stata package for conditional maximum likelihood estimation of dynamic binary panel data models. J. Statist. Software 78(7):1–26.

Bhattacharya S, Gupta A, Hasija S (2018) Single-sourcing vs. multisourcing: The roles of output veri<sup>fi</sup>ability on task modularity. MIS Quart. 42(4):1171–1186.

Bimpikis K, Candogan O, Ehsani S (2019) Supply disruptions and optimal network structures. Management Sci. 65(12):5504–5517.

Bishop CM (2006) Pattern Recognition and Machine Learning (Springer Press, New York).

Blackwell M, Iacus SM, King G, Porro G (2009) CEM: Coarsened exact matching in Stata. Stata J. 9(4):524–546.

Blundell R, Bond S (1998) Initial conditions and moment restrictions in dynamic panel data models. J. Econometrics 87(1):115–143

Brown D, Fersht P (2014) Executive Report: The State of Services and Outsourcing in 2014 (KPMG and HfS Research). https://www. iqpc.com/media/8186/33180.pdf.

Cabigiosu A, Camuffo A (2012) Beyond the mirroring hypothesis: Product modularity and interorganizational relations in the ai conditioning industry. Organ. Sci. 23(3):683–703.

Chen T, Guestrin C (2016) Xgboost: A scalable tree boosting system. Proc. 22nd ACM SIGKDD Internat. Conf. Knowledge Discover Data Mining (ACM, New York), 785–794.

Choudhury V, Sabherwal R (2003) Portfolios of control in outsourced software development projects. Inform. Systems Res. 14(3):291–314.

Clemons EK, Reddi S, Row S (1993) The impact of information technology on the organization of economic activity: The “move to the middle” hypothesis. J. Management Inform. Systems 10(2):9–35.

Cohen L, Young A (2006) Multi-Sourcing: Moving Beyond Outsourcin to Achieve Growth and Agility (Harvard Business Press, Cambridge, MA).

Dada M, Petruzzi N, Schwarz L (2007) A newsvendor’s procurement problem when suppliers are unreliable. Manufacturing Service Oper. Management 9(1):9–32.

Deloitte Consulting (2005) Calling a change in the outsourcing market: The realities for the world’s largest organizations. Accessed September 1, 2022, https://www.worldcat.org/title/calling-achange-in-the-outsourcing-market-the-realities-for-the-worlds largest-organizations/oclc/60884313.

Dey D, Fan M, Zhang C (2010) Design and analysis of contracts for software outsourcing. Inform. Systems Res. 21(1):93–114.

Dibbern J, Goles T, Hirschheim R, Jayatilaka B (2004) Information systems outsourcing: A survey and analysis of the literature. ACM SIGMIS Database 35(4):6–102.

Dyer JH, Hatch NW (2004) Using supplier networks to learn faster. MIT Sloan Management Rev. 45(3):57–63.

Federgruen A, Yang N (2008) Selecting a portfolio of suppliers under demand and supply risks. Oper. Res. 56(4):916–936.

Fitoussi D, Gurbaxani V (2012) IT outsourcing contracts and performance measurement. Inform. Systems Res. 23(1):129–143.

Gokpinar B, Hopp W, Iravani SMR (2013) In-house globalization: The role of globally distributed design and product architecture on product development performance. Production Oper. Management 22(6):1509–1523.

Gopal A, Gao G (2009) Certi<sup>fi</sup>cation in the Indian offshore IT services industry. Manufacturing Service Oper. Management 11(3):471–492.

Gopal A, Koka BR (2010) The role of contracts on quality and returns to quality in offshore software development outsourcing. Decision Sci. 41(3):491–516.

Gopal A, Konduru S (2008) On vendor preferences for contract types in offshore software projects: The case of <sup>fi</sup>xed price vs. time and materials contracts. Inform. Systems Res. 19(2):202–220.

Grover V, Teng JTC (1993) The decision to outsource information systems functions. J. Systems Management 44(11):34–38.

Han K, Kauffman RJ, Nault BR (2011) Returns to information tech nology outsourcing. Inform. Systems Res. 22(4):824–840.

Handley SM (2017) How governance misalignment and outsourcing capability impact performance. Production Oper. Management 26(1):134–155.

Handley S, Skowronski K, Thakar D (2022) The single-sourcing vs. multisourcing decision in information technology outsourcing. J. Oper. Management 68(6-7):702–727.

Hao X, Dawande M, Mookerjee V (2016) Optimal coordination in distributed software development. Production Oper. Management 25(1):56–76.

Helfat CE, Peteraf MA (2003) The dynamic resource based view: Capability lifecycles. Strategic Management J. 24(10):997–1010.

Hsiao C (2005) Analysis of Panel Data (Cambridge University Press, New York).

Hu B, Kostamis D (2015) Managing supply disruptions when sourcing from reliable and unreliable suppliers. Production Oper. Management 24(5):808–820.

Iacus SM, King G, Porro G (2012) Causal inference without balance checking: Coarsened exact matching. Political Anal. 20(1):1–24.

Imbens GW (1992) An ef<sup>fi</sup>cient method of moments estimator for discrete choice models with choice-based sampling. Econometrica 60(5):1187–1214.

Imbens GW, Lancaster T (1996) Ef<sup>fi</sup>cient estimation and strati<sup>fi</sup>ed sampling. J. Econometrics 74(2):289–318.

Karamouzis F (2011) Multisourcing competencies key initiative overview. Accessed September 1, 2022, https://www.gartner.com/en/ documents/1745519

King G, Nielsen R (2019) Why propensity scores should not be used for matching. Political Anal. 27(4):435–454.

Kirsch LJ (2004) Deploying common systems globally: The dynam ics of control. Inform. Systems Res. 15(4):374–395.

Kishore R, Rao HR, Nam K, Rajagopalan S, Chaudhury A (2003) A rela tionship perspective on IT outsourcing. Comm. ACM 46(12):86–92.

Koh CS, Ang S, Straub DW (2004) IT outsourcing success: A psychological contract perspective. Inform. Systems Res. 15(4):356–373.

Koo Y, Lee J-N, Heng CS, Park J (2017) Effect of multi-vendor outsourcing on organizational learning: A social relation perspective. Inform. Management 54(3):396–413.

Kotlarsky J, Oshri I, Dibben J, Mani D (2018) IS sourcing. Bush A, Rai A, eds. MIS Quarterly Research Curations. http://misq.org/ research-curations.

Lacity M, Hirschheim R (1993) The information systems outsourcing bandwagon. Sloan Management Rev. 35(1):73–86.

Lacity M, Willcocks L (1998) An empirical investigation of information technology sourcing practices: Lessons from experience. MIS Quart. 22(3):363–408.

Langlois RN (2002) Modularity in technology and organization. J. Econom. Behav. Organ. 49(1):19–37.

Lee JN, Miranda SM, Kim YM (2004) IT outsourcing strategies: Uni versalistic, contingency, and con<sup>fi</sup>gurational explanations of success. Inform. Systems Res. 15(2):110–131.

Leiblein MJ, Reuer JJ, Dalsace F (2002) Do make or buy decisions matter? The in<sup>fl</sup>uence of governance on technological performance. Strategic Management J. 23(9):817–833.

Levina N (2005) Collaborating on multi-party information systems development projects: A collective re<sup>fl</sup>ection-in-action view. Inform. Systems Res. 16(2):109–130.

Levina N, Ross J (2003) From the vendor’s perspective: Exploring the value proposition in information technology outsourcing. MIS Quart. 27(3):331–364.

Levina N, Su N (2008) Global multisourcing strategy: The emergence of a supplier portfolio in services offshoring. Decision Sci. 39(3):541–570.

Levina N, Vaast E (2005) The emergence of boundary spanning competence in practice: Implications for implementation and use in information systems. MIS Quart. 29(2):335–363.

Levina N, Vaast E (2008) Innovating or doing as told? Status differences and overlapping boundaries in offshore collaboration. MIS Quart. 32(2):307–332.

Li S, Shang J, Slaughter SA (2010) Why do software <sup>fi</sup>rms fail? Capabilities, competitive actions, and <sup>fi</sup>rm survival in the software industry from 1995 to 2007. Inform. Systems Res. 21(3):631–654.

Lioliou E, Willcocks L, Liu X (2019) Researching IT multi-sourcing and opportunistic behavior in conditions of uncertainty: A case approach. J. Bus. Res. 103:387–396.

Little TD, Bovaird JA, Widaman KF (2006) On the merits of orthogonalizing power and product terms: Implications for modeling interactions among latent variables. Structural Equation Model. 13(4):497–519.

Loh L, Venkatraman N (1992a) Determinants of information technology outsourcing: A cross-sectional analysis. J. Management Inform. Systems 9(1):7–24.

Loh L, Venkatraman N (1992b) Diffusion of information technology outsourcing: In<sup>fl</sup>uence sources and the Kodak effect. Inform. Systems Res. 3(4):334–358.

Mani D, Barua A, Whinston A (2012) An empirical analysis of the contractual and information structures of business process outsourcing relationships. Inform. Systems Res. 23(3):618–634.

Manski CF, McFadden D (1981) Structural Analysis of Discrete Data with Econometric Applications (MIT Press, Cambridge, MA).

Mishra A, Chandrasekaran A, MacCormack A (2015) Collaboration in multi-partner R&D projects: The impact of partnering scale and scope. J. Oper. Management 33(34):1–14.

Mishra A, Sinha KK (2016) Work design and integration glitches in globally distributed technology projects. Production Oper. Management 25(2):347–369.

Narasimhan R, Talluri S (2009) Perspectives on risk management in supply chains. J. Oper. Management 27(2):114–118.

Narayanan S, Jayaraman V, Luo Y, Swaminathan JM (2011) The antecedents of process integration in business process outsourcing and its effect on <sup>fi</sup>rm performance. J. Oper. Management 291(2):3–16.

Nickerson JA, Silverman BS (2003) Why <sup>fi</sup>rms want to organize ef<sup>fi</sup> ciently and what keeps them from doing so: Inappropriate gover nance, performance, and adaptation in a deregulated industry Admin. Sci. Quart. 48(3):433–465.

Nyden J, Kane L (2019) How to reduce value leakage in complex contracts. Sourcing Industry Group (SIG), https://sig.org/ blog/how-reduce-value-leakage-complex-contracts#:\~:text= According%20to%20reports%20authored%20by%20the%20 International%20Association,from%20the%20time%20of %20execution%20through%20to%20close-out.

Oshri I, Dibbern J, Kotlarsky J, Krancher O (2019) An information processing view on joint vendor performance in multi-sourcing: The role of the guardian. J. Management Inform. Systems 36(4):1248–1283.

Oshri I, Kotlarsky J, Willcocks L (2015) The Handbook of Global Out sourcing and Offshoring: The Definitive Guide to Strategy and Operations (Palgrave Macmillan, London).

Plugge A, Bouwman H (2018) Tensions in global IT multisourcing arrangements: Examining the barriers to attaining common value creation. J. Global Inform. Tech. Management 21(4):262–281.

Poppo L, Zenger T (2002) Do formal contracts and relational governance function as substitutes or complements? Strategic Management J. 23(8):707–725

Pournader M, Kach A, Talluri S (2020) A review of the existing and emerging topics in supply chain risk management literature. Decision Sci. 51(4):867–919.

Richardson J (1993) Parallel sourcing and supplier performance in the Japanese automobile industry. Strategic Management J. 14(5):339–350.

Sabherwal R (1999) The role of trust in outsourced IS development projects. Comm. ACM 42(2):80–86.

Sampson RC (2004) The cost of misaligned governance in R&D alli ances. J. Law Econom. Organ. 20(2):484–526.

Semykina A, Wooldridge J (2018) Binary response panel data models with sample selection and self-selection. J. Appl. Econometrics 33(2):179–197.

Sia SK, Koh C, Tan CX (2008) Strategic maneuvers for outsourcing <sup>fl</sup>exibility: An empirical assessment. Decision Sci. 39(3): 407–443.

Simon HA (1962) The architecture of complexity. Proc. Amer. Philos. Soc. 106(6):467–482.

Slaughter S, Ang S (1996) Employment outsourcing in information systems. Comm. ACM 39(7):47–54.

Su N, Levina N (2011) Global multisourcing strategy: Integrating learning from manufacturing into IT service outsourcing. IEEE Trans. Engrg. Management 58(4):717–729.

Su N, Levina N, Ross JW (2016) The long-tail strategy for IT out sourcing. MIT Sloan Management Rev. 57(2):81–89.

Susarla A (2012) Contractual <sup>fl</sup>exibility, rent seeking, and renegotiation design: An empirical analysis of information technology outsourcing contracts. Management Sci. 58(7):1388–1407.

Susarla A, Barua A (2011) Contracting ef<sup>fi</sup>ciency and new <sup>fi</sup>rm survival in markets enabled by information technology. Inform. Systems Res. 22(2):306–324.

Susarla A, Subramanyam R, Karhade P (2010) Contractual provi sions to mitigate holdup: Evidence from information technol ogy outsourcing. Inform. Systems Res. 21(1):37–55.

Tiwana A (2008) Does inter<sup>fi</sup>rm modularity complement ignorance? A <sup>fi</sup>eld study of software outsourcing alliances. Strategic Management J. 29(11):1241–1252.

Tomlin B, Yimin W (2005) On the value of mix <sup>fl</sup>exibility and dual sourcing in unreliable newsvendor networks. Manufacturing Service Oper. Management 7(1):37–57.

Tripathy A, Eppinger SD (2013) Structuring work distribution for global product development organizations. Production Oper. Management 22(6):1557–1575.

Vaidyanathan J, Narayanan S, Luo Y, Swaminathan JM (2012) Offshoring business process services and governance control mechanisms: An examination of service providers from India. Production Oper. Management 22(2):314–334.

Walden EA (2005) Intellectual property rights and cannibalization in information technology outsourcing contracts. MIS Quart. 29(4):699–720.

Wang Y, Gilland W, Tomlin B (2010) Mitigating supply risk: Dualsourcing or process improvement? Manufacturing Service Oper. Management 12(3):489–510.

Whitten D, Leidner D (2006) Bringing IT back: An analysis of the deci sion to backsource or switch vendors. Decision Sci. 37(4):605–621.

Wiener M, Saunders C (2014) Forced coopetition in IT multi-sourcing. J. Strategic Inform. Systems 23(3):210–225.

Williamson OE (1979) Transaction-cost economics: The governance of contractual relations. J. Law Econom. 22(2):233–261.

Williamson OE (1985) The Economic Institutions of Capitalism (Free Press, New York).

Winter SG, Szulanski G (2001) Replication as strategy. Organ. Sci. 12(6):339–351.

Wooldridge JM (2002) Econometric Analysis of Cross Section and Panel Data (MIT Press, Cambridge, MA)

Yang Z, Aydın G, Babich V, Beil DR (2012) Using a dual-sourcing option in the presence of asymmetric information about supplier reliability: Competition vs. diversi<sup>fi</sup>cation. Manufacturin Service Oper. Management 14(2):202–217.

Zollo M, Winter S (2002) Deliberate learning and the evolution of dynamic capabilities. Organ. Sci. 13(3):339–351.

C<sub>opy</sub>ri<sub>g</sub>ht 2023 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
