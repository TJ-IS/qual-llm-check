---
otero_id: 10700
otero_key: "7MZKDGFN"
title: "Generating insights through data preparation, visualization, and analysis: Framework for combining clustering and data visualization techniques for low-cardinality sequential data"
authors: "Svetlozar Nestorov; Boris Jukić; Nenad Jukić; Abhishek Sharma; Sippo Rossi"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113119"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Generating insights through data preparation, visualization, and analysis: Framework for combining clustering and data visualization techniques for low-cardinality sequential data

![](/api/attachments/7MZKDGFN/fulltext/images/cbef7e952cc667f80042f58e57a6021da8c5562512b9aba14ac6c0235f135601.jpg)

Svetlozar Nestorov<sup>a</sup>, Boris Jukić<sup>b</sup>, Nenad Jukić<sup>a,⁎</sup>, Abhishek Sharma<sup>a</sup>, Sippo Rossi<sup>c</sup>

<sup>a</sup> Quinlan School of Business, Loyola University Chicago, Chicago, IL, USA

<sup>b</sup> Reh School of Business, Clarkson University, Potsdam, NY, USA

<sup>c</sup> School of Business, Aalto University, Helsinki, Finland

## A R T I C L E I N F O

Keywords: Data visualization Sequential data Low-cardinality data Data preparation Clustering Motifs

## A B S T R A C T

In this paper, we introduce a novel approach for identifying and testing relationships and patterns on the types of sequential data that are broadly present in a number of diferent real-world scenarios and environments. The proposed two-phase framework combines data preparation, data visualization and clustering techniques in an innovative way. The first phase of the framework explores the large amount of sequential data in stages that can be undertaken iteratively. Those stages include data preparation, counting and value-based ordering, distribution visualization, and subsequence length determination, confirmation and re-visualization. The second phase of the framework explores sequence diferences, based on motifs, between data cohorts that are created using descriptive attributes, and visualizes the changes over time and diferent attribute values. To illustrate the analytical power of the proposed framework, we present a comprehensive example that applies the framework on a large formally-maintained research data set collected and managed by the US Census Bureau. The framework, and the presented example, utilize visualization as an analytics tool and not just a presentation accessory.

## 1. Introduction

With the proliferation of types and variety of data, there is a need for more types of analyses and presentations that bring out the relationships between diferent elements and summarize complex data with simple and easily understood visuals [1,2]. The analysis of the visualized data is often performed without a formal model or hypoth esis testing task. Analysts can quickly and easily identify patterns, trends and outliers from graphs and charts without describing them formally. Once the interesting patterns are identified, they can be confirmed formally and analyzed further using computational and statistical methods.

Data visualization is broadly defined as the visual representation of quantitative data for the purpose of communication and analysis [3]. Data visualization is becoming an integral part of data analysis for many organizations that collect vast amounts of enterprise data [4,5]. The approach to analyzing data sets to summarize their main characteristics (typically by using visual methods) and seeing what the data can tell us beyond the formal modeling or hypothesis testing task is often referred to as Exploratory Data Analysis (EDA) and has been promoted since the 1970's [6]. The renewed focus is driven by the explosion of Big Data and the widespread adoption of business intelligence tools [7]. As stated in [8], an increasingly important and necessary factor of data analysis is how users consume data visually and how visualization-reliant technologies align with human abilities to support business judgment and decision making.

One of the earliest and oft-cited examples of how data visualization can bring deeper insight than basic statistics is the Anscombe's quartet [3]. The quartet consists of four datasets. basically indistinguishable using statistical methods such as means, regression coeficient, and residual sum of squares. However, when the four datasets are visualized as graphs, they look very diferent and can be distinguished easily by a human, which ultimately results in very diferent interpretations and conclusions. Even with only few dimensions and data points in the Anscombe's quartet, it is dificult to find meaningful patterns and trends by just looking at the numbers and derived statistics. For larger and more complex dataset, spotting trends or outliers becomes impossible based purely on numerical data, which further supports the use of data visualization as one of the tools for analysis.

Even though businesses and research organizations recognize the value of using data visualization as part of their data analysis, in practice, data visualization is routinely applied incorrectly or used merely in presenting results rather than exploration [9,10]. Furthermore, the focus is often on using flashy chart types that do not enable pattern and trend identification [11]. As stated in [12] “the common misperception in the business domain is that visual analytics is simply providing ‘pretty’ visual representations of some underlying data”.

In this paper, we present a framework for using data visualization as part of the EDA process to identify and test relationships and patterns on the specific type of sequential data (low-cardinality sequential data), broadly present in a number of diferent real-world scenarios and environments. One of the main goals of our research is to show that data visualization can be used successfully to generate insights that can be confirmed analytically, a practice that is underutilized and even frowned upon in many areas of natural and social science and engineering [10,11].

In addition to presenting a formal visualization framework we will also empirically validate the framework using a comprehensive example. This example uses a large research data set collected and maintained by the US Census Bureau.

The rest of this paper is organized as follows. In Section 2 we will describe the characteristics of data that our framework is applicable for. In Section 3 we will give a detailed description of our framework. In Section 4 we will present a comprehensive example of the use of our framework on a formal large data set. Finally, in Section 5 we will present concluding remarks.

## 2. Applicable data

As we mentioned, the visualization framework proposed in this paper is applicable to data with certain characteristics. In particular, our framework is applicable on sequential data with low cardinality attributes. In this section we briefly describe the properties of sequential data with low cardinality attributes.

## 2.1. Sequential data

The defining characteristics of sequential data is a sequential order between items in a dataset [13,14]. In other words, sequential data consists of lists of ordered states, where the states can be numeric measurements or categorical descriptions. The order of states is often based on the time when it was observed. Sensor data is an example of sequential data where state is based on a numeric observation, since each measurement is associated with a numeric timestamp. Sensor data is used for variety of diferent types of analyses, such as distinguishing normal from faulty engines [15]. As an example of categorical sequential data, consider the sequential moves in a chess game such as “black moves a knight to $^ { \mathrm { a 6 , } }$ and then white moves a bishop to d6.” Such data can be used to classify chess games into ones played by ex perts versus ones played by novices [16].

As stated in [17] sources of sequential data surround and pervade our lives. Recently, there has been an enormous growth in the amount of commercial and scientific data, such as protein sequences, retail transactions, and web-logs consisting of data that have an inherent sequential nature.

## 2.2. Low cardinality data

Data attributes represent what the data is capturing, which can for example be the distances traveled by satellites, or marital status of persons. In general, data attributes can be continuous (implying that they contain real numbers and are defined over a continuous range) or categorical (meaning that they can take only a finite number of values) [18]. Distance traveled is an example of a continuous attribute and marital status is an example of a categorical attribute. The cardinality of a categorical attribute is defined as the number of distinct values that an attribute can take [19]. Attributes with a low cardinality are referred to as ‘traditional’ categorical attributes whereas the attributes with a very high cardinality are named ‘high-cardinality’ attributes. The threshold for high and low cardinality is somewhat subjective but 100 distinct values is certainly high-cardinality [18].

Based on literature [20] it can be noted that features with > 100 diferent values are rarely used directly. We will adopt a stricter definition of low cardinality attributes. In our framework we consider attribute value combinations, so a high number of those combinations leads to the typical problems of clustering high dimensional data. Thus, our low cardinality definition is no more than half a dozen distinct values.

The framework we are presenting here is suited for sequential data with categorical attributes of low cardinality. While this requirement may seem somewhat restrictive, the examples we will present in this paper will show that our approach is applicable to a wide range of data. One of the reasons for broad availability of data suited for our approach is the commonly used data preparation technique based on classification coding that can reduces the number of possible attribute values in the data set. Furthermore, any quantitative variable can be transformed to a low-cardinality categorical variable by partitioning the entire range of the variable values into several contiguous sub ranges [21]. Therefore, it is important to note that numerous real-world environments and scenarios create sequential data that is either of low cardinality or can be reduced to low cardinality as we will illustrate and discuss in this paper.

## 2.3. Related work

In this paper, we consider data visualization not only as an end product for communication of results and findings, but also as an integral part of the data analysis process. In the literature, this integrated approach is often referred to as Exploratory Data Analysis (EDA) [6]. With the proliferation of data analytics of large amounts of data for all levels of management, government, and science, the interest in EDA has increased dramatically [7,22]. There are many software tools developed and marketed with a focus on EDA for a large audience, not just other software developers or business analysts with advanced technical capabilities [23–25]

Sequential data is typically visualized using lines with diferent colors [3,9,26]. For distributions, a number of techniques have been developed and studied including histograms, stacked column charts and slopegraphs [3,27]. One of our contributions is the principled, flexible, and iterative approach to transforming and aggregating the sequential data, and then visualizing the resulting distributions.

Reordering of data in order to visually display and discover patterns and structures has been examined in the context of reorderable matrices [28,29]. Selecting a meaningful ordering requires some domain knowledge. As [29] points out “It is typical for all applications that they call for human expertise in the ordering of the rows and columns”. We apply the reordering principle to the distribution visualization of stacked bars.

While we employ the standard practice of visualizing clusters in multi-dimensional space by projecting them on 2 of the significant dimensions [30], we also propose a novel visualization methodology that uses the sequential nature of the data in order to display patterns, trends, and outliers

## 3. Framework

Our framework is based on a novel approach that combines data preparation, data visualization and data clustering techniques. Our aim is to provide insights via descriptive modeling for the entire data set as well as for segments of the set. The data sets to which our approach is applicable consist of sequential data where outcome states in each time period can take on (or be reduced to) one of the limited number of values contained in low cardinality attributes (as defined above). Each data set instance should also contain a number of descriptive classifier attributes, also with limited number of distinct values.

![](/api/attachments/7MZKDGFN/fulltext/images/ecbf0beac0b6bb413ceab57eb395beda68a4b744dae2f48a82a05a4fd444220d.jpg)  
Fig. 1. Framework.

The proposed framework, as shown in Fig. 1, has two phases. In Phase 1, we explore the large amount of sequential data using data preparation, data visualization, and data transformation supported by statistical methods. The process in Phase 1 can be iterative and can be recursively repeated at several points as outlined in the descriptions of the diferent stages. In Phase 2, we include descriptive attributes associated with the entities that generate the sequences. We segment the sequences into cohorts (e.g. prime age males with college degrees) that are based on the descriptive attributes (e.g. age, gender, education). Subsequently, we cluster the cohorts using a metric based on sequence motif distribution within each segment, as we will illustrate later in the examples in this paper. Using several types of visualizations of the clusters, we analyze the trends, diferences, changes, and outliers of the cohorts.

