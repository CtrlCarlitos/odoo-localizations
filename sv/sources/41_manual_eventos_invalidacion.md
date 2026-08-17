# Manual de eventos de Invalidación y Contingencia para el Sistema de Transmisión DTES

## Control de Versiones

| Versión | Fecha |
| :---: | :---: |
| 1.0 | 01/2022 |
| 1.1 | 05/2022 |

## Control de Cambios

| Detalle Versión | Detalle de Cambios |
| :---: | :--- |
| Versión 1.0 | Versión inicial del documento. |
| Versión 1.1 | Se amplía sobre el uso de campo tipo de invalidación.<br>Se modifica campo 22 en la estructura del evento de invalidación.<br>Se adiciona anexo 1 y 2. |

A continuación se muestra el contenido de la imagen en formato Markdown:

## Contenido

* Introducción .................................................................................................... 1
* Objetivo General ............................................................................................... 2
* Objetivos Específicos .......................................................................................... 2
1.  Manual de Eventos de Invalidación y Contingencia para el Sistema de Transmisión DTE ... 3
2.  Evento de invalidación ........................................................................................ 4
    2.1 Secciones de estructura para el evento de invalidación. .......................................... 4
    2.2 Proceso para transmitir el evento de invalidación. .................................................. 5
    2.3 Plazos para transmitir el evento de invalidación. ..................................................... 6
    2.4 Condiciones especiales. ................................................................................... 7
    2.5 Estructura para transmisión del evento de invalidación. ............................................ 9
3.  Evento de contingencia. ........................................................................................ 15
    3.1 Modelo de recepción para los DTE en generados contingencia. ................................... 15
    3.2 Secciones de la estructura definida por la Administración Tributaria para ingresar evento de contingencia. ........................................................................ 16
    3.3 Proceso para generar DTE "en contingencia" ........................................................... 17
    3.4 Proceso para transmitir documentos electrónicos en contingencia. ................................ 18
    3.5 Estructura para transmisión de evento de contingencia. ............................................. 21
* Acrónimos. ........................................................................................................ 25
* Anexo 1: Pruebas de transmisión satisfactorias mínimas para eventos de invalidación y contingencia en el Sistema Integrado DTE. ................................ 26
* Anexo 2: Condiciones para el envío del evento de invalidación. ......................................... 26

El siguiente es el contenido de la imagen en formato Markdown:

## Introducción

El presente manual describe las especificaciones técnicas para la generación y transmisión de los eventos de invalidación y contingencia para el Sistema de Transmisión DTE, donde se explican los términos, plazos y condiciones establecidos por esta Dirección General, a efecto que el emisor de Documentos Tributarios Electrónicos, los establezca en sus sistemas y los integre a sus procedimientos administrativos y operativos, de manera que una vez implementados los eventos puedan transmitirse sin inconvenientes.

Con la implementación de estos términos, plazos y condiciones en cada uno de los eventos, se establece el procedimiento a seguir cuando el emisor se encuentre en la necesidad de corregir los documentos tributarios electrónicos a los cuales la Administración Tributaria ya les ha otorgado el respectivo sello de recepción o cuando el contribuyente ante una situación imprevista que le impida realizar la transmisión de los documentos tributarios pueda continuar su operatividad.

En este manual también se encuentran detalladas las estructuras que contienen los campos con sus respectivas descripciones referente a la información requerida, asimismo se describe la condición, el tipo de dato en el que debe ser ingresada la información, su longitud y su respectivo nombre Json para programación.

## Objetivo General

Presentar a los contribuyentes de forma descriptiva, los lineamientos establecidos por la Administración Tributaria en el marco de la gestión de Documentos Tributarios Electrónicos la aplicación de los eventos de invalidación y contingencia para el Sistema de Transmisión DTE.

## Objetivos Específicos

1. Dar a conocer la información requerida en la estructura establecida por la Administración Tributaria para la generación de los eventos de invalidación y contingencia.
2. Explicar los procedimientos que el contribuyente debe realizar cuando surja la necesidad de aplicar dichos eventos, para hacer más eficiente los procesos de generación y transmisión, así como garantizar la recepción efectiva por parte de la Administración Tributaria.
3. Señalar los plazos y condiciones para la transmisión de los documentos electrónicos o documentos tributarios electrónicos según corresponda al tipo de evento a transmitir.

## 1. Manual de Eventos de Invalidación y Contingencia para el Sistema de Transmisión DTE.

Durante la generación, transmisión y recepción de documentos electrónicos, se prevé que pueden ocurrir errores que se identifiquen después de otorgado el sello de recepción por parte de la Administración Tributaria, asimismo, que pudiera darse imprevistos que impidan la transmisión de estos documentos de manera normal hacia la misma.

Los errores en los Documentos Tributarios Electrónicos o la imposibilidad de efectuar su transmisión normal a la Administración Tributaria tienen un efecto significativo en las operaciones cotidianas que los contribuyentes realizan, por tanto, es necesario establecer alternativas que posibiliten a los contribuyentes la continuidad de sus operaciones de una manera transparente y oportuna, lo que a su vez también garantiza generar un mejor ambiente de control dentro de un periodo.

Con la implementación de un evento de invalidación, se busca dar una solución factible, que permita al contribuyente corregir errores dados en los Documentos Tributarios Electrónicos y con el Evento de Contingencia se busca que el contribuyente continúe generando los documentos electrónicos, cuando existan casos de fuerza mayor, que impidan realizar la transmisión de estos a la Administración Tributaria de manera normal para la obtención de su respectivo sello de recepción.

Antes de comenzar a describir los eventos antes planteados es importante aclarar, que si bien, para los eventos establecidos por esta Administración se ha definido las estructuras respectivas y estas deben ser transmitidas en formato Json, estos no se consideran un Documento Tributario Electrónico (DTE) se consideran el medio por el cual el contribuyente informará a la Administración Tributaria que ocurrió un error o que durante un periodo de tiempo no puede realizar su transmisión de manera normal.

Desde el punto vista de la emisión de Documentos Tributarios Electrónicos, un evento se refiere al mensaje de datos firmado electrónicamente que contiene información que se relaciona con un documento tributario electrónico emitido previamente, que afecta o modifica dicho documento electrónico.

Para poder hacer uso de los eventos, el contribuyente deberá realizar previamente la adecuación de dichos eventos en sus sistemas de facturación internos de acuerdo a los requerimientos de las estructuras proporcionadas y las condiciones establecidas en este manual. Una vez se hayan realizado las adecuaciones necesarias de los sistemas, deberá realizar el proceso de pruebas para cada uno de los eventos por medio del Sistema de Transmisión de DTE con respuesta exitosa, es decir que se les otorgó el sello de recepción.

Las pruebas de dichos eventos serán consideradas al momento de realizar las verificaciones para el otorgamiento de la resolución que autorizará a los contribuyentes como emisores de documentos tributarios electrónicos; cabe aclarar que las pruebas para estos eventos deberán realizarse independientemente se solicite ingresar con uno o más DTE. (Ver anexo 1 Pruebas de Transmisión Satisfactorias Mínimas para eventos).

A continuación se muestra el contenido de la imagen en formato Markdown:

## 2. Evento de invalidación.

El evento de invalidación es un mensaje de datos firmado electrónicamente que se relaciona con un Documento Tributario Electrónico, que se genera en ocasión de la invalidación del mismo.

Cuando durante los procesos de emisión de documentos tributarios electrónicos ocurran errores que ocasionen la necesidad de invalidar el documento, el contribuyente emisor deberá realizar un evento de invalidación dentro de los plazos establecidos por la Administración Tributaria por tipo de documento.

Tomando en cuenta que los DTE únicamente deberán invalidarse por razones justificadas, se consideran entre estas las siguientes:

1.  Error en la identificación del cliente.
2.  Error en el producto o servicio facturado.
3.  Error en la fecha de la operación.
4.  Error en el precio de los bienes o servicios (aplica únicamente para Factura y Factura de Exportación).
5.  Por devolución de los bienes.
6.  Cuando se rescinda totalmente la operación.

Para realizar el proceso de invalidación, debe enviarse el evento haciendo uso de la estructura establecida que se detalla en este manual.

Es importante aclarar que este evento no elimina ni borra del sistema el DTE, solo se coloca el estado "INVALIDADO" al DTE que se le aplicó el evento de invalidación, dicho documento estará disponible con este estado en el momento que se realice la consulta pública de los DTE. Invalidar un documento, no lo desaparece de la base de datos interna de DGII.

El evento de invalidación también es sometido a verificación del cumplimiento de la estructura de datos establecida por la Administración Tributaria.

