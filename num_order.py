#blog of copyright owner: NancythEcat.org
#一千以内中文和阿拉伯自然数相互转换
import pdb

class Trans_Ch_to_Arab_num:
    def _init_(self):
        pass

    def recognize_ch_num(self, ch_num):
        ch_num_characters = ["零", "〇", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "百"]#, "千", "万", "亿", "兆"]
        boolean = 1
        if ch_num == "":
            boolean = 0
        else:
            for alpha in ch_num:
                if alpha in ch_num_characters:
                    pass
                else:
                    boolean = 0
            if boolean == 1:
                if len(ch_num) == 1:
                    if ch_num in ch_num_characters[2:13]:
                        pass
                    else:
                        boolean = 0
                elif len(ch_num) == 2:
                    if ch_num[0] == "十" in ch_num and ch_num[1] in ch_num_characters[2:12]:
                        pass
                    elif ch_num[1] == "十" in ch_num and ch_num[0] in ch_num_characters[2:12]:
                        pass
                    elif "百" in ch_num and len(ch_num) == 2:
                        pass
                    else:
                        boolean = 0
                elif len(ch_num) == 3:
                    if "十" in ch_num and ch_num[0] in ch_num_characters[2:12] and ch_num[-1] in ch_num_characters[2:12]:
                        pass
                elif len(ch_num) == 4:
                    if "百" in ch_num and "十" in ch_num:
                        pass
                    elif "百" in ch_num and "零" in ch_num:
                        pass
                    elif "百" in ch_num and "〇" in ch_num:
                        pass
                    else:
                        boolean = 0
                elif len(ch_num) == 5:
                    if ch_num[1] == "百" and ch_num[3] == "十" and ch_num[0] in ch_num_characters[2:12] and ch_num[2] in ch_num_characters[2:12] and ch_num[-1] in ch_num_characters[2:12]:
                        pass
                    else:
                        boolean = 0
                else:
                    boolean = 0
        return boolean

    def recognize_arab_num(self, arab_num):
        boolean = 1
        arab_num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if type(arab_num) == int:
            pass
        else:
            if type(arab_num) == str:
                for n in arab_num:
                    if n not in arab_num_list:
                        boolean = 0
                if arab_num[0] == "0":
                    boolean = 0
                if boolean == 1:
                    boolean = 2
        return boolean

    def single_ch_num(self, ch_num):
        if ch_num == "零":
            arab_num = 0        
        elif ch_num == "一":
            arab_num = 1
        elif ch_num == "二":
            arab_num = 2
        elif ch_num == "三":
            arab_num = 3
        elif ch_num == "四":
            arab_num = 4
        elif ch_num == "五":
            arab_num = 5
        elif ch_num == "六":
            arab_num = 6
        elif ch_num == "七":
            arab_num = 7
        elif ch_num == "八":
            arab_num = 8
        elif ch_num == "九":
            arab_num = 9
        elif ch_num == "十":
            arab_num = 10
        return arab_num

    def single_arab_num(self, arab_num):
        if arab_num == "0":
            ch_num = "零"        
        elif arab_num == "1":
            ch_num = "一"
        elif arab_num == "2":
            ch_num = "二"
        elif arab_num == "3":
            ch_num = "三"
        elif arab_num == "4":
            ch_num = "四"
        elif arab_num == "5":
            ch_num = "五"
        elif arab_num == "6":
            ch_num = "六"
        elif arab_num == "7":
            ch_num = "七"
        elif arab_num == "8":
            ch_num = "八"
        elif arab_num == "9":
            ch_num = "九"
        return ch_num        

    def trans_ch_to_arab(self, ch_num):
        #pdb.set_trace()
        if len(ch_num) == 1:
            arab_num = self.single_ch_num(ch_num)
        if len(ch_num) > 1:
            if ch_num[0] ==  "十" in ch_num and len(ch_num) == 2: #十四
                arab_num = 10 + self.single_ch_num(ch_num[1])
            elif ch_num[1] ==  "十" in ch_num and len(ch_num) == 2: #四十
                arab_num = 10 * self.single_ch_num(ch_num[0])
            elif "十" in ch_num and len(ch_num) == 3: #五十五
                arab_num = 10 * self.single_ch_num(ch_num[0]) + self.single_ch_num(ch_num[-1])
            elif "百" in ch_num and len(ch_num) == 5: #三百六十五
                arab_num = 100 * self.single_ch_num(ch_num[0]) + 10 * self.single_ch_num(ch_num[2]) + self.single_ch_num(ch_num[4])
            elif "百" in ch_num and len(ch_num) == 2: #六百
                arab_num = 100 * self.single_ch_num(ch_num[0])
            elif "百" in ch_num and len(ch_num) == 4 and "十" in ch_num: #五百五十
                arab_num = 100 * self.single_ch_num(ch_num[0]) + 10 * self.single_ch_num(ch_num[2])
            elif "百" in ch_num and len(ch_num) == 4 and "零" in ch_num: #七百零一
                arab_num = 100 * self.single_ch_num(ch_num[0]) + self.single_ch_num(ch_num[-1])
            elif "百" in ch_num and len(ch_num) == 4 and "〇" in ch_num: #七百〇一
                arab_num = 100 * self.single_ch_num(ch_num[0]) + self.single_ch_num(ch_num[-1])
        return arab_num

    def trans_arab_to_ch(self, arab_num):
        arab_num = str(arab_num)
        if len(arab_num) == 1:
            ch_num = self.single_arab_num(arab_num)
        elif len(arab_num) == 2:
            if arab_num == "10":
                ch_num = "十"
            elif arab_num[1] == "0":
                ch_num = self.single_arab_num(arab_num[0]) + "十"
            elif arab_num[0] == "1":
                ch_num = "十" + self.single_arab_num(arab_num[1])
            else:
                ch_num = self.single_arab_num(arab_num[0]) + "十" + self.single_arab_num(arab_num[1])
        elif len(arab_num) == 3:
            if arab_num[1:3] == "00":
                ch_num == self.single_arab_num(arab_num[0]) + "百"
            elif arab_num[1] == "0":
                ch_num = self.single_arab_num(arab_num[0]) + "百零" + self.single_arab_num(arab_num[-1])
            elif arab_num[-1] == "0":
                ch_num == self.single_arab_num(arab_num[0]) + "百" + self.single_arab_num(arab_num[1]) + "十"
            elif "0" not in arab_num:
                ch_num = self.single_arab_num(arab_num[0]) + "百" + self.single_arab_num(arab_num[1]) + "十" + self.single_arab_num(arab_num[-1])
        return ch_num

    def input_num(self, num):
        result = self.recognize_arab_num(num)
        if result == 1:
            num = [1, str(num)]
        elif result == 2:
            num = [1, num]
        elif self.recognize_ch_num(num):
            num = [2, num]
        else:
            num = [0, 1000]
        #print(num)
        return num

    def trans_num(self, num):
        #num = self.input_num()
        if num[0] == 0:
            transed_num = -1
        elif num[0] == 1:
            transed_num = self.trans_arab_to_ch(num[1])
        elif num[0] == 2:
            transed_num = self.trans_ch_to_arab(num[1])
        #print(transed_num)
        return transed_num


def main():
    trans = Trans_Ch_to_Arab_num()
    #num = trans.input_num()
    one_list = ["三十", "三三", "八百八十五", "五", "二十一", "十", "四十", "六十四", "十二", "七百零四"]
    arab_order_list = []
    ch_order_list = []
    #pdb.set_trace()
    for i in one_list:
        num = trans.input_num(i)
        if num[0]:
            ch_order_list.append(num[1])
    if ch_order_list:
        for ch_num in ch_order_list:
            arab_num = trans.trans_num([2, ch_num])
            arab_order_list.append(arab_num)
        arab_order_list.sort()
        ch_order_list = []
        for arab_num in arab_order_list:
            ch_order_list.append(trans.trans_num([1, arab_num]))
    else:
        ch_order_list = []
    print(ch_order_list)
    return ch_order_list

main()



