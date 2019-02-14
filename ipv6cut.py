#! /usr/bin/python

from IPy import IP
import IPy
import math
import optparse

def isPowerOfTwo(num):
        if (num & (num-1))==0:
                return True
        else:
                return False


def main():
        parser = optparse.OptionParser('usage: python ipv6cut.py -a <ipv6 address segment> -c <count>')
        parser.add_option('-a', dest='address', type='string', help='要分配的IPv6地址段')
        parser.add_option('-c', dest='count', type='int', help='要分配的段数')
        (options, args) = parser.parse_args()
        address = options.address
        count = options.count

        if not(address and count):
                print(parser.usage)
                exit(0)

        if not isPowerOfTwo(count):
                print('错误：分配的段数必须是2的幂！')
                exit(0)

        try:
                ipSegment = IP(address)
        except Exception as e:
                print(parser.usage)
                print(str(e))
                exit(0)

        ipList = []
        prefixlen = ipSegment.prefixlen()
        newPrefixLen = int(math.log2(count))
        ipBase = int(ipSegment.strDec())
        ipList.append(ipBase)
        ipSegmentLength = ipSegment.len()
        stepLength = int(ipSegmentLength/count)

        for i in range(1, count):
                nextIP = int(ipList[-1]) + stepLength
                ipList.append(nextIP)

        for item in ipList:
                print(str(IPy.intToIp(item, version=6))+ '/' + str(prefixlen+newPrefixLen))


if __name__ == '__main__':
        main()