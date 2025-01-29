import json
import sys
from typing import Dict, Optional

import numpy as np
import pandas as pd

import mindsdb.utilities.profiler as profiler
from mindsdb.integrations.libs.base import BaseMLEngine

IS_PY36 = sys.version_info[1] <= 6


class NumpyJSONEncoder(json.JSONEncoder):
    """
    Use this encoder to avoid
    "TypeError: Object of type float32 is not JSON serializable"

    Example:
    x = np.float32(5)
    json.dumps(x, cls=NumpyJSONEncoder)
    """

    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, (np.float, np.float32, np.float64)):
            return float(obj)
        else:
            return super().default(obj)


class SQLPredictorHandler(BaseMLEngine):
    name = "sqlpredictor"

    @staticmethod
    def create_validation(target, args=None, **kwargs):
        if "df" not in kwargs:
            return
        df = kwargs["df"]
        columns = [x.lower() for x in df.columns]
        if target.lower() not in columns:
            raise Exception(f"There is no column '{target}' in dataframe")

        if (
            "timeseries_settings" in args
            and args["timeseries_settings"].get("is_timeseries") is True
        ):
            tss = args["timeseries_settings"]
            if "order_by" in tss and tss["order_by"].lower() not in columns:
                raise Exception(f"There is no column '{tss['order_by']}' in dataframe")
            if isinstance(tss.get("group_by"), list):
                for column in tss["group_by"]:
                    if column.lower() not in columns:
                        raise Exception(f"There is no column '{column}' in dataframe")

    @profiler.profile("SQLPredictor.create")
    def create(
        self,
        target: str,
        df: Optional[pd.DataFrame] = None,
        args: Optional[Dict] = None,
    ) -> None:
        pass

    @profiler.profile("SQLPredictor.finetune")
    def finetune(
        self, df: Optional[pd.DataFrame] = None, args: Optional[Dict] = None
    ) -> None:
        pass

    @profiler.profile("SQLPredictor.predict")
    def predict(self, df, args=None):
        pass

    def _get_features_info(self):
        pass

    def _get_model_info(self):
        pass

    def _get_ensemble_data(self):
        pass

    def _get_progress_data(self):
        pass

    def describe(self, attribute: Optional[str] = None) -> pd.DataFrame:
        return pd.DataFrame()
