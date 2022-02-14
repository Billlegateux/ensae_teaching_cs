
.. index:: 1A, projet

.. _l-projinfo1a:

1A - Projets informatiques
==========================

* `Projet de programmation
  <https://www.ensae.fr/courses/projet-de-programmation/>`_
  (ENSAE)

Les exercices présentent la logique de la programmation
mais la pratique est la seule véritable façon de progresser.
La plupart des élèves qui n'avaient pas ou peu programmé
avec ce projet ont noté une réelle différence avant et après.
Ci-dessous, quelques phrases extraites de rapports d'étudiants
et qui traduiront mieux que je ne pourrais le faire les étapes
par lesquelles on passe dans ce type d'aventure.

.. toctree::

    projets/extrait_projet_1A_2015

.. contents::
    :local:

Travail attendu et contraintes
------------------------------

Le projet dure quatre mois au second semestre (de février à mai).
Il se conclut par un programme
et un rapport. Une soutenance fin mai, début juin.
Le rapport doit souligner la contribution originale des élèves,
illuster les résultats numériques obtenus et la
façon dont ils ont été obtenus.
On suppose que le rapport s'adresse à un public expert.
La soutenance doit reprendre les points principaux,
décrire brièvement la façon dont le travail a été réparti
au sein de l'équipe.

Chaque projet, quelque soit le sujet, devra comporter une **composante numérique**
(statistique, économique, financière, ...), que ce soit une stratégie de trading,
l'optimisation d'une intelligence artificielle pour un jeu, une simulation économique.
Cet aspect devra ressortir lors de la rédaction du rapport final qui devra exposer les résultats
numériques obtenus et faire au moins une ou deux allusions à la façon dont ces calculs ont
été implémentés. Voici la liste des contraintes :

* le projet doit inclure une **composante numérique**,
* le code doit inclure un **test unitaire**
  (voir :ref:`td1aunittestcicorrectionrst`),
* le projet ne doit inclure **aucune donnée réelle**,
* lors de la soutenance, chaque membre d'un groupe devra
  décrire le code d'un **algorithme utilisé** dans le projet
  et dire en quoi il est **optimal**.

Recommandations
---------------

Ces remarques sont plus un guide qu'un plan précis comme cet extrait de film bien connu
`The Pirate code <https://www.youtube.com/watch?v=WJVBvvS57j0>`_.

* :epkg:`git` et :epkg:`github`, tous les projets open source
  l'utilisent, il facilite le travail à plusieurs
* les **tests unitaires** sont utiles pour s'assurer qu'un algorithme
  fonctionne toujours malgré toutes les modifications
* un algorithme ne doit pas s'arrêter en cours de route, il doit
  aussi produire des résultats, un graphique permet en coup d'oeil
  d'en juger la cohérence.

Sujets proposés
---------------

Les sujets proposés abordent différents domaines connexes aux enseignements proposés à l'ENSAE
(finance, statistique, économie) et quelques jeux.
Tous les projets proposés sont des suggestions, les élèves sont libres d'élaborer un sujet de leur choix
ou de s'inspirer des énoncés ci-dessous à la condition de le faire valider par un encadrant.
Afin d'avoir un premier suivi productif,
il est conseillé de parcourir les références bibliographiques suggérées.
C'est souvent l'occasion de découvrir un sujet que vous ne verrez pas ou peu à l'ENSAE.
Par genre :

.. toctree::
    :maxdepth: 1

    projets/p_finance
    projets/p_data_folie
    projets/gen_ant
    projets/jeux
    projets/jeuxcartes
    projets/jeux_seul
    projets/jeux_maths
    projets/ml
    projets/p_security
    projets/technique
    projets/simulation

Liste exhaustive :

