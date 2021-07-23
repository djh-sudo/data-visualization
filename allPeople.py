from pyecharts.charts import Sunburst
from pyecharts import options as opts
import handleExcel as handle
from random import choice
from xpinyin import Pinyin
"""

"""
def readData():
    p = Pinyin()
    color = ['#da1d23',"#ebb40f","#dd4c51","#0aa3b5","#beb276","#9db2b7","#8b8c90","#3e0317","#e62969","#6569b0","#ef2d36","#ef2d36","#b53b54","#a5446f","#dd4c51","#120c0c","#039fb8","#5e777b","#f2684b","#e73451","#db646a","#e65656","#f89a1c","#aeb92c","#978847","#9d977f","#80a89d","#def2fd","#7a9bae","#cc7b6a","#a3a36f","#4eb849","#f68a5c","#c9b583","#fefef4","#baa635","#f7a128","#f26355","#744e03","#e2631e","#fde404","#7eb138","#ebb40f","#187a2f","#a2b029","#718933","#3aa255","#a2bb2b","#62aa3c","#03a653","#038549","#28b44b","#a3a830","#7ac141","#5e9a80","#c94930","#caa465","#dfbd7e","#be8663","#b9a449","#899893","#a1743b","#894810","#ddaf61","#b7906f","#eb9d5f","#ad213e","#794752","#cc3d41","#b14d57","#c78936","#8c292c","#e5762e","#a16c5a","#d4ad12","#9d5433","#c89f83","#bb764c","#692a19","#470604"]
    sh1 = handle.readByIndex('./stepover.xls', 3)
    col = handle.readSheetAllContentByCol(sh1)
    byClass = col[3][1:]
    name = col[1][1:]
    monitor = col[5][1:]
    CLASS = set()
    MONITOR = set()
    relation = {}
    for i in byClass:
        CLASS.add(i)
    for i in monitor:
        i = i.replace('\u3000','')
        if i:
            MONITOR.add(i)
    print("班级",CLASS)
    print("监督人",MONITOR)

    for k in range(len(name)):
        who = name[k]
        if who in MONITOR:
            belong = byClass[k]
            relation[who] = belong

    DATA = []
    RELATION = {}
    # 创建第一层行政班级
    count = 0
    for c in CLASS:
        temp = {}
        temp["name"] = c
        Color = {"color": choice(color)}
        temp["itemStyle"] = Color
        temp["children"] = []
        DATA.append(temp)
        RELATION[c] = count
        count = count + 1
    # 创建第二级负责人
    RELATION1 = {}
    for m in MONITOR:
        whoClass = relation[m]
        print("=> handle monitor ",m,whoClass)
        index = RELATION[whoClass]
        temp = {}
        if len(m) is 3:
            py = p.get_pinyin(m[0:2], tone_marks='numbers')
            py = py.split('-')
            pin = py[0][0] + py[1][0]
            pin = pin.upper()
            temp["name"] = pin + m.replace(m[0],'').replace(m[1],'')
        elif len(m) is 2:
            py = p.get_pinyin(m[0:1], tone_marks='numbers')
            py = py.split('-')
            pin = py[0][0]
            pin = pin.upper()
            temp["name"] = pin + m.replace(m[0], '')
        else:
            py = p.get_pinyin(m[0:3], tone_marks='numbers')
            py = py.split('-')
            pin = py[0][0] + py[1][0] + py[2][0]
            pin = pin.upper()
            temp["name"] = pin + m.replace(m[0], '').replace(m[1], '').replace(m[2], '')
        Color = {"color": choice(color)}
        temp["itemStyle"] = Color
        temp["children"] = []
        RELATION1[m] = len(DATA[index]["children"])
        # temp["value"] = 1
        # 对应的行政班级装入负责人列表
        DATA[index]["children"].append(temp)

    for k in range(len(name)):
        who = name[k]
        if who not in MONITOR or True:
            belongClass = byClass[k]
            supervisor = monitor[k].replace('\u3000','')
            # 得到对应的一级分支下标
            index = RELATION[belongClass]
            # 得到对应的二级分支下标
            index1 = RELATION1[supervisor]
            temp = {}
            if len(who) is 3:
                py = p.get_pinyin(who[0:2], tone_marks='numbers')
                py = py.split('-')
                pin = py[0][0] + py[1][0]
                pin = pin.upper()
                temp["name"] = pin + who.replace(who[0],'').replace(who[1],'')
            elif len(who) is 2:
                py = p.get_pinyin(who[0:1], tone_marks='numbers')
                py = py.split('-')
                pin = py[0][0]
                pin = pin.upper()
                temp["name"] = pin + who.replace(who[0], '')
            else:
                py = p.get_pinyin(who[0:3], tone_marks='numbers')
                py = py.split('-')
                pin = py[0][0] + py[1][0] + py[2][0]
                pin = pin.upper()
                temp["name"] = pin + who.replace(who[0], '').replace(who[1],'').replace(who[2],'')
            Color = {"color": choice(color)}
            temp["itemStyle"] = Color
            temp["value"] = 1
            DATA[index]["children"][index1]["children"].append(temp)
        else:
            continue
    # print(DATA)
    return DATA


def getStructure():
    data = readData()
    c = (
        Sunburst(init_opts=opts.InitOpts(theme='dark',width="700px", height="700px"))
        .add(
            "",
            data_pair=data,
            highlight_policy="ancestor",
            radius=[0, "95%"],
            sort_="null",
            levels=[
                {},
                {
                    "r0": "15%",
                    "r": "35%",
                    "itemStyle": {"borderWidth": 2},
                    "label": {"rotate": "tangential"},
                },
                {"r0": "35%", "r": "70%", "label": {"align": "right"}},
                {
                    "r0": "70%",
                    "r": "72%",
                    "label": {"position": "outside", "padding": 3, "silent": False},
                    "itemStyle": {"borderWidth": 3},
                },
            ],
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="负责结构图"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
        # .render("drink_flavors.html")
    )
    return c

