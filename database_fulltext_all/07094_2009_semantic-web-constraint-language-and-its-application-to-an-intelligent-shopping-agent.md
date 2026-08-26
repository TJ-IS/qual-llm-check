---
otero_id: 7094
otero_key: "DM2WAAR3"
title: "Semantic Web Constraint Language and its application to an intelligent shopping agent"
authors: "Hak-Jin Kim; Wooju Kim; Myungjin Lee"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.12.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Semantic Web Constraint Language and its application to an intelligent shopping agent

Hak-Jin Kim <sup>a,1</sup>, Wooju Kim <sup>b,</sup>⁎, Myungjin Lee <sup>b,2</sup>

<sup>a</sup> School of Business, Yonsei University, 134 Shinchon-dong, Seodaemoon-ku, Seoul, 120-749, South Korea

<sup>b</sup> Dept. of Information and Industrial Engineering, Yonsei University, 134 Shinchon-dong, Seodaemoon-ku, Seoul, 120-749, South Korea

## a r t i c l e i n f o

Article history: Received 3 December 2007 Received in revised form 2 December 2008 Accepted 12 December 2008 Available online 25 December 2008

Keywords: Semantic Web Constraints Optimization Decision making SWCL Internet shopping agent

## a b s t r a c t

Semantic Web society was initially focused only on data, but then gradually moved toward knowledge. If a vision of the Semantic Web is to enhance humans' decision-making assisted by machines, a missing but important part is knowledge about constraints on data and concepts represented by ontology. This paper proposes a Semantic Web Constraint Language (SWCL) based on OWL, and shows its effectiveness in representing and solving an internet shopper's decision-making problems by implementing a shopping agent in the Semantic Web environment.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Since Tim Berners-Lee initiated the idea of the Semantic Web, it has progressed fast along the trail he depicted in the Semantic Web "Layer Cake," and its ontology layers, based on RDF, RDF Schema, and OWL, have been almost stabilized. Despite this growth, OWL [32] — which intends to represent terms and their interrelationships with ontology — still has limitations in the representational power. A logic and rule layer was supposed to be a way to extend it. One of the choices for this logic layer was a Semantic Web Rule Language (SWRL), which was submitted as a recommendation to W3C in 2004 [17]. SWRL was designed to extend OWL's representational power by combining Horn-like rules with OWL. Two more noticeable rule languages are Semantic Web Service Language (SWSL) [3] and Web Rule Language (WRL) [1] that incorporate higher logics into the Semantic Web. The recent move of W3C in Rule Interchange Format (RIF) Working Group is about to produce a core rule language, which allows rules to be shared among rule systems. This activity seems to allow not only data, but also richer knowledge such as rules, to be sharable and reusable across application, enterprise, and community boundaries.

The vision which all the above attempt to achieve is to enhance human's decision-making quality in the context of the current web environment. This implication is partly revealed in Jim Hendler's speech of ISWC 2003 [16]. Decision making inevitably accompanies a target problem and the problem usually consists of a goal, a model, and data. In this perspective, the current state of the Semantic Web is not yet able to address how to represent goals and models suf<sup>fi</sup>ciently. Rule or logic might be seen as one of the models from this point of view. To solve the problems people or organizations face in the Web environment, a practical means to represent problems should be provided.

Constraint has traditionally been another backbone of human knowledge representation together with logic, and the inclusion of this missing piece must strengthen the representational power of the current Semantic Web. The great need for handling constraints in the Semantic Web environment has already been raised by [29], where the authors only dealt with such simple constraints as represented by modi<sup>fi</sup>ed built-in functions. The <sup>fi</sup>rst formal approach proposed to deal with constraints in OWL was [33] which will be discussed later in detail. Its theoretical foundation was greatly dependent on First Order Logic (FOL), in that the constraints that only conform to logic were suggested in their proposal. This makes its approach inadequate for handling that other most important part of constraints, arithmetic constraints. Arithmetic constraints are essential if decision making with classical optimization problems — which have traditionally been expressed with them — is intended to be included in the Semantic Web environment. Additionally, the proposed approach considers the decision problems of satis<sup>fi</sup>ability with no goals. The need for methods to handle mathematical optimization problems with goals is not an idiosyncratic matter, but a signi<sup>fi</sup>cant issue that we may face in everyday decision making. B2B e-procurement [38], resource allocation shared over the Web [15], and order ful<sup>fi</sup>llment on the Value Web [19,24] are canonical application areas where we need to handle optimization problems and exchange a great number of arithmetic constraints over the Web.

Our research objective is to complement existing methods by extending them beyond their limitations to handle mathematical optimization problems in the Semantic Web environment. To achieve this goal, this paper <sup>fi</sup>rst proposes a Semantic Web Constraint Language (SWCL) compatible with OWL. Next, it shows how the proposed SWCL can represent an internet shopper's problem in the real world and contribute to solving that problem by an implementation of a shopping agent that understands semantic information with OWL and SWRL.

The following section describes related works. Section 3 introduces SWCL and its abstract syntax and semantics. How SWCL can be applied to representing an internet shopper's problem, along with OWL and SWRL, will be explained in section 4. Section 5 discusses a brief design and issues in developing a shopping agent, which solves the shopper's problem by using OWL, SWRL, and SWCL. Conclusions will be presented comes in the <sup>fi</sup>nal section.

## 2. Related works

The Resource Description Framework (RDF) [6,27] is a language for representing information about resources in the World Wide Web. It is particularly intended for representing metadata about Web resources, for example, titles, authors and modi<sup>fi</sup>cation dates of Web pages, copyrights and licensing information of Web documents, and availability schedules for some shared resources. The generalization of the concept of “Web resource” extends the usefulness of RDF to representing information on any object that can be identi<sup>fi</sup>ed on the Web, even when it cannot be directly retrieved on the Web. RDF is based on the idea that objects may be identi<sup>fi</sup>ed by using Web identi<sup>fi</sup>ers, Uniform Resource Identi<sup>fi</sup>ers (URIs), and described in terms of simple properties and their values.

The Web Ontology Language (OWL) was designed to process the information content in applications, rather than to represent information in a form readable to human beings. It uses an abstract conceptual structure, called ontology, to explicitly represent the meanings of terms in vocabularies and the relationships between those terms. It extends machine interpretability of Web contents, supported by XML, RDF, and RDF Schema (RDF-S) [6], by providing additional vocabularies along with formal semantics. Although OWL adds considerable expressive power to the Semantic Web, it has limitations in expressiveness, particularly concerning how to express properties. Some believe that a way to overcome this might be to de<sup>fi</sup>ne properties as general rules such as Horn rules. Such integration of rule-based knowledge representation with DL-style knowledge representation is currently an active area of research.

