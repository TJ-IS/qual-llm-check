---
otero_id: 8644
otero_key: "JAGRPKCA"
title: "The language of quarterly reports as an indicator of change in the company’s financial status"
authors: "Camilla Magnusson; Antti Arppe; Tomas Eklund; Barbro Back; Hannu Vanharanta; Ari Visa"
year: "2005"
journal: "Information & Management"
doi: "10.1016/j.im.2004.02.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The language of quarterly reports as an indicator of change in the company’s financial status

Camilla Magnusson<sup>a,\*</sup>, Antti Arppe<sup>a</sup>, Tomas Eklund<sup>b</sup>, Barbro Back<sup>b</sup>, Hannu Vanharanta<sup>c</sup>, Ari Visa

<sup>a</sup>Department of General Linguistics, University of Helsinki, P.O. Box 9, 00014 University of Helsinki, Finland <sup>b</sup>Turku Centre for Computer Science (TUCS) and IAMSR, A<sup>˚</sup> bo Akademi University, 20520 Turku, Finland <sup>c</sup>Pori School of Technology and Economics, P.O. Box 300, 28101 Pori, Finland <sup>d</sup>Signal Processing Laboratory, Tampere University of Technology, P.O. Box 553, 33101 Tampere, Finland Received 24 March 2003; received in revised form 3 November 2003; accepted 21 February 2004 Available online 9 June 2004

## Abstract

This paper adopts a multi-methodological approach to information systems research in order to produce new information through data mining. This approach is particularly suitable for mining material that consists of both qualitative and quantitative information. The contents of quarterly reports from three telecommunications companies were compared. The study focused on the years 2000–2001, a period of economic decline for many IT companies. The central quantitative data, reflected by seven financial ratios, were visualised using self-organising maps. The qualitative data, consisting of the textual contents of the reports, were visualised using collocational networks; these showed the relationships between the central concepts in the texts. As the visualisations of the contents were compared, certain patterns could be found. The results seemed to suggest that changes in the networks indicated future changes in the self-organising maps. In the cases studied, a change in the textual data usually indicated a change in the financial data in the following quarter. This may be a consequence of the fact that the texts reflected the plans and future expectations of management, whereas the financial ratios reflected the current financial situation of the company. <sup>#</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Data mining; Quarterly reports; Multiple methods; Collocational networks; Self-organising maps

## 1. Introduction

Nowadays, a huge amount of financial information is available to stakeholders, decision makers, and investors. A large portion of this is in electronic form and accessible through the Internet. It comes in different forms, both as quantitative (numeric) and qualitative (textual) data. A company’s quarterly report is an example of a document that contains both of these. In order to base decisions on the available information, the reader of such a report would ideally access both the textual content and financial figures. As long as there only are a small number of documents to study, this is not a problem, but when the number increases, IT and data mining become essential tools. Different forms of data mining techniques used in a business context have been discussed extensively by Bose and Mahapatra [4].

IT is essential to data mining. When discussing the task of knowledge generation Spiegler [22] stated that technology was the prerequisite and means for this task. He also claimed that ‘‘if data become information when they add value, then information becomes knowledge when it adds insight, abstraction, and better understanding’’.

When working with a document containing different forms of data, a single data mining method may not suffice, as it is usually not possible to capture the essence of both textual and numeric information. Therefore, a combination of methods was developed. One mechanism is based on the statistical co-occurrences of words while the other is based on selforganising maps. The combination of these methods can reveal a more detailed and informative picture of the data in a financial report and this could provide the user with knowledge; i.e. the capacity to act based on the new information.

This combination of methods reflects pluralist thinking in IS research, as proposed by Mingers [17]. He endorses a multi-methodological approach to research by combining ways that represent different paradigms in order to produce a deeper understanding of the topic. Through adopting such an approach, our work produced an image of the changes in the financial status of three companies (Nokia, Ericsson, and Motorola) during a period of eight fiscal quarters, based on their quarterly reports.

This study focused on the years 2000 and 2001, during which the economic growth in the IT sector experienced a dramatic downturn. We decided to concentrate on the telecommunications sector, which was seriously affected by these developments. Our aim was to discover how these developments were reflected in the linguistic contents of the companies quarterly reports and whether the changes stated in the texts preceded the changes in the financial figures.

## 2. Background

The aim of our study was to apply two different data mining methods to the financial and the accompanying textual data in quarterly reports.

This was undertaken by observing whether changes in self-organising maps (SOMs), which are a way of visually representing multi-dimensional quantitative data, were systematically reflected by changes in socalled collocational networks, which are a way of representing the linguistic conceptual structure of the texts of quarterly reports.

