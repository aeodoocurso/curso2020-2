28 Herencia de modelos
29 Herencia de vistas
30 Herencia de métodos
31 Herencia por delegacion

- Crear nuevo módulo sale_helpdesk_xxx
  - añadir un listado de tickets en el pedido de venta.
  - añádir el campo etiqueta de helpdesk en el producto y poner un botón que cree ticket desde pedidos con las etiquetas de los productos del pedido.
  - hacer que al cancelar un pedido se cancelen todos los tickets asociados. (Volver a poner el campo state como un selection)

- Crear un nuevo módulo crm_helpdesk_xxx
  Será otra alternativa al primero que hemos hecho, utilizaremos toda la funcionalidad de los leads.

  Crearemos un nuevo modelo crm.lead.ticket con herencia por delegación utilizando como base el lead y añadiendo los campos acciones correctivas y preventivas.


34
36
38
35
