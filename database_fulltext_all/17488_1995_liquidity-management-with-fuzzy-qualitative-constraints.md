---
otero_id: 17488
otero_key: "3EFK5AHQ"
title: "Liquidity management with fuzzy qualitative constraints"
authors: "Francesco Gardin; Richard Power; Enrico Martinelli"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00033-o"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Liquidity management with fuzzy qualitative constraints $^{*}$

Francesco Gardin ${}^{a,*}$ , Richard Power ${}^{a}$ , Enrico Martinelli ${}^{b}$

$^{a}$ Artificial Intelligence Software spa, Via Rombon 11, 20134 Milan, Italy

$^{b}$ Department of Computer Science, University of Milan, Via Comelico, 39 20135 Milan, Italy

## Abstract

The treasurer of a bank must balance liquidity flows every day in an environment in which some future interest rates and transactions are known precisely, but some are uncertain. Decision support systems based on traditional mathematical programming approach find the optimal plan with respect to precise quantitative constraints provided by the user; we here suggest a procedure by which such systems can utilize probabilistic and Fuzzy qualitative constraints (e.g. “the treasury might have to cover a small deficit next Friday”). Each qualitative judgement is formalized by a discrete possibility distribution, which is converted to a discrete probability distribution; in this form the problem can be solved by the simple recourse method. Unexpected surpluses/deficits due to an uncertain future balance are evaluated in the objective function: by varying the evaluation coefficients along a scale from pessimistic to optimistic, we can obtain several solutions each adapted to a different risk policy.

Keywords: Fuzzy; Constraints; Logic programming; Stochastic programming; Simple recourse; Qualitative values; Possibility; Probabilistic judgment; Treasury; Liquidity; Risk management; Uncertainty

## 1. Introduction

On any working day, the commercial activities of a bank generate expenses and revenues which sum either to a net deficit or a net surplus. The treasurer seeks to cover the deficit, or utilize the surplus, in such a way that the bank profits by exploiting variations in interest rates. In Italy, liquidity flows are balanced mainly by short-term borrowing and lending on the interbank money market. The environment in which the treasurer operates is uncertain: some future interest rates are not quoted on the electronic market, and the balances for forthcoming days cannot be predicted precisely.

When we began in 1989 to develop a planning system to support liquidity management, our first impression was that the problem should be suited to an expert system approach, using heuristic rules to interpret qualitative judgements about future rates and balances. After some initial experiments we abandoned this view, for two reasons. First, since the electronic market for interbank operations had just been introduced, Italian treasurers had not yet accumulated sufficient experience in the new environment to provide a reliable source of expertise. Secondly, the environment was only partially uncertain; for most parameters reliable quantitative data were available, so that the problem could be solved by mathematical optimization provided that precise estimates were provided for the missing values. Following the latter approach, we developed the SEPT system [7], currently installed in many Italian banks, which finds a plan for the next two weeks which is optimal with respect to a scenario provided by the user.

The main weakness of SEPT is that the user must give precise estimates, such as “the overnight lending rate next Friday will be 11.5%”; the system cannot utilize estimates that are imprecise (“the lending rate will be between 10% and 13%”) or vague (“the lending rate might be high”). Our next aim, which is addressed in this paper, has been to develop a decision support system for liquidity management that can accept statistical and qualitative descriptions of uncertain parameters, and so produce a range of possible plans depending on the risk policy of the user. Essentially, we propose to extend a standard model for stochastic optimization so that it can include fuzzy as well as probabilistic constraints.

In all the models that we shall consider, the purpose is to optimize an objective function while respecting a set of constraints. If the cost function and the constraints are linear, the problem is usually defined as follows:

Minimize $Z = cx$ subject to $x \geq 0$ and $Ax = b$

Here x is a vector of n real numbers representing the solution; c is a vector associating a cost with each term in x; and Ax = b represents a set of m constraints of the form:

$$
\begin{array}{l} \mathrm {A_ {11} x_ {1} + A_ {12} x_ {2} + \ldots+ A_ {1n} x_ {n} = b_ {1}} \\ \mathrm {A_ {21} x_ {1} + A_ {22} x_ {2} + \ldots+ A_ {2n} x_ {n} = b_ {2}} \\ \vdots \\ \mathrm {A_ {m1} x_ {1} + A_ {m2} x_ {2} + \ldots+ A_ {mn} x_ {n} = b_ {m}} \end{array}
$$

If the parameters A, b, c, are known, the optimal solution can be found by familiar methods such as the simplex algorithm [5]. In practice however, as we have seen, the values of some parameters are often uncertain. To deal with such cases we need to find an appropriate way of representing uncertain values. When statistical information is available, they can be represented by probability distributions; for instance, an uncertain estimate of 10 could be replaced by a distribution [8, 0.2; 10, 0.5; 12, 0.3], meaning that the discrete values 8, 10, and 12 have probability values of 0.2, 0.5, and 0.3 respectively. If some values in A, b and c are replaced by discrete probability distributions the problem can be solved by a method known as the simple recourse model [23].

