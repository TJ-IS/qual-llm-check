---
otero_id: 13902
otero_key: "QJWMMFAY"
title: "Exploring the role of deep neural networks for post-disaster decision support"
authors: "Neha Chaudhuri; Indranil Bose"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113234"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Exploring the role of deep neural networks for post-disaster decision support

Neha Chaudhuri, Indranil Bose

![](/api/attachments/QJWMMFAY/fulltext/images/482c32dd2a5358c2a3a7a6d7468fc44193e2803edecf963b608380a0c8afc19d.jpg)

Indian Institute of Management Calcutta, Diamond Harbour Road, Joka, Kolkata 700104, India

## A R T I C L E I N F O

Keywords: Convolutional neural networks Decision support Deep learning Disaster management Image analytics

## A B S T R A C T

Disaster management operations are information intensive activities due to high uncertainty and complex information needs. Emergency response planners need to efectively plan response activities with limited resources and assign rescue teams to specific disaster sites with high probability of survivors swiftly. Decision making becomes tougher since the limited information available is heterogenous, untimely and often fragmented. We address the problem of lack of insightful information of the disaster sites by utilizing image data obtained from smart infrastructures. We collect geo-tagged images from earthquake-hit regions and apply deep learning method for classification of these images to identify survivors in debris. We find that deep learning method is able to classify the images with significantly higher accuracy than the conventionally used machine learning methods for image classification and utilizes significantly lesser time and computational resources. The novel application of image analytics and the resultant findings from our models have valuable implications for effective disaster response operations, especially in smart urban settlements

## 1. Introduction

