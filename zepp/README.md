# 🌈 Zepp | Zepp Life

### **通过 [Zepp Life](https://app.mi.com/details?id=com.xiaomi.hm.health) 绑定微信、支付宝实现同步步数**

<br>

> **改自：[motion-for-email](https://github.com/matocool/motion-for-email) 【邮箱版】**

+ **部署帐号、密码、步数范围 [`email.py`](https://github.com/geoi6sam1/GitHub-Actions-Public/blob/zepp/email.py) 如下：**

```python
# 帐号（这里只能是邮箱）
user = "email@zepp.step"
# 密码（尽量设置简单点）
password = "password"
# 步数范围（尽可能随机）
step = str(randint(17760,19999))
```

<br>

> **钉钉自定义机器人 [`chatbot.py`](https://github.com/zhuifengshen/DingtalkChatbot/blob/master/dingtalkchatbot/chatbot.py) 👉 [配置文档](https://github.com/zhuifengshen/DingtalkChatbot) 👈**

+ **钉钉机器人通知可自行设置，没有则不发送，不要乱填**

```python
# Webhook地址
webhook = ''
# 加签密钥
secret = ''
```

<br>

> **部署文件 [`zepp.yml`](https://github.com/geoi6sam1/GitHub-Actions-Public/blob/zepp/zepp.yml) 请自行放在目录 `.github/workflows` 下**

+ **默认 `1 0 * * *` 即北京时间早上8点1分
  - 但GitHub较玄学，一般是在9点半左右，范围是早上8点至12点**
