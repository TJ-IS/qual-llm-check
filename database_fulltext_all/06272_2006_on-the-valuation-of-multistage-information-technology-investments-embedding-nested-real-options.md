---
otero_id: 6272
otero_key: "TVV7WYGK"
title: "On the Valuation of Multistage Information Technology Investments Embedding Nested Real Options"
authors: "Michel Benaroch; Sandeep Shah; Mark Jeffery"
year: "2006"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222230108"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# On the Valuation of Multistage Information Technology Investments Embedding Nested Real Options

Michel Benaroch , Sandeep Shah & Mark Jeffery

To cite this article: Michel Benaroch , Sandeep Shah & Mark Jeffery (2006) On the Valuation of Multistage Information Technology Investments Embedding Nested Real Options, Journal of Management Information Systems, 23:1, 239-261

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222230108

![](/api/attachments/TVV7WYGK/fulltext/images/92fcf543f1e53380ed5f4953676b0c092be2d43b99c8397a419c528171fed04a.jpg)

Published online: 08 Dec 2014.

![](/api/attachments/TVV7WYGK/fulltext/images/e4e3752ad308d889ee7b3d402a6308cb814c6996dc970570eeb4a6051364966e.jpg)

Submit your article to this journal

![](/api/attachments/TVV7WYGK/fulltext/images/d98c4af84866afb6d27d4f5e5c661cf8dd85c140be64ab2bd40e88ff0ef68362.jpg)

Article views: 6

![](/api/attachments/TVV7WYGK/fulltext/images/84e23553a0ffa84b740008b7811725f7e8136241d7d4a979017eb1585ce79a8b.jpg)

View related articles

![](/api/attachments/TVV7WYGK/fulltext/images/e972e8b9c459fbdab8f04b8e5ad7f5329af747131e0287e8315ce955b1a97cb4.jpg)

Citing articles: 1 View citing articles

# On the Valuation of Multistage Information Technology Investments Embedding Nested Real Options

MICHEL BENAROCH, SANDEEP SHAH, AND MARK JEFFERY

MICHEL BENAROCH is a Professor of Information Systems in the Martin J. Whitman School of Management, Syracuse University. His current research interests focus on using real-option techniques to evaluate IT investments and manage their risk in an IT portfolio context, as well as on designing declarative ontology-centered modeling formalisms. He has published in a variety of outlets, including Information Systems Research, Journal of Management Information Systems, MIS Quarterly, IEEE Transactions on Knowledge and Data Engineering, International Journal of Human– Computer Studies, Information Retrieval, Decision Sciences, International Journal of Economic Dynamics and Control, and Decision Support Systems.

SANDEEP SHAH is a Research Fellow in the Center for Research on Technology and Innovation at the Kellogg School of Management. He has an MBA from the Kellogg School. Mr. Shah has more than ten years of experience in product development and management in technology, telecommunications, and wireless industries. He worked as an associate at the Telecommunications Development Fund (TDF), a venture capital firm focused on early stage telecommunications and technology companies. He is presently a Senior Analyst at Sapient Consulting.

MARK JEFFERY is an Associate Professor of Technology in the Center for Research on Technology and Innovation at the Kellogg School of Management. His research interests include technology portfolio management and real options. He has over 30 peer-reviewed publications in management, scientific, and technology journals, including a chapter on return on investment analysis in the Wiley Internet Encyclopedia. He has also developed 14 original case studies that are used in the Kellogg MBA course he teaches on technology portfolio management and in multiple Kellogg executive programs, including the three-day CIO/CXO executive program Driving Strategic Results Through IT Portfolio Management, which he directs.

ABSTRACT: As real options analysis (ROA) is being applied to increasingly complex information technology (IT) investment problems, a concern arises over the use of heuristic ROA models that are simpler to apply but can produce overvaluations. A good example is the application of a heuristic nested variation of the Black–Scholes (BS) model to the evaluation of interrelated IT investments as nested options. This particular heuristic BS model could overvalue by more than 100 percent. Using a binomial model that is custom-tailored to a generic IT investment embedding nested options as the “baseline,” we identify conditions under which the degree of overvaluation of this heuristic BS model is severe and unpredictable. Moreover, upon examining the structure of the custom-tailored binomial model, we identify the reason for overvaluation and derive a more accurate nested variation of the BS model. These findings should serve as a cautionary message about the use of untested heuristic ROA models.

KEY WORDS AND PHRASES: Black–Scholes model, interdependent investments, IT investment, nested real options, real options.

THE GROWING CONTRIBUTION OF REAL OPTIONS ANALYSIS (ROA) to information technology (IT) investment management is becoming apparent on two dimensions. During the past five years, over 50 information systems (IS) research articles on real options have been published, some in the most prestigious journals, and several IS textbooks started referencing ROA (e.g., [24, 32, 34]) or even fully covering the subject (e.g., [23]). In parallel, practitioners’ interest in applying ROA to IT investment problems has been increasing, as evident from studies with companies such as FedEx [35], Yankee 24 [5], a European auto parts manufacturer [27], Autoliv Inc. [29], an Irish Manufacturer [21], the Irish Fisheries Board [11], Naples Community Healthcare [10], a German dot-com firm [8], IBM [2], Deutsche Bank [22], Teradata [7], and an Irish financial institution [6].

With the growth in reliance on ROA, it is vital that ROA be applied correctly and accurately. ROA has been, and is still being, touted on the grounds that net present value (NPV) analysis undervalues risky investments and leads to underinvestment in IT. Yet, a recent Harvard Business Review article raises a concern voiced by chief financial officers (CFOs) who tell us that real options overestimate the value of uncertain projects [33]. We believe that one reason for this concern is the use of heuristic option valuation models that usually simplify the numeric complexities of ROA but produce only approximate valuations.<sup>1</sup>

A good example is a heuristic variation of the Black–Scholes (BS) model, which Bardhan et al. [2] used to evaluate a portfolio of interrelated IT investments as nested options. These authors’ model represents an initial attempt to develop a computationally simple heuristic for addressing a challenging IT investment problem. Their model does make the valuation of nested options more tractable, but we will show that it produces overvaluations. We recognize that their paper’s main focus and related developments are still valid, but ask whether their model’s valuations are acceptable approximations and whether there are other models that may provide more accurate valuations.

This research is concerned with the adequacy of heuristic valuations for IT investments embedding nested options. For such investments, a poor approximate valuation of one option is propagated to the valuation of other options in ways that can be unpredictable. More specifically, take the case of a sequential multiproject IT investment, where project i spawns, or enables undertaking, project i + 1 as a contingent follow-up investment opportunity. From an ROA perspective, each project can be treated as an option and the sequence of projects as a chain of nested options. ROA normally evaluates such a chain of options by working backward, starting with the innermost option (i.e., the last-stage project). When the value of an inner option is improperly factored into the value of a predecessor option, a valuation error occurs. For example, in Bardhan et al.’s [2] heuristic model, an error occurs because the value of option (stage) i + 1 is factored into the value of option (stage) i in a way that assumes that stage i + 1 is subject to the same sources of uncertainty affecting stage i. This kind of error would be propagated to earlier options and compounded to the point where the valuation result for the entire chain can distort reality. This concern is a pragmatic one, because many IT investments embed nested options and can be evaluated as such. In fact, Copeland and Tufano argue that most capital investments involve nested options: “in most cases, a company’s investments are multistaged, and at each step the company may push ahead or pull out after gaining new information” [13, p. 91].

To further focus the discussion, we make a distinction between intraproject and interproject nested options. In the case of intraproject nested options, the options are embedded in a single IT investment, and so they have the same underlying asset and they can overlap in time [3, 17]. We will not deal with these options hereafter, but refer the interested reader to Benaroch [3] and Trigeorgis [30] for a discussion of their valuation issues. By contrast, interproject nested options are embedded in sequential multistage IT investments, where each stage involves its own payoffs and sources of uncertainty. Hence, the options have different underlying assets. IT investments embedding such nested options have been studied extensively in the IS literature [2, 7, 14, 16, 17, 27].

The goal of this research is to examine the basis for our concern over the heuristic valuation of interproject nested options and to offer a way to address this concern. More specifically, we examine the adequacy of the heuristic variation of the BS model utilized by Bardhan et al. [2]. This untested model is tempting to use because its closed-form solution is much simpler to apply, but we will show that under certain conditions, it could overvalue investments embedding nested options by more than 100 percent. By examining the structure of a binomial model that is custom-tailored to a generic IT investment problem embedding nested options, we are able to identify the reason for the overvaluation and offer an alternative nested version of the BS model that corrects for the error. In addition, using the custom-tailored binomial model as the “baseline,” we illustrate the degree of overvaluation that the heuristic valuation model produces under different conditions.

The significance of this study and its findings goes to the heart of the ongoing debate over the role of real options in IS research and practice. A recent International Conference on Information Systems (ICIS) panel of top researchers in real options and IT investment evaluation surfaced two divergent perspectives on how ROA could be useful in IT investment decision making [26]. We believe that our study is making a contribution to both perspectives. One perspective is worried about problematic assumptions of typical option valuation models [35], difficulties in estimating option parameters [4, 27], and a complexity in communicating ROA to IS executives [15]. This perspective therefore holds that ROA need not necessarily be precise, as it should be used mainly for gaining insight. As one panel member explained: “IS researchers have been trying to steer business and IS executives away from fixating on a single number and instead to use ROA to gain insights into future possibilities enabled by an IT investment” [26, p. 142]. Our paper suggests that this perspective must be sensitive to the fact that imprecision in ROA and reliance on heuristic valuations can certainly lead to incorrect insights, at least in the case of nested options.

