---
otero_id: 13378
otero_key: "4A8P7N67"
title: "The economics of stock touting during Internet‐based pump and dump campaigns"
authors: "Michael Siering"
year: "2019"
journal: "Information Systems Journal"
doi: "10.1111/isj.12216"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
R E S E A R C H A R T I C L E

WILEY

# The economics of stock touting during Internetbased pump and dump campaigns

Michael Siering

Goethe University Frankfurt Theodor‐W.‐Adorno‐Platz 4, 60323 Frankfurt, Germany

Correspondence

Michael Siering, Goethe University Frankfurt, Theodor‐W.‐Adorno‐Platz 4, 60323 Frankfurt, Germany. Email: siering@wiwi.uni‐frankfurt.de

## Abstract

Information systems have facilitated the increase in relevance of financial markets. Nevertheless, the rise of the Internet has eased information‐based financial market manipulations. In this study, we examine the phenomenon of stock touting during pump and dump campaigns, in which deceivers advertise stocks to profit from an increased price level. We observe that the positive prospects promised are not confirmed by corporate disclosures and financial news. Furthermore, manipulators select targeted financial instruments based on specific stock and company characteristics. Manipulators avoid signals of anomaly and prefer unknown stocks. We find that stock touting has a positive market impact but that it is followed by a large decline in stock price in the subsequent days, causing investors to lose substantial amounts of their investments. We consider the impact of information generation, information content, and information presentation on the corresponding market reaction. Interestingly, information generation influences the demand for the stock, but information content and information presentation drive the willingness to pay. Our results are highly relevant for Internet users, software vendors, and market surveillance authorities, as a deep understanding of such information‐based manipulations is necessary to develop appropriate countermeasures.

## KEYWORDS

content analysis, deceptive information practices, event study, financial market manipulation, pump and dump manipulation, stock touting

## 1 | INTRODUCTION

In recent years, the trust in financial markets has been reduced because of the financial crisis and the increasing role of financial market manipulations. Technological improvements are also accompanied by several downsides, as manipulative behaviour has become an enormous problem in electronic markets, affecting a large number of Internet users (Chua, Wareham, & Robey, 2007; Gyongi & Garcia‐Molina, 2005). Specifically, the Internet is utilized by market manipulators to perform information‐based pump and dump market manipulations: in such cases, a deceiver first buys a stock and then advertises or commissions a promoter to tout the stock by spreading positive messages, thereby manipulating the share price and selling the stock at a profit (Frieder & Zittrain, 2006). In several cases, manipulators and stock promoters have already been prosecuted by regulatory authorities because of stock touting in the course of pump and dump manipulations (Bloomberg, 2015; SEC, 2014; Wall Street Journal, 1999).

Although the general negative impact of manipulations performed using the Internet is apparent, little is known about the detailed characteristics of stock touting and the stocks targeted by manipulators. In addition, the specific economic consequences of stock touting remain vague. Previous research neglects whether the positive prospects promised in stock touts are actually confirmed by financial news or corporate disclosures. Furthermore, prior studies have not investigated whether stocks with specific characteristics are targeted by manipulators, although suc information would be important for detecting manipulative behaviour and for fostering trust in financial market (Xiao & Benbasat, 2011). Additionally, previous research in the field of information systems categorizes the information practices performed by manipulators (Grazioli & Jarvenpaa, 2003), covering the information exchange between manipulators (for instance, a website) and their targets (Xiao & Benbasat, 2011), specifically manipulation of (1) information content, (2) information presentation, and (3) information generation. However, the influence of thes practices on the economic impact of stock touting remains vague as well

Prior research on stock touts sent via e‐mail has found that pump and dump schemes can cause dramatic losses for investors when scammers close their positions (Böhme & Holz, 2006). However, related studies have mainl investigated the information practice of information generation, primarily examining how the number of stock touts published influences the success of stock touting (Böhme & Holz, 2006; Hanke & Hauser, 2008). By contrast, the impact of information practices regarding information content and information presentation has been neglected Nevertheless, the transmission of positive information content, in particular, is a core component of pump and dump stock market manipulations (SEC, 2012b); thus, it should not be ignored. Finally, previous research has shown that information presentation, for instance, by applying specific text highlighting techniques, affects user behaviour therefore, it should not be neglected as well (Danaher, Mullarkey, & Essegaier, 2006)

In this study, we provide a thorough understanding of the phenomenon of stock touting using the Internet. We investigate whether stock touting in the course of pump and dump campaigns provides indications of deceptive behaviour. Therefore, we first investigate whether the positive prospects touted using the Internet actually prevail ie, whether they are also confirmed by corporate disclosures or financial news (research question 1). As a next step, we analyse whether pump and dump campaigns target stocks with specific stock and company characteristics to avoid being detected (research question 2). We then investigate whether stock touting in the course of pump and dump campaigns is effective, causes a market reaction (encompassing traded volume and stock returns during th campaign), and how the different information practices influence its success (research question 3)

For our empirical study, we acquire a dataset covering stock touts published in the course of pump and dump campaigns identified by means of criteria published by the United States Securities and Exchange Commission (SEC). These criteria, denoted as “common red flags”, should be considered to avoid being affected by market manipulations (SEC. 2012b), We first examine whether the positive prospects promised materialize and are reported in corporate disclosures and financial news. We then analyse the characteristics of the stocks touted and compare them with a control sample of non‐touted stocks. By means of an event study (MacKinlay, 1997), we investigate the market reaction following the stock touts; specifically, we examine whether investors actually lose some of their investments after buying the related stock. Finally, we investigate the different information practices used to explain the market reaction during the campaign.

Our analysis reveals that the positive corporate prospects outlined in the stock touts are rarely confirmed by corporate disclosures or financial news. We find that stock touting is focused on relatively easy to purchase stocks whose issuers have a short unburdened history and who report according to accepted financial standards. We als find that pump and dump campaigns have a market impact and that investors bear the risk of losing a substantia portion of their investments after the end of the campaign. Furthermore, our analysis explaining the market reaction reveals that information generation influences the demand for a stock, whereas information content and informatio presentation affect the willingness to pay for the stock. Consequently, we find several indications for deceptive behaviour in the context of stock touting.

We extend the previous understanding concerning the reliability of the stock touts' contents and concerning th stock characteristics targeted by manipulators, whereas we show that the positive prospects promised do no materialize and that manipulators prefer unknown products with characteristics that do not cause signs of anomaly. Furthermore, we contribute to the literature by investigating the economic impact of stock touting and the influenc of different information practices on the consequent market reaction. In addition, our results are of particula practical relevance for financial market participants, market surveillance authorities, and software vendors to develo appropriate detection mechanisms for information‐based market manipulations.

The remainder of this paper is structured as follows. In Section 2, we present recent developments related to financial markets and the “dark side” of information systems and summarize the results of previous work focusing on stock touting during pump and dump campaigns. Additionally, our research hypotheses are presented in Section 2. These hypotheses focus on the question of whether the positive prospects touted actually prevail, whether specifi product characteristics are preferred by deceivers, the economic impact of stock touting, and the impact of deceptiv information practices on the market reaction caused by stock touts. Section 3 explains how our dataset was created and presents the research methodology applied. Within Section 4, our empirical study is presented, and the results are discussed in Section 5. Finally, Section 6 concludes.

## 2 | BACKGROUND AND RESEARCH HYPOTHESES

## 2.1 | Financial markets and the “dark side” of information systems

The importance of financial markets has constantly increased (Epstein, 2004), whereas the expansion of information technologies has been a key driver of financial integration (Lagoarde‐Segot, 2017). Information systems have altered market mechanisms, thereby changing finance and banking (Currie & Lagoarde‐Segot, 2017). Specifically, the Interne enables more efficient information exchange and increases the speed of information processing; thus, it positivel influences market efficiency

Nevertheless, at the same time, the increased amount of available information and the role of market participants showing dishonest behaviour make it difficult for Internet users to assess the accuracy of the information published (Kim, Jeong, Kim, & So, 2011; Seo & La Paz, 2008). Furthermore, this increased uncertainty can lead to reduced willingness to use information systems (Tarafdar, Gupta, & Turel, 2013; Tarafdar, Tu, Ragu‐Nathan, & Ragu‐Nathan 2011) and to reduced trust towards the financial system as a whole (Siering, Clapham, Engel, & Gomber, 2017).

The Internet specifically enables dishonest behaviour due to low entry barriers, anonymity, and spatial as well as temporal separation of deceivers and targets (Xiao & Benbasat, 2011). Consequently, fake websites or deceptive online shops have become a serious problem within the Internet (Abbasi, Zhang, Zimbra, Chen, & Nunamaker 2010). For instance, the Federal Bureau of Investigation (FBI) lists several forms of Internet deception in the Interne crime report (FBI, 2015).

“Internet” serves as an umbrella term related to the world wide web including (social media) websites, message boards, and e‐mail. Deception can be characterized as a “form of information manipulation that occurs when an opportunistic agent induces a misrepresentation that is designed to influence the behaviour of another agent” (Johnson, Grazioli, Jamal, & Glen Berryman, 2001, p. 356); thus, it is “defined as a message knowingly transmitted by a sender to foster a false belief or conclusion by the receiver” (Buller & Burgoon, 1996, p. 205). Deception is a broader term than fraud because fraud is related to a legal violation that differs in various countries and is therefore more difficult to identify (Grazioli & Jarvenpaa, 2003). Internet deception thus encompasses information manipula tion using the world wide web as a medium (Grazioli & Jarvenpaa, 2003). Overall, approaches for detecting deceptive behaviour are essential to reduce the negative impact arising from deceptive behaviour pursued using the Internet (Zahedi, Abbasi, & Chen, 2015). Consequently, such approaches are valuable for increasing trust towards financia markets (Currie & Lagoarde‐Segot, 2017)

Different techniques carried out by deceptive market participants have been identified (Grazioli & Jarvenpaa 2003). In electronic commerce, deceivers either try to hinder consumers to obtain a correct view of a product b concealment and equivocation of product aspects or to foster an incorrect view of the product by falsification (Xiao & Benbasat, 2011). These different techniques can be pursued on diverse levels covering the information exchange between deceivers (eg, via a fraudulent website) and their targets (Xiao & Benbasat, 2011).

Specific deceptive information practices performed are the manipulation of (1) information content, (2) information presentation, and (3) information generation. Manipulation of information content encompasses the “direct alteration of the content of product information provided,” manipulation of information presentation includes th “manipulation of the design of how product information is presented,” and manipulation of information generation refers to the “manipulation of the dynamic production of product information” (Xiao & Benbasat, 2011)

Compared with other research topics in the field of information systems, deception has received far less attention (Wareham, Zheng, & Straub, 2005). Previous research has investigated which tactics are pursued by deceptive market participants (Grazioli & Jarvenpaa, 2003; Mavlanova, Benbunan‐Fich, & Kumar, 2008). Furthermore, the impact of perceived deception on consumer satisfaction and loyalty has been analysed (Román, 2010). However specifically focusing on financial markets, the targeted products (ie, stocks), the economic impact, and the influenc of the different information practices have been neglected so far. Nevertheless, such insights are important for researchers and practitioners to assess the severity of deceptive tactics and to develop appropriate countermeasures fostering the trust towards financial markets

Against this background, focusing on investment products, more specifically stocks, is of particular interest. First, an analysis whether the positive prospects touted can be confirmed provides initial insights into whether falsification is being performed. Second, an analysis of the stocks targeted allows the obtaining of specific insights related to the products usually targeted by manipulators to develop appropriate detection mechanisms. Third, it allows for a measuring of the economic impact and the impact of different information practices. On one hand, manipulators in the field of stock touting typically apply tactics such as falsification of information, for instance, regarding the future prospects of a stock (Grazioli & Jarvenpaa, 2003). On the other hand, in contrast to other fields of Internet deception, success can easily be measured by considering the financial performance of the investments advertised-most commonly by analysing the stock market reaction during pump and dump campaigns touting specific stocks.

## 2.2 | Economic impact of stock touting during pump and dump campaigns

