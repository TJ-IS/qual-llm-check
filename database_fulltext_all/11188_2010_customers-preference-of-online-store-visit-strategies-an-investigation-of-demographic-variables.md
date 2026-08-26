---
otero_id: 11188
otero_key: "B5W6N7XB"
title: "Customers’ preference of online store visit strategies: an investigation of demographic variables"
authors: "Chee Wei Phang; Atreyi Kankanhalli; Karthik Ramakrishnan; Krishnamurthy S Raman"
year: "2010"
journal: "European Journal of Information Systems"
doi: "10.1057/ejis.2010.32"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Customers’ preference of online store visit strategies: an investigation of demographic variables

Chee Wei Phang<sup>1</sup>, Atreyi Kankanhalli<sup>2</sup>, Karthik Ramakrishnan<sup>3</sup> and Krishnamurthy S. Raman<sup>2</sup>

<sup>1</sup>Department of Information Management and Information Systems, Fudan University, China; <sup>2</sup>Department of Information Systems, National University of Singapore; <sup>3</sup>Business Development and Marketing, Imfinity Pte. Ltd., Singapore

Chee Wei Phang, Information Management and Information Systems, Fudan University, Room 707, Siyuan Building, 670 Guoshun Road, Shanghai, 200433, China. Tel: þ 862165648784; Fax: þ 862165644783; E-mail: phangcw@fudan.edu.cn

## Abstract

There is significant interest among marketers and academics to understand how to segment online consumers to better fulfill their needs. Previous literature on brick-and-mortar shopping has advocated demographic variables as simple yet valuable indicators to understand consumers and segment them accordingly. However, research in the online shopping context has produced mixed findings about the effects of demographics, which limit their utility to online merchants. As an attempt to address the ambiguity, the study proposes a more comprehensive approach to investigate the effects of demographic variables in the online shopping context. This is done by considering the demographic variables in combinations and using clickstream data to more accurately derive online shoppers’ surfing behaviour for segmentation purposes. Following this approach, our study investigates the effects of the demographic variables of gender, age, income, and education, based on the theories of media naturalness and consumer trait and involvement. The results reveal various effects of age, income, and education on online consumers’ needs being reflected in their store visit strategies. Implications are suggested for e-commerce research and practice. European Journal of Information Systems (2010) 19, 344–358. doi:10.1057/ejis.2010.32

Keywords: electronic commerce; demographics; online store visit strategy; clickstream data

## Introduction

In order to satisfy and gain the loyalty of their online customers, it is imperative for businesses to leverage on the unique opportunities offered by e-commerce, particularly in identifying customer’s shopping motivations (van der Heijden et al., 2003). For online merchants, the motivations and needs of customers may be surmised from the strategies they employ while visiting an online store (Moe, 2003). For instance, some customers may choose to adopt a focused strategy to deliberately search for product information when visiting an online store; while others may prefer to casually explore an online store for the sake of shopping enjoyment. A way to explain the difference in their choice of online store visit strategies is through consumers’ demographics.

Demographic variables, such as gender, age, income, and education, have often been used and studied to segment the consumer population for better marketing strategies (Assael, 1992). These variables are relatively easy to assess as compared to eliciting consumers’ attitudes through perceptual surveys that require them to spend time and effort to complete.

Yet, demographic variables offer valuable insights into ‘who consumers are’ and ‘what they need’ (Assael, 1992; Kotler, 1997). For instance, income may serve as a simple indicator of a consumer’s purchasing power, and merchants may focus their marketing campaigns of luxury goods on those with high income. It is also common for e-commerce sites to request customers to fill in their demographic information during registration to experience personalized offerings, for example Amazon.com and eBay.com.

Likewise, the information systems (IS) literature has noted the association between individual demographics and technology usage. For instance, these characteristics have been related to individuals’ attitudes towards technologies (Agarwal & Prasad, 1999), physiological and cognitive skills to use technologies (Morris & Venkatesh, 2000), and computer-mediated communication patterns (Dennis et al., 1999). With the advent of e-commerce, there has been a convergence in the research on consumer behaviour and IS, where consumers’ demographics are expected to influence their use of Internet technologies to search for information and make purchases (Ahuja et al., 2003).

Early e-commerce research on demographics focused on their effects on consumers’ adoption of online shopping (e.g., Li et al., 1999; Burroughs & Sabherwal, 2001), while more recent studies have examined how these variables influence consumers’ needs and preferences when shopping online, for example seeking information or enjoyment (e.g., Joines et al., 2003; Rohm & Swaminathan, 2004). However, this stream of work has produced mixed findings about the effects of demographic variables (refer to the Appendix for a summary of e-commerce studies on demographic influences on search vs hedonic motivations). For instance, Klein & Ford (2003) found a negative relationship between consumers’ income and their tendency to engage in information search, while Joines et al. (2003) and Rohm & Swaminathan (2004) did not detect any effect of income. The ambiguous findings limit the utility of demographic variables to online merchants for customer segmentation and personalization purposes. The ambiguities also point to the need for a better understanding of the effects of demographic variables and a more comprehensive approach to study them. To address our research question, ‘how do demographic variables influence consumers’ preference of online store visit strategies?’ we suggest an approach that differs from previous studies as follows.

First, our study proposes the use of a combination of demographics (gender, age, income, and education), to investigate their effects on consumers’ online store visit strategies. This is based on the reasoning that these characteristics do not exist independent of each other and that they may have related effects. One demographic variable may make the effect of another more salient or they may even nullify each other as explained later in the paper. Studying the effects of the variables in isolation may not allow for the inter-relations to be uncovered and may result in ambiguous findings.

Second, in deriving consumers’ online store visit strategies, our study employs clickstream data which is considered more objective compared to the perceptual or subjective measures employed in prior research studying demographic effects (refer to the Appendix). It has been noted that consumers may not be able to accurately express their needs when prompted (Fah et al., 2005). In contrast, clickstream data represents the idiosyncratic steps taken by consumers during their surfing of an online store (Vriens & Grigsby, 2001). Such data can be tracked in an unobtrusive manner via mechanisms such as web-server logs or proxy-based logging software. Research has shown that strong regularities exist in web surfing behaviour (Huberman et al., 1998), and that analyzing clickstream data can aid in profiling consumers to identify their needs and strategies while visiting an online store (Moe, 2003). In this study, we employ a robust profiling technique developed by Moe (2003) to objectively derive consumers’ store visit strategies based on clickstream data.

Through the above approach and based on theoretical foundations, we propose hypotheses to explain the effects of combinations of demographic variables on consumers’ choice of online store visit strategies derived from clickstream data. The hypotheses were tested using clickstream data obtained from a sample of visitors at a popular online books and CDs/DVDs retailer. The findings indicate support for the hypotheses from which implications for research and practice are provided.

## Characteristics of online shopping

The online shopping environment differs from traditional shopping in physical stores in several ways that may implicate our study. First, research has noted the relative lack of social-experiential elements in online shopping, where consumers have limited interaction with products and sales assistants in the technologyenabled setting (Jahng et al., 2007). Second, the online shopping environment provides consumers access to an abundance of information (Li et al., 1999; Chiang & Dholakia, 2003), which also comes with the cost of information searching and processing, that is it becomes more time-consuming to locate and gather the information needed for decision making as the amount of information increases (Li et al., 1999). These characteristics of online shopping inform how demographics affect online shoppers’ needs and preferences, and have led us to employ appropriate theories to understand these effects, specifically media naturalness theory and consumer trait and involvement theory.

Media naturalness theory addresses the issues associated with the relative lack of socio-experiential elements in the online shopping environment, while consumer trait and involvement theory explains the implications of the availability of abundant information afforded by the Internet. Below we will discuss the two theories and then describe the profiling technique employed to derive consumers’ online store visit strategies, which constitutes the dependent variable of this study.

## Media naturalness theory

Media naturalness theory (Kock, 2004, 2005) proposes that a medium low in naturalness, or having low similarity with the face-to-face medium, will increase cognitive effort and decrease physiological arousal. Building on human evolution ideas, the theory argues that because it has been natural for our ancestors to communicate face-to-face, evolutionary pressures have led to the development of the human brain that is designed for face-to-face communication (Kock, 2004). Specifically, the co-location and synchronicity afforded by the face-to-face medium allows individuals to exchange communicative stimuli quickly and through different cues, for example facial expressions and speech.

