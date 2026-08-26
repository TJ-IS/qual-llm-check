---
otero_id: "2-s2.0-85171737702"
title: "Does the Stream API Benefit from Special Debugging Facilities? A Controlled Experiment on Loops and Streams with Specific Debuggers"
authors: "Reichl J.; Hanenberg S.; Gruhn V."
year: "2023"
journal: "Proceedings - International Conference on Software Engineering"
doi: "10.1109/icse48619.2023.00058"
---
# Scopus title-abstract-keyword metadata
Title: Does the Stream API Benefit from Special Debugging Facilities? A Controlled Experiment on Loops and Streams with Specific Debuggers
Abstract: Java's Stream API, that massively makes use of lambda expressions, permits a more declarative way of defining operations on collections in comparison to traditional loops. While experimental results suggest that the use of the Stream API has measurable benefits with respect to code readability (in comparison to loops), a remaining question is whether it has other implications. And one of such implications is, for example, tooling in general and debugging in particular because of the following: While the traditional loop-based approach applies filters one after another to single elements, the Stream API applies filters on whole collections. In the meantime there are dedicated debuggers for the Stream API, but it remains unclear whether such a debugger (on the Stream API) has a measurable benefit in comparison to the traditional stepwise debugger (on loops). The present papers introduces a controlled experiment on the debugging of filter operations using a stepwise debugger versus a stream debugger. The results indicate that under the experiment's settings the stream debugger has a significant (<.001) and large, positive effect (p2=.899; M_stepwiseM_stream ~ 204%). However, the experiment reveals that additional factors interact with the debugger treatment such as whether or not the failing object is known upfront. The mentioned factor has a strong and large disordinal interaction effect with the debugger (<.001; p2=.928): In case an object is known upfront that can be used to identify a failing filter, the stream debugger is even less efficient than the stepwise debugger (M_stepwiseM_stream~ 72%). Hence, while we found overall a positive effect of the stream debugger, the answer whether or not debugging is easier on loops or streams cannot be answered without taking the other variables into account. Consequently, we see a contribution of the present paper not only in the comparison of different debuggers but in the identification of additional factors. © 2023 IEEE.
Author keywords: Debugging aids; Programming Techniques; Software Engineering; Usability testing
Index keywords: Computer hardware description languages; Program debugging; Code readability; Controlled experiment; Debuggers; Debugging aids; Filter operations; Interaction effect; Lambda's; Programming technique; Single element; Usability testing; Software testing
Document type: Conference paper
Conference: 
Source title: Proceedings - International Conference on Software Engineering
Year: 2023
EID: 2-s2.0-85171737702
DOI: 10.1109/icse48619.2023.00058
Retrieval channels: authoritative_outlet_search
Local full-text files: 