The second perspective, on the other hand, holds that:

We’ve emphasized [here] the importance of insight . . . but we shouldn’t push insight . . . because in the end, real options and NPV are supposed to give us more precise ways of deciding whether to pursue a project or not. . . . the direction that we have to go in . . . is to push for preciseness. [26, p. 151]

We believe that our study represents another step in the push toward preciseness in applying ROA.

## Valuation of Simple Options

SINCE OUR OBJECTIVE IS TO CONTRAST ADAPTATIONS of two fundamental option valuation models—the discrete-time binomial model and the continuous-time BS model [20]—to the valuation of investments embedding nested options, it is important to first understand how these fundamental models value simple real options. We hereafter employ the following notations: C is the value of a call option;<sup>2</sup> V is the value of the uncertain underlying asset (usually the present value of investment payoffs); σ is the volatility (or variability) of V; I is option’s exercise price (usually the present value of investment cost); r is the discount factor equaling $1 + r _ { f } ,$ where $r _ { f }$ is the riskfree interest rate; and T is the option’s time to maturity.

The binomial model assumes that V follows a binomial multiplicative diffusion process. Starting at time $t _ { 0 } = 0 ,$ , by time $t _ { 1 } = t _ { 0 } + \Delta t$ , V may rise to uV with probability q or fall to dV with probability $1 - q ,$ , where $u = e ^ { \sigma \sqrt { \Delta t } } > 1 , d = 1 / u < 1$ , and $d < r < u . \mathrm { A s }$ seen in Figure 1a, a binomial tree for the underlying asset is built in this fashion for n of time periods, where $\Delta t = T / n$ . To compute the value of a call option on $V ,$ we create a second binomial tree for the option value, as seen in Figure 1b. The terminal nodes in the binomial option tree represent the terminal value of the option at time T; for example, the topmost terminal node is $C _ { u u } = \operatorname* { m a x } ( 0 , u ^ { 2 } V - I )$ . By working backward in the binomial option tree and setting $p \equiv ( r - d ) / ( u - d )$ , the value of a preceding node is computed using the formula

$$
C = \frac {p C _ {u} + (1 - p) C _ {d}}{r}.\tag{1}
$$

Equation (1) can be applied to determine the values of the call option at time $t _ { 0 } + \Delta t .$ $C _ { u } .$ and $C _ { d } ,$ and then to similarly determine the value of the option at time $t _ { 0 } .$ In this fashion, Equation (1) can be applied to an option that matures in n time periods (where $\Delta t = T / n )$

![](/api/attachments/TVV7WYGK/fulltext/images/b6e58874fca365048a07ae943e7b1e71da9aa864933177ba776a9c412178e320.jpg)  
(a) underlying asset binomial tree  
(b) option binomial tree  
Figure 1. Binomial Option Valuation Model

In the BS model, the value of a call option is its discounted expected terminal value, $E [ C _ { T } ]$ . The present value of a call is given by $C = e ^ { - r T } E [ C _ { T } ] .$ , where $e ^ { - r T }$ is the riskneutral present value factor. Given that $C _ { T } = \operatorname* { m a x } ( 0 , V _ { T } - I )$ , and assuming that $V _ { T }$ is log-normally distributed, and where $N ( \cdot )$ is the cumulative normal distribution, the present value of a call option has the following closed-form solution:

$$
\begin{array}{l} C = V N \left(d _ {1}\right) - e ^ {- r T} I N \left(d _ {2}\right) \\ d _ {1} = \frac {\ln (V / I) r T}{\sigma \sqrt {T}} + \frac {1}{2} \sigma \sqrt {T}, \quad d _ {2} = d _ {1} - \sigma \sqrt {T}. \end{array}\tag{2}
$$

Despite their differences, these two models have essentially the same underlying assumptions [4]. In fact, as shown in Appendix A, when n → ∞ in the binomial model, the model converges to the BS model in Equation (2). Therefore, their valuations for simple (nonnested) options are almost identical, as we shall see later.

## Valuation of Interproject Nested Options

A KEY SOURCE OF COMPLEXITY WITH NESTED OPTIONS is their nonadditive value and the unpredictable way in which they interact with one another [12, 31]. Yet, when each option has its own underlying asset, as in the case of interproject nested options, the valuation is somewhat simpler, and adapted versions of the binomial and the BS models can be developed.<sup>3</sup> However, this requires caution. With some effort, the binomial model can be tailored to fit every chain of nested options. Its transparency permits reflecting explicitly the structure of any investment embedding nested options. By contrast, although adapting the BS model is appealing for the numeric simplicity offered by its closed-form solution, its lack of transparency could raise questions about the quality or even validity of its valuations.

## Investment Structure and Valuation Approach

To put the discussion in context, consider a generic valuation problem involving a sequence of three staged projects. The stages can be undertaken at time $T _ { 1 } , T _ { 2 } ,$ , and $T _ { 3 } ,$ and they each have their own underlying asset $V _ { i }$ and cost $I _ { i \cdot }$ Stages II and III can be undertaken only if stage I is undertaken at $T _ { \mathrm { 1 } } = \mathrm { 0 }$ , but they need not necessarily be taken. Stage II is contingent on a favorable outcome of stage I and other contextual realities faced at $T _ { 2 } ,$ and likewise, stage III is contingent on stage II.

For example, consider the case of a data mart consolidation (DMC) investment [7]. DMC involves rehosting or rearchitecting data marts into an enterprise data warehouse. The main benefits include a reduction in IT support personnel, improvement in quantity and quality of data, and follow-up investment opportunities in customer relationship management (CRM) capabilities. However, the benefits from DMC are risky because of uncertainty over the quality of data sources, the level of user involvement in creating a consolidated data model, organizational resistance to centralizing control over data, and so on. In this light, many organizations stage the project in order to permit resolving risk without committing to a full-scale DMC effort. Given n clusters of data marts, each stage consolidates one cluster at a time. Upon investing $I _ { 1 }$ in rehosting and rearchitecting the first data marts cluster, management can decide whether to proceed with the next stage or abandon in midstream, depending on how much risk the completed stage has resolved. The same applies to the remaining stages. Once the DMC effort is completed, there is a follow-up (growth) investment opportunity to deploy CRM applications, contingent on what is learned about uncertainty due to the quality of data sources and user participation. Hence, in this example, each stage is a project that has its own cost, produces its own payoffs, involves its own sources of risk, and creates the option to proceed with the next-stage project.

We see that when a decision is made to undertake investment i in the sequence, real options arise from management’s ability to decide whether it wants to undertake followup investment $i + 1$ , contingent on what is learned upon the completion of investment i. Exercising the option to undertake investment i in the chain unlocks payoffs from the investment and spawns additional options to undertake follow-up investments. The options (investments) are independent in the sense that they each have a separate underlying asset, which is comprised of the direct payoffs produced by each investment plus future options that the investment creates.

Going back to the generic three-stage project, we seek to evaluate project I at $T _ { 1 }$ while accounting for its contingent follow-up opportunities in stages II and III. Based on the logic of the binomial model, this is done by working backward in the lattice in Figure 2, from $T _ { 3 } . \mathrm { A t } T _ { 3 } ,$ , a decision will be made to either invest $I _ { 3 }$ in stage III or not, depending on whether its net value is greater than zero. Relative to stage II, at time $T _ { 2 } ,$ the decision is equivalent to holding a simple call option, $C _ { 3 } ,$ , whose value is computed using the rightmost binomial trees in Figure 2. At $T _ { 2 } ,$ , a decision will be made whether to invest $I _ { 2 }$ in stage II, depending on whether the sum of its net value and option $C _ { 3 }$ exceeds zero. Relative to project I, at time $T _ { \mathrm { 1 : } }$ , the decision is equivalent to holding a call option, $C _ { 2 } . C _ { 2 }$ is a nested option, since investment $I _ { 2 }$ will generate both payoffs $V _ { 2 }$ and option $C _ { 3 } . \mathrm { A t } T _ { 1 } ,$ , a decision will be made whether to invest $I _ { 1 }$ in stage I, depending on whether the sum of its net value and option $C _ { 2 }$ is greater than zero. Here, too, the decision to invest in stage I can be treated as a nested option, $C _ { 1 } .$ . Without loss of generality, we assume that all options are European (e.g., they cannot be exercised before their maturity date).

![](/api/attachments/TVV7WYGK/fulltext/images/ce8b0e2e1d9cfaffa18a7677f06fb07bada105b01c9a393d6c03d692472dc2b6.jpg)

<sub>o</sub>m<sup>ial</sup> <sup>Options</sup> <sup>Valuation</sup> <sup>for</sup> <sup>the</sup> <sup>Three</sup> <sup>Sequential</sup>  
![](/api/attachments/TVV7WYGK/fulltext/images/03bb29b4d3d03fd88e2346fdb55f1c78a16423bb82434cf37f47f61ddaebc8c6.jpg)

## Adaptations of the Binomial and BS Models

