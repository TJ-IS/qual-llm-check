---
otero_id: 17631
otero_key: "8RXFVDDV"
title: "A behavioral approach of the dynamics of financial markets"
authors: "M. Sanglier; M. Romain; F. Flament"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90056-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A behavioral approach of the dynamics of financial markets $^{*}$

M. Sanglier \*, M. Romain, F. Flament 1

Instituts Internationaux de Physique et de Chimie, fondés par E. Solvay, Université Libre de Bruxelles, Campus Plaine CP231, 1050 Bruxelles, Belgium

We introduce a non-linear dynamic deterministic multi-stocks multi-agents model. The model can be viewed as the centre of a decision support system in managing financial portfolios, that would allow the decision maker to formalize, test and analyze the impacts of strategies on a market. It takes into account explicitly the perceptions, strategies and decisions of actors and their actions on a market. This approach attempts to model the decision process of interacting agents and so furnishes a tool for decision making in order to analyze the impacts of various strategies of actors on a market. Even in this simple model, the non-linear interactions can drive the system to sudden and unexpected effects which shows the importance of the attempt of the understanding of the dynamics.

Keywords: Non-linear models; Behaviour; Human decision making; Complex systems

## 1. Introduction

## 1.1. Background in non-linear dynamics

Dynamic non-linear models generating unpredictable behaviour as well as the concept of Self-Organization [8] are becoming more and more popular in financial economics [4]. This research attempts to bring the new concepts emerging from “self-organizing dynamic systems theory” [9] to bear on the issue of market dynamics. Instead of simply assuming instantaneous market equilibrium, it will explicitly consider the perceptions, strategies and decisions of the actors over time, generating in this way the changes in price and yield observed in the system. It will be an adapting learning model displaying complex temporal behaviour and emergent collective effects.

This new approach of complex system dynamics has already been applied on different domains such as, traffic flows $[11]$ and urban dynamics $[12]$ . The previous models were generally rather complex because of their high dimensionality (social, economical, spatial). In this application we attempt to represent the interaction of agents on a market in a simple way. The stock market is seen as an example. Our main purpose is to understand the impact of different strategies on the evolution of prices.

## 1.2. Financial area

The economic literature shows more and more evidence of the presence of non-linear dynamics, and chaos in theoretical, empirical and experimental works $^{2}$ . It is out of the scope of this paper to discuss the efficiency hypothesis as well as the existence of speculative bubbles and chaos $^{3}$ .

Psychologist experiments show that human beings are not completely rational decision makers. Shefrin and Statman [14] use some of these results to argue that investors may have an “irrational” preference for cash dividends. They explain this assumption by using two different theories on individual choice behaviour: the theory of self control [19] and the theory of choice under uncertainty [7].

Our approach, like Orlean [10], Topol [21] and Shiller [15] shows that financial markets can present an internal endogenous dynamic based on agents interactions. Prices are analyzed as the outcome of the sell and buy orders themselves activated by observation of exogenous and endogenous signals. The key element is that these interactions are non-linear by nature.

## 1.3. Behavioral approach

Hogarth [5] emphasizes “..the continuous adaptive nature of judgmental process used to cope with a complex changing environment..”.

In our model we focus on the way individual proceeds information. We try to consider explicitly perceptions, strategies and decisions of the actors and their impacts on the dynamics of the market. We assume that the agents adapt their way to improved decisions. More precisely, we have introduced explicitly an adaptation mechanism corresponding to a endogenous modification of certain decisional parameters. This research is in the field of the concept of bounded rationality $[16]$ that recognizes constraints internal to the decision maker. Decision makers act following their capacity to proceed the information.

Here the concept of the “mental map” is captured by the so-called “attractiveness function” (see equation (4)) which reflects the psychology and the relative sensitivity of an agent to signals (economic or others). So even when the actors receive the same information, they have their own interpretation and their different perception of the signals produce differentiated behaviours. In this approach, the classical micro economic utility functions is replaced by the concept of attractiveness.

## 1.4. Decision support system

The presence of non-linear dynamics interacting agents with different strategies requires that the problem to be formalized in terms of a decision support system. The aim of this approach is to capture some mechanisms inducing changes of structure, instead of describing the observed structure. The decision maker must learn how this system operates, what are the impacts on his strategy on the market, which strategy could be the best in a given environment. This tool must be viewed as an “integrator” [18] which allows the decision maker to test his intuitions and anticipation in an non-linear dynamical context.

