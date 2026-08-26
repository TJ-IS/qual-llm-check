---
otero_id: 21862
otero_key: "Z9KZEU5G"
title: "Knowledge assisted dynamic pricing for large-scale retailers"
authors: "Nahk Hyun Sung; Jae Kyu Lee"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00095-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge assisted dynamic pricing for large-scale retailers

Nahk Hyun Sung <sup>a,1</sup>, Jae Kyu Lee <sup>b,)</sup>

<sup>a</sup> School of Management, Yongin UniÕersity, 117-6 Samgadong, Yongin, Kyunggido, 449-714, South Korea <sup>b</sup> MIS Program Graduate School of Management, Korea AdÕanced Institute of Science and Technology, 207-43 Cheongryang, Dongdaemun-ku, Seoul 130-012, South Korea

## Abstract

It is very difficult for large-scale retailers to price thousands of items dynamically reflecting all constraints and policies. To solve this problem, we adopt a combined model approach that contingently selects appropriate pricing models and integrates them. The three proposed models are cost-plus, competitor-referenced, and demand-driven models. Since each model can be converted to a set of interval and point constraints, we have developed price point determination rules, which find a price point from the weighted interval and point constraints. A prototype system, Knowledge-Assisted Pricing Assistant KAPA is developed with this idea. According to our experiment involving 76 cases with 54 pricing experts,Ž . KAPA performed consistently, with human experts, about 89.5% accurate. This approach can be a very effective pricing scheme in the electronic marketing era. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Retail pricing models; Expert systems; Price point determination rules

## 1. Introduction

It is very difficult for large-scale retailers to price tens of thousands of items dynamically reflecting all constraints and policies. This is particularly true in the electronic marketing environment where our prices and our competitors are open and easily collectable. Let’s consider the following decision-making situation that supermarket managers face.

A supermarket manager, Susan, wants to set the price of ‘‘Choice Coffee 100 g bottled.’’ Its purchasing cost is US\$3.00, and the current price US\$3.70. A guideline from the merchandising division is to add the average markup rate of the category to the purchasing cost of the item. Suppose a common markup rate of instant coffee category is 33.3%, then the price should be set at US\$4.00. Susan noticed that the prices of three key competitors are US\$3.40, US\$3.75, and US\$3.80, respectively. In this situation, she feels that she should set the price at the level of a medium priced competitor, US\$3.75. Susan has also an intuition about the optimal price that can maximize the profit considering the implicit demand curve, and feels that the price should be cut to US\$3.50. Now, how should Susan set the price of the item reconciling the three conflicting principles?

Management of chain stores has many pricing policies that need quick and consistent implementation in the market. Management counts on daily judgment of pricing experts, which seems impossible to implement without systematic support. To automate or at least to support the judgmental process,Ž . we need to devise an integrated model that can combine several conflicting price modeling principles.

To solve this problem, we need to establish the basic pricing models, and set them up so that they are applicable in the hierarchies of merchandise and stores. Since the pricing model of a specific item in a particular store can be represented as a set of weighted interval and point constraints, we need to develop an algorithm that can find the most reasonable point from the weighted constraints. For this purpose, we develop price point determination rules.

This approach is applied to a leading supermarket chain in Korea called Hanwha, and a prototype expert system named Knowledge-Assisted Pricing Assistant KAPA is developed. The performanceŽ . was evaluated through a database of 76 cases of an item, and we found that KAPA performed consistently with human experts at a rate of about 89.5%. This result assures that this approach is applicable to large-scale retailers, either online or traditional.

This paper is organized as follows: In Section 2, we review the previous research for retail pricing. Section 3 describes the three pricing models, and Section 4 describes the contingency of applying retail pricing models and the integration process. In Section 5, the process of inheriting values to the integrated pricing model is explained with an illustrative example. In Section 6, the weight functions of pricing models are described, and in Section 7, price point determination rules to solve the integrated pricing model is proposed and an example is given. Section 8 describes the architecture and knowledgerepresentation scheme of the KAPA system. Section 9 presents experimental performance of KAPA in comparison with human experts in the Hanwha Supermarket Chain.

## 2. Previous research on pricing

Previous research for appropriate pricing can be classified into two categories: mathematical approaches and knowledge-based approaches. Traditional approaches have mainly focused on the formulation of mathematical programming models <sup>w</sup> <sup>x</sup> 4,5,10–12,15,16 . For instance, the optimal price of an item can be computed from the Niehan’s formula in 1Ž .

$$
p_{i}^{*} = \frac{\varepsilon_{i}}{1 + \varepsilon_{i}}\Delta c_{i} - \sum_{\substack{j = 1\\ j\neq i}}^{n}\big(p_{j} - \Delta c_{j}\big)\frac{\varepsilon_{ij}}{1 + \varepsilon_{i}}\frac{q_{j}}{q_{i}}\tag{1}
$$

where ${ p } _ { i } ^ { * }$ is the optimal price of item i, $\varepsilon _ { i }$ is the price elasticity of item i, $\varepsilon _ { i j }$ is the cross-price elasticity of item j by the price of item i, p is the price, $\varDelta c$ is the marginal cost, and q is the sales quantity.

This model is theoretically sophisticated. However, to apply the formula in reality, we have to estimate the price elasticity of each item and the cross price elasticity between the items. Since chain-store retailers handle so many items, it is impossible to estimate the elasticity of whole items in all the stores 13,21 . So the only choice left to us<sup>w</sup> <sup>x</sup> is the pricing expert’s judgment.

Despite the abundant use of expert systems in marketing 1,6,14,17–20 , very few have attempted <sup>w</sup> <sup>x</sup> retail pricing. Pizzano 17,20 and Sisodia and <sup>w</sup> <sup>x</sup> Warkentin 20 developed a pricing expert system<sup>w</sup> <sup>x</sup> named Pricing Strategy Advisor. The system supports the pricing of diverse industries. They reported that most evaluators rated the performance of the system the same as the level of senior manager. Casey and Murphy 7 developed an expert system for pricing new products. They reported that the system generated appropriate recommendations at 80% of accuracy. Singh and Bennavail 19 have<sup>w</sup> <sup>x</sup> proposed a retail pricing system named Price-Strat, which seeks profitable prices during price wars. The model was applied to the pricing of gasoline, car washes, and automobiles, and it reported improved profitability.

However, the above three knowledge-based pricing systems are not developed for the large-scale retailers. The pricing system for large-scale retailers requires additional features, because management cannot determine the entire pricing policy of items at a store level. So inheritance of policy through the hierarchies of merchandise and stores is an essential step in the large-scale retailer’s pricing.

