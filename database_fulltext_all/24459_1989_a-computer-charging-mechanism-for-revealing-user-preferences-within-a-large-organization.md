---
otero_id: 24459
otero_key: "MZ77NASB"
title: "A Computer Charging Mechanism for Revealing User Preferences within a Large Organization"
authors: "Roger Alan Pick; Andrew B. Whinston"
year: "1989"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1989.11517850"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Computer Charging Mechanism for Revealing User Preferences within a Large Organization

Roger Alan Pick & Andrew B. Whinston

To cite this article: Roger Alan Pick & Andrew B. Whinston (1989) A Computer Charging Mechanism for Revealing User Preferences within a Large Organization, Journal of Management Information Systems, 6:1, 87-100, DOI: 10.1080/07421222.1989.11517850

To link to this article: http://dx.doi.org/10.1080/07421222.1989.11517850

![](/api/attachments/MZ77NASB/fulltext/images/bd64e1df5ed2b4f3dff8d6359c4ca6c54e2d1fa0ce968e9feedb0038c89f436a.jpg)

Published online: 22 Dec 2015.

![](/api/attachments/MZ77NASB/fulltext/images/64ab6221cae05ad181584d4d38a77cff1e6942ed4cd052784284c2c563f1fbaf.jpg)

Submit your article to this journal ↗

![](/api/attachments/MZ77NASB/fulltext/images/82531592d75a8a8bf5e13eb8d588af4e697c3597218ed7c12aed74c9ae19a320.jpg)

View related articles ↗

![](/api/attachments/MZ77NASB/fulltext/images/278a62c68763d99e310563204d7a487493163501055ecf5191797ea0f24a3ec4.jpg)

Citing articles: 1 View citing articles ↗

# A Computer Charging Mechanism for Revealing User Preferences within a Large Organization

ROGER ALAN PICK and ANDREW B. WHINSTON

ROGER ALAN PICK is Assistant Professor of Quantitative Analysis and Information Systems in the College of Business Administration at the University of Cincinnati. He holds a B.S. in Mathematics from Oklahoma University and an M.S. in Mathematics from Purdue University. His Ph.D. is in Management Science with a major in Systems Analysis and Computer Science and a minor in Applied Economics from the Krannert Graduate School of Management at Purdue University. His research interests are in the areas of model management systems and the economics of computers and information. He has published in Communications of the ACM, IEEE Transactions on Systems, Man, and Cybernetics, in several conference proceedings, and he has co-authored a book chapter.

ANDREW B. WHINSTON is Professor of Information Systems, Computer Sciences and Economics at the University of Texas at Austin. His primary teaching interest is management information systems. His current research interests include database management and applications of artificial intelligence to economics and management. He has also studied applied economics, regulatory economics, and accounting theory. He has authored or co-authored over 150 papers and 11 books. The most recent books are Manager's Guide to Expert Systems Using GURU, Business Expert Systems, and Micro Database Management—Practical Techniques for Application Development. He has been a consultant to various companies, governmental agencies, and international organizations on data processing questions.

ABSTRACT: The development of effective techniques for allocating computer resources is a major concern in computer center management. Most proposals, while based on concepts originally developed by economists, are based on the assumption that participants provide truthful information. Over the past twenty years, researchers in economics have explored truth-revealing mechanisms. We apply these ideas to charging for computing resources within an organization. The resulting mechanism provides an incentive for users to tell the system administrator their true valuation of a given configuration. Applications of this mechanism to both long-term and short-term situations are outlined. The long-term situation demonstrates how an appropriate computer configuration can be derived from information obtained from its future users. The short-term situation involves setting priorities among jobs.

KEY WORDS AND PHRASES: Transfer pricing, queuing, truthful voting, computer charging, computing equipment selection.

## 1. Introduction

IS IT FEASIBLE IN A DECENTRALIZED ORGANIZATION to obtain funding and simultaneously solicit necessary planning information for a new computing system consistent with the goals of the organization? The answer is yes. Before showing why, consider two situations which might lead one to think that the answer is no.

Suppose the administrator of an organization's computing center foresees a possible need for additional computing power. In order to decide how much the organization should acquire, he must determine the needs of his users. In general, this cannot be inferred from the users' current usage. The inadequacies of the present system may distort and limit usage.

