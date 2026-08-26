---
otero_id: 6510
otero_key: "GM22HNUS"
title: "Theorizing Process Dynamics with Directed Graphs: A Diachronic Analysis of Digital Trace Data"
authors: "Brian T. Pentland; Emmanuelle Vaast; Julie Ryan Wolf"
year: "2021"
journal: "MIS Quarterly"
doi: "10.25300/misq/2021/15360"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# THEORIZING PROCESS DYNAMICS WITH DIRECTED GRAPHS: A DIACHRONIC ANALYSIS OF DIGITAL TRACE DATA<sup>1</sup>

Brian T. Pentland Michigan State University East Lansing, MI, U.S.A. {pentland@broad.msu.edu}

Emmanuelle Vaast McGill University Montreal, CANADA {emmanuelle.vaast@mcgill.ca}

Julie Ryan Wolf University of Rochester Rochester, NY, U.S.A. {Julie\_Ryan@URMC.Rochester.edu}

The growing availability of digital trace data has generated unprecedented opportunities for analyzing, explaining, and predicting the dynamics of process change. While research on process organization studies theorizes about process and change, and research on process mining rigorously measures and models business processes, there has so far been limited research that measures and theorizes about process dynamics. This gap represents an opportunity for new information systems research. This research note lays the foundation for such an endeavor by demonstrating the use of process mining for diachronic analysis of process dynamics. We detail the definitions, assumptions, and mechanics of an approach that is based on representing processes as weighted, directed graphs. Using this representation, we offer a precise definition of process dynamics that focuses attention on describing and measuring changes in process structure over time. We analyze process structure over two years at four dermatology clinics. Our analysis reveals process changes that were invisible to the medical staff in the clinics. This approach offers empirical insights that are relevant to many theoretical perspectives on process dynamics.

Keywords: Processual dynamics, event logs, trace data, process theorizing, routine dynamics, diachronic analysis

## Introduction

From the beginning, research on information systems (IS) has been concerned, implicity or explicitly, with process change. The earliest studies on “IT impacts” focused on how computers changed work and business (Keenoy 1958; Hoos 1960). In the 1990s, we began to study and theorize about structuration (DeSanctis and Poole 1994), coevolution (Yates 1993), and process reengineering (Hammer 1990; Grover et al. 1995). Currently, research on social media (Leonardi and Vaast 2017; Vaast et al. 2017) and platform evolution (Tiwana et al. 2010) has examined how digital innovation transforms our lives and the economy. In a broad sense, the fact that technology changes how things get done (and vice versa) is the raison d’être of the IS discipline.

In this research note, our central argument is that we have enormous opportunities for measuring and explaining process dynamics. By process dynamics, we mean changes in the structure of a process over time. Measuring this kind of change requires some form of diachronic analysis (Barley 1990; Berente et al. 2019). In the example we present here, we demonstrate how process mining methods can be used to advance a wide range of theoretical topics in IS and organizations.

This opportunity exists because widespread digitization is creating a lot of data about processes that were never available before and we have new tools for visualizing and analyzing that data (Berente et al. 2019). From research on process mining, we have increasingly sophisticated techniques for detecting and measuring process change (Maaradji et al. 2017; Yeshchenko et al. 2021), analyzing process variations (Rosa et al. 2017), and comparing formal process models (Becker and Laue 2012; Van Dongen et al. 2013). From research on process organization studies (Langley and Tsoukas 2016), we have novel theory about a wide range of processual phenomena (Tsoukas and Chia 2002; Feldman et al. 2016). Notably, the scholarship that measures process change is not concerned with theorizing it, while the scholarship that theorizes process change has struggled to measure it systematically. Process theory and process measurement are flourishing, but on separate islands. These islands need to be bridged because, in any research tradition, careful attention to empirical phenomena is the best way to develop and test theory.

To help build this needed bridge, we provide an example of how digital trace data can be used to theorize about process dynamics. By trace data, we refer to the timestamped event log data typically used for process mining (Dumas et al. 2018; van der Aalst 2013). We step through the definitions, assumptions, and mechanics of a simple approach to process mining that is based on representing processes as weighted, directed graphs. Using this representation, we offer a precise definition of process dynamics that focuses attention on describing and measuring changes in process structure. We analyze process structure over two years at four dermatology clinics. Our analysis reveals process changes that were invisible to the medical staff in the clinics. After presenting our method and findings, we discuss how this method relates to and bridges existing literatures. The insights we can gain from this approach to process dynamics are novel and would be unattainable by any other means.

## Two Motivations, One Opportunity

## An Empirical Mystery: Why Were These Routines Changing?

Our first motivation for this research note was an empirical mystery (Alvesson and Kärreman 2007; Locke et al. 2008). In a research project on process complexity (NSF SES-1734237), we noticed process changes that we could not explain. We had been studying the complexity of healthcare routines using electronic medical record (EMR) data from a set of four dermatology clinics at the University of Rochester Medical Center. The EMR audit trail allowed us to conduct a detailed cross-sectional comparison of the four clinics (Ryan et al. 2019). We found, for example, that clinics’ organization had a significant influence on the complexity of the recordkeeping task. In particular, when nurses were responsible for EMR entry (rather than residents or scribes), complexity was reduced.

While looking closely at the data, we noticed sudden changes that occurred simultaneously in all four clinics. When we asked clinical staff to explain what had happened, they were unaware that anything had changed and they had no explanation for our observations. The IT staff responsible for maintaining the EMR system confirmed that the changes were not due to system upgrades or some error in retrieving the data. Unraveling the mystery of the dermatology clinics provides a concrete case study of how to measure and explain process change with digital trace data.

## A Scholarly Gap: Two Islands of Process Research

Our second motivation comes from a remarkable gap in the research literature on process. While investigating the mysterious process changes in the dermatology clinics, we looked for relevant research on process change. Our search led us to two distinct islands.

On one island is scholarship on process theory (Hernes 2014; Langley and Tsoukas 2016) and routine dynamics (Feldman et al. 2016). This literature has a lot of theories and explanations for why processes change. For example, research on routine dynamics is focused on how routines emerge, are performed, and transformed over time within and among organizations (Feldman et al. 2016). Process theory provides sophisticated theoretical lexicons that illuminate how systems get reproduced over time or how change actually unfolds (Tsoukas and Chia 2002). Process research often adopts a practice perspective to make sense of the ways in which new technologies participate in practical and relational transformations (Feldman and Orlikowski 2011). Building upon philosophical foundations from Whitehead (1929/1978), James (1909/1996), Mead (1934/1962), and Dewey (1938/2008), and the more recent work of Hernes (2014), Rescher (1996), and Shotter (2006), it has relied mostly upon intensive, qualitative methods that enable researchers to understand why processes change (Langley and Tsoukas 2016).

On the other island is research on process mining (van der Aalst 2011; van der Aalst et al. 2011). This literature is concerned with methods for rigorously and efficiently mapping processes from event log data. It includes methods for detecting process change (Maaradji et al. 2017) and methods for evidence-based redesign of business processes (Reijers and Mansar 2005; Cho et al. 2017). This scholarship has developed sophisticated techniques that allow researchers to model processes precisely and to engage in the design of efficient business processes (Dumas et al. 2018). Scholarship from this island has been particularly innovative in developing detailed computational process models with significant practical applications (van der Aalst 2012). However, it has not much concerned itself with theoretical development about why processes may change.

These two research communities both study organizational processes, but they are completely separate. The recently published Handbook of Process Organization Studies (Langley and Tsoukas 2016) includes over 40 chapters on processes in organizations, but it does not contain a single citation of any research on process mining. Likewise, in the last ten years of proceedings from the International Conference on Business Process Management (2009-2018),<sup>2</sup> there is not a single citation of the organizational research community. One literature has sophisticated tools for measuring process change, the other literature has novel theories for explaining process change, but there is virtually no communication between them. A literature review by Breuker and Matzner (2014) reached a similar conclusion using journal articles retrieved from Scopus: out of 8,312 articles located in (or merely citing) the literature on process mining or organizational routines, there were no articles located in both fields and only nine articles that cited literature from both fields. More recently, Grisold et al. (2020) also noted this separation and have suggested possibilities for bridging the gap.

