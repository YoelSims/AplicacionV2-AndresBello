--Restricciones/Limitaciones/Consideraciones

--Restricciones
Como producto del análisis de requerimientos funcionales y no funcionales, se delimitaron las siguientes restricciones para el sistema de gestión escolar:

Alcance Funcional:
El sistema solo se ocupa de los procesos de matrícula, registro de calificaciones, gestión de estudiantes, docentes y representantes.
No se incluyen funcionalidades relacionadas con la gestión de inventarios escolares, control de acceso físico a las instalaciones ni administración financiera.

Tecnología:
La aplicación se desarrollará utilizando el lenguaje de programación Python en conjunto con el framework PyQt o Tkinter para la interfaz de usuario.
El gestor de base de datos será PostgreSQL.
No se considera la integración con sistemas basados en la web o aplicaciones móviles.

Entorno de Ejecución:
El sistema será exclusivamente una aplicación de escritorio y no será accesible desde navegadores web.
El sistema deberá ejecutarse en entornos Windows, macOS y Linux.

Interacción con Otros Sistemas:
El sistema no tiene opción de interactuar con otros sistemas externos, ya que está diseñado para trabajar de manera independiente.
Cualquier integración con otros sistemas requerirá un proceso adicional de desarrollo y aprobación.

Disponibilidad y Uso:
El sistema estará disponible para su uso durante el horario escolar, y cualquier mantenimiento o actualización se programará fuera de las horas de uso.
Los datos se deben ingresar de manera correcta para que el sistema funcione adecuadamente.

--Limitaciones:
--Factores que pueden afectar los requerimientos del sistema:

Requisitos de Hardware y Software:
Los equipos donde se ejecute la aplicación deben cumplir con los requisitos mínimos de hardware y software especificados, incluyendo:
Procesador de al menos 2.0 GHz.
4 GB de RAM (8 GB recomendados).
500 MB de espacio disponible en disco.
Python 3.7 o superior.
La base de datos PostgreSQL debe estar correctamente configurada y accesible desde las estaciones de trabajo.

Capacitación de Usuarios:
Los usuarios deben recibir la capacitación adecuada para usar el sistema eficientemente.
Los usuarios deben estar familiarizados con el uso básico de computadoras y aplicaciones de escritorio.

Acceso a Internet:
Aunque el sistema es de escritorio, es necesario acceso a internet para ciertas funcionalidades, como actualizaciones del sistema y respaldo de datos.
El sistema debe estar conectado a la red de la institución educativa para sincronizar y acceder a la base de datos centralizada.

Respaldo y Recuperación de Datos:
Se deben implementar políticas de respaldo y recuperación de datos para asegurar la integridad y disponibilidad de la información.
Se realizarán respaldos diarios de la base de datos, y se almacenarán en ubicaciones seguras

Mantenimiento y Soporte:
Un equipo de soporte técnico debe estar disponible para resolver cualquier problema técnico que surja.

El sistema debe estar sujeto a un plan de mantenimiento regular para asegurar su correcto funcionamiento y actualizarlo según sea necesario.

--Consideraciones:

Acceso y Autenticación:
El acceso al sistema estará restringido mediante autenticación con nombre de usuario y contraseña.
Diferentes niveles de acceso serán asignados según el rol del usuario (administradores, docentes, personal administrativo).

Protección de Datos:
La información sensible, como datos personales de estudiantes y docentes, debe ser protegida mediante encriptación.
Solo personal autorizado debe tener acceso a los datos confidenciales.

Regulación y Cumplimiento:
El sistema debe cumplir con las leyes y regulaciones locales de protección de datos y privacidad.
Se deben mantener registros de acceso y cambios en la base de datos para auditoría y seguimiento.