Pump and dump stock market manipulations aim at manipulating (ie, increasing) the share price by the publication of false and misleading information related to a specific stock (SEC, 2012b). Typically, after “pumping” the price by touting the stock in various newsletters or messages published within the Internet (ie, by publishing positive recommendations about the stock), the initiators then sell their shares with profits at an increased price level (Frieder & Zittrain, 2006).

Pump and dump campaigns are pursued either by manipulators who are independent from the targete company or by company representatives. In some cases, promoters are hired to tout a certain stock (Nelson, Price, & Rountree, 2009). Thereby, manipulators apply different information practices (Xiao & Benbasat, 2011) focusing on information content (eg, by publishing extremely positive information related to a stock, for instance about positiv business prospects that do not prevail), information presentation (eg, by using text highlighting), and, most generally information generation (eg, by producing an increased number of messages advertising a stock and by using different media channels).

Stock touting during pump and dump campaigns fits the Internet deception definition as provided above. On one hand, pump and dump campaigns are performed via the Internet. Here, different websites and newsletters are used to publish stock touts. On the other hand, pump and dump campaigns match the definition of deception (Buller & Burgoon, 1996), which encompasses a sender who knowingly transmits a message to foster a false belief by the receiver. Here, the receiver is an investor which shall be convinced to buy the stock. The sender can thus eithe be the manipulator (who holds shares and directly profits from a price increase) or a promoter who publishe positive news about a specific stock (and is rewarded for his activities by the manipulator). Consequently, manipulator and promoter (if involved) profit. Manipulators profit because of the price increase during the campaign. If promoters tout the stock, they profit because they earn a specific reward (eg, stocks of the touted company or cash, SEC, 2012b).

In the case of stock touting, the messages sent are represented by the different touts recommending a specific stock. Here, a positive view is transmitted about a company's future prospects (representing the false belief that is fostered). This is shown when the positive prospects promised are not confirmed by regular news sources in the form of corporate disclosures or financial news and when large price decreases are observed after the pump and dump campaign has ended. Typically, this false belief is knowingly (not mistakenly) transmitted. In this case, price increases during the campaign are driven by investors' false beliefs instead of by favourable business prospects. In previous years, the SEC has prosecuted several stock promoters for pursuing such pump and dump manipulations (Bloomberg, 2015; SEC, 2014; Wall Street Journal, 1999).

Previous research has investigated the economic impact of pump and dump campaigns pursued via e‐mail. Nevertheless, previous research relies on single communication channels (mostly e‐mail) and neglects the impact of the different manipulation levels on the success of Internet deception (Böhme & Holz, 2006; Hanke & Hauser 2008). In this context, most previous studies rely on datasets composed of “stock spam” received via e‐mail using the stock spam effectiveness monitor (SSEM, 2007) that covers stock touts from 2004 to 2007 (Hanke & Hauser, 2008). Different studies provide evidence that such stock spam causes financial market reactions. For instance, Böhme and Holz (2006) find that stock spam initially leads to positive abnormal returns but that this effect is reversed when no further spam is sent. Additionally, Hanke and Hauser (2008) find that stock spam influences turnover and the intraday price range. Frieder and Zittrain (2006) as well as Huang and Cheng (2013) confirm the impact of stock spam on stock prices. This leads to the conclusion that spammers follow a “buy low and spam high” strategy (Frieder & Zittrain, 2006). Different authors find that positive returns cannot be measured for every campaign. Instead, positive and negative outcomes occur almost equally frequent, but the positive abnormal returns are higher than the negative ones (Böhme & Holz, 2006; Nelson et al., 2009).

Related to the impact of regulatory countermeasures on the effectiveness of stock spam, Hu, McInish, and Zeng (2009) find that spam e‐mails following regulatory requirements and revealing conflicts of interest are accompanied by reduced market reactions. Based on moderated messages posted in 2008, Delort, Arunasalam, Leung, and Milosavljevic (2011) find that message boards are also used for market manipulations and that such messages lead to capital market reactions. These studies provide an understanding of the impact of pump and dump campaigns on financial markets. However, they mainly focus on stock touts distributed via e‐mail in the form of stock spam. Against the background of new spam‐filtering technologies and regulatory countermeasures (SEC, 2012c; Symantec, 2011) on one hand and new possibilities for distributing stock touts on social media on the other hand (SEC, 2012b), an understanding of the impact of such stock touts sent via channels apart from e‐mail is necessary.

Regarding the information practices and their impact on the success of stock touting, previous studies mainly focus on the manipulation of information generation and find that an increased number of messages sent has a positive influence on the subseguent market reaction (Erieder & Zittrain. 2006). Nevertheless the influence of the campaign duration on the economic impact remains vague. Furthermore, previous studies neglect the impact of information content (represented by positive information about a stock that is the main characteristic of pump and dump manipulations) and information presentation (by highlighting different parts of the information published, for instance, by using headlines or bold fonts). Moreover, previous studies do not provide comprehensive insights int the confirmability of the positive prospects touted, the stocks touted itself and they do not investigate whether such characteristics might be incorporated as domain knowledge in the field of deception detection. In this study, we aim at closing these research gaps

## 2.3 | Overview of research hypotheses

As outlined in Figure 1, we present our research hypotheses (H) to investigate the research questions (RQ), providing a comprehensive understanding of the phenomenon of stock touting. We focus on the positive prospects promised in stock touts (RQ1, H1) and the characteristics of touted stocks (RQ2, H2‐H4), and we examine the economic impac of stock touting (RQ3, H5‐H9). We focus on these research areas to assess whether deceptive behaviour can be identified in the field of stock touting. Therefore, we build upon the literature on Internet deception and the mode of deception detection (Johnson et al., 2001) to hypothesize about the content and factors typical for touted stocks. Furthermore, we focus on theories from financial (Fama, 1970), marketing (Arens, Schaefer, & Weigold, 2012) and especially information systems research (Xiao & Benbasat, 2011) to provide a thorough understanding of the economic impact of stock touting.

## 2.4 | Confirmability of stock touts

Pump and dump campaigns are characterized by the recommendation of specific stocks, whereas positive prospects related to the company issuing the stock are outlined claiming to materialize quickly. If these positive prospects prevail (and materialize), other information sources such as the corporations themselves and regular financial new also report on these positive events in the form of news articles about, eg, acquisitions or new product developments.

Nevertheless, in cases of pump and dump market manipulations, promoters perform falsifications to artificiall increase the share price related to a stock instead of conducting exhaustive research and recommending stocks with actually prevailing positive prospects (Xiao & Benbasat, 2011). Thus, the positive prospects reported can be regarded as a false belief that is fostered (Buller & Burgoon, 1996). Consequently, we hypothesize that claims made in stock touts during pump and dump campaigns cannot be verified using traditional news sources, thereby resembling indications for deceptive behaviour:

H1: The positive prospects touted are not confirmed by corporate disclosures and financial news.

![](/api/attachments/4A8P7N67/fulltext/images/63893874b6d7cc543e8a5f727446f2acc30162cf3479c73e312c84ce7db609f3.jpg)  
FIGURE 1 Overview of research hypotheses

## 2.5 | Characteristics of touted stocks

Insights related to the product targeted are helpful for developing appropriate detection mechanisms and improving the understanding of stock touting in general (Xiao & Benbasat, 2011). Manipulators can be expected to focus on products that do not cause signs of anomaly to avoid being detected and thus to avoid affecting the success of their tactics.

To derive our research hypotheses regarding the characteristics of touted stocks, we especially build upon the model of deception detection by Johnson et al. (2001). The model covers the phases of deception detection (ie, activation, hypothesis generation, hypothesis evaluation, global assessment) and posits that individuals detect deception if they are able to sense inconsistencies (Johnson et al., 2001; Johnson, Grazioli, & Jamal, 1993). Anomalies can be sensed because of the presence or absence of cues such as seals or reputation (Xiao & Benbasat, 2011) whereas many other informational cues can be used for detecting deception (Humpherys, Moffitt, Burns, Burgoon, & Felix, 2011; Meservy et al., 2005; Zhou, Burgoon, Nunamaker, & Twitchell, 2004; Zhou & Zhang, 2008). In general individuals are deceived successfully if they are unable to detect anomalies. The risk of being deceived is therefor especially high when domain knowledge is lacking (Johnson et al., 2001)

Since pump and dump campaigns focus on stocks, we consider the two most central product aspects that could lead to inconsistencies perceived by Internet users: the stock targeted and the company issuing the stock. It can generally be assumed that deceivers focus on companies and stocks that are less likely to cause signs of anomaly. In addition, deceivers can be expected to target stocks that are not well known, so Internet users have low domain knowledge related to the financial instrument. In this case, Internet users are less able to detect the deceptive actions; finally, a large number of users are expected to buy the advertised financial instrument. As possible signals of anomaly, we consider the questions how conveniently the touted stock can be traded, how well‐established the company issuing the stock is, and whether the company follows well‐established accounting standards.

## 2.5.1 | Stock characteristics

The products targeted during pump and dump campaigns are stocks traded on low‐regulated markets with a low market capitalization, so a manipulation can be successful even if only a small number of traders acts on the stock touts (SEC, 2012c). Nevertheless, although the market capitalization of the manipulated stock can be assumed low, the touted stock must have some supply so interested investors can buy the financial instrument and do not perceive a sign of anomaly because they are unable to trade the stock. Consequently, from the pool of stocks traded on low‐regulated markets, manipulators choose stocks that are relatively convenient to trade, which is, for instance, resembled in the free float, ie, the number of stocks available for trading on the market. Consequently, we hypothesize:

H2: Compared with non‐touted stocks, touted stocks are more convenient to trade.

## 2.5.2 | Company characteristics

If Internet users are interested in a stock, they first search for information regarding the company issuing the financia instrument (Da, Engelberg, & Gao, 2011). If a company has been active on the market for a long time span, a larger amount of news can be found, which might also include negative reports. Because negative news can have a more severe and a longer term impact than positive news, we hypothesize that manipulators prefer to focus on more recently funded companies to reduce the risk that possible signals of anomaly are perceived by Internet users Furthermore, when a company is more recently funded, Internet users have a lower chance of possessing domain knowledge related to the targeted instrument that would enable them to assess the company's real prospects and to detect deceptive information practices. Consequently, we hypothesize:

H3: Compared with non‐touted stocks, companies issuing touted stocks have been established more recently.

Because stocks advertised within pump and dump campaigns are traded on low‐regulated markets, issuing companies can choose between reporting standards when publishing their fiscal results. Such compliance with well‐accepted reporting standards could be seen as a third‐party seal, increasing the trust towards the compan (Kim, Ferrin, & Rao, 2008) and reducing the risk of anomaly detection. Consequently, we hypothesize:

H4: Compared with non‐touted stocks, companies issuing touted stocks more often follow wellaccepted reporting standards.

## 2.6 | Economic impact of stock touting

To elaborate on the economic impact of Internet deception in the form of stock touting during pump and dump campaigns and to hypothesize on the effects of different information practices, we build upon previous literature in the fields of information systems and financial markets

Pump and dump market manipulations are characterized by the publication of information that urges readers to buy the advertised stock (SEC, 2012b). Because this characteristic is similar to classical advertisements (Arens et al., 2012), we also focus on theoretical insights from marketing research to explain which aspects make stock touting effective. To distinguish effects on the economic impact of pump and dump campaigns, we follow the theoretica model of product‐related deceptive information practices by Xiao and Benbasat (2011) and consider the influenc of information generation, information content, and information presentation.

## 2.6.1 | Market reaction on stock touting

To derive our baseline hypothesis on the economic impact of Internet deception, we draw upon the efficient market hypothesis (Fama, 1970) to explain the impact of information on capital markets. In the following, the economic impact of Internet deception is represented with two important stock‐related variables: the trading volume of the touted stock to consider the demand and stock returns to incorporate the willingness to pay for the advertised stock.

