FROM apache/airflow:2.9.2

# Ajouter le fichier requirements.txt et installer les dépendances
ADD requirements.txt .
RUN pip install -r requirements.txt

# Ajouter le script d'initialisation
COPY init.sh /init.sh

# Donner les permissions d'exécution au script
RUN chmod +x /init.sh

# Configurer l'entrée du conteneur pour exécuter le script d'initialisation
ENTRYPOINT ["/init.sh", "&&", "/entrypoint"]
CMD ["webserver"]