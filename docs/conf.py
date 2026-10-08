# Configuration file for the Sphinx documentation builder.
project = 'moodle-block_recommendation'
copyright = '2025, Kelson da Costa Medeiros'
author = 'Kelson da Costa Medeiros'
release = '0.1.03'

extensions = [
    'moodle_docs_theme',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'moodle_docs_theme'
html_static_path = ['_static']

html_theme_options = {
    'github_repo': 'moodle-by-kelsoncm/block_recommendation',
    'show_edit_on_github': True,
}
