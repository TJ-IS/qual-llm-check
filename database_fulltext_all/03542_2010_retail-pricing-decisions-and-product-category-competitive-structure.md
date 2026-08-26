---
otero_id: 3542
otero_key: "MQ54CVAM"
title: "Retail pricing decisions and product category competitive structure"
authors: "Óscar González-Benito; María Pilar Martínez-Ruiz; Alejandro Mollá-Descals"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.01.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Retail pricing decisions and product category competitive structure

Óscar González-Benito <sup>a,</sup>⁎, María Pilar Martínez-Ruiz <sup>b,1</sup>, Alejandro Mollá-Descals <sup>c,2</sup>

<sup>a</sup> Dpto. Administración y Economía de la Empresa, Universidad de Salamanca, Campus Miguel de Unamuno, 37007 – Salamanca, Spain

<sup>b</sup> Área de Comercialización e Investigación de Mercados, Universidad de Castilla-La Mancha, Avenida de los Alfares, 44, 16002 – Cuenca, Spain

<sup>c</sup> Dpto. Comercialización e Investigación de Mercados, Universidad de Valencia, Avenida de los Naranjos, s/n, 46022 – Valencia, Spain

## a r t i c l e i n f o

Article history: Received 15 September 2008 Received in revised form 11 January 2010 Accepted 24 January 2010 Available online 29 January 2010

Keywords: Retail pricing decision model Demand forecasting Market share models Category management Competitive structure Store-level scanner data

## a b s t r a c t

This study addresses the use of demand forecasting techniques by retailers to support their decision making. Speci<sup>fi</sup>cally, the authors propose a pricing decision support model for retailers to estimate optimal prices, whose output depends on the con<sup>fi</sup>guration of a supporting measurement model. The measurement model is a demand function that relates sales and prices within the category; optimal prices are those whose effects on demand and retail margins maximize the category's pro<sup>fi</sup>tability. This investigation focuses particularly on the role of competitive structure, such that the authors consider two types of price competition asymmetries for demand forecasting: those depending on the brand (differential price effects) and those dealing with demand for competing brands (cross-price effects). By explicitly modeling competitive asymmetries in the demand function that underlies the decision support model, the authors assess implications for pricing decisions, sales, and pro<sup>fi</sup>tability. The empirical application of the model to store-level, aggregated scanner data for two frequently purchased categories reveals the impact of an asymmetric competitive structure on demand forecasting and optimal pricing decisions. Furthermore, this article quanti<sup>fi</sup>es the costs of ignoring asymmetric competitive interactions in retailers' decision making.

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

The increasing power of retailers has become more apparent in the form of greater autonomy in their <sup>fi</sup>nal pricing decisions. These autonomous retailer pricing decisions constitute a key element of marketing channel performance that can determine the pro<sup>fi</sup>ts of manufacturers [18], especially if the decisions come from large-scale retailers [20]. Therefore, it should come as no surprise that retailing research has focused primarily on category management and the favorable consequences of this management strategy compared with brand-centered management [45]. Authors cite the key role of category management in achieving more pro<sup>fi</sup>table retail pricing structures [3], yet no studies investigate the extent to which these positive consequences might depend on the implementation of the category management. Despite the importance of assessing and understanding the competitive structure of product categories for successful category management, prior research offers little empirical support. This article addresses this gap by analyzing how a greater understanding of the competitive structure within a product category may improve retail pricing decisions in the context of category management approaches.

A full understanding of any competitive structure requires the analysis of competition asymmetries [8]; we consider the role of two types of price competition asymmetries. First, the impact of variations in a brand's price may differ depending on the brand, in that the price changes of different brands likely affect demand with greater or lesser intensity. Second, the impact of variations in a brand's price may differ across the various levels of demand for competing brands. The higher the substitutability of two brands, the greater the impact of their price changes. If retailers explicitly consider these asymmetries in their category pricing decision making, they may make more precise predictions about market responses to their pricing decisions and thereby improve their pro<sup>fi</sup>tability.

We propose a pricing decision-making model, based on aggregated scanner data in the context of frequently purchased categories. In this model, the optimal prices are those whose effects on demand and retail margins maximize the category's pro<sup>fi</sup>tability; the output therefore depends on the con<sup>fi</sup>guration of a supporting measurement model, in which the demand function relates sales and prices within the category. Our proposed model explicitly details competitive asymmetries in the demand function, which indicates their implications for pricing decisions and thus for sales and pro<sup>fi</sup>tability.

Various authors have considered the problem of pricing decision optimization for retailers [10,21,25,29,31,39,42]. In Table 1, we summarize the key contributions of these studies for our investigation. Although all these approaches recognize that the optimal prices for a product category maximize its expected pro<sup>fi</sup>ts, few consider competitive asymmetries explicitly when they specify the relationship between prices and sales. Rather, the effects they <sup>fi</sup>nd result from different assumptions about consumer behavior. For example, some studies incorporate latent heterogeneity among consumers [10,21,42], whereas others incorporate latent heterogeneity among stores [25], though in neither case can they isolate the role of competitive asymmetries from other price optimization determinants.

Table 1  
Previous research contributions regarding the category pricing optimization decision.

<table><tr><td>Research</td><td>Retail context</td><td>Data (level of aggregation)</td><td>Explicit asymmetric effects?</td></tr><tr><td>Reibstein and Gatignon [31]</td><td>Grocery retailing</td><td>Store-level aggregated data. Two stores.</td><td>Yes</td></tr><tr><td>Vilcassim and Chintagunta [42]</td><td>Grocery retailing</td><td>Household-level data</td><td>No</td></tr><tr><td>Kim, Blattberg, and Rossi [21]</td><td>Grocery retailing</td><td>Household-level data</td><td>No</td></tr><tr><td>Tellis and Zufryden [39]</td><td>Grocery retailing</td><td>Household-level data</td><td>No</td></tr><tr><td>Montgomery [29]</td><td>Grocery retailing</td><td>Store-level aggregated data. One store</td><td>Yes</td></tr><tr><td>Chintagunta [10]</td><td>Grocery retailing</td><td>Store-level aggregated data. Several stores</td><td>No</td></tr><tr><td>Mantrala et al. [25]</td><td>Automotive aftermarket retailing</td><td>Store-level aggregated data. Several stores.</td><td>No</td></tr></table>

Notes: Each line corresponds to a brand and represents the effects of price changes across competing brands.

Two studies formalize each brand's demand within a product category as a function of all brand prices to capture competitive asymmetries [29,31], but this procedure is not robust [42], because the model can produce unrealistic solutions, such as in<sup>fi</sup>nite or negative prices. To resolve this issue, we incorporate brand demand decomposition into category demand and market share. In other words, the price effect consists of purchase decision and brand choice decision effects; the latter re<sup>fl</sup>ect the competitive interaction among brands. Using market share models that possess logical consistency adds robustness to the demand function and enables more explicit modeling of the asymmetric price effects [12].

This article's contribution is twofold. First, we investigate the role of competitive structure in successful retail category management, especially the extent to which understanding competitive structures within a product category improves the pro<sup>fi</sup>tability of the whole category as a result of improved pricing decisions. Our proposed model decomposes the price optimization problem of retailers into its relevant components (i.e., decision model, overall category demand model, and within-category market share model) and offers a way to understand the effects of the competitive structure (i.e., competitive asymmetries between brands). Second, our empirical application shows that the proposed decision support model can operate with the input of readily available, store-level, aggregated scanner data; we also provide a numerical example in which the consideration of competitive asymmetries changes the retailer's optimal decisions. Although our approach is based on assumptions subject to some limitations, it improves researchers' and practitioners' ability to make pricing decisions within a product category by accounting for competitive asymmetries. Our goal is to demonstrate that incorporating asymmetry in cross-price effects alters a retailer's pricing decision.

## 2. Modeling proposal

Our proposed model attempts to determine optimal prices for every brand included in a frequently purchased product category in a retail store. The proposal employs scanner data aggregated to the store-level and assumes that the retailer has information about sales, prices, and other marketing variables for every brand within the product category for a speci<sup>fi</sup>ed sample of time periods.

Of the three possible aggregation levels for scanner data— household, store, and market [17]—most studies focus on the storelevel, because of the limited availability of disaggregated scanner data from point-of-sale systems located in retail stores. Information about the purchase history of speci<sup>fi</sup>c households and consumers is available exclusively for those clients that the retailer can identify, such as through loyalty cards or credit accounts. Using such information can lead to bias though, such as when consumers use several cards or apply them only in speci<sup>fi</sup>c purchase occasions (e.g., large purchases).

Furthermore, the loyalty card consumer group may not represent the store's clients overall. Therefore, an analytical methodology that aims to be replicable for any store at any time and whose estimations and recommendations involve all potential customers of the store requires the use of scanner data aggregated to the store-level.

Our proposed model contains two key elements. First, the decision model provides an objective function, whose optimization determines the optimal prices, and the function depends on the market response to marketing stimuli, such as price. Second, this proposal represents a formalization of the measurement model that captures the relationship.

## 2.1. Decision model: objective function

A store's objective is to maximize the pro<sup>fi</sup>t generated by the product category [21,31,39,42]. Pro<sup>fi</sup>t $B _ { t }$ in period t thus equals the sum of the gross pro<sup>fi</sup>t generated by each brand N that constitutes the category, minus the <sup>fi</sup>xed costs $C F _ { t }$ for that category. The pro<sup>fi</sup>t of brand i equals the sold units $Q _ { i t }$ multiplied by the unitary margin, which is the difference between the unitary price $P _ { i t }$ and the unitary cost $C _ { i t } .$ In short,

