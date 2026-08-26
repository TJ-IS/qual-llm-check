---
otero_id: 1626
otero_key: "WKJ8NRAE"
title: "A Multimedia Solution to Productivity Gridlock: A Re-Engineered Jewelry Appraisal System at Zale Corporation"
authors: "Julie Newman; Kenneth Kozar"
year: "1994"
journal: "MIS Quarterly"
doi: "10.2307/249608"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
A Multimedia
Solution to
Productivity Gridlock:
A Re-Engineered
Jewelry Appraisal
System at Zale
Corporation $^{1}$

By: Julie Newman
53 Cyprus Grove Court
New Orleans, Louisiana 70131
U.S.A.

Kenneth A. Kozar
College of Business—
Campus Box 419
University of Colorado/Boulder
Boulder, Colorado 80309-0419
U.S.A.

## Abstract

Zale Corporation once melted down most of its damaged, returned, or repossessed jewelry, resulting in substantial lost revenues. It was determined that additional revenue could be produced from salvageable jewelry if the value of the items could be accurately determined. This meant the jewelry had to be appraised by experienced gemologists to determine the most profitable disposition. The gemologists' productivity suffered because the appraisal was extremely labor intensive. To address this problem, an automated multimedia system utilizing electronically linked measuring instruments, voice recognition, and interconnected LAN databases was developed. Although the unique voice recognition feature of the system was later abandoned, the use of the system enhanced productivity. This paper describes the systems development, its subsequent evolution, and the lessons learned from the process.

Keywords: Human-machine systems, multimedia, voice recognition, business process re-engineering, user/machine dialog design

ISRL Categories: AH0603, CA0201, CA14, DD0402, FB0403.04, HC0101

## Introduction

The world of gems, jewelry, and diamonds is a fascinating one. Even though most of us at one time or another purchase these items, the jewelry industry has been given little attention in the business or information systems literature. Some problems of the jewelry industry are common to many businesses, but others are unique. Unlike many other products, the component parts of a piece of jewelry as well as the composite item have intrinsic market value. Not many items sold in retail outlets could be melted down and sold for their salvage value. This uniqueness creates both problems and opportunities for Zale Corporation.

## The Problem/Opportunity

Zale Corporation, the world's largest jewelry retailer, has a jewelry processing center in its world headquarters building in Irving, Texas. Each year the center receives about 300,000 unsalable pieces of discontinued, damaged, or repossessed fine jewelry from its 1500 stores. In the past, a lack of sufficient processing ability forced Zale to ship these goods periodically to a local smelter to be melted down in acid baths. The smelter returned to Zale a check for the value of the recovered gold along with glass bottles containing the diamonds and other precious gemstones recovered from the melting process.

Almost all of the Corporation's so-called "surplus" jewelry was melted. Because the value of melted jewelry is far below its original cost, disposing of unsalable jewelry in this manner resulted in significant losses for Zale. Much of the original damage to this jewelry, if any, was slight—a loose prong or a scratch. However, determining a more profitable means of disposing of damaged jewelry is a very complex process. Experienced gemologists must perform a detailed appraisal of the jewelry. Scientific measuring devices, complex calculations, and subjective analysis are used to derive the current salvage value of each item and assess its potential for additional recovery. The gemologists also must look up current commodity prices for gold and gemstones to determine their salvage value (see Figure 1). Since a good gemologist can manually evaluate only about 25 pieces of jewelry per day, traditional methods are not a cost-effective process for appraising a high volume of jewelry.

In addition to the possibility of recovering additional revenue from intact damaged jewelry, there is an opportunity to recover more from the components of the jewelry that must be melted. Zale was paying “finders’ fees” to various vendors for locating specific gems to satisfy insurance claims and customer repairs. Tens of thousands of dollars each month could be saved if Zale maintained an accurate inventory of the loose gemstones that were recovered when large quantities of jewelry were melted. The diamonds and gems recovered from the smelting process were being sold through brokers in large batches with little understanding of their individual size and quality. A perpetual inventory that identified the size, shape, and quality of precious gemstones would allow them to be reused, thus greatly enhancing their value to Zale.

