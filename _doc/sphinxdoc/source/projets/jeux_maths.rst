
.. _l-proj_jeux_maths:

Jeux mathématiques
==================

.. contents::
    :local:

Ces sujets reposent sur un exposé mathématique.

.. _l-math-wifi:

Ondes Wifi
----------

Tout tient dans cet article : `Helmhurts <http://jasmcole.com/2014/08/25/helmhurts/>`_.

.. _l-math-pento:

Pentomino
---------

.. index:: pentomino, tétris

Un pentomino est un puzzle style Tétris (voir la page `Wikipédia <http://fr.wikipedia.org/wiki/Pentamino>`_).
Sur une grille, on doit disposer des pièces toutes différentes mais constituée d'un nombre fixe
de carrés pour former un rectangle sans trous.
Comment faire avec une méthode systématique ?

Vous pouvez soit vous lancer dans le vide, soit lire le document suivant `pentominoes.pdf <http://www.xavierdupre.fr/enseignement/projet_data/pentominoes.pdf>`_.
Encore une fois, la résolution du puzzle constitue l'essentiel du projet, l'interface graphique
est accessoire et la sortie pourrait tout-à-fait être réalisée en mode texte.

.. image:: pent1.png

.. image:: pent2.png

.. _l-math-motif:

Recherche exacte d'un motif, d'une expression
---------------------------------------------

.. index:: TF-IDF, BM25

L'objectif est assez simple puisqu'il s'agit de rechercher une expression,
un mot dans toutes les pages Wikipédia. Néanmoins, rechercher une expression parmi
plusieurs millions de pages est assez long et il est nécessaire d'optimiser
les algorithmes utilisés
(voir `Algorithme de recherche de sous-chaîne <http://fr.wikipedia.org/wiki/Algorithme_de_recherche_de_sous-cha%C3%AEne>`_
ou la `version anglaise <http://en.wikipedia.org/wiki/String_searching_algorithm>`_,
plus complète).
Dans un premier temps, on pourra comparer deux variantes parmi les cinq proposées :

* `Rabin–Karp algorithm <http://en.wikipedia.org/wiki/Rabin–Karp_string_search_algorithm>`_
* `Finite-state machine <http://en.wikipedia.org/wiki/Finite-state_machine>`_
* `Knuth–Morris–Pratt algorithm <http://en.wikipedia.org/wiki/Knuth–Morris–Pratt_algorithm>`_
* `Boyer–Moore string search algorithm <http://en.wikipedia.org/wiki/Boyer–Moore_string_search_algorithm>`_
* `Bitap algorithm <http://en.wikipedia.org/wiki/Bitap_algorithm>`_

Dans un second temps, on s'intéressera à la meilleure approche possible
pour implémenter trois combinaisons logiques entre deux mots :

* Ce document doit contenir m1 et m2.
* Ce document doit contenir m1 ou m2.
* Ce document doit contenir m1 et m2 avec au plus n mots entre m1 et m2.

.. _l-math-exp:

Recherche approximative d'un motif, d'une expression
----------------------------------------------------

.. index:: Smith-Waterman, Approximate String Matching

Il arrive qu'on ne connaisse pas l'orthographe d'un mot qu'on cherche ou qu'on se
trompe tout simplement et pourtant on souhaite toujours retrouver
l'ensemble des documents Internet (ici Wikipedia seulement)
qui contiennent une version approchée d'un mot ou d'une expression.
La page `Approximate String Matching <http://en.wikipedia.org/wiki/Approximate_string_matching>`_
décrit le problème et donne quelques liens
vers des solutions. Ces méthodes sont souvent utilisées pour la recherche
de sous-séquences ADN et sont très coûteuses en calcul.

Lorsque la séquence à chercher est courte, l'utilisation d'une
`distance de Levenstein <http://en.wikipedia.org/wiki/Levenshtein_distance>`_
(voir également `Smith-Waterman <http://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm>`_
ou encore `BLAST <http://en.wikipedia.org/wiki/BLAST>`_)
améliorée est encore possible pour un temps de calcul raisonnable.

Lorsqu'on veut rechercher par exemple si un texte est largement inspiré d'une page Wikipédia,
la chaîne est beaucoup plus longue et il faut ruser pour obtenir un temps de
calculer raisonnable. On a recours à des
`chaînes de Markov <http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=5715088>`_,
ou des `q-grams <http://www.xavierdupre.fr/enseignement/projet_data/q-gram_TCS92.pdf>`_
(voir aussi `celui-ci <http://www.xavierdupre.fr/enseignement/projet_data/q-gram_p195-lee.pdf>`_).
L'objectif n'est pas nécessairement d'utiliser ces méthodes mais de développer
des idées simples permettant de rechercher un long texte dans le corps de Wikipedia.

