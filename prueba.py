'''num_reg='21.198'
split = num_reg.split('.')
num_reg=''
for i in range(len(split)):
    num_reg+=split[i]
num_reg=int(num_reg)'''


persona = Alumno.objects.get(num_reg=pk)
if persona == None:
    persona = Profesor.objects.get(id=pk)
    if persona == None:
        persona == Preceptor.objects.get(id=pk)
        if persona == None:
            pass
else:
    pass # llamo al index con el parametro persona