---
otero_id: 22414
otero_key: "RWKNBBC5"
title: "Rho: A decision support system for pricing in law firms"
authors: "Madjid Tavana; QB. Chung; Dennis T. Kennedy"
year: "1998"
journal: "Information & Management"
doi: "10.1016/s0378-7206(97)00042-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Applications

# Rho: A decision support system for pricing in law firms

Madjid Tavana $^{a,*}$ , QB. Chung $^{1,a}$ , Dennis T. Kennedy $^{2,b}$

$^{a}$ Management Department, La Salle University, Philadelphia, PA 19141-1199, USA $^{b}$ Accounting Department, La Salle University, Philadelphia, PA 19141-1199, USA

Received 30 April 1997; accepted 16 August 1997

## Abstract

There is no single schedule of legal fees and the way they are calculated; a rational model of fee determination is acutely needed. This paper presents a decision support system called Rho that allows the user to enter the internal and external data into a set of decision models to determine the strategic pricing for law firms. The paper describes the main features of the system, the optimization model that plays a critical role in the decision process, an illustration of how the system was applied in a real setting, an assessment of the proposed approach and future research issues. © 1998 Elsevier Science B.V.

Keywords: Decision support systems; Model management systems; Optimization model; Law firms; Legal fees

## 1. Introduction

The complexity and heterogeneity of today's world have fostered growth in conflicts not only between individuals but also between large organizations, resulting in an increasingly litigious society. The need for more lawyers and the growth in the size and number of law firms show no signs of abating [27, 45]. In this environment, law firms are experiencing more frequent disagreements with their clients over legal bills. Problems in billing are not unusual inside nor outside the legal profession [11, 14, 21, 34]. In some cases, legal bills are brought to court for judicial decisions [24]. This is in contrast to what used to be the typical attorney's bill that stated 'for professional services rendered' followed by the amount charged.

## 1.1. Alternative billing methods for legal services

While various methods are employed by different US law practitioners for different types of services, these procedures can be categorized into a few groups. The first and most frequently used billing method is hourly; that is, charging by hours spent on the activity. As this traditional approach was often found inappropriate, several alternative billing methods were substituted. These value billing methods include unconventional time-based billing, fixed fees, and result-based billing $[13, 25, 41]$ .

In hourly billing, law firms calculate legal fees by multiplying a predetermined hourly rate by the number of hours the lawyer spends. Since the hourly billing method was originally the industry standard, law practitioners became accustomed to keeping track of their billable hours. Theoretically, measuring them is straightforward. Then, it became a simple matter to calculate a law firm's revenue or to project future revenues based on estimated billable hours. However, this approach presents a conflict of interest with clients [32], invites corruption in the billing process, and generates a cynicism that subverts the professional-client relationship [38]. While law firms find it inadequate to set fees arbitrarily, surveys show that this billing method is predominant [17, 47].

The primary basis for unconventional time-based billing is the amount of time a lawyer spends on a case and the billing amount still depends on the hourly rates; however, these methods use blended or discount rates. A blended rate assigns one uniform hourly rate for all partners and associates, and sometimes for use of paralegals as well. This results in an averaged rate, one that is far less than the rate of experienced partners yet higher than that of associates or paralegals. This encourages effective project management by assigning tasks to people who are least expensive. There are different discount billing methods. A discounted hourly rate is generally established before the project begins. If a time-based discount method is used, the legal fee is calculated after the work is completed using the standard rate, then a predetermined percentage that varies with the time of the engagement is used to determine the final charge. In volume discounting, a law firm agrees to reduce its hourly rates or final bills in exchange for a guaranteed amount of legal work. This is sometimes called full purchasing.

With fixed fees, a flat or maximum dollar amount is set for the legal services based on the type of service provided. This method forces the firm to manage projects effectively because the profit will otherwise be reduced or lost. There are several forms of fixed fees, including task-based fees, client-based fees, fee cap, result-based bonuses, and budget billing.

Result-based billing, like fixed fees, shifts risk from the client to the firm. The fees vary, depending on results. Before starting, the client and the firm define a positive outcome and the incremental fees associated with it. This arrangement is intended to promote more effective project management. The risk to the firm is that a negative outcome will result in less revenue. The concept of result-based billing has emerged as several alternatives: result-based fixed fees; result-based bonuses; contingent fees; defense contingency billing; premium billing; and cost-plus pricing.

