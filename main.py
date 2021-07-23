import date
import stackBar
import byClass
import allPeople
from pyecharts.charts import Calendar,Page


Page.save_resize_html("render.html",cfg_file="chart_config.json")

# def handleCalendar():
#     page = Page(layout=Page.DraggablePageLayout)
#     page.add(
#     date.calendar(),
#     stackBar.get_year_overlap_chart(),
#     byClass.get_year_overlap_chart(),
#     allPeople.getStructure(),
#     )
#     page.render("render.html")
#
#
# handleCalendar()