---
otero_id: 21109
otero_key: "TCWFMGDZ"
title: "EDGAR-Analyzer: automating the analysis of corporate data contained in the SEC's EDGAR database"
authors: "John Gerdes"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00096-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# EDGAR-Analyzer: automating the analysis of corporate data contained in the SEC’s EDGAR database

John Gerdes Jr.\*

The A. Gary Anderson Graduate School of Management, University of California, Riverside, CA, 92521, USA

## Abstract

Publicly owned companies, their officers and major investors are required to file regular disclosures with the Securities and Exchange Commission (SEC). To improve accessibility to these public documents, the SEC began developed the EDGAR (Electronic Data Gathering, Analysis and Retrieval) electronic disclosure system. This system provides ready, free access to all electronic filings made since 1994. The paper describes a tool that automates the analysis of SEC filings, emphasizing the unstructured text sections of these documents. To illustrate the capabilities of the EDGAR-Analyzer program, results of a largescale case study of corporate Y2K disclosures in 18,595 10K filings made from 1997 to 1999 is presented. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: SEC; EDGAR; Tool; Financial Analysis; Functional decomposition model; Y2K

## 1. Introduction

The recent trend for both the public and private sectors is to make information web-accessible. Putting data on-line leverages the universality of the Internet, improves user access, speeds the dissemination of information, and reduces costs for both the provider and user. The Securities and Exchange Commission (SEC), through its EDGAR (Electronic Data Gathering, Analysis and Retrieval) database initiative, was an early innovator in this area. The importance of the EDGAR database rests in the scope of the data it contains—disclosures of financial and operational performance of all publicly traded companies. It has been argued that under the Freedom of Information Act mandate, the Commission has an obligation to both promote and provide ready access to these documents [25,40].

Since its inception in the mid-1930s, the primary mission of the SEC has been to protect investors and maintain the integrity of securities markets. As part of this effort, domestic, publicly held companies are required to disclose complete and accurate information about their operations, as well as any event that could materially impact them [36]. This required information is extensive. The SEC receives 12 million pages of documents annually [29]. Manual processing of this much information is both expensive and time consuming. Having to physically handle paper filings also limits the timely access to this important, public information.

To address these problems, the SEC began developing the electronic disclosure system in 1983. After initial successful prototyping and testing, the Commission mandated electronic filings in 1994 [33]. Even though these documents were being stored in electronic form, their accessibility was still quite limited. Data was made available through five nationwide SEC reading rooms, and a limited number of private companies (primarily Mead Data Central) which provided on-line, tape, CD-ROM or paper versions of EDGAR Data [21]. A 1993 NSF research project was initiated to investigate the feasibility of disseminating EDGAR data through the Internet. Dubbed EDGAR on the Internet or EOI, this project demonstrated that it was feasible to provide access through electronic mail, ftp, gopher and World Wide Web. In late 1995, the base EDGAR system and technology developed through this project were transferred back to the SEC, which used it as the basis for the own web-based services. Since that time the Commission has continuously improved and expanded the EDGAR System. In May 1999, they started accepting filings submitted in HTML and PDF formats. The EDGAR database has grown to include over 1.7 million documents representing 610 GB of data, ranking it the 25th largest web accessible database [7]. For a more detailed history and development of the EDGAR system, the reader is directed to Refs. [5,20,21,33,35].

EDGAR has become a valuable resource for both investors and the securities markets. Although access has been greatly improved, the ability to automatically analyze these filings is limited due to the semistructured nature of the documents. The SEC requires firms to incorporate SGML tags to facilitate the identification of specific data fields and certain document sections. However, these tags provide direct access to only a small portion of the data contained in these documents. The typical filing consists of two major sections—the SEC Header, which identifies the form being filed along with basic corporate information (i.e., company name and address, accounting contact, etc.), followed by the Text section containing the filing’s main descriptive content. Depending on the type of form being filed, an additional Financial Data Schedule (FDS) may be included at the end of the filing [29]. This Schedule is submitted with each 10K and 10Q filing, as well as some special Schedules filed by investment and public utility holding companies [34]. The FDS utilizes an attribute—value scheme: a pair-wise, simple to parse representation of the standardized financial data contained in the filing. In addition to the FDS, only the Header section contains tags that identify individual data fields. Since the content of the Text section is free-form text, automated data extraction from this section is quite difficult [26]. Even though the Text section does includes <Table > tags to identify imbedded tables, extracting data from these tables is still quite challenging because there is no imposed structure to the table layout [27]. Note, as of version 7.0, the EDGAR System no longer requires firms to file FDS documents [34].

The sheer amount of information available through on-line databases such as EDGAR highlights the need for automated data analysis tools. Although simple, text-based search tools exist, they cannot handle complex, multi-dimensional inquiries—more advanced search tools are needed. In this paper, we present an initial attempt at developing such a tool. EDGAR-Analyzer, is an advanced, multi-dimensional search tool designed to facilitate computer-assisted analysis of unstructured, text-based data. Developmental and operational issues of this tool are discussed.

The next section briefly discusses the SEC’s EDGAR database and the currently available tools that provide access to this data. Section 3 focuses on the development of the EDGAR-Analyzer tool. To illustrate the tool’s capabilities, it was used in a largescale study of Y2K disclosures made in annual reports filed from 1997–1999. To provide a basis for this study, the issues surrounding the Y2K problem are outlined in Section 4, followed by a discussion of the exploratory study and the results obtained. Section 5 discusses the operational issues surrounding the use of EDGAR-Analyzer. Finally, we summarize our findings and give some direction for future research.

## 2. SEC’s EDGAR database

‘‘The laws and rules that govern the securities industry in the United States derive from a simple and straightforward concept: all investors, whether large institutions or private individuals, should have access to certain basic facts about an investment prior to buying it. To achieve this, the SEC requires public companies to disclose meaningful financial and other information to the public, which provides a common pool of knowledge for all investors to use to judge for themselves if a company’s securities are a good investment.’’ [36]. All public, domestic companies with assets exceeding \$10 million with at least 500 stockholders fall under the SEC’s reporting guidelines. In addition, certain individuals must also file with the Commission. Insider trades reported on Forms 3, 4, and 5 are an important part of EDGAR. Table 1 identifies the common forms periodically filed with the SEC.

To improve access to this information, the SEC developed the EDGAR system, currently in its 8th revision [37,42]. It has evolved to the point that it automates ‘‘the collection, validation, indexing, acceptance, and forwarding of submissions by companies and others who are required by law to file forms with the U.S. Securities and Exchange Commission (SEC). Its primary purpose is to increase the efficiency and fairness of the securities market for the benefit of investors, corporations, and the economy by accelerating the receipt, acceptance, dissemination, and analysis of time-sensitive corporate information filed with the agency’’ [31].

Beside the traditional SEC Reading Rooms, the Commission provides four Internet-based avenues through which the EDGAR data can be accessed, as follows.

. Quick Forms Lookup—a web-based search utility that allows the user to lookup company specific filings. This tool has a very limited search capabilities, allowing the user to restrict the search based only on filing date and form type. This tool has no full-text

Table 1

