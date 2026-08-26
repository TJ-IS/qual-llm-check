---
otero_id: 10302
otero_key: "MJD8FQFE"
title: "The superhit effect and long tail phenomenon in the context of electronic word of mouth"
authors: "M. Olmedilla; M.R. Martínez-Torres; S.L. Toral"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113120"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The superhit efect and long tail phenomenon in the context of electronic word of mouth

![](/api/attachments/MJD8FQFE/fulltext/images/e75e8b872e060e7be3eb7345e18d6c30dd9aff3911d69a9eb473c7eead5421cb.jpg)

M. Olmedilla<sup>a,⁎</sup>, M.R. Martínez-Torres<sup>b</sup>, S.L. Toral<sup>c</sup>

<sup>a</sup> Léonard de Vinci Pôle Universitaire, Research Center, 92 916 Paris La Défense, France

<sup>b</sup> Facultad de Turismo y Finanzas, University of Seville, Seville, Spain

<sup>c</sup> E. S. Ingenieros, University of Seville, Seville, Spain

## A R T I C L E I N F O

Keywords: Electronic word of mouth (eWOM) User-generated content Long tail Power-law fitting Elbow criterion

## A B S T R A C T

The proliferation of online retailers combined with recommender systems has facilitated the availability of various products and services through the Internet. However, the efect of this availability depends on the products' categories: in some cases, the web promotes the superhit products even more while keeping a short tail; however, in other cases, a long tail efect emerges. This paper investigates the coexistence of the superhit efect and long tail phenomenon from a quantitative perspective and proposes two diferent methods to mathematically indicate the presence of both phenomena in 28 diferent product categories collected from an eWOM (electronic word of mouth) website. The aim is to test whether the Internet promotes best-seller products, niche products or both. The findings reveal that eWOM promotes either the long tail phenomenon or superhit efect depending on the diferent product categories and that they can coexist.

## 1. Introduction

The efect of the Internet and the increase in information available to the consumer are redefining a shift in the distribution of the sales of products that are reviewed and purchased online. This subject has gained much attention and discussion among research related to information systems, marketing or operation management [8,29,56]. In this respect, online markets have proposed that nonhit or niche pro ducts represent an important part of the overall product sales [29]. This transformation of the distribution of product sales is what Anderson called the long tail [1]. The long tail phenomenon can be explained because, although consumers can now find everything efortlessly on the Internet, their choices are based on preferences that are not simi larly distributed [17]. Moreover, different search technologies [33] or peer-based recommendations associated with electronic commerce [55] are strongly related to the phenomenon of the long tail of demand because they lead to redistribution of the demand toward niche products and popular products. Actually, the influence of recommender systems in this point seems to be contradictory because they can promote both niche and popular products. However, this is an open debate in the current literature. In this regard, earlier studies have driven a wedge between two difering directions. On the one hand, research in favor of the long tail idea upholds that boosting the collection of products accessible over online channels (e.g., eWOM communities) will strengthen the sales of niche products [10,23]; however, others advocate the sales of popular products with even high ratings [65]. In both cases, the role of online channels is the same: to help consumers find their desired product, regardless of whether they are less popular or superhit products. The only diference is that, in some cases, the tail is extended, while in others, the tail is shortened [41].

Many existing studies on the topic focus on e-commerce sites [8–10], Web search distributions [35] or cultural products such as music [23], books, films or video games [66]. This paper expands the border of the long tail quantitative research by providing a new perspective on the understanding of both the superhit efect and long tail phenomenon of consumption patterns of online users within an eWOM community. Specifically, the presence of superhit or niche products is studied across the entire spectrum of product categories distributed within an eWOM community. This analysis is based on a unique data set of 105,918 online reviews of 68,650 products posted on a popular eWOM community by 44,352 diferent users. The accessibility to online reviews posted by users within the proper product category and subcategory allows diferentiating the type of distribution across products.

The overall aim of the paper was to test whether the existence of the superhit efect is compatible with the long tail phenomenon. To that end, this study compares two methodologies to mathematically measure a heavy-tailed and a long tail distribution: the power-law fitting method of the distribution of the number of products (supply side factor) per number of online reviews (demand side factor), previously proposed by Clauset et al. [16] and developed by Olmedilla et al. [56], as well as the elbow criterion demarcated by the power-law fitting. The main contribution of the proposed methodology is its ability to math ematically determine the presence of superhit and niche products.

The remainder of the paper is organized as follows. The next section discusses the related work and conceptual framework by conducting a literature review to develop the two proposed research questions. The section thereafter describes the research methodology. Here, the case study and data collection are detailed as well as the two methods used to fit the power-law distribution. The results are next presented. Finally, the study concludes with the discussion and implications of the study.

## 2. Related work and conceptual framework

## 2.1. Superhit efect vs long tail phenomenon

As aforementioned, the power-law distribution curve presents a small group of high-frequency events at the head followed by a large set of low-frequency events in the tail. In the sales distribution, which acquires the form of a power-law distribution, the head represents the superhit products and the long tail the niche products [39]. Fig. 1 depicts an example of a power-law distribution with all probable events ranked by their frequency. To the left (blue) are the superhits that dominate and to the right (orange) is the long tail with the niche content. In this example, there is a red cutof selected so that areas of both the head and long tail are equal. Actually, according to Elberse [23], the orange area under the curve may become larger than the blue area over time.

The superhit efect and long tail phenomenon are two contrasted theories still studied among many researchers. The long tail theory advocates that a big part of consumers prefer popular content while only a minority pursue the niche content [28]. In this regard, Anderson [1] theorizes that the tail at the end of the distribution curve is practically diferent from the head. He adds that consumers are moving toward the niches in the tail since the tail satisfies rare interests better [2]. Today, the Internet is allowing consumers to obtain information related to low-volume products from a massive, geographically dispersed group of people, facilitating this long tail efect [33,56]. Additionally, in some areas such as music, movies or blogging, the tail is theoretically unlimited because the Internet ofers infinite storing space. Since Anderson [1], the studies presented until now about the long tail have provided a theoretical framework or empirical details about the sales of rare products not available in traditional brick-and mortar stores. For example, some studies by Brynjolfsson et al. [8–10] draw attention to the Internet's long tail by analyzing data collected from a clothing retailer or from sales distributions in product markets such as Amazon. They consider that consumers find it easier to search for and discover niche products because (1) the Internet has eliminated communication barriers as well as stocking and distribution costs; and (2) due to the proliferation of Internet discovery tools such as recommendation engines. Similarly, the author Elberse [23] argues that the long tail of the sales distribution is becoming longer and fatter using data from Quickflix or Rhapsody Music.

![](/api/attachments/MJD8FQFE/fulltext/images/827edc187d05d29f38b3019aff32f3510fab0319442554a554938b2c86b4c03d.jpg)  
Fig. 1. Example chart representing the power-law distribution of products/ events.

Other researchers studying power-law distributions of the consumers' actions on the Internet find that much of the action occurring within power laws is placed at the head of the distribution where there are fewer events, but with high frequency [20], in essence, the superhit efect. This efect was originally presented to describe the few top performers reaching most of the audience and achieving most of the profits [62] and currently still thriving among online markets [9,71]. In this regard, Hennig-Thurau & Houston [30] provide empirical evidence that the superhit efect still leads in entertainment and guides consumers away from traditional forms of entertainment to new ones such as social media. Dellarocas [20] reveals through Gini coeficient analysis—a measure of the concentration of demand—that the weekly volume of movie online reviews is more skewed toward popular movies. Consequently, thanks to the Internet and digital technologies and networks [11], a product becomes more appreciated as the number of users increases, indicating that the superhit efect is afecting more products than before.

## 2.2. Electronic word of mouth (eWOM)

