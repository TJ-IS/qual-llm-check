---
otero_id: 16932
otero_key: "PQP2FY78"
title: "From what if to what's best in DSS"
authors: "Asim Roy"
year: "1987"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(87)90033-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# From What If to What's Best in DSS\*

Asim ROY

Arizona State University, Tempe, AZ 85287, USA

The author of IFPS/OPTIMUM presents some typical applications of optimization within decision support systems (DSS). They show that finding 'what's best' is gradually superseding the 'what if' and 'goal seeking' type of analysis that is prevalent now. IFPS/OPTIMUM is now used by over 130 companies, including many of the Fortune 500 ones. The main drawback of 'what if' and 'goal seeking' type of analysis is that one cannot impose restrictions on model variables and have the DSS generator solve for values of the 'what if' or 'goal seek' variables that satisfy those restrictions. Instead, one would have to muddle through many 'what if's' or 'goal seeks' at random and check if the restrictions are satisfied. It is a manual process that is very time consuming. 'What's best' analysis with optimization allows one to impose such restrictions easily and do the analysis quickly. This type of analysis is playing an increasingly significant role within decision support systems. Practicing management scientists and managers should note this phenomenon. New tools and new ways of addressing problems are emerging.

Keywords: Optimization in DSS, Optimization in planning languages, Optimization application in business.

![](/api/attachments/PQP2FY78/fulltext/images/aa0fe7ed1573d009ac8df8a7e6aaa133ff8ba30ea2698a6537f6fd62578af116.jpg)

Asim Roy is the author of IFPS/OP-TIMUM, now marketed by Execucom Systems Corp., Austin, Texas. He has a Bachelor of Engineering degree from Calcutta University, India. He completed his M.S. in Operations Research from Case Western Reserve University, Cleveland, and his Ph.D. in Operations Research from University of Texas at Austin. He is currently an Assistant Professor of Management Science in the College of Business at Arizona State University. At Ex-

ecucom, he was manager of the operations research group. His main research interest is in the integration of optimization techniques with DSS languages and in making 'end-user' optimization a reality.

\* The research was supported in part by the Faculty Research Development Award, Arizona State University, and by the Department of Decision and Information Systems Research Award, Arizona State University, 1986.

## 1. Introduction

Optimization capabilities have recently been added to some decision support system (DSS) generators. The IFPS/OPTIMUM system was designed for the mainframe DSS generator called IFPS (see [6], [7], [9], [10]) and the VINO system optimizes models (only linear ones) built in microcomputer DSS generators such as Visicalc, Lotus 1-2-3 and Multiplan [2]. The author of this paper is the developer of the pioneering optimization system, IFPS/OPTIMUM, and observed many of the applications of optimization within DSS. This paper reports on some of the DSS uses of optimization and presents simplified versions of the models actually used.

Many other individual applications of optimization within DSS have been reported. Russo and Sarker [11] reported one application of IFPS/OPTIMUM at Exxon, and Roy, DeFalomir and Lasdon [4] reported an application at Ponderosa Industrial in Mexico. Roy and Huttner [8] reported two applications of IFPS/OPTIMUM at Prime Computers. Wagner [12] discusses the use of optimization within DSS for strategic planning. Carlsson [1] reports using IFPS/OPTIMUM for solving a fuzzy multiobjective programming problem. Geoffrion [3] has noted the importance of providing optimization capabilities to a variety of users in a new mode. Experience shows that providing these tools in the DSS toolkit is a very effective way to promote the use of optimization.

The main purpose in providing optimization capabilities within DSS generators is to allow analysts to do more powerful model analysis than can be done with 'what if's' or 'goal seeking'. $^{1}$ However, even a well-designed, user-friendly optimization system such as IFPS/OPTIMUM had

difficulty in overcoming the fear of using a very complex tool. Much of that is changing as analysts learn to use optimization on the same models that were meant to be manually optimized using the 'what if' or 'goal seeking' mode of analysis. Two such models are presented next, ones that made the transition from 'what if' to 'what's best' mode of analysis. The main reason for the transition in these cases is that one cannot ask the 'what if' analyzer to obey restrictions on some model variables and solve for corresponding values of the 'what if' variables. The analysts were frustrated contains either data or an expression involving other model variables. For optimization, the IFPS model has some adjustable cells which contain the decision variables, and the model statements must compute the objective and constraints as functions of these decisions and of problem data. A directive set identifies which cells are decisions, constraints, and the objective, and specifies limits on the constraints and decisions.

To illustrate, the model and directive set for a simple product mix problem is shown. The model is self documenting.

