---
otero_id: 21081
otero_key: "SRGWEDAH"
title: "Implementing and testing a complex interactive MOLP algorithm"
authors: "Charles E. Downing; Jeffrey L. Ringuest"
year: "2002"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00011-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Implementing and testing a complex interactive MOLP algorithm

Charles E. Downing <sup>a,</sup>\*, Jeffrey L. Ringuest <sup>b,1</sup>

<sup>a</sup>Operations Management and Information Systems Department, College of Business, Northern Illinois University, DeKalb, IL 60115, USA

<sup>b</sup>Operations and Strategic Management Department, Wallace E. Carroll School of Management, Boston College, Chestnut Hill, MA 02467, USA

Accepted 1 December 2001

## Abstract

Many business decisions can be modeled as multiobjective linear programming (MOLP) problems. MOLP algorithms seek solutions to these problems by interacting with decision makers to arrive at an acceptable solution. However, due in part to the increasing complexity of these algorithms, and in part to the failure of developers to use graphical user interfaces, testing and comparison of competing algorithms has been minimal. We present herein results of research designed to address this circumstance. Using widely available microcomputer tools, we designed and built a Decision Support System (DSS) capable of running MOLP algorithms, and conducted a field test which asked 98 decision makers to solve a business case using the system. Two algorithms were programmed into the DSS, one a new and more mathematically complex algorithm, and one a previously used benchmark. Results demonstrate that the more complex algorithm was preferred as a decision-making aid over the benchmark. Additionally, results show that users found the DSS equally easy to work with for both algorithms, suggesting that the graphical user interface sufficiently masked the complexity of the new algorithm. This result is encouraging for the possibility of the implementation and testing of increasingly sophisticated MOLP algorithms. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Multiple criteria programming; Decision Support System (DSS); Field test; Behavioral decision making

## 1. Introduction

Having practicing business managers use complex mathematical algorithms has always been a challenge for Decision Support System (DSS) developers [22]. The field of multiobjective linear programming (MO

LP) produces algorithms that need human interaction to be used at all. Not surprisingly, development of usable software, which allows for the testing of MOLP algorithms, is a need continually cited in the literature [7,12,16]. Often, more complex algorithms are not received favorably by users, at least in part because the user interface does not mask their complexity. Users therefore gravitate to simpler algorithms. In fact, Turban and Aronson [22,p.86] state ‘‘An inconvenient user interface is one of the major reasons why managers have not used computers and quantitative analyses to the extent that these technologies have been available’’. A major opportunity exists for implementing and testing more complex MOLP algorithms if user interface concerns can be alleviated.

This paper demonstrates that currently available microcomputer software (see, e.g., Ref. [2]) can be used to implement and test MOLP algorithms with a user interface which masks the complexity of the algorithms. Two algorithms are implemented and tested using Visual Basic for Applications in Microsoft Excel. The first algorithm is a new, more complex algorithm and the second a simpler, benchmark algorithm. Significantly, users found the new algorithm to be a superior decision-making aid. Despite the fact that the more complex algorithm would prove to be more difficult to use on paper or on a system with an inconvenient interface, the users in our implementation rated it just as easy to use as the benchmark algorithm. This result supports the assertion that a convenient user interface will allow for the use of more complex algorithms in the field of MOLP.

## 2. Multiobjective linear programming

Optimal solutions to problems with a single linear mathematical objective can readily be found. For managers looking for the most profit, least cost, etc., these solutions are highly desirable. A major reason such solutions are not calculated with greater regularity in actual settings is that problems often contain more than one objective. Hence, numerous algorithms have been presented which seek solutions to problems with multiple linear objectives (see, e.g., Refs. [4,8,10,14,15, 19, 24,25]). Termed ‘‘Multiojbective Linear Programs (MOLP)’’, these problems do not have a single optimal solution; instead, algorithms for these problems rely on subjective input from human decision makers familiar with the problem at hand to reach an acceptable solution.

Multiobjective linear programming problems occur when two or more incommensurate linear objectives are to be optimized simultaneously subject to a set of linear constraints. The problem may be written mathematically as:

Optimize zðxÞ

Subject to gðxÞV b

$$
\mathbf {x} \geq 0
$$

where z(x) is a vector of m linear objective functions, g(x) is a vector of n linear constraints, b is a vector of n constants, and x is a vector of p real valued decision variables.

This problem is fundamentally different from single objective optimization problems. In the multiobjective problem, the optimal solution is that solution which yields a vector of objective function values, which is most preferred by the decision maker. This implies that subjective input is required from the decision maker. Perhaps the best way to incorporate this subjective information in the solution procedure is via interactive algorithms. Interactive algorithms are analogous to the search techniques that are commonly used in single objective nonlinear optimization. In search algorithms, a promising search direction is determined mathematically and the feasible region is explored in that direction in an attempt to find improved solutions. The search ends after a prescribed number of explorations fails to find an improved solution. In interactive algorithms, the search direction is determined from preference information that is elicited from the decision maker. The feasible region is then searched in this direction. The process is repeated until the decision maker is satisfied with the solution or until no improvement is made in the solution for a pre-specified number of iterations. The algorithms which employ this interactive strategy are too numerous to review here, but they have been reviewed and summarized previously (Refs. [1,7,8,10,12,16,19] and others).