Semantic Web Rule Language (SWRL) is a proposal for rule languages in the Semantic Web based on a combination of the OWL DL and OWL Lite, with the sublanguages of Rule Markup Language and Unary/Binary Datalog RuleML [4]. The proposal extends the set of OWL axioms to include Horn-like rules, and thus enables Horn-like rules to be combined with an OWL knowledge base. The proposed rules are the form of an implication between the antecedent (body) and the consequent (head). The intended meaning of the form can be read as: whenever the conditions speci<sup>fi</sup>ed in the antecedent hold, then the conditions speci<sup>fi</sup>ed in the consequent must also hold. The combination of OWL and Horn rules results in the creation of a highly expressive language. Still, there are reasons the proposal is not complete, and the language fails to represent accurately knowledge in our world. In particular, it fails in representing indistinct and imprecise knowledge and information [21], and lacks representing constraints knowledge.

Constraints are a new paradigm in computer programming, in which the relationships of variables of objects are represented with constraints. According to [21], constraints have been recognized as a very useful problem-solving paradigm in the Semantic Web. For instance, the agent architecture KRAFT, proposed in [37], explains fully the importance of constraints in an open and distributed knowledge system. This architecture, triggered by a user's request, <sup>fi</sup>rst locates appropriate on-line sources of knowledge; transforms heterogeneous knowledge into homogeneous constraints using interchange formats, namely Constraint Interchange Format (CIF); fuses the constraints with associated data and forms a constraint satisfaction problem dynamically; and <sup>fi</sup>nally feeds the problem to a local existing constraint solver to solve the problem and return the solution to the user. [33] argues that SWRL is not appropriate in this situation to ful<sup>fi</sup>ll user requests, and that an extension of SWRL, purely based on RDF and RDFS, is needed with proposing CIF. (See [33] for detailed arguments on why constraints are needed.) CIF was claimed to be expressive enough to encode constraints since it is basically an XML translation and encoding method of a constraint language for OODB, namely Colan [2]. Colan is known to be based on classical range-restricted FOL with the usual logical connectives (and, or, not), and mainly uses uni<sup>fi</sup>cation and pattern matching for resolving constraints. As these papers have argued, the main advantage in using constraints is that knowledge need not be embedded as a procedure in local database software, but can be transmitted on a network because constraints are declarative. When we consider transmitting a sales policy rule, for instance, it is usually hard to handle because traditional language paradigms express a rule with a procedure, not with data. Constraint paradigm facilitates it. [39] shows an advantage of the constraint paradigm by using soft constraints in the CIF approach.

The CIF approach does not harness the full power of constraints, however. As mentioned previously, CIF depends on uni<sup>fi</sup>cation and pattern matching of Colan in its solution methods. Because Colan originally purported to be used with database systems, this origin limits its expressive power to logical symbols and statements, and its solution methods to uni<sup>fi</sup>cation and pattern matching. On the other hand, many Semantic Web applications require solving a variety of decision problems, not only feasibility but optimization problems. The <sup>fi</sup>eld of mathematical programming has experienced such problems and produced a variety of techniques to handle them. Recently, the <sup>fi</sup>eld of constraints has also become interested in techniques for optimization problems from Operations Research (OR) and even tries to combine those with their own techniques [28]. We therefore believe that providing a different <sup>fl</sup>avor of constrains, arithmetic constraints, which can easily access the decision-modeling tradition in OR, might help to strengthen the applicability of Semantic Web technology. The approach proposed in this paper is complementary to the CIF approach rather than contradictory, because this paper is suggesting different types of constraints to be embedded in the extension of SWRL. While the CIF approach is basically dependant on Colan and interested in solving CSP problems, SWCL is employed to embed techniques from the conventional mathematical programming <sup>fi</sup>eld and is interested in solving optimization problems.

It is currently not easy to see practical applications using the current state of Semantic Web technology because the fusion of reasoning techniques with the Semantic Web is still seminal and needs to be mature. As a related practical work, [20] used representing and reasoning for protein structures in biomedical applications to process data resources remotely. Semantic Web technology might make the process in such a situation <sup>fl</sup>uent and seamless without clutter. Also, [11] used the KRAFT framework and exchanged knowledge based on a shared data model and a shared ontology for the data service network of British Telecommunications.

The last relevant work, related to embedding a modeling framework within the Semantic Web, is model management systems (MMS). Many solution techniques in the OR <sup>fi</sup>eld for decision problems are often incomprehensible to practitioners and require manual selection and modi<sup>fi</sup>cation to apply to different situations even with similar structures. The decision support system <sup>fi</sup>eld has been to identify models as an integral part of an information system as data in database systems [10]. In particular, Geoffrion's Structured Modeling scheme [12,13] has provided an idea of how to express a model as data. His basic idea is to separate model and instance structures and problems data, and may help to construct a knowledge database. Other relevant ideas about MMS [8,9,30,44] might be useful for the future of the Semantic Web.

## 3. A Semantic Web Constraint Language (SWCL)

A <sup>fi</sup>eld of decision science, the model management society, has made a great effort to represent constraints in an abstract level and to associate it with data models such as databases. What they ultimately hope to achieve is to allow human beings, regardless of what software and hardware platforms they are using, to manage and manipulate various mathematical decision models in a more abstract and seamless manner than before [23,25,46]. The same thing is required currently in the Semantic Web as mentioned in section 1. This section proposes a Semantic Web Constraint Language (SWCL) based on OWL to combine constraints with an OWL knowledge base in an abstract level.

Fig. 1 shows a document in OWL for representing population in geometrical regions, and demonstrates the necessity of SWCL. Suppose there are two OWL classes, “Country” and “Province,” with two related properties, “hasPart” and “populationValue.” “hasPart” property denotes the relationship that “Province” is a part of “Country” and “populationValue” the number of inhabitants in a region. It is expressed as Fig. 1 in an OWL document.

It is obvious as a knowledge that the population of each country should be equal to the sum of the populations of the provinces which belong to that country.

∑ x:populationValue = y:populationValue; for all yaCountry 1 xay:hasPart

When a.b stands for the value of property b of an instance a, we might represent the knowledge as a formal constraint (1). OWL and SWRL are not suf<sup>fi</sup>cient for expressing such a mathematical constraint. SWCL may serve to <sup>fi</sup>ll the gap.

## 3.1. Abstract syntax

To facilitate access to constraints and evaluation of their expressions, the syntax for SWCL in this section extends the abstract syntax of OWL described in the OWL Semantics and Abstract Syntax document [36], together with additional axioms for constraints as in SWRL [17]

An abstract syntax will be speci<sup>fi</sup>ed here by means of a version of Extended BNF, very similar to the EBNF notation used for XML [5]. Terminals are quoted, and non-terminals bold and not quoted. Alternatives are either separated by vertical bars (|) or given in different productions. Components that occur at most once are enclosed in square brackets ([…]); those which occur any number of times (including zero) are in braces ({…}). White space is ignored in productions here.

An OWL ontology in the abstract syntax level contains a sequence of axioms and facts. Its axioms may be of various kinds, for example “subclass” and “equivalentClass” axioms. It is proposed that this be extended with constraint axioms. The following is the fundamental constraint axiom.

![](/api/attachments/DM2WAAR3/fulltext/images/bf6fdc334a9d84dc4927ed27ff685663bdfb854913dc966c2d8a35b7e38d9c93.jpg)  
Fig. 1. OWL document for representing population.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
factor(c p)
    $y \in O: \langle x, y \rangle \in ER(p) \land x \in EC(c)$