In the law community, there has been much discussion of ways to structure legal fees $[31, 36, 37]$ . This phenomenon clearly indicates that: (1) there is no consensus among law practitioners on how legal fees should be determined; and (2) there is an acute need for a rational model of fee determination.

## 1.2. Review of relevant literature

The fee paid to or income of a lawyer is typically determined by the lawyer's specialty, education, experience, title, and reputation. While clients might want to hire a lawyer or a law firm that would charge less, this will not be the deciding factor when selecting professional service firms [30, 35]. The implication is that a good-pricing strategy or a competitive price is not a core competence for a law firm [28, 29]. Nevertheless, a good-pricing strategy coupled with reliable analytical techniques is essential to the survival of the firm. As the demographics of clients shift from individuals to corporations, more clients can afford the financial and human resources to challenge legal bills, and their details are constantly under scrutiny, either by the client organizations or third parties [3, 5, 12, 42]. This trend requires a change in the way law firms determine their legal fees: not only to reduce the burden and nuisance of fee settlement disputes but also to approach the billing process in a way that makes sense for both the law firm and the client.

Both Auty [2] and Forsyth [8] observe that the difficulties of setting professional fees have received limited analytical attention in the standard pricing references. In those publications that do consider it, the discussions are essentially descriptive and provide little pragmatic guidance for managers facing real-life decisions [20, 26, 48]. In much of the research literature, the issue of pricing historically has been confusing. For example, discussions of degenerate close-loop Nash solutions [7] and artificial feedforward networks with hidden units and backpropagation [15] are difficult concepts in practice. Furthermore, Gijsbrechts [9] notes that normative pricing models are often restricted to impractical cases and in many instances unrealistically ‘assume fully informed companies and optimal competitive reactions.’

The research primarily examines the factors associated with variability in audit fees. These studies provide evidence that client size and complexity are the most important factors affecting audit fees. Gist [10] replicated prior audit fee research using a more recent sample of 95 US publicly held firms. While client size and complexity explained most of the variation in audit fees, the client's financial condition, the audit firm's size and the client's regulatory aspects were also significant. Essentially, these studies identify underlying conditions that determine the quantity and quality of professional resources required to provide services to a client. Although they explain variability in pricing, they do not determine how to establish absolute price levels for specific firms serving specific clients. Both Forsyth and MacErlean [22] argue that the primary task in setting professional fees is to establish the value of the required skills.

Auty [2] designed and tested a model to make professionals associated with the construction industry more aware of their costs in providing different levels of service and, therefore, be better able to judge what fee to charge. The project was addressed as a material requirement planning exercise with two components. Initially, costs per billable hour were estimated for each fee-earning grade of professional. Then, client size and complexity, along with eleven other factors, were used to estimate the quantity of resources required to provide particular services. Field testing revealed that the participants did not appear to use the proposed method in setting fees. They indicated, in their responses to a questionnaire, that the model was too complex and did not reflect the way they did business.

Auty's research provides several lessons for setting professional fees. First, prevailing market conditions are a critical element in estimating the value of professional skills. How other firms are pricing their resources must be considered in building a fee-setting model. Second, any attempt to establish guidelines for setting fees should be based on an understanding of the particular firm's actual practices and should incorporate each firm's own historical data if the proposed process is not to be rejected by the professionals as inappropriate. Third, the participating professionals thought the method was too complex, and they overwhelmingly suggested that the number of factors be reduced. While complexity should be viewed as a constraint, she also recommended that the proposed process be computerized so that ‘complexity can be hidden from the user.’ Similarly, Gijsbrechts suggests, “A fruitful area for future work is the development of knowledge based pricing systems to help managers decide on appropriate pricing schemes in their particular situation.”

Our research is motivated by these needs and provides rational guidelines for reaching optimal solutions to the fee-setting problem. A decision support system (DSS) called Rho was developed to incorporate key-decision models with the internal and external data relevant to the decisions.

## 2. Architecture of Rho

DSS are developed to solve unstructured and semi-structured problems $[18, 39, 40, 46]$ . With minimum training, users can take advantage of various features of the system to make better business decisions $[16]$ . Typically, a DSS supports sophisticated analyses and forecasting by providing access to a vast amount of data stored in the database. Decision models available from the modeling side of the system present powerful tools that augment the human problem-solving process $[19, 23]$ . Rho is a DSS that is designed to facilitate either individual or collaborative judgments about the strategic pricing of legal services. Employing DSS has proven to be effective in collaborative decision-making environments $[44]$ . The basic components of Rho are the database, a model base, and a user interface.