The separation is not surprising since these literatures come from different scholarly traditions (computer science vs. sociology/organization theory), rely on different methods (process mining vs. participant observation), favor different representations (petri nets vs. textual description), and have different objectives (design vs. explanation). We present these differences in more detail below, but the key point is clear: an opportunity exists to apply methodological tools from process mining to the theoretical problem of process dynamics.

## A Methodological Opportunity: Digital Trace Data for Diachronic Analysis

Digital trace data constitute an essential resource for researchers to engage in “computationally intensive theory development” (Berente et al. 2019, p. 50). Digital trace data of the kind used in process mining (van der Aalst 2013) provide unprecedented opportunities for researchers to bridge these two streams of scholarship by measuring and theorizing about process dynamics. These opportunities stem from the availability of time-stamped process traces that are commonly referred to as event logs or audit trails (van der Aalst 2013).

While time-stamped event logs are commonly used for process discovery and conformance checking when the process is expected to be relatively stable (van der Aalst 2011), they can also be used for diachronic analysis. In linguistics, diachronic analysis refers to changes in a language over time (de Saussure 1919). In organizational research, it refers to changes in action patterns over time (Barley 1990). As we demonstrate here, diachronic analysis is an ideal approach for documenting changes in process over time. Diachronic analysis allows us to measure process dynamics that are difficult to observe and measure through traditional participant observation. With the growing availability of digital data that trace the execution of organizational processes, there are enormous opportunities for new research on process dynamics. In the sections that follow, we outline the theoretical and methodological foundations required to make this possible.

## Representing Processes as Directed Graphs

A process can be defined as a progression or sequence of events (Van de Ven and Poole 1995). Thus, to describe a process, we need two parts: (1) a lexicon of events, and (2) the sequential relations between those events. As it turns out, this is exactly the same information needed to define a directed graph (West, 1996). In this section, we lead the reader step by step through the terminology and concepts needed to describe the structure of a process as a weighted, directed graph.<sup>3</sup>

The lexicon defines the vertices (V). The lexicon is the list of events that make up the process. As Berente et al. (2019) note, there are many alternative ways to derive the lexicon for a process. When used in a directed graph, the lexicon of events becomes the vertices (nodes) of the network (V). For example, in the EMR audit trail data, the lexicon consists of 300 distinct events that are recorded by the EPIC EMR system.<sup>4</sup>

The sequence defines the edges (E). Sequential relations between events can be represented as edges (ties) in a directed graph. This is typically referred to as an edge list, (E). Between any two events in the lexicon, there may or may not be a direct sequential relation. For example, in the EMR audit trail, we can observe and count the sequential relation between any pair of events in the audit trail. The counts are the weights on the edges of the directed graph.

Vertices and edges define the process (P). In general, we can describe the structure of any discrete process, P, as a list of vertices, V, and a list of edges, E: P(V, E). This is standard notation and terminology in graph theory (West 1996).<sup>5</sup> The list of edges can be weighted, so that it shows the relative frequency of the edges in the process. In the process mining literature, this type of graph is referred to as a “directly-follows graph” (van der Aalst 2019, p. 321).

Figure 1 shows an example of one day in one dermatology clinic represented as a directed graph. It summarizes the action sequences for 25 visits. We include this image to reinforce a critical point about process measurement: processes can be very complicated. There is no way to tell what is going on here (or compare one day to the next) by simply looking at the graph.

The directed graph in Figure 1 seems complex because we have included all 300 event codes in the lexicon. Some researchers advocate for reducing the granularity of observed data for improved methodological rigor and to facilitate theoretical interpretation (e.g., Gioia et al. 2013; Berente et al. 2019). While this makes sense for some kinds of data and research questions, it is both undesirable and unnecessary for the procedure we present here. Reducing the number of codes from the lexicon is undesirable here because it throws out information. Without strong a priori knowledge of which codes are important, reducing or combining codes threatens the validity of the data. Furthermore, it is not necessary to recode the signal for synchronic or diachronic analysis (Barley 1990). As we demonstrate below, we can compare the signal to itself to detect change and compare it to other signals to detect difference without throwing out valid details in the data. The approach we demonstrate can be used with data at any level of granularity. Data can be analyzed at the finest level of granularity available. Alternatively, if a valid data reduction strategy is available, recoded or filtered data could be used.

![](/api/attachments/GM22HNUS/fulltext/images/59fab70a46a5d683e4cada9a86145add5435536ddd2c6be30070ffad32df1fc8.jpg)  
Figure 1. Process as Directed Graph

## Limitations and Alternatives

There are many alternative ways of representing process, each of which has distinct advantages and limitations. A weighted, directed graph is an indicator of process structure, not a formal process model like UML (Fowler and Kobryn 2004) or an executable process model, like BPMN (Chinosi and Trombetta 2012). Like any process description, it has limitations. Unlike system dynamics models (Forrester 1968), it does not represent stocks and flows of resources and it is limited to discrete (not continuous) processes. Unlike a Petri net (Murata 1989; Reisig and Rozenberg 1998), a directed graph does not capture concurrency or control flow. Petri nets have distinct advantages when it comes to modeling and analyzing particular processes for the purpose of design and improvement (Reijers and Mander 2005; Cho et al. 2017; van der Aalst 2019). For example, Petri nets can be used to analyze and avoid process deadlock (e.g., two or more concurrent threads, each waiting for the other to complete before it can proceed) (Ezpeleta, Colom and Martinez 1995). Alternatively, declarative models capture temporal precedence constraints from event logs (Maggi et al. 2012).

The main advantages of directed graphs are their proven utility in practice, their computational simplicity, and their flexibility. In commercial process mining applications, simple directed graphs of the kind we use here are common (van der Aalst 2019). They have also been used in empirical research on organizational routines (Pentland et al. 2010) and in the simulation of routine dynamics (Pentland et al. 2012; Pentland et al. 2020). Weighted, directed graphs are useful for empirical research because they are very flexible. P(V, E) can be constructed based on interviews, archival records, or observations of a running process. The data can be at any level of temporal granularity or abstraction, as long as it consists of sequentially related events. Unlike process design artifacts (e.g., UML, BPMN, or simple block diagrams), P(V, E) is based on empirical evidence about actual process execution. When the running process changes, the graph changes. As demonstrated below, P(V, E) is a sensitive indicator of process structure and an ideal tool for empirical research on process dynamics.

## Defining Process Dynamics

Across the physical, biological and economic sciences, research on dynamics starts from some form of difference equation:

$$
\mathrm{X} _ {\mathrm{t} + \Delta \mathrm{t}} = \mathrm{X} _ {\mathrm{t}} + \Delta_ {\mathrm{t}} + \dots + \varepsilon \tag {1}
$$

where X is a variable (or vector) that represents the properties of some system and  <sub>t</sub> represents a change in that variable (or vector) from one time period to the next. The error term, ε, can be interpreted as variability in the process or as measurement error. When $\Delta \mathfrak { t } ~  ~ 0 .$ difference equations become differential equations, suitable for the analysis of vectors of continuous state variables (Forrester 1968). The logic of the difference equation focuses our attention on fundamental questions in dynamics: What changed? How much did it change? How fast is it changing?

While this approach to modeling dynamics is nearly universal, it has an important theoretical limitation: it embodies what Emirbayer (1997) would refer to as a substantialist ontology, which focuses on fixed objects with variable properties. Conceptualizing processes as fixed objects tends to hide the possibility that the structure of the process itself may be changing over time (Tsoukas and Chia 2002; Langley and Tsoukas 2016).

