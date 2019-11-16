import pickle
import re
import jieba
import numpy as np
from keras.engine.saving import load_model
from keras.preprocessing import sequence
import tensorflow as tf
import os
from django.conf import settings

MAX_SENTENCE_LENGTH = 80
# 加载模型，并使模型和变量在同一图内
global graph
model = load_model(os.path.join(settings.BASE_DIR, 'my_model.h5'))
graph = tf.get_default_graph()
# 加载分词字典
with open(os.path.join(settings.BASE_DIR, 'word_dict.pickle'), 'rb') as handle:
    word2index = pickle.load(handle)

# 数据过滤
def regex_filter(s_line):
    # 剔除英文、数字，以及空格
    special_regex = re.compile(r"[a-zA-Z0-9\s]+")
    # 剔除英文标点符号和特殊符号
    en_regex = re.compile(r"[.…{|}#$%&\'()*+,!-_./:~^;<=>?@★●，。]+")
    # 剔除中文标点符号
    zn_regex = re.compile(r"[《》、，“”；～？！：（）【】]+")

    s_line = special_regex.sub(r"", s_line)
    s_line = en_regex.sub(r"", s_line)
    s_line = zn_regex.sub(r"", s_line)
    return s_line

def predict(sentence):
    print(sentence)
    xx = np.empty(1, dtype=list)
    # 数据预处理
    sentence = regex_filter(sentence)
    words = jieba.cut(sentence)
    seq = []
    for word in words:
        if word in word2index:
            seq.append(word2index[word])
        else:
            seq.append(word2index['UNK'])
    xx[0] = seq
    xx = sequence.pad_sequences(xx, maxlen=MAX_SENTENCE_LENGTH)

    label2word = {1: '喜好', 2: '悲伤', 3: '厌恶', 4: '愤怒', 5: '高兴', 0: '无情绪'}
    with graph.as_default():
        for x in model.predict(xx):
            x = x.tolist()
            label = x.index(max(x[0], x[1], x[2], x[3], x[4], x[5]))
            return label2word[label]