Most of the interactive algorithms for multiobjective linear programming problems are based on the idea of maximizing the decision maker’s value function over the set of objectives. Thus, they assume a rational decision maker. In particular, they often assume that the decision maker has complete knowledge of the problem and that they are consistent and coherent during the decision-making process. Behavioral researchers as far back as Simon [17] have, however, questioned this notion of a rational decision maker and, more recently, Huber et al. [9] and Simonson and Tversky [18] have conducted experiments in which they observed decision maker behavior which is inconsistent with value maximization. Based on these results, Tversky and Simonson [23] have developed an alternative to value maximization, which they call the componential context model.

Tversky and Simonson hypothesize that decision makers evaluate choices based on both the background and local context of the problem. In their model, the background context is defined by the options previously available to the decision maker, and the local context is defined by the options currently available to the decision maker. Tversky and Simonson capture the effect of the background context by combining the various objectives in a simple linear weighting model. They capture the effect of the local context by computing the relative advantage between pairs of alternatives. The relative advantage is measured as the sum of the standardized objective function improvements divided by the sum of the standardized objective function improvements plus the sum of the standardized objective function degradations. Tversky and Simonson have shown that their componential context model can account for observed decision maker behavior. Building on the work of Tversky and Simonson, Ringuest and Downing [15] have developed an interactive algorithm for multiobjective linear programming problems which explicitly considers the background and local contexts of the decision problem.

Once an interactive algorithm has been developed, the construction of software for the implementation of the algorithm provides some interesting challenges. Interactive algorithms ask the decision maker to provide input to the solution algorithm and to interpret output from the solution algorithm continually throughout the solution process. Thus, these inputs and outputs must be formatted so that they are intuitive and easy for the decision maker to use. Spreadsheet software would seem to be a natural vehicle for implementing interactive algorithms [21]. Yet, to date, there are very few examples of spreadsheet implementations of interactive algorithms (see Ref. [13] for a notable exception). In this paper, we present and test a spread sheet-based DSS implementation of the Ringuest and Downing algorithm.

## 3. The algorithm: MOLP with context-dependent preferences

The componential context model is appropriate for problems with a discrete set of alternatives. Ringuest and Downing [15] have developed an algorithm for solving multiobjective linear programming problems which follows the logic of the componential context model. As with the componential context model, Ringuest and Downing’s algorithm captures both the background and local contexts. For a detailed description of the algorithm, see Ref. [15].

The Ringuest and Downing algorithm, hereafter referred to as $^ { \mathrm { \sc ~ \sc ~ C O N T E X T } } { \mathrm { \sc , } }$ , can be summarized as follows.

(1) Ask the decision maker to rank or rate the objectives.

(2) Formulate and solve the linear compromise program.

(3) Present to the decision maker the objective function vector found from solving the linear compromise program (the first iteration) or the linear fractional program (each subsequent iteration). Ask the decision maker which objective function values they would like to improve on, which they are willing to allow to degrade, and which they would like to remain at their current levels. Give the decision maker the option of specifying a maximum percentage of degradation for any objective they are willing to allow to degrade.

(4) Formulate and solve the linear fractional program.

(5) Ask the decision maker if he/she is satisfied with the current solution. If he/she is, terminate the algorithm. If he/she is not, return to step 3.

## 4. Implementation

As stated previously, development of usable software which allows for the testing of MOLP algorithms is a need continually cited in the literature [7,12,16]. Therefore, we wanted to determine whether this algorithm could be implemented and used successfully on a mainstream computer spreadsheet package using DSS tools. The heavy decision maker involvement required with this, and in fact every other, interactive multiobjective linear programming algorithm necessitates that some sort of intuitive interface be provided to the decision maker. Ideally, that interface would not be a distraction to the decision maker, i.e., he/she would be able to give full attention to the problem at hand, and understanding or manipulating the computer program which runs the algorithm would require little attention. This point is often overlooked in the testing of multiobjective linear programming algorithms, and we see this as a critical oversight. If a user is consumed with the basic operations of an algorithm’s implementation, it is unlikely that he/she will be able to give the subtleties of the problem the intended thought, and confounding factors could influence the user’s satisfaction with the algorithm involved or the solutions achieved.