factor(i p)
    $y \in O: \langle x, y \rangle \in ER(p) \land x \in EC(i)$

termBlock(sign aggregateOperator parameter factor$_{1}$ ... factor$_{n}$)
    $y \in O$ $y = 'x'(sgn(sign), aggregateOperator(\forall \langle x_1, ..., x_n \rangle \in \prod_{i=1}^{n} EC(c_i)$
    '$x'(factor_1(x_1p_1), ..., factor_n(x_np_n)))$)
</div>

axiom ::=constraint

A constraint axiom consists of four elements: quali<sup>fi</sup>er, LHS (lefthand side), operator, and RHS (right-hand side). URIreference may be optionally added to identify the constraint.

```txt
constraint ::= 'Constraint('[URIreference]{qualifier} LHS operator RHS')
qualifier ::= 'Qualifier(' variable | description ')
variable ::= 'Variable(' description ')
LHS ::= 'LHS(' termBlock { termBlock } ')
operator ::= 'equal' | 'notEqual' | 'lessThan' | 'lessThanOrEqual' | 'greaterThan' | 'greaterThanOrEqual'
RHS ::= 'RHS(' termBlock { termBlock } ')'
```

LHS and RHS consist of one or more term blocks, termBlock, each of which is the term of a constraint. In constraint (1), LHS is a term block, ∑<sub>x∈y.hasPart</sub> x.populationValue, and RHS another term block, y.populationValue, while the quali<sup>fi</sup>er and operator are “Country” and ‘equal, respectively. “description,” including class identi<sup>fi</sup>ers and restrictions, is de<sup>fi</sup>ned in [36].

```txt
termBlock ::= 'TermBlock(' sign [aggregateOperator] { parameter }
    factor { factor }�')
sign ::= '+' | '-''
aggregateOperator := 'Sigma' | 'Production'
factor ::= 'Factor((' classID datavaluedPropertyID ) | ( individualID
    datavaluedPropertyID )�')
parameter ::= 'Parameter('variable | description�')
```

Ontologies incorporate information about classes, properties, and individuals, each of which can have an identi<sup>fi</sup>er of a URI reference. A factor in term block can be a class or a property name which is a URI reference [36]. In constraint (1), the LHS has only one termBlock that consists of a sign, ‘+,’ an aggregateOperator, ‘Sigma,’ a parameter, Country.hasPart, and a factor, Province.populationValue. aggreateOperators and parameters can be omitted depending on the situation. This is the case of RHS in (1), where RHS consists of only a sign, ‘+’ and a factor, Country.populationValue.

## 3.2. Direct model-theoretic semantics

The model-theoretic semantics for SWCL is a straightforward extension of the semantics for OWL given in the OWL Semantics and Abstract Syntax document [36]. Factors in a constraint may be classi<sup>fi</sup>ed into four groups: constants C, factors P used in parameters, factors Q used in quali<sup>fi</sup>ers, and factors V used as variables in a constraint solver. 〈a,b〉 is used to denote an ordered pair of a relation, and ‘×’ and ‘+’ are functions of multiplication and addition.

where ‘sgn’ is a function that has value 1 if sign is $" + "$ and value −1 if “−”.

LHS(termBlock … termBlock )

$$
y \in O: y = ^ {\prime} + ^ {\prime} (t e r m B l o c k _ {1}, \dots , t e r m B l o c k _ {n})
$$

$$
y \in O: y = ^ {\prime} + ^ {\prime} (t e r m B l o c k _ {1}, \dots , t e r m B l o c k _ {n})
$$

constraint(qualifier LHS operator RHS)

$$
\{V \in D (V) \mid \forall Q \in D (Q) L H S (V) o p e r a t o r R H S (V) \}
$$

where D(V) and D(Q) are the domains of factor items.

## 3.3. RDF concrete syntax

RDF Concrete Syntax is based on RDF Concepts and Abstract Syntax [22]. Constraint (1) may be written in Fig. 2 in the form of an SWCL document.

## 4. A Description of an internet shopper's problem

This section is intended to show how SWCL can help us represent a real-world Internet shopping problem with OWL, and also what advantages can be derived from using SWCL. Now suppose a shopper intends to shop for CDs at multiple Internet shopping malls. The task usually starts with using a search engine. The shopper types the titles of CDs or their descriptions into a search engine. Mostly, any current search engine will then display too much data for the shopper to browse or to decide where to buy.

The problem in this situation is caused by the fact that the usual search method is based on the process of <sup>fi</sup>nding text containing matched words or phrases, but search engines really do not understand the results of searches. One plausible remedy may be to incorporate Semantic Web technologies into the search mechanism [7,26] which will naturally enhance the precision of information retrieval. Obtaining good candidate products to purchase through such enhancements, however, is not enough for making good shopping decisions because there are still too many factors to be considered. So far, OWL is suf<sup>fi</sup>cient to realize the ontology-based search approach.

A sample ontology required for this shopping case is depicted in Fig. 3. It has eight classes with their related properties. Class CDs describes all CDs which are sold by class Mall, i.e. in all malls. Class ProductInMall contains information about the price of a CD sold in a mall, and class ShoppingItems information about a shopping list of a set of CDs in class ProductInMall. Class ProductOrder provides information about the total payment for a CD, and class PurchaseIn-Mall lists CDs sold in a mall with the subtotal costs. Class OrderList provides information for a shopper's shopping result such as the total purchase amount including delivery cost and discount rate. The data type properties are shown as boxes, and object properties as <sup>fi</sup>lar boxes. For example, in class ProductInMall, an object property hasMall has an instance of class Mall, and a datatype property hasMallSellingPrice is the sales price about a product in a shop. These concepts are designed from the perspective of an information intermediary, that is, a shopping agent.

What burdens shoppers more in decision making is that there are many internet shops which sell the same products with different prices under different conditions. In fact, list prices on products at a shopping site may not be the shopper's only concern in making a shopping decision. Differing sales polices from various shopping sites should also be taken into consideration to make the best shopping decision. Each shopping site has and uses its own sales policies as part of its corporate strategy because they are convenient tools for differentiating the company from others. The entries concerning sales policies, such as on refund policy, delivery policy, discount policy, and product package policy, are so complicated that they may confuse many shoppers.

Fig. 4 shows a real world delivery policy excerpted from a leading shopping site in Korea, CDPark. The picture on the left of Fig. 4 shows a screen shot of the delivery policy of CDPark and the one on the right its interpretation in a more readable form. As seen in the <sup>fi</sup>gure, CDPark offers free deliveries if the total amount of the purchase is 20,000 Korean Won or more. Otherwise they charge 1000 Korean Won for delivery.

![](/api/attachments/DM2WAAR3/fulltext/images/c135d2e26d6c95c8f123bed76ba405f4877c76da0580e34faff206ad48162f9b.jpg)  
Fig. 2. An illustration of SWCL document for constraint (1).

