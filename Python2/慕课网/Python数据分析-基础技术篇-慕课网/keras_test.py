# -*- coding: UTF-8 -*-
import numpy as up
from keras.model import Sequential
from keras.layers import Dense,Activation
from keras.optimizers import SGD

def main():
    from sklearn.datasets import load_iris
    iris=load_iris()
    print (iris["target"])
    from sklearn.preprocessing import LabelBinarizer
    print(LabelBinarizer().fit_transform(iris["target"]))
    #没敲完
if __name__=="__main__":
    main()

















