---
title: "Managing papers and notes: Zotero-Obsidian pipeline"
layout: single
permalink: /tutorials/ref_manager
toc: true
toc_sticky: true
toc_label: "Table of Contents"
last_modified_at: 2025-09-03
hidden: true
---

<br>
<i>
Disclaimer: Setting up this pipeline is a bit tedious which is why I have decided to write it up. You may need to play around a bit to find the best method for your note-keeping system and style. Your mileage may also vary if the version numbers are different from mine. Please let me know if you run into issues.
</i>

<div class="notice--info">
  <b>Version control:</b> The following are the versions that I have installed for Zotero, Obsidian, and their respective add-ons/plugins. The bolded ones are required or highly recommended for this tutorial. The others are optional and my personal preference (they are still nice to have but not required).
  <ul>
    <li><b>Zotero v7.0.15</b></li>
        <ul>
            <li><b>Better BibTex for Zotero v6.7.225</b></li>
            <li><b>DOI Manager v1.5.0</b></li>
        </ul>
    <li><b>Obsidian v1.8.10 (Installer v1.6.7)</b></li>
        <ul>
            <li><b>Admonition v10.3.2</b></li>
            <li>Advanced Tables v0.21.0</li>
            <li><b>Dataview v0.5.67</b></li>
            <li>Editor Syntax Highlight v0.1.3</li>
            <li>Find orphaned files and broken links v1.10.1</li>
            <li><b>Highlightr v1.2.2</b></li>
            <li><b>Iconize v2.14.3</b></li>
            <li>Minimal Theme Settings v8.1.1</li>
            <li>Recent Files v1.4.1</li>
            <li><b>Style Settings v1.0.9</b></li>
            <li><b>Templater v2.4.2</b></li>
            <li><b>Zotero Integration v3.2.1</b></li>
        </ul>
  </ul>
</div>

***

<br>

# Preface

<br>

The motivation for this tutorial stems from the problem that I ran into while reading papers and writing notes in just a reference manager. Too many times would I read a paper and forget the content of the paper after a few days, often times being unable to recall the experiments, findings, or even the background information of a paper. In addition to this, there were many times where I will remember a piece of information but not be able to recall from which paper I read it from. The most difficult issue to solve was how I had trouble connecting ideas from different papers, especially if I couldn't remember the author name or title that the ideas originated from.

The Zotero-Obsidian pipeline helps fix many of these issues. While tedious in its setup, not to mention writing up notes is more time-consuming than just highlighting a PDF file, I can say it is worthwhile in the long run. I find it helpful that I am making my own Wikipedia where I can search by topic and find relevant notes from various papers, rather than having to sift through papers to read notes.

<br>

## Why you should have a reference manager

<br>

This section is more tailored to students (like high school students and undergrads) who are just getting into hitting the books and reading more papers that cover specialized topics. Hopefully, students who are further along in their research career will already have a reference manager to keep track of their notes. 

But if you don't have one, having a reference manager is a starting point to keeping track of papers that you've read. Most reference managers will let you directly write notes and highlight PDF file. This is a great way to take quick notes as you read papers.

However, once you have many papers to keep track of, linking ideas across different papers or even remembering the contents of a paper may become more difficult. This is where using Obsidian and implementing the Zettelkasten system

<br>

## Obsidian to organize notes (Zettelkasten Method)

<br>

There are many YouTube and blog posts on the Zettelkasten method. I recommend looking it up as this is the note-taking method that I use for the following tutorial.

<br>

## ResearchRabbit to find papers

<br>

Once you have your Zotero set up and have at least a few papers on there, I recommend using ResearchRabbit and link your Zotero library to this service. ResearchRabbit will be able to take a look at all of your references in your library or folder, and create a list of relevant papers that are not in your library. 

