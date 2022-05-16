from scapy.all import *
import pandas as pd
import numpy as np
import multiprocessing as mp


def cap_quinturple(p) :
    global srcip, dstip, proto, sport, dport
    data={}
    if p.haslayer('IP'):   #6:TCP  17:UDP  1:ICMP
        srcip = p['IP'].src
        dstip = p['IP'].dst
        proto = p['IP'].proto
        if hasattr(p['IP'],'sport') and hasattr(p['IP'], 'dport'):
            sport = p['IP'].sport
            dport = p['IP'].dport
        else:
            sport = 0
            dport = 0

        data["srcip"] = srcip
        data["dstip"] = dstip
        data["proto"] = proto
        data["sport"] = sport
        data["dport"] = dport
        data['data'] = str(p)   #将数据本身存入
    # 如果没有IP层
    else:
        data["srcip"] = 0
        data["dstip"] = 0
        data["proto"] = 0
        data["sport"] = 0
        data["dport"] = 0
        data['data'] = str(p)  # 将数据本身存入

    return data

def df2csv(df,fname,mats=[],sep=','):   # 只追加前5列的数据，最后的data部分单独追加

    if len(df.columns) <= 0:
        return
    Nd = len(df.columns)
    Nd_1 = Nd - 1
    formats = mats[:]
    Nf = len(formats)
    # 确保对每个列都有对应的格式
    if Nf < Nd:
        for ii in range(Nf,Nd):
            coltype = df[df.columns[ii]].dtype
            ff = '%s'
            if coltype == np.int64:
                ff = '%d'
            elif coltype == np.float64:
                ff = '%f'
            formats.append(ff)
    fh=open(fname,'w')
    fh.write(','.join(df.columns) + '\n')
    for row in df.itertuples(index=False):
        ss = ''
        for ii in range(Nd):
            if ii==Nd_1:
                # 因为原本的data数据里面有非常多的逗号（,）会影响切割csv的判断，所以我们在data前面添加双引号，
                # 同时data内部的"可能影响整体的判定，所以将单个双引号替换为2个双引号，只保留其作为单纯双引号的意义
                ss += "\""+row[ii].replace("\"","\"\"")+"\""
                continue
            ss += formats[ii] % row[ii]
            # ss += str(row[ii])
            if ii < Nd_1:
                ss += sep
        fh.write(ss+'\n')
    fh.close()


