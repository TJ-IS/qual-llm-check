---
otero_id: 22152
otero_key: "HZ6JWV33"
title: "Improving searching and reading performance: the effect of highlighting and text color coding"
authors: "Jen-Her Wu; Yufei Yuan"
year: "2003"
journal: "Information & Management"
doi: "10.1016/s0378-7206(02)00091-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Improving searching and reading performance: the effect of highlighting and text color coding

Jen-Her Wu<sup>a,\*</sup>, Yufei Yuan<sup>b</sup>

<sup>a</sup>Department of Information Management, National Sun Yat-Sen University, Kaohsiung 80424, Taiwan ROC <sup>b</sup>Michael G. DeGroote School of Business, McMaster University, Hamilton, Ont., Canada

Received 7 July 2001; accepted 29 July 2002

## Abstract

A message presentation and processing model is presented here. It was used, in two experiments, to study how different types of highlighting and text display color combinations affect reading performance. We found that highlighting can significantly improve table searching and that the best highlighting method was color, followed by reverse video and blinking. When different color combinations were used for textual display, the reading speed was higher but the visual preference was lower for situations in which the foreground luminance was lower than the background luminance or the foreground chroma was lower than the background chroma. Hue combinations also affected both visual preference and reading speed, but did not override the dominant impacts of luminance and chroma contrast. The color impact on visual preference was not consistent with its impact on reading speed. Based on these findings, design guidelines are proposed. <sup>#</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: User interface design; Highlighting; Color combination; Reverse video; Blinking; Reading performance analysis

## 1. Introduction

Today, huge volumes of information are being generated and sent over computer networks. However, for information to be of any value, it must be seen as important and thus receiving attention [9]. Managers and office workers are confronted with information seems to be more than they are able or willing to process. For example, Tullis [28] reported that the employees of a single insurance company view over 4.8 million screens per year. Additionally, Galitz [8] reported that bell system employees, using only one software package, extract information from over 344 million displays each year. Thus, a saving of only a fraction of a second in the time it takes users to process each display could lead to enormous time and cost savings [6].

Many technologies have been developed to reduce this information overload, such as database queries, search engines, and more recently, software agents for information filtering. Another method of dealing with information overload is to improve the way that it is organized and displayed so that people can process it more efficiently. Today, computer display technology offers a wide variety of colors and highlighting techniques that may be used to improve the presentation of graphic and textual information [18]. However, with so many choices, it is difficult to investigate how best to employ them. The purpose of our research was therefore to study how different types of highlighting and color combinations affect reading performance. With such data, guidelines can be developed to aid in providing more efficient visual displays.

## 2. Research framework and hypotheses

## 2.1. Communication models

The human information process has been studied in the general framework of communication. In Shannon and Weaver’s general model of communication [25], six basic communication components were identified: a source, an encoder, a message, a channel, a decoder, and a receiver. Messages are encoded into signals and sent by a source to a receiver through a channel. At the receiver side, the signal is decoded into a message. This model has been used to study communication technology as well as human communication. Another model, proposed by Lasswell [12], was used to study mass communication; five components were identified: who? (communicator); says what? (message); in what channel? (channel); to whom? (receiver); and with what effect? (effect). Based on this, five research areas were identified: control research, content research, medium research, audience research, and effects research. With a focus on communication between information systems and human users, the GOMS model [3,10,11] has been widely used in human computer interaction research. This model analyzes how to perform a task in terms of goals, operators, methods, and selection rules. Here, goals are ‘‘what the user has to accomplish,’’ while operators are ‘‘actions performed in pursuing a goal.’’ The actions can be perceptual, cognitive, motor, or a mix of any or all of them. Operators can change the user’s internal mental state or change the state of the external physical environment. Methods are ‘‘sequences of operators that accomplish a goal.’ If there is more than one method to accomplish a goal, selection rules are necessary to represent user knowledge of which method should be applied.

## 2.2. Research framework

In our work we focused on the communication interface between a computer and a human. We studied the information process using the model shown in Fig. 1.

![](/api/attachments/HZ6JWV33/fulltext/images/6db13c79c325c593d7a9b27a2825876e9b44a43318d589c1e1fa2aec070709e5.jpg)  
Fig. 1. The message presentation and process model.

According to this model, a person needs to access messages to solve a particular problem or perform a specific task. The messages contain information as their content and this is presented in a certain way. Once a person receives the message, he or she carries out a series of mental processes, such as recognition, filtering, and abstraction. The outcome will then be an increase in the person’s knowledge. We therefore needed to investigate how message presentation can affect the efficiency of the mental process and the effectiveness of its outcome.

## 2.2.1. Task

People access messages for a task, such as: reading a management report, checking an email, or searching for product information on the web.

## 2.2.2. Message

Every message has two components: content and presentation. The first is the information contained in the message. A sender provides it intending to meet the receiver’s needs. However, the value of the message is determined by the receiver, not by the sender. The message can be presented in many different ways, depending on their media, format, and presentation style. The media can be video, audio, image, graph, and text. The choice of media will affect the type of sensor (eyes or ears) and the understanding of the recipient. A message can be constructed and organized in different forms depending in part on the media. For instance, a graphical object can represent a map, a flowchart, a bar chart, a pie, or a curve, while a textual word or phrase can represent plain text, hypertext, or a table. An audio or musical phrase is usually presented as a sequential unit, but a video clip is often divided into several sub-windows. The presentation format may therefore affect the receiver’s information selection and abstraction process. Within each format, there are also different factors affecting the presentation. For instance, a picture can be colored or black and white. A piece of text may use different fonts, high lights, and colors for the foreground and background. All of these may have a differing impact on efficiency and effectiveness of communication.

## 2.2.3. Mental process

Receiving a message requires a series of mental activities: recognizing the pattern, decoding its meaning, selecting useful or filtering out useless information, conceptualizing, summarizing, abstracting, and memorizing the information. These mental processes depend on each individual’s mental capabilities and are associated with education, age, and intelligence. They are also affected by human information processing limitations, such as sort-term memory, sequential processing, bias, etc. The ways in which information are organized and presented will also affect the efficiency and effectiveness of the mental processes. The first may be measured by the speed and effort required; the second by the knowledge received.

## 2.2.4. Knowledge

The message receiver learns from it and thus increases his or her knowledge, i.e. it is the outcome of the receiver’s mental processes. The receiver may understand or misunderstand the meaning of the message (precision), may understand some but miss other parts (completeness), and may remember some but forget other parts (recall). The effectiveness of learning therefore can be measured by these three: precision, completeness, and recall.

Much research has been performed on the efficiency and effectiveness of information presentation (media, format, and style) [1]. In our study, we focused on presentation style. We wanted to determine, for a specific task, what kind of text presentation style would lead to better reading performance. Specifically, we wanted to study two common tasks: searching for information in a table and reading news from text.

For the first task, a table format was selected because it is a common format of results generated by a database query. We focused on the use of different highlighting styles and their impact on search speed.

For the second task, a plain text format was selected for presenting news. We investigated how different color combinations of the text’s foreground and background affect reading speed and visual preference.

## 2.3. The effect of highlighting on searching a table

Mathieson and Keil [15] found that the task/technology fit affects reading performance. Further, Remus [23] indicated that a table is one of the most effective and commonly used means for information presentation in an IS, especially for tasks involving the

Type II

Type I

![](/api/attachments/HZ6JWV33/fulltext/images/7cf8a42a5603c591e4bb765349281de74884ce62a9da38f65c699ec3631302e4.jpg)  
Fig. 2. Four types of tabular form.

retrieval of specific values [4]. The commonly used table types can be classified into four groups (see Fig. 2): tables with column grid lines (type I); tables with row grid lines (type II); tables with column and row grid lines (type III); and tables without column and row grid lines (type IV). In addition, research has indicated that normal eye movement in a field scan are generally from top-to-bottom or left-to-right [2,27].

Research has also shown that, on average, subjects are quicker to find a target in a highlighted display than in a single-colored display without highlighting [7,13,17]. Under highlighted conditions, four types of highlighting are commonly used: boxing; blinking; reverse video; and color. Fisher and Tan used blinking, reverse video, and color conditions as aids to finding a target digit from five digits appearing in a horizontal array on the screen. They determined that the reading performance, in decreasing order was: color, reverse video, without highlighting, and blinking.

However, in most cases, the IS displays in a business environment differ from Fisher and Tan’s experimental scenario:

(1) in business IS displays, the targets are not a single digit and are not known in advance;

(2) the target items are not displayed in a known position, for instance, in the middle of the screen as they were by Fisher and Tan; and