---
### 2.1 Secciones de estructura para el evento de invalidación.

Para poder invalidar el DTE el emisor deberá enviar por medio del Sistema de transmisión DTE, la estructura Json del evento diseñada por la Administración Tributara, que consta de 4 secciones que se describen a continuación:

**Identificación:** Esta sección contiene la información que identifica plenamente al evento de invalidación electrónico como único en el universo de documentos electrónicos generados por el emisor, que tiene como objetivo proporcionar la información que permitirá realizar las respectivas correspondencias en la base de datos que almacenará dicha información. Asimismo, proporciona los campos necesarios para el correspondiente tratamiento del evento en relación a los demás sistemas de la DGII.

**Emisor del evento de invalidación:** Esta sección cuenta con los campos necesarios que permitan identificar al emisor y el tipo de establecimiento donde se está realizando el evento de invalidación.

**Identificación del documento a invalidar:** Hace referencia a los datos que identifican al Documento Tributario Electrónico que se desea invalidar (el cual ya ha obtenido el sello de recepción), e información básica que identifique al receptor. Dicha información descrita en esta sección debe tener correspondencia entre los datos que identifican al Documento Tributario Electrónico (DTE) y las generales del receptor que se describe en el documento a invalidar.

**Motivo de la invalidación:** En esta sección se deberá ingresar el motivo de invalidación del DTE, e identificar los responsables de efectuar y solicitar la invalidación; para una mejor comprensión de esta sección es necesario ampliar la información sobre el uso del campo “tipo de invalidación” en el cual deberá ingresar por medio de un código (según catálogo 024 Tipo de Invalidación), el motivo por el cual se invalidará el documento, teniendo para elección las tres opciones siguientes:

1. Error en la información del Documento Tributario Electrónico a invalidar.
2. Rescindir de la operación realizada.
3. Otro.

Por regla general, si el campo tipo de invalidación está lleno con la opción 1 o 3, será requerido que antes de enviar el evento de invalidación del DTE, se tenga generado, transmitido y con sello de recepción el documento que reemplaza al documento invalidado, debido a que la estructura del evento de invalidación solicita introducir tanto el “código de generación del documento a invalidar” como el “código de generación del documento que reemplaza al documento invalidado”. Ambos campos se encuentran en la sección "Identificación del documento a invalidar". Esta condición no aplicará para los casos que el documento a invalidar sea Nota de Crédito o Comprobante de Liquidación (Ver anexo 2 de este manual).

### 2.2 Proceso para transmitir el evento de invalidación.

El emisor debe generar el evento de invalidación en formato Json, ingresando el DTE que requiera ser invalidado (un evento por cada documento que se requiera invalidar), en dicho evento debe indicarse el motivo por el cual invalidará el DTE según la codificación establecida en catálogo "CAT-024 Tipo de Invalidación", una vez esté completa toda la información solicitada según la estructura establecida, el emisor enviará el archivo de datos en formato Json desde su plataforma al Sistema de transmisión DTE, por medio de modelo de recepción previo y tipo de transmisión normal, la Administración Tributaria recibe esta información y corre el proceso de verificación del cumplimiento de la estructura de datos, de no cumplir con dicha estructura, se rechazará el evento de la invalidación remitiendo un mensaje de datos que indican el error identificado en el citado evento para su corrección.

El emisor deberá solventar el o los errores identificados, para transmitir nuevamente el evento de invalidación, y una vez corregidos todos los errores indicados, la Administración Tributaria otorgará el sello de recepción. En el momento que se otorgue el sello de recepción al evento de invalidación, se colocará estado de invalidado al DTE que se ha informado mediante dicho evento.

El emisor y receptor podrán consultar en el portal oficial de servicios en línea del MH, el DTE por medio de su código de generación o sello de recepción.

Este evento de invalidación se podrá aplicar a todos los DTE establecidos en el Código Tributario, dentro de los siguientes plazos:

### 2.3 Plazos para transmitir el evento de invalidación.

| Documento Tributario Electrónico | Plazo para transmitir el evento de invalidación electrónico |
| :--- | :--- |
| Comprobante de Crédito Fiscal Electrónico.<br>Nota de Crédito Electrónica.<br>Nota de Débito Electrónica.<br>Nota de Remisión Electrónica.<br>Comprobante de Retención Electrónico.<br>Comprobante de Liquidación Electrónico.<br>Documentos Contable de Liquidación Electrónico.<br>Factura Sujeto Excluido<br>Comprobante de Donación | Podrá realizarse dentro de un plazo máximo de un día siguiente del otorgamiento del sello de recepción del documento.<br><br>Ejemplo: Si el DTE obtuvo sello de recepción a las 7:30:00 (de la mañana) el contribuyente emisor tendrá hasta las 23:59:59 del día siguiente para poder enviar el evento de invalidación para dicho DTE. |
| Factura Electrónica.<br>Factura de Exportación Electrónica. | Podrá realizarse dentro del plazo de tres meses contados a partir del otorgamiento del sello de recepción del documento.<br><br>Ejemplo: Si el DTE obtuvo el sello de recepción el 11 de noviembre 2021 a las 7:30:00 (de la mañana) el contribuyente emisor tendrá hasta el 11 de febrero 2022 a las 23:59:59 para poder enviar el evento de invalidación para dicho DTE. |

No se otorgará sello de recepción al evento de invalidación transmitido fuera de los plazos establecidos, por lo que el DTE aún conservará su validez original.

### 2.4 Condiciones especiales.

1. Cuando la invalidación del DTE sea por razones formales, y que por lo tanto procede la emisión de un nuevo documento, deberá emitirse primero el documento que sustituya al que se está invalidando, para ingresar el código de generación del documento que reemplazará la operación en la estructura del evento de invalidación que se transmitirá. Esta condición no tendrá efecto cuando el documento a invalidar sea Nota de Crédito o Comprobante de Liquidación.
1. Cuando el motivo de la invalidación sea rescindir la operación deberá ingresar únicamente el código de generación del DTE a invalidar.

    **Ejemplo 1:** Se emite factura electrónica con código de generación **FF54E9DB-79C3-42CE-B432-EC522C97EFB9** con error en el nombre del receptor el cual ya ha obtenido sello de recepción, por lo que es necesario emitir factura electrónica con nombre correcto.

    El emisor deberá primero emitir la nueva factura electrónica con el nombre correcto que tendrá un nuevo código de generación (**AD54E9BB-79A3-42AE-B432-EC522C97EFB7**) y su respectivo sello de recepción, posteriormente deberá generar el evento de invalidación describiendo en la sección "Identificación del Documento a Invalidar" la información del DTE a invalidar, que incluye entre otros el "**Código de generación del DTE a invalidar**" (factura incorrecta **FF54E9DB-79C3-42CE-B432-EC522C97EFB9**). Asimismo, deberá ingresar el "Código de generación del documento que corrige la operación" (segunda factura emitida y recepcionada correctamente **AD54E9BB-79A3-42AE-B432-EC522C97EFB7**).

    **Ejemplo 2:** Se emite factura electrónica por la venta de 2 sillas, por diferentes razones, el comprador decide regresar el producto solicitando la devolución del valor pagado, por tanto, no procede la emisión de un nuevo documento.

    En este caso el tipo de invalidación a aplicar será rescindir la operación, para lo que el emisor deberá describir la información de la factura electrónica incorrecta que se solicita en la sección "Identificación del documento a invalidar" y en el campo Código de generación del documento que reemplaza al documento a invalidar deberá ingresar la palabra null.

### 2.5 Estructura para transmisión del evento de invalidación
**ESTRUCTURA DE EVENTO DE INVALIDACIÓN PARA LOS DTE V2 **

#### Identificación del Evento de Invalidación

