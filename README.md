# Logically
#### A Programming Language for logic circuits

---

### About
Logically is a scripting language that can derive the combinational logic circuit of any logic expression. Given a set of logic operations, the language is capable of analyzing the resulting function and with a series of computations, a logical circuit will be derived.

### Introduction
Boolean logic is a branch from algebra in which variables are evaluated with truth tables where said variables have a value of “1” or “0” and certain outcome based on the expression. The operations used for evaluating the logic are OR, AND & NOT. These operations are represented by disjunction(), conjunction(∩), and negation(-), respectively. With these expressions, it is possible to express and evaluate Boolean Algebra. The following logic can then be used to construct circuits called combinational logic circuits (often referred as logical gates or logic circuits). 

These combinational logic circuits can range from very simple ones to very complicated ones. And so, developers use different techniques to specify the function of these combinational logic circuits like Boolean Algebra, Truth Tables and Logic Diagrams. Common combinational circuits made up that carry out a desired application include: Multiplexers, Encoders, Decoders, Half Adders, Full Adders, etc.


### Language Features
* Design logical circuits by implementing individual logic gates.
* Create complex logical expressions from logic circuits.
* Test circuits by generating truth tables.
* Simplify any logical expression with a single command.
* Generate visual circuit diagrams from generated circuits.
* Display the Venn Diagram of a given logical expression.


### Example Program
```
 >>out = XOR a b
 Added Expression to:  out
 >>b = AND c d
 Added Expression to:  out
 >>TABLE out
 The truth table is: 
 a	c	d	a ^ ( c and d )
 0	0	0	0
 0	0	1	0
 0	1	0	0
 0	1	1	1
 1	0	0	1
 1	0	1	1
 1	1	0	1
 1	1	1	0
```

### Installation
##### Dependencies
* Python 3.4 with the following packages:
  * SchemDraw
  * Matplotlib
  * TKinter
  * PLY
 ##### Instructions
 * Download the prrogram to your machine. You can download the code from <a href="https://github.com/javierramirezzayas/logically/zipball/master"> here </a>
 * After downloading the code open a terminal and run logically.py
 * Enjoy logically
  