The goal of this framework is to generate novel insights by looking for patterns based on the available data [31]. The framework accom plishes this goal in a way that, while being accessible, brings out in sights that could be missed by strictly focusing on non-visual statistical and data mining methods.

## 3.1. Phase 1: sequence analysis

In Phase 1, we explore the large amount of sequential data in stages that can be undertaken iteratively. Those stages include data preparation, counting and value-based ordering, distribution visualization, and subsequence length determination, confirmation, and revisualization.

## 3.1.1. Stage 1: data preparation

In analysis of data with sequential structure, it is often necessary to aggregate or summarize data at a higher level of granularity than its lowest level of natural coarseness. This process is typically called data coarsening [32]. The aggregation is needed when the data is by its nature continuous or when the number of possible discrete values is high.

There are two intertwined axes of coarsening for sequence data: time period and value (state). For example, consider a sequence of stock quotes taken every second of the trading day for the same company. Based on the data, the lowest level of granularity (i.e. time period) is 1 s and the value is the stock price at that moment. However, we may want to redefine time period to be longer and coarsen the data. If we consider a time period of 1 h, we will also have to define the value of the stock price for that hour. There are several options for computing the value: the average of all quotes, the last quote, the maximum quote, etc. The actual choice will depend on factors such as standard practices and domain knowledge.

The coarsening (or widening) of the time period definition, can introduce smoothing of data by averaging out localized variations. For example, in [33] the aggregation assumes that short-term fluctuation of the stock (say, within the period of 10 days) is not as important as its longer-term behavior, and therefore a 10-day period can be replaced with the average stock price during that time.

Time period definition can also be event driven. This is the case in a number of important settings, such as text, video, speech signals, biological structures, and web usage logs where a sequence is generally an ordered list of singletons [34]. Such event-sequence data is common to a broad range of application domains, from security to health care. This form of data captures information about the progression of events for an individual entity (e.g., a computer network device or a patient) in the form of a series of time-stamped observations [34].

In principle, increasing the coarseness of outcome value data is done with an awareness that the loss of diferentiating ability of data is exchanged with the reduction of the number of possible values. This tradeof is necessary to enable the visualization and clustering in a reduced dimensional space in a descriptive way that will motivate insight generation. The principle we adopt in our approach, is to limit the number of discrete values to be small, up to but no > 12. This restriction in our approach is motivated by two key factors. The first one is Miller Law as stated in the seminal article [35] centered around the notion of the magic number 7 (plus or minus two) and which provides evidence that most adults can store between 5 and 9 items in their short-term memory.

The second factor is the ability to diferentiate colors in human working memory. While humans can distinguish the diference in hue, saturation and value (brightness) in excess of a million color combinations, human color memory is not very good [36] since people tend to coarsen (bundle) colors when memorizing them, which leads to a limited number of colors that can be readily identified.

In the example we will present in Section 4, we conduct the data coarsening of all our outcomes, converting them into low cardinality attribute. The dimensionality reduction of time sequences is defined by the nature of data collection (monthly survey about employment throughout the month instead of daily or weekly employment status).

With the dimensional reduction completed, the data set can be described as follows:

Each sequence consists of d observations (states) where d is the number of time periods in which observations are recorded or derived by data coarsening. Each observation can assume one of e distinct values from a set E. Thus, each sequence is a list $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , . . . , \mathbf { x _ { d } } ,$ where each x assumes one of the discrete values in E.

The key point is to apply this coarsening approach in situations and data sets that ‘make sense’, meaning that the coarsening approach is fully transparent and can be rationally argued, and where interpretation and visualization of data points in the reduced dimensional space still carries logical meaning and ability to generate insight in a specific domain to which the data pertains.

For example, consider the games that a soccer team plays during a particular season. Each game has 3 possible outcomes for this team: a win (W), a draw (D), or a loss (L). This is the lowest level of granularity for this sequence data. For any team in the English Premier League (EPL) during the 2017–18 season, the sequence of game results consists of 38 values. However, in order to analyze the performance of the teams, we may consider coarsening the data by grouping multiple games into a single time period. Such aggregation will lessen the ex ternal efects of playing games home and away and facing diferent opponents. For instance, assume that the time period is widened to be a month instead of a single game. Then the sequence for every team will have just 10 observations (Aug 2017–May 2018). Of course, now we have to define the observation values for every month based on the individual games in it. A reasonable approach may be to sum up the points gained during the month, assuming 3 points for a win, 1 point for a draw, and 0 points for a loss. The range of these values is between 0 and 15. In order to reduce the cardinality of this month-outcome attribute, we can coarsen the values, by specifying several ranges. For example, 0–3 points for a losing month (L), 4–8 for a neutral month (N), and 9–15 for a winning month (W).

Note that we can refine this stage by observing problems with the computation of the values (outcomes) for new time periods. For ex ample, most values may be the same because we have aggregated the data too much. Then, we can adjust the time period definition, or modify the method for computing the value for each time period. In the EPL example, if it turns out that most of the months are neutral, we can shorten the corresponding range of points from 4 to 8 to 4–6.

This iterative nature of this stage is illustrated in Fig. 1. A running example illustrating all stages of the framework will be given in Section $^ { 4 , }$ and it will include an example of Stage 1 in Sub-section 4.1.

## 3.1.2. Stage 2: counting and value-based ordering

The goal of this stage is to generate the data that will be visualized

in Stage 3. In this stage, we divide every sequence into two parts: the head and the tail. The head is the last and most recent observation and the tail (also known as the lagged variable) is the rest of the sequence which consists of the first d-1 states. We divide all full sequences into diferent groups based on the value of their tails. Since each tail is a sequence of length d-1, where each observation can have e distinct values, there are $\mathbf { e } ^ { \mathbf { d } - 1 }$ groups. For each group, we compute the frequencies of the e diferent values of the heads. Thus, for each group we derive a vector $( \mathsf { f } _ { 1 } , \mathsf { f } _ { 2 } , . . . , \mathsf { f } _ { \mathrm { e } } )$ where $\mathsf { s u m } ( \mathsf { f } _ { \mathrm { i } } ) = 1$

In order to visualize all $\mathrm { e } ^ { \mathrm { d } - 1 }$ vectors, we need to order them systematically. We use the highest significant digit principle whereby the first time period is the least significant one and the last one in the tail (d-1) is the most significant one. The goal of this ordering is to position sequences that share common tail subsequences closer together.

Consider a simple example with d = 4 and $\mathbf { e } = 2 .$ Let the two distinct values of X be 0 and 1. Then, there are $\mathrm { e } ^ { \mathrm { d } - 1 } = 2 ^ { ( 4 - 1 ) } = 2 ^ { 3 } = 8$ sequences to be ordered. We can pick any ordering of the values $\mathbf { A } _ { \mathrm { i } }$ of X. In this example, we choose the natural order of 0 before 1. The 8 sequences will be ordered as follows: 000, 100, 010, 110, 001, 101, 011, 111. Note that this ordering of the sequences can also be achieved by multi-key sorting where the last observation (i.e. right-most observation) in each sequence is the primary sorting key, the second to last observation is the secondary key, and so on.

For each sequence, there is a corresponding vector $\mathbf { ( f _ { 1 } , f _ { 2 } ) }$ where $\mathbf { f } _ { 1 } + \mathbf { f } _ { 2 } = 1$ . Each vector represents the distribution of the head values for a specific tail.

The running example in Section 4 will include an example of Stage 2 in Sub-section 4.2.

## 3.1.3. Stage 3: distribution visualization

In this stage we visualize the data generated in Stage 2. The visualization depicts the distribution of each outcome from the set E in the last observation period d for each group. We use a series of 100% stacked columns showing the relative percentage of each of the discrete values in $\mathrm { E } ,$ using a color scale with clear categorical diferentiating ability. This process is referred to as pseudocoloring [37].

Pseudocoloring is a visualization technique for displaying discrete field data, whereby the data values are mapped through a pseudocolor scale—or color map—to determine the color representing each value. The mapping can be arbitrary, but most color maps work by continuously varying some color property, such as hue or saturation, to represent higher and lower data values [37]. Most scales are derived from some physical or mathematical behavior; sometimes they are selected based solely on hardware capabilities, often without consideration made to the perceptual capabilities of the human observer, who is ultimately the “consumer” of the information to be delivered by the scale [38].

A myriad of design rules for what constitutes a “good” colormap can be found in the more recent literature [39]. Some common rules include order, that is intuitive, natural and easy to remember [38,40,41]; perceptual uniformity: the property satisfying the requirement of equal changes in the data value to be equally perceivable in its color representation in the context of display devices [37,40,42,43] and high discriminative power [37,43,44]. The recent research, as well as practitioner's adoption, has identified Viridis scale (shown below) as a an especially good choice because of its ability to convey equally spaced numerical steps as equally spaced perceptual steps, resulting in desirable uniform appearance [39], with an added benefit of being more colorblind safe [45].

## Viridis Scale

For instance, consider an example that observes the size of publicly traded US companies at the end of the year and classifies them as Small (S), Midcap (M), and Large (L). As we are illustrating data associated with companies, we could use the Viridis scale, whose three anchor colors (i.e. right-most, center and left-most) are ripe plum (for S), lochinvar (for M) and ripe lemon (for L). Due to its properties described above (order, intuitiveness, perceptual uniformity, discriminative power, etc.), that would be considered a good choice [39]. On the other hand, if we used the classic-rainbow scale anchors: red (for S), green (for M) and violet (for L), that would be considered a poor choice, due to the absence of desirable properties listed above [37].

The running example in Section 4 will include an example of Stage 3 in Sub-section 4.3

3.1.4. Stage 4. Subsequence length determination, confirmation and $r e \mathrm { - }$ visualization

In this stage, we begin by visually examining charts created in Stage 3 in order to discover patterns. In particular, our aim is to transform the data points representing the original sequences of discrete states of length d into a series of overlapping sub-sequences of size $s \leq \mathrm { d } ,$ where the appropriate sub-sequence length s is suggested by visualizations and confirmed by statistical means.

When analyzing a data sequence, the selection of an appropriate mathematical model for the data is primarily motivated by the aim of prediction and/or rule discovery [46–48]. However, in our framework, the aim is to determine the most useful process sub-sequence granularity for the purpose of data transformation and presentation in a visualized context that will generate further insight. In other words, we want to determine whether discrete outcome values in our original sequence should be best transformed as:

• A series of d single values in each time period of a sequence,

• A series of d-1 overlapping sub-sequences of ordered pairs of out come values in two consecutive time periods of the original se quence

