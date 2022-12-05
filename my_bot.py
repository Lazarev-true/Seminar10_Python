from telegram.ext import ApplicationBuilder, CommandHandler
from commands import *


app = ApplicationBuilder().token("5583274342:AAGNVE4rtE1KIlRis2mWMrfKVdQ6Zx3TDts").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("sum", sum_now))
app.add_handler(CommandHandler("mult", mult_now))
app.add_handler(CommandHandler("graph", graph))
app.add_handler(CommandHandler("date", date_now))

print('Запуск')

app.run_polling()