Rather than abandoning the logic of the difference equation, we can simply use a representation that allows us to describe emergent differences in process structure. For the reasons discussed above, a weighted, directed graph is a good choice. Equation (2) shows the basic difference that Equation (1) expressed in terms of directed graphs. It expresses the difference in process structure at two adjacent points in time:

$$
(2) \quad \mathrm{P} (\mathrm{V}, \mathrm{E}) _ {\mathrm{t} + \Delta \mathrm{t}} = \mathrm{P} (\mathrm{V}, \mathrm{E}) _ {\mathrm{t}} + \Delta (\mathrm{v}, \mathrm{e}) _ {\mathrm{t}} + \dots + \varepsilon
$$

where (v,e) refers to some set of vertices (v) and edges (e) that are added or removed from time t to time t+t. Equation (2) formalizes the idea that the future process equals the current process, plus or minus any changes and any variability or error. In the absence of change, (v,e) = 0.

The expression (v,e) provides a way to explicitly operationalize the first critical element of process dynamics: measuring process change. This framework suggests that theorizing about process dynamics can be formalized in terms of network dynamics. Network dynamics can be analyzed in terms of the formation and dissolution of edges in a graph (Snijders, 2001), which can then help us explain and predict how a process changes, as discussed further below.

## Process Variety versus Process Change

Describing processes as a directed graph allows us to distinguish between variety and change. Variety arises when a given process structure has multiple execution paths (McCabe 1975) or variants (Rosa, van Der Aalst, Dumas, and Milani 2017). Real processes often have numerous execution paths. For example, Pentland et al. (2010) found over 1,000 different pathways in an invoice approval workflow. This level of variety does not require or imply any change in process structure. Processes can have variety even if they are not changing because a single, static graph can produce thousands of different paths. In Markovian terms (Anderson and Goodman 1957), the process is stationary, so there is no change from t to t+t and $\mathrm { P } ( \mathrm { V } , \mathrm { E } ) _ { \mathrm { t } + \Delta \mathrm { t } } = \mathrm { P } ( \mathrm { V } , \mathrm { E } )$ <sub>t</sub>.

In contrast, change means that a process has a different structure, so that $\mathrm { P ( ~ V , E ~ ) } _ { \mathrm { t + } \Delta \mathrm { t } } \neq \mathrm { P ( ~ V , E ~ ) } _ { \mathrm { t } }$ <sub>t</sub> . Process change means adding or removing vertices and/or edges in the process graph or changing the weights on the edges. Some frameworks distinguish between first-order and secondorder change (Weakland et al. 1974). First-order change is limited to changing weights on the edges; second-order change implies adding/removing edges.

In the dermatology clinics we analyze here, there are stretches of time when the process is very nearly stationary and there are moments of abrupt change. There are also periods where the sequential structure of the process changes gradually. Each of these phenomena poses different theoretical challenges and requires different explanations.

## Aggregating Iterations to Determine Process Structure

Because real business processes typically have a lot of variety, one needs to observe and aggregate multiple iterations to map the structure of the process. Aggregation is a standard procedure for time slices in dynamic social networks (Moody et al. 2005; Rossetti and Cazabet 2018). For process networks, there are two levels of temporal granularity to consider in analyzing process structure. One level is inside the graph, from one event to the next. We can think of this as the minimum temporal granularity, $\mathbf { t } _ { \mathrm { m i n } } .$ The other level is between graphs, t. By analogy to a movie, t is like the duration of each frame in the movie. The finest unit of time that can be discriminated in the data, $\mathbf { t } _ { \mathrm { m i n } } ,$ sets a boundary on what kinds of processes can be observed. $\operatorname { I f } \tan$ is one day, then there is no way to track processes where events occur more often than daily. To capture the overall process, t needs to be large to include enough iterations to reveal the process structure, but small enough to reveal changes in the process.

For example, in the EMR audit trail data we analyze here, the minimum temporal granularity was one second. This was given by the system. We chose a window of one day to estimate the structure of the process in each clinic (roughly 40 visits per day per clinic). The choice of $( \Delta \mathfrak { t } =$ 1 day) reflects the natural rhythm of the work in the clinics: they operate for 8 hours and then cease operations for 16 hours. Each day is potentially different because the clinical staff can change from day to day, so it makes sense to use each day as a snapshot of a clinic. In the next section, we use this framework to describe and measure process change in the dermatology clinics at the University of Rochester Medical Center.

## Example: Process Dynamics in Dermatology Clinics

The audit trail we analyze here traces actions in the EMR record-keeping process for over 57,000 patient visits, from January 2016 through December 2017. Table 1 shows the first seven minutes of one patient visit, as captured in the EMR audit trail.

The diachronic approach we demonstrate here is a simple and effective one for visualizing and theorizing about dynamics (Barley 1990; Berente et al. 2019). Our approach is inspired by the method used by Tralie and Perea (2018) to analyze temporal recurrence in video data. They analyze thousands of sequentially ordered images (video frames), each of which contains thousands of related data points (pixels). This basic time-slice methodology has also been applied to dynamic social networks (Moody et al. 2005; Rosetti and Cazabet 2018). We adapt this approach to the analysis of digital trace data. The approach includes five main steps:

1. Retrieve digital trace data. With the help of the IT staff, we retrieved two full years of patient visits from four dermatology clinics. The resulting data set included over 7.5 million time-stamped records that provide a trace of actions for patient visits from January 1, 2016 to December 31, 2017. The digital trace of each patient visit contains an average of 133 time-stamped events (sd = 45.1).

2. Select a lexicon. Berente et al. (2019) note that researchers must choose a lexicon (set of codes) for their data. For the reasons explained above, we chose to retain all 300 event codes that occur in the trace data. This includes actions by the medical staff as well as system-generated events that would be invisible to an outside observer. Retaining all of the information provides a more sensitive indicator of change. The lexicon provides the set of vertices in the graph that describes the process.

3. Select a temporal unit of analysis, t. In order to apply Equation (2) to the data, we need to select a time-step for the analysis. Since clinical work has a natural daily rhythm, we chose one day in each clinic.<sup>6</sup> We aggregate observed the data within that window to create a directed graph that represents the process during that time window. We knew that the clinics were organized differently, so we also separated the data for each clinic. Thus, the unit of analysis is the clinic-day: one day at one clinic.

4. Compute a process graph for each unit of analysis. We represent each clinic-day as a directed graph, as described above. We used the algorithm developed by Pentland et al. (2017) to transform the sequence data for each clinic-day into a weighted, directed graph with a set of vertices $\mathrm { ( V _ { c l i n i c - d a y } ) }$ and a set of edges $( \mathrm { E _ { c l i n i c - d a y } } ) . ^ { 7 }$ We compute V and E as vectors that include the frequency of the vertices and edges for each clinic-day so that the analysis reflects differences in how often each event (and pair of events) occurs.

5. Visualizing. Once the sequence of graphs is constructed, they can be visualized, compared, and analyzed in many ways (Handcock et al. 2008; Moody et al. 2005). Here, we compare the graphs to visualize differences between clinics on each day (synchronic comparison) and differences within clinics over time (diachronic analysis).