```csv
100 COLUMNS PROD 1, PROD 2, TOTAL
110 PROFIT CONTRIBUTION = REVENUE - VARIABLE COST
120 REVENUE = QUANTITY * PRICE
130 VARIABLE COST = LABOR COST + PLASTIC COST
140 LABOR COST = LABOR HOURS * LABOR COST PER HOUR
150 PLASTIC COST = POUNDS OF PLASTIC * PLASTIC COST PER POUND
160 LABOR HOURS = QUANTITY * LABOR HOURS PER UNIT
170 POUNDS OF PLASTIC = QUANTITY * POUNDS PLASTIC PER UNIT
178 ***
179 ***QUANTITY WILL BE ADJUSTED BY OPTIMUM
180 QUANTITY = 5000, 6000
181 ***
190 PRICE = 139, 189
200 LABOR HOURS PER UNIT = 0.5, 1
210 LABOR COST PER HOUR = 25
220 POUNDS PLASTIC PER UNIT = 2,3
230 PLASTIC COST PER POUND = 7
240 COLUMN TOTAL FOR PROFIT CONTRIBUTION THRU'
250 POUNDS OF PLASTIC = COLUMN PROD 1 + COLUMN PROD 2
```

having to try random solutions and then screening out the ones satisfactory to management.

Practicing managers and management scientists should note the availability of these new tools within the DSS tool kit. They can use these tools on many of their existing models and find better decisions for the organization more efficiently. This paper reports this new development through some applications. Following the overview of OPTIMUM, the next two sections discuss two applications in detail.

## 2. An Overview of OPTIMUM

OPTIMUM uses the IFPS planning language to define an optimization problem. IFPS is based on a matrix or spreadsheet, in which each cell

The directive set identifies the spreadsheet cells of concern to OPTIMUM as the OBJECTIVE, the DECISIONS, and the CONSTRAINTS. This directive instructs OPTIMUM to maximize PROFIT CONTRIBUTION (in column TOTAL) by finding the optimal values of the decision variables, QUANTITY in columns PROD 1 and PROD 2, within the indicated bounds. The values of the decision variables are to be selected so that LABOR HOURS (in column TOTAL) and POUNDS OF PLASTIC (in column TOTAL) do not exceed the specified limits.

## 100 OBJECTIVE

100 OBJECTIVE
110 MAXIMIZE PROFIT CONTRIBUTION (TOTAL)
120 DECISIONS
130 QUANTITY (PROD 1) BETWEEN 0 AND 5000
140 QUANTITY (PROD 2) BETWEEN 0 AND 6000

150 CONSTRAINTS
160 LABOR HOURS (TOTAL) .LE. 6000
170 POUNDS OF PLASTIC (TOTAL) .LE. 1800

Using this model, OPTIMUM diagnoses the linearity of the problem, generates the LP coefficient matrix, and transfers it to the linear programming solver. If the problem is nonlinear, it is solved by a nonlinear optimization code. After solution of an LP, objective and right hand side ranges are available. In addition, IFPS offers excellent reporting and graphics capabilities.

A major advantage of such a system is that problem generation, solution, and reporting are integrated. In the above example, the objective coefficients are computed in lines 110 through 150. The problem data in lines 190 through 230 is easily modified, and could be contained in a separate data file, or drawn from a data base using the IFPS DIMENSION database system.

A second advantage is ease of use. IFPS models are english-like, easy to understand, and utilize the spreadsheet format, which is widely accepted and understood. The ability to include many intermediate expressions in IFPS permits building a complex model in easy steps.

IFPS/OPTIMUM is mainly designed for small to medium size linear and nonlinear optimization problems. It recently added a mixed integer (linear) capability. However, many problems encountered are nonlinear because of if-then-else logic, max, min or round functions, etc. in the IFPS model. These lead to nondifferentiable, sometimes discontinuous optimization problems. Nonlinear programming algorithms designed for smooth problems often fail in these situations. It also cannot handle mixed integer nonlinear problems.

## 3. Collecting Accounts Receivable

Collection of accounts receivable has wide implications for the short term cash flow of a company. At one computer manufacturing firm, a separate group existed to follow up on accounts receivable. The receivables were classified by size (e.g., those under \$10,000 and those over \$10,000) and by age of the invoices (e.g., less than three months old, between three and six months old). The amount of time spent in collecting varied with size and age. This variation was also a function of the difficulty of the collection process. The payoff from such efforts is often erratic. For instance, a vigorous follow up on a high value account did not always result in full payment.

Due to the rapid expansion of sales, it became more difficult for the staff to follow up adequately on the outstanding receivables. Before sanctioning additional staff, management called for an analysis of the collection operation to determine two things:

(1) the amount of additional staffing required, and

(2) opportunities for improvement in the collection operation.

That is, the management wanted to find if collection time was being used optimally, and if there was a need for additional staff when collection time is optimally allocated.

