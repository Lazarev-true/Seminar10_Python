from telegram import Update
from telegram.ext import ContextTypes
import datetime
from sympy import *


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привет {update.effective_user.first_name}')
    
async def sum_now(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msge = update.message.text
    im = msge.split()
    b = int(im[1])
    a = int(im[2])
    y = a + b
    await update.message.reply_text(f'{a} + {b} = {y}')

async def mult_now(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msge = update.message.text
    im = msge.split()
    b = int(im[1])
    a = int(im[2])
    y = a * b
    await update.message.reply_text(f'{a} * {b} = {y}')

async def graph(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msge = update.message.text
    im = msge.split()
    b = int(im[1])
    a = int(im[2])
    x = Symbol('x')
    y = a * x**2 + b
    await update.message.reply_text(f'y = {a}x^2 + {b} {plot(y)}')
    
async def date_now(update: Update, context: ContextTypes.DEFAULT_TYPE):
    today = datetime.datetime.today()
    await update.message.reply_text(f'{today.strftime("%m/%d/%Y")}')