Our general hypothesis resembled the one presented by Osborne et al. [18].

When a company’s external environment and internal performance potential change:

\- there will be a change in the strategic thinking, expectations, and associated planning by its management,

\- this is reflected immediately in the text of the quarterly reports, and

\- is reflected with some time lag in the financial performance data; i.e. it takes time for the expectations and actions of the corporate management to materialise in the financial results.

This can be expected due to the nature of the quantitative and qualitative data in the quarterly reports. The financial performance figures can only represent developments prior to the publication of the quarterly report, whereas predictions and assessments can be stated in its text and not be binding on the management.

In order to test our hypothesis, we compared the results of analysis of the texts with those of a study of quantitative (financial) information.

## 3. The language of financial reporting

Quarterly reports are an important way for companies to communicate both past events and plans for the future to investors and analysts. The study of the linguistic contents of quarterly reports has nevertheless been overlooked in favour of the study of the language of annual reports. The annual report is, without doubt, the most typical company report to receive attention from linguists. As a genre, annual reports closely resemble quarterly reports. They have a similar structure and conventions, and they are read and produced by the same people within the same community. The basic functions of an annual report are similar to those of the quarterly report. What makes quarterly reports different from annual reports is their short-term perspective.

There is a broad body of literature on the language of annual reports, conducted both within applied linguistics and business communication studies. Studies of the language of annual reports can be considered background material for studying the language of quarterly reports, also. Three examples particularly relevant to the linguistic background of this article are Thomas [24], Kendall [9] and Osborne et al. A common feature for those studies was that they only concentrated on one part of the reports: the chairman’s letter to shareholders. We, however, used the complete texts of the financial reports.

Thomas concentrated on the development of one company over 4 years, a period during which it started to experience severe difficulties. During that time, the structure of the language in the reports also changed. According to the study, an increase in the use of passive constructions could be detected as the profits decreased. There was also an increase in verbs that presented the actor (i.e. the company) as ‘‘being’ rather than as ‘‘doing’’. This indicated that the management were trying to present themselves as victims of unfortunate circumstances and to create an impression of objectivity to the reader, as if the management were presenting plain facts on recent events. On the other hand, when the company was making more profit, it presented itself as aggressive and forwardmoving through the use of an active voice and verbs with both an actor and goal.

A similar discussion of the actions of a company and circumstances created by non-human agents was given by Kendall. Here, the concept of drama was introduced as a key to the language in annual reports. She classified the words and phrases describing actors and objects into two groups: god and devil terms. Some examples of god terms were growth, increased sales, and competitive position. These represented concepts that were unquestionably good. Devil terms, on the other hand, were losses, decline in sales, and regulations. Similar terminology was also used in the quarterly reports that constituted the material analysed in this article.

In their study of annual reports Osborne et al. showed that the text in annual reports reflected the strategic thinking of the management, who were associated with the financial performance of the company; different companies were clustered both according to performance and themes in the financial report texts.

Apparently, these clusters converged; i.e. a link was shown to exist between the textual and financial data.

## 4. Data and methods

The years 2000 and 2001 saw a dramatic downturn in the growth of the IT industry. We therefore considered this period as most suitable for studying changes, as they would be found in the financial figures of most IT companies at that time. We decided to focus on the telecommunications industry, which had experienced very strong growth in the 1990s. Within that sector, we decided to look at major mobile equipment and infrastructure vendors. At the end of the year 2000, three companies shared more than 50% of the market in mobile phone production: Nokia, Motorola, and Ericsson.

We decided to choose these three companies for the empirical part of our study. In addition, we hoped that their differences and similarities would provide us with interesting material. Nokia and Ericsson have many similarities. Firstly, they both originated in a Nordic country and this is the location of their head offices. Secondly, both have very small domestic markets, and are totally dependent on export, though this was partially offset by the growing EU market. Thirdly, the small domestic markets of Sweden and Finland were both quite technology oriented, providing for an ideal test market. Indeed, the Nordic countries were forerunners in telecommunications; an analogue wireless phone network (Nordic Mobile Telephone System, NMT) was implemented there in the early eighties. On the other hand, the primary difference between Ericsson and Nokia was that the former concentrated heavily on network technology, whereas the latter concentrated primarily on consumer devices. The network business area was the first and hardest hit by the telecommunications slump in 2001. During 2003, even Nokia had significantly reduced its activities in the area, indicating the extent of the slump.