A simplified version of the model that was used for this analysis is shown in fig. 1. The collections staff provided information about the makeup of the receivable portfolio and the time requirements for each invoice type. Further refinement of the categories was done for the analysis. For example, value categories were increased from two to four. The amount of time required to follow up on each invoice type was based on actual experience. Estimates of the fraction that paid only part of their accounts (partial payment fractions) were also based on staff experience. Note that the partial payment fractions and the amount of partial payments may be considered as random variables. However, such uncertainties were not built into the model in order to keep the analysis simple. Also, it was assumed that the amount of collection in each category was linearly proportional to the time spent. The model will now be explained in more detail.

The first three columns of the model (fig. 1) represent time periods. Column TOTAL is a special column used for summing variables over the first three columns. Lines 100 through 120 give the breakdown of existing invoices by age and value. This simplified model breaks down receivables into three ages categories [0 to 6 months old (HALF1), six to twelve months old (HALF2), and over one year old (OLDER)] and three value categories (under \$10,000, between \$10,000 and \$100,000, and those over \$100,000). Lines 150

```txt
10 COLUMNS HALF1, HALF2, OLDER, TOTAL
20 *
30 * TO EXPLAIN THE COLUMNS:
40 * HALF1 = INVOICE FROM THE CURRENT HALF YEAR
50 * HALF2 = INVOICE FROM THE SECOND HALF YEAR
60 * OLDER = INVOICE OLDER THAN ONE YEAR
70 * TOTAL = TOTAL OF ALL TIME PERIODS
80 *
90 * NUMBER OF INVOICES IN EACH TIME CATEGORY BROKEN BY DOLLAR VALUE
100 NUMBER LT 10 = 7000, 2000, 200
110 NUMBER 10 TO 100 = 500, 100, 20
120 NUMBER GT 100 = 150, 50, 20
130 *
140 * THE AMOUNT OF TIME EACH INVOICE TYPE REQUIRES FOR FOLLOW UP
150 TIME PER LT 10 = 1, 0.5, 1
160 TIME PER 10 TO 100 = 2, 3, 4.5
170 TIME PER GT 100 = 3, 4, 6
180 *
190 * CALCULATE THE TIME REQUIREMENTS OF THE PORTFOLIO
200 TIME REQUIRED LT 10 = NUMBER LT 10 * TIME PER LT 10
210 TIME REQUIRED 10 TO 100 = NUMBER 10 TO 100 * TIME PER 10 TO 100
220 TIME REQUIRED GT 100 = NUMBER GT 100 * TIME PER GT 100
230 *
240 * VALUE OF THE PORTFOLIO INCLUDING THE ISSUE OF PARTIAL PAYMENTS
250 PARTIAL 10 TO 100=30% * NUMBER 10 TO 100, 50% * NUMBER 10 TO 100, 0
260 PARTIAL GT 100 = 30% * NUMBER GT 100, 50% * NUMBER GT 100, 0
270 FULL VAL'E 10 TO 100 = NUMBER 10 TO 100 - PARTIAL 10 TO 100
280 FULL VALUE GT 100 = NUMBER GT 100 - PARTIAL GT 100
290 *
300 VALUE OF LT 10 = 8 * NUMBER LT 10
310 VALUE OF 10 TO 100 = 50 * FULL VALUE 10 TO 100 + 3 * PARTIAL 10 TO 100
320 VALUE OF GT 100 = 150 * FULL VALUE GT 100 + 6 * PARTIAL GT 100
330 TOTAL VALUE = SUM (L300 THRU L320)
340 *
350 * CALCULATE THE TIME SPENT ON COLLECTIONS AND AMOUNT COLLECTED
360 TIME ON LT 10 = 100
370 TIME ON 10 TO 100 = 100
380 TIME ON GT 100 = 100
390 TOTAL TIME SPENT = SUM (L360 THRU L380)
400 *
410 VALUE LT 10 COLLECTED = (TIME ON LT 10/TIME REQUIRED LT 10) * L300
420 VALUE LT TO COLLECTED = (L370/L210) * L310
430 VALUE GT 10C COLLECTED = (TIME ON GT 10O/TIME REQUIRED GT 1O) * L32O
440 VALUE COLLECTED = SUM (L41O THRU L43O)
450 *
460 DEFICIT ON LT 1O = TIME REQUIRED LT 1O - TIME ON LT 1O
470 DEFICIT ON LT TO 1O = TIME REQUIRED LT TO 1O - TIME ON LT TO 1O
480 DEFICIT ON GT 1O = TIME REQUIRED GT 1O - TIME ON GT 1O
490 *
50C COLUMN TOTAL FOR L39O, L44O = SUM (COLUMN1 THRU COLUMN3)
```  
Fig. 1. IFPS model.

through 170 specify the average hours required to follow up on an invoice of each type. Lines 200 through 220 calculate the total collection hours for all invoices. Lines 250 and 260 estimate the number of invoices that would make partial payments when followed up. It is assumed that full payments are made by accounts under \$10,000. For the remaining categories, it is assumed that about 30% make partial payments in the first six months (HALF1) and it increases to 50% in the second six months (HALF2). Lines 270 and 280 compute the number of invoices that are paid in full.

