#!/usr/bin/python
#coding: utf-8
#python版本：3.6及以上
import sys
import json
import requests

#用于解决中文字符显示不正确问题
reload(sys)
sys.setdefaultencoding("utf-8")


#zabbix报警信息
#topartid=sys.argv[1]
msg=sys.argv[1]

#企业微信secret与corpid
secret="VpAlz2yxkRzxVXrDTxTmSRdODXEeAfJsoceuLRKGu8s"
corpid="wwda7611dac8dffae5"


class WorkWeChat(object):
    def __init__(self,corpid,secret):
        self.secret = secret
        self.corpid = corpid
        self.access_token = self.getAccessToken()

    def getAccessToken(self):
        #用于获取token
        result = requests.get(
            url="https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params={
              "corpid":self.corpid,
              "corpsecret":self.secret
            }
        ).json()
        assert result.get("access_token"),"获取token失败，%s"%result

        return result.get("access_token")

    def getDepartmentID(self):
        #用于获取企业微信群id
        result = requests.get(
            url="https://qyapi.weixin.qq.com/cgi-bin/department/list",
            params={
                "access_token":self.access_token
            }
        ).json()
        return result

    def sendMsg(self,msg):
        #向企业微信发送报警信息
        body={
           # "touser" : "ZhuNing",
           "toparty" : 2,
           "msgtype" : "text",
           "agentid" : 1000002,
           "text" : {
               "content" : msg,
           },
           "safe":0
        }

        result = requests.post(
            url=" https://qyapi.weixin.qq.com/cgi-bin/message/send",
            params={
                "access_token":self.access_token
            },
            data=bytes(json.dumps(body,ensure_ascii=False))
        )
        return result




if __name__ == '__main__':
    obj = WorkWeChat(corpid,secret)
    # access_token = obj.getAccessToken()
    # result = obj.getDepartmentID()
    obj.sendMsg(msg)
    # print(result.get("department"))