Motorola, on the other hand, is an American company and therefore had the advantage of a large domestic market. The disadvantage, however, was that the US market had multiple competing standards, a disadvantage that the Nordic companies, operating on the more homogeneous EU market, did not experience. Of the three companies, Nokia is the most focused, whereas Ericsson and Motorola produced many other electronic products.

For our study, quarterly reports from these three companies, spanning from the first quarter in 2000 to the last quarter in 2001, were the research material. In order to compare the textual and financial information in these reports, two data mining methods were used. The texts were turned into collocational networks according to the method used by Magnusson and Vanharanta [16]. The financial data were visualised using a self-organising map.

## 4.1. Collocational networks

In order to visualise the central concepts and their connections within a quarterly report, a method originally devised by Williams [25] was applied. The main concept in this method is a collocational network. In his study, Williams uses the network for exploring the language of science in order to create specialised dictionaries. In our work, the method was used with a similar question: what are the central concepts in a text, in this case a quarterly report, and how are they linked?

For our study, a collocation was interpreted simply as ‘‘the occurrence of two or more words within a short space of each other in a text’’ following Sinclair [21]. It should be noted that the contents of each report were analysed separately. Pairs of words, collocations, are therefore patterns which occur within a single text.

An important factor is the concept of significant collocation, which takes place when two or more words occur together more frequently than would be expected by coincidence. Following Williams, the significance of collocation is measured using the Mutual Information or MI score. This, an information theoretic concept introduced in linguistics [5], compares the frequency of co-occurrence of node and collocate with the frequency of their occurrence independent of each other; it is widely used in lexicographical work.

This approach provided an opportunity for us to examine which concepts were emphasised by the company in a particular report. The concepts are reflected through the words that constitute the nodes of the network. The approach also allowed us to examine which concepts are most frequently linked to one another, by revealing which words regularly appear in close proximity.

It should be noted, however, that this method does not always bring out combinations of words that are perceived to belong together as phrases or compound words, such as balance and sheet, unless they occur very frequently in the text. This should not be a problem here, however, because we looked at what is central to the particular texts, not intending to find collocations that are typical for business language in general.

Before the actual analysis could take place some preliminary measures had to be made. Quarterly reports usually consist of both text and tables. As the text was the object of analysis, any tables that could easily be separated were removed. Some minor ones were not, but these were suppressed during the drawing of the networks by leaving out words such as adjusted, operational, and non-operational that occurred in the tables.

During the drawing of the networks a number of other words with little tactical relevance were left out, including: prepositions, articles, conjunctions, those referring to the time span of the report (quarter, first, etc.), and figures or currency.

The initial stage of the analysis entailed calculating the MI score for all words occurring within a span of four from one another. A maximum span of this size was recommended by Sinclair for studying collocations in English. With text sizes of approximately 4,000 words, an minimum MI score of 2.00 was found to produce a network of a suitable size. Lowering the score would have brought in words that occur together only occasionally, while a higher limit would have produced a network with only the most frequent combinations, leaving out interesting changes among the mid-frequency words.

## 4.2. Self-organising maps

Quantitative analysis of financial information is not new and many different tools have been used to accomplish it. One possible application is the SOM [12]. This is an unsupervised neural network that maps multidimensional data onto a two-dimensional topological map; it is commonly used for exploratory data mining. The map clusters data according to similarities, displaying the result as a map of nodes separated by borders: dark ones represent great differences, while light ones indicate similarities, forming clusters of data.

![](/api/attachments/JAGRPKCA/fulltext/images/f75144e944b5aeef9cdd08104057d9f43f5159032902dbae94c7ec51022731c9.jpg)  
Fig. 1. The SOM model.

The SOM has been used in a variety of economic and financial applications; for example, economic welfare and poverty distribution [8], economic environment analysis [14,15], bankruptcy prediction [1,10,19,20], credit rating [23] and financial benchmarking [2,6]. Back et al. [3] and Kloptchenko et al. [11] also explored the possibility of combining SOMs and text mining techniques in order to extract qualitative information from annual or quarterly reports.

In our study, the financial data of the reports were visualised using the SOM. The map used was from Karlsson et al. [7]. A SOM was created to benchmark the performance of 88 international telecommunications companies. A number of financial ratios were calculated, after which the SOM map was trained. The ratios included were: operating margin, return on equity, return on total assets (profitability ratios), current ratio (liquidity ratio), equity to capital, interest coverage (solvency ratios), and receivables turnover (efficiency ratio). These ratios were chosen based on an empirical study on the reliability and validity of financial ratios in international comparisons [13]. The map created was then used to display the actual financial performance of the three companies (Fig. 1). More information on the prior study and its results can be found in the original study.

