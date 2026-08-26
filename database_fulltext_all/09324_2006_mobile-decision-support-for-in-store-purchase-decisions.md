---
otero_id: 9324
otero_key: "ABMRW5JS"
title: "Mobile decision support for in-store purchase decisions"
authors: "Hans van der Heijden"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.03.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Mobile decision support for in-store purchase decisions

Hans van der Heijden

University of Surrey, School of Management, Guildford, Surrey, GU2 7XH, United Kingdom

Available online 31 May 2005

## Abstract

Consumer decision making is a well-known application domain for decision support systems. Emerging from this domain is support for consumers <sup>b</sup>on the go,<sup>Q</sup> when they are actually inside a retail store. This paper introduces a <sup>b</sup>product attractiveness cue<sup>Q</sup> as a way of delivering decision support in this context. The paper also provides an experiment to examine the effectiveness of these cues in a laboratory environment. On the basis of these results (N = 86), the attractiveness cue was shown effective in improving the consideration set quality of the participants. This effect was stable across treatments with 10 and 20 products. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Decision support systems; Consumer decision making; Mobile devices; Product attractiveness cue; Laboratory experiment

## 1. Introduction

Evaluating retail products and selecting the best product among competing alternatives is a wellknown application domain for decision support systems. Although consumer decision support systems have been developed for decades, the wide-scale adoption of the Internet made them readily available for the mass market. This spawned a body of research that focused specifically on the ways that decision aids can support consumers on the Internet (e.g., [20]).

An emerging application area, related to this domain, is decision support for consumers <sup>b</sup>on the go<sup>Q</sup>, e.g., when they are actually inside a retail store. For example, one can envision decision support for consumers facing complex decisions in retail stores for, say, durable goods. In this context, decision support systems operate on the personal mobile devices of the consumers. Such in-store opportunities are emerging as a result of the combination of three trends: (1) the increased computing power of small devices such as mobile phones, (2) the increasingly more widespread adoption of these mobile devices by consumers, and (3) the increasing possibilities of the products themselves to reveal product description data over wireless networks. For example, a technology such as Radio Frequency Identification (RFID) allows products to be <sup>b</sup>smart-tagged<sup>Q</sup>, e.g., equipped with data that can be traced in a wireless network. When RFID chips are attached to durable goods, they can assist mobile devices in recognizing the products that are available in the store. Early prototypes within this new application domain include Accenture’s Pocket Bargainfinder and Shopper’s Eye [5].

The implementation of decision support systems in this area is subject to new development requirements. In particular, decision aids would be constrained by the small screen size that is inherent to mobile devices. Decision support for consumer brand evaluation is traditionally implemented using a decision matrix. The decision matrix contains all product alternatives in rows, and the attributes for each alternative are listed in colums. Decision support is then provided through functionality to screen and sort alternatives (e.g., [6,17]). In a small screen environment, however, this type of support is difficult if not impossible to implement: the decision matrix quickly becomes too large for the screen to display in full. Scrolling along the decision matrix, while conceivable, is unwieldy, and comparable to searching for directions on a map with a magnifying glass. Therefore, in order to effectively support consumers in the in-store context, new types of decision aids are needed that move away from the traditional decision matrix approach.

The research project described in this paper introduces a new type of decision support system that is applicable to this context. It was implemented on a mobile device, it scans products in a retail store and then displays an electronic <sup>b</sup>smart<sup>Q</sup> label. The label displays the values of the product attributes. Decision support is implemented by augmenting the electronic label with a product attractiveness cue. This paper describes the decision support system in more detail, and reports the results of a lab experiment in which the system was tested on its effectiveness.

## 2. Theoretical background

## 2.1. Consideration set

Consumer decision making is often conceptualized as a rational, linear process, consisting of a number of mental steps through which consumers proceed as they make their purchasing decisions (e.g., [2], p. 17; [4]). Central to this process is the concept of the consideration set. The consideration set is defined as those brands that the consumer considers seriously when making a purchase and/or consumption decision [7,9]. It is central to the shopping process because it is the outcome of the first stage of decision making, and the starting point of the next stage of decision making. In the first stage, consumers screen a number of products and qualify or disqualify them for further consideration. In the second stage, they take the resulting set of products and select the best product among them. Analytical and empirical evidence shows that the size of the consideration set is often small: sets consisting between two and five alternatives have been reported in the literature [15].

