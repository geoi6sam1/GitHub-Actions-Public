# 🚀GitHub-Actions-Public

<p align="middle"></p>

### 1. **关于 [某加速器](https://ant.aff003.me) 自动刷邀请领无限流量**
* **原创作者：[二毛](https://erma0.cn)**
* **原创文章：[记一次某加速器APP算法解密实现刷邀请](https://segmentfault.com/a/1190000040012580)**
* **部署邀请码 [`index.py`](https://github.com/s757129/GitHub-Actions-Public/blob/main/ant/index.py) 如下：**

```python
#【某加速器】翻墙/搭梯子
ant = Ant('a***A') #邀请码
```

### 2. **关于 [小米运动](https://app.mi.com/details?id=com.xiaomi.hm.health) 每天自动提交步数**
* **钉钉自定义机器人 [`chatbot.py`](https://github.com/zhuifengshen/DingtalkChatbot/blob/master/dingtalkchatbot/chatbot.py) 👉 [配置文档](https://github.com/zhuifengshen/DingtalkChatbot) 👈**
* **部署账号密码步数 [`index.py`](https://github.com/s757129/GitHub-Actions-Public/blob/main/huami-step/index.py) 如下：**

```python
#【小米运动】微信/支付宝
user = "1*********6" #手机号
password = "1******8" #密码
step = str(randint(17760,19999)) #随机步数
```

**【注】不会使用钉钉机器人或不需要被通知等，可自行注释如下内容：**

```python
sendDingDing(result) #大概在第103行
```

### 3. **关于 [GitHub Actions](https://docs.github.com/cn/actions) 部署教程**
