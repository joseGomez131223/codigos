# main.py - ESP32 (MicroPython)
import network
import socket
import machine
import time
import gc

gc.collect()

# -----------------------------
# CONFIGURACIÓN DE PINES L298N
# -----------------------------
# Cambia los pines si lo deseas. Estos son seguros para ESP32.
IN1_PIN = 14  # Motor A
IN2_PIN = 27
IN3_PIN = 26  # Motor B
IN4_PIN = 25

# Pines ENA / ENB (opcional para PWM velocidad). Si tu módulo L298N tiene jumpers,
# puedes usarlos para habilitar. Si no los usas, deja los pines desconectados.
ENA_PIN = 33  # PWM para Motor A (OUT1/OUT2)
ENB_PIN = 32  # PWM para Motor B (OUT3/OUT4)

IN1 = machine.Pin(IN1_PIN, machine.Pin.OUT)
IN2 = machine.Pin(IN2_PIN, machine.Pin.OUT)
IN3 = machine.Pin(IN3_PIN, machine.Pin.OUT)
IN4 = machine.Pin(IN4_PIN, machine.Pin.OUT)

# PWM setup (frecuencia y duty range 0-1023)
try:
    ENA = machine.PWM(machine.Pin(ENA_PIN), freq=20000)
    ENB = machine.PWM(machine.Pin(ENB_PIN), freq=20000)
    # Velocidad por defecto (max): 1023
    DEFAULT_SPEED = 1023
    ENA.duty(DEFAULT_SPEED)
    ENB.duty(DEFAULT_SPEED)
    pwm_enabled = True
except Exception as e:
    print("PWM no inicializado (deshabilitado):", e)
    pwm_enabled = False

# Asegurar estado inicial: detenido
def stop():
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)

stop()

# Movimientos básicos
def forward():
    IN1.value(1); IN2.value(0)
    IN3.value(1); IN4.value(0)

def backward():
    IN1.value(0); IN2.value(1)
    IN3.value(0); IN4.value(1)

def left():
    # Giro en punto: motor izquierdo al revés, derecho adelante
    IN1.value(0); IN2.value(1)
    IN3.value(1); IN4.value(0)

def right():
    # Giro en punto: motor izquierdo adelante, derecho al revés
    IN1.value(1); IN2.value(0)
    IN3.value(0); IN4.value(1)

# Ajuste de velocidad (0..1023) si PWM está disponible
def set_speed(value):
    if not pwm_enabled:
        return
    v = int(max(0, min(1023, value)))
    ENA.duty(v)
    ENB.duty(v)

# -----------------------------
# CONFIGURAR PUNTO DE ACCESO (AP)
# -----------------------------
ap = network.WLAN(network.AP_IF)
ap.active(True)
# Esperar hasta que esté activo
timeout = 5
t0 = time.time()
while not ap.active() and (time.time() - t0) < timeout:
    time.sleep(0.1)

# Configurar SSID/pass
ap.config(essid="equipo 2", password="123456789", authmode=3)  # WPA2
ip_info = ap.ifconfig()
print("AP activo. SSID: 'equipo 2'  Password: '123456789'")
print("IP:", ip_info)

# ----------------------------------
# PÁGINA WEB HTML
# ----------------------------------
html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Control de Carrito</title>
<style>
body { background:#222; color:white; text-align:center; font-family:Arial; }
button { width:140px; height:55px; margin:10px; font-size:18px; border:none; border-radius:8px; cursor:pointer; }
.fwd { background:#4CAF50; }
.bwd { background:#E91E63; }
.left { background:#2196F3; }
.right { background:#FF9800; }
.stop { background:#9E9E9E; }
.range { width:300px; }
.footer { margin-top:20px; color:#bbb; font-size:12px; }
</style>
</head>
<body>
<h1>Control del Carrito</h1>
<h3>ESP32 + L298N</h3>

<form action="/command" method="get">
<button class="fwd" name="cmd" value="forward">Adelante</button><br>
<button class="left" name="cmd" value="left">Izquierda</button>
<button class="right" name="cmd" value="right">Derecha</button><br>
<button class="bwd" name="cmd" value="backward">Atrás</button><br>
<button class="stop" name="cmd" value="stop">Detener</button>
</form>

<br>
<form action="/speed" method="get">
<label>Velocidad (0-1023):</label><br>
<input class="range" type="range" min="0" max="1023" name="v" value="1023" oninput="out.value=v">
<output name="out">1023</output><br>
<button type="submit">Ajustar velocidad</button>
</form>

<div class="footer">Conéctate al WiFi <b>equipo 2</b> (clave <b>123456789</b>) y abre http://192.168.4.1</div>
</body>
</html>
"""

# ----------------------------------
# SERVIDOR WEB SIMPLE
# ----------------------------------
addr = ('0.0.0.0', 80)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(5)
s.settimeout(None)
print("Servidor web escuchando en 0.0.0.0:80")

def handle_request(conn):
    try:
        request = conn.recv(2048)  # leer petición
        if not request:
            return
        request = request.decode('utf-8', 'ignore')
        # Extraer la primera línea
        first_line = request.split('\r\n')[0]
        parts = first_line.split()
        path = '/'
        if len(parts) >= 2:
            path = parts[1]
        print("Request path:", path)

        # Rutas simples
        if path.startswith('/command'):
            # parsear parámetros (very simple)
            # ejemplo: /command?cmd=forward
            if 'cmd=forward' in path:
                forward()
            elif 'cmd=backward' in path:
                backward()
            elif 'cmd=left' in path:
                left()
            elif 'cmd=right' in path:
                right()
            elif 'cmd=stop' in path:
                stop()

        elif path.startswith('/speed'):
            # ejemplo: /speed?v=800
            # extraer valor v=
            try:
                if 'v=' in path:
                    idx = path.find('v=')
                    v_str = path[idx+2:]
                    # si hay & u otros params, quedar sólo con números
                    v_str = v_str.split('&')[0]
                    v = int(v_str)
                    set_speed(v)
                    print("Nueva velocidad:", v)
            except Exception as e:
                print("Error parseando velocidad:", e)

        # Responder la página principal siempre
        html_bytes = html.encode('utf-8')
        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: {}\r\nConnection: close\r\n\r\n".format(len(html_bytes))
        conn.sendall(header.encode('utf-8'))
        conn.sendall(html_bytes)
    except Exception as e:
        print("Error manejando petición:", e)
    finally:
        try:
            conn.close()
        except:
            pass

# Bucle principal
try:
    while True:
        conn, addr = s.accept()
        print("Conexión desde", addr)
        handle_request(conn)
        # limpieza de memoria
        gc.collect()
except KeyboardInterrupt:
    print("Deteniendo servidor...")
finally:
    s.close()
    ap.active(False)
    print("AP desactivado")