On the map, dashed lines indicate the borders of the different clusters that are identified by using letters. The interpretation of the six clusters is given by analysing the feature maps (see Fig. 2). On these, the weight for each neuron is visualised by grey-level imaging with light shades representing high values and dark shades representing low ones. We can study each input variable separately. The value of the variable operating margin (a profitability measure), for example, is high for the neurons on the right hand side of the map and low for the neurons on the left. Hence, a company that was mapped onto the neurons on the right side of the SOM had a higher operating margin than the companies on the left. On the other hand, the variable equity to capital (a solvency measure) had high values in the neurons on the lower right part of the map and low values on the upper left. Therefore, a company with high liabilities was mapped on the upper left part of the map and so on. In order to make the map more readable, we marked the locations indicating the performance of only the analysed companies for seven quarters, starting in 2000.

![](/api/attachments/JAGRPKCA/fulltext/images/f824d3559b0cdd0d837780d46b2bac27ec27612f8912a47984cc5daae6bbaa29.jpg)  
Fig. 2. The SOM feature maps.

The characteristics of the different clusters can be summarised as follows:

\- Groups A1 and A2 were the best performing companies. Profitability was very high, and solvency was good. The companies in group A2 were not quite as profitable as those in group A1, but had higher solvency and liquidity.

\- Group B was slightly poorer but was still very good, with good profitability and reasonable solvency.

\- Groups C1 and C2 were average. Profitability and liquidity was better in group C1 than C2, but solvency was better in group C2. Generally speaking, groups C1 and C2 are average.

\- Group D was the poorest, with very low values in nearly all ratios, especially in profitability and solvency.

## 5. Results

## 5.1. Collocational networks

A fruitful way to approach the collocational networks produced from the quarterly reports was to study the networks from each company separately, as suggested by Magnusson and Vanharanta. An approach of this kind gave insight into the periods of stability or change that occurred in the texts. There were two points of interest where stability or changes could be seen: the structures of the networks and the words they contained. Then, a closer look was taken at both in the networks created out of each company’s quarterly reports.

There is no definitive key to the interpretation of these networks. They simply reflect the surface structure of texts, and therefore require the interpretative decisions of a reader to interpret them, just like their texts. Analysis of the networks, as presented here, represents our own interpretation.

![](/api/attachments/JAGRPKCA/fulltext/images/c4f50ff120805a8fb3ebec388a1591b1193a038c18dd937a40281d82bf4956a7.jpg)  
Fig. 3. Nokia network 1/2001.

## 5.1.1. The Nokia reports

Looking at their collocational networks, a long period of stability was seen. During the year 2000, the networks hardly changed. They were almost identical, containing the name Nokia as a central node with links to others referring to the company’s business segments, such as Networks or Mobile Phones, or general nouns used in business, such as sales, market, and growth.

However, quite a remarkable change took place between the contents of the first and second report for 2001. Structurally, networks 1/2001 and 2/2001 (Figs. 3 and 4) look similar: they both have one central word, Nokia, around which most other words occurred and there were two collocational pairs outside the main structure.

![](/api/attachments/JAGRPKCA/fulltext/images/31bef99a5b12f2b3f46cd6b438a70f661d862efd1ef47bde0481351b87a041bc.jpg)  
Fig. 4. Nokia network 2/2001.

![](/api/attachments/JAGRPKCA/fulltext/images/a3c1d3de5ab48fb309304da957bf4c9273fa8aed0d05eb75e92c81a1514625a7.jpg)  
Fig. 5. Motorola network 4/2000.

Two words that appeared in 2/2001, marking the change in the networks, were decline and decreased. Neither appeared in the previous time frame. In the text of the report for 1/2001 decline did not appear at all and decreased only appeared twice, making the sudden increase to 5 and 16 occurrences, respectively, quite noticeable. At the same time words bearing positive connotations, such as growth and increased disappeared. The connection between these events was made explicit by the fact that sales, a word linked to increased in the first network, was linked to decline in the second.

After this change, the networks still retained the same structure. They always contained one major network with Nokia as the central node linked to about a dozen collocates. However, positive words like increased did not reappear.

## 5.1.2. The Motorola reports

These networks showed less uniformity than Nokia’s networks. Still, for the year 2000 they resembled each other quite closely. They consisted of one main network with the word sales as the central node. Linked to it were words like increased, higher, orders, and systems. Interestingly, the word lower also appeared.

