.. _configuration:

Configuration
=============

escaddocs_vars
--------------

**Sphinx-escaddocs** provides the config variable ``escaddocs_vars``, which must be a dictionary.
The key is used as identifier inside scss-files and the value must be a css/scss compatible string.

**Example conf.py**

.. code-block:: python

   escaddocs_vars = {
       'primary': '#FA2323',
       'secondary': '#379683',
       'cover': '#ffffff',
       'white': '#ffffff',
       'links': 'FA2323',
       'cover-bg': 'url(cover-bg.jpg) no-repeat center',
       'cover-overlay': 'rgba(250, 35, 35, 0.5)',
       'top-left-content': 'counter(page)',
       'bottom-center-content': '"Custom footer content"',
   }

This values are used then inside the scss files, which define the PDF layout.

Config vars
~~~~~~~~~~~

:primary: Primary color
:primary_opaque: Primary color with opaqueness. Example ``rgba(150, 26, 26, .5)``
:secondary: Secondary color
:cover: Text color on the cover
:white: A color representing white
:links: Color for links
:cover-bg: Cover background image. Can be a single color or even an image path.
:cover-overlay: RBG based color overlay for the cover-image. Example: ``rgba(250, 35, 35, 0.5)``
:top-left-content: Text or css function to display on pdf output. Example: ``counter(page)``
:top-center-content: Text or css function to display on pdf output.
:top-right-content: Text or css function to display on pdf output.
:bottom-left-content: Text or css function to display on pdf output.
:bottom-center-content: Text or css function to display on pdf output.
:bottom-right-content: Text or css function to display on pdf output.


All variables are defined inside ``/themes/sphinx_escaddocs/sttuc/stles/sources/_variables.scss``.

.. hint::

   If a content-string shall be set, please make sure to use extra `"` around the string.
   Example: `'bottom-center-content': '"Custom footer content"'`.

Examples
~~~~~~~~
The values from the configuration are taken as they are and injected into ``scss`` files, which are used to generate
the css files. So each value or command, which is supported by ``scss``, can be set.

Color selection
+++++++++++++++
.. code-block:: python

   escaddocs_vars = {
       'primary': '#FA2323',
       'cover-overlay': 'rgba(250, 35, 35, 0.5)',
   }

File references
+++++++++++++++
.. code-block:: python

   escaddocs_vars = {
       'cover-bg': 'url(cover-bg.jpg) no-repeat center'
   }

The file path must be relative to the Sphinx _static folder.
So in the above example the image is stored under ``/_static/cover-bg-jpg``.

escaddocs docs
++++++++++++++
This is ``escaddocs_vars`` as it is used inside the **Sphinx-escaddocs** ``conf.py`` file:

.. literalinclude:: conf.py
   :lines: 36-39

.. _escaddocs_file_name:

escaddocs_file_name
-------------------
.. versionadded:: 1.5

File name of the resulting PDF file in the ``escaddocs`` build folder.
If not set, the project name is used.

File name and extension can be set. But it should not be used to manipulate the output path.

Example::

   escaddocs_file_name = "my_cool.pdf"



Default: project name

escaddocs_debug
----------------
A boolean value. If set to ``True``, **Sphinx-escaddocs** will add some debug information add the end of the PDF.

This contains data about the used Python Environment and the Sphinx project.
It is mainly used if any problems occur and extra information is needed.

``escaddocs_debug = True``

You can see an example in our :download:`PDF Demo <_static/Sphinx-escaddocs-DEMO.pdf>` at the end of the file.

.. warning::

   The debug output contains absolute file paths and maybe other critical information.
   Do not use for official PDF releases.

escaddocs_use_weasyprint_api
----------------------------
.. versionadded:: 1.6

This forces escaddocs to use the weasyprint `python API <https://doc.courtbouillon.org/weasyprint/stable/api_reference.html#python-api>`_ instead of calling the binary via subproces.

``escaddocs_use_weasyprint_api = True``

.. warning::

   Other variables like `escaddocs_weasyprint_flags`_ will not work when using the API.

escaddocs_weasyprint_flags
--------------------------
.. versionadded:: 1.5

List of flags to pass to **weasyprint** subprocess. This may be helpfull in debugging the pdf creation

``escaddocs_weasyprint_flags = ['-v']``

.. warning::

   The flags should only pass switches to **weasyprint**, input and output file names are appended by **Sphinx-escaddocs**

escaddocs_weasyprint_timeout
----------------------------
.. versionadded:: 1.5

In rare cases **weasyprint** seems to run into infinite loops during processing of the input file.
To avoid blocking CI jobs a timeout can be configured. The build is aborted with a ``subprocess.TimeoutExpired`` exception.

``escaddocs_weasyprint_timeout = 300``

escaddocs_weasyprint_retries
----------------------------
.. versionadded:: 1.6

In rare cases **weasyprint** seems to run into infinite loops during processing of the input file.
In case a ``subprocess.TimeoutExpired`` exception occured and retries are configured **weasyprint** is started again.

``escaddocs_weasyprint_retries = 1``

escaddocs_theme
---------------
.. versionadded:: 1.5

Add custom theme for escaddocs. This overrides the default theme ``escaddocs_theme``

.. _theme_options:

escaddocs_theme_options
-----------------------
.. versionadded:: 1.5

Additional options for the theme. The default theme ``escaddocs_theme`` inherits all options from the **Sphinx Basic Theme**.

``escaddocs_theme`` options:

:nocover: Do not display cover pages (front and back cover)


escaddocs_weasyprint_filter
---------------------------
.. versionadded:: 1.6

If **weasyprint** is used as executable the output contains warnings and errors from **weasyprint**.
To reduce output noise the output can be filtered by a list of regular expressions given in this configuration option.

``escaddocs_weasyprint_filter = ["WARNING: Ignored"]``

To suppress all output, the quite flag `-q` should be used.
