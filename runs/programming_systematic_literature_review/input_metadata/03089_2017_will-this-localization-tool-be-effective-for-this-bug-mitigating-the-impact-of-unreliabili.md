---
otero_id: "2-s2.0-85001575065"
title: "Will this localization tool be effective for this bug? Mitigating the impact of unreliability of information retrieval based bug localization tools"
authors: "Le T.-D.B.; Thung F.; Lo D."
year: "2017"
journal: "Empirical Software Engineering"
doi: "10.1007/s10664-016-9484-y"
---
# Scopus title-abstract-keyword metadata
Title: Will this localization tool be effective for this bug? Mitigating the impact of unreliability of information retrieval based bug localization tools
Abstract: Information retrieval (IR) based bug localization approaches process a textual bug report and a collection of source code files to find buggy files. They output a ranked list of files sorted by their likelihood to contain the bug. Recently, several IR-based bug localization tools have been proposed. However, there are no perfect tools that can successfully localize faults within a few number of most suspicious program elements for every single input bug report. Therefore, it is difficult for developers to decide which tool would be effective for a given bug report. Furthermore, for some bug reports, no bug localization tools would be useful. Even a state-of-the-art bug localization tool outputs many ranked lists where buggy files appear very low in the lists. This potentially causes developers to distrust bug localization tools. In this work, we build an oracle that can automatically predict whether a ranked list produced by an IR-based bug localization tool is likely to be effective or not. We consider a ranked list to be effective if a buggy file appears in the top-N position of the list. If a ranked list is unlikely to be effective, developers do not need to waste time in checking the recommended files one by one. In such cases, it is better for developers to use traditional debugging methods or request for further information to localize bugs. To build this oracle, our approach extracts features that can be divided into four categories: score features, textual features, topic model features, and metadata features. We build a separate prediction model for each category, and combine them to create a composite prediction model which is used as the oracle. We name this solution APRILE, which stands for Automated PRediction of IR-based Bug Localization’s Effectiveness. We further integrate APRILE with two other components that are learned using our bagging-based ensemble classification (BEC) method. We refer to the extension of APRILE as APRILE +. We have evaluated APRILE + to predict the effectiveness of three state-of-the-art IR-based bug localization tools on more than three thousands bug reports from AspectJ, Eclipse, SWT, and Tomcat. APRILE + can achieve an average precision, recall, and F-measure of 77.61 %, 88.94 %, and 82.09 %, respectively. Furthermore, APRILE + outperforms a baseline approach by Le and Lo and APRILE by up to a 17.43 % and 10.51 % increase in F-measure respectively. © 2016, Springer Science+Business Media New York.
Author keywords: Bug localization; Bug reports; Effectiveness prediction; Information retrieval; Text classification
Index keywords: Classification (of information); Data mining; Forecasting; Information retrieval; Text processing; Bug localizations; Bug reports; Debugging methods; Ensemble classification; Prediction model; Program elements; State of the art; Text classification; Program debugging
Document type: Article
Conference: 
Source title: Empirical Software Engineering
Year: 2017
EID: 2-s2.0-85001575065
DOI: 10.1007/s10664-016-9484-y
Retrieval channels: authoritative_outlet_search
Local full-text files: 
