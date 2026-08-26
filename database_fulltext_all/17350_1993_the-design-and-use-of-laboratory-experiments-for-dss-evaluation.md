---
otero_id: 17350
otero_key: "N335KVF4"
title: "The design and use of laboratory experiments for DSS evaluation"
authors: "Charles L. Gardner; James R. Marsden; David E. Pingry"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90047-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The design and use of laboratory experiments for DSS evaluation \*

Charles L. Gardner

Eastern Kentucky University, Richmond KY, USA

James R. Marsden

University of Kentucky, Lexington KY, USA

David E. Pingry

University of Arizona, Tucson AZ, USA

DSS evaluation may be either ex-post or ex-ante. In the former, evaluation focuses on determining the actual result of DSS implementation. In the latter, emphasis is on predicting the likely impact of DSS alternatives on a given task set or on estimating relationships between DSS characteristics and task set(s) performance. If a firm can, ex-ante, effectively estimate or predict the performance of varying DSS on arrays of tasks or task sets, then it can avoid costly DSS selection errors and gain competitive and strategic advantages. We outline a methodology for developing such information using the induced-value methodology of experimental economics. An example experiment is detailed and initial results are presented relating to one general DSS hypothesis and one implication derived from a specific theory of DSS portfolio selection.

Keywords: DSS, DSS evaluation, DSS experiments, Induced value experiments, DSS portfolio, Ex-ante evaluation.

## 1. Introduction

In a recent extensive review, Benbasat and Nault [3] classified decision support system (DSS) experimentation issues into three categories: design, effects of use, and technology. In this paper we address issues of experimental design in the “effects of use” category. Specifically, we focus on the problem of designing experiments that yield general principles that are useful for ex-ante evaluation of DSS.

DSS evaluation may be either ex-post or ex-ante. In the former, evaluation focuses on deter-

![](/api/attachments/N335KVF4/fulltext/images/0e990bb60cb398e694c4bfa7d92633af1cf7e97ca71bc763f06a176cc1205f85.jpg)  
Charles L. Gardner is an Assistant Professor in the Department of Finance and Business Systems at Eastern Kentucky University. He recently completed his doctoral work at the University of Kentucky following a lengthy career with IBM. Dr. Gardner's research interests include DSS, computerized laboratory experiments, system evaluation, and data base systems.

![](/api/attachments/N335KVF4/fulltext/images/037acf3b20577f0f588224e2f11455a1e3d1893456892d17128bdb9a99bc0598.jpg)

James R. Marsden is the Philip Morris Professor and Chair, Department of Decision Science and Information Systems, and Professor of Economics at the University of Kentucky. Professor Marsden has held visiting positions at the University of North Carolina, Purdue University, University of York (England), and the University of Arizona. Dr. Marsden's research interests include DSS, expert system modeling of microeconomic markets, and management of information.

![](/api/attachments/N335KVF4/fulltext/images/9d45136c745a844012857342baff45ae0a9fe27cb7fa786a886c50968a64daf5.jpg)

David E. Pingry is Professor and Chair, Department of Management Information Systems and Professor of Economics at the University of Arizona. He previously was on the faculty at Virginia Polytechnic University and held visiting positions at Purdue University and at Texas A&M University. Dr. Pingry's research interests include DSS, management of information, and economics of information systems.

mining the actual result of DSS implementation. In the latter, emphasis is on predicting the likely impact of DSS alternatives on a given task set or on estimating relationships between DSS characteristics and task set(s) performance. On-going evaluations of implemented systems can provide critical information for monitoring performance and for input into later related business decisions. However, if a firm can effectively estimate or predict the performance of varying DSS on arrays of tasks or task sets, then it can avoid costly DSS selection errors and gain competitive and strategic advantages. Because of this, we concentrate our efforts on ex-ante evaluation.

To achieve optimality in DSS design and selection requires detailed knowledge. Such information may be in the form of general principles of DSS design, implementation, and use or in the form of information about the performance of a specific DSS on the tasks of interest. Testing general DSS theories and principles or developing information on specific or general DSS-task performance relationships can be time consuming and tedious, but rigorous laboratory experimentation can assist in acquiring ex-ante expertise. One might view our problem as an expert system knowledge acquisition problem where the expert system is one to be used for DSS selection. The ex-ante evaluation problem involves determining the information necessary to develop such a system.

We develop an experimental strategy for generating general DSS selection and evaluation principles. As an example of our approach we provide initial results of our ongoing research involving computerized laboratory experiments using human subjects.

## 2. Representing the DSS evaluation problem

