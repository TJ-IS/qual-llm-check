---
otero_id: 13200
otero_key: "KBJTAPTP"
title: "Using fuzzy repertory table-based technique for decision support"
authors: "J.J. Castro-Schez; L. Jimenez; J. Moreno; L. Rodriguez"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2003.11.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Using fuzzy repertory table-based technique for decision support

J.J. Castro-Schez<sup>a,</sup>\*, L. Jimenez<sup>a</sup>, J. Moreno<sup>b</sup>, L. Rodriguez<sup>c</sup>

<sup>a</sup> Department of Computer Science, E.S.I. Informatica, Universidad de Castilla-La Mancha, Paseo de la Universidad, 4, 13071 Ciudad Real, Spain

<sup>b</sup> Department of Computer Science, E.U.I. Industrial, Universidad de Castilla-La Mancha, Avenida Carlos III, 45004 Toledo, Spain Department of Computer Science, E.U. Politecnica, Universidad de Castilla-La Mancha, Plaza Manuel Meca, 1, 13400 Almaden, Spain

Received 23 April 2002; received in revised form 4 November 2003; accepted 4 November 2003 Available online 13 December 2003

## Abstract

This paper is mainly concerned with the extension of fuzzy repertory table technique (FRT), so as to permit managers of organizations or groups to use it as a decision support system (DSS). The work considers the problem of decision making in environments in which the options are clear. In such environments, the manager must analyze each option making use of his or her knowledge with the aim of highlighting its strength, originality and defects for each in turn. The manager will then choose the most advantageous option according to this information and his or her preferences. We have developed an FRT-based decision support technique for carrying out all these tasks. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Fuzzy repertory table; Repertory grid; Decision support systems; Knowledge-driven decision support system

## 1. Introduction

Computer-based methods are developed to improve the effectiveness of managerial decision making. Decision Support Systems (DSS) are being advocated, built and deployed in an increasing array of complex application domains. The object of the DSS is to aid human cognitive deficiencies by integrating various sources of information, providing intelligent access to relevant knowledge. By aiding the process of structuring decisions, they can also support choice from among well-defined alternatives. They employ artificial intelligence methods to address, by means of a heuristic approach, problems which are otherwise not easily handled by formal techniques [12].

A wide range of DSS have been developed, which vary in many ways. In the literature about this topic, we can find a number of frameworks for categorizing such systems [1,11,24,32]. According to these sources, the main DSS categories are:

 Data-oriented or data-driven. These systems are focused on data. They access and process large databases of structured data (e.g., file drawer and management reporting systems, data warehousing and data analysis systems).

 Model-oriented or model-driven. These systems put emphasis on access to and manipulation of a model (e.g., systems that use accounting and financial models, representational models, and optimization models).

 Intelligent or knowledge-driven. These systems are focused on the dominant knowledge base and integrate artificial intelligence technologies such as neuronal networks, expert systems, machine learning to support the decision making process in computer task.

DSS represent a wide research subject over many disciplines, such as statistics, economics, information science, cognitive psychology, and artificial intelligence. In this paper, we put together ideas from cognitive psychology and artificial intelligence for developing a knowledge-driven DSS.

This DSS will be useful for helping decisionmakers when they are faced with situations in which they must choose among a set of clear alternatives. In this context, conventional DSS schemes consist of the following stages: (a) specification of requirements, (b) evaluation of alternatives and (c) choice of solution. In order to put these stages into practice, we suggest the following methods:

 Fuzzy repertory table with an ideal decision confirmation, with the object of obtaining the specification of requirements and the evaluation of alternatives.

 An analysis of the relevant factors, whose aim is to obtain the best option according to the knowledge acquired.

The fuzzy repertory table facilitates the identification of significant characteristics associated with each option [7,8]. It is based on the repertory grid technique (RG) [28] which has been already used as a DSS [5]. However, this approach had some limitations that we try to resolve with the fuzzy repertory table technique (FRT).

The remainder of this paper is structured in the following way. Section 2 describes the repertory grid technique, justifies its choice as a tool useful for the specification of requirements and explains how the FRT solves the limitations of RG technique. The FRT will be explained in Section 3. Section 4 describes the

DSS developed. In Section 5, we apply the DSS suggested to a real example. Concluding remarks and future work are the subject of Section 6.

## 2. The background to repertory grid technique

The RG is a technique devised by clinical psychologist G. Kelly [28] for identifying the combination of characteristics or qualities which form an individual’s distinctive character.

In the field of knowledge acquisition, it has been proven to be a useful tool for identifying the significant characteristics associated with each element [4,6,8,17,19]. The main concepts in RG are:

 Elements, i.e., people, things, events or experiences which are being discussed, deal with or which are related to the particular problem or purpose for using the grid.

 Constructs, i.e., dimensions of similarity and difference among elements.

The most basic form for an RG is a rectangular matrix with elements as columns and constructs as rows. Each row –column intersection into the grid contains a rating showing how a person applied a given construct to a particular element.

The RG technique can be briefly described as follows:

Step 1. Identify the set of elements.

Step 2. Repeat until all elements are dissimilar.

Step 2.1. Select three elements from the set of elements which are currently rated in a similar way on all constructs.

Step 2.2. Identify a construct that will make two elements similar and the other different.

Step 2.3. Do a rating for all elements on the new construct.

Step 3. Identify two constructs that are given similar rates for all the entities.

Step 3.1. Add a new element to break the similarity.

Step 3.2. Do the rating for this new element on all constructs.

Step 4. If some new element has been added go to Step 2.

Step 5. End.

Similarities may occur either for elements or constructs. Hence, since we are interested in the study of similarities and differences among elements for identifying the requirements of the correct option among a set of well defined options, we will not study the similarities among constructs. Thus, we will say that two elements will be similar if they have similar ratings on many constructsdimensions. There are several distance measures for assessing the similarity between elements (e.g., Euclidean, Manhattan, Hamming). In any of these measures used, the lower the distance between two elements, the more similar the elements are deemed to be.

In decision support systems, the RG provides a mechanism for describing the properties (constructs) attached to each option (element) and these properties will reflect the requirements of the solution.

We could apply many manual and automatic techniques for identifying significant characteristics associated to each option, some of them are card or concept sorting [29,35], laddered grid [15,21,23,35,36]. . . We suggest the RG for doing this, for the following reasons:

 It has a solid foundation in human psychological theory [28]. According to this theory, the RG gives a reliable representation of the repertoire of constructs (or attributes) that the individual uses based on his personal experience in the field.

 It has been demonstrated to be useful in eliciting and acquiring knowledge from people [4,6,17,19].

 It has been successfully used as a tool in the design, delivery and evaluation of management interventions [13].

 It is easy to formalize, it allows us to have insight on an option and it is active (it makes instantaneous analysis on data just introduced, helping its user to express his knowledge).

 It is easy to use and understand, the basic fundamental can be quickly grasped because it is based on habitual human behavior, that is to say comparing some things for recognition and understanding of their differences.

The repertory grid technique has been already used for identifying attributes of great significance or value associated with each option, and to make the decision-maker’s work easy [5]. That method is based on an extension of classic or Kelly’s [28] repertory grid which works with values chosen from a rating scale defined within a bipolar distinction (i.e., each construct works on opposites, it has left and right distinctions poles). It requires the decision-maker to assign a value to each element accurately, that is to say, he must make crisp distinctions. However, in the decision-maker’s mind there is vagueness. This incompatibility in dealing with vague information has led to new extensions of repertory grid:

