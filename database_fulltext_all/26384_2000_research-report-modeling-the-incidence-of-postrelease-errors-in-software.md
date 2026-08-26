---
otero_id: 26384
otero_key: "T9W6T469"
title: "Research Report: Modeling the Incidence of Postrelease Errors in Software"
authors: "J. Christopher Westland"
year: "2000"
journal: "Information Systems Research"
doi: "10.1287/isre.11.3.320.12204"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [128.255.6.125] On: 15 September 2016, At: 09:21 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## 6SR

# Information Systems Research

![](/api/attachments/T9W6T469/fulltext/images/8532fb0ef35245ce95d08054ee8bf4fb255efcfd5919c8d0743eafd44e29ef18.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Research Report: Modeling the Incidence of Postrelease Errors in Software

J. Christopher Westland,

## To cite this article:

J. Christopher Westland, (2000) Research Report: Modeling the Incidence of Postrelease Errors in Software. Information Systems Research 11(3):320-324. http://dx.doi.org/10.1287/isre.11.3.320.12204

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2000 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/T9W6T469/fulltext/images/a329d651798531b799a1e4d2b03da0b99f2768b25f4fee9051d42a46321fc93a.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Report: Modeling the Incidence of Postrelease Errors in Software

J. Christopher Westland

Department of Information & Systems Management, The Hong Kong University of Science & Technology, Clear Water Bay, Kowloon, Hong Kong SAR, China westland@ust.hk

E <sup>rror</sup> <sup>search</sup> <sup>and</sup> <sup>correction</sup> <sup>are</sup> <sup>major</sup> <sup>contributors</sup> <sup>to</sup> <sup>software</sup> <sup>development</sup> <sup>cost,</sup> <sup>yet</sup> <sup>typ-</sup> ically uncover only a small fraction of software errors. Postrelease errors, i.e., those that are only observed after a system is released, threaten a variety of potential failures and consequences, each with low individual probability of occurrence. The combined effect of postrelease errors can and often does result in a significant rate of occurrence of these potential failures, with unpredictable consequences and severity. One particular source of postrelease errors that has received extensive publicity is the year 2000, or Y2K, error. The modeling in this research report suggests that testing probably needs to be conducted over more than half of the useful life of a system in order to discover even one-third of the total errors in the system. It suggests that short product lifecycles, lifetime testing, and effective feedback loops for error reporting are necessary to assure reliable software.

(Software Errors and Reliability; Economics of Information Technology)

## Introduction

Error search and correction are time consuming and expensive software development tasks. Various studies have questioned the effectiveness of these activities, finding that many errors go undetected at the time of software release.<sup>1</sup> The issue is clouded by a paucity of forecasting models for the occurrence of information systems errors in general, and in particular for errors that are so difficult to find that they are only observed after systems are released to production. Errors that are only observed after these systems are released will be termed postrelease errors in this research report. This report develops a model of postrelease error occurrence based on prior empirical findings, and calculates expected rates of postrelease error occurrence.

Adams (1980) called the failure of software testing to detect all but a small portion of systems errors the “5,000-year error” problem. Adams argued that the vast majority of software errors escape detection during prerelease testing. Any arbitrarily chosen one of these errors (assuming one could actually make such a choice) would appear only once in 5,000 years. However, because there are a large number of these types of errors inherent in any system, it is likely that one or more of these postrelease errors will appear in any time period and that some would result in serious disruptions to system’s services (Littlewood and Strigini 1993).

Validating Adam’s assertion concerning these extraordinarily long times to failure has been difficult. Butler and Finelli (1993) have even argued that software error rates can never accurately be predicted, despite what must be a significant demand for such forecasts. Most systems are retired within a decade or two because the organizational objectives, corporate hierarchy, and technology platforms they serve become obsolete. Most errors—serious or otherwise—are unlikely to manifest themselves during the software’s economic life. Yet an immense variety of potential failure types, each with low individual probability of occurrence, can and often do result in a significant rate of occurrence of postrelease errors, with unpredictable consequences and severity.

Software error forecasting is confounded by the poor quality of software error statistics and data collection. Software Productivity Research executive Capers Jones noted that fewer than 10 percent of companies who collect software development metrics include defect statistics and even fewer record process errors (Inwood 1994). Testing tends to be directed toward code rather than systems use. Unfortunately, notes Inwood, only about one in three program defects originate in code. The rest typically arise from unintended use of the code—i.e., where the programmer has correctly coded an incomplete or incorrect set of requirements specifications (as is the case with year 2000 errors). One survey of 20 companies suggested that the norm for software-defect removal is about 75 percent of the errors that appear in the first year after release (Inwood 1993). Greater complexity of programming tasks seems to contribute to the level of errors. For example, a study by Selby (1993) noted that complex software—indicated by high coupling/cohesion ratios— had 8.1 times more errors per line of source code than average.

## Model and Analysis

Controlling postrelease software errors is increasingly important. A legal niche is forming as computer technology becomes ever more pervasive and opportunities arise for customers to seek damages from faulty software. Car accidents, medical misdiagnosis, incorrect accounting, and faulty inventory lists are some ramifications of failing computer systems. Plaintiffs’ lawyer Bruce Bierhans argues that the majority of future litigation is going to center on computer performance (Geyelin 1994). The greater unpredictability of postrelease errors—both in severity and consequence—provides fertile soil for plaintiff’s lawsuits.<sup>2</sup> There appears to be no easy answer to the legal conundrum, but better prediction of postrelease errors will help management set optimal levels of testing, insurance, and legal disclaimers.

The model below contributes to the challenge of improving the handling of postrelease errors by building on Adams’ (1980) analysis of IBM software development data. Adam’s data can be fit to a least squares regression to a sixth degree polynomial yields:

$$
\begin{array}{r l} P [ t ] & = \text { Proportion   of   errors   detected   after } t \text { years } \\ & = 2. 2 6 1 \cdot 1 0 ^ {- 1 9} t + 3. 5 0 9 \cdot 1 0 ^ {- 1 7} t ^ {2} + 1. 3 8 0 \cdot 1 0 ^ {- 1 4} \\ & t ^ {3} + 4. 6 6 3 \cdot 1 0 ^ {- 1 2} t ^ {4} - 3. 8 6 1 \cdot 1 0 ^ {- 1 5} \\ & t ^ {5} + 5. 8 5 7 \cdot 1 0 ^ {- 1 9} t ^ {6} \end{array}
$$

This model can be extrapolated to infer error occurrence over the full life of the software system.<sup>3</sup> The coefficients are small because the proportion runs from 0 to 1, while years x run from 0 to 5,000, resulting in large exponents of the powers of t. In practice, the total number of errors in a system—call it M—will be unknown, which contributes to the risk and uncertainty of software implementations. If M were known, then P(t) • M would be the cumulative distribution function for errors appearing in the system.

Figures 1 and 2 depict Adam’s empirical, captured in the power series P(t), from a hypothetical long-run perspective of several hundred years, and from a short-run perspective that reflects the retirement of software in a much shorter period. Typically, this will be less than 20 years, though the Y2K problem has shown how enduring software and systems can be.

This expression of P(t) makes no assumptions about the total number of errors that are programmed into a particular system’s software. This number is presumably unknowable; the potential for new, varying, and unintended use of software makes the total count dependent on the environment, users, and application of the software, in addition to the program code. Nonetheless, it is instructive to assume that there is some absolute count of errors in a system, call it M, which will influence the rate of error occurrence in the short run. Let $M = 1 0 { , } 0 0 0 ;$ then Figures 3 and 4 show how quickly errors will appear in the long and short run, respectively.

Figure 1 P(t) in the Short Run  
![](/api/attachments/T9W6T469/fulltext/images/848f2f48d7698ffff9c21124d6207b7036a8adc85be7594b3c161a2ff245a0b7.jpg)

Figure 2 Cumulative Error Discovery in the Long Run, Assuming 10,000 Errors in the System  
![](/api/attachments/T9W6T469/fulltext/images/eb08c3156c10b2bb05aa9f5b4d97c19cfcc495c31c48269a9c053233bb1ea026.jpg)

In the short run, none of the 10,000 errors would be discovered if Figure 4 is indicative. Since in practice large numbers of errors are found in software testing and use, any absolute number must be much larger than 10,000 errors in total. Figure 4 shows that cumulative error discoveries accelerate over time. Different perspectives on this acceleration in error discovery are provided in Figures 5 through 6. These confirm the prudence of retiring a system before it reaches 10 to 20 years of age.

These extrapolations based on Adam’s data can be used to forecast how duration of software testing influences the resulting level of errors. Assume that the system will have a useful life of 2,3,4 . . . years. Then the statistic

Figure 3 Cumulative Error Discovery in the Short Run, Assuming 10,000 Errors in the System  
![](/api/attachments/T9W6T469/fulltext/images/938a182d3311c67683f45ba93cfed14c110989ab695b7df26bdaa969c2945956.jpg)

Figure 4 Elapsed Time to Discovery of the i<sup>th</sup> Error Assuming 10,000 Errors in the System  
![](/api/attachments/T9W6T469/fulltext/images/4d442f12f031d29ed58a6aa9a3c441235d706ea763ae40aba9492f5a69412059.jpg)

Figure 5 Rate of Error Discovery in the Long Run, Estimated as Dt • M • (dP(t)/dt)  
![](/api/attachments/T9W6T469/fulltext/images/cdbdc5fe2b99c9fc5acf5dd42b515d33dd46fcecc1d644bd73ed0f8f6b98c6a9.jpg)

Figure 6 Rate of Error Discovery in the Short Run, Estimated as Dt • M • (dP(t)/dt)  
![](/api/attachments/T9W6T469/fulltext/images/219e129e3cc158ef1a238507274193f5f99a2306907cd4db96d67392d4c8226f.jpg)

Figure 7 Portion of Errors That Will Occur That Are Actually Discovered (P( years)/P(software life))  
![](/api/attachments/T9W6T469/fulltext/images/539f138ab2a86864d90f047682ee9fa2b8be4f907f6cc75671d411667ee18847.jpg)

$$
\frac {P [ y e a r s ]}{P [ s o f t w a r e l i f e ]}
$$

provides a measure of the portion of errors that will be detected that would otherwise occur sometime during the useful life of the software. The closer to unity is the test statistic the more comprehensive is the testing. Too long a period of testing will be too costly; too short a time will result in too many costly errors. Figure 7 shows this statistic.

Figure 7 suggests that testing must occur over a substantial portion of the useful life of the system to detect any substantial portion of the total errors which will ever occur. Typically, more than half of a life span must pass prior to detecting one-third of errors. More intense testing during development is likely to increase detection rates. Thus the curves in practice may be steeper than Figure 4 indicates. Nonetheless, the curves suggest that the majority of errors are unlikely to be discovered prior to a system’s release.

The situation may not be as pronounced for software with short life cycles. Short life cycles appear to favor higher rates of detection, but in fact the particular errors detected are less likely to occur during an abbreviated lifetime. It is difficult to conjecture further without making explicit assumptions about how errors are corrected, though postrelease errors may take longer to correct in practice because they may be unanticipated and poorly understood. Error correction itself is a highly error-prone process, and often generates secondary, tertiary, and so forth errors where only one existed previously. Short life cycles are likely to force constrained software development cycles, and are likely to exacerbate the risk from postrelease errors.

## Discussion

The results of the model argue strongly for the adoption of a quality assurance viewpoint. Consistent with product quality assessment literature, we postulate five classes of metrics to measure the quality of software: defect, technical, satisfaction, warranty, and reputation. Defect measures are not available until the system can be run. Control of defects is the main objective of the testing and debugging phase of software development. Technical measures assess that the software code is well structured, that manuals for hardware and software use are adequate, that is complete, correct and up-to-date. Technical measures are available for any system at any time. User satisfaction measures actually describe the value received from using the system. The vendor engages in market studies and beta testing to ascertain user satisfaction. But this data tends to be quite difficult to directly link to development costs, despite the best wishes of the vendor. Warranty costs include technical support and training, and may be one of the most significant costs of software. War ranty costs are influenced by the level of defects, but also by the willingness of users to come forth with complaints, and ability and willingness of the software vendor to accommodate the user. Reputation measures the perceived user satisfaction with the software. Reputation could be significantly different from actual satisfaction for two reasons: (1) because individual users may use only a small fraction of the functions provided in any software package (e.g., consider the fraction of functionality actually used in any word processor), and (2) because marketing and advertising often influences buyer perceptions of software quality more than actual use.<sup>4</sup>

This strongly favors a strategy of continuous process improvement, rather than the test-and-forget strategy that is commonly invoked. Osterweil (1996, p. 1) comments:

All useful software systems evolve continuously, as errors are found and fixed, as requirements change, and as implementation architectures change (eg. because of the emergence of new technologies). Research has shown that costs to evolve software far outweigh costs for initial development. Inability to demonstrate quality can inhibit needed evolution and cause software to become obsolete.

Traditionally, programmers have operated in a politically charged atmosphere in which software errors “must be their fault.” Thus, out of self-protection, their literature has tended to focus on defects that they can formally handle at the time they have responsibility for programming. The politics of affixing blame for software problems has tended to color much of the software testing literature. In response to this tendency to affix blame, IBM has focused on patterns of software “fixes” rather than “causes of error” in order to allow software engineers to focus software quality rather than just debugging (Chillarege et al. 1992)

Software, by its nature, is not deterministic, since much of its operation depends on an uncertain data input stream. In a well designed system, the majority of input will have been specified in the software; data “surprises” even if handled gracefully, are likely to result in noticeable malfunction (i.e., errors) since the system will not know what to do with them. Cost effective testing must be incorporated into the maintenance of the system, since one cannot hold a system back from release for half of its useful life. It also suggests the need for effective feedback loops to report on errors when they occur, and to analyze and correct them quickly.

## References

Adams, E. N., III. 1980. Minimizing cost impact of software defects. IBM Research report RC 8228 (April).

Butler, R. W., G. Finelli. 1993. The infeasibility of quantifying the reliability of life-critical real-time software. IEEE Trans. Software Engrg. 19(1) 13–21.

Bender, D., A. Gahtan. 1998. Evaluating Legal Risks in the “Year 2000 Problem.” White & Case LLP White Paper (August) http:// www.whitecase.com/Year\_2000\_Problem\_memo.html-

Chillarege, R., I. S. Bhandari, J. K. Chaar, M. J. Halliday, D. S. Moebus, B. K. Ray, M-Y. Wong. 1992. Orthogonal defect classification-a concept for in-process measurements. IEEE Trans. Software Engrg. 18(11) 943–56

Geyelin, M. 1994. Faulty software means business for litigators. The Wall Street Journal Jan 21.

Inwood, C. 1993. Formal methods can cut your error rate. Comput. Canada 19(2) 29.

——. 1994. To err is human, to forgive uncommon in IS. Comput. Canada 20(6) 22.

Jones, Capers. 1993. Sick software. Computerworld 27(50) Dec 13 115.

Littlewood, B, L. Strigini. 1993. Validation of ultrahigh dependability for software-based systems. Comm. ACM 36(11) 69–73.

Osterweil, L. 1996. Report from the panel on software quality: Strategic directions. June 14–15 http://laser.cs.umass.edu/sdcr/ report/- 1.

Selby, R. W. 1993. Interconnectivity analysis techniques for error localization in large systems. J. Systems and Software 20(3) 267.