The database contains relevant data for a situation using a database management system. Rho is designed to access relevant internal and external time series data including:

\- financial data – revenues, direct and indirect costs, and profits;

\- human resources data – staffing information, historical billing rates by category, and annual salaries paid to individual lawyers;

\- operational data – billable hours by category; and

\- market intelligence – billing rates of competitors.

The model base is a repository of financial, statistical, and other operations research and management science methods, resulting in model management [6, 49]. Rho can take advantage of various forecasting models and a specially developed optimization model.

Table 1
Staffing data

<table><tr><td>Rank</td><td>Year 1</td><td>Year 2</td><td>Year 3</td><td>Year 4</td><td>Year 5</td><td>Year 6</td><td>Year 7</td></tr><tr><td>Senior partner</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>Junior partner</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>Senior associate</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>9</td></tr><tr><td>Fifth year associate</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>3</td><td>2</td></tr><tr><td>Fourth year associate</td><td>0</td><td>0</td><td>0</td><td>0</td><td>3</td><td>2</td><td>1</td></tr><tr><td>Third year associate</td><td>0</td><td>0</td><td>0</td><td>3</td><td>2</td><td>1</td><td>1</td></tr><tr><td>Second year associate</td><td>0</td><td>0</td><td>3</td><td>2</td><td>1</td><td>1</td><td>1</td></tr><tr><td>First year associate</td><td>0</td><td>3</td><td>2</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>Total</td><td>14</td><td>17</td><td>19</td><td>20</td><td>21</td><td>22</td><td>22</td></tr></table>

Note: The current year is year 6, and the optimal rates for year 7 are being determined.

The user interface lets the user access both the database and the model base. As the decision-making process progresses, the user may need to view historical data, to make projections by feeding the data into selected forecasting models, and to manipulate parameters of the optimization model.

## 3. Development of the optimization model

Professional fees, that makes sense, begin with hourly rates. Rho is designed to provide a systematic approach in determining rational hourly rates. Obviously, the development of guidelines for setting fees should begin with an understanding of the specific firm's current practices. Rho was developed by the authors at $M\&T^{3}$ , a medium-size, regional law firm with corporate clients, located in a major metropolitan area in New England. As presented in Table 1, M&T currently employs 22 attorneys in several professional ranks.

In determining hourly rates, one must consider the objective of the pricing decision and both the external and internal factors relevant to the decision. Based on discussions with those responsible for the fee-setting strategy at M&T, these elements were identified as profitability, competitiveness, and the firm's track record.

## 3.1. Profitability

Legal bills should not only cover the cost to run the business but also ensure a certain level of profit $[1, 4, 43]$ . The primary objective of the pricing decision is achieving a profit level comparable to or exceeding the profit in the previous year.

## 3.2. Competitiveness

To stay competitive, the firm adjusts to the rates of other firms even if it does not match them. Hourly rates of law firms in many regions are surveyed and published in various law practitioners' journals and newspapers [33].

## 3.3. Track records

Hourly rates are also a function of internal factors such as rank, experience, and the rate or salary history. For example, a partner's hourly rate for the next year would depend on this year's rate if the firm is in a steady condition. M&T, like other law firms, maintains certain salary gaps between different ranks or groups with different years of tenure.

Profitability and competitiveness are competing elements: One tends to increase hourly rates while the other tends to lower them. Since M&T seeks to maximize its profits, it would be inclined to increase hourly rates. However, taking the competitiveness criterion into consideration for its long term survival, M&T would need to keep its rates within a reasonable range. This situation requires an analytic decision

Maximize profit $\sum_{i=1}^{n}\left(h_{i,t}\rho_{i,t}\right)-E_t$

(1)

subject to

$$
\sum_ {i = 1} ^ {n} \left(h _ {i, t} \rho_ {i, t}\right) - E _ {t} - \Pi_ {t - 1} > 0,\tag{2}
$$

$$
l _ {i} \leq \rho_ {i, t} \leq u _ {i}, \quad i = 1,..., n,\tag{3}
$$

$$
\rho_ {i, t - 1} \leq \rho_ {i, t} \leq p _ {i} \rho_ {i, t - 1} \quad i = 1, \dots , n, \text { and } t > 1,\tag{4}
$$