Gaines’ approach [20] makes use of the fuzzy set concept for representing each construct pole (e.g., ‘cheap’ or ‘expensive’). To assign a value to a construct is considered as giving a degree of belonging to the fuzzy set that defines each construct pole.

 Ford’s approach [18] obtains uncertain knowledge expressed as rules but it works with values chosen from a pre-defined rating scale.

 Bathia’s approach [3] allows the decision-maker to enter a range of valued ratings rather than a crisp value.

Because there is a reciprocal influence between the technique and the decision-maker, in the RG it is very important to optimize the understandability of the knowledge. Knowledge which is more understandable makes the interaction easier and this may have a big effect on the process of knowledge acquisition and help to reduce the unwillingness to accept the knowledge acquired. One of the best ways to improve the knowledge understandability is offering the decision-maker the ability to express his knowledge as he usually expresses it. Thus, Web-Grid II [37] allows the user to embody symbolic and numeric constraints in the grid. However, it does not allow the representation of vagueness in numeric characteristics.

The assigning of linguistic terms to phenomena, in order to describe the object’s numeric characteristics or properties, is very natural. Decision-makers make such assignments every day. Thus, Hwang’s [25] approach, the fuzzy table allows the introduction of linguistic labels. This table adapts the grid for dealing with vagueness by means of fuzzy logic. This approach is the most appropriate for describing and manipulating linguistic information. Anyway, a grid that only takes into consideration fuzzy values does not seem to be suitable for our purpose of allowing the decision-maker to express himself freely, because not everything in the user’s mind is vague.

Fuzzy Repertory Table [7] takes into account this fact and extends the RG technique for allowing the representation of all values (crisp and vague) that a user applies when he thinks something out as well as what a decision-maker uses when he makes a detailed investigation and analysis of each option.

In the next section, some technical background, pertinent to our discussion, is given about FRT.

## 3. Fuzzy repertory table, a method for acquiring significant characteristics

The FRT is based on the repertory grid technique. FRT also likes a rectangular matrix with elements (as columns) and constructs (as rows). Each row –column intersection contains a rating, which consists of a set of trapezoidal functions (any cardinality is allowed) showing how a user applied a given construct to a particular element.

