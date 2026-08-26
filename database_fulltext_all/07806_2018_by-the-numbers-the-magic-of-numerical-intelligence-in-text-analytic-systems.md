---
otero_id: 7806
otero_key: "92ZU6XEZ"
title: "By the numbers: The magic of numerical intelligence in text analytic systems"
authors: "Richard Gruss; Alan S. Abrahams; Weiguo Fan; G. Alan Wang"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.07.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# By the numbers: The magic of numerical intelligence in text analytic systems<sup>☆</sup>

![](/api/attachments/92ZU6XEZ/fulltext/images/c93753362ac1eb2420d9a76b62cc25396249f7ff2e6c626613cb9199b357d9ad.jpg)

Richard Gruss<sup>a,⁎</sup>, Alan S. Abrahams<sup>b</sup>, Weiguo Fan<sup>c</sup>, G. Alan Wang<sup>b</sup>

<sup>a</sup> Department of Management, College of Business and Economics, Radford University, Radford, VA 24142, USA

<sup>b</sup> Department of Business Information Technology, Pamplin College of Business, Virginia Tech, Blacksburg, VA 24061, USA

<sup>c</sup> Department of Management Sciences, Tippie College of Business, University of Iowa, Iowa City, IA 52242, USA

## A R T I C L E I N F O

Keywords: Text analytics Information retrieva Numerical attributes Defect discovery

## A B S T R A C T

There is a growing recognition among MIS researchers and practitioners that social media provide a valuable source of business intelligence. Unearthing relevant and useful information among the voluminous postings remains a challenge, however. Automated methods based on text mining have made signi<sup>fi</sup>cant progress in recent years by discovering a variety of new methods and features. This study adds to this stream by introducing a novel text mining procedure centered around numerical expressions contained in text documents. In this method, numerical expressions are extracted, categorized, and binned, and their presence and magnitude are stored as document features. We demonstrate, using a case study from the automotive industry, that numerical expressions can be reliably identi<sup>fi</sup>ed, and that these numerical features enable improvements in document classi<sup>fi</sup>cation. As an extension to this case study, we contribute a decision support system for managing product quality using both textual and numerical attributes.

## 1. Introduction

The recent surge of academic interest in the use of social media re<sup>fl</sup>ects the growing role of customer to customer (C2C) communications as a resource for data-driven business decision making. Researchers are discovering e<sup>fi</sup>cient methods for businesses to <sup>fi</sup>nd, among the vast quantities of social media postings, opportunities for innovation [39], manufacturing defects [2,4,24,39,49], and un anticipated consumer safety issues [46].

Although several approaches for locating high quality content have been explored using social network analysis (SNA), most of the in formation in social media is expressed as unstructured text, and therefore many promising techniques are contributed by text mining (TM) and natural language processing (NLP). Some text-based methods that have proven e<sup>f</sup>ective include term prevalence metrics [2,24,46], latent Dirichlet allocation (LDA) [17,40], and ensemble methods [26].

One token type that is largely ignored in text analytic research is the numeric type. A number by itself conveys very little information, be cause the lexical token alone does not provide context for understanding its referent or the signi<sup>fi</sup>cance of its magnitude. For example in the two snippets “I was traveling at 25mph …” and “I was going at 15 miles per hour …”, a typical token-based approach would extract only unigrams like “25”, “15”, “mph”, and trigrams like “miles per hour”. These disjoint tokens hold little information value, as “mph” is not associated with “miles per hour” and the relative magnitude of 25 vs. 15 vs. other speed values is not recognized. In contrast, a numeric information extraction approach would recognize that both snippets are distinct expressions of measures of “vehicle speed”, and that the authors were describing travel at “low” speeds (e.g. relative to say 80 mph travel).

This study aims to <sup>fi</sup>ll this gap by proposing a procedure for creating a set of numerical features that communicate information about the semantics of numbers. We demonstrate the value of this approach with a case study in automotive defect identi<sup>fi</sup>cation.

When key terms are extracted using prevalence metrics as in [4], numbers sometimes appear in the list of n-grams that are signi<sup>fi</sup>cantly associated with the target class. These numbers are usually removed from curated term lists on the grounds that they communicate little information in isolation. Likewise, important numerical terms might not make it onto prevalent term lists because that particular value ap pears too infrequently when regarded solely as a lexical token. Furthermore, because the token alone is recognized, and not similar values, new examples would be incorrectly classi<sup>fi</sup>ed if the token value in the new observation is even slightly di<sup>f</sup>erent from past observations.

Consider, ${ } ^ { \mathfrak { a } } 1 5 ^ { \mathfrak { n } }$ and $\boldsymbol { \mathfrak { s o } } 5 ^ { \mathfrak { n } }$ in the example above: these would typically have insu<sup>fi</sup>cient prevalence to make it onto the prevalent terms list, as the distinct values are peculiar to each observation. However, once recognized as examples of “low speed”, the semantic concept of “low speed” may indeed have unusually high prevalence in a target class of documents that contain, for example, automobiles with manufacturing defects. The document feature set would include, instead of simply a “most prevalent terms” list, a “most prevalent semantic concepts” list. Furthermore, a new observation where the user is traveling at 10 mph or 20 mph would be correctly recognized as falling into the same category of low speed travel (compared to “10” and “20” being distinct and hitherto unseen tokens, in a conventional token-recognition ap proach, which would fail to recognize the signi<sup>fi</sup>cance of these values).

This study is an attempt to enrich the document feature set by assigning categories to numbers based on their function in the text. Signi<sup>fi</sup>cant n-grams (strings of words of length n), or “Smoke words,” introduced in [4], are marker terms that are substantially more prevalent in the target class of text documents than in the non-target class. Their original use case was in di<sup>f</sup>erentiating online postings indicative of manufacturing defects in automobiles. While our case study speci-<sup>fi</sup>cally involves the automotive industry, we maintain that this procedure is generalizable to any domain with a large variety of meaningful numerical attributes.

Tools that make use of numerical expressions in NLP tasks typically follow a procedure in which entities are <sup>fi</sup>rst located using Named Entity Recognition (NER), and then numerical attributes are attached based on textual proximity. The goal in this methodology is to build a database of entities with a structured representation. For example, in the sentence, “We tested an all-wheel-drive XLE model as well, which also delivered more than its 24-mpg promise.” [1], “XLE” would be identi<sup>fi</sup>ed as a car model, and the algorithm would need to add “mpg = 24” to that entity. An example of this approach can be found in [7]. Our approach di<sup>f</sup>ers in that we <sup>fi</sup>rst <sup>fi</sup>nd the numbers, learn their magnitude and units, and create indicators on the level of the social media posting. For example, instead of storing the fact that the XLE has an mpg of 24, we store the fact that a high mpg was mentioned in the posting. Our representation of the posting retains the original extracted value, but in addition, we discretize the value also, as that is informative for defect classi<sup>fi</sup>cation and for slice-and-dice drill-down of the textual dataset by numeric bands (e.g., rapidly <sup>fi</sup>nding all postings mentioning high fuel e<sup>fi</sup>ciency vehicles).

This paper addresses three main research questions. First, can a reasonably-sized set of domain-speci<sup>fi</sup>c numerical attributes be identi <sup>fi</sup>ed for a given industry? Second, can these numbers be processed and interpreted automatically? Third, are these numbers useful for general information mining tasks? We demonstrate via a case study that the answer to all of these questions is yes.

Our primary contribution is methodological. We propose a procedure for identifying and classifying a set of domain-relevant numerical attributes with a high level of precision and recall. Furthermore, we demonstrate how these numerical attributes can be combined with key term extraction to achieve improved performance in defect isolation tasks.

The rest of this paper is organized as follows. In Section 2, we provide our theoretical motivation and make the case for generalizability. In Section 3, we review related work in processing numerical attributes. In Section 4, we detail the procedure for numerical attribute extraction and classi<sup>fi</sup>cation. In Section $^ { 5 , }$ we demonstrate how the procedure works using a case study in the automotive industry, evaluating the e<sup>f</sup>ectiveness of the numerical attributes in locating defects in social media postings relative to earlier approaches that were all agnostic to numerical attributes. In Section 6, we further demonstrate the procedure's utility within this case study by proposing a Post Market Defect Surveillance System that o<sup>f</sup>ers a dynamic interface for exploring a social media data set using numerical attributes as <sup>fi</sup>lters and facets. In Section 7, we discuss limitations and future work. Finally, in Section

8, we discuss our conclusions and implications for research and practice.

## 2. Theoretical rationale

We contend that by advancing from a strictly lexical treatment of a numerical token to an interpretation of the number's function and magnitude, we are endowing a text analytic system with some degree of semantic understanding. Many attempts to add semantic comprehension to text classi<sup>fi</sup>ers have been inspired by <sup>fi</sup>ndings from cognitive science about how humans process meaning. The methods of arti<sup>fi</sup>cial intelligence, in many cases, were derived by de<sup>fi</sup>ning the processes of human intelligence (however narrowly) and approximating them computationally. Examples from natural language processing (NLP) include word sense disambiguation, topic analysis, named entity recognition, and recognizing textual entailment. We argue that our procedure of extracting and binning of numbers would add numerical intelligence to a variety of tasks in several domains, and we make our case from three perspectives: numeracy, speci<sup>fi</sup>city, and semantic richness.

Numeracy, which normally develops in childhood [12], is a basic understanding of numbers and their magnitudes. A variety of mental competencies are associated with numeracy, including estimating, ranking, understanding probabilities and making comparisons. People who are numerate are less likely fall prey to the biases that lead to poor decisions [34]. A lack of numeracy has been associated with making poor health decisions [42] and defaulting on a mortgage [16]. An estimation of magnitudes is a fundamental part of human intelligence, and our procedure is an attempt to add this competency to NLP systems.

Another reason why numerical intelligence can aid a variety of NLP tasks is that numbers represent an enhancement of speci<sup>fi</sup>city. Human language can be abstract and ambiguous, and so utterances that are speci<sup>fi</sup>c and concrete provide an opportunity for natural language parsers. When people make reference to numbers, they are producing evidence about a speci<sup>fi</sup>c case. For example, compare “my car doesn't start on cold mornings” to my “2002 model 56x doesn't start when it falls below 32°.” In addition to establishing their own credibility and competence, the speakers are acknowledging the particularity of their case, and this particularity should be leveraged for its information content.