If the administrator simply asks the users how much computing power they need or what various quantities of computing power are worth to them, he will not receive truthful answers from economically rational users. If they overstate their needs in answering this query, the users incur no costs. Indeed, they may perceive a benefit since excess capacity may give them more flexibility in the future. On the other hand, they perceive a cost of understating their needs. An understatement will, if acted upon by the system administrator, increase the danger that they will not receive adequate service in the future. Consequently, we can expect that the administrator will receive reports of exaggerated need. Should he proceed to acquire computing power upon the basis of such reports, he will overinvest, thereby consuming too much of the organization's resources.

The opposite situation arises if the administrator does not have the authority to request users to help fund the additional computing power but needs their financial participation in order to finance it. The administrator is then constrained to offering the users the choice of either contributing to the funding or being excluded from using the additional computing resources. The simplistic solution of requiring all users to pay an equal share of the total computing costs is not acceptable, because a large computing facility is characterized by economies of scale: high fixed costs and relatively low variable costs (Kang and Pick [9]). Suppose at least one user values the added computing power at a level above the marginal cost of being allowed to use the facility and below the shared (average) cost. He will choose not to participate in funding the computer and will then be barred from using it. However, the benefits from using the service exceed the costs of providing it for this additional user. Thus, exclusion of this user is not in the overall interests of the organization. A policy of exclusion would result in underutilization of the computer resources rather than in optimal usage.

It is often suggested that users pay according to how much they value computing power. Those who value it highly would pay a high price and those who benefit less would pay a low price. The difficulty with this approach is that users have an incentive to understate the value of computing power. By claiming that his benefit from computing power is quite small, a user would gain access to the computer but pay very little out of his budget for it. He becomes a “free rider,” carried by those who properly state their values truthfully. Furthermore, since all users will have an incentive to understate their value for computing power, the system administrator will be misinformed about the real situation and will acquire less computing power than the organization needs.

The crucial problem in each case is that users do not have incentives to be truthful about their needs. The administrator must have current information in order to determine how much computing power to acquire and how to fund it. In Section Two, we will propose a pricing mechanism that elicits this information.

A number of researchers have taken an interest in computer pricing as a mechanism to rationalize the use of computer resources. An elementary examination of the problem may be found in Chapter 11 of Sharpe [13]. A survey of various approaches was written by McKell et al. [11]. A broader but earlier survey was written by Cotton [4]. Babad [2] published an article that took into account the many kinds of resources offered by a computer center. He offered an algorithm to find a set of equilibrium prices in several contexts. A problem closely related to the present paper's discussion of user determination of the appropriate level of investment in computing power was examined by Kleijnen [10]. Mendelson [12] looked at queuing effects in a computer center.

As a special but interesting case of the transfer pricing problem (Whinston [16]), the internal computer pricing problem is generally approached using techniques from accounting, economics, and game theory. Using techniques from the economic literature, our approach to the problem proposes a charging mechanism that will allow a computing center to cover its costs, provide service to users according to their needs, and provide an incentive to users to describe their needs accurately.

The latter aspect of the charging mechanism is the contribution of this paper. Possessing correct information allows the computing center to plan and allocate resources in a way that is in the best interests of the organization as a whole.

Our charging mechanism is based upon what Tideman and Tullock $[15]$ call a “demand-revealing process.” This mechanism was independently discovered by Groves $[8]$ and Clarke $[3]$ . Groves was examining incentive structures within an organization. Clarke was looking at the allocation decision for public goods. Tideman and Tullock $[15]$ gave an excellent explanation of the process as well as a discussion of its strengths and weaknesses. An extensive discussion of the issues involved can be found in a special issue of Public Choice edited by Tideman $[14]$ .

In this paper, the demand-revealing process is used to solve two types of a “free-rider problem” that arise in computing center management. Section 2 describes the method. The method is applied in section 3 to the solicitation of information from users concerning their preferences in the context of computer center planning. Section 4 outlines the use of this method in a short-term operational setting. The advantages of the method and the difficulties that are expected to arise in an actual implementation are discussed in section 5.

## 2. An Introduction to the Demand-revealing Process

AS A SINGLE EXAMPLE OF HOW AND WHY the demand-revealing process works, suppose a group has a choice between two options A and B. A set of users will decide which option they collectively prefer. Each user knows in advance that he must pay a special charge (often called a Clarke–Groves tax in the public finance literature), which is computed based upon what he chooses and upon what his fellow users choose. Each user specifies which of the two options he prefers and by how much in monetary terms. The option collectively chosen is the one for which the greatest monetary preference is expressed. (This choice procedure avoids the undesirable implications of the General Possibility Theorem of Arrow [1] by using money as a medium of interpersonal preference comparisons.) We will denote the user by i and his own estimate of his preference (measured in dollars) by $d(i)$ .

