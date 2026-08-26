---
otero_id: 21742
otero_key: "8367XY3R"
title: "SIMAR: a software environment to define and test strategic management knowledge bases"
authors: "Michel R. Klein"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00026-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# SIMAR: a software environment to define and test strategic management knowledge bases

Michel R. Klein )

HEC Group, Information and Decision Support System Department, Jouy-en-josas 78350, France

## Abstract

The article describes the models used to simulate a consumer-good market, the firms competing on this market as well as the market allocation between products. The SIMAR application allows the formalisation of strategic knowledge under the form of rules. The first prototype of the application uses three simple knowledge bases coupled with the models to provide for each simulated firm a diagnosis on finance, product performance and production function. It is planned to use the blackboard architecture of the application to couple these knowledge bases to decide on the strategic decision of launching or abandoning a product. A future research goal is to automate the strategic decisions of the simulated firms and test formalised strategies in a simulated competitive environment. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Strategic knowledge bases; Company and market simulation; OPTRANS object; Knowledge base DSS development environment

## 1. Strategic management

## 1.1. Strategic management process

The term strategic management is usually defined as the process which describes the steps at the corporate and divisional level to develop marketdriven strategies for organizational survival and growth. The strategic management process for companies of a certain size will usually be broken down into strategic marketing process, new product development, production and financing. Strategic marketing, which we believe to be an important element in the strategic management process, is defined as ‘‘the steps taken at the product and<sup>r</sup>or market level to develop viable marketing plans and programs’’ 18 .<sup>w</sup> <sup>x</sup>

Carlsson defines strategic management as ‘‘the process of creating and Sustaining Competitive Advantage SCA over the planning period’’. He de- Ž . scribes this process as a six-step process ‘‘through which a company for a chosen planning period 1Ž . defines its operational context; 2 outlines and de- Ž . cides upon its strategic goals and long-term objectives; 3 explores and decides upon its strengths, Ž . weaknesses, opportunities and threats; 4 formulates Ž . its sustainable competitive advantages; and 5 de- Ž . velops a program of actions which exploits its competitive advantages and ensures profitability, financial balance, adaptability to sudden changes and a sound development of its capital structure’’ 2 . Ac-<sup>w</sup> <sup>x</sup> cording to Carlsson, the SCA is defined as ‘‘a composite of four conceptual constructs: the market position, the competitive position, the production position and profitability.’’ It is known that there is a normative approach and a descriptive approach to strategic management, Ansoff, being a representative of the former, and Minzberg of the second. We take the position here that: 1 We must understand how Ž . the strategic management process is going on in the organization if we wish to have some hope of implementing a decision support system DSS which will Ž . be used and which will improve upon the present situation. 2 A knowledge-based DSS development Ž . environment having the characteristics we propose should improve our chance of success to develop a useful application. 3 It is unlikely that such an Ž . application can support more than the most formalized part of the knowledge used in strategic management. We shall use examples taken from our experience of the software industry to illustrate this point of view.

1.2. Strategic management conceptual framework and models

## 1.2.1. Basic generic strategies

Most specialists agree that few generic strategies exist. According to Porter 12,13 , there are three<sup>w</sup> <sup>x</sup> generic strategies: cost leadership, differentiation and focus. Strategic moves such as acquisition, merger and alliances can be considered as actions to achieve one of the generic strategies. The strategy of cost leadership consists of producing at a lower cost than the competition and being able to dictate or at least strongly influence the market price. The strategy of differentiation consists of being unique in an industry along with some characteristics which are valuable to the customer providing a product with someŽ unique characteristics . The strategy of focus consists. of concentrating in order to serve a particular group of customers and tailoring the offer to their specific needs; it can be considered as a variant of the strategy of differentiation. We personally believe that the other components of the marketing mix salesŽ force, distribution and promotion are important in. strategy formulation since it is unfortunately not true that a better product can impose itself without a sufficient level and quality of marketing mix.

## 1.2.2. Strategic segments

Any strategic management must start with a correct analysis of the present strengths and weaknesses of the company. This must be done, as soon as the company reaches a certain size, by analyzing each Strategic Business Unit SBU independently. TheŽ . concept of strategic segmentation and SBU is an important idea in the literature on strategic management 12,13 . A SBU is the result of the segmenta-<sup>w</sup> <sup>x</sup> tion of the firm’s activities into strategic segments. A strategic segment is a market on which firms are competing with their products. A SBU is usually characterized by a unique combination of Key Success Factors KSFs . In other words, the concept of Ž . global market very rarely corresponds to reality. The market is made of the aggregation of more or less numerous segments. The nature of these segments and their typology depends on the nature of the products and of the consumers. There exist geographical segments where consumer behavior varies Ž according to localization , sociological segments . Žwhere consumer behavior varies according to socio-professional categories, to sex, income level, etc. , usage segments where consumption is related. Ž to characteristics of the product . In SIMAR, we. have decided to concentrate on a market where segments are based on usage.

## 1.2.3. Key success factors

A standard hypothesis is that the segment is characterized by a unique combination of KSFs. A KSF is a capacity a company must master if it wishes to be successful in a given segment. A list of each of the generic strategies has been associated by authors in this field and specialized consulting companies such as the Boston Consulting Group BCG andŽ . McKinsey.

## 1.2.4. Data needed to perform a strategic analysis

If we use as a starting point the four conceptual constructs proposed by Carlsson, we shall need to store data or observed facts concerning the compa- Ž . nies competing on the market, this will constitute the first ‘‘dimension’’ of our data. For each company, we shall have to store variables concerning the company itself and not specifically the products. For example, the variables related with the global financial structure of the company balance sheet, incomeŽ statements are of this kind; also the marketing vari-. ables related to the firm as a whole such as the company awareness on the market enter this category. Another list of variables will measure concepts, which are related to the products themselves. To this category belongs the marketing mix of each product: unit price, advertising budget, sales force associated to the product, product characteristics, as well as variables such as market share, product awareness, sales volume, production cost, inventory level, quantity of fixed assets needed to produce the product, contribution of the product to cover the firm fixed costs.The items of this second list of variables will be related to the product or SBU ‘‘dimension’’ of the database. As a consequence, two new ‘‘dimensions’’ can be identified in the data. The ‘‘variable’’ dimension and ‘‘product’’ or ‘‘SBU’’ dimension. The Fig. 1 shows a typical multidimensional structure for the data we wish to store.

Information, which is not related to a product but to the environment and the market, such as the product characteristics desired by the consumers, size of market segments, interest rate, etc., will be part of the ‘‘variable’’ dimension but related to the ‘‘time’’ dimension only.

## 1.2.5. Knowledge used in strategic management

Two kinds of knowledge are used in strategic management: quantitative knowledge or models to Ž . compute the value of certain variables, and qualitative knowledge used in reasoning about the situation from a strategic point of view. With respect to quantitative models, when one reads the literature on strategic management, it appears that a series of models is useful to compute variables which are used to evaluate part or the whole of a strategy:

![](/api/attachments/8367XY3R/fulltext/images/362d8a98db09f714f91a68df6522311fa4e4978f1de5f3acb2a468f04ca76096.jpg)  
Fig. 1. Four-dimensional ‘‘cube’’ in the simulation database.

– product portfolio model;

– marketing model;

– production model; and

– financial and fiscal models.

By portfolio models, we mean the standard model introduced by consulting firms such as the BCG growth<sup>r</sup>market-share matrix and the McKinsey market attractiveness–business strength matrix. These basic models have a number of severe limitations since they focus only on two dimensions, they lack explicit consideration of risk factors, etc. Despite these limitations, the portfolio models are useful.

By marketing model, we mean at least two kinds of models: a global market response model of the form:

$$
Q _ {t} = Q _ {\text { potential }} * \text { ENVIRONMENT } _ {t}
$$

$$
* \sum_ {\text { firms }} \text { MKT   MIX   TOT }.
$$

This model will simulate the evolution of the global market in particular as a function of the total marketing efforts of firms competing in this environment. The elements of the marketing mix are: price of product, advertising expenditures, distribution and sales force. These variables are decision variables of the firm, they have to be used by functions which are a composition of each other multiplicative effect . Ž .

A marketing mix model will be needed to explain in a way coherent with theory, for a given type of market, the breakdown of the global demand between the products on the market. In our case, we have decided to concentrate on one category of product: the fast-moving consumer goods for which more reliable quantitative models seem to exist. This model will use sub-models, as shown in Section 2.1.2.

By logistic and production model, we mean a model which will allow us to compute the cost of producing one unit of each one of the finished products during each period of analysis usually aŽ term or a year in strategic problems . Such models . are of the form:

$$
c = f \left(\mathrm{Rm} _ {t}, \mathrm{Mp} _ {t}, E _ {t}, \mathrm{Ser} _ {t}\right),
$$

where: Rm <sup>s</sup>the cost of raw material at period $t ;$ $\mathbf { M } \mathbf { p } _ { t } = \mathrm { t h e }$ cost of manpower at period $t ; ~ E _ { t } =$ the cost of energy at period $t ; \operatorname { S e r } _ { t } =$ the cost of services to the production insurance of equipment, mainte-Ž nance costs, etc. ..

This model will use as input for each product the level of production and will be related to the inventory model for computing the value of inventories. Clearly, the production function is highly dependent on the industry and the localization of the production plant. Such production functions have been defined for consumer goods as well as industrial products.

At the point where marketing and production meet, we find the problem of availability of products in stock. It is often the case that, due to a bad commercial forecast, the general conditions of the market or the efficiency of the marketing of a firm lead to a situation where the demand of a product is superior to the availability. In such a case, a procedure or model must be provided in order to allocate the residual demands to other products.

By financial models, we mean:

– a model to compute the income statement of a product and in particular its contribution to covering the firm fixed costs;

– a model to compute the income statement at the firm level; and

– a model to compute the firm’s balance sheet.

The balance sheet model implies the use of a certain number of sub-models to compute third-party accounts clients, suppliers, etc. and an equation ofŽ . uses and sources of funds.

## 2. Developing a simulation environment to experiment with strategic knowledge

