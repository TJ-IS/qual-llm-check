---
otero_id: 3816
otero_key: "G95EQYUG"
title: "The Influence of Query Interface Design on Decision-Making Performance"
authors: "Cheri Speier; Michael G. Morris"
year: "2003"
journal: "MIS Quarterly"
doi: "10.2307/30036539"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# THE INFLUENCE OF QUERY INTERFACE DESIGN ON DECISION-MAKING PERFORMANCE<sup>1</sup>

By: Cheri Speier Eli Broad College of Business Michigan State University East Lansing, MI 48824 U.S.A. cspeier@msu.edu

Michael G. Morris McIntire School of Commerce University of Virginia Charlottesville, VA 22904 U.S.A. mmorris@virginia.edu

## Abstract

Managers in modern organizations are confronted with ever-increasing volumes of information that they must evaluate when making a decision. Data warehousing and data mining technologies have given managers a number of valuable tools that can help them store, retrieve, and analyze information contained in large databases; however, maximizing user performance with these tools remains a challenge for information systems professionals. One important and under-explored aspect of the effectiveness of these tools is the design of the query interface. In this study, we compared the use of visual and text-based interfaces on both low and high complexity tasks. Results demonstrated that decision maker performance was more accurate using the text-based interface when task complexity was low; however, decision makers using the visual interface performed better when task complexity was high. In addition, decision makers’ subjective mental workload was significantly lower when using the visual interface, regardless of task complexity. In contrast to expectations, less time was needed to make a decision on low complexity tasks when using the visual interface, but those results were reversed under conditions of high task complexity. These results have important implications for the design of managerial decision-making systems, particularly in complex decision-making environments.

Keywords: Database, computer interface, decision-making

## Introduction

Effectively manipulating and interpreting data are critical organizational capabilities in today’s hypercompetitive business environment. Decision making often must occur more quickly and with finer granularity than in the past—for example, allocating product mix for a specific customer rather than an entire market (Swink 1995). As a result, many firms have invested in information technologies such as data warehousing and data mining to help managers make sense of data previously scattered throughout the enterprise (e.g., Cooper et al. 2000). In addition, these investments have led to an increase in the number of decision makers using these new data management technologies throughout the organization (Wixom and Watson 2001).

Despite the impressive technical advances associated with these new data management tools, there are a number of behavioral concerns associated with how these tools are used on an everyday basis. For example, while new data management technologies empower users to evaluate vast information repositories, they also have the potential to overwhelm decision makers, leading to information overload (Dillon 2000). Decision makers may now feel obligated to exhaustively scan large databases (Keim and Kriegel 1994), which can be time consuming and result in diminishing returns (Lohse 1997a).

As the information environment becomes increasingly saturated, getting managers’ attention and helping them find and focus on the most relevant data becomes increasingly difficult (Davenport and Beck 2001). Therefore, identifying querying techniques that can support efficient information retrieval and decision making to overcome the problem of overload has become critical. One potential mechanism for improving decision-making performance is information visualization (Card et al. 1999; Chen 1999; Tegarden 1999; Tufte 2001; Ware 2000) because it allows decision makers to leverage individua perceptual processes more effectively (Tegarden 1999).

Information visualization techniques have been widely applied in science and geography but have been integrated into business applications only recently (Mirel 1998; Roth et al. 1997). Existing research examining information visualization largely focuses on the construction of visualization techniques and is surprisingly silent on the evaluation of these techniques (Au et al. 2000). Therefore, empirical studies that assess the effectiveness of visualization techniques are sorely needed (Mirel 1998). To address this gap in the literature, the research question guiding this research is” “How do information visualization techniques such as visual query interfaces influence decision-making performance?”

While the design of query tools is an important aspect to understanding decision-making performance with technology, it is also important to examine contextual influences that might enable a decision maker to most effectively exploit these techniques. Building on the research question above, we extend our investigation into how query interfaces (which guide query construction and information representation) interact with task complexity and individual spatial ability to influence key decision-making outcomes.

## Theoretical Background and Hypothesis Development

Historically, there have been two major alternatives to query interface design: traditional textbased approaches and more modern visual approaches that take advantage of information visualization techniques (Shneiderman 1998). Central to our understanding of how a given query interface might support (or limit) decision-making effectiveness is the concept of restrictiveness (Silver 1991). System restrictiveness refers to the degree and manner in which a system limits its users’ decision-making processes to a subset of all possible processes. Implied by this definition of restrictiveness is the notion that the type of system (here, the query interface) employed could enforce a particular type of decision strategy. In the context of this research, both the text-based interface and the visual query interface enforced an “elimination by aspects (EBA)” strategy (Todd and Benbasat 1999), thus the decision strategy enforced by the interface was controlled. However, while enforcing the same decision strategy, the visual query interface differed from the textbased design across four different design dimensions.

First, the visual query interface employed information visualization techniques. Modern query interfaces go beyond simple text data presentation and include interactive, graphical representation and manipulation of data that purport to promote better user performance (Card et al. 1999; McCormick et al. 1987). The visual interface used here, the Homefinder (Ahlberg and Shneiderman 1994), presented data points corresponding to addresses on a city map as compared to a tabular display common of many popular query interfaces.

Second, the visual query interface included elements of “direct manipulation” (Shneiderman 1998). Here, the Homefinder employed dynamic visual query filters that were used to adjust query criteria, allowing more flexible (i.e., less restrictive), iterative querying (Keim and Kriegel 1994; Kumar et al. 1997). By adjusting each of these query filters (using slider bars and buttons) as needed, the user was able to enter an initia query and then dynamically refine it.

Third, as part of the direct manipulation element, users of the visual query interface received immediate feedback about the nature and scope of the data as they manipulated the various query filters (Ahlberg and Wistrand 1995; Keim and Kriegel 1994). This allowed them to immediately “see” the results of their queries vs. having to wait (albeit sometimes less than a second) for a textbased query to be processed by the computer and the results displayed on screen.

Finally, while both interfaces supported an EBA decision strategy, the manner in which it was implemented across the two interfaces varied. In the text-based interface, the user formulated a query, entered it, and received text output listing all of the attributes of each data point responsive to the query. However, in the visual query interface, users adjusted the aforementioned slider bars and received an overview of all the data that met the specified criteria, but received detailed data attributes only “on demand.” The visual query interface here supported this capability through the use of a starfield display (see Appendix A). Consistent with the design goals applied in this research, starfield displays allow a decision maker to gain a quick understanding of the nature and scope of the data without overwhelming them with unnecessary detail (Ahlberg and Wistrand 1995; Shneiderman 1998).

Given these contrasts in design, the research model developed in this study suggests that interface-based differences (e.g., how data are displayed, filtered, and manipulated) will affect the decision maker’s perception of effort required to use the system as well as their decision accuracy and speed in reaching a solution. In addition, it is reasonable to assume that the amount of data examined and one’s ability to understand and interpret graphical displays will moderate the relationship between query interface design and decision outcomes. Thus, this study extends the cognitive fit perspective from that of information presentation (i.e., match between information presentation and task—see, for examples, Vessey 1991; Vessey and Galletta 1991) to an interactive querying environment (i.e., match between querying interface and task).

The research model used in this study is illustrated in Figure 1. Decision accuracy and decision time were the primary outcomes of interest in this research; however, in order to gain some additional insight into the cognitive effort required when using visual and text-based interfaces, subjective mental workload (SMW) was also measured. Subjective mental workload represents the subjective experience of a decision maker and is influenced by a decision maker’s processing strategies, perceptions, and skill level (Hart and Staveland 1988; Scerbo and Mouloua 1999; Shiffrin and Schneider 1977).

![](/api/attachments/G95EQYUG/fulltext/images/5ae262128ce48271479bb5d31553fbf60a2e0f5c3835391858f67ce1979b3163.jpg)  
Figure 1. Research Model

## Task Complexity

Prior research suggests that task complexity increases when there are more information cues to process, more acts to execute, or increased interdependence between the cues and acts—for example, when one uses iterative querying in order to narrow down a large range of feasible solutions to a set of “best” answers (Wood 1986). In an information retrieval context, complexity increases as the number of potential solutions increases because the user must examine and compare each feasible solution to other feasible solutions if they wish to determine the most effective or accurate response (Campbell 1988; Card et al. 1983; Newell and Simon 1972).

In the context of this research, when querying a data set, there may be a small or very large number of feasible solutions that meet specific criteria. A decision maker should find it easier to evaluate a small number of feasible solutions to find the best outcome as opposed to evaluating a large range of possible solutions. A small number of feasible solutions can be presented simultaneously in a manageable display space (e.g., a single computer screen), allowing decision makers to focus their attention and more easily compare alternatives. Decision makers can typically process text-based information effectively while maintaining low levels of subjective mental workload when feasible solution sets are small (Payne et al. 1988).

