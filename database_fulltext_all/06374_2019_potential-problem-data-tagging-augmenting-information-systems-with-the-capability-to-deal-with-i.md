---
otero_id: 6374
otero_key: "WCT6NF53"
title: "Potential Problem Data Tagging: Augmenting information systems with the capability to deal with inaccuracies"
authors: "Philip Woodall; Vaggelis Giannikas; Wenrong Lu; Duncan McFarlane"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.04.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Potential Problem Data Tagging: Augmenting information systems with the capability to deal with inaccuracies

![](/api/attachments/WCT6NF53/fulltext/images/ec3e97ab1cf832e904b51a34cf22f1aa72683a5e8574f8372dc29f703a6c58b0.jpg)

Philip Woodall <sup>a,⁎</sup>, Vaggelis Giannikas<sup>b</sup>, Wenrong Lu<sup>a</sup>, Duncan McFarlane<sup>a</sup>

<sup>a</sup> Department of Engineering, 17 Charles Babbage Road, Cambridge CB3 0FS, UK

<sup>b</sup> School of Management, University of Bath, Bath BA2 7AY, UK

## A R T I C L E I N F O

Keywords: Data quality Information quality Accuracy Metadata Data analytics Data tags

## A B S T R A C T

Data quality tags are a means of informing decision makers about the quality of the data they use from information systems. Unfortunately, data quality tags have not been successfully adopted despite their potential to assist decision makers. One reason for the non-adoption is that maintaining the tags is expensive and timeconsuming: having a tag that represents accuracy, for example, would be massively time-consuming to measure because it requires some physical observation of reality to check the true value. We argue that a useful surrogate tag for accuracy can be created—without having to physically measure it—by counting the number of times the data has been exposed to an event that could cause it to become inaccurate. Experimental results show that the tags can help to avoid problems caused by inaccuracies, and also to help find the inaccuracies themselves.

## 1. Introduction

Data quality tags have been proposed as a means of informing decision makers about the quality of the data they are using from information systems [1,2]—tags are also referred to as data quality metadata [3]. Tags are important because without them, information systems essentially present data to users asserting that it is 100% correct, with no indication being provided about any deficiencies in the data [4–7]. If these deficiencies remain hidden, any resulting data analytics or decision-making from the data will be flawed [8] leading to costly, disruptive or even disastrous situations for both business [9–11] and academia [12].

Despite their importance, data quality tags have not been success fully adopted in information systems. One of the key barriers is that it is expensive and time-consuming to maintain such information [13–15]. For instance, it is notoriously dificult to measure and maintain a data tag about data accuracy [16], which is a key data quality dimension. This is because data accuracy problems are defined as the degree to which the reported value is in conformance with the actual or true value [17,18], and so to detect the presence of an inaccuracy often requires some manual observation or survey of the real or true value [19,20]. The actual value is often unknown [1,21] and hence measuring inaccuracies is often time-consuming, labour intensive [22], error prone in itself [23], and very dificult/costly to automate [20].

In order to address this issue, we argue that a useful tag for accuracy can be created and used in information systems that does not rely on performing physical observations. By counting the number of times the data has been exposed to an event that can cause it to become inaccurate, a useful surrogate for an accuracy measurement can be obtained automatically; we refer to this as Potential Problem Data Tagging, and show how it can be used to help avoid operational disruptions caused by inaccuracies and also help to find the inaccuracies in information systems. This work builds on the concepts from currency prediction work [20,24] that provides models to estimate how data will degrade over time, without having to rely on a baseline (e.g. manual observation) for comparison.

Potential Problem Data Tagging does not produce an bona fide accuracy measurement that can be used to assess accuracy in the sense of a normal metric because it is essentially a best guess at whether the data is in error or not, and it could be inaccurate in itself. Hence, we also show how this surrogate measure can be used in an operational decision-making environment to help select the best course of action from a set of alternative actions; in order to improve the performance of the action (such as by avoiding operational disruptions). In summary, the main contributions of this paper are: 1. showing how to automatically populate tag values that can be used as a substitute for an inaccuracy measure, and 2. showing how these values can be used within an op erational environment to select the best course of action for a decision.

Using an experimental simulation, based on a real-life decision making task of choosing what locations to pick items from in a warehouse, we explore the cases when this type of approach can provide the most useful indicators to help decision makers avoid problems with inaccurate data. Although the approach leads to recording many false positives, the experimental results show that the tags are usable and perform the best for high error rates and for problems with larger degrees of freedom with respect to the decision alternatives.

## 1.1. Motivating example: inaccuracies in warehouse decision-making

One example of a real decision-making case which can benefit from accuracy data tags is choosing what location to pick items from within a warehouse. In this case, a warehouse management system (WMS) records the locations, types and quantity of items in the warehouse. The decision uses the type and quantity criteria to determine which location to pick the required items from. There can be multiple decision options, hereon referred to as degrees of freedom (DOF), because the same item types are often stored at multiple diferent locations. Hence, there may be no single right answer with various alternative choices being satisfactory; this is termed “satisficing” decisions, where satisfying a chosen aspiration level, rather than an optimal solution, is the focus [25] as opposed to cases where there is only one optimal decision choice (see [15]). This type of decision is therefore referred to generally as a multi-criteria, satisficing decision. It is also analytical rather than judgemental, bargaining, or inspirational [26,27].

Once a location is chosen, a picker picks the physical items and always returns to update the WMS, so the data is always current; warehouses are strict about data updates to ensure that data is always current. However, if a picker makes a mistake in the picking or placement of items, an inaccuracy will result when the WMS is updated because the pickers are unaware of their own mistake. There are various causes of inaccuracies in warehouses [28], such as picking from the wrong location [29] or misreplacements [30,31]. This problem is compounded by the fact that there is no real indication of when a person will make these mistakes as they can occur anytime and at any location. Furthermore, it is not easy to detect the inaccuracies from the data alone, because when the locations to pick items from are selected from the WMS, the inaccurate data appears to be completely valid i.e. there is no obvious anomaly, such as more items at a location than is physically possible.

In this case, data tags that inform the WMS about which locations are inaccurate could be used to: 1. improve decision-making by enabling the WMS to choose the most accurate locations and hence help pickers avoid disruptions (such as being sent to locations that are empty) and, 2. help to find the inaccurate locations in the warehouse. However, to populate a data tag containing a true accuracy measurement is clearly problematic as there is no other source of this data, and hence continual inventory checks would be required to observe reality. Currently, warehouse organisations do use inventory checking as a way to ensure that the data in the WMS is accurate. However, it is dificult and inflexible for a warehouse to automate this process, and item tracking solutions such as Radio Frequency Identification (RFID) are expensive, inflexible, and sufer from inaccuracies themselves [32,33].

## 1.2. Characteristics of the general problem context

The above warehousing example is a particular decision-making case that exhibits the following general characteristics: 1. it is an analytical, multi-criteria, satisficing decision that can be improved by choosing better decision choices based on an understanding of the level of accuracy of the supporting data, 2. to measure accuracy is timeconsuming, labour intensive, error prone and dificult/costly to auto mate, 3. a surrogate data source does not exist to support the measurement of accuracy, 4. data that is inaccurate appears to be valid and does not exhibit any obvious anomalies, 5. the process to update the data does not correct the inaccuracy, 6. the data is kept current by regular updating of the data every time the real value changes, 7. the events that occur that cause the inaccuracies are known about in general, but it is not known when a particular instance of the event will cause an inaccuracy, 8. it is dificult or impossible to estimate the probabilities related to when data will become inaccurate.