$$
B _ {t} = \left(\sum_ {i = 1} ^ {N} (P _ {i t} - C _ {i t}) \cdot Q _ {i t}\right) - C F _ {t}\tag{1}
$$

The quantity that each brand sells depends on the pricing policy adopted for the category. Although the model focuses on this variable, the quantity sold also can represent a function of other marketing variables managed within a category (e.g., promotions through feature advertising and store displays). The quantity sold depends on other contextual circumstances E (e.g., seasonal consumer habits). Modelers therefore must understand sales as an endogenous variable, explained as follows:

$$
Q _ {i t} = f \Big (\{P _ {i t} \} _ {i = 1} ^ {N}; E _ {t} \Big)\tag{2}
$$

Optimal prices maximize the expected pro<sup>fi</sup>t, as in Eq. (1). These prices do not depend on the <sup>fi</sup>xed costs assumed by the retailer, so modelers can ignore this factor from an operational point of view. Although the retailing sector plays an increasingly important role in setting prices, the manufacturer's restrictions on the retailer's brand price modi<sup>fi</sup>cations still in<sup>fl</sup>uence the optimization problem; some national brands impose particularly signi<sup>fi</sup>cant limitations on the retail prices of their products.

In either case, our proposal constitutes a simpli<sup>fi</sup>ed interpretation of the problem, with three primary limitations: First, it assumes a <sup>fi</sup>xed cost structure, but the unitary cost for a brand may depend on sales volume, which can be negotiated with suppliers [39]. Similarly, sales category volume may condition the <sup>fi</sup>xed costs, at least partially. Therefore, we assume that the manufacturer is a strategic player with regard to maximization and that the wholesale price may be restrictive. This assumption is not problematic, because this research attempts to show that incorporating asymmetry in cross-price effects can change the retailer's pricing decision. Second, though the analysis does not include other product categories, complementary and substitutable relationships often exist across categories [9,33,43]. Certain product categories also may have objectives other than pro<sup>fi</sup>t maximization, such as generating customer <sup>fl</sup>ow to support other categories, enhancing store loyalty, or de<sup>fi</sup>ning the store image [14]. The optimal decision then maximizes pro<sup>fi</sup>ts across all product categories only after the consideration of all complementary and substitutability effects. Third, this approach does not integrate the marketing actions of competing stores, even though the assortment, prices, and promotions offered by competing stores likely affect category sales [7,26,38,43]. Thus, the decision-making process may represent a search for equilibrium in the context of game theory.

These limitations relate closely to three important circumstances that determine the pricing decisions of retailers [10], namely, negotiations and agreements with suppliers, brand and category objectives, and competition among retailers.

## 2.2. Measurement models: market response

After establishing the optimization problem, we must specify the demand function in Eq. (2), which represents the measurement model. Some researchers suggest splitting brand sales into total category sales Q and brand market share $\pi _ { i t }$ to obtain

$$
Q _ {i t} = \pi_ {i t} \cdot Q _ {t}\tag{3}
$$

This approach assumes that market share depends on the marketing decisions for each brand, as well as the resulting competitive interaction, whereas the total category sales absorb the effect of the contextual circumstances. In this case, both variables appear endogenous, assuming that

$$
\pi_ {i t} = f \left(\left\{P _ {i t} \right\} _ {i = 1} ^ {N}\right) \text { and } Q _ {t} = f \left(\left\{P _ {i t} \right\} _ {i = 1} ^ {N}; E _ {t}\right)\tag{4}
$$

## 2.2.1. Market share model

Models with logical consistency can explain market share [12,13]. This methodological framework requires coherence across estimated market shares, which must be positive and add to 1; it also assumes that the market share of each brand is equivalent to the attraction $A _ { i t }$ that the brand generates compared with the attraction of other brands. That is.

$$
\pi_ {i t} = \frac {A _ {i t}}{\sum_ {j = 1} ^ {N} A _ {j t}}\tag{5}
$$

To understand the attraction concept, consider the marketing effort for a corresponding brand. Assuming a logit multinomial (MNL) conditional con<sup>fi</sup>guration, attraction is:

$$
A _ {i t} = \exp (\alpha_ {i} + \beta \cdot P _ {i t})\tag{6}
$$

where α is an intrinsic attraction constant associated with each brand, and β is a parameter that relates to the price effect. Logit models from a disaggregated perspective can explain consumer choice behavior, such that market share represents the choice probability. The theory of random utility also helps clarify these models [24,27].

However, a classic explanatory con<sup>fi</sup>guration assumes symmetrical competition between brands, such that the price effect of one brand on another always remains the same, regardless of the brands considered [22]. The β parameter, which indicates the degree of competition or substitutability between brands, represents this constant effect. In turn, the classic MNL con<sup>fi</sup>guration assumes two types of competitive symmetries.

First, the effect of brand i on brand j is the same as the effect of brand j on brand i $( { \mathrm { i . e . , ~ } } i \to j = j \to i )$ . Such symmetry also marks a model in which absolute cross-price effects, de<sup>fi</sup>ned as the change in the market share points of a target brand when the price of the competing brand changes by 1% of the product category price, are symmetric in a classic logit model [35]. However, this assumption appears inadequate in certain competitive contexts. For example, with regard to the relationships between the price and quality tiers of brands and their price variations, promoting a high-priced brand sometimes has a greater effect on the demand for low-priced brands than vice versa [1,2,6,34–36]. The characteristics of some brands also relate to category promotional price elasticities [44]. Incorporating a speci<sup>fi</sup>c parameter $\beta _ { i }$ for each brand i offers a solution that assumes different effects for each brand [12]. The differential effects extend the proposed con<sup>fi</sup>guration in Eq. (6) as follows:

$$
A _ {i t} = \exp (\alpha_ {i} + \beta_ {i} \cdot P _ {i t})\tag{7}
$$

Second, this approach assumes that the effect of brand i on brand j is the same as the effect of brand i on brand k or any other competing brand $( { \mathrm { i } } . { \mathrm { e } } . , i \to j = i \to k )$ . This property remains in effect even in a model with differential effects, as outlined in Eq. (7). Therefore, the cross-elasticity of the market share of brand j with respect to the price of brand i must be independent of the former—a property called the independence of irrelevant alternatives. This assumption is too restrictive in certain competitive contexts, such as when greater competition occurs between brands that are closer in their price or quality [32,35,36].

To solve this inconvenience, Cooper and Nakanishi [12] propose an extended attraction model, in which the price of brand j has a different effect $\beta _ { i j }$ on each competing brand i. This model of crosseffects extends the con<sup>fi</sup>guration proposed in Eq. (7) as follows:

$$
A_{it} = \exp \left(\alpha_{i} + \sum_{\substack{j = 1\\ j\neq i}}^{N}\beta_{ij}\cdot P_{jt}\right)\tag{8}
$$

The explicit representation of the asymmetric competitive effects of price emerges through a sequential extension of the classic choice model, that is, the differential effects model on the <sup>fi</sup>rst level, and the cross-effects model on the second.

## 2.2.2. Model of overall demand

To explain overall category demand, we propose an exponential con<sup>fi</sup>guration:

$$
Q _ {t} = \exp \left(\gamma + \sum_ {m = 1} ^ {1 2} \xi_ {m} \cdot E _ {m t} + \sum_ {d = 1} ^ {6} \zeta_ {d} \cdot E _ {d t}\right) \cdot P C _ {t} ^ {\delta}\tag{9}
$$

where $E _ { m t }$ and $E _ { d t }$ are dummy variables that indicate each month m and each day d, respectively; $\xi _ { m }$ and $\zeta _ { d }$ are parameters for these seasonal effects, respectively; and γ is the demand constant. To identify this model, we must <sup>fi</sup>x one parameter for the month effect and one parameter for the day effect. Furthermore, $P C _ { t }$ represents the category price, or the sum of prices across brands weighted by their observed market shares, calculated as

$$
P C _ {t} = \sum_ {i = 1} ^ {N} \pi_ {i t} \cdot P _ {i t}\tag{10}
$$

and δ is the price effect parameter. The price effect of each brand in the category is proportional to the market share of those brands, because the price variations of leader brands should have a greater impact than those of less frequently purchased brands. The exponential con<sup>fi</sup>guration of the model also requires that the effect of the category price be proportional to the sales in every season.

## 3. Empirical analysis

To exemplify the explanatory possibilities of our proposed model and explore the role of a complex competitive structure with regard to the optimization of category prices, our empirical application addresses the context of frequently purchased products.

## 3.1. Study scenario and data

The data consist of receipts registered by a supermarket over the course of one year, which list 301 daily observations of prices and sales and thus capture intra-week variance. However, no information about other promotional variables (e.g., feature advertising and displays) that the grocery uses frequently is available. Two product categories represent the primary focus of our analysis: caffeinated ground coffee in 250-gram packages and yoghurt in 125-gram packages. We provide the statistics for the two categories in Tables 2 and 3.

Caffeinated ground coffee is a nonperishable category that we selected because it offers daily observations and was subject to frequent temporary price discounts during the study period. In addition, previous marketing studies have often analyzed this category [4,15,16,30]. The yoghurt category also offers daily observations and frequent temporary price discounts, but it represents a perishable product with a short expiration date, which distinguishes it from the coffee category.

Thus, our experiment includes two product categories with different degrees of perishability. Prior marketing research demonstrates that promotional effects can cause signi<sup>fi</sup>cant differences across categories, depending on certain unpredictable phenomena, such as stockpiling induced by promotions [28], and in this sense, the two product categories also differ in their purchasing trends, such that consumers buy yoghurt more frequently. This increased incidence can lead to more complex competitive structures, because substitutability and complementarity effects combine in frequently purchased categories [19].

## 3.2. Measurement models: estimation

