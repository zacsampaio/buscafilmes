<div align="center">
    <h1>Projeto Buscaflimes - Django + Python</h1>
</div>

Este foi o meu primeiro projeto utilizando **Django** e **Python**. O objetivo principal foi aprender e praticar essas tecnologias, explorando a criação de uma aplicação web simples que consome uma API de filmes para exibir informações ao usuário.

Ao abrir a aplicação, pode demorar um pouco para carregar, pois a versão gratuita do **Onrender** onde o projeto foi hospedado entra em hibernação após certo tempo de inatividade. Portanto, na primeira vez que você acessar, o tempo de resposta será maior.

## Tecnologias Utilizadas

- **Django**: Framework principal utilizado para o backend da aplicação, facilitando a construção de uma API RESTful.
- **Python**: Linguagem utilizada para o desenvolvimento do projeto.
- **HTML/CSS**: Para estruturação e estilização da interface de usuário.
- **Onrender**: Hospedagem do projeto utilizando o plano gratuito, que pode causar um tempo de inicialização maior devido à hibernação.

## Funcionalidades da Aplicação

A aplicação Buscaflimes permite que o usuário:z

- Pesquise filmes por nome.
- Veja detalhes de cada filme, como título, descrição, e ano de lançamento.
- Navegue por uma interface simples e intuitiva.

## Aprendizados e Melhorias

Neste projeto, pude aprimorar:

- A utilização do Django para o desenvolvimento backend e integração com o frontend.
- O consumo de APIs externas para buscar e exibir dados em tempo real.
- A organização de views e templates no Django para criar páginas dinâmicas e responsivas.
- A hospedagem do projeto em um ambiente de produção, enfrentando e aprendendo a lidar com os desafios da versão gratuita no Onrender.

## Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/zacsampaio/buscafilmes.git
   
2. Navegue até o diretório:
   ```bash
   cd buscafilmes
   
3. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use venv\Scripts\activate
  
4. Acesse a aplicação no navegador através do endereço exibido no terminal.
   ```bash
   pip install -r requirements.txt
   
5. Execute as migrações do banco de dados:
   ```bash
   python manage.py migrate

6. Inicie o servidor Django:
   ```bash
   python manage.py runserver
   
7. Acesse a aplicação no navegador através do endereço exibido no terminal 
