# EvaluacionTecnica
Evaluacion tecnica Reyna Madre
__________________________________________________________________________________________________________
Justificacion:
Con el fin de atender los requerimientos del cliente, se desarrollo un proyecto en Django el cual esta destinado a gestionar empleados dependiendo de departamentos pertenecientes a una empresa en especifico.

__________________________________________________________________________________________________________
Tecnologias usadas:
- Django v:3.2.5 (en entorno virtual).- El framework especificamente para realizar este proyecto.
- Python v:3.9.5.- el cual es el lenguaje de programacion en el cual esta orientado Django.
- Sqlite- La base de datos ocupada por el framework, la justificacion de esta herramienta, es que es la herramineta que viene por defecto
- HTML- para los formularios y vistas generadas en el proyecto, recomiendo poder aplicar algunos templates gratuitos ya que no soy muy experto en HTML y CSS
- JS- se utiliza para algunas opciones dinamicas dentro del sistema
- CSS- para los estilos de la pagina, recomiendo usar un template gratuito o reutilizar codigo de otros templates personales

__________________________________________________________________________________________________________
Se realizaron dos tipos de soluciones a este problema, principalmente porque Django como framework ya tiene algunas funciones que ayudan en la realizacion de este proyecto.
---------------------------------------------------------------------------------------------
La primer aplicacion la genere por medio de los comandos que Django ofrece,
- la creacion del poryecto
- creacion de aplicacion (Base de datos)
- Edicion de modelos necesarios (Tablas de la base de datos)
- creacion del superusuario (Principalmente para obtener un dashboard y poder loggear dentro de la aplicacion)

En este dashboard se pueden hacer configuraciones como
- creacion de usuarios (admin global y usuario normal) desde el mismo proyecto, el administrador global crea usuarios y da permisos a esos usuarios
  lo puede hacer por creacion de grupos (en caso de tener muchos usuarios), o por usuario.
- Filtros en tablas
- Cruds de tablas
- Creacion de grupos
- 
Cabe destacar que dentro de las tablas que genera django en este dashboad, se pueden hacer mas configuraciones como:
- Busqueda en tablas
- Filtros en tablas
- Ordenamiento de elementos en la tabla

Una infinidad de cosas si se lee bien la documentacion, Django ya te ofrece todo lo pedido en la evaluacion (Me ayudo de cierta manera porque soy principiante en Django y se que se pueden realizar mas cosas).

--------------------------------------------------------------------------------------------------
- La segunda aplicacion la cree desde 0, viene dentro del mismo dashboard('Clickeando view site')
En esta, de igual manera se usaron los modelos creados para la base de datos.
con python se realizo toda la logica necesaria para
- Listar empleados
- Crear empleados
- Editar empleados
- Buscar empleados por los filtros requeridos
- Eliminar empleados de la base de datos

Se realizaron eventos JS para el el ocultar y mostrar el menu lateral

__________________________________________________________________________________________________________
Logrado:
Se logro crear la aplicacion con los requerimientos necesarios de tener departamentos dentro de empresas y el crud de empleados
La busqueda por los metodos requeridos
la creacion de nuevo empleado con algunos campos requeridos y algunos no
y el loggin

__________________________________________________________________________________________________________
Puntos extras logrados:
La creacion de dos diferentes tipos de usuarios con comandos django
mostrar y ocultar el menu lateral
La creacion de grupos dentro del dashboard de admin