As a <sup>fi</sup>rst approximation of the decision problem, we consider three speci<sup>fi</sup>cations to estimate the market share model (Eqs. 6–8). The estimation relies on an adaptation of the maximum likelihood method for probabilistic models, and the parameter estimates maximize the following likelihood function:

$$
{\cal L} = \prod_ {t} \prod_ {i = 1} ^ {N} \pi_ {i t} ^ {g _ {i t} \cdot N}\tag{11}
$$

Brands in the coffee category: descriptive statistics.

<table><tr><td colspan="7"> $Sales^a$ </td></tr><tr><td></td><td>Mean</td><td>S.D.</td><td>Maximum</td><td>Minimum</td><td>Total</td><td>Market share</td></tr><tr><td>154</td><td>4.7</td><td>6.2</td><td>44</td><td>0</td><td>1411</td><td>0.10</td></tr><tr><td>Bonka</td><td>17.0</td><td>16.6</td><td>94</td><td>0</td><td>5120</td><td>0.35</td></tr><tr><td>Marcilla</td><td>14.6</td><td>15.7</td><td>91</td><td>0</td><td>4392</td><td>0.30</td></tr><tr><td>Saimaza</td><td>5.2</td><td>9.5</td><td>76</td><td>0</td><td>1561</td><td>0.11</td></tr><tr><td>Soley</td><td>4.6</td><td>7.3</td><td>57</td><td>0</td><td>1386</td><td>0.10</td></tr><tr><td>Bahia</td><td>2.2</td><td>3.4</td><td>26</td><td>0</td><td>646</td><td>0.04</td></tr><tr><td colspan="7"> $Price^b$ </td></tr><tr><td></td><td></td><td>Mean</td><td>S.D.</td><td>Maximum</td><td></td><td>Minimum</td></tr><tr><td>154</td><td></td><td>184.5</td><td>6.1</td><td>189</td><td></td><td>159</td></tr><tr><td>Bonka</td><td></td><td>206.4</td><td>13.7</td><td>235</td><td></td><td>185</td></tr><tr><td>Marcilla</td><td></td><td>217.6</td><td>21.0</td><td>259</td><td></td><td>189</td></tr><tr><td>Saimaza</td><td></td><td>225.6</td><td>18.4</td><td>249</td><td></td><td>189</td></tr><tr><td>Soley</td><td></td><td>204.7</td><td>11.1</td><td>235</td><td></td><td>187</td></tr><tr><td>Bahia</td><td></td><td>188.9</td><td>7.5</td><td>195</td><td></td><td>157</td></tr></table>

Notes: Each line corresponds to a brand and represents the effects of price changes across competing brands.  
<sup>a</sup> Sales in units.  
<sup>b</sup> Price in pesetas; 1 euro = 166.386 pesetas.

Brands in the yoghurt category: descriptive statistics.

<table><tr><td colspan="7"> $Sales^a$ </td></tr><tr><td></td><td>Mean</td><td>S.D.</td><td>Maximum</td><td>Minimum</td><td>Total</td><td>Market share</td></tr><tr><td>Chamburcy</td><td>115.7</td><td>219.7</td><td>2226</td><td>0</td><td>34841</td><td>0.24</td></tr><tr><td>Sveltesse</td><td>76.4</td><td>97.4</td><td>1088</td><td>0</td><td>22996</td><td>0.16</td></tr><tr><td>Danone</td><td>183.5</td><td>169.5</td><td>1168</td><td>0</td><td>55225</td><td>0.38</td></tr><tr><td>Yoplait</td><td>12.7</td><td>29.6</td><td>248</td><td>0</td><td>3828</td><td>0.03</td></tr><tr><td>Clesa</td><td>92.4</td><td>102.1</td><td>554</td><td>0</td><td>27812</td><td>0.19</td></tr><tr><td colspan="7"> $Price^b$ </td></tr><tr><td></td><td></td><td>Mean</td><td>S.D.</td><td>Maximum</td><td></td><td>Minimum</td></tr><tr><td>Chamburcy</td><td></td><td>27.4</td><td>2.8</td><td>31</td><td></td><td>21</td></tr><tr><td>Sveltesse</td><td></td><td>33.8</td><td>5.2</td><td>43</td><td></td><td>29</td></tr><tr><td>Danone</td><td></td><td>29.6</td><td>3.0</td><td>34</td><td></td><td>23</td></tr><tr><td>Yoplait</td><td></td><td>26.6</td><td>1.3</td><td>28</td><td></td><td>22</td></tr><tr><td>Clesa</td><td></td><td>20.7</td><td>2.0</td><td>24</td><td></td><td>19</td></tr></table>

<sup>a</sup> Sales in units.  
<sup>b</sup> Price in pesetas; 1 euro=166.386 pesetas.

where $g _ { i t }$ is the observed market share for brand i in period t. The values add to N for each period, that is, the number of observed shares. In Tables 4 and 5, we summarize the estimation results for both categories and outline the results of our test of the contribution of each explanatory con<sup>fi</sup>guration. The estimation procedure relies on GAUSS, with the OPTMUN (Newton–Raphson algorithm) optimization routine.

The explanatory con<sup>fi</sup>guration for all models is signi<sup>fi</sup>cant. Moreover, incorporating asymmetric price effects has a signi<sup>fi</sup>cant impact on both the differential effects model and the cross-effects model. The improvement in the model appears stronger for the yoghurt than for the coffee category, which implies that the competitive structure is more complex in the former.

The parameter associated with price in the classic model is negative, as expected a priori. That is, a price increase reduces brand attractiveness and market share. The price parameters with differential effects are also negative, though they differ across brands. We note that the price effects tend to be stronger for those brands with lower prices and market shares. The correlations between the price parameters and mean prices across the brands are 0.662 (coffee) and 0.207 (yoghurt); analogously, the correlations between the price parameters and market shares are 0.645 (coffee) and 0.478 (yoghurt).

Finally, as we expected, all signi<sup>fi</sup>cant price parameters in the model with cross-effects are positive. This <sup>fi</sup>nding indicates that a price increase for a particular brand also increases the attractiveness of competing brands, compared with the more expensive brand, causing their market shares to rise.

A very useful methodological framework provides a means to interpret the competitive asymmetries between brands within a product category [37]. Although analyzing speci<sup>fi</sup>c competitive patterns in the coffee and yoghurt categories is beyond the scope of this article, we consider the relationship between price competition and the price tiers of brands to be an interesting question. For each brand, we therefore compute the correlations between the cross-price parameters and the absolute mean price differences across competing brands. The average correlations within the categories are −0.167 (coffee) and 0.133 (yoghurt). The result for the coffee category thus is consistent with prior research that <sup>fi</sup>nds higher substitution effects between brands with more similar price levels. In marketing literature, this phenomenon is called the neighborhood cross-price effect; price competition between brands grows as the similarity in their prices increases [35]. The result for the yoghurt category is not consistent with that competitive pattern though. Furthermore, the observed correlations are not high. It thus appears that competitive asymmetries mainly arise from the unique features of the brand's own strategies [8].

Market share model for ground coffee: estimation results.

<table><tr><td colspan="7">Intrinsic attractiveness constants</td></tr><tr><td></td><td>Classic model</td><td colspan="3">Differential effects model</td><td colspan="2">Cross-effects model</td></tr><tr><td>154</td><td>0.55***</td><td>0.96</td><td></td><td></td><td>6.31**</td><td></td></tr><tr><td>Bonka</td><td>2.85***</td><td>1.07</td><td></td><td></td><td>4.24***</td><td></td></tr><tr><td>Marcilla</td><td>3.16***</td><td>-2.57</td><td></td><td></td><td>-3.77***</td><td></td></tr><tr><td>Saimaza</td><td>2.36***</td><td>1.08</td><td></td><td></td><td>-3.46</td><td></td></tr><tr><td>Soley</td><td>1.53***</td><td>-0.96</td><td></td><td></td><td>-1.01</td><td></td></tr><tr><td>Bahiaa</td><td>0</td><td>0</td><td></td><td></td><td>0</td><td></td></tr><tr><td colspan="7">Price effectsb</td></tr><tr><td></td><td>154</td><td>Bonka</td><td>Marcilla</td><td>Saimaza</td><td>Soley</td><td>Bahia</td></tr><tr><td colspan="7">Classic model</td></tr><tr><td>154</td><td>-0.05***</td><td>0c</td><td>0c</td><td>0c</td><td>0c</td><td>0c</td></tr><tr><td>Bonka</td><td>0c</td><td>-0.05***</td><td>0c</td><td>0c</td><td>0c</td><td>0c</td></tr><tr><td>Marcilla</td><td>0c</td><td>0c</td><td>-0.05***</td><td>0c</td><td>0c</td><td>0c</td></tr><tr><td>Saimaza</td><td>0c</td><td>0c</td><td>0c</td><td>-0.05***</td><td>0c</td><td>0c</td></tr><tr><td>Soley</td><td>0c</td><td>0c</td><td>0c</td><td>0c</td><td>-0.05***</td><td>0c</td></tr><tr><td>Bahia</td><td>0c</td><td>0c</td><td>0c</td><td>0c</td><td>0c</td><td>-0.05***</td></tr><tr><td colspan="7">Differential effects model</td></tr><tr><td>154</td><td>-0.07***</td><td>0c</td><td>0c</td><td>0c</td><td>0c</td><td>0c</td></tr><tr><td>Bonka</td><td>0c</td><td>-0.05***</td><td>0c</td><td>0c</td><td>0c</td><td>0c</td></tr><tr><td>Marcilla</td><td>0c</td><td>0c</td><td>-0.03***</td><td>0c</td><td>0c</td><td>0c</td></tr><tr><td>Saimaza</td><td>0c</td><td>0c</td><td>0c</td><td>-0.06***</td><td>0c</td><td>0c</td></tr><tr><td>Soley</td><td>0c</td><td>0c</td><td>0c</td><td>0c</td><td>-0.05***</td><td>0c</td></tr><tr><td>Bahia</td><td>0c</td><td>0c</td><td>0c</td><td>0c</td><td>0c</td><td>-0.06***</td></tr><tr><td colspan="7">Cross-effects model</td></tr><tr><td>154</td><td>0c</td><td>0.07***</td><td>0.07***</td><td>0.08***</td><td>0.07***</td><td>0.07***</td></tr><tr><td>Bonka</td><td>0.04***</td><td>0c</td><td>0.06***</td><td>0.05***</td><td>0.06***</td><td>0.06***</td></tr><tr><td>Marcilla</td><td>0.03****</td><td>0.03***</td><td>0c</td><td>0.05***</td><td>0.05***</td><td>0.04***</td></tr><tr><td>Saimaza</td><td>0.05***</td><td>0.06***</td><td>0.06***</td><td>0c</td><td>0.07***</td><td>0.05***</td></tr><tr><td>Soley</td><td>0.10***</td><td>0.07***</td><td>0.08***</td><td>0.07***</td><td>0c</td><td>0.07***</td></tr><tr><td>Bahia</td><td>0.06***</td><td>0.05***</td><td>0.06***</td><td>0.08***</td><td>0.06***</td><td>0c</td></tr><tr><td colspan="7">Goodness of fitd</td></tr><tr><td></td><td></td><td>Classic model</td><td></td><td>Differential effects model</td><td></td><td>Cross-effects model</td></tr><tr><td>Likelihood ratio test</td><td></td><td>676.00***</td><td></td><td>705.71***</td><td></td><td>746.40***</td></tr><tr><td>Pseudo R2 (ρ2)</td><td></td><td>0.12</td><td></td><td>0.13</td><td></td><td>0.13</td></tr><tr><td colspan="7">Comparison</td></tr><tr><td>Likelihood ratio test</td><td></td><td>29.71***</td><td></td><td></td><td></td><td></td></tr><tr><td>Likelihood ratio test</td><td></td><td></td><td></td><td>40.70**</td><td></td><td></td></tr></table>

