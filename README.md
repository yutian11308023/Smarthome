# 代码内容包含：

    1.Django整体项目框架代码:  
        myhome/
        Smarthome/
        manage.py
     
    2.语音模块和数据库交互部分代码：  
        API_server.py
     
    3.MQTT通信和数据库交互部分代码：
        mqttsubclient_nogateway.py
        mqttsubclient.py
        mqttpubclient.py  
        
    4.数据库：
        db.sqlite3
    
# 使用说明：  

-     将代码拷贝至已经配置好环境（hpecl_backup_7_26.rar）的树莓派中，进入manage.py同级目录
-     运行python3 manage.py runserver 0.0.0.0:8088
-     在同局域网下的浏览器访问：http://192.168.137.9:8088/myhome/index/，则可进入HPECL智能家居界面 
      ==注意：其中"192.168.137.9"应为当前树莓派ip。如果树莓派ip有改变，输入网址ip也需要改变，同时替换Smarthome/settings.py文件中的第28行ALLOWED_HOST的ip。==
-     运行python3 API_server.py，即可进行语音交互
-     运行python3 mqttsubclient_nogateway.py （不用网关时订阅节点数据）
            python3 mqttsubclient.py（用网关时订阅节点数据）  
            python3 mqttpubclient.py（发布控制命令数据）
      即可进行节点数据交互
