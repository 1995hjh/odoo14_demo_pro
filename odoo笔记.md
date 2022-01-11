# 创建项目
  new project--pure python--previously configured interpreter[选择odoo安装目录中的python目录中的python.exe]

# 引入odoo
  settings--project：项目名--project structure--add current root[添加odoo安装目录中的serve]

# 创建新模块：
 python环境路径  oddo-bin路径  scaffold  模块名  模块路径

## 注意：
 路径不允许有空格，比如odoo安装在C:\Program Files\Odoo 14.0.20220101\下面，路径中包含空格，那么应当先进入odoo的安装目录，然后在创建新模块
  > cd C:/
  > cd '.\Program Files\Odoo 14.0.20220101\'
  > python\python.exe server\odoo-bin scaffold demo_html C:\Workspace\odoo_demo_pro

# 运行新模块：
  拷贝odoo.conf, 修改相应配置
  add configured【打开运行配置，parameters处添加 -c C:\Workspace\odoo_demo_pro\local.conf，script path添加C:\Program Files\Odoo 14.0.20220101\server\odoo-bin】

# 刷新xml文件
  配置命令后面需要添加 --dev xml,完整如下：
  -c C:\Workspace\odoo_demo_pro\local.conf --dev xml

# 一些规则
  1、如果修改了数据库名，默认账号名密码  admin  admin\
  2、修改controllers.py文件，需要重启项目才能生效\
  3、通过xpath expr定位元素，只能定位到静态模块中的标签，不能定位动态生成的标签\
  4、odoo安装目录和新建的项目必须在同一个盘，否则新模块出现不能打开的bug\
  5、模块中新增xml文件，需要升级以后才生效
  6、如果找不到新模块，打开debug=1，刷新本地模块列表即可生效

# 一些尚未解决的问题（基于odoo14）
  1、views下面新建的xml文件如何引入scss文件\
  2、 static-src-xml目录下添加xml文件，如何添加路由\
  3、动态生成的标签如何定位
  