• A series of $d \cdot s + 1$ sub-sequences of ordered s-tuples in s consecutive time periods.

This determination is driven by examining sequences of sequential data with low cardinality attributes in the context of a Markoy chain model. The sequential data sets this paper is focused on represent processes consisting of events that take place at (or are measured in) discrete time intervals and whose outcomes are described by the discrete (countable) state space, which fits the most-narrow definition of a Markov Chain as a type of process that has either a discrete state space or a discrete index set (often representing time) [49]. A Markov chain of order 1 is a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event [50]. If the chain is currently in state $\mathbf { s _ { i } } ,$ then it moves to state s at the next step with a probability denoted by ${ \mathrm { p } } _ { \mathrm { i j } } ,$ , and this probability does not depend upon which states the chain was in before the current state, the process is defined as a Markov Chain [51]. In other words, if the Markov chain is currently in state $s _ { \mathrm { i } } ,$ then it moves to state s at the next step with a probability denoted by ${ \bf p _ { i j } }$ (the process can remain in the state it is ${ \mathrm { i n } } ,$ and this occurs with probability $\mathbf { p } _ { \mathrm { i i } } ) _ { \cdot }$ , and this probability does not depend upon which states the chain was in before the current one. The probabilities $\mathtt { p _ { i j } }$ are called transition probabilities. A square array R of transition probabilities $\mathtt { p _ { i j } }$ is called the matrix of transition probabilities, or the transition matrix [51]. A Markov chain of order m is a process where the probability of each event depends only on the states attained in the previous m events. In the context of our framework, the visualization of $\mathrm { e ^ { \mathrm { { d } \mathrm { { - 1 } } } } }$ vectors conducted in Stage 3 will provide an indication whether data sequences are consistent with the first, second or higher (s) order Markov chain, leading to the proper choice of sub-sequence granularity on which to base our data transformation.

The running example in Section 4 will include an example of Stage 4 in Sub-section 4.5. In this particular example (as we will discuss in Subsection 4.4) the visualization of vectors of individual state observations over eight time periods indicates that the proper data transformation is to group it into series of overlapping sub-sequences of ordered pairs of state observations.

Before committing to the data transformation based on the sequence size s indicated by visualization, we recommend confirming the existence of suficient explanatory power of all s elements of each subsequence with respect to the individual state value observation immediately following each sequence by obtaining statistical confirmation. In other words, we want to confirm whether the process is autoregressive up to s periods. In our example, that will be discussed in Subsection 4.4, we demonstrate how logit regression confirms, for the particular data set, that the process is auto-regressive up to two periods (i.e. second order Markov process), as shown in Fig. 4.

There are several important points to reiterate here. We use visualization to generate insight regarding the choice of subsequence length for the data transformation, prior to confirming our insight with explicit statistical test. Also, we expect that in most cases the subsequence length s will not exceed the value of 3. In practical forecasting methods, the order of auto-regressive processes is usually restricted to 3 and results/explanatory powers are rarely improved by going beyond the order of 2 [52]. Furthermore, an order higher than 3 is indicative of presence of shocks or seasonality and thus the time series is not a pure auto-regressive process [53]. Also, keeping in mind that the primary aim of this data transformation is to improve insight generation we want to limit the number of values obtained through grouping and visualization to be small, which implies that even with the length of subsequence s set at three, the number of individual state values should be limited to two so that the total number of ordered 3-tuples does not exceed 8.

Having transformed the data in our original sequence of individual state outcomes into a series of overlapping ordered pairs or s-tuples of outcomes, re-visualizations of the original data set will lead to clearer insight. Firstly, the data set created in Stage 2 and visualized in Stage 3, consisting of series of $\mathrm { e } ^ { \mathrm { d } - 1 }$ stacked columns can be reduced to the smaller number of $\boldsymbol { \mathrm { e } } ^ { s }$ stacked columns, producing a stacked column chart figure that, due to the smaller number of columns used, shows the confirmed insight in a less complex way than the one produced in Stage 3 (as shown in Fig. 5 in the running example discussed in Sub-section 4.4).

Furthermore, based on the confirmed value of $s ,$ we redefine the meaning of what an “observed state” is, and re-label accordingly, whereby each “observation” is a combination of value sequences of size s (as opposed to always using a single value label to define each observation). The reasoning we apply is as follows. If present state only depends on the last previous state as in the Markov chain, each observation is a single value. However, if present state depends on two previous states as in Markov chain of order two, then each observation in the transition probability matrix is actually based on pairs of single states observations. Such transition matrix can be visually depicted as an s-dimensional De Bruijn directed graph of e symbols of representing overlapping sub-sequences of s consecutive outcomes where each outcome is one of e possible state values (as shown in Fig. 6 in the running example in that will be discussed in Sub-section 4.4). In graph theory, an n-dimensional De Bruijn graph of m symbols is a directed graph representing overlaps between sequences of symbols [54]. It has m<sup>n</sup> vertices, consisting of all possible length-n sequences of the given symbols whereby the same symbol may appear multiple times in a sequence [55]. In the context of our framework, each vertex is a combination of possible discrete state sequences and the thickness of edges between two vertices (or auto recursive edges) may be visualized to correspond to transition probabilities. If the relevant sequence size s = 1 (as in Markov chain), this is equivalent to a standard transition matrix graph. If s > 1, these visualizations correspond to a De Bruijn graph. By combining color shades and thickness of lines, an additional insight may be revealed that may be not apparent from the stacked bar figure of states, as we will demonstrate in the running example in Sub section 4.5.

## 3.2. Phase 2: cohort clustering

In the second phase of the proposed framework, we outline a process for exploring sequence diferences between data cohorts, created using descriptive attributes, and visualizing the changes over time and diferent attribute values. Every sequence is generated by observing the state over time of some real-world entity such as a soccer team, a person, or a stock. These entities have many other attributes such as location, budget, age, education, industry, etc. Our approach enables the clustering and exploration of groups (cohorts) of entities based on their common attributes and their respective sequences. We transform the sequences into motifs (as we will describe below) and use the motif distribution within each group (cohort) to cluster the groups into more general categories. The process consists of the following stages:

![](/api/attachments/7MZKDGFN/fulltext/images/bb19a1fdde8e06f86a67cd6314448647171692415f32a3e496f708944f498a5d.jpg)  
Fig. 2. Sequence and motif example

## 3.2.1. Stage 5. Data transformation: motif generation

In this stage, we derive data from the sequence that can be analyzed further using a combination of clustering and visualization techniques.

We convert every sequence into a set of subsequences of length s where s is the number found in the first phase of our exploratory analysis. We will use the term motif to refer to a subsequence following the accepted practice in sequence analysis [56]. We include every contiguous subsequence of length s with overlap. Note that unlike many other approaches, our motif generation algorithm is simple. We do not mine specific, frequent, or representative motifs. Instead, we use the distribution of all of them within each group of real-world entities.

Our rationale for this transformation is that the set of motifs provides a characterization of the initial sequence that can be compared with the characterization of other sequences. Furthermore, the union of such sets for two groups of sequences can provide a principled way to compare the two groups even if there is little overlap between the full sequences and even if the two sets are very diferent in size (orders of magnitude).

Formally, a sequence $\mathrm { X _ { 1 } , \ X _ { 2 } , \ X _ { 3 } , \ X _ { 4 } , . . . , \ X _ { n } }$ will generate $\mathbf { n } { - } s + 1$ subsequences (motifs) of length $s ,$ starting at positions $1 , 2 , . . . , \bar { \bf n } { - } s + 1$ This is illustrated by Fig. 2, where length $s = 3$

Note that we consider the generated motifs as a set, so their order does not matter. Of course, the order of the states within a motif does matter.

The running example in Section 4 will include an example of Stage 5 in Sub-section 4.5.

## 3.2.2. Stage 6: cohort selection based on descriptive attribute coarsening

In this stage, every sequence is associated with its corresponding entity (such as a team or a person). These entities have other attributes that may be of interest for the analysis and exploration of the data. The attributes may be demographical such as age and gender, geographical such as location and city, or any other type. Given a particular domain, there may be standard ways of coarsening a continuous attribute, or aggregating categorical values into larger groups. For example, there are several standard categorizations for age in diferent domains such as ratings, retail, and advertising [57]. Also, precise locations can be aggregated to the level of zip codes, neighborhoods, cities, etc. The se lection of the attributes and their values is domain and question specific. In this paper, we assume that a selection has been made. Our framework works for any such selection and can be applied to multiple related selections.

Formally, based on the values of the selected attributes and the time

dimension value we generate cohorts as follows:

Let the selected attributes be $\mathbf { A } _ { 1 } , \mathbf { A } _ { 2 } , . . . , \mathbf { A } _ { \mathrm { m } } ,$ and the time dimension T. Let $\mathbf { A _ { i } }$ have $\mathrm { V _ { i } }$ distinct values and T has t diferent values. We generate $\mathrm { V } _ { 1 } { } ^ { * } \mathrm { V } _ { 2 } { } ^ { * } . . . ^ { * } \mathrm { V } _ { \mathrm { m } } { } ^ { * } \mathrm { t }$ cohorts that have the same values for all of their attributes $\mathbf { A } _ { 1 } , \mathbf { A } _ { 2 } , . . . , \mathbf { A } _ { \mathrm { m } } ,$ , and T. For each cohort we consider the union of all sets of motifs generated from sequences in that cohort. Thus, for every cohort we have a set of motifs of length s. Note that the sizes of the sets for diferent cohorts will be diferent, possibly orders of magnitude diferent.

For a simple illustration, consider again observing the size of publicly traded US companies at the end of the year: Small (S), Midcap (M), and Large (L). For each company we only consider two attributes, Industry and Region. Industry has only two distinct values: Tech and Non-tech, and Region has only 3 distinct values: East, Midwest, and West. The time dimension has 3 values: 1990–1999, 2000–2009, 2010–2018. Thus, we group all companies into 6 (2 ∗ 3) cohorts and consider each cohort for every time period, so the result is 18 groups. Within each group we have many sequences corresponding to all publicly traded companies for that industry and region. For example, Microsoft will be in the Tech industry and the West region cohorts for all three time periods. Its 3 sequences will all be LLLLLLLLLL. For $s = 2 ,$ this sequence will be transformed to 9 motifs LL.

The running example in Section 4 will include an example of Stage 6 in Sub-section 4.6.

## 3.2.3. Stage 7: vector generation

