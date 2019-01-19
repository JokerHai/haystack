django 初学者 案例


使用步骤：

        python -m venv venv

        . venv/bin/activate 进入虚拟环境

        pip install -r requirements.txt 导入jar 依赖包


        使用数据迁移命令创建数据库

            生成迁移文件

            python manage.py makemigrations

            同步到数据库中

            python manage.py migrate

        注意：
                数据库配置文件需要更改，请查看数据库配置的是否相同


