---
otero_id: 9174
otero_key: "QNYKVCM7"
title: "An intelligent mobile based decision support system for retinal disease diagnosis"
authors: "A. Bourouis; M. Feham; M.A. Hossain; L. Zhang"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.01.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An intelligent mobile based decision support system for retinal disease diagnosis

A. Bourouis <sup>a</sup>, M. Feham <sup>a</sup>, M.A. Hossain <sup>b</sup>, L. Zhang <sup>b,</sup>⁎

<sup>a</sup> STIC Laboratory, Abou-bekr Belkaid University of Tlemcen, Algeria

<sup>b</sup> Computational Intelligence Group, Department of Computer Science and Digital Technology, Faculty of Engineering and Environment, University of Northumbria at Newcastle, UK

## a r t i c l e i n f o

Article history: Received 4 February 2013 Received in revised form 24 November 2013 Accepted 8 January 2014 Available online 20 January 2014

Keywords: Retinal disease Neural Networks Mobile applications for Android environments Retinal image analysis Rooted method

## a b s t r a c t

Diabetes and Cataract are the key causes of retinal blindness for millions of people. Current detection of diabetes and Cataract from retinal images using Fundus camera is expensive and inconvenient since such detection is not portable and requires specialists to perform an operation. This paper presents an innovative development of a low cost Smartphone based intelligent system integrated with microscopic lens that allows patients in remote and isolated areas for regular eye examinations and disease diagnosis. This mobile diagnosis system uses an arti<sup>fi</sup>cial Neural Network algorithm to analyze the retinal images captured by the microscopic lens to identify retinal disease conditions. The algorithm is first of all trained with infected and normal retinal images using a personal computer and then further developed into a mobile-based diagnosis application for Android environments. The application is optimized by using the rooted method in order to increase battery lifetime and processing capacity. A duty cycle method is also proposed to greatly improve the energy ef<sup>fi</sup>ciency of this retinal scan and diagnosis system in Smartphone environments. The proposed mobile-based system is tested and veri<sup>fi</sup>ed using two well-known medical ophthalmology databases to demonstrate its merits and capabilities. The evaluation results indicate that the system shows competitive retinal disease detection accuracy rates (N87%). It also offers early detection of retinal diseases and shows great potential to be further developed to identify skin cancer.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

The increasing popularity of Smartphones with sensing capability is giving researchers the opportunity to design and develop mobile applications. Particularly, mobile technologies are creating new values in healthcare domains. For instance, handheld devices and Smartphones have been regarded as promising platforms to provide affordable solutions and scalable approaches to widespread care, and ultimately better patient health outcomes due to their mobility. With the new generation of mobile operating systems, e.g. Windows Phone 7, iOS, and Android, there have been substantial increasing developments and adoptions of mobile applications [1]. To date, more than 10,000 medical and healthcare applications are dedicated to Smartphones and hundreds of other handheld devices [2]. Since mobile technology has enabled the practice of care anywhere possible in medical <sup>fi</sup>elds, such as for patient monitoring, it is becoming a reality that it is no longer the case that a doctor must be physically present to monitor patients, or obtain their biological data.