Lines 300 through 320 estimate the total collectible value of the accounts receivable portfolio, accounting for partial payments. The average partial payment estimates are based on past experience. In case of full payments, an average invoice value for the category is used. For instance, in line 300, the average invoice value for receivables under \$10,000 is assumed to be \$8,000. In line 310,

<table><tr><td>20 *</td></tr><tr><td>30 * OBJECTIVE - MAXIMIZE TOTAL COLLECTION BY OPTIMAL</td></tr><tr><td>40 * ALLOCATION OF COLLECTION TIME</td></tr><tr><td>50 *</td></tr><tr><td>60 MAXIMIZE VALUE COLLECTED (TOTAL)</td></tr><tr><td>70 *</td></tr><tr><td>80 * DECISIONS - HOW MUCH TIME TO ALLOCATE TO DIFFERENT</td></tr><tr><td>90 * CATEGORIES OF INVOICES IN DIFFERENT PERIODS</td></tr><tr><td>100 *</td></tr><tr><td>110 DECISIONS</td></tr><tr><td>120 *</td></tr><tr><td>130 TIME ON LT 10, TIME ON 10 TO 100, TIME ON GT 100 (1-3)</td></tr><tr><td>140 ALL DECISION POSITIVE</td></tr><tr><td>150 *</td></tr><tr><td>160 CONSTRAINTS</td></tr><tr><td>170 *</td></tr><tr><td>180 * CONSTRAINT TYPE 1 - CANNOT ALLOCATE MORE TIME TO A</td></tr><tr><td>190 * CATEGORY THAN IS REQUIRED</td></tr><tr><td>200 *</td></tr><tr><td>210 DEFICIT ON LT 10 (1-3) .GE. 0</td></tr><tr><td>220 DEFICIT ON 10 TO 100 (1-3) .GE. 0</td></tr><tr><td>230 DEFICIT ON GT 100 (1-3) .GE. 0</td></tr><tr><td>240 *</td></tr><tr><td>250 * CONSTRAINT TYPE 2 - TOTAL TIME SPENT CANNOT EXCEED</td></tr><tr><td>260 * TIME AVAILABILITY</td></tr><tr><td>270 *</td></tr><tr><td>280 TOTAL TIME SPENT (TOTAL) .LE. 3900</td></tr></table>

Fig. 2. IFPS/OPTIMUM specifications.

? SOLVE

DO YOU AGREE THAT THIS PROBLEM IS LINEAR (YES, NO OR STOP)

? YES

PRINT INITIAL SOLUTION (YES OR NO)

? NO

OPTIMAL SOLUTION

ENTER SOLVE OPTIONS (OR END)

? ALL

<table><tr><td></td><td>HALF1</td><td>HALF2</td><td>OLDER</td><td>TOTAL</td></tr><tr><td>NUMBER LT 10</td><td>7000</td><td>2000</td><td>200</td><td></td></tr><tr><td>NUMBER 10 TO 100</td><td>500</td><td>100</td><td>20</td><td></td></tr><tr><td>NUMBER GT 100</td><td>150</td><td>50</td><td>20</td><td></td></tr><tr><td>TIME PER LT 10</td><td>1</td><td>.5000</td><td>1</td><td></td></tr><tr><td>TIME PER 10 TO 100</td><td>2</td><td>3</td><td>4.500</td><td></td></tr><tr><td>TIME PER GT 100</td><td>3</td><td>4</td><td>6</td><td></td></tr><tr><td>TIME REQUIRED LT 10</td><td>7000</td><td>1000</td><td>200</td><td></td></tr><tr><td>TIME REQUIRED 10 TO 100</td><td>1000</td><td>300</td><td>90</td><td></td></tr><tr><td>TIME REQUIRED GT 100</td><td>450</td><td>200</td><td>120</td><td></td></tr><tr><td>PARTIAL 10 TO 100</td><td>150</td><td>50</td><td>0</td><td></td></tr><tr><td>PARTIAL GT 100</td><td>45</td><td>25</td><td>0</td><td></td></tr><tr><td>FULL VALUE 10 TO 100</td><td>350</td><td>50</td><td>20</td><td></td></tr><tr><td>FULL VALUE GT 100</td><td>105</td><td>25</td><td>20</td><td></td></tr><tr><td>VALUE OF LT 10</td><td>56000</td><td>16000</td><td>1600</td><td></td></tr><tr><td>VALUE OF 10 TO 100</td><td>17950</td><td>2650</td><td>1000</td><td></td></tr><tr><td>VALUE OF GT 100</td><td>16020</td><td>3900</td><td>3000</td><td></td></tr><tr><td>TOTAL VALUE</td><td>89970</td><td>22550</td><td>5600</td><td></td></tr><tr><td>TIME ON LT 10</td><td>740</td><td>1000</td><td>0</td><td></td></tr><tr><td>TIME ON 10 TO 100</td><td>1000</td><td>300</td><td>90</td><td></td></tr><tr><td>TIME ON GT 100</td><td>450</td><td>200</td><td>120</td><td></td></tr><tr><td>TOTAL TIME SPENT</td><td>2190</td><td>1500</td><td>210</td><td>3900</td></tr><tr><td>VALUE LT 10 COLLECTED</td><td>5920</td><td>16000</td><td>0</td><td></td></tr><tr><td>VALUE 10 TO 100 COLLECTED</td><td>17950</td><td>2650</td><td>1000</td><td></td></tr><tr><td>VALUE GT 100 COLLECTED</td><td>16020</td><td>3900</td><td>3000</td><td></td></tr><tr><td>VALUE COLLECTED</td><td>39890</td><td>22550</td><td>4000</td><td>66440</td></tr><tr><td>DEFICIT ON LT 10</td><td>6260</td><td>0</td><td>200</td><td></td></tr><tr><td>DEFICIT ON 10 TO 100</td><td>0</td><td>0</td><td>0</td><td></td></tr><tr><td>DEFICIT ON GT 100</td><td>0</td><td>0</td><td>0</td><td></td></tr></table>

