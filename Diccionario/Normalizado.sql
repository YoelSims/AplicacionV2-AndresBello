--Explicación del Proceso de Normalización
Identificar y separar los atributos compuestos: Los atributos como nombre_estudiante y direccion se descomponen en sus componentes más pequeños.
Eliminar atributos multivalorados: Se crean tablas adicionales para atributos multivalorados como telefono y relaciones muchos a muchos.
Eliminar dependencias parciales: Se aseguran de que todos los atributos no clave dependen de la clave primaria completa.
Eliminar dependencias transitivas: Se aseguran de que los atributos no clave no dependan de otros atributos no clave.

--Estudiantes
id_estudiante (Clave Primaria)
codigo_estudiante
primer_nombre, 
segundo_nombre, 
primer_apellido, 
segundo_apellido
telefono_estudiante
correo_estudiante
fecha_nacimiento
cedula_identidad
sexo
discapacidad (Foránea: id_discapacidad)
nacionalidad (Foránea: id_nacionalidad)
turno (Foránea: id_turno)
direccion (Foránea: id_direccion)
grado (Foránea: id_grado)
seccion (Foránea: id_seccion)

--Notas
id_nota (Clave Primaria)
cualitativa_primer_corte
cuantitativa_primer_corte
cualitativa_segundo_corte
cuantitativa_segundo_corte
cualitativa_tercer_corte
cuantitativa_tercer_corte
nota_final
estudiante (Foránea: id_estudiante)
materia (Foránea: id_materia)

--Docentes
id_docente (Clave Primaria)
primer_nombre_docente
segundo_nombre_docente
primer_apellido_docente
segundo_apellido_docente
fecha_nacimiento
cedula_docente
sexo
correo_docente
telefono_docente
direccion_docente
departamento (Foránea: id_departamento)

--Matriculas
id_matricula (Clave Primaria)
codigo_matricula
fecha_matricula
codigo_centro_escolar_procedente
codigo_unico_instituto
nombre_instituto
anio_activo (Foránea: id_anio_activo)
estudiante (Foránea: id_estudiante)
modalidad (Foránea: id_modalidad)

--Materias
id_materia (Clave Primaria)
materia
departamento (Foránea: id_departamento)

--Direccion
id_direccion (Clave Primaria)
avenida, 
calle
edificio
piso
apto
parroquia
municipio

--Turno
id_turno (Clave Primaria)
nombre_turno

--Secciones
id_seccion (Clave Primaria)
nombre_seccion

--Grados
id_grado (Clave Primaria)
nombre_grado

--Nacionalidad
id_nacionalidad (Clave Primaria)
origen_nacionalidad

--Discapacidades
id_discapacidad (Clave Primaria)
tipo_discapacidad

--Modalidades
id_modalidad (Clave Primaria)
nombre_modalidad

--Años Activos
id_anio_activo (Clave Primaria)
anio_activo

--Dias
id_dia(Clave Primaria)
nombre_dia

--Horario
id_horario(Clave Primaria)
hora_inicio
hora_fin
dia (Foránea: id_dia)

--Salon
id_salon (Clave Primaria)
tipo_salon
capacidad
ubicacion

--Asistencia
id_asistencia (Clave Primaria)
estado_asistencia

--Representantes (Entidad Débil)
id_representante (Clave Parcial)
nombre_representante
apellido_representante
cedula_representante
telefono_representante
correo_representante
parentesco
id_estudiante (Foranea)

--Departamentos
id_departamento (Clave Primaria)
nombre_departamento

--Usuarios
id_usuario (Clave Primaria)
usuario
contrasena
correo
ultima_sesion
tipo_usuario (Foránea: id_tipo_usuario)

--Tipos de Usuarios
id_tipo_usuario (Clave Primaria)
tipo_usuario

--Materias_Estudiantes
id_materia (Clave Foranea)
id_estudiante (Clave Foranea)