$$
\gamma_ {i} \rho_ {i + 1, t} \leq \rho_ {i, t} \quad i = 1, \dots , n - 1,\tag{5}
$$

where

$\rho_{i,t} =$ the decision variable, hourly rate of lawyers at level $i$ at year $t$ ,

i = level at which a lawyer is ranked (e.g., 1 for senior partners,

2 for junior partners, 3 for senior associates, etc.),

n = number of levels,

$h_{i,t}$ = sum of billable hours of lawyers at level $i$ at year $t$ ,

$E_{t} =$ total expenses at year $t$ (projected, if in the future),

$\Pi_{t} = \text{net profit at year } t$ (projected, if in the future),

$l_{i}$ = lower bound of hourly rate for level i based on market intelligence,

$u_{i}$ = upper bound of hourly rate for level $i$ based on market intelligence,

$p_{i} =$ rate of increase in hourly rate for level $i$ for the next year,

$\lambda_{i} =$ gap between the hourly rates for levels $i$ and $i - 1$ (ratio).

Fig. 1. The optimization model.

process that renders optimal levels of hourly rates using linear programming. Because both elements are a function of hourly rates, the optimization model is constructed so that hourly rates are the decision variables, profit maximization is the objective, and the competitiveness requirement and hourly rate track records are constraints. Our optimization model is shown in Fig. 1.

\- The model incorporates a few premises that reflect the operations of $M \& T$ .

\- Revenue produced by those at a particular rank is calculated by multiplying the sum of billable hours by the rank-specific hourly rate. Summing the revenue for each rank across the hierarchy yields the total revenue.

\- There is a hierarchy within the firm.

\- Profit is total revenue less total expenses; the objective of this model is to maximize the profit.

\- The profit for the next year should exceed that of this year.

\- The same hourly rates apply to everyone at the same rank.

\- Based on the market rates, a set of upper and lower limits is established so the firm's rates fall between them. This captured the way $M \& T$ dealt with competition.

\- Next year's rate for a given rank can be higher than the current one, but there is a percentage limit on this.

\- The firm maintains a gap between the hourly rates of any two adjacent ranks; this can be expressed as a ratio. For example, if the gap between the rates of rank 3 and 4 should be greater than 10%, a constraint that $\rho_{3}>(1.1)\rho_{4}$ , or $\rho_{3}/\rho_{4}>1.1$ can be established.

These specifications represent the important operational details of the firm. More realistic models can be developed by introducing more specific conditions or by eliminating oversimplified elements.

## 4. Rate determination with Rho: An illustration

The data provided by M&T were used to demonstrate how Rho supports the rate-determination process. After data collection, the forecasting models in the model base were utilized to estimate the parameters required by the optimization model. Next, the optimization model was used to calculate the optimal hourly rates and the expected net profit. Then, the output from the model was given to the managing partners to aid them in setting policies.

## 4.1. Strategic evaluation of parameters

The projections for year 7 were provided by the managing partners of the firm. The expected billable hours by rank $(h_{i,t})$ for year 7 are necessary for projecting revenue and profit in equations (1) and (2). in Fig. 1. The billable hours for year 7 were forecast using a linear-regression model on historical data.

Some operating expenses for year 7 ( $E_{t}$ ), such as salaries, rental costs, and malpractice insurance, were calculated using currently available information. Other expenses for year 7, including the costs of computer services, supplies, postage, utilities, were forecast based on expected activity levels. It should be noted that the net profit for the current year ( $\Pi_{t-1}$ ) is the difference between total revenue and total operating expenses for year 6. Total revenue is the aggregation of rank-wise billable hours multiplied by the applicable rate. All the historical data required for calculating $\Pi_{t-1}$ were available from the database.

Table 2  
Comparison of revenues in years 5 through 7

<table><tr><td>Revenue</td><td>Year 5</td><td>Year 6</td><td>Year 7</td></tr><tr><td>Based on Rho&#x27;s recommendation</td><td>$4,413,000</td><td>$4,842,000</td><td>$5,236,000</td></tr><tr><td>Actual revenue</td><td>$4,161,000</td><td>$4,568,000</td><td>-</td></tr><tr><td>Difference (Foregone revenue)</td><td>$252,000</td><td>$274,000</td><td>-</td></tr></table>

