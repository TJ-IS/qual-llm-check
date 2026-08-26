---
otero_id: 22332
otero_key: "VG98ZR7K"
title: "IT process designs for improving information quality and reducing exception handling: A simulation experiment"
authors: "Diane M. Strong"
year: "1997"
journal: "Information & Management"
doi: "10.1016/s0378-7206(96)01089-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# IT process designs for improving information quality and reducing exception handling: A simulation experiment $^{1}$

Diane M. Strong $^{*}$

Worcester Polytechnic Institute, Department of Management, 100 Institute Road, Worcester, MA 01609, USA

## Abstract

Exceptions are cases that cannot be handled adequately in automated information processes (IP); but they can significantly affect IP performance. This research develops a model that captures the exception handling activities required in operational-level information processes. The model is sufficiently general to allow evaluation of the performance of information flow processes employing any combination of people and information technologies (IT). It is used to evaluate alternative designs for using IT to improve the quality of the information produced from IP while reducing the resources required for exception handling. In two simulation experiments using the model, advanced IT improved information quality significantly. They did not, however, always reduce flow time and human resource time. These results provide support for justifying the use of advanced IT in organizations for information quality improvement.© 1997 Elsevier Science B.V.

Keywords: Information quality; Exceptions; Exception handling; Process design; Simulation

## 1. Introduction

This paper considers relationships among information technology (IT) capabilities and the performance of complex operational-level information processes, namely, those that generate the information needed to run the core functions of a firm. These processes generally involve high volume transactions for processing orders, customers, inventory, account balances, etc. Much of this is relatively routine and has been automated using IT.

Despite their apparently routine nature, exceptions occur frequently and exception handling is a major component of their work [10, 17, 27, 29]. Exception handling involves manual 'work arounds' to handle cases that IT does not adequately handle or to adjust inputs to an acceptable form. Here, we define exceptions as cases that require special handling by people; that is, cases where the IT does not include enough logic or rules.

The presence of exceptions adversely affects process performance, specifically productivity, quality, and timeliness. Finding and handling exceptions requires time and human resources, reducing the timeliness of process outputs and human productivity. Their presence also leads to poor quality outputs when legitimate special cases or processing errors are not recognized and adequately handled. The finding and handling of exceptions is an information quality control activity. Unlike errors or product defects in manufacturing processes, exceptions cannot necessarily be eliminated because they include legitimate special cases.

Advanced IT and alternative process designs could potentially address these problems and improve process performance significantly $[7, 12]$ . Radical change to operational-level, revenue-generating processes, however, is risky, since they must function daily to ensure the revenue stream. Furthermore, expected performance improvements from new IT may not materialize for several reasons.

\- More advanced IT will not eliminate all exceptions [25, 28].

\- Firms are dynamic and organizational processes change [5, 23].

\- The overall effect of new IT may be small because other process activities also contribute to overall performance [11, 19].

To investigate advanced IT effects within alternative designs, we develop a model that captures exception-handling. We use this model to evaluate IT-based process design alternatives to improve information quality, productivity, and timeliness. This model provides an approach for analyzing the impacts of IT in operational-level information processes, thus reducing some of the risks associated with installing new IT and changing process designs.

## 2. Model

## 2.1. Research approach

The model represents an information process as an activity network with quality and time parameters for each activity. To illustrate its use as a simulation tool, the model is instantiated for an existing organizational process by specifying the structure of the activity network and the parameter values for each activity. This model is the basis for two experiments comparing design alternatives that vary human resource capabilities, locations for information quality controls, and IT capabilities. Three process performance measures: quality of the information, flow time through the process, and human resource requirements, are computed from the instantiated model using simulation. Figure 1 summarizes our research approach and the variables studied.

## 2.2. An example of the model

We start with an example before specifying the model in detail. Consider the activities for producing a product configuration, as shown in Figure 2. This represents a portion of the order fulfillment process used to instantiate our model. For each order, the input to the activities is the list of ordered components (referred to as technical information), whose quality is captured in $Q_{T}$ , one dimension in each order's state vector, which is one if the technical information is acceptable, otherwise zero. $P(Q_{T}=1)$ , a parameter of the model, is the probability that an order arrives with acceptable technical information.

![](/api/attachments/VG98ZR7K/fulltext/images/cb86efe34ef3030ca5aca5397d7d0edeaf71db9aa5215a8658f1b6b40b6b4dfe.jpg)  
Fig. 1. Overview of the research.

![](/api/attachments/VG98ZR7K/fulltext/images/53aeee39d66a21fea2a21745bd58f59c2581e821f39afaa07b2e5d0478c32834.jpg)  
Fig. 2. An example of activities and their parameters.