(3) in many situations, the targets have different types of tabular formats, e.g. they are in a column or a row of a table.

From a user interface design perspective, it is important to know whether highlighting conditions impact the reader, as suggested in the literature. What guideline can a system designer follow in designing highlighting conditions? The literature contains few empirically grounded answers, yet the answer is important to system engineers confronted with the issue of user interface design.

The following hypotheses are proposed.

H1a. The type of tabular format used affects the reading time of information searches.

H1b. The information display position within a table affects reading time during information searches.

H1c. The highlighting conditions affect the reading time of information searches.

2.4. The effect of color coding on reading textual data

A modern video display provides a real opportunity to use rich colors. Indeed, with 24-bit encoding for each pixel, it is possible to display more than 32 million colors. In general each color can be encoded in three dimensions: hue; luminance; and chroma.

## 2.4.1. Hue

This is the color without black, white, or gray added. Different colors result from different combinations of the three primary colors: red, yellow, and blue. There are three secondary colors: orange, green, and violet generated by combinations of any two of the three primary colors. More colors can be generated by further color combinations.

## 2.4.2. Luminance

This is the lightness of a color. Without hue, the lightest color is white and the darkest is black. Between these limits are different degrees of gray. Each color can also have a different luminance, e.g. blue with different luminance can range from sky blue, through soft blue, to dark blue.

## 2.4.3. Chroma

This is the measure of the purity of a color; it is also termed saturation. It is the percentage of a color versus the residual percentage of white or black. The higher the percentage of the color, the higher its purity and the brighter it appears. For instance, e.g. for a blue color with the same luminance level as dark gray, the different chroma levels (from high to low) range from vivid blue, through strong blue, and dull blue, to grayish blue, and ultimately to dark gray.

In general, color coding has proven to be the most effective way of enhancing search tasks and it is generally superior or at least equal to achromatic coding in identification tasks [20]. Sanders and McCormick [24] indicated that people differ markedly in their preferences for color, but generally blue, green, and red hues seemed to be most often preferred.

Aside from hue, people tend to prefer light to dark colors and saturated to unsaturated colors. Furthermore, when objects are placed against a background, people tend to prefer high contrast combinations, i.e. light colored objects with dark background colors or vice versa. In addition, research has indicated that better reading performance in terms of speed and accuracy is gained with dark on light polarity [5]. However, some other research (e.g. [21]) found that the high light–dark polarity has no effect on reading performance.

The question thus arises: will different hue, chromaticity, and luminance combinations influence performance when reading text in terms of speed and reader preference? To the best of our knowledge, very little has been done to answer this question systematically. Yet, the answer is important to designers who are confronted with the issue of using the right color for interface design. Therefore, the following hypotheses are proposed.

H2a. The luminance of the text foreground and background affects reading performance.

H2b. The chroma of the text foreground and background affects reading performance.

H2c. The hue of the text foreground and background affects reading performance.

## 3. Experimental design

Two laboratory experiments were performed to test the hypotheses.

## 3.1. Experiment I

In the first experiment (on highlighting), the task was to search for information in a table. The data used simulated a hypothetical firm’s scheduled and actual production information, as shown in Fig. 3. Only one of the nine products (e.g. the magic cleaner in the fourth row) did not have as much production as had been scheduled. Subjects were asked to find this exception data and record its value.

The data were represented using all four types of tabular forms. To assess the position impact, for each type of form the exception data was uniformly but randomly displayed in the second, fourth, sixth, and eighth row positions. The first two and the last two positions are in the upper and lower parts of the screen, respectively.

There were four highlight conditions: standard (i.e. without highlighting); blinking; reverse video; and color. In the standard condition, none of the digital data was highlighted; the background was uniformly light gray and the digital data were written in black.

![](/api/attachments/HZ6JWV33/fulltext/images/3e9bfb0345f0e00268fccce6acc217d16772209c4d2d3adc89fa75cf06483183.jpg)  
Fig. 3. Sample table shown in type IV form with color highlighting.

For the other three conditions, the exception data were highlighted as follows.

\- In the blinking condition, the on/off frequency of the data was 0.3 s. This frequency was chosen, because it provided visual comfort, as assessed by readers in several pilot experiments.

\- In the reverse video condition, the highlighted digits were white with a black background. In the color condition, the highlighted digits were colored red. This was based on work described in two articles: Post and Snyder [22] found that a red display yielded faster digit recognition time than white, yellow, or green; and Mathews et al. found that the speed of recognition went from red to blue, white, and green. Therefore, we selected red as the highlight color.

This experiment utilized a Latin square design approach. The variables (or factors) and conditions (or levels) of each variable in the experiment are shown in Table 1.

## 3.2. Experiment II

For the text reading experiment, the task involved reading a newspaper article from a color text display with different combinations of hue, luminance, and chroma levels in the foreground (font) and background.

The practical color co-ordinate system (PCCS) standard was used for color representation. In this, the major hues are red, orange, yellow, green, blue, and purple. Black and white (as well as gray) have no color or hue although they are often misrepresented as colors. There were nine levels of luminance: 1 (black), 2.4, 3.5, 4.5, 5.5 (gray), 6.5, 7.5, 8.5, and 9 (white); these are denoted as N1–N9. Similarly, the chroma levels were from low to high and divided into nine levels, denoted as S1–S9. Thus, the number of possible combinations of hue, luminance and chroma levels for the foreground and background were $( 7 \times 9 \times 9 ) ( 7 \times 9 \times [ 9 - 1 ] ) =$ 3922. Excluding some unrecognizable combinations, the possible number of choices was still too great to investigate fully.

Latin square design for experiment I

<table><tr><td rowspan="2">Highlighting</td><td colspan="4">Form type</td></tr><tr><td>I</td><td>II</td><td>III</td><td>IV</td></tr><tr><td>Without highlighting</td><td> $2^a$ </td><td>8</td><td>6</td><td>4</td></tr><tr><td>Blinking</td><td>4</td><td>6</td><td>2</td><td>8</td></tr><tr><td>Reverse video</td><td>6</td><td>4</td><td>8</td><td>2</td></tr><tr><td>Red color</td><td>8</td><td>2</td><td>4</td><td>6</td></tr></table>

<sup>a</sup> Indicates the display position of exception data.

To simply the experiment, we chose N8, N5, and N2 to represent high, medium, and low luminance; and S8, S5, S2 to represent high, medium, and low chroma, respectively. We also needed to reduce the number of hue combinations and decided to create two sets of hue combination comparisons. In the first, the foreground (font) was black or white and only the background had color; this was used to study the impact of different luminance levels. In the second, the foreground and background had different color combinations; this was used to study the impact of different chroma levels.

To find our first and most likely hue combination set, we performed a simple survey to determine which colors are used in popular application software packages. The common foreground and background color combinations were found to be: black, blue, or green on white, black on gray, white on blue, white on green, and black on yellow. The results of the minisurvey are summarized in Table 2. Based on this, the combinations (black or white)/(white or black), (black or white)/blue, (black or white)/green, and (black or white)/yellow were chosen to investigate the color luminance effect on reading performance.

To determine the second hue combination set, we considered six major colors based on the PCCS, i.e. red, orange, yellow, green, blue, and purple. In the foreground (FG) and background (BG) combinations, there could be 30 different combinations. However, previous research found that red on blue, blue on red, blue on black, and red on black produce poorer reading performance [14,16]. The American National Standard for Human Factors Engineering of Visual Display Terminal Workstations recommends avoidance of blue in work involving fine detail and also avoidance of a combination of pure red and blue on a dark background because of chromostereopsis. In addition, it states that visual displays should avoid simultaneous display of highly saturated, spectrally extreme colors [19]. Avoiding extreme color pairs, such as red and blue or yellow and purple, was also recommended. Many color combinations were therefore eliminated and the final set for our experiments was reduced to yellow/blue, blue/yellow, red/green, blue/green.

This experiment also utilized a Latin square design approach in investigating reading performance under different hue, luminance, and chroma level combinations in text fore- and backgrounds. For easy comparison, we divided the experiments into four groups, as shown in Tables 3–6. Each contained 36 different hue, luminance, and chroma level combinations. Groups 1 and 2 were used to test the major impact of relative luminance contrast between the fore- and background at different background chroma levels. In group 1 the foreground luminance was set higher than the background luminance and in group 2 the foreground luminance was set lower than the background luminance.

Table 2  
A survey of foreground/background color tools

