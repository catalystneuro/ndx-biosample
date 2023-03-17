from pynwb import NWBHDF5IO
from pynwb.testing.mock.file import mock_NWBFile

from ndx_biosample import BioSample


def test_biosample():

    biosample1 = BioSample(
        name="biosample1",
        SampleType="blood",
    )

    biosample2 = BioSample(
        name="biosample2",
        SampleType="blood",
        wasDerivedFrom=biosample1,
    )

    nwbfile = mock_NWBFile()
    nwbfile.add_lab_meta_data(biosample1)
    nwbfile.add_lab_meta_data(biosample2)

    with NWBHDF5IO("test_write.nwb", "w") as io:
         io.write(nwbfile)

    with NWBHDF5IO("test_write.nwb", "r") as io:
        nwbfile = io.read()
        assert nwbfile.lab_meta_data["biosample1"].SampleType == "blood"
    #     assert nwbfile.lab_meta_data["biosample2"].wasDerivedFrom[0] == nwbfile.lab_meta_data["biosample1"]

# class TestBioSampleRoundtrip(NWBH5IOMixin, TestCase):
#     """Simple roundtrip test for TetrodeSeries."""
#
#     def setUpContainer(self):
#         return BioSample(
#
#         )
#
#     def tearDown(self):
#         remove_test_file(self.path)
#
#     def test_roundtrip(self):
#         """
#         Add a TetrodeSeries to an NWBFile, write it to file, read the file, and test that the TetrodeSeries from the
#         file matches the original TetrodeSeries.
#         """
#         all_electrodes = self.nwbfile.create_electrode_table_region(
#             region=list(range(0, 10)),
#             description='all the electrodes'
#         )
#
#         data = np.random.rand(100, 3)
#         tetrode_series = TetrodeSeries(
#             name='TetrodeSeries',
#             description='description',
#             data=data,
#             rate=1000.,
#             electrodes=all_electrodes,
#             trode_id=1
#         )
#
#         self.nwbfile.add_acquisition(tetrode_series)
#
#         with NWBHDF5IO(self.path, mode='w') as io:
#             io.write(self.nwbfile)
#
#         with NWBHDF5IO(self.path, mode='r', load_namespaces=True) as io:
#             read_nwbfile = io.read()
#             self.assertContainerEqual(tetrode_series, read_nwbfile.acquisition['TetrodeSeries'])

#
# class TestTetrodeSeriesRoundtripPyNWB(AcquisitionH5IOMixin, TestCase):
#     """Complex, more complete roundtrip test for TetrodeSeries using pynwb.testing infrastructure."""
#
#     def setUpContainer(self):
#         """ Return the test TetrodeSeries to read/write """
#         self.device = Device(
#             name='device_name'
#         )
#
#         self.group = ElectrodeGroup(
#             name='electrode_group',
#             description='description',
#             location='location',
#             device=self.device
#         )
#
#         self.table = get_electrode_table()  # manually create a table of electrodes
#         for i in np.arange(10.):
#             self.table.add_row(
#                 x=i,
#                 y=i,
#                 z=i,
#                 imp=np.nan,
#                 location='location',
#                 filtering='filtering',
#                 group=self.group,
#                 group_name='electrode_group'
#             )
#
#         all_electrodes = DynamicTableRegion(
#             data=list(range(0, 10)),
#             description='all the electrodes',
#             name='electrodes',
#             table=self.table
#         )
#
#         data = np.random.rand(100, 3)
#         tetrode_series = TetrodeSeries(
#             name='name',
#             description='description',
#             data=data,
#             rate=1000.,
#             electrodes=all_electrodes,
#             trode_id=1
#         )
#         return tetrode_series
#
#     def addContainer(self, nwbfile):
#         """Add the test TetrodeSeries and related objects to the given NWBFile."""
#         nwbfile.add_device(self.device)
#         nwbfile.add_electrode_group(self.group)
#         nwbfile.set_electrode_table(self.table)
#         nwbfile.add_acquisition(self.container)
