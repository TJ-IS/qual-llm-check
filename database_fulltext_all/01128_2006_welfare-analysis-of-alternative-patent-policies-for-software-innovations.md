---
otero_id: 1128
otero_key: "DHM2FWM2"
title: "Welfare analysis of alternative patent policies for software innovations"
authors: "Matt E. Thatcher; Taeha Kim; David E. Pingry"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.10.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Welfare analysis of alternative patent policies for software innovations

Matt E. Thatcher<sup>a,\*</sup>, Taeha Kim<sup>b</sup>, David E. Pingry<sup>a,c</sup>

<sup>a</sup>Management Information Systems, University of Arizona, 430 McClelland Hall, Tucson, AZ 85721, United States

<sup>b</sup>School of Management, George Mason University, United States

<sup>c</sup>Management Information Systems/Economics, University of Arizona, United States

Available online 21 November 2004

## Abstract

We present a duopoly model that extends existing patent policy design models in the economics literature to formalize the links among the patent policy levers set by public policy (patent height and width), the strategic decisions made by firms (R&D investments, product development, product imitation, patent decision, and product pricing), the purchasing decisions made by consumers, and the market parameters. This integrated model enables policymakers to better analyze the impact of alternative patent policies on the level of social welfare and the distribution of that welfare among innovators, imitators, and consumers in a range of industry contexts—specifically targeting issues of software patents. Critical results include (1) an increase in patent width unambiguously increases R&D spending to generate a novel idea; (2) an increase in patent height may increase or decrease R&D spending depending on the efficiency with which an innovator can transform the novel idea into a commercial product; (3) while enforced patents will improve innovator profits they may worsen imitator profits, consumer welfare, or both and may even worsen total social welfare; (4) the optimal (social welfare maximizing) policy design is characterized by a relatively high patent height and moderate patent width. 3200.4 A 11

Keywords: Patent policy; Patent height; Patent width; Software patents; Social welfare; Innovation; R&D

## 1. Introduction

Technological innovations are a major source of economic growth, typically leading to improvements in productivity, per capita income, and standard of living for consumers [12,23]. They are also a source of competitive advantage and market power for many innovating firms, often leading to bargaining power with customers, barriers to entry for competitors, and a flow of profits from licensing fees. Firms engage in costly research and development (R&D) activities to discover and develop an innovative product. However, a discovery that is instantly imitated by competitors at low cost may not yield enough revenues to allow the innovator to recoup its R&D costs. The threat of cheap, quick imitation of technological innovations (e.g., software applications and internet-based business methods) has increased significantly with recent advances in software reverse engineering techniques. Competitors may use these techniques to reverse a program’s machine code back into the source code in which it was written, allowing them to duplicate how software programs perform certain operations without having access to the actual program.

One policy tool available to the US government to encourage technological innovation is a patent system that provides innovating firms with some protection from derivative products (or provides exclusive rights to make, use, or sell an innovation) for 20 years from the date the patent is awarded<sup>1</sup>. Patent law requires that an innovation under review must be new, useful, and nonobvious to a person of ordinary skill in the relevant field. Once a patent is awarded, it provides the patent holder with a scope of protection from imitation by competitors. A patent holder who believes that a patent has been infringed may file suit against those who make, use, or sell the derivative product to stop their use of the infringing product or to collect licensing fees. In the economics literature, the novelty and nonobvious requirement is referred to as the patent height and may be defined as the minimum quality improvement (or the minimum number of new product characteristics) a firm must make to an existing, well-known product to be awarded a patent. Once a patent has been awarded, the scope of protection from imitation is referred to as the patent width. If patent protection is narrow, then competitors may imitate a large number of the patented product’s characteristics without infringement. Alternatively, if patent protection is wide, then competitors may imitate only a small number of the patented product’s characteristics without infringement<sup>2</sup>.

The government views patent law as a policy tool used to stimulate R&D and innovation and maximize social welfare. However, recently, there has been debate in the popular press about the effectiveness of software patents in achieving these goals. Some argue that patent examiners may not possess the expertise to properly set the patent height (i.e., the novelty requirement) that an innovating firm must attain to be awarded a patent. As a result, patent examiners sometimes award patents to well-established software features (i.e., examiners’ set patent height too low). Others argue that court judges may not possess the expertise to properly assess the patent width (i.e., whether a derivative software product, or imitation, infringes an existing patent). As a result, court judges sometimes prevent the use and sale of differentiated derivative products (i.e., courts’ provide too wide a scope of protection). Examples of software patents that have been challenged in court as either too low or too wide include Amazon.com’s patent for its One-Click technology<sup>3</sup>, Priceline.com’s patent for its Name Your Own Price technology<sup>4</sup>, Allan Konrad’s patent on web-based access to databases<sup>5</sup>, and British Telecommunications patent for hyperlinks<sup>6</sup> [2,7,22,25,26]. While some critics argue that these concerns imply that software patents should not be awarded at all, others argue that these concerns may be addressed by identifying and setting the appropriate patent height and narrowing the patent width.

This discussion raises the question of whether an integrated framework can be developed that allows policymakers to evaluate the impact of alternative patent policies on firm strategies, consumer behavior, and social welfare in the software arena and whether this framework may be used to determine the optimal, social welfare-maximizing patent policy design. The economics literature has dealt extensively with a wide set of patent issues. However, this literature is fragmented and does not directly approach in a robust manner the patent issues in the context of software and business processes. Interestingly, the academic IT literature has essentially remained silent about these issues, avoiding formal economic analysis of software patent policy. This void in the IT literature persists despite the enormous growth in the number of software patents awarded over the past decade and despite the concern over their impact on technological innovation and consumer welfare.

The model presented in this paper synthesizes and extends some of the approaches taken in economics to address the current IT issues. Specifically, we are enriching the models in economics by creating a framework that integrates the patent policy levers set by public policy (patent height and patent width), the strategic decisions made by firms (R&D investments, product development, product imitation, patent decision, and product pricing), the purchasing decisions made by consumers, and the market parameters characterizing the context. This model will enable policymakers to better analyze the impact of alternative patent policies on the level of social welfare and the distribution of that welfare among innovators, imitators, and consumers in a range of contexts, including the software arena<sup>7</sup>.

Specifically, we present a multistage model of duopoly in which firms compete in idea generation (i.e., R&D), product development (i.e., product innovation and imitation), and pricing given a patent policy. We identify and characterize the enforceable set of patent policies that provide profit incentive for an innovator to develop and patent a product that meets the patent height. We also examine the impact of these enforceable policies on R&D expenditures, product development and pricing decisions, and the level and distribution of social welfare. Although we identify the socially optimal patent policy in a specific context, the more interesting application of the model may be for evaluating the effectiveness of current policy and the comparative effectiveness of proposed policies over a range of contexts, including the software arena. The critical insights are as follows:

<sup>!</sup> An increase in patent width unambiguously increases R&D spending by firms racing to develop a novel idea that may be developed by the winner (or innovator) into a commercial product.

<sup>!</sup> An increase in patent height may increase or decrease R&D spending depending on the efficiency with which an innovator can transform the novel idea into a commercial product.

There exists what we term a patent enforcement region (PER), defined as the set of policies that provide the innovator with profit incentive to develop and patent a product that meets the height, thereby restricting the imitator’s response.

<sup>!</sup> The set of policies within the PER is characterized by medium patent height and sufficiently wide scope of protection.

There exists a set of policies within the PER that results in the development and distribution of better quality products by both innovator and imitator (when compared to the product qualities developed without a patent) despite the restriction placed on the imitator.

Although, by definition, policies set within the PER improve innovator profits when compared to the no patent equilibrium, they may worsen imitator profits, consumer welfare, or both and may even worsen total social welfare.

Finally, there exists an optimal social welfare maximizing policy design on the boundary of the PER. This policy is characterized by a relatively high height (i.e., high within the context of the PER) with a moderate scope of protection. This policy not only maximizes social welfare but also makes all stakeholders (i.e., innovator, imitator, and consumers) better off.

## 2. Literature review

Early patent design literature, initiated by Nordhaus [23], examined the socially optimal patent length [13,27,33]. This work commonly assumed that innovators patent all innovations, and that the patents provide full protection from improvements (i.e., infinite patent height) and full protection from imitation (i.e., infinite patent width) while the policy is in force. Work in the patent design literature has since focused on extending this analysis to examine the economic impact of patent height and width.