<table><tr><td>Interface element</td><td>Foreground/ background</td><td>Number of software</td><td>Software</td></tr><tr><td rowspan="5">Editing area</td><td>Black/white</td><td>10</td><td>Amipro, Powerpoint, Word, SAS, SPSS, Netscape, Excel, Visio, Freelance, Lotus123</td></tr><tr><td>White/blue</td><td>1</td><td>PEII</td></tr><tr><td>Black/light blue</td><td>1</td><td>Amipro</td></tr><tr><td>Blue/white</td><td>1</td><td> $SAS^a$ </td></tr><tr><td>Green/white</td><td>1</td><td>SAS</td></tr><tr><td rowspan="3">Message box</td><td>Black/white</td><td>2</td><td>SPSS, Amipro</td></tr><tr><td>Black/yellow</td><td>1</td><td>Word</td></tr><tr><td>Black/gray</td><td>13</td><td>Win98,  $VB^b$ , C++, Schedule, Excel, Access, Visio, Freelance, Lotus123, Word, Powerpoint, SAS, Netscape</td></tr><tr><td rowspan="3">Function menu</td><td>Black/gray</td><td>9</td><td>Win98, Netscape, VB, C++, Access, Excel, Schedule, Word, Powerpoint</td></tr><tr><td>Black/white</td><td>6</td><td>Visio, Freelance, Lotus123, SPSS, Amipro, SAS</td></tr><tr><td>White/green</td><td>1</td><td>PEII</td></tr></table>

<sup>a</sup> This tool has more than one editing area.  
<sup>b</sup> VB only has message box and function menu.

Table 3  
Experimental design for the luminance effect

<table><tr><td rowspan="3">F/B chroma</td><td colspan="6">F/B luminance</td></tr><tr><td colspan="3">Group 1: FL &gt; BL</td><td colspan="3">Group 2: FL &lt; BL</td></tr><tr><td>N8/N5</td><td>N8/N2</td><td>N5/N2</td><td>N5/N8</td><td>N2/N8</td><td>N2/N5</td></tr><tr><td>High chroma (S0/S8)</td><td>W/B, W/L, W/G, W/Y</td><td>W/B, W/L, W/G, W/Y</td><td>W/B, W/L, W/G, W/Y</td><td>B/W, B/L, B/G, B/Y</td><td>B/W, B/L, B/G, B/Y</td><td>B/W, B/L, B/G, B/Y</td></tr><tr><td>Medium chroma (S0/S5)</td><td>W/B, W/L, W/G, W/Y</td><td>W/B, W/L, W/G, W/Y</td><td>W/B, W/L, W/G, W/Y</td><td>B/W, B/L, B/G, B/Y</td><td>B/W, B/L, B/G, B/Y</td><td>B/W, B/L, B/G, B/Y</td></tr><tr><td>Low chroma (S0/S3)</td><td>W/B, W/L, W/G, W/Y</td><td>W/B, W/L, W/G, W/Y</td><td>W/B, W/L, W/G, W/Y</td><td>B/W, B/L, B/G, B/Y</td><td>B/W, B/L, B/G, B/Y</td><td>B/W, B/L, B/G, B/Y</td></tr></table>

The foreground and background color combinations were white/black (W/B), white/blue (W/L), white/green (W/G), and white/yellow (W/Y) for group 1; and black/white (B/W), black/blue (B/L), black/green (B/G), and black/yellow (B/Y) for group 2. The real colors were shown in each cell.

Groups 3 and 4 were used to test the major impact of chroma contrast between the fore- and background, while the luminance levels for the foreground and background remained the same. In group 3 the foreground chroma level was set higher than the background chroma level and in group 4 the foreground chroma level was set lower than the background chroma level.

Thirty-six selections from newspapers were used as reading tasks. The stories were adjusted to have similar length and content complexity. They were then displayed with the various combinations of color, luminance, and chroma levels. For each case, users were asked to read the full story; they were then given a follow-up test to determine their reading effectiveness.

Table 4  
Experimental design for the luminance effect

<table><tr><td rowspan="2"></td><td colspan="6">Group 1: FL &gt; BL</td><td colspan="6">Group 2: FL &lt; BL</td></tr><tr><td colspan="2">N8/N5</td><td colspan="2">N8/N2</td><td colspan="2">N5/N2</td><td colspan="2">N5/N8</td><td colspan="2">N2/N8</td><td colspan="2">N2/N5</td></tr><tr><td rowspan="2">High chroma (S8/S8)</td><td>W/B</td><td>W/L</td><td>W/B</td><td>W/L</td><td>W/B</td><td>W/L</td><td>B/W</td><td>B/L</td><td>B/W</td><td>B/L</td><td>B/W</td><td>B/L</td></tr><tr><td>W/G</td><td>W/Y</td><td>W/G</td><td>W/Y</td><td>W/G</td><td>W/Y</td><td>B/G</td><td>B/Y</td><td>B/G</td><td>B/Y</td><td>B/G</td><td>B/Y</td></tr><tr><td rowspan="2">Medium chroma (S5/S5)</td><td>W/B</td><td>W/L</td><td>W/B</td><td>W/L</td><td>W/B</td><td>W/L</td><td>B/W</td><td>B/L</td><td>B/W</td><td>B/L</td><td>B/W</td><td>B/L</td></tr><tr><td>W/G</td><td>W/Y</td><td>W/G</td><td>W/Y</td><td>W/G</td><td>W/Y</td><td>B/G</td><td>B/Y</td><td>B/G</td><td>B/Y</td><td>B/G</td><td>B/Y</td></tr><tr><td rowspan="2">Low chroma (S3/S3)</td><td>W/B</td><td>W/L</td><td>W/B</td><td>W/L</td><td>W/B</td><td>W/L</td><td>B/W</td><td>B/L</td><td>B/W</td><td>B/L</td><td>B/W</td><td>B/L</td></tr><tr><td>W/G</td><td>W/Y</td><td>W/G</td><td>W/Y</td><td>W/G</td><td>W/Y</td><td>B/G</td><td>B/Y</td><td>B/G</td><td>B/Y</td><td>B/G</td><td>B/Y</td></tr></table>

Table 5  
Experimental design for the chroma effect

<table><tr><td rowspan="3">F/B luminance</td><td colspan="7">F/B chroma</td></tr><tr><td colspan="3">Group 3: FC &gt; BC</td><td colspan="4">Group 4: FC &lt; BC</td></tr><tr><td>S8/S5</td><td>S8/S3</td><td>S5/S3</td><td>S5/S8</td><td>S3/S8</td><td>S3/S5</td><td></td></tr><tr><td>High luminance (N7/N7)</td><td>Y/L, L/Y, R/G, L/G</td><td>Y/L, L/Y, R/G, L/G</td><td>Y/L, L/Y, R/G, L/G</td><td>Y/L, L/Y, R/G, L/G</td><td>Y/L, L/Y, R/G, L/G</td><td>Y/L, L/Y, R/G, L/G</td><td>Y/L, L/Y, R/G, L/G</td></tr><tr><td>Medium luminance (N5/N5)</td><td>Y/L, L/Y, R/G, L/G</td><td>Y/L, L/Y, R/G, L/G</td><td>Y/L, L/Y, R/G, L/G</td><td>Y/L, L/Y, R/G, L/G</td><td>Y/L, L/Y, R/G, L/G</td><td>Y/L, L/Y, R/G, L/G</td><td>Y/L, L/Y, R/G, L/G</td></tr><tr><td>Low luminance (N3/N3)</td><td>Y/L, L/Y, R/G, L/G</td><td>Y/L, L/Y, R/G, L/G</td><td>Y/L, L/Y, R/G, L/G</td><td>Y/L, L/Y, R/G, L/G</td><td>Y/L, L/Y, R/G, L/G</td><td>Y/L, L/Y, R/G, L/G</td><td>Y/L, L/Y, R/G, L/G</td></tr></table>

The foreground and background color combinations for groups 3 and 4 were: yellow/blue (Y/L), blue/yellow (L/Y), red/green (R/G), and blue/green (L/G).

Table 6  
Experimental design for the chroma effect

