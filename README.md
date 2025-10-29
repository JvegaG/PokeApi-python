# PokeApi - Python

Template de Api hecha en python con Clean Architecture basado en la data del api de pokemon _(ver https://pokeapi.co/)_

## Requerimientos

- **Instalacion de python:** Es necesario y obligatorio tener instalado python en tu computador, para esto sigue los pasos en esta web: https://www.python.org/downloads/
- **Docker (opcional):** En caso de seguir al pie de la letra esta guia, deberas instalar docker (no es estrictamente necesario), https://www.docker.com/

## Notas - Creación de propio entorno virtual (Opcional)

Cuando se trabaja en Node al instalar paquetes modificamos el archivo package.json y al ejecutar `npm install ` se crea la carpeta **node_modules** con los packages de nuestro proyecto.

Si queremos lograr algo similar en nuestro proyecto de python debemos configurar un entorno virtual, creamos la carpeta venv:

```bash
python -m venv venv
```

Activamos el entorno

```bash
source venv/bin/activate #bash

venv\Scripts\activate #powershell
```

Como te das cuenta que esta activo el entorno, porque en la terminal te aparecera (venv) en la ruta actual en la que te encuentras.

Con esto podras instalar tus modulos de terceros de python solamente en el entorno de tu proyecto y no en el entorno global donde tienes instalado python. Ejecutando algo tan simple como lo siguiente podras ver la _magia_ :sunglasses:.

```bash
pip install fastapi fastapi-injector uvicorn
```

A partir de aqui en adelante todos los comandos que hagas los ejecutaras en la terminal que tenga activo tu entorno virutal.
Usualmente en los proyectos de python se visualiza un archivo **requirements.txt** que contiene los modulos necesarios para el proyecto, si quieres generarlo o actualizarlo de acuerdo a las instalaciones que hayas hecho puedes ejecutar el siguiente comando.

```bash
pip freeze > requirements.txt
```

Si en algún momento deseas desactivar esto, cierras la terminal o ejecutas el comando

```bash
deactivate
```

**¿Porque usar ./venv?** Si no hacemos estas practicas recomendadas vamos a llegar a instalar paquetes o librerias en la ubicacion de la instalacion global de python, al hacer eso podemos llegar a tener los siguientes inconvenientes:

- Versiones incompatibles de las librerias (proyecto requiere v2 pero en mi global tengo la v1)
- Dificil replicar el entorno en otra maquina o servidor.
- Accidentalmente se actualizan dependencias en otro proyecto que afecta al tuyo.
- Requiere permisos de administrador (sudo) en algunas ocasiones.

Basicamente estas contaminando tu instalacion global de python, es por eso que se recomienda usar un entorno virtual de python (./venv). Con ello aislas tu proyecto y mantienes el conjunto de librerias con las versiones que tu necesitas para el mismo.

## Instalacion de módulos

En el archivo ./requirements.txt se tiene todos los modulos necesarios para el proyecto. Para instalar los modulos ejecutar el comando:

```bash
pip install -r requirements.txt
```

## Ejecución de proyecto

Asegurate de colocar las variables de entorno correctas en tu archivo **.env.{Enviroment}**. De acuerdo a eso puedes ir cambiando tus variables como las necesites. Para levantar el proyecto se debe ejecutar el comando:

```bash
Env=dev python main.py
```

## Testing

## Recomendaciones

## Bibliografía Util
