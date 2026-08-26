---
otero_id: 21001
otero_key: "Y3ZT6BDR"
title: "AdPalette: an algorithm for customizing online advertisements on the fly"
authors: "Gilbert G. Karuga; Andriy M. Khraban; Suresh K. Nair; Daniel O. Rice"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(01)00104-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# AdPalette: an algorithm for customizing online advertisements on the fly

Gilbert G. Karuga, Andriy M. Khraban, Suresh K. Nair <sup>)</sup>, Daniel O. Rice

School of Business Administration, UniÕersity of Connecticut, 368 Fairfield Road, U-41IM, Storrs, CT 06269-2041, USA

## Abstract

In this paper, we address customization and dynamic optimization of online advertisements. For online ads that attract click-throughs, we use click through rates to develop a methodology for customizing advertisements on the fly by changing content, copy, placement, animation and other attributes. We use techniques from optimization, conjoint analysis and genetic algorithms. Ads are reconstituted on the fly using graphic files for each level of each attribute, much like a painter would use a palette. We show that this approach improves response rates, reduces server storage requirements and improves ad efficiency. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Online advertisements; Optimization; Ad efficiency; conjoint analysis

## 1. Introduction

The Internet age has shifted the focus of advertising from traditional media, such as newspaper, radio, and television, to new AonlineB mediums such as web advertisement and electronic mail. In the past few years, marketers have begun to realize the significance of the Internet as an effective tool to implement direct marketing. However, only recently have marketers begun to consider using the technological capabilities of the Internet to target consumers more completely for direct marketing. Some of the most successful companies, such as DoubleClick, AdSmart and Flycast, have incorporated customer profiling to improve direct marketing efforts over the Internet 1 . The technology being used to accom- <sup>w</sup> <sup>x</sup> plish this is on the cutting edge of web interconnectivity. In this paper, we present a method to improve the effectiveness of online advertising. We call this method AdPalette. AdPalette uses elements of conjoint analysis, goal programming and genetic algorithms to generate dynamic online advertisements. The AdPalette algorithm combines the advertisement attribute levels i.e., characteristics of ads such asŽ size and color and produces the best advertisements. based on consumer feedback from click-throughs. The implementation of AdPalette takes full advantage of state of the art web technology and develops a superior online marketing technique that improves advertising effectiveness.

While we primarily take an information technology approach to the optimization of online advertising, the concept of consumer marketing is a topic that has long been considered in an extensive body of marketing literature. We borrow some concepts about consumer preference theory from this literature and assume that individual consumers show preferences to products based on certain attributes or characteristics of these products. In our paper, advertisements are considered to be products, which possess certain attributes—ad layout, style, color, etc.

1.1. Marketing, consumer preference, and internet adÕertising

Specifically, consumer preference theory supports the notion that consumers’ tastes for products differ across individuals. Observed purchasing trends have a strong bearing on how well a product appeals to the desires of individual consumers 9 .<sup>w x</sup>

In order to appeal to different tastes and preferences, marketers have designed mechanisms to reach individual consumers in unique ways that tailor the information content to the preferences of the target individual. A commonly observed technique of tar geting consumers with marketing information is direct marketing. In this technique, marketers identify the needs of consumers and prepare marketing information that has a higher chance of appealing to the consumer based on the consumers’ pre-identified preferences.

The problem from a marketing perspective has been one of narrowing the population to a target list that is most likely to respond to directed marketing <sup>w</sup> <sup>x</sup> 4 . However, it is important to note that the Internet changes the objective of direct marketing. The direct marketing challenge of identifying target consumers in mailing lists has been transformed into one of demarcating between individual user profiles and customizing marketing information that can be disseminated in mass media via the Internet. Heinen <sup>w</sup> <sup>x</sup> 10 discusses the dimensions that target marketing on the Internet will take. In this paper, he explores some of the ways that companies are, or will be, using the Internet to improve the marketing of their commercial businesses. Similarly, McCandless 13<sup>w</sup> <sup>x</sup> extends the idea of Internet based marketing and recognizes that the Internet has become very popular among companies because of its capabilities to promote direct customer feedback and quick-change strategies.

There are two essential elements to current direct marketing through the Internet: 1 determining the Ž . market segment; and 2 getting the right advertise-Ž . ment to the correct market segment. The Internet provides an easy way to obtain consumer information, which helps firms to determine consumer demographics, preference and value for products and services. This information is vitally important for firms conducting business on the Internet and firms are willing to pay for this information. Regularly firms offer AfreebiesB in exchange for the consumer information or purchase the information from information intermediaries who compensate consumers for this information 6 . The initial attempts at using<sup>w</sup> <sup>x</sup> the Internet for direct marketing had focused on the development of Decision Support Systems DSS forŽ . supporting the development of marketing strategies. O’Keefe and McEachern 15 look at Customer Decision Support Systems CDSS . This DSS is aŽ . web-based marketing model that establishes a link between a firm and its customers and additionally provides assistance in the decision-making process. More recently, the Internet has strengthened its role as an efficient channel for the collection and transmission of marketing information. Furthermore, an increase in competitive pressures coupled with advances in information collection and processing technologies and the need for scientific decision making has changed the concept of marketing research significantly 12 .<sup>w</sup> <sup>x</sup>

There remains a rather vague area in the literature, and this is the development of accurate models that may be used for identifying and targeting customers on the Internet. Existing literature does present a discussion of the possibilities of achieving some significant gains from using media to deliver information in form of advertisement to consumers in the target market and various issues surrounding such initiatives. However, the application of such an initiative has not been sufficiently considered, perhaps because the technology required for implementation of such initiatives did not previously exist 15 .<sup>w</sup> <sup>x</sup>

Web advertising has become very popular among companies due to its capability to generate direct customer feedback and information that businesses can use to change marketing strategies quickly. The Web also promotes personalized ads and other advertising opportunities. However, the full potential of Web advertising has yet to be realized. Some reasons that businesses have been unable to rapidly realize the full potential of Web advertising are that the Internet has been limited by traffic problems, bandwidth concerns and self-sufficiency issues 13 . <sup>w</sup> <sup>x</sup>

Table 1 Taxonomy of the current Web advertisement serving software capabilities

<table><tr><td rowspan="3">Software</td><td colspan="7">Targeting</td><td colspan="6">Scheduling</td></tr><tr><td colspan="3">Personal Profile</td><td rowspan="2">IP/Cookie</td><td rowspan="2">Geographic</td><td rowspan="2">Content</td><td rowspan="2">Searches</td><td colspan="3">Rotation</td><td colspan="3">Creative Rotation</td></tr><tr><td>Registration</td><td>Web Data</td><td>Other Data</td><td>Total number</td><td>Time Erames</td><td>Impression goal</td><td>Percentage</td><td>Frequency</td><td>Sequence</td></tr><tr><td>Accipiter AdManager 4.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ActiveTrack</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Ad Force</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Ad Juggler</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AdGenie</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AdKnowledge</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AdMan 1.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AdMaximize</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AdServer</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Banager</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>DAD</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>L90adMonitor</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Open AdStream</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>OrbitCycle</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Random Image Displayer</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Select Cast</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SpinBox</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>WebAdverts</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Legend: B; Present I; Absent  
Table References: http:<sup>rr</sup>adres.internet.com<sup>r</sup>software<sup>r</sup>management<sup>r</sup>0,1401,,00.html; http:<sup>rr</sup>www.engagetech.com; http:<sup>rr</sup>www. thethinkingmedia.com; http:<sup>rr</sup>www.adjuggler.com; http:<sup>rr</sup>www.ahg.com; http:<sup>rr</sup>www.adknowledge.com; http:<sup>rr</sup>www.medius.net; http:<sup>rr</sup>www.admaximize.com; http:<sup>rr</sup>www.sklar.com<sup>r</sup>dad<sup>r</sup>full-paper.html; http:<sup>rr</sup>www.l90admonitor.com; http:<sup>rr</sup>www.realmedia. com; http:<sup>rr</sup>www.orbitcycle.com; http:<sup>rr</sup>awsd.com<sup>r</sup>scripts<sup>r</sup>; http:<sup>rr</sup>www.spinbox.com; http:<sup>rr</sup>www.worldwidemart.com<sup>r</sup> scripts<sup>r</sup>image.shtml; http:<sup>rr</sup>www.banager.com; http:<sup>rr</sup>www.netgravity.com.