Common SEC Forms accessible through EDGAR search capability. (see http://www.sec.gov/edgar/ searchedgar/webusers.htm).

. Search EDGAR Archives—a web-based, search utility that permits a full text search of the tagged headers in the EDGAR filings (the text search does not extend to the filing body). Although the Boolean search capability is quite flexible, the interface is cumbersome. The user must be aware of which fields exist in the headers to take full advantage of these features. The only explicit option available to the user is to restrict the search based on filing dates.

. FTP Access—This mode is used primarily for bulk downloads of corporate filing for subsequent remote processing. The SEC provides daily, quarterly and annual indexes sorted by company name and form type. These indexes provide the company name, form type, CIK (central index key uniquely identifying the submitting company), date filed, and URL (the Internet location where the full text of the filing can be obtained).

. Direct bulk feed of EDGAR Data—The data accessible through both the SEC Web and FTP sites is time-delayed at least 24 hours [31]. As a premium service, the SEC offers a subscription for ‘real time access to all EDGAR data through a direct bulk feed. This option is used by commercial information brokers who, in turn provide real time access to their customers.

By law, corporate public disclosures are required to be accurate and clearly represent the operations of the firm [36]. This makes the data contained in the EDGAR database quite valuable to investors, corporations and security markets. As a result, a number of tools have been developed to facilitate data access (Table 2 contrasts the features of the different tools). The following section gives an overview of the data contained in the EDGAR database. This is followed by a brief discussion of the different tools currently available to analyze this data.

## 2.1. Underlying data in SEC’s EDGAR database

The EDGAR database contains all filings that have been electronically filed since January 1, 1994. (Note, Lexis/Nexis, Disclosure, and Westlaw have information dating as far back as 1968, but this information is privately held and not contained in the SEC database.) Because the regulation requiring electronic filings was phased-in over a 3-year period, some filings prior to May 1996 were submitted on paper, and are therefore not included in the EDGAR database. However, as of May 1996, all public firms subject to the SEC’s filing requirements must submit forms electronically [31]. Official filings must be either in a tagged-text or HTML format. PDF versions are also accepted, but only as a supplement to the official filing [31].

Table 2  
Comparison of features and capabilities of free and third-party tools for accessing EDGAR filings

<table><tr><td></td><td>SEC Edgar</td><td>SEC Info</td><td>10k wizard</td><td>Edgar Scan</td><td>Free Edgar</td><td>Yahoo! Financial</td><td>Search SEC</td></tr><tr><td colspan="8">Tool Focus</td></tr><tr><td>Individual company data</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td></tr><tr><td>Multiple company data</td><td>a</td><td>a</td><td>a</td><td>No</td><td>a</td><td>No</td><td>No</td></tr><tr><td>Single form</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td></tr><tr><td>Multiple forms</td><td>a</td><td>a</td><td>a</td><td>a,b</td><td>a</td><td>a,b</td><td>a,b</td></tr><tr><td>All SEC forms</td><td>a</td><td>a</td><td>a</td><td>No</td><td>a</td><td>No</td><td>No</td></tr><tr><td colspan="8">SEC Forms Supported</td></tr><tr><td>Annual Reports (10K, 10-K405)</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a c</td><td>a</td></tr><tr><td>Quarterly Reports (10Q, 10-QSB)</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a,c</td><td>a</td></tr><tr><td>Current Reports (8-K, 6-K)</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a,c</td><td>a</td></tr><tr><td>Proxy Filings (DEF 14A, PRE 14A)</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td><td>No</td><td>a</td></tr><tr><td>Mergers and Acquisitions (S-4)</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td><td>No</td><td>a</td></tr><tr><td>Insider Trading (144, 3, 4, 5)</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td><td>No</td><td>a</td></tr><tr><td>IPO Fillings (S-1, 42AB, SB-2)</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td><td>No</td><td>a</td></tr><tr><td>Prospectus (485)</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td><td>No</td><td>No</td></tr><tr><td>Mutual Funds (N-1A, N-30D, 497)</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td><td>No</td><td>No</td></tr><tr><td>Private Placement Offerings</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Mergers and Acquisitions (13D, 14D-1, 14d-9, S4)</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td><td>No</td><td>No</td></tr><tr><td>No Action Letter</td><td>No</td><td></td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>&#x27;33 Act Deals (F-1, F-10, F-1MEF, F-2, F-3, F-3D, F-3MEF, F-7, F-8, F-9, F-10, N-2, S-1, S-1MEF, S-11, S-11MEF, S-2, S-2MEF, S-20, S-3, S-3D, S-3MEF, S-B, SB-1, SB-2, and SB-2MEF)</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td><td>No</td><td>a</td></tr><tr><td colspan="8">Data Reported</td></tr><tr><td>Full Filing</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td><td>d</td><td>a</td></tr><tr><td>Context of Text Search/Highlight search words</td><td>No</td><td>a</td><td>No</td><td>No</td><td>a</td><td>No</td><td>No</td></tr><tr><td>Extracted Financial Data</td><td>No</td><td>a</td><td>No</td><td>a</td><td>a</td><td>No</td><td>No</td></tr><tr><td>Balance Sheet</td><td>No</td><td>a</td><td>a</td><td>a</td><td>a</td><td>No</td><td>No</td></tr><tr><td>Income Statement</td><td>No</td><td>a</td><td>a</td><td>a</td><td>a</td><td>No</td><td>No</td></tr><tr><td>Cash Flow</td><td>No</td><td>a</td><td>a</td><td>a</td><td>a</td><td>No</td><td>No</td></tr><tr><td>Financial Ratios</td><td>No</td><td>a</td><td>a</td><td>a</td><td>a</td><td>No</td><td>No</td></tr><tr><td colspan="8">Source of Extracted Financial Data</td></tr><tr><td>Financial Data Section (FDS)</td><td>No</td><td>a</td><td>a</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Financial Statements in Filing Body</td><td>No</td><td>a</td><td>No</td><td>a</td><td>a</td><td>No</td><td>No</td></tr><tr><td colspan="8">Available Constraints</td></tr><tr><td>Company name</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td><td>No</td><td>No</td></tr><tr><td>Stock Ticker</td><td>No</td><td>No</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td></tr><tr><td>CIK (SEC&#x27;s Central Index Key)</td><td>No</td><td>a</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Period Date</td><td>No</td><td>No</td><td>No</td><td>e</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Filing Date</td><td>a</td><td>a</td><td>a</td><td>e</td><td>No</td><td>a,c</td><td>a,f</td></tr><tr><td>Today&#x27;s Filings</td><td>a</td><td>a</td><td>a</td><td>e</td><td>a</td><td>a</td><td>a</td></tr><tr><td>Date Ranges</td><td>a</td><td>a</td><td>a</td><td>No</td><td>No</td><td>No</td><td>a,f</td></tr><tr><td>Entire EDGAR Database (since 1/1/94)</td><td>a</td><td>a</td><td>a</td><td>e</td><td>a</td><td>No</td><td>a</td></tr><tr><td colspan="8">Header Fields</td></tr><tr><td>Company Name</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td><td>No</td><td>No</td></tr><tr><td>Address (i.e., City, State, Zip Code)</td><td>a</td><td>a</td><td>No</td><td>No</td><td>a</td><td>No</td><td>No</td></tr><tr><td>SIC Code</td><td>No</td><td>a</td><td>a</td><td>No</td><td>a</td><td>No</td><td>No</td></tr><tr><td>Industry</td><td>No</td><td>a</td><td>a</td><td>g</td><td>No</td><td>No</td><td>h</td></tr><tr><td>Full Text Search</td><td>i</td><td>No</td><td>a</td><td>No</td><td>a</td><td>No</td><td>No</td></tr></table>

Table 2 (continued )

<table><tr><td></td><td>SEC Edgar</td><td>SEC Info</td><td>10k wizard</td><td>Edgar Scan</td><td>Free Edgar</td><td>Yahoo! Financial</td><td>Search SEC</td></tr><tr><td colspan="8">Available Constraints</td></tr><tr><td colspan="8">Boolean Text Searches</td></tr><tr><td colspan="8">Evidence Constraints</td></tr><tr><td>AND, OR, NOT Operators</td><td>a</td><td>a</td><td>a</td><td>No</td><td>a</td><td>No</td><td>No</td></tr><tr><td>Stemmed words</td><td>a</td><td>a</td><td>a</td><td>No</td><td>a</td><td>No</td><td>No</td></tr><tr><td>Thesaurus</td><td>a</td><td>a</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td colspan="8">Proximity Constraints</td></tr><tr><td>Tagged Field Value</td><td>a</td><td>a</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Within n Characters/NEAR</td><td>a</td><td>No</td><td>a</td><td>No</td><td>a</td><td>No</td><td>No</td></tr><tr><td colspan="8">Other Operators</td></tr><tr><td>Case-Sensitive Search</td><td>a</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Relevance Scoring</td><td>a</td><td>No</td><td>No</td><td>No</td><td>a</td><td>No</td><td>No</td></tr><tr><td colspan="8">Report Output Formats</td></tr><tr><td>ASCII</td><td>a</td><td>a</td><td>No</td><td>a</td><td>a</td><td>No</td><td>No</td></tr><tr><td>RTF</td><td>No</td><td>a</td><td>a</td><td>a</td><td>a</td><td>No</td><td>No</td></tr><tr><td>CSV (Spreadsheet)</td><td>No</td><td>a</td><td>l</td><td>a</td><td>a</td><td>No</td><td>No</td></tr><tr><td>HTML</td><td>a</td><td>a</td><td>a</td><td>a</td><td>No</td><td>a</td><td>a</td></tr><tr><td>PDF</td><td>j</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>XML</td><td>No</td><td>a</td><td>No</td><td>a,k</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Context for full text search results</td><td>No</td><td>No</td><td>No</td><td>No</td><td>a</td><td>No</td><td>No</td></tr><tr><td colspan="8">Other Services</td></tr><tr><td>Predefined Searches</td><td>No</td><td>a</td><td>a</td><td>a</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Watch list</td><td>No</td><td>a</td><td>a</td><td>l</td><td>a</td><td>No</td><td>No</td></tr><tr><td>Custom Research Service</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Real time</td><td>No</td><td>a</td><td>a</td><td>No</td><td>a</td><td>a</td><td>a</td></tr><tr><td>Related Information Available</td><td>No</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td><td>a</td></tr></table>

<sup>a</sup> Feature supported.  
<sup>b</sup> Displays all filings, and lets user select from list.  
<sup>c</sup> Limited to the past 3 weeks.  
<sup>d</sup> Synopsis of the filing (http://help.yahoo.com/help/us/fin/research/research-01.html).  
<sup>e</sup> By default all filings for the company are displayed, any the user can pick the desired filing based on period or filing date.  
<sup>f</sup> Limited to Today’s Filings, This Weeks Filings, or All Filings.  
<sup>g</sup> Links are provided to pull up an industry comparison, with all leading firms hyperlinked.  
<sup>h</sup> Monthly Public Utility report, Monthly Real Estate Report and World Bank Report are available.  
<sup>i</sup> Search is only of the document header.  
<sup>j</sup> Although Companies can file PDF data with EDGAR, these files are not available through their publicly available on-line service.  
<sup>k</sup> Experimental.  
<sup>l</sup> Available through premium service.

The format of documents submitted and stored in the EDGAR database are based on broad guidelines set forth by the Securities and Exchange Commission. These guidelines identify which sections each form should contain along with the type of accounting information that should be reported [8]. Unfortunately, there is a great deal of variety in how this information is presented. The Commission requires certain header tags such as the company’s name, address, firm’s SIC code, and auditor’s name. However, the filing’s body consists primarily of unstructured, free-form text. Filing guidelines support the use of some SGML tags in the filing body to facilitate viewing and printing on the Internet, but this are not required [5]. Unfortunately, the Commission’s filing submission software does not validate document-formatting correctness. The improper structuring of tags results in the poor identification of data objects, which complicates the automated parsing of these documents [21]. To a limited extent, this problem is being addressed in the Commission’s modernization efforts. As of version 8.0 the EDGARlink automatically checks and validates the formatting of the document header, but still does not validate the structure of the filing body [37,39].

Standard financial statements contained in a filing’s body (i.e., income statements, balance sheets, cash flow statements, etc.) are more structured than the remaining text. Unfortunately, extracting meaningful information from even this data can be challenging. For example, terms are not used consistently among all filers. Even within a given filing, errors and inconsistencies will occur making it difficult to automate the analysis process [27]. Some values can be found in the FDS’s tagged fields, but this data is not as detailed as regular financial statements. For example, the FDS only provides current period data and aggregate values, omitting much of the supporting data presented in financial reports. The FDS section also does not report footnotes to financial reports, often a critical source of important information about the firm’s financial statements.

To appreciate the complexities involved in analyzing these free-form documents, consider EdgarScan, PricewaterhouseCooper’s innovative tool that extracts financial tables from SEC filings. However, even with extensive post processing, EdgarScan can only process 90% of the filings automatically [27]. The steps EdgarScan goes through to provide accurate and consistent data include (adapted from Ref. [27]):

1. Finding the relevant financial tables in the filing.

2. Finding the boundaries (start and end) of each table, in a manner that is resilient to page breaks.

3. Finding the column headers and column boundaries for a table.

4. Finding the units (e.g., dollars in thousands) usually expressed near the table heading.

5. Recognizing line item labels, compensating for wrapped lines.

6. Compensating for long line labels that ‘‘push over’’ data values in the first column.

7. Normalizing labels to a canonical form (e.g., ‘‘Sales’’ and ‘‘Total Revenues’’ mean the same thing).

8. Inferring the underlying mathematical structure of the table (e.g., recognizing subtotals), and possibly recognizing mathematical errors in the filing.

9. Extracting the numeric values based on the column boundaries, while compensating for poorly formatted filings with wandering columns.

10. Validating the data by cross checking with other tables.

11. Resolving the format of footnotes to financial tables. A wide variety of numbering and layout conventions are used to identify footnotes (including not numbering them at all, and relying solely on layout).

## 2.2. State of the art in EDGAR analysis tools

Various tools have been developed that provide access to the SEC filings [5,15,28]. Three general classes of tools have emerged—third party, free, and commercial tools (see Table 3).

The third-party tools contract for their content from the primary tool providers. These secondary sites typically are portals or special interest sites that aggregate content from multiple sources. The capabilities of these tools vary considerably. For example, the SEC filings section of Yahoo!Financial provides free, real-time access to select SEC filings. However, only ‘glimpses’ (summaries, not complete filings) of 10K, 10Q, and 8-K class filings are available, with the user routed to Edgar-Online for more complete information. Only 3 weeks of historical data are available, and although filing summaries can be displayed, there is no provision for initiating a text search. In contrast, RagingBull, powered by 10K Wizard, is a full-featured site with functionality equivalent to the native 10K Wizard site.

From the researcher’s perspective, the other two segments (free and commercial tools) are more important. Since all of these tools utilize the SEC filings as their primary data source, they tend to differentiate themselves primarily through their value-added features. All provide access to full text of the filings. Some use extensive indexing to provide convenient, direct access to individual document subsections, such as the document header, management’s discussion and the various financial statements. There is also varying support for different output formats, including plain text, RTF (rich text format, compatible with most word processors), HTML, and CSV (a spreadsheet format used for financial tables).

Table 3  
List of tools that provide access to EDGAR data

<table><tr><td>Research Tool</td><td>Company</td><td>URL</td></tr><tr><td colspan="3">Third-Party tools</td></tr><tr><td>IPO</td><td>Powered by 10K Wizard</td><td>http://www.ipo.com/marketdata/edgarsearch.asp</td></tr><tr><td>Raging Bull</td><td>Powered by 10K Wizard</td><td>http://10kwizard.ragingbull.com/</td></tr><tr><td>Yahoo!Financial</td><td>Powered by Edgar-Online</td><td>http://biz.yahoo.com/reports/edgar.html</td></tr><tr><td colspan="3">Free Tools</td></tr><tr><td>10K Wizard</td><td>10K Wizard</td><td>http://www.10kwizard.com/</td></tr><tr><td>EDGAR</td><td>SEC</td><td>http://www.sec.gov/edgar.shtml</td></tr><tr><td>EdgarPro</td><td>Edgar-Online</td><td>http://www.edgarpro.com/Home.asp</td></tr><tr><td>EdgarScan</td><td>PricewaterhouseCoopers</td><td>http://216.139.201.54/recruit/edu.html</td></tr><tr><td>Freedgar</td><td>Edgar-Online</td><td>http://www.freeedgar.com/</td></tr><tr><td>Search-SEC</td><td>Search-SEC</td><td>http://www.search-sec.com/</td></tr><tr><td>SEC Info</td><td>Finnegan O&#x27;Malley &amp; Co.</td><td>http://www.secinfo.com/</td></tr><tr><td colspan="3">Commercial Tools</td></tr><tr><td>Disclosure, Edgar Direct, Global Access</td><td>Thomson Financial/Primark</td><td>http://www.primark.com/pfid/index.shtml</td></tr><tr><td>Edgar-Online</td><td>Edgar-Online</td><td>http://www.edgar-online.com/</td></tr><tr><td>Lexis/Nexis</td><td>Lexis/Nexis</td><td>http://web.lexis-nexis.com/universe/form/academic/s_secfile.html</td></tr><tr><td>Livedgar</td><td>Global Securities Information</td><td>http://www.livedgar.com/</td></tr><tr><td>SECnet</td><td>Washington Service Bureau</td><td>http://www.wsb.com/online/secnet/index.pl</td></tr></table>

One of the most useful features of these tools is their extensive search facilities. Again, search capabilities vary considerably. The user can implement a full text search with most of these tools. They allow the user to optionally refine a search by specifying explicit field constraints, such as the company’s name, stock ticker symbol, form type, business/industry sector (based on SIC code) and filing date. These two features used in combination can search for a specific term in a single filing; broaden the search to include all filings made by that company; or even to expand the search over the whole EDGAR database. Other useful features include display of the context for search results and relevancy ratings. The search context is done by either showing a block of text surrounding the search terms that are found, or by highlighting the words in the document. Relevancy ratings of search results are typically based on the count of search words in each document.

Commercial tools (those for which there is a fee for essential features) tend to have some additional value-added features which differentiate them from the free tools. Often this entails access to non-EDGAR content. For example, Lexis/Nexis provides access to a large array of business, industry, and government information. Some tools (i.e., Lexis/Nexis, and Disclosure) have filings that predate the electronic filing regulations and thus are not found in the SEC’s electronic system. Additional services include specialized database content (i.e., No-Action letters, private offering circulars, etc.), premium watch/alert services (which automatically alert users when filings of interest are posted), ability to store commonly used queries, and the availability of customer support.

Given that these tools all use the same underling data, they have had to differentiate themselves based on other value-added features. Kambil and Ginsburg suggest three strategic dimensions for information

vendors operating in Web-enabled environments (see Fig. 1): Value-Added Content, Process and Interaction. Most Vendors have already added value by linking SEC content to non-EDGAR data such as Ticker symbols. Most have also added value along the Process Dimension by providing full text searches, automatic data extraction, watch lists and alert services. These technological innovations can typically be easily copied, and thus do not represent a sustainable advantage for any particular vendor. In contrast, leveraging unique intellectual capabilities can provide points of distinction. They may be based on proprietary methods of analyzing the public EDGAR data alone, or in combination with proprietary data. The third dimension deals with the amount of customization available to the user. The most basic is a generic interface that does not provide for user customization. The SEC’s EDGAR site would fall under this category. Most EDGAR tool vendors provide some means to personalize the user interface through extensive search options and customized alert lists. To date, tool vendors have not adopted a significant community-based interface on their own sites. Instead, they have typically acted as content providers for special interest or portal sites that support community-based interaction. For example, Yahoo!Finance uses EDGAR Online to deliver their SEC filings page.

## 3. Development of EDGAR-Analyzer, a text-based analysis tool

EDGAR-Analyzer is designed to facilitate the analysis of SEC Filings. Although the Commission specifies the content and to some extent the layout of the various filings, much of the information is contained in unstructured text. EDGAR-Analyzer is a general-purpose tool, capable of searching for and recording evidence of user-specified subjects. Using data contained in the filing header, the program prescreens filings and analyzes only those forms that correspond to the time period and filing types of interest. It sequentially analyzes SEC filings, looking for evidence of a particular subject, concept or issue, and subsequently saves this evidence in a local database. Objective information from the tagged data fields is recorded for each filing, including those that do not address the issue of interest. The information captured includes generic, corporate information (i.e., company name, CIK number, SIC number, etc.), form information (i.e., form type, filing date, period date, etc.), and tagged financial data from the FDS when available.

![](/api/attachments/TCWFMGDZ/fulltext/images/6478864955dbbbae7286066738e950b95bd9af8f700236e541a27c7efefbbb7e.jpg)  
Fig. 1. Web Information System-enabled information vendor strategies (from Ref. [21]).

The underlying EDGAR filings are assumed to conform to a Hierarchical, Functional Dependency Model. Under this model, general higher-level objects are recursively constructed into increasingly specific objects (i.e., a filing consists of multiple sections, which each section consisting of multiple paragraphs made out of multiple sentences containing multiple words). At all levels, each object has a given central focus. The higher level objects are necessarily more broad in their scope. Objects can deal with multiple subjects, but this is undesirable. Consider a long report made up of a single paragraph. Breaking it up into separate sections, each with multiple paragraphs allows for compartmentalizing of central concepts, and makes it easier to understand. It is further assumed that underlying each subject is a set of critical, or at least important, factors. When a given subject is addressed, a clearer picture of the issues emerges as more of these critical factors are considered. This could result in better analysis, and improve the reader’s confidence that important matters were not overlooked. Similarly, a factor’s relative importance to a given subject is reflected by the frequency that this factor is discussed within that subject’s context. Consequently, even when documents are relatively unstructured (as is the case with SEC filings), issues surrounding a particular subject of interest are assumed to be in relatively close proximity to each other. Conceptually, each SEC filing is viewed as a composite of short discussions address ing different major topics. It is assumed that within each discussion the company focuses on those factors it feels are important. Due to their loose structure, there is no presumption that these documents have sections that can be cleanly divisible into blocks, each dealing with a single major topic. A specific critical factor can be discussed in relation to many broad topics. For example, lawsuits, patent issues, labor or employee impli cations, and international issues can each impact many different aspect of the firm. Searching the whole filing for these general concepts would tend to have a high hit rate, but a hit found in this manner does not necessarily imply a relationship to the specific issue being studied.

A consequence of this data model is that search accuracy can be improved by implementing a tiered strategy. At issue is the high number of false positives obtained with a simple keyword search when the context of the word usage is not considered. The number of false positives can be reduced by first searching for terms specific to the main subject of interest, extracting the context where this subject is discovered, and then doing the final search on this smaller block to look for terms related to contributing elements. Note, because of the variability found in the free-form text, this approach is still not foolproof, and manual inspection of the extracted text blocks is still required. However, it can greatly reduce the amount of information that must to be manually processed.

## 3.1. EDGAR-Analyzer

Using a GUI interface the user specifies the desired time period, forms and specific subjects or terms of interest. The user can also specify which tagged data fields to record, and any sub-concepts that should be captured within the broader text search. This search profile information is stored in a file, which allows the distributed analysis of filings. At this point, the program has enough information to begin the search.

The program uses the index files stored on the SEC FTP site to identify records of interest. These indexes provide the form type, company name, file size, submission date, and URLs of each filing, with the URL identifying the Internet address of the filing’s full text (see Table 4).

Having prescreened the filings, the full text of the first targeted filing is downloaded from the SEC site. The program searches the filing’s text section for evidence of user-specified concepts and issues using a keyword search. When a keyword is located, the whole paragraph containing that keyword is extracted and placed in a separate text block, thereby capturing the usage context. Multiple context passages are often extracted from a given filing. Once the filing text has been completely processed, the system reanalyzes the extracted text blocks for evidence of specific factors of interest to the researcher. It sets Boolean fields in the output database indicating if evidence of a specific issue is found. For example, the extracted text block could be searched for evidence that:

. management feels a certain issue would (or would not) have a material impact,

Table 4  
Excerpt from SEC quarterly index (1Q 1997)

<table><tr><td>Form type</td><td>Company name</td><td>CIK</td><td>Date</td><td>Filing URL</td></tr><tr><td>10-12B</td><td>Bull &amp; Bear Global Income Fund</td><td>1031235</td><td>19970123</td><td>edgar/data/1031235/0000950172-97-000052.txt</td></tr><tr><td>10-12B</td><td>First National Entertainment</td><td>853832</td><td>19970218</td><td>edgar/data/853832/0000853832-97-000002.txt</td></tr><tr><td>10-12B</td><td>Hartford Life</td><td>1032204</td><td>19970214</td><td>edgar/data/1032204/0000950123-97-001413.txt</td></tr><tr><td>10-12B</td><td>New Morton International</td><td>1035972</td><td>19970324</td><td>edgar/data/1035972/0000912057-97-009794.txt</td></tr><tr><td>10-12B</td><td>Synthetic Industries</td><td>901175</td><td>19970213</td><td>edgar/data/901175/0000901175-97-000001.txt</td></tr><tr><td>10-12B</td><td>WMS Hotel</td><td>1034754</td><td>19970228</td><td>edgar/data/1034754/0000950117-97-000339.txt</td></tr><tr><td>10-12B/A</td><td>Getty Petroleum Marketing</td><td>1025742</td><td>19970113</td><td>edgar/data/1025742/0000950124-97-000137.txt</td></tr><tr><td>10-12B/A</td><td>Getty Petroleum Marketing</td><td>1025742</td><td>19970127</td><td>edgar/data/1025742/0000950124-97-000358.txt</td></tr><tr><td>10-12B/A</td><td>Getty Petroleum Marketing</td><td>1025742</td><td>19970313</td><td>edgar/data/1025742/0000950124-97-001486.txt</td></tr><tr><td>10-12B/A</td><td>Ralcorp Holdings/MO</td><td>1029506</td><td>19970203</td><td>edgar/data/1029506/0000950138-97-000017.txt</td></tr><tr><td>10-12B/A</td><td>Tanisys Technology</td><td>929775</td><td>19970124</td><td>edgar/data/929775/0000912057-97-001668.txt</td></tr></table>

. a similar project has been completed thereby improving the likelihood for success,

. cost figures are provided, or

. International issues appear to be important.

The analysis of the filing text uses a non-casesensitive, literal string equality operator for single and multi-word terms. In the current version, there is no support for Regular Expressions, which would automate the search for common variants of the same term (i.e., plurals, and different tense) [14]. Also not supported in this version is the automatic support of synonyms.

The final stage in analyzing the SEC filing is a manual review of data generated by EDGAR-Analyzer. Because of the variability of the documents, the data collected has to be verified by looking at the raw filings and double-checking the information collected. Before pulling the documents up in a word processor, the targeted keywords and phrases are highlighted (i.e., bold-faced, increased font size, and a color change) using rich text format tags. Highlighting the targeted keywords facilitates the manual review.

## 3.2. Operational issues

The use of SEC data as the primary data source introduces a number of important operational issues. First, it is very difficult to cross-link SEC filings with outside information. In each filings, the SEC requires companies to include their CIK (Central Index Key) number—a unique corporation identifier assigned by the SEC. Unfortunately, other data sources to not include this identifier, using instead the company’s CUSIP (Committee for Uniform Security Identification Procedures) number and/or its stock ticker symbol. ‘‘The SEC does not, in general, use the ticker symbols or CUSIP number in keeping track of companies. The ticker symbol is the property of the exchanges that issue them, and they are not required to file the symbols with the SEC’’ [38]. As a result, establishing a link between the SEC data and these external data sources can be difficult. It may be possible to use the company’s name, but this can introduce potential errors in cases where the match is not exact or where the company has changed names. Many companies include their ticker symbol in their SEC filings, thereby eliminating this ambiguity. Unfortunately, ticker symbols and CUSIP numbers are not a tagged field, which makes them difficult and time consuming to extract even when they are provided in the filing.

The second operational issue is that it is difficult to accurately parse and identify common subjects across multiple filings. This impacts the ability to automate the retrieval of information from these filings. There are a number of causes for this, including:

. Poor identification of data objects [21]

\- Limited number of tagged items

\- HTML formatting errors

. Content inconsistency and incompleteness within a filing

. Inconsistent use of terminology across companies . Lack of precision (i.e., failure to include units in the financial statements)

. Legalistic phrasing complicates automated processing of text.

An HTML formatting error can cause incorrect parsing of the documents. Although the SEC guidelines call for tables to be tagged with a <Table> </ Table> pair, occasionally one of these tags is entered incorrectly (e.g.,/Table without the < > delimiters, typos such as misplaced slashes as in <Table/>, or even no end tag at all). The SEC documentation indicates that it is the responsibility of the filer to format these documents so that they are readable. EDGARlink, the SEC’s filing submission software, does not check for HTML tagging errors [39]. These errors can cause large blocks of text to be incorrectly interpreted as part of the table. Similarly, inconsistent content (as in contradicting statements), and variability in the terminology complicates the automated extraction of data. Ultimately, these types of errors make fully automated processing unreliable.

In addition, sentence construction can be quite cumbersome. Some sentences extend over 15 lines of text while others contain compound negatives (sometimes as many as four or five in single sentence). Consider the following two statements dealing with the Year 2000 problem that were extracted from 10K reports. Both are relatively common, with similar statements being made by more than 30 firms. In the first case, if the reader focuses on the text in the immediate proximity to the ‘material adverse’ clause, or even that following ‘the year 2000 problem,’ he/ she could get the wrong impression about that company’s readiness. The second statement contains multiple negative clauses that blur the meaning of the message.

The Company has not completed its analysis and is unable to conclude at this time that the year 2000 problem as it relates to its previously sold products and products purchased from key suppliers is not reasonably likely to have a material adverse effect.

. Without a reasonably complete assessment of systems that could be vulnerable to problems, the Company does not have reasonable basis to conclude that the Year 2000 compliance issue will not likely have an operational impact on the Company.

Lastly, the structure and content of SEC filings keeps evolving, averaging nearly 1 major revision in the filing specification per year. For example, the header tagging structure was changed to an XFDL scheme in EDGAR 7.0, and modified again in EDGAR release 8.0 [37,42]. Another important change is that as of release 8.0, filing of the FDS is no longer required [37,42]. Extracting financial data, such as the income statement or balance sheet, now requires going into the body of the filing and extracting the data from imbedded tables. Furthermore, these tables are not required to have any special tagging to facilitate processing [39]. An additional complication is that filing can now be submitted as a multi-part, hyper-linked document rather than a single, integrated document.

Because of the issues involved in analyzing these free-form documents, a number of trade-offs had to be considered in the development of the EDGAR-Analyzer program. The first was the relative importance of Type I (false negatives) and Type II (false positives) errors in the analysis. An emphasis on Type I errors puts a premium on identifying all the targeted records, resulting in an increased number of records which do not contain useful or interesting content. Under this scenario, the assumption is that the cost of an overlooked record of interest outweighs the added cost of processing irrelevant records. The opposite is true when focusing on Type II errors, which stresses the elimination of these non-targeted records, even at the expense of missing records of interest.

Since EDGAR-Analyzer uses a two-tiered search strategy, we must consider which strategy is appropriate at each tier. At the first level, it searches for records that deal with a targeted main issue (e.g., the Year 2000 Problem). At this level the program emphasizes completeness (i.e., avoiding Type I errors).

Once an interesting record is found, the program executes a secondary search for related factors. For the Year 2000 issue, this search may focus on imbedded chips, employee retention, and indirect impact of third parties. We are interested in only those instances where these factors are discussed in relation to the main issue, and not related to any other issue. The search for these terms is done on blocks of text extracted from the full document. These text blocks capture the context in which the targeted subject is discussed. This secondary screening limits which blocks of text are extracted from each filing in an attempt to minimize Type II errors.

Since records are screened strictly on the presence of user-specified keywords, the issue of focusing on Type I errors reduces to the identification of this target set of keywords. This tends to be an iterative process. An initial set of terms is established and run on a small, sample data set. Results are checked for accuracy, and completeness before the process is tried on the full data. An alternate approach would be to use focus groups to generate these keyword lists. Reducing the false positives is also dependent on the proper keyword selection. Using common terms like ‘sales,’ or ‘profits’ will yield a high hit ratio, but many hits will not be relevant. Keywords should be as specific as possible to the issues of interest.

Two sets of keywords (along with their synonyms) are generated. The primary set of keywords, the ‘Issue Defining’ (ID) terms, are closely related to the subject under study. If any of these terms are located in the document, the relevant section is deemed pertinent and subsequently extracted. The secondary keywords, the ‘Critical Factor’ (CF) terms, are associated with factors related to the targeted subject rather than the subject itself. For example, when dealing with the year 2000 problem, ID terms might include ‘Year 2000,’ ‘Y2K,’ and ‘Millennium Bug,’ while the CF terms might include ‘imbedded chips,’ ‘staff,’ and ‘cost.’ For this particular study, these terms were initially generated based on the issues discussed in the popular press, research reports and academic articles, and subsequently refined during pilot testing on sample SEC filings. Note that the presence of a CF term does not imply a discussion of the targeted subject, and thus does not automatically trigger the extraction of text. However, it could indicate a potentially relevant passage. As a result, a sliding relevancy scale is used. The program first executes a keyword search based on only the ID terms. When an ID term is located, the paragraph containing that term is marked for extraction. At this point, the relevancy threshold is decrease to include the CF set of words in the search. Contiguous paragraphs following the previously marked paragraph are then searched for any term within either the ID or CF set. Paragraphs containing a qualifying term from either set are extracted. Each extracted text block is marked with a delimiter to allow subsequent identification of the separate contiguous blocks. The remaining text is then searched for the next instance of an ID term, repeating the extraction process until the whole document is processed.

Another trade-off involved in the development of this tool is the issue of preprocessing filings before sending them to the search engine. The content variety and inadvertent formatting errors can greatly impact the processing of these files. For example, most files are single spaced, with double-spacing between paragraphs. However, some files are double-spaced throughout (using two hard carriage returns) with an indention indicating a paragraph break. In some instances, there is no discernable paragraph break at all (i.e., the company used hard carriage returns at the end of each line with no indentions). The ability to identify paragraph boundaries is critical to this application since the program extracts the search context information a paragraph at a time. Improperly identifying paragraph boundaries would reduce the effectiveness of the secondary search to identify contributing factors. A similar issue exists with word spacing. Since search phrases may contain multiple words (e.g., Year 2000), the search is sensitive to inter-word spacing. In both cases (paragraph and inter-word spacing), the problem can be resolved through a global search and replace process, but this can significantly impact processing time.

Two different solutions are used to address these problems. Because of the central role that paragraphs played in the methodology, it is important to reintegrate text back into contiguous paragraphs. Files were checked for double spacing and converted to singlespacing where needed. Using the same approach proved to be too computationally costly for the inter-word spacing issue. This issue was handled by specifying multiple search strings with different interword spacing (i.e., Year2000, Year<sub></sub>2000, and Year<sub></sub> <sub></sub>2000). This is not an optimal approach since it tends to increase Type I errors. This occurs when a spacing combination existing in the document is omitted from the search string set (i.e., Year <sub>  </sub> 2000). This can be addressed by selectively searching for instances of the first word in multi-word terms and replace instance where multiple spaces exist. An initial search for ID terms is done to prevent the time-consuming work of cleaning a file that does not contain anything of interest.

## 4. Sample study—Y2K

EDGAR-Analyzer was used to investigate corporate year 2000 remediation efforts as reported in their annual reports. Although this issue has been known since 1971 [6,44], it only emerged into the public and corporate consciousness around 1995–1996, which coincidentally is the same period of time that the EDGAR database was established. Recall that the year 2000 problem (Y2K) refers to the inability of software and hardware systems to handle dates beyond the year 1999. The problem stems from what was a common system design practice of representing dates by a six-digit field—MM-DD-YY, thereby capturing the month, day and only the last two digits of the year. As a result, the dates January 1, 1900 and January 1, 2000 were both represented as ‘1/1/00’. Unfortunately, most systems had no means to distinguish which of these dates is correct. Extensive information concerning the Year 2000 problem is available on the Internet. The interested reader is directed to the National Y2K Clearinghouse site run by the U.S. General Services Administration and located at http://www.y2k.gov/.

Before the actual study is discussed, a brief overview of issues surrounding the Y2K problem is presented. In practice, such a pre-analysis of the issues is necessary, for it helps to develop the set of keywords that EDGAR-Analyzer will use when parsing the document. This is followed by a discussion of the case study—the methods used and the results obtained.

## 4.1. Review of the Y2K problem

The ‘‘Year 2000 problem’’ relates to what was a common practice of computer programmers to use a two-digit rather than four-digit number to represent the year. This could cause systems or applications using dates in calculations, comparisons, or sorting to generate incorrect results when working with years after 1999 [32]. On the surface, the Y2K problem appeared to be a trivial, with an obvious solution— simply modify all date fields to include four digit years. On closer examination, this problem is seen to be much more complicated (see Table 5 for a list of potential issues/problems).

## Table 5

## Potential year 2000 problems

## Software

. Valid dates were often used to represent special conditions. For example, ‘1/1/00’, ‘9/9/99’, and ‘12/31/99’ might represent ‘date unknown’, ‘date not entered’, and ’infinite date’. Thus the Y2K problem was not limited to January 1, 2000

. Availability of well-documented source code may be limited, greatly complicating the analysis and code conversion efforts

. Inconsistent date formats were commonly used (e.g., YYYYMMDD, MMDDYYYY, DDMMYYYY)

. Not all dates are based on variable values. Hard-coded dates, calculated dates and dates imbedded in filenames are just three examples

. Multiple, non-compatible approaches were used to address the Y2K problem. These included field expansion, fixed window, and sliding windows

. The program logic needs to change to account for this different date representation. Changing date format may corrupt screen and printed output. Archived data may also have to be changed to be consistent with revised code so that it is still accessible.

. Leap year issues

## Hardware

. Many modern devices have embedded microprocessors that could be susceptible to the Y2K problem. In these devices, the logic is ‘burned’ into the chip and is therefore not modifiable

## Personnel

. Shortage of qualified personnel needed to address problems. Due to supply and demand pressures the cost to locate, hire and retain qualified staff was high

## Legal Issues

. Business interruption do to the failure of critical systems

. Directors and Officers liability for not addressing Y2K in a timely manner

. Stockholders suing accounting firms for inadequate disclosure of Y2K risks

. Collateral litigation – failure of one system preventing a company from delivering on their commitments

. Breach of contract and failure to perform service

. Consumer fraud class action based on misrepresentation of system performance

## Environmental

. Cascade failure if suppliers or customers fail to become year 2000 compliant

. Impact of potential public utilities failures (electric, gas, water, phone, etc.)

This was a worldwide problem. The sheer magnitude of the required Y2K conversion effort would tend to introduce new errors into existing applications, and adequate testing is critical to ensure that the Y2K problem has been corrected. Because of system interdependence, this testing should involve both unit testing and integrated system testing [18]. Also, research has shown that proper testing of large projects typically accounts for 50% of the whole project time [4]. Unfortunately, the required time to do adequate testing is often underestimated and in this case the time frame was unalterable (it had to be done by December 31, 1999).

Of particular interest to this case study is the SEC’s response to the Y2K problem since it is the controlling legal authority dealing with disclosure obligations of public corporations in the United States. The SEC’s bulletin of October of 1997 (subsequently revised on January 12, 1998) specifically addressed the ‘‘disclosure obligations relating to anticipated costs, problems and uncertainties associated with the Year 2000 issue’’ [30]. It required companies to disclose details of Y2K problems in their ‘Management’s Discussion and Analysis’ section if:

. ‘‘the cost of addressing the Year 2000 issue is a material event or uncertainty that would cause reported financial information not to be necessarily indicative of future operating results or financial condition, or

. ‘‘the costs or the consequences of incomplete or untimely resolution of their Year 2000 issue represent a known material event or uncertainty that is reasonably expected to affect their future financial results, or cause their reported financial information not to be necessarily indicative of future operating results or future financial condition‘‘ [30].

Also, ‘‘if Year 2000 issues materially affect a company’s products, services, or competitive conditions, companies may need to disclose this in their ‘‘Description of Business.’’ . . .[This] ‘‘disclosure must be reasonably specific and meaningful, rather than standard boilerplate’’ [30].

## 4.2. Case study

The focus of this study is to determine the status of Y2K remediation efforts as reported in corporate 10K documents filed with the SEC over the period 1997 –

1999 (corresponding to FY 1996– 1998). At issue is the type of disclosures made, and to what extent critical factors related to the Y2K problem are acknowledged in these disclosures.

The case study looked at all 10K reports electronically submitted and stored in EDGAR during the period January 1, 1997 to April 30, 1999, which amount to 18,595 filings (see Table 6). The 10K filing was targeted because it corresponds to the firm’s annual report that is required to provide extensive discussion of issues that impact, or even could potentially impact, the firm’s operations. These files tend to be detailed and can be of significant size. For this study, the average file size was 291 KB, which corresponds to approximately 100 pages. The largest files were 5 MB. Some 10K files reach 23 MB, although none that size were involved in this study. The sheer volume of information contained in these files makes finding topics of interest difficult and highlights the need for automated support. Note, only the 10K filings were analyzed, including all variants (e.g., 10K/A, 10KSB, 10 KT405, etc). The keywords and their synonyms use for the case study are listed in Table 7.

Pilot testing indicated that two ID terms were commonly used outside the context of the year 2000 problem. The first was ‘year 2000’ and its variants. With the approaching century change, many companies discussed plans that would be implemented in the year 2000, which created a false positive. The second was ‘y2k’. Actually, the term y2k was nearly exclusively used to refer to the year 2000 problem, but financial tables tended to use ‘fy2k’ (or its equivalent ‘fiscal year 2000’) in a non-relevant context. A simple keyword search for ‘y2k’ would caused a false hit on ‘fy2k’. These issues were found early in the analysis and a special filter was added to address this problem.

The program screened 10K filings for any indication of a year 2000 disclosure (based on the presence of ID in Table 7), and extracted relevant text blocks. These text blocks were then searched for critical issues/elements dealing with Y2K. Table 8 gives a list of the items tracked during the study. Certain concepts could not be automatically extracted and therefore required manual processing—for example, cost figures and dates information. EDGAR-Analyzer determined that 42.6% of the filings did not contain any ID term, and were logged as non-disclosing filings. To eliminate false positives, the extracted text blocks were manually reviewed. In the process, the data extracted by EDGAR-Analyzer was validated. Due to time constraints, only 1,847 filings containing Y2K disclosures were manually reviewed.

Table 6  
Breakdown of 10K filings processed

<table><tr><td></td><td>10Ks screened by Edgar Analyzer</td><td>Manually validated</td></tr><tr><td>10K Filings</td><td>18,595</td><td>9,764</td></tr><tr><td>Non-disclosures</td><td>7,917 (42.6%)</td><td>7,917 (81.1%)</td></tr><tr><td>Disclosures</td><td>10,678 (57.4%)</td><td>1,847 (18.9%)</td></tr></table>

Table 7  
Keywords/phrases used to locate information in SEC 10Ks. Multiple spellings of words are included where appropriate

<table><tr><td>Issue defining terms</td><td colspan="3">Critical factor terms</td></tr><tr><td>Year2000 (No Spaces)</td><td>Adverse</td><td>Embedded</td><td>Remediation</td></tr><tr><td>Year 2000 (One Space)</td><td>Analysis</td><td>Evaluated</td><td>Reviewing</td></tr><tr><td>Year 2000 (Two Spaces)</td><td>Assess</td><td>Failure</td><td>Significant</td></tr><tr><td>Y2K</td><td>Completed</td><td>HVAC</td><td>Substantial</td></tr><tr><td>Millenium Bug</td><td>Compliance</td><td>Liability</td><td>Supplier</td></tr><tr><td>Millennium Bug</td><td>Conducted</td><td>Material</td><td>Third Parties</td></tr><tr><td>Millenium Problem</td><td>Contingency</td><td>Miscalculations</td><td>Unknown Cost</td></tr><tr><td>Millennium Problem</td><td>Conversion</td><td>Not Pose</td><td>Vendor</td></tr><tr><td></td><td>Customer</td><td>Positive Effect</td><td>Warrant</td></tr><tr><td></td><td>Customers</td><td>Positive Impact</td><td>2000</td></tr><tr><td></td><td>Disrupt</td><td>Preliminary</td><td></td></tr></table>

## 4.3. Case study results

To illustrate the capabilities of this tool, five aspects of the Y2K problem were investigated, namely:

. How did the percentage of Y2K disclosures in annual reports changed over time?

. How did firms characterize the impact of the Y2K problem?

. To what extent are the various factors associated with Y2K discussed?

. How far along are companies in their remediation effort?

<table><tr><td>Critical elements</td><td>Informational elements</td></tr><tr><td>Imbedded Chips</td><td>Expected to have a positive impact</td></tr><tr><td>Staffing/Programmer Retention</td><td>In the business of Y2K remediation</td></tr><tr><td>Third Parties</td><td>Not material in 1998</td></tr><tr><td>Euro Conversion</td><td>Was any Y2K disclosure made</td></tr><tr><td>Leap Year</td><td></td></tr><tr><td>Liability and Warranty issues</td><td>Status of Y2K Remediation</td></tr><tr><td>Risk of Disruption</td><td>Not yet started</td></tr><tr><td>Impact on competitive position</td><td>Not finished remediation plan</td></tr><tr><td>Contingency plans</td><td>Not finished with analysis phase</td></tr><tr><td>Material/Not Material</td><td>Finished with analysis phase</td></tr><tr><td>Not material without discussion</td><td>Schedule date to complete assessment</td></tr><tr><td>Not material with some discussion</td><td>Schedule date to finish changes</td></tr><tr><td>Not material in 1998</td><td>Schedule date to finish testing</td></tr><tr><td>Not expected to be material</td><td>Schedule date to finish Y2K Project</td></tr><tr><td>Material</td><td>Substantially done with Y2K Project</td></tr><tr><td></td><td>Mission critical systems are Y2K compliant</td></tr><tr><td></td><td>Data Inconsistency and incompleteness</td></tr><tr><td></td><td>Currently Y2K Compliant</td></tr></table>

. And finally, what disclosures are made regarding the cost of their Y2K efforts?

For the analysis of Y2K disclosure frequency, all 18,595 annual reports, including those filings that were not manually checked, were incorporated. This was done to increase the sample population and get a sense as to firm’s Y2K awareness. Incorporating the non-verified data will tend to increase the number of false positives since an ID term may be used in a non-Y2K context, and thus, the reported disclosure percentages may be inflated from the actual number of disclosures. The remaining four topics focused on company specific disclosures, so only manually verified data was included in this analysis. Each of these issues is discussed below.

Fig. 2 illustrates the percentage of 10K filings that contain some form of Y2K disclosure. The number of filings peaks sharply every March, which corresponds to the large number of companies with a December fiscal year end (the SEC requires 10Ks to be filed within 3 months of the close of the fiscal year, explaining the peak in March). The bar chart shows that the percentage of filings with Y2K disclosures started to increase in November 1997. This corresponds to the SEC’s issuance of Staff Legal Bulletin No. 5 in October 1997 that outlined the specific obligations each firm had with regard to their the year 2000 disclosure (see discussion in prior section) [30].

The Commission requires firms to identify and disclose factors that may have a material impact on their operations. As mentioned above, both governmental regulating bodies and professional bodies issued opinions and guidelines requiring disclosure of Y2K-related information (Ref. [30] and Refs. [1,2,3,11], respectively). Consequently, this information should be common in filings submitted after the publication of these guidelines. Fig. 3 presents how the firm’s rating of the severity of the Y2K issue changed over time. The overall height of the bars indicates the percentages of 10K filings that contained some form of Y2K disclosure. The stacked bars break out six categories—the two most significant being ‘Materiality not Mentioned’ and ‘Not Material with Support.’ The first category is self-explanatory. The second category captures the number of filings that indicated that Y2K will not have a material impact and presented additional factors related to the Y2K problem to lend support to this statement. This is in contrast to those falling into the ‘‘Just Not Material’’ category which did not include any such support. Few filings fell into the remaining three categories. The balance of the filings for each year did not mention the materiality of the Y2K issue (note, the category ‘‘Unknown if Material’’ includes only those filings which stated specifically that they did not know if the impact was likely to be material or not).

Corporate Y2K Disclosures in 10Ks  
![](/api/attachments/TCWFMGDZ/fulltext/images/053beb9878ff1563f6935efb38363fa06e4736d9fe009f137e5ccc422fd16706.jpg)  
Fig. 2. Y2K disclosures in corporate 10K filings submitted from January 1997 to April 1999 (FY 1996– 1998). The line graph shows the number of filings per month. The bar chart shows the percentage of those filings that contained some form of Y2K disclosure.

Material / Immaterial Impact of Y2K (Aggregate Represents Percent of Y2K Disclosure)  
![](/api/attachments/TCWFMGDZ/fulltext/images/284de7d03dae03a68dcb70ae72a1dce1b1c458121f37c7540da5327f2d249324.jpg)  
Fig. 3. Breakdown of the self-purported impact of Year 2000 for fiscal year 1996 – 1998. Values represent percentage of manually checked 10Ks, with the aggregate representing percentage of 10Ks containing some form of Y2K disclosure.

Critical Y2K Factors Mentioned in 10Ks (Percent of Filings with Y2K Disclosure)  
![](/api/attachments/TCWFMGDZ/fulltext/images/c3df21fb9140cd0a2f65e1436746634fb72cb57a2fd94c74edb85857bb5f829e.jpg)  
Fig. 4. Frequency that various critical Y2K factors were discussed in 10K filings. The values are percentages of each the manually checked filings with some form of Y2K disclosure.

A statement of non-materiality may not engender much confidence without some accompanying evidence that the issues involved have been adequately addressed. For this reason, it is interesting to investigate the frequency these related issues are discussed. Fig. 4 looks at the frequency that 11 critical factors are discussed in the context of Y2K problems. It is interesting to note the dramatic rise in the awareness of ‘‘Imbedded Chips’’ in FY 1998 (these filings were submitted in 1999 for the previous year’s operation).

Another factor that could impact the reader’s confidence is a statement regarding the status of the remediation process. Statements being made late in the conversion process would tend to be more reliable than one made earlier. Fig. 5 focuses on important milestones in the Y2K effort. Finishing the assessment phase is important, for it marks when the point the firm has reviewed its exposure to Y2K problems and is now ready to address these issues. Unfortunately, in FY 1998 the number of firms that had not yet finished the assessment phase almost equaled those who had finished it. In addition, over 50 percent of the FY 1998 10K filings did not disclose if they completed their assessment or not. Given this result, coupled with the approaching December 31st deadline, the status of the firm’s contingency planning became important. Most firms had not finished their contingency plan as of the filing of they FY 1998 annual report. In addition, 187 filings, over 12% of filings with disclosures, indicated that they would develop a plan on an as-needed basis.

When addressing the materiality of the Y2K issue, some firms reported the costs of their remediation effort—both what had been spent to date and expected future expenditures. These values varied considerably. From an accounting perspective, it is important how these expenses are accounted for in the firm’s financial statements. Capitalizing these expenses allows the firm to spread the impact over multiple years, while expensing the costs recognizes them in a single year. The Emerging Issues Task Force (EITF) of the Financial Accounting Standards Board and International Accounting Standards Committee (IASC) both issued opinions stating that Y2K-related expenses should normally be expensed as incurred [11,19]. Fig. 6 reports how firms planned to account for their Y2K remediation expenses. Note that there is a significant number of firms planning to capitalize these expenses despite these authoritative opinions. Also note that there is a sizable group of firms which indicated that they did not track their internal costs.

![](/api/attachments/TCWFMGDZ/fulltext/images/082ec69498bc00f582069232b696b125947ca12d618b05b1849b2438ef311c08.jpg)  
Fig. 5. Identifies the Y2K remediation phase as disclosed in manually checked 10Ks for fiscal years 1996 – 1998.

![](/api/attachments/TCWFMGDZ/fulltext/images/6ef7d4203f18ae5ca8222372afa72658464ffde3209e2d9722f60f891c509fc4.jpg)  
Fig. 6. Percentage of manually reviewed 10K filings that disclose certain remediation cost information. Capitalize/Expense Costs categories indicate how they plan to recognize these expenses on their income statements.

## 5. Discussion and directions for further research

EDGAR-Analyzer addresses a shortcoming of existing tools that extract data from the SEC’s EDGAR database. Although existing tools provide basic search capability, most focus primarily on the financial data contained in the FDS. In contrast, EDGAR-Analyzer focuses on the text section of these filings. Extracting information from unstructured freeform text is challenging [10,22,24]. The approach adopted incorporated a tiered search strategy. Keywords specific to the targeted search are used to identify passages that deal with an issue of interest. These passages are extracted and subsequently reanalyzed to determine if sub-issues are addressed within the context of the more general targeted search. The final phase of the analysis is a manual review and validation of the automated analysis.

The case study points out a number of areas that would potentially improve the usefulness of the EDGAR database, as follows:

. Need for extending the EDGAR file specification to include tagged values of either the stock ticker symbol (along with the corresponding exchange), or CUSIP number.

. The structure of the EDGAR filings could be preprocessed to made them easier to analyze electronically. This would involve making contiguous paragraphs by removing imbedded hard line feeds, and extending the tagging to include tables, sections, subsections, and even paragraphs.

. The need to validate the tagging structure of filings. Improper tagging greatly complicates the analysis of these documents.

EDGAR-Analyzer’s identification of sub-issues related to the larger issue under study was very useful. For example, in the case study Boolean variables indicated if any evidence was found of a Y2K-related discussion of suppliers and customers, whether they felt Y2K would materially impact the company, or costs related to the remediation effort. Since the screening process was biased toward minimizing false negatives, these Boolean values reduced the number of issues that had to be manually verified.

This method of data mining was found to be effective in a case study involving Y2K disclosures found in annual reports. This study focused on finding all disclosures that dealt with the year 2000 problem. Consequently, a liberal screening strategy was used, which tended to include text blocks that were not pertinent. Even so, EDGAR-Analyzer eliminated 42.6% of the records analyzed as being non-Y2K disclosing, and extracted an average text block of 11.1 KB from each filing, which averages 291 KB, amounting to a 96% reduction in the amount of text that had to be manually processed.

## 5.1. Future of EDGAR

As suggested earlier, the SEC is continually refining the guidelines dealing with the filing requirements. There is an ongoing effort within the Commission to improve the availability and usability of corporate information within the EDGAR database. With each new version, additional forms are added to the list of required documents that must be filed electronically. Additional formats have also been added. The earliest documents were only available in ASCII text. In June 28, 1999, the SEC started accepting HTML and PDF files (although PDF filings are considered unofficial copies). In May 2000, the guidelines were again modified to allow HTML filings to include graphic images, and to allow multi-part, hyperlinked filings. Furthermore, ‘‘the Commission has rescinded the requirement for registrants to submit FDSs for filings due and submitted after January 1, 2001’’ [34]. This was dropped because it represented duplicate information to that contained in the filing body, and thus created a potential for data inconsistency. No alternative mechanism has been added to compensate for the absence of the FDS schedule. Those who want the obtained the financial data must now locate and extract that information from the filing body [40].

As part of the modernization effort, the SEC is migrating toward XML-based tagging of documents. The first step has already taken place. The Commission has instituted a change from the SGML header tags used since the initiation of EDGAR, to XFDL tags (XFDL is an XML-based language designed to handle forms). ‘‘Legacy filings (with SGML header tags) will no longer be accepted by the Commission’s EDGAR system after April 20, 2001’’ [41].

Based on an interview with the EDGAR project manager, the SEC envisions steady progress in integrating XML-type tagging into the Commission’s filing regulations [39]. The tagging is still quite limited, being required only for the filing header. Future EDGAR revisions will begin to include tags identifying content within the filing body, especially the financial reports. Processing these financial reports is challenging, and proper tagging would greatly import access to this information. The SEC is taking a cautious approach, preferring to wait for the private sector to develop generally accepted standards before establishing filing policy. One particularly promising initiative is the XBRL (Extensible Business Reporting Language) [45], which ‘‘uses XML-based data tags to describe financial statements for both public and private companies’’ [46].

## 5.2. Areas for future research

This paper describes the development and testing of a prototype tool designed to access, search and extract information of interest from the SEC EDGAR database. Having successfully demonstrated feasibility, the next phase of the project will focus on moving this application into a more robust, multi-user, serverbased environment.

To improve handling of the multiple variants that accompany most search terms, it is useful to incorporate regular expression processing and automatic synonym support (see Refs. [12,14], respectively). Regular expressions are especially important since the analysis of SEC filings primarily involves text processing. Regular expression support would facilitate handling of stemmed words, wild cards and word variants such as plurals and tenses. Automated support of domain specific synonyms would also help to reduce both Type 1 and Type 2 errors. One possibility is to tap into the extensive work done on WordNet, an on-line lexical reference systems organized into synonym sets [12].

The tiered search algorithm used in EDGAR Analyzer depends on the ability to accurately identify paragraph boundaries within the documents. As previously mentioned, this was a challenging aspect in the case study and represents a potential source of error. To assist in this critical process, techniques developed in the Computational Linguistics (CL), Information Retrieval (IR) and Data Mining literature need to be evaluated. Within CL, multiple paragraph extraction techniques have been developed [23]. Of particular interest is a TexTiling algorithm, which partitions full-length documents into coherent, multiparagraph passages that reflect the subtopic structure of the original text [16]. It is also important to validate the efficacy and efficiency of the tiered search algorithm against other search algorithms found in the IR literature [9,13,43]. To adequately evaluate and compare these techniques, standard IR methodology must be used, including the reporting of traditional recall and precision scores. Recent advances in text-based data mining may also be of use in refining the search algorithm [17].

EDGAR-Analyzer’s text-parsing routines must be continuously adapted to address on-going changes occurring in the SEC’s filing specifications. For example, the Commission has recently stopped supporting SGML tagging and required XFDL tagging, and firms can now submit multi-part, hyperlinked filings. To fully process these submissions, it must be possible to recursively recover and analyze each segment of the filing. Also, in extending EDGAR-Analyzer, it is important to plan for the future XML migration plans of the SEC.

EDGAR-Analyzer was written for a single user environment, but to reach its full potential it needs to support a broader, multi-user environment. Since the underlying engine is generic and useful in many different contexts efficiencies could be gained by creating specialized, community-based interfaces. Potential communities could include investors, analysts, lawyers, pre-IPO firms, regulators, insiders, etc. As suggested in Fig. 1, value can be added by moving to community-based environments. In this way, common variables of interest to a particular community could be predefined. Generation of community-specific search terms and appropriate synonym lists could also be facilitated through a group-based interface. Both of these features would speed up a search and hopefully improve the quality of the results returned.

To gain additional efficiencies and allow multi-user access and support, this tool needs to move to a server-based environment. Moving to an extensible, open-source architecture would allow distributed, multi-author development. The code needs to by reengineered in a language such as Python, which has both strong, native support for regular expressions and XML processing as well as providing cross platform support. Finally, it may be possible to extend EDGAR Analyzer’s data mining methodology to other textbased archival systems, such as news articles, journal articles, patent filing and government legislation (i.e., www.thomas.gov).

## References

[1] AICPA, The Year 2000 Issue—Current Accounting and Auditing Guidance, American Institute of Certified Public Accountants, 1997, http://www.aicpa.org/members/y2000/intro.htm

[2] AICPA, Year 2000 Issue Disclosure Considerations: Public and Nonpublic Entities, American Institute of Certified Public Accountants, 1997, http://www.aicpa.org/members/y2000/ discon.htm.

[3] AICPA, AICPA’s Letter to the SEC on Year 2000 MD and A Disclosure, American Institute of Certified Public Accountants, December 9, 1997, http://www.aicpa.org/belt/sec2000/ index.htm.

[4] H. Aronoff, S. Graham, A Testing-Centric Approach to Year 2000 Project Management, White Paper, Tech-Beamers, 1997, http://www.idsi.net/techbmrs/y2kh.htm.

[5] M.E. Bates, Where’s EDGAR Today? Finding SEC Filings Online, DATABASE, June 1996, http://www.onlineinc.com/ database/JuneDB/bates6.html.

[6] R.W. Bemer, What’s the date? Honeywell Computer Journal 5 (4) (1971) 205–208.

[7] M. Bergman, The Deep Web: Surfacing Hidden Value, BrightPlanet.com, July 2000, http://128.121.227.57/download/ deepwebwhitepaper.pdf.

[8] Bowne & Co., Securities Act Handbook, 2001, http://www. bowne.com/resources/secrules.asp.

[9] J. Callan, M. Connell, Query-based sampling of text databases, ACM TOIS 19 (2) (April 2001) 97 – 130.

[10] T.E. Doszkocs, Natural language processing in information retrieval, Journal of the American Society for Information Science 37 (4) (1986) 191–196.

[11] Emerging Issues Task Force, EITF Issue No. 96-14, Accounting for the Costs Associated with Modifying Computer Software for the Year 2000, 1997, http://www.ncua.gov/ref/ accounting<sub></sub>bulletins/bull971.pdf.

[12] C. Fellbaum (Ed.), WordNet: An Electronic Lexical Database, Bradford Books, MIT Press, Cambridge, MA, May 1998.

[13] F. Feng, W.B. Croft, Probabilistic techniques for text extraction, Information Process Management 37 (2) (March 2001) 199 – 220, http://ciir.cs.umass.edu/pubfiles/ir-187.pdf.

[14] J.E. Friedl, Mastering Regular Expressions, Powerful Tech-

niques for Perl and Other Tools, O’Reilly, Cambridge; Sebastopol, 1997.

[15] B. Goodwin, P. Smith, R. Bunney, EDGAR and Family: SEC data on the Web, Internet Prospector, Sept. 1998, http:// www.internet-prospector.org/edgar.htm.

[16] M.A. Hearst, TexTiling: segmenting text info multi-paragraph subtopic passages, Computational Linguistics 23 (1) (1997) 33 – 64.

[17] M.A. Hearst, Untangling text data mining, Proceedings of the ACL, University of Maryland, (June 20 – 26, 1999).

[18] L. Hyatt, L. Rosenberg, A Software Quality Model and Metrics for Identifying Project Risks and Assessing Software Quality, 8th Annual Software Technology Conference, April 1996, http://satc.gsfc.gov/support/STC<sub></sub>APR96/quality/stc<sub></sub> qual.html.

[19] IASC, SIC Draft Interpretation D6: Cost of Modifying Existing Software, International Accounting Standards Committee, October 1997, http://www.iasc.org.uk/frame/cen3doo6.htm.

[20] A. Kambil, Final Report: NSF Award 9319331: Internet Access to Large Government Data Archives: The Direct EDGAR Access System, NYU Stern School of Business, July 29, 1996.

[21] A. Kambil, M. Ginsburg, Public access web information systems: lessons from the Internet EDGAR project, NYU stern school of business, Communications of ACM 41 (7) (July 1998) 91 – 98, http://delivery.acm.org/10.1145/280000/ 278493/p91-kambil.pdf.

[22] P. McKevitt, D. Partridge, Y. Wilks, Why machines should analyze intention in natural language dialogue, International Journal of Human Computer Studies 51 (5) (November 1999) http://www.idealibrary.com/links/citation/1071-5819/51/947.

[23] M. Mitra, A. Singhal, C. Buckley, Automatic text summarization by paragraph extraction, in: I. Mani, M. Maybury (Eds.), Intelligent Scalable Text Summarization, Proceedings of a Workshop, Association of Computational Linguistics, vol. 104, (1997) 39 – 46, http://citeseer.nj.nec.com/ mitra97automatic.html.

[24] M.R. Muddamalle, Natural language versus controlled vocabulary in information retrieval: a case study in soil mechanics, Journal of the American Society for Information Science 49 (10) (1998) 881 – 887.

[25] R. Nader, Statement of Ralph Nader before FOIndiana: FREE-DOM OF INFORMATION, September 21, 1996, http:// www.cptech.org/govinfo/foindiana.html.

[26] K.M. Nelson, A. Kogan, R.P. Srivastava, M.A. Vasarhelyi, H. Lu, Virtual auditing agents: the EDGAR agent challenge, Decision Support Systems 28 (3) (2000) 241 – 253.

[27] PricewaterhouseCoopers, A Technical Overview of the Edgar-Scan System, April 9, 2001, http://edgarscan.pwcglobal.com EdgarScan/edgarscan<sub></sub>arch.html.

[28] B.F. Schwartz, EDGAR Update: the proliferation of commercial products, Legal Information Alert 15 (1) (January 1996) 1 – 5.

[29] Securities and Exchange Commission, Edgar Filer Manual, Release 5.10, SEC, Washington, DC, Sept. 1996.

[30] Securities and Exchange Commission, Staff Legal Bulletin No. 5, October 8, 1997, revised January 12, 1998, http:// www.sec.gov/interps/legal/slbcf5.htm.

[31] Securities and Exchange Commission, Important Information about EDGAR, Sept. 28, 1999, http://www.sec.gov/edgar/ aboutedgar.htm.

[32] Securities and Exchange Commission, Third Report on the Readiness of the United States Securities Industry and Public Companies To Meet the Information Processing Challenges of the Year 2000, July 1999, http://www.sec.gov/news/studies/ yr2000-3.htm.

[33] Securities and Exchange Commission, (undated by R.A. Sanders, and S.K. Das), EDGAR Filer Information: Electronic Filing and the EDGAR System: A Regulatory Overview, Washington, DC, SEC, Nov. 14, 2000, http://www.sec.gov/ info/edgar/overview1100.htm.

[34] Securities and Exchange Commission, EDGAR Filer Information: Electronic Filing and the EDGAR System: A Regulatory Overview, May 15, 2000, http://www.sec.gov/info/edgar/ ednews/edreg2ka.htm.

[35] Securities and Exchange Commission, Final Rule: Rulemaking for EDGAR System: RIN 3235-AH79, Rulemaking for EDGAR System, Nov. 6, 2000, http://www.sec.gov/rules/ final/33-7855.htm.

[36] Securities and Exchange Commission, The Investor’s Advocate: How the SEC Protects Investors and Maintains Market Integrity, Mar. 1, 2001, http://www.sec.gov/about/whatwedo. shtml.

[37] Securities and Exchange Commission, EDGAR Filer Manual v. 8.0, New Version: September 21, 2001, http://www.sec.gov/ info/edgar/filermanual.htm.

[38] Securities and Exchange Commission, Private communication with the SEC’s Internet Support Staff, April 25, 2001.

[39] Securities and Exchange Commission, Private communication with the SEC’s Edgar Program Manager, Nov. 30, 2001.

[40] Securities and Exchange Commission, SEC FOIA Program The Freedom of Information Act: What It Is, What It Does, October 9, 2001, http://www.sec.gov/foia.shtml.

[41] Securities and Exchange Commission, Termination of Legacy EDGAR on April 20, 2001, April 2001, http://www.sec.gov/ info/edgar/ednews/endlegacy.htm.

[42] Securities and Exchange Commission, Edgar Filer Manual, Release 8.0, SEC, Washington, DC, Sept. 2001, http:// www.sec.gov/info/edgar/filermanual.htm.

[43] F. Song, W.B. Croft, A general language model for information retrieval, Proceedings of Eighth International Conference on Information and Knowledge Management, Kansas City, MO, November 2 – 6, http://ciir.cs.umass.edu/pubfiles/ ir-171.pdf.

[44] C. Taylor, Millennium Madness: The History And The Hype, Time.com, (1999), http://www.bobbemer.com/taylor.htm (http://www.bobbemer.com/QUOTES.HTM).

[45] XBRL.org, Extensible Business Reporting Language Specification, version 2.0, 2001, http://www.xbrl.org/tr/2001/xbrl-2001-11-14-draft.doc.

[46] XBRL.org, Overview/Facts Sheet, 2001, http://www.xbrl.org/ Overview.htm.

![](/api/attachments/TCWFMGDZ/fulltext/images/d167ec5747d6035f8bea9250c456d2a98e1152d3fecf61c92358b5d8d4abc57e.jpg)

John Gerdes, Jr. received his BS and M. Eng. Degrees in Mechanical Engineering in 1976 and 1977, respectively, from Cornell University; MBA in 1981 from Lehigh University; MS in Computer Science and PhD in Information Systems in 1994 and 1996, respectively, from Vanderbilt University. He held the position of Visiting Assistant Professor in the Fisher College of Business, Ohio State University from 1996 to 1998. Since 1998, he

has held the position as Assistant Professor in Information Systems at the A. Gary Anderson Graduate School of Management, University of California, Riverside. Research interests include Web Data Mining, Distance Learning, Decision Support Systems and Electronic Commerce.