<table><tr><td colspan="3">Table 1. First Seven Minutes of One Visit</td></tr><tr><td>Timestamp</td><td>Action</td><td>Actor</td></tr><tr><td>1/5/16 15:33:00</td><td>CHECKIN_TIME</td><td>Licensed_Nurse</td></tr><tr><td>1/5/16 15:39:09</td><td>MR_REPORTS</td><td>Licensed_Nurse</td></tr><tr><td>1/5/16 15:39:11</td><td>UCW_RELATED_ENCOUNTERS</td><td>Licensed_Nurse</td></tr><tr><td>1/5/16 15:39:12</td><td>MR_ENC_ENCOUNTER</td><td>Licensed_Nurse</td></tr><tr><td>1/5/16 15:39:12</td><td>MR_REPORTS</td><td>Licensed_Nurse</td></tr><tr><td>1/5/16 15:39:12</td><td>FLOWSHEET</td><td>Licensed_Nurse</td></tr><tr><td>1/5/16 15:39:12</td><td>AC_VISIT_NAVIGATOR</td><td>Licensed_Nurse</td></tr><tr><td>1/5/16 15:40:00</td><td>ARVL_LST_DL_TIME</td><td>Licensed_Nurse</td></tr><tr><td>1/5/16 15:40:09</td><td>MR_REPORTS</td><td>Licensed_Nurse</td></tr><tr><td>1/5/16 15:40:09</td><td>MR_MEDICATIONS</td><td>Licensed_Nurse</td></tr></table>

## Measuring and Explaining Process Change

To see how the process changed over time, we used two different ways of comparing these graphs: comparison to a common reference and self-comparison. We applied those comparisons to the vectors of vertices $\mathrm { ( V _ { c l i n i c - d a y } ) }$ and the vectors of edges $\mathrm { ( E _ { c l i n i c - d a y } ) }$ . In our data, $\mathrm { V _ { c l i n i c - d a y } }$ has 300 elements and $\mathrm { E _ { c l i n i c - d a y } }$ has 12,421 elements, many of which are zero because not all elements appear in every clinic, every day.<sup>8</sup> For each of these comparisons, we used the cosine similarity. When the days are similar, the cosine similarity is closer to one; when the days are different, the cosine similarity is closer to zero. This analysis illuminated the empirical puzzle mentioned above: the processes changed systematically at specific points in time. Figure 2 shows the results.

In all four panels of Figure 2, the horizontal axis represents time, from January 2016 through December 2017, measured in days, without gaps for weekends or holidays. The vertical axis in all four panels is cosine similarity. Figure 2 (a & c) is based on vertices; Figure 2 (b & d) is based on edges. The upper half of Figure 2 (a & b) shows the cosine similarity of each clinic-day compared to a fixed reference clinic-day.<sup>9</sup> For clarity, the data are smoothed with a rolling mean of five days. The lower half of Figure 2 (c & d) shows the cosine similarity of five days in each clinic compared to the previous five days in the same clinic. In other words, it compares two adjacent moving windows as they slide across the data for each clinic (Maaradji et al. 2017; Pentland et al. 2014).

There are some key points to notice about these process trajectories. First, the changes occur in all four clinics simultaneously. Second, the changes occur abruptly, on specific dates: June 7, 2016, September 1, 2016, April 15, 2017, and September 1, 2017. After each change, the process rapidly stabilizes again until the next change. At each of the four changes, groups of action codes appear or disappear suddenly from the digital traces. The codes were not removed from the system; they simply stopped (or started) showing up in the traces. Third, there are multiple periods of stability. For months at a time, there is negligible change in process structure. During these periods of stability, (v,e) \~ 0. Fourth, the structure of process bounces back after changes: it returns to a prior state after the third shock. Thus, at least some of the changes appear to be reversible. Finally, the changes appear to be periodic because they happen at the same time each year.

## Explaining the Mystery

As mentioned above, these changes were invisible to the physicians and other staff members at the clinics. From their point of view as users of the system, nothing changed. The EMR systems analysts were also unaware of any changes. These changes were invisible to the participants and they would have been invisible to researchers as well had we not performed the diachronic analysis just described. Engaging with clinical staff helped us rule out certain possible explanations for the changes, such as system upgrades in the EMR, personnel turnover, or changes in the patient mix. Eventually, we got to the bottom of it.

(d)  
(c)  
![](/api/attachments/GM22HNUS/fulltext/images/3ec7c8026d028eb056c47500c83de64a7d71d57d6a0623a3c98910724046cb59.jpg)  
(b)

![](/api/attachments/GM22HNUS/fulltext/images/96046a0de1566bbf7a5322e248142b4befbaad4640dfd47363309eeaff22d3c4.jpg)

![](/api/attachments/GM22HNUS/fulltext/images/e8da430abb111957addac56ebdc7d4cf758fa980db95d1d8ee06cf4b6e169bb2.jpg)

![](/api/attachments/GM22HNUS/fulltext/images/09e83fa59beca7290a012cc4e8b454f693c53ec1cdf95dea8d47c81107d20bf6.jpg)  
Figure 2. Changes in Process Structure over Two Years at Four Clinics

Engaging with clinical staff helped us rule out certain possible explanations for the changes, such as system upgrades in the EMR, personnel turnover, or changes in the patient mix. Eventually, we got to the bottom of it.

Privacy policy. The change on June 7 resulted from a change in policy concerning the accessibility of psychiatric data. On that date, the hospital added an additional layer of controls to prevent unauthorized access. In the typical course of work, dermatologists do not need to access psychiatric data. These controls would not be visible to users who do not use psychiatric data, so the dermatology staff members were not aware that they had been added. However, they were added to the EMR audit trail and we can see the effect of this change quite clearly in Figure 2. Notice that the process does not bounce back from this change; it appears to have been permanent.

Flu season. It turns out that September 1 of each year marks the start of flu season. Starting on that day of each year, every patient visiting the clinic would be asked about vaccination and their vaccination status would be entered in the system. Likewise, April 15 marks the end of flu season. From the perspective of the clinical staff, this apparently did not seem like a change because it happens every year. Yet flu season was clearly visible in the trace data and affected the process. Unlike the change in privacy policy, flu season is truly seasonal. On April 15, the process bounced back to its original form. During flu season, we conjecture that the required documentation and activities for patients that have (or have not) been vaccinated accounts for the variation in process. Outside of flu season, the process appears to be quite stable, not just from day to day but from year to year.

## Discussion: Theorizing about Process Dynamics

The trajectories shown in Figure 2 represent a significant advance in the state of the art of the measurement of process dynamics. Until recently, a multiyear analysis with fine-grained data $( \mathbf { t } _ { \operatorname* { m i n } } = 1$ second) was simply not possible. By using all of the information from the digital traces, we can begin to formulate better theory that can be used to analyze, explain, and predict process dynamics.

Gregor (2006) offers a taxonomy of theories based on the primary goal of the theory, from Level 1 (analysis) to Level 5 (design and action). Gregor’s levels provide a roadmap for theory development in process dynamics. The basic model of process as directed graph can be considered a Level 1 theory—a theory for analysis. Directed graphs allow us to analyze process dynamics in terms of the formation, reinforcement, and dissolution of edges in the network. The expression (v,e)<sub>t</sub> constitutes a formal way to describe and measure process change in terms of graph structure from one time period to the next. In research on social networks, an extensive body of theoretical and empirical work on network dynamics employs longitudinal analysis of time slices (Snijders 2001; Moody et al 2005; Rosetti and Cazabet 2018). In research on processual phenomena, we are just getting started. A time series of directed graphs provides evidence of how a process changes that can be used by researchers to develop theory.

New empirical evidence can provide the basis for new interpretations and analysis (Level 1), explanations (Level 2), and predictions (Level 3). Eventually, IS scholars may aspire to Gregor's (2006, p. 620) Level 4 theory, which has “both testable propositions and causal explanations.” At this point, we are just beginning to analyze and explain the observed dynamics (Levels 1 and 2). Yet we can envision theoretical contributions at all of Gregor’s (2006) levels including analysis, explanation, and prediction.

Diachronic analysis of process dynamics can also fruitfully be used to advance theory from many different theoretical perspectives at different levels of theoretical abstraction and granularity, as suggested in Figure 3. We distinguish among grand theories with a relatively high level of abstraction whose ambition is to develop a general understanding of the social world, mechanisms that provide explanation of how processes change, and motors of processes that illuminate why processes change the way they do. The theories mentioned at each level of abstraction in Figure 3 are not meant to be comprehensive of all possible perspectives on process dynamics. They simply reflect prominent examples.