How should the value of nested options be calculated using the binomial and the BS models? A common assertion made in connection with nested options is that the underlying asset of a project comprises the project’s direct payoff plus all options it spawns [30]. However, we suspect that a literal interpretation of this assertion is the source of the problem with the nested BS version used by Bardhan et al. [2]. This assertion is qualitatively acceptable but quantitatively inaccurate. To see why, Carr [9] suggests we need to answer another question: should the value of a spawned option be treated as an “added value” to the underlying asset of the option (or investment) that spawned it, or should it be treated as a “subsidy” to the exercise price of the option that spawned it?

Under the “added value” logic, a nested BS model would compute $C _ { 2 }$ as a simple call with the underlying asset being $V _ { 2 } + C _ { 3 } ,$ , denoted $C _ { 2 } = B S ^ { A V } ( V _ { 2 } + C _ { 3 } , I _ { 2 } , \sigma _ { 2 } , T _ { 2 } , r ) =$ $B S ^ { A V } ( V _ { 2 } + B S ^ { A V } ( V _ { 3 } , I _ { 3 } , \sigma _ { 3 } , T _ { 3 } , r ) , I _ { 2 } , \sigma _ { 2 } , T _ { 2 } , r )$ . Likewise, $C _ { 1 }$ would be computed as $C _ { 1 } =$ $B S ^ { A V } ( V _ { 1 } + C _ { 2 } , I _ { 1 } , \sigma _ { 1 } , T _ { 1 } , r )$ . In relation to the one-step binomial model, Equation (1) would therefore have to be rewritten as

$$
C _ {i} = \frac {p _ {i} \max \left(u _ {i} \left(V _ {i} + C _ {i + 1}\right) - I _ {i} , 0\right) + \left(1 - p _ {i}\right) \max \left(d _ {i} \left(V _ {i} + C _ {i + 1}\right) - I _ {i} , 0\right)}{r},\tag{3}
$$

where $C _ { i }$ is the value of the preceding option (to be determined) and $C _ { i + 1 }$ is the value of the nested option.

The problem with this “added value” logic is that both the investment payoffs underlying a particular option and the value of a predecessor option, $V _ { i } + C _ { i + 1 }$ , are being subjected to the same multiplicative diffusion process and hence to the same volatility. In practical terms, it is assumed that stage i + 1 is subject to the same sources of uncertainty, or risk factors, affecting stage i. Hence, this nested version implicitly assumes that option $C _ { i + 1 }$ starts its life earlier—at $T _ { i }$ instead of $T _ { i + 1 } { \mathrm { - a n d } } .$ as a result, it inflates or deflates the value of terminal nodes in the binomial tree for option $C _ { i } .$ For example, given that $u _ { i } > 1$ , the topmost terminal node of the middle binomial option tree in Figure 2 will be inflated into max $( { u _ { 2 } } ^ { 3 } ( { V _ { 2 } } + C _ { 3 } ) - I _ { 2 } , 0 )$ , instead of being max $( { u _ { 2 } } ^ { 3 } V _ { 2 } + { C _ { 3 } } - I _ { 2 } , 0 )$ ; and, given that $d _ { i } < 1$ , the bottommost terminal node in that tree will be deflated into max $( d _ { 2 } ^ { ~ 3 } ( V _ { 2 } + C _ { 3 } ) - I _ { 2 } , 0 )$ , instead of being max $\therefore ( d _ { 2 } ^ { 3 } V _ { 2 } + C _ { 3 } -$ $I _ { 2 } , 0 )$ . Since, usually, some terminal nodes at the bottom of the binomial option tree equal 0, there is reason to believe that an adaptation of the BS model based on the “added value” logic would tend to overvalue investments embedding nested options.

Now, let us see what a nested binomial model would look like. Working backward in the binomial option trees, we plug the value of option $C _ { i + 1 }$ into the terminal nodes in the option tree for option $C _ { i } ,$ , and so on. For example, in Figure 2, the topmost terminal nodes in the binomial option trees for $C _ { 2 }$ and $C _ { 1 }$ become max $( { u _ { 2 } } ^ { 3 } V _ { 2 } + C _ { 3 } - I _ { 2 } ,$

0) and max $( { u _ { 1 } } ^ { 3 } V _ { 1 } + { C _ { 2 } } - I _ { 1 } , 0 )$ , respectively. Thus, the value of a nested option, $C _ { i + 1 } ,$ can be seen as a subsidy to the exercise price of the preceding option, I (rather than an additional stream of value to the underlying asset, V ). Accordingly, the formulation of the one-step binomial model would be

$$
C _ {i} = \frac {p _ {i} \max \left(u _ {i} V _ {i} - \left(I _ {i} - C _ {i + 1}\right) , 0\right) + \left(1 - p _ {i}\right) \max \left(d _ {i} V _ {i} - \left(I _ {i} - C _ {i + 1}\right) , 0\right)}{r}.\tag{4}
$$

The analogy for an adaptation of the BS model based on the “subsidy” logic suggests computing $C _ { 2 }$ as a simple option with the exercise price being $I _ { 2 } - C _ { 3 } ,$ , denoted $C _ { 2 } = B S ^ { s } ( V _ { 2 } , I _ { 2 } - C _ { 3 } , \sigma _ { 2 } , T _ { 2 } , r ) = B S ^ { s } ( V _ { 2 } , I _ { 2 } - B S ^ { s } ( V _ { 3 } , I _ { 3 } , \sigma _ { 3 } , T _ { 3 } , r ) , s _ { 2 } , T _ { 2 } , r ) .$ Likewise, $C _ { 1 }$ would be computed as $C _ { 1 } = B S ^ { S } ( V _ { 1 } , I _ { 1 } - C _ { 2 } , \sigma _ { 1 } , T _ { 1 } , r )$

A simple but crucial difference between the two nested models is evident. In the nested binomial model, relative to a particular time point, $T _ { i } ,$ the multiplicative diffusion process applies only to the project payoff, $V _ { i } ,$ underlying the specific option it embeds, $C _ { i } ,$ not to the value of the immediate predecessor option, $C _ { i + 1 }$ [18]. This is so because option $C _ { i + 1 }$ (investment stage i + 1) is not assumed to be subject to the sources of uncertainty affecting the underlying asset of option $C _ { i }$ (investment stage i). Figure 3 shows the impact of this critical difference on binomial valuations obtained using the two variations for nested options.

If the terms max(⋅,⋅) in Equations (3) and (4) are greater than 0, for example, the overvaluation error made when employing the “added value” logic (instead of the “subsidy” logic) is given as

$$
\text { overvaluation   by } C _ {i} ^ {A V} = \frac {C _ {i + 1} \left(p _ {i} u _ {i} + d _ {i} - p _ {i} d _ {i} - 1\right)}{r}.\tag{5}
$$

As shown in Appendix B, by developing an n-step version of the two binomial models, it is possible to derive an analytic formula for their difference and then make the usual limit argument to derive in a similar fashion a term for the overvaluation error made by the “added value” version.

However, the intuition behind the “added value” logic versus the “subsidy of strike price” logic gives a straightforward argument for a correct adaptation of the BS model for nested options and the error made when employing the “added value” logic.<sup>4</sup> Specifically, referring back to Equation (2), where $N ( d _ { j , i } ) ( j \in \{ 1 , 2 \} )$ ) denotes the cumulative normal distribution term for option $C _ { i } ,$ the nested BS model according to the “added value” logic is

$$
C _ {i} ^ {A V} = \left(V _ {i} + C _ {i + 1} ^ {A V}\right) N \left(d _ {1, i}\right) - e ^ {- r T _ {i}} I _ {i} N \left(d _ {2, i}\right),\tag{6}
$$

whereas the nested BS model according to the “subsidy” logic is

$$
C _ {i} ^ {S} = V _ {i} N \left(d _ {1, i}\right) - e ^ {- r T _ {i}} \left(I _ {i} - C _ {i + 1} ^ {S}\right) N \left(d _ {2, i}\right).\tag{7}
$$

Binomial option trees for the (correct) “subsidy” adaptation  
![](/api/attachments/TVV7WYGK/fulltext/images/f47a6d3209227775753f0f8e800d7197f15aa8c4b465e8a9e2e23fedb882422c.jpg)

Binomial option trees for the (heuristic) “added value” adaptation  
![](/api/attachments/TVV7WYGK/fulltext/images/e415b24b7b64209f02258c30207b6bed143ace19d4643d3aa4b9b45bd6e4578a.jpg)  
Figure 3. Sample Binomial Valuations for the Two Nested Variations Notes: Assumed parameter values: $C _ { 1 } \colon V _ { 1 } = 1 0 0 , I _ { 1 } = 8 0 , \sigma _ { 1 } = 5 0$ percent, $T _ { 1 } = 0 , r = 1 . 0 2 ; C _ { 2 } \colon$ V = 100, $I _ { 2 } = 8 0 , \sigma _ { 2 } = 5 0$ percent, $T _ { 2 } = 1 , r = 1 . 0 2 ;$ C : V = 100, I = 80, σ = 50 percent, $T _ { \scriptscriptstyle 3 } = 2 , r = 1 . 0 2$