Conversely, visual query interfaces typically do not present all of the detailed data simultaneously on the screen and instead provide these details only on demand (Shneiderman 1998). Thus, the use of visual querying may actually increase SMW when task complexity is low, since acquiring details of the feasible solutions involves assessing each feasible solution independently from all other possible solutions, making the decision-making process unnecessarily cumbersome. Therefore, we hypothesize:

H1a: Subjective mental workload will be lower with text-based querying than with visua querying when task complexity is low.

Under conditions of high task complexity, subjective mental workload increases as more data elements are evaluated and retained in working memory (Rossano and Moak 1998). Decision makers retain as much data as their working memory allows until the amount of data increases to a point where their ability is constrained (March and Simon 1958; Miller 1956). Once this point is reached, decision makers will resort to cognitive simplification strategies (Streufert 1973) that typically result in decreased decision quality, increased decision time, and/or increased confusion (Chewning and Harrell 1990; Jacoby et al. 1974a, 1974b; Johnson and Payne 1985). In such cases, decision makers may seek to reduce cognitive workload (Beach and Mitchell 1978) by relying on human perceptual processes that consume less time than cognitive or analytical processes (Kirlik et al. 1993; Payne et al. 1988). As Tufte states, “High information [visualization] displays are not only an appropriate and proper complement to human capabilities, but such designs are frequently optimal” (2001, pg. 168).

To leverage these perceptual processes, decision makers can use visualization techniques. Such techniques have been shown to reduce information processing demands on working memory (Kosslyn 1985, 1989; Lohse 1993; Pinker 1990; Wickens and Carswell 1995) by accelerating the speed and depth at which large amounts of data can be absorbed and comprehended (Orford et al. 1999; Schkade and Kleinmutz 1994). These results suggest that visual querying may help users focus on the most salient attributes of the data while filtering out less relevant detail (Ahlberg and Shneiderman 1994). By exploiting the brain’s capabilities to recognize patterns and thus reduce mental workload, decision performance can be improved dramatically (Card et al. 1999; Finke and Shepard 1986; Kim et al. 2000; Lohse 1997b; Shiffrin and Schneider 1977; Wickens and Carswell 1995). Therefore, we hypothesize:

H1b: Subjective mental workload will be lower with visual querying than with text-based querying when task complexity is high.

The hypotheses for decision accuracy and decision time are based on similar logic to those for subjective mental workload. With respect to decision accuracy, decision makers are likely to have ample cognitive capacity when processing low complexity tasks. When using text-based querying in relatively small data sets, decision makers can often quickly compare key attributes to reduce the set of feasible solutions to a final answer without running additional, iterative queries. However, decision makers using visual querying techniques are unable to compare a small number of feasible solutions simultaneously and must instead look at each record independently. This additional processing activity may result in errors since decision makers may not remember all of the detailed data when comparing one data point to another. Thus, we hypothesize:

H2a: Decision accuracy will be higher with textbased querying than with visual querying when task complexity is low.

In contrast to low complexity situations, when task complexity is high, decision makers are able to solve problems more effectively when directly manipulating the data (Frese 1987; Mirel 1998). As problems become increasingly complex, decision makers need to employ iterative data evaluation strategies that require them to keep track of prior comparisons in order to reach a best solution (Chambers et al. 1983). Decision makers often make trade-offs between different attributes to find the best potential solutions; however, keeping track of each potential solution and its attributes is very difficult (Mirel 1998). Therefore, evaluating different alternatives across a breadth of attributes increases a decision maker’s cognitive processing workload and can inhibit decision-making performance severely (Einhorn 1971; Johnson and Payne 1985; Simon 1979).

To help overcome these problems, decision makers can reduce cognitive processing through the use of visual querying techniques in order to reduce the amount of information examined (Smelcer and Carmel 1997). When the data set is large, visual querying can help focus decision makers’ attention on data that are directly relevant to a task (Simon 1979) and make any patterns in the data more salient, thus increasing decision performance (Kleinmunz and Schkade 1993; Scriabin and Vergin 1975; Swink and Speier 1999; Taylor and Iwanek 1980).

Visual querying also provides immediate, relevant feedback to a decision maker, increasing the sense of control he or she has over the querying process. Decision makers can instantly visualize how changing a single parameter by one increment affects the number of feasible solutions and then immediately reverse any changes made (Shneiderman 1998). This immediate feedback and control can have a positive effect on key decision making outcomes (Koenemann and Belkin 1996; Te’eni 1991). Therefore, we hypothesize:

H2b: Decision accuracy will be higher with visua querying than with text-based querying when task complexity is high.

Broadly speaking, user interface design attempts to model reality such that users are able to intuitively interact with a specific information system. For example, one of the reasons that personal financial software (such as Quicken) has been so successful is that the system designers chose a checkbook as the metaphor around which transactions are organized—that is, the computer model closely corresponds to the represented context (Norman 1993). For most tasks, textbased characters on a screen are abstractions that result in only a loose correspondence between the system and reality, while visual interfaces provide a more direct mapping (Card et al. 1998). When the correspondence between the system and reality is low, the user must first process the presented data and then structure it such that he or she understands it. These operations require significant cognitive processing by the user and hence require more time (Head 1984; Hutchins et. al. 1986).

When task complexity is low, there is only a limited amount of data to compare and evaluate. In these cases, the low correspondence between a text interface and reality is unlikely to place a significant burden on cognitive processing. While the correspondence between the visual interface and reality is higher, the physical process of selecting each data point in the feasible solution set to identify and evaluate the detailed attributes will likely add processing time. However, as the number of feasible solutions increases (thus increasing task complexity), the lack of correspondence between the text interface and reality will likely make it increasingly difficult to process data, thereby inhibiting decision making (Simon 1979; Streufert 1973). Visual query interfaces, with their more direct correspondence to reality, allow decision makers to more quickly isolate and evaluate only those records that are most relevant (Shneiderman 1998) and should therefore enable users to make decisions faster (Lohse 1997b), leading to the following hypotheses:

H3a: Decision time will be faster with text-based querying than with visual querying when task complexity is low.

H3b: Decision time will be faster with visual querying than with text-based querying when task complexity is high.

## Spatial Ability

Given the graphical nature of many of these query interfaces, spatial ability may be an important individual skill that moderates one’s performance with visual tools (Egan 1988; Loy 1991; Robinson and Swink 1994; Smelcer and Carmel 1997; Stanney and Salvendy 1995; Swink 1995; Taylor and Iwanek 1980). For example, individuals with stronger visualization skills often have higher decision accuracy and/or efficiency than those with lower spatial abilities (Chen and Rada 1996; Robinson and Swink 1994; Stasz 1980; Swink and Speier 1999). Not all the empirical evidence, however, has supported a positive relationship between visualization ability and performance (e.g., Smelcer and Carmel 1997; Swink 1995).

One explanation for the inconsistency in spatia ability effects is that system features can either capitalize on, or compensate for, users’ inherent abilities (Egan 1988; Stanney and Salvendy 1995). Users are able to capitalize on system features when they have some pre-existing leve of a given quality that the system was designed to tap (e.g., spatial ability). However, when a user lacks a particular quality, system features can overcome those limitations by compensating for that particular skill (e.g., spatial ability), leading to higher performance (Chen et al. 2000; Messick 1976; Stanney and Salvendy 1995). How one designs a system to take advantage of capitalization or compensation is an ongoing challenge for information system designers (Allen 2000).

Relevant to the problem studied in this research, visual querying relies on decision makers’ perceptual skills in multiple ways. When examining small solution sets, decision makers must keep track of which data points have been examined and mentally compare the attributes associated with the data points even when the attribute data can no longer be visualized—a difficult cognitive task, particularly for those with low spatial ability. On the other hand, when querying data sets with many feasible solutions, decision makers with strong spatial skills can more adeptly process a series of iterative queries (Brasseur 1997), increasing the both decision speed and accuracy. While suggesting that those with high spatial ability may capitalize on their skills in a visua querying environment to enhance decision-making performance, theory does not necessarily suggest the opposite—in other words, those with low spatial ability will not necessarily be better using text-based querying. Thus, we offer the following hypotheses for visual query interfaces only:

H4: Subjective mental workload will be lower with high spatial ability decision makers than with low spatial ability decision makers when using visual querying.

H5: Decision accuracy will be higher with high spatial ability decision makers than with low spatial ability decision makers when using visual querying.

H6: Decision time will be lower with high spatial ability decision makers than with low spatial ability decision makers when using visual querying.

## Research Method

A 2 × 2 × 2 experimental design was implemented to test the hypotheses. The three factors were query interface (text-based vs. visual, within subjects), task complexity (low vs. high, within subjects), and spatial ability (low vs. high, between subjects). A total of 372 undergraduates having either limited or no prior experience using database management systems participated in the study. Participants completed an initial pretest that captured a wide range of demographic, individual difference (including spatial ability), and attitudinal information. Subsequently, they completed two home-finding tasks (low and high task complexity) using either the visual or the textbased interface, and completed a post-test assessing their subjective mental workload after each task. For each task, subjects were told that their overall performance would be evaluated by both the accuracy of their decision and the speed at which they finished. They were asked to raise their hand as soon as they completed each task, at which time the experimenter provided them with a post-task survey and recorded the elapsed time on the task. Subjects then performed comparable tasks using the other interface and completed SMW post-tests as previously described. The order of the user interface treatments was counterbalanced across subjects. At the end of the experiment (i.e., after using both interfaces), subjects completed a final questionnaire designed to elicit their experience and their preference between the two interfaces.

