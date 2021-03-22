In [DU004 (Modify HTML DOM with Python Selenium)](https://github.com/udexon/DUNIIX/blob/main/DU004_Modify_HTML.md), we demonstrate how to "Modify HTML DOM with Python Selenium", with the  Python Selenium function `execute_script()` which in turn takes a string input of JavaScript statement:

```py
driver.execute_script("document.getElementsByTagName('li')[21].innerText='mifasolasido'")
```

In this tutorial, we shall explain how it can be simplified to the following Python script:

```py
f('some_name 21 li dom:')
```

This is perhaps the most practical and simple explanation of "metaprogramming", a niche topic in computer programming shrouded in secrecy for decades, due to lack of effort and motivation to popularize it.

```py

driver.execute_script("document.getElementsByTagName('li')[21].innerText='mifasolasido'")

f('some_name 21 li dom:')




f('li j_geid: 21 j_i: j_it: j_eq: doremon j_sq: jstr: es:')

def f_dom():
   f( S.pop()+' j_geid: '+ str(S.pop()) +' j_i: j_it: j_eq: '+ S.pop() +' j_sq: jstr: es:')
   
def f_dom1():
    driver.execute_script("document.getElementsByTagName('"+ S.pop() +"')["+ str(S.pop()) +"].innerText='"+ S.pop() +"'")
```