\*\*\*p < 0.01; \*\* p < 0.05; \*p < 0.10.  
<sup>a</sup> Reference brand, with a null constant of intrinsic attractiveness.  
<sup>b</sup> Effect of the price of the brand in this row on the attraction of the brand in this column.  
<sup>c</sup> Parameters set to 0 in the explanatory con<sup>fi</sup>guration.  
<sup>d</sup> Comparison with the trivial model speci<sup>fi</sup>ed only for the intrinsic attractiveness constants.

The estimation of the total demand model in Eq. (9), after a logtransformation of the function, provides a linear form. This estimation is based on a multiple regression analysis carried out with SPSS, and in Tables 6 and 7, we provide the estimation results for coffee and yoghurt categories.

The explanatory con<sup>fi</sup>guration of the model is signi<sup>fi</sup>cant in both categories, though the model adjustment is much greater for coffee than for yoghurt. The price category effect also is signi<sup>fi</sup>cant and negative, which indicates that a price increase prompts an increase in the category price but a reduction in total demand. Signi<sup>fi</sup>cant seasonal effects also appear in both categories; though they vary slightly between categories, higher demand for coffee and yoghurt consistently occurs during the <sup>fi</sup>rst months of the year and the last days of the week.

An alternative de<sup>fi</sup>nition of category price, as we introduced in Eq. (10), that ignores weights (market shares) and simply includes brand prices, produces a poorer <sup>fi</sup>t of the models for both product categories.

## 3.3. Decision model: simulation

If we assume that the estimated measurement models provide the market response, we can de<sup>fi</sup>ne optimal prices as those that maximize the pro<sup>fi</sup>t equation (Eq. 1). Without information about <sup>fi</sup>xed or unit costs, our analysis again relies on certain assumptions; however, because the optimization problem does not depend on <sup>fi</sup>xed costs, our estimation does not include any assumed values for them, and the estimated pro<sup>fi</sup>t ignores such costs. In addition, a common pricing policy applies a similar margin (whether absolute or relative) to all products, so we assume the unit cost for each product is proportional to the average price, as listed in Tables 2 and 3. The costs for the coffee brands equal 80% of the average shelf price, and those of the yoghurt brands are 75% of their shelf price.

The estimation results obtained when we accept these assumptions appear in Tables 8 and 9 for the coffee and yoghurt brands, respectively. Our estimation, which does not assume any manufacturer restriction on the retailer prices, uses direct programming in GAUSS with the OPTMUN (Newton–Raphson algorithm) optimization routines. The information comprises optimal prices in both absolute and relative terms, that is, the unitary and percentage margins, as well as the estimated effects of these prices on sales and pro<sup>fi</sup>ts. We quantify the results for both categories and for each particular brand, again in both absolute and relative terms (shares). The optimal prices do not depend on the seasonal period, though sales and pro<sup>fi</sup>ts re<sup>fl</sup>ect the varying in<sup>fl</sup>uence of different months of the year and the days of the week.

Classic analysis based on the symmetrical competition model indicates that optimal pricing decisions are not homogeneous across brands; margins in both unitary and percentage terms differ across brands. We therefore revise our proposed model to account for three underlying brand-speci<sup>fi</sup>c factors that may affect optimal prices: (1) observed market share, which affects total demand through the category price; (2) intrinsic brand attraction, which in<sup>fl</sup>uences the estimated market share; and (3) unitary cost, which affects the pro<sup>fi</sup>t margin. The percentage margins tend to be higher for brands with lower prices. In addition, we <sup>fi</sup>nd that the correlations between the percentage margins and prices across brands are 0.941 (coffee) and −0.929 (yoghurt).

To model competitive asymmetries, we also need to consider variations in the estimated results of the optimal prices, sales, and pro<sup>fi</sup>ts. Explicitly modeling the individual price effects of each brand suggests different optimal prices, as does the explicit modeling of the different price effects across competing brands. The clearest variations occur in the yoghurt category, consistent with its higher competitive asymmetry. Our analysis of both product categories indicates that no clear trends mark either the evolution of prices or estimated sales.

## 3.4. Economic implications of the asymmetric effects

These results reveal competitive asymmetries between brands, so we next attempt to quantify the impact of ignoring such effects, with regard to optimal pricing decisions. Though a sequential con<sup>fi</sup>guration of the market share model, we undertake an economic analysis in which we compare the performance of each explanatory con<sup>fi</sup>guration.

The pro<sup>fi</sup>t estimations for the classic, differential effects, and crosseffects models in Tables 8 and 9 demonstrate that the differential effects model outperforms the classic model, and the cross-effects model outperforms the differential effects model. The more extended the model, the better is its prediction of the market response. Therefore, we can estimate expected pro<sup>fi</sup>ts more precisely if we assume that the effect of prices on market shares behaves in accordance with the most complete model. Following this line of reasoning, we evaluate the costs according to the cross-effects model and calculate the estimated sales and pro<sup>fi</sup>ts for the optimal decisions that derive from it. Furthermore, we consider the demand function of the model with differential effects and quantify the consequences of a decision based solely on the symmetric classical model. In Tables 10 and 11, we present the results of these analyses, along with the costs calculated for the day of the week and the month that correlate with the lowest expected demand.

Market share model for yoghurt: estimation results