The task of producing a configuration for an ordered product is performed by IT. It has two associated quality parameters: the conditional probabilities of producing acceptable configuration information given the quality of the technical information, $P(Q_{C}=1 \mid Q_{T}=1)$ and $P(Q_{C}=1 \mid Q_{T}=0)$ . $P(Q_{C}=1 \mid Q_{T}=1)$ represents the usual case of correct inputs and correct outputs, while $P(Q_{C}=1 \mid Q_{T}=0)$ , the capability of IT to produce a correct configuration in spite of problems in its input, represents an unusual case whose probability will be low or zero. The second activity, the detection of exceptions, models the probability of correctly deciding whether the configured product is producible, $P(\text{Detect } Q_{C}=1 \mid Q_{C}=1)$ and $P(\text{Detect } Q_{C}=0 \mid Q_{C}=0)$ . This captures type I and type II errors in the detection activity. If the detection activity finds an exception (Detect $Q_{C}=0$ ), an exception handling activity is performed. Activity 3 models the probability of producing an acceptable configuration after handling detected problems: the probability of correctly fixing correctly detected problems, $P(Q_{C}=1 \mid Q_{C}=0)$ and the probability of retaining acceptable quality when an exception was incorrectly detected (i.e. a type I detection error), $\mathrm{P(Q_C = 1|Q_C = 1)}$ .

As a result of these activities, the quality of configuration information is set to acceptable $(Q_{C}=1)$ or unacceptable $(Q_{C}=0)$ and some elapsed time $(T_{F})$ and human resource time $(T_{H})$ are consumed. The quality and time parameters for each activity may differ in alternative process designs, depending on the expertise of the person or technology performing the activity. With this example as background, we now specify the model in detail.

## 2.3. Specification of the model

Activity Network. The model builds on models of office processing. Like many office models, ours includes a network of information processing activities, with one starting node and one or more terminating nodes, through which information objects flow. An information object (IO) is a group of related information, such as an order. Unlike other models, our model focuses on exception handling activities, because they affect the efficiency of the process.

Two types of activities are modeled, transformation activities and decision activities. Transformation activities model processing of IO, resulting in changes in the state of the object. These transformation activities include normal processing and processing to handle exceptions or quality problems.

Decision activities model branching within the activity network. They choose the next activity to perform on an object, using the information in the object state vector, but they do not change any values in the vector. Exception detection is a decision activity since it operates by examining the state vector and deciding whether to route the object to the next normal transformation activity or to an exception handling transformation.

Quality Parameters. We use the term information quality because we are studying information used for decision making. We apply the standard definition of product quality, that is, fitness for use [15], to information. Specifically, information is of acceptable quality if it is fit for use for its intended purpose. Information processes produce acceptable quality information if that information is usable for performing the activities that use the information as inputs. Data quality research also takes this approach of applying the standard product quality definition of fitness for use [30].

The method for capturing information quality in the model is based on the Markov process models of accounting and auditing systems, for example, [14, 31] and the models of data and production quality control, for example, [1, 2]. Our work differs by modeling all types of data, not just quantitative data. As in Markov models and office models, the model captures the flow of IO consisting of multiple pieces of information, rather than separately modeling each piece of information.

The state vector associated with each information object captures the quality of the object along several dimensions. For each dimension, quality is acceptable or unacceptable. When an object completes the process, its overall quality (Q) is acceptable (i.e. good enough or fit for use, not necessarily perfect) if the quality along all dimensions is acceptable, that is, Q = 1 iff $Q_{j} = 1 \forall j$ . If any dimension has unacceptable quality at the termination of the process, the object has unacceptable quality. The percentage of objects with acceptable quality is one of the computed performance measures.

The conditional probabilities associated with each transformation activity represent the probability of changing the value of some quality dimension in the state vector, given the current values in the state vector; for example, $P(Q_{3}=1 \mid Q_{1}=1, Q_{2}=0)$

represents the probability that a transformation results in setting $Q_{3}$ to acceptable when an object enters the transformation activity with acceptable quality for $Q_{1}$ and unacceptable quality for $Q_{2}$ . Several conditional probabilities are usually needed to capture the possible results of a transformation. These probabilities represent either normal processing, that may introduce errors, or exception handling activities that attempt to fix, but may not successfully fix, problems.

The conditional probabilities associated with decision activities are of the form, $P(\text{Detect } Q_{j} = 1 \mid Q_{j} = 1)$ and $P(\text{Detect } Q_{j} = 0 \mid Q_{j} = 0)$ , which represent the probabilities of correctly detecting acceptable or unacceptable quality in dimension j. If both are one, exception detection is perfect. Probabilities less than one model type I and type II errors in exception detection, which captures the notion of inspector fallibility in quality control systems. Based on the detected state, the information object is routed to the appropriate next activity.

Time Parameters. The two time parameters associated with each activity, elapsed time, $T_{F}$ , and human resource time, $T_{H}$ , are used to compute flow time and human resource time performance measures. $T_{F}$ represents the total flow time required for an object to complete processing by that activity, which includes actual processing time and any idle time for queuing. $T_{H}$ captures the distinction between activities performed by IT and activities performed by people, that is, $T_{H_{i}} > 0$ if activity i is performed by a person and $T_{H_{i}} = 0$ if it is performed by IT.

The model's utility is demonstrated by using it to evaluate information process design alternatives. Further discussion of the model's strengths and weaknesses is in Appendix A.

## 3. Method

The model is instantiated for an order fulfillment process. For this, the IO are orders and the quality of the order information is tracked for three dimensions of order information: technical, configuration, and sourcing. The quality of the information comprising an order is acceptable for use in producing the product ordered if all three dimensions have acceptable quality. This instantiated model is the basis for two simulation experiments.

