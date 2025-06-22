def simular_comportamiento(temperatura, estacion, usuario_tipo):
    """
    Devuelve el comportamiento del pato según el tipo de usuario, la temperatura del hábitat y la estación del año.
    """
    if usuario_tipo != "premium":
        return "Funcionalidad exclusiva para usuarios premium"
    if temperatura == "fría":
        return "El pato está nadando para entrar en calor."
    elif temperatura == "templada":
        return "El pato emite su sonido característico."
    elif temperatura == "caliente":
        if estacion == "verano":
            return "El pato vuela alto en verano."
        else:
            return "El pato vuela bajo."

    return "Condiciones desconocidas"

