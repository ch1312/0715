from django.http import HttpResponse


def index(request):
    """
    视图   函数视图
    :param request:  请求对象，包含了请求信息的一个请求对象
    :return: response 响应对象
    """
    return HttpResponse("hello world")


def about(request):
    return HttpResponse("这是一个about页面")


def urltest(request, num):
    print(num)
    return HttpResponse("这是一个url测试视图%s" % (num))


def urltestnew(request, city, year):
    return HttpResponse("%s年在%s" % (year, city))

def hello():
    return "hekklo"



from django.template import Template,Context
def gethtml(request):
    html="""
    <html>
        <head>
        </head>
        <body>
        <h1>我是一个h1标签</h1>
        <h2>我是{{ name }}</h2>
        <a href = "https://baike.baidu.com/item/%E5%BE%B7%E6%80%80%E6%81%A9%C2%B7%E9%9F%A6%E5%BE%B7/5457042?fromtitle=%E9%9F%A6%E5%BE%B7&fromid=64575&fr=aladdin">
        <img src='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1568003957396&di=a9ef056162060cc8d0bb4e830d80f1a4&imgtype=0&src=http%3A%2F%2F03imgmini.eastday.com%2Fmobile%2F20180917%2F62855583b6b5e607bdd7c8d54c34c8dc_wmk.jpeg' title = '这是韦德' alt='这个是韦德'>
        </a>
        <p>{{ content }}</p>
        </body>
    </html>
    """
    #1.构建模板结构
    tempalte_obj = Template(html)
    #2.创建渲染模板
    params = dict(name="韦德大爷",content="好几个总冠军")
    content_obj = Context(params)
    #3.进行数据渲染
    result = tempalte_obj.render(content_obj)
    #4.返回结果
    # return HttpResponse(html)
    return HttpResponse(result)


from django.shortcuts import render
def indextmp(request):
    name = "哈士奇111"
    return render(request,'index.html',{"name":name})

    # return HttpResponse("index")


from django.shortcuts import render_to_response
# def abc(request):
#     name = "hello"
#     return render_to_response("abc.html",{"name":name})


from django.template.loader import get_template
def abc(request):
    template = get_template("abc.html")
    name = "hello"
    result = template.render({'name':name})

    return HttpResponse(result)

# def tpltest(request):
#     params = dict(name="zhansan",age=18,hobby=["eat","sing","pingpang",'football'])
#     return render(request,"tpltest.html",params)




def tpltest(request,age):
    print(age)
    print (type(age))
    class Say(object):
        def say(self):
            return "hello"

    name = "zhangsan"
    # age = 17
    age= int(age)
    hobby = ["eat","sing","pingpang",'football']
    score = {"shuxue":89,"yingyu":90,"yuwen":100}
    say = Say()
    myjs = """
    <script>
    alert("hello")
    </script>
    """
    imgname = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1568025129173&di=179235fcf0b3f5eac748fca5837b0002&imgtype=jpg&src=http%3A%2F%2Fimg4.imgtn.bdimg.com%2Fit%2Fu%3D509642299%2C4059745910%26fm%3D214%26gp%3D0.jpg"
    # return render(request,"tpltest.html",{"name":name,"age":age,"hobby":hobby,"score":score})
    return render(request,"tpltest.html",locals())

def statictest(request):
    return render(request,"statictest.html")


def staticdemo(request):
    # 球星排行榜
    params = [
        {"name":"麦迪","img":"maidi.jpg","url":"https://baike.baidu.com/item/%E7%89%B9%E9%9B%B7%E8%A5%BF%C2%B7%E9%BA%A6%E6%A0%BC%E9%9B%B7%E8%BF%AA/6118977?fromtitle=%E9%BA%A6%E8%BF%AA&fromid=136057&fr=aladdin"},
        {"name":"科比","img":"kb.jpg","url":"https:www.baidu.com"},
        {"name":"姚明","img":"ym.jpg","url":"https:www.sina.com"},
        {"name":"易建联","img":"yjl.jpg","url":"https:www.taobao.com"},
    ]

    return render(request, "staticdemo.html", locals())

