<img src="img/D_Skeletons_color.jpg" alt="mascot" width=100%/>
<h1 align="center">The Grateful Net</h1>

<p align="center"><img src="img/mascot1.jpg" alt="mascot" height=50/>A tribute to the Grateful Dead.<img src="img/mascot1.jpg" alt="mascot" height=50/></p>

# Concept

Recurrent Neural Networks are a class of machine learning models.  They are similar to a classic neural network, however they "remember" their previous states.  This is very useful when dealing with sequences, including but not limited to natural language.  We will be training out network model on music lyrics, and hopefully we will get some interesting music lyrics out.

# Notation
Inside of my neural network implementation you will find symbols that follow this notation.  If you are following along this is their meaning.  This is standard notation</br>
x<sub>t</sub> corresponds to input at step t.</br>
s<sub>t</sub> is the state at step t.  This is what allows our network to "remember" previous inputs.</br>
s<sub>t</sub> = f(Ux<sub>t</sub> + Ws<sub>t-1</sub>), we define out function f as a nonlinearity.  I will be using tanh for this (defined below).  U and W are parameters to our neural network (we will also cover this later)
o<sub>t</sub> is the output at step t.

# Initial Thoughts and Predictions
My first guess is that the network will naturally tend to separate these two authors as their language diction is incredibly different.  If we input a word more related to Doctor Seuss than NWA I hypothesize that the network will drive itself towards an output of almost entire in Doctor Seuss' diction.

# Literature
To start this project, I have gone through some literature that I found essential to the understanding and creation of a Recurrent Neural Network.</br>

## Basic Definitions
[**One-hot Vector**](https://en.wikipedia.org/wiki/One-hot) refers to a group of bits among which the legal combinations of values are only those with a single high</br>

## Numpy
 [Basic Tutorial](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html)
 > Numpy is an expansive mathematics library for python.  I will be making great use the linear algebra functionality.

 [Full Documentation](https://docs.scipy.org/doc/numpy-1.11.0/reference/)
 > Having a strong foundation in numpy is essential in modeling networks in python.

## Equations
 tanh(x) = (e<sup>x</sup> - e<sup>-x</sup>) / (e<sup>x</sup> + e<sup>-x</sup>)
 > tanh is our nonlinear function that we will use to determine our state at each step.

## Algorithms
 [Loss Function](https://en.wikipedia.org/wiki/Loss_function)
 > Also known as a cost function, this function maps a set of values to the "cost" of running them.  This allows us to optimize our neural network based on the values at each step.

 [Gradient Descent](https://en.wikipedia.org/wiki/Gradient_descent)
 > Gradient Descent is an algorithm used to solve a system of linear equations.  This is essential to our backpropogation algorithm.

 [Backwards Error Propogation (backpropogation for short)](https://en.wikipedia.org/wiki/Backpropagation)
 > Coming soon!

 [Backpropogation Through Time (this shows up as bppt in our implementation)](http://minds.jacobs-university.de/sites/default/files/uploads/papers/ESNTutorialRev.pdf)
 > Coming soon!

## Neural Networks
 [Forward Feed Network](https://en.wikipedia.org/wiki/Feedforward_neural_network)</br>
 [Recurrent Neural Network](https://en.wikipedia.org/wiki/Recurrent_neural_network)</br>

# Implementation Steps
1. Implement a vanilla Recurrent Neural Network
2. Allow storage of networks to prevent the need for re-loading
3. Create a web page allowing people to see sample outputs of the network.
4. Optimize Network (Possibly moving to a Long Term Short Memory model)

# Results
Coming soon!

# Live demo
[Samples of the results](https://lukewoodsmu.github.io/theGratefulNet)
