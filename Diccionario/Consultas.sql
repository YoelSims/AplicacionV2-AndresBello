Informacion del Estudiante
SELECT 
    e.codigo_estudiante, e.primer_nombre, e.primer_apellido, 
    d.tipo_discapacidad, n.origen_nacionalidad, t.nombre_turno, 
    g.nombre_grado, s.nombre_seccion
FROM 
    estudiante e
JOIN 
    discapacidad d ON e.discapacidad = d.id_discapacidad
JOIN 
    nacionalidad n ON e.nacionalidad = n.id_nacionalidad
JOIN 
    turno t ON e.turno = t.id_turno
JOIN 
    grado g ON e.grado = g.id_grado
JOIN 
    seccion s ON e.seccion = s.id_seccion;


Docente y su Departamento
SELECT 
    d.primer_nombre_docente, d.primer_apellido_docente, 
    d.correo_docente, dept.nombre_departamento
FROM 
    docente d
JOIN 
    departamento dept ON d.departamento = dept.id_departamento;

Materia y su Departamento
SELECT 
    m.materia, dept.nombre_departamento
FROM 
    materia m
JOIN 
    departamento dept ON m.departamento = dept.id_departamento;

Estudiante con su Nota
SELECT 
    e.codigo_estudiante, e.primer_nombre, e.primer_apellido, 
    m.materia, n.nota_final
FROM 
    nota n
JOIN 
    estudiante e ON n.estudiante = e.id_estudiante
JOIN 
    materia m ON n.materia = m.id_materia;

Estudiante y su Clase
SELECT 
    e.codigo_estudiante, e.primer_nombre, d.primer_nombre_docente, 
    a.estado_asistencia, m.materia, h.hora_inicio, s.tipo_salon
FROM 
    clase c
JOIN 
    estudiante e ON c.id_estudiante = e.id_estudiante
JOIN 
    docente d ON c.id_docente = d.id_docente
JOIN 
    asistencia a ON c.id_asistencia = a.id_asistencia
JOIN 
    materia m ON c.id_materia = m.id_materia
JOIN 
    horario h ON c.id_horario = h.id_horario
JOIN 
    salon s ON c.id_salon = s.id_salon;

Matricula del Estudiante
SELECT 
    m.codigo_matricula, m.fecha_matricula, 
    e.codigo_estudiante, e.primer_nombre, 
    mo.nombre_modalidad
FROM 
    matricula m
JOIN 
    estudiante e ON m.estudiante = e.id_estudiante
JOIN 
    modalidad mo ON m.modalidad = mo.id_modalidad;

Representante Informacion
SELECT 
    r.nombre_representante, r.apellido_representante, 
    r.cedula_representante, e.codigo_estudiante, 
    e.primer_nombre, e.segundo_nombre, e.telefono_estudiante
FROM 
    representante r
JOIN 
    estudiante e ON r.id_estudiante = e.id_estudiante;

Estudiantes y su Direccion
SELECT 
    e.codigo_estudiante, e.primer_nombre, e.primer_apellido, 
    dir.avenida, dir.calle, dir.edificio, 
    dir.piso, dir.apto, dir.parroquia, dir.municipio
FROM 
    estudiante e
JOIN 
    direccion dir ON e.direccion = dir.id_direccion;

Estudiantes Escritos Materias
SELECT 
    m.materia, 
    COUNT(me.id_estudiante) AS num_estudiantes
FROM 
    materia m
JOIN 
    materias_estudiante me ON m.id_materia = me.id_materia
GROUP BY 
    m.materia;

Asistencia de Estudiantes
SELECT 
    e.codigo_estudiante, e.primer_nombre, e.primer_apellido, 
    a.estado_asistencia, 
    m.materia, 
    h.hora_inicio, h.hora_fin, 
    d.nombre_dia
FROM 
    clase c
JOIN 
    estudiante e ON c.id_estudiante = e.id_estudiante
JOIN 
    asistencia a ON c.id_asistencia = a.id_asistencia
JOIN 
    materia m ON c.id_materia = m.id_materia
JOIN 
    horario h ON c.id_horario = h.id_horario
JOIN 
    dia d ON c.id_horario = d.id_dia;




















--Listar todos los estudiantes
SELECT * FROM estudiante;

--Listar todas las notas de un estudiante específico
SELECT * FROM nota WHERE id_estudiante = 1;

--Listar todas las materias
SELECT * FROM materia;

--Listar todos los docentes
SELECT * FROM docente;

--Listar todas las matrículas
SELECT * FROM matricula;

--Obtener todas las notas de un estudiante específico, incluyendo la información de las materias
SELECT nota.*, materia.materia
FROM nota
JOIN materia ON nota.id_materia = materia.id_materia
WHERE nota.id_estudiante = 1;

--Obtener todos los estudiantes de una sección específica
SELECT estudiante.*
FROM estudiante
JOIN seccion ON estudiante.id_seccion = seccion.id_seccion
WHERE seccion.seccion = 'A';

