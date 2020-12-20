## 09/12/2020

21 Decoradores @constrains 
23 Actions
24 Manejo de Errores 
25 Defaults

- Añadir una restricción para hacer que el campo time no sea menor que 0
- Añadir un onchange para que al indicar la fecha ponga como fecha de vencimiento un día mas
- Modificar el botón de crear una etiqueta en el formulario de ticket para que abra una acción nueva, pasando por contexto el valor del nombre y la relación con el ticket.
- hacer una función para asignar el ticket por defecto al usuario que lo crea.
- hacer un cron que borre los tags que no estén asingnados a ningúnt ticket, que se ejecute una vez al día

## 09/12/2020

26 Campos Avanzados 
37 Wizards

- Crear un asistente para crear tickets desde la etiqueta
  - que coja por contexto el active_id para que el ticket creado tenga asociada la etiqueta desde la que se lanza el asistente
  - crear el boton en el formulario de la etiqueta
  - después de crear el ticket redirigir al formulario con el ticket creado
- Hacer que el campo tiempo dedicado sea calculado, en base al tiempo dedicado en cada acción, y hacer el inverse para que cree una acción cuando se escrive el tiempo dedicado.
- Modificar el search del campo computed.