For each set of s-motifs corresponding to a cohort, we compute the distribution of all possible values of the s-motifs. Since each state in the motif can have e diferent values, and the length of all motifs is $s ,$ there are $\boldsymbol { \mathrm { e } } ^ { s }$ diferent values. For every such value, we compute the fraction of all motifs in the set that have the given value. Thus, for each cohort, we generate a vector $< \mathrm { f _ { 1 } , f _ { 2 } , . . . , f _ { p } > }$ where $\boldsymbol { \mathsf { p } } = \boldsymbol { \mathsf { e } } ^ { s }$ and $\mathsf { s u m } ( \mathsf { f } _ { \mathrm { i } } ) = 1$

In order to illustrate the vector generation process, consider again the Microsoft example above, where all three sequences are LLLLLLL-LLL. Suppose that in the dataset, there is only one other company in the Tech industry and the West region cohort (we will call it Company X). Suppose that the market size sequence for the Company X during 1990–1999 was SSMSMLMMMM. This sequence will be transformed to the following 9 motifs of length 2: SS, SM, MS, SM, ML, LM, MM, MM, MM. Then the vector generated for the Tech industry and the West region cohort will consist of the frequencies of all possible values of the 2-motifs in the union of the motif sets (with duplicates) for Microsoft and the Company X. In this case, $\mathbf { e } = 3 , s = 2 , s _ { 0 } p = 2 ^ { 3 } = 9$ . Then the vector $< \mathrm { f _ { 1 } , f _ { 2 } , f _ { 3 } , f _ { 4 } , f _ { 5 } , f _ { 6 } , f _ { 7 } , f _ { 8 } , f _ { 9 } > }$ will be: $< 1 / 2 , 1 / 1 8 , 0 , 1 / 1 8 , 1 / 6 , 1 /$ $9 , 0 , 1 / 1 8 , 1 / 1 8 >$ , where f is the frequency of LL, $\mathbf { f } _ { 2 }$ is the frequency of ML, $\mathbf { f } _ { 3 }$ is the frequency of $\mathrm { { S L } , f _ { 4 } }$ is the frequency of LM, f is the frequency of MM, $\mathrm { f } _ { 6 }$ is the frequency of SM, f is the frequency of LS, f is the frequency of MS, and $\mathbf { f } _ { 9 }$ is the frequency of SS.

The running example in Section 4 will include an example of Stage 7 in Sub-section 4.7.

## 3.2.4. Stage 8: vector clustering

In the stage we cluster al $\mathrm { V } _ { 1 } { } ^ { * } \mathrm { V } _ { 2 } { } ^ { * } . . . ^ { * } \mathrm { V } _ { \mathrm { m } } { } ^ { * } \mathrm { t }$ vector in $\boldsymbol { \mathrm { e } } ^ { s }$ dimensions. In principle, we can apply any clustering algorithm. The goal is to find groups of cohorts that have similar distribution of their s-motifs.

There are several families of clustering algorithms. The choice for any particular dataset depends on the expected distribution, data size, and domain knowledge. In our framework, the total number of data points represented by the sequences is already reduced because of the data transformation described in Stages 5–7. The number of vectors to be clustered is $\mathrm { V } _ { 1 } { } ^ { * } \mathrm { V } _ { 2 } { } ^ { * } . . . ^ { * } \mathrm { V } _ { \mathrm { m } } { } ^ { * } \mathrm { t }$ and typically will be relatively small because of the value coarsening of $\mathbf { A } _ { 1 } , \mathbf { A } _ { 2 } , . . . , \mathbf { A } _ { \mathrm { m } }$

A good choice is a hard-clustering algorithm like K-Means [58] or its derivative models like hierarchical clustering methods [59]. Another option are soft probabilistic clustering techniques/mixture models like Expectation Maximization algorithm which works like the K-Means algorithm but assigns probabilities of being a member of each cluster to each data point instead of exact and hard associations to diferent clusters [60,61]. Unlike K-Means (which tries to estimate the center of the clusters in terms of a vector of N-dimension), Expectation Maximization tries to estimate a Gaussian Distributions for each cluster with their respective variances and means. Consequently, all given vector points in a hyperplane will have associations with multiple clusters but with diferent probabilities. This group of techniques can be better suited if we believe that clusters may overlap each other, and K-means is unable to discover these latent features of the data due to this overlapping. Both K-means and mixture models like Expectation Maximization work well when expected clusters are spherically shaped but sometimes the cluster shapes may be irregular instead of spherical. In those circumstances, density-based models (in particular DBSCAN) can provide a better method for discovering irregularly shaped clusters.

The running example in Section 4 will include an example of Stage 8 in Sub-section 4.8.

## 3.2.5. Stage 9: cluster visualization and analysis

In this stage we outline two types of visualizations of the clusters that can lead to finding patterns, trends, and outliers: projection and pacman. The outline of the visualizations is captured in Table 1. An example of projection visualization will be given in the running example in Section 4, in Figs. 10 and 11, in Sub-section 4.9 that gives an example of Stage 9. An example of Pacman visualization will be given in the running example in Section 4, in Fig. 12, in Sub-section 4.9 that gives an example of Stage 9.

## 4. Framework application example: current population survey

In this section we present a detailed running example of the appli cation of the proposed framework to a large, formally-maintained dataset. Using a formally-maintained data set to validate our framework was of critical importance. As stated in [62] “erudite modeling and esti mation can yield no immediate value or be meaningfully replicated without high quality data inputs”.

Current Population Survey (CPS) dataset is collected and main tained by the United States Census Bureau on behalf of the Bureau of Labor Statistics and it is used to calculate the major unemployment statistics for the US economy [63,64]. The CPS captures labor market and demographic information (such as age, gender, education level, employment status, etc.) from about 60,000 households across the United States. In our analysis, we use the dataset containing data from the CPS from 1974 through 2015, which encompasses $> 3 6 , 0 0 0 , 0 0 0$ observations.

The CPS survey is administered monthly with participants being interviewed for 4 months, omitted for 8 months, and then interviewed again for 4 months. Therefore, any interviewee can appear in the sample for a total of 8 months. This rotating panel research methodology for survey sampling (as opposed to a more traditional approach called fixed panel methodology) is used often in situations where measurements and their respective statistical estimates are calculated over a long period of time (multiple months or years) which exposes the subject of the analysis to natural and logistical changes like mortality, migration and changes of underlying assumptions [65–67]. In this methodology, equal sizes of sets of sample units are brought in and out of the sample in some specified pattern. These blocks of sample sets are called rotation groups. The blocks represent interview participants being in and out of rotation based on the pattern (4-8-4). The key ad vantage of rotating panel methodology has been the reduction of the variances of statistical estimation of level or change as compared to fixed panel approach. [65–67]. Henceforth, the CPS 4-8-4 rotating panel methodology improves the accuracy of the month-to-month, quarter-to-quarter, and year-to-year change estimates. The approach guarantees that in any given month, 1/8th of the housing units are interviewed for the first time, another 1/8th is interviewed for the

<table><tr><td>The number of clusters in the X dimensions is calculated as:</td></tr><tr><td>Projection and pacman visualizations.</td></tr><tr><td>The clusters are visualized by projecting the vectors in two dimensions defined by two of the es dimensions. The choice of the projection dimensions depends on the particular domain. It may also depend on the magnitude of their values in the frequency vectors.</td></tr><tr><td>Pacman</td></tr><tr><td>The clusters are visualized in a bi-directional table with the X axis corresponding to the time dimension T and the Y axis including all other attributes A1, A2, ..., Am. Each cell is a circle corresponding to a cohort and the color of the circle corresponds to the specific cluster that the cohort belongs to. Thus, each row contains t circles of different colors that represent the change or stability of the observed states of that cohort over time. This visualization is used to determine the changes over time of a given cohort based on the variability of the colors in the same rows. It can also be used to explore differences and similarity between different cohorts in different times. By pivoting the table, the differences due to the different values of the innermost attribute in the Y dimension of the table can be compared.</td></tr></table>

second time etc.

## 4.1. Data preparation

According to US Bureau of Labor Statistics, the primary purpose of the CPS is to “classify the sample population into three basic economic groups: The employed, the unemployed, and those not in the labor force.” [68]. In particular, the employment statuses are defined as follows [68,69]. People are defined employed, unemployed or not in the labor force, as those who, during the survey reference week (generally, the week that includes the 12th day of the month), met the following cri teria shown in Table 2.

The actual employment status of individuals in the CPS is derived from answers to several questions in the survey in order to ascertain its correctness [63]. To describe the employment status, we will use the following abbreviations employed (E), unemployed (U) and not-in-thelabor-force (N).

We first investigated the patterns of individual employment status over the eight months of interviews (i.e. the 4 + 4 part of the 4-8-4 rotation). In particular, we considered the first seven months and their relationship with the last month. Thus, the time period is defined by the data collection method and it is 1 month, and the sequence observation length, d, is 8. The number of states, e, is 3 (E, U, and N).

## 4.2. Counting and value based ordering

Given that d = 8 and e = 3, for the first seven months, there are 2187 $( = 3 ^ { 7 } )$ possible sequences of the employment statuses E, U, and N. The sequences range from EEEEEEE representing a person who was employed for the first 7 months of interviews, to UUUUUUU representing a person who was unemployed for the first 7 months of interviews. For each of the 2187 possible sequences, we identified all participants that exhibit the corresponding status sequence. Thus, we partitioned the data into 2187 segments. For each segment, we calculated the percentages of those participants that exhibit E, U, and N for the eighth and last month. For example, for everyone who was employed in the first seven interviews (sequence EEEEEEE), the percen tages of the eighth month are 98.72% for E, 0.46% for U, 0.82% for N.

## 4.3. Distribution visualization

The results of this initial investigation are visualized in Fig. 3. The sequences of the first seven interviews on the horizontal axis are ordered starting from EEEEEEE and ending at UUUUUUU. The letter closest to the axis represents the seventh interview month, while the farthest letter represents the first interview month. The complete ordering of the sequences is based on changing E to N, then to U, starting at the first month, then resetting the first month to E, changing the second month to N and continuing the process. In other words, we apply significant digit ordering<sup>1</sup> to place sequences in the aligned order with order of significance descending from right to left (opposite of the order of state sequence progression in time). For example, the first few sequences in this order are: EEEEEEE, NEEEEEE, UEEEEEE, ENEEEEE, NNEEEEE, UNEEEEE, EUEEEEE. Note that while the labels on the horizontal axis in Fig. 3 represent only some of the sequences, the visualization includes the breakdown of the eight and last interview month for all 2187 sequences. Using pseudocoloring, each sequence is represented by a single line, consisting of portions represented by three anchor colors on the Viridis scale (ripe plum for E, lochinvar for N, ripe lemon for U). These portions correspond to the percentage of the labor force status in month 8 (E, N, U), respectively, for all individuals in the particular segment.