Equation (7) extends the BS model to correctly value interproject nested options. Note, however, that a limitation of Equation (7) is that it is not mathematically defined when $I _ { i } < C _ { i + 1 }$ (i.e., in Equation (2), the term ln( $V / I _ { i } - C _ { i + 1 } )$ is not defined when $I _ { i } - C _ { i + 1 } < 0 )$ . This case occurs when the value of stage i + 1 project, $C _ { i + 1 } ,$ , represents a subsidy that is greater than the cost of stage i project, I<sub>i</sub>.

Furthermore, the error derived analytically when applying Equation (6) instead of Equation (7) is

$$
\text { overvaluation   by } C _ {i} ^ {A V} = C _ {i + 1} ^ {A V} \left(N \left(d _ {1, i}\right) - e ^ {- r T _ {i}} N \left(d _ {2, i}\right)\right).\tag{8}
$$

As shown in Appendix B, Equation (8) is identical to the error term derived using the n-step binomial versions of the two adaptations for nested options. It is important to note that, based on Equation (2), because $N ( d _ { 1 } )$ is always larger than $N ( d _ { 2 } )$ and because $e ^ { - r T }$ is always smaller than 1, the “added value” adaptation, Equation (6), will always overvalue investments embedding interproject nested options. Of course, using Equation (8) to calculate the overvaluation error for multiple nested options becomes analytically more challenging. But an examination of Equation (8) directly reveals conditions under which overvaluation will occur:

• The degree of overvaluation increases as $C _ { _ { i + 1 } } , r ,$ or $T _ { _ i }$ becomes larger.

• The degree of overvaluation increases as $V _ { _ { i + 1 } } , \sigma _ { _ { i + 1 } } , \mathrm { o r } T _ { _ { i + 1 } }$ becomes larger, or as $I _ { i + 1 }$ becomes smaller; any of these directional changes causes $C _ { \scriptscriptstyle i + 1 }$ to grow larger.

• The degree of overvaluation increases as $\sigma _ { i }$ becomes larger, because the difference between $N ( d _ { 1 , i } )$ and $\mathrm { N } ( d _ { 2 , i } )$ grows larger, as indicated in Equation (2).

## Numeric Analysis of the Different Nested Versions

THE GOAL OF THIS SECTION IS TO OFFER numeric simulation results that verify and assess the degree of overvaluation error occurring with the heuristic “added value” adaptation of the BS model. Another goal is to show how a small generic investment problem and sensitivity analysis can be used to test a heuristic option valuation model and thus identify conditions under which the “accuracy versus computational simplicity” trade-off may not be acceptable.

We continue our analysis using the nested binomial model, instead of the “subsidy” BS model, because of two reasons. First, since the binomial model is more transparent and can be tailored to the problem situation at hand, it can be used as a gold standard for validating the “subsidy” logic used to derive a correct adaptation of the BS model to nested options. Moreover, it enables one to more easily see the impact of complex interactions between nested options. Second, the “subsidy” adaptation of the BS model we derived cannot be computed when $I _ { 2 } < C _ { 3 }$ . Nevertheless, whenever possible we also report the valuation results for this version of the BS model for completeness.

To quantify the degree of overvaluation of the (heuristic) “added value” adaptation of the BS model, we compute the ratio

$$
\text { percent   overvaluation   by } C ^ {B S (A V)} = \frac {C ^ {B S (A V)} - C ^ {B N}}{C ^ {B N}},\tag{9}
$$

where $C ^ { B S ( A V ) }$ denotes the valuation of the heuristic BS adaptation, and $C ^ { B N }$ denotes the valuation of a custom-tailored nested binomial model. The valuation results for our derived “subsidy” version of the BS model will be denoted as C<sup>BS(S)</sup>.

We use the three-staged sequential investment from Figure 2, and start with the parameter values shown in Table 1. For simplicity, we value stage I as an option $C _ { 1 }$ that matures immediately (i.e., $T _ { 1 } = 0 )$ ; option $C _ { 1 }$ on its own would equal the simple NPV of stage I, $C _ { 1 } = V _ { 1 } - I _ { 1 }$ . The binomial tree we use has 48 binomial steps per year, corresponding approximately to one step each week of the project. Asset trees for individual options are built with the number of binomial steps equaling 48 times the difference between the expiry dates of that option and the immediately preceding option. For the example in Figure 2, if the expiry date of $C _ { 2 }$ and $C _ { 1 }$ are in 12 and 18 months, respectively, the corresponding asset trees will have 48 and 24 steps, respectively.

The valuation results produced using the nested binomial model and the two nested BS models are shown in Table 1. For the innermost option, $C _ { 3 } ,$ , which is a simple call option, $C ^ { B N }$ and $C ^ { B S ( A V ) }$ have similar valuations, \$19.44 and \$19.41, respectively. This represents an overvaluation of –0.2 percent. Clearly, the difference between these valuations is negligible, illustrating that the binomial valuation indeed converges to the BS valuation when the number of discrete binomial steps is sufficiently large. However, for the next two options, $C _ { 2 }$ and $C _ { 1 : }$ , which are both nested options, the results show a notable difference. For option $C _ { 1 }$ (including its nested options), the degree of overvaluation of $C ^ { B S ( A V ) }$ is 4.6 percent. Nevertheless, for a heuristic model, such a small degree of overvaluation could be acceptable.

<sub>hree-Stage</sub> <sub>Sequential</sub> <sub>Investment</sub> <sub>wi</sub>t<sup>h</sup> <sup>Two</sup> <sup>Nes</sup>

<table><tr><td rowspan="2">Scenario</td><td rowspan="2">Project stage</td><td rowspan="2">Option</td><td colspan="4">Option parameters</td><td colspan="3">Option values</td><td rowspan="2">Percent over-valuation of  $C^{BS(AV)}$ (percent)</td></tr><tr><td>Underlying asset (dollars)</td><td>Strike price (dollars)</td><td>Volatility (percent)</td><td>Time to expire (in years)</td><td>Tailored nested binomial,  $C^{BN}$ (dollars)</td><td>Correct nested BS,  $C^{BS(S)}$ (dollars)</td><td>Faulty nested BS,  $C^{BS(AV)}$ (dollars)</td></tr><tr><td rowspan="3">1</td><td>I</td><td> $C_1$ </td><td> $V_1 = 100$ </td><td> $I_1 = 90$ </td><td> $\sigma_1 = 50$ </td><td> $T_1 = 0.0$ </td><td>42.49</td><td>42.49</td><td>44.44</td><td>4.6</td></tr><tr><td>II</td><td> $C_2$ </td><td> $V_2 = 100$ </td><td> $I_2 = 90$ </td><td> $\sigma_2 = 50$ </td><td> $T_2 = 0.5$ </td><td>32.49</td><td>32.49</td><td>34.44</td><td>6.0</td></tr><tr><td>III</td><td> $C_3$ </td><td> $V_3 = 100$ </td><td> $I_3 = 90$ </td><td> $\sigma_3 = 50$ </td><td> $T_3 = 1.0$ </td><td>19.44</td><td>19.41</td><td>19.41</td><td>-0.2</td></tr><tr><td colspan="11">Risk-free rate = 2 percent.</td></tr></table>

Sensitivity analysis with various option parameter values, however, reveals conditions under which the degree of overvaluation by the heuristic nested BS model could be much higher. As seen in Table 2, under certain parameter values, the degree of overvaluation is as high as $^ { 3 2 }$ percent. Generally, the degree of overvaluation is most visible when option $C _ { 2 }$ or option $C _ { 3 }$ are deep in-the-money; that is, when stages II and III projects are very valuable and there is a high chance that they will be undertaken. Overall, the sensitivity analysis results reported in Table 2 confirm the patterns of overvaluation predicted based on an analytical examination of the overvaluation error derived using Equation (8).

Let us examine more closely the impact of changing parameters of options $C _ { 2 }$ and $C _ { 3 }$ on the degree of overvaluation by the nested ${ \mathrm { B S ^ { ( A V ) } } }$ model. (Recall that option $C _ { 1 }$ matures immediately.)

• Underlying assets: When $C _ { 3 }$ is deep in-the-money $( V _ { 3 } > > I _ { 3 } )$ and its value is higher relative to $V _ { 2 } ,$ the distortion effect of the nested ${ \mathrm { B S } } ^ { \mathrm { ( A V ) } }$ model on $C _ { 2 } ^ { \mathrm { ~ \mathfrak ~ { ~ s ~ } ~ } }$ multiplicative process is more visible, and the degree of overvaluation is high. A good example is an incremental development of software releases that is preceded by a large up-front investment in platform design, where upgrading from release i to release $i + 1$ (by adding features) is not very costly but it could generate substantial payoffs by catering to an additional new market segment.

• Exercise prices: When $C _ { 2 }$ is worth little because it is deep out-of-the-money $( V _ { 2 } < < I _ { 2 } )$ , so that the value of $C _ { 3 }$ is high relative to $C _ { 2 } ,$ the distortion effect of the heuristic nested ${ \mathrm { B S } } ^ { \mathrm { ( A V ) } }$ model on the diffusion process of $C _ { 2 }$ is more significant, and the degree of overvaluation is high. For example, this is usually the case with large-scale IT infrastructure investments that are staged, cost much, produce little direct payoffs, but enable the deployment of follow-up investments having a high payoff potential.