However, it may also be due to other inherent problems in the marketing strategies themselves.

## 1.2. Web-based adÕertising technologies— state of the art

The proliferation of online advertising firms and products that they offer is staggering. Online advertising firms have been very responsive to the increased popularity of the web. Consequently, there are numerous online advertising software products Ž . ad-serving software available on the market designed to improve the delivery of advertisements to the consumer. Due to the number of ad-serving software products available, we have selected a few representative products to illustrate common features and demonstrate the diversity among products. Table 1 below lists some of these products and provides an overview of the existing ad management industry practices and software capabilities based on publicly available information. For a more extensive description of these software products, refer to the Appendix A. One example of a product that is discussed in the literature is SelectCast developed by Aptex Software of San Diego. This software application is used to target individual customers in Internet advertising. SelectCast can generate advertising profiles that indicate what types of users tend to click on particular ads. The application does not depend on personal registration data. The program uses neural network technology software thatŽ AlearnsB on its own and relies on the same kind of pattern-match-. ing technology used in detecting credit-card fraud <sup>w</sup> <sup>x</sup> 16 . Please note that some products, such as Select-Cast, are very sophisticated and have multiple features while others are less complex and more downto-earth. Most of them share a somewhat standard selection of features and several of them have patented special techniques that they have developed.

Broadly, the software available employs three major techniques for advertising on the web. These are:

1. advertisement targeting,

2. advertisement scheduling,

3. creative banner rotation.

We will discuss these in turn.

Ž . 1 Advertisement targeting: AAd targetingB is a common feature in most ad-serving software programs. Based on data collected from one or several of information sources listed, ad-serving software performs a consumer targeting routine please note:Ž we cannot independently confirm whether web companies actually do what they claim :.

<sup>Ø</sup> visitor profiles gathered from site registration Ž . age, gender, income, business data, etc. ;

<sup>Ø</sup> area of content a visitor is viewing startingŽ with the first visit, systems automatically start learning about each site visitor’s individual interests and tastes, they keep learning more with each repeat visit ;.

<sup>Ø</sup> Internet-based registration domain type, Ž browser type, ISP, platform, time of day, day of the week ;.

<sup>Ø</sup> key-word or key-phrase searches;

<sup>Ø</sup> demographic data IP address, high-level andŽ specific domain ;.

<sup>Ø</sup> geographic data country, state, zip code, area Ž code ;.

<sup>Ø</sup> IP address and cookie information for ad or page;

<sup>Ø</sup> cumulative history of exposures to all ads in a campaign.

Companies have been applying the data collected by on-line marketing firms. This has given some firms valuable insight into consumer preference. Moreover, this information enables ad-serving firms to serve advertisements that are more likely to meet the needs and desires of online consumers.

Ž . 2 Advertisement scheduling: Advertisement scheduling, i.e., timing of display on web sites, is based on site monitoring data and objectives of scheduling, including:

<sup>Ø</sup> the total number of impressions or clicks theŽ . Ž ads automatically expire after specified number of days or impressions or click-throughs ;.

<sup>Ø</sup> specific time window requirements;

<sup>Ø</sup> guaranteed click counts;

<sup>Ø</sup> the number of impressions goal;

<sup>Ø</sup> combination of counts and date ranges;

<sup>Ø</sup> controlled frequency of ad delivery;

<sup>Ø</sup> AevenB impression distribution;

<sup>Ø</sup> banner AweightingB Žhow frequently a banner should be displayed compared to other banners ..

Ž . 3 Creative banner rotation: Banner rotation deals with cycling through a set of ads based on some criteria. These include one or more of the following:

<sup>Ø</sup> percentages fractions of time a particular adŽ . will be displayed as a part of an advertising campaign;

<sup>Ø</sup> frequency of displaying an ad;

<sup>Ø</sup> rotating a set of ads based on a pre-specified sequence.

Most providers of ad management software claim to optimize the ad stream. Their software products break down the large sites into AzonesB, or areas, in a process that they loosely call Aad targeting.B These software products appear to support multiple banner pools for each page, linking companion banners so that they can show the banners in some particular order while excluding competing advertisers’ messages on the same page. They also appear to compensate automatically for low levels of information about new visitors to the site, and to dynamically adjust levels of information about each visitor’s interests and tastes 18 . These are the prevailing tricks<sup>w</sup> <sup>x</sup> used to Aeffectively manageB banner ads.

About 70% of the available ad software packages automatically generate up-to-the-minute, customized reports. They Adetail how many impressions and clicks were generated both from the entire site and by each ad and advertiser, or how much revenue was generated on any day, week, month, year, or in any period specified 2 . <sup>w</sup> <sup>x</sup> B Some companies are particularly ingenious in their search for higher performance. For instance, ActivTrack from ThinkingŽ Media uses a client-side tracking method, which . Aplaces a small Java applet about 0.5 KB into an ad Ž . or page. The applet acts like a ‘radio transmitter.’ As soon as the ad or page loads into a browser, this transmitter starts sending real-time data on where the ad is running and how surfers are interacting with it back to the ActiveTrack database . . . B <sup>w</sup> <sup>x</sup> 2 .

## 2. Motivation

This research sets forth to establish a way to alter the contents and appearance of an advertisement dynamically through the Internet by incorporating user preferences. These user preferences are captured and stored using currently available technology.

In a few short years, Internet advertising has become a viable means to communicate marketing messages to the consumer. There have been many improvements in the delivery of the advertisements; of which, the most striking is the change in philosophy from mass advertising to mass customized advertising that is better aimed at the individual consumer. Technology has enabled the concept of mass customized advertising, so specific advertisements are directed to individual consumers. Simply posting banner advertisements on the web may no longer be adequate to advertise over the Internet 11 . Increas-<sup>w</sup> <sup>x</sup> ingly, Internet consumers are bombarded with Internet advertisements such as banner advertisements and even AspamB e-mail. One has to be creative to attract attention from potential customers. Online advertising effectiveness studies have shown that as the use of online advertising has rapidly increased, the effectiveness of online ads has steadily decreased. Furthermore, often over the life of a banner advertisement, there is a steady decrease in consumer click-through rates CTR , which has been blamed Ž . on a phenomenon called Abanner burn-outB <sup>w</sup> <sup>x</sup> 5 . CTRs are commonly used to measure the effectiveness of banner advertisements and correspond to the number of times a banner is actually clicked on over a period of time. Click-through is a very tangible way to measure the impression of an online banner advertisement. In fact, some ad serving companies, such as TechnoSurf and e-ads, actually charge on a AperclickB basis 1 .<sup>w</sup> <sup>x</sup>

