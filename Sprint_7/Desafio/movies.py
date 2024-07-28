import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# carregar chave API 
tmdb_api_key = os.getenv('TMDB_API_KEY')

# URL base da API do TMDb
base_url = "https://api.themoviedb.org/3"

# Função para converter objetos para dicionários
def convert_to_dict(obj):
    if hasattr(obj, '__dict__'):
        return obj.__dict__

# Função para obter detalhes do filme e do ator principal
def get_movie_details(movie_id):
    details_url = f"{base_url}/movie/{movie_id}"
    credits_url = f"{base_url}/movie/{movie_id}/credits"

    details_response = requests.get(details_url, params={'api_key': tmdb_api_key})
    credits_response = requests.get(credits_url, params={'api_key': tmdb_api_key})

    details_response.raise_for_status()
    credits_response.raise_for_status()

    details = details_response.json()
    credits = credits_response.json()

    main_actor = credits['cast'][0]['name'] if credits['cast'] else "N/A"
    
    # Encontrar o diretor na seção de "crew"
    director = next((member['name'] for member in credits['crew'] if member['job'] == 'Director'), "N/A")

    movie_data = {
        "id": details['id'],
        "title": details['title'],
        "release_date": details['release_date'],
        "original_language": details['original_language'],
        "overview": details['overview'],
        "popularity": details['popularity'],
        "vote_average": details['vote_average'],
        "vote_count": details['vote_count'],
        "main_actor": main_actor,
        "director": director
    }
    
    return movie_data

# Função para buscar dados do TMDb
def fetch_action_adventure_movies():
    tmdb_data = []

    # Definindo osIDs dos gêneros Ação e Aventura
    action_genre_id = 28
    adventure_genre_id = 12

    # URL de descoberta de filmes
    discover_url = f"{base_url}/discover/movie"

    # Buscar filmes de ação e aventura
    page = 1
    while True:
        try:
            response = requests.get(discover_url, params={
                'api_key': tmdb_api_key,
                'with_genres': f"{action_genre_id},{adventure_genre_id}",
                'primary_release_date.gte': '2010-01-01',
                'primary_release_date.lte': '2020-12-31',
                'page': page
            })
            response.raise_for_status()

            movie_data = response.json().get('results', [])
            if not movie_data:
                break
            
            for movie in movie_data:
                try:
                    movie_details = get_movie_details(movie['id'])
                    tmdb_data.append(movie_details)
                except Exception as e:
                    print(f"Erro ao obter detalhes para o filme com ID {movie['id']}: {e}")

            print(f"Página {page} de filmes obtida com sucesso.")
            page += 1

            if len(tmdb_data) >= 100:
                yield tmdb_data[:100]
                tmdb_data = tmdb_data[100:]

        except Exception as e:
            print(f"Erro ao obter filmes na página {page}: {e}")
            break

    if tmdb_data:
        yield tmdb_data