Consumers are progressively participating more in sharing their experiences with a product by writing online reviews, and eWOM is widely recognized as an influential information source on consumer decision making, which is well established in the academic literature [36,59]. Additionally, the emergence and impact of user-generated content within the Web have made classic WOM move toward eWOM [31], which has been enabled by the Internet and online communication [50]. Actually, eWOM—considered an inexpensive online medium—is currently decreasing the barriers of entrance into the product markets [49]. eWOM often has a strong impact on product judgements because the information received is more accessible. Reviews are published on many products and services and have become a part of the decision-making process for consumers [52].

Evidence from research suggests the capability of eWOM to find niche products, thus facilitating the long tail phenomenon [31,37] and the way eWOM is decreasing the cost of the information search about products [54]. For example, a study on this topic has concentrated on assessing the relationship between long tail and product sales [9]. Additionally, a more discerning approach is that “the efect of eWOM is not monolithic”, but it difers according to product characteristics [48]. Existing studies on eWOM have primarily dealt with information on products such as movies [67,68], books [8,15] and music [51]. In this regard, online reviews within eWOMs are very significant when con sumers are choosing products that they do not have first-hand experi ence with. Online reviews are also generally used to reduce uncertainty regarding service quality from the consumer perspective [60]. Additionally, the study by Park and Lee [58] describes how eWOM information's direction and website's reputation contribute to the eWOM efect, focusing on the moderating role of the product type.

## 2.3. Fitting power-law distributions online

Not always do the measured processes reach their maximum point around a typical value; sometimes, they diverge across a wide range [53]. For example, when the variance and/or mean is no longer finite, the Central Limit Theorem does not predict Gaussian distributions but predicts distributions that resemble power laws. Additionally, unlike normal distributions, observations in power-law distributions are far to the left of the mean and some outliers represent an uneven quantity of the total distribution's output [18]. In summary, large events occur more often in systems that exhibit power-law distributions. This means that the events in the tail of the distribution are more likely to occur in a power-law distribution, explaining why power laws are also called heavy tailed [3,6]. Thus, the extreme tails are important because they provide an idea of how often, on average, the largest events might occur. Consequently, power-law distribution is considered a valuable tool to measure these information uncertainties because Gaussian dis tributions cannot handle them at a certain probability.

Former and current research has examined whether Internet phenomena are better described by power-law distributions $[ 4 , 7 , 4 3 , 4 6 ]$ The findings in related fields show that power-law distributions usually emerge in Internet social systems [34], where users express their preferences among many choices (e.g., YouTube [27], eWOM communities [56], and Amazon [14]). Similarly, Brynjolfsson, Hu and Smith [8] argue that a power-law distribution can be used to describe the relationship between a product's sales rank and sales quantity. They observed that the interaction of online users exchanging information produces complex dynamics in the demand for products. Consequently, although other heavy-tailed distributions exist (e.g., lognormal, t-distribution, exponential or chi-squared distribution), this paper focuses on the power-law distribution because the superhit efect and long tail phenomenon prevail in online consumption patterns in which a relatively small number of very popular products account for most of the sales [9] and the tail of the distribution encloses niche products [2].

To fit the power-law distribution within this paper the number of reviews is used, not the content. Research has shown that the message content of the online reviews has less impact when users look at many reviews if they are about to make a purchase decision [5]. In this re gard, Shao [64] argues that a higher number of reviews, either positive or negative, is more probable to gather consumers looking for in formation and consequently increases product awareness. The author [44] defended no relationship between the valence of the online review (negative or positive value assigned to an online review) and sales. In this regard, many authors defended that a higher number has a greater influence on sales [13,22,44]. Interestingly, however, review volume does not necessarily mean the reviews are positive. Numerous studies have analyzed the efect of online reviews on product sales or con sumers' choices by also considering the characteristics of the reviews. Ir this respect, Chen et al. [12] argued that “negative WOM information has a greater impact on product sales than positive WOM information”. In fact, many authors have found that the negative reviews have a better im pact on purchase intention than positive reviews [19]. This positive efect of negative reviews has been evidenced in numerous studies. Fo example, Ghose and Ipeirotis [26] associate reviews of products rated negatively with product sales. This author's results are consistent with Berger et al. [5] who show that negative reviews have a positive impac on sales because they can increase publicity for lesser known products. Likewise, the results by Gavilan et al. [25] indicate that the negative reviews are used more for holiday decision making than positive ones. In general, users consider negative reviews more useful [63] or de monstrative for decision-making purposes [42] than positive reviews, because negative information is attention catching and incites curiosit [61] and controversial reviews can provoke substantial discussion [64] Consequently, as the proportion of negative or positive online consumer reviews increases. this indicates that there is a high involvement of consumers. Moreover, the research by Zhang et al. [70] found that consumers who noticed a high number of reviews demonstrated in creased arousal of their purchase intention of a product. Additionally, the authors do not explicitly distinguish the number of reviews as po sitive or negative. Consequently. the more online product reviews that are available the more likely a consumer will be informed about a product. There are other several relevant articles that have verified a positive impact of online reviews on sales by considering the volume of reviews. For example, a recent article by Maslowska et al. [47] found that products that have a high price benefit from a large number of reviews because potential customers detect that others might have bought the product. In this sense, Park et al. [59] also afirmed that the number of reviews can specify a product's popularity due to costumers assuming a relationship between the number of reviews and consumers who have bought the product. Likewise, the findings by Zhou and Duan [72] illustrate that a larger volume of internal WOM, which depends on the number of reviewers, has a positive impact on sales. Extant studies, such as that by Chevalier and Mayzlin [15], indicate that book sales between two sites (Amazon.com and Barnesandnoble.com) are related to the diference in the number of reviews per book throughout the sites. Additionally, Zhang et al. [69] found that the quantity of online reviews, among other characteristics, has an important influence on the sales of digital cameras and search goods.

## 3. Research motivation and research questions

Previous research has found that the impact of the Internet on the consumer product discovery process and found difering evidence regarding the shift in the sales distribution for diferent products. For example, Dellarocas et al. [21], has studied numerous motivations for consumers to contribute by word of mouth for hit or niche products.

On the one hand, the authors Gu et al. [29] examined the long tail phenomenon through the informative efect in the context of eWOM. They demonstrated that positive reviews in Amazon enhance the sales of popular products, whereas negative reviews worsen the sales of niche products. Therefore, their results suggest that “online WOM restrains the formation of the long tail”. On the other hand, and also using data from Amazon, the study by Chevalier and Mayzlin [15] found the opposite; online reviews influence book sales. The authors conclude that online review features influence the increase in the number of books sold at Amazon. This argument is also consistent with Zhu and Zhang [73], who also advocated that online reviews influence the difusion and adoption of products that are less popular. Additionally, Hervas-Draney [32] showed that WOM benefits more popular products and mainstream consumers and the authors Duan et al. [22] found that the number of online reviews is significantly associated with movie sales. Thus, the first research question addresses whether online WOM promote either the superhit efect or long tail phenomenon.

$\mathbf { R } \mathbf { Q _ { 1 } }$ . Does eWOM promote either the superhit efect or long tail phenomenon across product categories?

Furthermore, a large body of literature has studied different evi. dence sources regarding how the Internet afecting diferently the current distribution of products. It has concentrated on assessing the relationship between long tail and product sales [9,31]. For example, researchers have advocated that eWOM is a facilitator of the long tail phenomenon to help identify niche products [20]. By contrast, some researchers describe the distribution of products as very unequal with a few extreme outliers accumulated in the head [65]. Both phenomena are widely acknowledged in the article by Elberse and Oberholzer-Gee [24], where the authors not only found evidence of the long tail efect in home video sales but also found evidence of the superhit efect. This efect was more pronounced among best-selling video titles, which accounted for most of the sales.

An attractive distribution for data generated by these types of cumulative processes is the power law. In this regard, Newman [53] provides evidence that book sales do indeed follow a power law. However, little work has focused on whether the power-law distribu tion is a plausible fit to a data set of diferent product assortment concentrations. Thus, it would be convenient to model the distribution of product categories with the power law to discern whether there are high-frequency events in the short head or low but larger events in the tail. Thus, the outline arose from this framework encompassing the following research question:

