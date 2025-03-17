import random

def greedy_local_search(emisoras, estados_necesarios):

    emisoras_sel = []
    estados_no_cubiertos = estados_necesarios[:]            # Copiamos la lista para evitar modificar la original.

    while len(estados_no_cubiertos) > 0:
        emisoras_disp = []                                  # Lista para las emisoras que cubren al menos un estado descubierto.
        
        for emisora in emisoras:
            for estado in emisoras[emisora]:                # Un for para comprobar cada estado que la emisora en cuestión cubre:
                if estado in estados_no_cubiertos:
                    emisoras_disp.append(emisora)
                    break                                   # Cuando es confirmado que la emisora cubre un estado sin descubrir, pasamos a la siguiente emisora del grupo.
        
        if len(emisoras_disp) == 0: break

        emisora_sel = random.choice(emisoras_disp)          # La elección de la emisora en cuestión la hago al azar.
        emisoras_sel.append(emisora_sel)

        for estado in emisoras[emisora_sel]:                # A partir de aquí se eliminan los estados que ya están cubiertos de la lista de estados_no_cubiertos.
            if estado in estados_no_cubiertos:
                estados_no_cubiertos.remove(estado)

        print(f"[LOCAL] Emisora seleccionada: {emisora_sel}. Cubre los estados: {emisoras[emisora_sel]}. Quedan un total de: {len(estados_no_cubiertos)} estados sin cubrir.")
        
    return emisoras_sel