Fig. 3. Selected IFPS/OPTIMUM solution output.

PRINT SENSITIVITY ANALYSIS (YES OR NO)
? YES

<table><tr><td>VARIABLE NAME(COLUMN NAME)</td><td>OPTIMAL SOLUTION</td><td>OBJECTIVE COEFF</td><td>OPTIMAL (LOWER)</td><td>RANGE (UPPER)</td><td>VALUE TO ENTER</td></tr><tr><td>TIME ON LT 10(HALF1)</td><td>740</td><td>8</td><td>8</td><td>8.833</td><td>-</td></tr><tr><td>TIME ON LT 10(HALF2)</td><td>1000</td><td>16</td><td>8</td><td>-</td><td>-</td></tr><tr><td>TIME ON LT 10(OLDER)</td><td>0</td><td>8</td><td>-</td><td>-</td><td>8</td></tr><tr><td>TIME ON GT 100(HALF1)</td><td>450</td><td>35.60</td><td>8</td><td>-</td><td>-</td></tr><tr><td>TIME ON GT 100(HALF2)</td><td>200</td><td>19.50</td><td>8</td><td>-</td><td>-</td></tr><tr><td>TIME ON GT 100(OLDER)</td><td>120</td><td>25</td><td>8</td><td>-</td><td>-</td></tr><tr><td>TIME ON 10 TO 100(HALF1)</td><td>1000</td><td>17.95</td><td>8</td><td>-</td><td>-</td></tr><tr><td>TIME ON 10 TO 100(HALF2)</td><td>300</td><td>8.833</td><td>8</td><td>-</td><td>-</td></tr><tr><td>TIME ON 10 TO 100(OLDER)</td><td>90</td><td>11.11</td><td>8</td><td>-</td><td>-</td></tr><tr><td colspan="6">PRINT SHADOW PRICES (YES OR NO)? YES</td></tr><tr><td>CONSTRAINT VARIABLE</td><td>COLUMN</td><td colspan="2">FINAL VALUE</td><td colspan="2">SHADOW PRICES</td></tr><tr><td>DEFICIT ON LT 10</td><td>HALF1</td><td colspan="2">6260</td><td colspan="2">0</td></tr><tr><td>DEFICIT ON LT 10</td><td>HALF2</td><td colspan="2">0</td><td colspan="2">-8</td></tr><tr><td>DEFICIT ON LT 10</td><td>OLDER</td><td colspan="2">200</td><td colspan="2">0</td></tr><tr><td>DEFICIT ON 10 TO 100</td><td>HALF1</td><td colspan="2">0</td><td colspan="2">-9.950</td></tr><tr><td>DEFICIT ON 10 TO 100</td><td>HALF2</td><td colspan="2">0</td><td colspan="2">-.8333</td></tr><tr><td>DEFICIT ON 10 TO 100</td><td>OLDER</td><td colspan="2">0</td><td colspan="2">-3.111</td></tr><tr><td>DEFICIT ON GT 100</td><td>HALF1</td><td colspan="2">0</td><td colspan="2">-27.60</td></tr><tr><td>DEFICIT ON GT 100</td><td>HALF2</td><td colspan="2">0</td><td colspan="2">-11.50</td></tr><tr><td>DEFICIT ON GT 100</td><td>OLDER</td><td colspan="2">0</td><td colspan="2">-17</td></tr><tr><td>TOTAL TIME SPENT</td><td>TOTAL</td><td colspan="2">3900</td><td colspan="2">8</td></tr></table>

Fig. 4. Sensitivity analysis and shadow prices.

