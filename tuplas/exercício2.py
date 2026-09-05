vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]

print('Produtos com mais vendas em 2020 do que em 2019:')
for i in vendas_produtos:
  produto, v2019, v2020 = i
  if v2020 > v2019:
    percentual = (v2020 / v2019 - 1) * 100
    print(f'{produto}, com {v2019} vendas em 2019, e {v2020} vendas em 2020, um aumento de {percentual:.2f}%')