<table><tr><td colspan="6">Intrinsic attractiveness constants</td></tr><tr><td></td><td colspan="2">Classic model</td><td colspan="2">Differential effects model</td><td>Cross-effects model</td></tr><tr><td>Chamburcy</td><td colspan="2">1.10***</td><td colspan="2">6.19***</td><td>8.04***</td></tr><tr><td>Sveltesse</td><td colspan="2">2.02***</td><td colspan="2">-0.64</td><td>8.74***</td></tr><tr><td>Danone</td><td colspan="2">2.36***</td><td colspan="2">3.50***</td><td>10.55***</td></tr><tr><td>Yoplait</td><td colspan="2">-0.81***</td><td colspan="2">8.52***</td><td>21.14***</td></tr><tr><td>Clesaa</td><td colspan="2">0</td><td colspan="2">0</td><td>0</td></tr><tr><td colspan="6">Price effectsb</td></tr><tr><td colspan="6">Classic model</td></tr><tr><td>Chamburcy</td><td>Sveltesse</td><td>Danone</td><td>Yoplait</td><td>Clesa</td><td></td></tr><tr><td>Chamburcy -0.19***</td><td>0c</td><td>0c</td><td>0c</td><td>0c</td><td></td></tr><tr><td>Sveltesse 0c</td><td>-0.19***</td><td>0c</td><td>0c</td><td>0c</td><td></td></tr><tr><td>Danone 0c</td><td>0c</td><td>-0.19***</td><td>0c</td><td>0c</td><td></td></tr><tr><td>Yoplait 0c</td><td>0c</td><td>0c</td><td>-0.19***</td><td>0c</td><td></td></tr><tr><td>Clesa 0c</td><td>0c</td><td>0c</td><td>0c</td><td>-0.19***</td><td></td></tr><tr><td colspan="6">Differential effects model</td></tr><tr><td>154</td><td>Bonka</td><td>Marcilla</td><td>Saimaza</td><td>Soley</td><td>Bahia</td></tr><tr><td>Chamburcy</td><td>Sveltesse</td><td>Danone</td><td>Yoplait</td><td>Clesa</td><td></td></tr><tr><td>Chamburcy -0.34***</td><td>0c</td><td>0c</td><td>0c</td><td>0c</td><td></td></tr><tr><td>Sveltesse 0c</td><td>-0.07***</td><td>0c</td><td>0c</td><td>0c</td><td></td></tr><tr><td>Danone 0c</td><td>0c</td><td>-0.19***</td><td>0c</td><td>0c</td><td></td></tr><tr><td>Yoplait 0c</td><td>0c</td><td>0c</td><td>-0.51***</td><td>0c</td><td></td></tr><tr><td>Clesa 0c</td><td>0c</td><td>0c</td><td>0c</td><td>-0.13***</td><td></td></tr><tr><td colspan="6">Cross-effects model</td></tr><tr><td>Chamburcy</td><td>Sveltesse</td><td>Danone</td><td>Yoplait</td><td>Clesa</td><td></td></tr><tr><td>Chamburcy 0c</td><td>0.29***</td><td>0.28***</td><td>0.36***</td><td>0.41***</td><td></td></tr><tr><td>Sveltesse 0.10***</td><td>0c</td><td>0.06***</td><td>0.02</td><td>0.03</td><td></td></tr><tr><td>Danone 0.28***</td><td>0.11***</td><td>0c</td><td>0.18**</td><td>0.27***</td><td></td></tr><tr><td>Yoplait 0.67***</td><td>0.57***</td><td>0.59***</td><td>0c</td><td>0.67***</td><td></td></tr><tr><td>Clesa 0.01</td><td>0.14**</td><td>0.13***</td><td>-0.06</td><td>0c</td><td></td></tr><tr><td colspan="6">Goodness of fitd</td></tr><tr><td></td><td colspan="2">Classic model</td><td colspan="2">Differential effects model</td><td>Cross-effects model</td></tr><tr><td>Likelihood ratio test</td><td colspan="2">341.56***</td><td colspan="2">455.76***</td><td>527.62***</td></tr><tr><td>Pseudo R2 (ρ2)</td><td colspan="2">0.08</td><td colspan="2">0.11</td><td>0.12</td></tr><tr><td colspan="6">Comparison</td></tr><tr><td>Likelihood ratio test</td><td colspan="2">114.20***</td><td colspan="2"></td><td></td></tr><tr><td>Likelihood ratio test</td><td colspan="2"></td><td colspan="2">71.86***</td><td></td></tr></table>

\*\*\*p < 0.01; \*\*p < 0.05; \*p < 0.10.  
Reference brand, with a null constant of intrinsic attractiveness.  
<sup>b</sup> Effect of the price of the brand in this row on the attraction of the brand in this column.  
<sup>c</sup> Parameters set to 0 in the explicative con<sup>fi</sup>guration of the model.  
<sup>d</sup> Comparison with the trivial model speci<sup>fi</sup>ed only for the intrinsic attractiveness constants.

Our comparison of the expected results for the cross-effects models (Tables 8 and 9) with our subsequent estimations (Tables 10 and 11) clari<sup>fi</sup>es the impact of simplifying the competitive structure representation. The greatest consequences pertain to the difference in the predicted results when demand actually mirrors the predications of the cross-effects model. For the coffee category, the losses in the classic model equal 5.15 pesetas per day (827.74–822.60), whereas for the yoghurt category, they reach 44.58 pesetas daily (1536.79– 1492.18). If we aggregate these losses for the whole year and take the seasonal effects into account, we calculate a total annual loss of 3,827.35 pesetas (approximately 23€) in the coffee category and 27,716.06 pesetas (167€) in the yoghurt category. The economic consequences are much more severe for the perishable category than for the nonperishable category, consistent with the higher competitive asymmetry we detect in that category.

In summary, because retailers typically carry several product lines for a wide variety of manufacturers, they are interested in product category sales, not just sales of speci<sup>fi</sup>c items. An assessment of category performance requires the consideration of competitive effects, such that retailers need to measure the impact of each brand price on the sales of competing brands, which can constitute a highly complex competitive interaction. Our <sup>fi</sup>ndings show that the economic impact of assuming a simpli<sup>fi</sup>ed, symmetric competitive structure seems minimal if we consider only one category, but in the context of the multiple product categories that even a small retail store carries, the sales losses associated with a poor understanding of the competitive structure can be severe and detrimental to its long-term economic viability.

## 4. Conclusions

To contribute to existing knowledge about the factors that underlie category management success in retail stores, we investigate the role of the category's competitive structure and propose a decision model that can indicate optimal category prices, according to scanner data aggregated to the store-level. Optimal prices maximize expected pro<sup>fi</sup>t through their effects on demand and margins. Moreover, by explicitly modeling differential and cross-price effects on brand demand, we can assess the role of an asymmetric competitive structure for optimal decisions, as well as quantify the economic consequences of ignoring this asymmetry. The cross-effects model that we propose includes various price effects between pairs of brands separately, which makes

Table 6  
Total demand model for ground coffee: estimation results.

<table><tr><td>Constant</td><td>35.69***</td></tr><tr><td>Category price</td><td></td></tr><tr><td>Category price</td><td>-6.13***</td></tr><tr><td>Seasonal effects</td><td></td></tr><tr><td>Month of the year</td><td></td></tr><tr><td>January</td><td>0.89***</td></tr><tr><td>February</td><td>0.72***</td></tr><tr><td>March</td><td>0.95***</td></tr><tr><td>April</td><td>0.55***</td></tr><tr><td>May</td><td>0.53***</td></tr><tr><td>June</td><td>0.31***</td></tr><tr><td>July</td><td>0.40***</td></tr><tr><td>August</td><td>0.22**</td></tr><tr><td>September</td><td>0.11</td></tr><tr><td> $October^a$ </td><td>0</td></tr><tr><td>November</td><td>0.10</td></tr><tr><td>December</td><td>0.09</td></tr><tr><td>Day of the week</td><td></td></tr><tr><td> $Monday^b$ </td><td>0</td></tr><tr><td>Tuesday</td><td>0.04</td></tr><tr><td>Wednesday</td><td>0.02</td></tr><tr><td>Thursday</td><td>0.33***</td></tr><tr><td>Friday</td><td>0.75***</td></tr><tr><td>Saturday</td><td>1.07***</td></tr><tr><td>Goodness of  $fit^d$ </td><td></td></tr><tr><td> $R^2$ </td><td>0.64</td></tr><tr><td>ANOVA</td><td>29,371***</td></tr></table>

\*\*\*p<0.01; \*\*p<0.05; \*p<0.10.  
<sup>a</sup> Reference month with a null parameter.  
<sup>b</sup> Reference day with a null parameter.

Table 7  
Total demand model for yoghurt: estimation results.

<table><tr><td>Constant</td><td>16.80***</td></tr><tr><td>Category price</td><td></td></tr><tr><td>Category price</td><td>-3.44***</td></tr><tr><td>Seasonal effects</td><td></td></tr><tr><td>Month of the year</td><td></td></tr><tr><td>January</td><td>0.74***</td></tr><tr><td>February</td><td>0.57**</td></tr><tr><td>March</td><td>0.64***</td></tr><tr><td>April</td><td>0.46**</td></tr><tr><td>May</td><td>0.36**</td></tr><tr><td>June</td><td>0.19</td></tr><tr><td>July</td><td>0.08</td></tr><tr><td>August</td><td>0.29*</td></tr><tr><td> $September^a$ </td><td>0</td></tr><tr><td>October</td><td>0.03</td></tr><tr><td>November</td><td>0.11</td></tr><tr><td>December</td><td>0.15</td></tr><tr><td>Day of the week</td><td></td></tr><tr><td>Monday</td><td>0.21*</td></tr><tr><td>Tuesday</td><td>0.22**</td></tr><tr><td> $Wednesday^b$ </td><td>0</td></tr><tr><td>Thursday</td><td>0.18</td></tr><tr><td>Friday</td><td>0.55***</td></tr><tr><td>Saturday</td><td>0.93***</td></tr><tr><td>Goodness of fit</td><td></td></tr><tr><td> $R^2$ </td><td>0.30</td></tr><tr><td>ANOVA</td><td>7.03***</td></tr></table>

\*\*\*p<0.01; \*\*p<0.05; \*p<0.10.  
<sup>a</sup> Reference month with a null parameter.  
<sup>b</sup> Reference day with a null parameter.

Table 8  
Optimal pricing decisions in the coffee category.

