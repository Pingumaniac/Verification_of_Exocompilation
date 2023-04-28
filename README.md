# Verification_of_Exocompilation
CS 6315 Automated Verification Final Project

## Who am I?
#### Young-jae Moon
* M.Sc. in computer science and Engineering Graduate Fellowship recipient at Vanderbilt University (January 2023 - December 2024).
* Email: youngjae.moon@Vanderbilt.Edu

## Advisor
#### Professor Taylor Johnson
* Associate Professor of Computer Science at Vanderbilt University
* Website: http://www.taylortjohnson.com/

## What I have done?

* First, I have used Exocompiler to compile Exo functions embedded in Python into C (most of the functions from the GitHub repository of Exo language).
* Second, I have encoded the original Python and transformed C functions in Python.
* Third, I have encoded them again in SMT.
* Last, I have used an SMT solver to prove that the original and transformed programs are equivalent.

## What is Exo programming language?

Exo is an embedded DSL that helps low-level performance engineers transform very simple programs that specify what they want to compute into very complex programs that do the same thing as the specification, only much, much faster.

It is developed by Professor Gilbert Bernstein at University of Washington and other people. It is based on Python and compiles to C.

## Instructions to download Exo programming language

First, create a virtual environment for your project. Notice that Exo requires Python 3.9
```
python3 -m venv venv
. venv/bin/activate
```

Then, install exo-lang:
```
python -m pip install -U setuptools wheel
python -m pip install exo-lang
```

Please refer to Exo programming language website for more information: https://exo-lang.dev/

## How to compile Exo programs into C

For this project, you can download the python files in this GitHub repository and put them in the venv folder that you will have created if you have followed the instruction above.

Then, please run the following command:
```
exocc -o out --stem <name of output file> <name of python file>.py
```

If there is no error, you can view the compiled C and the header file in the 'out' folder.
```
ls out
```
Notice that the compiled C and header files are equivalent to the corresponding C and header files in this repository.

## Future project ideas for further improvements

#### 1. Represent Python and C functions directly in SMT instead of first representing them in Python and then SMT.

I have initially tried this using PySMT expressions such as ForAll, Implies, And, Equals, Plus, Times, etc. For instance, ForAll and Implies can be used to represent the for loop structure in Python instead. Nonetheless, this gave me endless errors for debugging. Hence I have stopped approaching in this way and changed the approach.

#### 2. Write more complex Exo functions for this project

I have noted that the Exo language lacks documentation, and hence when I have tried out implementing a simple ReLU function and an artificial neural network, they weren't able to be compiled. All Exo functions except conv2d (convolution for 2D) and gaussian blur in this file have been obtained from analyzing the GitHub repository of the Exo language and extracting specific functions mostly from their testing files, other remaining files, and from their web page.

#### 3. Optimizing transformation

PySMT can help in determining the optimal set of transformations and optimizations for the Exocompiler to generate optimised code for the target hardware accelerators.

#### 4. Code synthesis

PySMT can be used to synthesize code fragments that meet specific requirements: e.g., hardware compatibility or performance constraints. This can then be integrated into the generated low-level code.
