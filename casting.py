def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass

    precio = (int(input()))
    print("Precio:", precio)
    descuento = (float(input()))
    print("Descuento:",descuento)
    precio_con_descuento = (float(precio - descuento))
    print("Precio con descuento:",precio_con_descuento)
    cantidad = (int(input()))
    print("Total:",(float(precio_con_descuento * cantidad)))