• Volatilities: The degree of overvaluation is more pronounced when $\sigma _ { _ { 2 } } ,$ the volatility of $C _ { \mathrm { 2 } } ,$ is higher, because the upward distortion of the underlying asset by the heuristic nested ${ \mathrm { B S } } ^ { \mathrm { ( A V ) } }$ model is more significant. (Recall that the value of an option grows higher as its volatility increases.) Clearly, this is more so when $C _ { 3 }$ is worth more as a result of $\sigma _ { 3 }$ being high. For example, this is the case when the payoffs of stage II are very uncertain, and more so when the payoffs of stage III are also very uncertain.

• Maturity dates: The longer the life span of $C _ { 2 } ,$ the higher the degree of overvaluation, because the distortion effect of the heuristic nested ${ \mathrm { B S } } ^ { \mathrm { ( A V ) } }$ model on the multiplicative process of $C _ { 2 }$ is more accented, especially when $C _ { 3 }$ is worth more as a result of $T _ { \scriptscriptstyle 3 }$ being long as well. For example, this could be the case of largescale and lengthy strategic IT projects $( \mathrm { e . g . }$ ., enterprise resource planning [ERP] implementation) that spawn other large-scale and lengthy investment opportunities $( \mathrm { e . g . }$ , CRM deployment).

• Discount rate: While the degree of overvaluation by the heuristic nested BS<sup>(AV)</sup> model is less sensitive to the discount rate (risk-free interest rate), it does tend to get larger as the discount rate grows larger.

Table 2. Degree of Overvaluation of Project I (Option C<sub>1</sub>) Under Different Option Parameter Values

<table><tr><td colspan="10">a. Underlying asset (in percent)</td></tr><tr><td> $V_2$  $V_3$ </td><td>$40</td><td>$60</td><td>$80</td><td>$100</td><td>$120</td><td>$140</td><td></td><td></td><td></td></tr><tr><td>$40</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td></tr><tr><td>$60</td><td>1</td><td>2</td><td>1</td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td></tr><tr><td>$80</td><td>5</td><td>6</td><td>5</td><td>3</td><td>1</td><td>1</td><td></td><td></td><td></td></tr><tr><td>$100</td><td>17</td><td>17</td><td>10</td><td>5</td><td>2</td><td>1</td><td></td><td></td><td></td></tr><tr><td>$120</td><td>32</td><td>24</td><td>10</td><td>4</td><td>2</td><td>1</td><td></td><td></td><td></td></tr><tr><td>$140</td><td>26</td><td>15</td><td>5</td><td>2</td><td>1</td><td>1</td><td></td><td></td><td></td></tr><tr><td colspan="10">b. Exercise price (in percent)</td></tr><tr><td> $I_2$  $I_3$ </td><td>$50</td><td>$70</td><td>$90</td><td>$110</td><td>$130</td><td>$150</td><td></td><td></td><td></td></tr><tr><td>$50</td><td>0</td><td>1</td><td>2</td><td>8</td><td>18</td><td>29</td><td></td><td></td><td></td></tr><tr><td>$70</td><td>0</td><td>1</td><td>4</td><td>11</td><td>18</td><td>23</td><td></td><td></td><td></td></tr><tr><td>$90</td><td>0</td><td>1</td><td>5</td><td>9</td><td>13</td><td>14</td><td></td><td></td><td></td></tr><tr><td>$110</td><td>0</td><td>1</td><td>4</td><td>6</td><td>7</td><td>7</td><td></td><td></td><td></td></tr><tr><td>$130</td><td>0</td><td>1</td><td>2</td><td>3</td><td>5</td><td>5</td><td></td><td></td><td></td></tr><tr><td>$150</td><td>0</td><td>1</td><td>1</td><td>2</td><td>2</td><td>2</td><td></td><td></td><td></td></tr><tr><td colspan="10">c. Volatility (in percent)</td></tr><tr><td> $σ_2$  $σ_3$ </td><td>10</td><td>30</td><td>50</td><td>70</td><td>90</td><td></td><td></td><td></td><td></td></tr><tr><td>10</td><td>0</td><td>2</td><td>4</td><td>5</td><td>6</td><td></td><td></td><td></td><td></td></tr><tr><td>30</td><td>0</td><td>2</td><td>4</td><td>6</td><td>7</td><td></td><td></td><td></td><td></td></tr><tr><td>50</td><td>0</td><td>2</td><td>5</td><td>7</td><td>9</td><td></td><td></td><td></td><td></td></tr><tr><td>70</td><td>1</td><td>2</td><td>5</td><td>8</td><td>11</td><td></td><td></td><td></td><td></td></tr><tr><td>90</td><td>1</td><td>1</td><td>5</td><td>8</td><td>11</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="10">d. Discount rate (in percent)</td></tr><tr><td> $r_f$ </td><td colspan="9">Difference</td></tr><tr><td>2</td><td colspan="9">5</td></tr><tr><td>4</td><td colspan="9">5</td></tr><tr><td>6</td><td colspan="9">5</td></tr><tr><td>8</td><td colspan="9">5</td></tr><tr><td>10</td><td colspan="9">6</td></tr><tr><td>12</td><td colspan="9">6</td></tr><tr><td colspan="10">e. Maturity date (in percent)</td></tr><tr><td> $T_2$  $T_3$ </td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.9</td></tr><tr><td>1.1</td><td>0</td><td>1</td><td>3</td><td>4</td><td>5</td><td>5</td><td>5</td><td>6</td><td>6</td></tr><tr><td>1.2</td><td>0</td><td>1</td><td>3</td><td>4</td><td>5</td><td>5</td><td>6</td><td>6</td><td>6</td></tr></table>

Table 2. Continued

<table><tr><td colspan="11">e. Maturity date (in percent) Continued</td></tr><tr><td> $T_3^{T_2}$ </td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.9</td><td>1.0</td></tr><tr><td>1.3</td><td>0</td><td>1</td><td>3</td><td>4</td><td>5</td><td>5</td><td>6</td><td>6</td><td>6</td><td>6</td></tr><tr><td>1.4</td><td>0</td><td>1</td><td>2</td><td>4</td><td>4</td><td>5</td><td>6</td><td>7</td><td>7</td><td>7</td></tr><tr><td>1.5</td><td>0</td><td>1</td><td>2</td><td>4</td><td>4</td><td>5</td><td>6</td><td>7</td><td>7</td><td>7</td></tr><tr><td>1.6</td><td>0</td><td>1</td><td>2</td><td>4</td><td>4</td><td>5</td><td>6</td><td>7</td><td>7</td><td>8</td></tr><tr><td>1.7</td><td>0</td><td>1</td><td>2</td><td>4</td><td>4</td><td>5</td><td>6</td><td>7</td><td>7</td><td>8</td></tr><tr><td>1.8</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>7</td><td>8</td></tr><tr><td>1.9</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>7</td><td>8</td></tr></table>

The degree of overvaluation by the heuristic nested BS<sup>(AV)</sup> model is much more pronounced when several option parameters assume “extreme” values. As seen in Table 3, for some parameter values, the degree of overvaluation grows as high as 161 percent. We emphasize, however, that none of the scenarios borne by the parameter values shown in Table 3 can be dismissed for being unrealistic. For example, both scenarios 4 and 5 are typical of IT infrastructure investments—investments that cost much (I is large), are risky (σ is high), produce little direct payoffs (V is small), and spawn valuable but uncertain follow-up investment opportunities in the long run (T is far). A good example is the case of a costly and risky consolidation of data marts into a data warehouse, which is a large IT infrastructure investment that produces little payoffs of its own, but it spawns very valuable and uncertain follow-up investment opportunities in CRM, supply chain, and business intelligence applications [7]. Finally, with regard to scenarios 6 and 7, note that our derived “subsidy” adaptation of the BS model, BS<sup>(S)</sup>, cannot compute the value of options $C _ { 2 }$ and $C _ { 1 }$ because $I _ { 2 } < C _ { 3 }$

To see the overvaluation pattern for deeper chains of nested options, assume that stage I is deferrable for one year (i.e., $T _ { 1 } = 1 . 0 )$ , which makes it a real call option, and extend accordingly the dates for stages II and III by one year. Table 4 shows the results for the adjusted versions of scenario 1 and scenario 5. For scenario 1, the degree of overvaluation for the original two nested options is 4.6 percent (Table 1), but it rises to 13.6 percent for the three nested options (Table 4). By contrast, for scenario 5, the degree of overvaluation for the original two nested options is 161 percent (Table 3), but it drops to 95 percent for three nested options (Table 4). This tells us that the heuristic nested BS<sup>(AV)</sup> model produces unpredictable degrees of overvaluation for a deeper nesting of options, as a result of complex interactions between the options.

We could expand the numeric analysis to other interesting scenarios (e.g., NPV of stage I is negative), but the above simulation results portray a sufficiently clear picture. They confirm that untested heuristic option models could produce inadequate approximate valuations under certain plausible conditions. Such valuations could be so poor that they can mislead even when ROA is used to derive only qualitative insights. Moreover, the results confirm the validity of the nested adaptation of the BS model that we derived based on the “subsidy” logic.

