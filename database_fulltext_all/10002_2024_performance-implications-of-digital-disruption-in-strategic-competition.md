---
otero_id: 10002
otero_key: "5M5Q2XAN"
title: "Performance Implications of Digital Disruption in Strategic Competition"
authors: "Fabian J. Sting; Murat Tarakci; Jan Recker"
year: "2024"
journal: "MIS Quarterly"
doi: "10.25300/misq/2024/17999"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# PERFORMANCE IMPLICATIONS OF DIGITAL DISRUPTION IN STRATEGIC COMPETITION<sup>1</sup>

Fabian J. Sting

Faculty of Management, Economics, and Social Sciences, University of Cologne, Cologne, GERMANY, and Rotterdam School of Management, Erasmus University, Rotterdam, THE NETHERLANDS {sting@wiso.uni-koeln.de}

Murat Tarakci Rotterdam School of Management, Erasmus University, Rotterdam, THE NETHERLANDS {tarakci@rsm.nl}

Jan Recker Faculty of Business Administration, University of Hamburg, Hamburg, GERMANY {jan.christof.recker@uni-hamburg.de}

Pervasive digitalization is changing how firms engage in strategic competition. Some firms are pursuing digital disruption strategies, using digital resources to rewire their value chain and change the landscape of their industry by redefining performance expectations. Other firms are adapting to digitalization by adding digital resources into their existing value chain. Through NK model simulations, we advance our understanding of digital disruption vis-à-vis adaptation in strategic competition in two main ways. First, we unearth important nuances in performance trade-offs: A digital disruption strategy may be effective for relative performance at the expense of absolute performance gains. Second, we explore relevant marketand competitor-related conditions under which firms should opt (or not) for a digital disruption strategy.

Keywords: Digital Business Strategy, Digital Disruption, Theory-Building, Simulation, NK Model

## Introduction

Digital disruption—the upheaval of established or dominant industry paradigms via novel applications of digital technology (Baiyere et al., 2023; Christensen et al., 2015; Garcia & Calantone, 2002)—has become “new business gospel” (Lepore, 2014) because it opposes traditional adaptation strategies that aim to improve fit to given paradigms. To illustrate, Netflix is a well-known example of a firm that successfully upended a once physical, localized industry that required firms to master physical assets such as rental stores and video cassettes. Instead, Netflix committed to an alternative strategy developed around a new value chain that centered on digital resources, such as online streaming services, algorithmic-curated user playlists, and digital content production, which turned out to be disruptive (Baiyere et al., 2023; Randolph, 2019).

Netflix and other recognized cases of digital disruption, such as those in the music (Riemer & Johnston, 2019) and book industries (Utesheva et al., 2016), have been well documented and are intuitively appealing. Yet we also see many cases where digital strategic initiatives fail to disrupt (Adner, 2021; Furr & Shipilov, 2019). In addition, earlier research has adopted a focus on one focal firm—either the disruptor or disruptee—to highlight the importance of architectural discontinuity (Lyytinen & Rose, 2003) and the agency of firms leveraging digital technology (Riemer & Johnston, 2019). But upending established trajectories of performance improvement (Christensen & Bower, 1996, p. 202) should also affect competitive dynamics. Hence, we still need to better understand the performance implications of digital disruption in strategic competition (Adner, 2002; Baiyere et al., 2023; Christensen et al., 2015).

Building theory on how digital disruption strategies play out between competing firms requires unpacking at least three aspects of digital business strategy (e.g., Bharadwaj et al., 2013; Mithas et al., 2013; Park & Mithas, 2020): First, what trade-offs do firms face when allocating resources to digital disruption as opposed to adaptation? Second, how does a digital disruption strategy affect both the internal workings of the firm and its environment? Third, how will rivals respond to the launch of a digital disruption strategy compared to an adaptation strategy?

In this paper, we use agent-based simulation models to advance our theoretical understanding of digital disruption in a way that is sensitive to the shifts brought forward by digitalization (Baiyere et al., 2023; Lyytinen, 2022; Piccoli et al., 2022). Simulations offer a controlled yet versatile setting for unpacking the trade-offs as well as the internal and competitive dynamics when exploring how firms commit digital resources strategically to shape or indeed “disrupt” their business landscapes.

The theory we develop through simulation yields two nuanced insights into the co-evolutionary dynamics of digital disruption strategies in different market contexts. First, we suggest that digital disruption is not a strategic panacea across all industries. Markets can be more or less open to digital disruption depending on institutional regimes, regulations, digital readiness, and a variety of other industry forces (e.g., Hargadon & Douglas, 2001; Hinings et al., 2018; Karimi & Walter, 2015). We complement the demand-side views of Adner (2002) and Christensen and Bower (1996) by exploring the role that market openness plays in digital disruption.

Second, and arguably less intuitive, are our insights about the performance implications of digital disruption and adaptation in competition. We unearth how a firm’s performance objectives and its rival’s strategies mesh as simultaneous determinants of digital disruption. We find that allocating fewer resources to a digital disruption and more resources to an adaptation strategy can improve a firm’s absolute performance (e.g., in terms of growth in revenue or profit, Luo et al., 2007) when it faces a rival that embraces digital disruption. At the same time, our insights also imply that a digital disruption strategy fosters relative performance gains (i.e., as improvements in key metrics relative to the standing of a competitor, Luo et al., 2007), irrespective of a rival’s strategies.

These findings provide important theoretical and managerial contributions. First, we advance research on digital disruption by unearthing its performance implications (Baiyere et al., 2023; Lyytinen, 2022; Nell et al., 2021). Our key finding is that in several scenarios, digital disruption strategies boost relative performance at the expense of absolute performance. This nuanced perspective is important for firms seeking returns on investment from their digital strategic initiatives because it may prompt a reevaluation of success metrics and steer leaders away from the narrow pursuit of absolute performance gains. Second, we widen the scope of digital disruption research by integrating both competitive dynamics (e.g., Lyytinen & Rose, 2003; Riemer & Johnston, 2019) and demand-side boundary conditions (e.g., Adner, 2002; Christensen & Bower, 1996). Our analyses illustrate the importance of integrating both disruption and adaptation strategies to navigate competitive landscapes effectively. Third, endogenizing landscape changes could also be useful for understanding other phenomena, such as ontological reversal processes in digital-first human experiences (Baskerville et al., 2020).

## Conceptual Development

Digital disruption describes a process where a firm exercises agency to architecturally rewire its value chain and thereby the industry’s dominant value chain through novel applications of digital technology (Baiyere et al., 2023; Lyytinen & Rose, 2003; Riemer & Johnston, 2019).<sup>2</sup> This definition highlights two unique characteristics of digital disruptions. First, digital disruptions originate from digital strategic initiatives (Piccoli et al., 2022) that constitute a strategic action or response: In digital disruption, firms deliberately commit to the creation, deployment, and use of novel digital resources<sup>3</sup> to create and capture value. Second, since digital resources are encapsulated and accessible objects that can be separated, reused, and recombined (Schilling, 2000), firms can use them flexibly to architecturally rewire the interdependencies within their own—and thus, ultimately, the industry’s dominant— value chain (Amit & Han, 2017). When successful, this strategy culminates in landscape change. The conceptual basis for this possibility lies in digital resources’ ability to be homogenized, reprogrammable, and, in the end, generative (Baiyere et al., 2023; Piccoli et al., 2022; Tilson et al., 2010). All digital resources (e.g., offerings, content, processes, infrastructure, or other strategic assets) effectively become malleable (Henfridsson & Bygstad, 2013; Kallinikos et al., 2013; Zittrain, 2006), which means that they expand a focal firm’s options and ease for (re)combining strategic building blocks in new, versatile, generative, or even destructive, ways (Baiyere et al., 2023; Giustiziero et al., 2023; Lyytinen, 2022).

With digital disruption strategy, we thus refer to a firm’s commitment to strategic initiatives that primarily depend on, create, and exploit digital resources (as opposed to other firm resources) for rewiring its value chain. Engagement in digital strategic initiatives that manifest as the allocation of commitment to the creation, deployment, and use of digital resources can in turn be disruptive when such an initiative endogenously changes the landscape of the industry in which the firm operates. Digital disruption strategies are not merely new value chains launched by one firm; they create and shape new competitive realities for all firms when they succeed in recasting performance expectations, destroying current competencies, and dissolving old rules of engagement in that industry (Christensen & Bower, 1996; Garcia & Calantone, 2002; Lyytinen & Rose, 2003). Digital disruption is thus an ongoing process (Christensen et al., 2015) that can unfold in recurring ways rather than as a oneoff discrete change. In other words, digital disruption can be repeatedly triggered—by a firm and/or its rivals. This is crucial in strategic competition, as business landscapes and competitive logic are continuously evolving. Firms are always both subjects and agents in this coevolution, as they respond to and shape the prevailing competitive realities through strategic interactions.