<table><tr><td rowspan="2"></td><td colspan="6">Group 1: FC &gt; BC</td><td colspan="6">Group 2: FC &lt; BC</td></tr><tr><td colspan="2">S8/S5</td><td colspan="2">S8/S3</td><td colspan="2">S5/S3</td><td colspan="2">S5/S8</td><td colspan="2">S3/S8</td><td colspan="2">S3/S5</td></tr><tr><td rowspan="2">High luminance (N7/N7)</td><td>Y/L</td><td>L/Y</td><td>Y/L</td><td>L/Y</td><td>Y/L</td><td>L/Y</td><td>Y/L</td><td>L/Y</td><td>Y/L</td><td>L/Y</td><td>Y/L</td><td>L/Y</td></tr><tr><td>R/G</td><td>L/G</td><td>R/G</td><td>L/G</td><td>R/G</td><td>L/G</td><td>R/G</td><td>L/G</td><td>R/G</td><td>L/G</td><td>R/G</td><td>L/G</td></tr><tr><td rowspan="2">Medium luminance (N5/N5)</td><td>Y/L</td><td>L/Y</td><td>Y/L</td><td>L/Y</td><td>Y/L</td><td>L/Y</td><td>Y/L</td><td>L/Y</td><td>Y/L</td><td>L/Y</td><td>Y/L</td><td>L/Y</td></tr><tr><td>R/G</td><td>L/G</td><td>R/G</td><td>L/G</td><td>R/G</td><td>L/G</td><td>R/G</td><td>L/G</td><td>R/G</td><td>L/G</td><td>R/G</td><td>L/G</td></tr><tr><td rowspan="2">Low luminance (N3/N3)</td><td>Y/L</td><td>L/Y</td><td>Y/L</td><td>L/Y</td><td>Y/L</td><td>L/Y</td><td>Y/L</td><td>L/Y</td><td>Y/L</td><td>L/Y</td><td>Y/L</td><td>L/Y</td></tr><tr><td>R/G</td><td>L/G</td><td>R/G</td><td>L/G</td><td>R/G</td><td>L/G</td><td>R/G</td><td>L/G</td><td>R/G</td><td>L/G</td><td>R/G</td><td>L/G</td></tr></table>

Reading speed was measured in terms of the time spent on the text and each test case had five yes/no questions. All test materials were from the case content. For each, the reading time data was considered valid only if at least three of the five answers were correct. On average, 92% of the questions are correct. Users were asked to give a visual preference score for each color combination case. The visual preference scores ranged from 1 to 7, where a score of 1 indicated extremely unfavorable and 7 indicated extremely favorable. A score of 4 was, of course, neutral.

## 3.3. Subjects and procedure

Computer software was developed to model the environment and used to elicit and record the subjects reading performance. Prior to conducting the experiment, several preliminary versions of the experimental software were tested to gauge the clarity of the instructions, proper working of the software, adequacy of the user interface and the time required to complete the experimental tasks. Feedback from this pre-test served as a basis for correcting, refining, enhancing, and extending the software and the experiment tasks.

Participation in the experiment was voluntary; 136 undergraduate students majoring in business computing participated in it. After agreeing to help, the student was told that there was a small incentive [26]: a payment would be made to each subject based on his or her task performance, gauged in terms of the reading speed, accuracy, completeness, and care displayed by the subject’s response. The maximum payoff that could be achieved was \$150 NTD (less than \$5 US) for about 1 h work.

All participants were experienced in the use of computer systems. They were randomly assigned to one of four groups, each of 34 students. All participated in a training session, which consisted of an introduction to the intent of the experiment and discussed the software used. A short practice session concluded the training.

All then performed the same generic task, but with different highlighting and color combinations; thus each subject performed two sets of tasks. In the first, each group performed the same table search task with different sets of highlighting conditions. In the second set, each group performed the same text reading task, but with different levels of chroma, luminance, and hue combinations. Fig. 4 shows the experimental procedure.

## 4. Experimental results

## 4.1. Results of experiment I

The data set for the highlighting experiment was analyzed using ANOVA for multi factor analysis. Those conditions found to have significant effect were then tested using Tukey’s student range (HSD). Results were reported at significance levels of 0.01, 0.05, or 0.1, and are tagged with asterisks ( ), ( ), and ( ), respectively, in all results (see the relevant table).

The empirical evidence indicated that the tabular format, display position and highlighting condition significantly affected the subject’s table search performance. Test statistics are shown in Table 7. The ANOVA test rejected the null hypotheses of H1a, H1b, and H1c accepting the alternative hypotheses at $\alpha = 0 . 0 1$

Table 8  
![](/api/attachments/HZ6JWV33/fulltext/images/b6cf85d1ad3570b9485812eef0ceabc427581fe2087d07cd63f15407a2622998.jpg)  
Fig. 4. The procedure of the experiment.

Table 7  
ANOVA analysis on the impact on searching time

<table><tr><td>Factor</td><td>DF</td><td>ANOVA SS</td><td>Mean square</td><td>F-value</td><td>P-value</td></tr><tr><td>Tabular form type</td><td>3</td><td>517.30</td><td>172.43</td><td>47.66</td><td>0.000***</td></tr><tr><td>Display position</td><td>3</td><td>71.12</td><td>23.71</td><td>6.55</td><td>0.000***</td></tr><tr><td>Highlighting condition</td><td>3</td><td>2530.61</td><td>843.56</td><td>8.63</td><td>0.000***</td></tr></table>

Significantly different at 0.01 level.

## 4.1.1. The effect of tabular format

Tukey’s student range analysis (a ¼ 0:05) indicated that tabular format significantly affected the subject reading performance. Results suggest that two of the types (III and IV) result in slower, but similar reading speeds then the others. It seems therefore that the four tabular types may be classified into three groups, as shown in Table 8. The reading performance for tabular form type in decreasing order is then: groups C, B, and A. That is, performance with no lines or both column and row lines is better than that that with only column or only row lines.

## 4.1.2. The effect of display position

Tukey’s student range analysis $( \alpha = 0 . 0 5 )$ for the results indicated that display position significantly affected a subject’s reading performance. The four display positions may be classified into two groups (as seen in Table 9): group A (the lower positions: 8 and 6); and group B (the higher positions: 2 and 4). The performance when the search material was in the higher positions (upper CRT portion) was better. This finding is consistent with the normal eye movement; people tend to scan from top-to-bottom.

The tabular form type analysis

<table><tr><td>Tukey&#x27;s grouping</td><td>Reading speed</td><td>Tabular form type</td></tr><tr><td>A</td><td>8.30</td><td>I</td></tr><tr><td>B</td><td>7.11</td><td>II</td></tr><tr><td>C</td><td>5.77</td><td>IV</td></tr><tr><td>C</td><td>5.77</td><td>III</td></tr></table>

Table 9  
The display position analysis

<table><tr><td>Tukey&#x27;s grouping</td><td>Reading speed</td><td>Display position</td></tr><tr><td>A</td><td>7.16</td><td>8</td></tr><tr><td>A</td><td>7.09</td><td>6</td></tr><tr><td>B</td><td>6.43</td><td>2</td></tr><tr><td>B</td><td>6.27</td><td>4</td></tr></table>

Table 10  
The highlight condition analysis

<table><tr><td>Tukey&#x27;s grouping</td><td>Reading speed</td><td>Highlighting condition</td></tr><tr><td>A</td><td>10.75</td><td>Without highlighting</td></tr><tr><td>B</td><td>5.84</td><td>Blinking</td></tr><tr><td>B, C</td><td>5.40</td><td>Reverse video</td></tr><tr><td>C</td><td>4.97</td><td>Color</td></tr></table>

## 4.1.3. The effect of highlighting

Tukey’s student range analysis (a ¼ 0:05) indicated that the highlighting condition significantly affected the subject’s reading performance. The four highlight conditions can be classified into three groups (as shown in Table 10): group A (without highlighting) is slow; group B (blinking and reverse video) is faster but comparable; and group C (reverse video and color) is fastest. A substantial difference occurs between reading uniform versus highlighted text of any type (about twice as slow). The colored condition was superior.

## 4.2. Results of experiment II

The data set for experiment II was analyzed using ANOVA for multi factor analysis within each group followed by Student’s t-tests between the groups. Results were reported at significance levels of 0.01, 0.05, or 0.1, represented by asterisks ( ), ( ), and ( ), respectively, in the relevant tables. The statistical test rejected all of the null hypotheses for H2a, H2b, and H2c; and accepted the alternative hypotheses at a level of $\alpha = 0 . 0 1$

## 4.2.1. The effect of luminance

First we investigated differences in results between group 1 (foreground luminance, FL > background luminance, BL) and group 2 (the reverse, FL < BL). The contrast between the foreground and background luminance significantly affected the subject’s reading speed and visual preference. The mean and standard deviation (in parentheses) for reading time and visual preference for different luminance combinations are shown in Tables 11 and 12. To test the difference in mean reading time and visual preference, a Student’s ttest was performed for each row and an ANOVA test for each column.

Table 11  
The luminance contrast impact on reading speed