## Grand Theories: How Does the World Work?

Grand theories seek to articulate basic assumptions and principles about the social world (Gregor 2006). For instance, structuration theory (Giddens 1984) has been influential in research on IS (Orlikowski and Robey 1991; Jones and Karsten 2008; Poole and Descantis 2004). Implicitly or explicitly, structuration entails changes in practice and routines and should thus be observable in process dynamics.

Our research design mirrors Barley’s (1986) classic study on technology and structuration. Barley documented action patterns in two radiology departments before and after the introduction of computerized tomography (CT) scanners. He used synchronic and diachronic comparisons to argue that action patterns around the new technology were not determined by the technology. New technology provided an “occasion for structuring,” but the emergent patterns of action were constructed over time by the participants.

Our comparison of the four dermatology clinics would tend to support Barley’s (1986) findings: different clinics can use the same technology in different ways. All four clinics use the same system, but our analysis shows that one of the clinics—Batavia (see Figure 2)—is different from the others. We know that this clinic uses different procedures and is less complex than the others (Ryan et al. 2019). If we restricted our analysis to this kind of synchronic (or cross-sectional) comparison, it would tend to support a constructivist interpretation.

However, our diachronic analysis of the EMR recordkeeping process shows evidence of determinism. The patterns of action reveal much consistency from day to day, punctuated by sudden changes at all four clinics on specific dates. During the initial period and after the first policy change, the action patterns in the four clinics are very similar and they shift in unison. Then comes flu season, which disrupts the normal patterns. At the end of flu season, the action patterns return to normal. It is impossible to say how the observed patterns were originally formed after the technology was introduced several years ago.

![](/api/attachments/GM22HNUS/fulltext/images/cfea78cf4a3b8bcdf18d35837643453f052b7c2fe96204c7c3b783a2aa243933.jpg)  
Figure 3. Theorizing Process Dynamics

Nevertheless, as of January 2016, the similarity among clinics and the elastic response to the flu season (bouncing back to normal) support the idea that the system shared among clinics shaped the action patterns to a significant extent across all four clinics. In terms of these dynamics, which are only visible with diachronic analysis, Batavia was not different.

Determinism and constructivism have long been debated in studies of technology in general (Leonardi and Barley 2008) and in IS studies in particular (e.g., DeSanctis and Poole 1994). The theoretical question centers upon whether technology shapes social organization (determinism) or whether technology is socially constructed (constructivism). Our approach can contribute to this theoretical debate by helping researchers evaluate whether patterns of technologically enabled action are stable and/or changing.

## Mechanisms: How Do Processes Change?

Mechanisms provide midrange theoretical explanations of how processes change and of the ways in which changes happen in processes. For example, in the literature on organizational routines, current theory suggests that endogenous change occurs through performing and patterning (Feldman 2016; Danner-Schröder and Geiger 2016; Turner and Rindova 2018; Goh and Pentland 2019). In terms of the model presented here, performing and patterning can be interpreted as mechanisms that shape the structure of a directed graph over time as successive process iterations reinforce existing paths or create new ones.

In the EMR audit trails, we particularly find evidence for the mechanism of imbrication (Leonardi, 2011). Building on the work of Taylor (2001), Ciborra (2006), and Sassen (2006), Leonardi (2011) argues that human and material agency are interwoven in a process he refers to as imbrication. The metaphor of tiles on a roof presents a static image of overlapping human and material agency but Leonardi (2011) clearly conceptualizes imbrication as processual.

The imbrication of human and material agency can be seen vividly in the first major process change, on June 7, 2016, when new controls were added to the EMR system to prevent access to psychiatric data. The decision to strengthen the access controls exemplifies human agency; translating that decision into automated controls exemplifies material agency. The newly configured system shaped the audit trail of every subsequent patient visit in every clinic.

## Motors: Why Do Processes Change?

Diachronic analysis provides a basis for investigating the motors of process dynamics. Based on extensive literature review of change processes, Van de Ven and Poole (1995) identify four basic “motors”: life cycle, teleology, dialectics, and evolution. These four motors can operate alone or in combination to drive process dynamics.

The most obvious driver of process dynamics in the EMR data is a life cycle. A life cycle implies that changes occur in a regular progression or cyclical pattern (e.g., weekly, monthly, annually, etc.) Our EMR data provide clear evidence of an annual life cycle, as the process changes (and then changes back) over the course of a year because of flu season. While the reason may seem rather prosaic, it provides a perfect illustration of what Gregor (2006) would call a Level 4 theory. It explains and predicts the observed process change.

Each of the theoretical perspectives mentioned in Figure 3 brings its own set of assumptions, constructs, and data requirements, but network dynamics provides a solid Level 1 basis for analysis: forming/dissolving edges in a directed graph. Obviously, some theories may require additional data beyond what are typically included in a digital trace. As Berente et al. (2019) have argued, the analysis of trace data may require complementary resources, such as interviews or observations. The diachronic analysis described here provides a rigorous foundation for inquiry because it provides a clear picture of the timing and magnitude of change in the EMR process. However, the data did not speak for themselves. We needed information from the medical staff and the IT staff to rule out alternative explanations and identify flu season as a driver of process dynamics in dermatology clinics.

## Bridging the Two Islands: Process Dynamics

Our fundamental proposition is that the process mining methods—broadly defined as the analysis and interpretation of digital trace data—can help address the theoretical concerns of the organizational process community. Likewise, organizational process theory— broadly characterized by its recognition that processes are emergent—can enrich research in the process mining community. In making this proposition, it is important not to conflate the general idea of process mining with particular models such as Petri nets, declarative models or directed graphs. The particular model of process dynamics we propose here represents just one possibility.

Table 2 shows how the approach we demonstrate here provides a bridge between business process management (BPM) and organizational process scholarship. The analysis of detailed event logs comes from the island of BPM (Dumas et al. 2018; van der Aalst 2013), but the diachronic analysis comes from the island of organizational process (Langley and Tsoukas 2016). Generally speaking, BPM researchers have not theorized about process change, while most organizational process researchers have not analyzed digital trace data. However, to measure and explain process change, we need to bring the methods and theoretical perspectives of both communities together.

All of these perspectives have strengths and weaknesses in terms of data and representation. Each one reflects a partial view that may be more or less suited for a particular purpose. For this reason, it is best to think of them as complementary (Berente et al. 2019). As Box (1976) famously noted, all models are wrong, but some models are useful. The challenge is to always pick the model that is best suited to the research question or practical problem at hand.

## Process Dynamics: Signal or Noise?

This research note raises an important question for the study of processual phenomena: do we attribute the changes from one time period to the next to signal or noise? By signal, we mean process changes of theoretical or practical significance ((v,e)). By noise, we mean the normal daily variations that make it difficult to detect the signal () The process mining literature provides a variety of methodologies for analyzing process variation (Rosa et al. 2017), detecting drift (Bose et al. 2011), and filtering noise (Tax et al. 2019). But the interpretation of process variation is not a methodological issue, it is a theoretical issue. Electronic medical records are a notoriously noisy source of digital trace data (Kunzman 2018; Lee et al. 2017). However, what we perceive as signal or noise depends on our theoretical perspective.

