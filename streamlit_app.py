import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Tienda de Videojuegos", page_icon="🎮")

# Título y descripción
st.title("🎮 Tienda de Videojuegos")
st.write("Bienvenido a nuestra tienda en línea. Explora nuestra colección de videojuegos y elige tu favorito.")

# Lista de videojuegos disponibles
videojuegos = [
    {"nombre": "The Legend of Zelda: Breath of the Wild", "precio": 59.99},
    {"nombre": "Elden Ring", "precio": 49.99},
    {"nombre": "Cyberpunk 2077", "precio": 39.99},
    {"nombre": "God of War Ragnarök", "precio": 69.99},
    {"nombre": "Hollow Knight", "precio": 14.99}
]

# Selección de videojuego
juego_seleccionado = st.selectbox("Selecciona un videojuego", [juego["nombre"] for juego in videojuegos])

# Mostrar detalles del videojuego seleccionado
juego = next(juego for juego in videojuegos if juego["nombre"] == juego_seleccionado)
st.write(f"**Precio:** ${juego['precio']}")

# Selección de cantidad
cantidad = st.slider("Selecciona la cantidad", 1, 10, 1)
st.write(f"Has seleccionado {cantidad} unidad(es) de {juego_seleccionado}.")

# Cálculo del total
total = cantidad * juego['precio']
st.write(f"**Total a pagar:** ${total:.2f}")

# Botón de compra
if st.button("🛒 Comprar ahora"):
    st.success(f"¡Gracias por tu compra! Has adquirido {cantidad} unidad(es) de {juego_seleccionado}.")