M&T had collected the rates of twelve competitors in previous years. This market intelligence made it possible to forecast its competitors' rates and to establish a strategic domain for the firm's rates. The boundaries for the firm's hourly rates were established in consultation with the managing partners who maintained that the upper and lower limits for the firm's rates ( $l_{i}$ , and $u_{i}$ ) were the projected average market rate for each professional rank plus and minus one standard deviation. In addition, they believed that the gap between each of the adjacent ranks ( $\gamma_{i}$ ) should be at least 5% except for a 10% gap between junior partners and senior associates. The revenues in the prior year (5), the current year (6) and the predicted year (7) are shown in Table 2.

## 4.2. Policy review

With the evaluation of the parameters completed, the next step was running the optimization model to obtain the optimal hourly rates. Substituting the required parameters into the model yielded the detailed LP model for year 7 presented in Fig. 2. However, when the model was presented to the partners, they observed that the recommended hourly rates, with the exception of $\rho_{5}$ , coincided with the upper boundary of the track record constraint. They recognized that the firms' hourly rates were being constrained by the rate of increase policy. This prompted the partners to request that the model be run for years 5 and 6 so that they could examine the relationships between the competitiveness and track record constraints over time.

The Rho optimization model was run with the actual data from years 5 and 6. The charts in Fig. 3 depict the feasibility bands that are defined by two of the

```txt
Maximize
(1) Revenue
8020ρ₁ + 5154ρ₂ + 15565ρ₃ + 3195ρ₄ + 1524ρ₅ + 1454ρ₆ + 1420ρ₇

Subject to
(2) Profitability constraint
8020ρ₁ + 5154ρ₂ + 15565ρ₃ + 3195ρ₄ + 1524ρ₅ + 1454ρ₆ + 1420ρ₇ - 4810500 > 0,
(3) Competitiveness constraints
163 ≤ ρ₁ ≤ 196,
150 ≤ ρ₂ ≤ 180,
134 ≤ ρ₃ ≤ 159,
123 ≤ ρ₄ ≤ 144,
116 ≤ ρ₅ ≤ 132,
105 ≤ ρ₆ ≤ 120,
97 ≤ ρ₇ ≤ 109,
(4) Track record constraints (Rate of increase)
155 ≤ ρ₁ ≤ 171,
143 ≤ ρ₂ ≤ 157,
125 ≤ ρ₃ ≤ 138,
117 ≤ ρ₄ ≤ 129,
112 ≤ ρ₅ ≤ 123,
102 ≤ ρ₆ ≤ 112,
93 ≤ ρ₇ ≤ 102,
(5) Track record constraints (Gap ratios)
ρ₁ ≥ 1.05 ρ₂,
ρ₂ ≥ 1.10 ρ₃,
ρ₃ ≥ 1.05 ρ₄,
ρ₄ ≥ 1.05 ρ₅,
ρ₅ ≥ 1.05 ρ₆, and
ρ₆ ≥ 1.05 ρ₇.

The Solution
ρ₁ = 171, ρ₂ = 157, ρ₃ = 138, ρ₄ = 129, ρ₅ = 122.86, ρ₆ = 112, and ρ₇ = 102
Total Revenue = $5,236,000
Net Profit = $1,447,000
```  
Fig. 2. Illustration of optimization model and the solution.

policies. In one policy, the firm incorporates external market conditions by requiring its hourly rates to be within one standard deviation of the average of its competitors' rates. This policy is represented by the market low and market high boundaries. The other policy states that the hourly rate for any rank should not be less than it is in the current year and should not be increased by more than 10%. This policy is delineated by the current year rate and raise limit boundaries. The gap ratio policy is not included because it is not relevant in defining the feasible regions; rather, it considers the relative positions of the rates for the different ranks within the feasibility bands. The actual hourly rates for each rank are also presented.

Market Low Market High Current Raise Limit Year 6 Actual  
![](/api/attachments/RWKNBBC5/fulltext/images/68a809282bfee7a00976a13c67c4fb7ec854963a15d13bbf93b8c4efad9d8287.jpg)  
Market Low Market High Current Raise Limit Year 5 Actual

![](/api/attachments/RWKNBBC5/fulltext/images/bb19f490b25e15c4b511f684a997eefe945a8a0bb1833896e7812e64fa6f4d27.jpg)

![](/api/attachments/RWKNBBC5/fulltext/images/fcb1970109f77e0c4095fc86a84374ebf04b2b739349968ecb33e82ef1f5dfa2.jpg)  
Fig. 3. Comparison of feasibility bands for years 5 through 7.

