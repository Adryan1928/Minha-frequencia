# Minha-frequencia
## 📖 Introdução
Esse é um projeto feito em 2022 para a secretaria do Campus PDF quando eu era bolsita de lá.

### Contextualização e o problema
Todas as secretarias de escolas devem informar a presença de cada aluno no sistema do governo(Isso é feito a cada 2 meses), porque é através dessa frequência que o estudante está apto a permanecer ou não no programa do bolsa família, caso ele receba.

E o problema? Esse dados são inseridos totalmente de forma manual. É TERRÍVEL.

**Antes era feito da seguinte forma:**
A servidora imprime 1 planilha para cada mês, em cada planilha vai ter todos os alunos matriculados na escola e sua respectiva frequência daquele mês.

EX:
O sistema pede para informa a frequência de Janeiro e Fevereiro de 100 alunos daquela escola que possuem direito ao bolsa família.

Na escola possuem 1000 alunos (No IFRN PDF tinha mais de 1000), então nas planilhas imprimidas pela a servidora de Janeiro e Fevereiro vão ter 1000 alunos(Umas 6 folhas), mas só preciso daqueles 100 que o sistema pede.

Então é preciso ir procurando 1 a 1 em ambas as planilhas(Que eram 6 folhas cada, após ser imprimido) e informando no sistema (Um trabalho que levava incríveis 4 dias para serem feitos, e olha que tinha 2 bolsistas - um de manhã(EU) e outro á tarde).

### Nova solução
Visto que eu sou preguiçoso e era muito trabalho para mim, então resolvi desenvolver essa aplicação.

O que ela faz? Ela pega as 2 planilhas geradas(Janeiro e Fevereiro, mas que podem ser qualquer outro mês ou nome, desde que siga o padrão que está neste repositório), e uma 3º planilha denominada "Lista do sistema.xlsx", essa é a lista como está lá no sistema(ordem dos nomes e quais precisam ser informados), com isso, cruza esses dados e junta em uma única planilha apenas aqueles 100 alunos que o sistema pede(Como foi o exemplo citado, mas pode ser quantos forem necessários). Em cada linha da planilha vai ter o nome do aluno, presença do primeiro mês e a prsença do segundo mês.

Agora basta pegar essa planilha e ir inserindo no sistema.

Qual foi o ganho de produção real? A tarefa passou de ser realizada em 4 dias para ~30min.

Poupou muito esforço por parte dos bolsista, além de diminuir o error humano e alguém ser prejudicado por isso(Isso nunca aconteceu, só deixando claro).

**Feito com:** Pandas e Tkinter.

Documentação:

- [Pandas](https://pandas.pydata.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)

## ⚙️ Rodar

Para rodar o projeto siga os sequintes passos:

```shell
# Baixe as dependências
pip install -r requirements.txt

# Agora só rodar
py frequencia.py
```

Ou baixe o .exe e rode.

## ✅ Final

Esse sistema ainda é utilizado a cada 2 meses e consegue cumprir com seu objetivo, que é acelerar o processo de informar a frequência de cada aluno no sistema do governo.

Não ficou muito bonito, mas foi meu primeiro grande problema resolvido com programação.👍😁

OBS: Acho que vai ter erro de gramática no meio, mas estou com preguiça de revisar o texto e também acho que ninguém vai ler isso.