We are, of course, not the first to point out the impact of digital disruption on business landscapes. Digitalization has long been conceived as shaping the “landscape” for businesses: it has changed the nature and structure of economic goods, unleashed fierce price competition, opened new markets for existing products and services, reduced entry barriers for emergent firms, and enabled the creation of complex ecosystems (Adner et al., 2019; Autio et al., 2021; Lyytinen, 2022). Similarly, digitalization has also been argued to “ontologically reverse” (Baskerville et al., 2020) the landscape of the human experience, by shifting many aspects of the human experience into the digital realm where they then create and shape the physical human experience. Conceptually congruent, neither landscape shaping nor ontological reversal epitomizes technological change as an exogenous force (Yoo, 2013). Digital disruption is instead the result of agency exercised by a focal firm in light of new technology affordances (Baiyere et al., 2023; Riemer & Johnston, 2019). That said, digital disruption research has yet to examine this agency, and particularly its competitive performance implications.

In this understanding, a digital disruption strategy differs from alternative strategic logics that commit to an existing landscape, that is, a strategy where a firm adapts but does not rewire its value chain while adhering to given interdependencies among products, manufacturing, logistics, distribution, or other capabilities and assets. We label this contrasting choice as adaptation (Cyert & March, 1963; Levinthal & March, 1981; March, 1991)—a search strategy through which a firm improves its fit to an exogenously given or changing landscape (Levinthal, 1997). An adaptation strategy offers gradual position improvement (a local search in the neighborhood surrounding an existing solution) or a total shift (a distant search that requires the firm to pursue a long-jump to new regions of a given landscape, Levinthal, 1997; Posen & Levinthal, 2012). Adaptation has been proven and tested as an effective strategy for firms undertaking strategic initiatives under uncertainty, ambiguity, and complexity (Pich et al., 2002), including the digital transformation of value chains. The key point is that adaptation strategies may involve the exploitation of digital resources (such as the development of online service offerings or digital customer channels) but not the rewiring of a firm’s value chain. In other words, an adapting firm may choose to modify its value chain using digital resources (e.g., online marketing, digital services, or electronic channels), but it does so to improve its fit to an existing landscape rather than to change it.

Finally, we note that digital disruption is a process fraught with uncertainty: a firm’s digital strategy initiative may fail to disrupt the landscape, for example, when new value propositions elude customer esteem (Christensen et al., 2015; Furr & Shipilov, 2019), or when digital strategic launches are impeded by regulatory mandates or other institutional forces in that industry (e.g., Hargadon & Douglas, 2001). We cast these situations as a market’s openness to digital disruption.

## Grounding the Simulation Model in Real-Life Competition

Digital-age strategic competition is complex (Park & Mithas, 2020) and simulations always involve a trade-off between veridicality and abstraction (Miller, 2015). We thus use an empirical case to ground our model-building. The case we use is deliberately not a representative case of digital disruption but instead highlights strategic heterogeneity between two firms in allocating digital resources across disruption versus adaptation initiatives and the ensuing competitive dynamics that evolved: Our case describes two competing firms that embark on divergent strategies, one emphasizing fitting the landscape (i.e., adaptation) and the other one shaping the landscape (i.e., disruption).

Our example is set in the consumer goods retail sector, a market whose landscape has been substantially altered by the advent of Amazon since its origin as an online bookseller (Alihmahomed-Wilson & Reese, 2020). From the outset, Amazon committed mainly to digital resources for its strategic initiatives—for example, its “store” has existed for the most part only as an online platform, not in physical reality. Over time, Amazon expanded its range of offerings managed through digital resources from the purchase of books and similar consumer goods to cover groceries, as well as the provision of audio, video, and gaming media.

To illustrate the salience of Amazon’s digital disruption strategy, consider how it committed to this strategy by allocating resources to digital strategic initiatives such as the launch of Amazon Prime, where Amazon invested heavily in digital objects such as web services, data storage, and algorithmic capabilities.<sup>4</sup>

Amazon’s digital strategic initiative imposed substantial implications on competitors, often pinpointed in Jeff Bezos’s famous quip: “your margin is my opportunity” (Lahshinsky, 2012). Consider Australia’s leading retailer Woolworths Limited (hereafter “Woolworths”), which operates in a geographical market that Amazon did not enter until 2017. Still, Amazon’s rise as an online retailer of consumer goods ignited an ongoing process of landscape changes that affected the retail sector globally—including in Australia. This development—long before Amazon arrived in Australia—prompted Woolworths to reshape its fit to the changing landscape.

Woolworths’s strategy resembles what we call an adaptation strategy: the firm sought improvements to its position in the existing landscape, respecting its value chain and standing interdependencies. Woolworths engaged in what can be construed as local search (Levinthal, 1997):<sup>5</sup> It began local modifications to its value chain (e.g., changes in store product selections) to fit the changed landscape that Amazon’s digital strategic initiative unleashed. Woolworths also undertook initiatives that can be construed as distant search: For example, when online shopping could no longer be ignored in its home market, they debuted a mobile shopping application for home delivery yet grafted the online shopping fulfillment tasks onto existing operations in their physical retail stores.

Doing so constrained Woolworths’s search for further improvements: The new digital resource elements it grafted into its value chain hampered its traditional store operations, disrupted traditional purchasing protocols, and altered replenishment patterns.

What this demonstrates is that while Woolworths did adapt to a changing consumer goods landscape, it never embraced a digital disruption strategy per se: It maintained its bricksand-mortar value chain as the primary driver of value creation, gradually adding chosen digital elements such as mobile shopping solutions and home delivery services. This adaptation strategy yielded over 2.3 million customers downloading the new app in 2012, boosting online sales by 95% (Woolworths Limited, 2012), and Woolworths quickly generated Australia’s highest revenue in online retail, a rank they hold to this day (eCommerceDB, 2023).

The competitive dynamics between Amazon and Woolworths illustrate how digital-age business strategy is interdependent: One firm’s digital disruption strategy ripples into other firms’ digital strategic initiatives by affecting their landscape through an ongoing process that can progress gradually slow or suddenly surge. Amazon’s digital disruption strategy manifested as a total redesign of a traditional retail value chain enabled through digital strategic initiatives that reified retailing value-chain factors (e.g., product selection, regional distribution, marketing, and purchasing) as digital objects. These implemented changes created new customer value and altered expectations, thereby affecting other market players that followed a traditional brick-and-mortar retailing strategy. Even on its distant island continent, Woolworths experienced landscape turbulence spawned by Amazon’s strategy. Woolworths adapted to the changed landscape by adding selected digital elements (e.g., online shopping solutions and fulfillment processes) to its existing value chain rather than rewiring it completely.

This case illustrates how implementing digital disruption logic in strategic competition requires companies to understand: (1) the trade-offs in resource allocation choices that emanate from digital disruption versus adaptation strategies and (2) the implications this choice imposes on competitive interactions in a changing business landscape.

## Using Simulation to Theorize About Digital Disruption in Strategic Competition

The theory-building power of simulation has a long tradition in IS and management research since empirical models can fall short when underlying theoretical relationships are complex, dynamic, and nonlinear (e.g., Beese et al., 2019; Davis et al., 2007; Pentland et al., 2022). NK models, in particular, provide a versatile method to study complex, dynamic, and nonlinear organizational processes, such as those involved in strategic decision-making (e.g., Ganco & Hoetker, 2009; Kauffman, 1993; Levinthal, 1997; Siggelkow & Rivkin, 2005).<sup>6</sup>

Prior simulation work probing firms’ strategic choices has largely assumed an introspective viewpoint, focusing on interdependencies within a single firm’s digital strategy (e.g., Levinthal & Warglien, 1999; Nan & Tanriverdi, 2017) and its performance on stable landscapes (e.g., Brunswicker et al., 2019; Uotila et al., 2017) or those facing exogenous turbulence (e.g., Chandrasekaran et al., 2016; Gavetti et al., 2005; Posen & Levinthal, 2012). However, both competitive interaction and the endogenous reshaping of business landscapes are core elements of modern digital business strategy (Bharadwaj et al., 2013; Mithas et al., 2013) and key to understanding the digital disruption process (Christensen et al., 2015; Riemer & Johnston, 2019). To integrate these features, we thus extend current simulation models by using the notion of endogenously changed, “disrupted” landscapes. In our model, landscapes can be reshaped through firms’ actions, specifically by their launch of digital strategic initiatives that commit to the architectural rewiring of existing interdependencies through digital resources. Table 1 summarizes the main components of our simulation model, provides illustrations from our retailing case, and sketches their implications for firms’ strategizing.