However, there is often no statistical basis for representing uncertain parameters by probability distributions; a statement such as “interest rates might be high in the middle of next week” is qualitative and possibilistic in nature rather than quantitative and probabilistic. Zadeh [22] proposes that information of this sort can be represented better with the apparatus of fuzzy set theory: a qualitative estimate can be formalized as a discrete fuzzy set rather than as a probability distribution.

Note that the concept of a fuzzy set is not merely a disguised form of subjective probability, although both the theory of Fuzzy sets and the theory of probability were developed to attain realistic solutions to problems in decision analysis under uncertainty. In essence, Fuzzy set theory is aimed at dealing with sources of uncertainty or imprecision that are inherently vague and nonstatistical in nature.

Thus, probability theory does not provide an adequate tool for a direct representation of problems in which the available information, like the proposition stated above, is incomplete, imprecise or unreliable. Attempts to utilise probability theory in qualitative analysis have been made [13]. However, as argued above, this does not fulfil the basic motivation of qualitative modelling: that of capturing human vagueness.

This paper suggests a procedure for solving linear optimization problems in which some parameters are represented by discrete fuzzy sets. Our procedure has three stages. First, the problem is defined using appropriate representations for each parameter, so that some values are constants, some are discrete probability distributions, and some are discrete fuzzy sets. Secondly, the fuzzy sets are converted to probability distributions using Dubois and Prade's formula [6] to obtain an homogeneous representation of the uncertain parameters introduced. Finally, the resulting stochastic optimisation problem is solved by the simple recourse method. To illustrate this procedure we describe a simplified version of a planning system for managing the liquidity of a bank, in an environment where interest rates and daily liquidity balances are partly uncertain.

Our proposal is an example of a hybrid method which represents a compromise between the qualitative and quantitative approaches. In research on qualitative reasoning, a major problem has been that for complex models no definite solution results; for this reason there have been attempts to construct hybrid models which include some quantitative information $[3,9,21]$ or which take account of order of magnitude $[8]$ .

Our approach instead is to adopt the standard quantitative methods as our point of departure, and to modify them so that they can utilize qualitative or statistical estimates. This kind of hybrid model seems particularly well suited to financial applications, such as portfolio management $[10]$ and asset and liability management $[4]$ , in which most of the problem data are available in precise quantitative form.

## 2. Liquidity management in Italian banks

Until a few years ago, liquidity management in Italian banks was not seen as a complex task requiring computer support. This situation changed abruptly in 1990 when the Bank of Italy introduced an electronic market for domestic interbank operations in lira [16]. Through this market, commercial banks can offer to buy or sell money for specified durations and interest rates. In consequence treasurers must now interpret hundreds of offers, fluctuating during the day, in order to plan their cash flows and to exploit opportunities for arbitrage.

A transaction proposed on the interbank money market is defined by the following parameters:

\- Name of proposing bank

\- Type of operation (bid/offer)

\- Initial date

\- Final date

\- Amount

\- Interest rate

If a bank proposes a borrowing operation it quotes a bid rate (or “take rate”); for a lending operation it quotes an offer rate (or “ask rate” or “lend rate”). Since in general sellers offer a higher price than buyers, the offer rates for a given operation exceed the bid rates by a margin known as the spread. For instance, the average bid rate might be 8.5% and the average offer rate 9.5%, giving a spread of 1.0%.

Table 1 shows the names of interbank operations for the next 10 working days. We adopt the convention that the row indicates the day when the money departs, while the column indicates the day when it arrives. Thus the cell $(1,2)$ represents a lending operation since the money leaves

Interbank operations

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>1</td><td>-</td><td>ON</td><td>DV2</td><td>DV3</td><td>DV4</td><td>DV5</td><td>DV6</td><td>DV7</td><td>DV8</td><td>DV9</td></tr><tr><td>2</td><td>ON</td><td>-</td><td>TN</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td></tr><tr><td>3</td><td>DV2</td><td>TN</td><td>-</td><td>SN</td><td>DF</td><td>DF</td><td>DF</td><td>DT1S</td><td>DF</td><td>DF</td></tr><tr><td>4</td><td>DV3</td><td>DF</td><td>SN</td><td>-</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td></tr><tr><td>5</td><td>DV4</td><td>DF</td><td>DF</td><td>DF</td><td>-</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td></tr><tr><td>6</td><td>DV5</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td><td>-</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td></tr><tr><td>7</td><td>DV6</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td><td>-</td><td>DF</td><td>DF</td><td>DF</td></tr><tr><td>8</td><td>DV7</td><td>DF</td><td>DT1S</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td><td>-</td><td>DF</td><td>DF</td></tr><tr><td>9</td><td>DV8</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td><td>-</td><td>DF</td></tr><tr><td>10</td><td>DV9</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td><td>DF</td><td>-</td></tr></table>

