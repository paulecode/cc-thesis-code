def calculate_duration(row, df):
    if row.velocity == 0:
        return 0
    else:
        return (df.loc[(df['note'] == row.note) & (df['velocity'] == 0) & (df['time'] > row.time)].iloc[0]['time'] - row.time)
