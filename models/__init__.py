#!/bin.usr/python3
import os
import sys

working_path = os.getcwd()
parent_dir = os.path.dirname(working_path)
sys.path.append(working_path)

from models.engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()

