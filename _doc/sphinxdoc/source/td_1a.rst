
.. _l-td1a:

============================
Algorithmes et programmation
============================

`Algorithmes et Programmation <https://www.ensae.fr/courses/algorithmes-et-programmation/>`_ (ENSAE)

Plan approximatif du cours : :ref:`l-feuille-de-route-2022-1A`.

Cours animé par `Xavier Dupré <http://www.xavierdupre.fr/>`_ depuis 2001.

.. contents::
    :local:
    :depth: 1

.. |slideslogo| image:: _static/slides_logo.png
             :height: 20
             :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx/index.html

Le cours est évalué au premier semestre par la construction d'un
package :epkg:`python` (:ref:`l-examens-1A-algo`) et d'un examen.
Le second semestre est évalué par :ref:`projet informatique <l-projinfo1a>`.
Si vous savez déjà programmer, vous devriez aller jusqu'au bout d'un des énoncés
des :ref:`examens précédents <l-examens>` en moins d'une heure et demie.
L'informatique est plus souvent un outil qu'une matière à part entière.
Le paragraphe :ref:`td1a-notions` propose deux profils d'utilisation
et ce qu'il est suggéré de connaître pour chacun d'entre eux.
Le premier réflexe quand on ne sait pas doit être internet et un moteur
de recherche. `stackoverflow <https://stackoverflow.com/questions/tagged/python>`_,
`quora <https://www.quora.com/topic/Python-programming-language-1>`_
sont des forums d'échanges.
`Cheat Sheets <http://www.xavierdupre.fr/app/ensae_projects/helpsphinx/cheat_sheets.html>`_
est un mot qui vous mène très souvent vers un résumé des syntaxes les
plus utilisées. Les séances seront un sous-ensemble
des contenus proposés ci-dessous. Le cours propose un tour
d'horizon des algorithmes et pratiques logicielles à connaître
pour un ingénieur *full stack*.

Une bonne culture informatique est de plus en plus appréciée
dans le monde de l'entreprise, l'ingénieur *full stack*
est celui qui maîtrise à la fois un domaine métier,
celui pour lequel il a été formé, et les techniques informatiques
qu'il sera amené à manipuler au quotidien. Tous les thèmes ne seront
pas abordés.
Les connaissances en informatique sont hétérogènes après les classes
préparatoires, les énoncés sont à choisir en fonction des lacunes.

.. contents::
    :local:

Au terme du cours, les élèves sauront :

* résoudre un problème avec un assemblage d'algorithmes
* implémenter un algorithme sur les graphes
* construire un module python
* maîtriser les bases des outils python permettant de
  manipuler et représenter les données
* savoir écrire un test unitaire

------------

.. _l-td1a-lesbases:

TD - Les bases
==============

Les premières séances exposent les éléments de syntaxe propres à
la `programmation impérative
<https://fr.wikipedia.org/wiki/Programmation_imp%C3%A9rative>`_
et au langage :epkg:`Python`.

.. toctree::
    :maxdepth: 2

    notebooks/_gs1a_1_premiers_pas
    notebooks/_gs1a_2_variables
    notebooks/_gs1a_3_dictionnaires_fonctions
    notebooks/_gs1a_4_fichier_module
    notebooks/_gs1a_5_classes
    notebooks/_gs1a_6_algo_simple

Les programmes sont des assemblages de petites fonctions qui font souvent
les mêmes choses. Les programmeurs expérimentés sont plus rapides
en partie parce qu'ils accumulent des bouts de codes qu'ils réutilisent.
Voici une idée de ces *mêmes choses* qu'on fait tout le temps
et qu'il est important de comprendre.

.. toctree::
    :maxdepth: 1

    notebooks/code_liste_tuple
    notebooks/exercice_echelle
    notebooks/2020_surface
    notebooks/2020_suffix
    i_examples_classiques
    notebooks/structures_donnees_conversion
    notebooks/tableau_contingence
    notebooks/histogramme_rapide
    notebooks/code_multinomial
    notebooks/matrix_dictionary
    notebooks/coloriage_carre

Au terme de ces séances, si la programmation est nouvelle pour vous ou
si le langage vous paraît encore peu naturel,
je vous encourage à faire d'autres exercices comme
piocher dans les anciens :ref:`l-examens`, à regarder la liste des exercices
proposées à `Quelques exercices du Project Euler
<http://mathprepa.fr/python-project-euler-mpsi/>`_.
La plupart de ces notions font déjà partie du programme
des classes préparatoires scientifiques.