The variety of sales policies at many shopping malls actually interferes with a shopper's ability to make good shopping decisions. Fortunately, SWRL can be used to represent formally and publish outside such sales policies so that a computer agent can understand each shopping mall's sales policies. In this case, the computer shopping agent may consider not only list prices, but also sales policies such as delivery rate, and inform shoppers of eventual purchase costs.

Fig. 5 shows a SWRL document representing some of sales policies of CDPark shopping site in conjunction with the ontology depicted in Fig. 3. The <sup>fi</sup>rst three rules describe the delivery policy in Fig. 4 and the remaining two rules outline the additional discount policy of CDPark. The discount policy says that if the total amount of purchase at CDPark is 25,000 Korean Won or more, the mall will give a discount 2000 Korean Won. Otherwise no discount is given.

![](/api/attachments/DM2WAAR3/fulltext/images/a6a194d81efea3bfedc52b84d187b3d520fb717e4e24790ebeabb90ad725a1f0.jpg)  
Fig. 3. A sample ontology for the internet shopper's problem

After collecting all relevant product information, a shopper should determine his or her optimal choice. That is, when a shopper wants to buy more than one of an item for multiple products, he or she needs to determine how much to purchase of each item, and from what shopping sites, in order to make the optimal purchase. This kind of decision-making is not just restricted to the domain of B2C commerce. It could also occur seriously in the context of B2B commerce. The problem the shopper faces is a canonical optimization problem. Therefore constraints from the problem description ought to be identi<sup>fi</sup>ed and represented. SWCL is basically required for this purpose.

![](/api/attachments/DM2WAAR3/fulltext/images/a6bdb3d56ccfcb8a246355d9fb581286f3ca350347397e4408f80bef1619f062.jpg)  
Fig. 4. A delivery policy excerpted from a shopping site, CDPark in interpark.

![](/api/attachments/DM2WAAR3/fulltext/images/db1bd4a89a43a12af014c484cb3922a4c44b719b6f7f1c0aca0e475e7a1851b8.jpg)  
Fig. 5. A sample SWRL document for the CDPark's sales policies.

In our example, six constraints can be identi<sup>fi</sup>ed from the ontology for the shopper's problem as shown in Fig. 2. For the sake of convenience they are described in the same way as Eq. (1).

OrderList:totalPayment = OrderList:totalPaymentPerItem + PurchaseInMall:totalDeliveryRate − PurchaseInMall:totalDiscountRate

$$
\text { OrderList.totalPaymentPerItem } = \sum \text { PurchaseInMall.subTotalInMall } \tag {3}\tag{2}
$$

PurchaseInMall:totalDeliveryRate = ∑Mall:hasDeliveryRate

ð<sup>4</sup>Þ

PurchaseInMall:totalDiscountRate = ∑Mall:hasDiscountRate

ð<sup>5</sup>Þ

PurchaseInMall:subTotalInMall =

∑ ProductInMall:hasMallSellingPrice×ShoppingItems:hasQuantityInMall

ð<sup>6</sup>Þ

ProductOrder:purchaseQuantity = ∑ShoppingItems:hasQuantityInMall

ð<sup>7</sup>Þ

Constraint (2) in the shopper's problem ontology implies that the shopper's <sup>fi</sup>nal total payment for the purchase should be equal to the sum of the total payment for all products to be purchased and the total delivery cost minus additional discounts, if any. Constraint (3) means that the amount paid for the products is the sum of the subtotals the shopper pays at each mall. Each subtotal is expressed in constraint (6) as the sum of the products at the list price of each item and the quantity to purchase. The fact that the total delivery cost is the same as the sum of delivery costs incurred in each shop is obtained in constraint (4), while constraint (5) explains the same for the discount. Finally, constraint (7) means that the purchased amount of each product should be equal to the sum of the purchased amount of the product from each shop. The whole SWCL document for these constraints can be found at bhttp://iwec.yonsei.ac.kr/swcl/shoppingproblem.swclN. Due to lack of space we have not included the detailed SWCL-based representation here.

## 5. Development of an intelligent shopping agent using SWCL

This section proposes a shopping decision-making framework based on the Semantic Web to solve our scenario problem and shows how it is implemented.

## 5.1. A framework for intelligent shopping decision making

The framework for shopping decision-making in this section consists of <sup>fi</sup>ve components and three major information stores. Fig. 6 shows the overall framework and components with a depiction of major information <sup>fl</sup>ows. According to Simon [41], the decisionmaking process is described as four consecutive stages: intelligence, design, choice, and implementation. O'Keefe and McEachern [35] rede<sup>fi</sup>ned the process particularly as it relates to consumer decisionmaking with <sup>fi</sup>ve stages: need recognition, information search, evaluation, purchase, and after-purchase evaluation. From the perspective of O'Keefe and McEachern, our framework supports the second and third of the <sup>fi</sup>ve stages, information search and evaluation, and they correspond to Simon's design and choice, respectively. As shown in Fig. 6, a shopping agent's function is twofold. One consisting of SPARQL [40] processor and OWL/Rule reasoner [18,31,42,45] works for information search. The other part of the decision-making model manager takes charge of evaluation. The shopping agent console basically performs the job of user interface to the customer, and assigns tasks to the relevant component, SPARQL processor and decision-making model manager. Since ontology-based information search issues have been discussed in many studies, this paper reviews the information search stage brie<sup>fl</sup>y, and instead focuses more deeply on the evaluation stage.

To implement the information search step, this study adopts ARQ for the SPARQL processor and Jena [31] for OWL/Rule reasoner. A shopper might make a query about the required product by using our SPARQL compatible GUI. Then the shopping agent console generates the corresponding SPARQL query and passes it to a SPARQL processor. The SPARQL processor next retrieves the relevant product list via an OWL/ Rule reasoner. At this step, an OWL/Rule reasoner such as one found in Jena can consider the related SWRL rules in its query processing.

Once the shopping agent collects OWL facts on the product list and prices and SWRL rules on the sales policies of shopping malls, as shown in Fig. 6, the shopper decides what products to buy based on that knowledge. The shopper moves, after that, to the decision of where to buy the selected products to ful<sup>fi</sup>ll the decision goal he or she set, such as minimization of total payment. For this concern the shopper oughts to present the decision goal to the shopping agent console, which passes it to the decision-making model manager. The decision-making model manager next identi<sup>fi</sup>es and constructs a relevant decision model from the goal by using the context information represented in OWL, SWRL, and SWCL. It <sup>fi</sup>nally invokes an optimization solver to solve the model. The shopping agent is implemented as a JAVA application with Jena [31] managing the RDF processing. Jena is a Java framework for building Semantic Web applications that provides a programmatic environment for RDF, RDFS, OWL, and SPARQL, and includes a rule-based inference engine. It is used to perform OWL DL reasoning at the ontology level, as a part of the task of assembling candidate instances in the solution process. The mathematical decision model formulated from OWL, SWRL and SWCL is passed to an optimization solver, ILOG OPL Development Studio [14]. ILOG OPL Development Studio provides methods to build optimization models ef<sup>fi</sup>ciently, and state-of-the-art applications for the full range of planning and scheduling problems.

