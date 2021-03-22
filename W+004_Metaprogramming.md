In [DU004 (Modify HTML DOM with Python Selenium)](https://github.com/udexon/DUNIIX/blob/main/DU004_Modify_HTML.md), we demonstrate how to "Modify HTML DOM with Python Selenium", with the  Python Selenium function `execute_script()` which in turn takes a string input of JavaScript statement:

```py
driver.execute_script("document.getElementsByTagName('li')[21].innerText='mifasolasido'")
```

In this tutorial, we shall explain how it can be simplified to the following Python script:

```py
f('some_name 21 li dom:')
```

This is perhaps the most practical and simple explanation of "metaprogramming", a niche topic in computer programming shrouded in secrecy for decades, due to lack of effort and motivation to popularize it.


1. We shall first look at `f_dom1()` as shown below:

```py
def f_dom1():
    driver.execute_script("document.getElementsByTagName('"+ S.pop() +"')["+ str(S.pop()) +"].innerText='"+ S.pop() +"'")
```

It simply breaks the JavaScript command string into several parts, and inserts the required parameters, which are in turn read from a stack `S`.

The stack machine is perhaps THE universal data structure and architecture for metaprogramming that can be implemented across all known programming languages.

The programming language we employ, Phoscript, is derived from the Forth programming language, which in turn is based on a stack machine architecture.

To execute `f_dom1()`, the following script is entered in the Python interpreter:

```py
>>> f('jeff_w 21 li dom1:')
```

The parameters `jeff_w 21 li` are pushed on to the stack, and popped last in first out as the parameters in `f_dom1()`.

`f()` is the Python function that acts as the entry point into Phoscript. Any word that ends with a colon `:` character is mapped to a Python Phoscript function with prefix `f_*()`, i.e. `dom1:` is mapped to `f_dom1()`.


2. From item (1) above, we have demonstrated several issues with `f_dom1()`:
- `f_dom1()` is simple but not flexible enough.
- What if we want to access the DOM object with a different number of parameters?

To solve the various problems in (1), we added the following functions:

```py
def f_es():
    driver.execute_script( S.pop() )
    
def f_j_geid():
    S.append( "document.getElementsByTagName('"+ S.pop() +"')" )    
    
def f_j_i():
    i = str(S.pop())
    print(i, type(i))
    S.append( S.pop()+"["+i+"]" )
    
def f_j_it():
    S.append( S.pop()+".innerText")
    
def f_j_eq():
    S.append( S.pop()+"=" )
    
def f_j_sq(): # single quote
    S.append( "'"+S.pop()+"'")
    
def f_jstr(): # join two strings
    sa=S.pop()
    S.append( S.pop() + sa )
    
def f_dom():
   f( S.pop()+' j_geid: '+ str(S.pop()) +' j_i: j_it: j_eq: '+ S.pop() +' j_sq: jstr: es:')
  
```

These functions can be invoked using the following scripts:

1. Calling `f_dom()` or `dom:`

```py
>>> f('jeff_w 21 li dom:')
```

2. `f_dom()` itself is equivalent to:

```py
f('li j_geid: 21 j_i: j_it: j_eq: doremon j_sq: jstr: es:')
```

# Conclusions

1. We may loosely define "metaprogramming" as "using code in one programming language to manipulate the code in another programming language", although a rigourous definition will required deeper understanding of various issues involved, which takes time and experience to acquire.

2. We have demonstrated the use of Phoscript to manipulate code in Python and JavaScript. The requirement to understand all 3 programming languages may be an obstacles to many initially. However, as we shall demonstrate in subsequent tutorials, Phoscript can be used to create a "sandwiched metaprogramming training model" where learners of different expertise may choose to learn the modules at different levels, and proceed to start using Phoscript quickly without understanding the fundamentals, and learn the fundamentals while writing practical code. Phoscript sandwiched metaprogramming model is unique and is applicable to all known programming languages and programming frameworks.



<!--

Similarly `f_dom()` can be invoked via the following script:

```py

driver.execute_script("document.getElementsByTagName('li')[21].innerText='mifasolasido'")

f('some_name 21 li dom:')




f('li j_geid: 21 j_i: j_it: j_eq: doremon j_sq: jstr: es:')

def f_dom():
   f( S.pop()+' j_geid: '+ str(S.pop()) +' j_i: j_it: j_eq: '+ S.pop() +' j_sq: jstr: es:')
   
def f_dom1():
    driver.execute_script("document.getElementsByTagName('"+ S.pop() +"')["+ str(S.pop()) +"].innerText='"+ S.pop() +"'")
```

-->
