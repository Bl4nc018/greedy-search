from greedy_local_search import greedy_local_search
from greedy_global_search import greedy_global_search

if __name__ == "__main__":
    
    emisoras = {
        "kone": ["ID", "NV", "UT"], 
        "ktwo": ["WA", "ID", "MT"], 
        "kthree": ["OR", "NV", "CA"], 
        "kfour": ["NV", "UT"], 
        "kfive": ["CA", "AZ"], 
        "ksix": ["NM", "TX", "OK"],
        "kseven": ["OK", "KS", "CO"], 
        "keight": ["KS", "CO", "NE"], 
        "knine": ["NE", "SD", "WY"], 
        "kten": ["ND", "IA"], 
        "keleven": ["MN", "MO", "AR"], 
        "ktwelve": ["LA"], 
        "kthirteen": ["MO", "AR"], 
        }

    estados_necesarios = []                                 # Lista de todos los estados únicos que deben ser cubiertos
    for emisora_est in emisoras.values():
        for estado in emisora_est:
            if estado not in estados_necesarios:
                estados_necesarios.append(estado)

    print("\n===== Greedy Local Search =====")
    sol_local = greedy_local_search(emisoras, estados_necesarios)
    print("\nLista final de emisoras:", sol_local)

    print("\n===== Greedy Global Search =====")
    sol_global = greedy_global_search(emisoras, estados_necesarios)
    print("\nLista final de emisoras :", sol_global)