(1) Let:

A = index set of users preferring option A

B = index set of users preferring option B

$$
\mathrm{SUMA} = \sum_ {i \in A} d (i) \quad \mathrm{SUMB} = \sum_ {i \in B} d (i)
$$

(2) Results of choice procedure:

$$
\text {   If   } \mathrm{SUMA} > \mathrm{SUMB}, \text {   then   select   } A.
$$

If SUMA $<$ SUMB, then select $B$ .

If SUMA = SUMB, then select A or B randomly.

(3) Compute the charge:

Each user whose stated preference is the option not selected is charged zero.

Each user whose stated preference is the option selected is charged zero if the option selected would have been selected even if he had abstained.

Each user whose stated preference is the option selected is charged at the dollar amount at which the foregone option would have been preferred to the selected option if he had abstained.

One can see, from the above definition, that a user is charged the amount by which his choice (in a sense) hurts the remaining users. A rational user will seek to minimize the sum of the cost of his preferred option losing the election plus the charge. This minimum sum occurs when his stated direction and quantity of preference equals his true direction and quantity of preference. Essentially, an understatement risks the wrong outcome. An overstatement results in either no change in the net benefits or a change in outcome with a tax equaling or exceeding the increased benefit from the outcome.

Table 1 gives an example of three voters choosing between two options. The numbers supplied result in option A being chosen in this election. The magnitudes of the voters' preferences are given along with the appropriate Clark-Groves tax calculated as shown above.

Table 1 An Example of Three Users Choosing among Two Options

<table><tr><td rowspan="2">voter</td><td colspan="2">values of options</td><td rowspan="2">tax</td><td rowspan="2">net benefit</td></tr><tr><td>A</td><td>B</td></tr><tr><td>1</td><td>50</td><td>0</td><td>30</td><td>20</td></tr><tr><td>2</td><td>40</td><td>0</td><td>20</td><td>20</td></tr><tr><td>3</td><td>0</td><td>70</td><td>0</td><td>0</td></tr><tr><td>total</td><td>90</td><td>70</td><td></td><td></td></tr></table>

The following proposition is merely a special case of existing results $[3, 8, 15]$ . It is included for illustrative purposes only.

PROPOSITION: Overstatement of preference for an option is not an optimal strategy.

PROOF: Suppose user i truly prefers option A over option B by \$X. (The opposite situation is covered by symmetry.) Suppose he states that he prefers A over B by \$Y. If B was chosen and user i overstated his preference, Y > X, then he gained nothing over a truthful revelation Y = X. If option A was chosen and user i overstated his preference, Y > X, then the overstatement either did not change the outcome of the election or his poll tax exceeded the net benefit of winning. If option A was chosen and user i understated his preference, Y < X, then he gained nothing. The value of the preferred outcome always exceeds the poll tax. In summary, Y = X is a dominant strategy.

In fact, the result can be stronger than that given in the above proposition. Consider again user i with preference of option A over option B by \$X. He should never state that he prefers B over A, as this risks the costly possibility that he will end up with the wrong choice and also pay the Clarke–Groves tax. Suppose that he states that he prefers A over B by \$Y. Consider now the relation of his vote to the overall group choice. If B was chosen and user i understated his preference, Y < X, then he has relatively lost \$X and might have been able to change the outcome. Thus, understatement is a risky strategy. It might reduce the tax, but it risks an undesirable outcome.

Table 2 includes an example of three users choosing between two options. User 1 states a preference amount X, which may not necessarily be the same as his true preference of A over B, \$50. The table presents the tax and net benefit to user 1 as a function of X. In the case of overstatement, when X > 50, his net benefit will not change from 20. In the case of understatement, when X < 50, there are two situations depending upon the level of understatement. If 30 < X < 50, the net benefit will still be 20. However, if X < 30, net benefits are zero. This discontinuity in the net benefit is the risk taken by an understatement strategy.

In summary, the Clarke–Groves poll tax makes setting the stated value to the true value a good strategy. Overstatement results in a higher tax than the truth which negates any benefits accrued from the falsehood. Understatement poses a risk of losing the election.

Table 2 An Example where User 1 Misrepresents His True Value

