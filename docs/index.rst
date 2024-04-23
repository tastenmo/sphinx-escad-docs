.. sphinx-escad-docs documentation


Sphinx-escad-docs
==================

This Sphinx extension provides an easy way to build html and PDF documents.

It contains:

 * A PDF specific, CSS based basic Sphinx theme: ``sphinx_escaddocs``.
 * A Sphinx builder, called ``escaddocs``
 * :ref:`Directives <directives>` to

   * control different structures and content for ``HTML`` and ``PDF`` builds.
   * embed PDF inside HTML views.

It is using `weasyprint <https://weasyprint.org/>`__ as PDF generator.


.. note::

    This extension is in a beta phase.

    It is not bug free and documentation is also missing some minor stuff.
    You can help us to make it better by reporting bugs or by providing code/docs
    changes via a PR.
    
    The code is available on github: `tastenmo/sphinx-escad-docs <https://github.com/tastenmo/sphinx-escad-docs.git>`__
    
    A mirror is available on csvn: `Docs/sphinx-escad-docs <http://csvn:3000/Docs/sphinx-escad-docs.git>`__



Showcase
--------
| **Sphinx-escad-docs Documentation**
| The PDF is based on the current HTML documentation.
| :download:`Download PDF </_static/Sphinx-Escad-docs.pdf>`

.. if-builder:: html

    .. pdf-include:: _static/Sphinx-Escad-docs.pdf#view=Fit


| **Sphinx-SimplePDF Demo**
| A PDF containing different content types to check the handling of them by Sphinx-SimplePDF.
| :download:`Download PDF </_static/ESCAD-Document-template.pdf>`

.. if-builder:: html

    .. pdf-include:: _static/ESCAD-Document-template.pdf#view=Fit


.. if-builder:: escaddocs

    .. toctree::

       quickstart
       installation
       building
       configuration
       directives
       css
       tech_details
       changelog
       license


.. if-builder:: HTML

    .. include:: quickstart.rst

    Why another PDF builder?
    ------------------------

    You can use the Sphinx Latex builder to generate PDFs.
    And there is also the great `rinohtype <http://www.mos6581.org/rinohtype/master/#>`__ library.

    But both have some drawbacks, which we try to avoid with this solution.

    Latex distributions are quite big and Latex as language may not be the language of choice for everybody.

    rinohtype makes a lot of things easier, but it does not support additional Sphinx extensions very well
    (if they are using visitor-functions). For instance is it hard to get PlantUML running with rinohtype.

    But for sure, there are also scenarios where **Sphinx-SimplePDF** may not be the best solution.
    So if you are unhappy with **Sphinx-SimplePDF** please try the others as well :)

    One last thing ...
    ------------------
    This theme is heavily based on the excellent work of `Nekmo <https://github.com/Nekmo>`__ for the
    `Sphinx Business Theme <https://github.com/Nekmo/sphinx-business-theme>`__.

    Without this work, this theme would never exist. Thanks for it ♥


    .. toctree::
       :caption: Content
       :maxdepth: 3

       installation
       building
       configuration
       directives
       css
       tech_details
       examples/index
       changelog
       license

.. if-builder:: JSON

    .. include:: quickstart.rst

    Why another PDF builder?
    ------------------------

    You can use the Sphinx Latex builder to generate PDFs.
    And there is also the great `rinohtype <http://www.mos6581.org/rinohtype/master/#>`__ library.

    But both have some drawbacks, which we try to avoid with this solution.

    Latex distributions are quite big and Latex as language may not be the language of choice for everybody.

    rinohtype makes a lot of things easier, but it does not support additional Sphinx extensions very well
    (if they are using visitor-functions). For instance is it hard to get PlantUML running with rinohtype.

    But for sure, there are also scenarios where **Sphinx-SimplePDF** may not be the best solution.
    So if you are unhappy with **Sphinx-SimplePDF** please try the others as well :)

    One last thing ...
    ------------------
    This theme is heavily based on the excellent work of `Nekmo <https://github.com/Nekmo>`__ for the
    `Sphinx Business Theme <https://github.com/Nekmo/sphinx-business-theme>`__.

    Without this work, this theme would never exist. Thanks for it ♥


    .. toctree::
       :caption: Content
       :maxdepth: 3

       installation
       building
       configuration
       directives
       css
       tech_details
       examples/index
       changelog
       license