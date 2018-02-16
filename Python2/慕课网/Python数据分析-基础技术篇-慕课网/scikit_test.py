# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd

def main():
    #Pre-processing
    from sklearn.datasets import load_iris
    iris=load_iris()
    print (iris)
    print (len(iris["data"]))
    #翻译：该模块在0.18版本中被弃用，支持所有重构的类和函数都被移动到的model_selection模块。 另请注意，新的CV迭代器的接口与本模块的接口不同。 此模块将在0.20中删除。
    #解决办法：将“from sklearn.cross_validation import train_test_split” 改为“from sklearn.model_selection import train_test_split”
    from sklearn.model_selection import train_test_split
    train_data,test_data,train_target,test_target=train_test_split(iris.data,iris.target,test_size=0.2,random_state=1)

    #Model 建模
    from sklearn import tree
    clf=tree.DecisionTreeClassifier(criterion="entropy")
    clf.fit(train_data,train_target)    #进行练习
    y_pred=clf.predict(test_data) #进行预测

    #Verify 验证
    from sklearn import metrics
    print (metrics.accuracy_score(y_true=test_target,y_pred=y_pred))
    print (metrics.confusion_matrix(y_true=test_target,y_pred=y_pred))

    #输出决策树
    with open("./data/tree.dot","w") as fw:
        tree.export_graphviz(clf,out_file=fw)




if __name__=="__main__":
    main()
















