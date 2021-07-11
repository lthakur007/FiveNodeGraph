import tensorflow as tf
from tensorflow.keras.models import Sequential
import tensorflow.keras.layers
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense

#import tensorflow as tf


def NNOp(input, x, constant = 123):
    if (x == 1):
        print("Executing Conv2D")
        input = tf.keras.layers.Conv2D(1,(3,3))(input)
        return input
    if (x == 2):
        print("Executing MaxPooking2D")
        input = tf.keras.layers.MaxPooling2D(pool_size=(2,2))(input)
        return input
    if (x == 3):
        print("Executing relu")
        input = tf.keras.layers.Activation('relu')(input)
        return input
    if (x == 4):
        print("Executing add operation")
        input = input + constant
        return input
    if (x == 5):
        print("Executing multiply operation")
        input = input * constant
        return input

import itertools
OpLst = [1, 2, 3, 4, 5]
AllCombtns = list(itertools.permutations(OpLst))

import subprocess
import os
import time
import psutil
import signal
import sys
input = tf.keras.layers.Input(shape=(64,64,3))
for lst in AllCombtns:
    print("Combination being tested: {}".format(lst))
    pid = os.fork()
    if pid > 0:
        print("pid: {}".format(pid))
        #os.wait()
        time.sleep(3)
        count = 0
        while psutil.pid_exists(pid):
            #print("pid still exists")
            time.sleep(5)
            count += 1
            if (count >= 2):
                break
        os.kill(pid, signal.SIGTERM)
    else:
        time.sleep(3)
        for x in lst:
            input = NNOp(input, x)
        print("Combination executed successfully")
        time.sleep(3)
        sys.exit()