<table><tr><td colspan="4">Table 2. Bridging the Two Islands</td></tr><tr><td></td><td>Organizational process</td><td>Process dynamics(this paper)</td><td>Business process management</td></tr><tr><td>Emphasis</td><td>Theory developmentExplaining how processes unfold and change over time</td><td>Synchronic and diachronic analysisTheory development</td><td>Diagnose process problems and design solutions using detailed models of particular processesMethod development (e.g., model quality, computational efficiency)</td></tr><tr><td>Method</td><td>Participant observation</td><td>Process mining to generate network time slices</td><td>Process mining to discover stationary process model</td></tr><tr><td>Data</td><td>Fieldnotes</td><td>Digital trace data</td><td>Digital trace data</td></tr><tr><td>Process representation</td><td>Textual description and diagrams</td><td>Weighted, directed graphs</td><td>Petri nets</td></tr><tr><td>Assumptions about process and change</td><td>Processes are emergentConstant tension between stability and changeBoth stability and change need to be explained</td><td>Processes are emergentConstant tension between stability and changeBoth stability and change need to be explained</td><td>Processes are designedProcesses are generally stableChange needs to be managed/controlled</td></tr><tr><td>Strengths</td><td>Deep understanding, particularly when human actors are involved</td><td>Flexibility in sources of data, time scales, types of processesSynchronic/diachronic comparisonRelevant to many theoretical perspectives</td><td>Detailed models of control flow and concurrency in particular processes</td></tr></table>

From our original viewpoint, the changes in Figure 2 look like noise. They are idiosyncratic, unexpected variations that undermine the possibility of getting a model that fits the data for the whole two years. From the viewpoint of processual dynamics, however, these changes are the main signal. We need a diachronic analysis to see them and measure them. The changes represent phenomena that need to be explained.

This is a researcher’s choice—a theoretical choice—to adopt a synchronic or diachronic perspective on the data (Barley 1990). Berente et al. (2019) discuss synchronic and diachronic as complementary perspectives. We agree, but our experience with the analysis of our EMR data suggests that adopting one perspective can blind you to the other. In a synchronic analysis, we would compare P(V, E)<sub>ClinicA</sub> and P(V, E)<sub>ClinicB</sub>. This is an interesting line of inquiry, of course, but as we discussed above, it might lead to a different theoretical interpretation because it does not reveal dynamics. Unless we explicitly choose to investigate dynamics, we might never see it. It comes back to the question of what we consider signal and what we consider noise. If we are looking for time-invariant models, as in most BPM research, then processual change represents noise. If we are looking for processual dynamics, as in most organizational process research, then the opposite is true.

## Conclusion

The research agenda that we are pointing to here is very broad, but it can be stated succinctly: explaining stability and change in processual phenomena. By adopting a network-based process representation and a process mining methodology that allows us to generate directed graphs from trace data, the framework we have demonstrated here opens up opportunities for research that cannot be addressed in any other way.

IS scholarship has long sought to understand how change emerges and unfolds over time (Orlikowski and Yates 2002; Vaast and Levina 2015; Volkoff and Strong 2013). Research on process dynamics presents an opportunity to continue and energize this tradition. On the methodology side, techniques for process mining, discovery, and modeling have advanced dramatically (Dumas et al. 2018; Van der Aalst 2013). Digital trace data represent still largely untapped sources to apply these promising techniques. On the theory side, contemporary organization theorists (Hernes 2014; Tsoukas and Chia 2002) have set forth a radical new perspective with process at the foundation (Langley 1999; Langley and Tsoukas 2016). Now is the time to bridge these islands through research on process dynamics.

## Acknowledgments

This material is based on work supported by the National Science Foundation under Grant No. SES-1734237. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation. This research was also supported in part by University of Rochester CTSA (UL1 TR002001) from the National Center for Advancing Translational Sciences (NCATS) of the National Institutes of Health (NIH). The content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health. We thank our co-investigators Alice P. Pentland and Kenneth Frank for making this work possible and we are grateful for comments from Jan Recker and Marlon Dumas on various aspects of the argument. We also thank the senior editor, Brian Butler, the associate editor, and the two reviewers for their insightful comments during the review process. Any errors or omissions are our own.

## References

Alvesson, M., and D. Kärreman 2007. “Constructing Mystery: Empirical Matters in Theory Development,” Academy of Management Review (32:4), pp. 1265-1281.

Anderson, T. W., and Goodman, L. A. 1957. Statistical Inference about Markov Chains, The Annals of Mathematical Statistics (28:1), pp. 89-110.

Ashby, W. R. 1956. An Introduction to Cybernetics, London: Chapman & Hall.

Barley, S. R. 1986. “Technology as an Occasion for Structuring: Evidence from Observations of CT Scanners and the Social Order of Radiology Departments,” Administrative Science Quarterly (31:1), pp. 78-108.

Barley, S. R. 1990. “Images of Imaging: Notes on Doing Longitudinal Field Work,” Organization Science (1:3), pp. 220-247.

Becker, M., and Laue, R. 2012. “A Comparative Survey of Business Process Similarity Measures,” Computers in Industry (63:2), pp. 148-167.

Benitez, J., Ray, G., and Henseler, J. 2018. “Impact of Information Technology Infrastructure Flexibility on Mergers And Acquisitions,” MIS Quarterly (42:1), pp. 25- 43.

Berente, N., Seidel, S., and Safadi, H. 2019. “Research Commentary: Data-Driven Computationally Intensive Theory Development,” Information Systems Research (30:1), 50-64.

Bose, R. J. C., van der Aalst, W. M., Žliobaitė, I., and Pechenizkiy, M. 2011. “Handling Concept Drift in Process Mining,” in Proceedings of the International Conference on Advanced Information Systems Engineering, Berlin: Springer, pp. 391-405.

Box, G. E. 1976. “Science and Statistics,” Journal of the American Statistical Association (71:356), pp. 791-799.

Breuker, D., and Matzner M. 2014. “Performances of Business Processes and Organizational Routines: Similar Research Problems, Different Research Methods—A Literature Review,” in Proceedings of the European Conference on Information Systems, Tel Aviv, Israel.

Chinosi, M., and Trombetta, A. 2012. “BPMN: An Introduction to the Standard,” Computer Standards & Interfaces (34:1), pp. 124-134.

Cho, M., Song, M., Comuzzi, M., and Yoo, S. 2017. “Evaluating the Effect of Best Practices for Business Process Redesign: An Evidence-Based Approach Based on Process Mining Techniques,” Decision Support Systems (104), pp. 92-103.

Ciborra, C. 2006. “Imbrication of Representations: Risk and Digital Technologies,” Journal of Management Studies (43:6), pp. 1339-1356.

Danner-Schröder, A., and Geiger, D. 2016. “Unravelling the Motor of Patterning Work: Toward an Understanding of the Microlevel Dynamics of Standardization and Flexibility,” Organization Science (27:3), pp. 633-658.

De Saussure, F. 1916/2011. Course in General Linguistics. New York: Columbia University Press.

DeSanctis, G., and Poole, M. S. 1994. “Capturing the Complexity in Advanced Technology Use: Adaptive Structuration Theory,” Organization Science (5:2), pp. 121- 147.

Dewey, J. 1938/2008. The Later Works, 1925-1953, vol. 12: Logic: The Theory of Inquiry, J. A. Boyston (ed.), Carbondale: Southern Illinois Press, vol. 12.

Dumas, M., García-Bañuelos, L., and Dijkman, R. M. 2009. “Similarity Search of Business Process Models,” IEEE Data Engineering Bulletin (32:3), pp. 23-28.

Dumas, M., La Rosa, M., Mendling, J., & Reijers, H. A. 2018. Fundamentals of Business Process Management. Berlin,: Springer.

Emirbayer, M. 1997. “Manifesto for a Relational Sociology,” American Journal of Sociology (103:2), pp. 281-317.

Ezpeleta, J., Colom, J. M., and Martinez, J. 1995. “A Petri Net Based Deadlock Prevention Policy for Flexible Manufacturing Systems.” IEEE Transactions on Robotics and Automation (11:2), pp. 173-184.

Farjoun, M. 2016. “Contradictions, Dialectics and Paradoxes,” in The SAGE Handbook of Process

