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

### 如果修改了数据库名，默认账号名密码  admin  admin

### 添加路由，项目需要重启
