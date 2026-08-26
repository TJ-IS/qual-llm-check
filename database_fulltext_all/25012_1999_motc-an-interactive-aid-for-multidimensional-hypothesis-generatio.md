---
otero_id: 25012
otero_key: "AJWRKNPC"
title: "MOTC: An Interactive Aid for Multidimensional Hypothesis Generatio"
authors: "Krishnamohan Balachandran; Jan Buzydlowski; Garett Dworman; Steven O. Kimbrough; Tate Shafer; William J. Vachula"
year: "1999"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1999.11518232"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# MOTC: An Interactive Aid for Multidimensional Hypothesis Generatio

Krishnamohan Balachandran, Jan Buzydlowski, Garett Dworman, Steven O. Kimbrough, Tate Shafer & William J. Vachula

To cite this article: Krishnamohan Balachandran, Jan Buzydlowski, Garett Dworman, Steven O. Kimbrough, Tate Shafer & William J. Vachula (1999) MOTC: An Interactive Aid for Multidimensional Hypothesis Generatio, Journal of Management Information Systems, 16:1, 17-36, DOI: 10.1080/07421222.1999.11518232

To link to this article: http://dx.doi.org/10.1080/07421222.1999.11518232

![](/api/attachments/AJWRKNPC/fulltext/images/f077be5440131fa18c18b2f2b140043affcca217aefe530d974cca69000cfdc3.jpg)

Published online: 02 Dec 2015.

![](/api/attachments/AJWRKNPC/fulltext/images/84ce31d8a33b3cfb5a5498e5bf3e5b8090deb59f3bc44286c5377cf4f1957b0b.jpg)

Submit your article to this journal ↗

![](/api/attachments/AJWRKNPC/fulltext/images/01a63fc880b4eeb83a65a43eb6d50f094cecc07a4e82b4287c5405e17d6911b1.jpg)

View related articles ↗

# MOTC: An Interactive Aid for Multidimensional Hypothesis Generation

KRISHNAMOHAN BALACHANDRAN, JAN BUZYDLOWSKI, GARETT DWORMAN, STEVEN O. KIMBROUGH, TATE SHAFER, AND WILLIAM J. VACHULA

KRISHNAMOHAN BALACHANDRAN is a Ph.D. candidate at the Operations and Information Management department of the Wharton School of the University of Pennsylvania. He received a B.Tech. from the Indian Institute of Technology, Bombay, in 1993 and an M.S. from the Systems Engineering department of the University of Pennsylvania in 1995. His current research interests are benchmarking, consumer behavior, and data-mining applications related to these fields.

JAN BUZYDLOWSKI holds a bachelor's degree in mathematics, and master's degrees in statistics and computer science. His interests are in data storage and analysis as well as object technologies. His current research is in data scrubbing and object-oriented data warehouse design. He has taught for fifteen years and worked as a statistician for five years. He is currently finishing his Ph.D. in information systems at Drexel University.

GARETT DWORMAN is a Ph.D. candidate in the Department of Operations and Information Management at the Wharton School of the University of Pennsylvania. The main theme of his research is the design of cognitively motivated information access systems. For his dissertation he is developing pattern-oriented systems for accessing document collections. This technology is currently being applied to collections in museums and in the health-care industry.

STEVEN O. KIMBROUGH is a Professor at the Wharton School of the University of Pennsylvania. He received his Ph.D. in philosophy from the University of Wisconsin. His main research interests are electronic commerce, decision support and expert systems, logic modeling, and computational rationality. His active research areas include computational approaches to belief revision and nonmonotonic reasoning, formal languages for business communication, evolutionary computation (including genetic algorithms and genetic programming), and context-based information retrieval. He is currently co-Principal Investigator of the Logistics DSS project, which is part of DARPA's Advanced Logistics Program.

TATE SHAFER has a B.S. from the Wharton School of the University of Pennsylvania, where he studied information systems and finance. He served as an undergraduate research assistant to Steven O. Kimbrough and researched various IS fields, including computer programming, artificial intelligence, and information retrieval. He served for three semesters as a teaching assistant for the introductory information systems course at the Wharton School. He is a strategy consultant for Oliver, Wyman & Co.

WILLIAM J. VACHULA is currently a Ph.D. candidate in the Operation and Information Management department at the Wharton School of the University of Pennsylvania. He received a B.S.E.E. from Carnegie-Mellon University in 1983 and an M.S.E.E. from the University of Pennsylvania in 1989. His industry experience includes software and systems engineering, project and program management, and information systems consulting. His research interests include various application domains for software agents, computational economics techniques, and advanced systems analysis and design processes.

ABSTRACT: The paper reports on conceptual development in the areas of database mining and knowledge discovery in databases (KDD). Our efforts have also led to a prototype implementation, called MOTC, for exploring hypothesis space in large and complex data sets. Our KDD conceptual development rests on two main principles. First, we use the crosstab representation for working with qualitative data. This is by now standard in on-line analytical processing (OLAP) applications, and we reaffirm it with additional reasons. Second, and innovatively, we use prediction analysis as a measure of goodness for hypotheses. Prediction analysis is an established statistical technique for analysis of associations among qualitative variables. It generalizes and subsumes a large number of other such measures of association, depending on specific assumptions the user is willing to make. As such, it provides a very useful framework for exploring hypothesis space in a KDD context. The paper illustrates these points with an extensive discussion of MOTC.

KEY WORDS AND PHRASES: data mining, data visualization, hypotheses exploration, knowledge discovery in databases, OLAP, prediction analysis.

IT STANDS TO REASON THAT EXISTING DATABASES are underexploited. Organizational databases are typically created to record and facilitate business transactions. These databases often contain valuable information that fails to be recognized and used by the organizations that own and maintain them. Such, at least, is a widespread belief. This has led to a burgeoning industry of research papers, startup firms, and professional seminars focusing on what has come to be called KDD, the acronym for knowledge discovery in databases (see $[10]$ for a recent collection of representative papers). Real money is being bet that valuable knowledge is there to be discovered and that software innovations will help discover and exploit this knowledge economically.

We share the widespread belief in the efficacy, or at least potential, of KDD, and are exploring a concept that—we believe—addresses a central problem in KDD, namely, hypothesis generation. In what follows we describe our concept and our implementation in a prototype system called MOTC. First, however, we offer some comments to set the context.

The premise of KDD is that software innovations can materially contribute to more effective exploitation of databases. But just how can KDD software do this, and what is its relation to standard statistical methods? Put bluntly, here is a question we have heard posed by many statisticians and statistically trained practitioners: What does KDD have to offer that is not done well already by multiple regression techniques?

Put briefly, the answer is “plenty.” Standard statistical methods, including regression analysis, are hypothesis testing methods. For example, what regression analysis does is accept a functional form for a model/hypothesis and then find the “best” instance of a model/hypothesis of that form. Even if we were to grant that computational—for example, KDD or AI—approaches could never improve on this basic statistical task, much remains to be done—and to be researched in the interests of effective KDD.

