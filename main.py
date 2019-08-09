import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# plt.plot(x,y, label="First line")
# plt.plot(x2,y2, label="Second line")
# plt.legend()
# plt.show()

# hi

(pd.set_option("display.max_rows", None))
(pd.set_option("display.max_columns", None))
df = pd.read_csv("allscalesgeneratedmeans.csv")
# print(g.loc([[1]]))
g = df.groupby(["participant_code"])
for group in g:
    x = [0, 3, 6]

    df_grp = group[1]

    df_dqp = df_grp[df_grp.scale_type == "DQP"]
    # print(df_dqp)
    df_dqp.sort_values("booklet_type")
    y3 = list(df_dqp.choice_answer_value)
    # this will be Dqp

    df_dq = df_grp[df_grp.scale_type == "DQ"]
    print(df_dq)
    df_dq.sort_values("booklet_type")
    y2 = list(df_dq.choice_answer_value)

    df_badl = df_grp[df_grp.scale_type == "BADL"]
    print(df_badl)
    df_badl.sort_values("booklet_type")
    y = list(df_badl.choice_answer_value)

    df_eqp = df_grp[df_grp.scale_type == "EQP"]
    print(df_eqp)
    df_eqp.sort_values("booklet_type")
    y4 = list(df_eqp.choice_answer_value)
    print(y, y2, y3, y4)
    plt.xticks(np.arange(0, 9, step=3))
    if len(y) == 3:
        plt.plot(x, y, label="BADL")
    if len(y2) == 3:
        plt.plot(x, y2, label="DQ")
    if len(y3) == 3:
        plt.plot(x, y3, label="DQP")
    if len(y4) == 3:
            plt.plot(x, y4, label="EQP")
    plt.legend()
    plt.xlabel("timeline")
    plt.ylabel("average questionnaire answer")
    plt.show()

# print(group)
# print(g.mean())

# g.mean().to_csv("./allscalesgeneratedmeansgroupedreal.csv")
# g= df.groupby(["participant_code"])