------------

.. _l-td1a-algo-dicho-graphe:

TD - Algorithmes
================

Ces séances sont centrées autour de l'utilisation de la programmation
pour un usage scientifique. Il est rare de recoder un algorithme connu
mais il est rare qu'un algorithme s'applique tel quel sans une quelconque
optimisation pour un problème particulier.
On a souvent des idées pour énumérer les solutions d'un problème
et décrire les premières étapes avec les mains. Et puis, il faut écrire
un algorithme qui fonctionne pour toutes les tailles de problèmes.

#. Peut-on réécrire le problème par **récurrence** ?
   On aboutit le plus souvent à une solution issue de la programmation dynamique.
   Le coût est souvent **quadratique**.
#. Peut-on **couper le problème en deux**, construire une solution sur
   chaque moitié puis recoller les solutions ? On procède de cette façon par dichotomie.
   Le coût est souvent **logarithmique**.

Il est toujours plus facile d'imaginer un algorithme quand on
connaît déjà quelques algorithmes connus.

.. toctree::
    :maxdepth: 2

    notebooks/recherche_dichotomique
    notebooks/nbheap
    notebooks/2020_topk
    specials/algorithm_culture
    specials/np_complet
    specials/graphes
    notebooks/_gs1a_A_programmation_dynamique
    notebooks/_gs1a_A_prog_dyn
    notebooks/_gs1a_A_arbre_graph
    notebooks/_gs1a_A_optimisation_contrainte
    notebooks/_gs1a_A_algo
    notebooks/_gs1a_A_image
    notebooks/_gs1a_A_hash

Il est impossible de connaître tous les algorithmes.
Il est toujours utile d'en apprendre de nouveaux : :ref:`l-algoculture`.
La relecture du TD sur l'optimisation sous contrainte est conseillée
à ceux qui souhaitent optimiser des portefeuilles d'actions.
Il est préférable d'avoir fait la séance sur la distance de Jaccard
avant de faire celle sur la distance d'édition.
L'efficacité d'un algorithme est étroitement liée à la représentation des
données choisies. Le `trie <https://fr.wikipedia.org/wiki/Trie_(informatique)>`_
en est l'illustration.
Les recruteurs testent votre capacité à programmer avec des exercices
où ils vérifient que vous savez écrire du code et comparer la vitesse de deux
algorithmes. Le plus souvent,
il existe une façon naïve d'arriver au résultat et il existe un algorithme plus rapide.
La définition des algorithmes ne dépend pas du langage.
En revanche, il est préférable de bien connaître un langage
pour écrire un code rapide. En python, il est rare de ne pas utiliser :epkg:`numpy`.
Quelques exercices classiques :

.. toctree::
    :maxdepth: 1

    questions/question_2014
    notebooks/exercice_xn
    notebooks/exercice_echelle
    notebooks/exercice_morse
    notebooks/exercice_plus_grande_somme
    notebooks/tri_nlnd

Pour finir, un module :epkg:`python` qui s'intéresse à la résolution
de problème d'optimisation sous contraintes de type
`simplexe <https://fr.wikipedia.org/wiki/Simplexe>`_ :
`python-constraint <https://github.com/python-constraint/python-constraint>`_.

.. _td1a-algo-amusement:

S'amuser avec les algorithmes
+++++++++++++++++++++++++++++

Un peu plus ludique et présentés sous la forme de défis :

* :ref:`l-hermionne`
* `Optimisation de la tournée d'un camion poubelle
  <http://www.xavierdupre.fr/app/ensae_projects/helpsphinx/challenges/city_tour.html>`_ :
  le camion poubelle doit parcourir toutes les rues d'une ville,
  comment trouve-t-il le chemin le plus court ?

.. toctree::
    :maxdepth: 2

    questions/exams_algo_1a

*Quelques sources d'exercices*

* `Rosalind <http://rosalind.info/problems/topics/>`_
* `Google Jam <https://code.google.com/codejam/>`_
  (exemple : `Le problème des milkshakes
  <https://code.google.com/codejam/contest/32016/dashboard#s=p1​>`_)
