=================================
ColorCorner Software
=================================

This is a software based on corner.py (https://corner.readthedocs.io/en/latest/)
for 2d plots switched to color map [0,1] (including CL contours and scatter points) 
and 1d histograms switched to smooth density curves.

.. image::  /figures/2plots.png
- plot_scatter=True (left) , plot_scatter=False (right)

Installation
---------

Here is the console command:

.. code-block:: console

    $ pip install colorcorner

Usage [example]
---------

.. code:: python

    import numpy as np
    import matplotlib.pyplot as plt
    import colorcorner.colorcorner as cc
    
    x = np.random.normal(0,1,10000)
    y = np.random.normal(0,1,10000)
    z = np.random.normal(0,1,10000)
    
    labels = ['$\\alpha', '$\\beta$', '$\gamma$']
    
    fig = cc.plot(
                    np.transpose([x,y,z]), 
                    smooth1d=2,
                    color1d='b',
                    labels=labels,
                    cmap='jet',
                    CL=[30,60,90], # confidence levels of 30%, 60% and 90%
                    CL_color='r',  # color of the CL curves
                    plot_scatter=True,
                    scatter_color='w'
                )
    
    plt.show()

=================================  
API
=================================

.. sourcecode:: js

	{
	    "count": 1000,
	    "previous": null,
	    "results": [VERSIONS],
	    "next": "https://readthedocs.org/api/v2/version/?limit=10&offset=10"
	}


:>json string next: URI for next set of Versions.
:>json string previous: URI for previous set of Versions.
:>json integer count: Total number of Versions.
:>json array results: Array of ``Version`` objects.

:query string project__slug: Narrow to the versions for a specific ``Project``
:query boolean active: Pass ``true`` or ``false`` to show only active or inactive versions.
By default, the API returns all versions.

=================================  
About the Author
=================================

- Josiel Mendonça Soares de Souza (https://github.com/jmsdsouzaPhD)
- PhD in Physics by Universidade Federal do Rio Grande do Norte, Brazil
- Research Field: Gravitation, Cosmology and Gravitational Waves

=================================
License
=================================

MIT License

.. image:: /figures/logo3D.png