Applying the theory to the e-commerce context, the online shopping environment possesses lower naturalness compared to traditional shopping that affords faceto-face interaction. The lower naturalness of the online shopping environment leads to a decrease in physiological arousal, which is associated with excitement and pleasure (Kock, 2005). Face-to-face interaction triggers physiological arousal in human beings, whereas the online shopping environment makes interaction duller due to the lack of arousal through different human senses, for example taste, smell, and touch. Previous research investigating the influence of gender has advocated that females tend to have higher socialexperiential needs in shopping than males (e.g., Bergadaa et al., 1995), while no such differences have been suggested or are expected for age, income, and education. Since media naturalness theory explains how these needs are satisfied through different media, we make use of it to understand the effect of gender on consumers’ preference of online store visit strategies.

## Consumer trait and involvement theory

Consumer trait and involvement theory (Kassarjian, 1981) suggests that some consumers are more involved in shopping for products than others, which can be attributed to individual characteristics including their demographics. Individuals with higher involvement are more motivated to invest mental and physical effort in shopping for products (Slama & Tashchian, 1985; Laaksonen, 1994), such as searching for more product information (Beatty & Smith, 1987).

This theory and related concepts have also been applied in the online shopping context (Koufaris, 2002; Moon, 2004). For instance, Moon (2004) proposed that online consumers’ demographics may influence their tendency to search for product information through the Internet, but the effects were not explained or empirically tested. Based on the above, our study employs the consumer trait and involvement theory to understand the relationships between demographic variables and consumer’s preference of online store visit strategies.

## Typology of online store visit strategies

In this study, we apply the profiling technique developed by Moe (2003) to derive consumers’ online store visit strategies based on clickstream data. This technique was chosen for several reasons. First, the technique was theoretically derived based on consumer’s search modes (goal directed or exploratory), an approach that is widely adopted in similar research (e.g., Singh & Dalal, 1999; Dholakia & Bagozzi, 2001). In addition, this method included the time horizon of purchase to obtain a more refined classification of visit strategies. Using clickstream data, the technique has been shown to be robust in explicating the strategies of consumers visiting an online store that sells healthcare products (Moe, 2003). The welldefined and parsimonious set of visit strategies has also been applied in a number of studies to investigate online consumer behaviour (e.g., Vroomen et al., 2003; Nysveen & Pedersen, 2005).

Consumers visit an online store with varying search needs. Broadly, their search behaviour can be classified into goal-directed or exploratory search (Janiszewski, 1998). Goal-directed search refers to behaviour in which the consumer has a planned purchase in mind and employs search routines that aid in gathering specific product information. Exploratory search behaviour is characterized by stimulus-driven and undirected search (Janiszewski, 1998).

Purchase action could result from both goal-directed and exploratory search. In goal-directed search, consumers may decide to make the purchase once the accumulated product information satisfies their need. The depth of the search would vary according to the time horizon of the purchase. Purchase could also result from exploratory search if the right stimuli are encountered (Menon & Soman, 2002). Information gathered in exploratory search could assist in a future purchase decision or in augmenting product knowledge.

Taking both the search behaviour and the time horizon of purchase into consideration, Moe (2003) proposes the following four online store visit strategies: directed buying, search/deliberation, hedonic browsing, and knowledge building. Table 1 shows the typology of the store visit strategies and their brief descriptions (reader may refer to Moe (2003) for further details of these strategies).

## Hypotheses development

In examining the influence of demographic variables (gender, age, income, and education) on consumers’ preference of visit strategies, we focus on two of the strategies highlighted in Moe (2003), that is, search/ deliberation and hedonic browsing, due to the following reasons.

First, search/deliberation and hedonic browsing represent the strategies that are more probable for retailers to intervene and convert visit sessions into actual purchases compared to directed buying and knowledge building. In directed buying customers have more or less made up their mind to purchase and the retailer may not need to do much other than facilitating the transactions that follow. In knowledge building customers are primarily interested in enhancing their general understanding about the product/marketplace. There is relatively less that the retailers can effect for these sessions, since the customers’ shopping goal is unclear and the purchase possibility remains remote. In contrast, customers who engage in search/deliberation or hedonic browsing have not reached the final purchase decision phase as in directed buying; nor is their purchase intention still remote as in knowledge building. For customers engaging in search/deliberation, retailers can design software agents to guide their information search and help them in purchase consideration. For those engaging in hedonic browsing, retailers may attempt to present them with the right stimuli (e.g., highlighting the latest book offerings that match their preferred genres) to induce a purchase (Moe, 2003).

Table 1 Typology of online store visit strategies (Moe, 2003)

<table><tr><td>Directed search</td><td>Exploratory search</td></tr><tr><td colspan="2">Immediate purchase:</td></tr><tr><td>Directed Buying• Typically exhibited during the final product decision phase• Highly focused search as the consumer is trying to narrow down the product consideration set</td><td>Hedonic Browsing• Consumers are following cues rather than performing premeditated search routines• Could result in impulsive purchase if consumer’s curiosity is directed appropriately by stimuli encountered</td></tr><tr><td colspan="2">Future purchase:</td></tr><tr><td>Search/deliberation• While also goal oriented, the purchase intention is not immediate as with directed buying• Consumer is still involved in developing the product consideration set through deliberative search</td><td>Knowledge building• Aims primarily at information gathering with no clear intention of immediate purchase• Consumer does not aim to deliberate on a product consideration set, thus exhibiting a less systematic information gathering pattern</td></tr></table>

Second, the search/deliberation and hedonic browsing strategies correspond, respectively, to the two major types of shopping motivations, that is utilitarian and hedonic (Hirschman & Holbrook, 1982). The utilitarian shopping motivation is described as task-related and is directed towards satisfying functional needs (Batra & Ahtola, 1991). It is associated with planned purchase where customers have a clear goal in mind while shopping for a product (Moe, 2003). On the other hand, hedonic shopping motivation is related to fun, sensory stimulation, and enjoyment (Hirschman & Holbrook, 1982). It is associated with impulsive purchase, which results from a consumer’s irresistible, sudden urge to buy a product (Rook & Fisher, 1995). While consumers may be driven by both utilitarian and hedonic motivations to varying degrees, previous research has found that some consumers may shop mainly for utilitarian needs, while others primarily seek hedonic enjoyment (Jarboe & McDaniel, 1987; Brusdal & Lavik, 2005). Accordingly, we investigate the role played by the focal demographic variables (gender, age, income, education) in differentiating individual’s preference between these two strategies.

## Gender

Gender is a common demographic variable used by marketers to segment consumers (Kotler, 1997). Previous research on gender suggested that females tend to be more involved in shopping due to their traditional role as the family purchasing agent, for example in shopping for daily groceries (Slama & Tashchian, 1985). Yet, studies have also noted that this is changing with increasingly more women joining the workforce and no longer serving the role of family purchasing agents (McCall, 1977). As part of this trend, it has been observed that working females are placing more emphasis on leisure as opposed to domestic activities (McCall, 1977). This is echoed in a number of studies where females were found to seek leisure and enjoyment through shopping, that is the social-experiential aspects, as compared to males, who treated shopping primarily as a task with a clear objective to fulfil (Jarboe & McDaniel, 1987; Bergadaa et al., 1995).

However, in the online shopping context, previous research suggests a decrease in gender differences between utilitarian versus hedonic shopping orientations as compared to offline shopping (refer to the Appendix). With the exception of Swaminathan et al. (1999), a number of studies have found that females exhibit a lower social-experiential motivation for online shopping as compared to offline shopping (e.g., Rodgers & Harris, 2003; Dittmar et al., 2004). This may be attributed to the differentiating characteristics of online shopping. Specifically, online shopping still lacks the social-experiential elements afforded by the offline shopping environment, where shoppers are able to interact face to face with sales attendants and products (Jahng et al., 2007). Previous studies have also indicated that consumers prefer to use their full senses (e.g., taste, smell, touch) to experience and assess a product before purchase (Watson et al., 2002), which is not yet feasible in the online shopping environment. According to the media naturalness theory (Kock, 2004, 2005), this would reduce the physiological arousal in the online shopping environment, which may undermine the enjoyment perceived by consumers. Therefore, we expect females’ preference for hedonic browsing over search/deliberation as compared to males to diminish and become insignificant in the online shopping environment:

H1: There is no significant difference between males and females in their preference for search/deliberation or hedonic browsing strategy.

## Age, income, and education