--grado_turno
id_grado (Clave Foranea)
id_turno (Clave Foranea)

--Clase
id_clase (Clave Primaria)
id_estudiante (Clave Foranea)
id_docente (Clave Foranea)
id_asistencia (Clave Foranea)
id_materia (Clave Foranea)
id_horario (Clave Foranea)
id_salon (Clave Foranea)
------------------------------------------------------------
Relaciones y Cardinalidad

--Estudiantes
Discapacidad (id_discapacidad)
Relación: Muchos a Uno (Muchos Estudiantes tienen una Discapacidad)

Nacionalidad (id_nacionalidad)
Relación: Muchos a Uno (Muchos Estudiantes tienen una Nacionalidad)

Turno (id_turno)
Relación: Muchos a Uno (Muchos Estudiantes tienen un Turno)

Dirección (id_direccion)
Relación: Muchos a Uno (Muchos Estudiantes tienen una Dirección)

Grado (id_grado)
Relación: Muchos a Uno (Muchos Estudiantes tienen un Grado)

Sección (id_seccion)
Relación: Muchos a Uno (Muchos Estudiantes tienen una Sección)

Representantes (Entidad Débil)
Relación: Uno a Muchos (Un Estudiante tiene muchos Representantes)

Notas (id_estudiante)
Relación: Uno a Muchos (Un Estudiante tiene muchas Notas)

Matriculas (id_estudiante)
Relación: Uno a Muchos (Un Estudiante tiene muchas Matriculas)

Materias_Estudiantes
Relación: Muchos a Muchos (Muchos Estudiantes tienen muchas Materias)

Notas
-----Estudiantes (id_estudiante)
------Relación: Muchos a Uno (Muchas Notas pertenecen a un Estudiante)

Materias (id_materia)
Relación: Muchos a Uno (Muchas Notas pertenecen a una Materia)

Docentes
Departamentos (id_departamento)
Relación: Muchos a Uno (Muchos Docentes pertenecen a un Departamento)

Clase (id_docente)
Relación: Uno a Muchos (Un Docente tiene muchas Clases)

Matriculas
Años Activos (id_anio_activo)
Relación: Muchos a Uno (Muchas Matriculas pertenecen a un Año Activo)

Estudiantes (id_estudiante)
Relación: Muchos a Uno (Muchas Matriculas pertenecen a un Estudiante)

Modalidades (id_modalidad)
Relación: Muchos a Uno (Muchas Matriculas pertenecen a una Modalidad)

Materias
Departamentos (id_departamento)
Relación: Muchos a Uno (Muchas Materias pertenecen a un Departamento)

----Notas (id_materia)
----Relación: Uno a Muchos (Una Materia tiene muchas Notas)

Materias_Estudiantes
Relación: Muchos a Muchos (Una Materia tiene muchos Estudiantes)

Clase (id_materia)
Relación: Uno a Muchos (Una Materia tiene muchas Clases)

Dirección
Estudiantes (id_direccion)
Relación: Uno a Muchos (Una Dirección tiene muchos Estudiantes)

------Docentes (id_direccion_docente) 
------Relación: Uno a Muchos (Una Dirección tiene muchos Docentes)

Turno
Estudiantes (id_turno)
Relación: Uno a Muchos (Un Turno tiene muchos Estudiantes)

Grado_Turno
Relación: Muchos a Muchos (Un Turno tiene muchos Grados)

Secciones
Estudiantes (id_seccion)
Relación: Uno a Muchos (Una Sección tiene muchos Estudiantes)

Grados
Estudiantes (id_grado)
Relación: Uno a Muchos (Un Grado tiene muchos Estudiantes)

Grado_Turno
Relación: Muchos a Muchos (Un Grado tiene muchos Turnos)

Nacionalidad
Estudiantes (id_nacionalidad)
Relación: Uno a Muchos (Una Nacionalidad tiene muchos Estudiantes)

