
.. image:: pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a_notions.html#pour-un-profil-plutot-economiste

.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a_notions.html#pour-un-profil-plutot-data-scientist

.. _l-td2a-missing-values:

Valeurs manquantes
++++++++++++++++++

.. index:: valeurs manquantes

Les valeurs manquantes sont rarement l'objectif final
d'un système de prédiction mais elles sont souvent sur le chemin.
Pourquoi leur consacrer un chapitre alors qu'il paraît si facile
de les remplacer par la moyenne ? Pourquoi ne pas chercher à
les prédire puisqu'il s'agit d'utiliser une valeur appropriée à la
place de quelque chose qu'on ne connaît ? Les mots-clés importants :
*imputation*, *MICE*, *Amelia*.

Il vaut mieux garder les valeurs manquantes si cela réduit la
base de données de façon trop conséquente. Il y a deux approches,
la première consiste à les remplacer.
La manière naïve qui consiste à remplacer une valeur manquante par sa moyenne
suppose que les variables sont indépendantes ce qui est rarement le cas.
D'autres méthodes tiennent compte des corrélations.

La seconde approche consiste à tenir compte des valeurs
manquantes lors de l'apprentissage et donc à ne pas les remplacer.
La librairie :epkg:`XGBoost` apprend des forêts aléatoires qui définissent
pour chaque noeud des arbres la branche à suivre si
la variable est manquante.

*Notebook*

* :ref:`tdnote20191rst`
* :ref:`tdnote20192rst`

*Lectures*

* `Missing Data <https://en.wikipedia.org/wiki/Missing_data>`_
* `Imputation de données manquantes <https://www.math.univ-toulouse.fr/~besse/Wikistat/pdf/st-m-app-idm.pdf>`_
* `Missing Data & How to Deal: An overview of missing data <https://liberalarts.utexas.edu/prc/_files/cs/Missing-Data.pdf>`_
* `Additive Non-negative Matrix Factorization for Missing Data <https://arxiv.org/abs/1007.0380>`_
* `Scalable Tensor Factorizations for Incomplete Data <https://arxiv.org/pdf/1005.2197.pdf>`_
* `Missing-data imputation <http://www.stat.columbia.edu/~gelman/arm/missing.pdf>`_
* `Check your missing-data imputations using cross-validation <http://andrewgelman.com/2012/03/18/check-your-missing-data-imputations-using-cross-validation/>`_
* `Multiple Imputation for Continuous and Categorical Data: Comparing Joint and Conditional Approaches <http://www.stat.columbia.edu/~gelman/research/published/MI_manuscript_RR.pdf>`_
* `Multiple Imputation by Chained Equations: What is it and how does it work? <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3074241/>`_
* `Much ado about nothing: A comparison of missing data methods and software to fit incomplete data regression models <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1839993/>`_
* `Multivariate Imputation by Chained Equations in R <https://www.jstatsoft.org/article/view/v045i03>`_

*Librairies*

* `fancyimpute <https://github.com/hammerlab/fancyimpute>`_
* `knnimpute <https://github.com/hammerlab/knnimpute>`_
* `scikit-learn/impute <https://scikit-learn.org/stable/modules/impute.html>`_