| N° casilla | N° de sección | Campo Json | Campos del evento de Invalidación | Descripción de contenido del campo | Condición del campo | Tipo de dato | Longitud |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1 | identificacion.version | Versión (del Evento de Invalidación) | Se deberá ingresar el número de la versión del Archivo JSON en cual se esté trabajando, la cual debe asegurarse que sea la última versión vigente, es requerida para la transmisión del evento de invalidación es decir a falta de la misma dicho evento será rechazado.<br>La información requerida en este campo está comprendida en números enteros desde 1 al 99, sin puntos ni ceros a su derecha Ejemplo: La versión vigente para este evento actualmente es 2. | Requerido para su Transmisión | Numérico | Longitud: 2<br>Mínimo: 1,<br>Máximo: 2 |
| 2 | 1 | identificacion.ambiente | Ambiente de destino (del Evento de Invalidación) | Es el ambiente de trabajo por el cual se ésta transmitiendo el evento electrónico pudiendo seleccionar "00" - modo de pruebas o "01" - modo de producción.<br>Se deberá utilizar "00" - Modo Pruebas, únicamente cuando el contribuyente se encuentre realizando las pruebas tecnológicas para asegurarse que el software que han dispuesto para facturar electrónicamente, cumple con las condiciones técnicas para la generación y transmisión del evento de invalidación electrónico. En esta etapa los eventos transmitidos no tendrán validez para efectos tributarios.<br>Los contribuyentes estarán en ambiente de pruebas hasta cumplir con la cantidad de eventos de invalidación, transmitidos exitosamente, posteriormente deberá pasar a modo producción. Podrán utilizar ambiente destino "00", cuando se implementen actualizaciones indicadas por la Administración Tributaria, con el propósito de garantizar el correcto funcionamiento de dichos cambios.<br>Se deberá utilizar "01" - Modo Producción, una vez que el contribuyente haya cumplido con su proceso de pruebas exitosamente y la Administración Tributaria recepcione las transferencias de bienes y servicios por medio de DTE. A partir de este momento los documentos tendrán validez para efectos tributarios. | Requerido para su Transmisión | Alfanumérico | Longitud: 2 |
| 3 | 1 | identificacion.codigoGeneracion | Código de generación del evento de invalidación | Debe cumplir con el estándar del UUID v4, el cual debe ser único por documento (no debe repetirse) longitud de 32 dígitos separados por 4 guiones haciendo un total de 36 posiciones dividido en 5 grupos.<br>Código de generación consiste en un número identificador único, aleatorio y universal.<br>Ejemplo: 9AAD57C3-8315-438F-B041-E9FF92E9FD75 | Requerido para su Transmisión | Alfanumérico | Longitud: 36<br>Mínimo: 36,<br>Máximo: 36 |
| 4 | 1 | identificacion.fecAnula | Fecha del Evento de Invalidación | Deberá indicar la Fecha de Generación del evento de invalidación, la cual deberá tomarse del sistema del contribuyente emisor en el momento de generar dicho evento.<br>La estructura definida es: año, mes y día como se detalla a continuación: YYYY-MM-DD (2021-06-27) | Requerido para su Transmisión | Alfanumérico | 10 |
| 5 | 1 | identificacion.horAnula | Hora del Evento de Invalidación | Deberá indica la hora de generación del evento de invalidación, la cual deberá tomarse del sistema del contribuyente emisor en el instante de generar el evento, cuya estructura definida es: hora, minutos y segundos (HH:MM: SS) 15:58:30. | Requerido para su Transmisión | Alfanumérico | 8 |

#### Emisor del Evento de Invalidación

| N° casilla | N° de sección | Campo Json | Campos del evento de Invalidación | Descripción de contenido del campo | Condición del campo | Tipo de dato | Longitud |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 6 | 2 | emisor.nit | NIT (Emisor) | Deberá de contener el Número de NIT del Emisor sin guiones<br>Nota: Cuando el contribuyente homologue su DUI como su número de identificación tributaria ante el Ministerio de Hacienda deberá ingresar dicho número en este campo. | Requerido para su Transmisión | alfanumérico | Longitud: 14<br>Mínimo: 9,<br>Máximo: 14 |
| 7 | 2 | emisor.nombre | Nombre, denominación o razón social del contribuyente (Emisor) | En este campo deberá ingresar el nombre, denominación o razón social del contribuyente Emisor, tal cual aparezca en la última Tarjeta de NRC. | Requerido para su Transmisión | alfanumérico | Longitud: 250<br>Mínimo: 1,<br>Máximo: 250 |
| 8 | 2 | emisor.tipoEstablecimiento | Tipo de Establecimiento (Emisor) | Deberá de incorporar el tipo de establecimiento en el que se emite el DTE, según catálogo<br>Ver catálogo: **CAT-009** "Tipo de Establecimiento" | Requerido para su Transmisión | alfanumérico | 2 |
| 9 | 2 | emisor.nomEstablecimiento | Nombre de casa matriz, sucursal / agencia, predio/patio, bodega (Emisor) | Deberá de incorporar el nombre de la casa matriz, sucursal/agencia, predio/patio, bodega, según aplique, del contribuyente emisor donde se genera el evento de invalidación | Requerido para su Transmisión | alfanumérico | Longitud: 150<br>Mínimo: 1,<br>Máximo: 150 |
| 10 | 2 | emisor.codEstableMH | Código de Casa Matriz, Sucursal /Agencia, Predio/Patio, Bodega (Emisor) asignado por el MH | Deberá de incorporar el código que la Administración Tributaria le asigne, ya sea para casa matriz, sucursal/agencia, predio/patio, bodega, según aplique donde el contribuyente emisor genera el evento de invalidación.<br>Nota: por el momento durante la transición deberá enviarlo con null | Requerido para su Transmisión | alfanumérico null | Longitud: 4<br>Mínimo: 4,<br>Máximo: 4 |
| 11 | 2 | emisor.codEstable | Código de Casa Matriz, Sucursal /Agencia, Predio/Patio, Bodega (Emisor) asignado por la contribuyente | Deberá de incorporar el código el contribuyente posea internamente de la casa matriz, sucursal / agencia, predio/patio, bodega, según aplique, desde donde se genera el evento de invalidación.<br>Nota: Cuando no posea código interno deberá enviarlo con null | Opcional | alfanumérico null | Longitud: 10<br>Mínimo: 1,<br>Máximo: 10 |
| 12 | 2 | emisor.codPuntoVentaMH | Código de Identificación del Punto de Venta (Emisor) Asignado por el MH | Deberá incorporar el código del punto de venta asignado por el MH al lugar donde se genera el evento de Invalidación. Este código será informado cuando la Administración Tributaria lo asigne, por el momento deberá enviar este campo con null. | Requerido para su Transmisión | alfanumérico null | 4 |
| 13 | 2 | emisor.codPuntoVenta | Código de Identificación del Punto de Venta (Emisor) Asignado por la contribuyente | Deberá incorporar el código del punto de venta asignado al del contribuyente emisor donde se genera el DTE, que el contribuyente emisor maneja internamente, de no utilizar el punto de venta se completará con null. | Opcional | alfanumérico null | Longitud: 15<br>Mínimo: 1,<br>Máximo: 15 |
| 14 | 2 | emisor.telefono | N° de Teléfono (Emisor) | Debe de incorporar el número de teléfono del establecimiento donde se genera el evento de invalidación. | Requerido para su Transmisión | alfanumérico | Longitud: 30<br>Mínimo: 8,<br>Máximo: 30 |
| 15 | 2 | emisor.correo | Correo electrónico (Emisor) | Debe de incorporar el correo electrónico del establecimiento donde se genera el evento de invalidación | Requerido para su Transmisión | alfanumérico | Longitud máxima: 100 |

#### Identificación del Documento a Invalidar