Employed, unemployed, not-in-labor-force criteria.

<table><tr><td>Employed</td><td>Unemployed</td><td>Not in labor force</td></tr><tr><td>- Did any work at all as paid employees (a minimum of 1 h)</td><td>- Were not employed during the survey reference week</td><td rowspan="4">- Neither column 1 nor 2</td></tr><tr><td>- Worked in their own business or profession, or on their own farm</td><td>- Were available for work (except for temporary illness)</td></tr><tr><td>- Worked 15 or more hours as unpaid workers in a family member&#x27;s business</td><td rowspan="2">- Had made a specific, active effort to find employment sometime during the 4-week period ending with the survey reference week</td></tr><tr><td>- Were temporarily absent from their jobs or businesses because of illness, vacation, bad weather, a labor dispute, or another reason (whether or not they were paid for the time off or were seeking other jobs)</td></tr></table>

![](/api/attachments/7MZKDGFN/fulltext/images/2849c6acb60925539703e331ccadbc134633a0d354f9536eb92e3e36bfcb6907.jpg)  
Fig. 3. Distribution visualization

## 4.4. Subsequence length determination, confirmation and re-visualization

A visual examination of Fig. 3, leads to a conjecture that there are 9 diferent groups with similar color patterns. We demarcate these groups with white vertical lines in Fig. 3. The first group consists of lines which are predominantly ripe plum, corresponding to a large percentage of E in the last time period. The next group consists of lines with significant portion of lochinvar in the middle. In these groups the percentage of the last month with status N is larger. The third group is categorized by the significant amount of ripe lemon, corresponding to U status in the last month. The other 6 groups exhibit the same patterns. These nine groups closely correspond to the employment status of the last two interview months (6th and 7th) of the sequences.

This observation leads to further analysis to indeed confirm that the final employment status is heavily dependent upon the previous two statuses (antepenultimate and penultimate) and statuses prior to antepenultimate period did not have heavy influence on the final month status. We confirmed the insight generated by visualization by conducting the series of the logit regressions with the dependent variable being the employment state in the last period and predictor variables the employment states in previous periods. The Fig. 4 below shows the sharp drop in the explanatory power of previous periods after the period t-2.