<table><tr><td></td><td>154</td><td>Bonka</td><td>Marcilla</td><td>Saimaza</td><td>Soley</td><td>Bahia</td></tr><tr><td colspan="7">Assumption</td></tr><tr><td>Unitary cost</td><td>147.58</td><td>165.10</td><td>174.08</td><td>180.46</td><td>163.72</td><td>151.11</td></tr><tr><td colspan="7">Classic model</td></tr><tr><td colspan="7">Optimal price decision</td></tr><tr><td>Price</td><td>178.20</td><td>197.72</td><td>207.19</td><td>212.78</td><td>196.98</td><td>182.34</td></tr><tr><td>Unitary margin</td><td>30.61</td><td>32.62</td><td>33.11</td><td>32.31</td><td>33.26</td><td>31.23</td></tr><tr><td>Percentage margin</td><td>20.74</td><td>19.76</td><td>19.02</td><td>17.91</td><td>20.32</td><td>20.67</td></tr><tr><td colspan="7">Results</td></tr><tr><td>Total sales $^{a}$ </td><td>25.34</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sales $^{a}$ </td><td>2.25</td><td>8.96</td><td>7.87</td><td>2.70</td><td>2.49</td><td>1.07</td></tr><tr><td>Market share</td><td>8.87</td><td>35.35</td><td>31.07</td><td>10.66</td><td>9.81</td><td>4.23</td></tr><tr><td>Total profit $^{a}$ </td><td>825.14</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Profit $^{a}$ </td><td>68.83</td><td>292.19</td><td>260.65</td><td>87.30</td><td>82.70</td><td>33.47</td></tr><tr><td>Profit share</td><td>8.34</td><td>35.41</td><td>31.59</td><td>10.58</td><td>10.02</td><td>4.06</td></tr><tr><td colspan="7">Differential Effects Model</td></tr><tr><td colspan="7">Optimal price decision</td></tr><tr><td>Price</td><td>179.14</td><td>198.06</td><td>206.52</td><td>212.87</td><td>197.06</td><td>182.91</td></tr><tr><td>Unitary margin</td><td>31.55</td><td>32.96</td><td>32.44</td><td>32.41</td><td>33.34</td><td>31.80</td></tr><tr><td>Percentage margin</td><td>21.38</td><td>19.96</td><td>18.63</td><td>17.96</td><td>20.37</td><td>21.04</td></tr><tr><td colspan="7">Results</td></tr><tr><td>Total sales $^{a}$ </td><td>25.29</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sales $^{a}$ </td><td>2.30</td><td>9.10</td><td>7.62</td><td>2.70</td><td>2.49</td><td>1.08</td></tr><tr><td>Market share</td><td>9.08</td><td>35.97</td><td>30.13</td><td>10.69</td><td>9.86</td><td>4.28</td></tr><tr><td>Total profit $^{a}$ </td><td>824.83</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Profit $^{a}$ </td><td>72.45</td><td>299.89</td><td>247.25</td><td>87.62</td><td>83.15</td><td>34.47</td></tr><tr><td>Profit share</td><td>8.78</td><td>36.36</td><td>29.98</td><td>10.62</td><td>10.08</td><td>4.18</td></tr><tr><td colspan="7">Cross-Effects Model</td></tr><tr><td colspan="7">Optimal price decision</td></tr><tr><td>Price</td><td>180.26</td><td>198.33</td><td>203.44</td><td>208.86</td><td>194.42</td><td>179.22</td></tr><tr><td>Unitary margin</td><td>32.68</td><td>33.22</td><td>29.36</td><td>28.40</td><td>30.70</td><td>28.10</td></tr><tr><td>Percentage margin</td><td>22.14</td><td>20.12</td><td>16.87</td><td>15.74</td><td>18.75</td><td>18.60</td></tr><tr><td colspan="7">Results</td></tr><tr><td>Total sales $^{a}$ </td><td>26.56</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sales $^{a}$ </td><td>2.81</td><td>10.24</td><td>7.51</td><td>2.41</td><td>2.26</td><td>1.33</td></tr><tr><td>Market share</td><td>10.59</td><td>38.55</td><td>28.26</td><td>9.06</td><td>8.52</td><td>5.02</td></tr><tr><td>Total profit $^{a}$ </td><td>827.74</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Profit $^{a}$ </td><td>91.93</td><td>340.20</td><td>220.38</td><td>68.32</td><td>69.47</td><td>37.44</td></tr><tr><td>Profit share</td><td>11.11</td><td>41.10</td><td>26.62</td><td>8.25</td><td>8.39</td><td>4.52</td></tr></table>

<sup>a</sup> Calculated assuming the minimum demand seasonal period (October/Monday).

it more sophisticated than any existing explanatory con<sup>fi</sup>guration, such as those that distinguish price effects in terms of national and store brands, low- and high-priced brands, and so forth.

The empirical application of our model to two frequently purchased product categories, one perishable and one nonperishable, con<sup>fi</sup>rms the analytic possibilities of our model. The robust and aggregated nature of this proposal makes it easily applicable by any retail establishment at any time. The empirical application also clari<sup>fi</sup>es the consequences for the retailer if it makes its pricing decisions based solely on a simpli-<sup>fi</sup>ed interpretation of the category's competitive structure. Speci<sup>fi</sup>cally, greater competitive asymmetry will lead to higher cost estimates if the retailer ignores the competitive structure.

Scanner data can provide the information needed to optimize marketing policies in a particular product category, though their ability to do so depends on the accuracy of the market response estimation. The key lies in the measurement models that support the decision model. Explicit modeling of asymmetric competitive effects involves variations in both the optimal prices and the expected results, so ignoring such variance across the categories that constitute a store's retail assortment, especially with regard to frequently purchased products, will mean lost pro<sup>fi</sup>ts.

Table 9  
Optimal pricing decisions in the yoghurt category.

<table><tr><td></td><td>Chamburcy</td><td>Sveltesse</td><td>Danone</td><td>Yoplait</td><td>Clesa</td></tr><tr><td colspan="6">Assumption</td></tr><tr><td>Unitary cost</td><td>20.51</td><td>25.37</td><td>22.23</td><td>19.97</td><td>15.53</td></tr><tr><td colspan="6">Classic model</td></tr><tr><td colspan="6">Optimal price decision</td></tr><tr><td>Price</td><td>28.31</td><td>34.25</td><td>31.27</td><td>28.91</td><td>23.56</td></tr><tr><td>Unitary margin</td><td>7.80</td><td>8.88</td><td>9.04</td><td>8.94</td><td>8.04</td></tr><tr><td>Percentage margin</td><td>38.03</td><td>35.00</td><td>40.66</td><td>44.75</td><td>51.77</td></tr><tr><td colspan="6">Results</td></tr><tr><td>Total sales $^{a}$ </td><td></td><td></td><td>174.5</td><td></td><td></td></tr><tr><td>Sales $^{a}$ </td><td>36.56</td><td>29.42</td><td>73.03</td><td>4.87</td><td>30.32</td></tr><tr><td>Market share</td><td>20.99</td><td>16.89</td><td>41.92</td><td>2.79</td><td>17.40</td></tr><tr><td>Total profit $^{a}$ </td><td></td><td></td><td>1493.84</td><td></td><td></td></tr><tr><td>Profit $^{a}$ </td><td>285.23</td><td>261.29</td><td>660.14</td><td>43.51</td><td>243.67</td></tr><tr><td>Share profit</td><td>19.09</td><td>17.49</td><td>44.19</td><td>2.91</td><td>16.31</td></tr><tr><td colspan="6">Differential effects model</td></tr><tr><td colspan="6">Optimal price decision</td></tr><tr><td>Price</td><td>28.45</td><td>37.07</td><td>31.89</td><td>28.15</td><td>24.80</td></tr><tr><td>Unitary margin</td><td>7.94</td><td>11.70</td><td>9.66</td><td>8.18</td><td>9.28</td></tr><tr><td>Percentage margin</td><td>38.69</td><td>46.10</td><td>43.45</td><td>40.96</td><td>59.74</td></tr><tr><td colspan="6">Results</td></tr><tr><td>Total sales $^{a}$ </td><td></td><td></td><td>156.47</td><td></td><td></td></tr><tr><td>Sales $^{a}$ </td><td>25.91</td><td>31.73</td><td>65.11</td><td>2.52</td><td>31.20</td></tr><tr><td>Market share</td><td>16.56</td><td>20.28</td><td>41.61</td><td>1.61</td><td>19.94</td></tr><tr><td>Total profit $^{a}$ </td><td></td><td></td><td>1515.65</td><td></td><td></td></tr><tr><td>Profit $^{a}$ </td><td>205.61</td><td>371.07</td><td>628.92</td><td>20.65</td><td>289.40</td></tr><tr><td>Profit share</td><td>13.57</td><td>24.48</td><td>41.49</td><td>1.36</td><td>19.09</td></tr><tr><td colspan="6">Cross-effects model</td></tr><tr><td colspan="6">Optimal price decision</td></tr><tr><td>Price</td><td>27.57</td><td>36.73</td><td>31.81</td><td>25.81</td><td>26.12</td></tr><tr><td>Unitary margin</td><td>7.06</td><td>11.35</td><td>9.58</td><td>5.83</td><td>10.60</td></tr><tr><td>Percentage margin</td><td>34.41</td><td>44.75</td><td>43.11</td><td>29.21</td><td>68.27</td></tr><tr><td colspan="6">Results</td></tr><tr><td>Total sales $^{a}$ </td><td></td><td></td><td>158.28</td><td></td><td></td></tr><tr><td>Sales $^{a}$ </td><td>22.60</td><td>33.96</td><td>72.74</td><td>2.65</td><td>26.33</td></tr><tr><td>Market share</td><td>14.28</td><td>21.46</td><td>45.96</td><td>1.67</td><td>16.64</td></tr><tr><td>Total profit $^{a}$ </td><td></td><td></td><td>1536.79</td><td></td><td></td></tr><tr><td>Profit $^{a}$ </td><td>159.50</td><td>385.63</td><td>697.10</td><td>15.45</td><td>279.11</td></tr><tr><td>Share profit</td><td>10.38</td><td>25.09</td><td>45.36</td><td>1.01</td><td>18.16</td></tr></table>

<sup>a</sup> Calculated assuming the minimum demand seasonal period (September/Wednesday).

This study also con<sup>fi</sup>rms the importance of assessing categories to support retail category management. Retailers must attend to the competitive structures of their product categories to determine their optimal prices and thus their expected pro<sup>fi</sup>t. The same marketing actions applied to different brands may elicit different responses from consumers, which is highly signi<sup>fi</sup>cant for determining category-speci<sup>fi</sup>c price structures. Similarly, rivalry between brands differs across the various pairs of brands in a category, but it affects the optimal price structure. Retailers therefore must recognize and understand the complex competitive structure that results from the balance of substitution and complementary relationships among brands within a category. Our <sup>fi</sup>ndings suggest retailers should rely on their own scanner data, input into sophisticated forecasting techniques and decision support models, to obtain optimal solutions. Because optimal category prices depend on many factors beyond the asymmetric competitive effects between brands, including market shares, intrinsic attractiveness, and unitary costs, we assert that no clear patterns for optimal prices exist. In other words, any in<sup>fl</sup>exible rule for <sup>fi</sup>xing prices can be misleading.