Currently, there are no existing approaches that can provide an accuracy data tag to assist a decision-making problem with the above characteristics; Potential Problem Data Tagging aims to address this research gap. Section 2 describes the background research on accuracy, data tags and measuring accuracy automatically. Section 3 presents the Potential Problem Data Tagging approach, and Section 4 describes an application of the approach to the previously described warehousing example. Sections 5 and 6 describe and present the results of an evaluation of the approach using a simulation. Section 7 discusses the results and describes the limitations. Finally, Section 8 concludes by discussing the implications of this work.

## 2. Background

This section defines accuracy, provides a review of the use of data tags, and presents the existing approaches related to measuring accuracy with reference to the above characteristics.

## 2.1. Defining accuracy

Accuracy has featured prominently as a key dimension in much of the data quality research [34–37]. The definition by Ballou and Pazer [17] is an early example that covers a common theme of the misalignment between the data and reality, and is adopted in this research: accuracy is “the degree to which the reported value is in conformance with the actual or true value.” The term conformance alludes to the magnitude of the error (see the arguments presented in [38]) implying that it need not be a Boolean comparison between reality and data. The actual/true value implies that any assessment of accuracy requires an observation of this actual/true value in reality. Accuracy can be measured at the database level [35], the attribute level [19], and the record level [39]. For a good overview of accuracy definitions see [35]. We focus on measurement at the record level i.e. a record is accurate if all of its attribute values are accurate [40].

## 2.2. Existing work on data tagging

For relational databases, tags can be used to convey the quality of data records [39], columns [15], or individual values for various data quality dimensions [2]. The values in the tags can vary between discrete-ordinal indicators of quality, such as representations analogous to trafic-light signals [15,41] to continuous numerical indicators [39].

Various multi-attribute decision-making tasks have been considered in the data tag research, including residential apartment selection [13–15], ranking of firms according to their financial health [42], ranking of job alternatives [14], and allocation of budget among multiple types of advertising [41]. These works all assume, and rely on, a data tag for accuracy being available.

## 2.3. Existing approaches to measure accuracy

The following sections describe the diferent techniques and metrics that can measure accuracy. Approaches that address the quality dimension of currency are also reviewed, due to the similarity of currency to accuracy (see the discussion in [20]).

## 2.3.1. Valid but inaccurate data

Validation rules can be used to check whether data is likely to be inaccurate, such as that a social security number must consist of nine numeric digits [23], and it is considered to be inaccurate otherwise. Inaccuracies can be inferred using dependencies [43] or rules relating to multiple data columns [44]. Validation rules can also use temporal aspects to infer inaccuracies [45]. Anomaly/outlier detection solutions can be used to find patterns in data that do not conform to expected normal behaviour [16,46], which can also be considered a type of validity check. However, despite the references to accuracy, English suggests that many of these types of problems are validity checking [19]; hence the data could be both valid but inaccurate. For example, a person's social security number recorded in a database could contain nine numeric digits and still not be the social security number of that person. Hence, these types of approaches are not suitable to address the problem context in this paper because of the characteristic that data appears to be valid but can still be inaccurate.

![](/api/attachments/WCT6NF53/fulltext/images/e2e6b0851fbca219072eeb5e9316a3ee6fa211cb4d98a2306a17e70152a9ad70.jpg)  
Fig. 1. Illustration of the Potential Problem Data Tagging approach.

## 2.3.2. Unavailable or inaccurate surrogate sources

A surrogate source of data may be available from which the data can be checked against [34]. Online sources can be used, although the challenge is the extent to which they accurately represent reality itself [47]. Also, data redundancy between systems can be used to crosscheck data accuracy [22]. However, surrogate sources cannot be used to detect inaccuracies when a surrogate source does not exist and/or is not correct itself [48], which is the case for the characteristics of the problem context in this research.

## 2.3.3. Statistical analysis and currency

Inaccuracies can be estimated using statistical analysis of a series of measurements to determine estimation errors [21], or performing a sample of observations and then estimating the overall level of accuracy of a set of records [5,43]. Other statistical work observes currency of data that can become inaccurate if the real-world counterpart changes over time and the stored data values are not updated [20,48]. Markov models have been used to model the probabilities that attribute values change, and can estimate when data will become inaccurate [24,48]. Various useful currency metrics have been developed using probability theory [20,49–51].

The approach presented in this paper builds on the foundations of the currency approaches and makes three important changes: 1. removing the need to provide estimates of the transition probabilities for data values changes, 2. shifting the focus from the passage of time to the occurrence of events, and 3. the ability to operate with or without probability estimates.

The existing currency models rely on being able to estimate the transition probabilities for data value changes; hence, they are ideally suited to examples where these can be estimated, such as marital status [49], or the changing status of a process [24]. However, contrast this to the quantity of items at a warehouse location transitioning from 4 to 5 items, and what the associated probability is. There are two challenges with this: 1. it is dificult to determine what the transition probabilities should be and 2. there are a very large number of transitions that require probability estimates. Hence, the key adaptations for the context in this paper is that the equivalent of Markov model states now refer to whether the data is accurate or inaccurate rather than having states for each individual data value. Then the transition probability becomes an estimate of whether the data will become inaccurate or not. And this can simplified again to: a tally of the number of times data has been exposed to an event that can cause it to become inaccurate. Hence. in cases where it is dificult to estimate the probabilities, the information that must be known is only when events occur that may cause data to become inaccurate. Note that the shift from time to events is important in the case when it is known that both a particular event may cause an inaccuracy and when this event will occur (as in the warehouse example: the picking event may cause an inaccuracy and it is known when it occurs). Data that over a long period of time has been exposed to no events that may cause it to be inaccurate is less likely to be inaccurate than data that has been exposed to many of the events (regardless of the time period).

Table 1  
When and how to update the tags (EP is the expected probability).

<table><tr><td>When to set/update the tag</td><td>Starting value (or whenever the data is confirmed as being correct)</td><td>The first time the event occurs</td><td>All subsequent times when the event occurs</td><td>Whenever the data is confirmed to be definitely inaccurate</td></tr><tr><td>Value to set in the tag</td><td>0</td><td>EP</td><td>(currentValue + EP) - (currentValue * EP)</td><td>1</td></tr></table>

## 3. Potential Problem Data Tagging

A Potential Problem Data Tag is a recording of the number of times data has been exposed to an event that can cause it to become inaccurate. The event may not always cause the inaccuracy; hence, it does not produce an actual measure of accuracy, and must not be treated as such. However, the tag can be used to determine which data records are likely to be more accurate or less accurate than one another; this can be considered to be “relative accuracy” ([52], p. 5) between records in a database (note that this paper focusses on database records, further work would be required to extend the approach beyond this). These types of tag can be used to assist with operational decision making as shown in Fig. 1, which shows a database and front-end software application that is used to make decisions that are actioned in the physical operations.

The tags can be used to select either the least or most potentially accurate data from the database, which can then be used within the operations to find inaccuracies or avoid disruptions respectively. The increased ability to find inaccuracies can be used to support data correction activities, while avoiding disruptions can lead to higher operational performance. This capability is dynamic and can be switched at will, which can therefore align with the demands of the operations: such as in cases where time is critical and avoiding disruptions is required, to the opposite case where there are slack periods that allow staf to spend more time improving the quality of the data by finding inaccuracies. The switch is achieved by filtering the database records depending on the tag values, and the reporting mechanism of the application is the point at which this can be implemented (see Fig. 1).

