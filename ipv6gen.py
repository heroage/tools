#! /home/idctest1/anaconda3/bin/python
# coding: utf-8

from IPy import IP
import IPy
import math
import optparse

def main():
        parser = optparse.OptionParser('usage: python ipv6gen.py -a <起始IPv6地址> -p <IPv6地址前缀> -c <要分配的IPv6地址个数>')
        parser.add_option('-a', '--address', dest='address', type='string', help='起始IPv6地址')
        parser.add_option('-p', '--prefix', dest='prefix', type='int', help='IPv6地址前缀')
        parser.add_option('-c', '--count', dest='count', type='int', help='要分配的IPv6地址个数')
        (options, args) = parser.parse_args()
        address = options.address
        prefix = options.prefix
        count = options.count

        if not(address and count and prefix):
            print(parser.usage)
            exit(0)

        if not prefix in range(1, 129):
            print(parser.usage)
            exit(0)

        try:
            tmplist = [address, '/', str(prefix)]
            ip = IP(''.join(tmplist))
        except Exception as e:
            tmplist = ['IP地址: ', address, ' 与前缀 /', str(prefix), '不匹配！']
            print(''.join(tmplist))
            tobecontinue = input('是否继续分配？(Y/N)')
            if tobecontinue.upper()!='Y':
                exit(0)

        try:
            ip = IP(address)
        except Exception as e:
            print('#'*40)
            print(parser.usage)
            print(str(e))
            exit(0)

        num = 2**(128-prefix)
        ipint = ip.int()
        for i in range(count):
            print(''.join([IPy.intToIp(ipint + num*i, version=6), '/', str(prefix)]))


if __name__ == '__main__':
        main()