#rutas
RUTA_BACKEND="/home/cthop/ODTMan/backend"
RUTA_FRONTEND="/home/cthop/ODTMan/frontend"


#funcion para detener ambos servidores con control + c
control_c() {
    echo -e "\n\n Deteniendo servidores..."
    # detener procesos
    kill -9 $BACKEND_PID 2>/dev/null
    kill -9 $FRONTEND_PID 2>/dev/null
    echo "Servidores detenidos correctamente."
    exit 0
}

#captural la señal control + c y ejecutar la funcion control_c
trap control_c SIGINT

echo "=========Iniciando servidores========"

# lanzar backend
cd "$RUTA_BACKEND" || exit
echo -n "Python Ejecutandose desde:"
uv run python3 -c "import sys; print(sys.executable)"
uv run manage.py runserver 0.0.0.0:8000 & BACKEND_PID=$!
echo "PID Django: $BACKEND_PID"

sleep 2

# lanzar frontend
cd "$RUTA_FRONTEND" || exit
pnpm dev --host 0.0.0.0 & FRONTEND_PID=$!
echo "PID de Vite: $FRONTEND_PID"
