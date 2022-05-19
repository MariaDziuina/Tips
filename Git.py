# 0. Доступ у тебя есть, GitBash ты установила.
# 1. Сделай у себя где-то папку для репозитория. У меня она называется python, например.
# Открой GitBash, напиши там
cd path\folder\
# где path - адрес папки, folder - её название
# Так ты окажешься внутри этой папки

# 2. Напиши в командной строке
git init

# 3. Потом напиши
git clone git@bitbucket.org:zebrainy-dev/analytics.git
  
# 4. Напиши, что будет. Возможны два варианта:
# а) запросит логин-пароль от jira, ты его вводишь и получаешь доступ
# б) попросит создать SSH-ключ, это даже хорошо, хотя мой вроде ни разу не использовался

# 5. Если доступ будет, можно дальше голосом

# команда для создания ssh-ключа
ssh-keygen -t rsa -C "dzyuina.maria@skazbuka.com"
# -t rsa -C "dzyuina.maria@skazbuka.com" - это не всегда нужно указывать

# если нет доступа на clone можно попробовать узказать юзера
git config --global user.name "John Doe"
git config --global user.email dzyuina.maria@skazbuka.com


 git clone https://MariaDziuina@bitbucket.org/zebrainy-dev/analytics.git 


#Если есть проблемы с установкой пакета, импортом функций - возможно следует указать явно путь
import sys
sys.path.append('C:\\Users\\arx\\Documents\\Maria\\deeplay_python_common\\deeplay\\analytics')