![](/api/attachments/DM2WAAR3/fulltext/images/052247f38df5282f359bae1181f05c4c7800bb9b675aa5084b655aaf0c76cbe4.jpg)  
Fig. 6. A framework for intelligent shopping agent using SWCL.

## 5.2. Decision-making model identification

The decision-making model manager performs two major tasks: the identi<sup>fi</sup>cation of a decision-making model and the generation of an optimization model; the latter will be discussed in the next subsection. The identi<sup>fi</sup>cation process of a decision-making model consists of four consecutive steps: 1) goal identi<sup>fi</sup>cation, 2) constraint identi<sup>fi</sup>cation, 3) decision variable identi<sup>fi</sup>cation, and 4) optimization model identi<sup>fi</sup>cation.

1) Goal identi<sup>fi</sup>cation. This step identi<sup>fi</sup>es the shopper's decision goal for purchasing products. Fig. 7 shows the screenshot for this step. As shown in the <sup>fi</sup>gure, the shopper determines the purchasing amount of each product selected, and con<sup>fi</sup>gures the optimization directives: an optimization instruction and an optimization target. “Minimize” and “Orderlist.totalPayment” are selected as the optimization instruction and target in the <sup>fi</sup>gure, respectively. This is called objective factor for later reference.

2) Constraint identi<sup>fi</sup>cation. Once a goal is given, it is straightforward to extract relevant constraints. First, identify a constraint which has the goal as a “factor”; in terms of SWCL, a “factor” of the “termBlock” belonging to the constraint. Then put all other factors appearing in the constraint into the relevant factor set. Next, search for all constraints containing each newly added factor in the relevant factor set, and continue this process until there are no more factors to be added to the relevant factor set. After <sup>fi</sup>nishing this step, the relevant constraint set to the problem is obtained. Fig. 8 shows the constraints identi<sup>fi</sup>ed through this process for our example problem. Each constraint is denoted with the number of the corresponding formula mentioned before.

![](/api/attachments/DM2WAAR3/fulltext/images/109cb03404070ac8ef4f18acee6cf2b6bbd77606faca2b75ff2b19f86eec6b6a.jpg)  
Fig. 7. A screenshot for goal identi<sup>fi</sup>cation step

3) Decision variable identi<sup>fi</sup>cation. As a byproduct of constraint identi<sup>fi</sup>cation, we obtained a relevant factor set. In our problem, it is {totalPayment, totalPaymentPerItems, subTotalInMall, totalDeliveryRate, totalDiscountRate, hasMallSellingPrice, purchaseQuantity, hasQuantityInMall, hasDeliveryRate, hasDiscountRate}, where their domain class names are omitted. All the factors in this relevant factor set are initially candidates for decision variables. For each factor, we <sup>fi</sup>rst examine whether its value is available as a form of the literal from the OWL base. If that is the case, the factor is named a “constant” factor; otherwise, it is still regarded as a candidate decision variable. In the example problem, two constant factors, hasMallSellingPrice and purchaseQuantity, are found and removed from the candidates for decision variable.

The next step in decision variable identi<sup>fi</sup>cation is to examine whether a factor can be determined as “constant” by using SWRL rules. To do this, search for SWRL rules which have heads containing the factor and then apply those rules based on OWL. If a literal value for the factor is obtained by these rules, this factor is also classi<sup>fi</sup>ed as a constant factor.

In the case where a factor value cannot be directly determined by the application of rules, it is necessary to investigate further whether the value of the factor can be determined by the other candidate factors for decision variables. If the body of a SWRL rule can be interpreted as an interval value of a candidate decision variable factor, and the value of a candidate decision variable factor in its head can be determined by the candidate decision variable factor of the body, this can be handled by transforming the SWRL rule to the corresponding formuation. This issue will be discussed in more detail in section 5.3. In this step, if a factor satis<sup>fi</sup>es such a condition, it is called a stepwise constant factor and is handed over to the next step with relevant SWRL rules. In our case, hasDeliveryRate and hasDiscountRate are identi<sup>fi</sup>ed as stepwise constant factors with the SWRL rules in Fig. 5.

4) Optimization identi<sup>fi</sup>cation. Through the above three steps, we now have a relevant constraint set, a decision variable factor set, a constant factor set, a stepwise constant factor set, and the related SWRL rules. In the optimization identi<sup>fi</sup>cation step, an agent classi<sup>fi</sup>es what kind of programming model the given problem is (e.g., linear programming problem, integer programming problem, etc.). To see if the description can be formulated as a mixed integer programming model, it is enough to check whether every termBlock has only one decision variable factor, while the others are all constant factors or stepwise constant factors. If this condition is satis<sup>fi</sup>ed, then go to the optimization generation step in section 5.3; otherwise, stop the process and notify the shopper that the decision goal cannot be evaluated. Our example problem satis<sup>fi</sup>es this condition. This step fundamentally depends on what kinds of solvers are provided. Since this paper assumes a solver that is able to handle only linear functions, if the structure of generated constraints is not linear, the process stops.

![](/api/attachments/DM2WAAR3/fulltext/images/848f6e825dd9309f9221e5d51e22c135b22d3992c20224e0b34f753097652e13.jpg)  
Fig. 8. Identi<sup>fi</sup>ed constraints relevant to the selected goal (OrderList.totalPayment).

```javascript
{string} Mall = ...;
{string} CDs = ...;
float hasMallSellingPrice[Mall][CDs] = ...;
dvar float+ subTotalInMall[Mall];
dvar int+ hasQuantityInMall[Mall][CDs];
forall(i in Mall) {
    subTotalInMall[i] == sum(j in CDs) hasMallSellingPrice[i][j] * hasQuantityInMall[i][j];
};
```  
Fig. 9. Translated OPL statement from the constraint (6).

## 5.3. Optimization model generation and problem solving

This section will explain how to solve the problem at hands practically. To solve the identi<sup>fi</sup>ed optimization problem, we need to choose a speci<sup>fi</sup>c solver and understand its own language to de<sup>fi</sup>ne problems. This study uses ILOG OPL Development Studio as an optimization model solver [14] — which internally uses ILOG CPLEX as the mathematical programming engine — and we have limited our scope to the mixed integer linear programming model.

To obtain a solution with ILOG OPL Development Studio, the problem identi<sup>fi</sup>ed with OWL, SWRL and SWCL should be translated into OPL statements. This translation task is quite straightforward with the constructs in the relevant constraint set, the decision variable factor set, and the constant factor set. For each relevant constraint, the agent writes the corresponding OPL statement and then adds required decision variables and data declarations. Parameters and quali<sup>fi</sup>ers are also converted into the corresponding indices and quali<sup>fi</sup>ers in OPL. For example, the OPL statement translated from the constraint depicted in formula (6) appears in Fig. 9.