class pcap_cut():
    def __init__(self,):
        super(pcap_cut, self).__init__()
        # self.filename = filename
        # self.pool = pool
        # insert_part[0].hide()
        # insert_part[1].setText('程序正在执行，请稍等')
        # insert_part[2].show()
    def cap_quinturple(self,p):
        global srcip, dstip, proto, sport, dport
        data = {}
        if p.haslayer('IP'):  # 6:TCP  17:UDP  1:ICMP
            srcip = p['IP'].src
            dstip = p['IP'].dst
            proto = p['IP'].proto
            if hasattr(p['IP'], 'sport') and hasattr(p['IP'], 'dport'):
                sport = p['IP'].sport
                dport = p['IP'].dport
            else:
                sport = 0
                dport = 0

            data["srcip"] = srcip
            data["dstip"] = dstip
            data["proto"] = proto
            data["sport"] = sport
            data["dport"] = dport
            data['data'] = str(p)  # 将数据本身存入
        # 如果没有IP层
        else:
            data["srcip"] = 0
            data["dstip"] = 0
            data["proto"] = 0
            data["sport"] = 0
            data["dport"] = 0
            data['data'] = str(p)  # 将数据本身存入

        return data



    def judge(self, quinturple, sum):  # 判断数据包的五元组是否符合异常流量的五元组

        sum[0].append(quinturple['srcip'])
        sum[1].append(quinturple['dstip'])
        sum[2].append(quinturple['sport'])
        sum[3].append(quinturple['dport'])
        sum[4].append(quinturple['proto'])
        sum[5].append(quinturple['data'])

        return True

    def spilt_pcap(self, spr, sum):  # 根据五元组切割pcap
        '''

        :param spr: 传入的检测流量
        :param sum: 异常流量集合
        :return: sum
        '''
        length = len(spr)

        for i in range(0, length):
            quinturple = cap_quinturple(spr[i])
            self.judge(quinturple, sum)  # 步长为1，逐个提取当前流量
            print(i)
        return sum

    def read_pcap2(self,savename,pool,num=20):  # 一次性全部读入
        # df = pd.read_excel('./csv_labels/TestbedSatJun12Flows.xlsx', sheet_name='attack2',
        #                    usecols=[4, 5, 6, 7, 8])  # 读取xlsx文件的attack页
        # df = pd.read_csv(self.csv_file)  # 读取xlsx文件的attack页
        filterstr = "tcp || udp"
        pr = sniff(filter=filterstr, count=num)
        print('截取流量成功')
        # pr = rdpcap(self.filename)
        # print('读取pcap文件成功 \n')
        L = len(pr)
        sip = []  # 创建数组储存所有的源ip
        dst = []  # 创建数组储存所有目的ip
        sp = []  # 创建数组储存所有源端口
        dp = []
        pro = []
        store = []
        label = []
        sum1 = [[], [], [], [], [], [], []]

        sum2 = [sip, dst, sp, dp, pro, store, label]
        sum3 = [sip, dst, sp, dp, pro, store, label]

        count = 0
        param_dict = {'task1': pr[0:int(L / 10)],
                      'task2': pr[int(L / 10):int(2 * L / 10)],
                      'task3': pr[int(2 * L / 10):int(3 * L / 10)],
                      'task4': pr[int(3 * L / 10):int(4 * L / 10)],
                      'task5': pr[int(4 * L / 10):int(5 * L / 10)],
                      'task6': pr[int(5 * L / 10):int(6 * L / 10)],
                      'task7': pr[int(6 * L / 10):int(7 * L / 10)],
                      'task8': pr[int(7 * L / 10):int(8 * L / 10)],
                      'task9': pr[int(8 * L / 10):int(9 * L / 10)],
                      'task10': pr[int(9 * L / 10):L]}
        # 使用多进程处理数据集
        results = [pool.apply_async(self.spilt_pcap, args=( param, sum1.copy())) for name, param in param_dict.items()]
        sum2 = [p.get() for p in results]
        # print(sum2)
        # 将sum2里面所有数组合并到sum3内
        [sum3[j].extend(sum2[idx][j]) for idx, value in enumerate(sum2) for j in range(len(value))]
        df1 = pd.DataFrame({'srcip': sum3[0], 'dstip': sum3[1], 'sport': sum3[2], 'dport': sum3[3], 'proto': sum3[4],
                            'data': sum3[5], }, )  # 创建dataFrame储存,每一列储存对应的数值
        # df1.to_excel('Tuesday.xlsx', index=False)
        # df1.to_csv(savename, index=False)
        df1.to_pickle(savename)
        # df2csv(df1, 'junk4.csv',myformats=['%s', '%s', '%d', '%d','%d',"%s"])  # 7.5 sec
        df2csv(df1, 'save.csv',)  #
        return df1  # 将函数返回




if __name__ == '__main__':

    # file = './spilt/2017/Tuesday/' + os.listdir(r'./spilt/2017/Tuesday')[5]
    file = './new.pcap'
    # csv_file = r'./csv_labels/2017/extract/Friday.csv'
    print(file)
    # 在类中把进程池pool设为成员变量，即self.pool，同时把self作为参数传给线程池中的函数的时候会报错，所以尽量在外部定义pool
    num_cores = int(mp.cpu_count())
    print("本地计算机有: " + str(num_cores) + " 核心")
    pool = mp.Pool(num_cores)

    start = time.time()
    a = pcap_cut(file)
    a.read_pcap2('benign.csv',pool)
    # read_pcap2(file)
    end = time.time()
    print("运行时间：%.2f" % (end - start))

    # a=pd.read_pickle('benign.pkl')
    # a=pd.read_csv('junk3.csv')