Competitive asymmetries may alter the optimal pricing decision, so explicit modeling can improve pro<sup>fi</sup>tability. However, we consider only two kinds of asymmetries, namely, differential effects and crosseffects. An assessment of how the explicit consideration of speci<sup>fi</sup>c cross-effects may improve decision making is beyond of the scope of our analysis, though an approach similar to the one we propose herein could straightforwardly assess the economic impact of ignoring speci<sup>fi</sup>c asymmetric competition effects (e.g., high versus low market share brands; private versus store brands).

Table 10  
Economic analysis for the simpli<sup>fi</sup>ed interpretation of the competitive interaction among coffee brands.

<table><tr><td></td><td>154</td><td>Bonka</td><td>Marcilla</td><td>Saimaza</td><td>Soley</td><td>Bahia</td></tr><tr><td colspan="7">Assumption</td></tr><tr><td>Unitary cost</td><td>147.58</td><td>165.10</td><td>174.08</td><td>180.46</td><td>163.72</td><td>151.11</td></tr><tr><td colspan="7">Differential effects model</td></tr><tr><td colspan="7">Results based on optimal decision with the classic effects model</td></tr><tr><td>Total salesa</td><td>25.34</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Salesa</td><td>2.43</td><td>9.20</td><td>7.40</td><td>2.70</td><td>2.48</td><td>1.11</td></tr><tr><td>Market share</td><td>9.57</td><td>36.32</td><td>29.22</td><td>19.66</td><td>9.81</td><td>4.41</td></tr><tr><td>Total profita</td><td>824.50</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Profita</td><td>74.26</td><td>300.22</td><td>245.15</td><td>87.26</td><td>82.75</td><td>34.86</td></tr><tr><td>Profit share</td><td>9.01</td><td>36.41</td><td>29.73</td><td>10.58</td><td>10.04</td><td>4.23</td></tr><tr><td colspan="7">Cross-effects model</td></tr><tr><td colspan="7">Results based on optimal decision with the classic effects model</td></tr><tr><td>Total salesa</td><td>25.34</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Salesa</td><td>3.20</td><td>10.14</td><td>6.76</td><td>2.11</td><td>2.06</td><td>1.08</td></tr><tr><td>Market share</td><td>12.62</td><td>40.01</td><td>26.67</td><td>8.31</td><td>8.13</td><td>4.25</td></tr><tr><td>Total profita</td><td>822.60</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Profita</td><td>97.86</td><td>330.70</td><td>223.79</td><td>68.06</td><td>68.55</td><td>33.64</td></tr><tr><td>Profit share</td><td>11.90</td><td>40.20</td><td>27.21</td><td>8.27</td><td>8.33</td><td>4.09</td></tr><tr><td colspan="7">Results based on optimal decision with the differential effects model</td></tr><tr><td>Total salesa</td><td>25.30</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Salesa</td><td>3.03</td><td>10.02</td><td>7.02</td><td>2.12</td><td>2.04</td><td>1.06</td></tr><tr><td>Market share</td><td>11.98</td><td>39.63</td><td>27.76</td><td>8.39</td><td>8.08</td><td>4.17</td></tr><tr><td>Total profita</td><td>824.28</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Profita</td><td>95.59</td><td>330.42</td><td>227.79</td><td>68.78</td><td>68.14</td><td>33.57</td></tr><tr><td>Profit share</td><td>11.60</td><td>40.09</td><td>27.63</td><td>8.34</td><td>8.27</td><td>4.07</td></tr></table>

a Calculated assuming the minimum demand seasonal period (October/Monday).

Economic analysis for the simpli<sup>fi</sup>ed interpretation of the competitive interaction among yoghurt brands.

<table><tr><td></td><td>Chamburcy</td><td>Sveltesse</td><td>Danone</td><td>Yoplait</td><td>Clesa</td></tr><tr><td colspan="6">Assumption</td></tr><tr><td>Unitary cost</td><td>20.51</td><td>25.37</td><td>22.23</td><td>19.97</td><td>15.53</td></tr><tr><td colspan="6">Differential effects model</td></tr><tr><td colspan="6">Results based on optimal decision with the classic effects model</td></tr><tr><td>Total sales $^{a}$ </td><td></td><td></td><td>174.20</td><td></td><td></td></tr><tr><td>Sales $^{a}$ </td><td>26.62</td><td>37.97</td><td>71.88</td><td>1.69</td><td>36.05</td></tr><tr><td>Market share</td><td>15.28</td><td>21.79</td><td>41.26</td><td>0.97</td><td>20.70</td></tr><tr><td>Total profit $^{a}$ </td><td></td><td></td><td>1499.37</td><td></td><td></td></tr><tr><td>Profit $^{a}$ </td><td>207.66</td><td>337.18</td><td>649.68</td><td>15.08</td><td>289.76</td></tr><tr><td>Profit share</td><td>13.85</td><td>22.49</td><td>43.33</td><td>1.01</td><td>19.33</td></tr><tr><td colspan="6">Cross-effects model</td></tr><tr><td colspan="6">Results based on optimal decision with the classic effects model</td></tr><tr><td>Total sales $^{a}$ </td><td></td><td></td><td>174.20</td><td></td><td></td></tr><tr><td>Sales $^{a}$ </td><td>24.33</td><td>32.61</td><td>69.56</td><td>0.71</td><td>46.99</td></tr><tr><td>Market share</td><td>13.97</td><td>18.72</td><td>39.93</td><td>0.41</td><td>26.98</td></tr><tr><td>Total profit $^{a}$ </td><td></td><td></td><td>1492.18</td><td></td><td></td></tr><tr><td>Profit $^{a}$ </td><td>189.80</td><td>289.57</td><td>628.76</td><td>6.33</td><td>377.72</td></tr><tr><td>Profit share</td><td>12.72</td><td>19.41</td><td>42.14</td><td>0.42</td><td>25.31</td></tr><tr><td colspan="6">Results based on optimal decision with the differential effects model</td></tr><tr><td>Total sales $^{a}$ </td><td></td><td></td><td>156.47</td><td></td><td></td></tr><tr><td>Sales $^{a}$ </td><td>23.45</td><td>28.31</td><td>65.45</td><td>0.82</td><td>38.44</td></tr><tr><td>Market share</td><td>14.99</td><td>18.09</td><td>41.83</td><td>0.53</td><td>24.56</td></tr><tr><td>Total profit $^{a}$ </td><td></td><td></td><td>1512.66</td><td></td><td></td></tr><tr><td>Profit $^{a}$ </td><td>186.12</td><td>331.14</td><td>632.17</td><td>6.74</td><td>356.49</td></tr><tr><td>Profit share</td><td>12.30</td><td>21.89</td><td>41.79</td><td>0.45</td><td>23.57</td></tr></table>

<sup>a</sup> Calculated assuming the minimum demand seasonal period (September/Wednesday).

This proposal in turn could lead to an analytical management tool that is easy to integrate and use and effectively supports retail management decisions. Such a tool would offer valuable bene<sup>fi</sup>ts for retailers. To design and implement the analytical tool for their speci<sup>fi</sup>c situation, the retailers need to gather scanner data, along with support information that should be available from the retail manager (e.g., displays and feature advertising). Furthermore, they would need the support and cooperation of their retail distributors, which may require them to emphasize the positive implications of this tool, such as the advantages and potential bene<sup>fi</sup>ts of its applications, to managers. The basic information input therefore consists of the retail database and managerial judgments supplied by distributors. The implementation and calibration of this extended tool with actual data is key to con<sup>fi</sup>rming its validity, robustness, and reliability.

With its various assumptions and limitations, our proposed model remains incomplete, but its development and empirical application indicate speci<sup>fi</sup>c areas that require more sophisticated modeling. In particular, we note the need to connect marketing decisions to the cost structure, especially agreements with suppliers (i.e., the manufacturer is a strategic player in pricing decisions); the need to consider different categories, including the complementary and substitutability effects across them, simultaneously; and the need to calculate the response of competing stores and the potential equilibrium state that may lead to an optimal decision.

Furthermore, our empirical results must be interpreted with caution due to our data limitations. Because we ignore other marketing mix variables, our estimations may be biased. Another source of bias in the estimation stems from the potential problems with price endogeneity, which we do not properly address. Several researchers have noted the need to consider endogeneity in <sup>fi</sup>rm marketing decisions in explanatory models of market response (e.g., [5]), and since then, some research contributions have focused on incorporating the decision rules that govern <sup>fi</sup>rms' actions [11,23].

Another limitation pertains to the static nature of our proposed model. Practitioners understand any marketing decisions about a product category from a dynamic perspective; the lagged effects of prices, as well as other marketing variables, should prevent interpretations of prices as representative of time-isolated decisions. For example, Van Heerde and colleagues [40,41]recognize that the growth in sales caused by price promotions results from increased consumption and brand switching, as well as from consumers' anticipation of future purchases. Thus, any maximization of pro<sup>fi</sup>ts in a current period might come at the cost of future pro<sup>fi</sup>ts. Researchers should extend our investigation to determine the sequence of optimal decisions for a product category over an extended period of time.

## Acknowledgments

The authors thank the Spanish Ministry of Education and Science for its <sup>fi</sup>nancial support of the research reported in this paper (Research Project SEJ ECON SEJ2005-06105). The authors also thank two anonymous reviewers for their useful comments and suggestions on previous versions of this article.

