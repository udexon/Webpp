# Duniix Web++ &mdash; a New Way of Webbing the Web (Part I)
- _Phoscript Metaprogramming &mdash; Makes Programming as Easy as Manipulating Spreadsheets_

1. Consider these questions:
- a. How would you transfer data in a spreadsheet (Figure 1) 
to a web page (Figure 2, top left thumbnail) easily,
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

If you are a senior developer and like challenges, stop reading now and figure it out yourself before continuing!!

- We also wish to highlight that the metaprogramming techniques introduced with Duniix Phoscript will make web programming as simple as manipulating spreadsheet &mdash; something accessibe to even ___NON PROGRAMMMERS___ !!!

A typical setup using conventional tools such as Laravel back end with some front end framework, together with MySQL database etc. would be too cumbersome to accomplish this task, as years of "over engineering" has created dozens of behemoths with severe inflexibilities, that can only work in a few very limited ways.


2. Duniix Web++ consists of modules writte in JavaScript, PHP and Python, integrated using Phoscript, a metaprogramming script derived from the Forth programming language.

Due to unknown historical circumstances, the web ecosystems are constructed within 3 mutually exclusive territories:

- a. front end: JavaScript, HTML
- b. back end: PHP, Node.js, Python Django, etc.
- c. "automation" front end: Selenium Python, Java, Casperjs, Phantomjs, etc.

The unique stack machine architecture and reverse polish notation syntax of Phoscript allow it to be implemented as a metaprogramming shell easily within any of the programming language and framework mentioned above, as we shall illustrate.

3. Question (1) above will be solved with the 
following use case / modules:

- a. A YouTube page is opened using Python Selenium 
Chrome driver (browser).
- b. `<script>` elements are removed from the page
source and then the page source is saved as a local file.
 See [W+009](https://github.com/udexon/Webpp/blob/main/W%2B009_Remove_script.md) 
for details.
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

- g. The following code will modify the DOM elements highlighted in blue in figure 3:
```
document.querySelectorAll('#meta')[0].querySelector('#video-title').innerText='Learn English Online'
document.querySelectorAll('#meta')[0].querySelector('#metadata-line').innerText='expired 30 Apr 2021'
document.querySelectorAll('#meta')[0].querySelector('#byline-container').innerText='20% discount'
```

- f. `#meta` in `querySelectorAll()` selects all elements with `id="meta"`.
  -  `[0]` in `document.querySelectorAll('#meta')[0]` returns the first selected element, i.e. the top left thumbnail as shown in figure 3.
  -  `document.querySelectorAll('#meta')[0]` can be cascaded to select child element:
```
querySelector('#video-title')
querySelector('#metadata-line')
querySelector('#byline-container')
```
  - Finally, the selected element `.innerText` property is modified accordingly.

4. Item (3) above shows the required JavaScript code to modify the element concerned, so that we may display the data as we wish, using the template from YouTube.

As readers may notice, the data entries `Learn English Online`, `expired 30 Apr 2021`, `20% discount` need to be retrieved from somewhere, as the browser front end is an isolated environment, so designed to ensure network security.

These data may be retried from the back end (e.g. PHP), or injected via Python Selenium Chrome driver.

The seemingly trivial questions in (1) have highlighted many fundamental flaws in the existing web ecosystems &mdash; Why would such simple problems require such complicated solutions?

As you can see, now the simplest problem of data entry involves not only JavaScript, but PHP and Python as well!! The resulting code will be too complicated to be managed by mortal programmers. Here is where Phoscript metaprogramming script comes to rescue!!


5. This seems like a good point to take a break, before we continue in Part II.