#. ML algo : :ref:`l-ml-renf`
#. ML algo : :ref:`l-ml-chow`
#. ML algo : :ref:`l-ml-visage`
#. ML algo : :ref:`l-ml-deepext`
#. ML algo : :ref:`l-ml-align`
#. ML algo : :ref:`l-fast-k-NN`
#. ML algo : :ref:`l-ml-gradient-geom`
#. ML algo : :ref:`l-ml-tree-graph`
#. Jeu 1 : :ref:`l-jeu-deuxmille`
#. Jeu 1 : :ref:`l-jeuvoronoi`
#. Jeu 1 : :ref:`l-puzzle-GCHQ`
#. Jeu 1 : :ref:`l-tetrisia`
#. Jeu 1 : :ref:`l-rihikudo`
#. ML : :ref:`l-data-velib`
#. ML : :ref:`l-data-nuage`
#. ML : :ref:`l-data-twitter`
#. ML : :ref:`l-data-whoosh`
#. ML : :ref:`l-ml-reg-geod`
#. ML : :ref:`l-ml-ethique`
#. ML : :ref:`l-ml-fire-detection`
#. ML : :ref:`l-ml-snn`
#. ML : :ref:`l-ml-knn-pca`
#. ML : :ref:`l-ml-code-plagiat`
#. Finance : :ref:`l-fi-trend`
#. Finance : :ref:`l-fi-port`
#. Finance : :ref:`l-fi-pair`
#. Finance : :ref:`l-fi-ml`
#. Finance : :ref:`l-fi-etf`
#. Simulation : :ref:`l-sim-segre`
#. Simulation : :ref:`l-sim-panique`
#. Simulation : :ref:`l-sim-social`
#. Simulation : :ref:`l-sim-autoroute`
#. Simulation : :ref:`l-sim-covid`
#. Objets connectés : :ref:`l-tech-smart`
#. Objets connectés : :ref:`l-tech-domo`
#. Objets connectés : :ref:`l-visage-reel`
#. Objets connectés : :ref:`l-parole-reel`
#. Objets connectés : :ref:`l-parole-skype`
#. Algo génétique : :ref:`l-gen-optim`
#. Algo génétique : :ref:`l-gen-bag`
#. Algo génétique : :ref:`l-gen-tsp`
#. Algo génétique : :ref:`l-gen-ant`
#. Algo génétique : :ref:`l-gen-motif`
#. Jeu 2 : :ref:`l-jeu-awa`
#. Jeu 2 : :ref:`l-jeu-echec`
#. Jeu 2 : :ref:`l-jeu-echec1d`
#. Jeu 2 : :ref:`l-jeu-go`
#. Jeu 2 : :ref:`l-jeu-gomo`
#. Jeu 2 : :ref:`l-jeu-oth`
#. Jeu 2 : :ref:`l-jeu-pai-sho`
#. Jeu 2 : :ref:`l-jeu-p4`
#. Jeu 2 : :ref:`l-jeu-pokemon`
#. Jeu 2 : :ref:`l-jeu-tic-tac-toe-99`
#. Algo : :ref:`l-math-wifi`
#. Algo : :ref:`l-math-pento`
#. Algo : :ref:`l-math-motif`
#. Algo : :ref:`l-math-exp`
#. Algo : :ref:`l-math-tsp`
#. Algo : :ref:`l-math-tsp-plus`
#. Algo : :ref:`l-math-text`
#. Algo : :ref:`l-math_simulloi`
#. Algo : :ref:`l-math_appariement_graph`
#. Algo : :ref:`l-palindrome-projet-structure`
#. Algo : :ref:`l-grammaire_context_free`
#. Algo : :ref:`l-distance_tree_robinson_foulds`
#. Algo : :ref:`l-maths-inequation`
#. Algo : :ref:`l-maths-meilleur-clavier`
#. Algo : :ref:`l-impression-3D`
#. Algo : :ref:`l-string-period`
#. Jeu hasard : :ref:`l-carte-poker`
#. Jeu hasard : :ref:`l-carte-belotte`

Que faut-il en attendre ?
-------------------------

Vous serez plus **autonome**. Vous n'aurez plus l'assurance qu'une solution existe ni même quelqu'un
qui vous donnera la réponse tout de suite si vous ne trouvez pas. Vous devrez parfois vous interroger sur
les résultats numériques que vous avez obtenus et qui sont si loin de votre intuition qu'ils cachent
sans doute une erreur d'implémentation.
Vous devrez vous-même **définir le problème et y répondre**. Cela veut dire parfois aussi faire un
compromis entre ce que vous rêvez de faire et le temps que vous avez pour le faire.
Si vous travailler à deux, vous découvrirez qu'il n'est pas toujours évident de se **synchroniser**.
Heureusement, les outils ont beaucoup progressé ces dix dernières années.
Un projet informatique s'effectue le plus souvent sur le **long terme**.
Vous verrez que si on fait une pause de quelques semaines dans un projet,
on oublie beaucoup de petits détails qu'on redécouvre aux détours d'une exception.
Mais là encore, il existe des solutions.
Le plus important sans doute, programmer veut aussi dire être **créatif**.
Pour finir, voici ce qu'en ont retiré les élèves de première année en 2015 :
:ref:`l-extrait-projet-1A-2015`.

