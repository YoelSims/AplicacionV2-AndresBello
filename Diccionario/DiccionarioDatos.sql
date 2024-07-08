estudiante:
Campo	Tipo de Dato	No Nulo	Clave	Tabla Relacionada	Descripción
id_estudiante	INT	No	Primaria		Identificador único del estudiante.
codigo_estudiante	VARCHAR(10)	Sí			Código único asignado al estudiante.
primer_nombre_estudiante	VARCHAR(50)	Sí			Primer nombre del estudiante.
segundo_nombre_estudiante	VARCHAR(50)	Sí			Segundo nombre del estudiante. (Puede ser nulo)
primer_apellido_estudiante	VARCHAR(50)	Sí			Primer apellido del estudiante.
segundo_apellido_estudiante	VARCHAR(50)	Sí			Segundo apellido del estudiante. (Puede ser nulo)
direccion	VARCHAR(100)	Sí			Dirección de domicilio del estudiante.
telefono	VARCHAR(15)	Sí			Número de teléfono del estudiante.
correo_estudiante	VARCHAR(20)	Sí	Única		Correo electrónico del estudiante (debe ser único).
fecha_nacimiento	DATE	Sí			Fecha de nacimiento del estudiante.
cedula_identidad	VARCHAR(20)	Sí	Única		Número de cédula de identidad del estudiante (debe ser único).
id_sexo	INT	Sí	Foránea	Sexo	Clave foránea que referencia el sexo del estudiante.
id_discapacidad	INT	Sí	Foránea	Discapacidades	Clave foránea que referencia la discapacidad del estudiante.
id_nacionalidad	INT	Sí	Foránea	Nacionalidad	Clave foránea que referencia la nacionalidad del estudiante.
id_turno	INT	Sí	Foránea	Turnos	Clave foránea que referencia el turno del estudiante.
id_municipio	INT	Sí	Foránea	Municipio	Clave foránea que referencia el municipio del estudiante.
id_grado	INT	Sí	Foránea	Grados	Clave foránea que referencia el grado del estudiante.
id_seccion	INT	Sí	Foránea	Secciones	Clave foránea que referencia la sección del estudiante.

nota:
Campo	Tipo de Dato	No Nulo	Clave	Tabla Relacionada	Descripción
id_nota	INT	No	Primaria		Identificador único de la nota.
cualitativa_primer_corte	VARCHAR(50)	Sí			Evaluación cualitativa del primer corte.
cuantitativa_primer_corte	INT	Sí			Evaluación cuantitativa del primer corte.
cualitativa_segundo_corte	VARCHAR(50)	Sí			Evaluación cualitativa del segundo corte.
cuantitativa_segundo_corte	INT	Sí			Evaluación cuantitativa del segundo corte.
cualitativa_tercer_corte	VARCHAR(50)	Sí			Evaluación cualitativa del tercer corte.
cuantitativa_tercer_corte	INT	Sí			Evaluación cuantitativa del tercer corte.
nota_final	INT	Sí			Nota final del estudiante en la materia.
id_materia	INT	Sí	Foránea	Materias	Clave foránea que referencia la materia asociada a la nota.
id_estudiante	INT	Sí	Foránea	Estudiantes	Clave foránea que referencia el estudiante asociado a la nota.

docente:
Campo	Tipo de Dato	No Nulo	Clave	Tabla Relacionada	Descripción
id_docente	INT	No	Primaria		Identificador único del docente.
primer_nombre_docente	VARCHAR(50)	Sí			Primer nombre del docente.
segundo_nombre_docente	VARCHAR(50)	Sí			Segundo nombre del docente. (Puede ser nulo)
primer_apellido_docente	VARCHAR(50)	Sí			Primer apellido del docente.
segundo_apellido_docente	VARCHAR(50)	Sí			Segundo apellido del docente. (Puede ser nulo)
fecha_nacimiento	DATE	Sí			Fecha de nacimiento del docente.
cedula_docente	VARCHAR(20)	Sí	Única		Número de cédula de identidad del docente (debe ser único).
id_sexo	INT	Sí	Foránea	Sexo	Clave foránea que referencia el sexo del docente.
telefono	VARCHAR(15)	Sí			Número de teléfono del docente.
correo_docente	VARCHAR(50)	Sí	Única		Correo electrónico del docente (debe ser único).
id_departamento	INT	Sí	Foránea	Departamentos	Clave foránea que referencia el departamento del docente.