The consequence of not knowing the actual value of salvaged jewelry was clearly illustrated when one of the authors was handed a bottle of loose diamonds and told that their total value was “probably about one million dollars.” After appraisal, it was determined that the value of the diamonds in the bottle was closer to two million dollars.

A still greater potential for increasing the revenue produced by the disposition of distressed inventory came from refurbishing the jewelry and then retailing it at reduced margins through liquidation outlets. But first the rather daunting problem posed by the high volume of items that must be subjected to a gemologist's scrutiny had to be overcome.

![](/api/attachments/WKJ8NRAE/fulltext/images/ff993f07688031656e0f2c9b3693c8c37abaa45b087c31b9481b0732e31433e9.jpg)  
Figure 1. The Gemologists' World

To address the appraisal problem, Zale considered the possibility of automating the process in order to improve the productivity of the gemologists. At first glance, appraising jewelry appeared to be incompatible with automation. However, closer examination and revision of the gemologists' processes, combined with a concern for the end user, resulted in a creative and unique application of modern technology that led to dramatically increased productivity.

## An Automated Solution to Jewelry Appraisal

An automated system to receive and appraise the unsalable inventory that accumulates in Zale Corporation jewelry stores was proposed. The end result was an intelligent, multimedia system named “MEDUSA.” $^{2}$ MEDUSA was designed to run on a local area network and utilize voice recognition as the primary vehicle for capturing data. All of the activities performed by the gemologists were supported by voice commands, including the use of ancillary tools-of-the-trade such as calipers and diamond scales. Barcodes were used to track items as they made their way from receipt through a multitude of possible detours and destinations. This system allowed expert gemologists to increase their productivity by 600 percent, and Zale’s recovery from distressed merchandise has increased by millions of dollars.

To build the system, three criteria were identified that in combination were expected to have the necessary impact on productivity: (1) allow the gemologists' hands and eyes to be used solely for evaluating jewelry, not for completing forms or performing keyboard data entry, (2) eliminate as much as possible the need to evaluate every item, and (3) provide decision support for the gemologists throughout the entire appraisal process. The first objective was realized to be of pivotal importance after conducting simulated evaluations and observing that the gemologists' hands and eyes were continually occupied with instruments and of course, the jewelry itself. Each objective was met by integrating new technology with leading-edge systems already in place at Zale Corporation.

The system has evolved since its original design—the gemologists no longer use the voice recognition feature. But the development and evolution process are nonetheless instructive. The following describes Zale Corporation's experiences with this new process for dealing with unsalable jewelry.

## The Process of Evaluating Unsalable Jewelry

The purpose of the gemologists' evaluation is to ascertain accurately the actual salvage value of each piece of jewelry. This value is used as the basis for determining the greatest revenue-producing disposition for each item by estimating the resulting profit or loss and accurately assigning the results to the appropriate cost center.

The merchandise that is processed through the MEDUSA system is comprised of four types of unsalable jewelry: (1) damaged or defective items, (2) discontinued items, (3) repossessed items, and (4) trade-ins. The 1500 retail stores periodically return these items to Zale Corporation headquarters in Irving, Texas. Store personnel produce a shipping document by entering a transaction into their point-of-sale system. This transaction also updates a host-based file with the details of the shipment.

When the jewelry is received in the processing center at Zale headquarters, a unique barcode is affixed to each item. A receiving auditor enters the number of the accompanying document into MEDUSA, and the shipment information is retrieved from the host-based file and displayed on the auditor's LAN-based workstation.

The auditor receives each line of the shipment by scanning barcodes until the quantity scanned equals the quantity shipped. For instance, if the quantity of an item on a shipping document is "3," the system expects the auditor to scan three different barcodes before proceeding to the next line. After all items in a shipment are received, they are sorted into common categories (watches, gold jewelry with stones, gold jewelry without stones, etc.) and staged for evaluation by the gemologists.

