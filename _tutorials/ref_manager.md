---
title: "Zettelkasten Method: Zotero-Obsidian reference manager pipeline"
layout: single
permalink: /tutorials/ref_manager
toc: true
toc_sticky: true
toc_label: "Table of Contents"
last_modified_at: 2023-07-09
hidden: true
---

<br>
<i>
Disclaimer: Setting up this pipeline is a bit tedious which is why I have decided to write it up. You may need to play around a bit to find the best method for your note-keeping system and style. Your mileage may also vary if the version numbers are different from mine. Please let me know if you run into issues.
</i>

<div class="notice--info">
  <b>Version control:</b> The following are the versions that I have installed for Zotero, Obsidian, and their respective add-ons/plugins. The bolded ones are required or highly recommended for this tutorial. The others are optional and my personal preference (they are still nice to have but not required).
  <ul>
    <li><b>Zotero v6.0.31</b></li>
        <ul>
            <li><b>Better BibTex for Zotero v6.7.148</b></li>
            <li><b>DOI Manager v1.4.2</b></li>
            <li><b>Mdnotes for Zotero v0.2.3</b></li>
            <li><b>ZotFile 5.1.2</b></li>
            <li><b>Zutilo Utility for Zotero v3.10.0</b></li>
        </ul>
    <li><b>Obsidian v1.1.9 (Installer v1.0.3)</b></li>
        <ul>
            <li><b>Admonition v10.1.1</b></li>
            <li>Advanced Tables v0.19.1</li>
            <li>Calendar v1.5.10</li>
            <li><b>Citations v0.4.5</b></li>
            <li>Dataview v0.5.64</li>
            <li><b>Editor Syntax Highlight v0.1.3</b></li>
            <li>Find orphaned files and broken links v1.9.2</li>
            <li><b>Highlightr v1.2.2</b></li>
            <li>Icon Folder v2.8.0</li>
            <li>Minimal Theme Settings v7.3.1</li>
            <li>Recent Files v1.3.8</li>
            <li>Spaced Repetition v1.10.5</li>
            <li><b>Style Settings v1.0.7</b></li>
            <li><b>Templater v1.18.4</b></li>
            <li><b>Zotero Integration v3.1.7</b></li>
        </ul>
  </ul>
</div>

# Preface

The motivation for this tutorial stems from the problem that I ran into while reading papers and writing notes in just a reference manager. Too many times would I read a paper and forget the content of the paper after a few days, often times being unable to recall the experiments, findings, or even the background information of a paper. In addition to this, there were many times where I will remember a piece of information but not be able to recall from which paper I read it from. The most difficult issue to solve was how I had trouble connecting ideas from different papers, especially if I couldn't remember the author name or title that the ideas originated from.

The Zotero-Obsidian pipeline helps fix many of these issues. While tedious in its setup, not to mention writing up notes is more time-consuming than just highlighting a PDF file, I can say it is worthwhile in the long run. I find it helpful that I am making my own Wikipedia where I can search by topic and find relevant notes from various papers, rather than having to sift through papers to read notes.

## Why you should have a reference manager

This section is more tailored to students (like high school students and undergrads) who are just getting into hitting the books and reading more papers that cover specialized topics. Hopefully, students who are further along in their research career will already have a reference manager to keep track of their notes. 

But if you don't have one, having a reference manager is a starting point to keeping track of papers that you've read. Most reference managers will let you directly write notes and highlight PDF file. This is a great way to take quick notes as you read papers.

However, once you have many papers to keep track of, linking ideas across different papers or even remembering the contents of a paper may become more difficult. This is where using Obsidian and implementing the Zettelkasten system

## Obsidian to organize notes (Zettelkasten Method)

TBU

There are many YouTube and blog posts on the Zettelkasten method. I recommend looking it up as this is the note-taking method that I will be employing for the following tutorial.

## ResearchRabbit to find papers

Once you have your Zotero set up and have at least a few papers on there, I recommend using ResearchRabbit and link your Zotero library to this service. ResearchRabbit will be able to take a look at all of your references in your library or folder, and create a list of relevant papers that are not in your library. 