<table><tr><td colspan="2">Group 1: FL &gt; BL</td><td colspan="2">Group 2: FL &lt; BL</td><td rowspan="2">t-test of difference (N1/N2 = 408)</td></tr><tr><td>F/B luminance</td><td>Reading time</td><td>F/B luminance</td><td>Reading time</td></tr><tr><td>N8/N5</td><td>58.49(25.49)</td><td>N5/N8</td><td>53.25(19.94)</td><td> $t = 3.28$  $P = 0.001^{***}$ </td></tr><tr><td>N8/N2</td><td>53.83(20.89)</td><td>N2/N8</td><td>52.05(17.97)</td><td> $t = 1.31$  $P = 0.191$ </td></tr><tr><td>N5/N2</td><td>52.96(16.85)</td><td>N2/N5</td><td>52.46(17.69)</td><td> $t = 0.41$  $P = 0.68$ </td></tr><tr><td>ANOVA</td><td></td><td>ANOVA</td><td></td><td></td></tr><tr><td> $F = 13.60$ </td><td></td><td> $F = 0.91$ </td><td></td><td></td></tr><tr><td> $P = 0.000^{***}$ </td><td></td><td> $P = 0.41$ </td><td></td><td></td></tr></table>

\*\*\* Significantly different at 0.01 level.

Table 12  
The luminance contrast impact on visual preference

<table><tr><td colspan="2">Group 1: FL &gt; BL</td><td colspan="2">Group 2: FL &lt; BL</td><td rowspan="2">t-test of difference (N1/N2 = 408)</td></tr><tr><td>F/B luminance</td><td>Visual preference</td><td>F/B luminance</td><td>Visual preference</td></tr><tr><td>N8/N5</td><td>3.86(1.44)</td><td>N5/N8</td><td>3.61(0.93)</td><td> $t = 2.92$  $P = 0.002^{***}$ </td></tr><tr><td>N8/N2</td><td>5.05(0.99)</td><td>N2/N8</td><td>4.43(0.92)</td><td> $t = 9.30$  $P = 0.000^{***}$ </td></tr><tr><td>N5/N2</td><td>3.85(1.02)</td><td>N2/N5</td><td>3.46(1.14)</td><td> $t = 5.06$  $P = 0.000^{***}$ </td></tr><tr><td>ANOVA</td><td></td><td>ANOVA</td><td></td><td></td></tr><tr><td> $F = 118.54$  $P = 0.000^{***}$ </td><td></td><td> $F = 105.34$  $P = 0.000^{***}$ </td><td></td><td></td></tr></table>

\*\*\* Significantly different at 0.01 level.

For each row in Table 11, comparison of pairs of foreground/background (F/B) luminance level combinations show that reading speed was higher for $\mathrm { F L } < \mathbf { B L }$ than for $\mathrm { F L } > \mathrm { B L }$ . However, though a two-sample Student’s t-test showed that N5/N8 was significantly better than N8/N5, this was not true for the other two, i.e. they did not have a significant difference. Also, for its columns, an ANOVA test showed that when $\mathrm { F L } > \mathrm { B L }$ , different F/B luminance combinations significantly affect reading performance. Tukey’s student range analysis $( \alpha = 0 . 0 5 )$ indicated that the reading performance for N8/N2 or N5/N2 was better than N8/N5. But for the case of $\mathrm { F L } < \mathbf { B L }$ , ANOVA test showed that different F/B luminance combinations did not have significant impact on reading performance. Finally, among all F/B luminance combinations we can see that the average reading time for N8/N5 was the worst. Apparently, a high luminance foreground (N8) is difficult to read when the background luminance (N5) is not sufficiently low.

Similar analysis was performed on results of visual preference in Table 12. One may expect that the impact on reading speed will very similar to that on visual preference: if a person feels happy or satisfied when reading, he or she might be expected to read quickly. However, the test data did not show any such consistency. For instance, for F/B luminance ¼ N2/N5, the reading speed was nearly the fastest, but the visual preference was the worst. For F/B luminance ¼ N8/ N5, both the comfort and speed were bad. However, we did find that the N8/N2 and N2/N8 comparison does provide an example of both high visual preference and fast reading.

## 4.2.2. The side effect of background chroma level

Within and between groups 1 and 2, we further studied the impact of background chroma level. Here the foreground color was either black or white, thus its chroma ¼ S0, i.e. there is no color.

Along each row of Table 13, the two-sample Student’s t-test showed that, for each equal background chroma level, the $\mathrm { F L } < \mathbf { B L }$ group was always faster in reading than the FL > BL group, i.e. the background chroma level did not affect the relative advantage of the F/B luminance contrast. Down each column, an ANOVA test showed that only when $\mathrm { F L } > \mathrm { B L }$ , did the background chroma level affect reading performance. Tukey’s student range analysis $( \alpha = 0 . 0 5 )$ indicated that the performance for lower or median background chroma level (S2 or S5) was better than that for high chroma level (S8).

The impact on visual preference is shown in Table 14. It was interesting to see that in general the preference level was higher, but the reading speed was lower for the $\mathrm { F L } > \mathrm { B L }$ group than for the $\mathrm { F L } > \mathrm { B L }$ group. But within the $\mathrm { F L } > \mathrm { B L }$ group, S0/S2 and S0/S5 were preferred more than S0/S8 in both visual preference and reading speed. In the

Table 14  
Table 13  
The chroma level side effect on reading speed

<table><tr><td colspan="2">Group 1: FL &gt; BL</td><td colspan="2">Group 3: FL &lt; BL</td><td rowspan="2">t-test of difference (N1/N2 = 408)</td></tr><tr><td>F/B chroma</td><td>Reading time</td><td>F/B chroma</td><td>Reading time</td></tr><tr><td>S0/S8</td><td>58.09(24.62)</td><td>S0/S8</td><td>54.02(18.92)</td><td> $t = 2.65$  $P = 0.008^{***}$ </td></tr><tr><td>S0/S5</td><td>53.84(19.85)</td><td>S0/S5</td><td>51.56(18.71)</td><td> $t = 1.69$  $P = 0.091^{*}$ </td></tr><tr><td>S0/S2</td><td>53.35(19.32)</td><td>S0/S2</td><td>52.18(17.97)</td><td> $t = 0.90$  $P = 0.369$ </td></tr><tr><td>ANOVA</td><td></td><td>ANOVA</td><td></td><td></td></tr><tr><td> $F = 8.60$  $P = 0.001^{***}$ </td><td></td><td> $F = 1.90$  $P = 0.159$ </td><td></td><td></td></tr></table>

\* Significantly different at 0.1 level.  
冰率\* Significantly different at 0.01 level.

FL < BL group, the chroma level did not make difference in both visual preference and reading speed.

## 4.2.3. The effect of chroma contrast

We next investigated the difference between the results of chroma contrast tests of group 3, where the foreground chroma ðFCÞ > background chroma (BC); and group 4, where FC < BC. The mean and standard deviation (in parentheses) for reading time and visual preference for various chroma combinations are shown in Tables 15 and 16. To test the difference in mean reading time, and visual preference, we performed a Student’s t-test for each row and an ANOVA test for each column. Along each row, the reading speed was higher for the FC < BC group than for FC > BC group. A two-sample Student’s t-test showed that S5/S8 was significantly better than S8/S5, S2/S8 was better than S8/S2, and S2/S5 was better than S5/S2. However, within each group in the same column, the ANOVA showed that the variation in chroma levels did not affect the subjects’ reading speed.

The impact on visual preference, however, was different. The visual preference was lower for the FC > BC group than for the FC < BC group. Within each group, the ANOVA showed that the variation in chroma levels did affect the subjects’ visual preference. The F/B chroma of S8/S5 was given the highest visual preference, but resulted in the slowest reading speed. No chroma choice was both preferred and provided a faster reading result.

The chroma level side effect on visual preference

<table><tr><td colspan="2">Group 1: FL &gt; BL</td><td colspan="2">Group 2: FL &lt; BL</td><td rowspan="2">t-test of difference (N1/N2 = 408)</td></tr><tr><td>F/B chroma</td><td>Visual preference</td><td>F/B chroma</td><td>Visual preference</td></tr><tr><td>S8/S8</td><td>3.90(1.51)</td><td>S8/S8</td><td>3.84(1.21)</td><td> $t = 0.63$  $P = 0.526$ </td></tr><tr><td>S5/S5</td><td>4.38(1.20)</td><td>S5/S5</td><td>3.87(1.05)</td><td> $t = 6.43$  $P = 0.000^{***}$ </td></tr><tr><td>S2/S2</td><td>4.38(1.11)</td><td>S2/S2</td><td>3.80(0.97)</td><td> $t = 8.06$  $P = 0.000^{***}$ </td></tr><tr><td>ANOVA</td><td></td><td>ANOVA</td><td></td><td></td></tr><tr><td> $F = 16.54$  $P = 0.000^{***}$ </td><td></td><td> $F = 0.50$  $P = 0.606$ </td><td></td><td></td></tr></table>