A tag can be incorporated as an additional field in the database, and the tag updater component is responsible for setting/updating the values of the tags for the relevant data. The tag values must consist of any set of symbols that can produce an ordinal scale. For example, a con venient choice is a numeric value with zero indicating an accurate record, and values between zero and one indicating increasingly likely to be an inaccurate record, eventually with a value of 1 indicating a de finitely inaccurate record. The tag values are incremented based on events occurring that can cause inaccuracies to be inserted into the data. An event is something that happens in the physical operations of an organisation (e.g. a picker going to pick items in a warehouse, or the maintenance of a machine, etc.) that can cause an inaccuracy. Ideally an event can be observed automatically; however, if this is not possible, there may be an indication that the event occurred from the software application (an engineer entering a maintenance record, for example, indicates that maintenance of a machine occurred). Once the event occurs, it may only produce an inaccuracy in certain records in the database. In many cases the selection of which records to tag will be clear by the context, and it is especially clear when the event is in formed by the software application. For instance, when entering a new maintenance record for a machine, the inaccuracy is between that record and the machine (rather than for any other machine or any other database record). The tag updater component selects the afected records and updates their tag values when the event occurs. The tag updater must also reset the tag values after any data correction activity to indicate that the relevant data is now accurate. Finally, under certain conditions an event may be more or less likely to introduce an inaccuracy, and therefore the tag updater component should be able to modify the tags to reflect this increase/decrease in likelihood.

## 3.1. Setting the tag values

There are two distinct cases that determine how to set tag values: if the probability of an inaccuracy is not known and cannot be easily estimated, versus if it is known/can be estimated. In the former case, it is suficient to use a tally of event occurrences for each data record, which is updated each time the event occurs, this produces the required ordinal scale in a simple way. In the latter case, Table 1 shows one example of how to use a probability estimate for setting and updating tag values that also produces an ordinal scale. Note that this is a convenient strategy because the updates to the tag will tend to 1, but will never reach it, meaning that the value of 1 can be reserved for definitely inaccurate values. This construction satisfies the minimum/maximum requirements for metrics [53]. In the table, currentValue is the current value of the tag and EP is the “Expected Probability” of the event that causes an inaccuracy in the data record. EP can be estimated using observations of prior events and by calculating: the number of inaccuracies observed/the total number of events observed. The formula in Table 1 is essentially the probability of the union of two events (for non mutually exclusive events); it is equivalent to the probability that the inaccuracy occurred for the current event or the previous events or both. In this case, we assume that EP is constant for all events, the events are assumed to be independent, and also possesses the memoryless property because no information is gained from previous events. Note that these tag values align with the formalisms used in probabilistic databases [39] and decision making [20]. Furthermore, the value of EP can be set dynamically based on conditions related to the event; for example, it could be increased under conditions where the event is more likely to lead to an inaccuracy, and vice versa (an example of this is shown in Section 4 for two diferent EP values which are set dynamically).

## 3.2. Assumptions for use

The following assumptions must be satisfied for Potential Problem Data Tagging to be applicable to a problem and to potentially yield a benefit: 1. DOF > 1: the decision/task must have more than one DOF 2. tag correctness: when the event occurs, the tag values correctly tag an inaccuracy in at least one case (i.e. there is at least one true positive tag), 3. record diferentiation: when the event occurs, at least 1 record is tagged and not all records associated with the DOF are tagged.

Assumption 1 must hold true otherwise it is not possible to choose alternative courses of action for the decision, and it would not be a satisficing decision (cf. Section 1.2). Assumption 2 concerns the ability to correctly tag a record when it contains an inaccuracy. The challenge is that a) the choice of which record(s) to tag needs to be correct (i.e. it is possible to tag the wrong record(s)), and b) an accuracy may not always be inserted into a record because the event may not always result in an error that leads to an inaccuracy. These situations lead to tags being false negatives and false positives respectively. All of the possible situations are summarised in Fig. 2. In Fig. 2, ‘A’ is the set of records actually containing an inaccuracy caused by the event, and ‘T’ is the set of records that have been tagged as containing an inaccuracy for the event. Note that |A| refers to the number of actual inaccuracies that have been inserted into the data for a given event. For cases 1, 2, 3 and 4, there is the possibility that the approach will provide a benefit; case 2 being the best case where all the tags correctly tag all of the records containing the actual inaccuracies. The approach does not provide any benefit in case 5 because there are no tags that are true positives.

![](/api/attachments/WCT6NF53/fulltext/images/a4c17882bccfdc6a9afe4a20df9652267180599923393b5d389ae13e60ee42d7.jpg)  
Fig. 2. The overlap between the actual insertion of an inaccuracy and the tagging of a record.

Assumption 3 (i.e. record diferentiation) must be satisfied because otherwise there is no diferentiation between records that helps to in dicate which records are potentially more likely to be accurate than others. The same is true if DOF records are tagged. Note that these three assumptions need not always be satisfied (for every event occurrence) because the DOF, true positives etc. can all change for each different instance of an event.

## 4. Application to decision making in a warehouse

This section illustrates how to apply Potential Problem Data Tagging to the warehousing decision-making example presented in Section 1.1. where the data tags are used to improve decision-making by enabling the WMS to choose the most inaccurate/accurate locations and hence help pickers either find inaccuracies or avoid disruptions. Inaccuracies in the data can lead to the following disruptions: D1) pickers are sent to warehouse locations that contain too few items (or are empty), D2) pickers are sent to locations that contain the wrong item types, D3) the WMS rejects orders that the warehouse can fulfil assuming there are not enough items in the warehouse, D4) the WMS accepts orders that the warehouse cannot fulfil assuming there are enough items in the ware house. D1 and D2 are caused by the aforementioned misreplacements or picking from the wrong location. Misreplacements occur when items are put back into the wrong location either on top of similar items or into empty locations. Picking from the wrong location is when the picker takes the items from the wrong location. In later picks, if it is observed that there is nothing in a particular location when items are expected to be there, then the WMS is updated to reflect reality i.e. the location is set to zero quantity (so that pickers are not sent again to that location to face the disruption again). However, this has two side effects: firstly, the actual quantity in the warehouse is reduced so it is possible to reject orders which can actually be fulfilled (D3); secondly, the inaccuracy is not entirely solved because there is another location where the items actually are that will remain inaccurate. The opposite situation can occur when items are found in the warehouse that are not in the WMS, and hence, disruption D4 can occur. Not all inaccuracies necessarily lead to operational disruptions, however. For example, if the WMS records that there are too many items in a location, then the picker will not face a disruption because there will be enough for them to pick. Also, it is unlikely they will even notice the data inaccuracy as a) they are not aware of the value stored in the WMS while performing the picking task, b) it is impractical to always count the items lying in a storage location without spending considerable amounts of time.

The following sections describe how Potential Problem Data Tagging was implemented for the experimental evaluation, to help select the most accurate or inaccurate locations for the above warehousing example.

## 4.1. Event selection

