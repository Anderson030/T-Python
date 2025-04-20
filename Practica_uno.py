#Promedio de duración

otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5 
curso_promedio_crudo = 5
curso_dalto_crudo = 3.5


# Diferencias de duración 

diferencia_con_min =  dalto_curso / otros_cursos_min *100  #Nos indica cual es el porcentaje de diferencia
print(diferencia_con_min) #En este caso nos indica que el curso de dalto dura 60% de lo que duran los cursos min

#Pero si le restamos 100, nos da que el curso de dalto dura 40% menos que los cursos min

diferencia_con_min = 100 - dalto_curso / otros_cursos_min *100 
print(f"El curso de dalto dura {diferencia_con_min}% menos que el curso más rápido.")

diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
print(f"El curso de dalto dura {diferencia_con_max}% menos que el curso de mayor duración.")

diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio *100
print(f"El curso de dalto dura {diferencia_con_promedio}% menos que un curso de duración promedia.")

diferencia_promedio_crudo = 100 - otros_cursos_promedio /curso_promedio_crudo * 100 
print(f"La diferencia es de {diferencia_promedio_crudo}%")

diferencia_promedio_dalto = 100 - dalto_curso *1000 //curso_dalto_crudo / 10 
print(f"La diferencia es de {diferencia_promedio_dalto}%")


print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos")

print(f"Ver 10 horas de otros cursos equivale a ver {dalto_curso * 1000 // otros_cursos_promedio / 10} horas del curso de Dalto")