In forming the consideration set, decisions about the inclusion or exclusion of products (or, in other words, consideration set <sup>b</sup>membership<sup>Q</sup>) are required. They involve stepping through each alternative brand that is known to the consumer, as well as examining new products previously unknown [12]. Membership decisions are important because they have repercussions for the second stage. Consumers run the risk of including an inferior product in the consideration set, or excluding a superior product from the consideration set [16]. Their search for information about the alternatives is largely a result of the uncertainty about these risks [19].

Consumers in retail stores typically evaluate the attractiveness of durable products by locating them on the shelves and examining them in detail. This involves the study of the visual features of the product and the accompanying label which contains the nonvisual features. Carrying out this excercise allows them to decide if the product is worthy of further consideration.

## 2.2. Product attractiveness cue

The decision support system that is the focus of this paper was specifically developed to assist consumers in the development of their consideration set. The principal idea was to give consumers a cue about the attractiveness of a product on the shelves. This cue should be based on product attributes and personal preferences. Product attractiveness is defined here as the degree to which the product meets the personal preferences on a set of predefined product attributes (e.g., price). The decision support system should be able to provide a visual of these attributes, as well as a visual of the values for each attribute.

The attractiveness cue that was implemented on the prototype is based on the ranking of the product in comparison with competing brands that are available in the store. Each attribute value is given an ordinal rank and this rank was visualized using color shades. Nine shades of a single color (blue) were used to display the attractiveness rank to the user. Light shades corresponded to <sup>b</sup>good<sup>Q</sup> (high rank), dark shades corresponded to <sup>b</sup>poor<sup>Q</sup> (low rank). A summary rank was computed as a weighted average of the ordinal ranks of each attribute. The weightings were based on the personal preferences of the user. The summary rank was placed prominently at the bottom of the screen. It should be acknowledged that this is only a crude approximation of attractiveness because strictly speaking one cannot summate individual ranks.

Several considerations went into the design of the prototype. Color was used instead of, for example, the numerical representation, (i.e., the rank itself), because empirical evidence suggests that color acts as a quicker indication of good or bad than a numerical value [8]. Second, the number of color shades is small because people have trouble differentiating between large numbers of shades: the maximum number of visual or audio cues that people can meaningfully recognize is around seven plus or minus two [13].

## 2.3. Hypotheses

A research model provided the basis for the experiment that was conducted with the product attractiveness cue. The graphical respresentation of the research model is depicted in Fig. 1.

The dependent variable is consideration set quality. This is a generic performance measure that captures the risk of including inferior products and excluding superior products. Variance in quality is conceptualized as follows: quality is assumed to increase if the set contains more superior products and less inferior products. It is assumed to decrease if the set contains less superior products and more inferior products. Further details on the operationalization of superior and inferior products can be found in the method section.

![](/api/attachments/ABMRW5JS/fulltext/images/8f526e622c73593ba6a299a933131541dfd77831ff0db01fe94161a2ac646195.jpg)  
Fig. 1. Research model for experiment.

The rationale for the hypotheses below is grounded in behavioral decision making theory advanced by Payne and colleagues [10,14]. This theory posits that decision making is essentially a trade-off between cognitive effort and decision accuracy. Decision makers economize on effort at the expense of accuracy. This behavioral decision making approach is anything but new to decision support system researchers: it has been used in many other application domains as well, in particular in the domain of apartment selection problems [18]. For this reason the theory will not be described in more detail here.

The first hypothesis is that the availability of a product attractiveness cue will positively influence the quality of the consideration set. The purpose of the cue is to visualize the attractiveness of the product to the consumer. In theory, this color visualization should diminish the cognitive effort associated with the assessment of the attractiveness. Effort and accuracy are interrelated, in so far that the accuracy can potentially increase as the effort decreases. Although this is by no means an automatic process [18], with less mental effort consumers are able to more accurately decide whether a product is attractive or unattractive. Ultimately, this could result in relatively more superior and relatively less inferior brands in the consideration set. Evidence from other decision support experiments confirms that the use of color as a visual cue improves decision making performance [1]. The hypothesis therefore is that consumers with the product attractiveness cue will have a higher consideration set quality then consumers without the cue.