Our survey of current online advertising methods Ž . see Table 1 indicates that many firms directly target consumers, strategically place online advertisements, and even optimize the rotation of banners based on CTRs. However, we found no evidence of ad-serving firms that are dynamically optimizing banner advertisement effectiveness by changing the appearance or content of the banner to match the consumer audience. Our method, which we call Ad-Palette, involves dynamically creating online advertisements given various attributes and levels in such a manner that the best advertisement is created for the online consumer. AdPalette will allow the advertising firm to target consumers by combining the Abest of the bestB attributes of advertisements dynamically. This method enables variation of advertisement attributes, not only content but also such attributes as location, size, style, and even color. The Abest of the bestB concept will allow us to pick the best combination of advertisement attributes from potentially millions of possible combinations. Furthermore, AdPalette eliminates the need for storing large Aad librariesB, as the total advertisements are dynamically generated and only the attribute levels Ž . pieces need to be stored.

Our approach is different from the design of experiments based method proposed by Raghu et al. <sup>w</sup> <sup>x</sup> 17 elsewhere in this issue. In that approach, the focus is on determining the preference ordering between product offerings for each customer. Clusters are then formed with similar customers and customized products are designed for each cluster per-Ž haps using the median customer in each cluster . Our. approach on the other hand uses responses to ads at the aggregate level as seen by click through rates, and does not analyze individual responses. Therefore, our approach can accommodate real time data from millions of viewers to redesign ads. However, our approach could use Raghu et al.’s 17 approach to generate the initial set of ads and then dynamically redesign these ads based on click-throughs. To that extent, we would consider these two methods complementary.

## 3. The AdPalette approach

We model each advertisement as a bundle of attribute-level combinations. Each advertisement has a number of attributes, such as back drop, text, special interest, promotion offer, color, size, shape, location, animation, etc. Each of the attributes may have a number of possible leÕels. For example, the attribute AlocationB may have levels Atop,B Abottom,B Aleft side,B Aright side,B etc. The attribute AanimationB may have levels such as Ano animation,B Ablinking,B Ascrolling,B etc. In marketing literature on product designs using conjoint analysis, a similar framework is used 8,9 . An advertisement is com-<sup>w</sup> <sup>x</sup> pletely defined when one level of each attribute is chosen.

Note that traditionally AcompleteB ads are cycled through online sites. We are proposing here a method of using attributes of the ads to reconstitute and customize ads in real time. Clearly, if there are a number of attribute-levels possible say eight at-Ž tributes each with four levels there will be too many. AcompleteB ads that are possible $( 4 ^ { 8 } = 6 5 5 3 6 )$ . It would be impractical to store all of these ads in the server. Our approach obviates the necessity to store all these ads on the server. We make the assumption that all combinations of attribute levels are feasible. In practice, this may not be true. For example, we cannot write using white text on a white background because the text would no longer be readable. If such a situation arises, we recommend simply removing that ad from the lineup.

We use actual response rates from ads already placed to determine the combinations of attribute levels that will result in the best response rate. We assume an additive model, wherein the sum of the contributions of the attribute-levels would be the total response rate to the ad. This is commonly used in conjoint analysis based product design in marketing. We determine the attribute-level contributions using a goal-programming model 7 that does a data<sup>w</sup> <sup>x</sup> fitting exercise much like linear regression, but by minimizing the absolute deviation rather than minimizing the squared deviations. Next, we used ideas from Genetic Algorithms GA to seed completelyŽ . new designs using the crossover and mutation operators used commonly in GA 3,14 . We do this so that<sup>w</sup> <sup>x</sup> the mix of ads considered is not stuck in some local optima.

## 3.1. The AdPalette algorithm

The AdPalette algorithm is as follows a schematicŽ is shown in Fig. 1 ..

Step 1 Initialization : Place<sup>w</sup> <sup>x</sup> N random online advertisements and note their response rates using click through data.

Step 2 Goal program : Solve a goal program <sup>w</sup> <sup>x</sup> Ž . explained later with these N ads and their response rates to determine the optimal attribute level contributions to response rates.

Step 3 Choose best ads : Use the attribute-level<sup>w</sup> <sup>x</sup> contributions to determine x best ads.

![](/api/attachments/Y3ZT6BDR/fulltext/images/6506b481c178165c5bebb6c96a734d5f267edf1767ccb8a0b2b176886d0e772d.jpg)  
Fig. 1. The AdPalette algorithm will update and process click-through data and select the most effective ad components attribute levels ,Ž . generate new ads, and pass the new ad to the ad server.

Step 4 Crossover : Randomly pick two of the<sup>w</sup> <sup>x</sup> N ads and perform single point crossover explained Ž later to obtain two new ads. Repeat. $y / 2$ times to obtain y new ads.

Step 5 Mutation : Randomly pick<sup>w</sup> <sup>x</sup> z of the N ads and perform mutation explained later to obtainŽ . z new ads. You now have a total of Ž . N<sup>q</sup>x<sup>q</sup>y<sup>q</sup>z ads.

Step 6 Ad placement : Place these<sup>w</sup> <sup>x</sup> Ž . x<sup>q</sup>y<sup>q</sup>z new online ads and note their response rates.

Step 7 Delete poor ads : Delete the<sup>w</sup> <sup>x</sup> Ž . x<sup>q</sup>y<sup>q</sup>z worst responding ads from the Ž . N<sup>q</sup>x<sup>q</sup>y<sup>q</sup>z ads to be left with N ads. Break ties arbitrarily. Go to Step 2.

The above algorithm is never-ending and would continuously rejuvenate the ads being used. The only reason to stop the algorithm would be when the parameters of the ad campaign change, for example when the attributes or levels change, or the season changes, etc.

## 3.2. The optimization model

The model we present is a goal programming optimization. It tries to figure out the best fit to response rates using attribute-level contributions. We first present the notation used in the model.

Suppose $v _ { i a l }$ is a 0 or 1 value which is set to 1 if advertisement i uses level l of attribute a, and 0 otherwise. Therefore an ad with three attributes and four levels each may be represented using the following $v _ { i a l }$ values: 1000, 0010, 1000. Notice that each attribute should have only one 1 and the rest should be 0.

The input data are the following.

$v _ { i a l }$ 1 if level l of attribute a is chosen in design of advertisement i, 0 otherwise

$r _ { i }$ the observed response rate for advertisement i

The variables are the following.

$x _ { a l }$ the contribution to response rate from using attribute a at level l

$S _ { i } ^ { + } , \ S _ { i } ^ { - }$ the positive and negative deviations from the actual response rate

The problem then is to find the values of $x _ { a l }$ that solves the following goal program.

Minimize

$$
\sum_ {i} S _ {i} ^ {+} + \sum_ {i} S _ {i} ^ {-}
$$

subject to

$$
\sum_ {a} \sum_ {l} v _ {i a l} x _ {a l} - S _ {i} ^ {+} + S _ {i} ^ {-} = r _ {i} \text {   for   each   } i
$$

$$
S _ {i} ^ {+}, S _ {i} ^ {-} \geq 0.
$$

The first constraint ensures that the sum of the contributions to the response rate from ads already placed is equal to the observed response rate, and if not, the deviation in taken up by the positive and negative deviation variable. Since these deviations are being minimized in the objective function, at least one of them will be zero in the solution.