The efficient market hypothesis (Fama, 1970) is one of the fundamental foundations of financial research and is the theoretical basis for a wide range of research papers investigating capital market efficiency (Muntermann & Guettler, 2007; Patell & Wolfson, 1984). The efficient market hypothesis postulates that current stock prices reflect the available information, ranging from publicly available historical information (weak form), publicly available new information (semi‐strong form), and non‐public insider information (strong form)

In the context of pump and dump manipulations, the published information may be perceived by stock market participants as reliable; thus, according to the semi‐strong form of the efficient market hypothesis, this information translates into a market reaction. This also applies when considering the countermeasures against pump and dum manipulations undertaken by market surveillance authorities and enhanced spam filters (SEC, 2012c; Symantec, 2011), as deceivers have adapted strategies and publish messages in multiple channels such as regular websites and social media (SEC, 2012b). Consequently, investors confronted with these contents may rely on the informatio published and buy the recommended financial instrument. Therefore, we hypothesize:

H5a: Stock touting has an impact on traded volume

H5b: Stock touting has an impact on stock returns.

## 2.6.2 | Impact of information generation

Information generation encompasses the production of product‐related information (Xiao & Benbasat, 2011) and includes the dynamic preparation of personalized information according to a specific customer's preferences. In this context, Xiao and Benbasat (2011) mainly focus on product recommendation agents that present a specific set of products to the consumer and might therefore manipulate the results displayed. Apart from product recommendation agents, the manipulated display of online consumer reviews can be seen as another example of deception with regard to information generation. Here, manipulations can be conducted in the form of filtering negative or deliberately publishing positive online reviews

Stock touting is different from product recommendation agents. In case of a product recommendation agent, a customer searches for a product and the agent displays personalized recommendations. In the case of stock touting, an investor visits a website and reads a newsletter or social media message that recommends a specific stock. Thus stock touting is nonpersonalized with regard to the recommendation presented. Stock touting can be seen as compa rable to the display of nonpersonalized product reviews. A specific type of online review that is favourable about the product or service can be assumed to be displayed more prominently, and often, the same applies to touts related t a specific stock: different messages focusing on the stock make it more visible to a broader audience.

We consider two basic aspects in the field of nonpersonalized information generation. First, we consider the number of stock touts published. Second, we consider the campaign length, encompassing the time period durin which these stock recommendations have been published. Although Xiao and Benbasat (2011) do not directl address the question of how many times specific information is displayed (or how long a specific type of information is presented), they at least indirectly cover such information repetition in the course of information generation when considering that a specific type of information is displayed more often to a large number of customers compared wit other non‐favourable information.

A higher number of stock touts published also extends the reach of the corresponding campaign, especially when these recommendations are sent by different promoters who are followed by different groups of investors. In th context of advertising, extending a campaign's reach has proven to foster advertising success (Bellman, Schweda, & Varan, 2010). A pump and dump campaign can be assumed to profit from a higher number of promoters as well Furthermore, a higher number of exposures to an advertisement can positively affect consumers (Craig, Sternthal, & Leavitt, 1976). Additionally, an augmented exposure has positive effects on advertising recall and purchase intention for consumers with low product knowledge (Kim, Kim, Park, Sundar, & del Pobil, 2012). Thus, new product have to be advertised with more repetition (Tellis, 1997). In the context of stock touting, the messages sent addres less‐known stocks that are not traded at well‐known exchanges. Exposure to these recommendations can hav positive effects, ie, supporting the decision to buy the stock (Zielske, 1959). Thus, we hypothesize:

H6a: More stock touts published positively influences the traded volume.

H6b: More stock touts published positively influences the stock return.

Although a high number of stock touts published can generally be assumed to have a positive influence on the deci sion to buy a stock, this relationship should be curvilinear: an excessive number of stock touts published might also raise suspicion (Aune, Levine, Park, Asada, & Banas, 2005; Vrij, 2000; Vrij, Edward, Roberts, & Bull, 2000). When deceivers try too hard to convince investors, the behaviour might be the reverse: the market reaction will be reduced. Consequently, we hypothesize:

H6c: If too many stock touts are published, trading volume decreases.

H6d: If too many stock touts are published, stock returns decrease.

Closely related to the number of stock recommendations sent is the question what time span an advertising campaig should last. Previous research illustrates that a campaign is more effective when it consists of a series of advertisements (Unnava & Burnkrant, 1991; Zielske, 1959). In the case of stock touting, advertising success should depend on the question whether all messages are published during 1 day or whether different days are covered. Thus, w hypothesize:

H7a: A longer campaign length positively influences the traded volume.

H7b: A longer campaign length positively influences the stock return.

## 2.6.3 | Impact of information content

Information content encompasses the actual information transmitted by means of stock touting. In this respect, th manipulation of information content can refer to the withholding of negative or the explicit inclusion of positive infor mation (Xiao & Benbasat, 2011). Falsification of information content can, for instance, be conducted by writing “positiv reviews about products and services”, thereby providing a too‐positive view of a product (Xiao & Benbasat, 2011, p. 173)

Pump and dump campaigns fit this definition because they aim at transmitting a positive impression related to a specific stock; therefore, they exaggerate the stock's expected future performance (SEC, 2012b). Thus, we especially focus on emotive information to investigate the impact of information content on the success of Internet deception

Previous research from the perspective of advertising campaign effectiveness also outlines that emotions play an important role in increasing consumers' product attention and product recall (Chandy, Tellis, MacInnis, & Thaivanich, 2001). This finding especially holds in comparison to advertisements with low emotional content (Heath & Hyder, 2005). In general, advertisers aim at communicating a positive view related to a product to have an impact on consumers and to achieve the product's purchase (Sonnier, McAlister, & Rutz, 2011). For instance, an analysis of stock fund ads showed that evaluations of past returns were included in case of good performance but excluded after a market crash (Mullainathan, Schwartzstein, & Shleifer, 2008). In the financial context, behavioural finance theory supports the role of sentiment on financial markets since it assumes that investors also trade because of irrationa expectations that are evoked by factors such as sentiment (de Bondt, 1998). In this case, it has already been found for non‐deceptive messages that investors are influenced by the tone of the discussions related to certain financia instruments expressed in mainstream media (Tetlock, 2007), message boards (Antweiler & Frank, 2004), or Twitter (Bollen & Huina, 2011). Thus, we formulate that in the case of stock touting, more positive information content in the form of more positive sentiment has a positive influence on the corresponding market reaction:

H8a: Positive sentiment expressed within stock touts positively influences the traded volume.

H8b: Positive sentiment expressed within stock touts positively influences the stock return.

## 2.6.4 | Impact of information presentation

Information presentation encompasses the utilization of different forms of presentation or media to present the information so users are enabled to make better sense of the information displayed and to enable decision making Deceivers might therefore highlight parts of a text, make the presentation emotionally interesting for the reader, or even lead the reader's interest towards irrelevant information (Xiao & Benbasat, 2011). In the context of stock touting, deceivers might try to increase the readers' attention by using bold fonts or by including headlines, for instance, to further outline a stock's positive prospects.

Previous research has shown that the utilization of different presentation forms fosters consumer involvement (Jiang & Benbasat, 2007). Furthermore, readers usually give greater weight to specifically highlighted information compared with information given in the text (Bone & France, 2001). This fact also leads to an increased amount of time people spend processing the displayed information (Danaher et al., 2006). Consequently, if stock touts contain more elements that catch an investor's attention and that highlight the information presented, the investor takes more time to consider the message, is more convinced by the stock recommendation, and finally decides to bu the stock. Consequently, we hypothesize

H9a: Information highlighting within stock touts positively influences the traded volume.

H9b: Information highlighting within stock touts positively influences the stock return.

## 2.6.5 | Control variables

To control for other aspects potentially influencing the impact of stock touting, we control for corporate disclosures published during the campaign (C1) as they might have an influence on the financial market reaction, for instance when reporting on the future prospects of the stock. Furthermore, we include industry (C2) and time effects (C3) within our research model. Potential stock‐related aspects are taken into account within the statistical analysis by clustering the standard errors accordingly.

## 3 | RESEARCH METHODOLOGY

## 3.1 | Dataset acquisition

To investigate the confirmability of the positive prospects promised by stock touts, the characteristics of touted stocks, and the economics of stock touting, we acquired data from different sources. First, we compiled a dataset of stock touts. We also acquired the corresponding stock closing prices to determine the corresponding market reaction. Furthermore, we acquired stock and company information related to the touted stocks and to a contro sample of non‐touted stocks. Finally, we acquired corporate disclosures and financial news for the companies touted

As a source for stock touts, we selected specific stock touts matching criteria published by the SEC (SEC, 2012b) from the “Newsletters Hub” of the website http://newsletter.hotstocked.com/newsletters. This website does not publish its own stock recommendations but collects and aggregates different third‐party stock recommendations published via e‐mail as well as on websites and in social media, which ensures that an adequate audience is covered.

In contrast to pump and dump market manipulations solely distributed via e‐mail, in which each undesired message received is often seen as deceptive, it is more difficult to identify deceptive stock touts published in the Internet. In this case, the intention of the corresponding author, ie, the question of whether the stock price shall be manipulated, cannot be observed directly. To identify messages in the newsletters hub which are suspicious to be deceptive we follow the SEC guidelines that warn investors of pump and dump stock recommendations (SEC, 2012a, 2012b). Examples of suspicious content, as defined by the SEC, are given in Table 1. In this context, the stock tout must address stocks that are traded on low‐regulated markets, such as Pink Sheets or the OTC Bulletin Board (Hanke & Hauser, 2008), and each message must urge readers to buy the stock, as indicated by statements such as “anothe winner to buy now” or “new spotlight stock”. Furthermore, the messages contain vague disclaimers matching criteria published by the SEC. Here, the SEC gives the following examples: “From time to time, XYZ Newsletter may receive compensation from companies we write about”, “From time to time, XYZ Newsletter or its officers, directors, or staf may hold stock in some of the companies we write about”, or “XYZ Newsletter receives fees from the companies we write about in our newsletter” (SEC, 2012a).

To determine the market impact of stock touting, we also acquired the corresponding financial market information. Therefore, we downloaded the corresponding daily stock closing prices from Yahoo! Finance. We included only those stock touts in our dataset for which corresponding daily stock closing prices could be retrieved. This method reduced the total number of available suspicious stock recommendations as for some stocks, no daily prices were available. Our sample contains 1299 suspicious stock recommendations covering 221 stocks recommended in 25 campaigns by 156 publishers from 12/16/2010 to 04/09/2012.

TABLE 1 Examples of suspicious elements in stock touts as defined by the SEC

<table><tr><td>Element</td><td>Example</td></tr><tr><td>Statement urging the reader to buy the stock</td><td>“Another winner to buy now”“A new spotlight stock”“Shares can multiply dramatically in value over short time periods”“Wake Up, Put It On Your Screen NOW”</td></tr><tr><td>Vague disclaimer matching SEC criteria</td><td>“From time to time, XYZ Newsletter may receive compensation from companies we write about”“From time to time, XYZ Newsletter or its officers, directors, or staff may hold stock in some of the companies we write about”“XYZ Newsletter receives fees from the companies we write about in our newsletter”</td></tr></table>

Furthermore, to identify the characteristics of touted vs non‐touted stocks, we acquired a control sample of non‐touted stocks. Because the touted stocks are traded on low‐regulated over‐the‐counter (OTC) market segments we selected a random control sample with the same number of stocks from this market segment. For bot samples, we acquired the appropriate stock and company information from the OTCMarkets platform otcmarkets.com

Finally, we searched for related corporate disclosures and financial news published from 1 week before the campaign until 1 month after the campaign using the OTCMarkets platform that aggregates these news from different sources, thereby providing comprehensive news coverage. These news items are used to analyse whether the positive prospects promised in stock touts can actually be confirmed.

## 3.2 | Event study

To determine the stock market reaction caused by stock touting, we made use of event study methodolog (MacKinlay, 1997) which determines the impact of a certain event on stock returns. In this context, the event window denotes the period in which the event takes place, ie, the time when stock touts are published. We required that the stock touts are published within a maximum period of one trading week. This discards cases with too much tempora distance between the different touts.