## 3.1. Dependent variables

Three performance measures (information quality, flow time, and human resource time) are used in comparing the performance of alternative process designs. Information quality is measured as the percentage of orders completing the process with acceptable quality for the three dimensions modeled. Flow time is measured as the average time to move an order through the process. Human resource time is measured as the average labor hours required for processing each order. These were selected because they are the commonly cited expected benefits from applying IT in operational-level processing and they are benefits that sometimes fail to materialize $[21]$ .

In principle, these three measures of performance could be converted into a common measure, for example, a cost, so that tradeoffs among benefits could be evaluated easily and benefits could be compared directly to the costs of achieving these benefits. Cost measures, however, mask the underlying performance characteristics of information processes and make it difficult to determine how IT affects this performance.

## 3.2. Independent variables

Four independent variables test the sensitivity of the performance measures to variations in process design options. These represent choices that managers can make. Each independent variable maps into one or more parameters of one or more model activities.

IT Task Capabilities represent the ability of IT to handle the orders correctly. Any order not adequately processed is an exception that must be detected and handled. Some exceptions exist because it is not economical to include enough IT for all types of orders. In general, we expect an activity performed by new IT to result in fewer exceptions and take less time, otherwise it should not have been considered. These advantages, however, may be offset by increased difficulties in finding and fixing cases not handled by IT.

‘IT task capability’ is defined as the percentage of orders successfully handled; for example, it can handle 95% of the orders. This is a typical measure of IT capabilities when performing complex decision making activities, such as scheduling [3, 16]. For routine tasks with predictable order characteristics, the percentage handled should be 100%.

In the model, IT processing is a transformation activity. The conditional probabilities capture the percentage of orders handled, which may be conditional on the quality of the input information. Flow time for an IT transformation activity is a positive real number, but human resource time is zero. If the IT task capabilities are changed, the quality and flow time parameters of the activity representing the IT are changed.

IT Quality Control Capabilities represent the ability of IT to provide assistance to other activities, probably performed by people who handle exceptions. For example, IT can provide information about orders it cannot process to the person dealing with these cases. Also, the IT could suggest possible approaches. In addition, it is impractical to include capabilities to support all situations. For example, any assistance necessarily makes assumptions about the capabilities of the person.

In the model, IT quality control capabilities are captured in the parameters for exception detection and handling activities. If assistance with quality control is provided and it matches the capabilities of people, these activities can be performed quickly and accurately.

Human Resource Capabilities can mediate the impact of IT on performance. For example, IT quality control capabilities are more important with less skilled people. In addition, the magnitude of IT effects on performance can be compared to the magnitude of human resource effects; for example, investing in more advanced IT could be considered as an alternative to investing in people with more skills, etc. The experiments consider differences between experts and novices. In general, the former should always be able to perform activities quicker and with fewer quality problems than the latter novices. The magnitude of the difference, however, may vary, depending on the activity and on assistance from IT [22].

Human resource capabilities are measured in terms of the time required to perform activities and the quality of the decisions and information produced. They are captured in the same way as IT capabilities. Changing an activity performed by a person to an activity performed by IT involves changing its quality, flow time, and human resource time parameters.

Location of Quality Controls involves a decision about the location of exception detection and handling: that is, of inspection, re-work, and special processing rather than management control. These may be located near the source of the information (e.g. at sales order entry), near the place where the information is used (e.g. in manufacturing plants), or in between. Based on standard quality control advice to make the person at input responsible for its quality [8], we expect controls earlier in the process. The magnitude of the effect of different control locations, as compared to IT effects, provides some evidence about the value of reorganizing the process. In addition, design choices may depend on IT capabilities; for example, IT may provide capabilities people do not possess, allowing control location choices to be independent of human resource skills.

In the model, alternative locations for controls are captured by changing the placement of activities in the activity network and their associated parameters. Controls moved ahead of the boundaries of the activities being modeled are captured in the initial state vector values.

## 3.3. Field site

The research was motivated by our discussions with managers at a Fortune 100 electronics manufacturing firm that handled approximately 100,000 orders per year. This firm was experiencing many exceptions in a highly-automated order process that provided the information for the build-to-order manufacturing processes. Order information processing included some complex activities, such as, checking credit, producing product configurations, selecting build sites for product components, and scheduling production so that all components were ready at approximately the same time. Although most activities were automated, many people (one for every 1,000 orders processed annually) were needed to assure adequate throughput. These people spent two thirds of their time finding and handling exceptions. In addition, the quality of the information sent to manufacturing was inadequate; for example, product configurations were wrong and build sites did not have the capability or inventory to build assigned components.

What made this particular firm interesting was not that they had the same quality and productivity problems observed in other organizations, but that they were incorporating advanced IT into their order process in order to reduce the number of exceptions and increase process performance. Specifically, they developed new IT and revised existing IT for producing configuration, sourcing, and scheduling information. The order process changes allowed us to observe and evaluate the potential of IT for reducing exceptions. In particular, we evaluated the performance effects of alternative capabilities.

## 3.4. Data collection