Significantly different at 0.01 level.

Table 16  
Table 15  
The chroma contrast impact on reading speed

<table><tr><td colspan="2">Group 3: FC &gt; BC</td><td colspan="2">Group 4: FC &lt; BC</td><td rowspan="2">t-test of difference (N1/N2 = 408)</td></tr><tr><td>F/B chroma</td><td>Reading time</td><td>F/B chroma</td><td>Reading time</td></tr><tr><td>S8/S5</td><td>60.77(32.58)</td><td>S5/S8</td><td>53.88(19.72)</td><td> $t = 3.65$  $P = 0.000^{***}$ </td></tr><tr><td>S8/S2</td><td>59.01(19.97)</td><td>S2/S8</td><td>53.83(18.34)</td><td> $t = 3.87$  $P = 0.000^{***}$ </td></tr><tr><td>S5/S2</td><td>58.50(19.06)</td><td>S2/S5</td><td>52.84(17.49)</td><td> $t = 4.42$  $P = 0.000^{***}$ </td></tr><tr><td>ANOVA</td><td></td><td>ANOVA</td><td></td><td></td></tr><tr><td> $F = 1.53$ </td><td></td><td> $F = 1.00$ </td><td></td><td></td></tr><tr><td> $P = 0.226$ </td><td></td><td> $P = 0.376$ </td><td></td><td></td></tr></table>

\*\*\* Significantly different at 0.01 level.

## 4.2.4. The side effect of luminance level

The luminance level significantly affected the subjects’ reading speed and visual preference when both the foreground and background luminance were set at the same level. Along each row in Table 17, a twosample Student’s t-test showed that FC < BC was always significantly better than FC > BC for each F/B luminance level, i.e. when the F/B luminance levels are the same, they have no effect on the relative advantage of the F/B chroma. Along each column, the ANOVA test also showed that the luminance level significantly affected reading performance for cases where the FC level was either greater or lower than the BC level. Tukey’s student range analysis $( \alpha = 0 . 0 5 )$ indicated that the performance in decreasing order was N5/N5, N3/N3, N7/N7. The median luminance level seemed to be best.

We similarly analyzed the impact on visual preference, as shown in Table 18. The F/B luminance of N5/N5 produced both the highest preference and the fastest reading speed for both the FC > BC and FC < BC groups. However, the preference was higher, but the reading speed was lower for the $\mathrm { F C } > \mathrm { B C }$ group. The best choice for both preference and speed should be for an F/B luminance of N5/N5 with $\mathrm { F C } < \mathrm { B C } .$

The chroma contrast impact on visual preference

<table><tr><td colspan="2">Group 3: FC &gt; BC</td><td colspan="2">Group 4: FC &lt; BC</td><td rowspan="2">t-test of difference (N1/N2 = 408)</td></tr><tr><td>F/B chroma</td><td>Visual preference</td><td>F/B chroma</td><td>Visual preference</td></tr><tr><td>S8/S5</td><td>4.25(1.25)</td><td>S5/S8</td><td>3.73(1.49)</td><td> $t = 5.39$  $P = 0.000^{***}$ </td></tr><tr><td>S8/S2</td><td>4.07(1.16)</td><td>S2/S8</td><td>3.54(1.42)</td><td> $t = 5.79$  $P = 0.000^{***}$ </td></tr><tr><td>S5/S2</td><td>3.49(1.28)</td><td>S2/S5</td><td>3.08(1.42)</td><td> $t = 4.37$  $P = 0.000^{***}$ </td></tr><tr><td>ANOVA</td><td></td><td>ANOVA</td><td></td><td></td></tr><tr><td> $F = 39.27$  $P = 0.000^{***}$ </td><td></td><td> $F = 19.94$  $P = 0.000^{***}$ </td><td></td><td></td></tr></table>

\*\*\* Significantly different at 0.01 level.

Table 17  
The luminance level side effect on reading speed

<table><tr><td colspan="2">Group 3: FC &gt; BC</td><td colspan="2">Group 4: FC &lt; BC</td><td rowspan="2">t-test of difference (N1/N2 = 408)</td></tr><tr><td>F/B luminance</td><td>Reading time</td><td>F/B luminance</td><td>Reading time</td></tr><tr><td>N7/N7</td><td>62.80(32.53)</td><td>N7/N7</td><td>57.41(19.24)</td><td> $t = 2.88$  $P = 0.004^{***}$ </td></tr><tr><td>N5/N5</td><td>56.16(18.41)</td><td>N5/N5</td><td>51.78(18.34)</td><td> $t = 3.41$  $P = 0.001^{***}$ </td></tr><tr><td>N3/N3</td><td>59.32(20.18)</td><td>N3/N3</td><td>51.36(16.49)</td><td> $t = 6.17$  $P = 0.000^{***}$ </td></tr><tr><td>ANOVA</td><td></td><td>ANOVA</td><td></td><td></td></tr><tr><td> $F = 5.26$  $P = 0.008^{***}$ </td><td></td><td> $F = 12.73$  $P = 0.000^{***}$ </td><td></td><td></td></tr></table>

\*\*\* Significantly different at 0.01 level.

## 4.2.5. The effect of hue

Two reading tests were performed to help understand the effect of hue. The first had a combination of either a black or white foreground and a different hue as background; this test was performed with both greater and less foreground to background luminance. The second used a combination of different hues in the foreground and background; to this was added chroma variation.

4.2.5.1. Test 1. The test statistics for reading time and visual preference for this test set are shown in Tables 19 and 20. Along each column of the first, an ANOVA test showed that the hue combination significantly affected the subjects’ reading speed for both groups if the foreground luminance level was greater or less than that of the background. Among the four hue combinations examined, the best combination was white/blue for ${ \mathrm { F L } } > { \mathrm { B L } } ,$ and black/green for $\mathrm { F L } < \mathbf { B L }$ . White/black and black/ white did not perform well compared to the other color backgrounds. White/yellow was the worst, because white fonts are difficult to recognize even on a dark yellow background. Along each row of this

The luminance level side effect on visual preference

<table><tr><td colspan="2">Group 3: FC &gt; BC</td><td colspan="2">Group 4: FC &lt; BC</td><td rowspan="2">t-test of difference (N1/N2 = 408)</td></tr><tr><td>F/B luminance</td><td>Visual preference</td><td>F/B luminance</td><td>Visual preference</td></tr><tr><td>N7/N7</td><td>3.17(1.19)</td><td>N7/N7</td><td>2.67(1.35)</td><td> $t = 5.63$  $P = 0.000^{***}$ </td></tr><tr><td>N5/N5</td><td>4.69(1.07)</td><td>N5/N5</td><td>4.06(1.34)</td><td> $t = 7.49$  $P = 0.000^{***}$ </td></tr><tr><td>N3/N3</td><td>3.94(1.08)</td><td>N3/N3</td><td>3.65(1.35)</td><td> $t = 3.35$  $P = 0.001^{***}$ </td></tr><tr><td>ANOVA</td><td></td><td>ANOVA</td><td></td><td></td></tr><tr><td> $F = 176.25$  $P = 0.000^{***}$ </td><td></td><td> $F = 104.68$  $P = 0.000^{***}$ </td><td></td><td></td></tr></table>

Significantly different at 0.01 level.

Table 19  
The effect of hue with different luminance contrast on reading speed

<table><tr><td colspan="2">Group 1: FL &gt; BL</td><td colspan="2">Group 2: FL &lt; BL</td><td rowspan="2">t-test of difference (N1/N2 = 306)</td></tr><tr><td>Hue combinations</td><td>Reading time</td><td>Hue combinations</td><td>Reading time</td></tr><tr><td>White/black</td><td>56.39(19.20)</td><td>Black/white</td><td>55.50(19.94)</td><td> $t = 0.56$  $P = 0.57$ </td></tr><tr><td>White/blue</td><td>53.27(19.57)</td><td>Black/blue</td><td>52.71(17.58)</td><td> $t = 0.37$  $P = 0.71$ </td></tr><tr><td>White/green</td><td>54.00(20.50)</td><td>Black/green</td><td>50.93(17.29)</td><td> $t = 2.00$  $P = 0.045^{**}$ </td></tr><tr><td>White/yellow</td><td>56.72(25.89)</td><td>Black/yellow</td><td>51.20(19.01)</td><td> $t = 3.00$  $P = 0.003^{***}$ </td></tr><tr><td>ANOVA</td><td></td><td>ANOVA</td><td></td><td></td></tr><tr><td> $F = 9.92$ </td><td></td><td> $F = 11.77$ </td><td></td><td></td></tr><tr><td> $P = 0.000^{***}$ </td><td></td><td> $P = 0.000^{***}$ </td><td></td><td></td></tr></table>