## Modeling the Business Landscape

At the core of our simulation, we build on Kauffman’s (1993) standard NK model to represent how strategic decisions direct firms’ actions on business landscapes. The business landscape (in our illustrating case, the competitive arena of consumer goods retailing; see the first row of Table 1) reflects the current business reality describing the overall strategic position of a firm, as well as those of its rivals. Position, here, encompasses all decisions a firm can strategize to improve its fit.

Formally, each firm decides on N strategic product elements<sup>7</sup> in the vector $\mathbf { d } = ( d _ { 1 } , \hdots , d _ { m } , \hdots d _ { N } )$ . Each decision $d _ { m }$ is either 0 or 1, thus comprising $2 ^ { N }$ possible configurations per given landscape, and the height attained in the interdependent landscape represents a firm’s current performance. The degree of interdependency among strategic elements here defines a given business landscape’s level of complexity or ruggedness. Strategic decisions wield relative independence in smooth landscapes of low complexity but interact more strongly in rugged terrains of high complexity. In the model, $\pi _ { m }$ thus denotes the performance contribution of a specific decision $d _ { m } .$ . Business landscapes are more or less complex as $\pi _ { m }$ depends not only on the value of $d _ { m } ,$ but also on the decision set of K other elements denoted as $\mathbf { d } _ { - m } = ( d _ { m 1 } , \dots , d _ { m K } )$ . For every possible combination of $( d _ { m 1 } , \ \dots \ , \ d _ { m K } )$ , a random draw from a standardized uniform distribution is assigned to the performance contribution $\pi _ { m } \left( d _ { m } , \mathbf { d } _ { - m } \right)$ for element m. As K increases, elements increasingly intertwine with other elements of the strategy, and the landscape appears more rugged. The overall performance is the average of all decision contributions: $\Pi ( { \bf d } ) = \sum _ { m = 1 } ^ { N } \frac { \pi _ { m } ( d _ { m } , { \bf d } _ { - m } ) } { N }$

Firms explore the business landscape by altering one or more individual existing elements (representing the default of a pure adaptation strategy—see next section). We focus on two firms $( i , j = 1 , 2 ; ~ i \neq j )$ to examine their fine-grained competitive interaction. Such a two-firm contest is consistent with a large body of research in competitive dynamics that likewise considers the strategic actions and reactions of dyads (e.g., Chen & Miller, 2012).

## Modeling Digital Disruption and Adaptation Strategies