Our third theoretical basis for generalizability has to do with semantic richness. In cognitive science, “semantic richness” refers to the amount of information associated with a concept [22] and is a function of the variability of that concept's usage and contexts. Three measures of semantic richness are commonly used: 1) number of semantic neighbors (NSN), 2) number of features (NOF), and 3) contextual dispersion (CD). NSN refers to the number of words that are used in a similar context to the focal word, NOF refers to how many di<sup>f</sup>erent attributes of the concept are available in memory, and CD refers to the number of di<sup>f</sup>erent contexts in which the word is commonly used.

Several experiments have con<sup>fi</sup>rmed that words that are semantically rich are understood more quickly and accurately than those that are semantically impoverished. People are able to perform lexical decision and categorization tasks faster and more accurately for more semantically rich words [35–37,48]. When a word with few semantic neighbors, few features, and few contexts is presented to a person, more e<sup>f</sup>ort is required to arrive at an understanding of the word's meaning.

The aspect of semantic richness most applicable to machine learning is the number of features (NOF). The “features” of a concept are simply attributes that are associated with it, such as, for “grapefruit”, < is a fruit > and < is healthy > . [31] found that people are able to list more features of some words than for others. High-NOF words are comprehended more quickly and accurately than low-NOF words [18,48]. An advance in the semantic information supplied to a machine, therefore, is to add features to concepts. In our case study, we take numerical tokens from automobile postings and add features to them. For example, “200” is the lexical token, but we add features “ < is a number $> { ^ { \eta } , ^ { \alpha } < }$ < is a speed $> " ,$ , and $^ { * } <$ < is a high speed $> . ^ { \mathfrak { n } }$ The ad dition of these features aids the semantic richness of the text as it is presented to the machine, and aids in the machine's “understanding.”

Other number-intensive industries, with potential use cases for number extraction projects. Note that the typos in column two exist because we have captured the original text, verbatim, to illustrate the messiness of the source data and need for e<sup>fi</sup>cient and reliable number extraction and classi<sup>fi</sup>cation from messy usergenerated source data.