Hypothesis 1. The availability of the product attractiveness cue has a positive influence on the quality of the consideration set.

The second hypothesis concerns a potential moderator on the effect of the product attractiveness cue. It is conceivable that the added value of a decision support system increases as the decision becomes more complex [17]. A more complex decision places higher demands on the mental capacities of the decision maker. In theory, an opportunity to reduce mental effort should therefore be more welcome to the decision maker in the case of more complex decisions.

Typical operationalisations of decision complexity in the decision support system literature are the variation of the number of product alternatives and/or the number of product attributes [17]. For reasons of tractability, only the number of product alternatives have been varied. This is realistic because some retail stores have only a few number of products on display, and some have a large number of products. The hypothesis is that the product attractiveness cue is more helpful if the number of product alternatives is larger.

Hypothesis 2. A larger number of product alternatives positively moderates the influence of the product attractiveness cue on consideration set quality.

## 3. Method

The experimental design was a between subject 2  2 factorial, with two treatments: (1) availability of the product attractiveness cue, and (2) number of product alternatives. The number of product alternatives that a participant could choose from in the shop was 10 in the low complexity treatment and 20 in the high complexity treatment. The participants were randomly assigned to each of the four cells.

## 3.1. Participants

86 undergraduate students of a Danish business school (48 male, 38 female, mean age = 22.1 years, S.D. = 2.95) took part in the experiment as part of a course requirement. To encourage involvement, one digital camera was awarded to a random participant at the end of the experiment. Participants signed an informed consent form in which they agreed to participate to the best of their ability.

## 3.2. Context

The application domain selected was a store containing digital cameras. The digital camera was chosen because the purchase decision is based on a number of competing product attributes and selecting one was a task that the participants could identify with. The artifical lab store contained visual displays of cameras, and each camera visual was accompanied by a barcode. The mobile device could retrieve data about the digital camera from the barcode, and display these data to the user. This way, users could inform themselves about the cameras and then select the one that best met their preferences.

## 3.3. System

The mobile device used was an iPaq H3850 Personal Digital Assistant (Hewlett Packard) with an SPS 3000 barcode jacket (Symbol). The software was built by the author using Microsoft Windows Platform SDK for PocketPC 2002, Symbol Windows CE SDK, and Embedded Visual Basic 3.0 (Microsoft). Fig. 2 displays screenshots of the two versions of the information system, the first version without the product attractiveness cue, and the second version with the product attractiveness cue.

## 3.4. Dependent variable measures

The cameras had five attributes each. To be able to measure consideration set quality, a decision matrix similar to the one contained in [6] was created. The matrix is divided into five brand categories, with 2 or 4 alternatives per category, depending on the treatment. One alternative in each brand category is constructed such that no matter what the preferences were, this product was always better on all attributes than the others in its brand category. In multi-attribute decision making, this product is said to dominate the others. Across brands however, these brands did not dominate each other. Therefore, these products are the so-called non-dominated, or <sup>b</sup>superior<sup>Q</sup> alternatives. All alternatives that were dominated by other alternatives are <sup>b</sup>inferior<sup>Q</sup> products. The Appendix lists the values and attributes for each alternative. All five nondominated alternatives were available in each task complexity treatment: in the low treatment they were supplemented with five inferior products, and in the high treatment by fifteen inferior products.

![](/api/attachments/ABMRW5JS/fulltext/images/747e3cc67bca09bb454bf61e927689d29ddf15b0b326af041fc38451f4513247.jpg)  
Fig. 2. Screenshots of the two treatments. The first is without product attractiveness cue, the second with product attractiveness cue.

## 3.5. Procedure

Participants conducted the experimental task one at a time. After entering the lab store, the participant was given written instructions about the experiment. The participant then signed the informed consent form, and filled out a pre-experiment survey. This survey included a scheme where participants could fill in their personal preferences on the five camera attributes. During the briefing, all participants were informed of the polar values of each attribute, so that, at least theoretically, also the participants in the control groups were able to compute the ordinal ranks.