the average invoice value for receivables between \$10,000 and \$100,000 is estimated to be \$50,000, and the average partial payment amount is assumed to be \$3,000. Line 330 computes the total value for the three value categories. Lines 360 through 380 represent the decision variables for this model. The manager wants to find the optimal allocation of collection time among the different invoice types. Line 390 calculates the total allocated time. Lines 410 through 430 compute the expected collections for the different categories given the time allocations in lines 360 through 380. These relations reflect the critical assumption that the amount collected in each category is proportional to the time allocated. Line 440 computes the total collection. Lines 460 through 480 calculate the time short-fall from a given time allocation. Line 500 defines the special column (TOTAL) calculation for the variables TOTAL TIME SPENT and VALUE COLLECTED. The values for these variables are summed over all three columns.

In the actual case, attempts were made to find a satisfactory allocation using 'what if' analysis. However, out of frustration, the analysts finally resorted to IFPS/OPTIMUM to find the desired allocation more efficiently. Fig. 2 shows the IFPS/OPTIMUM specifications required to optimize the simplified model. Line 60 specifies the objective. Line 130 declares the decision variables of the problem – how much time to allocate to the different invoice types. Lines 210 through 230 specify constraints that ensure that the time allocated to a category does not exceed its requirement. The constraint in line 280 ensures that the total time allocated is within the availability limit. Fig. 3 shows selected solution output. It shows that the model is diagnosed as a linear. In that case, a linear programming routine is used to solve the problem. Fig. 4 shows the corresponding sensitivity analysis output and shadow prices.

Sensitivity analysis answers the question, 'How sensitive is the optimal solution to changes in certain key variables?' The first column of the sensitivity analysis output in Fig. 4 shows the optimal values of the decision variables and the second column (Objective Coeff column) shows the unit contribution to the objective value of each decision variable. These unit contributions are computed by OPTIMUM from the model equations. For the decision variable TIME ON LT 10(HALF1), the sensitivity analysis results in the columns of 'Optimal Range' state that the optimal solution would be unchanged for values of the objective coefficient between 8 and 8.833. For all the other decision variables (except TIME ON LT 10(OLDER)), the optimal solution is unchanged unless their objective coefficients (unit contributions) fall below 8. The sensitivity analysis essentially shows how much leeway you have in the objective coefficients, without affecting the optimal decision values.

The shadow price displayed in Fig. 4 answers the question 'How much will the objective change if I change a constraint limit?' For example, the shadow price of the constraint DEFICIT ON GT 100 (HALF1) is -\$27.6, meaning that VALUE COLLECTED would drop by -\$27.6 if the deficit is forced to be at least 1. The shadow prices essentially show which constraints affect the objective and how much, and therefore merit a closer examination.

The actual analysis verified the correctness of the existing policy of pursuing high value accounts first. It also showed that existing manpower is inadequate to follow up on the increasing volume of accounts receivable and that adding staff was justified. The management accepted and implemented the recommendations resulting from this analysis.

## 4. Dividend Policy Analysis

This application dealt with a controversial financial policy question – how much dividend should a company pay. Financial experts usually have a variety of recommendations on this question. The chemical firm in this case did not have a formal corporate dividend policy. But certain fundamental changes in the company's financial and operating positions, such as increasing cash flow from a new acquisition, dictated such a need. After considering several factors, the company decided to adopt a policy of paying a stable and increasing dividend – an approach generally used by many companies. Within this policy framework, the company was interested in finding a stable dividend growth rate that could be maintained in good and bad years, since the market would otherwise penalize the company's stock price if there is uncertainty in the dividends. In addition, it wanted the dividend policy to be in 'harmony' with other corporate goals such as growth in earnings per share, shareholder equity growth, net income growth, etc.

A financial model similar to the one in fig. 5 was constructed to analyze the impact of varying the dividend growth rate (line 280). The input to the model came from the company's latest five-year plan. It essentially involved income statement and capitalization data (lines 20, 30, 40, 60, 100, 240, 290, 320, 370). The model allowed the growth rate in dividends to vary (line 290). It assumed that when dividends exceed plan estimates (line 300) they are financed by debt (line 70). If a dividend payout different from the plan is made, the model recomputes the different ratios and performance parameters pertaining to the company. They include such items as the adjusted net income to common stock holders (line 90), adjusted common equity (line 150) and adjusted outstanding debt (line 170) and their percentages with respect to capitalization (lines 180, 200), earnings per share with increased dividends (line 230), net income growth rate (rate 350), shareholder equity growth rate (line 380), etc. The model essentially helps to accentuate the long-range implications of any dividend payout policy (line 280).

The model was initially supposed to take advantage of 'what if' and 'goal seeking' features of IFPS to examine alternative policies. The analyst soon realized that the process was extremely time consuming and that he could not enforce restrictions on certain variable values within those techniques. Hence he resorted to IFPS/OPTIMUM to find the best dividend payout policy. A number of