A problem still remains in dealing with the stepwise constant factor set such as the factors, hasDeliveryRate and hasDiscountRate, because from the point of view of a modeling language, integer programming doesn't have any primitive components to handle the stepwise structure. The Operations Research community uses a constructive trick to cope with the case of piecewise linear functions [34]. With a small modi<sup>fi</sup>cation, the stepwise structure can be handled easily. Since this trick requires extra linear constraints and variables, the agent should construct those constraints and variables with corresponding supporting constructs. Suppose that we have step levels $f _ { i } \ i { = } 1 , . . . . r$ at each interval $[ a _ { i } , a _ { i + 1 } ] i = 1 , 2 , . . . , r - 1$ and a value is determined to be one of f by which interval the value of a variable y is positioned. This step function is then constructed by introducing continuous variables $\lambda _ { i } i = 1 , . . . , 1$ r and binary variables $x _ { j } j = 1 , 2 , . . . , r ^ { - } 1 .$ If the step function value is denoted $\mathsf { a s } f ,$ the following constraints are needed:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$y = \sum_{i=1}^{r}\lambda_{i}a_{i}$ $\sum_{i=1}^{r}\lambda_{i}=1$ $\lambda_1\leq x_1,\lambda_r\leq x_{r-1}$ $\lambda_i\leq x_{i-1} + x_i,i = 2,K,r - 1$ $\sum_{i=1}^{r-1}x_i = 1$ $f = \sum_{i=1}^{r}x_if_i$
</div>

The overall translation procedure for an OPL statement is brie<sup>fl</sup>y described in Fig. 10. The GenerateStepConstraints sub-procedure uses the trick described above because this kind of constraint is piecewise linear and cannot be coped with in a CPLEX engine natively.

![](/api/attachments/DM2WAAR3/fulltext/images/8155d72e627536e833776cb1a457ac0dc99c7b9ba9402357a8767137aa40ce4b.jpg)  
Fig. 10. A general procedure to generate an OPL model.

![](/api/attachments/DM2WAAR3/fulltext/images/db6efb451a02104560c4679586b7cf78495aefb5879b2608b6fe3abf53900100.jpg)  
Fig. 11. A screenshot for optimal decision.

The generated OPL statements are transferred to ILOG OPL studio (Fig. 11); then OPL studio sends the solution for a given problem back to the decision-making model manager. As an example problem, Fig. 12 assumes the case when a shopper intends to <sup>fi</sup>nd the optimal purchase of 3 products, “RETURN,” “Rendezvous” and “MINA3,” from 4 shopping malls, “JoaMusic,” “CDBuy,” “CDPark,” and “HotTracks.” The <sup>fi</sup>gure says, as a result, that the shopper's optimal choice guarantees the minimal total payment, 63,700 Korean Won, and the solution recommends that the shopper purchase two “Rendezvous” and one “MINA3” from “HotTracks,” and one “RETURN” and two “MINA3” from “CDPark.”

Price comparison services on the Web use shopping bots to gather price information for speci<sup>fi</sup>c products from many vendors and allow shoppers to compare these prices. Fig. 13 shows an example of the price information for the album Rendezvous. A shopper may buy products from the vendor with the lowest price as the price comparison services recommend and save on the expenditure for some items.

Nevertheless, the recommendation may not be optimal in terms of the shopper's total expenditure because it does not consider vendor sales policies concerning such matters as delivery and purchase discounts. Table 1 shows the invoice, including delivery costs and discounts, when the albums MINA3, RETURN, and Rendezvous, are purchased at the lowest prices. CDBuy sells Rendezvous at a competitive price, and charges 3000 won for delivery, even though it delivers at no charge when the total amount of the purchase is greater than or equal to 50,000 won. The shopper's total payment, therefore, would be 65,100 won if bought from malls with rock bottom prices.

A shopping agent in the Semantic Web environment recommends an optimal choice by solving a problem with constraints represented with SWCL. Table 2 shows the shopping agent's recommendation obtained previously. Any purchase of more than 20,000 won from CDPark comes with free delivery; at HotTrack purchases totaling 25,000 won or more are delivered for free. A shopper, in addition, gets a 2000-won discount at CDPark for purchases of more than 25,000 won. Its total cost is 63,700 won, which is less than that of the price comparison service, because it <sup>fi</sup>nds the minimum total cost considering sales policies, which are excluded in the price comparison service. Using a knowledge-based shopping agent therefore provides a better decision-making recommendation to Internet shoppers than does price comparison services.

![](/api/attachments/DM2WAAR3/fulltext/images/741bc5d9f90805662337a302f315de4e715d444aad39041919e209342df0ee63.jpg)  
Fig. 12. A screenshot for optimal decision.

![](/api/attachments/DM2WAAR3/fulltext/images/003ba0ee21f3474ea768d3024bc05d1b1abc7ae5481c752c87f7d3c2b1dbe8a6.jpg)  
Fig. 13. Comparison price of shopping.com about album of Rendezvous.

## 6. Conclusion

SWCL is a meaningful tool to bridge between Semantic Web technology and Model Management Systems for virtual enterprises. Recently, thanks to advanced information technologies, virtual enterprises are becoming more widespread, typical examples being travel sites on the Internet. According to [43], the realization of the idea has several technical challenges: integration, security and compliance, user experience, and cost control. Semantic Web technology is mandatory for open and dynamic integration in heterogeneous platforms because it supports the representation of resources in seamless and automated processing methods. Furthermore, to settle many business decision-making problems, such as cost control, reasoning tools existing above knowledge exchange have become compulsory. On the other hand, how to manage a variety of mathematical models in a systematic way has been discussed in the <sup>fi</sup>eld of Model Management Systems and a formal way proposed to represent models independently. From the perspective of intelligent decision support systems for virtual enterprises, therefore, what is missing in providing reasoning for the system is the representation of decision-making problems in Semantic Web technology, and SWCL is supposed to <sup>fi</sup>ll the gap.

Table 1  
The price list when purchased from shopping malls with lowest prices

<table><tr><td>Shop</td><td>Album</td><td>Quantity</td><td>Price</td><td>Total</td><td>Delivery cost</td><td>Discount</td></tr><tr><td rowspan="3">JoaMusic</td><td>MINA3</td><td>3</td><td>9800</td><td>29,400</td><td>2500</td><td>0</td></tr><tr><td>RETURN</td><td>1</td><td>9800</td><td>9800</td><td></td><td></td></tr><tr><td>Rendezvous</td><td>0</td><td>Stock out</td><td>0</td><td></td><td></td></tr><tr><td rowspan="3">CDBuy</td><td>MINA3</td><td>0</td><td>Stock out</td><td>0</td><td>3000</td><td>0</td></tr><tr><td>RETURN</td><td>0</td><td>10,200</td><td>0</td><td></td><td></td></tr><tr><td>Rendezvous</td><td>2</td><td>10,200</td><td>20,400</td><td></td><td></td></tr><tr><td rowspan="3">CDPark</td><td>MINA3</td><td>0</td><td>11,000</td><td>0</td><td>0</td><td>0</td></tr><tr><td>RETURN</td><td>0</td><td>10,700</td><td>0</td><td></td><td></td></tr><tr><td>Rendezvous</td><td>0</td><td>Stock out</td><td>0</td><td></td><td></td></tr><tr><td rowspan="3">HotTracks</td><td>MINA3</td><td>0</td><td>11,000</td><td>0</td><td>0</td><td>0</td></tr><tr><td>RETURN</td><td>0</td><td>11,000</td><td>0</td><td></td><td></td></tr><tr><td>Rendezvous</td><td>0</td><td>11,000</td><td>0</td><td></td><td></td></tr><tr><td colspan="6">Total payment</td><td>65,100</td></tr></table>