This type of approach needs a flexible integrated, and adaptable support system at different levels:

1. choice of strategies, where some can be related to expert system

2. choice of the market environment (type of assets treated by the system)

3. choice of “internal model” other forms of interaction can be taken into account than the one presented in this application.

Another important characteristic of this support must be that the internal model of the relations between the variables cannot treated as “a black box” [17], the system must specify explicitly the concept, the model and the rule to the decision maker. With an endogenous change of strategy and rules, this system is related to the dynamic support system field [22].

This paper could be the first step in the building of a decision support system for the exploration and the understanding of the impact of strategies of actors on the dynamic of a financial market.

## 2. Description of the model

We have developed a dynamic multi-stocks multi-agents model with different strategies. These strategies lead actors to anticipations $^{4}$ according to their individual treatment of economic signals.

The question faced by the individual is when to buy or when to sell in order to increase his wealth. This decision process is quite complex, since it requires to perceive and to understand the variables of the economic environment and the models of competitors playing on the same market.

The orders are not thus inspired by the idea of an “optimal portfolio”, but are a synthesis of their “mental maps” (personal perception of economic environment, and interpretation before decision making) and their financial wealth. The signals are translated differently into purchase and sale orders by agents as a function of their own “mental maps” of the system. The intensity of orders for a given stock is a function of the price of the security, the wealth of the agent and the attractiveness of this stock relative to the other assets available. The difference between the desired number of shares and the actual number held by every agent is the driving force of motivation to readjust the desired quantity $^{5}$ .

Borrowing from Market Model [13], we define the set of information as the return, the risk and the security relative price variation. The pricing mechanism for the stock i is as follows:

$$
\frac {\Delta \mathrm{X} _ {\mathrm{i(t)}}}{\Delta \mathrm{t}} = \eta_ {\mathrm{i}} \mathrm{X} _ {\mathrm{i(t)}} \binom{\sum_ {\mathrm{k}} \mathrm{U} _ {\mathrm{i(t)}} ^ {\mathrm{k}}}{\frac {\sum_ {\mathrm{k}} \mathrm{N} _ {\mathrm{i(t)}} ^ {\mathrm{k}}}{\sum_ {\mathrm{k}} \mathrm{N} _ {\mathrm{i(t)}} ^ {\mathrm{k}}} - 1}\tag{1}
$$

Let $X_{i(t)}$ be the price of the asset i and $\eta_i$ a parameter which is a measure of the relative adjustment of the price $X_{i(t)}$ to the difference between the number of stock i held by the agent k, $N_i^k(t)$ and the desired number of shares, $U_i^k(t)$ . Every moment, each agent estimates the desired number of shares, $U_i^k(t)$ according to his financial wealth $Y^k(t)$ , the market value of the stock $X_i(t)$ , and the relative attractiveness of this stock as regards to the other assets.

$$
\mathrm{U} _ {\mathrm{i(t)}} ^ {\mathrm{k}} = \frac {\mathrm{Y} _ {(\mathrm{t})} ^ {\mathrm{k}}}{\mathrm{X} _ {\mathrm{i(t)}}} \frac {\mathrm{A} _ {\mathrm{i(t)}} ^ {\mathrm{k}}}{\sum_ {\mathrm{j}} \mathrm{A} _ {\mathrm{j(t)}} ^ {\mathrm{k}}}\tag{2}
$$

The wealth $Y^{k}(t)$ of an agent is calculated by the expression:

$$
\mathbf {Y} _ {(t)} ^ {k} = \sum_ {k} N _ {i (t)} ^ {k} X _ {i (t)}\tag{3}
$$

The attractiveness of a stock $A_{i}^{k}(t)$ takes into account the relative sensitivity of an agent to different signals. In this case, we only considered some basic economic signals (risk, return, trends):