<table><tr><td rowspan="2">Scenario</td><td rowspan="2">Project stage</td><td rowspan="2">Option</td><td colspan="4">Option parameters</td><td colspan="3">Option values</td><td rowspan="2">Percent over-valuation of  $C^{BS(AV)}$ (percent)</td></tr><tr><td>Underlying asset (dollars)</td><td>Strike price (dollars)</td><td>Volatility (percent)</td><td>Time to expire (in years)</td><td>Tailored nested binomial,  $C^{BN}$ (dollars)</td><td>Correct nested BS,  $C^{BS(S)}$ (dollars)</td><td>Faulty nested BS,  $C^{BS(AV)}$ (dollars)</td></tr><tr><td rowspan="3">2</td><td>I</td><td> $C_1$ </td><td> $V_1=100$ </td><td> $I_1=90$ </td><td> $\sigma_1=50$ </td><td> $T_1=0.0$ </td><td>45.21</td><td>45.33</td><td>59.89</td><td>32.7</td></tr><tr><td>II</td><td> $C_2$ </td><td> $V_2=100$ </td><td> $I_2=150$ </td><td> $\sigma_2=100$ </td><td> $T_2=1.0$ </td><td>35.21</td><td>35.33</td><td>49.89</td><td>41.7</td></tr><tr><td>III</td><td> $C_3$ </td><td> $V_3=90$ </td><td> $I_3=60$ </td><td> $\sigma_3=90$ </td><td> $T_3=1.5$ </td><td>37.45</td><td>37.59</td><td>37.59</td><td>0.4</td></tr><tr><td rowspan="3">3</td><td>I</td><td> $C_1$ </td><td> $V_1=100$ </td><td> $I_1=90$ </td><td> $\sigma_1=50$ </td><td> $T_1=0.0$ </td><td>46.48</td><td>46.45</td><td>62.64</td><td>34.8</td></tr><tr><td>II</td><td> $C_2$ </td><td> $V_2=100$ </td><td> $I_2=150$ </td><td> $\sigma_2=100$ </td><td> $T_2=1.0$ </td><td>36.48</td><td>36.45</td><td>52.64</td><td>44.3</td></tr><tr><td>III</td><td> $C_3$ </td><td> $V_3=90$ </td><td> $I_3=60$ </td><td> $\sigma_3=90$ </td><td> $T_3=1.8$ </td><td>41.57</td><td>41.68</td><td>41.68</td><td>0.3</td></tr><tr><td rowspan="3">4</td><td>I</td><td> $C_1$ </td><td> $V_1=100$ </td><td> $I_1=90$ </td><td> $\sigma_1=50$ </td><td> $T_1=0.0$ </td><td>23.82</td><td>23.79</td><td>52.81</td><td>121.7</td></tr><tr><td>II</td><td> $C_2$ </td><td> $V_2=50$ </td><td> $I_2=150$ </td><td> $\sigma_2=100$ </td><td> $T_2=1.0$ </td><td>13.82</td><td>13.79</td><td>42.81</td><td>209.8</td></tr><tr><td>III</td><td> $C_3$ </td><td> $V_3=130$ </td><td> $I_3=60$ </td><td> $\sigma_3=90$ </td><td> $T_3=1.8$ </td><td>76.81</td><td>76.75</td><td>76.75</td><td>-0.1</td></tr><tr><td rowspan="3">5</td><td>I</td><td> $C_1$ </td><td> $V_1=100$ </td><td> $I_1=90$ </td><td> $\sigma_1=50$ </td><td> $T_1=0.0$ </td><td>20.04</td><td>20.06</td><td>52.32</td><td>161.1</td></tr><tr><td>II</td><td> $C_2$ </td><td> $V_2=40$ </td><td> $I_2=150$ </td><td> $\sigma_2=100$ </td><td> $T_2=1.0$ </td><td>10.04</td><td>10.06</td><td>42.32</td><td>321.7</td></tr><tr><td>III</td><td> $C_3$ </td><td> $V_3=140$ </td><td> $I_3=60$ </td><td> $\sigma_3=90$ </td><td> $T_3=1.8$ </td><td>86.02</td><td>85.98</td><td>85.98</td><td>-0.0</td></tr><tr><td rowspan="3">6</td><td>I</td><td> $C_1$ </td><td> $V_1=20$ </td><td> $I_1=100$ </td><td> $\sigma_1=50$ </td><td> $T_1=0.0$ </td><td>151.45</td><td>N/A*</td><td>155.01</td><td>2.3</td></tr><tr><td>II</td><td> $C_2$ </td><td> $V_2=200$ </td><td> $I_2=120$ </td><td> $\sigma_2=50$ </td><td> $T_2=1.0$ </td><td>231.45</td><td>N/A*</td><td>235.01</td><td>1.5</td></tr><tr><td>III</td><td> $C_3$ </td><td> $V_3=300$ </td><td> $I_3=150$ </td><td> $\sigma_3=50$ </td><td> $T_3=1.5$ </td><td>152.08</td><td>152.14</td><td>152.14</td><td>-0.0</td></tr><tr><td rowspan="3">7</td><td>I</td><td> $C_1$ </td><td> $V_1=100$ </td><td> $I_1=90$ </td><td> $\sigma_1=50$ </td><td> $T_1=0.0$ </td><td>57.66</td><td>N/A*</td><td>75.15</td><td>30.3</td></tr><tr><td>II</td><td> $C_2$ </td><td> $V_2=40$ </td><td> $I_2=80$ </td><td> $\sigma_2=100$ </td><td> $T_2=1.0$ </td><td>47.66</td><td>N/A*</td><td>65.15</td><td>36.7</td></tr><tr><td>III</td><td> $C_3$ </td><td> $V_3=140$ </td><td> $I_3=60$ </td><td> $\sigma_3=90$ </td><td> $T_3=1.8$ </td><td>87.81</td><td>87.75</td><td>87.75</td><td>-0.1</td></tr><tr><td colspan="11">Notes: Risk-free rate = 2 percent. * N/A because the “subsidy” adaptation of the BS model is not defined when  $C_{i+1}>I_i$ .</td></tr></table>

<sub>ree</sub> <sub>of</sub> <sub>Overvaluation</sub> <sub>Und</sub><sup>er</sup> <sup>Various</sup> <sup>Option</sup> <sup>Para</sup>

<sub>ree</sub> <sub>of</sub> <sub>Overvaluation</sub> <sub>for</sub> <sub>a</sub> D<sup>eeper</sup> <sup>Chain</sup> <sup>of</sup> <sup>Nes</sup>

<table><tr><td rowspan="2">Scenario</td><td rowspan="2">Project stage</td><td rowspan="2">Option</td><td colspan="4">Option parameters</td><td colspan="3">Option values</td><td rowspan="2">Percent over-valuation of  $C^{BS(AV)}$ (percent)</td></tr><tr><td>Underlying asset (dollars)</td><td>Strike price (dollars)</td><td>Volatility (percent)</td><td>Time to expire (in years)</td><td>Tailored nested binomial,  $C^{BN}$ (dollars)</td><td>Correct nested BS,  $C^{BS(S)}$ (dollars)</td><td>Faulty nested BS,  $C^{BS(AV)}$ (dollars)</td></tr><tr><td rowspan="3">1&#x27;</td><td>I</td><td> $C_1$ </td><td> $V_1 = 100$ </td><td> $I_1 = 90$ </td><td> $\sigma_1 = 50$ </td><td> $T_1 = 1.0$ </td><td>49.65</td><td>49.71</td><td>56.38</td><td>13.6</td></tr><tr><td>II</td><td> $C_2$ </td><td> $V_2 = 100$ </td><td> $I_2 = 90$ </td><td> $\sigma_2 = 50$ </td><td> $T_2 = 1.5$ </td><td>37.16</td><td>37.11</td><td>39.26</td><td>5.7</td></tr><tr><td>III</td><td> $C_3$ </td><td> $V_3 = 100$ </td><td> $I_3 = 90$ </td><td> $\sigma_3 = 50$ </td><td> $T_3 = 2.5$ </td><td>25.07</td><td>25.04</td><td>25.04</td><td>-0.1</td></tr><tr><td rowspan="3">5&#x27;</td><td>I</td><td> $C_1$ </td><td> $V_1 = 100$ </td><td> $I_1 = 90$ </td><td> $\sigma_1 = 50$ </td><td> $T_1 = 1.0$ </td><td>30.18</td><td>30.43</td><td>59.07</td><td>95</td></tr><tr><td>II</td><td> $C_2$ </td><td> $V_2 = 40$ </td><td> $I_2 = 150$ </td><td> $\sigma_2 = 100$ </td><td> $T_2 = 2.0$ </td><td>10.04</td><td>10.06</td><td>42.32</td><td>321.7</td></tr><tr><td>III</td><td> $C_3$ </td><td> $V_3 = 140$ </td><td> $I_3 = 60$ </td><td> $\sigma_3 = 90$ </td><td> $T_3 = 2.8$ </td><td>86.02</td><td>85.98</td><td>85.98</td><td>-0.0</td></tr><tr><td colspan="11">Risk-free rate = 2 percent.</td></tr></table>

## Discussion

THIS RESEARCH INVESTIGATED THE POTENTIAL consequences of applying an untested heuristic option valuation model to IT investments embedding interproject nested options. It specifically illustrates this danger in the case of the heuristic variation of the BS model used by Bardhan et al. [2], and it derives two alternative models that avoid this danger. One is a custom-tailored binomial model, and the other is a more accurate nested version of the BS model.