Another module of the application aids appraising and maintains a perpetual inventory of the loose diamonds that are returned from the smelter. This inventory, including stones that are removed prior to melting, is used to satisfy most diamond bond insurance claims and other repairs. (A diamond bond insures that a customer's diamond will be replaced if it is ever broken or lost from its mounting.)

When jewelry that needs a diamond replaced is received from one of the stores, a gemologist determines the exact specifications of the stone needed to replace the customer's stone. With MEDUSA, the gemologist locates the diamond in the loose stone inventory and produces a barcoded label to keep track of the jewelry as it is circulated to the repair vendor and back to the store. At the end of each step in the process, MEDUSA automatically sends a fax message to the store so that the current status of the repair is always available to satisfy customer inquiries.

MEDUSA also provides mechanisms for transferring evaluated items to various liquidation centers, repair vendors, and smelters. All necessary documents and reports are generated, and financial accountability for all activity is maintained at the cost-center level.

## Multimedia Jewelry Evaluation

The jewelry evaluation module of MEDUSA utilizes unique processes and technology. (See Figure 2 for a view of the system inputs, outputs, and technological aids.) Voice recognition technology was chosen to satisfy the first productivity criterion of “keeping the gemologists’ hands and eyes on the jewelry.” To activate the voice processor, the gemologist uses a lightweight microphone headset plugged directly into a voice processing card located inside a 386-class workstation. Digital calipers and a highly sensitive digital scale are used to measure and weigh the jewelry. They are connected to the workstation through serial ports.

Positive identification of each item is ensured by its barcode label. When a gemologist is ready to evaluate an item, he or she scans the barcode with a fixed laser barcode scanner. The scanner utilizes a software interface to decode the scanner information for the workstation. If a repair is prescribed, a repair label is created with a barcode label printer that is attached to the workstation. If a stone is removed from a setting, the same printer produces a label for a “diamond paper” in which the diamond will be stored in inventory.

The second productivity criterion of eliminating the need to evaluate every item was met via an interconnected LAN environment that allows access to databases that reside on different LAN servers. A gemologist begins an evaluation by scanning the barcode on an item that has been received in MEDUSA. If the item originated as Zale-owned inventory, MEDUSA queries a database on another LAN called “MIDAS” $^{3}$ and retrieves a file containing its original manufacturing specifications. This file, known as an “adoption sheet,” was created by a buyer at the time of the original purchase. Adoption sheet data includes the type and weight of the mounting metal, the cut, color and clarity of the diamonds, etc.—all of the information that a gemologist must ascertain during an appraisal.

If adoption sheet data is available, the gemologist modifies data elements that now differ from the original specifications because of the current condition of an item. For example, an adoption sheet for a multi-diamond ring specifies that the ring contains six identical sidestones, but one of the sidestones is now missing. The gemologist changes the quantity of sidestones to “5,” reviews the rest of the specifications for discrepancies, and the evaluation is complete.

To confirm an evaluation, a gemologist can display a full-color image of an item on the workstation monitor. This image also is retrieved from a file on the MIDAS LAN. By referring to merchandise images, a gemologist can quickly verify whether the item being evaluated is the same item described on the adoption sheet and make the necessary corrections if an error in identifying an item has been made.

If adoption sheet data is not available, the gemologist must perform a complete evaluation. A typical, fully voice-supported appraisal for a simple diamond solitaire pendant with chain is scripted in Table 1. A “beep” sound is made after each data element appears on the screen to indicate to the user that the recognition was successful.

![](/api/attachments/WKJ8NRAE/fulltext/images/338311a8e2009a7a19523bde9a712238f34b9ddd9f1adab854f4630e488659f5.jpg)  
Figure 2. An Overview of the MEDUSA Appraisal System

The application deduces the probable depth of the diamond from its shape, length, and width. The application uses the dimensions and the specific gravity to calculate the carat weight, because it is impossible to accurately weigh a mounted diamond. The application then uses the quality of the diamond (color and clarity) plus its shape and size to look up its current market price from a gem-pricing index that is downloaded to the system each week. The market price of gold also is maintained in the system and used to calculate the salvage value of the gold in each item.

As each of these values is calculated, the gemologist either accepts the value by saying, "End," or speaks a new value digit by digit, followed by "End." After the values of all its components are derived, the system compiles the total salvage value of the item under evaluation and displays the amount for the gemologist's approval.

Table 1. An Example of a Voice-Supported Apraisal

<table><tr><td>MEDUSA PROMPTS:</td><td>USER SAYS:</td><td>SCREEN DISPLAYS:</td></tr><tr><td>Type?</td><td>“Pendant”</td><td>Pendant</td></tr><tr><td>Metal?</td><td>“Gold”</td><td></td></tr><tr><td>Karat?</td><td>“Fourteen”</td><td>14K</td></tr><tr><td>Weight?</td><td>(Puts pendant on scale) and says, “Read.”</td><td>2.32gm</td></tr><tr><td>Stones?</td><td>“Yes”</td><td></td></tr><tr><td>Type?</td><td>“Diamond”</td><td>Diamond</td></tr><tr><td>Shape?</td><td>“Oval”</td><td>Oval</td></tr><tr><td>Quantity?</td><td>“One”</td><td>1</td></tr><tr><td>Color</td><td>“H”</td><td>H</td></tr><tr><td>Clarity?</td><td>“SI2”</td><td>SI2</td></tr><tr><td>Length?</td><td>User measures length with caliper and says, “Read.”</td><td>10.5mm</td></tr><tr><td>Width?</td><td>User measures width with caliper and says, “Read.”</td><td>6.60mm</td></tr><tr><td>Depth?</td><td>“End,” to accept the system calculated value.*</td><td>3.79mm</td></tr><tr><td>Carat?</td><td>“End,” to accept the system calculated value.*</td><td>1.55ct</td></tr><tr><td>Value?</td><td>“End,” to accept the system calculated value.*</td><td>$4,050.00</td></tr><tr><td>Type?</td><td>“Continue,” to indicate that there are no more stones.</td><td></td></tr><tr><td>Melt Value?</td><td>“End,” to accept the system calculated value.</td><td>$4,051.26</td></tr><tr><td>Disposition?</td><td>“Liquidation”</td><td>Liquidation</td></tr><tr><td colspan="3">The application now returns to the “Enter barcode” prompt.</td></tr></table>

\*The user may override system-calculated values by speaking a new value, i.e., “three point eight five end.”

The interface was designed to be adaptable to the experience level of the end user. An experienced user who has memorized the evaluation scripts may choose to turn off the audio prompts. Each user also has the ability to adjust the intervals during which the voice processor is in “recognize” mode. As a gemologist becomes better at using the system, he or she can continually reduce the time required for an evaluation by turning off the voice prompts and then decreasing the time between beeps during which the voice recognizer is “listening” for a valid vocabulary word.

The third criterion for increasing productivity was the availability of decision support for the gemologists throughout the evaluation process. In addition to deriving salvage values for a gemologist's approval, the application provides support for determining the costs of standard repairs and their impact on the potential profitability of reselling an item instead of melting it. After a gemologist has chosen a final disposition for an item, the application also recommends a retail price if the disposition is other than "Melt."

## Speaker/Independent Voice Recognition

The jewelry evaluators' workstations consist of a number of technical features that in combination provide an optimum environment for appraising jewelry. A focus on speaker-independent voice recognition in particular is included here because voice input is promoted as an interface feature that will be popular in the future (Bylinsky, 1993), yet has received little discussion in the information systems literature. The voice recognition feature was a highlight of the early implementation of the system. As the gemologists grew familiar with the system and sought greater productivity, the users sought alternative and faster methods. Nonetheless, an in-depth discussion of the development issues helps to reveal the strengths and weaknesses of the voice recognition system both in this case and for other potential applications.

Vocabulary size is one of the most important criteria to consider when evaluating the feasibility of using voice recognition in an application. The vocabulary should be relatively small and very stable since retraining a vocabulary to recognize a new word can be time intensive. The vocabulary used in MEDUSA consists of 127 words specific to the jewelry industry. To create the vocabulary, 40 volunteers—an approximately equal mix of men and women—were asked to record each of the words that the application had to recognize. Then the vocabulary was “trained,” that is, a composite of all of the samples of each word in the vocabulary was created. Training is a batch process that can take many hours to complete, depending on the size of the vocabulary.

Each time an end user speaks a vocabulary word to the application, the word is stripped of all of the vocal characteristics that distinguish one speaker from another. The result is called a “token.” The token contains only those auditory features that make a word unique. Since the information in the token is relevant to the speech rather than to the speaker, the token is said to be “speaker normalized.” The normalized token is then compared to each of the templates in the vocabulary, and the template that is least different from the token is identified. The difference between the token and the closest template is scored; the score must be less than a specified value (called the acceptance threshold) for the application to recognize a vocabulary word.

The difference between the closest match and the second closest match also is calculated. This value must be greater than a specified value (called the delta threshold) in order for the application to proceed as though it has indeed recognized a vocabulary word correctly. If the delta threshold is too low, the user is asked to choose between the first and second matches:

System: "Did you say diamond?" User: "No"

System: "Did you say emerald?" User: "Yes"

At this point, the system can automatically untrain the word “diamond” and retrain the word “emerald.” This user's token for the word “emerald” is subtracted from the template for diamond and added to the template for emerald. The vocabulary system thus is encouraged to learn from its own mistakes. It is interesting to note that one of the templates in the vocabulary is called the “garbage collector.” The garbage collector is trained to recognize background noise, distortion, and conversation unrelated to the application so that the voice recognizer is not easily confused.

It is this adaptive training capability that is the key to accurate speaker-independent voice recognition. In the Zale application, using “on the fly” training has resulted in an accuracy rate that is better than 99 percent for a vocabulary that is considered large for this type of technology. Of course, productivity and user acceptance would be seriously impaired if the accuracy rate were poor.

## MEDUSA System Benefits

Since the first phase of MEDUSA implementation in November, 1991, the system has been accumulating data about the Zale Corporation's inventory of unsalable jewelry. The system is now yielding strategic information that is being used for much more sophisticated management of a valuable corporate asset. Executives now know the exact value of each commodity (gold, diamonds, etc.) in each of the disposition categories, and they have the flexibility to shift dispositions in response to changing business demands. For instance, it is possible to ascertain exactly how much cash can be generated quickly by melting all items currently designated for repair as well as the loss that will be incurred by doing so. Zale can now verify that it is paid by the smelter for the correct amount of gold and that the correct number of diamonds is returned after a melt. Prior to MEDUSA, Zale was at the mercy of its vendors to perform these services accurately.

Another example of better asset management was related by one of the gemologists. Zale's National Diamond Bond Replacement Center, Zale's service center that satisfies insurance claims for lost or broken diamonds, was running low on .25 carat diamonds. Using MEDUSA, the gemologists were able to locate quickly all the one-quarter carat diamonds mounted in jewelry in Zale's inventory targeted to be melted. These stones were removed from their mountings, transferred to Diamond Bond and used to satisfy insurance claims. Over \$100,000 worth of diamonds was supplied immediately, and the diamond bond center did not have to purchase additional stones.

In addition to financial control and increased revenue, MEDUSA is also contributing information that can be used to provide better quality merchandise to its customers. Zale's merchandisers now have the ability to identify chronically defective merchandise and advise manufacturers about defects. The MEDUSA gemologists are sensitizing the merchandisers to manufacturing techniques that should be avoided and are using information from MEDUSA to substantiate their advice. In one instance, the same defect was found repeatedly in a flexible tennis bracelet (it snapped in two instead of flexing). The item was recalled from all stores and returned to the vendor for credit.

MEDUSA also makes it possible to monitor shipments from the stores to the surplus processing center and ascertain whether abuse of corporate return and trade-in policies is occurring. Some stores grant excessive trade-in allowances in order to disguise unauthorized merchandise discounts. Now, when a trade-in is evaluated in MEDUSA, its appraised value is compared to the trade-in allowance granted to the customer, and significant discrepancies are reported to store management. Stores also used the practice of returning damaged merchandise to headquarters to relieve their inventories of admittedly undesirable, but definitely undamaged merchandise. These practices now can be identified and prevented.

## Adaptability and Evolution of MEDUSA

The MEDUSA system's "human factors" have had a positive influence on the morale and productivity of its end users.4 In large part, MEDUSA and its users simply are a good match: creative individuals with a flexible multimedia computer system. But with this innovative technology, the users function as far more than an adjunct to a computer system.

First of all, the gemologists believe that they could not accomplish their job without the system due to the magnitude of the work to be done. Without MEDUSA, either they would be faced with an impossible task, or more likely, they would be forced to perform their work far below their personal standards. MEDUSA provides its users with the means to increase their productivity while meeting very high standards for quality.

Unforeseen flexibility in operating modes has also proven to be popular with the end users. The application was intended to be operated in a single context with a carefully controlled series of voice commands. However, because the gemologists have control over the audio portion of the interface and the option of keyboard entry (initially provided in case the voice processor failed), they have developed a great variety of techniques for capturing data. In fact, none of the gemologists operates the system exactly as originally envisioned.

The flexibility of the system proved fortuitous during changing business conditions—MEDUSA has evolved to adapt to new business needs. Soon after MEDUSA was implemented, Zale closed hundreds of its stores in an effort to adjust its business to the adverse economic conditions that have affected many retailers during the past few years. The entire jewelry inventory from each of these stores was returned to the Zale processing center for evaluation using MEDUSA. The quantity of goods received was many times greater than MEDUSA was originally expected to handle.

Decisions were made to change the gemologists' procedures to accommodate the extraordinary demand for expedited processing. Certain types of simple jewelry are no longer evaluated. The gemologists who have the most experience with MEDUSA can now make appropriate business decisions about the disposition of such things as "gold without stones" without relying on the system, because some decisions that were formerly supported by MEDUSA have now become automatic for the users. In this context, MEDUSA has trained the users' judgement over time and served as a bridge to an even more productive approach.

For more complex items, voice processing has been replaced for the most part in favor of short cuts like “hot keys” to read the digital instruments and bypassing certain data elements. The financial necessity of increasing the speed of the gemologists was deemed more important than the consequent sacrifice of some of the strategic information that MEDUSA provided. According to one of the gemologists, “Voice is still the preferable way to operate the system, because you get quality not possible without it.”

The primary characteristic of voice recognition technology that impeded its use is the inherent delay that occurs after each word is spoken by the user. This is the time required for the voice processor to “recognize” a word. Not using the voice recognition feature eliminates this short delay. This elimination combined with modifying the evaluation procedures has increased the users’ productivity by 16 to 18 percent.

It is possible that similar gains in productivity could have been achieved by improved technology. For instance, upgrading the workstations might have “recompensated” for the recognition delay, or changes made to the LAN infrastructure might have decreased the voice response time. Retraining the vocabulary may have improved response time and accuracy, or new versions of the technology might make recognition faster. However, no matter how well integrated and finely tuned a system might be, there will be an inherent delay in recognizing spoken input. In determining the feasibility of incorporating voice recognition in an application, the designer must consider whether the delay can be used productively to perform part of a process or whether the delay will simply amount to lost time.

Even without the voice recognition component, the MEDUSA system demonstrates synergy between a human and a machine. A number of complex algorithms in the application require minimal input from the gemologist to calculate or deduce most of the measurements and values that are required to appraise jewelry. This background processing is performing all of the “left brain” activity, leaving the gemologist free to evaluate the quality, design, and desirability of the jewelry—the “right brain” activity. The decisions of the gemologist are a synthesis between the left brain “value” of the jewelry and its right brain “appeal.” MEDUSA thereby provides a satisfying experience for creative individuals who must perform subjective mental activity that cannot be performed by a computer but that requires computational support. Of course, even the calculations performed by the computer are scrutinized by the gemologist and can be overridden if the user’s superior judgement so rules.

Finally, the novelty of the system itself is an obvious element of pride to its users. The gemologists each have from 10 to 20 years of experience and are dedicated to the jewelry industry. According to the gemologists, not only is MEDUSA a high-quality state-of-the-art system, but it is the only computer system in the world developed for appraising jewelry. “Driving” something unique and superior definitely contributes to the users’ level of satisfaction with the system.

The above observations about MEDUSA could be applied in general terms to user-centric system design in any environment, regardless of the business or the technical platform. Some widely applicable lessons have been learned. A superior system will provide the users with the means to perform excellent-quality work; give them the flexibility to use the system in a variety of ways at their own discretion; and encourage the uniquely human contribution of the end user.

## Conclusion

The development of the MEDUSA system was based on a need to manage the elimination of unsalable inventory from Zale Corporation's 1500 stores and recover as much revenue as possible from its final disposition. In order to accomplish this, a creative solution to facilitate processing the jewelry and improve the quality of information available to executives has been employed with impressive results, both tangible and intangible.

To begin with, Zale Corporation is now stocking 40 clearance stores with jewelry that would have been melted in the past. In fact, 58 percent of all jewelry processed through MEDUSA has been recycled for sale as finished goods. Although it still is advisable to melt a great deal of Zale's distressed inventory, the losses thus incurred are now more than offset by selling the majority of the jewelry in "off-price" retail outlets. Zale also is internally supplying loose diamonds for repairs and insurance claims from its own inventory, and all costs previously incurred by using outside vendors to provide this service have been eliminated. The total financial impact on the corporation will amount to millions of dollars each year.

The workstation architecture and application design have struck a very positive chord with the end users. Not only does the system give them the ability to meet a demanding need for productivity, but the unique nature of the integrated environment empowers their creativity.

## Endnotes

$^{1}$ An earlier version of this paper won second place in the 1992 Society for Information Management International Paper Awards Competition.

$^{2}$ All Zale LAN-based systems are named after lesser known characters from Greek mythology.

$^{3}$ MIDAS stands for Merchandise Imaging and Data Administration System.

"For more details on human-computer interaction, see Card, S.K., Moran, T.P., and Newell, A. The Psychology of Human-Computer Interaction, Lawrence Erlbaum Associates, Hillsdale, N.J., 1983; Gerlach, J.H. and Kuo, F. "Understanding Human-Computer Interaction for Information Systems Design," MIS Quarterly (15:4), December 1991, pp. 526-549; Gould, J.D. and Lewis, C. "Designing for Usability: Key Principles and What Designers Think," Communications of the ACM (28:3), March 1985, pp. 300-311; and Norman, D.A. and Draper, S.W. (eds.) User Centered System Design—New Perspectives on Human-Computer Interaction, Lawrence Erlbaum Associates, Hillsdale, NJ, 1986.

## Reference

Bylinsky, G. "At Last! Computers You Can Talk To," Fortune (127:9), May 3, 1993, pp. 88-91.

## About the Authors

Julie Newman is a business solutions manager for Integrated Systems Solutions Corporation (ISSC), a subsidiary of IBM. For ISSC she specializes in outsourcing and consulting services related to distributed computing. Prior to joining ISSC, she was the manager of LAN Development for Zale Corporation, the world's largest jewelry retailer. She was the primary architect and designer of the system discussed in this paper and was one of the winners of the SIM International Paper Award Competition in 1992.

Kenneth A. Kozar is a member of the information systems faculty at the University of Colorado in Boulder. He has been on the faculties of several universities and has considerable experience as an MIS practitioner. He and various co-authors were winners in the SIM International Paper Award Competition in 1985 and 1989. He is an associate editor of the MIS Quarterly and on the Editorial Board of IS/Analyzer.
