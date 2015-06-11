# -*- coding: utf-8 -*-
"""This module contains functions for creating and returning abstract models
based on the project settings. These abstract models will be linked
between them with ManyToMany fields, from the leaves to the roots.
"""

from django.db import models
from django.db.models.loading import get_model
from django.conf import settings

COMPLEX_STRUCTURE = getattr(settings, "COMPLEX_STRUCTURE", None)
COMPLEX_APP_NAME = getattr(settings, "COMPLEX_APP_NAME", None)

abstract_models = {}
abstract_models_data = {}


def process():
    if not (COMPLEX_STRUCTURE or COMPLEX_APP_NAME):
        raise ValueError(
            'COMPLEX_STRUCTURE or COMPLEX_APP_NAME is not set.')
    for root in COMPLEX_STRUCTURE['roots']:
        for entity in root:
            class Meta:
                app_label = COMPLEX_APP_NAME
                abstract = True

            attrs = {'Meta': Meta, '__module__': COMPLEX_APP_NAME + '.models'}
            abstract_models_data[entity] = ['cs_' + entity, attrs]

    countl = 0
    for nodes in COMPLEX_STRUCTURE['nodes']:
        for node in nodes:
            for entity in node:
                # first add module and meta class
                class Meta:
                    app_label = COMPLEX_APP_NAME
                    abstract = True

                attrs = {'Meta': Meta,
                         '__module__': COMPLEX_APP_NAME + '.models'}
                # then add above roots
                for root in COMPLEX_STRUCTURE['roots'][:countl + 1]:
                    for root_entity in root:
                        attrs[root_entity.lower()] = models.ManyToManyField(
                            root_entity, related_name=entity.lower(),
                            verbose_name=root_entity, blank=True, null=True
                        )
                # then add above nodes
                for above_nodes in COMPLEX_STRUCTURE['nodes'][:countl]:
                    for node_list in above_nodes:
                        for node_entity in node_list:
                            attrs[
                                node_entity.lower()] = models.ManyToManyField(
                                node_entity, related_name=entity.lower(),
                                verbose_name=node_entity, blank=True, null=True
                            )
                abstract_models_data[entity] = ['cs_' + entity, attrs]
        countl += 1


def abstract_model(entity_name):
    if len(abstract_models_data) == 0:
        process()
    installed_model = abstract_models.get(entity_name, None)
    if installed_model is None:
        model = abstract_models_data.get(entity_name)
        if model:
            abstract_models[entity_name] = type(
                model[0], (models.Model,), model[1]
            )
            return abstract_models[entity_name]
        else:
            raise ValueError(
                'COMPLEX_STRUCTURE does not contain "%s"' % entity_name)
    else:
        return installed_model


def concrete_model(entity_name):
    if len(abstract_models_data) == 0:
        process()
    return get_model(COMPLEX_APP_NAME, entity_name)
