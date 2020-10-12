print('Bara svara ja, nej eller kanske')
sömn = input('Vill du vakna? ')

if sömn == 'ja':
    sömn = input('Är du säker? ')
    if sömn == 'ja':
        sömn = input('Är du 100% säker? ')
        if sömn == 'ja':
            sömn = input('Är du verkligen säker? du kan ju sova mer ')
            if sömn == 'ja':
                sömn = input('Vill du verkligen vakna nu? ')
                if sömn == 'ja':
                    sömn = input('Vill du 100% vakna upp? ')
                    if sömn == 'ja':
                        sömn = input('Du är galen manen, okej vakna nu då!')

if sömn == 'nej':
    sömn = print('Godnatt :D')
    if sömn == 'nej':
        sömn = print('Godnatt :D')
        if sömn == 'nej':
            sömn = print('Godnatt :D')
            if sömn == 'nej':
                sömn = print('Godnatt :D')
                if sömn == 'nej':
                    sömn = print('Godnatt :D')
                    if sömn == 'nej':
                        sömn = print('Godnatt :D')

if sömn == 'kanske':
    sömn = print('Okej sleep förlamningsdemon kommer ta dig ;)')
    if sömn == 'kanske':
        sömn = print('Okej sleep förlamningsdemon kommer ta dig ;)')
        if sömn == 'kanske':
            sömn = print('Okej sleep förlamningsdemon kommer ta dig ;)')
            if sömn == 'kanske':
                sömn = print('Okej sleep förlamningsdemon kommer ta dig ;)')
                if sömn == 'kanske':
                    sömn = print('Okej sleep förlamningsdemon kommer ta dig ;)')
                    if sömn == 'kanske':
                        sömn = print('Okej sleep förlamningsdemon kommer ta dig ;)')

if not sömn == "ja" or "nej" or "kanske":
    print("Du svarade inte dem 3 svaren jag sa att du skulle svara")