Accuracy of the models can be improved by including more parameters but that leads to more complex models. An optimal model is one that provides given accuracy for the least number of parameters. AIC (Akiake's Information Criterion) is a measure that provides the balance between error rates (sum of squared errors or SSE) and number of parameters (K), and it is one of the most commonly used metrics to choose optimal model from multiple models. The model with lowest AIC is usually an optimal model amongst various candidate models [70]. For N observations and K parameters, the AIC is as follows:

![](/api/attachments/7MZKDGFN/fulltext/images/24b30806cf412b2de495285d235241cab780a26426f607c69ca4db85a8dab8ff.jpg)  
Fig. 4. Explanatory power of previous periods.

Based on this finding, we investigated a generalized relationship between the employment status for the first two months and status in the third month, for any 3 consecutive interview months. Because of the 8-month gap between the fourth and fifth interviews, we do not con sider those statuses to have the same relationship as two consecutive calendar months, so those observations are excluded. Thus, from every 8-month sequence, we generated four 3-month sequences using only consecutive interview months: (1st, 2nd, 3rd), (2nd, 3rd, 4th), (5th, 6th, 7th), (6th, 7th, 8th).

We applied the partitioning scheme based on status combination to all 3-month observations using all 9 possible sequences of two employment statuses for the first two months in a sequence: EE, EN, EU, NE, NN, NU, UE, UN, UU. Note that for ease of explanation in this and all subsequent notations, the first letter corresponds to the first interview month, and the second letter corresponds to the second (and more recent) interview month. For each partition, we calculated the percentages of those participants that exhibit E, U, and N for the third consecutive month. The results of this new computation appear in Fig. 5.

We observe that the grouping pattern persists even without accounting for the earlier employment status. For example, the last of the nine groups in Fig. 3 has a very similar color pattern to the one in the last column (UU) in Fig. 5. Furthermore, we observed that there are significant pattern diferences between segments that share the same second-month status. For a particularly striking example, consider the segments UN and NN. Data observations in both segments include a “not in the labor force” (N) status for the second month. However, the third month status for NN is N in over 90% of the observations in the segment, while for UN, the third month status is N in < 70% of the observations in the segment.

This analysis motivates Phase 2 where we consider the partitioning of any population into the 9 diferent two consecutive month sequences. Thus, for any population, instead of having just three numbers: percentage employed (E), percentage unemployed (U), and percentage “not in the labor force” (N), we use 9 numbers corresponding to the percent employed for two consecutive months (EE), percent employed in previous month but currently unemployed (EU), and so on.

Note that the graph in Fig. 5 contains values that may appear counterintuitive. Consider the diference in final state probabilities between the following observation pairs: UE vs EU. The probability of an individual being in the state E in period t is greater when the employment state of that individual was U in period t-1 and E in period t-2 than vice versa. Same holds for observation pairs NE vs EN. However, with the use of further visualizations that lead to drilling down into the data, this outcome is logically explained.

Fig. 5 as stacked bar chart is appropriate given only 3 categorie being displayed. In instances with more categories, a more appropriate display (given human perceptual and cognitive limits) may be a slo pegraph.

The Fig. 5 can be recast as a De Bruijn graph, treated here as a specialized state transition network graph where each node represents a “state” as a combination of employment states in two consecutive periods. This is shown in Fig. 6. Standard definition of a De Bruijn graph is the one whose nodes are sequences of symbols from some alphabet and whose edges indicate the sequences which might overlap [55]. We include it here since it provides an alternative way of presenting the employment data in terms of the strength of tendencies for labor force participants to persist in a particular state as well as to transition to another state where employment state is treated as multi-period (in this case two period) event rather than the single (most current) event. The edge width (thickness) represents the probability of transition from the state represented by the outbound node into the state represented by the inbound node. For example, the edges starting at the node EN and terminating in the nodes NE, NN and NU are of very diferent width. The edge from EN into NE is wider (thicker) than the edge from EN to NN, representing greater probability of that the sequence EN will transition into NE than NN. Conversely the edge form EN to NU is the thinnest of those emanating from the node EN, representing the smallest probability that the sequence EN will transition into NU. This is consistent with the with distribution depicted in the 4th vertical bar in the Fig. 4 showing probabilities of an observant being in the state into E, N and U respectively if the previous two observed states were EN.

Furthermore, in Fig. 7 we present a reduced graph with only two types of states and their respective transition probabilities: “stable” (comprising pairs: EE, NN and UU) and “unstable” (all other pairs). Fig. 7 explains a counterintuitive outcome observed in Fig. 5, namely that unstable state has much higher probability of remaining unstable than probability of transitioning into the stable state.

Drilling further into the raw data confirms this insight, as demon strated by Fig. 8.

Note, that after the two sequences whose frequency dominates all others and are representing stable states of permanent employment and permanently not seeking employment (EEEEEEE and NNNNNNN), the next two most common sequences are the ones where those two states alternate in each subsequent period (ENENENE and NENENEN).

![](/api/attachments/7MZKDGFN/fulltext/images/090b320877b33ee901dc92e46b91e63500bb88634016ac83a1f7792826b5ade7.jpg)  
Fig. 5. Summarization of distribution visualization.

![](/api/attachments/7MZKDGFN/fulltext/images/5c52135716fa0b6146678a703deaa29c062796f845ca675e4c172cb4e7731f7b.jpg)  
Fig. 6. De Brujin graph of transition probabilities.

## 4.5. Data transformation: motif generation

As specified in Stage 5 of our proposed framework, we transform each sequence of 8 states into 7 motifs of size 2. For examples, EEN-NEEUN, will be transformed into the set (EE, EN, NN, NE, EE, EU, UN). This transformation reflects the insight that the pairs of consecutive employment statuses provide the best description of employment outcomes.

![](/api/attachments/7MZKDGFN/fulltext/images/367d2ab9b52d2966f1cf65c345bd7aa31da74fd1e9b116bbc14aa1f55a016037.jpg)  
Fig. 7. Reduced graph of transition probabilities.

![](/api/attachments/7MZKDGFN/fulltext/images/432cea0064bbb872611bbed80cfcde82e10b71dfd4b0619bdbbd99e02b71aa55.jpg)  
Fig. 8. Ranked sequence frequency distribution chart.

## 4.6. Cohort selection based on descriptive attribute coarsening

In the next stage of our analysis, we conduct segmentation of our data set based on a set of categorical variables. We considered three demographic classifications variables: age, gender, and education. While the CPS data contains a very detailed description of education, we have re-coded the education variable into four standard categories (At Least a Bachelor's Degree, Some College, High School, Less Than High School). The age variable is recoded into 3 categories (16–24, 25–54, 55–64). Interviewees over 65 have been excluded from our analysis because the majority of them are retired and rarely re-enter the labor force. The gender variable is coded as it is collected using the categories of Male and Female. Segmenting the interviewees for each year separately, using the 3 variables and their corresponding categories, yields 960 segments (40 years ∗ 2 genders ∗ 4 educations ∗ 3 ages).

## 4.7. Vector generation

For each of the 960 segments we calculated the partitioning of the segment population into the 9 two-status sequences (EE, NE, UE, EN, NN, UN, EU, NU, UU). Thus, we have 960 9-dimensional vectors with each vector component representing the percentages of participant with $\mathrm { E E , N E , . . . , }$ UU status for each of the 960 segments.

## 4.8. Vector clustering

We leveraged the k-means clustering algorithm to compute clusters of the 960 vectors corresponding to various combinations of the four categorical variables described above. K-means clustering algorithms use an iterative method of identifying and partitioning the data into subsets known as clusters [49]. Under this approach, each two-status sequence is treated as a dimension and, henceforth, a segment (row with n columns) is treated as a vector in n-dimensional space. Once all segments (vectors) are plotted, the algorithm calculates the distances between them and creates k clusters based on the segments' respective proximity to each other.

The proximity distance was calculated using standard Euclidean distance. In order to find out the optimal number of clusters (k) in the CPS example, we computed the clusters for various values of k ranging from 1 to 15 and calculated a cluster-fit measure within-sum-of-square (WSS) as a function of k [71]. The minimum number of clusters that brings sizable reduction in WSS, is considered to be the optimal number for k. The details of calculation of WSS are as follows:

Where the variables are defined as follows:

k – number of clusters

n – number of points in the i<sup>th</sup> cluster

• c – centroid of the i<sup>th</sup> cluster

$$
\bullet \mathrm{x} _ {\mathrm{ij}} - \mathrm{j} ^ {\text {th}} \text {point of the i} ^ {\text {th}} \text {cluster}
$$

Once the clusters are created, all CPS cohorts are scored with the respective cluster number. Each cohort is assigned to the cluster with other cohorts that are “most like it” where that determination is based on the Euclidean distances between the segments in n-dimensional space. As shown in Fig. 9, for our CPS example, sizeable reduction in WSS ceases after k reaches 7 and therefore, we used 7 clusters. We used the method that involves graphing the coeficient on a y-axis and the number of clusters on an x-axis. A marked flattening of the graph, suggests that the cluster that are being created are becoming similar (i.e. inter cluster dissimilarity and intra cluster similarity were maximized), thus the appropriate number of clusters is found at the ‘elbow’ of the graph [72]. In other words, we followed the recommendation to find the natural number of clusters in a data set by looking for the number of clusters at which there is a knee in the plot of the evaluation measure when it is plotted against the number of clusters [73].

## 4.9. Cluster visualization

In this section, we illustrate how Stage 9, the last stage in our framework, applies to the CPS example. We detail the use of diferent data visualizations in order to examine multiple aspects of the clustering results and derive insights about the data.

![](/api/attachments/7MZKDGFN/fulltext/images/3f3f969b7b1bad4bb3c0030d3a721c4bcab1d054a0529b063fa04e543591fdbb.jpg)  
Fig. 9. Sum of squares over number of clusters for the CPS data set.

First, we consider the review of the clusters in multidimensional space. Typically, visualizing the projections of the clusters along several pairs of the clustering dimensions provide good starting points for the analysis of the results. Domain knowledge plays an important role as well, since the interpretation of the dimensions drives the analysis.

In the CPS example, in order to analyze the 7 clusters, we consider several 2-dimensional projections of the 9-dimensional segments onto some of the important dimensions. Recall that each dimension corresponds to a particular 2-month employment status sequence. Fig. 10 shows the distributions of 960 cohorts into the 7 clusters across EE (employed for two consecutive months) and NN (not in the labor force for two consecutive months) and EE and UU (unemployed for two consecutive months). Diferent clusters assigned by our algorithm are represented by diferent colors. These colors are used to distinguish one cluster from the other (i.e. diferentiating ability).

Each circle (cohort) in the picture corresponds to a combination of the values of the 4 variables (first year of interview, gender, age and education). For example, the purple cluster on the rightmost side of the top panel in Fig. 10 has a very high percentage of continued employment (EE) of > 78% and low percentage of continued unemployment of < 4%. Similarly, the red cluster on the leftmost side has a similar low percentage of continued unemployment (UU) of 3%–8% but a much lower percentage of continued employment (EE) of only 15%–35%. Thus, the demographic segments in the purple cluster have much better employment outcomes than the ones in the red cluster even though their respective unemployment rates may be similar, even when we account for consecutive months of unemployment.

![](/api/attachments/7MZKDGFN/fulltext/images/2b079d8af7e7fbe4271b7ccbf5c690890a86bd1ae15a278b1657957acf8a975d.jpg)  
Fig. 10. Cluster projections on EE (continuous employment) – UU (continuous unemployment) and EE-NN (out of the labor force)

The orange and green clusters have the greatest dispersion in unemployment percentages. However, considering continuing employment or unemployment is only part of the story. The bottom panel of Fig. 10 shows the observation placement in EE-NN space. The purple cluster clearly has the lowest percentages for being out of the labor force (NN); the red cluster has the highest percentages for NN even though it had a similar range of percentages to the purple cluster for UU. The orange and green clusters complete a branch of a continuum for the EE-NN percentages.

If we consider continuous employment to be the most important criteria for judging employment outcomes, then cohorts in the purple cluster, cluster 1, have the most positive employment outcomes. There is a very high probability that they will be employed for two consecutive periods. The cohorts in the red cluster, cluster 7, however, are in a cluster with the worst employment outcomes. They have the lowest probability of continued employment (EE) of only 15%–35%. These endpoints, the “good” purple cluster and the “bad” red cluster, define the range of possible employment combinations we find within the data. Of the clusters in between these endpoints, the blue cluster, cluster 2, is clearly defined as being “almost as good” as cluster 1 for high EE percentages and low UU percentages. The other four clusters exhibit an interesting dichotomy: orange and yellow, clusters 5 and 6, cover the same range in EE-UU space but have very diferent percentages in EE-NN space. The same is true of the green and grey clusters, clusters 3 and 4. Looking at the yellow and grey clusters in EE-UU space shows a similar distribution for continuous employment or unemploy ment but the EE-NN space shows that these cohorts clearly have a weaker attachment to the labor force as they are more likely to be in the NN space.

Such detailed type of analysis, of course, requires substantive domain knowledge and meaningful interpretations of the dimensions corresponding to the 2-motifs. The motif generation and the subsequent visualizations provide a quick starting point for the analysis and a communication tool that is widely accessible. Based on our analysis, we can assign explanatory names to the 7 clusters as shown in Table 3.

The transitions between stable and unstable states, as discussed in Section 4.4, can be analyzed further using the clustering results. We can investigate the cluster coverage for movements into employment from “not in the labor force” (NE) or from unemployment (UE). Fig. 11 shows the projections of the clustering results in EE-UE and EE-NE spaces.

We observe much greater dispersion in cluster 1 when transitioning involves unemployment (U) and much tighter clusters when the transition involves the not-in-the-labor-force status (N). Note that in this example analysis, we chose 4 of the 36 possible two-dimensional combinations using our domain knowledge of the data and our interpretation of the meaning of the clustering dimensions. Actual domain experts (i.e. trained economists) can, of course, chose, interpret, analyze and derive meaning from many more combinations, for the economic research purposes.

The choice in any specific scenario will vary but the interpretations are aided by the clear and principled definition of the dimensions and the visualization of the clustering results.

Next, we consider the low-cardinality aspect of the discrete values in our dataset. As shown in Table 4, since there are only 9 two-status combinations, we can display the average numbers for all 7 clusters, an often-overlooked type of data visualization [3,9].

Table 4 provides a more complete picture of the clustering assignments by the average percentages for each two-state combination for each cluster. Since the K-Means clustering algorithm uses all 9 2-motifs in making cluster assignments, the full set of average percentages helps provide additional intuition on the sorting process underlying this statistical technique. Table 4 displays the average percentages for the nine 2-motifs for each cluster. In other words, each row in the table represents the cluster centroid values.

Comparing the average percentages across clusters, we observe that there is no uniform sorting across all 2-motifs. In assigning cluster numbers, we numbered the clusters from good to bad in terms of the EE percentages, so the descending sorting of column 1 in Table 4 is by construction. The remaining columns, however, indicate that the clustering did not impose a monotone sorting across any other 2-motif. Instead, the cluster sorting highlights distinct features across the seg ments that distinguish individuals in diferent cohorts and also their likelihood of transition between E, U, and N states.

<table><tr><td colspan="8">Cluster names.</td></tr><tr><td>Cluster number</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Cluster Name</td><td>Highest continuous employment</td><td>High continuous employment</td><td>Medium continuous employmentSignificant out of labor force</td><td>Medium continuous employmentSignificant unstable employment</td><td>Low continuous employmentSignificant out of labor force</td><td>Low continuous employmentSignificant unstable employment</td><td>Lowest continuous employment, highest out of labor force</td></tr></table>

![](/api/attachments/7MZKDGFN/fulltext/images/91e03a6c65f57ac56e9f5ad59e18c5c2e0da2549e4ca476d7a6f91b6e8c61c1e.jpg)  
Fig. 11. Cluster Projections on EE-NE (unstable employment) and EE-UE (unstable unemployment).

Table 4  
Average numbers for all two-status combinations in all clusters.

<table><tr><td>Cluster</td><td>EE</td><td>UE</td><td>EU</td><td>UU</td><td>NU</td><td>UN</td><td>NN</td><td>EN</td><td>NE</td></tr><tr><td>1</td><td>86.9%</td><td>1.9%</td><td>1.9%</td><td>1.2%</td><td>0.4%</td><td> $0.5^{\circ}/0$ </td><td>4.1%</td><td>1.7%</td><td>1.4%</td></tr><tr><td>2</td><td>70.7%</td><td>2.2%</td><td>2.0%</td><td>1.5%</td><td>0.8%</td><td>1.0%</td><td>13.9%</td><td>4.3%</td><td>3.7%</td></tr><tr><td>3</td><td>59.7%</td><td>1.3%</td><td>1.2%</td><td>0.9%</td><td>0.7%</td><td>0.8%</td><td>27.2%</td><td>4.3%</td><td>3.8%</td></tr><tr><td>4</td><td>53.8%</td><td>3.1%</td><td>2.8%</td><td>1.9%</td><td>1.9%</td><td>2.0%</td><td>18.8%</td><td>7.9%</td><td>7.8%</td></tr><tr><td>5</td><td>43.3%</td><td>1.2%</td><td>1.1%</td><td>1.0%</td><td>1.0%</td><td>1.1%</td><td>42.8%</td><td>4.5%</td><td>4.1%</td></tr><tr><td>6</td><td>35.7%</td><td>3.2%</td><td>2.9%</td><td>2.9%</td><td>3.2%</td><td>3.2%</td><td>31.4%</td><td>8.5%</td><td>9.0%</td></tr><tr><td>7</td><td>23.2%</td><td>1.5%</td><td>1.3%</td><td>1.5%</td><td>2.4%</td><td>2.4%</td><td>55.7%</td><td>5.7%</td><td>6.3%</td></tr></table>

Cluster 1 contains groups that have a very high labor force attach ment and persistent employment status. On average 87% of individuals in segments assigned to cluster 1 are employed in both periods. The transition rates between E and U are in the middle of the range of UE and EU transition rates across the clusters, and the fraction of individuals who are unemployed in consecutive months is toward the low end of the range of average UU percentages. A key distinguishing feature that segments in this cluster have is a very low number of people out of the labor force, and also very low numbers of individuals transiting in and out of the labor force (i.e. cluster 1 has the lowest transition probabilities for NU, UN, EN, and NE). The labor force participation rate for individuals in cluster 1 is over 90%.

Cluster 2 is very similar to cluster 1, but less concentrated in the persistent employment state (EE). The fraction of individuals who are employed in both periods drops from 87% in cluster 1 to 71% in cluster 2. All of the other transition state percentages are higher in cluster 2. In particular, the fraction of individual who are out of the labor force in both periods (NN) rises from 4% in cluster 1 to 14% in cluster 2.

Clusters 3 and 5 contain cohorts of individuals who are least likely to spend time in unemployment. These cohorts have fewer individuals in the persistent employment state than clusters 1 and 2. They have the lowest transition percentages of all segments in the UE, EU, and UU states – only 1% of individuals in these groups are in the persistent unemployment state. These groups have a relatively high percentages for the persistent out-of-the-labor-force status, NN: 27% for cluster 3 and 43% for cluster 5.

Clusters 4 and 6 experience the highest transition rates between labor market states. Their percentages for persistent employment are somewhat less than their counterparts in clusters 3 and 5, but they are far less likely to be in the persistent NN state. These clusters are notable in that they have the highest transition rates for moving in and out of employment: EU, UE, EN, and NE, as well as having the highest transition probabilities for the persistent unemployment state.

![](/api/attachments/7MZKDGFN/fulltext/images/1fcaf1ebb402653458f92435bb53526a8e154fd55ecd134114bf30bd282bc630.jpg)  
Fig. 12. Pacman visualization.

Finally, cluster 7 contains cohorts comprised of individuals with the lower level of attachment to the labor force. The average percentage of persistent employment is only 23%, and transition rates to and from unemployment are relatively low. This cluster has the highest percen tages of being out of the labor force at 56%.

Lastly, we consider the case of combining multi-period data and clustering when time (categorical attribute T) is not one of the clustering dimensions. The Pacman chart provides the visual basis for this exploration. In our example analysis, we demonstrate how we can visualize the movement of the cohorts across diferent clusters and compare their respective trajectories.

The Pacman visualization in Fig. 12 shows the cluster placement of cohorts with a combination of demographic characteristics. From this visualization we derive several insights based on the colors in a given row, compare diferent rows, and identify outliers.

First, we examine the cohort attributes for each cluster. The purple cluster, cluster 1, which has the best employment outcomes consists of predominantly male, 25–54 (prime age) cohorts with at least high school education. We observe a few outliers in the second and fourth row representing female cohorts with bachelor degree. We note that the trend for male, 25–54, high-school cohorts changes around 2008 from cluster 1 to cluster 2, the blue cluster, with somewhat worse employment outcomes.

On the other end of the spectrum, the red cluster comprises all females 16–24, 55–64 (non prime age) who have less than a high school education. Again, we find some outliers. Younger men with less than a high-school degree transitioned to the red cluster in 2008, leaving a high unemployment cluster for a cluster with a much higher likelihood of being out of the labor force.

According to our clustering, at all levels of education, prime age males are found in the better purple or blue clusters. Those with a high school education only, however, transition in 2008 from the purple cluster to the blue cluster, which has lower percentages of continual employment. There are other groups which transition temporarily in the late 80s/early 90s: prime age women with a bachelor's degree move from blue to purple; prime age women with high school diplomas move from grey to blue; and young females with less than a high school degree move from red to orange. Because the red cluster has the highest proportion of people who are continually out of the labor force, we consider the occupants of this cluster as less firmly attached. The majority in this cluster are older and younger women with less education.

The intent of the examples presented here was to provide an illustration of our framework. There are many more detailed insights that can be revealed and analyzed based on these figures. We shared our findings and visualizations with the economists at the Federal Reserve Bank of Kansas City, and they have confirmed that the findings are accurate and the visualizations provide a quick and novel way of analyzing the CPS data in a way that significantly shortens certain types of analysis, while also bringing out previously unknown insights. A paper in the field of economics, based on these insights, is being developed, which will include a more comprehensive analysis of this example. Examples from other data sets and domains is part of the future research that we intend to engage in with various domain experts.

## 5. Conclusions

In this paper, we proposed an approach for analyzing data that combines data preparation, data visualization and clustering techniques in a novel way. This approach is outlined as a detailed two-phase framework. The first phase of the framework explores the large amount of sequential data in stages that can be undertaken iteratively. Those stages include data preparation, counting and value-based ordering, distribution visualization, and subsequence length determination, confirmation, and re-visualization. The second phase of the framework explores sequence diferences between data cohorts that are created using descriptive attributes, and visualizes the changes over time and diferent attribute values.

As an illustration of this approach, we analyzed labor market dynamics via descriptive modeling for the entire population as well as for segments of the population based on demographic characteristics. We first showed that considering individual employment status for two consecutive months provides better characterization of their employment situation than a single current employment status. We used the aggregate percentages of the 9 diferent two-month status sequences to assign a quantitative summary (9-dimensional vector) to diferent segments of the labor force in diferent years. We applied k-means clustering algorithm to the resulting set of 9-dimensional vectors and derived an optimal clustering of 7 clusters. We analyzed the cluster characteristics and the segment demographics within each cluster. Our findings show that the distribution of employment outcomes varies greatly over time and across demographic groups and that the compositions underlying the headline unemployment rates are vastly different even for the same values. The point of the research we presented here was to illustrate the analytical power of the proposed framework that utilizes visualization as an analytics tool and not just a presentation accessory. We chose a formally-maintained data set capturing an example dealing with employment and demographics. This particular domain was chosen because we assumed that most readers will have at least some rudimentary understanding of these issues. sufficient to follow the example as it illustrates the framework.

It is important to note the accessibility aspect of our framework, as it can be deployed relatively inexpensively using of-the shelf software. We were able to conduct our example using R and Tableau, both of which are widely available and in widespread use.

Our analytical approach combining data visualization with clustering for low-cardinality sequential data can be applied to a myriad of diferent scenarios and situations. However, if the sequential data is not inherently low-cardinality or the goal of the analysis is to derive a precise predictive model then our approach is not applicable. For example, predicting (precisely) the closing price of a stock given a sequence of previous quotes lies outside our proposed framework. Similarly, tracking and predicting the movement of objects based on the sequence of their previous positions is not an appropriate task for our framework. However, for the same datasets, our framework can handle diferent but related questions, such as finding similar stocks and grouping together objects based on their fluctuation patterns, as we will demonstrate in our future work.

The domain knowledge for every dataset will play a major role in their analysis but the framework with the prescribed stages and types of graphs and charts presented in this paper is the same.

## References

[1] S. LaValle, E. Lesser, R. Shockley, M.S. Hopkins, N. Kruschwitz, Big data, analytic

and the path from insights to value, MIT Sloan Management Review 52 (2) (2011) 21.

[2] R. Agrawal, A. Kadadi, X. Dai, F. Andres, Challenges and opportunities with big data visualization, Proceedings of the 7th International Conference on Management of Computational and Collective intElligence in Digital EcoSystems, ACM, 2015, pp. 169–173.

[3] E. Tufte, The Visual Display of Quantitative Information, Graphics Press, Cheshire, USA, 2001.

[4] S. Berinato, Visualizations that Really Work, Harvard Business Review, 2016, pp. 92–100 June.

[5] S. Liu, W. Cui, Y. Wu, M. Liu, A survey on information visualization: recent ad vances and challenges, The Visual Computer (12) (2014) 1373–1393.

[6] J. Tukey, Exploratory Data Analysis (Addison-Wesley Series in Behavioral Science), Addison-Wesley Pub, Reading, Mass, 1977.

[7] B. Franks, Taming the Big Data Tidal Wave, first ed., Wiley, 2012

[8] A. Bacic, A. Fadlalla, Business information visualization intellectual contributions: an integrative framework of visualization capabilities and dimensions of visual intelligence, Decision Support Systems 89 (2016) 77–86.

[9] S. Few, Show Me the Numbers: Designing Tables and Graphs to Enlighten, Analytics Press, 2012.

[10] P. Fox, J, Hendler, Changing the equation on scientific data visualization, Science no. 331 (2011), pp. 705–708.

[11] J.A. Schwabish, An economist's guide to visualizing data, Journal of Economi Perspectives 28 (2014) 209–234.

[12] H. Park, M.A. Bellamy, R. Basole, Visual analytics for supply network management: system design and evaluation, Decision Support Systems 91 (2016) 89–102.

[13] S. Oh. A hierarchical clustering algorithm for categorical sequence data. Information Processing Letters 91 (3) (2004) 135–140

[14] Y. Chen, Y. Hu, Constraint-based sequential pattern mining: the consideration of recency and compactness, Decision Support Systems 42 (2) (2006) 1203–1215.

[15] X. Liu, N. Xue, Y. Yuan, Aircraft engine sensor fault diagnostics using an on-line OBEM update method, PLoS One 12 (2) (2017) e0171037, , https://doi.org/10. 1371/journal.pone.0171037.

[16] N. Lesh, M. Zaki, M. Oglhara, Scalable feature mining for sequential data, IEEE Intelligent Systems and Their Applications 15 (2) (2000).

[17] O. Akbilgic, J.A. Howe, Symbolic pattern recognition for sequential data, Sequential Analysis 36 (4) (2017) 528–540, https://doi.org/10.1080/07474946.2017. 1394719.

[18] J. Moeyersoms, D. Martens, Including high-cardinality attributes in predictive models a case study in churn prediction in the energy sector, Decision Suppor Systems 72 (2015) 72–81.

[19] C. Perlich, F. Provost, Distribution-based aggregation for relational learning with identifier attributes, Machine Learning 62 (1–2) (2006) 65–105.

[20] W. Verbeke, K. Dejaeger, D. Martens, J. Hur, B. Baesens, New insights into churn prediction in the telecommunication sector: a profit driven data mining approach, European Journal of Operational Research 218 (1) (2012) 211–229

[21] N. Blaikie, Analyzing Quantitative Data: From Description to Explanation, Sage, 2003.

[22] B. Franks, The Analytics Revolution: How to Improve Your Business by Making Analytics Operational in the Big Data Era. Wilev. 2014.

[23] D.G. Murray. Tableau Your Data!: Fast and Easy Visual Analysis with Tableau Software, Wiley, 2013

[24] A. Unwin, Graphical Data Analysis with R. Chapman and Hall/CRC. 2015

[25] W. Martinez. A. Martinez, J. Solka. Exploratory Data Analysis with MATLAB Chapman and Hall/CRC. 2017.

[26] Christa Kelleher, Thorsten Wagener, Ten guidelines for efective data visualization in scientific publications. Environmental Modelling & Software 26 (6) (2011) 822–827.

[27] S. Few, Now you See it: Simple Visualization Techniques for Quantitative Analysis, Analytics Press, 2009.

[28] Harri Siirtola, Erkki Mäkinen, Constructing and reconstructing the reorderable matrix, Information Visualization 4 (1) (2005) 32–48. https://doi,org/10.1057 palgrave,ivs.9500086 March.

[29] Jefrey Heer, Ben Shneiderman, Interactive dynamics for visual analysis, Queue 10 (2) (2012) 30.

[30] Raphael Fuchs, Helwig Hauser, Visualization of multi – variate scientific data. Computer Graphics Forum, vol. 28, Wiley/Blackwell, 2009, pp. 1670–1690 no. 6. (10.1111).

[31] G. Shmueli, To explain or to predict? Statistical Science 25 (3) (2010) 289–310

[32] Encyclopedia of Survey Research Methods, Edited by: Paul J. Lavrakas, Accessed on 25.3.2019, DOI: https://doi.org/10.4135/9781412963947.n375

[33] M. Gavrilov, D. Anguelov, P. Indyk, R. Motwani, Mining the stock market: cluster discovery, Proc. Sixth ACM SIGKDD Int. Conf. Knowledge Discovery & Data Mining, 2000.

[34] Z. Cheng, B. Cule, B. Goethals, Pattern based sequence classification, IEEE Transactions on Knowledge and Data Engineering 28 (5) (2016). https://doi,org 10.1109/TKDE.2015.2510010

[35] G. A. Miller, The magical number seven, plus or minus two: some limits on our capacity for processing information, Psychological Review, 63(2) (1956) pp. 81–97. CiteSeerX 10.1.1.308.8071, doi:10.1037/h0043158.PMID 13310704

[36] G.Y. Bae, M. Olkkonen, S.R. Allred, J. Flombaum, J. I, Why some colors appear more memorable than others: a model combining categories and particulars in color working memory, Journal of Experimental Psychology: General 144 (4) (2015) 744–763.

[37] D. Borland, R. Taylor, Rainbow color map (still) considered harmful, IEEE Computer Graphics and Applications 27 (2) (2007). https://doi,org/10.1109/MCG

2007.323435.

[38] H. Levkowitz, Perceptual steps along color scales, International Journal of Imaging Systems and Technology 7 (2) (1996) 97–101.

[39] R. Bujack, T. Turton, F. Samsel, C. Ware, D. Rogers, J. Ahrens, The good, the bad, and the ugly: a theoretical framework for the assessment of continuous colormaps, IEEE Transactions on Visualization and Computer Graphics 24 (1) (2018), https:/ doi.org/10.1109/TVCG.2017.2743978.

[40] K.R. Sloan, C.M. Brown, Color map techniques, Computer Graphics, and Image Processing 10 (4) (1979) 297–317.

[41] C. Ware, Color sequences for univariate maps: theory, experiments and principles, IEEE Computer Graphics and Applications 8 (5) (1988) 41–49.

[42] S.M. Pizer, Intensity mappings to linearize display devices, Computer Graphics and Image Processing 17 (3) (1981) 262–268.

[43] J. Tajima, Uniform color scale applications to computer graphics, Computer Vision, Graphics, and Image Processing 21 (3) (1983) 305–325

[44] H. Levkowitz, G.T. Herman, The design and evaluation of color scales for image data, IEEE Computer Graphics and Applications 12 (1) (1992) 72–80.

[45] C. Ware, T.L. Turton, F. Samsel, D. Rogers, Evaluating the perceptual uniformity of color sequences for feature discrimination. Conference: EuroVis Workshop on Reproducibility, Verification, and Validation in Visualization (EuroRV3), The Eurographics Association, Barcelona, Spain, 2017, , https://doi.org/10.2312 eurorv3.20171107.

[46] W.K. Ching, E.S. Fung, M.K. Ng, Higher-order Markov chain models for categorical data sequences, Naval Research Logistics 51 (2004) 557–574.

[47] C. Weihs, K. Ickstadt, Data science: the impact of statistics, International Journal of Data Science and Analytics 6 (2018) 189–194.

[48] G. Das. K. Lin. H. Mannila, G. Renganathan. P. Smyth. Rule discovery from time series, KDD 98 (1) (1998) 16–22.

[49] S. Asmussen, Applied Probability and Queues, Springer Science & Business Media, 2003.

[50] P. Gagniuc, Markoy Chains: From Theory to Implementation and Experimentation John Wiley & Sons, Hoboken, NJ, 2017.

[51] C.M. Grinstead, J.L. Snell, Introduction to Probability, University Press of Florida, 2009.

[52] M.K. Evans, Practical Business Forecasting, John Wiley & Sons, 2002, pp. 264–265.

[53] A. Kumar, De-Bruijn sequence and application in graph theory, International Journal of Progressive Sciences and Technologies 3 (1) (2016) 4–17.

[54] K. Ord, R. Fildes, N. Kourentzes, Principles of Business Forecasting, Second edition Nelson Education, 2012, p. 161.

[55] A. Ralston. de Brujin sequences - a model example of the interaction of discrete mathematics and computer science, Mathematics Magazine 55 (1982) 131–143.

[56] J.L.E.K.S. Lonardi, P. Patel, Finding motifs in time series, Proc. of the 2nd Workshop on Temporal Data Mining, 2002, pp. 53–68.

[57] F.D. Reynolds, J. Neter, Age Classification, Marketing Science Institute, 1979.

[58] J.A. Hartigan, M.A. Wong, Algorithm AS 136: a k-means clustering algorithm, Journal of the Royal Statistical Society. Series C (Applied Statistics) 28 (1) (1979) 100–108.

[59] J.H. Ward, Hierarchical grouping to optimize an objective function, Journal of the American Statistical Association 58 (301) (1963) 236–244, https://doi.org/10. 2307/2282967 (JSTOR 228296Z. MR 0148188)

[60] C. Ordonez, E. Omiecinski, Accelerating EM clustering to find high-quality solutions, Knowledge and Information Systems 7 (2) (2005) 135–157 https://doi-org. flagship.luc.edu/10.1007/s10115-003-0141-6.

[61] M. Meilă, D. Heckerman, An experimental comparison of model-based clustering methods, Machine Learning 42 (1–2) (2001) 9–19 https://doi-org.flagship.luc.edu 10.1023/A:1007648401407.

[62] J.R. Marsden. D.E. Pingry. Numerical data quality in IS research and the implications for replication, Decision Support Systems 115 (2018) A1–A7.

[63] Current Population Survey (CPS), Basic monthly data at the NBER, National Bureau of Economic Research, http://nber.org/data/cps\_basic.html , Accessed date: 25 March 2019.

[64] B.J. Lougee, T. Morley, M. Watson, The Road to Cyberinfrastructure at the Federal Reserve Bank of Kansas City, Federal Reserve Bank of Kansas City, Technical Briefing, vol, 18(2). (2018).

[65] Section on Survey Research Methods – JSM, Overview of Current Population Survey Methodology Yang Cheng Demographic Statistical Methods Division U.S. Census Bureau1 Washington. D C 20233-0001 (2012) pp. 3966–3967

[66] Design and Methodology, Current Population Survey, Technical Paper 66, Accessed

on 25.3.2019, https://www.census.gov/prod/2006pubs/tp-66.pdf, (2006), pp. 3.1 – 3.15.

[67] P.J. Layrakas, Encyclopedia of Survey Research Methods, SAGE Publications, 2008.

[68] Handbook of Methods, US Bureau of Labor Statistics, Accessed on 25.3.2019, https://www.bls.gov/opub/hom/cps/pdf/cps.pdf, pp. 2–4.

[69] T.F. Kelly, The creation of longitudinal data from cross-section surveys: an illus tration from the current population survey, Annuls Of Economics And Social Measurement 2 (2) (1973) 209–214.

[70] H. Akaike, A new look at the statistical model identification, IEEE Transactions on Automatic Control 19 (6) (1974) 716–723, https://doi.org/10.1109/TAC.1974. 1100705.

[71] W.J. Krzanowski, Y.T. Lai, A criterion for determining the number of groups in a data set using sum-of-squares clustering, Biometrics (1988) 23–34.

[72] D. Ketchen, C. Shook, The application of cluster analysis in strategic management research: an analysis and critique, Strategic Management Journal 17 (6) (1996) 441–458.

[73] P.-N. Tan, M. Steinbach, V. Kumar, Introduction to Data Mining, Addison Wesley, 2005.

Svetlozar Nestorov is an Assistant Professor of Information Systems at the Quinlan School of Business at Loyola University Chicago. Previously he worked at the University of Chicago as a senior research associate at the Computation Institute, an assistant professor of computer science, and a leader of the data warehouse project at the Nielsen Data Center at the Kilts Center for Marketing at the Booth School of Business. He is a cofounder of Mobissimo, a venture-backed travel search engine that was chosen as one of the 50 coolest Web sites by Time magazine in 2004. His research interests include dat visualization, data mining, high-performance computing, and Web technologies. His work has been published in a number of management information systems and computer science academic journals, conference publications, and books.

Boris Jukić is a Professor of Information Systems and the Director of the Master Program in Data Analytics at Clarkson University Reh School of Business. Previously he was also an Associate Dean of Graduate Programs at Reh Clarkson University School of Business. H conducts research in various information technology related areas including e-business, data visualization, data warehousing, data analytics, computing resource pricing and management, process and applications modeling as well as IT strategy. His work has been published in a number of management information systems and computer science academic journals, conference publications, and books.

Nenad Jukić is a Professor of Information Systems and the Director of Master of Science in Information Systems Management Program at the Quinlan School of Business at Loyola University Chicago. He conducts research in various information management-related areas, including database modeling and management, data visualization, data warehousing, business intelligence, data mining, business analytics, big data, e-business, and IT strategy. His work has been published in numerous information systems and computer science academic journals, conference publications, and books. In addition to his academic work, he provides expertise to database, data warehousing and big data projects for corporations and organizations that vary from startups to Fortune 500 companies and U.S. government agencies.

Abhishek Sharma is a database/business intelligence consultant and the founder of an IT consulting company, Awishkar, Inc. He is also a Clinical Professor of Information Systems at the Quinlan School of Business at Loyola University Chicago. He has worked at various information technology positions in fields such as information management, banking/ quantitative finance and instrumentation, process control, and statistical analysis in manufacturing environment. Parallel with his consulting work and teaching, he conducts research in a variety of fields, including database modeling and management, data vi sualization, data warehousing, business intelligence, data mining, very large databases (VLDBs)/big data, and IT strategy.

Sippo Rossi is a master's student specializing in information and service management at the Aalto University School of Business in Finland. As a research assistant. he has participated in research projects in a variety of fields, including database modeling and management, data visualization, business intelligence and information systems education. Alongside his studies and his academic work, he has worked in management con sulting as an analyst at Deloitte.