Before beginning the actual task of selecting a camera, the participant was shown how to work the mobile device. After the participant had successfully tried the device and expressed readiness to proceed, the actual purchase selection task started. The participants were told that there were no constraints on how many times they could scan a camera. A special consideration set table was provided so that participants could move cameras between the store and this table if they deemed the camera worthy of further consideration. As the participant proceeded in the experiment, all cameras that were put down on the consideration set table were recorded. On average, the actual decision making time was 7.02 min (S.D. = 3.20 min).

## 4. Results

As a manipulation check, we examined whether the participants had actually benefited from the decision aid. In the post-questionnaire we asked them to score the ease of assessing the attractiveness of the cameras, on a single-item 7-point scale ranging from <sup>b</sup>very difficult<sup>Q</sup> to <sup>b</sup>very easy.<sup>Q</sup> Table 1 displays the results.

The manipulation check was conducted by carrying out a two-way Analysis of Variance on perceived ease of assessing alternatives. The main effect of the product attractiveness cue was significant ( F = 7.01, $p { = } 0 . 0 1 0 )$ . There was no main effect of the number of alternatives, but there was an interaction effect ( F = 5.44, p = 0.022), suggesting that the perceived ease improved as the number of alternatives increased. Hence, the attractiveness cue is an appropriate decision aid manipulation, i.e., it succesfully decreased the mental effort associated with assessing attractiveness.

Table 1 further presents the means and standard deviations of the key dependent variables under study. To test the hypotheses, a two-way Multivariate Analysis of Variance (MANOVA) was used, with the number of non-dominated alternatives (superior products) and the number of dominated alternatives (inferior products) as the dependent variables. The two variables were significantly correlated (Pearson r = 0.24, p = 0.024). MANOVA assumes among other things that the dependent variables are normally distributed and that covariances and error variances are equal across groups. The frequency distributions, however, were skewed and these assumptions were not met. To correct for distortions that may occur because the distributions are asymmetrical and nonnormal, methodologists then suggest adopting at least a more stringent significant level than the typical $\begin{array} { r } { \alpha = 0 . 0 5 . } \end{array}$ , for example to $\alpha { = } 0 . 0 2 5$ ([11], p. 107). Table 2 presents the results of the MANOVA.

Mean perceived ease of assessing attractiveness, number of superior and inferior products in consideration set for attractiveness cues conditions as a function of the number of alternatives to choose from (N =86)

<table><tr><td rowspan="2"></td><td colspan="2">Attractiveness cue unavailable</td><td colspan="2">Attractiveness cue available</td></tr><tr><td>M</td><td>S.D.</td><td>M</td><td>S.D.</td></tr><tr><td colspan="5">Perceived ease of assessing alternative attractiveness</td></tr><tr><td>10 alternatives</td><td>5.6</td><td>1.2</td><td>5.7</td><td>1.1</td></tr><tr><td>20 alternatives</td><td>4.9</td><td>1.4</td><td>6.1</td><td>0.8</td></tr><tr><td colspan="5">Number of superior products in consideration set</td></tr><tr><td>10 alternatives</td><td>3.7</td><td>1.2</td><td>4.2</td><td>0.8</td></tr><tr><td>20 alternatives</td><td>3.9</td><td>1.4</td><td>4.5</td><td>0.9</td></tr><tr><td colspan="5">Number of inferior products in consideration set</td></tr><tr><td>10 alternatives</td><td>0.4</td><td>0.7</td><td>0.1</td><td>0.4</td></tr><tr><td>20 alternatives</td><td>2.1</td><td>1.7</td><td>1.6</td><td>1.4</td></tr></table>

Table 2  
Multivariate and univariate analyses of variance of number of superior and number of inferior products

<table><tr><td rowspan="3">Source</td><td rowspan="2" colspan="2">Multivariate</td><td colspan="4">Univariate</td></tr><tr><td colspan="2">Superior products</td><td colspan="2">Inferior products</td></tr><tr><td>F</td><td>p</td><td>F</td><td>p</td><td>F</td><td>p</td></tr><tr><td>Attractiveness cue (A)</td><td>5.04</td><td>0.009</td><td>5.36</td><td>0.023</td><td>2.16</td><td>0.146</td></tr><tr><td>Number of Alternatives (N)</td><td>21.03</td><td>0.000</td><td>0.92</td><td>0.340</td><td>41.81</td><td>0.000</td></tr><tr><td>A × N</td><td>0.19</td><td>0.827</td><td>0.00</td><td>0.982</td><td>0.34</td><td>0.557</td></tr></table>