To avoid such confounding factors, we endeavored to make our DSS as simple as possible for the decision maker. We implemented our algorithm on one of the most widely used computer spreadsheet packages in the world, Microsoft Excel. Excel has a built-in optimization utility called Solver, which can solve linear programs. Further, to accommodate those individuals who had no experience with Excel, using the DSS tools inherent in Visual Basic, we created a Graphical User Interface (GUI) that was independent of the basic functioning of Excel. In other words, if a user could perform computer mouse operations (e.g., point and click), he/she could use our interface. Thus, the entire instruction set for our DSS can be summarized in the following three steps: (1) open Excel (make sure Solver is initialized), (2) go under the ‘‘Tools’’ menu and choose ‘‘Context’’, and (3) follow the instructions which come up, pointing, clicking, and entering input as requested.

After the user has selected ‘‘Context’’, he/she is taken via the GUI through the five steps of the CON-TEXT algorithm as outlined in Section 3. A flowchart depiction of the program flow of the DSS is shown in Fig. 1. Note that steps where the user sees a screen and is requested to input information are double-outlined. Full pictures of these screens are shown in subsequent figures.

The computer implementation of the algorithm was nearly as simple as following this flowchart, due to the advanced features of Visual Basic. Where user input was required, a ‘‘Dialog Box’’ was designed to take the input. Designing a Dialog Box is straightforward. The designer need only ‘‘drag’’ and ‘‘drop’’ with his/ her mouse to define areas for user input, areas where messages to users will be printed, etc. The result is input areas similar to those shown in Figs. 2–7. All of the standard functions of a GUI (i.e., mouse compatibility) are built into the interface automatically. The designer can therefore concentrate on the intuitiveness and flow of the template. Simple BASIC-like code is then used to call the various Dialog Boxes, as well as to invoke Solver at the appropriate times. Our experience with the ease of design, as well as the mainstream nature of an Excel spreadsheet, suggests that this method of implementation would be useful for many complex algorithms which require heavy decision maker input.

![](/api/attachments/SRGWEDAH/fulltext/images/1e788dc11eff68dac8412b34ef130f536585aa02d7783858b0754386ca6e72fc.jpg)  
Fig. 1. Flow of the algorithm within the spreadsheet implementation.

## 5. Sample problem

In order to show an outline of the basic multicriteria analysis performed with our CONTEXT DSS, we use a small sample decision problem. The situational context is a fictitious international toy manufacturing company. The company has hired a decision maker to coordinate the advertising campaign for one of their new products. Upper management has told the decision maker to maximize three objectives:

(1) Potential Purchase Families Reached.

(2) Potential Unit Sales.

(3) Benefit/Cost of Advertising Efforts.

An example of the linear programming formulation, unseen by the decision maker, appears below. The three objectives are represented as $z _ { 1 } - z _ { 3 }$ in this formulation:

Maximize

$$
z _ {1} = x _ {1} + 9 x _ {2} + 1 0 x _ {3} + x _ {4} + 3 x _ {5}
$$

$$
z _ {2} = 9 x _ {1} + 2 x _ {2} + 2 x _ {3} + 7 x _ {4} + 4 x _ {5}
$$

$$
z _ {3} = 4 x _ {1} + 6 x _ {2} + 7 x _ {3} + 4 x _ {4} + 8 x _ {5}
$$

Subject to

$$
3 x _ {1} + 9 x _ {2} + 9 x _ {3} + 5 x _ {4} + 3 x _ {5} \leq 1 0 3 9
$$

$$
- 4 x _ {1} + - 1 x _ {2} + 3 x _ {3} + - 3 x _ {4} + - 2 x _ {5} \leq 9 4
$$

$$
3 x _ {1} + - 9 x _ {2} + - 9 x _ {3} + - 4 x _ {4} + 0 x _ {5} \leq 6 1
$$

$$
5 x _ {1} + 9 x _ {2} + 1 0 x _ {3} + x _ {4} + - 2 x _ {5} \leq 9 2 4
$$

$$
3 x _ {1} + - 3 x _ {2} + 0 x _ {3} + x _ {4} + 5 x _ {5} \leq 4 2 0
$$

$$
x _ {1}, x _ {2}, x _ {3}, x _ {4}, x _ {5} \geq 0
$$

The decision maker is informed that a computerized decision support system will aid in his/her efforts, and is given our user-friendly DSS. In this particular example, the menu choice for the CONTEXT method is ‘‘East method’’, as the method is being disguised for comparison purposes. This comparison will be described in Section 6. After he/she chooses ‘‘Tools’’ and then ‘‘East method’’, the decision maker is presented with the screen shown in Fig. 2.