## Experimental Task

A home finding task was used in this study to simulate a real estate acquisition decision. Vignettes were provided for each task (e.g., you have just taken a new job and need to purchase a home) and subjects were told to identify the five homes (out of approximately 1,100 homes available for sale) that best fit the criteria provided in the vignette. Subjects could create an unlimited number of queries to obtain their final solution and there were no time restrictions.

## Complexity Manipulation

Task complexity was manipulated by increasing the size and the homogeneity of the solution set (Campbell 1988; Wood 1986) and by creating a scenario that was not dominated by a few superior solutions (Schkade and Kleinmuntz 1994). Thus, for the low task complexity intervention, home attributes were defined such that five homes met the criteria. For the high task complexity intervention, “necessary” and “desirable” attributes were included in the task scenario. Once the necessary criteria were met, the solution set stil included approximately 200 homes. This task was constructed such that there was a “best five” set of solutions (determined a priori) across the 200- home subset. The best solutions met all of the criteria (i.e., both necessary and desired) and were within \$10,000 of the lowest priced home in the subset.

To reduce the number of homes selected in the high complexity intervention, decision makers were asked to identify homes that met (but did not necessarily exceed) all of the criteria at the lowest possible cost, providing the overall best value for the buyer. Subjects iterated through multiple queries by changing the value applied to different attributes/constraints (e.g., number of bedrooms, fireplace, cost) to obtain increasingly better solutions. For example, subjects could evaluate desirable attributes including the availability of a fireplace, having an extra bedroom to convert to an office, etc. (depending on the task scenario) by trading-off one or more of these desirable attributes against the increases in costs of the homes.

It was important that the low and high complexity tasks be equivalent across the two query interfaces. This was accomplished by first identifying an initial set of low and high complexity tasks that met our homogeneity criteria (solution set of 5 homes for low complexity and approximately 200 for high complexity), then creating a mirror image of the data by taking the same query attributes and changing the address of each home in order to alter its physical location. This allowed us to use the same data set across the two interfaces, yet mask the preferred solution in each.

All experiments involve making a series of tradeoffs and judgment calls. In this study, we decided that regardless of the interface used, subjects would always receive the “low complexity” task first. This allowed us to establish a reasonable baseline measurement of decision time against which the high complexity task times could be compared. We opted not to balance the task complexity manipulation because we felt that if the task order had been reversed, task completion times for the high complexity task could be inflated while those for the low complexity task might be artificially lowered. This approach did provide a slight advantage to the second (high complexity) task due to the subject having greater familiarity with the task and interface. Therefore, it led to a conservative test of the theory because the task ordering would tend to pull the means for the low and high complexity manipulations closer together, thus muting potential differences.

## Query Interfaces: Text-Based and Visual

The visual query interface was Homefinder<sup>2</sup> (Ahlberg and Shneiderman 1994), a type of geographic information system (GIS) that included visual tools that allowed decision makers to dynamically define and narrow the selection criteria for a desired home as part of their database query. Once the query constraints were defined, the interface then displayed the number of homes meeting those criteria using a starfield display (see Appendix A). Users could then use slider bars to constrain the solution set based on details that the vignette provided (as previously described). Homes that met these criteria appeared as a colored point on a city map (Washington, D.C), while those that did not meet the criteria disappeared from the screen. Users could click on any displayed point to obtain all of the detailed information associated with that particular home.

On the text-based interface, subjects entered home criteria into an input form (see Appendix B). After clicking an “Execute Query” button, a query was run against a Microsoft Access database and the solution set was displayed on the user’s computer screen. The input form enabled the user to enter the same criteria that were included in the Homefinder interface. The results were presented in an Access table where each row represented a particular home and the columns represented values for each of the attributes in the database (see Appendix C). The data underlying the Homefinder application was identical to that in the Access database. While precise equivalence is impossible when the nature of the interface is altered, each interface had a similar number of elements and every attempt was made to provide a comparable level of specificity in the directions that the users saw on screen. In the visual treatment, with fewer words (73 versus 91), additional graphic elements were likely to have made up the difference. Even considering only the number of words, the slight difference would not be likely to manifest itself in any meaningful time differences.

There were some slight differences in the output information provided to users. For example, distance information to a given point was reflected on the visual interface output, but not directly on the text-based interface output (although neighborhood and address information was contained on the output). This limitation of the text-based design was not relevant to identifying the optima solution to the task—in other words, it was an initial filtering tool only. In both the visual and the text-based interfaces, the initial input screen allowed users to enter distance criteria as an initial “must have” filter; however, once the minimum distance constraint had been met, it was no longer relevant to finding the set of best alternatives.

## Measurement

Measures were gathered for subjective mental workload, spatial ability, decision accuracy, and decision time. Subjective mental workload was measured using the NASA Task Load Index (NASA-TLX) (Hart and Staveland 1988) (see Appendix D). This instrument has been extensively used and validated in human factors research. The NASA-TLX instrument can capture subjective differences at low levels of workload (Morris et al. 1999; Wierwille and Eggemeier 1993) and yet is relatively easy to administer (Hart and Staveland 1988).

The NASA-TLX instrument conceptualizes SMW as six dimensions: mental demand, physical demand, time constraints, performance, effort, and level of frustration. The instrument presents all possible pairs of dimensions (15 combinations) and subjects are asked to select which of the dimensions (in each pair) most heavily contributed to their experienced workload. The SMW score is determined by counting the number of times each dimension influenced mental workload multiplied by the salience of each dimension (on a scale of 0 to 100). Dimension scores are added together to obtain an overall measure of SMW.<sup>3</sup> Subjects completed the NASA-TLX after each task.

Spatial visualization ability was measured by the spatial orientation instrument developed by Ekstrom, French, and Harman’s (1976). This instrument assesses a person’s ability to mentally manipulate objects within space. This ability predicts the ease with which users are able to construct a mental model of the information (Stanney and Salvendy 1995) and is particularly valuable when panning or scanning across a field of data (Cribben and Chen 2001). The spatial orientation instrument measures the subject’s response to 80 pictures by asking the subject to assess the similarity between spatial representations. It provides a numerical score indicating the number of visualizations the subject scored correctly.

Decision accuracy was operationalized as the number of matches the user had to the “best five” answers. It was calculated as the percentage of optimal (i.e., number of “best five” solutions identified by the user/5). Decision time was calculated as the number of minutes required to complete each task using a given user interface.

Finally, two measures of experience, prior experience using database management systems and prior experience buying homes/renting apartments, were used as control variables. Prior research has demonstrated the positive effect of both task and technology expertise (e.g., Mackay and Elam 1992). In addition, two individua difference variables—gender and computer selfefficacy (Compeau and Higgins 1995)—were also included as control variables.

A pilot test was conducted to test the interface and task complexity manipulations and evaluate the relevance of the experimental task for this population. Observation and interviews of student subjects indicated that they found the task engaging and were motivated to perform well. Minor instrumentation and research design modifications were made based on pilot study results.

## Results

The demographic characteristics of the sample were consistent with expectations: of the participants, 56 percent were women, 91 percent were younger than age 25, and the distribution of majors was consistent with the student population from which the sample was drawn. The majority (64 percent) had rented apartments or purchased homes and 51 percent had prior database experience, although only 4 percent of these subjects felt that their skills were well developed. Thus, our sample reflects what one might expect of a typica end-user population as opposed to one made up of information systems professionals.

Spatial visualization scores ranged from 20 to 80 (where 80 was a perfect score) and the average score was a 56. The sample was divided in half where those receiving 56 points (also the median) or below were assigned to the low spatial visualization group and those scoring greater than 56 points were placed in the high visualization group.

The hypotheses were tested using repeated measures ANOVA to capture any within-subject variation across tasks. The results are reported in Table 1 and significant relationships are illustrated in Figures 2a through 2d. Given the possibility of a task accuracy/time trade-off (i.e., subjects could have spent more time to get more accurate answers), a correlation analysis was performed on decision accuracy and time. There were no significant correlations<sup>4</sup> and, thus, a multivariate analysis was not needed. The control variables (task experience, database experience, gender, and computer self-efficacy) were all nonsignificant and were excluded from further analysis.

The results for subjective mental workload indicated that the main effects for interface and task complexity were significant as was the interface × task complexity interaction. There were no significant main or interaction effects for spatial ability. SMW for the visual query interface (549.59) was significantly lower than SMW for the text-based query interface (574.74) under conditions of high task complexity, providing strong support for H1b. Surprisingly, the results for H1a (low task complexity) mirrored those of H1b, in contrast to the hypothesized relationship. Subjective mental workload for the visual query interface (367.71) was significantly lower than that for the text-based approach (390.28). Thus, H1a was contradicted.