Note: multivariate F ratios were generated from Pillai’s statistic.

Table 2 demonstrates that the attractiveness cue significantly increased the number of superior products in the consideration set, and neither increased nor decreased the number of inferior products. Hypothesis 1 is therefore supported. These effects are not significantly moderated by an increase in the number of available products. Hypothesis 2 is therefore rejected.

Table 2 also demonstrates that the number of inferior products in the consideration set is significantly larger in the case of 20 alternatives than in the case of 10 alternatives. By design, the high complexity treatment added 10 inferior products and did not add any superior products. This finding is therefore not completely surprising: we can expect people to consider more inferior products if we increase the number of available inferior products.

Effect sizes were computed using partial $\eta ^ { 2 } .$ . For the number of superior products, the effect size for the Attractiveness Cue was 0.06 (a moderate effect) and for Number of Alternatives 0.01 (a small effect; cf. [3]). For the number of inferior products, the effect sizes were 0.03 (a small effect) and 0.34 (a large effect) respectively.

## 5. Discussion

On the basis of the results, the conclusion of this research project is that the product attractiveness cue was effective in improving the consideration set quality of the participants. In this experiment, the added value of the decision support system is unqualified by the number of alternatives, e.g., this effect is stable across the 10 alternatives treatment and the 20 alternatives treatment.

The results of this study point towards the usefulness of <sup>b</sup>feeding<sup>Q</sup> consumers with information as they move around the shop. The results also imply that we can provide the shopper with decision support, in a manner that is not too closely tied to the traditional decision matrix approach. Therefore, it seems fruitful to examine the ways in which we can expand on the approach followed in this paper. A number of possible opportunities for extending this work are listed below.

The attractiveness cue increased the number of superior alternatives but did not increase or decrease the number of inferior alternatives. Perhaps, in developing the decision aid, too much attention was paid to assessing the attractiveness of products rather than assessing their unattractiveness. If the decision aid would zoom in on the <sup>b</sup>estimated unattractiveness<sup>Q</sup> of products, then perhaps the number of inferior alternatives in the consideration set would decrease while the number of superior alternatives would remain constant. This is intriguing because such a remarkable effect on consumer decisions would require only a slight modification of the user interface. A future research project would be interesting in which the effect of attractiveness or unattractiveness focus on consideration set quality is studied.

From a technical point of view, there is still some way to go before we will see an application such as this in widespread use. For example, the prototype system stored all product and preference data on the stand-alone device. This would not be feasible in a real-world implementation. A production-ready system would have to connect to a wireless network to retrieve such product data and to update preference data. A technical architecture has yet to be designed to allow the prototype to be scalable, and such an architecture will likely include the use of distributed database servers (for products and product preferences), and the use of long and short-range wireless connections to access them.

Another interesting venue, both for practitioners and researchers, is to study the effects of different types of sensory cues. Examples include audio-based or text-based cues. If we use cues that are not visual, we can implement these types of decision support systems on small devices that do not necessarily have to resemble Personal Digital Assistants. For example, we could implement trembling cues on mobile phones (as most of them have trembling functionality when in silent mode), or we could implement audio cues on portable music players. A future research project would be interesting in which the effects of different sensory cues are studied on these devices.

To appreciate the findings of this study, the reader should recognize the limits of the experimental design. Experimental designs trade internal validity for external validity, and therefore, the results are affected by external validity threats—much like other experimental research. Claims that undergraduate business students are representative for larger populations of shoppers are questionable at best. Consequently, this project does not allow us to infer general statements about the average high street shopper. To generalise these findings it would be relevant to replicate the experiment on a probabilistic sample of retail shoppers.