The printing of a picking list by the WMS was selected as a convenient event that acts as a surrogate for the insertion of an inaccuracy. In reality, when a picking list is printed, it is handed to a picker whom while physically picking the items, could misreplace or pick the wrong items. Due to the dificulty in determining exactly which events will lead to a misreplacement or incorrect picking error, the solution always records that the error could have been made.

## 4.2. Selection of records to tag

There are two instances of inaccuracies that result from misreplacements and picking from the wrong location: 1. in the record about the expected picking location, and 2. in the record about the actual picking location (where items have been actually taken from or misplaced to). The “expected” record is known, and the “actual” record is unknown. For this reason, only the expected record was tagged. Also, if a misreplacement error does occur, then the expected record is guaranteed to be inaccurate. This solution therefore fits case 1 in Fig. 2 as it will generate one true positive and one false negative. Hence, the second assumption (tag correctness), which indicates whether the solution can provide a benefit, is satisfied. The final assumption (record diferentiation) is also satisfied as the solution will always tag 1 record for an event. The first assumption is satisfied as long as the warehouse contains the same type of items in multiple locations, which therefore provides DOF > 1.

## 4.3. The tag and tag updater component

The tag was implemented as an extra field in the WMS database. To demonstrate the case where EP is not known (e.g. in some warehouses there is no data on the errors), a simple tally was used starting at 0 and incremented by 1 each time the event occurred. To demonstrate the case when EP is known, the tag value of EP was set to 0.02 (based on observations of inaccuracies from historical inventory checks in a real warehouse where data was available). Furthermore, an additional case was also evaluated where according to observations in reality, a misreplacement is more likely to occur when there are empty locations nearby to the picking location (within approximately ± 3 locations). Hence, when this condition is true, the value of EP was increased to 0.05; a conditional check for nearby empty locations in the WMS was carried out by the tag updater component, and if true, the increased EP value was used, otherwise the default value of 0.02 was used. The tag updater component was implemented in Java, and it updates the tag values (as shown in Table 1) using SQL queries issued to the WMS database. It updates the tags when: 1. the picking list is printed—the tag is updated to indicate that an inaccuracy may have been inserted into the data, 2. after a data correction activity (inventory check) it is set to zero, 3. after a picker encounters a disruption thus confirming that there is an inaccuracy—the tag is set to 0 because the WMS is updated with the correct data for the location, and 4. after a replenishment, it is set to zero for the replenished location.

An example of the tag values for a database containing information on locations of items in a warehouse.

<table><tr><td>Location</td><td>Item type</td><td>Item quantity</td><td>Tag (using EP)</td><td>Tag (tally)</td></tr><tr><td>1</td><td>A</td><td>30</td><td>0.02</td><td>1</td></tr><tr><td>2</td><td>A</td><td>20</td><td>0</td><td>0</td></tr><tr><td>3</td><td>B</td><td>15</td><td>0.0975</td><td>2</td></tr><tr><td>4</td><td>B</td><td>4</td><td>0.14265</td><td>3</td></tr><tr><td>5</td><td>-</td><td>0</td><td>0</td><td>0</td></tr></table>

## 4.4. The reporting mechanism switch

The WMS was configured to return the locations with the required item type and suficient quantity and also with either the lowest tag value (to avoid disruptions) or with the highest tag value (to find inaccuracies). Importantly, the values within the tags are, therefore, never shown to the pickers. Table 2 shows an example set of tag values that arise after using this mechanism (and in comparison to the simple tally value in the final column) to update the tags in the simulated WMS database. Note that locations 2, 3 and 4 are within 3 locations of an empty location, and so they apply an EP value of 0.05 rather than 0.02. The table shows the state of the WMS after 6 picks starting with an inventory check (i.e. all data was accurate). Items have been picked from location 1 once, location 3 twice, and location 4 three times; the tag values reflect this. Hence, location 4 is most likely to contain an inaccurate value. Location 2 is the best location to pick item type A from in order to avoid disruptions. In the warehousing example, a picker could aim to “avoid” disruptions by being prompted to pick from storage locations that are most likely to contain accurate data. For ex: ample, if 10 items of type ‘A’ product can be picked by either storage location 1 or 2 (according to the WMS), then the “avoid” configuration would choose the location that is more likely to include accurate data in the WMS (i.e. location 2). The picker could aim to find inaccuracies by being prompted to pick from storage locations that are most likely to contain inaccurate data. In this way, visiting a storage location to perform a picking task is more likely to lead to a disruption that will allow the picker to notice the data inaccuracy too (e.g. a picker arrives at a location where there are too few items and so they know that there is an inaccuracy because they cannot complete their task). Whether it is the wrong quantity, item type or both, this can be reported back to the warehouse manager to update the WMS with the data reflecting the actual observation, and the tag is set to 0. At this point the manager knows that there is definitely another inaccuracy somewhere in the warehouse where the remaining missing items are. The warehouse manager may then decide to start an investigation to find the missing items (during picking activities) or could document the error and determine if an inventory check is needed (warehouses typically use the number of encountered inaccuracies as one way of triggering an inventory check).

In order to better understand the use of the two configurations, it is important here to diferentiate again between data inaccuracies and operational disruptions. As noted previously, inaccuracies do not always lead to disruptions unless the picker is asked to perform a task that they cannot complete due to the inaccuracy itself, and they will only know to report back when they face a disruption; and the tag is set back to 0 for the relevant location because the WMS is corrected. However, this does not correct the inaccuracy entirely because there is still a second instance of the inaccuracy in the warehouse where the missing items are located.

## 5. Experimental evaluation

This section describes the experimental simulation that Potential Problem Data Tagging was evaluated on, based on the previously described warehousing picking scenario. The following hypotheses were tested in the avoid and find configurations respectively:

AH0: There is no diference between the number of disruptions encountered when using Potential Problem Data Tagging to avoid disruptions compared to using a WMS as normal.

AH1: Fewer disruptions are encountered when using Potential Problem Data Tagging to avoid disruptions compared to using a WMS as normal.

FH0: There is no diference between the number of disruptions encountered when using Potential Problem Data Tagging to find dis ruptions compared to using a WMS as normal.

• FH1: More disruptions are encountered when using Potential Problem Data Tagging to find disruptions compared to using a WMS as normal.

These hypotheses were analysed under diferent cases including: using simple tally values for the tags versus using EP set to 0.02, replenishing items versus not replenishing items, and use of two diferent EP values of 0.02 as the default and 0.05 when a misreplacement is more likely to occur. Potential Problem Data Tagging avoid and find configurations do not eliminate disruptions, but shift them until later or earlier picking tasks respectively; the hypotheses were therefore also compared for 1 to 100 picks against 1 to 200 picks.

## 5.1. Simulating the warehousing problem

To test the aforementioned hypotheses, a simulation methodology was chosen. Typically, simulations have advantages over other research methods if a study concentrates on mechanisms and processes [54] like the warehouse picking operation studied here. Indeed, simulation approaches have been followed often in process analyses and are a com monly used tool to investigate warehouse operations [55–57].

