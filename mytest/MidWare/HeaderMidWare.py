# encoding: utf-8
import base64

proxyServer = '相应的代理服务器'##"http://proxy.abuyun.com:9010"

# 代理隧道验证信息
proxyUser = '用户名'
proxyPass = '密码'

proxyAuth = "Basic " + base64.b64encode(proxyUser + ":" + proxyPass)


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta["proxy"] = proxyServer

        request.headers["Proxy-Authorization"] = proxyAuth