We are moving quickly into an era where <sup>b</sup>smarttagging<sup>Q</sup> of products becomes increasingly widespread. The information that becomes available for consumers <sup>d</sup>on the go<sup>T</sup> increases in direct proportion to this development. Consequently, it is relevant to embark on more research on the way mobile users can effectively handle this information, and on the degree to which decision support systems can function in this new context. This project attempted to offer a first step in that direction.

## Acknowledgements

This experiment was conducted when the author was a visiting associate professor of information systems at the Copenhagen Business School. The author would like to thank Lotte Sangstad Sørensen for her assistance during the experiment and the department of Informatics at the Copenhagen Business School for the financial support of this research.

## Appendix A. Decision matrix used in experiment

Brand names were partly derived from public consumer reports, all other values are fictitious. Alternatives were randomly assigned to a shelf ID and attributes were randomly assigned to display order on the device, except for price which was always last. Superior products are displayed in italics.

<table><tr><td>Shelf ID</td><td>Brand</td><td>Resolution</td><td>Photo capacity</td><td>Digital zoom</td><td>Weight (g)</td><td>Price (in DKK)</td><td>Included in 10 alt. treatment</td></tr><tr><td>1</td><td>AGFA ePhoto CL45</td><td> $1280 \times 1048$ </td><td>64</td><td>3×</td><td>184</td><td>1900</td><td></td></tr><tr><td>2</td><td>AGFA ePhoto CL50</td><td> $640 \times 480$ </td><td>66</td><td>2.5×</td><td>188</td><td>1975</td><td></td></tr><tr><td>3</td><td>Sony DSC-P20</td><td> $2400 \times 1800$ </td><td>60</td><td>3×</td><td>176</td><td>2200</td><td></td></tr><tr><td>4</td><td>AGFA ePhoto CL60</td><td> $2400 \times 1800$ </td><td>62</td><td>2×</td><td>180</td><td>1825</td><td>x</td></tr><tr><td>5</td><td>Sony DSC-P50</td><td> $640 \times 480$ </td><td>56</td><td>2.5×</td><td>168</td><td>2050</td><td>x</td></tr><tr><td>6</td><td>Panasonic PV-DC 2500</td><td> $2400 \times 1800$ </td><td>64</td><td>2.5×</td><td>184</td><td>1900</td><td></td></tr><tr><td>7</td><td>Kodak DC 225</td><td> $640 \times 480$ </td><td>58</td><td>2.5×</td><td>172</td><td>2125</td><td></td></tr><tr><td>8</td><td>Toshiba PDR M-63</td><td> $2400 \times 1800$ </td><td>70</td><td>3×</td><td>156</td><td>1750</td><td>x</td></tr><tr><td>9</td><td>Kodak DC 215</td><td> $2400 \times 1800$ </td><td>60</td><td>3×</td><td>176</td><td>2200</td><td>x</td></tr><tr><td>10</td><td>AGFA ePhoto CL55</td><td> $2400 \times 1800$ </td><td>72</td><td>3×</td><td>160</td><td>1750</td><td>x</td></tr><tr><td>11</td><td>Panasonic PV-DC 1500</td><td> $2400 \times 1800$ </td><td>68</td><td>3×</td><td>160</td><td>1600</td><td>x</td></tr><tr><td>12</td><td>Toshiba PDR M-62</td><td> $640 \times 480$ </td><td>64</td><td>2×</td><td>184</td><td>1900</td><td>x</td></tr><tr><td>13</td><td>Sony DSC-P30</td><td> $2400 \times 1800$ </td><td>72</td><td>3×</td><td>164</td><td>1675</td><td>x</td></tr><tr><td>14</td><td>Panasonic PV-DC 2000</td><td> $1280 \times 1048$ </td><td>66</td><td>2×</td><td>188</td><td>1975</td><td>x</td></tr><tr><td>15</td><td>Kodak DC 230</td><td> $1280 \times 1048$ </td><td>56</td><td>2×</td><td>168</td><td>2050</td><td></td></tr><tr><td>16</td><td>Kodak DC 220</td><td> $2400 \times 1800$ </td><td>70</td><td>3×</td><td>164</td><td>1600</td><td>x</td></tr><tr><td>17</td><td>Sony DSC-P40</td><td> $1280 \times 1048$ </td><td>58</td><td>2×</td><td>172</td><td>2125</td><td></td></tr><tr><td>18</td><td>Toshiba PDR M-61</td><td> $1280 \times 1048$ </td><td>66</td><td>2.5×</td><td>188</td><td>1975</td><td></td></tr><tr><td>19</td><td>Panasonic PV-DC 3000</td><td> $640 \times 480$ </td><td>62</td><td>3×</td><td>180</td><td>1825</td><td></td></tr><tr><td>20</td><td>Toshiba PDR M-60</td><td> $2400 \times 1800$ </td><td>62</td><td>3×</td><td>180</td><td>1825</td><td></td></tr></table>

