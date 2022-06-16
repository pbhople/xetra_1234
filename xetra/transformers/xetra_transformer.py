""" Xetra ETL Component """
import logging
from typing import NamedTuple
from xetra.common.s3 import S3BucketConnector

class XetraSourceConfig(NamedTuple):

    """
    Class for source configuration data
    """

    src_first_extract_date: str
    src_columns: list
    src_col_date: str
    src_col_isin: str
    src_col_time: str
    src_col_start_price: str
    src_col_min_price: str
    src_col_max_price: str
    src_col_traded_vol: str

class XetraTargetConfig(NamedTuple):

    """
    Class for target configuration data
    """
    tgt_col_isin: str
    tgt_col_date: str
    tgt_col_op_price: str
    tgt_col_clos_price: str
    tgt_col_min_price: str
    tgt_col_max_price: str
    tgt_col_dail_trad_vol: str
    tgt_col_ch_prev_clos: str
    tgt_key: str
    tgt_key_date_format: str
    tgt_format: str

class XetraETL():

    """ Reads the Xetra data, transforms and writes the transformed data to target """

    def __init__(self, s3_bucket_src: S3BucketConnector, s3_bucket_tgt: S3BucketConnector, meta_key: str, src_args: XetraSourceConfig, tgt_args: XetraTargetConfig):


        """
        Constructor for XetraTransformer

        :param s3_bucket_src: connection to source S3 bucket
        :param s3_bucket_tgt: connection to target S3 bucket
        :param meta_key: used as self.meta_key -> key of meta file
        :param src_args: NamedTuple class with source configuration data
        :param tgt_args: NamedTuple class with target configuration data

        """
        
        self._logger = logging.getLogger(__name__)

        self.s3_bucket_src = s3_bucket_src
        self.s3_bucket_tgt = s3_bucket_tgt
        self.meta_key = meta_key
        self.src_args = src_args
        self.tgt_args = tgt_args
        self.extract_date = 
        self.extract_date_list = 
        self.meta_update_list = 

    def extract(self):
        pass

    def transform_report1(self):
        pass

    def load(self):
        pass

    def etl_report1(self):
        pass