$\mathbf { R } \mathbf { Q } _ { 2 } .$ Is it possible that the superhit efect coexists with the long tail phenomenon?

![](/api/attachments/MJD8FQFE/fulltext/images/6b884d380e01f7875a84c3f9d29df8be43b47413d3bdb3265b56b87e63831d2f.jpg)  
Fig. 2. Level specification of the main category “Travel”.

## 4. Research methodology

## 4.1. Case study and data collection

The eWOM community chosen for data gathering and analysis was Ciao UK, which is a popular website that more than 1.3 million users who have written more than 7 million reviews approximately 1.4 million of products [56]. It has branches in local language in major Western European countries. Three principal sections constitute the eWOM community of Ciao UK: the review section, shopping section and “My Ciao” section, which assess the relevant information about each registered user. Primarily, 28 main product categories have been established by Ciao, and each main category is subdivided into many more subcategories. Thus, registered users post and share their reviews within a specific category and subcategory related to the topic of the review. Almost all main categories have four levels of subcategories. For example, Fig. 2 shows the four levels of subcategories for the main cate gory “Travel”. In this case, the subcategory level 2 groups the reviews by continent, level 3 by country and level 4 by city. Because level 4 has a suficient level of detail for travel destination ofers, it was selected as the target level in the case of the Travel main category.

In the case of the main category “Beauty”, Fig. 3 shows that level 4 has also been selected for data analysis. Although there are further levels of detail, the level of specification given by level 5 is too much (almost indicating the product name) and with very few reviews per subcategory. Thus, level 4 was chosen because the information enclosed is suficient to study the data and there are many reviews per subcategory within this level.

Users can access Ciao for free and they also have the option to register. Whether they register, they must create an account where they provide nonmandatory information about themselves (e.g., name, gender, age, and country). To write a review of at least 120 words long, the users have to complete some fields such as the title of the review, name of the product to be reviewed, body containing the user's opinion and advantages and disadvantages. Finally, users post the review within the proper category and subcategory. This is actually the target data that were collected within this paper. Accordingly, the website was completely crawled by extracting a subset of almost 45,000 users, approximately 106,000 reviews of approximately 69,000 products and approximately 283,000 subcategories.

The crawler developed in Olmedilla et al. [57] has been applied to gather the data. More specifically, the programming language Python has been used to crawl the web combined with an open source web crawler framework called Scrapy. To begin with the scraping cycle of all the categories, an item “review” was defined that contains the fields “main category” and “subcategory” to be collected. Next, to crawl the information of each category, a class named spider was programmed. The spider browses the product webpage and, by using XPath selectors to perform data extractions from the HTML source, all the information about the main categories and subcategories was extracted. To this end, the method response.xpath(‘text\_to\_gather’).extract() was called and a list with all the elements (vector) of categories was built. Next, the acquired information was stored in the fields “main category” and “subcategory” from the table “product” inside a relational database designed in MySQL. Applying the SQL querying language can be used to access and track all the data stored in the database.

![](/api/attachments/MJD8FQFE/fulltext/images/984a253c30972103ba72029494ee9ebec91164bfa5c280f2fd665f77fa6ec72c.jpg)  
Fig. 3. Level specification of the main category “Beauty”.

![](/api/attachments/MJD8FQFE/fulltext/images/b36e390f054544387637b729c1818bd74d0b552651c7a1dafede573688f4730f.jpg)  
Fig. 4. Application of the elbow criterion to the power-law distribution.

## 4.2. Quantitative techniques

## 4.2.1. Fitting the power law to gathered data

The first method—the power-law distribution—used by Olmedilla et al. [56] has been extended to decide whether the data set follows a power-law distribution. According to Clauset et al. [16], many of the things that scientists measure have a typical size or ‘scale’—a typical value around which individual measurements are centered. Hence, a Gaussian distribution occurs. Nevertheless, not all things measured are Gaussian; otherwise, large events are extremely rare within Gaussian distributions. Additionally, those events in the part of the distribution that is far away from the mean and characterized by large and infrequent events— the tail—are more likely to occur in a power-law distribution [16]. Consequently, when the probability of peaking around a typical value of some quantity varies over a large dynamic range, these quantities might be consistent with a power-law distribution [53], which is defined as:

$$
P (x) = C x ^ {- \alpha} \mathrm{for} x > x _ {m i n}\tag{1}
$$

where P(x) is the probability (frequency) that the variable takes the value x; ∝ is the exponent of the distribution; x the variable to be analyzed; C is a constant that depends on the type of event; and $x _ { m i n }$ is the minimum value of x over which the power-law behavior starts. Because power laws typically describe systems where the larger events are fewer than smaller events, α remains positive. This confirms that the power law is a monotonically decreasing function.

Taking logarithms on both sides of (1), it is observed that, for a power-law,

$$
\ln (P) = \ln C - \propto \ln x,\tag{2}
$$

indicating that, in a graph with logarithmic scale, the relationship between ln(P) and lnx is described by a straight line whose negative slope is ∝.

In practice, identifying power-law behavior is dificult. In many cases, it is convenient to use the complementary cumulative distribu tion function (CDF) of a power-law-distributed variable, which is denoted as

$$
P (x) = \int_ {x} ^ {\infty} p (x) d x = \left(\frac {x}{x _ {m i n}}\right) ^ {- \alpha + 1}\tag{3}
$$

Essentially, because of applying this power-law distribution method, the cut-of value $x _ { m i n }$ is obtained. This value defines the point where the power-law distribution is no longer valid. Thus, it is the point beyond which there are no superhit products; consequently, the tail of the distribution starts.

R programming language was used to assess the presence of a power law in the data using the library poweRlaw, which follows the protocol for fitting a power-law model as described by Clauset et al. [16]. The function PLFIT was used to estimate x and α according to the

goodness of fit.

## 4.2.2. Finding the optimal x based on the elbow criterion

The second method used is based on the elbow criterion, which is an alternative method to determine the cut-of value $x _ { m i n } .$ . According to Kodinariya and Makwana [38], the elbow criterion is a visual method to determine the number of clusters that should be chosen for k-means clustering. This method is based on the relationship between the percentage of variance with respect to the number of clusters to find the optimal number of clusters. In this relationship, plotted as a graph, it was observed that the first positions reveal a high slope because having a low number of clusters may lead to a high percentage of variance between them. If the number of clusters continues to increase to a certain point, the slope decreases. This is because the increase in the number of clusters might not increase the variance as before, indicating that the optimal number of clusters has been exceeded for k-means clustering, producing an angle in the graph [40,45]. Extending the elbow criterion to the case of a power-law distribution, the problem consists of finding the point $x _ { m i n } ,$ where the sharp “elbow” is clearly visible in the graph.

Fig. 4 illustrates the selection of the elbow criterion based on choosing the value with a sharp decrease in the slope of the tangent. Given the function $f ( x ) = C x ^ { - \infty }$ , the tangent line at the point $( x _ { 0 } , f ( x _ { 0 } ) )$ is the unique straight line that passes through that point and has the same slope as the graph at that point, which is defined by the derivative value $f ^ { \prime } ( x _ { 0 } ) { \mathrm { : } }$

$$
f ^ {\prime (x _ {0})} = \lim _ {x \to x _ {0}} \frac {f (x) - f (x _ {0})}{x - x _ {0}},\tag{4}
$$

The blue lines of Fig. 4 represent the initial and final tangents, corresponding to the slope values of −∞and 0. The intermediate blue dotted lines represent all the possible intermediate values of the slope. The $x _ { m i n }$ is the point of the average slope between the two asymptotes of the graph, given by the value −1, which is the point from which the curve goes from decreasing very fast to decreasing very slow.

## 5. Results

Following the proposed methodology, a power-law distribution was fitted to the curve of the distribution of subcategories created by the users who have posted reviews over the 28 main categories distinguished by Ciao. The gathered result is shown in Fig. 5, which illustrates the distribution of the reviews over the main categories.

All the distributions obtained show some subcategories are very popular while others are only supported by a few reviews. By applying the two methods described in the previous section, we aimed to determine the presence of the superhit efect and length of the queue for each of the 28 main categories of Ciao.