We consider age, income, and education in combination in hypothesizing their effects on consumers’ preference of store visit strategies. This is because their effects may interact as informed by the consumer trait and involvement theory and previous literature discussed below.

Previous studies in the offline shopping context suggest that people tend to be more rational and seek greater certainty in their decision making as they age (Botwinick, 1973). Several explanations have been offered for this tendency. Specifically, as people age, they accumulate experience and knowledge about the marketplace and are clearer about what they want, thus becoming more goal-oriented in their shopping (Bhatnagar et al., 2000). Furthermore, older shoppers are more mature and have come to learn the responsibilities of life (e.g., the need to take care of family and to have long-term plans for themselves). This will make them more rational and careful in their purchase decisions (Brusdal & Lavik, 2005). In contrast, younger shoppers usually have fewer responsibilities, are more carefree, and tend to be more hedonic in shopping (Brusdal & Lavik, 2005). Consistent with this argument, studies in the offline context indicate that older shoppers as more likely to seek and employ external information in their shopping (Williams et al., 1978). Along the same lines, Gutierrez (2004) noted that younger shoppers are more likely to engage in impulsive buying, an indication that they do not plan their purchases as much as older shoppers do.

However, studies investigating the effect of age on online shopping behaviour have thus far provided ambiguous results (refer to the Appendix). For instance, Joines et al. (2003) and Rohm & Swaminathan (2004) did not detect any relationship between consumers’ age and their information search tendency. Klein & Ford (2003), on the other hand, found a significant relationship between consumers’ age and information search for automobile purchase. The ambiguity in findings motivates us to dig deeper into the effect of age in online shopping.

Particularly, the differentiating characteristics of online shopping inform us about how age may influence search tendency in this setting. While the online context offers consumers an abundance of information such as product prices and attributes (Li et al., 1999; Chiang & Dholakia, 2003), it also makes it more time-consuming to locate the information needed and decide at which point adequate information has been gathered for decision making (Berghel, 1997; Li et al., 1999). Thus, while older consumers may have a greater tendency for information seeking (as per the offline shopping findings), this could depend on the opportunity cost of search time to them. Since the opportunity cost of search time depends on consumer’s income, this suggests that age would affect search tendency in conjunction with income. Specifically, we propose that the age effect in increasing the search/deliberation tendency is salient only for shoppers with middle income, based on the consumer trait and involvement theory to be discussed next.

According to the consumer trait and involvement theory, consumers who possess mid-level income may exhibit relatively higher involvement in shopping compared to low- and high-income groups (Slama & Tashchian, 1985). Previous studies found that individuals with high income may be less motivated to engage in information deliberation because they face less price concern in making purchases and value free time more than money (Punj & Staelin, 1983; Slama & Tashchian, 1985). Applying this argument to the online shopping context, the time and effort invested in searching for and analyzing product information before purchase, can be considered as an opportunity cost of time (Punj & Staelin, 1983). For high-income shoppers, such opportunity cost of time is likely to be higher compared to those with lower incomes since their hourly income-generating potential is greater (Punj & Staelin, 1983; Slama & Tashchian, 1985). Consequently, although older shoppers are thought more likely to research their purchases carefully, those having high income may not find it worthwhile to spend their time and effort to perform information search/deliberation.

Also based on the consumer trait and involvement theory, consumers who fall within the low-income range would be less involved than the middle-income group due to their lower purchasing power that limits their product choices. With fewer alternatives to choose from, lowincome shoppers may be less motivated to engage in deliberative search for information on different products. They may instead choose to stick to a limited set of goodvalue products. Thus, although older shoppers are thought to have a preference for the information search strategy, this may not hold for those consumers with low income.

Since online shoppers with middle income have a wider range of product choices and face relatively less opportunity cost of time for information searching, we expect the age effect of increasing the tendency for search/ deliberation over hedonic browsing to be salient in this group. Collectively, the preceding discussion leads us to the following hypotheses:

H2.1: Within the low-income group, there is no significant difference between older shoppers and younger shoppers in their preference for search/deliberation or hedonic browsing strategy.

H2.2: Within the middle-income group, older shoppers are more likely to engage in search/deliberation than hedonic browsing strategy as compared to younger shoppers.

H2.3: Within the high-income group, there is no significant difference between older shoppers and younger shoppers in their preference for search/deliberation or hedonic browsing strategy.

Further, the effect of age in increasing consumer’s tendency for search/deliberation over hedonic browsing is only expected to be salient for shoppers with low education. Socio-economic theory and the human-capital of learned effectiveness perspective both suggest that individuals’ income is closely related to their education (Verba & Nie, 1972; Mirowsky & Ross, 2003). Education acts as a means of earning income, and represents the knowledge, skills, and resources acquired by individuals that structure their job opportunities (Mirowsky & Ross, 2003). This implies a non-purely linear relationship between education and income, whereby individuals with low education may be able to obtain higher income (i.e., low education does not necessarily correspond only to low income, and so on). The rationale is that individuals can develop their knowledge, skills, and resources, and learn to be more effective in their work that increases their income prospect. With this consideration, individuals with low education (e.g., elementary school to high school) may obtain an income from low up to the middle level in general (Arrow et al., 2000; Mirowsky & Ross, 2003), since their opportunity to secure high-income jobs may still be constrained by the higher academic qualifications required. In comparison, individuals with middle to high education are more likely to attain high-income levels with their knowledge and skills acquired and less restriction faced in terms of the qualifications required. Accordingly, we hypothesize the age effect to be salient within the low-education shoppers group, but not in the middle- and high-education groups. This is because the latter two groups are more likely to attain high-income levels, for which the search/deliberation tendency diminishes according to the consumer trait and involvement arguments (Kassarjian, 1981).

Zooming into the low-education group, older shoppers are likely to attain relatively higher income within this particular group, that is they can obtain middle-level income. This may be attributed to their accumulated work experience as compared to the younger shoppers. The general trend of income increasing with age is in accordance with socio-economic theories (Verba & Nie, 1972) as well as census reports (e.g., U.S. Census Bureau, 2005a). Taken together, older shoppers within the loweducation group are likely to adopt the search/deliberation strategy because of both age and middle-income effects. Conversely, older shoppers within the middle- and high-education groups may not exhibit such an effect since they map to the high-income category. In sum, the above discussion leads to the following hypotheses:

H3.1: Within the low-education group, older shoppers are more likely to engage in search/deliberation than hedonic browsing as compared to younger shoppers.

H3.2: Within the middle-education group, there is no significant difference between older shoppers and younger shoppers in their preference for search/ deliberation or hedonic browsing strategy.

H3.3: Within the high-education group, there is no significant difference between older shoppers and younger shoppers in their preference for search/deliberation or hedonic browsing strategy.

It is to be noted that we do not separately hypothesize the effect of the combination of income and education since their joint effect has already been considered in the arguments for hypotheses H3.1–H3.3 above.

## Research methodology

In this section, we first describe the study’s context and the means of data collection. We then explain the cluster analysis performed to identify the focal store visit strategies based on Moe (2003). Whereas the website studied in Moe (2003) dealt with healthcare products, the target website in this study sells books and CDs/DVDs. Books and CDs/DVDs are among the popular mid-priced products that are also considered to be most suitable for e-commerce (Chen et al., 2002). Last, we describe the non-parametric Mann-Whitney tests performed to assess our hypotheses.

## Context of study

In this study, we investigate the differences in shopping behaviour across demographics in the online storefront of one of the largest book retailers. The site sells primarily books with CDs/DVDs augmenting the catalogue. The site structure is clean, stable, and attracts a diverse audience. The structure is also simple and the design of the menu bar, which is always visible on the top, makes navigation easy. On a monthly average, the site had over 3,500,000 unique visitors who contributed to approximately 60,000,000 page views.

## Data collection

The clickstream data employed was provided by a leading Internet audience and media research company. The company recruits and maintains a panel of nearly 40,000 home Internet users in the United States. A proxy-based software is installed by panel members on their computers, which tracks their Internet usage, click-by-click and logs information, for example the requested URLs with time stamps and page content. A combination of household ID and member ID are used to ensure that each panel member is unique. Demographic information (gender, age, income, education) is also collected. We coded gender as a dummy variable where 1 indicates male and 2 indicates female. Age was a continuous variable. Education and income were measured using ordinal scale with six values as shown in Table 3.

