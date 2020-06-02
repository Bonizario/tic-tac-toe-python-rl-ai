"""Verifica se partida terminou---------------------------------------------"""      
def game_over(vet_board,dim,x,o):
    mat_board = np.reshape(vet_board,(dim,dim))
    
    #verifica linhas
    for player in (x,o):
        for i in range(dim):
            if mat_board[i,:].sum() == player*dim: #verifica linhas
                winner = player
                return True, winner
            elif mat_board[:,i].sum() == player*dim: #verifica colunas
                winner = player
                return True, winner
                
    #verifica diagonais
    for player in (x,o):
        if np.sum(np.diag(mat_board)) == player*dim: #diagonal principal
            winner = player
            return True, winner
        elif np.sum(np.diag(np.fliplr(mat_board))) == player*dim: #diagonal oposta
            winner = player
            return True, winner
    
    #verifica se deu empate
    if np.all((mat_board==0) == False): #todos os campos não estão vazios?
        winner = None
        return True, winner
    
    #Jogo ainda não terminou
    winner = None
    return False, winner
            
def draw_board(vet_board,x,o,dim):
    mat_board = np.resize(vet_board,(dim,dim))
    
    print(" ", end="")
    print("  1", end="  ")
    print(" 2", end="  ")
    print(" 3", end="  ") 
    print("")
    print("-------------")
    
    for i in range(dim):
        print(str(i+1), end=" ")
        for j in range(dim):
            print(" ", end="")
            if mat_board[i,j] == x:
                print("X  ", end="")
            elif mat_board[i,j] == o:
                print("O  ", end="")
            else:
                print("-  ", end="")
        print("")    