We shall now describe the application SIMAR, the goal of which is to provide an environment to define and test strategic knowledge bases. As we have described in Section 2.4.3, strategic knowledge can, at least in part, be formalized using the formalism of algebraic models and the formalism of rules. The goal of the SIMAR application will be twofold. On one hand, it will be to allow teams of users to define and test strategies in a simulated competitive environment as in a strategic business game ; on the Ž . other hand, it will be to allow the formalization of knowledge bases concerning strategic knowledge in order to test how much of it can be formalized. The ultimate goal is to define a series of knowledge bases, which can cooperate with each other and use knowledge coming from models and databases to replicate the cognitive process of an intelligent strategist. In other words, the goal is to define an artificial team in a strategic business game simulation.

Such an application implies the existence of development environment allowing the formalization of quantitative as well as qualitative knowledge and the definition of applications where both types of knowledge cooperate. Fortunately, this type of environment exists and has been our own research focus for many years. The environment we have used, OPTRANS Object, is briefly defined in Section 3 and in Klein 6 . The objective of such an application<sup>w</sup> <sup>x</sup> is not to simulate a set of companies competing in a given industry. The objective is to simulate an environment, which is sufficiently realistic to allow for the formalization of some pertinent and general strategic knowledge as found in textbooks on the subject. The simulated environment should not be, however, too complex to force users to invest an amount of time to master it which would take too long and discourage them.

## 2.1. Knowledge under the form of models

As seen in Section 1.2.5, we shall need to simulate a market and firms competing in the various segments of this market through their products. We shall first define the basic marketing concepts we wish to simulate and the way our simulated market works, then we shall define the production, financial and fiscal concepts we wish to simulate.

## 2.1.1. Modeling marketing concepts

2.1.1.1. General equation of the market. The general equation of the market is of the form:

$$
\begin{array}{c} Q _ {t} = Q _ {\text { potential } _ {t _ {0}}} * \text { ENVIRONMENT } _ {t} \\ * \text { MKT   MIX   TOT } _ {t}, \end{array}
$$

where: Q <sup>s</sup>total demand to the industry period t Ž . quantity ; $Q _ { \mathrm { p o t e n t i a l } _ { t _ { 0 } } } =$ initial value of potential market; ENVIRONMENT <sup>s</sup>effect of all factors external to the industry. It is a two-variable function of the form: Ž . growth rate , seasonal coefficient .

Table 1 Computation of the elements of the transition probability matrix

<table><tr><td>t t-1</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>1</td><td> $\frac{A1 + R1}{D1}$ </td><td> $\frac{A2}{D1}$ </td><td> $\frac{A3}{D1}$ </td><td> $\frac{A4}{D1}$ </td></tr><tr><td>2</td><td> $\frac{A1}{D2}$ </td><td> $\frac{A2 + R2}{D2}$ </td><td> $\frac{A3}{D2}$ </td><td> $\frac{A4}{D2}$ </td></tr><tr><td>3</td><td> $\frac{A1}{D3}$ </td><td> $\frac{A2}{D3}$ </td><td> $\frac{A3 + R3}{D3}$ </td><td> $\frac{A4}{D3}$ </td></tr><tr><td>4</td><td> $\frac{A1}{D4}$ </td><td> $\frac{A2}{D4}$ </td><td> $\frac{A3}{D4}$ </td><td> $\frac{A4 + R4}{D4}$ </td></tr></table>

There are 12 seasonal coefficients such that:

$$
\bar {s} = \frac {1}{1 2} \sum_ {t = 1} ^ {1 2} S _ {t} = 1.
$$

The growth rate factor is of the form: $Y _ { t } = e ^ { a t }$ where a<sup>s</sup>growth rate.

MKT MIX TOT <sup>s</sup>the effect of the marketing mix of all products on the market at period t, i.e., a function of the form:

$$
\varphi \left(Q _ {\bar {p}, t}, Q _ {\bar {a}, t}, Q _ {\bar {d}, t}\right),
$$

where $Q _ { \bar { p } , t } =$ the effect of the average price, weighted by the preceding period market share, of all products on the market.

The use of the weighted average implies, that all price modifications will have an even greater effect on the level of the global market if they are coming from market-leader products.

$Q _ { \overline { { a } } , t } = \mathsf { t h e }$ effect of advertising for all products from all firms.

This regrouping of the advertising effect at the firm level implies that the allocation of the advertising resources of each firm between its products has no incidence on the global impact of advertising: the total advertising expense only is of significance.

$Q _ { \bar { d } , t } =$ the effect of the distribution effort for all products at the level of each firm. This regrouping at the firm level has the same consequence as for $Q _ { \overline { { a } } , t } .$

Practically, the MKT MIX TOT variable takes its value between 0 and 1; the ENVIRONMENT variable takes its value around 1; the real market is, as a consequence, a fraction of the potential market, this fraction varying according to the efficiency of the marketing policy of all firms.

It should be noted that the market growth rate implies increases to the initial potential market from period to period, and so generates the potential market of period t.

2.1.1.2. Equation proÕiding market allocation between the products. The global real market and not Ž the potential market at . t is allocated between the different products in proportion to the efficiency of the marketing mix of each product relatively to all others.

One makes a distinction in computing the allocation of the global Market Share MS , which has notŽ . changed from t to t<sup>y</sup>1 and the allocation of the variation from t<sup>y</sup>1 to t of the global market. <sup>1</sup>

The allocation of the invariant from t<sup>y</sup>1 to t uses a probability transition matrix <sup>w</sup> <sup>x</sup> from state t<sup>y</sup>1 to the state t of the market the Markov chainŽ of first order Table 1 . The allocation of the varia-. Ž .

tion is made through an attraction probability vector $[ \gamma ] _ { i }$ on the market variation.

Let $Q _ { t }$ be the total demand to the industry at period t to be allocated so that:

$$
Q _ {t} = \sum_ {i = 1} ^ {n} q _ {i, t} \quad i = 1, \dots , n \text { products },
$$

with $q _ { i , t }$ demand to the product i at period t, $\Delta _ { t } = { \mathcal { Q } } _ { t } ^ { \dagger } - { \mathcal { Q } } _ { t - 1 } , [ \pmb { \alpha } ] _ { t }$ transition probability matrix at t.

This matrix is square $[ \pmb { \alpha } _ { n , n } ]$ and stochastic soŽ that the sum of terms of each line equals 1 ..

$$
\sum_ {i = 1} ^ {n} \pmb {\alpha} _ {i j, t} = 1
$$

with i column subscript, j line subscript, $[ \gamma ] _ { t }$ vector of attraction probabilities of delta Ž . with:

$$
\sum_ {i = 1} ^ {n} \pmb {\gamma} _ {i, t} = 1.
$$

The demand for product i at period t is:

$$
q _ {i, t} = \sum_ {j = 1} ^ {n} \left(\boldsymbol {\alpha} _ {j i, t} q _ {j, t - 1}\right) + \boldsymbol {\gamma} _ {i, t} \Delta_ {t}.
$$

It is an allocation procedure, which is simple and robust, which also has the advantage, as it will be shown with the computation of <sup>w x</sup> and $[ \gamma ]$ to integrate important marketing concepts.

Under matrix form, the equation gives:

$$
[ \boldsymbol {q} ] _ {t} = [ \boldsymbol {q} ] _ {t - 1} [ \boldsymbol {\alpha} ] _ {t} + \Delta_ {t} [ \boldsymbol {\gamma} ] _ {t}.
$$

The product of the line vector $[ \pmb q ] _ { t - 1 }$ by the $[ \pmb { \alpha } _ { t } ]$ matrix shows, that one applies a line $[ \pmb q ]$ on a column of $[ \pmb { \alpha } _ { t } ]$ to obtain a given $q _ { i , i }$

2.1.1.3. Transition probability matrix. The diagonal elements of the matrix $\pmb { \alpha } _ { i , i }$ reflect the probability that the product i will keep its market from t to t <sup>y</sup> 1 its ‘‘state’’ ; in other words, in less rigorousŽ . but clearer terms, the percentage of its market that the product i will keep from period t <sup>y</sup> 1 to t. To obtain this result, let us define: $\pmb { \alpha } _ { i i , t }$ probability for the product i of retaining in $t ,$ its market in t <sup>y</sup> 1. The n terms $\pmb { \alpha } _ { i i }$ being the diagonal terms of <sup>w</sup> <sup>x</sup> .

Similarly, the $\left( n ^ { 2 } - n \right)$ terms which are left and which are not on the diagonal measure the percentage of the market, in $t - 1$ , of product j that the product i will attract in t.

$\pmb { \alpha } _ { j i , t }$ probability of attraction of the market of product j at t by the product i in t<sup>y</sup>1 with:

$$
\boldsymbol {\alpha} _ {i i, t} = \frac {A _ {i , t} + R _ {i , t}}{D _ {i , t}} \quad \begin{array}{l} i = 1, \ldots , n \\ j = 1, \ldots , n \end{array}
$$

<sup>=</sup>number of products,

$$
\boldsymbol {\alpha} _ {j i, t} = \frac {A _ {i , t}}{D _ {j , t}} \quad i \text {   column   subscript }, j \text {   line   subscript },
$$

with $A _ { i , t }$ base attraction factor of product i in t. $R _ { i , t }$ base retention factor of product i in t. $D _ { j , t } = R _ { j , t }$ $+ \textstyle \sum _ { j = 1 } ^ { n } A _ { j , t }$ so that the stochastic property $\begin{array} { r } { \dot { \sum _ { i = 1 } ^ { n } } \pmb { \alpha } _ { j i , t } } \end{array}$ <sup>s</sup> 1 is kept for all lines j.

One can note that:

$$
\sum_ {j = 1} ^ {n} \alpha_ {j i, t} \neq 1.
$$

This algorithm has the advantage of relying on consumer behavior hypotheses which are often verified in the domain of consumer products. In addition, it provides coherent results with the preceding marketing hypotheses, e.g., an aggressive marketing policy, which leads to a high attraction probability factor, will allow product i, to gain at t, a substantial share of the market from the other products at t <sup>y</sup> 1: $A _ { i }$ is in fact the numerator of all $\pmb { \alpha } _ { i , j }$ where:

$$
\left. \begin{array}{l} D 1 = R 1 + S \\ D 2 = R 2 + S \\ D 3 = R 3 + S \\ D 4 = R 4 + S \end{array} \right) \text {with} S = \sum_ {i = 1} ^ {n} A _ {i}.
$$

2.1.1.4. Attraction probability Õector. The element i of the line vector $\gamma _ { i , t }$ is such that — Case 1: Delta, the variation of the total demand from t<sup>y</sup>1 to t, is positive: the total market increases:

$$
\boldsymbol {\gamma} _ {i, t} = \frac {A _ {i , t}}{\sum_ {i = 1} ^ {n} A _ {i , t}}.
$$

Case 2: Delta is negative: the total market decreases:

$$
\boldsymbol {\gamma} _ {i, t} = \left(1 - \frac {A _ {i , t}}{\sum_ {i = 1} ^ {n} A _ {i , t}}\right) / (n - 1),
$$

since:

$$
\sum_ {i = 1} ^ {n} \left(1 - \frac {A _ {i , t}}{\sum_ {j = 1} ^ {n} A _ {j , t}}\right) = n - 1.
$$

It is in fact necessary that: the allocation between the n products i of the increase of the global market must be done in proportion to the attraction factor $A _ { i } .$ . The allocation of the decrease of the market must be done in inverse proportion to the $A _ { i }$ factor.

2.1.1.5. Attraction and retention factors. $A _ { i , t } \colon$ attraction factor of product i is the result of the product of two functions: first, the function describing the efficiency of the marketing mix of product i; second, the awareness function stock of goodwill of prod-Ž . uct i of the firm<sup>r</sup>brand to which it belongs:

$$
\begin{array}{r l} A _ {i, t} = & \varphi (\text { MKT   MIX } _ {i, t} * \text { AWARENESS } (\text { PROD } _ {i} \\ & + \text { FIRM / BRAND }). \end{array}
$$

The basic attraction factor will be higher in proportion to the aggressiveness of the MKT MIX. It also depends on the joint awareness of the firm<sup>r</sup>brand and the product. The existence of a favorable firm<sup>r</sup>brand awareness will help in the launching of a new product launched by this brand<sup>r</sup>firm.

$R _ { i , t } \mathrm { : }$ holding back retention factor of productŽ . i is a function of, on one hand of the market share of product i at t<sup>y</sup>1; on the other hand, of the joint awareness of the product and the firm-brand.

The idea is that a favorable experience, and as a consequence a likely durable experience, that the consumer makes of a product, linked to the strength of the firm–brand image, will improve the retention factor of this product by the consumer:

$$
\begin{array}{r l} R _ {i, t} = & \varphi (\text { MKT   SHARE } _ {i, t - 1} * \text { AWARENESS } (\text { PROD } _ {i} \\ & + \text { FIRM / BRAND }). \end{array}
$$

There is a cumulative factor upwards, which makes it easier for market leaders to maintain their own market share, provided that these market leader products have a good product and brand awareness.

2.1.1.6. The awareness and ‘‘stock of goodwill’’. The awareness equation is similar to that in the model initially proposed by Koyck. One can find a similar treatment of the long-term effect of advertising initially introduced by Palda 11 , Telser 16 and<sup>w x</sup> <sup>w x</sup> Lambin. Simar uses a ‘‘stock of goodwill’’ concept as analyzed initially by Nerlove and Arrow 8 and <sup>w</sup> <sup>x</sup> by considering the ratio of advertising efficiency of product i compared to the advertising efficiency of all other products.

FIRM<sup>P</sup>BRAND<sup>P</sup>AWARENESS RM is definedŽ . by:

$$
\mathrm{RM} _ {j, t} = \frac {Q A _ {j , t}}{\sum_ {j = 1} ^ {m} Q A _ {j , t}} + \lambda \mathrm{RM} _ {j, t - 1}
$$

$$
j = 1, \dots , m \text { firms },
$$

$Q A _ { i , t } = \mathrm { t h e }$ advertising efficiency of firm–brand j Ž . i.e., for all its products at t; <sup>s</sup> the awareness persistence rate.

PROD<sup>P</sup>AWARENESS RP : the product aware- Ž . ness is defined as:

$$
\mathrm{RP} _ {i, t} = \frac {Q A _ {i , t}}{\sum_ {i = 1} ^ {n} Q A _ {i , t}} + \lambda \mathrm{RP} _ {i, t - 1}
$$

$$
i = 1, \dots , n \text { products },
$$

$Q A _ { i , t } = \mathrm { t h e }$ advertising efficiency of product i at t. One can prove that:

$$
\begin{array}{l} \mathrm{RP} _ {i, t} = \frac {Q A _ {i , t}}{\sum_ {i = 1} ^ {n} Q A _ {i , t}} + \lambda \frac {Q A _ {i , t - 1}}{\sum_ {i = 1} ^ {n} Q A _ {i , t - 1}} \\ \qquad + \lambda^ {2} \frac {Q A _ {i , t - 2}}{\sum_ {i = 1} ^ {n} Q A _ {i , t - 2}} + \dots \\ \qquad + \lambda^ {n} \frac {Q A _ {i , t - n}}{\sum_ {i = 1} ^ {n} Q A _ {i , t - n}}. \end{array}
$$

One assumption is that is a market parameter which is the same for all products.

## 2.1.2. Effect of the marketing mix

The marketing mix effect is the result of the composition of the advertising effect, the price effect, the distribution network effect and of the market segments access factor for the product i.

$$
\mathrm{MKT} \operatorname{MIX} _ {i, t} = \varphi \left(Q A _ {i, t} * Q P _ {i, t} * Q D _ {i, t} * Q A S _ {i, t}\right).
$$

2.1.2.1. Effect of adÕertising. The effect QA of the advertising budget follows a logistic curve having:

– an efficiency threshold;

– an inflexion point; and

– an upper asymptote.

$$
Q A = \operatorname{Max} A \left(1 - \exp \left(\frac {K 1}{\text { FirmNum } ^ {2}} A ^ {2}\right)\right),
$$

where A<sup>s</sup>advertising budget; K 1<sup>s</sup>parameter; Max A<sup>s</sup>maximum of QA.

![](/api/attachments/8367XY3R/fulltext/images/11c7669d67be573dbdfbb4f3abf0fbb44f810c905cea847b8211446bafaaf482.jpg)

The advertising elasticity effect, which allows a measure of the advertising budget efficiency, is:

$$
\eta_ {\mathrm{A}} = \frac {\mathrm{d} Q A}{\mathrm{d} A} \frac {A}{Q A}.
$$

This information is available to the teams participating in the simulation; if the simulation is used as a ‘‘business game’’, it can be bought. It would be easy to add a parameter to measure the media quality, and a parameter to measure message quality. For the initial theoretical justification of this model, see Bass and Parsons 1 .<sup>w</sup> <sup>x</sup>

2.1.2.2. Price efficiency x. The effect $( Q P )$ of the price is defined as an exponential curve having a maximum of 1 when the price is zero, and going to 0 when the price goes to the infinite.

$$
Q P = \exp \left(- \frac {K 2}{\text { FirmNum }} P ^ {2}\right),
$$

where P<sup>s</sup>price; K 2<sup>s</sup>parameter.

![](/api/attachments/8367XY3R/fulltext/images/3e4905c73b0f22dc26ff24726151d15a8b71d8e8d1899e07d2f4bdeb79f172cc.jpg)

The price elasticity, which allows a measure of the efficiency of the price policy however, it is Ž necessary to remember that competition has to be taken into account is:.

$$
\eta_ {\mathrm{P}} = \frac {\mathrm{d} Q P}{\mathrm{d} P} \frac {P}{Q P}.
$$

This information is computed by the simulation and can be bought by each firm.

2.1.2.3. Distribution network effect. The distribution effect QD is defined by an exponential function: the effect is nil when D is nil, The effect is maximal when D goes to the infinite:

$$
Q D = \text { Max } D \left(1 - \exp \left(\frac {- K 3}{\text { FirmNum }} D\right)\right),
$$

where D<sup>s</sup>cost of maintaining the distribution network, i.e., unit cost of maintaining the sale force <sup>=</sup> number of salesmen; K 3<sup>s</sup>parameter; Max $D =$ maximum value of QD. We have:

$$
\eta_ {\mathrm{D}} = \frac {\mathrm{d} Q D}{\mathrm{d} D} \frac {D}{Q D}.
$$

![](/api/attachments/8367XY3R/fulltext/images/4fd38a0ac821981fe9db078d80261cb1bc956d64904d20b7c5a84b4f4daca785.jpg)

NOTA: D is not equal to the total distribution cost. To D should be added — the costs of laying salesmen off and training costs of new salesmen. The relative weight of QA, QD, $Q P$ is a function of the values of K1, K 2, K 3 as well as MAX A, MAX D. A typical set of values for these parameters is given in 14 .<sup>w</sup> <sup>x</sup>

2.1.2.4. Effect of the product characteristics: access to market segments. The market segmentation of products in the fast-moving consumers goods category simulated by SIMAR is based on the product utilization type. The market has three segments, i.e., three types of product utilization. Each product in SIMAR has a characteristic, whose value opens up to a greater or lesser degree each one of these three segments. The value given to the product characteristic thus has a differentiated effect between the different types of products.

The access factor or segment is calculated in the following way: let $K _ { i }$ be the characteristic of product i. Each of the segments 1, 2, and 3 is described by two parameters: a mean and a standard deviation.

$$
\begin{array}{l} \bar {X} 1 \text {et} \sigma 1 \\ \bar {X} 2 \text {et} \sigma 2 \\ \bar {X} 3 \text {et} \sigma 3. \end{array}
$$

For a given segment, the mean represents the characteristics of the product which are best adapted to the kind of usage this segment corresponds to:

![](/api/attachments/8367XY3R/fulltext/images/3d3f813d18371080885ef3a5aea2c8746cd464e2ce87c04ef10d5db822a09832.jpg)

Ž . 1 One computes, for a given product i, an access probability density to each segment, such that, e.g., for the segment:

$$
\left. \begin{array}{l} P 1 (i) \\ P 2 (i) \\ P 3 (i) \end{array} \right) P 1 = \left(\frac {1}{2 \pi}\right) ^ {1 / 2} \mathrm{e} ^ {- 1 / 2} \left[ \frac {\overline {{X}} 1 - K _ {i}}{\sigma 1} \right] ^ {2}.
$$

In a similar way, the computation is done for all other products of the three segments.

Ž . 2 Then one sums for each segment the following probability densities:

$$
\begin{array}{l} S 1 = \sum_ {i = 1} ^ {n} P 1 (i) \\ S 2 = \sum_ {i = 1} ^ {n} P 2 (i) \\ S 3 = \sum_ {i = 1} ^ {n} P 3 (i). \end{array}
$$

Ž . 3 Then one computes for each product i an access factor for each of the three segments:

$$
\operatorname{AC1} (i) = \frac {P 1 (i)}{S 1}
$$

$$
\mathrm{AC2} (i) = \frac {P 2 (i)}{S 2}
$$

$$
\mathrm{AC3(i)} = \frac {P 3 (i)}{S 3}
$$

The global access factor QA iŽ . to the three segments is then the sum weighted by the size of each of the segments — of these three access factors:

$$
Q A S (i) = \mathrm{AC1} (i) Q 1 + \mathrm{AC2} (i) Q 2 + \mathrm{AC3} (i) Q 3
$$

so that $Q 1 + Q 2 + Q 3 = 1 \qquad $

Example of interpretation. The product type we consider is a detergent — let us consider three types of usage of this detergent Table 2 . Ž .

It suffices to define $K _ { i }$ as a continuous scalar variable so that, e.g., $X 1 = 1 0$ $X 2 = 2 0$ 44 $X 3 = 3 0$ et.. $\sigma = 4 . \ ^ { 2 }$ 2

The differentiation between products exists. However, substitutions are possible, which is why the use of normal law probability density enables one to evaluate the penetration of a product with the characteristic $K _ { i }$ to be made in each of the segments as a function of the penetration of others products.

Long-term effect. The equation is defined so that the greater the number of products on the market, the more the QAS iŽ . factor will decrease for each product.

The QAS factor appears in the equation, giving the base attraction factor, so that the attraction factors decrease relative to the retention factors of products which are not affected by the progressive decrease of QAS.

As a consequence, it will be more and more difficult for a new product to gain market share on the leading products of the market: this is what is happening on fast-moving consumer goods with a weak technological content. Thus, this is a second method to reinforce the effect of market share strategy.

## 2.1.3. Logistic simulation: supply, production and inÕentory management

The simulation of this function is based on the following assumptions: 1 one type of raw material Ž . is used for all products; 2 each product uses the Ž . same quantity of raw materials; 3 orders of raw Ž . materials are decided at the firm level and are delivered with one period lag time; 4 if the inventory ofŽ . raw materials are not sufficient for the planned production, the model will automatically issue a special order. Raw materials on special order are more costly. This extra cost is allocated to the purchase cost of raw materials for that period.

Table 2  
Market type by segment

<table><tr><td></td><td>Market type</td><td>Product characteristics</td></tr><tr><td>Segment 1</td><td>heavy wash</td><td>high cleaning power</td></tr><tr><td>Segment 2</td><td>washing machine</td><td>average cleaning power, no foam</td></tr><tr><td>Segment 3</td><td>light wash, hands, utensils washing</td><td>foam, special hand protection, low cleaning power</td></tr></table>

To the joint between the marketing and production function, one finds the problem of the inventory availability of the product. It is often the case, following a bad sale forecast, that the general conditions of the market or the relative efficiency of the marketing of a company creates a demand which is superior to the quantity of the product available.

$$
\text { demand } _ {i, t} > \text { available } _ {i, t}
$$

$$
\text { with   available } _ {i, t} = \text { production } _ {i, t} + \text { inventory } _ {i, t}.
$$

The rule, which is adopted, is then the following.

Whatever the efficiency of the marketing mix, the sales of the firm will be equal to the quantity of the product available. The remaining quantity, i.e., demand $\mathbf { \Phi } _ { i , t } - \mathbf { a v a i l a b l e } _ { i , t }$ will be allocated between all the other firms having still some product available $\left( \mathrm { a v a i l a b l e } _ { i , t } > \right)$ demand $\mathbf { \Phi } _ { i _ { j , t } } , \mathbf { \Phi } _ { j } = 1 , \ldots , n )$ to the pro rata of the efficiency of their marketing mix. If all or a part of the remaining quantity cannot be reallocated due to a lack of product of the other firms, it will show under the heading: ‘‘Non-satisfied demand’’. This rule is justified by the classical substitution phenomenon. In case of non-availability of product i from firm j at the sale point, the consumer will buy the product k of firm l, which will be available and will have his preference. For a complete description of the model, the reader is referred to the SIMAR methodological manual 14 . <sup>w</sup> <sup>x</sup>