## 3. Basic pricing models

In this section, we propose three pricing models. The adopted pricing models are the cost-plus model, the competitor-referenced model, and the demanddriven model 3,9,13,21 . Our targeted price is the <sup>w</sup> <sup>x</sup> price of a specific item in a store of a retailer’s chain.

## 3.1. Cost-plus model

Retailers use markups and markup rates as measures of profit. A markup is the difference between merchandise cost and price. The merchandise cost in retailing usually means the purchasing cost. The markup rate is the percentage of markup divided by the cost 3,9,13 . According to this model, the price <sup>w</sup> <sup>x</sup> can be determined by setting the markup rate as model 2 .Ž .

$$
P _ {i s} ^ {\alpha} = c _ {i} \big (1 + \alpha_ {i s} \big)\tag{2}
$$

where i is the item, $i = 1 , \ldots , m ,$ , s is a store in the retailer’s chain, $p$ is the price, c is the cost, is the markup rate, and the superscript  implies the result by the cost-plus model.

The target markup rate can be set at various levels. We can think of two types of hierarchies: merchandise and store. Commonly adopted merchandise levels are department, class, category, and item. The store can have higher level of store-group as illustrated in Fig. 1 in Section 5.

In this sense, the markup rate of an individual item at a specific store needs inheritance from more than one upper level. So a scheme to reconcile multiple inheritances needs to be devised in this model as described in Section 5.

## 3.2. Competitor-referenced model

The second model — the competitor referenced model — considers the competitors’ prices in comparison with our store’s price image policy.

The price image of a store is the perception that customers have about the overall price level of the store. A store manager usually sets the price image of the store considering customer characteristics and a typical competitor’s price image policy. If the price image of a store is the same as that of a competitor, a common rule is to set to the same price as that of the competitor. However, if the price image of the store is relatively lower higher than that of the competi-Ž . tor, the price should be set at a rate that is lower Ž . higher than the competitor’s. This competitor-referenced model can be expressed as the following equations Eqs. 3 and 4 .Ž Ž . Ž ..

$$
p _ {i s} ^ {\beta} = f \left(p _ {i \mid j}, j = 1, \dots , n\right)\tag{3}
$$

$$
p _ {i \mid j} = p _ {i j} \left(1 - \beta_ {s j}\right)\tag{4}
$$

where j is the competitors, $\mathbf { j } = 1 , \ldots , n , \ p _ { i \mid j }$ is the suggested price of item i considering competitor $j ^ { \prime } s$ price, $\beta _ { s j }$ is the price image of competitor j minus the price image of store s and the superscript $\beta$ implies the result by the competitor-referenced model.

The price image may be established a priori by a policy, or evaluated a posteriori by statistics. To compute and evaluate the store’s price image a posteriori, we can compare the relative average price level of the store against that of a competitor j as Ž . Eq. 5 .

$$
\beta_ {s j} = \sum_ {i = 1} ^ {m} \left(p _ {i j} / p _ {i s}\right) \left(q _ {i s} / \sum_ {i = 1} ^ {m} q _ {i s}\right) - 1\tag{5}
$$

In practice, the items for price comparison should be selected among items that are comparable with each other and typical enough. When the price image is classified into multiple levels, we need to match the ordinal level with the computable $\beta$ value. For instance, suppose we have classified the price image into three levels: low, medium, and high. Suppose the price image level of our store s is medium. Then, we can classify a competitor as a low-price image competitor LPIC if Ž . $\beta _ { s j } < - 0 . 0 4 ;$ a medium-price image competitor MPIC i Ž . $\mathrm { ~ : ~ } - 0 . 0 4 \leq \beta _ { s i } \leq 0 . 0 4 ;$ and a high-price image competitor HPIC ifŽ . $\beta _ { s j } > 0 . 0 4$ The boundary value 0.04 may vary depending upon the store’s definition of the price image difference.

{ department-07 is-a: department description: processed foods alpha: 0.25 gamma: 0.02 weight-of-alpha: 30 weight-of-negative-gamma: 48 weight-of-positive-gamma: 39}

![](/api/attachments/Z9KZEU5G/fulltext/images/c97e33e38dd52403f286620a6558c848629fdcab2b24add95debdf70c58ba7d0.jpg)

```yaml
{ class-0713
    is-a: class
    description: coffee
    department-of: department-07
    alpha: 0.30
    gamma: 0.03
    weight-of-alpha: 27
    weight-of-negative-gamma: 44
    weight-of-positive-gamma: 40 }
    { category-071301
    is-a: category
    description: instant coffee
    class-of: class-0713
    alpha: 0.333
    gamma: 0.04
    weight-of-alpha: 27
    weight-of-negative-gamma: 44
    weight-of-positive-gamma: 40 }
    { item-8801055000043
    is-a: item
    description: Choice Coffee 100g bottled
    category-of: category-071301
    cost: 3.00
    alpha: 0.333
    gamma: 0.04
    weight-of-alpha: 40
    weight-of-negative-gamma: 52
    weight-of-positive-gamma: 34 }
    { item-8801055000043-store(Seoul-KAIST)
    is-a: item-of-store
    description: Choice Coffee 100g bottled
    category-of: 071301
    current-price: 3.70
    sales-grade: A
    cost: 3.00
    alpha: 0.333
    beta(x): -0.05
    beta(y): 0.02
    beta(z): 0.05
    gamma: 0.05
    weight-of-alpha: 45
    weight-of-beta(x): 55
    weight-of-beta(y): 68
    weight-of-beta(z): 53
    weight-of-negative-gamma: 49
    weight-of-positive-gamma: 37 }
```  
Fig. 1. Multiple inheritance through the hierarchies of merchandise and stores bold characters represent the inherited values .Ž .

## 3.2.1. Sales grade and weight of competitors

When there is more than one competitor, the competitor-referenced price may be derived as a weighted combination of each competitor’s impact. It is our observation that the weight is significantly influenced by sales grade of the items. Usually retailers perform ABC analysis to distinguish fast-selling items from slow-selling ones. In the Hanwha case, an item is classified in the sales grade A if it belongs to the top 75% of sales contribution, B to the next 20%, and C to the bottom 5%.

Table 1  
Relative weights of competitors by sales grade of item

<table><tr><td>Sales grade</td><td>LPIC</td><td>MPIC</td><td>HPIC</td></tr><tr><td>A</td><td>55</td><td>68</td><td>53</td></tr><tr><td>B</td><td>45</td><td>75</td><td>62</td></tr><tr><td>C</td><td>35</td><td>58</td><td>71</td></tr></table>