Ce que vous ne lisez jamais mais que j'observe chaque année
-----------------------------------------------------------

Erreurs de design fréquentes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ce ne sont pas à proprement parler des erreurs car elles n'altèrent pas l'exécution du programme.
Toutefois elles le rendent plus difficile à lire et à corriger en cas d'une *vraie* erreur.
La plupart des développeurs les font lorsqu'ils apprennent à programmer et ne les font plus par la suite.

**Un seul gros fichier**

Chaque année, je vois plusieurs projets informatiques implémenter en un seul gros fichier.
C'est sans doute dû au fait que, lorsqu'on travaille à deux ou trois, il est plus facile de s'échanger un
seul fichier que plusieurs. Je remarque d'ailleurs que les "groupes" d'un élève font créent plus souvent
plusieurs fichiers.

Lorsqu'on développe un jeu, il est préférable de séparer la partie affiche de la partie
intelligence artificielle, il est encore mieux de les mettre dans deux fichiers séparés. La partie
IA sera considéré comme un module et la partie affichage comme le programme principal.

Pour éviter l'envoi continu de mail entre deux membres du même groupe, le meilleur recours est
l'emploi d'un logiciel de suivi de source. `GitHub <https://github.com/>`_ est une possibilité.
C'est celle que j'utilise pour développer ce cours : `sdpython/ensae_teaching_cs <https://github.com/sdpython/ensae_teaching_cs>`_.
Cela permet de suivre les modifications (`un commit <https://github.com/sdpython/ensae_teaching_cs/commit/796dcc695006f9bba44b649cb256f80c91f3a72b>`_),
ou de revenir en arrière.

**Le copier/coller de plus de 10 lignes pour changer un caractère**

Je schématise un peu. Concrètement, lorsqu'on programme un jeu à deux joueurs, on
fait des choses pour le premier joueur dans un bloc de code qu'on recopie pour l'autre
joueur avec quelques modifications subtiles ::

    if joueur == 1 :
        next_joueur = 2
        proba_1[eta_succ[U-1]]=1
        proba_2[eta_succ[U-1]]=0
        proba_2[eta_succ[U-2]]=0
        proba_1[sym(eta_succ[U-1])]=1
        proba_2[sym(eta_succ[U-1])]=0
        proba_2[sym(eta_succ[U-2])]=0
    else :
        next_joueur = 1
        proba_2[eta_succ[U-1]]=1
        proba_1[eta_succ[U-1]]=0
        proba_1[eta_succ[U-2]]=0
        proba_2[sym(eta_succ[U-1])]=1
        proba_1[sym(eta_succ[U-1])]=0
        proba_1[sym(eta_succ[U-2])]=0

Ceci est à éviter le plus possible. Cela allonge inutilement les programmes mais surtout cela
oblige développeur à répercuter une modification sur tous les blocs recopiés. Et on se trompe souvent.
Dans ce cas précis, il est facile d'écrire ::

    if joueur == 1 :
        pr1,pr2 = proba_1,proba_2
    else :
        pr1,pr2 = proba_2,proba_1

    next_joueur = 3 - next_joueur
    pr1[eta_succ[U-1]]=1
    pr2[eta_succ[U-1]]=0
    pr2[eta_succ[U-2]]=0
    pr1[sym(eta_succ[U-1])]=1
    pr2[sym(eta_succ[U-1])]=0
    pr2[sym(eta_succ[U-2])]=0

Et si on est vraiment pointilleux ::

    pr1,pr2 = proba_1,proba_2 if joueur == 1 else proba_2,proba_1

    next_joueur = 3 - next_joueur
    eu_1 = eta_succ[U-1]
    seu_1 = sym(eta_succ[U-1])

    pr1[eu_1]=1
    pr2[eu_1]=0
    pr2[eta_succ[U-2]]=0
    pr1[seu_1]=1
    pr2[seu_1]=0
    pr2[sym(eta_succ[U-2])]=0

**Les variables globales**

Elles sont pratiques :

    * On y met les paramètres d'une simulation ou l'état d'un jeu de poker.
    * On n'a pas besoin de les transmettre comme paramètres à chaque fonction.

