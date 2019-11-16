# 情绪识别api

用Django搭建的Web接口，输入一句话，通过训练好的模型来预测识别这句话的情绪。

## 示例
输入
```
http://jie12366.xyz:86/test/?sentence=卧槽
```
输出
```
{"code": 200, "msg": "厌恶"}
```
## 模型训练
基于LSTM的中文情绪识别 
https://github.com/jie12366/sentiment_analysis

## 相关博客
[中文情绪识别api](http://jie12366.xyz:8081/#/users/11/articles/46)
[基于LSTM的中文多分类情感分析](http://jie12366.xyz:8081/#/users/11/articles/35)
