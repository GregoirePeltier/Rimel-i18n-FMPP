## Auteurs

Nous sommes quatre étudiants en dernière année à Polytech Nice Sophia :

- prune.pillone@etu.unice.fr
- gregoire.peltier@etu.unice.fr
- hugo.francois@etu.unice.fr
- marion.marguerettaz@etu.unice.fr

## I. Context du projet
Nous avons choisi de restreindre le sujet en parlant de localisation (l10n) et non pas d’internationalisation (i18n). 
En effet i18n permet de concevoir et développer une application qui permet de facilement mettre en place l10n. 

La localisation est le fait d'adapter un logiciel à un marché international.
Cela inclut la traduction bien sûr, mais aussi le fait d'adapter l'interface et les tests afin d'être sûrs que le programme fonctionnera dans le langage visé.
                

En choisissant l10n cela nous permet de réduire l’amplitude du sujet et donc d’avoir une question plus spécifique.
Nous avons choisi de poser la question : “Quel est l’impact des techniques de mise en oeuvre de la localisation sur les projets informatique ?”.
Nous avons défini les techniques comme un ensemble des framework, librairies qui peuvent être utilisés par un projet.
Cette question est intéressante puisqu’elle touche à deux aspects, quelles techniques sont utilisées, mais aussi est-ce que ces techniques apportent des contraintes sur le projet , et lesquelles sont-elles ?

![Figure 1: Logo UCA](../assets/model/UCAlogoQlarge.png){:height="50px" }


## II. Question et sous-questions

###Question générale
Nous avons choisi de restreindre le sujet en parlant de localisation (l10n) et non pas d’internationalisation (i18n). En effet i18n permet de concevoir et développer une application qui permet de facilement mettre en place l10n. En choisissant l10n cela nous permet de réduire l’amplitude du sujet et donc d’avoir une question plus spécifique.
Nous avons choisi de poser la question : “Quel est l’impact des techniques de mise en oeuvre de la localisation sur les projets informatique ?”.
Nous avons défini les techniques comme un ensemble des framework, librairies ou développement dédiés à gérer de multiples langues dans un projet.
Cette question est intéressante puisqu’elle touche à deux aspects, quelles techniques sont utilisées, mais aussi est-ce que ces techniques apportent des contraintes sur le projet , et lesquelles sont-elles ? 

###Sous-questions 
- Sommes nous capables d’identifier l’impact de la localisation dans des projets informatiques ?
    -En fonction des résultats, on pourrait réorienter le projet vers une autre approche
- Sommes nous capables d’évaluer le type d’impact de la localisation ?
    - Si oui, quels impacts peut-on distinguer ?  
- Quelles sont les corrélations entre la gestion de version et la mise en oeuvre de la localisation dans un projet informatique ?
    - Est-ce qu’il y a des merges dédiés ?
    - Est-ce qu’il y a des branches dédiées ? 

## III. Collecte d'information

Préciser vos zones de recherches en fonction de votre projet,

1. les articles ou documents utiles à votre projet
2. les outils
 
## IV. Méthodologie

Pour cette expérience, nous avons d'abord récupéré des projets java depuis la source Weblate avec un script python [script.1]. Puis nous avons effectué des analyses sur ces projets. Tous les outils utilisés pour effectuer les analyses sont des scripts python que nous avons développé.

Nous avons choisi d'effectuer deux types d'analyses. 

La première concernant la structure d'un projet :
- Rechercher les .properties liés à la localisation dans les projets java [script.2]. Trouver la localisation des .properties nous permettra de déterminer si la l10n a un impact sur l'architecture des projets. 
    - Voir leur localisation s'ils sont dans des packages séparés ou non
    - Voir la quantité de fichiers .properties par rapport au reste des fichiers java

- Rechercher les marqueurs de traduction dans les fichiers Java/Jsp. [script.3]. Cette information permettra de voir la quantité de fichiers Java/JSP impactés par la l10n.
  
 Lors de la première itération, nous avons remarqué qu'une majorité des projets weblate java étaient en fait des projets Android. Les projets Android ont une gestion de la traduction particulière qui demande d'adapter notre première étape. Même si les fichiers sont différents, le but reste le même pour chaque étape voir l'influence sur l'architecture et le nombre de fichiers Java impactés.

- Rechercher répertoires "values" liés à la localisation dans les projets Android [script.4]
    - Voir la quantité de fichiers xml dans les répertoires "values" par rapport au reste des fichiers java
    
- Rechercher les marqueurs de traduction dans les fichiers java, pour voir le nombre de fichiers Java touchés par la traduction [script.3]


La deuxième analyse concerne la gestion de version avec : 
- Parcourir les commits pour trouver ceux qui sont liés à la l10n grâce à des mots clefs (localisation, translation etc) [script.5]
- Voir le nombre de fichiers impactés lors des commits liés à la localisation. Cette analyse permettra de savoir combien de commits sont liés à la localisation, et de voir quelle proportion prend la localisation sur le développement d'une application 

- Parcourir les branches pour déterminer si une branche est spécifique à la traduction [script.6]. Ces résultats montreront si une branche est spécifique à la gestion d'l10n ou non.

- Répartition des auteurs pour les commits de traduction. [script.7]. Cela permettra de savoir si les commits sont majoritairement de weblate ou de développeurs.

Toutes ces informations nous permettront d'avoir des métriques simples pour répondre à notre question "Quel est l'impact des techniques de mise en œuvre de la localisation sur les projets informatiques". 