Gilbert and Shapiro [11] examine the socially optimal mix between patent length and patent width. They assume the following:

<sup>!</sup> a firm has developed a single, innovative product (that is, neither the R&D race nor the product development competition is modeled);

<sup>!</sup> the patent authority has awarded the firm a patent for its innovative product (that is, the patent decision is not modeled);

the patent authority has set a minimum patent prize (or reward for innovation) that a patentee should achieve over the life of the patent (that is, the model does not address what size the prize should be); and

<sup>!</sup> the patent provides the patentee full protection from product improvements (that is, patent height is assumed infinite).

Given these assumptions, Gilbert and Shapiro determine the combination of patent length and patent width that allows the patentee to achieve a given patent prize at minimal social cost. They define patent width as the ability of the patentee to raise the price for its product with wider width allowing the patentee to charge a higher price. Since patent width is modeled as a price control, it does not affect the set of substitute products that are offered to consumers. The result is that the social costs of a given patent prize are minimized by awarding narrow but lengthy patents. That is, the optimal patent length is infinite with the patent width (i.e., price of the innovator’s product) set at the level that just covers the patentee’s R&D costs.

Klemperer [14] also examines the socially optimal mix between patent length and patent width. While he uses a model set-up similar to Gilbert and Shapiro [11], Klemperer defines patent width as how different a competitor’s product must be from a patented product to avoid infringement. Patent width may be thought of as determining the maximum number of product characteristics that may be imitated by competitors. While there are no direct controls on the patentee’s price, as in Gilbert and Shapiro, price is controlled indirectly with wider patents giving patentees more pricing power through greater product differentiation. That is, wider patents make imitation products less attractive to consumers, thereby reducing substitution away from the patented product. Similar to Gilbert and Shapiro, he determines the optimal patent policy that allocates a given patent prize to the patentee at minimal social cost. He identifies the conditions under which patents with infinite length and narrow protection are socially optimal and the conditions under which very short-lived but wide patents are optimal. Finally, he suggests that future research may focus on developing models to examine optimal patent height and to examine the effect of patent policy on R&D competition before the innovative product is developed.

Gallini [9] examines the socially optimal mix of patent length and patent width while assuming costly imitation and endogenizing the innovator’s decision to patent its innovative product and the competitors decisions to imitate. Gallini defines patent width similar to Gilbert and Shapiro [11] (i.e., a price control over the patentee’s product) and shows that social surplus is maximized when patents are very wide (i.e., allowing no imitation), and patent length is adjusted to achieve the revenue required to cover R&D costs.

Dijk [6], in response to Klemperer’s call, examines the socially optimal choice of patent height. Specifically, he examines patent height in a duopoly where two firms compete in improvements to a basic invention. He assumes exogenous to the model that:

<sup>!</sup> a firm has developed a single, basic invention (i.e., the R&D competition is not modeled);

<sup>!</sup> the firm holds a patent for the basic invention (i.e., the patent decision is not modeled); and

<sup>!</sup> the patent policy provides the patentee with infinite patent length and infinite patent width.

In this model, a competitor that wants to offer a competing product (or invent around the patented invention) must develop a product that meets or exceeds the patent height, which sets a minimum improvement level the competitor must offer to avoid patent infringement. Patent height is fixed by the patent authority and is exogenous to the model. Dijk uses a standard vertical differentiation model to analyze this competition in improvements between the patentee and its competitor, where product qualities are interpreted as improvements to the basic invention. This inclusion of a stage where firms compete simultaneously in product development is a critical contribution of this paper since previous work simply treated product innovations as exogenous. Dijk uncovers three critical findings: (1) low patent height does not affect the market equilibrium, (2) medium patent height hurts the patent holder (as it gives incentive to competitors to make profitable improvements), and (3) high patent height benefits the patent holder. Dijk suggests that future research may focus on developing models to examine the product development stage as a sequential equilibrium and to examine the impact of patent height on R&D competition and on a firm’s patent decision.

We limited our review to a set of closely related models of optimal patent policy design. Although the model we present in Section 5.3 builds on certain definitions and modeling conventions developed in this literature, it is not a linear extension of any one model. In particular, we address the patent policy issue from a different perspective than previous literature which commonly assumes that an innovative product has already been developed, and a patent has been awarded for the product. Given the perspective in the literature, the goal of the patent authority is to fine-tune the policy instruments (ex ante) to provide the patentee with a given prize at minimum social cost. In contrast, our model places the patent authority in its proper position as the first mover with the firms responding to policy incentives. Therefore, we are able to examine the impact of patent policy on R&D expenditures, the development and pricing of an innovative product and its imitation, and the innovator’s patent decision. We use this model to determine the optimal social welfare maximizing patent design and to examine the impact of policy instruments on the distribution of welfare among innovators, imitators, and consumers.

## 3. The model

We develop an integrated, five-stage economic model of duopoly competition that examines the optimal (i.e., social welfare maximizing) trade-off between patent height and patent width, assuming an infinite patent length (as assumed by Dijk [6]). We posit an initial unpatented product of given quality. In the first stage, the patent authority sets a policy defined by two instruments—a patent height and a patent width. The patent height defines the minimum level of improvement that a firm must make to the initial product to be awarded a patent. Once a patent is awarded, the patent width defines the extent to which the competitor may imitate the patented product. In the second stage, the two firms compete in an R&D race to generate a novel idea or feature (which in and of itself has no commercial value). In the third stage, the winner of the R&D race (or the innovator) transforms the novel idea into an improved commercial product at substantial fixed costs. Given the patent policy set in the first stage, the innovator decides whether or not to patent its product. In the fourth stage, the loser of the R&D race (or the imitator) observes the innovator’s product quality and patent decision and decides to what extent it will imitate the product. Finally, in the fifth stage, the firms simultaneously set prices for their products and offer them to the market. We now formally describe the model.

## 3.1. Patent policy (stage 1)

Initially, a patent authority sets a policy $( \mu , \lambda )$ . The patent height l is defined as the minimum improvement in product quality the innovator must make to the initial unpatented product in the third stage to be awarded a patent. For simplicity, we normalize the quality of the initial product to zero. This definition of patent height is similar to that used by Dijk [6]. The patent width is defined as $( \mu - \lambda )$ , where k is the maximum product quality the imitator may set in the fourth stage if the innovator is awarded a patent such that $\mu > \lambda > 0$ . For clarification, $\lambda { = } 0$ represents a wide scope of protection from imitation (i.e., giving the innovator full monopoly power), while k close to $\mu$ represents a narrow scope of protection from imitation. This interpretation of patent width is most consistent with that of Klemperer [14].

## 3.2. Idea generation (stage 2)

In the second stage, Firms 1 and 2 race to generate a novel idea by investing an amount $( 1 / 2 ) h \alpha _ { i } ^ { 2 } , i \in \{ 1$ 2} in R&D activities where (i) $\alpha _ { i } { > } 0$ is the conditional probability that Firm i generates an idea at time t given that it has not succeeded until that time, and (ii) $h { > } 0$ is a symmetric cost coefficient that characterizes the R&D cost infrastructure of each firm.

The probability of idea generation time s being within time t is $p r ( \tau < t ) { = } 1 { - } e ^ { - \alpha t }$ . Therefore, the probability that Firm 1 wins the race (and generates a novel idea before Firm 2) is,

$$
\operatorname{pr} \left(\tau_ {1} <   \tau_ {2}\right) = \int_ {0} ^ {\infty} \int_ {s} ^ {\infty} \alpha_ {1} e ^ {- \alpha_ {1} s} \alpha_ {2} e ^ {- \alpha_ {2} u} \mathrm{duds} = \frac {\alpha_ {1}}{\alpha_ {1} + \alpha_ {2}}.\tag{1}
$$

Symmetrically, the probability that Firm 2 wins the race is $\alpha _ { 2 } / ( \alpha _ { 1 } + \alpha _ { 2 } )$ . Therefore, Firm 1’s profit in the first stage is

$$
\Pi_ {1} = V _ {W} \frac {\alpha_ {1}}{\alpha_ {1} + \alpha_ {2}} + V _ {L} \frac {\alpha_ {2}}{\alpha_ {1} + \alpha_ {2}} - \frac {1}{2} h \alpha_ {1} ^ {2},\tag{2}
$$

