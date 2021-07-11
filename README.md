# FiveNodeGraph
Ask: Fixed configuration of 5 node graph(in other words 5 operations) which are 1) convolution 2) MaxPool 3) Add 4) Multiply and 5) Relu
Five Ops --> 120 Combinations possible.
I have run the code in Google colab. Output is available with the file name: **OutputFrmColab.txt**

Could not run on gpu:
I tried on AMD's MI60 gpu but the code which ran successfully on colab was resulting in memory exhaustion on gpu and eventually resulting in softhang.
