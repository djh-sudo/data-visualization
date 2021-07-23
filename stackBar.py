import datetime
from pyecharts import options as opts
from pyecharts.charts import Bar
import handleExcel as handle


def readData():
    sh1 = handle.readByIndex('./stepover.xls', 4)
    col = handle.readSheetAllContentByCol(sh1)
    l1 = col[2][1:]
    l2 = col[3][1:]
    l3 = col[4][1:]
    l4 = col[5][1:]
    l5 = col[6][1:]
    return l1, l2, l3, l4, l5



def get_year_overlap_chart():
    l1, l2, l3, l4, l5 = readData()
    begin = datetime.date(2021, 7, 11)
    end = datetime.date(2021, 8, 31)
    data = [
        [str(begin + datetime.timedelta(days=i))]
        for i in range((end - begin).days + 1)
    ]
    c = (
        Bar(init_opts=opts.InitOpts(theme='dark', width="1000px", height="400px"))  # 背景颜色
            .add_xaxis(data)
            .add_yaxis("1星人数", l1)
            .add_yaxis("2星人数", l2)
            .add_yaxis("3星人数", l3)
            .add_yaxis("4星人数", l4)
            .add_yaxis("5星人数", l5)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="每日星星统计", subtitle=""),
            datazoom_opts=opts.DataZoomOpts(),  # 水平线
            brush_opts=opts.BrushOpts(),  # 允许圈选功能
            toolbox_opts=opts.ToolboxOpts(),  # 允许切换折线/堆叠/柱状
            legend_opts=opts.LegendOpts(is_show=True,  # 图例的类型 显示与否
                                        type_='plain')
        )
    )
    return c