materia:
Campo	Tipo de Dato	No Nulo	Clave	Tabla Relacionada	Descripción
id_materia	INT	No	Primaria		Identificador único de la materia.
materia	VARCHAR(50)	Sí			Nombre o código de la materia.
id_area	INT	Sí	Foránea	Areas	Clave foránea que referencia el área de la materia.

sexo:
Campo	Tipo de Dato	No Nulo	Clave	Tabla Relacionada	Descripción
id_sexo	INT	No	Primaria		Identificador único del sexo.
sexo	VARCHAR(10)	Sí			Tipo de sexo (Masculino, Femenino, etc.).

seccion:
Campo	Tipo de Dato	No Nulo	Clave	Tabla Relacionada	Descripción
id_seccion	INT	No	Primaria		Identificador único de la sección.
seccion	VARCHAR(10)	Sí			Nombre o código de la sección.
id_grado	INT	Sí	Foránea	Grados	Clave foránea que referencia el grado de la sección.

grado:
Campo	Tipo de Dato	No Nulo	Clave	Tabla Relacionada	Descripción
id_grado	INT	No	Primaria		Identificador único del grado.
grado	VARCHAR(10)	Sí			Nombre o código del grado.

nacionalidad:
Campo	Tipo de Dato	No Nulo	Clave	Tabla Relacionada	Descripción
id_nacionalidad	INT	No	Primaria		Identificador único de la nacionalidad.
nacionalidad	VARCHAR(50)	Sí			Nombre o código de la nacionalidad.

discapacidades:
Campo	Tipo de Dato	No Nulo	Clave	Tabla Relacionada	Descripción
id_discapacidad	INT	No	Primaria		Identificador único de la discapacidad.
discapacidad	VARCHAR(50)	Sí			Nombre o código de la discapacidad.

matriculas:
Campo	Tipo de Dato	No Nulo	Clave	Tabla Relacionada	Descripción
id_numero_hoja	INT	No	Primaria		Identificador único del número de hoja.
fecha_matricula	DATE	Sí			Fecha de matrícula del estudiante.
codigo_centro_escolar_procedente	VARCHAR(20)	Sí			Código del centro escolar procedente.
codigo_unico_instituto	VARCHAR(20)	Sí			Código único del instituto.
nombre_instituto	VARCHAR(100)	Sí			Nombre del instituto.
id_anio_activo	INT	Sí	Foránea	Años Activos	Clave foránea que referencia el año activo.
id_estudiante	INT	Sí	Foránea	Estudiantes	Clave foránea que referencia el estudiante.
id_modalidad	INT	Sí	Foránea	Modalidades	Clave foránea que referencia la modalidad.
id_repitente	INT	Sí	Foránea	Repitentes	Clave foránea que referencia si es repitente o no.


modalidad:
Campo	Tipo de Dato	No Nulo	Clave	Tabla Relacionada	Descripción
id_modalidad	INT	No	Primaria		Identificador único de la modalidad.
modalidad	VARCHAR(50)	Sí			Nombre o código de la modalidad.

anioactivo:
Campo	Tipo de Dato	No Nulo	Clave	Tabla Relacionada	Descripción
id_anio_activo	INT	No	Primaria		Identificador único del año activo.
anio_activo	VARCHAR(4)	Sí			Año activo escolar (por ejemplo, "2024").

repitentes:
id_repitente	INT	No	Primaria		Identificador único del repitente.
repitente	VARCHAR(50)	Sí			Descripción del repitente.

