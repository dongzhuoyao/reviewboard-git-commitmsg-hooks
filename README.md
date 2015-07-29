# reviewboard-git-commitmsg-hooks
参考赖勇浩（http://laiyonghao.com）  的代码

本代码主要实现在git中本地commit的时候和ReviewBoard结合验证reviewid.<br>
每次代码commit的时候,message中必须包含:review:XXX.<br>
不存在的reviewid不允许commit<br>.最终实现一种强制性review机制<br>

安装步骤:<br>
1,cd到本路径,执行python setup.py install<br>
2,将commit-msg这个文件放到你管理的项目的hooks文件夹中<br>
3,如果是windows系统,在C:\ProgramData\reviewboard-git-hooks的conf.ini中修改配置,填写ReviewBoard的地址,用户名,密码