where $V _ { W } \left( V _ { L } \right)$ is the expected third stage payoff for the firm that wins (loses) the R&D race. Firm $2 \mathrm { { } s }$ profit in the first stage is symmetric. The structure of the R&D race described above is taken from Loury [18] and Beath et al.[3].

## 3.3. Product development (stages 3 and 4)

In the third stage, the innovator leverages its novel idea (generated through R&D expenditures) to design and develop a product of quality $s _ { W } { \in } ( 0 , \infty )$ given the patent policy $\left( \mu , \ \lambda \right)$ . The cost to the innovator of designing and developing the product is

$$
C _ {W} = k \frac {s _ {W} ^ {2}}{2},\tag{3}
$$

where $k { > } 0$ is a technology cost coefficient, the size of which affects the marginal cost of improving product quality. The cost function for product development is assumed to be quadratic because improving the overall quality of a product becomes increasingly difficult (and increasingly costly) as product quality increases. The quadratic form of this cost term has intuitive appeal, is widely used in the industrial organization literature [1,5,15,17,20,21,32], and has been used to analyze a diverse range of products including software products and information goods [16], medical services [10], and airline services [28].

In the fourth stage, the imitator observes the innovator’s product quality and then sets its own product quality. If, in the third stage, the innovator meets the patent height $( \mathrm { i . e . }$ , sets $s _ { W } { = } _ { \mu } )$ and patents its product, then the patent will be enforced, thereby restricting the imitator’s quality response to $s _ { L } { \in } ( 0 , \lambda ) ;$ otherwise, the imitator may fully imitate, $\scriptstyle { s _ { L } } \in ( 0 , s _ { W } )$

Both products are considered perfect substitutes except in quality. Given advances in technology, the imitator is able to cheaply reverse engineer the innovator’s product. This, together with the R&D expenditures made by the imitator in the first stage, suggests that it is reasonable to assume that the imitator’s fixed development cost is zero in stage 4. Therefore, the payoffs in the product development stages for the innovator and imitator, respectively, are

$$
V _ {W} = R _ {W} - C _ {W} \text {   and   } V _ {L} = R _ {L},\tag{4 and 5}
$$

where $R _ { W } \left( R _ { L } \right)$ is the expected revenue earned by the innovator (imitator) from product sales in the fifth stage.

## 3.4. Product pricing (stage 5)

In the fifth stage, both firms observe the product qualities set in the previous stages and then simultaneously set prices for their products. The demand structure underlying the price competition stage is taken from standard models of vertical product differentiation [6,8,31]. As noted by Dijk ([6], pp. 153) <sup>b</sup>the use of vertical differentiation models is justified since consumers are expected to evaluate product improvements of a basic product in much the same way as qualities of a product. Consumers prefer large to small improvements, just as they prefer highto low-quality products.<sup>Q</sup>