10 COLUMNS 1981-1985
20 OUTSTANDING DEBT = 3623,3390,3542,3290,2965
30 PREFERRED STOCK = 792,698,647,624,599
40 COMMON STOCK = 1561,1765,1876,1977,2139
50 CAPITALIZATION PER PLAN = OUTSTANDING DEBT + PREFERRED STOCK + COMMON STOCK
60 NET INCOME PER PLAN = 239,317,327,440,619
70 AFTER TAX INTEREST EXPENSE = 0.54 \* 0.12 \* '
80 (INCREASED IN TOTAL DIVIDENDS OVER PLAN/2 + PREVIOUS CUMULATIVE INCREASE IN DIVIDENDS)
90 ADJUSTED NET INCOME TO COMMON = NET INCOME PER PLAN - AFTER TAX INTEREST EXPENSE
100 SHARES OUTSTANDING = 38.543,41.231,45.352,46.532,51.324
110 DEBT TO CAPITALIZATION PER PLAN = (OUTSTANDING DEBT/CAPITALIZATION PER PLAN) \* 100
130 EQUITY TO CAPITALIZATION PER PLAN = (COMMON STOCK/CAPITALIZATION PER PLAN) \* 100
150 ADJUSTED COMMON EQUITY = COMMON STOCKS -'
160 CUMULATIVE INCREASE IN DIVIDENDS - AFTER TAX INTEREST EXPENSE
170 ADJUSTED OUTSTANDING DEBT = OUTSTANDING DEBT + INCREASE IN TOTAL DIVIDENDS OVER PLAN
175 ADJUSTED CAPITALIZATION = CAPITALIZATION PER PLAN - AFTER TAX INTEREST EXPENSE
180 ADJUSTED DEBT TO CAPITALIZATION = 100 \* (ADJUSTED OUTSTANDING DEBT/ADJUSTED CAPITALIZATION)
200 ADJUSTED EQUITY TO CAPITALIZATION = 100\* (ADJUSTED COMMON EQUITY/ADJUSTED CAPITALIZATION)
220 EPS PER PLAN = NET INCOME PER PLAN/SHARES OUTSTANDING
230 EPS WITH INCREASED DIVIDENDS = ADJUSTED NET INCOME TO COMMON/SHARES OUTSTANDING
240 DIVIDENDS 1980 = 64.521
250 DIVIDENDS PAID = DIVIDENDS 1980 \*'
260 (1+DIVIDEND GROWTH RATE/100), PREVIOUS \* (1+DIVIDEND GROWTH RATE/100)
270 DIVIDENDS PER SHARE = DIVIDENDS PAID/SHARES OUTSTANDING
280 DIVIDEND GROWTH RATE = 10,PREVIOUS
290 DIVIDENDS PER PLAN = 58.546,63.457,69.654,74.321,85.324
300 INCREASE IN TOTAL DIVIDENDS OVER PLAN = DIVIDENDS PAID - DIVIDENDS PER PLAN
310 CUMULATIVE INCREASE IN DIVIDENDS=PREVIOUS + INCREASE IN TOTAL DIVIDENDS OVER PLAN
320 NET INCOME 1980 = 79.986
330 NET INCOME AFTER TAX INTEREST EXPENSE = NET INCOME PER PLAN - AFTER TAX INTEREST EXPENSE
350 NET INCOME GROWTH RATE = ((L330-NET INCOME 1980)/NET INCOME 1980)\*100,)
360 ((L330-PREVIOUS L330)/PREVIOUS L330)\*100
365 CUMULATIVE NET INCOME GROWTH RATE = PREVIOUS + NET INCOME GROWTH RATE
370 COMMON EQUITY 1980 = 687.0
380 SHAREHOLDER EQUITY GROWTH RATE= ((ADJUSTED COMMON EQUITY - COMMON EQUITY 1980)/'
400 COMMON EQUITY 1980)\*100,((L150-PREVIOUS L150)/PREVIOUS L150)\*100

## Fig. 5. IFPS model.

10 \*
20 MAXIMIZE CUMULATIVE NET INCOME GROWTH RATE (1984)
30 \*
40 DECISIONS
50 DIVIDEND GROWTH RATE (1980) .GE. 0
60 \*
70 CONSTRAINTS
80 EPS WITH INCREASED DIVIDENDS (1981-1985) .GE. 6.2
90 CUMULATIVE INCREASE IN DIVIDENDS (1984) .GE. 57
100 SHAREHOLDER EQUITY GROWTH RATE (1981 THRU 1984) .GE. 4.7%
?SOLVE
DO YOU AGREE THAT THIS PROBLEM IS NONLINEAR (YES OR STOP)
?YES
PRINT INITIAL SOLUTION (YES OR NO)
?NO
LOCAL OPTIMUM FOUND
ENTER SOLVE OPTIONS (OR END)
?L280, L365, L380, L230, L310

