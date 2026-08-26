Screen this single AIS Basket article using the complete criteria in the system prompt.

Article metadata:

- record_id: {record_id}
- source_file: {source_file}
- title: {title}
- authors: {authors}
- year: {year}
- journal: {journal}
- doi: {doi}
- fulltext_chars: {fulltext_chars}

The article text is evidence for the source-paper assessment. The coding-agent transfer portion is your explicitly labeled analytical inference. Do not claim that the article discusses coding agents unless the text actually does.

<ARTICLE_FULLTEXT>
{fulltext}
</ARTICLE_FULLTEXT>

Return exactly one JSON object matching the required schema.
