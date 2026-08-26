---
otero_id: 19544
otero_key: "W2XC2JVW"
title: "Constructing a reliable Web graph with information on browsing behavior"
authors: "Yiqun Liu; Yufei Xue; Danqing Xu; Rongwei Cen; Min Zhang; Shaoping Ma; Liyun Ru"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.06.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Constructing a reliable Web graph with information on browsing behavior

Yiqun Liu ⁎, Yufei Xue, Danqing Xu, Rongwei Cen, Min Zhang, Shaoping Ma, Liyun Ru

State Key Lab of Intelligent Technology & Systems, Tsinghua National Laboratory for Information Science and Technology, Department of Computer Science and Technology, Tsinghua University, China

## a r t i c l e i n f o

Article history: Received 17 March 2010 Received in revised form 30 May 2012 Accepted 13 June 2012 Available online 23 June 2012

Keywords: Web graph Quality estimation Hyperlink analysis User behavior analysi PageRank

## a b s t r a c t

Page quality estimation is one of the greatest challenges for Web search engines. Hyperlink analysis algorithms such as PageRank and TrustRank are usually adopted for this task. However, low quality, unreliable and even spam data in the Web hyperlink graph makes it increasingly dif<sup>fi</sup>cult to estimate page quality effectively. Analyzing large-scale user browsing behavior logs, we found that a more reliable Web graph can be constructed by incorporating browsing behavior information. The experimental results show that hyperlink graphs constructed with the proposed methods are much smaller in size than the original graph. In addition, algorithms based on the proposed “sur<sup>fi</sup>ng with prior knowledge” model obtain better estimation results with these graphs for both high quality page and spam page identi<sup>fi</sup>cation tasks. Hyperlink graphs constructed with the proposed methods evaluate Web page quality more precisely and with less computational effort.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

The explosive growth of data on the Web makes information management and retrieval increasingly dif<sup>fi</sup>cult. For contemporary search engines, estimating page quality plays an important role in crawling, indexing and ranking processes. For this reason, the estimation of Web page quality is considered as one of the greatest challenges for Web search engines [14]

Currently, the estimation of page quality mainly relies on an analysis of the hyperlink structure of the Web. The success of PageRank [24] and other hyperlink analysis algorithms such as HITS (Hyperlink-Induced Topic Search) [18] and TrustRank [10] shows that it is possible to estimate Web page quality query independently. These hyperlink analysis algorithms are based on two basic assumptions [7]: <sup>fi</sup>rst, if two pages are connected by a hyperlink, the page linked is recommended by the page that links to it (recommendation). Second, the two pages share a similar topic (locality). Hyperlink analysis algorithms adopted by both commercial search engines (such as [4,11,20,24]) and researchers (such as [10,12,13,18,19]) all rely on these two assumptions. However, these two assumptions miss subtleties in the structure of the actual Web graph. The assumptions and the consequent algorithms thus face challenges in the current Web environment.

For example, Table 1 shows several top Web sites ranked by PageRank on a Chinese Web corpus<sup>1</sup> of over 130million pages. To determine whether the PageRank score accurately represents the popularity of a Web site, we also gathered traf<sup>fi</sup>c rankings as measured by Alexa.com.

The data in Table 1 show that several of the top 10 Web sites ranked by PageRank also received a large number of user visits. For example, www.baidu.com, www.qq.com and www.sina.com.cn are also the three most frequently visited Web sites in China according to Alexa.com (their traf<sup>fi</sup>c rankings are shown in Table 1 in italics). In contrast, several top-ranked sites received a relatively small number of user visits, such as www.hd315.gov.cn and www.miibeian. gov.cn. According to [24], pages with high PageRank values are either well cited from many places around the Web or pointed to by other high PageRank pages. In either case, the pages with the highest PageRank values should be frequently visited by Web users because PageRank can be regarded as “the probability that a random surfer visits a page”. Traf<sup>fi</sup>c is also considered as one of the possible applications of PageRank algorithm in [24]. However, these top-ranked sites do not receive as many user visits as their PageRank rankings indicate. Although authority does not necessarily mean high traf<sup>fi</sup>c on the Web, we believe that either the MII site or the www.hd315.gov. cn site should not be ranked so high in quality estimation results because there are many other government agencies which are also authoritative but ranked much lower than these two sites.

In order to <sup>fi</sup>nd out why the MII site and the www.hd315.gov.cn are ranked so high according to PageRank score, we examine the hyperlink structure of these sites. Fig. 1 shows how www.baidu.com (the most popular Chinese search engine) links to www.miibeian. gov.cn (home page of the Ministry of Industry and Information Technology of China). As shown in the red box, the hyperlink is located at the bottom of the page, and the anchor text contains the Web site's registration information. Each Web site in China should register to the Ministry of Industry and Information Technology (MII), and site owners are requested to put the registration information on each page. Therefore, almost all Web sites in China link to the MII Web site, and the PageRank score of www.miibeian.gov.cn is very high because of the huge number of in-links. The Web site www.hd315. gov.cn is highly ranked by PageRank for similar reason; each commercial site in China is required to put registration information on their pages, and the registration information contains a hyperlink to www.hd315.gov.cn.

Top-ranked Web sites by PageRank in a Chinese Web hyperlink graph.

<table><tr><td>Web site</td><td>Ranked by PageRank</td><td>Ranked by Alexa.com $^{a}$  traffic rankings in China</td></tr><tr><td>www.hd315.gov.cn</td><td>2</td><td>1655</td></tr><tr><td>www.qq.com</td><td>3</td><td>2</td></tr><tr><td>www.baidu.com</td><td>6</td><td>1</td></tr><tr><td>www.miibeian.gov.cn</td><td>7</td><td>179</td></tr><tr><td>www.sina.com.cn</td><td>9</td><td>3</td></tr></table>

<sup>a</sup> http://www.alexa.com/topsites/countries/CN.

From this example we can see that quality estimation results given by PageRank on practical Web environment may not be so reasonable. Web sites such as the MII site are ranked quite high because many Web pages link to them. However, many of these hyperlinks are created due to legal, commercialized or even spamming reasons. Hyperlinks on Web graph should not be treated as equally important as PageRank as supposed in [2]. Practical Web users do not act like the “random surfer”; instead, they only click hyperlinks interesting to them. Therefore, Web sites that are connected by hyperlinks that Web users are not interested in clicking usually get high PageRank score which they do not deserve.

This example shows that hyperlink analysis algorithms are not always successful in the real Web environment because of the existence of hyperlinks that users seldom click. Removing these hyperlinks from Web graph is an important step in constructing a more reliable graph on which link analysis algorithms can be performed more effectively.

To reduce noises in the Web graph, we analyze information on users' browsing behaviors collected by search engine toolbars or browser plug-in software. Information on browsing behavior can reveal which pages or hyperlinks are frequently visited by users and which are not, allowing construction of a more reliable Web graph.