representantes - Entidad Debil:
id_estudiante	INT	Sí	Clave Foránea	Estudiantes	Identificador único del estudiante
id_representante	INT	Sí	Clave Parcial		Identificador único del representante, parte de la clave primaria compuesta
nombre_madre	VARCHAR(50)	No			Primer nombre de la madre del estudiante
apellido_madre	VARCHAR(50)	No			Apellido de la madre del estudiante
cedula_identidad_madre	VARCHAR(20)	No			Cédula de identidad de la madre
telefono_madre	VARCHAR(15)	No			Teléfono de la madre
nombre_padre	VARCHAR(50)	No			Primer nombre del padre del estudiante
apellido_padre	VARCHAR(50)	No			Apellido del padre del estudiante
cedula_identidad_padre	VARCHAR(20)	No			Cédula de identidad del padre
telefono_padre	VARCHAR(15)	No			Teléfono del padre
nombre_representante	VARCHAR(50)	No			Primer nombre del representante
apellido_representante	VARCHAR(50)	No			Apellido del representante
telefono_representante	VARCHAR(15)	No			Teléfono del representante

departamentos:
id_departamento	INT	No	Primaria		Identificador único del departamento.
departamento	VARCHAR(50)	Sí			Nombre o código del departamento.

usuarios:
Campo	Tipo de Dato	No Nulo	Clave	Tabla Relacionada	Descripción
id_usuario	INT	No	Primaria		Identificador único del usuario.
usuario	VARCHAR(50)	Sí			Nombre de usuario para inicio de sesión.
contrasena	VARCHAR(50)	Sí			Contraseña del usuario.
correo	VARCHAR(50)	Sí	Única		Correo electrónico del usuario (debe ser único).
ultima_sesion	DATETIME	Sí			Fecha y hora de la última sesión del usuario.
id_tipo_usuario	INT	Sí	Foránea	Tipos de Usuarios	Clave foránea que referencia el tipo de usuario.

tipos_usuarios:
Campo	Tipo de Dato	No Nulo	Clave	Tabla Relacionada	Descripción
id_tipo_usuario	INT	No	Primaria		Identificador único del tipo de usuario.
tipo	VARCHAR(50)	Sí			Nombre o código del tipo de usuario.

materias_estudiantes:
Campo	Tipo de Dato	No Nulo	Clave	Tabla Relacionada	Descripción
id_materia	INT	Sí	Foránea	Materia	Clave foránea que referencia la materia.
id_estudiante	INT	Sí	Foránea	Estudiante	Clave foránea que referencia al estudiante.

docentes_estudiantes:
Campo	Tipo de Dato	No Nulo	Clave	Tabla Relacionada	Descripción
id_docente	INT	Sí	Foránea	Docentes	Clave foránea que referencia al docente.
id_estudiante	INT	Sí	Foránea	Estudiantes	Clave foránea que referencia al estudiante.

grado_turno:
Campo	Tipo de Dato	No Nulo	Clave	Tabla Relacionada	Descripción
id_grado	INT	Sí	Foránea	Grados	Clave foránea que referencia el grado.
id_turno	INT	Sí	Foránea	Turnos	Clave foránea que referencia el turno.

area:
Campo	Tipo de Dato (Tamaño)	No Nulo	Clave	Tabla Relación	Descripción
id_area	INT	Sí	Primaria		Identificador único del área
area	VARCHAR(50)	Sí			Nombre del área

municipio:
Campo	Tipo de Dato (Tamaño)	No Nulo	Clave	Tabla Relación	Descripción
id_municipio	INT	Sí	Primaria		Identificador único del municipio
municipio	VARCHAR(50)	Sí			Nombre del municipio

turno:
Campo	Tipo de Dato (Tamaño)	No Nulo	Clave	Tabla Relación	Descripción
id_turno	INT	Sí	Primaria		Identificador único del turno
turno	VARCHAR(10)	Sí			Nombre del turno