Table 4

on day 1 and returns (with interest) on day 2; instead (2,1) represents a borrowing operation since the money arrives today and leaves (with interest) tomorrow.

On the interbank market, all operations have a name which depends on their initial and final dates. By far the most popular operation is the “Overnight” (ON), which begins on the current day and ends on the following day. The deferred operations “Tomorrow Next” (TN) and “Spot Next” (SN) are also heavily used. Operations from the current day to days 3, 4, 5,...(DV) are less popular, and the remaining “Deferred” operations (DF) are scarcely used at all.

All commercial banks are obliged to maintain at the central bank an account known as the Riserva Obbligatoria (ROB). The amount in the reserve account depends on the volume of work of the bank, and may vary slightly from month to month. During monthly periods assessed from the 15th of each month to the 14th of the next, each bank may make some withdrawals from this account provided that a specified limit is not exceeded and provided that total amount withdrawn (measured in lire-days) is balanced by corresponding deposits. A practical system for liquidity management should obviously include operations with the central bank, but to simplify the presentation we will assume in this paper that only interbank operations are employed.

## 3. Liquidity management with precise quantitative data

We describe in this section the method used in SEPT, which finds the optimal plan with respect to a precise quantitative scenario. In later sections we show how this method can be extended to cope with qualitative estimates of interest rates and balances. For simplicity we will focus throughout on a trivial example with a planning period of just three days.

Table 2  
Interest rates

<table><tr><td></td><td>Day 1</td><td>Day 2</td><td>Day 3</td></tr><tr><td>Day 1</td><td>-</td><td>7.0</td><td>10.0</td></tr><tr><td>Day 2</td><td>8.0</td><td>-</td><td>9.0</td></tr><tr><td>Day 3</td><td>11.0</td><td>10.0</td><td>-</td></tr></table>

Table 3
Profit rates

<table><tr><td></td><td>Day 1</td><td>Day 2</td><td>Day 3</td></tr><tr><td>Day 1</td><td>-</td><td>7.0</td><td>20.0</td></tr><tr><td>Day 2</td><td>-8.0</td><td>-</td><td>9.0</td></tr><tr><td>Day 3</td><td>-22.0</td><td>-10.0</td><td>-</td></tr></table>

The profit (or cost) associated with each operation depends on the interest rates, which can be specified by a matrix (Table 2) with the same conventions as the operation matrix in Table 1.

Note that all borrowing rates here exceed lending rates by a “spread” of 1%. The unit profit for an operation is given by the formula

## Profit = Interest \* Duration / 36500

where the interest rate is measured in percentage points and the duration in days. Since we are interested only in relative profit (Table 3), it is convenient to ignore the constant denominator 36500. Obviously profit is positive for lending operations and negative for borrowing.

The daily balances (Table 4) are represented by a vector of amounts, measured here in billions of lire.

In this example, a surplus of 10 billion lire on the current day is utilized to cover a deficit of 10 billion lire on day 2. The most direct way of doing this would be to carry out the lending operation (1, 2). This operation would imply a new expense of 10 on the current day, setting the balance to zero, and a new revenue of 10 on day 2 when this sum is repaid, setting the day 2 balance to zero plus a small amount of interest. The crucial constraint is that the closing balance for each day should be zero, so that all surpluses are utilized and all deficits are covered. Such a solution can be represented by a matrix of amounts in which

<table><tr><td></td><td>Day 1</td><td>Day 2</td><td>Day 3</td></tr><tr><td>Balance</td><td>10</td><td>-10</td><td>0</td></tr></table>

Table 5 Solution

<table><tr><td></td><td>Day 1</td><td>Day 2</td><td>Day 3</td></tr><tr><td>Day 1</td><td>-</td><td>10</td><td>0</td></tr><tr><td>Day 2</td><td>0</td><td>-</td><td>0</td></tr><tr><td>Day 3</td><td>0</td><td>0</td><td>-</td></tr></table>

Table 6  
Daily cash flows

<table><tr><td>D</td><td>IB</td><td>FB</td><td>Bo</td><td>Le</td><td>Rc</td><td>Rp</td></tr><tr><td>1</td><td>10</td><td>0</td><td>0</td><td>10</td><td>0</td><td>0</td></tr><tr><td>2</td><td>-10</td><td>0</td><td>0</td><td>0</td><td>10</td><td>0</td></tr><tr><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

D Day
IB Initial Balance
FB Final Balance
Bo Borrowing
Rp Repayments
Le Lending
Rc Receipts

values of zero mean that the operation is not performed (Table 5).

The account table (Table 6) describes the cash flows during the three days and shows that the final balance at the end of each day is zero. The table excludes interest payments, which are too small to have any influence on planning. On each day, the final balance is given by the formula:

$$
\mathrm{FB} = \mathrm{IB} + \mathrm{Bo} + \mathrm{Rc} - \mathrm{Le} - \mathrm{Rp}
$$