<table><tr><td rowspan="2">voter</td><td colspan="2">True Value</td><td colspan="2">Stated Value</td><td rowspan="2">tax</td><td rowspan="2">net benefit</td></tr><tr><td>A</td><td>B</td><td>A</td><td>B</td></tr><tr><td>1</td><td>50</td><td>0</td><td>X</td><td>0</td><td>0, if X &lt; 3030, if X &gt; 30</td><td>0, if X &lt; 3020, if X &gt; 30</td></tr><tr><td>2</td><td>40</td><td>0</td><td>40</td><td>0</td><td>0, if X &lt; 3070 - X, if 30 &lt; X &lt; 700, if 70 &lt; X</td><td>0, if X &lt; 30X - 30, if 30 &lt; X &lt; 7040, if 70 &lt; X</td></tr><tr><td>3</td><td>0</td><td>70</td><td>0</td><td>70</td><td>X + 40, if X &lt; 300, if X &gt; 30</td><td>30 - X, if X &lt; 300, if X &gt; 30</td></tr><tr><td>total</td><td>90</td><td>70</td><td>X + 40</td><td>70</td><td></td><td></td></tr><tr><td colspan="2">option selected</td><td colspan="3">A, if X &gt; 30B, if X &lt; 30</td><td></td><td></td></tr></table>

The next section describes the combination of this choice mechanism with a compatible cost allocation mechanism.

## 3. An Application to Computing Center Planning

## 3.1 A Situation with One Continuous Attribute

Let's assume that we are considering purchasing computing power and it is available in any quantity. For the purposes of this discussion, consider computing power as an abstraction representing in a single dimension some overall quantity of computing investment. The following procedure gives an incentive-compatible mechanism under which economically rational users are induced to reveal their true preference for computing resources. The user is charged for a share of the cost of providing computing power plus a Clarke-Groves charge. This second charge motivates users to reveal the true value of computing power to them. This method is very similar to one outlined in Tideman and Tullock [15].

Let there be n users. Let computing power be scaled so that each unit costs \$1.

Step 1: Each user i is allocated a share $S_{i}$ of the total cost of providing computing power, $S_{i} \geq 0$ , $\sum_{i} S_{i} = 1$ . These may be assigned arbitrarily or based upon any a priori

notion of a fair allocation of cost. These shares are assigned in order to ensure that the full cost of the level of computing power selected is covered by the users. These shares may not be allocated based upon previously revealed preferences, since this would introduce a new incentive for misrepresentation.

Step 2: Each user i is required to report the curve, $MV_{i}$ , of the marginal value to him of computing power. These curves, one for each $i = 1, 2, \ldots, n$ , are summed vertically (see Figure 1) to give the curve $\sum_{i} MV_{t}$ . The intersection of this curve with the

![](/api/attachments/MZ77NASB/fulltext/images/749dd429f75f19e4ebffb96dc756223eef627bcf1a1cc5bb4962d7fbc2e4e07f.jpg)  
Figure 1. Continuous Case where $X' < X$

marginal cost (MC) curve gives the amount of computing power that is needed for the organization, denoted by X.

Step 3: The Clarke–Groves charge is now calculated. This charge is based upon the amount by which user i's marginal value curve $MV_{i}$ has changed the amount of computing power selected. This charge is in addition to the share of total cost that each user must pay. A horizontal line is drawn at $1 - S_{i}$ . This line represents marginal costs to all users except i. The curve $\sum_{j \neq i} MV_{j}$ is drawn. Its intersection with MC (at $1 - S_{i}$ )

projects to $X'$ on the horizontal axis. The intersection of these two curves gives the amount of computing power that the organization would acquire if user i did not participate. This might be more or less than the original amount, depending upon cost shares and the shapes of the MV curves. The Clarke–Groves charge is given by the difference between

$$
\sum_ {j \neq i} M V _ {j} \text {   and   } \sum_ {j \neq i} M C _ {j}, \text {   from   } X \text {   to   } X ^ {\prime},
$$

from the original amount to acquire to the amount to be acquired if user i does not participate. This region is shaded in Figure 1.

Now that we know how the Clarke–Groves charge is calculated in this case, we need to see why it induces truthful revelation of marginal valuation. The point $X'$ denotes the amount of computing power that would be supplied if user i reports an $MV_{i}$ equal to his cost share, $S_{i}$ . This is also the amount that would be preferred by all users excluding i. User i's reported $MV_{i}$ will change the amount of computing power allocated to the point X from $X'$ . The loss to the other users due to user i's preference is given by the shaded area. This area is the amount of the Clarke–Groves charge. Since the system administrator is charging user i for the loss he causes other users, he is motivated not to attempt to change the quantity of computing power from the point $X'$ unless by doing so his gain (assumed to correspond to overall organizational gain) exceeds the loss suffered by all other users. In either case, his greatest benefit is realized by reporting $MV_{i}$ truthfully.

