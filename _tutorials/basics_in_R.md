---
title: "Basics in R"
layout: single
permalink: /tutorials/basics_in_R
toc: true
toc_sticky: true
toc_label: "Table of Contents"
last_modified_at: 2021-07-01
#classes: wide
---

<br>
<i>
Disclaimer:  
I never took a formal CS course so my terminology and explanations of concepts may be questionable at times. Also, my code is usually messy so don't hesitate to email/message me with questions, especially if I don't explain something clearly. (But hey, if everything works, it works!)
</i>

<br>
  
>Tip:  
Google is your friend. 99% of coding relies on if you can Google the right question into the search bar. I recommend going to statexchange and other forums to look for answers. The other 1% relies on whether you can interpret the answer and modify it to fit your needs.

<br>

#  Before you start

1. Install R by going to CRAN which you can access by clicking  [here](https://cran.r-project.org/mirrors.html). Find a URL which is closest to you (for Pittsburgh people, this will be [Statlib, Carnegie Mellon University](http://lib.stat.cmu.edu/R/CRAN/)). Click on the Download link to whichever operating system you're working in (Linux, macOS, or Windows) and follow the directions.  
    
    * <u>Windows</u>: click on the hyperlink, "install R for the first time" and then click the download R link.  
    
    * <u>macOS</u>: this is a bit trickier and will heavily depend on whether you have Intel or the Apple Silicon processor. More details below...  
    
    For macOS users, you need to check which version of macOS you're running on and also which processor (i.e. Intel or Apple silicon). You can check this by clicking on the apple icon on the top left of your screen, and selecting *About This Mac* from the dropdown menu.  
    
    If you are using an older version of the macOS (i.e. Intel based), then next to *Processor*, it should say Intel:  
      
    ![](/images/macos_version.png)
    
    If you are using the newer Apple M1 macbooks which uses Apple silicon, then next to *Chip*, it should say Apple M1 instead of Intel:  
      
    ![](/images/macos_m1.jpeg)
    
    If you are using <b>Intel</b> on a macOS version that is 10.9 (i.e. Mavericks) or later, then you need to also install [XQuartz](https://www.xquartz.org/). Then you will <b>install R-4.1.0.pkg</b> and NOT the R-4.1.0-arm64.pkg.
    
    If you are using <b>Apple M1</b> on a macOS version that is 11.0 (i.e. Big Sur) or later, then you need to <b>install R-4.1.0-arm64.pkg</b>. You may still need to install [XQuartz](https://www.xquartz.org/). <b><u>Important: This package will not work if your processor is Intel based!!!</u></b>  
      
    ![](/images/R_download_page.png)
  
2. Download the free version of [RStudio Desktop](https://www.rstudio.com/products/rstudio/download/). This is an Integrated Development Environment (IDE) where you will write your code. You can technically write directly in R instead of RStudio but for the sake of making your life easier, please don't do this. The free version works fine for our purpose.  

![](/images/rstudio_download.png)

After you get to the Download page, scroll down until you see the free download version and click *DOWNLOAD*. Or alternatively, go [here](https://www.rstudio.com/products/rstudio/download/#download).

![](/images/rstudio_free.png)
  
3. Run line-by-line by pressing *Cmd+Enter* or *Ctrl+Enter*.  

4. Eventually, after a couple of months/years of using R you may get updates for R, for the packages that you have installed in R, or even for your operating system. Beware when you update anything (this includes big Windows and macOS updates). Some things may be dependent on other packages or may work only on certain versions of R or operating systems, and they could potentially stop cooperating if you update things. Just double check and make sure you can revert to an old version should things go south.  

<br>  
  
***
  
<br>

# RStudio Basics

## Intoduction
  
When you first open RStudio, you will get 4 panels and each panel will have a different purpose. Don't worry if you only see 3 panels--you may just need to open an R script file which will be covered later.  

![](/images/RStudio_overview.png)

<br>

<u>Top left panel</u>: This is where you will write your code. Think of it like a Word document. Once you write your line of code, you can press *Cmd*+*Enter* (or *Ctrl*+*Enter*) to run a single line of code.

<u>Bottom left panel</u>: This is your console. You can technically write your code directly in here but since you'll eventually want to save your code, try to write it in the top left panel.

<u>Top right panel</u>: You will see all of the variables that you have named and data that you have loaded here. You don't need to worry about this at the moment.

<u>Bottom right panel</u>: This is where your plots will appear if you plotted data. You can also read the help documentation from here by using the help( ) function or writing a ? (question mark) before the function to learn more about that function. I will explain this is in the *2.5 Getting help* section.

## Open a new document

There are two types of documents that will be of useful for you. For the sake of this tutorial, you can focus on R script files for now. R script files are good for writing just code and a few comments here and there. If you are feeling more advanced, you can use the R markdown document. This is more useful if you want to write notes down and keep track of what you did kind of like a lab notebook.

Open a new R Script document by going to *File* -> *New File* -> *R Script*, or you can press on the top right button with the green plus sign and click *R Script* from the dropdown menu (as seen in the picture below).

<br>

![](/images/new_doc.png)

## Installing and loading packages

Installing packages only needs to be done once. Once you have installed a package, all you need to do is load the package everytime you need to use it in a new R session.  

This step is for users installing the package, *car*, for the first time and this only needs to be done once.
  
Go to *Tools* located at the top and click *Install Packages*. Then under the *Packages* search bar search for "car" and select car once it comes up. Then check off *Install dependencies* and click *Install*.  

![](/images/install_package.png)

<br>

![](/images/car_package.png)

<br>

![](/images/dependencies.png)

<br>

You only need to install a particular package once. Once you do, every time you have a new R session, you must load that package so that R can access it by using the following function:  

```r
library(car)
```


##  Set your working directory

Always begin by setting your working directory. The directory is the location of the folder where you would like to work from. Generally, you will have you data, plots, and R script within this folder to work from. You can do this manually by going to the top menu bar and click *Session* -> *Set Working Directory* -> *Choose Directory...*. 

<br>

![*Session* -> *Set Working Directory* -> *Choose Directory...*](/images/working_directory.png)
<br><br>

Your life will be easier if you copy/paste the line of code that is generated in the console after this and incorporate it into your script for future reference. That way you can just press *Cmd*+*Enter* to set your working directory everytime you need to run some code, instead of manually entering it each time via the dropdown menu. The below is my working directory and <u>this will be different for every person</u>:

```r
setwd("~/Documents/PMI/2021 Summer/R tutorial")
```
<br>

## Functions

A function is a command that you write and run so that R can do that command on another object. For example, in the previous section we manually set the working directory, which produced a line of code using the setwd( ) function. Using the setwd( ) function, we are able to set the working directory to our folder of choice by writing the file path to that folder. In my example, my file path is "~/Documents/PMI/2021 Summer/R tutorial".  

Usually, functions are written in the following format:  

```r
function(x)
```

<br> 

Where x is the object you would like to pass through the function. The above example is a very simple one, and some functions can require you to pass multiple objects through it. In order to know what you need to enter within the paranthesis, I recommend that you look at the documentation for the function or look up examples on how to use the function online. We will cover how to look at documentation for functions in the next section.

## Getting help

As you start to use different functions, you may want to look at the documentation on that function in case you get stuck or need to learn more about a particular function.  

Let's say you want to learn more about the plot( ) function. You can look at the documentation for plot( ) by doing the following:  

```r
help("plot")
```

An alternative to this (which I prefer since it's faster to type out) is:  

```r
?plot
```


***

#  Notations
##  Adding comments

In an R script, anything after the # mark in a line of code will be considered a comment (a string of characters that R ignores). Not adding the # when you write a comment can give you an error since R will think it's part of the code and try to run it.  

Writing comments are helpful especially if you want to be able to look back at your script and know the purpose of each line of code. It is also helpful for anyone who needs to use and understand your script. To write a comment:  

```r
#This is how to write a proper comment
```

<br>

If you are using R markdown, you do not need to use # to write comments unless you plan to write comments inside a code block (which you can produce by pressing *Cmd+Alt+I*). Ignore this if you are using R Script.

<br>


