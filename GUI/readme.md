# Sistema de Gestión de Servicios de Clínica

## Integrantes
1. Bermeo Cevallos Jorge Alejandro.
2. Caceres Medina Bolivar Santiago.
3. Chalen Ochoa Shuska Akyra.
4. Gonzalez Rodríguez Scarlet Anabella.
5. Rivera Valdiviezo Ashley Daniela.
6. Silva Parrales Jipson Alexander.

## Descripción del proyecto

Este proyecto fue desarrollado en Python utilizando PySide6 para la creación de una interfaz gráfica de usuario (GUI). El sistema permite registrar información de pacientes y servicios médicos, incluyendo datos como código del servicio, nombre del servicio, costo base, nombre, apellido, cédula y correo electrónico.

Además, el sistema incorpora validaciones para garantizar que los datos ingresados cumplan con los formatos requeridos antes de ser almacenados.

## Validación implementada

Se implementó una validación de correo electrónico utilizando expresiones regulares (Regex) mediante el módulo `re` de Python. Esta validación verifica que el correo ingresado tenga una estructura válida, compuesta por:

* Un nombre de usuario.
* El símbolo `@`.
* Un dominio.
* Una extensión de dominio válida.

Si el correo no cumple con el formato establecido, el sistema muestra un mensaje de error y evita el registro de la información.

### Patrón utilizado

```python
r"^[\w\.-]+@[\w\.-]+\.\w+$"
```

## Ejemplos de correos válidos

* [usuario@gmail.com](mailto:usuario@gmail.com)
* [nombre.apellido@hotmail.com](mailto:nombre.apellido@hotmail.com)
* [estudiante2026@instituto.edu.ec](mailto:estudiante2026@instituto.edu.ec)
* [cliente_empresa@dominio.com](mailto:cliente_empresa@dominio.com)

## Ejemplos de correos inválidos

* correo.com
* usuario@
* @gmail.com
* usuario@gmail
* usuario gmail.com
* usuario@@gmail.com

## Funcionamiento

1. El usuario ingresa la información solicitada en la interfaz gráfica.
2. El sistema valida los datos ingresados.
3. Se verifica que el correo electrónico tenga un formato correcto.
4. Si el correo es inválido, se muestra un mensaje de error.
5. Si el correo es válido, la información se registra correctamente y se muestra un mensaje de confirmación.
6. Los registros almacenados pueden visualizarse mediante la opción "Mostrar Información".

## Tecnologías utilizadas

* Python
* PySide6
* Expresiones regulares (Regex)
* Qt Designer
* GitHub