<table><tr><td>Industry</td><td>Example number snippets</td><td>Frequent type</td><td>Project</td></tr><tr><td>Food</td><td>French Vanilla Pump Bottle, 1.5 L ( Pack of 2Licorice Laces - Red, 6 lbs :18-Count Pods ( Pack of 4)28 Individually Wrapped - 28Oz Total Food, 650 mg,150 VegetarianCapsules is approximately 140–150 calories drawback is 18 g of sugar per bottle</td><td>Package sizeServing sizeCalorie countNutrition info</td><td>Track problematic packaging, what nutrition information people are concerned with; understand competitors&#x27; or consumers&#x27; actual or preferred serving sizes or bulk quantity sizing; understand threshold limits for consumer&#x27;s nutrition concerns (excess sugar or calories)</td></tr><tr><td>Power tools</td><td>The Porter-Cable brand 4.5inch X 10 yard great deal for almost $ 100I purchased the Dremel 709–11 110pc accessory kit this is a 3rd rate product be carefulMANY USES OVER THE PASED 15 YEARS that is a 3 cutter head through were about 6 to 10 inches wide needed or is the 20 amp breaker in storage shed about 50 feet from my shop</td><td>Part sizePricePackage quant.RatingCustomerloyalty timeElectrical</td><td>Adjust warranty coverage based on time to failure; understand consumer&#x27;s size (fit), compatibility (e.g. voltage), and capacity (e.g. length) needs; understand assortment variety (e.g. different kit pieces; different cutter heads); identify focal product models, particularly for competitor comparison and compatibility concerns.</td></tr><tr><td>Electronics</td><td>Compaq Presario with 2 USBI have a 60 MB zip file on myI purchased this 15 ft . Mediabridge HDMI cable we were getting almost 100 m stream to the tv s switched to the cat5 connectivity cousin owns a Viewsonic Pro8500 and even he changed in perspective from 16x10 to 16x9 disks all the way to 2 TB without breaking a sweatI&#x27;m using Windows 7 (64 bit)</td><td>Memory sizeNetwork speedModel numberData storageOS version</td><td>Determine which equipment consumers are using in what combinations; understand size, compatibility and capacity (e.g. length or data volume or speed) needs; identify focal models for compatibility fixes. Identify focal competitor models consumers are using for comparison.</td></tr><tr><td>Car seats</td><td>seat that accommodates 30 or 35 poundsAddendum : At 9 months he is still s they go out at 90deg from the back less than 1 inch of movementI am 5 1/2 months pregnantIn 2012, 32 children in the United replacing a sub-$100 seat from a large seat of our BMW 530i and VW New Jetta</td><td>Child weightChild ageSeat anglePriceModel number</td><td>Detecting unsafe usage, such as improper size for child; understand buyer or user age, seat fit, price comparisons; identify focal vehicle models (e.g. for prioritizing compatibility fixes)</td></tr></table>

The perspectives of numeracy, speci<sup>fi</sup>city, and semantic richness provide theoretical justi<sup>fi</sup>cation for our procedure's broad applicability.

To demonstrate the centrality of numerical intelligence to several domains, we provide examples of numerical attributes from other industries and suggest relevant analytical projects. Table 1 below shows a sample of snippets extracted from a collection of Amazon.com reviews. Any industry whose online text tends to be dense with numbers could <sup>fi</sup>nd a promising application of this method.

## 3. Related work

The automatic identi<sup>fi</sup>cation and interpretation of numerical quantities is helpful in variety of NLP tasks. It is a critical subtask within question answering (QA) [27]. For example, in the 2002 TREC-10 QA contest, Hovy [20] showed the importance of constraining answers according to sensible ranges for the target variable; $\mathbf { e . g . , }$ , a nation's population should not be a small number like 10. [6] extended this reasoning and argued that numerical expressions can be viewed as a random sample following a Gaussian distribution, and therefore prob abilities can be assigned to individual realizations. For example, in our case study below, numbers around 60 are likely for a speed (in mph), but numbers > 140 are multiple standard deviations too high.

Learning the numerical attributes associated with physical objects can help with certain inferential tasks. For example, knowing the typical dimensions of a strawberry can help a computer vision algorithm to decide whether to label a red object in an image as a strawberry [45]. [11] showed that the application of knowledge about object dimensions can help select the appropriate numerical expressions in a sentence when there are several candidates. In this experiment, distributions of sensible size and weight ranges for physical objects were mined from web text by searching for similar objects using WordNet; for example, “apple” and “elephant” would have a signi<sup>fi</sup>cantly di<sup>f</sup>erent distribution of sizes. The notion of sensible distributions of numerical attributes was termed “numerical common sense” in [32]. In this study, the researchers were able to determine whether a number was uncommonly large, small, or normal, based on context (“the camera weighs only 2 pounds”). [8] used web mining to aggregate numerical references to a particular object and form tight intervals around an answer to a magnitude question.

Domain-speci<sup>fi</sup>c numerical quantities have been examined in [29,43] but the emphasis in these works is on accurate extraction, rather than on evaluating applications.

To our knowledge, this number-centric approach has not been tested in previous text analytic studies. Also, we know of no research that speci<sup>fi</sup>cally assesses impact of numerical attributes on the performance of text-based classi<sup>fi</sup>cation systems. This study aims to <sup>fi</sup>ll this gap, using the highly-complex automotive domain as an illustrative case.

## 4. Procedure for adding numerical attributes

The procedures for adding numerical features to text documents are speci<sup>fi</sup>ed in Listing 1 and diagrammed in Fig. 1. Steps 1–4 involve building the number classi<sup>fi</sup>er using a textual training set and verifying the classi<sup>fi</sup>er's accuracy. The goal of step 5 is to create a lookup table so that extracted and categorized numbers can be classi<sup>fi</sup>ed according to their magnitude. In Step 6, the classi<sup>fi</sup>er and lookup table are employed to add features to new documents. Each step is detailed and demonstrated in the case study in Section 5.

## 5. Case study: automobile defect detection from social media

We demonstrate the utility of our approach by means of a case study. Our chosen case study extends the research into using social media postings to <sup>fi</sup>nd manufacturing defects in automobiles [2–4].

Social media postings are increasingly recognized as a source of useful business intelligence, and lately there has been interest in using them for quality management, particularly in post market defect surveillance. In this case study, we use our procedure to extract, categorize, and bin numerical attributes in social media postings related to automobiles and demonstrate how these attributes improve e<sup>f</sup>ectiveness of systems designed to detect manufacturing defects. For example, our system can compare the age of cars, comprehend when a speed outside of the normal range, or recognize a voltage that not commonly associated with a model year. It can also combine numbers to make sophisticated observations, so for example it can deduce that in cars with high miles per gallon, a certain component lasts an unusually long time.

Listing 1 Proposed procedure for adding numerical attributes.

<table><tr><td>1. Obtain a representative sample of text documents.2. Hand-tag numerical expressions:a. Formulate an ontology of number categories.b. Hand-tag numbers according to categories.c. Check inter-rater reliability.d. Revise ontology and re-tag as needed.3. Build a classifier to automatically categorize number expressions, using surrounding text.4. Evaluate classifier:a. Ensure sufficient precision, accuracy, F1, and AUC.b. Drop numbers with insufficient performance.5. Create bin cutoffs:a. Standardize units.b. For each number category, create a distribution of values observed.c. Determine thresholds between useful bins (e.g. “high”, “medium”, and “low”).d. Store table of cutoffs as a reference for downstream processing.6. Deployment and indexing new documents:a. Extract numbers using regex.b. For each number:i. Use trained classifier to identify number category.ii. Use lookup table from 5 to bin number.iii. Add numerical feature to document feature vector (e.g., “high RPM = true”).</td></tr></table>

The surveillance of social media for product safety has been an especially rich area of investigation, due to the challenges presented to regulators such as the National Highway Tra<sup>fi</sup>c Safety Administration (NHTSA), the Food and Drug Administration (FDA) or the Consumer Product Safety Commission (CPSC). Unlike <sup>fi</sup>rms, which might monitor social media activity for themselves and a few key competitors, regulators have a mandate to oversee several industries, often with extremely limited resources. Automated methods for <sup>fi</sup>ltering out noise are especially needed in this case.

The most formidable challenge in using social media, especially for regulatory organizations, is the sheer volume of User Generated Content (UGC) being produced every day [3]. Latest numbers indicate that Amazon has over 140 million product reviews [30], TripAdvisor has over 570 million (TripAdvisor.com), and Yelp has over 142 million (https://www.yelp.com/press). Any system that aims to simplify the discovery of useful information in social media must provide an e<sup>f</sup>ective means of <sup>fi</sup>ltering out noise and leaving a manageable subset of user postings for further processing by human readers.

Several studies have proposed intelligent means of sifting through social media content for particular information needs. Methods have been proposed to predict stock market activity [25,33], discover socially important locations [13], <sup>fi</sup>nd important information for crisis management [38], and gauging customer response to business ads [21], to name only a few.

![](/api/attachments/92ZU6XEZ/fulltext/images/593a37a05dda2dc5096341b86179c25886d3ddd3251e37d7bf984da218fcf90f.jpg)  
Fig. 1. Proposed procedure for creating numerical features.

One area of active research is the application of text analytic methods to the detection of hazardous product defects in social media. A framework recommending a set of lexical, stylistic, social, sentiment, product, term, and semantic features was introduced in [2] and con-<sup>fi</sup>rmed in [5,24,46]. A consistent <sup>fi</sup>nding among these studies is that distinctive terms, product features, and semantic attributes are helpful to distinguish defects, but stylistic and sentiment features are not. This approach was later extended with a set of contextual features and ensemble methods in [26], and with heuristic methods in [17]. A procedure for identifying vehicle components to enrich the information set was proposed in [3]. [9] proposed an unsupervised method of defect detection using unlabeled Amazon.com reviews combined with “posi tive” labeled documents from the CPSC website SaferProducts.gov. Their positive unlabeled learning (PUL) approach provides an improvement in accuracy and a reduction in labor and may suggest interesting future directions. The [43] study deals speci<sup>fi</sup>cally with automotive numerical attributes, but the ontology is restricted (year, price, and mileage) and the technique makes heavy use of the structural elements of a classi<sup>fi</sup>ed ad. Our approach employs a greater variety of numerical attributes, and recognition is not dependent on the structural elements of the document.

In the sections that follow, we demonstrate step-by-step the proce dure speci<sup>fi</sup>ed in Listing 1 above.

## Step 1. Obtain a representative sample of text document

The classi<sup>fi</sup>er training data set is described in [4], and includes 1500 discussion threads each from Honda-Tech.com, ToyotaNation.com, and ChevroletForum.com, for a total of 4500 threads.

## Step 2. Hand-tag numerical expressions

113,355 numbers were extracted using the regular expression [−+]?[A-Za-z] ∗ \ d+[A-Za-z] ∗ [\.]?[\,]? \ d∗, along with a context of 40 previous tokens and 40 subsequent tokens. 35,000 of these “number snippets” were randomly selected for human tagging. Listing 2 gives examples of number snippets.

A pilot study was conducted to establish a comprehensive list of number types. 52 undergraduate business students tagged postings from online automotive postings using an initial trial set of 11 number types. Taggers were instructed to write in the number type if the number did not <sup>fi</sup>t into any of the given categories.

Based on the results of this pilot study, a list of 45 number types was stabilized for <sup>fi</sup>nal tagging: Address, Age of Vehicle, Age of Person, Age Other, Calendar Date, Calendar Day, Calendar Month, Calendar Year, Chemical Symbol, Count of Doors, Count of Vehicles, Count Other, Distance, Dollar Amount, Electrical, Piston Count, Piston Size, Error Code, Fuel E<sup>fi</sup>ciency, Horsepower, Length/Height Measure, Listing, Model Number of Component, Model Number of Vehicle, Model Year, Odometer Reading (# Miles),Passenger Capacity, Percent, Phone, Rank, Rating, Speed, Temperature,Time of Day, Time Duration, Tire Model, Tire Pressure, Torque, Transmission, VIN, Volume, Weight, Wheel Drive, Word, Other.

Using the dataset of 35,000 number snippets, 109 Master of Information Technology students were given extra credit to tag numbers using PamTag, a web-based collaborative tagging tool (https:// pamtag.pamplin.vt.edu/pamtag/description.html). 74 taggers completed the minimum of 200 tags. A gold standard authority set of 927 tags was completed by the lead researcher to check tagger accuracy, and all submissions from taggers with < 50% agreement with the authority were discarded. After poor performers were dropped, the <sup>fi</sup>nal set consisted of 20,850 tags (for 19,815 distinct number snippets). Tag comments were inspected for common problems. 104 tags marked “other” contained comments that they were “RPM” (Revolutions Per Minute) readings, so RPM was added as a number type. 61 tags indicated that the number referred to a gear, and 50 tags indicated that the number referred to an oil grade (e.g., 10w40), so Gear and Oil Grade were also added as potentially signi<sup>fi</sup>cant number types. It was also observed that automobile community participants frequently referred to the car model by its generation (“1st gen”, “2nd gen”, etc.), so Generation was added where appropriate. After these adjustments, average tagger agreement with authority was 74% (μ = 0.74, σ = 0.17).

788 number snippets were tagged by 2 or more taggers (max = 4), and inter-rater reliability was strong, with a Cohen's κ of 0.72, indicating “substantial agreement” [23]. In cases where taggers disagreed, con<sup>fl</sup>icts were resolved using the following rules: 1) If there was an authority tag, it overruled the others. 2) If there was no authority tag, majority won. 3) If there was a tie, the lead researcher (authority tagger) selected the <sup>fi</sup>nal tag. A total of 19,815 distinct number snippets were tagged from 5434 threads. Count of numbers per thread ranged from 1 to 257 with an average of 3.6 number snippets per thread.

An analysis was conducted to see which number types gave taggers the most di<sup>fi</sup>culty. Several numbers achieved 100% agreement: temperature, calendar day, tire pressure, rating, word, age of vehicle, rpm, oil grade, volume, weight, date, odometer reading, and door count. Numbers that had > 70% agreement included dollar amount, model year, time duration, speed, error code, piston count, transmission, chemical symbol, wheel drive, gears, and length. Numbers with < 60%

## Listing 2

Examples of number snippets extracted from social media postings. Focal number snippet example is shown in square brackets [ ] after number type, and full context is then shown with focal number snippet indicated between ‘===’ markers.

Model Year: [ 1998 ] weak ABS question … Im stumped Well This is not often I need help but this one got me . I know a lot of you guys are gods with honda wring so here we go . -Everything Was Fine (===1998===Honda Civic)-Parked car for a week to remove dash-After replacing Dash, Airbags, ECU, and ABS COntrol module, I have ABS Light-Had An SRS light to but I reset that with a

Transmission: [ 5-speed ] are the location of starter relay, clutch start switch and oxygen sensor ( bank 1 sensor 1 and sensor 2 ) . Thank you, Is the clutch in all the way ? I just got a 2004 Matrix ===5-speed=== and unless I have the clutch down ALL the way to the <sup>fl</sup>oor it will not start either . ^Good point . In most cases , it s simply the button on the <sup>fl</sup>oor that is n t depressed

Distance: [ \~650 km ] the bobber or something 1996 Corolla 1.66 L - about 400 miles but I travel about 360 mi HWY once a week . I went on a few trips over the summer in my 97 AE102 and had consistently gotten ===650\~km===or so on 90 /10 % highway/city driving . I still had about 1/8th of the tank left though . I shall start =) 96 DX 1.8 L 4 speed auto . I get approx . 325 miles with

agreement were dropped from the analysis. The following categories were dropped, either because the agreement was too low or because too few examples were available in the training set to ascertain reliability: Calendar Year, Rank (1st–2nd), Age Other, Age of Person, VIN (Vehicle Identi<sup>fi</sup>cation Number), Calendar Month, Passenger Capacity, and Word. The “Word” category comprises inventive respellings of common words with numbers substituted for letters, and examples include b4, st00pid, 2, ub3r, w00t, any1, 4 (for), y0, inf0, 0well, n00bs, and ph00kin. These are not really numbers, and their inclusion in the tag ging was strictly to allow taggers to accurately interpret these numbers.

After problematic categories were dropped, 19,431 distinct numbe snippets remained. The lead researcher inspected the miscellaneous categories (“Other” and “Count of Other”) to check for mis-taggings and potential new number categories. Based on the frequency of octane mentions, another new category was created for “Fuel Octane”, consisting of 81 new observations. The most common number types were Model Year (3944), Model Number of Component(2106), Other(1519), Count Other(1358), Dollar Amount (925), Model Number of Vehicle (873), Time Duration (810), Odometer Reading (765), Listing (699), Engine Piston Count(649), and Engine Cylinder Size(484).

The miscellaneous categories were dropped, as they were too heterogeneous. Due to the extreme imbalance in the representation frequency of the number classes, the classes were either sub-sampled or bootstrapped<sup>1</sup> to create a set of 300 instances of each number category, except for Rating, Address, and Calendar Year, which had very few instances (< 20). Imbalanced classes introduce problems in classi<sup>fi</sup>cation algorithms [10], and resampling has been shown empirically to be an e<sup>f</sup>ective way of handling class imbalance [28].

## Step 3. Build a classifier

A series of Naïve Bayes (NB) document classi<sup>fi</sup>ers were built using Python 2.7.6 using the Natural Language Toolkit(http://www.nltk.org). NB classi<sup>fi</sup>ers use Bayes' Theorem to probabilistically determine an in stance's class membership based on features of training instances [44]. In this case study, the tagged numbers were the class labels, and the surrounding text constituted a feature set.

Morphological attributes of the number itself played a key role in its classi<sup>fi</sup>cation. Several numbers were discernable based solely on char acters. For example, single-characters helped signal dollar amount (‘\$’), odometer readings (‘k’), oil grade (‘W’), percent (‘%’), and error codes<sup>2</sup> (which usually start with ‘P' or ‘U' or ‘B'), time of day (‘:’); double character sequences marked cylinder con<sup>fi</sup>gurations (‘I4’, ‘V8’), lengths (‘mm’, ‘cm’, ‘ft’) and gears (‘st’, ‘nd’, ‘rd’); and triple character sequences marked model generation (‘gen’), Pressure (‘psi’), speed(‘mph’), and RPM (‘rpm’). These characters were often appended or prepended to the numerical token without spaces.

In addition to character sequences, the magnitude of the number also revealed something about its class. For example, “Count Other” was rarely larger that 10 (“5 times”, “3 wires”, “4 lug nuts”, “2 engines”, etc.), whereas Odometer was rarely smaller than 10,000. Horsepower ranged from 100 to 400, and Fuel Octane was always 85–93. Therefore, character sequences and number magnitude were critical features in our classi<sup>fi</sup>cation.

Eight multinomial Naïve Bayes classi<sup>fi</sup>ers were constructed on automatically-extracted features based on widening windows of term around the focal number. Metrics were calculated using scikit-learn (http://scikit-learn.org/). For each classi<sup>fi</sup>er, a fresh 80–20 train-test split was created from the tagged data. The <sup>fi</sup>rst classi<sup>fi</sup>er used only morphological elements of the term itself (character sequences of length 1,2, and 3), and the others used token window widths of 1, 2, 3, 4, 5, 6, and 7 terms on either side. The complete process for building the number classi<sup>fi</sup>er is detailed in Fig. 2 below.

Number expressions were tokenized on white space and were preserved as strings including all characters, $\mathrm { e . g . , }$ “15mph”, during classi<sup>fi</sup>cation, to leverage helpful character sequences. Obtaining the number magnitude for binning by stripping out non-numeric characters was delayed until the numbers were extracted and classi<sup>fi</sup>ed from the full set. Feature sets consisted of the character sequences of length 1, 2, and 3 that occurred > 20 times in the numbers in the training data. Word sequences of varying length (1–7) from a window around the number were also used. The vocabulary for each classi<sup>fi</sup>er included only terms within the window size around each number in the training data. Vocabulary sizes and examples for each window size appear below in Table 2.

## Step 4. Evaluate classifier

Metrics for recall, precision, and $\mathrm { F } _ { 1 }$ (as de<sup>fi</sup>ned in [47]) for the best classi<sup>fi</sup>er (window = 5) are reported in Table 3. The classi<sup>fi</sup>er was able to achieve 40% accuracy using only morphological attributes of the number itself. With a window of 1, accuracy jumped to 60%. At window size $^ { 5 , }$ overall accuracy reached 71%, where it plateaued as the window widened to 6 and 7. We therefore concluded that the 5-window model was the correct tradeo<sup>f</sup> between accuracy and parsimony. Some additional features were hand-tuned into the 5-window classi<sup>fi</sup>er, raising the overall accuracy to 73%. Speci<sup>fi</sup>cally, the following were added as features for the number strings, since they were frequently appended the numerals and were longer than 3 characters: ‘door’, ‘amps’, ‘volts’, ‘liter’, ‘litre’, ‘year’, ‘mile’.

Number categories with an $\mathrm { F } _ { 1 }$ score of < 0.65 were considered unreliable and were dropped from consideration.

Some of the challenges in demarcating and classifying the numbers in social media postings can be seen in the examples in Listing 2 below. There are unpredictable units, abbreviations, spellings, spacing, capitalization, and punctuations. For example, 20 ft-lb of torque can be written 20 ft.-lbs., 20 foot/pounds, 20 ft/lbs, 20 torque, 20 tq, 20 tq, tq. 20, or simply 20. Especially challenging is the disagreement about whether units are part of the number itself (50 W, 50 watts, 50 watts, 50 wts, etc.; or 100 lbs, 100 lbs., 100-pounds, 100 pounds, etc.). Consolidating these variations into canonical categories is critical to reliable processing. Despite the di<sup>fi</sup>culties, our classi<sup>fi</sup>er was able to identify speeds with an F1 of 0.743 and odometer readings with an $\mathrm { F _ { 1 } }$ of 0.650.

Thus, in converting the numerical attributes to features, care had to be taken to derive the correct interpretation of each numerical string. Expressions of the same concept had di<sup>f</sup>erent abbreviations, scales, and units. For example, odometer readings, which appear in Listing 3 were written in a variety of di<sup>f</sup>erent manners: miles vs. kilometers, ranges with hyphens, ‘k’ for thousand, x for $0 ^ { \prime } s ,$ commas in the wrong place, sometimes ‘60′ intending 60,000, etc. Listing 3 also shows some of the ways of expressing speed. Transmission was always 2,3,4,5, or 6.

## Step 5. Create bin cutofs

Since each number type could have an in<sup>fi</sup>nite number of values, it was necessary to group/bin the numbers to derive some kind of interpretable magnitude. We made an initial pass through the training data to <sup>fi</sup>nd all instances of each number, and we calculated and stored the overall median for each category. To process the numbers in the postings, we adopted the work<sup>fl</sup>ow in Fig. 3. Text processing was completed

![](/api/attachments/92ZU6XEZ/fulltext/images/d893166a07b118d03f845473740acb11951a8c40335dab57bdb233be2b7f2f5d.jpg)  
Fig. 2. Process for building the number classi<sup>fi</sup>er.

Table 2  
Vocabulary lengths and examples for all window sizes.

<table><tr><td>Window</td><td>Vocabulary length</td><td>Example</td></tr><tr><td>0</td><td>0</td><td>75</td></tr><tr><td>1</td><td>182</td><td>about 75 mph</td></tr><tr><td>2</td><td>448</td><td>of about 75 mph .</td></tr><tr><td>3</td><td>735</td><td>speed of about 75 mph . Just</td></tr><tr><td>4</td><td>1034</td><td>top speed of about 75 mph . Just a</td></tr><tr><td>5</td><td>1235</td><td>a top speed of about 75 mph . Just a little</td></tr><tr><td>6</td><td>1525</td><td>with a top speed of about 75 mph . Just a little faster</td></tr><tr><td>7</td><td>1786</td><td>speed with a top speed of about 75 mph . Just a little faster than</td></tr></table>

with Python 2.7.6.

In our case study, we split on the median, but alternative binning approaches are possible – e.g. a domain expert could de<sup>fi</sup>ne low vs. medium vs. high mileage – however, we chose to employ a simple median-based discretization approaches. In some cases, there were few enough distinct values that we were able to create categorical variables. For example, for “Chemical Symbol for Gas”, our entire training set contained only 6 distinct gases—O2 (oxygen), O3 (ozone), N2O (nitrous oxide), H2 (hydrogen), HO2 (hydroperoxyl, an emission), and NO2 (nitrogen dioxide, also an emission)—so we added a categorical dummy <sup>fi</sup>eld for the speci<sup>fi</sup>c gas mentioned. Wheel Drive was always either 2 or 4. Wheel drive, gear, doors, oil grade, and transmission are coded as numerical nominal data, while all others are binary nominal (0 1). For most number categories, we included a dummy variable indicating that it was mentioned, along with two other dummy variables indicating whether the value was above the median or below the median. See Appendix A for more details on units and distributions.

## Step 6. Deployment and indexing new documents

Our deployment scenario demonstrates a pragmatic application of numerical attributes as features: enhancing product defect discovery from social media. We will use the data set from [2], in which 4500 social media postings were labeled as defect = yes/no (1/0). (As in the prior research, we have collapsed performance and safety defects into a

Table 3

Best number classi<sup>fi</sup>er performance (window = 5).

<table><tr><td>Number type</td><td>Precision</td><td>Recall</td><td> $F_1$ </td></tr><tr><td>Address (including streets-zip codes-highways)</td><td>0.941</td><td>0.955</td><td>0.948</td></tr><tr><td>Oil grade</td><td>0.935</td><td>0.921</td><td>0.928</td></tr><tr><td>Age of vehicle</td><td>0.853</td><td>1.000</td><td>0.921</td></tr><tr><td>Calendar date</td><td>0.918</td><td>0.862</td><td>0.889</td></tr><tr><td>Phone</td><td>0.797</td><td>1.000</td><td>0.887</td></tr><tr><td>Calendar day</td><td>0.893</td><td>0.862</td><td>0.877</td></tr><tr><td>Rating (stars)</td><td>0.882</td><td>0.849</td><td>0.865</td></tr><tr><td>RPM</td><td>0.794</td><td>0.915</td><td>0.850</td></tr><tr><td>Fuel octane</td><td>0.794</td><td>0.877</td><td>0.833</td></tr><tr><td>Gear</td><td>0.817</td><td>0.829</td><td>0.823</td></tr><tr><td>Temperature</td><td>0.806</td><td>0.833</td><td>0.820</td></tr><tr><td>Generation</td><td>0.771</td><td>0.871</td><td>0.818</td></tr><tr><td>Fuel Efficiency (MPG-KPG)</td><td>0.797</td><td>0.839</td><td>0.817</td></tr><tr><td>Chemical symbol for gas (O2-CO2-NO2)</td><td>0.727</td><td>0.906</td><td>0.807</td></tr><tr><td>Torque</td><td>0.807</td><td>0.780</td><td>0.793</td></tr><tr><td>Time of day</td><td>0.860</td><td>0.729</td><td>0.789</td></tr><tr><td>Wheel drive (2WD-4WD-WD-4 × 4)</td><td>0.894</td><td>0.700</td><td>0.785</td></tr><tr><td>Percent</td><td>0.785</td><td>0.761</td><td>0.773</td></tr><tr><td>Pressure (PSI or kPa)</td><td>0.676</td><td>0.889</td><td>0.768</td></tr><tr><td>Model year</td><td>0.764</td><td>0.757</td><td>0.760</td></tr><tr><td>Engine piston size (liters (L) or cubic centimeters (cc))</td><td>0.677</td><td>0.840</td><td>0.750</td></tr><tr><td>Weight</td><td>0.820</td><td>0.685</td><td>0.746</td></tr><tr><td>Count of vehicles</td><td>0.774</td><td>0.719</td><td>0.745</td></tr><tr><td>Speed (mph-kph)</td><td>0.764</td><td>0.724</td><td>0.743</td></tr><tr><td>Engine piston count (V8-straight 6)</td><td>0.679</td><td>0.792</td><td>0.731</td></tr><tr><td>Volume (non-engine-gallons)</td><td>0.771</td><td>0.667</td><td>0.715</td></tr><tr><td>Dollar amount-price-currency</td><td>0.745</td><td>0.660</td><td>0.700</td></tr><tr><td>Distance traveled</td><td>0.733</td><td>0.657</td><td>0.693</td></tr><tr><td>Horsepower</td><td>0.685</td><td>0.698</td><td>0.692</td></tr><tr><td>Count of doors</td><td>0.571</td><td>0.857</td><td>0.686</td></tr><tr><td>Transmission (5 speed-6 speed)</td><td>0.939</td><td>0.525</td><td>0.674</td></tr><tr><td>Electrical (watts-amps-volts)</td><td>0.822</td><td>0.569</td><td>0.673</td></tr><tr><td>Odometer reading (# miles)</td><td>0.597</td><td>0.714</td><td>0.650</td></tr><tr><td>Error code</td><td>0.661</td><td>0.639</td><td>0.650</td></tr><tr><td>Tire model</td><td>0.635</td><td>0.647</td><td>0.641</td></tr><tr><td>Time duration</td><td>0.618</td><td>0.630</td><td>0.624</td></tr><tr><td>Word (2 for to)</td><td>0.492</td><td>0.517</td><td>0.504</td></tr><tr><td>Length/height measure</td><td>0.325</td><td>0.441</td><td>0.374</td></tr><tr><td>Listing (1.-2.)</td><td>0.352</td><td>0.373</td><td>0.362</td></tr><tr><td>Model number of component</td><td>0.412</td><td>0.241</td><td>0.304</td></tr><tr><td>Model number of vehicle</td><td>0.326</td><td>0.215</td><td>0.259</td></tr></table>

Listing 3  
Di<sup>f</sup>erent “families” of number expressions from our training data set.  
![](/api/attachments/92ZU6XEZ/fulltext/images/ed8ade59c65d04da1b41078f6ae116559ceaeb8e5004d0c8145129f0cc686bfb.jpg)

![](/api/attachments/92ZU6XEZ/fulltext/images/24a7539bf3c0788ce25a6d6030db438632429793b9f4bf46f110d3a92b845121.jpg)  
Fig. 3. Work<sup>fl</sup>ow for processing numbers extracted from unstructured postings.

single category, titled “defects”). We hypothesize that some of the nu merical attributes will make e<sup>f</sup>ective features for di<sup>f</sup>erentiating auto motive social media postings that indicate a manufacturing or design defect.

Using the number classi<sup>fi</sup>er, we added the numerical attributes to the 4500 postings from Honda-Tech.com, ToyotaNation.com, and ChevroletForum.com. For the variables that were not treated as categorical, we recorded 3 values: presence, high, or low. The “presence” variables did not always equal the sum of the low and high, due to two facts: 1) a single posting sometimes contained both high and low values for a number and 2) in 81 cases, the program was unable to determine the magnitude of the number due to unpredictable text formatting, and the program threw an error.<sup>3</sup> Although we retain the “presence” dummy variables in the data set as a convenience for other applications, they are not included in the regression because their value is completely determined by the value of the “low” and “high” variables.

Although any of the number categories could be useful in some application—say, aspect-based information retrieval—for our particular case study, we selected a subset of numbers that might have some bearing on the improper functioning of the automobile. For example, whereas address and phone number might help to locate a dealership geographically, and a star rating might help to rank cars by customer satisfaction, they are unlikely to help address the functionality of the automobile.

For these reasons, and to prevent classi<sup>fi</sup>er-model over-speci<sup>fi</sup>ca tion, we concentrate on an auspicious subset of number categories. Using training data only, we regressed the defect binary outcome on all of the number variables, eliminating “\_present” variables where “high”

and low variables existed. We retained variables with a signi<sup>fi</sup>cant LogWorth. Table 4 below details the variables and the signi<sup>fi</sup>cance of their relationship with the defect outcome. We tested the resilience of this set of numbers to di<sup>f</sup>erent data sets by checking classi<sup>fi</sup>cation performance measures on both training data and unseen holdout data (see Table 5 below).

We then ran a series of logistic regressions to <sup>fi</sup>nd the best predictive model. All regressions were conducted with JMP Pro Version 13.0, and classi<sup>fi</sup>cation metrics were computed using the supplied confusion matrices.

## 5.1. Case study results

We build on the predictive model described in [2]. Model 1 comprises context-independent features: word count, Fog index, average word length, number of views, number of users, and sentiment features 6 principle components). Model $^ { 2 , }$ also replicated from [2], includes context-speci<sup>fi</sup>c features: smoke words, product features, and semantic principle components. Model 3 is the full combined model from [2]. Model 4 consists of only the hypothesized numerical attributes. Model 5 is the full model, with all variables included. Our full logistic model speci<sup>fi</sup>cation appears in Listing 4.

Table 5 summarizes the logistic regression results. To ensure that we were not unjusti<sup>fi</sup>ably bene<sup>fi</sup>tting from sampling error, we trained all models on the Honda and Toyota sets (n = 3000) and tested on the unseen Chevrolet set (n = 1500). We report R<sup>2</sup>, precision, recall, $\mathrm { { F } } _ { 1 } ,$ and AUC for each of 5 models for both the training and test sets.

We note <sup>fi</sup>rst that the addition of the numerical attributes results in a modest improvement in precision, recall, $\mathrm { F } _ { 1 } ,$ , and AUC on both training and holdout test data. We also note that adding the numerical attributes caused the model to have a smaller drop in AUC over Model 3 when moving from training to test data (13% vs. 15%), indicating that the model is not over-<sup>fi</sup>t, despite having more variables.

Numerical attributes with a signi<sup>fi</sup>cant relationship with the defect binary outcome.

<table><tr><td>Numerical attribute</td><td>LogWorth</td><td>Prob &gt; ChiSq</td></tr><tr><td>model_year_high</td><td>35.582</td><td>&lt; 0.001</td></tr><tr><td>hp_high</td><td>4.701</td><td>&lt; 0.001</td></tr><tr><td>error_code_present</td><td>3.180</td><td>0.001</td></tr><tr><td>hp_low</td><td>2.604</td><td>0.002</td></tr><tr><td>count_vehicles_low</td><td>2.304</td><td>0.005</td></tr><tr><td>odometer_middle</td><td>2.119</td><td>0.008</td></tr><tr><td>generation_high</td><td>2.080</td><td>0.008</td></tr><tr><td>pressure_low</td><td>2.009</td><td>0.010</td></tr><tr><td>odometer_low</td><td>1.851</td><td>0.014</td></tr><tr><td>weight_low</td><td>1.842</td><td>0.014</td></tr><tr><td>vehicle_age_high</td><td>1.669</td><td>0.021</td></tr><tr><td>fuel_octane_low</td><td>1.574</td><td>0.027</td></tr><tr><td>engine_size_high</td><td>1.424</td><td>0.038</td></tr><tr><td>pressure_high</td><td>1.403</td><td>0.040</td></tr><tr><td>oil_present</td><td>1.250</td><td>0.056</td></tr><tr><td>count_vehicles_high</td><td>1.125</td><td>0.075</td></tr><tr><td>fuel_eff_high</td><td>1.081</td><td>0.083</td></tr><tr><td>electrical_present</td><td>1.077</td><td>0.084</td></tr></table>

The coe<sup>fi</sup>cients represent the approximate percent change in log odds of a posting containing a defect over the base level. So for example (consult Table 5, rightmost column, above) the presence of a high pressure (“pressure\_high”) increases the log-odds of a post indicating a defect by 31% because $1 0 0 ^ { * } ( e ^ { { \cdot } 2 7 3 } - 1 ) = 3 1 . 3 9 . \mathrm { A g a i n } $ , from the rightmost column of Table 5 above, the presence of a high model year (“model\_year\_high”) increases the odds of defect by 36% because $1 0 0 ^ { * } ( e ^ { . 3 0 7 } - 1 ) = 3 5 . 9 3 .$ . A negative coe<sup>fi</sup>cient decreases the log-odds. For example, the presence of a high horsepower (“hp\_high”) reduces the log-odds of a defect by 52% because 100 $\ : ( e ^ { . 4 1 9 } - 1 ) = 5 2 . 0 4 \ :$ . These precise percentages will depend on the values of the other independent variables, but these calculations provide a rough understanding of the relative e<sup>f</sup>ect sizes.

We experimented with di<sup>f</sup>erent probability cuto<sup>f</sup>s in an attempt to <sup>fi</sup>nd an improved balance between precision and recall: speci<sup>fi</sup>cally, to see how many available defects we could discover without lowering precision too drastically. Table 6 and Fig. 4 summarize these results. An optimal tradeo<sup>f</sup> appears to be a cuto<sup>f</sup> of 0.1, which maximizes $\mathrm { F } _ { 1 }$ at 0.845, increasing our recall to 0.991 while reducing precision to 0.737. Any further decreases causes a degradation in precision. Higher cuto<sup>f</sup>s (> 0.1), provide little improvement in precision but drops in recall and F (Fig. 4).

A model with so many variables has the drawback of being complex to build. We therefore tested an extremely parsimonious model consisting only of smoke words and our numerical attributes. Such a model can be built automatically once a classi<sup>fi</sup>er is trained, without any semantic or sentiment processing (as was previously required in [2]), and without any expertise in identifying system components being discussed (as was previously necessary in [3]). Using the same procedure above (training and holdout sets), we ran a logistic regression using only smoke words and numerical features. Performance metrics are reported in Table 7. Although the performance is reduced, the added bene<sup>fi</sup>t of a simple model makes it attractive in practice.

We conclude from this case study that the numerical attributes are helpful additions to the construction of models for automotive defect detection in social media. The improvements are modest, but we discuss promising further directions in Section 7, Limitations and Future Work.

## 6. Numerical attributes for information retrieval systems

In addition to enabling simple but accurate defect prediction, the numerical attributes provide us with a rich instrument for information retrieval functions for managing defect posts. A dynamic decision support system (DSS) is ultimately necessary for managing product quality using social media because our predictive models are never perfect, and human interpretation is an important element of the process. Smoke words and numerical attributes provide a powerful means for <sup>fi</sup>ltering the data set based on probabilities, but a decision support system that allows humans to explore the data is a way of <sup>fi</sup>nding social media content that might cause concern but was nevertheless missed by our predictive models.

Fig. 5 shows a screen shot from a proposed Post Market Quality Surveillance System that makes use of smoke terms and numerical attributes. Social media postings are imported into the system, and smoke term analysis and numerical attribute extraction is completed automatically. In the user view, <sup>fi</sup>ltering facets are on the left, and postings appear on the right. Users can select smoke terms and/or numerical attributes, such as model year, horsepower, odometer, etc. Each facet is colored according to how strongly its presence is tied to defect likelihood (that is, the coe<sup>fi</sup>cients on the logistic regression). The identi<sup>fi</sup>ed numerical expressions are highlighted within the posting, and the posting as a whole is assigned a defect likelihood, which is visualized on the slider at the top. Users can route the posting to a relevant organizational unit or to the archive. This interface provides the bene<sup>fi</sup>ts of the precise predictive model with the <sup>fl</sup>exibility to allow human users to make evaluations and experiment with combinations of numeric attributes and smoke terms.

## 7. Limitations and future work

Our study has a number of limitations that can be resolved and explored in future work.

Some of the numbers in our data belonged to the same number category but referred to di<sup>f</sup>erent functions, so strict continuous com parison against a median did not always make sense. For example, normal pressure in a tire is not the same as normal pressure in a cylinder. Future studies should incorporate some kind of topic extraction to determine exactly what component the number is referring to.

In our case study, we selected a subset of numerical attributes based on their LogWorth in our training data. While this resulted in some improvement in locating defects in our holdout data, this may not have been the optimal subset. A selection of numbers based on domain expertise might provide better prediction. For example, if there is some known relationship between a combination of low speeds and high RPM, a model that incorporate those attributes would enhance recall performance. Future studies should investigate how known automotive performance characteristics might inspire better feature selection.

Another potential limitation of this approach is that unusual numerical values may arise either from a manufacturing problem or from an exceptional design. For example, a high RPM or a low pressure, which might suggest a concerning case for a normal engine, might result from the healthy operation of an uniquely designed engine. These cases could result in false positives. We do not think these are deal breakers, however, for two reasons: 1) car make/model can always be incorporated into a regression as a categorical variable, and 2) these are, by de<sup>fi</sup>nition, unusual cases, and thus would not bias the results substantively.

Additionally, there could be splits for each number category that would better separate the defect and non-defect classes, and these optimal splits should be investigated. This should be approached with caution, however, because many splitting methods have an exponential run-time [15]. Discretization of numerical attributes is a key technique of data preprocessing [41], and a more granular discretization of nu merical attributes is a logical next step. One important question to address is whether an optimal discretization is more useful than one informed by <sup>fi</sup>eld experts, who have their own pragmatic thresholds for real world applications.

Future studies should experiment with integrating the numerical attributes with proprietary data sources, such as engineering manuals that indicate acceptable tolerances for number ranges. Many businesses are seeking ways to integrate social media with in-house structure data stores, and this provides a promising use case.

Table 5  
Logistic regression results.

<table><tr><td>Variable</td><td>Model 1(context independent)</td><td>Model 2(context specific)</td><td>Model 3(full 2014 model)</td><td>Model 4(numerical attributes only)</td><td>Model 5(full model)</td></tr><tr><td>ZwordCount</td><td>-0.042</td><td></td><td>0.057</td><td></td><td>0.022</td></tr><tr><td>ZFogIndex</td><td>0.013</td><td></td><td>-0.039</td><td></td><td>-0.018</td></tr><tr><td>ZAverageWordLength</td><td>-0.036</td><td></td><td>-0.224**</td><td></td><td>-0.245**</td></tr><tr><td>Zviews</td><td>0.031</td><td></td><td>-0.053</td><td></td><td>-0.076</td></tr><tr><td>ZnumOfUsers</td><td>-0.107*</td><td></td><td>-0.026</td><td></td><td>-0.031</td></tr><tr><td>SentiFAC1_2</td><td>0.042</td><td></td><td>-0.067</td><td></td><td>-0.062</td></tr><tr><td>SentiFAC2_2</td><td>-0.206**</td><td></td><td>-0.004</td><td></td><td>0.002</td></tr><tr><td>SentiFAC3_2</td><td>0.058</td><td></td><td>0.068</td><td></td><td>0.056</td></tr><tr><td>SentiFAC4_2</td><td>0.058</td><td></td><td>0.046</td><td></td><td>0.059</td></tr><tr><td>SentiFAC5_2</td><td>-0.094</td><td></td><td>-0.039</td><td></td><td>-0.029</td></tr><tr><td>SentiFAC6_2</td><td>0.065*</td><td></td><td>0.124</td><td></td><td>0.127</td></tr><tr><td>ZSmokeWord</td><td></td><td>1.149**</td><td>1.237**</td><td></td><td>1.200**</td></tr><tr><td>AirConditioning</td><td></td><td>0.555**</td><td>0.502**</td><td></td><td>0.541**</td></tr><tr><td>Airbag</td><td></td><td>0.130</td><td>0.045</td><td></td><td>0.028</td></tr><tr><td>Braking</td><td></td><td>0.555**</td><td>0.551**</td><td></td><td>0.552**</td></tr><tr><td>Electricalsystem</td><td></td><td>0.330**</td><td>0.330**</td><td></td><td>0.359**</td></tr><tr><td>Engine</td><td></td><td>0.276**</td><td>0.273**</td><td></td><td>0.315**</td></tr><tr><td>Lights</td><td></td><td>0.140</td><td>0.142</td><td></td><td>0.144</td></tr><tr><td>SeatBelts</td><td></td><td>0.631**</td><td>0.611**</td><td></td><td>0.686**</td></tr><tr><td>Steering</td><td></td><td>0.542**</td><td>0.557**</td><td></td><td>0.569**</td></tr><tr><td>StructureandBody</td><td></td><td>0.555**</td><td>0.520**</td><td></td><td>0.545**</td></tr><tr><td>Transmission</td><td></td><td>0.196**</td><td>0.194**</td><td></td><td>0.149*</td></tr><tr><td>Visibility</td><td></td><td>0.556</td><td>0.477**</td><td></td><td>0.495**</td></tr><tr><td>WheelsandTires</td><td></td><td>0.172</td><td>0.167</td><td></td><td>0.155</td></tr><tr><td>Other</td><td></td><td>-0.405</td><td>-0.389**</td><td></td><td>-0.402**</td></tr><tr><td>Suspension</td><td></td><td>0.319**</td><td>0.346*</td><td></td><td>0.280</td></tr><tr><td>Acoustics</td><td></td><td>0.226</td><td>0.182</td><td></td><td>0.175</td></tr><tr><td>SemanFAC1_1</td><td></td><td>-0.105*</td><td>-0.170**</td><td></td><td>-0.156**</td></tr><tr><td>SemanFAC2_1</td><td></td><td>-0.128**</td><td>-0.127**</td><td></td><td>-0.134**</td></tr><tr><td>SemanFAC3_1</td><td></td><td>0.135**</td><td>0.174**</td><td></td><td>0.117*</td></tr><tr><td>SemanFAC4_1</td><td></td><td>-0.101*</td><td>-0.134**</td><td></td><td>-0.122*</td></tr><tr><td>SemanFAC5_1</td><td></td><td>-0.009</td><td>-0.040</td><td></td><td>-0.051</td></tr><tr><td>SemanFAC6_1</td><td></td><td>0.038</td><td>0.067</td><td></td><td>0.058</td></tr><tr><td>SemanFAC7_1</td><td></td><td>-0.041</td><td>-0.057</td><td></td><td>-0.054</td></tr><tr><td>SemanFAC8_1</td><td></td><td>-0.028</td><td>-0.056</td><td></td><td>-0.065</td></tr><tr><td>model_year_high</td><td></td><td></td><td></td><td>0.306**</td><td>0.307**</td></tr><tr><td>hp_high</td><td></td><td></td><td></td><td>-0.413**</td><td>-0.419**</td></tr><tr><td>error_code_present</td><td></td><td></td><td></td><td>0.058</td><td>-0.006</td></tr><tr><td>hp_low</td><td></td><td></td><td></td><td>-0.531**</td><td>-0.396*</td></tr><tr><td>count_vehicles_low</td><td></td><td></td><td></td><td>-0.122</td><td>0.036</td></tr><tr><td>odometer_middle</td><td></td><td></td><td></td><td>0.084</td><td>0.309**</td></tr><tr><td>generation_high</td><td></td><td></td><td></td><td>-0.188</td><td>-0.029</td></tr><tr><td>pressure_low</td><td></td><td></td><td></td><td>-0.282*</td><td>-0.150</td></tr><tr><td>odometer_low</td><td></td><td></td><td></td><td>-0.224**</td><td>-0.040</td></tr><tr><td>weight_low</td><td></td><td></td><td></td><td>-0.186</td><td>-0.097</td></tr><tr><td>vehicle_age_high</td><td></td><td></td><td></td><td>-0.222</td><td>0.052</td></tr><tr><td>fuel_octane_low</td><td></td><td></td><td></td><td>-0.234</td><td>-0.199</td></tr><tr><td>engine_size_high</td><td></td><td></td><td></td><td>-0.140</td><td>-0.030*</td></tr><tr><td>pressure_high</td><td></td><td></td><td></td><td>0.221*</td><td>0.273*</td></tr><tr><td>oil_present</td><td></td><td></td><td></td><td>-0.188</td><td>-0.110</td></tr><tr><td>count_vehicles_high</td><td></td><td></td><td></td><td>-0.132</td><td>-0.009</td></tr><tr><td>fuel_eff_high</td><td></td><td></td><td></td><td>-0.212*</td><td>-0.135*</td></tr><tr><td>electrical_present</td><td></td><td></td><td></td><td>0.101</td><td>0.067</td></tr></table>

<table><tr><td></td><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td><td>Model 5</td></tr><tr><td>R-square</td><td>0.014</td><td>0.219</td><td>0.228</td><td>0.036</td><td>0.25</td></tr><tr><td colspan="6">Test</td></tr><tr><td>Precision</td><td>0.327</td><td>0.83</td><td>0.834</td><td>0.788</td><td>0.843</td></tr><tr><td>Recall</td><td>0.548</td><td>0.469</td><td>0.502</td><td>0.59</td><td>0.586</td></tr><tr><td> $F_1$ </td><td>0.41</td><td>0.599</td><td>0.627</td><td>0.675</td><td>0.692</td></tr><tr><td>AUC</td><td>0.558</td><td>0.685</td><td>0.692</td><td>0.623</td><td>0.717</td></tr><tr><td colspan="6">Training</td></tr><tr><td>Precision</td><td>0.572</td><td>0.724</td><td>0.726</td><td>0.568</td><td>0.735</td></tr><tr><td>Recall</td><td>0.729</td><td>0.67</td><td>0.679</td><td>0.387</td><td>0.684</td></tr><tr><td>F1</td><td>0.641</td><td>0.696</td><td>0.702</td><td>0.460</td><td>0.709</td></tr><tr><td>AUC</td><td>0.558</td><td>0.807</td><td>0.811</td><td>0.612</td><td>0.823</td></tr></table>

Cuto<sup>f</sup> for precision, recall, and f1 was 0.5.  
<sup>⁎</sup> Signi<sup>fi</sup>cant at the 5% signi<sup>fi</sup>cance level.  
<sup>⁎⁎</sup> Signi<sup>fi</sup>cant at the 1% level.

![](/api/attachments/92ZU6XEZ/fulltext/images/4104127fbc4f14f5ff0fce555dabb78ff9c77ca58e7c1bd43fd9e42e93cbb6bc.jpg)

Listing 4  
Logistic model to predict the log-odds of a post indicating a vehicle with a manufacturing defect.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\log \left( \frac{prob\_ defect}{1 - prob\_ defect} \right) = \beta_0 + \sum_{i}^{34} \beta_i previous\_ feature_i + \beta_{35} model\_ year\_ high + \beta_{36} hp\_ high + \beta_{37} error\_ code\_ present + \beta_{38} hp\_ low + \beta_{39} count\_ vehicles\_ low + \beta_{40} odometer\_ middle + \beta_{41} generation\_ high + \beta_{42} pressure\_ low + \beta_{43} odometer\_ low + \beta_{44} weight\_ low + \beta_{45} vehicle\_ age\_ high + \beta_{46} fuel\_ octane\_ low + \beta_{47} engine\_ size\_ high + \beta_{48} pressure\_ high + \beta_{49} oil\_ present + \beta_{50} count\_ vehicles\_ high + \beta_{51} fuel\_ eff\_ high + \beta_{52} electrical\_ present$
</div>

Table 6

<table><tr><td colspan="8">Full model performance at different cutoffs.</td></tr><tr><td>Cutoff</td><td>0.05</td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td></tr><tr><td>Precision</td><td>0.722</td><td>0.737</td><td>0.766</td><td>0.795</td><td>0.825</td><td>0.843</td><td>0.85</td></tr><tr><td>Recall</td><td>0.999</td><td>0.991</td><td>0.918</td><td>0.825</td><td>0.718</td><td>0.586</td><td>0.448</td></tr><tr><td> $F_1$ </td><td>0.838</td><td>0.845</td><td>0.835</td><td>0.81</td><td>0.768</td><td>0.709</td><td>0.587</td></tr></table>

![](/api/attachments/92ZU6XEZ/fulltext/images/ecd3c8cda9ecd7789877ce7fde8d1c1b81703712eace1b7976d3b93f4a71258e.jpg)  
Fig. 4. Precision, recall, and F1 at di<sup>f</sup>erent cuto<sup>f</sup> levels in the logistic regression.

Table 7  
Simpli<sup>fi</sup>ed model performance metrics.

<table><tr><td>Metric</td><td>Training</td><td>Test</td></tr><tr><td>Precision</td><td>0.799</td><td>0.731</td></tr><tr><td>Recall</td><td>0.347</td><td>0.208</td></tr><tr><td> $F_1$ </td><td>0.484</td><td>0.323</td></tr><tr><td>AUC</td><td>0.79</td><td>0.65</td></tr></table>

The Defect Management System interface proposes a potential Information Retrieval (IR) application for our numerical attributes, and its utility should be assessed in a production context. A follow-up design science project which deploys this system and evaluates its e<sup>f</sup>ectiveness in quality control is currently in the planning stages.

## 8. Conclusion

We have presented a method for handling domain-speci<sup>fi</sup>c numerical attributes within social media text and demonstrated their utility in tasks related to quality management.

Our work has a number of implications for research and practice.

For research, we contribute a novel approach to dealing with numerical data in text. We demonstrate that a corpus-based method in which numbers are extracted and classi<sup>fi</sup>ed using supervised machine learning can be accurate, e<sup>f</sup>ective, and straightforward. This is a robust and proven procedure for creating structure from unstructured data, which makes classi<sup>fi</sup>cation easier in any domain.

For management practice, we supply a methodology for producing informed diagnostics from social media postings. Our case study applies directly to the automotive industry, but our method can be expanded to other number-intensive industries as well.

![](/api/attachments/92ZU6XEZ/fulltext/images/3ef32173a74537f95f9b2fee639fa46c8ae2f53ea56842565eb59c1de8365656.jpg)  
Fig. 5. Post Market Quality Surveillance System using smoke terms and numerical attributes.

Appendix A. Number categories, medians, and features extracted for our case study

<table><tr><td>Number category</td><td>Median</td><td>Features</td></tr><tr><td>Age of vehicle</td><td>72 months</td><td>vehicle_age_presentm vehicle_age_low, vehicle_age_high</td></tr><tr><td>Chemical symbol for Gas</td><td>Categorical</td><td>gas, gas_o2, gas_o3, gas_n2o, gas_h2, gas_h02, gas_no2</td></tr><tr><td>Count of doors</td><td>4</td><td>Doors</td></tr><tr><td>Count of vehicles</td><td>4</td><td>count_vehicles_present, count_vehicles_low, count_vehicles_high</td></tr><tr><td>Generation</td><td>5</td><td>generation_low, generation_high</td></tr><tr><td>Gear</td><td>3</td><td>gear_present</td></tr><tr><td>Distance traveled</td><td>305 miles</td><td>distance_present, distance_low, distance_high</td></tr><tr><td>Dollar amount</td><td>253</td><td>dollar_present, dollar_high, dollar_low</td></tr><tr><td>Electrical</td><td></td><td>electrical_present</td></tr><tr><td>Engine cylinder size</td><td>2.7 l</td><td>engine_size_present, engine_size_low, engine_size_high</td></tr><tr><td>Engine pistons</td><td>6</td><td>engine_pistons_present</td></tr><tr><td>Error code</td><td>Categorical</td><td>error_code_present</td></tr><tr><td>Fuel octane</td><td>91</td><td>fuel_octane_present, fuel_octane_low, fuel_octaine_high</td></tr><tr><td>Fuel efficiency</td><td>30 mpg</td><td>fuel_eff_present, fuel_eff_low, fuel_eff_high</td></tr><tr><td>Horsepower</td><td>200</td><td>hp_present, hp_low, hp_high</td></tr><tr><td>Model year</td><td>1997</td><td>model_year_present, model_year_low, model_year_high</td></tr><tr><td>Odometer reading</td><td>80,000 miles</td><td>odometer_present, odometer_low, odometer_middle, odometer_high</td></tr><tr><td>Speed</td><td>55 mph</td><td>speed_present, speed_range, speed_low, speed_high</td></tr><tr><td>Temperature</td><td>100 F</td><td>temperature_present, temperature_low, temperature_high</td></tr><tr><td>Tire model</td><td>Categorical</td><td>tire_model</td></tr><tr><td>Oil grade</td><td></td><td>oil_present, oil_low_temp, oil_viscosity</td></tr><tr><td>Pressure</td><td>32 psi</td><td>pressure_present, pressure_low, pressure_high</td></tr><tr><td>RPM</td><td>3000 rpm</td><td>rpm_present, rpm_low, rpm_high</td></tr><tr><td>Torque</td><td>195 ft lb</td><td>torque_present, high_torque, low_torque</td></tr><tr><td>Transmission</td><td>5 speed</td><td>trans_speed</td></tr><tr><td>Weight</td><td>150 lb</td><td>weight_present, weight_low, weight_high</td></tr><tr><td>Wheel drive</td><td>4</td><td>wheel_drive</td></tr></table>

## References

[1] Fuel Economy, Toyota Sienna Fuel Economy Review. (12/26/17), Caranddriver com. 2017 (Retrieved from). https://www caranddriver com reviews/2017-toyota-sienna-in-depth-model-review-2017-toyota-sienna-fueleconomy-review-car-and-driver-page-3.

[2] A.S. Abrahams, W. Fan, G.A. Wang, Z.J. Zhang, J. Jiao, An integrated text analytic framework for product defect discovery, Production and Operations Management 24 (6) (2015) 975–990.

[3] A.S. Abrahams, J. Jiao, W. Fan, G.A. Wang, Z. Zhang, What's buzzing in the blizzard of buzz? Automotive component isolation in social media postings, Decision Support Systems 55 (4) (2013) 871 882.

[4] A.S. Abrahams, J. Jiao, G.A. Wang, W. Fan, Vehicle defect discovery from social media, Decision Support Systems 54 (1) (2012) 87–97.

[5] D.Z. Adams, R. Gruss, A.S. Abrahams, Automated discovery of safety and e<sup>fi</sup>cacy concerns for joint & muscle pain relief treatments from online reviews. Internationa Journal of Medical Informatics 100 (2017) 108–120.

[6] T. Akiba, K. Itou, A. Fujii, Question Answering Using “Common Sense” and Utility Maximization Principle, National Institute of Informatics Testbeds and Community for Information Access Research (NTCIR-4), Tokyo, Japan, 2004.

[7] A. Bakalov, A. Fuxman, P.P. Talukdar, S. Chakrabarti, Scad: collective discovery of attribute values. Proceedings of the 20th International Conference on World Wide Web, ACM, 2011, pp. 447–456.

[8] S. Baneriee, S. Chakrabarti. G. Ramakrishnan. Learning to rank for quantity con: sensus queries. Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval. ACM. 2009, pp. 243–250.

[9] S.K. Bhat, A. Culotta, Identifying Leading Indicators of Product Recalls From Online Reviews Using Positive Unlabeled Learning and Domain Adaptation (arXiv preprint)., 2017. arXiv:1703.00518.

[10] F. Charte, A.J. Rivera, M.J. del Jesus, F. Herrera, Addressing imbalance in multilabel classi<sup>fi</sup>cation: measures and random resampling algorithms, Neurocomputing 163 (2015) 3–16.

[11] D. Davidov, A. Rappoport, Extraction and approximation of numerical attributes from the web. Proceedings of the 48th Annual Meeting of the Association for Computational Linguistics, Association for Computational Linguistics, 2010, pp. 1308-1317.

[12] B. Doig, B. McRae, K. Rowe, A Good Start to Numeracy: E<sup>f</sup>ective Numeracy Strategies from Research and Practice in Early Childhood, Australian Council for Educational Research (ACFR): ACFReSearch 2003

[13] A.S. Dokuz, M. Celik, Discovering socially important locations of social media users,

Expert Systems with Applications 86 (2017) 113–124.

[14] J. Doucette, M. Heywood, GP classi<sup>fi</sup>cation under imbalanced data sets: active subsampling and AUC approximation, Genetic Programming, 2008, pp. 266–277.

[15] T. Elomaa, J. Rousu, General and e<sup>fi</sup>cient multisplitting of numerical attributes, Machine Learning 36 (3) (1999) 201–244.

[16] K. Gerardi, L. Goette, S. Meier, Numerical ability predicts mortgage default, Proceedings of the National Academy of Sciences 110 (28) (2013) 11267–11271

[17] D.M. Goldberg, A.S. Abrahams, A Tabu search heuristic for smoke term curation in safety defect discovery, Decision Support Systems 105 (2018) 52–65.

[18] R. Grondin, S.J. Lupker, K. McRae, Shared features dominate the number-of-features e<sup>f</sup>ect, Proceedings of the Annual Meeting of the Cognitive Science Society, 2006.

[19] H. He, Y. Ma, Imbalanced Learning: Foundations, Algorithms, and Applications, John Wiley & Sons. 2013.

[20] E. Hovy. U. Hermiakob. C.-Y. Lin. D. Ravichandran, Using knowledge to facilitate factoid answer pinpointing. Proceedings of the 19th International Conference on Computational Linguistics, Vol. 1 Association for Computational Linguistics, 2002, pp. 1–7.

[21] H.-J. Jang, J. Sim, Y. Lee, O. Kwon, Deep sentiment analysis: mining the causality between personality-value-attitude for analyzing business ads in social media, Expert Systems with Applications 40 (18) (2013) 7492 7503.

[22] J. Kounios, D.L. Green, L. Payne, J.I. Fleck, R. Grondin, K. McRae, Semantic richness and the activation of concepts in semantic memory: evidence from event-related potentials, Brain Research 1282 (2009) 95 102.

[23] J.R. Landis, G.G. Koch, The measurement of observer agreement for categorica data, Biometrics (1977) 159–174

[24] D. Law, R. Gruss, A.S. Abrahams, Automated defect discovery for dishwasher appliances from online consumer reviews, Expert Systems with Applications 67 (2017) 84 94.

[25] L. Liu, J. Wu, P. Li, Q. Li, A social-media-based approach to predicting stock comovement., Expert Systems with Applications 42 (8) (2015) 3893–3901.

[26] Y. Liu, C. Jiang, H. Zhao, Using contextual features and multi-view ensemble learning in product defect identi<sup>fi</sup>cation from online discussion forums, Decision Support Systems 105 (2017) 1–12.

[27] Y. Liu, L. Wang, R. Chen, Y. Song, Y. Cai, A PUT-based approach to automatically extracting quantities and generating <sup>fi</sup>nal answers for numerical attributes, Entropy 18 (6) (2016) 235

[28] V. López, A. Fernández, S. García, V. Palade, F. Herrera, An insight into classi<sup>fi</sup>- cation with imbalanced data: Empirical results and current trends on using data intrinsic characteristics. Information Sciences 250 (2013) 113–141

[29] S. Mandhan. Y. Niwa, Numerical Atrribute Extraction From Clinical Texts (arXiy

preprint),, 2016. arXiv:1602.00269.

[30] J. McAuley, C. Targett, Q. Shi, A. Van Den Hengel, Image-based recommendations on styles and substitutes, Proceedings of the 38th International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM, 2015, pp. 43–52.

[31] K. McRae, G.S. Cree, M.S. Seidenberg, C. McNorgan, Semantic feature production norms for a large set of living and nonliving things, Behavior Research Methods 37 (4) (2005) 547–559.

[32] K. Narisawa, Y. Watanabe, J. Mizuno, N. Okazaki, K. Inui, Is a 204 cm Man Tall o Small? Acquisition of Numerical Common Sense From the Web, Vol. 1 ACL, 2013, pp. 382–391.

[33] T.H. Nguyen, K. Shirai, J. Velcin, Sentiment analysis on social media for stock movement prediction, Expert Systems with Applications 42 (24) (2015) 9603–9611

[34] E. Peters, D. Västfjäll, P. Slovic, C. Mertz, K. Mazzocco, S. Dickert, Numeracy and decision making, Psychological Science 17 (5) (2006) 407–413.

[35] P.M. Pexman, I.S. Hargreaves, P.D. Siakaluk, G.E. Bodner, J. Pope, There are many ways to be rich: E<sup>f</sup>ects of three measures of semantic richness on visual word re cognition, Psychonomic Bulletin & Review 15 (1) (2008) 161–167.

[36] P.M. Pexman, S.J. Lupker, Y. Hino, The impact of feedback semantics in visual word recognition: number-of-features e<sup>f</sup>ects in lexical decision and naming tasks, Psychonomic Bulletin & Review 9 (3) (2002) 542 549.

[37] P.M. Pexman, P.D. Siakaluk, M.J. Yap, Meaning in Mind: Semantic Richness E<sup>f</sup>ects in Language Processing, Frontiers E-books, 2014.

[38] D. Pohl, A. Bouchachia, H. Hellwagner, Batch-based active learning: application to social media data for crisis management, Expert Systems with Applications 93 (2018) 232–244.

[39] Z. Qiao, G.A. Wang, M. Zhou, W. Fan, The Impact of Customer Reviews on Product Innovation: Empirical Evidence in Mobile Apps, Analytics and Data Science, Springer, 2018, pp. 95–110.

[40] Z. Qiao, X. Zhang, M. Zhou, G.A. Wang, W. Fan, A Domain Oriented LDA Model for Mining Product Defects from Online Customer Reviews, The 50th Hawaii International Conference on System Sciences Waikoloa, HI, (2017).

[41] S. Ramírez-Gallego, S. García, J.M. Benítez, F. Herrera, Multivariate discretization based on evolutionary cut points selection for classi<sup>fi</sup>cation, IEEE Transactions on Cybernetics 46 (3) (2016) 595–608.

[42] V.F. Reyna, W.L. Nelson, P.K. Han, N.F. Dieckmann, How numeracy in<sup>fl</sup>uences risk comprehension and medical decision making, Psychological Bulletin 135 (6) (2009) 943.

[43] M. Rubens. P. Agarwal. Information Extraction from Online Automotive Classifieds (10/31/17). (2004) Retrieved from: http://www-nlp.stanford.edu/courses/ cs224n/2004/cs224n\_<sup>fi</sup>nal\_mrubens\_agarwalp.pdf.

[44] S.J. Russell, P. Norvig, Arti<sup>fi</sup>cial Intelligence: A Modern Approach, Pearson Education Limited, Malaysia, 2016.

[45] H. Takamura, J.i. Tsujii, Estimating numerical attributes by bringing together fragmentary clues, human language technologies, The 2015 Annual Conference of the North American Chapter of the ACL, Denver, CO, 2015, pp. 1305–1310.

[46] M. Winkler, A.S. Abrahams, R. Gruss, J.P. Ehsani, Toy safety surveillance from

online reviews, Decision Support Systems 90 (2016) 23–32.

[47] Y. Yang, An evaluation of statistical approaches to text categorization, Information Retrieval 1 (1) (1999) 69–90.

[48] M.J. Yap, S.E. Tan, P.M. Pexman, I.S. Hargreaves, Is more always better? E<sup>f</sup>ects of semantic richness on lexical decision, speeded pronunciation, and semantic classi <sup>fi</sup>cation, Psychonomic Bulletin & Review 18 (4) (2011) 742–750.

[49] X. Zhang, Z. Qiao, L. Tang, W. Fan, E. Fox, G. Wang, Identifying Product Defects from User Complaints: A Probabilistic Defect Model, https://vtechworks.lib.vt.edu handle/10919/64902, (2016).

Richard Gruss is an Assistant Professor in the College of Business and Economics at Radford University. He received a PhD from Virginia Tech, an MBA from Loyola University Chicago, a master's degree in Information Science from UNC-Chapel Hill, and a Master of Education from the University of Virginia. His research interests include social media and text analytics, and his work has appeared in Decision Support Systems, Expert Systems with Applications, the International Journal of Medical Informatics, and the Journal of Computing Sciences in Colleges.

Alan S. Abrahams is an Associate Professor in the Department of Business Information Technology, Pamplin College of Business at Virginia Tech. He received a PhD in Computer Science from the University of Cambridge, and holds a Bachelor of Business Science degree from the University of Cape Town. Dr. Abrahams' primary research interest is text mining for defect discovery. He is a Senior Editor of Decision Support Systems, and has published in a variety of journals including Production and Operations Management, Decision Support Systems, Expert Systems with Applications, Journal of Computer Information Systems, Communications of the AIS, and Group Decision and Negotiation.

Weiguo Fan is Henry B. Tippie Chair in Business Analytics, Tippie College of Business at the University of Iowa. He received his Ph.D. in Business Administration from the Ross School of Business, University of Michigan, Ann Arbor. He has published > 180 refereed journal and conference papers. His research has appeared in many premier IT/IS/OM journals such as Information Systems Research, Journal of Management Information Systems, Productions and Operations Management, IEEE Transactions on Knowledge and Data Engineering, Information Systems, Communications of the ACM, Information and Management, Journal of the American Society on Information Science and Technology.

G. Alan Wang is an Associate Professor in the Department of Business Information Technology, Pamplin College of Business at Virginia Tech. He received the Ph.D. in Management Information Systems from the University of Arizona. His research interests include heterogeneous data management, data cleansing, data mining and knowledge discovery, and decision support systems. He has published in Communications of the ACM, IEEE Transactions of Systems, Man and Cybernetics (Part A), IEEE Computer, Group Decision and Negotiation, Journal of the American Society for Information Science and Technology, and Journal of Intelligence Community Research and Development.