--Obtener todos los docentes de un departamento específico
SELECT docente.*
FROM docente
JOIN departamento ON docente.id_departamento = departamento.id_departamento
WHERE departamento.departamento = 'Matemáticas';

--Obtener el promedio de notas de un estudiante específico
SELECT AVG(nota_final) AS promedio_notas
FROM nota
WHERE id_estudiante = 1;

--Obtener todas las matrículas de un año específico
SELECT matricula.*
FROM matricula
JOIN anioactivo ON matricula.id_anio_activo = anioactivo.id_anio_activo
WHERE anioactivo.anio_activo = 2024;

--Obtener el promedio de notas por materia para un estudiante específico
SELECT materia.materia, AVG(nota.nota_final) AS promedio_notas
FROM nota
JOIN materia ON nota.id_materia = materia.id_materia
WHERE nota.id_estudiante = 1
GROUP BY materia.materia;

--Obtener la lista de estudiantes que tienen una nota final por debajo de 60 en cualquier materia
SELECT estudiante.*
FROM estudiante
JOIN nota ON estudiante.id_estudiante = nota.id_estudiante
WHERE nota.nota_final < 60;

--Obtener la lista de estudiantes junto con el nombre de su representante
SELECT estudiante.*, representante.nombre_representante, representante.apellido_representante
FROM estudiante
JOIN representante ON estudiante.id_estudiante = representante.id_estudiante;

--Obtener la lista de docentes junto con los departamentos a los que pertenecen
SELECT docente.*, departamento.departamento
FROM docente
JOIN departamento ON docente.id_departamento = departamento.id_departamento;

--Obtener la lista de estudiantes con alguna discapacidad
SELECT estudiante.*
FROM estudiante
JOIN discapacidad ON estudiante.id_discapacidad = discapacidad.id_discapacidad;

-- Obtener todos los grados y sus respectivos turnos asociados
SELECT g.grado, t.turno
FROM grado g
JOIN grado_turno gt ON g.id_grado = gt.id_grado
JOIN turno t ON gt.id_turno = t.id_turno;

-- Obtener todas las clases con sus detalles de grados, turnos, horarios, salones y materias
SELECT g.grado AS grado, t.turno AS turno, h.horario, s.salon, s.tipo, m.materia
FROM clase c
JOIN grado g ON c.id_grado = g.id_grado
JOIN turno t ON c.id_turno = t.id_turno
JOIN horario h ON c.id_horario = h.id_horario
JOIN salon s ON c.id_salon = s.id_salon
JOIN materia m ON c.id_materia = m.id_materia;

--Actualizar la dirección de un estudiante
UPDATE estudiante
SET direccion = '456 Calle Nueva'
WHERE id_estudiante = 1;

--Actualizar el número de teléfono de un docente
UPDATE docente
SET telefono = '555-9876'
WHERE id_docente = 1;

--Eliminar un estudiante
DELETE FROM estudiante
WHERE id_estudiante = 2;

--Eliminar una nota
DELETE FROM nota
WHERE id_nota = 1;

--Eliminar una matrícula
DELETE FROM matricula
WHERE id_matricula = 1;

--Insertar un nuevo estudiante
INSERT INTO estudiante (codigo_estudiante, primer_nombre_estudiante, segundo_nombre_estudiante, primer_apellido_estudiante, segundo_apellido_estudiante, direccion, telefono, fecha_nacimiento, cedula_identidad, id_sexo, id_discapacidad, id_nacionalidad, id_turno, id_municipio, id_grado, id_seccion)
VALUES ('2024-001', 'Juan', 'Carlos', 'Pérez', 'Gómez', '123 Calle Falsa', '555-1234', '2005-05-15', '12345678', 1, 1, 1, 1, 1, 1, 1);

--Insertar una nueva nota
INSERT INTO nota (id_estudiante, id_materia, cuantitativa_primer_corte, cuantitativa_segundo_corte, cuantitativa_tercer_corte, nota_final)
VALUES (1, 1, 85, 90, 88, 87.66);

--Insertar un nuevo docente
INSERT INTO docente (primer_nombre_docente, segundo_nombre_docente, primer_apellido_docente, segundo_apellido_docente, fecha_nacimiento, cedula_docente, id_sexo, telefono, id_departamento)
VALUES ('María', 'José', 'López', 'Martínez', '1980-10-25', '87654321', 2, '555-4321', 1);

--Insertar una nueva matrícula
INSERT INTO matricula (fecha_matricula, codigo_centro_escolar_procedente, codigo_unico_instituto, nombre_instituto, id_anio_activo, id_estudiante, id_modalidad, id_repitente)
VALUES ('2024-01-10', 'CS-2024', 'IN-2024', 'Instituto Nacional', 1, 1, 1, 1);

--Insertar un nuevo departamento
INSERT INTO departamento (departamento)
VALUES ('Ciencias Sociales');