The solution of the optimization gives the attribute-level contributions to response rates. We can then predict the response rate from any ad by simply adding the contributions from the attribute-levels used in that particular ad. Therefore, it is straightforward to identify the ad, which will have the highest predicted response rate by simply using the attribute levels that have the maximum contributions. For example, if an ad has two attributes say color andŽ animation with three levels each say red, blue, . Ž green for color and no animation, blinking, and shimmer for animation , and the optimal contribu- . tions for each attribute-level are:

<table><tr><td>Attribute 1 (color)</td><td>0.2</td><td>1.5</td><td>2.4</td></tr><tr><td>Attribute 2 (animation)</td><td>1.3</td><td>1.8</td><td>0.6</td></tr></table>

Then the ad with the best-predicted response rate will have level 3 of attribute 1 green and level 2 ofŽ . attribute 2 blinking animation , with a predicted Ž . response rate of 4.2 i.e., 2.4Ž . <sup>q</sup> 1.8 .

In our algorithm, we recommend identifying not just the best, but the x best ads. This is also simple. We examine for each attribute the highest and next highest contribution. We then choose those levels that result in the minimum loss if moving to the next best level. In the above example, the second best ad would have the same level for attribute 1 but level 1 for attribute 2 the loss from moving from the best toŽ the next best level is only 0.5 in attribute 2, but 0.9 for attribute 1 ..

## 3.3. A FreshB ads using genetic algorithm operators

In order to ensure that the algorithm does not get stuck in a locally optimal solution because dramatically different ads have not been tried out, we use two genetic algorithm based operators to re-seed the ad lineup. These are the crossover and mutation operators.

## 3.3.1. CrossoÕer

Randomly pick two ads from the existing lineup. Randomly pick a number from 1 to a Žthe number of attributes , say. i. Switch the attribute levels between the two ads up to and including i. Suppose there are three attributes each with four levels. Suppose the following two ads are chosen at random.

<table><tr><td>Ad 1</td><td>1000</td><td>0010</td><td>1000</td></tr><tr><td>Ad 2</td><td>0100</td><td>0001</td><td>0100</td></tr></table>

Suppose we pick a random number from 1 to 3, and let us say it turns out to be 2. Then the crossed over new ads will be as follows.

<table><tr><td>New Ad 1</td><td>0100</td><td>0001</td><td>1000</td></tr><tr><td>New Ad 2</td><td>1000</td><td>0010</td><td>0100</td></tr></table>

This is called single point crossover. In another approach, called uniform crossover, a set of attributes is randomly chosen say 50% of the at- Ž tributes , and the crossover takes place only in these. attributes. For example, in the above example, if the second attribute is randomly chosen for uniform crossover, the resulting ads would be as follows.

<table><tr><td>New Ad 1</td><td>1000</td><td>0001</td><td>1000</td></tr><tr><td>New Ad 2</td><td>0100</td><td>0010</td><td>0100</td></tr></table>

In our algorithm, we recommend $y / 2$ such crossovers, resulting in y new ads.

## 3.3.2. Mutation

Randomly pick one ad from the existing line-up and randomly switch one of the levels of the ad from the chosen to not chosen or vice-versa. For example, suppose the ad that is randomly chosen is as follows. Ad 0001 1000 0010

We pick a random number from 1 to 12 the totalŽ number of attribute levels above . Let us say it is 7.. We then switch the seventh bit from 0 to 1, or vice versa. In order to ensure that there is only one 1 for that attribute, we switch the 1 in that attribute to 0. In our example,

New Ad 0001 0010 0010

In our algorithm, we recommend z such mutations.

## 3.4. The Õalues of N, x, y and z

The value of N determines the number of ads in the lineup. Its value has to depend on the application and infrastructure constraints, if any, on the number of ads that can be cycled easily by the server. By the ‘application’, we mean the number of attribute level combinations, the variance in response rates when the same attribute level combinations are re-used, etc. For example, N would be higher when the

Back Drops  
![](/api/attachments/Y3ZT6BDR/fulltext/images/b895384f0d799bf1160cbeac7e0ccabc256eb7beaaa8992d1f939c9b1f1c28d7.jpg)

A Vacation to Remember!!

Paradise on Earth!!

Isn't it time for a Vacation?

Do we have a vacation for you?

Fig. 2. Three attributes and with 5, 5 and 4 levels each for the Vacation Advertisement from the numerical example. Ž .

T<sub>a</sub>bl<sub>e</sub> 2  
The in<sub>p</sub>ut data desi<sub>g</sub>n of ads alread<sub>y p</sub>laced and their res<sub>p</sub>onse ratesŽ $v _ { i a l } , ~ r _ { i } )$ Ž and the out<sub>p</sub>ut from the o<sub>p</sub>timization contribution to res<sub>p</sub>onse rate<sub>,</sub> and the <sub>p</sub>ositive and ne<sub>g</sub>ative d<sub>ev</sub>i<sub>a</sub>ti<sub>ons</sub> $x _ { a l } , S ^ { + } , S ^ { - } )$

<table><tr><td rowspan="3"></td><td colspan="13">Attribute levels chosen,  $v_{ial}$ </td><td rowspan="2">Σ $Σv_{ial} x_{al}$ </td><td rowspan="3">Observed response rate,  $r_i$ </td><td rowspan="3">S+</td><td rowspan="3">S-</td><td rowspan="3">Total</td></tr><tr><td colspan="5">Back drop</td><td colspan="5">Text</td><td colspan="3">Special interest</td></tr><tr><td>Sunrise</td><td>Palms</td><td>Server</td><td>Food</td><td>Festival</td><td>Remember</td><td>Paradise</td><td>God&#x27;s</td><td>Time</td><td>Do we</td><td>Romantic</td><td>Students</td><td>Seniors</td><td>Family</td></tr><tr><td>Ad1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>Ad2</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>2.6</td><td>2.6</td><td>0</td><td>2.6</td></tr><tr><td>Ad3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>2.4</td><td>2.4</td><td>0</td><td>2.4</td></tr><tr><td>Ad4</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>2.6</td><td>2.6</td><td>0</td><td>2.6</td></tr><tr><td>Ad5</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>4.5</td><td>4.5</td><td>0</td><td>4.5</td></tr><tr><td>Ad6</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>2.8</td><td>2.8</td><td>0</td><td>2.8</td></tr><tr><td>Ad7</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>3.5</td><td>3.5</td><td>0</td><td>3.5</td></tr><tr><td>Ad8</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1.6</td><td>1.6</td><td>0</td><td>1.6</td></tr><tr><td>Ad9</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1.2</td><td>0.7</td><td>0</td><td>1.2</td></tr><tr><td>Ad10</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>2.5</td><td>2.5</td><td>0</td><td>2.5</td></tr><tr><td> $x_{al}$ </td><td>1.6</td><td>0</td><td>1</td><td>0</td><td>0.1</td><td>1</td><td>1.1</td><td>1.9</td><td>0</td><td>0</td><td>2.6</td><td>1.2</td><td>0</td><td>1.5</td><td>Σ</td><td>0.5</td><td></td><td></td></tr></table>

attribute level combinations are high. In general, we may want to have N set to at least the number of attribute level combinations, in order to avoid over fitting with sparse data. Where the variances are low, lower values of N may suffice.

From prior genetic algorithms research 3,14 , we<sup>w</sup> <sup>x</sup> would suggest an $x / y / z$ ratio of 10:10:1. And an $N / ( x + y + z )$ ratio of 75:25. Therefore, if N is 84, then $( x + y + z = 2 1 )$ , and we have $x = 1 0 , \ y = 1 0 .$ and z<sup>s</sup>1. Thus, in this example, we will generate the 10 best ads from the optimization, add another 10 ads due to crossover, and add one ad using mutation. After using these 21 new ads and obtaining their response rates, we will then delete the 21 worst response rate ads.