| N° casilla | N° de sección | Campo Json | Campos del evento de Invalidación | Descripción de contenido del campo | Condición del campo | Tipo de dato | Longitud |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 16 | 3 | documento.tipoDte | Tipo DTE a Invalidar | Se deberá indicar el código del documento a Invalidar según catálogo: **CAT-002** "Tipo de Documento".<br>Como por ejemplo si se quiere Invalidar un comprobante de crédito fiscal con Código "03" | Requerido para su Transmisión | alfanumérico | Longitud: 2<br>Mínimo: 2,<br>Máximo: 2 |
| 17 | 3 | documento.codigoGeneracion | Código de generación del DTE a invalidar | Debe ingresar el código de generación del documento que se va a invalidar, deberá enviar un código de generación por evento de invalidación, dicho documento debe poseer sello de recepción.<br>Nota: No procederá el evento de invalidación en el caso que se envié un código de generación que no cuente con sello de recepción por parte de la Administración Tributaria. | Requerido para su Transmisión | Alfanumérico | Longitud: 36<br>Mínimo: 36,<br>Máximo: 36 |
| 18 | 3 | documento.selloRecibido | Sello de recepción (Del DTE a Invalidar) | Debe ingresar el sello de recepción asignado por la Administración Tributaria al DTE transmitido satisfactoriamente que el contribuyente quiere invalidar. | Requerido para su Transmisión | alfanumérico | Longitud: 40<br>Mínimo: 40,<br>Máximo: 40 |
| 19 | 3 | documento.numeroControl | Número de Control del DTE a Invalidar | Deberá ingresar el número de control del DTE que se desea invalidar. Debe cumplir con la estructura definida por la AT una longitud de 31 caracteres (las siglas DTE + código de tipo de documento + (8 dígitos alfanuméricos) para describir código de casa matriz o sucursal y código punto de venta + secuencial de 15 dígitos.<br>Ejemplo DTE-03-12345678-000000000000001 (se debe ingresar la estructura como se indica en el ejemplo incluyendo guiones) | Requerido para su Transmisión | alfanumérico | 31 |
| 20 | 3 | documento.fecEmi | Fecha de generación del DTE a Invalidar | Deberá de contener la fecha de emisión del DTE original a invalidar (la fecha contenida en el campo fecha de generación del documento a invalidar). | Requerido para su Transmisión | Alfanumérico | 10 |
| 21 | 3 | documento.montoIva | Monto total de la operación (Del DTE A Invalidar) | Deberá de contener el valor contenido en el campo "monto total de la operación" del DTE a invalidar (aplicará solo CCF, F y FEX)<br>Cuando los documentos a invalidar sean diferentes a CCF, F, y FEX este campo podrá ser null.<br>Este campo se expresarán valores monetarios con un máximo de dos decimales después del entero. Ej.: $12,345,678,901.12 | Requerido por Tipo de Operación | Numérico | 11,2 |
| 22 | 3 | documento.codigoGeneracionR | Código de generación del documento que reemplaza al documento invalidado | Cuando el Tipo de Invalidación no sea rescindir la operación (es decir cuando en campo tipo de invalidación este completo con los códigos 1 o 3), previo al envío del evento de invalidación, el contribuyente emisor deberá emitir un nuevo documento que sustituya la operación que se desea invalidar. Se exceptúan de esta condición los DTE siguientes: Nota de Crédito y Comprobante de Liquidación.<br>Para el envío del Evento deberá ingresar en este campo el código de generación del nuevo documento tributario electrónico al cual ya se le ha otorgado sello de recepción y que sustituye la operación que se está invalidando.<br>Cuando las causas de la invalidación sea rescindir la operación realizada, este campo se llenará con null. | Requerido por Tipo de Operación | Alfanumérico | 36 |
| 23 | 3 | documento.tipoDocumento | Tipo de documento de identificación (Receptor) | Deberá seleccionar codificación de acuerdo a catálogo de tipo de documento de identificación (Receptor). Ver Catálogo **CAT-022** "Tipo de documento del receptor".<br>Notas<br>Se ingresará la opción "13"-DUI para el caso de las personas naturales no inscritas en IVA.<br>Para el caso que el contribuyente homologue su DUI con su NIT ante el Ministerio de Hacienda, deberá elegir la opción "36" -NIT e ingresar el número de DUI que lo identifica como contribuyente. | Requerido para su Transmisión | numérico | Longitud: 2<br>Mínimo: 2,<br>Máximo: 2 |
| 24 | 3 | documento.numDocumento | Número de documento de Identificación (Receptor) | Deberá ingresar número de documento de identificación (Receptor).<br>Cuando el contribuyente homologue su DUI con su NIT ante el Ministerio de Hacienda, se aceptará como NIT su DUI. | Requerido para su Transmisión | alfanumérico | Longitud Máxima: 20 |
| 25 | 3 | documento.nombre | Nombre, denominación o razón social del contribuyente (Receptor) | Deberá contener el nombre, denominación o razón social del contribuyente receptor del DTE a invalidar | Requerido para su Transmisión | alfanumérico | Longitud: 200<br>Mínimo: 1,<br>Máximo: 200 |
| 26 | 3 | documento.telefono | N° de Teléfono (Receptor) | Debe incorporar el número de teléfono con longitud máxima de 30 dígitos | Opcional | alfanumérico | Longitud: 30<br>Mínimo: 8,<br>Máximo: 30 |
| 27 | 3 | documento.correo | Correo electrónico (Receptor) | Deberá incorporar el correo electrónico con dominio vigente, del contribuyente receptor. | Opcional | alfanumérico | Longitud Máxima: 100 |

#### Motivo de la Invalidación

| N° casilla | N° de sección | Campo Json | Campos del evento de Invalidación | Descripción de contenido del campo | Condición del campo | Tipo de dato | Longitud |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 28 | 4 | motivo.tipoAnulacion | Tipo de Invalidación | Debe indicar el motivo por el cual está invalidando el DTE según catálogo **CAT-024** "Tipo de invalidación" | Requerido para su Transmisión | numérico | 1 |
| 29 | 4 | motivo.motivoAnulacion | Motivo de Invalidación | En este campo el contribuyente emisor deberá describir el o los campos donde se encuentra el error que ocasiona el evento de invalidación. | Requerido para su Transmisión | alfanumérico | Longitud: 200<br>Mínimo: 1,<br>Máximo: 200 |
| 30 | 4 | motivo.nombreResponsable | Nombre del responsable de invalidar el documento (Emisor) | Deberá ingresará el nombre de la persona responsable de invalidar el documento tributario electrónico (Emisor) | Requerido para su Transmisión | alfanumérico | Longitud: 100<br>Mínimo: 1,<br>Máximo: 100 |
| 31 | 4 | motivo.tipDocResponsable | Tipo de documento de identificación del responsable de Invalidar el documento (Emisor) | Deberá seleccionar la codificación de acuerdo a catálogo **CAT-022** "Tipo de documento de identificación del responsable de invalidar el documento". | Requerido para su Transmisión | numérico | 1 |
| 32 | 4 | motivo.numDocResponsable | Número de documento de Identificación del responsable de Invalidar el documento (Emisor) | Deberá colocar el número de documento de identificación del responsable de invalidar el documento (Emisor). | Requerido para su Transmisión | alfanumérico | Longitud: 14<br>Mínimo: 1,<br>Máximo: 14 |
| 33 | 4 | motivo.nombreSolicita | Nombre de quien solicita invalidación el documento | Deberá ingresar el nombre de la persona quien solicita invalidar el documento tributario electrónico (receptor).<br>En caso que el solicitante de la invalidación sea el mismo emisor, se deberá colocar nuevamente los datos del emisor responsable de dicha solicitud. | Requerido para su Transmisión | alfanumérico | Longitud: 100<br>Mínimo: 1,<br>Máximo: 100 |
| 34 | 4 | motivo.tipDocSolicita | Tipo de documento de identificación de quien solicita Invalidar el documento | Deberá seleccionar codificación de acuerdo a catálogo **CAT-022** "Tipo de documento de identificación".<br>En caso que el solicitante de la Invalidación sea el mismo emisor, se deberá colocar nuevamente los datos del emisor responsable de dicha solicitud. | Requerido para su Transmisión | numérico | 1 |
| 35 | 4 | motivo.numDocSolicita | Número de documento de Identificación de quien solicita Invalidar el documento | Deberá ingresar número de documento de identificación de quien solicita invalidar el documento (receptor).<br>En caso que el solicitante de la invalidación sea el mismo emisor, se deberá colocar nuevamente los datos del emisor responsable de dicha solicitud. | Requerido para su Transmisión | alfanumérico | Longitud: 14<br>Mínimo: 1,<br>Máximo: 14 |

#### Sello de recepción del evento de invalidación

| N° casilla | N° de sección | Campo Json | Campos del evento de Invalidación | Descripción de contenido del campo | Condición del campo | Tipo de dato | Longitud |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 36 | 5 | Sello de recepción | Sello de recepción | Sello de recepción no es parte del archivo Json a enviar al Ministerio de Hacienda, ya que este será la respuesta de la Administración Tributar. | | | |

## 3. Evento de contingencia.

La contingencia se puede definir como un caso fortuito o fuerza mayor que le impide al facturador electrónico, transmitir de forma inmediata los documentos electrónicos a la Administración Tributaria.

Evento de Contingencia es un mensaje de datos firmado electrónicamente que se relaciona con uno o varios Documento Electrónico, que se generan en ocasión de casos que impiden realizar la transmisión de los DTE.

Cuando por motivo de fuerza mayor, el emisor no pueda realizar la transmisión de los documentos electrónicos a la Administración Tributaria, este podrá generar los documentos electrónicos con sus propios procesos de contingencia. Los contribuyentes son los encargados de diseñar y ejecutar en sus sistemas las condiciones que les permitan generar los documentos electrónicos, es decir, deben prever todos los medios técnicos y administrativos adecuados, así como los mecanismos alternativos que les garanticen el funcionamiento de sus servidores y equipos en el proceso de la emisión y resguardo de los documentos electrónicos, para que una vez superada la situación que les impida realizar la transmisión, estos puedan transmitir el evento de contingencia incorporando el detalle de todos los documentos generados durante el periodo en el que ocurrió la situación de fuerza mayor que le impidió transmitir dichos documentos a la Administración Tributaria de manera normal.

### 3.1 Modelo de recepción para los DTE en generados contingencia.

Para recepcionar los documentos que sean generados en contingencia, se ha diseñado el modelo de recepción diferida, el cual consiste en que el emisor genera en su sistema interno de facturación, el documento electrónico en formato JSON incorporándole su firma electrónica y entregará al receptor dicho documento por cualquier medio electrónico. Es decir, que entregará al receptor el documento electrónico sin contar con el sello de recepción (únicamente utilizado en contingencia).

Posteriormente superada la contingencia (reestablecida la conexión) deberá transmitir el evento de contingencia donde informa la situación de contingencia y los documentos entregados sin sello de recepción; por último, el contribuyente emisor debe transmitir a la Administración Tributaria dichos documentos generados en contingencia, para que esta pueda correr los procesos establecidos en referencia a la verificación del cumplimiento de la estructura de datos, una vez se reciba la información y esta cumpla con la estructura de datos establecida, la Administración Tributaria otorgará el “sello de recepción”, brindando a cada uno de los documentos electrónicos la calidad de Documento Tributarios Electrónico (DTE).

Si el documento electrónico no cumple con la estructura de datos establecida, será rechazado y se devolverá con un mensaje al emisor detallando los campos que no cumplen con la información solicitada, para su corrección y nuevo envío.

Una vez que el documento electrónico ha obtenido el sello de recepción, el Ministerio de Hacienda resguardará la información contendida en el DTE, y proporcionará un servicio donde cualquier usuario podrá consultar el estado del DTE, por medio del código de generación o el sello de recepción. 

#### Diagrama de Recepción Diferido. 
![Diagrama de Recepción Diferido.](diagram-recdif.png)

---
### 3.2 Secciones de la estructura definida por la Administración Tributaria para ingresar evento de contingencia.

La Administración Tributaria ha definido una estructura específica para el envío del evento de contingencia; una vez haya finalizado el inconveniente que le imposibilitó realizar su transmisión en línea de los DTE, el emisor deberá generar y firmar un mensaje de datos que contendrá toda la información requerida en la estructura definida por esta Administración para el envío del evento de contingencia, en formato Json. Este evento será enviado por medio del Sistema de transmisión DTE, modelo de recepción previo y tipo de transmisión normal.

La estructura diseñada para informar el evento de contingencia contiene 4 secciones que se describen a continuación:

1.  **Identificación:** Esta sección contiene la información que identifica plenamente al evento de contingencia, como único en el universo de documentos generados por el emisor, tiene como objetivo proporcionar la información que permitirá realizar las respectivas correspondencias de conformidad a la Ley de Firma Electrónica. Asimismo, proporciona los campos necesarios para el correspondiente tratamiento del evento en relación a los demás sistemas de la DGII.
2.  **Identificación del emisor del evento de contingencia:** Esta sección cuenta con los campos necesarios que permitan identificar al emisor y el establecimiento donde se está realizando el evento de contingencia.
3.  **Detalle de documentos Electrónicos en Contingencia:** Hace referencia a los datos que identifican al documento electrónico que se ha generado fuera de línea, proporcionando los datos de tipo de documento y código de generación, que permitirán una relación en el momento que se envíen los documentos electrónicos a la Administración Tributaria para que puedan ser recepcionados. Estos se informarán a manera de lista hasta un máximo de 5000 documentos por cada evento.
4.  **Motivo de la Contingencia:** En esta sección se deberá ingresar los datos que identifiquen el motivo y el periodo en que ocurrió el motivo de fuerza mayor que imposibilitó la transmisión en línea de los documentos electrónicos a la Administración Tributaria.
5.  


### 3.3 Proceso para generar DTE "en contingencia".

Se podrán emitir en contingencia los siguientes documentos electrónicos:

* Factura Electrónica.
* Comprobante de Crédito Fiscal Electrónico.
* Nota de Remisión Electrónica.
* Nota de Crédito Electrónica.
* Nota de Debito Electrónica.
* Factura de Exportación Electrónica.

Cuando se haga imposible la transmisión de estos documentos, el contribuyente podrá seguir operando con su sistema de respaldo para operar fuera de línea, la estructura que se utilizará para poder generar estos documentos en contingencia, será la misma estructura establecida por la DGII para realizar transmisión normal por tipo de documento, con algunas particularidades del llenado de ciertos campos los cuales se detallan a continuación:

**Modelo de Facturación:** Debe ingresar la opción 2 "Modelo de Facturación Diferido"

**Tipo de Transmisión:** Debe ingresar la opción 2 "Transmisión por Contingencia"

**Tipo de Contingencia:** Debe ingresar un código que identifique el tipo de contingencia, de acuerdo a catálogo CAT-005 Tipo de Contingencia.

**Motivo de Contingencia:** Deberá explicar el motivo de contingencia cuando en campo "tipo de contingencia" se ingrese la opción 5 - Otro motivo (si se requiere podrá ampliar el motivo de contingencia cuando tipo de contingencia sea diferente a 5).

### 3.4 Proceso para transmitir documentos electrónicos en contingencia.

Los contribuyentes están obligados a transmitir a la Administración Tributaria los documentos generados en contingencia.

Para poder transmitir estos documentos electrónicos generados en contingencia, la Administración Tributaria ha establecido el proceso de transmisión una vez que se supere la situación imprevista que le imposibilitó la transmisión, lo cual se describe a continuación:


#### MOMENTO 1

**Ocurrencia de fuerza mayor que impida al contribuyente emisor la transmisión del DTE, en los siguientes casos:**

a) Falla en conexiones del sistema del emisor (Siempre que no impida generar el documento electrónico y entregar la representación gráfica).
b) Falla en el suministro del servicio de Internet por el proveedor del emisor (Siempre que no impida generar el documento electrónico y entregar la representación gráfica).
c) Falla en el suministro del servicio de energía eléctrica por el proveedor del emisor que le impidan realizar la transmisión de los documentos electrónicos (Siempre que no impida generar el documento electrónico y entregar la representación gráfica).
d) No disponibilidad de sistema del MH para realizar la recepción (Siempre que no impida generar el documento electrónico y entregar la representación gráfica).

