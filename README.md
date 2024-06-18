# UBA_TP_IDS
Sitio web de hostería.

## Integrantes

#### Referente Docs
- Lucas Mancini

#### Referentes base de datos
- Joaquín Basile
- Lucas de la Peña

#### Referentes Forms
- Mateo Parrado

#### Referentes vistas
- Melanie Belen Garcia Lapegna
- Mirko Uriel Sáenz Valiente
- Ivan Colombo

#### Referentes API
- Tomas Ordorica
- Jose Piñeiro Sanchez
- Maxi Fittipaldi


## Ejecutar

### En docker (recomendado)
Ejecutar:
```
sudo docker buildx build -t ids_img .
sudo docker compose up # (-d para dejarlo en background)
```
y debería levantar el servicio de api (puerto 5000) y la parte web (puerto 8080)

#### Explicación
El Dockerfile contiene una imagen de debian con algunas dependencias que,
tanto la api como el servidor web utilizan. Sí, hay una imagen para ambas apps, y eso es
así para que el proyecto no sea tan pesado.

Luego el compose.yaml inicia el servicio web y el api con la red en host, de lo contrario,
habría falta de comunicación entre contenedores y se necesitaría una configuración más extensa.
Los archivos dentro de [web](web/) y [api](api/) se montan vía monturas bind, es decir, los
contenedores leen la aplicación del host y la imagen no necesita ser reconstruida por cambio.

### En host
El único requisito es tener instalado pipenv.
Podes usar **init.sh** o **pipenv install** en
ambas apps.
En caso de ser necesario instalar python 3.11.9,
ejecutar los siguientes comandos (debian):

```
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt update
$ sudo apt install python3.11
```

## Documentación y ayuda
[Descripción proyecto](https://docs.google.com/document/d/1mb9RKfqSAJfvnvmGMwoJfzLQW7B9jlwTmD1y_JOt8-A/edit?usp=sharing)
[Backlog-hitos](https://docs.google.com/document/d/1R4y3L9an2E5DqzXhLTx_3DH_y7Y3vlkNs5IGeWhuxcY/edit?usp=sharing)
[Diagrama de Equipos de Trabajo](https://lucid.app/lucidchart/0f51fec8-f261-472e-b8aa-eda9c11165a8/edit?viewport_loc=1336%2C-162%2C3282%2C1461%2C0_0&invitationId=inv_fb9dc69a-cd15-4fab-ba45-fca009497494)

[Flask docs](https://flask.palletsprojects.com/en/3.0.x/)
[Leaflet](https://leafletjs.com/examples.html)
[GIT cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf)
[GitHub SSH setup](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