![](/api/attachments/MJD8FQFE/fulltext/images/7ba2956e30cc3a47d40f76a8e6a02ce562202ea962db3a3f382a7d7fdc3e4b47.jpg)  
Fig. 5. Distribution of posted reviews for the 28 main categories.

Table 2  
Long tail parameters of the 28 main categories of Ciao UK according to the power-law method.

<table><tr><td>Main categories</td><td> $x_{min}$ </td><td> $\alpha$ </td><td>p-Value</td><td>Length tail %</td><td>Head area %</td><td>Tail area %</td></tr><tr><td>Adult products</td><td>3</td><td>2.97</td><td>0.602</td><td>68.75</td><td>46.03</td><td>53.97</td></tr><tr><td>Beauty</td><td>3</td><td>2.02</td><td>0.000</td><td>65.91</td><td>74.32</td><td>25.68</td></tr><tr><td>Books</td><td>7</td><td>2.20</td><td>0.011</td><td>76.03</td><td>72.02</td><td>27.98</td></tr><tr><td>Cameras</td><td>4</td><td>1.63</td><td>0.231</td><td>10.53</td><td>98.04</td><td>1.96</td></tr><tr><td>Cars &amp; motorcycles</td><td>3</td><td>1.84</td><td>0.047</td><td>30.00</td><td>89.88</td><td>10.12</td></tr><tr><td>Ciao Café</td><td>18</td><td>1.62</td><td>0.085</td><td>20.00</td><td>98.27</td><td>1.73</td></tr><tr><td>Computers</td><td>5</td><td>1.74</td><td>0.002</td><td>55.48</td><td>91.29</td><td>8.71</td></tr><tr><td>DVDs</td><td>5</td><td>1.78</td><td>0.435</td><td>52.17</td><td>91.13</td><td>8.87</td></tr><tr><td>Education &amp; careers</td><td>8</td><td>1.53</td><td>0.098</td><td>0.00</td><td>100</td><td>0</td></tr><tr><td>Electronics</td><td>20</td><td>2.21</td><td>0.683</td><td>55.56</td><td>88.74</td><td>11.26</td></tr><tr><td>Entertainment</td><td>18</td><td>2.72</td><td>0.940</td><td>56.52</td><td>80.92</td><td>19.08</td></tr><tr><td>Family</td><td>57</td><td>3.50</td><td>0.520</td><td>84.88</td><td>56.41</td><td>43.59</td></tr><tr><td>Fashion</td><td>2</td><td>2.09</td><td>0.065</td><td>35.71</td><td>77.92</td><td>22.08</td></tr><tr><td>Finance</td><td>118</td><td>3.24</td><td>0.590</td><td>50.00</td><td>82.78</td><td>17.22</td></tr><tr><td>Food &amp; drink</td><td>2</td><td>1.81</td><td>0.086</td><td>47.55</td><td>87.76</td><td>12.24</td></tr><tr><td>Games</td><td>9</td><td>2.13</td><td>0.171</td><td>80.52</td><td>73.59</td><td>26.41</td></tr><tr><td>Health</td><td>17</td><td>2.39</td><td>0.064</td><td>86.70</td><td>67.32</td><td>32.68</td></tr><tr><td>House &amp; garden</td><td>19</td><td>2.01</td><td>0.683</td><td>35.90</td><td>94.82</td><td>5.18</td></tr><tr><td>Household appliances</td><td>71</td><td>3.50</td><td>0.703</td><td>81.33</td><td>52.62</td><td>47.38</td></tr><tr><td>Internet</td><td>13</td><td>1.50</td><td>0.048</td><td>11.76</td><td>99.45</td><td>0.55</td></tr><tr><td>Music</td><td>8</td><td>3.50</td><td>0.179</td><td>71.05</td><td>60.18</td><td>39.82</td></tr><tr><td>Musical instruments &amp; equipment</td><td>8</td><td>2.70</td><td>0.711</td><td>83.33</td><td>45.28</td><td>54.72</td></tr><tr><td>Office equipment</td><td>4</td><td>1.52</td><td>0.161</td><td>0.00</td><td>100</td><td>0</td></tr><tr><td>Shopping</td><td>11</td><td>1.50</td><td>0.458</td><td>0.00</td><td>100</td><td>0</td></tr><tr><td>Software</td><td>7</td><td>1.52</td><td>0.538</td><td>20.00</td><td>98.13</td><td>1.87</td></tr><tr><td>Sports &amp; outdoors</td><td>5</td><td>2.21</td><td>0.036</td><td>68.46</td><td>72.56</td><td>27.44</td></tr><tr><td>Telecommunications</td><td>71</td><td>2.22</td><td>0.020</td><td>90.00</td><td>84.10</td><td>15.90</td></tr><tr><td>Travel</td><td>3</td><td>1.98</td><td>0.157</td><td>53.23</td><td>83.12</td><td>16.88</td></tr></table>

Table 1 describes in detail the long tail parameters of the 28 main categories according to the power-law adjustment. The first and second column show the $x _ { m i r }$ and ∝ values of the fitted power-law distribution, respectively. The third column corresponds to the goodness of fit, the pvalue. The fourth column shows the length of the tail. The length of the tail has been calculated as the number of subcategories with several reviews below the $x _ { m i n }$ threshold—that is, the number of subcategories that are not part of the fitted power-law distribution. The fifth and sixth columns represent the areas of the head and tail of the distribution, respectively, calculated also using the $x _ { m i n }$ value.

The values o $\dot { } x _ { m i n }$ distinguish between those subcategories that are part of the head of the power-law distribution (superhit products, above $x _ { m i n } )$ and those that belong to the tail (niche products, below $x _ { m i n } )$ . The ∝ exponent determines the shape of the power-law distribution. The fitting has an associated p-value; thus, in those cases where the calculated p-value is considerably lower than 0.05, the null hypothesis is rejected, indicating that the category does not follow a power-law distribution and there is no superhit efect. However, if the resulting p value is greater than 0.05, the null hypothesis cannot be rejected; hence, the distribution is likely to follow a power-law distribution and shows a superhit efect. Finally, the head area percentage column denotes the area contained to the left of the cut-of point of $x _ { m i n } ,$ which includes the dominating products or best sellers. The tail area percentage column embodies the tail—that is, the region to the right of the cut-of point of $x _ { m i n } .$

The same analysis was conducted but using the elbow method. Table 2 describes the results for the same 28 main categories. The first column displays the $x _ { m i n }$ values, which correspond to the turning point—that is, the point from which the function goes from decreasing very fast to decreasing very slowly. Accordingly, the function is traversed from the right to the left, from $x _ { m a x } \mathrm { t o \ - 1 , }$ , until the first point/ value that meets the search condition. This is the point of the average slope between the two asymptotes of the graph. The second column shows the length of the tail that was calculated using the calculated turning point. Finally, the third and fourth columns represent the areas of the head and tail of the distribution, respectively (calculated using the obtained turning point).

Long tail parameters of the 28 main categories of Ciao UK according to the elbow method.