El contribuyente podrá identificar que está en contingencia cuando al momento de enviar un DTE, el Sistema de transmisión DTE no responda después 5 segundos, o si al momento de enviar un DTE, el servicio del emisor falla y no procesa la respuesta del servicio de recepción. Cuando tengan ocurrencia estos hechos se deberá aplicar uno a uno los pasos establecidos en la "Política de reintentos" la cual se detalla en la "Guía de Integración Tecnológica". Una vez aplicada esta política de reintentos y no se logra la transmisión ni la recepción de los DTE el contribuyente deberá operar en contingencia.

El contribuyente emisor continuará generando y firmando el archivo Json del documento electrónico, dando cumplimiento con los requisitos de la estructura establecida por la Administración Tributaria para cada tipo de documento tributario electrónico, con el llenado de los campos específicos. Debido a que estos documentos no pueden ser transmitidos a la Administración Tributaria de manera normal, sino que posteriormente de haber superado la situación que impidió realizar la transmisión en línea, el emisor deberá en el momento de la generación del documento electrónico, ingresar en el campo "Modelo de facturación" la opción "**2 modelo de facturación Diferido**", en el campo "tipo de transmisión" la opción **2 (transmisión por contingencia)** y además en el campo "tipo de contingencia" ingresar el motivo de la contingencia con base al catálogo establecido.

El contribuyente emisor procede a almacenar el documento y generar la representación gráfica que deberá entregar al receptor sin sello de recepción, debiendo reflejar en dicha Representación que el documento ha sido emitido en "modelo de facturación diferido" y "transmitido en contingencia", para que los clientes se encuentren informados respecto al motivo de la falta temporal del sello de recepción en el documento.

---
#### MOMENTO 2
##### Envío de evento de contingencia por el contribuyente emisor.

Una vez superada la causa de fuerza mayor que dio origen a los documentos electrónicos en contingencia, el contribuyente emisor deberá generar, firmar y transmitir un **"Evento de Contingencia"**. Para transmitir el evento antes mencionado el emisor de documentos tributarios electrónicos tendrá un plazo máximo de **24 horas** para transmitir el evento, contadas a partir del cese de la situación de fuerza mayor que provocó la contingencia.

Mediante el evento de contingencia se deben informar los códigos de generación de todos los documentos electrónicos que fueron generados mientras ocurrió la situación de fuerza mayor, detallando los datos que identifican al documento electrónico en la estructura establecida por la Administración Tributaria en la sección detalle de documentos electrónicos en contingencia, donde podrá describir desde **1 hasta un máximo de 5,000 documentos electrónicos** generados en contingencia.