Ce choix simple peut devenir ennuyeux par la suite lorsqu'on souhaite faire
tourner plusieurs le même programme en changeant ces variables globales.
Pour éviter cela, le plus simple est de créer une classes qui les contient toutes et
de passer une instance de cette classe à chaque fonction qui en a besoin ::

    class VariablesGlobales :
        def __init__(self):
            self.epsilon = 0.01
            self.alpha = 0.5
            self.iter = 1000
            # ...

    variable = VariablesGlobales ()

    def fonction_qui_en_a_besoin( varglob) :
        s = varglob.alpha
        for i in range(0,varglob.iter):
            # ...

Façons d'écrire du code lent
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**if if if if**

::

    if x == 1:
        r = 0
    if x == 2:
        r = 1

Le second ``if`` porte sur une condition qui n'a aucune chance d'être vérifiée
si la première l'est. Il faut utiliser ``elif``.

::

    if x == 1:
        r = 0
    elif x == 2:
        r = 1

**sort à la place d'un top k**

::

    def deux_meilleures_options(l):
        l.sort()
        return l[0:2]

Trier toute une liste pour n'extraire que deux éléments est plus coûteux que nécessaire
même si c'est simple à coder.

::

    def deux_meilleures_options(l):
        ens = ((v, i) for i, v in enumerate(l))
        return min(ens)[0], min(ens[1:])[0]

**Appel de fonction inutile**

::

    def mean_vector(x):
        return sum(x) / len(x)

    if mean_vector(x)[0] < mean_vector(x)[1]:
        # ...

Le test appelle deux fois la fonction ``mean_vector`` avec les mêmes paramètres.
Le résultat sera forcément identique.

::

    def mean_vector(x):
        return sum(x) / len(x)

    v = mean_vector(x)
    if v[0] < v[1]:
        # ...

**deepcopy inutile**

::

    def enumerate_transposition(li):
        for i in range(1, len(li)):
            cl = copy.deepcopy(li)
            cl[0], cl[i] = li[i], li[0]
            yield cl

Est-il vraiment nécessaire de faire une copie la liste ?
Autant ne pas le faire et l'indiquer dans la documentation.

::

    def enumerate_transposition(li):
        """
        the function does not return a copy,
        do not modify the returned list
        """
        for i in range(1, len(li)):
            li[0], li[i] = li[i], li[0]
            yield li
            li[0], li[i] = li[i], li[0]

**langue**

Si vous hésitez entre l'anglais et le français, préférez l'anglais.

Oublis dans le rapport
^^^^^^^^^^^^^^^^^^^^^^

**Le code qu'on a jeté**

Lorsqu'on fait un projet de la sorte, il arrive souvent qu'on jette du code qu'on a écrit.
On découvre parfois que le programme tel qu'il est conçu ne permet pas de faire
tel ou tel chose, il faut en réécrire une partie. On écrit parfois du code jetable
lorsqu'on a besoin d'un résultat numérique. Une fois celui-ci obtenu, on l'intègre
au programme et on jette le code qui a permis de l'obtenu.

C'est parfois utile dans votre rapport de décrire ces codes jetés. Dans le premier cas,
le code jeté sert de justification au nouveau. Dans le second cas, cela rassure de voir
que certains résultats ne sortent pas de nulle part.

**Qu'avez-vous appris ?**

Certaines conclusions mentionnent le fait qu'on apprend beaucoup à faire un projet informatique,
seul, sans aide extérieure. On apprend autant que durant des séances de travaux pratiques.
C'est un des objectifs de l'exercice : apprendre à maîtriser cet outil qu'est la programmation.
Mais il n'est pas utile de préciser cela dans le rapport.

Mais ce projet demande aussi une part d'imagination, que ce soit pour concevoir une fonction d'évaluation
pour une intelligence artificielle, une simulation économique réaliste, une stratégie financière...
Tout au long de la mise en place de ses idées, on s'aperçoit que les premiers jets sont parfois
un peu naïf, que les premiers résultats numériques ne sont pas aussi bons qu'escomptés.
Il faut retravailler l'idée initiale. Cette partie doit ressortir dans votre rapport et elle
doit bien ressortir.

**Qu'est-ce que le lecteur va retenir ?**

Expliquer les choses, les illustrer, choisir le bon graphique, le bon tableau,
pour défendre une idée n'est pas toujours simple. Il faut parfois imaginer qu'un rapport
sera lu deux fois, une fois en diagonale, une autre plus sérieusement.

Il faut se poser la question de savoir ce que vous voulez que le lecteur
retienne.