Figure 1 provides a summary representation of the DSS evaluation problem. The set marked "D" represents the set of potential DSS or DSS portfolio. The set marked "T" represents task sets. Ex-post observations on a specific DSS focus on information relating to a specific mapping from a single element in D to a single element in T (e.g., that related to the mapping marked M1). The ex-ante evaluation of interest to us involves determining information on the set of all mappings from D to some selected task set, say Tj (e.g., the set of mappings M1', M2', ..., Mk' in Figure 1). In obtaining this information, it is important to determine what, if any, characteristics or information generalize across mappings. What, if any, general principles exist? What are the differences in mappings? What is unique to specific task sets or specific DSS configurations?

![](/api/attachments/N335KVF4/fulltext/images/e6bc60092fb6fbe5a01c8ba77a3804b5ee4f397b4980352c96d72e20bd46904b.jpg)  
Fig. 1. The DSS evaluation problem.

In two recent papers, Marsden and Pingry (MP) [11,12]. proposed a model of optimal DSS portfolio selection which attempts to isolate the critical evaluation variables for DSS. In their initial representation, MP concentrated on the problem of determining whether to use manual or computerized tools in dealing with a set of unstructured problems or decision making tasks. MP argue that the essence of DSS is that it assists in the Search for a model for an unstructured problem. The model could be a regression forecasting model, a linear program, an inventory model, or any of numerous other common model forms. Given this view, the basic DSS choice problem was formulated as follows:

maximize $_{x^c, x^m, \delta}$

$$
\begin{array}{r l} & \mathrm{x} ^ {\mathrm{c}} \left\{\mathrm{o} \left[ \mathrm{R} - \left(1 / \left(\Phi^ {\mathrm{c}} * \delta\right)\right) - \delta * \mathrm{C} ^ {\mathrm{c}} \right] - \mathrm{D} ^ {\mathrm{c}} \right\} \\ & + \mathrm{x} ^ {\mathrm{m}} \left\{\mathrm{o} \left[ \mathrm{R} - \left(1 / \left(\Phi^ {\mathrm{m}} * \delta\right)\right) - \delta * \mathrm{C} ^ {\mathrm{m}} \right] \right\} \end{array}
$$

subject to $x^{c} + x^{m} \leq 1$ .

where $x^{c}=0$ , 1 and $x^{m}=0$ , 1, o is the number of unstructured problem occurrences, R is the maximum revenue (or diminished cost) if tasks or problems are solved immediately at zero cost, $\delta$ is the number of search iterations over the manual or computerized tool set; $\Phi^{c}$ , $\Phi^{m}$ are search effectiveness parameters for, respectively, computerized and manual solution structure space; $C^{c}$ , $C^{m}$ are the cost of searching the computerized solution structure and manual solution structure spaces; and $D^{c}$ is the fixed cost of developing or purchasing the computerized system.

In words, the decision maker can purchase computerized support by spending $D^{c}$ . This support will improve the effectiveness of the system (increase $\Phi$ ) in searching for a solution and/or increase the efficiency (lower C) in searching for a solution. MP explain their basic formulation as follows:

The options the firm must evaluate, as represented in this mathematical programming formulation are:

(1) ignore the problem $(\mathbf{x}^{\mathrm{c}} = 0$ and $\mathbf{x}^{\mathrm{m}} = 0)$ ,

(2) implement a manual DSS ( $x^{c}=0$ and $x^{m}=1$ ), (3) implement a computerized DSS ( $x^{c}=1$ and $x^{m}=0$ ).

In addition, in order for the firm to evaluate these options it must determine the optimal number of search iterations ( $\delta$ ) for the computerized or manual system (given the various cost, revenue, and problem occurrence parameters).

The objective function is designed to capture the elements of the efficiency and effectiveness of the search for structure. This specific form assumes positive but decreasing marginal revenue from searching. Revenue asymptotically approaches R as $\delta$ goes to $\infty$ . The parameter (R) can be interpreted as the best (in terms of revenue) that the user can do for the given problem with the given structure type (assuming the search is free). Similarly, this form assumes that the marginal cost of searching is constant. This formulation is one of many reasonable formulations of the profit function (e.g., the rate of convergence to R could be a function of the level of R or the cost of searching could be variable)... the values of the parameters $\Phi^{c}$ and $\Phi^{m}$ can be interpreted as the ‘effectiveness’ of the search. The higher the value of $\Phi$ , the ‘quicker’ structures which generate higher revenue are ‘found.’

Operationalizations of a formal theory such as that proposed by MP can provide means to address questions about “what types of DSS work in what task settings” [10] (also see the discussion in [4]). But such operationalizations provide much more. They serve as means to test direct hypotheses as well as implications derived from the theory. It is here that we have an opportunity to determine whether we can uncover general DSS principles. As we suggested in our introductory remarks, achieving optimality in DSS design and selection requires detailed knowledge typically including both general DSS principles and specific DSS/task performance data.

In what follows we describe an experimental methodology and initial results concerning one general principle hypothesis and one hypothesis derived from the MP theoretical formulation. The general principle hypothesis is whether DSS users utilize the DSS the optimal number of times. Non-optimal use could clearly lead to misleading results concerning the value of DSS if used properly. If non-optimal use is common, we might then investigate whether or not it disappears under alternative user incentive or compensation schemes. If routine non-optimal use of DSS takes a consistent form or “bias”, this information could be used in DSS design to formulate systems to overcome such bias.

The example derived hypothesis we use is the following one deduced by MP from their theoretical formulation: as the cost of searching the computerized DSS set increases, the number of search iterations will decrease. Though straightforward in form and intuitively appealing, this hypothesis involves both the optimal operation of the DSS and whether users will act optimally in choosing DSS.

## 3. Experimental methodology

We contend that the methodological approach of experimental economics can be utilized as a key ingredient in determining the information necessary to perform meaningful ex-ante DSS evaluation. Our approach to the ex-ante DSS evaluation problem is consistent with a lengthy history of work in this area, research that has resulted in validated theories and general principles, sometimes in the form of heuristics (see discussions in [17], [18], [21], [22]). Examples of the development of useful ex-ante information in varying topic areas include: (1) alternative auction market mechanisms [14], [20]; (2) alternative market regulatory structures [7]; (3) public good problems [5]; (4) electronic markets [8], [9], [15]; and 5) composite good markets (natural gas industry) [14], [16].

