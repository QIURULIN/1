
# coding: utf-8

＃在[1]中：
从烧瓶导入 render_template，flash，redirect，Flask，request，escape
从应用程式汇入应用程式
从随机导入样品


@ app.route（' / '）
def  index（） - > ' html '：
    return render_template（' index.html '，the_title  =  “选择困难症患者饭点助选器”）
       
def  log_request（req：' flask_request '，res：str） - > 无：
    “”“记录Web请求和结果的详细信息。”“”
    with  open（' houtai.log '，' a '）as log：
        print（req.form，req.remote_addr，req.user_agent，res，file = log，sep = ' | '）
        
@ app.route（' / results '，methods  = [ ' POST ' ]）
def  results（） - > ' html '：
    x = request.form [ ' x ' ]
    Y1 = [ '白粥'，'鸡蛋'，'油条'，'肠粉'，'面条'，'米粉'，'面包'，'风爪' ]
    y2 = [ '西红柿炒鸡蛋'，'鱼香茄子'，'咖喱牛肉'，'宫保鸡丁'，'蒸水蛋'，'青菜'，'水煮牛肉' ]
    Y3 = [ '西兰花炒肉片'，'凉拌青瓜'，'客家酿豆腐'，'蒜香小龙虾'，'小鸡炖蘑菇'，'糖醋排骨'，'白切鸡' ]
    如果 “早餐” 在 x：
     Ý =样品（Y1，3），'放弃吧已经是中午了'
    elif  '午餐'  in x：
     Ý =样品（Y2，3），'这算是早餐了还是两个鸡蛋就算了吧'
    否则：Y =样品（Y3，3），'少吃点吧万一有人叫你去宵夜呢'
    title =  '已预约成功'
    
    log_request（请求，结果）
    return render_template（' results.html '，
                           the_x = x，
                           the_y = y）

@ app.route（' / houtai '）
def  view_the_log（） - > ' html '：
    “”“将日志文件的内容显示为HTML表。”“”
    contents = []
    用 open（' houtai.log '）作为日志：
        对于线在日志：
            contents.append（[]）
            对于项目在 line.split（' | '）：
                内容[ - 1 ] .append（escape（item））
    titles =（' Form Data '，' Remote_addr '，' User_agent '，' Results '）
    return render_template（' houtai.html '，
                           the_title = '查看日志'，
                           the_row_titles =标题，
                           the_data = contents，）