Un programme informatique est d'autant
plus difficile à cerner qu'il est long. Le rapport est la version la plus accessible de votre
travail. C'est le point de départ. A partir de là, on navigue plus aisément dans votre programme.

La phrase suivante est librement inspirée d'un rapport à propos d'un jeu :

    *On choisit finalement la première intelligence
    artificielle mais en choisissant cette fois-ci de bons paramètres.*

De cette phrase, je comprends que certains paramètres ont été optimisés mais
le rapport ne revient jamais sur cet aspect. Donc :

    * Je dois deviner quelle partie du programme a servi à cela, si toutefois le code est encore là.
      Je vois bien un fichier qui correspond mais il ne marche pas (ou plus). Je ne suis pas sûr
      d'avoir envie de le débugger.
    * Je ne sais pas quels sont ces paramètres, je n'ai aucune idée des résultats obtenus,
      ni même que la différence de niveau entre les bons paramètres et les mauvais.
    * Je comprends qu'un travail d'optimisation a été effectué mais je n'ai aucune idée
      de l'importance qu'il revêt. Si le rapport n'en fait pas mention, c'est sans doute
      que cela n'est qu'une contribution minime.

**Un exemple ou une copie d'écran**

Les copies d'écran est indispensable pour une interface graphique ou un site web.
Le résultats de vos algorithmes doit être illustrés sur au moins un exemple qui fonctionne
et, si cela a du sens, un autre qui ne fonctionne pas.

**Imprécision**

Je paraphrase :

    On a comparé les deux intelligences artificielles en jouant contre elles,
    la seconde est meilleure.

Et en chiffres ?

Maladresses lors de la soutenance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Court transparent, grand discours**

Lorsqu'on a beaucoup de choses à dire, on prend le risque de noyer l'auditoire sans pouvoir lui
rappeler au cours de ce discours les idées importantes qu'il devrait retenir.
Un transparent part souvent d'une intention lorsqu'on crée la présentation. Devant le public, on s'aperçoit
que l'intention est plus complexe qu'il n'y paraît. C'est à ce moment qu'il faut faire attention à ne pas noyer
ceux qui écoutent. Il ne faut pas hésiter alors à écrire au tableau les idées importantes même si elles n'étaient pas écrites
initialement sur la présentation. Le pire est sans doute de rester plus de deux minutes sur le même transparent tout
en exposant des idées insufisamment préparées dont la perception est le plus souvent confuse.

**Suivre le plan du rapport**

Il faut partir du principe que la soutenance s'adresse à un public non expert qui n'a probablement pas lu votre rapport.
Selon ce critère, suivre le même plan que le rapport ne devrait sans doute pas poser de problème.
Un bémol : en suivant le même plan que le rapport, on a parfois tendance à reproduire le même discours sans vraiment
chercher à l'adapter à ce moyen d'expression.

**Tout dire**

La soutenance est courte et impose souvent de faire un tri sur tout ce que vous voulez présenter.
Le plus souvent, l'auditoire n'est pas un expert et quand bien même il le serait, la plupart des présentations
abordent des sujets complexes qu'il est difficile d'appréhender en quelques minutes.
Vous n'avez pas l'occasion de démontrer la pertinence des résultats, il y a toujours
une forme de confiance qui s'établit entre celui qui expose et celui qui écoute. Car à la fin,
pour les derniers résultats, les plus intéressants, le public n'a pas d'autres choix que de croire
celui qui les énonce. Il est impossible de les vérifier sur le moment.

Comment installer cette relation de confiance ? Il n'y a pas de règles, juste quelques directions comme
montrer comment un algorithme se comporte sur un problème simple, montrer comment l'algorithme s'est construit
peu à peu en considérant quelques exemples précis, insister sur le fait que vous avez contrôlé chaque étape du développement
et laisser l'auditoire supposer que vous avez appliqué la même rigueur jusqu'à l'obtention des résultats finaux.
Au cinéma, cette figure s'appelle une `ellipse <http://fr.wikipedia.org/wiki/Ellipse_%28cin%C3%A9ma%29>`_ (voir aussi
`L'ellipse - leçon (filmée) de cinéma <https://www.youtube.com/watch?v=BMwN2JloosE>`_).

**Déduction rapide**

Beaucoup de groupes tirent des conclusions de peu d'expérimentations :
une simulation n'est pas une preuve mathématique,
et il faut répéter plusieurs fois la même simulation pour une avoir une certitude statistique.
