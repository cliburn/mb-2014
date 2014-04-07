Develop methods for robust normalization of Flow Cytometry (FCM) data sets.
----------------------------------------

### Objective

In FCM normalization, we are most interested in being able to align common cell subsets across different data samples so that they can be easily compared (or fit with a hierarchical model). Due to the frequent presence of variable numbers of dead cells and outliers in FCM samples, standard methods such as normalizing residuals or quantile normalization often result in poor alignment of cell subsets. Another approach common in image analysis is feature registration – a variant for FCM data used a nonlinear transform to align histogram-based features (modes) across samples. However, this univariate strategy suffers from the need to pre-identify specific features for alignment (since there may be a different number of modes in the histograms), and also in ignoring correlations across parameters.

We propose a new strategy for normalizing flow cytometry data from different batches that exploits batch controls to separate variability from technical and biological sources. Essentially, the method attempts to control for technical variation by performing a multivariate affine transformation that minimizes some measure of divergence across batch controls. We start with a collection of batches (groups of samples), each of which includes one batch control and other data samples. The proposed method works by first fitting Gaussian mixture models (GMM) to the batch control sample within each group. A batch control from each group is then nominated as the reference (e.g. choose sample with the smallest sum of initial divergence measures) to which the batch control sample from the other groups will be aligned. We then estimate the parameters of an affine transformation using numerical optimization to minimize some measure of divergence (e.g. the Kullback-Leibler (KL) divergence) between the reference and target batch control distributions. This affine transform is then applied to each of the samples in the same group as the target control sample for normalization.

We propose to evaluate two alternative strategies for calculating the divergence measure. In the local strategy, we will associate each mixture component in the batch with a mixture component in the reference distribution using the Munkres (Hungarian) algorithm to solve the assignment problem. Optimization will be used to minimize the sum of the component-wise divergences, calculated from the closed form for KL divergence between two multivariate Gaussians. In the global strategy, the objective function for numerical optimization will be the variational lower bound ${{D}_{V}}$ by
\\[
	{{D}_{V}}(P\|Q)\text{ }=\sum\limits_{j}{{{\tau }_{j}}}\log \frac{\sum\limits_{k}{{{\tau }_{k}}}{{e}^{-{{D}_{KL}}({{p}_{j}}\|{{p}_{k}})}}}{\sum\limits_{k}{{{\pi }_{k}}}{{e}^{-{{D}_{KL}}({{p}_{j}}\|{{q}_{k}})}}}
\\]
where ${{\tau }_{z}}$ is the weight of component $z$ in $P$, ${{\pi }_{z}}$ is the weight of component $z$ in $Q$, ${{p}_{j}}$ and ${{q}_{k}}$ are the individual Gaussian mixture components of $P$ and $Q$, and ${{D}_{KL}}({{p}_{j}}\|{{q}_{k}})$ is the KL divergence between component clusters. Conveniently, affine transformations of p-dimensional GMMs are themselves GMMs,
	\\[\left( \sum\limits_{i=1}^{j}{{{\pi }_{i}}}N(x;{{\mu }_{i}},{{\Sigma }_{i}}) \right)A+b\text{ }=\sum\limits_{i=1}^{j}{{{\pi }_{i}}}N(x;{{\mu }_{i}}A+b,{{A}^{T}}{{\Sigma }_{i}}A)\\]
where $A$ is a $p\times p$ matrix and $b$ is a vector of length $p$, enabling efficient numerical optimization to find optimal parameter values.

### Learning objectives

* Biology
    * Flow cytometry and single cell analysis
* Concepts
    * Normalization strategies
	* Affine  transforms
    * Graphical models and algorithms
    * Distance metrics between graphs/distributions
* Computation
	* Elements of statistical programming
	* Literate programming
	* Reproducible report generation
* Specific computational skills
    * Use of git for version control
    * Basics of LaTeX
    * Programming in Python
        * Basics
    	* Machine learning
    	* Graphical models
    	* Statistical visualization
   	* Automation of tasks with Makefiles (e.g. generation of tables and figures for report)

### Research tasks

* Generate outline of report
   * Standard structure of scientific report/paper
   * Use of Markdown for writing/editing
* Identify knowledge gaps
    * Focused literature review to address gaps
* Identify research gaps
    * Focused exploratory analysis to define gaps
    * Propose solution to close gap
    * Implement solution to close gap on toy (simulation) example
    * Apply solution to real data
* Planning and writing
    * Do some brainstorming and planning on whiteboard daily for at least 5-10 minutes
    * Spend at least 15 minutes daily writing draft report (it is much less intimidating to write a little bit every single day)
	* Plan sufficient time for draft revisions
* Meetings (suggested)
    * Long meeting once a week (90 minutes)
    * Short meetings daily to update on progress, identify problems and sketch next steps on whiteboard  (15 minutes)
