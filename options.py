from telebot import types

HOME_OPTIONS = []
for option in ['Order product','Check order status', 'Review Product', 'Cancel Order', 'Abort Order','Change Language','Rules', 'Help']:
     HOME_OPTIONS.append(types.InlineKeyboardButton(option, callback_data = option))