$$
\begin{array}{r l} & = \exp \left(\left(\nu_ {\mathrm{i(t)}} ^ {\mathrm{k}} r _ {\mathrm{i(t)}} - \mu_ {\mathrm{i}} ^ {\mathrm{k}} \sigma_ {\mathrm{i}} + \tau_ {\mathrm{i}} ^ {\mathrm{k}} \left(\frac {X _ {\mathrm{i(t)}} - X _ {\mathrm{i(t-1)}}}{X _ {\mathrm{i(t)}}}\right)\right) \right. \\ & \quad \times \left(1 + \Psi_ {\mathrm{i}} ^ {\mathrm{k}} \frac {Y _ {\mathrm{i(t)}} - Y _ {\mathrm{i(t-1)}}}{Y _ {\mathrm{i}}}\right) \end{array} \tag {4}
$$

where $\nu_{i}^{k}$ , $\mu_{i}^{k}$ and $\tau_{i}^{k}$ are the relative sensitivity of the agent k for the return $r_{i}(t)$ , risk $\sigma_{i}(t)$ and trend respectively.

The trend $^{6}$ is defined by:

$$
\left(\frac {\mathrm{X} _ {\mathrm{i(t)}} - \mathrm{X} _ {\mathrm{i(t-1)}}}{\mathrm{X} _ {\mathrm{i(t)}}}\right)
$$

In this application, we computed the risk $\sigma_{i}(t)$ and the return $r_{i}(t)$ as follow:

1. the return of a stock i at time t is a constant proportion of the return of all market $(R_{M(t)})$ : following the relation of the Market Model

$$
\mathbf {r} _ {\mathrm{i(t)}} = \alpha_ {\mathrm{i}} + \beta_ {\mathrm{i}} \mathbf {R} _ {\mathrm{M(t)}} + \epsilon_ {\mathrm{i(t)}}\tag{5}
$$

where:

$R_{M(t)}$ : is the market index at time t

$\beta_{i}$ : measures the degree of sensitivity of the share i to the market

$\epsilon_{i(1)}$ : is the part of the return due to specific factors of the firm

2. We estimate the risk of a share with the standard error of the return estimated over the n last observations $^{7}$ according to the Portfolio Theory [2]:

$$
\sigma_ {\mathrm{i}} ^ {2} = \frac {1}{N - 1} \sum_ {\mathrm{t} = 1} ^ {N} \left(\tilde {\mathrm{r}} _ {\mathrm{it}} - \mathrm{r} _ {\mathrm{i}}\right) ^ {2}
$$

Table 1

where $\tilde{r}_{it}$ is stock return in period t and $r_{i}$ is the mean value of $\tilde{r}_{it}$ .

The relation of the attractiveness concerns stocks belonging to the considered market, but our agents could be also sensitive to other assets or to the interest rate. This effect can be introduced with an external attractiveness.

In the second part of the description of the simulation, we analyzed the impacts of an endogenous change of the strategy of the actors given by the term with $\Psi_{i}^{k}$ . This means that the attractiveness of the actors is reinforced for stocks that have increased their wealth during the previous period and the contrariwise.

The term $U_{i}^{k}(t)$ corresponds to the management of the actor, but does contain neither the orders which are actually executed nor how the portfolio will be readjusted.

If the orders are naturally the difference between what they want and what they actually have, it is most unlikely that such a junction of all the expectations fulfils the desires of everyone. This difference will lead agents to readjust their desires, to elaborate a new plan, and to react on the market with new demands and new supplies.

The equation for the evolution of the number of shares $N_{i}^{k}(t)$ held by an agent k could be given by:

$$
\frac {\Delta \mathrm{N} _ {\mathrm{i(t)}} ^ {\mathrm{k}}}{\Delta t} = \xi_ {\mathrm{i}} ^ {\mathrm{k}} \left(\mathrm{U} _ {\mathrm{i(t)}} ^ {\mathrm{k}} - \mathrm{N} _ {\mathrm{i(t)}} ^ {\mathrm{k}}\right)\tag{6}
$$

where $\xi_{i}^{k}$ is the relative rate of the execution of the orders.

The interaction scheme (Fig. 1) shows how the system operates.

## 3. Data of the simulations

## 3.1. Reference value of the price of the stocks

For this first application, we have chosen four shares, with different values of parameter $\beta$ (Table 1), quoted on the Belgian stock market during the period January to March 1985. The shares selected are: “Royale Belge” (RB), “Banque Bruxelles Lambert” (BBL), “Krediet Bank” (KB) and “Sofina” (Sof). The first is an insurance company, the second and the third are financial companies and the last is a chemical firm.

![](/api/attachments/8RXFVDDV/fulltext/images/b2eafd95fa057fd44e9105f620b05dd94d80f83df4903cd6bee7e20e3dbd5c28.jpg)  
Fig. 1. Interaction scheme of the model.

All these firms are characterized by good profitability, so that a fundamental analysis could have justified the continuous presence of agents on this market. They show different values of parameters,. as it is reported in Table 1.

## 3.2. Strategy of the actors

In order to observe rather interesting results but as simple as possible, the most desirable set of financial agents must be a compromise between a minimal number and very differentiated behaviours.

Characteristic parameters of the stocks

<table><tr><td></td><td> $\alpha_{i}$ </td><td> $\beta_{i}$ </td></tr><tr><td>R.B.</td><td>0.0009</td><td>0.54</td></tr><tr><td>B.B.L.</td><td>0.0007</td><td>0.70</td></tr><tr><td>K.B.</td><td>0.0001</td><td>1.47</td></tr><tr><td>SOF</td><td>-0.0018</td><td>1.44</td></tr></table>

Characterization of the strategies of the actor in term of their sensitivity to signals

<table><tr><td></td><td>Mixed</td><td>Neutral</td><td>Risk taker</td><td>Bull</td><td>Bear</td></tr><tr><td> $R_{i}^{t}$ </td><td>+</td><td>+</td><td>+</td><td>0</td><td>0</td></tr><tr><td> $σ_{i}^{t}$ </td><td>0</td><td>+</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $ΔX_{i}>0$ </td><td>+</td><td>0</td><td>0</td><td>+</td><td>0</td></tr><tr><td> $ΔX_{i}<0$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>+</td></tr></table>

0 = not interested in, + = interested in.

We have chosen 5 types of actors divided into three categories.

2 actors following a market model (equation (5)): neutral and risk taker

2 chartist actors: bull, bear

## 1 mixed

They are characterized by different sensitivities to return, risk and trends. This is illustrated by Table 2.

The different parameters of the basic simulation are described in the appendix. For the initial conditions, the agents have the same portfolio and the wealth is equally distributed between the different assets.

The mixed, agent 1, is influenced by both the return and the trend.

The actors following a market model are defined as follows:

Neutral agent, agent 2 is sensitive both to the return and the risk.

Risk taker, agent 3 will invest in assets having a greater return without taking into account the corresponding risk factor.

The two "chartists".

![](/api/attachments/8RXFVDDV/fulltext/images/88b99bd88f6c2ea9b6820fa54d926e7c2fdf39d6183f95d7fa98a08f2172003e.jpg)  
Fig. 2. Evolution of the data of the return calculated for RB and BBL shares.

![](/api/attachments/8RXFVDDV/fulltext/images/1a39240410eb5eb5063eb33d4973d90e95b5f7d3e0495f601af75ccef68d232f.jpg)  
Fig. 3. Evolution of the data of the return calculated for KB and Sof shares.

Bull, agent 4, has a high propensity to buy shares with a growing price, the underlying hypothesis of this strategy supposes that the market always confirms its trend.

Bear, agent 5's strategy, is to anticipate changes in the market, believing that once a trend in the market has become established, it is too late to obtain profits following this trend.

Agents having more realistic and sophisticated behaviours can be easily imagined and simulated, however in a first attempt to understand the dynamics of the market, it is better to modelize the system with the above actors. In further applications, we could introduce explicit imitation between the actor as Orlean [10] has considered in his mimetic models.

## 3.3. Data of the risk and return

Returns for the four stocks are obtained following equation (5) (Figs. 2 and 3). This is one possibility; other choices could have been made.

This approach has the advantage of linking the evolution of a share with its environment, it distinguishes a risk associated with the whole market (volatility of trends of the market have consequences on future prices) and a specific risk of the firm.

## 4. Results of the simulations

4.1. Comparison between the simulated price and the data

The comparison between the simulated price and the true value is only an illustration, which help us to calibrate the parameters of the model, (in this simulation $\Psi_{i}^{k}=0$ ). This comparison shows a qualitative agreement for the movement of the price for RB, KB and Sof stocks (Fig. 4). It is difficult to reproduce all the “real” price evolutions, as our agents have only the choice between the four shares, so if they want to buy some, they have to sell some other ones. In this simplest version, we have not considered the possibility for our agents to choose other assets to increase their financial capitalization or to leave the market.

![](/api/attachments/8RXFVDDV/fulltext/images/7da33649315107dc44b408bf8e5791f323250bb97667c8c2abadbfb2c61f483c.jpg)

![](/api/attachments/8RXFVDDV/fulltext/images/2c0e00aa9694d07141df4acacd50faa2090697d0dff9ce5c0c5e9a849a9722ed.jpg)

This can be easily introduced in the model by considering for example an attractiveness for the interest rate or other assets.

The simulated curves in Fig. 4 have a one day delay compared to the real data. This effect comes from the fact that at the beginning of the period, the actors only know the return and risk parameters for the previous day. This has no effect on the dynamic of the system.

In terms of the evolution of portfolio, the dynamic is very complex. In Fig. 5, we observe

![](/api/attachments/8RXFVDDV/fulltext/images/23ee94bff31eed33ffde8aaa8e0bfe2a5d5973613897cd5f3ed72e36704e9203.jpg)

![](/api/attachments/8RXFVDDV/fulltext/images/c78497b3423d160134390d168617b2bd6ae1ecfffc842793ffa8d0a0aef7cac4.jpg)  
Fig. 4. (a) Evolution of the price for the RB share. (b) Evolution of the price for the BBL share. (c) Evolution of the price for the KB share. (d) Evolution of the price for the Sof share.

![](/api/attachments/8RXFVDDV/fulltext/images/7b94028aca4bb716711bae86566932f205fe62f77a2a3956a9411826fe031cb9.jpg)  
Fig. 5. Evolution of the risk taker actor's portfolio.

that the movement of the orders are much more important on the BBL stock as compared to the others. This is due to our choice of the initial conditions namely that the capitalization is distributed equally between the different assets.

## 4.2. Impacts of an endogenous change of the strategy

We have analyzed the impacts of an endogenous change of the strategy of the actors (expression (4)). The actors take into account the evolution of their wealth per stock in the previous period. Their attractiveness are reinforced for the stocks which has increased their profit and the contrariwise. The parameter $\Psi_{i}^{k}$ gives the intensity of this effect.

![](/api/attachments/8RXFVDDV/fulltext/images/c82cb8460f4dbe52460b74be9dc09d9c7f5cdcd7a27a61b5bf0cfbf4c7098ba8.jpg)  
Fig. 6. Wealth of the actors for the reference simulation with $\Psi_{i}^{k}=0$ .

![](/api/attachments/8RXFVDDV/fulltext/images/def10aa67eaed78311973536b7a8bbe1878d88441b10ae68f500131fb40ea76f.jpg)  
Fig. 7. Wealth of the actors for the simulation with $\Psi_{i}^{k}=220$ .

The simulation of the reference situation has been realized, without this effect, because $\Psi_{i}^{k}=0$ (Fig. 6). Comparing with a simulation with $\Psi_{i}^{k}=220$ (Fig. 7), we observe at the level of the evolution of their capitalization, that for all the winning actors, their profits are higher if they use this type of strategy and it is especially true for the bull actor. Also, we note that in the case of the reference simulation, the neutral actor has a higher profit than the mixed one and it is just the contrary for the simulation with $\Psi_{i}^{k}=220$ . But the most interesting point is shown in Fig. 8; the non-linear effect of the dynamic drives the system to a qualitatively different state, for a very small change of the parameter $\Psi_{i}^{k}$ .

![](/api/attachments/8RXFVDDV/fulltext/images/05cdc8c45b57c53c28b0f0a6c4a866aa8bc4d89dbf8910b51fef815d4eacd952.jpg)  
Fig. 8. Evolution of the wealth of the actor 3 for different values of $\Psi_{i}^{k}$ .

Table 3  
Values of the variables at the bifurcation point

<table><tr><td></td><td> $\Psi_{i}^{3}: 221$ t = 16</td><td> $\Psi_{i}^{3}: 222$ t = 16</td><td> $\Psi_{i}^{3}: 221$ t = 17</td><td> $\Psi_{i}^{3}: 222$ t = 17</td></tr><tr><td> $X_{1}$ </td><td>10146</td><td>10146</td><td>10697</td><td>10687</td></tr><tr><td> $N_{1}^{3}$ </td><td>5.34</td><td>5.33</td><td>19.5</td><td>18.2</td></tr><tr><td> $Y_{1}^{3}$ </td><td>54210</td><td>54109</td><td>208570</td><td>194386</td></tr><tr><td> $Y_{2}^{3}$ </td><td>70498</td><td>70475</td><td>48911</td><td>48895</td></tr><tr><td> $Y_{3}^{3}$ </td><td>165226</td><td>165392</td><td>113940</td><td>114057</td></tr><tr><td> $Y_{4}^{3}$ </td><td>259746</td><td>259700</td><td>178862</td><td>178832</td></tr><tr><td> $Y_{t}^{3}$ </td><td>549704</td><td>549715</td><td>550285</td><td>535636</td></tr></table>

More explicitly for agent 3 (who follows a market model), increasing $\Psi_{i}^{3}$ to 221.4 induces a growing trend of his wealth especially between t=16 and t=17. For $\Psi_{i}^{k}>221.5$ the trend goes in the opposite direction. By analysing more carefully the result, we observe that this effect is due to the attitude of agent 3 as regards to stock 1 (RB), and the impact of a big jump of this return (see Fig. 2), the consequences on the variable are presented in Table 3: the price of the stock has lost 10 francs, but this has no effect on the price of the other stocks; the wealth of the other actors is a little smaller.

This bifurcation reveals the unexpected and sudden effect which results from the non-linear dynamic of the system and shows that non-linear systems in certain regimes can be very sensitive to small changes of parameters. We show in Fig. 9, that the introduction of this endogenous change of strategy has some effects on the evolution of the price as well of course on the portfolio of the actors.

![](/api/attachments/8RXFVDDV/fulltext/images/c95f3f7b342846a41210af7fb1564bd25bd234400abd811472faebee4bde4326.jpg)  
Fig. 9. Effect of parameter $\Psi_{i}^{k}$ on the evolution of the price of Sofina stock.

## 5. Outlook in term of decision support system

This decision support system could be an interactive didactic game with two aspects:

1. the "player", the decision maker

He can choose his initial portfolio, his basic strategy and the market environment on which he wants to test his behaviour.

2. the other actors

This choice can be realized inside a catalogue of strategies. The “player” can explore various mixture of actors, predominance of institutional agents or speculative ones etc..

In that part, the following data must be defined:

a) the number of type of actors

