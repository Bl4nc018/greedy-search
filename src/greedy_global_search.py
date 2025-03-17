def greedy_global_search(emisoras, estados_necesarios):

    emisoras_sel = []
    estados_no_cubiertos = estados_necesarios[:]

    while len(estados_no_cubiertos) > 0:
        mejor_emisora = None
        est_mejor_emisora = []                              # Lista para guardar los estados que cubre la "mejor" emisora.

        for emisora in emisoras:
            est_emisora = []                                # Lista que almacena los estados descubiertos por la emisora.
            for estados in emisoras[emisora]:
                if estados in estados_no_cubiertos:
                    est_emisora.append(estados)
            
            if len(est_emisora) > len(est_mejor_emisora):   # En este if se comprueba si la emisora cubre más estados sin descubrir.
                mejor_emisora = emisora
                est_mejor_emisora = est_emisora

        if mejor_emisora is None: break                    

        emisoras_sel.append(mejor_emisora)

        for estados in est_mejor_emisora:                   # Se retiran los estados ya cubiertos de la lista de los estados_no_cubiertos.
            estados_no_cubiertos.remove(estados)

        print(f"[GLOBAL] Emisora seleccionada: {mejor_emisora}. Cubre los estados: {est_mejor_emisora}. Quedan un total de: {len(estados_no_cubiertos)} estados sin cubrir.")

    return emisoras_sel