<table><tr><td>Main categories</td><td> $x_{min}$ </td><td>Length tail %</td><td>Head area %</td><td>Tail area %</td></tr><tr><td>Adult products</td><td>2</td><td>56.25</td><td>63.49</td><td>36.51</td></tr><tr><td>Beauty</td><td>2</td><td>50.50</td><td>80.60</td><td>19.40</td></tr><tr><td>Books</td><td>5</td><td>69.51</td><td>77.23</td><td>22.77</td></tr><tr><td>Cameras</td><td>4</td><td>10.53</td><td>98.04</td><td>1.96</td></tr><tr><td>Cars &amp; motorcycles</td><td>2</td><td>18.75</td><td>95.63</td><td>4.37</td></tr><tr><td>Ciao Café</td><td>8</td><td>13.33</td><td>99.19</td><td>0.81</td></tr><tr><td>Computers</td><td>4</td><td>50.32</td><td>92.52</td><td>7.48</td></tr><tr><td>DVDs</td><td>4</td><td>50.00</td><td>93.51</td><td>6.49</td></tr><tr><td>Education &amp; careers</td><td>8</td><td>0.00</td><td>100.00</td><td>0.00</td></tr><tr><td>Electronics</td><td>24</td><td>62.22</td><td>81.47</td><td>18.53</td></tr><tr><td>Entertainment</td><td>23</td><td>70.83</td><td>62.31</td><td>37.69</td></tr><tr><td>Family</td><td>65</td><td>87.21</td><td>46.34</td><td>53.66</td></tr><tr><td>Fashion</td><td>2</td><td>35.71</td><td>77.92</td><td>22.08</td></tr><tr><td>Finance</td><td>149</td><td>66.67</td><td>54.04</td><td>45.96</td></tr><tr><td>Food &amp; drink</td><td>2</td><td>210.31</td><td>87.76</td><td>12.24</td></tr><tr><td>Games</td><td>11</td><td>83.61</td><td>69.11</td><td>30.89</td></tr><tr><td>Health</td><td>23</td><td>90.37</td><td>59.76</td><td>40.24</td></tr><tr><td>House &amp; garden</td><td>10</td><td>30.77</td><td>95.64</td><td>4.36</td></tr><tr><td>Household appliances</td><td>82</td><td>85.33</td><td>43.82</td><td>56.18</td></tr><tr><td>Internet</td><td>10</td><td>5.88</td><td>99.76</td><td>0.24</td></tr><tr><td>Music</td><td>5</td><td>68.42</td><td>68.86</td><td>31.14</td></tr><tr><td>Musical instruments &amp; equipment</td><td>9</td><td>86.67</td><td>38.58</td><td>61.42</td></tr><tr><td>Office equipment</td><td>8</td><td>16.67</td><td>97.11</td><td>2.89</td></tr><tr><td>Shopping</td><td>107</td><td>33.33</td><td>85.56</td><td>14.44</td></tr><tr><td>Software</td><td>7</td><td>20.00</td><td>98.13</td><td>1.87</td></tr><tr><td>Sports &amp; outdoors</td><td>7</td><td>77.69</td><td>63.88</td><td>36.12</td></tr><tr><td>Telecommunications</td><td>83</td><td>91.25</td><td>79.21</td><td>20.79</td></tr><tr><td>Travel</td><td>2</td><td>36.83</td><td>88.47</td><td>11.53</td></tr></table>

Both methods, the power-law fitting method and elbow criterion, were compared in Table 3 to test their coincidence when identifying the presence of the long tail and considering the area and length criteria. The result of this comparison is shown in the last column of Table 3. A True value means that both methods agree concerning the presence or absence of the long tail, a False value means that both methods disagree, and Uncertain means that both methods generate contradictory results. This is the case of Ciao Café, Electronics, Shopping, or Travel. The decision making was conducted by applying the joint-ratio 80:20 to the area under the tail and length of the tail. An area or length of the tail that is less than 20% of the maximum value indicates the absence of a long tail. Otherwise, the presence of the long tail is accepted.

Figs. 6 and 7 depict some of the distributions for the main categories shown in Table 3. The graphs show a power-law distribution fitted to the curve of the distribution of subcategories of products. Accordingly, the Y axis corresponds to the volume of reviews (number of reviews written by the users) and the X axis represents all the subcategories of products of each of the 28 main categories of products distinguished by Ciao UK. In both Figs. 6 and $^ { 7 , }$ the $x _ { m i n }$ value is demarcated by a horizontal red line representing its value calculated by the elbow method, and by a horizontal blue line representing its value calculated by the power-law method. According to Table 3, 15 of the 28 main categories (Adult Products, Beauty, Books, Entertainment, Family, Fashion, Finance, Food & Drink, Games, Health, Household & Appliances, Music, Musical Instruments, Sports & Outdoors, Telecommunications) clearly exhibit a long tail behavior as both criteria are accomplished using the two proposed methods.

Regarding the superhit efect, the p-values from Table 1 reveal that 7 of the 28 categories among the data sets (Beauty, Books, Cars &

Table 3  
Validity of the long tail presence through the consistency of the decision rules.

<table><tr><td rowspan="2">Main categories</td><td colspan="2">Areas</td><td colspan="2">Length of tail</td><td>Comparison</td></tr><tr><td>Power law</td><td>Elbow</td><td>Power law</td><td>Elbow</td><td>Areas vs. tail</td></tr><tr><td>Adult products</td><td>Strong Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>True</td></tr><tr><td>Beauty</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>True</td></tr><tr><td>Books</td><td>Yes</td><td>Yes</td><td>Strong Yes</td><td>Yes</td><td>True</td></tr><tr><td>Cameras</td><td>No</td><td>No</td><td>No</td><td>No</td><td>True</td></tr><tr><td>Cars &amp; motorcycles</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>False</td></tr><tr><td>Ciao Café</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Uncertain</td></tr><tr><td>Computers</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>False</td></tr><tr><td>DVDs</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>False</td></tr><tr><td>Education &amp; careers</td><td>No</td><td>No</td><td>No</td><td>No</td><td>True</td></tr><tr><td>Electronics</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Uncertain</td></tr><tr><td>Entertainment</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>True</td></tr><tr><td>Family</td><td>Yes</td><td>Strong Yes</td><td>Strong Yes</td><td>Strong Yes</td><td>True</td></tr><tr><td>Fashion</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>True</td></tr><tr><td>Finance</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>True</td></tr><tr><td>Food &amp; drink</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>True</td></tr><tr><td>Games</td><td>Yes</td><td>Yes</td><td>Strong Yes</td><td>Strong Yes</td><td>True</td></tr><tr><td>Health</td><td>Yes</td><td>Yes</td><td>Strong Yes</td><td>Strong Yes</td><td>True</td></tr><tr><td>House &amp; garden</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>False</td></tr><tr><td>Household appliances</td><td>Yes</td><td>Strong Yes</td><td>Strong Yes</td><td>Strong Yes</td><td>True</td></tr><tr><td>Internet</td><td>No</td><td>No</td><td>No</td><td>No</td><td>False</td></tr><tr><td>Music</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>True</td></tr><tr><td>Musical instruments &amp; equipment</td><td>Strong Yes</td><td>Strong Yes</td><td>Strong Yes</td><td>Strong Yes</td><td>True</td></tr><tr><td>Office equipment</td><td>No</td><td>No</td><td>No</td><td>No</td><td>True</td></tr><tr><td>Shopping</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>Uncertain</td></tr><tr><td>Software</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>False</td></tr><tr><td>Sports &amp; outdoors</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Strong Yes</td><td>True</td></tr><tr><td>Telecommunications</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Strong Yes</td><td>True</td></tr><tr><td>Travel</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>Uncertain</td></tr></table>

Motorcycles, Computers, Internet, Sports & Outdoors, Telecommunications) do not obey a power-law distribution (see Fig. 7). Their p-values are small enough so that the power-law model can be firmly discarded, according to their goodness of fit. As a diference and according to their p-values, the remaining 21 categories might be consistent with a powerlaw distribution. Consequently, and answering RQ , eWOM promotes both the superhit and long tail phenomena, although the superhit efect is more frequent across the 28 categories considered.

Among all 21 cases with the superhit efect, there are 6 cases without a long tail (DVDs, Education & Careers, Cameras, House & Garden, Ofice Equipment, Software), 11 with a long tail (Adult Products, Entertainment, Family, Finance, Food & Drink, Games, Health, Household Appliances, Music, Musical Instruments & Equipment, Fashion), and 4 of them with an uncertain long tail (Ciao Café, Shopping, Travel, Electronics). These findings answer ${ \mathrm { R Q } } _ { 2 }$ by showing that it is possible that the superhit efect coexists with the long tail phenomenon depending on the product categories.

![](/api/attachments/MJD8FQFE/fulltext/images/a51305e05fd12efc8ed98205e5a9ace102fccae6c22c7bafd3b7e77f05a1dee9.jpg)

