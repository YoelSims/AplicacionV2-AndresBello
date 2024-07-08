-- Precarga de datos

--nacionalidad
INSERT INTO nacionalidad (origen_nacionalidad) VALUES ('Venezolana'), ('Colombiana'), ('Argentina');

--discapacidades
INSERT INTO discapacidad (tipo_discapacidad) VALUES ('Visual'), ('Auditiva'), ('Motriz');

--turno
INSERT INTO turno (nombre_turno) VALUES ('Mañana'), ('Tarde'), ('Noche');

--grados
INSERT INTO grado (nombre_grado) VALUES ('Primero'), ('Segundo'), ('Tercero');

--secciones
INSERT INTO seccion (nombre_seccion) VALUES ('A'), ('B'), ('C');

--departamentos
INSERT INTO departamento (nombre_departamento) VALUES ('Ciencias'), ('Humanidades'), ('Artes');

--modalidades
INSERT INTO modalidad (nombre_modalidad) VALUES ('Regular'), ('Intensiva'), ('Semi-presencial');

--anos_activos
INSERT INTO anios_activo (anio_activo) VALUES ('2024'), ('2025'), ('2026');

--dias
INSERT INTO dia (nombre_dia) VALUES ('Lunes'), ('Martes'), ('Miércoles'), ('Jueves'), ('Viernes');

--horario
INSERT INTO horario (hora_inicio, hora_fin) VALUES ('08:00:00', '09:00:00'), ('09:00:00', '10:00:00'), ('10:00:00', '11:00:00');

--salon
INSERT INTO salon (tipo_salon, capacidad, ubicacion) VALUES ('Aula', 30, 'Edificio A'), ('Laboratorio', 20, 'Edificio B'), ('Auditorio', 100, 'Edificio C');

--asistencia
INSERT INTO asistencia (estado_asistencia) VALUES ('Presente'), ('Ausente'), ('Justificado');

--tipos_usuarios
INSERT INTO tipo_usuarios (tipo_usuario) VALUES ('Admin'), ('Docente'), ('Estudiante');

--usuarios
INSERT INTO usuario (usuario, contrasena, correo, ultima_sesion, tipo_usuario) VALUES 
('admin', 'admin123', 'admin@andresbello.edu', NOW(), 1),
('docente1', 'docente123', 'docente1@andresbello.edu', NOW(), 2),
('estudiante1', 'estudiante123', 'estudiante1@andresbello.edu', NOW(), 3);

--direccion
INSERT INTO direccion (avenida, calle, edificio, piso, apto, parroquia, municipio) VALUES
('Av. Principal', 'Calle 1', 'Edificio A', 'Piso 1', 'Apto 1', 'Parroquia 1', 'Municipio 1'),
('Av. Secundaria', 'Calle 2', 'Edificio B', 'Piso 2', 'Apto 2', 'Parroquia 2', 'Municipio 2');

--estudiantes
INSERT INTO estudiante (codigo_estudiante, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, telefono_estudiante, correo_estudiante, fecha_nacimiento, cedula_identidad, sexo, discapacidad, nacionalidad, turno, direccion, grado, seccion) VALUES
('E001', 'Juan', 'Carlos', 'Perez', 'Gomez', '04121234567', 'juan.perez@andresbello.edu', '2005-06-15', 'V12345678', 'M', 1, 1, 1, 1, 1, 1),
('E002', 'Maria', 'Jose', 'Martinez', 'Lopez', '04261234567', 'maria.martinez@andresbello.edu', '2006-08-22', 'V87654321', 'F', 2, 2, 2, 2, 2, 2);

--docentes
INSERT INTO docente (primer_nombre_docente, segundo_nombre_docente, primer_apellido_docente, segundo_apellido_docente, fecha_nacimiento, cedula_docente, sexo, correo_docente, telefono_docente, direccion_docente, departamento) VALUES
('Ana', 'Maria', 'Rodriguez', 'Fernandez', '1980-05-10', 'D12345678', 'F', 'ana.rodriguez@andresbello.edu', '04141234567', 'Calle 3, Edificio C, Piso 3, Apto 3', 1),
('Pedro', 'Luis', 'Gomez', 'Ramirez', '1975-11-20', 'D87654321', 'M', 'pedro.gomez@andresbello.edu', '04241234567', 'Calle 4, Edificio D, Piso 4, Apto 4', 2);

--materias
INSERT INTO materia (materia, departamento) VALUES
('Matemáticas', 1),
('Historia', 2),
('Dibujo', 3);

--notas
INSERT INTO nota (cualitativa_primer_corte, cuantitativa_primer_corte, cualitativa_segundo_corte, cuantitativa_segundo_corte, cualitativa_tercer_corte, cuantitativa_tercer_corte, nota_final, estudiante, materia) VALUES
('Bueno', 85, 'Muy Bueno', 90, 'Excelente', 95, 90, 1, 1),
('Regular', 70, 'Bueno', 75, 'Muy Bueno', 80, 75, 2, 2);

--representantes
INSERT INTO representante (nombre_representante, apellido_representante, cedula_representante, telefono_representante, correo_representante, parentesco, id_estudiante) VALUES
('Luis', 'Perez', 'R12345678', '04161234567', 'luis.perez@andresbello.edu', 'Padre', 1),
('Carmen', 'Martinez', 'R87654321', '04261234567', 'carmen.martinez@andresbello.edu', 'Madre', 2);

--matriculas
INSERT INTO matricula (codigo_matricula, fecha_matricula, codigo_centro_escolar_procedente, codigo_unico_instituto, nombre_instituto, anio_activo, estudiante, modalidad) VALUES
('M001', '2024-01-15', 'CE001', 'CU001', 'Instituto ABC', 1, 1, 1),
('M002', '2024-01-16', 'CE002', 'CU002', 'Instituto DEF', 2, 2, 2);

--materias_estudiantes
INSERT INTO materias_estudiante (id_materia, id_estudiante) VALUES
(1, 1),
(2, 2);

--grado_turno
INSERT INTO grado_turno (id_grado, id_turno) VALUES
(1, 1),
(2, 2);

--clase
INSERT INTO clase (id_estudiante, id_docente, id_asistencia, id_materia, id_horario, id_salon) VALUES
(1, 1, 1, 1, 1, 1),
(2, 2, 2, 2, 2, 2);