$$
\Pi (u; a, b, c, d) = \left\{ \begin{array}{l l} 0 & : u <   a \\ \frac {u - a}{b - a} & : a \leq u <   b \\ 1 & : b \leq u \leq c \\ \frac {d - u}{d - c} & : c <   u \leq d \\ 0 & : u > d \end{array} \right.\tag{1}
$$

By means of the trapezoidal functions (see Eq. (1) and Fig. 1), the FRT extends the forms of constraint that can be represented in a grid in order to increase its representational power, while allowing the user to express his knowledge with complete freedom. The FRT aim is to obtain a set of attributes and measurements for them. Measurement implies assigning numbers or symbols to measure something from a scale. These numbers will always be taken from a bipolar scale delimited by the most desirable and undesirable value. The FRT allows us to deal with the following scales of measurement:

![](/api/attachments/KBJTAPTP/fulltext/images/a74c7bddd5ede2d7af47da43ac6e7f6000044f7eaf7aef8e6a17f1ddb13fe329.jpg)  
Fig. 1. Graphical representation of Eq. (1).

 Ordinal scale. A number states precisely an element’s position in the series established by the scale (e.g., grades for academic performance, service quality assessment. . .).

 Continuous or real scale. A number, representing a particular quantity, defines an element (e.g., age, date, weight. . .).

 Nominal scale. There are no numbers. ‘‘Names’’ define the elements (e.g., marital status, religion, occupation, sex. . .).

The suitable values, for each scale mentioned earlier, are:

 Continuous or real scale. All of the following values may coexist in this scale.

 Fuzzy value. The user assigns a linguistic term to an element [40]. When the user introduces a new linguistic term, he must establish what interval of values is ‘‘perfectly’’ defined by it. These values will be the interval [b, c]. The parameters a and b are derived from adjacent terms in the construct scale.

 Crisp value. The user assigns a number, x, to an element. The function associated with this value is one with the parameters $a = b = c = d = x$

 Crisp interval value. The user assigns two numbers, x and y, to an element in such a way that the interval between these two values is meaningful for him. The trapezoidal function associated with this value is $a = b = x$ and $c = d = y .$

 Ordinal scale. The following values cannot coexist in the same scale.

 Boolean value. The user gives this value for representing logical propositions by means of false and true. Two functions are created, the parameters of these functions will be $a = b = c = d = 0 \quad ( { \mathrm { f a l s e } } ) \quad { \mathrm { a n d } } \quad a = b = c = d = 1$ (true).

 Ordered value. The user attaches numbers to elements in a particular order. The trapezoidal functions associated with this value are $a = b = d = c = x _ { 1 } , ~ a ^ { \prime } = b ^ { \prime } = c ^ { \prime } = d ^ { \prime } = x _ { 2 } , ~ a ^ { \prime \prime } = b ^ { \prime \prime } =$ $c ^ { \prime \prime } = d ^ { \prime \prime } = x _ { 3 } , . . .$ .where $x _ { 1 } , x _ { 2 } , x _ { 3 } , . . . . x _ { i }$ is the order assigned.

 Nominal scale.

 Nominal value. The user ascribes ‘‘names’’ to elements. There is not an order relation between them. The trapezoidal functions associated with these values are dynamically established.

Vagueness usually appears when the user gives values taken from the continuous or real scale. The user can provide concrete or fuzzy, unique or interval values. The fuzzy values will be given using linguistic values (e.g., high, medium, frequently, sometimes, rarely). FRT also allows the user to give symbolic values such as any and none and several values in any scale. This is another mechanism to deal with the imprecision present in the user’s thought or expression.

The FRT performance is shown in Fig. 2. It is also based on the search for elements that are similar and it finds attributes, defined in a bipolar scale, which allow differentiating between them.

![](/api/attachments/KBJTAPTP/fulltext/images/4805939c553744df2048c396bb20867280e01b84728f5c493f37afcc5a94dcb8.jpg)  
Fig. 2. General structure of FRT technique performance.

In the FRT development process, a new data structure is used, it is named the distinctions matrix (DM). The distinctions matrix is a rectangular array with $n \times n$ cells, where n is the quantity of FRT’s elements. Each intersection $( i , j )$ at the matrix holds within it knowledge concerning what the marked differences between i and j elements are and the level or grade of each differentiation. This grade associated with each differentiation (attached to a construct or attribute x) between i and j is expressed as strength $( i , j , x ) = d _ { \mathrm { N } } ( e _ { i } , e _ { j } , x )$ , where $d _ { \mathrm { N } }$ is the separability measurement suggested in Ref. [7]. We will now consider its definition.

The system of measurement of the separability between two elements holds information with regard to the gap that there is between them. Because all values in the FRT are represented by means of trapezoidal functions, the gap between two elements x and $y ,$ paying attention to a specified attribute i, will be calculated as the area of the fuzzy set defined in Eq. (2), where $\wedge$ is the minimum t-norm and \_ is the maximum t-conorm and A and B are the values that have been assigned to the attribute i for the elements x and y, respectively. This set is also shown in diagram form in Fig. 3.

(a)  
![](/api/attachments/KBJTAPTP/fulltext/images/cdd9a166a87c0f216e489fbfae2129e85e995f750a13178381aea781eee79663.jpg)

(b)  
![](/api/attachments/KBJTAPTP/fulltext/images/a6c6ae25f4f4652776825baeb980cf1f06bf8606e70f83582fc7fd667d85dd14.jpg)

![](/api/attachments/KBJTAPTP/fulltext/images/5f1ecc16a7869c39ac50983158aea0887edaa251b664fed70074f55289c74e7c.jpg)

(d)  
![](/api/attachments/KBJTAPTP/fulltext/images/019af20228016d4452defa01ec9e04b6ae12d0f1dd7a2fc837e52c2ca5c73535.jpg)  
Fig. 3. Calculus of gap between A and B values, (a) A and B values, (b) value greater than A, (c) value less than B and (d) gap between A and B.

$$
\begin{array}{c} \text { Gap - between } (A, B) = [ \text { Greater } (A) \land \text { Less } (B) ] \\ \lor [ \text { Less } (A) \land \text { Greater } (B) ] \end{array}\tag{2}
$$

The suggested measure is a real function, which is based on the calculation of the area of the fuzzy set Gap-between. The precise mathematical definition is established in Eq. (3).

$$
d (x, y, i) = a _ {1} (A, B) + a _ {2} (A, B),\tag{3}
$$

where

$$
a _ {1} (A, B) = \left\{ \begin{array}{l l} \frac {\left(\left(b ^ {\prime} - c\right) + \left(a ^ {\prime} - d\right)\right)}{2}, & \text { when } d \leq a ^ {\prime}, \\ \frac {\left(b ^ {\prime} - c\right) \times h}{2}, & \text { when } a ^ {\prime} <   d \text { and } c \leq b ^ {\prime}, \\ 0, & \text { otherwise }; \end{array} \right.
$$

$$
a _ {2} (A, B) = \left\{ \begin{array}{l l} \frac {\left(\left(b - c ^ {\prime}\right) + \left(a - d ^ {\prime}\right)\right)}{2}, & \text { when } d ^ {\prime} \leq a, \\ \frac {\left(b - c ^ {\prime}\right) \times h ^ {\prime}}{2}, & \text { when } a <   d ^ {\prime} \text { and } c ^ {\prime} \leq b, \\ 0, & \text { otherwise }; \end{array} \right.
$$

and

$$
h = \frac {(b ^ {\prime} - c)}{(b ^ {\prime} - a ^ {\prime}) + (d - c)}; h ^ {\prime} = \frac {(b - c ^ {\prime})}{(b - a) + (d ^ {\prime} - c ^ {\prime})}.
$$

The functions $a _ { 1 }$ and $a _ { 2 }$ are based on the definitions of the membership functions of the fuzzy sets A and $B ,$ and they calculate the area corresponding to the fuzzy sets Greater(A)^Less(B) and Greater(B)^Less(A), respectively.

The total gap or separation between two elements (x, y) is defined as the average value of the gap between them according to each attribute or construct, see Eq. (4),

$$
D (x, y) = \frac {\sum_ {i = 1} ^ {u} d _ {\mathrm{N}} (x , y , i)}{z}\tag{4}
$$

with u being the number of attributes; z is the number of attributes with some value other than none; $d _ { \mathrm { N } }$ is the normalized separation—see Eq. (5). The normalized separation between two elements (x, y) according to the attribute i is defined as

$$
d _ {\mathrm{N}} (x, y, i) = \frac {d (x , y , i)}{d (\max (i) , \min (i) , i)}\tag{5}
$$

with $d ( x , y , i )$ being the metric defined in Eq. (3) in relation to the i attribute and max(i) and min(i) are two functions which return, respectively, the maximum (rightmost value) and minimum (leftmost value) values from the i attribute scale. The rightmost value will be the one that has the greatest a and b parameters. The leftmost value is the one with the parameters c and d lowest.

Nominal attributes are often analyzed in linear models by applying two heuristics for developing dummy trapezoidal functions, see Ref. [7].

This measurement of the gap between two elements cannot be considered as a distance because it does not verify the triangular property $D ( x , y ) \le D ( x , z ) + D ( z , y )$ for all $x , y , z .$ . This is not a problem for our aim. It has been demonstrated in the psychology field that triangular assumption is not always fulfillable and in many situations we are even advised that it will be fulfilled only in part [39]. Other interesting properties fulfilled by the suggested measure can be found in Ref. [7].

In the next section, we show how FRT is integrated into a system useful for supporting decision in multiissue environments.

## 4. FRT-based decision support

The system suggested for supporting decision in multi-issue environment makes use of FRT for acquiring attributes important enough to merit the decision-maker’s attention. It is also used for acquiring the decision-maker’s requirements. FRT elements will be the set of possible options among which the decision maker must choose. The FRT output will be the features of the ideal option and what the significance attached to these features by the decision-maker is (decision-maker’s profile). Moreover, we obtain the values of these features for each option (FRT) and of how any one of these is different from the others (Distinctions Matrix). The system includes a method for analyzing this information and recommends an option to the decision-maker (see Fig. 4).

The process of developing the FRT (into the DSS suggested) is the same as when it is used for acquiring knowledge (see Section 3). Its novelty lies in its estimation of importance or priority attached to each attribute when the user makes a decision. Thus, after identifying a set of options, the decision-maker is asked to define some attributes (constructs), which characterize those options. To do this, FRT searches for similarities among the options and it presents three similar options to him with a request to state in what way two are alike and how they differ from a third. When he introduces a new attribute (construct) he is asked to estimate its importance or priority when he takes a decision in the domain. It will be expressed by means of real values assessed in a predefined range. In early phases of FRT development, we recommend higher priorities. He must also specify the preference value for the construct (that is, the ideal value).

Once the options are distinguished clearly (FRT has been already developed), we are going to obtain the relevant factors attached to each option, and after that we analyze them to obtain the most suitable option according to the decision-maker’s profile. To do all this, we use the algorithm Supporting Decision. This algorithm describes the way in which it establishes relevant factors (positive and negative) for each option from the information contained in FRT, the distinctions matrix and the decision-maker’s profile. It also estimates the most favorable or advantageous option and offers an explanation about that decision.

## 4.1. Algorithm supporting decision

The input of the algorithm is the set of valid options for decision-marker $\varepsilon , \ \mid \varepsilon \mid = k ,$ , FRT and its associated distinctions matrix (named DM).

The output of the algorithm will be an option which is recommended to the decision-marker and knowledge for justifying such a recommendation.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Step 1. For i = 1 to k
    For j = 1 to k
    For each  $C_x \in DM[i, j]$ 
    if  $d(\text{ideal}(x), FRT[x, i], x) \leq d(\neg \text{ideal}(x), FRT[x, i], x)$ 
    then  $Neg[i, j] = C_x$ ;  $Pos[j, i] = C_x$ 
    else  $Pos[i, j] = C_x$ ;  $Neg[j, i] = C_x$ 

Step 2. For  $A' = \{Pos, Neg\}$ 
    For i = 1 to k do
    For j = 1 to k do
    if  $|A'[i, j]| = 1$  then introduce the construct  $C_x$  in its relevant factors ( $R_{fi}^+$  for Pos or  $R_{fi}^-$  for Neg).
    if  $|A'[i, j]| &gt; 1$  then
    Develop a set C, such that  $C_x \in C$  iff  $C_x \in A'[i, j]$  and
    strength(i, j, x) = max $_y$ {strength(i, j, y)}
    if  $|C| = 1$  introduce the construct  $C_x \in C$  in its relevant factors ( $R_{fi}^+$  or  $R_{fi}^-$ ).
    if  $|C| &gt; 1$ 
    Develop a set  $C'$ , such that  $C_x \in C'$  iff  $C_x \in C$  and  $C_x$  is the highest priority construct.
    if  $|C'| = 1$  introduce the construct  $C_x \in C'$  in its relevant factors ( $R_{fi}^+$  or  $R_{fi}^-$ ).
    if  $|C'| &gt; 1$  introduce in its relevant factors ( $R_{fi}^+$  or  $R_{fi}^-$ ), all constructs  $C_x \in C'$ , such that  $C_x \notin R_{fi}$  ( $R_{fi}^+$  or  $R_{fi}^-$ ).
Step 3. For i = 1 to k
    Calculate Goodness( $O_i$ ) (see Equation (6)), where  $O_i \in E$ 
Step 4. Return  $O_e$  such that  $O_e = \max_{i=1...k} (Goodness(O_i))$ 
    For j = 1 to k do Show(FRT[Neg[j, e], e])
Step 5. End.
</div>

We firstly determine for each option which attributes are near to the construct value which is considered by the decision-marker as the ideal value (positive constructs) and those which are far from that ideal value (negative constructs). We derive two matrixes from FRT, one for holding the positive constructs and the other one with the negative constructs, where the matrix with negative constructs is the transpose matrix of that with the positive constructs. We will name them Pos and Neg (Step 1).

Next, we obtain for each option the sets with their positive and negative relevant factors (Step 2). These will be those constructs and their strength which distinguish this element from any other in a particular level of rank fixed previously by the manager. When several constructs distinguish between two options, we choose the construct that distinguishes with the highest strength. If there are several constructs that distinguish with equal strength, we choose the one which is the highest priority for the decision-maker. When all options have the same priority for him, we choose that construct which has not yet been included in the set. If any of them has not yet been included, we introduce all of them.

Then we study these factors for recommending one option (Step 3). We suggest a measurement (see Eq. (6)), defined for each option in order to compare the options. This measurement pays attention to the positive factors and their significance as an indicator for reinforcing an option (see Eq. (7)). The negative factors and their significance are used for cutting down on the option indicator (see Eq. (8)).

![](/api/attachments/KBJTAPTP/fulltext/images/8f2199209b434619ef1062240e217bcfc1a2ab3025f3832b2eedc588a820199c.jpg)  
Fig. 4. Structure of suggested Decision Support System.

Goodness $( O _ { i } ) = O _ { i } ^ { + } - O _ { i } ^ { - }$

ð6Þ

where

$$
O _ {i} ^ {+} = \sum_ {\forall x \in R _ {f i} ^ {+}} \operatorname{Strength} (x, i) \times \operatorname{Priority} (x)\tag{7}
$$

$$
O _ {i} ^ {-} = \sum_ {\forall x \in R _ {f i} ^ {-}} \operatorname{Strength} (x, i) \times \operatorname{Priority} (x)\tag{8}
$$

Priority(x) is a function which returns the priority associated to $C _ { x }$ construct. Strength(x, i) is a function which returns the strength associated to the construct $C _ { x }$ for the element i according to some other element j such as $\mathrm { D M } [ i , j ] = C _ { x } .$

The recommended option will be the one with the highest ‘‘goodness’’ value. To justify this decision, we show the constructs belonging to the negative constructs set that distinguish the recommended option from the remainder (Step 4).

In the next section, we describe a small real example to illustrate the DSS discussed so far. The case under study concerns a domain in which a student wants to rent a residence and requests the services of an estate agency.

## 5. Applying the DSS proposed to a real example

We use the suggested DSS for helping the student when he is looking for accommodation to rent. An estate agency sends him a list containing different accommodations and data about each of them (see Table 1). He must choose among them, that is, he must make a decision!

In this scenario, options are the different accommodations available in the list given by the estate agency, $\varepsilon { = } \{ A _ { 1 } , A _ { 2 } , A _ { 3 } , A _ { 4 } , A _ { 5 } , A _ { 6 } \}$ . We ask the student to read the description and look at pictures attached to each accommodation and complete an FRT session in which he describes and analyzes the differences and similarities among these accommodations, so we are equipping the data with meaning. In Figs. 6 and 7, we show the FRT and its associated distinctions matrix which is obtained at the end of the session. All attributes and values into the FRT are directly introduced and defined by the student.

Table 1  
List provided to the student for the estate agency, where in the description field we show only a part of the data provided referring to each accommodation and in the picture field we show the impression given by means of a picture set about each accom modation option. This last data has been abridged by us because it takes up a lot of writing space. Care has been taken to keep the essence of the example intact

<table><tr><td>Lodging</td><td>Description</td><td>Picture</td></tr><tr><td> $A_{1}$ </td><td>A room in a guest house, rent approximately £200 per month, has a phone and cooking facilities and located in the Highfield district.</td><td>Good appearance</td></tr><tr><td> $A_{2}$ </td><td>A room in a shared house, situated in Basset district, rent almost £230 per month, has cooking facilities but no phone.</td><td>Average appearance</td></tr><tr><td> $A_{3}$ </td><td>Apartment located in Basset district, rent around £350 per month, has a phone but no cooking facilities.</td><td>Good appearance</td></tr><tr><td> $A_{4}$ </td><td>Flat situated in St. Dennis district, has cooking facilities but no phone, rent approximately £310 per month.</td><td>Bad appearance</td></tr><tr><td> $A_{5}$ </td><td>Apartment in the St. Dennis district, rent £510 per month, has a phone, new furniture, air conditioning and cooking facilities.</td><td>Average appearance</td></tr><tr><td> $A_{6}$ </td><td>A room in a Hall of Residence located in the Bitterne district, has phone but no cooking facilities; air conditioning, rent £175 per month.</td><td>Good appearance</td></tr></table>

Now, we recall how this information is obtained (see Ref. [7]). Firstly, all accommodations are similar, there is not any construct or attribute attached to the accommodation. The technique randomly selects three accommodations of e, $\{ A _ { 1 } , A _ { 2 } , A _ { 5 } \}$ and asks for one attribute that distinguishes between these accommodation options, the student answers that rental rate is such an attribute. The technique helps the student to determine the type of this attribute (see

μ  
![](/api/attachments/KBJTAPTP/fulltext/images/57381128e46f2d22eafb79912e0b9ff43b5a93a19152690aa46165f6bf0ee11f.jpg)  
Fig. 5. Definition domain for the variable Rental rate.

Section 3), in this case the rental rate is a continuous fuzzy value. This information allows the technique to establish the attribute definition domain, that is the set of values that this attribute could take. The student values each accommodation belonging to <sub>q</sub> paying attention to this attribute. When the student introduces a fuzzy value (by means of a linguistic term), for example cheap, he establishes its core— those are the values which clearly belong to the linguistic term, the interval [b, c] in this case [100, 250]. When all values have been introduced, the values a and $d$ of each fuzzy value are determined on the basis of the values [b, c] of its right and left neighbor values and the type of the variable (see Fig. 5).

Table 2  
Relevant information, about constructs or attributes and student’s profile, obtained during the FRT development shown in Fig. 6

<table><tr><td>Variable</td><td>Definition domain</td><td>Ideal value</td><td>Priority</td></tr><tr><td>Rental rate (£)</td><td>{Cheap(100, 100, 250, 300),Average(250, 300, 400, 450),Expensive(400, 450, 600, 600)}</td><td>Cheap</td><td>20</td></tr><tr><td>Distance to work place(minutes walk)</td><td>{Near (0, 0, 15, 25),Average(15, 25, 30, 35),Far (30, 35, 50, 50)}</td><td>Near</td><td>10</td></tr><tr><td>House condition</td><td>{Bad (4, 4, 4, 4),Average_bad(3, 3, 3, 3),Average_good(2, 2, 2, 2),Good (1, 1, 1, 1)}</td><td>Good</td><td>8</td></tr><tr><td>Lodging type</td><td>{Room in guest house (1, 1, 1, 1)Shared house (2, 2, 2, 2)Hall (3, 3, 3, 3)Flat (4, 4, 4, 4)Apartment (5, 5, 5, 5)}</td><td>Apartment</td><td>0.5</td></tr><tr><td>Has phone</td><td>{Yes (1, 1, 1, 1)No (0, 0, 0, 0)}</td><td>Yes</td><td>0.3</td></tr><tr><td>Has cooking facilities</td><td>{Yes (1, 1, 1, 1)No (0, 0, 0, 0)}</td><td>Yes</td><td>0.1</td></tr></table>

<table><tr><td></td><td>A1</td><td>A2</td><td>A3</td><td>A4</td><td>A5</td><td>A6</td></tr><tr><td>Rental rate</td><td>Cheapa=100b=100c=250d=300</td><td>Cheapa=100b=100c=250d=300</td><td>Averagea=250b=300c=400d=450</td><td>Averagea=250b=300c=400d=450</td><td>Expensivea=400b=450c=600d=600</td><td>Cheapa=100b=100c=250d=300</td></tr><tr><td>Distance to work place</td><td>Neara=0b=0c=15d=25</td><td>Neara=0b=0c=15d=25</td><td>Neara=0b=0c=15d=25</td><td>Averagea=15b=25c=30d=35</td><td>Averagea=15b=25c=30d=35</td><td>Fara=30b=35c=50d=50</td></tr><tr><td>House condition</td><td>Gooda=b=c=d=1</td><td>Average_gooda=b=c=d=2</td><td>Gooda=b=c=d=1</td><td>Bada=b=c=d=4</td><td>Average_bada=b=c=d=3</td><td>Gooda=b=c=d=1</td></tr><tr><td>Lodging Type</td><td>Room in guest housea=b=c=d=1</td><td>Shared housea=b=c=d=2</td><td>Apartmenta=b=c=d=5</td><td>Flata=b=c=d=4</td><td>Apartmenta=b=c=d=5</td><td>Halla=b=c=d=3</td></tr><tr><td>Has phone</td><td>Yesa=b=c=d=1</td><td>Noa=b=c=d=0</td><td>Yesa=b=c=d=1</td><td>Noa=b=c=d=0</td><td>Yesa=b=c=d=1</td><td>Yesa=b=c=d=1</td></tr><tr><td>Has cooking facilities</td><td>Yesa=b=c=d=1</td><td>Yesa=b=c=d=1</td><td>Noa=b=c=d=0</td><td>Yesa=b=c=d=1</td><td>Yesa=b=c=d=1</td><td>Noa=b=c=d=0</td></tr></table>

Fig. 6. Fuzzy repertory table developed by the student in the renting scenario making use of information in Table 1.

As mentioned in Section 4, each time the student introduces an attribute in the FRT, he must estimate the importance that he assigns to this attribute when he is taking a decision. He must also tell us what the ideal value is. For Rental rate attribute, the student assigns priority 20 and indicates that its ideal value is Cheap.

The technique then analyzes the FRT obtained, to discover similar accommodations, which will be shown to the student, with the object of obtaining more attributes. By repeating this process until none of the accommodations are similar, we shall acquire the required set of attributes or variables and their definition domains which the student uses for assessing an accommodation (see Section 2).

We emphasize relevant information about the constructs acquired and the student’s profile in Table 2. The student wants accommodation which is located near to the University and whose rental rate will be cheap (these are two fuzzy values taken from a continuous or real scale), he prefers an apartment in good condition (these are two ordered values taken from an ordinal scale) and he would like the accommodation to have a phone and cooking facilities (these are two boolean values taken from an ordinal scale).

<table><tr><td></td><td> $A_1$ </td><td> $A_2$ </td><td> $A_3$ </td><td> $A_4$ </td><td> $A_5$ </td><td> $A_6$ </td></tr><tr><td> $A_1$ </td><td>Nil</td><td> $C_5(1)$ ;</td><td> $C_4(1);C_6(1)$ ;</td><td> $C_3(1)$ ; $C_4(0.75)$ ; $C_5(1)$ ;</td><td> $C_1(1);C_4(1)$ ;</td><td> $C_2(1);C_6(1)$ ;</td></tr><tr><td> $A_2$ </td><td> $C_5(1)$ ;</td><td>Nil</td><td> $C_4(0.75);C_5(1)$ ; $C_6(1)$ ;</td><td> $C_3(0.67)$ ;</td><td> $C_1(1);C_4(0.75)$ ; $C_5(1)$ ;</td><td> $C_2(1)$ ; $C_5(1);C_6(1)$ ;</td></tr><tr><td> $A_3$ </td><td> $C_4(1);C_6(1)$ ;</td><td> $C_4(0.75);C_5(1);C_6(1)$ ;</td><td>Nil</td><td> $C_3(1);C_5(1)$ ; $C_6(1)$ ;</td><td> $C_6(1)$ ;</td><td> $C_2(1)$ ;</td></tr><tr><td> $A_4$ </td><td> $C_3(1);C_4(0.75)$ ; $C_5(1)$ ;</td><td> $C_3(0.67)$ ;</td><td> $C_3(1);C_5(1)$ ; $C_6(1)$ ;</td><td>Nil</td><td> $C_5(1)$ ;</td><td> $C_3(1);C_5(1)$ ; $C_6(1)$ ;</td></tr><tr><td> $A_5$ </td><td> $C_1(1);C_4(1)$ ;</td><td> $C_1(1);C_4(0.75)$ ; $C_5(1)$ ;</td><td> $C_6(1)$ ;</td><td> $C_5(1)$ ;</td><td>Nil</td><td> $C_1(1);C_6(1)$ ;</td></tr><tr><td> $A_6$ </td><td> $C_2(1);C_6(1)$ ;</td><td> $C_2(1);C_5(1);C_6(1)$ ;</td><td> $C_2(1)$ ;</td><td> $C_3(1);C_5(1)$ ; $C_6(1)$ ;</td><td> $C_1(1);C_6(1)$ ;</td><td>Nil</td></tr></table>

Fig. 7. Distinctions matrix associated with the FRT shown in Fig. 6, with C (a) being the construct i, and its meaning in the cell $( x , y )$ is that i separates between x and y in a a degree, strength(x, y, i) = a. We introduce here only those constructs which separate between elements in a degree higher than 0.6.

<table><tr><td></td><td> ${\mathrm{A}}_{1}$ </td><td> ${\mathrm{A}}_{2}$ </td><td> ${\mathrm{A}}_{3}$ </td><td> ${\mathrm{A}}_{4}$ </td><td> ${\mathrm{A}}_{5}$ </td><td> ${\mathrm{A}}_{6}$ </td></tr><tr><td> ${\mathrm{A}}_{1}$ </td><td>Nil</td><td> ${\mathrm{C}}_{5}\left( 1\right) ;$ </td><td> ${\mathrm{C}}_{6}\left( 1\right) ;$ </td><td> ${\mathrm{C}}_{5}\left( 1\right) ;{\mathrm{C}}_{5}\left( 1\right) ;$ </td><td> ${\mathrm{C}}_{1}\left( 1\right) ;$ </td><td> ${\mathrm{C}}_{2}\left( 1\right) ;{\mathrm{C}}_{6}\left( 1\right) ;$ </td></tr><tr><td> ${\mathrm{A}}_{2}$ </td><td></td><td>Nil</td><td> ${\mathrm{C}}_{6}\left( 1\right) ;$ </td><td> ${\mathrm{C}}_{4}\left( {0.67}\right) ;$ </td><td> ${\mathrm{C}}_{1}\left( 1\right) ;$ </td><td> ${\mathrm{C}}_{2}\left( 1\right) ;{\mathrm{C}}_{6}\left( 1\right) ;$ </td></tr><tr><td> ${\mathrm{A}}_{3}$ </td><td> ${\mathrm{C}}_{4}\left( 1\right) ;$ </td><td> ${\mathrm{C}}_{4}\left( {0.75}\right) ;{\mathrm{C}}_{5}\left( 1\right) ;$ </td><td>Nil</td><td> ${\mathrm{C}}_{5}\left( 1\right) ;{\mathrm{C}}_{5}\left( 1\right) ;$ </td><td></td><td> ${\mathrm{C}}_{2}\left( 1\right) ;$ </td></tr><tr><td> ${\mathrm{A}}_{4}$ </td><td> ${\mathrm{C}}_{4}\left( {0.75}\right) ;$ </td><td></td><td> ${\mathrm{C}}_{6}\left( 1\right) ;$ </td><td>Nil</td><td></td><td> ${\mathrm{C}}_{6}\left( 1\right) ;$ </td></tr><tr><td> ${\mathrm{A}}_{5}$ </td><td> ${\mathrm{C}}_{4}\left( 1\right) ;$ </td><td> ${\mathrm{C}}_{4}\left( {0.75}\right) ;{\mathrm{C}}_{5}\left( 1\right) ;$ </td><td> ${\mathrm{C}}_{6}\left( 1\right) ;$ </td><td> ${\mathrm{C}}_{5}\left( 1\right) ;$ </td><td>Nil</td><td> ${\mathrm{C}}_{6}\left( 1\right) ;$ </td></tr><tr><td> ${\mathrm{A}}_{6}$ </td><td></td><td> ${\mathrm{C}}_{5}\left( 1\right) ;$ </td><td></td><td> ${\mathrm{C}}_{5}\left( 1\right) ;{\mathrm{C}}_{5}\left( 1\right) ;$ </td><td> ${\mathrm{C}}_{1}\left( 1\right) ;$ </td><td>Nil</td></tr></table>

Fig. 8. Positive constructs matrix derived from FRT in Fig. 6 and its associated distinctions matrix, shown in Fig. 7.

Next, we apply the suggested decision support algorithm (see p. 8) to the information shown in Table 2 and Figs. 6 and 7. We obtain the following information:

 Positive (Pos) and Negative (Neg) matrixes derived from FRT (see Figs. 8 and 9, respectively).

 Positive and Negative relevant factors $( R _ { \widehat { \mu } } ^ { + }$ $R _ { f i } ^ { - } )$ ), and Goodness of each option (see Fig. 10).

According to the information shown in Fig. 10, we recommend the accommodation $A _ { 1 }$ (it is the option with the highest goodness value). The justification of such a recommendation will be:

$A _ { 1 }$ is in good condition and it has a phone, $A _ { 4 }$ is in bad condition and it has no phone.

 $A _ { 1 }$ , its rent is Cheap, $A _ { 5 }$ is Expensive.

<table><tr><td></td><td> $A_1$ </td><td> $A_2$ </td><td> $A_3$ </td><td> $A_4$ </td><td> $A_5$ </td><td> $A_6$ </td></tr><tr><td> $A_1$ </td><td>Nil</td><td></td><td> $C_4(1)$ ;</td><td> $C_4(0.75)$ ;</td><td> $C_4(1)$ ;</td><td></td></tr><tr><td> $A_2$ </td><td> $C_5(1)$ ;</td><td>Nil</td><td> $C_4(0.75);C_5(1)$ ;</td><td></td><td> $C_4(0.75);C_5(1)$ ;</td><td> $C_5(1)$ ;</td></tr><tr><td> $A_3$ </td><td> $C_6(1)$ ;</td><td> $C_6(1)$ ;</td><td>Nil</td><td> $C_6(1)$ ;</td><td> $C_6(1)$ ;</td><td></td></tr><tr><td> $A_4$ </td><td> $C_5(1);C_5(1)$ ;</td><td> $C_5(0.67)$ ;</td><td> $C_5(1);C_5(1)$ ;</td><td>Nil</td><td> $C_5(1)$ ;</td><td> $C_5(1);C_5(1)$ ;</td></tr><tr><td> $A_5$ </td><td> $C_1(1)$ ;</td><td> $C_1(1)$ ;</td><td></td><td></td><td>Nil</td><td> $C_1(1)$ ;</td></tr><tr><td> $A_6$ </td><td> $C_2(1);C_6(1)$ ;</td><td> $C_2(1);C_6(1)$ ;</td><td> $C_2(1)$ ;</td><td> $C_6(1)$ ;</td><td> $C_6(1)$ ;</td><td>Nil</td></tr></table>

Fig. 9. Negative constructs matrix derived from FRT in Fig. 6 and its associated distinctions matrix, shown in Fig. 7.

 $A _ { 1 }$ has a phone, $A _ { 2 }$ has not.  
$A _ { 1 }$ has cooking facilities, $A _ { 3 }$ has not.

<table><tr><td></td><td> $R_{fi}^{+}$ </td><td> $R_{fi}^{-}$ </td><td> $O_{i}^{+}$ </td><td> $O_{i}^{-}$ </td><td>Goodness</td></tr><tr><td> $A_1$ </td><td> $C_1(1);C_2(1);C_3(1);C_5(1);C_6(1)$ </td><td> $C_4(1)$ </td><td>38.4</td><td>0.5</td><td>37.9</td></tr><tr><td> $A_2$ </td><td> $C_1(1);C_2(1);C_3(0.67);C_6(1)$ </td><td> $C_5(1)$ </td><td>35.46</td><td>0.3</td><td>35.16</td></tr><tr><td> $A_3$ </td><td> $C_2(1);C_3(1);C_4(1);C_5(1)$ </td><td> $C_6(1)$ </td><td>18.1</td><td>0.1</td><td>18</td></tr><tr><td> $A_4$ </td><td> $C_4(0.75);C_6(1)$ </td><td> $C_5(1);C_5(1)$ </td><td>0.475</td><td>8.3</td><td>-7.825</td></tr><tr><td> $A_5$ </td><td> $C_4(1);C_5(1);C_6(1)$ </td><td> $C_1(1)$ </td><td>0.9</td><td>20</td><td>-19.1</td></tr><tr><td> $A_6$ </td><td> $C_1(1);C_3(1);C_5(1);$ </td><td> $C_2(1);C_6(1)$ </td><td>28.3</td><td>10.1</td><td>18.2</td></tr></table>

Fig. 10. Information obtained with regard to each option.

$A _ { 1 }$ is near the University and has cooking facilities, $A _ { 6 }$ is far from University and has no cooking facilities.

## 6. Conclusions

In this paper, we have outlined the development of a knowledge-driven Multiple Attribute Decision Making system (MADM) for helping a decision-maker when he is faced with a choice in which the options are clear, that is in discrete decision spaces. Our research has been mainly focused on three aspects, which are:

 Determining the relevant attributes and assessing these attributes.

 Attaching priority or importance to each attribute.

 Processing the previously acquired information, to determine a ranking of each alternative.

Many MADM methods have been developed. Each one has its own characteristics with respect to the way of determining and assessing attributes and describing the preferences or priorities of the individual facing decision-making, the level of uncertainty embedded in the data set, the aggregation function,. . .[10].

We suggest a MADM system that makes use of ideas taken from psychology, knowledge acquisition and artificial intelligence fields in order to determine the relevant attributes. Nowadays, there are MADM methods that use techniques from artificial intelligence, such as data mining, artificial neuronal networks, rule-induction, machine learning algorithms,. . . These rely on the data describing input and output variables, in order to make abstractions, identifying relationships in data and determining the relevant attributes. However, these MADM methods obtain results that are accepted with reticence by the user because they are automatically acquired, without his intervention. We make use of the repertory grid technique and more precisely of the fuzzy repertory table to decrease this reticence. It obtains relevant attributes associated with each option by direct interaction with the user. This is also a difference from conventional MADM methods [2,16,26,30] in which little importance is given to the identification of the relevant attributes or criteria and the values that they can take.

According to the data type (attributes and preferences), the suggested MADM uses a combination of crisp and fuzzy values (see Ref. [9] for a description of fuzzy MADM systems). In the stage of the acquisition of the relevant attributes, the FRT gives license to the decision-maker to express how he usually makes it. He could use crisp and vague attributes, depending on the nature and situation of the problem under study. The vague attributes will be described by means of linguistic terms to address the inherent uncertainty present in his or her mind. Thus, we solve some of the drawbacks of other RGs that have been applied as DSS [5] and classical MADM systems, such as WSM [16], WPM [30], and modern MADM systems, such as AHP [33,34] and MAUT [27], which place a limit on what types of attributes they may have, and what values the attributes may hold, thereby distorting acquired results.

Usually, in the MADM systems [2,16,26,30], the decision-maker attaches weights to the attributes after all the relevant attributes have been found. These systems do not provide enough guidance to do this. Therefore, the resulting option’s score may not be reliable. In the suggested system, a single numerical score is used for attaching priorities (or weights) to attributes, and it is carried out during the development of the FRT, after observing on the distinctions matrix how that attribute is relevant for distinguishing between the various options.

The fuzzy repertory table facilitates the identification of significant characteristics associated with each option [7,8] and assists in priority attachment. We have provided sufficient background information about the fuzzy repertory table to enable the reader to use it. It has been our aim to point out the latent qualities of this technique for successful use in decision support (see Section 3).

We applied an algorithm to process the numerical values so as to determine a ranking of each alternative and recommend an option to the decision-marker. This algorithm selects the option that contains the shortest distance to the ideal solution and the farthest distance from the negative-ideal solution. A new measurement [7] is used to evaluate the relative closeness of alternatives to the ideal solution. It is based on a measurement whose origin is the definition given by the semantic concept between two fuzzy sets, but it is not fuzzy in itself [9,22,31,38] making it understandable by the user of the system. Consequently, this helps to focus the analysis of relevant attributes, making the interaction with the system easier (see Ref. [7]). This is also a difference from similar MADM methods which evaluate the distance among options in a geometrical sense, TOPSIS [26].

Moreover, we extract knowledge from the fuzzy repertory table, the distinctions matrix and the decision-maker’s profile to justify the option chosen. To do this, we make use of two matrixes with positive and negative attributes built from the distinctions matrix. This capability is a way in which the system suggested is different from other conventional MADM methods [2,14,16,26,27,30,31,34], which are weak in explaining their analysis results.

The DSS suggested here could be used in any domain. It has been efficiently tested in small static domains, i.e., domains with a small set of options which have a limited number of attributes. These domains do not have changing attributes over time. Our future goal is to analyze the dynamic properties of options that may influence the choice of given options. We consider that this would be of assistance for the decision-maker.

The decision support system suggested has one drawback, which is rooted in a weakness that is typical to the fuzzy repertory table and repertory grid techniques. The efficiency of these techniques decreases rapidly in proportion to the use of an increasing number of options and attributes (longer grids or fuzzy tables). Our intention is to improve our model with partition capabilities, such as MAUT [27], SMART [15] or AHP [33,34]. That is, we have as our aim the definition of a suitable mechanism for getting additional information from the decision-maker, in order to divide the original problem into several parts. Thus we solve or minimize the drawback of fuzzy repertory grid technique.

## Acknowledgements

This work has been funded by the Spanish Ministry of Science and Technology and Junta de Castilla-La Mancha under Research Projects ‘‘DIMO-CLUST’’ TIC2003-08807-C02-02 and ‘‘PREDA-COM’’ PBC-03-004.

## References

[1] S.L. Alter, Decision Support Systems: Current Practice and Continuing Challenges, Addison-Wesley, Reading, MA, 1980.

[2] R. Benayoun, B. Roy, N. Sussman, Manual de Reference du Programme ELECTRE, Note de Synthese et Formation, vol. 25, Direction Scientifique SEMA, Paris, Franch, 1966.

[3] S.K. Bhatia, Q.A. Yao, New approach to knowledge acquisition by repertory grids, in: B. Bhargava, et al. (Eds.), CIKM 93: Proceedings of the Second International Conference on Information and Knowledge Management, ACM Press, Washington, DC, 1993, pp. 738 – 740.

[4] J.H. Boose, Expertise Transfer for Expert System Design, Elsevier, New York, 1989.

[5] J.H. Boose, Using Repertory Grid-centered Knowledge Acquisition Tools for Decision Support, Proceedings of HICSS-22, vol. III, IEEE Computer Society, 1989, pp. 211 – 221.

[6] J.M. Bradshaw, S.P. Covington, P.J. Russo, J.H. Boose, Knowledge acquisition techniques for intelligent decision systems: integrating Aquinas and Axotl in DDUCKS, in: M. Henrion, et al. (Eds.), Uncertainty in Artificial Intelligence, Elsevier, Amsterdam, 1990, pp. 255– 270.

[7] J.J. Castro-Schez, J.L. Castro, J.M. Zurita, Fuzzy repertory table, a method for acquiring knowledge about input variables to machine learning algorithms, IEEE Transactions on Fuzzy Systems (in press).

[8] J.J. Castro-Schez, N.R. Jennings, X. Luo, N.R. Shadbolt, Acquiring Domain Knowledge for Negotiating Agents: a case of study, International Journal of Human-Computer Studies (in press).

[9] S.J. Chen, C.L. Hwang, Fuzzy Multiple Attribute Decision Making: Methods and Applications, Lecture Notes in Economics and Mathematical Systems, vol. N 375, Springer, Berlin, Germany, 1992.

[10] A. De Montis, P. De Toro, B. Droste-Franke, I. Omann, S. Stagl, Criteria for quality assessment of MCDA-methods, Proceedings of 3rd Biennial Conference of the European Society for Ecological Economics, Vienna, Austria, 2000.

[11] V. Dhar, R. Stein, Intelligent Decision Support Methods: The Science of Knowledge, Pretince-Hall, Upper Saddle River, NJ, 1997.

[12] M.J. Druzdzel, R.R. Flynn, Decision support systems, in: A. Kent (Ed.), Encyclopedia of Library and Information Science, vol. 67 (Suppl. 30), Marcel Dekker, New York, 2000, pp. 120–133.

[13] M. Easterby-Smith, R. Thorpe, D. Holman, Using repertory grids in management, Journal of European Industrial Training 20 (3) (1996) 1 –30.

[14] W. Edwards, How to use multiattribute utility measurement for social decision making, IEEE Transactions on Systems, Man and Cybernetics, SMC 7 (1997) 326 – 340.

[15] J. Evans, The knowledge elicitation problem: a psychological perspective, Behavior and Information Technology 1 (2) (1988) 111 – 130.

[16] P.C. Fishburn, Additive Utilities with Incomplete Product Set: Applications to Priorities and Assignments, Operations Research Society of America Publication, Baltimore, MD, 1967.

[17] K.M. Ford, A. Caas, J. Jones, H. Stahl, J. Novak, J.R. Adams-Webber, ICONKAT: an integrated constructivist knowledge acquisition tool, Knowledge Acquisition 4 (1991) 15 – 41.

[18] K.M. Ford, F.E. Petry, J.R. Adams-Webber, P.J. Chang, An approach to knowledge acquisition based on the structure of personal construct systems, IEEE Transactions on Knowledge and Data Engineering 3 (1) (1991) 78 – 87.

[19] B.R. Gaines, Empirical investigation of knowledge representation servers: design issues and applications experience with KRS, ACM SIGART Bulletin 2 (3) (1991) 45– 56.

[20] B.R. Gaines, M.L. Shaw, New directions in the analysis and interactive elicitation of personal construct systems, International Journal Man-Machine Studies 13 (1980) 81– 116.

[21] J. Gammack, R. Young, Psychological techniques for eliciting expert knowledge, in: M. Bramer (Ed.), Research and Development in Expert Systems, Cambridge Univ. Press, London, 1985, pp. 105 – 112.

[22] O. Gogus, T.O. Boucher, A consistency test for rational weights in multi-criterion decision analysis with fuzzy pairwise comparisons, Fuzzy Sets and Systems 86 (1997) 129– 138.

[23] A.C. Graesser, S.E. Gordon, L.E. Brainerd, QUEST: A model of question answering, Computers and Mathematics with Applications 23 (1992) 733 – 745.

[24] C.W. Holsapple, A.B. Whinston, Decision Support Systems: A Knowledge-based Approach, West Publishing, Minneapolis, MN, 1996.

[25] G.J. Hwang, Knowledge acquisition for fuzzy expert systems, International Journal of Intelligent Systems 10 (1995) 541 – 560.

[26] C.L. Hwang, K. Yoon, Multiple Attribute Decision Making: Methods and Applications, Springer, New York, NY, 1981.

[27] R.L. Keeny, H. Raiffa, Decision Making with Multiple Objectives: Preferences and Value Tradeoffs, Cambridge Univ. Press, Cambridge, UK, 1993.

[28] G.A. Kelly, The Psychology of Personal Constructs, Norton, New York, 1955.

[29] J. McDonald, D. Dearholt, K. Paap, R. Schvanevedt, A formal interface design methodology based on user knowledge, in: L. Curtis, B. Curtis (Eds.), Proceedings of the SIGCHI Conference on Human factors in Computing Systems (CHI 86), ACM, New York, NY, 1986, pp. 285–290.

[29] J. McDonald, D. Dearholt, K. Paap, R. Schvanevedt, A formal interface design methodology based on user knowledge, in: L. Borman, B. Curtis (Eds.), Proceedings of the SIGCHI Confer-

ence on Human factors in Computing Systems (CHI 86), ACM, New York, NY, 1986, pp. 285–290.

[30] D.W. Miller, M.K. Starr, Executive Decisions and Operations Research, Prentice-Hall, Englewood Cliffs, NJ, 1969.

[31] G. Munda, Multicriteria Evaluation in a Fuzzy Environment, Physica-Verlag, Heidelberg, 1995.

[32] D.J. Power, Supporting decision-makers: a expanded framework, Proceedings of Informing Science Conference, Krakov, Poland, 2001.

[33] T.L. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, USA, 1980.

[34] T.L. Saaty, Multicriteria Decision Making: The Analytic Hierarchy Process, RWS Publications, Pittsburg, 1992.

[35] G. Schreiber, H. Akkermans, A. Anjewierden, R. Hoog, N. Shadbolt, W. Van de Velde, B. Wielinga, Knowledge Engineering and Management: The Common KADS Methodology, Massachusetts Institute of Technology Press, Cambridge, MA, 2000.

[36] N.R. Shadbolt, A.M. Burton, The empirical study of knowledge elicitation techniques, SIGART Newsletter 108 (1989) 15 – 18.

[37] M.L. Shaw, B.R. Gaines, WebGrid II: developing hierarchical knowledge structures from flat grids, Proceedings of Eleventh Workshop on Knowledge Acquisition, Modeling and Management (KAW’98), Banff, Alberta, Canada, 1998.

[38] E. Triantaphyllou, C.T. Lin, Development and evaluation of five multiattribute decision-making methods, International Journal of Approximate Reasoning 14 (1996) 281 – 310.

[39] A. Tversky, L. Gati, Similarity, separability and the triangle inequality, Psycological Review 89 (2) (1982) 123– 154.

[40] L.A. Zadeh, The role of fuzzy logic in the management of uncertainty in expert systems, Fuzzy Sets and Systems 11 (1983) 197– 227.

![](/api/attachments/KBJTAPTP/fulltext/images/e87575520e0f87af8a240b8d2341a78436b290122ac1a4e197d363465c48564e.jpg)  
Jose J. Castro-Schez received the MS degree in 1995 and PhD degree in 2001 from the Computer Science Department at the University of Granada (Spain). He is an Associate Professor of Computer Science at the University of Castilla-La Mancha, Ciudad Real (Spain). His research interests include: knowledge acquisition, machine learning, decision support, electronic commerce and issues of representation in AI. He is author of numerous papers on AI-related subjects.

![](/api/attachments/KBJTAPTP/fulltext/images/e8dd69ae7e46e1041f1c22b2eae29f7cde8fe58c18dcc8fc253a2b2b60bb5ab4.jpg)

Luis Jimenez is an Associate Professor of Computer Science at the University of Castilla-La Mancha, Ciudad Real (Spain), where he founded and directs the ORETO Group. He received the MS degree in 1991 and PhD degree in 1997 from the Computer Science Department at the University of Granada (Spain). His main fields of interest are fuzzy logic, knowledge-based systems, machine learning and related applications, leading several research proj-

ects on these topics. He is a member of European Society of Fuzzy Logic and Technology (EUSFLAT).

![](/api/attachments/KBJTAPTP/fulltext/images/a5c547ccfc73d132292c8081843463ac9bc0a2acc63fa0f24b229277e760e34e.jpg)

Juan Moreno is an Associate Professor of Industrial Engineering at the University of Castilla-La Mancha, Toledo (Spain). He received a BE degree from the University of Castilla-La Mancha in 1992, MS degree from the University of Murcia in 1996 and PhD degree from the University of Castilla-La Mancha in 2002. His main fields of interest are fuzzy and linguistic modeling, dynamic systems modeling, fuzzy logic and neural networks.

![](/api/attachments/KBJTAPTP/fulltext/images/d9db1cf7a1ef75519f652a38c2410ecea966e35f48ab6b6f14d63303417899ec.jpg)

Luis Rodriguez graduated with an MS degree from the Computer Science Department at the University of Granada (Spain) in 1997. He is an Assistant Professor of Computer Science at the University of Castilla-La Mancha, Almaden (Spain). The interest of his current research includes computer vision, decision support, movements recognition and fuzzy and linguistic modeling. He is preparing a PhD thesis on movements recognition on

the image streams coming from the camera serves under the guidance of Dr. Luis Jimenez.