A budding change could be seen in the fourth network for 2000 and particularly in the first network for 2001 (Figs. 5 and 6). The main network still concentrated on sales, but there was also a smaller network around the word Motorola, which was the most frequent word in the text and was linked to the collocates announced and new. It seems that the company was trying to emphasise the announcement of new innovations. Interestingly, at the same time, positive words like higher and increased had disappeared.

Network 2/2001 looks quite similar. Motorola was still the most frequent word, but it was now only linked to announced. The word decline had also appeared as a collocate to sales.

In the third network for 2001, the changes continued. This looked very different from the previous ones as it did not contain any structure resembling a network, only pairs of collocations. Sales, which was a central node in the previous networks, was only linked to segment. Motorola was still linked to announced. What made the contents of this network particularly different from previous networks, was the complete lack of words describing the financial developments, such as increased, decreased, higher, and lower.

![](/api/attachments/JAGRPKCA/fulltext/images/e3eae9bab9edc1f54b5810ee7f7c6fe7dfe0e2b1d7b8b088780c2c21cfc5d1a6.jpg)  
Fig. 6. Motorola network 1/2001.

## 5.1.3. The Ericsson reports

A brief overview of the collocational networks based on Ericsson’s quarterly reports showed that they never exhibited the same stability as Nokia’s. During the period studied, both the structure and the content of the networks varied considerably. This was also obvious when looking at the texts: during this period the reports underwent several structural changes. New headings were introduced and old ones were abandoned or reorganised.

A particularly remarkable change in the networks happened between the third and fourth reports for 2000 (Figs. 7 and 8). Structurally, these networks were very different. There was also a significant difference between the lexical items used and the number of lexical items in the networks.

![](/api/attachments/JAGRPKCA/fulltext/images/e2541defa390cbf349b9bd6e2194c488d64555449791168b10a17ea49c3f8a16.jpg)  
Fig. 7. Ericsson network 3/2000.

![](/api/attachments/JAGRPKCA/fulltext/images/1e227ee83b38854472d6b8bf02e126807fda97b4686a667cef699c8ee76ee1e3.jpg)  
Fig. 8. Ericsson network 4/2000.

Network 3/2000 started with the most frequent word, Ericsson, linked to five collocates. One of these, increased, was linked to sales, which had four other collocates of its own. One of the collocates systems, was linked to mobile, which had five more collocates. These linkages meant that the main network for 3/ 2000 consisted of three parts, connected by collocational pairs. In addition, there were several separate collocational pairs and small networks outside the main network.

The structure of network 4/2000 was very different from that of 3/2000. It consisted of a main network attached around the most frequent word, we, and a smaller, separate network around operating. We was a new word, and the most frequent one in network 3/ 2000, Ericsson, had disappeared: the company now referred to itself using a pronoun.

In addition to these two major networks, there was one separate collocational pair, consisting of two new words, additional and restructuring; these were quite informative about Ericsson’s situation. The number of words in the network was much smaller than in the previous one (33 versus 14), and the structure was much less complex. The obvious reason was that report 3/ 2000 consisted of approximately 3,600 words, whereas report 4/2000 had approximately 2,100.

In the next network, 1/2001, the change continued. This contained even fewer words. Now there was only one word, expect, connected to we, as opposed to five collocates in the prior network. A new addition was the collocation efficiency program, a term bearing obvious negative connotations to anyone acquainted with corporate jargon.

## 5.1.4. Summary of the analysis of the networks

Changes in the collocational networks took place over a period of two quarters. After a period of general stability, impending change was first heralded by a seemingly minor change, such as the appearance of a single word or word pair with a negative connotation (expects or lower sales) or the disappearance of a word or word pair indicating the continuation of previous (positive) development (continued). At the same time, the network contained some words with positive connotations. This can be viewed as an anticipation of change by the management of the companies. In the next quarter, the heralded change really occurred and the structure and words contained in the network changed compared to preceding quarters. If the change represented a permanent change in the environment of the company, the change became stable, as was the case for Ericsson, with the most informative collocation in quarters 3/2000–3/2001 being efficiency program. Table 1 contains an overview of the most significant changes in the collocational networks based on the quarterly reports.

## 5.2. Self-organising maps

In observing the position of the companies in Fig. 1, it was essential to focus on movements between the groups rather than minor movements within them. Hence, the financial position of Nokia was relatively stable in quarters 1/2000–2/2001 with the company firmly in the A1 group. A major change for Nokia occurred between quarters 2/2001 and 3/2001, when the company moved to group C2. In the third quarter financial figures, Nokia’s profitability dropped considerably, and Nokia dropped from the best group into group C2. This was primarily due to defaulted loans to the Turkish telecom operator Telsim, as well as insolvency of the UK operator Dolphin.