## 2.1.4. Financial simulation

SIMAR simulates the computation of the products income statements, as well as the income statement, the balance sheet and the cash position of the firm.

Table 4 Company income statement  
Table 3 Product income statement

<table><tr><td>Sales</td><td>Quantity  $sold_t$ *Unit  $price_t$ </td></tr><tr><td>- Inventory variation</td><td>Possible FP inventory value reduction</td></tr><tr><td>- Production Costs</td><td>Period cost of production</td></tr><tr><td>- Cost of raw materials consumed</td><td>Period cost of raw materials consumed</td></tr><tr><td>= Gross margin</td><td></td></tr><tr><td>- Advertising costs</td><td>Decision</td></tr><tr><td>- Selling costs</td><td>Nb  $Salemen_t$ *MeanSalSaleman $_t$ + Nb Hires*UnitCtHire $_t$ + NbSalFired*UnitCtFire $_t$ </td></tr><tr><td>- Finished products inventory costs</td><td>FPQty $_t$ *UnitInvCtFP $_t$ </td></tr><tr><td>- Depreciation allowance</td><td>Fixed  $Assets_{t-1}$ *RateOfDepAssets $_t$ </td></tr><tr><td>- Other operating expenses</td><td>Sum of four previous accounts</td></tr><tr><td>= Contribution</td><td>Contribution of the product to the company</td></tr></table>

The variables used in these models are presented in the corresponding reports described in Section 2.2. The consequences of the various delays of payments on the cash position of the firm are modeled.

The financing of the firm can be made through increase in equity capital or long-term debt. A dividend policy can be defined. At the time of writing of this article, the fundamental problem of the share value has not been modeled. The classical valuation models, which use the stream future dividends, the P<sup>r</sup>E ratio or the CAPM could be used.

## 2.1.5. Fiscal simulation

The present model uses the standard rules concerning the company income tax. The income tax rate is one of the parameters of the simulation. The present model uses the French rules for the payment of the income tax. These rules can be easily changed. For a complete description of the financial and fiscal modeling, the reader is referred to the SIMAR methodological manual 14 . <sup>w</sup> <sup>x</sup>

## 2.2. Reports to present Õarious results of the simulation

The application provides several reports to present fundamental information needed to evaluate strategies. These reports concern the market, the products, the products income statements, the company income statement, balance sheet and use and source of fund statement. These reports also synthesize information on all products and on all firms on the market for any period of time of the simulation.

<table><tr><td>Sales</td><td>Sum of sales of all products of the company</td></tr><tr><td>- Inventory variation</td><td>Possible RM and FP inventory variation</td></tr><tr><td>- Production costs</td><td>Sum of the period production costs for all the products of the company</td></tr><tr><td>- RM purchase costs</td><td>Sum of RM purchase costs for all the products of the company + possible special RM purchase costs.</td></tr><tr><td>= Gross margin</td><td></td></tr><tr><td>Marketing research costs</td><td>Decision</td></tr><tr><td>Advertising costs</td><td>Sum of advertising costs over all company products</td></tr><tr><td>Selling costs</td><td>Sum of selling costs over all products + cost of laying off personnel</td></tr><tr><td>Storage costs of RM</td><td> $QtyStkRM_t *InvCtRM_t$ </td></tr><tr><td>Storage costs of FP</td><td>Sum of storage costs of all company products</td></tr><tr><td>Depreciation allowance</td><td>Sum of depreciation allowance over all products&#x27; production assets</td></tr><tr><td>= Other operating expenses</td><td>Sum of the six above accounts</td></tr><tr><td>= Operating income before interest and taxes</td><td>Gross margin — other operating expenses</td></tr><tr><td>- Interest income</td><td>If  $Cash_t > 0$ , then  $Cash_t *TermIntRate_t$ , else 0</td></tr><tr><td>- Interest on LTD</td><td>Sum of interests paid on the company LT loans</td></tr><tr><td>- Interest on overdraft</td><td>If  $Cash_t < 0$ , then  $Cash_t *OverdraftIntRate_t$ , else 0</td></tr><tr><td>= Financial income / loss</td><td></td></tr><tr><td>= Term income (before tax)</td><td>Operating income before interest and tax + financial profit</td></tr></table>

Table 5  
Balance sheet, asset side

<table><tr><td colspan="2">Balance sheet, asset side</td></tr><tr><td>Fixed assets net of accumulated allowance for depreciation</td><td> $Assets_t = Assets_{t-1} + investment_{t-1} - depreciation_t$ </td></tr><tr><td>Raw material inventory</td><td></td></tr><tr><td>Finished products inventory</td><td>Sum of finished products on all products of the firm</td></tr><tr><td>State income tax account receivable</td><td></td></tr><tr><td>Accounts receivable (clients)</td><td></td></tr><tr><td>Bank and marketable securities = Total assets</td><td></td></tr></table>

## 2.2.1. Quarterly reports

The term reports concern the products income statement, the company income statement, the company balance sheet and funds flow statements. To provide the reader with a feeling about the level of aggregation of the variables of these documents, we give their structure below:

Product income statement Table 3 ;Ž .

Company income statement Table 4 ;Ž .

Balance sheet, asset side Table 5 ;Ž .

Balance sheet, liabilities side Table 6 ; andŽ .

Funds flow statement Table 7 .Ž .

2.2.1.1. Computing the cash position of the company. The equilibrium of the balance sheet is maintained through the cash flow equation. The computation of the cash position is computed in several steps: before the computation of the full aggregated income statement, one computes the cash position:

Table 6  
Balance sheet, liabilities side

<table><tr><td>Capital</td><td> $Capital_{t} = capital_{t-1} + increase in capital_{t}$ </td></tr><tr><td>Net profit of the period</td><td></td></tr><tr><td> $Retained earnings_{t-1}$ </td><td>Retained earnings preceding period</td></tr><tr><td>(− Dividends paid)</td><td></td></tr><tr><td>LTD</td><td>Sum of all LT loans of the firm</td></tr><tr><td>Income tax due</td><td></td></tr><tr><td>Suppliers</td><td></td></tr><tr><td>Overdraft</td><td></td></tr><tr><td>= Total liabilities</td><td></td></tr></table>

Table 7  
Fund flow statement

