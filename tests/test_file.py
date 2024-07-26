# -*- coding: utf-8 -*-
# Author; alin m elena, alin@elena.re
# Contribs;
# Date: 26-07-2024
# ©alin m elena, GPL v3 https://www.gnu.org/licenses/gpl-3.0.en.html
import pytest
from data_tutorials.data import get_data
import hashlib
from pathlib import Path

def test_download_file():
   get_data(filename="LiFePO4_supercell.cif",folder="data-test")
   with open(Path("data-test")/"LiFePO4_supercell.cif", "rb") as f:
      h  = hashlib.file_digest(f, "sha256")
   assert h.hexdigest() == "ea9a538dde5bb84b92e9478dbcc078bb560b28a4f5e4b0469d416bff36be272e"
