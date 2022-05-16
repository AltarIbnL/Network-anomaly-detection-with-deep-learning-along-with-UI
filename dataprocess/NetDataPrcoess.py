#导入必须的库

import os
import shutil
import codecs


class DataPrcoess():
    def getdata(self,pathd):
        ls = os.listdir("./" + pathd)
        count = 0
        all_data = []
        for i in ls:
            # print(i)
            path = "./" + pathd + "/" + i
            all_data.append(self.readText(path))
            count += 1
        print(len(all_data))
        return all_data
    #新建文件夹
    # def setDir(self,path):
    #     if path not in os.listdir('./'):
    #         os.mkdir("./" + path)
    #     else:
    #         shutil.rmtree("./" + path)
    #         os.mkdir("./" + path)
    def setDir(self,path):
        if path not in os.listdir('./'):
            os.mkdir(path)
        else:
            shutil.rmtree(path)
            os.mkdir(path)
    # 将二进制转化为数字
    def hexdump(self,src, length=16):
        result = []
        digits = 4 if isinstance(src, str) else 2
        for i in range(0, len(src), length):
            s = src[i:i + length]
            hexa = ' '.join([hex(x)[2:].upper().zfill(digits) for x in s])
            text = ''.join([chr(x) if 0x20 <= x < 0x7F else '.' for x in s])
            result.append(
                "{0:04X}".format(i) + ' ' * 3 + hexa.ljust(length * (digits + 1)) + ' ' * 3 + "{0}".format(text))
        return '\n'.join(result)

    # 将数据以流为类写入文件夹
    def writeabnormaldata(self,data_excel, dirname):
        mid_pcap = []
        label_data = []
        label_label = []
        n = 1
        # self.setDir(dirname)
        for i in range(len(data_excel)):
            if data_excel["data"][i] == 0:
                continue
            count = 0
            mid_pcap.append(data_excel["data"][i])
            data_number = bytes(str(data_excel["data"][i][2:-1]), encoding="utf-8")
            original = codecs.escape_decode(data_number, "hex-escape")
            path = "./" + dirname + "/第%d条数据流" % n + ".txt"
            with open(path, 'a') as f:
                label_data.append(original[0])
                f.write(self.hexdump(original[0]))
                f.write("结束")
                label_label.append(n)
                count += 1
            data_excel["data"][i] = 0
            for j in range(i + 1, len(data_excel)):
                if data_excel["srcip"][i] == data_excel["srcip"][j] and data_excel["dstip"][i] == data_excel["dstip"][
                    j] and data_excel["sport"][i] == data_excel["sport"][j] and data_excel["dport"][i] == \
                        data_excel["dport"][j] and data_excel["proto"][i] == data_excel["proto"][j]:
                    count += 1
                    if count>6 and count<=7:
                        n += 1
                        count=0
                    mid_pcap.append(data_excel["data"][j])
                    data_number = bytes(data_excel["data"][j][2:-1], encoding="utf-8")
                    original = codecs.escape_decode(data_number, "hex-escape")
                    path = "./" + dirname + "/第%d条数据流" % n + ".txt"
                    with open(path, 'a') as f:
                        label_data.append(original[0])
                        f.write(self.hexdump(original[0]))
                        f.write("结束")
                        label_label.append(n)
                    data_excel["data"][j] = 0
            if count>0:
                n += 1
        return label_data ,label_label

    def readText(self,path):
        data_need = []
        mid_data = []
        file = open(path, "r")
        for line in file.readlines():
            curLine = line.strip().split(" ")
            flag = 0
            #         print(curLine)
            #         print("len",len(curLine))
            for i in range(3, 19):
                flag = 1
                #             print(curLine[i])
                if (i + 1 >= len(curLine) or (curLine[i] == "" and curLine[i + 1] == "")):
                    flag = 0
                    break
                else:
                    for h in range(i, len(curLine)):
                        if "结束" in curLine[h]:
                            flag = 0
                            #                 print(mid_data)
                            break
                mid_data.append(int(curLine[i], 16))
            if flag == 0:
                data_need.append(mid_data)
                mid_data = []
        return data_need