A 2-month data sample was collected, which witnessed 25.506 URL clicks from 2.602 browsing sessions of 1.457 unique users. The URL-related data consisted of unique panelist identifiers (i.e., household ID and member ID), the session start and end time, the URL name, and duration spent on the page. The data was converted into a set of measures that define the session behaviour, as specified in Moe (2003). The description of these measures and their expected patterns for the four strategies based on Moe (2003) are shown in Table 2. The shaded cells denote the combination of salient measures that distinguish the respective strategy from the rest (we will discuss this in the results of cluster analysis).

## Cluster analysis

Following Moe (2003), we employed the K-means clustering algorithm (MacQueen, 1967) to analyze a sample of 2,562 sessions (excluding outliers and idle sessions) using the session, focus, and variety measures. The demographic information of the sample is shown in Table 3. The K-means clustering algorithm was used because it can accommodate the large sample sizes associated with customer profiling (Anil et al., 1997). Before the cluster analysis was performed, all the measures were standardized to avoid scale issues. Several solutions were examined with varying numbers of clusters. Starting with a two cluster solution, the number of clusters was increased until one of the following two conditions is met: (1) the added cluster was virtually identical to one of the existing clusters; or (2) the added cluster contained an insignificant number of observations.

## Non-parametric tests of hypotheses related to demographic variables

After the focal visit strategies (search/deliberation and hedonic browsing) were derived from the cluster analysis, we performed non-parametric Mann-Whitney test to assess our hypotheses. Mann-Whitney test was chosen because it does not assume normality of data and homogeneity of variance (Wilcoxon, 1945). As the hypotheses involved testing the effect of demographic variables within specific customer segments, we first extracted the focal customer segments from the sample.

The middle-income group comprises those with an annual household income of USD 50,000–99,999 (N ¼ 565, 48.50% of the sample employing the two strategies), which is in accordance to the U.S. Census Bureau’s report (2005b). For the low-income group, annual household income is less than USD 50,000 (N ¼ 342, 29.36% of the sample); whereas for the highincome group, income ranges from USD 100,000 and above (N ¼ 258, 22.14% of the sample).

The low-education group refers to those with an education level of high school or lower (N ¼ 296, 25.41% of the sample). This categorization is consistent with previous studies, for example Baughcum et al. (2000). The middle-education group represents those who ‘attended some college’ to ‘bachelor’s degree’ (N ¼ 658, 56.48% of the sample), whereas the high-education group comprises those who attained ‘postgraduate degrees’ (N ¼ 211, 18.11% of the sample).

Table 2 Session measures and the expected patterns of online store visit strategies in Moe (2003)

<table><tr><td>Measure</td><td>Description</td><td>Directed buying</td><td>Hedonic browsing</td><td>Search/ deliberation</td><td>Knowledge building</td></tr><tr><td colspan="6">Session</td></tr><tr><td>PAGES</td><td>Total no. of non-administrative pages viewed</td><td>High</td><td>Low</td><td>High</td><td>Low</td></tr><tr><td>PGTIME</td><td>Avg. time spent on each page</td><td>High</td><td>Moderate</td><td>Moderate</td><td>High</td></tr><tr><td colspan="6">Focus</td></tr><tr><td>HOME</td><td>% of pages that were home pages</td><td>Low</td><td>Moderate</td><td>Low</td><td>Moderate</td></tr><tr><td>INFO</td><td>% of pages that were information-related pages</td><td>Low</td><td>Moderate</td><td>Moderate</td><td>High</td></tr><tr><td>CATG</td><td>% of pages that were category level pages</td><td>Moderate</td><td>High</td><td>High</td><td>Low</td></tr><tr><td>SEARCH</td><td>% of pages that were search result pages</td><td>Moderate</td><td>Moderate</td><td>High</td><td>Low</td></tr><tr><td>PROD</td><td>% of pages that were product level pages</td><td>High</td><td>Moderate</td><td>Moderate</td><td>Low</td></tr><tr><td colspan="6">Variety</td></tr><tr><td>DIFFCAT</td><td>% of category pages that were unique</td><td>Moderate</td><td>High</td><td>Moderate</td><td>Low</td></tr><tr><td>DIFFSEARCHa</td><td>% of search pages that were unique</td><td>Moderate</td><td>Low</td><td>High</td><td>Low</td></tr><tr><td>DIFFPROD</td><td>% of product pages that were unique</td><td>Low</td><td>High</td><td>High</td><td>Low</td></tr><tr><td>PRODCAT</td><td>Average no. of unique product pages viewed per category</td><td>Moderate</td><td>Low</td><td>High</td><td>Low</td></tr><tr><td>MAXREP</td><td>Maximum no. of repeated viewings of product pages</td><td>High</td><td>Low</td><td>Moderate</td><td>Low</td></tr></table>

<sup>a</sup>We omitted the measures related to brand level pages (BRANDPG and DIFFBRAND) that were used in Moe (2003). These measures are less applicable to the site structure and product categorization in the chosen e-commerce site that sells books and CDs/DVDs. Instead we added DIFFSEARCH that reflects the variety in the kinds of search performed by a customer. The measure is expected to be particularly high for the search/ deliberation strategy.

Table 3 Demographic information of sample

<table><tr><td colspan="2">Gender</td></tr><tr><td>Male</td><td>38.1%</td></tr><tr><td>Female</td><td>61.9%</td></tr><tr><td colspan="2">Age (years)</td></tr><tr><td colspan="2">Mean = 44.70</td></tr><tr><td colspan="2">Standard deviation = 16.02</td></tr><tr><td colspan="2">Education level</td></tr><tr><td>Elementary school</td><td>5.3%</td></tr><tr><td>Some high school</td><td>5.7%</td></tr><tr><td>High school graduate</td><td>15.2%</td></tr><tr><td>Some college</td><td>33.1%</td></tr><tr><td>Bachelor&#x27;s degree</td><td>24.4%</td></tr><tr><td>Postgraduate degree</td><td>16.3%</td></tr><tr><td colspan="2">Income level (USD)</td></tr><tr><td>0–24,999</td><td>7.0%</td></tr><tr><td>25,000–49,999</td><td>25.3%</td></tr><tr><td>50,000–74,999</td><td>26.4%</td></tr><tr><td>75,000–99,999</td><td>19.0%</td></tr><tr><td>100,000–149,999</td><td>13.0%</td></tr><tr><td>150,000 and above</td><td>9.3%</td></tr></table>

## Data analyses and results

In this section we first report the results of cluster analysis followed by the findings of hypotheses testing using the Mann-Whitney test.

## Results of cluster analysis

The results of cluster analysis (Table 4) are largely consistent with those of Moe (2003). Cluster 1 in our study (Table 4) mostly fitted with the characteristics of the directed buying strategy outlined in Table 2. The highsession measures, with a cluster average of 33.74 pages viewed (PAGES) and each page being viewed (PGTIME) on an average for 29.37 s, indicate deep involvement in the session with 32.84% of the total pages devoted to product-level pages (high PROD). The distinctive characteristic of this cluster is the high repeated product page views (MAXREP ¼ 1.83), which confirms the expectation that the customer repeatedly viewed the same product page. The only notable deviation from Moe (2003) is the high level of PRODCAT observed (moderate level in Moe (2003)). This difference could be due to the different products employed, which will be further elaborated in the Discussion and Implications section.

Cluster 2 (Table 4) largely fitted with the hedonic browsing strategy outlined in Table 2. A low product to category ratio (PRODCAT ¼ 2.49) and a relatively low repeated product page views (MAXREP ¼ 1.16) suggest that the sessions did not involve heavy deliberation on a specific product. The unfocused nature of the sessions is evident in the high variety of product pages viewed, that is the highest different products viewed among all (DIFFPROD ¼ 92.82%). This is typical of hedonic behaviour where the customer navigates following stimuli. The only difference that was observed compared to Moe (2003) is the relatively low measures related to category pages (CATPG and DIFFCAT). Again this could be due to the different products employed as discussed in the ‘Discussion and implications’ section.

Cluster 3 (Table 4) fitted well with the search/deliberation strategy outlined in Table 2. The presence of both high number of search pages (SEARCH ¼ 28.38%) and the variety in the search (DIFFSEARCH ¼ 67.52%) suggest a deep search-focused session. Further, the product to category pages ratio (PRODCAT ¼ 48.47), although lower than that of directed buying, is substantially higher than the corresponding values for hedonic browsing and knowledge building.

