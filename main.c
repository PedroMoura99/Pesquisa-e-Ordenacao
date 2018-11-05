#include <stdio.h>
#include <stdlib.h>

// Estrutura do nó da Arvore Trie
struct no {
    struct no *chave[27]; // Vetor de indexação
    struct no *pai; // Nó superior
    int filhos; // Número de filhos
};

typedef struct no nodo;

// Gerador da Arvore
nodo *arvore_trie( void ){
    nodo *raiz; // Ponteiro inicial
    int i; // Contador

    // Verifica se existe memoria para a criação da arvore
    if(!(raiz =(nodo *)malloc(sizeof(nodo)))){
        return NULL;
    }
    raiz->pai = NULL; // Defini o nó superior como nulo
    for(i = 0; i < 27; i++){
        raiz->chave[i] = NULL; // Inicialisa o vetor de indexação com todas a posições nulas
    }
    raiz->filhos = 0; // Seta o número de filhos para zero

    return raiz;
}

// Inserindo uma palavra na arvore
int inseri_arvore_trie(nodo *raiz, char *palavra){
    int i, val;
    nodo *aux, *pivo;

    pivo = raiz; // Aponta o pivor para a raiz

    // Inseção da palavra
    for(i = 0; palavra[i] != '\0'; i++){
        val = palavra[i] - 'a'; // Encontra o valor de indexação do caractere
        if(pivo->chave[val] != NULL){ // Verifica se o caractere ja foi utilizado
            pivo = pivo->chave[val]; // Se sim passa para o próximo
        }
        else { // Se não:
            aux = arvore_trie(); // Cria um no
            if (aux == NULL){ // Verifica se foi criado com sucesso
                return 0;
            }
            pivo->chave[val] = aux; // Liga o no ressem criado a arvore
            aux->pai = pivo; // Define o antecessor do nó ressem criado
            pivo->filhos++; // Almenta a quantudade de filhos do nó pai
            pivo = aux; // Avança para o novo nó
        }
    }

    if(pivo->chave[26] == NULL){
        pivo->chave[26] = (nodo *) 1;
        pivo->filhos++;
    }

    return 1; // Retorna 1 se tudo tiver dado certo
}

// Pega informações de uma palavra na arvore
nodo *get_arvore_trie(nodo *raiz, char *palavra){
	int i = 0, val;
	nodo *pivo;

	pivo = raiz; // Aponta o pivo para a raiz

	if (palavra[i] == '\0'){ // Verifica se existe uma palavra para pesquisar
		return NULL;
	}
	else {
        // Percorre a arvore seguindo a palavra
		while((palavra[i] != '\0') && (pivo != NULL)){
			val = palavra[i] - 'a'; // Encontra o valor de indexação da palavra
			pivo = pivo->chave[val]; // Avança na arvore
			i++; // Incrementa
        }
	}

	return pivo; // Retorna o nó onde se encontra a palavra
}

// busca na arvore
int busca_trie(nodo *raiz, char *palavra){
    nodo *aux;
    aux = get_arvore_trie(raiz, palavra); // Pega informações da palavra
    if((aux) && (aux->chave[26])){ // verifica se ela está na arvore
        return 1;
    }
    return 0;
}

// remove uma palavra da arvore
int remove_trie(nodo *raiz, char *palavra){
    int i;
    nodo *aux, *pai;

    aux = get_arvore_trie(raiz, palavra); // pega informações da palavra
    if((aux) && (aux->chave[26])){ // retira a palavra da arvore
        aux->chave[26] = NULL;
        aux->filhos--;
        while(aux->pai && (!aux->filhos)){
            pai = aux->pai;
            i = 0;
            while((pai->chave[i] != aux) && (i < 26)){
                i++;
            }
            pai->chave[i] = NULL;
            pai->filhos--;
            if(aux->pai){
                free(aux);
            }
            aux = pai;
        }
    }
    else{
        return 0;
    }
    return 1;
}

int main(){

    int controle = 100;
    char palavra[100];
    nodo *raiz;
    raiz = arvore_trie(); // cria a arvore
    while(controle){ // menu
        system("cls");
        printf("Escolha uma opcao:\n");
        printf("Inserir uma palavra (1)\n");
        printf("Remover uma paravra (2)\n");
        printf("Buscar uma palavra (3)\n");
        printf("Sair (0)\n");
        printf("Digite: ");
        scanf("%i", &controle);
        printf("\n");
        if(controle == 1){
            system("cls");
            printf("Digite a palavra: ");
            scanf("%s", &palavra);
            if(inseri_arvore_trie(raiz, palavra)){
                printf("\nInserido com sucesso.\n");
                system("pause");
            }
        }
        else if(controle == 2){
            system("cls");
            printf("Digite a palavra: ");
            scanf("%s", &palavra);
            if(remove_trie(raiz, palavra)){
                printf("\nRemovido com secesso.\n");
                system("pause");
            }
        }
        else if(controle == 3){
            system("cls");
            printf("Digite a palavra: ");
            scanf("%s", &palavra);
            if(busca_trie(raiz, palavra)){
                printf("\nPalavra encontrada.\n");
                system("pause");
            }
            else{
                printf("\nPalavra nao encontrada.\n");
                system("pause");
            }
        }
    }
    return 0;
}
