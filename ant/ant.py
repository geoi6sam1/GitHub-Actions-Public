# -*- encoding: utf-8 -*-

import requests,time,json
from base64 import b64decode
from hashlib import sha256, md5
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
# from Crypto.Hash import SHA256, MD5  # 和hashlib库一样


class Ant(object):
    """
    蚂蚁加速器刷邀请
    """
    def __init__(self, aff):
        self.aff = aff
        self.oauth_id = ''
        self.timestamp = ''
        self.url = 'http://ant.hyysapi.com/api.php'
        self.headers = {  # 加不加header都可以
            # 'User-Agent':
            # 'Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; E6533 Build/N2G48H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
        }
        # 明文key，再经EVP_BytesToKey方法生成最终key，最终HEX为：B496F831128E4FE1DE33F4B7A2C46E0DD4772524A4826FE4486FCC07E3E2B87F
        self.key = 'fjeldkb4438b1eb36b7e244b37dhg03j'  # 没发现哪个加密库中有EVP_BytesToKey算法
        self.hexkey = 'B496F831128E4FE1DE33F4B7A2C46E0DD4772524A4826FE4486FCC07E3E2B87F'
        self.b64key = 'tJb4MRKOT+HeM/S3osRuDdR3JSSkgm/kSG/MB+PiuH8='

    @staticmethod
    def get_timestamp(long=10):
        """
        取时间戳，默认10位
        """
        return str(time.time_ns())[:long]

    def decrypt(self, data: str):
        """
        aes解密
        """
        ct_iv = bytes.fromhex(data[:32])
        ct_bytes = bytes.fromhex(data[32:])
        ciper = AES.new(
            b64decode(self.b64key), AES.MODE_CFB, iv=ct_iv,
            segment_size=128)  # CFB模式，iv指定，块大小为128(默认为8，需填8的倍数，貌似AES标准区块大小就是128，和密钥大小128/192/256无关)
        plaintext = ciper.decrypt(ct_bytes)
        return plaintext.decode()

    def encrypt(self, data: str):
        """
        aes加密
        """
        # cipher = AES.new(bytes.fromhex(self.hexkey), AES.MODE_CFB)
        cipher = AES.new(b64decode(self.b64key), AES.MODE_CFB, segment_size=128)  # CFB模式，iv自动随机，块大小为128
        ct_bytes = cipher.iv + cipher.encrypt(data.encode())  # iv+加密结果合并
        return ct_bytes.hex().upper()  # hex编码

    def get_sign(self):
        """
        生成sign
        """
        template = 'appId=android&appVersion=2.1.8&data={}&timestamp={}2d5f22520633cfd5c44bacc1634a93f2'.format(
            self.encrypt_data, self.timestamp)
        # sha256
        sha = sha256()
        sha.update(template.encode())
        res = sha.hexdigest()
        # nd5
        m = md5()
        m.update(res.encode())
        res = m.hexdigest()
        return res

    def request(self, d):
        """
        请求封包
        """
        plaintext = {"version": "2.4.3", "app_type": "ss_proxy", "language": 0, "bundleId": "com.dd.antss"}
        d.update(plaintext)
        self.timestamp = self.get_timestamp(10)
        self.encrypt_data = self.encrypt(json.dumps(d, separators=(',', ':')))
        sign = self.get_sign()
        data = {
            "appId": "android",
            "appVersion": "2.1.8",
            "timestamp": self.timestamp,
            "data": self.encrypt_data,
            "sign": sign
        }
        res = requests.post(url=self.url, data=data, headers=self.headers)
        resj = res.json()
        res = self.decrypt(resj.get('data'))
        print(res)
        return res

    def get_user(self):
        """
        生成新用户
        """
        # 取随机md5
        m = md5()
        m.update(get_random_bytes(16))
        oauth_id = m.hexdigest()

        data = {"oauth_id": oauth_id, "oauth_type": "android", "mod": "user", "code": "up_sign"}
        self.request(data)
        self.oauth_id = oauth_id
        print(oauth_id)

    def invite(self):
        """
        刷邀请，邀请码：self.aff
        """
        self.get_user()
        data = {
            "oauth_id": self.oauth_id,
            "oauth_type": "android",
            "aff": self.aff,
            "mod": "user",
            "code": "exchangeAFF"
        }
        self.request(data)


if __name__ == "__main__":

    # 邀请码
    ant = Ant('bpVpM')
    ant.invite()

    ant = Ant('bAPqR')
    ant.invite()

    ant = Ant('bBYsh')
    ant.invite()
