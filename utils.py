"""
Author: Muhammad Acqmal Fadhilla Latief 109632348+AcqmalFadhilla@users.noreply.github.com
Date: 2024-12-09 15:59:43
LastEditors: Muhammad Acqmal Fadhilla Latief 109632348+AcqmalFadhilla@users.noreply.github.com
LastEditTime: 2024-12-13 10:03:02
FilePath: utils.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""

    
def group_by(data, column: str):
    distribution = data.groupby(column).agg(
        Target_graduated=("Target", lambda x: (x == "Graduate").sum()),
        Target_dropout=("Target", lambda x: (x == "Dropout").sum()),
        Target_enrolled=("Target", lambda x: (x == "Enrolled").sum()),
    ).reset_index()
        
    return distribution
    
def melt(df_group_by, column: str):
    df_distribution = df_group_by.melt(
        id_vars=[column],
        value_vars=["Target_graduated", "Target_dropout", "Target_enrolled"],
        var_name="Target",
        value_name="Count"
    )
    return df_distribution

def avg_value(value1, value2):
    return (value1 + value2) / 2

def get_key(data, values):
    return [key for key, value in data.items() if value == values][0]