Results for decision accuracy indicated significant main effects for both interface and task complexity but not for spatial ability. There also were significant interaction effects for interface × task complexity and for interface × spatial ability. In order to test each of the associated hypotheses, decision accuracy results for each of the four tasks (e.g., all four within-subject combinations) were teased apart using parameter estimates. Parameter estimates are the planned contrasts used to differentiate between the dependent variables and are reported using a t-value, transformed from the univariate F-test (SPSS 1990). The results indicated that the text-based query interface (degree of optimal = .80) produced significantly higher accuracy than the visual query interface (degree of optimal = .59) on low task complexity problems, providing support for H2a as expected. Also consistent with expectations, the visual interface (degree of optimal = .24) produced significantly higher accuracy than the text-based interface (degree of optimal = .13) on high task complexity problems. Thus, H2b was also supported.

<table><tr><td>Dependent Variable</td><td>Effect</td><td>F statistic (1, 372)</td><td>p-value</td><td>Effect</td><td>Visual Interface Mean (s.d.)</td><td>Text Interface Mean (s.d.)</td><td>Hypothesis</td></tr><tr><td>Mental Workload</td><td>Interface</td><td>4.885</td><td>.028</td><td></td><td></td><td></td><td></td></tr><tr><td>Mental Workload</td><td>Task Complexity</td><td>1530.967</td><td>.000</td><td></td><td></td><td></td><td></td></tr><tr><td>Mental Workload</td><td>Spatial Ability</td><td>.934</td><td>.424</td><td></td><td></td><td></td><td></td></tr><tr><td>Mental Workload</td><td>Interface × Task Complexity</td><td>5.837</td><td>.016</td><td>Low Comp. High Comp</td><td>367.711 (228.25) 549.592 (340.00)</td><td>390.275 (192.84) 574.736 (287.03)</td><td>H1a: Not supported H1b: Supported</td></tr><tr><td>Mental Workload</td><td>Interface × Spatial Ability</td><td>.550</td><td>.459</td><td>Low Spatial High Spatial</td><td>453.13 (287.92) 464.41 (280.78)</td><td>491.39 (248.78) 483.45 (230.95)</td><td>H4: Not Supported</td></tr><tr><td>Decision Accuracy</td><td>Interface</td><td>22.954</td><td>.000</td><td></td><td></td><td></td><td></td></tr><tr><td>Decision Accuracy</td><td>Task Complexity</td><td>4948.537</td><td>.000</td><td></td><td></td><td></td><td></td></tr><tr><td>Decision Accuracy</td><td>Spatial Ability</td><td>1.867</td><td>.135</td><td></td><td></td><td></td><td></td></tr><tr><td>Decision Accuracy</td><td>Interface × Task Complexity</td><td>441.994</td><td>.000</td><td>Low Comp. High Comp.</td><td>.595 (.183) .237 (.195)</td><td>.803 (.147) .131 (.168)</td><td>H2a/b: Supported</td></tr><tr><td>Decision Accuracy</td><td>Interface × Spatial Ability</td><td>4.959</td><td>.027</td><td>Low Spatial High Spatial</td><td>.392 (.178) .441 (.197)</td><td>.466 (.161) .468 (.161)</td><td>H5: Supported</td></tr><tr><td>Decision Time</td><td>Interface</td><td>14.980</td><td>.000</td><td></td><td></td><td></td><td></td></tr><tr><td>Decision Time</td><td>Task Complexity</td><td>3396.571</td><td>.000</td><td></td><td></td><td></td><td></td></tr><tr><td>Decision Time</td><td>Spatial Ability</td><td>1.248</td><td>.292</td><td></td><td></td><td></td><td></td></tr><tr><td>Decision Time</td><td>Interface X Task Complexity</td><td>127.597</td><td>.000</td><td>Low Comp. High Comp.</td><td>6.50 (1.63) 18.04 (5.54)</td><td>7.46 (1.78) 15.47 (4.37)</td><td>H3a/b: Contradicted</td></tr><tr><td>Decision Time</td><td>Interface × Spatial Ability</td><td>.144</td><td>.705</td><td>Low Spatial High Spatial</td><td>12.20 (3.69) 12.34 (3.50)</td><td>11.34 (2.96) 11.61 (3.17)</td><td>H6: Not Supported</td></tr></table>

![](/api/attachments/G95EQYUG/fulltext/images/a372cae54c4f99c86c3a0044b26c801297caafcea2befb9fe9f2c1dc3581db9d.jpg)

a. H1a/b: Interface × Task Complexity on Subjective Mental Workload  
![](/api/attachments/G95EQYUG/fulltext/images/45de1bc178498d8ad02ab694c12651df6fdf8496476da70b1109ec152ca60819.jpg)  
b. H2a/b: Interface × Task Complexity on Decision Accuracy  
Figure 2. Graphical Display of Significant Results

![](/api/attachments/G95EQYUG/fulltext/images/809a5c205f31eee69c7d17503c8da02fe6b489ae8b0f375b4805afb7fff4123f.jpg)  
Interface

c. H3a/b: Interface × Task Complexity on Decision Time  
![](/api/attachments/G95EQYUG/fulltext/images/1fa5c5523f70e8bec7a8909ee60b254f097c91dc87f3556ad277ff69066c8e14.jpg)  
d. H5: Interface × Spatial Ability on Decision Accuracy  
Figure 2. Graphical Display of Significant Results (Continued)

The pattern of results for decision time was surprising. Both interface type and task complexity provided significant main effects (spatial ability was not significant). There was also a significant interface × task complexity interaction. Parameter estimate results indicate that subjects using the text-based interface (decision time = 7.46 minutes) were significantly slower than those using the visual interface (decision time = 6.50 minutes) for low complexity problems. In contrast, subjects using the text-based interface (decision time = 15.47 minutes) were significantly faster than those using the visual interface (decision time = 18.04 minutes) when solving high complexity problems. These results were contrary to what was hypothesized in H3a and H3b.

There was a significant spatial ability × interface interaction for decision accuracy (H5) but not for subjective mental workload (H4) or decision time (H6), contrary to expectations. As predicted, the decision accuracy parameter estimates indicated that those with low spatial ability (degree of optimal = .392) had lower decision accuracy compared to those with high spatial ability (degree of optimal = .441) when using the visual interface. On the other hand, those with low spatial ability (degree of optimal = .466) had comparable decision accuracy to those with high spatial ability (degree of optimal = .468) when using the textbased interface.

## Discussion

The experimental results revealed that decision makers using the text-based query interface consistently made better decisions when task complexity was low, while decision makers using the visual query interface performed better when task complexity was high. This suggests that the visual representation of data may be a practical way to support processing of large data sets used by some decision makers, consistent with suggestions in the human-computer interaction literature (e.g., Myers et al. 1996; Wright 1997).

From a theoretical perspective, the notion of matching a specific system capability (e.g., information presentation) to a task is consistent with prior research related to decision-making (Todd and Benbasat 1999) and the theory of cognitive fit (Vessey 1991; Vessey and Galletta 1991). Related to our study, visual interfaces may be particularly beneficial when it is important to examine overall patterns embedded within the data or as a mechanism for reducing large solution sets. However, these visual interfaces appear to be less effective when specific detail is needed or when there are a small number of data points. This may be because they require more physical and cognitive operations in order to directly compare data attributes. Our results are consistent with extensions to the theory of cognitive fit (Vessey 1994) suggesting that design features that leverage perceptual processes may improve decision making for complex tasks— particularly those that are amenable to visual representation.

Matching display properties to the characteristics of the task is fairly straightforward for some decision-making tasks and less so for others. Here, the map metaphor for the home selection task provided a natural match between the user interface and the real world. However, determining an appropriate visual display could be problematic for more abstract tasks (e.g., managerial succession questions) where there is no inherent visual display that conforms to a decision maker’s mental model.

The results of this study also contribute to our theoretical understanding of system design and the notion of restrictiveness introduced by Silver (1991). The Homefinder visual query interface reduced system restrictiveness and increased user control by providing graphical representation, direct manipulation, immediate feedback, and “detail on demand,” thereby allowing decision makers to more effectively navigate a potentially unwieldy data set (e.g., Keim and Kriegel 1994; Myers et al. 1996; Robertson et al. 1993; Shneiderman 1998). The results suggest that it becomes increasingly difficult for users to compare possible solutions amid a large set of data in the more restrictive “write query/see result” textbased approach, resulting in disorientation (Foss 1989; Nielsen 1990), increased SMW (Heo and Hirtle 2001; Hochheiser and Shneiderman 2001), and/or lower performance (Johnson and Payne 1985). In light of the results observed in this research, future research examining the potentially complex relationship between design features and the actual or perceived restrictiveness of both types of interface would be a valuable theoretical addition to this line of inquiry.

