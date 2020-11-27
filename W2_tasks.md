# Tareas para la semana 23 Noviembre

Cada alumno creará un módulo helpdesk con su nombre, por ejemplo yo crearé el módulo "helpdesk_angelmoya".

Todos trabajaremos en el mismo repositorio, pero cada uno en su módulo en su fork.

## Creación de modelo, seguridad y menu.

Lo primero que haremos será crear el modelo helpdesk.ticket, con los campos:
- Nombre
- Descripción
- Fecha

Hacer dos grupos de usuario, helpdesk_manager y helpdesk_user

Hacer el menú Helpesk/Helpdesk/Tickets


## Mejorar la vista de formulario y listado y añadir campos.

Añadir los siguiente campos:

    Estado [Nuevo, Asignado, En proceso, Pendiente, Resuelto, Cancelado], que por defecto sea Nuevo
    Tiempo dedicado (en horas)
    Asignado (tipo check)
    Fecha límite
    Acción correctiva (html)
    Acción preventiva (html)

-- El campo nombre que sea obligatorio

En algún campo añadir un texto de ayuda indicando su funcionalidad, luego revisar que funciona.

El campo Asignado:

--    hacer que sea solo de lectura

--El campo nombre hacer que sea obligatorio.

En la vista tipo lista mostrar:

    nombre, fecha, estado

En la vista formulario:

    poner un header con el status bar
    nombre con h1 como en pedido de venta
    dos columnas:
        fecha, fecha límite
        asignado, tiempo dedicado
    solapas:
        Descripción
        Calidad
            Acción correctiva
            Acción preventiva


## Añadir método y traducir.