Table 1  
Summary of the lexical changes in the collocational networks

<table><tr><td>Quarter/company</td><td>Nokia</td><td>Motorola</td><td>Ericsson</td></tr><tr><td>1/2000</td><td>-</td><td>-</td><td>-</td></tr><tr><td>2/2000</td><td>-</td><td>-</td><td>-</td></tr><tr><td>3/2000</td><td>-</td><td>-</td><td>-</td></tr><tr><td>4/2000</td><td>-</td><td>Anticipation:  $\emptyset \rightarrow$  lower sales</td><td>Change: sales growth, sales increase → additional restructuring</td></tr><tr><td>1/2001</td><td>Anticipation: continued →  $\emptyset$ </td><td>Change: sales increased → significantly lower sales, sales down</td><td> $\emptyset \rightarrow$  efficiency program</td></tr><tr><td>2/2001</td><td>Change: new, strong growth, increased sales → decreased, sales decline</td><td>-</td><td>-</td></tr><tr><td>3/2001</td><td>-</td><td>-</td><td>-</td></tr><tr><td>4/2001</td><td>-</td><td>-</td><td>-</td></tr></table>

In the case of Motorola, its position was relatively stable throughout 2000, with the company in group C1 for most of the period. In Motorola’s case, a change started to take place between quarters 4/2000 and 1/2001, when the company moved to the poorer end of group C2. In 2/2001, it had moved to group D.

Finally, for Ericsson the financial situation appeared relatively stable through 2000, when the company was situated in group B (with a short move to group A1). Ericsson’s situation deteriorated significantly after the quarter 4/2000, when the company shifted first to group C1 and finally to group D. Ericsson’s financial performance decreased considerably between 4/2000 and 1/2001, dropping into the lower end of group C1, indicating rapidly declining performance. During 2/2001 to 3/2001, its profitability and solvency continued to decrease, and it was obvious that the company was experiencing difficulties. As can be noted, the changes for all the companies during the studied period were to the worse, with no exception.

## 6. Analysis of the combined results

Results of the changes in the collocational networks (as presented in Table 1) and the significant shifts in the SOM model (as in Fig. 1) were combined in Table 2. This shows that a significant change in the collocational network of a company’s quarterly report was followed by change in the position of the company in the SOM model in the next quarter. The changes in the collocational networks were, in turn, preceded by a smaller, anticipatory change in the collocational network of the prior quarterly report compared to preceding ones.

Looking at Nokia, a change took place in the textual material of the first and second quarters of 2001. The network for 2/2001 exhibited words such as decline and decrease. In the SOM reflecting the figures, a shift can be seen in the third quarter, when Nokia moved from an excellent performance group (A1) to the average (C2).

In the case of Motorola, there was an anticipation of change in the network for 4/2000, which was significantly smaller than the previous one. The real change, however, took place in the 1/2001 network. Words like down appear, and higher and increased disappear. On the SOM, Motorola moved from the average group (C1 to C2) between the quarters 4/2000 and 1/2001, and then on to poor performance group (D) in 2/2001.

For Ericsson the changes started even earlier. The networks created from Ericsson’s reports for 3/2000 and 4/2000 looked completely different. The large network of the third quarter had been transformed into a much smaller one in the fourth. One of the new words appearing in 4/2000 was the clearly negative restructuring, whereas positive words, such as increase and growth, had disappeared. On the SOM, Ericsson moved from the good performance group (B) to the average performance group (C1) and down to the low performance group (D) during quarters 4/2000 to 2/2001.

Table 2  
Comparison of changes in collocational networks and SOMs

<table><tr><td rowspan="2">Quarter</td><td colspan="3">Company</td></tr><tr><td>Nokia</td><td>Motorola</td><td>Ericsson</td></tr><tr><td>1/2000</td><td>-</td><td>-</td><td>-</td></tr><tr><td>2/2000</td><td>-</td><td>-</td><td>-</td></tr><tr><td>3/2000</td><td>-</td><td>-</td><td>-</td></tr><tr><td>4/2000</td><td>-</td><td>Network anticipation</td><td>Network change</td></tr><tr><td>1/2001</td><td>Network anticipation</td><td>Network change</td><td>SOM shift (B → C1)</td></tr><tr><td>2/2001</td><td>Network change</td><td>SOM shift (C2 → D)</td><td>SOM shift (C1 → D)</td></tr><tr><td>3/2001</td><td>SOM shift (A1 → C2)</td><td>-</td><td>-</td></tr><tr><td>4/2001</td><td>-</td><td>-</td><td>-</td></tr></table>