![](/api/attachments/MJD8FQFE/fulltext/images/fb27970fd828165b3fb229a22c5c875d5ac09121058593d5d63cabfc408a9250.jpg)

![](/api/attachments/MJD8FQFE/fulltext/images/36c151b90b81a11e1091fb728b6fd53b7b501dbe9f086f3b2356a42a7ecf7cdf.jpg)

![](/api/attachments/MJD8FQFE/fulltext/images/f31535227617ebaa3ec9d27b5f369141d0ecd324fe24c2fdbea076bee131877d.jpg)  
Subcategories of Food & Drink

![](/api/attachments/MJD8FQFE/fulltext/images/d459c42947bc64671fe8233542fad8ffb5fcf15b303de999c11fe73f6e46fb6c.jpg)

![](/api/attachments/MJD8FQFE/fulltext/images/a76816923a3d249949f5183415ad8388e43a086ac90d57ecebcaac6903b7352b.jpg)  
Subcategories of Household Appliances  
Fig. 6. Distribution of reviews for some of the main categories in Ciao UK (I)

![](/api/attachments/MJD8FQFE/fulltext/images/31f8ac05cf30ebd38be462004ec28d97ac55e904a6fbe252efbe02942b6f24a9.jpg)

![](/api/attachments/MJD8FQFE/fulltext/images/43d5bdcd2528e7e18aa33cdfb57d62ffe3474421fec91d4e111d5263c6c7d47c.jpg)

![](/api/attachments/MJD8FQFE/fulltext/images/98b0ddb95cbe3190fb8f25b7e3574accbb6da548a2582bc5fe029f9ae270229b.jpg)

![](/api/attachments/MJD8FQFE/fulltext/images/e35ed82ac89505f8ffc4304ba5dcdfa50602f89a9e32ca0f369d339d0d0bcf73.jpg)

![](/api/attachments/MJD8FQFE/fulltext/images/2f5bd328decaa2ea58518ff05f24ed3df1a5ef37c4bb4d3749e484d129ba11f8.jpg)

![](/api/attachments/MJD8FQFE/fulltext/images/a2c538818430099389a0ad500a37b78626917fa8cdea835618c002aed6b39b91.jpg)  
Fig. 7. Distribution of reviews for some of the main categories in Ciao UK (II).

## 6. Discussion and implications

## 6.1. Theoretical implications

Theoretically, this paper contributes to the growing research on how the Internet influences the superhit efect and formation of the long tail across Internet data and, more specifically, user-generated content. The results suggest that it is important to consider the impact of the eWOM communities on the consumer product discovery process because many products are only sold online and their consumers are more prone to use online reviews as the primary source for information. Existing literature related to the long tail has shown that eWOM has a positive impact on sales. For example, Brynjolfsson et al. [10] claim that consumers are previously informed about products before buying; thus. niche products are gaining an important share of the overall de. mand. Likewise, Elberse and OberholzerGee [24] show similar result for the comparison of the ofline and online sales of DVD and VHS video titles. The authors show that improvements in word of mouth can explain that the increase in the assortment of products ofered through online channels shift to a much larger number of niche products. In versely, Hervas-Draney [32] show that word of mouth benefits mostly the winner-take-all or market products and mainstream consumers. Thus, the interaction of users exchanging information about products within eWOM communities creates intricate dynamics in demand. More existing studies of eWOM have found evidence of the superhit efect. For example, Standifird [65] supports that eWOM promotes the sales of popular products; thus, the head part of the sales distribution becomes thicker. The premise of our study is to clarify these two schools of thought using the distribution of numerous product categories of online reviews of an eWOM community comprising 283.240 subcategories of 68,650 products to identify in which promotes the superhit and which promotes the long tail. In this regard, our study has found evidence of eWOM as a promoter of both the superhit efect and long tail phenomenon depending on the product categories. However, and following previous studies. the presence of the superhit effect is more extended than the long tail. This result indicates that the long tail phenomenon is closely related to certain categories of products where reviews dis seminate new knowledge about items or subcategories unknown for most users. Additionally, we found evidence that the long tail phenomenon is closely related to certain categories of products (e.g., Beauty, Books, Entertainment, Food & Drink, Health, Games, and Music).

The findings are supported by two quantitative methods that mathematically provide evidence about the superhit efect and long tail phenomena. Moreover, our study has important implications for the literature regarding the impact of eWOM on diferent products. We demonstrate that the long tail phenomenon can coexist with the superhit efect depending on the product category. In this regard, research by Lee et al. [41] argued that eWOM can change the rule of the long tail theory by diferentiating the cases across product types. The authors categorized product types based on the objectivity of product evaluation standards. Not surprisingly, the Internet is making it easier for consumers to gather information at a low cost and allows them to relay more on the experience of others when they evaluate products. Again, the increased availability of online reviews about many diferent products within eWOM communities is the explanatory factor for this phenomenon, given that this online channel allows customers to find more niche products that fit their preferences or to promote a product's popularity. The coexistence of superhit and niche products also means that eWOM has probably expanded an original short tail. Cases such music, entertainment and fashion are examples of product categories where online markets bring the difusion of new options otherwise unknown by customers. Additionally, online reviews provide not only the description of new options but also the quality of experience. Most reviews focus more on feelings, perceptions and satisfaction than on objective characteristics of products. Therefore, online channels ofer more complete information than what can be found in catalogs or advertising.

## 6.2. Managerial implications

In general, the Internet is changing the way consumers behave, and our study contributes to a better understanding of such consumer behavior within online markets. In this regard, our study ofers a new perspective on how online information, specifically within an eWOM community, influences the product awareness efect of both superhit and niche products. This disparity leads to a rich-get-richer situation, favoring the products that are already very popular in certain product categories, and leads to a more egalitarian distribution facilitating the formation of the long tail among other product categories. Consequently, as many assortments of products are only sold online and their consumers are more prone to use online reviews as the primary source for information, managers should understand that the under lying economic principles are finding out which products are enclosed in the tail or in the head of the distribution. Additionally, the study provides new insights about potential markets that can be open because of the tail expansion. Companies can shift toward a specialized ofer, focusing on products belonging to the tail of the distribution rather than to the head. A prior discovery of those categories exhibiting a long tail can then be used to gain new markets advancing future consumer trends.

Today, any brand or company can, at zero cost, reach many potential consumers via the Internet. This makes it profitable to invest time and efort to create products that might be of interest to even just a tiny segment. Therefore, a strategy of increasing product variety and product information about niche products might permit consumers to discover products that otherwise would be unavailable.

## 6.3. Implications for academics and practitioners

This work has implications for academics and practitioners. From an academic perspective, the study ofers the possibility of advancing on the conditions that favor the appearance of the two studied phenomena. Additionally, the distributions of products across categories can change over time, modifying the length of the tail or even the existence of the superhit efect. In general, the Internet is changing the pattern of behavior of consumers, and this study contributes to a better under standing of consumer behavior in online markets.

Due to the current importance of eWOM in businesses and eco nomics, our study has significant implications for multiproduct retailers. A retailer needs to comprehend the impact of eWOM on the distribution of diferent products to ofer the accurate product variety and manage inventory. In this regard, our results show which products of the distribution of product categories are from the long tail or are super hits, allowing specifications of the cases in detail. This implie that practitioners need to be strategic in choosing the product assort ment they are ofering online. Consequently, online retailers may need to focus more; if their objective is to capture the mass market, they should acquire and manage customers using the superhit or most popular products and focus on marketing those superhit products. By contrast, if their objective is to use long tail strategies to sell a wider range of goods in smaller quantities, they should focus on broadening their assortment with more niche products.

Likewise, firms can gain leverage of the results to develop better marketing strategies on advertising and promotion of products that consumers are more likely to purchase in the future.

## 6.4. Research limitations