Saurez-vous ruser ?

.. _l-math-tsp:

Problème du voyageur de commerce
--------------------------------

.. index:: TSP, hill climbing, salesman, circuit hamiltonien, hamiltonien

C'est un problème assez classique : `problème du voyageur de commerce <http://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce>`_
qui consiste à trouver le plus court chemin passant par tous les noeuds d'un graphe.
Le terme mathématique est : `circuit hamiltonien <http://fr.wikipedia.org/wiki/Graphe_hamiltonien>`_

On pourra essayer différents algorithmes :

* `Parcours eulériens et hamiltoniens <https://www.gerad.ca/~alainh/Euler-Hamilton.pdf>`_
* `Hill Climbing <http://en.wikipedia.org/wiki/Hill_climbing>`_
* `A New Algorithm For Finding Hamiltonian Ccircuits <http://www.dharwadker.org/hamilton/>`_
* `Trouver un cycle hamiltonien sur un graphe <http://blog.neamar.fr/2-uncategorised/129-algorithme-cycle-hamiltonien-graphe>`_

Un article sur les heuristiques utilisées lors de la résolution :

* `Evolving TSP heuristics using Multi Expression Programming <http://arxiv.org/abs/1509.02459>`_

Exemple d'utilisation :

* `multiroute avec Bing <https://www.multiroute.de/?locale=fr>`_

.. _l-math-tsp-plus:

Problème des tournées de véhicules
----------------------------------

Le `problème de tournées de véhicules <https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_tourn%C3%A9es_de_v%C3%A9hicules>`_
est une extension du voyageur de commerce. Pour le résoudre, on pourra s'inspirer
de l'article :
`Technical Note: Split algorithm in O(n) for the vehicle routing problem <http://arxiv.org/pdf/1508.02759v2.pdf>`_.

.. _l-math-text:

Construction d'une texture
--------------------------

.. index:: image processing

On veut peindre une image à l'aide d'un motif présent sur une image plus petite. Le problème
survient lorsqu'on la duplique, en collant deux fois la même image côte à côte, les deux bords
s'ajustent rarement. L'article
`Texture Synthesis by Non-parametric Sampling <http://www.xavierdupre.fr/enseignement/projet_data/texture_efros-iccv99.pdf>`_
propose une méthode pour contourner ce problème.
On pourra aussi regarder le site des auteurs. L'objectif est
d'implémenter l'algorithme. Dans un deuxième temps, on pourra s'intéresser au même genre de méthode mais appliquer au
débruitage d'une image. On s'inspire pour cela de l'article
`A Review Of Image Denoising Algorithms <http://www.xavierdupre.fr/enseignement/projet_data/debruitage_NLM_morel.pdf>`_
(chapitre 5). L'idée consiste à utiliser la redondance dans les images pour trouver dans
une partie non bruitée de l'image l'informatique cherchée.

* `Texture Synthesis by Non-parametric Sampling <http://www.xavierdupre.fr/enseignement/projet_data/texture_efros-iccv99.pdf>`_, Alexei A. Efros and Thomas K. Leung
* `Texture Synthesis by Non-parametric Sampling (web site) <http://graphics.cs.cmu.edu/people/efros/research/EfrosLeung.html>`_

.. _l-math_simulloi:

Simulation d'une loi statistique avec un algorithme d'optimisation A*
---------------------------------------------------------------------

L'objectif est d'implémenter l'algorithme décrit par l'article
`A* Sampling <http://papers.nips.cc/paper/5449-a-sampling.pdf>`_, Chris J. Maddison, Daniel Tarlow, Tom Minka.

.. _l-math_appariement_graph:

Recalage d'un réseau
--------------------

* `Mise en correspondance et recalage de graphes : application aux réeseaux routiers extraits d'un couple carte/image <https://hal.archives-ouvertes.fr/inria-00073156/document>`_, Christine Hivernat, Xavier Descombes, Sabine Randriamasy, Josiane Zerubia
* `Deformable Graph Matching <https://www.ri.cmu.edu/pub_files/2013/6/dgm.pdf>`_, Feng Zhou, Fernando De la Torre

.. index:: palindrome

.. _l-palindrome-projet-structure:

Structure de données adaptée à la recherche de palindromes
----------------------------------------------------------

Le projet a des aspects mathématiques et informatiques. Il part d'un problème :
découvrir tous les palindromes inclus dans une chaîne de caractères. Il propose
un algorithme rapide qui s'appuie sur une structure de données adaptées.
Le projet consiste à implémenter la méthode décrite par l'article
et de l'adapter à d'autres problèmes.