Cluster 4 (Table 4) represents knowledge building sessions as described in Table 2. The sessions are associated with a large number of informational page viewings (high INFO, 75.05%) and little presence of other pages (low CATG, SEARCH, and PROD). Average page view times are high (PGTIME ¼ 35.34s), suggesting effort to absorb information in the pages. The focus of these sessions is knowledge gathering and there is little intention to purchase, hence the low value of repeated product page views (MAXREP ¼ 0.21).

Another cluster emerged from the analysis as with Moe (2003). Cluster 5 is characteristic of visitors viewing few pages (PAGESo4) and spending less time on the pages with most of the focus being on the home page. These sessions are termed ‘Shallow’ to represent visitors who may have visited the site just to see what the site is about. Such behaviour is considered common partly because the Internet experiences inflows of new users who are exploring the different features of websites (Moe, 2003).

In sum, the results of the cluster analysis provide support for Moe’s (2003) typology by demonstrating the prominent characteristics of the four strategies as discussed above. Hence, we will test the hypotheses based on the identified sessions that demonstrate the search/ deliberation and hedonic browsing strategies.

## Results of hypotheses testing

The Mann-Whitney test results for the hypotheses testing are shown in Table 5.

For gender (Table 5), there is no significant difference between males and females in their preference of search/ deliberation or hedonic browsing, as expected (H1 supported). On the other hand, significant difference across the two strategies in terms of age is found within the middle-income and the low-education groups. The mean ranks in Table 5 indicate that shoppers in these two groups (middle-income and low-education) who adopted a search/deliberation strategy have a comparatively higher age than those adopting a hedonic browsing strategy. This implies that older shoppers in the two groups are more likely to prefer search/deliberation over hedonic browsing than younger shoppers (H2.2 and H3.1 supported).

Table 4 Results of cluster analysis in our study

<table><tr><td rowspan="2">Cluster</td><td>Directed buying</td><td>Hedonic browsing</td><td>Search/deliberation</td><td>Knowledge building</td><td>Shallow</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>N</td><td>45</td><td>707</td><td>458</td><td>41</td><td>1311</td></tr><tr><td>%</td><td>1.76</td><td>27.59</td><td>17.88</td><td>1.60</td><td>51.17</td></tr><tr><td colspan="6">Session measures</td></tr><tr><td>PAGES (number of)</td><td>33.74 (High)</td><td>5.76</td><td>24.87</td><td>3.83</td><td>3.52</td></tr><tr><td>PGTIME (seconds)</td><td>29.37</td><td>30.77</td><td>29.20</td><td>35.34 (High)</td><td>25.36</td></tr><tr><td colspan="6">Focus measures (% pages)</td></tr><tr><td>HOME</td><td>6.78%</td><td>10.70%</td><td>9.77%</td><td>16.33%</td><td>28.12%</td></tr><tr><td>INFO</td><td>2.17%</td><td>0.62%</td><td>1.29%</td><td>75.05% (High)</td><td>0.52%</td></tr><tr><td>CATPG</td><td>7.43%</td><td>0.93%</td><td>28.33%</td><td>0.96% (Low)</td><td>31.86%</td></tr><tr><td>SEARCH</td><td>38.92%</td><td>21.48%</td><td>28.38% (High)</td><td>4.38% (Low)</td><td>19.97%</td></tr><tr><td>PROD</td><td>32.84% (High)</td><td>30.35%</td><td>21.66%</td><td>1.49% (Low)</td><td>0.01%</td></tr><tr><td colspan="6">Variety measures</td></tr><tr><td>DIFFCAT</td><td>85.52%</td><td> $0.85\%^a$ </td><td>76.92%</td><td>3.86%</td><td>40.55%</td></tr><tr><td>DIFFSEARCH</td><td>58.12%</td><td>44.76%</td><td>67.52% (High)</td><td>21.40%</td><td>40.65%</td></tr><tr><td>DIFFPROD</td><td>83.18%</td><td>92.82% (High)</td><td>87.32%</td><td>7.70%</td><td>0.02%</td></tr><tr><td>PRODCAT (page views)</td><td> $440.17^a$ </td><td>2.49 (Low)</td><td>48.47 (High)</td><td>1.92</td><td>1.91</td></tr><tr><td>MAXREP (page views)</td><td>1.83 (High)</td><td>1.16 (Low)</td><td>1.49</td><td>0.21 (Low)</td><td>0.07</td></tr></table>

<sup>a</sup>Indicates the difference between our results and those of Moe (2003).

Last, there is no significant difference in the mean ranks between the shoppers adopting a search/deliberation strategy and those adopting a hedonic browsing strategy within the low-income, high-income, middle-education, and high-education groups, indicating no significant difference in their age (H2.1, H2.3, H3.2, and H3.3 supported).

## Discussion and implications

Demographics continue to be important means through which marketers segment and target consumers (Nielsen, 2009; Thomson Reuters, 2009). However, the utility of these simple yet powerful consumer indicators are confounded in the online shopping context due to the ambiguous findings about their effects indicated by existing research.

Our study posits that to better understand demographic effects on online consumer preferences, a more comprehensive approach as employed in this study may be needed. First, in deriving the dependent variable of shoppers’ online store visit strategy, our study taps on the Internet’s capability to unobtrusively track shoppers’ idiosyncratic steps of surfing, that is clickstream data (Vriens & Grigsby, 2001), instead of the perceptual or subjective measures employed in most previous research (e.g., Joines et al., 2003; Dittmar et al., 2004). Our approach based on objective clickstream data may allow the dependent variable to be more accurately derived. Second, in examining the effects of demographics in the online shopping context, our study employs these variables in combinations, which are seldom considered in prior research. This helps to uncover the combined effects of demographic variables, for example age is a salient differentiator of store visit strategy only in the middle-income consumer group. Third, the effects of the demographic variables are theoretically derived through the lenses of media naturalness theory and consumer trait and involvement theory. The hypotheses developed were then empirically tested using actual consumers’ demographic and clickstream data from a real e-commerce website selling books and CDs/DVDs.

Collectively, our approach uncovers the effect of age on shoppers’ preference of online store visit strategies within the middle-income and low-education groups. Should a simplistic approach of investigating a single demographic variable at a time have been employed, such effects may go undetected. It is hoped that our research can provide insights to both e-commerce researchers and practitioners on how demographic variables may be considered in the online shopping context.

## Theoretical implications

Our study responds to the need to re-examine the effects of demographic variables in the online shopping context given the ambiguous findings from previous literature. The significant effects found suggest that previous approaches using broad demographic classifications to differentiate customers may not be adequate. Rather, considering the effects of related demographic variables in combinations, as is done in this study, may lead to better explanations of variations in online shopping behaviour. Through the theoretical lens of the consumer trait and involvement theory, our approach investigates the variations within specific demographic segments, for example low-education shoppers. This is also different from modelling the joint effect of demographic variables as an interaction (where the variables are assumed as continuous), in which the effects may not be seen. Our approach is consistent with previous marketing literature indicating the value of demographic segments for understanding consumers’ characteristics (Frank et al., 1972).

Table 5 Mann-Whitney test results

<table><tr><td></td><td></td><td>Mean rank</td><td>Mann-Whitney U</td><td>Wilcoxon W</td><td>Z</td><td>Asymp. Sig.(two-tailed)</td><td>Result</td></tr><tr><td rowspan="2">H1(Gender)(N=1165)</td><td>Search/Deliberation</td><td>596.32</td><td>36,839.50</td><td>406,079.50</td><td>-1.304</td><td>0.192</td><td>Supported</td></tr><tr><td>Hedonic browsing</td><td>574.37</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">H2.1(Age – Low-income group)(N=342)</td><td>Search/Deliberation</td><td>175.02</td><td>13,205.50</td><td>36,425.50</td><td>-0.506</td><td>0.613</td><td>Supported</td></tr><tr><td>Hedonic browsing</td><td>169.42</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">H2.2(Age – Mid-income group)(N=565)</td><td>Search/Deliberation</td><td>301.13</td><td>33,413.00</td><td>96,959.00</td><td>-2.023</td><td> $0.043^a$ </td><td>Supported</td></tr><tr><td>Hedonic browsing</td><td>272.36</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">H2.3(Age – High-income group)(N=258)</td><td>Search/Deliberation</td><td>132.82</td><td>7891.50</td><td>17,207.50</td><td>-0.676</td><td>0.499</td><td>Supported</td></tr><tr><td>Hedonic browsing</td><td>126.53</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">H3.1(Age – Low-education group)(N=296)</td><td>Search/Deliberation</td><td>161.44</td><td>8939.50</td><td>25,229.50</td><td>-2.090</td><td> $0.037^a$ </td><td>Supported</td></tr><tr><td>Hedonic browsing</td><td>140.16</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">H3.2(Age – Mid-education group)(N=658)</td><td>Search/Deliberation</td><td>334.73</td><td>50,802.50</td><td>127,438.50</td><td>-0.583</td><td>0.560</td><td>Supported</td></tr><tr><td>Hedonic browsing</td><td>325.93</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">H3.3(Age – High-education group)(N=211)</td><td>Search/Deliberation</td><td>103.93</td><td>4945.00</td><td>7795.50</td><td>-0.366</td><td>0.715</td><td>Supported</td></tr><tr><td>Hedonic browsing</td><td>107.14</td><td></td><td></td><td></td><td></td><td></td></tr></table>

