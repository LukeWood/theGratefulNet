# SeussWithAttitude
This is a recurrent neural network program that is trained on a combination of Doctor Seuss and the rap group NWA.  The output should be quite comical.

# Notation
x<sub>t</sub> corresponds to input at step t.</br>
s<sub>t</sub> is the state at step t (hidden).</br>
s<sub>t</sub> = f(Ux<sub>t</sub> + Ws<sub>t-1</sub>)</br>, we define out function f as a nonlinearity.  I will be using tanh for this.  U and W are parameters.
o<sub>t</sub> is the output at step t.
