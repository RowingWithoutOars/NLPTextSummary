from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
import json
import fasttext
from django.views.decorators.http import require_http_methods


# classifier_ZASD = fasttext.train_supervised("/Users/usts/Desktop/biluFile/rawData/fasttext/raw_train_ZASD.txt", label="__label__")
# classifier_YJWP = fasttext.train_supervised("/Users/usts/Desktop/biluFile/rawData/fasttext/raw_train_YJWP.txt", label="__label__")
# classifier_YJAY = fasttext.train_supervised("/Users/usts/Desktop/biluFile/rawData/fasttext/raw_train_YJAY.txt", label="__label__")
# classifier_YJAFQY = fasttext.train_supervised("/Users/usts/Desktop/biluFile/rawData/fasttext/raw_train_YJAFQY.txt", label="__label__")
# classifier_EJWP = fasttext.train_supervised("/Users/usts/Desktop/biluFile/rawData/fasttext/raw_train_EJWP.txt", label="__label__")
# classifier_EJAY = fasttext.train_supervised("/Users/usts/Desktop/biluFile/rawData/fasttext/raw_train_EJAY.txt", label="__label__")
# classifier_EJAFQY = fasttext.train_supervised("/Users/usts/Desktop/biluFile/rawData/fasttext/raw_train_EJAFQY.txt", label="__label__")


def index(request):
    return HttpResponse("Hello World")

def testPost(request):

    # global classifier_ZASD
    # global classifier_YJWP
    # global classifier_YJAY
    # global classifier_YJAFQY
    # global classifier_EJWP
    # global classifier_EJAY
    # global classifier_EJAFQY
    dic = {}
    print(request.body)
    # json_request = json.loads(request.body)
    # ql = json_request.get('qLabel')
    # switch = {
    #     0: lambda content: classifier_ZASD.predict(str(content).replace('\r', '').replace('\n', '').replace('\t', '')),
    #     1: lambda content: classifier_YJWP.predict(str(content).replace('\r', '').replace('\n', '').replace('\t', '')),
    #     2: lambda content: classifier_YJAY.predict(str(content).replace('\r', '').replace('\n', '').replace('\t', '')),
    #     3: lambda content: classifier_YJAFQY.predict(str(content).replace('\r', '').replace('\n', '').replace('\t', '')),
    #     4: lambda content: classifier_EJWP.predict(str(content).replace('\r', '').replace('\n', '').replace('\t', '')),
    #     5: lambda content: classifier_EJAY.predict(str(content).replace('\r', '').replace('\n', '').replace('\t', '')),
    #     6: lambda content: classifier_EJAFQY.predict(str(content).replace('\r', '').replace('\n', '').replace('\t', ''))
    # }
    # try:
    #     content = json_request.get('content')
    #     label = switch[ql](content)
    #     dic["label"] = label[0]
    #     dic["p"] = [str(i) for i in label[1]]
    # except KeyError as e:
    #     pass
    print(dic)
    return JsonResponse(dic)