Organization Studies, A. Langley and H. Tsoukas (eds.), Thousand Oaks, CA: SAGE, pp. 87-109.

Feldman, M. S. 2016. “Routines as Process: Past, Present, and Future,” in Organizational Routines: A Process Perspective, J. Howard-Grenville, C. Rerup, A. Langley, and H. Tsoukas (eds.), Oxford: Oxford University Press, pp. 23–46.

Feldman, M. S., and Pentland, B. T. 2003. “Reconceptualizing Organizational Routines as a Source of Flexibility and Change,” Administrative Science Quarterly (48:1), pp. 94– 118.

Feldman, M. S., Pentland, B. T., D’Adderio, L., and Lazaric, N. 2016. “Beyond Routines as Things: Introduction to the Special Issue on Routine Dynamics,” Organization Science (27:3), pp. 505-513.

Feldman, M. S., and Orlikowski, W. J. 2011. “Theorizing Practice and Practicing Theory,” Organization Science (22:5), pp. 1240-1253.

Forrester, J. W. 1968. “Industrial Dynamics: After the First Decade,” Management Science (14:7), pp. 398-415.

Fowler, M., and Kobryn, C. 2004. UML Distilled: A Brief Guide to the Standard Object Modeling Language. Boston: Addison-Wesley Professional.

Giddens, A. 1984. The Constitution of Society : Outline of the Theory of Structuration. Cambridge: Polity Press.

Gioia, D. A., Corley, K. G., and Hamilton, A. L. 2013. “Seeking Qualitative Rigor in Inductive Research: Notes on the Gioia Methodology,” Organizational Research Methods (16:1), pp. 15-31.

Goh, K. T., and Pentland, B. T. 2019. “From Actions to Paths to Patterning: Toward a Dynamic Theory of Patterning in Routines,” Academy of Management Journal (62:6), pp. 1901-1929.

Gregor, S. 2006. “The Nature of Theory in Information Systems,” MIS Quarterly, (30:3), pp. 611-642.

Greve, H. R. 2003. Organizational Learning from Performance Feedback: A Behavioral Perspective on Innovation and Change. Cambridge: Cambridge University Press.

Grisold, T., Wurm, B., Mendling, J., and vom Brocke, J. 2020. “Using Process Mining to Support Theorizing About Change in Organizations,” in Proceedings of the 53rd Hawaii International Conference on System Sciences, Wailea, HI.

Grover, V., Jeong, S. R., Kettinger, W. J., and Teng, J. T. 1995. “The Implementation of Business Process Reengineering,” Journal of Management Information Systems (12:1), pp. 109-144.

Hammer, M. 1990. “Reengineering Work: Don’t Automate, Obliterate,” Harvard Business Review (68:4), pp. 104-112.

Handcock, M. S., Hunter, D. R., Butts, C. T., Goodreau, S. M., and Morris, M. 2008. “Statnet: Software Tools for the Representation, Visualization, Analysis and Simulation of Network Data,” Journal of Statistical Software (24:1), pp. 1548-1560.

Hernes, T. 2014. A Process Theory of Organization, Oxford: Oxford University Press.

Hodgson, G. M. 2016. “Evolutionary Theory,” in The SAGE Handbook of Process Organization Studies, A. Langley and

H. Tsoukas (eds.), Thousand Oaks, CA: SAGE, pp. 204- 219.

Hoos, I. R. 1960. “The Sociological Impact of Automation in the Office,” Management Science, (2), pp. 10-19.

James, W. 1909/1996. A Pluralistic Universe: Hibbert Lectures at Manchester College on the Present Situation in Philosophy. Lincoln: University of Nebraska Press.

Jones, M. R., and Karsten, H. 2008. “Giddens’s Structuration Theory and Information Systems Research,” MIS Quarterly (32:1), pp. 127-157.

Keenoy, C. L. 1958. “The Impact of Automation on the Field of Accounting,” Accounting Review (33:2), pp. 230-236.

Langley, A. 1999. “Strategies for Theorizing Process Data,” Academy of Management Review (24:4), pp. 691-710.

Langley, A., and Tsoukas, H. 2016a. “Introduction: Process Thinking, Process Theorizing and Process Researching,” in The SAGE Handbook of Process Organization Studies, A. Langley and H. Tsoukas (eds.). Thousand Oaks, CA: SAGE, ch. 1.

Langley, A., and Tsoukas, H. 2016b. The Sage Handbook of Process Organization Studies. Thousand Oaks, CA: SAGE.

Leonardi, P. M., and Barley, S. R. 2008. “Materiality and Change: Challenges to Building Better Theory about Technology and Organizing,” Information and Organization (18:3), pp. 159-176.

Leonardi, P. M., and Vaast, E. 2017. “Social Media and Their Affordances for Organizing: A Review and Agenda for Research,” Academy of Management Annals (11:1), pp. 150-188.

Leonardi, P. M. 2011. “When Flexible Routines Meet Flexible Technologies: Affordance, Constraint, and the Imbrication of Human and Material Agencies,” MIS Quarterly (35:1), pp. 147-167.

Locke, K., K. Golden-Biddle, and M. S. Feldman. 2008. “Perspective—Making Doubt Generative: Rethinking the Role of Doubt in the Research Process,” Organization Science (19:6), pp. 907–918.

Lomborg, S., and Bechmann, A. 2014. “Using APIs for Data Collection on Social Media,” The Information Society (30:4), pp. 256-265.

Maaradji, A., Dumas, M., La Rosa, M., and Ostovar, A. 2016. “Fast and Accurate Business Process Drift Detection,” in International Conference on Business Process Management, Berlin: Springer, pp. 406-422.

Maggi, F. M., Bose, R. J. C., and van der Aalst, W. M. 2012. “Efficient Discovery of Understandable Declarative Process Models from Event Logs,” in International Conference on Advanced Information Systems Engineering, Berlin: Springer, pp. 270-285.

McCabe, T. J. 1976. “A Complexity Measure,” IEEE Transactions on Software Engineering (SE2:4), pp. 308- 320.

Mead, G. H. 1934/1962. Mind, Self and Society. Chicago: University of Chicago Press.

Moody, J., McFarland, D., and Bender-deMoll, S. 2005. “Dynamic Network Visualization,” American Journal of Sociology (110:4), pp. 1206-1241.

Murata, T. 1989. “Petri Nets: Properties, Analysis and Applications,” in Proceedings of the IEEE (77:4), pp. 541- 580.

Orlikowski, W. J., and Yates, J. A. 2002. “It’s about Time: Temporal Structuring in Organizations,” Organization Science (13:6), pp. 684-700.

Orlikowski, W. J., and Robey, D. 1991. “Information Technology and the Structuring of Organizations,” Information Systems Research (2:2), pp. 143-169.

Pentland, B. T., and Feldman, M. S. 2007. “Narrative Networks: Patterns of Technology and Organization,” Organization Science (18:5), pp. 781-795.

Pentland, B. T., Feldman, M. S., Becker, M. C., and Liu, P. 2012. “Dynamics of Organizational Routines: A Generative Model,” Journal of Management Studies (49:8), pp. 1484- 1508.

Pentland, B. T., Hærem, T., and Hillison, D. 2011. “The (N) Ever-Changing World: Stability and Change in Organizational Routines,” Organization Science (22:6), pp. 1369-1383.

Pentland, B. T., Recker, J., and Wyner, G. 2017. “Rediscovering Handoffs,” Academy of Management Discoveries (3:3), pp. 284-301.

Pentland, B. T., Hærem, T., and Hillison, D. 2010 “Comparing Organizational Routines as Recurrent Patterns of Action,” Organization Studies (31:7), pp. 917-940.

Pentland, B., Hærem, T., and Khaledi, H. 2014. “Using Action Networks to Detect Change in Repetitive Patterns of Action,” in Proceedings of the International Conference on Information Systems, Auckland, New Zealand.

