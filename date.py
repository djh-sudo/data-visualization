import random
import datetime
import handleExcel as handle
import pyecharts.options as opts
from pyecharts.charts import Calendar,Page
# Page.save_resize_html("render.html",cfg_file='chart_config.json')


def getData():
    sh1 = handle.readByIndex('./stepover.xls', 4)
    col = handle.readSheetAllContentByCol(sh1)
    number = col[8]
    return number


def calendar():
    begin = datetime.date(2021, 7, 11)
    end = datetime.date(2021, 8, 31)
    peopleNumber = getData()
    data = [
        [str(begin + datetime.timedelta(days=i)), peopleNumber[i]]
        for i in range((end - begin).days + 1)
        ]

    can = (
        Calendar(init_opts=opts.InitOpts(theme='dark',width="500px", height="300px"))
        .add(
            series_name="",
            yaxis_data=data,
            calendar_opts=opts.CalendarOpts(
                pos_top="80",
                pos_left="30",
                pos_right="10",
                range_= ['2021-07-11', '2021-08-31'],
                yearlabel_opts=opts.CalendarYearLabelOpts(is_show= True),
            ),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(pos_top="30", pos_left="150", title="2021一战到底每日打卡人数"),
            visualmap_opts=opts.VisualMapOpts(
                max_=178, min_=160, orient="horizontal", is_piecewise=False
            ),
        )
        # .render("calendar_heatmap.html")
    )

    return can