It is clear that these companies all had experienced financial difficulties during the years 2000 and 2001, as they all shifted to worse performing groups during that time. Moreover, the companies had exhibited changes in their quarterly report texts as reflected in their collocational networks. The changes in the texts preceded the changes in the figures by approximately one quarter.

## 7. Conclusions

Information technology has made new methods possible for knowledge generation. However, a single method is often not sufficient for obtaining new insight and deeper understanding. Adopting a multi-methodological approach, we have combined two very different methods, collocational networks and selforganising maps, in order to produce a more extensive picture of the subject material than through the use of only a single method.

Based on our results, we confirmed our original hypothesis that changes in the qualitative data (text) preceded changes in the quantitative data (financial figures) for the companies studied.

It appears that the time lag was roughly one fiscal quarter. However, the developments of the chosen companies during the period were quite one-sided: the texts of the quarterly reports anticipated a worsening in financial performance, which indeed became a reality. The number of cases studied here is, however, too small to allow generalisation of the results.

Nevertheless, this study shows clearly that a combination of two data mining methods provides the user with access to information that a single method could not provide. When working with both qualitative and quantitative data, the methods can be seen to both support and complement each other.

## Acknowledgements

The authors would like to thank the National Technology Agency of Finland, (TEKES) (application form 40943/99) and the Academy of Finland for financial support, and Jonas Karlsson for permission to use his dataset.

## References

[1] B. Back, G. Oosterom, K. Sere, M. van Wezel, Intelligent information systems within business: bankruptcy predictions using neural networks, in: Proceedings of the 3rd European Conference on Information Systems, ECIS’95, Athens, 1995, pp. 99–111.

[2] B. Back, K. Sere, H. Vanharanta, Managing complexity in large data bases using self-organising maps, Accounting Management and Information Technologies 8, 1998, pp. 191–210.

[3] B. Back, J. Toivonen, H. Vanharanta, A. Visa, Comparing numerical data and text information from annual reports using self-organising maps, International Journal of Accounting Information Systems 2, 2001, pp. 249–269.

[4] I. Bose, R.K. Mahapatra, Business data mining—a machine learning perspective, Information and Management 39, 2001, pp. 211–225.

[5] K.W. Church, P. Hanks, Word association norms, mutual information, and lexicography, Computational Linguistics 16, 1990, pp. 22–29.

[6] T. Eklund, B. Back, H. Vanharanta, A. Visa, Using the selforganising map as a visualization tool in financial benchmarking, Information Visualization 2, 2003, pp. 171–181.

[7] J. Karlsson, B. Back, H. Vanharanta, A. Visa, Analysing financial performance with quarterly data using self-organising maps, TUCS Technical Report No. 430, Turku, 2001.

[8] S. Kaski, T. Kohonen, Exploratory data analysis by the selforganising map: structures of welfare and poverty in the world, in: Neural Networks in Financial Engineering, Proceedings of the Third International Conference on Neural Networks in the Capital Markets, London, 1995, pp. 498–507.

[9] J.E. Kendall, Good and evil in the chairmen’s ‘‘boiler plate’’: an analysis, Organization Studies 14, 1993, pp. 571–592.

[10] K. Kiviluoto, Predicting bankruptcies with self-organising maps, Neurocomputing 21, 1998, pp. 191–201.

[11] A. Kloptchenko, T. Eklund, B. Back, J. Karlsson, H. Vanharanta, A. Visa, Combining data and text mining techniques for analysing financial reports, in: Proceedings of the Eighth Americas Conference on Information Systems, Dallas, 2002, pp. 20–28.

[12] T. Kohonen, Self-Organising Maps, second ed., Springer, Berlin, 1997.

[13] J. Lehtinen, Financial Ratios in an International Comparison. Acta Wasaensia. 49, Vaasa, 1996.

[14] A. La¨nsiluoto, B. Back, H. Vanharanta, A. Visa, Country specific financial trend analysis with self-organising maps, in: Proceedings of the Tenth Annual Research Workshop on Artificial Intelligence and Emerging Technologies (AI/ET) in Accounting, Auditing and Tax, Atlanta, 2001, pp. 15–23.

[15] A. La¨nsiluoto, B. Back, H. Vanharanta, A. Visa, Multivariable business cycle analysis with self-organising maps—are the cycles similar? in: Proceedings of the European Conference on Accounting Information System, 2002.