Pentland, B., Liu, P., Kremser, W., and Haerem, T. 2020. “The Dynamics of Drift in Digitized Processes,” MIS Quarterly (44:1), pp. 19-47.

Poole, M. S., and DeSanctis, G. 2004. “Structuration Theory in Information Systems Research: Methods and Controversies,” in The Handbook of Information Systems Research, M. E. Whitman and A. B. Woszczynski (eds.), IGI Global, pp. 206-249.

Reijers, H. A., and Mansar, S. L. 2005. “Best Practices in Business Process Redesign: An Overview and Qualitative Evaluation of Successful Redesign Heuristics,” Omega (33:4), pp. 283-306.

Reisig, W., and G. Rozenberg (eds.). 1998. Lectures on Petri Nets I: Basic Models, Berlin: Springer.

Rescher, N. 1996. Process Metaphysics: An Introduction to Process Philosophy. Albany, NY: SUNY Press.

Rosa, M. L., van Der Aalst, W. M., Dumas, M., and Milani, F. P. 2017. “Business Process Variability Modeling: A Survey,” ACM Computing Surveys (50:1), pp.1-45.

Rossetti, G., R. Cazabet. 2018. “Community Discovery in Dynamic Networks: A Survey,” ACM Computing Surveys (51:2), pp. 1-37.

Ryan, J. L., Xie, Y., Kim, I., Frank, K., Pentland, A. P., and Pentland, B. T. 2019. “Team Documentation Influences Clinic Complexity and Patient Satisfaction,” Journal of Investigative Dermatology (139:5), S106.

Sassen, S. 2006. Territory, Authority, Rights: From Medieval to Global Assemblages, Princeton, NJ: Princeton University Press.

Schatzki, T. R. 2002. The Site of the Social: A Philosophical Account of the Constitution of Social Life and Change. University Park, PA: Penn State University Press.

Shotter, J. 2006. “Understanding Process from Within: An Argument For ‘Withness’ Thinking,” Organization Studies (27:4), pp. 585-604.

Snijders, T. A. B. 2001. “The statistical Evaluation of Social Network Dynamics,” Sociological Methodology (31:1), pp. 361-395.

Taylor, J. R. 2001. “Toward a Theory of Imbrication and Organizational Communication,” The American Journal of Semiotics (17:2), pp. 269-298.

Tax, N., Sidorova, N. and van der Aalst, W. M., 2019. “Discovering more Precise Process Models from Event Logs by Filtering out Chaotic Activities,” Journal of Intelligent Information Systems (52:1), pp. 107-139.

Tiwana, A., Konsynski, B., and Bush, A. A. 2010. “Research Commentary—Platform Evolution: Coevolution of Platform Architecture, Governance, and Environmental Dynamics,” Information Systems Research (21:4), pp. 675- 687.

Tralie, C. J., and Perea, J. A. 2018. “(Quasi) Periodicity Quantification in Video Data, Using Topology,” SIAM Journal on Imaging Sciences (11:2), pp. 1049-1077.

Tsoukas, H., and Chia, R. 2002. “On Organizational Becoming: Rethinking Organizational Change,” Organization Science (13:5), pp. 567-582.

Turner, S. F., and Rindova, V. P. 2018. “Watching the Clock: Action Timing, Patterning, and Routine Performance,” Academy of Management Journal (61:4), pp. 1253-1280.

Vaast, E., and Levina, N. 2015. “Speaking as One, but Not Speaking Up: Dealing with New Moral Taint in an Occupational Online Community,” Information and Organization (25:2), pp. 73-98.

Vaast, E., Safadi, H., Lapointe, L., and Negoita, B. 2017. “Social Media Affordances for Connective Action: An Examination of Microblogging Use During the Gulf of Mexico Oil Spill,” MIS Quarterly (41:4), pp. 1179-1205.

Van de Ven, A. H., and Poole, M. 1995. “Explaining Development and Change in Organizations,” Academy of Management Review (20:3), pp. 510-540.

van der Aalst, W. 2011. Process Mining: Discovery, Conformance and Enhancement of Business Processes. Heidelberg: Springer.

van der Aalst, W., Adriansyah, A., De Medeiros, A. K., Arcieri, F., Baier, T., Blickle, T., Bose, J. C., et al. 2011, “Process

Mining Manifesto,” in International Conference on Business Process Management, Berlin: Springer, pp. 169- 194.

van der Aalst, W. . 2013. “Business Process Management: A Comprehensive Survey,” ISRN Software Engineering, Article 507984.

van der Aalst, W. 2012. “Process Mining,” Communications of the ACM (55:8), pp. 76-83.

van der Aalst, W. 2019. “A Practitioner’s Guide to Process Mining: Limitations of the Directly-Follows Graph,” Procedia Computer Science (164), pp. 321–328.

Van Dongen, B., Dijkman, R., and Mendling, J. 2013. “Measuring Similarity between Business Process Models,” in Seminal Contributions to Information Systems Engineering, J. Bubenko, J. Krogstie, Ó. Pastor, B. Pernici, C. Rolland, A. Sølvberg (eds.), Berlin: Springer, pp. 405- 419.

Volkoff, O., and Strong, D. M. 2013. “Critical Realism and Affordances: Theorizing IT-Associated Organizational Change Processes,” MIS Quarterly (37:3), pp. 819-834.

Weakland, J. H., Fisch, R., Watzlawick, P., and Bodin, A. M. 1974. “Brief Therapy: Focused Problem Resolution,” Family Process (13:2), pp. 141-168.

West, D. B. 1996. Introduction to Graph Theory. Upper Saddle River, NJ: Prentice Hall.

Whitehead, A. N. 1929/1978. Process and Reality: An Essay in Cosmology. New York: Free Press.

Yates, J. 1993. “Co-evolution of Information-Processing Technology and Use: Interaction between the Life Insurance and Tabulating Industries,” Business History Review (67:1), pp. 1-51.

Yeshchenko, A., Di Ciccio, C., Mendling, J. and Polyvyanyy, A., 2021. “Visual Drift Detection for Sequence Data Analysis of Business Processes,” IEEE Transactions on Visualization and Computer Graphics (https://ieeexplore. ieee.org/document/9316994, early access).

## About the Authors

Brian T. Pentland is the Main Street Capital Partners Endowed Professor in the Broad College of Business at Michigan State University. His creative work has appeared in Academy of Management Journal, Academy of Management Review, Administrative Science Quarterly, Bandcamp, Journal of Management Studies, Management Science, MIS Quarterly, Organization Science, Organization Studies, Soundcloud, YouTube, and elsewhere. He received his Ph.D. in management from the Massachusetts Institute of Technology in 1991.

Emmanuelle Vaast is a professor of information systems at the Desautels Faculty of Management of McGill University. She studies how social and societal changes unfold with the development and use of digital technologies. Her research has been published in MIS Quarterly, Information Systems Research, Organization Science, and Organization Studies, among other outlets. Emmanuelle is a past division chair of the Organizational Communication and Information Systems (OCIS) division of the Academy of Management. She has served as a senior editor for Information Systems Research.

Julie Ryan Wolf is an associate professor of dermatology and radiation oncology, as well as a member of the University of Rochester NCI Community Oncology Research Program (NCORP) Research Base. She received her B.A. from University of Chicago, her Ph.D. in Pathology from UNC-Chapel Hill, and her M.P.H. from University of Rochester. She strives to improve healthcare by facilitating access to evidencebased, patient-centered care and to optimize metrics for assessing quality of care. Her research has been supported by the National Science Foundation (NSF), National Cancer Institute (NCI), Pfizer, Wilmot Cancer Institute, Hope Foundation, Biomedical Advanced Research and Development Authority (BARDA), National Institutes of Allergy and Infectious Disease (NIAID), Dermatology Foundation, and University of Rochester CTSA.
