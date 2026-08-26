---
otero_id: 10838
otero_key: "P2CE2JYP"
title: "Conceptualizing means-end chains of user goals as networks"
authors: "Sabine Matook"
year: "2013"
journal: "Information & Management"
doi: "10.1016/j.im.2012.12.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Conceptualizing means-end chains of user goals as networks

Sabine Matook \*

The University of Queensland, UQ Business School, 3 Blair Drive, Brisbane 4072, Queensland, Australia

A R T I C L E I N F O

Article history: Received 23 February 2009 Received in revised form 7 November 2012 Accepted 15 December 2012 Available online 2 January 2013

Keywords: Goal-directed behavior User goals Means-end chains Social network analysis Degree centrality Flow betweenness centrality UCINET

## A B S T R A C T

Goals are desired states that an individual tries to attain. The process of achieving a goal can be represented as interlinked means-end chains of user goals that have been traditionally visualized as hierarchies. Evidence in recent literature suggests that a network structure would be more appropriate and provide insight into a user’s process of seeking a goal. We investigated user goal means-end chains for the eBay online auction system, and produced its structure as a goal network. To analyze this network and assess the importance of various goals, social network analysis measures were used (specifically, degree and flow-betweenness centrality). In addition, goal networks for users with low and high IS value were created and differences in goal importance in the two groups were considered. Results revealed that the most important user goals are closely related to key features of the auction system; users with high IS value want to use eBay to buy, sell, and bid for products, while users with low IS value seem to avoid using eBay because of uncertain price bidding. As such, the results of our study suggest that differences in IS value may be due to differences in IS usage. IS designers, marketers, and providers of online auction system can use our findings to design and promote better systems for their users.

\- 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Users employ information systems (IS) to carry out goaldirected activities such as using a word processor to write a document or an enterprise system to create an invoice. The goals direct a user’s actions and behavior, including the adoption and acceptance of an IS [21]. Therefore, IS adoption is considered to be a goal striving process. For example, TAM assumes the user goal of enhanced job performance in work processes [12]. Despite that IS research considers user goals [1], they are often treated as constant. Yet, users often pursue multiple goals and aim to accomplish them with as little effort as possible. In their goal pursuit, users create paths of interlinked goals, known as meansend chains. In these, end goals represent desired final states and means goals represent intermediate states along the chain [15]. To understand user goals, prior IS research used means-end theory to determine goals for eBay, the online auction system [40], for hedonic gaming websites [30], and the use of mobile devices [23].

Means-end chains are commonly modeled as hierarchies [e.g., in the IS literature see 2,10,23]. A goal hierarchy is characterized by layers of super- and subordinated goals. One main assumption is that the chains are directed from lower to higher levels with the top hierarchical level providing the goals of importance. However, recent studies have suggested that a network model may be more appropriate for goal means-end chains [e.g., 4,26,34]. Comparing between the structures of a hierarchy and a network, van Rekom and Wierenga identified the network structure as a better representation of individual behavior when selecting a future employer. Their comparison also revealed differences in goal importance, which suggested that, depending on the structure used to represent means-end chains, differences occur over a user’s key motivational drivers for a behavior (i.e., user goals).

Against this backdrop, our research has two aims. Firstly, we attempt to determine the emergent structure for user goal means-end chains of an IS. To be able to use prior research results, eBay was selected as our study base. Secondly, we wish to determine differences in the emergent goal structure for a user’s IS value assessment. Users adoption and usage decision depends on the value provided by the IS; thus the IS is of value if it enables goal achievement. We used social network analysis measures (degree centrality and flow betweenness centrality) to examine variations in the IS value. Our research questions therefore are: (1) What is the structure of user goal means-end chains for eBay? and (2) To which extent do the goal structures differ based on IS value?

Our research enhances our understanding of the structure of user goal means-end chains for an online auction system and the importance of specific user goals. It also provides knowledge into the motivational commitment of users and the goals they try to attain. From a practical viewpoint, the conceptualization of user goals as interrelated goal networks may assist practitioners in the fields of software design and development, marketing, and service management (i.e., auction providers). Understanding what goals are important for users enables IS development teams to prioritize their goals and IS marketing operators to highlight important goals during advertising campaigns.

## 2. Theoretical background

## 2.1. Goal-directed behavior toward IS

Many IS researchers have adopted the psychological definition that perceived usefulness is the belief that IS use depends on the extent to which a user sees value in the IS [11], but others have argued that behavior is directed by goals and that a user’s desire to achieve a goal explains IS usage. To account for goals and goal desire, goal-oriented models emerged in IS research that focus on what the user wants to achieve with an IS. An example of a goaloriented model in IS is the ‘decision core’ [5] which has been conceptually developed but not yet empirically validated; this model maintains the attitude–intention–behavior relationship but introduces desire as a mediating factor, where desire is seen as a necessary requirement for the development of intentions and thus is placed between attitude and intention. The motivational commitment, which is the degree of desire, can vary for different goals. Hence, the ‘decision core’ bridges between goal setting and the use of the IS to achieve the goals.

