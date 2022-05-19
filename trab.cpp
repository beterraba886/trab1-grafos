#include <bits/stdc++.h>
using namespace std;



class Estacao{
    public:
        string nome;
        int x;
        int y;
        Estacao(string nome, int x, int y){
            this->nome = nome;
            this->x = x;
            this->y = y;
        }
};

class Linha{
    public:
        int n;
        string cor;
        vector<Estacao> estacoes;
};

map<string, pair<int, int>> estacoes;
vector<Estacao> adj[25]; //25 numero de estações

void lerEstacoes(){
    ifstream in_estacoes("in_estacoes.txt");
    string nome;
    while(getline(in_estacoes, nome, '>')){
        int x, y;
        in_estacoes >> x >> y;
        estacoes[nome] = {x, y};
        in_estacoes.ignore();
    }
}

void lerLinhas(int linha, string cor, int n){
    ifstream in_linhas;
    for(int i=0; i<n; i++){
        string estacao;
        int x;
        int y;
        getline(in_linhas, estacao, '>');
        //estacao = estacao.substr(1, estacao.size());
        cout << "estacao: " << estacao;
        //x = estacoes[estacao].second.first;
        //y = estacoes[estacao].second.second;
        //Estacao e = new Estacao(estacao, x , y);
        //adj[linha].push_back(new Estacao(estacao, x , y));
    }
    string teste;
    getline(cin, teste);
    cout << "teste: " << teste;
}
int main()
{
    //int linhas[7] = {1, 2, 4, 5, 6, 9, 11};
    lerEstacoes();
    for(int i=0; i<7; i++){
        string nomeLinha;
        string cor;
        int n;
        //cin >> nomeLinha >> cor >> n;
        //lerLinhas(i, cor, n);
    }
            for(auto x : estacoes){
            cout << "nome: " << x.first << " x: " << x.second.first << " y: " << x.second.second << "\n";
        }

}