This research also makes a contribution to existing knowledge by examining complex task environments. Early research evaluating query design and decision effectiveness focused on tasks that had a single right answer when users formulated an appropriate query (e.g., Suh and Jenkins 1992). Given the complexity of today’s business environment, knowledge workers are more likely to encounter multi-criterion decisionmaking where they are required to compare several attributes against a given set of criteria and make trade-offs in order to reach an optimal solution. Questions such as “Who would be the best candidate to hire?” or “Where should a franchise be located?” are examples of multi-criterion decision-making problems that are similar to the type of task used in this study.

The results suggest that use of a visual query interface fosters greater exploration of the data, leading to a deeper understanding of the best solution. Unlike conventional database querying, the use of starfield displays for visual querying encourages data browsing and may compel users to ask more questions than they might with conventional querying (Keim and Kriege 1994; Spoerri 1993). With visual interfaces, decision makers can quickly test “what if” scenarios and easily discover whether a specific criterion is a strong differentiator from other data points within the feasible solution set. This deeper exploration may help explain the surprising decision time results (H3B) as well. In short, visual query interfaces have the potential to foster and encourage exploration of the underlying data; however, this may manifest itself in greater decision time relative to text-based query interfaces. The good news behind this finding is that decision makers appear to make better decisions as a result, as evidenced by results for decision accuracy under conditions of high complexity.

The results also have important practical implications. End users of today’s advanced database management and retrieval systems are likely to fall across a broad range of functional areas. Such a diverse user base is markedly different from years past, when data management systems were considered the sole responsibility of information systems professionals. As end users’ need to work with large data sets (e.g., those typical of data warehousing and data mining tools applications) continues to increase, user interfaces that are able to improve decision effectiveness represent powerful tools that information systems managers should consider integral to the organization’s technical infrastructure.

In summary, the results suggest that visual interfaces help users see the whole—an important aspect of information visualization. Because the potential bandwidth is higher in visual query interfaces (allowing data to be encoded based on type, color, intensity, spatial attributes, etc.), these interfaces may better support users in filtering information, particularly when the potential solution set is large. They provide managers with an overview of the entire data set, then allow them to filter and drill down to get additional detail only when needed.

## Limitations of the Study

While the results offer interesting insights into the effectiveness of visual querying, a number of limitations must be considered when interpreting the findings. First, the subjects were undergraduate students; thus, the results here may not generalize to a broader population. Criticisms typically associated with the use of undergraduate subjects in experiments center around their domain expertise. In this case, we believed that a home selection task would be salient to a student population because most students (as supported by the results) have prior experience looking for off-campus housing. While the motivation of student subjects is always a potential limitation, comments from subjects during postexperiment debriefing sessions suggested they found the tasks engaging.

Second, the experimental task included a significant geographical component. This was fitting given research indicating that up to 80 percent of all business decisions require geographic data (Mennecke 1997). However, it is possible that the results are interface and task-specific, so care must be taken when generalizing the results to other tasks. Future research should investigate the degree to which the present results are robust across other types of problems.

Third, the subjects were not novices on both interfaces. Instead, they may have had an advantage on the text-based interface. Interestingly, the results suggested that subjective mental workload was actually lower for the visual interface, even though that interface was new to all subjects. Thus, we believe that the results represent a conservative estimate of the potentia benefits associated with use of visual interfaces. Finally, while the text and visual interfaces had comparable functionality and made use of identical data, it is not clear that either interface was optimal (however that might be defined). Future research might address these limitations by extending the current work to different interface styles in order to isolate individual design features and their influence on decision outcomes. For example, a systematic program of research might use specially constructed text-based and visual query interfaces that isolate only one of the design elements embedded in each of the two interfaces (e.g., varying feedback only) vs. the more holistic evaluation approach used in this research.

## Future Research

Given the nascent state of research in this area, there are many additional opportunities for future research. One area for future exploration would be to focus on decision-making processes vs. decision outcomes. One approach would involve using process-tracing techniques to better understand the micro-level cognitive processes associated with how decision makers create mental models of the problem space, construct initial queries, refine those queries, and interpret output in each interface. Similarly, additional research should further investigate the use of the subjective mental workload construct employed in this study. The information systems literature has largely overlooked this construct (see Morris et al. 1999); therefore, future research might investigate the degree to which mental workload explains users’ cognitive reaction to new technologies or designs (for an example of one approach, see Vessey and Galletta 1991). In addition, the measure of mental workload used in this study is, by definition, a subjective evaluation from users. The subjective responses from the NASA-TLX are widely interpreted to represent a user’s actual cognitive load; however, future work might investigate the validity of those subjective evaluations by comparing them with traditional objective measures of workload (e.g., heart rate or other physiological responses).

Other avenues for future research include examining other potential mediating and/or moderating variables. In the current study, we focused on one such individual difference variable, spatial ability, as a possible moderator of individual performance across interfaces. The results showed that decision makers with greater spatial ability had higher decision accuracy using the visual interface than those with lower spatial ability. This suggests that visual query interfaces allow those with higher visual ability to capitalize on their ability; however, text-based interfaces remain neutral with respect to performance across spatia ability levels. Future research might expand the range of individual difference variables included. For example, the Minnesota Clerical Test (Vessey and Galletta 1991) might be used to measure predisposition to detail in an attempt to add additional explanatory power and robustness to the model used in this study.

A final potential avenue for future research would be dissecting the relationship between menta workload and decision strategy. It is tempting to think of mental workload as increasing monotonically with task complexity—in other words, as task complexity increases, the cognitive burden that is placed on the user also rises proportionally. However, this may not necessarily be true. The decision-making literature (e.g., Payne et. al. 1988) suggests that users faced with a changing cost/benefit evaluation (i.e., with increasing complexity) may alter their decision-making strategy and, in the process, alter their perceived mental workload. For example, with a compensatory strategy, as the amount of information to be processed increases, mental workload may also increase because it becomes increasingly difficult to compare alternatives across a wide range of attributes (i.e., a greater number of bits). However, once task complexity becomes too high, decision makers may shift to a non-compensatory strategy. In such cases, their subjective menta workload may actually decrease, despite having to evaluate (at least theoretically) more information. Future research should test this proposition and, if it is valid, determine at what point increased information pushes mental workload to such high levels that decision makers change their decision strategy in order to reduce the cognitive burden. Results from such a study would have broad theoretical and practical implications for practice across a wide range of decision scenarios, particularly those associated with high task complexity/ high risk environments (e.g., air traffic control, financial markets, command and control).

## Conclusions

In sum, the results suggest that the dynamics of the task/solution scenario are an important consideration in the design of query interfaces to support decision making. Particularly when the potential solution set is large, visual query interfaces may help users navigate through a sea of potentially misleading information with greater effectiveness than they could using text-based interfaces. With the explosion of information available through the Internet, data mining tools, and push technologies, the potential of visual query tools to support decision making is compelling, particularly in light of the increased complexity inherent in many of the problems faced by managers in organizations today.

## Acknowledgments

We would like to thank Peter Todd and Jere Brophy for their helpful comments on this paper. We also are grateful to Ilze Zigurs, the Associate Editor, and the reviewers whose comments have improved the quality of the paper substantially.

## References

Ahlberg, C., and Shneiderman, B. “Visual Information Seeking: Tight Coupling of Dynamic Query Filters With Starfield Displays,” in Proceedings of the 1994 SIGCHI Conference, C. Plaisant (ed.), ACM Press, New York, 1994, pp. 313-317.

Ahlberg, C., and Wistrad, E. “IVEE: An Information Visualization and Exploration Environment,” in Proceedings of Information Visualization Symposium 95, N. Gershom and S. Eick (eds.), IEEE Computer Society Press, Los Alamitos, CA, 1995, pp. 66-73.

Allen, B. “Individual Differences and the Conundrums of User-Centered Design: Two Experiments,” Journal of the American Society for Information Sciences (51: 6), April 2000, pp. 508-520.

Au, P., Carey, M., Sewraz, S., Guo, Y., and Ruger, S. M. “New Paradigms in Information Visualization,” in Proceedings of the 23rd Annual International ACM SIGIR Conference on Research and Development in Formation Retrieval, E. Yannakoudakis, N. Belkin, M. Leong, and P. Ingwersen (eds.), ACM Press, New York, 2000, pp. 307-309.

Beach, L. R., and Mitchell, T. R. “A Contingency Model for the Selection of Decision Strategies,” Academy of Management Review (3:3), July 1978, pp. 439-449.

Brasseur, L. “Literacy in the Computer Age: A Complex Perceptual Landscape,” in Computers and Technical Communications: Pedagogical and Programmatic Perspectives, S. Selber (ed.), Ablex, Norwood, NJ, 1997, pp. 75-97.

Campbell, D. J. “Task Complexity: A Review and Analysis,” Academy of Management Review (13:1), January 1988, pp. 40-52.

Card, S. “Visualizing Retrieved Information: A Survey,” IEEE Computer Graphics and Applications (16:2), March 1996, pp. 63-67.