Heuristic models can be extremely useful, but they must be tested so that their trade-offs become clear. In the case of real options, choosing to use a heuristic valuation model usually involves trading off accuracy for computational simplicity. While higher valuation accuracy usually can be obtained with a custom-tailored binomial model (at the cost of effort), computational simplicity can be appealing when dealing with intricate IT investments. The case of nested options is one good example. An even stronger example can be as follows. Consider a case where project i spawns two (or more) alternative projects—say projects i + 1 and i + 2—and each of these in turn spawns two or more projects, forming a complex web of interdependent projects that can be modeled as chains of nested options. Assuming a limited IT budget, the goal could be to find which subset of the projects should be undertaken in order to maximize value. With a custom-tailored nested binomial model, this problem would be extremely difficult to solve. By contrast, with a nested variation of the BS model, it would be feasible to solve this problem, for example, by using a dynamic programming approach. Hence, the accuracy versus computational simplicity trade-off can be tempting when dealing with really complex IT investment problems.

Yet this research showed the importance of testing heuristic models before they are used. We showed that testing can inform about the trade-offs a particular heuristic model offers, and it could be critical even when the intended use of ROA is only to produce insights. A careful conceptual and numeric examination can inform about the cost that the accuracy versus computational simplicity trade-off presents under different conditions, and, sometimes, it could even remove the need to make the tradeoff. In our case, we specifically showed how examining a transparent custom-tailored binomial model for nested options improved our understanding to the point we were able to derive a more precise nested version of the BS model.

With this said, we must remember that all real option valuation models offer approximate valuations to one degree or another [1]. Even so-called accurate valuation models, such as the BS model, make certain assumptions whose validity is questionable in the context of IT investments [26]. Examples of such assumptions include the tradability and liquidity of real options [35] and the risk-neutrality of the investor [4, 5]. Moreover, it is difficult to obtain accurate estimates of certain option parameters, such as the volatility of investment payoffs constituting the underlying asset of an option [5, 15, 27]. Overall, these looming issues suggest that ROA could produce only approximate valuations, which, in some cases, can even lead to erroneous IT investment decisions. In this light, it is extremely important to be cautious with the use of heuristic models that can compound the effect of these looming issues in unpredictable ways. The bottom line advice we offer is simple—the transparency of an option valuation model usually should be more important than, and it must precede, computational simplicity considerations. In fact, in response to concerns about “the sophisticated math of real options,” as in the case of the BS model, Amram, a leading expert on real option utilization in practice, noted that “to communicate, [ROA] has to be transparent and clear” [28].

Acknowledgments: This research was supported in part by a research grant from the Brethen Institute for Operations Research at the Whitman School of Management, Syracuse University, and a grant from Teradata, a division of NCR, at the Kellogg School of Management, Northwestern University.

## NOTES

1. There could be other reasons for overvaluation with ROA. For example, under situations of information asymmetry, the opaque nature of options makes it easy for a chief information officer (CIO) to “invent” some options in order to get project funding from a non-IT expert chief financial officer (CFO). However, such reasons fall outside the scope of this research.

2. A call option provides its holder with the right (not obligation) to acquire an underlying asset V by paying cost I at a future maturity date T. The value of a call option, C, stems from the uncertain nature of V, as described by the volatility of V, σ.

3. Nested options are different from compound options. A compound option is an option whose underlying asset is another option [20]. Thus, for compound options, there is only one underlying asset, and no actual value (asset) is obtained upon exercising the option.

4. We thank Professor Alfred Taudes of the Vienna University of Economics and Business Administration for an important insight regarding the analytic derivation presented here.

## REFERENCES

1. Amram, M., and Kulatilaka, N. Disciplined decisions: Aligning strategy with the financial markets. Harvard Business Review, 77, 1 (January–February 1999), 95–104.

2. Bardhan, I.; Bagchi, S.; and Sougstad, R. Prioritizing a portfolio of information technology investment projects. Journal of Management Information Systems, 21, 2 (Fall 2004), 33–60.

3. Benaroch, M. Managing investments in information technology based on real options theory. Journal of Management Information Systems, 19, 2 (Fall 2002), 43–84.

4. Benaroch, M.; and Kauffman, R.J. A case for using real options pricing analysis to evaluate information technology project investment. Information Systems Research, 10, 1 (March 1999), 70–86.

5. Benaroch, M., and Kauffman, R.J. Justifying electronic banking network expansion using real options analysis. MIS Quarterly, 24, 2 (June 2000), 197–225.

6. Benaroch, M.; Lichtenstein, Y.; and Robinson, K. Real options use in IT investment risk management: An empirical investigation. Working Paper, Whitman School of Management, Syracuse University, June 2005.

7. Benaroch, M.; Shah, S.; and Jeffery, M. Option-based optimization of the risk-return balance of data warehousing investments. Working Paper, Center for Research on Technology and Innovation, Kellogg School of Management, Northwestern University, February 2005.

8. Bräutigam, J.; Esche, C.; and Mehler-Bicher, A. Uncertainty as a key value driver of real options. Paper presented at the Fifth Conference on Real Options: Theory Meets Practice,

Washington, DC, July 9–10, 2003 (available at www.realoptions.org/papers2003/ BraeutigamUncertainty.pdf).

9. Carr, P. The valuation of sequential exchange opportunities. Journal of Finance, 43, 5 (1988), 1235–1256.

10. Chapin, M.A.; Timur, A.; and Forrer, D.A. The examination on return on investment for information technology in the healthcare industry. Paper presented at the Third International Conference on the Management of Healthcare and Medical Technology, Warwick University, UK, September 7–9, 2003.

11. Clare, R., and Lichtenstein, Y. Real options analysis of an electronic-auction infrastructure for the Irish fishing industry. Paper presented at the Seventh European Conference on Evaluation of Information Technology (ECITE’2000), Dublin, Ireland, September 2000.

12. Copeland, T., and Antikarov, V. Real Options—A Practitioner’s Guide. New York: TEXERE, 2001.

13. Copeland, T., and Tufano, P. A real-world way to manage real options. Harvard Business Review, 82, 3 (March 2004), 90–99.

14. Dai, Q.; Kauffman, R.J.; and March, S.T. Analyzing investments in object-oriented middleware: An options perspective. Working Paper, Carlson School of Management, University of Minnesota, Minneapolis, May 2000 (available at www.misrc.umn.edu/workingpapers/ fullPapers/2000/0010\_050100.pdf).

15. de Jong, B.; Ribbers, P.; and van der Zee, H. Option pricing for IT valuation: A dead end. Electronic Journal of Information Systems Evaluation, 2, 1 (1999) (available at www.ejise.com/ volume-2/volume2-issue1/issue1-art1.htm).

16. Erdogmus, H., and Favaro, J. Keep your options open: Extreme programming and economics of flexibility. In G. Succi, M. Marchesi, L. Williams, and D. Wells (eds.), Extreme Programming Perspectives. Boston: Addison-Wesley, 2002, pp. 503–552.

17. Erdogmus, H., and Vandergraaf, J. Quantitative approaches for assessing the value of COTS-centric development. In Proceedings of the Sixth International Symposium on Software Metrics. Los Alamitos, CA: IEEE Computer Society Press, 1999, pp. 279–291.

18. Herath, H., and Park, C. Multi-stage capital investment opportunities as compound real options. Engineering Economist, 47, 1, 2002, 1–27.

19. Hsia, C. On binomial option pricing. Journal of Financial Research, 6 (1983), 41–46. 20. Hull, J.C. Options, Futures and Derivatives. Englewood Cliffs, NJ: Prentice Hall, 1987.

21. Kenneally, J., and Lichtenstein, Y. The optional value of IS projects: A study of an IS portfolio at a multinational manufacturer. Paper presented at the Tenth European Conference on Information Systems (ECIS’2002), Gdan;sk, Poland, June 6–8, 2002.

22. Lammers, M., and Lucke, C. Sourcing decisions under uncertainty: A real options approach for in- and outsourcing of IT-enabled business processes in the banking industry. Working Paper, University of Frankfurt, Germany, 2004.

23. Luftman, N.J. Managing the Information Technology Resource. Englewood Cliffs, NJ: Pearson Prentice Hall, 2004.

24. Pearlson, K.E., and Saunders, C.S. Managing and Using Information Systems: A Strategic Approach, 2d ed. New York: Wiley and Sons, 2004.

25. Rubinstein, M. Derivatives: A PowerPlus Picture Book, vol. 1. Corte Madera, CA: Inthe-Money Publishing, 1988.

26. Tallon, P.P.; Kauffman, R.J.; Lucas, H.C.; Whinston, A.B.; and Zhu, K. Using real options analysis for evaluating uncertain investments in information technology: Insights from the ICIS 2001 debate. Communications of the AIS, 9 (2002), 136–167.

27. Taudes, A.; Feurstein, M.; and Mild, A. Options analysis of software platform decisions: A case study. MIS Quarterly, 24, 2 (June 2000), 227–243.

28. Teach, E. Will real options take root? CFO Magazine (July–August 2003) (available at www.cfo.com/article.cfm/3009782).

29. Tegstam, M., and Weiner, J. Evaluating costs and benefits when implementing an information system—A PDM system at Autoliv Inc. Master’s thesis, Graduate Business School, School of Economics and Commercial Law, Goteborg University, Sweden, 2000 (available at www.handels.gu.se/epc/archive/00001593/).

30. Trigeorgis, L. Real Options. Cambridge, MA: MIT Press, 1996.

