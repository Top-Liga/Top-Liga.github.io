import traceback    # модуль трассировки для отслеживания ошибок
try:    
    import os   # импорт модуля работы с каталогами
    import datetime     # модуль для определния текущей даты
    DateNow = str(datetime.datetime.utcnow())[:19].replace(":", "-")    # текущая дата по UTC, отформатированная под строку для имени файла
    os.mkdir("build")
    with open("build/index.html", 'w') as f:
        f.write('\
        <!DOCTYPE html>\
        <html>\
        <head>\
            <meta charset="utf-8" />\
            <title>TopLiga</title>\
        </head>\
        <body>\
            <div class="body-content">\
                best games actual standings\
                <hr />\
                <footer>\
                    <p>'+DateNow+'</p>\
                </footer>\
            </div>\
        </body>\
        </html>\
        ')
except: 
    traceback.print_exc()