<sup>a</sup>Indicates significant difference between search/deliberation and Hedonic browsing.

Additionally, our research highlights the value of employing clickstream data and a robust profiling technique to more objectively derive the dependent variable, that is consumers’ motivations and needs as manifested in their store visit strategies (Moe, 2003). Therefore, this study proposes a more comprehensive approach of treating both the independent and dependent variables in studying the effects of demographic variables on online consumer preferences. Furthermore, our research extends the use of the media naturalness theory and consumer trait and involvement theory to the investigation of demographic effects in the online shopping context. Last, the study also contributes towards the consumer behaviour and marketing literature by extending the robust profiling technique developed by Moe (2003) and tested on healthcare products, to a different type of product, that is books and CDs/DVDs, which are among the most popular products sold online.

## Practical implications

A primary concern of e-commerce practitioners is to accurately target different segments of store visitors and decide on the appropriate marketing mix to influence their purchase behaviour. Our study suggests that online merchants would benefit from paying attention to specific demographic segments, such as the middleincome shoppers and the low-education shoppers. The middle-income shoppers segment has been recognized to constitute the dominant group of online shoppers, whereas the low-education shoppers segment is considered the promising next wave of online shoppers (Ernst & Young, 2000; Yahoo! & ACNielsen, 2001). With technologies and websites becoming easier to use, it is expected that an increasing number of low-education consumers will be shopping online. However, our study cautions that it is inadequate for online merchants to merely focus on these existing or promising demographic segments. It is important for online merchants to also consider the effect of age in these segments to understand consumers’ preference of store visit strategies as indicated in our study. Specifically, older shoppers within the middleincome and low-education groups are found to have a higher tendency towards adopting a search/deliberation strategy. With this knowledge, online merchants may focus their resources on providing shoppers fitting these demographic characteristics with tools that can facilitate product information search and deliberation to induce their purchase.

Online merchants may also benefit from the consideration of the effects of combinations of related demographic variables (i.e., age and income; age and education). With an understanding of the joint effects of these demographic variables, online merchants may flexibly employ any of the variables available to them to perform effective segmentation on consumers. Even if consumers’ age is not available, online merchants may still utilize their income and education characteristics since their joint effect has been incorporated in our arguments for hypotheses H3.1–H3.3. Specifically, one may expect loweducation shoppers with relatively higher income to show a preference for search/deliberation over hedonic browsing. As we have highlighted through the humancapital of learned effectiveness perspective, education may be associated with income such that low-education shoppers are most likely to have a low to middle-income level (Arrow et al., 2000; Mirowsky & Ross, 2003). Thus, online merchants may deduce that the higher-end of the group (i.e., those earning middle-income level) should demonstrate a preference for search/deliberation over hedonic browsing.

In sum, our findings serve to reinforce the value of demographics in the online shopping context, particularly in profiling consumers and selecting the appropriate marketing interventions. The implication for online merchants is thus to encourage customers to volunteer such information. This can be attempted by offering customers various value-added features, for example personalized recommendations, in exchange for this information.

## Limitations, future research, and conclusion

