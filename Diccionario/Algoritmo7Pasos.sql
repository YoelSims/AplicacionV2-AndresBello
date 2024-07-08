--Paso 1: Entidades Regulares o Fuertes

Estudiantes (id_estudiante(Clave Primaria), codigo_estudiante, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, 
avenida, calle, edificio, piso, apto, parroquia, municipio, telefono_estudiante,correo_estudiante, fecha_nacimiento, cedula_identidad, sexo)

Docente
id_docente ((Clave Primaria), primer_nombre_docente, segundo_nombre_docente, primer_apellido_docente, segundo_apellido_docente, fecha_nacimiento, cedula_docente, sexo, edad_docente, 
correo_docente, telefono_docente, direccion_docente)

Materia
id_materia ((Clave Primaria), nombre_materia)

Departamento
id_departamento ((Clave Primaria), nombre_departamento)

Notas
id_nota ((Clave Primaria), cualitativa_primer_corte, cuantitativa_primer_corte, cualitativa_segundo_corte, cuantitativa_segundo_corte, cualitativa_tercer_corte, cuantitativa_tercer_corte, nota_final)

Matriculas
id_matricula ((Clave Primaria), codigo_matricula, fecha_matricula, codigo_centro_escolar_procedente, codigo_unico_instituto, nombre_instituto, modalidad, anio_activo, repitente)

Turno
id_turno ((Clave Primaria), nombre_turno)

Grado
id_grado ((Clave Primaria), nombre_grado)

Asistencia
id_asistencia ((Clave Primaria), estado_asistencia)

Horario
id_horario ((Clave Primaria), hora_inicio, hora_fin)

Salon
id_salon ((Clave Primaria), tipo_salon, capacidad, ubicacion)

--Paso 2: Entidades Débiles

Representante (Entidad Débil) (id_representante (Clave Parcial), nombre_representante, apellido_representante, cedula_representante, 
telefono_representante, correo_representante, parentesco, id_estudiante (Foranea))

--Paso 3: Relaciones 1:1
No se identificaron relaciones 1:1 adicionales aparte de las ya identificadas en las entidades débiles.

--Paso 4: Relaciones 1:N
Matricula - Estudiantes: N:1
Entidades: Matricula, Estudiantes
Clave Foránea: id_estudiante (Clave Foranea en Matricula refiriéndose a la Clave Primaria id_estudiante en Estudiante)

Representante - Estudiantes: N:1
Entidades: Representante, Estudiantes
Clave Foránea: id_estudiante (Clave Foranea en Representante refiriéndose a la Clave Primaria id_estudiante en Estudiante)

Docente - Departamento: N:1
Entidades: Docente, Departamento
Clave Foránea: id_departamento (Clave Foranea en Docente refiriéndose a la Clave Primaria id_departamento en Departamento)

Nota - Estudiantes: N:1
Entidades: Nota, Estudiantes
Clave Foránea: id_estudiante (Clave Foranea en Nota refiriéndose a la Clave Primaria id_estudiante en Estudiantes)

Nota - Materia: N:1
Entidades: Nota, Materia
Clave Foránea: id_materia (Clave Foranea en Nota refiriéndose a la Clave Primaria id_materia en Materia)

Materia - Departamento: N:1
Entidades: Materia, Departamento
Clave Foránea: id_departamento (Clave Foranea en Materia refiriéndose a la Clave Primaria id_departamento en Departamento)

Estudiantes - Grado: N:1
Entidades: Estudiantes, Grado
Clave Foránea: id_grado (Clave Foranea en Estudiantes refiriéndose a la Clave Primaria id_grado en Grado)
Estudiantes - Turno: N:1

Entidades: Estudiantes, Turno
Clave Foránea: id_turno (Clave Foranea en Estudiantes refiriéndose a la Clave Primaria id_turno en Turno)

Usuarios - TiposUsuarios: N:1
Entidades: Usuarios, TiposUsuarios
Clave Foránea: id_tipo_usuario (Clave Foranea en Usuarios refiriéndose a la Clave Primaria id_tipo_usuario en TiposUsuarios)

--Paso 5: Relaciones N:M
Materia_Estudiante: N:M: (id_materia, id_estudiante)
Grado_Turno: N:M: (id_grado, id_turno)
Clase(id_estudiante, id_docente, id_asistencia, id_materia, id_horario, id_salon)

Estudiantes - Clase: N:M
(Un estudiante puede estar inscrito en múltiples clases, y una clase puede tener múltiples estudiantes)
Docente - Clase: N:M
(Un docente puede impartir múltiples clases, y una clase puede tener múltiples docentes)
Asistencia - Clase: N:M
(La asistencia se registra para cada estudiante en cada clase, y cada clase tiene múltiples registros de asistencia)

--Paso 6: Atributos Multivaluados
Matricula:
anio_activo(anio_activo, id_matricula)
modalidad(nombre_modalida, id_matricula)

Estudiantes:
Discapacidad (tipo_discapacidad, id_estudiante)
Nacionalidad (origen_nacionalidad, id_estudiante)
Direccion (avenida, calle, edificio, piso, apto, parroquia, municipio, id_estudiante)
Sección (nombre_seccion, id_estudiante)

Horario:
Día(nombre_dia, id_horario)

--Paso 7: Relaciones n-arias
Clase(id_estudiante, id_docente, id_asistencia, id_materia, id_horario, id_salon)