Examples of “nonstatistical” issues in KDD include:

1. Data cleaning: What can be done to locate and ameliorate the pervasive problems of invalid or incomplete data?

2. “First cut” analysis: What can be done to automatically provide an initial assessment of the patterns and potentially useful or interesting knowledge in a database? The aim here is, realistically, to automate some of the basic work that is now done by skilled human analysts.

3. Hypothesis generation: What can be done to support, or even automate, the finding of plausible hypotheses in the data? Found hypotheses would, of course, need to be tested subsequently with statistical techniques, but where do you get “the contenders” in the first place?

Our attention, and the research results reported in this paper, have focused on the hypothesis generation problem for KDD. Because hypothesis space is generally quite large (more on this below), it is normally impossible to enumerate and investigate all the potentially interesting hypotheses. Heuristics are necessary and, it would seem, a decision support philosophy is called for. What, then, are the main requirements, or desired features, of a decision support tool for investigating hypothesis space? We identify the following as among the principal requirements. Such a tool should:

1. Support users in hypothesizing relationships and patterns among the variables in the data at hand (we call this hypothesis hunting).

2. Provide users with some indication of the validity, accuracy, and specificity of various hypotheses (hypothesis evaluation).

3. Provide effective visualizations for hypotheses so that the powers of human visual processing can be exploited for exploring hypothesis space.

4. Support automated exploration of hypothesis space, with feedback and indicators for interactive (human-driven) exploration.

5. Support all of the above for data sets and hypotheses of reasonably high dimensionality, say, between 4 and 200 dimensions, as well on large data sets (e.g., with millions of records).

## What is needed, conceptually, to build such a tool?

1. A general concept or representation for data, hypotheses, and hypothesis space. This representation need not be universal but should be broadly applicable. We call this the hypothesis representation.

2. Given a hypothesis representation, we also need an indicator of quality for the hypothesis in question. We call this the measure of goodness.

3. The hypothesis representation and the measure of goodness should fit with, cohere with, the requirements (and implicit goals, described above) of a DSS for exploring hypothesis space.

## Hypothesis Representation

THERE ARE THREE MAIN ELEMENTS TO OUR HYPOTHESIS representation concept:

1. Focus on qualitative data.

2. Use the crosstab (also known as data cube, multidimensional data, and or cross-classifications of multivariate data) form for data (rather than, say, the relational form as in relational databases).

3. Represent hypotheses by identifying error values in the cells of the multidimensional (crosstab) data form.

These aspects of the concept, and why we have them, are perhaps best understood through a specific example. $^{1}$ Suppose we have data on two variables: $X_{1}$ party affiliation, and $X_{2}$ , support for an increased government role in social services. $X_{1}$ can take on the following values: Dem, Ind, and Rep (Democrat, Independent, and Republican). $X_{2}$ can have any of following values: left, left-center, center, right-center, right. Suppose we have the observations of the two variables taken together, as shown in Table 1. $^{2}$

## Focus on Qualitative Data

The variables $X_{1}$ and $X_{2}$ in Table 1 are qualitative (that is, categorical) because they take on discrete values (three such values in the case of $X_{1}$ and five for $X_{2}$ ). $X_{1}$ is arguably a nominal variable because there is no compelling natural ordering for its three values. $^{3}$ Dem, for example, is neither more nor less than Ind. Similarly, in a business database, Sales-Region and Division are nominal because, for example, Mid-Atlantic is neither more nor less than New England, and Marketing is neither more nor less than Manufacturing. $X_{2}$ , on the other hand, is an ordinal variable because there is a natural ordering for the values it takes on: left, left-center, center, and so on. Similarly, in a business database, Quarter (first, second, third, fourth) is naturally ordered and therefore ordinal. If a variable, such as Sales, is quantitative, then (for our framework) it will have to be quantized, or binned. Thus, for example, Sales ( $V_{2}$ ) might be binned as follows into five categories or bins (that is, forms [20]): $^{4}$

$$
V _ {2} ^ {1} [ 0 - 2 0, 0 0 0)
$$

$$
V _ {2} ^ {2} [ 2 0, 0 0 0 - 4 0, 0 0 0)
$$

$$
V _ {2} ^ {3} [ 4 0, 0 0 0 - 6 0, 0 0 0)
$$

$$
V _ {2} ^ {A} [ 6 0, 0 0 0 - 8 0, 0 0 0)
$$

$$
V _ {2} ^ {5} [ 8 0, 0 0 0 + ].
$$

Table 1. Party Affiliation and Support for Social Services by Top-Level Bureaucrats in Social Service Agencies

<table><tr><td rowspan="2">Support</td><td colspan="4">Party affiliation</td></tr><tr><td>Dem</td><td>Ind</td><td>Rep</td><td></td></tr><tr><td>Left</td><td>12</td><td>3</td><td>1</td><td>16</td></tr><tr><td>Left-center</td><td>1</td><td>2</td><td>2</td><td>5</td></tr><tr><td>Center</td><td>0</td><td>3</td><td>4</td><td>7</td></tr><tr><td>Right-center</td><td>0</td><td>1</td><td>1</td><td>2</td></tr><tr><td>Right</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td></td><td>13</td><td>9</td><td>9</td><td>31</td></tr></table>

By way of justification for this assumed focus, we note the following: (1) Many variables, perhaps the majority, occurring in business databases are naturally qualitative; (2) a general framework, including both qualitative and quantitative variables, is highly desirable; (3) with felicitous binning, quantitative variables can typically be represented qualitatively to a degree of accuracy sufficient for exploratory purposes; and (4) transformation of inherently qualitative variables to a quantitative scale is inherently arbitrary and known to induce results sensitive to the transformation imposed.

## Use the Crosstab Form for Data

This aspect of our focus requires less explanation and justification, since it is also standard practice in OLAP (on-line analytical processing) applications (see $[16, p. 179]$ on “the ‘cube’ foundation for multidimension DBMS datamarts,” $[8, p. 45]$ on “hypercube data representations,” $[27]$ and $[7]$ on “cubes”). Our reasons for using the crosstab form for data representation are simple and essentially identical to why it is now used so widely in OLAP applications (and has long been essential in statistics): The crosstab form easily accommodates qualitative variables and (most importantly) it has been demonstrated to be a natural representation for the sorts of reports and hypotheses in which users—managers and scientists—typically are interested. $^{5}$ (See also the literature on information visualization. For a review, see $[21]$ .)

## Represent Hypotheses by Identifying Error Values in the Cells of the Multidimensional Data Form

Recalling our example data, in Table 1, suppose that an investigator has the bureaucrat's support for increased social services. Following the notation of [14, 15], we use the statement $x \to y$ to mean, roughly, "if $x$ then predict $y$ " or " $x$ tends to be a sufficient condition for $y$ . $^{6}$ Suppose our investigator's hypothesis, or prediction (call it $P_1$ ), is that Democrats tend to be left or left-center, Independents tend to be at the center, and Republicans tend to be center, right-center, or right. Equivalently, but more compactly, we can say:

