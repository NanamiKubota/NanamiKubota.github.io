---
cssclass: research-note
title: {{title}}
authors: {%- for creator in creators -%}{%- if creator.name %} {{creator.name}}{%- else %} {{creator.lastName}}, {{creator.firstName}}{%- endif %}{% if not loop.last %};{% endif %}{% endfor %}
year: {{date | format("YYYY")}}
type: {{itemType}}{% if publicationTitle %}
publication: {{publicationTitle}}{% endif %}{% if archive %}
archive: {{archive}}{% endif %}{% if archiveLocation %}
archive-location: {{archiveLocation}}{% endif %}
date-added: {{dateAdded | format("YYYY-MM-DD")}}
topics: {% for t in tags %}{{t.tag}}{% if not loop.last %}, {% endif %}{% endfor %}
citekey: {{citekey}}
---
# {{title}}

```ad-info
title: Metadata

**Year**: {{date | format("YYYY")}}

**Authors**: {%- for creator in creators -%}{%- if creator.name %} {{creator.name}}{%- else %} {{creator.lastName}}, {{creator.firstName}}{%- endif %}{% if not loop.last %}; {% endif %}{% endfor %}

**Publication**: {{publicationTitle}}

**Zotero tags**: {% for t in tags %}[[{{t.tag}}]]{% if not loop.last %}, {% endif %}{% endfor %}

**Link**: {{url}} 

**Local**: [click to open in zotero](zotero://select/items/@{{citekey}})

**DOI**: [{{DOI}}](http://{{DOI}})

**Date Added**: {{dateAdded | format("YYYY-MM-DD")}}

**Cite Key**: [[@{{citekey}}]]
``` 
{% persist "obsidian_notes" %}

## 🔗 **Topics**:
## 🏷 Tags: #references


```ad-note
title: Summary
color: 255, 221, 51
icon: star

Enter summary of paper here.

```

{% endpersist %}


{% if abstractNote %}
```ad-note
title: Abstract
color: 250, 150, 255
icon: sticky-note

{{abstractNote}}

```

{% endif %}

{%- macro calloutHeader(color) -%}
	{%- switch color -%}
		{%- case "#ffd400" -%} 
			Interesting
		{%- case "#ff6666" -%} 
			Important
		{%- case "#5fb236" -%} 
			Terminology
		{%- case "#2ea8e5" -%} 
			Study-specific
		{%- case "#a28ae5" -%} 
			Misc
		{%- case "#e56eee" -%} 
			Magenta
		{%- case "#f19837" -%} 
			Orange
		{%- case "#aaaaaa" -%} 
			Grey
	{%- endswitch -%} 
{%- endmacro %}

## Annotations 
{% persist "annotations" %}
{% set annots = annotations | filterby("date", "dateafter", lastImportDate) -%}
{% if annots.length > 0 %} 
### Imported on {{importDate | format("YYYY-MM-DD h:mm a")}}

{% for color, annots in annots | groupby("color") -%} 

{% for annot in annots -%} 
> [!quote{% if annot.color %}|{{annot.color}}{% endif %}] {{calloutHeader(annot.color)}} 
{%- if annot.annotatedText %} 
> {{annot.annotatedText | nl2br}} 
{%- endif -%}
{%- if annot.imageRelativePath %} 
> ![[{{annot.imageRelativePath}}]] 
{%- endif %} 
{%- if annot.ocrText %} 
> {{annot.ocrText}} 
{%- endif %} 
{%- if annot.comment %} 
> 
>> {{annot.comment | nl2br}} 
{%- endif %} 
> 
> [Page {{annot.page}}](zotero://open-pdf/library/items/{{annot.attachment.itemKey}}?page={{annot.page}}) {{annot.date | format("YYYY-MM-DD h:mm a")}}

{% endfor -%} 
{% endfor -%} 
{% endif %} 
{% endpersist %}