Recall that we assume the price image level of store s is medium. With the sales-grade A items, customers tend to be more sensitive to price. So the price of a LPIC should be considered with a higher weight. With B or C items, customers are relatively less sensitive to price. So the MPIC should have a higher weight for the cases of B items, and the HPIC for the cases of C items. Table 1 illustrates the weight of competitors depending upon the sales grade. The illustrative weight is derived from the experts’ opinion studied in Section 9. The effect of a store-level price image needs to be inherited to the items in the store.

## 3.3. Demand-driÕen model

In the demand-driven model, the prices are judged to implicitly maximize profit or sales. The benefit of the demand-driven model is that it reflects the expected price sensitivity. The price change by the demand-driven model can be expressed as Eq. 6Ž .

$$
p _ {i s} ^ {\gamma} = p _ {i s} (1 + \gamma_ {i s})\tag{6}
$$

where $\gamma$ is the changed markup rate to maximize profit, and the superscript $\gamma$ implies the result by the demand-driven model.

Usually, the experts decide the direction of $\gamma$ with the conceptual model in mind such as:

$$
\begin{array}{l l l} \gamma_ {i s} > 0 & \text {if} & \varepsilon_ {i s} <   - 1 - l _ {s} \\ \gamma_ {i s} = 0 & \text {if} & - 1 - l _ {s} \leq \varepsilon_ {i s} \leq - 1 + l _ {s} \\ \gamma_ {i s} <   0 & \text {if} & \varepsilon_ {i s} > - 1 + l _ {s} \end{array}
$$

