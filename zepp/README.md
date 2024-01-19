# 🌈 Zepp | Zepp Life

### **通过 [Zepp](https://app.mi.com/details?id=com.huami.watch.hmwatchmanager)/[Zepp Life](https://app.mi.com/details?id=com.xiaomi.hm.health) 绑定微信、支付宝实现同步步数**

<br>

> **改自：[motion-for-email](https://github.com/matocool/motion-for-email)**

+ **部署帐号、密码、步数范围 [`email.py`](https://github.com/geoi6sam1/GitHub-Actions-Public/blob/zepp/zepp.py) 如下：**

```python
# 帐号（手机号或者邮箱）
user = "email@zepp.step"
# 密码（尽量设置简单点）
password = "password"
# 步数范围（尽可能随机）
step = str(randint(17760,29999))
```

<br>

> **部署文件 [`zepp.yml`](https://github.com/geoi6sam1/GitHub-Actions-Public/blob/zepp/zepp.yml) 请自行放在目录 `.github/workflows` 下**