We model a digital disruption strategy as the process of envisioning and searching a new business landscape (second row of Table 1). We represent the landscape emerging from Firm i’s digital disruption strategy using a newly constructed performance function $\Pi _ { i } ^ { ' }$

<table><tr><td colspan="4">Table 1. Linking Illustrating Example, Firm Implications, and Simulation Model</td></tr><tr><td>Key element</td><td>Illustrating example</td><td>Implication for firms&#x27; strategizing</td><td>Representation in the simulation</td></tr><tr><td>Business landscape</td><td>The competitive arena of consumer goods retailing; contested by Woolworths and Amazon.</td><td>Interdependencies across decisions, periods, and competitors shape firms&#x27; search and performance</td><td>Co-evolutionary competition on a rugged NK landscape.</td></tr><tr><td>Digital disruption strategy</td><td>Amazon&#x27;s rewiring of its value chain configuration unrestricted by the physical status quo configuration of competitors.</td><td>Rewiring the value chain through digital resources changes the interdependencies that determine how firms create and capture value.</td><td>Firms envision a newly constructed NK landscape that is unrestricted by the existing landscape.</td></tr><tr><td>Adaptation strategy</td><td>Woolworths&#x27;s incorporating e-commerce capabilities into its existing value chain to improve its fit to the changed landscape.</td><td>Incorporating adjustments to an existing value chain to improve its fit to the given interdependencies.</td><td>Firms pursue local hill climbing (and long jumps) to improve their fitness in the given NK landscape.</td></tr><tr><td>Resource allocation</td><td>Amazon&#x27;s resource commitment to online delivery fulfillment and delivery or Woolworths&#x27;s commitment to e-commerce retailing.</td><td>Digital disruption and adaptation become implemented through firms&#x27; strategic commitments (to digital resources or otherwise).</td><td>Firms decide on resource allocation to digital strategic initiatives and commit the remaining resources to adaptation.</td></tr><tr><td>(Industry-level) openness to digital disruption</td><td>The Australian retail market endorsed Amazon&#x27;s rewired value chain, changing standards for customer demand, fulfillment, and performance evaluation.</td><td>Digital disruption strategies may not only affect a focal firm&#x27;s value creation but also affect other firms&#x27; strategic options by changing the business landscape.</td><td>Rewired value chains have a contingent potential to reshape the existing landscape; the market&#x27;s openness to digital disruption is represented by the probability of endorsing landscape changes.</td></tr><tr><td>Absolute performance</td><td>Total revenue growth: For example, in 2022, Woolworths generated a total online net revenue of US$4 billion, a year-to-year increase of 29.1%.</td><td>Firms that seek to improve absolute performance compare their performance against their past performance in their strategizing.</td><td>The fitness level (height) of a firm reached in the landscape.</td></tr><tr><td>Relative performance</td><td>Relative revenue growth: For example, in 2022 Amazon Australia achieved 23.8 percentage points higher online net revenue growth relative to Woolworths.</td><td>Firms that seek to improve relative performance compare their performance against the competitors&#x27; performance in their strategizing.</td><td>The difference in fitness levels (or in heights) between a focal firm and its competitor in the landscape</td></tr></table>

In this reshaped business landscape, each decision $d _ { m }$ interacts with a newly drawn set of elements $\mathbf { d } _ { - m }$ to yield new performance contributions $\pi { m . } ^ { 8 }$ A digitally disrupted landscape entails a fresh field with different peaks, valleys, and gradients for all players as a digital disruption strategy creates new trade-offs for both customers and rivals. Moreover, if a firm launches a strategic digital disruption initiative, it may change how the market perceives both its own and a rival’s positioning. Here, our landscape metaphor also enables us to capture how a given initial landscape is recast: a new digitally disrupted landscape can replace the (initial analog) landscape when redefining “what performance means” (Christensen & Bower, 1996, p. 202). If the industry later endorses this “digitally disrupted landscape,” we then call it a “new landscape.”

We do not model firms’ strategic choices as a dichotomy of digital disruption versus adaptation. Rather, we recognize that digital disruptions originate from digital strategic initiatives to which firms commit a portion of their resources (Piccoli et al., 2022). Accordingly, we represent a firm’s strategy by the portion of initiatives aimed at digital disruption: $\alpha _ { i } \in [ 0 , 1 ]$ This variable parsimoniously captures the firm’s resource allocation toward unleashing digital disruptions. While this variable range accepts that digital disruption may usher in seismic landscape changes, executing a digital disruption strategy is a matter of degree— from rare attempts at a ground-breaking digital product or service offerings to frequent launches of digital disruption initiatives. Complementing our representation of a digital disruption strategy as a resource allocation choice, a firm enacts initiatives to adapt to an existing landscape per probability $1 - \alpha _ { i }$ (third row of Table 1). Importantly, our parsimonious representation of these decisions captures how digital disruption and adaptation offset one another—thus reflecting a strategic resource allocation trade-off for a firm: Should they choose to enact new affordances provided by novel digital resources to rewire their value chain or not?

## Modeling Digital Disruption and Adaptation Strategies

When firm i attempts to search for a new landscape, it hopes that its digitally disrupted landscape (represented by the new NK fitness function $\Pi _ { i } ^ { ' } )$ will realize and unsettle the old one (represented by the current NK fitness function Π). That is, digital disruption occurs when a landscape is replaced by a new digitally disrupted landscape.

The adoption of a new landscape—i.e., an industry with an architecturally rewired value chain enabled or embodied via digital resources (Baiyere et al., 2023; Lyytinen & Rose, 2003)—implies that all market players now face the realities of the new, digitally disrupted landscape. However, this landscape change is neither deterministic nor fully controlled by the focal firm. Actual success in landscape adoption may depend both on a rival’s strategic action (e.g., exit, reposition, or mimic) and market-level factors, such as network externalities, regulations, appropriability regimes, complementary assets, or even sheer chance (e.g., Argyres et al., 2015). However, to focus on parsimonious strategies amid varied industry appetite for digital disruption, we assume that each firm faces an equal chance of ?? for the adoption of a reshaped landscape. We refer to this exogenous probability as the market’s openness to digital disruption, a variable that subsumes institutional regimes, digital readiness, and other industry-level factors that could influence the openness of markets to endorsing landscape changes (e.g., Hargadon & Douglas, 2001; Hinings et al., 2018; Karimi & Walter, 2015).<sup>9</sup>

## Model Timeline

Firms search simultaneously as depicted in Figure 1. Our model starts at time t = 1 as focal Firm i randomly occupies position ${ \bf d } _ { i } ^ { 1 }$ in the initial landscape with its digital disruption strategy $\alpha _ { i } .$ In any period t with probability $\alpha _ { i } ,$ , the firm launches a digital disruption initiative and begins to search on the digitally disrupted landscape. Otherwise, it opts for adaptation and search on the existing landscape with probability $1 - \alpha _ { i }$ (Step 1).

In Step 2, search undergoes a randomly drawn product element $d _ { m } d _ { \scriptscriptstyle { n } }$ starting from the old configuration ${ \bf d } _ { i } ^ { t }$ . Each round, the firm can try N such iterative changes.<sup>10</sup> A firm will enact the newly found configuration $\mathbf { d } _ { i } ^ { t + 1 }$ only if this yields performance exceeding the current configuration— formally, only if $\Pi _ { i } ^ { ' } ( { \bf d } _ { i } ^ { t + 1 } ) > \Pi ( { \bf d } _ { i } ^ { t } )$ when searching on a digitally disrupted landscape, or only if $\Pi ( \mathbf { d } _ { i } ^ { t + 1 } ) > \Pi ( \mathbf { d } _ { i } ^ { t } )$ for search on the existing landscape. Otherwise, reversion to configuration ${ \bf d } _ { i } ^ { t }$ on the old landscape ends the search (Step 3 with position reverting to $\mathbf { d } _ { i } ^ { t + 1 } = \mathbf { d } _ { i } ^ { t } )$ . Thus, while a new landscape emerges from a stochastic process (akin to unconstrained idea generation), the firm maintains some control over both its selection and terrain position for implementation.

When any firm ushers in a digitally disrupted landscape, the industry then assesses the landscape for adoption (or not) in Step 4. If the industry adopts the firm’s digitally disrupted landscape at t+1, then the firm search ensues starting from configuration $\mathbf { d } _ { i } ^ { t + 1 }$ (and rival firm likewise on $\mathbf { d } _ { j } ^ { t + 1 } )$ on the new landscape. Otherwise, the firm restarts from its prior ${ \bf d } _ { i } ^ { t }$ (Step 4 reverting to $\mathbf { d } _ { i } ^ { t + 1 } = \mathbf { d } _ { i } ^ { t } )$ on the old landscape.<sup>11</sup>

![](/api/attachments/5M5Q2XAN/fulltext/images/ae170ec10a287623f8c41bfc0dc29fb8389b9bd944e315cffde973ee1d4c7da7.jpg)  
Figure 1. Competitive Dynamics at Strategic, Operational, and Market Levels

## How Firms Aspire for Performance

When allocating resources to strategic initiatives, firms pursue different performance priorities. We focus on two archetypical performance goals that firms seek in their strategizing: absolute versus relative performance (e.g., Luo et al., 2007; Short & Palmer, 2003). A firm that maximizes absolute performance emphasizes improvements over its own past attainments. In contrast, a firm seeking to improve relative performance focuses on doing better than competitors. This distinction highlights that a firm attends to its own and/or a rival’s performance as reference points in shaping its search behavior.<sup>12</sup>

We operationalize a firm’s absolute performance as its performance (height in the terrain) in the final period of a given simulation run, i.e., $\Pi _ { i } ( { \bf d } _ { i } ^ { T } )$ for $T ~ = ~ 5 0$ periods.<sup>13</sup> We operationalize the relative performance of Firm i as the performance gap (height difference) between two firms, that is, $\varDelta \Pi _ { i } = \Pi _ { i } ( \mathbf { d } _ { i } ^ { T } ) - \Pi _ { j } ( \mathbf { d } _ { j } ^ { T } ) \ ( i \neq j )$ in the final period T of a simulation run. In the following analyses, we shall juxtapose all competitive outcomes for relative versus absolute performance.

## Simulation and Analyses

We performed several simulation experiments. Table 2 reports the parameters used in our simulation experiments and summarizes our robustness analyses. In the reported main analyses, we parameterized the number of strategic product elements to $\bar { N } = 1 2 . ^ { 1 4 }$ Since simulation results are subject to random fluctuations, we replicated each run 10,000 times. All presented results proved statistically significant at $p < 0 . 0 1$

## Digital Disruption Strategies and Absolute Performance

Figure 2 plots the absolute performance of a focal Firm 1 subject to different conditions.<sup>15</sup> Horizontal axes mark a firm’s strategy ranging from no commitment $( \alpha _ { 1 } = 0 )$ to a fullfledged commitment $( \alpha _ { 1 } = 1 )$ to digital disruption. Vertical axes track average focal performance outcomes attained. Paired curves each plot Firm 1’s performance according to a rival Firm 2’s strategy $\alpha _ { 2 }$ . When facing a digitally disruptive (or adaptive) rival firm, the focal firm intuitively selects its own digital disruption allocation $\alpha _ { 1 }$ to maximize its performance on the solid (or dotted) curve.

<table><tr><td colspan="3">Table 2. Variables and Parameterization</td></tr><tr><td>Symbol</td><td>Definition</td><td>Parameterization</td></tr><tr><td>N</td><td>Number of elements of a product offering</td><td>N =12 in main analyses; N ∈ {10,16} in robustness analyses.</td></tr><tr><td>K</td><td>Landscape complexity</td><td>K = 6 in main analyses; K ∈ {4,8} in robustness analyses.</td></tr><tr><td>αi</td><td>Firm i&#x27;s digital disruption allocation</td><td>Decision variable αi ∈ {0,0.1,0.2, ...,0.9,1}</td></tr><tr><td>di</td><td>Product vector for Firm i</td><td>Endogenous variable representing Firm i&#x27;s current positioning</td></tr><tr><td>T</td><td>Final simulation period (i.e., termination at t = T)</td><td>T = 50 in main analyses; T ∈ {10,25,100,200,1000} in robustness analyses.</td></tr><tr><td>ρ</td><td>Openness to digital disruption</td><td>Exogenous ρ ∈ {0.1,0.9} in main analyses; Exogenous ρ ∈ {0.1,0.5,0.9} in robustness analyses</td></tr><tr><td>Πi</td><td>Absolute performance of Firm i</td><td>Endogenous outcome variable</td></tr><tr><td>ΔΠi</td><td>Relative performance of Firm i</td><td>Endogenous outcome variable</td></tr><tr><td colspan="3">Model extensions</td></tr><tr><td colspan="2">Similarity of digital disruption landscapes compared to the existing landscape</td><td>Number of overlapping elements S ∈ {0,3,6}</td></tr><tr><td colspan="2">Different representations of landscape replacement</td><td>Deterministic: select the landscape with the highest-performing product configuration.Stochastic: select the landscape with adoption chances proportional to current performances.</td></tr><tr><td colspan="2">Digital disruption strategies can change landscape complexity</td><td>Digital disruption strategies reduce (increase) complexity by affecting K such that ΔK ∈ {-2,+2}</td></tr><tr><td colspan="2">Adaptation strategy comprises local and distant search</td><td>In each adaptive search round, the firm creates and evaluates a long jump of max. length |N|</td></tr><tr><td colspan="2">Long-jump strategy replaces digital disruption strategy</td><td>Decision variable, δi ∈ {0,0.1,0.2, ...,0.9,1} for the inclination to long jumps of max. length |N|</td></tr></table>

![](/api/attachments/5M5Q2XAN/fulltext/images/07aa4040c12dcf15e782e5cbce67a6a55ed7d4bb36312c921fe47070f2f7f1a0.jpg)

![](/api/attachments/5M5Q2XAN/fulltext/images/cae72259e4a855f287ce1c35e03b7a2c41d85b73f8dca569b4a669682e72749d.jpg)  
Figure 2. Absolute Performance of the Focal Firm (Vertical Axis) as a Function of its Competitor’s Strategy under Low and High Openness to Digital Disruption

In an industry setting open to digital disruption (left panel of Figure 2), Firm 1’s performance exhibits an inverted parabolic shape where the rival mostly declines digital disruption $( \alpha _ { 2 } =$ 0.1). Here, the focal firm responds best by making small resource commitments to digital disruption $( \alpha _ { 1 } = 0 . 2 )$ . Such a small but purposeful resource commitment creates a real option for the firm to reshape the landscape, but only if its full execution offers a performance advantage. That said, a fullfledged digital disruption strategy would incur substantial opportunity costs: when search in the digitally disrupted landscape yields no improvement, the firm must retreat to its position on the old landscape. In other words, foregone adaptation to the existing landscape embodies opportunity costs for the firm.

Moreover, the focal firm’s performance suffers when the rival firm intensifies its commitment to digital disruption $( \alpha _ { 2 } =$ 0.9). To best respond to that situation, the focal firm should eliminate its digital disruption initiatives by setting its resource allocation near $\alpha _ { 1 } = 0 .$ . The rival’s digital disruption reaction thus inflicts harm to the focal firm and induces its retrenchment to avert further turbulence.

When the industry is more open to digital disruption (right panel of Figure 2), the focal firm’s trade-off shifts in favor of digital disruption, but only if the rival firm favors adaptation over digital disruption $( \alpha _ { 2 } = 0 . 1 )$ ). Here, results argue for an ideal strategy that balances search on digitally disrupted versus search on the existing landscape $( \alpha _ { 1 } = 0 . 8 )$ . This balance enables the firm to exploit the substantial upside potential of launching a successful digital disruption while retaining the benefits of adaptation in the current landscape. However, when the rival follows a digital disruption strategy $( \alpha _ { 2 } = 0 . 9 )$ , focal performance drops monotonically per its own investments into digital disruption. Intuitively, any further focal digital disruption initiatives would inject more turbulence hindering performance gains and eroding internal capabilities, so adaptation $( \alpha _ { 1 } = 0 )$ emerges as the focal firm’s best response. Therefore, in a market environment open to digital disruption, a balanced digital disruption strategy offers the highest absolute performance, unless a rival seeks a pure digital disruption strategy where adaptation-only is the best response.

## Digital Disruption Strategies and Relative Performance

Figure 3 displays the relative performance of a focal firm on the vertical axes under the same conditions in Figure 2. Again, the solid (or dotted) curve represents the focal firm facing a digitally disruptive (or adaptive) rival. Under relative performance, the focal firm outperforms where its relative performance exceeds the horizontal zero reference line. Here, the focal firm “wins”

against the rival firm in terms of relative performance; it “loses” below the zero line.

Under market conditions of low openness to digital disruption (left panel of Figure 3), our prior conclusion holds for a focal firm’s limited resource commitment to the digital disruption strategy since the relative performance curves eventually suffer when a focal firm pursues excessive digital disruption. Regardless of a rival’s strategy, the focal firm refrains from allout digital disruption since this seems unlikely to improve the landscape in a market not open to such. For maximum relative performance, the focal firm should limit digital disruption efforts to maximize relative performance $( \alpha _ { 2 } = 0 . 3 )$ . The focal firm experiences a superior (solid) performance curve when a rival firm emphasizes digital disruption. The fuel for that outperformance gap is the rival’s foregone adaptation benefits (on the given landscape) plus wasteful digital disruption investments that end up favoring the gap for Firm 1.

Under market conditions of high openness to digital disruption (right panel in Figure 3), a reversal emerges: consistent, monotonically increasing relative-performance curves (both solid and dotted) now show the focal firm benefits in relative terms when it enacts a pure digital disruption strategy—even when a rival responds in kind per the $( \alpha _ { 2 } = 0 . 9 )$ solid curve.

By choosing a full-fledged digital disruption strategy, the focal firm offsets losses from foregone adaptation with benefits as the rival underperforms in the new landscape. As successful digital disruption initiatives can potentially harm a rival’s performance, a digital disruption strategy can improve the focal firm’s relative position, whether by pulling ahead of or sinking the rival.

As indicated by the differences in the high openness (right) panels of Figures 2 and 3, shifting the focal firm’s objectives from absolute to relative performance, in effect, reverses the strategic trade-offs when its rival enacts a digital disruption strategy. For the focal firm, an adaptation strategy yields the highest absolute but low relative performance, while a fullfledged digital disruption strategy yields the highest relative result at the expense of absolute performance.

## Validation and Robustness of the Simulation Model

Here, we explain how we attempted to ensure the internal validity of our model and probe its external validity. We also created an online application that makes our simulation analyses and code openly accessible at https://mtarakci. shinyapps.io/DigitalDisruption/.

![](/api/attachments/5M5Q2XAN/fulltext/images/1f97cd99d4bd537b0c910b12b56e69104e780ca6e5221046b6474049a2acbdd9.jpg)

![](/api/attachments/5M5Q2XAN/fulltext/images/e4343663e08ab6eebd5647c73f40f53bb0dfccd1218f1c167bfc935a94735b88.jpg)  
Figure 3. Relative Performance of the Focal Firm (Vertical Axis) as a Function of its Competitor’s Strategy Under Low and High Openness to Digital Disruption

## Establishing Internal Validity

First, we performed robustness analyses (Table 2) by varying the parameterizations and specifications of our model (e.g., Brunswicker et al., 2019; Nan & Tanriverdi, 2017). As for model parameters at the firms’ digital strategy level, we systematically varied both model size and complexity. We simulated both tighter (N = 10, K = 4) and wider (N = 16, K = 8) landscape models with 10,000 replications per simulation instance (plus in-between NKs). Our main analyses and discussion of disruptions have assumed complexity-preserving landscape changes as a way to focus on the effects of a reshaped landscape featuring a fixed level of ruggedness. However, we still observe consistent patterns when digital disruption initiatives either reduce landscape ruggedness (i.e., setting N = 12 and K = 6 transforms into N = 12 and K = 4 with ΔK = −2) or raise it (i.e., setting N = 12 and K = 6 transforms into N = 12 and K = 8 with ΔK = +2). The effects of digital disruption thus do not hinge critically on how initiatives affect complexity.

Second, we relaxed the main assumptions of our model regarding firm-level strategies and industry-level landscape changes. We varied the extent to which digital disruption leads to landscapes similar to the existing one, tuning similarity from S = 0 (no similarity, N decisions’ contributing as completely new) up to S = N/2 where half the contributions remain the same even where a firm successfully unleashes digital disruption.<sup>16</sup> These analyses show all main results continuing to hold qualitatively for higher similarity while intuitively less accentuated (with competitive effects of landscape changes mitigated by rising S). This means that, whether digital disruption strategies alter complexity or landscapes vary in similarity, our key insights remain.

To probe the possibility of accentuated firm control during the landscape generation process, we also assessed a model variant reflecting firms that generate a number L of digitally disrupted landscapes for evaluation and select the most promising landscape after a disruptive move. We found our main findings to hold for widely varied parameterizations L∈{2,5,10}; however, tighter firm control on landscape quality intuitively adds absolute performance to its digital disruption strategy.

We further explored intermediate levels of market openness to digital disruption (i.e., ?? = 0.5). This variation intuitively favors a more balanced blend of adaptation and digital disruption strategies. While the quantitative outcomes of these models change, all our results persist qualitatively. These findings lend further validity to our model outcomes in that they broadly hold for a wider set of parameters generally representing firm strategies.

With respect to the level of competition, one salient assumption concerns the adoption of digital disruptions by the market: it randomly adopts a reshaped landscape with an exogenous probability ??. We investigated two alternative conceptualizations for this adoption process. First, we incorporated a deterministic performance-based conceptualization that greedily selects the landscape with the best performance position for any firm. While this view does curb the random element in digital disruption, the turbulence from digital disruption strategies eclipses this effect. Second, we examined a stochastic performance-based adoption. In this variant, we modeled adoption as a probability given by a ratio of the digitally disrupting firm’s performance to the sum of both firms’ results. This probabilistic approach implies that the industry can be expected to adopt the reshaped landscape with greater likelihood when the focal firm can demonstrate improved performance. All theoretical insights remain.

Finally, we simulated a new model variant where a firm’s allocation to a digital disruption strategy (represented by decision α) is replaced by a different, yet analogous, decision: a firm’s allocation to long jumps (represented by decision δ). Long jumps are completely redrawn vectors equivalent to Kauffman (1993) and Levinthal (1997). Here, firms evaluate the quality of long jumps in their search and pursue only those yielding a performance benefit. We observed the role of long jumps proving much less impactful compared to digital disruption strategies. First, no difference emerged between absolute and relative performance objectives for the most effective long-jump strategy. Second, a rival’s long-jump strategy proved irrelevant to the focal firm’s optimal strategy of balancing local and distant search. The divergent result here in the long-jump model variant arose since digital disruption strategies, unlike long-jump strategies, entail the creation of a fresh landscape and its new forced reality for all actors.

## Exploring External Validity

NK models simulate complex and dynamic interdependent processes, so the extent to which such a model accurately predicts and captures the essential behavior of a real-world system is limited (Railsback & Grimm, 2019). Also, using simulations to theorize about unknown outcomes of digital disruption in strategic competition heightens epistemic opacity in validating the results (Davis et al., 2007; Harrison et al., 2007).

Still, for purposes of result exploration and interpretation, we revisit the actual revenue trajectories reported for Woolworths and Amazon in 2021 and 2022 (Birmingham & McIntyre, 2023; eCommerceDB, 2023) in light of our simulation results. In terms of absolute performance, Woolworths’s online net revenue grew to US\$4,052 million in 2022 (eCommerceDB, 2023), while Amazon Australia generated online net revenue of US\$2,600 million (Birmingham & McIntyre, 2023). In the language espoused in our model, Woolworths’s adaptation strategy seemed a commensurate choice: Woolworths was able to nimbly allocate resources toward selected adaptation initiatives through which it could observe, learn, and iterate into the reshaped landscape at relatively low risk. Year-byyear, they improved on their absolute performance; in 2022, for example, by 29.1% (eCommerceDB, 2023).

At the same time, Amazon’s digital disruption strategy appeared to be successful in terms of relative performance. Comparatively speaking, Amazon’s annual online revenue growth rate exceeded that of Woolworths since it entered the Australian market. In 2022, for example, Amazon’s online revenue growth rate outperformed Woolworths by 23.8 percentage points.

While these facts are aligned with the outcomes resulting from our simulation, we highlight the parsimonious and stylized nature of NK model simulations (Ganco, 2017). We are not using the simulation to predict or explain the performance outcomes achieved by Woolworths and Amazon Australia. Many factors contribute to their outcomes beyond the simulation model we present. We merely note that the reported outcomes align with the theoretical arguments we developed through simulation. Our model is an abstraction of reality that brings some aspects into focus (e.g., resource allocation choices or the idea of endogenous landscape change) while omitting others (e.g., resource endowments, leadership, or customer behavior). Though we find that our case aids the theoretical sense-making process, we also caution that establishing external and predictive validity of our theoretical insights will require future empirical testing.

## Discussion

## Contributions and Implications

The literature on digital business strategy has so far studied key organizational capabilities for embracing digital technologies (e.g., Bharadwaj et al., 2013; Park & Mithas,

2020), the mechanisms involved in a firm’s action to rewire their value chain (e.g., Lucas Jr. & Goh, 2009; Lyytinen & Rose, 2003; Riemer & Johnston, 2019), and the resulting changes to scope, scale, and source of value creation and capture (e.g., Adner, 2002; Sabherwal & Chan, 2001; Utesheva et al., 2016; Wade & Hulland, 2004). We add to this conversation a simulation-based examination of digital disruption that features endogenously changing landscapes in strategic competition. Key to our model is how a firm’s rewiring of its value chain through novel application of digital technology can disrupt the business landscape for all players, thus engaging both the firm’s and rivals’ digital strategic initiatives that must operate on a newly disrupted landscape. This analysis allows us to expose how different strategies (i.e., digital disruption versus adaptation) play out in competition— a question yet unanswered in the literature (Bharadwaj et al., 2013; Furr & Shipilov, 2019; Park & Mithas, 2020).

Our insights offer several theoretical and managerial implications. First, we unearth an intricate interplay between digital disruption and adaptation strategies, contingent on performance priority, market openness, and the actions pursued by competitors. In Table 3, we summarize the insights we gained on the most effective digital strategies for firms that emanate from these contingencies. Explicating this interplay offers a much-needed advance considering how popular cases of digitally disrupting firms have skewed prevalent managerial wisdom to extol digital disruption strategies (e.g., Head, 2017; Lahshinsky, 2012). In a similar vein, the digital disruption literature has often highlighted the disruptive potential in digital technology (e.g., Autio et al., 2021; Furr & Shipilov, 2019) but without scrutinizing its implications for firm performance—let alone in competitive strategy settings. Our theoretical insights help shift the debate toward expected rather than coincidental performance outcomes.

Second, our analyses suggest that in most scenarios, the true promise of digital disruption strategies is in boosting relative performance. We thus advise researchers and practitioners against miscasting a fall in absolute performance as a failure of digital disruption when a firm may actually advance its relative performance. Rather, in light of their performance aims, the agency that firms opt to exert (Riemer & Johnston, 2019) and the architectural rewiring they can accomplish (Lyytinen & Rose, 2003) must both be viewed as contingent upon the market openness in which they operate (Bailey et al., 2022; Utesheva et al., 2016). That said, a sustained relative performance advantage might later translate into absolute performance advantages when competitive pressures drive out outperformed competitors in the long run.

Third, our analyses also expose the situations in which digital disruption and adaptation strategies are effective in tandem, and so offset each other’s risks (Table 3). Adaptation offers more predictable performance gains, but a pure adaptation strategy may leave a firm stranded on a local optimum that forfeits opportunities when disrupting the landscape. A digital disruption strategy may help dislodge a firm from local optima and dethrone its competitors, yet a pure disruption strategy eschews advancement on a given landscape. Balancing both strategies mitigates respective costs while helping a firm advance on newly shaped landscapes. However, our analyses also identify polar conditions where a firm should refrain from disruption altogether, such as when market openness to disruption is low, the competitor disrupts, or the firm strives for absolute performance. Contrariwise, when a market is open and the firm’s objective is relative performance, then a pure digital disruption strategy appears recommendable. Together, these insights widen the focus of prior research, which has so far focused on either disruptor or disruptee alone (e.g., Lyytinen & Rose, 2003; Riemer & Johnston, 2019). Moreover, they can guide firms seeking a return on investment from their digital strategic initiatives because they draw attention to ensuring alignment between ambition (to disrupt or not) and success metric (absolute or relative performance gains).

Table 3. Focal Firm’s Most Effective Strategic Choices Depending on Performance Priority, Market Openness, and Competitor Strategy

<table><tr><td rowspan="2"></td><td colspan="4">When the focal firm prioritizes:</td></tr><tr><td colspan="2">Absolute performance</td><td colspan="2">Relative performance</td></tr><tr><td rowspan="2">Market openness to digital disruption</td><td colspan="2">Rival firm&#x27;s strategy</td><td colspan="2">Rival firm&#x27;s strategy</td></tr><tr><td>Adaptation</td><td>Digital disruption</td><td>Adaptation</td><td>Digital disruption</td></tr><tr><td>Low</td><td>Adapt and rarely disrupt</td><td>Adapt</td><td>Adapt and rarely disrupt</td><td>Adapt and rarely disrupt</td></tr><tr><td>High</td><td>Balance adapt and disrupt</td><td>Adapt</td><td>Disrupt</td><td>Disrupt</td></tr></table>

## Limitations and Future Research Opportunities

Our goal has been to develop theoretical insights, not to test them. Doing so should be the next logical step. Our study, thus, presents an opportunity for future interdisciplinary and empirical research into the role of digital disruption in strategic competition, irrespective of whether such work refutes or supports the insights we offer.

As mentioned above, simulation-based theory building benefits from further empirical testing as an immediately valuable next step, not just to examine its outcomes but also to explore boundary conditions more profoundly. For example, future research can develop a multi-industry framework that involves both cut-throat competition and cooperation. Taken together with our work, these efforts would equip decision-makers with an even more actionable and robust toolkit for digital business strategy-making and it will ultimately improve the quality of theorizing about digital disruption.

In addition, we see opportunities for further theoretical and methodological digital strategy research based on simulations. One key aspect of our analyses was to reveal both the role of the demand side (Adner, 2002; Christensen & Bower, 1996) and the turbulence created by disrupting firms. Posen and Levinthal (2012) as well as Nan and Tanriverdi (2017) already argued that exogenous turbulence can shape firms’ strategies. However, they did not see this theoretical link operating in the reverse direction where strategic choices in the digital realm can endogenously unleash turbulence even for physical realities. Our simulation model endogenized disruptions as competitive strategies, which is a key premise of digital disruption (Adner, 2002; Karimi & Walter, 2015; Riemer & Johnston, 2019). This new approach may also be useful to scrutinize other ideas about the shifts brought forward by digitalization, such as the concept of “digital first” (Baskerville et al., 2020); that is, the view that many if not most aspects of the human experience now occur first in a digital world that then shapes and creates (rather than reflects) the physical reality through a process of ontological reversal. As in digital disruption, the idea of changing landscapes may prove helpful to understanding the ontological reversal process, so our way of modeling endogenous landscape changes may also be fruitful to understanding digital-first implications for digital human experiences, digital ecosystems, or digital human values.

## Acknowledgments

We thank Jerry Kane and the associate editor for their exceptional editorship and the three reviewers for their constructive feedback. Our simulation experiments (including additional analyses and code) are available at https://mtarakci.shinyapps.io/DigitalDisruption/. We thank participants at the Israel Strategy Conference, the University of Cologne, the University of Southern Denmark, Kuhne Logistics University, and the Rotterdam School of Management for their feedback during presentations. Usual disclaimers apply.

## References

Adner, R. (2002). When are technologies disruptive? A demand-based view of the emergence of competition. Strategic Management Journal, 23(8), 667-688. https://doi.org/10.1002/smj.246

Adner, R. (2021). Winning the right game: How to disrupt, defend, and deliver in a changing world. MIT Press.

Adner, R., Puranam, P., & Zhu, F. (2019). What is different about digital strategy? From quantitative to qualitative change. Strategy Science, 4(4), 253-261. https://doi.org/10.1287/stsc.2019.0099

Alihmahomed-Wilson, J., & Reese, E. (Eds.). (2020). The cost of free shipping: Amazon in the global economy. Pluto Press.

Amit, R., & Han, X. (2017). Resource configuration as a source of value creation in a digitally enabled world. Strategic Entrepreneurship Journal, 11(3), 228-242. https://doi.org/ 10.1002/sej.1256

Arend, R. J. (2022). Balancing the perceptions of NK modelling with critical insights. Journal of Innovation and Entrepreneurship, 11(23), 1-15. https://doi.org/10.1186/s13731-022-00212-9

Argyres, N., Bigelow, L., & Nickerson, J. A. (2015). Dominant designs, innovation shocks, and the follower’s dilemma. Strategic Management Journal, 36(2), 216-234. https://doi.org/10.1002/ smj.2207

Autio, E., Mudambi, R., & Yoo, Y. (2021). Digitalization and globalization in a turbulent world: Centrifugal and centripetal forces. Global Strategy Journal, 11(1), 3-16. https://doi.org/ 10.1002/gsj.1396

Bailey, D. E., Faraj, S., Hinds, P. J., Leonardi, P. M., & von Krogh, G. (2022). We are all theorists of technology now: a relational perspective on emerging technology and organizing. Organization Science, 33(1), 1-18. https://doi.org/10.1287/orsc.2021.1562

Baiyere, A., Grover, V., Lyytinen, K., Woerner, S., & Gupta, A. (2023). Digital “x”—Charting a path for digital-themed research. Information Systems Research, 34(2), 463-486. https://doi.org/10.1287/isre.2022.1186

Baskerville, R., Myers, M. D., & Yoo, Y. (2020). Digital First: The ontological reversal and new challenges for IS research. MIS Quarterly, 44(2), 509-523. https://doi.org/10.25300/MISQ/2020 14418

Beese, J., Haki, K., Aier, S., & Winter, R. (2019). Simulation-based research in information systems. Business & Information Systems Engineering, 61(4), 503-521. https://doi.org/10.1007/s12599-018- 0529-1

Bharadwaj, A., El Sawy, O. A., Pavlou, P. A., & Venkatraman, N. (2013). Digital business strategy: Toward a next generation of insights. MIS Quarterly, 37(2), 471-482. https://doi.org/ 10.25300/MISQ/2013/37:2.3

Birmingham, A., & McIntyre, P. (2023). Amazon Australia cracks \$100m in ad sales, \$1.3bn from online store, \$250m in Amazon Prime subscriptions; total sales hit \$2.6bn but posts loss of \$1.5m. Mi3. https://www.mi-3.com.au/27-03-2023/amazons-ad-businessaustralia-tops-100m-over-60-cent-ecommerce-outperforms-marketgold

Bromiley, P., & Harris, J. D. (2014). A Comparison of alternative measures of organizational aspirations. Strategic Management Journal, 35(3), 338-357. https://doi.org/10.1002/smj.2191

Brunswicker, S., Almirall, E., & Majchrzak, A. (2019). Optimizing and satisficing: The interplay between platform architecture and producers’ design strategies for platform performance. MIS

Quarterly, 43(4), 1249-1277. https://doi.org/10.25300/ MISQ/2019/13561

Chandrasekaran, A., Linderman, K., Sting, F. J., & Benner, M. J. (2016). Managing R&D project shifts in high-tech organizations: A multi-method study. Production and Operations Management, 25(3), 390-416. https://doi.org/10.1111/poms.12410

Chen, M.-J., & Miller, D. (2012). Competitive dynamics: Themes, trends, and a prospective research platform. Academy of Management Annals, 6(1), 135-210. https://doi.org/10.5465/ 19416520.2012.660762

Christensen, C. M., & Bower, J. L. (1996). Customer power, strategic investment, and the failure of leading firms. Strategic Management Journal, 17(3), 197-218. https://doi.org/10.1002/(SICI)1097- 0266(199603)17:3<197::AID-SMJ804>3.0.CO;2-U

Christensen, C. M., Raynor, M. E., & McDonald, R. (2015). What is disruptive innovation? Harvard Business Review, 93(12), 44-53.

Cyert, R. M., & March, J. G. (1963). A behavioral theory of the firm. Prentice Hall.

Davis, J. P., Eisenhardt, K. M., & Bingham, C. B. (2007). Developing theory through simulation methods. Academy of Management Review, 32(2), 480-499. https://doi.org/10.5465/amr.2007.2435 1453

eCommerceDB. (2023). eCommerce revenue analytics: Woolworths.com.au. ECDB. Retrieved May 23, 2023 from https://ecommercedb.com/store/woolworths.com.au

Faulkner, P., & Runde, J. (2019). Theorizing the Digital Object. MIS Quarterly, 43(4), 1279-1302. https://doi.org/10.25300/MISQ/ 2019/13136

Furr, N., & Shipilov, A. (2019). Digital doesn’t have to be disruptive. Harvard Business Review, 97(4), 94-103.

Ganco, M. (2017). NK Model as a representation of innovative search. Research Policy, 46(10), 1783-1800. https://doi.org/10.1016/ j.respol.2017.08.009

Ganco, M., & Hoetker, G. (2009). NK Modeling methodology in the strategy literature: Bounded search on a rugged landscape. In D. D. Bergh & D. J. Ketchen (Eds.), Research Methodology in Strategy and Management (Vol. 5 pp. 237-268). Emerald.

Garcia, R., & Calantone, R. J. (2002). A critical look at technological innovation typology and innovativeness terminology: A Literature review. Journal of Product Innovation Management, 19(2), 110- 132. https://doi.org/10.1016/S0737-6782(01)00132-1

Gavetti, G., Levinthal, D. A., & Rivkin, J. W. (2005). Strategy Making in novel and complex worlds: The power of analogy. Strategic Management Journal, 26(8), 691-712. https://doi.org/10.1002/ smj.475

Giustiziero, G., Kretschmer, T., Somaya, D., & Wu, B. (2023). Hyperspecialization and hyperscaling: A resource-based theory of the digital firm. Strategic Management Journal, 44(6), 1391-1424. https://doi.org/10.1002/smj.3365

Hargadon, A. B., & Douglas, Y. (2001). When innovations meet institutions: Edison and the design of the electric light. Administrative Science Quarterly, 46(3), 476-501. https://doi.org/ 10.2307/3094872

Harrison, J. R., Lin, Z., Carroll, G. R., & Carley, K. M. (2007). Simulation Modeling in organizational and management research. Academy of Management Review, 32(4), 1229-1245. https://doi.org/10.5465/AMR.2007.26586485

Head, B. (2017). The Amazon effect. Company Director, 33(10), 22- 27.

Henfridsson, O., & Bygstad, B. (2013). The generative mechanisms of digital infrastructure evolution. MIS Quarterly, 37(3), 907-931. https://doi.org/10.25300/MISQ/2013/37.3.11

Hinings, C. R., Gegenhuber, T., & Greenwood, R. (2018). Digital innovation and transformation: An institutional perspective. Information and Organization, 28(1), 52-61. https://doi.org/ 10.1016/j.infoandorg.2018.02.004

Kallinikos, J., Aaltonen, A., & Marton, A. (2013). The ambivalent ontology of digital artifacts. MIS Quarterly, 37(2), 357-370. https://doi.org/10.25300/MISQ/2013/37.2.02

Karimi, J., & Walter, Z. (2015). The role of dynamic capabilities in responding to digital disruption: A factor-based study of the newspaper industry. Journal of Management Information Systems, 32(1), 39-81. https://doi.org/10.1080/07421222.2015.1029380

Kauffman, S. A. (1993). The origins of order: Self-organization and selection in evolution. Oxford University Press.

Kotiloglu, S., Chen, Y., & Lechler, T. G. (2021). Organizational responses to performance feedback: A meta-analytic review. Strategic Organization, 19(2), 285-311. https://doi.org/10.1177/ 1476127019883361

Lahshinsky, A. (2012, November 16). Amazon’s Jeff Bezos: The ultimate disrupter. Fortune. https://fortune.com/2012/11/16/ amazons-jeff-bezos-the-ultimate-disrupter

Lepore, J. (2014, June 16). The disruption machine. The New Yorker. https://www.newyorker.com/magazine/2014/06/23/thedisruption-machine

Levinthal, D. A. (1997). Adaptation on rugged landscapes. Management Science, 43(7), 934-950. https://doi.org/10.1287/ mnsc.43.7.934

Levinthal, D. A., & March, J. G. (1981). A model of adaptive organizational search. Journal of Economic Behavior & Organization, 2(4), 307-333. https://doi.org/10.1016/0167- 2681(81)90012-3

Levinthal, D. A., & Warglien, M. (1999). Landscape design: Designing for local action in complex worlds. Organization Science, 10(3), 342-357. https://doi.org/10.1287/orsc.10.3.342

Lucas Jr., H. C., & Goh, J. M. (2009). Disruptive technology: How Kodak missed the digital photography revolution. Journal of Strategic Information Systems, 18(1), 46-55. https://doi.org/ 10.1016/j.jsis.2009.01.002

Luo, X., Rindfleisch, A., & Tse, D. K. (2007). Working with rivals: The impact of competitor alliances on financial performance. Journal of Marketing Research, 44(1), 73-83. https://doi.org/ 10.1509/jmkr.44.1.073

Lyytinen, K. (2022). Innovation logics in the digital era: A systemic review of the emerging digital innovation regime. Innovation: Organization & Management, 24(1), 13-34. https://doi.org/ 10.1080/14479338.2021.1938579

Lyytinen, K., & Rose, G. M. (2003). Disruptive information system innovation: The case of internet computing. Information Systems Journal, 13(4), 301-330. https://doi.org/10.1046/j.1365-2575. 2003.00155.x

March, J. G. (1991). Exploration and exploitation in organizational learning. Organization Science, 2(1), 71-87. https://doi.org/ 10.1287/orsc.2.1.71

Mihm, J., Sting, F. J., & Wang, T. (2015). On the effectiveness of patenting strategies in innovation races. Management Science, 61(11), 2662-2684. https://doi.org/10.1287/mnsc.2014.2128

Miller, K. D. (2015). Agent-based modeling and organization studies: A critical realist perspective. Organization Studies, 36(2), 175-196. https://doi.org/10.1177/0170840614556921

Mithas, S., Tafti, A., & Mitchell, W. (2013). How a firm’s competitive environment and digital strategic posture influence digital business strategy. MIS Quarterly, 37(2). https://doi.org/10.25300/MISQ/ 2013/37.2.09

Nan, N., & Tanriverdi, H. (2017). Unifying the role of IT in hyperturbulence and competitive advantage via a multilevel perspective of IS strategy. MIS Quarterly, 41(3), 937-958. https://doi.org/10.25300/MISQ/2017/41.3.12

Nell, P. C., Foss, N. J., Klein, P. G., & Schmitt, J. (2021). Avoiding digitalization traps: Tools for top managers. Business Horizons, 64(2), 163-169. https://doi.org/10.1016/j.bushor.2020.11.005

Park, Y., & Mithas, S. (2020). Organized Complexity of digital business strategy. MIS Quarterly, 44(1), 85-127. https://doi.org/ 10.25300/MISQ/2020/14477

Pentland, B. T., Yoo, Y., Recker, J., & Kim, I. (2022). From lock-in to transformation: A path-centric theory of emerging technology and organizing. Organization Science, 33(1), 194-211. https://doi.org/ 10.1287/orsc.2021.1543

Piccoli, G., Rodriguez, J., & Grover, V. (2022). Digital strategic initiatives and digital resources: Construct definition and future research directions. MIS Quarterly, 46(4), 2289-2316. https://doi.org/10.25300/MISQ/2022/17061

Pich, M. T., Loch, C. H., & de Meyer, A. (2002). On uncertainty, ambiguity, and complexity in project management. Management Science, 48(8), 1008-1023. https://doi.org/10.1287/mnsc.48.8. 1008.163

Posen, H. E., Keil, T., Kim, S., & Meissner, F. D. (2018). Renewing research on problemistic search—A review and research agenda. Academy of Management Annals, 12(1), 208-251. https://doi.org/10.5465/annals.2016.0018

Posen, H. E., & Levinthal, D. A. (2012). Chasing a moving target: Exploitation and exploration in dynamic environments. Management Science, 58(3), 587-601. https://doi.org/10.2307/ 41431672

Railsback, S. F., & Grimm, V. (2019). Agent-based and individualbased modeling: A practical introduction (2nd ed.). Princeton University Press.

Randolph, M. (2019). That will never work: The birth of Netflix and the amazing life of an idea. Octopus Publishing Group.

Riemer, K., & Johnston, R. B. (2019). Disruption as Worldview change: A Kuhnian analysis of the digital music revolution. Journal of Information Technology, 34(4), 350-370. https://doi.org/10.1177/0268396219835101

Sabherwal, R., & Chan, Y. E. (2001). Alignment between business and IS strategies: A study of prospectors, analyzers, and defenders. Information Systems Research, 12(1), 11-33. https://doi.org/ 10.1287/isre.12.1.11.9714

Schilling, M. A. (2000). Toward a general modular systems theory and its application to interfirm product modularity. Academy of Management Review, 25(2), 312-334. https://doi.org/10.5465/ amr.2000.3312918

Short, J. C., & Palmer, T. B. (2003). Organizational performance referents: An empirical examination of their content and influences. Organizational Behavior and Human Decision

Processes, 90(2), 209-224. https://doi.org/10.1016/S0749- 5978(02)00530-7

Siggelkow, N., & Rivkin, J. W. (2005). Speed and search: Designing organizations for turbulence and complexity. Organization Science, 16(2), 101-122. https://doi.org/10.1287/orsc.1050.0116

Tilson, D., Lyytinen, K., & Sørensen, C. (2010). Digital infrastructures: The missing IS research agenda. Information Systems Research, 21(4), 748-459. https://doi.org/10.1287/isre.1100.0318

Uotila, J., Keil, T., & Maula, M. (2017). Supply-side network effects and the development of information technology standards. MIS Quarterly, 41(4), 1207-1226. https://doi.org/10.25300/MISQ/ 2017/41.4.09

Utesheva, A., Simpson, J. R., & Cecez-Kecmanovic, D. (2016). Identity metamorphoses in digital disruption: A relational theory of identity. European Journal of Information Systems, 25(4), 344- 363. https://doi.org/10.1057/ejis.2015.19

Wade, M. R., & Hulland, J. (2004). The Resource-based view and information systems research: Review, extension, and suggestions for future research. MIS Quarterly, 28(1), 107-142. https://doi.org/10.2307/25148626

Woolworths Limited. (2012). 2012 Annual Report. Woolworths Limited. https://www.woolworthsgroup.com.au/content/dam/ wwg/investors/reports/2012/185965\_annual-report-2012.pdf

Yoo, Y. (2013). The tables have turned: How can the information systems field contribute to technology and innovation management research? Journal of the Association for Information Systems, 14(5), 227-236. https://doi.org/10.17705/1jais.00334

Zittrain, J. L. (2006). The generative internet. Harvard Law Review, 119, 1974-2040. https://doi.org/10.1145/1435417.1435426

## About the Authors

Fabian J. Sting is the Chaired Professor of Supply Chain Management—Strategy and Innovation at the University of Cologne, Germany, and a Professor of Digital Supply Chain Innovation at Rotterdam School of Management, Erasmus University. His research focuses on strategy implementation, value chain innovation, and the management of strategic projects.

Murat Tarakci is Professor and Chair of Innovation Strategy at Rotterdam School of Management, Erasmus University. His research and education activities focus on how organizations formulate and execute strategies to manage innovations. Murat’s mission is to create a positive impact by helping organizations address the grand societal challenges.

Jan Recker is an AIS Fellow, Alexander von Humboldt Fellow, Nucleus Professor for Information Systems and Digital Innovation at the University of Hamburg, and adjunct professor at the QUT Business School. His research focuses on digital innovation and entrepreneurship, digital solutions for sustainable development, and systems analysis and design. Most people like his podcast, This IS Research, more than his papers.
