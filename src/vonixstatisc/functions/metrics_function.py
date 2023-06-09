from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    mean_absolute_percentage_error,
    r2_score,
    mean_squared_log_error,
)
from rich.console import Console
from rich.table import Table
import pandas as pd


class MetricFunctions:

    """All metrics that can be used to compare the fitnesse for different models or between models"""

    def __init__(self, agent, y_predict, y_true, total_features) -> None:
        self.mae = round(mean_absolute_error(y_true, y_predict), 3)
        self.rmse = round(mean_squared_error(y_true, y_predict, squared=True), 3)
        self.rmsle = round(mean_squared_log_error(y_true, y_predict), 3)
        self.mape = round(mean_absolute_percentage_error(y_true, y_predict), 3)
        self.r2_score = round(r2_score(y_true, y_predict), 4)
        self.r2_score_adjusted = round(
            1
            - ((1 - r2_score(y_true, y_predict)) * (len(y_predict) - 1))
            / (len(y_true) - total_features - 1),
            4,
        )
        self.agent = agent

    def return_metrics(self):
        """returning metrics results for dataframe"""

        return_dict = {
            "agent": self.agent,
            "mean_absolute_error": self.mae,
            "root_mean_squared_error": self.rmse,
            "root_mean_squared_log_error": self.rmsle,
            "mean_absolute_percentage_error": self.mape,
            "r2_score": self.r2_score,
            "r2_score_adj": self.r2_score_adjusted,
        }

        return pd.DataFrame(return_dict)

    def print_table(self):
        """Method for pretty logging of models metrics"""
        console = Console()

        table = Table(show_header=True, header_style="bold")
        table.add_column("agent_id", justify="center")
        table.add_column("mean_absolute_error", justify="center")
        table.add_column("root_mean_squared_error", justify="center")
        table.add_column("root_mean_squared_log_error", justify="center")
        table.add_column("mean_absolute_percentage_error", justify="center")
        table.add_column("r2_score", justify="center")
        table.add_column("r2_score_adj", justify="center")

        table.add_row(
            str(self.agent),
            str(self.mae),
            str(self.rmse),
            str(self.rmsle),
            str(self.mape),
            str(self.r2_score),
            str(self.r2_score_adjusted),
        )

        console.print(table)
