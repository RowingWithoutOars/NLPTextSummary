# coding:utf-8
import fasttext

classifier = fasttext.train_supervised("/Users/usts/Desktop/biluFile/rawData/fasttext/raw_train_ZASD.txt", label="__label__")

f = open("/Users/usts/Desktop/biluFile/rawData/fasttext/raw_test.txt", "r")
data = []
for line in f:
    data.append(line)
for line in data:
    print("加载文本为："+line)
    label = classifier.predict(line.replace('\r', '').replace('\n', '').replace('\t', ''))
    print(label)
    break