\*\* Significantly different at 0.05 level.  
\*\*\* Significantly different at 0.01 level.

table, a Student’s t-test showed that for different background colors, $\mathrm { F L } < \mathrm { B I }$ was the same or better than FL > BL. The most significant difference was between white/yellow and black/yellow. It was also interesting to see that there was no significant performance difference between white/black and black/white. It is also important to note that white and black could be represented in different degrees of gray, based on the luminance level.

Visual preference results were again inconsistent with those from reading speed. The greatest difference in visual preference was between white/blue and black/blue; however, no statistical differences was found in their reading speeds. Visually white/black was preferred over black/white, but the reading time was essentially the same. However, black/yellow was, not surprisingly, better than white/yellow for both visual preference and reading speed. The best for both visual preference and reading speed was white/blue, followed by black/green.

Table 20  
The effect of hue with different luminance contrast on visual preference

<table><tr><td colspan="2">Group 3: FL &gt; BL</td><td colspan="2">Group 4: FL &lt; BL</td><td rowspan="2">t-test of difference (N1/N2 = 306)</td></tr><tr><td>Hue combinations</td><td>Visual preference</td><td>Hue combinations</td><td>Visual preference</td></tr><tr><td>White/black</td><td>4.29(1.02)</td><td>Black/white</td><td>3.81(0.98)</td><td> $t = 5.92$  $P = 0.000^{***}$ </td></tr><tr><td>White/blue</td><td>4.69(1.18)</td><td>Black/blue</td><td>3.38(1.32)</td><td> $t = 13.00$  $P = 0.000^{***}$ </td></tr><tr><td>White/green</td><td>4.06(1.40)</td><td>Black/green</td><td>4.10(0.92)</td><td> $t = 0.43$  $P = 0.334$ </td></tr><tr><td>White/yellow</td><td>3.83(1.41)</td><td>Black/yellow</td><td>4.07(0.91)</td><td> $t = 2.47$  $P = 0.007^{**}$ </td></tr><tr><td>ANOVA</td><td></td><td>ANOVA</td><td></td><td></td></tr><tr><td> $F = 29.86$ </td><td></td><td> $F = 22.45$ </td><td></td><td></td></tr><tr><td> $P = 0.000^{***}$ </td><td></td><td> $P = 0.000^{***}$ </td><td></td><td></td></tr></table>

\*\* Significantly different at 0.05 level.  
\*\*\* Significantly different at 0.01 level.

Table 22  
Table 21  
The effect of hue with different chroma contrast on reading speed

<table><tr><td colspan="2">Group 3: FC &gt; BC</td><td colspan="2">Group 4: FC &lt; BC</td><td rowspan="2">t-test of difference (N1/N2 = 306)</td></tr><tr><td>Color combinations</td><td>Reading time</td><td>Color combinations</td><td>Reading time</td></tr><tr><td>Yellow/blue</td><td>58.59(20.11)</td><td>Yellow/blue</td><td>54.20(16.92)</td><td> $t = 2.92$  $P = 0.004^{***}$ </td></tr><tr><td>Blue/yellow</td><td>62.54(34.92)</td><td>Blue/yellow</td><td>55.02(19.46)</td><td> $t = 3.29$  $P = 0.001^{***}$ </td></tr><tr><td>Red/green</td><td>59.40(21.78)</td><td>Red/green</td><td>53.04(19.51)</td><td> $t = 3.81$  $P = 0.000^{***}$ </td></tr><tr><td>Blue/green</td><td>57.15(17.83)</td><td>Blue/Green</td><td>51.80(17.99)</td><td> $t = 3.70$  $P = 0.000^{***}$ </td></tr><tr><td>ANOVA</td><td></td><td>ANOVA</td><td></td><td></td></tr><tr><td> $F = 5.44$  $P = 0.001^{***}$ </td><td></td><td> $F = 7.79$  $P = 0.000^{***}$ </td><td></td><td></td></tr></table>

\*\*\* Significantly different at 0.01 level.

4.2.5.2. Test 2. For the second set of hue comparison, the test statistics are shown in Tables 21 and 22. The ANOVA test showed that the color combination significantly affected the subjects’ reading speed for both groups when the FC level was greater or less than the BC level. Blue/green was the best when FC < BC and blue/yellow was the worst when FC > BC.

Along each row, the Student’s t-test showed that, for different hue combinations, reading speed for FC < BC was consistently better than FC > BC. Thus the hue combination did not change the dominant chroma contrast impact.

The effect of hue with different chroma contrast on visual preference

<table><tr><td colspan="2">FC &gt; BC</td><td colspan="2">FC &lt; BC</td><td rowspan="2">t-test of difference (N1/N2 = 306)</td></tr><tr><td>Color combinations</td><td>Visual preference</td><td>Color combinations</td><td>Visual preference</td></tr><tr><td>Yellow/blue</td><td>4.34(1.21)</td><td>Yellow/blue</td><td>3.13(1.60)</td><td> $t = 10.49$  $P = 0.000^{***}$ </td></tr><tr><td>Blue/yellow</td><td>4.04(1.14)</td><td>Blue/yellow</td><td>3.75(1.42)</td><td> $t = 2.77$  $P = 0.003^{***}$ </td></tr><tr><td>Red/green</td><td>3.51(1.34)</td><td>Red/green</td><td>3.46(1.44)</td><td> $t = 0.47$  $P = 0.320$ </td></tr><tr><td>Blue/green</td><td>3.84(1.25)</td><td>Blue/green</td><td>3.46(1.33)</td><td> $t = 3.62$  $P = 0.000^{***}$ </td></tr><tr><td>ANOVA</td><td></td><td>ANOVA</td><td></td><td></td></tr><tr><td> $F = 21.84$  $P = 0.000^{***}$ </td><td></td><td> $F = 8.37$  $P = 0.000^{***}$ </td><td></td><td></td></tr></table>

Significantly different at 0.01 level.

The visual preference results were found to be opposite to those from the reading speed test: the ANOVA test showed that the color combination significantly affected the subjects’ visual preference in each group. Blue/yellow was visually preferred, but the reading speed was slower than for red/green. Along each row, the Student’s t-test showed that, for different hue combinations, the visual preference for FC < BC was consistently worse than for FC > BC: thus the hue combination did not change the dominant chroma contrast impact on visual preference.

## 5. Conclusion and implications

## 5.1. Highlighting impact

Our empirical evidence indicated that the type of tabular format, display position, and highlighting condition affected the user search response time (i.e. in reading a target option).

(1) Among the four types of tables, users of a form with or without column and row grid lines had better performance than those with only column or row lines. In terms of the display position, the speed in searches where the result was in the upper part of the CRT outperformed that for the searches in lower.

(2) Among the four highlighting alternatives, the one using color was superior to the others (from a standpoint of reading times), followed by the reverse video and blinking, and that no highlighting was worst. The results were consistent with those found by Fisher and Tan, except that they reversed the last two, i.e. blinking was worst. There may be an explanation for this: in their experiment the display position was known in advance and blinking may have reduced the subject’s reading ability. In contrast, our display position was not fixed and the blinking helps the subject to identify the target quickly, thereby offsetting any side effect of the blinking on reading speed.

## 5.2. Color impact

The empirical evidence indicated that the luminance, chroma, and hue combination significantly affected visual preference and reading speed. This relationships, however, are not simple.

(1) In general, the reading speed was higher, but the visual preference was lower for FL < BL than for FL > BL, regardless of the difference in luminance level, chroma level, and hue combination. This means that: to improve reading speed the foreground should be darker and the background should be lighter (this agrees with Cushman), but to improve visual preference, the foreground should be lighter and the background should be darker.

(2) In general, the reading speed was higher, but the visual preference was lower for FC < BC than for FC > BC, regardless of the differences in luminance level, chroma level, and hue combinations. This means that: to improve reading speed, the foreground color should be less saturated than the background color, but to improve visual preference, the foreground color should be more saturated than the background color.

(3) Different hue combinations did affect the reading speed and visual preference. However, they did not override the dominant impact of relative luminance contrast and chroma contrast between the foreground and background on reading speed and visual preference.

(4) The impact of luminance, chroma, and hue combination on visual preference was not consistent with their impact on reading speed; indeed, sometimes they had the opposite effect. This means that we should select specific combinations in order to improve both visual preference and reading speed. It seems that visual preferences were more subjective and did not necessarily correlate with reading speed. Surprisingly, we have not found literature discussing any relationship between visual preference and reading speed.