We are working on further research that will explore the sensitivity of the overall effectiveness of the AdPalette algorithm to values of these parameters.

## 4. An illustrative example

We now illustrate our approach using a numerical example. Suppose we want to use online ads for a vacation destination. Suppose there are three attributes back drops, texts and special interests withŽ . levels as shown in Fig. 2.

We can generate 10 random ads from these three attributes by choosing various levels for each ad. These 10 random ads are shown in Table 2, where the levels chosen are noted. These ads are then displayed in the web pages and click-throughs noted, as also shown in Table 2. Fig. 3 illustrates the first three of these ads.

Suppose x<sup>s</sup>2, y<sup>s</sup>2 and z<sup>s</sup>1. Then, we choose the two best ads using the optimized attribute level contributions to response rate, as shown in Table 3. These are shown as ads 11 and 12. Next, we choose two ads from the existing lineup at random say AdsŽ 2 and 7 . We perform uniform crossover in a ran-. domly chosen attribute say attribute 1 . These resultŽ . in two new ads, Ads 13 and 14. Finally we randomly choose one ad for mutation say Ad 5 . We then Ž . switch a randomly chosen bit say attribute 2, level Ž 4 and change it from 0 to 1, giving our final new ad,. Ad 15. These operations are shown in Table 3, and the resulting five new ads are shown in Fig. 4.

We then use these five new ads and note their predicted response rates, as shown in Table 3. Using these predicted response rates are known, we delete the five worst ads from the existing lineup of 15 ads Ž . 10 original and 5 new . We then run the optimization again on the 10 remaining ads, and repeat the process, as before, as shown in Table 4.

The optimization for this example was done using the Solver in Microsoft Excel. Any general-purpose solver may be used in production. The algorithm is very fast and takes a few seconds for real-size problems.

## 5. Evaluation of AdPalette

We next evaluate AdPalette to see how effective it is and to compare it with ad serving methods that are currently employed to deliver ads to consumers. Information about existing ad serving systems is limited due to the competitive nature of the industry; however, our survey of existing systems see SectionŽ 1.2 allows us to make some reasonable assumptions. about what firms currently use.

We simulate the serving of ads to consumers and employ four different approaches to serving the ads listed below. In the simulation there are 2000 viewers, each with randomly generated utility from aŽ uniform distribution for various attributes of an. advertisement. We compute the utility for an ad presented to a viewer by adding up the utilities for the attributes present in the ad. Initially, 50% of the simulated viewers are randomly assigned to be either on or off-line. Only viewers on-line can see the ads being served. A viewer clicks on an ad if his utility for the ad is at least 80% of the utility derived from his most preferred ad. The ads are created and served to these simulated viewers as described below for each method and are shown for a total of 10 sequential iterations.

![](/api/attachments/Y3ZT6BDR/fulltext/images/6eda60cc4ad4457c00f7eda9827dfb0de7b11d7de2075166a9c9bd5bebf5a7d9.jpg)  
Advertisement 1

![](/api/attachments/Y3ZT6BDR/fulltext/images/a9878d3beab66bff4174ae9ec66f8091dda09eb7df1b509e6e41af30d14c3cb2.jpg)  
Advertisement 2

![](/api/attachments/Y3ZT6BDR/fulltext/images/1ad04df5b47f3d87c517bac8e09c4cad0afc7ef0f47a1fc32f6476192973eb84.jpg)  
Advertisement 3  
Fig. 3. The first three of the 10 advertisements for the Vacation Advertisement from the numerical example. Ž .

T<sub>a</sub>bl<sub>e</sub> 3  
Th<sub>e</sub> fi<sub>ve new a</sub>d<sub>s a</sub>ft<sub>er op</sub>ti<sub>m</sub>i<sub>za</sub>ti<sub>on crossover an</sub>d <sub>mu</sub>t<sub>a</sub>ti<sub>on</sub>

<table><tr><td rowspan="3"></td><td colspan="14">Attribute levels chosen,  $v_{ial}$ </td><td rowspan="3">Predicted response rate,  $r_i$ </td></tr><tr><td colspan="5">Back drop</td><td colspan="5">Text</td><td colspan="4">Special interest</td></tr><tr><td>Sunrise</td><td>Palms</td><td>Server</td><td>Food</td><td>Festival</td><td>Remember</td><td>Paradise</td><td>God&#x27;s</td><td>Time</td><td>Do we</td><td>Romantic</td><td>Students</td><td>Seniors</td><td>Family</td></tr><tr><td colspan="16">Optimal Best 2</td></tr><tr><td>Ad11</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>6.1</td></tr><tr><td>Ad12</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>5.5</td></tr><tr><td colspan="16">Pre-crossover</td></tr><tr><td>Ad2</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>2.6</td></tr><tr><td>Ad7</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>3.5</td></tr><tr><td colspan="16">Post-crossover (a=1)</td></tr><tr><td>Ad13</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>3.6</td></tr><tr><td>Ad14</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>2.5</td></tr><tr><td colspan="16">Pre-mutation</td></tr><tr><td>Ad5</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>4.5</td></tr><tr><td colspan="16">Post-mutation (a=2, l=4)</td></tr><tr><td>Ad15</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>2.6</td></tr></table>

![](/api/attachments/Y3ZT6BDR/fulltext/images/78458d84bfbe0532d999ae503ed7905f30ad2ec62145befce31cb71825395145.jpg)  
Fig. 4. The five new advertisements for the Vacation Advertisement from the numerical example, based on the optimal solution 11 and 12 ,Ž . crossover 13 and 14 and mutation 15 .Ž . Ž .

Method 1: Existing method, focus group<sup>r</sup>creative rotation