## 3.2 A Situation with Several Discrete Attributes

The case just considered is not realistic. It assumed that the alternative available to the system administrator could be described by a single quantity and that this quantity is available in a continuum of values. The more realistic case involves a variety of quantities: memory, speed, word length, instruction set, channels, secondary storage, and many more. Also, it is more realistic if only a few values are available for each type of attribute. For example, memory may only come in megabytes and one cannot reasonably purchase one half of a tape drive.

To handle this, we will model the situation of a system administrator attempting to select a particular computing system from a finite set of possibilities. Under the assumption, heretofore implicit in this paper, that users can evaluate the value of a computing system, we find that the many attributes pose no difficulty. The issue here is the reporting of preference by the users.

Assume that there are a finite number m of systems under consideration. Each system j has an acquisition cost $C_{j}, j = 1, 2, \ldots, m$ . Each user i, i = 1, 2, $\ldots$ , n, has a preallocated cost share $S_{i}$ of the chosen system. The system administrator knows the cost $C_{j}$ of each system under consideration. He needs to know the benefit each system may offer to the organization as a whole. He can acquire this information by asking each user i for the value to him of system j, $V_{ij}$ . The administrator's problem is then to select the system j for which the net benefit $\sum_{i} V_{ij} - C_{j}$ is maximized. (If the maximum is

nonpositive, no system is acquired.) The system is financed by requiring each user to pay a share $S_{i}$ of the costs. Each user will report his net benefit, $V_{ij} - S_{i} C_{j}$ . This situation is now handled as a generalization of the two-option vote described earlier. This is really a vote by the users among a finite set of options. In order to prevent misrepresentation, the Clarke–Groves charge must be assessed. To calculate the tax on user i, we compute the sum of all the other users' net values, $\sum_{k\neq i}(V_{kj}-S_{k}C_{j})$ for all the

Table 3 Three Users Evaluating Three Systems

<table><tr><td rowspan="2">user</td><td colspan="5">gross value of systems</td></tr><tr><td>i</td><td>b</td><td>m</td><td></td><td></td></tr><tr><td>1</td><td>70</td><td>30</td><td>40</td><td></td><td></td></tr><tr><td>2</td><td>40</td><td>60</td><td>40</td><td></td><td></td></tr><tr><td>3</td><td>20</td><td>75</td><td>60</td><td></td><td></td></tr><tr><td>system cost</td><td>30</td><td>60</td><td>90</td><td></td><td></td></tr><tr><td rowspan="2"></td><td colspan="3">net value of systems</td><td rowspan="2">tax</td><td rowspan="2">benefit from voting</td></tr><tr><td>i</td><td>b</td><td>m</td></tr><tr><td>1</td><td>60</td><td>10</td><td>10</td><td>0</td><td>0</td></tr><tr><td>2</td><td>30</td><td>40</td><td>10</td><td>5</td><td>5</td></tr><tr><td>3</td><td>10</td><td>55</td><td>30</td><td>40</td><td>5</td></tr><tr><td>total</td><td>100</td><td>105</td><td>50</td><td>choose b</td><td></td></tr><tr><td></td><td colspan="5">totals without vote by one user</td></tr><tr><td>without 1</td><td>40</td><td>95</td><td>40</td><td>choose b</td><td></td></tr><tr><td>without 2</td><td>70</td><td>65</td><td>40</td><td>choose i</td><td></td></tr><tr><td>without 3</td><td>90</td><td>50</td><td>20</td><td>choose i</td><td></td></tr></table>

