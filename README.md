<img src="D_Skeletons_color.jpg" alt="mascot" width=100%/>
# The Grateful Net

<img src="mascot1.jpg" alt="mascot" height=50/>This is a recurrent neural network program that is trained on the music of the band Grateful Dead.<img src="mascot1.jpg" alt="mascot" height=50/>

## Concept

Recurrent Neural Networks are a class of machine learning models.  They are similar to a classic neural network, however they "remember" their previous states.  This is very useful when dealing with sequences, including but not limited to natural language.  We will be training out network model on music lyrics, and hopefully we will get some interesting music lyrics out.

# Notation
Inside of my neural network implementation you will find symbols that follow this notation.  If you are following along this is their meaning.  This is standard notation</br>
x<sub>t</sub> corresponds to input at step t.</br>
s<sub>t</sub> is the state at step t (hidden).</br>
s<sub>t</sub> = f(Ux<sub>t</sub> + Ws<sub>t-1</sub>)</br>, we define out function f as a nonlinearity.  I will be using tanh for this.  U and W are parameters.
o<sub>t</sub> is the output at step t.

# Initial Thoughts and Predictions
My first guess is that the network will naturally tend to separate these two authors as their language diction is incredibly different.  If we input a word more related to Doctor Seuss than NWA I hypothesize that the network will drive itself towards an output of almost entire in Doctor Seuss' diction.

# Literature
To start this project, I have gone through some literature that I found essential to the understanding and creation of a Recurrent Neural Network.</br>
__Numpy__</br>
 [Basic Tutorial](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html)</br>
 [Full Documentation](https://docs.scipy.org/doc/numpy-1.11.0/reference/)</br>

__Equations__</br>
 tanh(x) = (e<sup>x</sup> - e<sup>-x</sup>) / (e<sup>x</sup> + e<sup>-x</sup>)</br>
</br>

__Algorithms__</br>
 [Gradient Descent](https://en.wikipedia.org/wiki/Gradient_descent)</br>
 [Backwards Error Propogation (backpropogation for short)](https://en.wikipedia.org/wiki/Backpropagation)</br>
</br>

__Neural Networks__</br>
 [Forward Feed Network](https://en.wikipedia.org/wiki/Feedforward_neural_network)</br>
 [Recurrent Neural Network](https://en.wikipedia.org/wiki/Recurrent_neural_network)</br>
