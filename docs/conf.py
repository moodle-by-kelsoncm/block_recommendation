import moodle_docs_theme

project = "moodle-block_recommendation"
copyright = "2025, Kelson da Costa Medeiros"
author = "Kelson da Costa Medeiros"
release = "0.1.03"

extensions = [
    "sphinx.ext.githubpages",
    "moodle_docs_theme",
]

templates_path = []
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "pt_BR"

html_theme = "moodle_docs_theme"
html_theme_path = [moodle_docs_theme.get_html_theme_path()]

html_theme_options = {
    "project_name": "moodle-block_recommendation",
    "tagline": "Plugin de bloco de recomendações e avisos para Moodle",
    "github_url": "https://github.com/moodle-by-kelsoncm/block_recommendation",
    "github_repo": "moodle-by-kelsoncm/block_recommendation",
    "github_version": "main",
    "doc_path": "docs/",
    "show_edit_on_github": True,
    "enable_dark_mode": True,
    "navigation_links": "Início|index, Instalação|installation, Configuração|configuration, Uso|usage",
}

html_static_path = []