Card, S. K., Mackinlay, J. D., and Shneiderman, B. Readings in Information Visualization: Using Vision to Think, Morgan Kaufmann, San Francisco, 1999.

Card, S. K., Moran, T. P., and Newell, A. The Psychology of Human-Computer Interaction, Lawrence Erlbaum Associates, Hillsdale, NJ, 1983.

Chambers, J., Cleveland, W., Kleiner, B., and Tukey, P. Graphical Methods for Data Analysis, Wadsworth International Group, Belmont, CA, 1983.

Chen, C. Information Visualization and Virtual Environments, Springer-Verlag, London, 1999.

Chen, C., Czerwinski, M., and Macredie, R. “Individual Differences in Virtual Environments - Introduction and Overview,” Journal of the American Society for Information Science (51:6), April 2000, pp. 499-507.

Chen, C., and Rada, R. “Interacting With Hypertext: A Meta-Analysis of Experimental Studies,”

Human-Computer Interaction (11:2), April 1996, pp. 125-156.

Chewning, E. G., and Harrell, A. M. “The Effect of Information Load on Decision Makers’ Cue Utilization Levels and Decision Quality in a Financial Distress Decision Task,” Accounting, Organizations, and Society (15:6), November 1990, pp. 527-542.

Compeau, D. R., and Higgins, C. A. “Computer Self-Efficacy: Development of a Measure and Initial Test,” MIS Quarterly (19:2), June 1995, pp. 189-211.

Cooper, B. L., Watson, H. J., Wixom, B. H., and Goodhue, D. L. “Data Warehousing Supports Corporate Strategy at First American Corporation,” MIS Quarterly (24:4), December 2000, pp. 547-567.

Cribbin, T., and Chen, C. “A Study of Navigation Strategies in Spatial-Semantic Visualizations,” in Proceedings of the 9th International Conference on Human-Computer Interaction, M. Smith, G. Salvendy, D. Harris, and R.J. Koubek (eds.), ACM Press, New York, 2001, pp. 948- 952.

Davenport, T. H., and Beck, J. C. The Attention Economy, Harvard Business School Press, Cambridge, MA, 2001.

Dillon, A. “Spatial-Semantics: How Users Derive Shape from Information Space,” Journal of the American Society for Information Science (51:6), April 2000, pp. 521-528.

Egan, D. E. “Individual Differences in Human Computer Interaction,” in Handbook of Human-Computer Interaction, M. Helander (ed.), North Holland, Amsterdam, 1988, pp. 543-568.

Einhorn, H. J. “Use of Nonlinear, Non-Compensatory Models as a Function of Task and Amount of Information,” Organizational Behavior and Human Performance (6:1), January 1971, pp. 1-27.

Ekstrom, R. B., French, J. W., and Harmon, H. H. Manual for Kit of Factor-Referenced Cognitive Tests, Educational Testing Service, Princeton, NJ, 1976.

Finke, R. A., and Shepard, R. N. “Visual Functions of Mental Imagery,” in Handbook of Perception and Human Performance, K. R. Boff, L. Kauffman, and J. P. Thomas (eds.), Wiley, New York, 1986, pp. 1-55.

Foss, C. L. “Tools for Reading and Browsing Hypertext,” Information Processing and Management (25:4), July 1989, pp. 407-418.

Frese, M. “A Theory of Control and Complexity: Implications for Software Design and Integration of Computer Systems into the Work Place,” in Psychological Issues of Human Computer Interaction in the Work Place, M. Frese, E. Ulich, and W. Dzida (eds.), Elsevier Science, Amsterdam, 1987, pp. 313-337.

Hart, S., and Staveland, L. “Development of NASA-TLX: Results of Empirical and Theoretical Research,” in Advances in Psychology, Vol 52, P. Hancock and N. Meshkati (eds.), North Holland, Amsterdam, 1988, pp. 139-184.

Head, C. G. “The Map as a Natural Language: A Paradigm for Understanding,” in New Insights in Cartographic Communication, C. Board (ed.), University of Toronto Press, Toronto, 1984, pp. 1-36.

Heo, M., and Hirtle, S. C. “An Empirical Comparison of Visualization Tools to Assist Information Retrieval on the Web,” Journal of the American Society for Information Science and Technology (52:8), June 2001, pp. 666-675.

Hochheiser, H., and Shneiderman, B. “Using Interactive Visualizations of WWW Log Data to Characterize Access Patterns and Inform Site Design,” Journal of the American Society for Information Science and Technology (52:4), February 2001, pp. 331-343.

Hutchins, E., Hollan, J., and Norman, D. “Direct Manipulation Interfaces,” in User Centered System Design: New Perspectives on Human-Computer Interaction, D. Norman and S. Draper (eds.), Lawrence-Erlbaum Associates, Hillsdale, NJ, 1986, pp. 87-124.

Jacoby, J., Speller, D. E., and Kohn, C. A. “Brand Choice Behavior as a Function of Information Load,” Journal of Marketing Research (11:1), February 1974a, pp. 532-544.

Jacoby, J., Speller, D. E., and Kohn, C. A. “Brand Choice as a Function of Information Load: Replication and Extension,” Journal of Consumer Research (1:1), June 1974b, pp. 33-42.

Johnson, E. J., and Payne, J. W. “Effort and Accuracy in Choice,” Management Science (31:4), April 1995, pp. 395-414.

Keim, D., and Kriegel, H. “Using Visualization to Support Data Mining of Large Existing Data-

bases,” in IEEE Visualization 93 Workshop: Database Issues for Data Visualization, J. Lee and G. Grinstein (eds.), Springer-Verlag, Berlin, 1994, pp. 210-228.

Kim, J., Hahn, H., and Hahn, J. “How Do We Understand a System With (So) Many Diagrams? Cognitive Integration Processes in Diagrammatic Reasoning,” Information Systems Research (11:3), September 2000, pp. 284-303.

Kirlik, A., Miller, R. A., and Jagacinski, R. J. “Supervisory Control in a Dynamic and Uncertain Environment: A Process Model of Skilled Human-Environment Interaction,” IEEE Transactions on Systems, Man, and Cybernetics (23:4), July/August 1993, pp. 929-952.

Kleinmuntz, D. N., and Schkade, D. A. “Information Displays and Decision Processes,” Psychological Science (4:4), July 1993, pp. 221-227.

Koenemann, J., and Belkin, N. “A Case for Interaction: A Study of Interactive Information Retrieval Behavior and Effectiveness,” in Proceedings of the 1996 SIGCHI Conference, M. Tauber (ed.), ACM Press, New York, 1996, pp. 205-212.

Kosslyn, S. M. “Graphics and Human Information Processing,” Journal of the American Statistical Association (80:391), September 1985, pp. 499-512.

Kosslyn, S. M. “Understanding Charts and Graphs,” Applied Cognitive Psychology (3:2), March 1989, pp. 185-225.

Kumar, H., Plaisant, C., and Shneiderman, B.. “Browsing Hierarchical Data with Multi-Level Dynamic Queries and Pruning,” International Journal of Human Computer Studies (46:1), January 1997, pp. 103-124.

Lohse, G. L. “A Cognitive Model for Understanding Graphical Perception,” Human Computer Interaction (8:4), October, 1993, pp. 353- 388.

Lohse, G. L. “Consumer Eye Movement Patterns on Yellow Pages Advertising,” Journal of Advertising (26:1), Spring 1997a, pp. 61-73.

Lohse, G. L. “The Role of Working Memory on Graphical Information Processing,” Behaviour and Information Technology (16:6), November 1997b, pp. 297-308.

Loy, S. L. “The Interaction Effects Between General Thinking Skills and an Interactive Graphics Based DSS to Support Problem Structuring,” Decision Sciences (22:4), September/October 1991, pp. 846-868.

Mackay, J. M., and Elam, J. J. “A Comparative Study of How Experts and Novices Use a Decision Aid to Solve Problems in Complex Knowledge Domains,” Information Systems Research (3:2), June 1992, pp. 150-172.

March, J., and Simon, H. “Cognitive Limits on Rationality,” in Organizations, J. March and H. Simon (eds.), Wiley and Sons, New York, 1958, pp. 136-171.

McCormick, B. H., DeFanti, T. A., and Brown, M. D. “Visualization in Scientific Computing—A Synopsis,” IEEE Computer Graphics and Applications (7:4), July 1987, pp. 61-70.

Mennecke, B. E. “Understanding the Role of Geographic Information Technologies in Business: Applications and Research Directions,” Journa of Geographic Information and Decision Analysis (1:1), January 1997, pp. 44-68.

Messick, S. Individuality in Learning, Jossey-Bass, San Francisco, 1976.

Miller, G. A. “The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information,” Psychological Review (63:1), January 1956, pp. 81-97.

Mirel, B. “Visualizations for Data Exploration and Analysis: A Critical Review of Usability Research,” Technical Communication (45:4), December 1998, pp. 491-509.

