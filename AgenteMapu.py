from AgenteIA.AgenteBuscador import AgenteBuscador


class AgenteMapu(AgenteBuscador):

    def __init__(self):
        super().__init__()
        self.estado_inicial = (3, 3, 1)  # Tres pacíficos, tres verdugos, bote en el lado inicial
        self.estado_meta = (0, 0, 0)     # Todos cruzaron el río
        self.tecnica = "amplitud"        # Usamos BFS
        self.add_funcion(self.sucesor)
    
    def sucesor(self, estado):
        pacificos, verdugos, lado_bote = estado
        hijos = []
        movimientos_posibles = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  # Posibles combinaciones de movimientos

        for mov_pacificos, mov_verdugos in movimientos_posibles:
            if lado_bote == 1:  # Bote en lado inicial
                nuevo_estado = (
                    pacificos - mov_pacificos,
                    verdugos - mov_verdugos,
                    0
                )
            else:  # Bote en lado opuesto
                nuevo_estado = (
                    pacificos + mov_pacificos,
                    verdugos + mov_verdugos,
                    1
                )

            # Verificar si el nuevo estado es válido
            if self.es_estado_valido(nuevo_estado):
                hijos.append(nuevo_estado)

        return hijos

    def es_estado_valido(self, estado):
        pacificos, verdugos, _ = estado

        # Verificar si hay un número negativo de pacíficos o verdugos
        if pacificos < 0 or verdugos < 0 or pacificos > 3 or verdugos > 3:
            return False

        # Verificar si los verdugos superan en número a los pacíficos en cualquier lado
        if pacificos < verdugos and pacificos > 0:
            return False

        return True

    def programa(self):
        super().programa()

    def describir_movimiento(self, estado_anterior, estado_actual):
        p_anterior, v_anterior, l_anterior = estado_anterior
        p_actual, v_actual, l_actual = estado_actual

        descripcion = ""

        if l_anterior == 1 and l_actual == 0:  # El bote se mueve hacia la derecha
            if p_anterior > p_actual:
                descripcion += f"Sube {p_anterior - p_actual} pacífico(s) al bote y "
            if v_anterior > v_actual:
                descripcion += f"Sube {v_anterior - v_actual} verdugo(s) al bote y "
            descripcion += "cruza el río hacia la derecha."
        elif l_anterior == 0 and l_actual == 1:  # El bote se mueve hacia la izquierda
            if p_anterior < p_actual:
                descripcion += f"Trae de vuelta {p_actual - p_anterior} pacífico(s) y "
            if v_anterior < v_actual:
                descripcion += f"trae de vuelta {v_actual - v_anterior} verdugo(s) y "
            descripcion += "cruza el río hacia la izquierda."

        return descripcion

    def programa(self):
        super().programa()
        instrucciones = []
        estado_anterior = self.estado_inicial
        for estado in self.acciones[1:]:  # Saltar el estado inicial
            instruccion = self.describir_movimiento(estado_anterior, estado)
            instrucciones.append(instruccion)
            estado_anterior = estado
        
        # Imprimir las instrucciones de forma clara
        print("Instrucciones para ganar el juego:")
        for i, instruccion in enumerate(instrucciones, 1):
            print(f"Paso {i}: {instruccion}")