Data for the model were collected by interviewing managers, staff specialists, and people performing order functions, by observation, and from archival records. Order processors were observed over several months. All activities were timed. The data, consisting of 600 activity descriptions, were coded using a multiple pass coding scheme that iteratively classified activities into more detailed categories. To reduce bias, activities were coded by a second coder yielding 95% agreement on the first pass and 75% on the second (refinement) pass. All data for the model were collected from more than one source and by more than one method.

For the second experiment, several values for each independent variable were needed. These were collected primarily from our work observation data by considering the process under different conditions, for example, before and after implementing the new IT, within different departments, while processing different products, and when employing novice and expert order processors.

## 3.5. The simulation

The simulation was developed in SLAM II [24], following well-established simulation modeling procedures. Using simulation allowed us to compute flow time when human resources were available eight hours per day with some activities accomplished by overnight batch computer processing. Resource availability and scheduling only affected the flow time measure; the quality and human resource time measures were not changed by this additional flexibility.

The activity network modeled the processing of customer orders through a network of activities representing information handling in the build-to-order process. The process started with the initial receipt of an order by the manufacturing organization from the sales organization and ended with the transfer of the order to plants to begin production. The activities included checking orders for technical and administrative accuracy, developing a product configuration for the order, sourcing the order components to plants, scheduling the order, and transferring the orders to production plants. Some activities were performed by IT while others are performed by order processors.

The state vector associated with each order captured information quality along three dimensions: $Q_{T}$ , $Q_{C}$ , and $Q_{S}$ information. Technical information was the list of ordered parts that was input to the configuration activity; configuration information was generated in the form of an engineering diagram for building the product; and sourcing information involved the plants assigned to build each sub-assembly of the product. For each dimension, quality was acceptable ( $Q_{j} = 1$ ) or unacceptable.

The quality parameters for each activity, the conditional probabilities, were estimated from several types of archival records; for example, for the IT processing activities, records listed all manual changes to IT outputs and why changes were made. This and exception data captured during manufacturing were used to estimate the IT conditional probabilities. Other reports tracked orders through each process stage and were used to estimate branching probabilities. The elapsed time and human resource time parameters in the simulation were estimated from work observation. These estimates were checked for reasonableness against the aggregate time data captured in archival records for over 1,000 orders. Historical order arrival data for a six-month period (approximately 450 orders) were used to drive the simulation. This was more realistic. There was, however, no significant difference in the performance measures produced from using historical data to using a fitted distribution.

Each simulation run produced quality, flow time, and order processor time required. The simulation modeled the actions of a single order processor; they represented independent parallel processors with no interaction. To validate the simulation model, these three performance measures were compared to actual performance. The human resource measure was within the observed range of values, but was higher than the average. Flow time was lower than the real performance, because delays for other than quality problems were not captured in the model.

## 3.6. Experimental design

The four independent variables, IT capabilities, IT assistance with quality control, locations of controls, and human resource capabilities, were varied to represent alternative process designs. The three performance measures were the dependent variables. Differences between two process designs of 2 hours in average flow time, 2.5 minutes in average human resource time, and 3 percent in average quality could be detected as significant, as computed using formulas and recommendations in Kirk [18], including $\alpha = 0.05$ and $1 - \beta = 0.80$ .

Two simulation experiments were designed using experimental design techniques. While a formal experimental design was not strictly necessary for simulation since it is often feasible to make many runs for all possible combinations of factors, using formal experimental designs for simulation was recommended [4]. Formal experimental designs provided statistically valid results, while focusing research attention on the key factors.

The first experiment was a $2 \times 2$ full factorial replicated design (eight runs). Two factors, representing two new information systems, were evaluated at two levels, present and absent in the order fulfillment process. The replication, needed to estimate the standard error, involved two simulation runs for each of the four possible combinations. Since the experiment used a replicated full factorial design, the two main effects and the 2-factor interaction could be estimated. Yates' algorithm for analyzing factorial designs was used to compute the effects using the average from the two replications. The standard error of the effects was computed from the standard deviations of the replications following the procedure in Box et al.[4], whose work dominated the effort and methods here.

The second experiment, which examined variations in the design options for including these two new information systems in the process, used six factors at two levels. Since there were $64\ (2^{6})$ possible combinations for this experiment, a fractional factorial design was adopted, requiring 16 runs. This resolution IV design (main effects were not confounded with two-factor interactions, but two-factor interactions were confounded with each other) allowed the following sixteen estimates (assuming 3-factor and higher interactions were zero): grand mean, six main effects, and seven alias groups of confounded two-factor interactions. The two alias groups consisting of 3-factor and higher order interactions were used to estimate the standard error. The results were computed by applying the Yates algorithm to the data from the sixteen simulation runs.

## 4. Findings and discussion

The first, baseline, experiment compared process performance before and after implementing new IT. It modeled the actual process design choices that were implemented at the field site. This provided a baseline for the second, design variations, experiment, which was essentially a sensitivity analysis of IT capabilities and their comparison to other alternatives.

## 4.1. The baseline experiment

