## 30/11/2020

- [14] Campos Calculados
- [15] Campos Relacionales
- [16] Decorador @api.depends
- [18] Metodos ORM

Tareas a realizar:
- crear un o2m en helpdesk.ticket apuntando a un nuevo modelo helpdesk.ticket.action que tenga un campo name y un campo date.
- crear un campo helpdesk.tag y añadir un m2m de etiquetas en el ticket.
- añadir un m2m en helpdesk.tag para ver todas las tareas relacionadas con cada tag.
- Hacer que el campo assigned sea calculado.
- hacer un campo calculado que indique, dentro de un ticket, la cantidad de tiquets asociados al mismo ususario.
- crear un campo nombre de etiqueta, y hacer un botón que cree la nueva etiqueta con ese nombre y lo asocie al ticket.

## 01/12/2020

- [17] Vista search
- [19] Kanban
- [20] Pivot, Graph y Calendar
- [22] Domains


Tareas a realizar:
- Añadir vista search:
  - filtrar por nombre y por usuario asignado
  - filtrar tickets asignados
  - filtrar tickets sin date_due
  - agrupar por date_due
  - agrupar por usuario asignado
- Vista pivot:
  - añadir vista pivot a la acción.
  - mostrar tiempo dedicado por usuario / mes
- Vista graph:
  - añadir vista pivot a la acción.
  - mostrar tiempo dedicado por usuario
- Vista calendar:
  - por fecha mostrando cada usuarioa asignado.
- Vista kanban:
  - mostrar en tarjeta usuario y tiempo dedicado
  - agrupar por usuario
  - extra: añadir un field color, para cambiar el color de la tarjeta, ver como está hecho en crm.lead

## 02/12/2020

- [33] Opciones avanzadas en vistas
- [13] Debug

Tareas a realizar:
- En el ticket tenemos un campo action_ids, y no tenemos definida una vista para el modelo al que apunta, crear una vista embevida, y vamos a ocultar el m2o en el formulario que aputna al o2m en el inverse_name.
- Las etiquetas tienen unas vistas que muestran el m2m a los tickets, hacer otra vista sin este m2m y hacer que desde el ticket se muestre la segunda vista.
- Hacer que el tag_ids no pueda crear nuevos tag_ids
