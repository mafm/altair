# This file auto-generated by altair.schema.parser.write_files().
# do not modify directly.

import traitlets as T
from ..baseobject import BaseObject
from .scaletype import ScaleType
from .nicetime import NiceTime


class Scale(BaseObject):
    padding = T.CFloat(default_value=None, allow_none=True, help="""Applies spacing among ordinal elements in the scale range.""")
    clamp = T.Bool(default_value=None, allow_none=True, help="""If true, values that exceed the data domain are clamped to either the minimum or maximum range value.""")
    exponent = T.CFloat(default_value=None, allow_none=True, help="""Sets the exponent of the scale transformation.""")
    type = T.Instance(ScaleType, default_value=None, allow_none=True)
    zero = T.Bool(default_value=None, allow_none=True, help="""If true, ensures that a zero baseline value is included in the scale domain.""")
    nice = T.Union([T.Bool(default_value=None, allow_none=True), T.Instance(NiceTime, default_value=None, allow_none=True)])
    range = T.Union([T.Unicode(default_value=None, allow_none=True), T.List(T.CFloat(default_value=None, allow_none=True), default_value=None, allow_none=True), T.List(T.Unicode(default_value=None, allow_none=True), default_value=None, allow_none=True)])
    bandSize = T.CFloat(default_value=None, allow_none=True, min=0)
    includeRawDomain = T.Bool(default_value=None, allow_none=True, help="""Uses the source data range as scale domain instead of aggregated data for aggregate axis.""")
    domain = T.Union([T.Unicode(default_value=None, allow_none=True), T.List(T.CFloat(default_value=None, allow_none=True), default_value=None, allow_none=True), T.List(T.Unicode(default_value=None, allow_none=True), default_value=None, allow_none=True)])
    round = T.Bool(default_value=None, allow_none=True, help="""If true, rounds numeric output values to integers.""")