The warehousing decision-making problem was implemented in software (using Java and MySQL) with one database representing the WMS and another, the physical warehouse. Operations on the warehouse and WMS were modelled by querying and updating the data in both databases, and inaccuracies could be checked by comparing the two. In the simulation. orders arrive at the warehouse and the WMS chooses the locations to pick items from that satisfy the orders. While picking the items, pickers can make the following mistakes, which result in inaccuracies, and can subsequently lead to disruptions: 1. misreplacement (occurring when, after taking all the items of a shelf, pickers put the remaining quantity back into the wrong empty location), 2. picking from the wrong location (occurring when a picker takes the items from a diferent location to the one that is specified on the picking list). As a result of these two mistakes, the following three disruptions can be encountered in the simulation: D1 (empty locations), D2 (wrong items) and D3 (WMS rejects orders that the warehouse can fulfil). Disruption D4 (WMS accepts orders that the warehouse cannot fulfil) is not faced in the simulation because the orders were chosen so that the warehouse can always satisfy the order. In the normal case, referred to in the hypotheses, there is no indication of priority of which locations are inaccurate or not (because as noted previously in Section 2, there is no current solution that can provide this). The normal case, however, does correct some inaccuracies in a sensible way, including when the picker does not find enough items to pick or finds the wrong item type, they return and update the WMS to reflect what they ob served. This sensible correction of inaccuracies is also done in the same way for the avoid and find configurations in order that the comparison is fair. Note that this type of correction does not solve the inaccuracy entirely because there is another inaccuracy instance (described at the end of Section 4) where the items have been moved to, which requires a more thorough check to find and correct. Due to the complexity of this check, it was not implemented.

Table 3  
Parameterisation of the experimental variables.

<table><tr><td>Variable</td><td>2 DOF</td><td>12 DOF</td><td>60 DOF</td></tr><tr><td>Warehouse locations</td><td colspan="3">100 (each is unique and only one item type is allowed in one location)</td></tr><tr><td>Initial configuration of the warehouse and WMS</td><td colspan="3">No inaccuracies, random insertion of item type, random insertion of quantity, random placement into locations. 5 different initial configurations were created and used as blocking factors in the trials.</td></tr><tr><td>Empty locations</td><td colspan="3">20 (randomly distributed)</td></tr><tr><td>Number of different item types in the warehouse</td><td>Random between 1 and 50</td><td>Random between 1 and 5</td><td>1 (all items are the same type)</td></tr><tr><td>Quantity for each item type in the warehouse</td><td>Random between 50 and 100</td><td>Random between 1 and 100</td><td>Random between 1 and 100</td></tr><tr><td>Orders (picking tasks) per trial</td><td colspan="3">200 per trial. The order contains one random product type and quantity. Orders were chosen deliberately so that the warehouse can always satisfy the order. (quantity and item type) by selecting an existing item type and not exceeding the quantity in the warehouse.</td></tr><tr><td>Order quantity</td><td>Random between 1 and 5 (or maximum in the warehouse)</td><td>Random between 1 and 20 (or maximum in the warehouse)</td><td>Random between 1 and 20 (or maximum in the warehouse)</td></tr><tr><td>Insertion of errors (misalignments)</td><td colspan="3">1% error rate (2 errors), 5% error rate (10 errors), and 20% error rate (40 errors)Attempted at random picking tasks. Some may not be successful if there is nothing to pick for that task or there are no locations available to misreplace items. The first location (with the same item type or empty) given by the WMS is chosen to misreplace the items or pick from the wrong location.</td></tr><tr><td>Types of errors inserted</td><td colspan="3">Misreplacement and pick from wrong location. Always split 50% each per trial. For misreplacements, they are 4 × more likely to occur if there are empty locations are within 3 locations of the pick location.</td></tr><tr><td>Satisfying orders</td><td colspan="3">Pickers only pick from single locations that have enough quantity available to satisfy the order.</td></tr><tr><td>Picking policy</td><td colspan="3">The actual location from which items are picked is chosen as the first location in the list generated by the WMS.</td></tr><tr><td>Inaccuracy correction</td><td colspan="3">If an inaccuracy is found, it is corrected only by updating the entry in the WMS. The other location where the items have been misplaced to was not updated in the WMS (as in reality, this would need to be physically found).</td></tr></table>

## 5.2. Experimental configuration and measurement

The experiments were run over 500 trials of 200 picking tasks for each of the three configurations: normal, avoid and find. The simulation explored three diferent error insertion rates (1%, 5%, and 20%) and three diferent DOF (2, 12, 60). The hypotheses were tested for all of these combinations. A 20% error rate is a very high value for warehouses, 1% is a low value, and 5% represents a typical value. A DOF of 2 is the minimum possible, and 60 is the average DOF that results from having all items the same in the warehouse simulation; 12 DOF re presents a typical normal value that results from having 5 diferent items in the warehouse.

The experimental variables and their parameterisation are summarised in Table 3, with the diferences shown for each DOF. All other factors were randomised (see Table 3). The disruptions were measured by incrementing a counter when the picker faced a disruption. A picker may pick from a location with an inaccuracy and not know about it if there are more than enough items to pick; to reflect reality, these instances were not counted as disruptions in the simulation.

## 6. Simulation results

This section presents the results of the simulation for avoiding dis ruptions and finding inaccuracies versus a normal operation of a WMS. A Student's t-test [58] was used to identify any significant diferences between the mean number of disruptions encountered.

## 6.1. Using a tally or a static setting of EP values

The first results shown are for the tally values and EP set to 0.02, which were confirmed as being the same after simulation executions of each. This is because having EP set to a single value and using the formula in Table 1 is logically the same as using a tally; the only difference being in the symbols used with the EP values providing a more useful interpretable probability value as described in Section 3.1.

## 6.1.1. Avoidance of disruptions

Fig. 3 illustrates the mean values for all cases tested. In all cases (including for 200 and 100 picks) Potential Problem Data Tagging is significantly diferent from the normal at the 99.9% level leading to reject the null hypothesis (AH0) in these cases; the only exceptions being for 200 picks at the 1% error rate with 2 and 12 DOF, which are not significant, and the 5% error rate with 12 DOF, which is only significant at the 95% confidence level.

## 6.1.2. Finding inaccuracies

When attempting to find inaccuracies, all results are significant at the 99.9% level, and the 1% error rate with 12 DOF is significant at the 95% level. Fig. 4 shows the comparison of the approaches against the normal operation of a WMS. The results show that in all cases save one, Potential Problem Data Tagging is significantly diferent from the normal operation of a WMS at the 99.9% confidence level. The other case (1% error rate with 12 DOF) is still significant, but at the 95% confidence level instead of 99.9%. For the first 100 picks, the 1% error rate with 12 DOF also becomes significantly diferent at 99.9% confidence. This indicates that the find performance also degrades over time. This can also be seen by observing the larger diferences between the mean number of inaccuracies found between the cases in Fig. 4b compared to the smaller diferences in Fig. 4a. The null hypotheses (FH0) are rejected for all cases when attempting to find inaccuracies using Potential Problem Data Tagging.

A confidence interval estimates analysis indicates that it is possible to find from approximately 7 to almost 8 more inaccuracies over 200 picks compared to the normal situation for the 20% error rate with 60 DOF. This equates to finding between 17.5% and 20% of the 40 inaccuracies inserted into the data in 200 picks. This falls to approximately 4 to 6 inaccuracies for the 20% error rate with 2 and 12 DOF.

![](/api/attachments/WCT6NF53/fulltext/images/bac133c70b533b34b46d02e619a4100561d9f8d0df9062a6f32f6ca6bfc99f91.jpg)

![](/api/attachments/WCT6NF53/fulltext/images/bee418cee6d79e01e18ceb2acb0af9c11d21cb5d885424ff319e856352755937.jpg)  
Fig. 3. Mean number of disruptions encountered for Potential Problem Data Tagging (avoid case) versus the normal operation of a WMS (Tally and EP = 0.02 case), a = 200 picks and b = 100 picks.