Table 2. Error-Cell Representation for the Hypothesis, or Prediction, $P_{1}$

<table><tr><td>Support</td><td colspan="3">Party affiliation</td></tr><tr><td></td><td>Dem</td><td>Ind</td><td>Rep</td></tr><tr><td>Left</td><td>0</td><td>1</td><td>1</td></tr><tr><td>Left-center</td><td>0</td><td>1</td><td>1</td></tr><tr><td>Center</td><td>1</td><td>0</td><td>0</td></tr><tr><td>Right-center</td><td>1</td><td>1</td><td>0</td></tr><tr><td>Right</td><td>1</td><td>1</td><td>0</td></tr></table>

P1: Dem → (left or left-center) and Ind → center and Rep → (center or right-center or right).

Equivalently, and in tabular form, we can label cells in the crosstab representation as either predicted by $P_{1}$ , in which case they receive an error value of 0, or as not predicated by $P_{1}$ , in which case they receive an error value of 1. Table 2 presents $P_{1}$ in this form.

Given that the data are to be presented in crosstab form, the error-cell representation for hypotheses is natural and, we think, quite elegant. Note as well two things. First, we can now give an operational characterization of hypotheses space. If the number of cells in a crosstab representation is C and the number of possible error values (two in Table 2: 0 for no error and 1 for error) is n, then the number of possible hypotheses is $(n^{C}-n)$ . (We subtract n to eliminate the cases in which all cells have the same error value. Presumably, these cannot be interesting predictions.) Thus, even for our little example, $P_{1}$ is just one of $2^{15}-2 = 32{,}766$ possible hypotheses for predicting and explaining these data. Second, as implied in our first comment just given, it is possible to use more than two (0 or 1) error-cell values. Perhaps observations falling in certain cells are intermediate and should have an error value of, say, 0.5. There is nothing in these representation or in prediction analysis (see the next section) that prevents this sort of generalization.

## Prediction Analysis

PUT BRIEFLY, PREDICTION ANALYSIS [14, 15] IS A WELL-ESTABLISHED technique that uses the crosstab and error-cell representations of data and predictions and also provides a measure of goodness for a prediction (on the given data). We can describe only the basic elements of prediction analysis here; much more thorough treatment is available in the open literature. What we find especially intriguing about prediction analysis—besides its intuitiveness and its fit with our preferred data representations—are two things: First, it has been shown to subsume most, if not all, standard measures of association for qualitative data, such as Cohen's Kappa, Kendall's $\tau$ , and Goodman and Kruskal's gamma (see [14, 15] for details). Second, prediction analysis was originally motivated to evaluate predictions ex ante, for example, on the basis of prior theory, But it also can be used ex post to select propositions from the data, in which case it is, as one would expect, asymptotically $\chi^{2}$ . Used ex post, prediction analysis is good for finding the “contenders,” hypotheses that merit careful scientific investigation using standard statistical techniques.

