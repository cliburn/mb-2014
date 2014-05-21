Introductory Activities
----

* Setting up working environment
	* Get a [Github](https://github.com/) account
	* Learn the basics of version control with Git. Start [here](http://rogerdudler.github.io/git-guide/)

* Learning Python
	* Download and install the [Anaconda distribution of Python](http://continuum.io/downloads)
	* Learn how to run and use an [Python notebook](http://ipython.org/notebook.html)
	* Learn how to program in Python from [A Byte of Python](http://swaroopch.com/book/python/)

* Understanding flow cytometry
	* Read [Introduction to Flow Cytometry: A Learning Guide](http://www.stemcell.umn.edu/prod/groups/med/@pub/@med/documents/asset/med_80691.pdf)
	* Read [Interpreting flow cytometry data: a guide for the perplexed](http://www.nature.com/ni/journal/v7/n7/abs/ni0706-681.html)

Daily exercises
----

**May 20, 2014**: Git and IPython notebook

* Try to find out what the following git commands do
    * git init
    * git clone
    * git add
    * git rm
    * git commit
    * git pull
    * git branch
    * git merge
    * git log
    * git show
    * git tag
    * gitk
* Create a repository (test–1) on Githbu and clone to your desktop. Then add soem files to this new repositry, commit and push to Github. You should see the changes on the Github web page.
* Crate a repostoiry (test–2) on your desktop with git init and put some files in it. Now figure out how to make test–2 appear on Github.
* Try to use all the other commands in the list above for the test–1 repostiry, making several commits along the way. Use gitk to view your commit history.
* Create a new Git repository (learn-python). Figure out how to start an ipython notebook. Wrte a function to find the reverse coemplement of a DNA string (see https://bioweb.uwlax.edu/GenWeb/Molecular/Seq_Anal/Reverse_Comp/reverse_comp.html if you don’t know what this is). Test that the funciton works (find out how unit tests are done). Use a Mardkown cell to document the function that you have written. Save and commit the notebook (test-dna.ipynb) to the repository. Now make the repository appear on our Github page.

**May 21, 2014**: IPython notebook

* If you have not already done so, I highly recommend installing the Anaconda Python distribution <http://continuum.io/downloads>
* Start an IPython notebook in the directory containing the learn-python Git repository
* From the Help Menu, click the *User Interface Tour* and *Keyboard Shortcuts* to learn how to use the notebook.
* Apart from the *Help Menu*, you can also type the following to get more information
    * ```?``` : Introduction and overview of IPython's features.
    * ```%quickref```: Quick reference.
    * ```help```: Python's own help system.
    * ```object?```: Details about 'object', use 'object??' for extra details.
* Complete the tutorial at <http://ipython.org/ipython-doc/dev/interactive/tutorial.html>
* Using Rmagic: Replicate the examples at <http://ipython.org/ipython-doc/dev/config/extensions/rmagic.html> in your own notebook
* The numpy module is the foundation for all numerical and statistical coding in Python. Learn how to use numpy arrays here <http://www.sam.math.ethz.ch/~raoulb/teaching/PythonTutorial/intro_numpy.html>