Design. Two new systems were investigated: CFIS which produced configuration information and SRIS which produced sourcing information. These were investigated because the impact of IT may differ, depending on starting characteristics of the activities. Specifically, CFIS replaced a manually-performed activity whereas SRIS replaced an activity performed by a traditional information system written in a third-generation language. All other factors in the process remained at the same values as in the originally instantiated model. Since these systems were developed by experts and were installed to improve process performance, the expected result was that IT would improve all three performance measures.

Results. The results in Figure 3 show that the configuration system (CFIS) significantly affected all three performance measures whereas the sourcing system (SRIS) significantly affected only the quality measure. All significant effects were in the appropriate direction.

Discussion. CFIS had significant quality effects, because it usually functioned correctly and because there was an independent manual quality check. It had significant time effects, because it provided a means of catching technical information problems earlier in the process. SRIS had a significant quality effect, because it produced fewer exceptions than the previous computer system, but no significant time effects, because the structure of quality control did not change when SRIS was installed.

CFIS had a larger effect on quality than SRIS. Prior to CFIS, generation of configuration information was a manual process with no separate quality control check. Prior to SRIS, sourcing information was generated by a computer system and the output was manually checked and fixed. As a result of the separate quality control check, most of the sourcing exceptions were caught by order processors, whereas configuration exceptions, while much fewer, were not caught. This illustrated the interaction between an activity that generated exceptions and the quality control activities that found and fixed these exceptions. Good quality control, that is, high probabilities of finding and correctly handling exceptions, could somewhat compensate for a high level of exceptions.

<table><tr><td>Factor</td><td>Quality</td><td>Flow Time (hours)</td><td>Human Resource Time (minutes)</td></tr><tr><td>Configuration</td><td>0.36**</td><td>-14.3**</td><td>-6.4*</td></tr><tr><td>System (CFIS)</td><td>(32.1)</td><td>(-21.7)</td><td>(-2.4)</td></tr><tr><td>Sourcing</td><td>0.05**</td><td>0.7</td><td>-0.3</td></tr><tr><td>System (SRIS)</td><td>(4.3)</td><td>(1.1)</td><td>(-1.4)</td></tr><tr><td rowspan="2">Interaction of CFIS and SRIS</td><td>0.02</td><td>-1.2</td><td>-0.5</td></tr><tr><td>(2.0)</td><td>(-1.8)</td><td>(-0.5)</td></tr><tr><td rowspan="2">t-statistics are in parenthesis, df=4</td><td colspan="3">** p&lt;0.01</td></tr><tr><td colspan="3">*p&lt;0.05</td></tr></table>

Fig. 3. Analysis of baseline experiment data.

## 4.2. The design variations experiment

Design. This experiment assumed that both CFIS and SRIS were present (this was one combination tested in the baseline experiment) and performed a sensitivity analysis of the performance impacts of IT. Six factors were varied in this experiment: IT task capabilities (the percentage of orders correctly processed by each of the two systems), IT assistance with quality control (the assistance each of the two systems provided for detecting and handling exceptions), the capabilities of people working in the process, and the location of control mechanisms (exception detection and handling activities).

Two levels of each of these six factors were used: a low value representing the worst possible performance and a high value representing the best. These two levels were realistic possible performance values. Using two extreme values for each factor tested whether that factor could have significant effects on the performance measures. For most factors the definition of high and low values was straight-forward, for example, 98% orders correctly handled (high) vs. 80% correctly handled (low). For location of quality controls factor, the high and low values represented the extremes of placing controls at the source of information (high value) or later when it is used (low value).

Results. The results in Figure 4 confirmed that all significant results affected the performance measures in the appropriate direction. Only four of the six main effects were significant for one or more of the dependent variables.

Discussion: Main Effects. Although the presence or absence of CFIS significantly affected all three performance measures in the baseline experiment, varying the capabilities of the CFIS did not significantly affect any of the performance measures. Varying CFIS's capabilities may not produce significant quality effects because the people detecting and handling CFIS exceptions were capable of handling the problems even when they were novices. CFIS provides assistance by running corrections to technical information through the system to check that changes were correct. Thus, almost all technical or configuration information exceptions were correctly detected and fixed, even when the number of exceptions was relatively high.

Both SRIS factors (percentage of orders correctly sourced and assistance to people detecting and handling sourcing exceptions) significantly affected quality and human resource time. The quality effect was significant because generated exceptions may not be caught or may be incorrectly fixed. The human resource time effect was significant: when the SRIS provided good quality control, it was able to detect exceptions, so no additional time was required.

The human resource capabilities affected all three performance measures. This showed the effects of large differences between novices and experts. The location of the controls factor significantly affected the time measures but not the quality. As long as controls were placed somewhere, the final quality of the order information was not significantly changed. Placing controls later increased flow time, because it took longer to send the order back for correction.

Discussion: Interaction Effects. The first four of the seven 2-way interaction alias groups were significant. Since these consist of confounded 2-factor interactions, interpretation may be more problematic than for the main effects. The first three significant 2-way interactions have straight forward interpretations. These non-zero interactions mean that the corresponding main effects were not additive. For example, the effect of switching from low control in sales and low human resource capabilities to high control in sales and high human resource capabilities was not the sum of the two main effects (a reduction of 56 minutes), but included some positive interaction effect (e.g. a net reduction of 42 minutes).