![](/api/attachments/W2XC2JVW/fulltext/images/33c9f81650601cc2332832a3e1311b96d53f6b81aa3996792104d43f9e19f474.jpg)  
Fig. 1. A sample site (http://www.baidu.com) that links to www.miibeian.gov.cn, the site in the sample corpus with the 7th highest PageRank score.

For example, although many pages link to the MII homepage, few people click on these links because site registration information is not interesting to most Web users. These hyperlinks may be regarded as “meaningless” or “invalid” because they are not involved in users' Web sur<sup>fi</sup>ng process. If we construct a new Web graph without these links, the representation of users' browsing behavior will not be affected, but the PageRank score calculated by the new graph will be more accurate because most of the hyperlinks connecting to the MII homepage are removed.

The number of users visiting a site can be regarded as implicit feedback about the importance of both hyperlinks and pages in the Web graph. However, constructing a more reliable graph with this kind of information remains a challenging problem. Retaining only the nodes and vertexes that have been visited at least once is one potential option. Several researchers, such as Liu et al. [22], have constructed such a graph, called a ‘user browsing graph’, and have used it to gain better estimates of page quality than with the original Web graph.<sup>2</sup> However, with user browsing information, there are other options in constructing a Web graph other than the user browsing graph. The contributions of our work include:

• With user browsing information, a new Web sur<sup>fi</sup>ng model is constructed other than the “random surfer model” adopted by previous researches such as PageRank. This “surf with prior knowledge model” incorporates both user behavior information and hyperlink information and is a better simulation of Web users' sur<sup>fi</sup>ng processes.

• Two quality estimation algorithms (userPageRank and userTrustRank) are proposed according to the new “surf with prior knowledge model”. These algorithms take user preference of hyperlinks into consideration and they can be performed on the user browsing graph.

• Two different kinds of Web graph construction algorithms are proposed besides user browsing graph to combine both browsing and hyperlink structure information. Characteristics and evolution of these graphs are studied and compared with the original Web graph.

The remainder of the paper is organized as follows: Section 2 gives a review of related work on page quality estimation and user browsing behavior analysis. Section 3 introduces the “surf with prior knowledge model” and the quality estimation algorithms based on it. Section 4 presents algorithms for constructing Web graphs based on both user browsing and hyperlink information. Section 5 describes the structure and evolution of the Web graphs constructed with the proposed algorithms. The experimental results of applying different algorithms to estimate page quality on different graphs are reported in Section 6. Conclusions and future work are provided in Section 7.

## 2. Related work

## 2.1. Page quality estimation

Most previous work on page quality estimation focuses on exploiting the hyperlink graph of the Web and builds a model based on that graph. Since the success of PageRank [24] in the late 1990s, extensive research has attempted to improve the ef<sup>fi</sup>ciency and effectiveness of the original algorithm [11–13]. However, the basic idea has not changed: a Web page's quality is evaluated by estimating the probability of a Web surfer's visiting the page using a random walk model. The HITS algorithm evaluates Web page quality using two different metrics, the hub score and authority score. Experimental results based on both IBM CLEVER search system evaluation [20] and human experts' annotations [1] have demonstrated the effectiveness of HITS.

In addition to methods to evaluate the quality of Web pages, researchers have proposed link analysis algorithms to identify spam pages. Spam pages are created with the intention of misleading search engines. Gyongyi et al. [10] developed the TrustRank algorithm to separate reputable pages from spam. This work was followed by other methods based on the link structure of spam pages, such as Anti-Trust Rank [19] and Truncated PageRank [2] algorithms. TrustRank is an effective link analysis algorithm that assigns a trust score to Web pages. Pages with low trust scores tend to be spam pages, and pages with high trust scores tend to be high quality pages.

These link analysis algorithms have become popular and important tools in search engines' ranking mechanisms. However, the Web graph on which these algorithms are based is not particularly reliable because hyperlinks can be easily added or deleted by page authors or even by Web users (via Web 2.0 services). Therefore, as shown in Table 1, noise in Web graphs makes it dif<sup>fi</sup>cult for these algorithms to evaluate page quality effectively.

Several methods have been proposed to counteract the manipulation of Web structure. Algorithms such as DiffusionRank [27] and AIR (Af<sup>fi</sup>nity Index Ranking) [17] were designed to <sup>fi</sup>x the <sup>fl</sup>aws of PageRank and TrustRank. DiffusionRank is motivated by the phenomenon of heat diffusion, which is analogous to the dissipation of energy via out-links. AIR scores for Web pages are obtained by using an equivalent electronic circuit model. Similar to TrustRank, both algorithms require the construction of a “high quality seed set”. Experimental results have shown that DiffusionRank and AIR perform better than PageRank and TrustRank in removing spam both on toy graphs and in real Web graphs. However, aside from hyperlinks generated for Web structure manipulation and spam, most Web pages contain meaningless and low quality hyperlinks such as copyright links, advertisement links, and registration information links and so on. These links are not popular and are seldom clicked by users, but they comprise a large part of Web graphs. Both DiffusionRank and AIR algorithms are unable to deal with this kind of “noise” in hyperlink structure data.

Because of the problems that hyperlink analysis algorithms encounter in real Web environment, researchers have tried to use features other than hyperlinks to evaluate quality of Web pages. Chau et al. [6] have identi<sup>fi</sup>ed pages on certain topics using both content-based and link-based features. Liu et al. [21] have proposed a learning-based method for identifying search target pages query independently using content-based and hyperlink-based features, such as document length and in-link count. Jacob et al. [15] have also adopted both content-based and hyperlink-based approaches to detect Web spam. Although these methods use features other than links, link analysis algorithms still play an important role in the identi<sup>fi</sup>cation of high quality pages or spam pages. Therefore, the quality of Web hyperlink data and the effectiveness of link analysis algorithms remain challenging problems.

In contrast to these approaches, we incorporate Web users' browsing behavior to indicate page quality. Most users' browsing behavior is driven by their interests and information needs. Therefore, pages that are visited and hyperlinks that are clicked by users should be regarded as more meaningful and more important than those that are not. It is therefore reasonable to use users' preferences to prune the hyperlink graph.

## 2.2. User browsing behavior analysis

Although researchers such as Page et al. [24] tried to incorporate browsing information (collected from DNS providers) in page quality estimation at the early stage of hyperlink analysis researches, browsing behavior analysis has not become popular until recent years. Web browser toolbars such as Google Toolbar and Live Toolbar collect user browsing information. It is considered as an important source of implicit feedback on page relevance and importance and was widely adopted in Web site usability [9,16,25], user intent understanding [26] and Web search [3,22,23,28] researches.

Using this information on browsing behavior, it is possible to prune the Web graph by removing unvisited nodes and links. For example, Liu et al. [22] constructed a “user browsing graph” with Web access log data. It is believed that the user browsing graph can avoid most of the problems of the original Web graph because links in the browsing graph are actually chosen and clicked by users. Liu et al. also proposed an algorithm to estimate page quality, BrowseRank, which is based on continuous-time Markov process model. Their study shows that the BrowseRank algorithm works better than hyperlink analysis algorithms such as PageRank and TrustRank when the latter two algorithms are performed on the whole Web graph.

The user browsing graph is not the only way to incorporate browsing behavior into page quality estimation. In addition, the interpretation of the user browsing graph is not obvious. For example, we can infer that the user browsing graph differs from the whole Web graph in some aspects, but precisely how do the structures of these two graphs differ from each other? How does the user browsing graph evolve over time? BrowseRank outperforms PageRank and TrustRank algorithms when the latter two algorithms are performed on the original Web graph, but how do hyperlink analysis algorithms perform on the user browsing graph?

We try to answer these questions through experimental studies, and we also attempt to determine how data on users' browsing behavior can be better analyzed to construct a more reasonable Web sur<sup>fi</sup>ng model rather than the widely adopted random surfer model.

## 3. Sur<sup>fi</sup>ng with prior knowledge

With the example shown in Table 1 and Fig. 1, we know that hyperlinks are not clicked by users with equal probabilities and they should not be treated as equally important in the construction of surfing models. However, due to the dif<sup>fi</sup>culties in collecting user browsing information, most previous works on Web graph mining are based on the “random surfer model” which supposes user simply keeps clicking on successive links at random.

Differently from these works, we collected a large amount of user browsing information with the help of a widely used search engine in China. These Web-access logs were collected from Aug. 3, 2008, to Oct. 6, 2008 (60days; logs from Sept. 3 to Sept. 7 were not included because of hard disk failure). Over 2.8billion hyperlink click events were recorded and can be adopted as prior knowledge in the construction of sur<sup>fi</sup>ng models. Details of these log data are introduced in Section 4.1.

Designed with random surfer model, one of the major <sup>fl</sup>aws of the PageRank algorithm is “over-democracy” [27]. The original algorithm assumes that the Web user either randomly follows a hyperlink on a Web page and navigates to the destination (with probability α) or randomly chooses a different page on the given Web graph (with probability 1−α).

$$
\operatorname{PageRank} ^ {(k + 1)} (X) = \alpha \cdot \sum_ {X _ {i} \Rightarrow X} \frac {\operatorname{PageRank} ^ {(k)} \left(X _ {i}\right)}{\# \text {Outlink} \left(X _ {i}\right)} + (1 - \alpha) \cdot \frac {1}{N}.\tag{1}
$$

According to Eq. (1), the PageRank score of a page is divided evenly between all of its outgoing hyperlinks. However, hyperlinks on Web pages are not equally important. Some hyperlinks, such as “top stories” links on the CNN.com homepage, are more important, whereas others, such as advertisements, are less important.

Therefore, it is not reasonable to assume that users will follow hyperlinks on a Web page with equal probabilities. If we introduce the probability of visiting page X<sub>j</sub> directly after visiting page $X _ { i } ,$ namely $P ( X _ { i } { \Rightarrow } X _ { j } )$ , the random surfer model will be replaced by the “surfing with prior knowledge” model and the estimation of $P ( X _ { i } { \Rightarrow } X _ { j } )$ requires prior knowledge of user browsing behaviors.

With the “surfing with prior knowledge” model, Web users do not click on hyperlinks on the Web pages they are visiting randomly, instead, each hyperlink L is clicked with a probability of $P ( X _ { i } { \Rightarrow } X _ { j } )$ in which X is the source page and $X _ { j }$ is the destination page of L.

With the new sur<sup>fi</sup>ng model, Eq. (1) can be modi<sup>fi</sup>ed as follows:

$$
\operatorname{PageRank} ^ {(k + 1)} (X) = \alpha \cdot \sum_ {X _ {i} \Rightarrow X} \operatorname{PageRank} ^ {(k)} \left(X _ {i}\right) P \left(X _ {i} \Rightarrow X\right) + (1 - \alpha) \cdot \frac {1}{N}.\tag{2}
$$

In $\mathrm { E q . ~ } ( 2 ) , P ( X _ { i } \Rightarrow X _ { j } )$ is the probability of visiting page X directly after visiting page $X _ { i \cdot }$ However, for the original Web graph, it is not possible to estimate this probability because the relevant information is not provided. Therefore, PageRank (as well as TrustRank) has to be computed using equal $P ( X _ { i } { \Rightarrow } X _ { j } )$ values (as Eq. (1)).

To incorporate prior user browsing information into the original Web graph, the user-visited nodes and edges should be selected and the number of user clicks on each hyperlink (edges) should be recorded. With this information, we can decide which hyperlinks are important and estimate the probability of $P ( X _ { i } { \Rightarrow } X _ { j } )$ with the maximum likelihood assumption.

If we use $U C ( X _ { i } { \Rightarrow } X _ { j } )$ to represent the number of user clicks from X to $X _ { j } ,$ the original PageRank algorithm can be modi<sup>fi</sup>ed as follows:

$$
\begin{array}{l} \text {userPageRank} ^ {(k + 1)} (X) \\ = \alpha \cdot \sum_ {X _ {i} \Rightarrow X} \text {userPageRank} ^ {(k)} (X _ {i}) \frac {\# U C (X _ {i} \Rightarrow X)}{\sum_ {X _ {i} \Rightarrow X _ {j}} \# U C (X _ {i} \Rightarrow X _ {j})} + (1 - \alpha) \cdot \frac {1}{N}. \end{array}\tag{3}
$$

In Eq. (3), the probability of $P ( X _ { i } { \Rightarrow } X _ { j } )$ is estimated by the weighted UC factor with maximum likelihood assumption. The PageRank of page X is divided between the outgoing links, weighted by UC of each link. Aside from this PageRank division, no other part of the original algorithm is changed. Therefore, the time complexity and the ef<sup>fi</sup>ciency of this algorithm stay the same.

A similar modi<sup>fi</sup>cation can be applied to the TrustRank algorithm, which traditionally divides the trust score equally between outgoing links. The original and the modi<sup>fi</sup>ed algorithms are shown in Eqs. (4) and (5) separately.

$$
\operatorname{TrustRank} ^ {(k + 1)} (X) = \alpha \cdot \sum_ {X _ {i} \Rightarrow X} \frac {\operatorname{TrustRank} ^ {(k)} \left(X _ {i}\right)}{\# \text {Outlink} \left(X _ {i}\right)} + (1 - \alpha) \cdot d\tag{4}
$$

$$
\begin{array}{l} \text {userTrustRank} ^ {(k + 1)} (X) \\ = \alpha \cdot \sum_ {X _ {i} \Rightarrow X} \text {userTrustRank} ^ {(k)} (X _ {i}) \frac {U C (X _ {i} \Rightarrow X)}{\sum_ {X _ {i} \Rightarrow X _ {j}} U C (X _ {i} \Rightarrow X _ {j})} + (1 - \alpha) \cdot d. \end{array}\tag{5}
$$

With the “surfing with prior knowledge” model, hyperlinks on Web pages are not treated as equally important, instead, the probability of user clicking is estimated with prior knowledge and maximum likelihood assumption. By this means, we hope to improve the performance of PageRank and TrustRank which is originally based on the random surfer model.

We believe that the new sur<sup>fi</sup>ng model can also be utilized to other graphs besides the Web hyperlink graph if the probability of visiting one node from another can be estimated. For example, let $G = ( V , E )$ denotes a social graph, where V represents the users and E represents the relationship between them. In many Web-based social network services such as Twitter and Weibo,<sup>3</sup> the relationship between users can be described as a directed edge from follower to followee, which is similar to the hyperlink from source page to destination page.

Intuitively, the in<sup>fl</sup>uence of s social node in social networks is similar to the quality score of a Web page. It means that if we try to estimate in<sup>fl</sup>uence scores on a social graph, hyperlink algorithms such as PageRank and TrustRank can also be utilized. As hyperlinks in a Web graph, we believe that the “following” relationships between nodes in a social graph are also not equally important. This is because users may follow another user for different reasons and closest relationships should be valued more. Therefore, “surfing with prior knowledge” model is also more reasonable than the random surfer model on the social graph although prior knowledge $\left( P ( X _ { i } { \Rightarrow } X _ { j } ) \right)$ ) should be estimated by different means.

## 4. Web Graph construction with information on browsing behavior

## 4.1. Data on user browsing behavior

Based on the “surfing with prior knowledge” model described in Section 3, we revise the original PageRank and TrustRank algorithms by incorporating prior user browsing behavior information. Therefore, the newly proposed userPageRank and userTrustRank algorithms require additional information and cannot be performed on the original Web graph. To construct a reliable Web graph that incorporates user browsing behavior information, we collected data on users' browsing behavior (also called Web-access log data or Web usage data). In contrast to log data from search engine queries and click-through data, this kind of data is collected using browser toolbars. It contains information on Web users' total browsing behavior, including their interactions with search engines and other Web sites.

To provide value-added services to users, most browser toolbars also collect anonymous click-through information on users' browsing behavior. Previous work such as [3] has used this kind of click-through information to improve ranking performance. Liu et al. [23] have proposed a Web spam identi<sup>fi</sup>cation algorithm based on this kind of user behavior data. In this paper, we also adopt Web access logs collected by toolbars because this enables us to freely collect users' browsing behavior information with no interruption to the users. An example of the information recorded in these logs is shown in Table 2 and Example 1.

Table 2 and Example 1 show that no private information was included in the log data. The information shown can be easily recorded using browser toolbars by commercial search engine systems. Therefore, collecting this kind of information for the construction of hyperlink graphs is practical and feasible.

4.2. Construction of a user browsing graph and a user-oriented hyperlink graph

With the data on users' browsing behavior described in Section 4.1, we identi<sup>fi</sup>ed which pages and hyperlinks were visited and the following two algorithms are adopted to construct the user browsing graph and the user-oriented hyperlink graph, respectively.

Algorithm 1 constructs a graph completely based on user behavior data. Only nodes and hyperlinks that were visited at least once are added to the graph. This graph is similar to the graph constructed by Liu et al. in [22], except that the number of user visits on each edge is also recorded to estimate P(X ⇒X ) for userPageRank and userTrustRank. Following their convention, we also call this graph user browsing graph (BG(V,E) for short).

Information recorded in Web-access logs.

<table><tr><td>Name</td><td>Description</td></tr><tr><td>Time stamp</td><td>Date/time of the click event</td></tr><tr><td>Session ID</td><td>A randomly assigned ID for each user session</td></tr><tr><td>Source URL</td><td>URL of the page that the user is visiting</td></tr><tr><td>Destination URL</td><td>URL of the page to which the user navigates</td></tr></table>

Example 1  
A sample Web-access log collected on Dec. 15, 2008.

<table><tr><td>(01:07:09) (3ffd50dc34fcd7409100101c63e9245b)</td><td>(http://v.youku.com/v_playlist/f1707968o1p7.html); (http://www.youku.com/playlist_show/id_1707968.html)</td></tr><tr><td>(01:07:09) (f0ac3a4a87d1a24b9c1aa328120366b0)</td><td>(http://user.qzone.qq.com/234866837); (http://cnc.imgcache.qq.com/qzone/blog/tmygb_static.htm)</td></tr><tr><td>(01:07:09) (3fb5ae2833252541b9ccd9820bad30f6)</td><td>(http://www.qzone8.net/hack/45665.html); (http://www.qzone8.net/hack/)</td></tr></table>

Algorithm 2 constructs a graph distinct from BG(V,E). These two graphs share a common set of nodes, though the graph constructed with Algorithm 2 retains all of the edges between these nodes from the original Web graph. We call this graph a user-oriented hyperlink graph (user-HG(V,E) for short) because it is extracted from the original Web graph but has nodes selected with user information. The original Web graph was constructed by the same search engine company that provided Web access logs to us. Collected in July 2008, it contains over 3billion pages from 111million Web sites and covers a major proportion of Chinese Web pages at that time.

Thus, both BG(V,E) and user-HG(V,E) are constructed with the help of browsing behavior data. The latter graph contains more hyperlinks, whereas the former graph only retains hyperlinks that are actually followed by users. We can see that userPageRank and userTrustRank cannot be performed on user-HG(V,E) because browsing information is not recorded for all edges on this graph.

## 4.3. Comparison of the user browsing and user-oriented hyperlink graphs

We constructed BG(V,E) and user-HG(V,E) with the data on user behavior described in Section 4.1. Table 3 shows how the compositions of these two graphs differ from each other.

According to Table 3, we found that although the hyperlink graph user-HG(V,E) shares a common set of nodes with BG(V,E), the compositions of these two graphs differ signi<sup>fi</sup>cantly. First, BG(V,E) is less than one-tenth the size of user-HG(V,E). The percentage of common pages in user-HG(V,E) is only 1.86%; thus, most (98.14%) of the links in user-HG(V,E) are not actually clicked by users. This difference is consistent with people's Web browsing experience that pages usually provide too many hyperlinks for users to click.

Another interesting <sup>fi</sup>nding is that the user-HG(V,E) graph does not include all the edges in BG(V,E). Less than one-quarter of the pages in BG(V,E) also appear in user-HG(V,E). This phenomenon can

## Algorithm 1

Algorithm to the construct of the user browsing graph.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1. $V = \{\}$, $E = \{\}$
2. For each record in the Web-access log, if the source URL is $A$ and the destination URL is $B$, then,
if $A \notin V$, $V = V \cup \{A\}$;
if $B \notin V$, $V = V \cup \{B\}$;
if $(A, B) \notin E$ $E = E \cup \{(A, B)\}$
Count(A, B) = 1;
else
Count(A, B) + + .
</div>

be partially explained by the fact that user-HG(V,E) is constructed with information collected by Web crawlers, and it is not possible for any crawler to collect the hyperlink graph of the whole Web; it is too huge and changing so fast. When we examined the links that only appear in BG(V,E), we found another reason why user-HG(V,E) does not include them. A large proportion of these links come from users' clicks on search engines result pages (SERPs). Table 4 shows the number of SERP-oriented hyperlinks in BG(V,E).

Tables 3 and 4 reveal that of the links that appear only in BG(V,E) (7.97million edges in total), over 3.27million come from SERPs of the <sup>fi</sup>ve most frequently used Chinese search engines. This number constitutes 30.96% of all edges in BG(V,E). Web users click many links on SERPs, but almost none of these links would be collected by crawlers. These links contain valuable information because they link to Web pages that are both recommended by search engines and clicked by users. It is not possible for Web crawlers to collect all of the links from SERPs without information on user behavior because the number of such links would be overwhelmingly large.

Another important type of links that appear only in BG(V,E) are hyperlinks that are clicked in users' password-protected sessions. For example, login authorization is sometimes needed to visit blog pages. After logging in, Web users often navigate among these pages, and Web-access logs can record these browsing behaviors. However, ordinary Web crawlers cannot collect these links because they are not allowed to access the contents of protected Web pages.

## 4.4. Construction of the user-oriented combined graph

Section 4.3 shows that the user browsing graph differs from the user-oriented hyperlink graph in at least two ways: <sup>fi</sup>rst, compared with user-HG(V,E), a large fraction of the edges (98.14% of E in user-HG(V,E)) are omitted from BG(V,E) because they are not clicked by any user. Second, BG(V,E) contains hyperlinks that are dif<sup>fi</sup>cult or impossible for Web crawlers to collect. Thus, each graph contains unique information that is not contained by the other graph. Therefore, if we construct a graph containing all of the hyperlinks and nodes in

## Algorithm 2

Algorithm to the construct of the user-oriented hyperlink graph.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1. $V = \{\}$, $E = \{\}$
2. For each record in the Web-access log, if the source URL is $A$ and the destination URL is $B$, then,
if $A \notin V$, $V = V \cup \{A\}$;
if $B \notin V$, $V = V \cup \{B\}$.
3. For each $A$ and each $B$ in $V$,
if((A, B) ∈ Original Web Graph) AND((A, B) ∉ E)
$E = E \cup \{(A, B)\}$.
</div>

Table 3  
Differences between BG(V,E) and user-HG(V,E) in the edge sets.

<table><tr><td></td><td># (Common edges)</td><td># (Total edges)</td><td>Percentage of common edges</td></tr><tr><td>BG(V,E)</td><td>2,591,716</td><td>10,564,205</td><td>24.53%</td></tr><tr><td>User-HG(V,E)</td><td></td><td>139,125,250</td><td>1.86%</td></tr></table>

BG(V,E) and user-HG(V,E), it should contain more complete hyperlink information. We adopt the following algorithm (Algorithm 3) to construct such a graph, which combines all of the hyperlink information in BG(V,E) and user-HG(V,E).

This algorithm can construct a graph that shares the same node set as BG(V,E) and user-HG(V,E) but that contains the hyperlinks of both graphs. Because it combines the edge sets of BG(V,E) and user-HG(V,E), we call it a user-oriented combined graph (user-CG(V,E) for short). Similar with user-HG(V,E), it does not contain clicking information on all the edges and userPageRank/userTrustRank cannot be performed on it.

## 4.5. Stats of the constructed graphs

With the data from Web-access logs described in Section 4.1 and the original whole Web graph (named whole-HG(V,E) for short) mentioned in Section 4.2, we constructed three graphs (BG(V,E), user-HG(V,E), and user-CG(V,E)). These graphs were constructed at the site-level instead of the page-level to improve ef<sup>fi</sup>ciency. This level of resolution is also appropriate because a large number of search engines adopt site-level link analysis algorithms and then obtain page-level link analysis scores using a propagation process within Web sites. Another problem with a page-level graph is that due to data sparsity problem, there are only a few user visits for a large part of pages and the behavior data may be not so reliable. However, for a site-level graph, the average number of user visits per site is much larger and data sparsity can be avoided to a large extent. According to experimental results in our previous work [28], we also found that a site-level model outperformed a page-level model because the average number of browsing activities per site is much larger, indicating more reliable behavior information sources.

Descriptive statistics of these constructed graphs are shown in Table 5.

We can see from Table 5 that BG(V,E), user-HG(V,E) and user-CG(V,E) cover a small percentage (3.83%) of the vertices of the original Web graph. The edge sets of these three graphs are also much smaller than the Web graph, but the average number of hyperlinks per node in user-HG(V,E) and user-CG(V,E) is higher than that of the whole-HG(V,E). This result means that user-accessed nodes are more strongly connected to each other than the other parts of the Web. This pattern hints the presence of a large SCC (Strongly Connected Component) proposed in [8] in the user browsing graphs. Another <sup>fi</sup>nding is that compared with user-HG(V,E) and user-CG(V,E), the ratio of edges to vertices in BG(V,E) is much smaller. Thus, a large fraction of hyperlinks are removed for this graph because they are not followed by users. The retained links are ostensibly more reliable than the others, however;

Number of SERP-oriented edges that are not included in user-HG(V,E).

<table><tr><td>Search engine</td><td>Number of edges that are not included inuser-HG(V,E)</td></tr><tr><td>Baidu.com</td><td>1,518,109</td></tr><tr><td>Google.cn</td><td>1,169,647</td></tr><tr><td>Sogou.com</td><td>291,829</td></tr><tr><td>Soso.com</td><td>147,034</td></tr><tr><td>Yahoo.com</td><td>143,860</td></tr><tr><td>Total</td><td>3,270,479 (30.96% of all edges in BG(V,E))</td></tr></table>

## Algorithm 3

Algorithm to the construct of the user-oriented combined graph.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1. $V = \{\} ,E = \{\}$   
2. For each record in the Web-access log, if the source URL is A and the destination URL is B, then,  
if $A\notin V,V = V\cup \{A\}$ if $B\notin V,V = V\cup \{B\}$ .  
3. For each A and each B in V,  
if((A,B)$\in BG(V,E))OR((A,B)\in userHG(V,E))$ $E = E\cup \{(A,B)\}$
</div>

whether this information loss creates problems for link analysis algorithms remains to be determined.

## 5. Structure and evolution of constructed graphs

## 5.1. Structure of the constructed graphs

The degree distribution has been used to describe the structure of the Web by many researchers, such as Broder et al. [5]. The existence of a power law in the degree distribution has been veri<sup>fi</sup>ed by several Web crawls [5,8] and is regarded as a basic property of the Web. We were interested in whether power laws could also describe the in-degree and out-degree distributions in the constructed graphs. Experimental results of degree distributions of both BG(V,E) and user-HG(V,E) are shown in Figs. 2 and 3. We did not consider the degree distributions of user-CG(V,E) because it is a combination of BG(V, E) and user-HG(V,E). If in-degree and out-degree distributions of these two graphs follow a power law, user-CG(V,E) will as well.

Fig. 2 shows that in-degree distributions of both BG(V,E) and user-HG(V,E) follow a power law. The exponent of the power law (1.75) is smaller than that found in previous results (approximately 2.1 in [6,9]). This difference is because our hyperlink graph is based on sites, whereas previous graphs were based on pages. There are fewer unpopular (low in-degree) nodes in a site-level graph compared with a page-level graph because a large number of unpopular pages may come from the same Web site. Another phenomenon is that the exponent of power law distribution in BG(V,E) (2.30) is larger than that of user-HG(V,E) (1.75). This difference implies that with an increase in in-degree i, the number of vertices with i in-links drops faster in the user browsing graph. This pattern can be explained by the fact that some Web sites are relatively more popular (have higher in-degree) in the user browsing graph than in the user-oriented hyperlink graph.

The out-degree distributions of both graphs also subscribe to the power law (Fig. 3). The exponent of the out-degree distribution in a page-based graph has been estimated to be 2.7 [5,8]. The exponent estimated for our site-based graph is much smaller (1.9). In a site-based graph, out-links that link to pages in the same site are omitted. This assumption reduces the number of out-links of many vertices and reduces the difference between high and low out-link vertices. The exponent of the out-degree distribution in BG(V,E) is larger than the one in user-HG(V, E). As for the out-degree distribution, this difference means that with the increase in out-degree o, the number of vertices with o in-links drops faster in the user browsing graph.

Sizes of the constructed and the original Web graphs.

<table><tr><td>Graph</td><td>Vertices (#)</td><td>Edges (#)</td><td>Edges/vertices</td></tr><tr><td> $BG(V,E)$ </td><td>4,252,495</td><td>10,564,205</td><td>2.48</td></tr><tr><td> $User-HG(V,E)$ </td><td>4,252,495</td><td>139,125,250</td><td>32.72</td></tr><tr><td> $User-CG(V,E)$ </td><td>4,252,495</td><td>147,097,739</td><td>34.59</td></tr><tr><td> $Whole-HG(V,E)$ </td><td>110,960,971</td><td>1,706,085,215</td><td>15.38</td></tr></table>

![](/api/attachments/W2XC2JVW/fulltext/images/53874b0ed4ba0591207d0e88ed1b1e9476cfe1bbf3e2159639e8c0948454dde8.jpg)  
Fig. 2. In-degree distributions of both BG(V,E) and user-HG(V,E) subscribe to the power law.

The experimental results shown in Figs. 2 and 3 con<sup>fi</sup>rm that similar to the whole Web graph, the in-degree and out-degree distributions of both BG(V,E) and user-HG(V,E) follow a power law. However, the exponents of the power law distributions are different because the constructions of BG(V,E) and user-HG(V,E) decrease the numbers of valueless nodes and hyperlinks compared with the original Web graph. The fact that BG(V,E) and user-HG(V,E) inherit characteristics of the whole Web makes it possible for us to perform state-of-the-art link analysis algorithms on these graphs.

## 5.2. Evolution of BG(V,E) and quality estimation of newly visited pages

The purpose of our work is to estimate Web page quality with the help of information on user browsing behavior. For practical search engine applications, an important issue is whether the page quality scores calculated off-line can be adopted for on-line search process. BG(V,E), user-HG(V,E) and user-CG(V,E) were all constructed with browsing behavior information collected by search engines. This kind of information is collected during a certain time period. Therefore, user behavior outside this time period cannot be included in the construction of these graphs. If pages needed by users are not included in the graphs, it is impossible to calculate their quality scores. Therefore, it is important to determine how the compositions of these graphs evolve over time and whether newly visited pages can be included in the graphs.

![](/api/attachments/W2XC2JVW/fulltext/images/1570d117661c2aa762aeaa06dc2172ac18ddbaaea817a149875b4514763286f4.jpg)  
Fig. 3. Out-degree distributions of both BG(V,E) and user-HG(V,E) subscribe to the power law.

To determine whether the construction of BG(V,E), user-HG(V,E) and user-CG(V,E) can avoid the problem of newly visited and missing pages, we designed the following experiment:

Step 1 A large number of pages appear each day, and only a fraction of them are visited by users. We only focus on the newly visited pages that are actually visited by users because the absence of pages from the graph could affect users' browsing experiences. Therefore, we examine how many newly visited pages are included by the constructed graphs.

In Fig. 4, each data point shows the percentage of newly clicked pages/hyperlinks that are not included by BG(V,E). On each day, BG(V,E) is constructed with browsing behavior data collected from Aug. 3, 2008, (the <sup>fi</sup>rst day in the <sup>fi</sup>gure) to the date before that day. We focus on BG(V,E) because user-HG(V,E) and user-CG(V,E) share the same vertex set. On the <sup>fi</sup>rst day, all of the edges and vertices are newly visited because no data has yet been included in BG(V,E). From the second day to approximately the 15th day, the percentage of newly visited edges and vertices drops. On each day after the 15th day, approximately 30% of the edges and 20% of the vertices are new to the BG(V,E), which is constructed with data collected before that day.

During the <sup>fi</sup>rst 15days, the percentage of newly visited edges and vertices drops because the structure of the browsing graph is more and more complete each day. At the 15th day, the browsing graph contains 6.12million edges and 2.56million vertices. From then on, the number of newly visited edges and vertices is relatively stable. Approximately 0.3million new edges and 0.1million new vertices appear on each subsequent day. Therefore, it takes approximately 15days to construct a stable user browsing graph and subsequently, approximately 20% of newly visited Web sites are not included in BG(V,E) each day.

Step 2 According to Step 1, approximately 20% of newly visited sites would be missing if we adopt BG(V,E) for quality estimation (supposing BG(V,E) is daily updated). To determine whether this missing subset of newly visited sites affects quality estimation. we examined whether Web sites that are not included in the graph are indexed by search engines. If they are not indexed by search engines, it is not necessary to calculate their quality estimation scores because search engines will not require these scores. We sampled 30,605 pages from the sites that are visited by users but not included in BG(V,E) (approximately 1% of all visited pages in these sites) and checked whether they are indexed by four widely used Chinese search engines (Baidu.com, Google.cn, Sogou.com, Yahoo.cn). The experimental results are shown in Table 6 (SE1–SE4 are used instead of search engine names).

The experimental results in Table 6 show that most of these pages (88.74% on average) are not indexed by search engines. It is not necessary for BG(V,E) to include these pages because search engine does not require their quality estimation scores.

Step 3 According to the results of Step 1 and 2, we can calculate that only 2.2% (11.26%×20%) of newly visited pages are both not included in BG(V,E) and required for quality estimation. Among the pages that are both indexed by search engines and visited by users, most will be included by BG(V,E) if this graph can be updated daily with new log data on browsing behavior. Therefore, it is appropriate to use BG(V,E) in quality estimation. Because user-HG(V,E) and user-CG(V,E) share the same vertex set with BG(V,E), these constructed graphs are also not substantially affected by the problem of new visits to missing pages. Thus, these graphs are also appropriate for quality estimation.

![](/api/attachments/W2XC2JVW/fulltext/images/025b8b423b8194a64ac0f0f7dbbc3aa1712dd7bd2707b1be46e1eabe592df565.jpg)  
Fig. 4. Evolution of BG(V,E). Category axis: day number, assuming Aug. 3, 2008, is the <sup>fi</sup>rst day. Value axis: percentage of newly clicked pages/hyperlinks not included in BG(V,E) (BG(V,E) is constructed with data collected from the <sup>fi</sup>rst day to the given day).

## 6. Experimental results and discussions

## 6.1. Experimental setup

In Section 1, we assume that the user-accessed part of the Web is more reliable than the parts that are never visited by users. On the basis of this assumption, we construct three different hyperlink graphs based on browsing behavior. To determine whether the constructed graphs outperform original Web graph in estimating page quality, we adopted two evaluation methods.

The <sup>fi</sup>rst method is based on the ROC/AUC metric, which is a traditional measure in quality estimation research, such as “Web Spam Challenge”.<sup>4</sup> To construct a ROC/AUC test set, we sampled 2279 Web sites randomly according to their frequencies of user visits and had two assessors annotate their quality scores. Approximately 39% of these sites were annotated as “high quality”, 19% were “spam”, and the others are “ordinary”. After performing link analysis algorithms, each site in the test set was assigned a quality estimation score. We can evaluate the performance of a link analysis algorithm on the basis of whether it assigns higher scores to good pages and lower scores to bad ones.

The second method is a pairwise orderedness test. This test was <sup>fi</sup>rst proposed by Gyöngyi et al. [10] and is based on the assumption that good pages should be ranked higher than bad pages by an ideal algorithm. We constructed a pairwise orderedness test set composed of 782 pairs of Web sites. These pairs were annotated by product managers of a Web user survey company. It is believed that the pairwise orderedness show the two sites' differences in reputation. For example, both http://video.sina.com.cn/ and http://v.blog.sohu. com/ are famous video-sharing Web sites in China. However. the former site is more popular and receives more user visits, so the pairwise quality order is http://video.sina.com.cn/>http://v.blog.sohu.com/. If an algorithm assigns a higher score to http://video.sina.com.cn/, it passes this pairwise orderedness test. We use the accuracy rate to evaluate the performance of the pairwise orderedness test, which is de<sup>fi</sup>ned as the percentage of correctly ranked Web site pairs.

With these two evaluation methods, we tested whether traditional hyperlink analysis algorithms perform better on BG(V,E), user-HG(V,E) and user-CG(V,E) than on the original Web graph. In addition, we also investigated whether a speci<sup>fi</sup>cally designed link analysis algorithm for browsing graphs (such as BrowseRank) performs better than the traditional methods (such as PageRank and TrustRank).

First, we compared the performance of the link analysis algorithms on the four graphs (BG(V,E), user-HG(V,E), user-CG(V,E) and whole-HG(V,E)). Second, we compared the performance of PageRank,

TrustRank, DiffusionRank and BrowseRank on BG(V,E). The latter comparisons were only performed on BG(V,E) because BrowseRank requires users' stay time information, which is only applicable for BG(V,E). In addition, to examine how the proposed userPageRank and userTrustRank algorithms perform, we compared their performances to that of the original algorithms on both a user browsing graph and a social graph constructed with data from China's largest micro-blogging service provider weibo.com.

For TrustRank and DiffusionRank, a high quality page “seed” set must be constructed. In these experiments, we follow the construction method proposed by Gyöngyi et al. in [10] and which is based on an inverse PageRank algorithm and human annotation. The inverse PageRank algorithm was performed on the whole Web graph, and we annotated the top 2000 Web sites ranked by inverse PageRank. Finally, 1153 high quality and popular Web sites were selected to compose the seed set. The parameters in our implementation of PageRank, TrustRank and Diffusion Rank algorithms are all tuned according to their original implementations [10,24,27]. The α parameters of PageRank and TrustRank algorithms are set to 0.85 according to [10,24], and the iteration time is both set to 30 because that is enough for the results to converge. Parameters for the DiffusionRank algorithm are set as: γ=1.0, α=0.85, and M=100, according to [27].

## 6.2. Quality estimation with different graphs

With the four different hyperlink graphs shown in Table 5, we applied the PageRank algorithm and evaluated the performance of page quality estimation. The experimental results of high quality page identi<sup>fi</sup>cation, spam page identi<sup>fi</sup>cation and the pairwise orderedness test are shown in Fig. 5. The performances of high quality and spam page identi<sup>fi</sup>cation are measured by the AUC value, whereas the pairwise orderedness test used accuracy as the evaluation metric.

Fig. 5 shows that PageRank applied to the original Web graph (whole-HG(V,E)) performs the worst in all three quality estimation tasks. This result indicates that the graphs constructed by Algorithms 1–3 can more effectively estimate Web page quality than can the original Web graph. The improvements in performance associated with each of these three graphs are shown in Table 7.

Table 6  
Percentage of newly visited pages indexed by search engines.

<table><tr><td>Search engine</td><td>Percentage of pages indexed</td></tr><tr><td>SE1</td><td>8.65%</td></tr><tr><td>SE2</td><td>11.52%</td></tr><tr><td>SE3</td><td>10.47%</td></tr><tr><td>SE4</td><td>14.41%</td></tr><tr><td>Average</td><td>11.26%</td></tr></table>

![](/api/attachments/W2XC2JVW/fulltext/images/b592b81171aa6395efaf16fecf62f7aee1fd44143e4652df4583b28f82affb41.jpg)  
Fig. 5. Quality estimation results with PageRank performed on BG(V,E), user-HG(V,E), user-CG(V,E) and whole-HG(V,E).

According to Table 7, the graphs constructed with information on browsing behavior outperform the original Web graph by approximately 5–25%. The adoption of user browsing behavior helps reduce possible noise in the original graph and makes the graph more reliable. This <sup>fi</sup>nding agrees with the results in [22] that BG(V,E) outperforms the original Web graph. It also validates our assumption proposed in Section 1 that the user-accessed part of the Web is more reliable than the parts that are never visited by users.

According to Fig. 5 and Table 7, among the three graphs constructed with user behavior information, BG(V,E) performs the worst, whereas user-HG(V,E) and user-CG(V,E) obtain very similar results. As described in Section 5.1, BG(V,E) contains fewer edges than the other two graphs. The retained links are on average more informative than the edges in the other graphs; however, this huge loss of edge data also compromises the page quality estimation. User-HG(V,E) and user-CG(V,E) share the same vertex set, and their edge sets are also very similar (only 7.97million edges are added to user-CG(V,E), making up 5.14% edges of the whole graph). Therefore, these two graphs perform similarly in page quality evaluation.

BG(V,E), user-HG(V,E) and user-CG(V,E) share the same vertex set, which is composed of all user-accessed sites recorded in Web-access logs. Although BG(V,E) contains the fewest edges of the four graphs, it still outperforms whole-HG(V,E). This result shows that the selection of the vertex set is more important than the selection of the edge set. Reducing the unvisited nodes in the original Web graph can be an effective method for constructing hyperlink graph.

In Section 1, we show in Table 1 a list of Web sites which are ranked top according to PageRank scores on the original Web graph. We also <sup>fi</sup>nd that some government Web sites (e.g., www.miiberan. gov.cn and www.hd315.gov.cn) are ranked quite high but fail to draw much user attention. These Web sites are authoritative and important but they should not be ranked so high because other similar government agency Web sites are generally ranked much lower. However, when we look into the results of PageRank performed on BG(V,E), we <sup>fi</sup>nd that the rankings of www.miiberan.gov.cn and www.hd315. gov.cn are more reasonable.

According to Table 8, both www.miiberan.gov.cn and www.hd315. gov.cn are ranked lower according to PageRank on BG(V,E) than that on whole-HG(V,E). They are also important resources according to the algorithm on the user browsing graph but not as important as the top-ranked ones. We believed that the rankings on BG(V,E) give a better estimation of their quality according to both popularity and authority.

Performance improvements of the graphs constructed with Algorithms 1–3 compared to the original Web graph.

<table><tr><td rowspan="2">Test method</td><td colspan="3">Improvement compared with whole-HG(V,E)</td></tr><tr><td>BG (V,E)</td><td>User-HG(V,E)</td><td>User-CG(V,E)</td></tr><tr><td>High quality page identification</td><td>+5.69%</td><td>+7.55%</td><td>+7.12%</td></tr><tr><td>Spam page identification</td><td>+3.77%</td><td>+7.44%</td><td>+7.46%</td></tr><tr><td>Pairwise orderedness test</td><td>+15.14%</td><td>+20.34%</td><td>+19.67%</td></tr></table>

PageRank ranking comparison of some government agency Websites on whole-HG(V,E) and BG(V,E).

<table><tr><td></td><td>PageRank ranking on whole-HG(V,E)</td><td>PageRank ranking on BG(V,E)</td></tr><tr><td>www.miibeian.gov.cn</td><td>5</td><td>23</td></tr><tr><td>www.hd315.gov.cn</td><td>2</td><td>117</td></tr></table>

## 6.3. Quality estimation with different link analysis algorithms

In [22], Liu et al. have shown that a speci<sup>fi</sup>cally designed link analysis algorithm (BrowseRank) outperforms TrustRank and PageRank for both spam <sup>fi</sup>ghting and high quality page identi<sup>fi</sup>cation when the latter two algorithms are applied to the original Web graph. They explained that BrowseRank improves performance because it can better represent users' preferences than PageRank and TrustRank. However, it is still unclear whether this improvement comes from algorithm and model design or from the adoption of data on user behavior. Thus, we tested the performance of PageRank, TrustRank and BrowseRank on the same BG(V,E) graph. This comparison was only performed on BG(V,E) because the calculation of BrowseRank requires users' stay time information, which is applicable to BG(V,E) only.

PageRank performs better on BG(V,E) than on the original Web graph (Fig. 5). Therefore, it is possible that the BrowseRank algorithm improves performance simply because it is performed on a graph constructed from data on user browsing behavior. The experimental results shown in Fig. 6 validate this assumption. TrustRank performs the best in both spam page identi<sup>fi</sup>cation and high quality page identi<sup>fi</sup>cation, whereas PageRank performs slightly better than the other three algorithms in the pairwise orderedness test. The good performance of TrustRank might come from the prior information stored in the “seed” set.

According to the results, TrustRank outperforms BrowseRank by 4.12% and 2.84% in high quality and spam page identi<sup>fi</sup>cation tasks, respectively. The performance improvements are small but demonstrate that the TrustRank algorithm can also be very effective on BG(V,E). The PageRank algorithm also performs no worse than BrowseRank on any of these tests. This result means that the performance improvement by the BrowseRank algorithm reported in [22] comes both from algorithm design and, perhaps more importantly, from the adoption of information on user browsing behavior. Additionally, PageRank and TrustRank are more ef<sup>fi</sup>cient than BrowseRank because they do not require collecting information on users' stay time.

![](/api/attachments/W2XC2JVW/fulltext/images/28d1014c96a1d0ce5bcac88607a56c6f350aa78313189a8ad0b3b15625d6c773.jpg)  
Fig. 6. Results of quality estimation with different link analysis algorithms on BG(V,E).

Table 9  
![](/api/attachments/W2XC2JVW/fulltext/images/0c2c3c57568a336a0c22843388d2e3f009a271e8e7bfeb925d4dee32affbfc9f.jpg)  
Fig. 7. Quality estimation results with the original PageRank/TrustRank and userPageRank/userTrustRank algorithms on BG(V,E).

These results and examples demonstrate that although BrowseRank is specially designed for BG(V,E), it does not perform better than PageRank, TrustRank or DiffusionRank applied to BG(V,E). BrowseRank favors the pages where users stay longer, but stay time does not necessarily indicate quality or user preference. Compared with the algorithm design, the incorporation of information on user browsing behavior in the construction of link graphs is perhaps more important.

## 6.4. UserPageRank and UserTrustRank on user browsing graph

In Section 3, we proposed the userPageRank and userTrustRank algorithms, which modify the original algorithms by estimation of $P ( X _ { i } { \Rightarrow } X _ { j } )$ according to user browsing information recorded in BG(V,E). To examine the effectiveness of these algorithms, we compared their performance with the original PageRank/TrustRank algorithms (Fig. 7).

The modi<sup>fi</sup>ed algorithms perform slightly better than the original algorithms. They perform almost equivalently in high quality page identi<sup>fi</sup>cation and perform slightly different in spam page identi<sup>fi</sup>cation. For both PageRank and TrustRank algorithms, the modi<sup>fi</sup>ed algorithms outperform the original ones by approximately 3% in spam identi<sup>fi</sup>cation. Examining several test cases, we <sup>fi</sup>nd that this performance improvement comes from modi<sup>fi</sup>cation to the algorithms.

An example is the spam site whose URL is http://11sss11xp.org/. Among the 2279 Web sites in the ROC/AUC test set, it is ranked 1030th by the original TrustRank algorithm and 1672nd by the userTrustRank algorithm. Because a spam site should be assigned a low ranking position, userTrustRank performs better for this test case. We investigated the hyperlink structure of this site to analyze why the modi<sup>fi</sup>ed algorithm performs better.

In Tables 9 and 10, we can see that this site receives many in-links from search engines (such as www.yahoo.cn and image.baidu.com). This phenomenon can be explained because spam sites are designed to achieve unjusti<sup>fi</sup>ably favorable rankings in search engines. This spam site also receives in-links from several Web 2.0 sites, such as my.51.com, which is a blog service site. With the original TrustRank algorithm, trust scores of the original sites should be evenly divided between their outgoing links. In contrast, for userTrustRank, trust scores are assigned by estimating P(X ⇒X ), the probability of visiting site $X _ { j }$ after visiting $\bar { X _ { i } } .$ Because this site is a spam site that users generally do not visit, P(X ⇒X ) for this site should be low. For example, the site www.yahoo.cn has 35,000 outgoing links in BG(V,E). Altogether, 208,658 user clicks are performed on these outgoing links, and only one of them links to 11sss11xp.org. With the original TrustRank algorithm, the spam site receives 1/35,000 of Yahoo's trust score, whereas userTrustRank only assigns 1/208,658 of the corresponding score to this spam site. We can see that userTrustRank divides a page's trust score according to counts of users' visits, and this adaptation can help identify spam sites.

Web sites that link to a spam site (http://11sss11xp.org/) in BG(V,E).

<table><tr><td>Source Web site</td><td>Destination Web site</td><td># User visits</td></tr><tr><td>http://web.gougou.com/</td><td>http://11sss11xp.org/</td><td>3</td></tr><tr><td>http://image.baidu.com/</td><td>http://11sss11xp.org/</td><td>1</td></tr><tr><td>http://www.yahoo.cn/</td><td>http://11sss11xp.org/</td><td>1</td></tr><tr><td>http://domainhelp.search.com/</td><td>http://11sss11xp.org/</td><td>1</td></tr><tr><td>http://my.51.com/</td><td>http://11sss11xp.org/</td><td>1</td></tr></table>

Table 10  
Information on sites that connect to a spam site (http://11sss11xp.org/).

<table><tr><td>Site</td><td># Out-link</td><td># User visits</td></tr><tr><td>www.yahoo.cn</td><td>35,000</td><td>208,658</td></tr><tr><td>my.51.com</td><td>86,295</td><td>19,443,717</td></tr><tr><td>image.baidu.com</td><td>148,611</td><td>8,218,706</td></tr></table>

## 6.5. UserPageRank and UserTrustRank on social graph

In order to further examine the performance of userPageRank and userTrustRank algorithms, we also constructed a social graph as described in Section 3 and see how they perform on it. The data was collected in September 2011 from weibo.com, which is China's largest social network service provider. Information of 2,631,342 users and about 3.6billion relationships was collected. To the best of our knowledge, it is one of the largest corpuses in social network studies. Information recorded in our data set is shown in Table 11.

As described in Section 3, the userPageRank and userTrustRank require the estimation of $P ( X _ { i } { \Rightarrow } X _ { j } )$ as prior knowledge. In social graph, we adopted the number of common tags as a sign of closeness between users. We believe that the assumption is reasonable because the following relationships between users with many common interests should be more reliable than those not. Therefore, the weight of an edge in the social graph equals to the number of common tags between nodes it connects. After performing userPageRank and userTrustRank algorithms on the weighted social graph, social in<sup>fl</sup>uence estimation results are shown in Fig. 8.

Fig. 8 shows the AUC performances of different in<sup>fl</sup>uence estimation algorithms on the social graph. We use the users with “Veri<sup>fi</sup>ed sign” as more in<sup>fl</sup>uent ones in our evaluation because their identity has been veri<sup>fi</sup>ed by weibo.com and according to the veri<sup>fi</sup>cation policy,<sup>5</sup> only “authoritative” person or organizations will be veri<sup>fi</sup>ed. For the seed set of TrustRank and userTrustRank, we select 100 people from “Weibo hall of fame<sup>6</sup>” which is composed of famous people in certain <sup>fi</sup>elds such as entertainment, politics, techniques and so on.

According to the results shown in Fig. 8, we see that the performance of PageRank, userPageRank and userTrustRank is similar to each other while TrustRank performs the worst among all algorithms. Although the AUC performance of PageRank is almost the same as userPageRank and userTrustRank, we <sup>fi</sup>nd that these algorithms give quite different rankings. The top results of the algorithms in Table 12 show that both PageRank and TrustRank put famous entertainment stars (such as Xidi Xu, Chen Yao and Mi Yang) at the top of their result lists. Meanwhile, userPageRank and userTrustRank favor accounts that post interesting jokes or quotations (such as joke selection and classic quotations).

The differences in top ranked results are caused by the fact that although the entertainment stars have many followers, a large part of these followers do not share same tags with the stars. This is because many of the stars do not list any tags on their accounts such as Xidi Xu and Chen Yao. People follow the accounts such as joke selection and classic quotations because they actually provide interesting information and in<sup>fl</sup>uent people. Therefore, we believe that userPageRank and userTrustRank algorithms give more reasonable estimation of social in<sup>fl</sup>uence.

Table 11  
Information recorded in the collected micro-blogging data.

<table><tr><td>Information</td><td>Explanations</td></tr><tr><td>User ID</td><td>The unique identifier for each user</td></tr><tr><td>User name</td><td>The name of the user</td></tr><tr><td>Verified sign</td><td>Whether the user&#x27;s identification is verified by weibo.com</td></tr><tr><td>Followees</td><td>The ID list that are followed by the user</td></tr><tr><td>Followers</td><td>The ID list that follow the user</td></tr><tr><td>Tags</td><td>A list of keywords describing the user&#x27;s interests with the purpose of self-introduction</td></tr></table>

## 7. Conclusion and future works

Page quality estimation is one of the greatest challenges for search engines. Link analysis algorithms have made progress in this <sup>fi</sup>eld but encounter increasing challenges in the real Web environment. In this paper, we analyze user browsing behavior and proposed two hyperlink analysis algorithms based on “sur<sup>fi</sup>ng with prior knowledge” model instead of the random surfer model. We also construct reliable link graphs in which this browsing behavior information is embedded. Three construction algorithms are adopted to construct three different kinds of link graphs, BG(V,E), user-HG(V,E) and user-CG(V,E). We examined the structure of these graphs and found that they inherit characteristics, such as power law distributions of in-degrees and out-degrees, from the original Web graph. The evolution of these graphs is also studied, and they are found to be appropriate for page quality estimation by search engines.

The experimental results show that the graphs constructed with browsing behavior data are more effective than the original Web graph in estimating Web page quality. PageRank on BG(V,E), user-HG(V,E) and user-CG(V,E) outperforms PageRank on the whole Web graph. In addition, user-HG(V,E) and user-CG(V,E) work better than BG(V,E), probably because the construction process of BG(V,E) omits too many meaningful hyperlinks. We also found that PageRank, TrustRank and DiffusionRank perform as well as (or even better than) BrowseRank when they are performed on the same graph (BG(V,E)). This result reveals that the incorporation of user browsing information is perhaps more important than the selection of link analysis algorithms. Additionally, the construction of user browsing graphs introduces more information. Thus, it is possible to modify the original TrustRank/PageRank algorithms by estimating the importance of outgoing links. The modi-<sup>fi</sup>ed algorithms (called userPageRank and userTrustRank) show better performance in both Web spam identi<sup>fi</sup>cation and social in<sup>fl</sup>uence estimation.

Although the Web/micro-blogging collections and data on user browsing behavior are collected on Chinese Web environment, the algorithms are not specially designed for the speci<sup>fi</sup>c collection. Therefore, they should not behave signi<sup>fi</sup>cantly differently in a multi-language collection as long as reliable data sources can be provided.

![](/api/attachments/W2XC2JVW/fulltext/images/84563ef52a68975fe76509e3cc734e18b598dc84eb122b9915dd63dc411d09dc.jpg)  
Fig. 8. Social in<sup>fl</sup>uence estimation results with the original PageRank/TrustRank and userPageRank/userTrustRank algorithms on social graph of weibo.com.

Table 12  
Top results of PageRank, TrustRank, userPageRank and userTrustRank algorithms on the social graph of weibo.com.

<table><tr><td>Rank</td><td>PageRank</td><td>userPageRank</td><td>TrustRank</td><td>userTrustRank</td></tr><tr><td>1</td><td>Kangyong Cai</td><td>Joke selection</td><td>Kangyong Cai</td><td>Kangyong Cai</td></tr><tr><td>2</td><td>Xidi Xu</td><td>Kangyong Cai</td><td>Mi Yang</td><td>Joke selection</td></tr><tr><td>3</td><td>Cold joke selection</td><td>Classic quotations</td><td>Na Xie</td><td>Xiaoxian Zhang</td></tr><tr><td>4</td><td>Chen Yao</td><td>Cold joke selection</td><td>Weiqi Fan</td><td>Classic quotations</td></tr><tr><td>5</td><td>Xiaogang Feng</td><td>Global fashion</td><td>Lihong Wang</td><td>Cold joke selection</td></tr></table>

Several technical issues remain, which we address here as future work:

First, Web pages that are visited by users only comprise a small fraction of pages on the Web. Although it has been found that most pages that users need can be included in the vertex set of BG(V,E), search engines still need to keep many more pages in their index to meet all possible user needs. To estimate quality of these pages, we are planning to predict user preferences for a certain page by using the pages that users previously visited as training set. If we can calculate the probability that a Web page will be visited by users in the future, this information will help construct a large-scale, credible link graph not limited by data on user behavior. Second, the evolution of the user browsing graph can be regarded as a combination of the evolution of both the Web and Web users' interests. In this paper, we analyzed the short term evolution (a period of 60days) of the graph. We are considering collecting long-term data to determine how the evolutionary process re-<sup>fl</sup>ects changes in users' behavior and interests.

## Acknowledgments

This work is supported by the Natural Science Foundation (60903107, 61073071) and the National High Technology Research and Development (863) Program of China (2011AA01A207). In the early stages of this work, we bene<sup>fi</sup>ted enormously from discussions with Yijiang Jin. We thank Jianli Ni for kindly offering help in data collection and corpus construction. We also thank Tao Hong, Fei Ma, and Shouke Qin from Baidu.com and anonymous referees of this paper for their valuable comments and suggestions.

## References

[1] B. Amento, L. Terveen, W. Hill, Does authority mean quality? Predicting expert quality ratings of Web documents, In: Proc. of 23rd ACM SIGIR Conference, 2000, pp. 296–303.

[2] L. Becchetti, C. Castillo, D. Donato, S. Leonardi, R. Baeza-Yates, Using rank propagation and probabilistic counting for link based spam detection, In: Proceeding of the Workshop on Web Mining and Web Usage Analysis, 2006.

[3] M. Bilenko, R.W. White, Mining the search trails of sur<sup>fi</sup>ng crowds: identifying relevant Web sites from user activity, In: Proc. of the 17th WWW Conference 2008, pp. 51–60.

[4] S. Brin, L. Page, The anatomy of a large-scale hypertextual Web search engine, Computer Networks and ISDN Systems 30 (1998) 107–117.

[5] A. Broder, R. Kumar, F. Maghoul, P. Raghavan, S. Rajagopalan, R. Stata, A. Tomkins, J. Wiener, Graph structure in the Web, Computer Networks 33 (2000) 309–320

[6] M. Chau, H. Chen, A machine learning approach to web page <sup>fi</sup>ltering using content and structure analysis, Decision Support Systems 44 (2) (2008) 482–494.

[7] N. Craswell, D. Hawking, S. Robertson, Effective site <sup>fi</sup>nding using link anchor information, In: Proceedings of the 24th ACM SIGIR Conference, 2001, pp. 250–257.

[8] D. Donato, L. Laura, S. Leonardi, S. Millozzi, The Web as a graph: how far we are, ACM Transaction on Internet Technology 7 (1) (2007) 4.

[9] X. Fang, C.W. Holsapple, An empirical study of web site navigation structures' im pacts on web site usability, Decision Support Systems 43 (2) (2007) 476–491

[10] Z. Gyöngyi, H. Garcia-Molina, J. Pedersen, Combating Web spam with TrustRank, In: Proceedings of the Thirtieth International VLDB Conference, 2004, pp. 576–587.

[11] T. Haveliwala, Ef<sup>fi</sup>cient computation of PageRank, Technical Report, Stanford University 1999, http://dbpubs.stanford.edu/pub/1999-31

[12]. T. Haveliwala Topic-sensitive PageRank: a context-sensitive ranking algorithm for Web search JEEE Transaction on Knowledge and Data Engineering 15 (4) (2003) 784–796

[13] T. Haveliwala, S. Kamvar, G. Jeh, An analytical comparison of approaches to personalizing PageRankStanford Technical Report, http://ilpubs.stanford.edu:8090/596/.

[14] M.R. Henzinger, R. Motwani, C. Silverstein, Challenges in web search engines, In: SIGIR Forum, 36, 2002, pp. 11–22, (Sep. 2002).

[15] A. Jacob, C. Olivier, C. Carlos, WITCH: a new approach to Web spam detection, Yahoo! Research Report No. YR-2008-001, 2008.

[16] Y. Kang, Y. Kim, Do visitors' interest level and perceived quantity of web page content matter in shaping the attitude toward a web site? Decision Support Systems 42 (2) (2006) 1187–1202.

[17] R. Kaul, Y. Yun, S. Kim, Ranking billions of web pages using diodes, Communications of the ACM 52 (8) (2009) 132–136.

[18] J.M. Kleinberg, Authoritative sources in a hyperlinked environment, Journal of ACM 46 (5) (1999) 604–632

[19] V. Krishnan, R. Raj, Web spam detection with anti-TrustRank, In: The 2nd International Workshop on Adversarial Information Retrieval on the Web, 2006, p. 3.

[20] R. Kumar, P. Raghavan, S. Rajagopalan, S. Rajagopalan, A. Tomkins, Core algorithms in the CLEVER system, ACM Transactions on Internet Technology 6 (2) (2006) 131–152

[21] Y. Liu, M. Zhang, R. Cen, L. Ru, S. Ma, Data cleansing for Web information retrieval using query independent features, Journal of the American Society for Information Science and Technology 58 (12) (2007) 1884–1898.

[22] Y. Liu, B. Gao, T. Liu, Y. Zhang, Z. Ma, S. He, H. Li, BrowseRank: letting web users vote for page importance, In: Proc. of 31st ACM SIGIR Conference, 2008, pp. 451–458.

[23] Y. Liu, F. Chen, W. Kong, H. Yu, M. Zhang, S. Ma, L. Ru, Identifying Web spam with the wisdom of the crowds, ACM Transaction on the Web 6 (1) (March 2012) (Article No. 2, 30 pages).

[24] L. Page, S. Brin, R. Motwani, T. Winograd, The PageRank citation ranking: bringing order to the Web, Stanford Technical Report, 1999. http://ilpubs.stanford.edu: 8090/422/.

[25] H. Wu, M. Gordon, K. DeMaagd, W. Fan, Mining web navigations for intelligence, Decision Support Systems 41 (3) (2006) 574–591.

[26] D. Xu, Y. Liu, M. Zhang, L. Ru, S. Ma, Predicting Epidemic Tendency through Search Behavior Analysis, In Proceedings of the 22nd International Joint Conference on Arti<sup>fi</sup>cial Intelligence (IJCAI-11) (Barcelona, Spain) (2011) 2361–2366.

[27] H. Yang, I. King, M.R. Lyu, DiffusionRank: a possible penicillin for Web spamming, In: Proc. of 30th ACM SIGIR Conference, 2007, pp. 431–438.

[28] B. Zhou, Y. Liu, M. Zhang, Y. Jin, S. Ma, Incorporating Web browsing information into anchor texts for web search, Information Retrieval 14 (3) (2011) 290–314.

![](/api/attachments/W2XC2JVW/fulltext/images/1a45ff27f2b5115d805cf7038c564148f0b5e4c45c5b13346416ba506b94ed40.jpg)

![](/api/attachments/W2XC2JVW/fulltext/images/422dc81a3ffd207364c20b77f2a40bf45ff71ce39763a16e6bec878e2eca1cad.jpg)

![](/api/attachments/W2XC2JVW/fulltext/images/3cc200200a2301a8212e87bc7f8d956794de3dbb53beece3c934b2b1a3b29161.jpg)

![](/api/attachments/W2XC2JVW/fulltext/images/c6118f280f0d29731f359127828643533119e793d90a5c7b0858b9237bbbdf03.jpg)  
Yiqun Liu, Male, born in January 1981. He received his bachelor and Ph.D. degrees from the Dept, of Computer Science and Technology of Tsinghua University in July 2003 and July 2007, respectively. He is now working as an assistant professor in Tsinghua University and an undergraduate mentor for the C.S. & T. department. His research interests include Web information retrieval. Web user behavior analysis and performance evaluation of on-line services. Most of his recent works and publications can be found at his homepage (http://www.thuir.cn/group/\~YQLiu/).

![](/api/attachments/W2XC2JVW/fulltext/images/1c662b704de87a3362c402f61429122efea05c755086e08bb7982dedbede0bd5.jpg)

Shaoping Ma, Male, born in February 1961. He received his bachelor and Ph.D. degrees from the Dept. of Computer Science and Technology of Tsinghua University in July 1982 and July 1997, respectively. He is now working as a professor in Tsinghua University. His research interests include knowledge engineering Web information retrieval and natural language processing. Most of his recent works and publications can be found at his homepage (http:// www.thuir.cn/cms/index.php?page=msp).

Yufei Xue, Male, born in September 1985. He received his bachelor degree from the Dept. of Computer Science and Technology of Tsinghua University in July 2007. He is now a Ph.D. candidate in the same department. His re search interests include Web user behavior analysis and Web user intent analysis.

![](/api/attachments/W2XC2JVW/fulltext/images/4790a6790b3dc5149f9ecedb8110c081de356106da24f185e6feadf00db40d98.jpg)

Rongwei Cen, Male, born in April 1982. He received his bachelor and Ph.D. degrees from the Dept. of Computer Science and Technology of Tsinghua University in July 2005 and July 2010, respectively. He is now working as an engineer in the State Information Center of China. His research interests include Web information retrieval and Web user behavior analysis. Most of his recent works and publications can be found at his homepage (http://www. thuir.cn/group/\~RWCen/).

Min Zhang, Female, born in December 1977. She received her bachelor and Ph.D. degrees from the Dept. of Computer Science and Technology of Tsinghua University in July 1999 and July 2003, respectively. She is now working as an associate professor in Tsinghua University. Her research interests include information retrieval, machine learning and natural language processing. Most of her recent works and publications can be found at her homepage (http:// www.thuir.cn/group/\~mzhang/).

Liyun Ru, Male, born in December 1979. He received his bachelor degree from the Dept. of Computer Science and Technology of Tsinghua University in July 2002. He is now a Ph.D. candidate in the same department. His research interests include Web search engine, user behavior analysis and Web user intent analysis

![](/api/attachments/W2XC2JVW/fulltext/images/4e39d36726f609b273d07fbfab64eb762b6f243e4524e78b4135807dd8c76e12.jpg)

Danqing Xu, Female, born in June 1986. She received her bachelor degree from the Dept. of Computer Science and Technology of Tsinghua University in July 2010. She is now a master student in the same department. Her research interests include Web user behavior analysis and social networks.
