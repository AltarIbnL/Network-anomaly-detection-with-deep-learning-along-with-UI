from scapy.all import *
import pyshark

def pack_callback(packet):
    print ( packet.show() )
    if packet['Ether'].payload:
        # print(packet)
        print (packet['Ether'].src)
        print (packet['Ether'].dst)
        print (packet['Ether'].type)

    if packet['ARP'].payload:
        print(packet)
        print (packet['ARP'].psrc)
        print (packet['ARP'].pdst)
        print (packet['ARP'].hwsrc)
        print (packet['ARP'].hwdst)
    time.sleep(2)

filterstr="tcp || udp"
B = sniff(filter=filterstr,count=300)




# B= sniff(count=5)
# B[0]['ARP']

# a = rdpcap('./new.pcap')
# print(a[0])

# capture = pyshark.LiveCapture(bpf_filter='ip and tcp port')
# capture = pyshark.LiveCapture()
# capture.sniff(timeout=20)
# print(capture)