The principal limitation of this paper could be that the methodology has been implemented in only one eWOM community. Nevertheless, it would be possible to extend the two methods (power-law fitting and elbow criterion) to fit the distribution of products in other eWOM communities. Another probable methodological limitation in this study could be the sample of the data set because Ciao UK does not represent the total population but a particular subset of online users. Additionally, users within Ciao might have multiple profiles, or users' profiles might be employed by several people. Although this limitation does not bias the results, they must be understood as applying to a certain set of online users. A further limitation of the study is that a user does not have to provide any purchase proof of the reviewed product to be allowed to write a review. However, writing reviews reports the following benefits to a user: (1) the status benefit that can be achieved from writing reviews, receiving review ratings from other users, rating and commenting on other reviews and referring members to the site and (2) the economic benefit, which, depending on the status a user has within the community and if he/she writes reviews frequently, a certain amount of money is paid by Ciao. Consequently, to obtain such benefits, the users might not be interested in being dishonest. Finally, another limitation of the data is the absence of sales data because this paper draws on online review volume, which is the best available data within an eWOM community. Nevertheless, the context of this study analyzes product diversity of those products that are supposed to be purchased before the user writes any online review.

## 6.5. Future work

Further research can extend these findings by characterizing the niche products across the long tail and superhit products in the head of the distribution. The goal would be to discover some common patterns among niche products through the creation of social network models or association rules and to discover clusters of niche products that can represent a profitable target for retailers. Furthermore, products can be classified as search and experience products. Thus, as future work, we could analyze which type of product is more prone to exhibit the studied behaviors. It would also be interesting to test the validity of the presented models on other eWOM data, where there is available specific information on sales (e.g., Amazon).

## Acknowledgements

This work was supported by Fundación Hergar under the Research Project entitled “Caracterización del fenómeno de la “Cola Larga” en los portales de boca a boca electrónico” with reference AIFH2017/005.

## References

[1] C. Anderson, The long tail, Wired Magazine 12 (10) (2004).

[2] C. Anderson, Long Tail: Why the Future of Business is Selling Less of More, Hyperion Books, New York, 2008.

[3] H. Aguinis, E. O'Boyle Jr., E. Gonzalez-Mulé, H. Joo, Cumulative advantage: con ductors and insulators of heavy-tailed productivity distributions and productivity stars, Personnel Psychology 69 (1) (2016) 3–66.

[4] A.L. Barabási, R. Albert, Emergence of scaling in random networks, Science 286 (1999) 509–512.

[5] J. Berger, A.T. Sorensen, S.J. Rasmussen, Positive efects of negative publicity: when negative reviews increase sales. Marketing Science 29 (5) (2010) 815–827

[6] K. Bimpikis, M.G. Markakis, Inventory pooling under heavy-tailed demand, Management Science 62 (6) (2015) 1800–1813.

[7] L. Breslau, P. Cao, L. Fan, G. Phillips, G.,.S. Shenker, Web caching and Zipf-like distributions: Evidence and implications, INFOCOM’99, Eighteenth Annual Joint Conference of the IEEE Computer and Communications Societies, Proceedings IEEE, vol. 1, 1999, pp. 126–134.

[8] E. Brynjolfsson, Y. Hu, M. Smith, Consumer surplus in the digital economy: estimating the value of increased product variety at online booksellers. Management Science 49 (11) (2003) 1580–1596.

[9] E. Brynjolfsson, Y. Hu, M. Smith, Research commentary-long tails vs. superstars: the efect of information technology on product variety and sales concentration patterns, Information Systems Research 21 (4) (2010) 736–747

[10] E. Brynjolfsson, Y. Hu, D. Simester, Goodbye pareto principle, hello long tail: the efect of search costs on the concentration of product sales, Management Science 57 (8) (2011) 1373–1386.

[11] E. Brynjolfsson, A. McAfee, M. Spence, New world order: labor, capital, and ideas in the power law economy. Foreign Affairs 93 (4) (2014) 44–53.

[12] Y. Chen, Q. Wang, J. Xie, Online social interactions: a natural experiment on word of mouth versus observational learning, Journal of Marketing Research 48 (2) (2011) 238–254

[13] P.Y. Chen, S.Y. Wu, J. Yoon, The impact of online recommandations and consumer feedback on sales, ICIS 2004 Proceedings (2004) 58.

[14] J. Chevalier, A. Goolsbee, Measuring prices and price competition online: Amazon com and BarnesandNoble com, Ouantitative Marketing and Fconomics 1 (2) (2003) 203–222

[15] J. Chevalier, D. Mayzlin, The efect of word of mouth on sales: online book reviews, Journal of Marketing Research 43 (3) (2006) 345–354.

[16] A. Clauset, C. Shalizi, M. Newman, Power-law distributions in empirical data, SIAM Review 51 (4) (2009) 661–703

[17] E.K. Clemons, How information changes consumer behavior and how consumer

behavior determines corporate strategy, Journal of Management Information Systems 25 (2) (2008) 13–40.

[18] G.C. Crawford, H. Aguinis, B. Lichtenstein, P. Davidsson, B. McKelvey, Power law distributions in entrepreneurship: implications for theory and research, Journal of Business Venturing 30 (5) (2015) 696–713.

[19] G. Cui, H.K. Lui, X. Guo, X. The efect of online consumer reviews on new produc sales, International Journal of Electronic Commerce 17 (1) (2012) 39–58.

[20] C. Dellarocas, R. Narayan, R, Tall heads vs. long tails: do consumer reviews increase the informational inequality between hit and niche products? School of Business Research Paper No. 06-056, 2007.

[21] C. Dellarocas, G. Gao, R. Narayan, Are consumers more likely to contribute online reviews for hit or niche products? Journal of Management Information Systems 27 (2) (2010) 127–158.

[22] W. Duan, B. Gu, A.B. Whinston, Do online reviews matter?—an empirical investigation of panel data, Decision Support Systems 45 (4) (2008) 1007–1016.

[23] A. Elberse, Should you invest in the long tail? Harvard Business Review 86 (7/8) (2008) 88–96.

[24] A. Elberse, F. Oberholzer-Gee, Superstars and Underdogs: An Examination of the Long Tail Phenomenon in Video Sales, Harvard Business School. 2007, pp. 07–015

[25] D. Gavilan, M. Avello, G. Martinez-Navarro, The influence of online ratings and reviews on hotel booking consideration, Tourism Management 66 (2018) 53–61.

[26] A. Ghose, P.G. Ipeirotis, Estimating the helpfulness and economic impact of product reviews: mining text and reviewer characteristics, IEEE Transactions on Knowledge and Data Engineering 23 (10) (2011) 1498–1512.

[27] P. Gill, M. Arlitt, Z. Li, A. Mahanti, Youtube traffic characterization: a view from the edge, Proceedings of the 7th ACM SIGCOMM Conference on Internet Measurement. 2007. pp. 15–28.

[28] S. Goel, A. Broder, E. Gabrilovich, B. Pang, Anatomy of the long tail: ordinar people with extraordinary tastes, Proceedings of the Third ACM International Conference on Web Search and Data Mining, 2010, pp. 201–210.

[29] B. Gu, Q. Tang, A. Whinston, The influence of online word-of-mouth on long tail formation, Decision Support Systems 56 (2013) 474–481.

[30] T. Hennig-Thurau, M.B. Houston, Integrated entertainment marketing: creating blockbusters and niche products by combining product, communication, distribution, and pricing decisions, Entertainment Science (2019) 785–820.

[31] T. Hennig-Thurau, K.P. Gwinner, G. Walsh, D. Gremler, Electronic word-of-mouth via consumer-opinion platforms: what motivates consumers to articulate themselves on the Internet? Journal of Interactive Marketing 18 (1) (2004) 38–52.

[32] A. Hervas-Draney, Word of Mouth and Taste Matching: A Theory of the Long Tail, (2009).

[33] O. Hinz, J. Eckert, B. Skiera, Drivers of the long tail phenomenon: an empirica analysis, Journal of Management Information Systems 27 (4) (2011) 43–70

[34] B. Huberman, The Laws of the Web: Patterns in the Ecology of Information, MIT Press, Cambridge, Massachusetts, 2003.