El envío de este evento de contingencia es un requisito previo para poder transmitir el lote de los citados documentos electrónicos, para que puedan ser procesados por la Administración Tributaria; el emisor transmitirá el evento por medio de un archivo **JSON** conforme a la estructura definida, dicho archivo se deberá transmitir a través del Sistema de transmisión **DTE** con modelo de recepción previo y tipo de transmisión normal.

Una vez que el contribuyente emisor transmita el evento de contingencia, la Administración Tributaria lo recibirá y realizará el proceso de verificación del cumplimiento de la estructura de datos establecida por la Administración Tributaria y una vez habiendo superado los mismos, dará respuesta a través de un sello de recepción al evento transmitido.

Cuando el evento de contingencia no cumpla con la estructura de datos establecida se rechazará, se regresará por medio del Sistema de transmisión DTE al emisor, indicando el error identificado para su corrección en un plazo máximo de **24 horas** después de que el evento haya sido rechazado. El emisor deberá solventar, para transmitir nuevamente el evento de contingencia, y una vez corregidos todos los errores indicados, la Administración Tributaria colocará el sello de recepción para posteriormente almacenar este evento para su conservación en la base de datos de **DGII**.


#### MOMENTO 3
##### Transmisión de documentos electrónicos en contingencia.

Una vez el **"Evento de Contingencia"** haya obtenido el sello de recepción por parte de la Administración Tributaria, el contribuyente emisor deberá transmitir un archivo Json firmado electrónicamente que compile el lote de los documentos electrónicos generados en contingencia que fueron informados previamente en el evento (Es decir que no podrán incluir en este lote, documentos que no hayan sido informados en contingencia o que se realizaron en transmisión normal sin inconvenientes para su transmisión).

El lote de los documentos electrónicos generados en contingencia una vez transmitidos se procesará documento por documento, a los cuales se les aplicará un proceso de verificación del cumplimiento de la estructura de datos establecida por la Administración Tributaria por tipo de documento tributario electrónico.

Se tendrá un plazo máximo de **72 horas** contadas a partir del otorgamiento del sello de recepción del evento de contingencia para poder enviar el lote de todos los documentos electrónicos que fueron informados en dicho evento, para que una vez transmitidos, a estos, les sea aplicado el proceso de verificación del cumplimiento de la estructura de datos establecida por la Administración Tributaria y una vez superados estos requisitos puedan obtener el sello de recepción correspondiente a cada uno de los documentos transmitidos e informados previamente en el evento de superada la contingencia.

**Notas importantes:**

> * Cuando sea factible el emisor deberá entregar la representación gráfica con su sello de recepción o en su defecto el archivo Json del documento tributario electrónico que contenga el sello de recepción otorgado por la Administración Tributaria.
> * Si el contribuyente no realiza la transmisión del evento de contingencia o no realiza la transmisión de los DTE reportados en el evento dentro del plazo establecido en la resolución de autorización respectiva, deberá informar y justificar por escrito a la DGII, las razones del incumplimiento y solicitar autorización de prórroga del plazo establecido, a efecto que se permita la correspondiente transmisión del evento y de los citados documentos.
> * Previa a la fecha designada por la Administración Tributaria, los contribuyentes están sujetos a las condiciones bajo las cuales se les ha otorgado la respectiva autorización.
> * Queda facultada la Administración Tributaria para revocar la autorización otorgada para emitir DTE cuando verifique que el contribuyente no resguarda la seguridad, cumplimiento y exactitud de los impuestos causados, de acuerdo a las disposiciones legales pertinentes y a lo establecido en la respectiva autorización.

### 3.5 Estructura para transmisión de evento de contingencia. 

#### Información de Identificación

| N° Casilla | Sección | Campo Json | Campos del Evento de Contingencia | Descripción de Contenido del Campo | Condición del Campo | Tipo de dato | Longitud |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1 | identificacion.version | Versión (del evento de contingencia) | Se deberá ingresar el número de la versión del Archivo JSON en cual se esté trabajando, la cual debe asegurarse que sea la última versión publicada por la Administración Tributaria. Para el evento de contingencia es decir a falta de la misma, dicho evento será rechazado.<br>La información requerida en este campo está comprendida en números enteros desde 1 al 99 sin puntos ni ceros a su derecha, los cuales no deben de usarse para la transmisión del documento.<br>El contribuyente deberá colocar los valores de la versión del documento electrónico pudiendo seleccionar: "00" modo de pruebas o "01" modo de producción. | Requerido para su Transmisión | Numérico | Longitud: 2<br>Mínimo: 1<br>Máximo: 2 |
| 2 | 1 | identificacion.ambiente | Ambiente de Destino (del evento de contingencia) | Se deberá utilizar "00" - Modo Pruebas, únicamente cuando el contribuyente se encuentre realizando las pruebas tecnológicas con la Administración Tributaria para la recepción del documento electrónicamente, cumple con las condiciones técnicas para la transmisión, y una vez que estas pruebas sean completadas, los DTE en esta etapa los eventos transmitidos no tendrán validez para efectos tributarios.<br>Los contribuyentes estarán en ambiente de pruebas hasta cumplir con la cantidad de eventos en contingencia, transmitidos exitosamente y la Administración Tributaria los acepte como validos.<br>Podrán utilizar ambiente destino "00", cuando lo implementen los desarrollos propios o la Administración Tributaria con el propósito de garantizar el correcto funcionamiento de dichos cambios.<br>Se deberá utilizar "01" - Modo Producción, una vez que el contribuyente esté validado para transmitir de forma exitosamente y la Administración Tributaria recepcione las pruebas previas al ambiente de producción y la valide en la estructura establecida, a partir de este momento los documentos tendrán validez para efectos tributarios. | Requerido para su Transmisión | Alfanumérico | Longitud: 2<br>Mínimo: 2<br>Máximo: 2 |
| 3 | 1 | identificacion.codigoGeneracion | Código de Generación del evento de contingencia | Debe cumplir con el estándar del UUID v4, el cual debe ser único por documento (el cual no debe repetirse) longitud de 32 dígitos separados por 4 guiones haciendo un total de 36 posiciones dividido en 5 grupos.<br>Código de generación consiste en un número identificador único, aleatorio y universal.<br>Ejemplo: "FF54E90B-79C5-42C1-8452-EC52C97E1BE9". | Requerido para su Transmisión | Alfanumérico | Longitud: 36<br>Mínimo: 36<br>Máximo: 36 |
| 4 | 1 | identificacion.fechaTransmision | Fecha transmisión del evento de contingencia | Deberá indicar la Fecha de Generación del evento de contingencia, la cual deberá tomarse del sistema del contribuyente emisor en el momento de generar dicho evento. | Requerido para su Transmisión | Alfanumérico | 10 |
| 5 | 1 | identificacion.hTransmision | Hora transmisión del evento contingencia | Deberá indicar la hora de generación del evento de contingencia, la cual deberá tomarse del sistema del contribuyente emisor en el instante de generar el evento, cuya estructura definida es hora, minuto y segundos HH:MM:SS. | Requerido para su Transmisión | Alfanumérico | 8 |
---
 
#### Identificación del emisor del evento de contingencia
 