The progress in developing general principles in the reference discipline of economics is encouraging to our pursuits since the problems we address are similar. For example, economic laboratory experimentation (see $[19]$ ) has confirmed over and over again that the simple supply and demand model (known as the double-auction) is very robust and performs with great efficiency and predictability. That is, if you can provide the necessary information about the supply and demand curves, you can predict the ex-post market clearing price and quantity. At the present time we know of no similar principles which have been submitted to rigorous testing and could be evoked in DSS evaluation.

Drawing from the experimental economics methodology, we can structure carefully controlled experimental settings in which we know the usefulness of the DSS or DSS characteristics under study. We can go beyond the question posed in [10] (“what types of DSS work in what task setting”?) and beyond the typical DSS experiments (see [3], [4]). We can control the potential usefulness of the DSS or DSS characteristics provided. We can structure experiments where the DSS information can be accessed and utilized successfully or unsuccessfully. We can identify and track the behavioral responses to alternative DSS-task combinations. When such experiments meet the requirements detailed in [18], we are not left wondering whether it was the DSS or the individual subjects’ response to and use of that DSS that led to observed results.

To obtain such information reliably, Smith's principles include the critical ingredient that the experimental design incorporate performance based rewards for participating human subjects, that is:

Control is the essence of experimental methodology, and in experimental exchange studies it is important that one be able to state that, as between two experiments, individual values (e.g., demand or supply) either do or do not differ in a specified way. Such control can be achieved by using a reward structure to induce prescribed monetary value on actions. The concept of induced valuation ... depends upon the postulate of non-satiation:

Given a costless choice between two alternatives, identical except that the first yields more of the reward medium (usually currency) than the second, the first will always be chosen (preferred) over the second, by an autonomous individual, i.e., utility is a monotone increasing function of the monetary reward, U(M), U' > 0. [17]

The kernel of this approach is that subjects in the experiments must be paid for how well they perform the task at hand. This, in turn, implies that how well they perform can be measured. The “realism” of the task is not created by the use of real world jargon and constructs or by the complexity of the task, but by paying the subjects real money (or other real compensation such as extra credit). This implies that the experimental task be structured from the point of view of the experimenter, even if it appears unstructured to the participant. In DSS experimentation to date, it seems that the test for “realism” has been the complexity or language (business jargon) of the task. Realism also seems to have been associated with less experimental control (see $[2]$ for a discussion of issues in DSS experimentation). Somehow the leap of faith is made that if the task looks real, subjects will take it seriously. In experimental economics the focus has been placed on capturing the important trade-offs of the “real” world and then paying the subjects an amount sufficient to take the task seriously.

A show-up fee is not equivalent to paying the subject for task performance. The subject may income maximize with a show-up fee by getting done as soon as possible. Even if they are required to stay, or have nothing better to do, they still have no particular reason to take the task seriously. Note that the subjects may take the task seriously for other reasons (fun, please the experimenter, compete with the other subjects, etc.). However, as has been demonstrated on numerous occasions in the experimental economics literature (see earlier cites), paying sufficient amounts to subjects based upon performance yields interested performances.

DSS experimentation has historically treated the incentives of the subjects rather lightly. In their comprehensive survey, Benbasat and Nault [3] do not address the compensation of the subjects nor do their detailed summary tables record the method or amount of compensation. The casual treatment of subject incentive can make it difficult to interpret experimental results. For example, is a DSS bad or was it being used inappropriately? What were the incentives to use it?