<table><tr><td>Investment</td><td>Decision</td></tr><tr><td>Increase in inventory</td><td>Increase in total inventory value (RM and FP)</td></tr><tr><td>Reimbursement of overdraft</td><td></td></tr><tr><td>Reimbursement of LTD</td><td>Reimbursement of capital of loans</td></tr><tr><td>Increase of income tax</td><td></td></tr><tr><td>Decrease of fiscal debt</td><td></td></tr><tr><td>Increase of clients receivables</td><td></td></tr><tr><td>Decrease of suppliers liability</td><td></td></tr><tr><td>Dividend paid</td><td></td></tr><tr><td>Cash</td><td></td></tr><tr><td>= Total uses of funds</td><td></td></tr><tr><td>Cash preceding term</td><td></td></tr><tr><td>Result</td><td></td></tr><tr><td>Depreciation allowance</td><td></td></tr><tr><td>Decrease of inventory value</td><td>Decrease in total inventory value (RM and FP)</td></tr><tr><td>Increase in capital</td><td></td></tr><tr><td>New LTD</td><td></td></tr><tr><td>Overdraft</td><td></td></tr><tr><td>Decrease of income tax debt</td><td></td></tr><tr><td>Increase of income tax debt</td><td></td></tr><tr><td>Decrease of clients receivable</td><td></td></tr><tr><td>Increase of suppliers</td><td></td></tr><tr><td>= Total sources of funds</td><td></td></tr></table>

$$
\begin{array}{l} \text {Cash} _ {t} = \text {Cash} _ {t - 1} + (\text {New LTD} _ {t} + \text {Increase in K} _ {t} \\ \quad + \text {Clients payments} _ {t} + \text {Interests income} _ {t} \\ \quad + \text {Taxes reimbursement} _ {t}) \\ \quad - (\text {Supplier's payments} _ {t} \\ \quad + \text {Advertising expenses} _ {t} \\ \quad + \text {FP Inventory Ct} _ {t} + \text {RM Inventory Ct} _ {t} \\ \quad + \text {Production Ct} _ {t} + \text {Interests on overdraft} _ {t} \\ \quad + \text {Investment} _ {t} + \text {LTD repayment} _ {t} \\ \quad + \text {Dividends} _ {t} + \text {Taxes} _ {t}), \end{array}
$$

if Cash <sup>)</sup>0, one activates a reimbursement procedure if overdraft exists; if $\mathrm { C a s h } _ { t } < 0 .$ , one activates an overdraft procedure.

Decision rules with respect to cash.

Ž .a The cash account is never negative on the balance sheet; a negative cash account will be set to zero and the negative amount will be converted into an overdraft of the same amount.

Ž . b If an overdraft exists, any positive cash will be used to reduce the overdraft under the assumption that rule a is always applied.Ž .

Ž .c When there is an overdraft, additional interest on the overdraft is computed, which adds itself to the possible current interests on LTD and will be reducing the profit of the year.

Ž .d The overdraft covers the negative cash and the additional overdraft which will be created by additional interests.

Formally, if Cash $_ t > 0$ , then reimbursement of the overdraft occurs.

Total reimbursement:

$$
\mathrm{Cash} _ {t} > \text { Overdraft } _ {t} \Rightarrow \mathrm{Cash} _ {t} = \mathrm{Cash} _ {t} - \text { Overdraft } _ {t - 1}
$$

$$
\text { Overdraft } _ {t} = 0.
$$

Partial reimbursement:

Overdraft <sup>)</sup>Cash

$$
\Rightarrow \text { Overdraft } _ {t} = \text { Overdraft } _ {t - 1} - \text { Cash } _ {t},
$$

Cash <sup>s</sup>0. <sub>t</sub>

If Cash $_ t < 0 ,$ , then new interest is computed, with CI )abs Cash Ž . <sup>s</sup> additional interests.

## 2.2.2. Annual reports

The annual report is made of the company income statement and the company balance sheet as shown on Section 2.2.

## 2.3. Graphics

The graphics available are dealing with product as well as company information.

Since the development environment used provides a report generator and that all information decision,Ž parameters and results of the simulation are stored. in a database, any kind of standard graphics can be generated. Special kinds of graphical presentation for strategic analysis of product positioning are available as shown on Fig. 2. The user can select which variables he wishes to display on the X and Y axes and which variable is proportional to the circle radius.

## 2.4. Strategic knowledge

We shall now outline the qualitative knowledge, which we need to formalize to be able to make a strategic analysis. We have seen that this knowledge can be broken down into at least four domains: financial, market analysis and product performance, production performance, human resources and strategic analysis.

Financial knowledge is necessary to diagnose the financial situation and resources of a firm. It must be possible to assess the financial solidity of a company, its financial structure, the level of return on assets and return on equity it has generated up to the present time, and its capacity to bring together new financial resources for further development.

Product and marketing knowledge is necessary to diagnose the main characteristics of the firm products margin, contribution to cover fixed costs, mar-Ž ket share, etc. and their positioning compared to . competitors’ products. This knowledge should allow one to ascertain whether the present products match to the market needs and whether they are competitive. In other words, should the company keep its present products, increase the production capacity of some of them, abandon some products, or put new ones on the market? Finally, what are the desired characteristics of new products and what resources are needed to launch them successfully?

Production performance knowledge is necessary to evaluate the order of raw material policy, production level decisions, unit costs of the firm’s products. This knowledge is also needed to diagnose the ability of the firm to develop a strategy based on cost advantage, etc.

Human resources and strategic knowledge are necessary to assess whether the adequate management skills are available to implement the development of a strategic plan.

## 2.4.1. Financial diagnosis

In the financial diagnosis Knowledge Base KB ,Ž . we are planning to use the following basic concepts:

– product return on fixed assets;

– product contribution to cover the company fixed costs;

# E

![](/api/attachments/8367XY3R/fulltext/images/98dd79bf61610d77e76e6125347998d2d8252b28f5086b667b516fd5e6f7c2f7.jpg)  
Fig. 2. Graphical representation for product positioning analysis.

– company overall return on fixed assets and company return on equity;

– cost of equity capital and cost of long-term debt;

– average cost of capital; and

– company LT borrowing capacity and company overdraft capacity.

An example of a possible financial diagnosis generated by the financial KB is given below Fig. 3 . Ž .

Product performance analysis: in the marketing knowledge bases we are planning to use the following concepts:

– product volume of sales;

– product adequation with the market expected characteristic;

– product market share;

– product contribution to cover fixed costs of production;

– product return on fixed product production assets;

– product present phase in the product life cycle; – product awareness, company awareness;

– product elasticity with respect to price, advertising budget and sales force;

– product position with respect to competition on the same segment; and

– company line of product;

An example of a possible product performance analysis produced by the marketing knowledge base is presented below Fig. 4 . Ž .

<table><tr><td>Financial diagnosis for company SEDIL at period 8 (4T 1998)</td></tr><tr><td>The company SEDIL has been profitable since 1T 1998. Retained earnings have increased from 500 to 7400. The company&#x27;s overall annual return on fixed assets for 1998 is 18%. The average return on fixed assets, since the beginning of the simulation, has been 17%. The annual return on equity for 1998 is 12%. The average return on equity, since the beginning of the simulation, has been of 10%. The company has two loans outstanding. The interest on the last company LT loan is 9% and the average cost of LTD is 11%. The ratio of debt to total assets is 30.6%. The average cost of capital is 10.30%.</td></tr></table>

Fig. 3. Example of a financial diagnosis.

<table><tr><td>2.4.2. Production performance analysisThe production and supply diagnosis knowledgebase we are planning uses the following concepts:– period volume of production;</td><td>– variation of the volume of production from preceding period;– period maximum level of production without extra costs;</td></tr></table>

<table><tr><td>Product performance analysis for the company SEDIL at period 8 (4T 1998)</td></tr><tr><td>The company SEDIL has two products. The first product SEDIL.Product1 has been marketed since the beginning of the simulation. The second product has been on the market since 4T 1997. SEDIL.Product1 has a volume of sales of 216000 and a return on fixed assets of -7.5 %. The return is measured using the contribution generated over the product life as of today.Product 2 has a volume of sales of 318000 and a return on fixed assets of 38 % since its launching at period 4T 1997. Product one has a cumulative contribution of -1500. Product2 has a cumulative contribution of 3900 and its contribution covers 63 % of the fixed cost of production for 1998.The market share of product1 has decreased from 20 to 10 %, the market share of Product2 has increased from 0 to 12 %. The sales of product1 have decreased of 35000 to 20000 (decrease of - 42%) and the sales of product2 have increased from 0 to 20000 units.Product1 awareness has increased from 0.62 to 0.68. Product2 awareness has increased from 0 to 0.07. The firm awareness has moved from 0.62 to 0.75. The evolution of the product positioning is presented below. The y axis representing the market share and the x axis the return, the circle radius being proportional to the sales volume</td></tr></table>

Fig. 4. Example of product performance analysis.

– period unit cost of production;

– weighted average cost of raw material;

– period cost of raw materials;

– level of special order of raw material; and

– unit weighted average cost of finished products.

An example of a possible diagnosis of the production function is given below Fig. 5 .Ž .

## 2.4.3. Strategic analysis

A first prototype strategic analysis knowledge base has been defined. The goal of this first strategic analysis knowledge base will be limited to the decision to abandon an existing product or to launch a new product. The concepts used by this knowledge base are the following:

– product positioning what are the product char-Ž acteristics vs. the market expectation ;.

– competitive position of the product existence ofŽ competing products on the same segments with better or similar characteristics ;.

– potential of the market segment; and

– comparative analysis of the marketing mix threeŽ other elements of the marketing mix ..

The line of reasoning, which is followed, is roughly the following.

A first rule sub-set is trying to identify if, at a given period, each product must be abandoned. It is the case if the product cannot provide any positive contribution because: 1 the product characteristic is Ž . too far from the market expectation; 2 the productŽ . characteristic is too far from the market expectation and other competitive products with better characteristics are present on the same segment; 3 the Ž . product characteristic is not too far from market expectation and the product is in competition with other products on the same segments with similar characteristics and the firm lacks the resources to improve the marketing mix; 4 the product charac-Ž . teristic is not far from the market expectation but the segment size is getting too small and the product is in competition on the same segment with the other products with a good marketing mix.

