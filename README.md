# Find_Seat
Ce README sera écrit en français par commodité, l'ensemble du code et des tests sont écrits et documentés exclusivement en anglais.
Le but de l'exercice est de trouver l'ID d'un siège d'avion qui n'est pas présent dans une liste de sièges représentés sous format codé.

## Instructions

1. S'assurer que le fichier find_seat.py se trouve dans le même dossier que scan.txt
2. Lancer le programme via la commande `python find_seat.py`
3. Les tests unitaires peuvent être lancés via la commande `python unit_tests.py`

## Procédé de résolution

Etant donné qu'on nous demande un numéro d'id de siège, j'ai commencé en créant les fonctions decode_boarding_pass(), decode_row() et decode_column().
D'ailleurs c'est là qu'a été ma première erreur, j'ai voulu commencer par les fonctions mais il aurait été bien plus sage de faire du Test Driven Development (TDD), étant donné qu'on nous donne justement des exemples de billets avec leur code, leur id ainsi que la colonne et la ligne. Je me suis montré trop pressé, et n'ai fait les tests correspondants qu'après l'écriture de la fonction.

Une fois les fonctions écrites et testées, il m'a suffi d'ouvrir le fichier scan.txt ligne par ligne, pour ensuite obtenir la liste occupied_seats, qui regroupe tous les IDs des sièges pris par quelqu'un d'autre. Enfin, il suffit d'un tri de la liste puis de rechercher la première (et normalement la seule) occurence d'un trou dans cette liste d'IDs consécutifs.

## Idées d'ajouts de features

Donner une possibilité de lire un autre fichier que scan.txt.

S'adapter au cas ou plusieurs sièges vides se situent dans l'avion, les indiquer dans l'ordre pour permettre un choix éclairé.

Pour réduire légèrement la complexité spatiale, remplacer la liste dans laquelle on stocke les billets repérés par un dictionnaire donc les clés pourraient être les numéros de rangée et les valeurs les sièges de ces rangées déjà occupés. Ainsi une clé qui possèderait 8 valeurs pourrait être supprimée, et il ne resterait que les rangées de début et fin d'avion avec des sièges manquants, et une seule rangée à 7 sièges occupés, le siège restant serait le nôtre.

Pour réduire la complexité temporelle de la recherche du siège, une recherche plus optimisée comme la recherche binaire pourrait être envisageable, en comparant l'ID du premier et du dernier siège, et voyant si l'ID manquant semble situé dans la première ou seconde partie de la liste occupied_seats via l'ID au milieu de la liste. Malheureusement je n'y pense que trop tard (14:47), je n'ai pas le temps d'implémenter cette feature qui aurait pu être intéressante.

On pourrait donner la possibilité de pouvoir modifier la taille de l'avion. Le nombre de rangées et de colonnes devrait toujours être un multiple de deux, mais si on modifie en conséquence le code des sièges, on devrait pouvoir adapter le code à tout type d'avion de forme semblable.

Tous ces ajouts de features demanderaient bien sûr d'autres tests adaptés.