However, comparing with other mobile-based intelligent health monitoring systems, there are limited developments focusing on retinal disease related detection. Moreover, research showed that diabetes and Cataract are the key retinal diseases that cause retinal blindness. Especially, the number of diabetic patients aged 64+ will be over 82 million in developing countries by 2022 and nearly 40 million people mostly living in remote areas in developed countries will become blind due to Cataract (http://www.who.int/blindness/en/). Fig. 1 also shows some examples of healthy and infected retinal images respectively for diabetes and Cataract conditions.

Therefore, this paper is motivated by the above medical research and focuses on the development of an intelligent mobile-based automatic diagnosis facility to identify retinal diseases. It employs a feed forward Neural Network (NN) to analyze patients' retinal images and perform disease diagnosis. The Neural Network is initially trained with healthy and infected retinal images on a personal computer and then embedded in an Android environment. An energy ef-<sup>fi</sup>cient algorithm based on the duty cycle technique is also proposed to optimize the power consumption of this retinal disease diagnosis system in Smartphone environments. After retinal images are captured by the microscopic lens attached with the Smartphone, a series of Android's image processing APIs are also employed to analyze the raw images. The selection of an optimal number of hidden neurons for the Neural Network implementation is also carried out. We also present experiments using 260 retinal images extracted from two well-known medical retinal image databases (DIARETDB0 and STARE databases) to evaluate the system's ef<sup>fi</sup>ciency. The DIARETDB0 image database is especially built to support the development of benchmark diabetic retinopathy detection methods. The STARE database includes healthy and infectious retinal images with various medical causes e.g. diabetes, Cataract and Drusen. In our application, we especially focus on the detection of retinal problems caused solely by diabetes and Cataract. The algorithm is implemented, tested and veri<sup>fi</sup>ed for both rooted and unrooted operating environments of the Smartphone to demonstrate its merits and capabilities for optimal solutions.

![](/api/attachments/QNYKVCM7/fulltext/images/1ee1d16cc30bf01c5791a1588c7cfcf84fbf7e5ac12f9ba04f2d8ef930b4c2a1.jpg)  
Fig. 1. Healthy and infected retinal images that cause blindness.

Finally, the proposed intelligent mobile-based scheme allows Smartphone users to get access to low cost regular eye examination and disease diagnosis without the need of any specialists at anytime and anywhere.

The paper is organized in the following way. Section 2 discusses related work. The mobile-based retinal disease diagnosis system is presented in Section 3 including discussions of the methodology and the implementation of the core functionality of the system. Details of the evaluation of the system are presented in Section 4. Finally, Section 5 summarizes and concludes the contribution of our research.

## 2. Related work

In this section, we discuss related decision support systems for healthcare and medical computer-aided diagnosis based on PCs and Smartphones. Since optimization plays a crucial role for mobile-based applications, various optimization strategies are also explored and discussed.

## 2.1. Desktop-based diagnosis applications

Several computing techniques have been proposed in the literature for the detection of eye abnormalities and retinal diseases. Wang et al. [3] applied a Bayesian classi<sup>fi</sup>er based on color features to detect eye diseases. They used a complex algorithm that combined a brightness adjustment method with both statistical classi<sup>fi</sup>cation and a localwindow-based veri<sup>fi</sup>cation strategy. Their system achieved reasonable accuracy rates but it needed a high processing capacity. Region growing techniques on gray level images were described in [4] for the diagnosis of eye abnormalities. The idea was based on a supervised method for blood vessel detection in retinal images. It used a Neural Network scheme for pixel classi<sup>fi</sup>cation and computed a 7-D vector composed of gray-level and moment invariants-based features for pixel representation. As compared with other existing solutions in literature, this method was simple and easy to implement but it required comparatively more complex tools and resources.

Data mining techniques and decision support systems have been also employed for the detection of eye abnormality. For example, Jegelevicius and Lukosevicius [5] used a decision support algorithm for the differential diagnosis of intraocular tumors using parameters from eye images. Dua et al. [6] have also proposed a retinal blood vessel monitoring algorithm which was able to provide information on retinal vessel that can be calibrated to normal expected blood vessel diameters. It was also used to detect microvascular anomalies to aid the early detection of diabetic retinopathy. Another integrated analyzer has been presented by Cree et al. [7]. The system described, quanti<sup>fi</sup>ed and monitored the presence of microaneurysms in retinal <sup>fl</sup>uorescein angiograms. Moreover, a multi-layer Neural Network for the detection of lesions in gray scale retinal images was discussed in [8]. However, this Neural Network based system had not been properly evaluated using a larger dimension of input vectors. Abnormality classi<sup>fi</sup>cations using perception learning have also been proposed in [9]. This work also described the use of a multi-layer Neural Network to distinguish eye diseases. The analysis was based on the selection of an optimal number of hidden neurons and it explored principal component analysis for feature optimization.

## 2.2. Mobile-based diagnosis systems

The development of intelligent mobile-based healthcare systems (i.e. mHealth) has become a rising research topic recently, since mHealth applications with the advancements in mobile technologies are able to provide ef<sup>fi</sup>cient solutions for health monitoring. Especially, some systems also included pervasive wearable monitoring devices [10]. For example, a mobile health monitoring system including a ring sensor for blood oxygen saturation level monitoring was described in [11,12]. A Smartphone based health data acquisition system was also discussed in [13]. Their work generally proposed a low cost mobilebased solution and used a mobile device's Bluetooth to transfer patients' physiological data collected using medical devices to a temporary storage. Remote heart monitoring for elderly people using cellular wireless networks is discussed in [14]. Their system monitored elderly people's health condition through a network of wireless sensors and used this information to recommend personalized treatment plans to doctors. Another approach for ECG data compression for a mobile tele-cardiology model is described in [15]. This system employed a signi<sup>fi</sup>cant compression ratio and showed reduction in transmission time over GSM network.

Moreover, there has been substantial development of mobile technologies on a number of medical fronts. For example, the development of modern Smartphone hardware technologies has provided impetus on mobile adaptation to many health services. For instance, Zhu et al. [16] proposed a prototype system that used a mobile device with a built-in camera, wireless network connectivity and intelligent image analysis algorithms to estimate the calorie intake.

![](/api/attachments/QNYKVCM7/fulltext/images/3c25a8799e49da2704b4e890db2b26c126fc47e46de86d52c1af81a65ab01b7b.jpg)  
Fig. 2. The system architecture.

Buttussi and Chittaro [17] discussed a mobile-based personal trainer wearable system that generated physical <sup>fi</sup>tness exercise plans. Mobile-based cloud computing for mHealth services was also presented in [18,19]. Maass and Varshney [20] designed a ubiquitous information system for healthcare applications. They employed an Android mobile phone as the alarm gateway in their proposed implementation model. Overall, the discussions of the above related work indicate that the use of mobile technologies for teledermatology, telepathology and remote monitoring of vital biosignals of patients has been widely employed and attracted further attention [21,22].

## 2.3. System optimization

There were also extensive intelligent decision-making applications employing classi<sup>fi</sup>cation algorithms at the server or cloud side. However, the majority of such contributions have not considered optimized strategies for the application of AI algorithms on the client side (e.g. Smartphones). Since the main goals of optimizations are to achieve high recognition accuracy rates with low processing complexity (e.g. execution time and energy consumption), there are three essential factors in<sup>fl</sup>uential to optimization methods including the choices of hardware, development platforms and software architectures. For example, Könönen et al. [23] used a Support Vector Machine (SVM) in an activity recognition system. The training of this SVM classi<sup>fi</sup>er was carried out using a personal computer. The trained model was then uploaded to Nokia N95. The operating system of this mobile device was Symbian OS written in C++. However, the prede<sup>fi</sup>ned LIBSVM library integrated in Symbian was originally written in C with high complexity. It also contained algorithms designed for a wide range of applications, the majority of which were not needed for their application. Also, the computational and memory requirements of their SVM classi<sup>fi</sup>er were quite high. The hardware choices and the employed development strategy in their system showed limitations to optimization. Miluzzo et al. [24] applied Gaussian Mixture Models (GMMs) and SVMs to Nokia N95 and Apple iPhone to automatically detect sensing contexts. Their sensing and classi<sup>fi</sup>cation algorithms running on Smartphones consumed a considerable amount of battery power since the system used a JME based Symbian which did not provide APIs for power cycle and resource management routines. Fábián et al. [25] described a mobile-based Neural Network system that recognized and recorded users' motions. Their system employed a complex architecture incorporating six multiplayer Neural Networks, one for each activity. Many optimization issues related to power consumption and computational time of the system have not been considered yet.

![](/api/attachments/QNYKVCM7/fulltext/images/3ff907086960448828879eaf45181bc987d7d7735e67fd128dfd0fdf326a7106.jpg)  
Fig. 3. The duty cycle and energy ef<sup>fi</sup>cient principle

In this research, we employ a modi<sup>fi</sup>ed Neural Network for the rooted method application of a Smartphone for retinal disease diagnosis. The training of the Neural Network is performed in the developed Java framework on a personal computer. The parameters of the networks (the weight matrices and the bias vectors representing the classi<sup>fi</sup>cation knowledge) with the same network topology are then applied to a mobile-based diagnosis system as a mobile development library. In this way, we effectively maintain the reliability and ef<sup>fi</sup>ciency of this mobile-based Neural Network diagnosis system. This research has the following distinctive aspects: (1) capturing high resolution retinal color images using a microscope attached to the Smartphone; (2) using arti<sup>fi</sup>cial Neural Networks for local abnormal/normal retinal RGB image classi<sup>fi</sup>cation, i.e. distinguishing between normal and disease related retinal images; (3) optimizing and exporting this Neural Networkbased retinal disease detection component to an Android-based mobile platform and performing real-time early detection of retinal diseases; and (4) employing images from two medical retinal image databases to evaluate the ef<sup>fi</sup>ciency of this mobile-based intelligent solution.

## 3. The mobile-based intelligent retinal disease diagnosis system

In this research, our mobile-based intelligent retinal disease diagnosis system was designed to provide a fully functional feature rich software application with a user friendly graphical user interface to

![](/api/attachments/QNYKVCM7/fulltext/images/c0eb9aa14217440170b7f519f101aa614657f6b20cf5f804ffdbd608f0f9160d.jpg)

Fig. 4. The Android phone with an external microscope lens.  
![](/api/attachments/QNYKVCM7/fulltext/images/4eb23580fbe14df5bf484fb40a48014d028d0022a5dd9ee7b53b3828b317e215.jpg)  
Fig. 5. A captured image of the retina on a Galaxy S device.

analyze retinal images and perform diagnosis. The employed Neural Network based approach is able to run on both desktop computers and Android-based mobile devices for image classi<sup>fi</sup>cation of abnormal/normal retina. In order to achieve a real-time ef<sup>fi</sup>cient solution, <sup>fi</sup>rst of all, the feed forward Neural Network algorithm is trained and tested on a desktop computer using retinal datasets with healthy and infectious states. Then the trained Neural Network is installed in a mobile device with an Android operation system (OS). In the test stage, a microscopic lens is also employed and attached with this Android Smartphone, which is used to collect users' retinal images and perform diagnosis. The advantage of using such a microscopic lens is that it allows the system to capture high resolution retinal images and thus provide better performance for disease diagnosis. Various optimization techniques have also been taken into account in this research in order to provide an ef<sup>fi</sup>cient mobile-based intelligent solution to perform real-time diagnosis. Fig. 2 shows the system architecture.

![](/api/attachments/QNYKVCM7/fulltext/images/3289b7d34a09514f9587042a21d0a3364564ea2f005d26231f4f7c70ff33c476.jpg)  
Fig. 7. The schematic diagram for the training of the Neural Network.

Overall, in order to make the system execute ef<sup>fi</sup>ciently on a mobile device with limited processing capability, we use two separate platforms for the training and testing of the system. i.e. we use a normal personal computer to conduct the training of the Neural Network. The trained Neural Network is then exported to mobile devices. The Smartphone-based Neural Network diagnosis system is subsequently used to perform diagnosis at the test stage. In this way, the computational intensive training of the system does not need to be conducted on mobile devices. Especially, the training is also not required to perform each time for each diagnosis. Thus the trained Neural Network has the capability to analyze test images in a few seconds in the testing stage to perform ef<sup>fi</sup>cient diagnosis. Therefore, it is capable of performing rapid assessment of a large number of test cases.

![](/api/attachments/QNYKVCM7/fulltext/images/8d955ad31effd7969d409f021533562ae27f080cedbd78040860cd24cb5941c6.jpg)  
Fig. 6. The chain of the retinal image processing technique.

![](/api/attachments/QNYKVCM7/fulltext/images/987e0180acbc44f4a7c548da47703e75d56b43ce500038545456f664769b9f26.jpg)  
Fig. 8. The feed forward Neural Network topology.

Moreover, Google's Android operation system is chosen for this application since it is widely used and there are both Linux and Windows versions available to allow <sup>fl</sup>exible portability. Also, the Android SDK provides all the core plumbing features such as device drivers, memory and process management, network stack, and security to allow <sup>fl</sup>exible, reliable and portable data storage and processing [26]. In recent years, computing resources in the actual Smartphones are also dramatically improved in comparison to the earlier mobile device generations. Devices with the Android OS have computing features typically about

![](/api/attachments/QNYKVCM7/fulltext/images/325c2ad805b499d69eced1846c50b67c542244e2c219c689a88a19b599d83e32.jpg)  
Fig. 9. The core functionality of the mobile-based retinal disease diagnosis system.

1.2 GHz CPU and 512 MB operative memory. Such con<sup>fi</sup>gurations are able to allow for the execution of more complicated computing tasks than just data storage and transmission. Hence, such Android Smartphones provide additional bene<sup>fi</sup>ts to developers.

Recent technology and miniaturization have also accelerated the convergence between Smartphones and powerful computers facilitating the development of the phone technology. Smartphone computation capabilities are growing while integrating a suite of sensors. Android also provides a more complete set of APIs to allow access to the low level components of the Smartphone operating system while taking advantage of more powerful hardware (CPU and RAM). For example, we can turn the sensors off, tier inactive activities, and make our application possess the highest priorities using the duty cycle and rooted method in order to increase the battery lifetime and the computational capacity of the phone when running our Android application. We also use Android resource management APIs to apply scheduled sleep functions to both sensors and activities while they are not active to save energy.

Especially, since Smartphones have limitations in maximum CPU performance, with the rooted method, we can easily exceed these limitations and use the power of the phone processor to conduct intensive disease diagnosis. To compensate the battery use of the processor, we propose an automatic duty cycle algorithm to extend battery life. This duty cycle algorithm has been initially employed in the wireless sensor networks <sup>fi</sup>eld in order to achieve optimal network performance in all traf<sup>fi</sup>c conditions. The main idea of the algorithm is that it intends to balance successful data delivery and delay constraints of diverse applications to minimize power consumption without human intervention. Mapping this duty cycle optimization technique for processing in mobiles is relatively challenging as it has never been used in mobilebased application environments. We use the duty cycle technique in the following way in our application.

First of all, we force some sensors to switch to the IDLE mode and make them in use just when needed. We also integrate some camera control options with the application framework and only activate those activities related to retinal image capturing with all other unrelated functions disabled automatically. Since screen brightness is considered as the main energy consumer, once the application is launched, the duty cycle algorithm is enabled in order to reduce the screen frame rate and lower its brightness. It also changes the background color brightness level of both of the diagnosis system and the application browser so that the application consumes less battery and in turn serves as a green solution [34]. The duty cycle algorithm used by our retinal image analysis application is performed as the key technique to lower battery usage and in turn increase the resource performance of the CPU and RAM. Our adaptive duty cycling scheme is also different from the one used in sensor networks and driven by the following three principles: (i) disabling unused internal sensors and activities

![](/api/attachments/QNYKVCM7/fulltext/images/c66620a5b8c4e02aa9f89c40e4fd56fdf293c7973029c26ad5a55703f2fecf4d.jpg)

Table 1  
Example test data extracted from the DIARETDB0 database.

<table><tr><td>Example test images</td><td>Normal/infected</td><td>If infected, any description about the condition (e.g. caused by diabetes or any other diseases if applicable)</td></tr><tr><td></td><td>Infected</td><td>Diabetic retinopathy</td></tr><tr><td></td><td>Normal</td><td>N/A</td></tr><tr><td></td><td>Normal</td><td>N/A</td></tr><tr><td></td><td>Normal</td><td>N/A</td></tr><tr><td></td><td>Infected</td><td>Diabetic retinopathy</td></tr></table>

(ii) on-demand services enabled based on users' needs and (iii) optimizing the current consumption sources such as the screen brightness adjusti<sup>fi</sup>cation and employing vibration options (see Fig. 3). Some example pseudo code for the duty cycle technique is provided in the following.

Rooted, unrooted and relative speed of the application.

<table><tr><td>Context</td><td>Unrooted</td><td>Rooted</td><td>Ratio unrooted/rooted applications</td></tr><tr><td>Run time (RT) in sec</td><td>32</td><td>11</td><td>2.91</td></tr><tr><td>Response time (RPT) in sec</td><td>2.4</td><td>0.66</td><td>3.64</td></tr><tr><td>Relative speed (RT/RPT)</td><td>13.33</td><td>16.67</td><td>N/A</td></tr></table>

Algorithm 1. Pseudo-code of part of the duty cycle technique for iTEST.

The mobile device used in this work is a Galaxy S GT-I9000, which is provided with an unmodi<sup>fi</sup>ed version of Android OS 2.3.4. The application was also tested with the rooted version 2.3.4. Generally, a rooted Android device has full control of the device's software and hardware which makes all features and functions easily accessible. The rooted method is also employed in our algorithm implementation so that the mobilebased diagnosis system is able to have access to all memory and processor resources. For example, the rooted method employed in the coding of the system allows us to manage Android Activity and control memory of the mobile device. For instance, if there is a newly arrived activity (e.g. an incoming call) when our application is active and performing diagnosis (the current running activity with the highest priority), our system is able to change the state of the activity and turn our application into pause with the reservation of its current processing status. Therefore, with the rooted method, we are able to allow the user to deal with a newly arrived phone activity (e.g. allowing the incoming call to overtake the current activity) and make the diagnosis system active again when the new activity (e.g. the phone call activity) <sup>fi</sup>nishes and becomes inactive.

In our system, the Android handset employed has also been attached with an external separate microscope, which allows a microscopic retinal image to be captured directly using our application (see Fig. 4). A commercial phone microscopic lens ×60/100 is employed in this research attached with the mobile device to help to capture high quality retinal images. The Android Application Programming Interface (API) also allows easy access to image processing functions and control of the integrated camera with the external microscopic device. For example, the android.graphics API provides low level graphics classes (e.g. Bitmap, BitmapFactory, Camera, Canvas, etc) and tools (such as canvases, color <sup>fi</sup>lters and image formatting) for image drawing handling [27]. Especially, such a function enables the extraction of high quality retinal images and provides a robust and scalable approach to computeraided automatic diagnosis. Fig. 5 shows an example retinal image captured by this microscopic lens.

As mentioned above, we employ a multi-layer Neural Network in this research to perform diagnosis. Neural Networks are generally well-known for classi<sup>fi</sup>cation tasks and pattern recognition. Multilayer perceptron (MLP) based on feed forward with Backpropagation is also one of the most classic supervised Neural Network algorithms [28]. It is chosen due to its promising performances and robustness of the modeling of the problem domain.

As discussed earlier, in order to optimize the consumption of the processor and battery resources, the complexity of the system has to be reduced as much as possible. This motivated us to employ an optimized Neural Network trained using a personal computer and subsequently exported to mobile devices. We <sup>fi</sup>rst of all develop a Java framework using a powerful high performance computer to perform the training of the Neural Network. We employ 40 abnormal and 20 healthy retinal images for the training of the Neural Network. These training images are borrowed from a medical ophthalmology database, DIARETDB0 [29]. Then the trained weights of the network are saved in an individual <sup>fi</sup>le. We also develop a library called nncig.jar which will be called and loaded in our Android-based application. Overall, the framework employed in the training stage has three functions: normalization, training and storage (see Fig. 2). First of all, the normalization function normalizes a retinal image into the size of 32×32 pixels and transforms it to a onedimensional vector to store all pixel information. Then the training algorithm of the Neural Networks uses these normalized images for training. Subsequently, the trained Neural Network is stored as a Java <sup>fi</sup>le adapted to our nncig library. Once the system is trained, it has the capability to analyze a test image and perform real-time disease diagnosis.

Furthermore, in comparison with the work of Gardner et al. [8], which used gray retinal images for a desktop-based diagnosis system, this research uses color images as inputs for a mobile-based application. Also in this research, the colorful images are presented as onedimensional vectors containing red, green and blue pixel values. The input of the Neural Network is thus represented by n dimensions of a colorful retinal image (n = imageHeight ∗ imageWidth ∗ 3). For instance, as mentioned above, each colorful retinal image is represented by 32 by 32 pixels. For each pixel, the application uses red, green and blue coordinates to represent the color of that pixel. Therefore, the input layer of the Neural Network has 3072 (32 ∗ 32 ∗ 3) input nodes.

We also would like to address that there is no difference in the proposed algorithm as compared to the algorithm demonstrated in [8]. However, it is worth mentioning that we used color retinal images with different dimensions and in different operating system environments. Therefore, the main challenges were the adoption of the algorithm for color image processing that includes classi<sup>fi</sup>cation, automatic dimension setting, design and development within optimal mobile operating environments. Based on the review of various related works in literature and a full investigation of all image classi<sup>fi</sup>cation methods employing Neural Networks [33], our proposed retinal disease diagnosis algorithm discussed above uses an innovative concept of image segmentation and transformation based on one-dimensional RGB vectors, which contain all image information and are considered as input vectors of the Neural Network based diagnosis system (see Fig. 6). In comparison with related work [8,24,25], such a segmentation technique is highly compatible with all APIs and development tools in both desktop and mobile environments. In contrast, authors of [8] applied a segmentation method of many grids to the retinal images, and then they used a binarization technique for all gray images.

Moreover, in order to <sup>fi</sup>nd the best Neural Network topology, we have also employed different settings of the hidden layer with neurons ranging from 4 to 20. There are many recommendations for the design of the Neural Network topologies in the arti<sup>fi</sup>cial intelligence and machine learning <sup>fi</sup>elds [9,28,30]. The trial and error method is one of the most conventional approaches for the Neural Network construction and development suggested in the <sup>fi</sup>eld [9,28,30] and has been applied to this research and other healthcare and AI applications as well, e.g. the work Gardner et al. [8]. After several trial and error experiments, 12 neurons in the hidden layer are selected for this feed forward Neural Network since it leads to the most optimal results compared with other neuron settings in the hidden layer.

Finally, the following speci<sup>fi</sup>c network topology suitable to our proposed application has been identi<sup>fi</sup>ed: the input layer with 3072 nodes, one hidden layer with 12 neurons and the output layer with two nodes respectively representing normal and abnormal classes for retinal conditions. The sigmoid function is also used to calculate the <sup>fi</sup>nal output of the Neural Network. Fig. 7 shows the data <sup>fl</sup>ow of the Neural Network training procedure. Fig. 8 shows the network topology. This intelligent mobile-based retinal disease diagnosis system is developed using the Android SDK and the Netbeans IDE. The core functions of the system are also illustrated in Fig. 9.

As indicated above, the training step is computationally intensive as the learning is linked with the training of a large number of images. Therefore it was performed in a powerful computing environment in order to achieve competitive learning performances. However, this is just one-off and the trained algorithm does not need to be retrained as it possesses the learning capability to capture all unexpected changes in retinal images caused by Cataract or diabetes. This offers a great opportunity to enable the recognition process to perform faster with minimum power consumptions. It also does not affect the operational deployment of the system in a real setting in any way.

## 4. Experiments and results

This research is designed and developed to detect abnormal retina from normal cases. Since eye abnormality could be caused by many factors, e.g. Cataract or diabetes, we considered both Cataract and diabetic related eye abnormality detection in this application. We employ two medical image databases, DIARETDB0 [29] and STARE [31,32], for the evaluation of this intelligent mobile-based diagnosis system. The DIARETDB0 image database is especially built to support the development of benchmark diabetic retinopathy detection methods. The

![](/api/attachments/QNYKVCM7/fulltext/images/1717bf99c5c7b06829579235116adfeebce25eac2a2174e85cf4f67ea1e709ce.jpg)  
Fig. 10. Energy consumption of the development with and without root, with Y axis indicating the number of tests conducted and X axis showing the battery life in hours.

STARE database includes healthy and diseased retinal images with various medical causes e.g. diabetes, Cataract and Drusen. In this application, we especially focus on the detection of eye abnormal conditions solely caused by Cataract and diabetes.

For the training of the Neural Network conducted earlier, we used 20 normal retinal images and 40 abnormal cases with 32 × 32 resolutions extracted from an ophthalmology database, DIARETDB0 [29]. After the total error rate at the training stage of the Neural Network was reduced to 0.0099, the implemented Android-based Neural Network application is stored in an APK <sup>fi</sup>le. Then the trained Neural Network algorithm is exported to the mobile device and performs initial testing, i.e. the classi<sup>fi</sup>cation of 60 test images of healthy (20) and abnormal retina (40) cases. These test images are also extracted from the same ophthalmology database [29]. Some example test data are shown in Table 1.

Table 3  
Example test data extracted from the STARE database.

<table><tr><td>Example test images</td><td>Normal/ Infected</td><td>If infected, any description about the condition (e.g. caused by diabetes or any other diseases if applicable)</td></tr><tr><td></td><td>Normal</td><td>Drusen early stage</td></tr><tr><td></td><td>Infected</td><td>Cataract early stage</td></tr><tr><td></td><td>Normal</td><td>N/A</td></tr><tr><td></td><td>Infected</td><td>Diabetes retinopathy</td></tr><tr><td></td><td>Normal</td><td>N/A</td></tr></table>

As discussed earlier, this mobile-based diagnosis system is trained using images with $3 2 \times 3 2$ resolutions. Any test images captured using the microscopic lens attached with the Smartphone have been converted to both $3 2 \times 3 2$ and $4 8 0 \times 3 6 0$ during the testing. Since the system is trained using images with 32 × 32 resolutions, with the <sup>fi</sup>rst image normalization method (i.e. conversion to 32 × 32 resolutions), the system has achieved an accuracy rate of 98%. The second application with the converted images in $4 8 0 \times 3 6 0$ resolutions achieved a slightly lower accuracy rate, i.e. 92.80%. The decrease in the performance has been caused by the fact that such images have just taken a slide window from the raw images for analysis and disease diagnosis rather than employing a full view of a test retinal. Our experiments also re<sup>fl</sup>ect the work of Gardner et al. [8] and indicate that the images with 32 × 32 resolutions are able to capture more global views of retinal conditions than the cropping (taking a slide window) from the original images with 480 × 360 resolutions. It also advises us to employ images with 32 × 32 resolutions for further evaluation.

Moreover, the application's loading and responding speed in both rooted and unrooted Android Smartphones is also evaluated. It is observed that with the rooted method, the application's run time is 2.91 times faster than the unrooted method. In contrast, for the response time, the rooted method is about 3.64 times faster than the unrooted method (see Table 2). It is also noted that for the unrooted application, the response time (RPT) is about 13.33 times faster as compared to the run time (RT). In contrast, it is about 16.67 times faster than the run time in the case of the rooted application.

Moreover, when we compare our developments with the system described in [18], which used cloud Neural Networks based on HTTP transfer protocols, we found that local Neural Networks are much faster than remote cloud-based processing. It is noticed that the execution time of our system is about 120 times faster as compared to the cloud-based Neural Network presented in [18]. It is worth mentioning that both applications have been evaluated in the same environmental settings, e.g. the same network communication conditions with averaged uploading and downloading speed respectively 205 kbps (26 kB/s) and 442 kbps (55 kB/s).

We also explored the energy consumption aspect for the rooted and unrooted applications, since it is a very important issue for mobile healthcare applications. As indicated earlier, the application presented here is optimized by the rooted method in order to increase battery life and processor capacity. Fig. 10 shows the battery life differences between the rooted and unrooted settings. The evaluation indicates that the system is able to work more than 14 h, which can be used to test approximately 50 patients, with WiFi network enabled.

Another experiment has also been conducted with a newly released handset, Galaxy SII, with Android OS v2.3.4. The above trained Neural Networks are used to classify 200 new test images with 130 examples taken from the above ophthalmology database and another 70 sample images extracted from STARE database [31,32]. Overall, the STARE database has 400 raw retinal images collected by medical centers in the US. It is used as a valuable reference for medical eye research. The STARE database includes healthy and infectious retinal images with various medical causes e.g. diabetes, Cataract and Drusen. In our application, we especially focus on the detection of retinal problems caused by diabetes and Cataract. Some example test images from this database are also illustrated in Table 3. For this second experiment, all the test images are converted only to 32 × 32 resolutions in comparison with the <sup>fi</sup>rst experiment using DIARETDB0 database. Among the 200 test images, there are 160 images representing infectious retina and 40 for healthy cases. The evaluation results of this second experiment are also presented in Table 4.

Testing results for the second experiment with 200 retinal images.

<table><tr><td>Retinal images (32 × 32)</td><td>Detection accuracy rates</td></tr><tr><td>Abnormal images</td><td>91.87%</td></tr><tr><td>Normal images</td><td>87.5%</td></tr></table>

![](/api/attachments/QNYKVCM7/fulltext/images/2df088f9343e7bd8d6efa2c7653341a260801f974496b7e0ecb5932c2ee9ba1c.jpg)  
Fig. 11. Power consumption before and after the root-duty cycle algorithm.

The above evaluation results shown in Table 4 indicate the ef<sup>fi</sup>ciency of this mobile-based retinal disease diagnosis system. The rooted method employed also shows promising optimal system performance in terms of battery life and processor capacity.

Moreover, the most popular energy pro<sup>fi</sup>ler tools in Android OS are PowerTutor [35] and PowerPro<sup>fi</sup>le. The PowerTutor energy pro<sup>fi</sup>ler tool is an Android app working on Android Smartphones to calculate the power consumptions of CPU, display, GPS, WiFi, and all applications running in the system. In order to monitor energy consumption in real-time, we integrated the PowerTutor energy pro<sup>fi</sup>ler function with our application.

After installing the PowerTutor application in both unrooted and rooted (with duty cycle enabled) Android Galaxy S2 devices, we tested each phone using retina scan applications and obtained the following performance details shown in Fig. 11. The y-axis of Fig. 11 indicates the power consumption of each application in the test environments for both root and unroot settings. We tested the retinal image scan application through continuous execution. On average, the application consumes about 13 mW (milliWatt) before applying the root duty cycle algorithm and 8 mW after using the proposed duty cycle algorithm. The differences of the result are mainly caused by the different times required for the running of an application, i.e. more time needed to run an application may subsequently increase the power consumption. Fig. 11 indicates that the rooted method with the proposed duty cycle algorithm optimizes the power consumption and improves the battery life greatly when using our retinal application. We observe that from the screen consumption perspective the rooted method with the duty cycle algorithm consumes approximately only one third of the power in comparison to that required by the normal usage without root and the proposed algorithm. The CPU consumption is also decreased using our proposed algorithm since many sensors and inactive applications are disabled during the retinal disease diagnosis process. Overall, our approach using the root and duty cycle method improves the energy ef<sup>fi</sup>ciency of the retinal scan and diagnosis system in Smartphone environments. The testing results shown in Fig. 11 thus indicate that our mobile-based diagnosis system with the proposed energy ef<sup>fi</sup>cient algorithm based on the duty cycle technique could be considered as a green solution.

## 5. Conclusion

This paper has presented an intelligent mobile-based retinal disease detection scheme using commercially available Smartphones with the integration of an external microscope. The proposed scheme was especially developed for the Android operating platform using a feed forward Neural Network. It was then evaluated and veri<sup>fi</sup>ed through two sets of experiments (using benchmark datasets) to demonstrate the merits and capabilities of the chosen approach. It is noted that the implemented Smartphone based system offers fast retinal disease detection (the shortest response time: 0.66 s for a single test) with very high accuracy rates and also requires very little energy consumption through the rooted method. The proposed energy ef<sup>fi</sup>cient algorithm based on the duty cycle technique also signi<sup>fi</sup>cantly optimizes the power consumption of Smartphones. The application is also very easy to be operated by any mobile user and could be used remotely as an ef-<sup>fi</sup>cient low cost mobile solution for health monitoring at anytime. These features are very notable as compared to the existing Fundus camera based complex and very expensive solutions. In future work, we also aim to further distinguish various causes of retinal abnormalities. Another line of our research has also extended the current system for skin cancer detection. Finally, the system shows great potential in evolving healthcare applications to bene<sup>fi</sup>t wider communities.

## References

[1] International Telecommunication Union, http://www.itu.int2012(Accessed in October 2012).

[2] A.C. Powers, Diabetes mellitus, Harrison's Principles of Internal Medicine, 15th edition, McGraw-Hill, New York, NY, 2001, pp. 2109–2135.

[3] H. Wang, W. Hsu, K.G. Goh, M.L. Lee, An effective approach to detect lesions in color retinal images, Proceedings of IEEE Conference on Computer Vision and, Pattern Recognition, vol. 2, 2000, pp. 181–186.

[4] D. Marin, A. Aquino, M.E. Ġegundez-Arias. I.M. Brayo, A. New, Supervised method for blood vessel segmentation in retinal images by using gray-level and moment invariants-based features, IEEE Transactions on Medical Imaging (Jan. 2011) 146–158.

[5] D. Jegelevicius, A. Lukosevicius, Application of data mining technique for diagnosis of posterior uveal melanoma, Informatica 13 (4) (2002) 455–464

[6] S. Dua, N. Kandiraju, H.W. Thompson, Design and implementation of a unique blood-vessel detection algorithm towards early diagnosis of diabetic retinopathy, Proceedings of International Conference on Information Technology: Coding and Computing, vol. 1, 2005, pp. 26–31.

[7] M.J. Cree, J.A. Olson, K.C. McHardy, J.V. Forrester, P.F. Sharp, Automated microaneurysm detection, Proceedings of International Conference on Image Processing, vol. 3, 1996, pp. 699–702.

[8] G.G. Gardner, D. Keating, T.H. Williamson, A.T. Elliott, Automatic detection of diabetic retinopathy using an artificial neural network: a screening tool British Journal of Ophthalmology 80 (1996) 940–944

[9] P. Treigys, V. Šaltenis, Neural network as an ophthalmology disease classi<sup>fi</sup>er, Information Technology and Control 36 (4) (2007).

[10] A. Bourouis, M. Feham, A. Bouchachia, Ubiquitous Mobile Health Monitoring System for Elderly (UMHMSE), International Journal of Computer Science & Information Technology 3 (3) (2011)

[11] Q. Pan, P. Yang, R. Zhang, C. Lin, S. Gong, L. Li, J. Yan, G. Ning, A mobile health system design for home and community use, Biomedical and Health Informatics (BHI), IEEE-EMBS International Conference, 2012, pp, 116-119.

[12] H.H. Asada, P. Shaltis, A. Reisner, S. Rhee, R.C. Hutchinson, Mobile monitoring with wearable photoplethysmographic biosensors, IEEE Engineering in Medicine and Biology Magazine 22 (3) (2003) 28–40

[13] M.A. Al-Taee, N.A. Jaradat, D.M.A. Ali, Mobile phone-based health data acquisition system using Bluetooth technology, Applied Electrical Eng. and Computing Technologies (AEECT), 2011, pp. 1–6.

[14] P. Ross, Managing care through air, IEEE Spectrum (2004) 26–31.

[15] R.S.H. Istepanian, A.A. Petrosian, Optimal zonal wavelet-based ECG data compression for a mobile telecardiology system, IEEE Transactions on Information Technology in Biomedicine 4 (3) (2000) 200–211.

[16] F. Zhu, M. Bosh, I. Woo, S. Kim, C.J. Boushey, D.S. Ebert, E.J. Delp, The use of mobile devices in aiding dietary assessment and evaluation, IEEE, Journal of Selected Topics in Signal Processing 4 (2010) 756–766.

[17] F. Buttussi, L. Chittaro, MOPET: a context-aware and user adaptive wearable system for <sup>fi</sup>tness training, Arti<sup>fi</sup>cial Intelligence in Medicine 42 (2008) 153–163.

[18] A. Bourouis, M. Feham, A. Bouchachia, A new architecture of a ubiquitous health monitoring system: a prototype of cloud mobile health monitoring system, International Journal of Computer Science & Information Technology (IJCSIT) 3 (3) (2011).

[19] M.T. Nkosi, F. Mekuria, Cloud computing for enhanced mobile health applications, The Second IEEE International Conference on Cloud Computing Technology and Science (CloudCom), 2010, pp. 629–633.

[20] W. Maass, U. Varshney, Design and evaluation of Ubiquitous Information System and use in healthcare, Decision Support Systems 54 (1) (2012) 597–609.

[21] P. Zhang, Y. Kogure, H. Matsuoka, M. Akutagawa, Y. Kinouchi, A remote patient monitoring system using a Java-enabled 3G mobile phone, Proceedings of IEEE Conference on Engineering in Medicine and Biology Society, 2007, pp. 3713–3716.

[22] National Institutes of Health-National Heart, Lung, and Blood Institute, National High Blood Pressure Education Program Working Group Report on Hypertension in Diabetes, Hypertension 23 (2) (1994) 145–158.

[23] V. Könönen, J. Mäntyjärvi, H. Similä, J. Pärkkä, M. Ermes, Automatic feature selection for context recognition in mobile devices, Pervasive and Mobile Computing 6 (2) (2010) 181–197.

[24] E. Miluzzo, M. Papandrea, N. Lane, H. Lu, A. Campbell, Pocket, bag, hand, etc.—automatically detecting phone context through discovery, Proceedings of ACM International Workshop on Sensing for App Phones (PhoneSense) Collocated With ACM SenSys, Zurich, Switzerland, 2010.

[25] Á. Fábián, N. Győrbíró, G. Hományi, Activity recognition system for mobile phones using the MotionBand device, Proceedings of the 1st International Conference on MOBILE Wireless MiddleWARE, Operating Systems, and Applications, 2008.

[26] P. Ferrill, Pro Android Python With SL4a, 1st edition Apress, 2011. (ISBN-10: 1430235691).

[27] Android APIs, http://developer.android.com/reference/android/graphics/packagesummary.html2013(Assessed in June 2013).

[28] S. Piramuthu, M.J. Shaw, J.A. Gentry, A classi<sup>fi</sup>cation approach using multi-layered neural networks, Decision Support Systems 11 (5) (1994) 509–525.

[29] DIARETDB0 - Standard Diabetic Retinopathy Database, http://www2.it.lut.<sup>fi</sup>/project/ imageret/diaretdb0/index.html2012(Accessed in Dec 2012).

[30] M.T. Jones, Arti<sup>fi</sup>cial Intelligence: A System Approach, Jones and Bartlett Publishers, Sudbury, Massachusetts, 2009.

[31] STructured Analysis of the Retina (STARE), http://www.parl.clemson.edu/\~ahoover/ stare/2013(Assessed in Feb 2013).

[32] A. Hoover, M. Goldbaum, Locating the optic nerve in a retinal image using the fuzzy convergence of the blood vessels, IEEE Transactions on Medical Imaging 22 (8) (2003) 951–958.

[33] M. Egmont-Petersen, D. de Ridder, H. Handels, Image processing with neural networks—a review Pattern Recognition 35 (10) (2002) 2279–2301

[34] M. Conti, D. Diodati, C.M. Pinotti, B. Crispo, Optimal solutions for pairing services on Smartphones: a strategy to minimize energy consumption, IEEE International Conference in Green Computing and Communications (GreenCom), 2012, pp. 269–276.

[35] PowerTutor, http://ziyang.eecs.umich.edu/projects/powertutor/2013(accessed in August 2013).

A. Bourouis received his B.E. and M.E. degrees in Telecommunication from the University of Tlemcen, Algeria, in 2007 and 2009 respectively. He joined the STIC Laboratory of research in 2010 as a PhD researcher. His research work includes the design and develop ment of location-based service (LBS), body sensor networks (BSN) and mobile healthcare applications.

M. Feham received the Dr. Eng. degree in Optical and Microwave Communications from the University of Limoges (France) in 1987, and his PhD in Science from the University of Tlemcen (Algeria) in 1996. Since 1987, he has been an Assistant Professor and Professor of Microwave, Communication Engineering and Telecommunication Networks. He has served on the Scienti<sup>fi</sup>c Council and other committees of the Electronics and Telecommunication Departments of the University of Tlemcen. His research interest now is mobile networks and services.

M.A. Hossain is currently serving as a professor of Computer Science in the Northumbria University, UK. He has extensive research experience in computational intelligence, optimisation, intelligent tutoring, Internet security, computational system biology, and real-time and adaptive control. He received a PhD degree in 1995 from the University of Shef<sup>fi</sup>eld. Previously he led two large EU funded projects: eLINK (5.5 million EURO) and EAST-WEST project (400 K) with various Asian and EU partner countries and was involved in many other funded research council proiects. Prof, Hossain currently is also a project coordinator for the EU funded CLink project (2.5 million Euro) with research collaboration from 14 project partners. Prof. Hossain has published over 175 refereed research articles and 12 books. He received the “IET-F C Williams 1996” award for the journal paper and ‘Best Paper Award’ for his CSBio 2010 conference paper. He is a member of the IEEE.

L. Zhang is currently a Senior Lecturer in Computer Science in Northumbria University, UK and also an Honorary Research Fellow in the University of Birmingham, UK. Dr. Zhang holds expertise in arti<sup>fi</sup>cial intelligence, affective computing and mobile healthcare developments. She gained her PhD and postdoctoral Research Fellow experience from the University of Birmingham. Previously, she was a principal investigator for a Technology Strategy Board funded project in collaboration with an industrial partner and the National Autistic Society. She also worked on several EPSRC and EU funded projects. Currently she is also involved in the EU funded CLink project (2.5 million Euro) with research collaboration from 14 project partners including 6 EU and 8 Asian partners. She is also an editorial board member for the International Journal of Computational Linguistics and Journal of Technology for Education and Learning.