The danger in using a deterministic system like SEPT is that the problem data are assumed to be certain, and hence no allowance is made for risk. To use a familiar analogy, the optimal route for walking from one place to another might pass near the edge of a cliff; it would be most unwise to follow this route if the location of the cliff was uncertain. Observing the behaviour of SEPT we have noticed that it sometimes plans a huge flow towards days on which interest rates are expected to be high, in order to accumulate a surplus that can be lent at profitable rates. By putting all its eggs in one basket in this way, the system is vulnerable to a large loss if for some reason the interest rates on this day sharply decline.

## 4. Conversion of fuzzy sets to probability distributions

How can a system like SEPT be extended in order to accommodate probabilistic and qualitative estimates of uncertain parameters? Let us suppose that the interest rates for the operations (2, 3) and (3, 2) are not yet quoted on the electronic market, and that the balances for days 2 and 3 are also uncertain. The treasurer judges that the interest rate for the lending operation (2, 3) will be “quite high”; the rate for the corresponding borrowing operation (3, 2) can be derived by adding a typical spread of 1%. Concerning the balances, the treasurer foresees that on day 2 “there might be a small deficit”. Moreover, from statistical information he can postulate a set of daily balances for day 3 and to assign them a probability distribution, here labelled “about zero”. Thus the problem data of tables 2 and 4 are modified as follows in Table 7.

To make further progress, we need to find an appropriate way of formalizing the qualitative (nonstatistical) concepts like “high interest rate” and “small deficit”. Zadeh (1978) has argued that much of the information on which human decisions are based is possibilistic rather than probabilistic in nature. Intuitively, possibility is associated with feasibility and ease of attainment, while probability is associated with frequency and degree of belief. Sources of uncertainty that are inherently vague and non-statistical are more appropriately represented by possibility distributions, which can be defined in terms of fuzzy sets.

Suppose that a parameter X refers to a future interest rate which is at present uncertain, and that F is a vague property of interest rates, such as the property of being high. If U is the set of interest rates, we can formalize F as a fuzzy subset of U by defining a membership function $\mu_{F}$ which specifies, for each member of U, the degree to which it belongs to F. Given the assertion “X is F” (i.e. “the interest rate will be high”), the function $\mu_{F}$ determines a possibility distribution $\pi$ for X, so that for any member u of U, the possibility that X equals u is given by $\pi(\mathbf{u})$ . Usually the maximum value of $\mu_{\mathrm{F}}(\mathbf{u})$ will be 1, meaning that some interest rates are definitely high; in this case the possibility distribution $\pi$ coincides with $\mu_{F}$ . The representation of uncertain quantities by possibility distributions has been investigated by Leitch and Shen [11] and by Vescovi and Travé-Massuyès [18], who propose a method for defining what they call “qualitative fuzzy values”.

Table 7  
Interest rates and balances with uncertain values

<table><tr><td></td><td>Day 1</td><td>Day 2</td><td>Day 3</td></tr><tr><td>Day 1</td><td>-</td><td>7</td><td>10</td></tr><tr><td>Day 2</td><td>8</td><td>-</td><td>quite high</td></tr><tr><td>Day 3</td><td>11</td><td>quite high</td><td>-</td></tr><tr><td>Balance</td><td>10</td><td>small deficit</td><td>about zero</td></tr></table>

Table 8  
The qualitative estimation for day

<table><tr><td>Day</td><td>Balance</td><td>Possibility distr.</td><td>Probability distr.</td></tr><tr><td>2</td><td>small deficit</td><td> $[-10, 1; -5, 0.3; -15, 0.3]$ </td><td> $[-10, 0.8; -5, 0.1; -15, 0.1]$ </td></tr></table>

In our context it is convenient to represent qualitative values using discrete fuzzy distributions. These are well suited to represent qualitative variables like interest rates and daily balances, for which a discrete set of relevant values and judgements about their corresponding possibility may be found. It is useless to represent these variables as continuous ones, because we need not to consider all the possible daily balances, distinguished by a few Lire. It's suffices to consider only the most significant (e.g. the best and the worst expected and the medium ones differentiated by 5 millions). Another important reason for using discrete distributions is the availability of simple and efficient methods of converting possibility values into corresponding probability distributions and stating linear qualitative and probabilistic constraints.

These methods permit us to gain computational efficiency without any significant loss of representational expressiveness. A general discussion about the tradeoff between representational expressiveness and computational efficiency in model building can be found in [1].

Several authors have investigated methods of converting possibility distributions to probability distributions while maintaining consistency [6,12,14]. We pursue here Dubois and Prade's [6] solution. Suppose that the uncertain interest rate for the operation (2, 3) is represented by a discrete possibility distribution $\pi$ ; this might for example be [9%, 1; 8%, 0.6; 10%, 0.6], where 9%, 8%, 10% are interest rates and 1, 0.6, 0.6 are their respective possibility values. Denote by $\pi_1 \ldots \pi_n$ the possibility values in descending order, so that $\mu_1$ represents the highest value 1 and $\pi_n$ represents the lowest value. For any possibility value $\pi_i$ ( $i = 1 \ldots n$ ) the corresponding probability value $p_i$ is given by

