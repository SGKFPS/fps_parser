# FPS parser and clean-up tool

This module is a collection of scripts and tools shared among FPS developers and data analysts that handles parsing and cleaning up raw input data.

The module is divided into two parts: the **parser** and the **clean-up** tool.

The **parser** is responsible for parsing the raw input data. It contains source specific functions and scripts that are responsible for combining and exporting all the raw data into a single Pandas Dataframe according to the requirements of each FPS tool/module (usually one per location).

The **clean-up** is responsible for cleaning up the collection of raw data and preparing them as inputs for the FPS tools/modules.