where is the price elasticity, l is the bound of price elasticity that maintains the current price $( l _ { s } >$ 0 ..

As mentioned earlier, the precise dynamic estimation of the demand curve for thousands of items is impossible to implement. In practice, sales managers are obliged to judge the direction of price change and its magnitude.

## 4. Contingent selection and integration of models

## 4.1. Use releÕant models by aÕailable data

The above three pricing models have their own foundation and appropriate situation to apply. The cost-plus model can be used during the introduction stage of an item without any serious competitors. The competitor-referenced model can be used when we know the competitors’ prices. The demand-driven model can be used when there exist experts who can judge the demand curve and substitution effects. To take advantages of three models, we need to select appropriate models depending upon the situation, and integrate them in reconciliation of the conflicting principles. Typical factors that determine the situation for model selection are whether the item is a new or existing one and whether a store has competitors or not as summarized in Table 2 .

Table 2  
Situations and relevant models

<table><tr><td rowspan="2">Item</td><td colspan="2">Store</td></tr><tr><td>Without competitors</td><td>With competitors</td></tr><tr><td>New item</td><td>Cost-plus model ( $w^{\alpha} \geq 0, w^{\beta} = w^{\gamma} = 0$ )</td><td>Cost-plus modelCompetitor-referenced model ( $w^{\alpha} \geq 0, w^{\beta} \geq 0, w^{\gamma} = 0$ )</td></tr><tr><td>Existing item</td><td>Cost-plus modelDemand-driven model ( $w^{\alpha} \geq 0, w^{\beta} = 0, w^{\gamma} \geq 0$ )</td><td>Cost-plus modelCompetitor-referenced modelDemand-driven model ( $w^{\alpha} \geq 0, w^{\beta} \geq 0, w^{\gamma} \geq 0$ )</td></tr></table>

## 4.2. Integration of models

Since the three models suggest different prices, we need to integrate them into a combined model. The models can be integrated in several ways. In this study, we adopt a weighted linear additive model as Ž . Eq. 7 2,8 : <sup>w</sup> <sup>x</sup>

$$
\begin{array}{l} \hat {p} _ {i s} = w _ {i s} ^ {\alpha} \left\{c _ {i} (1 + \alpha_ {i s}) \right\} + \sum_ {j = 1} ^ {n} w _ {s j} ^ {\beta} \left\{p _ {i j} (1 - \beta_ {s j}) \right\} \\ \quad + w _ {i s} ^ {\gamma} \left\{p _ {i s} (1 + \gamma_ {i s}) \right\} \end{array}\tag{7}
$$

where, $\hat { p }$ is the suggested price from the combined model, ${ w _ { i s } ^ { \alpha } }$ is the weight of cost-plus model, $w _ { s j } ^ { \beta }$ is the weight of competitor $j , \ j = 1 , \ldots , n$ , and $w _ { i s } ^ { \dot { \gamma } }$ is the weight of demand-driven model.

Note that the weights for irrelevant models in Table 2 are zero. The weights may be given as points or functions see Section 6 for weight function . Ž . There are some reasonable methods of determining the weights. The first method is determination by policy. Management may decide the weights with purpose. The second method is determination by the average score of experts’ weights. In this case, we need to study how the experts judge the optimal weights. The third method might be determination by learning. In this study, we adopt the second method as illustrated in Section 9

## 5. Multiple inheritances of values

To derive the values $( \alpha , \beta , \gamma , w ^ { \alpha } , w ^ { \beta }$ , and $w ^ { \gamma } )$ in model 7 for a specific item in a specific store, Ž . we need to inherit them from the upper classes. There are two types of hierarchies in retailing: merchandise and store 9,13 .<sup>w</sup> <sup>x</sup>

In most supermarket business, the merchandise is classified into four levels: department, class, category, and item. Departments classify the merchandise into processed foods, vegetables, fruits, beverages, etc. The processed-foods department is broken down into classes of coffee, noodles, milk, etc. The class of coffee is segmented into categories of instant coffee, canned coffee, and bean coffee. The instant coffee category has items like ‘‘Choice Coffee 100 g bottled’’, ‘‘Choice Coffee 175 g bottled’’, ‘‘Maxim Original Blend 175 g bottled’’, etc.

The other dimension of aggregation is the hierarchy of stores. A large supermarket chain usually has hundreds of stores. So management of the supermarket chain usually sets pricing policies at the level of store groups possibly classified by the price image level and<sup>r</sup>or regional characteristics. In addition, store managers set pricing strategies at its own store level. Refer to the illustrative inheritances in Figs. 1 and 2. We can see that there are multiple inheritances from upper levels and from different hierarchies. So we need to set resolution rules. To resolve the conflict between different levels, we adopt the lowest-leÕel-first strategy. To resolve the conflict from different hierarchies, we need to set a resolution rule as illustrated in Table 3. The smaller number means higher priority. For instance, to inherit , the merchandise hierarchy has higher priority than the store hierarchy.

Selective inheritance means to inherit from the highest prioritized source. In this manner, the values for the item ‘‘Choice Coffee 100 g bottled’’ at the Seoul-KAIST store can be derived as the frame in the bottom of Fig. 1. Suppose we have three competitors x, y, and z who have low, medium, and high price image levels respectively, as illustrated in Fig. 2.

In this example, the ‘‘Choice Coffee 100 g bottled in the store Seoul-KAIST ’’ is represented as anŽ . instance ‘‘item-8801055000043-store Seoul-Ž KAIST ’’, and it inherits slot values from both the. merchandise hierarchy and the store hierarchy. The values for cost,  and  are inherited from the category and item frames, and the values for $\beta _ { s x } ,$ $\beta _ { s y } , ~ \bar { \beta _ { s z } } , ~ w ^ { \alpha } , ~ w _ { x } ^ { \beta } , ~ w _ { y } ^ { \beta } , ~ w _ { z } ^ { \beta } ,$ , and $w ^ { \gamma }$ from the store Ž . Seoul-KAIST frame.

The store inherits competitor-related values $( \beta _ { s x } ,$ $\beta _ { s y } , \beta _ { s z }$ , and price image levels from the competi- .

tor frames as illustrated in Fig. 2. In this manner, we can define the values for the model in Eq. 7 at anŽ . item-in-a-store level.

## 6. Weight functions

The weights may be treated as point values or functional forms. Since the preference of changing the values of $\alpha , \beta ,$ and  is gradual, we adopt the functional form. Three simple weight functions that we can adopt are a triangle, rectangle, and sloped linear line. The triangle means the symmetric preference around a point; the rectangle means the flat preference for the interval, and the sloped linear line means a directional asymmetric preference.

In this study, we adopt the triangular weight function for $w ^ { \alpha }$ , rectangular weight function for $w ^ { \beta } ,$ and sloped linear line for $w ^ { \gamma } .$

The weight function of $w ^ { \alpha }$ is depicted as Fig. 3. This figure means that $c ( 1 + \alpha )$ has the highest weight value $w ^ { \alpha }$ , and its neighbor has gradually degraded weights. So to define the weight function $w ^ { \alpha } ( p ) .$ , we additionally need to specify the range . This triangular weight function for item i can be represented in notational form as $w _ { i s } ^ { \alpha } ( p ) =$ TRIANGLE $[ c _ { i s } , \alpha _ { i s } , w _ { i s } ^ { \alpha } , \lambda _ { i s } ] .$

The triangular weight function $w _ { i s } ^ { \alpha } ( p )$ can be mathematically defined as Eq. 8 .Ž .

$$
w _ {i s} ^ {\alpha} (p) = \left\{ \begin{array}{l l} 0 & i f p \leq c _ {i} \left(1 + \alpha_ {i s} - \lambda_ {i s}\right) \\ \frac {w _ {i s} ^ {\alpha}}{c _ {i} \lambda_ {i s}} \left(p - c _ {i} - c _ {i} \alpha_ {i s} + c _ {i} \lambda_ {i s}\right) & i f c _ {i} \left(1 + \alpha_ {i s} - \lambda_ {i s}\right) <   p \leq c _ {i} \left(1 + \alpha_ {i s}\right) \\ - \frac {w _ {i s} ^ {\alpha}}{c _ {i} \lambda_ {i s}} \left(p - c _ {i} - c _ {i} \alpha_ {i s} - c _ {i} \lambda_ {i s}\right) & i f c _ {i} \left(1 + \alpha_ {i s}\right) <   p \leq c _ {i} \left(1 + \alpha_ {i s} + \lambda_ {i s}\right) \\ 0 & i f p > c _ {i} \left(1 + \alpha_ {i s} + \lambda_ {i s}\right) \end{array} \right.\tag{8}
$$

The rectangular weight functions of a competitor-referenced model with three competitors Ž . x, y, and z are depicted in Fig. 4. The weight function is determined depending upon the store’s and competitors’ price image levels. Recall that our store’s price image level is medium. For the LPIC x, the price of store s has to be higher than $p _ { i x }$ . This can be represented as a rectangular weight function between $p _ { i }$ and $p _ { i x } ( 1 - \beta _ { s x } )$ . For the MPIC y whose price image is the same as that of the store s, managers feel like adjusting between $p _ { i _ { ) } }$ and $p _ { i s } .$ For the HPIC $z , p _ { i s }$ has to be lower than $p _ { i z } ,$ so it needs adjustment between $p _ { i z }$ and $p _ { i z } ( 1 - \beta _ { s z } )$ . The weight function of a competitor-referenced model against competitor j can be simply denoted as w pŽ .<sup>s</sup>RECTANGLE $[ p _ { i s } , p _ { i j } , \beta _ { s j } , w _ { i s j } , j = x , y , z ] .$

The weight function of a competitor-referenced model can be mathematically defined as Table 4 depending upon the price images of the store and its competitors.

We adopt the sloped linear weight function for the demand-driven model. Suppose the value is judged by pricing experts. Then the slope of the weight function is positive or negative depending upon the sign of  value. If the slope is positive, it implies a markup. If the slope is negative, it implies a markdown. Each case is depicted in Fig. 5 a and b Ž . Ž . respectively. This means that the targeted point is given the highest weight. The $w _ { i s } ^ { \gamma } ( p )$ can be simply denoted as $S L O P E [ p _ { i s } , \gamma _ { i s } , w _ { i s } ^ { \gamma } ]$

A mathematical form of the sloped linear weight functions can be represented as 9a and b .Ž . Ž .

Markup Adjustment $( \gamma _ { i s } > 0 )$

$$
w _ {i s} ^ {\gamma} (p) = \left\{ \begin{array}{l l} 0 & \text { if } p <   p _ {i s} \\ \frac {w _ {i s} ^ {\gamma}}{p _ {i s} \gamma_ {i s}} (p - p _ {i s}) & \text { if } p _ {i s} \leq p \leq p _ {i s} (1 + \gamma_ {i s}) \\ 0 & \text { if } p > p _ {i s} (1 + \gamma_ {i s}) \end{array} \right.\tag{9a}
$$

```yaml
{price-8801055000043-competitors
    is-a: price-of-competitors
    description: Choice Coffee 100g bottled
    price-of-competitor(x): 3.40
    price-of-competitor(y): 3.75
    price-of-competitor(z): 3.80 }

{competitor(x)
    is-a: competitor
    competitor-of: Store(Seoul-KAIST)
    description: Good Morning Store
    beta: -0.05; lower than -0.04
    price-image-level: low }

{competitor(y)
    is-a: competitor
    competitor-of: Store(Seoul-KAIST)
    description: Family Store
    beta: 0.02; between -0.04 and 0.04
    price-image-level: medium }

{competitor(z)
    is-a: competitor
    competitor-of: Store (Seoul-KAIST)
    description: Lucky Store
    beta: 0.05; larger than 0.04
    price-image-level: high }
```  
Fig. 2. Competitors’ prices of the item-code ‘8801055000043’ and their price-image-levels.

Markdown Adjustment $( \gamma _ { i s } < 0 )$

$$
w _ {i s} ^ {\gamma} (p) = \left\{ \begin{array}{l l} 0 & \text {   if   } p <   p _ {i s} (1 - \gamma_ {i s}) \\ - \frac {w _ {i s} ^ {\gamma}}{p _ {i s} \gamma_ {i s}} (p - p _ {i s}) & \text {   if   } p _ {i s} (1 - \gamma_ {i s}) \leq p \leq p _ {i s} \\ 0 & \text {   if   } p > p _ {i s} \end{array} \right.\tag{9b}
$$

Table 3 Illustrative priority of inheriting values

<table><tr><td rowspan="2">Level of hierarchy</td><td colspan="3">Values</td></tr><tr><td>Cost-plus model  $\alpha, w^{\alpha}$ </td><td>Competitor-referenced model  $\beta, w^{\beta}$ </td><td>Demand-driven model  $\gamma, w^{\gamma}$ </td></tr><tr><td>Store</td><td></td><td></td><td></td></tr><tr><td>Store group</td><td>6</td><td>2</td><td>3</td></tr><tr><td>Store</td><td>5</td><td>1</td><td>1</td></tr><tr><td>Merchandise</td><td></td><td></td><td></td></tr><tr><td>Department</td><td>4</td><td>6</td><td>6</td></tr><tr><td>Class</td><td>3</td><td>5</td><td>5</td></tr><tr><td>Category</td><td>2</td><td>4</td><td>4</td></tr><tr><td>Item</td><td>1</td><td>3</td><td>2</td></tr></table>

The next step is the integration of weight functions from these three models. The integrated weight functions for the ‘‘Choice Coffee 100 g bottled’’ case are illustrated in Fig. 6.

## 7. Price point determination rules

Now our concern is how to select a price point from the integrated weight functions as in Fig. 6. So we need to establish rules, namely price point determination rules. A reasonable rule is to find the point with the largest cumulative weight as illustrate in Fig. 7.

In this example, the interval 3.70, 3.75 has the<sup>w</sup> <sup>x</sup> largest cumulative weight, 121. If the highest weight is a point, the point is a suggested price by model

![](/api/attachments/Z9KZEU5G/fulltext/images/fd0cdccd1a3d57ae2bdc7261f3193dab8beed1ce699d97c3eaa51ae9a06958fe.jpg)  
Fig. 3. Triangular weight function of cost-plus model.

![](/api/attachments/Z9KZEU5G/fulltext/images/ced0342bf43e3f9b6f7260bde80413c37645f0c91b5bb4c041cddb17ea36bf7d.jpg)  
Fig. 4. Rectangular weight function of competitor-referenced model.

Ž . Ž 7 . However, if the highest weight is an interval or intervals , we have to set a rule to select a point from. the interval.

The first rule for the existing items is to select the point nearest to the current price. The second rule for new items is to select the point nearest to what the cost-plus model suggests. The third rule might be to select the center of the interval. In this study, we adopt the first and second rules. According to these rules, the current price US\$3.70 is suggested as the best price.

## 8. Implementation of KAPA

## 8.1. Architecture of KAPA

To implement the combined model and the price point determination rules, we have developed an experimental system named KAPA whose architecture is depicted in Fig. 8.

The knowledge base is composed of databases and rule bases. Databases are composed of merchandise, stores, and competitors databases. The databases were illustrated in Figs. 1 and 2.

Rectangular weight functions between the relative price images

<table><tr><td rowspan="2">Price Image</td><td colspan="5">Ours</td></tr><tr><td colspan="2">Low</td><td colspan="2">Medium</td><td>High</td></tr><tr><td colspan="6">Competitors&#x27;</td></tr><tr><td>Low (e.g. x)</td><td colspan="2"> $\begin{cases} 0 & \text{ifp} < p_{is} \\ w_{ix}^{\beta} & \text{ifp}_{is} \leq p \leq p_{ix} \\ 0 & \text{ifp} > p_{ix} \end{cases}$ </td><td colspan="2"> $\begin{cases} 0 & \text{ifp} < p_{ix} \\ w_{ix}^{\beta} & \text{ifp}_{ix} \leq p \leq p_{ix}(1 - \beta_{sx}) \\ 0 & \text{ifp} > p_{ix}(1 - \beta_{sx}) \end{cases}$ </td><td> $\begin{cases} 0 & \text{ifp} < p_{ix} \\ w_{ix}^{\beta} & \text{ifp}_{ix} \leq p \leq p_{ix}(1 - \beta_{sx}) \\ 0 & \text{ifp} > p_{ix}(1 - \beta_{sx}) \end{cases}$ </td></tr><tr><td>Medium (e.g. y)</td><td colspan="2"> $\begin{cases} 0 & \text{ifp} < p_{iy}(1 - \beta_{sy}) \\ w_{ix}^{\beta} & \text{ifp}_{iy}(1 - \beta_{sy}) \leq p \leq p_{iy} \\ 0 & \text{ifp} > p_{iy} \end{cases}$ </td><td colspan="2"> $\begin{cases} 0 & \text{ifp} < p_{is} \\ w_{iy}^{\beta} & \text{ifp}_{is} \leq p \leq p_{iy} \\ 0 & \text{ifp} > p_{iy} \end{cases}$ </td><td> $\begin{cases} 0 & \text{ifp} < p_{iy} \\ w_{iy}^{\beta} & \text{ifp}_{iy} \leq p \leq p_{iy}(1 - \beta_{sy}) \\ 0 & \text{ifp} > p_{iy}(1 - \beta_{sy}) \end{cases}$ </td></tr><tr><td>High (e.g. z)</td><td colspan="2"> $\begin{cases} 0 & \text{ifp} < p_{iz}(1 - \beta_{sz}) \\ w_{iz}^{\beta} & \text{ifp}_{iz}(1 - \beta_{sz}) \leq p \leq p_{iz} \\ 0 & \text{ifp} > p_{iz} \end{cases}$ </td><td colspan="2"> $\begin{cases} 0 & \text{ifp} < p_{iz}(1 - \beta_{sz}) \\ w_{iz}^{\beta} & \text{ifp}_{iz}(1 - \beta_{sz}) \leq p \leq p_{iz} \\ 0 & \text{ifp} > p_{iz} \end{cases}$ </td><td> $\begin{cases} 0 & \textbf{ifp} < p_{is} \\ w_{iz}^{\beta} & \text{ifp}_{is} \leq p \leq p_{iz} \\ 0 & \text{ifp} > p_{iz} \end{cases}$ </td></tr></table>

![](/api/attachments/Z9KZEU5G/fulltext/images/dba5b944f9d75950188882a288960b794bceb941bf4a144c42d6edffec116fb8.jpg)

![](/api/attachments/Z9KZEU5G/fulltext/images/36b049f9b378dce510dcc6be31ec266346bcf262544bc6fa39a704c685773196.jpg)  
Fig. 5. a Sloped linear weight function for markup adjustmentŽ . $( \gamma _ { i s } < 0 ) .$ Ž . . b Sloped linear weight function for markdown adjustment $( \gamma _ { i s } < 0 )$

## 8.2. Rule-bases

Pricing policies, competition policies, and demand-driven judgments are stored in the form of rules. The pricing rules are illustrated in Fig. 9.

## 8.3. Knowledge acquisition

We interviewed management personnel of the supermarket chain Hanwha to define pricing policies and necessary values for the integrated model. The sales and profit goals of the company and divisions were established by the annual plan of the year. The merchandising division shares the goal of sales and profit with the sales division. The most important goal of the merchandising division was profit maximization, while the managers of the sales division were more interested in sales maximization. The managers of the merchandising division emphasized the role of the cost-plus model, while the managers of the sales division stressed the competitor-referenced model and demand-driven model.

![](/api/attachments/Z9KZEU5G/fulltext/images/20727de309288f99b153127412506906acd8f73260f705007ab31d7708011194.jpg)  
Fig. 6. Integrated weight functions.

![](/api/attachments/Z9KZEU5G/fulltext/images/9cb6e12598b990152b5d550d552fff9575bdc11485bde3700557bc8e0972249f.jpg)  
Fig. 7. Cumulative weights of the case of illustration.

In the next step, we interviewed the managers of the two divisions to extract the knowledge about how they set the cost-plus price and how they set the competitor-referenced price. Six key values , $\beta _ { \mathrm { L P I C } } ,$ $\beta _ { \mathrm { M P I C } } , ~ \beta _ { \mathrm { H P I C } }$ and  Žboth $\gamma > 0$ and $\gamma < 0$ .  cases .

## 8.4. Determination of weights

To set the weights of pricing models, we asked 51 experts from the merchandising and sales division about the relative importance of the factors. Each expert was asked to assign a weight to each factor on a scale from 1 to 8. This result is organized as the frequencies of weights, and the total weight is computed by summing the weights multiplied by frequencies. By dividing the total by the number of experts and then by multiplying by 10 to enhance the readability, the estimates of weights are computed. These weights along with the , , and can derive the weight functions. The result for the sales grade of item A is listed in Table 5.

Note the difference in the weights of $\gamma > 0$ and $\gamma < 0 .$ This happened because the pricing experts are more cautious to markups than markdowns.

## 9. Performance of KAPA

## 9.1. Experimental design

The objective of KAPA was to duplicate experts’ pricing practices. To measure the performance of KAPA, we need to know its conformity to experts. To study the experts’ pricing decisions, we asked 54 experts of the Hanwha Supermarket Chain. Among them, 51 experts are the same people who answered the questions for weight determination in Section 8.4. An expert from the sales division revealed extremely high prices to the questions, so we omitted his response from the sample. The remaining 53 experts have from 1 to 15 years of experience, with an average of 6 years.

![](/api/attachments/Z9KZEU5G/fulltext/images/54b0ce7ad078c192a1058c400dabbb9035093db91866176617430d76c3422a80.jpg)  
Fig. 8. Architecture of KAPA system.

The selected store had the medium price image strategy and had three competitors with different price images: LPIC, MPIC, and HPIC. Among 647 categories dealt with by the store, this experiment focused on the instant coffee category. Again, among 24 items in the instant coffee category, the item ‘‘Choice Coffee 100 g bottled’’ is studied. The cost of the item was US\$3.00. Cost-plus markup rate Ž . of the category was 20%.

The questionnaires were for the 16 new item cases and 60 existing item cases. Thus, we had 76 cases in total. For the new item cases, the prices of competitors are provided to experts. And for the existing item cases, the current price and sales grade of the item are also provided. The existing item cases are composed of 20 cases of A, B, and C sales grades, respectively.

Fig. 9. Rules for the combined model.

```txt
/* Rule for cost-plus model by merchandise class and sales-grade */
(RULE cost-plus(1)

IF    class-code = class-0713
    item = existing
    sales-grade = A

THEN    alpha = 22)

/* Rule for cost-plus model by merchandise category and sales-grade */
(RULE cost-plus(2)

IF    category-code = category-140101
    item = existing

THEN    alpha = 33
    weight-of-alpha = 77)

/* Rule for competitor-referenced model by sales-grade */
(RULE competitor-reference(x))

IF    competitor = <x> ; <> implies variable
    sales-grade = A

THEN    beta = 0.10
    weight-of-beta = 200

/* Rule for demand-driven model by merchandise department and sales-grade */
(RULE demand-driven(1))

IF    department-code = department-07
    item = existing
    sales-grade = A
    markup-rate > 0.30

THEN    gamma = -0.05 ; markdown
    weight-of-negative-gamma = 120 )

/* Rules to assign-weight by merchandise department and sales-grade */
(RULE assign-weight(1))

IF    department = departmentt-07
    item = existing
    sales-grade = A

THEN    weight-of-alpha = 45
    weight-of-beta(x) = 55
    weight-of-beta(y) = 68
    weight-of-beta(z) = 53
    weight-of-negative-gamma = 49
    weight-of-positive-gamma = 37
```

## 9.2. RepresentatiÕe Õalue of experts’ opinion

Two candidates for representative value were the mean and the mode of experts’ answers. Since there are differences in experts’ opinion, we need to select a representative value from the statistics. Total of 44 out of 76 cases had the same value in mean and mode, but 32 cases had different values. In this study, we adopted the mode as the representative value of experts’ answers.

Table 5  
Illustrative estimated weights

<table><tr><td rowspan="2">Model</td><td rowspan="2">Factor</td><td colspan="8">Frequency of weight</td><td rowspan="2">Total weight W</td><td rowspan="2">Estimated weight 10W/51</td><td rowspan="2">Order</td></tr><tr><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td></tr><tr><td>Cost-plus</td><td> $\alpha$ </td><td>6</td><td>6</td><td>6</td><td>10</td><td>3</td><td>9</td><td>6</td><td>5</td><td>232</td><td>45</td><td>5</td></tr><tr><td rowspan="3">Competitor-referenced</td><td> $\beta_{LPIC}$ </td><td>11</td><td>7</td><td>10</td><td>7</td><td>7</td><td>5</td><td>3</td><td>1</td><td>282</td><td>55</td><td>2</td></tr><tr><td> $\beta_{MPIC}$ </td><td>19</td><td>15</td><td>10</td><td>1</td><td>5</td><td>1</td><td>0</td><td>0</td><td>345</td><td>68</td><td>1</td></tr><tr><td> $\beta_{HPIC}$ </td><td>9</td><td>9</td><td>6</td><td>10</td><td>5</td><td>7</td><td>5</td><td>0</td><td>272</td><td>53</td><td>3</td></tr><tr><td rowspan="2">Demand-driven</td><td> $\gamma < 0$ </td><td>3</td><td>7</td><td>7</td><td>13</td><td>11</td><td>8</td><td>2</td><td>0</td><td>252</td><td>49</td><td>4</td></tr><tr><td> $\gamma > 0$ </td><td>1</td><td>4</td><td>3</td><td>5</td><td>14</td><td>11</td><td>8</td><td>5</td><td>189</td><td>37</td><td>6</td></tr></table>

## 9.3. Illustration with a new item case

To explain the new item case, let us give an example. In the case N-1, prices of LPIC, MPIC, and HPIC are US\$3.40, US\$3.60, and US\$3.80, respectively. The price suggested by the cost-plus model is US\$3.60. Table 6 shows the results from experts answers, whose mode is US\$3.60.

On the other hand, Fig. 10 a is the weight func- Ž . tions of KAPA for this case, and Fig. 10 b is itsŽ . cumulative weight functions. The point US\$3.60 has the largest cumulative weight 113, which is equal to the mode in Table 6. This implies that KAPA can replace human experts’ judgments for the retail pricing.

## 9.4. Illustration with an existing item case

Let us see an example case E-1 from the existing item cases. The example case E-1 has the same competitors as case N-1 with the current price US\$3.20, cost<sup>s</sup>US\$3.00, and <sup>s</sup>0.333 Žc <sup>s</sup> US\$0.10 . The summary of experts’ answers for the. three sales grades is listed in Table 7.

According to Table 7, mode of sales-grade A item is US\$3.40, which is the same as the price of LPIC. In the cases of the sales-grade B and C items, mode is US\$3.60, which coincides with the price of MPIC and cost-plus model.

Table 6  
Suggested price by experts for the case N-1

<table><tr><td>Price</td><td>3.20</td><td>3.30</td><td>3.40</td><td>3.50</td><td>3.55</td><td>3.60</td><td>3.70</td><td>3.79</td><td>3.80</td></tr><tr><td>Frequency</td><td>1</td><td>1</td><td>4</td><td>13</td><td>1</td><td>27</td><td>4</td><td>1</td><td>1</td></tr></table>

Fig. 11 a is the weight functions of the case E-1 Ž . with the sales-grade A, and Fig. 11 b is its cumula-Ž . tive weight functions. In Fig. 11 b , the candidateŽ . price is in the interval 3.40, 3.50 . So we applied the criterion of taking the price nearest to the current price resulting in US\$3.40 that is the same as the experts’ mode.

## 9.5. Summary of the experimental results

As a measure of validation, we counted the hit ratio of KAPA with the mode of experts’ answers. In the new item cases, the hit ratio was 14 out of 16 cases. The hit ratio of existing item cases with the criterion of nearest to current price rule was 54 out of 60 cases. The hit ratio of existing item cases withŽ the criterion of average was 52 out of 60 cases. The. hit-ratio of KAPA is summarized in Table 8 With this result, we confirmed that KAPA could perform on a highly consistent basis with the mode of human experts. This implies that KAPA is applicable to pricing million of items dynamically.

## 10. Conclusion

In this paper, we have proposed a combined model for retail pricing. The base models are costplus, competitor-referenced, and demand-driven models. We adopted the weight functions to combine the models, and the price point determination rules to solve the models. This approach is implemented in the experimental system KAPA, and its performance turns out highly consistent with the mode of experts opinions.

![](/api/attachments/Z9KZEU5G/fulltext/images/8f35bdbfbfd454e2074c43b2bc2fb5c55cfeb953214d61e34979281a210aacb9.jpg)

![](/api/attachments/Z9KZEU5G/fulltext/images/5f45d75aff8dce620bb4f87f6a1fb9285f491cee38da3cda9b026413884a1c2e.jpg)  
Fig. 10. a Weight functions of case N-1. b Cumulative weight function of case N-1.Ž . Ž .

Since the prices of competitors are open and easily collectable in the electronic commerce environment, this approach is quite realistic to implement. So KAPA can be used not only for the traditional retail stores, but also for the electronic stores.

Suggested price by experts for the case E-1

<table><tr><td rowspan="2">Sales grade</td><td colspan="13">Price</td></tr><tr><td>3.00</td><td>3.10</td><td>3.20</td><td>3.30</td><td>3.40</td><td>3.48</td><td>3.50</td><td>3.58</td><td>3.59</td><td>3.60</td><td>3.65</td><td>3.70</td><td>3.80</td></tr><tr><td>A</td><td></td><td></td><td>9</td><td>8</td><td>14</td><td>1</td><td>10</td><td></td><td></td><td>7</td><td></td><td>3</td><td>1</td></tr><tr><td>B</td><td></td><td>1</td><td>4</td><td>2</td><td>14</td><td></td><td>4</td><td>1</td><td>1</td><td>23</td><td></td><td>1</td><td>2</td></tr><tr><td>C</td><td>1</td><td></td><td></td><td>3</td><td>7</td><td></td><td>6</td><td></td><td></td><td>24</td><td>2</td><td>3</td><td>7</td></tr></table>

Table 8  
![](/api/attachments/Z9KZEU5G/fulltext/images/315f496afa6fce28b53645dabbcf70d725c532fd002aef2e59f4361e7fd7dfdc.jpg)  
(b) weight

![](/api/attachments/Z9KZEU5G/fulltext/images/c96446c11319a383e5a893893324b9fe2226e26af2edd81f74e8e169b3aba45c.jpg)  
Fig. 11. a Weight functions of case E-1. b Cumulative weight function of case E-1.Ž . Ž .

## References

<sup>w</sup> <sup>x</sup> 1 M.M. Abraham, M.L. Lodish, PROMOTER: an automated promotion evaluation system, Marketing Science 6 2 1987Ž . Ž . 101–123.

<sup>w</sup> <sup>x</sup> 2 E. Ballesteto, C. Romero, Multiple Criteria Decision Making and its Applications to Economic Problems, Kluwer Academic Publishers, 1998.

<sup>w</sup> <sup>x</sup> 3 B. Berman, J.R. Evans, Retail Management A Strategic Approach, 4th edn., Macmillan, 1989.

<sup>w</sup> <sup>x</sup> 4 R.C. Blattberg, K.J. Wisniewski, Price-induced patterns of competition, Marketing Science 8 4 1989 291–309 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 A.V. Bultez, P.A. Naert, S.H.A.R.P.: Shelf Allocation for Retailers’ Profit , Marketing Science 7 3 1988 211–231. Ž . Ž .

Hit ratio of KAPA

<table><tr><td>Criteria</td><td colspan="3">Criterion of the price nearest to the current price (nearest the cost-plus price for new items)</td></tr><tr><td>Items</td><td>New items</td><td>Existing items</td><td>Total</td></tr><tr><td rowspan="2">Hit ratio</td><td>14/16</td><td>54/60</td><td>68/76</td></tr><tr><td>87.5%</td><td>90.0%</td><td>89.5%</td></tr></table>

<sup>w</sup> <sup>x</sup> 6 R. Burke, A. Rangaswamy, J. Wind, J. Eliashberg, A knowledge-based system for advertising design, Marketing Science 9 3 1990 212–229.Ž . Ž .

7 C. Casey, C. Murphy, Expert systems in marketing: an application for pricing new products, Expert Systems with Applications 7 4 1994 545–552.Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 G Colson, C. Bruyn, Models and methods in multiple criteria decision making,International Series in Modern Applied Mathematics and Computer Science, Pergamon Press, 1990.

<sup>w</sup> <sup>x</sup> 9 W.R. Davidson, D.J. Sweeney, R.W. Stampfl, Retailing Management, Wiley, 1988.

<sup>w</sup> <sup>x</sup> 10 P.R. Dickson, J.E. Urbany, Retailer reactions to competitive price changes, Journal of Retailing 70 1 1994 1–21.Ž . Ž .

<sup>w</sup> <sup>x</sup> 11 Y. Kinberg, A. Rao, M.F. Shakun, A mathematical model for price promotions, Management Science 20 1974 948–959.Ž .

<sup>w</sup> <sup>x</sup> 12 R. Lal, R. Staelin, An approach for developing an optimal discount pricing policy, Management Science 30 1984Ž . 1524–1539.

<sup>w</sup> <sup>x</sup> 13 M. Levy, B.A. Weitz, Retailing Management, Irwin, 1991.

<sup>w</sup> <sup>x</sup>14 A.A. Mitchell, J.E. Russo, D.R. Wittink, Issues in the development and use of expert systems for marketing decisions, International Journal of Research in Marketing 8 1 1991Ž . Ž . 41–50.

<sup>w</sup> <sup>x</sup> 15 A.L. Montgomety, Creating micro-marketing pricing strategies using supermarket scanner data, Marketing Science 16 Ž . Ž . 4 1997 315–337.

<sup>w</sup> <sup>x</sup> 16 K.B. Monroe, A.J.D. Bitta, Models for pricing decisions, Journal of Marketing Research, August 1978 413–428.Ž .

<sup>w</sup> <sup>x</sup> 17 R. Pizzano, Pricing Strategy, http:<sup>rr</sup>www.pizzano.com<sup>r</sup> pricevol.htm.

<sup>w</sup> <sup>x</sup> 18 S. Ram, S. Ram, INNOVATOR: an expert system for new product launch decisions, Applied Artificial Intelligence 2 Ž . 1988 129–148.

<sup>w</sup> <sup>x</sup> 19 M.G. Singh, J.C. Bennavail, Price-Strat: a knowledge support system for profitable decision-making during price wars, Information and Decision Technologies 19 1994 277–296.Ž .

<sup>w</sup> <sup>x</sup> 20 S.R. Sisodia, M.E. Warkentin, Marketing and expert systems: review, synthesis and agenda, in: Proceedings of The World Congress on Expert Systems,1991, pp. 274–281.

<sup>w</sup> <sup>x</sup> 21 P.H. Yoo, Pricing Policy, Pakyungsa, Seoul, 1991.

![](/api/attachments/Z9KZEU5G/fulltext/images/5923164d44a5d324e7da1b0a0ba98bc15c5b593c362befcd1f941fcbbb81f32c.jpg)

Nahk Hyun Sung is an Assistant Professor of MIS at the School of Management of Yongin University. He received a Ph.D. 1999 from the Korea Ad-Ž . vanced Institute of Science and Technology KAIST . He received a BA 1981Ž . Ž . from Seoul National University and a MS 1990 from the KAIST. He hasŽ . worked in developing information systems for retail industry from 1983 to 1996. His main research interests are on intelligent information systems for retailers and for electronic commerce environment.

![](/api/attachments/Z9KZEU5G/fulltext/images/4e4e45369c3b82dec7a3992c26b6442d7750119cba872515bb826d9f2d2d47ed.jpg)

Jae Kyu Lee is a Professor of Management Information Systems at the Korea Advanced Institute of Science and Technology and Director of the International Center for Electronic Commerce. He received a BA from Seoul National University, a MS from the Korea Advanced Institute of Science and Technology and a Ph.D. from the Wharton School, University of Pennsylvania. He has previously served as an exchange professor at Carnegie-Mellon University 1989 andŽ .

University of Texas at Austin 1994 . He was the chair of theŽ . 1998 International Conference on Electronic Commerce ICECŽ . and the 3rd World Congress on Expert Systems 1996 . He hasŽ . authored several books on Electronic Commerce and Expert Systems and published numerous papers in the following journals: Management Science, Decision Support Systems, Expert Systems with Applications, Expert Systems, Decision Science and many others. Currently, he is an editor of various international journals like Decision support Systems, Expert Systems with Applications, and International Journal of Electronic Commerce. His main research interests are in the fields of Electronic Commerce and Intelligent Management Information Systems.
