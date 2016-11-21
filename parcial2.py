import sqlite3 #Importamos el modulo de SQLite este ya lo incluye por default debian
conn = sqlite3.connect('datos_empleados.db') #Abrimos la base de datos 
print "Base de datos conectada con"
empleadoos='''
 SELECT id,nombre,salario,nombredepto FROM empleado  JOIN departamento
      ON empleado.id_depto = departamento.id_depto 
 order  by departamento.id_depto;
 '''

reempleado = conn.execute(empleadoos)
listatramos = []  
for row in reempleado:
	#print "id = ", row[0]
	#print "nombre = ", row[1]
	#print "salario = ", row[2]
	#print "departamento = ", row[3] 
	if row[2] > 0.01 and row[2] < 472:
		if row[0] not in listatramos:
			descuento_afp = row[2]*0.0625
			descuento_isss= row[2]*0.03
			total = descuento_afp+descuento_isss
			renta = 0
			salario_neto = row[2] - total
			id_empleado = row[0]
			conn.execute("INSERT INTO pago_empleado2 (id_empleado,descuento_afp,descuento_isss,renta,salario_neto) VALUES (?,?,?,?,?)", (id_empleado,round(descuento_afp,2),round(descuento_isss,2),round(renta,2),round(salario_neto,2)))
			conn.commit()
			print listatramos
			listatramos.append(row[0])
	if row[2] > 472 and row[2] < 895.24:
		if row[0] not in listatramos:
			id_empleado = row[0]
			descuento_afp = row[2]*0.0625
			descuento_isss= row[2]*0.03
			totaldes = descuento_afp+descuento_isss
			exceso= row[2]-472
			total_tramo=exceso * 0.10
			renta=total_tramo+17.67
			totales = totaldes + renta
			salario_neto = row[2] - totales
			conn.execute("INSERT INTO pago_empleado2 (id_empleado,descuento_afp,descuento_isss,renta,salario_neto) VALUES (?,?,?,?,?)",  (id_empleado,round(descuento_afp,2),round(descuento_isss,2),round(renta,2),round(salario_neto,2)))
			conn.commit()
			listatramos.append(row[0])
	if row[2] > 895.24 and row[2] < 2038.10:
		if row[2] not in listatramos:
			id_empleado = row[0]
			descuento_afp = row[2]*0.0625
			descuento_isss= row[2]*0.03
			totaldes = descuento_afp+descuento_isss
			exceso= row[2]-895.24
			total_tramo=exceso * 0.20
			renta=total_tramo+ 60.00
			totales = totaldes + renta
			salario_neto = row[2] - totales
			conn.execute("INSERT INTO pago_empleado2 (id_empleado,descuento_afp,descuento_isss,renta,salario_neto) VALUES (?,?,?,?,?)",  (id_empleado,round(descuento_afp,2),round(descuento_isss,2),round(renta,2),round(salario_neto,2)))
			conn.commit()
			listatramos.append(row[0])
	if row[2] > 2038.11:
		if row[0] not in listatramos:
			id_empleado = row[0]
			descuento_afp = row[2]*0.0625
			descuento_isss= row[2]*0.03
			totaldes = descuento_afp+descuento_isss
			exceso= row[2]-2038.10
			total_tramo=exceso * 0.30
			renta=total_tramo+ 288.57
			totales = totaldes + renta
			salario_neto = row[2] - totales
			conn.execute("INSERT INTO pago_empleado2 (id_empleado,descuento_afp,descuento_isss,renta,salario_neto) VALUES (?,?,?,?,?)",  (id_empleado,round(descuento_afp,2),round(descuento_isss,2),round(renta,2),round(salario_neto,2)))
			conn.commit()
			listatramos.append(row[0])
			cursor2 = conn.cursor()
sql1= '''SELECT empleado.id, pago_empleado2.id_empleado, empleado.nombre, empleado.salario,pago_empleado2.descuento_afp, pago_empleado2.descuento_isss, pago_empleado2.renta, pago_empleado2.salario_neto FROM empleado INNER JOIN pago_empleado2 ON empleado.id = pago_empleado2.id_empleado order by pago_empleado2.id_empleado;'''
try:
	cursor1 = cursor2.execute(sql1)
	for row in cursor1:
		print row
except:
	conn.rollback()
conn.close()