If the quality per dollar of the innovator’s product were higher than that of the imitator’s product (i.e., $s _ { W } / p _ { W } { > } s _ { L } / p _ { L }$ , then the innovator would dominate the market in the fifth stage. However, we are more interested in examining the case in which the innovator does not dominate the market. We assume that consumers have heterogeneous tastes regarding product quality, and that each consumer either purchases one product or nothing at all. The indirect

## 4. Results

## 4.1. Price competition (Stage 5)

In the fifth stage, revenues for both firms are

$$
R _ {W} = p _ {W} \left(1 - \frac {p _ {W} - p _ {L}}{s _ {W} - s _ {L}}\right) \text {   and   } R _ {L} = p _ {L} \left(\frac {p _ {W} - p _ {L}}{s _ {W} - s _ {L}} - \frac {p _ {L}}{s _ {L}}\right),
$$

utility of an individual consumer is $( \theta s _ { W } { - } p _ { W } )$ if she buys from the innovator, $( \theta s _ { L } - p _ { L } )$ if she buys from the imitator, and zero if she does not buy a product, where $p _ { i } , i { \in } ( W , L )$ is the price of Firm $i \ ' \mathrm { s }$ improvement to the initial product, and h is a consumer taste parameter that indicates the intensity with which a consumer prefers improvements to the initial product. h is uniformly distributed with density 1. Consumers with a taste parameter $\frac { \left( p _ { W } - p _ { L } \right) } { \left( s _ { W } - s _ { L } \right) } < \tilde { \theta } \leq \stackrel { . } { 1 }$ buy the higher quality product from the innovator since $( \tilde { \theta } s _ { W } - p _ { W } ) { \geq } ( \tilde { \theta } s _ { L } { - } p _ { L } )$ . Consumers with a taste parameter $\scriptstyle { \frac { p _ { L } } { s _ { L } } } < { \hat { \theta } } < { \frac { ( p _ { W } - p _ { L } ) } { ( s _ { W } - s _ { L } ) } }$ buy the lower quality product from the imitator since $( \hat { \theta } s _ { L } - p _ { L } ) > ( \hat { \theta } s _ { W } - p _ { W } )$ Finally, the remaining consumers buy nothing. Without loss of generality, we normalize the number of consumers in the market to 1. Therefore, the vertically differentiated demands for the innovator and imitator, respectively, are

$$
Q _ {W} = 1 - \frac {p _ {W} - p _ {L}}{s _ {W} - s _ {L}} \text {   and   } Q _ {L} = \frac {p _ {W} - p _ {L}}{s _ {W} - s _ {L}} - \frac {p _ {L}}{s _ {L}}.\tag{6 and 7}
$$

As is common in the patent design literature $[ 6 , 1 0 , 1 1 , 1 4 ]$ , we assume the marginal cost of developing the product is zero. Therefore, the revenues earned by the firms in the fifth stage are

$$
R _ {i} = p _ {i} Q _ {i}, \forall i \in \{W, L \}.\tag{8}
$$

In this game, both firms know the payoff functions as common knowledge and know the history of the game thus far. The competition between the two firms is analyzed by solving for the subgame perfect equilibrium of the game. Comparative static analyses and graphical analyses are used to examine the impact of patent policy instruments on market equilibrium and the level and distribution of social welfare.

ð9 and 10Þ

and the second derivatives of both revenue functions with respect to prices are negative

$$
\frac {\partial^ {2} R _ {W}}{\partial p _ {W} ^ {2}} = - \frac {2}{s _ {W} - s _ {L}} <   0 \text { and } \frac {\partial^ {2} R _ {L}}{\partial p _ {L} ^ {2}} = - \frac {2 s _ {w}}{s _ {L} (s _ {W} - s _ {L})} <   0.\tag{11 and 12}
$$

Therefore, we derive both firms’ price reaction functions, given the product qualities set in the product development stages, by solving the first-order conditions (FOC)

$$
\frac {\partial R _ {W}}{\partial p _ {W}} = \frac {s _ {W} - s _ {L} - 2 p _ {W} + p _ {L}}{s _ {W} - s _ {L}} = 0 \mathrm{and} \frac {\partial R _ {L}}{\partial p _ {L}} = \frac {2 s _ {W} p _ {L} - s _ {L} p _ {W}}{s _ {L} (s _ {W} - s _ {L})} = 0.\tag{13 and 14}
$$

Solving for the price reaction curves gives

$$
p _ {W} (p _ {L}) = \frac {1}{2} (s _ {W} - s _ {L}) + \frac {1}{2} p _ {L} \text {   and   } p _ {L} (p _ {W}) = \left(\frac {s _ {L}}{2 s _ {W}}\right) p _ {W}.\tag{15 and 16}
$$

The point at which the price reaction curves intersect determines the unique price equilibrium

$$
p _ {W} (s _ {W}, s _ {L}) = \frac {2 s _ {W} (s _ {W} - s _ {L})}{4 s _ {W} - s _ {L}} \text {and} p _ {L} (s _ {W}, s _ {L}) = \frac {s _ {L} (s _ {W} - s _ {L})}{4 s _ {W} - s _ {L}}.\tag{17 and 18}
$$

Given Eqs. (17 and 18), we note that the equilibrium demand for each product is positive

$$
Q _ {W} (s _ {W}, s _ {L}) = \frac {2 s _ {W}}{4 s _ {W} - s _ {L}} > 0 \text { and } Q _ {L} (s _ {W}, s _ {L}) = \frac {s _ {W}}{4 s _ {W} - s _ {L}} > 0.\tag{19 and 20}
$$

## 4.2. Product development (stages 3 and 4)

## 4.2.1. No patent equilibrium (NPE)

In this section, we derive the equilibrium product quality decisions made by firms when a patent is not in force—that is, when the innovator does not patent its improvement to the initial product. This equilibrium, which we term the no patent equilibrium (NPE) will be used as a baseline for comparison to consider the impact of patent policy in later sections.

Proposition 1. Given that a patent is not in force there exists a unique quality equilibrium $( s _ { W } ^ { B } , s _ { L } ^ { B } )$ .

In stage 4, the imitator sets a product quality, given the quality set by the innovator in stage 3, which maximizes its payoff

$$
V _ {L} = R _ {L} ^ {*} = \frac {s _ {W} s _ {L} (s _ {W} - s _ {L})}{(4 s _ {W} - s _ {L}) ^ {2}}.\tag{21}
$$

The second derivative of $V _ { L }$ with respect to quality is negative

$$
\frac {\partial^ {2} V _ {L}}{\partial s _ {L} ^ {2}} = - \frac {2 s _ {W} ^ {2} (7 s _ {L} + 8 s _ {W})}{(4 s _ {W} - s _ {L}) ^ {4}} <   0.\tag{22}
$$

Therefore, we derive the imitator’s quality reaction function by solving for the FOC

$$
\frac {\partial V _ {L}}{\partial s _ {L}} = \frac {s _ {W} ^ {2} (4 s _ {W} - 7 s _ {L})}{(4 s _ {W} - s _ {L}) ^ {3}} = 0 \Leftrightarrow s _ {L} (s _ {W}) = \frac {4}{7} s _ {W}.\tag{23}
$$

This reaction function demonstrates that, in stage 4, the imitator’s best response to each quality set by the innovator is not to fully imitate the innovator’s product but rather to differentiate itself from the innovator by setting a lower quality. Customer heterogeneity in $\theta ,$ the taste parameter for product quality, creates opportunities for market segmentation. That is, the low quality product may be sold to those that value quality less intensely at a relatively low markup, whereas the high quality product may be targeted toward those that value quality more intensely at a comparatively higher markup. The imitator’s payoff when facing vertical market segmentation in the pricing stage is concave. That is, the imitator’s payoff $( V _ { L } )$ increases with its own quality $\left( s _ { L } \right)$ at low levels of quality. However, at some level of imitation (or quality), the payoff is maximized after which point the imitator’s payoff decreases with quality.

In the third stage, the innovator, knowing the imitator’s quality reaction function, sets a product quality that maximizes its payoff

$$
V _ {W} = \frac {4 s _ {W} ^ {2} (s _ {W} - s _ {L})}{(4 s _ {W} - s _ {L}) ^ {2}} - \frac {k s _ {W} ^ {2}}{2} = \frac {7 s _ {W}}{4 8} - \frac {k s _ {W} ^ {2}}{2}.\tag{24}
$$

The second derivative of $V _ { W }$ with respect to quality is negative, $\scriptstyle \cdot ( \partial ^ { 2 } V _ { W } / \partial s _ { W } ^ { 2 } ) = - k < 0$ . Therefore, we determine the NPE qualities by solving the FOC of $V _ { W }$ and substituting into $s _ { L } ( s _ { W } )$

$$
\frac {\partial V _ {W}}{\partial s _ {W}} = \frac {7}{4 8} - k s _ {W} = 0 \Leftrightarrow \left(s _ {W} ^ {B}, s _ {L} ^ {B}\right) = \left(\frac {7}{4 8 k}, \frac {1}{1 2 k}\right).\tag{25}
$$

## 4.2.2. Patent equilibrium (PE)

In this section, we derive the equilibrium product quality decisions made by firms when the innovator has a profit incentive to meet the patent height and patent its product. We term this the patent equilibrium (PE).

Proposition 2. There exists a set of PE. That is, there exists a set of patent policies $( \mu , \lambda )$ that, if set by the patent authority, replace the NPE $( s _ { W } ^ { B } , s _ { L } ^ { B } )$

To determine the set of policies that replace the NPE, we identify the condition under which the innovator will have profit incentive to meet the patent height $\mu$ and patent its product

$$
V _ {W} (\mu , \lambda) = \left(\frac {\mu^ {2} (8 (\mu - \lambda) - k (4 \mu - \lambda) ^ {2})}{2 (4 \mu - \lambda) ^ {2}}\right) > \frac {4 9}{4 6 0 8 k} = V _ {W} \left(s _ {W} ^ {B}, s _ {L} ^ {B}\right).\tag{26}
$$

Setting $V _ { \scriptscriptstyle W } ( \mu , \lambda ) { = } V _ { \scriptscriptstyle W } ( s _ { \scriptscriptstyle W } ^ { B } , s _ { \scriptscriptstyle L } ^ { B } )$ and solving for k gives

$$
\lambda (\mu) = \frac {\mu \left(1 8 4 3 2 k \mu (k \mu - 1) + 3 9 2 + 1 9 2 \sqrt {(- 6 k \mu (2 3 0 4 k ^ {2} \mu^ {2} - 1 5 3 6 k \mu + 4 9))}\right)}{2 (2 3 0 4 k ^ {2} \mu^ {2} + 4 9)}.\tag{27}
$$

Eq. (27) defines a closed region of policies that replace the NPE. This region, which we term the patent enforcement region (PER), has a particular shape, as shown in Fig. 1. The patent policy will then be in force and will restrict the imitator’s quality reaction such that $s _ { L } { = } \lambda { < } s _ { L } ( \mu )$ , resulting in a PE. Alternatively, if the patent authority sets any policy $( \mu , \lambda )$ outside of the PER (or in what we term the patent nonenforcement region [PNR]), the innovator will not have a profit incentive to meet the patent height and will instead produce at the NPE. For clarification, when considering Figs. 1, 2, 3, 5, and $^ { 6 , }$ any policy set in the PER results in a PE; alternatively, any policy set outside the PER results in the NPE. Below, we briefly discuss the impact that patent policies set within the PER will have on the firms’ product quality decisions

![](/api/attachments/DHM2FWM2/fulltext/images/d6fb6267b4cb581abd7454cf4bff20a7f93547009b87582e959a6e6170745fc5.jpg)  
Fig. 1. The patent enforcement region.

Consider Fig. 2. Within the PER, there are three areas of interest. If the patent authority sets a policy in Region $\mathrm { ~ A ~ } ( \mathrm { i . e . , } \mu { > } s _ { W } ^ { B } , \lambda { < } s _ { L } ^ { B } )$ , then the innovator will develop a higher quality product than it would in the NPE (despite the increase in product development costs), while the patent width forces the imitator to develop a lower quality product than it would in the NPE. That is, in this region, the increased revenue earned by the innovator from greater product differentiation outweighs the increase in production costs associated with meeting the patent height. If the patent authority sets a policy in Region B $( \mathrm { i . e . , } \bar { \mu } { > } s _ { W } ^ { B } , \lambda { > } s _ { L } ^ { B } )$ , then the innovator will develop a better quality product than it would in the NPE. However, despite the restrictive patent width, the imitator also has the incentive to develop a better quality product than it would have in the NPE. Policies in Region B are particularly interesting in that they result in the development of better quality products by both firms. Finally, if the patent authority sets a policy in Region $\mathrm { ~ C ~ } ( \mathrm { i . e . , } \ \mu \mathrm { \bar { < } } s _ { { \scriptscriptstyle W } } ^ { \  B } , \lambda { < } s _ { { \scriptscriptstyle L } } ^ { \  B } )$ , then both the innovator and imitator will develop lower quality products than they would in the NPE. These policies are interesting given the discussion in the popular press. That is, some have argued that it is too easy to attain a patent (that is, the effective patent height is too low), and others have argued that patents provide too much protection (that is, the effective patent width is too wide). The policies in Region C are consistent with low patent heights and wider protections. Interestingly, we find that setting such policies will adversely affect the product quality offered by each firm relative to qualities offered in the NPE. Finally, as shown earlier, we note that any patent policy set outside of the PER will result in the NPE.

![](/api/attachments/DHM2FWM2/fulltext/images/e7b6da5fab45b89a1c8158c85f6ee356aacefef56c56deae8d63427d1355c222.jpg)  
Fig. 2. Three different types of quality equilibrium within the PER.

In summary, this analysis demonstrates the dramatically different implications of various patent policies for product quality decisions by firms. Later, in Section 5, we analyze the welfare implications of policies within the PER. Below, we formalize why the patent system (or the setting of patent height and patent width) is not one-sizefits-all but instead requires customization to specific market parameters if the patent authority hopes to encourage innovation (through larger product improvements) and to improve consumer welfare. Specifically, we consider the impact of the innovator’s cost coefficient (k) for product development on the location and shape of the PER.

Proposition 3. A reduction in the innovator’s product development cost coefficient (k) will shift the PER up and outward.

Fig. 3 illustrates how a reduction in k (or an improvement in the efficiency with which the innovator transforms novel ideas into commercial products) shifts the PER. Firstly, we note that as k decreases, the point of intersection between the PER and the imitator’s quality reaction curve shifts outward; that is, the qualities produced by both firms under the NPE increase along the imitator’s reaction curve. Secondly, we note that the PER shifts up and outward. This shift defines a new set of patent policies that, if set by the patent authority, will replace the NPE. This result has some interesting implications for patent policy. For example, the patent authority may be able to set relatively low patents to foster the diffusion of better quality products in older, traditional industries in which firms are saddled with costly legacy production technologies (or high k). Alternatively, the patent authority may need to set relatively higher patents in newer, knowledge-based industries equipped with more flexible and efficient production technologies (or low k) if it wants to alter the firms’ product quality decisions. Fig. 3 also suggests that industries characterized by more modern, efficient product development infrastructure may provide the patent authority with a larger set of enforceable policies to consider. In summary, Proposition 3 and Fig. 3 imply that it may be inappropriate to apply existing patent policy, designed for innovations in a simpler industrial era, in a uniform way to newer industries in which technology has enabled fundamental improvements in firms’ production capabilities.

![](/api/attachments/DHM2FWM2/fulltext/images/61679b95f460dc41932272b586427f65e467111a15d712acc9d731fc154af428.jpg)  
Fig. 3. Shift in PER from improvement in the innovator’s technology cost coefficient (k).

Having discussed the impact of patent policy instruments on product development in stages 3 and 4, we now consider the impact of these instruments on product pricing in the fifth stage.

Proposition 4. Given policies resulting in a ${ \mathrm { P E } } ,$ an increase in patent height (keeping patent width constant) leads to an increase in the prices charged by both firms.

Proposition 5. Given policies resulting in a PE, a narrowing of patent width (i.e., an increase in k) leads to a decrease in the price charged by the innovator. However, it leads to an increase in the imitator’s price if the difference between $\mu$ and $\lambda$ is large (that is, the firms’ products are highly differentiated) but a decrease in the imitator’s price if the difference is small (that is, the firms’ products are more substitutable).

Given a PE, the equilibrium prices charged in the fourth stage are

$$
p _ {W} (\mu , \lambda) = \frac {2 \mu (\mu - \lambda)}{4 \mu - \lambda} \text { and } p _ {L} (\mu , \lambda) = \frac {\lambda (\mu - \lambda)}{4 \mu - \lambda}.\tag{28 and 29}
$$

The derivatives of both price functions with respect to $\mu$ are positive

$$
\frac {\partial p _ {W}}{\partial \mu} = \frac {2 (4 \mu^ {2} - 2 \mu \lambda + \lambda^ {2})}{(4 \mu - \lambda) ^ {2}} > 0 \text { and } \frac {\partial p _ {L}}{\partial \mu} = \frac {3 \lambda^ {2}}{(4 \mu - \lambda) ^ {2}} > 0.\tag{30 and 31}
$$

Therefore, both firms respond to an increase in $\mu$ (within the PER) by increasing prices. The derivatives of both price functions with respect to $\lambda$ are

$$
\frac {\partial p _ {W}}{\partial \lambda} = - \frac {6 \mu^ {2}}{(4 \mu - \lambda) ^ {2}} <   0 \text { and } \frac {\partial p _ {L}}{\partial \lambda} = \frac {4 \mu^ {2} - 8 \mu \lambda + \lambda^ {2}}{(4 \mu - \lambda) ^ {2}}.\tag{32 and 33}
$$

As we can see, the derivative of the innovator’s price is negative, implying that an increase in $\lambda$ (or narrowing the patent width) will lead to a decrease in the innovator’s price. This is intuitive since an increase in k implies less market power (or more competition from derivative products) for the innovator. However, the derivative of the imitator’s price is signed by the following:

$$
\text {   If   } \mu > \frac {\lambda (2 + \sqrt {3})}{2} \text {   then   } \frac {\partial p _ {W}}{\partial \lambda} > 0; \text {   otherwise,   if   } \mu <   \frac {\lambda (2 + \sqrt {3})}{2} \text {   then   } \frac {\partial p _ {W}}{\partial \lambda} <   0.\tag{34}
$$

In other words, if the products are highly differentiated, then the imitator will respond to an increase in $\lambda$ by increasing its price to capture more revenues from its existing customers. Otherwise, if the products are more substitutable, then the imitator will respond to an increase in $\lambda$ by reducing its price to capture more consumers from the innovator.

## 4.3. Idea generation (stage 2)

In this section, we derive the equilibrium R&D investments in idea generation made by firms in the second stage. The unique equilibrium in stage 2 is (see Appendix for the proof)

$$
\alpha_ {1} = \alpha_ {2} = \frac {1}{2 h} \sqrt {h (V _ {W} - V _ {L})}.\tag{35}
$$

The equilibrium R&D investments are decreasing and convex with respect to h but increasing and concave with respect to $( V _ { W } - V _ { L } )$ . These findings are quite intuitive. We note that $( V _ { W } - V _ { L } )$ may be interpreted as the economic benefit achieved by an innovating firm or the economic incentive for winning the R&D race. Of course, the size of the incentive $( V _ { W } - V _ { L } )$ depends partially on the patent policy set by the patent authority in the first stage. We now examine the impact of the patent policy instruments $( \mu , \lambda )$ on the firms’ incentives to invest in R&D (or idea generation) in the second stage.

Proposition 6. For a given patent height, if the patent authority narrows the patent width (or increases k) then both firms will decrease their R&D expenditures.

Proposition 7. For a given patent width, if the patent authority raises the patent height (or increases l) the impact on the firms’ investments in R&D activities will depend on the size of k, or the efficiency of the innovator’s production capability when transforming a novel idea into a commercial product. Specifically,

(i) if the innovator’s production capability is relatively inefficient (i.e., k is high), then an increase in patent height will lead to a decrease in both firms’ R&D expenditures;

(ii) otherwise, if the innovator’s production capability is relatively efficient (i.e., k is low), then an increase in patent height will lead to an increase in both firms’ R&D expenditures.

For simplicity, we consider the impact of a change in k and a change in l on the difference in second stage payoffs

$$
\frac {\partial \left(V _ {W} - V _ {L}\right)}{\partial \lambda} = - \frac {3 \mu^ {2}}{(4 \mu - \lambda) ^ {2}} <   0 \text {   and   }\tag{36}
$$

$$
\frac {\partial (V _ {W} - V _ {L})}{\partial \mu} = - \frac {1 6 k \mu^ {3} - 4 \mu^ {2} - 8 k \mu^ {2} \lambda + k \mu \lambda^ {2} + 2 \mu \lambda - \lambda^ {2}}{(4 \mu - \lambda) ^ {2}}.\tag{37}
$$

Eq. (36) is negative, implying that, holding patent height constant, a narrowing of patent width (an increase in k) will lead to a decrease in the difference in second stage payoffs. That is, the narrower is the scope of protection, the lower is the economic incentive for firms to invest in R&D.

In contrast, the sign of Eq. (37) (i.e., the impact of a change in patent height on R&D incentives) depends on the size of k. Specifically,

$$
\text { if   } k > \frac {4 \mu^ {2} - 2 \mu \lambda + \lambda^ {2}}{\mu (4 \mu - \lambda) ^ {2}} \text {   then   } \frac {\partial (V _ {W} - V _ {L})}{\partial \mu} <   0.\tag{38}
$$

That is, if the innovator’s production capability is relatively inefficient, then an increase in the patent height (which given a high k will be costly for the innovator to attain in stage 3) will reduce the difference in second stage payoffs and, therefore, decrease both firms’ R&D expenditures in stage 2. Otherwise,

$$
\text { if } k <   \frac {4 \mu^ {2} - 2 \mu \lambda + \lambda^ {2}}{\mu (4 \mu - \lambda) ^ {2}} \text { then } \frac {\partial (V _ {W} - V _ {L})}{\partial \mu} > 0.\tag{39}
$$

That is, if the innovator’s production capability is relatively efficient, then an increase in the patent height (which given a low k will be relatively cheap for the innovator to attain in stage 3) will increase the difference in second stage payoffs and, therefore, increase both firms’ R&D expenditures in stage 2.

These results have significant implications for regulators setting patent policy to stimulate R&D activities and encourage innovation. Not surprisingly, a wider scope of protection from imitation will provide incentive for more R&D intensity. Similarly, setting higher patent heights in industries characterized by efficient, modernized infrastructures for product development will increase economic incentives for R&D. Alternatively, setting higher patent heights in industries characterized by less efficient, legacy infrastructures will reduce economic incentives for R&D. As a result, regulators must be particularly careful to consider the production capabilities of competing firms before setting patent height since increasing the patent height may actually reduce R&D spending in certain contexts.

## 5. Welfare analysis

In the previous section, we characterized the PER or the set of patent policies $( \mu , \lambda )$ that result in a PE. This region defines the set of enforceable patent policies from which a patent authority may choose to maximize socia welfare. In this section, we examine the welfare implications of these policies.

## 5.1. Patent policy and social welfare

In the first stage, the patent authority sets a policy $( \mu , \lambda )$ with the goal of maximizing social welfare. Current social welfare is defined as the sum of consumer surplus and producer surplus. Therefore, given the product qualities and prices set by both firms, the social welfare function is given by

$$
\omega = \int_ {0} ^ {1 - \frac {p _ {W} - p _ {L}}{s _ {W} - s _ {L}}} (s _ {W} - s _ {W} Q) d Q + \int_ {1 - \frac {p _ {W} - p _ {L}}{s _ {W} - s _ {L}}} ^ {1 - \frac {p _ {L}}{s _ {L}}} (s _ {L} - s _ {L} Q) d Q - \frac {k s _ {W} ^ {2}}{2}.\tag{40}
$$

[See Fig. 4 for a graphical representation of the sum of the first two integrals (or the sum of the benefits accrued to producers and consumers) in Eq. (40)] Substituting the equilibrium prices and solving gives

$$
\omega = \int_ {0} ^ {\frac {2 s _ {W}}{4 s _ {W} - s _ {L}}} (s _ {W} - s _ {W} Q) d Q + \int_ {\frac {2 s _ {W}}{4 s _ {W} - s _ {L}}} ^ {\frac {3 s _ {W}}{4 s _ {W} - s _ {L}}} (s _ {L} - s _ {L} Q) d Q - \frac {k s _ {W} ^ {2}}{2} = \frac {s _ {W} \left(1 2 s _ {W} ^ {2} - s _ {W} s _ {L} - 2 s _ {L} ^ {2}\right)}{2 (4 s _ {W} - s _ {L}) ^ {2}} - \frac {k s _ {W} ^ {2}}{2}.\tag{41}
$$

To analyze the welfare implications of setting alternative patent policies, we substitute $\mu$ for $s _ { W }$ and $\lambda$ for $s _ { L }$ . Therefore, the patent authority’s objective becomes

$$
\begin{array}{l} \text { Maximize } _ {\mu , \lambda} \omega = \frac {\mu (1 2 \mu^ {2} - \mu \lambda - 2 \lambda^ {2})}{2 (4 \mu - \lambda) ^ {2}} - \frac {k \mu^ {2}}{2} \\ \text { subject   to: } \\ \mu \left(1 8 4 3 2 k \mu (k \mu - 1) + 3 9 2 + 1 9 2 \sqrt {(- 6 k \mu (2 3 0 4 k ^ {2} \mu^ {2} - 1 5 3 6 k \mu + 4 9))}\right) \\ \lambda \leq \frac {2 (2 3 0 4 k ^ {2} \mu^ {2} + 4 9)}{(2 3 0 4 k ^ {2} \mu^ {2} + 4 9)} \\ \mu \geq \lambda \\ \mu > 0, \lambda > 0 \end{array} \tag {1}\tag{42}
$$

where the three constraints define the PER. To examine the welfare implications of alternative patent policies, we present a geometric interpretation. The patent authority’s objective function can be transformed as

$$
\lambda = \frac {\mu \Big (1 6 \omega + 8 k \mu^ {2} - \mu - \sqrt {(- 1 9 2 \omega \mu + 9 7 \mu^ {2} - 9 6 k \mu^ {3})} \Big)}{2 (2 \omega + 2 \mu + k \mu^ {2})}.\tag{43}
$$

We use Eq. (43) to map the objective function onto the $( \mu , \lambda )$ plane as a series of isowelfare curves where each curve maps all combinations of $( \mu , \lambda )$ that generate a specific level of social welfare.

Fig. 5 maps three isowelfare curves on the $( \mu , \lambda )$ plane. Note that higher curves represent higher levels of social welfare since the derivative of the social welfare function with respect to $\lambda$ is positive

$$
\frac {\partial \omega}{\partial \lambda} = \frac {\mu^ {2} (2 0 \mu - 1 7 \lambda)}{2 (4 \mu - \lambda) ^ {3}} > 0.\tag{44}
$$

Using Fig. 5, we can describe the directional impact of setting various patent policies on the level of social welfare.

![](/api/attachments/DHM2FWM2/fulltext/images/a984e77934034319909b2f51ef99c0adceb3420af25ec82b72b68dae569a681a.jpg)  
Fig. 4. Graphical representation of the sum of consumer and producer benefits (stage 5).

Firstly, we consider the set of patent policies in the PER that lies on isowelfare curve $\left( \omega _ { \mathrm { N P E } } \right)$ , the curve that intersects the NPE. We observe that since this set of patent policies lie on the same isowelfare curve as the NPE, they generate the same level of social welfare than that generated in an unregulated market. Therefore, while these policies may replace the NPE (since they provide the innovator with profit incentive to meet the height and patent the product), they only change the distribution of social welfare among the firms and consumers, not the level of social welfare itself. We will examine the impact of alternative patent policies on welfare distribution in Section 5.2. Secondly, we observe that the set of patent policies in the PER that lies above isowelfare $\left( \omega _ { \mathrm { N P E } } \right)$ will generate higher levels of social welfare than is generated in the NPE. Thirdly, we observe that the set of patent policies that lies below the isowelfare curve will generate lower levels of social welfare than in the NPE. This observation formalizes and supports the arguments in the popular press that low patent heights and overly wide patent protections may be socially inefficient. In fact, in Fig. 5, the policy in the PER with the lowest height and a full scope of protection (k=0) generates the lowest level of social welfare in the PER.

![](/api/attachments/DHM2FWM2/fulltext/images/9c81b5765be33e907b7213d98b1383fb2a3610643b8440483220ae4b8fd278a4.jpg)  
Fig. 5. Patent policy and social welfare.

We note that the set of patent policies that lies outside the PER will result in the NPE $\left( \mathrm { i . e . , ~ } \omega _ { \mathrm { N P E } } \right)$ since the innovator will not have profit incentive to meet the height and patent its product if these policies are set by the patent authority. We also note that the policy $( \mu ^ { * } , \lambda ^ { * } )$ that maximizes social welfare is the policy on the boundary of the PER at which the isowelfare curve is tangent to the PER [see isowelfare curve $\omega ^ { * }$ in Fig. 5]. This analysis suggests that the optimal patent design is characterized by a relatively high height (i.e., high within the context of the enforceable set) with a moderate scope of protection. This policy combination generates the most social welfare among those policies that provide the innovator with profit incentive to attain a patent.

Based on this graphical interpretation, we make a final observation. From Fig. 5, we see that there exists a set of patent policies within the PER that provide the innovator with a full scope of protection, k=0. An interesting observation is that the policies within the PER characterized by $\begin{array} { r } { \left( \mu { > } \frac { 1 8 - \sqrt { 6 5 } } { 4 8 k } , \lambda = 0 \right) } \end{array}$ generate more social welfare than is generated in an unregulated duopoly market (i.e., the NPE). That is, the patent authority may improve social welfare by setting a policy that gives the innovator full protection from imitation, but only if the patent height is set sufficiently high.

## 5.2. Patent policy and welfare distribution

In the previous section, we used a transformation of the patent authority’s objective function (i.e., the social welfare function) to examine the impact of policies in the PER on the level of social welfare generated by a given patent policy. In this section, we use similar transformations of the consumer welfare function and the imitator welfare function within the PER to examine the impact of various policies on the distribution of social welfare among firms and consumers. In our model, consumer welfare is given by

$$
\Omega = \omega - V _ {W} - V _ {L} = \frac {(4 s _ {W} + 5 s _ {L}) s _ {W} ^ {2}}{2 (4 s _ {W} - s _ {L}) ^ {2}}.\tag{45}
$$

Substituting $( \mu , \lambda )$ for $( s _ { W } , s _ { L } )$ gives

$$
\Omega = \frac {(4 \mu + 5 \lambda) \mu^ {2}}{2 (4 \mu - \lambda) ^ {2}}.\tag{46}
$$

Therefore, the transformation of the consumer surplus function is

$$
\lambda = \frac {\mu (1 6 \Omega + 5 \mu - \sqrt {\mu (1 9 2 \Omega + 2 5 \mu)})}{4 \Omega}.\tag{47}
$$

In addition, imitator welfare is given by $R _ { L }$ . Substituting $( \mu , \lambda )$ for $( s _ { W } , s _ { L } )$ gives

$$
\Psi = R _ {L} = \frac {\mu \lambda (\mu - \lambda)}{(4 \mu - \lambda) ^ {2}}.\tag{48}
$$

Therefore, the transformation of the Imitator’s welfare function is

$$
\lambda = \frac {\mu (8 \Psi + \mu - \sqrt {\mu (\mu - 4 8 \Psi)})}{2 (\Psi + \mu)}.\tag{49}
$$

Fig. 6 maps the isowelfare curves for the consumers, the imitator, and social welfare that intersect the NPE. This mapping generates five areas of interest labeled in Fig. 6, with the patent policies within each area having a different impact on welfare distribution when compared to the distribution in the NPE.

Initially, we observe that for the entire PER innovator profit improves since it is the innovator<sup>T</sup>s profitmaximizing quality and patent decisions that define this region. Therefore, the innovator is always better off (or at least as well off) in the PER than at the NPE. We now consider the five areas in Fig. 6 to examine the impact of alternative patent policies on the welfare of the remaining stakeholders.

The policies in Area F lie below all three isowelfare curves. Therefore, these policies, if set by a patent authority, will benefit the innovator at the expense of consumers and the imitator. Furthermore, these policies will result in a decrease in social welfare. These policies may be considered bad options by the patent authority since the innovator benefits at the expense of the welfare of society and all other stakeholders. We note that these policies are generally characterized by lower patent heights.

The policies in Area G lie above all of the isowelfare curves. Therefore, these policies, if set by a patent authority, will improve the welfare of all stakeholders—i.e., innovator, imitator, and consumers alike. These policy options may be considered good options by the patent authority since these policies make all stakeholders better off. We note that these policies are generally characterized by higher patent heights than those policies in Area F.

The policies in Area H lie above the social welfare curve but below the imitator’s and consumers’ curves. Therefore, these policies (as in Area F) benefit the innovator at the expense of the consumers and the imitator. However, total social welfare increases in this case. While these policies may be more attractive (or palatable) to the patent authority than those in Area F, the authority may still have concerns about setting a policy that simultaneously limits competition and adversely affects consumer welfare.

![](/api/attachments/DHM2FWM2/fulltext/images/8e56739d81a0a305c73e04cbbe324221a1136e06c4a4083eb9d2dca0566c91be.jpg)  
Fig. 6. Patent policy and social welfare distribution.

The policies in Area J lie above the social welfare and imitator curves but below the consumer curve. Therefore, these policies benefit both firms but at the expense of consumers. In this case, the overall impact of this distribution is to increase total social welfare. However, again the patent authority may have concerns about setting a patent policy that makes firms better off at the expense of consumers.

Finally, the policies in Area K lie above the social welfare and consumer welfare curves but below the imitator curve. Therefore, these policies benefit both the innovator and consumers at the expense of the imitator. This area shows that providing the innovator with full protection from imitation may benefit consumers and improve social welfare as long as the patent height is set sufficiently high.

In this section, we acknowledged that the patent authority may be interested not only in the level of social welfare generated by a patent policy but also in the distribution of that welfare among firms and consumers. By mapping the consumer, imitator, and social welfare curves onto the (l, k) plane in Fig. 6, we were able to examine the impact of patent policies in the PER on welfare distribution and briefly comment on the attractiveness of various policies to the patent authority.

## 6. Conclusions and implications

We have developed a model that integrates the patent policy instruments set by public policy (patent height and patent width), the strategic decisions made by firms (R&D investments, product innovation, product imitation, patent decision, and pricing), the purchasing decisions made by consumers, and the market parameters characterizing the context. Although this integrated model does not capture all of the potential complexity of determining the implications of alternative patent policies, it does offer a realistic perspective for framing the discussion of many of the broader questions.

Question (1) Is granting a patent to an innovating firm always in the public interest?

In the context of the model, the answer is no. In fact, the critics that claim patent protection is too low or too wide have good reason to be concerned. The welfare trade-offs between these policy instruments are more complex than previously suggested in the literature. We show that there exists a feasible subset of patent policies that, if set by the patent authority, will decrease social welfare or result in a distribution of welfare that may be considered unacceptable (or unfair) to the authority (see Figs. 5 and 6).

Question (2) Should patent policy be customized for each industry or group of industries (as opposed to applied uniformly across industries)?

In the context of our model, the answer is yes. The optimal patent design is determined by the parameters of the firms and the consumers that often differ across industries. Therefore, those who suggest that policies designed for traditional industries may not be appropriate to apply to computer-based industries are likely correct in this assertion.

Question (3) Should patent policy exist at all?

This question is open for debate. Based on our model, one is tempted to argue for a customized patent policy for each industry as suggested in the answer to Question 2. However, we note that in this model, the implementation costs—the costs associated with collecting the data (e.g., customer preferences, firm R&D, and product development cost structures) necessary to design and enforce customized policies—are ignored. Realistically, policymakers often face substantial implementation costs, which may make customization too costly and in some cases impossible. Currently, policymakers deal with this data complexity by setting a uniform policy across industries. This, of course, has costs of its own. As demonstrated in the model, a uniform policy is likely to be nonoptimal for any given industry or time. Therefore, when considering the costs of designing and enforcing patent policy, the broader policy trade-offs for society are

design a customized policy for each individual or group of industries resulting in higher implementation costs but more incentives for innovation;

<sup>!</sup> design a uniform policy to apply across all industries resulting in lower implementation costs but uncertain impact on incentives for innovation; and

<sup>!</sup> do not have a patent policy at all resulting in no implementation costs but no additional incentives for innovation.

Although our model does not directly address the welfare trade-offs between policy implementation costs and policy effectiveness, it can be extended to examine this critical issue by relaxing the assumption that implementation costs are zero. In addition, the model could be extended to consider the effectiveness of applying a specific patent policy uniformly across diverse industries.

## Acknowledgements

The authors would like to thank the editors and the anonymous reviewers for their many constructive suggestions. Helpful comments on earlier drafts of this work were received from David Meader, John Wooders, and Daniel Zeng.

![](/api/attachments/DHM2FWM2/fulltext/images/959cb2689d4ed0ed7250ea93f713a452edd75dfcaf22946b7a6919f1ff06169e.jpg)  
Fig. 7. Reaction curves of success rate choice (stage 2).

## Appendix A

Lemma 1. There exists a unique success rate equilibrium in the first stage (idea generation).

The following derivation is based on Beath et al.[3]. The second derivative of first stage profit is negative,

$$
\frac {\partial}{\partial \alpha_ {1} ^ {2}} \Pi_ {1} = - \frac {2 \alpha_ {2} (V _ {W} - V _ {L})}{(\alpha_ {1} + \alpha_ {2}) ^ {3}} - h <   0.
$$

Therefore, we solve for the FOC,

$$
\frac {\partial}{\partial \alpha_ {1}} \Pi_ {1} = \frac {\alpha_ {2} (V _ {W} - V _ {L})}{(\alpha_ {1} + \alpha_ {2}) ^ {2}} - h \alpha_ {1} = 0.
$$

We now need to work out reaction functions:

(1) define $\begin{array} { r } { T ( \alpha _ { 1 } , \alpha _ { 2 } ) = \frac { \alpha _ { 2 } \left( V _ { W } - V _ { L } \right) } { \left( \alpha _ { 1 } + \alpha _ { 2 } \right) ^ { 2 } } - h \alpha _ { 1 } ; } \end{array}$

(2) for all $\begin{array} { r } { \alpha _ { 2 } { > } 0 , \ T ( 0 , \alpha _ { 2 } ) = \frac { \left( V _ { W } - V _ { L } \right) } { \alpha _ { \cdot } ^ { 2 } } { > } 0 ; } \end{array}$

(3) for all $\begin{array} { r } { \alpha _ { 2 } { > } 0 , \ \operatorname* { l i m } _ { \alpha _ { 1 } \to \infty } T ( \alpha _ { 1 } ^ { - 2 } \alpha _ { 2 } ) = - \infty ; } \end{array}$ and

(4) for all $\textstyle \alpha _ { 1 } { > } 0 , \ \alpha _ { 2 } { > } 0 , \ \frac { \partial } { \partial \alpha _ { 1 } } T ( \alpha _ { 1 } , \alpha _ { 2 } ) = \frac { \partial } { \partial \alpha _ { 1 } ^ { 2 } } \prod _ { 1 } { < } 0$ as already shown in the beginning.

These conditions guarantee a well-defined reaction curve, and we can find the property of the reaction curve from the following,

$$
\frac {\partial}{\partial \alpha_ {2}} T (\alpha_ {1}, \alpha_ {2}) = \frac {(V _ {W} - V _ {L}) (\alpha_ {1} - \alpha_ {2})}{(\alpha_ {1} + \alpha_ {2}) ^ {3}},
$$

$( \alpha _ { 1 } - \alpha _ { 2 } ) { > } 0 : \alpha _ { 1 } ( \alpha _ { 2 } )$ has a positive slope; $( \alpha _ { 1 } - \alpha _ { 2 } ) { < } 0 : \alpha _ { 1 } ( \alpha _ { 2 } )$ has a negative slope:

From these properties, we can describe the reaction function, as shown in Fig. 7. And there is a unique equilibrium choice $\begin{array} { r } { \alpha _ { 1 } = \alpha _ { 2 } = \frac { 1 } { 2 h } \sqrt { h ( V _ { W } - V _ { L } ) } } \end{array}$ from solving:

ð Þ1 $\alpha _ { 1 } = \alpha _ { 2 } ;$

ð Þ2 $T ( \alpha _ { 1 } , \alpha _ { 2 } ) = 0 .$

## References

[1] A. Barua, C. Kriebel, T. Mukhopadhyay, An economic analysis of strategic information technology investments, MIS Quarterly 15 (3) (1991 (September)) 313–331.

[2] T. Baumann, Gathering storm clouds for internet patents, Intellectual Property and Technology Law Journal 13 (10) (2001(October)) 1 –4.

[3] J. Beath, Y. Katsoulacos, D. Ulph, Strategic R&D policy, Economic Journal 99 (395) (1989) 74 – 83 (Supplement).

[4] S. Besen, L. Raskin, An introduction to the law and economics of intellectual property, Journal of Economic Perspectives 5 (1) (1991 (Winter)) 3 – 27.

[5] H. Cremer, J.-F. Thisse, Commodity taxation in a differentiated oligopoly, International Economic Review 35 (3) (1994 (August)) 613– 633.

[6] T. Dijk, Patent height and competition in product development, Journal of Industrial Economics 44 (2) (1996 (June)) 151–167.

[7] S. Durant, T. Chuang, E-commerce patents and shifting balances in patent law, IEEE Communications Magazine (2000 (July)) 106– 110.

[8] J. Gabszewicz, J. Thisse, Price competition, quality and income disparities, Journal of Economic Theory 2 (3) (1979 (June)) 340– 359.

[9] N. Gallini, Patent policy and costly innovation, RAND Journal of Economics 23 (1) (1992 (Spring)) 52– 63.

[10] E. Gal-Or, Strategic and non-strategic differentiation, Canadian Journal of Economics 20 (2) (1987 (May)) 340– 356.

[11] R. Gilbert, C. Shapiro, Optimal patent length and breadth, RAND Journal of Economics 21 (1) (1990 (Spring)) 106– 112.

[12] R. Hsu, Maintaining high living standards through innovation, Strong Patents, Communications of the ACM 41 (10) (1998 (October)) 27 – 28.

[13] M. Kamien, N. Schwartz, Patent life and R&D rivalry, The American Economic Review 64 (1) (1974 (March)) 183–187.

[14] P. Klemperer, How broad should the scope of patent protection be? RAND Journal of Economics 21 (1) (1990 (Spring)) 113–130.

[15] L. Lambertini, Choosing roles in a duopoly for endogenously differentiated products, Australian Economic Papers 35 (67) (1996 (December)) 205–224.

[16] L. Lambertini, R. Orsini, Vertically differentiated monopoly with a positional good, Australian Economic Papers 41 (2) (2002 (June)) 151–163.

[17] L. Lambertini, R. Orsini, Monopoly, Quality, and Network Externalities, Working Paper (October 15, 2003), University of Bologna, http://www.dse.unibo.it/lamberti/ RaiKeioFinal.pdf.

[18] G. Loury, Market structure and innovation, The Quarterly Journal of Economics 93 (3) (1979 (August)) 395– 410.

[19] J. Marsden, D. Pingry, IT reference disciplines—Andy Whinston, a case study, in: C. Holsapple, V. Jacob, H. Rao (Eds.), Business Modelling: Multidisciplinary Approaches— Economics, Operational, and Information Systems Perspectives, Kluwer Academic Publishers, 2002, In Honor of Andy Whinston.

[20] K. Moorthy, Product and price competition in a duopoly model, Marketing Science 7 (2) (1988 (Summer)) 141– 168.

[21] K. Moorthy, I. Png, Market segmentation, cannibalization, and the timing of product introductions, Management Science 38 (3) (1992 (March)) 345–359.

[22] T. Mullaney, S. Ante, Info Wars, Business Week Online (2000 (June 5)).

[23] W. Nordhaus, Invention, Growth, and Welfare, The MIT Press, 1969.

[24] T. O’Donoghue, S. Scotchmer, J. Thisse, Patent breadth, patent life, and the pace of technological progress, Journal of Economics and Management Strategy 7 (1) (1998 (Spring)) 1 – 32.

[25] S. Patton, Barnesandnoble.com fights back, CIO (2001 (September 15)) 78– 84.

[26] K. Rivette, D. Kline, Discovering New Value in Intellectual Property, Harvard Business Review (2000 (January–February)) 54– 66.

[27] F. Scherer, Nordhaus’ theory of optimal patent life: a geometric reinterpretation, The American Economic Review 62 (3) (1972 (June)) 422 – 427.

[28] P. Schmitt, The impact of a marginal cost increase on price and quality: theory and evidence from airline market strikes, Australian Economic Papers 41 (3) (2002 (September)) 282– 304.

[29] S. Scotchmer, Protecting early innovators: should secondgeneration products be patentable? RAND Journal of Economics 27 (2) (1996 (Summer)) 322– 331.

[30] S. Scotchmer, J. Green, Novely and disclosure in patent law, RAND Journal of Economics 21 (1) (1990 (Spring)) 131– 146.

[31] A. Shaked, J. Sutton, Relaxing price competition through product differentiation, Review of Economic Studies 49 (1) (1982 (January)) 3– 13.

[32] A. Spence, Monopoly, quality and regulation, Bell Journal of Economics 6 (2) (1975 (Autumn)) 417– 429.

[33] P. Tandon, Optimal patents with compulsory licensing, The Journal of Political Economy 90 (3) (1982 (June)) 470– 486.

Matt E. Thatcher is Assistant Professor of Management Information Systems at the Eller College of Management at the University of Arizona, where he has been a member of the faculty since 1997. He holds a BS in economics and an MA and PhD in information technology from the Wharton School of the University of Pennsylvania. His research examines the economic impacts of information technology (IT) including the business value of IT investments, the impact of patent policies on technology innovation, product design, and consumer welfare, and the strategic uses of information in the services industry.

Taeha Kim is Assistant Professor of Management Information Systems in the School of Management at the George Mason University. He received a PhD from the University of Arizona in 2002 and an MBA and a BBA from Seoul National University. His primary research interests include intellectual property rights, digital rights management, and strategic issues of software competition.

David E. Pingry is a Professor of Management Information Systems and Economics at the Eller College of Management at the University of Arizona. Previously, Professor Pingry was on the faculty at Virginia Tech, and he has held visiting faculty positions at Purdue University, Texas A and M, and the University of Connecticut. His current interests are decision support systems, patent policy, and IT productivity.