b) their respective strategy

c) their initial portfolio

d) their rate of efficiency on the market

An additional feature can be introduced to the straightforward running of this system, by including a process by which the program can choose successful strategies, according to what the decision maker considers success to be.

## 6. Conclusions

We have presented here a multi-agents multi-stocks model which provides a tool to study financial dynamics. Our agents have an individual strategy, and create an “economic environment” in evolution. The financial dynamics generated by agents are instantly reinterpreted and produce rather new orders, new actions on the system. In any case, the imperfect perception of the system endows the actors with ignorance which cause (with differing opinions) exploration to occur. This is an important source for non-linearity common with social systems. Even in this simple model, the non-linear interactions can drive the system to sudden and unexpected effects which shows the importance of the attempt of the understanding of the dynamics.

Our future research will be oriented toward agents with more sophisticated strategies using either the fundamental and technical analysis or other provisional models with in some case a limited information. The model presented here is the first step of the elaboration of a didactic tool for market specialists. This tool could be considered as a “Dynamic Decision Support System”. Its users will have the opportunity to introduce their own technique, and they will be able to measure its impacts on a given environment.

## Acknowledgements

This work is supported by the Solvay Institute for Physics and Chemistry. The authors wish to thank I. Prigogine for his constant interest. E. Mosekilde and P. Praet are thanking for many fruitful and stimulating discussions. Thank to S. Wargnies for help with the computer treatment.