* `Eertree: An Efficient Data Structure for Processing Palindromes in Strings <http://arxiv.org/abs/1506.04862>`_.

.. index:: grammaire

.. _l-grammaire_context_free:

Implémentation d'une grammaire probabiliste pour traiter le langage naturel
---------------------------------------------------------------------------

Les grammaires (voir `grammaires non contextuelles <https://fr.wikipedia.org/wiki/Grammaire_non_contextuelle>`_
permettent d'analyser un texte en taggant les mots ou en les catégorisant.
Le projet consiste à implémenter l'algorithme décrit dans le document suivant :
`Probabilistic Context-Free Grammars (PCFGs) <http://www.cs.columbia.edu/~mcollins/courses/nlp2011/notes/pcfgs.pdf>`_
puis d'appliquer cela sur des articles d'un journal, une page Wikipédia...

.. index:: tree, arbre, distance, Robinson–Foulds, Levenshtein

.. _l-distance_tree_robinson_foulds:

Distance entre deux arbres : Robinson–Foulds (2016)
---------------------------------------------------

On sait calculer une distance entre deux séquences qu'on appelle distance d'édition
ou `distance de Levenshtein <https://fr.wikipedia.org/wiki/Distance_de_Levenshtein>`_.
Il paraît difficile d'adapter cette distance au cas de deux arbres mais une telle
distance existe :
`distance de Robinson–Foulds <https://en.wikipedia.org/wiki/Robinson%E2%80%93Foulds_metric>`_.
L'objectif du projet est d'implémenter cette distance et de l'application
à des arbres de décision, telle que ceux produits par `scikit-learn <http://scikit-learn.org/>`_.
Vous trouvez d'autres articles dans cet article
:ref:`Référence similarités entre graphes <blog-article-graph-distance>`.

.. index:: inéquations, résolution, systèmes

.. _l-maths-inequation:

Résolution de systèmes d'inéquations (2016)
-------------------------------------------

On se débrouille beaucoup mieux avec la résolution d'un système linéaire d'équations.
Mais des inéquations, on préfère quand il s'agit de minimiser ou maximiser.
Et quand il ne s'agit de rien de tout ça, on peut s'orienter vers
les idées proposées dans l'article :
`Exact algorithms for linear matrix inequalities <http://arxiv.org/pdf/1508.03715v1.pdf>`_.

Sujet plutôt très mathématique puisqu'il s'agit d'implémenter un algorithme
de résolutions de tels systèmes.

.. _l-maths-meilleur-clavier:

Elaboration d'un clavier (2017)
-------------------------------

Le clavier `Azerty <https://fr.wikipedia.org/wiki/AZERTY>`_ n'est pas le plus aimé mais il a encore
la vie dure. L'article suivant
`Bépo, Dvorak, Colemak... A la recherche du clavier français qui pourrait remplacer l'azerty <http://www.lemonde.fr/pixels/article/2016/04/23/bepo-dvorak-colemak-a-la-recherche-du-clavier-francais-qui-pourrait-remplacer-l-azerty_4907632_4408996.html>`_
aborde quelques façons de concevoir un clavier.
L'idée de ce projet est de concevoir un clavier qui minimise une fonction d'utilité,
de voir si cette utilité est différente pour un programmeur et un romancier.

.. _l-impression-3D:

Impression 3D (2018)
--------------------

L'article suivant introduit un algorithme mathématique
pour dessiner une structure complexe avec une imprimante 3D.

* `Freeform Assembly Planning <https://arxiv.org/pdf/1801.00527.pdf>`_

.. _l-string-period:

Détection de période dans les séquences qui préservent l'ordre (2018)
---------------------------------------------------------------------

Le sujet s'appuie sur l'article
`String Periods in the Order-Preserving Model <https://arxiv.org/pdf/1801.01404.pdf>`_.
On considère deux séquences :math:`(X_1, ..., X_n)` et :math:`(Y_1, ..., Y_n)`
où chaque :math:`X_i` et :math:`Y_i` sont choisis dans un ensemble fini d'entiers.
On dit que les séquences sont équivalentes en ordre (noté :math:`X \approx Y`) si :

.. math::

    \forall i, j \in [1,...,n], \; X_i < X_j \Leftrightarrow Y_i < Y_j

Example : 5 2 7 5 1 3 10 3 5 :math:`\approx` 6 4 7 6 3 5 9 5 6

L'article se pose la question de détection de période dans ce type de séquences.