[35] B. Huberman, F. Wu, Bootstrapping the long tail in peer to peer systems, Managing Complexity: Insights, Concepts, Applications, Springer, Berlin Heidelberg, 2008, pp. 263–272.

[36] F.R. Jiménez, N.A. Mendoza, Too popular to ignore: the influence of online reviews on purchase intentions of search and experience products, Journal of Interactive Marketing 27 (3) (2013) 226–235.

[37] M. Khammash. G. Griffiths. Arrivederci CIAO.com. Buongiorno Bing.com'— electronic word-of-mouth (eWOM). antecedences and consequences. International Journal of Information Management 31 (1) (2011) 82–87.

[38] T. Kodinariva, P. Makwana. Review on determining number of cluster in K-means clustering. International Journal 1. (6) (2013) 90–95.

[39] C. Koçaş, C. Akkan, A system for pricing the sales distribution from blockbusters to the long tail, Decision Support Systems 89 (2016) 56–65.

[40] T. Krahe, R. El-Danaf, E. Dilger, S. Henderson, W. Guido, Morphologically distinct classes of relay cells exhibit regional preferences in the dorsal lateral geniculate nucleus of the mouse, The Journal of Neuroscience 31 (48) (2011) 17437–17448

[41] J. Lee, J.N. Lee, H. Shin, The long tail or the short tail: the categorv-specific impact of eWOM on sales distribution, Decision Support Systems 51 (3) (2011) 466–479.

[42] J. Lee, D.H. Park. I. Han, The effect of negative online consumer reviews on product attitude: an information processing view. Electronic Commerce Research and Applications 7 (3) (2008) 341–352

[43] X. Li, Y. Xu, Y. Zhang, J. Shi, Long Tail Distribution in the Web Usage of a Chinese Learning Website, Information Science and Engineering, International Symposium, (2012), pp, 64–67.

[44] Y. Liu, Word of mouth for movies: its dynamics and impact on box office revenue Journal of Marketing 70 (3) (2006) 74–89.

[45] T. Madhulatha, An overview on clustering methods, Journal of Engineering IOSR 2 (4) (2012) 719–725

[46] A. Mahanti, N. Carlsson, A. Mahanti, M. Arlitt, C. Williamson, A tale of the tails: power-laws in internet measurements, IEEE Network 27 (1) (2013) 59–64.

[47] E. Maslowska, E.C. Malthouse, V. Viswanathan, Do customer reviews drive purchase decisions? The moderating roles of review exposure and price. Decision Support Systems 98 (2017) 1–9

[48] E. Manes, E., A. Tchetchik, The role of electronic word of mouth in reducing information asymmetry: an empirical investigation of online hotel booking, Journal of Business Research 85 (2018) 185–196.

[49] M. Martínez-Torres, Analysis of open innovation communities from the perspective of Social Network Analysis, Technology Analysis & Strategic Management 26 (4)

(2014) 435–451.

[50] W.W. Moe, M. Trusov, The value of social dynamics in online product ratings forums, Journal of Marketing Research 48 (3) (2011) 444–456.

[51] M. Morales-Arroyo, T. Pandey, Identification of critical eWOM dimensions for music albums. JEEE International Conference on Management of Innovation and Technology (2010) 1230–1235.

[52] S. Mudambi, D. Schuf, What makes a helpful online review? A study of customer reviews on Amazon.com, MIS Quarterly 34 (1) (2010) 185–200.

[53] M. Newman, Power laws, Pareto distributions and Zipf's law, Contemporary Physic 46 (5) (2005) 323–351.

[54] A. Odić, M. Tkalčič, J. Tasič, A. Košir, Predicting and detecting the relevant con textual information in a movie-recommender system, Interacting with Computers 25 (1) (2013) 74–90.

[55] G. Oestreicher-Singer, A. Sundararajan, Recommendation networks and the long tail of electronic commerce. MIS Ouarterly 36 (1) (2012) 65–83

[56] M. Olmedilla, M.R. Martínez-Torres, S. Toral, Examining the power-law distribution among eWOM communities: a characterisation approach of the Long Tail, Technology Analysis & Strategic Management 28 (5) (2015) 601–613.

[57] M. Olmedilla. M.R. Martínez-Torres, S. Toral. Harvesting Big Data in social science: a methodological approach for collecting online user-generated content, Compute Standards & Interfaces 46 (2016) 79–87

[58] C. Park, T.M. Lee, Information direction, website reputation and eWOM efect: a moderating role of product type, Journal of Business Research 62 (1) (2009) 61–67.

[59] D.H. Park, J. Lee, I. Han, The efect of on-line consumer reviews on consume purchasing intention: the moderating role of involvement, International Journal of Electronic Commerce 11 (4) (2007) 125–148

[60] T. Reimer. M. Benkenstein. When good WOM hurts and bad WOM gains: the effect of untrustworthy online reviews, Journal of Business Research 69 (12) (2016) 5993-6001.

[61] J. Ren, J.V. Nickerson, Online review systems: How emotional language drives sales, Twentieth Americas Conference on Information Systems, 2014 (April).

[62] S. Rosen, The economics of superstars, The American Economic Review 71 (5) (1981) 845.

[63] S. Sen, D. Lerman, Why are you telling me this? An examination into negative consumer reviews on the web, Journal of Interactive Marketing 21 (4) (2007) 76-94.

[64] K. Shao, The efects of controversial reviews on product sales performance: the mediating role of the volume of word of mouth, International Journal of Marketing Studies 4 (4) (2012) 32

[65] S. Standifird, Reputation and ecommerce: eBay auction and the asymmetrical impact of positive and negative ratings, Journal of Management 27 (3) (2001) 279–295.

[66] C. Tucker, J. Zhang, How does popularity information afect choices? A field ex periment, Management Science 57 (5) (2011) 828–842.

[67] W. Yang, Y. Huang, Y. Lin, Study of comments on oficial movie blogs, International Journal of Electronic Business Management 34(3) (200) 201–210.

[68] J. Yeap, J. Ignatius, T. Ramayah, Determining consumers' most preferred eWOM platform for movie reviews: a fuzzy analytic hierarchy process approach, Computers in Human Behavior 31 (2014) 250–258.

[69] L. Zhang, B. Ma, D.K. Cartwright, The impact of online user reviews on cameras sales. European Journal of Marketing 47 (7) (2013) 1115–1128

[70] K.Z. Zhang, S.J. Zhao, C.M. Cheung, M.K. Lee, Examining the influence of online reviews on consumers' decision-making: a heuristic-systematic model. Decision Support Systems 67 (2014) 78–89.

[71] W. Zhou, W. Duan, Online user reviews, product variety, and the long tail: an empirical investigation on online software downloads. Electronic Commerce Research and Applications 11 (3) (2012) 275–289.

[72] W. Zhou, W. Duan, An empirical study of how third-party websites influence the feedback mechanism between online word-of-mouth and retail sales. Decision Support Systems 76 (2015) 14–23.

[73] F. Zhu, X. Zhang, Impact of online consumer reviews on sales: the moderating role of product and consumer characteristics, Journal of Marketing 74 (2) (2010) 133-148.

María Olmedilla is an Associate Professor of Data Analytics and Digital Marketing in the EMLV Business School at the University Pôle Léonard de Vinci. She obtained a PhD in Strategic Management and International Business at the University of Seville. Her main research interests include eWOM and Open Innovation communities, studving the Long Tail characterization and recommender systems.

Rocío Martínez-Torres was born in Madrid, Spain, in 1973. She received the degree in Business Administration in 1996 and the Ph. D. degree from the University of Seville Spain. in 2003. She is currently a Professor at Management and Marketing Department at the University of Seville. Her research interests include intellectual capital and knowledge management. virtual communities and open innovation

Sergio Toral is full Professor in Digital Electronic Systems at the Department of Electronic Engineering, University of Seville. His main research interests include Open Source Software projects, Open Innovation, Computational Intelligence and Social Network Analysis.