Since the fourth significant interaction affected the quality measure in a direction opposite to that expected for quality, the corresponding main effects are not additive. For factors 3 and 4, this can be interpreted as follows:

\- Reducing the number of exceptions from SRIS had less effect on quality if assistance with quality control was already good.

<table><tr><td>Factor</td><td>Quality</td><td>Flow Time (hours)</td><td>Human Resource Time (minutes)</td></tr><tr><td>1. Configuration System: Percentage handled</td><td>0.002(0.4)</td><td>-1.0(-2.3)</td><td>-1.2(-2.1)</td></tr><tr><td>2. Configuration System: Assistance with QC</td><td>0.012(1.8)</td><td>-0.3(-0.7)</td><td>-0.3(-0.5)</td></tr><tr><td>3. Sourcing System: Percentage handled</td><td>0.058**(9.1)</td><td>-0.3(-0.7)</td><td>-3.0*(-5.5)</td></tr><tr><td>4. Sourcing System: Assistance with QC</td><td>0.027*(4.1)</td><td>-0.4(-0.9)</td><td>-5.8**(-10.4)</td></tr><tr><td>5. Human Resource Capabilities</td><td>0.023*(3.5)</td><td>-4.2**(-9.4)</td><td>-25.6**(-45.9)</td></tr><tr><td>6. Location of Controls</td><td>0.008(1.2)</td><td>-21.7**(-49.2)</td><td>-30.7**(-55.1)</td></tr><tr><td>Interactions:</td><td></td><td></td><td></td></tr><tr><td>Factors 5x6 + 1x4</td><td>-0.001(-0.2)</td><td>0.8(1.9)</td><td>14.6**(26.2)</td></tr><tr><td>Factors 4x5 + 1x6</td><td>-0.012(-1.9)</td><td>0.5(1.1)</td><td>4.3**(7.7)</td></tr><tr><td>Factors 3x5 + 1x2</td><td>-0.015(-2.3)</td><td>0.8(1.7)</td><td>1.8*(3.2)</td></tr><tr><td>Factors 3x4 + 2x6</td><td>-0.027*(-4.2)</td><td>-0.5(-1.0)</td><td>-0.2(-0.3)</td></tr><tr><td>Factors 1x3 + 2x5</td><td>-0.005(-0.7)</td><td>0.7(1.5)</td><td>0.0(0.1)</td></tr><tr><td>Factors 2x4 + 3x6</td><td>0.002(0.3)</td><td>-0.1(-0.1)</td><td>-0.6(-1.1)</td></tr><tr><td>Factors 1x5 + 2x3 + 4x6</td><td>-0.002(-0.3)</td><td>0.1(0.3)</td><td>-0.2(-0.3)</td></tr><tr><td>t-statistics are in parenthesis, df=2</td><td colspan="3">** p&lt;0.01* p&lt;0.05</td></tr></table>

Fig. 4. Analysis of the design variations experiment data.

\- Alternatively, improving assistance with quality control had little effect on quality if few exceptions were present.

## 4.3. Discussion of process design alternatives

Improving IT Capabilities. We first compared performance from the first run of the baseline experiment, the only run with no new IT, to the measures from all the other runs. For information quality, the run without new IT had the lowest value of all. For time measures, some runs had better performance than the run with no new IT. Upon further examination, flow time increased only when early process controls were weak. Human resource time increased only when both early process controls were weak and order processors were novices. In summary, installing new IT increased information quality in all experimental runs. Flow time and human resource time were affected by other process characteristics. Specifically, if new IT was a justification for employing less skilled people or maintaining less control on process inputs, flow time and human resource time increased.

Improving IT Capabilities vs. Other Options. We then compared the impacts of IT versus the impacts of other process factors by examining the magnitude of their effects. For quality, improved IT capabilities had more impact than human resource capabilities and location of controls. For the time measures, human resource capabilities and location of controls had more effect than any of the IT factors. In summary, if improved information quality was needed, installing IT with capabilities for correctly handling most inputs and for providing assistance with quality control had the highest impact. If improved flow time was needed, more process reorganization was necessary. One way to reorganize a process was to change the location of controls. The earlier exceptions were caught the smaller was the flow time delay.

Quality Control Design Alternatives. Several alternatives for quality control were investigated, including the location of controls, the capabilities of IT to assist with quality control, and the capabilities of the people performing quality control. The second experiment provided evidence that these quality control design decisions affected all three performance measures. Improved IT assistance increased the resulting quality and reduced the people time. In addition, using experts improved quality. Changing the location of controls improved flow time.

Although IT may not directly reduce human resource requirements, a secondary effect was likely to be reduced human resource requirements, because fewer people were needed to handle exceptions. If people must still review computer system outputs (to detect fewer exceptions), however, improved quality may not have affected human resource requirements. To improve all three performance measures significantly, the employment of IT should be combined with some design or reorganization of the process.

Since these results were obtained from a study of one information process and two new systems, they should not be assumed to provide general results. However, the process was common to most manufacturing and service firms [26]. The systems were applied to common manufacturing decisions that are likely to require advanced IT in any firm.

## 5. Conclusion

