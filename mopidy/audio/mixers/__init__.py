import pygst
pygst.require('0.10')
import gst
import gobject

from .auto import AutoAudioMixer
from .fake import FakeMixer
from .nad import NadMixer


def register_mixer(mixer_class):
    gobject.type_register(mixer_class)
    gst.element_register(
        mixer_class, mixer_class.__name__.lower(), gst.RANK_MARGINAL)


def register_mixers():
    register_mixer(AutoAudioMixer)
    register_mixer(FakeMixer)
    register_mixer(NadMixer)
