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

# Função para obter detalhes da série e do ator principal
def get_tv_show_details(tv_show_id):
    details_url = f"{base_url}/tv/{tv_show_id}"
    credits_url = f"{base_url}/tv/{tv_show_id}/credits"

    details_response = requests.get(details_url, params={'api_key': tmdb_api_key})
    credits_response = requests.get(credits_url, params={'api_key': tmdb_api_key})

    details_response.raise_for_status()
    credits_response.raise_for_status()

    details = details_response.json()
    credits = credits_response.json()
    main_actor = credits['cast'][0]['name'] if credits['cast'] else "N/A"

    tv_show_data = {
        "id": details['id'],
        "name": details['name'],
        "first_air_date": details['first_air_date'],
        "original_language": details['original_language'],
        "overview": details['overview'],
        "popularity": details['popularity'],
        "vote_average": details['vote_average'],
        "vote_count": details['vote_count'],
        "main_actor": main_actor
    }
    
    return tv_show_data

# Função para buscar dados do TMDb
def fetch_action_adventure_tv_shows():
    tmdb_data = []

    # IDs dos gêneros Ação e Aventura
    action_genre_id = 10759
    adventure_genre_id = 10765

    # URL de descoberta de séries de TV
    discover_url = f"{base_url}/discover/tv"

    # Buscar séries de ação e aventura
    page = 1
    while True:
        try:
            response = requests.get(discover_url, params={
                'api_key': tmdb_api_key,
                'with_genres': f"{action_genre_id},{adventure_genre_id}",
                'first_air_date.gte': '2010-01-01',
                'first_air_date.lte': '2020-12-31',
                'page': page
            })
            response.raise_for_status()

            tv_show_data = response.json().get('results', [])
            if not tv_show_data:
                break
            
            for tv_show in tv_show_data:
                try:
                    tv_show_details = get_tv_show_details(tv_show['id'])
                    tmdb_data.append(tv_show_details)
                except Exception as e:
                    print(f"Erro ao obter detalhes para a série com ID {tv_show['id']}: {e}")

            print(f"Página {page} de séries de TV obtida com sucesso.")
            page += 1

            if len(tmdb_data) >= 100:
                yield tmdb_data[:100]
                tmdb_data = tmdb_data[100:]

        except Exception as e:
            print(f"Erro ao obter séries de TV na página {page}: {e}")
            break

    if tmdb_data:
        yield tmdb_data