## References

[1] G.M. Allenby, A uni<sup>fi</sup>ed approach to identifying, estimating and testing demand structures with aggregate scanner data, Marketing Science 8 (3) (1989) 265–280 {AU: I did not <sup>fi</sup>nd this source in the text but added it to a citation on p. 10; is that placement okay? It will be much easier to add this source in the text than to renumber all the references, so if not, please add it where appropriate}.

[2] G.M. Allenby, P.E. Rossi, Quality perceptions and asymmetric switching between brands, Marketing Science 10 (1971) 185–204.

[3] S. Basuroy, M.K. Mantrala, R.G. Walters, The impact of category management on retailer prices and performance: theory and evidence, Journal of Marketing 65 (4) (2001) 16–32.

[4] D.R. Bell, J. Chiang, V. Padamanabhan, The decomposition of promotional response: an empirical generalization, Marketing Science 18 (4) (1999) 504.

[5] D. Besanko, S. Gupta, D. Jain, Logit demand estimation under competitive pricing behaviour: an equilibrium framework, Management Science 44 (11) (1998) 1533–1547.

[6] B. Bronnenberg, L. Wathieu, Asymmetric promotion effects and brand positioning Marketing Science 15 (4) (1996) 379–394.

[7] R.E. Bucklin, J.M. Lattin, A model of product category competition among grocery retailers, Journal of Retailing 68 (3) (1992) 271–293

[8] G.S. Carpenter, G.S.; L. G. Cooper; D. M. Hanssens and D. F. Midgley. Modeling asymmetric competition, Marketing Science 7 (4) (1988) 393–412.

[9] Y. Chen, J.D. Hess, R.T. Wilcox, Z.J. Zhang, Accounting pro<sup>fi</sup>ts versus marketing pro<sup>fi</sup>ts: a relevant metric for category management, Marketing Science 18 (3) (1999) 208–229.

[10] P.K. Chintagunta, Investigating category pricing behavior at a retail chain, Journal of Marketing Research 39 (2) (2002) 141–154.

[11] P.K. Chintagunta, V. Kadiyali, N.J. Vilcassim, Endogeneity and simultaneity in competitive pricing and advertising: a logit demand analysis, Journal of Business 79 (6) (2006) 2761–2787.

[12] L.G. Cooper, Competitive maps: the structure underlying asymmetric cross elasticities, Management Science 34 (3) (1988) 707–723.

[13] L.G. Cooper, Market-share models, in: J. Eliashberg, G.L. Lilien (Eds.), Marketing, Handbooks in Operations Research and Management Science, vol. 5, Elsevier Science Publishers B.V, North Holland, 1993, pp. 259–314, Amsterdam, 8.

[14] S.K. Dhar, S.J. Hoch, Affective category management depends on the role of the category, Journal of Retailing 77 (2) (2001) 165–184.

[15] K.E. Fish, J.D. Johnson, R.E. Dorsey, J.G. Blodgett, Using an arti<sup>fi</sup>cial neural network trained with a genetic algorithm to model brand share, Journal of Business Research 57 (2004) 79–85.

[16] S. Gupta, Impact of sales promotion on when, what and how much to buy, Journal of Marketing Research 25 (4) (1988) 342–355.

[17] S. Gupta, P. Chintagunta, A. Kaul, D.R. Wittink, Do household scanner data provide representative inferences from brand choices: a comparison with store data, Journal of Marketing Research 33 (4) (1996) 383–398 8.

[18] H. Haghighat, H. Sei<sup>fi</sup>, A.R. Kian, The role of market pricing mechanism under imperfect competition, Decision Support Systems 45 (2) (2008) 267–277 May.

[19] B.A. Harlam, L.M. Lodish, Modeling consumers' choices of multiple items, Journal of Marketing Research 32 (4) (1995) 404–418.

[20] N. Hyun, J. Kyu, Knowledge assisted dynamic pricing for large-scale retailers, Decision Support Systems 28 (4) (2000) 347–363.

[21] B.-D. Kim, R.C. Blattberg, P.E. Rossi, Modeling the distribution of price sensitivity and implications for optimal retail pricing, Journal of Business and Economic Statistics 13 (3) (1995) 291–303.

[22] L. Krishnamurthi, S.R. Raj, K. Sivakumar, Unique inter-brand effects of price on brand choice, Journal of Business Research 34 (1995) 47–56.

[23] P. Manchanda, P.E. Rossi, P.K. Chintagunta, Response modeling with nonrandom marketing-mix variables, Journal of Marketing Research 41 (4) (2004) 467–478.

[24] C. Manski, The structure of random utility models, Theory and Decision 8 (1977) 229–254.

[25] M.K. Mantrala, P.B. Seetharaman, R. Kaul, S. Gopalakrishna, A. Stam, Optimal pricing strategies for an automotive aftermarket retailer, Journal of Marketing Research 43 (4) (2006) 588–604.

[26] B.W. Marion, Competition in grocery retailing: the impact of new strategic group on price increases, Review of Industrial Organization 13 (4) (1998) 281–299.

[27] D. McFadden, Conditional logit analysis of qualitative choice behavior, in: P. Zarembka (Ed.), Frontiers in Econometrics, Academic Press, New York, 1974, pp. 105–142.

[28] C. Mela, K. Jedidi, D. Bowman, The long term impact of promotions on consumer stockpiling behavior, Journal of Marketing Research 35 (2) (1998) 250–262.

[29] A.L. Montgomery, Creating micro-marketing pricing strategies using supermarket scanner data, Marketing Science 16 (4) (1997) 315–337.

[30] C. Narasimhan, S.A. Neslin, S.K. Sen, Promotional elasticities and category characteristics, Journal of Marketing 60 (1996) 17.

[31] D.J. Reibstein, H. Gatignon, Optimal product line pricing: the in<sup>fl</sup>uence of elasticities and cross-elasticities, Journal of Marketing Research 21 (3) (1984) 259–267.

[32] G.J. Russell, A model of latent symmetry in cross-price elasticities, Marketing Letters 3 (1992) 157–169.

[33] S. Sayman, J.S. Raju, Investigating cross-category effects of store brands, Review of Industrial Organization 24 (2) (2004) 129–141.

[34] R. Sethuraman, A meta-analysis of national brand and store brand cross-promotional price elasticities, Marketing Letters 6 (4) (1995) 275–286.

[35] R. Sethuraman, V. Srinivasan, D. Kim, Asymmetric and neighborhood cross-price effects: some empirical generalizations, Marketing Science 18 (1) (1999) 23–41.

[36] K. Sivakumar, Price-tier competition: distinguishing between intertier competition and intratier competition, Journal of Business Research 56 (2003) 947–959

[37] K. Sivakumar, Manifestation and measurement of asymmetric brand competition, Journal of Business Research 57 (2004) 813–820.

[38] K. Sudhir, D. Talukdar, Does store brand patronage improve store patronage? Review of Industrial Organization 24 (2) (2004) 143–160.

[39] G.J. Tellis, F.S. Zufryden, Tackling the retailer decision maze: which brands to discount, how much, when and why? Marketing Science 14 (3) (1995) 271–299.

[40] H.J. Van Heerde, P.S.H. Lee<sup>fl</sup>ang, D.R. Wittink, The estimation of pre- and postpromotion dips with store-level scanner data, Journal of Marketing Research 37 (3) (2000) 383–395.

[41] H.J. Van Heerde, P.S.H. Lee<sup>fl</sup>ang, D.R. Wittink, Is 75% of sales promotion bump due to brand switching? No, only 33% is, Journal of Marketing Research 40 (4) (2003) 481–491.

[42] N.J. Vilcassim, P.K. Chintagunta, Investigating retailer product category pricing from household scanner panel data, Journal of Retailing 71 (2) (1995) 103–128.

[43] R.G. Walters, Assessing the impact of retail price promotions on product substitution, complementary purchase, and interstore sales displacement, Journal of Marketing 55 (2) (1991) 17–28.

[44] R.G. Walters, W. Bommer, Measuring the impact of product and promotionrelated factors on product category price elasticities, Journal of Business Research 36 (1996) 203–216.

[45] M.J. Zenor, The pro<sup>fi</sup>t bene<sup>fi</sup>ts of category management, Journal of Marketing Research 31 (2) (1994) 202–213.

Óscar González-Benito is Full Professor at the Área of Comercialización e Investigación de Mercados of the University of Salamanca (Spain). He has participated in different Conferences and Seminars worldwide as a presenter, reviewer and chairman. He has written several articles in different international journals with a high standing impact (e.g. Journal of Retailing, British Journal of Management, Journal of the Operational Research Society, Marketing Letters, etc.). His main research lines are retailing, distribution and operations management. Member of the European Marketing Academy (EMAC).

María Pilar Martínez-Ruiz is Associate Professor at the Department of Marketing of the University of Castilla-La Mancha (Spain). She has participated in different Conferences and Seminars worldwide and has written several articles in different high standing international journals (e.g., The International Journal of Market Research, Journal of the Operational Research Society, European Journal of Marketing, etc.). Her main research lines are retailing, marketing communications, sales promotions and product and services innovation. Member of the following associations: Academy of Marketing Science (AMS), European Marketing Academy (EMAC) and The European Association for Education and Research in Commercial Distribution (EAERCD).

Alejandro Mollá-Descals is Full Professor at the Department of Comercialización e Investigación de Mercados of the University of Valencia (Spain). He has participated in different Conferences and Seminars worldwide and has written several articles in different international journals with a high standing impact (e.g. Journal of the Operational Research Society, International Journal of Market Research, etc.). His main research lines are retailing, distribution and consumer research. Member of the European Marketing Academy (EMAC).