<table><tr><td></td><td>1981</td><td>1982</td><td>1983</td><td>1984</td><td>1985</td></tr><tr><td>DIVIDEND GROWTH RATE</td><td>8.022</td><td>8.022</td><td>8.022</td><td>8.022</td><td>8.022</td></tr><tr><td>CUMULATIVE NET INCOME GROWTH RATE</td><td>177.9</td><td>212.2</td><td>215.7</td><td>252.0</td><td>294.3</td></tr><tr><td>SHAREHOLDER EQUITY GROWTH RATE</td><td>125.5</td><td>12.35</td><td>5.662</td><td>4.711</td><td>7.875</td></tr><tr><td>EPS WITH INCREASED DIVIDENDS</td><td>6.209</td><td>7.653</td><td>7.184</td><td>9.41</td><td>12</td></tr><tr><td>CUMULATIVE INCREASE IN DIVIDENDS</td><td>11.15</td><td>22.98</td><td>34.66</td><td>48.19</td><td>57.77</td></tr></table>

Fig. 6. IFPS/OPTIMUM specifications and the optimal solution.

different OPTIMUM formulations were actually used to arrive at the final dividend policy. Fig. 6 shows one such formulation that maximizes the cumulative net income growth over the 5-year planning horizon (line 20), keeps the earnings per share at an acceptable level (line 80), wants the shareholder equity growth rate to be more than 4.7% (line 100) and desires the cumulative increase in dividends to be at least 57. Given these restrictions, OPTIMUM finds the optimal dividend growth rate to be 8 percent, as shown in fig. 6. Management initially thought the dividend rate could grow at 10 percent.

If there was a multiple objective optimization capability in OPTIMUM, then this application would have been well suited for it. The analysts were actually trading-off between the different objectives in the different formulations. In each formulation, all the objectives except one were stated as constraints with lower bounds on them. An acceptable dividend policy emerged from the analysis.

## 5. Conclusions

Users of DSS tools are slowly realizing the value of optimization. They are gradually finding out the limitations of 'what if' and 'goal seek' type of analysis where restrictions cannot be imposed on certain model variables and a backward solution done to find satisfactory values for the decisions. In addition, they are realizing that performing optimization manually by trying different 'what if's' on the decision variables is a waste time, and that the power of mathematics embedded in the optimization tools could do a better analysis more efficiently.

From the many applications seen so far, it can be concluded that optimization will play an increasingly useful role in the analysis of DSS models. From the author's contacts with many of the DSS vendors, it seems that a number of other leading languages are planning to include optimization capabilities in the future. They would help to upgrade the 'what if' and 'goal seeking' mode of analysis to the 'what's best' mode with concurrent increases in productivity of the analysts and an enrichment of the DSS toolkit.

Practicing managers and management scientists should be aware of these emerging tools. As shown in this paper, they can open up new application horizons.

## References

[1] Carlsson, C., Fuzzy Multiobjective Programming With Composite Compromises, presented at the Task Force Meeting on Multiobjective and Stochastic Optimization at IIASA (Nov.-Dec., 1981).

[2] Cunningham, C., and L. Schrage, Optimization in Spreadsheets with VINO (Scientific Press, Palo Alto, CA, 1985).

[3] Geoffrion, A.M., Can MS/OR Evolve Fast Enough, Interfaces 13 (1983) 10–25.

[4] Roy, Asim, Emma De Falomir and Leon Lasdon, An Optimization-Based Decision Support System for a Product Mix Problem, Interfaces 12, No. 2 (April, 1982) 26–33.

[5] Roy, Asim, and Emma De Falomir, Selecting Products and Quantities: Making an Optimal Decision, Financial Case Report Series (Execucom Systems Corporation, Austin, TX 78766, 1981).

[6] Roy, Asim, Decision Support Systems - From Simulation to Optimization, Proceedings of the Fourteenth Hawaii International Conference on Systems Sciences 1 (1981).

[7] Roy, Asim, Introducing a Nonlinear Optimizer into a Financial Planning Language, Tenth International Symposium on Mathematical Programming (Montreal, Aug., 1979).

[8] Roy, Asim, and Terrie Huttner, Optimization with Decision Support Systems at Prime Computers – Two Applications, ORSA/TIMS Joint National Meeting (Houston, Oct., 1981).

[9] Roy, Asim, Optimization and Planning Languages, Fourth European Congress on Operations Research (Cambridge, England, July, 1981).

[10] Roy, Asim, L. Lasdon, and J. Lordeman, Extending Planning Languages to Include Optimization Capabilities, Management Science 32, No. 3 (March, 1986) 360–373.

[11] Russo, G., and S. Sarkar, A DSS for Plannig Petrochemical Production, Third International DSS '83 Transactions, G. Huber, ed. (June, 1983) 45–53.

[12] Wagner, G.R., Optimizing Decision Support Systems, Datamation (May, 1980) 209–214.
