
from hdmf import docval
from hdmf.utils import popargs_to_dict
from pynwb import register_class
from pynwb.file import LabMetaData, Subject


@register_class('BioSample', "ndx-biosample")
class BioSample(LabMetaData):
    __nwbfields__ = (
        "sameAs",
        "hasMember",
        "SampleType",
        "AssayType",
        "Anatomy",
    )

    @docval(
        dict(
            name="name",
            type=str,
            doc="The name of this BioSample.",
        ),
        dict(
            name="SampleType",
            type=str,
            doc="Type of sample.",
        ),
        dict(
            name="sameAs",
            type=str,
            shape=(None, ),
            doc="Identifiers for other BioSamples that are the same as this.",
            default=None,
        ),
        dict(
            name="hasMember",
            type=str,
            shape=(None, ),
            doc="Identifiers of members of this BioSample.",
            default=None,
        ),
        dict(
            name="AssayType",
            doc="Assay type.",
            type=str,
            default=None,
            shape=(None, ),
        ),
        dict(
            name="Anatomy",
            doc="Anatomy.",
            type=str,
            default=None,
            shape=(None, ),
        ),
        dict(
            name="wasAttributedTo",
            doc="Participant(s) or Subject(s) associated with this sample.",
            default=None,
            type=Subject,
            shape=(None, ),
        ),
        dict(
            name="wasDerivedFrom",
            doc="Describes the hierarchy of sample derivation or aggregation.",
            default=None,
            type="BioSample",
            shape=(None, ),
        ),
    )
    def __init__(self, **kwargs):
        args_to_set = popargs_to_dict(
            (
                "sameAs",
                "hasMember",
                "SampleType",
                "AssayType",
                "Anatomy",
                "wasAttributedTo",
                "wasDerivedFrom",
            ),
            kwargs,
        )
        super().__init__(**kwargs)
        for key, val in args_to_set.items():
            setattr(self, key, val)
