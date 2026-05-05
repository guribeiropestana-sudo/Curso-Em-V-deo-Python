cid = str(input('Qual cidade você nasceu ')).strip()
print('Você nasceu numa cidade que começa com SANTO? ',end='')
print(cid[:5].upper()=='SANTO')
