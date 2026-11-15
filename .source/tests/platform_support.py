"""Shared platform requirement for tests that exercise native anchored I/O."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import scope_io

requires_anchored_io = unittest.skipUnless(
    scope_io.supports_anchoring(), 'requires native anchored filesystem I/O'
)