( Twenty-five ads chosen at random and shown.

( Select top 15 ads focus group . Ž .

( Serve all 15 ads in the first rotation and calculate the click-through rate CTR .Ž .

( Serve each ad a number of times proportional to the CTR in the next nine rotations.

Method 2: Goal programming GPŽ .

( Ten ads chosen at random and are shown to simulated viewers.

( CTR for each ad is recorded.

( Input—ads attribute level combinations Ž . and CTR into GP.

( Output from GP—contribution for each attribute level.

( Fifteen best ads are constructed using the highest scoring attribute levels in various combinations.

( These 15 ads are shown to simulated viewers, CTR recorded, run GP, construct best ads. Repeat this process for the remaining of 10 total rotations.

Method 3: Goal programming plus crossover:

( Ten ads chosen at random and are shown to simulated viewers.

( CTR for each ad is recorded.

( Input—ads attribute level combinations Ž . and the CTR into GP.

( Output from GP—contribution for each attribute level.

( Thirteen best ads are constructed using the highest scoring attribute levels in various combinations.

T<sub>a</sub>bl<sub>e</sub> 4 R<sub>e</sub>-<sub>op</sub>ti<sub>m</sub>i<sub>z</sub>i<sub>ng us</sub>i<sub>ng</sub> th<sub>e new a</sub>d<sub>s</sub>

<table><tr><td rowspan="3"></td><td colspan="13">Attribute levels chosen,  $v_{ial}$ </td><td rowspan="2"> $\sum$  $\sum v_{ial} x_{al}$ </td><td rowspan="3">Observed  $S^{+}$  response rate,  $r_{i}$ </td><td rowspan="3"> $S^{-}$ </td><td rowspan="3">Total</td></tr><tr><td colspan="5">Back drop</td><td colspan="5">Text</td><td colspan="3">Special interest</td></tr><tr><td>Sunrise</td><td>Palms</td><td>Server</td><td>Food</td><td>Festival</td><td>Remember</td><td>Paradise</td><td>God&#x27;s</td><td>Time</td><td>Do we</td><td>Romantic</td><td>Students</td><td>Seniors</td><td>Family</td></tr><tr><td>Ad2</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>2.6</td><td>2.6</td><td>0</td></tr><tr><td>Ad4</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>2.6</td><td>2.6</td><td>0</td></tr><tr><td>Ad5</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>4.5</td><td>4.5</td><td>0</td></tr><tr><td>Ad6</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>2.8</td><td>2.8</td><td>0</td></tr><tr><td>Ad7</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>3.5</td><td>3.5</td><td>0</td></tr><tr><td>Ad11</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>3.5</td><td>3.5</td><td>0</td></tr><tr><td>Ad12</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>4.6</td><td>4.6</td><td>0</td></tr><tr><td>Ad13</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>3.4</td><td>3.2</td><td>0</td></tr><tr><td>Ad14</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>2.7</td><td>2.7</td><td>0</td></tr><tr><td>Ad15</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>4.9</td><td>4.9</td><td>0</td></tr><tr><td> $x_{al}$ </td><td>2.3</td><td>3.3</td><td>3.4</td><td>2.6</td><td>0</td><td>0.1</td><td>0</td><td>1.2</td><td>1.6</td><td>0</td><td>0</td><td>0.5</td><td>0.2</td><td>0</td><td> $\sum$ </td><td>0.2</td><td></td></tr></table>

Table 5  
Comparative analysis of performance across ad optimization methods

<table><tr><td>Method</td><td>Average number of click-throughsa</td><td>Click-through rate (CTR), %</td></tr><tr><td>(1) Focus/creative rotation</td><td>151.15</td><td>7.6</td></tr><tr><td>(2) Goal programming</td><td>218.95</td><td>10.9</td></tr><tr><td>(3) GP and crossover</td><td>224.20</td><td>11.2</td></tr><tr><td>(4) GP, crossover and mutation</td><td>228.11</td><td>11.4</td></tr></table>

<sup>a</sup> Per iteration for 2000 simulated viewers.

( Two ads of the 13 are chosen at randomŽ . and combined using crossover genetic algorithm GA operator, two crossover ads Ž . added to the 13 for a total of 15 ads.

( All 15 ads are shown to simulated viewers, CTR recorded, run GP, construct 13 best ads by GP, two by crossover. Repeat this process for the remaining of 10 total rotations.

Method 4: Goal programming, crossover plus mutation

( Ten ads chosen at random and are shown to simulated viewers.

( CTR for each ad is recorded.

( Input—ads attribute level combinationsŽ . and CTR into GP.

( Output from GP—contribution for each attribute level.

( Twelve best ads are constructed using the highest scoring attribute levels in various combinations.

( Two ads of the 12 are chosen at randomŽ . and combined using crossover spliced atŽ the end of the first attribute , two crossover. ads combined to the 12 for a total of 14 ads.

( One ad of the 12 is chosen at randomŽ . and altered using a mutation GA algorithm operator, mutated ad combined with 14 new ads for a total of 15.

( All 15 ads are shown to simulated viewers, CTR recorded, run GP, construct 12 best ads by GP, two by crossover and one by mutation. Repeat this process for the remaining of 10 total rotations.

Table 5 and Fig. 5 show the improvement of each method over 10 sequential iterations. Clearly, use of the GP solution yields a 43.4% superior solution over the Focus Group<sup>r</sup>Creative Rotation alone. Additionally, the use of GP and Crossover yields a 2.75% better solution than by GP alone; and use of GP, Crossover and Mutation yields a further 1.79% improvement over GP and Crossover. Clearly much of the benefit comes from simply using the GP, with marginal further improvements using the two genetic operators. Note from the graph that use of Crossover and Mutation does not always guarantee a better solution; however, it may yield a better solution on average than GP. We attribute this to the fact that the use of these genetic operators allows us to generate improved ads that would otherwise not be generated: thereby reducing the chance that we become stuck in a local optimum.

![](/api/attachments/Y3ZT6BDR/fulltext/images/35ba4423b931e209a75eeee17456dd97bfa976c9c7a2957b29918c2540590371.jpg)  
Fig. 5. Click through rates for alternate methods.

## 6. Advantages and disadvantages of AdPalette

We showed in the previous section that AdPalette improves the efficiency of ad creation and rotation. The proposed model also results in efficient utilization of computing resource. In particular, we note that storage requirements under the proposed method will be significantly lower than in methods currently being used methods that store and use completeŽ ads . As an illustration, consider an advertisement. that has a attributes and l levels per attribute. Suppose also that the storage requirement per attribute level is s kilobytes say a jpeg file with graphics forŽ each attribute-level used in the ad . The storage. requirement for our model would be sla kilobytes. However, the total number of possible advertisements that our model can create is $l ^ { a } .$ Other techniques that attempt targeted online advertising choosing from $l ^ { a }$ complete ads as in our method would require storage of $s l ^ { a }$ . This means that our method can be up to $( l ^ { a - 1 } ) / a$ times more efficient in storage utilization. AdPalette’s storage savings can grow exponentially with the number of attribute levels that the advertisement has, independent of the size of each graphic file, s. Consider the following numerical example. An advertisement with four attributes each having five levels. Table 6 shows the comparison of the memory requirements for our method and the extreme case.

As can be seen from Table $^ { 6 , }$ for a comparable number of ads, the space required for full ad methods is considerably larger, whereas for comparable storage space, the number of ads that can be displayed is significantly smaller. Considering that some attribute levels will be digitized graphics and audio files, the capacity savings in our model can be substantial.

Savings in server storage requirement four attributes with five Ž levels each, 100 KB file size for each attribute level.

<table><tr><td>Online advertisements methods</td><td>Total number of advertisements</td><td>Storage requirements, MB</td></tr><tr><td>AdPalette</td><td>625</td><td>2</td></tr><tr><td>Full ad method</td><td>625</td><td>62.5</td></tr><tr><td>Full ad method, fewer ads</td><td>20</td><td>2</td></tr></table>

One of the weaknesses of AdPalette is that its operation is based solely on the click-through information. Therefore, if an ad attracts attention but is not clicked on, this information will not be captured and hence will not be available to AdPalette. Perhaps, in the future, when alternative ways of data capturing are available eyeball and cursor move-Ž ments, etc. , this problem will not be as acute..

Another problem is that of self-selection bias. Some online surveys are prone to a self-selection bias—misrepresentation of the population at large by eliminating those who are not online or do not have time to complete a survey. However, we believe that AdPalette is less vulnerable to this bias because we define our AproductB as the online ad itself, and not the target product or service being advertised. For example, in our illustrative example, our product is the online ad and not the advertised vacation. Under this definition, one has to be online to be a prospect for our ad, and we are not eliminating from the population others who may be interested in vacations but do not have online access. Since there is no survey to fill, and only a click that is necessary, we believe that the time requirement will not be an impediment to whether a person clicks through or not. Of course, a prospect may factor in the time spent looking at the target site once they click through. We could further restrict our results to be valid only to a target audience of Aonline users in the market for product or service $\mathrm { \Delta } \mathrm { X , \ " }$ to reduce any bias in interpretation of the results.

There is, however, still the bias from the fact that the ads may be shown only on certain web sites, for instance, New York Times, and these web sites may have an audience with a specific demographic profile. Therefore, the results of AdPalette will be only valid for redisplay on the same or similar sites. If the ad is shown on a wider cross-section of web sites with heterogeneous demographic profiles, then Ad-Palette should be run separately for click-throughs from homogeneous subgroups of web sites e.g., Ž have different AdPalettes for women oriented sites, such as iVillage . The optimal ads should be redis-. played only within those sub groups.

## 7. Conclusion

We have presented an algorithm for customizing ads in real time using response rates from ads already placed. Instead of cycling AfullB ads through the web sites or e-mails, as is done at present, we present a method that works at the attribute level to reconstitute ads on the fly. We consider AdPalette as an effective approach that incrementally adds response information to the ad strategy to influence future ad placement. Our method requires response rate information, and assumes that all attribute level combinations are feasible.

We show with simulated data that our method results in improved ad effectiveness, savings in server storage requirements, and ability to display more ads for the same amount of storage space. Since our method considers all possible ads, it does not suffer from the absence of certain ads from a traditional lineup due to oversight or them not being picked by focus groups. Our approach is fast and can be used for real time ad rotation. We believe this paper makes a significant contribution to the sparse literature on customizing online ads available at the moment. We plan on future work that will address the sensitivity of parameter values on the effectiveness of our approach.

## Appendix A. Table of online advertising technologies

<table><tr><td>Software</td><td>Developer</td><td>Features</td></tr><tr><td>Accipiter AdManager 4.0</td><td>Engage Technologies</td><td>·ad scheduling and targeting, inventory rotation, generation of up-to-the-minute, customized reports ·enables sites to target ads using a wide range of criteria: ·web and enterprise-wide visitor profiles ·declared visitor profile information gathered from site registration ·area of content a visitor is viewing ·Internet-based registration, including domain type, browser, platform, time of day, and day of the week ·keyword or keyphrase searches ·compound demographic targets specified by the site ·scheduling features that allow ads to be scheduled either by the total number of impressions or clicks, specific time frames specified by the advertiser, click count or impression goal, combinations of counts and date ranges, and specific counts and date ranges ·reports can detail how many impressions and clicks were generated both from the entire site and by each ad and advertiser, or how much revenue was generated on any day, week, month, year, or in any period specified</td></tr><tr><td>Accipiter</td><td>Engage</td><td rowspan="2">• serves highly targeted ads based on visitor's behavior across the entire Internet without collecting or using any personally identifying information</td></tr><tr><td>AdManager 4.0</td><td>Technologies</td></tr><tr><td>ActiveTrack</td><td>Thinking Media</td><td>• uses client-side tracking• the client-side tracking method places a small Java applet (about 0.5 KB) into an ad or page. The applet acts like a “radio transmitter.” As soon as the ad or page loads into a browser, this transmitter starts sending real-time data on where the ad is running and how surfers are interacting with it back to the ActiveTrack database, bypassing server-based reporting entirely• ActiveTrack databases keep track of IP address and cookie information for ad or page; the IP and cookie combination identifies one browser, on a specific machine, via an ISP, which in turn translates into a single set of eyeballs; ActiveTrack uses this to create a “closed loop” system of associating the delivery of any and all ActiveTrack-enabled ads and web pages to individual Web surfers, and tracking the actions they take, including the reach and frequency of ad delivery and cumulative history of exposures to all advertising in a campaign• advertisers can use time for evaluating the effectiveness of their campaigns, including time-on-page, and play time, as standard metrics• ActiveTrack provides complete reports on any in-banner behavior for ActiveTrack rich media; this can include scores of games played, time spent interacting with the banner, contact information entered, menu choices, and more, regardless of whether a click-through or transaction was generated; this becomes part of the anonymous profile of individual surfers, which in turn can be used to adjust delivery of creative messages</td></tr><tr><td>Ad Force</td><td>AdForce</td><td>• advertising less repetitious, more relevant, and more likely to match interests of the web surfers• AdForce targets campaigns with a wide variety of criteria including domain/SIC code, content area, keywords, and geography• provides the advertisers with details regarding the type of users who saw their ads, visited their site, registered or bought their product; reports can further summarize how</td></tr><tr><td>ActiveTrack</td><td>Thinking Media</td><td>often these users access the Web, what other kinds of sites they go to, and how likely they are to purchase online</td></tr><tr><td>Ad Juggler</td><td>digitalNATION</td><td>·100% of the banner management is performed via the Web browser; the system also supports multiple banner pools for each page within a site, users determine the sets of banners that appear on it·statistical reports are generated and e-mailed based on the number of delivered impressions/clicks or based on a length of time; advertisers can set the report generation frequency and contact e-mail addresses without administrative involvement·transparent support for multiple non-overlapping banners on one page; this is accomplished by using cookies or IP address-tracking database for browsers that do not support cookies to ensure that click-throughs are properly redirected; both SSI and cookie modes are independent of each other, and can be used interchangeably or in any combination·to allow extra flexibility in assigning banners to particular pages or areas of the site, “virtual” pools can now be defined, if deemed more appropriate as compared to “physically” existing pages</td></tr><tr><td>AdGenie</td><td>AHG</td><td>·it can be used to add, update, renew and review current ads through HTML forms; it will display ads as part of HTML pages, in a separate frame or on the pages produced by CGI programs on the fly; the ads automatically expire after specified amount of days or impressions or click-throughs; users can specify various parameters for ad display, such as day(s) of the week, time intervals, pages, domain name extension, and keywords (if used in conjunction with search engine)</td></tr><tr><td>AdKnowledge</td><td>AdKnowledge</td><td>·cross-site targeting, including by page, keyword, domain, operating system and browser type·creative rotation including hourly, daily, percentage, fractional, frequency and sequence·robust cookie database to define customer segments and target different creatives to each segment</td></tr><tr><td>AdMan</td><td>Medius Interactive</td><td>·banners can be placed and weighted for control over frequency and distribution of ad exposures·banners can also be added or removed automatically from all rotations according to set time periods</td></tr><tr><td>AdMaximize</td><td>AppNet</td><td>· provides real-time information on performance of specific ad creative and placement· enables advertising optimization</td></tr><tr><td>AdServer</td><td>NetGravity</td><td>· advanced inventory management model that accounts for fine-grain targeting, unique site traffic patterns, and overlapping profiles· user data targeting: deliver one-to-one targeted promotions to known users· geoTargeting: enables you to accurately segment and target your audience by geographical areas, and firmagraphic data· targeting audiences based on demographic data</td></tr><tr><td>DAD</td><td>free</td><td>· each ad's remaining daily impressions get recalculated once a day; an ad's remaining daily impressions is set to the total number of remaining impressions for the ad divided by the number of days remaining in the ad's run; this value is used for weighted targeting instead of just impressions remaining in the ad run to provide some even distribution of an ad's delivery over its entire run· clickthrough rates decline pretty steadily as a user sees the same banner ad over and over again. Advertisers like to be able to limit the number of times that a specific user will see a specific banner. This requires more work by the advertiser—they need to provide more different banners to your site—but it can increase click-throughs; DAD can limit the number of times a given user is exposed to a specific banner· if an ad has an exposure limit set, DAD retrieves the current session ID and attempts to find out how many times the current session ID has seen each of the possible ads; if that value exceeds the exposure count, the ad is marked as ineligible; when DAD eventually picks the actual ad to serve, it increments the session ID's count of times that ad has been viewed</td></tr><tr><td>Open AdStream</td><td>Real Media</td><td>· open AdStream can target ads by making use of database information collected on visitors; the information is encoded in a cookie on the visitor's browser and is read before subsequent ad deliveries; the software can target based on page content, environmental variables, search words, top-level domain targeting, sub-domain targeting, operating system, browser, and cookies· deliver advertising campaigns based on demographic and visitor registration information· controlled frequency of ad rotation· linked companion banners</td></tr><tr><td>Open AdStream</td><td>Real Media</td><td>·exclusion of competitive advertisers' message on the same page·registration database targeting—target ads based upon registration information (age, gender, income, etc.)·target ads to visitors of specific page positions, pages, directories, or sites; pages, directories, and sites can be grouped together into content sections which can then be targeted with one mouse-click; content keywords can also be embedded into the HTML of a page to allow further content targeting·Open AdStream can target ads based upon passively gathered information about the visitor like browser, operating system, and domain·search words·database integration—integrate virtually any database to target visitors·domain targeting·starting with the first visit, the system automatically starts learning about each site visitor's individual interests and tastes; the system keeps learning more with each repeat visit·monitors the ad server schedule to optimize ad distribution, automatically compensates for low levels of information about new site visitors, and dynamically adjusts levels of information about each visitor's interests and tastes·prioritizes and rates campaigns based on the ad server criteria·enables a web site publisher to more accurately target ads using information collected from a visitor·specification of targeting values to be included in the cookie file·target ads based on key word searches</td></tr></table>

## References

<sup>w</sup> <sup>x</sup> 1 Ad Networks, Brokers, and Reps, URL: http:<sup>rr</sup>www. adbility.com<sup>r</sup>wpag<sup>r</sup>ba network.htm, Jan. 2000.

<sup>w</sup> <sup>x</sup> 2 Adres, URL: http:<sup>rr</sup>adres.internet.com<sup>r</sup>software<sup>r</sup>management<sup>r</sup>article<sup>r</sup>0,1401,9261 176211,00.html, Jan. 2000.<sub>–</sub>

<sup>w</sup> <sup>x</sup> 3 P.V. Balakrishnan, V.S. Jacob, Genetic algorithms for product design. Management Science 42 8 1996 1105–1117.Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 S. Bhattacharyya, Direct marketing performance modeling using genetic algorithms, Journal of Computing 11 3 1999Ž . Ž . Ž . Summer .

<sup>w</sup> <sup>x</sup> 5 D. Blankenhorn, AdKnowledge goes beyond clicks to measurable results, Advertising Age 70 9 1999 Mar. .Ž . Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 A. Chang, P.K. Kannan, A.B. Whinston, The economics of freebies in exchange for consumer information on the internet: an exploratory study, International Journal of Electronic Commerce 4 1 1999 Fall .Ž . Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 G.D. Eppen, F.J. Gould, C.P. Schmidt, J.H. Moore, L.R. Weatherford, Introductory Management Science. 5th edn., Prentice Hall, New Jersey, 1998.

<sup>w</sup> <sup>x</sup> 8 P.E. Green, A.M. Krieger, Models and heuristics for product line selection, Marketing Science 4 1985 1–19.Ž .

<sup>w</sup> <sup>x</sup> 9 P.E. Green, A.M. Krieger, Recent contributions to optimal

product positioning and buyer segmentation, European Journal of Operational Research 41 1989 127–141.Ž .

<sup>w</sup> <sup>x</sup> 10 J. Heinen, Internet marketing practices, Information Management and Computer Security 4 5 1996 7–14. Ž . Ž .

<sup>w</sup> <sup>x</sup> 11 IAB Online Advertising Effectiveness Study: a joint research effort of Internet Advertising Bureau and Millward Brown Interactive, 1997.

<sup>w</sup> <sup>x</sup> 12 P.K. Kannan, A. Chang, A.B. Whinston, Marketing information on the i-way, Communications of the ACM 41 3Ž . Ž . Ž . 1998 35–43, March .

<sup>w</sup> <sup>x</sup> 13 M. McCandless, Web advertising, IEEE Intelligent Systems 13 3 1998 May–June .Ž . Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 Z. Michalewicz, Genetic Algorithms<sup>q</sup>Data Structures<sup>s</sup> Evolution Programs. 3rd edn., Springer, Berlin, 1996.

<sup>w</sup> <sup>x</sup>15 R. O’Keefe, T. McEachern, Web-based customer decision support systems, Communications of the ACM 41 3 1998Ž . Ž . Ž . March .

<sup>w</sup> <sup>x</sup> 16 J. Patrick, Online advertising goes one-on-one, Scientific America 277 6 1997 Dec. .Ž . Ž . Ž .

<sup>w</sup> <sup>x</sup> 17 T.S. Raghu, P.K. Kannan, H.R. Rao, A.B. Whinston, Dynamic profiling of customers for customized offerings over the Internet, a model and analysis, Decision Support Systems 32 2 2001 117–134.Ž . Ž .

<sup>w</sup> <sup>x</sup> 18 Realmedia, URL: http:<sup>rr</sup>www.realmedia.com, Jan. 2000.

![](/api/attachments/Y3ZT6BDR/fulltext/images/3f9980eafd843b1d640044b85e2d2d1d0d677fdd68aba4ca9fc344b03870636e.jpg)

Gilbert G. Karuga is a PhD student at the University of Connecticut, Department of Operations and Information Management. He received his BS degree Ž . Mathematics in 1988 and MBA in 1990 from the University of Nairobi, Kenya. His current research interests are in online service delivery, especially in the design and optimization of online business models. He also has teaching interests in Business information systems, especially the deployment of business decisions support systems.

![](/api/attachments/Y3ZT6BDR/fulltext/images/c24e525850783bd502a2b92bf3b930bf9df0e81ae451a96aa05a0155c9ec067c.jpg)

Andriy M. Khraban is completing his PhD in Operations and Information Management at the University of Connecticut. He holds an MA in Economics and an MA in Financial Management from the Catholic University of America Ž . Washington, DC, USA , and a BA in Economics from the National University of Kyiv-Mohyla Academy Kyiv,Ž Ukraine . His business experience in- . cludes Ukrainian utility industry regulation and energy market restructuring. He

currently teaches courses in MIS and Operations Management at the University of Connecticut. His current research interests are in e-commerce related areas.

![](/api/attachments/Y3ZT6BDR/fulltext/images/37257a3e9e076e44876770cf25f96ec9c896c738cbdf83769833c5e40c8bc786.jpg)

Suresh K. Nair received his PhD and M.S. degrees from Northwestern University, and a BS degree from Indian Institute of Technology, Kharagpur. He is currently an Associate Professor, Director of Research and Grant Development, and Cizik Research Scholar with the School of Business Administration, University of Connecticut, Storrs. His current research interests are service operations, especially in financial services, product design and yield management.

He is consultant to various businesses. He has published in Management Science, NaÕal Research Logistics, IIE Transactions, IEEE Transactions on Engineering Management, Decision Sciences and European Journal of Operational Research.

![](/api/attachments/Y3ZT6BDR/fulltext/images/f08939eda4e95a913fae4413446004fdd6bf1bc9dd0fbf7320056f6a7405d7c7.jpg)

Daniel O. Rice holds an MBA in Finance from the University of Connecticut and a BS degree in Naval Architecture and Marine Engineering from the United States Coast Guard Academy. He is currently pursuing a PhD in Information Systems at the School of Business Administration, University of Connecticut, Storrs. His current research interests are Internet economics, data privacy and security, and business to business and consumer relationships management.