Disaster response is a profoundly complex and information-in tensive activity [11. Natural disasters are accompanied by breakdown of existing physical and social communication infrastructure leading to great uncertainty due to the lack of reliable information [2]. In such situations, community intelligence from the disaster sites is the primary source of information [3]. However, the information from such sources is heterogenous, fragmented and hence complex, making assimilation of any useful knowledge incredibly challenging [4,5]. Additionally, this information is seldom accurate and reliable. However, due to the lack of integration of all dependable sources of information, various crucial decisions for disaster response that are made based on them are seldom optimal [6]. This uncertainty combined with the added complexity arising from the need for timely decision-making results in the use of heuristics instead of reliable data. The informal nature of such decisionmaking processes combined with the lack of accurate information impact the optimality of the resulting decisions [7].

Timeliness and participation of human hands from multiple, geo graphically distributed organizations and their communication are critical [8] to ensure efective management of the limited humanitarian and other resources for disaster response. Information management is crucial for such operations. Information from decision support systems (DSS) can be efectively utilized for strategic planning to ensure optimal prioritization and allocation of resources among discrete response activities [9]. Such systems need to be able to provide timely support for various decision situations ranging from disaster assessment to optimal resource allocation.

Additionally. information technologies have an immense potential for supporting these systems for efective disaster response. A report by the National Research Council in the US has asserted that IT has unrealized potential to improve how communities, individuals handle disasters [10]. The impact of such advanced IT systems can be realized by focusing on two major areas of decision making, namely, the development of accurate sources of information and the development of efective DSS. Although several efective DSS for disaster response exist, the development of reliable sources of information is still lacking.

The inadequacy of reliable information during disaster planning highlights not just the lack of access to accurate sources of information but also the lack of processing capability of unconventional sources of information. Recently, various studies have highlighted the eficacy of user-generated data from social media for disaster planning and response [3,11]. Platforms like Facebook and Twitter support peer-topeer information dissemination during disaster situations. Studies have reported that usage of such platforms have surpassed the usage of conventional modes such as fixed phone and radio, as witnessed in the case of the Hurricane Sandy disaster of 2012 [12]. Local communities are thus increasingly opting for social media platforms which act as informal and public backchannel communication systems in the absence (or scarcity) of conventional modes including fixed phones, and news reports during and after disasters [13,14]. Apart from such secondary sources of data, a gradual integration of the smart infrastructure in a city can be a potential source of accurate and primary information for disaster response. These infrastructures have been found to be resistant to various disasters but their capability to broadcast information is restricted due to disasters [15]. Data from such devices, if captured and processed locally, can prove to be an accurate and reliable source of rich information for decision making during disasters [15].

Further, Hristidis et al. [4] have highlighted the need to integrate discrete data sources and resources in a collaborative and timely manner, and the need to collect updated information from these dis tributed sources through one integrated information system. However, this data can be efectively utilized only if we develop novel information processing capabilities. Image analytics can be one potential tool to aid disaster response planning [16]. With gradual maturation of analytic technologies, data collected from smart devices can be potentially collected and processed by emergency personnel on the ground and response planning can be made on site as against centrally as done currently. Software behemoths like Google have been aiming to build deep learning (DL) models that are capable of executing on portable mobile devices. Google has recently developed MnasNet (a mobile DL model) with reduced network depth and cheaper computations to balance the accuracy-resource eficiency trade-of. Although image analytics is also gaining acceptance in the domain of healthcare research for patient image retrieval [17] and object identification [18], its potential in disaster management domain has not been explored. A review of existing literature reveals a research gap with respect to the application of deep neural networks within the field of disaster management using the huge volumes of data from smart urban infrastructure. We respond to this lack of scholarship on decision support for disaster response in this study. The primary research objective of this study is to demonstrate the capability of image analytics in aiding de cisions on resource prioritization for disaster response. Consequently, this study attempts to respond to the following research questions:

How can image analytics be used for disaster response?

Which image analytic techniques are more efective in this context?

Our research utilizes convolutional neural networks (CNN) for classification of image data and compares them with traditional machine learning (ML) techniques. The identification of survivors from partial body parts visible from a huge dataset of images is considered to be a challenging task [19]. The DL and ML based models proposed by us can classify images with a high accuracy for determining the presence of human survivors in debris from photographs of disaster zones. This study contributes to decision making for disaster response by:

1. identifying a novel source of accurate information during disasters and demonstrating its technical eficacy for decision support

2. comparing various DL and ML models in terms of their efectiveness for disaster response.

We initiate this study by examining related work in diferent domains followed by the analysis of image data through various advanced analytic techniques. This is followed by the presentation of results. Next, we discuss the results that are obtained and present the im plications of this study for both research and practice.

## 2. Related work

## 2.1. DSS for management of smart infrastructure

Urban planners have identified an opportunity to use the rapid technological advancements to build smart and sustainable urban infrastructure. This smart urbanization is transforming the challenges faced by conventional urban areas into opportunities where people can share common resources without competing with one another; thus leading to better utilization of assets, improvement in infrastructural conditions, environmental conservation, and enhanced governance [20]. Smart urban areas are being built on vast networks of sensors, cameras, and other connected devices that are capable of capturing rich, real-time information from every nook and corner of the area continuously [21]. Urban planners and managers are increasingly using this huge stream of heterogenous and unstructured data for decisionmaking, with the help of partnerships with regulators, academicians, and other stakeholders [22].

Existing studies in this domain have emphasized the potential role of big data in obtaining valuable insights derived from various data sources. This can help in efective planning, design, allocation and management of services and resources across smart urban areas [23]. Researchers have used ML techniques to address a variety of urban issues and services, including social security fraud detection [24], elearning evaluation systems [25], smart urban management [26], trafic management [27], energy consumption [28], and waste management [29].

While researchers and city planners have been actively finding databased solutions for socio-technical systems such as infrastructure (in cluding communication, water, energy, and transport), and services (including healthcare, education, and waste management), there has been scant attention paid to time-constrained (e.g., disaster response scenarios) decision situations. Often such situations are characterized by abundance of heterogenous data but lack of time and often processing capabilities. However, real-time data collected from these smart urban infrastructures can also be utilized for time-constrained decisionmaking during disaster response scenarios. In this study, we have therefore acknowledged images as a valuable source of accurate information and developed innovative use-cases.

## 2.2. Decision systems for managing disaster situations

Efective disaster management relies on the timeliness of response, as well as participation of human hands from multiple, geographically distributed organizations and their communications [8]. Hence, management of information is critical for disaster response operations and involves strategic planning to ensure timely and efective prioritization and allocation of resources among discrete response activities [30]. In this regard, existing studies have asserted the vital role of information technology to refine the way communities and individuals deal with disasters [31] and have suggested the utilization of urban management information systems to assist decision makers in post-disaster situations. Researchers have stressed the urgency to consolidate discrete data sources and resources, and the necessity to collect and disseminate updated information from these distributed sources. For instance, Peng et al. [5] have proposed a DSS for analysis of heterogenous distributed data by implementing data mining to gain useful insights. Further, Delen et al. [32] have built a supply chain for collection of blood based on analytics. Their proposed solution could overcome the challenges of providing immediate medical aid in post-disaster situations.

A significant part of the secondary and tertiary communication networks including sensors and other devices get disrupted during a disaster. Only a limited part of the smart infrastructure is able to withstand the damage. The breakdown of major communication networks results in limited data transmission to remote disaster planning centers. This has prompted central disaster planning units to rely on social media data as an additional source of data for efective disaster response planning [33]. This is viable because online social communities have developed into complex information systems that are capable of providing real-time information about the ground-level situation after a disaster [34]. And these communities are increasingly using social networking sites for peer-to-peer and public backchannel communication during and after disasters [13,14]. For instance, Kogan et al. [12] have investigated the nature of information dissemination just after the Hurricane Sandy disaster of 2012. The study has found that the usage of social media platforms actually surpassed the usage of conventional modes such as fixed phone and radio [12]. As a result, emergency service agencies and city planners across various geographies have started to collect and disseminate information using their oficial social media handles during disasters [35].

Examination of social media data from Twitter and Facebook has helped researchers and emergency service agencies understand the nature of information exchange during and after a disaster [36]. Thi has enabled the development of eficient disaster assessment systems that use geo-location information to classify the impact of disasters on the basis of severity and extent of damage [37].

A thorough review of extant literature reveals that although studies have proposed relatively eficient disaster response systems, they have been fraught with an overt singular focus on a particular datatype, i.e., user-generated content on social media platforms. The efectiveness of such data analysis for disaster management can be further improved if data from real-time information systems of smart infrastructures could be integrated with them. Moreover, such attempts have primarily utilized textual content rather than the additional multimedia content (such as images and videos) available simultaneously with it. To address this gap in literature, we use a hybrid dataset which combines images collected from multiple data sources including social media platforms and smart urban infrastructures.

## 2.3. DL as an aid to decision-making process

Despite being a very powerful framework, DL has found limited adoption in extant research in information systems. Some of those ex amples include prediction of sales in the fashion industry [38], pre diction of risk for aviation incidents [39], detection of automobile claims fraud [40] and text-based emotion recognition [41]. All of these studies have utilized these techniques on huge, complex, and multidimensional datasets on which traditional algorithms have performed with very limited accuracy. Hence, there is a huge latent potential for adopting DL techniques to develop usable knowledge from such com plex datasets that have become more prevalent in recent times. For example, Kraus and Feuerriegel [42] have used DL to automate the process of using company disclosures for financial decision-making with the help of transfer learning. This system is aimed at interpreting the complexity and ambiguity of natural language.

These studies have also asserted the significance of integrating multiple heterogenous data sources (such as social media data and geographical information) for decision support situations like personalized recommendation systems [43]. Another significant application of these advanced techniques includes image analysis and classification in domains like trafic engineering [44], crime evidence analysis [45], and healthcare [46]. For instance, Pan et al. [44] have developed a vehicle logo recognition system from video surveillance data and showed that the CNN-based classifier performed better than the SVMbased classifier. From a methodological viewpoint, the limited image dataset used for this study made the proposed model prone to overfitting and required the application of transfer learning from pretrained CNN models to overcome it.

Table 1 describes that diversified applications of DL techniques to support decision-making. Despite the eficacy of DL techniques in these diverse decision support applications, there exists a clear gap in their application in time-constrained decision situations like disaster management.

## 2.4. Applications of machine and deep learning for disaster response

Analysis of disaster-related data using ML and DL techniques has significant potential for improving disaster response. However, regardless of recent advancements in DL, our literature review reveals that this technique has been sparsely used for disaster management purposes. Kundu et al. [47] have utilized DL to map post-disaster tweets to pre-defined action classes such as infrastructure damage, resources needed, resources available, and resource locations. The proposed model has performed better than the conventional bag-of-words approach. While this study has focused on textual data obtained from Twitter, another study by Attari et al. [48] has classified images collected from unmanned aerial vehicles and satellites for assessment of damage. Their proposed system first localized objects using pixel-level classification and followed that with the use of CNN to distinguish between diferent levels of damage. Compared to traditional methods of data analytics, DL techniques have produced better outcomes when used on heterogenous datasets. For instance, Song et al. [49] have used data derived from diverse sources including GPS records, earthquake data, and news report data to understand human evacuation behavior and mobility during a disaster.

The key literature related to the use of DSS for disaster management is summarized in Table 2. It reveals a research gap with respect to the application of advanced technologies, such as ML and DL techniques, for disaster response activities by utilizing the potential of the huge amount of heterogenous data (including text and other multimedia) generated by smart urban infrastructures. We intend to cover the research gap by developing a model that can analyze real-life objective visual data collected from robust smart infrastructures as well as the visual data obtained from reliable social media channels. This proposed model will use DL techniques to classify images based on presence (or absence) of potential survivors.

## 3. Research method

In this section, we discuss the data and research method used in this study. The analytical framework used in this research is shown in Fig. 1 below and is explained in the following sub-sections.

## 3.1. Data collection

The images are collected from the earthquake-hit regions of Tohoku, Japan (2011) and Bologna, Italy (2012). We have focused on earthquake-hit regions because a recent study conducted by researchers from the Centre for Research on the Epidemiology of Disasters suggested that “earthquakes (including tsunamis) were more destructive and killed more people than all other types of disaster put together, claiming nearly 55% of the total lives lost due to natural disasters”. Though we have focused on earthquakes for this study, our proposed models can also be applied in cases of other natural disasters. The two disaster sites are chosen on the basis of the following criteria: (i) they had witnessed disasters of similar scale and extent of impact on the people and infrastructure, (ii) both sites were smart urban environments embedded with IoT devices, motion cameras, remote cameras, and sensors at the time when the disaster struck.

Application of DL techniques in diferent domains to support decision-making.

<table><tr><td>Studies</td><td>Application domains</td><td>Input datatypes</td><td>Data sources</td></tr><tr><td>Loureiro et al. [38]</td><td>Prediction of sales in the fashion industry</td><td>Textual and numerical</td><td>Anonymized company retail data</td></tr><tr><td>Kratzwald et al. [41]</td><td>Emotion detection</td><td>Textual</td><td>Self-reports, Facebook posts, Tweets and literary tales</td></tr><tr><td>Guo et al. [43]</td><td>Recommendation systems</td><td>Textual</td><td>Social media and geographical data</td></tr><tr><td>Kraus and Feuerriegel [42]</td><td>Financial decision support</td><td>Textual</td><td>Mandatory company disclosure documents</td></tr><tr><td>Pan et al. [44]</td><td>Vehicle logo recognition system for traffic engineering</td><td>Video</td><td>Traffic video surveillance footage</td></tr><tr><td>Saikia et al. [45]</td><td>Crime evidence analysis</td><td>Image and video</td><td>Visual security surveillance system</td></tr><tr><td>Zhao et al. [46]</td><td>Healthcare: health monitoring</td><td>Image</td><td>Sensor data and healthcare reports</td></tr></table>

Table 2  
A summary of related literature.

<table><tr><td>Topic studied</td><td>Key focus</td><td>Data used</td><td>Findings</td></tr><tr><td rowspan="3">Decision support for urban infrastructure management</td><td>smart urban management [26]</td><td>Sensor data of water usage, vehicle parking patterns, waste disposal patterns, smart homes</td><td>Built four-tier scalable architecture to integrate and analyze heterogenous smart city data for smart urban management</td></tr><tr><td>traffic management [27]</td><td>real-time traffic information including sensor data about traffic congestion, parking areas</td><td>Evaluated emergency traffic evacuation system for unpredictable traffic incident scenarios</td></tr><tr><td>energy consumption [28]</td><td>smart electric meter data</td><td>Accurately predicted energy consumption levels of households</td></tr><tr><td rowspan="3">Identification of credible information sources post-disaster and integration for effective decision making</td><td>Social media as a credible information source [36]</td><td>Web-based survey and message count data of web forum users</td><td>Virtual communities&#x27; reliance on online social networks for information exchange boosted information quality in a post-disaster situation</td></tr><tr><td>Integration of social media data with geo-location data [37]</td><td>Tweets and their geo-tagged location data</td><td>Achieved more efficient damage prediction and assessment</td></tr><tr><td>System framework to support multi-criteria decisions [5]</td><td>Theoretical framework</td><td>Efficient incident information management system integrated varied data sources and used data mining for multi-criteria decision making</td></tr><tr><td rowspan="3">ML and DL for disaster management</td><td>Classification of text data into action classes for immediate disaster response [47]</td><td>Post-disaster tweets</td><td>DL was used to map tweets to action classes such as damage and resources needed. This method was found to be superior than the bag-of-words approach</td></tr><tr><td>Image classification for damage assessment [48]</td><td>Images collected from unmanned aerial vehicles and satellites</td><td>Image analytics performed better than traditional methods for effective damage assessment</td></tr><tr><td>Use of discrete data sources [49]</td><td>GPS records, earthquake data, news report data</td><td>Explained human evacuation behavior and mobility</td></tr></table>

We have collected images of these two sites from several data sources and created a single large image dataset of earthquake-hit urban spaces (as shown in Fig. 2). We have drawn the initial dataset from the Natural Hazards Image Database of the National Centers fo Environmental Information (www.ngdc.noaa.gov/hazardimages/) and Cambridge Earthquake Impact Database (http://www.ceqid.org/ CEQID/Home.aspx). We have supplanted the dataset with images col lected from the oficial Twitter handles and Facebook pages maintained by the local governments and emergency response services in Tokyo and Bologna. These handles have been used by oficial agencies to disseminate information and share images of the damages sufered by various sites in the afected regions. These posts have included images of urban areas with nearly demolished buildings and victims stuck in the debris along with a short textual description. The accompanying texts have reported the location from where the image has been captured and the location of the camera that has captured them.

For this study, we have collected data using event-specific keywords and hashtags. All images published within two months of each incident have been collected by restricting the timeline. This approach has been in line with other studies that have used social media images for analytics in the domain of disaster management [50]. Duplicate posts with images have been removed by comparing their textual content using cosine similarity. The threshold for similarity of two posts has been taken as 0.8 for this study.

The key details of data collected from both disaster sites are presented in Table 3 below.

## 3.2. Pre-processing

The image dataset has gone through a four-stage manual data preparation process to ensure relevance and relatedness to the disaster events under consideration (refer to pre-processing block of Fig. 2). The first phase included filtering of images manually for removing unrelated

![](/api/attachments/QJWMMFAY/fulltext/images/5f955254a12d48554d52581180a32966f42d9d0f768c462a51b03de599f2d23e.jpg)  
Fig. 1. The analytical framework used in this study.

![](/api/attachments/QJWMMFAY/fulltext/images/77e3f24b04334892a7b9a72b5189e5b7bb54dd7604df40f4afc14edb09e143ad.jpg)  
Original image- with human

![](/api/attachments/QJWMMFAY/fulltext/images/c116292aca8d2d3f396b9049bee2c941b545235d513f3f85b0866245b7f9cb6d.jpg)  
Transformed imagewith human

![](/api/attachments/QJWMMFAY/fulltext/images/a02b76a9836067620bb0be5bec70af568c47a5af90c775becfbc06479053415d.jpg)  
Transformed imagewith human

![](/api/attachments/QJWMMFAY/fulltext/images/69069bb6573007cd66d22bf3b758bc70a8f853586a878d6bc3c59ec2d7905788.jpg)  
Transformed imagewith human

![](/api/attachments/QJWMMFAY/fulltext/images/f27177d086df927fceeb6b1e0bb5baf9ace36af00be614864bd52529d55e2996.jpg)  
Original imagewithout human

![](/api/attachments/QJWMMFAY/fulltext/images/595baad697951ad73411c1fb54ab6c6a48f91b8607b05bf0dbe39da72c0c22c9.jpg)  
Transformed imagewithout human

![](/api/attachments/QJWMMFAY/fulltext/images/ce14838f7d9cbfdf8647e5b415ad022a8fddadc8a62fb6e4b481b6393fc1d627.jpg)  
Transformed imagewithout human

![](/api/attachments/QJWMMFAY/fulltext/images/b4dc5ce040298d04a8b680fe99721bd68c93e6eb4fab8ec02d9edb045129bd04.jpg)  
Transformed imagewithout human

Fig. 2. Examples of original and transformed images after pre-processing.

images. The second phase has included labeling of image manually.

For filtering of images, two external domain experts independently examined the images manually by inspecting their sources and appropriateness for the study. Unrelated images (e.g., including those containing banners, celebrities, advertisements calling for donations and outside help) are removed in the first stage. We have pruned the dataset by eliminating images that have showed emergency relief workers doing rescue work. These images are considered irrelevant for the analysis as the model is likely to wrongly classify these images owing to the DL model being trained to classify images with a human body part or whole (i.e., victims trapped under debris who need to be rescued). Following this, the remaining dataset is labelled manually into two classes: (i) Class I are images with human body parts or whole human bodies (ii) Class II are images with no traces of human body parts.

Finally, we have pre-processed the dataset following the steps that are suggested by Jia et al. [51]. The images are first uniformly resized to ensure identical aspect ratio and size. This step is necessary because the neural networks work on square shaped images only. Next, the global zero-mean unit variance batch normalization is performed to reduce internal covariate shift [52] and to improve training time as well as stability. To capture translational invariance, and reduce overfitting, we further applied label-preserving transformations to the dataset [53]. The image data transformation methods used for this study have in cluded rotation, translation, rescaling, flipping, shearing, and stretching [53]. Image transformation is a necessary pre-processing step as it presents diferent image variations to the neural networks, which in turn helps them learn better features and ensures overall improvement in performance generalization. These perturbed versions of the original images are finally augmented to the existing dataset. Some examples of transformed and original labelled images present in the dataset are shown in Fig. 2. At the end of the data preparation stage, the final dataset consisted of 16,041 images.

## 3.3. Classification

The proposed ML and DL models classify a large image dataset drawn from earthquake-hit smart urban regions. The objective of the classification task is to classify the images based on the presence of human survivors trapped under debris. To compare the performances of the techniques, this study employs three advanced DL and two ML techniques (as shown in Fig. 1).

## 3.3.1. ML techniques

The ML models used for this study are Support Vector Machines (SVM) [54] and Artificial Neural Networks (ANN) [55]. Past studies have shown that SVM and ANN have outperformed other widely used ML techniques for similar binary classification tasks (that is discussed in this research) involving large image datasets [56–58]. Hence, we chose SVM and ANN for comparison with the DL techniques. Researchers have found that though SVMs are slower than Decision trees (DT) and Random Forests (RF) in classifying new instances, but they result in significantly higher classification accuracies [57]. Similarly, ANN scores higher than DT and RF in terms of accuracies as well as resource utilization [58]. ANN transform an input by taking it through a series of fully connected hidden layers including the final output layer. Therefore, ANN are expected to perform better for simple and centered images but underperform for images with complex variations.

## 3.3.2. DL techniques

DL is essentially a subset of classical ML, and an advanced version of artificial neural networks (ANN). ANN are biologically inspired computational networks having interconnected single processing units (neurons) arranged in layers. While intermediate layers of traditional ANNs are fully connected intermediate layers (or hidden layers), the DL convolutional neural networks (CNNs) characteristically consist of sparsely connected convolutional layers and pooling layers in addition to a fully connected layer. Unlike in other neural networks, these convolutional layers allow weight sharing and automated extraction of visual features from input images [59]. Therefore, CNNs are well suited for image recognition and classification tasks as the stack of convolutional and pooling layers allow the networks to learn hierarchies of representations, high-level features from low-level pixels. Moreover, transfer learning (technique explained in the following subsection) and the deep network structure enable CNNs to be adaptable for diferent applications within the same domain and also perform better with larger image datasets. Hence, we chose to apply CNN for this study.

Further, the convolutional layers consist of a collection of learnable parameters (also called hyperparameters), that are set before the beginning of the learning process. Tuning of these parameters was done by applying exhaustive search. These layers, along with other fully connected layers, are responsible for transforming the input images to the final class scores.

Among the widely used CNN architectures, the VGG-16 architecture has been used by Attari et al. [48] to classify images in order to successfully identify objects and assess damage in post-disaster scenarios. However, VGG-16 architecture sufers from overfitting as well as significantly higher training time due to a slower feature extraction process [60]. It thus requires huge computation time and resources making it ineficient when applied to image datasets with more complex features. Therefore, the variants of CNN used in this study include AlexNet, Inception-V3, and ResNet-50 [61]. These architectures have been developed as newer modified versions of the existing VGG models to achieve improvement in computational resources and to handle the problem of overfitting [60].

Table 3  
A summary of data collected from Facebook and Twitter for Tokyo and Bologna earthquakes.

<table><tr><td>Disaster location</td><td>Keywords used</td><td>No. of posts</td><td>No. of images</td><td>No. of filtered posts</td><td>No. of filtered images</td></tr><tr><td>Tohoku, Japan – 2011</td><td>Tohoku earthquake, Tohoku damage, Tohoku disaster, Tohoku victims, Tohoku crisis, Tohoku people trapped</td><td>279,033</td><td>82,291</td><td>3284</td><td>2174</td></tr><tr><td>Bologna, Italy - 2012</td><td>Bologna earthquake, Bologna damage, Bologna disaster, Bologna victims, Bologna crisis, Bologna people trapped</td><td>649,264</td><td>174,566</td><td>6041</td><td>4917</td></tr><tr><td>Total</td><td></td><td>928,297</td><td>256,857</td><td>9325</td><td>7091</td></tr></table>

AlexNet is one of the earliest deep neural networks designed for complex scene image classification using ImageNet data. It has displayed higher classification accuracy as compared to the conventionally used ML techniques [61]. The other networks and their newer modified versions (versions are diferent in terms of the layers present in the networks), including ResNet and Inception, have been developed sub sequently to enhance classifier accuracy and resource utilization. We chose ResNet-50 and Inception-V3 versions of the networks as these models have a good fit with the size and complexity of the classification task without a lot of demand on time and computational resources [61].

## 3.3.3. Transfer learning

Transfer learning is a ML algorithm in which a model trained for one task is re-purposed for a second task. It helps to train a large target network in the absence of a large target dataset, thus overcoming the limitation of a small training set and reduce overfitting [62]. It improves the performance of a target domain by using knowledge from a source domain (possibly diferent). Transfer learning ofers significant improvement over other traditional learning methods, such as un supervised learning and reinforcement learning, in terms of time spent on model building and training datasets [62]. Studies have shown that transfer learning, when performed along with fine-tuning of pre-trained models, gives better accuracies than cases where models were built and parameters were initialized from scratch [63]. Therefore, we applied transfer learning to our proposed target models.

Following the transfer learning approach adopted by Ng et al. [64], we re-purposed algorithm snippets of the existing pre-trained deep network models (termed as source networks) to fine-tune their existing parameters in order to expedite results and help gain better accuracies at the same time. Therefore, we trained the new target DL models on source networks (AlexNet, ResNet-50, Inception-V3) with their n layers chosen as the first n layers of our target models. To fine-tune the pretrained models, we selectively retrained some of these n layers. Finetuning these models enabled us to improve generalization [65]. We finally initialized and trained the last layer of each new target model for this study. The ‘softmax’ function was used in the final layer of the classifier for all three target CNN models under a cross-entropy system [66].

Further, to improve the models' ability to resist overfitting, we partitioned the initial training dataset into K (K = 5) folds and per formed K fold cross-validation. The best parameters combinations for the models are found by repeating the training-validation procedure 5 times (same as the number of folds defined). To optimize the choice of parameters, we adopted a brute-force search approach which is terminated when the training and validation errors have stabilized. The in itialized parameters for the CNN architectures are presented in Table 4 below. Additionally, a comparison of validation and training errors for the models have shown that the validation error values are within

0.04% of the training errors, therefore confirming insignificant overfitting.

## 3.4. Performance metrics

To compare the performances of the variants of DL methods with that of the traditional ML methods, five models are chosen: SVM and ANN from ML and three architectural variants of the CNN from the DL domain.

Six widely used metrics are calculated to evaluate the overall performance of the classification models. These metrics are positive predictive value (PPV), sensitivity (Sn), F1-score, accuracy (A), specificity (Sp) and negative predictive value (NPV) [67–69]. They are defined below.

$$
\text { Positive   predictive   value } (P P V) = \frac {\alpha}{\alpha + \gamma}
$$

$$
S e n s i t i v i t y (S n) = \frac {\alpha}{\alpha + \delta}\tag{1}
$$

(2)

$$
F 1 - s c o r e = \frac {2 * P P V * S n}{P P V + S n}\tag{3}
$$

$$
A c c u r a c y (A) = \frac {\alpha + \beta}{\alpha + \beta + \gamma + \delta}\tag{4}
$$

$$
S p e c i f i c i t y (S p) = \frac {\beta}{\beta + \gamma}\tag{5}
$$

$$
N e g a t i v e p r e d i c t i v e v a l u e (N P V) = \frac {\beta}{\beta + \delta}\tag{6}
$$

In the above equations, the number of true positives and the number of true negatives is denoted by α and $\beta ,$ and the number of false positives and false negatives is denoted by γ and δ respectively.

Further, the geometric mean (GM) score is considered to be a useful measure to evaluate models that are used on two-class imbalanced datasets [70]. It aggregates both specificity and sensitivity. Thus, the scores for geometric mean, false omission rate [71] are also calculated to evaluate the performances of the final models. They are calculated as shown below.

$$
F a l s e o m i s s i o n r a t e (F O R) = 1 - N P V\tag{7}
$$

$$
\text { Geometric   mean } (G M) = \sqrt {S n \times S p}\tag{8}
$$

We have also compared accuracy, sensitivity, and specificity scores for the image dataset with the same scores that are obtained after adding a controlled amount of statistical noise to the dataset. This is

## Table 4

Parameters for CNN architectures.

<table><tr><td></td><td>ResNet-50</td><td>Inception-V3</td><td>AlexNet</td></tr><tr><td>Batch size</td><td>8</td><td>16</td><td>32</td></tr><tr><td>Number of training epochs</td><td>10</td><td>10</td><td>30</td></tr><tr><td>Learning rate</td><td>0.001</td><td>0.005</td><td>0.001</td></tr><tr><td>Number of layers in target network model</td><td>51</td><td>49</td><td>9</td></tr></table>

Table 5  
A comparison of accuracy scores for a sample of images.

<table><tr><td rowspan="2">CNN architectures</td><td rowspan="2">Class accuracies</td><td><img src="/api/attachments/QJWMMFAY/fulltext/images/f8e6a79bc97d88c25ad0aee286124b6a607eb091c1ee854419672b03807ced24.jpg"/></td><td><img src="/api/attachments/QJWMMFAY/fulltext/images/2eb73224353ed7fbee56ff1fc9130889d62d60d805ae37bb0eb123f26680542a.jpg"/></td><td><img src="/api/attachments/QJWMMFAY/fulltext/images/8eb33b63a3fd15aaa432fce4a0b434804679ac1653c219a51efd847674602c83.jpg"/></td><td><img src="/api/attachments/QJWMMFAY/fulltext/images/721787a856c125fe680fac1a7eae2187be936b43dbf2b43baa4ebd7df0a36cb2.jpg"/></td></tr><tr><td>Image 1</td><td>Image 2</td><td>Image 3</td><td>Image 4</td></tr><tr><td rowspan="2">ResNet-50</td><td>Class I</td><td>0.0107</td><td>0.9378</td><td>0.8918</td><td>0.9831</td></tr><tr><td>Class II</td><td>0.9893</td><td>0.0622</td><td>0.1082</td><td>0.0169</td></tr><tr><td rowspan="2">Inception V3</td><td>Class I</td><td>0.0176</td><td>0.9411</td><td>0.8563</td><td>0.9756</td></tr><tr><td>Class II</td><td>0.9824</td><td>0.0589</td><td>0.1437</td><td>0.0244</td></tr><tr><td rowspan="2">AlexNet</td><td>Class I</td><td>0.0258</td><td>0.8865</td><td>0.8157</td><td>0.9457</td></tr><tr><td>Class II</td><td>0.9742</td><td>0.1135</td><td>0.1843</td><td>0.0543</td></tr><tr><td rowspan="2">SVM</td><td>Class I</td><td>0.0552</td><td>0.7867</td><td>0.6789</td><td>0.9312</td></tr><tr><td>Class II</td><td>0.9448</td><td>0.2133</td><td>0.3211</td><td>0.0688</td></tr><tr><td rowspan="2">ANN</td><td>Class I</td><td>0.0667</td><td>0.8140</td><td>0.6153</td><td>0.9308</td></tr><tr><td>Class II</td><td>0.9333</td><td>0.1860</td><td>0.3847</td><td>0.0692</td></tr></table>

Class I are images with human body parts or whole human bodies and class II are images with no traces of human body parts.

done as a robustness check. The results have shown that the performances of the models do not significantly worsen after adding noise to the dataset. This confirms that the ML and DL models used in this re search are robust.

## 4. Results

The results of the study are presented and discussed in this section.

We first present a comparison of prediction accuracy for a sample of images obtained by the models in Table 5. While image 1 does not have any human bodies present, image 4 shows a prominent whole human body (i.e., victim crying for help). These images are accurately identi fied by all three CNN architectures with comparable accuracies. However, the accuracies for image 2 (of a small baby stuck under the debris of broken walls) and image 3 (minuscule human body parts) are com paratively lower but are still decisive.

Table 6 finally summarizes the performance scores that are obtained for each of the DL and ML models used in this study.

The results that are presented in Table 6 show that all proposed models exhibit high classification ability for images of disaster-hit regions based on the presence (or absence) of victims in them, with ResNet-50 exhibiting significantly higher scores for all evaluation metrics, as compared to other models.

The PPV score for the best performing model (ResNet-50) is found to be 90.81% while its sensitivity and specificity are found to be 93.33% and 91.05% respectively. The scores for FOR and GM have also been reported in Table 6 above. FOR measures the proportion of false negatives that are incorrectly rejected and GM indicates the balance between classification performances for binary classification. Thus, ResNet-50 model with the lowest value of FOR (0.0649) and highest GM score (0.9219) is the best performing model.

Although accuracy is widely used to evaluate classifiers its value depends on the chosen prediction probability threshold, and is hence not a very robust performance metric [72]. Thus, we also report Receiver Operating Characteristics - Area under curve (ROC-AUC) values for our proposed models in Table 6. This curve takes into account all prediction probability threshold values and gives an overall performance measure. It ranges from 0 to 1 and AUC = 0.5 signifies random guessing whereas AUC = 1 signifies perfect prediction [73].

Table 6  
Performance scores for ML and DL models on test data.

<table><tr><td rowspan="2">Metrics</td><td colspan="3">DL</td><td colspan="2">ML</td></tr><tr><td>ResNet-50</td><td>Inception V3</td><td>AlexNet</td><td>SVM</td><td>ANN</td></tr><tr><td>Accuracy</td><td>0.9216</td><td>0.8784</td><td>0.8054</td><td>0.7595</td><td>0.7432</td></tr><tr><td>Sensitivity</td><td>0.9333</td><td>0.8778</td><td>0.8056</td><td>0.7486</td><td>0.7322</td></tr><tr><td>Specificity</td><td>0.9105</td><td>0.8789</td><td>0.8053</td><td>0.7701</td><td>0.7540</td></tr><tr><td>PPV</td><td>0.9081</td><td>0.8729</td><td>0.7967</td><td>0.7611</td><td>0.7444</td></tr><tr><td>F1 score</td><td>0.9205</td><td>0.8753</td><td>0.8011</td><td>0.7548</td><td>0.7383</td></tr><tr><td>NPV</td><td>0.9351</td><td>0.8836</td><td>0.8138</td><td>0.7579</td><td>0.7421</td></tr><tr><td>FOR</td><td>0.0649</td><td>0.1164</td><td>0.1862</td><td>0.2421</td><td>0.2579</td></tr><tr><td>GM</td><td>0.9219</td><td>0.8784</td><td>0.8054</td><td>0.7593</td><td>0.7430</td></tr><tr><td>ROC-AUC</td><td>0.9814</td><td>0.9283</td><td>0.9148</td><td>0.8212</td><td>0.7919</td></tr></table>

Table 7  
Per-class performance scores and ROC-AUC score for the DL models.

<table><tr><td rowspan="2">Metrics</td><td colspan="2">ResNet-50</td><td colspan="2">Inception-V3</td><td colspan="2">AlexNet</td></tr><tr><td>Class I</td><td>Class II</td><td>Class I</td><td>Class II</td><td>Class I</td><td>Class II</td></tr><tr><td>Accuracy per class</td><td>0.9333</td><td>0.9105</td><td>0.8778</td><td>0.8789</td><td>0.8056</td><td>0.8053</td></tr><tr><td>PPV per class</td><td>0.9081</td><td>0.9351</td><td>0.8729</td><td>0.8836</td><td>0.7967</td><td>0.8138</td></tr><tr><td>Sensitivity per class</td><td>0.9333</td><td>0.9105</td><td>0.8778</td><td>0.8789</td><td>0.8056</td><td>0.8053</td></tr><tr><td>F1 score per class</td><td>0.9205</td><td>0.9227</td><td>0.8753</td><td>0.8813</td><td>0.8011</td><td>0.8095</td></tr></table>

Class I are images with human body parts or whole human bodies and class II are images with no traces of human body parts.

Additionally, the per-class scores of sensitivity, specificity, and F1- score of the DL-based CNN architectures are calculated to determine the performance concerning each class in the image dataset. These measures account for model performance for uneven class distributions. The results are reported in Table 7 below.

Accurately identified images belong to either true positives or true negatives. Since false positives and false negatives denote cases where images are wrongly classified, these cases restrict the performances of the models. Accuracy as a metric is more important for image retrieval systems (e.g., for Google Images) [18]. Since, the primary focus of disaster response is to save as many lives as possible, decision-makers can allow false positives, but cannot allow false negatives. While in cluding false positives will escalate the number of emergency workers and resources required for disaster response, excluding false negatives may lead to loss of lives due to misclassification [21]. The findings of this study allow us to conclude that a multi-layer CNN is capable of achieving notable results on a large complex image dataset.

## 5. Discussion

This study utilizes CNN for classification of a large image dataset drawn from earthquake-hit smart urban sites. In disaster response decision scenarios, decision-makers need to employ a similar method for decisions concerning the assessment of disaster-afected areas and then prioritization of relief work to sites that have a higher probability of trapped victims. With due consideration to both model performance and the required computational capabilities, we have found that

ResNet-50 and Inception-V3 surpass all other architectures.

## 5.1. Performance comparison of ML and DL models

Tables 5 and 6 illustrate that the deep CNN architectures (ResNet-50, Inception-V3, and AlexNet) significantly outperform ML approaches (SVM and ANN). It suggests the need to deploy DL-based systems fo disaster response after having fine-tuned them specifically to the con text of the problem.

In this study, the proposed models have been able to classify images with high accuracies. These accuracies however show trends of further improvement with decreasing noise in the dataset. This trend of per formance improvement is much stronger for the ML models. Therefore, our analysis reveals DL models are able to handle noise in the dataset significantly better than their ML counterparts. The greater depth in the network layers for the CNN models enables this improvement in per formance [59].

Moreover, the significant diference in performances for all evaluation metrics can be attributed to the inherent architectural diferences between the CNN and traditional ANN which enable CNN to reduce computational complexity while ensuring translational invariance. The DL models perform better as they are able to utilize their parametric space better and allocate significantly lower memory for parameters from the start [74].

CNNs are more capable of handling issues relating to image recognition and classification. Similar patterns are also observed for sensitivity, specificity, and PPV scores.

## 5.2. DL-based decision support system for efective disaster response

The DL techniques are able to identify images with partially visible human body parts with a high degree of accuracy. However, this whole process involves complex interpretations of the outcomes that are more suitable for decision analysts with suficient knowledge and expertise of DL models. The operationalization of this innovative solution for ground-level workers and disaster planners would require the super imposition of the output with geolocation data to support crucial de cision making about prioritization of relief response.

Further, efective disaster response activities primarily involve prioritization of limited resources to help save the maximum number of lives possible. Hence, relief eforts need to be directed towards disaster sites that have been correctly identified by our model as having the maximum number of victims trapped under debris. This strategy will help curtail wastage of valuable resources and time in conventional heuristics-based rescue operations. Future studies should therefore aim to integrate resource allocation process with the DL system. Further research in this domain could also potentially pave way for deployment of similar DSS with more comprehensible, illustrative output in the form of clearly identified disaster zones with survivors. The result could then be easily interpreted by emergency workers on site with little training.

## 6. Implications

## 6.1. Implications for decision makers in the context of disaster response

Traditionally, most critical disaster response decisions are based on textual data arising from community intelligence of disaster-affected sites. This information is seldom accurate and reliable, but due to the lack of other sources of information, that can be easily collected and assimilated, most decisions tend to rely on them. An image is a much richer source of information than text but requires greater processing to derive useful knowledge for decision-making. We have demonstrated the application of image processing and the use of image data in a domain that traditionally depended on text-based data. Although processing of image data is more complex than textual data, the results from the demonstrated technique can be used by decision makers after minimal training for using such data in time-constrained decision situations.

With a focus on efective prioritization of limited resources towards saving maximum number of lives, the aim of decision-making based on image analytics would be to cater to disaster sites that have been identified accurately only (true positives). As the availability of resources increases, the region of relief operations will widen and include sites with some expectation of finding victims (both true positives and false negatives).

Finally, this study also provides empirical evidence of the superiority of DL methods over the traditional ML techniques. As technologies in both these dimensions mature and become readily available for usage by emergency workers at the ground and middle level, these insights will become directly applicable. Eforts can be geared towards setting up requisite infrastructure for provisioning and processing of image data from various heterogenous smart infrastructures, using DL techniques.

## 6.2. Implications for regulators in the context of disaster response

Disasters and other social crises are accompanied with degeneration of social reporting into collective rumor mills [3]. However, lack of reliable information from credible sources often compels critical decisions to be made based on community intelligence. Given the enormous implications due to wrong decisions in such situations, it is important to take decisions which are evidence-based. Data provided by smart infrastructures are a good source of accurate and reliable information. This study has demonstrated an example of usage of such information (primarily from image data) to assist with such decisions. Eforts by regulators should be geared towards the installation of such infrastructure to improve city management and to aid with disaster relief during adverse situations. This would also allow regulators to ofload some critical decision making to ground level emergency personnel who have the latest information about the disaster situation. Crucial operational decisions can then be taken by rescue workers leading to significantly lower response time.

## 6.3. Implications for research

The insights from this study have significant implications for researchers, especially in the domain of decision support for disaster management. Firstly, image data from smart infrastructures has not been used to aid decision making to the best of our knowledge. We have demonstrated its capabilities in the domain of disaster management, but we believe similar analytic techniques can be deployed in other domains like DSS for healthcare and trafic management. Scholars should consider using this rich data and DL methods to discover knowledge that can help in efective decision making.

Secondly, we have found that the application of DL methods has the potential to boost the performance of conventional DSS in disaster response. These methods can also be applied to other data-aided (for both textual and visual data) decision-making scenarios. Future scholars can therefore deploy similar techniques to improve the efectiveness of such systems further. However, such applications would require scholars to contextualize the DL neural network architectures specific to the domains to ensure optimal accuracy.

## 7. Conclusion

This study puts focus on the DL method to demonstrate the capability of image analytics in aiding resource prioritization decisions for disaster response. It uses images as a novel source of accurate information during disasters and demonstrates their technical eficacy for decision support. The images are collected from earthquake-hit sites and are classified to identify survivors in debris. DL techniques are found to perform better than the ML techniques.

Additionally, we also aim to integrate information from other sources, such as textual data from microblogs and online communities, with image classifiers to help emergency personnel make more informed decisions. This study also has important practical applicability with the gradual maturation of analytic technologies and advances in the capabilities of portable devices. Data collected from smart infrastructures can be collected and processed by emergency personnel and response planning can be made on site as against centrally, as done at this time. This can improve the efectiveness of disaster response in emergency situations.

## Contribution

The authors do not wish to include any author contribution statement for the paper.

## References

[1] T.H. Davenport, L. Prusak, Working With Knowledge : How Organizations Manage What They Know. Harvard Business School Press. 1998.

[2] L. Argote, Input uncertainty and organizational coordination in hospital emergency units, Adm. Sci, O. 27 (2006) 420–434.

[3] O. Oh, M. Agrawal, H.R. Rao, Community intelligence and social media services: rumor theoretic analysis of tweets during social crises, MIS Q. 37 (2013) 407–426.

[4] V. Hristidis, S.-C. Chen, T. Li, S. Luis, Y. Deng, Survey of data management and analysis in disaster situations, J. Syst. Softw. 83 (2010) 1701–1714.

[5] Y. Peng, Y. Zhang, Y. Tang, S. Li, An incident information management framework based on data integration, data mining, and multi-criteria decision making, Decis. Support, Syst, 51 (2011) 316–327.

[6] J. Lee, N. Bharosa, J. Yang, M. Janssen, H.R. Rao, Group value and intention to use - a study of multi-agency disaster management information systems for public safety, Decis, Support, Syst, 50 (2011) 404–414.

[7] H.T. Moges, V. Van Vlasselaer, W. Lemahieu, B. Baesens, Determining the use of data quality metadata (DOM) for decision making purposes and its impact on decision outcomes - an exploratory study, Decis. Support, Syst. 83 (2016) 32–46.

[8] J.S.S. Santiago, W.S. Manuela, M.L.L. Tan, S.K. Sañez, A.Z.U. Tong, Of timelines and timeliness: lessons from typhoon Haiyan in early disaster response, Disasters 40 (2016) 644–667.

[9] R. Stephenson, P.S. Anderson, Disasters and the information technology revolution, Disasters 21 (1997) 305–334.

[10] R.R. Rao, J. Eisenberg, T. Schmitt, Improving Disaster Management: The Role of IT in Mitigation, Preparedness, Response, and Recovery, National Academies Press 2007.

[11] J. Radianti, S.R. Hiltz, L. Labaka, An overview of public concerns during the recovery period after a major earthquake: Nepal Twitter analysis, Proc. Annu. Hawai Int. Conf. Syst. Sci., Hawaii, 2016, pp. 136–145.

[12] M. Kogan, L. Palen, K.M. Anderson, Think local, retweet global: retweeting by the geographically-vulnerable during hurricane sandy, Proc. 2015 ACM Int. Conf. Comput. Coop. Work Soc. Comput, 2015, pp. 981–993.

[13] Y. Xiao, Q. Huang, K. Wu, Understanding social media data for disaster management, Nat. Hazards 79 (2015) 1663–1679.

[14] P. Zlateva, D. Velev, Use of social media in natural disaster management, Int. Proc. Econ. Dev. Res. (2012) 41–45.

[15] P. Sakhardande, S. Hanagal, S. Kulkarni, Design of disaster management system using IoT based interconnected network with smart city monitoring, Proc. Int. Conf. Internet Things Appl. IOTA 2016, Pune, India, 2016, pp. 185–190.

[16] D. Delen, H. Demirkan, Data, information and analytics as services, Decis. Support. Svst, 55 (2013) 359–363.

[17] S.F. Da Silva, M.X. Ribeiro, J.D.E.S. Batista Neto, C. Traina-Jr., A.J.M. Traina, Improving the ranking quality of medical image retrieval using a genetic feature selection method, Decis. Support. Syst. 51 (2011) 810–820.

[18] S.H. Kwok, J.L. Zhao, Content-based object organization for eficient image retrieval in image databases, Decis, Support, Syst, 42 (2006) 1901–1916.

[19] C. Plagemann, V. Ganapathi, D. Koller, S. Thrun, Real-time identification and localization of body parts from depth images, Proc. IEEE Int. Conf. Robot. Autom., Alaska, 2010, pp. 3108–3113

[20] P. Geofron, Smart cities and smart mobilities, Automob. Revolut. Towar. A New Electro-Mobility Paradig, 1st ed., Springer International Publishing, Cham, 2016, pp. 87-98

[21] N. Chaudhuri, I. Bose, Application of image analytics for disaster response in smart cities, Proc. Hawaiian Int, Conf. Syst, Sci., Hawaii, 2019, pp. 3036–3045

[22] S. Bresciani, A. Ferraris, M. Del Giudice, The management of organizational ambidexterity through alliances in a new context of analysis: internet of things (IoT) smart city proiects, Technol, Forecast. Soc, Change 136 (2018) 331–338.

[23] S. Guha, S. Kumar, Emergence of big data research in operations management information systems, and healthcare: past contributions and future roadmap, Prod Oper. Manag. 27 (2017) 1724–1735.

[24] V. Van Vlasselaer, T. Eliassi-Rad. L. Akoglu, M. Snoeck, B. Baesens, GOTCHA! Network-based fraud detection for social security fraud, Manag. Sci. 63 (2016)

3090–3110.

[25] A. Oztekin, D. Delen, A. Turkyilmaz, S. Zaim, A machine learning-based usabilit evaluation method for eLearning systems, Decis. Support. Syst. 56 (2013) 63–73.

[26] M.M. Rathore, A. Ahmad, A. Paul, S. Rho, Urban planning and building smart cities based on the internet of things using big data analytics, Comput. Netw. 101 (2016) 63–80.

[27] G.L. Hamza-Lup, K.A. Hua, R. Peng, Leveraging e-transportation in real-time trafic evacuation management, Electron. Commer. Res. Appl. 6 (2007) 413–424.

[28] K. Hopf, M. Sodenkamp, T. Staake, Enhancing energy eficiency in the residentia sector with smart meter data analytics, Electron. Mark. 28 (2018) 453–473.

[29] N. Srikantha, K. Moinuddin, L.K. S, A. Narayana, Waste management in ioT-enabled smart cities: a survey, Int. J. Eng. Comput. Sci 6 (2017) 2319–7242.

[30] C.W. Fisher, B.R. Kingma, Criticality of data quality as exemplified in two disasters, Inf. Manag. 39 (2001) 109–116.

[31] V. Hristidis, S.C. Chen, T. Li, S. Luis, Y. Deng, Survey of data management and analysis in disaster situations, J. Syst. Softw. 83 (2010) 1701–1714.

[32] D. Delen, M. Erraguntla, R.J. Mayer, C.N. Wu, Better management of blood supplychain with GIS-based analytics, Ann. Oper. Res. 185 (2011) 181–193.

[33] M. Turof, S.R. Hiltz, V.A. Bañuls, G. Van Den Eede, Multiple perspectives on planning for emergencies: an introduction to the special issue on planning and foresight for emergency preparedness and management, Technol. Forecast. Soc. Change 80 (2013) 1647–1656.

[34] V. Senadheera, M. Warren, S. Leitch, Social media as an information system: im proving the technological agility, Enterp. Inf. Syst. 11 (2017) 512–533.

[35] R. Subba, T. Bui, Online convergence behavior, social media communications and crisis response: an empirical study of the 2015 Nepal earthquake police Twitter project, Hawaiian Int. Conf. Syst. Sci., Hawaii, 2017, pp. 284–293.

[36] Y. Lu, D. Yang, Information exchange in virtual communities under extreme disaster conditions, Decis. Support. Syst. 50 (2011) 529–538

[37] D. Wu, Y. Cui, Disaster early warning and damage assessment analysis using social media data and geo-location information, Decis. Support. Syst. 111 (2018) 48–59.

[38] A.L.D. Loureiro, V.L. Miguéis, L.F.M. da Silva, Exploring the use of deep neural networks for sales forecasting in fashion retail, Decis. Support. Syst. 114 (2018) 81–93.

[39] X. Zhang, S. Mahadevan, Ensemble machine learning models for aviation inciden risk prediction, Decis. Support, Syst. 116 (2019) 48–63.

[40] Y. Wang, W. Xu, Leveraging deep learning with LDA-based text analytics to detect automobile insurance fraud, Decis. Support. Syst. 105 (2018) 87–95

[41] B. Kratzwald, S. Ilić, M. Kraus, S. Feuerriegel, H. Prendinger, Deep learning for afective computing: text-based emotion recognition in decision support, Decis Support. Syst. 115 (2018) 24–35.

[42] M. Kraus, S. Feuerriegel, Decision support from financial disclosures with deep neural networks and transfer learning, Decis. Support. Syst. 104 (2017) 38–48.

[43] J. Guo, W. Zhang, W. Fan, W. Li, Combining geographical and social influences with deep learning for personalized point-of-interest recommendation, J. Manag. Inf. Syst. 35 (2018) 1121–1153.

[44] C. Pan, Z. Yan, X. Xu, M. Sun, J. Shao, D. Wu, Vehicle logo recognition based on deep learning architecture in video surveillance for intelligent trafic system, Proc. 2013 IET Int. Conf. Smart Sustain. City, 2013, pp. 123–126.

[45] S. Saikia, E. Fidalgo, E. Alegre, L. Fernández-Robles, Object detection for crime scene evidence analysis using deep learning. Lect. Notes Comput. Sci. (Including Subser. Lect. Notes Artif, Intell. Lect. Notes Bioinformatics). 2017, pp. 14–24.

[46] R. Zhao, R. Yan, Z. Chen, K. Mao, P. Wang, R.X. Gao, Deep learning and its applications to machine health monitoring, Mech. Syst. Signal Process. 115 (2019) 213-237

[47] S. Kundu, P.. Srijith, M.S. Desarkar, Classification of short-texts generated during disasters: a deep neural network based approach, IEEE/ACM Int. Conf. Adv. Soc. Networks Anal. Min, IEEE, Barcelona, Spain, 2018, pp. 790–793.

[48] N. Attari, F. Ofli, M. Awad, J. Lucas, S. Chawla, Nazr-CNN: fine-frained classification of UAV imagery for damage assessment, Proc. Int. Conf. Data Sci. Ady. Anal. IEEE, Tokyo, Japan, 2017, pp. 50–59.

[49] X. Song, R. Shibasaki, N.J. Yuan, X. Xie, T. Li, R. Adachi, DeepMob: learning deep knowledge of human emergency behavior and mobility from big and heterogeneous data ACM Trans Inf Syst, 35 (2017).1-19

[50] F. Alam, M. Imran, F. Ofli, Image4Act: online social media image processing for disaster response, Proc. IEEE/ACM Int. Conf. Adv. Soc. Networks Anal. Mining, ASONAM 2017 Sydney Australia 2017 pn 601–604

[51] Y. Jia, E. Shelhamer, J. Donahue, S. Karayev, J. Long, R. Girshick, S. Guadarrama, T. Darrell, Cafe: convolutional architecture for fast feature embedding, Proc. 22nd ACM Int. Conf. Multimed, 2014, pp. 657–678.

[52] S. Iofe, C. Szegedy, Batch normalization: accelerating deep network training by reducing internal covariate shift, Proc. 32nd Int. Conf. Int, Conf. Mach. Learn., Lille France, 2015. pp. 448–456.

[53] A. Krizhevsky, I. Sutskever, G.E. Hinton, ImageNet classification with deep con volutional neural networks. Commun, ACM 60 (2017) 1097–1105

[54] JA.K. Suvkens. J. Vandewalle. Least squares support vector machine classifiers Neural, Process, Lett, 9 (1999) 293–300

[55] R.P. Lippmann, An introduction to computing with neural nets, IEEE ASSP Mag. 4 (1987).4–22

[56] S. Lessmann, B. Baesens, H.V. Seow, L.C. Thomas, Benchmarking state-of-the-art classification algorithms for credit scoring: an update of research, Eur. J. Oper. Res. 247 (2015).124–136

[57] M. Arun Kumar, M. Gopal, A hybrid SVM based decision tree, Pattern Recogn. 43 (2010).3977–3987

[58] H. Rouabeh, C. Abdelmoula, M. Masmoudi, Performance evaluation of decision tree and neural network techniques for road scene image classification task, Proc. Int.

Image Process. Appl. Syst. Conf., Sfax, Tunisia, 2014, pp. 1–6.

[59] J. Tao, A.V. Deokar, A. Deshmukh, Analysing forward-looking statements in initial public ofering prospectuses: a text analytics approach, J. Bus. Anal. 1 (2018) 54–70.

[60] K. He, J. Sun, Convolutional neural networks at constrained time cost, Proc. IEEE Comput. Soc. Conf. Comput. Vis. Pattern Recognit, 2015, pp. 5353–5360.

[61] Z. Wu, C. Shen, A. van den Hengel, Wider or deeper: revisiting the ResNet model for visual recognition, Pattern Recogn. 90 (2019) 119–133, https://doi.org/10.1109/ CVPR.2016.499.

[62] S.J. Pan, Q. Yang, A survey on transfer learning, IEEE Trans. Knowl. Data Eng. 22 (2009) 1345–1359.

[63] M.E. Taylor, P. Stone, Transfer learning for reinforcement learning domains: a survey, J. Mach. Learn. Res. 10 (2009) 1633–1685.

[64] H.-W. Ng, V.D. Nguyen, V. Vonikakis, S. Winkler, Deep learning for emotion recognition on small datasets using transfer learning, Proc. 2015 ACM Int. Conf. Multimodal Interact. - ICMI ‘15, Seattle, USA, 2015, pp. 443–449.

[65] J. Yosinki, J. Clune, Y. Bengio, H. Lipson, How transferable are features in deep neural networks? Proc. 27th Int. Conf. Neural Inf. Process. Syst, MIT Press, Cambridge, MA, USA ©2014, Montreal, Canada, 2014, pp. 3320–3328.

[66] F. Chollet, Keras documentation, Keras.Io, 2015, https://keras.io/%0Ahttps:// keras.io.

[67] M. Sokolova, N. Japkowicz, S. Szpakowicz, Beyond accuracy, f-score and ROC: a family of discriminant measures for performance evaluation, Proc. Australas. Jt. Conf. Artif. Intell., Hobart, Australia, 2006, pp. 1015–1021.

[68] D.M.W.D. Powers, Evaluation: from precision, recall and f-factor to ROC, informedness, markedness & correlation, J. Mach. Learn. Technol. 2 (2011) 37–63 (doi:10.1.1.214.9232).

[69] A. Tharwat, Classification assessment methods, Appl. Comput. Informatics 8 (2018) (In press).

[70] H. He, Y. Ma, Imbalanced Learning: Foundations, Algorithms, and Applications, 1s ed., John Wiley & Sons, Ltd, 2013.

[71] M. Sokolova, G. Lapalme, A systematic analysis of performance measures for clas sification tasks, Inf. Process. Manag. 45 (2009) 427–437.

[72] D. Martens, J. Vanthienen, W. Verbeke, B. Baesens, Performance of classification models from a user perspective, Decis. Support. Syst. 51 (2011) 782–793.

[73] S. Moro, P. Cortez, P. Rita, A data-driven approach to predict the success of bank telemarketing, Decis. Support. Syst. 62 (2014) 22–31.

[74] K. Sarkar, B. Hampiholi, K. Varanasi, D. Stricker, Learning 3D shapes as multi

layered height-maps using 2D convolutional networks, Lect. Notes Comput. Sci, 2018, pp. 74–89.

![](/api/attachments/QJWMMFAY/fulltext/images/5b0cfb127a21fdc023f9ad32a7273de02b9b0eecedaa631fb40346fc82fb0b6c.jpg)

Neha Chaudhuri is a doctoral candidate of Management Information Systems at the Indian Institute of Management Calcutta. She has done her Bachelor of Technology in Computer Science and Engineering and then Masters of Technology in Information Technology from Indian Institute of Engineering Science and Technology, Shibpur (formerly, Bengal Engineering and Science University, Shibpur). Her research interests are in data analytics, information privacy, misinformation and VLSI design. Her works have appeared in the proceedings of the IEEE as well as proceedings of conferences like HICSS and WeB (pre ICIS).

![](/api/attachments/QJWMMFAY/fulltext/images/cb2ca8b0be2cb8a3d63e4c8dffbd5a10e8992f446fe4627d79d6e92880f64798.jpg)

Indranil Bose is Professor of Management Information Systems at the Indian Institute of Management, Calcutta. He acts as Coordinator of IIMC Case Research Center. He holds a B. Tech. from the Indian Institute of Technology, MS from the University of Iowa, MS and Ph.D. from Purdue University. His research interests are in business analytics, telecommunications, information security, and online communities. His publications have appeared in MIS Quarterly, Communications of the ACM, Communications of AIS, Computers and Operations Research, Decision Support Systems, Ergonomics, European Journal of Operational Research, Information & Management, International Journal of Production Economics, Journal of Organizational Computing and Electronic Commerce.

Journal of the American Society for Information Science and Technology, Operations Research Letters etc, He serves as Senior Editor of Decision Support Systems and Pacific Asia Journal of AIS, as Associate Editor of Communications of AIS, Information & Management, Information Technology & Management and the Journal of the AIS.
