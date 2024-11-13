# Cliente y Servidor TCP en Python

Este proyecto implementa un sistema de comunicación cliente-servidor TCP utilizando Python, donde el servidor procesa mensajes y responde con versiones en mayúsculas de los mismos.

## 🚀 Características

- Servidor TCP en localhost:5000
- Respuestas en mayúsculas
- Manejo de desconexiones
- Logging detallado
- Pruebas documentadas

## 📋 Requisitos Previos

- Python 3.6 o superior
- Sistema operativo: Windows/Linux/MacOS

## 🔧 Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

## 💻 Uso

### Iniciar el Servidor

```bash
python3 servidor.py
```

### Iniciar el Cliente

```bash
python3 cliente.py
```

## 📝 Pruebas Realizadas

### Prueba 1: Envío de Mensaje Normal
![Prueba de mensaje normal](/img/1.png)
[Prueba de mensaje](/img/2.png)
[Prueba de mensaje](/img/3.png)

Las imagenes muestran:
- Servidor iniciado correctamente en localhost:5000
- Cliente conectado exitosamente
- Mensaje "hola servidor" enviado
- Respuesta "HOLA SERVIDOR" recibida
- Logs detallados de la comunicación

### Prueba 2: Prueba de Desconexión
![Prueba de desconexión](/img/4.png)

Se puede observar:
- Envío del comando "DESCONEXION"
- Servidor registra la solicitud
- Cliente se desconecta correctamente
- Logs muestran el proceso completo

### Prueba 3: Verificación del Servidor
![Servidor activo](/img/3.png)
![Nueva conexión](/img/4.png)

Las imágenes demuestran:
- Servidor manteniéndose activo
- Listo para aceptar nuevas conexiones
- Sistema de logging funcionando correctamente

## ✅ Verificación de Requisitos

Se han completado todas las funcionalidades requeridas:
- [x] Servidor escuchando en localhost:5000
- [x] Conexión exitosa del cliente
- [x] Procesamiento de mensajes normales
- [x] Conversión a mayúsculas
- [x] Manejo correcto de desconexión
- [x] Servidor permanece activo para nuevas conexiones

## 🛠️ Estructura del Proyecto
```
proyecto/
├── README.md
├── servidor.py
├── cliente.py
└── img/
    ├── 1.png
    ├── 2.png
    ├── 3.png
    └── 4.png
```

## ⚙️ Configuración

El servidor usa por defecto:
- Host: localhost
- Puerto: 5000

## 💡 Uso del Cliente

1. Enviar mensajes normales:
   - Escribe cualquier texto y presiona Enter
   - Recibirás el mismo mensaje en mayúsculas

2. Desconexión:
   - Escribe "DESCONEXION" para cerrar la conexión
   - El cliente se cerrará automáticamente

## 👨‍💻 Desarrollo

El proyecto está desarrollado siguiendo las mejores prácticas:
- Código comentado y estructurado
- Manejo de errores robusto
- Logging para debugging
- Clean code principles

## ✨ Mejoras Futuras

- [ ] Implementar GUI
- [ ] Soporte para múltiples clientes simultáneos
- [ ] Configuración mediante archivo externo
- [ ] Sistema de autenticación

## 📄 Licencia

Distribuido bajo la licencia MIT. Ver `LICENSE` para más información.