$$
p _ {i} = \sum_ {j = 1} ^ {n} \frac {\pi_ {j} - \pi_ {j + 1}}{j} \text { with } \pi_ {n + 1} = 0.
$$

Thus in our example we have:

$$
\begin{array}{r l} & p _ {1} = (1 - 0. 6) + (0. 6 - 0. 6) / 2 + (0. 6 - 0. 0) / 3 \\ & \quad = 0. 6 \\ & p _ {2} = (0. 6 - 0. 6) / 2 + (0. 6 - 0. 0) / 3 = 0. 2 \\ & p _ {3} = (0. 6 - 0. 0) / 3 = 0. 2 \end{array}
$$

It will be seen that if $\pi_{1}\ldots\pi_{n}$ are in descending order and $\pi_{1}=1$ , the probability values $p_{1}\ldots p_{n}$ will necessarily sum to 1. We can now replace the original possibility distribution [9%, 1; 8%, 0.6; 10%, 0.6] with a probability distribution [9%, 0.6; 8%, 0.2; 10%, 0.2] which can be used in the simple recourse model.

Applying the same method to the balances, the qualitative estimates for day 2 can be represented by a discrete possibility distribution which replace the precise estimates of -10 used in table 4, and the associated probability distribution can be computed (Table 8).

Table 9

<table><tr><td colspan="3">The probabilistic estimation for day 3</td></tr><tr><td>Day</td><td>Balance</td><td>Probability distribution</td></tr><tr><td>3</td><td>about zero</td><td>[0, 0.8; -5, 0.1; 5, 0.1]</td></tr></table>

According to the statistical information available, the qualitative estimates for day 3 can be represented directly by a discrete probability distribution (Table 9) which replaces the precise estimate used in Table 4,

## 5. The simple recourse model

The two-stage simple recourse model $[19,20,23]$ can be applied when some parameters in a linear programming problem are replaced by discrete probability distributions. The basic idea of the simple recourse model is to construct a larger linear programming problem that takes account of the various outcomes permitted by the uncertain parameters.

Beale [2] has shown that uncertain coefficients in the objective function can be replaced by an average of the possible values weighted according to their probabilities. Thus the interest rate for $(2, 3)$ is given by

$$
(9.0 * 0.6) + (7.0 * 0.2) + (11.0 * 0.2) = 9.0\%
$$

and, applying a spread of 1%, the rate for $(3, 2)$ is 10.0%.

The uncertain balances cannot be treated so simply since they affect the constraints. The simple recourse method deals with uncertainty in the b vector by reformulating the constraint so that all possible outcomes are considered. In the original deterministic formulation of the problem, the balance constraint for day 2 was

$$
\mathrm{x} _ {2 1} + \mathrm{x} _ {2 3} - \mathrm{x} _ {1 2} - \mathrm{x} _ {3 2} = - 1 0
$$

where $x_{21}$ , $x_{32}$ are the amounts for the borrowing operations (2, 1) and (3, 2), $x_{12}$ , $x_{23}$ are the amounts for the lending operations (1, 2) and (2, 3), and -10 is the initial balance (in this case a deficit). Intuitively, the meaning of the constraint is that the operations (1, 2) and (3, 2) must provide sufficient revenue on day 2 to cover the initial deficit of 10 billion lire together with the extra expense due to the operations (2, 1) and (2, 3). The solution in table 5 respects this constraint because $x_{12}$ is set equal to 10, and all other amounts to zero.

The probability distribution for day 2 assigns probabilities to three levels of the initial balance: -5, -10, and -15. For each of these levels a separate constraint is formulated, introducing some further variables to take up the positive or negative slack. We can think of the discrete levels -5, -10, -15 as representing different predictions of the initial balance and $y_{21}^{+}$ , $y_{21}^{-}$ , $y_{22}^{+}$ , $y_{22}^{-}$ , $y_{23}^{+}$ , $y_{23}^{-}$ as the amounts (positive or negative) by which these predictions deviate from the value eventually observed.

$$
\begin{array}{l} \mathrm {x_ {21} + x_ {23} - x_ {12} - x_ {32} + y_ {21} ^ {+} - y_ {21} ^ {-} = - 5} \\ \mathrm {x_ {21} + x_ {23} - x_ {12} - x_ {32} + y_ {22} ^ {+} - y_ {22} ^ {-} = - 10} \\ \mathrm {x_ {21} + x_ {23} - x_ {12} - x_ {32} + y_ {23} ^ {+} - y_ {23} ^ {-} = - 15} \end{array}
$$

