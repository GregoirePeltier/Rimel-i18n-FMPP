---
layout: default
title : Modèle de chapitre pour 2020
date:   2020-01-03 22:00:00 +0100
---

---

> **Date de rendu finale : Mars 2020 au plus tard**
> - Respecter la structure pour que les chapitres soient bien indépendants
> - Remarques :
>>    - Les titres peuvent changer pour etre en adéquation avec votre étude.
>>    - De même il est possible de modifier la structure, celle qui est proposée ici est là pour vous aider.
>>    - Utiliser des références pour justifier votre argumentaire, vos choix etc.

---

**_janvier 2020_**

## Authors

We are four students in last year of Polytech' Nice-Sophia specialized in Software Architecture :

- prune.pillone@etu.unice.fr
- gregoire.peltier@etu.unice.fr
- hugo.francois@etu.unice.fr
- marion.marguerettaz@etu.unice.fr

## I. Research context /Project
Nous avons choisi de restreindre le sujet en parlant de localisation (l10n) et non pas d’internationalisation (i18n). 
En effet i18n permet de concevoir et développer une application qui permet de facilement mettre en place l10n. 

La localisation est le fait d'adapter un logiciel à un marché international.
Cela inclut la traduction bien sûr, mais aussi le fait d'adapter l'interface et les tests afin d'être sûrs que le programme fonctionnera dans le langage visé.
                

En choisissant l10n cela nous permet de réduire l’amplitude du sujet et donc d’avoir une question plus spécifique.
Nous avons choisi de poser la question : “Quel est l’impact des techniques de mise en oeuvre de la localisation sur les projets informatique ?”.
Nous avons défini les techniques comme un ensemble des framework, librairies qui peuvent être utilisés par un projet.
Cette question est intéressante puisqu’elle touche à deux aspects, quelles techniques sont utilisées, mais aussi est-ce que ces techniques apportent des contraintes sur le projet , et lesquelles sont-elles ?


Préciser ici votre contexte.

Pourquoi c'est intéressant.

![Figure 1: Logo UCA](../assets/model/UCAlogoQlarge.png){:height="50px" }


## II. Observations/General question

1. Commencez par formuler une question sur quelque chose que vous observez ou constatez ou encore une idée émergente. Attention pour répondre à cette question vous devrez être capable de quantifier vos réponses.
2. Préciser bien pourquoi cette question est intéressante de votre point de vue et éventuellement en quoi la question est plus générale que le contexte de votre projet \(ex: Choisir une libraire de code est un problème récurrent qui se pose très différemment cependant en fonction des objectifs\)

Cette première étape nécessite beaucoup de réflexion pour se définir la bonne question afin de poser les bonnes bases pour la suit.

### Sous Questions :
- Sommes nous capables d’identifier l’impact de la localisation dans des projets informatiques ?
    -En fonction des résultats, on pourrait réorienter le projet vers une autre approche
- Sommes nous capables d’évaluer le type d’impact de la localisation ?
    - Si oui, quels impacts peut-on distinguer ?  
- Quelles sont les corrélations entre la gestion de version et la mise en oeuvre de la localisation dans un projet informatique ?
    - Est-ce qu’il y a des merges dédiés ?
    - Est-ce qu’il y a des branches dédiées ? 

## III. information gathering

Préciser vos zones de recherches en fonction de votre projet,

1. les articles ou documents utiles à votre projet
2. les outils
 
## IV. Hypothesis & Experiences

1. Il s'agit ici d'énoncer sous forme d' hypothèses ce que vous allez chercher à démontrer. Vous devez définir vos hypothèses de façon à pouvoir les _mesurer facilement._ Bien sûr, votre hypothèse devrait être construite de manière à v_ous aider à répondre à votre question initiale_.Explicitez ces différents points.
2. Test de l’hypothèse par l’expérimentation. 1. Vos tests d’expérimentations permettent de vérifier si vos hypothèses sont vraies ou fausses. 2. Il est possible que vous deviez répéter vos expérimentations pour vous assurer que les premiers résultats ne sont pas seulement un accident.
3. Explicitez bien les outils utilisés et comment.
4. Justifiez vos choix

## V. Result Analysis and Conclusion

1. Analyse des résultats & construction d’une conclusion : Une fois votre expérience terminée, vous récupérez vos mesures et vous les analysez pour voir si votre hypothèse tient la route. 

## VI. Tools \(facultatif\)
1.Récupération de projet java depuis la source Weblate avec un script python
2. Checkout de ces projets afin de visualiser comment est gérée la traduction dans ces projets à l’aide d’un script python
    a. Recherche les .properties (toujours avec le script python)
      - Voir leur localisation (dans des package séparés, tous regroupés)
      - La quantité de fichiers présents
    b. Rechercher les marqueurs de traduction dans les fichiers java, pour voir le nombre de fichiers touchés
3. Parcourir les commits pour trouver ceux qui sont liés aux fichiers de .properties avec un script python
    a. Déterminer le nombre de commit pour ces fichiers
    b. Le nombre de fichiers qui sont aussi modifiés lors de ce commit

L’impact de la localisation pourra être mesuré par 

1. La localisation des .properties, est-ce que cela a influencé l’architecture d’un projet
2. Le nombre de marqueurs de traductions trouvés dans les fichiers java 
    a. Ainsi que la vitesse à laquel ses marqueurs ont été ajouté à un fichier (est-ce qu’ils sont ajoutés à la création du fichier ou plus tard)
3. Le nombre de commit affectés à la localisation, cela nous permettra de voir combien de commit sont liés à la localisation ou non, et donc de voir quel proportion la localisation prend sur le développement d’une application.
    a. Hypothèse = un commit lié à localisation est un commit qui contient dans son message de commit 
    "localization" ou "l10n" ou "i18n" ou "internationalization" ou "translate" ou "translation" ou "weblate"
4. Le nombre de lignes/fichiers affectés à un commit lié à la localisation

Ces informations nous permettront de faire un état des lieux et d’avoir des métriques simples pour commencer à répondre à notre question  “Quel est l’impact des techniques de mise en oeuvre de la localisation sur les projets informatique ?”. Selon les résultats, nous pourrons ensuite aviser pour prendre compte un autre langage ou une autre source de récupération de projets.

Précisez votre utilisation des outils ou les développements \(e.g. scripts\) réalisés pour atteindre vos objectifs. Ce chapitre doit viser à \(1\) pouvoir reproduire vos expériementations, \(2\) partager/expliquer à d'autres l'usage des outils.

## VI. Menaces à la validité des résultats

## VII. References

1. ref1
1. ref2
