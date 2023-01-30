import colorama
# вимикає згортання
colorama.init(wrap=False)
# автоскидання кольору, колір заднього плану, яскравість текст
colorama.init(autoreset=True)
# колір тексту
print(colorama.Fore.MAGENTA + 'some MAGENTA text')
# колір заднього планну тексту
print(colorama.Back.BLACK + 'and with a green background')
# яскравість тексту
print(colorama.Style.DIM + 'and in dim text')
# скидання кольору, колір заднього плану, яскравість тексту
print(colorama.Style.RESET_ALL)
print('back to normal now')
print(colorama.Fore.MAGENTA + colorama.Back.BLACK + colorama.Style.DIM + "back")