An examination of the feasibility bands for years 5 and 6 reveals that the firm had been very conservative in setting hourly rates across all ranks. The actual rates for both years are in the lower region of the feasibility band, far below both the upper market limit and the raise limit. Based on these observations, the partners decided to use Rho to help them with the decision process for year 7. While the recommended rates were considerably higher than they would have been if past practice of years 5 and 6 had been followed, the shape and position of the feasibility band for year 7 is quite different from previous years. The width of the feasibility band is much narrower, and its lower boundary is the lower market limit rather than the firm's prior year rates. Furthermore, the upper limit of the feasibility band in both of the previous years is defined by both the projected market high and the raise limit. In contrast, the upper boundary for year 7 is simply the raise limit, and there is a conspicuous gap between the raise constraint and the upper market limit.

The changes in the feasibility band were occurring because the 10% rate limit policy was restricting the firm's hourly rates to a slower growth than was occurring in the market. Consequently, the firm's hourly rates had fallen considerably below the average of its competitors. The partners were concerned about these trends, and they held several meetings to discuss them. They identified potentially negative implications for the firm's financial performance, market image, recruiting, and retention. Therefore, the partners decided to increase the raise limit to 15% and adopt the revised hourly rates suggested by Rho for year 7. A graphical display of this policy decision is presented in Fig. 4. Also presented are the projected revenue based on both the Rho recommended rates with the previous 10% raise limit and the revised 15% raise limit policies together with the actual revenue for years 5, 6 and 7.

If M&T had continued the fee-setting patterns depicted in Fig. 3(c), it is likely that both revenue and profit for year 7 would have been less than projected by Rho under the 10% policy. With the Rho recommended rates, however, both actual revenue and profit for year 7 exceeded the projection under the 15% raise policy. While it was possible that billable hours would decrease as the hourly rates increased, examination of the billing records revealed that total billable hours had increased. The rate of increase was associated with a corresponding decrease in the number of billable hours per case. However, the firm was then able to accept more cases and actually increase its total billable hours at the same time it was increasing rates.

![](/api/attachments/RWKNBBC5/fulltext/images/7c847463c4ec9d8e7f842de8727c2b02da8e7c42010d1387c1d767eb980ab47c.jpg)  
Fig. 4. Comparison of revenues based on different scenarios for years 5 through 7.

From the outset, the Rho project was enthusiastically received by the managing partners at M&T. They had been aware of the fee setting problems for some time, and Rho provided a vehicle for a systematic analysis of the related issues. The partners concern about the competitiveness of the firm had dominated fee setting. Rho demonstrated how their emphasis on competitiveness had sacrificed the profitability of the firm and actually threatened the long-term survival of M&T. Because of these experiences, Rho was adopted enthusiastically by the managing partners. Not only did they use it for strategic pricing, but they also began to use it to challenge assumptions and revise policies. Rho has resulted in an increase in revenues and profits for M&T.

## 5. Conclusion

While many different billing practices are currently employed in the legal profession, there has been limited pragmatic guidance for valuing professional services. Rho provides an LP-based DSS to help managers develop pricing strategies for legal services that reflect the market circumstances confronting their firm and its particular way of doing business. The experience at M&T illustrates that the benefits of using Rho are derived not only from the determination of an optimal fee structure from a particular set of operational policies, but also from the group dynamics that it encourages. Once a decision model is built, it can be run to yield a desired set of solutions, or it can be test run with different scenarios to conduct what-if analyses. Rho shelters managers from computational complexity and numerical details, allowing them to concentrate on the strategic analysis of different policies. When this analysis is conducted in a group decision-making session, unrecognized managerial issues are revealed and management responses generate a common understanding that contributes to the development of group-decision models. In addition to providing management with a systematic approach to developing pricing strategies, Rho also provides a rational explanation of the firm's policies for its clients.

The DSS proposed in this paper can aid partners in systematically setting hourly rates and help them justify the rates to themselves and their clients. Further, it will provide the firm with the flexibility to establish ‘value billing.’

## Acknowledgements

The authors wish to thank Professor Sibley and the anonymous reviewers for their useful comments.

## References

[1] R.J. Arndt, Techniques for enhancing law firm profits, Legal Economics 13(7), 1987, pp. 26–30.

[2] S. Auty, Designing and testing a resource-based method for setting professional fees, Journal of Professional Services Marketing 13(2), 1996, pp. 71–92.

