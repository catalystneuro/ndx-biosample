# -*- coding: utf-8 -*-
import os.path

from pynwb.spec import (
    export_spec,
    NWBNamespaceBuilder,
    NWBGroupSpec,
    NWBAttributeSpec,
    NWBRefSpec,
    NWBLinkSpec, NWBDatasetSpec,
)


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc="""My NWB extension""",
        name="""ndx-biosample""",
        version="""0.1.0""",
        author=list(map(str.strip, """Ben Dichter""".split(','))),
        contact=list(map(str.strip, """ben.dichter@catalystneuro.com""".split(',')))
    )

    # TODO: specify the neurodata_types that are used by the extension as well
    # as in which namespace they are found.
    # this is similar to specifying the Python modules that need to be imported
    # to use your new data types.
    # all types included or used by the types specified here will also be
    # included.
    ns_builder.include_type("LabMetaData", namespace="core")

    # TODO: define your new data types
    # see https://pynwb.readthedocs.io/en/latest/extensions.html#extending-nwb
    # for more information

    BioSample = NWBGroupSpec(
        neurodata_type_def="BioSample",
        neurodata_type_inc="LabMetaData",
        doc="Description of the sample that was studied.",
        attributes=[
            NWBAttributeSpec(
                name="sameAs",
                doc="same as",
                dtype="text",
                shape=(None,),
                required=False,
            ),
            NWBAttributeSpec(
                name="hasMember",
                doc="has member",
                dtype="text",
                shape=(None,),
                required=False,
            ),
            NWBAttributeSpec(
                name="SampleType",
                doc="Sample type",
                dtype="text",
                required=True,
            ),
            NWBAttributeSpec(
                name="AssayType",
                doc="Assay type",
                required=False,
                shape=(None, ),
                dtype="text",
            ),
            NWBAttributeSpec(
                name="Anatomy",
                doc="Anatomy",
                required=False,
                shape=(None, ),
                dtype="text",
            ),
            NWBAttributeSpec(
                name="wasDerivedFrom",
                doc="Describes the hierarchy of sample derivation or aggregation.",
                required=False,
                shape=(None, ),
                dtype=NWBRefSpec(
                    reftype="object",
                    target_type="BioSample",
                )
            ),
            NWBAttributeSpec(
                name="wasAttributedTo",
                doc="Participant(s) or Subject(s) associated with this sample.",
                required=False,
                dtype=NWBRefSpec(
                    reftype="object",
                    target_type="Subject",
                ),
                shape=(None, ),
            ),
        ],
        datasets=[
            NWBDatasetSpec(
                name="wasDerivedFrom",
                doc="Describes the hierarchy of sample derivation or aggregation.",
                quantity="?",
                dtype=NWBRefSpec(
                    target_type="BioSample",
                    reftype="object",
                ),
            )
        ]
    )

    # TODO: add all of your new data types to this list
    new_data_types = [BioSample, ]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)
    print('Spec files generated. Please make sure to rerun `pip install .` to load the changes.')


if __name__ == '__main__':
    # usage: python create_extension_spec.py
    main()
