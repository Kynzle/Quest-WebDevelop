import os
from flask import Flask, render_template

#данные о сотрудниках
staff_list = [{'Отдел разработки':[{'Главный разработчик':'Фёдоров Руслан'},{'Младший разработчик':'Иванова Ирина'},{'Тестировщик':'Романов Пётр'}]}, 
{'Бухгалтерия':[{'Старший бухгалтер':'Петров Иван'},{'Бухгалтер':'Антонова Ольга'}]}]  

def staff_form():
    ''' функция формирует шаблон с данными о сотрудниках'''
    html = render_template('start.html', emp1=staff_list[0].get('Отдел разработки')[0].get('Главный разработчик'), emp2=staff_list[0].get('Отдел разработки')[1].get('Младший разработчик'), 
    emp3=staff_list[0].get('Отдел разработки')[2].get('Тестировщик'),emp4=staff_list[1].get('Бухгалтерия')[0].get('Старший бухгалтер'),emp5=staff_list[1].get('Бухгалтерия')[1].get('Бухгалтер'))
    return html

folder = os.getcwd() # запоминаем текущую рабочую папку
# Создаём объект веб-приложения:
app = Flask(__name__, template_folder=folder, static_folder=folder)  
app.add_url_rule('/', 'start', staff_form, methods=['get'])   # создаёт правило для URL '/'

if __name__ == "__main__":
    # Запускаем веб-сервер:
    app.run()