[3] J.E. Bahls, Laying down the law on legal fees, Nation's Business 76(10), 1988, pp. 54R–55R.

[4] W. Bower, Practice management and profitability, Law Practice Management 17(3), 1991, pp. 43–45.

[5] E.R. Browne, Clamping down on legal costs, Mortgage Banking (1992) 67–71.

[6] Q.B. Chung and R.M. O'Keefe, A formal analysis of model management literature, Annals of Operations Research 38(1)-4, 1992, pp. 137-176.

[7] E. Dockner and A. Gaunersdorfer, Strategic new product pricing when demand obeys saturation effects, European Journal of Operational Research 90, 1996, pp. 589–598.

[8] P. Forsyth, Marketing Professional Services: A Handbook, London: Financial Times/Pitman, 1992.

[9] E. Gijsbrechts, Prices and pricing research in consumer marketing: Some recent developments, International Journal of Research in Marketing 10, 1993, pp. 115–151.

[10] W. Gist, Explaining variability in external audit fees, Accounting and Business Research 23(89), 1992, pp. 79–84.

[11] S.B. Goldberg, The ethics of billing: A round table, ABA Journal (1991) 56–60.

[12] G. Greenfield, Harnessing the cost of legal bills, Risk Management (1993) 28–32.

[13] G.C. Hazard, Ethics: In many firms the practice of billable hours has become insidious, The National Law Journal 14(24), 1992, pp. 19–20.

[14] L. Himelstein, The verdict: Guilty of overcharging, Business Week (1993) 62–63.

[15] H. Hruschka, Determining market response functions by neural network modeling: A comparison to econometric techniques, European Journal of Operational Research 66, 1993, pp. 27–35.

[16] M. Igbaria and R.H. Sprague, Jr., C. Basnet and L. Foulds, The impact and benefits of a DSS: The case of fleet manager, Information and Management 31, 1996, pp. 215–225.

[17] D. Itkin, The economics of practicing law: A 1992 snapshot, Wisconsin Lawyer 10, 1993, pp. 10–14.

[18] P.G.W. Keen, M. Scott Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley: Reading: MA, 1980.

[19] M.C. Kettlehut, Using a DSS to incorporate expert opinion in strategic product development funding decisions, Information and Management 20, 1991, pp. 363–471.

[20] P. Kotler, P. Bloom, Marketing Professional Services, Englewood Cliffs, NJ: Prentice-Hall, Inc., 1984.

[21] I.B. Levinson, Winning the legal costs game, Management Review (1993) 34–37.

[22] N. MacErlean, Fees on a downward spiral, Accountancy (UK) 111, 1993, pp. 32–33.

[23] H. Min, A model-based decision support system for locating banks, Information and Management 17, 1989, pp. 207–215.

[24] D. Molvig, Breaking away from the billable hour, Law Office Economics and Management 33(2), 1992, pp. 131–138.

[25] National Law Journal, Sampler of rates around the country, 15(12) (1992).

[26] A. Palmer, C. Cole, Services Marketing: Principles and Practice, Englewood Cliffs, NJ: Prentice-Hall, Inc., 1995.

[27] Philadelphia Inquirer, The Workforce in 2005, 5 (1994).

[28] C.K. Prahalad, The role of core competencies in the corporation, Research Technology Management 36(6), 1993, pp. 40–47.

[29] C.K. Prahalad and G. Hamel, The core competence of the corporation, IEEE Engineering Management Review 20(3), 1992, pp. 5–14.

[30] J. Rathmell, Marketing in the Service Sector, Cambridge MA: Winthrop, 1974.

[31] R.C. Reed, J.W. McRae, K.S. Marshall, A.W. SoRelle and E.R.S. Alvarez, Alternative billing methods: A Status report from the task force, Legal Economics 15(6), 1989, pp. 18–26.

[32] D. Rubinstein, How much to charge: The subject they don't teach in law school, The National Law Journal 15(32), 1993, pp. S10.

[33] K. Rutman, J. Scorza, C.M. Neal, C.K. Lawrence, D. Stickle, Hourly rates for partners and associates, The National Law Journal 15(12) (1992).

[34] L.W. Schonbrunn, Reining In Legal Fees, Across The Board, 1992, pp. 53–54.

[35] H. Simon, Price Management, Amsterdam: Elsevier Science, 1989.