For any proposed solution, the variables $y_{21}^{+}, y_{21}^{-}$ , etc. here represent positive or negative deviations which are evaluated in the objective function. For instance, the plan of lending 10 billion lire from day 1 to day 2 will leave a deficit of 5 billion on day 2 if the initial balance turns out to be -15 billion, as in the third of the above constraints, and so $y_{23}^{-}$ will assume the value 5.

A similar treatment is needed for day 3, which has a balance estimated by the probability distribution $[0, 0.8; -5, 0.1; 5, 0.1]$ . The original constraint

$$
\mathbf {x} _ {3 1} + \mathbf {x} _ {3 2} - \mathbf {x} _ {1 3} - \mathbf {x} _ {2 3} = 0
$$

is replaced by the constraints

$$
\begin{array}{l} \mathbf {x} _ {3 1} + \mathbf {x} _ {3 2} - \mathbf {x} _ {1 3} - \mathbf {x} _ {2 3} + \mathbf {y} _ {3 1} ^ {+} - \mathbf {y} _ {3 1} ^ {-} = - 5 \\ \mathbf {x} _ {3 1} + \mathbf {x} _ {3 2} - \mathbf {x} _ {1 3} - \mathbf {x} _ {2 3} + \mathbf {y} _ {3 2} ^ {+} - \mathbf {y} _ {3 2} ^ {-} = 0 \\ \mathbf {x} _ {3 1} + \mathbf {x} _ {3 2} - \mathbf {x} _ {1 3} - \mathbf {x} _ {2 3} + \mathbf {y} _ {3 3} ^ {+} - \mathbf {y} _ {3 3} ^ {-} = + 5 \end{array}
$$

To complete the model, the objective function must be extended so that it evaluates any surpluses or deficits resulting from the uncertain initial balances on days 2 and 3. In this domain it seems more natural to define the objective function in terms of profit rather than cost. We therefore aim to maximize the total profit Z, given by the formula:

$$
\begin{array}{r l} Z = 7 x _ {1 2} + 2 0 x _ {1 3} + 9 x _ {2 3} - 8 x _ {2 1} - 2 2 x _ {3 1} - 1 0 x _ {3 2} \\ & + q _ {2} ^ {+} \left(0. 1 y _ {2 1} ^ {+} + 0. 8 y _ {2 2} ^ {+} + 0. 1 y _ {2 3} ^ {+}\right) \\ & + q _ {2} ^ {-} \left(0. 1 y _ {2 1} ^ {-} + 0. 8 y _ {2 2} ^ {-} + 0. 1 y _ {2 3} ^ {-}\right) \\ & + q _ {3} ^ {+} \left(0. 1 y _ {3 1} ^ {+} + 0. 8 y _ {3 2} ^ {+} + 0. 1 y _ {3 3} ^ {+}\right) \\ & + q _ {3} ^ {-} \left(0. 1 y _ {3 1} ^ {-} + 0. 8 y _ {3 2} ^ {-} + 0. 1 y _ {3 3} ^ {-}\right) \end{array}
$$

where $q_{2}^{+}$ and $q_{2}^{-}$ associate profits with a surplus or deficit on day 2, and $q_{3}^{+}$ and $q_{3}^{-}$ associate profits with a surplus or deficit on day 3. The values of $q_{2}^{+}$ , $q_{2}^{-}$ , $q_{3}^{+}$ , $q_{3}^{-}$ , might be selected according to the assumption that unexpected surpluses/deficits must be utilized/covered at unfavourable rates. By varying these values we can obtain different solutions which reflect different degrees of optimism or pessimism.

Suppose for example that unexpected surpluses on days 2 and 3 can be lent at the low rates of 3% and 4% (these assumptions remain constant), and that we vary the borrowing rates $[q_{2}^{-}, q_{3}^{-}]$ from $[5\%, 4\%]$ (extremely optimistic assumption) to $[20\%, 19\%]$ (extremely pessimistic). As we move along this scale, four different solutions are produced:

Borrowing rates: [5%, 4%] to [13%, 12%]

Solution 1: Lend 10 from day 1-2; Lend 10 from day 2-3.

Borrowing rates: [13%, 12%] to [14%, 13%]
Solution 2: Lend 10 from day 1-2.

Borrowing rates: [14%, 13%] to [16%, 15%]
Solution 3: Lend 10 from day 1–3; Borrow 5 from day 3-2.

Borrowing rates: [16%, 15%] to [20%, 19%]

Solution 4: Lend 10 from day 1-2; Borrow 10 from day 3-2.

## 6. Discussion

The models we have described can be implemented conveniently using the technology of constraint logic programming (CLP). A program for liquidity management with precise quantitative data $[15]$ has been implemented in the CLP language CHIP $[17]$ , which allows the formulation of constraints in a declarative style based on PROLOG; a simplified version of this system has been modified so that it can accept uncertain data in the form of discrete possibility or probability distributions.

In liquidity management, an adequate plan must satisfy a set of balance constraints, which require that on any day the bank closes without any significant surplus or deficit. In CHIP, the balance constraint for a given day can be formulated by the expression