## Appendix

Table 4
Values of the parameters

<table><tr><td></td><td>mixed</td><td>neutral</td><td>risk taker</td><td>bull</td><td>bear</td></tr><tr><td> $\nu_{i}^{k} (i = 1..4)$ </td><td>150.0</td><td>200</td><td>200</td><td>0.0</td><td>0.0</td></tr><tr><td> $\mu_{i}^{k} (i = 1..4)$ </td><td>50</td><td>200</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td> $\tau_{i}^{k} (i = 1..4)$ </td><td>300.0</td><td>0.0</td><td>0.0</td><td>500</td><td>-900</td></tr><tr><td> $\xi_{i}^{k} (i = 1..4)$ </td><td>0.35</td><td>0.35</td><td>0.35</td><td>0.35</td><td>0.35</td></tr><tr><td> $\eta_{i} (i = 1..4)$ </td><td>0.1</td><td></td><td></td><td></td><td></td></tr></table>

Table 5  
Initial value of the variables

<table><tr><td>Share</td><td>RB Share</td><td>BBL Share</td><td>KB Share</td><td>Sofina</td></tr><tr><td> $X_{i}$ </td><td>10450</td><td>1750</td><td>7800</td><td>7310</td></tr><tr><td> $N_{i}^{k} (k = 1..4)$ </td><td>13</td><td>78</td><td>17.5</td><td>19</td></tr></table>