[Read more about ResearchRabbit on their official website here.](https://www.researchrabbit.ai/)

Note: there is a limit to how many papers ResearchRabbit will look at so breaking down your library into smaller subfolders by category may be helpful if you have a large collection. In my case, I currently have a folder for Pf phage papers, a folder for evolutionary game theory papers, a folder for cheater viruses, and a folder for clinically-relevant mutations in <i>Pseudomonas aeruginosa</i>. There is overlap between all folders but this helps cut down the number of papers ResearchRabbit can look through.

<br>

***

<br>

# Download Zotero

<br>

You can download Zotero for free from the [Zotero website](https://www.zotero.org/). The first 300 MB of storage is free, then you can pay to further increase storage space. You don't necessarily need the extra storage if you are okay with saving everything on just your local computer and not have an online storage space as backup. The space quota is for the online sync storage space, which is nice to have as a safety net. 

Zotero is made by a nonprofit and is open-source, which means users can volunteer to contribute and provide add-ons that enhance your experience. This includes add-ons that makes it easier to import notes and metadata into Obsidian.

<br>

## Settings

<br>

The following are the plugins that I have installed on Zotero:

Zotero v7.0.15:
- Better BibTex for Zotero v6.7.225
- DOI Manager v1.5.0

These plugins help me import metadata from Zotero, including but not limited to author names, journal name, year published, abstract, etc. The plugins also help me import any highlights and notes that I made on the PDF file. These include words highlighted using the highter (including the color that I used), as well as figures that I've circled with the "Area" tool.

To download, go to the [Zotero plugin webpage](https://www.zotero.org/support/plugins) and search for the plugin. Follow the instructions for each plugin as written.

<br>

***

<br>

# Download Obsidian

<br>

Obsidian can be downloaded for free from the [official Obsidian website](https://obsidian.md/). Once you have that downloaded, I put my Obsidian folder under my Documents folder and created a vault called "Literature Notes". You can name your vault anything. I keep ALL of my reference notes in one vault.

<br>

## Settings

<br>

The following are the community plugins that I have installed into Obsidian.

<b>Obsidian v1.8.10 (Installer v1.6.7)</b>
- <b>Admonition v10.3.2</b>
- Advanced Tables v0.21.0
- <b>Dataview v0.5.67</b>
- Editor Syntax Highlight v0.1.3
- Find orphaned files and broken links v1.10.1
- <b>Highlightr v1.2.2</b>
- <b>Iconize v2.14.3</b>
- Minimal Theme Settings v8.1.1
- Recent Files v1.4.1
- <b>Style Settings v1.0.9</b>
- <b>Templater v2.4.2</b>
- <b>Zotero Integration v3.2.1</b>

<br>

The bolded plugins are required or highly recommended. The other plugins are optional and not necessary for the purposes of this tutorial.

In addition to this, make sure that under the "Core plugins" tab that the following plugins are turned on:
- Backlinks
- Command palette
- File recovery
- Graph view
- Note composer
- Outgoing links
- Page preview
- Quick switcher
- Search
- Templates

<br>

For the Templates core plugin, make sure to either click the gear icon next to it or click on the Templates tab on the left and type "templates" for "Template folder location":

![](/images/template_obsidian.png){: .image-center}

<br>

For the Zotero Integration community plugin, make sure to set the following settings:

![](/images/zotero_integrate1.png){: .image-center}

![](/images/zotero_integrate2.png){: .image-center}

![](/images/zotero_integrate3.png){: .image-center}

<br>

## Scripts and templates

<br>

Under your vault folder (in my case, it will be "Literature Notes"), make a folder named "templates" and add the following markdown files in the templates folder (make sure to remove the underscore in the filename when saving to your computer):

- [idea_template.md](https://github.com/NanamiKubota/NanamiKubota.github.io/blob/main/scripts/obsidian/_idea%20template.md)
- [notes_template.md](https://github.com/NanamiKubota/NanamiKubota.github.io/blob/main/scripts/obsidian/_notes%20template.md)
- [refrences_template.md](https://github.com/NanamiKubota/NanamiKubota.github.io/blob/main/scripts/obsidian/_references%20template.md)

The template above will help extract and format your reference metadata and your notes/idea into a standardized format. Feel free to customize the templates to suite your needs.

To get the highlighter color to translate from Zotero to Obsidian, download the following CSS file (make sure to remove the underscore in the filename when saving to your computer):

[callouts.css](https://github.com/NanamiKubota/NanamiKubota.github.io/blob/main/scripts/obsidian/_callouts.css)

Save the css file under "Literature Notes" > ".obsidian" > "snippets". The ".obsidian" folder is hidden folder at least on Mac, so make sure that you are able to see hidden folders by doing Command + Shift + . (period) in Finder. If there is no "snippets" folder, make sure that all Obsidian plugins are installed before proceeding.

After saving the css file under snippets, make sure to go back to the Obsidian settings (click the gear icon) and go to Appearance. Scroll down to the "CSS snippets" section and make sure that the callouts is turned on. You may need to click the refresh button for the callouts to show up.

![](/images/callouts_snippets.png){: .image-center}

<br>

### Reference template

The reference template will allow you to seamlessly import metadata and your notes (including text that you highlighted) from Zotero into Obsidian.

<br>

#### Highlighter

I like to use different highlighter colors in Zotero to signify different things as I am reading a paper. For example, for general portions of the text that I find important, I will use the yellow highlighter. For really important information, I use the red highlighter. For terminology or explanation of abbreviations, I use green. Blue is reserved for methods or hypotheses that the authors used for the paper. And the purple color is for miscellaneous pieces of information, such as cited references that I would like to go back and read further. 

Your highlighting scheme might be different than mine. To customize what each highlighter color means and its corresponding icon when importing to Obsidian, edit the references_template.md for the color and callouts.css file for the icon as needed.

For the references_template.md, go to this section and change the labels to your scheme. For example, if your yellow highlight means "Question", change "Interesting" to "Question".

```
{%- macro calloutHeader(color) -%}
	{# 
		Change the labels below so the highlight color aligns with your highlight scheme
		For example, if your yellow highlight means "Question", change "Interesting" to "Question" below:
	#}
	{%- switch color -%}
		{%- case "yellow" -%}
			Interesting
		{%- case "red" -%}
			Important
		{%- case "green" -%}
			Terminology
		{%- case "blue" -%}
			Study-specific
		{%- case "purple" -%}
			Misc
		{%- case "orange" -%}
			Misc
		{%- case "magenta" -%}
			Misc
		{%- case "grey" -%}
			Misc
	{%- endswitch -%}
{%- endmacro %}
```


<br>

#### CSS

The CSS allows Obsidian to take your Zotero highlights and highlight color from the PDF and convert them into text blocks with the appropriate color. This script is needed for the reference template to work properly. Otherwise, Obsidian will not know what color to make the text block based off of the highlighter color.

The css file needs to be within a hidden folder in your vault named, ".obsidian" > "snippets". 

If you want to change the associated icons to your highlight color, change them on the callout-icon lines.

The list of possible icons can be found here: https://lucide.dev/icons/

Put the icon name after "lucide-". Ex: for the "heart" icon, type "lucide-heart"

More info on Obsidian and icons can be found here: https://docs.obsidian.md/Reference/CSS+variables/Foundations/Icons

```css
/* Yellow */
.research-note 
.callout[data-callout-metadata="#ffd400"] {
  --callout-color: 255, 212, 0 !important;
}
.callout[data-callout="yellow"] {
  --callout-color: 255, 212, 0 !important;
  --callout-icon: lucide-star; /* change icon here */
}

/* Red */
.research-note 
.callout[data-callout-metadata="#ff6666"] {
  --callout-color: 255, 102, 102 !important;
}
.callout[data-callout="red"] {
  --callout-color: 255, 102, 102 !important;
  --callout-icon: lucide-alert-circle; /* change icon here */
}

/* Orange */
.research-note
.callout[data-callout-metadata="#f19837"] {
  --callout-color: 241, 152, 55 !important;
}
.callout[data-callout="orange"] {
  --callout-color: 241, 152, 55 !important;
  --callout-icon: lucide-quote; /* change icon here */
}

/* Green */
.research-note
.callout[data-callout-metadata="#5fb236"] {
  --callout-color: 95, 178, 54 !important;
}
.callout[data-callout="green"] {
  --callout-color: 95, 178, 54 !important;
  --callout-icon: lucide-book-open; /* change icon here */
}

/* Blue */
.research-note
.callout[data-callout-metadata="#2ea8e5"] {
  --callout-color: 46, 168, 229 !important;
}
.callout[data-callout="blue"] {
  --callout-color: 46, 168, 229 !important;
  --callout-icon: lucide-flask-conical; /* change icon here */
}

/* Magenta */
.research-note
.callout[data-callout-metadata="#e56eee"] {
  --callout-color: 229, 110, 238 !important;
}
.callout[data-callout="magenta"] {
  --callout-color: 229, 110, 238 !important;
  --callout-icon: lucide-quote; /* change icon here */
}

/* Purple */
.research-note
.callout[data-callout-metadata="#a28ae5"] {
  --callout-color: 162, 138, 229 !important;
}
.callout[data-callout="purple"] {
  --callout-color: 162, 138, 229 !important;
  --callout-icon: lucide-quote; /* change icon here */
}

/* Grey */
.research-note
.callout[data-callout-metadata="#aaaaaa"] {
  --callout-color: 170, 170, 170 !important;
}
.callout[data-callout="grey"] {
  --callout-color: 170, 170, 170 !important;
  --callout-icon: lucide-quote; /* change icon here */
}
```



<br>

### Notes templates

I use the "Notes" template to create a file on a certain terminology. This is different from my "Idea" template which I use for more conceptual notes that are usually a sentence long. Think of a "Notes" file as an entry on Wikipedia. It is usually a webpage on a topic with various subsections and contains links to other pages.

The notes files are especially useful if you quickly want to find relevant ideas/concepts on the topic or references on the topic.

<br>

### Idea templates

The idea template is used to create more conceptual notes. For example, if I read a paper and wanted to write down a concept such as "Pyocyanin can function as an electron transfer facilitator to increase ATP production in an anoxic environment", I can use the idea template to create a file with this title and link it back to the paper that this concept came from. 

This way, when I open the reference page that I created in Obsidian, I can quickly see the different notes and ideas discussed in the paper. Likewise, if I see the idea file, I can quickly figure out which paper this concept came from.

Additionally, I can link other concepts and notes to this idea page so that this page will appear whenever I am on a related page.

<br>

## Links and tags

When you first start using Obsidian, you may be confused what links and tags are and how they are different. Links are used to connect documents (references, notes, and ideas) with other related documents. Linking documents will help make connections in your graph, and will later help you link ideas from different papers together.

Tags are used to categorize documents by document type. For example, I categorize documents either as reference, note, or idea. You may use your own system but this categorization has helped me navigate my notes better.

- reference: used to tag documents that contain metadata from papers imported from Zotero.
- note: a word/terminology (think words found in dictionaries or Wikipedia pages)
- idea: a sentence that condenses a concept or idea or fact, either from literature or my own ideas/hypotheses
  - I further differentiate my ideas from others by adding a question mark emoji at the start of the document title and by adding a question mark tag. 

<br>

## Graph view

Once you start linking your references with your notes and ideas, as well as linking notes to ideas, Obsidian will begin making a web-like graph that shows the connections between linked documents (i.e. nodes). You can view your graph by opening "graph view" (there is a button located on the left).

To color your nodes by category (references, ideas, and notes), you can pick a color under the Groups dropdown menu and select your category. Note that the order of your subgroups are important in that the subgroups at the top will be prioritized in the event that the node falls into multiple categories.

To hide your template documents from showing up as nodes, add this to the search bar:
```
-path:templates -path:search
```

These will hide your documents under your templates folder.

<br>

# Import your first reference

Now you are ready to import your first reference paper from Zotero to Obsidian! First, make sure that Zotero is also running. Then in Obsidian, open the Command palette by doing Command + P (you will need to toggle on the core plugin to use this shortcut). Then start typing "Zotero Integration", and you should hopefully see your reference template pop up as an option.

Pick the paper that you want to import and hit enter. Your reference should be imported!

You can also assign keyboard shortcuts to make this process faster. Just go to Settings > Hotkeys. Then search "Zotero" and change the "Zotero Integration: references template" section. For me, I've set mine as Command + R. Make sure the shortcut isn't used by a different command.

![](/images/obsidian_keyboard_shortcut.png){: .image-center}

<br>

# Create a new note/idea page

In Obsidian, create a new file via Command + N. Type in the title on the file and then open the Command palette (Command + P). Type in "templates: Insert template" and click on either the idea or note template.

You can also make a new note by creating a new link within another file. To do so, write the note within two square brackets "[[Example title here]]". Then, click on the link and this should create a new file for you. Then in the Command palette, type in "templates: Insert template" and click on either the idea or note template.

You can also create keyboard shortcuts for this too. As mentioned in the earlier section, just go to Settings > Hotkeys. Then search "templates" and assign the keyboard shortcut for "Templates: Insert template". For me, I've assigned mine as Command + =. Make sure the shortcut isn't used by a different command.

![](/images/obsidian_keyboard_shortcut2.png){: .image-center}


<br>