Afin d'avoir une donnée globale nous avons analysé les 1000 projets Java les mieux notés sur Github pour avoir une estimation du nombre de projets faisant de la traduction (tous outils confondus).

Concernant l'organisation, nous avons procédé en deux étapes pour chaque analyse. Tout d'abord créer un script permettant de récolter une information spécifique puis créer un ou plusieurs graphiques depuis ces résultats afin de mieux les visualiser et les analyser. 
Chaque membre de l'équipe a créé des scripts et des graphiques.

## V. Analyse des résultats

1. Analyse des résultats concernant l'architecture des projets

Projets Android :
Concernant l'architecture des projets elle n'est pas impactée par la gestion de la localisation puisque tous les projets androids suivent la même norme qui consiste a ranger les fichiers de traductions dans le répertoire "res" à la racine. La gestion des différentes langues se fait avec différents répertoires "values". Un répertoire va correspondre à une langage par exemple /res/values-de contenant un fichier "strings.xml".

[INSERTION android_project.png]

Nous pouvons voir graphique au graphique ci-dessus que la taille des projets (ici le nombre de java file servent de références) n'a pas d'incidence sur la quantité de langue traduite. On peut aussi remarquer que les projets qui sont plus petits ont une grosse quantité de langues traduites (par exemple: mini.pocket, PixelKnot, card-locker) par rapport à leur quantité de fichier java. [A REVOIR]


Projets Java :

[INSERTION java_project_graph.png]


[INSERTION java_project_properties_localisation.png]


    "Android stat": {
        "average": 14.591324874594275,
        "averageOccurrencePerProject": 109.54545454545455,
        "totalNbFile": 6778,
        "totalNbFileWithKey": 989,
        "totalNbOccurrence": 4820
    },
    "Java stat": {
        "average": 9.652063345278004,
        "averageOccurrencePerProject": 921.5,
        "totalNbFile": 8651,
        "totalNbFileWithKey": 835,
        "totalNbOccurrence": 3686
    }


## VI. Menaces à la validité des résultats

Commits de localisation : 
Lorsqu'on étudie le graphique représentant le pourcentage de commits liés à la localisation sur la branche master, on se rend rapidemment compte que le pourcentage est extrêment variable.
[INSERTION pourcentage_commit_graph.png]
Si on excepte les projets n'ayant aucun commits de localisation, le plus bas est à 1%, et le plus haut est à 76%. 
Cette disparité dans le pourcentage nous a étonné, car nous nous attendions à ce que l'automatisation avec weblate permette de garder le nombre de commits assez bas, et régulier entre différents projets.

La question s'est ensuite posée de savoir si une branche en particulier était dédiée à la localisation. 
Pour cela nous avons réalisé un graphique en batons avec 3 valeurs pour chaque projet :
- Le pourcentage moyen de commits sur toutes les branches (bleu clair)
- Le pourcentage maximal de commits pour ce projet (violet)
- Le pourcentage de commits sur master (vert)

[INSERTION graph_branches.png]

Globalement, on observe qu'il n'y a pas de branches dédiée à la localisation, car seuls 2 projets montrent une différence notable entre le pourcentage maximal et le pourcentage moyen.
On remarque aussi qu'un bon nombre de projet (33 / 64) ont leur pourcentage de commits sur master égal au pourcentage maximal de commits, on peut donc supposer que master est la branche dédiée à la localisation pour ces projets là.

Encore une fois, nous nous n'attendions pas à ce résulat, et nous pensions voir beaucoup plus de projets possédant une branche de localisation dédiée autre que master. 

On peut toutefois remarquer que le pourcentage de commits de localisation en moyenne sur toutes les branches reste globalement assez proche du nombre de commits maximal, ce qui peut montrer qu'il n'y a pas de grande disparité entre la répartition des commits sur les branches.


## VII. Conclusion 

## VIII. Outils \(facultatif\)
Avec ces valeurs, si on observe que la branche maximale a la même valeur que master, c'est que la localisation se concentre majoritairement sur master.

Enfin, nous avons souhaité étudier la répartition des commits en fonction des auteurs : si le commit a été fait par un humain ou par Weblate. 
Nous avons donc réalisé un digramme en boite à moustaches du pourcentage de répartion de commits de localisation réalisé par Weblate sur tous les projets. 
[INSERTION graph_moyenne.png]
La moyenne est à 50%, le minimum est à 0% et le maximum à 95%. Cela représente donc un grand écart type. 

Nous sommes encore une fois surpris d'avoir la moitié des commits de localisation réalisés par des humains, car nous attendions à un pourcentage
assez faible, compte tenu de l'automatisation des commits par Weblate.


## VI. Menaces à la validité des résultats

Les principales menaces à la validité des résultats se situent dans nos hypothèses  et nos échantillons de départ.
En effet, le fait de récupérer des projets open source sur Weblate peut provoquer un biais dans les résultats, car les projets open source ne fonctionnent pas de la même manière que des projets "privés".

De plus, pour déterminer les commits à la localisation nous utilisons des mots-clés ["localization", "l10n", "i18n", "internationalization", "translate", "translation", "weblate"]
Le problème se trouve dans le fait que ces mots clés ne sont peut être pas les bons, et qu'ils peuvent peut être inclure d'autres commits.
Pour essayer de corriger ce problème, nous avons déterminé un indice de confiance. Nous avons choisi 40 commits identifiés comme commit de localisation et nous avons vérifié qu'il s'agissait bien de cela. Nous avons donc obtenu : 


## VII. References
1. ref1
1. ref2