Some of these rules imply to be able to evaluate if the firm can acquire financial resources borrowing,Ž increase in equity capital at a cost which is lower. than the expected return of the product. As can be noticed, some of these rules will imply the computation of a projected product income statement. It is clear that the projected product income statement will be influenced by the competitors decisions. There is no attempt as of today to formalize the knowledge related with the selection of adequate human resources for management, production and R&D.

## 2.5. Structure of the SIMAR multidimensional database

The SIMAR application has been designed so that the totality of information used or generated during the simulation is stored in a database for further analysis. This information concerns the simulation parameters, the firms decisions, the simulation results, etc. The database used by OPTRANS is of a multidimensional structure. This means that the entry points to the data are based on the characteristics of the data themselves and will allow users to explore and view the data easily. Dimensions represent the keys associated with individual attributes in the data

## Production performance analysis for company SEDIL at period 8 (4T 1998)

The volume of production has increased from 35000 units to 49000 units. The maximum production capacity without extra hours has moved from 20000 units to 49000 units

The unit cost of production has moved from a minimum of 1.690 to a maximum of 1.949. The production has needed supplementary hours (overtime)

Fig. 5. Example of production performance analysis.

model. The following multidimensional structure has been adopted for the SIMAR application.

## 2.5.1. The dimensions used and their structure

2.5.1.1. Dimension 1. The name of this dimension is: Companies. This dimension is never modified, it contains the Firm names. The firms effectively used in the simulation belongs to the group of items ‘‘TheCompanies’’, which is created at the initialization phase.

2.5.1.2. Dimension 2. The name of this dimension is: Time. This dimension contains the time items. The first item is always called initial, it corresponds to the fourth term of the year preceding the first simulated year.

Starting from the choice of the first year in the initialization phase, the application creates the number of items corresponding to the terms of the years selected for simulation. The terms of the years corresponding to the number of periods of the simulation belongs to the group of items ‘‘ThePeriods’’. Similarly, there exists the group ‘‘TheYears’’.

2.5.1.3. Dimension 3. The name of this dimension is: Products. This dimension holds the names of the products; it is modified during the simulation as products are created and suppressed. The products are grouped by firm and in the chronological order of their creation. They belong to the group of items ‘‘products’’.

2.5.1.4. Dimension 5. The name of this dimension is: Loans. At the initialization stage, this dimension holds five empty groups: Emp\_Firm 1, Emp\_Firm 2, etc. During the simulation, the loans are created with names such that Loan1.2, which corresponds to the second Loan of Firm 1. The items are ranked in the following order:

Loan\_Firm1

## 2.6. User interface of the simulation enÕironment

## 2.5.2. List of Õariables of dimension 4

2.5.1.5. Dimension 4. The name of this dimension is: Variables. This is the dimension one has to know in order to find the right values of the model variables. A priori, each of the items of this dimension corresponds to a model variable or parameter. As far as possible, the order of model variable in the list of variables of the application is the same as that of the items in the ‘‘variable’’ dimension.

Fig. 6 shows the main window of the SIMAR application. The menu of the main window gives access to the following functions:

– file load Ž . <sup>r</sup>new<sup>r</sup>end : to manage the back-up files in case several simulations are run;

The list of variable is available in the SIMAR methodological manual 14 . The number of vari-<sup>w</sup> <sup>x</sup> ables is at present 184 but this number is increasing as new concepts are added to perform diagnosis using knowledge bases. Most of these concepts are derived from these 184 elementary concepts.

– parameter: to change the value of parameter for a simulation period;

– simulation periodŽ . <sup>r</sup>decisions<sup>r</sup>financing<sup>r</sup>run ; – edition.

<sup>q</sup>Loan1.1

Loan\_Firm2

The ‘‘simulation’’ command allows to run a period of the simulation a quarter . It is this commandŽ . which will be extended to make clear which firm will have its decisions simulated using a knowledge base. The ‘‘Print’’ command has three sub-options: for selecting the quarter, for selecting the report to be printed or displayed, for selecting the destination of the report screen, file, printer . The reports are Ž . classified between:

– quarterly reports;

Loan\_Firm3

<sup>q</sup>Loan2.1

– annual report;

<sup>q</sup>Loan2.2

– synthetic reports; and

– expert diagnosis.

The ‘‘expert diagnosis’’ option will provide the diagnosis of the company based on:

– the financial knowledge base;

– the sales and marketing knowledge base;

## 5 E H R

![](/api/attachments/8367XY3R/fulltext/images/d1439bb425d36acdcc233d65cc7fbba5dd678961b6424b118238b34038784747.jpg)  
Fig. 6. Main windows of the SIMAR application.

– the production knowledge base; and – the global strategic knowledge base.

## 2.7. Experiment with the system

## 2.7.1. Versions of SIMAR aÕailable

Several versions of the SIMAR application exist. One version has a simplified sub-model for the financial and fiscal function and a simplified submodel for the production and supply chain function. The simplified version simulates time periods, which can be a month, a quarter or a year. The full version simulates time periods of a quarter. The first phase of tests is currently checking the correction of the formalization of the quantitative models in the OP-TRANS algebraic language. Several simulations have been carried out successfully. A version of SIMAR has been developed to allow it to be used by distributed users on a local area network. This version is currently being tested. The ultimate goal is to extend its usage to INTERNET. All the simulations as of today have been made using decision made by teams of students. The knowledge bases are being defined so as to support the analysis of simulated company performance with respect to financial, marketing and production functions. A first prototype of a strategic knowledge base has been defined. It is at present limited to the decision to abandon or to launch a product.

## 2.7.2. Simulation of strategies

The financial return from strategic actions taken for fast-moving consumer goods cannot be computed by a static analysis and computation in a certainty world. It can only be evaluated in a dynamic context: the one of competition. It is therefore necessary to design a relevant strategy, which will provide the rules to make the necessary decisions at each quarter in this dynamic context. These decisions concern:

– which products are abandoned, and

– which product are launched.

In case of product abandon or launch, the reallocation of the fixed assets and the sales force.

For each product:

– the level of investment;

– the lay off of salesmen;

– the hiring of salesmen;

– the advertising budget;

– the unit price of the product;

– the characteristic of the product; and

– the production level.

For the company:

– the purchase of raw materials;

– the request for a new long-term loan amount,Ž duration ;.

– the issue of new equity capital number of Ž share, issue price ;.

– the dividend distribution rate; and

– the purchase of information list of requested Ž information ..

2.7.2.1. Competition. Competition is present at all levels of the marketing mix. Competition is the more to be feared for consumer goods with a weak technological component and with little innovation. From a static point of view, this means that the components of the marketing mix of a firm, in particular saturation effects, are directly linked to the efficiency of the marketing mix of the other firms it is competing with. An advertising budget and a distribution policy, which are efficient in a given context, can be inefficient in another one. From a dynamical point of view, the definition of the marketing mix will be the consequence of a series of actions and reactions with cumulative factor downwards or upwards over several periods. The example of ‘‘price battle’’ comes readily to mind.

2.7.2.2. Strategies. They are numerous and their determination is a function of a large set of factors. Some marketing concepts can help define them.

– the concept of market share.

A ‘‘market leader’’ product has a certain number of advantages, among which is a greater product awareness and the benefits it derives from consumer habits market inertia . A ‘‘market leader’’ productŽ . can, as a consequence, have the priority objective of retaining its own market, rather than attracting the market of other products. A new product<sup>r</sup>brand must, on the contrary, have an aggressive strategy, which is difficult and costly to implement. A possible strategy can be, as soon as a new market segment is appearing, to obtain a substantial part of it through important advertising investments to ‘‘create’’ the awareness of the brand<sup>r</sup>product. Another is to bet on a low price and to obtain a good margin by reducing advertising and distribution costs, so avoiding the consequences of decreasing financial returns. A third can be, by rapid adjustments of the product marketing mix, to take advantage of a slow reaction of competitors: the ‘‘strike method’’.

A frequent strategy is to identify a ‘‘forgotten’’ market segment which has been overlooked by competitors and then to launch a product on this segment, taking advantage of minimum cost and a better match between product-characteristic and market segment.

Another classical strategy is to develop a full line of products, and to be present on all segments. The advantage of this strategy, which can be considerable, is nevertheless reduced by the ‘‘cannibalization’’ effects of a product line. Products from the same company, which occupy all the segments of a market, compete against each other more than if they were only present on the two extreme segments of the same market.

## 3. Knowledge-based-DSS development environment used: OPTRANS Object

OPTRANS Object is the result of a research effort undertaken to solve some of the problems which were described in the NATO Advanced Study Institute on DSS. During this Summer School held at Il Ciocco Italy in 1990, an analysis of the first gener-Ž . ation KB-DSS development environment was made and research directions were discussed cf. 19 . TheŽ <sup>w</sup> <sup>x</sup>. basic hypothesis taken in this work is that the development environment should be defined as a tool to formalize different kinds of knowledge needed to implement a solution. This knowledge concerns the definition of:

– application user interface;

– quantitative models used to compute decision criteria;

– qualitative knowledge, used to simulate reasoning and provide automatic explanation of conclusions;

– presentation of information, to facilitate understanding and problem recognition; and

– data, used by models and facts used in reasoning.

Preliminary results concerning OPTRANS object were described in Klein and Traunmuller 4 and¨ <sup>w</sup> <sup>x</sup> Klein 5 . In the conceptual framework proposed <sup>w</sup> <sup>x</sup> here, the term KB-DSS application in short applica- Ž tion covers two concepts:.

– a general concept, and

– a technical concept.

In a general sense, an application is the set of software objects which is jointly used to support the solution of a decision class when interacting with a user. In a technical sense, an application is the software object which will put together the instructions relating the software objects of the same application.

In OPTRANS, an application is built from six main interrelating objects Fig. 7 :Ž .

– the application itself in its technical sense : the Ž . instructions of the application define the user interface and the global logic of the application;

– a common data structure which is used to exchange information between objects;

– the models which are used to formalise quantitative relations between the data;

– the reports which are used to define the presentation of information;

– the experts which are used to formalise qualitative knowledge; and

– the databases which are used to define and query more complex data which will be used by the application.

In fact, the situation is more complex and it is not always possible with OPTRANS to have computation only localised to models. This is the case when, e.g., the user wishes to use variables with multiple indexes. The sales figure of a product for period t and firm f will naturally be indexed by time, product and company. Some algebraic languages allow multiple index variables, such as SML 3 or DIA-<sup>w</sup> <sup>x</sup> DEM 10 , but these systems do not provide the <sup>w</sup> <sup>x</sup> knowledge base and database component which OP-