Discapacidades
Estudiantes (id_discapacidad)
Relación: Uno a Muchos (Una Discapacidad tiene muchos Estudiantes)

Modalidades
Matriculas (id_modalidad)
Relación: Uno a Muchos (Una Modalidad tiene muchas Matriculas)

Años Activos
Matriculas (id_anio_activo)
Relación: Uno a Muchos (Un Año Activo tiene muchas Matriculas)

Días
Horario (id_dia)
Relación: Uno a Muchos (Un Día tiene muchos Horarios)

Horario
---Días (id_dia)
---Relación: Muchos a Uno (Muchos Horarios están en un Día)

Clase (id_horario)
Relación: Uno a Muchos (Un Horario tiene muchas Clases)

Salón
Clase (id_salon)
Relación: Uno a Muchos (Un Salón tiene muchas Clases)

Asistencia
Clase (id_asistencia)
Relación: Uno a Muchos (Una Asistencia tiene muchas Clases)

Representantes (Entidad Débil)

Estudiantes (id_estudiante)
Relación: Muchos a Uno (Muchos Representantes pertenecen a un Estudiante)

Departamentos
Docentes (id_departamento)
Relación: Uno a Muchos (Un Departamento tiene muchos Docentes)

Materias (id_departamento)
Relación: Uno a Muchos (Un Departamento tiene muchas Materias)

Usuarios
Tipos de Usuarios (id_tipo_usuario)
Relación: Muchos a Uno (Muchos Usuarios tienen un Tipo de Usuario)
Tipos de Usuarios

Usuarios (id_tipo_usuario)
Relación: Uno a Muchos (Un Tipo de Usuario tiene muchos Usuarios)

Materias_Estudiantes
Estudiantes (id_estudiante)
Relación: Muchos a Muchos (Muchos Estudiantes tienen muchas Materias)

Materias (id_materia)
Relación: Muchos a Muchos (Muchas Materias tienen muchos Estudiantes)

Grado_Turno
Grados (id_grado)
Relación: Muchos a Muchos (Muchos Grados tienen muchos Turnos)

Turnos (id_turno)
Relación: Muchos a Muchos (Muchos Turnos tienen muchos Grados)

Clase
Estudiantes (id_estudiante)
Relación: Muchos a Uno (Muchas Clases tienen un Estudiante)

Docentes (id_docente)
Relación: Muchos a Uno (Muchas Clases tienen un Docente)

Asistencias (id_asistencia)
Relación: Muchos a Uno (Muchas Clases tienen una Asistencia)

Materias (id_materia)
Relación: Muchos a Uno (Muchas Clases tienen una Materia)

Horarios (id_horario)
Relación: Muchos a Uno (Muchas Clases tienen un Horario)

Salones (id_salon)
Relación: Muchos a Uno (Muchas Clases tienen un Salón)

Estudiante y Clase Cardinalidad: N:M
Relacion: Muchos a Muchos (Un estudiante puede estar inscrito en múltiples clases, y una clase puede tener múltiples estudiantes.)

Docente y Clase Cardinalidad: N:M
Relacion: Muchos a Muchos (Un docente puede impartir múltiples clases, y una clase puede tener múltiples docentes).

Materia y Clase Cardinalidad: N:1
Relación: Muchos a uno (Una materia puede ser enseñada en múltiples clases, pero cada clase es para una sola materia.)

Horario y Clase Cardinalidad: N:1
Relación: Muchos a uno (Un horario puede estar asociado con múltiples clases, pero cada clase tiene un único horario.)

Salón y Clase Cardinalidad: N:1
Relación: Muchos a uno (Un salón puede albergar múltiples clases en diferentes horarios, pero cada clase se imparte en un único salón.)

Asistencia y Clase Cardinalidad: N:M
Relacion: Muchos a Muchos (La asistencia se registra para cada estudiante en cada clase, y cada clase tiene múltiples registros de asistencia.)