Findings from this study need to be interpreted in light of its limitations. A limitation of this study is its intra-site focus, that is the clickstream data analyzed is reflective of the behaviour of customers in a single e-commerce site. However, online shoppers are sometimes found to indulge in comparison shopping to find product information from competing sites. A few studies such as Park & Fader (2004) have attempted to explore this issue. Future research may build on our study and conduct a systematic inter-site comparison to understand the possible differences in shopping behaviour vis-a\`-vis demographics across different websites. Also our findings are based on clickstream data originating from one country, which may limit their generalizability. Future research may be conducted in other countries to validate our findings.

Further, although our results of cluster analysis provide good support for the typology developed by Moe (2003), there are two differences between our results and those of Moe (2003) that deserve attention. One such difference lies in the high ratio of product to category pages (PRODCAT) observed in the directed buying sessions while it should be moderate based on the results of Moe (2003). Another difference concerns the lower than expected values found for session measures related to category pages (CATPG and DIFFCAT) in the hedonic browsing sessions. These differences could arise from the different nature of the products employed in Moe (2003) (healthcare products) versus our study (books and CDs/ DVDs), which may present interesting areas for future research. The nature of products may impact the way customers gather information and make purchases (Beatty & Smith, 1987). There are various ways of classifying products based on their nature, for example ease of assessing the product attributes; and whether the products convey cultural meanings. The former approach classifies products into search, experience, or credence types (Darby & Karni, 1973), whereas the latter classifies products into cultural and non-cultural types (WIPO, 2003).

Books and CDs/DVDs are examples of the search products type, in which customers can assess the majority of attributes (e.g., size and price) before purchase. In contrast, the healthcare products studied in Moe (2003) belong to the credence type, in which their attributes are difficult to verify even after consumption (e.g., the exact ingredients of health supplements). Online shoppers are able to access more product pages for search products compared to credence products because the majority of their attributes can be easily extracted and digitized (Lal & Sarvary, 1999). A customer who is nearing the decision to purchase books may be particularly interested to glance through the digitized sample pages of the books under consideration. As the range of book categories has been narrowed down in the directed buying stage, the viewing of the different sample pages may instead contribute to a high product to category pages ratio (PRODCAT). However, this reasoning requires further investigation that includes the different product types in the sample, and statistically tests their differences.

In addition, books and CDs/DVDs are also instances of cultural products, which are defined as goods that ‘convey ideas, symbols, and ways of life’ (WIPO, 2003, p. 85). Such products can typically be classified into different genres based on their perceived similarities, for example ‘fiction’ and ‘non-fiction’ for books. Prior research suggests that the genres of cultural products vary in their appeal to consumers (Litman & Ahn, 1998). Consumers’ preference towards certain genres of cultural products could impact the way they engage in hedonic browsing. Specifically, consumers may just visit the few preferred genres/categories of books when they shop for hedonic enjoyment, which contradicts the findings from Moe (2003). During hedonic browsing for healthcare products (a non-cultural product), consumers may not have an emotional attachment towards particular product categories. Rather, they may randomly browse through different product categories with the hope of discovering something interesting. Again this reasoning requires further research.

Last, although our results did not indicate gender differences in the online context and noted consumer’ inability to interact with the product face-to-face as a potential cause, future research may investigate products that do not require such interaction, for example digital products (Hui & Chau, 2002). It will be useful to study if females would prefer hedonic browsing while shopping for these products online.

In conclusion, e-commerce marketers must identify customers’ underlying shopping motivations and needs

## About the authors

Chee Wei Phang is Assistant Professor in the Department of Information Management and Information Systems at Fudan University, China. He obtained his B. Comp and Ph.D. from the National University of Singapore (NUS). His research has appeared in the Journal of the Association for Information Systems, IEEE Transactions on Engineering Management, Communications of the ACM, and Journal of Strategic Information Systems; and in the proceedings of the ICIS and HICSS among others. His research interests are in virtual communities, e-commerce, knowledge management, and IT in public sector.

Atreyi Kankanhalli is Associate Professor in the Department of Information Systems at the National University of Singapore (NUS). She obtained her B. Tech. from the Indian Institute of Technology Delhi, and Ph.D. from NUS. She had visiting stints at the University of California Berkeley and Indian Institute of Science Bangalore. Dr. Kankanhalli has considerable work experience in industrial R&D and consulted for several organizations. Her research interests are in knowledge management, IT-enabled organizational forms and services, and IT in public sector. Her work has appeared in the MIS Quarterly, Journal of Management Information Systems, Journal of the Association for Information Systems, IEEE Transactions on Engineering Management, Communications of the ACM, Journal of Strategic Information Systems, Decision Support Systems, and the proceedings of the ICIS and HICSS among others. She serves on several information systems conference committees and on the editorial

## References

AGARWAL R and PRASAD J (1999) Are individual differences germane to the acceptance of new information technologies? Decision Sciences 30(2), 361-391.

AHUJA M, GUPTA B and RAMAN P (2003) An empirical investigation of online consumer purchasing behavior. Communications of the ACM 46(12). 145–151

ANIL C, CARROLL JD, GREEN PE and ROTONDO JA (1997) A feature-based approach to market segmentation via overlapping K-centroids clustering. Journal of Marketing Research 34(3), 370–377.

in order to effectively satisfy them. Understanding the influence of demographics on customer’s preferred strategies for visiting online stores such as through this study can help practitioners to select the appropriate interventions to meet different customers’ needs and realize the promise of the Internet for their business.

## Acknowledgements

This study is supported by the Singapore’s Ministry of Education research grant number R-253-000-063-646 and the National Natural Science Foundation of China research grant number 70828003.

boards of the MIS Quarterly, IEEE Transactions on Engineering Management, and Information and Management, among others.

Karthik Ramakrishnan obtained his Bachelor of Computing (Honors) in Information Systems from the National University of Singapore. He was selected for the prestigious NUS Overseas Colleges programme at Stanford University, where, apart from pursuing businessrelated courses, he was involved in creating business plans and pitching to venture capitalists. At present, Karthik is leading Business Development and Marketing at Imfinity, a technology consulting company, where he is responsible for identifying new opportunities and fueling the company’s growth internationally. His research interests are in e-commerce and consumer behaviour.

Krishnamurthy S. Raman is a retired professor of Information Systems, National University of Singapore. His research interests include group support systems, information technology in small businesses, government policy and information technology, and cross national/ cultural issues in information technology. His research papers in these areas have been presented in international conferences and published in international journals including Information Systems Research, Journal of Management Information Systems, Decision Support Systems, ACM Transactions on Computer-Human Interaction, Communications of the ACM, and European Journal of Information Systems.

ARROW KJ, BOWLES S and DURLAUF SN (2000) Meritocracy and Economic Inequality, Princeton University Press, Princeton, NJ.

ASSAEL H (1992) Consumer Behavior and Marketing Action, PWS-KENT, Boston, MA.

B R and A OT (1991) Measuring the hedonic and utilitarian sources of consumer attitudes. Marketing Letters 2(2), 159–170.

B AE, C LA, D CM, P SW and W RC (2000) Maternal perceptions of overweight preschool children. Pediatrics 106(6). 1380–1386.

BEATTY S and SMITH S (1987) External search effort: an investigation across several product categories. Journal of Consumer Research 14(1), 83–95.

BERGADAA M, FAURE C and PERRIEN J (1995) Enduring involvement with shopping. Journal of Social Psychology 135(1), 17–25.

BERGHEL H (1997) Cyberspace 2000: dealing with information overload. Communications of the ACM 40(2), 19–24.

BHATNAGAR A, MISRA S and RAO HR (2000) On risk, convenience, and Internet shopping behavior. Communications of the ACM 43(11), 98–105.

BOTWINICK J (1973) Aging and Behavior, Springer, New York.

BRUSDAL R and LAVIK R (2005) Young hedonist and rational grown ups? A closer look at consumer identities in Norway. Paper presented at ESA Conference; 9–12 September, Torun, Polen.

BURROUGHS RE and SABHERWAL R (2001) Determinants of retail electronic purchasing: a multi-period investigation. Journal of Information System Operation Research 40(1), 35–56.

CHEN L, GILLENSON M and SHERRELL D (2002) Enticing online consumers: an extended technology acceptance perspective. Information & Management 39(8), 705–719.

CHIANG K-P and DHOLAKIA RB (2003) Factors driving consumer intention to shop online: an empirical investigation. Journal of Consumer Psychology 13(1–2), 177–183.

DARBY MR and KARNI E (1973) Free competition and the optimal amount of fraud. Journal of Law and Economics 16(April), 67–86.

D AR, K ST and H YC (1999) Gender differences in the effects of media richness. Small Group Research 30(4), 405–437.

DHOLAKIA U and BAGOZZI R (2001) Consumer behavior in digital environments. In Digital Marketing (WIND J and MAHAJAN V, Eds), pp 163–200, Wiley, New York.

DITTMAR H, LONG K and MEEK R (2004) Buying on the Internet: gender difference in on-line and conventional buying motivations. Sex Roles 50(5/6), 423–444.

ERNST & YOUNG (2000) Global online retailing. An Ernst & Young Special Report.

FAH W, GORDON MD and PATHAK P (2005) Effective profiling of consumer information retrieval needs: a unified framework and empirical comparison. Decision Support Systems 40(2), 213–233.

FRANK RE, MASSY WF and WIND Y (1972) Market Segmentation, Prentice-Hall, Eaglewood Cliffs, NJ.

GUTIERREZ BPB (2004) Determinants of planned and impulse buying: the case of the Philippines. Asia Pacific Management Review 9(6), 1061–1078.

HIRSCHMAN EC and HOLBROOK MB (1982) Hedonic consumption; emerging concepts, methods, and propositions. Journal of Marketing 46(3), 92–101.

HUBERMAN BA, PIROLLI P, PITKOW JE and LUKOSE RM (1998) Strong regularities in World Wide Web surfing. Science 280(5360), 95–97.

HUI KL and CHAU PYK (2002) Classifying digital products. Communications of the ACM 45(6), 73–79.

JAHNG J., JAIN H and RAMAMURTHY K (2007) Effects of interaction richness on consumer attitudes and behavioral intentions in e-commerce: some experimental results. European Journal of Information Systems 16, 254-269.

JANISZEWSKI C (1998) The influence of display characteristics on visual exploratory search behavior. Journal of Consumer Research 25(3), 290–301.

JARBOE GR and MCDANIEL CD (1987) A profile of browsers in regional shopping malls. Journal of the Academy of Marketing Science 15(1), 46–53.

JOINES JL, SCHERER CW and SCHEUFELE DA (2003) Exploring motivations for consumer Web use and their implications for e-commerce. Journal of Consumer Marketing 20(2), 90–108.

KASSARJIAN HH (1981) Low involvement – a second look. In Advances in Consumer Research (MONROE KB, Ed.), Vol. 8, pp 31–34, Association for Consumer Research. Ann Arbor, MI

KLEIN LR and FORD GT (2003) Consumer search for information in the digital age: an empirical study of prepurchase search. Journal of Interactive Marketing 17(3), 29–49.

KOCK N (2004) The psychobiological model: towards a new theory of computer-mediated communication based on Darwinian evolution. Organization Science 15(3), 327–348.

KOCK N (2005) Media richness or media naturalness? The evolution of our biological communication apparatus and its influence on our

behavior toward e-communication tools. IEEE Transactions on Professional Communication 48(2), 117–130.

KOTLER P (1997) Marketing Management: Analysis Planning and Control, Prentice-Hall. NI.

KOUFARIS M (2002) Applying the technology acceptance model and flow theory to online consumer behavior. Information Systems Research 13(2), 205–223.

LAAKSONEN P (1994) Consumer Involvement: Concepts and Research, Routledge, London.

LAL R and SARVARY M (1999) When and how is the Internet likely to decrease price competition? Marketing Science 18(4), 485–503.

LI H, KUO C and RUSSELL MG (1999) The impact of perceived channel utilities, shopping orientations, and demographics on the consumer’s online buying behavior. Journal of Computer Mediated Communication 5(2), 1–20.

LITMAN B and AHN H (1998) Predicting financial success of motion pictures: the early ‘90s experience. In The Motion Picture Mega Industry (LITMAN BR, Ed.), pp 172–197, Allyn Bacon, Needham Heights, MA.

MACQUEEN JB (1967) Some methods for classification and analysis of multivariate observations. In Proceedings of the 5th Berkeley Symposium on Mathematical Statistics and Probability (LE CAM LM and NEYMAN J, Eds), pp 281–297, University of California Press, Berkeley.

M C SH (1977) Meet the ‘Workwife’. Journal of Marketing 41 (Summer), 55–65.

MENON S and SOMAN D (2002) Managing the power of curiosity for effective web advertising strategies. Journal of Advertising 31(3), 1–14.

MIROWSKY J and ROSS CE (2003) Education, Social Status, and Health, Aldine Transaction, New Brunswick, NJ.

MOE WW (2003) Buying, searching, or browsing: differentiating between online shoppers using in-store navigational clickstreams. Journal of Consumer Psychology 13(1/2), 29–40.

MooN B-L (2004) Consumer adoption of the internet as an information search and product purchase channel: some research hypotheses. International Journal of Internet Marketing and Advertising 1(1), 104–118.

MORRIS MG and VENKATESH V (2000) Age differences in technology adoption decisions: implications for a changing work force. Personnel Psychology 53, 375–403.

NIELSEN (2009) Segmentation and targeting: demographics. Nielsen Expertise, The Nielsen Company US. [WWW document] http://en-us .nielsen.com/tab/expertise/segmentation\_and\_targeting/demographics, accessed.11 November 2009

N H and P PE (2005) Search mode and purchase intention in online shopping behavior. International Journal of Internet Marketing and Advertising 2(4), 288–306.

PARK YH and FADER PS (2004) Modeling browsing behavior at multiple websites. Marketing Science 23(3), 280–303.

P GN and S R (1983) A model of consumer information search behavior for new automobiles. Journal of Consumer Research 9(4), 366–380.

RODGERS S and HARRIS MA (2003) Gender and e-commerce: an exploratory study. Journal of Advertising Research 43(3), 322–329.

ROHM AJ and SWAMINATHAN V (2004) A typology of online shoppers based on shopping motivations. Journal of Business Research 57(7), 748–758.

ROOK DW and FISHER RJ (1995) Normative influences on impulsive buying behavior. lourngl of Consumer Resegrch 22(3). 305–313.

SINGH SN and DALAL NP (1999) Web home pages as advertisements. Communications of the ACM 42(8), 91–98.

SLAMA ME and TASHCHIAN A (1985) Selected socioeconomic and demographic characteristics associated with purchasing involvement. Journal of Marketing 49(1), 72–82.

SWAMINATHAN V, LEPOWSKA-WHITE E and RAO BP (1999) Browsers or buyers in cyberspace? Journal of Computer Mediated Communication 5(2), 1–23.

THOMSON REUTERS (2009) Consumer expectations for healthcare services: demographics matter. Thomson Reuters White Paper, 17 June, [WWW document] http://thomsonreuters.com/content/healthcare/white\_ papers/consumer expectations, accessed 11 November 2009.

U.S. CENSUS BUREAU (2005a) Income, poverty, and health insurance coverage in the United States: 2004. Current Population Reports, U.S. Government Printing Office, Washington, D.C.

U.S. CENSUS BUREAU (2005b) Income Data. 2005 Economic Survey, U.S. Government Printing Office, Washington, D.C.

VAN DER HEIJDEN H, VERHAGEN T and CREEMERS M (2003) Understanding online purchase intentions: contributions from technology and trust perspectives. European Journal of Information Systems 12(1), 41–48.

VERBA S and NIE N (1972) Participation in America: Political Democracy and Social Equality, Harper and Row, New York.

VRIENS M and GRIGSBY M (2001) Building profitable online customerbrand relationships. Marketing Management 10(4), 34–39.

VROOMEN B, DONKERS B, VERHOEF PC and FRANSES PH (2003) Purchasing complex services on the Internet: an analysis of mortgage loan acquisitions. ERIM Report Series.

WATSON RT, LEYLAND FP, PIERRE B and GEORGE MZ (2002) U-commerce: expanding the universe of marketing. Journal of the Academy of Marketing Science 30(4), 329–343.

WILCOXON F (1945) Individual comparisons by ranking methods. Biometrics Bulletin 1(6), 80–83.

WILLIAMS RH, PAINTER JJ and NICHOLAS HR (1978) A policy-oriented typology of grocery shoppers. Journal of Retailing 54(1), 27–43.

WIPO (2003) Guide on Surveying the Economic Contribution of the Copyright-Based Industries. UNESCO, Geneva.

YAHOO! INC CALIF and ACNIELSEN NY (2001) Yahoo!/ACNielsen Internet Confidence Index [WWW document] http://docs.yahoo.com/docs/pr/ release809.html, accessed 11 November 2009.

## Appendix

See Table A1.

Table A1 Summary of previous e-commerce research on the effects of demographics on shoppers’ needs and preferences

<table><tr><td>Author (date)</td><td>Methodology</td><td>Measurement of shoppers' preferences and needs</td><td>Relevant findings on demographic effects</td></tr><tr><td colspan="4">Gender</td></tr><tr><td>Dittmar et al. (2004)</td><td>Performed two studies to examine gender differences in attitudes towards conventional and online shopping. Study 1 Thematic analysis based on 113 written accounts from university students on shopping perceptions Study 2 Survey of 240 university students</td><td>Perceptual scale measures</td><td>No obvious difference between males and females in terms of their functional and social-experiential motivations in shopping online</td></tr><tr><td>Joines et al. (2003)</td><td>Survey of 59 university students and 59 New York State residents</td><td>Subjective measure (percentage of time spent on searching for product and service-related information)</td><td>Gender has no effect on consumers' tendency to search for more product and service-related information in online shoppinga</td></tr><tr><td>Rodgers &amp; Harris (2003)</td><td>Survey of 227 university students</td><td>Perceptual scale measures</td><td>Females find online shopping to be less emotionally gratifying, which implies a less obvious difference between males and females in their need for hedonic enjoyment while shopping online</td></tr><tr><td>Swaminathan et al. (1999)</td><td>Survey of 428 Internet users</td><td>Perceptual scale measures</td><td>Males are less motivated than females by social needs in online shopping</td></tr><tr><td colspan="4">Age</td></tr><tr><td>Joines et al. (2003)</td><td>Survey of 59 university students and 59 New York State residents</td><td>Subjective measure (percentage of time spent on searching for product and service-related information)</td><td>Age has no effect on consumers' tendency to search for more product and service-related information in online shoppinga</td></tr><tr><td>Klein &amp; Ford (2003)</td><td>Survey of 337 individuals who are going to purchase a car in the next 6 months, or who have purchased a car in the past 18 months</td><td>Self-reported measure (time spent on information searching and number of sources used)</td><td>Age is negatively related to consumers' tendency to engage in information searchb</td></tr><tr><td colspan="4">Table A1 Continued</td></tr><tr><td>Rohm &amp; Swaminathan (2004)</td><td>Survey of 412 online shoppers</td><td>Perceptual scale measures</td><td>Age has no effect on consumers' preference to engage in searching for information across different shops, products and brands</td></tr><tr><td>Income</td><td></td><td></td><td></td></tr><tr><td>Joines et al. (2003)</td><td>Survey of 59 university students and 59 New York State residents</td><td>Subjective measure (percentage of time spent on searching for product and service-related information)</td><td>Income has no effect on consumers' tendency to search for more product and service-related information in online shoppinga</td></tr><tr><td>Klein &amp; Ford (2003)</td><td>Survey of 337 individuals who are going to purchase a car in the next 6 months, or who have purchased a car in the past 18 months</td><td>Self-reported measure (time spent on information searching and number of sources used)</td><td>Income is negatively related to consumers' tendency to engage in information search, but only in terms of time spent and not number of sources usedb</td></tr><tr><td>Rohm &amp; Swaminathan (2004)</td><td>Survey of 412 online shoppers</td><td>Perceptual scale measures</td><td>Income has no effect on consumers' preference to engage in searching for information across different shops, products and brands</td></tr><tr><td>Education</td><td></td><td></td><td></td></tr><tr><td>Joines et al. (2003)</td><td>Survey of 59 university students and 59 New York State residents</td><td>Subjective measure (percentage of time spent on searching for product and service-related information)</td><td>Education has no effect on consumers' tendency to search for more product and service-related information in online shoppinga</td></tr><tr><td>Klein &amp; Ford (2003)</td><td>Survey of 337 individuals who are going to purchase a car in the next 6 months, or who have purchased a car in the past 18 months</td><td>Self-reported measure (time spent on information searching and number of sources used)</td><td>Education is positively related to consumers' tendency to engage in information search, but only in terms of number of sources used but not for time spent on searchingb</td></tr></table>

<sup>a</sup> It should be noted that the sample employed in this study included offline shoppers as well.  
<sup>b</sup>It should be noted that the study combined both the online and offline sources of information in measuring information search.