![](/api/attachments/8367XY3R/fulltext/images/5eb9a6f8353de32b1e0757ec51acdb41ea2d0c67300766dbc11077cbcb138dc6.jpg)  
Fig. 7. The main components of a KB-DSS application designed with OPTRANS.

TRANS provides. This approach, which is based on a limited number of conceptual objects used in KB-DSS, leads to the design of structured applications. It also provides applications where data capture, computation and presentation of information are to a large extent independent. This characteristic is essential, since it is the key to easy changes in the application according to the user’s needs. As can be seen, OPTRANS takes an approach, which is fundamentally different from the spreadsheet, where the same grid of cells is used to store data, formulas and define the presentation of information. With OP-TRANS, the applications data are structured into two subsets, namely a table and a list, as shown in Fig. 8. The table is used for variables with multiple occurrences and the list for variables with only one occurrence.

Line labels denote lines of the table and column headers denote columns. Variables denote a variable with only one occurrence.

An OPTRANS application uses a certain number of resources which exchange information between themselves. By resources, we mean user-defined objects<sup>q</sup>system-provided algorithms associated with the object class. The resources are the following.

## 3.1. Models

The models are conceptual objects formalizing user-knowledge concerning quantitative relations between variables with single or multiple occurrence .Ž . They are associated with algorithms called solvers.

The role of solvers is to compute values of variables, which are not known. In OPTRANS the models, variables can be indexed. However, as of today, only one index can be used. As a consequence, some computations cannot be done at the model level and are done at the database or interface level.

## 3.2. Reports

The reports are conceptual objects defining a presentation of information. A report, in the general case, is made up of text interspersed with data, tables, graphics and images. These objects are placed on the report page directly by the user. The algorithms associated with a report are display and printing routines, standard text editor algorithms cut,Ž paste, search, etc. . SIMAR uses reports to present. the product income statement, the company income statement and balance sheets, as well as numerous other company and market documents to analyze the results of the simulation.

## 3.3. Experts or knowledge bases

The knowledge bases KB are conceptual objectsŽ . used to represent a user-qualitative knowledge on a domain of expertise. The formalism will include a syntax to define facts, scale, rules, etc. To a knowledge base are associated algorithms to simulate reasoning inference, analogy, etc. and explanation. Ž .

![](/api/attachments/8367XY3R/fulltext/images/6a724183620a9e25d9f96bad731a139a3c34cb445fc54987fd901a9f81c0b9a6.jpg)  
Fig. 8. Structure of the application data in OPTRANS.

We give below an example of a rule taken out of the SIMAR prototype strategic KB:

IF Product Characteristic

<sup>s</sup>bad AND ' Competing Product With Better

Characteristics

AND Segment Potential<sup>s</sup> Ž .mean OR bad

THEN Product Status<sup>s</sup>abandon.

## 3.4. Databases

The databases are conceptual objects, which use a formalism to represent data models. The algorithms associated with the databases are related to two basic database functions: data structure definition and database query. OPTRANS is using a data model called multidimensional, which has been in use for a long time for DSS applications. The advantage of this data model is that it gives the user as entry points the characteristics of the data themselves: dimensions represent the keys associated with individual attributes in the data model. The reader interested to understand the advantages of this model for DSS databases is referred to Weldon 17 , Stein and<sup>w</sup> <sup>x</sup> Dhar 15 for a presentation of this data model.<sup>w</sup> <sup>x</sup> SIMAR uses a five-dimensional database, which is briefly described in Section 2.4.

## 3.5. Database models

The database models are conceptual objects formalizing user-knowledge concerning quantitative relations between attributes of objects. They are models, which use information from the database without first extracting it and transferring it from the database to the application file. They are equivalent to stored procedures in a relational DBMS. For example, a database model can be used to compute statistics regarding a large number of companies included in the database. The application might be a credit evaluation system working with a particular company data and using statistics computed on all companies of the same industrial sector.

## 3.6. Hypertext files

A hypertext file is a software object, which can include marked words anchors . A hypertext is asso-Ž . ciated with algorithms such as a hypertext engine able to consult the information in hypertext mode moving from a text to the text associated with a marked word.

## 3.7. Communication between resources

As a consequence of the OPTRANS structure, an application can use a knowledge base, the rules of which employ variables of a model. The conclusion of a reasoning sequence can be communicated to the application. One application can request data, which are attributes of objects in the database, etc. For more details on OPTRANS Object, the reader is referred to the OPTRANS user manual 9 . For a<sup>w</sup> <sup>x</sup> brief description, with an example of the expert component, the reader is referred to Klein 6 . For an<sup>w</sup> <sup>x</sup> example of the use of the modeling component, the reader is referred to Klein and Grubbstrom 7 .<sup>w</sup> <sup>x</sup>

## 4. Structure of the SIMAR application

The structure of the SIMAR application is best explained by Fig. 9. As can be seen from this figure, SIMAR is using a library of models, a library of reports, a library of knowledge bases KB , and aŽ . library of files used by the hypertext engine. The application shares a common data structure.

This structure is derived from OPTRANS and is the consequence of the objects used in OPTRANS to build an application as explained in Section 3. The computations are done in models. For example, different models are used to compute: product income statement, company income statements, firm production cost, firm storage costs, loan repayment schedule, etc.

Thirteen models are used in the application. However computations corresponding to aggregates sums Ž of variables on products and on firms are presently . done at the interface level. Three prototype knowledge bases are used: one for the financial diagnosis, one for the commercial and marketing diagnosis and one for the production and supply chain diagnosis. A certain knowledge base will be defined for defining a strategy for:

![](/api/attachments/8367XY3R/fulltext/images/b2c1a2b2c024e8a39b413e26fa964ce791c9311f498ea9470ae5d73440769dbd.jpg)  
Fig. 9. Structure of the SIMAR application.

– product abandoning;

– increase in production capacity; and

– product positioning and launching.

The hypertext engine is presently only used for the assistance to the system. The common data structure is used to exchange information between the resources. For example, the concluded facts of the financial diagnosis KB, the marketing KB and the production and supply chain KB are stored in this structure. The strategic KB will then read in this structure the facts needed for its own functioning.

The structure of the application is in fact more complex since the application, in its technical sense, is broken down in several modules. A module is a logical unit, which can itself use models, reports and knowledge bases. However, the common data structure list of labels, headings and variables staysŽ . common to all modules. Twelve modules are used in the SIMAR application for:

– defining the initialization of the simulation and the main menu;

– saving and loading the application resources;

– the input of compulsory decisions;

– the input of financing decisions;

– the input of and saving simulation parameters;

– defining the database view before importing data from the database and setting the expert into motion;

– the display and edition of reports;

– testing if the simulation is possible, existence of parameters, calling the main simulation computation;

– defining the view of the database, importing market simulation parameters and calling the market simulation model;

– defining the view of the database for importing data needed for accounting, fiscal and logistic models; and

– defining the view of the database for importing data needed for the computation of annual reports, calling the model to perform computation for annual reports.

## 5. Some lessons from trying to use the application with a real company

The above-described diagnosis and strategic decisions have shown that some of the basic strategic knowledge have been modeled. However, it would be wrong to believe that all important strategic knowledge can be formalized. We have tried to apply the above model to a French software company. The software, which this company produces, does not enter in the category of consumer goods for which we have built our SIMAR application. This attempt is interesting, however, to point out the kind of strategic knowledge which cannot be modeled or for which there is no interest to be modelled. So we are now going to give a brief description of the activity of this company and of its strategic decision during the last 18 years to contrast it with the formalized knowledge we have presented above.

## 5.1. Nature of the company

The company is a French software house, the activity of which is broken down into four main activities:

– sales of software products;

– maintenance of software product;

– educational seminars for the company product; and

– special software development.

The company is on two software market segments. The first is development software softwareŽ for application development and the second is appli-. cation software. This second market is itself broken down into market sub-segments:

– financial software for banks;

– sales forecasting and reporting;

– financial software for companies and local governments; and

– educational software.

The development software is an international market, which is highly specialized and dominated by US companies. The application software market is a domestic market, which only is exposed to domestic competition. The development software necessitates a much higher investment than the application software. The company, which was initially developing software for the minicomputer market Digital VaxŽ minicomputers decided in 1990 to specialize in the. PC market. Since there is a direct link between the sales of software, maintenance and educational seminars, the maintenance income and educational income are directly computed from the sales figure for each product<sup>r</sup>market segment software.

## 5.2. Use of the application

The company uses a marketing mix model to simulate expected level of sales using different hypotheses for the size of the sale force, promotion expenditure and price. The production model is mainly used to compute the cost of maintaining and developing products when people are hired for that purpose. The project management model is mainly used to simulate the impact of the adoption of a project on future expenses and sales. The FINSIM model described in 5 is used to evaluate the overall<sup>w</sup> <sup>x</sup> financial performance of the company and compute financial needs and simulate financing strategies.

## 5.3. Strategy formulation

According to the CEO, a number of important strategic moves were made by the company during the last 18 years. The first was the decision to quit the minicomputer market in 1980 and to concentrate on the PC market. This move was highly successful. The second was the integration in 1985 of AI technology into the application software. The third was the decision in 1990 to adopt graphical interface technology, to invest in object-oriented programming and make the system software available under Windows. These moves were made to:

– move from declining minicomputer to rapidlyŽ . expanding PC market; Ž .

– add a competitive advantage new functionsŽ with AI ;.

– stay competitive with other competitive products by adopting a characteristic already used by some competitors graphical user interface ;Ž .

– make the company products more easily expandable and more reliable adoption of softwareŽ engineering technology ; and.

– create an independent company specialized in R&D.

The first decision is a move to quit a decreasing market segment for a very rapidly expanding one. The second is a differentiation to offer new functions to the application software. The third is a reaction to competition. The fourth is an investment to stay competitive in the long run by decreasing maintenance costs and improving the capacity of the products to adapt to the market evolution. The goal of the last move is to obtain a better control of R&D costs, have a better chance to benefit from European and governmental research contracts and to seek more efficiently for risk capital.

