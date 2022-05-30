# фильтруем пользователей с кол-вом рук меньше 10, чтоб убрать шум
plhands=tbl.groupby(['PlayerID']).agg(
                {
                    'GameID': lambda x: x.nunique(),
                }).reset_index()
tbl0=tbl.merge(plhands, 'left', on='PlayerID', suffixes=('_rght', '_total'))