systems being considered. If the system with the highest net value is still chosen, then the charge is zero. If there is a change in the system selected (i.e., if user i's preferences have changed the decision made by the overall organization), then the charge is equal to the minimal preference he could have expressed to change the decision. The charge is also equal to the net cost of user i's preferences to other users in terms of the system selection.

To illustrate selection among discrete computing systems, we give in Table 3 an example involving three users, 1, 2, and 3, who are evaluating three systems, i, b, and m. We will assume that the cost share of each user is 1/3.

## 4. Priority Queuing During the Short Run

CONSIDER THE PRIORITY PROBLEM FACED BY THE ADMINISTRATOR of a computing system. In determining the order in which jobs are to be run, the administrator faces several conflicting objectives. Three mentioned by Greenberger [7] are:

1. Reduce average response time and number of jobs waiting.

2. Acknowledge customer importance and urgency of request.

3. Serve in fair order and limit length of wait.

Each of these objectives may be served individually by choosing an appropriate queuing discipline:

Table 4 A Static Queue Example

<table><tr><td>user</td><td>cost/unit time delayed (c)</td><td>time/job (t)</td></tr><tr><td>1</td><td>1</td><td>6</td></tr><tr><td>2</td><td>2</td><td>4</td></tr><tr><td>3</td><td>3</td><td>5</td></tr></table>

Table 5 Values of Orderings to User

<table><tr><td rowspan="2">user</td><td colspan="6">order</td></tr><tr><td>1,2,3</td><td>1,3,2</td><td>3,1,2</td><td>2,1,3</td><td>2,3,1</td><td>3,2,1</td></tr><tr><td>1</td><td>9</td><td>9</td><td>4</td><td>5</td><td>0</td><td>0</td></tr><tr><td>2</td><td>10</td><td>0</td><td>0</td><td>22</td><td>22</td><td>12</td></tr><tr><td>3</td><td>0</td><td>12</td><td>30</td><td>0</td><td>18</td><td>30</td></tr><tr><td>total</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>value</td><td>19</td><td>21</td><td>34</td><td>27</td><td>40</td><td>42</td></tr></table>

Table 6 Total Values with Each User Abstaining

<table><tr><td>user abstaining</td><td>order 1,2,3</td><td>1,3,2</td><td>3,1,2</td><td>2,1,3</td><td>2,3,1</td><td>3,2,1</td><td>C-G charge</td></tr><tr><td>1</td><td>10</td><td>12</td><td>30</td><td>22</td><td>40</td><td>42</td><td>0</td></tr><tr><td>2</td><td>9</td><td>21</td><td>34</td><td>5</td><td>18</td><td>30</td><td>4</td></tr><tr><td>3</td><td>19</td><td>9</td><td>4</td><td>27</td><td>22</td><td>12</td><td>15</td></tr></table>

Table 7 Apparent Values of Orderings to User

<table><tr><td>uservote</td><td>1,2,3</td><td>1,3,2</td><td>3,1,2</td><td>2,1,3</td><td>2,3,1</td><td>3,2,1</td><td></td></tr><tr><td>1</td><td>900</td><td>900</td><td>400</td><td>500</td><td>0</td><td>0</td><td></td></tr><tr><td>2</td><td>10</td><td>0</td><td>0</td><td>22</td><td>22</td><td>12</td><td></td></tr><tr><td>3</td><td>0</td><td>12</td><td>30</td><td>0</td><td>18</td><td>30</td><td></td></tr><tr><td>total</td><td>910</td><td>912</td><td>430</td><td>522</td><td>40</td><td>42</td><td></td></tr><tr><td>abstaining</td><td>1,2,3</td><td>1,3,2</td><td>3,1,2</td><td>2,1,3</td><td>2,3,1</td><td>3,2,1</td><td>charge</td></tr><tr><td>1</td><td>10</td><td>12</td><td>30</td><td>22</td><td>40</td><td>42</td><td>30</td></tr><tr><td>2</td><td>900</td><td>912</td><td>430</td><td>500</td><td>18</td><td>30</td><td>0</td></tr><tr><td>3</td><td>910</td><td>900</td><td>400</td><td>522</td><td>22</td><td>12</td><td>10</td></tr></table>

1. Average response time is best reduced by running the job with the shortest service time next.

2. Customer importance can be acknowledged by having several different priority queues.

3. Limiting length of wait can be accomplished by a first come/first serve rule.

Each of these serves its purpose but will discriminate against certain classes of users if the computing center serves a diverse range of users. For instance, users having long jobs will have excessive waits under a shortest service time next rule, while users with short jobs suffer under a first come/first served rule when they have to wait behind a huge job.

As a good compromise, consider the cost of delay as an inverse measure of performance. Apply this measure to the context of a simple computing center with a single queue of jobs awaiting execution. Assume that the computer can only execute one job at a time. Multiprogramming, multiprocessing, and preemption of jobs already running will not be considered. We will also assume that the cost of delay to user i as he waits for his job is linear with time. This assumption implies a constant cost rate.

If we denote the cost rate for user i as $c_{i}$ and the time estimate for his job as $t_{i}$ , then serving the job with the highest ratio of $c_{i}/t_{i}$ next will minimize the total delay cost. A proof of this may be found on pages 83–85 of Cox and Smith [5].

If we implement the scheme of running the job with the highest ratio $c_{i}/t_{i}$ next, then the user has an incentive to misrepresent the needed information. He is encouraged to state $c = \infty$ and t = 0. The administrator wishes to change these incentives so as to encourage users to represent properly their delay costs and running time.

To encourage users to specify an accurate estimate of their running time, a mechanism widely used by many computing systems is endorsed: a job will be kicked off the system if it uses more time than estimated. This will encourage a type of misrepresentation in the form of unbundling a large job into many smaller jobs, but this is probably not much of a practical difficulty. To encourage users to specify their true delay cost rates, we will use a demand-revealing process. There will be a charge, the Clarke–Groves charge, which is levied in addition to any charges for computing time and resources and in addition to any delay costs suffered internally by the user. As a concrete example, suppose there is a static queue of three users with delay cost rates and execution times as given in Table 4.

In that table, the ratios of c/t for users 1, 2, 3 are 1/6, 1/2, and 3/5 respectively. So, the optimal ordering of the users to minimize total delay costs would be to run 3, then 2, and then 1. Table 5 gives each user's valuation of each of the six possible orderings. Notice that the voting mechanism gives the most value to 3, 2, 1—the same result as the c/t rule.

To determine Clarke–Groves charges, we look at the total values as if each user were to abstain from voting (state c = 0) as shown in Table 6. The Clarke–Groves charges are computed as follows. Since user 1 did not change the outcome, his Clarke-Groves charge is zero. Had user 2 abstained, option 3, 1, 2 would have been the choice. It would have been preferred to 3, 2, 1 (the chosen option) by \$4. Hence, user 2 is taxed

4. Had user 3 abstained, 2, 1, 3 would have been preferred to 3, 2, 1 by \$15, which is his Clarke-Groves tax.

The Clarke–Groves charge turns out to be exactly equal to the delay cost imposed by each user upon the others. For instance, user 3 delays user 1 and user 2 by five time units, for a total delay cost to user 1 and user 2 of \$15. User 2 delays user 1 by 4 units for a delay cost of \$4. User 1, who delays no one, paid no Clarke–Groves charges and caused no delay costs.

The actual implementation of this would involve using the highest c/t rule to sort users in decreasing c/t order and computing Clarke–Groves charges by charging delay costs imposed on other users, using the formula

$$
\text { Clarke - - Groves   Charge   on   User } M = t _ {M} \sum_ {i = M + 1} ^ {N} c _ {i}
$$

Since the rational user will seek to minimize delay costs plus Clarke–Groves charges, he will be driven to a position of representing his cost rates accurately. A truthful response will cause each user to affect the outcome exactly properly. A nontruthful response cannot benefit the user. In fact, it carries a risk of making him worse off than he would have been with the truth. If he understates his value, he may pass up the opportunity to obtain the result he desires at an attractive price. If he overstates his value, he may wind up paying more than it is worth to him to have his choice.

As an example, consider the above example when user 1 misrepresents his cost rate to be 100 in order to be run first. Table 7 gives the resulting apparent values and charges.

Hence, by his misrepresentation, user 1 changes the outcome and gains by having 0 delay, which is worth \$9 to him. But his Clarke–Groves charge is \$30. So, he has a net loss.

The extension of the Clarke–Groves charging mechanism from a static queue to a dynamic one can be accomplished using expectations. Although this is not a perfect method, the alternatives present difficulties. Recomputing all the taxes each time a job enters the system is not feasible. Since the Clarke–Groves charge equals delay costs imposed upon other users, we can use delay cost as our tax. It is also difficult to compute the actual costs since the administrator would have to add up the costs for all users from the time a job runs until the next slack period. Instead, one can charge the expected delay costs imposed by the user upon other users. The details have been worked out in another context by Dolan $[6]$ .

## 5. Advantages, Disadvantages, Strengths, and Weaknesses

WE HAVE DESCRIBED A TECHNIQUE THAT DISCOURAGES USERS from misrepresenting their needs. The technique, called the demand-revealing process, uses economic incentives that are structured in such a way that a person will not profit from misrepresentation and misrepresentation creates a risk of being worse off. The economic incentives take the form of a charge, called the Clarke–Groves charge, which is computed for each user based upon the statements provided by him and all other users.

At first glance, the demand-revealing process seems so powerful that Tideman and Tullock [15] felt it necessary to warn their readers that the process will not cure cancer nor stop the tides. It has the advantage of providing a computing system administrator with a method of finding out the needs of his users while providing a way of funding his systems. This kind of problem was long considered insoluble. If we can practically implement a demand-revealing mechanism based upon the Clarke-Groves charge, we have implemented a very useful tool. Of course, implementation faces a number of practical and theoretical obstacles.

One major problem with this approach is that the administrator's problem has become the user's problem. The user must be able to evaluate systems and his own needs and rank alternatives cardinally. Although he presumably does not lie to himself, the necessary evaluations would require much expertise. It is not realistic to consider such expertise as being distributed throughout the organization. Related to this problem of expertise is the fact that the Clarke-Groves charge is complex and difficult to understand. If the user does not understand that this charge really makes telling the truth his own best interest, then all this is for nothing. His misunderstanding of the charges would cause him to behave irrationally, contrary to his own interests and the interests of the entire organization. We feel that both of these weaknesses can be compensated for by training.

In contrast to some previously published criteria on what makes for a good charging mechanism $[11, 13]$ , the charge depends upon actions by other users; it is dependent upon factors outside the control of the individual being charged. The complexity of the charge is also contrary to most descriptions of good mechanisms. The response to this criticism is that the lists of criteria cited above are internally inconsistent. No charging mechanism has been invented that meets all the criteria and none ever will. The demand-revealing process meets some of them.

The Clarke–Groves charge may produce incentive distortions if the collected money is used for any purpose of which the users approve or disapprove. Tideman and Tullock $[15]$ propose that the charge be wasted. The problem with this is that we are then forced into a solution method that generates economically inefficient solutions. One must decide whether the optimal receipt of information makes up for the loss due to the charges. In practice, allocating the charge to a general overhead account may be close enough to “waste” to prevent problems.

Another problem with this mechanism is that it can be subverted by a coalition. The process obtains optimal incentives only if the users cannot plan their votes together. Coalitions will not have time to form under the short-run case. It can be a problem in the long-run resource allocation application. Anyone who intends to apply this methodology must take steps to prevent users from discussing their preferences and their voting strategy.

Finally, the cost shares should be initially set so that they are exceeded by the marginal valuation of each user in order to prevent users from choosing not to participate. Since setting shares by reported valuation would distort incentives, a different method must be used. One way to do this is to hire a consultant to allocate shares. The consultant would be given a nearly full description of the user and the user's use of the computer. The only information that must not be provided to the consultant is past reported valuations. The consultant can be motivated by tying his compensation to the closeness with which his a priori cost shares match the marginal valuations.

## ACKNOWLEDGEMENT

We wish to thank the anonymous referees, who provided comments that improved the technical quality and readability of this paper.

## REFERENCES

1. Arrow, K. J. Social Choice and Individual Values, 2nd edition. New Haven: Yale University Press, 1963.

2. Babad, Y. M. Pricing model for a computer center. Operations Research, 29,1, (January–February, 1981), 75–94.

3. Clarke, E. H. Multipart pricing of public goods. Public Choice, 11 (Fall, 1971), 18–33.

4. Cotton, I. W. Microeconomics and the market for computer services. Computing Surveys, 7, 2 (June, 1975), 95–111.

5. Cox, D. R., and Smith, W. L. Queues. New York: John Wiley and Sons, 1961.

6. Dolan, R. J. Incentive mechanisms for priority queuing problems. Bell Journal of Economics, 9, 2 (Autumn, 1978), 421–436.

7. Greenberger, M. The priority problem and computer time sharing. Management Science, 12, 11 (July, 1966), 838–906.

8. Groves, T. Incentives in teams. Econometrica, 41, 4 (July, 1973), 617–631.
9. Kang, Y. M., and Pick, R. A. An analysis of computer performance with resp

scale economics and technological changes. Submitted to MIS Quarterly, 1988.

10. Kleijnen, J. P. C., and Van Reeken, A. J. Principles of computer charging in a univer-

sity-type organization. Communications of the ACM, 26, 11 (November, 1983), 926–932.

11. McKell, L. J.; Hansen, J. V.; and Heitger, L. E. Charging for computing resources. Computing Surveys, 11, 2 (June, 1979), 105–120.

12. Mendelson, H. Pricing computer services: queueing effects. Communications of the ACM, 28, 3 (March, 1985), 312–321.

13. Sharpe, W. F. The Economics of Computers. New York: Columbia University Press, 1969.

14. Tideman, T. N. (ed.). Public Choice, 29, 2 (special supplement to Spring 1977), special issue on demand-revealing process.

15. Tideman, T. N., and Tullock, G. A new and superior process for making social choices. Journal of Political Economy, 84, 6 (December, 1976), 1145–1159.

16. Whinston, A. Price guides in decentralized organizations. In W. W. Cooper, H. J.

Leavitt, and N. W. Shelly II (eds.), New Perspectives in Organization Research. New York: John Wiley and Sons, 1964, 405–448.