## 5.3. Guidelines for designing effective textual displays

In summary, we suggest the following.

(1) Based on the content, select a plain text or tabular form. Menus and sidebar are also tabular forms. For news or other descriptive content, plain text may be better. For items with a similar structure, a tabular form is more appropriate.

![](/api/attachments/HZ6JWV33/fulltext/images/846e137553dbc9fd587ce9ecab1a9f8ff170ff2723642b8d29594564dbf94c70.jpg)  
(b)  
Fig. 5. Homepage of Netscape.com.

(2) In a table, the separation between column, row, or cells depends on the possible search pattern.

If the search is column by column, the columns should be separated.

If the search is row by row, the rows should be separated.

If both column and row searching is necessary, do not use separators or separate the cells by determining first how the cell is best found without the use of separating lines.

Alternatively, different color backgrounds can be used instead of lines to provide soft separation.

(3) In text format, a different background color can be used to group different content. Within each group with the same background color, the color of the font, the luminance level, or the chroma level can be varied to simplify recognition, etc.

## 5.4. A practical example

As an illustration of the guidelines, let us look at the homepage of Netscape.com.

\- Twelve different front and background color combinations were carefully used.

\- The page is divided into several blocks.

\- Background colors are used for grouping. For instance, in Fig. 5a, the top bar, in deep blue, is used to indicate the main menu; the left side grayish bar shows a topic list, and the middle white background is used to show the major stories.

\- On the bottom, different tones of blue are used to show the four most commonly used reference categories (see Fig. 5b).

\- The grouping can be nested. For instance, a small table is used for the stock index.

\- Different color fonts are used for different purposes. For instance, a red font is used for short headings in order to catch the reader’s attention, and deep blue font is used to indicate secondary headings. The white font in the blue background shows the buttons.

\- The font color also has an emotional impact such as a red for warning, pink for love, black for serious business, and green for relaxation, though this is culture dependent and the same text may send different messages to different people internationally. We also see the use of red and green for highlighting the decrease and increase in the stock index in the stock index table.

## Acknowledgements

This research was supported by the National Science Council of Taiwan, under operating grant NSC86-2418-H-110-002. The authors would like to thank Mr. Her-Sen Doong for his assistance in collecting and analyzing data.

## References

[1] N. Archer, M.M. Head, J.P. Wollersheim, Y. Yuan, An investigation of voice and text output modes with information abstraction in a computer interface, Interacting with Computers 8, 1996, pp. 323–345.

[2] A. Cakir, D. Hart, T. Stewart, Visual Display Terminals: A Manual Covering Ergonomics, Workplace Design, Health and Safety, Task Organization, Wiley, New York, 1980.

[3] S.K. Card et al. The Psychology of Human–Computer Interaction, Lawrence Erlbaum, London, 1983.

[4] R.A. Coll, J.H. Coll, G. Thakur, Graphs and tables: a fourfactor experiment, Communications of the ACM 37 (4), 1994, pp. 77–86.

[5] W.H. Cushman, Reading from microfiche, a VDT, and the printed page: subjective fatigue and performance, Human Factors 28, 1986, pp. 63–73.

[6] D.L. Fisher, K.C. Tan, Visual displays: the highlighting paradox, Human Factors 31 (1), 1989, pp. 17–30.

[7] D.L. Fisher, D.G. Coury, T.O. Tengs, S.A. Duffy, Minimizing the time to search visual display: the role of highlighting, Human Factors 31 (2), 1989, pp. 167–182.

[8] W.O. Galitz, in: Proceedings of the Life Office Management Association on Human Factors in Office Automation, Atlanta, 1980.

[9] M.H. Goldhaber, The attention economy and the net, Telepolis, 27.11.1997, http://www.heise.de/tp/english/special/eco/6097/1.html.

[10] B.E. John, D.E. Kieras, Using GOMS for user interface design and evaluation: which technique? ACM Transactions on Computer–Human Interaction 3, 1996, pp. 287–319.

[11] D.E. Kieras, Towards a practical GOMS model methodology for user interface design, in: M. Helander (Ed.), Handbook of Human–Computer Interaction, Elsevier, Amsterdam, 1988, pp. 135–157.

[12] H.D. Lasswell, The structure and function of communication in society, in: L. Bryson (Ed.), The Communication of Ideas, Institute for Religious and Social Studies, 1948, in: J. Hanson, D.J. Maxcy (Eds.), Notable Selections in Mass Media, Guilford, Connecticut, 1996, pp. 22–29 (reprint).

[13] J.V. Lovasik, M.L. Matthews, H. Kergoat, Neural optical, and search performance in prolonged viewing of chromatic displays, Human Factors 31 (3), 1989, pp. 273–289.

[14] L.W. MacDonald, Using color effectively in computer graphics, IEEE Computer Graphics and Applications, July/ August 1999, pp. 20–35.

[15] K. Mathieson, M. Keil, Beyond the interface: ease of use and task/technology fit, Information and Management 34, 1998, pp. 221–230.

[16] M.L. Matthews, The influence of color on CRT reading performance and subjective well-being under operational conditions, Applied Ergonomics 18 (4), 1987, pp. 323–328.

[17] M.L. Matthews, J.V. Lovasik, K. Mertins, Visual performance and subjective discomfort in prolonged viewing of chromatic displays, Human Factors 31 (3), 1989, pp. 259–271.

[18] J. Morrison, D. Vogel, The impacts of presentation visuals on presentation, Information and Management 33, 1998, pp. 125–135.

[19] G.M. Murch, Physiological Principles for the Effective Use of Color, IEEE Computer Graphic and Applications 11 (November 1984) 49–54.

[20] S. Pastoor, Legibility and subjective preference for color combinations in text, Human Factors 32 (2), 1990, pp. 157–171.

[21] U. Pawlak, Ergonomic aspects of image polarity, Behavior and Information Technology 5, 1986, pp. 335–348.

[22] D.L. Post, H.L. Snyder, Color contrast metric complex images, Report HFL/ONR 86-2, Virginia Polytechnic Institute and State University, 1986.

[23] W. Remus, An empirical investigation of the impact of graphical and tabular data presentations of decision making, Management Science 30 (5), 1984, pp. 533–542.

[24] M.S. Sanders, E.J. McCormick, Human Factors in Engineering and Design, 7th ed., McGraw-Hill, New York, 1993.

[25] C.E. Shannon, W. Weaver, The Mathematical Theory of Communication, University of Illinois Press, Urbana, 1949.

[26] V.L. Smith, Experimental economics: induced value theory, American Economics Review 66, 1976, pp. 274–279.

[27] W.D. Thomson, J. Saunders, The perception of flicker on rasterscanned displays, Human Factors 39 (1), 1997, pp. 48–66.

[28] T.S. Tullis, The formatting of alphanumeric displays: a review and analysis, Human Factors 25, 1983, pp. 657–682.

![](/api/attachments/HZ6JWV33/fulltext/images/4e99890788f4832c4105a615d1477a384ab5fd61c5f5b35e003feb6cce86969f.jpg)

Jen-Her Wu is professor of Information Management at National Sun Yat-Sen University. Prior to his doctoral study at the University of Kentucky, he received a BS degree in industrial design, earned an MS degree in computer science and worked as an engineer and manager in the manufacturing industry. Professor Wu teaches a variety of information management courses. His current research interests are in the areas of

information systems development and management, human computer interaction, and knowledge management. His research articles span such diverse journals as Information and Management, Expert Systems, Knowledge Acquisition, Decision Support Systems, Simulation Digest, International Journal of Expert Systems: Research and Applications, International Journal of Intelligent Systems in Accounting, Finance and Management, Journal of Computer Information Systems, and others.

![](/api/attachments/HZ6JWV33/fulltext/images/0a46fa72c3365d06f22dc64195801992f0e6962d36996ba0d776dcf5c6bfe425.jpg)

Yufei Yuan is currently a professor of Information Systems at Michael G. DeGroote School of Business, McMaster University, Canada. He received his PhD in computer information systems from the University of Michigan in US in 1985. His research interests are in the areas of mobile commerce, web-based negotiation support system, business model in electronic commerce, approximate reasoning with fuzzy logic,

matching problem, and decision support in health care. He has published more than 40 papers in professional journals such as International Journal of Electronic Markets, Internet research, Fuzzy Sets and Systems, European Journal of Operational Research, Management Sciences, Academic Medicine, Medical Decision Making, International Journal of Human–Computer Systems, and others.
