---
otero_id: 26764
otero_key: "ZS6E3S23"
title: "Measuring Software Engineering Evolution: A Rasch Calibration"
authors: "Sasa Dekleva; David Drehmer"
year: "1997"
journal: "Information Systems Research"
doi: "10.1287/isre.8.1.95"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [129.105.215.146] On: 11 May 2016, At: 00:59 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## HSR Information Systems Research

![](/api/attachments/ZS6E3S23/fulltext/images/5e9cb86109674b65175f65b02a77b4666359ef78672705d8d7d0fa62f5b62271.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Measuring Software Engineering Evolution: A Rasch Calibration

Sasa Dekleva, David Drehmer,

## To cite this article:

Sasa Dekleva, David Drehmer, (1997) Measuring Software Engineering Evolution: A Rasch Calibration. Information Systems Research 8(1):95-104. http://dx.doi.org/10.1287/isre.8.1.95

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article's accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1997 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/ZS6E3S23/fulltext/images/5f8dcdc6a9f3bc4e5576d47d930d02695efffe4ad00c5cbe6eb7ba605fead65b.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Measuring Software Engineering Evolution: A Rasch Calibration

Sasa Dekleva • David Drehmer

College of Commerce, DePaul University, 1 East Jackson Boulevard, Chicago, Illinois 60604-2287
sdekleva@condor.depaul.edu
ddrehmer@wppost.depaul.edu

This investigation provides an empirical scaling of software engineering practices derived from the software process maturity model developed by the Software Engineering Institute of Carnegie Mellon University (Humphrey et al. 1989). An analysis of data collected in an extended software maintenance study has shown that the responses to Humphrey's key software practice items fit the Rasch psychometric model providing an alternative framework in which to understand the software development practices. The Rasch model analysis describes the likelihood of a practice deployment for any level of evolution and provides precise and meaningful measures.

(Measurement and Scaling; Software Process Maturity; Software Process Evolution; Rasch Model; Software Productivity; Software Quality; Risks)

## Introduction

The importance of software reliability is well recognized but its achievement seems more difficult and advances do not parallel those made in hardware engineering and hardware reliability assessment. Various planning, analysis, design, coding, review, testing, quality assurance, and management methods and techniques have been proposed to improve the software engineering process.

At the request of the U.S. Air Force the Software Engineering Institute (SEI) at Carnegie Mellon University developed a Software Capability Evaluation (SCE) to be used by government agencies in judging how capable companies are at developing software (Bollinger and McGowan 1991, Humphrey 1989). According to Anthes (1990) companies view a favorable software process maturity assessment by SEI or its licensees as a competitive advantage, particularly when bidding on federal government jobs. SEI has asserted that a higher maturity level is associated with lower risk, higher productivity and higher quality of the software process (Humphrey et al. 1989). Some initial reports supporting that assertion have been published (Herbsleb et al.

1994). These ratings may have an effect on U.S. Government procurement processes, and may also be used by private industry as a basis for deciding who should be awarded contracts and who should not.

Adapted from Crosby's (1979) quality management maturity grid, SEI defined a software engineering process maturity model containing five maturity levels labeled initial, repeatable, defined, managed, and optimized (Humphrey 1988, Humphrey et al. 1989, Kennett and Koenig 1988).

Each process maturity level conceptually represents a distinctive evolutionary plateau. The framework “models the stages that an organization must go through to establish a culture of engineering excellence. Each model stage lays the foundation on which effective practices for the next level are built” (Humphrey and Curtis 1991, p. 45). The five maturity levels provide the top-level of a multiple layered structure of the software engineering capability model (Humphrey 1988, Weber et al. 1991) and a guideline for the software process improvement. The model has been further elaborated with industrial input and has been released and is currently known as the Capability Maturity Model for Software (CMM) (Paulk et al. 1995). A description of each of these levels may be seen in Table 1.

A questionnaire was developed to make a preliminary assessment of software engineering maturity level (Humphrey and Sweet 1987, Humphrey et al. 1989). Each maturity level was composed of clusters of related practices. These practices were specific policies, procedures, and activities, that represented the link between the maturity model and the questionnaire. Thus, the key practices specified indicators used to generate questionnaire items.

Drehmer and Dekleva (1992) presented an empirically-determined interpretation of these questionnaire items. That study was limited to items associated with the repeatable (level 2) and defined (level 3) SEI maturity levels. The present study extends the scope of Drehmer and Dekleva (1992) to determine whether the key questionnaire items form a cumulative hierarchy necessary to establish a pattern of growth in terms of actual software engineering practices. The relationships between the Humphrey et al. (1989) and Drehmer and Dekleva (1992) frameworks are also examined. Item response theory, and particularly the Rasch model, provides an ideal mechanism for representing the structure of scale data (Rasch 1960, 1980; Wright 1977; Wright and Masters 1982; Wright and Stone 1979).

## Method

## Analysis

The process of any measurement involves the comparison of a stimulus to a set of standards. In this case the stimulus is the respondent's software engineering practice and the standards are questionnaire items. Traditionally, a simple count of questionnaire items endorsed has been assumed to provide a measure of the strength of the phenomenon being assessed.

It turns out, however, that the count of endorsed items is a sufficient indicator only under some fairly restrictive conditions. To convert this count to a measure it matters which items have been endorsed. We would expect that items representing evolutionary stages already passed by subjects would be endorsed while items representing evolutionary levels not yet reached would be rejected, at least in a probabilistic sense. This modern approach to measurement owes its logic and underlying mathematics to Georg Rasch. The Rasch model is not a data-analytic model based on data covariance structures, but rather a definition of the necessary conditions for measurement.

Table 1 SEI Software Process Maturity Model

<table><tr><td>Level</td><td>Description</td></tr><tr><td>Initial</td><td rowspan="2">The organization lacks sound management practices. Schedules, budgets, functionality, and system quality are unpredictable. The success of projects depends on heroic commitments of individuals rather than organizational capability.</td></tr><tr><td>Level 1</td></tr><tr><td>Repeatable</td><td rowspan="2">Project standards and management techniques are implemented. Project planning and management is based on past experience enabling organizations to repeat successful practices used on previous projects. The Repeatable maturity level provides a stable, managed, and controllable environment with realistic project plans. Project managers track costs, schedules, and functionality. They are able to identify problems in meeting plans and commitments.</td></tr><tr><td>Level 2</td></tr><tr><td>Defined</td><td rowspan="2">Defined level is achieved by the organizations with standard and documented process for both software engineering and management. A group for permanent evaluation and improvement of software engineering and management process is organized, training program for staff and managers is implemented, and software quality is tracked. Both projects and processes are stable; costs, schedules, functionality, and quality are under control.</td></tr><tr><td>Level 3</td></tr><tr><td>Managed</td><td rowspan="2">The organizations at the Managed maturity level collect quantitative productivity and quality measurements in an organization-wide process database. The well-defined and consistent metrics enable the evaluation of processes and products with the goal to narrow the variation and manage the effect of learning curve of a new application domain. The ability of operating within measurable limits enables level four organizations to predict process and product quality within the quantitative bounds.</td></tr><tr><td>Level 4</td></tr><tr><td>Optimizing</td><td rowspan="2">Organizations at the Optimizing level are focused on process improvement. Statistical evidence is used to advance the existing process and to identify best new methods and technologies with the goal of preventing the defects. Defects are studied and processes strengthened to avoid recurrence of known types of defects and disseminate lessons learned throughout the organization.</td></tr><tr><td>Level 5</td></tr></table>

The fundamental idea behind our application of the Rasch model is that each SEI key questionnaire item represents a particular level of software engineering evolution, $\delta_{\iota}$ . When an organization endorses an item, that organization is stating that the evolution of its own software engineering practices exceeds the level described by the item. If we conceptualized a continuum from low to high evolution, it would be possible to locate both items, $\delta_{\iota}$ , and organizations, $\beta_{\nu}$ , on the same scale. This is analogous to using a ruler for making physical measurements: an object is compared to calibrated markings ( $\delta_{\iota}$ ) of length on a stick to determine its length ( $\beta_{\nu}$ ).

If the items were ordered from low to high evolution, one would expect that an organization would be located in a transition zone between places where all items had been endorsed and where no items had been endorsed (see Figure 1).

The difference between the item's evolution level, $\delta_{\nu}$ , and the organization's evolution, $\beta_{\nu}$ , should describe the odds that the $\iota$ th item will be endorsed by the $\nu$ th organization.

Consider a matrix, X, that consists of responses to questionnaire items where columns are items and rows represent organizations. Each cell of the matrix contains a “1” if the item is endorsed by the organization and a zero, otherwise. Let $P(X_{\nu i}=1|\beta_{\nu},\delta_{i})$ represent the probability of endorsing the ith item by the $\nu$ th organization. Then $1-P(X_{\nu i}=1|\beta_{\nu},\delta_{i})$ would represent the probability of not endorsing the item. One often used formulation for expressing such probability data is the odds ratio, the ratio of endorsements to nonendorsements, i.e., $P/(1-P)$ (subscripts omitted). The Rasch model specifies that this odds ratio should govern the differences between the item's calibration and the organization's measure. To create an equal interval and linear scale in item calibration units, the natural logarithm of the odds, a logit, was set equal to the difference between an item's difficulty, $\delta_{i}$ , and a respondent's ability, $\beta_{\nu}$ , as expressed in Eq. (1):

$$
\ln \left(\frac {P _ {\nu \iota}}{1 - P _ {\nu \iota}}\right) = \beta_ {\nu} - \delta_ {\iota}.\tag{1}
$$

The expected probability of endorsing an item may be derived from Eq. (1) and is a simple function of abil-

Figure 1 Response Pattern Zones

$$
\begin{array}{c c c c c c c c c c c c c c c c c c c c c c c} \beta & & & & & & & & & & & & & & & & \\ 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 0 & 1 & 0 & 0 & 1 & 1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ \hline \text { endorsement } & \text { transition } & \text { rejection } \\ \hline \text { low } & \text { Evolution } & \text { high } \end{array}
$$

ity and item difficulty as shown in Eq. (2). This is the common expression for the Rasch model.

$$
P (X _ {\nu \iota} = 1 | \beta_ {\nu} \delta_ {\iota}) = \frac {\exp (\beta_ {\nu} - \delta_ {\iota})}{1 + \exp (\beta_ {\nu} - \delta_ {\iota})}.\tag{2}
$$

An organization's location on the variable should indicate how far along that variable particular scaled items should be endorsed. Similarly, an item's location on the variable should determine in a probabilistic sense which organizations will endorse it. When an assessment of item and organization fit indicates congruence with this model, strong inferences about construct validity and measurement precision are possible.

One feature that distinguishes the Rasch model from other item response theory (IRT) models is the separability of item and organization parameters. Rasch (1960, 1980) and others have shown that the Rasch model is the only logistic model that leads to algebraically independent estimates for organization and item parameters. This leads to very desirable features in that it is the only method that provides item calibrations that are invariant across organizations and organization measurements that are invariant across items (Rasch 1960, 1980; Wright and Masters 1982; Wright and Stone 1979). McRae (1991, p. 423) quipped “The appropriateness of this specification is perhaps most obvious when considering the failure to achieve it in physical measurement: The yardstick which expands with increases in temperature is not a useful tool for comparing the heights of Athabaskan and Navajo Native Americans. One can easily imagine the fanciful theories that users of this yardstick would develop to account for the greater (sic) height of the Navajo.”

Rasch's separability theorem also leads to sufficient statistics for both person and item parameter estimates. This means that the estimates extract all of the relevant information from the data. Any residual differences between the observed data and that predicted by the model are known to be independent and can therefore be used to test the validity of the model.

## Subjects

Two cohorts of practicing software maintainers volunteered to participate in this study. The first cohort consisted of 44 surviving respondents (from an original base of 62) who were members of a third-round Delphi panel in a larger study (Dekleva 1992). The second cohort of subjects consisted of 39 respondents who completed a mail survey designed specifically for this investigation.

Each subject was an experienced software maintainer with an average of 15 years in information systems of which 11 years has been spent in software maintenance or management of maintenance and therefore was qualified as an appropriate subject. The first cohort was solicited from persons who attended the 1990 and 1991 Software Management Association professional conferences and the second cohort was attendees of the 1992 meeting of the same conference. Each indicated a high level of maintenance problem awareness and interest in maintenance in general. With the exception of one participant from Australia and one from Great Britain in the first cohort, all were from the United States or Canada.

## Instruments

The instrument consisted of 38 items described as “the key questions” or “asterisked questions” to determine the software engineering maturity levels “repeatable, level 2” (items 1–12), “defined, level 3” (items 13–26) and “managed, level 4” (items 27–38) (Humphrey and Sweet 1987). The first 26 items were presented to the first cohort as part of a third round Delphi survey as a separate section with the following heading: “The following are supplementary questions which should enable us to provide important additional feedback. The questions investigate your MIS department in general, not just the maintenance function.”

The second cohort completed a mailed survey consisting of 61 items, 38 of which were key items representing the SEI repeatable, defined and managed maturity thresholds. Since no organization was believed to pass the optimizing threshold, none of these items were used. It was the belief that the practices defined by these items would rarely occur and would not be revealing of the underlying structure of process maturity. The full text of the 38 survey items is presented in the appendix to this paper.

Each item from the questionnaire was coded "1" if it was endorsed by the respondent and coded "0" if it was not endorsed. Rasch item calibrations were obtained from the BIGSTEPS, Version 2.31 (Wright and Linacre 1992).

## Results

A preliminary analysis was undertaken to determine whether the two cohorts were sufficiently similar to warrant pooling them to obtain more stable estimates of item locations than could be done with each sample separately. The 25 items from the SEI Software Process Maturity Scale (Humphrey et al. 1989) used by Drehmer and Dekleva (1992) were calibrated using BIGSTEPS, Version 2.31 (Wright and Linacre 1992) for each cohort separately. The locations (MEASURE) under each analysis for corresponding items were significantly correlated with each other $r(25)=0.847, p<0.001$ . The two cohorts were then pooled to form one sample and the 25 items were recalibrated. The correlations of item locations for each cohort and the combined sample were $r(25)=0.966 (p<0.001)$ and $r(25)=0.952 (p<0.001)$ , respectively. The reliability estimate of item calibrations was 0.95 based on the pooled sample.

Table 2 provides the final Rasch estimate of the item's (software engineering practice) location (MEASURE) on the underlying evolution variable. The measure of location is the primary information of interest in this analysis. Every measure is an estimate and the precision of that estimate is described by its standard error (ERROR). An additional set of fit statistics (INFIT and OUTFIT) describes how well the data fit the Rasch specification. These statistics answer the question about whether the item belongs in this construct.

If one conceptualizes a variable, a particular respondent would be expected to have a zone of endorsement at one end of the scale, a zone of rejection at the other end, and a zone of transition in the middle. Two fit statistics are provided and each assesses a different character of possible misfit. Both of these statistics are presented in their standardized form. OUTFIT is an approximately normally-distributed

Table 2 Calibrations, Standard Errors and Fit Statistics of Evolution Scale

<table><tr><td colspan="2">Item &amp; Level*</td><td>Measure</td><td>Error</td><td>Infit</td><td>Outfit</td><td>Key Software Practices</td></tr><tr><td></td><td>38</td><td>9.18</td><td>1.45</td><td colspan="2">Max. estim.</td><td>Design errors projected</td></tr><tr><td></td><td>27</td><td>7.64</td><td>.77</td><td>-.2</td><td>-.2</td><td>Process metrics database</td></tr><tr><td></td><td>32</td><td>7.64</td><td>.77</td><td>-.2</td><td>-.2</td><td>Code, test errors projected</td></tr><tr><td>15</td><td></td><td>7.54</td><td>.45</td><td>.5</td><td>1.2</td><td>Training review leaders</td></tr><tr><td>25</td><td></td><td>7.08</td><td>.41</td><td>-.5</td><td>-.7</td><td>SQA sample verification</td></tr><tr><td>14</td><td></td><td>6.94</td><td>.37</td><td>1.2</td><td>1.1</td><td>Developers training required</td></tr><tr><td></td><td>37</td><td>6.75</td><td>.58</td><td>-.6</td><td>-.4</td><td>Forecast remaining errors</td></tr><tr><td>7</td><td></td><td>6.63</td><td>.35</td><td>.9</td><td>-.1</td><td>Profiles of software size</td></tr><tr><td>26</td><td></td><td>6.49</td><td>.34</td><td>-.1</td><td>-.3</td><td>Adequacy of regression test</td></tr><tr><td></td><td>30</td><td>6.44</td><td>.54</td><td>-.3</td><td>-.2</td><td>Review efficiency analyzed</td></tr><tr><td></td><td>29</td><td>6.17</td><td>.50</td><td>-.4</td><td>-.2</td><td>Test coverage measured</td></tr><tr><td></td><td>36</td><td>6.12</td><td>.50</td><td>-.9</td><td>-.6</td><td>Design and code coverage</td></tr><tr><td>21</td><td></td><td>5.48</td><td>.29</td><td>1.3</td><td>.3</td><td>Compliance with standards</td></tr><tr><td></td><td>33</td><td>5.33</td><td>.42</td><td>-1.2</td><td>-.2</td><td>Error cause analysis</td></tr><tr><td></td><td>35</td><td>5.00</td><td>.40</td><td>.9</td><td>.4</td><td>Software process assessed</td></tr><tr><td>4</td><td></td><td>4.95</td><td>.27</td><td>.6</td><td>-.1</td><td>Size estimated</td></tr><tr><td></td><td>34</td><td>4.84</td><td>.40</td><td>-.6</td><td>-.8</td><td>Code review standards</td></tr><tr><td>2</td><td></td><td>4.63</td><td>.27</td><td>1.4</td><td>1.8</td><td>Configuration control</td></tr><tr><td>19</td><td></td><td>4.38</td><td>.27</td><td>.1</td><td>.2</td><td>Design review items tracked</td></tr><tr><td>20</td><td></td><td>4.37</td><td>.27</td><td>.2</td><td>.0</td><td>Code review items tracked</td></tr><tr><td></td><td>31</td><td>4.36</td><td>.39</td><td>-.3</td><td>-.2</td><td>Design review data analyzed</td></tr><tr><td>6</td><td></td><td>4.29</td><td>.27</td><td>-.7</td><td>-1.0</td><td>Software cost estimated</td></tr><tr><td></td><td>28</td><td>4.23</td><td>.38</td><td>-.6</td><td>-.4</td><td>New technology intro. managed</td></tr><tr><td>5</td><td></td><td>4.21</td><td>.27</td><td>.7</td><td>.0</td><td>Software development scheduled</td></tr><tr><td>17</td><td></td><td>4.06</td><td>.27</td><td>1.0</td><td>.3</td><td>Standards documented, used</td></tr><tr><td>3</td><td></td><td>3.76</td><td>.28</td><td>1.0</td><td>1.7</td><td>Formal management review</td></tr><tr><td>10</td><td></td><td>3.51</td><td>.28</td><td>.6</td><td>.0</td><td>Managers sign off</td></tr><tr><td></td><td>16</td><td>3.45</td><td>.28</td><td>-.1</td><td>1.7</td><td>Development standardized</td></tr><tr><td></td><td>23</td><td>3.40</td><td>.29</td><td>-2.3</td><td>-1.7</td><td>Design changes controlled</td></tr><tr><td></td><td>24</td><td>2.93</td><td>.31</td><td>.4</td><td>-.4</td><td>Code reviews conducted</td></tr><tr><td>11</td><td></td><td>2.84</td><td>.31</td><td>-2.1</td><td>-1.8</td><td>Requirements change control</td></tr><tr><td></td><td>22</td><td>2.64</td><td>.32</td><td>.0</td><td>-.6</td><td>Design reviews conducted</td></tr><tr><td>12</td><td></td><td>1.93</td><td>.37</td><td>.7</td><td>.0</td><td>Code changes controlled</td></tr></table>

\* Items 1–12 were SEI Level 2 items, items 13–26 were Level 3, and items 27–38 were Level 4.

index based on a sum of squared residuals and is particularly sensitive to outlying values (responses located away from the center). Its expected value is zero. Negative OUTFITs indicate a response pattern that is more stable and generally a better-fitting pattern than would be expected while positive OUTFITs indicate a more random pattern of responses than would be expected from the model in the endorsement and rejection zones. INFIT provides an alternative fit assessment that is more sensitive to inlying observations and is relatively insensitive to the effects of outliers. INFIT is particularly sensitive to the pattern of responses in the zone of transition. INFIT is also approximately normally distributed with an expectation of zero and a standard deviation of one.

INFITs or OUTFITs greater than two would not be expected more than 5% of the time if the data conforms to the model. Five items were deleted due to a lack of fit; two subjects appeared to provide response patterns considerably different from others in the sample and each was eliminated in order to estimate an uncontaminated location for each remaining item.

Item 13, “There is a software engineering process group function,” was discarded from our final version of the scale due to a lack of fit. It is believed that the phrase “software engineering process group” was ambiguously understood by some respondents. Item 9, “Senior management has a mechanism for the status review of software development projects” did not fit the Rasch model, though it was very frequently endorsed. Since it seemed to add very little to understanding the ordering of the items, and because of its lack of fit, it too was eliminated. Two items dealing with statistical reporting, “Statistics on software design errors are gathered” and “Statistics on software code and test errors are gathered” were also found to not represent the underlying construct described by the rest of the items. These were also eliminated as was “The Software Quality Assurance (SQA) function has a separate management reporting channel.” The reliability of the final scale of 33 items was 0.93.

## Discussion

The SEI definition of software process maturity levels was based on contributions, inputs and reviews from over 500 practicing software engineers and project managers. The items numbered 1–12 were used by SEI to demarcate the transition from level 1 to level 2, items numbered 13–26 differentiate level 2 from level 3, while the remainder of the items were used to distinguish companies transitioning from level 3 to level 4.

Table 2 displays the items in the calibration order produced by the present analysis. The box and whisker display in Figure 2 presents the distribution of these item calibrations for items in each SEI level. The box marks the interquartile range of the items and the whiskers denote the range of the tails of the distributions. An examination of these diagrams reveals generally increasing calibrations along the maturity variable for each succeeding level. This would support the notion that the actual practices of organizations follow the prescribed practices described by Humphrey (1988). However, the heterogeneous item clustering within a maturity level and the large overlap among the levels indicate that the use of practices in the industry does not precisely follow the optimal path described by Humphrey. The present investigation has described evolution in terms of actual software engineering practices. The CMM is predicated on an optimal ordering that transcends natural evolutionary practice captured by the Rasch analysis.

![](/api/attachments/ZS6E3S23/fulltext/images/bfeca60541f933e27b9b8c6881b4e48be9068f481ee9d4343bc595fe4afea538.jpg)

If one examines the continuity of content of items along the scale described by the Rasch analysis, one might speculate that the clustering of items represents a continuous progression. One can entertain the notion that a meaningful growth hierarchy is represented by these items, particularly since the Rasch model requires that in order to endorse a higher item, there must be a high probability that lower level items were also endorsed. A joint distribution of items and respondents is given in Figure 3.

## Stage A: Reviews and Change Control

An examination of the item content along the calibrated evolution scale on the ordinate axis should reveal how practices change as the software engineering evolves. Consistent with Drehmer and Dekleva (1992), the items with the lowest calibrations describe practices of

Figure 3 Evolution Map of Organizations and Key Software Practices

<table><tr><td colspan="5">Rasch Evolution</td></tr><tr><td>Organizations</td><td></td><td colspan="3">Key software practices</td></tr><tr><td></td><td>8.0</td><td>Design errors projected</td><td></td><td></td></tr><tr><td></td><td></td><td>Training review leaders</td><td>Code, test errors projected</td><td>Process metrics database</td></tr><tr><td>XX</td><td>7.0</td><td>SQA sample verificationDevelopers training required</td><td></td><td></td></tr><tr><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>XXXX</td><td></td><td>Forecast remaining errorsProfiles of software size</td><td></td><td></td></tr><tr><td></td><td></td><td>Adequacy of regression test</td><td>Review efficiency analyzed</td><td></td></tr><tr><td>XXX</td><td></td><td>Design and code coverage</td><td>Test coverage measured</td><td></td></tr><tr><td>X</td><td>6.0</td><td></td><td></td><td></td></tr><tr><td>XX</td><td></td><td></td><td></td><td></td></tr><tr><td>XXXX</td><td></td><td>Compliance with standardsError cause analysis</td><td></td><td></td></tr><tr><td>XX</td><td></td><td></td><td></td><td></td></tr><tr><td>XXXXX</td><td>5.0</td><td>Size estimatedCode review standards</td><td>Software process assessed</td><td></td></tr><tr><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>XXX</td><td></td><td></td><td></td><td></td></tr><tr><td>XXXXXXX</td><td></td><td>Configuration control</td><td></td><td></td></tr><tr><td>XXXXX</td><td></td><td>Code review items tracked</td><td>Design review items tracked</td><td>Design review data analyzed</td></tr><tr><td>X</td><td></td><td>Software cost estimated</td><td>New technology intro. managed</td><td></td></tr><tr><td>XXX</td><td></td><td>Software development scheduled</td><td></td><td></td></tr><tr><td>XXXXX</td><td>4.0</td><td>Standards documented, used</td><td></td><td></td></tr><tr><td>XX</td><td></td><td></td><td></td><td></td></tr><tr><td>XX</td><td></td><td>Formal management reviewManagers sign off</td><td></td><td></td></tr><tr><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>XXXX</td><td></td><td>Design changes controlled</td><td>Development standardized</td><td></td></tr><tr><td>XX</td><td></td><td></td><td></td><td></td></tr><tr><td>XXXXX</td><td>3.0</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>Code reviews conducted</td><td>Requirements change control</td><td></td></tr><tr><td>X</td><td></td><td>Design reviews conducted</td><td></td><td></td></tr><tr><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>XX</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>2.0</td><td></td><td></td><td></td></tr><tr><td>X</td><td></td><td>Code changes controlled</td><td></td><td></td></tr><tr><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>XXX</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>1.0</td><td></td><td></td><td></td></tr><tr><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>XX</td><td>0.0</td><td></td><td></td><td></td></tr><tr><td>Organizations</td><td></td><td colspan="3">Key software practices</td></tr></table>

performing design and code reviews and the use of mechanisms for controlling code, requirements, and design changes. The establishment of these controls lifts an environment to the first stage of software process evolution and occupies measures from zero through about 3.4 logits (log odds units).

Stage B: Standard Process and Project Management It appears that the next level focuses on standardization of software development process and implementation of project management practices. The two efforts seem to be simultaneous. Soon after the managers start signing off and reviewing before making contractual commitments, formal scheduling and estimating procedures are implemented. Similarly, soon after a standard software process is realized, a need for a mechanism used for managing and supporting the introduction of new technologies is recognized. This stage runs from about 3.4 to 4.3 logits.

## Stage C: Review Management and Configuration Control

The practices then smoothly shift to focus on managed outcomes of the reviews and information produced when standards were not fully met. Review data are analyzed, action items from code and design reviews are tracked to closure, and code review standards are applied. In addition, software configuration control becomes a function practiced in every project and a formal procedure for software size estimation is introduced. Stage C spans from 4.3 to just under 5 logits.

## Stage D: Software Process Improvement

This represents the endpoint of the middle evolution stages. These stages generally deal with the analysis and improvement of software process and include stages B, C and D. Perhaps the evolutionary push was to develop a process that produced fewer action items. The process is systematically being improved, analysis of errors is extended to identify related process inadequacies, and a mechanism is put in place to ensure compliance with the software process standards. It appears that a standard software process is implemented at Stage B and that this process is systematically analyzed and perfected at evolution Stage D, which runs from 5 to 5.5 logits on this empirically derived scale.

## Stage E: Management of Review and Test Coverages

A noticeable gap between Stages D and E separates the middle from the higher evolution stages where advanced engineering and management practices are gradually implemented. At Stage E, the coverages of design, code, and test reviews are measured and recorded. In other words, reviews are not only practiced but their coverage becomes systematically observed. This indicates that the significance of reviews becomes apparent at this point of evolution and data accumulated at this level enable further progression to Stage F. This stage occupies locations from about 6 logits to 6.2 logits on the evolution scale.

## Stage F: Analysis of Measurements

Data accumulated at the lower level now enable the introduction of review efficiency analysis for every project, while an errors database enables assessments of remaining errors distribution. A mechanism is also implemented to assure the adequacy of regression testing. The scope of measurements is further expanded. For example, maintenance of software size profiles for each configuration is initiated. The base of this stage is located at about 6.4 logits and extends to about 6.8 logits.

## Stage G: Advanced Practices

Some of the practices at this level are above the evolution level of the most mature organizations in our sample. Six practices describing this level represent two issues. It comes as a surprise that an organization needs to progress in its software process evolution all the way up to this level to realize that training should be required. Perhaps the analysis at the preceding level helps managers recognizing this need. The other issue is further extension in quality assurance practices. For example, the sampling adequacy for quality assurance is insured and code, test, and design errors are projected and analyzed. Finally, a process measurements database is established at this level and process measurements are gathered for all projects. This activity seems to prepare an organization to climb to the process optimization evolution level and possibly other higher levels not investigated in this study. Anything above 6.9 logits is considered to belong to Stage G.

David Andrich (1988, p. 10) has pointed out that “devising a measuring instrument is as important in what it teaches about the variable as are the subsequent acts of measurement using the instrument.” For example, management may have been asked to sign off on a project (item 10) without an evaluation against schedules and estimations (items 4, 5 and 6). Similarly, scheduling appears at a lower level of evolution than estimation. At first thought this seems unreasonable in that management is put in the impossible position of taking responsibility for a project without any means of evaluating the consequences of its actions. However, it might point out the evolutionary need to develop the tools for such an evaluation showing a higher level of evolution. It might also show that a fundamental change in what tasks are done has not changed, but how that task is accomplished may change considerably throughout the evolution cycle.

The “evolutionary necessity” hypothesis is also illustrated by the examination of review processes. The lowest level asks whether code and design reviews are conducted. In an apparent effort to improve the effectiveness of reviews, outcome data are analyzed and action items are tracked. This reveals the need to consistently apply review standards which, as evolution progresses even further, enables the analysis of the review efficiency. Surprisingly but not unusually, the highest level of evolution must apparently be reached before the need for training of design and code review leaders is recognized. It appears that each step represents an iterative refinement advancing an implemented procedure. Each step stabilizes variability of lower-level steps.

## Conclusions

A picture of the evolution of software engineering process has been identified by fitting item responses to the Rasch model. Using this new definition, a meaningful measure for software engineering evolution may be made that not only makes conceptual sense, but also is supported by empirical data.

There is a pattern that emerges in the evolutionary process, a pattern of consecutive reengineering of software engineering practices. New practices appear to have been developed to help earlier implemented practices work more effectively. The pattern is one of correcting inefficiency and ineffectiveness.

Implementing a process improvement may not maximize its potential yield. This research suggests that to make an improvement functional, it would be useful to determine what other practices are needed to support the process change. For example, the adoption of reviews (items 3, 24) before the estimation and scheduling (items 5, 6) leads to ineffective review procedures. An anonymous reviewer suggested "In a haste of trying to rush to an unachievable delivery date, the developers do not have time to read the design documents or code before coming to the review meeting and therefore they miss many of the defects they would have caught had they have the luxury of an adequately planned schedule." Similarly, reviews that identify problem lists may be ineffective until and unless a management process is established to follow-up on the results of, and track the problem list generated in the reviews (items 19, 20, 31).

The respondents in this study come from environments ranging from scientific programming to the development of business systems to operating systems. While these encompass a very large proportion of computer systems development tasks, still others with unique methodologies exist. Questions remain unanswered as to whether this model is applicable to projects using rapid prototyping, object orientation, implementation of pre-written software, projects that are predominately artificial intelligence driven, or those which come from very small-project working environments. These may represent revolutionary approaches that would seem discontinuous in the current evolutionary framework. $^{1}$

$^{1}$ The authors wish to thank the reviewers and editors for their thoughtful comments and guidance. This research was supported, in part, by grants from the Quality of Instruction Council, University Research Council, and School of Accountancy, DePaul University, Chicago, Illinois. A prior version of this paper was presented to the International Conference on Information Systems, Orlando, FL, Dec. 1993.

## Appendix

Item Text for Software Process Evolution Scale in Calibration Order

38. Are design errors projected and compared to actual?

27. Has a managed and controlled process database been established for process metrics data across all projects?

32. Are code and test errors projected and compared to actual?

15. Is a formal training program required for design and code review leaders?

25. Is a mechanism used for verifying that the samples examined by Software Quality Assurance are truly representative of the work performed?

14. Is there a required software engineering training program for software developers?

37. Is the error data from code reviews and tests analyzed to determine the likely distribution and characteristics of the errors remaining in the product?

7. Are profiles of software size maintained for each software configuration item, over time?

26. Is there a mechanism for assuring the adequacy of regression testing?

30. Is review efficiency analyzed for each project?

29. Is test coverage measured and recorded for each phase of functional testing?

36. Are design and code review coverages measured and recorded? 21. Is a mechanism used for ensuring compliance with the software engineering standards?

33. Are analyses of errors conducted to determine their process related causes?

35. Is a mechanism used for periodically assessing the software engineering process and implementing indicated improvements?

4. Is a formal procedure used to make estimates of software size?
34. Are code review standards applied?

2. Is there a software configuration control function for each project that involves software development?

19. Are the action items resulting from design reviews tracked to closure?
20. Are the action items resulting from code reviews tracked to closure?

31. Are the review data gathered during design reviews analyzed?
6. Are formal procedures applied to estimating software development cost?

28. Is a mechanism used for managing and supporting the introduction of new technologies?

5. Is a formal procedure used to produce software development schedules?

17. Does the software organization use a standardized and documented software development process on each project?

3. Is a formal procedure used in the management review of each software development prior to making contractual commitments?

10. Do software development first-line managers sign off on their schedules and cost estimates?

16. Does the software organization use a standardized software development process?

23. Is a mechanism used for controlling changes to the software design?
24. Are software code reviews conducted?

11. Is a mechanism used for controlling changes to the software requirements?

22. Are internal software design reviews conducted?

12. Is a mechanism used for controlling changes to the code? (Who can make changes and under which circumstances?)

XXX Does senior management have a mechanism for the regular review of the status of software development projects?

XXX Is there a software engineering process group function?

XXX Are statistics on software design errors gathered?

XXX Are statistics on software code and test errors gathered?

XXX Does the Software Quality Assurance (SQA) function have a management reporting channel separate from the software development project management?

## References

Andrich, D., Rasch Models for Measurement, Sage, Newberry Park, CA, 1988.

Anthes, G. H., "Software Developers Climb onto Assessment Bandwagon," Computerworld, October 8, 1990, 106–107.

Bollinger, T. B. and C. McGowan, "A Critical Look at Software Capability Evaluations," IEEE Software, 8, 4 (1991), 25–41.

Crosby, P. B., Quality is Free, McGraw-Hill, New York, 1979.

Dekleva, S., "Delphi Study of Software Maintenance Problems," in Proc. Conf. on Software Maintenance 1992, IEEE Computer Society Press, Los Alamitos, CA, 1992, 10–17.

Drehmer, D. E. and S. Dekleva, "Calibration of Software Engineering Maturity," paper presented at the Academy of Management Meeting, Las Vegas, August 1992.

Herbsleb, J., A. Carleton, J. Rozum, J. Siegel, and D. Zubrow, "Benefits of CMM-Based Software Process Improvement: Initial Results," Technical Report CMU/SEI-94-TR-13, Carnegie-Mellon University, Software Engineering Institute, Pittsburgh, PA, 1994.

Humphrey, W. S., "Characterizing the Software Process: A Maturity Framework," IEEE Software, 5, 3 (1988), 73–79.

—, D. H. Kitson, and T. C. Kasse, "The State of Software Engineering Practice: A Preliminary Report," Technical Report CMU/SEI-89-TR-1 ESD-TR-89-01, Carnegie-Mellon University, Software Engineering Institute, Pittsburgh, PA, 1989.

— and W. Curtis, "Comments on 'A Critical Look,' IEEE Software, 8, 4 (1991), 42–46.

— and W. Sweet, "A Method for Assessing the Software Engineering Capability of Contractors," paper CMU/SEI-87-TR-23, ADA187230, Carnegie Mellon University, Software Engineering Institute, Pittsburgh, PA, 1987.

Kennett, R. S. and S. Koenig, "A Process Management Approach to SQA (Software Quality Assurance)," Quality Progress, 21, 11 (1988), 66–70.

McRae, J. E., "Rasch Measurement and Differences Between Women and Men in Self Esteem," Social Science Research, 20 (1991), 421–436.

Paulk, M. C., B. Curtis, and M. B. Chrissis, "Capability Maturity Model for Software," Paper CMU/SEI-91-TR-24, Carnegie Mellon University, Software Engineering Institute, Pittsburgh, PA, 1991.

—, C. V. Weber, B. Curtis, and M. B. Chrissis, The Capability Maturity Model: Guidelines for Improving the Software Process. Addison Wesley, Reading, MA, 1995.

Rasch, G., Probabilistic Models for Some Intelligence and Attainment Tests, Danmarks Paedogogiske Institut, Copenhagen, 1960, (University of Chicago Press, Chicago, IL, 1980).

Weber, C. V., M. C. Paulk, C. J. Wise, and J. V. Withey, "Key Practices of the Capability Maturity Model," Technical Report CMU/SEI-91-TR-00, Carnegie-Mellon University, Software Engineering Institute, Pittsburgh, PA, 1991.

Wright, B. D., "Solving Measurement Problems with the Rasch Model," J. Educational Measurement, 14, 2 (1977), 97–116.

— and J. M. Linacre, BIGSTEPS: Rasch Analysis for all Two-Facet Models, Mesa Press, Psychometric Laboratory, University of Chicago, Chicago, IL, 1992.

— and G. N. Masters, Rating Scale Analysis, Mesa Press, Chicago, IL, 1982.

— and M. H. Stone, Best Test Design, Mesa Press, Chicago, IL, 1979.

John L. King, Associate Editor. This paper was received on August 1, 1994, and has been with the authors $6\frac{1}{2}$ months for 3 revisions.