## References

[1] I. Benbasat, A.S. Dexter, An experimental evaluation of graphical and color-enhanced information presentation, Management Science 31 (11) (1985) 1348 – 1364.

[2] J.R. Bettman, An Information Processing Theory of Consumer Choice, Addison-Wesley, Reading, MA, 1979.

[3] J. Cohen, Statistical Power Analysis for the Behavioral Sciences, Lawrence Erlbaum, Hillsdale, NJ, 1988.

[4] J.F. Engel, R.D. Blackwell, P.W. Miniard, Consumer Behavior, Dryden Press, Dryden, Forth Worth, 1995.

[5] A.E. Fano, Shopper’s eye: using location-based filtering for a shopping agent in the physical world, Proceedings of the Second International Conference on Autonomous Agents, 1998.

[6] G. Haubl, V. Trifts, Consumer decision making in online shopping environments: the effects of interactive decision aids, Marketing Science 19 (1) (2000) 4 – 21.

[7] J.R. Hauser, B. Wernerfelt, An evaluation cost model of consideration sets, Journal of Consumer Research 16 (1990 March) 393– 408.

[8] E. Hoadley, Investigating the effects of color, Communications of the ACM 33 (2) (1990) 120 – 125.

[9] J.A. Howard, J.N. Sheth, The Theory of Buyer Behavior, Wiley, New York, 1969.

[10] E.J. Johnson, J.W. Payne, Effort and accuracy in choice, Management Science 31 (4) (1985) 395– 414.

[11] G. Keppel, Design and Analysis: a Researcher’s Handbook, Prentice Hall, Upper Saddle River, NJ, 1991.

[12] D.R. Lehmann, Y. Pan, Context effects, new brand entry, and consideration sets, Journal of Marketing Research 31 (3) (1994) 364–374.

[13] G.A. Miller, The magical number seven, plus or minus two: some limits on our capacity for processing information, Psychological Review 63 (1956) 81– 97.

[14] J.W. Payne, J. Bettman, E.J. Johnson, The Adaptive Decision Maker, Cambridge University Press, New York, 1993.

[15] J. Roberts, A grounded model of consideration set size and composition, Advances in Consumer Research (16) (1989) 749– 757.

[16] A.D. Shocker, M. Ben-Akiva, B. Boccara, P. Nedungadi, Consideration set influences on consumer decision making and choice: issues, models, and suggestions, Marketing Letters 2 (1) (1991) 181–197.

[17] P. Todd, I. Benbasat, The use of information in decison making: an experimental investigation of the impact of computer-based decision aids, MIS Quarterly (1992 September) 373– 393.

[18] P. Todd, I. Benbasat, Evaluating the impact of DSS, cognitive effort, and incentives on strategy selection, Information Systems Research 10 (4) (1999) 356– 374.

[19] J.E. Urbany, P.R. Dickson, W.L. Wilkie, Buyer uncertainty and information search, Journal of Consumer Research 16 (1989) 208– 215.

[20] S.-T. Yuan, A personalized and integrative comparion-shopping engine and its applications, Decision Support Systems 34 (2002) 139– 156.

Hans van der Heijden is a senior lecturer of information systems at the University of Surrey, United Kingdom. He holds a Ph.D. in management information systems from Erasmus University, Netherlands. Currently he serves as an associate editor for the European Journal of Information Systems. Dr. van der Heijden has an interest in user acceptance of information systems and the application of online research methods to information systems research. His publications have appeared in MIS Quarterly, European Journal of Information Systems, Information and Management, and Journal of Information Technology.
