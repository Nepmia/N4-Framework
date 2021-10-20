# App basic informations and folder paths 

VERSION=0 #Default version, it will be managed by your builder even if you can do it manually which I don't recommend.

NAME="app"
TEMPLATE_FOLDER=f"{NAME}/templates"
STATIC_FOLDER=f"{NAME}/static"
MODULE_FOLDER=f"{NAME}/modules"
ROOT=f"{NAME}/"
COMPONENT_FOLDER=f"{NAME}/components"
PRODUCTION_EXPORT_FOLDER=f"production/{VERSION}"

# Regular Expressions

PAGE_TITLE_REGEX="pageTitle=\"(\S+)\""
COMPONENT_REGEX="\${(\S+)}"


