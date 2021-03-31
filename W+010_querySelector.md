# Duniix Web++ &mdash; a New Way of Webbing the Web

1. Consider these questions:
- a. How would you transfer data in a spreadsheet (Figure 1) to a web page (Figure 2) easily,
using templates cloned from any website of
your choice (including websites such as Google,
 YouTube, Facebook etc.)? 
- b. How would you use YouTube as template and change an entry on the web page with your own JSON data?

- Figure 1
<img src="https://github.com/udexon/Webpp/blob/main/img/Spreadsheet_JSON.png" width=400>

- Figure 2
<img src="https://github.com/udexon/Webpp/blob/main/img/YouTube_DOM.png" width=600>

<!-- readers want a simple to understand example!! -->

Each part of this question sounds like a junior developer's trick.

If you are a senior develop and like challenges, stop reading now and figure it out yourself before continuing!!

A typical setup using conventional tools such as Laravel back end with some front end framework, together with MySQL database etc. would be too cumbersome to accomplish this task, as years of "over engineering" has created dozens of behemoths with severe inflexibilities, that can only work in a few very limited ways.


2. Duniix Web++ consists of modules writte in JavaScript, PHP and Python, integrated using Phoscript, a metaprogramming script derived from the Forth programming language.

Due to unknown historical circumstances, the web ecosystems are constructed within 3 mutually exclusive territories:

- a. front end: JavaScript, HTML
- b. back end: PHP, Node.js, Python Django, etc.
- c. "automation" front end: Selenium Python, Java, Casperjs, Phantonmjs, etc.

The unique stack machine architecture and reverse polish notation syntax of Phoscript allow it to be implemented as a metaprogramming shell easily within any of the programming language and framework mentioned above, as we shall illustrate.

3. Question (1) above will be solved with the 
following use case / modules:

- a. A YouTube page is opened using Python Selenium 
Chrome driver (browser).
- b. `<script>` elements are removed from the page
source and then the page source is saved as a local file.
- c. The cloned local copy of YouTube page
is opened using Selenium Chrome driver again.
- d. Right click on the element that you wish to modify, move the mouse pointer to the last item on the menu "Inspect". The corresponding DOM HTML will be displayed in the Developer Tool window, as shown in figure 3.


- Figure 3
<img src="https://github.com/udexon/Webpp/blob/main/img/DOM_id_meta.png" width=600>

- e. Move the mouse pointer to the following element in the Developer Tool window:
- `<div class="style-scope ytd-rich-grid-media" id="meta">`
Right click on it - Copy - Copy outerHTML, as shown in figure 4.

- Figure 4
<img src="https://github.com/udexon/Webpp/blob/main/img/DOM_outerHTML.png" width=600>

- f. Paste the outerHTML code into a text editor, as shown in figure 5.
- Figure 5
<img src="https://github.com/udexon/Webpp/blob/main/img/DOM_meta_html.png" width=600>

- g. The following code will modify the DOM elements highlighter in blue in figure 3:
```
document.querySelectorAll('#meta')[0].querySelector('#video-title').innerText='Learn English Online'
document.querySelectorAll('#meta')[0].querySelector('#metadata-line').innerText='expired 30 Apr 2021'
document.querySelectorAll('#meta')[0].querySelector('#byline-container').innerText='20% discount'
```