| N° Casilla | Sección | Campo Json | Campos del Evento de Contingencia | Descripción de Contenido del Campo | Condición del Campo | Tipo de dato | Longitud |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 6 | 2 | emisor.nit | NIT (Emisor) del Emisor del evento de contingencia | Deberá de contener el Número de NIT del Emisor sin guiones.<br>Nota: Cuando el contribuyente homologue su DUI como su número de identificación tributaria, el Ministerio de Hacienda deberá ingresar dicho número en este campo. | Requerido para su Transmisión | Alfanumérico | Longitud: 14<br>Mínimo: 9<br>Máximo: 14 |
| 7 | 2 | emisor.nomb | Nombre, denominación o razón social del contribuyente (Emisor) del Emisor del evento de contingencia | Deberá contener el nombre, denominación o razón social del contribuyente emisor, tal cual aparece en la última tarjeta de NRC. | Requerido para su Transmisión | Alfanumérico | Longitud: 250<br>Mínimo: 1<br>Máximo: 250 |
| 8 | 2 | emisor.nombrC | Nombre del responsable del documento del Emisor del evento de contingencia | Indicar el nombre de la persona responsable del establecimiento que informa el evento de contingencia. | Requerido para su Transmisión | Alfanumérico | Longitud: 100<br>Mínimo: 1<br>Máximo: 100 |
| 9 | 2 | emisor.tipDoc | Tipo de documento de identificación de la persona del Emisor del evento de contingencia | Deberá colocar el código de documento de identificación de la persona que informa el evento, de acuerdo al valor del catálogo de tipo de documento de identificación **CAT-022** "Tipo de documento de Identificación". | Requerido para su Transmisión | Alfanumérico | 2 |
| 10 | 2 | emisor.numDoc | Número de documento de identificación del responsable del Emisor del evento de contingencia | Deberá colocar el número de documento de identificación de la persona que informa el evento de contingencia. | Requerido para su Transmisión | Alfanumérico | Longitud: 25<br>Mínimo: 1<br>Máximo: 25 |
| 11 | 2 | emisor.tipoEstablecimiento | Tipo de establecimiento (terminales de punto de venta) en contingencia del Emisor del evento de contingencia | Deberá de incorporar el código de tipo de establecimiento en el que se emiten los documentos, el cual deberá ser requerido para los POS (ver catálogo de codificación **CAT-009** Tipo de establecimiento). | Requerido para su Transmisión | Alfanumérico | 2 |
| 12 | 2 | emisor.codEstablecimiento | Código de tipo de establecimiento (Emisor) Asignado por el MH del Emisor del evento de contingencia | Deberá de incorporar el código de casa matriz / Sucursal / Agencia / Tienda / Bodega, asignado por el Ministerio de Hacienda o quien este designe. | Opcional para su Transmisión | Alfanumérico | Longitud: 4<br>Mínimo: 1<br>Máximo: 4 |
| 13 | 2 | emisor.codPuntoVenta | Código de identificación del punto de venta (Emisor) Asignado por el MH del Emisor del evento de contingencia | Nota: Por el momento durante la transmisión deberá enviarlo con null<br>Deberá incorporar el código del punto de venta asignado por el Ministerio de Hacienda, el cual será un correlativo, este será informado cuando la Administración Tributaria lo asigne, por el momento se deberá enviar con valores de "001". | Opcional para su Transmisión | Alfanumérico | Longitud: 4<br>Mínimo: 1<br>Máximo: 4 |
| 14 | 2 | emisor.telefono | N° de Teléfono (Emisor) del Emisor del evento de contingencia | Debe de incorporar el número de teléfono del establecimiento emisor donde se genera el evento de contingencia. | Requerido para su Transmisión | Alfanumérico | Longitud: 50<br>Mínimo: 8<br>Máximo: 50 |
| 15 | 2 | emisor.correo | Correo electrónico (Emisor) del Emisor del evento de contingencia | Debe de incorporar el correo electrónico del establecimiento donde se genera el evento de contingencia. | Requerido para su Transmisión | Alfanumérico | Longitud: 100<br>Mínimo: 1<br>Máximo: 100 |


#### Detalle de documentos Electrónicos en Contingencia

| N° Casilla | Sección | Campo Json | Campos del Evento de Contingencia | Descripción de Contenido del Campo | Condición del Campo | Tipo de dato | Longitud |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 16 | 3 | detalleDTE.noItem | N° de Items (Detalle de documentos Electrónicos en Contingencia) | Esta sección es obligatoria se deberá repetir sección completa desde campo 17 "N° de Items" hasta campo 19 "código de generación de documento electrónico en contingencia" hasta un máximo de 5000 veces. (Cada ítem debe detallar un DTE).<br>En este campo se hará referencia a las filas de los items por cada bien o servicio vendido, por lo que deberá contener una numeración secuencial iniciando en 1 al hasta un máximo de 5,000 ítems.<br>NOTA: Se podrán informar hasta un máximo de 5000 código de generación, en el caso que quisiera informar más de 5000 documentos se deberá generar un nuevo evento de contingencia. | Requerido para su Transmisión | Numérico | 4 |
| 17 | 3 | detalleDTE.tipoDoc | Tipo de documento en contingencia (Detalle de documentos Electrónicos en Contingencia) | Se deberá colocar el código del tipo de documento electrónico generados en contingencia de acuerdo a codificación según catálogo **CAT-026** Tipo de Documento en Contingencia.<br>Se podrán emitir en contingencia los siguientes documentos: "01-F", "03-CCF", "05-NC", "06-ND", "04-NR", "11-FEX" y "14-FSE". | Requerido para su Transmisión | Alfanumérico | Longitud: 2<br>Mínimo: 2<br>Máximo: 2 |
| 18 | 3 | detalleDTE.codigoGeneracion | Código de generación de documento electrónico en contingencia (Detalle de documentos Electrónicos en Contingencia) | Deberá incorporar el código de generación de cada uno de los documentos emitidos en contingencia.<br>Debe cumplir con el estándar del UUID v4, el cual debe ser único por documento (el cual no debe repetirse) longitud de 32 dígitos separados por 4 guiones haciendo un total de 36 posiciones dividido en 5 grupos. <br>Código de generación consiste en un número identificador único, aleatorio y universal.  | Requerido para su Transmisión | Alfanumérico | Longitud: 36<br>Mínimo: 36<br>Máximo: 36 |


#### Motivo de la Contingencia

| N° Casilla | Sección | Campo Json | Campos del Evento de Contingencia | Descripción de Contenido del Campo | Condición del Campo | Tipo de dato | Longitud |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 19 | 4 | motivo.fInicio | Fecha inicio (del Evento de Entrada en Contingencia) | Deberá detallar la fecha de inicio de entrada en contingencia. La estructura definida es: año, mes y día como se detalla a continuación: YYYY-MM-DD (2021-06-27) | Requerido para su Transmisión | Alfanumérico | 10 |
| 20 | 4 | motivo.fFin | Fecha fin (del Evento de Salida en Contingencia) | Deberá detallar la fecha en que finalizó la contingencia. La estructura definida es: año, mes y día como se detalla a continuación: YYYY-MM-DD (2021-06-27) | Requerido para su Transmisión | Alfanumérico | 10 |
| 21 | 4 | motivo.hInicio | Hora inicio (del Evento de Entrada en Contingencia) | Deberá detallar la hora de inicio de entrada en contingencia. La estructura de la hora de entrada en contingencia será definida por la Administración Tributaria, cuya estructura definida es: hora, minutos y segundos (HH:MM:SS) 15:58:30. formato 24hr. | Requerido para su Transmisión | Alfanumérico | 8 |
| 22 | 4 | motivo.hFin | Hora fin (del Evento de Entrada en Contingencia) | Deberá detallar la hora en que finalizó la contingencia. La estructura de la hora de salida en contingencia será definida por la Administración Tributaria, cuya estructura definida es: hora, minutos y segundos (HH:MM:SS) 15:58:30. formato 24hr. | Requerido para su Transmisión | Alfanumérico | 8 |
| 23 | 4 | motivo.tipoContingencia | Tipo de Contingencia (Motivo de la Contingencia) | Deberá seleccionar del catálogo de contingencias cualquiera de las 5 opciones que aplique según el motivo (ver catálogo de codificación: **CAT-005** Tipo de Contingencia) | Requerido para su Transmisión | Numérico | 1 |
| 24 | 4 | motivo.motivoContingencia | Motivo de Contingencia (Motivo de la Contingencia) | En este campo el Contribuyente Emisor podrá ampliar la razón de la contingencia.<br>Podrá enviar campo null siempre que haya elegido motivo de contingencia diferente a "5" (Según catálogo "**005** Tipo de Contingencia").<br>Si el contribuyente Emisor seleccionó la opción "5" deberá obligatoriamente especificar razón u otro motivo de contingencia tendrá un máximo de 1000 caracteres. | Requerido por Tipo de Operación | Alfanumérico | Longitud: 500<br>Mínimo: 1<br>Máximo: 500 |


#### Sello de recepción del evento de superada la contingencia

| N° Casilla | Sección | Campo Json | Campos del Evento de Contingencia | Descripción de Contenido del Campo | Condición del Campo | Tipo de dato | Longitud |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 25 | 5 |  | Sello de recepción del evento de superada la contingencia | Sello de recepción no es parte del archivo Json a enviar al Ministerio de Hacienda, ya que este será la respuesta de la Administración Tributaria. | | | |


## Acrónimos

* **DTE:** Documentos tributarios electrónicos
* **F:** Factura
* **CCF:** Comprobante de Crédito Fiscal
* **NC:** Nota de Crédito
* **ND:** Nota de Debito
* **NR:** Nota de Remisión
* **CR:** Comprobante de Retención
* **CL:** Comprobante de Liquidación
* **DCL:** Documento Contable de Liquidación
* **Json:** JavaScript Object Notation (notación de objeto de JavaScript)

## Anexo 1: Pruebas de transmisión satisfactorias mínimas para eventos de invalidación y contingencia en el Sistema Integrado DTE.

