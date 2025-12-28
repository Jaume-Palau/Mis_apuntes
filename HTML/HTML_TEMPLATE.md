# Este es un documento para tener una platilla de lo básico.

## Webs de plantillas:
- https://www.w3schools.com/html/default.asp
- https://htmlboilerplates.com/
- https://github.com/h5bp/html5-boilerplate#quick-start

## Etiquetas básicas:

- h1 a h6 → títulos
- p → párrafos
- a → enlaces
- img → imágenes
- ul, ol, li → listas
- div → contenedor genérico
- span → contenedor en línea
- blockquote → citas largas
- cite → origen de la cita
- code → código literal
- strong → importancia
- em → énfasis
- br → salto de linea

## Etiquetas semánticas de estructura:

- article → Define partes con suficiente imoprtancia como para considerarse una   
entidad destacable con informafion a su alrededor

- nav → Lista de enlaces que normalmente sera el menu de navegacion de la web

- header → Zona común de la parte superior de nuestra web

- footer → Zona común de la parte inferior de nuestra web

- section → Para agrupar unaseccion de nuestro documento web

- main → Para agrupar el conjunto de contenido de nuestra pagina

- aside → Lo opuesto a main, para agrupar lo mas irrelevante


## Etiquetas semámticas de texto:

Dan relevancia a partes de texto, sirven para el SEO y Accesibilidad. Normalmente son etiquetas de línea

- strong → Dar mas relevancia al texto

- em → Dar mas énfasis a partes del texto

- time → Marcar fechas o horas

- address → Indicar la forma de contacto o dirección 

## Atajos útiles de Emmet (HTML)

### Plantilla base
!
→ Genera la estructura HTML5 completa

### Clases e IDs
- div.container
- #main

<div class="container"></div>
<div id="main"></div>

### Anidar elementos
header>nav>ul>li

### Elementos hermanos
header+main+footer

### Multiplicar elementos
li*5

### Texto dentro de la etiqueta
p{Hola mundo}

### Atributos
- a[href="#"]
- img[src="img.jpg" alt="imagen"]

### Estructura típica de página
header>nav+main+footer

### Listas con clase
ul>li.item*3
