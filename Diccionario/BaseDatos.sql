CREATE DATABASE andresbello;
USE andresbello;

CREATE TABLE turno (
    id_turno INT AUTO_INCREMENT PRIMARY KEY,
    nombre_turno VARCHAR(50) NOT NULL
)ENGINE=InnoDB;

CREATE TABLE seccion (
    id_seccion INT AUTO_INCREMENT PRIMARY KEY,
    nombre_seccion VARCHAR(50) NOT NULL
)ENGINE=InnoDB;

CREATE TABLE grado (
    id_grado INT AUTO_INCREMENT PRIMARY KEY,
    nombre_grado VARCHAR(50) NOT NULL
)ENGINE=InnoDB;

CREATE TABLE nacionalidad (
    id_nacionalidad INT AUTO_INCREMENT PRIMARY KEY,
    origen_nacionalidad VARCHAR(50) NOT NULL
)ENGINE=InnoDB;

CREATE TABLE discapacidad (
    id_discapacidad INT AUTO_INCREMENT PRIMARY KEY,
    tipo_discapacidad VARCHAR(50) NOT NULL
)ENGINE=InnoDB;

CREATE TABLE modalidad (
    id_modalidad INT AUTO_INCREMENT PRIMARY KEY,
    nombre_modalidad VARCHAR(50) NOT NULL
)ENGINE=InnoDB;

CREATE TABLE anio_activo (
    id_anio_activo INT AUTO_INCREMENT PRIMARY KEY,
    anio_activo VARCHAR(4) NOT NULL
)ENGINE=InnoDB;

CREATE TABLE dia (
    id_dia INT AUTO_INCREMENT PRIMARY KEY,
    nombre_dia VARCHAR(50) NOT NULL
)ENGINE=InnoDB;

CREATE TABLE horario (
    id_horario INT AUTO_INCREMENT PRIMARY KEY,
    hora_inicio TIME,
    hora_fin TIME
)ENGINE=InnoDB;

CREATE TABLE salon (
    id_salon INT AUTO_INCREMENT PRIMARY KEY,
    tipo_salon VARCHAR(50) NOT NULL,
    capacidad INT,
    ubicacion VARCHAR(100)
)ENGINE=InnoDB;

CREATE TABLE asistencia (
    id_asistencia INT AUTO_INCREMENT PRIMARY KEY,
    estado_asistencia VARCHAR(50) NOT NULL
)ENGINE=InnoDB;

CREATE TABLE departamento (
    id_departamento INT AUTO_INCREMENT PRIMARY KEY,
    nombre_departamento VARCHAR(50) NOT NULL
)ENGINE=InnoDB;

CREATE TABLE tipo_usuario (
    id_tipo_usuario INT AUTO_INCREMENT PRIMARY KEY,
    tipo_usuario VARCHAR(50) NOT NULL
)ENGINE=InnoDB;

CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL,
    contrasena VARCHAR(50) NOT NULL,
    correo VARCHAR(50),
    ultima_sesion DATETIME,
    tipo_usuario INT,
    FOREIGN KEY (tipo_usuario) REFERENCES tipos_usuario(id_tipo_usuario)
)ENGINE=InnoDB;

CREATE TABLE docente (
    id_docente INT AUTO_INCREMENT PRIMARY KEY,
    primer_nombre_docente VARCHAR(50) NOT NULL,
    segundo_nombre_docente VARCHAR(50),
    primer_apellido_docente VARCHAR(50) NOT NULL,
    segundo_apellido_docente VARCHAR(50),
    fecha_nacimiento DATE,
    cedula_docente VARCHAR(20) NOT NULL,
    sexo VARCHAR(10),
    correo_docente VARCHAR(50) NOT NULL,
    telefono_docente VARCHAR(15),
    direccion_docente VARCHAR(100),
    departamento INT,
    FOREIGN KEY (departamento) REFERENCES departamento(id_departamento)
)ENGINE=InnoDB;

CREATE TABLE materia (
    id_materia INT AUTO_INCREMENT PRIMARY KEY,
    materia VARCHAR(50) NOT NULL,
    departamento INT,
    FOREIGN KEY (departamento) REFERENCES departamento(id_departamento)
)ENGINE=InnoDB;

CREATE TABLE direccion (
    id_direccion INT AUTO_INCREMENT PRIMARY KEY,
    avenida VARCHAR(50),
    calle VARCHAR(50),
    edificio VARCHAR(50),
    piso VARCHAR(10),
    apto VARCHAR(10),
    parroquia VARCHAR(50),
    municipio VARCHAR(50)
)ENGINE=InnoDB;