When considering only the first 100 picks for the 20% error rate with 2 DOF, the number of inaccuracies found falls to approximately 2. It also falls for the 20% error rate with 60 DOF to between 6 and 7 inaccuracies. However, for the 20% error rate with 12 DOF the confidence interval itself increases from (5.58, 6.23) for the first 100 picks to (4.54, 6.55) for all 200 picks.

## 6.2. Using dynamic setting of EP values

Secondly, the results are shown for dynamically setting the EP value based on the context (using a default value of 0.02 and increased to 0.05 when it is more likely that an inaccuracy will be inserted); these results are also presented both with and without replenishment of items in the warehouse.

## 6.2.1. Without replenishment

When dynamically setting the EP value based on the context to avoid disruptions, the only cases that were not significant were for DOF of 2 and 12, for the 1% error rate for 200 picks. For the 100 picks case only the DOF of 2 for 1% was not significant. All other cases were very significant over the 99.9% level. For finding inaccuracies, all cases were very significant except the 1% error rate for 12 DOF for 200 picks, which was significant at the 99% level; and for 100 picks the 1% error rate for 2 DOF was significant at the same level. The results for these cases are shown in Figs. 5 and 6.

## 6.2.2. With replenishment

The previous results were collected without replenishment of items in the simulation. The following results included items being replenished back to a quantity of 100 at 75 and 150 picks for locations where the quantity was lower than 10 items. For avoiding disruptions, all cases are significant at the 99.9% level (Fig. 7).

When attempting to find inaccuracies, the results show that in all cases save one, Potential Problem Data Tagging is significantly diferent from the normal operation of a WMS at the 99.9% confidence level (see Fig. 8a). This is also true for the first 100 picks (see Fig. 8b). For both 100 and 200 picks, the other case (1% error rate with 2 DOF) is stil significant, but only at the 95% confidence level. The null hypotheses (FH0) are therefore rejected for all cases.

## 7. Analysis and discussion

For both the avoid and find configurations, the performance against the normal improves as the error rate increases. For the avoid 200 picks case, the confidence interval estimates increase monotonically as the error rate increases. This is also the case for the find configuration save for 20% error rate with 2 DOF case, which does not difer drastically and is likely due to the inherent variation in the simulation. As the error rate increases, the false positive tags (that result because the error does not occur) are replaced by true positives (see “error does not occur” and case 1 in Fig. 2). Hence, the tags become more accurate as the error rate increases. The improvement can also be explained partly due to the fact that, when avoiding disruptions, the normal case performs comparatively well when there are few errors. This is because there is a high chance a disruption will be avoided since there are many storage locations that an item can be picked from without causing a disruption.

In general, the find case shows greater performance than the avoid case, which can be seen by the larger number of inaccuracies that can be found (especially for higher error rates with higher DOF) compared to the smaller number of disruptions avoided in the avoid case. There are a number of reasons why find outperforms the avoid case: in the find configuration the same storage locations are picked from for dif ferent orders until their quantity runs out (the performance is reduced slightly due to the replenishments). As a result, the find configuration tends to group the errors into a smaller number of locations that have a much higher chance of containing an inaccuracy. This is not true in the normal case, where the inaccuracies are more uniformly spread be tween locations. This phenomenon also makes it more likely that a location with an inaccuracy from a previous picking task is accidentally tagged again as having an inaccuracy. Therefore, some of the false negatives become true positives, which improves the performance.

Regarding DOF, one would expect the performance to improve as it increases because there is more opportunity to choose diferent storage locations that are more or less likely to be inaccurate. This is confirmed in all cases where the confidence interval estimates show that as the DOF increase the performance of the find and avoid against the normal improves. The results show that this efect is larger as the error rate increases.

The confidence interval estimates analysis indicates that both the avoid and find configurations for 200 picks very slightly outperform 100 picks. This outperformance is more evident for the 20% error rate compared to 1% and 5%. In the find case this again improves. This is likely due to the solution always outperforming the normal and having more time to avoid disruptions or find inaccuracies in the 200 picks case. It is more evident in the higher error rate and higher DOF case due to the solution performing the best in this situation.

b  
![](/api/attachments/WCT6NF53/fulltext/images/559cb917ca5da06804774644ed675694409779afd0c92199c60b19a1f42ba479.jpg)

![](/api/attachments/WCT6NF53/fulltext/images/e22c1bf9fc70c6731b098aef1cff4df3adcc0cee7f397ac3b2040735af9d4cc7.jpg)  
Fig. 4. Mean number of inaccuracies found for Potential Problem Data Tagging (find case) versus the normal operation of a WMS (Tally and EP = 0.02 case), a = 200 picks and b = 100 picks.

Finally, in cases where it is dificult to estimate the probabilities, the information that must be known is only when events occur that may cause data to become inaccurate. This is demonstrated by the first set of analysis where we found no diference in the results when using a tally compared to using a static setting for the EP value.

## 7.1. Limitations

While the proposed approach can help to avoid and find operational disruptions, there are various limitations. Firstly, the events that cause the inaccuracy need to be known in advance; although it is not necessary to know which particular instance of the event will cause an inaccuracy. Furthermore, the approach requires that each time the event occurs it is possible to automatically record that it has taken place, and also know which database records are the correct ones to tag. This may not be feasible or possible for some scenarios. Despite this reliance on the events, a benefit is that it is often inexpensive to simply record when an event occurs and keep track of this in a database. Contrast this with an RFID tracking solution that requires expensive hardware equipment to be installed. Another limitation is that the approach does not eradicate the disruptions, but continually avoids them. This is mitigated in some part with the ability to find the inaccuracies when the approach is configured this way; also the ability to avoid disruptions for as long as possible is certainly useful in various settings such as in times of peak load on a warehouse. However, a superior solution would be able to both detect and eradicate the inaccuracies. Also, the approach proposed requires that the events are independent and possess the memoryless property, which are limiting. The approach not being a proper metric of accuracy is also limiting as it is unknown whether the tag values can be used directly in a traditional data quality assessment. Another limitation relates to the simulation which did not measure disruption D4. The orders were chosen so that the warehouse can always satisfy the order because in prior executions of the simulation, it was found that many orders were not be picked when an order required more quantity to be available in the warehouse. In reality, many warehouses have a separate area where items are stored in bulk (so the items are available, but just not easily accessible), and the picking locations (providing fast access to items) are replenished according to predictions of future orders. Hence, D4 is a rare issue compared to the others, and was therefore not measured in the simulation. A more general point about the choice of simulation as a methodological tool needs to also be raised. Even though simulations are often used to study warehousing processes like picking and replenishment, their limitations are known as their results can often afected by the setting. We believe that this study has been designed in a way that allows a fair illustration of the benefits and limitations of our approach for a wide range of settings and cases and we note that analytical models could be used for further evaluation of this approach in future research.

![](/api/attachments/WCT6NF53/fulltext/images/572837c6dab0cd9b4f94ac3acceca84f560f81ad2b4dbf8c452d24fc5f642f74.jpg)

![](/api/attachments/WCT6NF53/fulltext/images/be547aa071b7a77634bf643906790bfa867e46462a8c34363679f44018e000fc.jpg)  
Fig. 5. Mean number of disruptions encountered for Potential Problem Data Tagging (avoid case) versus the normal operation of a WMS (dynamic case without replenishment), a = 200 picks and b = 100 picks.

