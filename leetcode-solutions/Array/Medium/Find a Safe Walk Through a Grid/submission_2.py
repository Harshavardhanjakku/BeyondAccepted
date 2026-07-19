# Problem: Find a Safe Walk Through a Grid
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

from collections import deque

class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        linhas = len(grid)
        colunas = len(grid[0])

        # Já desconta a vida se a casa inicial (0,0) for perigosa (1)
        vida_inicial = health - grid[0][0]
        
        # Se já morreu na largada, nem tenta
        if vida_inicial <= 0:
            return False

        # Fila de duas pontas (Deque) usada na Busca em Largura (BFS 0-1)
        fila = deque()
        fila.append((0, 0, vida_inicial))

        # Matriz de visitados para não ficar andando em círculos (evita recálculo e subproblemas infinitos)
        visitados = set()
        visitados.add((0, 0))

        # Cima, Baixo, Esquerda, Direita
        direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while len(fila) > 0:
            # Tira o primeiro elemento da fila
            r, c, vida_atual = fila.popleft()

            # Condição de parada: chegou no destino vivo!
            if r == linhas - 1 and c == colunas - 1:
                return vida_atual >= 1

            for dr, dc in direcoes:
                nr = r + dr
                nc = c + dc

                # Verifica se o vizinho tá dentro do mapa e se ainda não foi visitado
                if 0 <= nr < linhas and 0 <= nc < colunas and (nr, nc) not in visitados:
                    
                    # Calcula como ficaria a vida se for pra essa casa
                    nova_vida = vida_atual - grid[nr][nc]

                    # Só continua se a vida não zerar 
                    if nova_vida >= 1:
                        visitados.add((nr, nc))

                        # LÓGICA DO BFS 0-1 (Estratégia parecida com Dijkstra Guloso):
                        if grid[nr][nc] == 0:
                            # Custo 0: Não gasta vida. Joga pro INÍCIO da fila pra explorar logo!
                            fila.appendleft((nr, nc, nova_vida))
                        else:
                            # Custo 1: Gasta vida. Joga pro FINAL da fila.
                            fila.append((nr, nc, nova_vida))

        return False