* :ref:`Algorithmes classiques implémentés <l-blog-algo-impl>`
* `tryalgo <https://github.com/jilljenn/tryalgo>`_

------------

.. _l-td1a-numpy-pandas-plt:

TD - calcul matriciel, graphes, données - data science
======================================================

En dix ans, le langage python s'est imposé comme le premier langage
pour manipuler les données. Il n'est pas le plus efficace
mais c'est celui qui aujourd'hui procure la plus grande agilité.
La séance sur les dataframes propose des outils de manipulation et visualisation
des données utiles pour tous les projets réalisés à l'école.
Ces séances sont centrées sur les outils indispensables pour manipuler
facilement les données et faire des calculs rapides.
Ces outils sont similaires à ceux qu'on trouve dans de nombreux languages à usage scientifique
(`R <http://www.r-project.org/>`_, `SciLab <http://www.scilab.org/fr>`_,
`Julia <http://julialang.org/>`_, `Octave <http://www.gnu.org/software/octave/>`_, ...).
Ces séances peuvent paraître plus longues car elles
s'appuient sur des modules qu'il faut découvrir
puis utiliser pour résoudre des exercices. Toutefois, les modules
:epkg:`numpy`, :epkg:`pandas`, :epkg:`matplotlib`
sont incontournables pour manipuler les données en :epkg:`Python`.

.. toctree::
    :maxdepth: 1

    notebooks/2020_regex
    notebooks/2022_serialisation
    notebooks/td1a_cenonce_session_10
    notebooks/td1a_correction_session_10
    notebooks/decorrelation
    notebooks/decorrelation_correction
    notebooks/td1a_cython_edit
    notebooks/td1a_cython_edit_correction
    notebooks/td1a_cenonce_session_12_plot
    notebooks/td1a_cenonce_session_12_carte
    notebooks/td1a_cenonce_session_12_js
    notebooks/td1a_correction_session_12

Il existe de nombreuses librairies de visualisation des données en :epkg:`Python` et
elles se sont multipliées depuis l'avènement des notebooks :
`10 plotting libraries at PyData 2016
<http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2016/pydata2016.html>`_.

S'amuser avec des données
+++++++++++++++++++++++++

Une fois qu'on est agile avec les données, on peut facilement explorer,
émettre des hypothèses ou résoudre quelques énigmes :

* `Que font les habitants de Chicago après le travail ? <http://www.xavierdupre.fr/app/ensae_projects/helpsphinx/challenges/city_bike.html>`_
  (ceux qui font du vélo tout du moins)

------------

.. _l-td1a-ut-flask-profiling:

TD - Site web et pratiques logicielles
======================================

Le langage :epkg:`Python` est au programme des classes préparatoires scientifiques
(`Prise en main du logiciel Python <https://www.ac-paris.fr/portail/jcms/p1_742307/prise-en-main-du-logiciel-python>`_)
et les étudiants ont déjà vu ou parcouru des exercices algorithmiques
(voir `MathPrepas, Programmation en Python <http://mathprepa.fr/python-project-euler-mpsi/>`_).
**Cette partie s'adesse essentiellement à ceux qui ont déjà programmé.**
On peut se pencher sur d'autres aspects logiciels tels que les
tests unitaires, le templating, les sites Web, le scraping, encoding, les notebooks...
Les **tests unitaires** et **git** font partie des pratiques logicielles qu'il faut
connaître pour écrire du code sans trop de bugs et qu'il faut appliquer
dès qu'un programme est conçu pour durer.

*Lectures*

.. toctree::
    :maxdepth: 1

    specials/siteflask
    specials/unittest_coverage_git_profling
    notebooks/git_notebook
    notebooks/profiling_example
    notebooks/2020_profile
    notebooks/2022_profiling
    notebooks/notebook_convert
    notebooks/jupyter_custom_magics
    specials/python_cplusplus
    specials/gui
    notebooks/2022_unit_test

*Exercices*

.. toctree::
    :maxdepth: 2

    notebooks/_gs1a_B_ci
    notebooks/_gs1a_B_sql
    notebooks/_gs1a_S_cython

Deux exercices sont suggérés pour une séance de deux heures à choisir parmi :

#. Appliquer une des méthodes décrites dans
   `Profiling <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/notebooks/completion_profiling.html#completionprofilingrst>`_
   à un exercice d'une séance précédente