![](/api/attachments/WCT6NF53/fulltext/images/91c6854a447b416fab90216c340d7a6f6ff2eebb0bc67d4282f9e94ad7195527.jpg)

![](/api/attachments/WCT6NF53/fulltext/images/189c18b6cc1d34eae3fd507ebc2e95a334afa491a811545f3fa744aa24a674f6.jpg)  
Fig. 6. Mean number of inaccuracies found for Potential Problem Data Tagging (find case) versus the normal operation of a WMS (dynamic case without replen ishment), a = 200 picks and b = 100 picks.

## 8. Summary and conclusion

This research has proposed and evaluated an alternative, and automatic, way of populating accuracy tags in information systems so that they can help to avoid operational disruptions and/or to find the inaccuracies that cause the disruptions. Both the avoid and find config urations of Potential Problem Data Tagging demonstrate an improvement over the normal case and increasingly so as the error rate and DOF increase. This brings the concept of data tagging closer to adoption in actual information systems because the approach reduces the level of data tag maintenance required due to it being highly automated. One advantage of the approach is that it is possible to switch between the avoiding and finding configurations dynamically, therefore, it is possible to better to control when data with inaccuracies are encountered versus when the efects of poor data want to be avoided. This switching ability raises questions about when is the best time to perform a data quality detection/correction program, and deliberately “setting up” the data so that it is primed for a DQ detection/correction program. Finally, the choice of the warehousing decision-making task in this work illustrates how the experimental setting can be simplified in future data tagging research because 1. it is easy to measure whether the tags themselves are of benefit or not, 2. the decision-making task can be carried out automatically by the information system thus removing all “decision-maker issues”, such as being overloaded and inconsistent, and 3. the tags do not need to be presented to the user, thus avoiding issues with representation and visualisation of tags [59,60]. Future work could consider extending these types of tags with values of utility in order that they can be changed and used for diferent contexts [61] especially in Big Data environments [62], and this is important given that data is being repurposed for data analytics-related decision-making [63] and performance reporting [64] at the same time as being used operationally.

![](/api/attachments/WCT6NF53/fulltext/images/df0b12f6443384258a7fb6a1a0e5e2cc6a519ba2b45d5eb26583cf29f70ae3d1.jpg)

![](/api/attachments/WCT6NF53/fulltext/images/92d08ac6c152ebdef68fd2ca53b75a116964321583e897df502933d58abc4aa9.jpg)  
Fig. 7. Mean number of disruptions encountered for Potential Problem Data Tagging (avoid case) versus the normal operation of a WMS (dynamic case with replenishment), a = 200 picks and b = 100 picks.

a  
![](/api/attachments/WCT6NF53/fulltext/images/23351d6c2c33fd599e23bc50c6be3dd82955e306532ce463af0957e5458bdb89.jpg)

b  
![](/api/attachments/WCT6NF53/fulltext/images/54f701b087386f6fde78ab6c64136bcadedb5e74d0d73f1e2e137bd81c024cac.jpg)  
Fig. 8. Mean number of inaccuracies found for Potential Problem Data Tagging (find case) versus the normal operation of a WMS (dynamic case with replenishment), a = 200 picks and b = 100 picks.

## Acknowledgements

We acknowledge YH Global Supply Chain Co., Ltd. for supporting this research financially, and for providing access to their operations and expertise. We also thank Alena Puchkova for her help.

## References

[1] G. Shankaranarayan, M. Ziad, R.Y. Wang, Managing data quality in dynamic de cision environments: an information product approach, Journal of Database Management (JDM) 14 (4) (2003) 14–32

[2] R. Wang, M.P. Reddy, B. Kon, Toward quality data: an attribute-based approach, Decision Support Systems 13 (3–4) (1995) 349–372.

[3] G. Shankaranarayanan, A. Even, The metadata enigma, Communications of the ACM 49 (2) (2006) 88–94.

[4] W. Kent, The breakdown of the information model in multi-database systems, SIGMOD Rec. 20 (4) (1991) 10–15.

[5] A. Motro, I. Rakov, Not all answers are equally good: estimating the quality of database answers, Flexible Query Answering Systems, Springer US, Boston, MA, 1997, pp. 1–21.

[6] A. Parssian, W. Yeoh, M.S. Ee, Quality-based SQL: specifying information quality in relational database queries. Computer 48 (9) (2015) 69–74.

[7] N.K. Yeganeh, S. Sadiq, M.A. Sharaf, A framework for data quality aware query systems, Information Systems 46 (2014) 24–44.

[8] D. Ardagna, C. Cappiello, W. Samá, M. Vitali, Context-aware data quality assess ment for big data. Future Generation Computer Systems 89 (2018) 548–562.

[9] C. Fisher, B. Kingma, Criticality of data quality as exemplified in two disasters, Information & Management 39 (2) (2001) 109–116.

[10] K.M. Hüner, A. Schierning, B. Otto, H. Österle, Product data quality in supply chains: the case of Beiersdorf, Electronic Markets 21 (2) (2011) 141.

[11] T.C. Redman, The impact of poor data quality on the typical enterprise, Communications of the ACM 41 (2) (1998) 79–82.

[12] J.R. Marsden, D.E. Pingry, Numerical data quality in IS research and the implica tions for replication, Decision Support Systems 115 (2018) A1–A7

[13] I.N. Chengalur-Smith, D.P. Ballou, H.L. Pazer, The impact of data quality information on decision making: an exploratory analysis, JEEE Transactions on Knowledge and Data Engineering 11 (6) (1999) 853–864.

[14] C. Fisher, I. Chengalur-Smith, D.P. Ballou, The impact of experience and time on the use of data quality information in decision making, Information Systems Research 14 (2) (2003) 170–188.

[15] R. Price, G. Shanks, The impact of data quality tags on decision-making outcomes and process, Journal of the Association for Information Systems 12 (4) (2011) 323

[16] J. Hipp, M. Müller, J. Hohendorf, F. Naumann, Rule-based measurement of data quality in nominal data, International Conference on Information Quality (ICIQ), 2007, pp. 364–378.

[17] D.P. Ballou, H.L. Pazer, Designing information systems to optimize the accuracytimeliness tradeoff, Information Systems Research 6 (1) (1995) 51–72.

[18] L. English. Improving Data Warehouse and Business Information Ouality: Methods

for Reducing Costs and Increasing Profits, John Wiley & Sons, 1999.

[19] L. English, Plain English About Information Quality: Defining and Measuring Accuracy, DM Review, 2003.

[20] B. Heinrich, M. Klier, Metric-based data quality assessment — developing and evaluating a probability-based currency metric, Decision Support Systems 72 (2015) 82–96.

[21] N.R. Joglekar, E.G. Anderson, G. Shankaranarayanan, Accuracy of aggregate data in distributed project settings: model, analysis and implications, Journal of Data and Information Ouality 4 (3) (2013) 1–22.

[22] J. Han, D. Jiang, L. Li, Automatic accuracy assessment via hashing in multiple source environments, Expert Systems with Applications 37 (3) (2010) 2609–2620

[23] J.E. Olson, Data Quality: The Accuracy Dimension, Morgan Kaufmann, San Francisco, 2003