31. Trigeorgis, L. Real Options: Managerial Flexibility and Strategy in Resource Allocation. Cambridge, MA: MIT Press, 1997.

32. Turban, E.; McLean, E.; and Wetherbe, J. Information Technology for Management: Transforming Business in the Digital Economy, 4th ed. New York: Wiley & Sons, 2004.

33. van Putten, A.B., and McMillan, I.C. Making real options really work. Harvard Business Review, 82, 12 (December 2004), 134–141.

34. Ward, J., and Peppard, J. Strategic Planning for Information Systems. New York: Wiley, 2002.

35. Zhu, K. Evaluating information technology investment: Cash flows or growth options? Paper presented at the 1999 Workshop on Information Systems Economics (WISE’99), Charlotte, NC, September 1999.

## Appendix A. The n-Step Binomial Model

AS WE SAW IN EQUATION (1), the one-step binomial model for a call option that matures in time T is

$$
C = \frac {p C _ {u} + (1 - p) C _ {d}}{r},
$$

where $C _ { u } = \operatorname* { m a x } ( 0 , u V - I ) , C _ { d } = \operatorname* { m a x } ( 0 , d V - I )$ , and the parameters $V , I , p , u , d ,$ and r are as defined before. The n-step version of the binomial model can be written as [19, 25]

$$
\dot {C} = \sum_ {j = 0} ^ {n} p ^ {j} (1 - p) ^ {n - j} \binom {n} {j} \max \left[ u ^ {j} d ^ {n - j} V - I, 0 \right] / r ^ {n},\tag{A1}
$$

where

$$
\binom {n} {j} = \left(\frac {n !}{j ! (n - j) !}\right),
$$

$p$ is the probability that the underlying asset $V$ will make an upward move in one time period $( \Delta t = T / n )$ , and $r ^ { n }$ is the discount factor. If a is the minimum number of upward moves that V has to make over n periods for C to take on a positive value, then for all $j < a , \operatorname* { m a x } [ u ^ { j } d ^ { n - j } V - I , 0 ] = 0$ , and for all $j \geq a , \operatorname* { m a x } [ u ^ { j } d ^ { n - j } V - I , 0 ] = u ^ { j } d ^ { n - j } V - I .$ Therefore, we can write Equation (A1) as

$$
C = V \left[ \sum_ {j = a} ^ {n} p ^ {j} (1 - p) ^ {n - j} \binom {n} {j} \frac {\left(u ^ {j} d ^ {n - j}\right)}{r ^ {n}} \right] - I r ^ {- n} \left[ \sum_ {j = a} ^ {n} p ^ {j} (1 - p) ^ {n - j} \binom {n} {j} \right].\tag{A2}
$$

This expression can be rewritten as

$$
C = V B (a; n, p ^ {\prime}) - I r ^ {- n} B (a; n, p),\tag{A3}
$$

where $B ( \cdot )$ is the complementary binomial distribution, or the probability of the number of upward moves in V out of n moves is equal or greater than a, with up move probabilities $p = ( r - d ) / ( u - d )$ and $p ^ { \prime } = p ( u d / r )$ . It has been shown that when $n \to \infty$ , then $B ( a ; n , p ^ { \prime } )  N ( d _ { 1 } ) , B ( a ; n , p )  N ( d _ { 2 } ) ,$ , and $r ^ { n } = e ^ { - r T } .$ , where $N ( d _ { 1 } )$ and $N ( d _ { 2 } )$ are the cumulative normal distribution terms used in the BS model. Hence, when $n \to \infty$ , the n-step binomial model becomes exactly the BS model in Equation (2):

$$
\begin{array}{l} C = V N \left(d _ {1}\right) - e ^ {- r T} I N \left(d _ {2}\right) \\ d _ {1} = \frac {\ln (V / I) r T}{\sigma \sqrt {T}} + \frac {1}{2} \sigma \sqrt {T}, \quad d _ {2} = d _ {1} - \sigma \sqrt {T}. \end{array}\tag{A4}
$$

## Appendix B. Using the n-Step Binomial Model to Derive the Error Term for the “Added Value” Adaptation

BASED ON APPENDIX A, WE DEVELOP the n-step versions of the binomial model for the “added value” logic and the “subsidy of exercise price” logic, and then we make the usual limit argument to show that these versions are equal to the nested adaptations developed directly based on the BS model for both logics. Subsequently, we show that the overvaluation error term of the “added value” version for the case of a one-step binomial model equals the term obtained in Equation (5), and that for the n-step binomial model, the error term equals the error term derived using the BS adaptations in Equation (8).

For the “added value” logic, Equation (A1) can be written as

$$
C _ {i} ^ {A V} = \sum_ {j = 0} ^ {n} p _ {i} ^ {j} \left(1 - p _ {i}\right) ^ {n - j} \binom {n} {j} \max \Big [ u _ {i} ^ {j} d _ {i} ^ {n - j} \left(V _ {i} + C _ {i + 1}\right) - I _ {i}, 0 \Big ] \Bigg / r ^ {n},\tag{B1}
$$

and for the “subsidy” logic as

$$
C _ {i} ^ {S} = \sum_ {j = 0} ^ {n} p _ {i} ^ {j} \left(1 - p _ {i}\right) ^ {n - j} \binom {n} {j} \max \Big [ u _ {i} ^ {j} d _ {i} ^ {n - j} V _ {i} - \big (I _ {i} - C _ {i + 1} \big), 0 \Big ] \Bigg / r ^ {n}.\tag{B2}
$$

By analogy of how Equation (A1) maps to Equation (A4) when $n \to \infty$ , Equations (B1) and (B2) can be written as

$$
C _ {i} ^ {A V} = \left(V _ {i} + C _ {i + 1}\right) N \left(d _ {1, i}\right) + I _ {i} e ^ {- r T _ {i}} N \left(d _ {2, i}\right)\tag{B1'}
$$

$$
C _ {i} ^ {S} = V _ {i} N (d _ {1, i}) + (I _ {i} - C _ {i + 1}) e ^ {- r T _ {i}} N (d _ {2, i}).\tag{B2'}
$$

The difference between Equation (B1′) and Equation (B2′) is the overvaluation error made by the “added value” version:

$$
\begin{array}{c} \text {overvaluation of} C _ {i} ^ {A V} = C _ {i} ^ {A V} - C _ {i} ^ {S} \\ = \sum_ {j = 0} ^ {n} p _ {i} ^ {j} (1 - p _ {i}) ^ {n - j} \binom {n} {j} \max \left[ u _ {i} ^ {j} d _ {i} ^ {n - j} C _ {i + 1} - C _ {i + 1}, 0 \right] / r ^ {n}. \end{array}\tag{B3}
$$

When $n = 1$ and the discounting term (r<sup>n</sup>) is removed for simplicity from all expressions, the right-hand side of Equation (B3) equals (recall that $0 ! = 1 )$

$$
\begin{array}{c} \text {overvaluation of} C _ {i} ^ {A V} = (1 - p _ {i}) \binom {1} {0} \max \big [ d _ {i} C _ {i + 1} - C _ {i + 1}, 0 \big ] \\ + p _ {i} \binom {1} {1} \max \big [ u _ {i} C _ {i + 1} - C _ {i + 1}, 0 \big ] \\ = \max \big [ d _ {i} C _ {i + 1} - C _ {i + 1} - p _ {i} d _ {i} C _ {i + 1} + p _ {i} C _ {i + 1}, 0 \big ] + \max \big [ p _ {i} u _ {i} C _ {i + 1} - p _ {i} C _ {i + 1}, 0 \big ] \\ = \max \big [ d _ {i} C _ {i + 1} - C _ {i + 1} - p _ {i} d _ {i} C _ {i + 1} + p _ {i} C _ {i + 1} + p _ {i} u _ {i} C _ {i + 1} - p _ {i} C _ {i + 1}, 0 \big ] \\ = \max \big [ C _ {i + 1} (p _ {i} u _ {i} + d _ {i} - p _ {i} d _ {i} - 1), 0 \big ]. \end{array}\tag{B3'}
$$

If the terms max[⋅,⋅] in Equations (B1) and (B2) are assumed to be greater than 0 (just like we assumed for Equation (5)), and bringing back the discounting term into Equation (B3′), we get the same error term derived in Equation (5) based on a onestep binomial process:

$$
\text { overvaluation   of } C _ {i} ^ {A V} = \frac {C _ {i + 1} \left(p _ {i} u _ {i} + d _ {i} - p _ {i} d _ {i} - 1\right)}{r}.\tag{B3''}
$$

Moreover, by analogy of how Equation (A1) maps to Equation (A4) when $n \to \infty$ Equation (B3) can be rewritten as

$$
\begin{array}{l} \text {overvaluation of} C _ {i} ^ {A V} = C _ {i} ^ {A V} - C _ {i} ^ {S} \\ \quad = C _ {i + 1} N (d _ {1, i}) + C _ {i + 1} e ^ {- r T} N (d _ {2, i}) \\ \quad = C _ {i + 1} (N (d _ {1, i}) + e ^ {- r T} N (d _ {2, i})). \end{array}\tag{B3''}
$$

Equation $( \mathbf { B } 3 ^ { \prime \prime \prime } )$ equals the error term in Equation (8), which was derived directly based on the “added value” and the “subsidy” adaptations of the BS model to nested options.
