a = float(input('Qual é a altura da parede? '))
l = float(input('Qual é a largura da parede? '))
print('A area da parede é {:.2f}m²'.format(a*l),end=',')
print(' será necessário {:.2f}L de tinta.'.format(a*l/2))