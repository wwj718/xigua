#用来本项目记录经验与备忘


类型：模板
位置：main
名称：base.html
{% url "link_list_latest" as link_list_latest %}<!--最新链接  项目-->
注释：

位置: url("^best/$",
        CommentList.as_view(),  #这个才是view 逻辑部分
        name="comment_list_best"),
最佳建议模范这个,都是评分最高
 #按分数排序如此简单，有接口，不添加false就行  很好的设计

注意事项：  
item 是link，是核心对象   我们的核心对象是Suggestions  可以暂且用原来的的名字
model class Link(Displayable, Ownable)  


#coding=utf-8