[36] M. Slade, Revolution in Lawyers' Fees: The Meter Is Being Shut Off, New York Times, 1993.

[37] R. Smith, How Do Law Firms Set Their Fees? California Law Business, 1990.

[38] B. Solomon, R. Gibbsons, Coming to terms with new billing methods, National Law Review 15(12) (1992) pp. S4, 42.

[39] R.H. Sprague, A framework for the development of decision support systems, MIS Quarterly 4(2), 1980, pp. 1–26.

[40] R.H. Sprague, E.D. Carlson, Building Effective Decision Support Systems, Englewood Cliffs, NJ: Prentice-Hall, Inc., 1982.

[41] A. Stevens, ABA Tackles Firms' Tendencies For Creative Clockwork in Billing, Wall Street Journal (1993).

[42] A. Stevens, As Some Clients Grow Bill-Savvy, Others May Find They Get the Tab, Wall Street Journal (1994).

[43] M.J. Strausser, Fees to Profit By, ABA Journal, Mar. (1991) 53–54.

[44] B.C.Y. Tan, H. Teo and I. Wei, Promoting concensus in small decision making groups, Information and Management 28, 1995, pp. 251–259.

[45] Wall Street Journal, Looking good: Where the fast growth is and will be, 1995.

[46] C. Wagner, Decision support systems for messy problems, Information and Management 28, 1995, pp. 393–403.

[47] T. Weidlich, Billing picture reveals a mix of alternatives, The National Law Journal (1993).

[48] E. Wheatley, Marketing Professional Services, Englewood Cliffs, NJ: Prentice-Hall, Inc., 1983.

[49] H.J. Will, Model management systems, information systems and organizational structure, in: E. Grochla, N. Szyperski (Eds.), Walter de Gruyter, 1975, pp. 467–483.

![](/api/attachments/RWKNBBC5/fulltext/images/2f45947309f2f67feebfdac8f9eb9bf0e01b90089d1156142451ac57357d3655.jpg)  
Madjid Tavana is Chairman of the Management Department and Associate Professor of Management Information Systems at La Salle University where he has also served as the Director of the Center for Technology and Management. Dr. Tavana has been a Visiting Scholar at the Anderson Graduate School of Management at UCLA and a Faculty Fellow in Aeronautics and Space Research at NASA – Kennedy Space Center for two

consecutive years. He received an M.B.A. in Management Science from La Salle University and a Post-Master of Information Systems from Drexel University. Dr. Tavana completed his doctoral coursework in Systems Sciences at the Wharton School of the University of Pennsylvania and received his Ph.D. in Management Information Systems from the American University of London. He has also received a Post-Doctorate in Strategic Decision Making from the Wharton School of the University of Pennsylvania. Dr. Tavana has published in such journals as Decision Sciences, Omega, Computers and Operations Research, International Journal of Operations and Production Management, Expert Systems with Applications, Journal of Behavioral Decision Making, Journal of International Information Management, Journal of Management Systems, Interface, Accounting Enquiries, and Organizational Behavior and Statistics.

![](/api/attachments/RWKNBBC5/fulltext/images/c8b5451fe40c6c8330af1ff39ab879614179cb5a35072b1a46f2d04dc0636d7c.jpg)

Q.B. Chung is Assistant Professor of Management Information Systems at La Salle University. Dr. Chung received an MBA from State University of New York at Albany and a Ph.D. in Management from Rensselaer Polytechnic Institute. His research focuses on enhancing the quality of managerial decision through Information Technology and quantitative methods of Operations Research and Management Science, along with the

socioeconomical issues surrounding IT such as electronic commerce and strategic alliances. He has published in such journals as Annals of Operations Research, European Journal of Information System, Intelligent Systems in Accounting, Finance and Management, and Omega.

![](/api/attachments/RWKNBBC5/fulltext/images/a53de29f038fe6a9de1669c4c09790fbb394fdc5d60eab5963bd231051e78779.jpg)

Dennis Kennedy is an Associate Professor of Accounting at La Salle University. Dr. Kennedy teaches graduate and undergraduate courses in financial accounting, and seminars on the conceptual framework and measurement issues in accounting. He received an M.B.A. and Ph.D. in Accounting from Temple University. Dr. Kennedy has published in such journals as Journal of

Accounting, Auditing and Finance, Omega, Journal of Behavioral Decision Making, Journal of Management Systems, Interface and Accounting Enquiries.