While we argue that controlled laboratory experimentation using induced value provides a means to our informational ends, we also must stress, of course, that the methodology is no guarantee of success. In each application, the quality of the experimental design is critical to being able to accurately measure what the experiment is intended to measure. The experience with induced value experimentation in economics does, however, encourage us that the approach will be useful in DSS experimentation. Task design, consistency of subject pool responses to decision maker pool responses, appropriate subject incentive mechanisms, experimental length and replication requirements all have been widely analyzed by experimental economists (for detailed commentary and serial reports updating progress, see Research in Experimental Economics, JAI press, edited by Vernon Smith, the first volume of which appeared in 1983). The objective of our experiments is to demonstrate the possibility of creating a realistic environment of the important trade-offs in DSS selection and use by making these trade-offs real to the subjects by paying them for performance.

We admit that we are taking a fairly narrow approach to DSS experimentation. We are interested in evaluation from the point of view of input-output. We are not concerned with process. We are not addressing design methodology or technology issues as discussed by Benbasat and Nault. We would argue, however, that the approach here can be used to address these issues as well and our ongoing research efforts are moving in these directions.

## 4. The experimental environment

Our first step in completing the hypothesis tests discussed earlier was the formal operationalization of the MP theory. Following the experimental economics framework, our objective for the initial set of experiments was to examine the performance of DSS under the following conditions:

1. The task as perceived by the subjects should be unstructured.

2. The DSS should be simple, yet it should capture the major components which characterize DSS.

3. The DSS should be a “good” DSS if used well and be “bad” if it is not used well.

4. “Good” and “bad” should be measurable.

5. The subjects should have significant incentive to utilize the DSS well.

