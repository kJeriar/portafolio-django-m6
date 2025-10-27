# Desglose Ejercicio
Instrucciones
En función de tu proyecto personal previamente establecido, deberás implementar clase a clase las diferentes tecnologías y competencias técnicas adquiridas a lo largo del curso.

Recuerda que este proyecto irá directamente al registro de evidencia de tu portafolio, el cual deberá demostrar el dominio, competencias técnicas y diferentes habilidades relacionadas con el desarrollo de aplicaciones web utilizando el framework Django.

Requerimientos Funcionales Mínimos Esperados

Describir las características fundamentales del framework Django para el desarrollo de aplicaciones empresariales acorde al entorno Python.
Realizar una investigación sobre las principales características de Django, sus ventajas para el desarrollo de aplicaciones empresariales y cómo facilita el desarrollo rápido y escalable en el entorno Python.
Ejemplo: Comparación de Django con otros frameworks para aplicaciones empresariales.
Utilizar las herramientas administrativas provistas por el framework para la configuración de un nuevo proyecto web Django.
Configurar un nuevo proyecto web en Django utilizando las herramientas de administración del framework, como django-admin startproject y django-admin startapp.
Ejemplo: Creación de un proyecto básico y configuración de su estructura.
Implementar una aplicación web Django utilizando templates para el despliegue de páginas con contenido dinámico que dan solución a un requerimiento.
Diseñar una interfaz web dinámica utilizando los sistemas de plantillas de Django para mostrar información proveniente de una base de datos.
Ejemplo: Crear una página que muestre una lista de productos o usuarios, con datos provenientes de un modelo de base de datos.
Implementar formularios en un aplicativo web utilizando el framework Django para la captura y procesamiento de información dando solución a un problema.
Crear formularios web utilizando los formularios de Django para recibir datos del usuario, validarlos y almacenarlos en la base de datos.
Ejemplo: Implementar un formulario para registrar nuevos usuarios o productos en una aplicación.
Implementar mecanismos de autenticación y autorización para el establecimiento de controles de seguridad utilizando el framework Django.
Configurar el sistema de autenticación de Django para permitir la creación de usuarios, inicio de sesión, y control de accesos en la aplicación.
Ejemplo: Restringir el acceso a ciertas vistas o páginas según el rol del usuario (administrador, usuario regular, etc.).
Implementar módulo de administración de usuarios y permisos utilizando el módulo preconstruido provisto por el framework Django.
Configurar y personalizar el módulo de administración de Django para gestionar usuarios, roles y permisos dentro de la aplicación web.
Ejemplo: Crear una vista de administración que permita gestionar los permisos de usuarios, sus datos y otros aspectos de la seguridad.
Entrega

Repositorio en GitHub:
Subir todos los proyectos y configuraciones relacionadas con el desarrollo de la aplicación web utilizando Django.
Mantener un historial de cambios mediante commits con mensajes descriptivos.
Incluir un archivo README.md que explique la estructura y funcionamiento de la aplicación desarrollada.


**************************************
En este proyecto se construyó una aplicación Django sencilla que muestra un portafolio de proyectos personales sin necesidad de base de datos. Se definió una clase Proyecto y una lista estática como fuente de datos para simular la lógica del modelo. Desde las vistas, se renderizan los proyectos en una página principal y se muestra su detalle identificándolos por su título. Se implementó una estructura limpia basada en el patrón MVC, con rutas (urls.py), vistas (views.py) y plantillas (templates/) separadas. Además, se creó un archivo base.html con Bootstrap 5 integrado por CDN y un archivo styles.css para personalizar colores y tipografía, permitiendo un diseño moderno y responsiva. El resultado final es una web funcional, modular.