Beyond the specific results from the simulation experiments, this study contributes to information systems research and practice in two areas. First, it provides a model of exception handling in routine information processes that can be used to evaluate information process designs. Second, it contributes to our ability to analyze the impacts of IT on performance.

Overall, the model contributes by combining features of existing models into a new model that captures exception detection and handling activities and computes quality and productivity measures. The model is of practical value, because it uses data that can be collected from operating processes and because it provides a framework for thinking about the impacts of new IT.

In this study, we demonstrated a rigorous method for studying IT impacts. Our model and the performance measures computed from the model provide a means for understanding relationships among exceptions, the need for exception handling, and the resulting quality and time measures. Measuring performance has been a problem in MIS field research, and attributing performance changes, given many other organizational variables, to changes in independent variables is problematic. The model isolates the effects of independent variables on the performance measures so that these relationships can be studied and understood. By using field data in the model, we achieve the advantages of using realistic data while maintaining the control of laboratory experiments.

This method should be useful in other studies of IT impact. It uses realistic field data to run experiments that cannot be run at field sites. The knowledge gained from using this approach to study IT impacts could significantly improve our ability to effectively use IT in organizations.

## Appendix A

## Strengths and Weaknesses of the Model

Each model component (activity network, quality parameter, or time parameter) is found in the accounting or office modeling literature. We combined these three independent components into one model. Although our experience with the model leads us to view these characteristics as strengths, others may view them as weaknesses.

Simplification of the Markov process model. The model of quality is a special case of a Markov chain model of quality and quality changes. In the general case, the states in the state vector are the possible combinations of two quality values (acceptable and unacceptable) for N quality dimensions, that is, $2^{N}$ independent states. The quality parameters for each transformation activity consist of a $2^{N} \times 2^{N}$ probability transition matrix. As our study progressed, we discovered that most of the transition probabilities are zero for any particular transformation activity and that each activity considers only a few of the possible quality dimensions. Therefore, we used the simplified version of modeling activities with several conditional probabilities, rather than a full probability transition matrix, and with the N dimensions as states rather than the $2^{N}$ independent states in the state vector. This is both more tractable and more realistic. Thus, the conditional probabilities in our model are the non-zero transition probabilities in the full Markov chain model.

Markov memoryless property. The model assumes that the current state of an object and its location in the network is sufficient information for determining the next activity for that object; that is, the processing of objects through the network can be modeled as a Markov process [13]. In practice, this memory-less property of a Markov process is not overly restrictive, because it depends on how the states are defined rather than being an inherent property of the process. For information processing activities, people and computer systems usually can determine the next activity to be performed based on the current information associated with an object.

Independence of quality and time parameters. The time parameters in the model represent average processing times independent of characteristics of individual objects, and are thus independent of the quality parameters. In practice, processing time may depend on the quality of the object. This is handled in two ways. First, activities with significantly different processing times, because of quality, are modeled as separate activities. Second, the processing time parameter is an average that summarizes normal variations in time due to small differences in quality.

IT as general information processors. All activities in the model have the same parameters (two time parameters and several conditional probabilities representing quality state changes or branching decisions) independent of the type of processor performing the activity; that is, people, traditional IT, and advanced IT are all captured in the model using the same method. Thus, the model focuses on the information inputs and outputs of activities, not on the procedures or rules for performing activities. This perspective is one that has emerged from literature on organizations as information processing systems developed from the early work of March and Simon [20] and Cyert and March [6] and extended by Galbraith [9]. This treatment focuses attention on the role of IT within an information process rather than technical issues related to any particular IT or type of IT.

Focus on exception handling and quality control activities. The focus on exception handling and quality control as key variables differs from the focus of prior models. Even without formally applying the model to an information process, managers can think about: (1) exceptions and their causes, (2) performance impacts of exceptions and exception handling, and (3) efficient procedures for finding and fixing exceptions. Our results indicate that it is important to evaluate the performance impacts of exception handling and quality control when considering process design options, especially those involving new IT.

The model's exception handling focus provides a framework for thinking more generally about IT effects. Although computer systems typically improve performance, they can also generate exceptions, cause extra work, and make it more difficult for people to find and fix them. These problems are not centered on the IT activities, but on the interface to the surrounding information process. These problems occur in many situations, not just in operational-level processes. For example, work may need to be changed to match IT needs or workers may find it easier to perform work manually and enter data later into the computer.

## References

[1] D.P. Ballou and H.L. Pazer, “The Impact of Inspection Fallibility on the Inspection Policy in Serial Production Systems,” Management Science, 28 (4) April 1982, pp. 387–399.

[2] D.P Ballou and H.L. Pazer, "Modeling Data and Process Quality in Multi-Input, Multi-Output Information Systems," Management Science, 31 (2) February 1985, pp. 150–162.

[3] D.G. Bobrow, S. Mittal and M.J. Stefik, "Expert Systems: Perils and Promise," Communications of the ACM, 29 (9) September 1986, pp. 880-894.

[4] G.E.P. Box, W.G. Hunter and J.S. Hunter, Statistics for Experimenters: An Introduction to Design, Data Analysis, and Model Building, John Wiley and Sons, 1978.