The strategic variables for the company are discussed during meetings held every year during the board meeting. They are also discussed regularly in informal meetings among product managers, the sales manager, the accountant, the software engineers and the chief executive of the company. A discussion with the chief executive of the company has shown that his main problems are the following. 1 ForŽ . each software product: comparison with competitive products in terms of clients needs, technical characteristics, price, quality of user interface, documentation, sale force, advertising and promotion. This implies the adoption of new technology for software development. 2 To master the technical problemsŽ . related with compilors and the operating systems under which are used the software products DOSŽ and Windows . 3 To master the reliability problem. Ž . Žhow to produce reliable and performing software of a large size . 4 How to attract and keep top level. Ž . software engineers at a reasonable salary level. 5Ž . How to attract and keep top level salesman. 6 HowŽ . to attract and keep top level application programmers. 7 How to obtain precise information onŽ . characteristics of competitive products to provide good arguments to the sales force during negotiation and to provide guidance for the enhancement of its own products. 8 How to obtain reliable informationŽ . on the reasons which have led important potential customers to give preference to competition. 9Ž . How to protect the investment of the company Ž . Ž . software protection . 10 How to find the financing for the R&D expenses on new products researchŽ contracts . 11 How to finance the launching and. Ž . marketing of new products. 12 Which type ofŽ . distribution agreement to sign with dealers. 13Ž . How to motivate dealers and develop good relations with dealers based on mutual trust.

## 5.4. What one should not attempt to model

As can be seen, the above-described processes and CSFs cannot be modeled using quantitative models since they rely on the selection of human resources and the motivation of people. These problems deal essentially with the search for competent people, the motivation of employees, negotiation with main customers and strategy formulation. These are the daily problems of the senior executives of the company. It is not possible to model, to take just this example, the action of selecting a good manager to take care of the launching of a new product. Even if it is eventually possible to write a knowledge base, which will recall for the decision maker what he should check when facing such decisions, the modeling of this kind of knowledge is worthwhile only if the analysis must be repeated often as what happens in a strategy consulting company for clients. In other companies, since these situations are not repeated, the cost of modeling them by far exceeds the potential benefits.

## 6. Conclusions and indications for future research

An application to simulate a market and compa nies in competition on this market has been developed. This application can use knowledge bases. Three prototype simple knowledge bases have been developed: a knowledge base for financial diagnosis, a knowledge base for marketing analysis and product positioning, a knowledge base for production cost analysis. The prototype of a strategic knowledge base has been defined. This knowledge base uses the conclusion of the three diagnosis knowledge bases. It concentrates on the decision to abandon a product and to launch a new product. The decision to abandon a product is the result of an analysis of the competitive position of the product. The decision to launch a new product incorporates the decisions concerning the choice of characteristics of the new product, the production level and its marketing mix and the estimated market size. The development of this prototype strategic knowledge base helps to specify the right formalism for this type of knowledge and the kind of strategic knowledge, which can be formalized. Future research will concentrate on improving the prototype strategic KB. The prototype strategic KB will be accessible as a ‘‘consultant’’ to support the teams. The ultimate goal being to use the strategic KB as an ‘‘artificial’’ team for a firm playing against the teams of students or business executives participating in the simulation. In the future, we can even expect to have various KBs being used as virtual teams. SIMAR could then be used to simulate 5 to 20 years of company activity. Each simulated company being managed by a knowledge base. The role of the players will then be, not to make decisions, but to study the strategic KB and to improve it. Several other fruitful research directions could be: 1 The adaptation of the modelsŽ . and the KB to specific industries. 2 To extend theŽ . simulation to handle real-time decision making. In this case, the decisions are input at any time by the participants. Consequences of decisions are taken into account immediately. 3 To introduce an R&DŽ . model.

With respect to the last point in the present simulation, a new product can always be put on the market if the fixed assets to produce it can be financed by the company. There is no need to do any R&D prior to having a product available with new characteristics. However, there are many industries where this is a very unrealistic assumption. There is always an industrial risk. R&D do not always give birth to a new product with the expected characteristics.

## Acknowledgements

A first version of the SIMAR market simulation model was initially programmed in PASCAL. An early version of this article was presented at Abo Ž . Finland in June 1994 during an IAMSR international seminar on knowledge-based systems and strategic management. The work on the new version of SIMAR, including the new AI characteristics to define and test strategic knowledge bases, started in 1996. We would like to thank: the company SIG for financing this research and the company Decision Systems Research for providing support on OP-TRANS Object; Ms. Claire Sauvecane and Philippe Granjon from SIG for their work on the models and database part of the application; Cyrille Danes from DSR for his work on the client-server version of the SIMAR application; Professor Victor Hargreaves for some stylistic comments.

## References

<sup>w</sup> <sup>x</sup> 1 F.M. Bass, L.J. Parsons, Simultaneous-equation regression analysis of sales and advertising, Applied Economics 1 1969 Ž . 103–124.

<sup>w</sup> <sup>x</sup> 2 C. Carlsson, Knowledge formation in strategic management, Research Report 4<sup>r</sup>93, Institute for Advance Management Systems Research, Abo Akademi University, Finland.

<sup>w</sup> <sup>x</sup> 3 A.M. Geoffrion, SML: a model definition language for structured modeling, Working Paper 360, Western Management Science Institute, UCLA, 1988.

<sup>w</sup> <sup>x</sup> 4 M. Klein, R. Traunmuller, User interface of knowledge-based¨ DSS development environment, some further developments, in: V. Marik, J. Lazansky, R. Wagner Eds. , Database andŽ . Expert Systems Applications, Proceedings 4th International Conference, DEXA, 1993, Springer Verlag, Lecture Notes in Computer Science, 1993.

<sup>w</sup> <sup>x</sup> 5 M. Klein, L. Methlie, Knowledge-Based DSS, Wiley, New York, 1995.

<sup>w</sup> <sup>x</sup> 6 M. Klein, Using OPTRANS Objet as a knowledge-based DSS development environment to design KB-DSS applications, in: M. Bazewicz Ed. , Proceedings of the 19th Infor-Ž . mation Systems’ Architecture and Technology ISAT , Inter-Ž . national Scientific School, Wroclaw University of Technology, Faculty of Computer Science and Management, 1997.

<sup>w</sup> <sup>x</sup> 7 M. Klein, R.W. Grubbstrom, Using OPTRANS as a KB-DSS development environment for designing DSS for production management, European Journal of Operational Research, Special Issue, Vol. 109, Proceedings of the Bruges 1997 DSS Conference, 1998.

<sup>w</sup> <sup>x</sup> 8 M. Nerlove, K.J. Arrow, Optimal advertising policy under dynamic conditions, Economica May 1962 129–142.Ž .

<sup>w</sup> <sup>x</sup>9 OPTRANS Object, Manuel d’Introduction version 3.22 ,Ž . Decision Systems Research, 4 rue de la Liberation, 78350 Jouy-en-Josas, France, Web: http<sup>rr</sup>:www.dsr.fr.

<sup>w</sup> <sup>x</sup> 10 M. Page, DIADEM 4.0 Manuel de Reference, CRISS, UPMF, Octobre 1995.

<sup>w</sup> <sup>x</sup>11 K. Palda, The Measurement of Cumulative Advertising Effects, Prentice-Hall, Englewood Cliffs, NJ, 1964.

<sup>w</sup> <sup>x</sup> 12 M.E. Porter, Competitive Strategy: Techniques for Analyzing Industries and Competitors, The Free Press, New York, 1980.

<sup>w</sup> <sup>x</sup> 13 M.E. Porter, Competitive Advantage: Creating and Sustaining Superior Performance, The Free Press, New York, 1985.

<sup>w</sup> <sup>x</sup> 14 Simar Manuel Methodologique, SIG, 4 rue de la Liberation, ´ 78350 Jouy-en-Josas, France, 1998, sig@easynet.fr.

<sup>w</sup> <sup>x</sup> 15 R. Stein, V. Dhar, Intelligent Decision Support Methods, Prentice-Hall, Englewood Cliffs, NJ, 1997.

<sup>w</sup> <sup>x</sup> 16 L.G. Telser, The demand for branded goods as estimated from consumer panel data, Review of Economics and Statistics August 1962 300–324.Ž .

<sup>w</sup> <sup>x</sup> 17 J.L. Weldon, Managing multidimensional data, Database Programming and Design 8 1995 .Ž .

<sup>w</sup> <sup>x</sup> 18 Y. Wind, G. Lilien, Marketing strategy models, in: L. Eliasburg Ed. , Handbook in OR and MS, Vol. 5, Elsevier,Ž . Amsterdam, 1993.

<sup>w</sup> <sup>x</sup> 19 Winston and Holsapple, Decision Support Systems, Springer, Coll. Computer and System Science 101, 1993.

![](/api/attachments/8367XY3R/fulltext/images/150f41b62fac21c6bbc2de560b8e4efa35e803e19f701bcbc60cdac5bc2fbdbf.jpg)

Dr. Michel R. Klein is a Professor of Management at HEC School of Management, France. A former Graduate of HEC after his studies in Mathematics and Physics, he holds a ‘‘licence’’ in Econometrics, an MBA from the Tuck School of Business Administration at Dartmouth College, a doctorate in Management from the University of Lille France. Michel Klein has been in charge of developing several knowledge-based DSS applications such as FINSIM and

SEXTAN widely used in France in banks to support credit officers and risk analysts. Since 1993, he has been heading the team developing OPTRANS Object, a KB-DSS development environment, at the company Decision System Research DSR .Ž . Michel Klein is the author of several books and co-author of the book Knowledge-Based Decision Support System published by Wiley in 1995. He has been on the program committee of several international conference on management and engineering applications of Artificial Intelligence and was the Editor, with T. Jelassi and W. Mayon White, of the IFIP TC8<sup>r</sup>WG8.3 conference on ‘‘DSS, Experience and Expectations’’. Michel Klein has published in such journals as the European Journal of Operational Research, the International Journal of Production Economics, etc. He has presented papers at several IFIP World Computer Conferences, at several IFIP working group conferences, the International Conference on Decision Support Systems, the Database and Expert Systems Application DEXA conference, the Hawaii In-Ž . ternational Congress on Systems Sciences, at the AI Internationa Conference, etc. He participated in two NATO Advanced Studies Institute on DSS. He is Associate Editor of DSS International and of Information and System Engineering. Michel Klein’s present research interests include the design of knowledge-based objectoriented DSS development environment, the coupling of simulation and reasoning, the design of knowledge-based applications in finance, production, engineering and strategy. He has recently been involved in a distance learning project with the London School of Economics and other European Business School using PC-based video.
