"""
graph_match_AE
Graph match autoeencoders
"""

# Add imports here
from .models import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
