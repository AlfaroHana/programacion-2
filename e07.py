import datetime

dia= int(input("Ingresa tu día de nacimiento: "))
mes= int(input("Ingresa tu mes de nacimiento: "))
año_nac= int(input("Ingresa tu año de nacimiento: "))
fn= datetime.datetime(año_nac, mes, dia)
fa= datetime.datetime.now()

t_delta= fa-fn
dias_totales= t_delta.days

años= dias_totales//365
dias_restantes= dias_totales%365
meses_restantes= dias_restantes//30


ts= fn.timestamp()

print("Fecha de nacimiento:", dia, "-", mes, "-", año_nac)
print("Total de segundos:", int(ts))
print("Días totales vividos:", dias_totales)
print("Edad: ", años, "años y ", meses_restantes," meses")