This paper proposes a Semantic Web Constraint Language, SWCL based on OWL, and shows how SWCL effectively represents an internet shopper's problem in the real world, together with current Semantic Web components such as OWL and SWRL. To implement our idea and empirically prove the bene<sup>fi</sup>ts of SWCL, we devised an Internet shopping decision-making framework and developed a prototype system for an intelligent shopping agent. The system showed how effectively an intelligent shopping agent can solve an internet shopper's purchasing problem by utilizing and combining OWL, SWRL, SWCL and optimization model technologies.

Beyond this study, there are still several limitations and further research issues. First, SWCL currently covers only the polynomial form of mathematical constraints. Second, the scope of optimization models is restricted only to the mixed integer linear programming model. Linear expressions with integer variables are quite powerful because many decision-making problems can be formulated with them and practically the mixed integer linear programming is one of the classes actively used in reality. The extension to general polynomials, however, might give a wider range of applicability. Another issue is using a constraint programming solver instead of a mathematical programming solver. Recently constraint programming has been focused as solution methods in Operations Research. Because the constraint programming paradigm is known as more <sup>fl</sup>exible and expressive than mathematical programming, it might help to form a tight integration with Semantic Web technology. That is, coping with nonlinearity, global constraints, and propagation techniques are attractive characteristics. A problem is that a constraint programming solver usually has a prede<sup>fi</sup>ned application domain. For instance, the most widely used <sup>fi</sup>nite-domain constraint solver can deal with only models with integer variables. In its current state, therefore, it cannot handle models with both integer and continuous variables, even though it can cope with nonlinearity and has abundant expressions. Hence it could be said that tight integration depends on the future maturity of solver technology. Finally, since the <sup>fi</sup>eld of mathematical programming has conventionally applied different solution methods to different models so that it may exploit the special structures in models, it has a variety of combinations of models and solution techniques. This creates dif<sup>fi</sup>culties for non-experts on solver techniques when trying to choose the best solver for solving a problem. That is why decision support systems are necessary, and model management might be a good candidate for it. Still, it is unknown how to integrate model management and Semantic Web technology. This is one of the most important issues requiring further research.

Table 2  
The price list when purchased through a shopping agent

<table><tr><td>Shop</td><td>Album</td><td>Quantity</td><td>Price</td><td>Total</td><td>Delivery cost</td><td>Discount</td></tr><tr><td rowspan="3">JoaMusic</td><td>MINA3</td><td>0</td><td>9800</td><td>0</td><td>0</td><td>0</td></tr><tr><td>RETURN</td><td>0</td><td>9800</td><td>0</td><td></td><td></td></tr><tr><td>Rendezvous</td><td>0</td><td>Stock out</td><td>0</td><td></td><td></td></tr><tr><td rowspan="3">CDBuy</td><td>MINA3</td><td>0</td><td>Stock out</td><td>0</td><td>0</td><td>0</td></tr><tr><td>RETURN</td><td>0</td><td>10,200</td><td>0</td><td></td><td></td></tr><tr><td>Rendezvous</td><td>0</td><td>10,200</td><td>0</td><td></td><td></td></tr><tr><td rowspan="3">CDPark</td><td>MINA3</td><td>2</td><td>11,000</td><td>22,000</td><td>0</td><td>-2000</td></tr><tr><td>RETURN</td><td>1</td><td>10,700</td><td>10,700</td><td></td><td></td></tr><tr><td>Rendezvous</td><td>0</td><td>Stock out</td><td>0</td><td></td><td></td></tr><tr><td rowspan="3">HotTracks</td><td>MINA3</td><td>1</td><td>11,000</td><td>11,000</td><td>0</td><td>0</td></tr><tr><td>RETURN</td><td>0</td><td>11,000</td><td>0</td><td></td><td></td></tr><tr><td>Rendezvous</td><td>2</td><td>11,000</td><td>22,000</td><td></td><td></td></tr><tr><td colspan="6">Total payment</td><td>63,700</td></tr></table>

## References

[1] J. Angele, H. Boley, J. de Bruijn, D. Fensel, P. Hitzler, M. Kifer, R. Krummenacher, H. Lausen, A. Polleres, R. Studer, Web Rule Language (WRL), W3C Member Submission, Sep. 2005.

[2] N. Bassiliades, P.M.D. Gray, Colan: a functional constraint language and its implementation, Data & Knowledge Engineering 14 (1994) 203–249.

[3] S. Battle, A. Bernstein, H. Boley, B. Grosof, M. Gruninger, R. Hull, M. Kifer, D. Martin, S. McIlraith, D. McGuinness, J. Su, S. Tabet, Semantic Web Services Language (SWSL), W3C Member Submission, Sep. 2005.

[4] H. Boley, S. Tabet, G. Wagner, Design rationale of RuleML: a markup language for Semantic Web rules, Proc. SWWS'01, Stanford, July/August 2001.

[5] T. Bray, J. Paoli, C.M. Sperberg-McQueen, E. Maler, Extensible Markup Language (XML) 10 W3C Recommendation Second Edition Oct, 2000.

[6] D. Brickley, R.V. Guha, RDF vocabulary description language 1.0: RDF schema, W3C Recommendation, Feb. 2004.

[7] C. Cesarano, A. d'Acierno, A. Picariello, An intelligent search agent system for semantic information retrieval on the internet, workshop on web information and data management, Proceedings of the Fifth ACM International Workshop on Web Information and Data Management (ACM WIDM), 2003.

[8] K. Chari, T.K. Sen, An implementation of a graph-based modeling system for structured modeling, Decision Support Systems 22 (1998) 103–120.

[9] M. Desrochers, C.V. Jones, J.K. Lenstra, M.W.P. Savelsbergh, L. Stougie, Towards a model and algorithm management system for vehicle routing and scheduling problems, Decision Support Systems 25 (1999) 109–133.

[10] D.R. Dolk, Model management and structured modeling: the role of an information resource dictionary system. Communications of the ACM 31 (6) (1988) 704–718.

[11] N.J. Fiddian, P. Marti, J.C. Pazzaglia, K. Hui, A. Preece, D.M. Jones, Z. Cui, A knowledge processing system for data service network design, BT Technology Journal 17 (4) (1999) 117–130.

[12] A.M. Geoffrion, An introduction to structured modeling, Management Science 33 (5) (1987) 547–588.

[13] A.M. Geoffrion, The formal aspects of structured modeling, Operations Research 37 (1) (1989) 30–51.

[14] H. Gerald, and M. Stefan, ILOG OPL Studio, OR Spektrum: Organ der Deutschen Gesellschaft für Operations Research (1999) 419–427.

