estilo = {"":0, "Padrão":0, "Negrito":1, "Underline":4, "Negativo":7}
text = {"":0, "Black":30, "Red":31, "Green":32, "Yellow":33, "Blue":34, "Magenta":35, "Cyan":36, "Grey":37, "White":97}
bg = {"":0, "Black":40, "Red":41, "Green":42, "Yellow":43,"Blue":44, "Magenta":45, "Cyan":46, "Grey":47, "White":107}


def colorir(msg, style='Padrão', texto='White', backgroud='Black'):
    print(f'\033[{estilo[style]};{text[texto]};{bg[backgroud]}m{msg}\033[m')
