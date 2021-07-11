# FiveNodeGraph
Ask: Fixed configuration of 5 node graph(in other words 5 operations) which are 1) convolution 2) MaxPool 3) Add 4) Multiply and 5) Relu
Five Ops --> 120 Combinations possible.
Ran the code in Google colab. Output is available with the file name: **OutputFrmColab.txt**

Ran the code on Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz. output is available with the file name: **CpuOut.txt**


Could not run on gpu:
Tried running on AMD's MI60 gpu but the code which ran successfully on colab was resulting in memory exhaustion on gpu and eventually resulting in softhang.