[5] M.D. Cohen and P. Bacdayan, “Organizational Routines are Stored as Procedural Memory: Evidence from a Laboratory Study,” Organization Science, 5 (4) November 1994, pp. 554–568.

[6] R.M. Cyert and J.G. March, A Behavioral Theory of the Firm, Prentice-Hall, 1963.

[7] T.H. Davenport and J.E. Short, “The New Industrial Engineering: Information Technology and Business Process Redesign,” Sloan Management Review, 31 (4) Summer 1990, pp. 11–27.

[8] A.V. Figenbaum, Total Quality Control, 3rd ed., Revised, McGraw-Hill, New York, NY, 1991.

[9] J.R. Galbraith, Organization Design, Addison-Wesley, 1977.

[10] L. Gasser, “The Integration of Computing and Routine Work,” ACM Transactions on Office Information Systems, 4(3) July 1986, pp. 205–255.

[11] G. Hall, J. Rosenthal and J. Wade, “How to Make Reengineering Really Work,” Harvard Business Review, 71(6) November-December 1993, pp. 119–131.

[12] M. Hammer, “Reengineering Work: Don’t Automate, Obliterate,” Harvard Business Review, 68 (4) July-August 1990, pp. 104–112.

[13] D.P. Heyman and M.J. Sobel, Stochastic Models in Operations Research, Vol. 1: Stochastic Processes and Operating Characteristics, McGraw-Hill, 1982.

[14] J.R. Johnson, R.A. Leitch and J. Neter, “Characteristics of Errors in Accounts Receivable and Inventory Audits,” The Accounting Review, LVI (2) April 1981, pp. 270–291.

[15] J.M. Juran, Juran on Leadership for Quality: An Executive Handbook, The Free Press, New York, 1989.

[16] J.W. Kaewert and J.M. Frost, Developing Expert Systems for Manufacturing: A Case Study Approach, McGraw-Hill, NY, 1990.

[17] Karbe, B. H. and N. G. Ramsperger, “Influence of exception handling on the support of cooperative office work,” in S. Gibbs and A. A. Verrijn-Stuart (Eds.) Multi-User Interfaces and Applications, North-Holland, 1990. Reprinted in SIGOIS Bulletin, 11 (4) December 1990, pp. 2–15.

[18] R.E. Kirk, Experimental Design: Procedures for the Behavioral Sciences, Brooks/Cole, 1982.

[19] L.O. Levin and S.S. Aurand, “Evaluating automated workflow systems for administrative processes,” Interfaces, 24 (5) September–October 1994, pp. 141–151.

[20] J.G. March and H.A. Simon, Organizations, John Wiley and Sons, 1958.

[21] M.L. Markus, Systems in Organizations: Bugs and Features, Pitman Publishing Inc., 1984.

[22] E. Oz, J. Fedorowicz and T. Stapleton, “Improving quality, speed and confidence in decision-making: Measuring expert system benefits,” Information and Management, 24 (2) February 1993, pp. 71–82.

[23] M.A. Palley, “Hospital information systems and DRG reimbursement: The adaptation of large transaction processing systems to radical rule changes,” Information and Management, 20 (3) March 1991, pp. 227–234.

[24] A.A.B. Pritsker, Introduction to Simulation and SLAM II, 2nd ed., John Wiley and Sons, 1986.

[25] H. Saastamoinen and G.M. White, “On handling exceptions,” Proceedings of the Conference on Organizational Computing Systems, ACM SIGOIS, August 1995, pp. 302–310.

[26] B.P. Shapiro, V.K. Rangan and J.J. Sviokla, “Staple yourself to an order,” Harvard Business Review, 70 (4) July-August 1992, pp. 113–122.

[27] D.M. Strong, “Decision support for exception handling and quality control in office operations,” Decision Support Systems, 8 (3) 1992, pp. 217–227.

[28] D.M. Strong, and S.M. Miller, “Exceptions and exception handling in computerized information processes,” ACM Transactions on Information Systems, 13 (2) April 1995, pp. 206–233.

[29] L.A. Suchman, “Office procedure as practical action: Models of work and system design,” ACM Transactions on Office Information Systems, 1 (4) October 1983, pp. 320–328.

[30] R.Y. Wang, and D.M. Strong, “Beyond accuracy: What data quality means to data consumers,” Journal of MIS, 12 (4) Spring 1996, pp. 5–34.

[31] S. Yu, and J. Neter, “A stochastic model of the internal control system,” Journal of Accounting Research, 11 (2) Autumn 1973, pp. 273–295.

![](/api/attachments/VG98ZR7K/fulltext/images/7b50c1bd4d5115435c8e1f01bd0b6ad46fb3b2572ddd94ea433aa3163de0273b.jpg)  
Diane M. Strong is an assistant professor of Management at Worcester Polytechnic Institute. She received her Ph.D. in information systems from Carnegie Mellon University. Dr. Strong's research centers on data and information quality. She is a founder of the Conference on Information Quality and is Program Co-Chair for the 1997 conference. Her publications have appeared in ACM Transactions on Information Systems, Communications of the ACM, Journal

of MIS, MIS Quarterly, and other leading journals.