Goals may be self-set (e.g., write a letter), assigned (e.g., a company requires the use of an accounting IS, collectively developed (e.g., a team decides on the use of wikis for project documentation) [22], or adopted (e.g., an individual wants his or her project team to win a quality award). Different goal sources can influence the number of user goals, which may agree or disagree with one another. Goals that work in the same direction support each other, and attainment of one goal contributes to the attainment of another. One way to resolve goal conflicts is by assigning priorities of each goal among them all [3]. Consequently, a goal ranking emerges and users pursue the more important ones first.

From an economic perspective, all behavior is rational as reflected by selecting means based on maximizing utility. However, individuals can be distracted in their goal pursuit by emotional factors such as impulsive, spontaneous, and automatic behaviors. While studying continuing IS use, Ortiz de Guinea and Markus [24] argued that habitual behavior is not rational but is triggered by unconsciously performing a habit. Still, they considered habitual behavior to be a goal striving process in which the user’s behavior is focused on goal achievement. The use of an IS depends, however, on the value that an IS provides to the user by achieving a goal. For example, a user wants to buy stocks of company BHP Billiton. Therefore, the user needs to find out its current stock price. The user’s goal is to ‘‘get stock price information for BHP Billiton’’. Among various options (e.g., financial newspapers), the user believes that an online search at the Australian stock exchange will result in satisfactory goal achievement. With this belief, the user develops a desire to use the ASX website, performs the search, and gets the information. In this case, the user was successful in goal attainment, the IS was useful in fulfilling the goal, hence, the user would evaluate the IS as having high value.

## 2.2. The theory of means-end chains

Means-end chain theory posits that individual behavior is driven by personal motives which can be conceptualized in the context of an IS as user goals [15]. The theory assumes that individuals behave in a certain way, e.g., purchase a product or use a tool, not for the sake of it; rather they view the behavior as a means to achieve something. Thus, individuals engage in activities or use objects because they expect a particular value from their behavior.

Traditionally, means-end chains have been conceptualized as hierarchical, with alternating means and ends [13]. These chains form a goal structure of super-ordinate and sub-ordinate goals that are relevant to a specific behavior. The evaluation of a behavior or a product is conceptualized as a top-down process in which the higher level goals require satisfaction of all lower level goals [25]. Thus, in a hierarchy, different goal levels exist. The low level goals are means to achieve end goals at the middle level, which in turn are means to achieving the higher level goals. For example, Chiu presents login mechanism as a means to achieve the middle layered goal of preventing unauthorized access to satisfy the final end of security of data and documents. Lower level goals have therefore been attributed lower importance than middle and higher level goals.

IS research has used means-end theory to elicit user goals for different IS (see Table 1). All of the studies used laddering, an indepth interviewing technique, to elicit individual goals. The resulting structure of the user goals is a hierarchy with three to five levels.

For illustrative purposes of a goal means-end chain, Fig. 1 presents a goal hierarchy of one of the studies. Note that there are three goal groups that are further explained in the methodology section.

Table 1  
Means-end chain studies in IS research.

<table><tr><td>Study</td><td>Research focus</td><td>Means-end structure</td><td>Number of goal and goal examples</td></tr><tr><td>[10]</td><td>Requirements identification of a web-based document management system</td><td>Hierarchical: 3 layers</td><td>49 goals (e.g., document tracking mechanisms, decreasing data entry errors, security of data, control of document procession procedures)</td></tr><tr><td>[20]</td><td>Identifying reasons for resistance to Internet banking</td><td>Hierarchical: 3 layers</td><td>30 goals (e.g., resistance to change, lack of an official receipt, insecure to use, possibility of password misuse)</td></tr><tr><td>[23]</td><td>Better understanding of the value of mobile applications</td><td>Hierarchical: 5 layers with fundamental and means objectives</td><td>37 goals (e.g., minimize cost of mobile devices, maximize speed of mobile services, increase bandwidth, prevent tampering of data)</td></tr><tr><td>[30]</td><td>Motivation of users to choose a entertainment web sites and information web sites</td><td>Hierarchical: 3 layers</td><td>25 goals for entertainment websites (e.g., find other people, happiness)</td></tr><tr><td>[31]</td><td>Identification of critical functionalities of a successful e-learning system</td><td>Hierarchical: 4 layers</td><td>22 goals for information websites (e.g., better side design, save time, satisfaction)</td></tr><tr><td rowspan="2">[40]</td><td rowspan="2">Measuring IS usefulness in relation to various user goals for an auction website</td><td rowspan="2">Hierarchical: 4 layers</td><td>46 goals from the instructor&#x27;s perspective (e.g., web template for instruction material, save time in preparing instruction material)</td></tr><tr><td>27 goals (e.g., purchase a product, sell a product, enjoy usage, benefit from getting rid of a product)</td></tr></table>

![](/api/attachments/P2CE2JYP/fulltext/images/2f3df60e6a3bcd472f05acc366cb3645c69bb118079720a2115be83fafd5369e.jpg)  
Fig. 1. Means-end chain hierarchy of online auction IS by Zumpe and van der Heijden.

In the goal hierarchies of Table 1, lower layered goals are more concrete goals (e.g., web template for instruction material) than the higher ones (e.g., fun and enjoyment of life) [31]. The number of means-end chain goals identified varies between 22 and 49 goals. For example, Subramony identified 22 goals for information web sites and 25 for entertainment websites, which are connected in a total of 61 means-end chains. The meaning of the means-end chain goals spans a wide field. For example, Chiu creates means-end chains to identify user requirements for IS development, while Nah et al. elicited user goals for mobile commerce. Means-end chains have also been used to identify hindrances toward using a particular technology, as shown by Kuisma et al. [20] for Internet banking; he elicited goals, for example, perceived insecurity of the online channel, bank account misuse, and a general strong resistance to change from using an AMT to Internet banking. A study by Zumpe and van der Heijden identified user goals for e-Bay’s system, which referred to the key functions; i.e., bidding for a product, and buying a product, but also included more high-level goals as end goal; e.g., enjoy using the product, or benefit from its usage.

## 2.3. Structural approaches for means-end goal chains

## 2.3.1. Competing understanding of goal means-end chains as hierarchies and networks

Modeling means-end chains as hierarchies is based on the assumption that the cognitive paths of goal achievement start at lower layered goals and go through layered goals to the higher goals. Various studies have supported this hierarchical model [18,25]. However, there are reasons why this model may not be an optimal representation: bi-directional linkages sometimes occur between goals in a hierarchy. The strongest evidence for structuring goal means-end chains as goal networks was presented by van Rekom and Wierenga. Their results suggested that goals form a network; as they did not represent means-end chains as a hierarchy but investigated the structure. For example, they asked if the goal feel fine is a means to the goal be motivated and also if the goal be motivated is a meanstothe goal feel fine. Using anexample of students who are seeking employment, differences in goal importance and goal position for different goal structures were determined.

## 2.3.2. Analysis of goal networks using graph theory and social network analysis

Graph theory provides a common vocabulary and basic concepts to describe structures (e.g., networks and hierarchies)

[38]. Graph theory and social network analysis provide a way to calculate measures of graph structures [37]. A user goal (either a means or end goal) is represented as a vertex and the paths represent the edges. A graph is a directed digraph if a direction is assigned to each of its edges. A digraph is symmetric (bidirectional), if the graph has two directions and is asymmetric, if for each edge only one direction exists. A hierarchy is an acyclic asymmetric digraph when it has a finite set of vertices that have no incoming edges and a finite set of vertices that have no outgoing edges. When the entire graph has a direction, it cannot have bidirectional edges [9]. Consequently, a network is a symmetric digraph with bi-directional edges. Social network analysis considers a graph to be a network even if edges are asymmetric (e.g., friendship networks). In our study, however, we refer to a graph as a network only if it is symmetric.

In graph theory and social network analysis there are different measures of centrality; they are used to locate the position of a vertex (a user goal in our application). Prior research in IS used measures of centrality in their studies. For example, centrality was used to determine the nature and names of central actors of the European Conference on IS community [35], and to study ‘‘give-help’’ relationships among employees in settings where knowledge barriers exists that constrain the use of an IS [33].

Three centrality measures are common in the analysis of networks:

Degree centrality of a vertex refers to the number of direct edges attached to it [19]. The more edges a vertex has to other vertices in the graph the more prominent it is. Prominence indicates the importance of a vertex in such way that highly prominent vertices are most important. In a network, vertices positioned at the periphery have fewer linkages to other vertices. Degree centrality is calculated by summing up the number of outdegrees (i.e., edges beginning at a vertex) and in-degrees (i.e., edges ending at a vertex) [14].

Closeness centrality is the sum of the shortest paths of a vertex to all other vertices [14]. Goals with lower closeness scores are likely to be achieved more quickly than other goals, because the means-end chain will reach them earlier. It does, however, not mean that these goals represent the final user end goals [7]. Betweenness centrality measures the extent to which a vertex controls and mediates the shortest path between other vertices [39]. It considers a vertex as being in a beneficial position if it is positioned on the shortest path between two other vertices: it counts the number of shortest paths that pass through a vertex and can be used to explain the importance a particular goal. Flow betweenness centrality is measured by the proportion of the entire flow between pairs of vertices [16]. This centrality measure is concerned with a vertex that lies on a large number of paths. Thus, this measure determines to which extent the flow of information, gossip, and cognitive linkages would be reduced if the particular vertex was removed from the graph.

Aggregated implication matrix for the auction IS eBay.

<table><tr><td rowspan="2">Goal no.</td><td colspan="14">eBay goals as ends</td><td rowspan="2">Out-degrees</td></tr><tr><td>eBay goals as means</td><td>G1</td><td>G2</td><td>G3</td><td>G4</td><td>G5</td><td>G6</td><td>G7</td><td>G8</td><td>G9</td><td>G10</td><td>G11</td><td>G12</td><td>G13</td></tr><tr><td>G1</td><td>Buying a product</td><td></td><td>0.84</td><td>0.88</td><td>0.28</td><td>0.59</td><td>0.46</td><td>0.16</td><td>0.51</td><td>0.46</td><td>0.26</td><td>0.27</td><td>0.18</td><td>0.21</td><td>5.10</td></tr><tr><td>G2</td><td>Bidding for a product</td><td>0.48</td><td></td><td>0.71</td><td>0.25</td><td>0.42</td><td>0.42</td><td>0.16</td><td>0.42</td><td>0.38</td><td>0.25</td><td>0.26</td><td>0.23</td><td>0.21</td><td>4.17</td></tr><tr><td>G3</td><td>Searching for product in reg. of price and characteristic</td><td>0.70</td><td>0.50</td><td></td><td>0.36</td><td>0.52</td><td>0.44</td><td>0.29</td><td>0.46</td><td>0.36</td><td>0.28</td><td>0.28</td><td>0.29</td><td>0.27</td><td>4.73</td></tr><tr><td>G4</td><td>Selling a product</td><td>0.43</td><td>0.28</td><td>0.45</td><td></td><td>0.09</td><td>0.36</td><td>0.70</td><td>0.23</td><td>0.12</td><td>0.38</td><td>0.37</td><td>0.60</td><td>0.54</td><td>4.54</td></tr><tr><td>G5</td><td>Getting a product with the intention to use it yourself</td><td>0.85</td><td>0.70</td><td>0.70</td><td>0.23</td><td></td><td>0.19</td><td>0.18</td><td>0.56</td><td>0.53</td><td>0.14</td><td>0.13</td><td>0.12</td><td>0.19</td><td>4.53</td></tr><tr><td>G6</td><td>Getting a product with the intention to give it away</td><td>0.63</td><td>0.54</td><td>0.46</td><td>0.31</td><td>0.18</td><td></td><td>0.42</td><td>0.19</td><td>0.19</td><td>0.43</td><td>0.51</td><td>0.37</td><td>0.34</td><td>4.58</td></tr><tr><td>G7</td><td>Getting rid of (sell) a product</td><td>0.30</td><td>0.23</td><td>0.29</td><td>0.69</td><td>0.21</td><td>0.42</td><td></td><td>0.13</td><td>0.23</td><td>0.47</td><td>0.37</td><td>0.59</td><td>0.59</td><td>4.53</td></tr><tr><td>G8</td><td>Enjoy using a product</td><td>0.81</td><td>0.67</td><td>0.60</td><td>0.14</td><td>0.66</td><td>0.23</td><td>0.17</td><td></td><td>0.65</td><td>0.30</td><td>0.18</td><td>0.13</td><td>0.24</td><td>4.79</td></tr><tr><td>G9</td><td>Benefit from the usage</td><td>0.83</td><td>0.59</td><td>0.60</td><td>0.19</td><td>0.72</td><td>0.24</td><td>0.19</td><td>0.77</td><td></td><td>0.19</td><td>0.17</td><td>0.18</td><td>0.21</td><td>4.89</td></tr><tr><td>G10</td><td>Enjoy giving away a product</td><td>0.51</td><td>0.46</td><td>0.34</td><td>0.54</td><td>0.23</td><td>0.64</td><td>0.46</td><td>0.23</td><td>0.20</td><td></td><td>0.66</td><td>0.40</td><td>0.40</td><td>5.06</td></tr><tr><td>G11</td><td>Benefit from giving away a product</td><td>0.44</td><td>0.34</td><td>0.30</td><td>0.64</td><td>0.21</td><td>0.70</td><td>0.52</td><td>0.21</td><td>0.19</td><td>0.72</td><td></td><td>0.40</td><td>0.42</td><td>5.09</td></tr><tr><td>G12</td><td>Enjoy getting rid of (sell) a product</td><td>0.33</td><td>0.27</td><td>0.26</td><td>0.68</td><td>0.21</td><td>0.36</td><td>0.73</td><td>0.15</td><td>0.18</td><td>0.52</td><td>0.42</td><td></td><td>0.58</td><td>4.70</td></tr><tr><td>G13</td><td>Benefit from getting rid of a product</td><td>0.28</td><td>0.23</td><td>0.18</td><td>0.68</td><td>0.17</td><td>0.41</td><td>0.71</td><td>0.18</td><td>0.18</td><td>0.48</td><td>0.56</td><td>0.69</td><td></td><td>4.77</td></tr><tr><td></td><td>In-Degrees</td><td>6.59</td><td>5.66</td><td>5.78</td><td>5.01</td><td>4.21</td><td>4.87</td><td>4.70</td><td>4.03</td><td>3.66</td><td>4.40</td><td>4.18</td><td>4.19</td><td>4.21</td><td>61.48</td></tr></table>

When analyzing goal structure, it is important to consider that network graphs are focused on central vertices but hierarchies are concerned with the top vertices in the hierarchy.

## 3. Methodology

In our study, data were collected with a questionnaire (see Appendix A). We used results from prior research, in particular user goals found by Zumpe and van der Heijden. We carefully studied the authors’ data collection and analytic process, and believe they correctly carried out their research when eliciting the goals and building the mean-end chains. Building on prior findings (i.e., goals already identified for an IS) allowed us to create a cumulative body of knowledge on the interplay between IS value and user goals, because we can go beyond the pure identification of goals for an IS.

Their work elicited 27 user goals for the Australian version of eBay but we only used a subset of 13 goals in this study (see Table 2). The goals omitted in our study were either double entries in the hierarchy or were deemed not to be irrelevant to our effort. The omitted goals can be sorted into three groups (see Fig. 1). Group 1 included two goals that were not linked by a means-end chain path with any other goal in the hierarchy. Group 2 included six goals that were already represented in the hierarchy although not at the same level of detail. Details related to the product location, viz. ‘‘products for/from home’’ and ‘‘products for/from work or university’’. Group 3 included five goals that represent a special case, because a user must obtain these products in order to be able to add others to a collection. Thus, the five goals are only a special case of the buying/bidding goals and have been omitted. During our selection process, we also merged two goals ‘‘search for price information’’ and ‘‘search for product characteristics’’ into one goal ‘‘searching for products in regard of price and characteristics’’. Consequently, we felt that we had good reasons to use the set of 13 user goals. With 13 goals participants ‘only’ needed to answer 156 questions.

Participants were sought from different management IS courses at a major Australian university. To improve participation and obtain a high response rate, various steps were taken, including prenotification, endorsement of the study by the lecturer, handing out small non-financial tokens for participation, and ensuring privacy and anonymity. Student participants were suitable candidates because, they frequently use the Internet which gives them the necessary experience to participate in our study [29,32].

The questionnaire included two parts and a section to gather demographic data. In the first part, the value of the auction IS was measured using five items (measured on a 7-point Likert scale) taken from the utilitarian dimension of the HED/UT scale [36]. Because these items did not imply any goals a user might have with an IS, we saw them as goal-neutral and suitable for capturing the IS value. In the second part, data on user goals were collected as suggested by van Rekom and Wierenga. We first asked the importance of each of the 13 goals (1: very unimportant to 7: very important). Then, we determined the emergent structure of the means-end chains through a goal implication matrix (a square matrix with 13 means goals as rows and 13 end goals as columns). For each cell, participants were asked to indicate if a relationship exists between the means and the ends. For example, if the goal buying a product was seen as a means to the end goal enjoy using the product, then the participant would fill in YES; but if it was not perceived as a means, then the participant would fill in NO.

In survey research, common method bias is often a problem because it can inflate or affect the data gathered [8,27]. However, we think that our data were not impacted because we used known methods to remove potential bias: temporal, proximal, and methodological separation of the measurements. A temporal separation was achieved by introducing a time lag between the measurements. The two parts of the questionnaire were given at different times to the participants (part one was given at the start of a lecture and part two near to the end). The proximate separation was achieved by placing part one and part two on different sheets of paper. A methodological separation was achieved by using different response formats (Likert scale or binary) for each question. This attempted to diminish any recall of information from short-term memory. In addition, we reduced the risk of participants becoming tired and not sincerely answering the questions by minimizing the number of goals to 13. Furthermore, we told the participants a cover story (means-end chains as a decision tool for online marketing strategies) to distract them from linking the measurements of IS value to the goal means-end chains. Finally, participants were given clear instructions on how to work through the matrix, viz. to answer the questions column by column, to ensure they assessed the corresponding but converse means-end pairs separately from one another.

## 4. Data analysis and results

A total of 149 individuals participated in the survey; this included all students present on the days that data was collected (with a 100% response rate). The participants’ age varied from 17 to 42 with an average age of 20 years. Different nationalities were surveyed, the largest being Australian (42%), followed by Chinese (25%), Malaysian (7%), and others (26%) (e.g., German, Indian, Singaporean). Most participants had some form of university education, the most common being a partially or fully completed bachelor’s degree.

For the construct of IS value, the reliability of the scale as satisfactory (Cronbach a = 0.88), which is greater than the recommended minimum of 0.7. We also carried out an exploratory factor analysis of the five UT items (principal component analysis/ varimax rotation) and one single factor emerged. Descriptive statistics for IS value are: mean = 4.72; SD = 1.20; min = 1; max = 7.

The implication matrix included the 13 user goals as rows and columns. All participants filled in their beliefs about the means-end chain relations, and their answers were translated as agreement (cell value 1) or disagreement (cell value 0). Subsequently, the 149 individual matrices were combined into an aggregated implication matrix by averaging the cell values of the individual implication matrices. Some descriptive statistics for the aggregated implication matrix were: number of observations = 156; min = 0.094; max = 0.879; and the average value of the goal path (mean) = 3.94. The mean value determines the probability that any given path between two random goals was present (i.e., 39.4%).

In the first analysis stage, the emergent structure was determined. The decision whether to treat the model as a hierarchy or network depended on the number of mutual dyads. In an aggregated implication matrix any cell value > 0 for corresponding goals indicated mutual dyads. A cell value close to 1 indicated a high number of mutual dyads while a cell value close to 0 indicated fewer mutual dyads. As a further indicator of a network structure, the correlation between the numbers above the diagonal (i.e., p ! q) and below the diagonal (i.e., q ! p) in the implication matrix can be computed. In a hierarchy, each pair of two goals p and q would have a direction from p ! q and any direction from q ! p would be very unlikely. The hierarchical case suggested a negative correlation between the cells of p ! q and the cells of q ! p. This means that when, in the implication matrix, the triangle above the diagonal increased, the triangle below the diagonal decreased, or vice versa. A positive correlation suggested a nonhierarchical and thus, symmetric network structure, because both the triangles above and below decreased or increased together.

An initial visual inspection of the aggregated implication matrix in Table 2 suggested that the matrix was not strictly asymmetric. The calculation of Pearson correlation coefficient provided statistical support that mutual dyads existed. The correlation coefficient in our study was positive significant (0.824 with p = 0.01) supporting a symmetric goal network structure.

Next, we analyze the goal network using measures from socia network analysis, in particular degree and flow betweenness centrality. Degree centrality allowed us to gain an understanding of the immediate linkages a goal has with its direct neighbors. Thus, we could identify the goal that was most central in the local neighborhood. Flow betweenness centrality allowed us to consider all linkages in the goal network and thus provides us with information about goal centrality in relation to the entire graph.

Importance and centrality for the eBay user goals.

<table><tr><td colspan="6">Network structure data</td><td colspan="2">Goal importance data</td></tr><tr><td>User goals sorted by degree centrality</td><td>Out-degrees</td><td>In-degrees</td><td>Degree</td><td>User goals sorted by flow betweenness</td><td>Flow betweenness</td><td>User goals sorted by importance</td><td>Average importance</td></tr><tr><td>G1: Buying a product</td><td>5.1</td><td>6.6</td><td>11.7</td><td>G1: Buying a product</td><td>32.3</td><td>G3: Searching for a product in reg. of price and characteristic</td><td>5.7</td></tr><tr><td>G3: Searching for a product in reg. of price and characteristic</td><td>4.7</td><td>5.8</td><td>10.5</td><td>G6: Getting a product with the intention to give it away</td><td>14.5</td><td>G1: Buying a product</td><td>5.3</td></tr><tr><td>G2: Bidding for a product</td><td>4.2</td><td>5.7</td><td>9.8</td><td>G10: Enjoy giving away a product</td><td>12.8</td><td>G2: Bidding for a product</td><td>5.0</td></tr><tr><td>G4: Selling a product</td><td>4.5</td><td>5.0</td><td>9.6</td><td>G11: Benefit from giving away a product</td><td>11.8</td><td>G4: Selling a product</td><td>5.0</td></tr><tr><td>G10: Enjoy giving away a product</td><td>5.1</td><td>4.4</td><td>9.5</td><td>G12: Enjoy getting rid of (sell) a product</td><td>10.9</td><td>G11: Benefit from giving away a product</td><td>4.8</td></tr><tr><td>G6: Getting a product with the intention to give it away</td><td>4.6</td><td>4.9</td><td>9.4</td><td>G5: Getting a product with the intention to use it yourself</td><td>9.8</td><td>G10: Enjoy giving away a product</td><td>4.7</td></tr><tr><td>G11: Benefit from giving away a product</td><td>5.1</td><td>4.2</td><td>9.3</td><td>G13: Benefit from getting rid of a product</td><td>9.8</td><td>G7: Getting rid of (sell) a product</td><td>4.7</td></tr><tr><td>G7: Getting rid of (sell) a product</td><td>4.5</td><td>4.7</td><td>9.2</td><td>G3: Searching for a product in reg. of price and characteristic</td><td>7.5</td><td>G5: Getting a product with the intention to use it yourself</td><td>4.6</td></tr><tr><td>G13: Benefit from getting rid of a product</td><td>4.8</td><td>4.2</td><td>9.0</td><td>G8: Enjoy using a product</td><td>5.8</td><td>G12: Enjoy getting rid of (sell) a product</td><td>4.5</td></tr><tr><td>G12: Enjoy getting rid of (sell) a product</td><td>4.7</td><td>4.2</td><td>8.9</td><td>G4: Selling a product</td><td>5.1</td><td>G6: Getting a product with the intention to give it away</td><td>4.4</td></tr><tr><td>G8: Enjoy using a product</td><td>4.8</td><td>4.0</td><td>8.8</td><td>G7: Getting rid of (sell) a product</td><td>3.5</td><td>G9: Benefit from the usage</td><td>4.2</td></tr><tr><td>G5: Getting a product with the intention to use it yourself</td><td>4.5</td><td>4.2</td><td>8.7</td><td>G2: Bidding for a product</td><td>2.6</td><td>G13: Benefit from getting rid of a product</td><td>4.1</td></tr><tr><td>G9: Benefit from the usage</td><td>4.9</td><td>3.7</td><td>8.6</td><td>G9: Benefit from the usage</td><td>2.2</td><td>G8: Enjoy using a product</td><td>3.9</td></tr></table>

![](/api/attachments/P2CE2JYP/fulltext/images/7f5b1936103acf01d42431f6d87e978f4473e7103fe80b476f4a8ef689338b45.jpg)  
Fig. 2. Means-end chain network of user goals based on degree centrality for all participants.

We did not consider closeness centrality and betweenness centrality, because they measure the geodesic goal linkages, which assume that a user only creates means-end chains along the shortest path. Table 3 presents the results of degree centrality and flow betweenness centrality. We used UCINET to compute the calculation.

Based on degree centrality, the two most central goals were G1: buying a product followed by G3: searching for product in regard of price and characteristics. These goals were important in the local goal neighborhood. They are characterized by a high involvement in many means-end chains, either as a means goal or an end goal. G1 is also the important goal based on in-degrees. Regarding flow betweenness, the central goal was again G1 but the second central goal was G6: getting the product with the intention to give it away. The flow betweenness central goals are key goals because of their control over the flow within the goal network. If G1 or G6 were removed, the flow of the goal process and the entire goal effort could be interrupted.

The least degree central goals related to product usage, viz. G8, G5, and G9. Based on flow betweenness centrality, the three least central goals are G7, G2, and G9. These goals are less important due to their peripheral position in the network and because they are only loosely connected in the network.

To visualize the goal network, we used the software program NetDraw that can read UCINET system files. All network diagrams use spring embedding node repulsion and equal path length to position the goals graphically with the smallest path lengths close to one another but also to avoid goals that would be located very close together and thus, melting or merging into each other. Fig. 2 presents the goal network based on degree centrality of all participants. The size of the vertices indicates degree centrality values. For reasons of clarity and readability, we follow the approach by van Rekom and Wierenga, and show only those edges on which the majority (-50%) of the study participants agreed. Thus, we included only an arrow when the cell value in the aggregated implication matrix was greater than or equal to 0.50.

The questionnaire also assessed the importance of the 13 goals which can serve as an independent measure for its importance. As Table 3 shows, the more degree central goals were grouped at the top of the importance ranking while the least were grouped at the bottom. We therefore inferred that degree centrality expressed the importance of user goals for the auction system.

We further analyzed the data to look for differences in the goal structure with respect to the users’ IS value assessments. We divided the participants into groups of high and low IS value. High IS value was determined as one SD above the mean (5.92) and low as one SD below the mean (3.52). As a result, 23 participants were allocated into the high IS value group and 30 were placed in the low IS value group. These two groups were close to equal in size. The splitting resulted in the creation of two additional aggregated goal implication matrices for which we also calculated degree centrality and flow betweenness centrality (see Tables 4 and 5, and Fig. 3).

We first analyze the degree centrality results. For the high value group, the three most central goals were G1, G2, and G3 and the least central were G11, G12, and G9. For the low value group, the three most central goals were G1, G3, and G11 while the least central goals were G9, G8, and G5. For flow betweenness centrality results showed that the top central goal for the low value group and high value group was G1. Differences emerged for the other goals. For the high value group, the second flow betweenness central goal was G4, which is ranked on position 10 for the low value group and the allrespondents group. Another central goal for flow betweenness was the goal G3, which ranked as position 3 in the high value group and as position 2 in the low value group. The goals G9 and G2 were ranked lowest in flow betweenness centrality in the all participant group and the low value group. Goal G10, although highly ranked in the all respondents group, was only ranked at position 13 (last) in the high value group.

## 5. Discussion

## 5.1. User goal positions in a means-end chain network

Conceptualizing means-end chains as goal networks provided insight into user motivations toward technology. The analysis of degree and flow betweenness centrality revealed how frequently goals are interrelated. Our analysis underlined the importance of goals to a user.

![](/api/attachments/P2CE2JYP/fulltext/images/957dedd4b44905b0fd8c160eb798c50e83b7c40471f95c44fe9ebf66f4004393.jpg)  
Fig. 3. Means-end chain networks based on flow betweenness for the high group and low group in relation to their IS value assessments.

Splitting the users into groups with either high or low IS value provided other interesting findings. User with high value assessments considered the bidding to be the third most important goal, but for the low IS value group this goal was less important (the eighth in ranking). To cater for the low value user group, eBay offers its ‘‘buy it now’’ feature, however; eBay is known as an online auction system. Hence, the low IS value assessment might be the result of a cognitive comparison between eBay with an online shopping website such as amazon.com.

If we assume that persons use eBay to buy a product for a relative or friend, then G10 and G11 are important goals and may serve as entry points to the network; as the motivational starting point. This is particularly true for the low IS value group.

The goals G9 and G5 are positioned at the periphery of the network due to their low degree centrality. If a user wants to achieve these goals then eBay might not be the appropriate site for them. Furthermore, these goals are less important for users. The low importance rankings might indicate that the achievement of

G9 can be accomplished in ways that do not require technology support, for example buying products offline.

Flow betweenness centrality reflects the control of a goal over the process. The removal of a high betweenness centrality goal (its non-fulfillment) from a means-end path will disrupt the achievement process. Consequently, the IS should ensure achievement of goals with high flow betweenness centrality (i.e., G1, G3, G4) because of their mediating role.

The goal G1: buying a product controls has most control over the flow through the network. Hence, users expect from an online auction system that it enables them to obtain a product. If the activity is not possible or seen by the users as a difficult task, then the achievement of almost all goals is at risk. To support the achievement of the buying goal, the number of steps a user must undertake to place a bid or complete an auction should be kept to a minimum. Interestingly, for the high IS value group the second flow betweenness central goal is G4: selling a product which is ranked tenth for the low IS value group. This suggests that users who value eBay highly do not just purchase products but also sell products via the system.

## Table 4

Degree centrality results for all participants, high IS value group and low IS value group.

<table><tr><td colspan="2">All respondents (n = 149)</td><td colspan="2">High value assessment (n = 23)</td><td colspan="2">Low value assessment (n = 30)</td></tr><tr><td>User goals</td><td>Degree</td><td>User goals</td><td>Degree</td><td>User goals</td><td>Degree</td></tr><tr><td>G1: Buying a product</td><td>11.7</td><td>G1: Buying a product</td><td>12.4</td><td>G1: Buying a product</td><td>10.8</td></tr><tr><td>G3: Searching for a product in reg. of price and characteristic</td><td>10.5</td><td>G3: Searching for a product in reg. of price and characteristic</td><td>10.5</td><td>G3: Searching for a product in reg. of price and characteristic</td><td>10.8</td></tr><tr><td>G2: Bidding for a product</td><td>9.8</td><td>G2: Bidding for a product</td><td>10.3</td><td>G11: Benefit from giving away a product</td><td>10.4</td></tr><tr><td>G4: Selling a product</td><td>9.6</td><td>G6: Getting a product with the intention to give it away</td><td>9.8</td><td>G10: Enjoy giving away a product</td><td>10.1</td></tr><tr><td>G10: Enjoy giving away a product</td><td>9.5</td><td>G7: Getting rid of (sell) a product</td><td>9.7</td><td>G7: Getting rid of (sell) a product</td><td>9.7</td></tr><tr><td>G6: Getting a product with the intention to give it away</td><td>9.4</td><td>G4: Selling a product</td><td>9.0</td><td>G13: Benefit from getting rid of a product</td><td>9.6</td></tr><tr><td>G11: Benefit from giving away a product</td><td>9.3</td><td>G13: Benefit from getting rid of a product</td><td>8.8</td><td>G4: Selling a product</td><td>9.5</td></tr><tr><td>G7: Getting rid of (sell) a product</td><td>9.2</td><td>G10: Enjoy giving away a product</td><td>8.6</td><td>G2: Bidding for a product</td><td>9.5</td></tr><tr><td>G13: Benefit from getting rid of a product</td><td>9.0</td><td>G5: Getting a product with the intention to use it yourself</td><td>8.6</td><td>G6: Getting a product with the intention to give it away</td><td>9.4</td></tr><tr><td>G12: Enjoy getting rid of (sell) a product</td><td>8.9</td><td>G8: Enjoy using a product</td><td>8.5</td><td>G12: Enjoy getting rid of (sell) a product</td><td>9.4</td></tr><tr><td>G8: Enjoy using a product</td><td>8.8</td><td>G11: Benefit from giving away a product</td><td>8.5</td><td>G9: Benefit from the usage</td><td>8.6</td></tr><tr><td>G5: Getting a product with the intention to use it yourself</td><td>8.7</td><td>G12: Enjoy getting rid of (sell) a product</td><td>8.1</td><td>G8: Enjoy using a product</td><td>8.2</td></tr><tr><td>G9: Benefit from the usage</td><td>8.6</td><td>G9: Benefit from the usage</td><td>7.8</td><td>G5: Getting a product with the intention to use it yourself</td><td>8.2</td></tr></table>

Table 5  
Flow betweenness results for all participants, high IS value group and low IS value group.

<table><tr><td colspan="2">All respondents (n = 149)</td><td colspan="2">High value assessment (n = 23)</td><td colspan="2">Low value assessment (n = 30)</td></tr><tr><td>User goals</td><td>Flow Betweenness</td><td>User goals</td><td>Flow Betweenness</td><td>User goals</td><td>Flow Betweenness</td></tr><tr><td>G1: Buying a product</td><td>32.3</td><td>G1: Buying a product</td><td>34.5</td><td>G1: Buying a product</td><td>35.6</td></tr><tr><td>G6: Getting a product with the intention to give it away</td><td>14.5</td><td>G4: Selling a product</td><td>16.1</td><td>G3: Searching for a product in reg. of price and characteristic</td><td>17.6</td></tr><tr><td>G10: Enjoy giving away a product</td><td>12.8</td><td>G3: Searching for a product in reg. of price and characteristic</td><td>8.0</td><td>G6: Getting a product with the intention to give it away</td><td>15.5</td></tr><tr><td>G11: Benefit from giving away a product</td><td>11.8</td><td>G5: Getting a product with the intention to use it yourself</td><td>7.9</td><td>G7: Getting rid of (sell) a product</td><td>8.9</td></tr><tr><td>G12: Enjoy getting rid of (sell) a product</td><td>10.9</td><td>G8: Enjoy using a product</td><td>7.9</td><td>G5: Getting a product with the intention to use it yourself</td><td>8.3</td></tr><tr><td>G5: Getting a product with the intention to use it yourself</td><td>9.8</td><td>G2: Bidding for a product</td><td>5.0</td><td>G8: Enjoy using a product</td><td>8.3</td></tr><tr><td>G13: Benefit from getting rid of a product</td><td>9.8</td><td>G9: Benefit from the usage</td><td>2.6</td><td>G11: Benefit from giving away a product</td><td>7.9</td></tr><tr><td>G3: Searching for a product in reg. of price and characteristic</td><td>7.5</td><td>G6: Getting a product with the intention to give it away</td><td>1.9</td><td>G10: Enjoy giving away a product</td><td>4.4</td></tr><tr><td>G8: Enjoy using a product</td><td>5.8</td><td>G11: Benefit from giving away a product</td><td>1.9</td><td>G13: Benefit from getting rid of a product</td><td>3.2</td></tr><tr><td>G4: Selling a product</td><td>5.1</td><td>G7: Getting rid of (sell) a product</td><td>1.5</td><td>G4: Selling a product</td><td>3.0</td></tr><tr><td>G7: Getting rid of (sell) a product</td><td>3.5</td><td>G12: Enjoy getting rid of (sell) a product</td><td>1.5</td><td>G12: Enjoy getting rid of (sell) a product</td><td>3.0</td></tr><tr><td>G2: Bidding for a product</td><td>2.6</td><td>G13: Benefit from getting rid of a product</td><td>1.5</td><td>G9: Benefit from the usage</td><td>1.1</td></tr><tr><td>G9: Benefit from the usage</td><td>2.2</td><td>G10: Enjoy giving away a product</td><td>1.0</td><td>G2: Bidding for a product</td><td>0.8</td></tr></table>

## 5.2. Contributions to theory and implications for practice

We addressed an important theoretical gap in the literature on the impact of structuring user goal means-end chains by investigating differences in the goal structures between users who assessed the value of the IS as high versus low. First, our work contributes by suggesting goal networks as a better representation of means-end chains. While traditionally, means-end chains were structured as hierarchies, we showed that the network perspective provides new insights into the user’s goal striving process. For example, prior research refers to eBay as the number one auction system in the US, if not worldwide [17]. Thus, a means-end chain hierarchy, would include goals such as buying, selling, and bidding, albeit at the lowest layer. This implies that the bidding goal is as important for a user as any of the other lower layered goals. Yet, our findings showed that the bidding goal was not an important goal for many users. In fact, it was only seen as important for users who attribute high value to the IS. The differences in importance of the bidding goal would not have been identified if the user goals had been visualized as a hierarchy. Consequently, our study provides empirical support for the benefits and insights that can be gained when means-end chains are structured as networks. Second, our findings showed that users create cognitive paths of interlinked goals when using an IS; however, goals are not equally important to all users and thus the IS has different perceived values to its users. A positive attitude alone is not a sufficient condition for a behavioral intention to occur; a user must desire to achieve the goal. Third, we added to our understanding of online auction systems by identifying the various usage scenarios that a user may experience when using eBay. The goals in our study were elicited for eBay by determining their importance in usage scenario in which users value the IS differently. Thus, our study offers additional insights into e-commerce systems.

This research has several implications for practice. First, operators can use the findings to improve their service offerings and align them closer to users’ needs. Thus operators may use our results to optimize their marketing campaigns by emphasizing goals and IS features that are linked to high IS value evaluations. Furthermore, the operator can use the goal networks to measure customer satisfaction with the IS by determining what goals were pursued and the extent to which they were fulfilled. In this way, operators gain nuanced insights into their current user base. In addition, operators may utilize our findings to introduce the IS to novice users. Novice users would benefit from detailed introductions (e.g., videos, usage description) that explain the features provided by the IS and how to use them to achieve different goals. Finally, findings of the study can be used during the design and development process of other online systems. Highly central goals, which might be overlooked in a hierarchical means-end structure, may serve as the foundation for defining user requirements.

## 5.3. Limitations

As with any empirical research, our study had limitations. One was the use of only a selection of user goals elicited in prior research for online auctions and there may be additional goals that are relevant for users. We relied on the results of Zumpe and van der Heijden. We made every effort to understand how they identified the user goals and believe that good practice of the research technique was applied.

A second limitation was a question of the generalizability of our findings. Although means-end chains emerging as networks is a general finding and thus, applies to settings other than online auction systems, the goals themselves are tied to eBay. For goals identified in the other means-end chain studies, the networks and centrality results may be different.

A third limitation referred to the data collection. We took care to reduce any bias due to temporal, proximal, and methodological separation of the study variables. However, data about means-end chains can be seen as single-items indices of a user’s perception of a goal, although prior research has suggested that a single-item measure is as good as multi-item measures in its predictive validity and reliability under conditions of object clarity [6,28].

## 6. Conclusions

In our paper, we have proposed that modeling means-end chains of user goals as a network better explains the goal striving process and is better at revealing the important motivational drivers of users. Analysis of the goal networks showed variations in IS value because people had differences in opinion of the goal’s importance. Users who perceived the IS of high value want to use eBay to buy, sell, and bid for products whereas users with low IS value seem to avoid using eBay because of uncertain price bidding. The research sought to address an important theoretical gap in our understanding of the multi-facet nature of user goals and their structures. The findings can be used to provide better designs and market auction systems to users and allow novice users to understand their goals in using a system.

## Acknowledgement

The author would like to thank Sue Brown, Sabine Madsen, and Ray Zammuto for their valuable comments and helpful feedback on earlier versions of the manuscript. In addition, the author would like to thank Sam Ferguson for his comprehensive editing of the manuscript.

## Appendix A. Questionnaire

## Information System Value

Would you agree or disagree that for you eBay is: (7-point Likert scale, ranging from [1: extremely disagree] to [7: extremely agree])

1. Effective

2. Helpful

3. Functional

4. Necessary

5. Practical

## Goal Importance Rating

How important are the goals below [the 13 user goals have been presented in a Table] for you?

(7-point Likert scale, ranging from 1: very unimportant to 7: very important)

## Means – End Chain Relations

Indicate in the matrix below for each goal in the top row, if it is a means for each goal in the left column. Write your answer in each cell.

(Dichotomous variable)

## References

[1] M.K.T. Ahuja, Jason Bennett moving beyond intentions and toward the theory of trying: effects of work environment and gender on post-adoption information technology use, MIS Quarterly 29 (3), 2005, pp. 427–459.

[2] P. Aschmoneit, M. Heitmann, Customer centred community application design, The International Journal on Media Management 4 (1), 2002, pp. 13–21.

[3] J.T. Austin, J.B. Vancouver, Goal constructs in psychology: Structure, process, and content, Psychological Bulletin 120 (3), 1996, pp. 338–375.

[4] R. Bagozzi, G. Henderson, P. Dabholkar, D. Iacobucci, Network analysis of hierarchical cognitive connections between concrete and abstract goals, in: D. Iacobucci (Ed.), Networks in Marketing, Sage, Thousand Oaks, 1996, pp. 367–383.

[5] R.P. Bagozzi, The legacy of the technology acceptance model and a proposal for a paradigm shift, Journal of the Association for Information Systems 8 (4), 2007, pp. 244-254

[6] L. Bergkvist, J.R. Rossiter, The predictive validity of multiple-item versus singleitem measures of the same constructs, Journal of Marketing Research 44 (2), 2007, pp. 175–184.

[7] S.P. Borgatti, Centrality and network flow, Social Networks 27 (1), 2005, pp. 55– 71.

[8] A. Burton-Jones, Minimizing method bias through programmatic research, MIS Quarterly 33 (3), 2009, pp. 445–471.

[9] G. Chartrand, L. Lesniak, Graphs & Digraphs, Chapman & Hall/CRC, Boca Raton, 2005.

[10] C.M. Chiu, Applying means-end chain theory to eliciting system requirements and understanding users perceptual orientations Information & Management 42 (3) 2005, pp. 455–468.

[11] F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS Quarterly 13 (3), 1989, pp. 319–340.

[12] F.D. Davis, R.P. Bagozzi, P.R. Warshaw, User acceptance of computer technology: A comparison of two theoretical models, Management Science 35 (8), 1989, pp. 982-1003

[13] R.P. DeShon, J.Z. Gillespie, A motivated action theory account of goal orientation, Journal of, Applied Psychology 90 (6), 2005, pp. 1096–1127.

[14] L.C. Freeman, Centrality in social networks: Conceptual clarification, Social Networks 1 (3), 1979, pp. 215–239.

[15] J. Gutman, A means-end chain model based on consumer categorization processes, Journal of Marketing 46 (2), 1982, pp. 60–72.

[16] R.A. Hanneman, M. Riddle, Introduction to Social Network Methods, University of California, Riverside, Riverside, CA, 2005.

[17] K. Hasker, R. Sickles, eBay in the economic literature: analysis of an auction marketplace, Review of Industrial Organization 37 (1), 2010, pp. 3–42.

[18] M.B. Houston, B.A. Walker, Self-relevance and purchase goals: Mapping a consumer decision, Journal of the Academy of Marketing Science 24 (3), 1996, pp. 232–245.

[19] D. Knoke, S. Yang, Social Network Analysis, Sage Thousand Oaks, CA, 2008.

[20] T. Kuisma, T. Laukkanen, M. Hiltunen, Mapping the reasons for resistance to Internet banking: a means-end approach, International Journal of Information Management 27 (2), 2007, pp. 75–85.

[21] E.A. Locke, G.P. Latham, Building a practically useful theory of goal setting and task motivation: a 35-year Odyssey, American Psychologist 57 (9), 2002, pp. 705–717.

[22] E.A. Locke, G.P. Latham, New directions in goal-setting theory, Current Directions in Psychological Science 15 (5), 2006, pp. 265–268.

[23] F. Nah, K. Siau, H. Sheng, The value of mobile application: a utility company study, Communications of the ACM 48 (2), 2005, pp. 85–90.

[24] A. Ortiz de Guinea, M.L. Markus, Why break the habit of a lifetime? Rethinking the roles of intention, habit, and emotion in continuing information technology use MIS Ouarterly 33 (3).2009 pp. 433-444

[25] J.M. Phillips, T.J. Reynolds, A hard look at hard laddering, Qualitative Market Research: An International Journal 12 (1), 2009, pp. 83–99.

[26] R. Pieters, H. Baumgartner, D. Allen, A means-end chain approach to consumer goal structures, International Journal of Research in Marketing 12 (3), 1995, pp. 227–244.

[27] P.M. Podsakoff, S.B. MacKenzie, J.Y. Lee, N.P. Podsakoff, Common method biases in behavioral research: a critical review of the literature and recommended remedies, Journal of Applied Psychology 88 (5), 2003, pp. 879–903.

[28] J.R. Rossiter, The C-OAR-SE procedure for scale development in marketing, International Journal of Research in Marketing 19 (4), 2002, pp. 305–335.

[29] B.C. Su, Consumer E-Tailer choice strategies at on-line shopping comparison sites, International Journal of Electronic Commerce 11 (3), 2007, pp. 135–159

[30] D.P. Subramony, Why users choose particular web sites over others: introducing a means-end approach to human computer interaction, Journal of Electroni Commerce Research 3 (3), 2002, pp. 144–161.

[31] P.-C. Sun, G. Hsing Kenneth, Finger, Critical functionalities of a successful elearning system—an analysis from instructors’ cognitive structure toward system usage, Decision Support Systems 48 (1), 2009, pp. 293–302.

[32] W. Swinyard, S. Smith, Why people (don’t) shop online: study of the internet consumer, Psychology and Marketing 20 (7), 2003, pp. 567–597.

[33] T.A. Sykes, V. Venkatesh, S. Gosain, Model of acceptance with peer support: a social network perspective to understand employees, MIS Quarterly 33 (2), 2009, pp. 371–393.

[34] J. Van Rekom, B. Wierenga, On the hierarchical nature of means-end relationships in laddering data, Journal of Business Research 60 (4), 2007, pp. 401–410.

[35] R. Vidgen, S. Henneberg, P. Naude, What sort of community is the European Conference on Information Systems?. A social network analysis 1993–2005 European Journal of Information Systems 16 (1), 2007, pp. 5–19.

[36] K. Voss, E. Spangenberg, B. Grohmann, Measuring the hedonic and utilitarian dimensions of consumer attitude, Journal of Marketing Research 40 (3), 2003, pp. 310–320.

[37] S. Wasserman, K. Faust, Social network analysis: Methods and applications, Cambridge University Press, Cambridge, UK, 1994.

[38] D.B. West, Introduction to graph theory, Prentice Hall, Upper Saddle River, NJ, 2001.

[39] B. Zemljic, V. Hlebec, Reliability of measures of centrality and prominence, Socia Networks 27 (1). 2005, pp. 73–88

[40] S. Zumpe, H. van der Heijden, On the use of variable user goals to measure perceived usefulness, in: Proceedings of the European Conference on Information Systems, St Gallen, Switzerland, 2007.

![](/api/attachments/P2CE2JYP/fulltext/images/242d19e59b4b17bf387d25a663b195d67205cbd2ae8276ef8fc76de40c4e6bd3.jpg)  
Sabine Matook. Ph.D. is a senior lecturer in Information Systems at the UO Business School. University of Queensland. She received her doctoral degree from the Technische Universita¨t (TU) Dresden, Germany. Her research interests are on the IT artifact and in the areas of goal-related IS use, electronic marketplaces and social media, and agile IS development. Her work has appeared in Decision Support Systems, European Journal of Information Systems, Journal of Strategic Information Systems, and the International Journal of Operations & Production Management. Dr. Matook has presented research papers at a variety of conferences, including the International Conference on Information Systems.