This set of conditions gives users the possibility of making good use of a DSS in an unstructured environment and being rewarded for it. The obvious question is do they? Also, do they respond in the ways predicted by the MP theory? Many additional interesting hypotheses and questions can be analyzed (e.g., is DSS used well when the incentives are not high for the user?). But, because our purpose here is to illustrate the methodology, we limit our presentation of results as indicated above. Later reports will provide comprehensive results (interested readers are referred to Gardner's [6] recent dissertation for complete experimental specifications, details of session coordination, procedures, and complete results of his phase of the experimental agenda).

The experimental task we chose was based on an economics of information problem presented in Ahituv and Wand [1]. The stream of unstructured problems was made up of production decisions which bad to be made in the face of uncertain demands. The subject had to select a level of production from three choices (low, medium, high) in an attempt to meet unknown (random) demands (low, medium, high). Subjects could utilize a DSS or could make a decision without seeking such information. The DSS had two major features. It could generate a forecast of demand and it could give information about forecasts, demands and decisions in prior periods. The computerized forecasts of demand had to be purchased in ascending order of reliability (that is, to purchase second forecast, first forecast must have been purchased). The subject could stop purchasing forecasts DSS at any point and make the final output choice. There was a maximum number of forecasts available for each problem occurrence. The manual DSS was interpreted as learning based on replications without accessing computerized DSS.

This task was made consistent with the MP selection theory above by charging the subject a cost for purchasing a forecast. This is analogous to the search cost, $C^{c}$ . In addition, in order to make the decision environment more realistic, a cost for the time used to make a decision was charged with a running clock and time cost continuously displayed on each subject's computer screen during each decision period.

The revenue curve was such that the expected value of the forecasts increased at a decreasing rate. This assumption follows a decision making setting where the decision maker first sees the information with highest marginal contribution. Since the actual demand is randomly generated from a prescribed distribution of low, medium, and high occurrences, the maximum revenue achievable, R, can only be determined in an expected value sense. For each experimental replication, we could compute the optimal number of searches (that is, the number of searches to maximize expected profit) and expected optimum revenue and optimum profit. We defined optimum revenue as that achievable if the subject had chosen the optimum number of forecasts (DSS consultations) and made the output choice indicated by that forecast. The expected optimum profit is the optimum revenue less the search costs for performing the optimal number of searches.

Experimental subjects were asked to make a decision during each period. The decision type was the same for each period, but the parameters faced by the subject were varied. The number of forecasts available for purchase in a single experiment session was fixed in order to facilitate investigation of hypotheses concerning the utilization of information as a function of the amount of information available.

Actual demand for each period was randomly generated by the experimental program using a three element probability vector (PI). Each element of this PI vector represents the discrete prior probability of occurrence of each of the three possible events (or states) or demands. The four PI vectors used in our experiments were:

$$
\begin{array}{c c c c} 0. 2 & 0. 3 3 3 & 0. 1 & 0. 3 \\ \mathrm{PI} _ {1} = 0. 5, \mathrm{PI} _ {2} = 0. 3 3 3, \mathrm{PI} _ {3} = 0. 6, \mathrm{PI} _ {4} = 0. 2 \\ 0. 3 & 0. 3 3 3 & 0. 3 & 0. 5 \end{array}
$$

Each of the DSS tools for this experiment can be represented by a stochastic (reliability) matrix whose elements are non-negative and where each

row sums to one. Each element of these matrices (illustrated below) represents the conditional probability of a signal (low, medium or high forecast) given an event (low, medium or high demand), that is:

<table><tr><td rowspan="2">Demand</td><td colspan="3">Forecast</td></tr><tr><td>L</td><td>M</td><td>H</td></tr><tr><td>L</td><td> $a_{11}$ </td><td> $a_{12}$ </td><td> $a_{13}$ </td></tr><tr><td>M</td><td> $a_{21}$ </td><td> $a_{22}$ </td><td> $a_{23}$ </td></tr><tr><td>H</td><td> $a_{31}$ </td><td> $a_{32}$ </td><td> $a_{33}$ </td></tr></table>

Different reliability matrices were created for our experiments. Elements of the matrices were selected so that $0 \leq a_{ij} \leq 1$ and the rows summed to 1 (see [6] for a complete listing of these matrices). Matrices were ordered by reliability as indicated by increasing size of diagonal elements (accurate predictions) and decreasing size of off-diagonal elements (inaccurate predictions). The subject received the least reliable forecasts first and then in ascending order. To be consistent with the MP theory, the reliability increased at a decreasing rate. The DSS also provided the subject with the ability to call up the complete history of the prior six periods.

The experimental scenario required the subject to make a decision during each period of the experimental game. The subject could develop his/her own strategy or decision rule based upon whether or not he/she purchased the signals, that is, consulted one or more of the available DSS tools or forecasts. A gross revenue payoff matrix was created to represent the payoff result as a function of the action taken (production L, M, H) and the actual event (demand of L, M, H). Net payoff or profit for an experimental period was calculated by taking the gross payoff and subtracting the cost of the forecast or DSS search and the time cost. Subjects were paid on a specified exchange rate of U.S. dollars for profit achieved in experimental dollars. The experiments were structured so that each subject participated in two experimental sessions, one with actual cash payments based upon performance and one without cash payments. This was done in order to provide a means for directly analyzing the impact of such payments on performance. In all sessions, net “profit” values were computed and displayed immediately after the conclusion of each decision period.

Each session had six cycles. This “numbers of cycles per session” value was chosen by us after pretesting the experimental software. This value fit comfortably within a one hour session time frame that included a video tape instruction presentation and a practice session. All cycles were randomly assigned. No uniquely configured cycle was used more than once (see Gardner, 1990, for laboratory experiment control forms used to assign customized versions of the experiment program randomly and insure that all combinations were covered at least one time for both the “for-pay” and the “not for-pay” experiments).

One net payoff matrix was calculated and used throughout the experiments. The following matrix is the matrix actually used in the experiments:

<table><tr><td rowspan="2">Action</td><td colspan="3">Event (demand)</td></tr><tr><td>Low</td><td>Medium</td><td>High</td></tr><tr><td>Low</td><td>7</td><td>-12.5</td><td>-32</td></tr><tr><td>Medium</td><td>-12.5</td><td>17.5</td><td>-2</td></tr><tr><td>High</td><td>-32</td><td>-2</td><td>28</td></tr></table>

The experimental design described above meets the five conditions outlined above. First, the problem is perceived as unstructured by the subjects. Second, the DSS is simple, yet it captures two of the main aspects of a DSS: it gives a forecast and has memory. Third, the parameters of the experiment can be set so that it is possible for the DSS to create value if used enough, but not too much. Thus, success and failure are both possible. Fourth, the profit of the DSS can be calculated and the subjects can be paid (in the for-payment sessions) accordingly. Last, the subject could do better if he/she used the system better. Such an experimental design is an example of processes that can serve as a basis for a search for DSS principles.

## 5. Experimental procedures

MBA graduate and upper division undergraduate students were recruited as human subjects for the experiments. Recruiting consisted of class presentations and discussions of research objectives, experimental methodologies to be followed, and the need for student subject participation. Of special significance was the presentation of the compensation methodology to be used. The students were asked to participate on two separate occasions. They were paid \$5.00 for showing up at each session. One of the sessions included no compensation other than the show up fee, and the other session included the show up fee plus an additional fee amount determined by how a subject performed during the experiment. We attempted to have as many of the subjects as possible participate in both “incentive driven” (pay for performance) and “non-incentive driven” sessions. This permitted the analysis of the experimental results with respect to the various factors and variables in different incentive/non-incentive combinations and sequences. Both sessions appeared the same to the subject except that they would know when they were being paid for performance and when they were not.

Only those students who filled out the “request to participate” forms were contacted to participate in experiment sessions. Subjects were contacted by phone 1 to 2 days prior to scheduling experiment sessions. Those who were paid the incentive for the first session but not the second were selected randomly as were those who were paid the incentive for the second session but not the first. Subjects were asked to schedule their second session after completing the first session and reminded about how they would be compensated. The sessions were scheduled to fit the subjects’ schedules.

The program used to assign experimental sessions utilized random assignments with the condition that each unique parameter combination was assigned to a subject session. Experimental sessions were designed such that each unique combination of all of the factors above were covered by at least one “cycle” or one complete experimental game. Cycle numbers were randomly assigned to subjects to form unique configurations for individual experimental sessions. This insured that there was no “presession” information passed to subjects from either their own prior sessions or the prior sessions of other subjects.

The experimental session begins with a video taped presentation welcoming the subjects to the MIS Research Laboratory and introducing them to the experiment and its environment (copies of tape are available). The video also shows a complete practice session of the experiment. After viewing the video presentation the subjects participate in a computerized tutorial. This tutorial is textual and gives the subject a detailed description of the experiment and how he/she will interact with the experimental program via the keyboard and video display. The “incentive pay” methodology is explained to the subject along with a verbal description of how his/her pay will be computed at the end of the experimental session.

The video is followed by a short, five problem occurrence practice session to acquaint them with the computer system, the user interface screen and generally how to conduct their part of the session. This practice session version of the experimental program is customized so that there is no information to be obtained by purchasing IS and the PI vector is strictly neutral across all three demands (L, M, and H). This is intended to eliminate any “learning” by the subject of how to “play the game”. All that the subject learns during the practice session is the mechanics of playing the experimental game.

The practice session is followed by six cycles of the actual experimental session. Each cycle consists of multiple decision periods, with the number of decision periods per cycle randomly assigned and taking on a value of 20, 30, 40, or 50. The number of DSS (information systems) that are available for purchase during a given cycle was constant but was randomly varied across cycles, taking on a value of 5, 6, 8, 9, or 10.

Upon completion of individual sessions, the individual's compensation is calculated and a payment check issued. If it is the subject's first session, the subject is asked to schedule a second session before leaving the lab.

Each cycle is begun with an information screen indicating to the subject the following information:

(1) The number of problem occurrences that are in the current cycle.

(2) The fact that they are being advanced 100 experimental dollars. This advance serves to cover start up problems and prevent early “bankruptcy”.

(3) For “for-pay” sessions only, the conversion factor for converting experimental dollars to real U.S. dollars at the end of the experiment. (The experimental program is customized to provide an expected payoff (EV) maximum of one U.S. dollar per cycle.)

During each cycle profits/losses are added to the subject's account balance and displayed. If the subject's account balance becomes zero or negative at any time during the cycle, the subject is considered "bankrupt" and the cycle ended. After the end of a cycle (due to normal termination or due to bankruptcy) the subject is immediately presented with the next cycle. No time limit is placed upon the subject for completing any cycle or the overall experimental session. However, a clock is constantly displayed showing the subject the elapsed time per problem occurrence and there is a time charge for each second of decision time. The clock is reset to zero at the beginning of each problem occurrence.

For the “incentive driven” (for-pay) sessions the incentive pay is calculated as follows:

\- The advance of 100 experimental dollars is subtracted from the final account balance at the end of each cycle of the experimental game. This represents the profit for the cycle in experimental dollars. Only positive profits are counted with zero and negative cycle profits counting as zero experimental dollars for the cycle.

\- This experimental profit is divided by the conversion assigned to each cycle and displayed for the subject at the beginning of each cycle. This gives the number of real U.S. dollars that the subject has earned for that cycle.

\- The real U.S. dollars is added up for all cycles finished by the subject during the session. This is the total incentive pay for the session.

\- The total incentive pay is added to the five dollar “show-up” fee and paid in check to the subject.

\- The five real U.S. dollar “show-up” fee is paid no matter what the incentive pay was for the subject.

The customized experimental software we developed enabled us to randomly vary pertinent relevant variables across the range of values of interest, to carefully track and preserve experimental outcomes, and to easily monitor subjects.

Table 1  
Initial results relating to H1. $^{a}$

<table><tr><td>Category</td><td>All</td><td>For-pay</td><td>Not for-pay</td></tr><tr><td>Observations</td><td>16,790</td><td>8,930</td><td>7,860</td></tr><tr><td>Profit achieved</td><td>4.96(14.7)</td><td>5.16(14.7)</td><td>4.74(14.8)</td></tr><tr><td>Optimal DSS to consult - DSS actually consulted</td><td>0.90(2.4)</td><td>0.98(2.4)</td><td>0.81(2.5)</td></tr><tr><td>Profit from optimal action less actual profit achieved</td><td>2.94(17.7)</td><td>2.75(17.7)</td><td>3.16(17.7)</td></tr><tr><td>Revenue achieved</td><td>11.30(15.2)</td><td>11.41(15.1)</td><td>11.17(15.4)</td></tr></table>

$^{a}$ Sample standard deviations given in parentheses under values.

## 6. Initial results

As we indicated earlier, our purpose here is to illustrate a methodology and elucidate how it may serve us in ex-ante DSS evaluation. We limit our presentation of results to those pertinent to one general hypothesis and one specific implication derived from the MP theory. Experiments utilized 47 subjects and resulted in a total of 19,380 experimental outcomes across the intended variable ranges.

H1 - DSS users utilize the DSS the optimal number of times.

The results provided in Table 1 indicate that, on average, subjects underutilized or undersearched by slightly under one system. That is, subjects consulted, on average, 0.9 fewer forecasts of demand than was optimal. Though in “for-pay” sessions subjects actually, on average, undersearched a bit more (0.98 vs. 0.81), these sessions yielded greater average profit (5.16 vs. 4.74). While one possible explanation is more attentive decision making during the “for-pay” sessions, we reserve speculation until we complete a thorough analysis of expanded experimentation. Discussions with subjects following the completion of experimental session indicated that the monetary payments and the nature of the computerized game presentation (even where no performance payments were to be made) both led to interested participation in this case.

H2 - As the cost of searching the computerized DSS set increases, the optimal number of search iterations decreases.

Per iteration search costs were randomly generated for each experiment from the following set of values: $C^{c} \in \{1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75\}$ . Table 2 provides a summary of results for three of these per iteration search costs. The information is summarized for “for-pay” subject sessions and “non-pay” subject sessions, all values are averages across the number of experimental replications indicated, and the optimal number of information systems to consult is determined based upon a decision rule to maximize expected return.

For the overall average (TOTAL) and for the “for-pay” and “not for-pay” subgroups, the results presented in Table 2 are consistent with the implication derived from the MP theory that searching decreases as search cost increases. But the results also provide an interesting result concerning the difference between optimal and actual number of DSS or “predictions” consulted. Consider, for example, experiments where search cost was \$1.50 and the optimal number of information systems or DSS to consult was 6. In the set of experiments using a \$1.50 search cost, pay subjects consulted 30.8% (1.85/6.00) less than the optimal number. In non-pay experiments, subjects consulted 40.2% (2.4/6.00) less than the optimal number of information systems. With higher search costs of \$2.00, pay experiment subjects consulted 9% (0.27/3.00) more than the optimal number (12.7% in non-pay experiments). With the \$2.50 search cost, subjects consulted 9.3% fewer than the optimal number of information systems (9.3% in non-pay experiments). While these are but initial results, they interest us because of their consistency across groups (see Table 2) and their consistency with higher relative costs driving closer to optimal behavior.

Table 2  
Initial results relating to H2.

<table><tr><td></td><td> $C^c = 1.50$ </td><td>2.00</td><td>2.50</td></tr><tr><td colspan="4">Number of observations</td></tr><tr><td>Total</td><td>1500</td><td>1450</td><td>1310</td></tr><tr><td>For-pay</td><td>780</td><td>720</td><td>700</td></tr><tr><td>Not for-pay</td><td>720</td><td>730</td><td>610</td></tr><tr><td colspan="4">Average number of DSS forecasts consulted</td></tr><tr><td>Total</td><td>3.88</td><td>3.32</td><td>3.01</td></tr><tr><td>For-pay</td><td>4.15</td><td>3.27</td><td>2.72</td></tr><tr><td>Not for-pay</td><td>3.59</td><td>3.38</td><td>3.28</td></tr><tr><td colspan="4">Optimal number of DSS forecasts – number consulted</td></tr><tr><td>Total</td><td>2.12</td><td>-0.33</td><td>0.02</td></tr><tr><td>For-pay</td><td>1.85</td><td>-0.27</td><td>0.28</td></tr><tr><td>Not for-pay</td><td>2.41</td><td>-0.38</td><td>-0.28</td></tr></table>

While there might be a temptation to label the derived implication as “obvious,” we point out that the results here go beyond what one’s mental view is of “what should be.” Through these experiments we have demonstrated that individual users actually respond to search costs in a way described by the theory. Further the results held in both types of experimental settings, one with performance based subject payments and one without such payments but still utilizing apparently motivated subjects.

## 7. Concluding remarks

We have focused on ex-ante evaluation, on structuring techniques for determining the information necessary to optimally design DSS or optimally select DSS portfolio. After positing the usefulness of the induced-value experimental methodology, we illustrated how such experimentation can be used in ex-ante methodology and presented a limited set of initial results from our current experimentation.

While ex-post evaluation may provide helpful information for future decision making, such information may come too late to avoid the firm's demise. Survival in competitive situations is not guaranteed. Errors in the short run may make long running planning irrelevant. For these reasons, we argue the importance of ex-ante evaluation and offer this methodological discussion as a means to stir debate and stimulate research in this important area.

## References

[1] N. Ahituv and T. Wand, Comparative Evaluation of Information Under Two Business Objectives, Decision Sciences, 15 (1984) 31–51.

[2] I. Benbasat, Ed., The Information Systems Research

Challenge: Experimental Research Methods, Vol. 2 (Harvard Business School, Cambridge, MA, 1989).

[3] I. Benbasat, and R. Nault, An Evaluation of Empirical Research in Managerial Support Systems, Decision Support Systems 6, No. 3 (1990) 203–226.

[4] I. Benbasat, G. DeSanctis and R. Nault, Empirical Research in Management Support Systems: A Review and Assessment, Paper presented at NATO ASI on Decision Support Systems (Barga, Italy, June 1991).

[5] D. Brookshire, D.L. Corsey and W.D. Schultze, Experiments in the Solicitation of Private and Public Values: An Overview, in: L. Green and J. Kagel, Eds., Advances in Behavioral Economics, Vol. 2, (Ablex Publishing Company, Norwood, NJ, 1990).

[6] C.L. Gardner, Jr., Testing the Hypotheses of an DSS Theory: The Integration of Microeconomic Theory, Laboratory Experiments, and Information Theory Evaluations, Ph.D. Thesis (University of Kentucky, Lexington, KY, 1991).

[7] G.W. Harrison, M. McKee and E.E. Rutstrom, Experimental Evaluation of Institutions of Monopoly, in: L. Green and J. Kagel, Eds., Advances in Behavioral Economics, Vol. 2 (Ablex Publishing Company, Norwood, NJ, 1990).

[8] E. Hoffman, J.R. Marsden and A.B. Whinston, Laboratory Experiments and Computer Simulation: An Introduction to the Use of Experimental and Process Model Data in Economic Analysis, in: L. Green and J. Kagel, Eds., Advances in Behavioral Economics, Vol. 2 (Ablex Publishing Company, Norwood, NJ, 1990).

[9] R.R. King, V.L. Smith and A.W. Williams, The Robustness of Bubbles and Crashes in Experimental Stock Markets (Department of Economics, University of Arizona, Tucson, AZ, 1989).

[10] J. Kotteman and W.E. Remus, Evidence and Principles of Functional and Dysfunctional DSS, OMEGA 15, No. 2 (1987) 135–143.

[11] J.R. Marsden and D.E. Pingry, Problem Structure and DSS Design, Proceedings of the Nineteenth Hawaii International Conference on System Sciences (1986) 603–608.

[12] J.R. Marsden and D.E. Pingry, Decision Tables for Decision Support System Design, Proceedings of the Twentieth Hawaii International Conference on System Sciences (1987) 647–654.

[13] J.R. Marsden and D.E. Pingry, A Theory of Decision Support System Portfolio Design and Evaluation, Decision Support Systems, forthcoming.

[14] K.A. McCabe, S.J. Rassenti and V.L. Smith, Auction Design for Composite Goods – The Natural Gas Industry, Journal of Economic Behavior and Organization 14, No. 1 (1990) 127–149.

[15] D. Porter and V.L. Smith, The Scope of Bubbles in Experimental Asset Markets (Department of Economics, University of Arizona, Tucson, AZ, 1989).

[16] S.J. Rassenti, S.S. Reynolds and V.L. Smith, Cotenancy and Competition in an Experimental Auction Market for Natural Gas Pipeline Networks, (department of Economics, University of Arizona, Tucson, AZ, 1989).

[17] V.L. Smith, Experimental Economics: Induced Value

Theory, American Economic Review 66, No. 2 (1976) 274–279.

[18] V.L. Smith, Microeconomic Systems as an Experimental Science, American Economic Review 72, No. 5 (1982) 923–955.

[19] V.L. Smith, Theory, Experiment and Economics, Journal of Economic Perspectives 3, No. 1 (1989) 151–169.

[20] V.L. Smith and A.W. Williams, The Boundaries of Competitive Price Theory: Convergence, Expectations, and Transaction Costs, in: L. Green and J. Kagel, Eds.,

Advances in Behavioral Economics, Vol. 2 (Ablex Publishing Company, Norwood, NJ, 1990).

[21] V.L. Smith, G.L. Suchanek and A.W. Williams, Bubbles, Crashes, and Endogenous Expectations in Experimental Markets, Econometrica 56, No. 5 (1988) 1119–1151.

[22] V.L. Smith, A.W. Williams, W. Bratton and M.G. Vannoni, Competitive Market Institutions: Double Auctions versus Sealed Bid-Offer Auctions, American Economic Review 72, No. 1 (1982) 58–77.
