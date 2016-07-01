imgur-exam 
===========

##使用 ##

Django https://www.djangoproject.com/<br>
requests http://docs.python-requests.org/en/master/<br>
Bootstrap http://getbootstrap.com/<br>
Jquery https://jquery.com/<br>
imgur http://api.imgur.com/<br>

需求
----

访问 http://127.0.0.1/upload/ 打开一个页面，页面正中间（竖直居中、水平居中）有一个按钮，点击后弹出文件选择框，选择文件后（必须限制只能选择图片类型的文件，其他文件不可选或弹出提示）将图片上传至imgur，并在按钮下方直接显示此图片的在线链接（无刷新无跳转），按钮上方为所有用户最近上传的十张图片与图片链接（横排、响应式）。

##实现##

Django FirstBlood Project upload app,用户账号密码过期时间有两年时间所以直接获取access_token，不需要每次重复获取。<br>
参照api.imgur.com,注册app之后可以直接实现获取照片<br>

##说明##

runserver之后访问 http://127.0.0.1/upload
