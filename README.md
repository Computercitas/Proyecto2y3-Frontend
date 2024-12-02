# Integración del Frontend de los Proyectos 2 y 3


Este repositorio combina las funcionalidades de los Proyectos 2 y 3 en una única aplicación web usando **React**, **Vite** y **TypeScript**. Cada proyecto está implementado como rutas independientes, ofreciendo una navegación fluida entre ellos. A continuación, se describe cómo se estructuró y desarrolló el frontend:

### 1. **Estructura del Proyecto**
Se definió una arquitectura modular para separar las funcionalidades:
- **Home:** Una página inicial que permite al usuario navegar hacia los proyectos mediante un diseño limpio e intuitivo.
- **Proyecto 2:** Implementación de la funcionalidad de búsqueda basada en el índice invertido, mostrando resultados interactivos.
- **Proyecto 3:** Búsqueda multimedia que permite realizar consultas de imágenes y retorna el top-k de los resultados más parecidos.

### 2. **Uso de React Router**
Se utilizó **React Router** para gestionar las rutas entre las páginas:
- `/`: Página principal con opciones para acceder a los proyectos.
- `/proyecto2`: Ruta que carga el frontend del Proyecto 2 mediante un iframe en el puerto `5174`.
- `/proyecto3`: Ruta que carga el frontend del Proyecto 3 mediante un iframe en el puerto `5176`.

El puerto general del frontend conjunto es el **5175**, permitiendo centralizar las rutas y funcionalidades.

### 3. **Diseño Interactivo**
- Se diseñó la página principal con botones estilizados que dirigen a cada proyecto.
- Se implementó un estilo uniforme utilizando **CSS** personalizado para mantener un diseño profesional.
- En el Proyecto 3, los resultados se muestran en una tabla interactiva con imágenes y metadatos como la distancia KNN y el tiempo de consulta.

### 4. **Implementación de Funcionalidades**
#### Proyecto 2
- El Proyecto 2 se integró mediante un iframe que apunta a su puerto específico (`http://localhost:5174`).
#### Proyecto 3
- El Proyecto 3 se integró mediante un iframe que apunta a su puerto específico (`http://localhost:5176`).

### 5. **Ventajas de la Integración**
- Centraliza el acceso a ambos proyectos en una sola aplicación.
- Proporciona una experiencia de usuario consistente y profesional.
- Facilita la navegación y permite la reutilización de componentes comunes.

### 6. **Tecnologías Usadas**
- **React + Vite:** Para el desarrollo rápido y eficiente del frontend.
- **TypeScript:** Para un desarrollo más robusto con tipado estático.
- **CSS:** Para un diseño atractivo y profesional.
- **React Router:** Para la navegación entre los proyectos.


### 7. **Enlaces de cada proyecto**
- [Repositorio del Proyecto 2](https://github.com/Dateadores/Proyecto2)
- [Repositorio del Proyecto 3](https://github.com/Dateadores/Proyecto3)

### 8. **¿Cómo probarlo?**

#### Ejecutar Proyecto 2

Para ejecutar el frontend, primero entrar a la carpeta `Proyecto2`:

```bash
cd Proyecto2
```

Luego, utilizar los siguientes comandos en la terminal:

```bash
npm i
```

```bash
npm run dev
```

#### Ejecutar Proyecto 3

Ahora entramos a la carpeta `Proyecto3`, para esto simplemente abrir otra terminal sin borrar la anterior:

```bash
cd Proyecto3
```

Luego, utilizar los siguientes comandos en la terminal:

```bash
npm i
```

```bash
npm run dev
```

#### Ejecutar la combinación del Frontend

Ahora entramos a la carpeta `frontend-combinado`, para esto simplemente abrir otra terminal sin borrar la anterior:

```bash
cd fc
```

y luego:

```bash
cd frontend-combinado
```

Luego, utilizar los siguientes comandos en la terminal:

```bash
npm i
```

```bash
npm run dev
```

### Autores

|                                                                             | Nombre                                                                   | GitHub                                                     |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------- |
| ![Mariel](https://github.com/MarielUTEC.png?size=50)                        | [Mariel Carolina Tovar Tolentino](https://github.com/MarielUTEC)         | [@MarielUTEC](https://github.com/MarielUTEC)               |
| ![Noemi](https://github.com/NoemiHuarino-utec.png?size=50)                  | [Noemi Alejandra Huarino Anchillo](https://github.com/NoemiHuarino-utec) | [@NoemiHuarino-utec](https://github.com/NoemiHuarino-utec) |
| <img src="https://github.com/Sergio-So.png?size=50" width="50" height="50"> | [Sergio Sebastian Sotil Lozada](https://github.com/Sergio-So)            | [@Sergio-So](https://github.com/Sergio-So)                 |
| ![Davi](https://github.com/CS-DaviMagalhaes.png?size=50)                    | [Davi Magalhaes Eler](https://github.com/CS-DaviMagalhaes)               | [@CS-DaviMagalhaes](https://github.com/CS-DaviMagalhaes)   |
| ![Jose](https://github.com/EddisonPinedoEsp.png?size=50)                    | [Jose Eddison Pinedo Espinoza](https://github.com/EddisonPinedoEsp)      | [@EddisonPinedoEsp](https://github.com/EddisonPinedoEsp)   |
