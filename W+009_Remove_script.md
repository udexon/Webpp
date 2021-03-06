# W+009: Removing `<script>` from HTML pages

1. One of the biggest obstacles in "cloning" web pages from "other" websites is the complex embedded `<script>` code.

Of course, we do not advocate violating copyright laws, as subsequent modifications to the layout, fonts and other properties have not had legal precedents which demonstrate the relevance and applicabilities of such violations.

2. They can be easily removed using the following Python BeautifulSoup code:

- https://github.com/udexon/Webpp/blob/main/src/h_extract_script_1.py

3. Figure 1 and figure 2 show the YouTube page before (online) and after (local copy) the `<script>` is removed:

- Figure 1
<img src="https://github.com/udexon/Webpp/blob/main/img/yt_local.png" width=600>

- Figure 2
<img src="https://github.com/udexon/Webpp/blob/main/img/yt_html.png" width=600>