#. Concevoir une campagne publicataire avec

------------

.. _td1a-notions:

Les notions qu'il faut avoir comprises ou vues
==============================================

* Les bases du langage :epkg:`Python` : boucles, tests, fonctions,
  listes, dictionnaires,
  modules, expressions régulières.
* Les classes.
* Le tri, la recherche dichotomique, la programmation dynamique
  (plus court chemin dans un graphe, distance d'édition).
* La notion de coût algorithmique.
* Notion de graphes et de parcours dans un graphe
  (connexité, ordonnancement, chemin hamiltonien).
* Le calcul matriciel, les dataframes, les graphes (cartes).
* Le format JSON, la sérialisation.
* Les tests unitaires.
* `Git <https://fr.wikipedia.org/wiki/Git>`_.

Séance notée
++++++++++++

La dernière séance est une séance notée. Tous les documents sont autorisés.
Les examens passés sont disponibles : :ref:`l-examens`. Les examens sont plutôt
destinés à ceux qui viennent de commencer la programmation. Si votre pratique
est régulière, vous devriez aller trois fois plus vite à la fin de la scolarité.

.. _l-td1a-start:

------------

Getting started
===============

Il faut vous reporter à la section :ref:`l-installation-courte`
pour installer :epkg:`Python`. Certaines séances pratiques
utilisent des données depuis ce site. Elles sont facilement
téléchargeables avec ces deux modules :epkg:`pyquickhelper`.

Il faut ensuite un outil pour écrire des programmes.
Si la majorité des exemples sont fournis sous forme de
:epkg:`notebook` mais ce n'est pas le seul environnement de
travail ce qu'on surnomme un :ref:`l-gs-ide`.
:epkg:`Spyder` ou :epkg:`PyCharm`. Sous Windows,
:epkg:`PTVS` dispose d'un bon débuggeur. L'éditeur le plus utilisé
est :epkg:`Visual Studio Code`. Il dispose de nombreuses extensions dont une
pour travailler sur une machine distante.

.. _l-td1a-biblio:

------------

Bibliographie
=============

*Cheat Sheet*

* `Résumé de la syntaxe <http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_resume/python_sheet.html>`_
* :epkg:`teachpyx` : notes de cours sur le langage :epkg:`Python`
* `Aide Mémoire Python <http://www.le-memento.fr/python.html>`_
* `Python Cheat Sheets <https://github.com/Naereen/pysheeet>`_, aborde des sujets
  rares comme les sockets, l'API C, ...

*Liens*

* `Message de service aux débutants en Python
  <http://sametmax.com/message-de-service-aux-debutants-en-python/>`_
* `Cours et tutos <http://sametmax.com/cours-et-tutos/>`_
* `Les trucmuchables en Python <http://sametmax.com/les-trucmuchables-en-python/>`_
  (iterable, mutable, immutable, ...)
* `A gallery of interesting IPython Notebooks
  <https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks>`_
* `Data Science in Python <http://blog.yhathq.com/posts/data-science-in-python-tutorial.html>`_
* `Installer Python pour faire des statistiques
  <http://www.xavierdupre.fr/blog/2014-02-26_nojs.html>`_
* `Exercices de programmation
  <http://www.xavierdupre.fr/blog/2014-03-22_nojs.html>`_
* `De l'idée au programme informatique
  <http://www.xavierdupre.fr/blog/2013-11-08_nojs.html>`_
* `Questions Fréquentes <https://docs.python.org/3/faq/index.html>`_
* :ref:`l-FAQs`
* :ref:`l-glossary`
* :ref:`l-questions`
* `Débugger en Python <http://www.xavierdupre.fr/blog/2014-06-02_nojs.html>`_
* `Modules standards <https://docs.python.org/3/library/>`_
* `8 Regular Expressions You Should Know
  <http://code.tutsplus.com/tutorials/8-regular-expressions-you-should-know--net-6149>`_ *(2016/03)*
* `Love Python <http://love-python.blogspot.fr/>`_ *(2016/03)*
* `The Hitchhiker's Guide to Python!
  <http://docs.python-guide.org/en/latest/>`_ *(2016/06)*
* `Evolution of a salesman: A complete genetic algorithm tutorial for Python
  <https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35>`_

*Livres*

* `Apprentissage de la programmation
  <http://inforef.be/swi/python.htm>`_, Gérald Swinnen
* `Une introduction à Python 3
  <https://perso.limsi.fr/pointal/python:courspython3>`_
* `Programmation avec le langage Python
  <http://www.xavierdupre.fr/site2013/documents/python/initiation_via_python_ellipse_mai_2010.pdf>`_
  (PDF, ou version `Ellipse <http://www.editions-ellipses.fr/product_info.php?products_id=6891>`_),
  version web et plus récentes : :epkg:`teachpyx`.
* `Teach Yourself Python in 24 Hours
  <http://www.pauahtun.org/TYPython/>`_, Ivan Van Laningham
  (le site est visuellement difficile, `version PDF
  <http://ptgmedia.pearsoncmg.com/images/9780672336874/samplepages/0672336871.pdf>`_)
* `Précis de recherche opérationnelle
  <http://www.eyrolles.com/Informatique/Livre/precis-de-recherche-operationnelle-9782100706129>`_,
  Robert Faure, Bernard Lemaire, Christophe Picouleau
* `Problem Solving with Algorithms and Data Structures
  <https://www.cs.auckland.ac.nz/courses/compsci107s1c/resources/ProblemSolvingwithAlgorithmsandDataStructures.pdf>`_,
  Brad Miller, David Ranum (version `html <http://interactivepython.org/courselib/static/pythonds/index.html>`_)
* `Automate Boring Stuff with Python <https://automatetheboringstuff.com/>`_ (2016/03)
* `Intermediate Python Release <http://pythontips.com/2015/08/17/intermediate-python-released/#more-665>`_ (2016/03)

*Cours*

* `Apprenez à programmer en Python <http://openclassrooms.com/courses/apprenez-a-programmer-en-python>`_ (openclassrooms)
* `A gallery of interesting Jupyter Notebooks <https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks>`_
* `Python Notes <http://www.thomas-cokelaer.info/tutorials/python/index.html>`_
* `Program Arcade Games With Python And Pygame <http://programarcadegames.com/>`_
* `Python cours et TPs <http://mathcpge.org/index.php?option=com_content&view=article&id=55&Itemid=146>`_ *(2016/04)*
* `Le Python en prépas <http://web.isen-bretagne.fr/livres/python/>`_ (2016/04)
* `Algorithmique et programmation en CPGE <http://python-liesse.enseeiht.fr/cours/index.html>`_ *(2016/04)*

*Exercices et jeux*

* `codingame <http://www.codingame.com/>`_
* `Quelques exercices du Project Euler <http://mathprepa.fr/python-project-euler-mpsi/>`_ *(2016/04)*
* `Countdown to 2016 <http://nbviewer.jupyter.org/url/norvig.com/ipython/Countdown.ipynb>`_ *(2016/08)*
* `The Convex Hull Problem <http://nbviewer.jupyter.org/url/norvig.com/ipython/Convex%20Hull.ipynb>`_ *(2016/08)*
* `Rosalind <http://rosalind.info/problems/topics/>`_ *(2016/09)*

*MOOC*

* `Code Academy Python <http://www.codecademy.com/tracks/python>`_ (utilise Python 2.7)
* `Un premier Mooc Inria sur Python <https://www.france-universite-numerique-mooc.fr/courses/inria/41001/Trimestre_4_2014/about>`_
* `pyvideo.org <http://pyvideo.org/>`_

*Outils*

* `PythonTutor <http://pythontutor.com/>`_ : pour suivre pas à pas l'exécution d'un programme (petit)

A propos du cours
=================

Ce cours a commencé en 2004 et n'a cessé de s'enrichir.
Il est animé par `Xavier Dupré <mailto:xavier.dupre AT gmail.com>`_ (ENSAE 1999).
Il a pour objectif d'introduire la programmation avec
:epkg:`Python`, des algorithmes, et de présenter quelques pratiques
tirées de l'industrie logicielle. Les deux derniers points sont
assez rarement évoqués dans le cursus scolaire français mais
revêt de plus en plus d'importance en datascience.

.. toctree::
    :maxdepth: 1

    questions/route_1A_2018
    questions/route_1A_2019
    questions/route_1A_2020
    questions/route_1A_2021
    questions/route_1A_2022
