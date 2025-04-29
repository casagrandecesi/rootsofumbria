import requests
from bs4 import BeautifulSoup

base_url = "https://dati.regione.umbria.it/dataset/?page="

all_datasets = []

# La paginazione va da 1 a 22
for page_num in range(1, 23):
    url = f"{base_url}{page_num}"
    print(f"Elaborazione della pagina: {url}")
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Errore nel download della pagina {page_num} (status code: {response.status_code})")
        continue  # Passa alla pagina successiva se c'è un errore
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Trova tutti gli h2 con classe "dataset-heading"
    dataset_items = soup.find_all("h2", class_="dataset-heading")
    
    if not dataset_items:
        print(f"Nessun dataset trovato nella pagina {page_num}")
        continue
    
    for item in dataset_items:
        title = item.get_text(strip=True)
        if title and title not in all_datasets:
            all_datasets.append(title)

print(f"\nTotale dataset trovati: {len(all_datasets)}")
for idx, title in enumerate(all_datasets, start=1):
    print(f"{idx}. {title}")