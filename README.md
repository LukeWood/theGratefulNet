# SeussWithAttitude
This is a recurrent neural network program that is trained on a combination of Doctor Seuss and the rap group NWA.  The output should be quite comical.

# Notation
Inside of my neural network implementation you will find symbols that follow this notation.  If you are following along this is their meaning.  This is standard notation</br>
x<sub>t</sub> corresponds to input at step t.</br>
s<sub>t</sub> is the state at step t (hidden).</br>
s<sub>t</sub> = f(Ux<sub>t</sub> + Ws<sub>t-1</sub>)</br>, we define out function f as a nonlinearity.  I will be using tanh for this.  U and W are parameters.
o<sub>t</sub> is the output at step t.

# Initial Thoughts and Predictions
My first guess is that the network will naturally tend to separate these two authors as their language diction is incredibly different.  If we input a word more related to Doctor Seuss than NWA I hypothesize that the network will drive itself towards an output of almost entire in Doctor Seuss' diction.