[24] Y. Zak, A. Even, Development and evaluation of a continuous-time Markov chain model for detecting and handling data currency declines, Decision Support Systems 103 (2017) 82–93.

[25] I.A. Gelman, Setting priorities for data accuracy improvements in satisficing deci sion-making scenarios: a guiding theory, Decision Support Systems 48 (4) (2010) 507–520.

[26] P.C. Nutt, How decision makers evaluate alternatives and the influence of com plexity, Management Science 44 (8) (1998) 1148–1166.

[27] G. Shankaranarayanan, A. Even, S. Watts, The role of process metadata and data quality perceptions in decision-making: an empirical framework and investigation, Journal of Information Technology Management 17 (1) (2006).

[28] A. Sarac, N. Absi, S. Dauzère-Pérès, A literature review on the impact of RFID technologies on supply chain management, International Journal of Production Economics 128 (1) (2010) 77–95

[29] N. DeHoratius, A. Raman, Inventory record inaccuracy: an empirical analysis, Management Science 54 (4) (2008) 627–641.

[30] H. Lee, O. Özer, Unlocking the value of RFID, Production and Operations Management 16 (1) (2007) 40–64.

[31] Y. Rekik, E. Sahin, Y. Dallery, Analysis of the impact of the RFID technology on reducing product misplacement errors at retail stores, International Journal of Production Economics 112 (1) (2008) 264–278

[32] H.-L. Chan, T.-M. Choi, C.-L. Hui, RFID versus bar-coding systems: transactions errors in health care apparel inventory control, Decision Support Systems 54 (1) (2012) 803–811

[33] Y.-J. Tu, W. Zhou, S. Piramuthu, A novel means to address RFID tag/item separation in supply chains, Decision Support Systems 115 (2018) 13–23.

[34] L. English, Information Quality Applied: Best Practices for Improving Business Information, Processes and Systems, John Wiley & Sons. 2009.

[35] C. Fisher. EJ. Lauria. C.C. Matheus, An accuracy metric: percentages, randomness. and probabilities, Journal of Data and Information Ouality (JDIO) 1 (3) (2009) 16

[37] Y. Wand, R. Wang, Anchoring data quality dimensions in ontological foundations Communications of the ACM 39 (11) (1996) 86–95

[38] T. Haegemans, M. Snoeck, W. Lemahieu, Towards a precise definition of data accuracy and a justification for its measure International Conference on Informatior Quality, 2016 (pp. 16–1).

[39] D. Suciu, D. Olteanu, R. Christopher, C. Koch, Probabilistic Databases, 1st ed., Morgan & Claypool Publishers, 2011.

[40] A. Parssian, S. Sarkar, V.S. Jacob, Assessing data quality for information products: impact of selection, projection, and Cartesian product, Management Science 50 (7) (2004).967–982

[41] S. Watts, G. Shankaranarayanan, A. Even, Data quality assessment in context: a

cognitive perspective, Decision Support Systems 48 (1) (2009) 202–211.

[42] H.-T. Moges, V.V. Vlasselaer, W. Lemahieu, B. Baesens, Determining the use of data quality metadata (DQM) for decision making purposes and its impact on decision outcomes — an exploratory study, Decision Support Systems 83 (2016) 32–46.

[43] V. Sessions, M. Valtorta, Towards a method for data accuracy assessment utilizing a Bayesian network learning algorithm, Journal of Data and Information Quality (JDIQ) 1 (3) (2009) 14.

[44] P. Woodall, M. Oberhofer, A. Borek, A classification of data quality assessment and improvement methods, International Journal of Information Quality 3 (4) (2014) 298–321.

[45] A. Maydanchik, Data Quality Assessment, Technics Publications LLC, 2007.

[46] V. Chandola, A. Banerjee, V. Kumar, Anomaly detection: a survey, ACM Computing Surveys 41 (3) (2009) 1–58.

[47] R. Lukyanenko, J. Parsons, Y.F. Wiersma, The IQ of the crowd: understanding and improving information quality in structured user-generated content, Information Systems Research 25 (4) (2014) 669–689.

[48] A. Wechsler, A. Even, Using a Markov-chain model for assessing accuracy degradation and developing data maintenance policies, AMCIS 2012 Proceedings, 2012.

[49] B. Heinrich, D. Hristova, A quantitative approach for modelling the influence of currency of information on decision-making under uncertainty, Journal of Decision Systems 25 (1) (2016) 16–41.

[50] B. Heinrich, M. Klier, Assessing data currency — a probabilistic approach, Journa of Information Science 37 (1) (2011) 86–100.

[51] B. Heinrich, M. Klier, M. Kaiser, A procedure to develop metrics for currency and its application in CRM, Journal of Data and Information Ouality 1 (1) (2009) 1–28.

[52] W. Fan, F. Geerts, Foundations of Data Quality Management, Morgan & Claypool Publ, San Rafael, Calif, 2012.

[53] B. Heinrich, D. Hristova, M. Klier, A. Schiller, A. Szubartowicz, Requirements for data quality metrics, Journal of Data and Information Quality 9 (2) (2018) 1–32.

[54] G.N. Gilbert, K.G. Troitzsch, Simulation for the Social Scientist, 2nd ed., Open University Press Maidenhead Fngland: New York NY 2005

[55] F. Faria, V. Reis, An original simulation model to improve the order picking

performance: case study of an automated warehouse, Computational Logistics 9335 (2015) 689–703.

[56] V. Giannikas, W. Lu, B. Robertson, D. McFarlane, An interventionist strategy for warehouse order picking: evidence from two case studies, International Journal of Production Economics 189 (2017) 63–76

[57] G. Pedrielli, A. Vinsensius, E.P. Chew, L.H. Lee, A. Duri, Haobin Li, Hybrid order picking strategies for fashion E-commerce warehouse systems, Proceedings of the 2016 Winter Simulation Conference (WSC), 2016, pp. 2250–2261.

[58] D.C. Montgomery, Design and Analysis of Experiments, 8th Edition Internationa Student Version edition, John Wiley & Sons, Singapore, 2012.

[59] G. Shankaranarayanan, B. Zhu, SPIDEQ - a prototype for decision making with quality metadata, Proceedings of the International Conference on Information Quality, Spain, 2016 (p. Paper 20).

[60] R.Y. Wang, D.M. Strong, Beyond accuracy: what data quality means to data con sumers, Journal of Management Information Systems 12 (4) (1996) 5–34.

[61] A. Even, G. Shankaranarayanan, Utility-driven assessment of data quality, ACM SIGMIS Database 38 (2) (2007) 75–93.

[62] J. Merino, I. Caballero, B. Rivas, M. Serrano, M. Piattini, A data quality in use model for big data, Future Generation Computer Systems 63 (2016) 123–130.

[63] P. Woodall, The data repurposing challenge: new pressures from data analytics, Journal of Data and Information Quality 8 (3–4) (2017) 11:1–11:4.

[64] V. Vallurupalli, I. Bose, Business intelligence for performance measurement: a case based analysis, Decision Support Systems 111 (2018) 72–85.

Philip Woodall is a Senior Research Associate at the University of Cambridge specialising in industrial data management. His particular research interest is in data quality, data sharing and data value. He has extensive experience working with international public and private organisations from various sectors, including transport, utilities, defence, public sector, manufacturing, and aerospace, to improve their data management practices. Philip worked previously in the software industry and gained his Ph.D. in Computer Science from Keele University.
