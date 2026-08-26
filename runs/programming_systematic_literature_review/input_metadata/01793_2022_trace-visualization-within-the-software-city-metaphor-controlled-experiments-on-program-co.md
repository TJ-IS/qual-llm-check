---
otero_id: "2-s2.0-85133229848"
title: "Trace visualization within the Software City metaphor: Controlled experiments on program comprehension"
authors: "Dashuber V.; Philippsen M."
year: "2022"
journal: "Information and Software Technology"
doi: "10.1016/j.infsof.2022.106989"
---
# Scopus title-abstract-keyword metadata
Title: Trace visualization within the Software City metaphor: Controlled experiments on program comprehension
Abstract: Context: Especially with the rise of microservice architectures, software is hard to understand when just the static dependencies are known. The actual call paths and the dynamic behavior of the application are hidden behind network communication. To comprehend what is going on in the software the vast amount of runtime data (traces) needs to be reduced and visualized. Objective: This work explores more effective visualizations to support program comprehension based on runtime data. The pure DYNACITY visualization supports understanding normal behavior, while DYNACITYrc supports the comprehension of faulty behavior. Method: DYNACITY uses the city metaphor for visualization. Its novel trace visualization displays dynamic dependencies as arcs atop the city. To reduce the number of traces, DYNACITY aggregates all requests between the same two components into one arc whose brightness reflects both the number and the total duration of the requests. DYNACITY also encodes dynamic trace data in a heatmap that it uses to light up the building: the brighter a building is, the more active it is, i.e., the more and the longer the requests are that it receives and/or spawns. An additional color scheme reflects any error/status codes among the aggregated traces. In a controlled experiment, we compare our approach with a traditional trace visualization built into the same Software City but showing all dependencies (without aggregation) as individual arcs and also disabling the heatmap. We also report on a second study that evaluates if an error-based coloring of only the arcs is sufficient or if the buildings should also be colored. We call this extension DYNACITYrc as it is meant to support root cause analyses. The source code and the raw data of the quantitative evaluations are available from https://github.com/qaware/dynacity. Results: We show quantitatively that a group of professional software developers who participated in a controlled experiment solve typical software comprehension tasks more correctly (11.7%) and also saved 5.83% of the total allotted time with the help of DYNACITY and that they prefer it over the more traditional dynamic trace visualization. The color scheme based on HTTP error codes in DYNACITYrc supports developers when performing root cause analyses, as the median of them stated that the visualization helped them much in solving the tasks. The evaluation also shows that subjects using DYNACITYrc with colored arcs and buildings find the responsible component 26.2% and the underlying root cause 33.3% more correctly than the group with just colored arcs. They also ranked it 40% more helpful to color both. Conclusion: The DYNACITY visualization helps professional software engineers to understand the dynamic behavior of a software system better and faster. The color encoding of error codes in DYNACITYrc also helps them with root cause analyses. © 2022 The Authors
Author keywords: Aggregation; Heatmap; Program comprehension; Root cause analysis; Software city; Trace visualization
Index keywords: Errors; HTTP; Memory architecture; Color schemes; Controlled experiment; Dynamic behaviors; Dynamic traces; Heatmaps; Program comprehension; Root cause analysis; Run-time data; Software city; Trace visualization; Visualization
Document type: Article
Conference: 
Source title: Information and Software Technology
Year: 2022
EID: 2-s2.0-85133229848
DOI: 10.1016/j.infsof.2022.106989
Retrieval channels: authoritative_outlet_search
Local full-text files: 