The market impact during the event window was determined by calculating abnormal returns which are defined as “the actual ex post return of the security over the event window minus the normal return of the firm over the window” (MacKinlay. 1997, p. 15). Thus, the proportion of the return is calculated which can be attributed to the event. Therefore, the normal return, which is defined as “the expected return without conditioning on the event taking place” (MacKinlay, 1997, p. 15), is determined. In this study, we estimated normal returns by means of the constant mean return model (MacKinlay, 1997), which assumes that the normal return equals the mean return of the security during the estimation window. To specify the estimation window, we followed Böhme and Holz (2006 and skipped the 3 trading days preceding the campaign and selected the previous 30 trading days to estimate th mean returns. Consequently, we avoided that the event was included in the estimation window. In addition, we onl analysed stocks that had not been targeted by a pump and dump campaign within the preceding 4 months to eliminate interdependencies between different campaigns.

The constant mean return model was selected as it has been shown to be most appropriate for determining the market impact in the field of thinly traded stocks (Böhme & Holz, 2006; MacKinlay, 1997). Furthermore, this ensures comparability with previous research in the context of pump and dump market manipulations. As our event covers several days, we aggregated the daily abnormal returns during the event window (car\_event). To calculate the impact after the pump and dump campaign has ended, we further determined the average cumulated abnormal returns fo the next 20 trading days following the event

In Equations (1) to $( 3 ) , R _ { i t }$ denotes the actual return for stock i on day t which is determined by taking into account the closing prices P for stock i on day t and $t \mathrm { ~ - ~ } 1 . \mathsf { A } R _ { i t }$ is the abnormal return for stock i on day t, considering the mean return over the estimation window R . $C A R _ { i } ( T _ { 1 } , T _ { 2 } )$ is the cumulative abnormal return between day $T _ { 1 }$ and day $T _ { 2 } .$ Thereby, we define car\_event as $C A R _ { i } ( T _ { 1 } , T _ { 2 } )$ with $\tau _ { 1 }$ defined as the first day of the campaign and $T _ { 2 }$ defined as the last day of the campaign.

$$
R _ {i t} = \frac {P _ {i t} - P _ {i t - 1}}{P _ {i t - 1}}\tag{1}
$$

$$
A R _ {i t} = R _ {i t} - \overline {{R _ {i}}}\tag{2}
$$

$$
C A R _ {i} (T _ {1}, T _ {2}) = \sum_ {t = T _ {1}} ^ {T _ {2}} A R _ {i t}\tag{3}
$$

In order to determine the impact on the traded volume, we calculated the cumulative abnormal volume based on the same methodology and included the logarithm of this resulting variable within our analyses (cvol\_event).

As a robustness check, we also evaluated different parameterizations of the event study. For instance, our results remain robust when a gap of 10 days between estimation window and event window is chosen or when the distance to a previous pump and dump campaign is set to 1, 2, or 3 months. However, if the distance between two pump and dump campaigns is diminished, the significance of the results is reduced, which might be caused by the fact that the touted stocks are well-known to investors and that interested investors have already traded the related stocks with the result that abnormal returns are diminished.

## 3.3 | Content analysis

Content analysis makes “inferences from a symbolic medium, usually texts” by classifying “textual material, reducing it to more relevant, manageable bits of data” (Weber, 1983). Within this study, we performed different analyses using the stock touts' contents. First, we manually determined the topic categories discussed in the stock‐touting campaigns as well as in the corresponding corporate disclosures and financial news to analyse whether the positive prospects reported could actually be confirmed.

Furthermore, to measure the impact of the sentiment expressed, we followed an automated dictionary‐based sentiment analysis approach that determines sentiment by incorporating a dictionary of sentiment‐bearing words Within the financial domain, such dictionary‐based approaches have often been applied and have proven to be prom ising (Loughran & McDonald, 2011; Tetlock, 2007; Tetlock, Saar‐Tsechansky, & Macskassy, 2008). Furthermore, i comparison to a machine learning‐based approach, no gold‐standard corpus of labelled documents for classifier train ing is necessary.

We used the well‐established dictionary of the General Inquirer (Stone, Bales, Namenwirth, & Ogilvie, 1962), including word lists of positive and negative expressions. This practice is advantageous due to the dictionary's exten sive previous validation (Weber, 1990). Furthermore, since the dictionary is publicly available, automated coding of documents is transparent, and results can be reproduced easily (Krippendorff, 2013)

To calculate the sentiment for each pump and dump campaign, we first determined the sentiment of the suspicious stock recommendations. We obtained the occurrences of positive and negative words by comparing each document with the positive and negative word lists. Examples for positive and negative terms are “rally” and “volatile”, respectively. We followed Loughran and McDonald (2011) and reversed a word's interpretation if it was preceded by a negation. Then, we adapted three document‐level sentiment measures (Equations (4)‐(6)), positivity and negativity, representing ratios of positive (pos) and negative (neg) words related to the total words (n) of a document and polarity, which determines the sentiment's direction (ie, from negative to positive) and its strength (Tetlock et al., 2008; Zhang & Skiena, 2010). If a document contains neither positive nor negative words, polarity is defined as zero. Thereafter, for each campaign, the average of these measures related to the documents contained was calculated and used within the following analysis

$$
p o s i t i v i t y = \frac {p o s}{n}\tag{4}
$$

$$
n e g a t i v i t y = \frac {n e g}{n}\tag{5}
$$

$$
\text { polarity } = \frac {\text { pos - neg }}{\text { pos } + \text { neg }}\tag{6}
$$

To analyze the information presentation within the pump and dump campaigns, we determined the number of highlighted elements in the document by analyzing the hypertext markup language. Thereby, we determined th number of tags indicating bold texts and headlines to measure the number of elements used to catch the readers attention (Xiao & Benbasat, 2011). The results remain robust if images are included as well, but because images are often included due to formatting reasons, we report the results considering the textual highlights. For each campaign we calculated the average score and included this variable within our analysis.

## 3.4 | Variable operationalization

Table 2 summarizes the variables that this study focused on and overviews variable operationalization. We distinguish between variables related to the confirmability of the positive prospects touted, the characteristics of touted stocks, as well as variables related to the economic impact of stock touting. The specific methodology on how to determine the different variables is provided within the previous section.

## 3.5 | Regression analysis

In order to explain which factors determine the logarithm of the cumulative abnormal volume (cvol\_event) and th cumulative abnormal returns measured during the event window (car event), we estimated different ordinary least squares regressions using robust standard errors clustered at stock level. As explanatory variables, we included count which is defined as the number of recommendations published within the campaign, no\_promoters which denotes the number of distinct promoters publishing the recommendations, days which denotes the difference between the beginning and the end of the campaign in days (eg, days = 0 denotes a stock touting campaign lasting for 1 day), polarity, positivity as well as negativity which denote the different sentiment measures and highlights representing the amount of highlights within the text (ie, bold texts and headlines). Furthermore, we include the different control variables.

TABLE 2 Variable operationalization

<table><tr><td>Focus</td><td>Research Hypothesis</td><td>Variable</td><td>Description</td></tr><tr><td>Confirmability of stock touts</td><td>H1</td><td>Topic categories</td><td>Different topic categories determined by manual analysis (Table 3).</td></tr><tr><td rowspan="7">Characteristics of touted stocks</td><td>-</td><td>Market capitalization</td><td>Market capitalization of the touted stock (in millions).</td></tr><tr><td>H2</td><td>Authorized shares</td><td>Number of stocks that the company can issue (in millions).</td></tr><tr><td></td><td>Shares outstanding</td><td>Number of stocks issued by the company (in millions).</td></tr><tr><td></td><td>Free float</td><td>Number of stocks available for trading on the market (in millions).</td></tr><tr><td>H3</td><td>Age</td><td>Age of the issuing company in years.</td></tr><tr><td></td><td>Renamed</td><td>Dummy variable indicating whether the issuing company has been renamed.</td></tr><tr><td>H4</td><td>SEC-reporting</td><td>Dummy variable indicating whether the issuing company reports according to SEC standards.</td></tr><tr><td rowspan="12">Economic impact of stock touting</td><td>H5</td><td>car_event</td><td>Aggregated abnormal return during the stock touting campaign.</td></tr><tr><td></td><td>cvol_event</td><td>Logarithm of the aggregated abnormal volume during the stock touting campaign.</td></tr><tr><td>H6</td><td>count</td><td>Number of messages sent during the stock touting campaign.</td></tr><tr><td></td><td>no_promoters</td><td>Number of promoters being active during the stock touting campaign.</td></tr><tr><td>H7</td><td>days</td><td>Difference between the beginning and the end of the campaign in days.</td></tr><tr><td>H8</td><td>polarity</td><td>Sentiment polarity of a stock tout (averaged per campaign).</td></tr><tr><td></td><td>positivity</td><td>Ratio of positive words related to the total words of a stock tout (averaged per campaign).</td></tr><tr><td></td><td>negativity</td><td>Ratio of negative words related to the total words of a stock tout (averaged per campaign).</td></tr><tr><td>H9</td><td>highlights</td><td>Amount of highlighted elements in a stock tout (averaged per campaign).</td></tr><tr><td>C1</td><td>disclosure</td><td>Dummy variable indicating whether corporate disclosures were published during the campaign.</td></tr><tr><td>C2</td><td>industry</td><td>Dummy variables to control for the company&#x27;s industry.</td></tr><tr><td>C3</td><td>time</td><td>Dummy variables to control for monthly time-effects.</td></tr></table>

## 4 | EMPIRICAL STUDY

## 4.1 | Confirmability of stock touts

Table 3 reports the results of our analysis of the positive prospects touted per campaign and the number of topics confirmed by corporate disclosures and financial news. Focusing on the different topics discussed, we find that stock touts mainly report on positive prospects such as outstanding product or service developments (27.78%), genera positive business opportunities (33.73%), and potential acquisitions (11.11%). As already outlined, the stock touts urge readers to buy the stock since the positive prospects are claimed to materialize within short periods of time.

In all cases, if these positive prospects prevail or materialize, they are also expected to be reported by the affected companies within corporate disclosures and by journalists within financial news. Nevertheless, our analysis of these reliable information sources shows that the positive prospects are rarely confirmed by corporate disclosures or financial news. For instance, only 0.40% of all cases report on outstanding product or service developments, and only 0.79% report on new contract agreements. This result is similar for other categories. Consequently, we find sup port for H1 because the positive prospects touted are rarely confirmed by corporate disclosures and financial news

## 4.2 | Characteristics of touted stocks

To investigate whether stocks with specific characteristics are preferred for stock touting, we compare the touted stocks within our sample with our control sample of non‐touted stocks. Because the companies from both samples are traded on the same marketplace and thus match the SFC criterion to be small and thinly traded stock (SEC, 2012a), valid conclusions can be drawn from the comparison of both samples.

The resulting company and stock characteristics are presented in Table 4. As seen from the table, the companie covered are comparable regarding the most important characteristic of pump and dump campaigns. Both have a comparably low market capitalization of approximately 1 million US Dollars (median). Nevertheless, the other stoc characteristics show significant differences (Wilcoxon rank‐sum test for equality of medians).

Related to the question of how conveniently a stock can be traded, the number of authorized shares and the number of shares outstanding are higher in case of touted stocks compared with control sample stocks. This findin is notable because the market capitalization of the touted and control sample stocks is similar, Conseguently, the touted stocks are more convenient to trade. Most important, the free float of the touted stocks is higher than th free float within the control sample. This result shows that—once manipulators have increased the attention related to a stock—they ensure that the stock can be bought. Consequently, H2 is supported

Furthermore, our results confirm that manipulators avoid sending signals of anomaly as they focus on more recently established companies when compared with the control sample. Moreover, the targeted companies have more often been renamed within the past. This finding shows that manipulators prefer to focus on more recently funded companies with a shorter history (H3 supported). Finally, we observe that manipulators focus on companies following SEC reporting standards rather than reporting according to less‐strict alternative reporting standards (73% versus 36%). As follows, H4 can be supported as well.

TABLE 3 Topic categories of stock touting campaigns

<table><tr><td>Category</td><td>Definition</td><td>Examples</td><td colspan="2">Touted in Campaigns</td><td colspan="2">Reported by News/Corp. Disclosures</td></tr><tr><td>Product or service</td><td>Reports on outstanding product or service developments</td><td>“They have solved the puzzle”“Intends to establish itself and its technology as an industry standard”</td><td>70</td><td>27.78%</td><td>1</td><td>0.40%</td></tr><tr><td>Contract</td><td>Reports on contracts with third parties in order to distribute products or services</td><td>“Finalizes major distribution deal with European pharmatech company”“One big contract news could send the company soaring”</td><td>26</td><td>10.32%</td><td>2</td><td>0.79%</td></tr><tr><td>Acquisition</td><td>Reports on acquisition</td><td>“Signed a letter of intent to acquire a competitor”“Enters agreement to buy call center”</td><td>28</td><td>11.11%</td><td>0</td><td>0.00%</td></tr><tr><td>Financial results</td><td>Reports on financial results</td><td>&quot;On track to complete the fiscal year by more than doubling revenue over last year”“On target to produce record third quarter revenue and anticipates a full year profit”</td><td>8</td><td>3.17%</td><td>1</td><td>0.40%</td></tr><tr><td>Financing</td><td>Reports on corporate financing</td><td>“2.5 million dollar funding commitment on a joint venture”“$10 million financing arrangement secured”</td><td>11</td><td>4.37%</td><td>0</td><td>0.00%</td></tr><tr><td>General opportunity</td><td>Reports on general business opportunities</td><td>“Major oil discovery in the southern United Kingdom began to circulate near where the company has been developing”“A Potential Half-Billion Dollar Discovery”</td><td>85</td><td>33.73%</td><td>7</td><td>2.77%</td></tr><tr><td>Undefined</td><td>No specific reasons given</td><td>“We see lots of potential in this play”“Intrinsically undervalued stock”</td><td>24</td><td>9.52%</td><td>0</td><td>0.00%</td></tr></table>

## 4.3 | Economic impact of stock touting

In the following, we first present our event study results focusing on the economic impact of stock touting. Thereafter, we investigate the influence of the different information practices on the observed economic impact.

## 4.3.1 | Descriptive results

Table 5 shows the descriptive statistics of our sample. The 252 stock touting campaigns in our sample are, o average, composed of five messages sent out by approximately two promoters over 1.869 days, whereas the longest campaign in the sample covers a period of 5 days. In total, 157 promoters have published the stock touts. Furthermore, the most comprehensive campaign advertising a stock consists of 42 messages and is carried out by 14 promoters.

Considering the number of messages sent and the number of promoters conducting a stock touting campaign seems appropriate for explaining the campaign impact. Focusing on the sentiment measures, the average sentiment polarity is 0.459. This finding shows that the messages sent contain a positive sentiment, which is also indicated b the positivity score of 0.057, which exceeds the amount of negativity contained in the pump and dump messages (0.020). Interestingly, each stock recommendation contains approximately eight highlights showing that the publishers of stock touts make use of this feature.

TABLE 4 Characteristics of touted and non‐touted stocks in the control sample

<table><tr><td rowspan="2" colspan="2"></td><td colspan="4">Touted Stocks</td><td colspan="4">Non-Touted Stocks</td><td></td></tr><tr><td>Min</td><td>Mean</td><td>Median</td><td>Max</td><td>Min</td><td>Mean</td><td>Median</td><td>Max</td><td>P-Value</td></tr><tr><td rowspan="4">H2</td><td>Market capitalization</td><td>0</td><td>12.7</td><td>1.0</td><td>286</td><td>0</td><td>261</td><td>1.1</td><td>23500</td><td>0.350</td></tr><tr><td>Authorized shares</td><td>25</td><td>1390</td><td>500</td><td>18000</td><td>1.4</td><td>806</td><td>150</td><td>10000</td><td>0.000***</td></tr><tr><td>Shares outstanding</td><td>0.5</td><td>491</td><td>109</td><td>15000</td><td>0</td><td>138</td><td>37.5</td><td>4700</td><td>0.000***</td></tr><tr><td>Free float</td><td>0</td><td>338</td><td>57.6</td><td>6530</td><td>0</td><td>168</td><td>8.6</td><td>4550</td><td>0.000***</td></tr><tr><td rowspan="2">H3</td><td>Age</td><td>4</td><td>12.89</td><td>9</td><td>68</td><td>1</td><td>22.15</td><td>14</td><td>113</td><td>0.030**</td></tr><tr><td>Renamed</td><td>0</td><td>0.7273</td><td>1</td><td>1</td><td>0</td><td>0.6234</td><td>1</td><td>1</td><td>0.052*</td></tr><tr><td>H4</td><td>SEC-reporting</td><td>0</td><td>0.7338</td><td>1</td><td>1</td><td>0</td><td>0.3636</td><td>0</td><td>1</td><td>0.000***</td></tr></table>

Note: Free float, authorized shares, shares outstanding, market capitalization in millions.  
\*P < 10%. \*\*P < 5%. \*\*\*P < 1%.

TABLE 5 Means, standard deviations, (SD) and correlations

<table><tr><td></td><td>Variable</td><td>Mean</td><td>SD</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>1</td><td>car_event</td><td>0.09</td><td>0.41</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>cvol_event</td><td>2.22</td><td>7.53</td><td>0.23</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>count</td><td>5.16</td><td>6.19</td><td>0.19</td><td>0.43</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>no_promoters</td><td>2.71</td><td>2.60</td><td>0.20</td><td>0.41</td><td>0.83</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>days</td><td>0.87</td><td>1.21</td><td>0.14</td><td>0.43</td><td>0.42</td><td>0.35</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td>polarity</td><td>0.46</td><td>0.19</td><td>0.17</td><td>0.01</td><td>-0.02</td><td>0.02</td><td>-0.08</td><td>1</td><td></td><td></td><td></td></tr><tr><td>7</td><td>positivity</td><td>0.06</td><td>0.01</td><td>0.17</td><td>-0.01</td><td>-0.02</td><td>0.01</td><td>-0.09</td><td>0.45</td><td>1</td><td></td><td></td></tr><tr><td>8</td><td>negativity</td><td>0.02</td><td>0.01</td><td>-0.05</td><td>-0.02</td><td>-0.03</td><td>-0.06</td><td>-0.03</td><td>-0.63</td><td>0.18</td><td>1</td><td></td></tr><tr><td>9</td><td>highlights</td><td>7.53</td><td>20.18</td><td>-0.13</td><td>-0.02</td><td>-0.16</td><td>-0.17</td><td>-0.06</td><td>0.12</td><td>0.02</td><td>-0.09</td><td>1</td></tr></table>

Table 5 also shows the correlations of the different variables. The number of promoters being active during a campaign (no\_promoters) and the number of messages sent (count) are highly correlated. Thus, we include only on of these variables at the same time within our further analysis. In addition, high correlations among polarity and positivity and negativity can be observed as these variables each measure the campaign sentiment

## 4.3.2 | Market reaction on stock touting

The distribution of the cumulative abnormal returns during the event window is depicted in Figure 2. Thereby, we first confirm a result that has also been reported for stock spam sent via e‐mail (Böhme & Holz, 2006; Nelson et al., 2009). Although the mean cumulative abnormal event window return (car\_event) is above zero (mean: 8.7%, median: 2.0%), cases also exist in which car\_event is negative, probably caused by market participants selling th stocks already during the campaign.

Overall, since a Wilcoxon signed‐rank test for equality of medians reports that the median of car\_event is significantly different from zero at a 1% level of significance, our sample campaigns still affect capital markets although the SEC has issued several warnings and spam filters have been constantly improved. Focusing on the cumulative abnormal trading volume, we observe that the average trading volume during the campaigns is

![](/api/attachments/4A8P7N67/fulltext/images/9a1701041fc1110d29aa6ac2f15549ecf43e512785207be7cb406837676c40a7.jpg)  
FIGURE 2 Distribution of cumulative abnormal returns during the stock touting campaign event window (car\_event)

28.81 times higher than in normal cases (Wilcoxon signed‐rank test: significantly different from zero at the 1% level). Thus, hypotheses H5a and H5b are supported.

Furthermore. to investigate whether investors buving the touted stocks are confronted with potentia losses, we consider the developments after the event window when the stock touting has ended. Therefore, we calculated the average cumulative abnormal returns beginning from the last message published for the following 20 trading days. As shown in Figure 3, we find on average cumulative abnormal returns of −20.60% within the first 5 days, −30.11% within the first 10 days, and − 47.40% within the first 20 trading days after stock touting has ended. These values are different from zero at a 1% level of significance. We therefore find a massive price decrease after the campaign has ended, which may be caused by manipulators or private investors selling the advertised stocks. This result also underlines that the positive corporate prospects advertised by the stock touts in our sample do not prevail and supports that the stock touts at hand are used to foster a false belief.

![](/api/attachments/4A8P7N67/fulltext/images/935cdf41ef440634776aba0338002c452ebb09d22efcda7d26c01250cd8ad450.jpg)  
FIGURE 3 Time series of average cumulative abnormal returns (CAR) after the end of the stock touting campaign

## 4.3.3 | The impact of deceptive information practices on traded volume

To investigate the impact of deceptive information practices on traded volume, we run four different regressions, considering information generation, information content, and information presentation, to explain the logarithm of the cumulative abnormal trading volume during the campaign (cvol\_event). We run these regressions to evaluate H6a by incorporating either the number of messages sent or the number of promoters publishing a stock recommendation (due to a high correlation of both variables, we include only one at the same time). Furthermore, we test H7a b including the number of days of each advertising campaign. To examine H8a, we consider the sentiment polarity measure and the positivity and negativity measures to investigate the campaign sentiment's impact on the capita market's reaction. Finally, to investigate H9a, we include the average number of highlights within each message.

The results of the impact of deceptive information practices on the cumulative abnormal trading volume during the campaign are presented in Table 6. The results clearly illustrate that information generation has a significant impact on the success of the deceptive information practices. This finding is shown in regressions (1) to (4) by th positive impact of the number of messages published, the number of promoters publishing these messages, and the number of days the campaign lasts. Throughout the regressions, H6a and H7a are supported at a 1% level of sig nificance. Consequently, we find that increasing the potential exposure of Internet users to the recommended stock has a positive effect on the success of a pump and dump campaign. Nevertheless, H6c is partially supported as well The publication of too many stock touts reduces the positive effect of additional messages (significant at a 5% leve of significance). However, if nonpersonalized information generation is measured using the number of promoters, we find no significant negative influence. Overall, when considering the coefficients and the mean variable scores the relative impact of the number of stock touts is higher than the impact of the campaign length since the average number of stock touts published is five, whereas the average campaign has a duration of approximately 2 days.

Interestingly, neither information content nor information presentation has a significant influence on th cumulative abnormal trading volume. The corresponding coefficients are not significant throughout the different regressions (H8a and H9a are not supported). This finding indicates that the mere presence of stock recommendations representing new information to Internet users increases their demand and leads them to invest in the appro priate stock—despite the specific information content or information presentation.

TABLE 6 OLS regression results for explaining cumulative abnormal trading volume during the stock touting campaign

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">(1) #Touts, Sentiment Polarity</td><td colspan="2">(2) # Promoters, Sentiment Polarity</td><td colspan="2">(3) #Touts, Positivity/Negativity</td><td colspan="2">(4) #Promoters, Positivity/Negativity</td></tr><tr><td>Coeff.</td><td>P-value</td><td>Coeff.</td><td>P-value</td><td>Coeff.</td><td>P-value</td><td>Coeff.</td><td>P-value</td></tr><tr><td colspan="2">constant</td><td>1.455</td><td>0.016**</td><td>1.475</td><td>0.026**</td><td>1.500</td><td>0.018**</td><td>1.469</td><td>0.030**</td></tr><tr><td rowspan="2">H6a</td><td>count</td><td>0.172</td><td>0.000***</td><td></td><td></td><td>0.174</td><td>0.000***</td><td></td><td></td></tr><tr><td>no_promoters</td><td></td><td></td><td>0.292</td><td>0.003***</td><td></td><td></td><td>0.299</td><td>0.002***</td></tr><tr><td rowspan="2">H6c</td><td>count $^{2}$ </td><td>-0.003</td><td>0.003***</td><td></td><td></td><td>-0.003</td><td>0.004***</td><td></td><td></td></tr><tr><td>no_promoters $^{2}$ </td><td></td><td></td><td>-0.011</td><td>0.182</td><td></td><td></td><td>-0.012</td><td>0.168</td></tr><tr><td>H7a</td><td>days</td><td>0.373</td><td>0.000***</td><td>0.472</td><td>0.000***</td><td>0.369</td><td>0.000***</td><td>0.470</td><td>0.000***</td></tr><tr><td rowspan="3">H8a</td><td>polarity</td><td>-0.045</td><td>0.919</td><td>-0.110</td><td>0.803</td><td></td><td></td><td></td><td></td></tr><tr><td>positivity</td><td></td><td></td><td></td><td></td><td>-2.068</td><td>0.677</td><td>-2.247</td><td>0.653</td></tr><tr><td>negativity</td><td></td><td></td><td></td><td></td><td>2.513</td><td>0.748</td><td>3.907</td><td>0.615</td></tr><tr><td>H9a</td><td>highlights</td><td>0.004</td><td>0.382</td><td>0.003</td><td>0.474</td><td>0.004</td><td>0.361</td><td>0.003</td><td>0.448</td></tr><tr><td>C1</td><td>disclosure</td><td>0.048</td><td>0.849</td><td>0.008</td><td>0.974</td><td>0.057</td><td>0.826</td><td>0.014</td><td>0.957</td></tr><tr><td>C2</td><td>industry effects</td><td colspan="2">included</td><td colspan="2">included</td><td colspan="2">included</td><td colspan="2">included</td></tr><tr><td>C3</td><td>time effects</td><td colspan="2">included</td><td colspan="2">included</td><td colspan="2">included</td><td colspan="2">included</td></tr><tr><td colspan="2">F</td><td>8.206</td><td>0.000***</td><td>9.735</td><td>0.000***</td><td>7.793</td><td>0.000***</td><td>9.364</td><td>0.000***</td></tr><tr><td colspan="2">R $^{2}$ </td><td></td><td>0.367</td><td></td><td>0.353</td><td></td><td>0.368</td><td></td><td>0.354</td></tr><tr><td colspan="2">Adjusted R $^{2}$ </td><td></td><td>0.306</td><td></td><td>0.291</td><td></td><td>0.303</td><td></td><td>0.288</td></tr></table>

Note: Standard errors clustered by stock.  
\*P < 10%. \*\*P < 5%. \*\*\*P < 1%.

Corporate disclosures do not have a significant impact on the cumulative abnormal trading volume measured This result might be attributed to the fact that the targeted companies do not have an appropriate public exposur and analyst coverage so their disclosures do not have an additional impact or, as already discussed, no relevant corporate news is published.

To further evaluate the goodness of our results and to test for multicollinearity, we calculated the variance inflation factor for each independent variable, and no multicollinearity was detected (O'Brien, 2007). Furthermore, the F‐scores of regressions (1) to (4) show that the hypothesis that none of the independent variables influences the cumulative abnormal return during the event window can be rejected at a 1% level of significance Considering the adjusted $R ^ { 2 }$ of the different regressions, approximately 30% of the variance can be explained by the different models.

## 4.3.4 | The impact of deceptive information practices on stock returns

Next to the impact of deceptive information practices on the cumulative abnormal trading volume, we also conside the impact on the cumulative abnormal return measured during the event, ie, while the stock touts are sent (Table 7).

As illustrated in Table 6, regressions (1) to (4) indicate that, in contrast to cumulative abnormal volume, information generation has no significant influence on the cumulative abnormal return. Thus, neither a high number of messages sent nor an increased number of promoters publishing stock touts influences the stock price reactions (H6b and H6d not supported). Considering the number of days the advertising campaign lasts, we also find no significant influence on the subsequent capital market reaction. As a result, research hypothesis H7b is not supported.

TABLE 7 OLS regression results for explaining cumulative abnormal returns (car\_event) during the stock touting campaign

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">(1) # Touts, Sentiment Polarity</td><td colspan="2">(2) # Promoters, Sentiment Polarity</td><td colspan="2">(3) #Touts, Positivity/Negativity</td><td colspan="2">(4) #Promoters, Positivity/Negativity</td></tr><tr><td>Coeff.</td><td>P-value</td><td>Coeff.</td><td>P-value</td><td>Coeff.</td><td>P-value</td><td>Coeff.</td><td>P-value</td></tr><tr><td colspan="2">constant</td><td>-0.052</td><td>0.711</td><td>-0.004</td><td>0.979</td><td>-0.061</td><td>0.681</td><td>-0.012</td><td>0.944</td></tr><tr><td rowspan="2">H6b</td><td>count</td><td>-0.002</td><td>0.818</td><td></td><td></td><td>-0.005</td><td>0.656</td><td></td><td></td></tr><tr><td>no_promoters</td><td></td><td></td><td>-0.032</td><td>0.515</td><td></td><td></td><td>-0.039</td><td>0.428</td></tr><tr><td rowspan="2">H6d</td><td> $count^2$ </td><td>0.000</td><td>0.364</td><td></td><td></td><td>0.000</td><td>0.302</td><td></td><td></td></tr><tr><td> $no\_promoters^2$ </td><td></td><td></td><td>0.005</td><td>0.317</td><td></td><td></td><td>0.006</td><td>0.268</td></tr><tr><td>H7b</td><td>days</td><td>0.033</td><td>0.142</td><td>0.027</td><td>0.246</td><td>0.037</td><td>0.110</td><td>0.029</td><td>0.210</td></tr><tr><td rowspan="3">H8b</td><td>polarity</td><td>0.409</td><td>0.016**</td><td>0.400</td><td>0.018**</td><td></td><td></td><td></td><td></td></tr><tr><td>positivity</td><td></td><td></td><td></td><td></td><td>4.695</td><td>0.012**</td><td>4.668</td><td>0.012**</td></tr><tr><td>negativity</td><td></td><td></td><td></td><td></td><td>-3.037</td><td>0.122</td><td>-3.059</td><td>0.127</td></tr><tr><td>H9b</td><td>highlights</td><td>-0.003</td><td>0.020**</td><td>-0.003</td><td>0.024**</td><td>-0.003</td><td>0.041**</td><td>-0.002</td><td>0.047**</td></tr><tr><td>C1</td><td>disclosure</td><td>0.010</td><td>0.935</td><td>-0.018</td><td>0.886</td><td>0.010</td><td>0.936</td><td>-0.019</td><td>0.875</td></tr><tr><td>C2</td><td>industry effects</td><td colspan="2">included</td><td colspan="2">included</td><td colspan="2">included</td><td colspan="2">included</td></tr><tr><td>C3</td><td>time effects</td><td colspan="2">included</td><td colspan="2">included</td><td colspan="2">included</td><td colspan="2">included</td></tr><tr><td colspan="2">F</td><td>1.408</td><td>0.112</td><td>1.385</td><td>0.123</td><td>1.385</td><td>0.119</td><td>1.359</td><td>0.133</td></tr><tr><td colspan="2"> $R^2$ </td><td></td><td>0.119</td><td></td><td>0.131</td><td></td><td>0.125</td><td></td><td>0.138</td></tr><tr><td colspan="2">Adjusted  $R^2$ </td><td></td><td>0.034</td><td></td><td>0.047</td><td></td><td>0.037</td><td></td><td>0.051</td></tr></table>

Note: Standard errors clustered by stock.  
\*P < 10%. \*\*P < 5%. \*\*\*P < 1%.

Related to information content, we find that when the expressed sentiment within the campaign is more positive, the cumulative abnormal returns during the event window are higher. Consequently, research hypothe sis H8b is supported. This finding is indicated by the polarity measure included in regressions (1) and (2) as well as by the positivity and negativity measures in regressions (3) and (4). If positivity and negativity are considered, we find that mainly the use of positive sentiment‐bearing words leads to a positive impact that is significant at the 5% level whereas the coefficients of negativity are negative but not significant.

Finally, investigating the impact of information presentation on cumulative abnormal returns, we find that highlights contained in the messages have a significant negative effect. Consequently, if the publishers include more highlights in the text (for instance by an increased amount of bold font used), investors are less willing to pay a high price for the stock, thereby reducing cumulative abnormal returns. Related to hypothesis H9b, information presentation influences the market reaction, but negatively rather than positively (as initially hypothesized). Again corporate disclosures published during the campaigns have no significant influence.

Related to the economic impact, we find that the sentiment polarity has a large influence on the cumulative abnormal return, whereas an increase from zero to the maximum polarity of one would increase the cumulativ abnormal return by more than 40 percentage points. An increase from zero to the mean polarity would still result in an increase of more than 18 percentage points. By contrast, the economic impact of text highlighting is muc lower, as shown by the low coefficient.

To further evaluate the goodness of our results and to test for multicollinearity, we calculated the variance inflation factor for each independent variable and no multicollinearity was detected (O'Brien, 2007). The F‐scores of regressions (1) to (4) are comparably low, whereas this value is driven by the inclusion of the different control vari ables. If these are excluded, the results remain robust, but the E-Score is (depending on the regression configuration significant at the 1% and 5% levels, respectively. Finally, the adjusted $R ^ { 2 }$ of the different regressions shows that 3.4% to 5.1% of the variance of car\_event can be explained. This finding indicates that although the different independent variables contribute to car event, they do not have a substantial influence. This result is not uncommon due to the complex nature of returns and is indicated in related studies, in which $R ^ { 2 }$ is comparably low when abnormal returns are explained (Loughran & McDonald, 2010, 2011; Tetlock et al., 2008).

The conclusions from these regressions remain robust when we include daily dummy variables instead of controlling for the number of days (days) and when we include dummy variables for each promoter to control for promoter‐specific aspects instead of the number of promoters (no\_promoters). Moreover, we evaluated different parameterizations of the event study, which did not affect the results.

## 5 | DISCUSSION

## 5.1 | Economics of stock touting

Our study focuses on the phenomenon of stock touting during pump and dump campaigns and investigates the confirmability of stock touts, the characteristics of touted stocks, and the economic impact of stock touting. Considering the confirmability of stock touts, we find that stock touts report on positive business prospects but that these business prospects are rarely confirmed by corporate disclosures or financial news (H1, please see Table 8 for a summary of our research hypotheses). Focusing on the characteristics of touted stocks, we find that manipulators prefer stocks that are more convenient to trade, have a shorter history, and fulfil the reporting obligations of a trusted third party (please see H2‐H4). This finding shows that manipulators focus on products that are not related to signals of anomaly, so investors buy the stock. Referring to the model of deception detection by Johnson et al. (2001), this result underlines the goal of avoiding being perceived as suspicious

Related to the economic impact of stock touting (please see H5‐H9), our results show that the stock touts in ou sample cause stock market reactions. During the campaigns, we measure an average cumulative abnormal return of 8.7%. However, cases also exist in which negative cumulative abnormal returns already occur during the campaign.

TABLE 8 Summary of hypothesis testing

<table><tr><td>Focus</td><td>#</td><td>Hypothesis</td><td>Result</td></tr><tr><td>Confirmability of stock touts</td><td>H1</td><td>The positive prospects touted are not confirmed by corporate disclosures and financial news.</td><td>√</td></tr><tr><td rowspan="3">Characteristics of touted stocks</td><td>H2</td><td>Compared with non-touted stocks, touted stocks are more convenient to trade.</td><td>√</td></tr><tr><td>H3</td><td>Compared with non-touted stocks, companies issuing touted stocks have been established more recently.</td><td>√</td></tr><tr><td>H4</td><td>Compared with non-touted stocks, companies issuing touted stocks more often follow well-accepted reporting standards.</td><td>√</td></tr><tr><td rowspan="12">Economic impact of stock touting</td><td>H5a</td><td>Stock touting has an impact on traded volume.</td><td>√</td></tr><tr><td>H5b</td><td>Stock touting has an impact on stock returns.</td><td>√</td></tr><tr><td>H6a</td><td>More stock touts published positively influences the traded volume.</td><td>√</td></tr><tr><td>H6b</td><td>More stock touts published positively influences the stock return.</td><td>x</td></tr><tr><td>H6c</td><td>If too many stock touts are published, trading volume decreases.</td><td>(√)</td></tr><tr><td>H6d</td><td>If too many stock touts are published, stock returns decrease.</td><td>x</td></tr><tr><td>H7a</td><td>A longer campaign length positively influences the traded volume.</td><td>√</td></tr><tr><td>H7b</td><td>A longer campaign length positively influences the stock return.</td><td>x</td></tr><tr><td>H8a</td><td>Positive sentiment expressed within stock touts positively influences the traded volume.</td><td>x</td></tr><tr><td>H8b</td><td>Positive sentiment expressed within stock touts positively influences the stock return.</td><td>√</td></tr><tr><td>H9a</td><td>Information highlighting within stock touts positively influences the traded volume.</td><td>x</td></tr><tr><td>H9b</td><td>Information highlighting within stock touts positively influences the stock return.</td><td>x</td></tr></table>

✓ Hypothesis supported, (✓) Hypothesis partially supported ✗ Hypothesis not supported

One explanation could be that manipulators “dump” their stocks while the stock is being “pumped”. If the cumulative abnormal return within the next days after the end of the campaign is considered, we find that investors are confronted with large negative cumulative abnormal returns; consequently, they lose substantial parts of their investments if they invested during the campaign.

Focusing on the deceptive information practices performed. our results indicate that information generatior influences the demand related to a specific stock, whereas information content and information presentation influence the willingness to pay for the stock. Related to the demand for the stock, which is represented by the cumulative abnormal trading volume during the campaign, we find that a higher spread of stock touts during the campaign positivel influences the market reaction. This finding shows that Internet users buy the corresponding stock if it is advertised because they do not notice deceptive behaviour. Nevertheless, the question of how much money they are willing t pay for the stock is influenced by the information content and presentation. If the stock touts are more positive, higher cumulative abnormal returns can be observed. Interestingly, a higher level of highlights within the text leads to lowe cumulative abnormal returns, which is the opposite of what was expected. One possible explanation for this resul might be related to the model of deception detection (Johnson et al.. 2001): a higher number of highlights might be perceived by the readers as an anomaly within the text, reducing their trust towards the tout and reducing thei willingness to pay for the stock. Nevertheless, future research might further investigate the reasons for this finding.

We also observe that social media is actually used to distribute pump and dump market manipulations. A search for the ticker symbols of the touted stocks on the micro‐blogging service Twitter revealed that 41.67% of the campaigns analysed are also accompanied by recommendations of the related stocks on Twitter. However, the question of whether a stock is also recommended on Twitter has no significant influence on the following capita market reaction when we additionally control for this aspect. This finding might be explained by the fact that Twitte messages are too short to properly advertise the stock. Instead, related messages refer to the stock recommendations discussing such financial instruments in more detail.

Based on our reasoning and our analyses, we thus find different indications for deceptive behaviour resembled in the stock touts under investigation. We clarify that the general setting of stock touting during pump and dump campaigns matches the deception definition. Furthermore, the stock recommendations in our sample match th SEC criteria of “common red flags” that should be considered to avoid being affected by pump and dump market manipulations. Related to the RQs, we find that the positive prospects touted are rarely confirmed by corporate disclosures and financial news, thereby providing indications of falsification. Furthermore, guided by theory from the field of deception detection and resulting from our comparison of touted and non-touted stocks, we observe further indications for deceptive behaviour as promoters focus on stocks that are not related to signals of anomaly, ie, that do not sound too good to be true. Finally, and most importantly, our event study shows a large price decline after stock touting ends. This result provides further evidence for the false belief, ie, non‐prevailing positive prospects of the targeted stocks.

## 5.2 | Implications for research

In this study, we contribute to the literature on stock touting in the course of pump and dump campaigns in specific and to the literature on the “dark side” of information systems in the form of Internet deception in general.

We contribute to the literature by providing a comprehensive understanding of the phenomenon of stock touting. Extending previous research, we concentrate on stock touts distributed not only via e‐mail but also on websites and in social media, which ensures that an adequate audience is considered. We specifically investigat the confirmability of stock touts and show that the positive prospects promised are rarely confirmed by corporate disclosures and financial news. Thus, adapting the definition by Buller and Burgoon (1996), we provide indications that these prospects resemble a false belief that is fostered. Furthermore, we focus on the so‐far neglected product characteristics preferred by manipulators. Here, our results enhance the previous understanding, as we show the applicability of the model of deception detection by Johnson et al. (2001) in the field of stock touting. We provide new insights on whether manipulators prefer specific product characteristics when selecting financial instrument for their manipulations: they aim at avoiding signals of anomaly and focus on stocks about which Internet users hav low knowledge.

We rely on the efficient market hypothesis to hypothesize on the stock market impact during stock touting. We confirm that pump and dump campaigns are effective, thereby showing that stock touts are perceived to provid relevant information. Consequently, we observe positive mean cumulative abnormal returns during the campaign. Nevertheless, as the positive prospects rarely materialize, negative mean cumulative abnormal returns are observed after the campaign. Our study enhances the previous understanding by explicitly focusing on the economic consequences of deceptive information practices. We find that information generation influences the demand related to the manipulated stock. Furthermore, information content and information presentation influence the willingnes to pay for the stock. Consequently, we specifically adapt the concept of deceptive information practices (Xiao & Benbasat, 2011) to a novel context (ie, from electronic commerce to the field of stock touting), by focusing on nonpersonalized instead of personalized information generation.

Against the background of the increasingly pronounced role of information systems within financial markets, our study contributes to the literature by providing evidence that next to positive aspects fostering market efficiency (Currie & Lagoarde‐Segot, 2017), information systems can also cultivate behaviour negatively influencing the func tioning of financial markets. We confirm that the phenomenon of stock touting leads to effects that might impact market efficiency and reduce trust towards financial markets, thereby potentially negatively affecting the market function. Although stock touting does not necessarily depend on the availability of information systems, the Internet, in particular, eases stock touting due to its low entry barriers, anonymity, and spatial as well as temporal separation o manipulators and their targets (Xiao & Benbasat, 2011). Consequently, this study also contributes to the literature on the “dark side” of information systems by providing insights into a setting in which information systems are utilized for information manipulation.

## 5.3 | Implications for practice

From a practical perspective, our study has implications for market surveillance authorities, retail investors, and software vendors. In general, this study shows that stock touts should be considered with caution because investors bear the risk substantial parts of their investments into the financial instruments touted. When organizing their efforts to detect pump and dump market manipulations, market surveillance authorities should especially focus on financial instruments from low‐regulated markets that are easy to trade, whose issuing companies are recentl founded and follow well‐established reporting standards. Furthermore, when analysing the information published, market surveillance authorities and retail investors should especially consider stock touts that express a positive sen timent and report on positive business prospects to avoid being affected by pump and dump market manipulations

As a consequence, market surveillance authorities should be aware of information manipulation and foster activities for monitoring the web and especially social media to investigate whether deceivers try to manipulate the market by distributing false positive information. This study thus underlines that regulatory countermeasures are necessary to foster market integrity and to increase trust towards financial markets. Finally, software vendors can incorporate the results of this study to develop deception detection mechanisms that might help to detect sus picious contents and suspicious financial instruments. In this context, deception detection systems might incorporate stock characteristics and message contents related to a certain stock to detect suspicious behaviour and to protec market participants.

## 5.4 | Limitations

The stock touts studied here are published by different promoters. Thus, a campaign's success could depend on a single promoter's outreach: campaigns that are carried out by promoters and followed by many investors may have a higher impact compared with messages published by promoters with a small number of followers. To mitigate thi potential limitation, we control for the number of promoters involved in a campaign. Because the different stock recommendations are aggregated at the newsletters hub, users have the chance to notice every stock tou analysed. This leads to a comparable audience and fundamentally reduces the risk that the results are driven b single promoters.

Moreover, the dataset is acquired by selecting documents that match criteria published by the SEC Consequently, the study may not cover the entire number of available stock touts. However, the stock touts obtained lead to capital market reactions and cover a substantial number of promoters and stocks. This finding leads to the assumption that we have covered a representative number of stock touts. Furthermore, due to the event study design, we leave a gap between the estimation and event window so the influence of potential messages not covered by our data source is minimized.

Finally, the results of this study might encourage scammers to change their information practices to increase the success of their manipulations. For instance, they might alter information generation by increasing the number o sources or information content by including more positive information. Nevertheless, this would provide usefu insights for market surveillance authorities that might especially take care of such potentially fraudulent behaviou in the course of their deception detection activities.

## 5.5 | Future research

Based on our results, future research can analyse and compare the impact of pump and dump market manipulations in different countries to examine whether cultural aspects influence the effectiveness of pump and dump campaigns.

Furthermore, it could be analysed whether suspicious stock recommendations are discussed by retail investors in stock message boards and whether this behaviour influences the effectiveness of the related campaigns. Finally the results of this study might be incorporated within a predictive model in the context of deception detection to support Internet users and market surveillance authorities

## 6 | CONCLUSION

In this study, we provide insights on the confirmability of stock touts, the characteristics of touted stocks, and the economic impact of stock touting. The positive prospects promised are rarely confirmed by corporate disclosures or financial news. Manipulators are shown to prefer stocks with specific characteristics, and the impact of deceptive information practices is described. Based on the results, stock touting during pump and dump campaigns can be seen to be a risk for Internet users because they might lose substantial portions of their investments when buying the touted stocks. To mitigate this risk, Internet users themselves have to be empowered via financial literacy initiatives to reduce their susceptibility to stock touting. Furthermore, regulatory authorities are encouraged to tak countermeasures, for instance, in the form of automated detection mechanisms. This recommendation is of specia importance as new automated investment strategies are built upon stock recommendations published within th Internet; therefore, these strategies would be vulnerable to pump and dump manipulations as well

## ORCID

Michael Siering http://orcid.org/0000-0003-3618-8423

## REFERENCES

Abbasi, A., Zhang, Z., Zimbra, D., Chen, H., & Nunamaker, J. F. (2010). Detecting fake websites: The contribution of statistica learning theory. MIS Quarterly, 34(3), 435–461

Antweiler, W., & Frank, M. Z. (2004). Is all that talk just noise? The information content of Internet stock message boards The Journal of Finance, 59(3), 1259–1294.

Arens, W. F., Schaefer, D. H., & Weigold, M. F. (2012). Advertising. New York: McGraw‐Hill Irwin.

Aune, R. K., Levine, T. R., Park, H. S., Asada, K. J. K., & Banas, J. A. (2005). Tests of a theory of communicative responsibility. Journal of Language and Social Psychology, 24(4), 358–381.

Bellman, S., Schweda, A., & Varan, D. (2010). Minimum effective frequency for interactive television ads. Journal of Direct Data and Digital Marketing Practice, 11, 281–301

Bloomberg. (2015). Executives sued by SEC over Bob Marley pump‐and‐dump scheme. https://www.bloomberg.com/news articles/2015‐11‐17/java‐executives‐sued‐by‐sec‐for‐bob‐marley‐pump‐and‐dump‐scheme (accessed 16 February 2017)

Böhme, R. & Holz, T. (2006). The effect of stock spam on financial markets. 5th Workshop on the Economics of Information Security, WEIS 2006, Robinson College, Univ. of Cambridge, England

Bollen, J., & Huina, M. (2011). Twitter mood as a stock market predictor. Computers and Operations Research, 44(10), 91–94.

de Bondt, W. F. M. (1998). A portrait of the individual investor. European Economic Review, 42(3–5), 831–844.

Bone, P. F., & France, K. R. (2001). Package graphics and consumer product beliefs. Journal of Business and Psychology, 15(3), 467–489.

Buller, D. B., & Burgoon, J. K. (1996). Interpersonal deception theory. Communication Theory, 6(3), 203–242.

Chandy, R. K., Tellis, G. J., MacInnis, D. J., & Thaivanich, P. (2001). What to say when: Advertising appeals in evolving markets. Journal of Marketing Research, 38(4), 399–414

Chua, C. E. H., Wareham, J., & Robey, D. (2007). The role of online trading communities in managing Internet auction fraud. MIS Quarterly, 31(4), 759–781.

Craig, C. S., Sternthal, B., & Leavitt, C. (1976). Advertising wearout: An experimental analysis. Journal of Marketing Research 13(4), 365–372.

Currie, W. L., & Lagoarde‐Segot, T. (2017). Financialization and information technology: Themes, issues and critical debates— part I. Journal of Information Technology, 32, 211–217.

Da, Z., Engelberg, J., & Gao, P. (2011). In search of attention. The Journal of Finance, 66(5), 1461–1499.

Danaher, P. J., Mullarkey, G. W., & Essegaier, S. (2006). Factors affecting web site visit duration: A cross‐domain analysis Journal of Marketing Research, 43(2), 182–194.

Delort, J.‐Y., Arunasalam, B., Leung, H., & Milosavljevic, M. (2011). The impact of manipulation in internet stock message boards. International Journal of Banking and Finance, 8(4), 1–18.

Epstein, G. (2004). Financialization and the world economy. Northampton, Massachusetts: Edward Elgar Publishing.

Fama, E. F. (1970). Efficient capital markets: A review of theory and empirical work. The Journal of Finance, 25(2), 383–417.

FBI. (2015). Internet Crime Report. https://www.ic3.gov/media/annualreport/2015\_IC3Report.pdf (accessed 16 February 2017).

Frieder, L., & Zittrain, J. (2006). Spam works: Evidence from stock touts and corresponding market activity. Berkman Cente Research Publication.

Grazioli, S., & Jarvenpaa, S. L. (2003). Consumer and business deception on the Internet: Content analysis of documentary evidence. International Journal of Electronic Commerce, 7(4), 93–118

Gyongi, Z., & Garcia‐Molina, H. (2005). Spam: It's not just for inboxes anymore. IEEE Computer, 38(10), 28–34

Hanke, M., & Hauser, F. (2008). On the effects of stock spam e‐mails. Journal of Financial Markets, 11(1), 57–83.

Heath, R. G., & Hyder, P. (2005). Measuring the hidden power of emotive advertising. International Journal of Market Research, 47(5), 467–486.

Hu, B., McInish, T., & Zeng, L. (2009). The CAN‐SPAM Act of 2003 and stock spam emails. Financial Services Review, 18, 87–104.

Huang, Y. C., & Cheng, Y. J. (2013). Stock manipulation and its effects: Pump and dump versus stabilization. Review of Quantitative Finance and Accounting, 44(4), 791–815.

Humpherys, S. L., Moffitt, K. C., Burns, M. B., Burgoon, J. K., & Felix, W. F. (2011). Identification of fraudulent financia statements using linguistic credibility analysis. Decision Support Systems, 50(3), 585–594

Jiang, Z., & Benbasat, I. (2007). The effects of presentation formats and task complexity on online consumers' product understanding. MIS Quarterly, 31(3), 475–500

Johnson, P. E., Grazioli, S., & Jamal, K. (1993). Fraud detection: Intentionality and deception in cognition. Accounting Organizations and Society, 18(5), 467–488.

Johnson, P. E., Grazioli, S., Jamal, K., & Glen Berryman, R. (2001). Detecting deception: Adversarial problem solving in a low base‐rate world. Cognitive Science, 25(3), 355–392.

Kim, D. J., Ferrin, D. L., & Rao, H. R. (2008). A trust‐based consumer decision‐making model in electronic commerce: The role of trust, perceived risk, and their antecedents. Decision Support Systems, 44(2), 544–564

Kim, K. J., Kim, S. Y., Park, E., Sundar, S. S., & del Pobil, A. P. (2012). The more the better? Effects of ad exposure frequency on online consumers with varying product knowledge. 8th International Conference on Information Science and Digita Content Technology.

Kim, W., Jeong, O.‐R., Kim, C., & So, J. (2011). The dark side of the Internet: Attacks, costs and responses. Informatio Systems, 36(3), 675–705.

Krippendorff, K. (2013). Content analysis: An introduction to its methodology (Third ed.). Los Angeles: Sage.

Lagoarde‐Segot, T. (2017). Financialization: towards a new research agenda. International Review of Financial Analysis, 51, 113–123.

Loughran, T., & McDonald, B. (2010). Measuring readability in financial text. Working paper, University of Notre Dame.

Loughran, T., & McDonald, B. (2011). When is a liability not a liability? Textual analysis, dictionaries, and 10‐Ks. The Journal o Finance, 66(1), 35–65.

MacKinlay, A. C. (1997). Event studies in economics and finance. Journal of Economic Literature, 35(1), 13–39

Mavlanova, T., Benbunan‐Fich, R., & Kumar, N. (2008). Deception tactics and counterfeit deception in online environments ICIS 2008 Proceedings.

Meservy, T. O., Jensen, M. L., Kruse, J., Burgoon, J. K., Nunamaker, J. F., Twitchell, D. P., Tsechpenakis, G., & Metaxas, D. N. (2005). Deception detection through automatic, unobtrusive analysis of nonverbal behaviour. IEEE Intelligent Systems, 20(5), 36–43.

Mullainathan, S., Schwartzstein, J., & Shleifer, A. (2008). Coarse thinking and persuasion. The Quarterly Journal of Economics, 123(2), 577–619.

Muntermann, J., & Guettler, A. (2007). Intraday stock price effects of ad hoc disclosures: The German case. Journal of International Financial Markets, Institutions and Money, 17(1), 1–24.

Nelson, K. K., Price, R. A., & Rountree, B. R. (2009). Why do investors pay attention to stock spam? Working Paper.

O'Brien, R. M. (2007). A caution regarding rules of thumb for variance inflation factors. Quality & Quantity, 41, 673–690.

Patell, J. M., & Wolfson, M. A. (1984). The intraday speed of adjustment of stock prices to earnings and dividend announcements. Journal of Financial Economics, 13(2), 223–252

Román, S. (2010). Relational consequences of perceived deception in online shopping: The moderating roles of type of prod uct, consumer's attitude toward the internet and consumer's demographics. Journal of Business Ethics, 95(3), 373–391.

SEC. (2012a). Internet fraud: Tips for checking out newsletters. http://www.sec.gov/investor/pubs/cyberfraud/newsletter htm (accessed 15 September 2015)

SEC. (2012b). Investor alert: Social media and investing—avoiding fraud. http://www.sec.gov/investor/alerts socialmediaandfraud.pdf (accessed 15 September 2015).

SEC. (2012c). SEC microcap fraud‐fighting initiative expels 379 dormant shell companies to protect investors from potentia scams. http://www.sec.gov/news/press/2012/2012‐91.htm (accessed 15 September 2015).

SEC. (2014). SEC charges three penny stock promoters behind pump‐and‐dump schemes. https://www.sec.gov/News PressRelease/Detail/PressRelease/1370543470309 (accessed 16 February 2017)

Seo, D., & La Paz, A. I. (2008). Exploring the dark side of IS in achieving organizational agility. Communications of the ACM 51(11), 136–139.

Siering, M., Clapham, B., Engel, O., & Gomber, P. (2017). A taxonomy of financial market manipulations: Establishing trust and market integrity in the financialized economy through automated fraud detection. Journal of Information Technology 32(3).251-269.

Sonnier, G. P., McAlister, L., & Rutz, O. J. (2011). A dynamic model of the effect of online communications on firm sales Marketing Science, 30(4), 702–716.

SSEM. (2007). Stock spam effectiveness monitor. https://www.crummy.com/features/StockSpam/ (accessed 06 December 2018)

Stone, P. J., Bales, R. F., Namenwirth, J. Z., & Ogilvie, D. M. (1962). The general inquirer: A computer system for content analysis and retrieval based on the sentence as a unit of information. behavioural Science, 7(4), 484–498.

Symantec. (2011). Global debt crises news drives pump‐and‐dump stock scams. http://www.symantec.com/connect/blogs global‐debt‐crises‐news‐drives‐pump‐and‐dump‐stock‐scams (accessed 15 September 2015).

Tarafdar, M., Gupta, A., & Turel, O. (2013). The dark side of information technology use. Information Systems Journal, 23(3) 269–275.

Tarafdar, M., Tu, Q., Ragu‐Nathan, T. S., & Ragu‐Nathan, B. S. (2011). Crossing to the dark side: Examining creators, out comes, and inhibitors of technostress. Communications of the ACM, 54(9), 113–120.

Tellis, G. J. (1997). Effective frequency: One exposure or three factors. Journal of Advertising Research, 37(4), 75–80.

Tetlock, P. C. (2007). Giving content to investor sentiment: The role of media in the stock market. The Journal of Finance 62(3), 1139–1168.

Tetlock, P. C., Saar‐Tsechansky, M., & Macskassy, S. (2008). More than words: Quantifying language to measure firms fundamentals. The Journal of Finance, 63(3), 1437–1467.

Unnava, H. R., & Burnkrant, R. E. (1991). Effects of repeating varied ad executions or brand name memory. Journal of Marketing Research, 28(4), 406–416.

Vrij, A. (2000). Detecting lies and deceit: The psychology of lying and implications for professional practice. Chichester, UK: John Wiley and Sons.

Vrij, A., Edward, K., Roberts, K. P., & Bull, R. (2000). Detecting deceit via analysis of verbal and nonverbal behaviour. Journa of Nonverbal behaviour, 24(4), 239–263.

Wall Street Journal. (1999). SEC charges 13 in ongoing sweep against illegal online stock touting. https://www.wsj.com/arti cles/SB919989275551999000 (accessed 16 February 2017).

Wareham, J., Zheng, J. G., & Straub, D. (2005). Critical themes in electronic commerce research: A meta‐analysis. Journal of Information Technology, 20(1), 1–19.

Weber, R. P. (1983). Measurement models for content analysis. Quality & Quantity, 17(2), 127–149.

Weber, R. P. (1990). Basic content analysis (2. ed., 1. print ed.). Newbury Park, California, USA: Sage.

Xiao, B., & Benbasat, I. (2011). Product‐related deception in E‐commerce: A theoretical perspective. MIS Quarterly, 35(1) 169–195.

Zahedi, F. M., Abbasi, A., & Chen, Y. (2015). Fake‐website detection tools: Identifying elements that promote individuals' us and enhance their performance. Journal of the Association for Information Systems, 16(6), 448–484.

Zhang, W., & Skiena, S. (2010). Trading strategies to exploit blog and news sentiment. Proceedings of the 4th Internationa AAAI Conference on Weblogs and Social Media, Washington, DC, USA

Zhou, L., Burgoon, J. K., Nunamaker, J. F., & Twitchell, D. (2004). Automating linguistics‐based cues for detecting deception in text‐based asynchronous computer‐mediated communications. Group Decision and Negotiation, 13(1), 81–106.

Zhou, L., & Zhang, D. (2008). Following linguistic footprints: Automatic deception detection in online communication. Communications of the ACM, 51(9), 119–122.

Zielske, H. A. (1959). The remembering and forgetting of advertising. Journal of Marketing, 23(3), 239–243.

Michael Siering is a postdoctoral research associate at Goethe University Frankfurt and works as a Business Consultant in the field of risk management. He has been a visiting scholar at Penn State University. His research focuses on decision support systems in electronic markets, with a focus on the analysis of user generated content by means of sentiment analysis and text mining. His work has been published in outlets such as Journal of Management Information Systems, Journal of Information Technology and Decision Support Systems, and conference proceedings such as ICIS, ECIS, and HICSS.

How to cite this article: Siering M. The economics of stock touting during Internet‐based pump and dump campaigns. Info Systems J. 2018;1–28. https://doi.org/10.1111/isj.12216
