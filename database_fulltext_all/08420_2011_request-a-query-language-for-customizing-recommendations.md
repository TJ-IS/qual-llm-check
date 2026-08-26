---
otero_id: 8420
otero_key: "P5479VD3"
title: "REQUEST: A Query Language for Customizing Recommendations"
authors: "Gediminas Adomavicius; Alexander Tuzhilin; Rong Zheng"
year: "2011"
journal: "Information Systems Research"
doi: "10.1287/isre.1100.0274"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## 6SR

![](/api/attachments/P5479VD3/fulltext/images/e4b3b93bfa461f0f7084a9469aa6afcd152702e26561cebc16f910f8b2c6a674.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# REQUEST: A Query Language for Customizing Recommendations

Gediminas Adomavicius, Alexander Tuzhilin, Rong Zheng,

To cite this article:

Gediminas Adomavicius, Alexander Tuzhilin, Rong Zheng, (2011) REQUEST: A Query Language for Customizing Recommendations. Information Systems Research 22(1):99-117. http://dx.doi.org/10.1287/isre.1100.0274

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2011, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/P5479VD3/fulltext/images/471d8d4322a29de7415e270c44355a53a22b3f845026dd9f31c9f405aa00d7b4.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# REQUEST: A Query Language for Customizing Recommendations

Gediminas Adomavicius

Department of Information and Decision Sciences, Carlson School of Management, University of Minnesota, Minneapolis, Minnesota 55455, gedas@umn.edu

Alexander Tuzhilin

Information, Operations & Management Sciences Department, Stern School of Business, New York University, New York, New York 10012, atuzhili@stern.nyu.edu

Rong Zheng

Department of Information Systems, Business Statistics and Operations Management, Business School, Hong Kong University of Science and Technology, Kowloon, Hong Kong, rzheng@ust.hk

nitially popularized by Amazon.com, recommendation technologies have become widespread over the past Iseveral years. However, the types of recommendations available to the users in these recommender systems are typically determined by the vendor and therefore are not flexible. In this paper, we address this problem by presenting the recommendation query language REQUEST that allows users to customize recommendations by formulating them in the ways satisfying personalized needs of the users. REQUEST is based on the multidimensional model of recommender systems that supports additional contextual dimensions besides traditional User and Item dimensions and also OLAP-type aggregation and filtering capabilities. This paper also presents the recommendation algebra RA, shows how REQUEST recommendations can be mapped into this algebra, and analyzes the expressive power of the query language and the algebra. This paper also shows how users can customize their recommendations using REQUEST queries through a series of examples.

Key words: personalization; recommender systems; recommendation query language; multidimensional recommendations; contextual recommendations; recommendation algebra

History: Sumit Sarkar, Senior Editor; Debabrata Dey, Associate Editor. This paper was received on June 4, 2006, and was with the authors 24 months for revisions. Published online in Articles in Advance March 1, 2010.

## 1. Introduction

Recommender systems represent an important class of personalization technologies that help users to deal with information overload in e-commerce and numerous other applications. There has been much work done in the area of recommender systems over the past 15 years since the introduction of the first papers on the subject (Hill et al. 1995, Resnick et al. 1994, Shardanand and Maes 1995), especially after these technologies were popularized by Amazon and Netflix, as well as after the establishment of the \$1,000,000 Netflix Prize competition that attracted more than 45,000 contestants from 180 countries (Bennet and Lanning 2007). A survey of the rapidly growing field of recommender systems can be found in Adomavicius and Tuzhilin (2005b).

Most of the work in recommender systems focuses on a two-dimensional paradigm of recommending items to users or users to items (e.g., books to customers or customers for books). Although there are different types of approaches to deriving recommendations, including the ranking (Cohen et al. 1999) and market basket analysis based (Mild and Reutterer 2001), the majority of the academic work in recommender systems and implementations of commercial systems, including Amazon and Netflix, focuses on the rating-based approach (Adomavicius and Tuzhilin 2005b), where recommendations use explicit or implicit ratings provided by the end-users.

Rating-based approaches are usually classified into content-based, collaborative, and hybrid (Balabanovic and Shoham 1997). In content-based recommendation methods, rating R-u i of item i for user u is typically estimated based on the ratings R-u i- assigned by the same user u to other items i- that are “similar” to item i in terms of their content. For example, to recommend movies to user u, the content-based approach tries to understand user preferences by analyzing commonalities among the content of the movies user u has rated highly before. Then, only the movies that have a high degree of similarity with customer’s past preferences are recommended.

Collaborative (or collaborative filtering) recommender systems try to predict rating R-u i of item i for user u based on how other “similar” users upreviously rated item i. Here, “user similarity” is defined in terms of the distance between the ratings users u and u- assigned to the items that both of them rated, the most popular types of distance metrics being correlation- and cosine-based measures between two rating vectors (Adomavicius and Tuzhilin 2005b). Then, collaborative filtering methods recommend those items to the user that she has not rated yet and that were highly rated by similar users.

Content and collaborative methods can be combined into a hybrid approach in several different ways (Balabanovic and Shoham 1997, Burke 2007). One popular way to combine them is by learning and maintaining user profiles based on the content analysis of the items preferred by the users, and then directly comparing the resulting profiles to determine similar users to make collaborative recommendations. Other types of hybrid methods are also possible and are described in Adomavicius and Tuzhilin (2005b) and Burke (2007).

Although the traditional two-dimensional user/ item paradigm described above is suitable for some applications, such as recommending books and music CDs, it is significantly less suitable for the “contextrich” applications, such as traveling or shopping applications. For example, when recommending vacations to travelers, one would likely recommend a different vacation to a customer in the winter than in the summer, i.e., the time-of-travel context is clearly important when making recommendations. Similarly, when recommending groceries, a “smart” shopping cart (Wade 2003) needs to take into account not only information about products and customers, but also such information as shopping date/time, store, who accompanies the primary shopper, products already placed into the shopping cart, and its location in the store. Clearly, the two-dimensional paradigm of classical recommender systems is less suitable for these applications.

To provide better recommendations in such contextually rich applications, one may need to consider other dimensions besides item and user. For example, when a movie recommendation provider (such as Netflix) recommends movies, it may also want to consider such additional dimensions as time when the movie was seen, company in which the movie was seen (e.g., alone, with friends, parents, etc.), and place in which it was seen (e.g., in the theater or at home). A completely different movie may be recommended by a movie recommendation provider to a student when he wants to see it on a Saturday night with his girlfriend in a movie theater than when he wants to see it on Thursday evening with his parents at home.

In Adomavicius et al. (2005) and Adomavicius and Tuzhilin (2001), we proposed a new multidimensional approach to recommender systems where we incorporated multiple dimensions and the OLAP-based cubes of ratings into the recommendation model. To estimate missing ratings in multidimensional cubes, we proposed the reduction-based method in Adomavicius et al. (2005) and the heuristic-based and model-based methods in Adomavicius and Tuzhilin (2005a).

However, the multidimensional approach described in Adomavicius et al. (2005) and the classical twodimensional recommendation methods have one significant limitation in common. These methods are hard wired by the developers into the recommender systems, are inflexible and limited in their expressiveness, and therefore neglect some possible needs of the users. For example, a typical recommender system would recommend the top k items to a user, or the best k users for a product. This situation is quite limited, especially in multidimensional settings, where the number of possible recommendations increases significantly with the number of dimensions (Adomavicius and Tuzhilin 2001). Therefore, there is a need to empower end-users and other stakeholders by providing them with the tools for expressing recommendations that are of interest to them (Adomavicius and Tuzhilin 2001, 2005b; Koutrika et al. 2008). For example, Jane Doe may need a recommendation for the best two dates to go on vacation to Jamaica with her boyfriend. Also, Netflix or an on-demand movie service, such as provided by the Time Warner Cable, can envision a Web-based interface to a multidimensional cube of ratings that lets the users express the recommendations that are of interest to them or automatically tailors recommendations based on a given context, such as the time of day or the day of week. For example, a certain user (e.g., Tom) may seek recommendations for him and his girlfriend of top three movies and the best times to see them over the weekend, and he enters this request into the recommender system via the Web-based interface. Such query-based recommendation applications are not limited to on-demand movies, but are relevant to a broad range of recommendation applications, including retail, financial, travel, and other applications. Furthermore, we believe that flexible recommendation capabilities would be appealing to a variety of different users, and not just to the end-users who are direct recipients of recommendations. For example, such functionality would be useful to the analysts of a company providing recommendation services, who may want to take advantage of all the knowledge that their recommender system holds and analyze it from a variety of different perspectives (“show me the top two movie genres for each user age bracket,” etc.). Alternatively, an agent in a call center can use such a system to recommend the best plans and services to the customers of a telecommunications company.

One tool for expressing such requests is a recommendation language that is similar to how database users use query languages to retrieve information from databases. In fact, one may try to use the popular database query language SQL for this purpose, and the above-mentioned recommendation for Tom and his girlfriend can be specified in SQL as

SELECT R.MovieId, R.TimeId, R.UserId,

R.CompanionId, AVG(R.PersonalRating)

FROM MovieRecommender R, User U, Time T, Companion C

WHERE R.UserId U.UserId AND

R.TimeId T.TimeId AND

R.CompanionId <sub>=</sub> C.CompanionId AND

U.Name “Tom” AND

T.TimeOfWeek “weekend” AND

C.Type <sub>=</sub> “Girlfriend”

GROUP BY R.MovieId, R.TimeId, R.UserId, R.CompanionId

where User and Companion are the relations storing information about customers and different types of companions, MovieRecommender is the ratings table, and Time is the temporal dimension table. Although “doable,” this SQL query and, more generally, SQL at large would have the following problems when used for recommendation purposes. First, notice that SQL does not exactly provide the requested recommendation: it returns the list of tuples (movies, times to see them, users, etc.), but does not specify what is recommended to whom and does not provide the top three recommended movie/time pairs. More generally, as it will be shown in this paper, recommendations are not really queries according to the standard meaning of this term because, generally, recommendations represent very idiosyncratic outputs that cannot be expressed in SQL. Second, SQL is a comprehensive, general-purpose database query language, and therefore many of the possible SQL queries do not represent recommendations. Therefore, to help the end-user formulate recommendations correctly and meaningfully, one may want to impose elaborate constraints on SQL to be able to restrict the language for the recommendation task. However, the development of a simple, elegant, and intuitive system of such constraints for SQL constitutes a very hard problem. A better alternative would be to introduce a language that is directly defined on top of the “native” multidimensional recommendation model. Third, the above SQL query is fairly cumbersome: it constitutes a join of four relational tables, has six conditions in the WHERE clause, has the GROUP BY statement and the aggregation function AVG. Clearly, there should be a better and more intuitive way to express this simple type of recommendation, and this observation served as a direct motivation for developing a special-purpose recommendation language. This necessity to replace cumbersome SQL queries with more elegant and intuitive formulations grows substantially for the significantly more complex recommendations, such as the ones that will be presented in §3. Fourth, this cumbersomeness may have not only a cognitive effect on the users writing queries, but could possibly also affect query performance in some cases, because processing multiple join queries can be a very timeconsuming operation. In summary, the above issues can be attributed to the task and model mismatch. SQL is a general-purpose query language, which makes it a less intuitive and less useful tool for users in the “vertical” application domain of recommender systems, where SQL may not have some specialized capabilities important for recommender systems. Also, SQL is based on the relational data model, and multidimensional recommendations on the multidimensional model (Adomavicius et al. 2005) would need to be mapped into the relational model to support SQL queries, which leads to various translation problems. To avoid these issues, it is advantageous to develop a specialized (vertical) query language based on the idiosyncratic characteristics of the domain of recommender systems that supports the multidimensional recommendation model and has the constructs, which are directly suited for recommendation applications.

In this paper, we follow this approach and present a new recommendation query language, REQUEST,<sup>1</sup> that allows its users to express in a flexible manner a broad range of recommendations that are tailored to their own individual needs, and therefore more accurately reflect their interests. For example, the earlier recommendation for Tom can be expressed in REQUEST as

RECOMMEND Movie, Time TO User, Companion

USING MovieRecommender

RESTRICT User.Name “Tom” AND

Time.TimeOfWeek “weekend” AND

Companion.Type <sub>=</sub> “Girlfriend”

BASED ON PersonalRating

SHOW TOP 3

where MovieRecommender is a five-dimensional cube of ratings having dimensions–User, Movie, Time,

Companion, and Theater; also, PersonalRating represents the ratings measure for the cube.

The above REQUEST query is based on the OLAP paradigm (Chaudhuri and Dayal 1997, Kimball 1996), which is a natural choice for querying multidimensional recommender systems, because the data model of REQUEST matches the multidimensional data model of the ratings cube. Besides REQUEST, we also present a multidimensional recommendation algebra RA that is used for defining certain “core” parts of REQUEST queries. We also describe how these core REQUEST queries can be processed by mapping them into this algebra.

This paper makes the following contributions. It proposes language REQUEST for expressing flexible user-driven recommendations and presents its syntax and semantics. It also presents recommendation algebra RA, which complements a formal definition of REQUEST. We also show how the core REQUEST queries can be mapped into RA, thus providing a way to process these queries, and compare the expressive power of REQUEST and RA.

## 2. Background: Multidimensional Recommender Systems

Taking into account some of the conventions for defining OLAP cubes (Thomas and Datta 2001), we define a multidimensional ratings cube as a tuple (D, $M , H , E , L )$ as follows.

Dimensions (D). $D = \{ d _ { 1 } , d _ { 2 } , \dots , d _ { n } \}$ is a set of n dimensions, where each $d _ { i }$ is a dimension name. For example, in addition to the standard User and Movie dimensions of the traditional movie recommender systems, such as MovieLens (Miller et al. 2003), we consider other contextual dimensions (Adomavicius et al. 2005, Adomavicius and Tuzhilin 2001), such as Time, Theater, and Companion, $\mathbf { i . e . , } D =$ {User, Movie, Time, Theater, Companion}.

Attribute Hierarchies (H). Each dimension $d _ { i }$ is represented by a set of attributes $A _ { i } = \{ a _ { i 1 } , \ldots , a _ { i t } \}$ where each $a _ { i j }$ is an attribute name; $\mathrm { e . g . } , A _ { \mathrm { t i m e } } = \{ \mathrm { D a t e , }$ DayOfWeek, TimeOfWeek, Month, Quarter, Year}. The domain of attribute x of dimension d is denoted as dom(dx, e.g., dom(Time.DayOfWeek) {Mon, Tue, Wed, Thu,Fri, Sat, Sun} and dom(Time.TimeOfWeek) {weekday, weekend}.

The multidimensional recommendation model allows for OLAP-based aggregation hierarchies (Adomavicius et al. 2005, Adomavicius and Tuzhilin 2001) that help aggregate ratings according to the methods described in Adomavicius et al. (2005). In particular, attributes $A _ { i }$ of dimension $d _ { i }$ form a directed acyclic graph (i.e., a hierarchy) $H _ { i } = ( A _ { i } , E _ { i } )$ with set of nodes $A _ { i } \ ( \mathrm { i . e . } $ each node corresponds to an attribute) and set of edges $E _ { i } .$ . There exists a directed edge in $H _ { i }$ from attribute $x \in A _ { i }$ to attribute $y \in A _ { i }$ if and only if every value of x uniquely determines the value of $y , \mathrm { i . e . , }$ if attribute $y$ is functionally dependent on attribute $x .$ . Such an edge will be denoted $( x , y )$ or $x  y$ . We will assume that $H _ { i }$ has a single root node, $R o o t ( H _ { i } )$ , which we will call the key dimension attribute, consistent with the standard database terminology. Let $H = \{ H _ { 1 } , \ldots , H _ { n } \}$

Given hierarchy $H _ { i }$ and attribute $d _ { i } . x \in A _ { i } ,$ we define $S u b G r a p h ( \dot { H } _ { i } , d _ { i } . x )$ to be a subgraph of $H _ { i }$ rooted at $d _ { i } . x , \mathrm { i . e . }$ , it defines the graph containing all the nodes and edges reachable from $d _ { i } . x .$

Elements (E). Each dimension $d _ { i }$ in a cube is represented by a set of elements $E _ { i }$ . For instance, dimension Movie in our example is represented by all the movies available for the users to rate. For simplicity and without loss of generality, we use the domain of the key dimension attribute to represent the set of elements of $d _ { i } , \mathrm { i . e . , } E _ { i } : = d o m ( R o o t ( \bar { H _ { i } } ) )$ . An example of the elements’ set for the User dimension would be a set of all user IDs available in the data. Let $E = \{ E _ { 1 } , \ldots , E _ { n } \}$

Measures (M). $M = \{ m _ { 1 } , m _ { 2 } , \dots , m _ { k } \}$ represents a set of measures, where each $m _ { i }$ is a different type of a rating from domain dom(m ). The measures can either be numeric or Boolean. A numeric measure usually represents a discrete finite ordered value, $\mathrm { e . g . , a }$ movie rating on the scale of $\{ 1 , \ldots , N \}$ . A Boolean measure can be used to represent a “status $\mathrm { { f l a g ^ { \prime \prime } } }$ denoting the state of a rating or its specific characteristic, e.g., indicating whether a given movie has been seen by a given user.

Example 1. Consider the application for recommending movies to users that has the following dimensions, each dimension defined by the attributes specified in parentheses:

(1) Movie: the set of all the movies that can be recommended; it is defined as Movie(MovieID, Title, Length, ReleaseYear, Director, Genre).

(2) User: the people to whom movies are recommended; it is defined as User(UserID, Name, Address, Age, Gender, Profession).

(3) Theater: the movie theaters showing the movies; it is defined as Theater(TheaterID, Name, Address, Capacity, City, State, Country).

(4) Time: the time when the movie can be or has been seen; it is defined as Time(Date, DayOfWeek, TimeOfWeek, Month, Quarter, Year).

(5) Companion: represents a person or a group of persons with whom one can see the movie. It is defined as Companion(companionType), where attribute companionType has values “alone,” “friends,” “girlfriend/boyfriend,” “family,” “co-workers,” and “others.”

We also use three rating measures in this example: PublicRating, a numeric measure specifying how much the general public liked the movie; PersonalRating, a numeric measure specifying how much a particular person liked or is predicted to like the movie in the settings specified by the Time, Theater, and Companion dimensions; and Consumed, a Boolean measure specifying whether or not a given user has actually seen a given movie in a given context. The PersonalRating assigned to a movie by a person depends on where and how the movie has been seen, with whom, and at what time. Finally, we consider the following aggregation hierarchies: Movie: MovieID Genre; User: UserID <sub>→</sub> Age, UserID <sub>→</sub> Gender, UserID <sub>→</sub> Profession; Theater: TheaterID <sub>→</sub> City State Country; Time: Date DayOfWeek TimeOfWeek, Date Month Quarter Year. <sup></sup>

Cube Cells (L). Each cube is a partially defined rating function R from an n-dimensional space of $E _ { 1 } \times \cdots \times E _ { n }$ to a k-dimensional space of measures, i.e., R $E _ { 1 } \times \cdots \times E _ { n } \to d o m ( m _ { 1 } ) \times \cdots \times d o m ( m _ { k } )$ . Alternatively, a cube can be perceived as a set of cells $L ,$ each cell l <sub>∈</sub> L consisting of the tuple -address content, i.e., l -address content, where addres $s = ( \alpha _ { 1 } , \ldots , \alpha _ { n } ) , \alpha _ { i } \in$ $E _ { i } ,$ and $c o n t e n t = ( \beta _ { 1 } , \ldots , \beta _ { k } ) , \ \beta _ { i } \in d o m ( m _ { i } )$ . Because the mapping R is partial, content can also have value NULL for some cells. We also use the notation Laddress content to refer to a specific cell, and Laddressm to refer to a specific measure within a cell. Furthermore, the ratings $R ( \alpha _ { 1 } , \ldots , \alpha _ { n } )$ of the recommendation space $S = E _ { 1 } \times E _ { 2 } \times \cdot \cdot \cdot \times E _ { n }$ are either explicitly provided by the users or are implicitly inferred by the system as described below. For example, R(Aviator, Jane, theater5, 2/19/2005, boyfriend) <sub>=</sub> (6, 8, True) means that Jane gave rating 6 (i.e., PersonalRating 6) to Aviator that she actually saw (i.e., Consumed True) with her boyfriend on February 19, 2005, in movie theater 5, but the general public gave the movie the rating of 8 (i.e., PublicRating 8).

Given these preliminaries, the recommendation problem is defined as follows. First, the system needs to estimate the unknown ratings and make the rating function R total (Adomavicius et al. 2005). Second, to make a recommendation, one needs to select certain nonoverlapping “what” dimensions $d _ { i 1 } , \ldots , d _ { i k }$ (k < n) and certain “for whom” dimensions $d _ { j 1 } , \ldots , d _ { j l }$ (l < n), and, accordingly, recommend for each tuple $( \alpha _ { j 1 } , \dots , \alpha _ { j l } ) \ \in \ E _ { j 1 } \ \times \ \cdots \ \times \ E _ { j l }$ tuple $( \alpha _ { i 1 } , \ldots , \alpha _ { i k } ) \in$ $E _ { i 1 } ^ { \dot { \mathbf { \alpha } } } \times \cdots \times E _ { i k }$ maximizing the rating $R ( \alpha _ { 1 } , \ldots , \alpha _ { n } )$ across all the tuples $\left( \alpha _ { 1 } , \ldots , \alpha _ { n } \right)$ coinciding with $( \alpha _ { j 1 } , \ldots , \alpha _ { j l } ) \in E _ { j 1 } \times \cdots \times E _ { j l }$ on corresponding dimensions $d _ { j 1 } , \dotsc , d _ { j l }$

Because the rating cube is only partially filled, it is important to estimate the unspecified ratings for recommendation purposes. This multidimensional rating estimation problem is addressed in Adomavicius et al. (2005), where the reduction-based method of estimating unknown ratings in terms of the known ratings is presented. To understand how it works, assume that we want to recommend a movie to Jane Doe who wants to see it with her boyfriend on Saturday in a movie theater. If the Time dimension is partitioned into weekend and weekday components, and because Saturday falls on a weekend, the reduction-based approach uses only the ratings for the movies seen on weekends by customers with their boyfriends/girlfriends in the movie theaters to provide recommendations for Jane Doe. It was shown that this approach outperforms the standard collaborative filtering in multidimensional settings under certain conditions (Adomavicius et al. 2005). Alternative multidimensional rating estimation methods include heuristic- and model-based approaches (Adomavicius and Tuzhilin 2005a).

In this paper, we focus on the querying capabilities of the REQUEST language, and therefore we assume that the multidimensional ratings cube is fully precomputed before users start issuing recommendation queries. In other words, we assume that all the unknown ratings have been estimated using any of the aforementioned rating estimation techniques. How to perform rating estimation “on demand” based on the query that was issued on a partially filled ratings cube constitutes an interesting future research problem, as we mention in §6.

The work described in Adomavicius et al. (2005) focuses on presenting the multidimensional recommendation model and does not specify how to express a wide variety of recommendations that are possible in multidimensional settings. In the next section, we address this limitation by presenting the query language REQUEST for expressing such recommendations.

## 3. Recommendation Query Language REQUEST

In this section, we describe the language by providing various examples of REQUEST queries in §3.1, then present its syntax in §3.2, and semantics in §3.3.

## 3.1. Introducing REQUEST via Examples

All the examples presented in this section are based on the five-dimensional MovieRecommender schema from Example 1. The first example presents the most basic and traditional recommendation request.

Query 1: Recommend the best movies to users. RECOMMEND Movie TO User USING MovieRecommender BASED ON PersonalRating

In this query, the RECOMMEND and TO clauses specify that movies will be recommended to users. The USING clause specifies the name of the multidimensional rating cube. The BASED ON clause specifies that personal ratings are used for recommendation purposes. The movies in this query are ordered separately for each user based on the PersonalRating measure that is either provided by the user or estimated from the set of known ratings, as mentioned in §2. The query returns the highest-rated movie for each user. Query 1 actually uses some defaults, and the equivalent query with the explicitly specified parameters is

RECOMMEND Movie (MovieID) TO User (UserID) USING MovieRecommender BASED ON PersonalRating(AVG) SHOW TOP 1 BY PersonalRating

Qualifier AVG specifies that, when the MovieRecommender cube is reduced to two dimensions, Movie and User, all the ratings of a movie seen by a user on different occasions are aggregated by averaging their values (note that the user could see or rate the same movie more than once across different contexts). Each measure can have its own default aggregation function (e.g., AVG in this case). The SHOW TOP k clause returns k best movies for the user ordered by aggregated PersonalRating measure (by default, k 1). MovieID and UserID represent the dimensional attributes that will be used when displaying the results.

Next, we introduce the restrictions on the recommendation criteria.

Query 2: Recommend, using personal ratings, the top five action movies to users older than 18.

RECOMMEND Movie TO User

USING MovieRecommender

RESTRICT Movie.Genre “Action” AND

User.Age ><sub>=</sub> 18

BASED ON PersonalRating(AVG)

SHOW TOP 5 BY PersonalRating

The RESTRICT clause is used to select the movies and the users satisfying the selection criteria. Then, only the selected movies are ordered for each selected user based on the instructions specified in the BASED ON and the SHOW clauses, as discussed above. As this and other examples show, the syntax of REQUEST differs from that of SQL. This is done on purpose to reflect significant differences between the application domains these languages are meant for. We discuss this further in §3.2.

We next show how ratings are filtered using the POSTFILTER clause.

Query 3: Recommend the top five movies to the user for the weekend, but only when personal ratings of the movies are higher than 7 (if fewer than five movies satisfy these criteria, then show only those satisfying them).

RECOMMEND Movie TO User

USING MovieRecommender

RESTRICT Time.TimeOfWeek “weekend”

BASED ON PersonalRating(AVG)

POSTFILTER PersonalRating > 7

SHOW TOP 5

Query 3 demonstrates that different clauses (RESTRICT and POSTFILTER) are used for the selections of attributes and ratings. First, only the weekend ratings are selected with the RESTRICT clause. Then, they are aggregated using the “BASED ON PersonalRating(AVG)” clause. Only then the POSTFILTER clause is applied to these aggregated PersonalRatings and only those greater than 7 are selected. If we want to restrict nonaggregated ratings, we should use the PREFILTER clause, as will be shown in Query 5. The reasons for using separate RESTRICT and POSTFIL-TER clauses when restricting attributes and ratings are discussed in §3.2.

The next example shows that more than one dimension can be used in recommendations, i.e., Movie and Time are recommended to User and Companion.

Query 4: Recommend to Tom and his girlfriend the top three movies and the best times to see them over the weekend.

RECOMMEND Movie, Time TO User,

Companion

USING MovieRecommender

RESTRICT User.Name “Tom” AND

Time.TimeOfWeek “weekend” AND

Companion.Type <sub>=</sub> “Girlfriend”

BASED ON PersonalRating

SHOW TOP 3

Sometimes, a certain group of people may be interested in a certain type of movies. For example, there has been work done on the topic of recommending to groups of users (Jameson and Smyth 2007) as well as using aggregate ratings in the recommendation process (Umyarov and Tuzhilin 2008). The next example shows how this type of aggregation can be done in REQUEST.

Query 5: Recommend movie genre to various professions using only the movies with personal ratings higher than 6.

RECOMMEND Movie.Genre TO

User.Profession

USING MovieRecommender

PREFILTER PersonalRating > 6

BASED ON PersonalRating(AVG)

This query aggregates rating scores for individual movies into averaged rating scores for different genres of movies. Also, individual users are aggregated by profession, and each profession becomes a new target for a recommendation. Before the ratings are aggregated, the PREFILTER operator selects the ratings higher than 6, and only these ratings are aggregated. It differs from the POSTFILTER operator in Query 3 because it deals with nonaggregated ratings, whereas POSTFILTER is applied to the aggregate ratings. This distinction is crucial in some recommendation settings.

The next example demonstrates that recommendations are not restricted to the User dimension; in general, different things can be recommended to various objects.

Query 6: Identify the top two professions that appreciate the movie Beautiful Mind the most.

RECOMMEND User.Profession TO Movie

USING MovieRecommender

RESTRICT Movie.Title “Beautiful Mind”

BASED ON PersonalRating(AVG)

SHOW TOP 2

Remember that a rating score for a movie is either explicitly specified by the user or is estimated from the existing user-specified ratings using one of the rating estimation methods described in Adomavicius and Tuzhilin (2005a) or Adomavicius et al. (2005). The next query is a modification of Query 1 that makes use of this fact.

Query 7: Recommend the best movies to users that they have not seen yet.

RECOMMEND Movie TO User

USING MovieRecommender

BASED ON PersonalRating(AVG),

Consumed(DISJ)

POSTFILTER NOT(Consumed)

SHOW TOP 1 BY PersonalRating

This query collects all the ratings given to a movie by a user (note that the user can provide multiple ratings to a movie seen in different contexts). Consumed is a Boolean flag related to PersonalRating measure specifying whether a movie was seen (consumed) by a user in some context. Consumed (DISJ) is the disjunction of the values of all of these flags for a movie/user pair. If this disjunction is true (the cumulative Consumed flag is True), this means that on at least one occasion, the user has seen the movie. The POSTFILTER NOT(Consumed) statement removes these cases. Thus, only the movies that the user has not seen (in any context) are recommended.

The next query shows how recommendations based on multiple ratings are used.

Query 8: Show the top five movies with both public ratings and personal ratings higher than 8 to students based only on the movies they have seen.

RECOMMEND Movie To User USING MovieRecommender

RESTRICT User.Profession <sub>=</sub> “Student” PREFILTER Consumed BASED ON PersonalRating(AVG), PublicRating(AVG) POSTFILTER PublicRating > 8 AND PersonalRating > 8 SHOW TOP 5 BY PersonalRating, PublicRating

This query first selects the ratings of movies provided by students that they have previously seen (i.e., prefilters them based on the Consumed flag). Then, it aggregates them based on personal and public ratings and selects only PublicRating and PersonalRating that, on average, are greater than eight. Finally, it sorts the movies for each user based on these two ratings in a standard lexicographic manner and selects the top five of them for each user.

Because ratings in a recommender system can be provided by users or estimated by software, note that we have an option of differentiating between actual, estimated, and other types of ratings for any rating measure. The REQUEST language supports this functionality via binary flags (implemented as separate Boolean measures) that can be used in PRE- and POSTFILTER clauses, as well as be aggregated using specific Boolean aggregation functions. For example, Queries 7 and 8 use the Consumed flag specifying if the rating is based on the movie that the user has actually seen. This is possible because, as explained earlier, all the estimated ratings and the related flags are precomputed, and thus can be used conceptually as additional measures.

After introducing REQUEST via examples, we next define the syntax of the language.

## 3.2. Syntactic Definition of REQUEST

We have developed REQUEST as a “vertical” query language for the specific domain of recommender systems. Following this approach, we tried to make sure that every construct of the language has a well-defined and intuitive meaning pertaining to recommender systems, while at the same time trying to maintain expressiveness and rigor of the language.

The BNF specification of REQUEST syntax is presented in Figure 1. First, note that we do not mimic the syntax of SQL for REQUEST because, if we tried to do so, this would likely cause many false assumptions on behalf of the users who may assume that properties of SQL operators automatically extend to REQUEST simply because the names of the operators are the same. For example, the RESTRICT clause of REQUEST is significantly more restrictive than the WHERE clause of ${ \mathrm { S Q L } } ,$ as will be explained below. This observation is also applicable to various other REQUEST clauses that will be discussed later in this section.

## Figure 1 BNF Specification of REQUEST Syntax

```verilog
// general syntax of a REQUEST query
REQUEST_query ::=
RECOMMEND recommend_dim_list TO recipient_dim_list
USING cube_name
[RESTRICT dimension_restrictions]
[PREFILTER preaggregation_measure_restrictions]
BASED ON aggr_measure_list
[POSTFILTER postaggregation_measure_restrictions]
[SHOW measure_rank_restriction]

// RECOMMEND and TO clauses
recommend_dim_list ::= dimension_list
recipient_dim_list ::= dimension_list
dimension_list ::= single_dimension {, single_dimension}* 
single_dimension ::= {dimension_name [output_attribute_list] | dimension_attribute}
output_attribute_list ::= (attribute_name {, attribute_name}*)
// USING clause
cube_name ::= variable

// RESTRICT clause
dimension_restrictions ::= single_dimension_restriction {AND single_dimension_restriction}* 
single_dimension_restriction ::=
    dimension_attribute {numeric_comparison | textual_comparison | set_membership_test}

// BASED ON clause
aggr_measure_list ::= single_aggr_measure {, single_aggr_measure}* 
single_aggr_measure ::= measure_name [(rating_aggr_function)]
rating_aggr_function ::= numeric_aggr_function | boolean_aggr_function
numeric_aggr_function ::= MIN | MAX | SUM | AVG
boolean_aggr_function ::= DISJ | CONJ | MAJORITY

// PREFILTER and POSTFILTER clauses
preaggregation_measure_restrictions ::= measure_restrictions
postaggregation_measure_restrictions ::= measure_restrictions
measure_restrictions ::= single_measure_restriction {logical_op single_measure_restriction}* 
single_measure_restriction ::= numeric_measure_restriction | boolean_measure_restriction
logical_op ::= AND | OR
numeric_measure_restriction ::= measure_name numeric_comparison
boolean_measure_restriction ::= measure_name | NOT (measure_name) | measure_name = boolean_value

// SHOW clause
measure_rank_restriction ::= {TOP | BOTTOM} number [BY measure_list]
measure_list ::= measure_name {, measure_name}* 

// common expressions
dimension_attribute ::= dimension_name.attribute_name
dimension_name ::= variable
attribute_name ::= variable
measure_name ::= variable
numeric_comparison ::= {= | <> | > | < | <= | >=} number
textual_comparison ::= {= | LIKE } 'string'
set_membership_test ::= {IN | NOT IN} (value_list)
value_list ::= numeric_value_list | textual_value_list
numeric_value_list ::= number {, number}* 
textual_value_list ::= 'string' {, 'string'}* 
boolean_value ::= true | false
```

As Figure 1 shows, the USING clause allows only a single cube, thus restricting recommendations to a single cube of ratings and prohibiting joins between cubes in REQUEST. We made this restriction because multicube recommendations seldom have meaningful and practically important applications and also can lead to various complications and side effects. For example, to join two cubes on a certain dimension, such as Time, the two dimensions should be identical for all the levels of the aggregation hierarchy, e.g., across the entire Time hierarchy, which is often impractical and also difficult to enforce. Also, if multiple cubes are used in queries, then there is a dilemma of whether the PUSH and PULL operators of the standard OLAP querying paradigm (Agrawal et al. 1997), that can “push” one of the dimensions to become a measure and also “pull” a measure as a new dimension, should be supported at the algebraic level. Without such operators incorporated into REQUEST, certain multicube queries either cannot be expressed or can be done only in a very convoluted manner. At the same time, incorporating the PUSH and PULL operators into the language creates numerous complications for REQUEST because of the inherent semantic differences between dimensions and measures in the multidimensional recommendation model. Therefore, having multiple cubes creates various problems both with and without the PUSH and PULL operators in REQUEST. Finally, when joining cubes, estimated ratings need to be reevaluated for the joined cubes, often in significantly higher-dimensional spaces. This can lead to the rating estimation problem because of the rating sparsity in the joined cube. Instead of supporting joins in REQUEST, a much better alternative is for the domain expert to manually build a single cube from two or more individual cubes. In the rest of this section, we describe the syntax of REQUEST based on Figure 1.

The RESTRICT clause contains dimension\_restrictions that constitute the standard restrictions of the “slice-and-dice” operator of the OLAP systems. Each individual restriction is limited to the numeric and textual comparison of a dimension attribute to a constant value (or a set of values), as specified in the BNF grammar in Figure 1, and these dimensions and attributes have to be present in the schema of the cube\_name cube. Moreover, multiple restrictions in a single RESTRICT clause are permitted, but only if combined by logical operator AND. Disjunctions (OR) are not allowed because the result of such restrictions would no longer be a multidimensional cube, as illustrated in Figure 2.

We also would like to note that, although the RESTRICT clause is somewhat similar to the WHERE clause of SQL, they also have the following key differences mostly stemming from our need to restrict REQUEST to make it more suitable for the recommendation applications. First, the WHERE clause of SQL is not limited to conjunctions, as RESTRICT is, but can also have disjunctions. Second, each individual restriction (conjunct) in the RESTRICT clause can involve only one dimension (i.e., a comparison of some dimension attribute to a constant, as mentioned earlier) to ensure that the result of the restriction is still a proper multidimensional cube. For this reason, for example, the restriction “RESTRICT User.Age > Movie.Length” is not allowed in REQUEST. In contrast, the WHERE clause of SQL allows having attributes from multiple relations in a single condition. Third, the WHERE clause of SQL supports nested queries, whereas RESTRICT does not. Besides these major differences between the two clauses, there

Figure 2

Combining Dimension Restrictions Using (a) AND and (b) OR Operators  
![](/api/attachments/P5479VD3/fulltext/images/65e52915b78595c8229d300dd8443dbab7790e03aadb4b22936c070fe914acc2.jpg)

![](/api/attachments/P5479VD3/fulltext/images/ce794425bea1128e770b65188881af95ae20ecac5156861d0dab63a83389099a.jpg)

are also minor differences apparent from the BNF grammars of the two languages.

The PREFILTER and POSTFILTER clauses contain measure\_restrictions that constitute a set of restrictions on various types of measures used in cube\_name. Note that, unlike dimension\_restrictions, both AND and OR operators are allowed in measure\_restrictions according to Figure 1. REQUEST uses separate RESTRICT and PRE-/POSTFILTER clauses when restricting attributes on dimensions and rating measures for the following reasons. First, these two types of restrictions are semantically very different: the first one restricts the contextual information by imposing conditions on dimensional attributes, while the second does it on the measures. Second, the POSTFILTER clause must be kept separately because, unlike RESTRICT, it is applicable to the aggregate ratings, which are semantically different from the unaggregated ratings. Although this point is not applicable to the PRE-FILTER clause, it is better to keep both the PREand the POSTFILTER clauses (as they are symmetric), which makes it impossible to merge PREFILTER and RESTRICT clauses. Third, as pointed out before, only conjunctions are allowed in RESTRICT, but both conjunctions and disjunctions are allowed in the PRE- and POSTFILTER clauses, making it even more important to treat them separately. Fourth, to keep

RECOMMEND movie (Title) TO user (Name) USING TestCube BASED ON Rating SHOW TOP 2

the semantics of recommendations clear, it is important not to mix the rating measures and dimensional restrictions by prohibiting expressions of the form “PersonalRating > Time.DayOfWeek.” These were the reasons for keeping the two types of restrictions separate. Note that this situation is not unlike the case in temporal databases, where separate WHERE and WHEN clauses are used for regular and temporal dimensions (Snodgrass 1987).

Formally, the output of a recommendation query is a set of tuples $\{ \hat { ( } t , L _ { t } ) \mid t \in T \} ,$ , where t is a recommendation recipient and L is a list of recommendations for recipient t. For example, in a movie recommender system, a simple example of a recommendation tuple would be: (JohnDoe, <(Titanic, 10), (Gladiator, 9), (StarWars, 8)>). In other words, T represents the element combinations of dimensions from recipient\_dim\_list specified in the TO clause of the query, and $L _ { t }$ consists of an ordered set of k recommendations, where k is specified by the SHOW clause of the query. More precisely, $L _ { t } =$ $< ( r _ { t 1 } , m _ { t 1 } ) , \ldots , ( r _ { t k } , m _ { t k } ) >$ , i.e., each recommendation is represented by a tuple $( r _ { t j } , m _ { t j } )$ , where $r _ { t j } \in R _ { q }$ and $m _ { t j } \in M _ { q }$ . Here, $R _ { q }$ represents the element combinations of dimensions from recommend\_dim\_list specified in the RECOMMEND clause of the query (note that recommend\_dim\_list and recipient\_dim\_list must be mutually exclusive), and $M _ { q }$ represents the combinations of possible values for one or more measures that are specified in measure\_list in the BY subclause of the SHOW clause. Specific tuples $( r _ { t j } , m _ { t j } )$ are obtained from the processed ratings cube $( \mathrm { i . e . , }$ after restrictions and aggregations specified in the query are done) by sorting all cells belonging to a given recipient t based on their measure values; these measure values $m _ { t j }$ and the corresponding element combinations of RECOM-MEND dimensions $r _ { t j }$ constitute the contents of each recommendation in $L _ { t } ^ { ' } . ~ L _ { t }$ is further truncated according to the SHOW clause that limits the results to the top or bottom k recommendations. If more than one measure is specified in measure\_list, then the ordering is lexicographic. For example, in Query 8, Movies are first ordered based on the PersonalRating measure; if some records have the same value of PersonalRating, then those are further sorted based on PublicRating. Also, if the optional BY subclause is not specified, the results are sorted according to the first measure in the BASED ON clause.

According to the above formalism, the output of a recommendation query, i.e., $\{ ( t , L _ { t } ) \mid t \in \bar  T \}$ , can be intuitively represented as a matrix, the rows of which are defined by elements t of the TO dimensions (i.e., by the recommendation recipients). The entries in each row are defined by the elements of list $L _ { t } ,$ where each element represents the specific values of the RECOMMEND dimensions and corresponding rating measures. In other words, one row in a recommendation matrix directly corresponds to one recommendation tuple -t L  described earlier. For example, Figure 3 shows the output matrices for two recommendations (movies to users and vice versa). The answer to the left query shows the top two movies for each user, and the right one—the top two users for each movie (as specified in the SHOW clause). The output matrix produced for the left query in Figure 3 is based on users (as specified in the TO clause), and its cells contain movies (as specified in the RECOMMEND clause) and the corresponding rating measures, which were also used for sorting.

Figure 3 Generating Recommendations from a Multidimensional Ratings Cube

<table><tr><td></td><td>K-PAX</td><td>Life of Brian</td><td>Memento</td><td>Notorious</td></tr><tr><td>Alice</td><td>4</td><td>3</td><td>2</td><td>4</td></tr><tr><td>Bob</td><td>5</td><td>4</td><td>5</td><td>3</td></tr><tr><td>Cindy</td><td>2</td><td>2</td><td>4</td><td>4</td></tr><tr><td>David</td><td>3</td><td>5</td><td>5</td><td>2</td></tr></table>

![](/api/attachments/P5479VD3/fulltext/images/9161de5715e1b1541fe5e0c1632a43329cba66b880acb22a65c3d6f99d27550b.jpg)

<table><tr><td rowspan="2">Alice</td><td>K-PAX, 4</td></tr><tr><td>Notorious, 4</td></tr><tr><td rowspan="2">Bob</td><td>K-PAX, 5</td></tr><tr><td>Memento, 5</td></tr><tr><td rowspan="2">Cindy</td><td>Memento, 4</td></tr><tr><td>Notorious, 4</td></tr><tr><td rowspan="2">David</td><td>Life of Brian, 5</td></tr><tr><td>Memento, 5</td></tr></table>

![](/api/attachments/P5479VD3/fulltext/images/983cccc58ba9284401131fb2663b8f9ebef382909288333e5f5b0396a649ca55.jpg)

RECOMMEND user (Name) TO movie (Title) USING TestCube BASED ON Rating SHOW TOP 2

<table><tr><td rowspan="2">K-PAX</td><td>Bob, 5</td></tr><tr><td>Alice, 4</td></tr><tr><td rowspan="2">Life of Brian</td><td>David, 5</td></tr><tr><td>Bob, 4</td></tr><tr><td rowspan="2">Memento</td><td>Bob, 5</td></tr><tr><td>David, 5</td></tr><tr><td rowspan="2">Notorious</td><td>Alice, 5</td></tr><tr><td>Cindy, 5</td></tr></table>

Note that, if the end-users want to use actual user names and movie titles in the output matrix, they should specify the output\_attribute\_list parameters from Figure 1 in the RECOMMEND and TO clauses. For example, the left recommendation in Figure 3 is stated as “RECOMMEND Movie(Title) TO User(Name)    ” If the output\_attribute\_list parameters are not specified, then the dimension keys are used as defaults. For example, instead of using the names of the users, the system would output the recommendations using user IDs. Also, note that the recommendation results can be more complex in the sense that multiple dimensions can be used in the RECOMMEND and TO clauses, as Query 4 from §3.1 demonstrates. In such cases, each row in the output matrix would represent a multidimensional element t (i.e., a vector representing a unique combination of elements of TO dimensions) and, correspondingly, would also have more complex multidimensional entries in the cells.

Although we used the term “REQUEST queries” throughout this paper, recommendations are really not queries according to the standard meaning of the term, because they return a very idiosyncratic output of a recommendation matrix, which prevents the whole recommendation operation from being closed. To address this issue, we distinguish between the Core-REQUEST query containing RECOMMEND, TO, USING, RESTRICT, PREFILTER, POSTFILTER, and BASED ON clauses, and the recommendation wrapper containing RECOMMEND, TO, and SHOW clauses (note, however, that different aspects of RECOM-MEND and TO are used in core and wrapper parts of the query). The Core-REQUEST query operates on a multidimensional cube of ratings and always returns the same type of an object—a cube of ratings. In contrast to this, the recommendation wrapper takes a multidimensional cube of ratings and transforms it to a different type of object—the recommendation matrix that is subsequently returned as an output to the end-user. When processing REQUEST queries, the core query is evaluated first, and then the wrapper is applied to the output of the Core-REQUEST query.

Although REQUEST is related to the OLAP query languages, it has certain distinctive characteristics pertaining to recommendations that make it different from these languages. First, as explained above, REQUEST queries are divided into the “core” and “wrapper” components, each component requiring separate evaluation methods. Second, ratings can be actual (specified by the user) and inferred (from the actual ratings). Therefore, REQUEST supports mechanisms for distinguishing between different types of ratings, as Query 7 demonstrated. Third, the language provides various other recommendationspecific properties, such as using a single cube of ratings, the PREFILTER and POSTFILTER clauses, and recommendation-specific types of aggregations. All this differentiates REQUEST from the generalpurpose OLAP-based query languages and makes it a uniquely suited vertically targeted language for recommender systems. This approach of developing a special-purpose vertical query language to meet the idiosyncratic needs of a particular class of applications (recommender systems, in this case) is in line with the development of other types of specialpurpose query languages for different classes of vertical database applications, such as temporal, spatial, and multimedia applications.

## 3.3. Semantics of REQUEST Queries

Operational semantics of REQUEST are defined as the following sequence of operations over the cube cube\_name from the USING clause of the query. Note that these operational semantics are only conceptual, i.e., the actual query processing may be performed differently, but would result in the same outcome.

(1) Dimension Restrictions. First, the dimension restrictions specified in the RESTRICT clause, if present, produce a subcube of cube\_name by restricting some of its dimensions to include only a subset of their elements specified in the RESTRICT clause. For example, “RESTRICT User.Age <sub>≥</sub> 18 AND Movie.Genre ‘action’ ” produces a smaller cube having only the users with ages 18 and above and only the action movies. Section 3.2 lists the limits to the syntax of these restrictions (e.g., only comparisons of dimensional attributes to constants are allowed, and no disjunctions in the RESTRICT clause). This amounts to applying restrictions in the RESTRICT clause one dimension at a time and also restricting one attribute at a time. The order in which these dimensions are restricted is unimportant because the final result does not depend on it.

(2) Measure-Based Cube Filtering (Before Aggregation). In this step, the cells of the restricted cube produced in Step 1 are further filtered based on measure restrictions specified in the PREFILTER clause. Because the measures supported by our multidimensional recommendation model can be either numeric or Boolean, the measure-based filtering capabilities of REQUEST include comparisons of both numeric and Boolean measures to specific values, as specified in Figure 1. Also, note that this step filters individual cube cells based on their measure values using multiple restrictions combined with AND and OR logical operators. Again, all measures mentioned in the PREFILTER clause have to be present in the schema of the cube\_name cube.

(3) Cube Aggregation. After performing restricting and prefiltering operations in Steps 1 and 2, the remaining cells of the obtained cube are aggre-

gated according to the dimensions and their granularity levels specified in the mutually exclusive lists recommend\_dim\_list and recipient\_dim\_list from the RECOMMEND and TO clauses and according to the following three rules: (1) if a dimension is specified in either the RECOMMEND or TO clause by itself, i.e., without providing an aggregation attribute (e.g., Movie), then the cube is not aggregated along this dimension; (2) if a dimension is specified in either the RECOMMEND or TO clause with a corresponding aggregation attribute (e.g., Movie.Genre), then the cube is aggregated along this dimension based on the specified attribute (e.g., all individual movies are aggregated into their genres); and (3) if a dimension is omitted from both RECOMMEND and TO clauses, then the cube is aggregated fully along this dimension (i.e., in the resulting cube, this dimension essentially disappears). Furthermore, the aggregation is done for the measures specified in the BASED ON clause. This clause also specifies the aggregation functions to be used for each measure. The currently supported numeric aggregation functions include AVG, SUM, MIN, and MAX, and the supported Boolean aggregation functions include CONJ (i.e., conjunction), DISJ (i.e., disjunction), and MAJORITY; however, the REQUEST language can be easily extended to support additional aggregation functions, such as AVG-in-TOP-n. If an aggregation function is not specified for the measures in the BASED ON clause, a default aggregation function for that measure is used (e.g., AVG). Essentially, this step represents a typical “roll-up” operation in OLAP systems. Figure 4 provides further illustration of the cube aggregation operation, where the Time dimension is collapsed and the User dimension is aggregated based on the gender attribute. Then, for each movie, all the ratings across different occasions provided by users of a particular gender (e.g., see the shaded area in Figure 4) are averaged using the AVG function.

(4) Measure-Based Cube Filtering (After Aggregation). In this step, the cells of the resulting aggregated cube can further be filtered based on the aggregated measure restrictions specified in the POSTFIL-TER clause. As it is specified in the BNF grammar in Figure 1, the syntax of the POSTFILTER clause is the same as for PREFILTER. Thus, if a given REQUEST query contains no aggregation, then PREFILTER and POSTFILTER, if both present, can be combined as a conjunction into one measure-based filtering operation at the query processing stage. Also, all the measures mentioned in the POSTFILTER clause must appear among the measures mentioned in the BASED ON clause (because only these measures are aggregated). Note that the POSTFILTER clause is somewhat similar to the HAVING clause in SQL because both of them provide additional restrictions based on the aggregated data. However, one significant difference is that SQL allows creating an arbitrary number of aggregated attributes from the same unaggregated one, e.g., “SELECT MIN(Rating), MAX(Rating), SUM(Rating), COUNT(Rating), AVG(Rating) FROM Table.” In contrast, each measure can lead to just one aggregated version of itself in REQUEST. Another difference is that REQUEST supports not only numeric, but also Boolean aggregation functions (that are not available in standard SQL).

(5) Generating Recommendations. In this step, the cube obtained in Step 4 is transformed into a specialized recommendation matrix, as was described in detail in §3.2. The rows of this matrix are determined by the TO clause of the REQUEST query. Each row of the matrix also contains the list of the records specified in the RECOMMEND clause and the measures are used to sort the results. These lists of records are sorted and truncated based on the SHOW clause.

Figure 4 Cube Aggregation Operation  
![](/api/attachments/P5479VD3/fulltext/images/3ad8b73a0f971daa3b7b1fe43cf1614c3dc1f79eb727c55f649e303a0bb61049.jpg)

This completes the description of semantics of the REQUEST language. This description was provided in a semiformal manner in the sense that we did not use mathematics to define semantics of each of the five operations formally for the sake of readability. However, we provided enough details for the interested reader to easily understand and reconstruct formal semantic procedures defining each of these five steps. Moreover, we provide a formal definition of recommendation algebra RA in §4, which will make this reconstruction process even easier.

We next present algebra RA that more formally defines how REQUEST queries are processed. Because algebraic operators should return objects of the same type as their inputs, we will target the RA only to the Core-REQUEST queries (corresponding to Steps 1–4 above). To process a full REQUEST query, we construct an algebraic expression equivalent to the Core-REQUEST query, evaluate ${ \mathrm { i t } } ,$ and then feed the results into the REQUEST wrapper to produce the final output.

## 4. Recommendation Algebra RA

Because multidimensional recommendations are based on the OLAP paradigm, we use the OLAP algebras introduced in the database community (Agrawal et al. 1997, Gyssens and Lakshmanan 1997, Li and Wang 1996, Marcel 1999, Thomas and Datta 2001) to define the recommendation algebra. However, since the REQUEST language is tailored specifically for the domain of recommendations, only a subset of the standard OLAP operators is needed to process REQUEST queries. For example, we do not use a JOIN operator in the recommendation algebra because REQUEST works only on one cube, and we do not use the PUSH and PULL operators for the reasons explained in §3. In the rest of this section, we describe the recommendation algebra RA. We will follow the definitions of the OLAP operators introduced in Thomas and Datta (2001).

The general syntax of RA operators is

$$
C _ {O} = O P _ {p a r a m e t e r s} (C _ {I}),
$$

where $C _ { I } = ( D , M , H , E , L )$ denotes the input cube, $C _ { O } = ( D ^ { * } , M ^ { * } , H ^ { * } , E ^ { * } , L ^ { * } ) \mathrm { . }$ —the resulting output cube, OP—an RA operator, and parameters—the parameters of operator OP. The ratings cube and its components D, M, H, E, and L are defined in §2.

We next introduce individual operators using this general syntax.

Dimension Restriction (DRSTR) Operator. This operator defines the slice-and-dice operation on the cube by putting restrictions on the dimensions. The simplest form of DRSTR operator is

$$
C _ {O} = D R S T R _ {P s i m p l e} (C _ {I}),
$$

where $P _ { s i m p l e }$ is a domain restriction based on a single dimension $d _ { i } , \mathrm { \ e . g . , \mathrm { \ ^ { \prime \prime } U s e r . A g e } } > 2 1 . ^ { \prime \prime }$ In other words, $P _ { s i m p l e }$ is a Boolean function (a predicate) of the form $P _ { s i m p l e } \colon E _ { i } $ {true, false}. Given an arbitrary input ratings cube, as a result of this operator, only those cells that satisfy the given predicate are retained in the resulting cube. The calculation of $C _ { O }$ is formally defined as

$$
\begin{array}{l} (1) D ^ {*} = D, M ^ {*} = M, \text {and} H ^ {*} = H. \\ (2) E _ {i} ^ {*} = \{e _ {i} \in E _ {i} \mid P _ {s i m p l e} (e _ {i}) \}. \text {Also}, E _ {j} ^ {*} = E _ {j}, \text {if} j \neq i. \\ (3) L ^ {*} = \{(a d d r e s s, c o n t e n t) \in L \mid a d d r e s s \in E _ {1} ^ {*} \times \dots \times \\ E _ {n} ^ {*} \}. \end{array}
$$

In addition to the aforementioned simple predicates, this operator can also support more complex predicates. For example, $P _ { c o m p l e x }$ could be represented by a compound predicate of the form

$$
P _ {c o m p l e x} = p _ {1} \text { AND } p _ {2} \text { AND } \dots \text { AND } p _ {x},
$$

where each $p _ { j }$ is a domain restriction involving a single dimension. Because the result of a simple predicate-based restriction is always a cube, the compound restriction operator is defined as a composition of simple restriction operators, i.e.,

$$
\begin{array}{l} C _ {O} = D R S T R _ {P c o m p l e x} (C _ {I}) \\ \quad = D R S T R _ {p 1 A N D \dots A N D p x} (C _ {I}) \\ \quad = D R S T R _ {p 1} (D R S T R _ {p 2} (\dots (D R S T R _ {p x} (C _ {I})) \dots)). \end{array}
$$

Note that, the while DRSTR operator can support predicates with conjunctions (logical AND operations), it does not support arbitrary disjunctions (logical OR operations) because the result of such operations is no longer guaranteed to be a cube, as mentioned earlier.

Measure Restriction (MRSTR) Operator. This operator defines the cell filtering operation on the ratings cube by putting restrictions on measures. The simplest form of MRSTR operator is

$$
C _ {O} = M R S T R _ {P} (C _ {I}),
$$

where P is a measure restriction based on a single measure $m _ { j }$ . The restrictions can be based on a numeric measure (“PersonalRating > 7”) and on a Boolean measure (“Consumed false”).

Unlike the DRSTR operator (which is a slice-anddice operator), the MRSTR operator performs simple filtering of cube cells, and therefore can support more complex predicates, e.g.,

$$
P = p _ {1} <   o p > p _ {2} <   o p > \dots <   o p > p _ {x},
$$

where <op> represents a logical operator AND or OR. Given an arbitrary input cube, as a result of this operator, only the content of cells that satisfy the given predicate are retained in the resulting cube. The content of all other cells is assigned to NULL (these cells are retained and not deleted to maintain the proper cube structure).

The calculation of $C _ { O }$ is formally defined as follows: (1) $D ^ { * } = D , M ^ { * } = M , H ^ { * } = H ,$ , and $E ^ { * } = E$

(2) Assign $L ^ { * } = L$ . Then, -address content $\in L ^ { * } \colon$ : if <sub>¬</sub>P (content), then $L ^ { * } [ a d d r e s s ] = \mathrm { N U L L }$

Metric Projection (MRPJ) Operator. This operator restricts the output of a ratings cube to include only a subset of the original set of measures. The simple form of MRPJ operator is

$$
C _ {O} = M R P J _ {m j} (C _ {I}),
$$

where $m _ { j }$ is a measure to be projected out. The calculation of $\scriptstyle \left( C _ { o } \right)$ is formally defined as follows:

(1) $D ^ { * } = D , H ^ { * } = H ,$ and E∗ E.

(2) $M ^ { * } = M - \{ m _ { i } \} .$

(3) Assign $L ^ { * } = L$ . Then, -address content $\in { L } ^ { * } \colon$ remove the jth measure from L∗[address]. If, as a result, L∗[address] has no more measures left, assign $L ^ { * } [ a d d r e s s ] = \mathrm { N U L L }$ .

If a set of metrics $M ^ { \prime } = \{ m _ { 1 } ^ { \prime } , \ldots , m _ { x } ^ { \prime } \}$ is needed to be removed at once, a more complex MRPJ operator can be implemented as a composition of simple MRPJ operators. In other words,

$$
C _ {O} = M R P J _ {M ^ {\prime}} (C _ {I}) = M R P J _ {m ^ {\prime} 1} (\ldots (M R P J _ {m ^ {\prime} x} (C _ {I})) \ldots).
$$

Destroy Dimension (DTDM) Operator. This operator reduces dimensions of the resulting ratings cube by including only a subset of the original set of dimensions. The simplest form of DTDM is

$$
C _ {O} = D T D M _ {d i} (C _ {I}),
$$

where $d _ { i }$ is a dimension to be destroyed. Note that, if we destroyed dimension $d _ { i }$ by just removing its component from all cube cell addresses, we would have a number of cells in the cube with the same exact addresses, which leads to ambiguous results, and therefore is undesirable. One way to deal with this situation is to aggregate all cells with the same address into a single cell in a resulting cube. Because, as described below, we already have an operator for cell aggregation (i.e., AGGR), we do not introduce the aggregation capability into DTDM. Therefore, to properly destroy dimension $d _ { i } ,$ we restrict the use of the DTDM operator only to the situations in which there is no ambiguity and no loss of information in the resulting cube. Thus, dimension $d _ { i }$ can be destroyed only when it has been maximally aggregated, i.e., when $| E _ { i } | = 1$

The calculation of $C _ { O }$ is formally defined as follows: (1) If $| E _ { i } | > 1$ , abort processing and return the same ratings cube, i.e., ${ C _ { O } } ^ { - } = C _ { I }$ . Otherwise, continue as specified below.

(2) $M ^ { * } = M , D ^ { * } = D - \{ d _ { i } \} , H ^ { * } = H - \{ H _ { i } \}$ , and $E ^ { * } =$ $E - \left\{ E _ { i } \right\}$

(3) Assign $L ^ { * } = L$ . Then, -address content $\in { L } ^ { * } \colon$ remove the ith dimension from address.

If a set of dimensions $D ^ { \prime } = \{ d _ { 1 } ^ { \prime } , \ldots , d _ { x } ^ { \prime } \}$ is needed to be removed at once (assuming they are all maximally aggregated), a more complex DTDM operator can be easily implemented as a combination of simpler DTDM statements. In other words,

$$
C _ {O} = D T D M _ {D ^ {\prime}} (C _ {I}) = D T D M _ {d ^ {\prime} 1} (\dots (D T D M _ {d ^ {\prime} x} (C _ {I})) \dots).
$$

Aggregation (AGGR) Operator. The aggregation operator performs aggregation on one or more dimensions and applies aggregation functions, such as SUM, AVG, etc., to each of the measures of the cube based on dimensions specified as grouping attributes. The general form of AGGR is

$$
C _ {O} = A G G R _ {(d _ {1}. x _ {1}, \dots , d _ {l}. x _ {l}), (m _ {1}. f _ {1}, \dots , m _ {k}. f _ {k})} (C _ {I}),
$$

where $d _ { i } . x _ { i }$ represents a grouping attribute for dimension $d _ { i }$ (specified only for dimensions that need to be grouped). Also, $m _ { j } . f _ { j }$ is an aggregation function specified for each cube measure $m _ { j } .$ If the aggregation function is not specified for some measure, a default aggregation function for that measure is used. After aggregation, $d _ { i } . . x _ { i }$ becomes a dimension (with its own attributes, whichever appropriate) by replacing $d _ { i } .$ . Our model also provides a special option to aggregate the dimension completely by specifying $d _ { i } . x _ { i }$ as $\breve { d } _ { i } . \mathrm { A L L }$ (instead of using some attribute name). Furthermore, $m _ { j } . f _ { j }$ can be one of the standard numeric aggregation functions $( \mathrm { e . g . }$ , MAX, MIN, AVG, SUM) or Boolean aggregation functions, including

$$
f _ {j} (B) = \mathrm{DISJ} (B) = \bigvee_ {b \in B} b,
$$

$$
f _ {j} (B) = \operatorname{CONJ} (B) = \bigwedge_ {b \in B} b, \quad \text { and }
$$

$$
f _ {j} (B) = \mathrm{MAJORITY} (B)
$$

$$
= \left\{ \begin{array}{l l} \text {true} & \text {if} | \{b \in B \mid b = \text {true} \} | \\ & \quad \geq | \{b \in B \mid b = \text {false} \} | \\ \text {false} & \text {otherwise.} \end{array} \right.
$$

As an example, consider the movie recommender system having three dimensions: User, Movie, and

Time. Suppose user John Doe wants to know which movies that he has not seen yet are most relevant to him, regardless of when he is planning to watch them. Suppose the system has the following four ratings for John Doe: [(John Doe, Gladiator, weekday), (Rating <sub>=</sub> 8, Consumed <sub>=</sub> true)], [(John Doe, Gladiator, weekend), (Rating  9, Consumed  false)], [(John Doe, Titanic, weekday), (Rating <sub>=</sub> 7, Consumed <sub>=</sub> false)], [(John Doe, Titanic, weekend), (Rating 8, Consumed false)]. In this case, the aggregation operator would look like

$$
C _ {O} = A G G R _ {\text {(Time.ALL) , (Rating.AVG, Consumed.DISJ)}} \left(C _ {I}\right).
$$

Because the time dimension has to be aggregated completely, we use AVG function to aggregate the ratings for the same movie; we also use DISJ Boolean aggregation function to make sure that movies with at least one Consumed rating would not get recommended (because the user has seen it already). In this case, the results of aggregation would be: [(John Doe, Gladiator, ALL), (Rating <sub>=</sub> 85, Consumed <sub>=</sub> true)], [(John Doe, Titanic, ALL), (Rating <sub>=</sub> 75, Consumed <sub>=</sub> false)], and the user, by filtering on the “Consumed <sub>=</sub> false” status flag, would be able to receive a correct recommendation of Titanic because the user has already seen Gladiator.

Now, consider the same four ratings but a different scenario, where John Doe wants to know which times of week would be best for him in terms of movie watching, regardless of what kind of movie he is planning on watching. In this case, the aggregation operator would be

$$
C _ {O} = A G G R _ {\text {(Movie.ALL, Time.TimeOfWeek), (Rating.AVG, Consumed.CONJ)}} \left(C _ {I}\right).
$$

Because the movie dimension has to be aggregated completely, we again use AVG function to aggregate the ratings for the same time values. However, this time it may make more sense to use the CONJ Boolean aggregation function to make sure that only time periods with no unseen movies $( \mathrm { i . e . , }$ with no Consumed false flags) would get labeled as Consumed true (since only in that case there would not be anything for the user to watch during that time period). Note that, while in the current model we use CONJ, DISJ, and MAJORITY functions, other Boolean aggregation functions are also possible.

The calculation of $C _ { O }$ is then formally defined as follows:

(1) $\begin{array} { r } { D ^ { * } = D - \bigcup _ { i } \{ d _ { i } \} + \bigcup _ { i } \{ d _ { i } . x _ { i } \} } \end{array}$ . Note that, if $d _ { i } . x _ { i } =$ Root-H , then dimension $d _ { i }$ remains unchanged, $\mathrm { i . e . , }$ there is no aggregation on $d _ { i } .$ . As a result, $E _ { i } ,$ and $H _ { i }$ (see below) would also remain unchanged.

(2) $M ^ { * } = M .$

(3) $\forall i = 1 , \ldots , n \colon H _ { i } ^ { * } = S u b G r a p h ( H _ { i } , d _ { i } . x _ { i } )$ . In other words, the attributes for the newly aggregated dimension are the ones that are uniquely determined by the new key attribute $d _ { i } . x _ { i } ( \mathrm { i . e . } $ , that are reachable from $d _ { i } . x _ { i }$ in the attribute hierarchy for dimension $d _ { i } )$ . Furthermore, after aggregation, only the hierarchy structure rooted in node $d _ { i } . x _ { i }$ is needed for further processing. For example, based on Time dimension attribute hierarchy (i.e., Time  DayOfWeek TimeOfWeek), after aggregating Time dimension based on DayOfWeek, the new set of attributes would be {DayOfWeek, TimeOfWeek}.

(4) $\forall i = 1 , \ldots , n \colon E _ { i } ^ { * } = d o m ( d _ { i } . x _ { i } )$ The cube cells along the newly aggregated dimension become labeled with the values of the new key attribute. For example, after aggregating Time dimension based on DayOfWeek, the cube cells for this dimension would be labeled as {Mon, Tue, Wed, Thu, Fri, Sat, Sun}.

$$
(5) (\forall a d d r e s s ^ {*} \in E _ {1} ^ {*} \times \dots \times E _ {n} ^ {*}) (\forall j = 1, \ldots , k)
$$

$$
L ^ {*} [ a d d r e s s ^ {*} ]. m _ {j} = \underset {f _ {j _ {a d d r e s s \in L}, a d d r e s s <   a d d r e s s ^ {*}}} {a g g r} (L [ a d d r e s s ]. m _ {j}).
$$

In other words, each metric $m _ { j }$ is computed for each cell of the new cube using aggregation function $f _ { j }$ and based on cells from input cube that were replaced by (or aggregated into) a given cell. More precisely, given address $\mathbf { \Psi } = ( e _ { 1 } , \dots , e _ { n } ) \in E _ { 1 } \times \dots \times E _ { n }$ and address $\mathbf { \Phi } ^ { * } = ( e _ { 1 } ^ { * } , \ldots , e _ { n } ^ { * } ) \in E _ { 1 } ^ { * } \times \cdot \cdot \cdot \times E _ { n } ^ { * } ,$ we say that address address∗ if and only if $d _ { i } = e _ { i } \Rightarrow d _ { i } . x _ { i } = e _ { i } ^ { * }$ Finally, note that cube cells that have NULL values are ignored during the aggregation. However, if all underlying cells have NULL values for a specific aggregation, then that aggregated cell will be assigned the NULL value as well.

Composition of RA Operators. The recommendation algebra RA is formed by the composition of these five operators. Because each of these operators takes a rating cube and produces another rating cube, the RA algebra is closed. For example, Query 3 (recommend the top five movies to the user to see over the weekend, but only when the personal ratings of the movies are higher than 7) can be expressed in RA as

$$
\begin{array}{l} \text {MRSTR} _ {\text {(PersonalRating > 7)}} (\text {DTDM} _ {\text {(Theater, Time, Companion)}}) \\ \text {AGGR} _ {\text {(Theater. ALL, Time. ALL, Companion. ALL), (PersonalRating.AVG)}} (\text {MRPJ} _ {\text {(PublicRating, Consumed)}} (\text {DRSTR} _ {\text {(Time.TimeOfWeek = "weekend")}} \\ \text {(MovieRecommender))} \end{array}
$$

As explained before, this algebraic expression specifies only the core part of the REQUEST query. The actual recommendation results are generated by the REQUEST wrapper from the results of the core query. Therefore, this algebraic expression destroys all other dimensions toward the end, leaving only the User and Movie dimensions for the wrapper to work with.

Also, this example shows how MRPJ and DTDM operators remove measures and dimensions from the cube; e.g., PublicRating and Consumed measures as well as Theater, Time, and Companion dimensions are removed from the MovieRecommender cube.

## 5. Mapping REQUEST Queries into Recommendation Algebra RA

The translation of the core part of the REQUEST query is based on the underlying algebra RA. In particular, the mapping is performed by parsing the query and generating corresponding algebraic operators. The MAP algorithm, presented in Figure $5 ,$ shows how to translate an arbitrary Core-REQUEST query with its specific parameters, such as various aggregations as well as measure or dimension restrictions, into an algebraic expression in RA.

As mentioned earlier, the most general form of the REQUEST query is

REQUEST\_query <sub>=</sub>

RECOMMEND recommend\_dim\_list TO recipient\_dim\_list

USING cube\_name

RESTRICT dimension\_restrictions

PREFILTER preaggregation\_measure\_restrictions

BASED ON aggr\_measure\_list

POSTFILTER postaggregation\_measure\_restrictions

SHOW measure\_rank\_restriction

Based on the input query REQUEST\_query, the MAP algorithm produces a corresponding algebraic expression $R A \_ o p$ in RA. By default, initially RA\_op is assigned the identity operator ID (Line 1), i.e., ID $( c u \bar { b } e ) \equiv c u b e$ for any cube instance. Then, MAP continuously “grows” this initial algebraic expression RA\_op by composing it with newly generated operators in the following way. For notational purposes, we use the symbol to represent the composition of two algebraic operators, i.e., $o p _ { 1 } \oplus o p _ { 2 } ( c u b e ) =$ $o p _ { 2 } ( o p _ { 1 } ( c u b e ) )$ for any cube and any algebraic operators $o p _ { 1 } , o p _ { 2 }$ . In particular, first, MAP checks whether REQUEST\_query has any restrictions on dimensions (Line 2) and, if so, MAP then generates a dimension restriction operator DRSTR with corresponding parameters (Line 3). Second, MAP checks whether REQUEST\_query has any preaggregation restrictions on measures (Line 4) and, if so, it then generates a measure restriction operator MRSTR with corresponding parameters (Line 5). Third, once dimension and measure restrictions are applied, the aggregation is performed next. The measures to be aggregated and their aggregation functions are specified by the user in the BASED ON clause of the query, but first the unused measures (measures that do not appear in this clause) are projected out using operator MRPJ (Lines 6 and 7).

## Figure 5 Mapping Core-REQUEST Queries into RA Expressions

MAP(REQUEST\_query) { (1) $R A \_ o p : = I D$ (2) if (<sub>∃</sub>RESTRICT clause in REQUEST\_query), then (3) RA\_op := RA\_op <sub>⊕</sub> DRSTR<sub>-dimension\_restr</sub> <sub>ictions</sub> (4) if (<sub>∃</sub>PREFILTER clause in REQUEST\_query), then (5) $R A \_ o p : = R A \_ o p \oplus M R S T R _  ( \ i$ preaggregation\_measure\_restr ictions (6) foreach m <sub></sub> aggr\_measure\_list in BASED ON clause (7) $R A \_ o p : = R \bar { A } \_ o p$ <sub>⊕</sub> MRPJ (8) dimension\_aggregations = <sub></sub> (9) foreach $d _ { i } \in \overline { { c u b e } } \_ n a m e$ (10) if d recommend\_dim\_list recipient\_dim\_list, then (11) dimension\_aggregations := dimension\_aggregations <sub>∪</sub> {d .ALL} (12) else if (<sub>∃</sub>x d<sub>i</sub>x <sub>∈</sub>recommend\_dim\_list <sub>∪</sub> recipient\_dim\_list then (13) dimension\_aggregations := dimension\_aggregations <sub>∪</sub> {d .x} (14) measure\_aggregations = <sub></sub> (15) foreach $( m _ { j } , a g g r _ { j } ) \in a g g r _ { - }$ measure\_list in BASED ON clause (16) measure\_aggregations := measure\_aggregations <sub>∪</sub> {m .aggr } (17) $R A \_ o p : = R A \_ o p \oplus A G G R _ { ( \cdot }$ dimension\_aggregations-measure\_aggregations (18) foreach d recommend\_dim\_list recipient\_dim\_list (19) $R A \_ o p : = R A \_ o p \oplus D T D M _ { d }$ (20) if (<sub>∃</sub>POSTFILTER clause in REQUEST\_query), then (21) $R A \_ o p : = R A \_ o p \oplus M R S T R _ { ( }$ postaggregation\_measure\_restr ictions (22) return $R A \_ o p ;$

Subsequently, operator AGGR is generated (Line 17) with parameters dimension\_aggregations and measure\_aggregations, where the former specifies the granularity (or aggregation) levels for all dimensions that need to be grouped (Lines 8–13) and the latter specifies aggregation functions for all measures (Lines 14–16). Fourth, all the irrelevant (and fully aggregated) dimensions, i.e., the dimensions that do not appear in RECOMMEND and TO clauses, are destroyed using operator DTDM (Lines 18 and 19). Fifth, MAP checks whether REQUEST\_query has any postaggregation restrictions on measures (Line 20) and, if so, it then generates a measure restriction operator MRSTR with corresponding parameters (Line 21). Finally, Line 22 returns the resulting algebraic expression RA\_op, and the query results can be obtained by applying RA\_op to the input cube cube\_name specified in the USING clause.

We next explore a formal relationship between the Core-REQUEST queries and RA. To do this, we first introduce some preliminary concepts. Let o be a specific instance of any of the five RA operators, for example, $o = \mathrm { D R S T R } _ { \mathrm { 1 } }$ <sub>-MovieGenre “comedy”</sub>. Given recommendation cube $C ,$ we say that $o$ is a well-defined operation for C if o-C can be successfully performed based on the schema of cube C as well as the dimensions, attributes, and measures specified in operator o. For example, operator $\mathrm { D R S T \bar { R } _ { ( M o v i e . G e n r e = ^ { \prime \prime } c o m e d y ^ { \prime \prime } ) } }$ is well defined for any cube that has dimension Movie with an attribute Genre and is not well defined for any other cube.

The notion of a well-defined operation can be directly extended from a single algebraic operator to sequences of operators. Let s be a sequence of RA operators, $\mathrm { i . e . , } s = \left. o _ { 1 } , \ldots , o _ { n } \right.$ , where each $o _ { i }$ is a specific instance of any of the five RA operators. We say that s is a well-defined operation sequence for cube C if operation $o _ { n } ( o _ { n - 1 } ( . . . ( o _ { 2 } ( o _ { 1 } ( C ) ) ) ) )$ can be successfully performed in the sense that each operator $o _ { i }$ in the sequence is well defined for its input cube: operator $o _ { 1 }$ is well defined for cube $C , \ o _ { 2 }$ is well defined for cube $o _ { 1 } ( C )$ , etc., $\mathbf { i . e . , \ } o _ { i }$ is well defined for cube $o _ { i - 1 } ( . . . ( o _ { 1 } ( C ) ) )$ for each $i = 2 , \ldots , n .$

Lemma 1 (Safe Swap of DRSTR Forward). Let o<sub>DRSTR</sub> be an instance of the DRTSR operator, ${ \cal O } _ { \mathrm { A N Y } }$ be an instance of any of the five RA operators $( i . e . ,$ DRSTR, MRSTR, MRPJ, DTDM, AGGR), and C be a recommendation cube, where $o _ { \mathrm { D R S T R } } ( o _ { \mathrm { A N Y } } ( C ) )$ is well defined. Then, $o _ { \mathrm { A N Y } } ( o _ { \mathrm { D R S T R } } ( C ) )$ is also well defined and $o _ { \mathrm { D R S T R } } ( o _ { \mathrm { A N Y } } ( C ) ) = o _ { \mathrm { A N Y } } ( o _ { \mathrm { D R S T R } } ( C ) )$

Proof. Immediate from the definitions of RA operators. <sup></sup>

Lemma 2 (Safe Swap of DTDM Back). Let $o _ { \mathrm { D T D M } }$ be an instance of the DTDM operator, ${ \cal O } _ { \mathrm { A N Y } }$ be an instance of any of the five RA operators, and C be a recommendation cube, where $o _ { \mathrm { A N Y } } ( o _ { \mathrm { D T D M } } ( C ) )$ is well defined. Then, $o _ { \mathrm { D T D M } } ( o _ { \mathrm { A N Y } } ( C ) )$ is also well defined and $o _ { \mathrm { A N Y } } ( o _ { \mathrm { D T D M } } ( C ) ) = o _ { \mathrm { D T D M } } ( o _ { \mathrm { A N Y } } ( C ) )$

Proof. Immediate from the definitions of RA operators. <sup></sup>

Lemma 3 (Safe Swap of MRPJ Back). Let ${ \cal O } _ { \mathrm { M R P J } }$ be an instance of the MRPJ operator, ${ \cal O } _ { \mathrm { A N Y } }$ be an instance of any of the five RA operators, and C be a recommendation cube, where $o _ { \mathrm { A N Y } } ( o _ { \mathrm { M R P } } ( C ) )$ is well defined. Then, $o _ { \mathrm { M R P } } { ( o _ { \mathrm { A N Y } } ( C ) ) }$ is also well defined and $o _ { \mathrm { A N Y } } ( o _ { \mathrm { M R P J } } ( C ) ) = o _ { \mathrm { M R P J } } ( o _ { \mathrm { A N Y } } ( C ) )$

Proof. Immediate from the definitions of RA operators. <sup></sup>

Theorem 1 (Canonical Form of RA). Let C be a recommendation cube. Then, for any sequence s of RA operators, such that s-C is a well-defined operation, there exists a corresponding canonical sequence s- of the form<sup>2</sup>

$$
s ^ {\prime} = \langle [ \mathrm{DRSTR} ], [ \mathrm{MRSTR} ], (\mathrm{AGGR}, [ \mathrm{MRSTR} ]) ^ {*},
$$

DTDM MRPJ<sub></sub>

(1)

that is equivalent to $s ( C ) , i . e . , s ^ { \prime } ( C ) = s ( C )$ , and where the number of AGGR operators in $s ^ { \prime }$ is equal to the number of AGGR operators in s.

Proof. The proof is provided in the online appendix.<sup>3</sup> <sup></sup>

We next establish the relationship between Core-REQUEST and RA.

Theorem 2. RA is strictly more expressive than Core-REQUEST.

Proof. Obviously, RA is at least as expressive as the Core-REQUEST language, because every Core-REQUEST statement can be expressed in RA using the MAP algorithm. Furthermore, directly from the MAP algorithm, we have that all Core-REQUEST queries are of the following algebraic form: [DRSTR], [MRSTR], [MRPJ], [AGGR], [DTDM], [MRSTR]<sub></sub>. Based on Lemmas 2 and 3 and also on the fact that, in the absence of AGGR operator, PREFILTER and POSTFILTER can be represented as one measure restriction operation (as mentioned in §3), all Core-REQUEST queries can also be expressed by the following equivalent sequence: <sub></sub>[DRSTR], [MRSTR], [AGGR, [MRSTR]], [DTDM], [MRPJ] . Based on Theorem 1, it is clear that RA can produce the expressions of a strictly more general form, i.e., [DRSTR], [MRSTR], (AGGR, [MRSTR])∗, [DTDM], [MRPJ] , where the precise difference in expressive power lies in the RA’s ability to specify multiple <sub></sub>AGGR, [MRSTR]<sub></sub> operator sequences (as opposed to only 0 or 1 such sequences in Core-REQUEST). <sup></sup>

Theorems 1 and 2 explain the difference between expressive powers of RA and Core-REQUEST at the theoretical level: Core-REQUEST allows at most one aggregation operation in a query, while RA supports multiple aggregations because the algebra is closed. For example, in a two-dimensional recommendation application with User and Movie dimensions and one measure, Rating, the following RA expression

$$
\begin{array}{c} \text {AGGR} _ {\text {(User.ALL, Movie.ALL),(Rating.AVG)}} \left(\text {MRSTR} _ {\text {(Rating>7)}} \right. \\ \left(\text {AGGR} _ {\text {(User.Profession, Movie.Genre),(Rating.AVG)}} (\mathrm{C})\right) \end{array}
$$

cannot be expressed in Core-REQUEST.

One way to address the issue that Core-REQUEST is strictly less expressive than RA is to extend REQUEST in such a way that their expressive powers would become equal. According to Theorems 1 and $^ { 2 , }$ this would mean providing support for multiple aggregations (and optional measure restriction capabilities after each aggregation) in REQUEST. One way to achieve this is by supporting an arbitrary number of Core-REQUEST query compositions (e.g., that could be implemented via nested queries). It immediately follows from Theorems 1 and 2 and Lemmas 1–3 that such an extended language would have the same expressive power as algebra RA. Upon careful consideration, however, we decided against this extension when designing REQUEST because multiple aggregations (1) do not occur naturally in recommendation applications, and therefore have a very limited need in the real-world applications and (2) unnecessarily complicate the language design by adding extra complexity needed for allowing an arbitrary number of aggregations. These extensions would make REQUEST significantly less user-friendly without providing tangible benefits. Note also that, aside from these query compositions with two or more aggregation operators (which cannot be expressed in Core-REQUEST), composition of any other Core-REQUEST queries (i.e., having zero or one aggregations among them) can always be expressed in Core-REQUEST, according to Theorem 1, Lemmas 1–3, and the definitions of RA operators.

## 6. Conclusions

In this paper, we introduced language REQUEST for specifying user-driven recommendations. REQUEST queries are formulated on multidimensional cubes of ratings, support OLAP-based aggregation capabilities, are expressed in a simple declarative language capturing idiosyncrasies of recommender systems, and thus provide several advantages to the users of recommender systems. In particular, REQUEST empowers the end-users by letting them customize recommendations by formulating them in the ways that satisfy their individual needs in a flexible and user-friendly manner. Also, unlike SQL, which constitutes a general-purpose database query language, REQUEST is designed specifically for multidimensional recommender systems. Therefore its constructs are developed exclusively for specific recommendation contexts, and every REQUEST query can be directly interpreted as a recommendation. As a result, REQUEST can express complex recommendations in a concise and clear manner. Finally, REQUEST design follows the multidimensional data model and does not depend on any of its particular implementations.

We also presented an OLAP-based recommendation algebra RA, showed how REQUEST recommendations can be expressed in it, and analyzed its expressiveness. Therefore, REQUEST queries can be processed using this mapping similarly to how SQL queries are processed in relational DBMSes. One query processing problem pertaining to recommender systems deals with the determination of which new ratings need to be evaluated to answer a particular REQUEST query, in case the entire cube of ratings cannot be precomputed ahead of time. For example, to answer the query “which movies to recommend to Jane Doe to see on March 5 on Saturday night with her boyfriend in a movie theatre,” the system may not need to estimate all the ratings on the fly in the recommendation cube described in Example 1. Because rating estimation in such cases becomes query dependent, an interesting and challenging problem is to determine the subset of ratings that needs to be estimated to answer a given query. We plan to study this problem in the future.

Finally, it is important to develop a good GUI-based front end to REQUEST, so that naïve end-users would be able to express their user-driven recommendations using this interface. Designing such interface constitutes another topic of our future research.

## Acknowledgments

Research of G. Adomavicius was supported, in part, by the National Science Foundation (NSF) under Grant 0546443. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the NSF.

## References

Adomavicius, G., A. Tuzhilin. 2001. Multidimensional recommender systems: A data warehousing approach. L. Fiege, G. Mühl, U. Wilhelm, eds. Electronic Commerce: Second Internat. Workshop (WELCOM 2001), Lecture Notes in Computer Science, Vol. 2232. Springer-Verlag, Heidelberg, Germany, 180–192.

Adomavicius, G., A. Tuzhilin. 2005a. Incorporating context into recommender systems using multidimensional rating estimation methods. Proc. 1st Internat. Workshop Web Personalization, Recommender Systems and Intelligent User Interfaces (WPRSIU 2005). Reading, UK, 3–13.

Adomavicius, G., A. Tuzhilin. 2005b. Towards the next generation of recommender systems: A survey of the state-of-the-art and possible extensions. IEEE Trans. Knowledge Data Engrg. 17(6) 734–749.

Adomavicius, G., R. Sankaranarayanan, S. Sen, A. Tuzhilin. 2005. Incorporating contextual information in recommender systems using a multidimensional approach. ACM Trans. Inform. Systems 23(1) 103–145.

Agrawal, R., A. Gupta, S. Sarawagi. 1997. Modeling multidi mensional databases. Proc. 13th Internat. Conf. Data Engrg. (ICDE’97), Birmingham, UK, 232–243.

Balabanovic, M., Y. Shoham. 1997. Fab: Content-based, collaborative recommendation. Commun. ACM 40(3) 66–72.

Bennet, J., S. Lanning. 2007. The Netflix prize. Proc. KDD Cup and Workshop 2007 at the 13th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining, San Jose, CA.

Burke, R. 2007. Hybrid Web recommender systems. P. Brusilovsky, A. Kobsa, W. Nejdl, eds. The Adaptive Web: Methods and Strategies of Web Personalization, Lecture Notes in Computer Science, Vol. 4321. Springer-Verlag, Berlin, 377–408.

Ceri, S., G. Gottlob. 1985. Translating SQL into relational algebra: Optimization, semantics and equivalence of SQL queries. IEEE Trans. Software Engrg. 11(4) 324–345.

Chaudhuri, S., U. Dayal. 1997. An overview of data warehousing and OLAP technology. ACM SIGMOD Record 26(1) 65–74.

Cohen, W. W., R. E. Schapire, Y. Singer. 1999. Learning to order things. J. Artificial Intelligence Res. 10 243–270.

Gyssens, M., L. V. S. Lakshmanan. 1997. A foundation for multidimensional databases. Proc. 23rd Internat. Conf. Very Large Data Bases (VLDB-97), Athens, Greece, 106–115.

Hill, W., L. Stead, M. Rosenstein, G. Furnas. 1995. Recommending and evaluating choices in a virtual community of use. Proc. Conf. Human Factors Comput. Systems (CHI’95), Boston, 194–201.

Jameson, A., B. Smyth. 2007. Recommendation to groups. P. Brusilovsky, A. Kobsa, W. Nejdl, eds. The Adaptive Web: Methods and Strategies of Web Personalization, Lecture Notes in Com puter Science, Vol. 4321. Springer-Verlag, Berlin, 596–627.

Koutrika, G., R. Ikeda, B. Bercovitz, H. Garcia-Molina. 2008. Flexible recommendations over rich data. Proc. 2008 ACM Conf. Recommender Systems (RecSys’08), Lausanne, Switzerland, 203–210.

Li, C., X. S. Wang. 1996. A data model for supporting on-line analytical processing. Proc. 5th Internat. Conf. Inform. Knowledge Management (CIKM-1996), Rockville, MA, 81–88.

Marcel, P. 1999. Modeling and querying multidimensional databases: An overview. Networking Inform. Systems J. 2(5) 515–548.

Mild, A., T. Reutterer. 2001. Collaborative filtering methods for binary market basket data analysis. Lecture Notes in Computer

Science, Vol. 2252. Springer, Berlin/Heidelberg, Germany, 302–313.

Miller, B. N., I. Albert, S. K. Lam, J. A. Konstan, J. Riedl. 2003. MovieLens unplugged: Experiences with an occasionally connected recommender system. Proc. Internat. Conf. Intelligent User Interfaces, Miami, 263–266.

Resnick, P., N. Iakovou, M. Sushak, P. Bergstrom, J. Riedl. 1994. GroupLens: An open architecture for collaborative filtering of netnews. Proc. 1994 ACM Conf. Comput. Supported Cooperative Work, Chapel Hill, NC, 175–186.

Shardanand, U., P. Maes. 1995. Social information filtering: Algorithms for automating “word of mouth.” Proc. Conf. Human Factors Comput. Systems, New York, 210–217.

Snodgrass, R. 1987. The temporal query language TQuel. ACM Trans. Database Systems 12(2) 247–298.

Thomas, H., A. Datta. 2001. A conceptual model and algebra for online analytical processing in decision support databases. Inform. Systems Res. 12(1) 83–102.

Umyarov, A., A. Tuzhilin. 2008. Improving collaborative filtering recommendations using external data. Proc. IEEE Internat. Conf. Data Mining (ICDM-2008), Pisa, Italy, 618–627.

Wade, W. 2003. A grocery cart that holds bread, butter and preferences. New York Times (January 16) E6.