[16] C. Magnusson, H. Vanharanta, Visualizing sequences of texts using collocational networks, in: Machine Learning and Data Mining in Pattern Recognition, Proceedings of MLDM 2003, Springer, Berlin, pp. 276–283.

[17] J. Mingers, Combining IS research methods: towards a pluralist methodology, Information Systems Research 12, 2001, pp. 240–259.

[18] J.D. Osborne, C.I. Stubbart, A. Ramaprasad, Strategic groups and competitive enactment: a study of dynamic relationships between mental models and performance, Strategic Management Journal 22, 2001, pp. 435–454.

[19] B. Mart´ın-del-Br´ıo, C. Serrano-Cinca, Self-organising neural networks for the analysis and representation of data: some financial cases, Neural Computing and Applications 1, 1993, pp. 193–206.

[20] C. Serrano-Cinca, Self organising neural networks for financial diagnosis, Decision Support Systems 17, 1996, pp. 227–238.

[21] J. Sinclair, Corpus, Concordance, Collocation, Oxford University Press, Oxford, 1991.

[22] I. Spiegler, Technology and knowledge: bridging a ‘‘generating’’ gap, Information and Management 40, 2003, pp. 533–539.

[23] R.G.H. Tan, J. van den Berg, W.-M. van den Bergh, Credit rating classification using self-organising maps, in: K. Smith, J. Gupta (Eds.), Neural Networks in Business: Techniques

and Applications, Idea Group Publishing, Hershey, 2002, pp. 140–153.

[24] J. Thomas, Discourse in the marketplace: the making of meaning in annual reports, The Journal of Business Communication 34, 1997, pp. 47–66.

[25] G.C. Williams, Collocational networks: interlocking patterns of lexis in a corpus of plant biology research articles, International Journal of Corpus Linguistics 3, 1998, pp. 151–171.

![](/api/attachments/JAGRPKCA/fulltext/images/b3a379a0ea506e57ff9da526827f24af0da79528a99350e2973bb5aec27373e6.jpg)  
Camilla Magnusson (MA Linguistics, University of Helsinki, 2002) is a doctoral student at the Department of General Linguistics at the University of Helsinki, Finland. Her research interests include the linguistic study of corporate communication and text mining.

![](/api/attachments/JAGRPKCA/fulltext/images/958006582d41b1f86ee01e7bbd7faa83562803551bb855f866d1410841330176.jpg)

Antti Arppe (MSc Engineering, Helsinki University of Technology, 1995) is a researcher and doctoral student at the Department of General Linguistics at the University of Helsinki, Finland. His current research interests center on multi-methodological research strategies in linguistics (corpus-based and experimentational methods) and lexical semantics.

![](/api/attachments/JAGRPKCA/fulltext/images/8cf3c28df313af3ae16cad5a9afec8fd40f6f4b60397454686ec11ed459c9c8e.jpg)

Tomas Eklund (LSc (Economics), A<sup>˚</sup> bo Akademi University, 2003) is a doctoral student at Turku Centre for Computer Science, A<sup>˚</sup> bo Akademi University, in Turku, Finland. The topic of his doctoral dissertation is the use of self-organising neural networks in financial benchmarking. His publications have appeared in Information Visualization and International Journal of Intelligent Systems in Accounting, Finance and Management.

![](/api/attachments/JAGRPKCA/fulltext/images/4ae61820bd0633468162f277738addcbf4ed8a889063d13985fb5d1f0391e7fb.jpg)

Barbro Back is professor of Accounting Information Systems at A<sup>˚</sup> bo Akademi University in Turku, Finland. Her research interests are in the areas of data mining, neural networks, financial benchmarking and enterprise resource planning systems. She has published in journals such as Journal of Management Information Systems, Accounting, Management and Information Technologies, International Journal of Accounting

Information Systems and European Journal of Operational Research.

![](/api/attachments/JAGRPKCA/fulltext/images/af92d9f40139928e1c59f25d1e5df132f6c4942d887a408e8079989facd4cb5f.jpg)  
Hannu Vanharanta is professor of Industrial Management and Engineering at Tampere University of Technology in Pori, Finland. His research interests include strategic management, human resource management, knowledge management and executive support systems.

![](/api/attachments/JAGRPKCA/fulltext/images/a05dc2bd412dd23ffad6da6f203dc72626c0c98e081366b3c7b245d2a1966d49.jpg)  
Ari Visa is professor of digital signal processing at Tampere University of Technology in Tampere, Finland. His current research interests are in multimedia and multimedia systems, adaptive systems, wireless communications, distributed computing, soft computing, computer vision, knowledge mining, and knowledge retrieval.