## References

[1] W.A. Barnett, J. Geweke, K. Shell, Economic Complexity. Cambridge University Press, 1989.

[2] R.A. Brealey, S.C. Myers, Principles of Corporate Finance, Mac Graw Hill International Editions, p. 127. 1988.

[3] W. Brock, ‘Chaos and Complexity in Economic and Financial Science’ in von Furstenberg G., Boston Kluwer Academic Publishers, 1990.

[4] P. De Grauw and K. Vansanten, Deterministic Chaos in Foreign Exchange Market, CEPR Discussion Paper N° 370, 1990.

[5] R. Hogarth, Beyond Discrete Biases: Functional and Dysfunctional Aspects of Judgmental Heuristics, Psychological Bulletin, vol. 90, 197–217, 1982.

[6] D. Hsieh, Testing for non-linear Dependence in Daily foreign Exchange Rates, Journ. of Business, vol. 62, N°3, 1989.

[7] D. Kahneman and D. Tversky, The Psychology of Preferences, Scientific American, vol. 246, 263–291, 1979.

[8] J. Lesourne, Economie de l'Ordre et du Désordre, Economica Paris, 1991.

[9] G. Nicolis and I. Prigogine, Self-Organization in Non-Equilibrium Systems, Wiley, New York, (1977).

[10] A. Orléan, Comportements Mimétiques et Diversité d'Opinions in 'Théorie Economique et Crises des Marchés Financiers', Economica, p. 45–65, 1989.