$$
\text { InterbankExpenses } = \text { InterbankRevenues }
$$

## + InitialBalance

which means that expenses due to lending and repayments on the interbank market must exceed revenues due to borrowing and receipts by an amount equal to the initial balance resulting from the other transactions of the bank. If the initial balance is unknown, because the other transactions are only partly predictable, this constraint becomes fuzzy. We want to say that on day 3, the interbank revenues should be a little larger than the interbank expenses in order to cover a possible small deficit. This paper has shown that such constraints can be incorporated into a simple recourse model provided that they are formalized as discrete possibility distributions.

The introduction of uncertainty into the planning system allows the user to produce a range of plans which reflect different attitudes towards risk. If future rates and balances were known for certain, there would be no need to take account of risk attitude: prudent and adventurous treasurers would select the same plan. Since in fact some parameters are uncertain, it might happen for example that a small deficit is predicted on day N, when interest rates are expected to be low, thus confronting the treasurer with a dilemma. The prudent treasurer might renounce some profitable alternative operations in order to ensure that the deficit is covered; the adventurous treasurer might instead allow a large deficit to accumulate on day N, assuming that he/she can borrow cheaply when the day arrives.

These diverse attitudes to risk can be represented in the model by the values assigned to the coefficients $q_{N}^{+}$ and $q_{N}^{-}$ in the objective function. Since $q_{N}^{+}$ depends on the lending rate for an unexpected surplus, and $q_{N}^{-}$ on the borrowing rate for an unexpected deficit, we can obtain a prudent plan by imposing a large spread between the borrowing and lending rates (e.g. 13% and 5%), so that borrowing is expensive and lending unprofitable; by making borrowing cheaper and lending more profitable we obtain more adventurous plans.

<table><tr><td rowspan="2">Pessimism</td><td>Prudent</td><td>Neutral</td><td>Risky</td><td>Optimism</td></tr><tr><td>S1</td><td>S2</td><td>S3</td><td>S4</td></tr></table>

Fig. 1. Relationship between solution and risk attitude

In experiments with a small number of fuzzy constraints we have found that typically three or four different solutions are generated as the values of $q_{N}^{+}$ and $q_{N}^{-}$ are gradually moved along the scale from pessimism to optimism. This situation is shown schematically in Fig. 1, in which the horizontal line represents the dimension pessimism-optimism, and the lower vertical lines show the boundaries where one solution gives way to another. To establish a relationship between a qualitative statement of risk attitude (e.g. prudent, neutral, risky) and the solution sequence S1...S4, it would be necessary to define the boundaries between these attitudes.

## Acknowledgements

We would like to express our gratitude to Prof. Roy Leitch for hosting Enrico Martinelli at Heriot-Watt University, Edinburgh, and to Prof. Degli Antoni of Milan University for providing support for this visit and for some ideas. The work on constraint logic programming was conducted using the language CHIP developed at ECRC, Munich; we thank Dr. Alexander Herold of ECRC for technical support. Our thanks are also due to Prof. Fabio Schoen of Milan University for useful discussions about the simple recourse model, and to the Banca Popolare Veneta for expertise on liquidity management.

## References

[1] A.V. Balakrishnan and A.B. Whinston, (1991) Information Issues in Model Specification. Information System Research 2(4), 263–286, 1991.

[2] E. Beale, (1955) On minimizing a convex function subject to linear inequalities. J. Roy. Statist. Soc., Ser. B. 17, 173–184.

[3] D. Berleant and B.J. Kuipers, (1992) Qualitative-numeric simulation with Q3, In. B. Faltings and P. Struss, eds., Recent Advances in Qualitative Physics, MIT Press, Cambridge, MA, 1992.

[4] J. Broek, and H. Daniels, (1991) Application of constraint logic programming to asset and liability management in banks. Computer science in economics and management 4, 107–116.

[5] G. Dantzig, (1963) Linear programming and extensions. Princeton University Press.

[6] D. Dubois and H. Prade, (1983) Unfair coins and necessity measures: towards a possibilistic interpretation of histograms. Fuzzy sets and systems 10, 15–20.

[7] F. Gardin, G. Baldassi, R. Power, C. Rossignoli and H. Taylor, (1991) SEPT: a hybrid intelligent system for the bank treasury dealing room. Proceedings of the first conference on Artificial Intelligence on Wall Street, October 1991, New York.

[8] F. Gardin and S. Vaturi, (1989) A calculus based on qualitative order of magnitude and its applications to financial mathematics. In R. Huber et al (ed) Artificial Intelligence in scientific computation: towards second generation systems. J.C. Baltzer AG, Scientific Publishing Co., IMACS, 73–81.

[9] Hinkknanen et al (1993) On the Usage of Qualitative Reasoning as an Approach Towards Enterprise Modelling, working paper, Center of Information System Management, The University of Texas, Austin TX (forthcoming in: Annals of Operations Research, Special Volume on Data, Expert Knowledge and Decisions).

