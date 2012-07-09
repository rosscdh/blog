Date: 2012-07-06 09:00:00
Title: Python Cubes
Tags: python,cubes,big data
Category: 2012europython
Slug: euro-python-cubes

# Cubes #

- json data objects that allow you to describe data facets
- comes with simple tools and an admin interface
- batteries included: sql interfaces; used to have mongo but that was dropped; customizable interfaces are possible
- the browser does the logical to data mapping

### The Cell ###

** The core aspect **

- star formation model or snowflake formation schema
- a cell is a form of filter of the data: from the users perspective
- multi-dimensional breadcrumbs form the users perspective
- cells are composed of paths; depending on the hierarchy of the dimensions
- dimensions can be drilled-down into and very simple via the browser GUI
- can specify dimensions to drill down into
- _seems to be using pandas_ ?
- can get browser.facts(cell) browser.vales(cell dimension) browser.cell_details(cell)
- can specify page size and page number

### DB features ###

- only requires read access as it takes that db and stores it locally


### Slicer ###

- model validation
- model translation
- workspace testing
- denormalization

### The Future ###

- pandas is coming as a feature for derived measures
- open data; shared repo of models
- shared repo of dimensions
- public cubes


Looks to be a very interesting little tool; but i think pandas is somewhat easier at conceptual level (but does not have the pretty interface)... <http://packages.python.org/cubes/> <https://github.com/Stiivi/cubes>