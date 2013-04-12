djangoP1
Project django mpm4&arg2

Project realized by Marc Pifarré Montalà and Aleix Ribes Grimaldos.

Repository link: https://github.com/mpifa/djangoP1

This repository is based on the creation of a database of video games. This database consists of four main entities Games, Platforms, companies and types.

Initially the database consisted of the following scheme: (Games <-> Platforms (Console Games) <-> Companies

but we saw it was not addapted to our final idea so we made the following changes:

Company ----- MADE ---- Platfoms

Game ----- SupportedBy---- Platforms

Game ----- BelongsTo ---- Type

Game -------- Company

In the Game the company field is directly in relationship with company, because a Game can only be distributed by a company

This Repository contains:

Django APP
Templates
CSS style file
TEST DATA ( SAMPLE DB and IMAGES )