This screen presents the user with the so-called ‘‘pay-off matrix’’ [19], or as we have titled it ‘‘Payoff Table’’, and additionally asks the DM to rank the three objectives. The Payoff Table is constructed by optimizing each objective function separately. The final result shown is a table containing values of all the objective functions (rows) obtained while solving each single objective problem (columns) one at a time. This table tells the DM how high an objective can go, as well as how low, thereby helping the DM to understand the conflict between different objectives, as well as providing a framework within which to work. For example, in the table shown, unit Sales can get as large as 1879.00 (K), or as small as 511.00 (K). The ‘‘Max #2’’ column means ‘‘what would happen if all resources were dedicated to getting the best value for objective (2) (Sales)’’? The answer from the table is ‘‘The company would get 1879.00 (K) in unit Sales, would reach 243.17 (K) Potential Purchase Families, and would have 972.67 Sales for every \$100 spent in advertising.’’ Similarly, if Potential Purchase Families reached (objective (1)) were maximized, the company would only have 511.00 (K) in unit Sales.

Our decision maker now needs to decide the order of importance of these objectives. As shown in Fig. 2, in this example, he/she has placed a premium on the Benefit/Cost Ratio of Advertising Efforts (ranked #1), ranked Sales as the second most important objective, and ranked Potential Purchase Families Reached as third. He/she then clicks on the ‘‘OK’’ button with the computer’s mouse, and is presented with Fig. 3.

Thus, the solution to the linear compromise program yields 1039.00 (K) Potential Purchase Families Reached, 656.63 (K) in unit Sales, and 1459.00 Sales/ \$100 in Advertising. The DM, of course, is not required to know anything about the linear compromise program. He/she is only requested to decide whether these values are acceptable.

![](/api/attachments/SRGWEDAH/fulltext/images/7915b0cce36bdd4ffc145ec865144be5e5f26ed5d7c3e58885b07019147823e8.jpg)  
Fig. 2. User interface for ranking of objectives.

In this example, the DM is not satisfied and uses the mouse to click on the ‘‘No’’ button and is then presented with Fig. 4. This screen, the ‘‘Log of Solutions’’, is used to remind the DM of the original payoff table and previous solutions, and to request subsequent input from the DM. Input is taken in the bottom portion of the screen, where the DM is asked which objectives should increase or stay the same, and which can be allowed to decrease. Of those that can decrease, the DM is given the option of specifying a maximum percentage of decrease.

Our decision maker notices that Sales are fairly low (656.63 K units out of a possible 1879.00 K) and believes this number needs improvement, and correspondingly selects ‘‘Up’’ for the Sales objective. In return, he/she is willing to allow both Families and Sales/\$100 to decrease. In particular, the DM is willing to allow Families to decrease by as much as 40%, but is only willing to allow Sales/\$100 (his/her most important objective) to decrease by 5%. After completing this information as shown, the DM clicks on ‘‘Run the Method’’ and the linear fractional program is solved. Again, the DM need not be concerned about the mathematical method involved, but instead is presented with a screen similar to Fig. 3, this time yielding objective values of Families (K) = 966.05, Sales (K) = 879.53, and Sales/\$100 = 1386.05.

![](/api/attachments/SRGWEDAH/fulltext/images/485860785fed67e0383da1cdd46bbc49b7974b0478a32565bc01c72fde147966.jpg)  
Fig. 3. Solution presentation.

Again, in this example, the DM is not satisfied and clicks on ‘‘No’’ to get the solution log and input screen. The DM is still not satisfied with the Sales number and subsequently chooses ‘‘Up’’ for that objective, and is willing to allow Families to decrease but would like Sales/\$100 to remain the same. Having these aspirations results in a nonfeasible solution for the linear fractional program, and the DM is shown the screen in Fig. 5. After clicking ‘‘OK’’, the DM is returned to a screen similar to Fig. 4, with his/her aspirations still displayed at the bottom as a reminder of the unrealistic request.

Our decision maker changes the ‘‘Same’’ request for Sales/\$100 to ‘‘Down by at Most 5%’’ in hopes of achieving a larger Sales value, and clicks ‘‘Run the Method’’. This action results in a screen similar to Fig. 3 with objective values of Families (K) = 896.75,

![](/api/attachments/SRGWEDAH/fulltext/images/55e3a3ee39fad7d3d32d80123feff7fa5750023b9c0facb3df27a7752ef06ee1.jpg)  
Fig. 4. User interface for solution log and movement of objective values.

Sales (K) = 1091.29, and Sales/\$100 = 1316.75. As a final step, the DM would like Families to increase, and is willing to trade a 9% decrease (at most) in Sales and a 15% decrease (at most) in Sales/\$100. This step results in a solution with which the DM is satisfied, having final objective values of Families (K) = 949.99, Sales (K) = 993.07, and Sales/\$100 =

![](/api/attachments/SRGWEDAH/fulltext/images/562fc70ed66de30cbd06da2e9391fe2255d9e2b90271bd9fcc66afe4d2b43a3b.jpg)  
Fig. 5. Message to user when specifications result in no feasible solution.

1230.73. The final ‘‘Log of Solutions’’ that the DM sees is shown in Fig. 6. He/she has seen this identical screen after each iteration, with information under ‘‘Trials’’ building cumulatively.

Notice that this screen contains a history of the entire process, except for a record of ‘‘Down by at Most’’ percentages, which can be viewed by the DM by clicking on ‘‘See Percentage Log’’. The final ‘‘Log of Percentages Used’’ for this example is shown in Fig. 7.

The log screens permit the running of seven successful trials, but it is important to note that the DM is free to go under ‘‘Tools’’ and run the method as many times as he/she chooses. As such, there is no functional limit on how many trials the DM may perform to arrive at an acceptable solution.

## 6. CONTEXT versus STEM: a field test

To help determine whether our DSS was truly ‘‘easy to use’’, we conducted a full scale field test in which we asked 98 decision makers to use the system

![](/api/attachments/SRGWEDAH/fulltext/images/926f0e32c2bdb310c28cb84dc7df45ad5e1546eeec0d0a4e944f7fc95ed93d00.jpg)  
Fig. 6. Solution log after four successful iterations.

to seek acceptable objective values for a problem in a simulated business environment. The problem scenario was the toy manufacturing company described in the previous section, and the coefficients for the multiobjective linear programming problems were randomly generated using Steuer’s ADBASE Code [20]. Each problem had three objectives, five constraints and five variables. All objective function coefficients were positive and 90% of the constraint coefficients were nonzero. For a benchmark comparison, we also implemented and field-tested the less complex step method. For consistency, we implemented this algorithm on a spreadsheet DSS, which was nearly identical to the one described for the CONTEXT method.

![](/api/attachments/SRGWEDAH/fulltext/images/6db5d0cd78248d90bc6e73d92361475de848cfe0448f8d7b3170388d4b5547da.jpg)  
Fig. 7. Percentage log—history of ‘‘down by at most’’ percentages entered by user.

The step method (STEM) was proposed by Benayoun et al. [4]. In this method, the decision maker is asked at each step to react to compromise solutions found by solving a weighted min–max problem (i.e., finding a solution which is closest to the ideal solution in the min–max sense). The interaction scheme requires the decision maker to specify which objectives in the solution can be degraded so that the levels of unsatisfactory objectives can be improved. The decision maker is also asked to specify the amount by which the satisfactory objectives can be degraded. This information is used to compute the weights used in the problem formulation. STEM requires the same decision maker input as are required in step 2 and all subsequent steps of CONTEXT. STEM differs from CONTEXT primarily in that it is not based on any specific model of decision maker behavior, whereas CONTEXT is based on the componential context model.

Similar to experiments conducted by Buchanan [5], the experiences of the decision makers with the algorithms and the interface were measured using six criteria:

C1: The decision maker’s confidence in the final solution.

C2: Ease of use of the method.

C3: Ease of understanding the method.

C4: Ability of the method to aid in decision making.

C5: Number of iterations.

C6: Elapsed time (seconds).

Measures C1 through C4 were obtained by having the decision makers complete a survey after using each method. Each criterion was measured on a 1 to 7 scale, with ‘‘7’’ being the strongest response (e.g., if a decision maker marked ‘‘7’’ for C1, he/she would be ‘‘extremely satisfied’’ with the final solution). Further, qualitative comments were solicited. It should be noted that when measuring constructs such as user satisfaction the literature reveals several valid instruments [3,6,11], but Buchanan’s survey was chosen for this study since it has been utilized previously with success in the field of MOLP.

Measures C5 and C6 were automatically recorded by the DSS. For each algorithm, an iteration was counted when the decision maker’s inputs resulted in a new feasible solution. With either of the algorithms, it is possible for the decision maker to provide inputs that result in infeasible solutions (e.g., ask for all objectives to be simultaneously improved). In these cases, a warning message was displayed and the decision maker was asked to provide new inputs. Only when the decision maker provided inputs which resulted in a new feasible solution was an iteration counted for either algorithm. Elapsed time was also measured in a consistent manner for both algorithms. With each method, the timer began when the decision maker clicked on the ‘‘Run the Method’’ button (shown in Fig. 4) and stopped after the decision maker reached his/her final feasible solution. Thus, any unsuccessful trials after the final feasible solution were not counted in the elapsed time. Additionally, it should be noted that this method of timing did not capture payoff table calculation time, initial solution time, or any initial ‘‘thinking time’’ of the decision maker.

Graduate business students at the Master’s level were selected to be the decision makers of the experiment. Two pilot studies were run prior to the full field test, which is reported in this paper. The first pilot study was conducted in a laboratory equipped with 11 personal computers on which our DSS had been loaded. Training was done individually as each of 16 participants entered the laboratory. Each decision maker was asked to analyze a case using the DSS and to fill out a survey before leaving the laboratory.

The second pilot was run as a ‘‘virtual laboratory’’. A different group of 13 decision makers were given a diskette which contained the decision support system, along with printed copies of instructions and the survey. Then, they sat through a group training session. At the end of the session, the decision makers were asked to go to a public computer facility on campus or to their own personal work station (i.e., to use whatever system they typically used) to analyze the same case that was used in the prior pilot study. Eleven decision makers returned the disk and a completed survey by the specified deadline (a period of 1 week). The results of the two pilot studies were statistically compared. These tests showed that the virtual environment did not significantly alter the results.

The full study was administered to a third group of 120 potential decision makers, on a voluntary basis. These individuals received over an hour of training, mostly dealing with the context of the business situation being examined, and the process of completing the exercise. This training was developed from the pilot studies. Little training was needed on the use of the DSS interface. A disk containing a copy of our DSS and a problem scenario was given to each decision maker. To match the context of the case, two different mathematical scenarios were generated using Steuer’s problem generator. These mathematical programs were described as modeling the design of two different regional advertising campaigns, in two different geographic regions, labeled on the interface simply as ‘‘East’’ and ‘‘West’’. The East method was the CONTEXT algorithm, and the West method was the benchmark algorithm. Decision makers were asked to solve the problem for each region (meaning they would use both algorithms). Half of the decision makers did the East method first, and half of the decision makers did the West method first. This division was accomplished by having ‘‘East’’ appear first on the toolbar of half of the systems, and ‘‘West’’ appear first on the toolbar of the other half. Additionally, the two mathematical scenarios that were generated were equally split between the two algorithms. The final result was a symmetric division of four possible cases: decision makers who used East first on Scenario 1 followed by West on Scenario 2, decision makers who used East first on Scenario 2 followed by West on Scenario 1, decision makers who used West first on Scenario 1 followed by East on Scenario 2, and decision makers who used West first on Scenario 2 followed by East on Scenario 1. Thus, all 98 participating decision makers had the opportunity to use both algorithms. Parametric paired difference testing, comparing responses concerning the East method versus those concerning the West method, was used due to the significant sample size.

Ninety-eight surveys were returned; two-diskettes were deemed unusable, leaving 96 data points for C5 and C6. These 96 disks were analyzed both systematically (virus detection software) and qualitatively (by speaking directly to the decision makers) in an attempt to determine that the data therein was of high quality. However, it is important to note that, while the authors are confident that the graduate students who served as decision makers for this study took the study seriously, there is no such guarantee whenever human subjects are used. The means for each method for each criterion, as well as the p values for the paired difference experiments, appear in Table 1. All testing was one-tailed, with $\mathrm { H } _ { 0 }$ being that the two means were equal, and the alternate hypothesis being that the CONTEXT method was preferred.

As shown, our subjects stated that they had significantly $( p < 0 . 0 5 2 )$ more confidence in the final solution that they obtained with the CONTEXT method as compared to the final solution that they obtained with STEM. Since both means were close to 4, additional tests were conducted comparing the CONTEXT mean to 4 and the STEM mean to 4. Results showed that the CONTEXT mean was greater than 4 $( p { < } 0 . 0 1 1 )$ and the STEM mean was not $( p < 0 . 3 5 0 )$

In addition, it took our subjects significantly $( p <$ 0.000) fewer iterations, on average, to reach a satisfactory solution with the CONTEXT method than with STEM. Finally, the average elapsed time for the CONTEXT method was significantly $( p < 0 . 0 0 1 )$ less than that for STEM. These facts, along with qualitative information gathered from the surveys, imply that decision makers were able to reach satisfactory solutions faster with the CONTEXT method, possibly due to the algorithm’s ability to account for problem context. Further testing would be required to prove that this is in fact the cause.

CONTEXT versus STEM: mean and p values for each criterion

<table><tr><td></td><td>CONTEXT mean</td><td>STEM mean</td><td>p value: paired t-test</td></tr><tr><td>C1: Confidence in the final solutiona</td><td>4.45</td><td>4.07</td><td>0.052</td></tr><tr><td>C2: Ease of usea</td><td>5.10</td><td>4.80</td><td>0.068</td></tr><tr><td>C3: Ease of understandinga</td><td>4.95</td><td>4.61</td><td>0.065</td></tr><tr><td>C4: Aid in decision makinga</td><td>4.40</td><td>4.07</td><td>0.071</td></tr><tr><td>C5: Number of iterationsb</td><td>3.16</td><td>5.49</td><td>0.000</td></tr><tr><td>C6: Elapsed time (seconds)b</td><td>220</td><td>350</td><td>0.001</td></tr></table>

Degrees of freedom for C1 through $\mathrm { C } 4 = n - 1 = 9 7 .$  
Degrees of freedom for C5 and $C 6 = n - 1 = 9 5 .$  
<sup>a</sup> Measured on a 1 to 7 scale, where $" 7 "$ is ‘‘very confident’’, etc. $\operatorname { H } _ { 0 } { \mathrm { : } }$ CONTEXT mean = STEM mean. $\operatorname { H } _ { \mathrm { a } } \colon$ CONTEXT mean > STEM mean.  
b $\operatorname { H } _ { 0 } { \mathrm { : } }$ CONTEXT mean = STEM mean. $\mathrm { H } _ { \mathrm { a } } \colon$ CONTEXT mean < STEM mean.

More important to this study is the fact that these results show no significant differences between the CONTEXT method and STEM for criteria C2 and C3. These two criteria could be interpreted as the ‘‘DSS interface’’ criteria. Since the mathematics of the algorithms have essentially been hidden from the decision makers, when asked about ‘‘Ease of Use’’ and ‘‘Ease of Understanding’’, it follows that the response would be based primarily on the ease of the interface. Thus, the ‘‘no difference’’ result between the two algorithms is expected, and in fact desired. Even though the CONTEXT method is more complex mathematically, the users found both methods (and both interfaces) to be equally easy to use and understand. This result suggests that the DSS is an agreeable interface for decision makers in multi-criteria situations. Further, we should note that during the time frame when users were running the algorithms and completing the surveys, questions concerning usage of the DSS template were almost nonexistent. We handed out 98 computer disks containing the DSS template and received 96 usable disks at the end of the study. The two unusable disks were deemed such due to virus corruption and not because of any problem with the system.

## 7. Summary and conclusions

In this paper, we have presented a DSS spreadsheet implementation of the CONTEXT method. The CONTEXT method is a new and advanced multiobjective linear programming algorithm that accounts for decision maker behavior. Using the features of Visual Basic for Applications and Solver in Microsoft Excel, we built and tested a decision support system for decision makers to use to attempt to reach satisfactory solutions to problems with multiple, conflicting objectives. Additionally, we implemented an established algorithm, STEM, in the system as well. For comparison, we had 96 users apply the two disguised methods to a hypothetical business case. Results show that the CONTEXT method is preferred to STEM by decision makers for having confidence in the final solution, but that it is no more difficult to use than the less complex STEM. Further, due to the intuitive nature of the system, training and start-up of the project was seamless, and operational questions during the process were minimal. These tests suggest that, given the current capabilities of user-friendly Decision Support System (DSS) tools, algorithm development and testing need not be inhibited. In particular, the following observations should be noted:

. Users and developers found the DSS equally easy to use and understand for both algorithms. This fact demonstrates that complex algorithms can be masked by the user interfaces of such systems, and that testing and development volume and speed can increase.

. Users were more confident with their final solution and arrived at their solution faster using the complex algorithm. This fact demonstrates that a theoretically ‘‘better’’ algorithm did not meet user resistance due to its complexity.

. Implementation, user training, and the field experiment were successful and relatively painless using the microcomputer packages. This fact demonstrates that algorithm developers can rapidly prototype and beta test new algorithms.

. The CONTEXT algorithm was shown to be superior to a previously established algorithm, STEM. Care should be taken, however, to note that these results were based on small problems with three objectives and five constraints.

The first three observations give reason to believe that the cycle of slow or nontesting and development of complex MOLP algorithms can be broken. The fourth gives credibility to a new algorithm.

## References

[1] Y. Aksoy, Interactive multiple objective decision making: a bibliography (1965 – 1988), Management Research News 13 (1990) 1 – 8.

[2] A. Angehrn, T. Jelassi, DSS research and practice in perspective, Decision Support Systems 12 (4) (November 1994) 267 – 275.

[3] J.E. Bailey, S.W. Pearson, Development of a tool for measuring and analyzing computer user satisfaction, Management Science 29 (5) (1983) 530 – 545.

[4] R. Benayoun, J. DeMontgolfier, J. Tergny, O. Laritchev, Linear programming with multiple objective functions: STEP-method (STEM), Mathematical Programming 1 (1971) 366 – 375.

[5] J.T. Buchanan, An experimental evaluation of interactive MCDM methods and the decision making process, Journal of the Operational Research Society 9 (1994) 1050–1059.

[6] W.J. Doll, G. Torkzadeh, The measurement of end-user computing satisfaction, MIS Quarterly 12 (2) (1988) 259 – 274.

[7] J.S. Dyer, P.C. Fishburn, R.E. Steuer, J. Wallenius, S. Zionts, Multiple criteria decision making, multiattribute utility theory: the next ten years, Management Science 38 (1992) 645– 654.

[8] G.W. Evans, An overview of techniques for solving multiobjective mathematical programs, Management Science 30 (1984) 1268– 1282.

[9] J.J. Huber, W. Payne, C. Pluto, Adding asymmetrically dominated alternatives: violations of regularity and the similarity hypotheses, Journal of Consumer Research 9 (1982) 90–98.

[10] C.L. Hwang, A.S.M. Masud, Multiple Objective Decision Making: Methods and Applications, Springer-Verlag, New York, 1976.

[11] B. Ives, M. Olson, J.J. Baroudi, The Measurement of User Information Satisfaction, Communications of the ACM 26 (10) (1983) 785– 794.

[12] P. Korhonen, H. Moskowitz, J. Wallenius, Multiple criteria decision support, European Journal of Operational Research 63 (1992) 361 – 375.

[13] J. Korycki, W. Ogryczak, A Spreadsheet Implementation of Aspiration/Reservation Based Decision Support, Clemson University, Clemson, SC, 1995.

[14] J.L. Ringuest, Multiobjective Optimization: Behavioral and Computational Considerations, Kluwer Academic Publishing, Boston, 1992.

[15] J.L. Ringuest, C.E. Downing, Multiobjective linear programming with context-dependent preferences, Journal of the Operational Research Society 48 (7) (1997) 714 – 725.

[16] W.S. Shin, A. Ravindran, Interactive multiple objective optimization: survey I. Continuous case, Computers and Operations Research 18 (1991) 97– 114.

[17] H.A. Simon, Models of Man, Macmillan, New York, 1957.

[18] I. Simonson, A. Tversky, Choice in context: tradeoff in contrasts and extremeness aversion, Journal of Marketing Re search 29 (1992) 281 – 295.

[19] R.E. Steuer, Multiple Criteria Optimization: Theory, Computation, and Application, Wiley, New York, 1986.

[20] R.E. Steuer, Manual for the ADBASE Multiple Objective Linear Programming Package, Faculty of Management Science, University of Georgia, Athens, Georgia, 1995.

[21] M.D. Trout, S.K. Tadisina, R.J. Clinton, Interactive optimization aspects of electronic spreadsheet models for design and planning, Journal of the Operational Research Society 42 (1991) 349– 355.

[22] E. Turban, J.E. Aronson, Decision Support Systems and Intelligent Systems, 5th edn., Prentice-Hall, Upper Saddle River, NJ (USA), 1998.

[23] A. Tversky, I. Simonson, Context-dependent preferences, Management Science 10 (1993) 1179– 1189.

[24] D. von Winterfeldt, W. Edwards, Decision Analysis and Behavioral Research, Cambridge Univ. Press, Cambridge, Eng land, 1986.

[25] M. Zeleny, Multiple Criteria Decision Making, McGraw-Hill, New York, 1982.

![](/api/attachments/SRGWEDAH/fulltext/images/54f4729b17b869d96a8ff86835933b3c9c7d0ce52365517580eefecc97602043.jpg)

Charles E. Downing is an Associate Professor in the Operations Management and Information Systems Department of the College of Business at Northern Illinois University. Professor Downing researches and consults in topics such as measuring the effectiveness of management information systems, the implementation and management of Decision Support Systems, and telecommunications and electronic commerce. His articles have appeared in

major journals such as Information and Management, Journal of Global Information Management, The Journal of Information Technology Management, Information Systems Management, Journal of End User Computing, Journal of Educational Technology Systems, European Journal of Operational Research, and Journal of the Operational Research Society. He has been quoted in The Boston Herald and other popular press venues, and he was a contributing author of the book ‘‘Groupware: Collaborative Strategies for Corporate LANs and Intranets’’. Professor Downing has significant experience as an Information Technology consultant in the financial services industry. He was national director of Ernst and Young’s microcomputer and telecommunication systems for the Defined Contribution Services group, and as an independent consultant designed, programmed, and implemented telephone interactive voice response systems for Chicago Title and Trust and numerous other companies. Professor Downing received his PhD from Northwestern University in Systems Analysis and Design.

![](/api/attachments/SRGWEDAH/fulltext/images/f7a126036936940ffdc664c3e1ae268edefd76476c52c3ee5665f2d05b5150ef.jpg)

Jeffrey L. Ringuest is Director of Curriculum and Research for the Graduate School of Management and Professor of Operations and Strategic Management at Boston College in Chestnut Hill, MA. He has an MS and PhD in Systems Engineering from Clemson University, Clemson, South Carolina.

Professor Ringuest is the author of Multiobjective Optimization: Behavioral and Computational Considerations, Kluwer

Academic, Publishing, 1992. He has also published in Computers and Operations Research, Decision Sciences, the European Journal of Operational Research, The Journal of High Technology Management Research, the IEEE Transactions on Engineering Management, Management Science, Mathematics and Computers in Simulation, Mathematical Modelling, Operations Research Letters, Research Technology Management, Socio-Economic Planning Sciences and others. Professor Ringuest is a member of DSI, and INFORMS and is on the editorial advisory board of Computers and Operations Research. His research interests are in the area of multicriteria decision making including computational problems, the interface between classical decision theory and multiple objective mathematical programming, and the application of these techniques to problems in research and development, and technology management.