Morris, M. G., Speier, C., and Hoffer, J. A. “An Examination of Procedural and Object-Oriented Systems Analysis Methods: Does Prior Experience Help or Hinder Performance?” Decision Sciences (30:1), Winter 1999, pp. 107 - 136.

Myers, B. A., Holland, J. D., and Cruz, I. F. “Strategic Directions in Human Computer Interaction,” ACM Computing Surveys (28:4), December 1996, pp. 794-809.

Newell, A., and Simon, H. A. Human Problem Solving, Prentice-Hall, Englewood Cliffs, NJ, 1972.

Nielsen, J. Hypertext and Hypermedia, Academia Press, London, 1990.

Norman, D. Things That Make Us Smart, Addison-Wesley, Reading, MA, 1993.

Orford, S., Harris, R., and Dorling, D. “Geography: Information Visualization in the Social Sciences,” Social Science Computer Review (17:3), Fall 1999, pp. 289-304.

Payne, J., Bettman, J. R., and Johnson, E. J. “Adaptive Strategy Selection in Decision Making,” Journal of Experimental Psychology: Learning, Memory, and Cognition (14:3), July 1988, pp. 534-552.

Pinker, S. “A Theory of Graph Comprehension,” in Artificial Intelligence and the Future of Testing, R. Freedle (ed.), Lawrence Erlbaum Associates, Hillsdale, NJ, 1990, pp. 73-126.

Robertson, G. G., Card, S. K., and Mackinlay, J. D. “Information Visualization Using 3-D Interactive Animation,” Communications of the ACM (36:4), April 1993, pp. 56-71.

Robinson, E. P. Jr., and Swink, M. “Reason Based Solutions and the Complexity of Distribution Network Design Problems,” European Journal of Operational Research (76:3), March 1996, pp. 393-409.

Rossano, M. J., and Moak, J. “Spatial Representations from Computer Models: Cognitive Load, Orientation Specificity and the Acquisition of Survey Knowledge,” British Journal of Psychology (89:3), August 1998, pp. 481-497.

Roth, S., Chuah, M., Kerpedjiev, S., Kolojejchick, J., and Lucas, P. “Toward an Information Visualization Workspace,” Human-Computer Interaction (12:1/2), January 1997, pp. 131- 185.

Scerbo, M. W., and Mouloua, M. Automation Technology and Human Performance: Current Research and Trends, Lawrence Erlbaum Associates, Hillsdale, NJ, 1999.

Schkade, D. A., and Kleinmuntz, D. N. “Information Displays and Choice Processes: Differential Effects of Organization, Form, and Sequence,” Organizational Behavior and Human Decision Processes (57:3), March 1994, pp. 319-337.

Scriabin, M., and Vergin, R. C. “Comparison of Computer Algorithms and Visual Based Methods for Plant Layout, Management Science (22:2), February 1975, pp. 172-181.

Shiffrin, R., and Schneider, W. “Controlled and Automatic Human Information Processing: Perceptual Learning, Automatic Attending, and

a General Theory,” Psychological Review (84:2), March 1977, pp. 119-127.

Shneiderman, B. Designing the User Interface: Strategies for Effective Human Computer Interaction (3<sup>rd</sup> Edition), Addison Wesley, Reading, MA, 1998.

Silver, M. S. “Decision Support Systems: Directed and Nondirected Change,” Information Systems Research (1:1), March 1991, pp. 47-70.

Simon, H. A. “Information Processing Models of Cognition,” Annual Review of Psychology (30), 1979, pp. 363-396.

Smelcer, J., and Carmel, E. “The Effectiveness of Different Representations for Managerial Problem Solving: Comparing Maps and Tables,” Decision Sciences (28:2), Spring 1997, pp. 391-420.

Spoerri, A. “InfoCrystal: A Visual Tool for Information Retrieval,” In Proceedings of the Second International Conference on Information and Knowledge Management, B. Bhargava, T. Finin, and Y. Yesha (eds.), ACM Press, New York, 1993, pp. 150-157.

SPSS, Inc. SPSS Advanced Statistics User’s Guide, SPSS, Inc, Chicago, 1990.

Stanney, K. M., and Salvendy, G. “Information Visualization: Assisting Low Spatial Individuals with Information Access Tasks Through the Use of Visual Mediators,” Ergonomics (38:6), June 1995, pp. 1184-1196.

Stasz, C. Planning During Map Learning: The Global Strategies of High and Low Visual-Spatial Individuals (N-1594-ONR), The Rand Corporation, Santa Monica, CA, 1980.

Streufert, S. C. “Effects of Information Relevance on Decision Making in Complex Environments,” Memory and Cognition (1:3), June 1973, pp. 389-403.

Suh, K. S., and Jenkins, A. M. “Comparison of Linear Keyword and Restricted Natural Language Database Interfaces for Novice Users,” Information Systems Research (3:3), September 1992, pp. 252-272.

Swink, M. “The Influences of Task and User Factors on Performance in a Logistics DSS Application,” Decision Sciences (26:4), July/August 1995, pp. 503-529.

Swink, M., and Speier, C. “Presenting Geographic Information: Effects on Data Aggrega-

tion, Dispersion, and Users’ Spatial Orientation,” Decision Sciences (30:1), Winter 1999, pp. 169-196.

Taylor, P. B., and Iwanek, R. “Intuitive Versus Optimal Solutions to Some Problems in Distribution,” OMEGA (8:2), April 1980, pp. 183-192.

Te’eni, D. “Feedback in DSS as a Source of Control: Experiments with the Timing of Feedback,” Decision Sciences (22:3), July/August 1991, pp. 644-655.

Tegarden, D. P. “Business Information Visualization,” Communications of AIS (1:4), January 1999, pp. 1-37.

Todd, P., and Benbasat, I. “Evaluating the Impact of DSS, Cognitive Effort, and Incentives on Strategy Selection,” Information Systems Research (10:4), December 1999, pp. 356-374.

Tufte, E. R. The Visual Display of Quantitative Information., Graphics Press, Chesire, CT, 2001.

Vessey, I. “Cognitive Fit: A Theory-Based Analysis of the Graphs Versus Tables Literature,” Decision Sciences (22:2), Spring 1991, pp. 219-240.

Vessey, I. “The Effect of Information Presentation on Decision Making: A Cost-Benefit Analysis,” Information & Management (27:2), August 1994, pp. 103-119.

Vessey, I., and Galletta, D. “Cognitive Fit: An Empirical Study of Information Acquisition,” Information Systems Research (2:1), March 1991, pp. 63-84.

Ware, C. Information Visualization: Perception for Design, Academic Press, San Diego, CA, 2000.

Wickens, C. D., and Carswell, C. M. “The Proximity Compatibility Principle: Its Psychological Foundation and Relevance to Display Design,” Human Factors (37:3), September 1995, pp. 473-494.

Wierwille, W. W., and Eggemeier, F. T. “Recommendations for Mental Workload Measurement in a Test and Evaluation Environment, Human Factors (35:2), June 1993, pp. 263 -281.

Wixom, B. H., and Watson, H. J. “An Empirical Investigation of the Success Factors for Data Warehousing,” MIS Quarterly (25:1), March 2001, pp. 17-41.

Wood, R. “Task Complexity: Definition of the Construct,” Organizational Behavior and

Human Decision Processes (37:1), February 1986, pp. 60 - 82.

Wright, W. “Business Visualization Applications, IEEE Computer Graphics and Applications (17:4), July/August 1997, pp. 66-70.

## About the Authors

Cheri Speier is an associate professor of Information Systems at Michigan State University. Her research interests include the influence of work environments on decision making, individua acceptance and use of technology, effective user training environments, and the effective use of information technology to support supply chain relationships. Her work has appeared in journals such as MIS Quarterly, Decision Sciences, Organizational Behavior and Human Decision Processes, and the Journal of Marketing, among others. Cheri was awarded the MSU Universitywide Teacher Scholar award in 2001, recognizing her excellence in teaching and research. She earned a Ph.D. in Management Information Systems at Indiana University.

Michael G. Morris is an assistant professor of Commerce within the Information Technology area at the McIntire School of Commerce, University of Virginia. He received his Ph.D. in Management Information Systems from Indiana University in 1996. His research interests can broadly be classified as socio-cognitive aspects of human response to information technology, including user acceptance of information technology, usability engineering, and decision-making. His research has been published in MIS Quarterly, Organizational Behavior and Human Decision Processes, and Personnel Psychology, among others.

## Appendix A

Visual Interface  
![](/api/attachments/G95EQYUG/fulltext/images/c3116940454a82bd11b214b2c3a8769f7cde8e79dda75cc16d45dcfc5c74d4dd.jpg)

## Appendix B

## Text-Based Interface

## Dynamic Home Finder

Section 1: Quadrant and Mileage Information

In order to find out where you would like to live, please enter the information in the following four fields.

After you have finished, continue to Section 2.

## Section 2: Type of Place Desired

![](/api/attachments/G95EQYUG/fulltext/images/d664751ca8061087a054ae9121168bd8ad88b961ba01197255ff176c0bd066ec.jpg)