[10] J. Kallberg and W. Ziemba, (1983) Comparison of alternative utility functions in portfolio selection problems. Management Science 29, 1257–1276.

[11] R. Leitch and Q. Shen, (1992) Being committed to qualitative simulation. In R. Leitch (ed) Proceedings of the 6th international workshop on qualitative reasoning about physical systems, Heriot-Watt University, Edinburgh.

[12] Y. Leung, (1980) Maximum entropy estimation with inexact information. In R. Yager (ed.) Fuzzy set and possibility theory: recent developments. Pergamon Press, 32–37.

[13] M.W. Merkhofer, (1987) Quantifying Judgmental Uncertainty: Methodology, Experience and Insights, In IEEE Transactions on Systems, Man, and Cybernetics, Vol. SMC-17, 741–752.

[14] S. Moral, (1986) Construction of a probability distribution from fuzzy information. In A. Jones et al (eds.) Fuzzy set theory and applications, 51–60.

[15] R. Power, H. Taylor and F. Gardin, (1993) Treasury management: a support system implemented in CHIP. CHIC project internal report.

[16] H. Taylor, G. Trotta and I. Zaniboni, (1989) Descrizione del funzionamento del sistema esperto di pianificazione, In Un sistemo esperto per la gestione della tesoreria, M. De Marco (ed), Universita' Cattolica di Milano.

[17] P. Van Hentenryck, (1989) Constraint satisfaction in logic programming MIT Press, Cambridge Mass.

[18] M. Vescovi and L. Travé-Massuyès, (1992) A constructive approach to qualitative fuzzy simulation. In R. Leitch (ed) Proceedings of the sixth international workshop on qualitative reasoning about physical systems, Heriot-Watt University, Edinburgh.

[19] D. Walkup and R. Wets, (1967) Stochastic programs with recourse. SIAM J. Appl. Math 15, 1299–1314.

[20] R. Wets, (1966) Programming under uncertainty: the complete problem. Z. Wahrscheinlichkeitstheorie verw. Geb. 4, 316–339.

[21] B.C. Williams, (1991) A theory of interactions: unifying qualitative and quantitative algebraic reasoning, Artificial Intelligence, 51, 39–94.

[22] L. Zadeh, (1978) Fuzzy sets as a basis for a theory of possibility. Fuzzy sets and systems 1, 3–28.

[23] W. Ziemba, (1975) Stochastic programs with simple recourse. In P. Hammer and G. Zoutendijk (eds.) Mathematical programming: theory and practice. North Holland: Amsterdam, 213–273.

![](/api/attachments/3EFK5AHQ/fulltext/images/5b6346761ce54ff0e2849d2761bb1b2728910edc0659c8e8f7845688dcde532c.jpg)

Francesco Gardin graduated in Physics from the University of Padua. Subsequently he undertook research in symbolic calculation, LISP programming and expert systems (1980–1983) at the Computer Science Laboratory of Exeter University. He then lectures in the Theory and Application of Computing Machines at the University of Udine and in Artificial Intelligence at the Department of Computer Science of the University

of Milan. In 1982, he founded AIS Spa, of which he is currently Managing Director, for the planning and marketing of financial applications based on Artificial Intelligence. In 1988 he founded ARS and ACS which specialize in Artificial

Reality Systems and Parallel Computing and Neural Networks. His research activity is spread amongst four principal sectors: basic research into Artificial Intelligence, expert systems, artificial reality, parallel computing and neural networks. He is author of more than forty publications in the above areas and he is also a member of the editorial board of several scientific journals. He is supervisor of more than fifty master theses.

Richard Power was born in London in 1948. He has a B.A. in Psychology from the University of Sheffield (1970), and a PH.D. from The Department of Machine Intelligence at the University of Edinburgh (1974). After 3 years as research fellow in the Sussex University Experimental Psychology Laboratory he emigrated to Italy, where he became chief scientist of the Milan-based company Artificial Intelligence Software. Since 1993 he has held the post of senior research fellow at the Information Technology Research Institute of the University of Brighton. He has published 30 papers mainly in the fields of Computational Linguistics and Expert Systems.

![](/api/attachments/3EFK5AHQ/fulltext/images/c15618310d3f9010afc3f00084e210f261b10e785df87245da6fec96d0d6df65.jpg)

Enrico Martinelli was born in Milan in 1968. He received the degree in Computer Science in February 1994 from University of Milan. In 1993, during his thesis, he was a visiting researcher at the Heriot-Watt University of Edinburgh where he investigated the potential using of Constraint Logic Programming languages as an implementation engine for qualitative simulation. From March 1994 he is employee in the Milan-based

company Artificial Intelligence Software. His research interests include constraint logic programming with particular emphasis on its application in nondeterministic environments and the application of Fuzzy logic in decision support systems and expert systems in financial management.