[15] P. Gray, K. Hui, A. Preece, An expressive constraint language for semantic web application, IJCAI 2001 Workshop on E-Business and the Intelligent Web, 2001.

[16] J. Hendler, On beyond ontology: returning to AI from the Semantic Web, ISWC2003 Invited Talks, Oct. 2003.

[17] I. Horrocks, P.F. Patel-Schneider, H. Boley, S. Tabet, B. Grosof, M. Dean, SWRL: a Semantic Web Rule language combining OWL and RuleML, W3C Member Submission, May 2004.

[18] U. Hustadt, B. Motik, U. Sattler, Reasoning in description logics with a concrete domain in the framework of resolution, Proc. of the 16th European Conference on Arti<sup>fi</sup>cial Intelligence (ECAI), 2004, pp. 353–357.

[19] K.B. Jeong, Application of Semantic Web Constraint Language SWCL for Virtual Enterprise, M.S. Thesis (in Korean), Dept. of Information & Industrial Engineering, (Univ. of Yonsei, Seoul, 2007).

[20] G.J.L. Kemp, C.J. Robertson, P.M.D. Gray, N. Angelopoulos, CORBA and XML: design choices for database federations BNCOD 17 LNCS 1832, 2000 pp. 191-208.

[21l M. Kifer Requirements for an expressive rule language on the semantic web W3C Workshop on Rule Languages for Interoperability, 2005.

[22] G. Klyne, J.J. Carroll, B. McBride, Resource Description Framework (RDF) concepts and abstract syntax, W3C Recommendation, Feb. 2004.

[23] R. Krishnan, Knowledge Based Aids for Model Construction, Ph.D. Dissertation (The University of. Texas, Austin, 1987).

[24] J.P. Laudon, K.C. Laudon, Management Information Systems: Managing the Digital Firm & Multimedia Student, Prentice Hall, 2006.

[25] J.K. Lee, M.Y. Kim, Knowledge-assisted optimization model formulation: UNIK OPT, Decision Support Systems 13 (1995) 111–132.

[26] B. Liang, J. Tang, J.Z. Li, Association search in semantic web: search + inference, WWW (2005) 992–993 (Special interest tracks and posters).

[27] F. Manola, E. Miller, RDF Primer, W3C Recommendation, Feb. 2004.

[28] K. Marriott, P.J. Stuckey, Programming with Constraints: An Introduction, The MIT Press, 1998.

[29] C.J. Matheus, K. Baclawski, M.M. Kokar, J.J. Letkowski, Using SWRL and OWL to capture domain knowledge for a situation awareness application applied to a supply logistics scenario, Lecture Notes on Computer Science 3791 (2005) 130–140.

[30] M. Mayer, Future trends in model management systems: parallel and distributed extensions, Decision Support Systems 22 (1998) 325–335.

[31] B. McBride, Jena: implementing the RDF model and syntax speci<sup>fi</sup>cation, Semantic Web Workshop (WWW), 2001.

[32] D.L. McGuinness, F. van Harmelen, OWL Web Ontology Language overview, W3C Recommendation, Feb. 2004.

[33] C. McKenzie, P.M.D. Gray, A.D. Preece, Extending SWRL to express fully-quanti<sup>fi</sup>ed constraints, RuleML (2004) 139–154.

[34] G.L. Nemhauser, L.A. Wolsey, Integer and Combinatorial Optimization, John Wiley & Sons, 1999.

[35] R. O'Keefe, T. Mceachern, Web-based customer decision support systems, CACM 41 (1998) 71–78.

[36] P.F. Patel-Schneider, P. Hayes, I. Horrocks, OWL Web Ontology Language semantics and abstract syntax, W3C Recommendation, Feb. 2004.

[37] A. Preece, K. Hui, A. Gray, P. Marti, T. Bench-Capon, Z. Cui, D. Jones, KRAFT: an agent architecture for knowledge fusion, International Journal of Cooperative Information Systems 10 (1&2) (2001) 171–195.

[38] A. Preece, S. Chalmers, C. McKenzie, J.Z. Pan, P. Gray, A semantic web approach to handling soft constraints in virtual organisations, ACM International Conference Proceeding Series 156 (2006) 151–161.

[39] A. Preece, S. Chalmers, C. McKenzie, J.Z. Pan, P. Gray, Handling soft constraints in the semantic web architecture, Proceedings of the WWW2006 Workshop on Reasoning on the Web (RoW), 2006.

[40] E. Prud'hommeaux, A. Seaborne, SPARQL query language for RDF, W3C Candidate Recommendation, June 2007.

[41] H.A. Simon, The New Science of Management Decision, Harper and Row, New York, 1960.

[42] E. Sirin, B. Parsia, B.C. Grau, A. Kalyanpur, Y. Katz, Pellet: a practical OWL-DL reasoner, Web Semantics: Science, Services and Agents on the World Wide Web 5 (2) (2007) 51–53.

[43] Sun Microsystems inc., Identity Management: Technology Cornerstone of the Virtual Enterprise, October 2004 white paper retrieved from http://www.sun. com/software/products/identity/wp\_virtual\_enterprise.pdf

[44] Y. Tsai, Model integration using SML, Decision Support Systems 22 (1998) 355–377.

[45] D. Tsarkov, I. Horrocks, FaCT++ description logic reasoner: system description, Proc, of the Int. Joint Conf, on Automated Reasoning (IICAR). 2006.

[46] K. Yeom, J.K. Lee, Logical representation of integer programming models, Decision Support Systems 18 (1996) 227–251.

Hak-Jin Kim is an Assistant Professor of Operations Research in the School of Business at Yonsei University. He holds a PhD in Operations Research in Tepper School of Business from Carnegie Mellon University, an MS in Mathematics from University of Illinois at Urbana-Champaign, and a Bachelor of Business Administration from Yonsei University, Seoul, Korea. His research interests are in the Integer Programming, Constraint Programming, and Economics of Finance and Information Systems, including Risk Management, Pricing Strategies, Open Computing and Semantic Web. He has published in Annals of Operations Research, Knowledge Engineering Review, Telematics and Informatics, and Lecture Notes in Computer Science.

Wooju Kim is a professor of Information and Industrial Engineering at Yonsei University in Korea. He received a BBA degree from Yonsei University in 1987, and a PhD in Management Science from KAIST in 1994. He has published many papers related to the issues including Semantic Web, Web Services, e-Business, Expert Systems, S/W Engineering, and Managerial Forecasting. His current research areas are decision support systems on the Semantic Web environment, Semantic Web mining, knowledge management and intelligent web services.

Myungjin Lee is a PhD candidate of Information and Industrial Engineering at Yonsei University in Korea. He has experiences about XML, XML Web Services, and Semantic Web. Therefore, He has been developing SMART Semantic Web Framework which provides a programmatic environment for Ontology reasoning and management. His primary research interests are in Semantic Web, Decision Support Agent, Semantic Web Mining, Semantic Information Retrieval. combining Semantic Web with Machine Learning. He has published a contributed volume, Novel XML & XML Web Services and Novel ISP in Korea.