| N° | Tipo de evento | Pruebas satisfactorias mínimas |
| :--- | :--- | :--- |
| 1 | Evento de Invalidación | 5 |
| 2 | Evento de Contingencia | 5 |

---

## Anexo 2: Condiciones para el envío del evento de invalidación.

El evento de invalidación tendrá aplicación cuando ocurran errores formales, así mismo en el caso de la factura y factura de exportación, además de invalidarse por errores formales, también tiene aplicación la invalidación por ajustes que disminuyan, anulen o rescindan operaciones.

En la estructura de datos proporcionada para el envío de dicho evento en la sección “Motivo de la invalidación” se encuentra el campo “Tipo de Invalidación” donde se ingresará por medio de un código el tipo de error por el cual se requiere invalidar el DTE, dicha codificación únicamente podrá ser la establecida en el catálogo **024-** Tipo de Invalidación.

Cuando en campo motivo de invalidación se encuentre lleno con la opción **1** (Error en la Información del Documento Tributario Electrónico a Invalidar) o **3** (Otro), deberá primero generar, transmitir y obtener el sello de recepción del documento que corrige la operación, ya que el evento de invalidación requiere dejar constancia del código de generación del documento correcto. Se exceptúa de esta condición la Nota de Crédito y Comprobante de Liquidación.

Cuando en campo motivo de invalidación se encuentre lleno con la opción **2** (Rescindir de la operación realizada) o el documento a invalidar sea Nota de Crédito o Comprobante de Liquidación, en campo “Código de generación del documento que reemplaza al documento invalidado” deberá ingresar la palabra null.

---

### Invalidación de los documentos relacionados con otro DTE.

Cuando se requiera invalidar un DTE relacionado con otro DTE, deberá tomar en cuenta los procesos que se detallan en la siguiente tabla:

## DTE a Invalidar

| DTE a Invalidar | Proceso | Doc. Relacionado |
| :--- | :--- | :--- |
| F | Si el tipo de invalidación es **1** o **3** deberá generar y transmitir la nueva factura con la que corregirá la operación, para posteriormente invalidar la factura incorrecta, ingresando en el evento de invalidación tanto el código de generación de la factura a invalidar (Factura incorrecta) como el código de generación de la factura que la sustituye (factura correcta).<br>Si el tipo de invalidación es **2** deberá generar y transmitir el evento de invalidación referenciando únicamente el código de generación de la F incorrecta, ingresando en campo "código de generación del documento que reemplaza al invalidado" la palabra null.<br>No hay necesidad de invalidar los documentos relacionados a la factura para invalidarla (Nota de Remisión). | NR |
| CCF | Si el tipo de invalidación es **1** o **3** deberá generar, transmitir y obtener el sello de recepción del nuevo CCF con el que corregirá la operación, para posteriormente realizar proceso de invalidación del CCF incorrecto, ingresando en la estructura del evento de invalidación tanto el código de generación del documento a invalidar (CCF incorrecto) como el código de generación del CCF que sustituye la operación (CCF correcto).<br>Si el tipo de invalidación es **2** deberá generar y transmitir el evento de invalidación referenciando únicamente el código de generación del CCF incorrecto, ingresando en campo "código de generación del documento que reemplaza al invalidado" la palabra null.<br> No hay necesidad de invalidar los documentos que fueron relacionados al CCF para invalidarlo (Nota de Remisión, Documento Contable de Liquidación o Comprobante de liquidación).<br>**Notas:**<br>1. No podrá invalidarse CCF que esté relacionado a una Nota de Crédito o Nota de Débito activa. (primero debe invalidar la Nota de Crédito o Nota de Débito para posteriormente invalidar dicho CCF).<br>2. Si se requiere invalidar un CCF referenciado a un CR podrá realizarse invalidación sin necesidad de invalidar previamente el CR, ya que los ajustes al CR procederán por medio de Nota de Crédito. | NR / DCL / CL |
| NC | Deberá realizar el evento de invalidación referenciando únicamente el código de generación de la NC incorrecta e ingresando en campo "código de generación del documento que reemplaza al invalidado" la palabra **null**. Una vez invalidada la Nota de Crédito incorrecta deberá generar, transmitir y obtener el sello de recepción de una nueva nota de crédito con la que corregirá la operación.<br>Deberá generar y transmitir el evento de invalidación referenciando únicamente el código de generación de la NC incorrecta, ingresando en campo "código de generación del documento que reemplaza al invalidado" la palabra **null**.<br> Para invalidar NC **no** es necesario invalidar los documentos relacionados (CCF, CR). | CCF |
| ND | Deberá generar, transmitir y obtener el sello de recepción de una nueva ND con la que corregirá la operación, posteriormente realizar la invalidación de la ND incorrecta, ingresando en el evento de invalidación tanto el código de generación de la ND a invalidar (incorrecta) como el código de generación de la ND que la sustituye (correcta).<br>Deberá generar y transmitir el evento de invalidación referenciando únicamente el código de generación de la ND incorrecta, ingresando en campo "código de generación del documento que reemplaza al invalidado" la palabra **null**.<br> Para invalidar ND **no** es necesario invalidar los documentos relacionados (CCF, CR). | CCF |
| NR | Deberá generar, transmitir y obtener el sello de recepción de la nueva NR con la que corregirá la operación, posteriormente realizar proceso de invalidación de la NR incorrecta, ingresando en la estructura del evento de invalidación tanto el código de generación del documento a invalidar como el código de generación de la NR que contiene la información correcta.<br>Deberá generar y transmitir el evento de invalidación referenciando únicamente el código de generación de la NR incorrecta, ingresando en campo "código de generación del documento que reemplaza al invalidado" la palabra **null**.<br>No hay necesidad de invalidar los documentos relacionados (Factura o CCF). | F/CCF |
| CR | Si el tipo de invalidación es 1 o 3, deberá generar y transmitir el sello de recepción de un nuevo CR con el que corregirá la operación, posteriormente generar y transmitir el evento de invalidación del CR incorrecto, ingresando en la estructura de dicho evento tanto el código de generación del documento a invalidar (CR incorrecto) como el código de generación del documento que sustituye al anterior (CR correcto).<br>Si el tipo de invalidación es la opción 2, deberá generar y transmitir el evento de invalidación referenciando únicamente el código de generación del CR incorrecto, ingresando en campo 'código de generación del documento que reemplaza al invalidado' la palabra null.<br>No hay necesidad de invalidar los documentos informados en el CR para su invalidación. | N/A sección de relacionados |
| CL | Si el tipo de invalidación es 1 o 3 deberá realizar el evento de invalidación referenciando únicamente el código de generación del CL incorrecto e ingresando en campo "código de generación del documento que reemplaza al invalidado" la palabra null. Una vez invalidado el CL incorrecto deberá generar, transmitir y obtener el sello de recepción de un nuevo CL con el que corregirá la operación.<br>Si el Tipo de invalidación es 2 deberá generar y transmitir el evento de invalidación referenciando únicamente el código de generación del CL incorrecto, ingresando en campo "código de generación del documento que reemplaza al invalidado" la palabra null.<br>Para invalidar CL **no** es necesario invalidar los documentos informados (CCF, NC, ND, FEX). En el momento que se realice la invalidación del CL incorrecto, los documentos informados estarán disponibles para que sean ingresados en un nuevo CL. | N/A sección de relacionados |
| DCL | Si el tipo de invalidación es 1 o 3 deberá generar, transmitir y obtener el sello de recepción para un nuevo DCL con el que corregirá la operación, posteriormente realizará la invalidación del DCL incorrecto, ingresando en la estructura de dicho evento tanto el código de generación del documento a invalidar (DCL incorrecto) como el código de generación del documento que sustituye al anterior (DCL correcto).<br>Si el Tipo de invalidación es 2 deberá generar y transmitir el evento de invalidación referenciando únicamente el código de generación del DCL incorrecto, ingresando en campo "código de generación del documento que reemplaza al invalidado" la palabra null. | N/A sección de relacionados |
| FEX | Si el tipo de invalidación es 1 o 3 deberá generar y transmitir el sello de recepción de la FEX con la que corregirá la operación y posteriormente realizará la FEX incorrecta, ingresando en el evento de invalidación tanto el código de generación de la FEX a invalidar (incorrecta) como el código de generación de la FEX que la sustituye (correcta).<br>Si el Tipo de invalidación es 2 deberá generar y transmitir el evento de invalidación referenciando únicamente el código de generación de la FEX incorrecta, ingresando en campo "código de generación del documento que reemplaza al invalidado" la palabra null. | N/A sección de relacionados |

