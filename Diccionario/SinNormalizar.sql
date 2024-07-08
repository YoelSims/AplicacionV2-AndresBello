------------------------ENTIDADES------------------
Estudiantes
id_estudiante (Clave Primaria)
codigo_estudiante (Atributo Simple)
nombre (Atributo Compuesto: primer_nombre_estudiante, segundo_nombre_estudiante)
apellido(Atributo Compuesto: primer_apellido_estudiante, segundo_apellido_estudiante)
direccion (Atributo Compuesto, Multivalorado: avenida, calle, edificio, piso, apto, parroquia, municipio)
telefono (Atributo Simple)
correo (Atributo Simple))
fecha_nacimiento (Atributo Simple)
cedula_identidad (Atributo Simple)
edad (Atributo Derivado de fecha_nacimiento)
sexo (Atributo Simple)
discapacidad (Atributo Multivalorado)
nacionalidad (Atributo Multivalorado)
seccion (Atributo Multivalorado)

Representante (Entidad Debil)
id_representante (Clave Parcial)
nombre_representante(Atributo Compuesto: nombre_representante, apellido_representante)
cedula_representante(Atributo Simple)
telefono_representante(Atributo Simple)
correo_representante(Atributo Simple)
parentesco(Atributo Simple)

Docente
id_docente (Clave Primaria)
nombre (Atributo Compuesto: primer_nombre_docente, segundo_nombre_docente)
apellido(Atributo Compuesto: primer_apellido_docente, segundo_apellido_docente)
fecha_nacimiento (Atributo Simple)
cedula_docente (Atributo Simple)
sexo (Atributo Simple)
edad_docente (Atributo Derivado de fecha_nacimiento)
correo_docente (Atributo Simple)
telefono_docente (Atributo Multivalorado)
direccion_docente(Atributo Simple)

Materia
id_materia (Clave Primaria)
nombre_materia (Atributo Simple)

Departamento
id_departamento (Clave Primaria)
nonmbre_departamento (Atributo Simple)

Notas
id_nota (Clave Primaria)
nota_primer_corte(Atributo Compuesto: cualitativa_primer_corte, cuantitativa_primer_corte)
nota_segundo_corte(Atributo Compuesto: cualitativa_segundo_corte, cuantitativa_segundo_corte)
nota_tercer_corte(Atributo Compuesto: cualitativa_tercer_corte, cuantitativa_tercer_corte)
nota_final (Atributo Simple)

Matriculas
id_matricula (Clave Primaria)
código_matricula (Atributo Simple)
fecha_matricula (Atributo Simple)
codigo_centro_escolar_procedente (Atributo Simple)
codigo_unico_instituto (Atributo Simple)
nombre_instituto (Atributo Simple)
modalidad (Atributo Multivalorado)
año_activo (Atributo Simple)
repitente (Atributo Simple)

Turno
id_turno(Clave Primaria)
nombre_turno(Atributo Simple)

Grado
id_grado(Clave Primaria)
nombre_grado(Atributo Simple)

Asistencia
id_asistencia(Clave Primaria)
estado_asistencia(Atributo Simple)

Horario
id_horario(Clave Primaria)
horario(Atributo Compuesto: hora_inicio, hora_fin)
dia(Atributo Multivalorado)

Salon
id_salon(Clave Primaria)
tipo_salon(Atributo Simple)
capacidad(Atributo Simple)
ubicacion(Atributo Simple)

Usuarios
id_usuario (Clave Primaria)
usuario (Atributo Simple)
contraseña (Atributo Simple)
correo (Atributo Simple)
ultima_sesion (Atributo Simple)

TiposUsuarios
id_tipo_usuario (Clave Primaria)
tipo_usuario (Atributo Simple)

Relaciones y Cardinalidad:

Matricula – Estudiante – Cardinalidad: N:1
Muchos a uno (Muchas matrículas pueden pertenecer a un solo estudiante, pero cada matrícula pertenece a un solo estudiante)

Representante – Estudiante – Cardinalidad: N:1
Muchos a uno (Muchos representantes pueden estar relacionados con un solo estudiante, pero cada representante está relacionado con un solo estudiante)

Docente – Departamento – Cardinalidad: N:1
Muchos a uno (Muchos docentes pueden pertenecer a un solo departamento, pero cada docente pertenece a un solo departamento)

Nota – Estudiante – Cardinalidad: N:1
Muchos a uno (Muchas notas pueden pertenecer a un solo estudiante, pero cada nota pertenece a un solo estudiante)

Nota – Materia – Cardinalidad: N:1
Muchos a uno (Muchas notas pueden ser de una sola materia, pero cada nota pertenece a una sola materia)

Materia – Departamento – Cardinalidad: N:1
Muchos a uno (Muchas materias pueden pertenecer a un solo departamento, pero cada materia pertenece a un solo departamento)

Usuarios - Tipos de Usuarios – Cardinalidad: N:1
Relación: Muchos a uno (Muchos usuarios pueden tener el mismo tipo, pero cada usuario tiene un solo tipo)

Materias – Estudiantes – Cardinalidad: N:M
Relación: Muchos a muchos (Muchos estudiantes pueden tener muchas materias, y muchas materias pueden tener muchos estudiantes)

Estudiante y Grado Cardinalidad: N:1
Relación: Muchos a uno (Un estudiante está en un único grado, pero un grado puede tener múltiples estudiantes.)

Estudiantes y Turno Cardinalidad: N:1
Relación: Muchos a uno (Un estudiante está en un único turno, pero un turno puede tener múltiples estudiantes.)

Turno y Grado Cardinalidad: N:M
Relacion: Muchos a Muchos (Un turno puede estar asociado con varios grados, Un grado puede tener varios turnos.)