The principal measure of hypothesis value in prediction analysis is $\nabla$ (pronounced “dell,” which is defined as follows:

$$
\nabla = 1 - \frac {\text { observed   error }}{\text { expected   error }}.\tag{1}
$$

Let $n_{ij}$ be the number of observations in cell row i, column j, and $w_{ij}$ be the error value for the cell in row i, column j. (Again, although we are holding the discussion in terms of a two-dimensional example, all of this generalizes in a straightforward way.) Then, we may define the observed error for a particular prediction (error-cell table) as

(2)

$$
\text { observed   error } = \sum_ {i = 1} ^ {R} \sum_ {j = 1} ^ {C} w _ {i j} \cdot n _ {i j}
$$

where the number of forms in the row variable is R and the number of forms in the column variable is C.

Finally, the expected error formula is

(3)

$$
\text { expected   error } = \sum_ {i = 1} ^ {R} \sum_ {j = 1} ^ {C} w _ {i j} \cdot n _ {i \bullet} \cdot n _ {\bullet j} / n,
$$

where

$n_{i\bullet}=$ the number of observations in category i of the first (row) variable.

$n_{\cdot j} =$ the number of observations in category $j$ of the second (column) variable.

$n =$ the total number of observations.

That is, $n_{*i}$ and $n_{j*}$ are the row and column marginals, which are presented in Table 1. Note as well:

1. If the observed error equals 0, then $\nabla$ is 1. This is the highest possible value for $\nabla$ .

2. If the observed error equals the expected error, then $\nabla$ is 0. This indicates, roughly, a prediction no better than chance, rather like a correlation of 0. (But remember: standard correlation coefficients apply to real numbers, quantitative variables, not qualitative variables.)

3. $\nabla$ may be negative, arbitrarily so. A negative value is like a negative correlation, but may go lower than -1.

4. In general, a higher $\nabla$ indicates a better prediction, but this neglects considerations of parsimony. After all, if all the error cells are set to 0, then $\nabla$ will equal 1. $^{7}$ Prediction analysis uses what it calls the precision, which is the expected error rate for a prediction, P. Precision in this sense is called U and is defined as

$$
U = \sum_ {i = 1} ^ {R} \sum_ {j = 1} ^ {C} w _ {i j} \cdot n _ {i \bullet} \cdot n _ {\bullet j} / (n \cdot n).\tag{4}
$$

Note that if $w_{ij} = 1$ for all $i, j$ (i.e., everything is an error), then $U = 1$ .

5. In finding good hypotheses, we seek to maximize $\nabla$ . We might think of maximizing $\nabla$ and U jointly, as in $\alpha \cdot U$ or in $\nabla \cdot U$ ; or we might think of U as a constraint on this maximization problem. We might also think of imposing other constraints, such as “naturalness” conditions. For example, in the error cell representation, one might require that there should be no gaps in columns between error and nonerror cells. But this is a topic beyond the scope of the present paper. For present purposes, we rely on the user’s judgment to impose reasonableness criteria on hypotheses explored.

## MOTC: A DSS for Exploring Hypothesis Space

MOTC IS A PROTOTYPE IMPLEMENTATION OF A DSS for exploring hypothesis space. It assumes the two main frameworks we have just discussed (crosstabulation of qualitative data for hypothesis representation, and prediction analysis for a measure of goodness for hypotheses), and it meets, or at least addresses, the main requirements we identified above for such a DSS. MOTC is implemented in Visual Basic 5 and Microsoft Access, and runs in a Windows NT environment.

The central dominating metaphor in MOTC is the representation of variables (dimensions) as binned bars. A single bar corresponds to a single variable. Bars are arrayed horizontally and are divided by vertical lines indicating bins. Each bin corresponds to a category for the variable in question. Thus, in our previous example the bar for Party Affiliation would have three bins, while the bar for support would have five bins. A user may right-click on a bar and MOTC will present information about the underlying binning arrangement. See the figures below for illustrations. The width of a bin as displayed represents the percentage of records in the relevant data set that have values falling into the bin in question. Wider bins indicate proportionately larger numbers of records. MOTC as presently implemented allows up to eight variables to be represented as bars on the display. A bar may have any number of bins. This is in fact an interesting and nontrivial degree of multidimensionality (also see our later discussion of the focus+context technique used by Rao and Card in their Table Lens program [32]).

MOTC as currently implemented has two modes of operation: hypothesis-hunting (that is, brush) mode, and hypothesis evaluation (that is, prediction) mode. In hypothesis-hunting mode, users use brushing with the mouse to display relationships among variables. Users choose particular bins and brush them with a chosen color by clicking on them. MOTC responds by applying the same color to bins associated with other variables. For example, if the user brushes bin 3 of variable 1 with purple, MOTC might respond by covering 25 percent of bin 2 of variable 4 in purple, indicating thereby that 25 percent of the records associated with bin 2 of variable 4 also are associated with bin 3 of variable 1. (See the various figures, below, for illustrations.) A user may brush more than one bin with a single color, either within or without a single variable. The effect is a logical “or” for bins within a single variable (bar) and an “and” for bins in different variables. Further, suppose purple is used to brush bins 1 and 2 of variable X, bins 4 and 5 of variable Y, and bins 7 and 8 of variable Z. Suppose further that we are in prediction mode (see below) and that we want X and Y to predict Z. Then, the equivalent representation in prediction analysis terminology is:

$$
((X _ {1} \lor X _ {2}) \land (Y _ {4} \lor Y _ {5})) \rightarrow (Z _ {7} \lor Z _ {8}).
$$

MOTC presently supports up to five colors for brushing. Each color used corresponds to a separate $\rightarrow$ rule in terms of prediction analysis. Working in brush mode, the user explores hypothesis space, with MOTC providing feedback by coloring bins in the unbrushed bars (predicted variables). The user thus gets a rough idea of where the “big hits” in the predictions lie.

In hypothesis evaluation, or prediction, mode, the user brushes—clicks and colors—bins in the predictor and predicted variable bars. In essence, the user is interactively populating a higher-dimensional version (up to eight dimensions in the current implementation) of an error-cell table, as in Table 2. Doing so specifies a hypothesis, and MOTC responds by calculating and displaying $\nabla$ and U for the hypothesis.

Working iteratively, the user may explore hypothesis space by switching back and forth between hypothesis-hunting mode and hypothesis evaluation mode. This continues until the user reaches reflective equilibrium.

## A Sketch of MOTC at Work

OUR PURPOSE IN THIS SECTION IS TO GIVE THE READER a sense of what it is like to work with MOTC to explore a collection of data. We shall work with a hypothetical, rather abstract example and use drawings, rather than original screen dumps, in our illustrations. We do this for several reasons. Most importantly, our aim is to communicate the essential concepts associated with MOTC. We want to discuss the forest, rather than the trees. Screen dumps from, and descriptions of, MOTC are available in considerable detail elsewhere, including the open literature $[1, 2]$ , as well as Web sites (http://grace.wharton.upenn.edu/\~sok/motc and http://www.practicalreasoning.com/motc). Here, our aim is to communicate in as brief a manner as possible the core ideas of how MOTC works from a user's perspective.

A user's interaction with MOTC begins with the data, which must be stored in a Microsoft Access database and must reside in a single table or query. $^{9}$ Once such a table or query exists, the user may launch MOTC, open the appropriate Access database, and select for investigation the particular table or query of interest.

Once the user identifies the data source (table or query), MOTC presents the user with a list of attribute names (from the database) for the data source. The user selects up to eight attributes to explore. $^{10}$ For each attribute or dimension, the user must also make decisions about binning the data. MOTC will guess whether the data for a given attribute are continuous (e.g., sales in dollars) or discrete (e.g., sales regions). The user must either override or confirm this guess. MOTC will then guess how best to categorize, or bin, the data. Again, the user may override the guess and indicate how MOTC should bin the data by dimension. (On binning, see our discussion above.)

Once these decisions are taken, MOTC presents the user with a display showing each attribute as a horizontal bar, with vertical lines indicating bins. In figure 1, which is a drawn schematic of the real program, we see that there are four attributes under joint consideration. These are labeled A, B, C, and D. Attributes A and D are each binned into three categories (1, 2, and 3; call them low, medium, and high), while attributes B and C each have four bins. (The number of bins in MOTC is open-ended, but it seldom is useful to have more than 8 or 10.)

At this point, MOTC is by default in brush (or hypothesis-finding) mode. The user would select a color (MOTC supports up to five colors) and begin to explore by “brushing” a bin on an attribute. Here, we will use shading and patterns instead of colors. Figure 2 shows a notional display in which the user has selected the horizontal line pattern and brushed the leftmost (1, or “low”) bin on attribute A.

MOTC has responded by shading bins in the other three attributes. $^{[11]}$ These MOTC shadings should be interpreted as histograms. Remember that every observation fits into some (exactly one) bin on each dimension. Recalling our party affiliation example, if you are left-center, then there is some party affiliation that you have. MOTC is for discovering interesting patterns in the distribution of observations across bins. What MOTC is telling us here is that, if an observation is from bin 1 (leftmost bin) of attribute A, then it will tend to be in bins 3 or 4 of attribute B, bins 1 or 2 of attribute C, and bin 2 of attribute D. This would appear to be a significant, or at least interesting, pattern. How good is this as a hypothesis? How well does it predict?

At this point, the user is in position to state a hypothesis and have MOTC calculate its dell and precision values, from prediction analysis. The user then switches to prediction mode, chooses a color (pattern), and clicks on the bins corresponding to the hypothesis.

In figure 3, the user has clicked on bin 1 of attribute A, bins 3 and 4 of attribute B, bins 1 and 2 of attribute C, and bin 2 of attribute D. Notice that the shading completely fills each selected bin. What this display is indicating to MOTC is the error-cell representation for the hypothesis. From this display, MOTC constructs the analog of Table 2, calculates $\nabla$ and U (dell and precision), and displays them for the user. The user is then free to continue exploring other hypotheses.

In the case at hand, it is likely that $\nabla$ would be reasonably high (which is good), but that U (precision) would be fairly low (which is bad). Typically, the user will want to explore more complete hypotheses (what if the observation is in bin 2 of A?). The end result of this kind of exploration might produce a complete hypothesis, as in figure 4. $^{12}$ With such a hypothesis expressed, MOTC would then calculate $\nabla$ and U (dell and precision), and display them for the user.

![](/api/attachments/AJWRKNPC/fulltext/images/8265564baea9663cdf1b25295fb9cf74ca1e88aa547ccc2bc79a4ad72a16ebd1.jpg)

A  
![](/api/attachments/AJWRKNPC/fulltext/images/240e9520fcf69c8499d471cd43868cc24f627812c3e86ce4c587278132c33538.jpg)

![](/api/attachments/AJWRKNPC/fulltext/images/318a4ca046326c080044768fcdcdfb09f6fe61ef4196ba14b9a68ccc664908ed.jpg)

C  
![](/api/attachments/AJWRKNPC/fulltext/images/9390ad8f25ff2b2b937b1947b0bda7e43fe2a67f4a280f114e3a8d5608bf21d1.jpg)

D  
![](/api/attachments/AJWRKNPC/fulltext/images/a2770efa4ce1d137712acff21fb10dca2c1ae627aa73fc0beb79fde9113518a8.jpg)  
Figure 1. Binned, Four-Dimensional Data Set Ready for Exploration in MOTC

A  
B  
![](/api/attachments/AJWRKNPC/fulltext/images/c918197133cbf2279ddacc1be9339189bdbe0c37b3b551815d6bd7715631c8de.jpg)

C  
![](/api/attachments/AJWRKNPC/fulltext/images/08a5857e382b0d65b3d54d35c24d945464711ab2fb1983df022966d119bd1bfd.jpg)

D  
Figure 2. MOTC in Hypothesis Generation Mode  
![](/api/attachments/AJWRKNPC/fulltext/images/001859a8bed94ce80ade03b5bf41fe327192393b3d294ffbf27639112b628f96.jpg)

![](/api/attachments/AJWRKNPC/fulltext/images/f68e5160ad5c050ce1f3a60010bc77511bf6edb71907463e76200da74c1bea62.jpg)

![](/api/attachments/AJWRKNPC/fulltext/images/d3ce2a67465bd3cbf638ba6f4073ef70606738a058d3855201ce08ab50f56cd6.jpg)

![](/api/attachments/AJWRKNPC/fulltext/images/4c4a793b187fa07dd4209261f465bd78c33828620a0f50594c403445669ef4cc.jpg)

![](/api/attachments/AJWRKNPC/fulltext/images/e1abf033f835a8e773ef1bd8171283a0e38d2169bc3311e1933e2a42f13a4078.jpg)  
Figure 3. MOTC in Prediction Mode

![](/api/attachments/AJWRKNPC/fulltext/images/159d786b5e6caacd9ef34225f2168f4408c3d8b3d2c777197fb151a4e99fcfa8.jpg)

![](/api/attachments/AJWRKNPC/fulltext/images/70c70bc3dd7b1e45b078a29f2a9a46285b1e2365a65b771d8c23c73a7e67396d.jpg)

![](/api/attachments/AJWRKNPC/fulltext/images/3667fea9db0681185665acd3cc60735a95af090af43f2586decbeed560f34b38.jpg)

![](/api/attachments/AJWRKNPC/fulltext/images/5f5695c82613ebc5a65fcefd57a8bf5488fefdc9a65e05d605c6c532dcde17ab.jpg)  
Figure 4. MOTC with a Complete Prediction on the Data

And the user, as we have said, can continue exploring in this manner until he or she reaches reflective equilibrium.

## Comparison with Alternatives

MOTC, AS WE HAVE SEEN, ASSUMES TWO MAIN FRAMEWORKS (the crosstabulation form for representing hypotheses, and prediction analysis for measuring goodness of hypotheses), and provides an interactive environment of some promise for discovering interesting hypotheses. Here we want to consider how MOTC, or the ideas it embodies, compares with what has appeared in the relevant literature? Two points first: (1) MOTC is nearly unique, or at least unusual, among database-mining tools in using the crosstabulation form, $^{13}$ and (2) MOTC is unique in being an end-user interactive tool for supporting prediction analysis. For these reasons, we are less concerned here with establishing originality and more focused on placing MOTC within the nexus of data-visualization techniques. This serves the purposes of better understanding what MOTC is about and of pointing toward future research.

## Design Goals of the MOTC Interface

If we step back and look at the larger picture, the purpose of MOTC is to help the user discover interesting patterns in data and to provide an evaluation of the predictive value of those patterns. To this end, we identified three main desiderata for MOTC's interface design:

1. Present a display that can represent a very large number of records. The simple fact is that modern databases are huge and we need tools for dealing with them. Of course, for purposes of pattern discovery it is always possible—even desirable—to sample from the underlying data. Even so, having the option of examining larger datasets is always a good thing, since patterns evident in large datasets may not be apparent in smaller sample sets.

2. Effectively display a large number of variables. It is also a simple or brute fact that modern databases present large numbers of dimensions, or fields, among which users have an interest in discovering patterns. To limit a user's view of the data to only a subset of the data's variables is a severe restriction on the user's ability to discover patterns. Unfortunately, too many variables (dimensions) in a display can quickly overwhelm a user's cognitive resources. Therefore, a second goal of MOTC's interface is to maximize the number of displayed dimensions without overwhelming the user.

3. Provide for visualization that helps users discover associations among variables. Passively displaying information only goes so far in helping users discover patterns in the data. To be a truly effective interface, the display must actively highlight associations among variables in the data by providing users with feedback about the quality of the apparent associations.

These are general goals that have attracted study outside the context of MOTC. We now briefly review and discuss this literature.

## Present a Display That Can Represent a Very Large Number of Records

It is generally accepted that people process visual information more easily than textual or numerical information. “Scanning a thousand tiny bars with your eyes requires hardly any conscious effort, unlike reading a thousand numbers, which takes a great deal of mental energy and time” [31]. Information-visualization techniques can take advantage of this by displaying enormous amounts of information on the screen. For example, the SeeSoft system effectively displays over 15,000 lines of code on the screen [9] by representing code with pixel-thin liens that reflect the code’s visual outline. InXight’s “wide widgets” [31] are visual components that can be incorporated into a GUI information system to display several orders of magnitude more data than traditional display tools (e.g., spreadsheets or hierarchical trees). Wide widgets are focus+context interfaces [12, 35] that dynamically distort spatial layouts so that users can zoom in on several records or variables while the rest of the records shrink to fit within the remaining space. In this way, users can focus on several items without losing the context provided by the remaining items. One wide widget, the Table Lens, has been demonstrated with a table of baseball statistics containing 323 rows by 232 columns = 7,429 cells [30]. Others include the Perspective Wall [26] and the Hyperbolic Tree Viewer [25]. $^{14}$

Wright [40] demonstrates several applications that make use of 3D effects. One application, a financial portfolio manager, displays more than 3,000 bonds on a single screen. This system uses color to indicate long and short positions, height for the bond's value, and the x and y axes to represent subportfolios and time to maturity.

Unfortunately, these techniques will fall short for very large databases, because, ultimately, we are limited to the number of pixels on the screen. Even with techniques like VisDB's pixel-oriented approach $[22, 23]$ , which displays a data record per pixel, we are still limited to the number of pixels on the screen. With today's technology, this means approximately $1,024 \times 1,024 \approx 1MB$ records, which will not do for multimillion, gigabyte, and certainly not terrabyte-sized databases.

To present an unlimited number of records on the screen at once, we need to present summaries of data. If summaries are provided for each variable, then the only limitation is the number of variables that can be displayed, regardless of the number of records in the database. The InfoCrystal [36] uses an innovative extension of Venn diagrams to visualize data summaries. MiniSet's Evidence Visualizer [3] uses rows of pie charts to summarize the data: one row for each variable, one pie chart for each attribute. The pie chart represents the number of records matching the query variable's chosen value with the pie chart's value.

The approach of presenting summaries of all the data is strongly endorsed by

Shneiderman, who preaches the following mantra (as he calls it) for designing visual information seeking systems: “Overview first, zoom and filter, then details-on-demand” [34, p. 2].

To overview very large numbers of records, we must sample or summarize. MOTC represents a summarization strategy (the crosstabulation form), but there is nothing to prevent applying MOTC to sampled data.

## Effectively Display a Large Number of Variables

The problem of displaying multidimensional data in an effective manner, one that is comprehensible to users, has been studied for some time (see $[20, 21]$ for useful reviews). Perhaps the most natural and widespread approach for adding dimensions to a display is to add visual cues to an existing display. For example, the three dimensions of a 3D graph can be augmented by encoding points on the graph with color, texturing, shapes (glyphs), shading, and other such techniques. Becker $[3]$ demonstrates the use of such techniques with the MineSet system, and various forms of these techniques are supported by contemporary data-visualization software tools (e.g., Advanced Visual Systems).

This family of techniques has two important limitations. First, there are only so many visual cues that can be employed. Perhaps five to ten variables can be represented on a 2D display using the three geographic dimensions, color (divided into hue, saturation, and brightness), shape, size, texture, and shading. Second, and more limiting, is that humans cannot effectively process that many visual cues of this sort at once. More than a few visual cues quickly overwhelm users. Projecting multiple dimensions onto a two-dimensional plane also becomes quickly illegible. Jones [21, ch. 14], for example, reports that eight dimensions are too much for this technique and even six and seven dimensions are difficult to comprehend.

As an example, Feiner and Beshers's Worlds Within Worlds technique [11], which plots $n$ dimensions by successively embedding three-dimensional coordinate systems inside one another, can theoretically display any number of dimensions on the screen. However, Jones [21, ch. 14] points out that more than three levels (nine dimensions) is incomprehensible and even two levels (six dimensions) can be difficult to assimilate.

In MOTC, we present the same visual cue for each variable (a horizontal bar on the screen, with coloring), and use secondary visual cues (position, color) to distinguish the categories associated with a variable (the bins). A popular set of techniques using this approach are graphical matrices in which rows and columns represent variables, and each cell in the matrix is a comparison of the pair of variables represented by the cell's row and column. Perhaps the most common representation of the two variables associated with a matrix cell is a scatter plot $[4, 5, 21]$ . However, other representations are possible, such as histogram profiles $[38]$ , boxplots, and sunplots $[20, ch. 5]$ .

Unfortunately, graphical matrices only allow direct comparisons between two variables. A simpler technique is to display a row of variables. When combined with brushing (see above), variable rows allow any number of variables to be directly compared. MineSet's Evidence Visualizer [3], with its rows of pie charts, does just this. The Influence Explorer [38] presents rows of histograms, each histogram summarizing the values of a single variable. Thus, MOTC's display approach for variables should, in future research, be assessed as a member of this category of representation. Very likely it will be possible to improve the display, but that is something to be determined by extended empirical testing, something that has yet to be done for nearly all the interesting techniques.

Even using graphical matrices of variable rows, the number of variables that can be displayed is limited to the number of rows or columns that can fit on the screen. A natural extension of this technique to use the focus+context ability of Table Lens $[30]$ to augment the number of rows and columns displayed, thereby augmenting the number of variables. Indeed, the interface for MOTC is an elementary example of this idea: The underlying dataset can have a very large number of dimensions, among which the user picks up to eight for a particular analysis; different dimensions can be picked in different analyses. In future editions of MOTC (or MOTC-like systems), we would think that this process could be made smoother and easier and that doing so would benefit the user.

One more technique is worth noting. Inselberg's parallel coordinates system [17, 18, 19, 21] represents variables as vertical bars, and database records as "polylines" that connect each of the variables' vertical bars. Where a polyline crosses a variable's vertical bar represents that polyline's record's value for the variable. This technique allows a very large number of variables to be displayed—as many variables as vertical lines that will fit on the screen. The drawback of this approach is that each polyline represents one record, so the technique is limited to displaying only a relatively small number of records.

## Visualizing Associations Between Variables

Visualization techniques are known to be very helpful for discovering patterns in data. This is especially so for relationships between two variables. Things are more difficult when multiple variables are involved. For this problem, MOTC's approach is of a kind that is accepted in the literature: Present multiple variables and support active display of linkages among them. For example, selecting a record or range of records in one of the Influence Explorer's histograms highlights the corresponding records in the other histograms [38]. Similarly, the Lifelines system [29] displays compact medical patient histories in which users can, say, click on a particular patient visit and immediately see related information, such as other visits by the same patient, medication, reports, prescriptions, and lab tests. Visage [24, 33] presents multiple views of the same data. One window may present geographic data in map form, while another window presents the data as a histogram, and yet another presents the data in a table. Selection of a subset of data in any window highlights the corresponding representation of the data in the other windows. Graphical matrices can be dynamically linked through brushing [4, 5] in which selecting a set of records in one scatterplot (or whatever graphical technique is used for the graphical matrix) simultaneously highlights the same records in the rest of the matrix's cells.

MOTC's use of brushing should be seen as a visualization approach of the kind explored in this literature. As with the issue of display of multiple dimensions, much further research is needed in order to find the optimal design (if there is one) of this sort.

## Summary and Discussion

So, WHAT HAVE WE GOT AND HOW GOOD IS IT? Recall that earlier we argued for a series of goals for any tool to support the hypothesis-generation activity in KDD and database mining. Here, with additional comments, is that list again:

1. Support users in hypothesizing relationships and patterns among the variables in the data at hand. MOTC has hypothesis-hunting mode, in which users may use the mouse quickly and interactively to try out and test arbitrary hypotheses, and thereby explore hypothesis space.

2. Provide users with some indication of the validity, accuracy, and specificity of various hypotheses. MOTC employs prediction analysis for this.

3. Provide effective visualizations for hypotheses, so that the powers of human visual processing can be exploited for exploring hypothesis space. MOTC contributes an innovation in visualization by representing multidimensional hypotheses as binned bars that can be brushed with a mouse. Also, MOTC innovates by tying together hypothesis hunting and evaluation, and does so with a common visual representation.

4. Support automated exploration of hypothesis space, with feedback and indicators for interactive (human-driven) exploration. MOTC does not do this at present, although we have plans to add these features. Briefly, we intend to begin by using a genetic algorithm to encode and search for hypotheses (see Table 2). As in our candle-lighting work [6], we envisage storing the most interesting solutions found by the genetic algorithm during its search and using these solutions as feedback to the user.

5. Support all of the above for data sets and hypotheses of reasonably high dimensionality, say, between 4 and 200 dimensions, as well as on large data sets (e.g., with millions of records). MOTC is not computationally very sensitive to the number of underlying records. We have worked successfully with much larger data sets than those we report here. But MOTC is sensitive to the number of cells in the crosstab grid. With ten variables and ten bins per variable, the multidimensional data grid has 1,010 cells, a number perhaps too large for practical purposes. On the other hand, twelve variables with only four bins each is only $4^{12} \approx 16$ million cells, and this is quite manageable on today's PCs. In short, MOTC-like systems will work over a wide range of useful and computationally feasible problems.

All of this, we think, looks very good and very promising. Still, the ultimate value of any system like MOTC has to be determined by testing real people on real problems. Our experience to date, which is admittedly anecdotal, is very encouraging. Moreover, we note that if you value prediction analysis, then you need to calculate $\nabla$ , U, and so on. MOTC makes these calculations and does them quickly and easily from a user's point of view. All this is excellent reason to proceed to experiments with real people and real problems.

## NOTES

Acknowledgments: This paper is an expanded version of a paper presented by K. Balachandran, J. Buzydlowski, G. Dworman, S.O. Kimbrough, E. Rosengarten, T. Shafer, and W. Vachula, at the Thirty-First Hawaii International Conference on System Sciences. Special thanks to James D. Laing for introducing us to prediction analysis, for encouraging noises as these ideas were developed, and for insightful comments on an earlier version of this paper. Thanks also to Balaji Padmanabhan for some useful comments and suggestions. None of the shortcomings of this paper should be attributed to either Laing or Padmanabhan. This material is based upon work supported by, or in part by, the U.S. Army Research Office under contract/grant number DAAH04–1–0391, and DARPA contract DASWO1 97 K 0007.

1. The example that follows is from [14]. We invite the reader to examine that discussion as a way of following up on this paper.

2. We use the two-variable case for illustration only. As noted above, an important requirement for a hypothesis-exploration DSS is that it handle reasonably high-dimensionality hypotheses. Except where noted—e.g., limitations of screen space in MOTC-like implementations—our points and methods generalize to arbitrarily many dimensions, at least in principle.

3. Nothing much turns on this. One could argue that, at least for certain purposes, this is an ordinal variable. Our point is that this approach can handle nominal variables, if there are any.

4. How a basically quantitative variable should be binned—including how many forms it should have—is typically determined by the investigator, although some principles for automatic binning are available $[39]$ . It is well known that infelicitous binning can lead to anomalies and distortions. In general, for a quantitative variable it is better to have more bins than fewer, in order to reduce or even eliminate loss of information. Having more bins does have increased computational cost. Neglecting computational costs, prediction analysis transparently accommodates arbitrarily large numbers of bins (and cells); in particular, it is unaffected by the presence of crosstab cells without data instances.

5. We do not want to suggest that the data format evident in Table 1 is the only kind of crosstab representation for qualitative data. It is not, and the methods we discuss here, including MOTC itself, are not limited to this particular format, but further elaborating upon the point would be a diversion here. See the discussion in [14] of the condensed ordinal form for one example of an alternative crosstab representation.

6. Or for the cogniscenti of nonmonotonic or defeasible reasoning, "if $x$ then presumably $y$ ." But this is a subtlety we defer to another paper.

7. Of course, if expected error is 0, the ratio is undefined.

8. $\nabla \cdot U = U - K$ or the absolute reduction in error of the prediction. One might prefer instead, e.g., to use the relative reduction in error.

9. How essential is Microsoft Access? In principle, MOTC could be converted easily to work with any ODBC-compliant database, but MOTC makes essential use of Microsoft-specific features, particularly crosstab queries, which are not part of standard SQL. In the future, we intend to completely reimplement MOTC in order to make it database-neutral. That will require a substantial amount of work.

10. The limitation to eight attributes is arbitrary. We chose it to be large enough to make the point that MOTC could handle a nontrivial number of dimensions (eight is interesting), and small enough to fit conveniently on most screens. We intend to relax this in future editions. Doing this right—to allow, say, 200 attributes—will require more sophisticated screen management techniques. See the section Comparison with Alternatives.

11. There is nothing significant about brushing the A (topmost) attribute. The ordering of the attributes on the screen is arbitrary. The user can brush a bin in any of the attributes and MOTC will respond appropriately.

12. The following remarks will perhaps be useful for interpreting figure 4, and specifically the hypothesis it represents. First, recall figure 3, which is a simpler figure of MOTC in prediction mode. There, the hypothesis represented is, roughly, "If A is low, and B is high (bins 3 and 4), and C is low (bins 1 and 2), then D is middling (bin 2)." (We say "roughly" because the shading is really serving to determine the error-cell representation.) Call this hypothesis $\alpha$ . It is indicated by the horizontal shading, which is retained in figure 4. In addition, figure 4 contains two other hypotheses. $\beta$ (indicated by vertical shading): "If A is high, and B is low and C is high, then D is low." $\gamma$ (indicated by cross-hatched shading): "If A is middling, and B is in bin 2 and C is in bin 3, then D is high." In total, figure 4 represents the conjunction of these three hypothesis: $\alpha$ and $\beta$ and $\gamma$ . This is a complete hypothesis in that every bin is associated with some hypothesis (or prediction).

13. Thanks to Balaji Padmanabhan for this point. See also [28].

## REFERENCES

1. Balachandran, K.; Buzydlowski, J.; Dworman, G.; Kimbrough, S.O.; Shafer, T.; and Vachula, W.J. MOTC: An aid to multidimensional hypothesis generation. In J.F. Nunamaker, Jr., and R.H. Sprague, Jr. (eds.), Proceedings of the Thirty-First Hawaii International Conference on System Sciences. Los Alamitos, CA: IEEE Computer Society Press, 1998, CD-ROM.

2. Balachandran, K.; Buzydlowski, J.; Dworman, G.; Kimbrough, S.O.; Shafer, T.; and Vachula, W.J. Examples of MOTC at work for knowledge discovery in data. Communications of AIS, forthcoming. Also available at http://grace.wharton.upenn.edu/\~sok/motc.

3. Becker, B.G. Using mine set for knowledge discovery. IEEE Computer Graphics and Applications, 13 (July–August 1997), 75–78.

4. Becker, R.A., and Cleveland, W.S. Brushing scatter plots. Technometrics, 29, 2 (1987), 127–142.

5. Becker, R.A.; Huber, P.J.; Cleveland, W.S.; and Wilks, A.R. Dynamic graphics for data analysis. Statistical Science, 2, 4 (1987), 355–395.

6. Branley, B.; Fradin, R.; Kimbrough, S.O.; and Shafer, T. On heuristic mapping of decision surfaces for post-evaluation analysis. In J.F. Nunamaker, Jr. and R.H. Sprague, Jr. (eds.), Proceedings of the Thirtieth Hawaii International Conference on System Sciences. Los Alamitos, CA: IEEE Computer Society Press, 1997.

7. Codd, E.F.; Codd, S.B.; and Salley, C.T. Beyond decision support. Computerworld, 27, 30 (July 26, 1993).

8. Dhar, V., and Stein, R. Seven Methods for Transforming Corporate Data into Business Intelligence. Upper Saddle River, NJ: Prentice-Hall, 1997.

9. Eick, S.B.; Steven, J.L.; and Sumner, E.E. Seesoft: a tool for visualizing line oriented software. IEEE Transactions on Software Engineering, 18, 11 (1992), 957–968.

10. Fayyad, U.M.; Piatetsky-Shapiro, G.; Smyth, P.; and Uthurusamy, R., eds. Advances in Knowledge Discovery and Data Mining. Cambridge, MA: MIT Press, 1996.

11. Feiner, S., and Beshers, C. Worlds within worlds: metaphors for exploring n-dimensional virtual worlds. Proceedings of the ACM Symposium on User Interface Software 1990. New York: ACM Press, 1990, pp. 76–83.

12. Furnas, G.W. Generalized fisheye views. ACM SIGCHI Conference on Human Factors in Computing Systems. New York: ACM Press, 1986, pp. 16–23.

13. Gershon, N., and Eick, S.G. Information visualization. IEEE Computer Graphics and Applications, 13 (July–August 1997), 29–78.

14. Hildebrand, D.K.; Laing, J.D.; and Rosenthal, H. Analysis of Ordinal Data, vol. 8 of Quantitative Applications in the Social Sciences. Newbury Park, CA: Sage Publications, 1977.

15. Hildebrand, D.K.; Laing, J.D.; and Rosenthal, H. Prediction Analysis of Cross Classifications. New York: John Wiley & Sons, 1977.

16. Inmon, W.H. Building the Data Warehouse, 2d ed. New York: Wiley Computer Publishing, 1996.

17. Inselberg, A. The plane with parallel co-ordinates. The Visual Computer, 1 (1985), 69–91.

18. Inselberg, A., and Dimsdale, B. Multidimensional lines: proximity and applications. SIAM Journal of Applied Mathematics, 54 (April 1994), 578–596.

19. Inselberg, A., and Dimsdale, B. Multidimensional lines: representation. SIAM Journal of Applied Mathematics, 54 (April 1994), 559–577.

20. Jambu, M. Exploratory and Multivariate Data Analysis: Statistical Modeling and Decision Science. San Diego: Academic Press, 1991.

21. Jones, C.V. Visualization and Optimization: Operations Research/Computer Science Interfaces. Boston: Kluwer Academic Publishers, 1995.

22. Keim, D.A. Pixel-oriented visualization techniques for exploring very large databases. Journal of Computational and Graphical Statistics, 5, 1 (March 1996), 58–77.

23. Keim, D.A., and Kriegel, H.-P. VisDB: database exploration using multidimensional visualization. IEEE Computer Graphics and Applications, 14 (September 1994), 40–49.

24. Kolojejchick, J.; Roth, S.F.; and Lucas, P. Information appliances and tools in visage. IEEE Computer Graphics and Applications, 13 (July–August 1997), 32–41.

25. Lamping, J.; Rao, R.; and Pirolli, P. A focus+context technique based on hyperbolic geometry for visualizing large hierarchies. In I.R. Katz, R. Mack, and L. Marks (eds.), ACM SIGCHI Conference on Human Factors in Computing Systems. Denver: Association of Computing Machinery (ACM), 1995, pp. 401–408.

26. Mackinlay, J.D.; Robertson, G.G.; and Card, S.K. The perspective wall: detail and context smoothly integrated. ACM SIGCHI Conference on Human Factors in Computing Systems. New Orleans: Association of Computing Machinery (ACM), 1991, pp. 173–179.

27. Menninger, D. Oracle OLAP products: adding value to the data warehouse. An Oracle White Paper, Part#: C10281, September 1995.

28. Moore, A., and Lee, M.S. Cached sufficient statistics for efficient machine learning with large datasets. Journal of Artificial Intelligence Research, 8, 3 (1998), 67–91.

29. Plaisant, C.; Rose, A.; Milash, B.; Widoff, S.; and Shneiderman, B. Lifelines: visualizing personal histories. In M.J. Tauber (ed.), ACM SIGCHI Conference on Human Factors in Computing Systems. Vancouver, BC: Association of Computing Machinery (ACM), 1996, pp. 221–227.

30. Rao, R., and Card, S.K. Exploring large tables with the table lens. In I.R. Katz, R. Mack, and L. Marks (eds.), ACM SIGCHI Conference on Human Factors in Computing Systems—Conference Proceedings Companion. Denver: Association of Computing Machinery (ACM), 1995, pp. 403–404.

31. Rao, R. From research to real world with Z-GUI. IEEE Computer Graphics and Applications, 13 (July–August 1997), 71–73.

32. Rao, R., and Card, S.K. The Table Lens: merging graphical and symbolic representations in an interactive focus+context visualization for tabular information. Proceedings of the CHI '94 Conference, 1994, pp. 318–323.

33. Roth, S.F.; Lucas, P.; Senn, J.A.; Gomberg, C.C.; Burks, M.B.; Stroffolino, P.J.; Kolojejchick, J.A.; and Dunmire, C. Visage: a user interface environment for exploring information. IEEE Conference on Information Visualization. San Francisco: IEEE Computer Press, October 1996, pp. 3–12.

34. Shneiderman, B. The eyes have it: a task by data type taxonomy of information visualizations. Proceedings of the IEEE Symposium on Visual Languages 1996. Los Alamitos, CA: IEEE Publications, September 1996, pp. 336–343 [an active hyperlinked version of Shneiderman's taxonomy is available at the OLIVE site: http://otal.umd.edu/Olive].

35. Spence, R., and Apperley, M. Database navigation: an office environment for the professional. Behaviour & Information Technology, 1, 1 (1982), 43–54.

36. Spoerri, A. Infocrystal: a visual tool for information retrieval and management. Conference on Information Knowledge and Management. Washington, DC: Association of Computing Machinery (ACM), November 1993, pp. 11–20.

37. Tauber, M.J., ed. ACM SIGCHI Conference on Human Factors in Computing Systems. Vancouver, BC: Association of Computing Machinery (ACM), 1996.

38. Tweedie, L.A.; Spence, R.; Dawkes, H.; and Su, H. Externalising abstract mathematical models. In M.J. Tauber (ed.), ACM SIGCHI Conference on Human Factors in Computing Systems. Vancouver, BC: Association of Computing Machinery (ACM), 1996, pp. 406–412.

39. Wand, M.P. Data-based choice of histogram bin width. American Statistician, 51, 1 (1997), 59–64.

40. Wright, W. Business visualization applications. IEEE Computer Graphics and Applications, 13 (July–August 1997), 66–70.