In order to find you the right home, please answer one of the questions to the right. if you answer question 5, please answer question 5a.

You must enter the information exact. For example, if you want a house you must type House.

After you have finished, continue to Section 3.

## Section 3: Cost and Information

In order for you to recieve the best possible home. please answer each of the questions to the right. This will aid in the selection(s) of your home.

1. Enter the Quadrant for A (1-16): 1

2. Enter the Quadrant for B (1-16):

3. Enter the Distance from A (1-30):

4. Enter the Distance from B (1-30): 1

5. If you are looking for a house, enter House:

5a. Do you want a new House (Y or N):

6. If you are looking for a Townhouse, enter THse::

7. If you are looking for a Condo, enter Condo:

8. How many Bedrooms do you want (1-7):

9. Enter the Minimum Cost Range (from 50k):

10. Enter the Maximum Cost [up to 500k):

11. Do you want a Garage (Y or N)::

12. Do you want a Fireplace (Y or N)::

13. Do you want Central Air (Y or N)::

Execute Query

## Appendix C

## Text-Based Query Output

<table><tr><td></td><td>ID</td><td>Type</td><td>Address</td><td>Neighborhood</td><td>State</td><td>Cost</td><td>Bed</td><td>Fireplace</td><td>Garage</td><td>CentralAir</td><td>NewHome</td></tr><tr><td></td><td>1</td><td>House</td><td>5780 Hamilton Street</td><td>Beltsville,</td><td>MD</td><td>$184,950.00</td><td>4</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>2</td><td>House</td><td>5459 S. Lincoln St.</td><td>Beltsville,</td><td>MD</td><td>$173,950.00</td><td>3</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>3</td><td>House</td><td>6256 Glass Road</td><td>Beltsville,</td><td>MD</td><td>$195,950.00</td><td>6</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>4</td><td>House</td><td>5744 Hamilton Street</td><td>Beltsville,</td><td>MD</td><td>$184,950.00</td><td>3</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>5</td><td>House</td><td>5376 S. Capitol St.</td><td>Beltsville,</td><td>MD</td><td>$162,950.00</td><td>3</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>6</td><td>House</td><td>5816 Hamilton Street</td><td>Beltsville,</td><td>MD</td><td>$184,950.00</td><td>4</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>7</td><td>House</td><td>5400 S. Lincoln St.</td><td>Beltsville,</td><td>MD</td><td>$173,950.00</td><td>4</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>8</td><td>House</td><td>5208 S. Capitol St.</td><td>Beltsville,</td><td>MD</td><td>$162,950.00</td><td>3</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>9</td><td>House</td><td>5064 S. Capitol St.</td><td>Beltsville,</td><td>MD</td><td>$162,950.00</td><td>3</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>10</td><td>House</td><td>5816 Hamilton Street</td><td>Beltsville,</td><td>MD</td><td>$184,950.00</td><td>4</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>11</td><td>House</td><td>5733 Glass Road</td><td>Beltsville,</td><td>MD</td><td>$195,950.00</td><td>6</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>12</td><td>House</td><td>5448 S. Capitol St.</td><td>Beltsville,</td><td>MD</td><td>$162,950.00</td><td>4</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>13</td><td>House</td><td>6147 Rowalt Drive</td><td>Beltsville,</td><td>MD</td><td>$210,950.00</td><td>5</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>14</td><td>House</td><td>5852 Hamilton Street</td><td>Beltsville,</td><td>MD</td><td>$184,950.00</td><td>4</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>15</td><td>House</td><td>6410 Rowalt Drive</td><td>Beltsville,</td><td>MD</td><td>$210,950.00</td><td>6</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>16</td><td>House</td><td>6433 Polk Street</td><td>Beltsville,</td><td>MD</td><td>$221,950.00</td><td>6</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>17</td><td>House</td><td>5621 S. Lincoln St.</td><td>Beltsville,</td><td>MD</td><td>$173,950.00</td><td>3</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>18</td><td>House</td><td>5748 S. Lincoln St.</td><td>Beltsville,</td><td>MD</td><td>$173,950.00</td><td>4</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>19</td><td>House</td><td>5885 Rowalt Drive</td><td>Beltsville,</td><td>MD</td><td>$210,950.00</td><td>5</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>20</td><td>House</td><td>5714 S. Lincoln St.</td><td>Beltsville,</td><td>MD</td><td>$173,950.00</td><td>3</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>21</td><td>House</td><td>6360 Webster Court</td><td>Beltsville,</td><td>MD</td><td>$206,950.00</td><td>6</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>22</td><td>House</td><td>5519 Hamilton Street</td><td>Beltsville,</td><td>MD</td><td>$184,950.00</td><td>3</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>23</td><td>House</td><td>5816 S. Lincoln St.</td><td>Beltsville,</td><td>MD</td><td>$173,950.00</td><td>3</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>24</td><td>THse</td><td>4856 31st Street</td><td>Beltsville,</td><td>MD</td><td>$140,950.00</td><td>2</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td></td><td>25</td><td>THse</td><td>4775 Hapsburg Road</td><td>Beltsville,</td><td>MD</td><td>$136,950.00</td><td>3</td><td>N</td><td>N</td><td>Y</td><td>Y</td></tr></table>

## Appendix D

## NASA Task Load Index

We would like to know about the workload you experienced in performing this task. Feelings of workload can come from several different factors. For example, some people feel that mental or time demands are the most important factors in perceived workload. Others may feel that their performance or amount of frustration is the most important part of their feelings of workload.

Following the box below you will be presented with a series of pairs of items or titles (for example, Effort vs. Mental Demands). You will be asked to choose which of the items was more important to your experience of workload in the task that you just performed. Titles and meanings for each item are presented below.

<table><tr><td>Title</td><td>Descriptions</td></tr><tr><td>Mental Demand</td><td>How much mental and perceptual activity was required (e.g. thinking, deciding, calculating, remembering, looking, searching, etc.)? Was the task easy or demanding, simple or complex, exacting or forgiving?</td></tr><tr><td>Physical Demand</td><td>How much physical activity was required (e.g. pushing, pulling, turning, controlling, activating, etc.)? Was the task easy or demanding, slow or brisk, slack or strenuous, restful or laborious?</td></tr><tr><td>Time Demand</td><td>How much time pressure did you feel due to the rate or pace at which the tasks occurred? Was the pace slow and leisurely or rapid and frantic?</td></tr><tr><td>Performance</td><td>How successful do you think you were in accomplishing the goals of the task? How satisfied were you with your performance in accomplishing these goals?</td></tr><tr><td>Effort</td><td>How hard did you have to work (mentally and physically) to accomplish your level of performance.</td></tr><tr><td>Frustration Level</td><td>Level How insecure, discouraged, irritated, stressed and annoyed versus secure, gratified, content, relaxed and complacent did you feel during the task.</td></tr></table>

On questions 52 through 66, for each pair of titles listed, circle the title that represents the more important contributor to workload for the tasks you performed in this session. (5 dyads listed per page)

52. Effort or Performance

53. Time Demand or Effort

54. Performance or Frustration

55. Physical Demand or Performance

56. Time Demand or Frustration

57. Physical Demand or Frustration

58. Physical Demand or Time Demand

59. Time Demand or Mental Demand

60. Frustration or Effort

61. Performance or Time Demand

62. Mental Demand or Physical Demand

63. Frustration or Mental Demand

64. Performance or Mental Demand

65. Mental Demand or Effort

66. Effort or Physical Demand

For questions 67 through 72, place an “X” on each scale at the point that matches your experience. Each line has two endpoint descriptors that describe the scale. Consider each scale individually. Your ratings will play an important role in the evaluation being conducted, therefore, your participation is greatly appreciated.

## 67. Mental Demand

![](/api/attachments/G95EQYUG/fulltext/images/67ae89ae2b94783efc1faea07cb7aac5738e8d6da52f6a842e47ee8fc3ca43fd.jpg)

## 68. Physical Demand

![](/api/attachments/G95EQYUG/fulltext/images/bac44734eeb3228e556be0d51bcff3786a016e4a8b20478ab6ef7f79b9f73bce.jpg)

## 69. Time Demand

![](/api/attachments/G95EQYUG/fulltext/images/4653b951f9d159b773ef437d812b4b34b175025761c286e954de74492002a324.jpg)

## 70. Performance

![](/api/attachments/G95EQYUG/fulltext/images/7b4f6774e4fadfcfece455d1f560ca34c6c5a200a8f10f33fb2f8b235f267519.jpg)

## 71. Effort

![](/api/attachments/G95EQYUG/fulltext/images/022114d68e21217a8d7d59e6a61ad939966bdb21b2746320f6cf6b3e0b74a5ee.jpg)

## 72. Frustration

![](/api/attachments/G95EQYUG/fulltext/images/a4ee392ecf19f555376d4a30055af0857f02f6ad24c594ccc7edc04d8eb843b0.jpg)