CREATE TABLE estudiante (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    codigo_estudiante VARCHAR(10) NOT NULL,
    primer_nombre VARCHAR(50) NOT NULL,
    segundo_nombre VARCHAR(50),
    primer_apellido VARCHAR(50) NOT NULL,
    segundo_apellido VARCHAR(50),
    telefono_estudiante VARCHAR(15),
    correo_estudiante VARCHAR(50) NOT NULL,
    fecha_nacimiento DATE,
    cedula_identidad VARCHAR(20) NOT NULL,
    sexo VARCHAR(10),
    discapacidad INT,
    nacionalidad INT,
    turno INT,
    direccion INT,
    grado INT,
    seccion INT,
    FOREIGN KEY (discapacidad) REFERENCES discapacidad(id_discapacidad),
    FOREIGN KEY (nacionalidad) REFERENCES nacionalidad(id_nacionalidad),
    FOREIGN KEY (turno) REFERENCES turno(id_turno),
    FOREIGN KEY (direccion) REFERENCES direccion(id_direccion),
    FOREIGN KEY (grado) REFERENCES grado(id_grado),
    FOREIGN KEY (seccion) REFERENCES seccion(id_seccion)
)ENGINE=InnoDB;

CREATE TABLE representante (
    id_representante INT AUTO_INCREMENT PRIMARY KEY,
    nombre_representante VARCHAR(50) NOT NULL,
    apellido_representante VARCHAR(50) NOT NULL,
    cedula_representante VARCHAR(20) NOT NULL,
    telefono_representante VARCHAR(15),
    correo_representante VARCHAR(50),
    parentesco VARCHAR(50),
    id_estudiante INT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
)ENGINE=InnoDB;

CREATE TABLE matricula (
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    codigo_matricula VARCHAR(20) NOT NULL,
    fecha_matricula DATE NOT NULL,
    codigo_centro_escolar_procedente VARCHAR(20),
    codigo_unico_instituto VARCHAR(20),
    nombre_instituto VARCHAR(100),
    anio_activo INT,
    estudiante INT,
    modalidad INT,
    FOREIGN KEY (anio_activo) REFERENCES anio_activo(id_anio_activo),
    FOREIGN KEY (estudiante) REFERENCES estudiante(id_estudiante),
    FOREIGN KEY (modalidad) REFERENCES modalidad(id_modalidad)
)ENGINE=InnoDB;

CREATE TABLE nota (
    id_nota INT AUTO_INCREMENT PRIMARY KEY,
    cualitativa_primer_corte VARCHAR(50),
    cuantitativa_primer_corte INT,
    cualitativa_segundo_corte VARCHAR(50),
    cuantitativa_segundo_corte INT,
    cualitativa_tercer_corte VARCHAR(50),
    cuantitativa_tercer_corte INT,
    nota_final INT,
    estudiante INT,
    materia INT,
    FOREIGN KEY (estudiante) REFERENCES estudiante(id_estudiante),
    FOREIGN KEY (materia) REFERENCES materia(id_materia)
)ENGINE=InnoDB;

CREATE TABLE materias_estudiante (
    id_materia INT,
    id_estudiante INT,
    PRIMARY KEY (id_materia, id_estudiante),
    FOREIGN KEY (id_materia) REFERENCES materia(id_materia),
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
)ENGINE=InnoDB;

CREATE TABLE grado_turno (
    id_grado INT,
    id_turno INT,
    PRIMARY KEY (id_grado, id_turno),
    FOREIGN KEY (id_grado) REFERENCES grado(id_grado),
    FOREIGN KEY (id_turno) REFERENCES turno(id_turno)
)ENGINE=InnoDB;

CREATE TABLE clase (
    id_clase INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT,
    id_docente INT,
    id_asistencia INT,
    id_materia INT,
    id_horario INT,
    id_salon INT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante),
    FOREIGN KEY (id_docente) REFERENCES docente(id_docente),
    FOREIGN KEY (id_asistencia) REFERENCES asistencia(id_asistencia),
    FOREIGN KEY (id_materia) REFERENCES materia(id_materia),
    FOREIGN KEY (id_horario) REFERENCES horario(id_horario),
    FOREIGN KEY (id_salon) REFERENCES salon(id_salon)
)ENGINE=InnoDB;


--------------------------------------------------------------------------------