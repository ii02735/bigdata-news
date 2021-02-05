# Projet Big Data Spark - NewsAnalytics

### Contexte
Le but de ce projet est de développer une pipeline big data
qui devra être capable de traiter une forte volumétrie de données à intervalles réguliers (batch).

### API

[Currents API](https://currentsapi.services/en) est une API proposant des données sur des articles de journaux.

### Fonctionnement

Un cluster Spark interroge **périodiquement** l'API Currents API pour récupérer les dernières actualités, pour ensuite les traiter
et les envoyer à **une base de données Mongo**.

Ces données stockées sont ensuite interrogées pour les représenter sur une IHM sous **Streamlit**.

## Configuration

### Configurer le virtualenv si nécessaire
    
La configuration d'un [virtualenv](https://virtualenv.pypa.io/en/stable/) est optionelle. Elle est recommendée si vous utilisez un IDE tel que PyCharm par exemple, afin de mieux isoler les dépendances entre celles du projet et de votre système. 
```sh
# création de l'environnement virtuel
python3 -m venv ./venv #(sur Linux / Mac)
python3 -m venv .\venv #(Sur Windows)
# activation de l'environnement
.\venv\Scripts\Activate.ps1 # (Si vous êtes sur powershell)
.\venv\Scripts\Activate.bat # (Sur tout autre shell windows)
source ./venv/bin/activate # (Linux/Mac) 
```

### Récupération du projet

```sh
git clone git@github.com:ii02735/bigdata-news.git
cd bigdata-news
```
### Variables d'environnement à remplir

Vous devez tout d'abord créer une copie du fichier `.env.dist` qui sera ensuite nommée `.env`.

Les variables à définir sont les suivantes :

- `API_KEY` : une **clé d'API** de CurrentAPI
- `MONGO_URL` : L'URL de connexion au serveur Mongo, si utilisation du container Docker proposé dans la stack Docker, écrire `mongo://mongo/news`
- `JOB_SCHEDULE` : La période d'exécution pour la tâche CRON (en minutes, passer **une valeur négative** si l'exécution de la tâche n'est pas souhaitée)

### Démarrer Docker
    
La stack Docker, gérée par **docker-compose** contient les services suivant :

- `spark-master` : le nœud maître du cluster de Spark
- `spark-worker` : le nœud esclave du cluster de Spark
- `pyspark-notebook` : un jupyter notebook contenant des dépendances de `pyspark`
- `mongo` : un serveur de base de données Mongo    

Pour pouvoir démarrer cette stack : `docker-compose up`   

### Installation des dépendances
[pip](https://pypi.python.org/pypi/pip) est le gestionnaire de dépendances qui
va nous permettre d'installer tout ce qui est nécessaire à ce projet.

Si vous souhaitez utiliser le notebook, il vous sera nécessaire de :

- Vous rendre dans le dossier `news`
- Exécuter la commande suivante : `pip3 install -r requirements.txt` ou `python3 -m pip install -r requirements.txt`


### Démarrer Streamlit

Se rendre dans le dossier `news` puis exécuter la commande suivante :

Si sous environnement virtuel : `streamlit run app.py`

Sinon : `python3 -m streamlit run app.py`