[11] I. Prigogine, R. Herman, Kinetic Theory of Vehicular Traffic, American Elsevier NY, (1971).

[12] M. Sanglier and P.M. Allen, Evolutionary Models of Urban Systems: an Application to the Belgian Provinces, Environment and Planning A, 21, p. 477–498, (1989).

[13] W.F. Sharpe, A Simplified Model of Portfolio Analysis, Management Science, p. 277–293, 1963.

[14] H.M. Shefrin, M. Statman, Explaining Investor Preference for Cash Dividend, Journal of Financial Economics, vol. 13, 253–282, 1984.

[15] R. Shiller, Stock Prices and Social Dynamics, Brooking Papers in Economic Activity, vol. 2, p. 457–498, 1984.

[16] H. Simon, Human Nature in Politics: The Dialogue of Psychology with Political Science, reprinted in: Miriam Campanella ed. Between Rationality and Cognition. Policy-making under Conditions of Uncertainty, Complexity and Turbulence, Torino, Albert Meynier, p. 11–34, 1988.

[17] H.G. Sol. Conflicting Experiences with DSS. Decision Support System, vol. 3, p. 203–211. 1987.

[18] R.H. Sprague, DSS in Context, Decision Support System, vol. 3, p. 197–202, 1987.

[19] R. Thaler, H.M. Shefrin, An Economic Theory of Self-control, Journal of Political Economy, vol. 98, 392–410, 1981.

[20] J.S. Thomsen, E. Mosekilde, and J.D. Sterman and 'Hyperchaotic Phenomena in Dynamic Decision Making' in Complexity, Chaos, and Biological Evolution, ed. by E. Mosekilde and L. Mosekilde, Plenum Press, New York, 1991.

[21] R. Topol, Bubbles and Volatility of Stock Prices: Effect of Mimetic Contagion, the Economic Journal, vol. 101, n° 407, p. 786–800, 1991.

[22] A. Verbaeck, F. Wierda, Interactive. Modelling for Information System Design the Mosaic Tool. Proceedings of the international Working Conference on Dynamic Modelling of Information System, the Netherlands, 1990.