[Read more about ResearchRabbit on their official website here.](https://www.researchrabbit.ai/)

Note: there is a limit to how many papers ResearchRabbit will look at so breaking down your library into smaller subfolders by category may be helpful if you have a large collection. In my case, I currently have a folder for Pf phage papers, a folder for evolutionary game theory papers, a folder for cheater viruses, and a folder for clinically-relevant mutations in <i>Pseudomonas aeruginosa</i>. There is overlap between all folders but this helps cut down the number of papers ResearchRabbit can look through.

# Download Zotero

TBU

You can download Zotero for free from the [Zotero website](https://www.zotero.org/). The first 300 MB of storage is free, then you can pay to further increase storage space. You don't necessarily need the extra storage if you are okay with saving everything on just your local computer and not have an online storage space as backup. The space quota is for the online sync storage space, which is nice to have as a safety net. 

Zotero is made by a nonprofit and is open-source, which means users can volunteer to contribute and provide add-ons that enhance your experience. This includes add-ons that makes it easier to import notes and metadata into Obsidian.

## Settings

The following are the plugins that I have installed on Zotero:

Zotero v6.0.31:
- Better BibTex for Zotero v6.7.148
- DOI Manager v1.4.2
- Mdnotes for Zotero v0.2.3
- ZotFile 5.1.2
- Zutilo Utility for Zotero v3.10.0

These plugins help me import metadata from Zotero, including but not limited to author names, journal name, year published, abstract, etc. The plugins also help me import any highlights that I made on the PDF file. These include words highlighted using the highter (including the color that I used), as well as figures that I've circled with the "Area" tool and notes I've written with the "Post-it" tool.

# Download Obsidian

Obsidian can be downloaded for free from the [official Obsidian website](https://obsidian.md/). Once you have that downloaded, I put my Obsidian folder under my Documents folder and created a vault called "Literature Notes". You can name your vault anything. I keep ALL of my reference notes in one vault.

## Settings

The following are the community plugins that I have installed into Obsidian.

<b>Obsidian v1.1.9 (Installer v1.0.3)</b>
- <b>Admonition v10.1.1</b>
- Advanced Tables v0.19.1
- Calendar v1.5.10</li>
- <b>Citations v0.4.5</b>
- Dataview v0.5.64
- <b>Editor Syntax Highlight v0.1.3</b>
- Find orphaned files and broken links v1.9.2
- <b>Highlightr v1.2.2</b>
- Icon Folder v2.8.0
- Minimal Theme Settings v7.3.1
- Recent Files v1.3.8
- Spaced Repetition v1.10.5
- <b>Style Settings v1.0.7</b>
- <b>Templater v1.18.4</b>
- <b>Zotero Integration v3.1.7</b>

The bolded plugins are required or highly recommended. The other plugins are optional and not necessary for the purposes of this tutorial.

## Scripts and templates

Under your vault folder (in my case, it will be "Literature Notes"), make a folder named "templates" and add the following markdown files in the templates folder:

- [idea_template.md](https://github.com/NanamiKubota/NanamiKubota.github.io/blob/main/scripts/idea_template.md)
- [notes_template.md](https://github.com/NanamiKubota/NanamiKubota.github.io/blob/main/scripts/notes_template.md)
- [refrences_template.md](https://github.com/NanamiKubota/NanamiKubota.github.io/blob/main/scripts/references_template.md)

The template above will help extract and format your reference metadata and your notes/idea into a standardized format. Feel free to customize the templates to suite your needs.

### Reference template

TBU

#### highlighter

I like to use different highlighter colors in Zotero to signify different things as I am reading a paper. For example, for general portions of the text that I find important, I will use the yellow highlighter. For really important information, I use the red highlighter. For terminology or explanation of abbreviations, I use green. Blue is reserved for methods or hypotheses that the authors used for the paper. And the purple color is for miscellaneous pieces of information, such as cited references that I would like to go back and read further. 

Since setting up my Zotero-Obsidian pipeline, Zotero has increased the number of colors that can be used 

#### CSS

The CSS allows Obsidian to take your Zotero highlights and highlight color from the PDF and convert them into text blocks with the appropriate color. This script is needed for the reference template to work properly. Otherwise, Obsidian will not know what color to make the text block based off of the highlighter color.

The css file needs to be within a hidden folder in your vault named, ".obsidian" > "snippets". In your snippets folder, create a "callouts.css" with the following in the css file:

```CSS
/* Yellow */
.research-note .callout[data-callout-metadata="#ffd400"] {
  --callout-color: 255, 204, 0;
}

/* Red */
.research-note .callout[data-callout-metadata="#ff6666"] {
  --callout-color: 255, 59, 48;
}

/* Green */
.research-note .callout[data-callout-metadata="#5fb236"] {
  --callout-color: 40, 205, 65;
}

/* Blue */
.research-note .callout[data-callout-metadata="#2ea8e5"] {
  --callout-color: 0, 122, 255;
}

/* Purple */
.research-note .callout[data-callout-metadata="#a28ae5"] {
  --callout-color: 125, 84, 222;
}

/* Magenta */
.research-note .callout[data-callout-metadata="#e56eee"] {
  --callout-color: 229, 110, 238;
}

/* Orange */
.research-note .callout[data-callout-metadata="#f19837"] {
  --callout-color: 241, 152, 55;
}

/* Grey */
.research-note .callout[data-callout-metadata="#aaaaaa"] {
  --callout-color: 170, 170, 170;
}
```

### Notes templates

## Links and tags

When you first start using Obsidian, you may be confused what links and tags are and how they are different. Links are used to connect documents (references, notes, and ideas) with other related documents. Linking documents will help make connections in your graph, and will later help you link ideas from different papers together.

Tags are used to categorize documents by document type. For example, I categorize documents either as reference, note, or idea. You may use your own system but this categorization has helped me navigate my notes better.

- reference: used to tag documents that contain metadata from papers imported from Zotero.
- note: a word/terminology (think words found in dictionaries or Wikipedia pages)
- idea: a sentence that condenses a concept or idea or fact, either from literature or my own ideas/hypotheses
  - I further differentiate my ideas from others by adding a question mark emoji at the start of the document title and by adding a question mark tag. 

## Graph view

Once you start linking your references with your notes and ideas, as well as linking notes to ideas, Obsidian will begin making a web-like graph that shows the connections between linked documents (i.e. nodes). You can view your graph by opening "graph view" (there is a button located on the left).

To color your nodes by category (references, ideas, and notes), you can pick a color under the Groups dropdown menu and select your category. Note that the order of your subgroups are important in that the subgroups at the top will be prioritized in the event that the node falls into multiple categories.

To hide your template documents from showing up as nodes, add this to the search bar:
```
-path:templates -path:search
```

These will hide your documents under your templates folder.

