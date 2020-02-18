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

## III. information gathering

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


## V. Result Analysis and Conclusion

1. Analyse des résultats & construction d’une conclusion : Une fois votre expérience terminée, vous récupérez vos mesures et vous les analysez pour voir si votre hypothèse tient la route. 

## VI. Tools \(facultatif\)
Précisez votre utilisation des outils ou les développements \(e.g. scripts\) réalisés pour atteindre vos objectifs. Ce chapitre doit viser à 
\(1\) pouvoir reproduire vos expériementations, 
\(2\) partager/expliquer à d'autres l'usage des outils.

## VI. Menaces à la validité des résultats

## VII. References

1. ref1
1. ref2
